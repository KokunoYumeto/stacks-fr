from __future__ import annotations

import copy
import csv
import hashlib
import importlib.util
import io
import json
import os
import sys
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).resolve()
TASK = SCRIPT.parent
EVIDENCE = TASK / "evidence"
PARTS_DIR = TASK / "parts"
FR = SCRIPT.parents[2]
WORKSPACE = SCRIPT.parents[7]
PREDECESSOR = FR / "00_control" / "final_cumulative_116"
PREDECESSOR_MANIFEST = PREDECESSOR / "evidence" / "FINAL_CUMULATIVE_SOURCE_MANIFEST.csv"
PREDECESSOR_CONTRACT = PREDECESSOR / "evidence" / "FINAL_CUMULATIVE_INPUT_CONTRACT.json"
ASSEMBLER_PATH = TASK / "assemble_final_cumulative.py"
CONTRACT_OUT = EVIDENCE / "FINAL_CUMULATIVE_INPUT_CONTRACT.json"
REBIND_REPORT = EVIDENCE / "POSTCLOSURE_SUCCESSOR_REBIND_REPORT.json"
PINNED_COMMIT = "a04446e57ec1fbc252a871afcec7752fb2807b14"
PART_RANGES = {
    1: (1, 10), 2: (11, 15), 3: (16, 25), 4: (26, 33),
    5: (34, 38), 6: (39, 49), 7: (50, 59), 8: (60, 68),
    9: (69, 79), 10: (80, 90), 11: (91, 101), 12: (102, 116),
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def rel(path: Path) -> str:
    return path.resolve().relative_to(WORKSPACE.resolve()).as_posix()


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile("wb", dir=path.parent, delete=False) as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
            temporary = Path(handle.name)
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary and temporary.exists():
            temporary.unlink()


spec = importlib.util.spec_from_file_location("successor_assembler", ASSEMBLER_PATH)
if spec is None or spec.loader is None:
    raise SystemExit("cannot load cumulative assembler")
assembler = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = assembler
spec.loader.exec_module(assembler)

with PREDECESSOR_MANIFEST.open(encoding="utf-8", newline="") as fh:
    prior_rows = list(csv.DictReader(fh))
chapter_rows = [row for row in prior_rows if row.get("role") == "terminal-chapter-source"]
if [int(row["chapter"]) for row in chapter_rows] != list(range(1, 117)):
    raise SystemExit("predecessor selection is not exactly Chapters 1-116")

sources = []
for row in chapter_rows:
    chapter = int(row["chapter"])
    path = WORKSPACE / row["path"]
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    title, issues = assembler.standalone_text_issues(text, row["stem"])
    if issues or title is None:
        raise SystemExit(f"standalone validation failed for Chapter {chapter}: {issues}")
    sources.append(
        assembler.SelectedSource(
            part=int(row["part"][1:]),
            chapter=chapter,
            stem=row["stem"],
            path=path,
            recorded_path=rel(path),
            byte_count=len(raw),
            sha256=sha256(raw),
            title=title,
            manifest_role="terminal-chapter",
            text=text,
        )
    )

predecessor_contract = json.loads(PREDECESSOR_CONTRACT.read_text(encoding="utf-8"))
successor_contract = copy.deepcopy(predecessor_contract)
successor_contract["inventory_authority"] = predecessor_contract["inventory_authority"]
part_bindings = []
preamble = assembler.transformed_preamble(FR / "p01" / "tex" / "preamble.tex")

for part, (start, end) in PART_RANGES.items():
    part_sources = [source for source in sources if start <= source.chapter <= end]
    if [source.chapter for source in part_sources] != list(range(start, end + 1)):
        raise SystemExit(f"part {part} selection mismatch")
    part_dir = PARTS_DIR / f"p{part:02d}"
    master = part_dir / f"stacks_fr_part{part:02d}_successor_20260921.tex"
    manifest = part_dir / f"PART{part:02d}_SOURCE_MANIFEST_SUCCESSOR_20260921.csv"
    report = part_dir / f"PART{part:02d}_ASSEMBLY_REPORT_SUCCESSOR_20260921.json"

    transformed_blocks = []
    transforms = []
    for source in part_sources:
        transformed, counts = assembler.transform_source(source)
        transformed_blocks.append(transformed)
        transforms.append({"chapter": source.chapter, "stem": source.stem, **counts})
    master_text = (
        preamble
        + "\\begin{document}\n"
        + f"\\title{{Le projet Stacks --- édition française, partie {part}}}\n"
        + "\\maketitle\n\\tableofcontents\n"
        + "\n".join(transformed_blocks)
        + "\n\\bibliography{my}\n\\bibliographystyle{amsalpha}\n\\end{document}\n"
    )
    master_data = master_text.encode("utf-8")

    manifest_buffer = io.StringIO(newline="")
    writer = csv.DictWriter(
        manifest_buffer,
        fieldnames=("role", "chapter", "stem", "source_path", "source_bytes", "source_sha256"),
        lineterminator="\n",
    )
    writer.writeheader()
    for source in part_sources:
        writer.writerow(
            {
                "role": "terminal-chapter",
                "chapter": source.chapter,
                "stem": source.stem,
                "source_path": source.recorded_path,
                "source_bytes": source.byte_count,
                "source_sha256": source.sha256,
            }
        )
    if part == 1:
        directly_bound_roles = {
            "preamble", "global-navigation", "bibliography",
            "contributors", "book-class", "upstream-assembly-rule",
            "upstream-reference-rule",
        }
        for authority in successor_contract["support_authorities"]:
            if authority["role"] not in directly_bound_roles:
                continue
            support_path = WORKSPACE / authority["path"]
            support_raw = support_path.read_bytes()
            writer.writerow(
                {
                    "role": authority["role"],
                    "chapter": "",
                    "stem": "",
                    "source_path": rel(support_path),
                    "source_bytes": len(support_raw),
                    "source_sha256": sha256(support_raw),
                }
            )
    manifest_data = manifest_buffer.getvalue().encode("utf-8")

    atomic_write(master, master_data)
    atomic_write(manifest, manifest_data)
    report_object = {
        "schema": "stacks-fr-postclosure-successor-part-assembly-v1",
        "status": "PASS",
        "pinned_commit": PINNED_COMMIT,
        "part": part,
        "chapter_count": len(part_sources),
        "chapter_numbers": [source.chapter for source in part_sources],
        "chapters": [
            {
                "chapter": source.chapter,
                "stem": source.stem,
                "source_path": source.recorded_path,
                "source_bytes": source.byte_count,
                "source_sha256": source.sha256,
            }
            for source in part_sources
        ],
        "source_manifest": {
            "path": rel(manifest), "bytes": len(manifest_data), "sha256": sha256(manifest_data)
        },
        "output": {
            "path": rel(master), "bytes": len(master_data), "sha256": sha256(master_data)
        },
        "transforms": transforms,
        "source_selection": {
            "predecessor_manifest": rel(PREDECESSOR_MANIFEST),
            "predecessor_manifest_sha256": sha256(PREDECESSOR_MANIFEST.read_bytes()),
            "policy": "same 116 canonical paths; live postclosure bytes rebound after reader-visible language and running-head repairs",
        },
        "tex_or_render_invoked": False,
    }
    if part == 11:
        book_contract = successor_contract["generated_book_contract"]
        report_object.update(
            {
                "gfdl_block_sha256": book_contract["gfdl_block"]["sha256"],
                "attribution_block_sha256": book_contract["attribution_block"]["sha256"],
                "non_endorsement_block_sha256": book_contract["non_endorsement_block"]["sha256"],
                "transformed_preamble_sha256": book_contract["transformed_preamble_sha256"],
            }
        )
    report_data = (json.dumps(report_object, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    atomic_write(report, report_data)
    part_bindings.append(
        {
            "part": part,
            "report": {"path": rel(report), "bytes": len(report_data), "sha256": sha256(report_data)},
            "manifest": {"path": rel(manifest), "bytes": len(manifest_data), "sha256": sha256(manifest_data)},
            "master": {"path": rel(master), "bytes": len(master_data), "sha256": sha256(master_data)},
        }
    )

for spec_item, binding in zip(successor_contract["parts"], part_bindings, strict=True):
    if spec_item["part"] != binding["part"]:
        raise SystemExit("part contract order mismatch")
    spec_item["binding"] = "stable"
    spec_item["report_schema"] = "stacks-fr-postclosure-successor-part-assembly-v1"
    spec_item["accepted_report_statuses"] = ["PASS"]
    spec_item["selected_manifest_role"] = "terminal-chapter"
    spec_item["report_path_base"] = "workspace-root"
    spec_item["manifest_path_base"] = "workspace-root"
    spec_item.pop("manifest_field_aliases", None)
    spec_item.pop("report_artifact_shape", None)
    spec_item["report"] = binding["report"]
    spec_item["manifest"] = binding["manifest"]
    spec_item["master"] = binding["master"]

# Chapter 1 is also the exact license-source support authority. Reader-visible
# citation normalization changed its bytes but not the verbatim license block.
for authority in successor_contract["support_authorities"]:
    if authority["role"] == "license-source":
        support_path = WORKSPACE / authority["path"]
        support_raw = support_path.read_bytes()
        authority["bytes"] = len(support_raw)
        authority["sha256"] = sha256(support_raw)

successor_contract["output_policy"]["validate_inputs_report"] = rel(EVIDENCE / "FINAL_CUMULATIVE_VALIDATE_INPUTS_REPORT.json")
successor_contract["output_policy"]["final_tex"] = rel(TASK / "output" / "stacks_fr_complete_116.tex")
successor_contract["output_policy"]["final_source_manifest"] = rel(EVIDENCE / "FINAL_CUMULATIVE_SOURCE_MANIFEST.csv")
successor_contract["output_policy"]["final_report"] = rel(EVIDENCE / "FINAL_CUMULATIVE_ASSEMBLY_REPORT.json")
successor_contract["output_policy"]["gate"] = "All twelve postclosure successor report/manifest/master triads, 116 live chapter sources, generated index, references, and deterministic replay must validate before writing."
contract_data = (json.dumps(successor_contract, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
atomic_write(CONTRACT_OUT, contract_data)

receipts = []
for path in (
    FR / "00_control" / "POSTCLOSURE_CROSS_REFERENCE_LANGUAGE_REPAIR_20260921.json",
    FR / "00_control" / "POSTCLOSURE_CITATION_KEY_REPAIR_20260921.json",
    FR / "p10" / "work" / "ch090_round1" / "POSTCLOSURE_LANGUAGE_REPAIR_20260921.json",
    FR / "p11" / "work" / "ch091_round1" / "POSTCLOSURE_LANGUAGE_REPAIR_20260921.json",
):
    if path.is_file():
        receipts.append({"path": rel(path), "bytes": path.stat().st_size, "sha256": sha256(path.read_bytes())})

report_object = {
    "schema": "stacks-fr-postclosure-successor-rebind-v1",
    "status": "PASS_REBOUND_BUILD_PENDING",
    "pinned_commit": PINNED_COMMIT,
    "predecessor_manifest": {
        "path": rel(PREDECESSOR_MANIFEST),
        "bytes": PREDECESSOR_MANIFEST.stat().st_size,
        "sha256": sha256(PREDECESSOR_MANIFEST.read_bytes()),
    },
    "chapter_count": len(sources),
    "parts": part_bindings,
    "successor_contract": {"path": rel(CONTRACT_OUT), "bytes": len(contract_data), "sha256": sha256(contract_data)},
    "postclosure_receipts": receipts,
    "source_hashes": [
        {"chapter": source.chapter, "stem": source.stem, "path": source.recorded_path, "bytes": source.byte_count, "sha256": source.sha256}
        for source in sources
    ],
    "next_action": "Run successor assembler validation/selftests, assemble deterministically, then perform one guarded cumulative TeX build.",
}
report_data = (json.dumps(report_object, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
atomic_write(REBIND_REPORT, report_data)
print(json.dumps({"status": report_object["status"], "chapters": len(sources), "parts": len(part_bindings), "contract_sha256": sha256(contract_data), "report_sha256": sha256(report_data)}, indent=2))
