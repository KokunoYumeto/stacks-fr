# Support et dimension des modules

## Résultat et portée

La section complète est comparée : anglais L14909–15098 (190 lignes), français L14690–14869 (180 lignes), huit paires complètes. 85 occurrences de règles sont contextualisées, non un décompte de tous les mots. Couverture continue : 62 sections, 543 paires et 5290 occurrences. Ni le chapitre ni l’édition ne sont terminés.

La première preuve reçoit le verbe négatif manquant dans ni a∈J ni b∈J. Une seconde formulation explicite que l’élément devenu inversible peut dépendre de l’idéal premier considéré ; l’ancien français pouvait déjà se lire ainsi. Aucun objet, résultat ou hypothèse n’est corrigé dans la source.

La filtration à quotients R/p_i, ses deux preuves, le support, la longueur après localisation, l’annulateur, les multiplicités et les dimensions sont comparés intégralement. La région length/longueur et les deux titres de preuves sont des traductions préexistantes, recensées exactement. Aucun symbole mathématique ou renvoi ne change.

Lecture produite par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. Le canon est consulté pour cette révision rétrospective, non présenté comme consulté lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch28.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH27_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH28_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH28_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH28_OCCURRENCES.json) · [Opérations](ALGEBRA_PROSE_BATCH28_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH28_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH28_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH28_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH28_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH28_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Christian Peskine — Introduction algébrique à la géométrie projective

[Source consultée](https://perso.univ-rennes1.fr/matthieu.romagny/M2_0708/bouquin.pdf) · [Fichier conservé](canon-consulted/fr-algebra/peskine-geometrie-projective-2007.pdf)

Pages PDF 57–58 et 126–127 / imprimées 56–57 et 125–126 entièrement lues ; définition 7.18, proposition 7.19, théorème 7.20, corollaire 7.21, théorème 15.7 et définition 15.8. Page PDF 58 rendue et inspectée visuellement.

Attestations courtes : « Support d’un module », « module de type fini », « annulateur de M », « dimension de M ».

Atteste support, module de type fini, annulateur, localisation et le registre des filtrations/dimensions. La définition du support par les localisés non nuls et sa fermeture dans le cas fini concordent avec les notions de Stacks.

Limites : Les résultats et les notations de Peskine ne remplacent pas ceux de Stacks. Les pages lues ne sont pas une attestation exacte de chaque phrase corrigée ni du mot cyclique ; ces choix sont motivés directement par la grammaire et le raisonnement source. La non-appartenance simultanée de a et b n'est pas une convention lexicale issue du canon.

SHA-256 : C84D597457282B22B993F523791F4A3E391A74554FF76F7F49878640789435BA.

## Modifications et motifs

Les deux opérations ne sont pas des corrections de théorèmes : une phrase française est réparée, un quantificateur est clarifié. Les anciens octets restent conservés et chaque opération est réversible. Aucune amélioration mathématique de la source n’est insérée.

### FR-ALGEBRA-B28-REPAIR-0001

Anglais L14936 ; français L14714.

Avant :
```tex
peut pas être premier. Choisissons $a, b\in R$ tels que $ab \in J$, mais que
ni $a \in J$ ni $b\in J$.
```

Après :
```tex
peut pas être premier. Choisissons $a, b\in R$ tels que $ab \in J$, mais que l'on n'ait
ni $a \in J$ ni $b\in J$.
```

Module fini devient module de type fini, non module de cardinal fini. La filtration, les quotients R/p_i et les deux preuves sont conservés. La phrase ni a∈J ni b∈J reçoit le verbe négatif qui manquait en français. La maximalité des contre-exemples, les deux inclusions strictes et la preuve par famille d'Oka sont entièrement comparées.

Les titres Première démonstration et Seconde démonstration traduisent les titres officiels. Le changement grammatical ne remplace pas les conditions de non-appartenance par des hypothèses plus fortes.

### FR-ALGEBRA-B28-REPAIR-0002

Anglais L14991 ; français L14769.

Avant :
```tex
Comme un élément de $\mathfrak m$ devient une unité dans $R_{\mathfrak p}$
pour tout idéal premier $\mathfrak p \not = \mathfrak m$ de $R$, nous voyons
que $M_{\mathfrak p} = 0$.
```

Après :
```tex
Comme un élément de $\mathfrak m$, choisi pour chaque idéal premier considéré, devient une unité dans $R_{\mathfrak p}$
pour tout idéal premier $\mathfrak p \not = \mathfrak m$ de $R$, nous voyons
que $M_{\mathfrak p} = 0$.
```

Non nul, de type fini, local et noethérien restent présents. Les deux implications sont conservées. Le français précise que l'élément de l'idéal maximal devenu inversible est choisi pour chaque idéal premier considéré ; il n'affirme pas qu'un unique élément convient simultanément à tous. Il s'agit d'une clarification linguistique du quantificateur en contexte, pas d'une correction du théorème source.

L'ancienne formulation pouvait déjà recevoir la lecture dépendant de p ; la précision ne la classe pas comme théorème faux. Le choix dépendant du premier n'est pas un choix global d'un élément hors de tous les autres premiers.

## Observations séparées sur la source

Aucune nouvelle observation d’errata source n’est créée dans ce lot. La convention d(0)=−∞ est déjà explicite dans la définition officielle et n’exige pas d’ajouter une hypothèse non nul. Aucune revendication de déduplication globale ou de première découverte n’est faite.

## Règles contextualisées

### FR-ALGEBRA-B28-RULE-SUPPORT

Support et annulateur sont comparés par définition ; les localisations ne sont pas remplacées par des quotients.

Canon : FR-ALGEBRA-B28-CANON-PESKINE.

### FR-ALGEBRA-B28-RULE-FINITE

Finitude des générateurs, longueur finie et non-nullité restent distinctes.

Canon : FR-ALGEBRA-B28-CANON-PESKINE.

### FR-ALGEBRA-B28-RULE-FILTER

Chaque passage de filtration et de sous-quotient est confronté à sa preuve source ; cyclique n'est pas attribué faussement à une attestation exacte.

Canon : FR-ALGEBRA-B28-CANON-PESKINE.

### FR-ALGEBRA-B28-RULE-IDEAL

Minimalité dans le support et maximalité d'un contre-exemple restent différentes.

Canon : FR-ALGEBRA-B28-CANON-PESKINE.

### FR-ALGEBRA-B28-RULE-LOGIC

Négations, quantificateurs et sens des inclusions vérifiés dans les deux passages complets, sans citation lexicale inventée.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B28-RULE-DIMENSION

La longueur sur l'anneau localisé et la dimension du support gardent leurs objets ; suite exacte courte reste une variante française conservée.

Canon : FR-ALGEBRA-B28-CANON-PESKINE.

## Passages parallèles complets

### 01 — section-support

Anglais L14909–14914 ; français L14690–14695.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14909) · FR-ALGEBRA-B28-CHOICE-0001.

Le titre et l'annonce correspondent exactement : support et dimension des modules. Aucun chapitre de géométrie des faisceaux ni résultat extérieur n'est ajouté.

Point particulier à relire : Lecture complète de cette section seulement ; chapitre, édition et publication restent inachevés.

Règles : FR-ALGEBRA-B28-RULE-SUPPORT, FR-ALGEBRA-B28-RULE-DIMENSION.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Support and dimension of modules}
\label{section-support}

\noindent
Some basic results on the support and dimension of modules.
```

Français restauré :
```tex
\section{Support et dimension des modules}
\label{section-support}

\noindent
Quelques résultats élémentaires sur le support et la dimension des modules.
```

</details>

### 02 — lemma-filter-Noetherian-module

Anglais L14915–14959 ; français L14696–14737.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14915) · FR-ALGEBRA-B28-CHOICE-0002.

Module fini devient module de type fini, non module de cardinal fini. La filtration, les quotients R/p_i et les deux preuves sont conservés. La phrase ni a∈J ni b∈J reçoit le verbe négatif qui manquait en français. La maximalité des contre-exemples, les deux inclusions strictes et la preuve par famille d'Oka sont entièrement comparées.

Point particulier à relire : Les titres Première démonstration et Seconde démonstration traduisent les titres officiels. Le changement grammatical ne remplace pas les conditions de non-appartenance par des hypothèses plus fortes.

Règles : FR-ALGEBRA-B28-RULE-FINITE, FR-ALGEBRA-B28-RULE-FILTER, FR-ALGEBRA-B28-RULE-IDEAL, FR-ALGEBRA-B28-RULE-LOGIC, FR-ALGEBRA-B28-RULE-DIMENSION.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-filter-Noetherian-module}
Let $R$ be a Noetherian ring, and let $M$ be a finite $R$-module.
There exists a filtration by $R$-submodules
$$
0 = M_0 \subset M_1 \subset \ldots \subset M_n = M
$$
such that each quotient $M_i/M_{i-1}$ is isomorphic
to $R/\mathfrak p_i$ for some prime ideal $\mathfrak p_i$
of $R$.
\end{lemma}

\begin{proof}[First proof]
By Lemma \ref{lemma-trivial-filter-finite-module}
it suffices to do the case $M = R/I$ for some ideal $I$.
Consider the set $S$ of ideals $J$ such that the lemma
does not hold for the module $R/J$, and order it by
inclusion. To arrive at a
contradiction, assume that $S$ is not empty. Because
$R$ is Noetherian, $S$ has a maximal element $J$.
By definition of $S$, the ideal $J$ cannot be prime.
Pick $a, b\in R$ such that $ab \in J$, but neither
$a \in J$ nor $b\in J$. Consider the filtration
$0 \subset aR/(J \cap aR) \subset R/J$.
Note that both the submodule $aR/(J \cap aR)$ and the quotient
module $(R/J)/(aR/(J \cap aR))$ are cyclic modules; write
them as $R/J'$ and $R/J''$ so we have a short exact sequence
$0 \to R/J' \to R/J \to R/J'' \to 0$.
The inclusion $J \subset J'$ is strict
as $b \in J'$ and the inclusion $J \subset J''$ is strict as $a \in J''$.
Hence by maximality of $J$, both $R/J'$ and $R/J''$ have a filtration as
above and hence so does $R/J$. Contradiction.
\end{proof}

\begin{proof}[Second proof]
For an $R$-module $M$ we say $P(M)$ holds if there exists a filtration
as in the statement of the lemma. Observe that $P$ is stable under
extensions and holds for $0$. By Lemma \ref{lemma-trivial-filter-finite-module}
it suffices to prove $P(R/I)$ holds for every ideal $I$.
If not then because $R$ is Noetherian, there is a maximal
counter example $J$. By Example \ref{example-oka-family-property-modules} and
Proposition \ref{proposition-oka}
the ideal $J$ is prime which is a contradiction.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-filter-Noetherian-module}
Soit $R$ un anneau noethérien et soit $M$ un $R$-module de type fini.
Il existe une filtration par des sous-$R$-modules
$$
0 = M_0 \subset M_1 \subset \ldots \subset M_n = M
$$
telle que chaque quotient $M_i/M_{i-1}$ soit isomorphe à
$R/\mathfrak p_i$ pour un certain idéal premier $\mathfrak p_i$ de $R$.
\end{lemma}

\begin{proof}[Première démonstration]
D'après le Lemme \ref{lemma-trivial-filter-finite-module}, il suffit de traiter
le cas $M = R/I$ pour un certain idéal $I$.
Considérons l'ensemble $S$ des idéaux $J$ tels que le lemme ne soit pas vrai
pour le module $R/J$, et ordonnons-le par inclusion. Pour obtenir une
contradiction, supposons que $S$ ne soit pas vide. Comme $R$ est noethérien,
$S$ possède un élément maximal $J$. Par définition de $S$, l'idéal $J$ ne
peut pas être premier. Choisissons $a, b\in R$ tels que $ab \in J$, mais que l'on n'ait
ni $a \in J$ ni $b\in J$. Considérons la filtration
$0 \subset aR/(J \cap aR) \subset R/J$.
Remarquons que le sous-module $aR/(J \cap aR)$ et le module quotient
$(R/J)/(aR/(J \cap aR))$ sont tous deux cycliques ; écrivons-les respectivement
$R/J'$ et $R/J''$, de sorte que nous ayons une suite exacte courte
$0 \to R/J' \to R/J \to R/J'' \to 0$.
L'inclusion $J \subset J'$ est stricte puisque $b \in J'$, et l'inclusion
$J \subset J''$ est stricte puisque $a \in J''$.
Par maximalité de $J$, les modules $R/J'$ et $R/J''$ possèdent donc tous deux
une filtration comme ci-dessus, et il en va de même de $R/J$. Contradiction.
\end{proof}

\begin{proof}[Seconde démonstration]
Pour un $R$-module $M$, disons que $P(M)$ est satisfaite s'il existe une
filtration comme dans l'énoncé du lemme. Remarquons que $P$ est stable par
extensions et qu'elle est satisfaite pour $0$. D'après le Lemme
\ref{lemma-trivial-filter-finite-module}, il suffit de démontrer que $P(R/I)$
est satisfaite pour tout idéal $I$. Dans le cas contraire, comme $R$ est
noethérien, il existe un contre-exemple maximal $J$. D'après l'Exemple
\ref{example-oka-family-property-modules} et la Proposition
\ref{proposition-oka}, l'idéal $J$ est premier, ce qui est une contradiction.
\end{proof}
```

</details>

### 03 — lemma-filter-primes-in-support

Anglais L14960–14972 ; français L14738–14750.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14960) · FR-ALGEBRA-B28-CHOICE-0003.

L'union des V(p_i), l'appartenance de chaque p_i au support et les deux renvois restent exacts. Support a ici le sens des localisations non nulles, effectivement attesté chez Peskine.

Point particulier à relire : La finitude du module est une hypothèse reprise du lemme précédent ; elle n'est ni supprimée ni imposée à un énoncé général.

Règles : Titre directement comparé.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-filter-primes-in-support}
Let $R$, $M$, $M_i$, $\mathfrak p_i$ as in
Lemma \ref{lemma-filter-Noetherian-module}.
Then $\text{Supp}(M) = \bigcup V(\mathfrak p_i)$
and in particular $\mathfrak p_i \in \text{Supp}(M)$.
\end{lemma}

\begin{proof}
This follows from Lemmas \ref{lemma-support-closed} and
\ref{lemma-support-quotient}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-filter-primes-in-support}
Soient $R$, $M$, $M_i$ et $\mathfrak p_i$ comme dans le Lemme
\ref{lemma-filter-Noetherian-module}.
Alors $\text{Supp}(M) = \bigcup V(\mathfrak p_i)$ et, en particulier,
$\mathfrak p_i \in \text{Supp}(M)$.
\end{lemma}

\begin{proof}
Cela découle des Lemmes \ref{lemma-support-closed} et
\ref{lemma-support-quotient}.
\end{proof}
```

</details>

### 04 — lemma-support-point

Anglais L14973–14995 ; français L14751–14773.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14973) · FR-ALGEBRA-B28-CHOICE-0004.

Non nul, de type fini, local et noethérien restent présents. Les deux implications sont conservées. Le français précise que l'élément de l'idéal maximal devenu inversible est choisi pour chaque idéal premier considéré ; il n'affirme pas qu'un unique élément convient simultanément à tous. Il s'agit d'une clarification linguistique du quantificateur en contexte, pas d'une correction du théorème source.

Point particulier à relire : L'ancienne formulation pouvait déjà recevoir la lecture dépendant de p ; la précision ne la classe pas comme théorème faux. Le choix dépendant du premier n'est pas un choix global d'un élément hors de tous les autres premiers.

Règles : FR-ALGEBRA-B28-RULE-FINITE, FR-ALGEBRA-B28-RULE-FILTER, FR-ALGEBRA-B28-RULE-IDEAL, FR-ALGEBRA-B28-RULE-LOGIC, FR-ALGEBRA-B28-RULE-DIMENSION.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-support-point}
Suppose that $R$ is a Noetherian local ring with
maximal ideal $\mathfrak m$. Let $M$ be a nonzero finite
$R$-module. Then $\text{Supp}(M) = \{ \mathfrak m\}$
if and only if $M$ has finite length over $R$.
\end{lemma}

\begin{proof}
Assume that $\text{Supp}(M) = \{ \mathfrak m\}$.
It suffices to show that all the primes $\mathfrak p_i$
in the filtration of Lemma \ref{lemma-filter-Noetherian-module}
are the maximal ideal. This is clear by
Lemma \ref{lemma-filter-primes-in-support}.

\medskip\noindent
Suppose that $M$ has finite length over $R$.
Then $\mathfrak m^n M = 0$ by Lemma \ref{lemma-length-infinite}.
Since some element of $\mathfrak m$ maps to a unit
in $R_{\mathfrak p}$ for any prime
$\mathfrak p \not = \mathfrak m$ in $R$ we see $M_{\mathfrak p} = 0$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-support-point}
Supposons que $R$ soit un anneau local noethérien d'idéal maximal
$\mathfrak m$. Soit $M$ un $R$-module non nul de type fini.
Alors $\text{Supp}(M) = \{ \mathfrak m\}$ si et seulement si $M$ est de
longueur finie sur $R$.
\end{lemma}

\begin{proof}
Supposons que $\text{Supp}(M) = \{ \mathfrak m\}$.
Il suffit de montrer que tous les idéaux premiers $\mathfrak p_i$ de la
filtration du Lemme \ref{lemma-filter-Noetherian-module} sont égaux à l'idéal
maximal. Cela résulte immédiatement du Lemme
\ref{lemma-filter-primes-in-support}.

\medskip\noindent
Supposons que $M$ soit de longueur finie sur $R$.
Alors $\mathfrak m^n M = 0$ d'après le Lemme \ref{lemma-length-infinite}.
Comme un élément de $\mathfrak m$, choisi pour chaque idéal premier considéré, devient une unité dans $R_{\mathfrak p}$
pour tout idéal premier $\mathfrak p \not = \mathfrak m$ de $R$, nous voyons
que $M_{\mathfrak p} = 0$.
\end{proof}
```

</details>

### 05 — lemma-Noetherian-power-ideal-kills-module

Anglais L14996–15015 ; français L14774–14794.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14996) · FR-ALGEBRA-B28-CHOICE-0005.

L'existence de n≥0, la puissance qui annule M, l'annulateur, son radical et les inclusions de fermés sont comparés. Aucun passage du cas noethérien au cas général n'est fait.

Point particulier à relire : La traduction n'identifie pas l'annulateur à son radical. La borne n≥0 et les sens opposés des inclusions d'idéaux et de fermés restent exacts.

Règles : FR-ALGEBRA-B28-RULE-FINITE, FR-ALGEBRA-B28-RULE-IDEAL, FR-ALGEBRA-B28-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Noetherian-power-ideal-kills-module}
Let $R$ be a Noetherian ring.
Let $I \subset R$ be an ideal.
Let $M$ be a finite $R$-module.
Then $I^nM = 0$ for some $n \geq 0$ if and only if
$\text{Supp}(M) \subset V(I)$.
\end{lemma}

\begin{proof}
Indeed, $I^nM = 0$ is equivalent to $I^n \subset \text{Ann}(M)$.
Since $R$ is Noetherian, this is equivalent to
$I \subset \sqrt{\text{Ann}(M)}$, see
Lemma \ref{lemma-Noetherian-power}.
This in turn is equivalent to $V(I) \supset V(\text{Ann}(M))$, see
Lemma \ref{lemma-Zariski-topology}.
By Lemma \ref{lemma-support-closed}
this is equivalent to $V(I) \supset \text{Supp}(M)$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-Noetherian-power-ideal-kills-module}
Soit $R$ un anneau noethérien.
Soit $I \subset R$ un idéal.
Soit $M$ un $R$-module de type fini.
Alors $I^nM = 0$ pour un certain $n \geq 0$ si et seulement si
$\text{Supp}(M) \subset V(I)$.
\end{lemma}

\begin{proof}
En effet, $I^nM = 0$ équivaut à $I^n \subset \text{Ann}(M)$.
Puisque $R$ est noethérien, cela équivaut à
$I \subset \sqrt{\text{Ann}(M)}$, voir le Lemme
\ref{lemma-Noetherian-power}.
À son tour, cette condition équivaut à
$V(I) \supset V(\text{Ann}(M))$, voir le Lemme
\ref{lemma-Zariski-topology}.
D'après le Lemme \ref{lemma-support-closed}, elle équivaut à
$V(I) \supset \text{Supp}(M)$.
\end{proof}
```

</details>

### 06 — lemma-filter-minimal-primes-in-support

Anglais L15016–15052 ; français L14795–14829.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15016) · FR-ALGEBRA-B28-CHOICE-0006.

Minimal désigne un élément minimal du support, pas automatiquement un premier minimal de l'anneau. Les multiplicités dans la filtration égalent la longueur du module localisé. Le corps résiduel, les deux cas d'inclusion et la longueur un restent littéraux ; seul length/longueur est une traduction déjà présente dans la formule.

Point particulier à relire : La lecture premier minimal est contrôlée dans le support. Aucun qualificatif de source n'est supprimé ou ajouté. La longueur est une longueur sur R_p, non sur R.

Règles : FR-ALGEBRA-B28-RULE-SUPPORT, FR-ALGEBRA-B28-RULE-FILTER, FR-ALGEBRA-B28-RULE-IDEAL, FR-ALGEBRA-B28-RULE-LOGIC, FR-ALGEBRA-B28-RULE-DIMENSION.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-filter-minimal-primes-in-support}
Let $R$, $M$, $M_i$, $\mathfrak p_i$ as in
Lemma \ref{lemma-filter-Noetherian-module}.
The minimal elements of the set $\{\mathfrak p_i\}$
are the minimal elements of $\text{Supp}(M)$.
The number of times a minimal prime $\mathfrak p$
occurs is
$$
\#\{i \mid \mathfrak p_i = \mathfrak p\}
=
\text{length}_{R_\mathfrak p} M_{\mathfrak p}.
$$
\end{lemma}

\begin{proof}
The first statement follows because
$\text{Supp}(M) = \bigcup V(\mathfrak p_i)$, see
Lemma \ref{lemma-filter-primes-in-support}.
Let $\mathfrak p \in \text{Supp}(M)$ be minimal.
The support of $M_{\mathfrak p}$ is the set
consisting of the maximal ideal $\mathfrak p R_{\mathfrak p}$.
Hence by Lemma \ref{lemma-support-point} the length
of $M_{\mathfrak p}$ is finite and $> 0$. Next we
note that $M_{\mathfrak p}$ has a filtration with subquotients
$
(R/\mathfrak p_i)_{\mathfrak p}
=
R_{\mathfrak p}/{\mathfrak p_i}R_{\mathfrak p}
$.
These are zero if $\mathfrak p_i \not \subset \mathfrak p$
and equal to $\kappa(\mathfrak p)$ if $\mathfrak p_i \subset
\mathfrak p$ because by minimality of $\mathfrak p$
we have $\mathfrak p_i = \mathfrak p$ in this case.
The result follows since $\kappa(\mathfrak p)$ has length $1$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-filter-minimal-primes-in-support}
Soient $R$, $M$, $M_i$ et $\mathfrak p_i$ comme dans le Lemme
\ref{lemma-filter-Noetherian-module}.
Les éléments minimaux de l'ensemble $\{\mathfrak p_i\}$ sont les éléments
minimaux de $\text{Supp}(M)$. Le nombre de fois qu'un idéal premier minimal
$\mathfrak p$ apparaît est
$$
\#\{i \mid \mathfrak p_i = \mathfrak p\}
=
\text{longueur}_{R_\mathfrak p} M_{\mathfrak p}.
$$
\end{lemma}

\begin{proof}
La première assertion résulte de l'égalité
$\text{Supp}(M) = \bigcup V(\mathfrak p_i)$, voir le Lemme
\ref{lemma-filter-primes-in-support}.
Soit $\mathfrak p \in \text{Supp}(M)$ un élément minimal.
Le support de $M_{\mathfrak p}$ est l'ensemble réduit à l'idéal maximal
$\mathfrak p R_{\mathfrak p}$. D'après le Lemme \ref{lemma-support-point},
la longueur de $M_{\mathfrak p}$ est donc finie et $> 0$.
Remarquons ensuite que $M_{\mathfrak p}$ possède une filtration dont les
sous-quotients sont
$
(R/\mathfrak p_i)_{\mathfrak p}
=
R_{\mathfrak p}/{\mathfrak p_i}R_{\mathfrak p}
$.
Ils sont nuls si $\mathfrak p_i \not \subset \mathfrak p$, et ils sont égaux à
$\kappa(\mathfrak p)$ si $\mathfrak p_i \subset \mathfrak p$, car la
minimalité de $\mathfrak p$ donne alors $\mathfrak p_i = \mathfrak p$.
Le résultat en découle puisque $\kappa(\mathfrak p)$ est de longueur $1$.
\end{proof}
```

</details>

### 07 — lemma-support-dimension-d

Anglais L15053–15071 ; français L14830–14850.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15053) · FR-ALGEBRA-B28-CHOICE-0007.

Le nombre d(M) est celui défini dans Stacks, non une nouvelle convention tirée du canon. Le maximum des dimensions, la dimension de V(p_i) et le rôle des premiers minimaux sont comparés. Pour M=0, la définition source fixe d(0)=−∞, compatible avec le support vide ; aucune hypothèse non nul n'est ajoutée.

Point particulier à relire : La convention d(0)=−∞ a été relue directement dans definition-d. L'écriture du maximum vide reste la convention implicite du texte et n'est pas enrichie dans la traduction. Les conventions de Peskine ne sont pas importées.

Règles : FR-ALGEBRA-B28-RULE-FINITE, FR-ALGEBRA-B28-RULE-IDEAL, FR-ALGEBRA-B28-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-support-dimension-d}
Let $R$ be a Noetherian local ring.
Let $M$ be a finite $R$-module.
Then $d(M) = \dim(\text{Supp}(M))$ where $d(M)$ is as in
Definition \ref{definition-d}.
\end{lemma}

\begin{proof}
Let $M_i, \mathfrak p_i$ be as in Lemma \ref{lemma-filter-Noetherian-module}.
By Lemma \ref{lemma-hilbert-ses-chi} we obtain the equality
$d(M) = \max \{ d(R/\mathfrak p_i) \}$. By
Proposition \ref{proposition-dimension} we have
$d(R/\mathfrak p_i) = \dim(R/\mathfrak p_i)$.
Trivially $\dim(R/\mathfrak p_i) = \dim V(\mathfrak p_i)$.
Since all minimal primes of $\text{Supp}(M)$ occur among
the $\mathfrak p_i$ (Lemma \ref{lemma-filter-minimal-primes-in-support}) we win.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-support-dimension-d}
Soit $R$ un anneau local noethérien.
Soit $M$ un $R$-module de type fini.
Alors $d(M) = \dim(\text{Supp}(M))$, où $d(M)$ est défini dans la
Définition \ref{definition-d}.
\end{lemma}

\begin{proof}
Soient $M_i, \mathfrak p_i$ comme dans le Lemme
\ref{lemma-filter-Noetherian-module}.
Le Lemme \ref{lemma-hilbert-ses-chi} donne l'égalité
$d(M) = \max \{ d(R/\mathfrak p_i) \}$. D'après la Proposition
\ref{proposition-dimension}, nous avons
$d(R/\mathfrak p_i) = \dim(R/\mathfrak p_i)$.
Il est clair que $\dim(R/\mathfrak p_i) = \dim V(\mathfrak p_i)$.
Comme tous les idéaux premiers minimaux de $\text{Supp}(M)$ figurent parmi les
$\mathfrak p_i$ (Lemme \ref{lemma-filter-minimal-primes-in-support}), le
résultat en découle.
\end{proof}
```

</details>

### 08 — lemma-ses-dimension

Anglais L15072–15098 ; français L14851–14869.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15072) · FR-ALGEBRA-B28-CHOICE-0008.

La suite exacte courte et ses trois modules de type fini restent identiques. Le maximum des deux dimensions est conservé. La seconde preuve vaut sans localité, utilise les trois supports fermés et l'union des supports ; elle n'est pas remplacée par une preuve extérieure.

Point particulier à relire : Le registre suite exacte courte est conservé ; le canon atteste suite exacte mais les passages lus ne prouvent pas que ce soit l'unique variante française admissible.

Règles : FR-ALGEBRA-B28-RULE-FINITE, FR-ALGEBRA-B28-RULE-LOGIC, FR-ALGEBRA-B28-RULE-DIMENSION.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ses-dimension}
Let $R$ be a Noetherian ring. Let $0 \to M' \to M \to M'' \to 0$
be a short exact sequence of finite $R$-modules. Then
$\max\{\dim(\text{Supp}(M')), \dim(\text{Supp}(M''))\} =
\dim(\text{Supp}(M))$.
\end{lemma}

\begin{proof}
If $R$ is local, this follows immediately from
Lemmas \ref{lemma-support-dimension-d} and \ref{lemma-hilbert-ses-chi}.
A more elementary argument, which works also if $R$ is not local,
is to use that $\text{Supp}(M')$, $\text{Supp}(M'')$, and
$\text{Supp}(M)$ are closed (Lemma \ref{lemma-support-closed})
and that $\text{Supp}(M) = \text{Supp}(M') \cup \text{Supp}(M'')$
(Lemma \ref{lemma-support-quotient}).
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ses-dimension}
Soit $R$ un anneau noethérien. Soit
$0 \to M' \to M \to M'' \to 0$ une suite exacte courte de $R$-modules de
type fini. Alors
$\max\{\dim(\text{Supp}(M')), \dim(\text{Supp}(M''))\} =
\dim(\text{Supp}(M))$.
\end{lemma}

\begin{proof}
Si $R$ est local, cela découle immédiatement des Lemmes
\ref{lemma-support-dimension-d} et \ref{lemma-hilbert-ses-chi}.
Un argument plus élémentaire, qui vaut aussi lorsque $R$ n'est pas local,
consiste à utiliser le fait que $\text{Supp}(M')$, $\text{Supp}(M'')$ et
$\text{Supp}(M)$ sont fermés (Lemme \ref{lemma-support-closed}) et que
$\text{Supp}(M) = \text{Supp}(M') \cup \text{Supp}(M'')$
(Lemme \ref{lemma-support-quotient}).
\end{proof}
```

</details>

## Contrôles et suite

Les 128 régions mathématiques correspondent exactement après une exception linguistique préexistante, liée à sa position et non remplacée indistinctement. Le préfixe de 10 627 régions passe avec quarante et une exceptions linguistiques au total ; les différences sont vérifiées dans leur ordre et avec leurs multiplicités exactes.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items restent identiques. Aucune citation ne figure dans ce lot ; les deux titres français de preuves sont des exceptions linguistiques préexistantes précisément identifiées. Les opérations inverses retrouvent le lot précédent puis tous les octets du témoin public préservé. Préfixe déjà relu et suffixe encore non relu sont inchangés.

Les 543 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Idéaux premiers associés, anglais L15099 / français L14870. Aucun PDF nouveau ni publication ; restauration globale en cours.

