"""Bounded source-fidelity continuation check; never edits chapter bodies."""
import argparse, hashlib, json, re, subprocess, urllib.request
from datetime import datetime, timezone
from pathlib import Path

COMMIT = "a04446e57ec1fbc252a871afcec7752fb2807b14"
SOURCE_COMMIT = "0fca0328aaf6a995831bb95be7ee243563bc6658"
CASES = [
    dict(id="DERIVED-024", chapter=13, stem="derived",
         source="is an isomorphism as desired.",
         target="$F(A)[0] \\to F(I^\\bullet)$ est un isomorphisme, comme voulu.",
         reason="La conclusion officielle dit isomorphisme, non quasi-isomorphisme. La lecture officielle est déjà rétablie dans la source publiée."),
    dict(id="DERIVED-029", chapter=13, stem="derived",
         source="This proves faithfulness. Fully faithfulness is proved in the exact same manner.",
         target="Cela démontre la fidélité. La pleine fidélité se démontre exactement de la même manière.",
         reason="La source mentionne la pleine fidélité après la fidélité. La remplacer par la seule plénitude serait une correction éditoriale, absente de la traduction publiée."),
    dict(id="NOTE-SOURCE-RESOLUTION", chapter=13, stem="derived",
         source="By (1) we see that $\\mathcal{I}$ is nonempty. Pick $P$ in $\\mathcal{I}$.",
         target="D'après (1), $\\mathcal{I}$ n'est pas vide. Choisissons $P$ dans $\\mathcal{I}$.",
         reason="La note expliquant que la classe contient zéro appartient à l'anglais officiel. Sa traduction n'est pas un ajout du traducteur."),
    dict(id="CONSTRUCTION-RECOLLEMENT", chapter=110, stem="examples",
         source="correct this by glueing in an affine line instead",
         target="Corrigeons cela en recollant plutôt une droite affine",
         reason="Le verbe corriger appartient à la construction officielle. Il ne signale pas une intervention éditoriale dans la traduction."),
    dict(id="REMARQUE-GRUSON", chapter=10, stem="algebra",
         source="We note that there is an error in the proof of faithfully flat descent of projectivity in \\cite{GruRay}.",
         target="Signalons qu'il y a une erreur dans la démonstration de la descente fidèlement plate de la projectivité dans \\cite{GruRay}.",
         reason="Le commentaire sur une erreur de la littérature se trouve déjà dans l'anglais officiel et doit rester dans sa traduction."),
    dict(id="REMARQUE-EGA", chapter=110, stem="examples",
         source="In this section we give a counterexample to the final sentence in \\cite[0, Example 19.10.3(i)]{EGA}",
         target="Dans cette section, nous donnons un contre-exemple à la dernière phrase de \\cite[0, exemple 19.10.3(i)]{EGA}",
         reason="Le contre-exemple et le commentaire sur les errata d'EGA proviennent de Stacks, non d'une proposition ajoutée par l'IA."),
    dict(id="REMARQUE-AOKI", chapter=110, stem="examples",
         source="is mentioned in the Erratum \\cite{AokiHomStacksErr} to \\cite{AokiHomStacks}.",
         target="Cette même difficulté est mentionnée dans l'erratum \\cite{AokiHomStacksErr} à \\cite{AokiHomStacks}.",
         reason="Le commentaire sur l'erratum est celui de la source. L'effacer retirerait du contenu officiel.")
]

def sha(b): return hashlib.sha256(b).hexdigest().upper()
def norm(s): return re.sub(r"\s+", " ", s).strip()
def active_text(s):
    lines=[]
    for line in s.splitlines(keepends=True):
        cut = re.search(r"(?<!\\)%", line)
        lines.append(line[:cut.start()]+"\n" if cut else line)
    return "".join(lines)
def locate(text, quote):
    text = active_text(text)
    pattern = r"\s+".join(re.escape(p) for p in quote.split())
    hits=list(re.finditer(pattern, text))
    if len(hits)!=1:
        raise ValueError(f"Expected one active occurrence, found {len(hits)}: {quote}")
    return text[:hits[0].start()].count("\n")+1

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--repo", type=Path, required=True)
    p.add_argument("--authority", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a=p.parse_args()
    repo=a.repo.resolve()
    edition=repo/"editions"/"2026-09-30-faithful116"
    manifest=json.loads((edition/"restoration"/"FRENCH_RESTORATION_ASSEMBLY_MANIFEST.r2.json").read_text(encoding="utf-8-sig"))
    sources={x["stem"]:x for x in manifest["sources"]}
    before={}
    files=[]
    checks=[]
    git="C:/Program Files/Git/cmd/git.exe"
    for stem in sorted({x["stem"] for x in CASES}):
        spec=sources[stem]
        target=edition/"chapters"/f'{spec["chapter"]:03d}_{stem}.fr.tex'
        official=a.authority/f"{stem}.tex"
        tb=target.read_bytes(); ob=official.read_bytes()
        if sha(tb)!=spec["selected_sha256"] or sha(ob)!=spec["authority_sha256"]:
            raise ValueError(f"Bound source hash mismatch: {stem}")
        rel=target.relative_to(repo).as_posix()
        gb=subprocess.check_output([git,"-C",str(repo),"show",f"{SOURCE_COMMIT}:{rel}"])
        if gb!=tb: raise ValueError(f"Released Git blob mismatch: {stem}")
        url=f"https://raw.githubusercontent.com/KokunoYumeto/stacks-fr/{SOURCE_COMMIT}/{rel}"
        req=urllib.request.Request(url,headers={"User-Agent":"source-fidelity-bounded-check/1.0"})
        with urllib.request.urlopen(req, timeout=60) as response: pb=response.read()
        if pb!=tb: raise ValueError(f"Anonymous public bytes mismatch: {stem}")
        before[stem]=(target,tb,official,ob)
        files.append(dict(stem=stem, target_path=rel,target_bytes=len(tb),target_sha256=sha(tb),
                          authority_bytes=len(ob),authority_sha256=sha(ob),
                          source_commit=SOURCE_COMMIT,public_url=url,
                          public_byte_match=True,committed_blob_match=True,selection_hash_match=True))
    for c in CASES:
        target,tb,official,ob=before[c["stem"]]
        sl=locate(ob.decode("utf-8-sig"),c["source"])
        tl=locate(tb.decode("utf-8-sig"),c["target"])
        checks.append(dict(id=c["id"],stem=c["stem"],official_line=sl,french_line=tl,
                           official_quote=c["source"],french_quote=c["target"],
                           rationale_fr=c["reason"],
                           official_url=f"https://github.com/stacks/stacks-project/blob/{COMMIT}/{c['stem']}.tex#L{sl}",
                           french_url=f"https://github.com/KokunoYumeto/stacks-fr/blob/{SOURCE_COMMIT}/{target.relative_to(repo).as_posix()}#L{tl}",
                           outcome="PRESERVED_OFFICIAL_READING"))
    for target,tb,official,ob in before.values():
        if target.read_bytes()!=tb or official.read_bytes()!=ob:
            raise ValueError("Source mutation during read-only check")
    out=dict(schema="french_restoration_bounded_continuation_v1",
             status="PASS_NO_NEW_RESTORATION_REQUIRED_IN_CHECKED_LOCI",
             checked_at_utc=datetime.now(timezone.utc).isoformat(),
             scope="Sept passages ciblés dans trois unités publiées; ni audit intégral de la prose ni certification experte.",
             model="gpt-6.1-sol",effort="ultra",human_expert_review=False,
             authority_commit=COMMIT,source_commit=SOURCE_COMMIT,
             checked_loci=len(checks),checked_source_units=len(files),
             new_source_edits=0,source_mutations=0,
             qualification="Ce résultat ne prouve pas l'absence de toute divergence non encore identifiée dans les 116 chapitres.",
             files=files,checks=checks)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:out[k] for k in ["status","checked_loci","checked_source_units","new_source_edits","source_mutations"]},ensure_ascii=False))
if __name__=="__main__": main()

