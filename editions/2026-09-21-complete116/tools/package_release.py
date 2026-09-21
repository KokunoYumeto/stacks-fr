#!/usr/bin/env python3
"""Create the ordered French Stacks release payload without staging copies."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import shutil
import zipfile
from pathlib import Path, PurePosixPath


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
FR_ROOT = ROOT.parents[1]
WORKSPACE = next(parent for parent in ROOT.parents if parent.name.lower() == "interlanguage")
UPSTREAM = (
    WORKSPACE
    / "03_projects/language_management/cjk/03_working_translations/stacks_cjk_20260821/upstream/src"
    / "stacks-project-a04446e57ec1fbc252a871afcec7752fb2807b14"
)
MANIFEST = ROOT / "evidence" / "FINAL_CUMULATIVE_SOURCE_MANIFEST.csv"
PDF = ROOT / "output" / "stacks_fr_complete_116.pdf"
TEX = ROOT / "output" / "stacks_fr_complete_116.tex"

PUBLIC_PDF = HERE / "01_stacks_project_french_complete_116.pdf"
PUBLIC_TEX = HERE / "02_stacks_project_french_complete_116.tex"
SOURCE_ZIP = HERE / "03_stacks_project_french_complete_source.zip"
PROVENANCE_ZIP = HERE / "04_stacks_project_french_provenance_evidence.zip"
VISUAL_ZIP = HERE / "05_stacks_project_french_visual_qa.zip"
PUBLIC_README = HERE / "06_README_PUBLICATION.md"
CHECKSUMS = HERE / "07_SHA256SUMS.txt"
PUBLIC_MANIFEST = HERE / "PUBLIC_FILE_MANIFEST.csv"
SANITATION_MANIFEST = HERE / "PUBLIC_PROVENANCE_SANITATION_MANIFEST.csv"

EXPECTED_PDF_SHA256 = "05CD5ECDD3AFFDB7A485051D320F204521B2B2B6E0FCD00D6D38E89D5500ADA2"
EXPECTED_TEX_SHA256 = "B10511895138E6E38DE5E3BB357FBB597E6CA1406DCAC9ED69C42D2E2054A29E"

TEXT_SUFFIXES = {
    ".json", ".jsonl", ".csv", ".tsv", ".md", ".txt", ".log",
    ".blg", ".fls", ".sha256", ".yaml", ".yml", ".toml", ".xml",
}
EXCLUDED_COMPONENTS = {
    "build", "output", "outputs", "release", "tmp", "__pycache__",
    "pages", "contacts", "changed_pages_120dpi", "contacts_changed_120dpi",
    "pre_repair_see_20260921", "coherent_nllb_int8_tmp", "topologies_hf_home",
    "topologies_model_ct2", "topologies_model_hf",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def zip_write_bytes(archive: zipfile.ZipFile, arcname: str, data: bytes) -> None:
    info = zipfile.ZipInfo(str(PurePosixPath(arcname)), date_time=(2026, 9, 21, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def zip_write_file(archive: zipfile.ZipFile, arcname: str, path: Path) -> None:
    zip_write_bytes(archive, arcname, path.read_bytes())


def workspace_path(recorded: str) -> Path:
    candidate = (WORKSPACE / recorded.replace("/", os.sep)).resolve()
    candidate.relative_to(WORKSPACE.resolve())
    return candidate


def sanitize_text(data: bytes) -> tuple[bytes, int]:
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        text = data.decode("cp1252")
    home = str(Path.home())
    home_forward = home.replace("\\", "/")
    username = Path.home().name
    substitutions = 0
    for pattern, replacement in (
        (re.escape(home), "%USERPROFILE%"),
        (re.escape(home_forward), "%USERPROFILE%"),
        (re.escape(username), "[REDACTED_USER]"),
    ):
        text, count = re.subn(pattern, replacement, text, flags=re.IGNORECASE)
        substitutions += count
    return text.encode("utf-8"), substitutions


def excluded(path: Path) -> bool:
    lowered = {part.lower() for part in path.parts}
    return bool(lowered & EXCLUDED_COMPONENTS) or any(
        "cache" in part or part.startswith("models--") for part in lowered
    )


for target in (PUBLIC_PDF, PUBLIC_TEX, SOURCE_ZIP, PROVENANCE_ZIP, VISUAL_ZIP, CHECKSUMS, PUBLIC_MANIFEST, SANITATION_MANIFEST):
    if target.exists():
        raise SystemExit(f"refusing to overwrite release payload: {target}")

if sha256(PDF) != EXPECTED_PDF_SHA256 or sha256(TEX) != EXPECTED_TEX_SHA256:
    raise SystemExit("final PDF/TeX binding mismatch")
shutil.copyfile(PDF, PUBLIC_PDF)
shutil.copyfile(TEX, PUBLIC_TEX)
shutil.copyfile(HERE / "README_PUBLICATION.md", PUBLIC_README)
if sha256(PUBLIC_PDF) != EXPECTED_PDF_SHA256 or sha256(PUBLIC_TEX) != EXPECTED_TEX_SHA256:
    raise SystemExit("public PDF/TeX copy mismatch")

with MANIFEST.open(encoding="utf-8", newline="") as stream:
    manifest_rows = list(csv.DictReader(stream))
chapter_rows = [row for row in manifest_rows if row["role"] == "terminal-chapter-source"]
if len(chapter_rows) != 116:
    raise SystemExit(f"expected 116 chapter rows, found {len(chapter_rows)}")

source_entries: list[tuple[str, Path]] = [
    ("stacks_fr_complete_116.tex", TEX),
    ("stacks-project-book.cls", UPSTREAM / "stacks-project-book.cls"),
    ("my.bib", workspace_path(next(row["path"] for row in manifest_rows if row["role"] == "bibliography"))),
    ("COPYING", UPSTREAM / "COPYING"),
    ("CONTRIBUTORS", UPSTREAM / "CONTRIBUTORS"),
    ("UPSTREAM_README", UPSTREAM / "README"),
    ("BUILD.md", HERE / "SOURCE_BUILD_README.md"),
    ("manifests/FINAL_CUMULATIVE_SOURCE_MANIFEST.csv", MANIFEST),
    ("manifests/FINAL_CUMULATIVE_ASSEMBLY_REPORT.json", ROOT / "evidence" / "FINAL_CUMULATIVE_ASSEMBLY_REPORT.json"),
    ("manifests/FINAL_CUMULATIVE_VALIDATE_INPUTS_REPORT.json", ROOT / "evidence" / "FINAL_CUMULATIVE_VALIDATE_INPUTS_REPORT.json"),
    ("manifests/FINAL_CUMULATIVE_INPUT_CONTRACT.json", ROOT / "evidence" / "FINAL_CUMULATIVE_INPUT_CONTRACT.json"),
    ("tools/assemble_final_cumulative.py", ROOT / "assemble_final_cumulative.py"),
    ("tools/generate_successor_bindings.py", ROOT / "generate_successor_bindings.py"),
    ("tools/package_release.py", HERE / "package_release.py"),
]
for path in sorted((ROOT / "build_tools").iterdir(), key=lambda item: item.name.lower()):
    # The guarded runner is intentionally machine-local and contains an
    # absolute workspace binding. The portable build command in BUILD.md,
    # latexmkrc, and the independent auditor are the releasable build tools.
    if path.is_file() and path.name != "run_guarded_cumulative_build.ps1":
        source_entries.append((f"tools/build_tools/{path.name}", path))

for row in sorted(chapter_rows, key=lambda item: int(item["chapter"])):
    path = workspace_path(row["path"])
    if sha256(path) != row["sha256"] or path.stat().st_size != int(row["bytes"]):
        raise SystemExit(f"chapter binding mismatch: {path}")
    source_entries.append((f"chapters/{int(row['chapter']):03d}_{row['stem']}.fr.tex", path))

for row in manifest_rows:
    if row["role"] in {"part-master-witness", "part-report", "part-source-manifest"}:
        path = workspace_path(row["path"])
        source_entries.append((f"parts/{row['part']}/{path.name}", path))
for role, arcname in (
    ("preamble", "support/preamble.tex"),
    ("global-navigation", "support/chapters.tex"),
    ("license-source", "support/introduction.tex"),
    ("partition-authority", "support/PARTS.csv"),
):
    source_entries.append((arcname, workspace_path(next(row["path"] for row in manifest_rows if row["role"] == role))))

seen: set[str] = set()
with zipfile.ZipFile(SOURCE_ZIP, "w", allowZip64=True) as archive:
    for arcname, path in source_entries:
        if arcname in seen:
            raise SystemExit(f"duplicate source archive name: {arcname}")
        seen.add(arcname)
        zip_write_file(archive, arcname, path)

# Textual provenance is complete across the twelve part lanes and global control,
# while generated renders, build trees, models, and duplicate deliverables are
# deliberately kept out of this human-auditable archive.
provenance_candidates: dict[str, Path] = {}
roots = [FR_ROOT / f"p{part:02d}" for part in range(1, 13)] + [FR_ROOT / "00_control", FR_ROOT / "pending-evidence"]
for base in roots:
    if not base.exists():
        continue
    for path in base.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES or excluded(path.relative_to(FR_ROOT)):
            continue
        arcname = str(PurePosixPath("project") / PurePosixPath(path.relative_to(FR_ROOT).as_posix()))
        provenance_candidates[arcname] = path
build_audit_path = ROOT / "evidence" / "FINAL_CUMULATIVE_BUILD_AUDIT_B1051189.json"
build_audit = json.loads(build_audit_path.read_text(encoding="utf-8"))
build_dir = Path(build_audit["build_dir"])
for name in ("stacks_fr_complete_116.log", "stacks_fr_complete_116.fls", "stacks_fr_complete_116.blg"):
    path = build_dir / name
    provenance_candidates[f"final_build/{name}"] = path
provenance_candidates["publication/README_PUBLICATION.md"] = HERE / "README_PUBLICATION.md"

sanitation_rows: list[dict[str, object]] = []
with zipfile.ZipFile(PROVENANCE_ZIP, "w", allowZip64=True) as archive:
    for arcname, path in sorted(provenance_candidates.items()):
        raw = path.read_bytes()
        packaged, replacements = sanitize_text(raw)
        zip_write_bytes(archive, arcname, packaged)
        sanitation_rows.append(
            {
                "archive_path": arcname,
                "original_bytes": len(raw),
                "original_sha256": sha256_bytes(raw),
                "packaged_bytes": len(packaged),
                "packaged_sha256": sha256_bytes(packaged),
                "local_identity_replacements": replacements,
            }
        )

with SANITATION_MANIFEST.open("w", encoding="utf-8", newline="") as stream:
    fields = ["archive_path", "original_bytes", "original_sha256", "packaged_bytes", "packaged_sha256", "local_identity_replacements"]
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    writer.writerows(sanitation_rows)

# Visual archive: the complete inspected changed-page contact set, the two final
# replacement-page renders, and every associated text manifest/ledger.
visual_entries: dict[str, Path] = {}
old_visual = ROOT / "evidence" / "visual_qa" / "FINAL_39997049B981_20260921"
new_visual = ROOT / "evidence" / "visual_qa" / "FINAL_05CD5ECDD3AF_20260921_POSTREPAIR"
for path in old_visual.rglob("*"):
    if not path.is_file():
        continue
    rel = path.relative_to(old_visual)
    if "changed_pages_120dpi" in rel.parts:
        continue
    visual_entries[str(PurePosixPath("pre_repair_changed_page_review") / PurePosixPath(rel.as_posix()))] = path
for path in new_visual.rglob("*"):
    if path.is_file():
        rel = path.relative_to(new_visual)
        visual_entries[str(PurePosixPath("final_postrepair_review") / PurePosixPath(rel.as_posix()))] = path

with zipfile.ZipFile(VISUAL_ZIP, "w", allowZip64=True) as archive:
    for arcname, path in sorted(visual_entries.items()):
        if path.suffix.lower() in TEXT_SUFFIXES:
            data, _ = sanitize_text(path.read_bytes())
            zip_write_bytes(archive, arcname, data)
        else:
            zip_write_file(archive, arcname, path)

# Verify every archive entry is unique, readable, and internally CRC-clean.
for archive_path in (SOURCE_ZIP, PROVENANCE_ZIP, VISUAL_ZIP):
    with zipfile.ZipFile(archive_path, "r") as archive:
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise SystemExit(f"duplicate ZIP entry in {archive_path}")
        bad = archive.testzip()
        if bad is not None:
            raise SystemExit(f"ZIP CRC failure in {archive_path}: {bad}")

public_files = [PUBLIC_PDF, PUBLIC_TEX, SOURCE_ZIP, PROVENANCE_ZIP, VISUAL_ZIP, PUBLIC_README]
with CHECKSUMS.open("w", encoding="ascii", newline="\n") as stream:
    for path in public_files:
        stream.write(f"{sha256(path)}  {path.name}\n")
public_files.append(CHECKSUMS)

with PUBLIC_MANIFEST.open("w", encoding="utf-8", newline="") as stream:
    fields = ["order", "filename", "bytes", "sha256", "purpose"]
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    purposes = {
        PUBLIC_PDF.name: "complete 8374-page French reader",
        PUBLIC_TEX.name: "exact cumulative editable LaTeX",
        SOURCE_ZIP.name: "complete modular editable source and rebuild tooling",
        PROVENANCE_ZIP.name: "translation decisions, canon witnesses, logs, and source/build evidence",
        VISUAL_ZIP.name: "render, geometry, and visual-review evidence",
        PUBLIC_README.name: "public description and file guide",
        CHECKSUMS.name: "SHA-256 inventory",
    }
    for order, path in enumerate(public_files, 1):
        writer.writerow(
            {
                "order": order,
                "filename": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "purpose": purposes[path.name],
            }
        )

print(
    json.dumps(
        {
            "status": "PASS",
            "source_entries": len(source_entries),
            "provenance_entries": len(provenance_candidates),
            "visual_entries": len(visual_entries),
            "public_manifest": str(PUBLIC_MANIFEST),
            "public_manifest_sha256": sha256(PUBLIC_MANIFEST),
            "sanitation_manifest": str(SANITATION_MANIFEST),
            "sanitation_manifest_sha256": sha256(SANITATION_MANIFEST),
            "files": [
                {"path": str(path), "bytes": path.stat().st_size, "sha256": sha256(path)}
                for path in public_files
            ],
        },
        ensure_ascii=False,
        indent=2,
    )
)
