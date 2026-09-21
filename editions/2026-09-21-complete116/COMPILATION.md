# Recompiler le lecteur français complet

Le fichier `stacks_fr_complete_116.tex` contient tout le texte traduit et
l’index général. Il utilise les fichiers voisins `stacks-project-book.cls`
et `my.bib`.

Il faut une distribution TeX fournissant `latexmk`, pdfLaTeX, BibTeX, les
paquets AMS, le français de Babel, `xy`, `multicol`, `hyperref` et Latin Modern.
Depuis ce répertoire, exécuter :

```text
latexmk -norc -pdf -bibtex -interaction=nonstopmode -halt-on-error -file-line-error -recorder stacks_fr_complete_116.tex
```

La compilation de référence produit un lecteur de 8 374 pages. Les empreintes
du PDF, du TeX, du journal et de l’enregistrement des entrées de compilation sont
conservées dans les sommes de contrôle et l’archive de provenance. Une autre
version de la distribution TeX peut produire des octets PDF différents.

`chapters/` contient les 116 sources françaises modifiables individuellement.
Leur sélection est décrite dans `manifests/FINAL_CUMULATIVE_SOURCE_MANIFEST.csv`.
`parts/` conserve les douze assemblages intermédiaires et leurs manifestes.
Les outils d’assemblage et leurs contrats d’entrée sont dans `tools/` et
`manifests/` ; ils permettent d’examiner la reconstruction des sources.

La source anglaise de référence est le commit
`a04446e57ec1fbc252a871afcec7752fb2807b14` du Stacks Project.
La traduction est indépendante, réalisée avec l’assistance de l’IA et non
approuvée par le Stacks Project. Voir `COPYING` et `CONTRIBUTORS` pour les textes
de licence et les attributions ; `BUILD.md` conserve la notice technique reçue
du producteur en anglais.
