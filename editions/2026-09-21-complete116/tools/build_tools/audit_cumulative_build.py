#!/usr/bin/env python3
"""Deterministic, file-only audit for the guarded cumulative Stacks build."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


TRUE_BANG_ERROR = re.compile(
    r"^!\s*(?:"
    r"(?:LaTeX|Package\s+\S+|Class\s+\S+|pdfTeX)\s+Error\b|"
    r"Undefined control sequence\b|Emergency stop\b|Fatal error\b|"
    r"TeX capacity exceeded\b|Runaway argument\b|File ended while scanning\b|"
    r"Paragraph ended before\b|Missing\s+.+?\s+inserted\b|Extra\s+.+|"
    r"Misplaced\s+.+|Improper\s+.+|Bad math environment delimiter\b|"
    r"Display math should end\b|You can't use\b|I can't\b|"
    r"Use of\s+.+?doesn't match\b|Argument of\s+.+?has an extra\b"
    r")",
    re.IGNORECASE,
)
BOX_TRACE_FONT = re.compile(
    r"\\(?:OT1|T1|TS1|OML|OMS|OMX|U)/[^\s]+|\[\]",
    re.IGNORECASE,
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def file_record(path: Path) -> dict[str, Any]:
    return {
        "path": str(path.resolve()),
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
    }


def read_latin1(path: Path) -> str:
    return path.read_bytes().decode("latin-1", errors="replace")


def compact(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def parse_tex_output_summary(log_text: str, expected_pdf_name: str) -> dict[str, Any]:
    """Parse pdfTeX's summary even when TeX wraps inside numeric fields."""
    flattened = compact(log_text)
    pattern = re.compile(
        r"Output\s+written\s+on\s+"
        r"(?P<pdf>.+?\.pdf)\s*"
        r"\(\s*(?P<pages>[0-9][0-9,\s]*?)\s+pages?\s*,\s*"
        r"(?P<bytes>[0-9][0-9,\s]*?)\s+bytes?\s*\)\s*\.?",
        re.IGNORECASE,
    )
    candidates: list[dict[str, Any]] = []
    for match in pattern.finditer(flattened):
        pdf_text = compact(match.group("pdf"))
        pdf_basename = Path(pdf_text.replace("\\", "/")).name
        pages_digits = re.sub(r"[^0-9]", "", match.group("pages"))
        bytes_digits = re.sub(r"[^0-9]", "", match.group("bytes"))
        if not pages_digits or not bytes_digits:
            continue
        candidates.append(
            {
                "pdf_text": pdf_text,
                "pdf_basename": pdf_basename,
                "pages": int(pages_digits),
                "bytes": int(bytes_digits),
                "normalized_summary": match.group(0),
            }
        )
    matching = [c for c in candidates if c["pdf_basename"].lower() == expected_pdf_name.lower()]
    if not matching:
        raise ValueError(
            f"No TeX output summary found for {expected_pdf_name}; candidates={candidates[-3:]}"
        )
    return matching[-1]


def matching_excerpts(text: str, patterns: list[str]) -> list[str]:
    excerpts: list[str] = []
    seen: set[str] = set()
    for pattern in patterns:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE | re.MULTILINE):
            excerpt = compact(match.group(0))[:1000]
            if excerpt not in seen:
                excerpts.append(excerpt)
                seen.add(excerpt)
    return excerpts


def run_selftest() -> int:
    fixtures = [
        (
            "Output written on stacks_fr_complete_116.pdf (1 page, 42 bytes).",
            1,
            42,
        ),
        (
            "Output written on stacks_fr_complete_116.pdf (12\n345 pages, 987\n654 bytes).",
            12345,
            987654,
        ),
        (
            "Output written on\n stacks_fr_complete_116.pdf\n (20 001 pages,\n 123 456 789 bytes)\n.",
            20001,
            123456789,
        ),
    ]
    results: list[dict[str, Any]] = []
    for text, expected_pages, expected_bytes in fixtures:
        parsed = parse_tex_output_summary(text, "stacks_fr_complete_116.pdf")
        ok = parsed["pages"] == expected_pages and parsed["bytes"] == expected_bytes
        results.append(
            {
                "expected_pages": expected_pages,
                "expected_bytes": expected_bytes,
                "parsed_pages": parsed["pages"],
                "parsed_bytes": parsed["bytes"],
                "pass": ok,
            }
        )
    missing_summary_rejected = False
    try:
        parse_tex_output_summary("No pages of output.", "stacks_fr_complete_116.pdf")
    except ValueError:
        missing_summary_rejected = True
    font_trace = r"! []\OT1/lmr/m/n/10 (\OML/lmm/m/it/10 M; N)"
    real_error = r"! Undefined control sequence."
    unfamiliar = r"! unfamiliar diagnostic"
    bang_classifier = {
        "font_trace_not_error": bool(BOX_TRACE_FONT.search(font_trace))
        and not bool(TRUE_BANG_ERROR.search(font_trace)),
        "explicit_error_detected": bool(TRUE_BANG_ERROR.search(real_error)),
        "unfamiliar_is_not_silently_classified": not bool(BOX_TRACE_FONT.search(unfamiliar))
        and not bool(TRUE_BANG_ERROR.search(unfamiliar)),
    }
    status = (
        all(item["pass"] for item in results)
        and missing_summary_rejected
        and all(bang_classifier.values())
    )
    print(
        json.dumps(
            {
                "schema": "final-cumulative-build-auditor-selftest-v1",
                "status": "PASS" if status else "FAIL",
                "fixtures": results,
                "missing_summary_rejected": missing_summary_rejected,
                "bang_classifier": bang_classifier,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if status else 2


def audit(args: argparse.Namespace) -> int:
    build_dir = Path(args.build_dir).resolve()
    job = args.jobname
    paths = {
        "pdf": build_dir / f"{job}.pdf",
        "log": build_dir / f"{job}.log",
        "fls": build_dir / f"{job}.fls",
        "aux": build_dir / f"{job}.aux",
        "bbl": build_dir / f"{job}.bbl",
        "blg": build_dir / f"{job}.blg",
        "fdb_latexmk": build_dir / f"{job}.fdb_latexmk",
        "latexmk_stdout": build_dir / "latexmk.stdout.log",
        "latexmk_stderr": build_dir / "latexmk.stderr.log",
    }
    required = ("pdf", "log", "fls", "aux", "bbl")
    artifacts: dict[str, Any] = {}
    for name, path in paths.items():
        artifacts[name] = file_record(path) if path.is_file() else {"path": str(path), "missing": True}

    missing_required = [name for name in required if not paths[name].is_file()]
    empty_required = [
        name for name in required if paths[name].is_file() and paths[name].stat().st_size == 0
    ]

    log_text = read_latin1(paths["log"]) if paths["log"].is_file() else ""
    fls_text = read_latin1(paths["fls"]) if paths["fls"].is_file() else ""
    aux_text = read_latin1(paths["aux"]) if paths["aux"].is_file() else ""
    bbl_text = read_latin1(paths["bbl"]) if paths["bbl"].is_file() else ""
    blg_text = read_latin1(paths["blg"]) if paths["blg"].is_file() else ""

    summary: dict[str, Any] | None = None
    summary_error: str | None = None
    if log_text:
        try:
            summary = parse_tex_output_summary(log_text, f"{job}.pdf")
        except ValueError as exc:
            summary_error = str(exc)

    true_bang_errors: list[str] = []
    font_box_traces: list[str] = []
    unclassified_bang_lines: list[str] = []
    for line in log_text.splitlines():
        if not re.match(r"^!\s+", line):
            continue
        if TRUE_BANG_ERROR.search(line):
            true_bang_errors.append(line[:1000])
        elif BOX_TRACE_FONT.search(line):
            font_box_traces.append(line[:1000])
        else:
            unclassified_bang_lines.append(line[:1000])
    fatal_errors = true_bang_errors + unclassified_bang_lines
    fatal_errors.extend(
        matching_excerpts(
            log_text,
            [
                r"\bEmergency stop\b",
                r"\bFatal error occurred\b",
                r"\bNo pages of output\b",
                r"\b(?:LaTeX|Package|Class|pdfTeX) Error\b[^\r\n]*",
            ],
        )
    )
    fatal_errors = list(dict.fromkeys(fatal_errors))
    undefined_references = matching_excerpts(
        log_text,
        [
            r"LaTeX Warning:\s+(?:Hyper\s+)?Reference[\s\S]{0,1000}?undefined",
            r"There were undefined references",
        ],
    )
    undefined_citations = matching_excerpts(
        log_text + "\n" + blg_text,
        [
            r"LaTeX Warning:\s+Citation[\s\S]{0,1000}?undefined",
            r"There were undefined citations",
            r"Warning--I didn't find a database entry for[^\r\n]*",
            r"I found no \\citation commands[^\r\n]*",
        ],
    )
    rerun_indicators = matching_excerpts(
        log_text,
        [
            r"Rerun\s+to\s+get\s+cross-references\s+right",
            r"Label\(s\)\s+may\s+have\s+changed",
            r"rerunfilecheck Warning:\s+File[\s\S]{0,1000}?has changed",
            r"Please\s+\(?re\)?run\s+(?:LaTeX|BibTeX)",
            r"No\s+file\s+[\s\S]{0,500}?\.bbl",
        ],
    )

    pdfinfo_result: dict[str, Any] = {"invoked": False}
    pdfinfo_pages: int | None = None
    if paths["pdf"].is_file():
        proc = subprocess.run(
            [args.pdfinfo, str(paths["pdf"])],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        pdfinfo_result = {
            "invoked": True,
            "path": str(Path(args.pdfinfo).resolve()),
            "exit_code": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
        }
        page_match = re.search(r"^Pages:\s*([0-9]+)\s*$", proc.stdout, re.MULTILINE)
        if page_match:
            pdfinfo_pages = int(page_match.group(1))

    pdf_header_ok = False
    if paths["pdf"].is_file():
        with paths["pdf"].open("rb") as stream:
            pdf_header_ok = stream.read(5) == b"%PDF-"

    bbl_bibitem_count = len(re.findall(r"\\bibitem(?:\s*\[[^]]*\])?\s*\{", bbl_text))
    checks = {
        "latexmk_exit_zero": args.latexmk_exit_code == 0,
        "required_artifacts_present": not missing_required,
        "required_artifacts_nonempty": not empty_required,
        "pdf_header_valid": pdf_header_ok,
        "tex_output_summary_parsed": summary is not None,
        "pdfinfo_exit_zero": pdfinfo_result.get("exit_code") == 0,
        "pdfinfo_page_count_parsed": pdfinfo_pages is not None,
        "pdf_page_count_matches_log": bool(
            summary is not None and pdfinfo_pages is not None and summary["pages"] == pdfinfo_pages
        ),
        "pdf_byte_count_matches_log": bool(
            summary is not None
            and paths["pdf"].is_file()
            and summary["bytes"] == paths["pdf"].stat().st_size
        ),
        "log_has_no_fatal_errors": not fatal_errors,
        "log_has_no_undefined_references": not undefined_references,
        "log_and_blg_have_no_undefined_citations": not undefined_citations,
        "log_has_no_rerun_indicators": not rerun_indicators,
        "fls_records_main_tex": f"{job}.tex".lower() in fls_text.lower(),
        "fls_records_book_class": "stacks-project-book.cls" in fls_text.lower(),
        "aux_records_bibliography_database": bool(
            re.search(r"\\bibdata\{[^}]*\bmy\b[^}]*\}", aux_text)
        ),
        "aux_records_bibliography_style": "\\bibstyle{amsalpha}" in aux_text,
        "bbl_has_thebibliography": "\\begin{thebibliography}" in bbl_text,
        "bbl_has_bibitems": bbl_bibitem_count > 0,
        "blg_present": paths["blg"].is_file() and paths["blg"].stat().st_size > 0,
        "latexmk_database_present": paths["fdb_latexmk"].is_file()
        and paths["fdb_latexmk"].stat().st_size > 0,
    }
    failed_checks = [name for name, passed in checks.items() if not passed]
    status = "PASS" if not failed_checks else "FAIL"
    report = {
        "schema": "final-cumulative-build-audit-v1",
        "written_at_utc": utc_now(),
        "status": status,
        "build_dir": str(build_dir),
        "jobname": job,
        "frozen_bindings": {
            "runner_sha256": args.runner_sha256,
            "auditor_sha256": args.auditor_sha256,
            "source_sha256": args.source_sha256,
            "manifest_sha256": args.manifest_sha256,
            "assembly_report_sha256": args.assembly_report_sha256,
            "ready_validation_sha256": args.validation_sha256,
            "preflight_sha256": args.preflight_sha256,
        },
        "latexmk_exit_code": args.latexmk_exit_code,
        "artifacts": artifacts,
        "tex_output_summary": summary,
        "tex_output_summary_error": summary_error,
        "page_count": pdfinfo_pages,
        "pdfinfo": pdfinfo_result,
        "diagnostics": {
            "fatal_errors": fatal_errors,
            "bang_line_classification": {
                "true_error_lines": true_bang_errors,
                "font_box_trace_lines": font_box_traces,
                "unclassified_bang_lines": unclassified_bang_lines,
            },
            "undefined_references": undefined_references,
            "undefined_citations": undefined_citations,
            "rerun_indicators": rerun_indicators,
            "bbl_bibitem_count": bbl_bibitem_count,
            "missing_required_artifacts": missing_required,
            "empty_required_artifacts": empty_required,
        },
        "checks": checks,
        "failed_checks": failed_checks,
    }
    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "failed_checks": failed_checks}, sort_keys=True))
    return 0 if status == "PASS" else 2


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--build-dir")
    parser.add_argument("--jobname")
    parser.add_argument("--pdfinfo")
    parser.add_argument("--latexmk-exit-code", type=int)
    parser.add_argument("--output")
    parser.add_argument("--runner-sha256")
    parser.add_argument("--auditor-sha256")
    parser.add_argument("--source-sha256")
    parser.add_argument("--manifest-sha256")
    parser.add_argument("--assembly-report-sha256")
    parser.add_argument("--validation-sha256")
    parser.add_argument("--preflight-sha256")
    return parser


def main() -> int:
    parser = make_parser()
    args = parser.parse_args()
    if args.selftest:
        return run_selftest()
    required = [
        "build_dir",
        "jobname",
        "pdfinfo",
        "latexmk_exit_code",
        "output",
        "runner_sha256",
        "auditor_sha256",
        "source_sha256",
        "manifest_sha256",
        "assembly_report_sha256",
        "validation_sha256",
        "preflight_sha256",
    ]
    missing = [name for name in required if getattr(args, name) is None]
    if missing:
        parser.error(f"missing required audit arguments: {', '.join(missing)}")
    return audit(args)


if __name__ == "__main__":
    sys.exit(main())
