# Longueur des modules

## Résultat et portée

La section complète est comparée : anglais L12346–12698 (353 lignes), français L12252–12596 (345 lignes), soit quinze paires comprenant définitions, énoncés, preuves, slogans et transitions. 167 occurrences sont reliées à des choix contextualisés. La lecture continue atteint 52 sections, 455 paires et 3820 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Trois opérations françaises : une construction R-sous-module réparée et deux clarifications indiquant un idéal maximal choisi, sans suggérer que l’anneau soit local. Aucun résultat, symbole ou renvoi ne change. Les autres passages sont conservés après comparaison intégrale.

Aucune nouvelle proposition de correction de la source n’est admise dans ce lot. Les conventions implicites sur les étapes strictes, les dimensions infinies et le produit 0·∞ sont notées ici sans modifier la traduction. Module fini reste le terme technique signifiant module de type fini, et simple n’est pas remplacé par indécomposable.

Lecture et réparations produites par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. L’appui documentaire est rétrospectif, non présenté comme une consultation lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch19.fr.tex) · [État précédent](staged/fr/010_algebra.prose-batch18.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH18_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH19_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH19_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH19_OCCURRENCES.json) · [Avant/après](ALGEBRA_PROSE_BATCH19_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH19_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH19_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH19_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH19_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH19_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Jean-François Dat — Algèbre ENS 2016–2017

[Source consultée](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/AlgebreM1/ENS1617.pdf) · [Fichier conservé](canon-consulted/fr-algebra/dat-algebre-ens1617.pdf)

Pages 83 et 84 entièrement lues, §1.8.3 et début de §1.8.4 ; page 83 rendue avec Poppler et inspectée.

Attestations courtes : « Modules de longueur finie », « chaîne strictement croissante de sous-modules », « module simple », « annulateur », « quotients successifs ».

Même définition de longueur, facteurs simples, annulateur et additivité ; le texte p.84 explicite le comptage des sauts dans les filtrations induites.

Limites : Le canon de langue ne remplace pas l'autorité mathématique Stacks. Ni semi-local ni homomorphisme local plat n'est ici revendiqué comme attestation verbatim. Consultation rétrospective, aucune relecture humaine.

SHA-256 : DB5B7FD8139D62C37D0DDDDC90EF22D3EDCF74CC663C5267815E4EA3CECBBB18.

### Antoine Ducros — Introduction à la théorie des schémas

[Source consultée](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Page 26 entièrement lue ; §§0.2.4.3–0.2.6.2.

Attestations courtes : « sous-module », « de type fini », « famille génératrice finie ».

Construction A-module et sous-module, génération finie distinguée de la présentation finie et du cardinal de l'ensemble.

Limites : La page n'atteste pas à elle seule toute la terminologie de la longueur et de la platitude. Module fini est conservé comme convention déjà définie dans le chapitre ; aucune nouvelle attestation de ce synonyme n'est inventée.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

## Les trois réparations françaises

### FR-ALGEBRA-B19-REPAIR-0001

Anglais L12461 ; français L12367.

Avant :
```tex
Soit $R$ un anneau d'idéal maximal $\mathfrak m$.
```

Après :
```tex
Soit $R$ un anneau ayant un idéal maximal $\mathfrak m$.
```

Clarification de la formulation française, pas découverte d'une hypothèse manquante. L'égalité avec la dimension à l'infini se lit avec la convention ∞ du texte, non comme une égalité de cardinaux infinis distincts.

### FR-ALGEBRA-B19-REPAIR-0002

Anglais L12485 ; français L12392.

Avant :
```tex
$S^{-1}N$ pour un certain sous-module $R$-module $N \subset M$, par le Lemme
```

Après :
```tex
$S^{-1}N$ pour un certain $R$-sous-module $N \subset M$, par le Lemme
```

Réparation grammaticale de sous-module R-module ; aucun symbole ni renvoi ne change.

### FR-ALGEBRA-B19-REPAIR-0003

Anglais L12491 ; français L12398.

Avant :
```tex
Soit $R$ un anneau dont l'idéal maximal $\mathfrak m$ est engendré par un nombre fini d'éléments.
```

Après :
```tex
Soit $R$ un anneau possédant un idéal maximal $\mathfrak m$ engendré par un nombre fini d'éléments.
```

Le déterminant indéfini rend explicite le choix d'un idéal maximal. On ne qualifie pas la version précédente de nouveau théorème faux ; on écarte une ambiguïté.

## Règles contextualisées

### FR-ALGEBRA-B19-RULE-LENGTH

Lire chaque chaîne avec ses extrémités, sa stricte croissance et ses facteurs ; longueur ne désigne pas un cardinal.

Canon : FR-ALGEBRA-B19-CANON-DAT.

### FR-ALGEBRA-B19-RULE-MODULE

Module fini signifie génération finie. Vérifier la structure de module et l'anneau de scalaires à chaque occurrence.

Canon : FR-ALGEBRA-B19-CANON-DUCROS.

### FR-ALGEBRA-B19-RULE-SIMPLE

Simple implique non nul et deux seuls sous-modules ; annulateur et quotients successifs sont lus dans leur preuve complète.

Canon : FR-ALGEBRA-B19-CANON-DAT.

### FR-ALGEBRA-B19-RULE-LOCAL

Distinguer un idéal maximal choisi, un anneau local, un morphisme local et la localisation ; justification contextuelle sans nouvelle attestation externe revendiquée.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B19-RULE-MAP

Préserver les qualifications des applications et leurs domaines ; local plat est plus précis que plat entre anneaux locaux.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B19-RULE-EXACT

L'additivité provient des chaînes strictes, des intersections et des images ; les degrés résiduels de la somme finale sont conservés.

Canon : FR-ALGEBRA-B19-CANON-DAT.

### FR-ALGEBRA-B19-RULE-LOGIC

Les quantificateurs, dépendances et équivalences sont vérifiés par lecture de chaque paire complète.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-length

Anglais L12346–12348 ; français L12252–12254.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12346) · FR-ALGEBRA-B19-CHOICE-0001.

Longueur est le terme attesté chez Dat, §1.8.3. La notation officielle length reste inchangée dans les formules ; le titre français ne crée pas une nouvelle notion.

Règles : FR-ALGEBRA-B19-RULE-LENGTH.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Length}
\label{section-length}
```

Français restauré :
```tex
\section{Longueur}
\label{section-length}
```

</details>

### 02 — definition-length

Anglais L12349–12378 ; français L12255–12284.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12349) · FR-ALGEBRA-B19-CHOICE-0002.

La longueur est le supremum des nombres de facteurs dans des chaînes strictes allant de zéro à M. Les mots chaîne, sous-module, longueur et raffinement sont lus avec cette définition, non comme une mesure de taille ensembliste. La distinction entre chaîne minimale et chaîne maximale pour le raffinement est conservée. Pour M nul, la définition donne zéro ; aucune exception artificielle n'est ajoutée. Dat emploie la même définition et le même cadre lexical.

Point particulier à relire : Ne pas confondre maximal pour le raffinement avec plus grand sous-module ; le texte ne prétend pas encore que toutes les chaînes maximales ont la même longueur.

Règles : FR-ALGEBRA-B19-RULE-LENGTH, FR-ALGEBRA-B19-RULE-MODULE, FR-ALGEBRA-B19-RULE-LOCAL, FR-ALGEBRA-B19-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-length}
Let $R$ be a ring. For any $R$-module $M$
we define the {\it length} of $M$ over $R$ by the
formula
$$
\text{length}_R(M)
=
\sup
\{
n
\mid
\exists\ 0 = M_0 \subset M_1 \subset \ldots \subset M_n = M,
\text{ }M_i \not = M_{i + 1}
\}.
$$
\end{definition}

\noindent
In other words it is the supremum of the lengths of chains
of submodules. There is an obvious notion of when a chain
of submodules is a refinement of another. This gives a
partial ordering on the collection of all chains of submodules,
with the smallest chain having the shape $0 = M_0 \subset M_1 = M$
if $M$ is not zero.
We note the obvious fact that if the length of
$M$ is finite, then every chain can be refined to a
maximal chain. But it is not as obvious that all maximal
chains have the same length (as we will see later).
```

Français restauré :
```tex
\begin{definition}
\label{definition-length}
Soit $R$ un anneau. Pour tout $R$-module $M$,
nous définissons la {\it longueur} de $M$ sur $R$ par la
formule
$$
\text{length}_R(M)
=
\sup
\{
n
\mid
\exists\ 0 = M_0 \subset M_1 \subset \ldots \subset M_n = M,
\text{ }M_i \not = M_{i + 1}
\}.
$$
\end{definition}

\noindent
Autrement dit, c'est le supremum des longueurs des chaînes
de sous-modules. Il existe une notion évidente de chaîne
de sous-modules qui raffine une autre. Cela donne un
ordre partiel sur l'ensemble de toutes les chaînes de sous-modules,
la chaîne minimale ayant la forme $0 = M_0 \subset M_1 = M$
si $M$ n'est pas nul.
Remarquons le fait évident que si la longueur de
$M$ est finie, toute chaîne peut être raffinée en une
chaîne maximale. Mais il est moins évident que toutes les chaînes maximales
ont la même longueur (comme nous le verrons plus loin).
```

</details>

### 03 — lemma-finite-length-finite

Anglais L12379–12392 ; français L12285–12298.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12379) · FR-ALGEBRA-B19-CHOICE-0003.

La finitude conclue est celle du module, c'est-à-dire l'existence d'une famille génératrice finie, et non la finitude de son ensemble sous-jacent. Module fini est conservé dans son sens technique déjà établi dans le chapitre. Ducros atteste la formulation explicite de type fini. La preuve omise dans l'anglais reste omise ; on ne la remplace pas par un argument nouveau.

Point particulier à relire : Fini est technique, pas cardinal. Aucune preuve ajoutée là où l'original la déclare omise.

Règles : FR-ALGEBRA-B19-RULE-LENGTH, FR-ALGEBRA-B19-RULE-MODULE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-finite-length-finite}
\begin{slogan}
Modules of finite length are finite.
\end{slogan}
Let $R$ be a ring.
Let $M$ be an $R$-module.
If $\text{length}_R(M) < \infty$ then $M$ is a finite $R$-module.
\end{lemma}

\begin{proof}
Omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-finite-length-finite}
\begin{slogan}
Les modules de longueur finie sont finis.
\end{slogan}
Soit $R$ un anneau.
Soit $M$ un $R$-module.
Si $\text{length}_R(M) < \infty$, alors $M$ est un $R$-module fini.
\end{lemma}

\begin{proof}
Démonstration omise.
\end{proof}
```

</details>

### 04 — lemma-length-additive

Anglais L12393–12419 ; français L12299–12325.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12393) · FR-ALGEBRA-B19-CHOICE-0004.

La suite est bien exacte courte, avec zéro aux deux extrémités. La preuve compare d'abord les filtrations construites à partir des deux termes extrêmes, puis les filtrations induites par intersection et image. Les deux sens des inégalités sont conservés. Nombre d'étapes doit se lire après suppression des répétitions dans les filtrations induites ; Dat explicite ces sauts p.84. Cette explication figure au dossier, sans ajout dans le texte diplomatique.

Point particulier à relire : Les répétitions doivent être retirées pour compter les étapes strictes des filtrations induites ; il s'agit d'une convention de lecture documentée, non d'une nouvelle correction de source.

Règles : FR-ALGEBRA-B19-RULE-LENGTH, FR-ALGEBRA-B19-RULE-MODULE, FR-ALGEBRA-B19-RULE-EXACT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-length-additive}
\begin{slogan}
Length is additive in short exact sequences.
\end{slogan}
If $0 \to M' \to M \to M'' \to 0$
is a short exact sequence of modules over $R$ then
the length of $M$ is the sum of the
lengths of $M'$ and $M''$.
\end{lemma}

\begin{proof}
Given filtrations of $M'$ and $M''$ of lengths $n', n''$
it is easy to make a corresponding filtration of $M$
of length $n' + n''$. Thus we see that $\text{length}_R M
\geq \text{length}_R M' + \text{length}_R M''$.
Conversely, given a filtration
$M_0 \subset M_1 \subset \ldots \subset M_n$ of
$M$ consider the induced filtrations
$M_i' = M_i \cap M'$ and $M_i'' = \Im(M_i \to M'')$.
Let $n'$ (resp.\ $n''$) be the number of steps in the filtration
$\{M'_i\}$ (resp.\ $\{M''_i\}$).
If $M_i' = M_{i + 1}'$ and $M_i'' = M_{i + 1}''$ then
$M_i = M_{i + 1}$. Hence we conclude that $n' + n'' \geq n$.
Combined with the earlier result we win.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-length-additive}
\begin{slogan}
La longueur est additive dans les suites exactes courtes.
\end{slogan}
Si $0 \to M' \to M \to M'' \to 0$
est une suite exacte courte de modules sur $R$, alors
la longueur de $M$ est la somme des
longueurs de $M'$ et $M''$.
\end{lemma}

\begin{proof}
Étant données des filtrations de $M'$ et $M''$ de longueurs $n', n''$,
il est facile de construire une filtration correspondante de $M$
de longueur $n' + n''$. Ainsi
$\text{length}_R M \geq \text{length}_R M' + \text{length}_R M''$.
Réciproquement, étant donnée une filtration
$M_0 \subset M_1 \subset \ldots \subset M_n$ de
$M$, considérons les filtrations induites
$M_i' = M_i \cap M'$ et $M_i'' = \Im(M_i \to M'')$.
Soit $n'$ (resp.\ $n''$) le nombre d'étapes de la filtration
$\{M'_i\}$ (resp.\ $\{M''_i\}$).
Si $M_i' = M_{i + 1}'$ et $M_i'' = M_{i + 1}''$, alors
$M_i = M_{i + 1}$. Nous concluons donc que $n' + n'' \geq n$.
Avec le résultat précédent, c'est démontré.
\end{proof}
```

</details>

### 05 — lemma-length-infinite

Anglais L12420–12443 ; français L12326–12349.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12420) · FR-ALGEBRA-B19-CHOICE-0005.

L'anneau est local ; aucune hypothèse noethérienne n'est introduite. La non-annulation de toutes les puissances implique une longueur infinie, et la reformulation est exactement sa contraposée. La chaîne et le raisonnement par l'unité 1−gf₂ sont conservés. Distinctes porte sur les étapes de la chaîne, non sur les seuls éléments f_i.

Règles : FR-ALGEBRA-B19-RULE-LENGTH, FR-ALGEBRA-B19-RULE-MODULE, FR-ALGEBRA-B19-RULE-LOCAL, FR-ALGEBRA-B19-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-length-infinite}
Let $R$ be a local ring with maximal ideal $\mathfrak m$.
If $M$ is an $R$-module and $\mathfrak m^n M \not = 0$ for all $n \geq 0$,
then $\text{length}_R(M) = \infty$. In other words, if $M$
has finite length then $\mathfrak m^nM = 0$ for some $n$.
\end{lemma}

\begin{proof}
Assume $\mathfrak m^n M \not = 0$ for all $n\geq 0$.
Choose $x \in M$ and $f_1, \ldots, f_n \in \mathfrak m$
such that $f_1f_2 \ldots f_n x \not = 0$.
The first $n$ steps in the filtration
$$
0 \subset R f_1 \ldots f_n x \subset R f_1 \ldots f_{n - 1} x
\subset \ldots \subset R x \subset M
$$
are distinct. For example, if
$R f_1 x = R f_1 f_2 x$ , then $f_1 x = g f_1 f_2 x$ for some $g$,
hence $(1 - gf_2) f_1 x = 0$ hence $f_1 x = 0$ as $1 - gf_2$ is a unit
which is a contradiction with the choice of $x$ and $f_1, \ldots, f_n$.
Hence the length is infinite.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-length-infinite}
Soit $R$ un anneau local d'idéal maximal $\mathfrak m$.
Si $M$ est un $R$-module et $\mathfrak m^n M \not = 0$ pour tout $n \geq 0$,
alors $\text{length}_R(M) = \infty$. Autrement dit, si $M$
est de longueur finie, alors $\mathfrak m^nM = 0$ pour un certain $n$.
\end{lemma}

\begin{proof}
Supposons que $\mathfrak m^n M \not = 0$ pour tout $n\geq 0$.
Choisissons $x \in M$ et $f_1, \ldots, f_n \in \mathfrak m$
tels que $f_1f_2 \ldots f_n x \not = 0$.
Les $n$ premières étapes de la filtration
$$
0 \subset R f_1 \ldots f_n x \subset R f_1 \ldots f_{n - 1} x
\subset \ldots \subset R x \subset M
$$
sont distinctes. Par exemple, si
$R f_1 x = R f_1 f_2 x$, alors $f_1 x = g f_1 f_2 x$ pour un certain $g$,
d'où $(1 - gf_2) f_1 x = 0$, donc $f_1 x = 0$ puisque $1 - gf_2$ est une unité,
ce qui contredit le choix de $x$ et de $f_1, \ldots, f_n$.
Ainsi la longueur est infinie.
\end{proof}
```

</details>

### 06 — lemma-length-independent

Anglais L12444–12458 ; français L12350–12364.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12444) · FR-ALGEBRA-B19-CHOICE-0006.

La restriction des scalaires peut ajouter des sous-modules : la longueur sur R est donc supérieure ou égale à celle sur S. La surjectivité du morphisme suffit pour l'égalité ; aucune platitude n'est requise. Les deux preuves et les deux structures de module restent distinguées.

Règles : FR-ALGEBRA-B19-RULE-LENGTH, FR-ALGEBRA-B19-RULE-MODULE, FR-ALGEBRA-B19-RULE-MAP.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-length-independent}
Let $R \to S$ be a ring map. Let $M$ be an $S$-module.
We always have $\text{length}_R(M) \geq \text{length}_S(M)$.
If $R \to S$ is surjective then equality holds.
\end{lemma}

\begin{proof}
A filtration of $M$ by $S$-submodules gives rise a filtration
of $M$ by $R$-submodules. This proves the inequality.
And if $R \to S$ is surjective, then any $R$-submodule
of $M$ is automatically an $S$-submodule. Hence equality
in this case.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-length-independent}
Soit $R \to S$ un morphisme d'anneaux. Soit $M$ un $S$-module.
Nous avons toujours $\text{length}_R(M) \geq \text{length}_S(M)$.
Si $R \to S$ est surjectif, alors il y a égalité.
\end{lemma}

\begin{proof}
Une filtration de $M$ par des $S$-sous-modules donne une filtration
de $M$ par des $R$-sous-modules. Cela démontre l'inégalité.
Et si $R \to S$ est surjectif, tout $R$-sous-module
de $M$ est automatiquement un $S$-sous-module. Il y a donc égalité
dans ce cas.
\end{proof}
```

</details>

### 07 — lemma-dimension-is-length

Anglais L12459–12475 ; français L12365–12382.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12459) · FR-ALGEBRA-B19-CHOICE-0007.

La source choisit un idéal maximal sans supposer l'anneau local. Ayant un idéal maximal remplace d'idéal maximal pour rendre ce choix explicite sans changer la portée mathématique. La condition est mM=0, non seulement une annulation par une puissance. La comparaison avec la dimension du corps quotient et l'équivalence entre base finie et génération finie sont conservées. La longueur prend des valeurs dans N∪{∞} : le passage ne distingue pas les cardinaux infinis des dimensions.

Point particulier à relire : Clarification de la formulation française, pas découverte d'une hypothèse manquante. L'égalité avec la dimension à l'infini se lit avec la convention ∞ du texte, non comme une égalité de cardinaux infinis distincts.

Règles : FR-ALGEBRA-B19-RULE-LENGTH, FR-ALGEBRA-B19-RULE-MODULE, FR-ALGEBRA-B19-RULE-LOCAL, FR-ALGEBRA-B19-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-dimension-is-length}
Let $R$ be a ring with maximal ideal $\mathfrak m$.
Suppose that $M$ is an $R$-module with
$\mathfrak m M  =  0$. Then the length of $M$ as
an $R$-module agrees with the dimension of $M$ as
a $R/\mathfrak m$ vector space.
The length is finite if and only if $M$ is a finite $R$-module.
\end{lemma}

\begin{proof}
The first part is a special case of Lemma \ref{lemma-length-independent}.
Thus the length is finite if and only if $M$ has a finite basis
as a $R/\mathfrak m$-vector space if and only if $M$ has a finite
set of generators as an $R$-module.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-dimension-is-length}
Soit $R$ un anneau ayant un idéal maximal $\mathfrak m$.
Supposons que $M$ soit un $R$-module tel que
$\mathfrak m M  =  0$. Alors la longueur de $M$ comme
$R$-module coïncide avec la dimension de $M$ comme
espace vectoriel sur $R/\mathfrak m$.
La longueur est finie si et seulement si $M$ est un $R$-module fini.
\end{lemma}

\begin{proof}
La première assertion est un cas particulier du
Lemme \ref{lemma-length-independent}.
Ainsi la longueur est finie si et seulement si $M$ possède une base finie
comme espace vectoriel sur $R/\mathfrak m$, si et seulement si $M$ possède un ensemble fini
de générateurs comme $R$-module.
\end{proof}
```

</details>

### 08 — lemma-length-localize

Anglais L12476–12488 ; français L12383–12395.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12476) · FR-ALGEBRA-B19-CHOICE-0008.

La localisation ne peut augmenter la longueur, puisque tout sous-module localisé provient d'un sous-module de M. La double construction sous-module R-module est réparée en R-sous-module, conformément à la construction française chez Ducros. Aucun changement d'anneau ni inversion de l'inégalité. Le cas d'une localisation nulle reste couvert, avec longueur zéro.

Point particulier à relire : Réparation grammaticale de sous-module R-module ; aucun symbole ni renvoi ne change.

Règles : FR-ALGEBRA-B19-RULE-MODULE, FR-ALGEBRA-B19-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-length-localize}
Let $R$ be a ring. Let $M$ be an $R$-module. Let $S \subset R$ be
a multiplicative subset. Then
$\text{length}_R(M) \geq \text{length}_{S^{-1}R}(S^{-1}M)$.
\end{lemma}

\begin{proof}
Any submodule $N' \subset S^{-1}M$ is of the form
$S^{-1}N$ for some $R$-submodule $N \subset M$, by Lemma
\ref{lemma-submodule-localization}. The lemma follows.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-length-localize}
Soit $R$ un anneau. Soit $M$ un $R$-module. Soit $S \subset R$ un
ensemble multiplicatif. Alors
$\text{length}_R(M) \geq \text{length}_{S^{-1}R}(S^{-1}M)$.
\end{lemma}

\begin{proof}
Tout sous-module $N' \subset S^{-1}M$ est de la forme
$S^{-1}N$ pour un certain $R$-sous-module $N \subset M$, par le Lemme
\ref{lemma-submodule-localization}. Le lemme en découle.
\end{proof}
```

</details>

### 09 — lemma-length-finite

Anglais L12489–12507 ; français L12396–12415.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12489) · FR-ALGEBRA-B19-CHOICE-0009.

Il suffit d'un idéal maximal de type fini ; R n'est pas supposé local. Un anneau possédant un idéal maximal rend cette portée explicite, là où dont l'idéal maximal pouvait suggérer l'unicité. Les deux hypothèses de finitude, celle de l'idéal et celle du module, ainsi que l'annulation par une puissance sont conservées. Chaque quotient successif est annihilé par m et de type fini ; la preuve conclut par additivité.

Point particulier à relire : Le déterminant indéfini rend explicite le choix d'un idéal maximal. On ne qualifie pas la version précédente de nouveau théorème faux ; on écarte une ambiguïté.

Règles : FR-ALGEBRA-B19-RULE-LENGTH, FR-ALGEBRA-B19-RULE-MODULE, FR-ALGEBRA-B19-RULE-SIMPLE, FR-ALGEBRA-B19-RULE-LOCAL, FR-ALGEBRA-B19-RULE-EXACT, FR-ALGEBRA-B19-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-length-finite}
Let $R$ be a ring with finitely generated
maximal ideal $\mathfrak m$. (For example $R$ Noetherian.)
Suppose that $M$ is a finite $R$-module with
$\mathfrak m^n M  =  0$ for some $n$.
Then $\text{length}_R(M) < \infty$.
\end{lemma}

\begin{proof}
Consider the filtration
$0 = \mathfrak m^n M \subset
\mathfrak m^{n-1} M \subset
\ldots \subset \mathfrak m M \subset M$.
All of the subquotients are finitely generated $R$-modules
to which Lemma \ref{lemma-dimension-is-length} applies. We conclude
by additivity, see Lemma \ref{lemma-length-additive}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-length-finite}
Soit $R$ un anneau possédant un idéal maximal $\mathfrak m$ engendré par un nombre fini d'éléments.
(Par exemple, $R$ est noethérien.)
Supposons que $M$ soit un $R$-module fini tel que
$\mathfrak m^n M  =  0$ pour un certain $n$.
Alors $\text{length}_R(M) < \infty$.
\end{lemma}

\begin{proof}
Considérons la filtration
$0 = \mathfrak m^n M \subset
\mathfrak m^{n-1} M \subset
\ldots \subset \mathfrak m M \subset M$.
Tous les quotients successifs sont des $R$-modules de type fini
auxquels s'applique le Lemme \ref{lemma-dimension-is-length}. Nous concluons
par additivité, voir le Lemme \ref{lemma-length-additive}.
\end{proof}
```

</details>

### 10 — definition-simple-module

Anglais L12508–12515 ; français L12416–12423.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12508) · FR-ALGEBRA-B19-CHOICE-0010.

Simple signifie non nul et sans sous-module autre que zéro et lui-même. Dat donne exactement cette notion p.83. Ne pas remplacer simple par indécomposable : cette dernière propriété serait plus faible. La non-nullité reste explicite.

Point particulier à relire : Simple et indécomposable ne sont pas synonymes.

Règles : FR-ALGEBRA-B19-RULE-MODULE, FR-ALGEBRA-B19-RULE-SIMPLE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-simple-module}
Let $R$ be a ring. Let $M$ be an $R$-module.
We say $M$ is {\it simple} if $M \not = 0$ and
every submodule of $M$ is either equal to $M$ or
to $0$.
\end{definition}
```

Français restauré :
```tex
\begin{definition}
\label{definition-simple-module}
Soit $R$ un anneau. Soit $M$ un $R$-module.
Nous disons que $M$ est {\it simple} si $M \not = 0$ et
tout sous-module de $M$ est soit égal à $M$, soit
à $0$.
\end{definition}
```

</details>

### 11 — lemma-characterize-length-1

Anglais L12516–12544 ; français L12424–12452.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12516) · FR-ALGEBRA-B19-CHOICE-0011.

Les trois assertions restent équivalentes : simplicité, longueur un et quotient par un idéal maximal. Annulateur est attesté chez Dat avec la même définition. Le choix d'un élément non nul, sa génération du module, le morphisme du quotient et la contradiction obtenue à partir d'un sous-module non trivial sont tous conservés. La notation condensée I inclus dans m dans la phrase de choix est héritée de l'anglais, non une correction mathématique apportée par la traduction.

Point particulier à relire : La phrase officielle Let I subset m be a maximal ideal contenant I est condensée ; le lecteur comprend que m est choisi maximal. La formule officielle et sa traduction sont préservées.

Règles : FR-ALGEBRA-B19-RULE-LENGTH, FR-ALGEBRA-B19-RULE-MODULE, FR-ALGEBRA-B19-RULE-SIMPLE, FR-ALGEBRA-B19-RULE-LOCAL, FR-ALGEBRA-B19-RULE-MAP, FR-ALGEBRA-B19-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-length-1}
Let $R$ be a ring. Let $M$ be an $R$-module.
The following are equivalent:
\begin{enumerate}
\item $M$ is simple,
\item $\text{length}_R(M) = 1$, and
\item $M \cong R/\mathfrak m$ for some maximal ideal
$\mathfrak m \subset R$.
\end{enumerate}
\end{lemma}

\begin{proof}
Let $\mathfrak m$ be a maximal ideal of $R$.
By Lemma \ref{lemma-dimension-is-length} the module
$R/\mathfrak m$ has length $1$. The equivalence of
the first two assertions is tautological.
Suppose that $M$ is simple. Choose $x \in M$, $x \not = 0$.
As $M$ is simple we have $M = R \cdot x$.
Let $I \subset R$ be the annihilator of $x$, i.e.,
$I = \{f \in R \mid fx = 0\}$. The map $R/I \to M$,
$f \bmod I \mapsto fx$ is an isomorphism, hence
$R/I$ is a simple $R$-module. Since $R/I \not = 0$ we see $I \not = R$.
Let $I \subset \mathfrak m$ be a maximal ideal containing $I$.
If $I \not = \mathfrak m$, then $\mathfrak m /I \subset R/I$
is a nontrivial submodule contradicting the simplicity
of $R/I$. Hence we see $I = \mathfrak m$ as desired.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-characterize-length-1}
Soit $R$ un anneau. Soit $M$ un $R$-module.
Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item $M$ est simple,
\item $\text{length}_R(M) = 1$, et
\item $M \cong R/\mathfrak m$ pour un idéal maximal
$\mathfrak m \subset R$.
\end{enumerate}
\end{lemma}

\begin{proof}
Soit $\mathfrak m$ un idéal maximal de $R$.
Par le Lemme \ref{lemma-dimension-is-length}, le module
$R/\mathfrak m$ est de longueur $1$. L'équivalence des deux
premières assertions est tautologique.
Supposons que $M$ soit simple. Choisissons $x \in M$, $x \not = 0$.
Comme $M$ est simple, nous avons $M = R \cdot x$.
Soit $I \subset R$ l'annulateur de $x$, c'est-à-dire
$I = \{f \in R \mid fx = 0\}$. L'application $R/I \to M$,
$f \bmod I \mapsto fx$ est un isomorphisme, donc
$R/I$ est un $R$-module simple. Comme $R/I \not = 0$, nous voyons que $I \not = R$.
Soit $I \subset \mathfrak m$ un idéal maximal contenant $I$.
Si $I \not = \mathfrak m$, alors $\mathfrak m /I \subset R/I$
est un sous-module non trivial, ce qui contredit la simplicité
de $R/I$. Nous obtenons donc $I = \mathfrak m$, comme voulu.
\end{proof}
```

</details>

### 12 — lemma-simple-pieces

Anglais L12545–12601 ; français L12453–12509.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12545) · FR-ALGEBRA-B19-CHOICE-0012.

Maximale concerne une chaîne pour le raffinement, et non chaque sous-module pris séparément. Les facteurs sont simples et de la forme R/m_i ; le nombre de facteurs égale la longueur. La dernière assertion compte ceux associés à un idéal maximal donné et les identifie à la longueur localisée. L'exactitude de la localisation et les deux cas du corps résiduel sont conservés. Seuls les deux if dans un même affichage deviennent si.

Point particulier à relire : L'exception linguistique ne porte que sur if→si, deux fois dans un affichage ; les idéaux primés et non primés restent distincts.

Règles : FR-ALGEBRA-B19-RULE-LENGTH, FR-ALGEBRA-B19-RULE-MODULE, FR-ALGEBRA-B19-RULE-SIMPLE, FR-ALGEBRA-B19-RULE-LOCAL, FR-ALGEBRA-B19-RULE-EXACT, FR-ALGEBRA-B19-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-simple-pieces}
Let $R$ be a ring. Let $M$ be a finite length $R$-module.
Choose any maximal chain of submodules
$$
0 = M_0 \subset M_1 \subset M_2 \subset \ldots \subset M_n = M
$$
with $M_i \not = M_{i-1}$, $i = 1, \ldots, n$. Then
\begin{enumerate}
\item $n = \text{length}_R(M)$,
\item each $M_i/M_{i-1}$ is simple,
\item each $M_i/M_{i-1}$ is of the form
$R/\mathfrak m_i$ for some maximal ideal $\mathfrak m_i$,
\item given a maximal ideal $\mathfrak m \subset R$
we have
$$
\# \{i \mid \mathfrak m_i = \mathfrak m\}
=
\text{length}_{R_{\mathfrak m}} (M_{\mathfrak m}).
$$
\end{enumerate}
\end{lemma}

\begin{proof}
If $M_i/M_{i-1}$ is not simple then we can refine the filtration
and the filtration is not maximal. Thus we see that $M_i/M_{i-1}$
is simple. By Lemma \ref{lemma-characterize-length-1} the modules
$M_i/M_{i-1}$ have length $1$ and are of the form $R/\mathfrak m_i$
for some maximal ideals $\mathfrak m_i$. By additivity of length,
Lemma \ref{lemma-length-additive}, we see $n = \text{length}_R(M)$.
Since localization is exact, we see that
$$
0 = (M_0)_{\mathfrak m}
\subset (M_1)_{\mathfrak m}
\subset (M_2)_{\mathfrak m}
\subset \ldots
\subset (M_n)_{\mathfrak m} = M_{\mathfrak m}
$$
is a filtration of $M_{\mathfrak m}$ with successive quotients
$(M_i/M_{i-1})_{\mathfrak m}$. Thus the last statement follows
directly from the fact that given maximal ideals $\mathfrak m$,
$\mathfrak m'$ of $R$ we have
$$
(R/\mathfrak m')_{\mathfrak m}
\cong
\left\{
\begin{matrix}
0 &
\text{if } \mathfrak m \not = \mathfrak m', \\
R_{\mathfrak m}/\mathfrak m R_{\mathfrak m} &
\text{if } \mathfrak m  = \mathfrak m'
\end{matrix}
\right.
$$
This we leave to the reader.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-simple-pieces}
Soit $R$ un anneau. Soit $M$ un $R$-module de longueur finie.
Choisissons une chaîne maximale quelconque de sous-modules
$$
0 = M_0 \subset M_1 \subset M_2 \subset \ldots \subset M_n = M
$$
telle que $M_i \not = M_{i-1}$, $i = 1, \ldots, n$. Alors
\begin{enumerate}
\item $n = \text{length}_R(M)$,
\item chaque $M_i/M_{i-1}$ est simple,
\item chaque $M_i/M_{i-1}$ est de la forme
$R/\mathfrak m_i$ pour un certain idéal maximal $\mathfrak m_i$,
\item étant donné un idéal maximal $\mathfrak m \subset R$,
nous avons
$$
\# \{i \mid \mathfrak m_i = \mathfrak m\}
=
\text{length}_{R_{\mathfrak m}} (M_{\mathfrak m}).
$$
\end{enumerate}
\end{lemma}

\begin{proof}
Si $M_i/M_{i-1}$ n'est pas simple, nous pouvons raffiner la filtration
et la filtration n'est pas maximale. Ainsi $M_i/M_{i-1}$
est simple. Par le Lemme \ref{lemma-characterize-length-1}, les modules
$M_i/M_{i-1}$ sont de longueur $1$ et sont de la forme $R/\mathfrak m_i$
pour certains idéaux maximaux $\mathfrak m_i$. Par additivité de la longueur,
Lemme \ref{lemma-length-additive}, nous voyons que $n = \text{length}_R(M)$.
Comme la localisation est exacte, nous voyons que
$$
0 = (M_0)_{\mathfrak m}
\subset (M_1)_{\mathfrak m}
\subset (M_2)_{\mathfrak m}
\subset \ldots
\subset (M_n)_{\mathfrak m} = M_{\mathfrak m}
$$
est une filtration de $M_{\mathfrak m}$ dont les quotients successifs sont
$(M_i/M_{i-1})_{\mathfrak m}$. La dernière assertion découle alors
directement du fait que pour des idéaux maximaux $\mathfrak m$,
$\mathfrak m'$ de $R$, nous avons
$$
(R/\mathfrak m')_{\mathfrak m}
\cong
\left\{
\begin{matrix}
0 &
\text{si } \mathfrak m \not = \mathfrak m', \\
R_{\mathfrak m}/\mathfrak m R_{\mathfrak m} &
\text{si } \mathfrak m  = \mathfrak m'
\end{matrix}
\right.
$$
Nous laissons cela au lecteur.
\end{proof}
```

</details>

### 13 — lemma-pushdown-module

Anglais L12602–12640 ; français L12510–12548.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12602) · FR-ALGEBRA-B19-CHOICE-0013.

A est local et B semi-local ; tous les idéaux maximaux énumérés de B sont au-dessus de celui de A, avec degrés résiduels finis. La somme est pondérée par ces degrés : ils ne sont ni omis ni remplacés par un nombre de points. La preuve utilise les facteurs simples de M et l'additivité de la longueur. Au-dessus de désigne la contraction de l'idéal maximal, pas un ordre spatial.

Point particulier à relire : Les pages du canon consultées n'attestent pas séparément l'expression semi-local ni au-dessus de ; choix conservés sur analyse du contexte, pas présentés comme attestations nouvelles.

Règles : FR-ALGEBRA-B19-RULE-LENGTH, FR-ALGEBRA-B19-RULE-MODULE, FR-ALGEBRA-B19-RULE-LOCAL, FR-ALGEBRA-B19-RULE-MAP, FR-ALGEBRA-B19-RULE-EXACT, FR-ALGEBRA-B19-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-pushdown-module}
Let $A$ be a local ring with maximal ideal $\mathfrak m$.
Let $B$ be a semi-local ring with maximal ideals $\mathfrak m_i$,
$i = 1, \ldots, n$.
Suppose that $A \to B$ is a homomorphism such that each $\mathfrak m_i$
lies over $\mathfrak m$ and such that
$$
[\kappa(\mathfrak m_i) : \kappa(\mathfrak m)] < \infty.
$$
Let $M$ be a $B$-module of finite length.
Then
$$
\text{length}_A(M) = \sum\nolimits_{i = 1, \ldots, n}
[\kappa(\mathfrak m_i) : \kappa(\mathfrak m)]
\text{length}_{B_{\mathfrak m_i}}(M_{\mathfrak m_i}),
$$
in particular $\text{length}_A(M) < \infty$.
\end{lemma}

\begin{proof}
Choose a maximal chain
$$
0 = M_0
\subset M_1
\subset M_2
\subset \ldots
\subset M_m = M
$$
by $B$-submodules as in Lemma \ref{lemma-simple-pieces}.
Then each quotient $M_j/M_{j - 1}$ is isomorphic to
$\kappa(\mathfrak m_{i(j)})$ for some $i(j) \in \{1, \ldots, n\}$.
Moreover
$\text{length}_A(\kappa(\mathfrak m_i)) =
[\kappa(\mathfrak m_i) : \kappa(\mathfrak m)]$ by
Lemma \ref{lemma-dimension-is-length}. The lemma follows
by additivity of lengths (Lemma \ref{lemma-length-additive}).
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-pushdown-module}
Soit $A$ un anneau local d'idéal maximal $\mathfrak m$.
Soit $B$ un anneau semi-local d'idéaux maximaux $\mathfrak m_i$,
$i = 1, \ldots, n$.
Supposons que $A \to B$ soit un homomorphisme tel que chaque $\mathfrak m_i$
soit au-dessus de $\mathfrak m$ et tel que
$$
[\kappa(\mathfrak m_i) : \kappa(\mathfrak m)] < \infty.
$$
Soit $M$ un $B$-module de longueur finie.
Alors
$$
\text{length}_A(M) = \sum\nolimits_{i = 1, \ldots, n}
[\kappa(\mathfrak m_i) : \kappa(\mathfrak m)]
\text{length}_{B_{\mathfrak m_i}}(M_{\mathfrak m_i}),
$$
en particulier $\text{length}_A(M) < \infty$.
\end{lemma}

\begin{proof}
Choisissons une chaîne maximale
$$
0 = M_0
\subset M_1
\subset M_2
\subset \ldots
\subset M_m = M
$$
par des $B$-sous-modules comme dans le Lemme \ref{lemma-simple-pieces}.
Alors chaque quotient $M_j/M_{j - 1}$ est isomorphe à
$\kappa(\mathfrak m_{i(j)})$ pour un certain $i(j) \in \{1, \ldots, n\}$.
De plus
$\text{length}_A(\kappa(\mathfrak m_i)) =
[\kappa(\mathfrak m_i) : \kappa(\mathfrak m)]$ par le
Lemme \ref{lemma-dimension-is-length}. Le lemme découle
de l'additivité des longueurs (Lemme \ref{lemma-length-additive}).
\end{proof}
```

</details>

### 14 — lemma-pullback-module

Anglais L12641–12672 ; français L12549–12579.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12641) · FR-ALGEBRA-B19-CHOICE-0014.

Le morphisme est local et plat entre anneaux locaux ; la localité du morphisme ne se déduit pas du seul fait que les anneaux soient locaux. Le français conserve bien ces trois qualifications et la fidèle platitude utilisée dans la preuve. La longueur après extension des scalaires est multipliée par celle de la fibre fermée. La conclusion de finitude comporte explicitement la finitude de cette fibre. Les cas infinis sont conservés, non supprimés pour simplifier l'énoncé.

Point particulier à relire : Pour le module nul et une fibre de longueur infinie, le produit se lit avec 0·∞=0. Convention implicite documentée ici, non ajoutée au texte ni admise comme erreur de source.

Règles : FR-ALGEBRA-B19-RULE-LENGTH, FR-ALGEBRA-B19-RULE-MODULE, FR-ALGEBRA-B19-RULE-LOCAL, FR-ALGEBRA-B19-RULE-MAP, FR-ALGEBRA-B19-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-pullback-module}
Let $A \to B$ be a flat local homomorphism of local rings.
Then for any $A$-module $M$ we have
$$
\text{length}_A(M) \text{length}_B(B/\mathfrak m_AB)
=
\text{length}_B(M \otimes_A B).
$$
In particular, if $\text{length}_B(B/\mathfrak m_AB) < \infty$
then $M$ has finite length if and only if $M \otimes_A B$ has finite length.
\end{lemma}

\begin{proof}
The ring map $A \to B$ is faithfully flat by
Lemma \ref{lemma-local-flat-ff}.
Hence if $0 = M_0 \subset M_1 \subset \ldots \subset M_n = M$
is a chain of length $n$ in $M$, then the corresponding chain
$0 = M_0 \otimes_A B \subset M_1 \otimes_A B \subset
\ldots \subset M_n \otimes_A B = M \otimes_A B$ has length $n$
also. This proves
$\text{length}_A(M) = \infty \Rightarrow
\text{length}_B(M \otimes_A B) = \infty$.
Next, assume $\text{length}_A(M) < \infty$. In this case we see
that $M$ has a filtration of length $\ell = \text{length}_A(M)$
whose quotients are $A/\mathfrak m_A$. Arguing as above
we see that $M \otimes_A B$ has a filtration of length $\ell$
whose quotients are isomorphic to
$B \otimes_A A/\mathfrak m_A =  B/\mathfrak m_AB$.
Thus the lemma follows.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-pullback-module}
Soit $A \to B$ un homomorphisme local plat d'anneaux locaux.
Alors, pour tout $A$-module $M$, nous avons
$$
\text{length}_A(M) \text{length}_B(B/\mathfrak m_AB)
=
\text{length}_B(M \otimes_A B).
$$
En particulier, si $\text{length}_B(B/\mathfrak m_AB) < \infty$,
alors $M$ est de longueur finie si et seulement si $M \otimes_A B$ est de longueur finie.
\end{lemma}

\begin{proof}
Le morphisme d'anneaux $A \to B$ est fidèlement plat par le
Lemme \ref{lemma-local-flat-ff}.
Ainsi, si $0 = M_0 \subset M_1 \subset \ldots \subset M_n = M$
est une chaîne de longueur $n$ dans $M$, la chaîne correspondante
$0 = M_0 \otimes_A B \subset M_1 \otimes_A B \subset
\ldots \subset M_n \otimes_A B = M \otimes_A B$ est aussi de longueur $n$.
Cela démontre
$\text{length}_A(M) = \infty \Rightarrow
\text{length}_B(M \otimes_A B) = \infty$.
Supposons maintenant $\text{length}_A(M) < \infty$. Dans ce cas, $M$ possède une filtration de longueur $\ell = \text{length}_A(M)$
dont les quotients sont $A/\mathfrak m_A$. En raisonnant comme ci-dessus,
nous voyons que $M \otimes_A B$ possède une filtration de longueur $\ell$
dont les quotients sont isomorphes à
$B \otimes_A A/\mathfrak m_A =  B/\mathfrak m_AB$.
Le lemme en découle.
\end{proof}
```

</details>

### 15 — lemma-pullback-transitive

Anglais L12673–12698 ; français L12580–12596.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12673) · FR-ALGEBRA-B19-CHOICE-0015.

Les deux morphismes sont locaux plats. Le produit des longueurs des deux fibres est la longueur de la fibre composée, avec les trois idéaux et anneaux à leur place. La preuve applique exactement le lemme précédent à B→C et au B-module B/m_AB ; aucune hypothèse de finitude n'est ajoutée.

Point particulier à relire : Aucun renommage des idéaux des trois anneaux ; ne pas confondre la fibre composée avec la seconde fibre seule.

Règles : FR-ALGEBRA-B19-RULE-MODULE, FR-ALGEBRA-B19-RULE-LOCAL, FR-ALGEBRA-B19-RULE-MAP.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-pullback-transitive}
Let $A \to B \to C$ be flat local homomorphisms of local rings. Then
$$
\text{length}_B(B/\mathfrak m_A B)
\text{length}_C(C/\mathfrak m_B C)
=
\text{length}_C(C/\mathfrak m_A C)
$$
\end{lemma}

\begin{proof}
Follows from Lemma \ref{lemma-pullback-module} applied to the ring map
$B \to C$ and the $B$-module $M = B/\mathfrak m_A B$
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-pullback-transitive}
Soient $A \to B \to C$ des homomorphismes locaux plats d'anneaux locaux. Alors
$$
\text{length}_B(B/\mathfrak m_A B)
\text{length}_C(C/\mathfrak m_B C)
=
\text{length}_C(C/\mathfrak m_A C)
$$
\end{lemma}

\begin{proof}
Cela résulte du Lemme \ref{lemma-pullback-module} appliqué au morphisme d'anneaux
$B \to C$ et au $B$-module $M = B/\mathfrak m_A B$.
\end{proof}
```

</details>

## Contrôles et suite

Les 221 régions mathématiques concordent avec une seule exception linguistique exacte : deux if deviennent si dans le même affichage. Le préfixe de 9 028 régions passe avec vingt-sept exceptions linguistiques exactes, dont vingt-six antérieures. Aucun symbole mathématique français ne change depuis le lot précédent.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items restent identiques. Il n’y a pas de citation bibliographique ni de titre facultatif traduit dans ce lot. Les opérations inverses retrouvent le lot précédent puis tous les octets du témoin public préservé. Préfixe déjà relu et suffixe encore non relu sont inchangés.

Les 455 paires sont contiguës, sans lacune ni chevauchement. Les vérifications mécaniques complètent la lecture du sens ; elles ne la remplacent pas. Prochaine lecture : Anneaux artiniens, anglais L12699 / français L12597. Aucun nouveau PDF ni publication dans ce lot ; restauration globale toujours en cours.

