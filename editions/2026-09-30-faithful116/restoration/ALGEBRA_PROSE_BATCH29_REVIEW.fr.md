# Idéaux premiers associés

## Résultat et portée

La section complète est comparée : anglais L15099–15541 (443 lignes), français L14870–15296 (427 lignes), vingt et une paires complètes. 175 occurrences de règles sont contextualisées, non un décompte de tous les mots. Couverture continue : 63 sections, 564 paires et 5465 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Deux phrases françaises sont réparées : soit au lieu de est après un élément tel que ; l’application reçoit le nom qui permet l’accord injective. Démonstration omise remplace aussi Omis, conformément aux passages déjà normalisés. Aucun résultat ou symbole mathématique ne change.

L’association, les annulateurs, le support, les filtrations, la localisation, la contraction et les diviseurs de zéro sont comparés intégralement. La tournure dans M est réellement attestée : le soupçon de registre est un faux positif rejeté, non un motif de normalisation gratuite. Les hypothèses noethériennes et de type fini du canon ne sont pas importées dans les assertions générales de Stacks.

Lecture produite par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. Le canon est consulté pour cette révision rétrospective, non présenté comme consulté lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch29.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH28_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH29_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH29_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH29_OCCURRENCES.json) · [Opérations](ALGEBRA_PROSE_BATCH29_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH29_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH29_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH29_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH29_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH29_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Christian Peskine — Introduction algébrique à la géométrie projective

[Source consultée](https://perso.univ-rennes1.fr/matthieu.romagny/M2_0708/bouquin.pdf) · [Fichier conservé](canon-consulted/fr-algebra/peskine-geometrie-projective-2007.pdf)

Pages PDF 37, 84, 86, 138 et 144 / imprimées 36, 83, 85, 137 et 143 entièrement lues. Définition 5.2, proposition 5.6, corollaire 5.7, proposition 16.1 et définition 16.3 particulièrement consultés. Page PDF 138 rendue et inspectée visuellement.

Attestations courtes : « Idéaux premiers associés », « annulateur », « non diviseur de 0 dans M ».

Atteste premier associé, annulateur et le registre dans M pour l'action d'un élément sur un module. Le critère par injectivité et les premiers associés donne le sens précis retenu.

Limites : Peskine énonce ici des résultats pour des modules de type fini sur des anneaux noethériens. Ces hypothèses ne sont pas importées dans les assertions générales de Stacks. La réparation des modes verbaux et de l'accord injective repose sur la phrase française et ses objets, pas sur une attestation inventée de chaque phrase.

SHA-256 : C84D597457282B22B993F523791F4A3E391A74554FF76F7F49878640789435BA.

## Modifications et motifs

Les trois opérations ne sont pas des corrections de théorèmes : deux phrases françaises sont réparées et une mention d’omission est normalisée. Les anciens octets restent conservés et chaque opération est réversible. Aucune amélioration mathématique de la source n’est insérée.

### FR-ALGEBRA-B29-REPAIR-0001

Anglais L15365 ; français L15129.

Avant :
```tex
$\mathfrak p \in \text{Ass}_R(M)$. Soit $m \in M$ un élément tel que
l'annulateur de $m$ dans $R$ est $\mathfrak p$. Soit
```

Après :
```tex
$\mathfrak p \in \text{Ass}_R(M)$. Soit $m \in M$ un élément tel que
l'annulateur de $m$ dans $R$ soit $\mathfrak p$. Soit
```

L'hypothèse noethérienne porte sur S, pas R. L'annulateur dans R et celui dans S restent distincts. Le subjonctif soit remplace est après tel que ; l'application de R/p dans S/I reçoit son nom grammatical et l'accord injective. Les deux corrections n'ajoutent ni hypothèse ni justification extérieure.

La formule R/p⊂S/I est inchangée ; nommer l'application répare la phrase française, pas l'argument anglais.

### FR-ALGEBRA-B29-REPAIR-0002

Anglais L15367 ; français L15132.

Avant :
```tex
Alors $R/\mathfrak p \subset S/I$ est injectif. En combinant les Lemmes
```

Après :
```tex
Alors l'application $R/\mathfrak p \subset S/I$ est injective. En combinant les Lemmes
```

L'hypothèse noethérienne porte sur S, pas R. L'annulateur dans R et celui dans S restent distincts. Le subjonctif soit remplace est après tel que ; l'application de R/p dans S/I reçoit son nom grammatical et l'accord injective. Les deux corrections n'ajoutent ni hypothèse ni justification extérieure.

La formule R/p⊂S/I est inchangée ; nommer l'application répare la phrase française, pas l'argument anglais.

### FR-ALGEBRA-B29-REPAIR-0003

Anglais L15390 ; français L15152.

Avant :
```tex
Omis.
```

Après :
```tex
Démonstration omise.
```

L'identification via l'injection des spectres est conservée. Démonstration omise remplace Omis selon la normalisation française déjà appliquée ; aucune preuve nouvelle n'est écrite.

Omis reste compréhensible comme argument omis. La normalisation ne prétend pas que cette forme rendait le lemme faux.

## Observations séparées sur la source

Trois observations sont distinctes de la traduction : la coquille annilator, la faute grammaticale Let R is et le domaine incorrect p∈R dans une quantification sur les idéaux premiers. Les deux premières sont déjà rendues idiomatiquement en français ; la formule de la troisième reste littérale. Aucune admission, déduplication globale ou première découverte n’est revendiquée.

### lemma-ass

[Anglais officiel L15146](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15146) · FR-ALGEBRA-B29-SOURCE-NOTE-0001.

```tex
then the annilator of the image $m'' \in M''$ of $m$ is $\mathfrak p$.
```

La source imprime annilator pour annihilator. Le contexte parle de l'annulateur de l'image de m ; aucune autre notion n'est définie. Correction anglaise proposée : annihilator. Le français annulateur est la traduction idiomatique de ce sens et reste inchangé.

Confiance forte sur la coquille et son interprétation ; pas d'admission ou de déduplication globale.

### lemma-one-equation-module

[Anglais officiel L15298](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15298) · FR-ALGEBRA-B29-SOURCE-NOTE-0002.

```tex
Let $R$ is a Noetherian local ring, $M$ a finite $R$-module, and
```

L'anglais Let R is mêle deux constructions. Let R be est la correction grammaticale proposée. Le français Soient rend déjà le sens sans ajouter d'hypothèse et n'est pas changé pour reproduire une faute d'anglais.

Confiance forte sur la faute grammaticale, aucune correction mathématique ou admission au registre.

### lemma-localize-ass

[Anglais officiel L15446](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15446) · FR-ALGEBRA-B29-SOURCE-NOTE-0003.

```tex
since for $\mathfrak p \in R$, $S \cap \mathfrak p = \emptyset$ we have
```

La variable p désigne un idéal premier de R : la localisation M_p et S∩p l'exigent. La formule p∈R le traite à tort comme un élément de l'anneau. Le domaine attendu est p∈Spec(R), ou en prose un idéal premier de R. La traduction conserve la formule officielle p∈R et la proposition de correction reste séparée.

Confiance forte sur le défaut de type ; disposition non admise, sans revendication de première découverte.

## Règles contextualisées

### FR-ALGEBRA-B29-RULE-ASSOCIATED

Association signifie égalité à l'annulateur d'un élément, non simple inclusion ou appartenance au support.

Canon : FR-ALGEBRA-B29-CANON-PESKINE.

### FR-ALGEBRA-B29-RULE-MODULE

Module de type fini et ensemble fini restent distincts ; hypothèses et objets comparés dans chaque passage.

Canon : FR-ALGEBRA-B29-CANON-PESKINE.

### FR-ALGEBRA-B29-RULE-DIVISOR

L'action sur le module garde le sens d'injectivité de la multiplication ; dans M est un registre attesté, non une faute à remplacer.

Canon : FR-ALGEBRA-B29-CANON-PESKINE.

### FR-ALGEBRA-B29-RULE-SUPPORT

Support, contraction et localisation conservent leurs objets et leurs sens source.

Canon : FR-ALGEBRA-B29-CANON-PESKINE.

### FR-ALGEBRA-B29-RULE-LOGIC

Chaque portée est comparée au passage anglais complet, sans attribuer au canon toutes les tournures de rédaction.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B29-RULE-FINITE

Noethérianité de R ou S, finitude de Ass et dimension sont contrôlées séparément.

Canon : FR-ALGEBRA-B29-CANON-PESKINE.

## Passages parallèles complets

### 01 — section-ass

Anglais L15099–15106 ; français L14870–14877.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15099) · FR-ALGEBRA-B29-CHOICE-0001.

La définition usuelle reste distincte de celle des premiers faiblement associés. Non noethérien et non de type fini ne sont pas effacés. Aucun choix d'une définition plus générale n'est imposé à la source.

Règles : FR-ALGEBRA-B29-RULE-ASSOCIATED, FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Associated primes}
\label{section-ass}

\noindent
Here is the standard definition. For non-Noetherian rings and non-finite
modules it may be more appropriate to use the definition in
Section \ref{section-weakly-ass}.
```

Français restauré :
```tex
\section{Idéaux premiers associés}
\label{section-ass}

\noindent
Voici la définition usuelle. Pour les anneaux non noethériens et les modules
qui ne sont pas de type fini, il peut être plus approprié d'utiliser la
définition de la section \ref{section-weakly-ass}.
```

</details>

### 02 — definition-associated

Anglais L15107–15116 ; français L14878–14886.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15107) · FR-ALGEBRA-B29-CHOICE-0002.

Premier associé, élément et annulateur correspondent exactement à la définition. L'attestation de Peskine est plus restrictive dans ses hypothèses ; la définition générale de Stacks reste générale.

Point particulier à relire : Le canon est une attestation de vocabulaire et de notion ; ses hypothèses de type fini/noethérien ne restreignent pas cette définition officielle.

Règles : FR-ALGEBRA-B29-RULE-ASSOCIATED, FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-associated}
Let $R$ be a ring. Let $M$ be an $R$-module.
A prime $\mathfrak p$ of $R$ is {\it associated} to $M$
if there exists an element $m \in M$ whose annihilator
is $\mathfrak p$.
The set of all such primes is denoted $\text{Ass}_R(M)$
or $\text{Ass}(M)$.
\end{definition}
```

Français restauré :
```tex
\begin{definition}
\label{definition-associated}
Soit $R$ un anneau. Soit $M$ un $R$-module.
Un idéal premier $\mathfrak p$ de $R$ est {\it associé} à $M$ s'il existe un
élément $m \in M$ dont l'annulateur est $\mathfrak p$.
L'ensemble de tous ces idéaux premiers se note $\text{Ass}_R(M)$ ou
$\text{Ass}(M)$.
\end{definition}
```

</details>

### 03 — lemma-ass-support

Anglais L15117–15129 ; français L14887–14898.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15117) · FR-ALGEBRA-B29-CHOICE-0003.

L'inclusion de Ass dans Supp et l'argument de non-annulation après localisation sont conservés. L'image de m dans le localisé n'est pas remplacée par un nouvel élément choisi.

Règles : FR-ALGEBRA-B29-RULE-ASSOCIATED, FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ass-support}
Let $R$ be a ring. Let $M$ be an $R$-module.
Then $\text{Ass}(M) \subset \text{Supp}(M)$.
\end{lemma}

\begin{proof}
If $m \in M$ has annihilator $\mathfrak p$, then in particular
no element of $R \setminus \mathfrak p$ annihilates $m$.
Hence $m$ is a nonzero element of $M_{\mathfrak p}$, i.e.,
$\mathfrak p \in \text{Supp}(M)$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ass-support}
Soit $R$ un anneau. Soit $M$ un $R$-module.
Alors $\text{Ass}(M) \subset \text{Supp}(M)$.
\end{lemma}

\begin{proof}
Si $m \in M$ a pour annulateur $\mathfrak p$, alors aucun élément de
$R \setminus \mathfrak p$ n'annule $m$. Ainsi, $m$ est un élément non nul de
$M_{\mathfrak p}$, c'est-à-dire que $\mathfrak p \in \text{Supp}(M)$.
\end{proof}
```

</details>

### 04 — lemma-ass

Anglais L15130–15151 ; français L14899–14919.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15130) · FR-ALGEBRA-B29-CHOICE-0004.

Les deux inclusions, l'égalité pour la somme directe, les deux cas d'existence de g et l'avis d'omission de la dernière preuve restent identiques. La coquille anglaise annilator est comprise comme annihilator et rendue annulateur, sans changement mathématique.

Point particulier à relire : Annilator est une coquille anglaise, pas un nouvel objet. La traduction du sens en annulateur ne constitue pas une amélioration de théorème.

Règles : FR-ALGEBRA-B29-RULE-ASSOCIATED, FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ass}
Let $R$ be a ring. Let $0 \to M' \to M \to M'' \to 0$ be a short exact sequence
of $R$-modules. Then $\text{Ass}(M') \subset \text{Ass}(M)$ and
$\text{Ass}(M) \subset \text{Ass}(M') \cup \text{Ass}(M'')$.
Also $\text{Ass}(M' \oplus M'') = \text{Ass}(M') \cup \text{Ass}(M'')$.
\end{lemma}

\begin{proof}
If $m' \in M'$, then the annihilator of $m'$ viewed as an element of $M'$
is the same as the annihilator of $m'$ viewed as an element of $M$. Hence
the inclusion $\text{Ass}(M') \subset \text{Ass}(M)$. Let $m \in M$
be an element whose annihilator is a prime ideal $\mathfrak p$. If there
exists a $g \in R$, $g \not \in \mathfrak p$ such that $m' = gm \in M'$
then the annihilator of $m'$ is $\mathfrak p$. If there does not
exist a $g \in R$, $g \not \in \mathfrak p$ such that $gm \in M'$,
then the annilator of the image $m'' \in M''$ of $m$ is $\mathfrak p$.
This proves the inclusion
$\text{Ass}(M) \subset \text{Ass}(M') \cup \text{Ass}(M'')$.
We omit the proof of the final statement.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ass}
Soit $R$ un anneau. Soit $0 \to M' \to M \to M'' \to 0$ une suite exacte
courte de $R$-modules. Alors $\text{Ass}(M') \subset \text{Ass}(M)$ et
$\text{Ass}(M) \subset \text{Ass}(M') \cup \text{Ass}(M'')$.
De plus, $\text{Ass}(M' \oplus M'') = \text{Ass}(M') \cup \text{Ass}(M'')$.
\end{lemma}

\begin{proof}
Si $m' \in M'$, l'annulateur de $m'$ considéré comme élément de $M'$ est le
même que l'annulateur de $m'$ considéré comme élément de $M$. On obtient donc
l'inclusion $\text{Ass}(M') \subset \text{Ass}(M)$. Soit $m \in M$ un élément
dont l'annulateur est un idéal premier $\mathfrak p$. S'il existe
$g \in R$, $g \not \in \mathfrak p$, tel que $m' = gm \in M'$, alors
l'annulateur de $m'$ est $\mathfrak p$. S'il n'existe aucun
$g \in R$, $g \not \in \mathfrak p$, tel que $gm \in M'$, alors l'annulateur
de l'image $m'' \in M''$ de $m$ est $\mathfrak p$. Cela démontre l'inclusion
$\text{Ass}(M) \subset \text{Ass}(M') \cup \text{Ass}(M'')$.
Nous omettons la démonstration de la dernière assertion.
\end{proof}
```

</details>

### 05 — lemma-ass-filter

Anglais L15152–15174 ; français L14920–14943.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15152) · FR-ALGEBRA-B29-CHOICE-0005.

La filtration, l'induction sur sa longueur, l'image non nulle dans R/p_n et l'élément fm gardent leurs rôles. La longueur de filtration n'est pas la longueur du module.

Règles : FR-ALGEBRA-B29-RULE-ASSOCIATED, FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ass-filter}
Let $R$ be a ring, and $M$ an $R$-module.
Suppose there exists a filtration by $R$-submodules
$$
0 = M_0 \subset M_1 \subset \ldots \subset M_n = M
$$
such that each quotient $M_i/M_{i-1}$ is isomorphic to $R/\mathfrak p_i$
for some prime ideal $\mathfrak p_i$ of $R$.
Then $\text{Ass}(M) \subset \{\mathfrak p_1, \ldots, \mathfrak p_n\}$.
\end{lemma}

\begin{proof}
By induction on the length $n$ of the filtration $\{ M_i \}$.
Pick $m \in M$ whose annihilator is a prime $\mathfrak p$.
If $m \in M_{n-1}$ we are done by induction. If not,
then $m$ maps to a nonzero element of $M/M_{n-1} \cong
R/\mathfrak p_n$. Hence we have $\mathfrak p \subset \mathfrak p_n$.
If equality does not hold, then we can find $f \in \mathfrak p_n$,
$f \not\in \mathfrak p$. In this case the annihilator of $fm$ is still
$\mathfrak p$ and $fm \in M_{n-1}$. Thus we win by induction.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ass-filter}
Soit $R$ un anneau et soit $M$ un $R$-module.
Supposons qu'il existe une filtration par des sous-$R$-modules
$$
0 = M_0 \subset M_1 \subset \ldots \subset M_n = M
$$
telle que chaque quotient $M_i/M_{i-1}$ soit isomorphe à $R/\mathfrak p_i$
pour un certain idéal premier $\mathfrak p_i$ de $R$.
Alors $\text{Ass}(M) \subset \{\mathfrak p_1, \ldots, \mathfrak p_n\}$.
\end{lemma}

\begin{proof}
Raisonnons par récurrence sur la longueur $n$ de la filtration $\{ M_i \}$.
Choisissons $m \in M$ dont l'annulateur est un idéal premier $\mathfrak p$.
Si $m \in M_{n-1}$, le résultat découle de l'hypothèse de récurrence. Sinon,
$m$ s'envoie sur un élément non nul de
$M/M_{n-1} \cong R/\mathfrak p_n$. Nous avons donc
$\mathfrak p \subset \mathfrak p_n$.
S'il n'y a pas égalité, nous pouvons trouver $f \in \mathfrak p_n$,
$f \not\in \mathfrak p$. Dans ce cas, l'annulateur de $fm$ est encore
$\mathfrak p$ et $fm \in M_{n-1}$. L'hypothèse de récurrence conclut.
\end{proof}
```

</details>

### 06 — lemma-finite-ass

Anglais L15175–15186 ; français L14944–14955.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15175) · FR-ALGEBRA-B29-CHOICE-0006.

La noethérianité de R et la génération finie de M restent explicites ; fini s'applique à l'ensemble Ass, non au cardinal du module.

Règles : FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-finite-ass}
Let $R$ be a Noetherian ring.
Let $M$ be a finite $R$-module.
Then $\text{Ass}(M)$ is finite.
\end{lemma}

\begin{proof}
Immediate from Lemma \ref{lemma-ass-filter} and
Lemma \ref{lemma-filter-Noetherian-module}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-finite-ass}
Soit $R$ un anneau noethérien.
Soit $M$ un $R$-module de type fini.
Alors $\text{Ass}(M)$ est fini.
\end{lemma}

\begin{proof}
Cela résulte immédiatement du Lemme \ref{lemma-ass-filter} et du Lemme
\ref{lemma-filter-Noetherian-module}.
\end{proof}
```

</details>

### 07 — proposition-minimal-primes-associated-primes

Anglais L15187–15232 ; français L14956–15003.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15187) · FR-ALGEBRA-B29-CHOICE-0007.

Les trois ensembles de premiers minimaux et le quantificateur toute filtration sont conservés. Le choix du premier indice i, les produits d'idéaux, l'élément f et les deux inclusions de la preuve sont entièrement relus.

Point particulier à relire : Les premiers minimaux du support ne sont pas identifiés sans condition aux premiers minimaux de R.

Règles : FR-ALGEBRA-B29-RULE-ASSOCIATED, FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-SUPPORT, FR-ALGEBRA-B29-RULE-LOGIC, FR-ALGEBRA-B29-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{proposition}
\label{proposition-minimal-primes-associated-primes}
Let $R$ be a Noetherian ring.
Let $M$ be a finite $R$-module.
The following sets of primes are the same:
\begin{enumerate}
\item The minimal primes in the support of $M$.
\item The minimal primes in $\text{Ass}(M)$.
\item For any filtration $0 = M_0 \subset M_1 \subset \ldots
\subset M_{n-1} \subset M_n = M$ with $M_i/M_{i-1} \cong R/\mathfrak p_i$
the minimal primes of the set $\{\mathfrak p_i\}$.
\end{enumerate}
\end{proposition}

\begin{proof}
Choose a filtration as in (3).
In Lemma \ref{lemma-filter-minimal-primes-in-support}
we have seen that the sets in (1) and (3) are equal.

\medskip\noindent
Let $\mathfrak p$ be a minimal element of the set $\{\mathfrak p_i\}$.
Let $i$ be minimal such that $\mathfrak p = \mathfrak p_i$.
Pick $m \in M_i$, $m \not \in M_{i-1}$. The annihilator of $m$
is contained in $\mathfrak p_i = \mathfrak p$ and contains
$\mathfrak p_1 \mathfrak p_2 \ldots \mathfrak p_i$. By our choice of
$i$ and $\mathfrak p$ we have $\mathfrak p_j \not \subset \mathfrak p$
for $j < i$ and hence we have
$\mathfrak p_1 \mathfrak p_2 \ldots \mathfrak p_{i - 1}
\not \subset \mathfrak p_i$. Pick
$f \in \mathfrak p_1 \mathfrak p_2 \ldots \mathfrak p_{i - 1}$,
$f \not \in \mathfrak p$. Then $fm$ has annihilator $\mathfrak p$.
In this way we see that $\mathfrak p$ is an associated prime of $M$.
By Lemma \ref{lemma-ass-support} we have $\text{Ass}(M) \subset \text{Supp}(M)$
and hence $\mathfrak p$ is minimal in $\text{Ass}(M)$.
Thus the set of primes in (1) is contained in the set of primes of (2).

\medskip\noindent
Let $\mathfrak p$ be a minimal element of $\text{Ass}(M)$.
Since $\text{Ass}(M) \subset \text{Supp}(M)$ there is a minimal
element $\mathfrak q$ of $\text{Supp}(M)$ with
$\mathfrak q \subset \mathfrak p$. We have just shown that
$\mathfrak q \in \text{Ass}(M)$. Hence $\mathfrak q = \mathfrak p$
by minimality of $\mathfrak p$. Thus the set of primes in (2) is
contained in the set of primes of (1).
\end{proof}
```

Français restauré :
```tex
\begin{proposition}
\label{proposition-minimal-primes-associated-primes}
Soit $R$ un anneau noethérien.
Soit $M$ un $R$-module de type fini.
Les ensembles d'idéaux premiers suivants sont égaux :
\begin{enumerate}
\item les idéaux premiers minimaux du support de $M$ ;
\item les idéaux premiers minimaux de $\text{Ass}(M)$ ;
\item pour toute filtration $0 = M_0 \subset M_1 \subset \ldots
\subset M_{n-1} \subset M_n = M$ telle que
$M_i/M_{i-1} \cong R/\mathfrak p_i$, les idéaux premiers minimaux de
l'ensemble $\{\mathfrak p_i\}$.
\end{enumerate}
\end{proposition}

\begin{proof}
Choisissons une filtration comme en (3).
Le Lemme \ref{lemma-filter-minimal-primes-in-support} montre que les ensembles
de (1) et (3) sont égaux.

\medskip\noindent
Soit $\mathfrak p$ un élément minimal de l'ensemble $\{\mathfrak p_i\}$.
Choisissons $i$ minimal tel que $\mathfrak p = \mathfrak p_i$.
Prenons $m \in M_i$, $m \not \in M_{i-1}$. L'annulateur de $m$ est contenu
dans $\mathfrak p_i = \mathfrak p$ et contient
$\mathfrak p_1 \mathfrak p_2 \ldots \mathfrak p_i$. Par notre choix de
$i$ et de $\mathfrak p$, nous avons $\mathfrak p_j \not \subset \mathfrak p$
pour $j < i$, et donc
$\mathfrak p_1 \mathfrak p_2 \ldots \mathfrak p_{i - 1}
\not \subset \mathfrak p_i$. Choisissons
$f \in \mathfrak p_1 \mathfrak p_2 \ldots \mathfrak p_{i - 1}$,
$f \not \in \mathfrak p$. Alors $fm$ a pour annulateur $\mathfrak p$.
Ainsi, $\mathfrak p$ est un idéal premier associé à $M$.
Le Lemme \ref{lemma-ass-support} donne
$\text{Ass}(M) \subset \text{Supp}(M)$ ; par conséquent, $\mathfrak p$ est
minimal dans $\text{Ass}(M)$. L'ensemble des idéaux premiers de (1) est donc
contenu dans l'ensemble des idéaux premiers de (2).

\medskip\noindent
Soit $\mathfrak p$ un élément minimal de $\text{Ass}(M)$.
Puisque $\text{Ass}(M) \subset \text{Supp}(M)$, il existe un élément minimal
$\mathfrak q$ de $\text{Supp}(M)$ tel que
$\mathfrak q \subset \mathfrak p$. Nous venons de montrer que
$\mathfrak q \in \text{Ass}(M)$. Nous avons donc
$\mathfrak q = \mathfrak p$ par minimalité de $\mathfrak p$. Ainsi, l'ensemble des idéaux premiers de (2) est
contenu dans celui de (1).
\end{proof}
```

</details>

### 08 — lemma-ass-zero

Anglais L15233–15258 ; français L15004–15026.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15233) · FR-ALGEBRA-B29-CHOICE-0008.

Le slogan concerne tout module non nul sur un anneau noethérien, pas seulement les modules de type fini. La preuve utilise un sous-module non nul de type fini et remonte à M ; aucune finitude nouvelle n'est imposée.

Point particulier à relire : Les hypothèses de finitude du canon ne sont pas transportées dans ce résultat pour M quelconque.

Règles : FR-ALGEBRA-B29-RULE-ASSOCIATED, FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-LOGIC, FR-ALGEBRA-B29-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ass-zero}
\begin{slogan}
Over a Noetherian ring each nonzero module has an associated prime.
\end{slogan}
Let $R$ be a Noetherian ring. Let $M$ be an $R$-module.
Then
$$
M = (0) \Leftrightarrow \text{Ass}(M) = \emptyset.
$$
\end{lemma}

\begin{proof}
If $M = (0)$, then $\text{Ass}(M) = \emptyset$ by definition.
If $M \not = 0$, pick any nonzero finitely generated submodule
$M' \subset M$, for example a submodule generated by a single nonzero
element. By
Lemma \ref{lemma-support-zero}
we see that $\text{Supp}(M')$ is nonempty. By
Proposition \ref{proposition-minimal-primes-associated-primes}
this implies that $\text{Ass}(M')$ is nonempty.
By
Lemma \ref{lemma-ass}
this implies $\text{Ass}(M) \not = \emptyset$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ass-zero}
\begin{slogan}
Sur un anneau noethérien, tout module non nul possède un idéal premier associé.
\end{slogan}
Soit $R$ un anneau noethérien. Soit $M$ un $R$-module.
Alors
$$
M = (0) \Leftrightarrow \text{Ass}(M) = \emptyset.
$$
\end{lemma}

\begin{proof}
Si $M = (0)$, alors $\text{Ass}(M) = \emptyset$ par définition.
Si $M \not = 0$, choisissons un sous-module non nul de type fini
$M' \subset M$, par exemple le sous-module engendré par un seul élément non
nul. Le Lemme \ref{lemma-support-zero} montre que $\text{Supp}(M')$ n'est pas
vide. D'après la Proposition
\ref{proposition-minimal-primes-associated-primes}, il en résulte que
$\text{Ass}(M')$ n'est pas vide. Le Lemme \ref{lemma-ass} implique alors que
$\text{Ass}(M) \not = \emptyset$.
\end{proof}
```

</details>

### 09 — lemma-ass-minimal-prime-support

Anglais L15259–15276 ; français L15027–15043.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15259) · FR-ALGEBRA-B29-CHOICE-0009.

Minimal signifie minimal dans le support. Le passage aux unions de sous-modules de type fini et les deux unions de Supp/Ass restent exacts.

Règles : FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-LOGIC, FR-ALGEBRA-B29-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ass-minimal-prime-support}
Let $R$ be a Noetherian ring.
Let $M$ be an $R$-module.
Any $\mathfrak p \in \text{Supp}(M)$ which is minimal among the elements
of $\text{Supp}(M)$ is an element of $\text{Ass}(M)$.
\end{lemma}

\begin{proof}
If $M$ is a finite $R$-module, then this is a consequence of
Proposition \ref{proposition-minimal-primes-associated-primes}.
In general write $M = \bigcup M_\lambda$ as the union of its
finite submodules, and use that
$\text{Supp}(M) = \bigcup \text{Supp}(M_\lambda)$
and
$\text{Ass}(M) = \bigcup \text{Ass}(M_\lambda)$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ass-minimal-prime-support}
Soit $R$ un anneau noethérien.
Soit $M$ un $R$-module.
Tout $\mathfrak p \in \text{Supp}(M)$ qui est minimal parmi les éléments de
$\text{Supp}(M)$ appartient à $\text{Ass}(M)$.
\end{lemma}

\begin{proof}
Si $M$ est un $R$-module de type fini, cela résulte de la Proposition
\ref{proposition-minimal-primes-associated-primes}.
Dans le cas général, écrivons $M = \bigcup M_\lambda$ comme réunion de ses
sous-modules de type fini et utilisons les égalités
$\text{Supp}(M) = \bigcup \text{Supp}(M_\lambda)$ et
$\text{Ass}(M) = \bigcup \text{Ass}(M_\lambda)$.
\end{proof}
```

</details>

### 10 — lemma-ass-zero-divisors

Anglais L15277–15295 ; français L15044–15061.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15277) · FR-ALGEBRA-B29-CHOICE-0010.

Diviseur de zéro dans M est conservé : ce registre est attesté chez Peskine et signifie que la multiplication sur le module n'est pas injective. La réunion des premiers associés et la preuve par le noyau N sont fidèles.

Point particulier à relire : Faux positif de registre rejeté après lecture : dans M est réellement attesté. Il serait injustifié de le déclarer incorrect au seul motif que M n'est pas un anneau.

Règles : FR-ALGEBRA-B29-RULE-ASSOCIATED, FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-DIVISOR, FR-ALGEBRA-B29-RULE-LOGIC, FR-ALGEBRA-B29-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ass-zero-divisors}
Let $R$ be a Noetherian ring.
Let $M$ be an $R$-module.
The union $\bigcup_{\mathfrak q \in \text{Ass}(M)} \mathfrak q$
is the set of elements of $R$ which are zerodivisors on $M$.
\end{lemma}

\begin{proof}
Any element in any associated prime clearly is a zerodivisor on $M$.
Conversely, suppose $x \in R$ is a zerodivisor on $M$.
Consider the submodule $N = \{m \in M \mid xm = 0\}$.
Since $N$ is not zero it has an associated prime $\mathfrak q$ by
Lemma \ref{lemma-ass-zero}.
Then $x \in \mathfrak q$ and $\mathfrak q$
is an associated prime of $M$ by
Lemma \ref{lemma-ass}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ass-zero-divisors}
Soit $R$ un anneau noethérien.
Soit $M$ un $R$-module.
La réunion $\bigcup_{\mathfrak q \in \text{Ass}(M)} \mathfrak q$ est
l'ensemble des éléments de $R$ qui sont des diviseurs de zéro dans $M$.
\end{lemma}

\begin{proof}
Tout élément appartenant à un idéal premier associé est manifestement un
diviseur de zéro dans $M$. Réciproquement, supposons que $x \in R$ soit un
diviseur de zéro dans $M$. Considérons le sous-module
$N = \{m \in M \mid xm = 0\}$. Comme $N$ n'est pas nul, il possède un idéal
premier associé $\mathfrak q$ d'après le Lemme \ref{lemma-ass-zero}.
Alors $x \in \mathfrak q$, et $\mathfrak q$ est un idéal premier associé à
$M$ d'après le Lemme \ref{lemma-ass}.
\end{proof}
```

</details>

### 11 — lemma-one-equation-module

Anglais L15296–15327 ; français L15062–15093.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15296) · FR-ALGEBRA-B29-CHOICE-0011.

Les deux inégalités et l'égalité de droite sous la condition sur les premiers minimaux restent exactes. Le français ne remplace pas cette condition par la seule hypothèse de non-diviseur de zéro. Les chaînes de premiers et les renvois restent dans l'argument source.

Point particulier à relire : La coquille Let R is n'est pas reproduite comme faute française. La formule source et le cas de support vide restent littéraux ; aucune nouvelle hypothèse M≠0 n'est ajoutée.

Règles : FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-DIVISOR, FR-ALGEBRA-B29-RULE-SUPPORT, FR-ALGEBRA-B29-RULE-LOGIC, FR-ALGEBRA-B29-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-one-equation-module}
Let $R$ is a Noetherian local ring, $M$ a finite $R$-module, and
$f \in \mathfrak m$ an element of the maximal ideal of $R$. Then
$$
\dim(\text{Supp}(M/fM)) \leq
\dim(\text{Supp}(M)) \leq
\dim(\text{Supp}(M/fM)) + 1
$$
If $f$ is not in any of the minimal primes of the support of $M$
(for example if $f$ is a nonzerodivisor on $M$), then equality
holds for the right inequality.
\end{lemma}

\begin{proof}
(The parenthetical statement follows from Lemma \ref{lemma-ass-zero-divisors}.)
The first inequality follows from $\text{Supp}(M/fM) \subset \text{Supp}(M)$,
see Lemma \ref{lemma-support-quotient}. For the second inequality, note
that $\text{Supp}(M/fM) = \text{Supp}(M) \cap V(f)$, see
Lemma \ref{lemma-support-quotient}. It follows, for example by
Lemma \ref{lemma-filter-primes-in-support} and elementary properties
of dimension, that it suffices to show
$\dim V(\mathfrak p) \leq \dim (V(\mathfrak p) \cap V(f)) + 1$
for primes $\mathfrak p$ of $R$. This is a consequence of
Lemma \ref{lemma-one-equation}.
Finally, if $f$ is not contained in any minimal
prime of the support of $M$, then the chains of primes in
$\text{Supp}(M/fM)$ all give
rise to chains in $\text{Supp}(M)$ which are at least one step away
from being maximal.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-one-equation-module}
Soient $R$ un anneau local noethérien, $M$ un $R$-module de type fini et
$f \in \mathfrak m$ un élément de l'idéal maximal de $R$. Alors
$$
\dim(\text{Supp}(M/fM)) \leq
\dim(\text{Supp}(M)) \leq
\dim(\text{Supp}(M/fM)) + 1
$$
Si $f$ n'appartient à aucun des idéaux premiers minimaux du support de $M$
(par exemple, si $f$ est un non-diviseur de zéro dans $M$), alors l'inégalité
de droite est une égalité.
\end{lemma}

\begin{proof}
(L'assertion entre parenthèses résulte du Lemme
\ref{lemma-ass-zero-divisors}.) La première inégalité découle de
$\text{Supp}(M/fM) \subset \text{Supp}(M)$, voir le Lemme
\ref{lemma-support-quotient}. Pour la seconde, remarquons que
$\text{Supp}(M/fM) = \text{Supp}(M) \cap V(f)$, voir le Lemme
\ref{lemma-support-quotient}. Il en résulte, par exemple d'après le Lemme
\ref{lemma-filter-primes-in-support} et les propriétés élémentaires de la
dimension, qu'il suffit de montrer que
$\dim V(\mathfrak p) \leq \dim (V(\mathfrak p) \cap V(f)) + 1$
pour les idéaux premiers $\mathfrak p$ de $R$. C'est une conséquence du
Lemme \ref{lemma-one-equation}.
Enfin, si $f$ n'est contenu dans aucun idéal premier minimal du support de $M$,
alors toute chaîne d'idéaux premiers de $\text{Supp}(M/fM)$ donne naissance à
une chaîne dans $\text{Supp}(M)$ à laquelle il manque encore au moins une étape
pour être maximale.
\end{proof}
```

</details>

### 12 — lemma-ass-functorial

Anglais L15328–15340 ; français L15094–15106.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15328) · FR-ALGEBRA-B29-CHOICE-0012.

La contraction de l'annulateur donne l'inclusion annoncée. La notation q∩R, même pour un morphisme non injectif, est conservée comme raccourci officiel pour l'image réciproque, sans ajouter une hypothèse d'injection.

Point particulier à relire : La contraction se lit à travers le morphisme donné. Le raccourci q∩R n'est pas une autorisation d'ajouter que R est un sous-anneau de S.

Règles : FR-ALGEBRA-B29-RULE-ASSOCIATED, FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ass-functorial}
Let $\varphi : R \to S$ be a ring map.
Let $M$ be an $S$-module.
Then $\Spec(\varphi)(\text{Ass}_S(M)) \subset \text{Ass}_R(M)$.
\end{lemma}

\begin{proof}
If $\mathfrak q \in \text{Ass}_S(M)$, then there exists an $m$ in $M$
such that the annihilator of $m$ in $S$ is $\mathfrak q$. Then the annihilator
of $m$ in $R$ is $\mathfrak q \cap R$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ass-functorial}
Soit $\varphi : R \to S$ un morphisme d'anneaux.
Soit $M$ un $S$-module.
Alors $\Spec(\varphi)(\text{Ass}_S(M)) \subset \text{Ass}_R(M)$.
\end{lemma}

\begin{proof}
Si $\mathfrak q \in \text{Ass}_S(M)$, il existe un élément $m$ de $M$ tel que
l'annulateur de $m$ dans $S$ soit $\mathfrak q$. L'annulateur de $m$ dans $R$
est alors $\mathfrak q \cap R$.
\end{proof}
```

</details>

### 13 — remark-ass-reverse-functorial

Anglais L15341–15351 ; français L15107–15117.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15341) · FR-ALGEBRA-B29-CHOICE-0013.

Le contre-exemple non noethérien à infinité de variables reste intact. La remarque dit que l'inclusion inverse peut échouer, pas que toute fonctorialité échoue.

Règles : FR-ALGEBRA-B29-RULE-MODULE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{remark}
\label{remark-ass-reverse-functorial}
Let $\varphi : R \to S$ be a ring map.
Let $M$ be an $S$-module.
Then it is not always the case that
$\Spec(\varphi)(\text{Ass}_S(M)) \supset \text{Ass}_R(M)$.
For example, consider the ring map
$R = k \to S = k[x_1, x_2, x_3, \ldots]/(x_i^2)$ and $M = S$.
Then $\text{Ass}_R(M)$ is not empty, but $\text{Ass}_S(S)$ is empty.
\end{remark}
```

Français restauré :
```tex
\begin{remark}
\label{remark-ass-reverse-functorial}
Soit $\varphi : R \to S$ un morphisme d'anneaux.
Soit $M$ un $S$-module.
Il n'est pas toujours vrai que
$\Spec(\varphi)(\text{Ass}_S(M)) \supset \text{Ass}_R(M)$.
Par exemple, considérons le morphisme d'anneaux
$R = k \to S = k[x_1, x_2, x_3, \ldots]/(x_i^2)$ et $M = S$.
Alors $\text{Ass}_R(M)$ n'est pas vide, tandis que $\text{Ass}_S(S)$ est vide.
\end{remark}
```

</details>

### 14 — lemma-ass-functorial-Noetherian

Anglais L15352–15378 ; français L15118–15141.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15352) · FR-ALGEBRA-B29-CHOICE-0014.

L'hypothèse noethérienne porte sur S, pas R. L'annulateur dans R et celui dans S restent distincts. Le subjonctif soit remplace est après tel que ; l'application de R/p dans S/I reçoit son nom grammatical et l'accord injective. Les deux corrections n'ajoutent ni hypothèse ni justification extérieure.

Point particulier à relire : La formule R/p⊂S/I est inchangée ; nommer l'application répare la phrase française, pas l'argument anglais.

Règles : FR-ALGEBRA-B29-RULE-ASSOCIATED, FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-DIVISOR, FR-ALGEBRA-B29-RULE-LOGIC, FR-ALGEBRA-B29-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ass-functorial-Noetherian}
Let $\varphi : R \to S$ be a ring map.
Let $M$ be an $S$-module. If $S$ is Noetherian, then
$\Spec(\varphi)(\text{Ass}_S(M)) = \text{Ass}_R(M)$.
\end{lemma}

\begin{proof}
We have already seen in
Lemma \ref{lemma-ass-functorial}
that
$\Spec(\varphi)(\text{Ass}_S(M)) \subset \text{Ass}_R(M)$.
For the converse, choose a prime $\mathfrak p \in \text{Ass}_R(M)$.
Let $m \in M$ be an element such that the annihilator of $m$ in $R$
is $\mathfrak p$. Let $I = \{g \in S \mid gm = 0\}$ be the annihilator
of $m$ in $S$. Then $R/\mathfrak p \subset S/I$ is injective.
Combining Lemmas \ref{lemma-injective-minimal-primes-in-image} and
\ref{lemma-minimal-prime-image-minimal-prime} we see that
there is a prime $\mathfrak q \subset S$ minimal over $I$
mapping to $\mathfrak p$. By
Proposition \ref{proposition-minimal-primes-associated-primes}
we see that $\mathfrak q$ is an associated prime of $S/I$, hence
$\mathfrak q$ is an associated prime of $M$ by
Lemma \ref{lemma-ass}
and we win.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ass-functorial-Noetherian}
Soit $\varphi : R \to S$ un morphisme d'anneaux.
Soit $M$ un $S$-module. Si $S$ est noethérien, alors
$\Spec(\varphi)(\text{Ass}_S(M)) = \text{Ass}_R(M)$.
\end{lemma}

\begin{proof}
Nous avons déjà vu dans le Lemme \ref{lemma-ass-functorial} que
$\Spec(\varphi)(\text{Ass}_S(M)) \subset \text{Ass}_R(M)$.
Pour l'inclusion réciproque, choisissons un idéal premier
$\mathfrak p \in \text{Ass}_R(M)$. Soit $m \in M$ un élément tel que
l'annulateur de $m$ dans $R$ soit $\mathfrak p$. Soit
$I = \{g \in S \mid gm = 0\}$ l'annulateur de $m$ dans $S$.
Alors l'application $R/\mathfrak p \subset S/I$ est injective. En combinant les Lemmes
\ref{lemma-injective-minimal-primes-in-image} et
\ref{lemma-minimal-prime-image-minimal-prime}, nous voyons qu'il existe un
idéal premier $\mathfrak q \subset S$ minimal au-dessus de $I$ qui s'envoie
sur $\mathfrak p$. D'après la Proposition
\ref{proposition-minimal-primes-associated-primes}, $\mathfrak q$ est un idéal
premier associé à $S/I$ ; par le Lemme \ref{lemma-ass}, $\mathfrak q$ est donc
un idéal premier associé à $M$, ce qui conclut.
\end{proof}
```

</details>

### 15 — lemma-ass-quotient-ring

Anglais L15379–15392 ; français L15142–15154.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15379) · FR-ALGEBRA-B29-CHOICE-0015.

L'identification via l'injection des spectres est conservée. Démonstration omise remplace Omis selon la normalisation française déjà appliquée ; aucune preuve nouvelle n'est écrite.

Point particulier à relire : Omis reste compréhensible comme argument omis. La normalisation ne prétend pas que cette forme rendait le lemme faux.

Règles : FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-DIVISOR, FR-ALGEBRA-B29-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ass-quotient-ring}
Let $R$ be a ring.
Let $I$ be an ideal.
Let $M$ be an $R/I$-module.
Via the canonical injection
$\Spec(R/I) \to \Spec(R)$
we have $\text{Ass}_{R/I}(M) = \text{Ass}_R(M)$.
\end{lemma}

\begin{proof}
Omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ass-quotient-ring}
Soit $R$ un anneau.
Soit $I$ un idéal.
Soit $M$ un $R/I$-module.
Via l'injection canonique $\Spec(R/I) \to \Spec(R)$, nous avons
$\text{Ass}_{R/I}(M) = \text{Ass}_R(M)$.
\end{lemma}

\begin{proof}
Démonstration omise.
\end{proof}
```

</details>

### 16 — lemma-associated-primes-localize

Anglais L15393–15421 ; français L15155–15181.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15393) · FR-ALGEBRA-B29-CHOICE-0016.

La première implication est générale ; la réciproque suppose que l'idéal premier est de type fini. Les générateurs f_i, les multiplicateurs g_i et l'annulateur du produit gardent leurs indices et leurs objets.

Règles : FR-ALGEBRA-B29-RULE-ASSOCIATED, FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-SUPPORT, FR-ALGEBRA-B29-RULE-LOGIC, FR-ALGEBRA-B29-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-associated-primes-localize}
Let $R$ be a ring.
Let $M$ be an $R$-module.
Let $\mathfrak p \subset R$ be a prime.
\begin{enumerate}
\item If $\mathfrak p \in \text{Ass}(M)$ then
$\mathfrak pR_{\mathfrak p} \in \text{Ass}(M_{\mathfrak p})$.
\item If $\mathfrak p$ is finitely generated then the converse holds
as well.
\end{enumerate}
\end{lemma}

\begin{proof}
If $\mathfrak p \in \text{Ass}(M)$ there exists an element $m \in M$
whose annihilator is $\mathfrak p$. As localization is exact
(Proposition \ref{proposition-localization-exact})
we see that the annihilator of $m/1$ in
$M_{\mathfrak p}$ is $\mathfrak pR_{\mathfrak p}$ hence (1) holds.
Assume $\mathfrak pR_{\mathfrak p} \in \text{Ass}(M_{\mathfrak p})$
and $\mathfrak p = (f_1, \ldots, f_n)$. Let $m/g$ be an element of
$M_{\mathfrak p}$ whose annihilator is $\mathfrak pR_{\mathfrak p}$.
This implies that the annihilator of $m$ is contained in $\mathfrak p$.
As $f_i m/g = 0$ in $M_{\mathfrak p}$ we see there exists a
$g_i \in R$, $g_i \not \in \mathfrak p$ such that $g_i f_i m = 0$ in $M$.
Combined we see the annihilator of $g_1\ldots g_nm$ is $\mathfrak p$. Hence
$\mathfrak p \in \text{Ass}(M)$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-associated-primes-localize}
Soit $R$ un anneau.
Soit $M$ un $R$-module.
Soit $\mathfrak p \subset R$ un idéal premier.
\begin{enumerate}
\item Si $\mathfrak p \in \text{Ass}(M)$, alors
$\mathfrak pR_{\mathfrak p} \in \text{Ass}(M_{\mathfrak p})$.
\item Si $\mathfrak p$ est de type fini, la réciproque est également vraie.
\end{enumerate}
\end{lemma}

\begin{proof}
Si $\mathfrak p \in \text{Ass}(M)$, il existe un élément $m \in M$ dont
l'annulateur est $\mathfrak p$. Comme la localisation est exacte
(Proposition \ref{proposition-localization-exact}), l'annulateur de $m/1$ dans
$M_{\mathfrak p}$ est $\mathfrak pR_{\mathfrak p}$ ; cela démontre (1).
Supposons $\mathfrak pR_{\mathfrak p} \in \text{Ass}(M_{\mathfrak p})$ et
$\mathfrak p = (f_1, \ldots, f_n)$. Soit $m/g$ un élément de
$M_{\mathfrak p}$ dont l'annulateur est $\mathfrak pR_{\mathfrak p}$.
Cela implique que l'annulateur de $m$ est contenu dans $\mathfrak p$.
Comme $f_i m/g = 0$ dans $M_{\mathfrak p}$, il existe
$g_i \in R$, $g_i \not \in \mathfrak p$, tel que $g_i f_i m = 0$ dans $M$.
En combinant ces faits, nous voyons que l'annulateur de $g_1\ldots g_nm$ est
$\mathfrak p$. Ainsi, $\mathfrak p \in \text{Ass}(M)$.
\end{proof}
```

</details>

### 17 — lemma-localize-ass

Anglais L15422–15449 ; français L15182–15208.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15422) · FR-ALGEBRA-B29-CHOICE-0017.

Les trois clauses distinguent identification des spectres, inclusion et égalité noethérienne. Les annulateurs et leurs localisations sont conservés. Le domaine imprimé p∈R de la preuve est un défaut de source signalé séparément, non corrigé dans la formule française.

Point particulier à relire : Le français conserve p∈R, exactement comme l'autorité. L'observation de type est non admise et séparée du texte.

Règles : FR-ALGEBRA-B29-RULE-ASSOCIATED, FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-DIVISOR, FR-ALGEBRA-B29-RULE-SUPPORT, FR-ALGEBRA-B29-RULE-LOGIC, FR-ALGEBRA-B29-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-localize-ass}
Let $R$ be a ring. Let $M$ be an $R$-module.
Let $S \subset R$ be a multiplicative subset.
Via the canonical injection $\Spec(S^{-1}R) \to \Spec(R)$
we have
\begin{enumerate}
\item $\text{Ass}_R(S^{-1}M) = \text{Ass}_{S^{-1}R}(S^{-1}M)$,
\item
$\text{Ass}_R(M) \cap \Spec(S^{-1}R) \subset \text{Ass}_R(S^{-1}M)$, and
\item if $R$ is Noetherian this inclusion is an equality.
\end{enumerate}
\end{lemma}

\begin{proof}
For $m \in S^{-1}M$, let $I \subset R$ and $J \subset S^{-1}R$ be the
annihilators of $m$. Then $I$ is the inverse image of $J$ by the map
$R \to S^{-1}R$ and $J = S^{-1}I$. The equality in (1) follows by the
description of the map $\Spec(S^{-1}R) \to \Spec(R)$ in
Lemma \ref{lemma-spec-localization}.
For $m \in M$, let $I \subset R$ be the annihilator of $m$ in $R$
and let $J \subset S^{-1}R$ be the annihilator of $m/1 \in S^{-1}M$.
We have $J = S^{-1}I$ which implies (2). The equality in the
Noetherian case follows from Lemma \ref{lemma-associated-primes-localize}
since for $\mathfrak p \in R$, $S \cap \mathfrak p = \emptyset$ we have
$M_{\mathfrak p} = (S^{-1}M)_{S^{-1}\mathfrak p}$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-localize-ass}
Soit $R$ un anneau. Soit $M$ un $R$-module.
Soit $S \subset R$ une partie multiplicative.
Via l'injection canonique $\Spec(S^{-1}R) \to \Spec(R)$, nous avons
\begin{enumerate}
\item $\text{Ass}_R(S^{-1}M) = \text{Ass}_{S^{-1}R}(S^{-1}M)$,
\item
$\text{Ass}_R(M) \cap \Spec(S^{-1}R) \subset \text{Ass}_R(S^{-1}M)$, et
\item si $R$ est noethérien, cette inclusion est une égalité.
\end{enumerate}
\end{lemma}

\begin{proof}
Pour $m \in S^{-1}M$, soient $I \subset R$ et $J \subset S^{-1}R$ les
annulateurs de $m$. Alors $I$ est l'image réciproque de $J$ par le morphisme
$R \to S^{-1}R$, et $J = S^{-1}I$. L'égalité de (1) résulte de la description
du morphisme $\Spec(S^{-1}R) \to \Spec(R)$ donnée dans le Lemme
\ref{lemma-spec-localization}.
Pour $m \in M$, soit $I \subset R$ l'annulateur de $m$ dans $R$, et soit
$J \subset S^{-1}R$ l'annulateur de $m/1 \in S^{-1}M$.
Nous avons $J = S^{-1}I$, ce qui implique (2). Dans le cas noethérien,
l'égalité résulte du Lemme \ref{lemma-associated-primes-localize}, car pour
$\mathfrak p \in R$, $S \cap \mathfrak p = \emptyset$, nous avons
$M_{\mathfrak p} = (S^{-1}M)_{S^{-1}\mathfrak p}$.
\end{proof}
```

</details>

### 18 — lemma-localize-ass-nonzero-divisors

Anglais L15450–15469 ; français L15209–15227.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15450) · FR-ALGEBRA-B29-CHOICE-0018.

L'hypothèse porte sur chaque élément de S et son action sur M. L'injection de M dans le localisé et les deux annulateurs sont identiques ; dans M n'est pas remplacé sans nécessité.

Règles : FR-ALGEBRA-B29-RULE-ASSOCIATED, FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-DIVISOR, FR-ALGEBRA-B29-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-localize-ass-nonzero-divisors}
Let $R$ be a ring. Let $M$ be an $R$-module.
Let $S \subset R$ be a multiplicative subset.
Assume that every $s \in S$ is a nonzerodivisor on $M$.
Then
$$
\text{Ass}_R(M) = \text{Ass}_R(S^{-1}M).
$$
\end{lemma}

\begin{proof}
As $M \subset S^{-1}M$ by assumption we get the inclusion
$\text{Ass}(M) \subset \text{Ass}(S^{-1}M)$ from
Lemma \ref{lemma-ass}.
Conversely, suppose that $n/s \in S^{-1}M$ is an element whose
annihilator is a prime ideal $\mathfrak p$. Then the annihilator
of $n \in M$ is also $\mathfrak p$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-localize-ass-nonzero-divisors}
Soit $R$ un anneau. Soit $M$ un $R$-module.
Soit $S \subset R$ une partie multiplicative.
Supposons que tout $s \in S$ soit un non-diviseur de zéro dans $M$.
Alors
$$
\text{Ass}_R(M) = \text{Ass}_R(S^{-1}M).
$$
\end{lemma}

\begin{proof}
Puisque $M \subset S^{-1}M$ par hypothèse, le Lemme \ref{lemma-ass} donne
l'inclusion $\text{Ass}(M) \subset \text{Ass}(S^{-1}M)$.
Réciproquement, supposons que $n/s \in S^{-1}M$ soit un élément dont
l'annulateur est un idéal premier $\mathfrak p$. Alors l'annulateur de
$n \in M$ est lui aussi $\mathfrak p$.
\end{proof}
```

</details>

### 19 — lemma-ideal-nonzerodivisor

Anglais L15470–15494 ; français L15228–15251.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15470) · FR-ALGEBRA-B29-CHOICE-0019.

Le critère d'existence dans I et la non-inclusion dans chaque premier associé sont comparés. L'évitement des premiers est appliqué à l'ensemble fini Ass(M). Aucun quantificateur ni hypothèse locale n'est omis.

Règles : FR-ALGEBRA-B29-RULE-ASSOCIATED, FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-DIVISOR, FR-ALGEBRA-B29-RULE-LOGIC, FR-ALGEBRA-B29-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ideal-nonzerodivisor}
Let $R$ be a Noetherian local ring with
maximal ideal $\mathfrak m$. Let $I \subset \mathfrak m$
be an ideal. Let $M$ be a finite $R$-module.
The following are equivalent:
\begin{enumerate}
\item There exists an $x \in I$ which is not a zerodivisor on $M$.
\item We have $I \not \subset \mathfrak q$ for all
$\mathfrak q \in \text{Ass}(M)$.
\end{enumerate}
\end{lemma}

\begin{proof}
If there exists a nonzerodivisor $x$ in $I$,
then $x$ clearly cannot be in any associated
prime of $M$. Conversely, suppose $I \not \subset \mathfrak q$
for all $\mathfrak q \in \text{Ass}(M)$. In this case we can
choose $x \in I$, $x \not \in \mathfrak q$ for all
$\mathfrak q \in \text{Ass}(M)$ by Lemmas
\ref{lemma-finite-ass} and \ref{lemma-silly}.
By Lemma \ref{lemma-ass-zero-divisors} the element $x$
is not a zerodivisor on $M$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ideal-nonzerodivisor}
Soit $R$ un anneau local noethérien d'idéal maximal $\mathfrak m$.
Soit $I \subset \mathfrak m$ un idéal. Soit $M$ un $R$-module de type fini.
Les conditions suivantes sont équivalentes :
\begin{enumerate}
\item Il existe $x \in I$ qui n'est pas un diviseur de zéro dans $M$.
\item Nous avons $I \not \subset \mathfrak q$ pour tout
$\mathfrak q \in \text{Ass}(M)$.
\end{enumerate}
\end{lemma}

\begin{proof}
S'il existe un non-diviseur de zéro $x$ dans $I$, alors $x$ ne peut
manifestement appartenir à aucun idéal premier associé à $M$.
Réciproquement, supposons $I \not \subset \mathfrak q$ pour tout
$\mathfrak q \in \text{Ass}(M)$. Nous pouvons alors choisir
$x \in I$, $x \not \in \mathfrak q$ pour tout
$\mathfrak q \in \text{Ass}(M)$, d'après les Lemmes
\ref{lemma-finite-ass} et \ref{lemma-silly}.
Le Lemme \ref{lemma-ass-zero-divisors} montre que l'élément $x$ n'est pas un
diviseur de zéro dans $M$.
\end{proof}
```

</details>

### 20 — lemma-zero-at-ass-zero

Anglais L15495–15520 ; français L15252–15276.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15495) · FR-ALGEBRA-B29-CHOICE-0020.

Le produit indexé sur les premiers associés et l'injectivité de la flèche restent exacts. Le raisonnement sur Rx et le support non nul est conservé. La remarque éditoriale proposant de déplacer le lemme reste traduite, sans déplacement effectif.

Point particulier à relire : La remarque This lemma should probably be put somewhere else n'est ni supprimée ni exécutée.

Règles : FR-ALGEBRA-B29-RULE-ASSOCIATED, FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-DIVISOR, FR-ALGEBRA-B29-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-zero-at-ass-zero}
Let $R$ be a ring. Let $M$ be an $R$-module. If $R$ is Noetherian
the map
$$
M
\longrightarrow
\prod\nolimits_{\mathfrak p \in \text{Ass}(M)} M_{\mathfrak p}
$$
is injective.
\end{lemma}

\begin{proof}
Let $x \in M$ be an element of the kernel of the map.
Then if $\mathfrak p$ is an associated prime of $Rx \subset M$
we see on the one hand that $\mathfrak p \in \text{Ass}(M)$
(Lemma \ref{lemma-ass}) and
on the other hand that $(Rx)_{\mathfrak p} \subset M_{\mathfrak p}$
is not zero. This contradiction shows that $\text{Ass}(Rx) = \emptyset$.
Hence $Rx = 0$ by
Lemma \ref{lemma-ass-zero}.
\end{proof}

\noindent
This lemma should probably be put somewhere else.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-zero-at-ass-zero}
Soit $R$ un anneau. Soit $M$ un $R$-module. Si $R$ est noethérien,
l'application
$$
M
\longrightarrow
\prod\nolimits_{\mathfrak p \in \text{Ass}(M)} M_{\mathfrak p}
$$
est injective.
\end{lemma}

\begin{proof}
Soit $x \in M$ un élément du noyau de l'application.
Alors, si $\mathfrak p$ est un idéal premier associé à $Rx \subset M$, nous
voyons d'une part que $\mathfrak p \in \text{Ass}(M)$
(Lemme \ref{lemma-ass}) et d'autre part que
$(Rx)_{\mathfrak p} \subset M_{\mathfrak p}$ n'est pas nul.
Cette contradiction montre que $\text{Ass}(Rx) = \emptyset$.
Ainsi, $Rx = 0$ d'après le Lemme \ref{lemma-ass-zero}.
\end{proof}

\noindent
Ce lemme devrait probablement être placé ailleurs.
```

</details>

### 21 — lemma-dim-not-zero-exists-nonzerodivisor-nonunit

Anglais L15521–15541 ; français L15277–15296.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15521) · FR-ALGEBRA-B29-CHOICE-0021.

Type fini sur un corps, dimension strictement positive, élément non-diviseur de zéro et non inversible restent distincts. La preuve utilise les premiers associés finis, les maximaux infinis et l'évitement ; aucun résultat extérieur n'est importé.

Règles : FR-ALGEBRA-B29-RULE-ASSOCIATED, FR-ALGEBRA-B29-RULE-MODULE, FR-ALGEBRA-B29-RULE-DIVISOR, FR-ALGEBRA-B29-RULE-LOGIC, FR-ALGEBRA-B29-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-dim-not-zero-exists-nonzerodivisor-nonunit}
Let $k$ be a field. Let $S$ be a finite type $k$ algebra.
If $\dim(S) > 0$, then there exists an element $f \in S$
which is a nonzerodivisor and a nonunit.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-finite-ass} the ring $S$ has finitely many associated
prime ideals. By Lemma \ref{lemma-finite-type-algebra-finite-nr-primes}
the ring $S$ has infinitely many maximal ideals. Hence we can choose
a maximal ideal $\mathfrak m \subset S$ which is not an associated prime
of $S$. By prime avoidance (Lemma \ref{lemma-silly}),
we can choose a nonzero $f \in \mathfrak m$ 
which is not contained in any of the associated primes of $S$.
By Lemma \ref{lemma-ass-zero-divisors} the element $f$ is a nonzerodivisor
and as $f \in \mathfrak m$ we see that $f$ is not a unit.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-dim-not-zero-exists-nonzerodivisor-nonunit}
Soit $k$ un corps. Soit $S$ une $k$-algèbre de type fini.
Si $\dim(S) > 0$, alors il existe un élément $f \in S$ qui est un
non-diviseur de zéro et n'est pas inversible.
\end{lemma}

\begin{proof}
D'après le Lemme \ref{lemma-finite-ass}, l'anneau $S$ ne possède qu'un nombre
fini d'idéaux premiers associés. D'après le Lemme
\ref{lemma-finite-type-algebra-finite-nr-primes}, l'anneau $S$ possède une
infinité d'idéaux maximaux. Nous pouvons donc choisir un idéal maximal
$\mathfrak m \subset S$ qui ne soit pas un idéal premier associé à $S$.
Par évitement des idéaux premiers (Lemme \ref{lemma-silly}), nous pouvons
choisir un élément non nul $f \in \mathfrak m$ qui n'appartient à aucun des
idéaux premiers associés à $S$. D'après le Lemme
\ref{lemma-ass-zero-divisors}, l'élément $f$ est un non-diviseur de zéro ; et,
comme $f \in \mathfrak m$, nous voyons que $f$ n'est pas une unité.
\end{proof}
```

</details>

## Contrôles et suite

Les 334 régions mathématiques de cette section sont identiques, sans exception. Le préfixe de 10 961 régions passe avec les quarante et une exceptions linguistiques antérieures ; les différences sont vérifiées dans leur ordre et avec leurs multiplicités exactes.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items restent identiques. Aucune citation ou titre facultatif différent ne figure dans ce lot. Les opérations inverses retrouvent le lot précédent puis tous les octets du témoin public préservé. Préfixe déjà relu et suffixe encore non relu sont inchangés.

Les 564 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Puissances symboliques, anglais L15542 / français L15297. Aucun PDF nouveau ni publication ; restauration globale en cours.

