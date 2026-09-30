# Algèbres d’éclatement

## Résultat et portée

Comparaison complète : anglais L17136–17401 /français L16902–17167, 266 lignes chacun, treize paires et 140 occurrences contextualisées. Couverture continue : 70 sections, 634 paires et 6278 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Une précision française explicite que le noyau est annulé par une puissance de f, comme dans la source et la preuve, et non nécessairement par f seul. L’abréviation ancienne peut être légitime ; il s’agit d’éviter une lecture restrictive. Aucun symbole ni résultat changé.

Quatre observations anglaises sont conservées hors traduction : by manquant, variable x_n au lieu de t_n, application P→A au lieu de P→R, et cas R corps non traité par la condition I⊂m. Pas de correction mathématique cachée dans la traduction.

Lecture produite par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. Le canon est consulté rétrospectivement, non présenté comme consulté lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch36.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH35_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH36_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH36_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH36_OCCURRENCES.json) · [Opérations](ALGEBRA_PROSE_BATCH36_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH36_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH36_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH36_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH36_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH36_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Jean-François Dat — Introduction à la théorie des Schémas, M2, 2025–2026

[Source consultée](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/Schemas/Schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/dat-schemas.pdf)

Couverture PDF1 et pages PDF/imprimées52–53 et67–70 entièrement lues. Sections2.6.5,2.9.1–2.9.4 ; PDF68 rendu et inspecté visuellement.

Attestations courtes : « algèbre de Rees », « éclatement », « anneau intègre », « anneau de valuation », « ordre de dominance ».

Atteste directement Rees comme somme graduée des puissances et distingue les mêmes éléments selon le degré ; expose les cartes affines, la présentation et les mots réduit/intègre. La domination est définie par contraction de l'idéal maximal.

Limites : Le changement de base de Rees p68 y est plat ; aucune platitude n'est importée dans le lemme général de Stacks. La convention régulière p69 n'exige pas quotient non nul. Le max de l'inégalité valuative p52 n'est pas importé. Le composé exact algèbre d'éclatement affine et la formulation de torsion ne sont pas prétendus attestés. Consultation rétrospective, pas relecture humaine.

SHA-256 : 9298B062AC2BDF64161A107980A30F98E1F2DF6DEB4DA98E1FEB21BA494D26A1.

### Christian Peskine — Introduction algébrique à la géométrie projective

[Source consultée](https://perso.univ-rennes1.fr/matthieu.romagny/M2_0708/bouquin.pdf) · [Fichier conservé](canon-consulted/fr-algebra/peskine-geometrie-projective-2007.pdf)

Pages PDF106–108 /imprimées105–107 entièrement lues : section13.1, exemple précédant la définition13.3, définition13.3, et définition13.10.

Attestations courtes : « anneau de Rees », « anneau gradué associé ».

Le même objet ⊕I^n est appelé anneau de Rees ; conserver algèbre de Rees respecte la structure sur la base et l'attestation directe chez Dat.

Limites : Les hypothèses noethériennes et la terminologie projetant voisines ne sont pas introduites dans la définition générale. Ces pages ne prouvent pas le lemme valuatif final. Consultation rétrospective limitée à ces pages.

SHA-256 : C84D597457282B22B993F523791F4A3E391A74554FF76F7F49878640789435BA.

## Modifications et motifs

Une précision de portée, réversible et sans changement de formule. Les autres formulations fidèles sont conservées après lecture complète et justification. Les anomalies anglaises restent visibles dans le français diplomatique et motivées séparément.

### FR-ALGEBRA-B36-REPAIR-0001

Anglais L17290 ; français L17056.

Avant :
```tex
est l'ensemble des éléments de $f$-torsion de $R'$.
```

Après :
```tex
est l'ensemble des éléments annulés par une puissance de $f$ dans $R'$.
```

Une clarification remplace éléments de f-torsion par éléments annulés par une puissance de f dans l'énoncé. La source dit f-power torsion et la preuve française emploie déjà pour les puissances de f ; la nouvelle formulation évite de suggérer le seul noyau de multiplication par f. Par exemple, dans k[t]/(t²), la classe1 est tuée par t² mais pas par t. f-torsion peut aussi servir d'abréviation correcte selon les conventions : il s'agit d'une précision de portée, non de prétendre qu'une nouvelle proposition mathématique est corrigée. L'application, la surjectivité et les deux sens de l'identification du noyau sont comparés.

L'ancienne abréviation f-torsion est parfois légitime. La précision choisie empêche néanmoins une lecture restrictive ; elle ne change aucun symbole ni la propriété source.

## Observations séparées sur la source

Les quatre observations distinguent syntaxe, variable polynomiale, anneau de changement de base et cas frontière du lemme valuatif. Aucun registre n’est admis, aucune déduplication globale ni première découverte revendiquée.

### definition-blow-up

[Anglais officiel L17155](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17155) · FR-ALGEBRA-B36-SOURCE-NOTE-0001.

```tex
Denote $a^{(1)}$ the element $a$
```

Denote by X the element exige by. L'ajout est grammatical ; notons X l'élément traduit déjà cette opération correctement. Aucun effet sur le degré de a ou la construction.

Confiance forte sur la syntaxe ; observation séparée, pas d'admission ni de première découverte.

### example-rees-algebra-polynomial

[Anglais officiel L17221](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17221) · FR-ALGEBRA-B36-SOURCE-NOTE-0002.

```tex
$t^E = t_1^{e_1} \ldots x_n^{e_n}$
```

L'anneau P ne contient que t1,…,tn, et E indexe leurs exposants. x_n est indéfini ; t_n rétablit le monôme annoncé et les relations utilisant les mêmes t_i. La présentation reste valide, mais cette formule doit lire t_n. Le français conserve x_n diplomatiquement.

Confiance forte par les variables définies et les relations adjacentes ; aucune mutation source.

### lemma-affine-blowup-quotient-description

[Anglais officiel L17267](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17267) · FR-ALGEBRA-B36-SOURCE-NOTE-0003.

```tex
Apply Lemma \ref{lemma-blowup-base-change} to the map $P \to A$ to conclude.
```

Le seul homomorphisme introduit est P→R envoyant t_i sur a_i. A n'est pas défini dans le lemme ni dans cette preuve ; appliquer le changement de base à P→R donne précisément la présentation sur R. Remplacer A par R est la correction minimale proposée, non appliquée à la traduction.

Confiance forte sur le type du but ; aucune admission, déduplication globale ou première découverte.

### lemma-valuation-ring-colimit-affine-blowups

[Anglais officiel L17362](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17362) · FR-ALGEBRA-B36-SOURCE-NOTE-0004.

```tex
a \in I \subset \mathfrak m
```

Contre-exemple de frontière : prendre R=K=A=k un corps, avec m=0. C'est bien un anneau local intègre dominé par un anneau de valuation. La condition (1) impose I=0 et a=0. Bl_0(k) est k en degré0 ; localiser au générateur homogène nul donne l'anneau nul, dont la fibre en m est nulle, contrairement à (3). La famille admissible est donc vide et ne peut fournir ces sous-anneaux dans k ni la réunion annoncée. Pour R non corps, choisir d∈m non nul et multiplier par d le dénominateur commun et tous les numérateurs force I⊂m ; la domination assure la fibre non nulle. On peut exclure R corps ou traiter ce cas en autorisant la carte unité. Ce sont des propositions source, pas des changements français. La formule et la condition restent littérales.

Confiance forte sur le cas corps, calcul explicite ; pas de nouvelle admission ou première découverte.

## Règles contextualisées

### FR-ALGEBRA-B36-RULE-BLOWUP

Rees est directement attesté ; éclatement est celui de l'idéal. Le composé affine est motivé par la carte standard, avec sa lacune d'attestation exacte déclarée.

Canon : FR-ALGEBRA-B36-CANON-DAT, FR-ALGEBRA-B36-CANON-PESKINE.

### FR-ALGEBRA-B36-RULE-GRADED

Graduation, somme directe, variables et présentation ont leurs indices source. Les changements de nom d'objet ou de variable de la source restent signalés séparément.

Canon : FR-ALGEBRA-B36-CANON-DAT, FR-ALGEBRA-B36-CANON-PESKINE.

### FR-ALGEBRA-B36-RULE-TORSION

La lecture complète des représentants et des preuves distingue une puissance quelconque de la puissance1. La précision française est une explicitation directe de f-power torsion, pas une prétendue attestation externe.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B36-RULE-RING

Les conditions sur l'anneau et l'idéal sont vérifiées dans chaque passage, sans ajouter finitude, noethérianité ou réduction.

Canon : FR-ALGEBRA-B36-CANON-DAT, FR-ALGEBRA-B36-CANON-PESKINE.

### FR-ALGEBRA-B36-RULE-MAP

Source et but, surjection et isomorphisme, quotient et densité conservent leur portée. La lecture intégrale de la preuve complète l'appui lexical.

Canon : FR-ALGEBRA-B36-CANON-DAT.

### FR-ALGEBRA-B36-RULE-VALUATION

Domination locale et filtrance sont lues avec les trois conditions. Le cas corps est une anomalie source, pas un glissement de registre français.

Canon : FR-ALGEBRA-B36-CANON-DAT.

### FR-ALGEBRA-B36-RULE-LOGIC

Chaque quantificateur et sens d'implication est contextualisé dans les treize passages complets ; pas de généralisation silencieuse.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-blow-up

Anglais L17136–17141 ; français L16902–16907.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17136) · FR-ALGEBRA-B36-CHOICE-0001.

Éclatement est directement attesté chez Dat, section2.9 ; algèbre de Rees en2.9.1 et chez Peskine13.3. Observations élémentaires conserve la portée, sans transformer la section d'algèbre commutative en construction géométrique supplémentaire.

Règles : FR-ALGEBRA-B36-RULE-BLOWUP.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Blow up algebras}
\label{section-blow-up}

\noindent
In this section we make some elementary observations about blowing up.
```

Français restauré :
```tex
\section{Algèbres d'éclatement}
\label{section-blow-up}

\noindent
Dans cette section, nous présentons quelques observations élémentaires sur l'éclatement.
```

</details>

### 02 — definition-blow-up

Anglais L17142–17167 ; français L16908–16933.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17142) · FR-ALGEBRA-B36-CHOICE-0002.

Définition entière, deux clauses et explication par représentants comparées. Algèbre de Rees et algèbre graduée sont attestées ; le degré1 ne se confond pas avec le même élément en degré0, distinction explicitement soulignée chez Dat. Le composé algèbre d'éclatement affine désigne ici l'anneau de la carte standard, non l'éclatement global comme schéma. L'équivalence exacte des fractions inclut la puissance supplémentaire a^k même quand a est diviseur de zéro.

Point particulier à relire : Pas d'attestation mot pour mot du composé algèbre d'éclatement affine dans les pages consultées. Justification explicite par l'algèbre de la carte standard ; pas de citation fabriquée. Notons est idiomatique malgré le by manquant en anglais.

Règles : FR-ALGEBRA-B36-RULE-BLOWUP, FR-ALGEBRA-B36-RULE-GRADED, FR-ALGEBRA-B36-RULE-RING, FR-ALGEBRA-B36-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-blow-up}
Let $R$ be a ring.
Let $I \subset R$ be an ideal.
\begin{enumerate}
\item The {\it blowup algebra}, or the {\it Rees algebra}, associated to
the pair $(R, I)$ is the graded $R$-algebra
$$
\text{Bl}_I(R) =
\bigoplus\nolimits_{n \geq 0} I^n =
R \oplus I \oplus I^2 \oplus \ldots
$$
where the summand $I^n$ is placed in degree $n$.
\item Let $a \in I$ be an element. Denote $a^{(1)}$ the element $a$
seen as an element of degree $1$ in the Rees algebra. Then the
{\it affine blowup algebra} $R[\frac{I}{a}]$ is the algebra
$(\text{Bl}_I(R))_{(a^{(1)})}$ constructed in Section \ref{section-proj}.
\end{enumerate}
\end{definition}

\noindent
In other words, an element of $R[\frac{I}{a}]$ is represented by
an expression of the form $x/a^n$ with $x \in I^n$. Two representatives
$x/a^n$ and $y/a^m$ define the same element if and only if
$a^k(a^mx - a^ny) = 0$ for some $k \geq 0$.
```

Français restauré :
```tex
\begin{definition}
\label{definition-blow-up}
Soit $R$ un anneau.
Soit $I \subset R$ un idéal.
\begin{enumerate}
\item L'{\it algèbre d'éclatement}, ou {\it algèbre de Rees}, associée à
la paire $(R, I)$ est la $R$-algèbre graduée
$$
\text{Bl}_I(R) =
\bigoplus\nolimits_{n \geq 0} I^n =
R \oplus I \oplus I^2 \oplus \ldots
$$
où le facteur direct $I^n$ est placé en degré $n$.
\item Soit $a \in I$ un élément. Notons $a^{(1)}$ l'élément $a$
considéré comme un élément de degré $1$ de l'algèbre de Rees. L'
{\it algèbre d'éclatement affine} $R[\frac{I}{a}]$ est alors l'algèbre
$(\text{Bl}_I(R))_{(a^{(1)})}$ construite dans la section \ref{section-proj}.
\end{enumerate}
\end{definition}

\noindent
Autrement dit, un élément de $R[\frac{I}{a}]$ est représenté par
une expression de la forme $x/a^n$ avec $x \in I^n$. Deux représentants
$x/a^n$ et $y/a^m$ définissent le même élément si et seulement si
$a^k(a^mx - a^ny) = 0$ pour un certain $k \geq 0$.
```

</details>

### 03 — lemma-affine-blowup

Anglais L17168–17182 ; français L16934–16948.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17168) · FR-ALGEBRA-B36-CHOICE-0003.

Les trois conclusions restent distinctes : non-diviseur de zéro, idéal principal et égalité après localisation. La preuve entière renvoie à la description, sans nouvelle preuve ajoutée. Le cas a=0 et l'anneau nul ne sont pas exclus silencieusement.

Règles : FR-ALGEBRA-B36-RULE-BLOWUP, FR-ALGEBRA-B36-RULE-TORSION, FR-ALGEBRA-B36-RULE-RING.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-affine-blowup}
Let $R$ be a ring, $I \subset R$ an ideal, and $a \in I$.
Let $R' = R[\frac{I}{a}]$ be the affine blowup algebra. Then
\begin{enumerate}
\item the image of $a$ in $R'$ is a nonzerodivisor,
\item $IR' = aR'$, and
\item $(R')_a = R_a$.
\end{enumerate}
\end{lemma}

\begin{proof}
Immediate from the description of $R[\frac{I}{a}]$ above.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-affine-blowup}
Soit $R$ un anneau, $I \subset R$ un idéal et $a \in I$.
Soit $R' = R[\frac{I}{a}]$ l'algèbre d'éclatement affine. Alors
\begin{enumerate}
\item l'image de $a$ dans $R'$ est un non-diviseur de zéro,
\item $IR' = aR'$, et
\item $(R')_a = R_a$.
\end{enumerate}
\end{lemma}

\begin{proof}
Cela résulte immédiatement de la description de $R[\frac{I}{a}]$ ci-dessus.
\end{proof}
```

</details>

### 04 — lemma-blowup-base-change

Anglais L17183–17208 ; français L16949–16974.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17183) · FR-ALGEBRA-B36-CHOICE-0004.

L'homomorphisme R→S est arbitraire, non supposé plat. Le quotient par la torsion pour les puissances de b est conservé ; la formation de Rees commute au changement de base plat chez Dat, mais cette restriction n'est pas importée. Toute la construction de l'inverse, la représentation par somme et le noyau tensoriel sont comparés. La torsion en a dans le tenseur est la même action que celle de son image b : pas une nouvelle erreur de variable.

Point particulier à relire : Ne pas assimiler b-torsion au seul annulateur de b, ni remplacer le quotient par une égalité générale de changement de base. a agit via b dans le S-module : alias correct, non faute anglaise.

Règles : FR-ALGEBRA-B36-RULE-TORSION, FR-ALGEBRA-B36-RULE-RING, FR-ALGEBRA-B36-RULE-MAP.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-blowup-base-change}
Let $R \to S$ be a ring map. Let $I \subset R$ be an ideal
and $a \in I$. Set $J = IS$ and let $b \in J$ be the image of $a$.
Then $S[\frac{J}{b}]$ is the quotient of $S \otimes_R R[\frac{I}{a}]$
by the ideal of elements annihilated by some power of $b$.
\end{lemma}

\begin{proof}
Let $S'$ be the quotient of $S \otimes_R R[\frac{I}{a}]$ by its
$b$-power torsion elements. The ring map
$$
S \otimes_R R[\textstyle{\frac{I}{a}}]
\longrightarrow
S[\textstyle{\frac{J}{b}}]
$$
is surjective and annihilates $a$-power torsion as $b$ is a nonzerodivisor
in $S[\frac{J}{b}]$. Hence we obtain a surjective map $S' \to S[\frac{J}{b}]$.
To see that the kernel is trivial, we construct an inverse map. Namely, let
$z = y/b^n$ be an element of $S[\frac{J}{b}]$, i.e., $y \in J^n$.
Write $y = \sum x_is_i$ with $x_i \in I^n$ and $s_i \in S$.
We map $z$ to the class of $\sum s_i \otimes x_i/a^n$ in
$S'$. This is well defined because an element of the kernel of the map
$S \otimes_R I^n \to J^n$ is annihilated by $a^n$, hence maps to zero in $S'$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-blowup-base-change}
Soit $R \to S$ un homomorphisme d'anneaux. Soit $I \subset R$ un idéal
et soit $a \in I$. Posons $J = IS$ et soit $b \in J$ l'image de $a$.
Alors $S[\frac{J}{b}]$ est le quotient de $S \otimes_R R[\frac{I}{a}]$
par l'idéal des éléments annulés par une puissance de $b$.
\end{lemma}

\begin{proof}
Soit $S'$ le quotient de $S \otimes_R R[\frac{I}{a}]$ par ses
éléments de torsion pour les puissances de $b$. L'homomorphisme d'anneaux
$$
S \otimes_R R[\textstyle{\frac{I}{a}}]
\longrightarrow
S[\textstyle{\frac{J}{b}}]
$$
est surjectif et annule la torsion pour les puissances de $a$, puisque $b$ est un non-diviseur de zéro
dans $S[\frac{J}{b}]$. On obtient donc une application surjective $S' \to S[\frac{J}{b}]$.
Pour voir que son noyau est trivial, construisons une application inverse. Soit
$z = y/b^n$ un élément de $S[\frac{J}{b}]$, c'est-à-dire $y \in J^n$.
Écrivons $y = \sum x_is_i$ avec $x_i \in I^n$ et $s_i \in S$.
On envoie $z$ sur la classe de $\sum s_i \otimes x_i/a^n$ dans
$S'$. Cette définition est bonne, car un élément du noyau de l'application
$S \otimes_R I^n \to J^n$ est annulé par $a^n$, donc a une image nulle dans $S'$.
\end{proof}
```

</details>

### 05 — example-rees-algebra-polynomial

Anglais L17209–17227 ; français L16975–16993.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17209) · FR-ALGEBRA-B36-CHOICE-0005.

L'isomorphisme, chaque générateur, les relations, indices et degrés sont comparés. Algèbre de polynômes, monômes et delta de Kronecker restent leur sens. Dat2.9.3 offre une présentation analogue sous hypothèse de suite régulière, sans remplacer cet exemple sur base quelconque par son exemple sur un corps. La variable x_n inattendue dans l'anglais reste dans la formule française ; observation séparée.

Point particulier à relire : x_n est une variable inexistante dans P ; elle est conservée diplomatiquement, avec justification de t_n dans l'observation séparée.

Règles : FR-ALGEBRA-B36-RULE-GRADED, FR-ALGEBRA-B36-RULE-RING, FR-ALGEBRA-B36-RULE-MAP, FR-ALGEBRA-B36-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-rees-algebra-polynomial}
Let $R$ be a ring. Let $P = R[t_1, \ldots, t_n]$ be the polynomial algebra.
Let $I = (t_1, \ldots, t_n) \subset P$. With notation as in
Definition \ref{definition-blow-up} there is an isomorphism
$$
P[T_1, \ldots, T_n]/(t_iT_j - t_jT_i) \longrightarrow \text{Bl}_I(P)
$$
sending $T_i$ to $t_i^{(1)}$. We leave it to the reader to show that
this map is well defined. Since $I$ is generated by $t_1, \ldots, t_n$
we see that our map is surjective. To see that our map is injective
one has to show: for each $e \geq 1$ the $P$-module $I^e$ is generated
by the monomials $t^E = t_1^{e_1} \ldots x_n^{e_n}$ for multiindices
$E = (e_1, \ldots, e_n)$ of degree $|E| = e$ subject only to the
relations $t_i t^E = t_j t^{E'}$ when $|E| = |E'| = e$ and
$e_a + \delta_{a i} = e'_a + \delta_{a j},\ a = 1, \ldots, n$
(Kronecker delta). We omit the details.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-rees-algebra-polynomial}
Soit $R$ un anneau. Soit $P = R[t_1, \ldots, t_n]$ l'algèbre de polynômes.
Soit $I = (t_1, \ldots, t_n) \subset P$. Avec les notations de la
Définition \ref{definition-blow-up}, il existe un isomorphisme
$$
P[T_1, \ldots, T_n]/(t_iT_j - t_jT_i) \longrightarrow \text{Bl}_I(P)
$$
qui envoie $T_i$ sur $t_i^{(1)}$. Nous laissons au lecteur le soin de montrer que
cette application est bien définie. Puisque $I$ est engendré par $t_1, \ldots, t_n$,
on voit que notre application est surjective. Pour montrer qu'elle est injective,
il faut établir ceci : pour tout $e \geq 1$, le $P$-module $I^e$ est engendré
par les monômes $t^E = t_1^{e_1} \ldots x_n^{e_n}$, pour les multi-indices
$E = (e_1, \ldots, e_n)$ de degré $|E| = e$, soumis uniquement aux
relations $t_i t^E = t_j t^{E'}$ lorsque $|E| = |E'| = e$ et
$e_a + \delta_{a i} = e'_a + \delta_{a j},\ a = 1, \ldots, n$
(delta de Kronecker). Nous omettons les détails.
\end{example}
```

</details>

### 06 — example-affine-blowup-algebra-polynomial

Anglais L17228–17248 ; français L16994–17014.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17228) · FR-ALGEBRA-B36-CHOICE-0006.

La source et le but de l'isomorphisme, le quotient, les fractions, l'absence de t1-torsion et l'inversion de t1 sont comparés. Les cartes affines de Dat2.9.3–2.9.4 appuient le registre, pas une hypothèse de corps ajoutée. Les deux méthodes proposées et l'omission des détails sont conservées.

Règles : FR-ALGEBRA-B36-RULE-BLOWUP, FR-ALGEBRA-B36-RULE-GRADED, FR-ALGEBRA-B36-RULE-TORSION, FR-ALGEBRA-B36-RULE-RING, FR-ALGEBRA-B36-RULE-MAP.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-affine-blowup-algebra-polynomial}
Let $R$ be a ring. Let $P = R[t_1, \ldots, t_n]$ be the polynomial algebra.
Let $I = (t_1, \ldots, t_n) \subset P$. Let $a = t_1$. With notation as in
Definition \ref{definition-blow-up} there is an isomorphism
$$
P[x_2, \ldots, x_n]/(t_1x_2 - t_2, \ldots, t_1x_n - t_n)
\longrightarrow
\textstyle{P[\frac{I}{a}] = P[\frac{I}{t_1}]}
$$
sending $x_i$ to $t_i/t_1$. We leave it to the reader to show that
this map is well defined. Since $I$ is generated by $t_1, \ldots, t_n$
we see that our map is surjective. To see that our map is injective,
the reader can argue that the source and target of our map are
$t_1$-torsion free and that the map is an isomorphism after inverting
$t_1$, see Lemma \ref{lemma-affine-blowup}. Alternatively, the reader
can use the description of the Rees algebra in
Example \ref{example-rees-algebra-polynomial}.
We omit the details.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-affine-blowup-algebra-polynomial}
Soit $R$ un anneau. Soit $P = R[t_1, \ldots, t_n]$ l'algèbre de polynômes.
Soit $I = (t_1, \ldots, t_n) \subset P$. Soit $a = t_1$. Avec les notations de la
Définition \ref{definition-blow-up}, il existe un isomorphisme
$$
P[x_2, \ldots, x_n]/(t_1x_2 - t_2, \ldots, t_1x_n - t_n)
\longrightarrow
\textstyle{P[\frac{I}{a}] = P[\frac{I}{t_1}]}
$$
qui envoie $x_i$ sur $t_i/t_1$. Nous laissons au lecteur le soin de montrer que
cette application est bien définie. Puisque $I$ est engendré par $t_1, \ldots, t_n$,
on voit que notre application est surjective. Pour montrer qu'elle est injective,
le lecteur peut observer que la source et le but de notre application sont
sans $t_1$-torsion et que l'application est un isomorphisme après inversion de
$t_1$ ; voir le Lemme \ref{lemma-affine-blowup}. Le lecteur peut aussi
utiliser la description de l'algèbre de Rees donnée dans
l'Exemple \ref{example-rees-algebra-polynomial}.
Nous omettons les détails.
\end{example}
```

</details>

### 07 — lemma-affine-blowup-quotient-description

Anglais L17249–17269 ; français L17015–17035.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17249) · FR-ALGEBRA-B36-CHOICE-0007.

La surjection n'est pas remplacée par un isomorphisme. Son noyau est la torsion pour une puissance de a, non nécessairement le noyau de la multiplication par a seule. Le changement de base et la présentation polynomiale sont comparés intégralement ; le P→A anglais indéfini reste littéral dans la formule française et signalé hors traduction.

Point particulier à relire : A n'est pas défini dans cette preuve ; seule l'application P→R est introduite. La formule anglaise est conservée, pas une erreur introduite par le français.

Règles : FR-ALGEBRA-B36-RULE-TORSION, FR-ALGEBRA-B36-RULE-RING, FR-ALGEBRA-B36-RULE-MAP.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-affine-blowup-quotient-description}
Let $R$ be a ring. Let $I = (a_1, \ldots, a_n)$ be an ideal of $R$.
Let $a = a_1$. Then there is a surjection
$$
R[x_2, \ldots, x_n]/(a x_2 - a_2, \ldots, a x_n - a_n)
\longrightarrow
\textstyle{R[\frac{I}{a}]}
$$
whose kernel is the $a$-power torsion in the source.
\end{lemma}

\begin{proof}
Consider the ring map $P = \mathbf{Z}[t_1, \ldots, t_n] \to R$
sending $t_i$ to $a_i$. Set $J = (t_1, \ldots, t_n)$.
By Example \ref{example-affine-blowup-algebra-polynomial} we have
$P[\frac{J}{t_1}] =
P[x_2, \ldots, x_n]/(t_1 x_2 - t_2, \ldots, t_1 x_n - t_n)$.
Apply Lemma \ref{lemma-blowup-base-change} to the map $P \to A$ to conclude.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-affine-blowup-quotient-description}
Soit $R$ un anneau. Soit $I = (a_1, \ldots, a_n)$ un idéal de $R$.
Soit $a = a_1$. Il existe alors une surjection
$$
R[x_2, \ldots, x_n]/(a x_2 - a_2, \ldots, a x_n - a_n)
\longrightarrow
\textstyle{R[\frac{I}{a}]}
$$
dont le noyau est la torsion pour les puissances de $a$ dans la source.
\end{lemma}

\begin{proof}
Considérons l'homomorphisme d'anneaux $P = \mathbf{Z}[t_1, \ldots, t_n] \to R$
qui envoie $t_i$ sur $a_i$. Posons $J = (t_1, \ldots, t_n)$.
D'après l'Exemple \ref{example-affine-blowup-algebra-polynomial}, on a
$P[\frac{J}{t_1}] =
P[x_2, \ldots, x_n]/(t_1 x_2 - t_2, \ldots, t_1 x_n - t_n)$.
On conclut en appliquant le Lemme \ref{lemma-blowup-base-change} à l'application $P \to A$.
\end{proof}
```

</details>

### 08 — lemma-blowup-in-principal

Anglais L17270–17284 ; français L17036–17050.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17270) · FR-ALGEBRA-B36-CHOICE-0008.

L'égalité des fermés V(f)=V(I), non l'égalité des idéaux, et les deux relations de puissances sont préservées. Non-diviseur de zéro, localisation et toutes les égalités ont leur portée originale. Aucun entier uniforme ni égalité f=a n'est ajouté.

Règles : FR-ALGEBRA-B36-RULE-TORSION, FR-ALGEBRA-B36-RULE-RING, FR-ALGEBRA-B36-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-blowup-in-principal}
Let $R$ be a ring, $I \subset R$ an ideal, and $a \in I$.
Set $R' = R[\frac{I}{a}]$. If $f \in R$ is such that $V(f) = V(I)$,
then $f$ maps to a nonzerodivisor in $R'$ and $R'_f = R'_a = R_a$.
\end{lemma}

\begin{proof}
We will use the results of Lemma \ref{lemma-affine-blowup}
without further mention.
The assumption $V(f) = V(I)$ implies $V(fR') = V(IR') = V(aR')$.
Hence $a^n = fb$ and $f^m = ac$ for some $b, c \in R'$.
The lemma follows.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-blowup-in-principal}
Soit $R$ un anneau, $I \subset R$ un idéal et $a \in I$.
Posons $R' = R[\frac{I}{a}]$. Si $f \in R$ vérifie $V(f) = V(I)$,
alors l'image de $f$ dans $R'$ est un non-diviseur de zéro et $R'_f = R'_a = R_a$.
\end{lemma}

\begin{proof}
Nous utiliserons les résultats du Lemme \ref{lemma-affine-blowup}
sans les mentionner davantage.
L'hypothèse $V(f) = V(I)$ implique $V(fR') = V(IR') = V(aR')$.
Ainsi $a^n = fb$ et $f^m = ac$ pour certains $b, c \in R'$.
Le lemme en résulte.
\end{proof}
```

</details>

### 09 — lemma-blowup-add-principal

Anglais L17285–17304 ; français L17051–17070.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17285) · FR-ALGEBRA-B36-CHOICE-0009.

Une clarification remplace éléments de f-torsion par éléments annulés par une puissance de f dans l'énoncé. La source dit f-power torsion et la preuve française emploie déjà pour les puissances de f ; la nouvelle formulation évite de suggérer le seul noyau de multiplication par f. Par exemple, dans k[t]/(t²), la classe1 est tuée par t² mais pas par t. f-torsion peut aussi servir d'abréviation correcte selon les conventions : il s'agit d'une précision de portée, non de prétendre qu'une nouvelle proposition mathématique est corrigée. L'application, la surjectivité et les deux sens de l'identification du noyau sont comparés.

Point particulier à relire : L'ancienne abréviation f-torsion est parfois légitime. La précision choisie empêche néanmoins une lecture restrictive ; elle ne change aucun symbole ni la propriété source.

Règles : FR-ALGEBRA-B36-RULE-TORSION, FR-ALGEBRA-B36-RULE-RING, FR-ALGEBRA-B36-RULE-MAP, FR-ALGEBRA-B36-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-blowup-add-principal}
Let $R$ be a ring, $I \subset R$ an ideal, $a \in I$, and $f \in R$.
Set $R' = R[\frac{I}{a}]$ and $R'' = R[\frac{fI}{fa}]$. Then
there is a surjective $R$-algebra map $R' \to R''$ whose kernel
is the set of $f$-power torsion elements of $R'$.
\end{lemma}

\begin{proof}
The map is given by sending $x/a^n$ for $x \in I^n$ to $f^nx/(fa)^n$.
It is straightforward to check this map is well defined and surjective.
Since $af$ is a nonzero divisor in $R''$
(Lemma \ref{lemma-affine-blowup}) we see that the set of $f$-power
torsion elements are mapped to zero. Conversely, if $x \in R'$
and $f^n x \not = 0$ for all $n > 0$, then $(af)^n x \not = 0$
for all $n$ as $a$ is a nonzero divisor in $R'$. It follows
that the image of $x$ in $R''$ is not zero by the description of
$R''$ following Definition \ref{definition-blow-up}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-blowup-add-principal}
Soit $R$ un anneau, $I \subset R$ un idéal, $a \in I$ et $f \in R$.
Posons $R' = R[\frac{I}{a}]$ et $R'' = R[\frac{fI}{fa}]$. Alors
il existe un homomorphisme surjectif de $R$-algèbres $R' \to R''$ dont le noyau
est l'ensemble des éléments annulés par une puissance de $f$ dans $R'$.
\end{lemma}

\begin{proof}
L'application envoie $x/a^n$, pour $x \in I^n$, sur $f^nx/(fa)^n$.
On vérifie immédiatement que cette application est bien définie et surjective.
Puisque $af$ est un non-diviseur de zéro dans $R''$
(Lemme \ref{lemma-affine-blowup}), l'ensemble des éléments de torsion
pour les puissances de $f$ est envoyé sur zéro. Réciproquement, si $x \in R'$
et si $f^n x \not = 0$ pour tout $n > 0$, alors $(af)^n x \not = 0$
pour tout $n$, puisque $a$ est un non-diviseur de zéro dans $R'$. Il s'ensuit
que l'image de $x$ dans $R''$ n'est pas nulle, d'après la description de
$R''$ donnée après la Définition \ref{definition-blow-up}.
\end{proof}
```

</details>

### 10 — lemma-blowup-reduced

Anglais L17305–17321 ; français L17071–17087.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17305) · FR-ALGEBRA-B36-CHOICE-0010.

Réduit et élément nilpotent sont attestés dans le registre de Dat2.9.2 ; la preuve de fractions est intégralement comparée, avec N=me et la possibilité d'augmenter N. Le slogan reste de même portée ; invariant ne devient pas une assertion réciproque non énoncée.

Règles : FR-ALGEBRA-B36-RULE-BLOWUP, FR-ALGEBRA-B36-RULE-RING, FR-ALGEBRA-B36-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-blowup-reduced}
\begin{slogan}
Being reduced is invariant under blowup
\end{slogan}
If $R$ is reduced then every (affine) blowup algebra of $R$ is reduced.
\end{lemma}

\begin{proof}
Let $I \subset R$ be an ideal and $a \in I$. Suppose $x/a^n$ with
$x \in I^n$ is a nilpotent element of $R[\frac{I}{a}]$. Then
$(x/a^n)^m = 0$. Hence $a^N x^m = 0$ in $R$ for some $N \geq 0$.
After increasing $N$ if necessary we may assume $N = me$ for some
$e \geq 0$. Then $(a^e x)^m = 0$ and since $R$ is reduced we find
$a^e x = 0$. This means that $x/a^n = 0$ in $R[\frac{I}{a}]$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-blowup-reduced}
\begin{slogan}
La propriété d'être réduit est invariante par éclatement
\end{slogan}
Si $R$ est réduit, toute algèbre d'éclatement (affine) de $R$ est réduite.
\end{lemma}

\begin{proof}
Soit $I \subset R$ un idéal et soit $a \in I$. Supposons que $x/a^n$, avec
$x \in I^n$, soit un élément nilpotent de $R[\frac{I}{a}]$. Alors
$(x/a^n)^m = 0$. Ainsi $a^N x^m = 0$ dans $R$ pour un certain $N \geq 0$.
Après avoir augmenté $N$ si nécessaire, on peut supposer $N = me$ pour un certain
$e \geq 0$. Alors $(a^e x)^m = 0$ et, puisque $R$ est réduit, on obtient
$a^e x = 0$. Cela signifie que $x/a^n = 0$ dans $R[\frac{I}{a}]$.
\end{proof}
```

</details>

### 11 — lemma-blowup-domain

Anglais L17322–17334 ; français L17088–17100.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17322) · FR-ALGEBRA-B36-CHOICE-0011.

Anneau intègre, corps des fractions et élément non nul sont attestés chez Dat. La condition a≠0 est bien conservée, essentielle pour exclure la carte nulle. La preuve des deux facteurs dont le produit est nul reste identique.

Règles : FR-ALGEBRA-B36-RULE-BLOWUP, FR-ALGEBRA-B36-RULE-RING, FR-ALGEBRA-B36-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-blowup-domain}
Let $R$ be a domain, $I \subset R$ an ideal, and $a \in I$ a nonzero
element. Then the affine blowup algebra $R[\frac{I}{a}]$ is a domain.
\end{lemma}

\begin{proof}
Suppose $x/a^n$, $y/a^m$ with $x \in I^n$, $y \in I^m$
are elements of $R[\frac{I}{a}]$ whose product is zero.
Then $a^N x y = 0$ in $R$. Since $R$ is a domain we conclude
that either $x = 0$ or $y = 0$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-blowup-domain}
Soit $R$ un anneau intègre, $I \subset R$ un idéal et $a \in I$ un élément
non nul. Alors l'algèbre d'éclatement affine $R[\frac{I}{a}]$ est intègre.
\end{lemma}

\begin{proof}
Supposons que $x/a^n$, $y/a^m$, avec $x \in I^n$, $y \in I^m$,
soient des éléments de $R[\frac{I}{a}]$ dont le produit est nul.
Alors $a^N x y = 0$ dans $R$. Puisque $R$ est intègre, on en déduit
que $x = 0$ ou $y = 0$.
\end{proof}
```

</details>

### 12 — lemma-blowup-dominant

Anglais L17335–17350 ; français L17101–17116.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17335) · FR-ALGEBRA-B36-CHOICE-0012.

Image dense et idéaux premiers minimaux conservent leur sens topologique. La preuve ne suppose pas R réduit : le noyau consiste d'éléments nilpotents. Le texte français ne transforme pas la densité en surjectivité ou injectivité de l'homomorphisme.

Règles : FR-ALGEBRA-B36-RULE-RING, FR-ALGEBRA-B36-RULE-MAP, FR-ALGEBRA-B36-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-blowup-dominant}
Let $R$ be a ring. Let $I \subset R$ be an ideal. Let $a \in I$.
If $a$ is not contained in any minimal prime of $R$, then
$\Spec(R[\frac{I}{a}]) \to \Spec(R)$ has dense image.
\end{lemma}

\begin{proof}
If $a^k x = 0$ for $x \in R$, then $x$ is contained in all the
minimal primes of $R$ and hence nilpotent, see
Lemma \ref{lemma-Zariski-topology}.
Thus the kernel of $R \to R[\frac{I}{a}]$ consists of nilpotent
elements. Hence the result follows from
Lemma \ref{lemma-image-dense-generic-points}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-blowup-dominant}
Soit $R$ un anneau. Soit $I \subset R$ un idéal. Soit $a \in I$.
Si $a$ n'appartient à aucun idéal premier minimal de $R$, alors
$\Spec(R[\frac{I}{a}]) \to \Spec(R)$ a une image dense.
\end{lemma}

\begin{proof}
Si $a^k x = 0$ pour $x \in R$, alors $x$ appartient à tous les
idéaux premiers minimaux de $R$ et est donc nilpotent ; voir le
Lemme \ref{lemma-Zariski-topology}.
Ainsi, le noyau de $R \to R[\frac{I}{a}]$ est constitué d'éléments
nilpotents. Le résultat découle donc du
Lemme \ref{lemma-image-dense-generic-points}.
\end{proof}
```

</details>

### 13 — lemma-valuation-ring-colimit-affine-blowups

Anglais L17351–17401 ; français L17117–17167.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17351) · FR-ALGEBRA-B36-CHOICE-0013.

Colimite filtrante, réunion filtrante, anneau local intègre, corps des fractions et domine sont comparés avec les trois conditions et toute la preuve. Dat2.6.5 définit la domination par contraction de l'idéal maximal ; aucune valuation discrète ni hypothèse noethérienne n'est ajoutée. Le cas R corps pose un défaut source séparé, non corrigé silencieusement. Pour R non corps, multiplier le dénominateur et les numérateurs par un non-zéro de m donne I⊂m ; la domination empêche mR[I/a] d'être l'idéal unité. Cette étape explicative reste dans la revue, non ajoutée à la traduction.

Point particulier à relire : R corps est autorisé par les hypothèses et domine lui-même, mais m=0 impose I=a=0 et une carte nulle incompatible avec la fibre non nulle. La correction source proposée est soit exclure le cas corps, soit traiter ce cas à part, soit autoriser l'idéal unité ; aucune n'est choisie dans le corps de traduction. La preuve de filtrance suppose les a non nuls pour les sous-anneaux de K ; cela est expliqué, non retouché.

Règles : FR-ALGEBRA-B36-RULE-BLOWUP, FR-ALGEBRA-B36-RULE-GRADED, FR-ALGEBRA-B36-RULE-RING, FR-ALGEBRA-B36-RULE-VALUATION, FR-ALGEBRA-B36-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-valuation-ring-colimit-affine-blowups}
Let $(R, \mathfrak m)$ be a local domain with fraction field $K$.
Let $R \subset A \subset K$ be a valuation ring which dominates $R$.
Then
$$
A = \colim R[\textstyle{\frac{I}{a}}]
$$
is a directed colimit of affine blowups $R \to R[\frac{I}{a}]$ with
the following properties
\begin{enumerate}
\item $a \in I \subset \mathfrak m$,
\item $I$ is finitely generated, and
\item the fibre ring of $R \to R[\frac{I}{a}]$ at $\mathfrak m$
is not zero.
\end{enumerate}
\end{lemma}

\begin{proof}
Any blowup algebra $R[\frac{I}{a}]$ is a domain contained in $K$ see
Lemma \ref{lemma-blowup-domain}. The lemma simply says that $A$ is the
directed union of the ones where $a \in I$ have properties (1), (2), (3).
If $R[\frac{I}{a}] \subset A$ and $R[\frac{J}{b}] \subset A$, then
we have
$$
R[\textstyle{\frac{I}{a}}] \cup R[\textstyle{\frac{J}{b}}]  \subset
R[\textstyle{\frac{IJ}{ab}}] \subset A
$$
The first inclusion because $x/a^n = b^nx/(ab)^n$ and the second one
because if $z \in (IJ)^n$, then $z = \sum x_iy_i$ with $x_i \in I^n$
and $y_i \in J^n$ and hence $z/(ab)^n = \sum (x_i/a^n)(y_i/b^n)$
is contained in $A$.

\medskip\noindent
Consider a finite subset $E \subset A$. Say $E = \{e_1, \ldots, e_n\}$.
Choose a nonzero $a \in R$ such that we can write $e_i = f_i/a$ for
all $i = 1, \ldots, n$. Set $I = (f_1, \ldots, f_n, a)$.
We claim that $R[\frac{I}{a}] \subset A$. This is clear as an element
of $R[\frac{I}{a}]$ can be represented as a polynomial in the elements
$e_i$. The lemma follows immediately from this observation.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-valuation-ring-colimit-affine-blowups}
Soit $(R, \mathfrak m)$ un anneau local intègre de corps des fractions $K$.
Soit $R \subset A \subset K$ un anneau de valuation qui domine $R$.
Alors
$$
A = \colim R[\textstyle{\frac{I}{a}}]
$$
est une colimite filtrante d'éclatements affines $R \to R[\frac{I}{a}]$ possédant
les propriétés suivantes :
\begin{enumerate}
\item $a \in I \subset \mathfrak m$,
\item $I$ est de type fini, et
\item l'anneau de la fibre de $R \to R[\frac{I}{a}]$ en $\mathfrak m$
n'est pas nul.
\end{enumerate}
\end{lemma}

\begin{proof}
Toute algèbre d'éclatement $R[\frac{I}{a}]$ est un anneau intègre contenu dans $K$ ; voir le
Lemme \ref{lemma-blowup-domain}. Le lemme dit simplement que $A$ est la
réunion filtrante de celles pour lesquelles $a \in I$ et les propriétés (1), (2), (3) sont satisfaites.
Si $R[\frac{I}{a}] \subset A$ et $R[\frac{J}{b}] \subset A$, alors
on a
$$
R[\textstyle{\frac{I}{a}}] \cup R[\textstyle{\frac{J}{b}}]  \subset
R[\textstyle{\frac{IJ}{ab}}] \subset A
$$
La première inclusion vient de ce que $x/a^n = b^nx/(ab)^n$, et la seconde
de ce que, si $z \in (IJ)^n$, alors $z = \sum x_iy_i$ avec $x_i \in I^n$
et $y_i \in J^n$, et donc $z/(ab)^n = \sum (x_i/a^n)(y_i/b^n)$
appartient à $A$.

\medskip\noindent
Considérons une partie finie $E \subset A$. Écrivons $E = \{e_1, \ldots, e_n\}$.
Choisissons $a \in R$ non nul tel que l'on puisse écrire $e_i = f_i/a$ pour
tout $i = 1, \ldots, n$. Posons $I = (f_1, \ldots, f_n, a)$.
Nous affirmons que $R[\frac{I}{a}] \subset A$. C'est clair, car un élément
de $R[\frac{I}{a}]$ peut être représenté par un polynôme en les éléments
$e_i$. Le lemme résulte immédiatement de cette observation.
\end{proof}
```

</details>

## Contrôles et suite

Les 215 régions mathématiques nouvelles sont exactement identiques. Le préfixe de 12 391 régions passe avec quarante-trois exceptions linguistiques antérieures précisément recensées dans leur ordre et avec leurs multiplicités.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items sont identiques. Aucun titre facultatif ni citation dans ce lot. L’opération inverse retrouve le lot précédent puis tous les octets du témoin public préservé ; préfixe antérieur et suffixe ultérieur restent inchangés.

Les 634 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Groupes Ext, anglais L17402 /français L17168. Aucun PDF nouveau ni publication ; restauration globale en cours.

