# Traduction française fidèle du projet Stacks

Cette reconstruction restitue le contenu mathématique du Stacks Project à la
révision `a04446e57ec1fbc252a871afcec7752fb2807b14`. Son objet est une traduction
française, non une réédition qui corrige ou augmente silencieusement les
énoncés et les preuves de la source anglaise.

Les lectures originales sont conservées même lorsqu’une correction a été
proposée. Les propositions d’errata restent séparées du texte traduit. Les
réparations linguistiques françaises justifiées ne sont pas annulées pour
rétablir une erreur de traduction. Les versions françaises antérieures,
comprenant des modifications éditoriales, restent conservées distinctement ;
elles ne sont pas présentées ici comme la traduction fidèle.

Le fichier cumulatif rassemble les 116 unités de source, dont la licence GNU
FDL, avec l’index général et la bibliographie. Quarante unités diffèrent du
témoin français public conservé, en raison des restaurations et des réparations
linguistiques retenues ; les 76 autres unités sont identiques à ce témoin.
Ce décompte ne correspond pas à un nombre de théorèmes faux ou corrigés.

## Lire et reconstruire les sources

Le texte complet est dans `stacks_fr_faithful_116.tex`. Les 116 sources
individuelles sont dans `chapters/`. Le fichier cumulatif et les fichiers voisins
`stacks-project-book.cls` et `my.bib` suffisent avec une distribution TeX
appropriée pour recompiler le lecteur ; les instructions sont dans
[COMPILATION.md](COMPILATION.md).

L’assemblage reconstruit d’abord exactement le témoin public à partir de ses
chapitres, après la seule normalisation des fins de ligne. Il substitue ensuite
les chapitres restaurés et vérifie deux assemblages identiques. Aucune
superposition de corrections mathématiques n’intervient dans ce processus.
La sélection et les empreintes sont documentées dans
[le manifeste](manifests/FRENCH_RESTORATION_ASSEMBLY_MANIFEST.json) et
[le reçu d’assemblage](manifests/ASSEMBLY_RECEIPT.json).

Le lecteur restauré a été recompilé : 8 372 pages, sans erreur fatale, référence
indéfinie, citation indéfinie ou demande de nouvelle passe dans le journal final.
Le cumulatif est reconstruit à l’identique à partir des sources incluses.
Ces contrôles ne sont pas une nouvelle relecture linguistique intégrale et ne
certifient pas chaque choix de traduction. Aucune relecture humaine experte
n’est revendiquée. Le contrôle visuel et la vérification des téléchargements
publics font l’objet de reçus séparés.

## Attribution et relecture

La traduction reçue est attribuée à OpenAI Codex — GPT-5.6 Sol, effort Ultra,
selon la notice du producteur. L’assemblage de la présente reconstruction et ses
notices sont produits par OpenAI Codex — GPT-6.1 Sol, effort Ultra. Les
attributions originales et la licence restent dans `CONTRIBUTORS` et `COPYING`.

Il s’agit d’une traduction indépendante réalisée avec l’assistance de l’IA,
non d’une publication officielle ou approuvée par les auteurs du Stacks
Project. Les relectures spécialisées de la traduction sont bienvenues. Les
dossiers de restauration distinguent les changements retirés, les variantes
françaises conservées et les propositions de correction de la source anglaise.
