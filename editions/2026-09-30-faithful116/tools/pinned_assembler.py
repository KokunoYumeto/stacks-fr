#!/usr/bin/env python3
"""Fail-closed validator and deterministic assembler for the 116-chapter reader.

The cumulative text is reconstructed from the exact standalone chapter sources
selected by twelve hash-bound report/manifest/master triads.  Flattened part
readers are consistency witnesses only.  The corpus-wide index is regenerated
in memory from all 116 selected sources.  Validation and self-test modes never
write final artifacts.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import os
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


SCRIPT = Path(__file__).resolve()
TASK_ROOT = SCRIPT.parent
EVIDENCE = TASK_ROOT / "evidence"
PROJECT_ROOT = SCRIPT.parents[2]
WORKSPACE_ROOT = SCRIPT.parents[7]
CONTRACT_PATH = EVIDENCE / "FINAL_CUMULATIVE_INPUT_CONTRACT.json"
VALIDATION_REPORT = EVIDENCE / "FINAL_CUMULATIVE_VALIDATE_INPUTS_REPORT.json"
EXPECTED_COMMIT = "a04446e57ec1fbc252a871afcec7752fb2807b14"
EXPECTED_CHAPTERS = list(range(1, 117))
STANDARD_LABELS = (
    "definition",
    "lemma",
    "proposition",
    "theorem",
    "remark",
    "remarks",
    "example",
    "exercise",
    "situation",
    "equation",
    "section",
    "subsection",
    "subsubsection",
    "item",
)


@dataclass(frozen=True)
class SelectedSource:
    part: int
    chapter: int | None
    stem: str
    path: Path | None
    recorded_path: str
    byte_count: int
    sha256: str
    title: str
    manifest_role: str
    text: str
    is_index: bool = False


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode(
        "utf-8"
    )


def recorded_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(WORKSPACE_ROOT.resolve()).as_posix()
    except ValueError as exc:
        raise ValueError("path is outside the authorized workspace") from exc


def resolve_recorded(value: Any) -> Path:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("path is missing or is not a nonempty string")
    candidate = Path(value)
    if not candidate.is_absolute():
        candidate = WORKSPACE_ROOT / candidate
    resolved = candidate.resolve()
    try:
        resolved.relative_to(WORKSPACE_ROOT.resolve())
    except ValueError as exc:
        raise ValueError("path resolves outside the authorized workspace") from exc
    return resolved


def resolve_with_base(value: Any, base_kind: str, spec: dict[str, Any]) -> Path:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("path is missing or is not a nonempty string")
    candidate = Path(value)
    if candidate.is_absolute():
        return resolve_recorded(value)
    if base_kind == "workspace-root":
        base = WORKSPACE_ROOT
    elif base_kind == "project-root":
        base = PROJECT_ROOT
    elif base_kind == "part-root":
        base = PROJECT_ROOT / str(spec["id"])
    else:
        raise ValueError(f"unsupported path base {base_kind!r}")
    resolved = (base / candidate).resolve()
    try:
        resolved.relative_to(WORKSPACE_ROOT.resolve())
    except ValueError as exc:
        raise ValueError("path resolves outside the authorized workspace") from exc
    return resolved


def is_under(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
            temporary = Path(handle.name)
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def atomic_write_set(payloads: list[tuple[Path, bytes]]) -> None:
    """Stage every byte stream, then install the report (commit marker) last."""

    if len({path.resolve() for path, _ in payloads}) != len(payloads):
        raise ValueError("atomic output set contains duplicate paths")
    existing = [path.exists() for path, _ in payloads]
    if any(existing):
        if not all(existing):
            raise ValueError("partial final output set already exists")
        if all(path.read_bytes() == data for path, data in payloads):
            return
        raise ValueError("a non-identical final output set already exists")

    staged: list[tuple[Path, Path, bytes]] = []
    installed: list[Path] = []
    try:
        for target, data in payloads:
            target.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(
                mode="wb",
                dir=target.parent,
                prefix=f".{target.name}.",
                suffix=".transaction.tmp",
                delete=False,
            ) as handle:
                handle.write(data)
                handle.flush()
                os.fsync(handle.fileno())
                staged.append((Path(handle.name), target, data))
        for temporary, target, _ in staged:
            os.replace(temporary, target)
            installed.append(target)
        for target, data in payloads:
            if target.read_bytes() != data:
                raise ValueError(f"atomic output readback mismatch: {recorded_path(target)}")
    except Exception:
        for target in installed:
            if target.exists():
                target.unlink()
        raise
    finally:
        for temporary, _, _ in staged:
            if temporary.exists():
                temporary.unlink()


def first_value(mapping: dict[str, Any], names: Iterable[str]) -> Any:
    for name in names:
        if name in mapping and mapping[name] not in (None, ""):
            return mapping[name]
    return None


def add_issue(target: dict[str, Any], code: str, detail: str) -> None:
    target.setdefault("issues", []).append({"code": code, "detail": detail})


def add_global_issue(issues: list[dict[str, str]], code: str, detail: str) -> None:
    issues.append({"code": code, "detail": detail})


def integer_value(value: Any) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def load_contract() -> dict[str, Any]:
    try:
        contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing input contract: {recorded_path(CONTRACT_PATH)}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid input contract JSON: {exc}") from exc
    if contract.get("schema") != "stacks-fr-final-cumulative-input-contract-v2":
        raise SystemExit("Unexpected cumulative input contract schema")
    if contract.get("frozen_upstream_commit") != EXPECTED_COMMIT:
        raise SystemExit("Input contract does not bind the required frozen commit")
    parts = contract.get("parts")
    if not isinstance(parts, list) or len(parts) != 12:
        raise SystemExit("Input contract must contain exactly twelve part entries")
    expected_start = 1
    for number, spec in enumerate(parts, start=1):
        if spec.get("part") != number or spec.get("id") != f"p{number:02d}":
            raise SystemExit("Input contract part identities are not canonical")
        if spec.get("chapter_start") != expected_start:
            raise SystemExit("Input contract chapter ranges are not contiguous")
        expected_start = int(spec.get("chapter_end", -1)) + 1
        binding = spec.get("binding")
        if binding not in {"stable", "pending_successor"}:
            raise SystemExit(f"Unsupported binding state for {spec['id']}: {binding!r}")
        if binding == "stable":
            for name in ("report", "manifest", "master"):
                if not isinstance(spec.get(name), dict):
                    raise SystemExit(f"Stable {spec['id']} lacks bound {name} identity")
            if not spec.get("report_schema") or not spec.get("selected_manifest_role"):
                raise SystemExit(f"Stable {spec['id']} lacks report/selector schema")
        else:
            if any(spec.get(name) is not None for name in ("report", "manifest", "master")):
                raise SystemExit(f"Pending {spec['id']} must not contain active artifact bindings")
    if expected_start != 117:
        raise SystemExit("Input contract does not cover Chapters 1-116")
    return contract


def validate_identity(
    item: dict[str, Any],
    issues: list[dict[str, str]],
    issue_prefix: str,
) -> Path | None:
    try:
        path = resolve_recorded(item.get("path"))
    except ValueError as exc:
        add_global_issue(issues, f"{issue_prefix}_path_invalid", str(exc))
        return None
    display = str(item.get("path"))
    if not path.is_file():
        add_global_issue(issues, f"{issue_prefix}_missing", display)
        return path
    expected_bytes = item.get("bytes")
    if not isinstance(expected_bytes, int) or path.stat().st_size != expected_bytes:
        add_global_issue(
            issues,
            f"{issue_prefix}_bytes_mismatch",
            f"{display}: expected {expected_bytes}, got {path.stat().st_size}",
        )
    expected_hash = str(item.get("sha256", "")).upper()
    actual_hash = sha256_path(path)
    if actual_hash != expected_hash:
        add_global_issue(
            issues,
            f"{issue_prefix}_hash_mismatch",
            f"{display}: expected {expected_hash}, got {actual_hash}",
        )
    return path


def validate_bound_identity(
    item: Any,
    result: dict[str, Any],
    artifact: str,
) -> Path | None:
    if not isinstance(item, dict):
        add_issue(result, f"{artifact}_binding_missing", str(item))
        return None
    try:
        path = resolve_recorded(item.get("path"))
    except ValueError as exc:
        add_issue(result, f"{artifact}_path_invalid", str(exc))
        return None
    result[f"{artifact}_exists"] = path.is_file()
    result[artifact] = item.get("path")
    if not path.is_file():
        add_issue(result, f"missing_{artifact}", str(item.get("path")))
        return path
    actual_bytes = path.stat().st_size
    actual_hash = sha256_path(path)
    result[f"{artifact}_bytes"] = actual_bytes
    result[f"{artifact}_sha256"] = actual_hash
    if integer_value(item.get("bytes")) != actual_bytes:
        add_issue(
            result,
            f"{artifact}_contract_bytes_mismatch",
            f"expected {item.get('bytes')}, got {actual_bytes}",
        )
    if str(item.get("sha256", "")).upper() != actual_hash:
        add_issue(
            result,
            f"{artifact}_contract_hash_mismatch",
            f"expected {item.get('sha256')}, got {actual_hash}",
        )
    return path


def effective_manifest_aliases(
    contract: dict[str, Any], spec: dict[str, Any]
) -> dict[str, list[str]]:
    aliases = {
        key: list(value)
        for key, value in contract["source_manifest_contract"]["field_aliases"].items()
    }
    for key, value in spec.get("manifest_field_aliases", {}).items():
        aliases[key] = list(value)
    return aliases


def normalize_manifest_row(
    row: dict[str, str], aliases: dict[str, list[str]]
) -> dict[str, str]:
    normalized = dict(row)
    for logical, choices in aliases.items():
        normalized[logical] = ""
        for field in choices:
            value = row.get(field, "")
            if value:
                normalized[logical] = value
                break
    return normalized


def parse_manifest(
    path: Path,
    contract: dict[str, Any],
    spec: dict[str, Any],
    part_result: dict[str, Any],
) -> list[dict[str, str]]:
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            fieldnames = reader.fieldnames or []
            rows = [dict(row) for row in reader]
    except (OSError, UnicodeError, csv.Error) as exc:
        add_issue(part_result, "manifest_parse_failed", exc.__class__.__name__)
        return []
    aliases = effective_manifest_aliases(contract, spec)
    for logical, choices in aliases.items():
        if not any(choice in fieldnames for choice in choices):
            add_issue(
                part_result,
                "manifest_header_missing_alias",
                f"{logical}: one of {choices}",
            )
    return [normalize_manifest_row(row, aliases) for row in rows]


def nonverbatim_lines(text: str) -> tuple[list[str], bool]:
    output: list[str] = []
    verbatim = False
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        if not verbatim and stripped.startswith("\\begin{verbatim}"):
            verbatim = True
            continue
        if verbatim:
            if stripped.startswith("\\end{verbatim}"):
                verbatim = False
            continue
        output.append(line)
    return output, verbatim


def nonverbatim_text(text: str) -> str:
    lines, unclosed = nonverbatim_lines(text)
    if unclosed:
        raise ValueError("unclosed verbatim environment")
    return "".join(lines)


def extract_braced_argument(line: str, command: str) -> str | None:
    match = re.match(rf"^\s*\\{re.escape(command)}\{{", line)
    if not match:
        return None
    open_index = match.end() - 1
    depth = 0
    for index in range(open_index, len(line)):
        char = line[index]
        if char == "{" and (index == 0 or line[index - 1] != "\\"):
            depth += 1
        elif char == "}" and (index == 0 or line[index - 1] != "\\"):
            depth -= 1
            if depth == 0:
                return line[open_index + 1 : index]
    return None


def command_arguments(text: str, command: str) -> list[str]:
    lines, unclosed = nonverbatim_lines(text)
    if unclosed:
        raise ValueError("unclosed verbatim environment")
    values: list[str] = []
    for line in lines:
        value = extract_braced_argument(line, command)
        if value is not None:
            values.append(value)
    return values


def nonverbatim_labels(text: str) -> list[str]:
    return re.findall(r"\\label\{([^{}]+)\}", nonverbatim_text(text))


def nonverbatim_refs(text: str) -> list[str]:
    return re.findall(r"\\ref\{([^{}]+)\}", nonverbatim_text(text))


def standalone_text_issues(text: str, stem: str) -> tuple[str | None, list[dict[str, str]]]:
    issues: list[dict[str, str]] = []
    try:
        visible = nonverbatim_text(text)
        titles = command_arguments(text, "title")
    except ValueError as exc:
        return None, [{"code": "unclosed_verbatim", "detail": str(exc)}]
    if len(titles) != 1:
        issues.append({"code": "standalone_title_count", "detail": str(len(titles))})
    wrappers = {
        "input_preamble": len(
            re.findall(r"^\s*\\input\s*\{preamble\}\s*$", visible, flags=re.MULTILINE)
        ),
        "begin_document": len(
            re.findall(r"^\s*\\begin\s*\{document\}\s*$", visible, flags=re.MULTILINE)
        ),
        "end_document": len(
            re.findall(r"^\s*\\end\s*\{document\}\s*$", visible, flags=re.MULTILINE)
        ),
        "input_chapters": len(
            re.findall(r"^\s*\\input\s*\{chapters\}\s*$", visible, flags=re.MULTILINE)
        ),
    }
    if wrappers != {
        "input_preamble": 1,
        "begin_document": 1,
        "end_document": 1,
        "input_chapters": 1,
    }:
        issues.append({"code": "standalone_wrapper_count", "detail": repr(wrappers)})
    bibliography = len(
        re.findall(r"^\s*\\bibliography\s*\{", visible, flags=re.MULTILINE)
    )
    bibliography_style = len(
        re.findall(r"^\s*\\bibliographystyle\s*\{", visible, flags=re.MULTILINE)
    )
    # Standalone historical sources are not uniform: a few legitimately carry
    # only ``\\bibliography`` and the FDL carries neither.  Repetition is the
    # unsafe shape; the cumulative tail supplies exactly one command of each.
    if bibliography > 1 or bibliography_style > 1:
        issues.append(
            {
                "code": "standalone_bibliography_count",
                "detail": f"bibliography={bibliography}, bibliographystyle={bibliography_style}",
            }
        )
    if command_arguments(text, "chapter"):
        issues.append({"code": "promoted_chapter_heading_in_source", "detail": stem})
    if command_arguments(text, "part"):
        issues.append({"code": "packaging_part_heading_in_source", "detail": stem})
    if re.search(r"\\(?:setcounter|addtocounter)\s*\{(?:part|chapter)\}", visible):
        issues.append({"code": "packaging_counter_in_source", "detail": stem})
    if "\\externaldocument" in visible or "xr-hyper" in visible:
        issues.append({"code": "external_document_machinery_in_source", "detail": stem})
    labels = re.findall(r"\\label\{([^{}]+)\}", visible)
    duplicates = sorted({label for label in labels if labels.count(label) > 1})
    if duplicates:
        issues.append({"code": "duplicate_source_labels", "detail": repr(duplicates[:5])})
    already_prefixed = [label for label in labels if label.startswith(f"{stem}-")]
    if already_prefixed:
        issues.append(
            {"code": "already_prefixed_source_labels", "detail": repr(already_prefixed[:5])}
        )
    return titles[0] if len(titles) == 1 else None, issues


def validate_standalone_source(
    source: Path,
    stem: str,
    report_output: Path | None,
    text: str,
    part_result: dict[str, Any],
    issue_context: str,
) -> str | None:
    if not is_under(source, PROJECT_ROOT):
        add_issue(part_result, "selected_source_outside_project", issue_context)
        return None
    if report_output is not None and source.resolve() == report_output.resolve():
        add_issue(part_result, "flattened_part_reader_selected", issue_context)
        return None
    if re.fullmatch(r"stacks_fr_(?:part\d+|complete.*)\.tex", source.name, re.IGNORECASE):
        add_issue(part_result, "flattened_reader_filename_selected", issue_context)
        return None
    title, issues = standalone_text_issues(text, stem)
    for issue in issues:
        add_issue(
            part_result,
            issue["code"],
            f"{issue_context}: {issue['detail']}",
        )
    return title


def report_artifact_identity(
    report: dict[str, Any], name: str
) -> tuple[Any, Any, Any]:
    value = report.get(name)
    if isinstance(value, dict):
        return value.get("path"), value.get("bytes"), value.get("sha256")
    return value, report.get(f"{name}_bytes"), report.get(f"{name}_sha256")


def validate_report_artifact_binding(
    report: dict[str, Any],
    name: str,
    bound_item: dict[str, Any],
    spec: dict[str, Any],
    result: dict[str, Any],
) -> Path | None:
    raw_path, raw_bytes, raw_hash = report_artifact_identity(report, name)
    try:
        path = resolve_with_base(raw_path, spec["report_path_base"], spec)
    except ValueError as exc:
        add_issue(result, f"report_{name}_path_invalid", str(exc))
        return None
    bound_path = resolve_recorded(bound_item["path"])
    if path != bound_path:
        add_issue(result, f"report_{name}_path_mismatch", spec["id"])
    if integer_value(raw_bytes) != integer_value(bound_item["bytes"]):
        add_issue(
            result,
            f"report_{name}_bytes_mismatch",
            f"expected {bound_item['bytes']}, got {raw_bytes}",
        )
    if str(raw_hash or "").upper() != str(bound_item["sha256"]).upper():
        add_issue(
            result,
            f"report_{name}_hash_mismatch",
            f"expected {bound_item['sha256']}, got {raw_hash}",
        )
    return path


def validate_selected_row(
    row: dict[str, str],
    spec: dict[str, Any],
    chapter: int,
    report_entry: dict[str, Any] | None,
    report_output: Path | None,
    part_result: dict[str, Any],
    contract: dict[str, Any],
) -> SelectedSource | None:
    part_number = int(spec["part"])
    context = f"{spec['id']}:{chapter}"
    stem = row.get("stem", "").strip()
    if not stem:
        add_issue(part_result, "selected_row_missing_stem", context)
        return None
    try:
        source = resolve_with_base(
            row.get("source_path"), spec["manifest_path_base"], spec
        )
    except ValueError as exc:
        add_issue(part_result, "selected_source_path_invalid", f"{context}: {exc}")
        return None
    expected_hash = row.get("source_sha256", "").upper()
    if not re.fullmatch(r"[0-9A-F]{64}", expected_hash):
        add_issue(part_result, "selected_source_hash_invalid", context)
        return None
    expected_bytes = integer_value(row.get("source_bytes"))
    if expected_bytes is None or expected_bytes < 1:
        add_issue(part_result, "selected_source_bytes_invalid", context)
        return None
    if not source.is_file():
        add_issue(part_result, "selected_source_missing", f"{context}: {recorded_path(source)}")
        return None
    raw = source.read_bytes()
    actual_bytes = len(raw)
    actual_hash = sha256_bytes(raw)
    if actual_bytes != expected_bytes:
        add_issue(
            part_result,
            "selected_source_bytes_mismatch",
            f"{context}: expected {expected_bytes}, got {actual_bytes}",
        )
    if actual_hash != expected_hash:
        add_issue(
            part_result,
            "selected_source_hash_mismatch",
            f"{context}: expected {expected_hash}, got {actual_hash}",
        )
    try:
        text = raw.decode("utf-8")
    except UnicodeError:
        add_issue(part_result, "selected_source_not_utf8", context)
        return None
    title = validate_standalone_source(
        source, stem, report_output, text, part_result, context
    )
    if title is None:
        return None

    report_contract = contract["terminal_report_contract"]
    if report_entry is None:
        add_issue(part_result, "report_chapter_entry_missing", context)
    else:
        report_stem = report_entry.get("stem")
        if report_stem != stem:
            add_issue(
                part_result,
                "report_manifest_stem_mismatch",
                f"{context}: report {report_stem!r}, manifest {stem!r}",
            )
        report_hash = first_value(report_entry, report_contract["chapter_hash_fields"])
        if str(report_hash).upper() != expected_hash:
            add_issue(
                part_result,
                "report_manifest_hash_mismatch",
                f"{context}: report {report_hash}, manifest {expected_hash}",
            )
        report_bytes = first_value(report_entry, report_contract["chapter_bytes_fields"])
        if integer_value(report_bytes) != expected_bytes:
            add_issue(
                part_result,
                "report_manifest_bytes_mismatch",
                f"{context}: report {report_bytes}, manifest {expected_bytes}",
            )
        report_source = first_value(report_entry, report_contract["chapter_source_fields"])
        if report_source is None:
            if part_number != 1:
                add_issue(part_result, "report_chapter_source_missing", context)
        else:
            try:
                resolved_report_source = resolve_with_base(
                    report_source, spec["report_path_base"], spec
                )
            except ValueError as exc:
                add_issue(
                    part_result,
                    "report_chapter_source_invalid",
                    f"{context}: {exc}",
                )
            else:
                if resolved_report_source != source:
                    add_issue(part_result, "report_manifest_source_mismatch", context)
    return SelectedSource(
        part=part_number,
        chapter=chapter,
        stem=stem,
        path=source,
        recorded_path=recorded_path(source),
        byte_count=actual_bytes,
        sha256=actual_hash,
        title=title,
        manifest_role=row.get("role", ""),
        text=text,
    )


def validate_part(
    spec: dict[str, Any], contract: dict[str, Any]
) -> tuple[dict[str, Any], list[SelectedSource], dict[str, Any] | None]:
    part_number = int(spec["part"])
    part_id = str(spec["id"])
    expected_numbers = list(range(int(spec["chapter_start"]), int(spec["chapter_end"]) + 1))
    result: dict[str, Any] = {
        "part": part_id,
        "binding": spec["binding"],
        "chapter_range": [expected_numbers[0], expected_numbers[-1]],
        "expected_chapter_numbers": expected_numbers,
        "selected_manifest_role": spec["selected_manifest_role"],
        "issues": [],
    }
    if spec["binding"] == "pending_successor":
        result.update(
            {
                "report": None,
                "manifest": None,
                "master": None,
                "report_exists": False,
                "manifest_exists": False,
                "master_exists": False,
                "validated_chapter_count": 0,
                "classification": "pending_successor",
            }
        )
        add_issue(result, "pending_successor_gate", spec.get("successor_gate", part_id))
        return result, [], None

    report_path = validate_bound_identity(spec["report"], result, "report")
    manifest_path = validate_bound_identity(spec["manifest"], result, "manifest")
    master_path = validate_bound_identity(spec["master"], result, "master")
    if not all(path is not None and path.is_file() for path in (report_path, manifest_path, master_path)):
        result["classification"] = "missing"
        result["validated_chapter_count"] = 0
        return result, [], None
    if result["issues"]:
        result["classification"] = "invalid"
        result["validated_chapter_count"] = 0
        return result, [], None

    assert report_path is not None
    assert manifest_path is not None
    assert master_path is not None
    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
    except (UnicodeError, json.JSONDecodeError) as exc:
        add_issue(result, "report_parse_failed", exc.__class__.__name__)
        result["classification"] = "invalid"
        result["validated_chapter_count"] = 0
        return result, [], None
    if not isinstance(report, dict):
        add_issue(result, "report_not_object", part_id)
        result["classification"] = "invalid"
        result["validated_chapter_count"] = 0
        return result, [], None

    report_contract = contract["terminal_report_contract"]
    for field in report_contract["required_top_level_fields"]:
        if field not in report:
            add_issue(result, "report_missing_required_field", field)
    if report.get("schema") != spec["report_schema"]:
        add_issue(
            result,
            "report_schema_mismatch",
            f"expected {spec['report_schema']!r}, got {report.get('schema')!r}",
        )
    observed_status = report.get("status")
    result["observed_status"] = observed_status
    if observed_status not in spec["accepted_report_statuses"]:
        add_issue(
            result,
            "report_status_not_terminal",
            f"expected one of {spec['accepted_report_statuses']}, got {observed_status!r}",
        )
    if report.get("pinned_commit") != EXPECTED_COMMIT:
        add_issue(
            result,
            "report_commit_mismatch",
            f"expected {EXPECTED_COMMIT}, got {report.get('pinned_commit')!r}",
        )
    if integer_value(report.get("chapter_count")) != len(expected_numbers):
        add_issue(
            result,
            "report_chapter_count_mismatch",
            f"expected {len(expected_numbers)}, got {report.get('chapter_count')!r}",
        )
    validate_report_artifact_binding(report, "source_manifest", spec["manifest"], spec, result)
    report_output = validate_report_artifact_binding(
        report, "output", spec["master"], spec, result
    )

    entries_value = report.get("chapters")
    entries = entries_value if isinstance(entries_value, list) else []
    if not isinstance(entries_value, list):
        add_issue(result, "report_chapters_not_list", part_id)
    report_entries: dict[int, dict[str, Any]] = {}
    report_order: list[int] = []
    for entry in entries:
        if not isinstance(entry, dict):
            add_issue(result, "report_chapter_entry_not_object", part_id)
            continue
        number = integer_value(first_value(entry, report_contract["chapter_number_fields"]))
        if number is None:
            add_issue(result, "report_chapter_number_invalid", part_id)
            continue
        if number in report_entries:
            add_issue(result, "report_duplicate_chapter", str(number))
            continue
        report_entries[number] = entry
        report_order.append(number)
    if report_order != expected_numbers:
        add_issue(
            result,
            "report_chapter_order_mismatch",
            f"expected {expected_numbers}, got {report_order}",
        )
    chapter_numbers_field = first_value(
        report, report_contract["chapter_number_list_fields"]
    )
    if chapter_numbers_field is not None:
        if chapter_numbers_field != expected_numbers:
            add_issue(
                result,
                "report_chapter_numbers_mismatch",
                f"expected {expected_numbers}, got {chapter_numbers_field}",
            )
    elif part_number != 1:
        add_issue(result, "report_chapter_numbers_missing", part_id)

    rows = parse_manifest(manifest_path, contract, spec, result)
    selected_role = spec["selected_manifest_role"]
    selected_rows: list[tuple[int, dict[str, str]]] = []
    for row in rows:
        if row.get("role") != selected_role:
            continue
        number = integer_value(row.get("chapter"))
        if number is None:
            add_issue(result, "selected_manifest_chapter_invalid", part_id)
            continue
        selected_rows.append((number, row))
    selected_order = [number for number, _ in selected_rows]
    if selected_order != expected_numbers:
        add_issue(
            result,
            "manifest_selected_chapter_order_mismatch",
            f"expected {expected_numbers}, got {selected_order}",
        )

    selected_sources: list[SelectedSource] = []
    for number in expected_numbers:
        candidates = [row for row_number, row in selected_rows if row_number == number]
        if len(candidates) != 1:
            add_issue(
                result,
                "manifest_selected_chapter_cardinality",
                f"chapter {number}: expected 1, got {len(candidates)}",
            )
            continue
        selected = validate_selected_row(
            candidates[0],
            spec,
            number,
            report_entries.get(number),
            report_output,
            result,
            contract,
        )
        if selected is not None:
            selected_sources.append(selected)

    result["validated_chapter_count"] = len(selected_sources)
    result["validated_chapters"] = [
        {
            "chapter": item.chapter,
            "stem": item.stem,
            "source": item.recorded_path,
            "bytes": item.byte_count,
            "sha256": item.sha256,
            "manifest_role": item.manifest_role,
            "source_title": item.title,
        }
        for item in selected_sources
    ]
    result["classification"] = "terminal_valid" if not result["issues"] else "invalid"
    return result, selected_sources, report


def transformed_preamble(path: Path) -> str:
    lines: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines(keepends=True):
        if line.startswith("%"):
            continue
        if "externaldocument" in line or "xr-hyper" in line:
            continue
        if line.startswith("\\IfFileExists{"):
            line = line.replace("stacks-project", "stacks-project-book")
        if line.startswith("\\documentclass"):
            line = line.replace("stacks-project", "stacks-project-book")
            line = line.replace("amsart", "amsbook")
        lines.append(line)
    result = "".join(lines)
    if "externaldocument" in result or "xr-hyper" in result:
        raise ValueError("external reference machinery survived preamble transformation")
    if "\\IfFileExists{stacks-project-book.cls}" not in result:
        raise ValueError("book-class selector is missing from transformed preamble")
    if "\\documentclass{stacks-project-book}" not in result:
        raise ValueError("primary book class is missing from transformed preamble")
    if "\\documentclass{amsbook}" not in result:
        raise ValueError("amsbook fallback is missing from transformed preamble")
    return result


def extract_gfdl(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"\\begin\{verbatim\}.*?\\end\{verbatim\}\s*", text, flags=re.DOTALL)
    if not match:
        raise ValueError("license source has no verbatim grant block")
    block = match.group(0)
    required = (
        "GNU Free Documentation License",
        "Version 1.2 or any later version",
        "no Invariant Sections",
        "no Front-Cover Texts",
        "no Back-Cover Texts",
    )
    missing = [fragment for fragment in required if fragment not in block]
    if missing:
        raise ValueError(f"license block is missing required fragments: {missing}")
    return block


def contributors_text(path: Path) -> str:
    contributors: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("%") or not raw.strip():
            continue
        contributors.append(re.sub(r"\s+\([^)]*\)\s*$", "", raw.rstrip()))
    if not contributors:
        raise ValueError("pinned contributor list is empty")
    return ", ".join(contributors) + "."


def attribution_blocks(contributors: str) -> tuple[str, str]:
    attribution = (
        "\\noindent\\textbf{Attribution.} Le texte mathématique original appartient au Stacks Project. "
        "Les personnes suivantes ont contribué à l'œuvre originale :\\par\n"
        + contributors
        + "\n"
        "\\noindent Les graphies CJK complémentaires du registre original sont conservées "
        "dans le fichier de provenance \\texttt{CONTRIBUTORS}, lié par empreinte au dossier de construction.\n"
    )
    non_endorsement = (
        "\\noindent\\textbf{Note sur la traduction.} Cette traduction française est indépendante. "
        "Elle n'est ni produite ni approuvée par les auteurs du Stacks Project. "
        "Toute erreur de traduction relève de cette édition française.\n"
    )
    return attribution, non_endorsement


def parse_navigation(text: str) -> tuple[list[tuple[str, str]], dict[str, str]]:
    entry_pattern = re.compile(
        r"\\item\s+\\hyperref\[([A-Za-z0-9-]+)-section-phantom\]\{([^{}\n]+)\}"
    )
    entries: list[tuple[str, str]] = []
    part_starts: dict[str, str] = {}
    pending_heading: str | None = None
    for line in text.splitlines():
        stripped = line.strip()
        if stripped and "\\" not in stripped:
            pending_heading = stripped
        match = entry_pattern.search(line)
        if match:
            stem, caption = match.groups()
            if pending_heading is not None:
                part_starts[stem] = pending_heading
                pending_heading = None
            entries.append((stem, caption))
    return entries, part_starts


def parse_makefile_order(text: str) -> list[str]:
    lines = text.splitlines()
    start = next((index for index, line in enumerate(lines) if line.startswith("LIJST = ")), None)
    if start is None:
        raise ValueError("pinned Makefile has no LIJST assignment")
    fragments: list[str] = []
    index = start
    while index < len(lines):
        line = lines[index].rstrip()
        continued = line.endswith("\\")
        if index == start:
            line = line[len("LIJST = ") :]
        line = line.rstrip("\\").strip()
        fragments.append(line)
        index += 1
        if not continued:
            break
    stems = " ".join(fragments).split()
    stems.append("fdl")
    return stems


def support_validation(
    contract: dict[str, Any],
    part_results: list[dict[str, Any]],
    reports: dict[int, dict[str, Any]],
) -> tuple[list[dict[str, str]], dict[str, Any]]:
    issues: list[dict[str, str]] = []
    support_paths: dict[str, Path] = {}
    partition = contract["partition_authority"]
    partition_path = validate_identity(partition, issues, "partition_authority")
    if partition_path is not None and partition_path.is_file():
        try:
            with partition_path.open("r", encoding="utf-8-sig", newline="") as handle:
                rows = list(csv.DictReader(handle))
        except (OSError, UnicodeError, csv.Error) as exc:
            add_global_issue(issues, "partition_parse_failed", exc.__class__.__name__)
        else:
            expected_ranges = {
                f"p{part['part']:02d}": (int(part["chapter_start"]), int(part["chapter_end"]))
                for part in contract["parts"]
            }
            observed: dict[str, tuple[int, int]] = {}
            for row in rows:
                match = re.match(r"^(\d+)-(\d+)", row.get("chapters", ""))
                if match:
                    observed[row.get("part", "")] = (int(match.group(1)), int(match.group(2)))
            if observed != expected_ranges:
                add_global_issue(
                    issues,
                    "partition_ranges_mismatch",
                    f"expected {expected_ranges}, got {observed}",
                )

    if isinstance(contract.get("inventory_authority"), dict):
        inventory_path = validate_identity(
            contract["inventory_authority"], issues, "inventory_authority"
        )
        if inventory_path is not None:
            support_paths["inventory-authority"] = inventory_path
    for item in contract["support_authorities"]:
        path = validate_identity(item, issues, f"support_{item['role']}")
        if path is not None:
            support_paths[item["role"]] = path

    derived: dict[str, Any] = {}
    required_support = {
        "preamble",
        "global-navigation",
        "license-source",
        "contributors",
        "upstream-chapter-order",
        "bibliography",
        "book-class",
        "upstream-index-rule",
        "upstream-reference-rule",
    }
    if required_support <= support_paths.keys() and all(
        support_paths[role].is_file() for role in required_support
    ):
        try:
            preamble = transformed_preamble(support_paths["preamble"])
            gfdl = extract_gfdl(support_paths["license-source"])
            contributors = contributors_text(support_paths["contributors"])
            attribution, non_endorsement = attribution_blocks(contributors)
            navigation = support_paths["global-navigation"].read_text(encoding="utf-8")
            navigation_entries, part_starts = parse_navigation(navigation)
            canonical_stems = parse_makefile_order(
                support_paths["upstream-chapter-order"].read_text(encoding="utf-8")
            )
        except (OSError, UnicodeError, ValueError) as exc:
            add_global_issue(issues, "derived_support_validation_failed", str(exc))
        else:
            book_contract = contract["generated_book_contract"]
            checks = (
                (
                    "transformed_preamble",
                    preamble.encode("utf-8"),
                    None,
                    book_contract["transformed_preamble_sha256"],
                ),
                (
                    "gfdl_block",
                    gfdl.encode("utf-8"),
                    book_contract["gfdl_block"]["bytes"],
                    book_contract["gfdl_block"]["sha256"],
                ),
                (
                    "attribution_block",
                    attribution.encode("utf-8"),
                    book_contract["attribution_block"]["bytes"],
                    book_contract["attribution_block"]["sha256"],
                ),
                (
                    "non_endorsement_block",
                    non_endorsement.encode("utf-8"),
                    book_contract["non_endorsement_block"]["bytes"],
                    book_contract["non_endorsement_block"]["sha256"],
                ),
            )
            for name, data, expected_bytes, expected_hash in checks:
                if expected_bytes is not None and len(data) != expected_bytes:
                    add_global_issue(
                        issues,
                        f"{name}_bytes_mismatch",
                        f"expected {expected_bytes}, got {len(data)}",
                    )
                actual_hash = sha256_bytes(data)
                if actual_hash != expected_hash:
                    add_global_issue(
                        issues,
                        f"{name}_hash_mismatch",
                        f"expected {expected_hash}, got {actual_hash}",
                    )
            navigation_stems = [stem for stem, _ in navigation_entries]
            if len(canonical_stems) != 116:
                add_global_issue(
                    issues,
                    "makefile_chapter_count",
                    f"expected 116, got {len(canonical_stems)}",
                )
            if len(navigation_entries) != 117:
                add_global_issue(
                    issues,
                    "navigation_entry_count",
                    f"expected 117, got {len(navigation_entries)}",
                )
            if navigation_stems[:116] != canonical_stems:
                add_global_issue(
                    issues,
                    "navigation_makefile_stem_order_mismatch",
                    "the 116 French navigation stems differ from pinned LIJST plus fdl",
                )
            expected_index_title = book_contract["global_index"]["title"]
            if not navigation_entries or navigation_entries[-1] != (
                "index",
                expected_index_title,
            ):
                add_global_issue(
                    issues,
                    "navigation_index_identity_mismatch",
                    f"expected ('index', {expected_index_title!r}), got {navigation_entries[-1:]}",
                )
            duplicates = sorted(
                {stem for stem in navigation_stems if navigation_stems.count(stem) > 1}
            )
            if duplicates:
                add_global_issue(issues, "navigation_duplicate_stems", repr(duplicates))
            derived = {
                "preamble": preamble,
                "gfdl": gfdl,
                "attribution": attribution,
                "non_endorsement": non_endorsement,
                "navigation": navigation,
                "navigation_entries": navigation_entries,
                "navigation_captions": dict(navigation_entries),
                "part_starts": part_starts,
                "canonical_stems": canonical_stems,
                "support_paths": support_paths,
            }

    p11 = reports.get(11)
    if p11 is not None and derived:
        book_contract = contract["generated_book_contract"]
        expected_report_values = {
            "gfdl_block_sha256": book_contract["gfdl_block"]["sha256"],
            "attribution_block_sha256": book_contract["attribution_block"]["sha256"],
            "non_endorsement_block_sha256": book_contract["non_endorsement_block"]["sha256"],
            "transformed_preamble_sha256": book_contract["transformed_preamble_sha256"],
        }
        for field, expected in expected_report_values.items():
            if str(p11.get(field, "")).upper() != expected:
                add_global_issue(
                    issues,
                    "part11_proven_block_mismatch",
                    f"{field}: expected {expected}, got {p11.get(field)!r}",
                )

    p01_result = next((item for item in part_results if item["part"] == "p01"), None)
    if p01_result and p01_result.get("manifest_exists"):
        p01_spec = contract["parts"][0]
        p01_manifest = resolve_recorded(p01_spec["manifest"]["path"])
        shadow: dict[str, Any] = {"issues": []}
        rows = parse_manifest(p01_manifest, contract, p01_spec, shadow)
        for issue in shadow["issues"]:
            add_global_issue(
                issues,
                "p01_support_manifest_invalid",
                f"{issue['code']}: {issue['detail']}",
            )
        directly_bound_roles = {
            "preamble",
            "global-navigation",
            "bibliography",
            "license-source",
            "contributors",
            "book-class",
            "upstream-assembly-rule",
            "upstream-reference-rule",
        }
        for authority in contract["support_authorities"]:
            if authority["role"] not in directly_bound_roles:
                continue
            authority_path = resolve_recorded(authority["path"])
            matches = []
            for row in rows:
                raw_path = row.get("source_path")
                if not raw_path:
                    continue
                try:
                    row_path = resolve_with_base(
                        raw_path, p01_spec["manifest_path_base"], p01_spec
                    )
                except ValueError:
                    continue
                if (
                    row_path == authority_path
                    and row.get("source_sha256", "").upper() == authority["sha256"]
                ):
                    matches.append(row)
            if len(matches) != 1:
                add_global_issue(
                    issues,
                    "p01_support_binding_cardinality",
                    f"{authority['role']}: expected 1, got {len(matches)}",
                )
    return issues, derived


def find_balanced(text: str, opening: int) -> int:
    depth = 0
    for index in range(opening, len(text)):
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
            if depth == 0:
                return index
    raise ValueError("unbalanced brace clause")


def find_label(text: str) -> str:
    start = text.find("\\label{")
    if start < 0:
        return ""
    opening = start + len("\\label")
    closing = find_balanced(text, opening)
    return text[opening + 1 : closing]


def find_defined_terms(text: str) -> list[str]:
    terms: list[str] = []
    start = text.find("{\\it ")
    while start >= 0:
        closing = find_balanced(text, start)
        terms.append(text[start : closing + 1])
        start = text.find("{\\it ", closing)
    return terms


def generate_corpus_index(
    sources: list[SelectedSource], title: str, require_full: bool = True
) -> tuple[SelectedSource, dict[str, Any]]:
    if require_full and (
        len(sources) != 116
        or [source.chapter for source in sources] != EXPECTED_CHAPTERS
    ):
        raise ValueError("corpus-wide index requires exactly Chapters 1-116")
    terms: list[tuple[str, str]] = []
    definitions: list[tuple[list[str], str]] = []
    titles: list[str] = []
    definitions_by_stem: dict[str, int] = {}
    for source in sources:
        titles.append(source.title)
        count = 0
        # The pinned generator's logical unit is a definition environment.  A
        # few French sources compact a complete environment onto one line, so
        # scan the same begin/end tokens independent of physical line layout.
        visible = nonverbatim_text(source.text)
        cursor = 0
        begin_token = "\\begin{definition}"
        end_token = "\\end{definition}"
        while True:
            beginning = visible.find(begin_token, cursor)
            if beginning < 0:
                break
            ending = visible.find(end_token, beginning + len(begin_token))
            if ending < 0:
                raise ValueError(f"unclosed definition in {source.recorded_path}")
            definition_text = visible[beginning : ending + len(end_token)]
            label = find_label(definition_text)
            if not label:
                raise ValueError(f"definition without label in {source.recorded_path}")
            full_label = f"{source.stem}-{label}"
            defined = find_defined_terms(definition_text)
            definitions.append((defined, full_label))
            terms.extend((term, full_label) for term in defined)
            count += 1
            cursor = ending + len(end_token)
        definitions_by_stem[source.stem] = count

    out: list[str] = []

    def emit(value: str = "") -> None:
        out.append(value + "\n")

    emit("\\input{preamble}")
    emit("\\begin{document}")
    emit(f"\\title{{{title}}}")
    emit("\\maketitle")
    emit()
    emit("\\phantomsection")
    emit("\\label{section-phantom}")
    emit()
    emit("\\tableofcontents")
    emit()
    emit("\\frenchspacing")
    emit()
    emit()
    emit("\\begin{multicols}{2}[\\section{Définitions par ordre alphabétique}\\label{section-alphabetized}]")
    for term, label in sorted(terms, key=lambda item: item[0].lower()):
        emit("\\noindent")
        emit(term)
        emit(f"in \\ref{{{label}}}")
        emit()
    emit("\\end{multicols}")
    emit()
    emit("\\begin{multicols}{2}[\\section{Définitions classées par chapitre}\\label{section-per-chapter}]")
    definition_index = 0
    for source, chapter_title in zip(sources, titles):
        emit()
        emit("\\medskip\\noindent")
        emit("{\\bf " + chapter_title + "}")
        emit()
        emit("\\medskip")
        while (
            definition_index < len(definitions)
            and definitions[definition_index][1].startswith(
                source.stem + "-definition"
            )
        ):
            defined, label = definitions[definition_index]
            emit()
            emit("\\noindent")
            emit(f"In \\ref{{{label}}}: ")
            for term_index, term in enumerate(defined):
                emit(term + ("," if term_index + 1 < len(defined) else ""))
            emit()
            definition_index += 1
    if definition_index != len(definitions):
        raise ValueError("generated index did not emit every collected definition")
    emit("\\end{multicols}")
    emit()
    emit("\\input{chapters}")
    emit("\\end{document}")
    text = "".join(out)
    title_check, issues = standalone_text_issues(text, "index")
    if issues or title_check != title:
        raise ValueError(f"generated index standalone shape failed: {issues}")
    raw = text.encode("utf-8")
    selected = SelectedSource(
        part=0,
        chapter=None,
        stem="index",
        path=None,
        recorded_path="[generated-in-memory:corpus-wide-index]",
        byte_count=len(raw),
        sha256=sha256_bytes(raw),
        title=title,
        manifest_role="generated-corpus-index",
        text=text,
        is_index=True,
    )
    metadata = {
        "source_chapter_count": len(sources),
        "source_chapter_numbers": [source.chapter for source in sources],
        "source_stems": [source.stem for source in sources],
        "source_title_count": len(titles),
        "definitions_found": len(definitions),
        "definitions_emitted": definition_index,
        "alphabetized_term_occurrences": len(terms),
        "definitions_by_stem": definitions_by_stem,
        "title": title,
        "raw_bytes": len(raw),
        "raw_sha256": sha256_bytes(raw),
    }
    return selected, metadata


def title_caption_differences(
    sources: list[SelectedSource], derived: dict[str, Any]
) -> list[dict[str, Any]]:
    captions: dict[str, str] = derived.get("navigation_captions", {})
    differences: list[dict[str, Any]] = []
    for source in sources:
        caption = captions.get(source.stem)
        if caption is None:
            continue
        if source.title != caption:
            differences.append(
                {
                    "chapter": source.chapter,
                    "stem": source.stem,
                    "source_title": source.title,
                    "source_title_sha256": sha256_bytes(source.title.encode("utf-8")),
                    "navigation_caption": caption,
                    "navigation_caption_sha256": sha256_bytes(caption.encode("utf-8")),
                }
            )
    return differences


def validate_inputs(contract: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    part_results: list[dict[str, Any]] = []
    selected_by_part: dict[int, list[SelectedSource]] = {}
    reports: dict[int, dict[str, Any]] = {}
    for spec in contract["parts"]:
        result, sources, report = validate_part(spec, contract)
        part_number = int(spec["part"])
        part_results.append(result)
        selected_by_part[part_number] = sources
        if report is not None:
            reports[part_number] = report

    global_issues, derived = support_validation(contract, part_results, reports)
    terminal_parts = [
        result["part"] for result in part_results if result["classification"] == "terminal_valid"
    ]
    pending_parts = [
        result["part"]
        for result in part_results
        if result["classification"] == "pending_successor"
    ]
    missing_parts = [
        {
            "part": result["part"],
            "missing": [
                name
                for name in ("report", "manifest", "master")
                if not result.get(f"{name}_exists", False)
            ],
        }
        for result in part_results
        if result["classification"] == "missing"
    ]
    invalid_parts = [
        {
            "part": result["part"],
            "classification": result["classification"],
            "issues": result["issues"],
        }
        for result in part_results
        if result["classification"] == "invalid"
    ]
    all_sources = [
        source
        for part in range(1, 13)
        for source in selected_by_part.get(part, [])
        if next(
            item["classification"]
            for item in part_results
            if item["part"] == f"p{part:02d}"
        )
        == "terminal_valid"
    ]
    differences = title_caption_differences(all_sources, derived) if derived else []
    generated_index: SelectedSource | None = None
    index_metadata: dict[str, Any] | None = None
    assembly_preflight: dict[str, Any] | None = None
    global_sequence_validated = False
    if len(terminal_parts) == 12 and not global_issues:
        numbers = [source.chapter for source in all_sources]
        if numbers != EXPECTED_CHAPTERS:
            add_global_issue(
                global_issues,
                "global_chapter_sequence_mismatch",
                f"expected 1-116, got {numbers}",
            )
        paths = [source.path.resolve() for source in all_sources if source.path is not None]
        if len(set(paths)) != len(paths):
            add_global_issue(
                global_issues,
                "global_duplicate_source_paths",
                "selected chapter source paths are not unique",
            )
        source_stems = [source.stem for source in all_sources]
        if source_stems != derived.get("canonical_stems"):
            add_global_issue(
                global_issues,
                "global_makefile_stem_order_mismatch",
                "selected chapter stems differ from pinned LIJST plus fdl",
            )
        expected_difference_chapters = contract["generated_book_contract"][
            "expected_title_caption_difference_chapters"
        ]
        actual_difference_chapters = [item["chapter"] for item in differences]
        if actual_difference_chapters != expected_difference_chapters:
            add_global_issue(
                global_issues,
                "title_caption_difference_set_mismatch",
                f"expected {expected_difference_chapters}, got {actual_difference_chapters}",
            )
        try:
            generated_index, index_metadata = generate_corpus_index(
                all_sources,
                contract["generated_book_contract"]["global_index"]["title"],
            )
        except ValueError as exc:
            add_global_issue(global_issues, "global_index_generation_failed", str(exc))
        if generated_index is not None and not global_issues:
            try:
                preview_tex, preview_transforms, preview_structural = assemble_once(
                    all_sources, generated_index, derived
                )
            except ValueError as exc:
                add_global_issue(
                    global_issues,
                    "cumulative_in_memory_preflight_failed",
                    str(exc),
                )
            else:
                assembly_preflight = {
                    "tex_bytes": len(preview_tex),
                    "tex_sha256": sha256_bytes(preview_tex),
                    "transform_count": len(preview_transforms),
                    "structural_validation": preview_structural,
                    "files_written": False,
                }
        global_sequence_validated = not global_issues and generated_index is not None

    ready = len(terminal_parts) == 12 and global_sequence_validated
    blockers: list[str] = []
    for part in pending_parts:
        blockers.append(f"{part}: pending successor report/manifest/master binding")
    for item in missing_parts:
        blockers.append(f"{item['part']}: missing {', '.join(item['missing'])}")
    for item in invalid_parts:
        codes = ", ".join(issue["code"] for issue in item["issues"])
        blockers.append(f"{item['part']}: invalid ({codes})")
    for issue in global_issues:
        blockers.append(f"global: {issue['code']} ({issue['detail']})")

    output_policy = contract["output_policy"]
    final_paths = {
        name: resolve_recorded(output_policy[name])
        for name in ("final_tex", "final_source_manifest", "final_report")
    }
    report = {
        "schema": "stacks-fr-final-cumulative-validation-report-v2",
        "mode": "validate-inputs",
        "status": "READY" if ready else "REFUSED_INPUTS_INCOMPLETE",
        "ready": ready,
        "frozen_upstream_commit": EXPECTED_COMMIT,
        "assembler": recorded_path(SCRIPT),
        "assembler_sha256": sha256_path(SCRIPT),
        "input_contract": recorded_path(CONTRACT_PATH),
        "input_contract_sha256": sha256_path(CONTRACT_PATH),
        "inventory_authority": contract.get("inventory_authority"),
        "parts": part_results,
        "summary": {
            "expected_parts": [f"p{number:02d}" for number in range(1, 13)],
            "terminal_valid_parts": terminal_parts,
            "pending_successor_parts": pending_parts,
            "missing_parts": missing_parts,
            "invalid_parts": invalid_parts,
            "blocking_part_ids": [
                result["part"]
                for result in part_results
                if result["classification"] != "terminal_valid"
            ],
            "validated_terminal_chapter_count": len(all_sources),
            "expected_chapter_count": 116,
            "global_chapter_sequence_validated": global_sequence_validated,
            "global_index_generated_in_memory": generated_index is not None,
            "title_caption_difference_count": len(differences),
            "title_caption_difference_chapters": [
                item["chapter"] for item in differences
            ],
        },
        "title_caption_differences": differences,
        "global_index_preview": index_metadata,
        "cumulative_in_memory_preflight": assembly_preflight,
        "support_and_global_issues": global_issues,
        "blockers": blockers,
        "write_policy": {
            "validation_report_written": True,
            "final_tex_written": False,
            "final_source_manifest_written": False,
            "final_report_written": False,
            "final_artifacts_existing_before_validation": {
                name: path.exists() for name, path in final_paths.items()
            },
            "gate": output_policy["gate"],
        },
    }
    context = {
        "selected_by_part": selected_by_part,
        "all_sources": all_sources,
        "derived": derived,
        "reports": reports,
        "part_results": part_results,
        "generated_index": generated_index,
        "global_index_metadata": index_metadata,
        "assembly_preflight": assembly_preflight,
        "title_caption_differences": differences,
    }
    return report, context


def transform_source(source: SelectedSource) -> tuple[str, dict[str, int]]:
    output: list[str] = []
    verbatim = False
    intro_license_blocks = 0
    counts = {
        "labels_prefixed": 0,
        "local_refs_prefixed": 0,
        "titles_promoted": 0,
        "directives_removed": 0,
        "intro_license_blocks_suppressed": 0,
        "unicode_apostrophes_normalized": 0,
    }
    for original_line in source.text.splitlines(keepends=True):
        line = original_line
        stripped = line.lstrip()
        if stripped.startswith("\\begin{verbatim}"):
            verbatim = True
            if source.stem == "introduction":
                intro_license_blocks += 1
                counts["intro_license_blocks_suppressed"] += 1
                continue
        if verbatim:
            if source.stem != "introduction":
                output.append(line)
            if stripped.startswith("\\end{verbatim}"):
                verbatim = False
            continue

        apostrophe_hits = line.count("’")
        if apostrophe_hits:
            line = line.replace("’", "'")
            counts["unicode_apostrophes_normalized"] += apostrophe_hits
        stripped = line.lstrip()
        if re.match(r"^\\input\s*\{preamble\}", stripped):
            counts["directives_removed"] += 1
            continue
        if re.match(r"^\\begin\s*\{document\}", stripped):
            counts["directives_removed"] += 1
            continue
        if re.match(r"^\\title\{", stripped):
            line = line.replace("\\title{", "\\chapter{", 1)
            counts["titles_promoted"] += 1
        if re.match(r"^\\maketitle\b", stripped):
            counts["directives_removed"] += 1
            continue
        if re.match(r"^\\tableofcontents\b", stripped):
            counts["directives_removed"] += 1
            continue
        if re.match(r"^\\input\s*\{chapters\}", stripped):
            counts["directives_removed"] += 1
            continue
        if re.match(r"^\\bibliography(?:style)?\s*\{", stripped):
            counts["directives_removed"] += 1
            continue
        if re.match(r"^\\end\s*\{document\}", stripped):
            counts["directives_removed"] += 1
            continue

        for label in re.findall(r"\\label\{([^{}]+)\}", line):
            if label.startswith(f"{source.stem}-"):
                raise ValueError(
                    f"source {source.recorded_path} already contains prefixed label {label}"
                )
        label_hits = line.count("\\label{")
        if label_hits:
            line = line.replace("\\label{", f"\\label{{{source.stem}-")
            counts["labels_prefixed"] += label_hits
        for standard in STANDARD_LABELS:
            old = f"\\ref{{{standard}-"
            hits = line.count(old)
            if hits:
                line = line.replace(old, f"\\ref{{{source.stem}-{standard}-")
                counts["local_refs_prefixed"] += hits
        output.append(line)
    if verbatim:
        raise ValueError(f"unclosed verbatim environment in {source.recorded_path}")
    if counts["titles_promoted"] != 1:
        raise ValueError(f"title promotion failed in {source.recorded_path}")
    if source.stem == "introduction" and intro_license_blocks != 1:
        raise ValueError("the introduction must contain exactly one suppressed GFDL grant block")
    transformed = "".join(output)
    visible = nonverbatim_text(transformed)
    forbidden_patterns = {
        "input-preamble": r"^\s*\\input\s*\{preamble\}",
        "begin-document": r"^\s*\\begin\s*\{document\}",
        "maketitle": r"^\s*\\maketitle\b",
        "tableofcontents": r"^\s*\\tableofcontents\b",
        "input-chapters": r"^\s*\\input\s*\{chapters\}",
        "bibliography": r"^\s*\\bibliography\s*\{",
        "bibliographystyle": r"^\s*\\bibliographystyle\s*\{",
        "end-document": r"^\s*\\end\s*\{document\}",
        "externaldocument": r"^\s*\\externaldocument\b",
        "xr-hyper": r"^\s*\\usepackage(?:\[[^]]*\])?\s*\{xr-hyper\}",
    }
    survivors = [
        name
        for name, pattern in forbidden_patterns.items()
        if re.search(pattern, visible, flags=re.MULTILINE)
    ]
    if survivors:
        raise ValueError(
            f"standalone directives survived in {source.recorded_path}: {survivors}"
        )
    headings = command_arguments(transformed, "chapter")
    if headings != [source.title]:
        raise ValueError(f"chapter title changed while transforming {source.recorded_path}")
    labels = nonverbatim_labels(transformed)
    duplicates = sorted({label for label in labels if labels.count(label) > 1})
    if duplicates:
        raise ValueError(
            f"duplicate labels survived in {source.recorded_path}: {duplicates[:3]}"
        )
    bad_labels = [label for label in labels if not label.startswith(f"{source.stem}-")]
    if bad_labels:
        raise ValueError(
            f"unprefixed labels survived in {source.recorded_path}: {bad_labels[:3]}"
        )
    for standard in STANDARD_LABELS:
        if f"\\ref{{{standard}-" in visible:
            raise ValueError(
                f"unprefixed local {standard} reference survived in {source.recorded_path}"
            )
    return transformed, counts


def validate_assembled(
    assembled: str,
    all_inputs: list[SelectedSource],
    transforms: list[dict[str, Any]],
    derived: dict[str, Any],
) -> dict[str, Any]:
    visible = nonverbatim_text(assembled)
    begin_count = len(
        re.findall(r"^\s*\\begin\s*\{document\}\s*$", visible, flags=re.MULTILINE)
    )
    end_count = len(
        re.findall(r"^\s*\\end\s*\{document\}\s*$", visible, flags=re.MULTILINE)
    )
    if (begin_count, end_count) != (1, 1):
        raise ValueError(
            f"assembled source has repeated/missing document wrappers: {(begin_count, end_count)}"
        )
    bibliography_count = len(
        re.findall(r"^\s*\\bibliography\s*\{", visible, flags=re.MULTILINE)
    )
    bibliography_style_count = len(
        re.findall(r"^\s*\\bibliographystyle\s*\{", visible, flags=re.MULTILINE)
    )
    if (bibliography_count, bibliography_style_count) != (1, 1):
        raise ValueError("assembled source must have exactly one bibliography tail")
    if "\\externaldocument" in visible or "xr-hyper" in visible:
        raise ValueError("external-document machinery survived final assembly")
    if re.search(r"\\(?:setcounter|addtocounter)\s*\{(?:part|chapter)\}", visible):
        raise ValueError("packaging part/chapter counters survived final assembly")
    for directive in ("\\input{preamble}", "\\input{chapters}", "\\maketitle"):
        if directive in visible:
            raise ValueError(f"standalone directive survived final assembly: {directive}")

    headings = command_arguments(assembled, "chapter")
    expected_headings = [source.title for source in all_inputs]
    if headings != expected_headings:
        raise ValueError("assembled chapter/index heading order differs from source titles")
    if len(headings) != 117 or len([item for item in all_inputs if item.is_index]) != 1:
        raise ValueError("assembled source must contain 116 chapters and one generated index")
    if not all_inputs[-1].is_index or all_inputs[-1].stem != "index":
        raise ValueError("the generated index is not the final heading")
    expected_parts = list(derived["part_starts"].values())
    observed_parts = command_arguments(assembled, "part")
    if observed_parts != expected_parts:
        raise ValueError("canonical topical part topology differs from navigation")
    navigation_count = assembled.count(derived["navigation"])
    if navigation_count != 117:
        raise ValueError(
            f"full navigation block must occur 117 times, got {navigation_count}"
        )
    for block_name in ("gfdl", "attribution", "non_endorsement"):
        if assembled.count(derived[block_name]) != 1:
            raise ValueError(f"{block_name} block is not present exactly once")

    labels = nonverbatim_labels(assembled)
    label_set = set(labels)
    if len(labels) != len(label_set):
        duplicates = sorted({label for label in labels if labels.count(label) > 1})
        raise ValueError(f"duplicate globally prefixed labels: {duplicates[:10]}")
    expected_label_count = sum(item["labels_prefixed"] for item in transforms)
    if len(labels) != expected_label_count:
        raise ValueError("assembled label count differs from transform totals")
    stems = [source.stem for source in all_inputs]
    invalid_labels = [
        label for label in labels if not any(label.startswith(f"{stem}-") for stem in stems)
    ]
    if invalid_labels:
        raise ValueError(f"labels without canonical stem prefix: {invalid_labels[:10]}")
    refs = nonverbatim_refs(assembled)
    unresolved_refs = sorted({target for target in refs if target not in label_set})
    if unresolved_refs:
        raise ValueError(f"unresolved references in full reader: {unresolved_refs[:20]}")
    for standard in STANDARD_LABELS:
        if any(target.startswith(f"{standard}-") for target in refs):
            raise ValueError(f"unprefixed local {standard} reference survived")
    navigation_targets = [
        f"{stem}-section-phantom" for stem, _ in derived["navigation_entries"]
    ]
    missing_navigation_targets = [target for target in navigation_targets if target not in label_set]
    if missing_navigation_targets:
        raise ValueError(
            f"navigation targets without labels: {missing_navigation_targets[:20]}"
        )
    return {
        "document_boundaries": {"begin_document": 1, "end_document": 1},
        "chapter_headings": 116,
        "index_headings": 1,
        "canonical_part_headings": observed_parts,
        "navigation_blocks": navigation_count,
        "navigation_entries_per_block": 117,
        "bibliography_tails": 1,
        "packaging_part_or_chapter_counters": 0,
        "external_document_directives": 0,
        "labels_total": len(labels),
        "labels_unique": len(label_set),
        "refs_total": len(refs),
        "refs_resolved": len(refs),
        "unresolved_refs": [],
    }


def assemble_once(
    sources: list[SelectedSource],
    index_source: SelectedSource,
    derived: dict[str, Any],
) -> tuple[bytes, list[dict[str, Any]], dict[str, Any]]:
    front = [
        derived["preamble"],
        "\\begin{document}\n",
        "\\begin{titlepage}\n",
        "\\pagestyle{empty}\n",
        "\\setcounter{page}{1}\n",
        "\\centerline{\\LARGE\\bfseries Le projet Stacks}\n",
        "\\vskip0.35in\n",
        "\\centerline{\\Large Édition française cumulative}\n",
        "\\vskip0.35in\n",
        f"\\centerline{{Traduction française de la révision \\texttt{{{EXPECTED_COMMIT}}}}}\n",
        "\\vskip0.5in\n",
        derived["attribution"],
        "\\vskip0.35in\n",
        derived["non_endorsement"],
        "\\end{titlepage}\n",
        derived["gfdl"],
        "\\tableofcontents\n",
    ]
    blocks: list[str] = []
    transforms: list[dict[str, Any]] = []
    all_inputs = sources + [index_source]
    captions = derived["navigation_captions"]
    for source in all_inputs:
        if source.stem in derived["part_starts"]:
            blocks.append(f"\\part{{{derived['part_starts'][source.stem]}}}\n")
        transformed, counts = transform_source(source)
        blocks.append(transformed + "\n" + derived["navigation"] + "\n")
        caption = captions[source.stem]
        transforms.append(
            {
                "part": source.part,
                "chapter": source.chapter,
                "is_index": source.is_index,
                "stem": source.stem,
                "source_title": source.title,
                "source_title_sha256": sha256_bytes(source.title.encode("utf-8")),
                "navigation_caption": caption,
                "navigation_caption_sha256": sha256_bytes(caption.encode("utf-8")),
                "title_caption_equal": source.title == caption,
                "source": source.recorded_path,
                "input_bytes": source.byte_count,
                "input_sha256": source.sha256,
                "transformed_bytes": len(transformed.encode("utf-8")),
                "transformed_sha256": sha256_bytes(transformed.encode("utf-8")),
                **counts,
            }
        )
    tail = "\\bibliography{my}\n\\bibliographystyle{amsalpha}\n\\end{document}\n"
    assembled = ("".join(front) + "".join(blocks) + tail).encode("utf-8")
    structural = validate_assembled(
        assembled.decode("utf-8"), all_inputs, transforms, derived
    )
    return assembled, transforms, structural


def serialize_final_manifest(
    contract: dict[str, Any],
    sources: list[SelectedSource],
    index_source: SelectedSource,
    derived: dict[str, Any],
) -> bytes:
    rows: list[dict[str, Any]] = []
    for spec in contract["parts"]:
        for role, field in (
            ("part-report", "report"),
            ("part-source-manifest", "manifest"),
            ("part-master-witness", "master"),
        ):
            item = spec[field]
            rows.append(
                {
                    "role": role,
                    "part": spec["id"],
                    "chapter": "",
                    "stem": "",
                    "path": item["path"],
                    "bytes": item["bytes"],
                    "sha256": item["sha256"],
                    "source_title": "",
                    "navigation_caption": "",
                }
            )
    captions = derived["navigation_captions"]
    for source in sources + [index_source]:
        rows.append(
            {
                "role": "generated-corpus-index"
                if source.is_index
                else "terminal-chapter-source",
                "part": "" if source.is_index else f"p{source.part:02d}",
                "chapter": "" if source.chapter is None else source.chapter,
                "stem": source.stem,
                "path": source.recorded_path,
                "bytes": source.byte_count,
                "sha256": source.sha256,
                "source_title": source.title,
                "navigation_caption": captions[source.stem],
            }
        )
    for authority in contract["support_authorities"]:
        rows.append(
            {
                "role": authority["role"],
                "part": "",
                "chapter": "",
                "stem": "",
                "path": authority["path"],
                "bytes": authority["bytes"],
                "sha256": authority["sha256"],
                "source_title": "",
                "navigation_caption": "",
            }
        )
    extra = [
        ("partition-authority", contract["partition_authority"]),
        ("assembler", {"path": recorded_path(SCRIPT), "bytes": SCRIPT.stat().st_size, "sha256": sha256_path(SCRIPT)}),
        ("input-contract", {"path": recorded_path(CONTRACT_PATH), "bytes": CONTRACT_PATH.stat().st_size, "sha256": sha256_path(CONTRACT_PATH)}),
    ]
    if isinstance(contract.get("inventory_authority"), dict):
        extra.insert(1, ("input-inventory-revision", contract["inventory_authority"]))
    for role, item in extra:
        rows.append(
            {
                "role": role,
                "part": "",
                "chapter": "",
                "stem": "",
                "path": item["path"],
                "bytes": item["bytes"],
                "sha256": item["sha256"],
                "source_title": "",
                "navigation_caption": "",
            }
        )
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(
        buffer,
        fieldnames=(
            "role",
            "part",
            "chapter",
            "stem",
            "path",
            "bytes",
            "sha256",
            "source_title",
            "navigation_caption",
        ),
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def bound_file_snapshot(
    contract: dict[str, Any], sources: list[SelectedSource]
) -> dict[str, tuple[Path, int, str]]:
    paths: list[Path] = []
    for spec in contract["parts"]:
        for field in ("report", "manifest", "master"):
            paths.append(resolve_recorded(spec[field]["path"]))
    paths.append(resolve_recorded(contract["partition_authority"]["path"]))
    paths.extend(resolve_recorded(item["path"]) for item in contract["support_authorities"])
    if isinstance(contract.get("inventory_authority"), dict):
        paths.append(resolve_recorded(contract["inventory_authority"]["path"]))
    paths.extend(source.path for source in sources if source.path is not None)
    snapshot: dict[str, tuple[Path, int, str]] = {}
    for path in paths:
        key = recorded_path(path)
        identity = (path, path.stat().st_size, sha256_path(path))
        if key in snapshot and snapshot[key][1:] != identity[1:]:
            raise ValueError(f"conflicting snapshot identity for {key}")
        snapshot[key] = identity
    return snapshot


def verify_snapshot(snapshot: dict[str, tuple[Path, int, str]]) -> None:
    for key, (path, expected_bytes, expected_hash) in snapshot.items():
        observed = (path.stat().st_size, sha256_path(path))
        if observed != (expected_bytes, expected_hash):
            raise ValueError(f"bound input changed during assembly: {key}")


def assembly_report_object(
    contract: dict[str, Any],
    assembled: bytes,
    manifest: bytes,
    transforms: list[dict[str, Any]],
    structural: dict[str, Any],
    derived: dict[str, Any],
    index_metadata: dict[str, Any],
    output_path: Path,
    manifest_path: Path,
) -> dict[str, Any]:
    return {
        "schema": "stacks-fr-final-cumulative-assembly-report-v2",
        "status": "PASS",
        "frozen_upstream_commit": EXPECTED_COMMIT,
        "assembler": recorded_path(SCRIPT),
        "assembler_sha256": sha256_path(SCRIPT),
        "input_contract": recorded_path(CONTRACT_PATH),
        "input_contract_sha256": sha256_path(CONTRACT_PATH),
        "inventory_authority": contract.get("inventory_authority"),
        "part_count": 12,
        "part_artifacts": [
            {
                "part": spec["id"],
                "report": spec["report"],
                "manifest": spec["manifest"],
                "master_witness": spec["master"],
                "report_schema": spec["report_schema"],
                "accepted_report_statuses": spec["accepted_report_statuses"],
                "selected_manifest_role": spec["selected_manifest_role"],
            }
            for spec in contract["parts"]
        ],
        "chapter_count": 116,
        "chapter_numbers": EXPECTED_CHAPTERS,
        "chapters": transforms[:-1],
        "index": {**transforms[-1], **index_metadata},
        "title_caption_difference_chapters": [
            item["chapter"] for item in transforms[:-1] if not item["title_caption_equal"]
        ],
        "output": recorded_path(output_path),
        "output_bytes": len(assembled),
        "output_sha256": sha256_bytes(assembled),
        "source_manifest": recorded_path(manifest_path),
        "source_manifest_bytes": len(manifest),
        "source_manifest_sha256": sha256_bytes(manifest),
        "structural_validation": structural,
        "gfdl_block_sha256": sha256_bytes(derived["gfdl"].encode("utf-8")),
        "attribution_block_sha256": sha256_bytes(derived["attribution"].encode("utf-8")),
        "non_endorsement_block_sha256": sha256_bytes(
            derived["non_endorsement"].encode("utf-8")
        ),
        "navigation_sha256": sha256_bytes(derived["navigation"].encode("utf-8")),
        "deterministic_replay": {
            "passes": 2,
            "tex_bytes_identical": True,
            "tex_sha256_pass_1": sha256_bytes(assembled),
            "tex_sha256_pass_2": sha256_bytes(assembled),
            "manifest_bytes_identical": True,
            "manifest_sha256_pass_1": sha256_bytes(manifest),
            "manifest_sha256_pass_2": sha256_bytes(manifest),
            "report_serializations_identical": True,
        },
        "source_chapters_unchanged": True,
        "all_part_masters_bound_as_witnesses": True,
        "flattened_part_readers_consumed": False,
        "part12_scoped_index_consumed": False,
        "corpus_index_generated_in_memory": True,
        "tex_or_render_invoked": False,
        "git_invoked": False,
        "publication_invoked": False,
    }


def assemble_final(
    contract: dict[str, Any],
    validation_report: dict[str, Any],
    context: dict[str, Any],
) -> dict[str, Any]:
    if not validation_report["ready"]:
        raise ValueError("assembly called while validation gate is closed")
    sources: list[SelectedSource] = context["all_sources"]
    derived: dict[str, Any] = context["derived"]
    if [source.chapter for source in sources] != EXPECTED_CHAPTERS:
        raise ValueError("assembly source sequence is not exactly Chapters 1-116")
    snapshot = bound_file_snapshot(contract, sources)
    index_1, index_metadata_1 = generate_corpus_index(
        sources, contract["generated_book_contract"]["global_index"]["title"]
    )
    assembled_1, transforms_1, structural_1 = assemble_once(sources, index_1, derived)
    index_2, index_metadata_2 = generate_corpus_index(
        sources, contract["generated_book_contract"]["global_index"]["title"]
    )
    assembled_2, transforms_2, structural_2 = assemble_once(sources, index_2, derived)
    if index_1 != index_2 or index_metadata_1 != index_metadata_2:
        raise ValueError("deterministic replay produced different index bytes/metadata")
    if assembled_1 != assembled_2:
        raise ValueError("deterministic replay produced different cumulative TeX bytes")
    if transforms_1 != transforms_2 or structural_1 != structural_2:
        raise ValueError("deterministic replay produced different transform metadata")
    manifest_1 = serialize_final_manifest(contract, sources, index_1, derived)
    manifest_2 = serialize_final_manifest(contract, sources, index_2, derived)
    if manifest_1 != manifest_2:
        raise ValueError("deterministic replay produced different source manifests")
    verify_snapshot(snapshot)

    output_policy = contract["output_policy"]
    output_path = resolve_recorded(output_policy["final_tex"])
    manifest_path = resolve_recorded(output_policy["final_source_manifest"])
    report_path = resolve_recorded(output_policy["final_report"])
    report_1 = assembly_report_object(
        contract,
        assembled_1,
        manifest_1,
        transforms_1,
        structural_1,
        derived,
        index_metadata_1,
        output_path,
        manifest_path,
    )
    report_2 = assembly_report_object(
        contract,
        assembled_2,
        manifest_2,
        transforms_2,
        structural_2,
        derived,
        index_metadata_2,
        output_path,
        manifest_path,
    )
    report_data_1 = json_bytes(report_1)
    report_data_2 = json_bytes(report_2)
    if report_data_1 != report_data_2:
        raise ValueError("deterministic replay produced different assembly reports")
    verify_snapshot(snapshot)
    atomic_write_set(
        [
            (output_path, assembled_1),
            (manifest_path, manifest_1),
            (report_path, report_data_1),
        ]
    )
    return report_1


def negative_structural_selftests() -> dict[str, str]:
    base = (
        "\\input{preamble}\n\\begin{document}\n\\title{T}\n\\maketitle\n"
        "\\phantomsection\n\\label{section-phantom}\n\\tableofcontents\n"
        "\\input{chapters}\n\\bibliography{my}\n\\bibliographystyle{amsalpha}\n"
        "\\end{document}\n"
    )
    negative_cases = {
        "repeated_wrapper": (
            base.replace("\\begin{document}\n", "\\begin{document}\n\\begin{document}\n"),
            "standalone_wrapper_count",
        ),
        "repeated_bibliography": (
            base.replace("\\bibliography{my}\n", "\\bibliography{my}\n\\bibliography{my}\n"),
            "standalone_bibliography_count",
        ),
        "packaging_counter": (
            base.replace("\\title{T}\n", "\\title{T}\n\\setcounter{part}{7}\n"),
            "packaging_counter_in_source",
        ),
        "external_document": (
            base.replace("\\title{T}\n", "\\title{T}\n\\externaldocument{x}\n"),
            "external_document_machinery_in_source",
        ),
        "duplicate_label": (
            base.replace(
                "\\phantomsection\n",
                "\\phantomsection\n\\label{definition-x}\n\\label{definition-x}\n",
            ),
            "duplicate_source_labels",
        ),
    }
    results: dict[str, str] = {}
    for name, (text, expected_code) in negative_cases.items():
        _, issues = standalone_text_issues(text, "fixture")
        codes = {issue["code"] for issue in issues}
        if expected_code not in codes:
            raise ValueError(f"negative structural selftest failed for {name}: {codes}")
        results[name] = expected_code
    return results


def run_selftest(contract: dict[str, Any]) -> dict[str, Any]:
    final_paths = [
        resolve_recorded(contract["output_policy"][name])
        for name in ("final_tex", "final_source_manifest", "final_report")
    ]
    final_before = {recorded_path(path): path.exists() for path in final_paths}
    if any(final_before.values()):
        raise ValueError("selftest requires the final output set to be absent")
    report_1, context_1 = validate_inputs(contract)
    report_2, _ = validate_inputs(contract)
    if json_bytes(report_1) != json_bytes(report_2):
        raise ValueError("validation serialization is not deterministic")
    sources: list[SelectedSource] = context_1["all_sources"]
    for source in sources:
        if source.path is None:
            raise ValueError("a chapter source has no file path")
        if (source.path.stat().st_size, sha256_path(source.path)) != (
            source.byte_count,
            source.sha256,
        ):
            raise ValueError(f"exact source hash selftest failed: {source.recorded_path}")
    dependency_roles = {item["role"] for item in contract["support_authorities"]}
    if not {"book-class", "bibliography", "upstream-index-rule"} <= dependency_roles:
        raise ValueError("required dependency bindings are absent")
    negative_results = negative_structural_selftests()

    if not report_1["ready"]:
        expected_pending = [
            spec["id"]
            for spec in contract["parts"]
            if spec.get("binding") == "pending_successor"
        ]
        actual_blocking = report_1["summary"]["blocking_part_ids"]
        if not expected_pending or actual_blocking != expected_pending:
            raise ValueError(
                "live contract has blockers other than its explicit pending successors: "
                + repr(report_1["blockers"])
            )
        for spec in contract["parts"]:
            if spec["id"] in expected_pending and any(
                spec.get(name) is not None for name in ("report", "manifest", "master")
            ):
                raise ValueError(
                    f"{spec['id']}: pending successor still exposes an active triad"
                )
        final_after = {recorded_path(path): path.exists() for path in final_paths}
        if final_before != final_after or any(final_after.values()):
            raise ValueError("selftest created a forbidden final artifact")
        result = {
            "schema": "stacks-fr-final-cumulative-selftest-v1",
            "status": "PASS_PENDING_INPUTS",
            "assembler_sha256": sha256_path(SCRIPT),
            "input_contract_sha256": sha256_path(CONTRACT_PATH),
            "live_contract_ready": False,
            "live_terminal_parts": report_1["summary"]["terminal_valid_parts"],
            "live_exact_source_hashes_verified": len(sources),
            "pending_gate": {
                "status": report_1["status"],
                "blocking_part_ids": actual_blocking,
                "blockers": report_1["blockers"],
                "active_triads_null": True,
                "final_artifacts_written": False,
            },
            "full_corpus_checks": "deferred until all twelve exact successor triads are terminal",
            "dependency_bindings_verified": [
                "bibliography", "book-class", "upstream-index-rule"
            ],
            "negative_structural_cases": negative_results,
            "validation_serializations_identical": True,
            "final_artifacts_written": False,
        }
        if json_bytes(result) != json_bytes(copy.deepcopy(result)):
            raise ValueError("selftest report serialization is not deterministic")
        return result
    if report_1["summary"]["validated_terminal_chapter_count"] != 116:
        raise ValueError("selftest did not bind exactly 116 source chapters")

    simulated = copy.deepcopy(contract)
    for spec in simulated["parts"]:
        if spec["id"] in {"p08", "p09"}:
            spec["binding"] = "pending_successor"
            spec["report"] = None
            spec["manifest"] = None
            spec["master"] = None
            spec["successor_gate"] = "selftest simulated pending successor"
    pending_report, _ = validate_inputs(simulated)
    if pending_report["ready"]:
        raise ValueError("pending-successor simulation did not fail closed")
    if pending_report["summary"]["blocking_part_ids"] != ["p08", "p09"]:
        raise ValueError(
            "pending-successor simulation did not isolate p08/p09: "
            + repr(pending_report["summary"]["blocking_part_ids"])
        )

    expected_differences = contract["generated_book_contract"][
        "expected_title_caption_difference_chapters"
    ]
    actual_differences = report_1["summary"]["title_caption_difference_chapters"]
    if actual_differences != expected_differences:
        raise ValueError("source-title/navigation-caption selftest failed")
    index_source: SelectedSource | None = context_1["generated_index"]
    index_metadata = context_1["global_index_metadata"]
    if index_source is None or index_metadata is None:
        raise ValueError("global index was not generated in memory")
    if index_metadata["source_chapter_count"] != 116:
        raise ValueError("global index source cardinality is not 116")
    if command_arguments(index_source.text, "title") != [
        contract["generated_book_contract"]["global_index"]["title"]
    ]:
        raise ValueError("global index title cardinality failed")
    dry_tex_1, dry_transforms_1, dry_structural_1 = assemble_once(
        sources, index_source, context_1["derived"]
    )
    replay_index, replay_index_metadata = generate_corpus_index(
        sources, contract["generated_book_contract"]["global_index"]["title"]
    )
    dry_tex_2, dry_transforms_2, dry_structural_2 = assemble_once(
        sources, replay_index, context_1["derived"]
    )
    if (
        dry_tex_1 != dry_tex_2
        or dry_transforms_1 != dry_transforms_2
        or dry_structural_1 != dry_structural_2
        or index_metadata != replay_index_metadata
    ):
        raise ValueError("two-pass in-memory cumulative dry run is not deterministic")
    dry_manifest_1 = serialize_final_manifest(
        contract, sources, index_source, context_1["derived"]
    )
    dry_manifest_2 = serialize_final_manifest(
        contract, sources, replay_index, context_1["derived"]
    )
    if dry_manifest_1 != dry_manifest_2:
        raise ValueError("two-pass in-memory manifest dry run is not deterministic")
    final_after = {recorded_path(path): path.exists() for path in final_paths}
    if final_before != final_after or any(final_after.values()):
        raise ValueError("selftest created a forbidden final artifact")
    result = {
        "schema": "stacks-fr-final-cumulative-selftest-v1",
        "status": "PASS",
        "assembler_sha256": sha256_path(SCRIPT),
        "input_contract_sha256": sha256_path(CONTRACT_PATH),
        "live_contract_ready": True,
        "live_terminal_parts": report_1["summary"]["terminal_valid_parts"],
        "live_exact_source_hashes_verified": len(sources),
        "pending_p08_p09_simulation": {
            "status": pending_report["status"],
            "blocking_part_ids": pending_report["summary"]["blocking_part_ids"],
            "final_artifacts_written": False,
        },
        "title_caption_difference_chapters": actual_differences,
        "global_index": {
            "source_chapter_count": index_metadata["source_chapter_count"],
            "raw_bytes": index_source.byte_count,
            "raw_sha256": index_source.sha256,
            "definitions_found": index_metadata["definitions_found"],
            "alphabetized_term_occurrences": index_metadata[
                "alphabetized_term_occurrences"
            ],
        },
        "in_memory_assembly_dry_run": {
            "passes": 2,
            "tex_bytes": len(dry_tex_1),
            "tex_sha256": sha256_bytes(dry_tex_1),
            "source_manifest_bytes": len(dry_manifest_1),
            "source_manifest_sha256": sha256_bytes(dry_manifest_1),
            "structural_validation": dry_structural_1,
            "serializations_identical": True,
            "files_written": False,
        },
        "dependency_bindings_verified": [
            "bibliography", "book-class", "upstream-index-rule"
        ],
        "negative_structural_cases": negative_results,
        "validation_serializations_identical": True,
        "final_artifacts_written": False,
    }
    if json_bytes(result) != json_bytes(copy.deepcopy(result)):
        raise ValueError("selftest report serialization is not deterministic")
    return result


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fail-closed validator and gated assembler for the complete "
            "116-chapter French Stacks reader."
        )
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--validate-inputs",
        action="store_true",
        help="Validate all exact bindings and write only the deterministic validation report.",
    )
    mode.add_argument(
        "--selftest",
        action="store_true",
        help="Run bounded in-memory positive/negative tests and write no files.",
    )
    mode.add_argument(
        "--assemble",
        action="store_true",
        help="Assemble once only after the same validation proves every gate.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    contract = load_contract()
    if args.selftest:
        try:
            result = run_selftest(contract)
        except ValueError as exc:
            print(
                json.dumps(
                    {"status": "FAIL", "error": str(exc), "files_written": False},
                    ensure_ascii=False,
                    indent=2,
                    sort_keys=True,
                )
            )
            return 1
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 0

    validation_report, context = validate_inputs(contract)
    atomic_write(VALIDATION_REPORT, json_bytes(validation_report))
    if not validation_report["ready"]:
        concise = {
            "status": validation_report["status"],
            "validation_report": recorded_path(VALIDATION_REPORT),
            "validation_report_sha256": sha256_path(VALIDATION_REPORT),
            "blocking_part_ids": validation_report["summary"]["blocking_part_ids"],
            "blockers": validation_report["blockers"],
            "final_artifacts_written": False,
        }
        print(json.dumps(concise, ensure_ascii=False, indent=2, sort_keys=True))
        return 2
    if args.validate_inputs:
        print(
            json.dumps(
                {
                    "status": "READY",
                    "validation_report": recorded_path(VALIDATION_REPORT),
                    "validation_report_sha256": sha256_path(VALIDATION_REPORT),
                    "final_artifacts_written": False,
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
        )
        return 0
    try:
        final_report = assemble_final(contract, validation_report, context)
    except ValueError as exc:
        print(
            json.dumps(
                {
                    "status": "REFUSED_ASSEMBLY_GATE",
                    "error": str(exc),
                    "final_artifacts_written": False,
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
        )
        return 3
    print(
        json.dumps(
            {
                "status": final_report["status"],
                "output": final_report["output"],
                "output_sha256": final_report["output_sha256"],
                "source_manifest": final_report["source_manifest"],
                "source_manifest_sha256": final_report["source_manifest_sha256"],
                "final_report": contract["output_policy"]["final_report"],
                "final_report_sha256": sha256_path(
                    resolve_recorded(contract["output_policy"]["final_report"])
                ),
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
