"""Reassemble the complete French reader from the included chapter sources.

No translation or mathematical correction is performed by this tool.
It selects only the portable pure transformations of the pinned assembler.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys
import types

ROOT = Path(__file__).resolve().parents[1]

def digest(data):
    return hashlib.sha256(data).hexdigest().upper()

def load_pure_assembler():
    path = ROOT / "tools/pinned_assembler.py"
    raw = path.read_bytes()
    receipt = json.loads((ROOT / "manifests/ASSEMBLY_RECEIPT.json").read_text(encoding="utf-8"))
    assert digest(raw) == receipt["pinned_assembler_sha256"]
    tree = ast.parse(raw.decode("utf-8"), filename=str(path))
    constants = {"EXPECTED_COMMIT", "EXPECTED_CHAPTERS", "STANDARD_LABELS"}
    nodes = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef)):
            nodes.append(node)
        elif isinstance(node, ast.Assign) and all(isinstance(x, ast.Name) and x.id in constants for x in node.targets):
            nodes.append(node)
    pure = types.ModuleType("portable_pinned_french_assembler")
    sys.modules[pure.__name__] = pure
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), "exec"), pure.__dict__)
    return pure, receipt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-if-missing", action="store_true")
    args = parser.parse_args()
    module, receipt = load_pure_assembler()
    manifest = json.loads((ROOT / "manifests/FRENCH_RESTORATION_ASSEMBLY_MANIFEST.json").read_text(encoding="utf-8"))
    sources = []
    for item in manifest["sources"]:
        path = ROOT / "chapters" / f"{item['chapter']:03d}_{item['stem']}.fr.tex"
        raw = path.read_bytes()
        assert len(raw) == item["selected_bytes"] and digest(raw) == item["selected_sha256"]
        text = path.read_text(encoding="utf-8")
        title, issues = module.standalone_text_issues(text, item["stem"])
        assert not issues, (path.name, issues)
        sources.append(module.SelectedSource(
            part=0, chapter=item["chapter"], stem=item["stem"], path=path,
            recorded_path="chapters/" + path.name, byte_count=len(raw),
            sha256=item["selected_sha256"], title=title, manifest_role=item["selection"], text=text))
    assert len(sources) == 116
    navigation = (ROOT / "chapters.tex").read_text(encoding="utf-8")
    entries, starts = module.parse_navigation(navigation)
    attribution, note = module.attribution_blocks(module.contributors_text(ROOT / "CONTRIBUTORS"))
    derived = {"preamble": module.transformed_preamble(ROOT / "preamble.tex"),
               "gfdl": module.extract_gfdl(ROOT / "chapters/001_introduction.fr.tex"),
               "attribution": attribution, "non_endorsement": note,
               "navigation": navigation, "navigation_entries": entries,
               "navigation_captions": dict(entries), "part_starts": starts}
    index, _ = module.generate_corpus_index(sources, "Index généré automatiquement")
    data, _, checks = module.assemble_once(sources, index, derived)
    assert digest(data) == receipt["cumulative_source_sha256"]
    output = ROOT / "stacks_fr_faithful_116.tex"
    if output.exists():
        assert output.read_bytes() == data, "Le fichier cumulatif diffère de sa reconstruction."
    elif args.write_if_missing:
        output.write_bytes(data)
    else:
        raise FileNotFoundError("Utiliser --write-if-missing pour recréer le fichier cumulatif absent.")
    print(json.dumps({"status": "PASS", "chapters": 116, "bytes": len(data),
                      "sha256": digest(data), "labels": checks["labels_total"],
                      "references": checks["refs_total"]}))

if __name__ == "__main__":
    main()
