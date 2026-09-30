# Algèbre commutative : diviseurs de zéro et spectres

## Résultat et portée

Trois sections entièrement comparées : anglais L4536–5088 et français L4516–5068. Les 16 paires contiennent les énoncés, preuves, exemples et transitions complets. 228 occurrences sont reliées à des règles contextualisées. Le préfixe relu atteint 27 sections, 166 paires et 1326 occurrences. Le chapitre et l’édition restent inachevés.

Quatre opérations rétablissent la fidélité dans deux exemples : deux qualifications non nul ajoutées au cas de Z[x] sont retirées ; le renvoi former redevient premier et la localisation at the maximal ideal redevient en l’idéal maximal. Ces restaurations réintroduisent ou préservent des lacunes et ambiguïtés du témoin officiel. Elles ne sont pas une approbation mathématique de ses assertions. Les corrections envisagées restent entièrement séparées du français fidèle.

Quatorze observations de source sont documentées avec leur phrase exacte et une raison vérifiable. Elles ne sont pas présentées comme des découvertes nouvelles ou des admissions dans le registre d’errata ; aucune déduplication de ce registre n’est revendiquée. Les hésitations d’antécédent et d’exposants sont distinguées des erreurs directement démontrables.

Comparaison assistée par IA, sans relecture humaine. Le canon a été consulté rétrospectivement ; aucune consultation antérieure n’est inventée. Les remarques de relecture n’empêchent pas la poursuite du travail.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch7.fr.tex) · [État français précédent](staged/fr/010_algebra.prose-batch6.fr.tex) · [Lot précédent](ALGEBRA_PROSE_BATCH6_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH7_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH7_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH7_OCCURRENCES.json) · [Restaurations avant/après](ALGEBRA_PROSE_BATCH7_REPAIRS.json) · [Exceptions linguistiques des formules](ALGEBRA_PROSE_BATCH7_MATH_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH7_COVERAGE.json) · [Observations de source séparées](ALGEBRA_PROSE_BATCH7_SOURCE_OBSERVATIONS.json).

## Canon français effectivement consulté

### Antoine Ducros — Introduction à la théorie des schémas, juillet 2021

[Source universitaire](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [PDF conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages PDF/imprimées indiquées lues intégralement. Appui précis : 0.1.4–8 (corps, nilpotent, réduit, principal, factoriel) ; 2.1.3.3–2.1.8.2 (parties multiplicatives, diviseurs de zéro, corps des fractions, localisation et transitivité) ; 4.2.1–11 (spectres de Z[T] et k[S,T]) ; 4.3.12–16 et 4.3.22 (irréductibilité, point générique, sobriété, composantes). Les pages 71,198,209 ont aussi été lues visuellement.

Attestations courtes : « diviseurs de zéro », « corps des fractions », « anneau factoriel », « point générique », « sobre », « composantes irréductibles ».

L'usage des termes est lu avec leurs définitions, les noyaux et les exemples de fibres ; la page 198 décrit explicitement les idéaux (0) et (p). La terminologie n'est pas déduite d'une simple recherche de mots.

Limites : L'expression anneau total des fractions et les termes spectral, profini, totalement discontinu ne sont pas attestés dans ces pages. Le chapitre sur k[S,T] suppose k algébriquement clos ; la finitude des composantes p.211 suppose la noethérianité : aucune de ces hypothèses n'est importée. Plusieurs coquilles propres au cours (multiplication des fractions p.71, notations des coordonnées p.201, cible de l'évaluation p.203) ne sont pas utilisées comme modèle de formules. Les suites de pages non lues ne sont pas déclarées consultées. Consultation rétrospective, sans prétendre que le traducteur initial l'a effectuée.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

## Règles contextualisées

### FR-ALGEBRA-B7-RULE-LOCALISATION

Diviseurs de zéro, localisation et fractions sont attestés en contexte chez Ducros 2.1.3–8. L'anneau total n'est pas nécessairement un corps ; le syntagme complet reste sans attestation externe dans ce lot. Une localisation en un idéal premier inverse son complément, une localisation en un élément inverse ses puissances : la confusion de la source est signalée, non réparée dans la traduction.

Canon : FR-ALGEBRA-B7-CANON-DUCROS.

### FR-ALGEBRA-B7-RULE-ANNEAUX

Corps, réduit et nilpotent suivent Ducros 0.1.4–7 ; principal et factoriel suivent 0.1.8. Nilpotent ne signifie pas nul, unité signifie élément inversible, et les propriétés de domaine restent algébriques. Euclidien est retenu par son sens précis dans l'argument du témoin, sans attestation nouvelle prétendue.

Canon : FR-ALGEBRA-B7-CANON-DUCROS.

### FR-ALGEBRA-B7-RULE-PREMIERS

Les premiers minimaux correspondent aux composantes irréductibles par inversion de l'ordre, non aux points fermés. Les maximaux du localisé ne sont pas confondus avec les maximaux de l'anneau initial. Ducros 4.3.15 atteste le lien aux fermés irréductibles ; aucune hypothèse noethérienne n'est ajoutée.

Canon : FR-ALGEBRA-B7-CANON-DUCROS.

### FR-ALGEBRA-B7-RULE-TOPOLOGIE

Adhérence, point générique et sobre sont directement motivés par Ducros 4.3.12–16. Séparé s'entend ici au sens de Hausdorff. Profini, spectral et totalement discontinu restent des choix documentés mais sans nouvelle attestation dans le canon consulté ; leurs définitions citées dans Stacks gouvernent. Principal décrit un D(f), non un ouvert affine arbitraire.

Canon : FR-ALGEBRA-B7-CANON-DUCROS.

### FR-ALGEBRA-B7-RULE-POLYNOMES

Le sens de l'irréductibilité des polynômes, du contenu et de l'évaluation est comparé à Ducros 0.1.8 et 4.2.1–11. Associés signifie à multiplication par une unité près ; distincts ne garantit pas non associés. Les défauts de l'argument anglais ne sont pas corrigés par un choix français plus fort.

Canon : FR-ALGEBRA-B7-CANON-DUCROS.

### FR-ALGEBRA-B7-RULE-APPLICATIONS

Plongement exprime l'injectivité ; morphisme conserve ici les applications d'anneaux et les applications induites sur leurs spectres. Le sens contravariant est vérifié avec les formules. De type fini exprime une génération finie, non la finitude du sous-jacent. Les isomorphismes d'anneaux et homéomorphismes sont distingués.

Canon : FR-ALGEBRA-B7-CANON-DUCROS.

## Passages parallèles complets

### 01 — section-total-quotient-ring

Anglais L4536–4541 ; français L4516–4521.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4536) · FR-ALGEBRA-B7-CHOICE-0001.

Diviseurs de zéro ne signifie pas éléments nuls : un élément peut annuler un autre élément non nul. Le titre conserve anneau total des fractions et ne remplace pas anneau par corps. L'introduction porte sur un idéal premier minimal, non sur un idéal maximal de l'anneau initial. Ducros 2.1.4 atteste diviseurs de zéro dans la même discussion de localisation ; le syntagme complet anneau total des fractions n'a pas été retrouvé dans les pages effectivement consultées et reste justifié provisoirement par la définition source.

Règles : FR-ALGEBRA-B7-RULE-LOCALISATION, FR-ALGEBRA-B7-RULE-PREMIERS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Zerodivisors and total rings of fractions}
\label{section-total-quotient-ring}

\noindent
The local ring at a minimal prime has the following properties.
```

Français restauré :
```tex
\section{Diviseurs de zéro et anneaux totaux des fractions}
\label{section-total-quotient-ring}

\noindent
L'anneau local en un idéal premier minimal possède les propriétés suivantes.
```

</details>

### 02 — lemma-minimal-prime-reduced-ring

Anglais L4542–4558 ; français L4522–4538.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4542) · FR-ALGEBRA-B7-CHOICE-0002.

Le maximal appartient à l'anneau localisé ; le premier de départ est minimal dans R. La nilpotence porte sur chaque élément de l'idéal, pas sur l'idéal entier ni sur un exposant commun. La condition réduit n'est requise que pour la conclusion corps. Le français l'anneau local explicite sans changer le sens le pronom anglais it. Réduit, nilpotent et corps sont définis chez Ducros 0.1.4–7 ; sa formule fautive de multiplication de fractions p.71 n'est pas utilisée.

Règles : FR-ALGEBRA-B7-RULE-ANNEAUX, FR-ALGEBRA-B7-RULE-PREMIERS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-minimal-prime-reduced-ring}
Let $\mathfrak p$ be a minimal prime of a ring $R$.
Every element of the maximal ideal of $R_{\mathfrak p}$
is nilpotent. If $R$ is reduced then $R_{\mathfrak p}$
is a field.
\end{lemma}

\begin{proof}
If some element $x$ of ${\mathfrak p}R_{\mathfrak p}$
is not nilpotent, then $D(x) \not = \emptyset$, see
Lemma \ref{lemma-Zariski-topology}. This contradicts
the minimality of $\mathfrak p$. If $R$ is reduced,
then ${\mathfrak p}R_{\mathfrak p} = 0$ and
hence it is a field.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-minimal-prime-reduced-ring}
Soit $\mathfrak p$ un idéal premier minimal d'un anneau $R$.
Tout élément de l'idéal maximal de $R_{\mathfrak p}$
est nilpotent. Si $R$ est réduit, alors $R_{\mathfrak p}$
est un corps.
\end{lemma}

\begin{proof}
Si un élément $x$ de ${\mathfrak p}R_{\mathfrak p}$
n'est pas nilpotent, alors $D(x) \not = \emptyset$ ; voir le
lemme \ref{lemma-Zariski-topology}. Cela contredit
la minimalité de $\mathfrak p$. Si $R$ est réduit,
alors ${\mathfrak p}R_{\mathfrak p} = 0$ et
l'anneau local est donc un corps.
\end{proof}
```

</details>

### 03 — lemma-reduced-ring-sub-product-fields

Anglais L4559–4591 ; français L4539–4571.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4559) · FR-ALGEBRA-B7-CHOICE-0003.

Les trois conclusions sont conservées : sous-anneau, plongement précis dans le produit des localisés, puis égalité avec l'ensemble des diviseurs de zéro. Produit ne devient pas somme directe et l'ensemble des premiers minimaux n'est pas déclaré fini. Le raisonnement par noyaux et les deux sens de la caractérisation xy=0 sont intégralement traduits. Le non-zéro de y dans la réciproque découle de y hors du premier ; aucune restriction supplémentaire n'est ajoutée. Les mots minimal dans les indices ont le même graphisme dans les deux langues.

Règles : FR-ALGEBRA-B7-RULE-LOCALISATION, FR-ALGEBRA-B7-RULE-ANNEAUX, FR-ALGEBRA-B7-RULE-PREMIERS, FR-ALGEBRA-B7-RULE-APPLICATIONS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-reduced-ring-sub-product-fields}
Let $R$ be a reduced ring. Then
\begin{enumerate}
\item $R$ is a subring of a product of fields,
\item $R \to \prod_{\mathfrak p\text{ minimal}} R_{\mathfrak p}$
is an embedding into a product of fields,
\item $\bigcup_{\mathfrak p\text{ minimal}} \mathfrak p$ is the set
of zerodivisors of $R$.
\end{enumerate}
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-minimal-prime-reduced-ring} each of the rings
$R_\mathfrak p$ is a field. In particular, the kernel of the ring
map $R \to R_\mathfrak p$ is $\mathfrak p$.
By Lemma \ref{lemma-Zariski-topology}
we have $\bigcap_{\mathfrak p} \mathfrak p = (0)$.
Hence (2) and (1) are true. If $x y = 0$ and $y \not = 0$, then
$y \not \in \mathfrak p$ for some minimal prime $\mathfrak p$.
Hence $x \in \mathfrak p$. Thus every zerodivisor of $R$ is contained
in $\bigcup_{\mathfrak p\text{ minimal}} \mathfrak p$.
Conversely, suppose that $x \in \mathfrak p$ for some minimal
prime $\mathfrak p$. Then $x$ maps to zero in $R_\mathfrak p$,
hence there exists $y \in R$, $y \not \in \mathfrak p$ such that
$xy = 0$. In other words, $x$ is a zerodivisor. This finishes the
proof of (3) and the lemma.
\end{proof}

\noindent
The total ring of fractions $Q(R)$ of a ring $R$ was introduced in
Example \ref{example-localize-at-prime}.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-reduced-ring-sub-product-fields}
Soit $R$ un anneau réduit. Alors
\begin{enumerate}
\item $R$ est un sous-anneau d'un produit de corps,
\item $R \to \prod_{\mathfrak p\text{ minimal}} R_{\mathfrak p}$
est un plongement dans un produit de corps,
\item $\bigcup_{\mathfrak p\text{ minimal}} \mathfrak p$ est l'ensemble
des diviseurs de zéro de $R$.
\end{enumerate}
\end{lemma}

\begin{proof}
D'après le lemme \ref{lemma-minimal-prime-reduced-ring}, chacun des anneaux
$R_\mathfrak p$ est un corps. En particulier, le noyau du morphisme d'anneaux
$R \to R_\mathfrak p$ est $\mathfrak p$.
D'après le lemme \ref{lemma-Zariski-topology},
nous avons $\bigcap_{\mathfrak p} \mathfrak p = (0)$.
Ainsi (2) et (1) sont vraies. Si $x y = 0$ et $y \not = 0$, alors
$y \not \in \mathfrak p$ pour un certain idéal premier minimal $\mathfrak p$.
Par conséquent, $x \in \mathfrak p$. Ainsi, tout diviseur de zéro de $R$ appartient
à $\bigcup_{\mathfrak p\text{ minimal}} \mathfrak p$.
Réciproquement, supposons que $x \in \mathfrak p$ pour un certain idéal
premier minimal $\mathfrak p$. Alors l'image de $x$ dans $R_\mathfrak p$ est nulle ;
il existe donc $y \in R$, $y \not \in \mathfrak p$ tel que
$xy = 0$. Autrement dit, $x$ est un diviseur de zéro. Cela achève la
démonstration de (3) et du lemme.
\end{proof}

\noindent
L'anneau total des fractions $Q(R)$ d'un anneau $R$ a été introduit dans
l'exemple \ref{example-localize-at-prime}.
```

</details>

### 04 — lemma-total-ring-fractions

Anglais L4592–4610 ; français L4572–4590.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4592) · FR-ALGEBRA-B7-CHOICE-0004.

Partie multiplicative et éléments non diviseurs de zéro conservent exactement la condition sur S. L'énoncé identifie deux anneaux totaux de fractions, non R avec son localisé. La démonstration conserve l'implication du non-diviseur x vers le numérateur r, sans ajouter une nouvelle démonstration. Ducros 2.1.3–8 donne le langage de la localisation, des fractions et de sa transitivité ; il ne fournit pas ici l'appellation complète de Q(R). La transition vers le recollement appartient à la paire et reste traduite.

Règles : FR-ALGEBRA-B7-RULE-LOCALISATION.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-total-ring-fractions}
Let $R$ be a ring.
Let $S \subset R$ be a multiplicative subset consisting of nonzerodivisors.
Then $Q(R) \cong Q(S^{-1}R)$.
In particular $Q(R) \cong Q(Q(R))$.
\end{lemma}

\begin{proof}
If $x \in S^{-1}R$ is a nonzerodivisor, and
$x = r/f$ for some $r \in R$, $f \in S$, then
$r$ is a nonzerodivisor in $R$. Whence the lemma.
\end{proof}

\noindent
We can apply glueing results to prove something about
total rings of fractions $Q(R)$ which we introduced in
Example \ref{example-localize-at-prime}.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-total-ring-fractions}
Soit $R$ un anneau.
Soit $S \subset R$ une partie multiplicative formée d'éléments non diviseurs de zéro.
Alors $Q(R) \cong Q(S^{-1}R)$.
En particulier, $Q(R) \cong Q(Q(R))$.
\end{lemma}

\begin{proof}
Si $x \in S^{-1}R$ est un élément non diviseur de zéro et si
$x = r/f$ pour certains $r \in R$, $f \in S$, alors
$r$ est un élément non diviseur de zéro de $R$. Le lemme en résulte.
\end{proof}

\noindent
Nous pouvons appliquer les résultats de recollement pour démontrer une propriété des
anneaux totaux des fractions $Q(R)$, que nous avons introduits dans
l'exemple \ref{example-localize-at-prime}.
```

</details>

### 05 — lemma-total-ring-fractions-no-embedded-points

Anglais L4611–4655 ; français L4591–4635.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4611) · FR-ALGEBRA-B7-CHOICE-0005.

Les deux hypothèses distinctes sont conservées : finitude des premiers minimaux ET égalité de leur réunion avec les diviseurs de zéro. Il n'est ajouté ni réduction de R ni hypothèse noethérienne. Les morphismes naturels partent de Q(R), la comparaison des spectres est faite comme parties de Spec(R), et les Ai sont les facteurs locaux obtenus. Anneau local qui est une localisation n'est pas changé en corps ; les Ai peuvent avoir des nilpotents. La conclusion et la réduction à un ensemble discret fini restent celles de Stacks.

Règles : FR-ALGEBRA-B7-RULE-LOCALISATION, FR-ALGEBRA-B7-RULE-PREMIERS, FR-ALGEBRA-B7-RULE-APPLICATIONS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-total-ring-fractions-no-embedded-points}
Let $R$ be a ring.
Assume that $R$ has finitely many minimal primes
$\mathfrak q_1, \ldots, \mathfrak q_t$, and that
$\mathfrak q_1 \cup \ldots \cup \mathfrak q_t$ is the set
of zerodivisors of $R$.
Then the total ring of fractions $Q(R)$ is equal to
$R_{\mathfrak q_1} \times \ldots \times R_{\mathfrak q_t}$.
\end{lemma}

\begin{proof}
There are natural maps $Q(R) \to R_{\mathfrak q_i}$ since
any nonzerodivisor is contained in $R \setminus \mathfrak q_i$.
Hence a natural map
$Q(R) \to R_{\mathfrak q_1} \times \ldots \times R_{\mathfrak q_t}$.
For any nonminimal prime $\mathfrak p \subset R$ we see that
$\mathfrak p \not \subset \mathfrak q_1 \cup \ldots \cup \mathfrak q_t$
by Lemma \ref{lemma-silly}. Hence
$\Spec(Q(R)) = \{\mathfrak q_1, \ldots, \mathfrak q_t\}$
(as subsets of $\Spec(R)$, see Lemma \ref{lemma-spec-localization}).
Therefore $\Spec(Q(R))$ is a finite discrete set and
it follows that $Q(R) = A_1 \times \ldots \times A_t$
with $\Spec(A_i) = \{\mathfrak{q}_i\}$, see
Lemma \ref{lemma-disjoint-implies-product}.
Moreover $A_i$ is a local ring, which is a localization
of $R$. Hence $A_i \cong R_{\mathfrak q_i}$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-total-ring-fractions-no-embedded-points}
Soit $R$ un anneau.
Supposons que $R$ possède un nombre fini d'idéaux premiers minimaux
$\mathfrak q_1, \ldots, \mathfrak q_t$, et que
$\mathfrak q_1 \cup \ldots \cup \mathfrak q_t$ soit l'ensemble
des diviseurs de zéro de $R$.
Alors l'anneau total des fractions $Q(R)$ est égal à
$R_{\mathfrak q_1} \times \ldots \times R_{\mathfrak q_t}$.
\end{lemma}

\begin{proof}
Il existe des morphismes naturels $Q(R) \to R_{\mathfrak q_i}$ puisque
tout élément non diviseur de zéro appartient à $R \setminus \mathfrak q_i$.
Il existe donc un morphisme naturel
$Q(R) \to R_{\mathfrak q_1} \times \ldots \times R_{\mathfrak q_t}$.
Pour tout idéal premier non minimal $\mathfrak p \subset R$, nous voyons que
$\mathfrak p \not \subset \mathfrak q_1 \cup \ldots \cup \mathfrak q_t$
d'après le lemme \ref{lemma-silly}. Par conséquent,
$\Spec(Q(R)) = \{\mathfrak q_1, \ldots, \mathfrak q_t\}$
(comme sous-ensembles de $\Spec(R)$ ; voir le lemme \ref{lemma-spec-localization}).
Ainsi $\Spec(Q(R))$ est un ensemble discret fini et
il s'ensuit que $Q(R) = A_1 \times \ldots \times A_t$,
avec $\Spec(A_i) = \{\mathfrak{q}_i\}$ ; voir le
lemme \ref{lemma-disjoint-implies-product}.
De plus, $A_i$ est un anneau local qui est une localisation
de $R$. Ainsi $A_i \cong R_{\mathfrak q_i}$.
\end{proof}
```

</details>

### 06 — section-irreducible

Anglais L4656–4663 ; français L4636–4643.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4656) · FR-ALGEBRA-B7-CHOICE-0006.

Composantes irréductibles et idéaux premiers minimaux sont correctement appariés, contrairement à composantes connexes et idempotents du lot précédent. Ducros 4.3.15 et 4.3.22 atteste le vocabulaire de l'irréductibilité et de ses composantes ; sa finitude suppose un espace noethérien et n'est pas importée dans ce titre général.

Règles : FR-ALGEBRA-B7-RULE-PREMIERS, FR-ALGEBRA-B7-RULE-TOPOLOGIE, FR-ALGEBRA-B7-RULE-POLYNOMES.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Irreducible components of spectra}
\label{section-irreducible}

\noindent
We show that irreducible components of
the spectrum of a ring correspond to the
minimal primes in the ring.
```

Français restauré :
```tex
\section{Composantes irréductibles des spectres}
\label{section-irreducible}

\noindent
Nous montrons que les composantes irréductibles du
spectre d'un anneau correspondent aux
idéaux premiers minimaux de l'anneau.
```

</details>

### 07 — lemma-irreducible

Anglais L4664–4705 ; français L4644–4685.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4664) · FR-ALGEBRA-B7-CHOICE-0007.

Adhérence, fermé irréductible, composante et point générique gardent leur sens topologique. Les trois conclusions et la preuve entière conservent la contravariance entre inclusion des idéaux et inclusion des V(I). La fermeture d'un singleton n'est pas remplacée par le singleton. L'unicité du point générique et le terme sobre sont explicitement attestés chez Ducros 4.3.15–16. La transition jusqu'au lemme spectral est incluse ; elle n'identifie pas sobre et spectral. Le cas vide non détaillé dans la preuve anglaise n'est pas réparé silencieusement.

Point particulier à relire : Pour I=R, V(I) est vide et l'étape choisissant a,b hors de I n'est pas possible ; il faut traiter ce cas ou partir d'un fermé irréductible non vide. Cette omission de preuve appartient au texte anglais. La consultation de Ducros confirme la convention non vide mais n'autorise pas à l'ajouter silencieusement ici.

Règles : FR-ALGEBRA-B7-RULE-PREMIERS, FR-ALGEBRA-B7-RULE-TOPOLOGIE, FR-ALGEBRA-B7-RULE-POLYNOMES.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-irreducible}
Let $R$ be a ring.
\begin{enumerate}
\item For a prime $\mathfrak p \subset R$ the closure
of $\{\mathfrak p\}$ in the Zariski topology is $V(\mathfrak p)$.
In a formula $\overline{\{\mathfrak p\}} = V(\mathfrak p)$.
\item The irreducible closed subsets of $\Spec(R)$ are
exactly the subsets $V(\mathfrak p)$, with $\mathfrak p \subset R$
a prime.
\item The irreducible components (see Topology,
Definition \ref{topology-definition-irreducible-components})
of $\Spec(R)$ are  exactly the subsets $V(\mathfrak p)$,
with $\mathfrak p \subset R$ a minimal prime.
\end{enumerate}
\end{lemma}

\begin{proof}
Note that if $ \mathfrak p \in V(I)$, then
$I \subset \mathfrak p$. Hence,
clearly $\overline{\{\mathfrak p\}} = V(\mathfrak p)$.
In particular $V(\mathfrak p)$ is the closure of
a singleton and hence irreducible.
The second assertion implies the third.
To show the second, let
$V(I) \subset \Spec(R)$ with $I$ a radical ideal.
If $I$ is not prime, then choose $a, b\in R$, $a, b\not \in I$
with $ab\in I$. In this case $V(I, a) \cup V(I, b) = V(I)$,
but neither $V(I, b) = V(I)$ nor $V(I, a) = V(I)$, by
Lemma \ref{lemma-Zariski-topology}. Hence $V(I)$ is not
irreducible.
\end{proof}

\noindent
In other words, this lemma shows that every irreducible closed
subset of $\Spec(R)$ is of the form $V(\mathfrak p)$ for
some prime $\mathfrak p$. Since $V(\mathfrak p) = \overline{\{\mathfrak p\}}$
we see that each irreducible closed subset has a unique generic point,
see Topology, Definition \ref{topology-definition-generic-point}.
In particular, $\Spec(R)$ is a sober topological space.
We record this fact in the following lemma.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-irreducible}
Soit $R$ un anneau.
\begin{enumerate}
\item Pour un idéal premier $\mathfrak p \subset R$, l'adhérence
de $\{\mathfrak p\}$ dans la topologie de Zariski est $V(\mathfrak p)$.
Sous forme de formule, $\overline{\{\mathfrak p\}} = V(\mathfrak p)$.
\item Les sous-ensembles fermés irréductibles de $\Spec(R)$ sont
exactement les sous-ensembles $V(\mathfrak p)$, où $\mathfrak p \subset R$
est un idéal premier.
\item Les composantes irréductibles (voir Topologie,
définition \ref{topology-definition-irreducible-components})
de $\Spec(R)$ sont exactement les sous-ensembles $V(\mathfrak p)$,
où $\mathfrak p \subset R$ est un idéal premier minimal.
\end{enumerate}
\end{lemma}

\begin{proof}
Notons que, si $ \mathfrak p \in V(I)$, alors
$I \subset \mathfrak p$. Par conséquent,
il est clair que $\overline{\{\mathfrak p\}} = V(\mathfrak p)$.
En particulier, $V(\mathfrak p)$ est l'adhérence d'un
singleton et est donc irréductible.
La deuxième assertion entraîne la troisième.
Pour démontrer la deuxième, soit
$V(I) \subset \Spec(R)$, où $I$ est un idéal radical.
Si $I$ n'est pas premier, choisissons $a, b\in R$, $a, b\not \in I$
avec $ab\in I$. Dans ce cas, $V(I, a) \cup V(I, b) = V(I)$,
mais ni $V(I, b) = V(I)$ ni $V(I, a) = V(I)$, d'après le
lemme \ref{lemma-Zariski-topology}. Ainsi $V(I)$ n'est pas
irréductible.
\end{proof}

\noindent
Autrement dit, ce lemme montre que tout sous-ensemble fermé irréductible
de $\Spec(R)$ est de la forme $V(\mathfrak p)$ pour
un certain idéal premier $\mathfrak p$. Puisque $V(\mathfrak p) = \overline{\{\mathfrak p\}}$,
nous voyons que tout sous-ensemble fermé irréductible possède un unique point générique ;
voir Topologie, définition \ref{topology-definition-generic-point}.
En particulier, $\Spec(R)$ est un espace topologique sobre.
Consignons ce fait dans le lemme suivant.
```

</details>

### 08 — lemma-spec-spectral

Anglais L4706–4716 ; français L4686–4696.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4706) · FR-ALGEBRA-B7-CHOICE-0008.

Espace spectral reste une propriété topologique, non la simple expression espace muni d'un spectre. Le renvoi à la définition et les deux lemmes utilisés sont inchangés. Les pages de Ducros consultées attestent sobre, pas le terme spectral ni l'ensemble des axiomes de cette notion. Ce choix est donc retenu par correspondance avec la définition officielle et la continuité terminologique, avec cette limite d'attestation explicitement signalée.

Point particulier à relire : Sobre est attesté directement ; spectral ne l'est pas dans les pages utilisées. Aucun certificat terminologique indépendant exhaustif n'est revendiqué.

Règles : FR-ALGEBRA-B7-RULE-TOPOLOGIE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-spec-spectral}
The spectrum of a ring is a spectral space, see Topology, Definition
\ref{topology-definition-spectral-space}.
\end{lemma}

\begin{proof}
Formally this follows from Lemma \ref{lemma-irreducible} and
Lemma \ref{lemma-topology-spec}. See also discussion above.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-spec-spectral}
Le spectre d'un anneau est un espace spectral ; voir Topologie, définition
\ref{topology-definition-spectral-space}.
\end{lemma}

\begin{proof}
Formellement, cela résulte du lemme \ref{lemma-irreducible} et du
lemme \ref{lemma-topology-spec}. Voir aussi la discussion ci-dessus.
\end{proof}
```

</details>

### 09 — lemma-irreducible-components-containing-x

Anglais L4717–4737 ; français L4697–4717.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4717) · FR-ALGEBRA-B7-CHOICE-0009.

Passant par signifie contenant le point, pas ayant ce point pour point générique. La première correspondance concerne tous les premiers du localisé ; la seconde concerne ses premiers minimaux. Le français maintient la localisation en p et la relation q incluse dans p. Correspondance bijective traduit one-to-one correspondence et n'impose pas que ces ensembles portent la même topologie.

Règles : FR-ALGEBRA-B7-RULE-PREMIERS, FR-ALGEBRA-B7-RULE-TOPOLOGIE, FR-ALGEBRA-B7-RULE-POLYNOMES, FR-ALGEBRA-B7-RULE-APPLICATIONS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-irreducible-components-containing-x}
Let $R$ be a ring. Let $\mathfrak p \subset R$ be a prime.
\begin{enumerate}
\item the set of irreducible closed subsets of $\Spec(R)$
passing through $\mathfrak p$ is in one-to-one correspondence with
primes $\mathfrak q \subset R_{\mathfrak p}$.
\item The set of irreducible components of $\Spec(R)$ passing through
$\mathfrak p$ is in one-to-one correspondence with minimal
primes $\mathfrak q \subset R_{\mathfrak p}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Follows from Lemma \ref{lemma-irreducible}
and the description of $\Spec(R_\mathfrak p)$ in
Lemma \ref{lemma-spec-localization} which shows that
$\Spec(R_\mathfrak p)$ corresponds to primes $\mathfrak q$ in $R$
with $\mathfrak q \subset \mathfrak p$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-irreducible-components-containing-x}
Soit $R$ un anneau. Soit $\mathfrak p \subset R$ un idéal premier.
\begin{enumerate}
\item L'ensemble des sous-ensembles fermés irréductibles de $\Spec(R)$
passant par $\mathfrak p$ est en correspondance bijective avec les
idéaux premiers $\mathfrak q \subset R_{\mathfrak p}$.
\item L'ensemble des composantes irréductibles de $\Spec(R)$ passant par
$\mathfrak p$ est en correspondance bijective avec les idéaux
premiers minimaux $\mathfrak q \subset R_{\mathfrak p}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Cela résulte du lemme \ref{lemma-irreducible}
et de la description de $\Spec(R_\mathfrak p)$ donnée dans le
lemme \ref{lemma-spec-localization}, qui montre que
$\Spec(R_\mathfrak p)$ correspond aux idéaux premiers $\mathfrak q$ de $R$
tels que $\mathfrak q \subset \mathfrak p$.
\end{proof}
```

</details>

### 10 — lemma-standard-open-containing-maximal-point

Anglais L4738–4757 ; français L4718–4737.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4738) · FR-ALGEBRA-B7-CHOICE-0010.

Le label historique contenant maximal n'est pas pris pour une hypothèse : le texte requiert bien p minimal. W est quasi-compact et ne contient pas p ; D(f) est disjoint de W et contient p. La preuve garde la famille finie des gi, leurs exposants éventuellement différents ni et le même f pour tous les indices. Ouverts affines principaux est compatible avec les D(gi) de la source. Ni nilpotence uniforme de l'idéal ni couverture totale du spectre ne sont ajoutées.

Règles : FR-ALGEBRA-B7-RULE-ANNEAUX, FR-ALGEBRA-B7-RULE-PREMIERS, FR-ALGEBRA-B7-RULE-TOPOLOGIE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-standard-open-containing-maximal-point}
Let $R$ be a ring.
Let $\mathfrak p$ be a minimal prime of $R$.
Let $W \subset \Spec(R)$ be a quasi-compact open
not containing the point $\mathfrak p$. Then there
exists an $f \in R$, $f \not \in \mathfrak p$ such
that $D(f) \cap W = \emptyset$.
\end{lemma}

\begin{proof}
Since $W$ is quasi-compact we may write it as a finite union
of standard affine opens $D(g_i)$, $i = 1, \ldots, n$.
Since $\mathfrak p \not \in W$ we have $g_i \in \mathfrak p$ for
all $i$. By Lemma \ref{lemma-minimal-prime-reduced-ring}
each $g_i$ is nilpotent in $R_{\mathfrak p}$. Hence we can find
an $f \in R$, $f \not \in \mathfrak p$ such that for all $i$ we have
$f g_i^{n_i} = 0$ for some $n_i > 0$. Then $D(f)$ works.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-standard-open-containing-maximal-point}
Soit $R$ un anneau.
Soit $\mathfrak p$ un idéal premier minimal de $R$.
Soit $W \subset \Spec(R)$ un ouvert quasi-compact
qui ne contient pas le point $\mathfrak p$. Alors il
existe $f \in R$, $f \not \in \mathfrak p$, tel
que $D(f) \cap W = \emptyset$.
\end{lemma}

\begin{proof}
Puisque $W$ est quasi-compact, nous pouvons l'écrire comme réunion finie
d'ouverts affines principaux $D(g_i)$, $i = 1, \ldots, n$.
Puisque $\mathfrak p \not \in W$, nous avons $g_i \in \mathfrak p$ pour
tout $i$. D'après le lemme \ref{lemma-minimal-prime-reduced-ring},
chaque $g_i$ est nilpotent dans $R_{\mathfrak p}$. Nous pouvons donc trouver
$f \in R$, $f \not \in \mathfrak p$, tel que, pour tout $i$, nous ayons
$f g_i^{n_i} = 0$ pour un certain $n_i > 0$. Alors $D(f)$ convient.
\end{proof}
```

</details>

### 11 — lemma-ring-with-only-minimal-primes

Anglais L4758–4815 ; français L4738–4795.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4758) · FR-ALGEBRA-B7-CHOICE-0011.

Séparé traduit Hausdorff dans le contexte explicitement topologique, et non la séparation d'un morphisme de schémas. Totalement discontinu n'est pas remplacé par discret. La liste garde ses huit conditions mathématiques, son neuvième item éditorial et les deux preuves. La quasi-compacité du spectre et l'absence de spécialisations non triviales ne sont pas renforcées en finitude du spectre. La tournure française au féminin pour conditions est une adaptation grammaticale légitime. Les termes profini et totalement discontinu n'ont pas d'attestation indépendante nouvelle dans les pages lues ; ils sont retenus au regard des définitions citées et non déclarés nouvellement certifiés par Ducros.

Point particulier à relire : Le neuvième item « ajouter d'autres conditions ici » est l'instruction éditoriale littérale du témoin. Ce n'est ni une instruction pour ce travail ni une neuvième propriété mathématique prouvée. Il reste visible dans la traduction fidèle.

Règles : FR-ALGEBRA-B7-RULE-PREMIERS, FR-ALGEBRA-B7-RULE-TOPOLOGIE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ring-with-only-minimal-primes}
Let $R$ be a ring. Let $X = \Spec(R)$ as a topological space.
The following are equivalent
\begin{enumerate}
\item $X$ is profinite,
\item $X$ is Hausdorff,
\item $X$ is totally disconnected.
\item every quasi-compact open of $X$ is closed,
\item there are no nontrivial inclusions between its prime ideals,
\item every prime ideal is a maximal ideal,
\item every prime ideal is minimal,
\item every standard open $D(f) \subset X$ is closed, and
\item add more here.
\end{enumerate}
\end{lemma}

\begin{proof}
First proof. It is clear that (5), (6), and (7) are equivalent.
It is clear that (4) and (8) are equivalent as every quasi-compact
open is a finite union of standard opens.
The implication (7) $\Rightarrow$ (4) follows from
Lemma \ref{lemma-standard-open-containing-maximal-point}.
Assume (4) holds. Let $\mathfrak p, \mathfrak p'$ be distinct
primes of $R$. Choose an $f \in \mathfrak p'$, $f \not \in \mathfrak p$
(if needed switch $\mathfrak p$ with $\mathfrak p'$).
Then $\mathfrak p' \not \in D(f)$ and $\mathfrak p \in D(f)$.
By (4) the open $D(f)$ is also closed.
Hence $\mathfrak p$ and $\mathfrak p'$ are in disjoint open
neighbourhoods whose union is $X$. Thus $X$ is Hausdorff and totally
disconnected. Thus (4) $\Rightarrow$ (2) and (3).
If (3) holds then there cannot be any specializations
between points of $\Spec(R)$ and we see that (5) holds.
If $X$ is Hausdorff then every point is closed, so (2) implies (6).
Thus (2), (3), (4), (5), (6), (7) and (8) are equivalent.
Any profinite space is Hausdorff, so (1) implies (2).
If $X$ satisfies (2) and (3), then $X$ (being quasi-compact by
Lemma \ref{lemma-quasi-compact}) is profinite by
Topology, Lemma \ref{topology-lemma-profinite}.

\medskip\noindent
Second proof. Besides the equivalence of (4) and (8) this follows
from Lemma \ref{lemma-spec-spectral} and purely topological facts, see
Topology, Lemma \ref{topology-lemma-characterize-profinite-spectral}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ring-with-only-minimal-primes}
Soit $R$ un anneau. Soit $X = \Spec(R)$ comme espace topologique.
Les conditions suivantes sont équivalentes :
\begin{enumerate}
\item $X$ est profini,
\item $X$ est séparé,
\item $X$ est totalement discontinu.
\item tout ouvert quasi-compact de $X$ est fermé,
\item il n'existe aucune inclusion non triviale entre ses idéaux premiers,
\item tout idéal premier est un idéal maximal,
\item tout idéal premier est minimal,
\item tout ouvert principal $D(f) \subset X$ est fermé, et
\item ajouter d'autres conditions ici.
\end{enumerate}
\end{lemma}

\begin{proof}
Première démonstration. Il est clair que (5), (6) et (7) sont équivalentes.
Il est clair que (4) et (8) sont équivalentes, puisque tout ouvert quasi-compact
est une réunion finie d'ouverts principaux.
L'implication (7) $\Rightarrow$ (4) résulte du
lemme \ref{lemma-standard-open-containing-maximal-point}.
Supposons (4). Soient $\mathfrak p, \mathfrak p'$ deux idéaux premiers
distincts de $R$. Choisissons $f \in \mathfrak p'$, $f \not \in \mathfrak p$
(au besoin, échangeons $\mathfrak p$ et $\mathfrak p'$).
Alors $\mathfrak p' \not \in D(f)$ et $\mathfrak p \in D(f)$.
D'après (4), l'ouvert $D(f)$ est également fermé.
Ainsi $\mathfrak p$ et $\mathfrak p'$ appartiennent à des voisinages ouverts
disjoints dont la réunion est $X$. Par conséquent, $X$ est séparé et totalement
discontinu. Ainsi (4) $\Rightarrow$ (2) et (3).
Si (3) est satisfaite, il ne peut exister aucune spécialisation
entre les points de $\Spec(R)$, et nous voyons que (5) est satisfaite.
Si $X$ est séparé, tout point est fermé, donc (2) entraîne (6).
Ainsi (2), (3), (4), (5), (6), (7) et (8) sont équivalentes.
Tout espace profini est séparé, donc (1) entraîne (2).
Si $X$ satisfait (2) et (3), alors $X$ (qui est quasi-compact d'après le
lemme \ref{lemma-quasi-compact}) est profini d'après
Topologie, lemme \ref{topology-lemma-profinite}.

\medskip\noindent
Deuxième démonstration. Outre l'équivalence de (4) et (8), cela résulte
du lemme \ref{lemma-spec-spectral} et de faits purement topologiques ; voir
Topologie, lemme \ref{topology-lemma-characterize-profinite-spectral}.
\end{proof}
```

</details>

### 12 — section-examples-spectra

Anglais L4816–4821 ; français L4796–4801.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4816) · FR-ALGEBRA-B7-CHOICE-0012.

Le titre et l'introduction annoncent des exemples, sans leur attribuer la valeur d'une classification générale corrigée. Tout le texte des quatre exemples suivants est comparé. Les difficultés de leurs preuves sont consignées à part, et non absorbées dans la traduction.

Règles : Titre et contexte directement comparés.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Examples of spectra of rings}
\label{section-examples-spectra}

\noindent
In this section we put some examples of spectra.
```

Français restauré :
```tex
\section{Exemples de spectres d'anneaux}
\label{section-examples-spectra}

\noindent
Dans cette section, nous donnons quelques exemples de spectres.
```

</details>

### 13 — example-spec-Zxmodx2minus4

Anglais L4822–4862 ; français L4802–4842.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4822) · FR-ALGEBRA-B7-CHOICE-0013.

Les trois cas de contraction vers Z restent (2), (q) avec q>2, puis (0). L'anneau principal est un anneau intègre à idéaux principaux : PID n'est pas traduit par domaine principal ni par anneau factoriel seul. Les deux racines, leurs signes et le point unique au-dessus de 2 sont préservés. Le passage du quotient à son anneau polynomial ambiant conserve les abus de notation d'idéaux de l'anglais sans créer un nouvel idéal. Ducros 4.2.1–5 atteste le même registre des fibres et des points de spectres arithmétiques, sans être la source de cet exemple particulier.

Règles : FR-ALGEBRA-B7-RULE-ANNEAUX, FR-ALGEBRA-B7-RULE-PREMIERS, FR-ALGEBRA-B7-RULE-APPLICATIONS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-spec-Zxmodx2minus4}
In this example we describe $X = \Spec(\mathbf{Z}[x]/(x^2 - 4))$.
Let $\mathfrak{p}$ be an arbitrary prime in $X$.
Let $\phi : \mathbf{Z} \to \mathbf{Z}[x]/(x^2 - 4)$ be the natural ring map.
Then, $ \phi^{-1}(\mathfrak p)$ is a prime in $\mathbf{Z}$.
If $ \phi^{-1}(\mathfrak p) = (2)$, then since $\mathfrak p$ contains $2$,
it corresponds to a prime ideal in
$\mathbf{Z}[x]/(x^2 - 4, 2) \cong (\mathbf{Z}/2\mathbf{Z})[x]/(x^2)$
via the map $ \mathbf{Z}[x]/(x^2 - 4) \to  \mathbf{Z}[x]/(x^2 - 4, 2)$.
Any prime in $(\mathbf{Z}/2\mathbf{Z})[x]/(x^2)$ corresponds to a prime
in $(\mathbf{Z}/2\mathbf{Z})[x]$ containing $(x^2)$.  Such primes will
then contain $x$.  Since
$(\mathbf{Z}/2\mathbf{Z}) \cong (\mathbf{Z}/2\mathbf{Z})[x]/(x)$ is a field,
$(x)$ is a maximal ideal.  Since any prime contains $(x)$ and $(x)$ is
maximal, the ring contains only one prime $(x)$.  Thus, in this case,
$\mathfrak p = (2, x)$.  Now, if $ \phi^{-1}(\mathfrak p) = (q)$ for
$q > 2$, then since $\mathfrak p$ contains $q$, it corresponds to a
prime ideal in
$\mathbf{Z}[x]/(x^2 - 4, q) \cong (\mathbf{Z}/q\mathbf{Z})[x]/(x^2 - 4)$
via the map $ \mathbf{Z}[x]/(x^2 - 4) \to  \mathbf{Z}[x]/(x^2 - 4, q)$.
Any prime in $(\mathbf{Z}/q\mathbf{Z})[x]/(x^2 - 4)$ corresponds to a
prime in $(\mathbf{Z}/q\mathbf{Z})[x]$ containing $(x^2 - 4) = (x -2)(x + 2)$.
Hence, these primes must contain either $x -2$ or $x + 2$.  Since
$(\mathbf{Z}/q\mathbf{Z})[x]$ is a PID, all nonzero
primes are maximal, and so there
are precisely 2 primes in $(\mathbf{Z}/q\mathbf{Z})[x]$ containing
$(x-2)(x + 2)$, namely $(x-2)$ and $(x + 2)$.  In conclusion, there exist two
primes $(q, x-2)$ and $(q, x + 2)$ since $2 \neq -2 \in \mathbf{Z}/(q)$.
Finally, we treat the case where $\phi^{-1}(\mathfrak p) = (0)$.  Notice
that $\mathfrak p$ corresponds to a prime ideal in $\mathbf{Z}[x]$ that
contains $(x^2 - 4) = (x -2)(x + 2)$.  Hence, $\mathfrak p$ contains either
$(x-2)$ or $(x + 2)$.  Hence, $\mathfrak p$ corresponds to a prime in
$\mathbf{Z}[x]/(x - 2)$ or one in $\mathbf{Z}[x]/(x + 2)$ that intersects
$\mathbf{Z}$ only at $0$, by assumption.  Since
$\mathbf{Z}[x]/(x - 2) \cong \mathbf{Z}$ and
$\mathbf{Z}[x]/(x + 2) \cong \mathbf{Z}$, this means that $\mathfrak p$
must correspond to $0$ in one of these rings.  Thus,
$\mathfrak p = (x - 2)$ or $\mathfrak p = (x + 2)$ in the original ring.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-spec-Zxmodx2minus4}
Dans cet exemple, nous décrivons $X = \Spec(\mathbf{Z}[x]/(x^2 - 4))$.
Soit $\mathfrak{p}$ un idéal premier arbitraire de $X$.
Soit $\phi : \mathbf{Z} \to \mathbf{Z}[x]/(x^2 - 4)$ le morphisme d'anneaux naturel.
Alors $ \phi^{-1}(\mathfrak p)$ est un idéal premier de $\mathbf{Z}$.
Si $ \phi^{-1}(\mathfrak p) = (2)$, alors, puisque $\mathfrak p$ contient $2$,
il correspond à un idéal premier de
$\mathbf{Z}[x]/(x^2 - 4, 2) \cong (\mathbf{Z}/2\mathbf{Z})[x]/(x^2)$
via le morphisme $ \mathbf{Z}[x]/(x^2 - 4) \to  \mathbf{Z}[x]/(x^2 - 4, 2)$.
Tout idéal premier de $(\mathbf{Z}/2\mathbf{Z})[x]/(x^2)$ correspond à un idéal premier
de $(\mathbf{Z}/2\mathbf{Z})[x]$ contenant $(x^2)$. Un tel idéal premier
contient alors $x$. Puisque
$(\mathbf{Z}/2\mathbf{Z}) \cong (\mathbf{Z}/2\mathbf{Z})[x]/(x)$ est un corps,
$(x)$ est un idéal maximal. Puisque tout idéal premier contient $(x)$ et que $(x)$ est
maximal, l'anneau ne possède qu'un seul idéal premier, $(x)$. Ainsi, dans ce cas,
$\mathfrak p = (2, x)$. Maintenant, si $ \phi^{-1}(\mathfrak p) = (q)$ pour
$q > 2$, alors, puisque $\mathfrak p$ contient $q$, il correspond à un
idéal premier de
$\mathbf{Z}[x]/(x^2 - 4, q) \cong (\mathbf{Z}/q\mathbf{Z})[x]/(x^2 - 4)$
via le morphisme $ \mathbf{Z}[x]/(x^2 - 4) \to  \mathbf{Z}[x]/(x^2 - 4, q)$.
Tout idéal premier de $(\mathbf{Z}/q\mathbf{Z})[x]/(x^2 - 4)$ correspond à un
idéal premier de $(\mathbf{Z}/q\mathbf{Z})[x]$ contenant $(x^2 - 4) = (x -2)(x + 2)$.
Par conséquent, ces idéaux premiers doivent contenir soit $x -2$, soit $x + 2$. Puisque
$(\mathbf{Z}/q\mathbf{Z})[x]$ est un anneau principal, tous les idéaux premiers
non nuls sont maximaux, et il existe donc
exactement deux idéaux premiers de $(\mathbf{Z}/q\mathbf{Z})[x]$ contenant
$(x-2)(x + 2)$, à savoir $(x-2)$ et $(x + 2)$. En conclusion, il existe deux
idéaux premiers $(q, x-2)$ et $(q, x + 2)$ puisque $2 \neq -2 \in \mathbf{Z}/(q)$.
Enfin, traitons le cas où $\phi^{-1}(\mathfrak p) = (0)$. Remarquons
que $\mathfrak p$ correspond à un idéal premier de $\mathbf{Z}[x]$ qui
contient $(x^2 - 4) = (x -2)(x + 2)$. Ainsi, $\mathfrak p$ contient soit
$(x-2)$, soit $(x + 2)$. Par conséquent, $\mathfrak p$ correspond à un idéal premier de
$\mathbf{Z}[x]/(x - 2)$ ou de $\mathbf{Z}[x]/(x + 2)$ dont l'intersection
avec $\mathbf{Z}$ est réduite à $0$, par hypothèse. Puisque
$\mathbf{Z}[x]/(x - 2) \cong \mathbf{Z}$ et
$\mathbf{Z}[x]/(x + 2) \cong \mathbf{Z}$, cela signifie que $\mathfrak p$
doit correspondre à $0$ dans l'un de ces anneaux. Ainsi,
$\mathfrak p = (x - 2)$ ou $\mathfrak p = (x + 2)$ dans l'anneau initial.
\end{example}
```

</details>

### 14 — example-spec-Zx

Anglais L4863–4888 ; français L4843–4868.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4863) · FR-ALGEBRA-B7-CHOICE-0014.

Deux qualifications françaises non nul, absentes de l'anglais, sont retirées au début et à la conclusion du cas de contraction nulle. Elles rendaient une partie de l'argument plus exacte mais ne relevaient pas de la traduction. La source omet aussi le premier (q) dans la fibre fermée, et le degré minimal d'un relevé ne garantit pas son contenu 1 : ces points sont conservés dans le dossier, pas corrigés dans le corps. Anneau euclidien, irréductible et dénominateur commun traduisent l'argument sans substituer la classification de Ducros 4.2.2–3, qui comprend explicitement (0) et (q).

Point particulier à relire : La suppression des deux qualifications françaises restaure une lacune du texte source, pas un résultat exact. Par exemple (0) est premier dans Z[x] et n'est pas engendré par un irréductible ; (q) est premier et correspond au premier nul de Fq[x]. De plus 2x+2 relève le polynôme irréductible 2x+2 de F3[x] avec degré minimal, mais est réductible dans Z[x]. Ces contre-exemples sont séparés de la traduction.

Règles : FR-ALGEBRA-B7-RULE-ANNEAUX, FR-ALGEBRA-B7-RULE-PREMIERS, FR-ALGEBRA-B7-RULE-TOPOLOGIE, FR-ALGEBRA-B7-RULE-POLYNOMES.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-spec-Zx}
In this example we describe $X = \Spec(\mathbf{Z}[x])$.
Fix $\mathfrak p \in X$.
Let $\phi : \mathbf{Z} \to \mathbf{Z}[x]$ and notice
that $\phi^{-1}(\mathfrak p) \in \Spec(\mathbf{Z})$.
If $\phi^{-1}(\mathfrak p) = (q)$ for $q$ a prime number $q > 0$,
then $\mathfrak p$ corresponds to a prime in $(\mathbf{Z}/(q))[x]$,
which must be generated by a polynomial that is irreducible in
$(\mathbf{Z}/(q))[x]$.   If we choose a representative of this polynomial
with minimal degree, then it will also be irreducible in $\mathbf{Z}[x]$.
Hence, in this case $\mathfrak p = (q, f_q)$ where $f_q$ is an irreducible
polynomial in $\mathbf{Z}[x]$ that is irreducible when viewed
in $(\mathbf{Z}/(q) [x])$. Now, assume that $\phi^{-1}(\mathfrak p) = (0)$.
In this case, $\mathfrak p$ must be generated by nonconstant polynomials
which, since $\mathfrak p$ is prime, may be assumed to be irreducible in
$\mathbf{Z}[x]$.  By Gauss' lemma, these polynomials are also irreducible
in $\mathbf{Q}[x]$.  Since $\mathbf{Q}[x]$ is a Euclidean domain, if there
are at least two distinct irreducibles $f, g$ generating $\mathfrak p$,
then $1 = af + bg$ for $a, b \in \mathbf{Q}[x]$.  Multiplying through by
a common denominator, we see that $m = \bar{a}f + \bar{b} g$ for
$\bar{a}, \bar{b} \in \mathbf{Z}[x]$ and nonzero $m \in \mathbf{Z}$.
This is a contradiction.  Hence, $\mathfrak p$ is generated by one
irreducible polynomial in $\mathbf{Z}[x]$.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-spec-Zx}
Dans cet exemple, nous décrivons $X = \Spec(\mathbf{Z}[x])$.
Fixons $\mathfrak p \in X$.
Soit $\phi : \mathbf{Z} \to \mathbf{Z}[x]$ et remarquons
que $\phi^{-1}(\mathfrak p) \in \Spec(\mathbf{Z})$.
Si $\phi^{-1}(\mathfrak p) = (q)$ pour $q$ un nombre premier tel que $q > 0$,
alors $\mathfrak p$ correspond à un idéal premier de $(\mathbf{Z}/(q))[x]$,
qui doit être engendré par un polynôme irréductible dans
$(\mathbf{Z}/(q))[x]$. Si nous choisissons un représentant de ce polynôme
de degré minimal, il sera également irréductible dans $\mathbf{Z}[x]$.
Ainsi, dans ce cas, $\mathfrak p = (q, f_q)$, où $f_q$ est un polynôme
irréductible de $\mathbf{Z}[x]$ qui reste irréductible lorsqu'on le considère
dans $(\mathbf{Z}/(q) [x])$. Supposons maintenant que $\phi^{-1}(\mathfrak p) = (0)$.
Dans ce cas, $\mathfrak p$ doit être engendré par des polynômes non constants
qui, puisque $\mathfrak p$ est premier, peuvent être supposés irréductibles dans
$\mathbf{Z}[x]$. D'après le lemme de Gauss, ces polynômes sont aussi irréductibles
dans $\mathbf{Q}[x]$. Puisque $\mathbf{Q}[x]$ est un anneau euclidien, s'il
existe au moins deux polynômes irréductibles distincts $f, g$ qui engendrent $\mathfrak p$,
alors $1 = af + bg$ pour certains $a, b \in \mathbf{Q}[x]$. En multipliant par
un dénominateur commun, nous voyons que $m = \bar{a}f + \bar{b} g$ pour
certains $\bar{a}, \bar{b} \in \mathbf{Z}[x]$ et un certain $m \in \mathbf{Z}$ non nul.
C'est une contradiction. Ainsi, $\mathfrak p$ est engendré par un
polynôme irréductible de $\mathbf{Z}[x]$.
\end{example}
```

</details>

### 15 — example-spec-kxy

Anglais L4889–4930 ; français L4869–4910.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4889) · FR-ALGEBRA-B7-CHOICE-0015.

Le corps reste arbitraire, tandis que l'exemple de Ducros 4.2.6–11 suppose le corps algébriquement clos : cette hypothèse externe n'est pas importée. UFD devient anneau factoriel ; associates devient associés ; relatively prime devient premiers entre eux. Nonunit est élément non inversible. Chasser les dénominateurs conserve l'opération de multiplication par un dénominateur commun, non une suppression de termes. La preuve entière, y compris ses deux appartenances fautives à k[x] et ses choix de représentants à une unité près, reste celle de la source. Le dossier explique les problèmes de type sans insérer k[x,y] à leur place.

Point particulier à relire : La preuve affiche p,a,b dans k[x] et ah,bh dans k[x], alors que les coefficients de Bézout et les polynômes obtenus en chassant les dénominateurs vivent généralement dans k[x,y]. Elle utilise aussi des égalités après association sans expliciter les unités. Aucun correctif n'est glissé dans les formules.

Règles : FR-ALGEBRA-B7-RULE-LOCALISATION, FR-ALGEBRA-B7-RULE-ANNEAUX, FR-ALGEBRA-B7-RULE-PREMIERS, FR-ALGEBRA-B7-RULE-TOPOLOGIE, FR-ALGEBRA-B7-RULE-POLYNOMES.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-spec-kxy}
In this example we describe $X = \Spec(k[x, y])$
when $k$ is an arbitrary field.
Clearly $(0)$ is prime, and any principal ideal generated by an
irreducible polynomial will also be a prime since $k[x, y]$ is a
unique factorization domain. Now assume $\mathfrak p$ is an
element of $X$ that is not principal. Since $k[x, y]$ is a
Noetherian UFD, the prime ideal $\mathfrak p$ can be generated
by a finite number of irreducible polynomials $(f_1, \ldots, f_n)$.
Now, I claim that if $f, g$ are irreducible polynomials in $k[x, y]$
that are not associates, then $(f, g) \cap k[x] \neq 0$. To do this,
it is enough to show that $f$ and $g$ are relatively prime when
viewed in $k(x)[y]$. In this case, $k(x)[y]$ is a Euclidean domain,
so by applying the Euclidean algorithm and clearing denominators, we
obtain $p = af + bg$ for $p, a, b \in k[x]$. Thus, assume this is not
the case, that is, that some nonunit $h \in k(x)[y]$ divides both
$f$ and $g$. Then, by Gauss's lemma, for some $a, b \in k(x)$ we
have $ah | f$ and $bh | g$ for $ah, bh \in k[x]$. By
irreducibility, $ah = f$ and
$bh = g$ (since $h \notin k(x)$). So, back in $k(x)[y]$, $f, g $
are associates, as $\frac{a}{b} g = f$. Since
$k(x)$ is the fraction field of $k[x]$, we can write $g = \frac{r}{s} f $
for elements $r , s \in k[x]$ sharing no common factors. This
implies that $sg = rf$ in $k[x, y]$ and so $s$ must divide $f$
since $k[x, y]$ is a UFD. Hence, $s = 1$ or $s = f$. If $s = f$,
then $r = g$, implying $f, g \in k[x]$ and thus must be units in
$k(x)$ and relatively prime in $k(x)[y]$, contradicting our
hypothesis. If $s = 1$, then $g = rf$, another contradiction.
Thus, we must have $f, g$ relatively prime in $k(x)[y]$, a
Euclidean domain. Thus, we have reduced to the case $\mathfrak p$
contains some irreducible polynomial $p \in k[x] \subset k[x, y]$.
By the above, $\mathfrak p$ corresponds to a prime in the ring
$k[x, y]/(p) = k(\alpha)[y]$, where $\alpha$ is an element
algebraic over $k$ with minimum polynomial $p$. This is a
PID, and so any prime ideal corresponds to $(0)$ or an
irreducible polynomial in $k(\alpha)[y]$. Thus, $\mathfrak p$
is of the form $(p)$ or $(p, f)$ where $f$ is a
polynomial in $k[x, y]$ that is irreducible in the quotient
$k[x, y]/(p)$.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-spec-kxy}
Dans cet exemple, nous décrivons $X = \Spec(k[x, y])$
lorsque $k$ est un corps arbitraire.
Il est clair que $(0)$ est premier, et tout idéal principal engendré par un
polynôme irréductible est également premier puisque $k[x, y]$ est un
anneau factoriel. Supposons maintenant que $\mathfrak p$ soit un
élément de $X$ qui n'est pas principal. Puisque $k[x, y]$ est un
anneau factoriel noethérien, l'idéal premier $\mathfrak p$ peut être engendré
par un nombre fini de polynômes irréductibles $(f_1, \ldots, f_n)$.
Affirmons maintenant que, si $f, g$ sont des polynômes irréductibles de $k[x, y]$
qui ne sont pas associés, alors $(f, g) \cap k[x] \neq 0$. Pour le montrer,
il suffit d'établir que $f$ et $g$ sont premiers entre eux lorsqu'on les
considère dans $k(x)[y]$. Dans ce cas, $k(x)[y]$ est un anneau euclidien ;
en appliquant l'algorithme d'Euclide et en chassant les dénominateurs, nous
obtenons $p = af + bg$ pour $p, a, b \in k[x]$. Supposons donc que ce ne soit pas
le cas, c'est-à-dire qu'un certain élément non inversible $h \in k(x)[y]$ divise à la fois
$f$ et $g$. Alors, d'après le lemme de Gauss, pour certains $a, b \in k(x)$, nous
avons $ah | f$ et $bh | g$ avec $ah, bh \in k[x]$. Par
irréductibilité, $ah = f$ et
$bh = g$ (puisque $h \notin k(x)$). Ainsi, de retour dans $k(x)[y]$, $f, g $
sont associés, car $\frac{a}{b} g = f$. Puisque
$k(x)$ est le corps des fractions de $k[x]$, nous pouvons écrire $g = \frac{r}{s} f $
pour des éléments $r , s \in k[x]$ sans facteur commun. Cela
entraîne que $sg = rf$ dans $k[x, y]$, et donc que $s$ doit diviser $f$,
puisque $k[x, y]$ est un anneau factoriel. Ainsi, $s = 1$ ou $s = f$. Si $s = f$,
alors $r = g$, ce qui entraîne $f, g \in k[x]$ ; ils doivent donc être des unités de
$k(x)$ et être premiers entre eux dans $k(x)[y]$, en contradiction avec notre
hypothèse. Si $s = 1$, alors $g = rf$, autre contradiction.
Ainsi, $f, g$ doivent être premiers entre eux dans $k(x)[y]$, qui est un
anneau euclidien. Nous nous sommes donc ramenés au cas où $\mathfrak p$
contient un polynôme irréductible $p \in k[x] \subset k[x, y]$.
D'après ce qui précède, $\mathfrak p$ correspond à un idéal premier de l'anneau
$k[x, y]/(p) = k(\alpha)[y]$, où $\alpha$ est un élément
algébrique sur $k$ de polynôme minimal $p$. Cet anneau est
principal, et tout idéal premier correspond donc à $(0)$ ou à un
polynôme irréductible de $k(\alpha)[y]$. Ainsi, $\mathfrak p$
est de la forme $(p)$ ou $(p, f)$, où $f$ est un
polynôme de $k[x, y]$ qui est irréductible dans le quotient
$k[x, y]/(p)$.
\end{example}
```

</details>

### 16 — example-affine-open-not-standard

Anglais L4931–5088 ; français L4911–5068.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4931) · FR-ALGEBRA-B7-CHOICE-0016.

Toutes les étapes sont conservées : présentation de R, surjectivité par divisions, construction de Ra, évaluations, idéaux maximaux, deux ouverts, homéomorphisme et argument des unités. Deux écarts de prose sont rétablis : former redevient premier plutôt que dernier, et maximal ideal redevient idéal maximal plutôt qu'élément. Le premier rétablit la direction du renvoi sans résoudre son ambiguïté ; le second conserve une erreur mathématique anglaise identifiable. Les trois mots de liaison dans les affichages sont les seules différences admises entre régions mathématiques. De type fini ne signifie pas anneau fini ; homéomorphisme local injectif ne signifie pas isomorphisme d'anneaux. Les formules problématiques et l'explication finale des paramètres ne sont ni complétées ni normalisées.

Point particulier à relire : La source contient notamment h au lieu de g au degré <2, un terme constant a omis, 2a-a au lieu du 2a-2 voisin, un renvoi former ambigu, la confusion entre inverser z-a et localiser en l'idéal (z-a), et un dernier usage de k,ell non introduits. Son assertion sur toute localisation a l'exception des localisations triviales. Le rétablissement littéral n'approuve pas ces lignes ; consulter les observations séparées et les opérations avant/après.

Règles : FR-ALGEBRA-B7-RULE-LOCALISATION, FR-ALGEBRA-B7-RULE-ANNEAUX, FR-ALGEBRA-B7-RULE-PREMIERS, FR-ALGEBRA-B7-RULE-TOPOLOGIE, FR-ALGEBRA-B7-RULE-POLYNOMES, FR-ALGEBRA-B7-RULE-APPLICATIONS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-affine-open-not-standard}
Consider the ring
$$
R = \{ f \in \mathbf{Q}[z]\text{ with }f(0) = f(1) \}.
$$
Consider the map
$$
\varphi : \mathbf{Q}[A, B] \to R
$$
defined by $\varphi(A) = z^2-z$ and $\varphi(B) = z^3-z^2$.  It is
easily checked that $(A^3 - B^2 + AB) \subset \Ker(\varphi)$ and that
$A^3 - B^2 + AB$ is irreducible. Assume that $\varphi$ is surjective;
then since $R$ is an integral domain (it is a subring of an integral
domain), $\Ker(\varphi)$ must be a prime ideal of $\mathbf{Q}[A, B]$.
The prime ideals which contain $(A^3-B^2 + AB)$ are $(A^3-B^2 + AB)$
itself and any maximal ideal $(f, g)$ with $f, g\in\mathbf{Q}[A, B]$
such that $f$ is irreducible mod $g$. But $R$ is not a field, so the
kernel must be $(A^3-B^2 + AB)$; hence $\varphi$ gives an isomorphism
$R \to \mathbf{Q}[A, B]/(A^3-B^2 + AB)$.

\medskip\noindent
To see that $\varphi$ is surjective, we must express any
$f\in R$ as a $\mathbf{Q}$-coefficient polynomial in $A(z) = z^2-z$
and $B(z) = z^3-z^2$. Note the relation $zA(z) = B(z)$. Let
$a = f(0) = f(1)$. Then $z(z-1)$ must divide $f(z)-a$, so we can write
$f(z) = z(z-1)g(z)+a = A(z)g(z)+a$.  If $\deg(g) < 2$, then
$h(z) = c_1z + c_0$ and $f(z) = A(z)(c_1z + c_0)+a = c_1B(z)+c_0A(z)+a$, so we
are done.  If $\deg(g)\geq 2$, then by the polynomial division
algorithm, we can write $g(z) = A(z)h(z)+b_1z + b_0$
($\deg(h)\leq\deg(g)-2$), so $f(z) = A(z)^2h(z)+b_1B(z)+b_0A(z)$.
Applying division to $h(z)$ and iterating, we obtain an expression
for $f(z)$ as a polynomial in $A(z)$ and $B(z)$; hence $\varphi$ is
surjective.

\medskip\noindent
Now let $a \in \mathbf{Q}$, $a \neq 0, \frac{1}{2}, 1$ and
consider
$$
R_a = \{ f \in \mathbf{Q}[z, \frac{1}{z-a}]\text{ with }f(0) = f(1)
\}.
$$
This is a finitely generated $\mathbf{Q}$-algebra as well: it is
easy to check that the functions $z^2-z$, $z^3-z$, and
$\frac{a^2-a}{z-a}+z$ generate $R_a$ as an $\mathbf{Q}$-algebra.  We
have the following inclusions:
$$
R\subset R_a\subset\mathbf{Q}[z, \frac{1}{z-a}], \quad
R\subset\mathbf{Q}[z]\subset\mathbf{Q}[z, \frac{1}{z-a}].
$$
Recall (Lemma \ref{lemma-spec-localization}) that for a ring T and a
multiplicative subset $S\subset T$, the ring map $T \to S^{-1}T$
induces a map on spectra $\Spec(S^{-1}T) \to \Spec(T)$
which is a homeomorphism onto the subset
$$
\{\mathfrak p \in \Spec(T) \mid S \cap \mathfrak p = \emptyset\}
\subset \Spec(T).
$$
When $S = \{ 1, f, f^2, \ldots\}$ for some $f\in T$, this is
the open set $D(f)\subset T$.  We now verify a corresponding
property for the ring map $R \to R_a$: we will show that the map
$\theta : \Spec(R_a) \to \Spec(R)$ induced by inclusion
$R\subset R_a$ is a homeomorphism onto an open subset of
$\Spec(R)$ by verifying that $\theta$ is an injective local
homeomorphism.  We do so with respect to an open cover of
$\Spec(R_a)$ by two distinguished opens, as we now describe.
For any $r\in\mathbf{Q}$, let $\text{ev}_r : R \to \mathbf{Q}$ be the
homomorphism given by evaluation at $r$.  Note that for $r = 0$ and
$r = 1-a$, this can be extended to a homomorphism
$\text{ev}_r' : R_a \to \mathbf{Q}$ (the latter because $\frac{1}{z-a}$
is well-defined at $z = 1-a$, since $a\neq\frac{1}{2}$).  However,
$\text{ev}_a$ does not extend to $R_a$.  Write
$\mathfrak{m}_r = \Ker(\text{ev}_r)$. We have
$$
\mathfrak{m}_0 = (z^2-z, z^3-z),
$$
$$
\mathfrak{m}_a = ((z-1 + a)(z-a), (z^2-1 + a)(z-a)), \text{ and}
$$
$$
\mathfrak{m}_{1-a} = ((z-1 + a)(z-a), (z-1 + a)(z^2-a)).
$$
To verify this, note that the right-hand sides are clearly contained in
the left-hand sides. Then check that the right-hand sides are
maximal ideals by writing the generators in terms of $A$ and $B$,
and viewing $R$ as $\mathbf{Q}[A, B]/(A^3-B^2 + AB)$. Note that
$\mathfrak{m}_a$ is not in the image of $\theta$: we have
$$
(z^2 - z)^2(z - a)\left(\frac{a^2 - a}{z - a} + z\right) =
(z^2 - z)^2(a^2 - a) + (z^2 - z)^2(z - a)z
$$
The left hand side is in $\mathfrak m_a R_a$ because
$(z^2 - z)(z - a)$ is in $\mathfrak m_a$ and because
$(z^2 - z)(\frac{a^2 - a}{z - a} + z)$ is in $R_a$. Similarly
the element $(z^2 - z)^2(z - a)z$ is in $\mathfrak m_a R_a$
because $(z^2 - z)$ is in $R_a$ and $(z^2 - z)(z - a)$ is in $\mathfrak m_a$.
As $a \not \in \{0, 1\}$ we conclude that
$(z^2 - z)^2 \in \mathfrak m_a R_a$. Hence
no ideal $I$ of $R_a$ can satisfy $I \cap R = \mathfrak m_a$, as such
an $I$ would have to contain $(z^2 - z)^2$, which is in $R$ but not in
$\mathfrak m_a$. The distinguished open set
$D((z-1 + a)(z-a))\subset\Spec(R)$ is equal to the complement of
the closed set $\{\mathfrak{m}_a, \mathfrak{m}_{1-a}\}$.
Then check that $R_{(z-1 + a)(z-a)} = (R_a)_{(z-1 + a)(z-a)}$; calling
this localized ring $R'$, then, it follows that the map $R \to R'$
factors as $R \to R_a \to R'$.  By Lemma
\ref{lemma-spec-localization}, then, these maps express
$\Spec(R') \subset \Spec(R_a)$ and
$\Spec(R') \subset \Spec(R)$ as open subsets; hence
$\theta : \Spec(R_a) \to \Spec(R)$, when restricted to
$D((z-1 + a)(z-a))$, is a homeomorphism onto an open subset.
Similarly, $\theta$ restricted to
$D((z^2 + z + 2a-2)(z-a)) \subset \Spec(R_a)$ is a homeomorphism
onto the open subset $D((z^2 + z + 2a-2)(z-a)) \subset \Spec(R)$.
Depending on whether $z^2 + z + 2a-2$ is irreducible or not over
$\mathbf{Q}$, this former distinguished open set has complement
equal to one or two closed points along with the closed point
$\mathfrak{m}_a$. Furthermore, the ideal in $R_a$ generated by the
elements $(z^2 + z + 2a-a)(z-a)$ and $(z-1 + a)(z-a)$ is all of $R_a$, so
these two distinguished open sets cover $\Spec(R_a)$. Hence in
order to show that $\theta$ is a homeomorphism onto
$\Spec(R)-\{\mathfrak{m}_a\}$, it suffices to show
that these one or two points can never equal $\mathfrak{m}_{1-a}$.
And this is indeed the case, since $1-a$ is a root of $z^2 + z + 2a-2$
if and only if $a = 0$ or $a = 1$, both of which do not occur.

\medskip\noindent
Despite this homeomorphism which mimics the behavior of a
localization at an element of $R$, while
$\mathbf{Q}[z, \frac{1}{z-a}]$ is the localization of $\mathbf{Q}[z]$
at the maximal ideal $(z-a)$, the ring $R_a$ is {\it not} a
localization of $R$: Any localization $S^{-1}R$ results in more
units than the original ring $R$.  The units of $R$ are
$\mathbf{Q}^\times$, the units of $\mathbf{Q}$.  In fact, it is
easy to see that the units of $R_a$ are $\mathbf{Q}^*$.
Namely, the units of $\mathbf{Q}[z, \frac{1}{z - a}]$ are
$c (z - a)^n$ for $c \in \mathbf{Q}^*$ and $n \in \mathbf{Z}$
and it is clear that these are in $R_a$ only if $n = 0$.
Hence $R_a$ has no more units than
$R$ does, and thus cannot be a localization of $R$.

\medskip\noindent
We used the fact that $a\neq 0, 1$ to ensure that
$\frac{1}{z-a}$ makes sense at $z = 0, 1$.  We used the fact that
$a\neq 1/2$ in a few places: (1) In order to be able to talk about
the kernel of $\text{ev}_{1-a}$ on $R_a$, which ensures that
$\mathfrak{m}_{1-a}$ is a point of $R_a$ (i.e., that $R_a$ is
missing just one point of $R$). (2) At the end in order to conclude
that $(z-a)^{k + \ell}$ can only be in $R$ for $k = \ell = 0$; indeed, if
$a = 1/2$, then this is in $R$ as long as $k + \ell$ is even. Hence
there would indeed be more units in $R_a$ than in $R$, and $R_a$
could possibly be a localization of $R$.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-affine-open-not-standard}
Considérons l'anneau
$$
R = \{ f \in \mathbf{Q}[z]\text{ vérifiant }f(0) = f(1) \}.
$$
Considérons le morphisme
$$
\varphi : \mathbf{Q}[A, B] \to R
$$
défini par $\varphi(A) = z^2-z$ et $\varphi(B) = z^3-z^2$. On vérifie
aisément que $(A^3 - B^2 + AB) \subset \Ker(\varphi)$ et que
$A^3 - B^2 + AB$ est irréductible. Supposons que $\varphi$ soit surjectif ;
alors, puisque $R$ est un anneau intègre (c'est un sous-anneau d'un anneau
intègre), $\Ker(\varphi)$ doit être un idéal premier de $\mathbf{Q}[A, B]$.
Les idéaux premiers qui contiennent $(A^3-B^2 + AB)$ sont $(A^3-B^2 + AB)$
lui-même et tout idéal maximal $(f, g)$, avec $f, g\in\mathbf{Q}[A, B]$,
tel que $f$ soit irréductible modulo $g$. Mais $R$ n'est pas un corps, donc le
noyau doit être $(A^3-B^2 + AB)$ ; ainsi, $\varphi$ donne un isomorphisme
$R \to \mathbf{Q}[A, B]/(A^3-B^2 + AB)$.

\medskip\noindent
Pour voir que $\varphi$ est surjectif, nous devons exprimer tout
$f\in R$ comme un polynôme à coefficients dans $\mathbf{Q}$ en $A(z) = z^2-z$
et $B(z) = z^3-z^2$. Notons la relation $zA(z) = B(z)$. Soit
$a = f(0) = f(1)$. Alors $z(z-1)$ doit diviser $f(z)-a$, et nous pouvons donc écrire
$f(z) = z(z-1)g(z)+a = A(z)g(z)+a$. Si $\deg(g) < 2$, alors
$h(z) = c_1z + c_0$ et $f(z) = A(z)(c_1z + c_0)+a = c_1B(z)+c_0A(z)+a$, et nous
avons terminé. Si $\deg(g)\geq 2$, alors, d'après l'algorithme de division
euclidienne des polynômes, nous pouvons écrire $g(z) = A(z)h(z)+b_1z + b_0$
($\deg(h)\leq\deg(g)-2$), de sorte que $f(z) = A(z)^2h(z)+b_1B(z)+b_0A(z)$.
En appliquant la division à $h(z)$ et en itérant, nous obtenons une expression
de $f(z)$ comme polynôme en $A(z)$ et $B(z)$ ; ainsi, $\varphi$ est
surjectif.

\medskip\noindent
Soit maintenant $a \in \mathbf{Q}$, $a \neq 0, \frac{1}{2}, 1$, et
considérons
$$
R_a = \{ f \in \mathbf{Q}[z, \frac{1}{z-a}]\text{ vérifiant }f(0) = f(1)
\}.
$$
C'est encore une $\mathbf{Q}$-algèbre de type fini : on vérifie
aisément que les fonctions $z^2-z$, $z^3-z$ et
$\frac{a^2-a}{z-a}+z$ engendrent $R_a$ comme $\mathbf{Q}$-algèbre. Nous
avons les inclusions suivantes :
$$
R\subset R_a\subset\mathbf{Q}[z, \frac{1}{z-a}], \quad
R\subset\mathbf{Q}[z]\subset\mathbf{Q}[z, \frac{1}{z-a}].
$$
Rappelons (lemme \ref{lemma-spec-localization}) que, pour un anneau T et une
partie multiplicative $S\subset T$, le morphisme d'anneaux $T \to S^{-1}T$
induit un morphisme sur les spectres $\Spec(S^{-1}T) \to \Spec(T)$
qui est un homéomorphisme sur le sous-ensemble
$$
\{\mathfrak p \in \Spec(T) \mid S \cap \mathfrak p = \emptyset\}
\subset \Spec(T).
$$
Lorsque $S = \{ 1, f, f^2, \ldots\}$ pour un certain $f\in T$, il s'agit
de l'ouvert $D(f)\subset T$. Vérifions maintenant une propriété analogue
pour le morphisme d'anneaux $R \to R_a$ : nous allons montrer que le morphisme
$\theta : \Spec(R_a) \to \Spec(R)$ induit par l'inclusion
$R\subset R_a$ est un homéomorphisme sur un sous-ensemble ouvert de
$\Spec(R)$ en vérifiant que $\theta$ est un homéomorphisme local
injectif. Nous le faisons relativement à un recouvrement ouvert de
$\Spec(R_a)$ par deux ouverts principaux, que nous décrivons maintenant.
Pour tout $r\in\mathbf{Q}$, soit $\text{ev}_r : R \to \mathbf{Q}$ le
morphisme donné par l'évaluation en $r$. Notons que, pour $r = 0$ et
$r = 1-a$, celui-ci se prolonge en un morphisme
$\text{ev}_r' : R_a \to \mathbf{Q}$ (dans le second cas, parce que $\frac{1}{z-a}$
est bien défini en $z = 1-a$, puisque $a\neq\frac{1}{2}$). Toutefois,
$\text{ev}_a$ ne se prolonge pas à $R_a$. Posons
$\mathfrak{m}_r = \Ker(\text{ev}_r)$. Nous avons
$$
\mathfrak{m}_0 = (z^2-z, z^3-z),
$$
$$
\mathfrak{m}_a = ((z-1 + a)(z-a), (z^2-1 + a)(z-a)), \text{ et}
$$
$$
\mathfrak{m}_{1-a} = ((z-1 + a)(z-a), (z-1 + a)(z^2-a)).
$$
Pour le vérifier, notons que les membres de droite sont clairement contenus dans
les membres de gauche. Vérifions ensuite que les membres de droite sont des
idéaux maximaux en écrivant les générateurs en fonction de $A$ et $B$,
et en considérant $R$ comme $\mathbf{Q}[A, B]/(A^3-B^2 + AB)$. Notons que
$\mathfrak{m}_a$ n'appartient pas à l'image de $\theta$ : nous avons
$$
(z^2 - z)^2(z - a)\left(\frac{a^2 - a}{z - a} + z\right) =
(z^2 - z)^2(a^2 - a) + (z^2 - z)^2(z - a)z
$$
Le membre de gauche appartient à $\mathfrak m_a R_a$ parce que
$(z^2 - z)(z - a)$ appartient à $\mathfrak m_a$ et que
$(z^2 - z)(\frac{a^2 - a}{z - a} + z)$ appartient à $R_a$. De même,
l'élément $(z^2 - z)^2(z - a)z$ appartient à $\mathfrak m_a R_a$
parce que $(z^2 - z)$ appartient à $R_a$ et que $(z^2 - z)(z - a)$ appartient à $\mathfrak m_a$.
Comme $a \not \in \{0, 1\}$, nous en concluons que
$(z^2 - z)^2 \in \mathfrak m_a R_a$. Par conséquent,
aucun idéal $I$ de $R_a$ ne peut vérifier $I \cap R = \mathfrak m_a$, car un tel
$I$ devrait contenir $(z^2 - z)^2$, qui appartient à $R$ mais pas à
$\mathfrak m_a$. L'ouvert principal
$D((z-1 + a)(z-a))\subset\Spec(R)$ est égal au complémentaire du
fermé $\{\mathfrak{m}_a, \mathfrak{m}_{1-a}\}$.
Vérifions alors que $R_{(z-1 + a)(z-a)} = (R_a)_{(z-1 + a)(z-a)}$ ; en
notant cet anneau localisé $R'$, il s'ensuit que le morphisme $R \to R'$
se factorise en $R \to R_a \to R'$. D'après le lemme
\ref{lemma-spec-localization}, ces morphismes présentent alors
$\Spec(R') \subset \Spec(R_a)$ et
$\Spec(R') \subset \Spec(R)$ comme des sous-ensembles ouverts ; ainsi,
$\theta : \Spec(R_a) \to \Spec(R)$, restreint à
$D((z-1 + a)(z-a))$, est un homéomorphisme sur un sous-ensemble ouvert.
De même, la restriction de $\theta$ à
$D((z^2 + z + 2a-2)(z-a)) \subset \Spec(R_a)$ est un homéomorphisme
sur le sous-ensemble ouvert $D((z^2 + z + 2a-2)(z-a)) \subset \Spec(R)$.
Selon que $z^2 + z + 2a-2$ est irréductible ou non sur
$\mathbf{Q}$, le complémentaire de ce premier ouvert principal
est constitué d'un ou deux points fermés, ainsi que du point fermé
$\mathfrak{m}_a$. De plus, l'idéal de $R_a$ engendré par les
éléments $(z^2 + z + 2a-a)(z-a)$ et $(z-1 + a)(z-a)$ est égal à $R_a$ tout entier ; ainsi,
ces deux ouverts principaux recouvrent $\Spec(R_a)$. Par conséquent, pour
montrer que $\theta$ est un homéomorphisme sur
$\Spec(R)-\{\mathfrak{m}_a\}$, il suffit de montrer
que ces un ou deux points ne peuvent jamais être égaux à $\mathfrak{m}_{1-a}$.
Et c'est bien le cas, puisque $1-a$ est une racine de $z^2 + z + 2a-2$
si et seulement si $a = 0$ ou $a = 1$, deux cas qui ne se produisent pas.

\medskip\noindent
Malgré cet homéomorphisme, qui imite le comportement d'une
localisation en un élément de $R$, tandis que
$\mathbf{Q}[z, \frac{1}{z-a}]$ est la localisation de $\mathbf{Q}[z]$
en l'idéal maximal $(z-a)$, l'anneau $R_a$ n'est {\it pas} une
localisation de $R$ : toute localisation $S^{-1}R$ produit davantage
d'unités que l'anneau initial $R$. Les unités de $R$ sont
$\mathbf{Q}^\times$, les unités de $\mathbf{Q}$. En fait, il est
facile de voir que les unités de $R_a$ sont $\mathbf{Q}^*$.
En effet, les unités de $\mathbf{Q}[z, \frac{1}{z - a}]$ sont
$c (z - a)^n$ pour $c \in \mathbf{Q}^*$ et $n \in \mathbf{Z}$,
et il est clair que celles-ci n'appartiennent à $R_a$ que si $n = 0$.
Ainsi, $R_a$ ne possède pas davantage d'unités que
$R$ et ne peut donc pas être une localisation de $R$.

\medskip\noindent
Nous avons utilisé le fait que $a\neq 0, 1$ pour garantir que
$\frac{1}{z-a}$ est défini en $z = 0, 1$. Nous avons utilisé le fait que
$a\neq 1/2$ en plusieurs endroits : (1) pour pouvoir parler du
noyau de $\text{ev}_{1-a}$ sur $R_a$, ce qui garantit que
$\mathfrak{m}_{1-a}$ est un point de $R_a$ (c'est-à-dire que $R_a$
ne possède qu'un point de moins que $R$). (2) À la fin, pour conclure
que $(z-a)^{k + \ell}$ ne peut appartenir à $R$ que pour $k = \ell = 0$ ; en effet, si
$a = 1/2$, cet élément appartient à $R$ dès que $k + \ell$ est pair. Il
y aurait alors effectivement davantage d'unités dans $R_a$ que dans $R$, et $R_a$
pourrait éventuellement être une localisation de $R$.
\end{example}
```

</details>

## Observations sur le texte source sans modification du témoin

Ces notes ne font pas partie de la traduction. Le statut proposé ne signifie ni examen humain ni admission comme nouvel erratum.

### FR-ALGEBRA-B7-SOURCE-NOTE-0001

[Source L4690](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4690) — lemma-irreducible.

```tex
If $I$ is not prime, then choose $a, b\in R$, $a, b\not \in I$
```

Le cas I=R donne V(I)=vide, donc non irréductible, mais ne permet aucun choix hors de I. Ajouter un traitement du cas vide serait un amendement de preuve, non une traduction.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B7-SOURCE-NOTE-0002

[Source L4771](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4771) — lemma-ring-with-only-minimal-primes.

```tex
\item add more here.
```

L'item est un emplacement éditorial ; les deux preuves traitent les conditions (1) à (8), pas une propriété (9). Il est conservé comme texte source, sans l'exécuter.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B7-SOURCE-NOTE-0003

[Source L4871](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4871) — example-spec-Zx.

```tex
which must be generated by a polynomial that is irreducible in
```

Le premier nul de Fq[x] correspond à (q) dans Z[x] et n'a pas de générateur irréductible. Dans la fibre de contraction nulle, (0) est aussi premier. Ducros 4.2.2.1 et 4.2.3.1 les donne explicitement. La suppression des ajouts français ne résout pas la classification source.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B7-SOURCE-NOTE-0004

[Source L4873](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4873) — example-spec-Zx.

```tex
with minimal degree, then it will also be irreducible in $\mathbf{Z}[x]$.
```

Contre-exemple à degré minimal seul : modulo 3, 2x+2 est irréductible de degré 1 ; son relevé 2x+2 a degré minimal mais se factorise en 2(x+1) dans Z[x]. Imposer un relevé primitif et de même degré réglerait cette étape ; la source ne le dit pas.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B7-SOURCE-NOTE-0005

[Source L4881](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4881) — example-spec-Zx.

```tex
are at least two distinct irreducibles $f, g$ generating $\mathfrak p$,
```

Deux irréductibles distincts peuvent être associés, par exemple x et -x. Bézout dans Q[x] demande ici non associés. On peut choisir des représentants non associés dans un système convenable, mais cette étape n'est pas explicitée par la source.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B7-SOURCE-NOTE-0006

[Source L4904](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4904) — example-spec-kxy.

```tex
obtain $p = af + bg$ for $p, a, b \in k[x]$. Thus, assume this is not
```

Après Bézout dans k(x)[y], les coefficients après dénominateurs vivent généralement dans k[x,y], pas k[x]. Exemple f=y, g=y²+x sur Q : avec a,b dans Q[x], annuler les coefficients de y² et y force a=b=0, donc aucun p non nul. f et g sont irréductibles non associés. Séparer p dans k[x] et a,b dans k[x,y] est une correction proposée non appliquée.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B7-SOURCE-NOTE-0007

[Source L4907](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4907) — example-spec-kxy.

```tex
have $ah | f$ and $bh | g$ for $ah, bh \in k[x]$. By
```

La phrase suivante suppose h hors de k(x), donc de degré positif en y ; multiplier par un scalaire non nul a de k(x) ne peut donner ah dans k[x]. Le sens visé est k[x,y]. Les égalités après association demandent aussi un choix d'unité, conservé implicite dans le témoin.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B7-SOURCE-NOTE-0008

[Source L4958](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4958) — example-affine-open-not-standard.

```tex
$h(z) = c_1z + c_0$ and $f(z) = A(z)(c_1z + c_0)+a = c_1B(z)+c_0A(z)+a$, so we
```

La condition porte sur deg(g)<2 et f=A g+a ; c'est g, non h encore non défini dans ce cas, qui devrait être linéaire. La formule officielle reste intacte.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B7-SOURCE-NOTE-0009

[Source L4961](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4961) — example-affine-open-not-standard.

```tex
($\deg(h)\leq\deg(g)-2$), so $f(z) = A(z)^2h(z)+b_1B(z)+b_0A(z)$.
```

Substituer g=A h+b1 z+b0 dans f=A g+a donne A²h+b1B+b0A+a. Le terme constant a a disparu de la ligne officielle ; il n'est pas réinséré dans le français fidèle.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B7-SOURCE-NOTE-0010

[Source L5049](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5049) — example-affine-open-not-standard.

```tex
elements $(z^2 + z + 2a-a)(z-a)$ and $(z-1 + a)(z-a)$ is all of $R_a$, so
```

Les ouverts voisins emploient z²+z+2a-2, pas 2a-a. De plus (z²+z+a)(z-a) n'appartient généralement pas à R : ses valeurs en 0 et 1 diffèrent de 2-a. Pour a=3, autorisé, elles valent -9 et -10. Remplacer 2a-a par 2a-2 est un correctif proposé, non appliqué.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B7-SOURCE-NOTE-0011

[Source L5061](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5061) — example-affine-open-not-standard.

```tex
at the maximal ideal $(z-a)$, the ring $R_a$ is {\it not} a
```

Q[z,1/(z-a)] inverse z-a ; Q[z]_(z-a) inverse au contraire les polynômes hors de l'idéal (z-a), où z-a reste non inversible. Ce sont des localisations différentes. Le français avait corrigé le type de localisation ; la fidélité exige de rétablir l'idéal maximal et d'expliquer le problème à part.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B7-SOURCE-NOTE-0012

[Source L5062](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5062) — example-affine-open-not-standard.

```tex
localization of $R$: Any localization $S^{-1}R$ results in more
```

Une localisation qui n'inverse que des unités est isomorphe à R et n'ajoute aucune unité. Dans le contexte d'une extension propre injective, l'argument peut être précisé ; la phrase universelle isolée est excessive. Aucun mot supplémentaire n'est ajouté au témoin.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B7-SOURCE-NOTE-0013

[Source L5046](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5046) — example-affine-open-not-standard.

```tex
$\mathbf{Q}$, this former distinguished open set has complement
```

Deux mentions du même D(polynôme), dans Spec(Ra) puis dans Spec(R), précèdent former. Mais ma n'est pas un point de Spec(Ra), d'après le passage antérieur. La restauration premier préserve le renvoi anglais sans prétendre lever l'ambiguïté de son antécédent.

Confiance éditoriale : modérée, interprétation à réexaminer ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B7-SOURCE-NOTE-0014

[Source L5079](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5079) — example-affine-open-not-standard.

```tex
that $(z-a)^{k + \ell}$ can only be in $R$ for $k = \ell = 0$; indeed, if
```

La fin réemploie k et ell sans les définir dans cet exemple, après avoir employé n entier. Si k et ell sont des entiers quelconques, k=1,ell=-1 donne la puissance 0 dans R sans les annuler tous deux. Une ancienne convention non écrite sur leurs signes ne peut pas être supposée. Le passage est conservé et le doute est distinct des erreurs de traduction.

Confiance éditoriale : modérée, interprétation à réexaminer ; appréciation motivée, non probabilité calibrée. Témoin conservé.

## Contrôles exacts

Les 490 régions mathématiques du lot concordent après trois exceptions exactes : with devient vérifiant deux fois, and devient et une fois. Les 3 728 régions du préfixe passent avec quatorze exceptions linguistiques au total. La comparaison brute sans exceptions est fausse ; aucun masque général du contenu mathématique n’est utilisé.

Labels, références, environnements, contrôles TeX et items concordent. Les régions mathématiques du fichier cible entier ne changent pas. Le retour inverse retrouve exactement le lot précédent puis le témoin français publié. Les 166 paires couvrent le préfixe sans lacune ni chevauchement ; les parties antérieures et le suffixe non relu sont inchangés.

Prochaine lecture : Une méta-observation sur les idéaux premiers, anglais L5089 / français L5069. Aucun nouveau PDF, aucune publication ni certification globale du chapitre ou de l’édition ne sont revendiqués.

