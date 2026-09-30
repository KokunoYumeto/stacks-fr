# Dimension

## Résultat et portée

La section complète est comparée : anglais L14305–14730 (426 lignes), français L14111–14532 (422 lignes), quinze paires complètes. 253 occurrences de règles sont contextualisées, non un décompte de tous les mots. Couverture continue : 60 sections, 530 paires et 5098 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Deux formulations françaises de comparaison de degrés sont simplifiées en conservant exactement les formules. Une opération distincte rétablit minimal ideal sans la qualification premier ajoutée par la traduction ; son motif diplomatique et son alternative sont explicites. Les deux observations de source restent hors du texte français : qualification de minimal, et convention de dimension de l’anneau nul.

Les dix conditions de dimension zéro, les cinq conditions de dimension un, les trois conditions de dimension d, les localisations, les paramètres et toutes les étapes des preuves sont comparés. Les deux régions length/longueur sont des traductions linguistiques préexistantes ; aucun symbole mathématique ou renvoi ne change.

Lecture produite par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. Le canon est consulté pour cette révision rétrospective, non présenté comme consulté lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch26.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH25_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH26_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH26_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH26_OCCURRENCES.json) · [Opérations](ALGEBRA_PROSE_BATCH26_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH26_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH26_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH26_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH26_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH26_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Antoine Ducros — Cours sur les schémas

[Source consultée](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages PDF/imprimées 122–124 entièrement lues ; §2.8.14, §2.8.15 et proposition 2.8.16. Page 122 rendue et inspectée visuellement.

Attestations courtes : « dimension de Krull », « borne supérieure », « chaîne strictement croissante », « anneau local noethérien ».

Atteste le registre des chaînes, de leur longueur, de la dimension de Krull et de la régularité locale. Le cas de l'anneau nul à −∞ est explicitement traité.

Limites : L'attestation ne remplace ni les théorèmes ni les renvois de Stacks. Elle ne dispense pas de vérifier les objets et les quantificateurs de chaque passage.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

### Christian Peskine — Introduction algébrique à la géométrie projective

[Source consultée](https://perso.univ-rennes1.fr/matthieu.romagny/M2_0708/bouquin.pdf) · [Fichier conservé](canon-consulted/fr-algebra/peskine-geometrie-projective-2007.pdf)

Pages PDF 125–129 / imprimées 124–128 et PDF 158 / imprimée 157 entièrement lues. Corollaires 15.4–15.5, théorème 15.7, définitions 15.15/15.19, proposition 15.20 et définition 18.1 ; page PDF 129 rendue et inspectée.

Attestations courtes : « système de paramètres », « idéal premier minimal », « hauteur », « Anneaux locaux réguliers ».

Registre français des paramètres, de la hauteur et de la comparaison des degrés, ainsi que les notions locales liées à la dimension.

Limites : Les conventions de dimension et les formulations de Peskine ne sont pas importées. Ses paramètres concernent aussi les modules ; Stacks définit ici ceux d'un anneau. Le passage atteste degré strictement inférieur à, mais le remplacement retenu conserve plutôt directement la formule source.

SHA-256 : C84D597457282B22B993F523791F4A3E391A74554FF76F7F49878640789435BA.

## Modifications et motifs

Les deux changements de registre ne sont pas comptés comme des corrections de théorèmes. La restauration de qualification est comptée séparément ; les anciens octets restent conservés et chaque opération est réversible.

### FR-ALGEBRA-B26-REPAIR-0001

Anglais L14376 ; français L14182.

Avant :
```tex
où $\mathfrak p_i$ est un idéal premier minimal.
```

Après :
```tex
où $\mathfrak p_i$ est un idéal minimal.
```

Les deux implications, la finitude des composantes, la décomposition en produit, le radical localement nilpotent puis nilpotent et la longueur finie sont relus intégralement. Une restauration diplomatique retire premier ajouté à minimal ideal : le français rend désormais idéal minimal, tandis que le sens visiblement visé — idéal premier minimal — est expliqué séparément. Cette restauration ne prétend pas que l'ancienne précision française était mathématiquement fausse.

Minimal ideal omet prime dans la source ; la restitution est signalée comme diplomatique et discutable en tant que décision éditoriale, non comme amélioration mathématique. Deux réserves sont motivées séparément : cette terminologie, et la réciproque universelle pour l'anneau nul.

### FR-ALGEBRA-B26-REPAIR-0002

Anglais L14513 ; français L14317.

Avant :
```tex
est de degré strictement inférieur ($ < 1$). Autrement dit,
```

Après :
```tex
est de degré $ < 1$. Autrement dit,
```

Les cinq conditions et leur ordre restent identiques ; la non-nilpotence de x est présente dans les deux conditions nécessaires. La preuve par évitement, l'idéal à un générateur, la borne de longueur et la contradiction par deux idéaux premiers distincts sont conservées. De degré strictement inférieur ($ < 1$) devient de degré $ < 1$ : la comparaison est portée directement par la formule, sans comparatif français suspendu ni signe modifié.

Les deux régions length/longueur de cette section sont des traductions préexistantes du texte lisible de formules. La flèche non étiquetée de la suite exacte reste non étiquetée ; aucune multiplication par x supplémentaire n'est dessinée dans la traduction.

### FR-ALGEBRA-B26-REPAIR-0003

Anglais L14586 ; français L14390.

Avant :
```tex
est de degré strictement inférieur ($ < d$). Autrement dit,
```

Après :
```tex
est de degré $ < d$. Autrement dit,
```

Les trois caractérisations et les inégalités cycliques dim(R)≥d′(R)≥d(R)≥dim(R) sont fidèles. La récurrence, les monômes comptés par le binomial, les suites exactes et la chaîne quotient sont comparés ligne par ligne. Le degré $ < d$ est rendu directement, sans le comparatif français suspendu. Dans le paragraphe suivant, éléments pour variables est une traduction contextuelle des générateurs, non une nouvelle assertion sur l'indépendance algébrique.

Les longueurs des chaînes et les degrés restent strictement les mêmes. Les questions de finitude traitées par la preuve source ne sont pas remplacées par une autre preuve. La traduction éléments explicite le sens de générateurs du contexte, à distinguer d'une variable formelle.

## Observations séparées sur la source

Ces observations ne sont ni des corrections insérées dans la traduction, ni des admissions nouvelles au registre. Aucune revendication de déduplication globale ou de première découverte n’est faite.

### lemma-Noetherian-dimension-0

[Anglais officiel L14376](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14376) · FR-ALGEBRA-B26-SOURCE-NOTE-0001.

```tex
with $\mathfrak p_i$ a minimal ideal.
```

Le contexte donne des idéaux premiers minimaux correspondant aux composantes irréductibles ; le mot prime manque. Minimal parmi tous les idéaux serait faux : pour R=k×k, p=0×k est premier minimal, mais contient strictement l'idéal nul. La correction anglaise suggérée est minimal prime ideal. La restauration française retire le mot premier ajouté, sans modifier les formules ni imposer une correction à la source. Cette décision diplomatique, et l'alternative d'une explicitation contextuelle, sont rendues visibles pour une relecture ultérieure.

Confiance éditoriale forte pour le sens visé et le contre-exemple ; décision diplomatique réversible, aucune probabilité calibrée ni admission nouvelle.

### lemma-Noetherian-dimension-0

[Anglais officiel L14366](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14366) · FR-ALGEBRA-B26-SOURCE-NOTE-0002.

```tex
Conversely, any Artinian ring is Noetherian of dimension zero.
```

Les conventions officielles admettent l'anneau nul. Il est artinien car il n'a qu'un idéal, donc toute chaîne descendante est constante. Son spectre est vide et la définition topologique citée donne dim(0)=−∞, non zéro. La réciproque universelle de ce lemme et la condition (2) de proposition-dimension-zero-ring ne couvrent donc pas correctement R=0. Deux remèdes possibles sont d'exclure R=0 dans les énoncés concernés, ou d'exprimer la condition par dim(R)≤0 en conservant la convention à −∞. Aucun de ces remèdes n'est appliqué ici : les dix clauses françaises restent fidèles. Les pièces exactes de convention et les loci liés sont conservés dans le dossier ; pas de revendication de première découverte ni de déduplication du registre.

Confiance forte sur la réserve sous les conventions effectivement lues ; toute formulation corrective reste proposée et séparée.

[Pièce primaire algebra.tex L36–45](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L36)
SHA-256 du fichier : FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.

```tex
A ring is commutative with $1$. The zero ring is a ring. In fact it is
the only ring that does not have a prime ideal. The Kronecker
symbol $\delta_{ij}$ will be used. If $R \to S$ is a ring map and
$\mathfrak q$ a prime of $S$, then we use the notation
``$\mathfrak p = R \cap \mathfrak q$''
to indicate the prime which is the inverse image of $\mathfrak q$ under
$R \to S$ even if $R$ is not a subring of $S$ and even if $R \to S$
is not injective.
```

[Pièce primaire algebra.tex L12707–12711](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12707)
SHA-256 du fichier : FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.

```tex
\begin{definition}
\label{definition-artinian}
A ring $R$ is {\it Artinian} if it satisfies the
descending chain condition for ideals.
\end{definition}
```

[Pièce primaire topology.tex L1391–1419](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1391)
SHA-256 du fichier : C6BAC8DCF8AD96DC47416BF34CB45BA4A10B894E40D67D3E1FA68D8EF0D9F872.

```tex
\begin{definition}
\label{definition-Krull}
Let $X$ be a topological space.
\begin{enumerate}
\item A {\it chain of irreducible closed subsets} of $X$
is a sequence $Z_0 \subset Z_1 \subset \ldots \subset Z_n \subset X$
with $Z_i$ closed irreducible and $Z_i \not = Z_{i + 1}$ for
$i = 0, \ldots, n - 1$.
\item The {\it length} of a chain
$Z_0 \subset Z_1 \subset \ldots \subset Z_n \subset X$
of irreducible closed subsets of $X$ is the
integer $n$.
\item The {\it dimension} or more precisely the {\it Krull dimension}
$\dim(X)$ of $X$ is the element of
$\{-\infty, 0, 1, 2, 3, \ldots, \infty\}$ defined by the formula:
$$
\dim(X) =
\sup \{\text{lengths of chains of irreducible closed subsets}\}
$$
Thus $\dim(X) = -\infty$ if and only if $X$ is the empty space.
\item Let $x \in X$.
The {\it Krull dimension of $X$ at $x$} is defined as
$$
\dim_x(X) = \min \{\dim(U), x\in U\subset X\text{ open}\}
$$
the minimum of $\dim(U)$ where $U$ runs over the open
neighbourhoods of $x$ in $X$.
\end{enumerate}
\end{definition}
```

[Pièce primaire algebra.tex L14414–14420](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14414)
SHA-256 du fichier : FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.

```tex
\begin{proposition}
\label{proposition-dimension-zero-ring}
Let $R$ be a ring. The following are equivalent:
\begin{enumerate}
\item $R$ is Artinian,
\item $R$ is Noetherian and $\dim(R) = 0$,
\item $R$ has finite length as a module over itself,
```

## Règles contextualisées

### FR-ALGEBRA-B26-RULE-DIMENSION

Dimensions, hauteurs et longueurs contrôlées dans chaque passage ; n inclusions pour n+1 idéaux, localisation et bornes préservées.

Canon : FR-ALGEBRA-B26-CANON-DUCROS, FR-ALGEBRA-B26-CANON-PESKINE.

### FR-ALGEBRA-B26-RULE-IDEAL

Primalité, minimalité, radical et nilpotence distingués ; défaut de qualification source traité dans une observation séparée.

Canon : FR-ALGEBRA-B26-CANON-PESKINE.

### FR-ALGEBRA-B26-RULE-PARAMETER

Paramètres d'un anneau et génération de l'idéal maximal distingués ; aucun passage à une suite régulière arbitraire.

Canon : FR-ALGEBRA-B26-CANON-PESKINE, FR-ALGEBRA-B26-CANON-DUCROS.

### FR-ALGEBRA-B26-RULE-LOCAL

Hypothèses locales, noethérianité, artinianité et quotients comparés ; réserve de l'anneau nul conservée hors traduction.

Canon : FR-ALGEBRA-B26-CANON-DUCROS, FR-ALGEBRA-B26-CANON-PESKINE.

### FR-ALGEBRA-B26-RULE-DEGREE

Degrés et exactitude comparés avec les fonctions φ/χ de Stacks, non une convention documentaire substituée.

Canon : FR-ALGEBRA-B26-CANON-PESKINE.

### FR-ALGEBRA-B26-RULE-LOGIC

Quantificateurs, stricteté, négations et sens des implications relus ; simplifications françaises limitées à leur justification source.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-dimension

Anglais L14305–14311 ; français L14111–14117.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14305) · FR-ALGEBRA-B26-CHOICE-0001.

Le titre Dimension et le renvoi à la topologie sont conservés. La lecture porte sur la section entière : chaînes, dimension de Krull, hauteur, dimension zéro, paramètres et inégalités. Aucune théorie de dimension supplémentaire n'est interpolée.

Point particulier à relire : Il s'agit d'un contrôle rétrospectif et borné, pas d'une validation humaine ni de la fin du chapitre.

Règles : FR-ALGEBRA-B26-RULE-DIMENSION.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Dimension}
\label{section-dimension}

\noindent
Please compare with
Topology, Section \ref{topology-section-krull-dimension}.
```

Français restauré :
```tex
\section{Dimension}
\label{section-dimension}

\noindent
Comparer avec
Topologie, section \ref{topology-section-krull-dimension}.
```

</details>

### 02 — definition-chain-primes

Anglais L14312–14325 ; français L14118–14131.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14312) · FR-ALGEBRA-B26-CHOICE-0002.

Chaîne d'idéaux premiers et longueur sont attestés dans le cours de Ducros. La longueur est n pour n+1 idéaux, et toutes les inclusions successives sont strictes. La bijection avec les fermés irréductibles renverse les inclusions ; le renvoi officiel est identique.

Point particulier à relire : La longueur compte les inclusions strictes, non les idéaux. On n'ajoute pas maximal à la définition générale d'une chaîne.

Règles : FR-ALGEBRA-B26-RULE-DIMENSION, FR-ALGEBRA-B26-RULE-IDEAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-chain-primes}
Let $R$ be a ring. A {\it chain of prime ideals} is a sequence
$\mathfrak p_0 \subset \mathfrak p_1 \subset \ldots \subset \mathfrak p_n$
of prime ideals of $R$ such that $\mathfrak p_i \not = \mathfrak p_{i + 1}$
for $i = 0, \ldots, n - 1$. The {\it length} of this chain of prime
ideals is $n$.
\end{definition}

\noindent
Recall that we have an inclusion reversing bijection between prime
ideals of a ring $R$ and irreducible closed subsets of $\Spec(R)$,
see Lemma \ref{lemma-irreducible}.
```

Français restauré :
```tex
\begin{definition}
\label{definition-chain-primes}
Soit $R$ un anneau. Une {\it chaîne d'idéaux premiers} est une suite
$\mathfrak p_0 \subset \mathfrak p_1 \subset \ldots \subset \mathfrak p_n$
d'idéaux premiers de $R$ telle que $\mathfrak p_i \not = \mathfrak p_{i + 1}$
pour $i = 0, \ldots, n - 1$. La {\it longueur} de cette chaîne d'idéaux
premiers est $n$.
\end{definition}

\noindent
Rappelons qu'il existe une bijection renversant les inclusions entre les
idéaux premiers d'un anneau $R$ et les sous-ensembles fermés irréductibles de
$\Spec(R)$; voir le Lemme \ref{lemma-irreducible}.
```

</details>

### 03 — definition-Krull

Anglais L14326–14345 ; français L14132–14151.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14326) · FR-ALGEBRA-B26-CHOICE-0003.

Dimension de Krull et borne supérieure sont directement attestés chez Ducros. Le français garde la définition via Spec(R), le renvoi topologique et la chaîne affichée. La phrase finale explicite seulement la longueur n annoncée par l'anglais ; elle n'ajoute pas une hypothèse.

Point particulier à relire : Le cas de l'ensemble vide est fixé à −∞ par la définition topologique effectivement citée ; Ducros utilise aussi cette convention. Le français ne remplace pas silencieusement la dimension de l'anneau nul par zéro.

Règles : FR-ALGEBRA-B26-RULE-DIMENSION, FR-ALGEBRA-B26-RULE-IDEAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-Krull}
The {\it Krull dimension} of the ring $R$ is the
Krull dimension of the topological space $\Spec(R)$, see
Topology, Definition \ref{topology-definition-Krull}.
In other words it is the supremum of the integers $n\geq 0$
such that $R$ has a chain of prime ideals
$$
\mathfrak p_0
\subset
\mathfrak p_1
\subset
\ldots
\subset
\mathfrak p_n, \quad
\mathfrak p_i \not = \mathfrak p_{i + 1}.
$$
of length $n$.
\end{definition}
```

Français restauré :
```tex
\begin{definition}
\label{definition-Krull}
La {\it dimension de Krull} de l'anneau $R$ est la dimension de Krull
de l'espace topologique $\Spec(R)$; voir
Topologie, Définition \ref{topology-definition-Krull}.
Autrement dit, c'est la borne supérieure des entiers $n\geq 0$
pour lesquels $R$ possède une chaîne d'idéaux premiers
$$
\mathfrak p_0
\subset
\mathfrak p_1
\subset
\ldots
\subset
\mathfrak p_n, \quad
\mathfrak p_i \not = \mathfrak p_{i + 1}.
$$
Cette chaîne est de longueur $n$.
\end{definition}
```

</details>

### 04 — definition-height

Anglais L14346–14351 ; français L14152–14157.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14346) · FR-ALGEBRA-B26-CHOICE-0004.

Hauteur est attesté par la définition 15.19 de Peskine. Pour un idéal premier, la définition officielle est dim(R_p) ; on ne la remplace pas par la hauteur d'un idéal arbitraire. Le corps, le localisé et l'idéal p restent identiques.

Point particulier à relire : Peskine définit aussi la hauteur d'un idéal non premier par un minimum. Cette extension documentaire n'est pas ajoutée à la définition de Stacks. La locution exacte système régulier de paramètres n'est pas revendiquée comme citation de la page consultée.

Règles : FR-ALGEBRA-B26-RULE-DIMENSION, FR-ALGEBRA-B26-RULE-IDEAL, FR-ALGEBRA-B26-RULE-LOCAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-height}
The {\it height} of a prime ideal $\mathfrak p$ of
a ring $R$ is the dimension of the local ring $R_{\mathfrak p}$.
\end{definition}
```

Français restauré :
```tex
\begin{definition}
\label{definition-height}
La {\it hauteur} d'un idéal premier $\mathfrak p$ d'un anneau $R$
est la dimension de l'anneau local $R_{\mathfrak p}$.
\end{definition}
```

</details>

### 05 — lemma-dimension-height

Anglais L14352–14362 ; français L14158–14168.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14352) · FR-ALGEBRA-B26-CHOICE-0005.

La borne supérieure des hauteurs des idéaux premiers, ou seulement des maximaux, est conservée. Ajouter un idéal maximal au bout d'une chaîne est la preuve abrégée source, sans reconstruction différente.

Point particulier à relire : La formule parenthétique (maximaux) porte sur les idéaux premiers. Le raisonnement abrégé reste inchangé.

Règles : FR-ALGEBRA-B26-RULE-DIMENSION, FR-ALGEBRA-B26-RULE-IDEAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-dimension-height}
The Krull dimension of $R$ is the supremum of the
heights of its (maximal) primes.
\end{lemma}

\begin{proof}
This is so because we can always add a maximal ideal at the end of a chain
of prime ideals.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-dimension-height}
La dimension de Krull de $R$ est la borne supérieure des hauteurs de ses
idéaux premiers (maximaux).
\end{lemma}

\begin{proof}
Cela résulte du fait que l'on peut toujours ajouter un idéal maximal à la fin
d'une chaîne d'idéaux premiers.
\end{proof}
```

</details>

### 06 — lemma-Noetherian-dimension-0

Anglais L14363–14402 ; français L14169–14208.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14363) · FR-ALGEBRA-B26-CHOICE-0006.

Les deux implications, la finitude des composantes, la décomposition en produit, le radical localement nilpotent puis nilpotent et la longueur finie sont relus intégralement. Une restauration diplomatique retire premier ajouté à minimal ideal : le français rend désormais idéal minimal, tandis que le sens visiblement visé — idéal premier minimal — est expliqué séparément. Cette restauration ne prétend pas que l'ancienne précision française était mathématiquement fausse.

Point particulier à relire : Minimal ideal omet prime dans la source ; la restitution est signalée comme diplomatique et discutable en tant que décision éditoriale, non comme amélioration mathématique. Deux réserves sont motivées séparément : cette terminologie, et la réciproque universelle pour l'anneau nul.

Règles : FR-ALGEBRA-B26-RULE-DIMENSION, FR-ALGEBRA-B26-RULE-IDEAL, FR-ALGEBRA-B26-RULE-LOCAL, FR-ALGEBRA-B26-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Noetherian-dimension-0}
A Noetherian ring of dimension $0$ is Artinian.
Conversely, any Artinian ring is Noetherian of dimension zero.
\end{lemma}

\begin{proof}
Assume $R$ is a Noetherian ring of dimension $0$.
By Lemma \ref{lemma-Noetherian-topology} the space $\Spec(R)$
is Noetherian. By Topology, Lemma \ref{topology-lemma-Noetherian} we see
that $\Spec(R)$ has finitely many irreducible
components, say $\Spec(R) = Z_1 \cup \ldots \cup Z_r$.
According to Lemma \ref{lemma-irreducible} each $Z_i = V(\mathfrak p_i)$
with $\mathfrak p_i$ a minimal ideal. Since the dimension is $0$
these $\mathfrak p_i$ are also maximal. Thus $\Spec(R)$
is the discrete topological space with elements $\mathfrak p_i$.
All elements $f$ of the Jacobson radical $\bigcap \mathfrak p_i$
are nilpotent since otherwise $R_f$ would not be the zero ring
and we would have another prime.
By Lemma \ref{lemma-product-local} $R$ is equal to
$\prod R_{\mathfrak p_i}$. Since $R_{\mathfrak p_i}$
is also Noetherian and dimension $0$, the previous arguments
show that its radical $\mathfrak p_iR_{\mathfrak p_i}$ is locally nilpotent.
Lemma \ref{lemma-Noetherian-power} gives
$\mathfrak p_i^nR_{\mathfrak p_i} = 0$ for some $n \geq 1$.
By Lemma \ref{lemma-length-finite} we conclude that $R_{\mathfrak p_i}$
has finite length over $R$. Hence we conclude that $R$
is Artinian by Lemma \ref{lemma-artinian-finite-length}.

\medskip\noindent
If $R$ is an Artinian ring then by Lemma \ref{lemma-artinian-finite-length}
it is Noetherian. All of its primes are maximal by a combination
of Lemmas \ref{lemma-artinian-finite-nr-max},
\ref{lemma-artinian-radical-nilpotent} and \ref{lemma-product-local}.
\end{proof}

\noindent
In the following we will use the invariant $d(-)$ defined
in Definition \ref{definition-d}. Here is a warm up lemma.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-Noetherian-dimension-0}
Un anneau noethérien de dimension $0$ est artinien.
Réciproquement, tout anneau artinien est noethérien de dimension zéro.
\end{lemma}

\begin{proof}
Supposons que $R$ soit un anneau noethérien de dimension $0$.
D'après le Lemme \ref{lemma-Noetherian-topology}, l'espace $\Spec(R)$
est noethérien. D'après Topologie, Lemme \ref{topology-lemma-Noetherian},
$\Spec(R)$ possède un nombre fini de composantes irréductibles, disons
$\Spec(R) = Z_1 \cup \ldots \cup Z_r$.
D'après le Lemme \ref{lemma-irreducible}, chaque $Z_i = V(\mathfrak p_i)$,
où $\mathfrak p_i$ est un idéal minimal. Comme la dimension est $0$,
ces $\mathfrak p_i$ sont également maximaux. Ainsi $\Spec(R)$ est l'espace
topologique discret dont les éléments sont les $\mathfrak p_i$.
Tout élément $f$ du radical de Jacobson $\bigcap \mathfrak p_i$ est nilpotent,
car sinon $R_f$ ne serait pas l'anneau nul et nous aurions un autre idéal premier.
D'après le Lemme \ref{lemma-product-local}, $R$ est égal à
$\prod R_{\mathfrak p_i}$. Comme $R_{\mathfrak p_i}$ est lui aussi noethérien
et de dimension $0$, les arguments précédents montrent que son radical
$\mathfrak p_iR_{\mathfrak p_i}$ est localement nilpotent.
Le Lemme \ref{lemma-Noetherian-power} donne
$\mathfrak p_i^nR_{\mathfrak p_i} = 0$ pour un certain $n \geq 1$.
D'après le Lemme \ref{lemma-length-finite}, nous en concluons que
$R_{\mathfrak p_i}$ est de longueur finie sur $R$. Le Lemme
\ref{lemma-artinian-finite-length} montre alors que $R$ est artinien.

\medskip\noindent
Si $R$ est un anneau artinien, alors le Lemme
\ref{lemma-artinian-finite-length} montre qu'il est noethérien. Tous ses
idéaux premiers sont maximaux par combinaison des Lemmes
\ref{lemma-artinian-finite-nr-max},
\ref{lemma-artinian-radical-nilpotent} et \ref{lemma-product-local}.
\end{proof}

\noindent
Dans la suite, nous utiliserons l'invariant $d(-)$ défini dans la
Définition \ref{definition-d}. Commençons par un lemme préparatoire.
```

</details>

### 07 — lemma-dimension-0-d-0

Anglais L14403–14413 ; français L14209–14219.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14403) · FR-ALGEBRA-B26-CHOICE-0007.

Le cadre local noethérien et l'équivalence entre dim(R)=0 et d(R)=0 restent exacts. La preuve par longueur finie et le renvoi sont conservés ; anneau local exclut le cas nul dans la convention usuelle de Stacks.

Point particulier à relire : Le d de Stacks est le degré de χ, pas celui de φ ; la distinction du lot précédent demeure active. Aucune convention alternative n'est importée.

Règles : FR-ALGEBRA-B26-RULE-DIMENSION, FR-ALGEBRA-B26-RULE-LOCAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-dimension-0-d-0}
Let $R$ be a Noetherian local ring.
Then $\dim(R) = 0 \Leftrightarrow d(R) = 0$.
\end{lemma}

\begin{proof}
This is because $d(R) = 0$ if and only if $R$ has finite
length as an $R$-module. See Lemma \ref{lemma-artinian-finite-length}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-dimension-0-d-0}
Soit $R$ un anneau local noethérien.
Alors $\dim(R) = 0 \Leftrightarrow d(R) = 0$.
\end{lemma}

\begin{proof}
En effet, $d(R) = 0$ si et seulement si $R$ est de longueur finie
comme $R$-module. Voir le Lemme \ref{lemma-artinian-finite-length}.
\end{proof}
```

</details>

### 08 — proposition-dimension-zero-ring

Anglais L14414–14444 ; français L14220–14248.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14414) · FR-ALGEBRA-B26-CHOICE-0008.

Les dix conditions sont comparées séparément et restent toutes présentes : artinianité, noethérianité, longueur finie, produits locaux, spectre discret fini, d(R_i), nilpotence et absence d'inclusions strictes. Aucun non nul n'est ajouté à R pour réparer la réserve source exposée à part.

Point particulier à relire : L'anneau nul est artinien mais son spectre est vide, donc sa dimension officielle est −∞. La condition (2) nécessite une réserve ; on garde néanmoins le texte officiel et on explique le problème séparément, sans qualifier cette observation de nouvelle admission au registre.

Règles : FR-ALGEBRA-B26-RULE-DIMENSION, FR-ALGEBRA-B26-RULE-IDEAL, FR-ALGEBRA-B26-RULE-LOCAL, FR-ALGEBRA-B26-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{proposition}
\label{proposition-dimension-zero-ring}
Let $R$ be a ring. The following are equivalent:
\begin{enumerate}
\item $R$ is Artinian,
\item $R$ is Noetherian and $\dim(R) = 0$,
\item $R$ has finite length as a module over itself,
\item $R$ is a finite product of Artinian local rings,
\item $R$ is Noetherian and $\Spec(R)$ is a
finite discrete topological space,
\item $R$ is a finite product of Noetherian local rings
of dimension $0$,
\item $R$ is a finite product of Noetherian local rings
$R_i$ with $d(R_i) = 0$,
\item $R$ is a finite product of Noetherian local rings
$R_i$ whose maximal ideals are nilpotent,
\item $R$ is Noetherian, has finitely many maximal
ideals and its Jacobson radical ideal is nilpotent, and
\item $R$ is Noetherian and there are no strict inclusions
among its primes.
\end{enumerate}
\end{proposition}

\begin{proof}
This is a combination of Lemmas
\ref{lemma-product-local},
\ref{lemma-artinian-finite-length},
\ref{lemma-Noetherian-dimension-0}, and
\ref{lemma-dimension-0-d-0}.
\end{proof}
```

Français restauré :
```tex
\begin{proposition}
\label{proposition-dimension-zero-ring}
Soit $R$ un anneau. Les conditions suivantes sont équivalentes :
\begin{enumerate}
\item $R$ est artinien;
\item $R$ est noethérien et $\dim(R) = 0$;
\item $R$ est de longueur finie comme module sur lui-même;
\item $R$ est un produit fini d'anneaux locaux artiniens;
\item $R$ est noethérien et $\Spec(R)$ est un espace topologique discret fini;
\item $R$ est un produit fini d'anneaux locaux noethériens de dimension $0$;
\item $R$ est un produit fini d'anneaux locaux noethériens $R_i$
tels que $d(R_i) = 0$;
\item $R$ est un produit fini d'anneaux locaux noethériens $R_i$
dont les idéaux maximaux sont nilpotents;
\item $R$ est noethérien, possède un nombre fini d'idéaux maximaux
et son radical de Jacobson est nilpotent; et
\item $R$ est noethérien et il n'existe aucune inclusion stricte entre
ses idéaux premiers.
\end{enumerate}
\end{proposition}

\begin{proof}
C'est une combinaison des Lemmes
\ref{lemma-product-local},
\ref{lemma-artinian-finite-length},
\ref{lemma-Noetherian-dimension-0} et
\ref{lemma-dimension-0-d-0}.
\end{proof}
```

</details>

### 09 — lemma-height-1

Anglais L14445–14519 ; français L14249–14324.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14445) · FR-ALGEBRA-B26-CHOICE-0009.

Les cinq conditions et leur ordre restent identiques ; la non-nilpotence de x est présente dans les deux conditions nécessaires. La preuve par évitement, l'idéal à un générateur, la borne de longueur et la contradiction par deux idéaux premiers distincts sont conservées. De degré strictement inférieur ($ < 1$) devient de degré $ < 1$ : la comparaison est portée directement par la formule, sans comparatif français suspendu ni signe modifié.

Point particulier à relire : Les deux régions length/longueur de cette section sont des traductions préexistantes du texte lisible de formules. La flèche non étiquetée de la suite exacte reste non étiquetée ; aucune multiplication par x supplémentaire n'est dessinée dans la traduction.

Règles : FR-ALGEBRA-B26-RULE-DIMENSION, FR-ALGEBRA-B26-RULE-IDEAL, FR-ALGEBRA-B26-RULE-PARAMETER, FR-ALGEBRA-B26-RULE-LOCAL, FR-ALGEBRA-B26-RULE-DEGREE, FR-ALGEBRA-B26-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-height-1}
Let $R$ be a local Noetherian ring.
The following are equivalent:
\begin{enumerate}
\item
\label{item-dim-1}
$\dim(R) = 1$,
\item
\label{item-d-1}
$d(R) = 1$,
\item
\label{item-Vx}
there exists an $x \in \mathfrak m$, $x$ not nilpotent
such that $V(x) = \{\mathfrak m\}$,
\item
\label{item-x}
there exists an $x \in \mathfrak m$, $x$ not nilpotent
such that $\mathfrak m = \sqrt{(x)}$, and
\item
\label{item-ideal-1}
there exists an ideal of definition generated by $1$ element,
and no ideal of definition is generated by $0$ elements.
\end{enumerate}
\end{lemma}

\begin{proof}
First, assume that $\dim(R) = 1$.
Let $\mathfrak p_i$ be the minimal primes of $R$.
Because the dimension is $1$ the only other prime of $R$
is $\mathfrak m$.
According to Lemma \ref{lemma-Noetherian-irreducible-components}
there are finitely many. Hence we can find $x \in \mathfrak m$,
$x \not \in \mathfrak p_i$, see Lemma \ref{lemma-silly}.
Thus the only prime containing $x$ is $\mathfrak m$ and
hence (\ref{item-Vx}).

\medskip\noindent
If (\ref{item-Vx}) then $\mathfrak m = \sqrt{(x)}$ by
Lemma \ref{lemma-Zariski-topology}, and hence (\ref{item-x}).
The converse is clear as well.
The equivalence of (\ref{item-x}) and (\ref{item-ideal-1}) follows
from directly the definitions.

\medskip\noindent
Assume (\ref{item-ideal-1}).
Let $I = (x)$ be an ideal of definition.
Note that $I^n/I^{n + 1}$ is a quotient of $R/I$ via multiplication
by $x^n$ and hence $\text{length}_R(I^n/I^{n + 1})$ is bounded.
Thus $d(R) = 0$ or $d(R) = 1$, but $d(R) = 0$ is excluded
by the assumption that $0$ is not an ideal of definition.

\medskip\noindent
Assume (\ref{item-d-1}). To get a contradiction, assume there
exist primes $\mathfrak p \subset \mathfrak q \subset \mathfrak m$,
with both inclusions strict. Pick some ideal of definition $I \subset R$.
We will repeatedly use
Lemma \ref{lemma-hilbert-ses-chi}. First of all
it implies, via the exact sequence
$0 \to \mathfrak p \to R \to R/\mathfrak p \to 0$,
that $d(R/\mathfrak p) \leq 1$. But it clearly cannot
be zero. Pick $x\in \mathfrak q$, $x\not \in \mathfrak p$.
Consider the short exact sequence
$$
0 \to R/\mathfrak p \to R/\mathfrak p \to R/(xR + \mathfrak p) \to 0.
$$
This implies that $\chi_{I, R/\mathfrak p} - \chi_{I, R/\mathfrak p}
- \chi_{I, R/(xR + \mathfrak p)} = - \chi_{I, R/(xR + \mathfrak p)}$
has degree $ < 1$. In other words, $d(R/(xR + \mathfrak p)) = 0$,
and hence $\dim(R/(xR + \mathfrak p)) = 0$, by
Lemma \ref{lemma-dimension-0-d-0}. But $R/(xR + \mathfrak p)$
has the distinct primes $\mathfrak q/(xR + \mathfrak p)$ and
$\mathfrak m/(xR + \mathfrak p)$ which gives the desired contradiction.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-height-1}
Soit $R$ un anneau local noethérien.
Les conditions suivantes sont équivalentes :
\begin{enumerate}
\item
\label{item-dim-1}
$\dim(R) = 1$;
\item
\label{item-d-1}
$d(R) = 1$;
\item
\label{item-Vx}
il existe $x \in \mathfrak m$, avec $x$ non nilpotent, tel que
$V(x) = \{\mathfrak m\}$;
\item
\label{item-x}
il existe $x \in \mathfrak m$, avec $x$ non nilpotent, tel que
$\mathfrak m = \sqrt{(x)}$; et
\item
\label{item-ideal-1}
il existe un idéal de définition engendré par $1$ élément,
et aucun idéal de définition n'est engendré par $0$ élément.
\end{enumerate}
\end{lemma}

\begin{proof}
Supposons d'abord que $\dim(R) = 1$.
Soient $\mathfrak p_i$ les idéaux premiers minimaux de $R$.
Comme la dimension est $1$, le seul autre idéal premier de $R$ est
$\mathfrak m$.
D'après le Lemme \ref{lemma-Noetherian-irreducible-components},
ils sont en nombre fini. Nous pouvons donc trouver $x \in \mathfrak m$,
$x \not \in \mathfrak p_i$; voir le Lemme \ref{lemma-silly}.
Le seul idéal premier contenant $x$ est ainsi $\mathfrak m$, d'où
(\ref{item-Vx}).

\medskip\noindent
Si (\ref{item-Vx}) est satisfaite, alors
$\mathfrak m = \sqrt{(x)}$ d'après le Lemme
\ref{lemma-Zariski-topology}, d'où (\ref{item-x}).
La réciproque est également claire.
L'équivalence entre (\ref{item-x}) et (\ref{item-ideal-1}) découle
directement des définitions.

\medskip\noindent
Supposons (\ref{item-ideal-1}).
Soit $I = (x)$ un idéal de définition.
Remarquons que $I^n/I^{n + 1}$ est un quotient de $R/I$ par la multiplication
par $x^n$, et donc que $\text{longueur}_R(I^n/I^{n + 1})$ est bornée.
Ainsi $d(R) = 0$ ou $d(R) = 1$, mais $d(R) = 0$ est exclu par
l'hypothèse selon laquelle $0$ n'est pas un idéal de définition.

\medskip\noindent
Supposons (\ref{item-d-1}). Pour obtenir une contradiction, supposons qu'il
existe des idéaux premiers $\mathfrak p \subset \mathfrak q \subset \mathfrak m$,
les deux inclusions étant strictes. Choisissons un idéal de définition
$I \subset R$. Nous utiliserons plusieurs fois le
Lemme \ref{lemma-hilbert-ses-chi}. Tout d'abord, appliqué à la suite exacte
$0 \to \mathfrak p \to R \to R/\mathfrak p \to 0$,
il implique que $d(R/\mathfrak p) \leq 1$. Mais cette valeur ne peut
évidemment pas être nulle. Choisissons $x\in \mathfrak q$,
$x\not \in \mathfrak p$. Considérons la suite exacte courte
$$
0 \to R/\mathfrak p \to R/\mathfrak p \to R/(xR + \mathfrak p) \to 0.
$$
Cela implique que $\chi_{I, R/\mathfrak p} - \chi_{I, R/\mathfrak p}
- \chi_{I, R/(xR + \mathfrak p)} = - \chi_{I, R/(xR + \mathfrak p)}$
est de degré $ < 1$. Autrement dit,
$d(R/(xR + \mathfrak p)) = 0$, et donc
$\dim(R/(xR + \mathfrak p)) = 0$, d'après le
Lemme \ref{lemma-dimension-0-d-0}. Mais $R/(xR + \mathfrak p)$ possède les
idéaux premiers distincts $\mathfrak q/(xR + \mathfrak p)$ et
$\mathfrak m/(xR + \mathfrak p)$, ce qui donne la contradiction cherchée.
\end{proof}
```

</details>

### 10 — proposition-dimension

Anglais L14520–14613 ; français L14325–14417.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14520) · FR-ALGEBRA-B26-CHOICE-0010.

Les trois caractérisations et les inégalités cycliques dim(R)≥d′(R)≥d(R)≥dim(R) sont fidèles. La récurrence, les monômes comptés par le binomial, les suites exactes et la chaîne quotient sont comparés ligne par ligne. Le degré $ < d$ est rendu directement, sans le comparatif français suspendu. Dans le paragraphe suivant, éléments pour variables est une traduction contextuelle des générateurs, non une nouvelle assertion sur l'indépendance algébrique.

Point particulier à relire : Les longueurs des chaînes et les degrés restent strictement les mêmes. Les questions de finitude traitées par la preuve source ne sont pas remplacées par une autre preuve. La traduction éléments explicite le sens de générateurs du contexte, à distinguer d'une variable formelle.

Règles : FR-ALGEBRA-B26-RULE-DIMENSION, FR-ALGEBRA-B26-RULE-IDEAL, FR-ALGEBRA-B26-RULE-PARAMETER, FR-ALGEBRA-B26-RULE-LOCAL, FR-ALGEBRA-B26-RULE-DEGREE, FR-ALGEBRA-B26-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{proposition}
\label{proposition-dimension}
Let $R$ be a local Noetherian ring. Let $d \geq 0$ be an integer.
The following are equivalent:
\begin{enumerate}
\item
\label{item-dim-d}
$\dim(R) = d$,
\item
\label{item-d-d}
$d(R) = d$,
\item
\label{item-ideal-d}
there exists an ideal of definition generated by $d$ elements,
and no ideal of definition is generated by fewer than $d$ elements.
\end{enumerate}
\end{proposition}

\begin{proof}
This proof is really just the same as the proof of Lemma
\ref{lemma-height-1}. We will prove the proposition by induction
on $d$. By Lemmas \ref{lemma-dimension-0-d-0} and \ref{lemma-height-1}
we may assume that $d > 1$. Denote the minimal number of
generators for an ideal of definition of $R$ by $d'(R)$.
We will prove the inequalities
$\dim(R) \geq d'(R) \geq d(R) \geq \dim(R)$,
and hence they are all equal.

\medskip\noindent
First, assume that $\dim(R) = d$.
Let $\mathfrak p_i$ be the minimal primes of $R$.
According to Lemma \ref{lemma-Noetherian-irreducible-components}
there are finitely many. Hence we can find $x \in \mathfrak m$,
$x \not \in \mathfrak p_i$, see Lemma \ref{lemma-silly}.
Note that every maximal chain of primes starts with some $\mathfrak p_i$,
hence the dimension of $R/xR$ is at most $d-1$. By induction
there are $x_2, \ldots, x_d$ which generate an ideal of definition
in $R/xR$. Hence $R$ has an ideal of definition generated
by (at most) $d$ elements.

\medskip\noindent
Assume $d'(R) = d$. Let $I = (x_1, \ldots, x_d)$ be an ideal
of definition. Note that $I^n/I^{n + 1}$ is a quotient of a direct
sum of $\binom{d + n - 1}{d - 1}$ copies $R/I$ via multiplication
by all degree $n$ monomials in $x_1, \ldots, x_d$.
Hence $\text{length}_R(I^n/I^{n + 1})$ is bounded by a polynomial
of degree $d-1$. Thus $d(R) \leq d$.

\medskip\noindent
Assume $d(R) = d$. Consider a chain of primes
$\mathfrak p \subset \mathfrak q \subset
\mathfrak q_2 \subset \ldots \subset \mathfrak q_e = \mathfrak m$,
with all inclusions strict, and $e \geq 2$.
Pick some ideal of definition $I \subset R$.
We will repeatedly use
Lemma \ref{lemma-hilbert-ses-chi}. First of all
it implies, via the exact sequence
$0 \to \mathfrak p \to R \to R/\mathfrak p \to 0$,
that $d(R/\mathfrak p) \leq d$. But it clearly cannot
be zero. Pick $x\in \mathfrak q$, $x\not \in \mathfrak p$.
Consider the short exact sequence
$$
0 \to R/\mathfrak p \to R/\mathfrak p \to R/(xR + \mathfrak p) \to 0.
$$
This implies that $\chi_{I, R/\mathfrak p} - \chi_{I, R/\mathfrak p}
- \chi_{I, R/(xR + \mathfrak p)} = - \chi_{I, R/(xR + \mathfrak p)}$
has degree $ < d$. In other words, $d(R/(xR + \mathfrak p)) \leq d - 1$,
and hence $\dim(R/(xR + \mathfrak p)) \leq d - 1$, by
induction. Now $R/(xR + \mathfrak p)$ has the chain of prime ideals
$\mathfrak q/(xR + \mathfrak p) \subset \mathfrak q_2/(xR + \mathfrak p)
\subset \ldots \subset \mathfrak q_e/(xR + \mathfrak p)$ which gives
$e - 1 \leq d - 1$. Since we started with an arbitrary chain of
primes this proves that $\dim(R) \leq d(R)$.

\medskip\noindent
Reading back the reader will see we proved the circular
inequalities as desired.
\end{proof}

\noindent
Let $(R, \mathfrak m)$ be a Noetherian local ring.
From the above it is clear that $\mathfrak m$ cannot be
generated by fewer than $\dim(R)$ variables.
By Nakayama's Lemma \ref{lemma-NAK} the minimal number
of generators of $\mathfrak m$ equals $\dim_{\kappa(\mathfrak m)}
\mathfrak m/\mathfrak m^2$. Hence we have the following
fundamental inequality
$$
\dim(R) \leq \dim_{\kappa(\mathfrak m)} \mathfrak m/\mathfrak m^2.
$$
It turns out that the rings where equality holds
have a lot of good properties. They are called
regular local rings.
```

Français restauré :
```tex
\begin{proposition}
\label{proposition-dimension}
Soit $R$ un anneau local noethérien. Soit $d \geq 0$ un entier.
Les conditions suivantes sont équivalentes :
\begin{enumerate}
\item
\label{item-dim-d}
$\dim(R) = d$;
\item
\label{item-d-d}
$d(R) = d$;
\item
\label{item-ideal-d}
il existe un idéal de définition engendré par $d$ éléments,
et aucun idéal de définition n'est engendré par moins de $d$ éléments.
\end{enumerate}
\end{proposition}

\begin{proof}
Cette démonstration est essentiellement la même que celle du Lemme
\ref{lemma-height-1}. Nous procédons par récurrence sur $d$.
D'après les Lemmes \ref{lemma-dimension-0-d-0} et \ref{lemma-height-1},
nous pouvons supposer que $d > 1$. Notons le nombre minimal de
générateurs d'un idéal de définition de $R$ par $d'(R)$.
Nous allons démontrer les inégalités
$\dim(R) \geq d'(R) \geq d(R) \geq \dim(R)$,
ce qui montrera que ces nombres sont tous égaux.

\medskip\noindent
Supposons d'abord que $\dim(R) = d$.
Soient $\mathfrak p_i$ les idéaux premiers minimaux de $R$.
D'après le Lemme \ref{lemma-Noetherian-irreducible-components},
ils sont en nombre fini. Nous pouvons donc trouver $x \in \mathfrak m$,
$x \not \in \mathfrak p_i$; voir le Lemme \ref{lemma-silly}.
Toute chaîne maximale d'idéaux premiers commence par un certain
$\mathfrak p_i$; la dimension de $R/xR$ est donc au plus $d-1$.
Par récurrence, il existe $x_2, \ldots, x_d$ qui engendrent un idéal de
définition dans $R/xR$. Ainsi $R$ possède un idéal de définition engendré
par (au plus) $d$ éléments.

\medskip\noindent
Supposons $d'(R) = d$. Soit $I = (x_1, \ldots, x_d)$ un idéal de définition.
Remarquons que $I^n/I^{n + 1}$ est un quotient d'une somme directe de
$\binom{d + n - 1}{d - 1}$ copies de $R/I$, par multiplication par tous les
monômes de degré $n$ en $x_1, \ldots, x_d$.
Ainsi $\text{longueur}_R(I^n/I^{n + 1})$ est bornée par un polynôme
de degré $d-1$. Donc $d(R) \leq d$.

\medskip\noindent
Supposons $d(R) = d$. Considérons une chaîne d'idéaux premiers
$\mathfrak p \subset \mathfrak q \subset
\mathfrak q_2 \subset \ldots \subset \mathfrak q_e = \mathfrak m$,
où toutes les inclusions sont strictes et $e \geq 2$.
Choisissons un idéal de définition $I \subset R$.
Nous utiliserons plusieurs fois le Lemme \ref{lemma-hilbert-ses-chi}.
Tout d'abord, appliqué à la suite exacte
$0 \to \mathfrak p \to R \to R/\mathfrak p \to 0$,
il implique que $d(R/\mathfrak p) \leq d$. Mais cette valeur ne peut
évidemment pas être nulle. Choisissons $x\in \mathfrak q$,
$x\not \in \mathfrak p$. Considérons la suite exacte courte
$$
0 \to R/\mathfrak p \to R/\mathfrak p \to R/(xR + \mathfrak p) \to 0.
$$
Cela implique que $\chi_{I, R/\mathfrak p} - \chi_{I, R/\mathfrak p}
- \chi_{I, R/(xR + \mathfrak p)} = - \chi_{I, R/(xR + \mathfrak p)}$
est de degré $ < d$. Autrement dit,
$d(R/(xR + \mathfrak p)) \leq d - 1$, et donc
$\dim(R/(xR + \mathfrak p)) \leq d - 1$, par récurrence.
Or $R/(xR + \mathfrak p)$ possède la chaîne d'idéaux premiers
$\mathfrak q/(xR + \mathfrak p) \subset \mathfrak q_2/(xR + \mathfrak p)
\subset \ldots \subset \mathfrak q_e/(xR + \mathfrak p)$, ce qui donne
$e - 1 \leq d - 1$. Comme nous sommes partis d'une chaîne arbitraire
d'idéaux premiers, cela prouve que $\dim(R) \leq d(R)$.

\medskip\noindent
En relisant la démonstration, le lecteur constatera que nous avons obtenu
les inégalités cycliques voulues.
\end{proof}

\noindent
Soit $(R, \mathfrak m)$ un anneau local noethérien.
D'après ce qui précède, il est clair que $\mathfrak m$ ne peut être
engendré par moins de $\dim(R)$ éléments.
D'après le lemme de Nakayama \ref{lemma-NAK}, le nombre minimal de
générateurs de $\mathfrak m$ est égal à $\dim_{\kappa(\mathfrak m)}
\mathfrak m/\mathfrak m^2$. Nous avons donc l'inégalité fondamentale
$$
\dim(R) \leq \dim_{\kappa(\mathfrak m)} \mathfrak m/\mathfrak m^2.
$$
Il se trouve que les anneaux pour lesquels l'égalité est vérifiée
possèdent de nombreuses bonnes propriétés. On les appelle anneaux locaux
réguliers.
```

</details>

### 11 — definition-regular-local

Anglais L14614–14632 ; français L14418–14436.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14614) · FR-ALGEBRA-B26-CHOICE-0011.

Système de paramètres, anneau local régulier et idéal de définition concordent avec les passages lus de Peskine et Ducros. La suite a exactement d termes ; la seconde condition impose que ces termes engendrent m, pas seulement un idéal m-primaire. Le système régulier de paramètres n'est pas confondu avec une suite régulière quelconque.

Point particulier à relire : Les pages lues attestent système de paramètres et la définition d'anneau local régulier. Le libellé système régulier de paramètres est justifié ici par la définition officielle, sans inventer une attestation exacte externe.

Règles : FR-ALGEBRA-B26-RULE-DIMENSION, FR-ALGEBRA-B26-RULE-IDEAL, FR-ALGEBRA-B26-RULE-PARAMETER, FR-ALGEBRA-B26-RULE-LOCAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-regular-local}
Let $(R, \mathfrak m)$ be a Noetherian local ring of dimension $d$.
\begin{enumerate}
\item A {\it system of parameters of $R$} is a sequence of elements
$x_1, \ldots, x_d \in \mathfrak m$ which generates an ideal of
definition of $R$,
\item if there exist $x_1, \ldots, x_d \in \mathfrak m$
such that $\mathfrak m = (x_1, \ldots, x_d)$ then we call
$R$ a {\it regular local ring} and $x_1, \ldots, x_d$ a {\it regular
system of parameters}.
\end{enumerate}
\end{definition}

\noindent
The following lemmas are clear from the proofs of the
lemmas and proposition above, but we spell them out so we have
convenient references.
```

Français restauré :
```tex
\begin{definition}
\label{definition-regular-local}
Soit $(R, \mathfrak m)$ un anneau local noethérien de dimension $d$.
\begin{enumerate}
\item Un {\it système de paramètres de $R$} est une suite d'éléments
$x_1, \ldots, x_d \in \mathfrak m$ qui engendre un idéal de définition
de $R$;
\item s'il existe $x_1, \ldots, x_d \in \mathfrak m$ tels que
$\mathfrak m = (x_1, \ldots, x_d)$, alors nous appelons $R$ un
{\it anneau local régulier}, et $x_1, \ldots, x_d$ un {\it système
régulier de paramètres}.
\end{enumerate}
\end{definition}

\noindent
Les lemmes suivants ressortent clairement des démonstrations des lemmes
et de la proposition ci-dessus, mais nous les énonçons explicitement afin
de disposer de références commodes.
```

</details>

### 12 — lemma-minimal-over-1

Anglais L14633–14663 ; français L14437–14468.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14633) · FR-ALGEBRA-B26-CHOICE-0012.

Minimal au-dessus de (x) conserve la minimalité parmi les idéaux premiers contenant cet idéal. La preuve développe naturellement minimal over x en minimal parmi les idéaux premiers contenant x ; contrairement au minimal ideal isolé plus haut, cette formule source désigne déjà la notion de minimalité au-dessus d'un idéal. Les cas nilpotent et non nilpotent, les hauteurs 0/1 et le quotient R/p restent exacts.

Point particulier à relire : La locution minimal au-dessus est justifiée directement par la définition source et la preuve de localisation ; aucune citation externe exacte de cette locution n'a été relevée dans ces pages.

Règles : FR-ALGEBRA-B26-RULE-DIMENSION, FR-ALGEBRA-B26-RULE-IDEAL, FR-ALGEBRA-B26-RULE-LOCAL, FR-ALGEBRA-B26-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-minimal-over-1}
Let $R$ be a Noetherian ring. Let $x \in R$.
\begin{enumerate}
\item If $\mathfrak p$ is minimal over $(x)$
then the height of $\mathfrak p$ is $0$ or $1$.
\item If $\mathfrak p, \mathfrak q \in \Spec(R)$ and $\mathfrak q$
is minimal over $(\mathfrak p, x)$, then there is no prime strictly
between $\mathfrak p$ and $\mathfrak q$.
\end{enumerate}
\end{lemma}

\begin{proof}
Proof of (1). If $\mathfrak p$ is minimal over $x$, then the only
prime ideal of $R_\mathfrak p$ containing $x$ is the maximal ideal
$\mathfrak p R_\mathfrak p$. This is true because the primes of
$R_\mathfrak p$ correspond $1$-to-$1$ with the primes of $R$ contained
in $\mathfrak p$, see Lemma \ref{lemma-spec-localization}.
Hence Lemma \ref{lemma-height-1} shows $\dim(R_\mathfrak p) = 1$
if $x$ is not nilpotent in $R_\mathfrak p$. Of course, if
$x$ is nilpotent in $R_\mathfrak p$ the argument gives that
$\mathfrak pR_\mathfrak p$ is the only prime ideal and we see
that the height is $0$.

\medskip\noindent
Proof of (2). By part (1) we see that $\mathfrak q/\mathfrak p$
is a prime of height $1$ or $0$ in $R/\mathfrak p$. This immediately
implies there cannot be a prime strictly between $\mathfrak p$
and $\mathfrak q$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-minimal-over-1}
Soit $R$ un anneau noethérien. Soit $x \in R$.
\begin{enumerate}
\item Si $\mathfrak p$ est minimal au-dessus de $(x)$,
alors la hauteur de $\mathfrak p$ est $0$ ou $1$.
\item Si $\mathfrak p, \mathfrak q \in \Spec(R)$ et si $\mathfrak q$
est minimal au-dessus de $(\mathfrak p, x)$, alors il n'existe aucun idéal
premier strictement compris entre $\mathfrak p$ et $\mathfrak q$.
\end{enumerate}
\end{lemma}

\begin{proof}
Démonstration de (1). Si $\mathfrak p$ est minimal parmi les idéaux premiers
contenant $x$, alors le seul idéal premier de $R_\mathfrak p$ contenant $x$
est l'idéal maximal $\mathfrak p R_\mathfrak p$. En effet, les idéaux premiers
de $R_\mathfrak p$ correspondent de façon $1$ à $1$ aux idéaux premiers de
$R$ contenus dans $\mathfrak p$; voir le Lemme
\ref{lemma-spec-localization}.
Le Lemme \ref{lemma-height-1} montre donc que
$\dim(R_\mathfrak p) = 1$ si $x$ n'est pas nilpotent dans
$R_\mathfrak p$. Bien entendu, si $x$ est nilpotent dans
$R_\mathfrak p$, l'argument montre que $\mathfrak pR_\mathfrak p$ est le
seul idéal premier et que la hauteur est $0$.

\medskip\noindent
Démonstration de (2). D'après la partie (1),
$\mathfrak q/\mathfrak p$ est un idéal premier de hauteur $1$ ou $0$
dans $R/\mathfrak p$. Il en résulte immédiatement qu'il ne peut exister
d'idéal premier strictement compris entre $\mathfrak p$ et $\mathfrak q$.
\end{proof}
```

</details>

### 13 — lemma-minimal-over-r

Anglais L14664–14692 ; français L14469–14498.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14664) · FR-ALGEBRA-B26-CHOICE-0013.

Les deux bornes sont préservées : hauteur au plus r et longueur de toute chaîne intermédiaire au plus r. Le localisé et le quotient correspondent aux mêmes objets. Aucun idéal premier intermédiaire ni générateur n'est supprimé ; minimal au-dessus conserve la notion technique source.

Point particulier à relire : La borne ≤r n'est pas une égalité et ne requiert pas r générateurs minimaux. La même justification source couvre chaque occurrence en contexte.

Règles : FR-ALGEBRA-B26-RULE-DIMENSION, FR-ALGEBRA-B26-RULE-IDEAL, FR-ALGEBRA-B26-RULE-LOCAL, FR-ALGEBRA-B26-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-minimal-over-r}
Let $R$ be a Noetherian ring. Let $f_1, \ldots, f_r \in R$.
\begin{enumerate}
\item If $\mathfrak p$ is minimal over $(f_1, \ldots, f_r)$
then the height of $\mathfrak p$ is $\leq r$.
\item If $\mathfrak p, \mathfrak q \in \Spec(R)$ and
$\mathfrak q$ is minimal over $(\mathfrak p, f_1, \ldots, f_r)$,
then every chain of primes between $\mathfrak p$ and $\mathfrak q$
has length at most $r$.
\end{enumerate}
\end{lemma}

\begin{proof}
Proof of (1). If $\mathfrak p$ is minimal over $f_1, \ldots, f_r$,
then the only prime ideal of $R_\mathfrak p$ containing $f_1, \ldots, f_r$
is the maximal ideal $\mathfrak p R_\mathfrak p$. This is true because
the primes of $R_\mathfrak p$ correspond $1$-to-$1$ with the primes of
$R$ contained in $\mathfrak p$, see Lemma \ref{lemma-spec-localization}.
Hence Proposition \ref{proposition-dimension} shows
$\dim(R_\mathfrak p) \leq r$.

\medskip\noindent
Proof of (2). By part (1) we see that $\mathfrak q/\mathfrak p$
is a prime of height $\leq r$. This immediately
implies the statement about chains of primes between $\mathfrak p$
and $\mathfrak q$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-minimal-over-r}
Soit $R$ un anneau noethérien. Soient $f_1, \ldots, f_r \in R$.
\begin{enumerate}
\item Si $\mathfrak p$ est minimal au-dessus de $(f_1, \ldots, f_r)$,
alors la hauteur de $\mathfrak p$ est $\leq r$.
\item Si $\mathfrak p, \mathfrak q \in \Spec(R)$ et si
$\mathfrak q$ est minimal au-dessus de $(\mathfrak p, f_1, \ldots, f_r)$,
alors toute chaîne d'idéaux premiers entre $\mathfrak p$ et
$\mathfrak q$ est de longueur au plus $r$.
\end{enumerate}
\end{lemma}

\begin{proof}
Démonstration de (1). Si $\mathfrak p$ est minimal parmi les idéaux premiers
contenant $f_1, \ldots, f_r$, alors le seul idéal premier de
$R_\mathfrak p$ contenant $f_1, \ldots, f_r$ est l'idéal maximal
$\mathfrak p R_\mathfrak p$. En effet, les idéaux premiers de
$R_\mathfrak p$ correspondent de façon $1$ à $1$ aux idéaux premiers de
$R$ contenus dans $\mathfrak p$; voir le Lemme
\ref{lemma-spec-localization}. La Proposition \ref{proposition-dimension}
montre donc que $\dim(R_\mathfrak p) \leq r$.

\medskip\noindent
Démonstration de (2). D'après la partie (1),
$\mathfrak q/\mathfrak p$ est un idéal premier de hauteur $\leq r$.
Cela implique immédiatement l'assertion sur les chaînes d'idéaux premiers
entre $\mathfrak p$ et $\mathfrak q$.
\end{proof}
```

</details>

### 14 — lemma-one-equation

Anglais L14693–14711 ; français L14499–14518.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14693) · FR-ALGEBRA-B26-CHOICE-0014.

La baisse de dimension après quotient par x est au plus une unité. L'égalité est garantie lorsque x évite tous les premiers minimaux ; non-diviseur de zéro reste seulement un exemple de cette hypothèse. Les relèvements du système de paramètres et la preuve par prolongement des chaînes gardent leur rôle source.

Point particulier à relire : Non-diviseur de zéro est retenu conformément au registre déjà consulté dans les lots antérieurs ; aucune nouvelle attestation de ce libellé n'est prétendue dans les deux références de ce lot.

Règles : FR-ALGEBRA-B26-RULE-DIMENSION, FR-ALGEBRA-B26-RULE-IDEAL, FR-ALGEBRA-B26-RULE-PARAMETER, FR-ALGEBRA-B26-RULE-LOCAL, FR-ALGEBRA-B26-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-one-equation}
Suppose that $R$ is a Noetherian local ring and $x\in \mathfrak m$ an
element of its maximal ideal. Then $\dim R \leq \dim R/xR + 1$.
If $x$ is not contained in any of the minimal primes of $R$
then equality holds. (For example if $x$ is a nonzerodivisor.)
\end{lemma}

\begin{proof}
If $x_1, \ldots, x_{\dim R/xR} \in R$ map to elements of $R/xR$ which
generate an ideal of definition for $R/xR$, then $x, x_1, \ldots,
x_{\dim R/xR}$ generate an ideal of definition for $R$. Hence
the inequality by Proposition \ref{proposition-dimension}.
On the other hand, if $x$ is not contained in any minimal
prime of $R$, then the chains of primes in $R/xR$ all give
rise to chains in $R$ which are at least one step away
from being maximal.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-one-equation}
Supposons que $R$ soit un anneau local noethérien et que
$x\in \mathfrak m$ soit un élément de son idéal maximal. Alors
$\dim R \leq \dim R/xR + 1$.
Si $x$ n'appartient à aucun des idéaux premiers minimaux de $R$,
alors il y a égalité. (Par exemple, si $x$ est un non-diviseur de zéro.)
\end{lemma}

\begin{proof}
Si $x_1, \ldots, x_{\dim R/xR} \in R$ s'envoient sur des éléments de
$R/xR$ qui engendrent un idéal de définition de $R/xR$, alors
$x, x_1, \ldots, x_{\dim R/xR}$ engendrent un idéal de définition de $R$.
L'inégalité résulte donc de la Proposition \ref{proposition-dimension}.
D'autre part, si $x$ n'appartient à aucun idéal premier minimal de $R$,
alors toute chaîne d'idéaux premiers de $R/xR$ donne naissance à une
chaîne dans $R$ à laquelle il manque encore au moins une étape pour être
maximale.
\end{proof}
```

</details>

### 15 — lemma-elements-generate-ideal-definition

Anglais L14712–14730 ; français L14519–14532.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14712) · FR-ALGEBRA-B26-CHOICE-0015.

Les d éléments engendrent un idéal de définition, avec d=dim(R). Le français conserve pour tout i=1,…,d et la dimension d−i du quotient successif. La preuve abrégée propose les mêmes deux voies et les mêmes renvois ; aucune démonstration supplémentaire n'est introduite.

Point particulier à relire : Le contrôle porte sur le système complet de paramètres et tous les quotients successifs. Le mot régulier n'est pas ajouté.

Règles : FR-ALGEBRA-B26-RULE-IDEAL, FR-ALGEBRA-B26-RULE-PARAMETER, FR-ALGEBRA-B26-RULE-LOCAL, FR-ALGEBRA-B26-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-elements-generate-ideal-definition}
Let $(R, \mathfrak m)$ be a Noetherian local ring.
Suppose $x_1, \ldots, x_d \in \mathfrak m$ generate an
ideal of definition and $d = \dim(R)$. Then
$\dim(R/(x_1, \ldots, x_i)) = d - i$ for all $i = 1, \ldots, d$.
\end{lemma}

\begin{proof}
Follows either from the proof of Proposition \ref{proposition-dimension},
or by using induction on $d$ and Lemma \ref{lemma-one-equation}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-elements-generate-ideal-definition}
Soit $(R, \mathfrak m)$ un anneau local noethérien.
Supposons que $x_1, \ldots, x_d \in \mathfrak m$ engendrent un idéal
de définition et que $d = \dim(R)$. Alors
$\dim(R/(x_1, \ldots, x_i)) = d - i$ pour tout $i = 1, \ldots, d$.
\end{lemma}

\begin{proof}
Cela découle soit de la démonstration de la Proposition
\ref{proposition-dimension}, soit d'une récurrence sur $d$ utilisant le
Lemme \ref{lemma-one-equation}.
\end{proof}
```

</details>

## Contrôles et suite

Les 260 régions mathématiques correspondent exactement après deux exceptions linguistiques préexistantes, liées à leurs positions et non remplacées indistinctement. Le préfixe de 10 403 régions passe avec trente-neuf exceptions linguistiques au total ; les différences sont vérifiées dans leur ordre et avec leurs multiplicités exactes.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items restent identiques. Aucune citation ni titre facultatif ne figure dans ce lot. Les opérations inverses retrouvent le lot précédent puis tous les octets du témoin public préservé. Préfixe déjà relu et suffixe encore non relu sont inchangés.

Les 530 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Applications de la théorie de la dimension, anglais L14731 / français L14533. Aucun PDF nouveau ni publication ; restauration globale en cours.

