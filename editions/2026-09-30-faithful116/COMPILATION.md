# Recompiler la traduction française fidèle

Cette reconstruction conserve les lectures mathématiques de la source anglaise
du Stacks Project au commit `a04446e57ec1fbc252a871afcec7752fb2807b14`.
Les corrections proposées pour cette source ne sont pas appliquées au texte de
la traduction. Les versions françaises antérieures sont conservées séparément.

Le fichier `stacks_fr_faithful_116.tex` contient les 116 unités complètes, l’index
et la bibliographie. Ce n’est pas un simple fichier maître avec des entrées
manquantes. Les sources des chapitres sont également dans `chapters/`.

Le fichier cumulatif utilise les fichiers voisins `stacks-project-book.cls`
et `my.bib`, ainsi que les paquets ordinaires d’une distribution TeX : AMS,
Babel avec le français, Latin Modern, `xy`, `multicol`, `verbatim` et `hyperref`.
Il ne dépend d’aucune image extérieure ni d’une superposition de corrections.

Depuis ce répertoire, une distribution TeX complète permet de lancer :

```text
latexmk -norc -r tools/latexmkrc.pl -pdf -bibtex -interaction=nonstopmode -halt-on-error -file-line-error -recorder -outdir=build stacks_fr_faithful_116.tex
```

Dans l’espace de travail de production, toutes les compilations utilisent le
verrou machine `Global\InterlanguageTeXSlotV1`. Une compilation indépendante doit
être sérialisée avec les autres travaux TeX du même environnement.

Pour vérifier que le fichier cumulatif correspond exactement aux sources
modulaires, avec Python 3 :

```text
python tools/reassemble.py
```

Si le cumulatif a été supprimé, `--write-if-missing` permet de le reconstruire.
Les seules transformations d’assemblage sont celles du producteur conservées
dans `tools/pinned_assembler.py` : titres de chapitres, préfixes des identifiants
locaux, navigation, index, déplacement de la notice de licence et normalisation
typographique des apostrophes. Elles ne modifient pas les énoncés ou les preuves.

L’empreinte de chaque chapitre sélectionné est dans
`manifests/FRENCH_RESTORATION_ASSEMBLY_MANIFEST.json`. Le reçu
`manifests/ASSEMBLY_RECEIPT.json` lie la reconstruction cumulative à ces fichiers.
Le contrôle des sources ne constitue pas une relecture humaine experte.

La traduction reçue est attribuée à OpenAI Codex — GPT-5.6 Sol, effort Ultra,
selon la notice du producteur. Il s’agit d’une traduction indépendante, et non
d’une publication officielle ou approuvée par les auteurs du Stacks Project.
L’assemblage de cette reconstruction et sa présente notice technique sont
produits par OpenAI Codex — GPT-6.1 Sol, effort Ultra. Aucun contrôle humain
expert n’est revendiqué.
Les attributions originales et la licence GNU FDL restent dans `CONTRIBUTORS`
et `COPYING`.
