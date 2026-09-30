# Algèbre commutative : colimites, localisation et Hom

## Résultat et portée

Quatre sections lues entièrement dans les deux langues : lignes officielles 702-1701 et françaises 697-1692. Les 36 paires ci-dessous comprennent énoncés, preuves, slogans, exemples et transitions, sans lacune. Avec le lot 1 conservé, la lecture continue atteint onze sections et 62 paires. Le reste du chapitre et de l’édition n’est pas déclaré certifié.

Deux désignations corollaire sont rétablies là où le français avait harmonisé ou neutralisé la dénomination anglaise. Aucune formule ni assertion mathématique ne change. Les anomalies mathématiques du texte anglais restent diplomatiquement reproduites et signalées séparément ci-dessous. Il ne s’agit pas de deux théorèmes erronés.

Comparaison assistée par IA, sans relecture humaine. La consultation du canon est rétrospective et ne prouve pas que le traducteur initial l’avait consulté. Les attestations restent circonscrites aux passages effectivement lus ; les lacunes sont explicites. La revue experte est bienvenue, jamais une condition d’attente.

Autorité : commit `a04446e57ec1fbc252a871afcec7752fb2807b14`, `algebra.tex`, SHA-256 `FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3`.
[LaTeX actuel](staged/fr/010_algebra.prose-batch2.fr.tex) · [Version précédente conservée](staged/fr/010_algebra.prose-batch1.fr.tex) · [Premier lot](ALGEBRA_PROSE_BATCH1_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH2_VALIDATION.json) · [Choix structurés](ALGEBRA_PROSE_BATCH2_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH2_OCCURRENCES.json) · [Couverture continue](ALGEBRA_PROSE_BATCH2_COVERAGE.json).

## Les deux restaurations de désignation

### FR-ALGEBRA-B2-RESTORE-0001

Source L1371 : The corollary then follows.

Avant :
```tex
L'énoncé en résulte.
```
Après :
```tex
Le corollaire en résulte.
```

Rétablir le nom corollary de la phrase source, que énoncé neutralisait. Le résultat reste dans son environnement lemma ; il ne s'agit pas de corriger le classement anglais.

Alternative : Garder lemme ou énoncé faciliterait une lecture harmonisée mais effacerait la désignation source. Un commentaire séparé peut l'expliquer sans réécrire la traduction.

### FR-ALGEBRA-B2-RESTORE-0002

Source L1375 : If, in the preceding Corollary, we take

Avant :
```tex
Si, dans le lemme précédent, nous prenons
```
Après :
```tex
Si, dans le corollaire précédent, nous prenons
```

Rétablir Corollary, remplacé silencieusement par lemme. Le lecteur retrouve ainsi l'incohérence de dénomination effectivement présente dans le texte officiel, signalée hors du texte traduit.

Alternative : Garder lemme ou énoncé faciliterait une lecture harmonisée mais effacerait la désignation source. Un commentaire séparé peut l'expliquer sans réécrire la traduction.

## Canon français réellement consulté

### Antoine Ducros, Introduction à la théorie des schémas, juillet 2021

[Source universitaire](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [PDF conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

1.6.10.4 et 1.6.11.1-4, pp.63-64 ; 2.1.2-3, pp.69-71 ; 2.1.4.1-4 et 2.1.5.1-2, pp.71-72. Pages indiquées lues en entier ; couverture également lue.

Attestations courtes : « ensemble préordonné », « diagramme commutatif filtrant », « partie multiplicative », « corps des fractions ».

Colimites de modules par somme directe/quotient ; préordre sans antisymétrie ; majorants communs et égalité à un stade ultérieur ; localisation et inversibilité. Ces passages justifient le registre, sans remplacer les preuves officielles.

Limites : Le cours contient ses propres coquilles : Mi pour Xi p.63, et produit de fractions as/bt p.71 au lieu du produit compatible avec la construction p.70. Elles ne sont pas importées. Le passage de colimites filtrantes à l'homologie dans Stacks est comparé directement à la source, non faussement cité comme théorème lu chez Ducros.

SHA-256 : `8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66`.

### Henri Lombardi, Algèbre constructive, JNCF 2014

[Source universitaire](https://www.cristal.univ-lille.fr/jncf2014/files/lecture-notes/lombardi.pdf) · [PDF conservé](canon-consulted/fr-algebra/lombardi-algebre-constructive-2014.pdf)

Définition 3.2, fait 3.3 et contexte pp.6-7 ; ces deux pages sont relues dans ce lot. Inspection visuelle de p.6 consignée auparavant dans le lot 1, non prétendue répétée ici.

Attestations courtes : « de présentation finie », « module des relations », « système générateur ».

Les générateurs sont distingués de leurs relations ; la présentation finie impose un noyau de type fini dans une présentation libre finie.

Limites : Le fait 3.3 n'a pas de preuve détaillée dans le passage. Le A^n de 3.2 après A^m et la convention constructive sur cohérent ne sont pas importés. Ce texte n'est pas utilisé comme preuve de la caractérisation par Hom/colimites.

SHA-256 : `25FC73F21A24EF8AF8D19D3FA86A3156FC34D3CCD8D2A1556CE5DB993B46B723`.

## Règles contextualisées et limites

### FR-ALGEBRA-B2-RULE-colimite

Ducros 1.6.10.4 et 1.6.11.3. Distinguer somme directe de modules et réunion disjointe ensembliste ; ne pas confondre colimite quelconque et colimite filtrante.

Canon : FR-ALGEBRA-B2-CANON-DUCROS.

### FR-ALGEBRA-B2-RULE-filtrant

Ducros 1.6.11.1-3 distingue préordre, majorants communs et diagramme filtrant. Le sens dans chaque occurrence est vérifié contre l'ensemble ou la catégorie d'indices source ; aucune antisymétrie nouvelle.

Canon : FR-ALGEBRA-B2-CANON-DUCROS.

### FR-ALGEBRA-B2-RULE-localisation

Ducros 2.1.2-5. Permettre 0 dans S ; distinguer fractions égales après multiplication et produit en croix ; ne pas transformer le morphisme de localisation en inclusion sans hypothèse.

Canon : FR-ALGEBRA-B2-CANON-DUCROS.

### FR-ALGEBRA-B2-RULE-universel

L'existence, l'unicité et les factorisations gardent les mêmes objets. Ducros pp.64 et 69-71 atteste le registre des propriétés universelles ; le détail des quasi-inverses de modules est contrôlé dans Stacks, pas attribué à ces pages.

Canon : FR-ALGEBRA-B2-CANON-DUCROS.

### FR-ALGEBRA-B2-RULE-exactitude

Vérification directe des noyaux/images, de la variance de Hom et des quantificateurs. Injectivité caractérise la génération finie ; bijectivité caractérise la présentation finie. Pas d'attestation externe exhaustive nouvelle des slogans d'exactitude.

Canon : comparaison source ; pas de nouvelle attestation lexicale indépendante revendiquée.

### FR-ALGEBRA-B2-RULE-presentation

Lombardi 3.2-3.3. Nombre fini de générateurs et de relations, non cardinalité finie du module. Dans M_(S,E), S et E sont finis ; le système d'indices entier peut être infini.

Canon : FR-ALGEBRA-B2-CANON-LOMBARDI.

### FR-ALGEBRA-B2-RULE-hom-variance

Le carré de Hom détermine la précomposition contravariante et la postcomposition covariante. Le titre Hom interne est conservé par son objet mathématique explicite, sans attestation textuelle indépendante nouvellement acquise.

Canon : comparaison source ; pas de nouvelle attestation lexicale indépendante revendiquée.

### FR-ALGEBRA-B2-RULE-quotients

Ducros 1.6.10.4 atteste les sous-modules et quotients ; Lombardi 3.2 les relations. L'image réciproque d'un sous-module localisé est un préimage, non une intersection exigeant une injection. Le facteur direct final est contrôlé contre la factorisation de l'identité.

Canon : FR-ALGEBRA-B2-CANON-DUCROS, FR-ALGEBRA-B2-CANON-LOMBARDI.

## Passages parallèles complets

### 01 — section-colimits

Anglais L702-713 ; français L697-708.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L702) · `FR-ALGEBRA-B2-CHOICE-0001`.

Colimite est attesté chez Ducros, 1.6.10-11. L'ensemble préordonné reste plus général qu'un ensemble partiellement ordonné : ne pas introduire l'antisymétrie. Tous les renvois à Catégories sont conservés.

Règles : FR-ALGEBRA-B2-RULE-colimite, FR-ALGEBRA-B2-RULE-filtrant.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Colimits}
\label{section-colimits}

\noindent
Some of the material in this section overlaps with the general
discussion on colimits in
Categories, Sections \ref{categories-section-limits} --
\ref{categories-section-posets-limits}.
The notion of a preordered set is defined in
Categories, Definition \ref{categories-definition-directed-set}.
It is a slightly weaker notion than a partially ordered set.
```

Français actuel :
```tex
\section{Colimites}
\label{section-colimits}

\noindent
Une partie du contenu de cette section recoupe l'étude générale
des colimites dans
Catégories, sections \ref{categories-section-limits} --
\ref{categories-section-posets-limits}.
La notion d'ensemble préordonné est définie dans
Catégories, Définition \ref{categories-definition-directed-set}.
Elle est légèrement plus faible que celle d'ensemble partiellement ordonné.
```

</details>

### 02 — definition-directed-system

Anglais L714-735 ; français L709-730.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L714) · `FR-ALGEBRA-B2-CHOICE-0002`.

Le système est d'abord défini sur un préordre quelconque ; filtrant ne vaut que sous l'hypothèse supplémentaire sur I. Identités et composition restent inchangées. Ducros 1.6.11.1-2 donne le même préordre et la condition de majorant. La formulation système filtrant est compatible avec cette définition, sans prétendre être une citation mot à mot de son diagramme commutatif filtrant.

Règles : FR-ALGEBRA-B2-RULE-colimite, FR-ALGEBRA-B2-RULE-filtrant.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-directed-system}
Let $(I, \leq)$ be a preordered set.
A {\it system $(M_i, \mu_{ij})$ of $R$-modules over $I$}
consists of a family of $R$-modules $\{M_i\}_{i\in I}$ indexed
by $I$ and a family of $R$-module maps $\{\mu_{ij} : M_i \to M_j\}_{i \leq j}$
such that for all $i \leq j \leq k$
$$
\mu_{ii} = \text{id}_{M_i}\quad
\mu_{ik} = \mu_{jk}\circ \mu_{ij}
$$
We say $(M_i, \mu_{ij})$ is a {\it directed system} if $I$ is a directed set.
\end{definition}

\noindent
This is the same as the notion defined in Categories,
Definition \ref{categories-definition-system-over-poset}
and Section \ref{categories-section-posets-limits}.
We refer to Categories, Definition \ref{categories-definition-colimit}
for the definition of a colimit of a diagram/system in any
category.
```

Français actuel :
```tex
\begin{definition}
\label{definition-directed-system}
Soit $(I, \leq)$ un ensemble préordonné.
Un {\it système $(M_i, \mu_{ij})$ de $R$-modules sur $I$}
est constitué d'une famille de $R$-modules $\{M_i\}_{i\in I}$ indexée
par $I$ et d'une famille d'homomorphismes de $R$-modules $\{\mu_{ij} : M_i \to M_j\}_{i \leq j}$
telles que, pour tous $i \leq j \leq k$,
$$
\mu_{ii} = \text{id}_{M_i}\quad
\mu_{ik} = \mu_{jk}\circ \mu_{ij}
$$
Nous disons que $(M_i, \mu_{ij})$ est un {\it système filtrant} si $I$ est un ensemble filtrant.
\end{definition}

\noindent
C'est la même notion que celle définie dans Catégories,
Définition \ref{categories-definition-system-over-poset}
et section \ref{categories-section-posets-limits}.
Nous renvoyons à Catégories, Définition \ref{categories-definition-colimit},
pour la définition d'une colimite d'un diagramme ou d'un système dans une
catégorie quelconque.
```

</details>

### 03 — lemma-colimit

Anglais L736-776 ; français L731-771.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L736) · `FR-ALGEBRA-B2-CHOICE-0003`.

La somme est directe et le quotient est par le sous-module engendré par les différences indiquées. Le sens des inclusions et de la projection est inchangé. La preuve garde l'unicité et la propriété universelle. Ducros 1.6.10.4 atteste cette construction ; son signe global opposé dans les générateurs n'est pas substitué à celui du Stacks Project. Facteur, dans la somme directe explicitement nommée, ne la transforme pas en produit infini ; sommant serait une autre formulation possible.

Règles : FR-ALGEBRA-B2-RULE-colimite, FR-ALGEBRA-B2-RULE-filtrant, FR-ALGEBRA-B2-RULE-universel, FR-ALGEBRA-B2-RULE-quotients.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-colimit}
Let $(M_i, \mu_{ij})$ be a system of $R$-modules over the preordered set $I$.
The colimit of the system $(M_i, \mu_{ij})$ is the quotient $R$-module
$(\bigoplus_{i\in I} M_i) /Q$ where $Q$ is the
$R$-submodule generated by all elements
$$
\iota_i(x_i) - \iota_j(\mu_{ij}(x_i))
$$
where $\iota_i : M_i \to \bigoplus_{i\in I} M_i$
is the natural inclusion. We denote the colimit
$M = \colim_i M_i$. We denote
$\pi : \bigoplus_{i\in I} M_i \to M$ the
projection map and
$\phi_i = \pi \circ \iota_i : M_i \to M$.
\end{lemma}

\begin{proof}
This lemma is a special case of
Categories, Lemma \ref{categories-lemma-colimits-coproducts-coequalizers}
but we will also prove it directly in this case.
Namely, note that $\phi_i = \phi_j\circ \mu_{ij}$ in the above
construction. To show the pair $(M, \phi_i)$ is the colimit we have
to show it satisfies the universal property: for any other such pair
$(Y, \psi_i)$ with $\psi_i : M_i \to
Y$, $\psi_i = \psi_j\circ \mu_{ij}$, there is a unique $R$-module
homomorphism $g : M \to Y$ such that the
following diagram commutes:
$$
\xymatrix{
M_i \ar[rr]^{\mu_{ij}} \ar[dr]^{\phi_i} \ar[ddr]_{\psi_i} & &
M_j\ar[dl]_{\phi_j} \ar[ddl]^{\psi_j} \\
& M \ar[d]^{g}\\
& Y
}
$$
And this is clear because we can define $g$ by taking the
map $\psi_i$ on the summand $M_i$ in the direct sum
$\bigoplus M_i$.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-colimit}
Soit $(M_i, \mu_{ij})$ un système de $R$-modules sur l'ensemble préordonné $I$.
La colimite du système $(M_i, \mu_{ij})$ est le $R$-module quotient
$(\bigoplus_{i\in I} M_i) /Q$, où $Q$ est le
$R$-sous-module engendré par tous les éléments
$$
\iota_i(x_i) - \iota_j(\mu_{ij}(x_i))
$$
où $\iota_i : M_i \to \bigoplus_{i\in I} M_i$
est l'inclusion canonique. Nous notons la colimite
$M = \colim_i M_i$. Nous notons
$\pi : \bigoplus_{i\in I} M_i \to M$ la
projection et
$\phi_i = \pi \circ \iota_i : M_i \to M$.
\end{lemma}

\begin{proof}
Ce lemme est un cas particulier de
Catégories, Lemme \ref{categories-lemma-colimits-coproducts-coequalizers},
mais nous allons aussi le démontrer directement dans ce cas.
Remarquons en effet que $\phi_i = \phi_j\circ \mu_{ij}$ dans la
construction ci-dessus. Pour montrer que la paire $(M, \phi_i)$ est la colimite, nous devons
montrer qu'elle satisfait la propriété universelle : pour toute autre paire de ce type
$(Y, \psi_i)$ avec $\psi_i : M_i \to
Y$, $\psi_i = \psi_j\circ \mu_{ij}$, il existe un unique homomorphisme de
$R$-modules $g : M \to Y$ tel que le
diagramme suivant soit commutatif :
$$
\xymatrix{
M_i \ar[rr]^{\mu_{ij}} \ar[dr]^{\phi_i} \ar[ddr]_{\psi_i} & &
M_j\ar[dl]_{\phi_j} \ar[ddl]^{\psi_j} \\
& M \ar[d]^{g}\\
& Y
}
$$
Cela est clair, car nous pouvons définir $g$ en prenant
l'application $\psi_i$ sur le facteur $M_i$ de la somme directe
$\bigoplus M_i$.
\end{proof}
```

</details>

### 04 — lemma-directed-colimit

Anglais L777-809 ; français L772-804.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L777) · `FR-ALGEBRA-B2-CHOICE-0004`.

L'hypothèse filtrante permet l'égalité à un indice commun ultérieur. Le texte français garde la réunion disjointe, la relation, l'addition à un majorant commun et l'action des scalaires. Pour un certain traduit exactement for some sans changer l'existence de j. Ducros 1.6.11.3 donne cette description. La preuve reste omise comme dans l'anglais.

Règles : FR-ALGEBRA-B2-RULE-colimite, FR-ALGEBRA-B2-RULE-filtrant.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-directed-colimit}
Let $(M_i, \mu_{ij})$ be a system of $R$-modules over the
preordered set $I$. Assume that $I$ is directed.
The colimit of the system $(M_i, \mu_{ij})$ is canonically
isomorphic to the module $M$ defined as follows:
\begin{enumerate}
\item as a set let
$$
M = \left(\coprod\nolimits_{i \in I} M_i\right)/\sim
$$
where for $m \in M_i$ and $m' \in M_{i'}$ we have
$$
m \sim m' \Leftrightarrow
\mu_{ij}(m) = \mu_{i'j}(m')\text{ for some }j \geq i, i'
$$
\item as an abelian group for $m \in M_i$ and $m' \in M_{i'}$
we define the sum of the classes of $m$ and $m'$ in $M$
to be the class of $\mu_{ij}(m) + \mu_{i'j}(m')$ where
$j \in I$ is any index with $i \leq j$ and $i' \leq j$, and
\item as an $R$-module define for $m \in M_i$ and $x \in R$
the product of $x$ and the class of $m$ in $M$ to be the
class of $xm$ in $M$.
\end{enumerate}
The canonical maps $\phi_i : M_i \to M$ are induced by the canonical
maps $M_i \to \coprod_{i \in I} M_i$.
\end{lemma}

\begin{proof}
Omitted. Compare with
Categories, Section \ref{categories-section-directed-colimits}.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-directed-colimit}
Soit $(M_i, \mu_{ij})$ un système de $R$-modules sur
l'ensemble préordonné $I$. Supposons que $I$ soit filtrant.
La colimite du système $(M_i, \mu_{ij})$ est canoniquement
isomorphe au module $M$ défini comme suit :
\begin{enumerate}
\item comme ensemble, posons
$$
M = \left(\coprod\nolimits_{i \in I} M_i\right)/\sim
$$
où, pour $m \in M_i$ et $m' \in M_{i'}$, nous avons
$$
m \sim m' \Leftrightarrow
\mu_{ij}(m) = \mu_{i'j}(m')\text{ pour un certain }j \geq i, i'
$$
\item comme groupe abélien, pour $m \in M_i$ et $m' \in M_{i'}$,
nous définissons la somme des classes de $m$ et $m'$ dans $M$
comme étant la classe de $\mu_{ij}(m) + \mu_{i'j}(m')$, où
$j \in I$ est un indice quelconque tel que $i \leq j$ et $i' \leq j$, et
\item comme $R$-module, pour $m \in M_i$ et $x \in R$, définissons
le produit de $x$ par la classe de $m$ dans $M$ comme étant la
classe de $xm$ dans $M$.
\end{enumerate}
Les applications canoniques $\phi_i : M_i \to M$ sont induites par les applications
canoniques $M_i \to \coprod_{i \in I} M_i$.
\end{lemma}

\begin{proof}
Démonstration omise. Comparer à
Catégories, section \ref{categories-section-directed-colimits}.
\end{proof}
```

</details>

### 05 — lemma-zero-directed-limit

Anglais L810-822 ; français L805-817.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L810) · `FR-ALGEBRA-B2-CHOICE-0005`.

L'annulation dans la colimite équivaut à l'annulation à un stade ultérieur, et non dès le stade de départ. La condition filtrante et le si et seulement si sont conservés ; aucune injectivité des transitions n'est ajoutée.

Règles : FR-ALGEBRA-B2-RULE-colimite, FR-ALGEBRA-B2-RULE-filtrant.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-zero-directed-limit}
Let $(M_i, \mu_{ij})$ be a directed system.
Let $M = \colim M_i$ with $\mu_i : M_i \to M$.
Then, $\mu_i(x_i) = 0$ for $x_i \in M_i$ if and only if
there exists $j \geq i$ such that $\mu_{ij}(x_i) = 0$.
\end{lemma}

\begin{proof}
This is clear from the description of the directed colimit
in Lemma \ref{lemma-directed-colimit}.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-zero-directed-limit}
Soit $(M_i, \mu_{ij})$ un système filtrant.
Soit $M = \colim M_i$ avec $\mu_i : M_i \to M$.
Alors $\mu_i(x_i) = 0$ pour $x_i \in M_i$ si et seulement s'il
existe $j \geq i$ tel que $\mu_{ij}(x_i) = 0$.
\end{lemma}

\begin{proof}
Cela résulte clairement de la description de la colimite filtrante
du Lemme \ref{lemma-directed-colimit}.
\end{proof}
```

</details>

### 06 — example-zero-colimit-different

Anglais L823-842 ; français L818-837.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L823) · `FR-ALGEBRA-B2-CHOICE-0006`.

Le préordre en fourche n'a que les deux inégalités déclarées. Le conoyau conserve le signe moins, la somme des noyaux pour M_a et l'image du noyau pour M_b. Il montre l'échec du critère précédent sans filtrance, sans contredire sa version filtrante.

Règles : FR-ALGEBRA-B2-RULE-colimite, FR-ALGEBRA-B2-RULE-filtrant, FR-ALGEBRA-B2-RULE-exactitude.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-zero-colimit-different}
Consider the partially ordered set $I = \{a, b, c\}$ with
$a < b$ and $a < c$ and no other strict inequalities.
A system $(M_a, M_b, M_c, \mu_{ab}, \mu_{ac})$
over $I$ consists of three $R$-modules $M_a, M_b, M_c$
and two $R$-module homomorphisms $\mu_{ab} : M_a \to M_b$ and
$\mu_{ac} : M_a \to M_c$.
The colimit of the system is just
$$
M := \colim_{i \in I} M_i = \Coker(M_a \to M_b \oplus M_c)
$$
where the map is $\mu_{ab} \oplus -\mu_{ac}$. Thus the kernel of the
canonical map $M_a \to M$ is $\Ker(\mu_{ab}) + \Ker(\mu_{ac})$.
And the kernel of the canonical map $M_b \to M$ is the image of
$\Ker(\mu_{ac})$ under the map $\mu_{ab}$. Hence clearly
the result of Lemma \ref{lemma-zero-directed-limit} is false for
general systems.
\end{example}
```

Français actuel :
```tex
\begin{example}
\label{example-zero-colimit-different}
Considérons l'ensemble partiellement ordonné $I = \{a, b, c\}$ avec
$a < b$ et $a < c$, et aucune autre inégalité stricte.
Un système $(M_a, M_b, M_c, \mu_{ab}, \mu_{ac})$
sur $I$ est constitué de trois $R$-modules $M_a, M_b, M_c$
et de deux homomorphismes de $R$-modules $\mu_{ab} : M_a \to M_b$ et
$\mu_{ac} : M_a \to M_c$.
La colimite du système est simplement
$$
M := \colim_{i \in I} M_i = \Coker(M_a \to M_b \oplus M_c)
$$
où l'application est $\mu_{ab} \oplus -\mu_{ac}$. Le noyau de
l'application canonique $M_a \to M$ est donc $\Ker(\mu_{ab}) + \Ker(\mu_{ac})$.
Et le noyau de l'application canonique $M_b \to M$ est l'image de
$\Ker(\mu_{ac})$ par l'application $\mu_{ab}$. Par conséquent, il est clair que
le résultat du Lemme \ref{lemma-zero-directed-limit} est faux pour les
systèmes généraux.
\end{example}
```

</details>

### 07 — definition-homomorphism-directed-systems

Anglais L843-861 ; français L838-856.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L843) · `FR-ALGEBRA-B2-CHOICE-0007`.

Les systèmes ont le même ensemble d'indices ; les composantes satisfont le même carré de naturalité. Transformation naturelle rend la transformation de foncteurs technique de l'anglais, non une hypothèse nouvelle. L'ordre de composition est contrôlé dans la formule.

Règles : FR-ALGEBRA-B2-RULE-filtrant, FR-ALGEBRA-B2-RULE-hom-variance.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-homomorphism-directed-systems}
Let $(M_i, \mu_{ij})$, $(N_i, \nu_{ij})$ be
systems of $R$-modules over the same preordered set $I$.
A {\it homomorphism of systems} $\Phi$ from $(M_i, \mu_{ij})$ to
$(N_i, \nu_{ij})$ is by definition a family of $R$-module homomorphisms
$\phi_i : M_i \to N_i$
such that $\phi_j \circ \mu_{ij} = \nu_{ij} \circ \phi_i$
for all $i \leq j$.
\end{definition}

\noindent
This is the same notion as a transformation of functors
between the associated diagrams $M : I \to \text{Mod}_R$
and $N : I \to \text{Mod}_R$, in the language of
categories.
The following lemma is a special case of
Categories, Lemma \ref{categories-lemma-functorial-colimit}.
```

Français actuel :
```tex
\begin{definition}
\label{definition-homomorphism-directed-systems}
Soient $(M_i, \mu_{ij})$, $(N_i, \nu_{ij})$ des
systèmes de $R$-modules sur le même ensemble préordonné $I$.
Un {\it homomorphisme de systèmes} $\Phi$ de $(M_i, \mu_{ij})$ vers
$(N_i, \nu_{ij})$ est, par définition, une famille d'homomorphismes de $R$-modules
$\phi_i : M_i \to N_i$
tels que $\phi_j \circ \mu_{ij} = \nu_{ij} \circ \phi_i$
pour tous $i \leq j$.
\end{definition}

\noindent
C'est la même notion que celle de transformation naturelle de foncteurs
entre les diagrammes associés $M : I \to \text{Mod}_R$
et $N : I \to \text{Mod}_R$, dans le langage des
catégories.
Le lemme suivant est un cas particulier de
Catégories, Lemme \ref{categories-lemma-functorial-colimit}.
```

</details>

### 08 — lemma-homomorphism-limit

Anglais L862-906 ; français L857-901.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L862) · `FR-ALGEBRA-B2-CHOICE-0008`.

Le morphisme induit est unique et compatible aux applications structurales. La preuve utilise les sommes directes puis envoie les générateurs du premier noyau dans le second. Les inclusions de sommants implicites dans x_j moins mu_jk(x_j) restent implicites ; aucune autre construction n'est introduite.

Règles : FR-ALGEBRA-B2-RULE-filtrant, FR-ALGEBRA-B2-RULE-universel, FR-ALGEBRA-B2-RULE-exactitude.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-homomorphism-limit}
Let $(M_i, \mu_{ij})$, $(N_i, \nu_{ij})$ be
systems of $R$-modules over the same preordered set.
A morphism of systems $\Phi = (\phi_i)$ from $(M_i, \mu_{ij})$ to
$(N_i, \nu_{ij})$ induces a unique homomorphism
$$
\colim \phi_i : \colim M_i \longrightarrow \colim N_i
$$
such that
$$
\xymatrix{
M_i \ar[r] \ar[d]_{\phi_i} & \colim M_i \ar[d]^{\colim \phi_i} \\
N_i \ar[r] & \colim N_i
}
$$
commutes for all $i \in I$.
\end{lemma}

\begin{proof}
Write $M = \colim M_i$ and $N = \colim N_i$ and $\phi = \colim \phi_i$
(as yet to be constructed). We will use the explicit description of $M$
and $N$ in Lemma \ref{lemma-colimit} without further mention.
The condition of the lemma is equivalent to the condition that
$$
\xymatrix{
\bigoplus_{i\in I} M_i \ar[r] \ar[d]_{\bigoplus\phi_i} & M \ar[d]^\phi \\
\bigoplus_{i\in I} N_i \ar[r] & N
}
$$
commutes. Hence it is clear that if $\phi$ exists, then it is unique.
To see that $\phi$ exists, it suffices to show that the kernel of the
upper horizontal arrow is mapped by $\bigoplus \phi_i$ to the kernel
of the lower horizontal arrow. To see this, let $j \leq k$ and
$x_j \in M_j$. Then
$$
(\bigoplus \phi_i)(x_j - \mu_{jk}(x_j))
=
\phi_j(x_j) - \phi_k(\mu_{jk}(x_j))
=
\phi_j(x_j) - \nu_{jk}(\phi_j(x_j))
$$
which is in the kernel of the lower horizontal arrow as required.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-homomorphism-limit}
Soient $(M_i, \mu_{ij})$, $(N_i, \nu_{ij})$ des
systèmes de $R$-modules sur le même ensemble préordonné.
Un morphisme de systèmes $\Phi = (\phi_i)$ de $(M_i, \mu_{ij})$ vers
$(N_i, \nu_{ij})$ induit un unique homomorphisme
$$
\colim \phi_i : \colim M_i \longrightarrow \colim N_i
$$
tel que
$$
\xymatrix{
M_i \ar[r] \ar[d]_{\phi_i} & \colim M_i \ar[d]^{\colim \phi_i} \\
N_i \ar[r] & \colim N_i
}
$$
soit commutatif pour tout $i \in I$.
\end{lemma}

\begin{proof}
Écrivons $M = \colim M_i$, $N = \colim N_i$ et $\phi = \colim \phi_i$
(ce dernier restant à construire). Nous utiliserons sans autre mention la description explicite de $M$
et de $N$ donnée au Lemme \ref{lemma-colimit}.
La condition du lemme équivaut à ce que
$$
\xymatrix{
\bigoplus_{i\in I} M_i \ar[r] \ar[d]_{\bigoplus\phi_i} & M \ar[d]^\phi \\
\bigoplus_{i\in I} N_i \ar[r] & N
}
$$
soit commutatif. Il est donc clair que, si $\phi$ existe, il est unique.
Pour voir que $\phi$ existe, il suffit de montrer que le noyau de la
flèche horizontale supérieure est envoyé par $\bigoplus \phi_i$ dans le noyau
de la flèche horizontale inférieure. Pour cela, soient $j \leq k$ et
$x_j \in M_j$. Alors
$$
(\bigoplus \phi_i)(x_j - \mu_{jk}(x_j))
=
\phi_j(x_j) - \phi_k(\mu_{jk}(x_j))
=
\phi_j(x_j) - \nu_{jk}(\phi_j(x_j))
$$
appartient au noyau de la flèche horizontale inférieure, comme voulu.
\end{proof}
```

</details>

### 09 — lemma-directed-colimit-exact

Anglais L907-982 ; français L902-977.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L907) · `FR-ALGEBRA-B2-CHOICE-0009`.

Le slogan distingue colimites filtrantes et colimites sur un ensemble filtrant. L'énoncé suppose un complexe, pas son exactitude : son homologie H_i peut être non nulle. Le français conserve cette portée, les deux étapes de surjectivité et d'injectivité, puis le passage à un indice ultérieur. Aucune suite courte avec des zéros nouveaux n'est ajoutée.

Règles : FR-ALGEBRA-B2-RULE-colimite, FR-ALGEBRA-B2-RULE-filtrant, FR-ALGEBRA-B2-RULE-exactitude.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-directed-colimit-exact}
\begin{slogan}
Filtered colimits are exact. Directed colimits are exact.
\end{slogan}
Let $I$ be a directed set.
Let $(L_i, \lambda_{ij})$, $(M_i, \mu_{ij})$, and
$(N_i, \nu_{ij})$ be systems of $R$-modules over $I$.
Let $\varphi_i : L_i \to M_i$ and $\psi_i : M_i \to N_i$ be
morphisms of systems over $I$. Assume that for all $i \in I$ the
sequence of $R$-modules
$$
\xymatrix{
L_i \ar[r]^{\varphi_i} &
M_i \ar[r]^{\psi_i} &
N_i
}
$$
is a complex with homology $H_i$.
Then the $R$-modules $H_i$ form a system over $I$,
the sequence of $R$-modules
$$
\xymatrix{
\colim_i L_i \ar[r]^\varphi &
\colim_i M_i \ar[r]^\psi &
\colim_i N_i
}
$$
is a complex as well, and denoting $H$ its homology we have
$$
H = \colim_i H_i.
$$
\end{lemma}

\begin{proof}
It is clear that
$
\xymatrix{
\colim_i L_i \ar[r]^\varphi &
\colim_i M_i \ar[r]^\psi &
\colim_i N_i
}
$
is a complex. For each $i \in I$, there is a canonical
$R$-module morphism $H_i \to H$ (sending each
$[m] \in H_i = \Ker(\psi_i) / \Im(\varphi_i)$ to the
residue class in $H = \Ker(\psi) / \Im(\varphi)$
of the image of $m$ in $\colim_i M_i$). These give rise
to a morphism $\colim_i H_i \to H$. It remains to
show that this morphism is surjective and injective.

\medskip\noindent
We are going to repeatedly use the description of colimits over $I$
as in Lemma \ref{lemma-directed-colimit} without further mention.
Let $h \in H$.
Since $H = \Ker(\psi)/\Im(\varphi)$ we see that
$h$ is the class mod $\Im(\varphi)$ of an element $[m]$
in $\Ker(\psi) \subset \colim_i M_i$. Choose an
$i$ such that $[m]$ comes from an element $m \in M_i$. Choose
a $j \geq i$ such that $\nu_{ij}(\psi_i(m)) = 0$ which is possible
since $[m] \in \Ker(\psi)$. After replacing $i$ by $j$ and
$m$ by $\mu_{ij}(m)$ we see that we may assume $m \in \Ker(\psi_i)$.
This shows that the map $\colim_i H_i \to H$ is surjective.

\medskip\noindent
Suppose that $h_i \in H_i$ has image zero on $H$. Since
$H_i = \Ker(\psi_i)/\Im(\varphi_i)$ we may represent
$h_i$ by an element $m \in \Ker(\psi_i) \subset M_i$.
The assumption on the vanishing of $h_i$ in $H$ means that
the class of $m$ in $\colim_i M_i$ lies in the image
of $\varphi$. Hence there exists a $j \geq i$ and an $l \in L_j$
such that $\varphi_j(l) = \mu_{ij}(m)$. Clearly this shows that
the image of $h_i$ in $H_j$ is zero. This proves the
injectivity of $\colim_i H_i \to H$.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-directed-colimit-exact}
\begin{slogan}
Les colimites filtrantes sont exactes. Les colimites sur un ensemble filtrant sont exactes.
\end{slogan}
Soit $I$ un ensemble filtrant.
Soient $(L_i, \lambda_{ij})$, $(M_i, \mu_{ij})$ et
$(N_i, \nu_{ij})$ des systèmes de $R$-modules sur $I$.
Soient $\varphi_i : L_i \to M_i$ et $\psi_i : M_i \to N_i$ des
morphismes de systèmes sur $I$. Supposons que, pour tout $i \in I$, la
suite de $R$-modules
$$
\xymatrix{
L_i \ar[r]^{\varphi_i} &
M_i \ar[r]^{\psi_i} &
N_i
}
$$
soit un complexe d'homologie $H_i$.
Alors les $R$-modules $H_i$ forment un système sur $I$,
la suite de $R$-modules
$$
\xymatrix{
\colim_i L_i \ar[r]^\varphi &
\colim_i M_i \ar[r]^\psi &
\colim_i N_i
}
$$
est elle aussi un complexe et, en notant $H$ son homologie, nous avons
$$
H = \colim_i H_i.
$$
\end{lemma}

\begin{proof}
Il est clair que
$
\xymatrix{
\colim_i L_i \ar[r]^\varphi &
\colim_i M_i \ar[r]^\psi &
\colim_i N_i
}
$
est un complexe. Pour chaque $i \in I$, il existe un morphisme canonique de
$R$-modules $H_i \to H$ (qui envoie chaque
$[m] \in H_i = \Ker(\psi_i) / \Im(\varphi_i)$ sur la
classe dans $H = \Ker(\psi) / \Im(\varphi)$
de l'image de $m$ dans $\colim_i M_i$). Ces morphismes donnent lieu
à un morphisme $\colim_i H_i \to H$. Il reste à
montrer que ce morphisme est surjectif et injectif.

\medskip\noindent
Nous allons utiliser à plusieurs reprises, sans autre mention, la description des colimites sur $I$
donnée au Lemme \ref{lemma-directed-colimit}.
Soit $h \in H$.
Puisque $H = \Ker(\psi)/\Im(\varphi)$, on voit que
$h$ est la classe modulo $\Im(\varphi)$ d'un élément $[m]$
de $\Ker(\psi) \subset \colim_i M_i$. Choisissons un
$i$ tel que $[m]$ provienne d'un élément $m \in M_i$. Choisissons
$j \geq i$ tel que $\nu_{ij}(\psi_i(m)) = 0$, ce qui est possible
puisque $[m] \in \Ker(\psi)$. Après avoir remplacé $i$ par $j$ et
$m$ par $\mu_{ij}(m)$, nous voyons que nous pouvons supposer $m \in \Ker(\psi_i)$.
Cela montre que l'application $\colim_i H_i \to H$ est surjective.

\medskip\noindent
Supposons qu'un $h_i \in H_i$ ait une image nulle dans $H$. Puisque
$H_i = \Ker(\psi_i)/\Im(\varphi_i)$, nous pouvons représenter
$h_i$ par un élément $m \in \Ker(\psi_i) \subset M_i$.
L'hypothèse d'annulation de $h_i$ dans $H$ signifie que
la classe de $m$ dans $\colim_i M_i$ appartient à l'image
de $\varphi$. Il existe donc un $j \geq i$ et un $l \in L_j$
tels que $\varphi_j(l) = \mu_{ij}(m)$. Cela montre clairement que
l'image de $h_i$ dans $H_j$ est nulle. Ceci démontre
l'injectivité de $\colim_i H_i \to H$.
\end{proof}
```

</details>

### 10 — example-colimit-not-exact

Anglais L983-999 ; français L978-994.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L983) · `FR-ALGEBRA-B2-CHOICE-0010`.

Le système de cinq composantes et l'application terme à terme restent ceux de la source. L'injectivité de chaque composante n'implique pas celle des colimites pour la fourche non filtrante. Le contre-exemple est conservé en entier, sans changer les objets Z ni les flèches 0 et 1.

Règles : FR-ALGEBRA-B2-RULE-colimite, FR-ALGEBRA-B2-RULE-filtrant, FR-ALGEBRA-B2-RULE-exactitude.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-colimit-not-exact}
Taking colimits is not exact in general.
Consider the partially ordered set $I = \{a, b, c\}$ with
$a < b$ and $a < c$ and no other strict inequalities,
as in Example \ref{example-zero-colimit-different}.
Consider the map of systems
$(0, \mathbf{Z}, \mathbf{Z}, 0, 0) \to
(\mathbf{Z}, \mathbf{Z}, \mathbf{Z}, 1, 1)$.
From the description of the colimit in
Example \ref{example-zero-colimit-different}
we see that the associated map of colimits is not injective,
even though the map of systems is injective on each object.
Hence the result of Lemma \ref{lemma-directed-colimit-exact}
is false for general systems.
\end{example}
```

Français actuel :
```tex
\begin{example}
\label{example-colimit-not-exact}
La prise des colimites n'est pas exacte en général.
Considérons l'ensemble partiellement ordonné $I = \{a, b, c\}$ avec
$a < b$ et $a < c$, et aucune autre inégalité stricte,
comme dans l'Exemple \ref{example-zero-colimit-different}.
Considérons l'application de systèmes
$(0, \mathbf{Z}, \mathbf{Z}, 0, 0) \to
(\mathbf{Z}, \mathbf{Z}, \mathbf{Z}, 1, 1)$.
D'après la description de la colimite dans
l'Exemple \ref{example-zero-colimit-different},
nous voyons que l'application associée entre les colimites n'est pas injective,
bien que l'application de systèmes soit injective sur chaque objet.
Par conséquent, le résultat du Lemme \ref{lemma-directed-colimit-exact}
est faux pour les systèmes généraux.
\end{example}
```

</details>

### 11 — lemma-almost-directed-colimit-exact

Anglais L1000-1037 ; français L995-1032.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1000) · `FR-ALGEBRA-B2-CHOICE-0011`.

Les hypothèses restent données par le renvoi précis aux Catégories. La preuve décompose la catégorie d'indices en catégories filtrantes et garde J éventuellement vide, puis l'exactitude des sommes directes. Le passage de groupes abéliens à R-modules dans la preuve est déjà dans l'anglais : il est conservé, sans ajouter R=Z dans la traduction.

Point particulier à relire : R apparaît sans nouvelle déclaration après l'énoncé pour les groupes abéliens. Fidélité littérale, non certification de présentation parfaite.

Règles : FR-ALGEBRA-B2-RULE-colimite, FR-ALGEBRA-B2-RULE-filtrant, FR-ALGEBRA-B2-RULE-exactitude.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-almost-directed-colimit-exact}
Let $\mathcal{I}$ be an index category satisfying the assumptions of
Categories, Lemma \ref{categories-lemma-split-into-directed}.
Then taking colimits of diagrams of abelian groups over $\mathcal{I}$
is exact (i.e., the analogue of
Lemma \ref{lemma-directed-colimit-exact}
holds in this situation).
\end{lemma}

\begin{proof}
By
Categories, Lemma \ref{categories-lemma-split-into-directed}
we may write $\mathcal{I} = \coprod_{j \in J} \mathcal{I}_j$ with each
$\mathcal{I}_j$ a filtered category, and $J$ possibly empty. By
Categories, Lemma \ref{categories-lemma-directed-category-system}
taking colimits over the index categories $\mathcal{I}_j$ is
the same as taking the colimit over some directed set. Hence
Lemma \ref{lemma-directed-colimit-exact}
applies to these colimits. This reduces the problem to showing that
coproducts in the category of $R$-modules over the set $J$ are exact.
In other words, exact sequences
$L_j \to M_j \to N_j$ of $R$ modules we have to show that
$$
\bigoplus\nolimits_{j \in J} L_j
\longrightarrow
\bigoplus\nolimits_{j \in J} M_j
\longrightarrow
\bigoplus\nolimits_{j \in J} N_j
$$
is exact. This can be verified by hand, and holds even if $J$ is empty.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-almost-directed-colimit-exact}
Soit $\mathcal{I}$ une catégorie d'indices satisfaisant aux hypothèses de
Catégories, Lemme \ref{categories-lemma-split-into-directed}.
Alors la prise des colimites de diagrammes de groupes abéliens sur $\mathcal{I}$
est exacte (c'est-à-dire que l'analogue du
Lemme \ref{lemma-directed-colimit-exact}
vaut dans cette situation).
\end{lemma}

\begin{proof}
D'après
Catégories, Lemme \ref{categories-lemma-split-into-directed},
nous pouvons écrire $\mathcal{I} = \coprod_{j \in J} \mathcal{I}_j$, où chaque
$\mathcal{I}_j$ est une catégorie filtrante et où $J$ peut être vide. D'après
Catégories, Lemme \ref{categories-lemma-directed-category-system},
prendre les colimites sur les catégories d'indices $\mathcal{I}_j$ revient à
prendre la colimite sur un certain ensemble filtrant. Le
Lemme \ref{lemma-directed-colimit-exact}
s'applique donc à ces colimites. Le problème se ramène ainsi à montrer que
les coproduits dans la catégorie des $R$-modules indexés par l'ensemble $J$ sont exacts.
Autrement dit, étant données des suites exactes
$L_j \to M_j \to N_j$ de $R$-modules, nous devons montrer que
$$
\bigoplus\nolimits_{j \in J} L_j
\longrightarrow
\bigoplus\nolimits_{j \in J} M_j
\longrightarrow
\bigoplus\nolimits_{j \in J} N_j
$$
est exacte. Cela se vérifie directement et reste vrai même si $J$ est vide.
\end{proof}
```

</details>

### 12 — section-localization

Anglais L1038-1040 ; français L1033-1035.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1038) · `FR-ALGEBRA-B2-CHOICE-0012`.

Le titre Localisation reprend le registre de Ducros §2.1 ; il n'introduit pas la localisation des catégories, qui serait un autre objet.

Règles : FR-ALGEBRA-B2-RULE-localisation.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Localization}
\label{section-localization}
```

Français actuel :
```tex
\section{Localisation}
\label{section-localization}
```

</details>

### 13 — definition-multiplicative-subset

Anglais L1041-1066 ; français L1036-1061.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1041) · `FR-ALGEBRA-B2-CHOICE-0013`.

Partie multiplicative contient 1 et est stable par produit. Ducros 2.1.3.3 atteste précisément ces conditions ; 0 n'est pas exclu. La relation de fractions conserve le facteur u : ne pas remplacer par un produit en croix valable seulement sous des hypothèses supplémentaires. Addition et multiplication des anneaux sont conservées.

Règles : FR-ALGEBRA-B2-RULE-localisation.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-multiplicative-subset}
Let $R$ be a ring, $S$ a subset of $R$.
We say $S$ is a {\it multiplicative subset of $R$} if
$1\in S$ and $S$ is closed
under multiplication, i.e., $s, s' \in S \Rightarrow ss' \in S$.
\end{definition}

\noindent
Given a ring $A$ and a multiplicative subset $S$, we
define a relation on $A \times S$ as follows:
$$
(x, s) \sim (y, t)
\Leftrightarrow
\exists u \in S \text{ such that } (xt-ys)u = 0
$$
It is easily checked that this is an equivalence relation.
Let $x/s$ (or $\frac{x}{s}$) be the equivalence class of $(x, s)$ and
$S^{-1}A$ be the set of all equivalence classes. Define addition
and multiplication in $S^{-1}A$ as follows:
$$
x/s + y/t = (xt + ys)/st, \quad
x/s \cdot y/t = xy/st
$$
One can check that $S^{-1}A$ becomes a ring under these operations.
```

Français actuel :
```tex
\begin{definition}
\label{definition-multiplicative-subset}
Soit $R$ un anneau et soit $S$ un sous-ensemble de $R$.
Nous disons que $S$ est une {\it partie multiplicative de $R$} si
$1\in S$ et si $S$ est stable
par multiplication, c'est-à-dire si $s, s' \in S \Rightarrow ss' \in S$.
\end{definition}

\noindent
Étant donnés un anneau $A$ et une partie multiplicative $S$, nous
définissons une relation sur $A \times S$ comme suit :
$$
(x, s) \sim (y, t)
\Leftrightarrow
\exists u \in S \text{ tel que } (xt-ys)u = 0
$$
On vérifie aisément qu'il s'agit d'une relation d'équivalence.
Notons $x/s$ (ou $\frac{x}{s}$) la classe d'équivalence de $(x, s)$ et
$S^{-1}A$ l'ensemble de toutes les classes d'équivalence. Définissons l'addition
et la multiplication dans $S^{-1}A$ comme suit :
$$
x/s + y/t = (xt + ys)/st, \quad
x/s \cdot y/t = xy/st
$$
On vérifie que ces opérations font de $S^{-1}A$ un anneau.
```

</details>

### 14 — definition-localization

Anglais L1067-1082 ; français L1062-1077.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1067) · `FR-ALGEBRA-B2-CHOICE-0014`.

Localisation relativement à S est une variante de localisé par rapport à la partie multiplicative S chez Ducros p.71. Le morphisme canonique n'est pas supposé injectif. L'argument exige que S ne contienne aucun diviseur de zéro ; le français ne suppose ni intégrité ni non-nullité arbitraire de A.

Règles : FR-ALGEBRA-B2-RULE-localisation, FR-ALGEBRA-B2-RULE-universel, FR-ALGEBRA-B2-RULE-exactitude.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-localization}
This ring is called the {\it localization of $A$ with respect to $S$}.
\end{definition}

\noindent
We have a natural ring map from $A$ to its localization $S^{-1}A$,
$$
A \longrightarrow S^{-1}A, \quad x \longmapsto x/1
$$
which is sometimes called the {\it localization map}. In general the
localization map is not injective, unless $S$ contains no zerodivisors.
For, if $x/1 = 0$, then there is a $u\in S$ such that $xu = 0$ in $A$ and
hence $x = 0$ since there are no zerodivisors in $S$.
The localization of a ring has the following universal property.
```

Français actuel :
```tex
\begin{definition}
\label{definition-localization}
Cet anneau est appelé la {\it localisation de $A$ relativement à $S$}.
\end{definition}

\noindent
Il existe un morphisme naturel d'anneaux de $A$ vers sa localisation $S^{-1}A$,
$$
A \longrightarrow S^{-1}A, \quad x \longmapsto x/1
$$
parfois appelé le {\it morphisme de localisation}. En général, le
morphisme de localisation n'est pas injectif, à moins que $S$ ne contienne aucun diviseur de zéro.
En effet, si $x/1 = 0$, il existe un $u\in S$ tel que $xu = 0$ dans $A$, et
donc $x = 0$ puisqu'il n'y a pas de diviseur de zéro dans $S$.
La localisation d'un anneau possède la propriété universelle suivante.
```

</details>

### 15 — proposition-universal-property-localization

Anglais L1083-1109 ; français L1078-1104.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1083) · `FR-ALGEBRA-B2-CHOICE-0015`.

L'image de chaque élément de S doit être inversible, traduite par unité dans B. La propriété universelle affirme existence et unicité de g ; les deux preuves, la formule f(x)f(s)^-1 et le diagramme restent inchangés. Ducros 2.1.2-3 fournit le même registre, sans imposer sa construction par polynômes à cette preuve.

Règles : FR-ALGEBRA-B2-RULE-universel.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{proposition}
\label{proposition-universal-property-localization}
Let $f : A \to B$ be a ring map that sends every element in $S$ to a unit
of $B$. Then there is a unique homomorphism $g : S^{-1}A \to B$ such
that the following diagram commutes.
$$
\xymatrix{
A \ar[rr]^{f} \ar[dr] & & B \\
& S^{-1}A \ar[ur]_g
}
$$
\end{proposition}

\begin{proof}
Existence. We define a map $g$ as follows. For $x/s\in S^{-1}A$, let
$g(x/s) = f(x)f(s)^{-1}\in B$. It is easily checked from the definition
that this is a well-defined ring map. And it is also clear that
this makes the diagram commutative.

\medskip\noindent
Uniqueness. We now show that if $g' : S^{-1}A \to B$
satisfies $g'(x/1) = f(x)$, then $g = g'$. Hence $f(s) = g'(s/1)$ for
$s \in S$ by the commutativity of the diagram. But then $g'(1/s)f(s) = 1$
in $B$, which implies that $g'(1/s) = f(s)^{-1}$ and hence
$g'(x/s) = g'(x/1)g'(1/s) = f(x)f(s)^{-1} = g(x/s)$.
\end{proof}
```

Français actuel :
```tex
\begin{proposition}
\label{proposition-universal-property-localization}
Soit $f : A \to B$ un morphisme d'anneaux qui envoie chaque élément de $S$ sur une unité
de $B$. Il existe alors un unique homomorphisme $g : S^{-1}A \to B$ tel
que le diagramme suivant soit commutatif.
$$
\xymatrix{
A \ar[rr]^{f} \ar[dr] & & B \\
& S^{-1}A \ar[ur]_g
}
$$
\end{proposition}

\begin{proof}
Existence. Définissons une application $g$ comme suit. Pour $x/s\in S^{-1}A$, posons
$g(x/s) = f(x)f(s)^{-1}\in B$. La définition permet de vérifier aisément
qu'il s'agit d'un morphisme d'anneaux bien défini. Il est également clair que
ce morphisme rend le diagramme commutatif.

\medskip\noindent
Unicité. Montrons maintenant que, si $g' : S^{-1}A \to B$
satisfait $g'(x/1) = f(x)$, alors $g = g'$. La commutativité du diagramme donne donc $f(s) = g'(s/1)$ pour
$s \in S$. Mais alors $g'(1/s)f(s) = 1$
dans $B$, ce qui implique $g'(1/s) = f(s)^{-1}$, puis
$g'(x/s) = g'(x/1)g'(1/s) = f(x)f(s)^{-1} = g(x/s)$.
\end{proof}
```

</details>

### 16 — lemma-localization-zero

Anglais L1110-1119 ; français L1105-1114.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1110) · `FR-ALGEBRA-B2-CHOICE-0016`.

Le critère est exactement 0 appartient à S. La preuve compare les classes de fractions ; elle ne présuppose pas A intègre. Ducros 2.1.4.3 confirme cet usage. L'ellipse toute paire dans la première phrase conserve la formule source.

Règles : FR-ALGEBRA-B2-RULE-localisation.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-localization-zero}
The localization $S^{-1}A$ is the zero ring if and only if $0\in S$.
\end{lemma}

\begin{proof}
If $0\in S$, any pair $(a, s)\sim (0, 1)$ by definition.
If $0\not \in S$, then clearly $1/1 \neq 0/1$ in $S^{-1}A$.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-localization-zero}
La localisation $S^{-1}A$ est l'anneau nul si et seulement si $0\in S$.
\end{lemma}

\begin{proof}
Si $0\in S$, toute paire $(a, s)\sim (0, 1)$ par définition.
Si $0\not \in S$, alors il est clair que $1/1 \neq 0/1$ dans $S^{-1}A$.
\end{proof}
```

</details>

### 17 — lemma-localization-and-modules

Anglais L1120-1157 ; français L1115-1152.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1120) · `FR-ALGEBRA-B2-CHOICE-0017`.

L'équivalence concerne les modules sur le localisé et les R-modules où chaque s agit par un automorphisme. L'action x_N après s_N inverse garde son sens ; les quasi-inverses restent sans vérification détaillée. Le paragraphe suivant conserve aussi la formule source mn/st dans une construction de modules : son défaut de typage est signalé séparément, jamais réparé clandestinement.

Point particulier à relire : La formule m/s fois n/t = mn/st, avec m,n dans un module, n'est généralement pas définie. Anomalie anglaise reproduite ; une correction doit être un erratum séparé.

Règles : FR-ALGEBRA-B2-RULE-localisation, FR-ALGEBRA-B2-RULE-universel.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-localization-and-modules}
Let $R$ be a ring. Let $S \subset R$ be a multiplicative subset.
The category of $S^{-1}R$-modules is equivalent to the category
of $R$-modules $N$ with the property that every $s \in S$ acts as
an automorphism on $N$.
\end{lemma}

\begin{proof}
The functor which defines the equivalence associates to an $S^{-1}R$-module
$M$ the same module but now viewed as an $R$-module via the localization
map $R \to S^{-1}R$. Conversely, if $N$ is an $R$-module, such that every
$s \in S$ acts via an automorphism $s_N$, then we can think of $N$ as an
$S^{-1}R$-module by letting $x/s$ act via $x_N  \circ s_N^{-1}$.
We omit the verification that these two functors are quasi-inverse to
each other.
\end{proof}

\noindent
The notion of localization of a ring can be generalized to the
localization of a module. Let $A$ be a ring, $S$ a multiplicative
subset of $A$ and $M$ an $A$-module. We define a relation on
$M \times S$ as follows
$$
(m, s) \sim (n, t)
\Leftrightarrow
\exists u\in S \text{ such that } (mt-ns)u = 0
$$
This is clearly an equivalence relation. Denote by $m/s$ (or
$\frac{m}{s}$) be the equivalence class of $(m, s)$ and $S^{-1}M$ be
the set of all equivalence classes. Define the addition and scalar
multiplication as follows
$$
m/s + n/t = (mt + ns)/st,\quad
m/s\cdot n/t = mn/st
$$
It is clear that this makes $S^{-1}M$ an $S^{-1}A$-module.
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-localization-and-modules}
Soit $R$ un anneau. Soit $S \subset R$ une partie multiplicative.
La catégorie des $S^{-1}R$-modules est équivalente à la catégorie
des $R$-modules $N$ ayant la propriété que tout $s \in S$ agit sur
$N$ par un automorphisme.
\end{lemma}

\begin{proof}
Le foncteur qui définit l'équivalence associe à un $S^{-1}R$-module
$M$ le même module, considéré maintenant comme un $R$-module au moyen du morphisme de localisation
$R \to S^{-1}R$. Réciproquement, si $N$ est un $R$-module tel que tout
$s \in S$ agisse par un automorphisme $s_N$, nous pouvons considérer $N$ comme un
$S^{-1}R$-module en faisant agir $x/s$ par $x_N  \circ s_N^{-1}$.
Nous omettons de vérifier que ces deux foncteurs sont quasi-inverses l'un de
l'autre.
\end{proof}

\noindent
La notion de localisation d'un anneau se généralise à la
localisation d'un module. Soient $A$ un anneau, $S$ une partie multiplicative
de $A$ et $M$ un $A$-module. Nous définissons une relation sur
$M \times S$ comme suit :
$$
(m, s) \sim (n, t)
\Leftrightarrow
\exists u\in S \text{ tel que } (mt-ns)u = 0
$$
Il s'agit clairement d'une relation d'équivalence. Notons $m/s$ (ou
$\frac{m}{s}$) la classe d'équivalence de $(m, s)$ et $S^{-1}M$
l'ensemble de toutes les classes d'équivalence. Définissons l'addition et la multiplication
scalaire comme suit :
$$
m/s + n/t = (mt + ns)/st,\quad
m/s\cdot n/t = mn/st
$$
Il est clair que cela fait de $S^{-1}M$ un $S^{-1}A$-module.
```

</details>

### 18 — definition-localization-module

Anglais L1158-1169 ; français L1153-1164.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1158) · `FR-ALGEBRA-B2-CHOICE-0018`.

La localisation du module et son application m vers m/1 sont conservées. Ce n'est pas en général une inclusion : le français ne transforme pas le morphisme en plongement.

Règles : FR-ALGEBRA-B2-RULE-localisation, FR-ALGEBRA-B2-RULE-universel.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-localization-module}
The $S^{-1}A$-module $S^{-1}M$ is called the {\it localization} of $M$
with respect to $S$.
\end{definition}

\noindent
Note that there is an $A$-module map $M \to S^{-1}M$, $m \mapsto m/1$
which is sometimes
called the {\it localization map}. It satisfies the following universal
property.
```

Français actuel :
```tex
\begin{definition}
\label{definition-localization-module}
Le $S^{-1}A$-module $S^{-1}M$ est appelé la {\it localisation} de $M$
relativement à $S$.
\end{definition}

\noindent
Remarquons qu'il existe un homomorphisme de $A$-modules $M \to S^{-1}M$, $m \mapsto m/1$,
parfois
appelé le {\it morphisme de localisation}. Il satisfait la propriété
universelle suivante.
```

</details>

### 19 — lemma-universal-property-localization-module

Anglais L1170-1212 ; français L1165-1206.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1170) · `FR-ALGEBRA-B2-CHOICE-0019`.

Tous les éléments de S agissent par automorphismes sur N. L'isomorphisme Hom et la précomposition sont inchangés. s inverse dans la preuve désigne l'automorphisme inverse sur N, non un élément supposé déjà dans R. Prolongée garde les guillemets source. Le masculin déterminé peut renvoyer à l'homomorphisme alpha ; il n'est pas une erreur de sens à remplacer mécaniquement. Le calcul complet de linéarité est conservé.

Règles : FR-ALGEBRA-B2-RULE-localisation, FR-ALGEBRA-B2-RULE-exactitude, FR-ALGEBRA-B2-RULE-quotients.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-universal-property-localization-module}
Let $R$ be a ring. Let $S \subset R$ a multiplicative subset. Let $M$, $N$
be $R$-modules. Assume all the elements of $S$ act as automorphisms on $N$.
Then the canonical map
$$
\Hom_R(S^{-1}M, N) \longrightarrow \Hom_R(M, N)
$$
induced by the localization map, is an isomorphism.
\end{lemma}

\begin{proof}
It is clear that the map is well-defined and $R$-linear.
Injectivity: Let $\alpha \in \Hom_R(S^{-1}M, N)$ and take an arbitrary
element $m/s \in S^{-1}M$. Then, since $s \cdot \alpha(m/s) = \alpha(m/1)$,
we have $ \alpha(m/s) =s^{-1}(\alpha (m/1))$, so $\alpha$ is completely
determined by what it does on the image of $M$ in $S^{-1}M$.
Surjectivity: Let $\beta : M \rightarrow N$ be a given R-linear map.
We need to show that it can be "extended" to $S^{-1}M$. Define a map of
sets
$$
M \times S \rightarrow N,\quad
(m,s) \mapsto s^{-1}\beta(m)
$$
Clearly, this map respects the equivalence relation from above, so it
descends to a well-defined map $\alpha : S^{-1}M \rightarrow N$.
It remains to show that this map is $R$-linear, so take
$r, r' \in R$ as well as $s, s' \in S$ and
$m, m' \in M$. Then
\begin{align*}
\alpha(r \cdot m/s + r' \cdot m' /s')
& =
\alpha((r \cdot s' \cdot m + r' \cdot s \cdot m') /(ss')) \\
& =
(ss')^{-1}\beta(r \cdot s' \cdot m + r' \cdot s \cdot m') \\
& =
(ss')^{-1} (r \cdot s' \beta (m) + r' \cdot s \beta (m')) \\
& =
r \alpha (m/s) + r' \alpha (m' /s')
\end{align*}
and we win.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-universal-property-localization-module}
Soit $R$ un anneau. Soit $S \subset R$ une partie multiplicative. Soient $M$, $N$
des $R$-modules. Supposons que tous les éléments de $S$ agissent sur $N$ par des automorphismes.
Alors l'application canonique
$$
\Hom_R(S^{-1}M, N) \longrightarrow \Hom_R(M, N)
$$
induite par le morphisme de localisation est un isomorphisme.
\end{lemma}

\begin{proof}
Il est clair que l'application est bien définie et $R$-linéaire.
Injectivité : soit $\alpha \in \Hom_R(S^{-1}M, N)$ et prenons un
élément arbitraire $m/s \in S^{-1}M$. Puisque $s \cdot \alpha(m/s) = \alpha(m/1)$,
nous avons $ \alpha(m/s) =s^{-1}(\alpha (m/1))$ ; ainsi, $\alpha$ est entièrement
déterminé par ses valeurs sur l'image de $M$ dans $S^{-1}M$.
Surjectivité : soit $\beta : M \rightarrow N$ une application R-linéaire donnée.
Nous devons montrer qu'elle peut être ``prolongée'' à $S^{-1}M$. Définissons une application d'ensembles
$$
M \times S \rightarrow N,\quad
(m,s) \mapsto s^{-1}\beta(m)
$$
Cette application respecte clairement la relation d'équivalence ci-dessus ; elle
passe donc au quotient en une application bien définie $\alpha : S^{-1}M \rightarrow N$.
Il reste à montrer que cette application est $R$-linéaire ; prenons donc
$r, r' \in R$, ainsi que $s, s' \in S$ et
$m, m' \in M$. Alors
\begin{align*}
\alpha(r \cdot m/s + r' \cdot m' /s')
& =
\alpha((r \cdot s' \cdot m + r' \cdot s \cdot m') /(ss')) \\
& =
(ss')^{-1}\beta(r \cdot s' \cdot m + r' \cdot s \cdot m') \\
& =
(ss')^{-1} (r \cdot s' \beta (m) + r' \cdot s \beta (m')) \\
& =
r \alpha (m/s) + r' \alpha (m' /s')
\end{align*}
ce qui conclut.
\end{proof}
```

</details>

### 20 — example-localize-at-prime

Anglais L1213-1241 ; français L1207-1235.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1213) · `FR-ALGEBRA-B2-CHOICE-0020`.

Localisation en un idéal premier, en un élément, anneau total et corps des fractions restent quatre cas distincts. La nilpotence de f caractérise A_f nul. Le troisième cas ne suppose pas A intègre ; seul le quatrième le suppose. Ducros 2.1.5 atteste corps des fractions et localisation en f. Anneau total des quotients / des fractions est conservé selon sa définition explicite ; aucune attestation exacte de ces deux syntagmes n'est revendiquée dans les pages consultées.

Point particulier à relire : Attestation exacte des deux noms de l'anneau total non acquise ici ; aucune assurance lexicale exhaustive n'est inventée.

Règles : FR-ALGEBRA-B2-RULE-localisation, FR-ALGEBRA-B2-RULE-quotients.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-localize-at-prime}
Let $A$ be a ring and let $M$ be an $A$-module.
Here are some important examples of localizations.
\begin{enumerate}
\item Given $\mathfrak p$ a prime ideal of $A$ consider
$S = A\setminus\mathfrak p$. It is
immediately checked that $S$ is a multiplicative set. In this case
we denote $A_\mathfrak p$ and $M_\mathfrak p$ the localization of
$A$ and $M$ with respect to $S$ respectively. These are
called the {\it localization of $A$, resp.\ $M$ at $\mathfrak p$}.
\item Let $f\in A$. Consider $S = \{1, f, f^2, \ldots\}$.
This is clearly a multiplicative subset of $A$.
In this case we denote $A_f$
(resp. $M_f$) the localization $S^{-1}A$ (resp. $S^{-1}M$).
This is called the {\it localization of $A$, resp.\ $M$ with
respect to $f$}.
Note that $A_f = 0$ if and only if $f$ is nilpotent in $A$.
\item Let $S = \{f \in A \mid f \text{ is not a zerodivisor in }A\}$.
This is a multiplicative subset of $A$. In this case the
ring $Q(A) = S^{-1}A$ is called either the
{\it total quotient ring}, or the {\it total ring of fractions}
of $A$.
\item If $A$ is a domain, then the total quotient ring $Q(A)$ is
the field of fractions of $A$. Please see
Fields, Example \ref{fields-example-quotient-field}.
\end{enumerate}
\end{example}
```

Français actuel :
```tex
\begin{example}
\label{example-localize-at-prime}
Soit $A$ un anneau et soit $M$ un $A$-module.
Voici quelques exemples importants de localisations.
\begin{enumerate}
\item Étant donné un idéal premier $\mathfrak p$ de $A$, considérons
$S = A\setminus\mathfrak p$. On vérifie
immédiatement que $S$ est une partie multiplicative. Dans ce cas,
nous notons $A_\mathfrak p$ et $M_\mathfrak p$ les localisations de
$A$ et de $M$ relativement à $S$, respectivement. Elles sont
appelées la {\it localisation de $A$, resp.\ de $M$, en $\mathfrak p$}.
\item Soit $f\in A$. Considérons $S = \{1, f, f^2, \ldots\}$.
C'est clairement une partie multiplicative de $A$.
Dans ce cas, nous notons $A_f$
(resp. $M_f$) la localisation $S^{-1}A$ (resp. $S^{-1}M$).
Elle est appelée la {\it localisation de $A$, resp.\ de $M$, relativement
à $f$}.
Remarquons que $A_f = 0$ si et seulement si $f$ est nilpotent dans $A$.
\item Soit $S = \{f \in A \mid f \text{ n'est pas un diviseur de zéro dans }A\}$.
C'est une partie multiplicative de $A$. Dans ce cas, l'anneau
$Q(A) = S^{-1}A$ est appelé soit l'{\it anneau total des quotients},
soit l'{\it anneau total des fractions}
de $A$.
\item Si $A$ est un anneau intègre, alors l'anneau total des quotients $Q(A)$ est
le corps des fractions de $A$. Voir
Corps, Exemple \ref{fields-example-quotient-field}.
\end{enumerate}
\end{example}
```

</details>

### 21 — lemma-localization-colimit

Anglais L1242-1274 ; français L1236-1268.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1242) · `FR-ALGEBRA-B2-CHOICE-0021`.

Le préordre utilise un facteur f'' dans R et non nécessairement dans S. La flèche M_f' vers M_f et ses puissances sont identiques. La preuve reste une indication, non une nouvelle démonstration. Les conventions A, M, N et le produit SS' du paragraphe suivant sont conservés.

Règles : FR-ALGEBRA-B2-RULE-localisation, FR-ALGEBRA-B2-RULE-universel.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-localization-colimit}
Let $R$ be a ring.
Let $S \subset R$ be a multiplicative subset.
Let $M$ be an $R$-module.
Then
$$
S^{-1}M = \colim_{f \in S} M_f
$$
where the preorder on $S$ is given by
$f \geq f' \Leftrightarrow f = f'f''$ for some $f'' \in R$
in which case the map $M_{f'} \to M_f$ is given
by $m/(f')^e \mapsto m(f'')^e/f^e$.
\end{lemma}

\begin{proof}
Omitted. Hint: Use the universal property of
Lemma \ref{lemma-universal-property-localization-module}.
\end{proof}

\noindent
In the following paragraph,
let $A$ denote a ring,
and $M, N$ denote modules over $A$.

\medskip\noindent
If $S$ and $S'$ are multiplicative sets of $A$, then it is
clear that
$$
SS' = \{ss' : s\in S, \ s'\in S'\}
$$
is also a multiplicative set of $A$. Then the following holds.
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-localization-colimit}
Soit $R$ un anneau.
Soit $S \subset R$ une partie multiplicative.
Soit $M$ un $R$-module.
Alors
$$
S^{-1}M = \colim_{f \in S} M_f
$$
où le préordre sur $S$ est donné par
$f \geq f' \Leftrightarrow f = f'f''$ pour un certain $f'' \in R$,
auquel cas l'application $M_{f'} \to M_f$ est donnée
par $m/(f')^e \mapsto m(f'')^e/f^e$.
\end{lemma}

\begin{proof}
Démonstration omise. Indication : utiliser la propriété universelle du
Lemme \ref{lemma-universal-property-localization-module}.
\end{proof}

\noindent
Dans le paragraphe suivant,
$A$ désigne un anneau,
et $M, N$ désignent des modules sur $A$.

\medskip\noindent
Si $S$ et $S'$ sont des parties multiplicatives de $A$, il est alors
clair que
$$
SS' = \{ss' : s\in S, \ s'\in S'\}
$$
est également une partie multiplicative de $A$. On a alors le résultat suivant.
```

</details>

### 22 — proposition-localize-twice

Anglais L1275-1300 ; français L1269-1294.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1275) · `FR-ALGEBRA-B2-CHOICE-0022`.

L'image S barre vit dans S' inverse A. Les deux applications construites par propriété universelle sont inverses et conservent l'ordre des deux localisations. Aucun remplacement des ensembles de dénominateurs n'est effectué.

Règles : FR-ALGEBRA-B2-RULE-universel.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{proposition}
\label{proposition-localize-twice}
Let $\overline{S}$ be the image of $S$ in $S'^{-1}A$, then
$(SS')^{-1}A$ is isomorphic to $\overline{S}^{-1}(S'^{-1}A)$.
\end{proposition}

\begin{proof}
The map sending $x\in A$ to $x/1\in (SS')^{-1}A$ induces a map
sending $x/s\in S'^{-1}A$ to $x/s \in (SS')^{-1}A$, by universal
property. The image of the elements in $\overline{S}$ are invertible
in $(SS')^{-1}A$. By the universal property we get a map
$f : \overline{S}^{-1}(S'^{-1}A) \to (SS')^{-1}A$ which maps
$(x/s')/(s/1)$ to $x/ss'$.

\medskip\noindent
On the other hand, the map from $A$ to $\overline{S}^{-1}(S'^{-1}A)$
sending $x\in A$ to $(x/1)/(1/1)$ also induces a map
$g : (SS')^{-1}A \to \overline{S}^{-1}(S'^{-1}A)$ which sends $x/ss'$
to $(x/s')/(s/1)$, by the universal property again. It is
immediately checked that $f$ and $g$ are inverse to each other,
hence they are both isomorphisms.
\end{proof}

\noindent
For the module $M$ we have
```

Français actuel :
```tex
\begin{proposition}
\label{proposition-localize-twice}
Soit $\overline{S}$ l'image de $S$ dans $S'^{-1}A$ ; alors
$(SS')^{-1}A$ est isomorphe à $\overline{S}^{-1}(S'^{-1}A)$.
\end{proposition}

\begin{proof}
L'application qui envoie $x\in A$ sur $x/1\in (SS')^{-1}A$ induit, par propriété
universelle, une application qui envoie $x/s\in S'^{-1}A$ sur $x/s \in (SS')^{-1}A$.
Les images des éléments de $\overline{S}$ sont inversibles
dans $(SS')^{-1}A$. La propriété universelle fournit une application
$f : \overline{S}^{-1}(S'^{-1}A) \to (SS')^{-1}A$ qui envoie
$(x/s')/(s/1)$ sur $x/ss'$.

\medskip\noindent
D'autre part, l'application de $A$ vers $\overline{S}^{-1}(S'^{-1}A)$
qui envoie $x\in A$ sur $(x/1)/(1/1)$ induit elle aussi, par la propriété universelle,
une application $g : (SS')^{-1}A \to \overline{S}^{-1}(S'^{-1}A)$ qui envoie $x/ss'$
sur $(x/s')/(s/1)$. On vérifie
immédiatement que $f$ et $g$ sont inverses l'un de l'autre ;
ce sont donc tous deux des isomorphismes.
\end{proof}

\noindent
Pour le module $M$, nous avons
```

</details>

### 23 — proposition-localize-twice-module

Anglais L1301-1334 ; français L1295-1328.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1301) · `FR-ALGEBRA-B2-CHOICE-0023`.

Le module localisé d'abord en S' est regardé comme A-module. La source affirme qu'aucune propriété universelle n'a été démontrée, malgré le lemme précédent : cette discordance narrative reste littérale. Les deux applications explicites, l'indépendance des représentants et la fonctorialité gardent leur portée. Pour certains porte sur s et s', et et traduit and sans nouvelle hypothèse.

Point particulier à relire : L'affirmation sur l'absence de propriété universelle contredit le voisinage du texte officiel. Ne pas la corriger dans la traduction de référence.

Règles : FR-ALGEBRA-B2-RULE-localisation, FR-ALGEBRA-B2-RULE-universel, FR-ALGEBRA-B2-RULE-exactitude, FR-ALGEBRA-B2-RULE-hom-variance.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{proposition}
\label{proposition-localize-twice-module}
View $S'^{-1}M$ as an $A$-module, then $S^{-1}(S'^{-1}M)$ is
isomorphic to $(SS')^{-1}M$.
\end{proposition}

\begin{proof}
Note that given a $A$-module M, we have not proved any
universal property for $S^{-1}M$. Hence we cannot reason
as in the preceding proof; we have to construct the isomorphism explicitly.

\medskip\noindent
We define the maps as follows
\begin{align*}
& f : S^{-1}(S'^{-1}M) \longrightarrow (SS')^{-1}M, \quad \frac{x/s'}{s}\mapsto
x/ss'\\
& g : (SS')^{-1}M \longrightarrow S^{-1}(S'^{-1}M), \quad x/t\mapsto
\frac{x/s'}{s}\ \text{for some }s\in S, s'\in S', \text{ and }
t = ss'
\end{align*}
We have to check that these homomorphisms are well-defined, that is,
independent the choice of the fraction. This is easily checked and it is also
straightforward to show that they are inverse to each other.
\end{proof}

\noindent
If $u : M \to N$ is an $A$ homomorphism, then the localization indeed
induces a well-defined $S^{-1}A$ homomorphism $S^{-1}u : S^{-1}M \to
S^{-1}N$ which sends $x/s$ to $u(x)/s$. It is immediately checked that
this construction is functorial, so that $S^{-1}$
is actually a functor from the category of $A$-modules to the
category of $S^{-1}A$-modules. Moreover this functor is exact,
as we show in the following proposition.
```

Français actuel :
```tex
\begin{proposition}
\label{proposition-localize-twice-module}
Considérons $S'^{-1}M$ comme un $A$-module ; alors $S^{-1}(S'^{-1}M)$ est
isomorphe à $(SS')^{-1}M$.
\end{proposition}

\begin{proof}
Remarquons qu'étant donné un $A$-module M, nous n'avons démontré aucune
propriété universelle pour $S^{-1}M$. Nous ne pouvons donc pas raisonner
comme dans la démonstration précédente ; nous devons construire explicitement l'isomorphisme.

\medskip\noindent
Définissons les applications comme suit :
\begin{align*}
& f : S^{-1}(S'^{-1}M) \longrightarrow (SS')^{-1}M, \quad \frac{x/s'}{s}\mapsto
x/ss'\\
& g : (SS')^{-1}M \longrightarrow S^{-1}(S'^{-1}M), \quad x/t\mapsto
\frac{x/s'}{s}\ \text{pour certains }s\in S, s'\in S', \text{ et }
t = ss'
\end{align*}
Nous devons vérifier que ces homomorphismes sont bien définis, c'est-à-dire
indépendants du choix de la fraction. Cela se vérifie aisément et il est également
immédiat qu'ils sont inverses l'un de l'autre.
\end{proof}

\noindent
Si $u : M \to N$ est un homomorphisme de $A$-modules, la localisation
induit bien un homomorphisme de $S^{-1}A$-modules $S^{-1}u : S^{-1}M \to
S^{-1}N$ qui envoie $x/s$ sur $u(x)/s$. On vérifie immédiatement que
cette construction est fonctorielle, si bien que $S^{-1}$
est effectivement un foncteur de la catégorie des $A$-modules vers la
catégorie des $S^{-1}A$-modules. De plus, ce foncteur est exact,
comme le montre la proposition suivante.
```

</details>

### 24 — proposition-localization-exact

Anglais L1335-1354 ; français L1329-1348.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1335) · `FR-ALGEBRA-B2-CHOICE-0024`.

La suite à trois termes n'est pas déclarée courte ; aucun zéro n'est ajouté. La preuve transforme v(x)/s nul en v(xt)=0 puis x/s en l'image de y/st. Le foncteur et les anneaux de scalaires sont ceux de la source.

Règles : FR-ALGEBRA-B2-RULE-localisation, FR-ALGEBRA-B2-RULE-exactitude.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{proposition}
\label{proposition-localization-exact}
\begin{slogan}
Localization is exact.
\end{slogan}
Let $L\xrightarrow{u} M\xrightarrow{v} N$ be an exact sequence
of $R$-modules. Then
$S^{-1}L \to S^{-1}M \to S^{-1}N$ is also exact.
\end{proposition}

\begin{proof}
First it is clear that $S^{-1}L \to S^{-1}M \to S^{-1}N$ is a complex
since localization is a functor. Next suppose that $x/s$ maps to zero
in $S^{-1}N$ for some $x/s \in S^{-1}M$. Then by definition there is a
$t\in S$ such that $v(xt) = v(x)t = 0$ in $N$, which means
$xt \in \Ker(v)$. By the exactness of $L \to M \to N$ we have
$xt = u(y)$ for some $y$ in $L$. Then $x/s$ is the image of $y/st$.
This proves the exactness.
\end{proof}
```

Français actuel :
```tex
\begin{proposition}
\label{proposition-localization-exact}
\begin{slogan}
La localisation est exacte.
\end{slogan}
Soit $L\xrightarrow{u} M\xrightarrow{v} N$ une suite exacte
de $R$-modules. Alors
$S^{-1}L \to S^{-1}M \to S^{-1}N$ est également exacte.
\end{proposition}

\begin{proof}
Tout d'abord, il est clair que $S^{-1}L \to S^{-1}M \to S^{-1}N$ est un complexe,
puisque la localisation est un foncteur. Supposons ensuite que $x/s$ s'envoie sur zéro
dans $S^{-1}N$ pour un certain $x/s \in S^{-1}M$. Il existe alors, par définition, un
$t\in S$ tel que $v(xt) = v(x)t = 0$ dans $N$, ce qui signifie que
$xt \in \Ker(v)$. Par l'exactitude de $L \to M \to N$, nous avons
$xt = u(y)$ pour un certain $y$ dans $L$. Ainsi, $x/s$ est l'image de $y/st$.
Cela démontre l'exactitude.
\end{proof}
```

</details>

### 25 — lemma-localize-quotient-modules

Anglais L1355-1378 ; français L1349-1372.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1355) · `FR-ALGEBRA-B2-CHOICE-0025`.

L'isomorphisme entre le localisé d'un quotient et le quotient des localisés est inchangé, ainsi que la suite exacte courte de preuve. Deux désignations sont rétablies : corollaire au lieu d'énoncé ou lemme. L'environnement technique reste lemma comme dans l'anglais. Cette fidélité de dénomination n'est pas l'affirmation de deux erreurs mathématiques.

Point particulier à relire : Deux retours au mot corollaire malgré l'environnement lemma : incohérence de source conservée et visible ici.

Règles : FR-ALGEBRA-B2-RULE-localisation, FR-ALGEBRA-B2-RULE-exactitude, FR-ALGEBRA-B2-RULE-quotients.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-localize-quotient-modules}
Localization respects quotients, i.e. if $N$ is a submodule of
$M$, then $S^{-1}(M/N)\simeq (S^{-1}M)/(S^{-1}N)$.
\end{lemma}

\begin{proof}
From the exact sequence
$$
0 \longrightarrow N \longrightarrow M \longrightarrow M/N \longrightarrow 0
$$
we have
$$
0 \longrightarrow S^{-1}N \longrightarrow S^{-1}M
\longrightarrow S^{-1}(M/N) \longrightarrow 0
$$
The corollary then follows.
\end{proof}

\noindent
If, in the preceding Corollary, we take $N = I$ and $M = A$ for an ideal $I$ of
$A$, we see that $S^{-1}A/S^{-1}I \simeq S^{-1}(A/I)$ as $A$-modules. The next
proposition shows that they are isomorphic as rings.
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-localize-quotient-modules}
La localisation respecte les quotients : si $N$ est un sous-module de
$M$, alors $S^{-1}(M/N)\simeq (S^{-1}M)/(S^{-1}N)$.
\end{lemma}

\begin{proof}
La suite exacte
$$
0 \longrightarrow N \longrightarrow M \longrightarrow M/N \longrightarrow 0
$$
donne
$$
0 \longrightarrow S^{-1}N \longrightarrow S^{-1}M
\longrightarrow S^{-1}(M/N) \longrightarrow 0
$$
Le corollaire en résulte.
\end{proof}

\noindent
Si, dans le corollaire précédent, nous prenons $N = I$ et $M = A$ pour un idéal $I$ de
$A$, nous voyons que $S^{-1}A/S^{-1}I \simeq S^{-1}(A/I)$ comme $A$-modules. La
proposition suivante montre qu'ils sont isomorphes comme anneaux.
```

</details>

### 26 — proposition-localize-quotient

Anglais L1379-1419 ; français L1373-1413.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1379) · `FR-ALGEBRA-B2-CHOICE-0026`.

L'image S barre dans A/I est conservée. Les fractions, les deux passages au quotient et les morphismes inverses f barre et g sont identiques. Isomorphe comme anneau est plus précis que le seul isomorphisme de modules précédent ; aucune structure n'est oubliée.

Règles : FR-ALGEBRA-B2-RULE-localisation, FR-ALGEBRA-B2-RULE-universel, FR-ALGEBRA-B2-RULE-exactitude, FR-ALGEBRA-B2-RULE-quotients.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{proposition}
\label{proposition-localize-quotient}
Let $I$ be an ideal of $A$, $S$ a multiplicative set of $A$. Then
$S^{-1}I$ is an ideal of $S^{-1}A$ and $\overline{S}^{-1}(A/I)$ is
isomorphic to $S^{-1}A/S^{-1}I$, where $\overline{S}$ is
the image of $S$ in $A/I$.
\end{proposition}

\begin{proof}
The fact that $S^{-1}I$ is an ideal is clear since $I$ itself is an
ideal. Define
$$
f : S^{-1}A\longrightarrow \overline{S}^{-1}(A/I), \quad x/s\mapsto
\overline{x}/\overline{s}
$$
where $\overline{x}$ and $\overline{s}$ are the images of $x$ and
$s$ in $A/I$. We shall keep similar notations in this proof.
This map is well-defined by the universal property of
$S^{-1}A$, and $S^{-1}I$ is contained in the kernel of it,
therefore it induces a map
$$
\overline{f} : S^{-1}A/S^{-1}I \longrightarrow \overline{S}^{-1}(A/I), \quad
\overline{x/s}\mapsto \overline{x}/\overline{s}
$$

\medskip\noindent
On the other hand, the map $A \to S^{-1}A/S^{-1}I$ sending $x$ to
$\overline{x/1}$ induces a map $A/I \to S^{-1}A/S^{-1}I$ sending
$\overline{x}$ to $\overline{x/1}$. The image of $\overline{S}$ is
invertible in $S^{-1}A/S^{-1}I$, thus induces a map
$$
g : \overline{S}^{-1}(A/I) \longrightarrow S^{-1}A/S^{-1}I, \quad
\frac{\overline{x}}{\overline{s}}\mapsto \overline{x/s}
$$
by the universal property. It is then clear that $\overline{f}$ and $g$
are inverse to each other, hence are both isomorphisms.
\end{proof}

\noindent
We now consider how submodules behave in localization.
```

Français actuel :
```tex
\begin{proposition}
\label{proposition-localize-quotient}
Soient $I$ un idéal de $A$ et $S$ une partie multiplicative de $A$. Alors
$S^{-1}I$ est un idéal de $S^{-1}A$ et $\overline{S}^{-1}(A/I)$ est
isomorphe à $S^{-1}A/S^{-1}I$, où $\overline{S}$ est
l'image de $S$ dans $A/I$.
\end{proposition}

\begin{proof}
Le fait que $S^{-1}I$ soit un idéal est clair puisque $I$ est lui-même un
idéal. Définissons
$$
f : S^{-1}A\longrightarrow \overline{S}^{-1}(A/I), \quad x/s\mapsto
\overline{x}/\overline{s}
$$
où $\overline{x}$ et $\overline{s}$ sont les images de $x$ et de
$s$ dans $A/I$. Nous conserverons des notations semblables dans cette démonstration.
Cette application est bien définie par la propriété universelle de
$S^{-1}A$, et $S^{-1}I$ est contenu dans son noyau ;
elle induit donc une application
$$
\overline{f} : S^{-1}A/S^{-1}I \longrightarrow \overline{S}^{-1}(A/I), \quad
\overline{x/s}\mapsto \overline{x}/\overline{s}
$$

\medskip\noindent
D'autre part, l'application $A \to S^{-1}A/S^{-1}I$ qui envoie $x$ sur
$\overline{x/1}$ induit une application $A/I \to S^{-1}A/S^{-1}I$ qui envoie
$\overline{x}$ sur $\overline{x/1}$. L'image de $\overline{S}$ est
inversible dans $S^{-1}A/S^{-1}I$ ; elle induit donc une application
$$
g : \overline{S}^{-1}(A/I) \longrightarrow S^{-1}A/S^{-1}I, \quad
\frac{\overline{x}}{\overline{s}}\mapsto \overline{x/s}
$$
par la propriété universelle. Il est alors clair que $\overline{f}$ et $g$
sont inverses l'un de l'autre ; ce sont donc tous deux des isomorphismes.
\end{proof}

\noindent
Étudions maintenant le comportement des sous-modules par localisation.
```

</details>

### 27 — lemma-submodule-localization

Anglais L1420-1439 ; français L1414-1433.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1420) · `FR-ALGEBRA-B2-CHOICE-0027`.

Tout sous-module localisé vient de son image réciproque dans M. La preuve garde l'inclusion et l'argument par 1/s. R au lieu de A dans S inverse R est déjà imprimé dans l'anglais et reste inchangé. La transition avec N=I et M=A conserve le même idéal ; le I explicité en prose n'est pas un nouveau quantificateur.

Point particulier à relire : Conserver la lettre R de la source dans la preuve, sans la remplacer par A.

Règles : FR-ALGEBRA-B2-RULE-quotients.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-submodule-localization}
Any submodule $N'$ of $S^{-1}M$ is of the form $S^{-1}N$ for some
$N\subset M$. Indeed one can take $N$ to be the inverse image of
$N'$ in $M$.
\end{lemma}

\begin{proof}
Let $N$ be the inverse image of $N'$ in $M$. Then one can see that
$S^{-1}N\supset N'$. To show they are equal, take $x/s$ in
$S^{-1}N$, where $s\in S$ and $x\in N$. This yields that $x/1\in
N'$. Since $N'$ is an $S^{-1}R$-submodule we have
$x/s = x/1\cdot 1/s\in N'$. This finishes the proof.
\end{proof}

\noindent
Taking $M = A$ and $N = I$ an ideal of $A$, we have the following
corollary, which can be viewed as a converse of the first part of
Proposition \ref{proposition-localize-quotient}.
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-submodule-localization}
Tout sous-module $N'$ de $S^{-1}M$ est de la forme $S^{-1}N$ pour un certain
$N\subset M$. On peut en effet prendre pour $N$ l'image réciproque de
$N'$ dans $M$.
\end{lemma}

\begin{proof}
Soit $N$ l'image réciproque de $N'$ dans $M$. On voit alors que
$S^{-1}N\supset N'$. Pour montrer qu'ils sont égaux, prenons $x/s$ dans
$S^{-1}N$, où $s\in S$ et $x\in N$. Il s'ensuit que $x/1\in
N'$. Puisque $N'$ est un $S^{-1}R$-sous-module, nous avons
$x/s = x/1\cdot 1/s\in N'$. Cela achève la démonstration.
\end{proof}

\noindent
En prenant $M = A$ et $N = I$, où I est un idéal de $A$, nous obtenons le
corollaire suivant, que l'on peut considérer comme une réciproque de la première partie de la
Proposition \ref{proposition-localize-quotient}.
```

</details>

### 28 — lemma-ideal-in-localization

Anglais L1440-1461 ; français L1434-1454.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1440) · `FR-ALGEBRA-B2-CHOICE-0028`.

Localisés d'idéaux dans le slogan désigne exactement les modules idéaux localisés, sans affirmer l'injectivité du morphisme A vers S inverse A. L'idéal choisi est l'image réciproque et la preuve garde son unique référence.

Règles : FR-ALGEBRA-B2-RULE-localisation, FR-ALGEBRA-B2-RULE-quotients.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ideal-in-localization}
\begin{slogan}
Ideals in the localization of a ring are localizations of ideals.
\end{slogan}
Each ideal $I'$ of $S^{-1}A$ takes the form $S^{-1}I$, where one can
take $I$ to be the inverse image of $I'$ in $A$.
\end{lemma}

\begin{proof}
Immediate from Lemma \ref{lemma-submodule-localization}.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-ideal-in-localization}
\begin{slogan}
Les idéaux de la localisation d'un anneau sont les localisés d'idéaux.
\end{slogan}
Tout idéal $I'$ de $S^{-1}A$ est de la forme $S^{-1}I$, où l'on peut
prendre pour $I$ l'image réciproque de $I'$ dans $A$.
\end{lemma}

\begin{proof}
Cela résulte immédiatement du Lemme \ref{lemma-submodule-localization}.
\end{proof}
```

</details>

### 29 — section-hom

Anglais L1462-1494 ; français L1455-1487.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1462) · `FR-ALGEBRA-B2-CHOICE-0029`.

Hom interne désigne ici le module des applications linéaires, pas seulement un ensemble. La structure additive et l'action R sont conservées. Précomposition et postcomposition respectent la variance : le premier argument est contravariant. Aucun signe ni flèche du carré ne change. Le syntagme exact Hom interne n'est pas prétendu attesté par les deux nouvelles lectures de canon de ce lot.

Point particulier à relire : Attestation externe exacte de Hom interne absente des passages nouvellement consultés ; choix maintenu provisoirement par son sens explicite.

Règles : FR-ALGEBRA-B2-RULE-hom-variance.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Internal Hom}
\label{section-hom}

\noindent
If $R$ is a ring, and $M$, $N$ are $R$-modules, then
$$
\Hom_R(M, N) = \{ \varphi : M \to N\}
$$
is the set of $R$-linear maps from $M$ to $N$. This set comes with
the structure of an abelian group by setting
$(\varphi + \psi)(m) = \varphi(m) + \psi(m)$, as usual.
In fact, $\Hom_R(M, N)$ is also an $R$-module via the rule
$(x \varphi)(m) = x \varphi(m) = \varphi(xm)$.

\medskip\noindent
Given maps $a : M \to M'$ and $b : N \to N'$ of $R$-modules, we can
pre-compose and post-compose homomorphisms by $a$ and $b$. This leads
to the following commutative diagram
$$
\xymatrix{
\Hom_R(M', N) \ar[d]_{- \circ a} \ar[r]_{b \circ -} &
\Hom_R(M', N') \ar[d]^{- \circ a} \\
\Hom_R(M, N) \ar[r]^{b \circ -} &
\Hom_R(M, N')
}
$$
In fact, the maps in this diagram are $R$-module maps.
Thus $\Hom_R$ defines an additive functor
$$
\text{Mod}_R^{opp} \times \text{Mod}_R \longrightarrow \text{Mod}_R, \quad
(M, N) \longmapsto \Hom_R(M, N)
$$
```

Français actuel :
```tex
\section{Hom interne}
\label{section-hom}

\noindent
Si $R$ est un anneau et si $M$, $N$ sont des $R$-modules, alors
$$
\Hom_R(M, N) = \{ \varphi : M \to N\}
$$
est l'ensemble des applications $R$-linéaires de $M$ vers $N$. Cet ensemble est muni
d'une structure de groupe abélien en posant, comme d'habitude,
$(\varphi + \psi)(m) = \varphi(m) + \psi(m)$.
En fait, $\Hom_R(M, N)$ est aussi un $R$-module par la règle
$(x \varphi)(m) = x \varphi(m) = \varphi(xm)$.

\medskip\noindent
Étant donnés des homomorphismes $a : M \to M'$ et $b : N \to N'$ de $R$-modules, nous pouvons
précomposer et postcomposer les homomorphismes par $a$ et $b$. On obtient
le diagramme commutatif suivant :
$$
\xymatrix{
\Hom_R(M', N) \ar[d]_{- \circ a} \ar[r]_{b \circ -} &
\Hom_R(M', N') \ar[d]^{- \circ a} \\
\Hom_R(M, N) \ar[r]^{b \circ -} &
\Hom_R(M, N')
}
$$
En fait, les applications de ce diagramme sont des homomorphismes de $R$-modules.
Ainsi, $\Hom_R$ définit un foncteur additif
$$
\text{Mod}_R^{opp} \times \text{Mod}_R \longrightarrow \text{Mod}_R, \quad
(M, N) \longmapsto \Hom_R(M, N)
$$
```

</details>

### 30 — lemma-hom-exact

Anglais L1495-1512 ; français L1488-1505.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1495) · `FR-ALGEBRA-B2-CHOICE-0030`.

Les deux équivalences et le quantificateur pour tout N restent présents. La première séquence inverse l'ordre des M_i ; la seconde le garde. Ne pas transformer l'exactitude à gauche en exactitude complète. La démonstration demeure omise.

Règles : FR-ALGEBRA-B2-RULE-exactitude.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-hom-exact}
Exactness and $\Hom_R$. Let $R$ be a ring. Let $M_1$, $M_2$, $M_3$
be $R$-modules. Let $M_1 \to M_2$ and $M_2 \to M_3$ be $R$-module maps.
\begin{enumerate}
\item $M_1 \to M_2 \to M_3 \to 0$ is exact if and only if
$0 \to \Hom_R(M_3, N) \to \Hom_R(M_2, N) \to \Hom_R(M_1, N)$
is exact for all $R$-modules $N$.
\item $0 \to M_1 \to M_2 \to M_3$ is exact if and only if
$0 \to \Hom_R(N, M_1) \to \Hom_R(N, M_2) \to \Hom_R(N, M_3)$
is exact for all $R$-modules $N$.
\end{enumerate}
\end{lemma}

\begin{proof}
Omitted.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-hom-exact}
Exactitude et $\Hom_R$. Soit $R$ un anneau. Soient $M_1$, $M_2$, $M_3$
des $R$-modules. Soient $M_1 \to M_2$ et $M_2 \to M_3$ des homomorphismes de $R$-modules.
\begin{enumerate}
\item $M_1 \to M_2 \to M_3 \to 0$ est exacte si et seulement si
$0 \to \Hom_R(M_3, N) \to \Hom_R(M_2, N) \to \Hom_R(M_1, N)$
est exacte pour tout $R$-module $N$.
\item $0 \to M_1 \to M_2 \to M_3$ est exacte si et seulement si
$0 \to \Hom_R(N, M_1) \to \Hom_R(N, M_2) \to \Hom_R(N, M_3)$
est exacte pour tout $R$-module $N$.
\end{enumerate}
\end{lemma}

\begin{proof}
Démonstration omise.
\end{proof}
```

</details>

### 31 — lemma-hom-from-finitely-presented

Anglais L1513-1579 ; français L1506-1572.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1513) · `FR-ALGEBRA-B2-CHOICE-0031`.

M est de présentation finie, pas simplement de type fini. Les trois expressions Hom gardent leurs anneaux de base. La preuve utilise les deux rangs finis n,m, l'exactitude de la localisation puis la même suite obtenue par Hom. En inversant S est une formulation de localisation, non une inversion de flèches du diagramme.

Règles : FR-ALGEBRA-B2-RULE-localisation, FR-ALGEBRA-B2-RULE-exactitude, FR-ALGEBRA-B2-RULE-presentation.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-hom-from-finitely-presented}
Let $R$ be a ring. Let $M$ be a finitely presented $R$-module.
Let $N$ be an $R$-module.
\begin{enumerate}
\item For $f \in R$ we have
$\Hom_R(M, N)_f = \Hom_{R_f}(M_f, N_f) = \Hom_R(M_f, N_f)$,
\item for a multiplicative subset $S$ of $R$ we have
$$
S^{-1}\Hom_R(M, N) = \Hom_{S^{-1}R}(S^{-1}M, S^{-1}N) =
\Hom_R(S^{-1}M, S^{-1}N).
$$
\end{enumerate}
\end{lemma}

\begin{proof}
Part (1) is a special case of part (2).
The second equality in (2) follows from
Lemma \ref{lemma-localization-and-modules}.
Choose a presentation
$$
\bigoplus\nolimits_{j = 1, \ldots, m} R
\longrightarrow
\bigoplus\nolimits_{i = 1, \ldots, n} R
\to M \to 0.
$$
By
Lemma \ref{lemma-hom-exact}
this gives an exact sequence
$$
0 \to
\Hom_R(M, N) \to
\bigoplus\nolimits_{i = 1, \ldots, n} N
\longrightarrow
\bigoplus\nolimits_{j = 1, \ldots, m} N.
$$
Inverting $S$ and using Proposition \ref{proposition-localization-exact}
we get an exact sequence
$$
0 \to
S^{-1}\Hom_R(M, N) \to
\bigoplus\nolimits_{i = 1, \ldots, n} S^{-1}N
\longrightarrow
\bigoplus\nolimits_{j = 1, \ldots, m} S^{-1}N
$$
and the result follows since $S^{-1}M$ sits in
an exact sequence
$$
\bigoplus\nolimits_{j = 1, \ldots, m} S^{-1}R
\longrightarrow
\bigoplus\nolimits_{i = 1, \ldots, n} S^{-1}R \to S^{-1}M \to 0
$$
which induces (by Lemma \ref{lemma-hom-exact})
the exact sequence
$$
0 \to
\Hom_{S^{-1}R}(S^{-1}M, S^{-1}N) \to
\bigoplus\nolimits_{i = 1, \ldots, n} S^{-1}N
\longrightarrow
\bigoplus\nolimits_{j = 1, \ldots, m} S^{-1}N
$$
which is the same as the one above.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-hom-from-finitely-presented}
Soit $R$ un anneau. Soit $M$ un $R$-module de présentation finie.
Soit $N$ un $R$-module.
\begin{enumerate}
\item Pour $f \in R$, nous avons
$\Hom_R(M, N)_f = \Hom_{R_f}(M_f, N_f) = \Hom_R(M_f, N_f)$,
\item pour une partie multiplicative $S$ de $R$, nous avons
$$
S^{-1}\Hom_R(M, N) = \Hom_{S^{-1}R}(S^{-1}M, S^{-1}N) =
\Hom_R(S^{-1}M, S^{-1}N).
$$
\end{enumerate}
\end{lemma}

\begin{proof}
L'assertion (1) est un cas particulier de l'assertion (2).
La seconde égalité dans (2) résulte du
Lemme \ref{lemma-localization-and-modules}.
Choisissons une présentation
$$
\bigoplus\nolimits_{j = 1, \ldots, m} R
\longrightarrow
\bigoplus\nolimits_{i = 1, \ldots, n} R
\to M \to 0.
$$
D'après le
Lemme \ref{lemma-hom-exact},
nous obtenons une suite exacte
$$
0 \to
\Hom_R(M, N) \to
\bigoplus\nolimits_{i = 1, \ldots, n} N
\longrightarrow
\bigoplus\nolimits_{j = 1, \ldots, m} N.
$$
En inversant $S$ et en utilisant la Proposition \ref{proposition-localization-exact},
nous obtenons une suite exacte
$$
0 \to
S^{-1}\Hom_R(M, N) \to
\bigoplus\nolimits_{i = 1, \ldots, n} S^{-1}N
\longrightarrow
\bigoplus\nolimits_{j = 1, \ldots, m} S^{-1}N
$$
et le résultat en découle puisque $S^{-1}M$ s'insère dans
une suite exacte
$$
\bigoplus\nolimits_{j = 1, \ldots, m} S^{-1}R
\longrightarrow
\bigoplus\nolimits_{i = 1, \ldots, n} S^{-1}R \to S^{-1}M \to 0
$$
qui induit (d'après le Lemme \ref{lemma-hom-exact})
la suite exacte
$$
0 \to
\Hom_{S^{-1}R}(S^{-1}M, S^{-1}N) \to
\bigoplus\nolimits_{i = 1, \ldots, n} S^{-1}N
\longrightarrow
\bigoplus\nolimits_{j = 1, \ldots, m} S^{-1}N
$$
qui est la même que ci-dessus.
\end{proof}
```

</details>

### 32 — section-colim-and-hom

Anglais L1580-1587 ; français L1573-1580.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1580) · `FR-ALGEBRA-B2-CHOICE-0032`.

Le titre et l'introduction distinguent génération finie et présentation finie. La caractérisation porte sur le foncteur Hom(N,-), non sur Hom(-,N). Lombardi 3.2-3.3 atteste la distinction entre générateurs et relations finies.

Règles : FR-ALGEBRA-B2-RULE-presentation.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Characterizing finite and finitely presented modules}
\label{section-colim-and-hom}

\noindent
Given a module $N$ over a ring $R$, you can characterize whether or not
$N$ is a finite module or a finitely presented module
in terms of the functor $\Hom_R(N, -)$.
```

Français actuel :
```tex
\section{Caractérisation des modules de type fini et de présentation finie}
\label{section-colim-and-hom}

\noindent
Étant donné un module $N$ sur un anneau $R$, on peut caractériser si
$N$ est ou non un module de type fini ou un module de présentation finie
à l'aide du foncteur $\Hom_R(N, -)$.
```

</details>

### 33 — lemma-characterize-finite-module-hom

Anglais L1588-1619 ; français L1581-1612.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1588) · `FR-ALGEBRA-B2-CHOICE-0033`.

La propriété équivalente est l'injectivité pour toute colimite filtrante, non la surjectivité. Les générateurs en nombre fini permettent un seul indice ultérieur. Au retour, se factorise par N_E exprime l'image contenue dans le sous-module N_E via son inclusion ; ce n'est pas une correction du raisonnement. Le quotient colim N/N_E nul est conservé.

Règles : FR-ALGEBRA-B2-RULE-colimite, FR-ALGEBRA-B2-RULE-filtrant, FR-ALGEBRA-B2-RULE-exactitude, FR-ALGEBRA-B2-RULE-presentation, FR-ALGEBRA-B2-RULE-quotients.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-finite-module-hom}
Let $R$ be a ring. Let $N$ be an $R$-module. The following are equivalent
\begin{enumerate}
\item $N$ is a finite $R$-module,
\item for any filtered colimit $M = \colim M_i$ of $R$-modules the map
$\colim \Hom_R(N, M_i) \to \Hom_R(N, M)$ is injective.
\end{enumerate}
\end{lemma}

\begin{proof}
Assume (1) and choose generators $x_1, \ldots, x_m$ for $N$.
If $N \to M_i$ is a module map and the composition
$N \to M_i \to M$ is zero, then because $M = \colim_{i' \geq i} M_{i'}$
for each $j \in \{1, \ldots, m\}$ we can find a $i' \geq i$ such that
$x_j$ maps to zero in $M_{i'}$. Since there are finitely many
$x_j$ we can find a single $i'$ which works for all of them.
Then the composition $N \to M_i \to M_{i'}$ is zero and we conclude
the map is injective, i.e., part (2) holds.

\medskip\noindent
Assume (2). For a finite subset $E \subset N$ denote $N_E \subset N$
the $R$-submodule generated by the elements of $E$. Then
$0 = \colim N/N_E$ is a filtered colimit. Hence we see that
$\text{id} : N \to N$ maps into $N_E$ for some $E$, i.e., $N$
is finitely generated.
\end{proof}

\noindent
For purposes of reference, we define what it means to have a relation
between elements of a module.
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-characterize-finite-module-hom}
Soit $R$ un anneau. Soit $N$ un $R$-module. Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item $N$ est un $R$-module de type fini,
\item pour toute colimite filtrante $M = \colim M_i$ de $R$-modules, l'application
$\colim \Hom_R(N, M_i) \to \Hom_R(N, M)$ est injective.
\end{enumerate}
\end{lemma}

\begin{proof}
Supposons (1) et choisissons des générateurs $x_1, \ldots, x_m$ de $N$.
Si $N \to M_i$ est un homomorphisme de modules et si la composée
$N \to M_i \to M$ est nulle, alors, puisque $M = \colim_{i' \geq i} M_{i'}$,
pour tout $j \in \{1, \ldots, m\}$, nous pouvons trouver un $i' \geq i$ tel que
$x_j$ s'envoie sur zéro dans $M_{i'}$. Comme les $x_j$ sont en nombre fini,
nous pouvons trouver un seul $i'$ qui convienne à tous.
La composée $N \to M_i \to M_{i'}$ est alors nulle, et nous en concluons que
l'application est injective, c'est-à-dire que l'assertion (2) vaut.

\medskip\noindent
Supposons (2). Pour un sous-ensemble fini $E \subset N$, notons $N_E \subset N$
le $R$-sous-module engendré par les éléments de $E$. Alors
$0 = \colim N/N_E$ est une colimite filtrante. Nous voyons donc que
$\text{id} : N \to N$ se factorise par $N_E$ pour un certain $E$, c'est-à-dire que $N$
est de type fini.
\end{proof}

\noindent
Pour référence, nous définissons ce que signifie l'existence d'une relation
entre des éléments d'un module.
```

</details>

### 34 — definition-relation

Anglais L1620-1628 ; français L1613-1621.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1620) · `FR-ALGEBRA-B2-CHOICE-0034`.

Une relation est une famille de coefficients dans R donnant une combinaison nulle des éléments de M. n peut être zéro. Lombardi 3.2 atteste module des relations ; la définition concrète officielle fixe ici le contenu sans importer ses conventions de cohérence.

Règles : titre et contexte directement comparés.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-relation}
Let $R$ be a ring. Let $M$ be an $R$-module.
Let $n \geq 0$ and $x_i \in M$ for $i = 1, \ldots, n$.
A {\it relation} between $x_1, \ldots, x_n$ in $M$ is a
sequence of elements $f_1, \ldots, f_n \in R$ such that
$\sum_{i = 1, \ldots, n} f_i x_i = 0$.
\end{definition}
```

Français actuel :
```tex
\begin{definition}
\label{definition-relation}
Soit $R$ un anneau. Soit $M$ un $R$-module.
Soient $n \geq 0$ et $x_i \in M$ pour $i = 1, \ldots, n$.
Une {\it relation} entre $x_1, \ldots, x_n$ dans $M$ est une
suite d'éléments $f_1, \ldots, f_n \in R$ telle que
$\sum_{i = 1, \ldots, n} f_i x_i = 0$.
\end{definition}
```

</details>

### 35 — lemma-module-colimit-fp

Anglais L1629-1657 ; français L1622-1650.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1629) · `FR-ALGEBRA-B2-CHOICE-0035`.

Chaque module est la colimite d'un système filtrant de modules de présentation finie. Les deux choix S et E sont finis ; ni M ni l'ensemble de toutes ses relations ne sont dits finis. Le conoyau R puissance #E vers R puissance #S, l'inclusion des données et la compatibilité vers M restent exacts. Les transitions ne sont pas supposées injectives.

Règles : FR-ALGEBRA-B2-RULE-colimite, FR-ALGEBRA-B2-RULE-filtrant, FR-ALGEBRA-B2-RULE-exactitude, FR-ALGEBRA-B2-RULE-presentation.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-module-colimit-fp}
Let $R$ be a ring and let $M$ be an $R$-module.
Then $M$ is the colimit of a directed system
$(M_i, \mu_{ij})$ of $R$-modules
with all $M_i$ finitely presented $R$-modules.
\end{lemma}

\begin{proof}
Consider any finite subset $S \subset M$ and any finite
collection of relations $E$ among the elements
of $S$. So each $s \in S$ corresponds to $x_s \in M$ and
each $e \in E$ consists of a vector
of elements $f_{e, s} \in R$ such that $\sum f_{e, s} x_s = 0$.
Let $M_{S, E}$ be the cokernel of the map
$$
R^{\# E} \longrightarrow R^{\# S}, \quad
(g_e)_{e\in E} \longmapsto (\sum g_e f_{e, s})_{s\in S}.
$$
There are canonical maps $M_{S, E} \to M$.
If $S \subset S'$ and if the elements of
$E$ correspond, via this map, to relations
in $E'$, then there is an obvious map
$M_{S, E} \to M_{S', E'}$ commuting with the
maps to $M$. Let $I$ be the set of pairs
$(S, E)$ with ordering by inclusion as above.
It is clear that the colimit of this directed system is $M$.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-module-colimit-fp}
Soit $R$ un anneau et soit $M$ un $R$-module.
Alors $M$ est la colimite d'un système filtrant
$(M_i, \mu_{ij})$ de $R$-modules
dont tous les $M_i$ sont des $R$-modules de présentation finie.
\end{lemma}

\begin{proof}
Considérons un sous-ensemble fini quelconque $S \subset M$ et une famille finie
de relations $E$ entre les éléments
de $S$. Ainsi, chaque $s \in S$ correspond à un $x_s \in M$ et
chaque $e \in E$ est constitué d'un vecteur
d'éléments $f_{e, s} \in R$ tel que $\sum f_{e, s} x_s = 0$.
Soit $M_{S, E}$ le conoyau de l'application
$$
R^{\# E} \longrightarrow R^{\# S}, \quad
(g_e)_{e\in E} \longmapsto (\sum g_e f_{e, s})_{s\in S}.
$$
Il existe des applications canoniques $M_{S, E} \to M$.
Si $S \subset S'$ et si les éléments de
$E$ correspondent, par cette application, à des relations
de $E'$, il existe alors une application évidente
$M_{S, E} \to M_{S', E'}$ qui commute aux
applications vers $M$. Soit $I$ l'ensemble des paires
$(S, E)$, ordonné par l'inclusion décrite ci-dessus.
Il est clair que la colimite de ce système filtrant est $M$.
\end{proof}
```

</details>

### 36 — lemma-characterize-finitely-presented-module-hom

Anglais L1658-1701 ; français L1651-1692.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1658) · `FR-ALGEBRA-B2-CHOICE-0036`.

La propriété est maintenant la bijectivité pour toute colimite filtrante. La présentation par deux modules libres de type fini, la commutation avec les sommes finies, puis l'exactitude filtrante restent intactes. Réciproquement, l'identité se factorise par un N_i ; le facteur direct est de présentation finie. La justification finale condensée de la source n'est ni remplacée ni augmentée ; fonctorielle en le module est une tournure lourde mais de sens correct.

Règles : FR-ALGEBRA-B2-RULE-colimite, FR-ALGEBRA-B2-RULE-filtrant, FR-ALGEBRA-B2-RULE-exactitude, FR-ALGEBRA-B2-RULE-presentation, FR-ALGEBRA-B2-RULE-hom-variance, FR-ALGEBRA-B2-RULE-quotients.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-finitely-presented-module-hom}
Let $R$ be a ring. Let $N$ be an $R$-module. The following are equivalent
\begin{enumerate}
\item $N$ is a finitely presented $R$-module,
\item for any filtered colimit $M = \colim M_i$ of $R$-modules the map
$\colim \Hom_R(N, M_i) \to \Hom_R(N, M)$ is bijective.
\end{enumerate}
\end{lemma}

\begin{proof}
Assume (1) and choose an exact sequence $F_{-1} \to F_0 \to N \to 0$
with $F_i$ finite free. Then we have an exact sequence
$$
0 \to \Hom_R(N, M) \to \Hom_R(F_0, M) \to \Hom_R(F_{-1}, M)
$$
functorial in the $R$-module $M$. The functors $\Hom_R(F_i, M)$ commute
with filtered colimits as $\Hom_R(R^{\oplus n}, M) = M^{\oplus n}$.
Since filtered colimits are exact
(Lemma \ref{lemma-directed-colimit-exact})
we see that (2) holds.

\medskip\noindent
Assume (2). By Lemma \ref{lemma-module-colimit-fp}
we can write $N = \colim N_i$ as a filtered
colimit such that $N_i$ is of finite presentation for all $i$.
Thus $\text{id}_N$ factors through $N_i$ for some $i$.
This means that $N$ is a direct summand of a finitely
presented $R$-module (namely $N_i$) and hence finitely presented.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-characterize-finitely-presented-module-hom}
Soit $R$ un anneau. Soit $N$ un $R$-module. Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item $N$ est un $R$-module de présentation finie,
\item pour toute colimite filtrante $M = \colim M_i$ de $R$-modules, l'application
$\colim \Hom_R(N, M_i) \to \Hom_R(N, M)$ est bijective.
\end{enumerate}
\end{lemma}

\begin{proof}
Supposons (1) et choisissons une suite exacte $F_{-1} \to F_0 \to N \to 0$
où les $F_i$ sont libres de type fini. Nous avons alors une suite exacte
$$
0 \to \Hom_R(N, M) \to \Hom_R(F_0, M) \to \Hom_R(F_{-1}, M)
$$
fonctorielle en le $R$-module $M$. Les foncteurs $\Hom_R(F_i, M)$ commutent
aux colimites filtrantes puisque $\Hom_R(R^{\oplus n}, M) = M^{\oplus n}$.
Comme les colimites filtrantes sont exactes
(Lemme \ref{lemma-directed-colimit-exact}),
nous voyons que (2) vaut.

\medskip\noindent
Supposons (2). D'après le Lemme \ref{lemma-module-colimit-fp},
nous pouvons écrire $N = \colim N_i$ comme une colimite
filtrante telle que $N_i$ soit de présentation finie pour tout $i$.
Ainsi, $\text{id}_N$ se factorise par $N_i$ pour un certain $i$.
Cela signifie que $N$ est facteur direct d'un module de
présentation finie sur $R$ (à savoir $N_i$), et est donc de présentation finie.
\end{proof}
```

</details>

## Contrôles exacts

Les 656 régions mathématiques correspondent dans l’ordre après cinq exceptions explicites, contenant six traductions de texte lecteur : for some, such that, is not a zerodivisor in et and. Aucune formule n’est masquée globalement. Les 1 174 régions du préfixe cumulatif passent avec les mêmes exceptions ; celles-ci ne changent ni les objets ni les quantificateurs.

[Les cinq exceptions exactes](ALGEBRA_PROSE_BATCH2_MATH_EXCEPTIONS.json). Les labels, références, citations, commandes invariantes, événements d’environnement, items et contrôles TeX passent. Les mathématiques du fichier entier et les octets hors du lot restent inchangés. Le retour inverse retrouve le lot 1 puis, après ses quatre réparations et les six restaurations historiques, tous les octets du témoin public préservé.

Prochaine lecture : Produits tensoriels, source L1702 / français L1693. Aucun nouveau PDF ni aucune publication de l’édition restaurée n’est revendiqué. Les constats ne valent pas certification de vérité mathématique ni attestation indépendante de chaque mot.

