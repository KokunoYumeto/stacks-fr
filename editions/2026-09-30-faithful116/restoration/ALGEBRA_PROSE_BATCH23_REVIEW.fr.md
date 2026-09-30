# Proj d’un anneau gradué

## Résultat et portée

Une section complète est comparée : anglais L13364–13773 (410 lignes), français L13209–13615 (407 lignes), soit onze paires complètes. 267 occurrences sont contextualisées. Couverture continue : 57 sections, 493 paires et 4506 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Deux réparations françaises : une nouvelle occurrence d’idéal irrelevant et le remplacement de se plonge dans par s’envoie dans, conformément à la formulation explicite de l’original. Aucun résultat, symbole mathématique ni renvoi n’est modifié. Les localisations de degré zéro, les dix propriétés topologiques et les arguments d’homogénéisation sont relus intégralement.

Ce dossier distingue fidélité de traduction, justification lexicale et observation sur l’original. Une inclusion inversée dans la preuve sur le premier homogène reste littérale dans le français ; le sens correct et un exemple sont argumentés séparément. Aucune nouvelle admission au registre n’est revendiquée.

Lecture et réparations produites par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. L’appui documentaire est rétrospectif, non présenté comme une consultation lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch23.fr.tex) · [État précédent](staged/fr/010_algebra.prose-batch22.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH22_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH23_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH23_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH23_OCCURRENCES.json) · [Avant/après](ALGEBRA_PROSE_BATCH23_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH23_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH23_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH23_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH23_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH23_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Antoine Ducros — Introduction à la théorie des schémas

[Source consultée](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages 274–277 entièrement lues, §§6.1.7–6.1.13.1 ; page 277 rendue et inspectée.

Attestations courtes : « idéal premier homogène », « spectre homogène », « application continue », « homéomorphisme ».

Contraction homogène, composante de degré zéro, localisation et construction de Proj ; distinction entre application continue et morphisme d'espaces annelés.

Limites : Le Sph(B) de Ducros est plus grand que Proj(B). La structure de schéma et ses preuves plus complètes ne sont pas ajoutées au passage topologique de Stacks.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

### Jean-François Dat — Schémas

[Source consultée](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/Schemas/Schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/dat-schemas.pdf)

Pages 57–60 entièrement lues, fin du §2.7.2 puis §§2.7.3–2.7.6.

Attestations courtes : « topologie induite », « Ouverts principaux », « localisé », « sous-anneau », « homéomorphisme ».

Ouverts D₊(f), sous-anneau de degré zéro, correspondance des premiers et localisations des modules dans le registre français.

Limites : Les passages de recollement, faisceaux et fonctorialité sont lus pour le contexte, sans les importer dans Stacks. Aucune correction globale des notes de Dat n'est certifiée.

SHA-256 : 9298B062AC2BDF64161A107980A30F98E1F2DF6DEB4DA98E1FEB21BA494D26A1.

### D. Schaub — Multiplicité et dépendance intégrale sur un idéal

[Source consultée](https://www.numdam.org/item/PSMIR_1976___4_A1_0.pdf) · [Fichier conservé](canon-consulted/fr-algebra/multiplicite-dependance-integrale-1976.pdf)

Page PDF 4 / imprimée 3 relue entièrement, définition 5 et proposition 2 ; inspection visuelle obtenue dans le lot précédent.

Attestations courtes : « un idéal gradué est irrelevant », « un idéal irrelevant ».

Justifie la correction contextuelle de l'occurrence supplémentaire idéal non pertinent.

Limites : Le terme est attesté ; la définition exacte et le rôle de (S/I)₊ restent ceux de Stacks. Pas d'importation des équivalences ou des hypothèses de Schaub.

SHA-256 : DFB4EF15B0D6BAA348EB469B727B2967E9EB40BE4F42B3E6FB803186F3D538A3.

## Réparations françaises

Le vocabulaire irrelevant est attesté et contextualisé. La phrase s’envoie dans garde l’existence du morphisme officiel sans faire appel à une propriété supplémentaire dans cette étape de preuve.

### FR-ALGEBRA-B23-REPAIR-0001

Anglais L13566 ; français L13411.

Avant :
```tex
idéal non pertinent
```

Après :
```tex
idéal irrelevant
```

Les dix assertions sont comparées une à une : ouverts, intersections, décomposition en degrés, cas de degré zéro, base, homéomorphismes, absence possible de quasi-compacité, fermés, idéaux homogènes et critère du fermé vide. Idéal irrelevant remplace une nouvelle occurrence du calque. S'envoie dans remplace se plonge dans : la phrase officielle affirme l'existence d'un morphisme, sans devoir invoquer son injectivité. Tous les quantificateurs, les anneaux quotient et les dix étapes de preuve restent fidèles.

La localisation de degré zéro se définit en fait comme un sous-anneau ; son injection naturelle n'est pas nécessaire à la phrase de preuve considérée. La correction rapproche la formulation de la seule affirmation explicite maps into. Le texte français à l'intérieur de l'affichage et le titre Topologie sur Proj sont deux traductions linguistiques existantes, précisément enregistrées, non de nouvelles formules. Non pertinent a la même référence exacte que dans le lot précédent ; la règle n'est pas appliquée hors de ce passage.

### FR-ALGEBRA-B23-REPAIR-0002

Anglais L13564 ; français L13408.

Avant :
```tex
qui
se plonge dans
```

Après :
```tex
qui
s’envoie dans
```

Les dix assertions sont comparées une à une : ouverts, intersections, décomposition en degrés, cas de degré zéro, base, homéomorphismes, absence possible de quasi-compacité, fermés, idéaux homogènes et critère du fermé vide. Idéal irrelevant remplace une nouvelle occurrence du calque. S'envoie dans remplace se plonge dans : la phrase officielle affirme l'existence d'un morphisme, sans devoir invoquer son injectivité. Tous les quantificateurs, les anneaux quotient et les dix étapes de preuve restent fidèles.

La localisation de degré zéro se définit en fait comme un sous-anneau ; son injection naturelle n'est pas nécessaire à la phrase de preuve considérée. La correction rapproche la formulation de la seule affirmation explicite maps into. Le texte français à l'intérieur de l'affichage et le titre Topologie sur Proj sont deux traductions linguistiques existantes, précisément enregistrées, non de nouvelles formules. Non pertinent a la même référence exacte que dans le lot précédent ; la règle n'est pas appliquée hors de ce passage.

## Observations sur le texte anglais conservé

L’inclusion de la preuve de lemma-smear-out est inversée dans l’original. Elle n’est pas réparée dans la traduction ; le motif et le contre-exemple suivant permettent de l’examiner séparément.

### lemma-smear-out

[Anglais officiel L13663](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13663) · FR-ALGEBRA-B23-SOURCE-NOTE-0001.

```tex
because $\mathfrak p \subset \mathfrak q$.
```

q est engendré par des éléments de p : par définition q⊂p, et cette inclusion permet de déduire fg∈p de fg∈q. L'inclusion imprimée est inversée. Exemple : dans k[x] gradué usuellement, p=(x−1) est premier et son idéal homogène q est (0), car aucun monôme non nul ne s'annule en x=1. Ainsi p n'est pas contenu dans q. La fin de la preuve et le lemme suivant utilisent bien q⊂p. Le français conserve néanmoins le sens imprimé ; correction proposée séparée de la traduction officielle.

Confiance éditoriale forte : définition de q, implication de preuve, exemple explicite et lemme suivant concordent ; ce n'est pas une probabilité calibrée ni une admission au registre.

## Règles contextualisées

### FR-ALGEBRA-B23-RULE-HOMOGENEOUS

Homogénéité, degré, localisation et composantes comparés à leurs objets exacts dans Stacks.

Canon : FR-ALGEBRA-B23-CANON-DUCROS, FR-ALGEBRA-B23-CANON-DAT.

### FR-ALGEBRA-B23-RULE-SPECTRUM

Topologie et correspondances distinguées de la structure de schéma ; dénomination de Stacks conservée.

Canon : FR-ALGEBRA-B23-CANON-DUCROS, FR-ALGEBRA-B23-CANON-DAT.

### FR-ALGEBRA-B23-RULE-IRRELEVANT

L'objet (S/I)₊ est conservé ; seule la dénomination est réparée.

Canon : FR-ALGEBRA-B23-CANON-SCHAUB.

### FR-ALGEBRA-B23-RULE-LOCALIZATION

Composante de degré zéro, relation de fractions et sens des morphismes vérifiés.

Canon : FR-ALGEBRA-B23-CANON-DAT, FR-ALGEBRA-B23-CANON-DUCROS.

### FR-ALGEBRA-B23-RULE-IDEAL

Primalité, minimalité, inclusion et nilpotence sont comparées dans chaque argument, sans réparer silencieusement l'original.

Canon : FR-ALGEBRA-B23-CANON-DUCROS, FR-ALGEBRA-B23-CANON-DAT.

### FR-ALGEBRA-B23-RULE-FINITE

Finitude du module et de l'algèbre, famille de relations éventuellement infinie, hypothèses et conclusions relues.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B23-RULE-LOGIC

Quantificateurs, négations, sens des inclusions et étapes de preuve relus dans les passages complets.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-proj

Anglais L13364–13381 ; français L13209–13226.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13364) · FR-ALGEBRA-B23-CHOICE-0001.

Idéal homogène conserve les trois descriptions équivalentes : sous-module gradué, génération homogène et appartenance composante par composante. Le critère de primalité est testé seulement sur les éléments homogènes, comme dans l'original.

Point particulier à relire : Les attestations servent au vocabulaire ; la définition officielle gouverne l'ensemble et les opérations.

Règles : FR-ALGEBRA-B23-RULE-HOMOGENEOUS, FR-ALGEBRA-B23-RULE-IDEAL, FR-ALGEBRA-B23-RULE-FINITE, FR-ALGEBRA-B23-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Proj of a graded ring}
\label{section-proj}

\noindent
Let $S$ be a graded ring.
A {\it homogeneous ideal} is simply an ideal
$I \subset S$ which is also a graded submodule of $S$.
Equivalently, it is an ideal generated by homogeneous elements.
Equivalently, if $f \in I$ and
$$
f = f_0 + f_1 + \ldots + f_n
$$
is the decomposition of $f$ into homogeneous parts in $S$ then $f_i \in I$
for each $i$. To check that a homogeneous ideal $\mathfrak p$
is prime it suffices to check that if $ab \in \mathfrak p$
with $a, b$ homogeneous then either $a \in \mathfrak p$ or
$b \in \mathfrak p$.
```

Français restauré :
```tex
\section{Proj d'un anneau gradué}
\label{section-proj}

\noindent
Soit $S$ un anneau gradué.
Un {\it idéal homogène} est simplement un idéal
$I \subset S$ qui est aussi un sous-module gradué de $S$.
De manière équivalente, c'est un idéal engendré par des éléments homogènes.
De manière équivalente, si $f \in I$ et
$$
f = f_0 + f_1 + \ldots + f_n
$$
est la décomposition de $f$ en composantes homogènes dans $S$, alors $f_i \in I$
pour tout $i$. Pour vérifier qu'un idéal homogène $\mathfrak p$
est premier, il suffit de vérifier que si $ab \in \mathfrak p$
avec $a, b$ homogènes, alors soit $a \in \mathfrak p$, soit
$b \in \mathfrak p$.
```

</details>

### 02 — definition-proj

Anglais L13382–13409 ; français L13227–13254.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13382) · FR-ALGEBRA-B23-CHOICE-0002.

Proj exclut les idéaux premiers contenant S₊ ; ni tout le spectre homogène de Ducros ni une hypothèse de génération en degré un ne sont importés. La topologie est induite de Spec(S). Les localisations S_(f) et M_(f) sont leurs composantes de degré zéro, non la totalité des localisations.

Point particulier à relire : Ducros nomme spectre homogène Sph(B) l'ensemble de tous les premiers homogènes, puis définit Proj comme un ouvert. Stacks appelle directement Proj spectre homogène. Le français suit ici la dénomination de Stacks, sans confondre les deux ensembles.

Règles : FR-ALGEBRA-B23-RULE-HOMOGENEOUS, FR-ALGEBRA-B23-RULE-SPECTRUM, FR-ALGEBRA-B23-RULE-LOCALIZATION, FR-ALGEBRA-B23-RULE-IDEAL, FR-ALGEBRA-B23-RULE-FINITE, FR-ALGEBRA-B23-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-proj}
Let $S$ be a graded ring.
We define $\text{Proj}(S)$ to be the set of homogeneous
prime ideals $\mathfrak p$ of $S$ such that
$S_{+} \not \subset \mathfrak p$.
The set $\text{Proj}(S)$ is a subset of $\Spec(S)$
and we endow it with the induced topology.
The topological space $\text{Proj}(S)$ is called the
{\it homogeneous spectrum} of the graded ring $S$.
\end{definition}

\noindent
Note that by construction there is a continuous map
$$
\text{Proj}(S) \longrightarrow \Spec(S_0).
$$

\medskip\noindent
Let $S = \oplus_{d \geq 0} S_d$ be a graded ring.
Let $f\in S_d$ and assume that $d \geq 1$.
We define $S_{(f)}$ to be the subring of $S_f$
consisting of elements of the form $r/f^n$ with $r$ homogeneous and
$\deg(r) = nd$. If $M$ is a graded $S$-module,
then we define the $S_{(f)}$-module $M_{(f)}$ as the
sub module of $M_f$ consisting of elements of
the form $x/f^n$ with $x$ homogeneous of degree $nd$.
```

Français restauré :
```tex
\begin{definition}
\label{definition-proj}
Soit $S$ un anneau gradué.
Nous définissons $\text{Proj}(S)$ comme l'ensemble des idéaux
premiers homogènes $\mathfrak p$ de $S$ tels que
$S_{+} \not \subset \mathfrak p$.
L'ensemble $\text{Proj}(S)$ est un sous-ensemble de $\Spec(S)$
et nous le munissons de la topologie induite.
L'espace topologique $\text{Proj}(S)$ est appelé le
{\it spectre homogène} de l'anneau gradué $S$.
\end{definition}

\noindent
Remarquons que, par construction, il existe un morphisme continu
$$
\text{Proj}(S) \longrightarrow \Spec(S_0).
$$

\medskip\noindent
Soit $S = \oplus_{d \geq 0} S_d$ un anneau gradué.
Soit $f\in S_d$ et supposons que $d \geq 1$.
Nous définissons $S_{(f)}$ comme le sous-anneau de $S_f$
constitué des éléments de la forme $r/f^n$, avec $r$ homogène et
$\deg(r) = nd$. Si $M$ est un $S$-module gradué,
nous définissons le $S_{(f)}$-module $M_{(f)}$ comme le
sous-module de $M_f$ constitué des éléments de
la forme $x/f^n$, où $x$ est homogène de degré $nd$.
```

</details>

### 03 — lemma-Z-graded

Anglais L13410–13450 ; français L13255–13295.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13410) · FR-ALGEBRA-B23-CHOICE-0003.

L'élément inversible a un degré strictement positif. Les puissances d et les exposants deg(a), deg(b), i restent identiques. Le radical de p₀S fournit l'idéal premier homogène voulu. La preuve montre ensuite l'ouverture ; sa présentation elliptique de l'injectivité reste source-littérale.

Point particulier à relire : Les explications plus développées de Ducros §§6.1.9–6.1.10 éclairent la lecture, mais ne sont pas incorporées à la preuve elliptique de Stacks. Aucune hypothèse supplémentaire ni amélioration de preuve.

Règles : FR-ALGEBRA-B23-RULE-HOMOGENEOUS, FR-ALGEBRA-B23-RULE-SPECTRUM, FR-ALGEBRA-B23-RULE-LOCALIZATION, FR-ALGEBRA-B23-RULE-IDEAL, FR-ALGEBRA-B23-RULE-FINITE, FR-ALGEBRA-B23-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Z-graded}
Let $S$ be a $\mathbf{Z}$-graded ring containing a homogeneous
invertible element of positive degree. Then the set
$G \subset \Spec(S)$ of $\mathbf{Z}$-graded primes of $S$
(with induced topology) maps homeomorphically to $\Spec(S_0)$.
\end{lemma}

\begin{proof}
First we show that the map is a bijection by constructing an inverse.
Let $f \in S_d$, $d > 0$ be invertible in $S$.
If $\mathfrak p_0$ is a prime of $S_0$, then $\mathfrak p_0S$
is a $\mathbf{Z}$-graded ideal of $S$ such that
$\mathfrak p_0S \cap S_0 = \mathfrak p_0$. And if $ab \in \mathfrak p_0S$
with $a$, $b$ homogeneous, then
$a^db^d/f^{\deg(a) + \deg(b)} \in \mathfrak p_0$.
Thus either $a^d/f^{\deg(a)} \in \mathfrak p_0$ or
$b^d/f^{\deg(b)} \in \mathfrak p_0$, in other words either
$a^d \in \mathfrak p_0S$ or $b^d \in \mathfrak p_0S$.
It follows that $\sqrt{\mathfrak p_0S}$ is a $\mathbf{Z}$-graded
prime ideal of $S$ whose intersection with $S_0$ is $\mathfrak p_0$.

\medskip\noindent
To show that the map is a homeomorphism we show that
the image of $G \cap D(g)$ is open. If $g = \sum g_i$
with $g_i \in S_i$, then by the above $G \cap D(g)$
maps onto the set $\bigcup D(g_i^d/f^i)$ which is open.
\end{proof}

\noindent
For $f \in S$ homogeneous of degree $> 0$ we define
$$
D_{+}(f) = \{ \mathfrak p \in \text{Proj}(S) \mid f \not\in \mathfrak p \}.
$$
Finally, for a homogeneous ideal $I \subset S$ we define
$$
V_{+}(I) = \{ \mathfrak p \in \text{Proj}(S) \mid I \subset \mathfrak p \}.
$$
We will use more generally the notation $V_{+}(E)$ for any
set $E$ of homogeneous elements $E \subset S$.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-Z-graded}
Soit $S$ un anneau gradué par $\mathbf{Z}$ contenant un
élément inversible homogène de degré strictement positif. Alors l'ensemble
$G \subset \Spec(S)$ des idéaux premiers gradués par $\mathbf{Z}$ de $S$
(muni de la topologie induite) s'envoie homéomorphiquement sur $\Spec(S_0)$.
\end{lemma}

\begin{proof}
Montrons d'abord que le morphisme est une bijection en construisant un inverse.
Soit $f \in S_d$, $d > 0$, inversible dans $S$.
Si $\mathfrak p_0$ est un idéal premier de $S_0$, alors
$\mathfrak p_0S$ est un idéal gradué par $\mathbf{Z}$ de $S$ tel que
$\mathfrak p_0S \cap S_0 = \mathfrak p_0$. Et si $ab \in \mathfrak p_0S$
avec $a$, $b$ homogènes, alors
$a^db^d/f^{\deg(a) + \deg(b)} \in \mathfrak p_0$.
Ainsi, soit $a^d/f^{\deg(a)} \in \mathfrak p_0$, soit
$b^d/f^{\deg(b)} \in \mathfrak p_0$, autrement dit soit
$a^d \in \mathfrak p_0S$, soit $b^d \in \mathfrak p_0S$.
Il s'ensuit que $\sqrt{\mathfrak p_0S}$ est un idéal premier
gradué par $\mathbf{Z}$ de $S$ dont l'intersection avec $S_0$ est $\mathfrak p_0$.

\medskip\noindent
Pour montrer que le morphisme est un homéomorphisme, montrons que
l'image de $G \cap D(g)$ est ouverte. Si $g = \sum g_i$
avec $g_i \in S_i$, alors, d'après ce qui précède, $G \cap D(g)$
s'envoie sur l'ensemble $\bigcup D(g_i^d/f^i)$, qui est ouvert.
\end{proof}

\noindent
Pour $f \in S$ homogène de degré $> 0$, nous définissons
$$
D_{+}(f) = \{ \mathfrak p \in \text{Proj}(S) \mid f \not\in \mathfrak p \}.
$$
Enfin, pour un idéal homogène $I \subset S$, nous définissons
$$
V_{+}(I) = \{ \mathfrak p \in \text{Proj}(S) \mid I \subset \mathfrak p \}.
$$
Nous utiliserons plus généralement la notation $V_{+}(E)$ pour tout
ensemble $E$ d'éléments homogènes $E \subset S$.
```

</details>

### 04 — lemma-topology-proj

Anglais L13451–13571 ; français L13296–13416.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13451) · FR-ALGEBRA-B23-CHOICE-0004.

Les dix assertions sont comparées une à une : ouverts, intersections, décomposition en degrés, cas de degré zéro, base, homéomorphismes, absence possible de quasi-compacité, fermés, idéaux homogènes et critère du fermé vide. Idéal irrelevant remplace une nouvelle occurrence du calque. S'envoie dans remplace se plonge dans : la phrase officielle affirme l'existence d'un morphisme, sans devoir invoquer son injectivité. Tous les quantificateurs, les anneaux quotient et les dix étapes de preuve restent fidèles.

Point particulier à relire : La localisation de degré zéro se définit en fait comme un sous-anneau ; son injection naturelle n'est pas nécessaire à la phrase de preuve considérée. La correction rapproche la formulation de la seule affirmation explicite maps into. Le texte français à l'intérieur de l'affichage et le titre Topologie sur Proj sont deux traductions linguistiques existantes, précisément enregistrées, non de nouvelles formules. Non pertinent a la même référence exacte que dans le lot précédent ; la règle n'est pas appliquée hors de ce passage.

Règles : FR-ALGEBRA-B23-RULE-HOMOGENEOUS, FR-ALGEBRA-B23-RULE-SPECTRUM, FR-ALGEBRA-B23-RULE-IRRELEVANT, FR-ALGEBRA-B23-RULE-LOCALIZATION, FR-ALGEBRA-B23-RULE-IDEAL, FR-ALGEBRA-B23-RULE-FINITE, FR-ALGEBRA-B23-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}[Topology on Proj]
\label{lemma-topology-proj}
Let $S = \oplus_{d \geq 0} S_d$ be a graded ring.
\begin{enumerate}
\item The sets $D_{+}(f)$ are open in $\text{Proj}(S)$.
\item We have $D_{+}(ff') = D_{+}(f) \cap D_{+}(f')$.
\item Let $g = g_0 + \ldots + g_m$ be an element
of $S$ with $g_i \in S_i$. Then
$$
D(g) \cap \text{Proj}(S) =
(D(g_0) \cap \text{Proj}(S))
\cup
\bigcup\nolimits_{i \geq 1} D_{+}(g_i).
$$
\item
Let $g_0\in S_0$ be a homogeneous element of degree $0$. Then
$$
D(g_0) \cap \text{Proj}(S)
=
\bigcup\nolimits_{f \in S_d, \ d\geq 1} D_{+}(g_0 f).
$$
\item The open sets $D_{+}(f)$ form a
basis for the topology of $\text{Proj}(S)$.
\item Let $f \in S$ be homogeneous of positive degree.
The ring $S_f$ has a natural $\mathbf{Z}$-grading.
The ring maps $S \to S_f \leftarrow S_{(f)}$ induce
homeomorphisms
$$
D_{+}(f)
\leftarrow
\{\mathbf{Z}\text{-graded primes of }S_f\}
\to
\Spec(S_{(f)}).
$$
\item There exists an $S$ such that $\text{Proj}(S)$ is not
quasi-compact.
\item The sets $V_{+}(I)$ are closed.
\item Any closed subset $T \subset \text{Proj}(S)$ is of
the form $V_{+}(I)$ for some homogeneous ideal $I \subset S$.
\item For any graded ideal $I \subset S$ we have
$V_{+}(I) = \emptyset$ if and only if $S_{+} \subset \sqrt{I}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Since $D_{+}(f) = \text{Proj}(S) \cap D(f)$, these sets are open.
This proves (1). Also (2) follows as $D(ff') = D(f) \cap D(f')$.
Similarly the sets $V_{+}(I) = \text{Proj}(S) \cap V(I)$
are closed. This proves (8).

\medskip\noindent
Suppose that $T \subset \text{Proj}(S)$ is closed.
Then we can write $T = \text{Proj}(S) \cap V(J)$ for some
ideal $J \subset S$. By definition of a homogeneous ideal
if $g \in J$, $g = g_0 + \ldots + g_m$
with $g_d \in S_d$ then $g_d \in \mathfrak p$ for all
$\mathfrak p \in T$. Thus, letting $I \subset S$
be the ideal generated by the homogeneous parts of the elements
of $J$ we have $T = V_{+}(I)$. This proves (9).

\medskip\noindent
The formula for $\text{Proj}(S) \cap D(g)$, with $g \in S$ is direct
from the definitions. This proves (3).
Consider the formula for $\text{Proj}(S) \cap D(g_0)$.
The inclusion of the right hand side in the left hand side is
obvious. For the other inclusion, suppose $g_0 \not \in \mathfrak p$
with $\mathfrak p \in \text{Proj}(S)$. If all $g_0f \in \mathfrak p$
for all homogeneous $f$ of positive degree, then we see that
$S_{+} \subset \mathfrak p$ which is a contradiction. This gives
the other inclusion. This proves (4).

\medskip\noindent
The collection of opens $D(g) \cap \text{Proj}(S)$
forms a basis for the topology since the standard opens
$D(g) \subset \Spec(S)$ form a basis for the topology on
$\Spec(S)$. By the formulas above we can express
$D(g) \cap \text{Proj}(S)$ as a union of opens $D_{+}(f)$.
Hence the collection of opens $D_{+}(f)$ forms a basis for the topology
also. This proves (5).

\medskip\noindent
Proof of (6). First we note that $D_{+}(f)$ may be identified
with a subset (with induced topology) of $D(f) = \Spec(S_f)$
via Lemma \ref{lemma-standard-open}. Note that the ring
$S_f$ has a $\mathbf{Z}$-grading. The homogeneous elements are
of the form $r/f^n$ with $r \in S$ homogeneous and have
degree $\deg(r/f^n) = \deg(r) - n\deg(f)$. The subset
$D_{+}(f)$ corresponds exactly to those prime ideals
$\mathfrak p \subset S_f$ which are $\mathbf{Z}$-graded ideals
(i.e., generated by homogeneous elements). Hence we have to show that
the set of $\mathbf{Z}$-graded prime ideals of $S_f$ maps homeomorphically
to $\Spec(S_{(f)})$. This follows from Lemma \ref{lemma-Z-graded}.

\medskip\noindent
Let $S = \mathbf{Z}[X_1, X_2, X_3, \ldots]$ with grading such that
each $X_i$ has degree $1$. Then it is easy to see that
$$
\text{Proj}(S) = \bigcup\nolimits_{i = 1}^\infty D_{+}(X_i)
$$
does not have a finite refinement. This proves (7).

\medskip\noindent
Let $I \subset S$ be a graded ideal.
If $\sqrt{I} \supset S_{+}$ then $V_{+}(I) = \emptyset$ since
every prime $\mathfrak p \in \text{Proj}(S)$ does not contain
$S_{+}$ by definition. Conversely, suppose that
$S_{+} \not \subset \sqrt{I}$. Then we can find an element
$f \in S_{+}$ such that $f$ is not nilpotent modulo $I$.
Clearly this means that one of the homogeneous parts of $f$
is not nilpotent modulo $I$, in other words we may (and do)
assume that $f$ is homogeneous. This implies that
$I S_f \not = S_f$, in other words that $(S/I)_f$ is not
zero. Hence $(S/I)_{(f)} \not = 0$ since it is a ring
which maps into $(S/I)_f$. Pick a prime
$\mathfrak q \subset (S/I)_{(f)}$. This corresponds to
a graded prime of $S/I$, not containing the irrelevant ideal
$(S/I)_{+}$. And this in turn corresponds to a graded prime
ideal $\mathfrak p$ of $S$, containing $I$ but not containing $S_{+}$
as desired. This proves (10) and finishes the proof.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}[Topologie sur Proj]
\label{lemma-topology-proj}
Soit $S = \oplus_{d \geq 0} S_d$ un anneau gradué.
\begin{enumerate}
\item Les ensembles $D_{+}(f)$ sont ouverts dans $\text{Proj}(S)$.
\item Nous avons $D_{+}(ff') = D_{+}(f) \cap D_{+}(f')$.
\item Soit $g = g_0 + \ldots + g_m$ un élément
de $S$ avec $g_i \in S_i$. Alors
$$
D(g) \cap \text{Proj}(S) =
(D(g_0) \cap \text{Proj}(S))
\cup
\bigcup\nolimits_{i \geq 1} D_{+}(g_i).
$$
\item
Soit $g_0\in S_0$ un élément homogène de degré $0$. Alors
$$
D(g_0) \cap \text{Proj}(S)
=
\bigcup\nolimits_{f \in S_d, \ d\geq 1} D_{+}(g_0 f).
$$
\item Les ouverts $D_{+}(f)$ forment une
base de la topologie de $\text{Proj}(S)$.
\item Soit $f \in S$ homogène de degré positif.
L'anneau $S_f$ possède une graduation naturelle par $\mathbf{Z}$.
Les morphismes d'anneaux $S \to S_f \leftarrow S_{(f)}$ induisent
des homéomorphismes
$$
D_{+}(f)
\leftarrow
\{\mathbf{Z}\text{-idéaux premiers gradués de }S_f\}
\to
\Spec(S_{(f)}).
$$
\item Il existe un $S$ tel que $\text{Proj}(S)$ ne soit pas
quasi-compact.
\item Les ensembles $V_{+}(I)$ sont fermés.
\item Tout fermé $T \subset \text{Proj}(S)$ est de
la forme $V_{+}(I)$ pour un certain idéal homogène $I \subset S$.
\item Pour tout idéal gradué $I \subset S$, nous avons
$V_{+}(I) = \emptyset$ si et seulement si $S_{+} \subset \sqrt{I}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Puisque $D_{+}(f) = \text{Proj}(S) \cap D(f)$, ces ensembles sont ouverts.
Ceci démontre (1). De même, (2) découle de $D(ff') = D(f) \cap D(f')$.
De manière analogue, les ensembles $V_{+}(I) = \text{Proj}(S) \cap V(I)$
sont fermés. Ceci démontre (8).

\medskip\noindent
Supposons que $T \subset \text{Proj}(S)$ soit fermé.
Alors nous pouvons écrire $T = \text{Proj}(S) \cap V(J)$ pour un
idéal $J \subset S$. Par définition d'un idéal homogène,
si $g \in J$, $g = g_0 + \ldots + g_m$
avec $g_d \in S_d$, alors $g_d \in \mathfrak p$ pour tout
$\mathfrak p \in T$. Ainsi, si $I \subset S$
est l'idéal engendré par les composantes homogènes des éléments
de $J$, nous avons $T = V_{+}(I)$. Ceci démontre (9).

\medskip\noindent
La formule pour $\text{Proj}(S) \cap D(g)$, avec $g \in S$, découle directement
des définitions. Ceci démontre (3).
Considérons la formule pour $\text{Proj}(S) \cap D(g_0)$.
L'inclusion du membre de droite dans le membre de gauche est
évidente. Pour l'autre inclusion, supposons $g_0 \not \in \mathfrak p$
avec $\mathfrak p \in \text{Proj}(S)$. Si $g_0f \in \mathfrak p$
pour tout $f$ homogène de degré positif, alors nous voyons que
$S_{+} \subset \mathfrak p$, ce qui est une contradiction. Cela donne
l'autre inclusion. Ceci démontre (4).

\medskip\noindent
La collection des ouverts $D(g) \cap \text{Proj}(S)$
forme une base de la topologie, puisque les ouverts standards
$D(g) \subset \Spec(S)$ forment une base de la topologie de
$\Spec(S)$. D'après les formules ci-dessus, nous pouvons exprimer
$D(g) \cap \text{Proj}(S)$ comme une réunion d'ouverts $D_{+}(f)$.
Ainsi la collection des ouverts $D_{+}(f)$ forme aussi une base de la topologie.
Ceci démontre (5).

\medskip\noindent
Preuve de (6). Notons d'abord que $D_{+}(f)$ peut être identifié
à un sous-ensemble (muni de la topologie induite) de $D(f) = \Spec(S_f)$
via le Lemme \ref{lemma-standard-open}. Remarquons que l'anneau
$S_f$ est gradué par $\mathbf{Z}$. Les éléments homogènes sont
de la forme $r/f^n$ avec $r \in S$ homogène et ont
pour degré $\deg(r/f^n) = \deg(r) - n\deg(f)$. Le sous-ensemble
$D_{+}(f)$ correspond exactement aux idéaux premiers
$\mathfrak p \subset S_f$ qui sont des idéaux gradués par $\mathbf{Z}$
(c'est-à-dire engendrés par des éléments homogènes). Il suffit donc de montrer que
l'ensemble des idéaux premiers gradués par $\mathbf{Z}$ de $S_f$ s'envoie
homéomorphiquement sur $\Spec(S_{(f)})$. Cela découle du Lemme \ref{lemma-Z-graded}.

\medskip\noindent
Soit $S = \mathbf{Z}[X_1, X_2, X_3, \ldots]$ avec une graduation telle que
chaque $X_i$ soit de degré $1$. Alors il est facile de voir que
$$
\text{Proj}(S) = \bigcup\nolimits_{i = 1}^\infty D_{+}(X_i)
$$
n'admet pas de sous-recouvrement fini. Ceci démontre (7).

\medskip\noindent
Soit $I \subset S$ un idéal gradué.
Si $\sqrt{I} \supset S_{+}$, alors $V_{+}(I) = \emptyset$, puisque
tout idéal premier $\mathfrak p \in \text{Proj}(S)$ ne contient pas
$S_{+}$ par définition. Réciproquement, supposons que
$S_{+} \not \subset \sqrt{I}$. Nous pouvons trouver un élément
$f \in S_{+}$ tel que $f$ ne soit pas nilpotent modulo $I$.
Cela signifie clairement que l'une des composantes homogènes de $f$
n'est pas nilpotente modulo $I$; autrement dit, nous pouvons (et allons)
supposer que $f$ est homogène. Cela implique que
$I S_f \not = S_f$, autrement dit que $(S/I)_f$ n'est pas
nul. Donc $(S/I)_{(f)} \not = 0$, puisque c'est un anneau qui
s’envoie dans $(S/I)_f$. Choisissons un idéal premier
$\mathfrak q \subset (S/I)_{(f)}$. Celui-ci correspond à
un idéal premier gradué de $S/I$, qui ne contient pas l'idéal irrelevant
$(S/I)_{+}$. Cela correspond à son tour à un idéal premier
gradué $\mathfrak p$ de $S$, contenant $I$ mais ne contenant pas $S_{+}$,
comme voulu. Ceci démontre (10) et achève la démonstration.
\end{proof}
```

</details>

### 05 — example-proj-polynomial-ring-1-variable

Anglais L13572–13598 ; français L13417–13443.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13572) · FR-ALGEBRA-B23-CHOICE-0005.

La bijection est un homéomorphisme pour tout anneau R, sans hypothèse de corps. X n'appartient pas au premier de Proj, ce qui permet d'en déduire l'appartenance du coefficient a. Les définitions suivantes des fractions de même degré et des relations d'égalité sont relues avec les dénominateurs homogènes hors du premier.

Point particulier à relire : Les fractions peuvent avoir des dénominateurs diviseurs de zéro ; la relation d'égalité emploie explicitement un multiplicateur f″. Pas de supposition d'intégrité.

Règles : FR-ALGEBRA-B23-RULE-HOMOGENEOUS, FR-ALGEBRA-B23-RULE-SPECTRUM, FR-ALGEBRA-B23-RULE-LOCALIZATION, FR-ALGEBRA-B23-RULE-FINITE, FR-ALGEBRA-B23-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-proj-polynomial-ring-1-variable}
Let $R$ be a ring. If $S = R[X]$ with $\deg(X) = 1$, then the natural map
$\text{Proj}(S) \to \Spec(R)$ is a bijection and in fact a homeomorphism.
Namely, suppose $\mathfrak p \in \text{Proj}(S)$. Since
$S_{+} \not \subset \mathfrak p$ we see that $X \not \in \mathfrak p$.
Thus if $aX^n \in \mathfrak p$ with $a \in R$ and $n > 0$, then
$a \in \mathfrak p$. It follows that $\mathfrak p = \mathfrak p_0S$
with $\mathfrak p_0 = \mathfrak p \cap R$.
\end{example}

\noindent
If $\mathfrak p \in \text{Proj}(S)$, then we
define $S_{(\mathfrak p)}$ to be the ring whose
elements are fractions $r/f$ where $r, f \in S$ are homogeneous
elements of the same degree such that $f \not\in \mathfrak p$.
As usual we say $r/f = r'/f'$ if and only if there exists
some $f'' \in S$ homogeneous, $f'' \not \in \mathfrak p$ such
that $f''(rf' - r'f) = 0$.
Given a graded $S$-module $M$ we let
$M_{(\mathfrak p)}$ be the $S_{(\mathfrak p)}$-module
whose elements are fractions $x/f$ with $x \in M$
and $f \in S$ homogeneous of the same degree such that
$f \not \in \mathfrak p$. We say $x/f = x'/f'$
if and only if there exists some $f'' \in S$ homogeneous,
$f'' \not \in \mathfrak p$ such that $f''(xf' - x'f) = 0$.
```

Français restauré :
```tex
\begin{example}
\label{example-proj-polynomial-ring-1-variable}
Soit $R$ un anneau. Si $S = R[X]$ avec $\deg(X) = 1$, alors le morphisme naturel
$\text{Proj}(S) \to \Spec(R)$ est une bijection et même un homéomorphisme.
En effet, soit $\mathfrak p \in \text{Proj}(S)$. Puisque
$S_{+} \not \subset \mathfrak p$, nous voyons que $X \not \in \mathfrak p$.
Ainsi, si $aX^n \in \mathfrak p$ avec $a \in R$ et $n > 0$, alors
$a \in \mathfrak p$. Il s'ensuit que $\mathfrak p = \mathfrak p_0S$
avec $\mathfrak p_0 = \mathfrak p \cap R$.
\end{example}

\noindent
Si $\mathfrak p \in \text{Proj}(S)$, nous
définissons $S_{(\mathfrak p)}$ comme l'anneau dont les
éléments sont les fractions $r/f$, où $r, f \in S$ sont des
éléments homogènes de même degré tels que $f \not\in \mathfrak p$.
Comme d'habitude, nous disons que $r/f = r'/f'$ si et seulement s'il existe
un certain $f'' \in S$ homogène, $f'' \not \in \mathfrak p$, tel
que $f''(rf' - r'f) = 0$.
Étant donné un $S$-module gradué $M$, nous posons
$M_{(\mathfrak p)}$ égal au $S_{(\mathfrak p)}$-module
dont les éléments sont les fractions $x/f$, où $x \in M$
et $f \in S$ sont homogènes de même degré, avec
$f \not \in \mathfrak p$. Nous disons que $x/f = x'/f'$
si et seulement s'il existe un certain $f'' \in S$ homogène,
$f'' \not \in \mathfrak p$, tel que $f''(xf' - x'f) = 0$.
```

</details>

### 06 — lemma-proj-prime

Anglais L13599–13628 ; français L13444–13473.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13599) · FR-ALGEBRA-B23-CHOICE-0006.

Les anneaux et les modules sont localisés au premier correspondant. La formule explicite de ψ et son inverse indiqué gardent leurs exposants et leur ordre de multiplication ; la vérification omise dans Stacks n'est pas complétée dans le français.

Point particulier à relire : Le degré du numérateur et celui du dénominateur sont égaux. La vérification omise n'autorise ni une certification externe nouvelle de l'isomorphisme ni une insertion de preuve.

Règles : FR-ALGEBRA-B23-RULE-HOMOGENEOUS, FR-ALGEBRA-B23-RULE-LOCALIZATION, FR-ALGEBRA-B23-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-proj-prime}
Let $S$ be a graded ring. Let $M$ be a graded $S$-module.
Let $\mathfrak p$ be an element of $\text{Proj}(S)$.
Let $f \in S$ be a homogeneous element of positive degree
such that $f \not \in \mathfrak p$, i.e., $\mathfrak p \in D_{+}(f)$.
Let $\mathfrak p' \subset S_{(f)}$ be the element of
$\Spec(S_{(f)})$ corresponding to $\mathfrak p$ as in
Lemma \ref{lemma-topology-proj}. Then
$S_{(\mathfrak p)} = (S_{(f)})_{\mathfrak p'}$
and compatibly
$M_{(\mathfrak p)} = (M_{(f)})_{\mathfrak p'}$.
\end{lemma}

\begin{proof}
We define a map $\psi : M_{(\mathfrak p)} \to (M_{(f)})_{\mathfrak p'}$.
Let $x/g \in M_{(\mathfrak p)}$. We set
$$
\psi(x/g) = (x g^{\deg(f) - 1}/f^{\deg(x)})/(g^{\deg(f)}/f^{\deg(g)}).
$$
This makes sense since $\deg(x) = \deg(g)$ and since
$g^{\deg(f)}/f^{\deg(g)} \not \in \mathfrak p'$.
We omit the verification that $\psi$ is well defined, a module map
and an isomorphism. Hint: the inverse sends $(x/f^n)/(g/f^m)$ to
$(xf^m)/(g f^n)$.
\end{proof}

\noindent
Here is a graded variant of Lemma \ref{lemma-silly}.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-proj-prime}
Soit $S$ un anneau gradué. Soit $M$ un $S$-module gradué.
Soit $\mathfrak p$ un élément de $\text{Proj}(S)$.
Soit $f \in S$ un élément homogène de degré positif
tel que $f \not \in \mathfrak p$, c'est-à-dire $\mathfrak p \in D_{+}(f)$.
Soit $\mathfrak p' \subset S_{(f)}$ l'élément de
$\Spec(S_{(f)})$ correspondant à $\mathfrak p$ comme dans
le Lemme \ref{lemma-topology-proj}. Alors
$S_{(\mathfrak p)} = (S_{(f)})_{\mathfrak p'}$
et, de manière compatible,
$M_{(\mathfrak p)} = (M_{(f)})_{\mathfrak p'}$.
\end{lemma}

\begin{proof}
Nous définissons un morphisme $\psi : M_{(\mathfrak p)} \to (M_{(f)})_{\mathfrak p'}$.
Soit $x/g \in M_{(\mathfrak p)}$. Posons
$$
\psi(x/g) = (x g^{\deg(f) - 1}/f^{\deg(x)})/(g^{\deg(f)}/f^{\deg(g)}).
$$
Ceci a un sens puisque $\deg(x) = \deg(g)$ et puisque
$g^{\deg(f)}/f^{\deg(g)} \not \in \mathfrak p'$.
Nous omettons la vérification que $\psi$ est bien défini, est un morphisme
de modules et est un isomorphisme. Indication : l'inverse envoie
$(x/f^n)/(g/f^m)$ sur $(xf^m)/(g f^n)$.
\end{proof}

\noindent
Voici une variante graduée du Lemme \ref{lemma-silly}.
```

</details>

### 07 — lemma-graded-silly

Anglais L13629–13649 ; français L13474–13494.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13629) · FR-ALGEBRA-B23-CHOICE-0007.

L'évitement d'une famille finie d'idéaux premiers conserve I⊂S₊, le degré positif, l'absence d'inclusions et la récurrence. La somme de puissances finale est homogène ; le second terme échappe au dernier premier tandis qu'il appartient aux précédents.

Point particulier à relire : Le cas où la famille contient des inclusions est réduit avant la récurrence. Le caractère homogène et les degrés des puissances finales ne sont pas simplifiés.

Règles : FR-ALGEBRA-B23-RULE-HOMOGENEOUS, FR-ALGEBRA-B23-RULE-IDEAL, FR-ALGEBRA-B23-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-graded-silly}
Suppose $S$ is a graded ring, $\mathfrak p_i$, $i = 1, \ldots, r$
homogeneous prime ideals and $I \subset S_{+}$ a graded ideal.
Assume $I \not\subset \mathfrak p_i$ for all $i$. Then there
exists a homogeneous element $x\in I$ of positive degree such
that $x\not\in \mathfrak p_i$ for all $i$.
\end{lemma}

\begin{proof}
We may assume there are no inclusions among the $\mathfrak p_i$.
The result is true for $r = 1$. Suppose the result holds for $r - 1$.
Pick $x \in I$ homogeneous of positive degree such that
$x \not \in \mathfrak p_i$ for all $i = 1, \ldots, r - 1$.
If $x \not\in \mathfrak p_r$ we are done. So assume $x \in \mathfrak p_r$.
If $I \mathfrak p_1 \ldots \mathfrak p_{r-1} \subset \mathfrak p_r$
then $I \subset \mathfrak p_r$ a contradiction.
Pick $y \in I\mathfrak p_1 \ldots \mathfrak p_{r-1}$ homogeneous
and $y \not \in \mathfrak p_r$. Then $x^{\deg(y)} + y^{\deg(x)}$ works.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-graded-silly}
Supposons que $S$ soit un anneau gradué, que les $\mathfrak p_i$, $i = 1, \ldots, r$,
soient des idéaux premiers homogènes et que $I \subset S_{+}$ soit un idéal gradué.
Supposons que $I \not\subset \mathfrak p_i$ pour tout $i$. Alors il
existe un élément homogène $x\in I$ de degré positif tel que
$x\not\in \mathfrak p_i$ pour tout $i$.
\end{lemma}

\begin{proof}
Nous pouvons supposer qu'il n'y a aucune inclusion entre les $\mathfrak p_i$.
Le résultat est vrai pour $r = 1$. Supposons le résultat vrai pour $r - 1$.
Choisissons $x \in I$ homogène de degré positif tel que
$x \not \in \mathfrak p_i$ pour tous les $i = 1, \ldots, r - 1$.
Si $x \not\in \mathfrak p_r$, c'est terminé. Supposons donc $x \in \mathfrak p_r$.
Si $I \mathfrak p_1 \ldots \mathfrak p_{r-1} \subset \mathfrak p_r$,
alors $I \subset \mathfrak p_r$, contradiction.
Choisissons $y \in I\mathfrak p_1 \ldots \mathfrak p_{r-1}$ homogène
et $y \not \in \mathfrak p_r$. Alors $x^{\deg(y)} + y^{\deg(x)}$ convient.
\end{proof}
```

</details>

### 08 — lemma-smear-out

Anglais L13650–13668 ; français L13495–13513.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13650) · FR-ALGEBRA-B23-CHOICE-0008.

L'idéal q est engendré par les éléments homogènes du premier p. La conclusion et l'argument sur les facteurs homogènes sont fidèles. L'inclusion p⊂q imprimée dans la justification est conservée, mais son sens erroné est expliqué séparément : par construction c'est q⊂p. Cette observation n'est pas une modification de la traduction.

Point particulier à relire : Observation source distincte, sans affirmation de déduplication au registre ni de découverte inédite. La traduction garde la coquille d'inclusion ; le dossier indique le sens correct et un exemple concret.

Règles : FR-ALGEBRA-B23-RULE-HOMOGENEOUS, FR-ALGEBRA-B23-RULE-IDEAL, FR-ALGEBRA-B23-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-smear-out}
Let $S$ be a graded ring.
Let $\mathfrak p \subset S$ be a prime.
Let $\mathfrak q$ be the homogeneous ideal of $S$ generated by the
homogeneous elements of $\mathfrak p$. Then $\mathfrak q$ is a
prime ideal of $S$.
\end{lemma}

\begin{proof}
To prove that $\mathfrak q$ is prime, it suffices to check that
if $f, g \in S$ are homogeneous and $fg \in \mathfrak q$, then
either $f$ or $g$ in $\mathfrak q$. Then $fg \in \mathfrak p$
because $\mathfrak p \subset \mathfrak q$. Since $\mathfrak p$
is prime we see that either $f \in \mathfrak p$ or $g \in \mathfrak p$.
Since $f$ and $g$ are homogeneous, it then is clear that either
$f \in \mathfrak q$ or $g \in \mathfrak q$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-smear-out}
Soit $S$ un anneau gradué.
Soit $\mathfrak p \subset S$ un idéal premier.
Soit $\mathfrak q$ l'idéal homogène de $S$ engendré par les
éléments homogènes de $\mathfrak p$. Alors $\mathfrak q$ est un
idéal premier de $S$.
\end{lemma}

\begin{proof}
Pour prouver que $\mathfrak q$ est premier, il suffit de vérifier que
si $f, g \in S$ sont homogènes et si $fg \in \mathfrak q$, alors
$f$ ou $g$ appartient à $\mathfrak q$. Alors $fg \in \mathfrak p$
car $\mathfrak p \subset \mathfrak q$. Comme $\mathfrak p$
est premier, nous voyons que soit $f \in \mathfrak p$, soit $g \in \mathfrak p$.
Comme $f$ et $g$ sont homogènes, il est alors clair que soit
$f \in \mathfrak q$, soit $g \in \mathfrak q$.
\end{proof}
```

</details>

### 09 — lemma-graded-ring-minimal-prime

Anglais L13669–13684 ; français L13514–13529.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13669) · FR-ALGEBRA-B23-CHOICE-0009.

Les deux assertions concernent les premiers minimaux de S puis ceux au-dessus d'un idéal homogène I. Le passage à S/I et l'inclusion q⊂p sont conservés. Pas d'ajout d'hypothèse noethérienne.

Point particulier à relire : Le premier minimal q ne peut être strictement contenu dans p minimal ; ce raisonnement dépend du lemme précédent mais pas de sa coquille locale d'inclusion.

Règles : FR-ALGEBRA-B23-RULE-HOMOGENEOUS, FR-ALGEBRA-B23-RULE-IDEAL, FR-ALGEBRA-B23-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-graded-ring-minimal-prime}
Let $S$ be a graded ring.
\begin{enumerate}
\item Any minimal prime of $S$ is a homogeneous ideal of $S$.
\item Given a homogeneous ideal $I \subset S$ any minimal
prime over $I$ is homogeneous.
\end{enumerate}
\end{lemma}

\begin{proof}
The first assertion holds because the prime $\mathfrak q$ constructed in
Lemma \ref{lemma-smear-out} satisfies $\mathfrak q \subset \mathfrak p$.
The second because we may consider $S/I$ and apply the first part.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-graded-ring-minimal-prime}
Soit $S$ un anneau gradué.
\begin{enumerate}
\item Tout idéal premier minimal de $S$ est un idéal homogène de $S$.
\item Étant donné un idéal homogène $I \subset S$, tout idéal premier
minimal au-dessus de $I$ est homogène.
\end{enumerate}
\end{lemma}

\begin{proof}
La première assertion est vraie car l'idéal premier $\mathfrak q$ construit dans
le Lemme \ref{lemma-smear-out} vérifie $\mathfrak q \subset \mathfrak p$.
La seconde découle de ce que nous pouvons considérer $S/I$ et appliquer la première partie.
\end{proof}
```

</details>

### 10 — lemma-dehomogenize-finite-type

Anglais L13685–13728 ; français L13530–13573.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13685) · FR-ALGEBRA-B23-CHOICE-0010.

La finitude sur R et celle du module sont distinguées. Les générateurs homogènes et leurs fractions sont comparés, ainsi que l'égalité des degrés et la borne e_i<deg(f). Les éléments de degré zéro des localisations demeurent l'objet des deux assertions.

Point particulier à relire : De type fini pour l'algèbre et fini pour le module gardent leur sens de génération finie, non de cardinal fini. Aucun remplacement mécanique hors contexte.

Règles : FR-ALGEBRA-B23-RULE-HOMOGENEOUS, FR-ALGEBRA-B23-RULE-FINITE, FR-ALGEBRA-B23-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-dehomogenize-finite-type}
Let $R$ be a ring. Let $S$ be a graded $R$-algebra. Let $f \in S_{+}$
be homogeneous. Assume that $S$ is of finite type over $R$. Then
\begin{enumerate}
\item the ring $S_{(f)}$ is of finite type over $R$, and
\item for any finite graded $S$-module $M$ the module $M_{(f)}$
is a finite $S_{(f)}$-module.
\end{enumerate}
\end{lemma}

\begin{proof}
Choose $f_1, \ldots, f_n \in S$ which generate $S$ as an $R$-algebra.
We may assume that each $f_i$ is homogeneous (by decomposing each $f_i$
into its homogeneous components). An element of $S_{(f)}$ is a sum
of the form
$$
\sum\nolimits_{e\deg(f) =
\sum e_i\deg(f_i)} \lambda_{e_1 \ldots e_n} f_1^{e_1} \ldots f_n^{e_n}/f^e
$$
with $\lambda_{e_1 \ldots e_n} \in R$. Thus $S_{(f)}$ is generated
as an $R$-algebra by the $f_1^{e_1} \ldots f_n^{e_n} /f^e$ with the
property that $e\deg(f) = \sum e_i\deg(f_i)$. If $e_i \geq \deg(f)$
then we can write this as
$$
f_1^{e_1} \ldots f_n^{e_n}/f^e =
f_i^{\deg(f)}/f^{\deg(f_i)} \cdot
f_1^{e_1} \ldots f_i^{e_i - \deg(f)} \ldots f_n^{e_n}/f^{e - \deg(f_i)}
$$
Thus we only need the elements $f_i^{\deg(f)}/f^{\deg(f_i)}$ as well
as the elements $f_1^{e_1} \ldots f_n^{e_n} /f^e$ with
$e \deg(f) = \sum e_i \deg(f_i)$ and $e_i < \deg(f)$.
This is a finite list and we see that (1) is true.

\medskip\noindent
To see (2) suppose that $M$ is generated by homogeneous elements
$x_1, \ldots, x_m$. Then arguing
as above we find that $M_{(f)}$ is generated as an $S_{(f)}$-module
by the finite list of elements of the form
$f_1^{e_1} \ldots f_n^{e_n} x_j /f^e$
with $e \deg(f) = \sum e_i \deg(f_i) + \deg(x_j)$ and
$e_i < \deg(f)$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-dehomogenize-finite-type}
Soit $R$ un anneau. Soit $S$ une $R$-algèbre graduée. Soit $f \in S_{+}$
homogène. Supposons que $S$ soit de type fini sur $R$. Alors
\begin{enumerate}
\item l'anneau $S_{(f)}$ est de type fini sur $R$, et
\item pour tout $S$-module gradué fini $M$, le module $M_{(f)}$
est un $S_{(f)}$-module fini.
\end{enumerate}
\end{lemma}

\begin{proof}
Choisissons $f_1, \ldots, f_n \in S$ qui engendrent $S$ comme $R$-algèbre.
Nous pouvons supposer que chaque $f_i$ est homogène (en décomposant chaque $f_i$
en ses composantes homogènes). Un élément de $S_{(f)}$ est une somme
de la forme
$$
\sum\nolimits_{e\deg(f) =
\sum e_i\deg(f_i)} \lambda_{e_1 \ldots e_n} f_1^{e_1} \ldots f_n^{e_n}/f^e
$$
avec $\lambda_{e_1 \ldots e_n} \in R$. Ainsi $S_{(f)}$ est engendré
comme $R$-algèbre par les $f_1^{e_1} \ldots f_n^{e_n} /f^e$ vérifiant
$e\deg(f) = \sum e_i\deg(f_i)$. Si $e_i \geq \deg(f)$,
nous pouvons écrire ceci sous la forme
$$
f_1^{e_1} \ldots f_n^{e_n}/f^e =
f_i^{\deg(f)}/f^{\deg(f_i)} \cdot
f_1^{e_1} \ldots f_i^{e_i - \deg(f)} \ldots f_n^{e_n}/f^{e - \deg(f_i)}
$$
Ainsi, il ne nous faut que les éléments $f_i^{\deg(f)}/f^{\deg(f_i)}$, ainsi
que les éléments $f_1^{e_1} \ldots f_n^{e_n} /f^e$ tels que
$e \deg(f) = \sum e_i \deg(f_i)$ et $e_i < \deg(f)$.
Il s'agit d'une liste finie, et nous voyons que (1) est vraie.

\medskip\noindent
Pour voir (2), supposons que $M$ soit engendré par des éléments homogènes
$x_1, \ldots, x_m$. En raisonnant
comme ci-dessus, nous trouvons que $M_{(f)}$ est engendré comme $S_{(f)}$-module
par la liste finie des éléments de la forme
$f_1^{e_1} \ldots f_n^{e_n} x_j /f^e$
avec $e \deg(f) = \sum e_i \deg(f_i) + \deg(x_j)$ et
$e_i < \deg(f)$.
\end{proof}
```

</details>

### 11 — lemma-homogenize

Anglais L13729–13773 ; français L13574–13615.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L13729) · FR-ALGEBRA-B23-CHOICE-0011.

L'algèbre S et le module N sont construits pour une R-algèbre R′ de type fini et un module fini. S₀=R et la génération en degré un sont les conclusions, non des hypothèses sur R′. Homogénéisation minimale, maximum d_j, puissances de X₀, décalages S(−d_j) et conoyau restent identiques ; aucun détail omis n'est ajouté.

Point particulier à relire : Les relations peuvent être indexées par un ensemble J infini ; le module N reste fini parce qu'il est un quotient de S^r. Ne pas remplacer cette conclusion par présenté de façon finie.

Règles : FR-ALGEBRA-B23-RULE-HOMOGENEOUS, FR-ALGEBRA-B23-RULE-LOCALIZATION, FR-ALGEBRA-B23-RULE-IDEAL, FR-ALGEBRA-B23-RULE-FINITE, FR-ALGEBRA-B23-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-homogenize}
Let $R$ be a ring.
Let $R'$ be a finite type $R$-algebra, and let $M$ be a finite $R'$-module.
There exists a graded $R$-algebra $S$, a graded $S$-module $N$ and
an element $f \in S$ homogeneous of degree $1$ such that
\begin{enumerate}
\item $R' \cong S_{(f)}$ and $M \cong N_{(f)}$ (as modules),
\item $S_0 = R$ and $S$ is generated by finitely many elements
of degree $1$ over $R$, and
\item $N$ is a finite $S$-module.
\end{enumerate}
\end{lemma}

\begin{proof}
We may write $R' = R[x_1, \ldots, x_n]/I$ for some ideal $I$.
For an element $g \in R[x_1, \ldots, x_n]$ denote
$\tilde g \in R[X_0, \ldots, X_n]$ the element homogeneous of minimal
degree such that $g = \tilde g(1, x_1, \ldots, x_n)$.
Let $\tilde I \subset R[X_0, \ldots, X_n]$ generated by all
elements $\tilde g$, $g \in I$.
Set $S = R[X_0, \ldots, X_n]/\tilde I$ and denote $f$ the image
of $X_0$ in $S$. By construction we have an isomorphism
$$
S_{(f)} \longrightarrow R', \quad
X_i/X_0 \longmapsto x_i.
$$
To do the same thing with the module $M$ we choose a presentation
$$
M = (R')^{\oplus r}/\sum\nolimits_{j \in J} R'k_j
$$
with $k_j = (k_{1j}, \ldots, k_{rj})$. Let $d_{ij} = \deg(\tilde k_{ij})$.
Set $d_j = \max\{d_{ij}\}$. Set $K_{ij} = X_0^{d_j - d_{ij}}\tilde k_{ij}$
which is homogeneous of degree $d_j$. With this notation we set
$$
N = \Coker\Big(
\bigoplus\nolimits_{j \in J} S(-d_j) \xrightarrow{(K_{ij})} S^{\oplus r}
\Big)
$$
which works. Some details omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-homogenize}
Soit $R$ un anneau.
Soit $R'$ une $R$-algèbre de type fini, et soit $M$ un $R'$-module fini.
Il existe une $R$-algèbre graduée $S$, un $S$-module gradué $N$ et
un élément $f \in S$ homogène de degré $1$ tels que
\begin{enumerate}
\item $R' \cong S_{(f)}$ et $M \cong N_{(f)}$ (comme modules),
\item $S_0 = R$ et $S$ est engendré par un nombre fini d'éléments
de degré $1$ sur $R$, et
\item $N$ est un $S$-module fini.
\end{enumerate}
\end{lemma}

\begin{proof}
Nous pouvons écrire $R' = R[x_1, \ldots, x_n]/I$ pour un certain idéal $I$.
Pour un élément $g \in R[x_1, \ldots, x_n]$, notons
$\tilde g \in R[X_0, \ldots, X_n]$ l'élément homogène de degré minimal
tel que $g = \tilde g(1, x_1, \ldots, x_n)$.
Soit $\tilde I \subset R[X_0, \ldots, X_n]$ l'idéal engendré par tous les
éléments $\tilde g$, $g \in I$.
Posons $S = R[X_0, \ldots, X_n]/\tilde I$ et notons $f$ l'image
de $X_0$ dans $S$. Par construction, nous avons un isomorphisme
$$
S_{(f)} \longrightarrow R', \quad
X_i/X_0 \longmapsto x_i.
$$
Pour faire de même avec le module $M$, choisissons une présentation
$$
M = (R')^{\oplus r}/\sum\nolimits_{j \in J} R'k_j
$$
avec $k_j = (k_{1j}, \ldots, k_{rj})$. Posons $d_{ij} = \deg(\tilde k_{ij})$.
Posons $d_j = \max\{d_{ij}\}$. Posons $K_{ij} = X_0^{d_j - d_{ij}}\tilde k_{ij}$,
qui est homogène de degré $d_j$. Avec cette notation, posons
$$
N = \Coker\Big(
\bigoplus\nolimits_{j \in J} S(-d_j) \xrightarrow{(K_{ij})} S^{\oplus r}
\Big)
$$
ce qui convient. Certains détails sont omis.
\end{proof}
```

</details>

## Contrôles et suite

Les 360 régions mathématiques correspondent exactement après une exception linguistique existante à l’intérieur d’un affichage. Le préfixe de 9 824 régions passe avec vingt-huit exceptions linguistiques au total. Les deux nouvelles opérations ne touchent aucune région mathématique.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items restent identiques. Aucune citation bibliographique ne figure dans ce lot. Le titre facultatif Topologie sur Proj est une traduction existante et fidèle, précisément enregistrée ; l’identité du lemme est inchangée. Les opérations inverses retrouvent le lot précédent puis tous les octets du témoin public préservé. Préfixe déjà relu et suffixe encore non relu sont inchangés.

Les 493 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Anneaux gradués noethériens, anglais L13774 / français L13616. Aucun PDF nouveau ni publication ; restauration globale en cours.

