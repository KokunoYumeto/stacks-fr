# Anneaux gradués

## Résultat et portée

Une section complète est comparée : anglais L13199–13363 (165 lignes), français L13049–13208 (160 lignes), soit quatre paires complètes. 103 occurrences sont contextualisées. Couverture continue : 56 sections, 482 paires et 4239 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Trois réparations françaises : idéal irrelevant remplace le calque idéal non pertinent, une suite répare la phrase sur l’exactitude à chaque degré, et Théorème localise le libellé d’une citation. La variante tordu est conservée sur attestation avec la même convention de degré. Aucun résultat, symbole mathématique ni renvoi n’est modifié.

Ce dossier distingue fidélité de traduction et justification lexicale. Les difficultés de formulation de l’original sont expliquées dans les notes de lecture, sans nouvelle admission au registre ni ajout à la traduction.

Lecture et réparations produites par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. L’appui documentaire est rétrospectif, non présenté comme une consultation lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch22.fr.tex) · [État précédent](staged/fr/010_algebra.prose-batch21.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH21_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH22_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH22_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH22_OCCURRENCES.json) · [Avant/après](ALGEBRA_PROSE_BATCH22_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH22_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH22_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH22_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH22_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH22_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Antoine Ducros — Introduction à la théorie des schémas

[Source consultée](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages 271–273 entièrement lues, §§6.1.1–6.1.6.3.

Attestations courtes : « anneau gradué », « composantes homogènes », « idéal homogène », « en degrés positifs ».

Sommes directes, degré, homogénéité et localisations graduées dans le registre des schémas projectifs.

Limites : Ducros permet les degrés négatifs pour un anneau et emploie une convention de degré de morphisme différente ; Stacks garde ses propres conventions. Ce passage n'atteste pas idéal irrelevant.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

### D. Schaub — Multiplicité et dépendance intégrale sur un idéal

[Source consultée](https://www.numdam.org/item/PSMIR_1976___4_A1_0.pdf) · [Fichier conservé](canon-consulted/fr-algebra/multiplicite-dependance-integrale-1976.pdf)

Page PDF 4 / imprimée 3 entièrement lue, définition 5 et début de la proposition 2 ; page rendue et inspectée.

Attestations courtes : « un idéal gradué est irrelevant », « un idéal irrelevant ».

Attestation française d'irrelevant dans l'algèbre graduée, justifiant le remplacement du calque non pertinent.

Limites : La définition porte sur la propriété d'un idéal contenant une puissance de l'idéal des degrés positifs ; la définition exacte du S₊ nommé ici reste celle de Stacks. Les équivalences additionnelles de Schaub ne sont pas importées.

SHA-256 : DFB4EF15B0D6BAA348EB469B727B2967E9EB40BE4F42B3E6FB803186F3D538A3.

### Jean-François Dat — Schémas

[Source consultée](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/Schemas/Schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/dat-schemas.pdf)

Page 61 entièrement lue, §2.7.7 Décalage et début du §2.7.8.

Attestations courtes : « Décalage », « décalé », « module gradué ».

M(n)_d=M_{n+d} est la même convention de décalage que dans Stacks ; cette alternative française est documentée.

Limites : Ne justifie pas de remplacer tous les emplois de tordu ni de modifier les hypothèses de génération en degré un dans les résultats associés.

SHA-256 : 9298B062AC2BDF64161A107980A30F98E1F2DF6DEB4DA98E1FEB21BA494D26A1.

### Gaspard Fougea et Romain Gourvil — Théorème des Syzygies de Hilbert

[Source consultée](https://www.math.ens.psl.eu/shared-files/9610/?Gourvil_Fougea.pdf=) · [Fichier conservé](canon-consulted/fr-algebra/gourvil-fougea-modules-gradues.pdf)

Page 8 entièrement lue, définitions 2.27–2.29 ; titre et auteurs vérifiés sur la page 1, date 24 juin 2012.

Attestations courtes : « le tordu », « tordu d’un module gradué », « préserve le degré ».

Atteste réellement le nom substantivé tordu avec M(a)_n=M_{n+a}, permettant de conserver cette variante.

Limites : Texte étudiant sous la direction de Lie Fu, utilisé comme attestation lexicale complémentaire. Sa convention de modules concentrés en degrés positifs n'est pas importée ; ni ses autres arguments ni sa correction mathématique complète ne sont certifiés.

SHA-256 : 5F1CF8083697F7D0C7C1D4982628BDE4F7FE595F221EA301A78F143DCE91250E.

## Réparations françaises

Le remplacement de non pertinent par irrelevant suit un usage attesté. La phrase sur les suites exactes et le libellé bibliographique sont corrigés sans changer les hypothèses, la conclusion ni la référence.

### FR-ALGEBRA-B22-REPAIR-0001

Anglais L13207 ; français L13057.

Avant :
```tex
idéal non pertinent
```

Après :
```tex
idéal irrelevant
```

L'anneau est gradué en degrés non négatifs, tandis que le module peut avoir des degrés négatifs ; cette différence est conservée. Les morphismes préservent le degré. Idéal irrelevant remplace le calque non pertinent sur attestation du vocabulaire chez Schaub, avec la définition de S₊ inchangée. La phrase sur l'exactitude à chaque degré reçoit seulement les mots une suite. Tordu est conservé : cette formulation est réellement attestée chez Fougea et Gourvil avec la même convention M(a)_n=M_{n+a} ; Dat emploie aussi décalé. Toutes les formules de décalage, tenseur et Hom sont intactes.

Schaub appelle irrelevant un idéal contenant une puissance de la somme des degrés positifs ; ce passage atteste le terme, pas une nouvelle hypothèse dans Stacks. Tordu et décalé sont deux usages attestés avec la même formule. Le document étudiant de l'ENS est un témoin lexical secondaire dans la hiérarchie du canon, pas une autorité pour modifier les conventions de Stacks. La convention de Ducros autorise des anneaux Z-gradués plus généraux ; seule la terminologie est reprise.

### FR-ALGEBRA-B22-REPAIR-0002

Anglais L13227 ; français L13078.

Avant :
```tex
de modules gradués est exacte courte à chaque degré.
```

Après :
```tex
de modules gradués est une suite exacte courte à chaque degré.
```

L'anneau est gradué en degrés non négatifs, tandis que le module peut avoir des degrés négatifs ; cette différence est conservée. Les morphismes préservent le degré. Idéal irrelevant remplace le calque non pertinent sur attestation du vocabulaire chez Schaub, avec la définition de S₊ inchangée. La phrase sur l'exactitude à chaque degré reçoit seulement les mots une suite. Tordu est conservé : cette formulation est réellement attestée chez Fougea et Gourvil avec la même convention M(a)_n=M_{n+a} ; Dat emploie aussi décalé. Toutes les formules de décalage, tenseur et Hom sont intactes.

Schaub appelle irrelevant un idéal contenant une puissance de la somme des degrés positifs ; ce passage atteste le terme, pas une nouvelle hypothèse dans Stacks. Tordu et décalé sont deux usages attestés avec la même formule. Le document étudiant de l'ENS est un témoin lexical secondaire dans la hiérarchie du canon, pas une autorité pour modifier les conventions de Stacks. La convention de Ducros autorise des anneaux Z-gradués plus généraux ; seule la terminologie est reprise.

### FR-ALGEBRA-B22-REPAIR-0003

Anglais L13310 ; français L13160.

Avant :
```tex
\cite[Theorem 2.3.2]{Huneke-Swanson}
```

Après :
```tex
\cite[Théorème 2.3.2]{Huneke-Swanson}
```

Clôture intégrale de R dans S conserve le sens relatif, sans supposer S intègre ni passer à un corps des fractions. Théorème remplace Theorem dans le libellé visible de la citation ; le numéro 2.3.2 et la clé Huneke-Swanson sont identiques. La récurrence sur m−n, le degré nul de t, les automorphismes horizontaux et le quotient polynomial sont relus intégralement. La formulation suivante de C dans l'original est concise et maladroite ; son contexte fixe le sous-anneau des éléments entiers, et la traduction reste littérale à cet endroit.

L'écriture s↦t^deg(s)s du diagramme s'applique d'abord aux composantes homogènes puis s'étend par additivité. La phrase anglaise integral closure C of S[...] over R[...] signifie ici les éléments de S[...] entiers sur R[...], non que tout S[...] est entier. Le français conserve ce raccourci ; aucune nouvelle correction source n'est admise. La citation est localisée sans permutation de renvoi.

## Observations sur le texte anglais conservé

Aucune nouvelle observation source n’est enregistrée dans ce lot. Les limites d’attestation et les raccourcis de l’original sont signalés au niveau de chaque passage, sans réécriture de la source.

## Règles contextualisées

### FR-ALGEBRA-B22-RULE-GRADED

Degrés des anneaux et des modules, homogénéité et composantes vérifiés avec les conventions de Stacks.

Canon : FR-ALGEBRA-B22-CANON-DUCROS.

### FR-ALGEBRA-B22-RULE-IRRELEVANT

Vocabulaire attesté ; l'objet exact demeure S₊ défini dans Stacks.

Canon : FR-ALGEBRA-B22-CANON-SCHAUB.

### FR-ALGEBRA-B22-RULE-TWIST

La convention M(n)_d=M_{n+d} est inchangée ; les morphismes ici sont de degré zéro.

Canon : FR-ALGEBRA-B22-CANON-DAT, FR-ALGEBRA-B22-CANON-FOUGEA-GOURVIL.

### FR-ALGEBRA-B22-RULE-SUM

Construction sous-jacente, somme plutôt que produit, et objets gradués lus dans chaque définition.

Canon : FR-ALGEBRA-B22-CANON-DUCROS.

### FR-ALGEBRA-B22-RULE-FINITE

Type fini, génération en degré un et récurrence conservent leurs hypothèses et leurs bornes.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B22-RULE-INTEGRAL

Contenu gouverné par l'argument officiel, sans extrapolation d'une attestation portant sur les idéaux entiers.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B22-RULE-LOGIC

Quantificateurs, divisibilité, exactitude et libellé visible de la citation comparés en contexte.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-graded

Anglais L13199–13248 ; français L13049–13098.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13199) · FR-ALGEBRA-B22-CHOICE-0001.

L'anneau est gradué en degrés non négatifs, tandis que le module peut avoir des degrés négatifs ; cette différence est conservée. Les morphismes préservent le degré. Idéal irrelevant remplace le calque non pertinent sur attestation du vocabulaire chez Schaub, avec la définition de S₊ inchangée. La phrase sur l'exactitude à chaque degré reçoit seulement les mots une suite. Tordu est conservé : cette formulation est réellement attestée chez Fougea et Gourvil avec la même convention M(a)_n=M_{n+a} ; Dat emploie aussi décalé. Toutes les formules de décalage, tenseur et Hom sont intactes.

Point particulier à relire : Schaub appelle irrelevant un idéal contenant une puissance de la somme des degrés positifs ; ce passage atteste le terme, pas une nouvelle hypothèse dans Stacks. Tordu et décalé sont deux usages attestés avec la même formule. Le document étudiant de l'ENS est un témoin lexical secondaire dans la hiérarchie du canon, pas une autorité pour modifier les conventions de Stacks. La convention de Ducros autorise des anneaux Z-gradués plus généraux ; seule la terminologie est reprise.

Règles : FR-ALGEBRA-B22-RULE-GRADED, FR-ALGEBRA-B22-RULE-IRRELEVANT, FR-ALGEBRA-B22-RULE-TWIST, FR-ALGEBRA-B22-RULE-SUM, FR-ALGEBRA-B22-RULE-FINITE, FR-ALGEBRA-B22-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Graded rings}
\label{section-graded}

\noindent
A {\it graded ring} will be for us a ring $S$ endowed
with a direct sum decomposition $S = \bigoplus_{d \geq 0} S_d$
of the underlying abelian group such that $S_d \cdot S_e \subset S_{d + e}$.
Note that we do not allow nonzero elements in negative degrees.
The {\it irrelevant ideal} is the ideal $S_{+} = \bigoplus_{d > 0} S_d$.
A {\it graded module}
will be an $S$-module $M$ endowed with a direct sum decomposition
$M = \bigoplus_{n\in \mathbf{Z}} M_n$ of the underlying abelian group
such that $S_d \cdot M_e \subset M_{d + e}$. Note that for modules we do allow
nonzero elements in negative degrees.
We think of $S$ as a graded $S$-module by setting $S_{-k} = (0)$
for $k > 0$. An element $x$ (resp.\ $f$) of $M$ (resp.\ $S$) is called
{\it homogeneous}
if $x \in M_d$ (resp.\ $f \in S_d$) for some $d$.
A {\it map of graded $S$-modules} is a map of $S$-modules
$\varphi : M \to M'$ such that $\varphi(M_d) \subset M'_d$.
We do not allow maps to shift degrees. Let us denote
$\text{GrHom}_0(M, N)$ the $S_0$-module of homomorphisms
of graded modules from $M$ to $N$.

\medskip\noindent
At this point there are the notions of graded ideal,
graded quotient ring, graded submodule, graded quotient module,
graded tensor product, etc. We leave it to the reader to find the
relevant definitions, and lemmas. For example: A short exact sequence
of graded modules is short exact in every degree.

\medskip\noindent
Given a graded ring $S$, a graded $S$-module $M$ and $n \in \mathbf{Z}$
we denote $M(n)$ the graded $S$-module with $M(n)_d = M_{n + d}$.
This is called the {\it twist of $M$ by $n$}. In particular we get
modules $S(n)$, $n \in \mathbf{Z}$ which will play an important
role in the study of projective schemes. There are some obvious
functorial isomorphisms such as
$(M \oplus N)(n) = M(n) \oplus N(n)$,
$(M \otimes_S N)(n) = M \otimes_S N(n) = M(n) \otimes_S N$.
In addition we can define a graded $S$-module structure on
the $S_0$-module
$$
\text{GrHom}(M, N) =
\bigoplus\nolimits_{n \in \mathbf{Z}} \text{GrHom}_n(M, N),
\quad
\text{GrHom}_n(M, N) = \text{GrHom}_0(M, N(n)).
$$
We omit the definition of the multiplication.
```

Français restauré :
```tex
\section{Anneaux gradués}
\label{section-graded}

\noindent
Un {\it anneau gradué} sera pour nous un anneau $S$ muni
d'une décomposition en somme directe $S = \bigoplus_{d \geq 0} S_d$
du groupe abélien sous-jacent, telle que $S_d \cdot S_e \subset S_{d + e}$.
Remarquons que nous n'autorisons pas d'éléments non nuls en degrés négatifs.
L'{\it idéal irrelevant} est l'idéal $S_{+} = \bigoplus_{d > 0} S_d$.
Un {\it module gradué}
sera un $S$-module $M$ muni d'une décomposition en somme directe
$M = \bigoplus_{n\in \mathbf{Z}} M_n$ du groupe abélien sous-jacent
telle que $S_d \cdot M_e \subset M_{d + e}$. Remarquons que pour les modules
nous autorisons des éléments non nuls en degrés négatifs.
Nous considérons $S$ comme un $S$-module gradué en posant $S_{-k} = (0)$
pour $k > 0$. Un élément $x$ (resp.\ $f$) de $M$ (resp.\ $S$) est appelé
{\it homogène}
si $x \in M_d$ (resp.\ $f \in S_d$) pour un certain $d$.
Un {\it morphisme de $S$-modules gradués} est un morphisme de $S$-modules
$\varphi : M \to M'$ tel que $\varphi(M_d) \subset M'_d$.
Nous n'autorisons pas les morphismes à décaler les degrés. Notons
$\text{GrHom}_0(M, N)$ le $S_0$-module des homomorphismes
de modules gradués de $M$ vers $N$.

\medskip\noindent
À ce stade interviennent les notions d'idéal gradué,
d'anneau quotient gradué, de sous-module gradué, de module quotient gradué,
de produit tensoriel gradué, etc. Nous laissons au lecteur le soin de trouver
les définitions et les lemmes pertinents. Par exemple : une suite exacte courte
de modules gradués est une suite exacte courte à chaque degré.

\medskip\noindent
Étant donné un anneau gradué $S$, un $S$-module gradué $M$ et $n \in \mathbf{Z}$,
nous notons $M(n)$ le $S$-module gradué tel que $M(n)_d = M_{n + d}$.
C'est ce que l'on appelle le {\it tordu de $M$ par $n$}. En particulier, nous obtenons
les modules $S(n)$, $n \in \mathbf{Z}$, qui joueront un rôle important
dans l'étude des schémas projectifs. Il existe des isomorphismes
fonctoriels évidents tels que
$(M \oplus N)(n) = M(n) \oplus N(n)$,
$(M \otimes_S N)(n) = M \otimes_S N(n) = M(n) \otimes_S N$.
De plus, nous pouvons définir une structure de $S$-module gradué sur
le $S_0$-module
$$
\text{GrHom}(M, N) =
\bigoplus\nolimits_{n \in \mathbf{Z}} \text{GrHom}_n(M, N),
\quad
\text{GrHom}_n(M, N) = \text{GrHom}_0(M, N(n)).
$$
Nous omettons la définition de la multiplication.
```

</details>

### 02 — lemma-graded-NAK

Anglais L13249–13281 ; français L13099–13131.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13249) · FR-ALGEBRA-B22-CHOICE-0002.

Les quatre assertions de Nakayama gradué conservent leurs conditions de type fini. La preuve choisit un générateur homogène de degré minimal : l'action des degrés strictement positifs ne peut produire ce degré minimal. La récurrence et les trois applications au quotient, à l'image et au morphisme depuis la somme des S(−d_i) restent fidèles. La construction S^(d) et M^(d), qui suit la preuve, conserve le changement d'indice et non une simple suppression de composantes dans la même graduation.

Point particulier à relire : Aucune restriction n≥0 n'est ajoutée au module. De type fini assure la borne inférieure des degrés des générateurs ; le module nul est le cas initial implicite de la récurrence.

Règles : FR-ALGEBRA-B22-RULE-GRADED, FR-ALGEBRA-B22-RULE-SUM, FR-ALGEBRA-B22-RULE-FINITE, FR-ALGEBRA-B22-RULE-INTEGRAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-graded-NAK}
Let $S$ be a graded ring. Let $M$ be a graded $S$-module.
\begin{enumerate}
\item If $S_+M = M$ and $M$ is finite, then $M = 0$.
\item If $N, N' \subset M$ are graded submodules,
$M = N + S_+N'$, and $N'$ is finite, then $M = N$.
\item If $N \to M$ is a map of graded modules, $N/S_+N \to M/S_+M$
is surjective, and $M$ is finite, then $N \to M$ is surjective.
\item If $x_1, \ldots, x_n \in M$ are homogeneous and generate $M/S_+M$
and $M$ is finite, then $x_1, \ldots, x_n$ generate $M$.
\end{enumerate}
\end{lemma}

\begin{proof}
Proof of (1). Choose generators $y_1, \ldots, y_r$ of $M$ over $S$.
We may assume that $y_i$ is homogeneous of degree $d_i$. After
renumbering we may assume $d_r = \min(d_i)$. Then the condition that
$S_+M = M$ implies $y_r = 0$. Hence $M = 0$ by induction on $r$.
Part (2) follows by applying (1) to $M/N$. Part (3) follows by
applying (2) to the submodules $\Im(N \to M)$ and $M$.
Part (4) follows by applying (3) to the module map
$\bigoplus S(-d_i) \to M$, $(s_1, \ldots, s_n) \mapsto \sum s_i x_i$.
\end{proof}

\noindent
Let $S$ be a graded ring. Let $d \geq 1$ be an integer.
We set $S^{(d)} = \bigoplus_{n \geq 0} S_{nd}$. We think of
$S^{(d)}$ as a graded ring with degree $n$ summand
$(S^{(d)})_n = S_{nd}$. Given a graded $S$-module $M$ we
can similarly consider $M^{(d)} = \bigoplus_{n \in \mathbf{Z}} M_{nd}$
which is a graded $S^{(d)}$-module.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-graded-NAK}
Soit $S$ un anneau gradué. Soit $M$ un $S$-module gradué.
\begin{enumerate}
\item Si $S_+M = M$ et si $M$ est fini, alors $M = 0$.
\item Si $N, N' \subset M$ sont des sous-modules gradués,
$M = N + S_+N'$, et si $N'$ est fini, alors $M = N$.
\item Si $N \to M$ est un morphisme de modules gradués, si $N/S_+N \to M/S_+M$
est surjectif, et si $M$ est fini, alors $N \to M$ est surjectif.
\item Si $x_1, \ldots, x_n \in M$ sont homogènes, engendrent $M/S_+M$
et si $M$ est fini, alors $x_1, \ldots, x_n$ engendrent $M$.
\end{enumerate}
\end{lemma}

\begin{proof}
Preuve de (1). Choisissons des générateurs $y_1, \ldots, y_r$ de $M$ sur $S$.
Nous pouvons supposer que $y_i$ est homogène de degré $d_i$. Après
réindexation, nous pouvons supposer $d_r = \min(d_i)$. Alors la condition
$S_+M = M$ implique $y_r = 0$. Donc $M = 0$ par récurrence sur $r$.
La partie (2) s'obtient en appliquant (1) à $M/N$. La partie (3) s'obtient en
appliquant (2) aux sous-modules $\Im(N \to M)$ et $M$.
La partie (4) s'obtient en appliquant (3) au morphisme de modules
$\bigoplus S(-d_i) \to M$, $(s_1, \ldots, s_n) \mapsto \sum s_i x_i$.
\end{proof}

\noindent
Soit $S$ un anneau gradué. Soit $d \geq 1$ un entier.
Posons $S^{(d)} = \bigoplus_{n \geq 0} S_{nd}$. Nous considérons
$S^{(d)}$ comme un anneau gradué dont la composante de degré $n$ est
$(S^{(d)})_n = S_{nd}$. Étant donné un $S$-module gradué $M$, nous
pouvons de même considérer $M^{(d)} = \bigoplus_{n \in \mathbf{Z}} M_{nd}$,
qui est un $S^{(d)}$-module gradué.
```

</details>

### 03 — lemma-uple-generated-degree-1

Anglais L13282–13306 ; français L13132–13156.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13282) · FR-ALGEBRA-B22-CHOICE-0003.

S est de type fini comme algèbre sur S₀. Suffisamment divisible ne devient pas suffisamment grand. Les générateurs homogènes, leurs degrés positifs, le multiple m du ppcm, la borne N≥r et le degré rm gardent exactement leurs valeurs. Le français conserve l'argument combinatoire sans ajouter une hypothèse de génération en degré un à S lui-même.

Point particulier à relire : Le cas S=S₀ est trivial ; le choix de générateurs de degrés positifs dans l'argument concerne le cas non trivial. Pas de réécriture de la preuve ni de nouveau candidat errata pour ce raccourci.

Règles : FR-ALGEBRA-B22-RULE-GRADED, FR-ALGEBRA-B22-RULE-FINITE, FR-ALGEBRA-B22-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-uple-generated-degree-1}
Let $S$ be a graded ring, which is finitely generated over $S_0$.
Then for all sufficiently divisible $d$ the algebra
$S^{(d)}$ is generated in degree $1$ over $S_0$.
\end{lemma}

\begin{proof}
Say $S$ is generated by $f_1, \ldots, f_r \in S$ over $S_0$.
After replacing $f_i$ by their homogeneous parts, we may assume
$f_i$ is homogeneous of degree $d_i > 0$. Then any element of
$S_n$ is a linear combination with coefficients in $S_0$ of monomials
$f_1^{e_1} \ldots f_r^{e_r}$ with $\sum e_i d_i = n$.
Let $m$ be a multiple of $\text{lcm}(d_i)$. For any $N \geq r$ if
$$
\sum e_i d_i = N m
$$
then for some $i$ we have $e_i \geq m/d_i$ by an elementary argument.
Hence every monomial of degree $N m$ is a product of a monomial
of degree $m$, namely $f_i^{m/d_i}$, and a monomial of degree $(N - 1)m$.
It follows that any monomial of degree $nrm$ with $n \geq 2$
is a product of monomials of degree $rm$. Thus $S^{(rm)}$ is generated
in degree $1$ over $S_0$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-uple-generated-degree-1}
Soit $S$ un anneau gradué, qui est de type fini sur $S_0$.
Alors, pour tout $d$ suffisamment divisible, l'algèbre
$S^{(d)}$ est engendrée en degré $1$ sur $S_0$.
\end{lemma}

\begin{proof}
Disons que $S$ est engendré par $f_1, \ldots, f_r \in S$ sur $S_0$.
Après remplacement des $f_i$ par leurs composantes homogènes, nous pouvons
supposer que $f_i$ est homogène de degré $d_i > 0$. Alors tout élément de
$S_n$ est une combinaison linéaire à coefficients dans $S_0$ de monômes
$f_1^{e_1} \ldots f_r^{e_r}$ tels que $\sum e_i d_i = n$.
Soit $m$ un multiple de $\text{lcm}(d_i)$. Pour tout $N \geq r$, si
$$
\sum e_i d_i = N m
$$
alors il existe un $i$ tel que $e_i \geq m/d_i$, par un argument élémentaire.
Ainsi tout monôme de degré $N m$ est le produit d'un monôme
de degré $m$, à savoir $f_i^{m/d_i}$, et d'un monôme de degré $(N - 1)m$.
Il s'ensuit que tout monôme de degré $nrm$, pour $n \geq 2$,
est un produit de monômes de degré $rm$. Ainsi $S^{(rm)}$ est engendrée
en degré $1$ sur $S_0$.
\end{proof}
```

</details>

### 04 — lemma-integral-closure-graded

Anglais L13307–13363 ; français L13157–13208.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13307) · FR-ALGEBRA-B22-CHOICE-0004.

Clôture intégrale de R dans S conserve le sens relatif, sans supposer S intègre ni passer à un corps des fractions. Théorème remplace Theorem dans le libellé visible de la citation ; le numéro 2.3.2 et la clé Huneke-Swanson sont identiques. La récurrence sur m−n, le degré nul de t, les automorphismes horizontaux et le quotient polynomial sont relus intégralement. La formulation suivante de C dans l'original est concise et maladroite ; son contexte fixe le sous-anneau des éléments entiers, et la traduction reste littérale à cet endroit.

Point particulier à relire : L'écriture s↦t^deg(s)s du diagramme s'applique d'abord aux composantes homogènes puis s'étend par additivité. La phrase anglaise integral closure C of S[...] over R[...] signifie ici les éléments de S[...] entiers sur R[...], non que tout S[...] est entier. Le français conserve ce raccourci ; aucune nouvelle correction source n'est admise. La citation est localisée sans permutation de renvoi.

Règles : FR-ALGEBRA-B22-RULE-GRADED, FR-ALGEBRA-B22-RULE-SUM, FR-ALGEBRA-B22-RULE-FINITE, FR-ALGEBRA-B22-RULE-INTEGRAL, FR-ALGEBRA-B22-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-integral-closure-graded}
\begin{reference}
\cite[Theorem 2.3.2]{Huneke-Swanson}
\end{reference}
Let $R \to S$ be a homomorphism of graded rings.
Let $S' \subset S$ be the integral closure of $R$ in $S$.
Then
$$
S' = \bigoplus\nolimits_{d \geq 0} S' \cap S_d,
$$
i.e., $S'$ is a graded $R$-subalgebra of $S$.
\end{lemma}

\begin{proof}
We have to show the following: If
$s = s_n + s_{n + 1} + \ldots + s_m \in S'$, then each homogeneous
part $s_j \in S'$. We will prove this by induction on $m - n$ over
all homomorphisms $R \to S$ of graded rings. First note that it
is immediate that $s_0$ is integral over $R_0$ (hence over $R$) as
there is a ring map $S \to S_0$ compatible with the ring map $R \to R_0$.
Thus, after replacing $s$ by $s - s_0$, we may assume $n > 0$. Consider the
extension of graded rings $R[t, t^{-1}] \to S[t, t^{-1}]$ where
$t$ has degree $0$. There is a commutative diagram
$$
\xymatrix{
S[t, t^{-1}] \ar[rr]_{s \mapsto t^{\deg(s)}s} & & S[t, t^{-1}] \\
R[t, t^{-1}] \ar[u] \ar[rr]^{r \mapsto t^{\deg(r)}r} & &  R[t, t^{-1}] \ar[u]
}
$$
where the horizontal maps are ring automorphisms. Hence the integral
closure $C$ of $S[t, t^{-1}]$ over $R[t, t^{-1}]$ maps into itself.
Thus we see that
$$
t^m(s_n + s_{n + 1} + \ldots + s_m) -
(t^ns_n + t^{n + 1}s_{n + 1} + \ldots + t^ms_m) \in C
$$
which implies by induction hypothesis that each $(t^m - t^i)s_i \in C$
for $i = n, \ldots, m - 1$. Note that for any ring $A$ and $m > i \geq n > 0$
we have $A[t, t^{-1}]/(t^m - t^i - 1) \cong A[t]/(t^m - t^i - 1) \supset A$
because $t(t^{m - 1} - t^{i - 1}) = 1$ in $A[t]/(t^m - t^i - 1)$.
Since $t^m - t^i$ maps to $1$ we see the image of $s_i$ in the ring
$S[t]/(t^m - t^i - 1)$ is integral over $R[t]/(t^m - t^i - 1)$ for
$i = n, \ldots, m - 1$. Since $R \to R[t]/(t^m - t^i - 1)$ is finite
we see that $s_i$ is integral over $R$ by transitivity, see
Lemma \ref{lemma-integral-transitive}.
Finally, we also conclude that $s_m = s - \sum_{i = n, \ldots, m - 1} s_i$
is integral over $R$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-integral-closure-graded}
\begin{reference}
\cite[Théorème 2.3.2]{Huneke-Swanson}
\end{reference}
Soit $R \to S$ un homomorphisme d'anneaux gradués.
Soit $S' \subset S$ la clôture intégrale de $R$ dans $S$.
Alors
$$
S' = \bigoplus\nolimits_{d \geq 0} S' \cap S_d,
$$
c'est-à-dire que $S'$ est une $R$-sous-algèbre graduée de $S$.
\end{lemma}

\begin{proof}
Nous devons montrer ce qui suit : si
$s = s_n + s_{n + 1} + \ldots + s_m \in S'$, alors chaque
composante homogène $s_j \in S'$. Nous le démontrerons par récurrence
sur $m - n$ pour tous les homomorphismes $R \to S$ d'anneaux gradués.
Tout d'abord, il est immédiat que $s_0$ est entier sur $R_0$ (et donc sur $R$),
car il existe un morphisme d'anneaux $S \to S_0$ compatible avec le morphisme
d'anneaux $R \to R_0$. Ainsi, après avoir remplacé $s$ par $s - s_0$, nous
pouvons supposer $n > 0$. Considérons l'extension d'anneaux gradués
$R[t, t^{-1}] \to S[t, t^{-1}]$ où $t$ est de degré $0$. Il existe un diagramme
commutatif
$$
\xymatrix{
S[t, t^{-1}] \ar[rr]_{s \mapsto t^{\deg(s)}s} & & S[t, t^{-1}] \\
R[t, t^{-1}] \ar[u] \ar[rr]^{r \mapsto t^{\deg(r)}r} & &  R[t, t^{-1}] \ar[u]
}
$$
où les morphismes horizontaux sont des automorphismes d'anneaux. Ainsi la clôture
intégrale $C$ de $S[t, t^{-1}]$ sur $R[t, t^{-1}]$ se transforme en elle-même.
Nous voyons donc que
$$
t^m(s_n + s_{n + 1} + \ldots + s_m) -
(t^ns_n + t^{n + 1}s_{n + 1} + \ldots + t^ms_m) \in C
$$
ce qui implique, par l'hypothèse de récurrence, que chaque $(t^m - t^i)s_i \in C$
pour $i = n, \ldots, m - 1$. Remarquons que pour tout anneau $A$ et
$m > i \geq n > 0$, nous avons
$A[t, t^{-1}]/(t^m - t^i - 1) \cong A[t]/(t^m - t^i - 1) \supset A$
car $t(t^{m - 1} - t^{i - 1}) = 1$ dans $A[t]/(t^m - t^i - 1)$.
Comme $t^m - t^i$ s'envoie sur $1$, nous voyons que l'image de $s_i$ dans
l'anneau $S[t]/(t^m - t^i - 1)$ est entière sur
$R[t]/(t^m - t^i - 1)$ pour $i = n, \ldots, m - 1$. Comme
$R \to R[t]/(t^m - t^i - 1)$ est fini, nous voyons que $s_i$ est entier
sur $R$ par transitivité, voir le Lemme \ref{lemma-integral-transitive}.
Enfin, nous concluons également que $s_m = s - \sum_{i = n, \ldots, m - 1} s_i$
est entier sur $R$.
\end{proof}
```

</details>

## Contrôles et suite

Les 165 régions mathématiques sont strictement identiques sans exception nouvelle. Le préfixe de 9 464 régions passe avec vingt-sept exceptions linguistiques antérieures. Les trois nouvelles opérations ne touchent aucune région mathématique.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items restent identiques. Le seul libellé bibliographique traduit garde sa clé Huneke-Swanson et le numéro 2.3.2 ; aucun titre facultatif n’est modifié. Les opérations inverses retrouvent le lot précédent puis tous les octets du témoin public préservé. Préfixe déjà relu et suffixe encore non relu sont inchangés.

Les 482 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Proj d’un anneau gradué, anglais L13364 / français L13209. Aucun PDF nouveau ni publication ; restauration globale en cours.

