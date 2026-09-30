# Anneaux gradués noethériens

## Résultat et portée

Une section complète est comparée : anglais L13774–13990 (217 lignes), français L13616–13824 (209 lignes), soit onze paires complètes. 157 occurrences de règles sont contextualisées ; il ne s’agit pas d’un décompte de tous les mots. Couverture continue : 58 sections, 504 paires et 4663 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Une clarification française : finalement constante devient constante à partir d'un certain rang. Le quantificateur n≫0, le résultat et la démonstration restent les mêmes ; la formulation antérieure n'est pas déclarée fausse. Aucun symbole mathématique, hypothèse ou renvoi n'est modifié. Les fonctions à valeurs dans un groupe abélien et dans K₀′ sont conservées, sans substitution de la formulation plus étroite par la longueur.

La comparaison couvre aussi les deux récurrences, la suite exacte degré par degré, le polynôme sur les classes de congruence et la borne stricte finale. Aucune nouvelle observation source ni admission au registre n’est revendiquée.

Lecture et clarification produites par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. L’appui documentaire est rétrospectif, non présenté comme une consultation lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch24.fr.tex) · [État précédent](staged/fr/010_algebra.prose-batch23.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH23_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH24_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH24_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH24_OCCURRENCES.json) · [Avant/après](ALGEBRA_PROSE_BATCH24_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH24_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH24_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH24_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH24_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH24_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Christian Peskine — Introduction algébrique à la géométrie projective

[Source consultée](https://perso.univ-rennes1.fr/matthieu.romagny/M2_0708/bouquin.pdf) · [Fichier conservé](canon-consulted/fr-algebra/peskine-geometrie-projective-2007.pdf)

Page de titre vérifiée ; pages PDF 118–119 / imprimées 117–118 entièrement lues, §§14.2–14.3. Page PDF 119 rendue et inspectée.

Attestations courtes : « module gradué de type fini », « fonction de Hilbert », « polynôme à coefficients rationnels ».

Registre des modules gradués, additivité, différences finies et base binomiale de Newton. Les égalités asymptotiques sont formulées avec un seuil n₀.

Limites : La fonction de longueur de Peskine a un cadre plus restreint que la fonction K₀′-valuée de Stacks. Ni polynôme numérique A-valué, ni polynôme périodique, ni la phrase constante à partir d'un certain rang ne sont attestés textuellement par ces pages.

SHA-256 : C84D597457282B22B993F523791F4A3E391A74554FF76F7F49878640789435BA.

### Antoine Ducros — Introduction à la théorie des schémas

[Source consultée](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages 24–26 entièrement lues, §§0.1.6–0.1.8.2 et §§0.2.1–0.2.6.

Attestations courtes : « anneau noethérien », « A-algèbre », « groupe abélien », « de type fini », « famille génératrice finie ».

Génération d'une algèbre, permanence noethérienne et distinction entre type fini et présentation finie pour les modules.

Limites : Les pages ne portent pas sur les polynômes numériques ni sur les modules gradués. Elles attestent le registre algébrique général ; les hypothèses précises proviennent de l'original.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

## Clarification française

Le choix explicite la constance à partir d'un seuil. Il ne supprime pas l'indétermination des petites valeurs de n et ne rend pas la fonction constante sur tous les entiers.

### FR-ALGEBRA-B24-REPAIR-0001

Anglais L13866 ; français L13708.

Avant :
```tex
finalement constante
```

Après :
```tex
constante à partir d'un certain rang
```

La différence f(n)−f(n−1), les coefficients binomiaux décalés et le terme a₋₁ sont conservés. Finalement constante devient constante à partir d'un certain rang : clarification du sens de eventually constant, déjà imposé par n≫0, non changement du résultat. La vérification laissée au lecteur n'est pas rédigée à sa place.

Finalement n'est pas traité comme une fausse affirmation mathématique ; la nouvelle formulation explicite le seuil et évite une lecture seulement temporelle. Peskine formule les conclusions asymptotiques avec un seuil n₀, mais n'atteste pas textuellement la nouvelle phrase. La justification principale est le quantificateur officiel.

## Observations sur le texte anglais conservé

Aucune nouvelle observation de défaut source dans ce lot. Les conventions et ellipses pertinentes sont expliquées à côté des passages ; elles ne deviennent pas des corrections cachées. Les observations antérieures restent séparées.

## Règles contextualisées

### FR-ALGEBRA-B24-RULE-GRADED

Degrés, composantes et caractère homogène comparés dans les onze passages complets ; distinction entre degré zéro et multiplication de degré un.

Canon : FR-ALGEBRA-B24-CANON-PESKINE.

### FR-ALGEBRA-B24-RULE-FINITE

Génération finie distinguée de cardinal fini et de présentation finie ; objets algèbre, idéal et module distingués.

Canon : FR-ALGEBRA-B24-CANON-DUCROS, FR-ALGEBRA-B24-CANON-PESKINE.

### FR-ALGEBRA-B24-RULE-NOETHERIAN

Hypothèses noethériennes et quotients comparés, sans élargissement des énoncés.

Canon : FR-ALGEBRA-B24-CANON-DUCROS.

### FR-ALGEBRA-B24-RULE-HILBERT

Appui lexical limité aux polynômes de Hilbert ; définition A-valuée et classes de congruence justifiées directement par Stacks, avec les lacunes d'attestation signalées.

Canon : FR-ALGEBRA-B24-CANON-PESKINE.

### FR-ALGEBRA-B24-RULE-MODULE

Groupes, modules et additivité relus ; aucune fonction de longueur n'est substituée à K₀′.

Canon : FR-ALGEBRA-B24-CANON-DUCROS, FR-ALGEBRA-B24-CANON-PESKINE.

### FR-ALGEBRA-B24-RULE-LOGIC

Quantificateurs, deux récurrences, seuils et sens des inégalités vérifiés en contexte ; l'explicitation du seuil reste fidèle.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-noetherian-graded

Anglais L13774–13780 ; français L13616–13622.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13774) · FR-ALGEBRA-B24-CHOICE-0001.

Le titre et l'introduction annoncent une théorie des anneaux gradués noethériens et des polynômes de Hilbert, sans transformer la section en géométrie projective ni en théorie de la longueur.

Point particulier à relire : L'appui documentaire est obtenu lors de cette révision, non revendiqué pour la traduction initiale.

Règles : FR-ALGEBRA-B24-RULE-GRADED, FR-ALGEBRA-B24-RULE-NOETHERIAN, FR-ALGEBRA-B24-RULE-HILBERT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Noetherian graded rings}
\label{section-noetherian-graded}

\noindent
A bit of theory on Noetherian graded rings including some material on
Hilbert polynomials.
```

Français restauré :
```tex
\section{Anneaux gradués noethériens}
\label{section-noetherian-graded}

\noindent
Quelques éléments de théorie des anneaux gradués noethériens,
notamment sur les polynômes de Hilbert.
```

</details>

### 02 — lemma-S-plus-generated

Anglais L13781–13801 ; français L13623–13643.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13781) · FR-ALGEBRA-B24-CHOICE-0002.

Les deux sens de l'équivalence sont conservés : génération de S comme S₀-algèbre et génération de S₊ comme idéal. La réduction aux éléments homogènes, la récurrence sur d et la composante de degré d−deg(fᵢ) sont comparées ligne par ligne ; aucun générateur supplémentaire ni hypothèse de finitude n'est ajouté.

Point particulier à relire : Le mot engendre porte sur deux structures différentes. La génération de l'idéal n'impose pas ici un ensemble fini ; aucune hypothèse noethérienne n'est anticipée.

Règles : FR-ALGEBRA-B24-RULE-GRADED, FR-ALGEBRA-B24-RULE-FINITE, FR-ALGEBRA-B24-RULE-NOETHERIAN, FR-ALGEBRA-B24-RULE-HILBERT, FR-ALGEBRA-B24-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-S-plus-generated}
Let $S$ be a graded ring. A set of homogeneous elements
$f_i \in S_{+}$ generates $S$ as an algebra over $S_0$ if
and only if they generate $S_{+}$ as an ideal of $S$.
\end{lemma}

\begin{proof}
If the $f_i$ generate $S$ as an algebra over $S_0$ then every element
in $S_{+}$ is a polynomial without constant term in the $f_i$ and hence
$S_{+}$ is generated by the $f_i$ as an ideal. Conversely, suppose that
$S_{+} = \sum Sf_i$. We will prove that any element $f$ of $S$ can be written
as a polynomial in the $f_i$ with coefficients in $S_0$. It suffices
to do this for homogeneous elements. Say $f$ has degree $d$. Then we may
perform induction on $d$. The case $d = 0$ is immediate. If $d > 0$
then $f \in S_{+}$ hence we can write $f = \sum g_i f_i$
for some $g_i \in S$. As $S$ is graded we can replace $g_i$ by its
homogeneous component of degree $d - \deg(f_i)$. By induction we
see that each $g_i$ is a polynomial in the $f_i$ and we win.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-S-plus-generated}
Soit $S$ un anneau gradué. Un ensemble d'éléments homogènes
$f_i \in S_{+}$ engendre $S$ comme algèbre sur $S_0$ si et seulement
si ces éléments engendrent $S_{+}$ comme idéal de $S$.
\end{lemma}

\begin{proof}
Si les $f_i$ engendrent $S$ comme algèbre sur $S_0$, tout élément
de $S_{+}$ est un polynôme sans terme constant en les $f_i$, et donc
$S_{+}$ est engendré par les $f_i$ comme idéal. Réciproquement, supposons que
$S_{+} = \sum Sf_i$. Nous montrerons que tout élément $f$ de $S$ s'écrit
comme un polynôme en les $f_i$ à coefficients dans $S_0$. Il suffit
de le faire pour les éléments homogènes. Supposons que $f$ soit de degré $d$.
Nous pouvons alors raisonner par récurrence sur $d$. Le cas $d = 0$ est immédiat.
Si $d > 0$, alors $f \in S_{+}$, donc nous pouvons écrire $f = \sum g_i f_i$
pour certains $g_i \in S$. Comme $S$ est gradué, nous pouvons remplacer
$g_i$ par sa composante homogène de degré $d - \deg(f_i)$. Par récurrence,
nous voyons que chaque $g_i$ est un polynôme en les $f_i$, et le résultat suit.
\end{proof}
```

</details>

### 03 — lemma-graded-Noetherian

Anglais L13802–13819 ; français L13644–13661.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13802) · FR-ALGEBRA-B24-CHOICE-0003.

Noethérien et de type fini comme idéal restent distincts. Le quotient S/S₊, la décomposition homogène des générateurs et la surjection depuis l'anneau polynomial sont fidèles. Le morphisme envoie Xᵢ sur fᵢ ; les deux renvois officiels sont inchangés.

Point particulier à relire : Le cours de Ducros atteste la permanence des algèbres de type fini sur un anneau noethérien ; les objets et l'argument spécifiques restent ceux de Stacks.

Règles : FR-ALGEBRA-B24-RULE-GRADED, FR-ALGEBRA-B24-RULE-FINITE, FR-ALGEBRA-B24-RULE-NOETHERIAN, FR-ALGEBRA-B24-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-graded-Noetherian}
A graded ring $S$ is Noetherian if and only if $S_0$ is
Noetherian and $S_{+}$ is finitely generated as an ideal of $S$.
\end{lemma}

\begin{proof}
It is clear that if $S$ is Noetherian then $S_0 = S/S_{+}$ is Noetherian
and $S_{+}$ is finitely generated. Conversely, assume $S_0$ is Noetherian
and $S_{+}$ finitely generated as an ideal of $S$. Pick generators
$S_{+} = (f_1, \ldots, f_n)$. By decomposing the $f_i$ into homogeneous
pieces we may assume each $f_i$ is homogeneous. By
Lemma \ref{lemma-S-plus-generated}
we see that $S_0[X_1, \ldots X_n] \to S$ sending $X_i$ to $f_i$
is surjective. Thus $S$ is Noetherian by
Lemma \ref{lemma-Noetherian-permanence}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-graded-Noetherian}
Un anneau gradué $S$ est noethérien si et seulement si $S_0$ est
noethérien et si $S_{+}$ est de type fini comme idéal de $S$.
\end{lemma}

\begin{proof}
Il est clair que si $S$ est noethérien, alors $S_0 = S/S_{+}$ est noethérien
et $S_{+}$ est de type fini. Réciproquement, supposons $S_0$ noethérien
et $S_{+}$ de type fini comme idéal de $S$. Choisissons des générateurs
$S_{+} = (f_1, \ldots, f_n)$. En décomposant les $f_i$ en composantes homogènes,
nous pouvons supposer que chaque $f_i$ est homogène. Par le
Lemme \ref{lemma-S-plus-generated}, nous voyons que
$S_0[X_1, \ldots X_n] \to S$ qui envoie $X_i$ sur $f_i$
est surjectif. Ainsi $S$ est noethérien par le
Lemme \ref{lemma-Noetherian-permanence}.
\end{proof}
```

</details>

### 04 — definition-numerical-polynomial

Anglais L13820–13840 ; français L13662–13682.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13820) · FR-ALGEBRA-B24-CHOICE-0004.

Polynôme numérique est conservé avec la définition locale à valeurs dans un groupe abélien A : combinaison finie des coefficients binomiaux pour n suffisamment grand. La remarque sur Q[T] explique la base binomiale, sans réduire A à Z ou Q ni imposer une définition pour tous les entiers.

Point particulier à relire : Aucune attestation externe exacte de la locution polynôme numérique dans cette généralité A-valuée n'a été trouvée dans les pages consultées. Le choix est justifié provisoirement par la définition explicite de Stacks et la terminologie française des polynômes de Hilbert, non par une prétendue équivalence au polynôme ordinaire.

Règles : FR-ALGEBRA-B24-RULE-FINITE, FR-ALGEBRA-B24-RULE-HILBERT, FR-ALGEBRA-B24-RULE-MODULE, FR-ALGEBRA-B24-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-numerical-polynomial}
Let $A$ be an abelian group.
We say that a function $f : n \mapsto f(n) \in A$
defined for all sufficient large integers $n$ is a
{\it numerical polynomial} if there exists $r \geq 0$,
elements $a_0, \ldots, a_r\in A$ such that
$$
f(n) = \sum\nolimits_{i = 0}^r \binom{n}{i} a_i
$$
for all $n \gg 0$.
\end{definition}

\noindent
The reason for using the binomial coefficients is the
elementary fact that any polynomial $P \in \mathbf{Q}[T]$
all of whose values at integer points are integers, is
equal to a sum $P(T) = \sum a_i \binom{T}{i}$ with
$a_i \in \mathbf{Z}$. Note that in particular the
expressions $\binom{T + 1}{i + 1}$ are of this form.
```

Français restauré :
```tex
\begin{definition}
\label{definition-numerical-polynomial}
Soit $A$ un groupe abélien.
Nous disons qu'une fonction $f : n \mapsto f(n) \in A$
définie pour tous les entiers $n$ suffisamment grands est un
{\it polynôme numérique} s'il existe $r \geq 0$,
des éléments $a_0, \ldots, a_r\in A$ tels que
$$
f(n) = \sum\nolimits_{i = 0}^r \binom{n}{i} a_i
$$
pour tout $n \gg 0$.
\end{definition}

\noindent
La raison d'utiliser les coefficients binomiaux est le
fait élémentaire que tout polynôme $P \in \mathbf{Q}[T]$
dont toutes les valeurs aux points entiers sont entières est
égal à une somme $P(T) = \sum a_i \binom{T}{i}$ avec
$a_i \in \mathbf{Z}$. Remarquons qu'en particulier les
expressions $\binom{T + 1}{i + 1}$ sont de cette forme.
```

</details>

### 05 — lemma-numerical-polynomial-functorial

Anglais L13841–13851 ; français L13683–13693.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13841) · FR-ALGEBRA-B24-CHOICE-0005.

L'homomorphisme de groupes abéliens compose la fonction et transporte les coefficients aᵢ. La composée garde donc la définition précédente. Le résultat immédiat et son degré de généralité sont conservés.

Point particulier à relire : La fonctorialité se fonde sur la définition source, pas sur un théorème externe nouveau. Les groupes abéliens peuvent avoir de la torsion.

Règles : FR-ALGEBRA-B24-RULE-FINITE, FR-ALGEBRA-B24-RULE-HILBERT, FR-ALGEBRA-B24-RULE-MODULE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-numerical-polynomial-functorial}
If $A \to A'$ is a homomorphism of abelian groups and if
$f : n \mapsto f(n) \in A$ is a numerical polynomial,
then so is the composition.
\end{lemma}

\begin{proof}
This is immediate from the definitions.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-numerical-polynomial-functorial}
Si $A \to A'$ est un homomorphisme de groupes abéliens et si
$f : n \mapsto f(n) \in A$ est un polynôme numérique,
alors la composée l'est également.
\end{lemma}

\begin{proof}
Ceci est immédiat d'après les définitions.
\end{proof}
```

</details>

### 06 — lemma-numerical-polynomial

Anglais L13852–13871 ; français L13694–13713.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13852) · FR-ALGEBRA-B24-CHOICE-0006.

La différence f(n)−f(n−1), les coefficients binomiaux décalés et le terme a₋₁ sont conservés. Finalement constante devient constante à partir d'un certain rang : clarification du sens de eventually constant, déjà imposé par n≫0, non changement du résultat. La vérification laissée au lecteur n'est pas rédigée à sa place.

Point particulier à relire : Finalement n'est pas traité comme une fausse affirmation mathématique ; la nouvelle formulation explicite le seuil et évite une lecture seulement temporelle. Peskine formule les conclusions asymptotiques avec un seuil n₀, mais n'atteste pas textuellement la nouvelle phrase. La justification principale est le quantificateur officiel.

Règles : FR-ALGEBRA-B24-RULE-FINITE, FR-ALGEBRA-B24-RULE-HILBERT, FR-ALGEBRA-B24-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-numerical-polynomial}
Suppose that $f: n \mapsto f(n) \in A$
is defined for all $n$ sufficiently large
and suppose that $n \mapsto f(n) - f(n-1)$
is a numerical polynomial. Then $f$ is a
numerical polynomial.
\end{lemma}

\begin{proof}
Let $f(n) - f(n-1) = \sum\nolimits_{i = 0}^r \binom{n}{i} a_i$
for all $n \gg 0$. Set
$g(n) = f(n) - \sum\nolimits_{i = 0}^r \binom{n + 1}{i + 1} a_i$.
Then $g(n) - g(n-1) = 0$ for all $n \gg 0$. Hence $g$ is
eventually constant, say equal to $a_{-1}$. We leave it
to the reader to show that
$a_{-1} + \sum\nolimits_{i = 0}^r \binom{n + 1}{i + 1} a_i$
has the required shape (see remark above the lemma).
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-numerical-polynomial}
Supposons que $f: n \mapsto f(n) \in A$
soit définie pour tout $n$ suffisamment grand,
et supposons que $n \mapsto f(n) - f(n-1)$
soit un polynôme numérique. Alors $f$ est un
polynôme numérique.
\end{lemma}

\begin{proof}
Soit $f(n) - f(n-1) = \sum\nolimits_{i = 0}^r \binom{n}{i} a_i$
pour tout $n \gg 0$. Posons
$g(n) = f(n) - \sum\nolimits_{i = 0}^r \binom{n + 1}{i + 1} a_i$.
Alors $g(n) - g(n-1) = 0$ pour tout $n \gg 0$. Ainsi $g$ est
constante à partir d'un certain rang, disons égale à $a_{-1}$. Nous laissons
au lecteur le soin de montrer que
$a_{-1} + \sum\nolimits_{i = 0}^r \binom{n + 1}{i + 1} a_i$
a la forme requise (voir la remarque au-dessus du lemme).
\end{proof}
```

</details>

### 07 — lemma-graded-module-fg

Anglais L13872–13888 ; français L13714–13730.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13872) · FR-ALGEBRA-B24-CHOICE-0007.

Module gradué de type fini et module fini signifient ici génération finie, pas cardinal fini. Le passage aux composantes homogènes et les monômes de degré n sont relus. Les générateurs de S sont choisis de degré strictement positif, tandis que les degrés des générateurs de M ne sont pas supposés positifs.

Point particulier à relire : Les monômes de degré n forment une famille finie parce que les degrés des fᵢ sont positifs et les familles de générateurs sont finies. Ce détail explique la lecture ; il n'est pas inséré dans la preuve abrégée.

Règles : FR-ALGEBRA-B24-RULE-GRADED, FR-ALGEBRA-B24-RULE-FINITE, FR-ALGEBRA-B24-RULE-MODULE, FR-ALGEBRA-B24-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-graded-module-fg}
If $M$ is a finitely generated graded $S$-module,
and if $S$ is finitely generated over $S_0$, then
each $M_n$ is a finite $S_0$-module.
\end{lemma}

\begin{proof}
Suppose the generators of $M$ are $m_i$ and the generators
of $S$ are $f_i$. By taking homogeneous components we may
assume that the $m_i$ and the $f_i$ are homogeneous
and we may assume $f_i \in S_{+}$. In this case it is
clear that each $M_n$ is generated over $S_0$
by the ``monomials'' $\prod f_i^{e_i} m_j$ whose
degree is $n$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-graded-module-fg}
Si $M$ est un $S$-module gradué de type fini,
et si $S$ est de type fini sur $S_0$, alors
chaque $M_n$ est un $S_0$-module fini.
\end{lemma}

\begin{proof}
Supposons que les générateurs de $M$ soient les $m_i$ et les générateurs
de $S$ les $f_i$. En prenant les composantes homogènes, nous pouvons
supposer que les $m_i$ et les $f_i$ sont homogènes
et nous pouvons supposer $f_i \in S_{+}$. Dans ce cas, il est
clair que chaque $M_n$ est engendré sur $S_0$
par les « monômes » $\prod f_i^{e_i} m_j$ dont le
degré est $n$.
\end{proof}
```

</details>

### 08 — proposition-graded-hilbert-polynomial

Anglais L13889–13945 ; français L13731–13786.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13889) · FR-ALGEBRA-B24-CHOICE-0008.

La fonction prend ses valeurs dans K₀′(S₀), et non dans Z ni dans une longueur. La génération de S₊ en degré un est une hypothèse essentielle. Les deux récurrences, le sous-module maximal de nilpotence, l'additivité degré par degré et l'injectivité finale sont intégralement comparés. La multiplication par x est explicitement non graduée de degré zéro ; la suite relie M_d à M_{d+1}, puis au quotient de degré d+1.

Point particulier à relire : Peskine traite une fonction de longueur dans un cadre plus restreint ; ses hypothèses ne sont pas importées. Le sous-module de nilpotence de x est homogène et la noethérianité donne un exposant uniforme, mais ces détails implicitement utilisés par Stacks ne sont pas ajoutés. La preuve et ses ellipses restent diplomatiques.

Règles : FR-ALGEBRA-B24-RULE-GRADED, FR-ALGEBRA-B24-RULE-FINITE, FR-ALGEBRA-B24-RULE-NOETHERIAN, FR-ALGEBRA-B24-RULE-HILBERT, FR-ALGEBRA-B24-RULE-MODULE, FR-ALGEBRA-B24-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{proposition}
\label{proposition-graded-hilbert-polynomial}
Suppose that $S$ is a Noetherian graded ring
and $M$ a finite graded $S$-module. Consider the
function
$$
\mathbf{Z} \longrightarrow K'_0(S_0), \quad
n \longmapsto [M_n]
$$
see Lemma \ref{lemma-graded-module-fg}.
If $S_{+}$ is generated by elements of degree $1$,
then this function is a numerical polynomial.
\end{proposition}

\begin{proof}
We prove this by induction on the minimal number of
generators of $S_1$. If this number is $0$, then
$M_n = 0$ for all $n \gg 0$ and the result holds.
To prove the induction step, let $x\in S_1$
be one of a minimal set of generators, such that
the induction hypothesis applies to the
graded ring $S/(x)$.

\medskip\noindent
First we show the result holds if $x$ is nilpotent on $M$.
This we do by induction on the minimal integer $r$ such that
$x^r M  = 0$. If $r = 1$, then $M$ is a module over $S/xS$
and the result holds (by the other induction hypothesis).
If $r > 1$, then we can find a short exact sequence
$0 \to M' \to M \to M'' \to 0$ such that the integers
$r', r''$ are strictly smaller than $r$. Thus we know
the result for $M''$ and $M'$. Hence
we get the result for $M$ because of the relation
$
[M_d]  = [M'_d] + [M''_d]
$
in $K'_0(S_0)$.

\medskip\noindent
If $x$ is not nilpotent on $M$, let $M' \subset M$ be
the largest submodule on which $x$ is nilpotent.
Consider the exact sequence $0 \to M' \to M \to M/M' \to 0$
we see again it suffices to prove the result for $M/M'$. In other
words we may assume that multiplication by $x$ is injective.

\medskip\noindent
Let $\overline{M} = M/xM$. Note that the map $x : M \to M$
is {\it not} a map of graded $S$-modules, since it does
not map $M_d$ into $M_d$. Namely, for each $d$ we have the
following short exact sequence
$$
0 \to M_d \xrightarrow{x} M_{d + 1} \to \overline{M}_{d + 1} \to 0
$$
This proves that $[M_{d + 1}] - [M_d] = [\overline{M}_{d + 1}]$.
Hence we win by Lemma \ref{lemma-numerical-polynomial}.
\end{proof}
```

Français restauré :
```tex
\begin{proposition}
\label{proposition-graded-hilbert-polynomial}
Supposons que $S$ soit un anneau gradué noethérien
et $M$ un $S$-module gradué fini. Considérons la
fonction
$$
\mathbf{Z} \longrightarrow K'_0(S_0), \quad
n \longmapsto [M_n]
$$
voir le Lemme \ref{lemma-graded-module-fg}.
Si $S_{+}$ est engendré par des éléments de degré $1$,
alors cette fonction est un polynôme numérique.
\end{proposition}

\begin{proof}
Nous démontrons ceci par récurrence sur le nombre minimal de
générateurs de $S_1$. Si ce nombre est $0$, alors
$M_n = 0$ pour tout $n \gg 0$ et le résultat est vrai.
Pour l'étape de récurrence, soit $x\in S_1$
l'un des générateurs d'un ensemble minimal, tel que
l'hypothèse de récurrence s'applique à l'anneau gradué $S/(x)$.

\medskip\noindent
Montrons d'abord que le résultat est vrai si $x$ est nilpotent sur $M$.
Nous raisonnons par récurrence sur le plus petit entier $r$ tel que
$x^r M  = 0$. Si $r = 1$, alors $M$ est un module sur $S/xS$
et le résultat est vrai (par l'autre hypothèse de récurrence).
Si $r > 1$, nous pouvons trouver une suite exacte courte
$0 \to M' \to M \to M'' \to 0$ telle que les entiers
$r', r''$ soient strictement plus petits que $r$. Nous connaissons donc
le résultat pour $M''$ et $M'$. Ainsi
nous obtenons le résultat pour $M$ en raison de la relation
$
[M_d]  = [M'_d] + [M''_d]
$
dans $K'_0(S_0)$.

\medskip\noindent
Si $x$ n'est pas nilpotent sur $M$, soit $M' \subset M$ le
plus grand sous-module sur lequel $x$ est nilpotent.
Considérons la suite exacte $0 \to M' \to M \to M/M' \to 0$ :
nous voyons à nouveau qu'il suffit de prouver le résultat pour $M/M'$.
Autrement dit, nous pouvons supposer que la multiplication par $x$ est injective.

\medskip\noindent
Posons $\overline{M} = M/xM$. Remarquons que l'application $x : M \to M$
n'est {\it pas} une application de $S$-modules gradués, car elle
n'envoie pas $M_d$ dans $M_d$. En effet, pour chaque $d$, nous avons la
suite exacte courte suivante
$$
0 \to M_d \xrightarrow{x} M_{d + 1} \to \overline{M}_{d + 1} \to 0
$$
Ceci montre que $[M_{d + 1}] - [M_d] = [\overline{M}_{d + 1}]$.
Le résultat découle alors du Lemme \ref{lemma-numerical-polynomial}.
\end{proof}
```

</details>

### 09 — remark-period-polynomial

Anglais L13946–13953 ; français L13787–13794.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13946) · FR-ALGEBRA-B24-CHOICE-0009.

Polynôme périodique conserve l'explication explicite : polynôme numérique sur chaque classe de congruence modulo un entier. Il ne devient pas une fonction périodique. L'absence de génération en degré un est la variante considérée ; le contexte du module fini de la proposition est conservé sans ajout de texte.

Point particulier à relire : Aucune attestation externe exacte de polynôme périodique dans les pages consultées. Quasi-polynôme est une alternative de dénomination possible, non choisie sans nécessité ; l'explication locale de Stacks rend le terme conservé non ambigu. La finitude du module reste une convention contextuelle, pas une correction cachée.

Règles : FR-ALGEBRA-B24-RULE-GRADED, FR-ALGEBRA-B24-RULE-FINITE, FR-ALGEBRA-B24-RULE-NOETHERIAN, FR-ALGEBRA-B24-RULE-HILBERT, FR-ALGEBRA-B24-RULE-MODULE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{remark}
\label{remark-period-polynomial}
If $S$ is still Noetherian but $S$ is not generated in degree $1$,
then the function associated to a graded $S$-module is a periodic
polynomial (i.e., it is a numerical polynomial on the
congruence classes of integers modulo $n$ for some $n$).
\end{remark}
```

Français restauré :
```tex
\begin{remark}
\label{remark-period-polynomial}
Si $S$ est toujours noethérien mais $S$ n'est pas engendré en degré $1$,
alors la fonction associée à un $S$-module gradué est un
polynôme périodique (c'est-à-dire un polynôme numérique sur les
classes de congruence des entiers modulo $n$ pour un certain $n$).
\end{remark}
```

</details>

### 10 — example-hilbert-function

Anglais L13954–13963 ; français L13795–13804.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13954) · FR-ALGEBRA-B24-CHOICE-0010.

L'identification K₀(k)=K₀′(k)=Z et la dimension de M_n sont conservées. L'exemple est le cas polynomial sur le corps k, selon le renvoi officiel. Le module est de type fini ; ni longueur générale ni nombre total de générateurs ne remplace la dimension graduée.

Point particulier à relire : La qualité de corps de k vient du contexte et de l'exemple cité. Aucune nouvelle hypothèse n'est imprimée ; le rôle de la dimension est explicitement relu.

Règles : FR-ALGEBRA-B24-RULE-GRADED, FR-ALGEBRA-B24-RULE-FINITE, FR-ALGEBRA-B24-RULE-HILBERT, FR-ALGEBRA-B24-RULE-MODULE, FR-ALGEBRA-B24-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-hilbert-function}
Suppose that $S = k[X_1, \ldots, X_d]$.
By Example \ref{example-K0-field} we may identify
$K_0(k) = K'_0(k) = \mathbf{Z}$. Hence any finitely
generated graded $k[X_1, \ldots, X_d]$-module
gives rise to a numerical polynomial
$n \mapsto \dim_k(M_n)$.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-hilbert-function}
Supposons que $S = k[X_1, \ldots, X_d]$.
Par l'Exemple \ref{example-K0-field}, nous pouvons identifier
$K_0(k) = K'_0(k) = \mathbf{Z}$. Ainsi tout module gradué
de type fini sur $k[X_1, \ldots, X_d]$
donne lieu à un polynôme numérique
$n \mapsto \dim_k(M_n)$.
\end{example}
```

</details>

### 11 — lemma-quotient-smaller-d

Anglais L13964–13990 ; français L13805–13824.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13964) · FR-ALGEBRA-B24-CHOICE-0011.

Corps, idéal gradué non nul, quotient, degré strictement inférieur à d−1 et exception du polynôme nul pour d=1 sont tous conservés. Les coefficients binomiaux, le degré e de f, l'inclusion dans I_n et les deux inégalités ont leurs mêmes indices et sens. Aucun ≤ ne remplace la borne stricte finale.

Point particulier à relire : Le polynôme de Hilbert d'un quotient peut être nul. L'idéal non nul et la borne d−1 ne sont pas remplacés par une assertion sur tous les idéaux. La preuve est celle de l'original, non une nouvelle démonstration.

Règles : FR-ALGEBRA-B24-RULE-GRADED, FR-ALGEBRA-B24-RULE-NOETHERIAN, FR-ALGEBRA-B24-RULE-HILBERT, FR-ALGEBRA-B24-RULE-MODULE, FR-ALGEBRA-B24-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-quotient-smaller-d}
Let $k$ be a field. Suppose that $I \subset k[X_1, \ldots, X_d]$
is a nonzero graded ideal. Let $M = k[X_1, \ldots, X_d]/I$.
Then the numerical polynomial $n \mapsto \dim_k(M_n)$ (see
Example \ref{example-hilbert-function})
has degree $ < d - 1$ (or is zero if $d = 1$).
\end{lemma}

\begin{proof}
The numerical polynomial associated to the graded module
$k[X_1, \ldots, X_d]$ is $n \mapsto \binom{n - 1 + d}{d - 1}$.
For any nonzero homogeneous $f \in I$ of degree $e$
and any degree $n >> e$ we have $I_n \supset f \cdot k[X_1, \ldots, X_d]_{n-e}$
and hence $\dim_k(I_n) \geq \binom{n - e - 1 + d}{d - 1}$. Hence
$\dim_k(M_n) \leq \binom{n - 1 + d}{d - 1} - \binom{n - e - 1 + d}{d - 1}$.
We win because the last expression
has degree $ < d - 1$ (or is zero if $d = 1$).
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-quotient-smaller-d}
Soit $k$ un corps. Supposons que $I \subset k[X_1, \ldots, X_d]$
soit un idéal gradué non nul. Soit $M = k[X_1, \ldots, X_d]/I$.
Alors le polynôme numérique $n \mapsto \dim_k(M_n)$ (voir
l'Exemple \ref{example-hilbert-function})
est de degré $ < d - 1$ (ou est nul si $d = 1$).
\end{lemma}

\begin{proof}
Le polynôme numérique associé au module gradué
$k[X_1, \ldots, X_d]$ est $n \mapsto \binom{n - 1 + d}{d - 1}$.
Pour tout élément homogène non nul $f \in I$ de degré $e$
et tout degré $n >> e$, nous avons $I_n \supset f \cdot k[X_1, \ldots, X_d]_{n-e}$
et donc $\dim_k(I_n) \geq \binom{n - e - 1 + d}{d - 1}$. Ainsi
$\dim_k(M_n) \leq \binom{n - 1 + d}{d - 1} - \binom{n - e - 1 + d}{d - 1}$.
Le résultat suit car la dernière expression
est de degré $ < d - 1$ (ou est nulle si $d = 1$).
\end{proof}
```

</details>

## Contrôles et suite

Les 159 régions mathématiques sont strictement identiques. Le préfixe de 9 983 régions passe avec les vingt-huit exceptions linguistiques antérieures, sans exception nouvelle. La clarification ne touche aucune région mathématique.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items restent identiques. Aucune citation ni titre facultatif ne figure dans ce lot. Les opérations inverses retrouvent le lot précédent puis tous les octets du témoin public préservé. Préfixe déjà relu et suffixe encore non relu sont inchangés.

Les 504 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Anneaux locaux noethériens, anglais L13991 / français L13825. Aucun PDF nouveau ni publication ; restauration globale en cours.

