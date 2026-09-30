# Algèbre commutative : anneaux locaux, radical de Jacobson et Nakayama

## Résultat et portée

Trois sections entièrement comparées : source L3305–3766 et français L3275–3746. Les 15 paires ci-dessous contiennent tous les énoncés, preuves, notes, diagrammes et transitions, notamment les douze formes de Nakayama et leurs preuves. 179 occurrences sont reliées à des règles contextualisées. La lecture cumulative atteint 20 sections, 131 paires et 847 occurrences ; le chapitre entier et l’édition restent inachevés.

Aucun nouveau changement du français n’est nécessaire dans ce lot. Aucun fichier source de traduction n’est recopié pour fabriquer une version différente. Les anciens états et les propositions de corrections mathématiques restent séparés ; cette lecture de fidélité ne certifie pas la vérité de tous les arguments officiels.

Comparaison assistée par IA, sans relecture humaine. La consultation du canon est rétrospective et n’est pas attribuée au traducteur initial. Les variantes, limites et points délicats restent visibles pour une éventuelle relecture experte, sans attente imposée.

Autorité : commit `a04446e57ec1fbc252a871afcec7752fb2807b14`, SHA-256 `FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3`.
[LaTeX conservé](staged/fr/010_algebra.prose-batch3.fr.tex) · [Lot précédent](ALGEBRA_PROSE_BATCH4_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH5_VALIDATION.json) · [Choix structurés](ALGEBRA_PROSE_BATCH5_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH5_OCCURRENCES.json) · [Couverture](ALGEBRA_PROSE_BATCH5_COVERAGE.json).

## Canon français effectivement consulté

### Antoine Ducros, Introduction à la théorie des schémas, juillet 2021

[Source universitaire](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [PDF conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages indiquées lues en entier. §2.2.1–19, notamment 2.2.9–17 ; §2.3.1–5.2 avec preuves ; surtout 3.3.6 pour les morphismes locaux. Le début de 3.3.2.1 avant p.170 n’est pas déclaré lu ici.

Attestations courtes : « anneau local », « corps résiduel », « morphisme local », « module de type fini », « partie multiplicative ».

Anneau local, inversibilité, corps résiduel et localisé ; morphisme local et contraction ; finitude, générateurs et Nakayama.

Limites : Exemples et espaces annelés ne sont pas ajoutés à Stacks. Les coquilles a1u de 2.3.1, u(m sans parenthèse et les coquilles d’indices ne sont pas importées. Les intersections mal extraites pp.78 et 172 ont été vérifiées sur le rendu. Ces pages ne donnent pas toutes les douze variantes de Stacks.

SHA-256 : `8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66`.

### Olivier Debarre, Algèbre 2, ENS, 2012–2013

[Source universitaire](https://www.math.ens.psl.eu/~debarre/Algebre2.pdf) · [PDF conservé](canon-consulted/fr-fields/debarre-algebre2.pdf)

Pages imprimées 46–47 lues entièrement : II.3.5, définition du radical, II.3.8 et II.3.9 avec toute sa preuve, remarques et exemples II.3.10–11. Le théorème II.4.1 commencé en bas de p.47 n’est pas déclaré intégralement lu.

Attestations courtes : « radical de Jacobson », « Lemme de Nakayama », « corps résiduel », « de type fini ».

Intersection des maximaux, inversibilité de 1+a, annulation et génération modulo un idéal.

Limites : L’hypothèse A non nul du cours n’est pas ajoutée à Stacks. Sa discussion historique ne remplace pas MatCA. Sa preuve par Cayley–Hamilton ne remplace pas la preuve déterminantielle officielle.

SHA-256 : `3FF86D7FD86BA2F1A349ACABE9E4FDDE57282B7A58D66A741CC78BE40E971CC0`.

### Jean-François Dat, Introduction à la théorie des Schémas, Sorbonne Université, M2, 2025–2026

[Source universitaire](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/Schemas/Schemas.pdf) · [PDF conservé](canon-consulted/fr-algebra/dat-schemas.pdf)

Page 10 entière : exemples de platitude, lemme de fidèle platitude et preuve, définition locale et deux corollaires. La définition antérieure et la suite après p.10 ne sont pas déclarées lues dans ce lot.

Attestations courtes : « morphisme local », « fidèlement plat ».

Attestation lexicale de morphisme local et comparaison des précautions sur les surjectivités.

Limites : La formule phi inverse de m égale n est ill-typée pour les idéaux maximaux respectifs de A et B ; elle est vérifiée visuellement et exclue. Ducros 3.3.6 donne la formule bien typée. Aucune platitude n’est ajoutée à Stacks.

SHA-256 : `9298B062AC2BDF64161A107980A30F98E1F2DF6DEB4DA98E1FEB21BA494D26A1`.

## Règles contextualisées

### FR-ALGEBRA-B5-RULE-local

Ducros 2.2.9–17 et 3.3.6 : unique maximal ; morphisme local comme condition supplémentaire.

Canon : FR-ALGEBRA-B5-CANON-DUCROS, FR-ALGEBRA-B5-CANON-DEBARRE.

### FR-ALGEBRA-B5-RULE-residuel

Ducros 2.2.13 et 2.2.17 : quotient et corps des fractions du quotient par un premier. Au-dessus de est contrôlé par la contraction.

Canon : FR-ALGEBRA-B5-CANON-DUCROS, FR-ALGEBRA-B5-CANON-DEBARRE.

### FR-ALGEBRA-B5-RULE-unites

Unité signifie inversible ; distinguer 1, idéal unité, nilradical et intersection des maximaux. Non nul n'est ajouté nulle part.

Canon : FR-ALGEBRA-B5-CANON-DUCROS, FR-ALGEBRA-B5-CANON-DEBARRE.

### FR-ALGEBRA-B5-RULE-diagrammes

Objets, flèches et produits contrôlés dans la source. Pas d'attestation lexicale exacte nouvelle pour carré cartésien ou anneau de la fibre ; justification par la construction.

Canon : Comparaison directe ; attestation externe exacte non acquise.

### FR-ALGEBRA-B5-RULE-finitude

Ducros 2.3 et Debarre II.3 : génération finie, images dans le quotient et annihilation. Contrôler le module concerné ; ne pas ajouter la finitude aux cas nilpotents.

Canon : FR-ALGEBRA-B5-CANON-DUCROS, FR-ALGEBRA-B5-CANON-DEBARRE.

### FR-ALGEBRA-B5-RULE-localisation

Ducros 2.2.14–17 et 2.3.4 : quotient et localisation, égalité dans M puis dans le localisé, anneaux de scalaires successifs.

Canon : FR-ALGEBRA-B5-CANON-DUCROS.

### FR-ALGEBRA-B5-RULE-applications

Conserver portée de chaque implication et surjectivité. Surjectivité des spectres n'est pas celle du morphisme d'anneaux. Ducros 3.3.6 et 2.3.4.

Canon : FR-ALGEBRA-B5-CANON-DUCROS.

### FR-ALGEBRA-B5-RULE-nakayama

Conserver la preuve matricielle et ses douze déductions. La citation historique vient de Stacks, sans prétendue lecture directe de MatCA.

Canon : FR-ALGEBRA-B5-CANON-DEBARRE, FR-ALGEBRA-B5-CANON-DUCROS.

## Passages parallèles complets

### 01 — section-local-rings

Anglais L3305–3310 ; français L3275–3280.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3305) · `FR-ALGEBRA-B5-CHOICE-0001`.

Au cœur de la géométrie algébrique rend bread and butter par une phrase idiomatique de même fonction. Pain quotidien serait plus littéral mais artificiel ici. Aucun résultat n'est ajouté. Anneaux locaux est attesté chez Ducros §2.2.

Règles : FR-ALGEBRA-B5-RULE-local.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Local rings}
\label{section-local-rings}

\noindent
Local rings are the bread and butter of algebraic geometry.
```

Français conservé :
```tex
\section{Anneaux locaux}
\label{section-local-rings}

\noindent
Les anneaux locaux sont au cœur de la géométrie algébrique.
```

</details>

### 02 — definition-local-ring

Anglais L3311–3359 ; français L3281–3331.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3311) · `FR-ALGEBRA-B5-CHOICE-0002`.

Exactement un idéal maximal exclut l'anneau nul, contrairement à au plus un. Corps résiduel est attesté en Ducros 2.2.13 et Debarre II.3 ; quotient, triplet et notations restent explicites. Morphisme local d'anneaux locaux impose une condition supplémentaire, et ne désigne pas tout morphisme entre anneaux locaux. Ducros 3.3.6 confirme cette condition. Tous les paragraphes de localisation et le morphisme entre corps résiduels sont conservés. La désignation proposition de proposition-localize-quotient vient de l'anglais et n'est pas harmonisée avec son environnement.

Point particulier à relire : Proposition est la désignation anglaise de la référence ; pas d'harmonisation silencieuse.

Règles : FR-ALGEBRA-B5-RULE-local, FR-ALGEBRA-B5-RULE-residuel, FR-ALGEBRA-B5-RULE-diagrammes, FR-ALGEBRA-B5-RULE-localisation.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-local-ring}
A {\it local ring} is a ring with exactly one maximal ideal.
If $R$ is a local ring, then the maximal ideal is often denoted
$\mathfrak m_R$ and the field $R/\mathfrak m_R$ is called the
{\it residue field} of the local ring $R$.
We often say ``let $(R, \mathfrak m)$ be a local ring''
or ``let $(R, \mathfrak m, \kappa)$ be a local ring''
to indicate that $R$ is local, $\mathfrak m$ is its unique
maximal ideal and $\kappa = R/\mathfrak m$ is its residue field.
A {\it local homomorphism of local rings} is a ring map
$\varphi : R \to S$ such that $R$ and $S$ are local rings and such
that $\varphi(\mathfrak m_R) \subset \mathfrak m_S$.
If it is given that $R$ and $S$ are local rings, then the phrase
``{\it local ring map $\varphi : R \to S$}'' means that $\varphi$
is a local homomorphism of local rings.
\end{definition}

\noindent
A field is a local ring. Any ring map between fields is a local
homomorphism of local rings.

\medskip\noindent
The localization $R_\mathfrak p$ of a ring $R$ at a prime $\mathfrak p$
is a local ring with maximal ideal $\mathfrak p R_\mathfrak p$. Namely, by
Lemma \ref{lemma-spec-localization} every prime ideal of $R_\mathfrak p$
is contained in the prime ideal $\mathfrak p R_\mathfrak p$
(hence this is a maximal ideal and the only maximal ideal of $R_\mathfrak p$).
The residue field of $R_\mathfrak p$ is denoted $\kappa(\mathfrak p)$;
we call it the {\it residue field of $\mathfrak p$}; by
Proposition \ref{proposition-localize-quotient} we may identify
$\kappa(\mathfrak p)$ with the field of fractions of the domain $R/\mathfrak p$.
Via the composition
$$
\Spec(\kappa(\mathfrak p)) \to \Spec(R_\mathfrak p) \to \Spec(R)
$$
the unique point of the source maps to the point $\mathfrak p$ of the target.

\medskip\noindent
Let $\varphi : R \to S$ be a ring map. Let $\mathfrak q \subset S$ be a prime
and consider the prime $\mathfrak p = \varphi^{-1}(\mathfrak q)$ of $R$.
Since $\varphi(\mathfrak p) \subset \mathfrak q$ the induced ring map
$$
R_\mathfrak p \to S_\mathfrak q,\quad r/g \mapsto \varphi(r)/\varphi(g)
$$
is a local ring map and we obtain an induced map of residue fields
$\kappa(\mathfrak p) \to \kappa(\mathfrak q)$.
```

Français conservé :
```tex
\begin{definition}
\label{definition-local-ring}
Un {\it anneau local} est un anneau qui possède exactement un idéal maximal.
Si $R$ est un anneau local, on note souvent son idéal maximal
$\mathfrak m_R$, et le corps $R/\mathfrak m_R$ est appelé le
{\it corps résiduel} de l'anneau local $R$.
Nous disons souvent « soit $(R, \mathfrak m)$ un anneau local »
ou « soit $(R, \mathfrak m, \kappa)$ un anneau local »
pour indiquer que $R$ est local, que $\mathfrak m$ est son unique
idéal maximal et que $\kappa = R/\mathfrak m$ est son corps résiduel.
Un {\it morphisme local d'anneaux locaux} est un morphisme d'anneaux
$\varphi : R \to S$ tel que $R$ et $S$ soient des anneaux locaux et
que $\varphi(\mathfrak m_R) \subset \mathfrak m_S$.
S'il est entendu que $R$ et $S$ sont des anneaux locaux, l'expression
« {\it morphisme local d'anneaux $\varphi : R \to S$} » signifie que
$\varphi$ est un morphisme local d'anneaux locaux.
\end{definition}

\noindent
Un corps est un anneau local. Tout morphisme d'anneaux entre corps est
un morphisme local d'anneaux locaux.

\medskip\noindent
La localisation $R_\mathfrak p$ d'un anneau $R$ en un idéal premier
$\mathfrak p$ est un anneau local d'idéal maximal
$\mathfrak p R_\mathfrak p$. En effet, d'après le
lemme \ref{lemma-spec-localization}, tout idéal premier de $R_\mathfrak p$
est contenu dans l'idéal premier $\mathfrak p R_\mathfrak p$
(qui est donc un idéal maximal, et l'unique idéal maximal de $R_\mathfrak p$).
Le corps résiduel de $R_\mathfrak p$ est noté $\kappa(\mathfrak p)$ ;
nous l'appelons le {\it corps résiduel de $\mathfrak p$}. D'après la
proposition \ref{proposition-localize-quotient}, nous pouvons identifier
$\kappa(\mathfrak p)$ au corps des fractions de l'anneau intègre
$R/\mathfrak p$. Par la composée
$$
\Spec(\kappa(\mathfrak p)) \to \Spec(R_\mathfrak p) \to \Spec(R)
$$
l'unique point de la source est envoyé sur le point $\mathfrak p$ du but.

\medskip\noindent
Soit $\varphi : R \to S$ un morphisme d'anneaux. Soit
$\mathfrak q \subset S$ un idéal premier, et considérons l'idéal premier
$\mathfrak p = \varphi^{-1}(\mathfrak q)$ de $R$.
Puisque $\varphi(\mathfrak p) \subset \mathfrak q$, le morphisme d'anneaux induit
$$
R_\mathfrak p \to S_\mathfrak q,\quad r/g \mapsto \varphi(r)/\varphi(g)
$$
est un morphisme local d'anneaux locaux, et nous obtenons un morphisme induit
entre les corps résiduels $\kappa(\mathfrak p) \to \kappa(\mathfrak q)$.
```

</details>

### 03 — example-not-local

Anglais L3360–3365 ; français L3332–3337.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3360) · `FR-ALGEBRA-B5-CHOICE-0003`.

Non maximal qualifie l'idéal premier. La négation et la direction du morphisme de localisation restent celles de la source. Aucune restriction n'est ajoutée pour faire disparaître ce contre-exemple.

Règles : FR-ALGEBRA-B5-RULE-local.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-not-local}
If $R$ is a local ring and $\mathfrak p \subset R$ is a non-maximal
prime ideal, then $R \to R_\mathfrak p$ is not a local homomorphism.
\end{example}
```

Français conservé :
```tex
\begin{example}
\label{example-not-local}
Si $R$ est un anneau local et si $\mathfrak p \subset R$ est un idéal premier
non maximal, alors $R \to R_\mathfrak p$ n'est pas un morphisme local.
\end{example}
```

</details>

### 04 — lemma-characterize-local-ring

Anglais L3366–3398 ; français L3338–3370.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3366) · `FR-ALGEBRA-B5-CHOICE-0004`.

Les quatre critères restent distincts : point fermé unique, maximalité, inversibilité hors du maximal, alternative pour x et 1-x. Ou bien les deux préserve le ou inclusif ; anneau non nul reste dans (4). Ducros 2.2.9 atteste le registre. L'existence du maximal, la contradiction par les restes chinois et toutes les implications gardent la preuve anglaise, non celle du canon.

Règles : FR-ALGEBRA-B5-RULE-local, FR-ALGEBRA-B5-RULE-unites, FR-ALGEBRA-B5-RULE-applications, FR-ALGEBRA-B5-RULE-nakayama.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-local-ring}
Let $R$ be a ring. The following are equivalent:
\begin{enumerate}
\item $R$ is a local ring,
\item $\Spec(R)$ has exactly one closed point,
\item $R$ has a maximal ideal $\mathfrak m$
and every element of $R \setminus \mathfrak m$
is a unit, and
\item $R$ is not the zero ring and for every $x \in R$ either $x$
or $1 - x$ is invertible or both.
\end{enumerate}
\end{lemma}

\begin{proof}
Let $R$ be a ring, and $\mathfrak m$ a maximal ideal.
If $x \in R \setminus \mathfrak m$, and $x$ is not a unit
then there is a maximal ideal $\mathfrak m'$ containing $x$.
Hence $R$ has at least two maximal ideals. Conversely,
if $\mathfrak m'$ is another maximal ideal, then choose
$x \in \mathfrak m'$, $x \not \in \mathfrak m$. Clearly
$x$ is not a unit. This proves the equivalence of (1) and (3).
The equivalence (1) and (2) is tautological.
If $R$ is local then (4) holds since $x$ is either in $\mathfrak m$
or not. If (4) holds, and $\mathfrak m$, $\mathfrak m'$ are distinct
maximal ideals then we may choose $x \in R$ such that
$x \bmod \mathfrak m' = 0$ and $x \bmod \mathfrak m = 1$
by the Chinese remainder theorem
(Lemma \ref{lemma-chinese-remainder}).
This element $x$ is not invertible and neither is $1 - x$ which is
a contradiction. Thus (4) and (1) are equivalent.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-characterize-local-ring}
Soit $R$ un anneau. Les conditions suivantes sont équivalentes :
\begin{enumerate}
\item $R$ est un anneau local,
\item $\Spec(R)$ possède exactement un point fermé,
\item $R$ possède un idéal maximal $\mathfrak m$
et tout élément de $R \setminus \mathfrak m$
est une unité, et
\item $R$ n'est pas l'anneau nul et, pour tout $x \in R$, ou bien $x$,
ou bien $1 - x$, ou bien les deux sont inversibles.
\end{enumerate}
\end{lemma}

\begin{proof}
Soient $R$ un anneau et $\mathfrak m$ un idéal maximal.
Si $x \in R \setminus \mathfrak m$ et si $x$ n'est pas une unité,
alors il existe un idéal maximal $\mathfrak m'$ contenant $x$.
Ainsi $R$ possède au moins deux idéaux maximaux. Réciproquement,
si $\mathfrak m'$ est un autre idéal maximal, choisissons
$x \in \mathfrak m'$ tel que $x \not \in \mathfrak m$. Clairement,
$x$ n'est pas une unité. Cela démontre l'équivalence de (1) et de (3).
L'équivalence de (1) et de (2) est tautologique.
Si $R$ est local, alors (4) est vraie, puisque $x$ appartient ou non à
$\mathfrak m$. Si (4) est vraie et si $\mathfrak m$, $\mathfrak m'$
sont des idéaux maximaux distincts, nous pouvons choisir $x \in R$ tel que
$x \bmod \mathfrak m' = 0$ et $x \bmod \mathfrak m = 1$
par le théorème des restes chinois
(lemme \ref{lemma-chinese-remainder}).
Cet élément $x$ n'est pas inversible, et $1 - x$ ne l'est pas davantage,
ce qui est une contradiction. Ainsi (4) et (1) sont équivalentes.
\end{proof}
```

</details>

### 05 — lemma-characterize-local-ring-map

Anglais L3399–3420 ; français L3371–3392.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3399) · `FR-ALGEBRA-B5-CHOICE-0005`.

Les deux anneaux sont supposés locaux avant les équivalences. Image du maximal, image réciproque et reflet de l'inversibilité ne sont pas confondus. L'implication inverse de (4) est automatique pour un morphisme d'anneaux, non ajoutée comme hypothèse. Contraposée exprime la relation exacte avec (2), comme le raisonnement de Ducros 3.3.6. La formule erronée de Dat p.10 n'est pas importée.

Point particulier à relire : Dat p.10 inverse m et n dans l'image réciproque malgré les idéaux maximaux respectifs de A et B. Coquille vérifiée sur l'image et exclue ; Ducros 3.3.6 et l'autorité concordent.

Règles : FR-ALGEBRA-B5-RULE-local, FR-ALGEBRA-B5-RULE-unites, FR-ALGEBRA-B5-RULE-applications.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-local-ring-map}
Let $\varphi : R \to S$ be a ring map. Assume $R$ and $S$ are local rings.
The following are equivalent:
\begin{enumerate}
\item $\varphi$ is a local ring map,
\item $\varphi(\mathfrak m_R) \subset \mathfrak m_S$,
\item $\varphi^{-1}(\mathfrak m_S) = \mathfrak m_R$, and
\item for any $x \in R$, if $\varphi(x)$ is invertible in $S$, then $x$
is invertible in $R$.
\end{enumerate}
\end{lemma}

\begin{proof}
Conditions (1) and (2) are equivalent by definition.
If (3) holds then (2) holds. Conversely, if (2) holds, then
$\varphi^{-1}(\mathfrak m_S)$ is a prime ideal containing
the maximal ideal $\mathfrak m_R$, hence
$\varphi^{-1}(\mathfrak m_S) = \mathfrak m_R$. Finally, (4) is the
contrapositive of (2) by Lemma \ref{lemma-characterize-local-ring}.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-characterize-local-ring-map}
Soit $\varphi : R \to S$ un morphisme d'anneaux. Supposons que $R$ et $S$
soient des anneaux locaux. Les conditions suivantes sont équivalentes :
\begin{enumerate}
\item $\varphi$ est un morphisme local d'anneaux,
\item $\varphi(\mathfrak m_R) \subset \mathfrak m_S$,
\item $\varphi^{-1}(\mathfrak m_S) = \mathfrak m_R$, et
\item pour tout $x \in R$, si $\varphi(x)$ est inversible dans $S$, alors $x$
est inversible dans $R$.
\end{enumerate}
\end{lemma}

\begin{proof}
Les conditions (1) et (2) sont équivalentes par définition.
Si (3) est vraie, alors (2) l'est. Réciproquement, si (2) est vraie,
$\varphi^{-1}(\mathfrak m_S)$ est un idéal premier contenant
l'idéal maximal $\mathfrak m_R$, donc
$\varphi^{-1}(\mathfrak m_S) = \mathfrak m_R$. Enfin, (4) est la
contraposée de (2) d'après le lemme \ref{lemma-characterize-local-ring}.
\end{proof}
```

</details>

### 06 — remark-fundamental-diagram

Anglais L3421–3498 ; français L3393–3473.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3421) · `FR-ALGEBRA-B5-CHOICE-0006`.

Les deux diagrammes entiers, leurs flèches et quotients sont conservés. Colonnes extrêmes et homéomorphismes sur leurs images gardent leur portée. Carrés cartésiens d'espaces topologiques traduit fibre squares pour les localisations et quotients ici écrits, pas pour tous les produits tensoriels. Au-dessus de est explicitement défini par contraction. Anneau non nul ne devient pas corps. Les pages nouvellement lues n'attestent pas mot pour mot carrés cartésiens : le choix est justifié par la construction source.

Point particulier à relire : Justification conceptuelle et source-localisée de carrés cartésiens ; pas d'attestation lexicale indépendante nouvelle revendiquée.

Règles : FR-ALGEBRA-B5-RULE-residuel, FR-ALGEBRA-B5-RULE-unites, FR-ALGEBRA-B5-RULE-diagrammes, FR-ALGEBRA-B5-RULE-applications.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{remark}
\label{remark-fundamental-diagram}
A fundamental commutative diagram associated to a ring map
$\varphi : R \to S$ and a prime $\mathfrak p \subset R$ is the following
$$
\xymatrix{
\kappa(\mathfrak p) \otimes_R S =
S_{\mathfrak p}/{\mathfrak p}S_{\mathfrak p}
&
S_{\mathfrak p} \ar[l]
&
S \ar[r] \ar[l]
&
S/\mathfrak pS \ar[r]
&
(R \setminus \mathfrak p)^{-1}S/\mathfrak pS
\\
\kappa(\mathfrak p) =
R_{\mathfrak p}/{\mathfrak p}R_{\mathfrak p} \ar[u]
&
R_{\mathfrak p} \ar[u] \ar[l]
&
R \ar[u] \ar[r] \ar[l]
&
R/\mathfrak p \ar[u] \ar[r]
&
\kappa(\mathfrak p) \ar[u]
}
$$
In this diagram the outer left and outer right columns are identical.
On spectra the horizontal maps induce homeomorphisms
onto their images and the squares induce fibre squares of topological spaces
(see Lemmas \ref{lemma-spec-localization} and \ref{lemma-spec-closed}).
This shows that $\mathfrak p$ is in the image of the map on Spec if and
only if $S \otimes_R \kappa(\mathfrak p)$ is not the zero ring.
If there does exist a prime $\mathfrak q \subset S$ lying over
$\mathfrak p$, i.e., with $\mathfrak p = \varphi^{-1}(\mathfrak q)$
then we can extend the diagram to the following diagram
$$
\xymatrix{
\kappa(\mathfrak q) = S_{\mathfrak q}/{\mathfrak q}S_{\mathfrak q}
&
S_{\mathfrak q} \ar[l]
&
S \ar[r] \ar[l]
&
S/\mathfrak q \ar[r]
&
\kappa(\mathfrak q)
\\
\kappa(\mathfrak p) \otimes_R S =
S_{\mathfrak p}/{\mathfrak p}S_{\mathfrak p} \ar[u]
&
S_{\mathfrak p} \ar[u] \ar[l]
&
S \ar[u] \ar[r] \ar[l]
&
S/\mathfrak pS \ar[u] \ar[r]
&
(R \setminus \mathfrak p)^{-1}S/\mathfrak pS \ar[u]
\\
\kappa(\mathfrak p) =
R_{\mathfrak p}/{\mathfrak p}R_{\mathfrak p} \ar[u]
&
R_{\mathfrak p} \ar[u] \ar[l]
&
R \ar[u] \ar[r] \ar[l]
&
R/\mathfrak p \ar[u] \ar[r]
&
\kappa(\mathfrak p) \ar[u]
}
$$
In this diagram it is still the case that the outer left and outer right
columns are identical and that on spectra the horizontal maps induce
homeomorphisms onto their image.
\end{remark}
```

Français conservé :
```tex
\begin{remark}
\label{remark-fundamental-diagram}
Un diagramme commutatif fondamental associé à un morphisme d'anneaux
$\varphi : R \to S$ et à un idéal premier $\mathfrak p \subset R$ est le suivant :
$$
\xymatrix{
\kappa(\mathfrak p) \otimes_R S =
S_{\mathfrak p}/{\mathfrak p}S_{\mathfrak p}
&
S_{\mathfrak p} \ar[l]
&
S \ar[r] \ar[l]
&
S/\mathfrak pS \ar[r]
&
(R \setminus \mathfrak p)^{-1}S/\mathfrak pS
\\
\kappa(\mathfrak p) =
R_{\mathfrak p}/{\mathfrak p}R_{\mathfrak p} \ar[u]
&
R_{\mathfrak p} \ar[u] \ar[l]
&
R \ar[u] \ar[r] \ar[l]
&
R/\mathfrak p \ar[u] \ar[r]
&
\kappa(\mathfrak p) \ar[u]
}
$$
Dans ce diagramme, les colonnes extrêmes gauche et droite sont identiques.
Sur les spectres, les morphismes horizontaux induisent des homéomorphismes
sur leurs images, et les carrés induisent des carrés cartésiens d'espaces
topologiques (voir les lemmes \ref{lemma-spec-localization}
et \ref{lemma-spec-closed}).
Cela montre que $\mathfrak p$ appartient à l'image de l'application
entre spectres si et seulement si
$S \otimes_R \kappa(\mathfrak p)$ n'est pas l'anneau nul.
S'il existe un idéal premier $\mathfrak q \subset S$ au-dessus de
$\mathfrak p$, c'est-à-dire tel que
$\mathfrak p = \varphi^{-1}(\mathfrak q)$,
alors nous pouvons compléter le diagramme en le diagramme suivant :
$$
\xymatrix{
\kappa(\mathfrak q) = S_{\mathfrak q}/{\mathfrak q}S_{\mathfrak q}
&
S_{\mathfrak q} \ar[l]
&
S \ar[r] \ar[l]
&
S/\mathfrak q \ar[r]
&
\kappa(\mathfrak q)
\\
\kappa(\mathfrak p) \otimes_R S =
S_{\mathfrak p}/{\mathfrak p}S_{\mathfrak p} \ar[u]
&
S_{\mathfrak p} \ar[u] \ar[l]
&
S \ar[u] \ar[r] \ar[l]
&
S/\mathfrak pS \ar[u] \ar[r]
&
(R \setminus \mathfrak p)^{-1}S/\mathfrak pS \ar[u]
\\
\kappa(\mathfrak p) =
R_{\mathfrak p}/{\mathfrak p}R_{\mathfrak p} \ar[u]
&
R_{\mathfrak p} \ar[u] \ar[l]
&
R \ar[u] \ar[r] \ar[l]
&
R/\mathfrak p \ar[u] \ar[r]
&
\kappa(\mathfrak p) \ar[u]
}
$$
Dans ce diagramme encore, les colonnes extrêmes gauche et droite sont
identiques et, sur les spectres, les morphismes horizontaux induisent
des homéomorphismes sur leurs images.
\end{remark}
```

</details>

### 07 — lemma-in-image

Anglais L3499–3518 ; français L3474–3493.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3499) · `FR-ALGEBRA-B5-CHOICE-0007`.

Les cinq conditions gardent ordre, premier, localisations et contraction finale. Appartenir à l'image n'est pas une surjectivité globale. Le renvoi et la preuve par reformulation sont conservés, sans ajouter platitude ni finitude. La propriété des morphismes plats chez Dat ne renforce pas ce lemme.

Règles : FR-ALGEBRA-B5-RULE-applications.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-in-image}
Let $\varphi : R \to S$ be a ring map. Let $\mathfrak p$
be a prime of $R$. The following are equivalent
\begin{enumerate}
\item $\mathfrak p$ is in the image of
$\Spec(S) \to \Spec(R)$,
\item $S \otimes_R \kappa(\mathfrak p) \not = 0$,
\item $S_{\mathfrak p}/\mathfrak p S_{\mathfrak p} \not = 0$,
\item $(S/\mathfrak pS)_{\mathfrak p} \not = 0$, and
\item $\mathfrak p = \varphi^{-1}(\mathfrak pS)$.
\end{enumerate}
\end{lemma}

\begin{proof}
We have already seen the equivalence of the first two
in Remark \ref{remark-fundamental-diagram}. The others
are just reformulations of this.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-in-image}
Soit $\varphi : R \to S$ un morphisme d'anneaux. Soit $\mathfrak p$
un idéal premier de $R$. Les conditions suivantes sont équivalentes :
\begin{enumerate}
\item $\mathfrak p$ appartient à l'image de
$\Spec(S) \to \Spec(R)$,
\item $S \otimes_R \kappa(\mathfrak p) \not = 0$,
\item $S_{\mathfrak p}/\mathfrak p S_{\mathfrak p} \not = 0$,
\item $(S/\mathfrak pS)_{\mathfrak p} \not = 0$, et
\item $\mathfrak p = \varphi^{-1}(\mathfrak pS)$.
\end{enumerate}
\end{lemma}

\begin{proof}
Nous avons déjà vu l'équivalence des deux premières conditions
dans la remarque \ref{remark-fundamental-diagram}. Les autres
n'en sont que des reformulations.
\end{proof}
```

</details>

### 08 — remark-local-ring-fibre

Anglais L3519–3545 ; français L3494–3514.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3519) · `FR-ALGEBRA-B5-CHOICE-0008`.

Anneau de la fibre traduit descriptivement fibre ring, dont l'objet est défini par le produit tensoriel exact, non une fibre de module. Au-dessus de garde le sens de contraction. S'identifie à rend l'isomorphisme canonique des morphismes issu de la localisation, pas une égalité préalable des objets. Les deux isomorphismes et leurs anneaux de base restent exacts. Les pages consultées attestent localisé et corps résiduel, mais pas mot pour mot anneau de la fibre.

Point particulier à relire : Même limite pour anneau de la fibre ; la formule exacte permet de vérifier le sens.

Règles : FR-ALGEBRA-B5-RULE-residuel, FR-ALGEBRA-B5-RULE-diagrammes, FR-ALGEBRA-B5-RULE-localisation, FR-ALGEBRA-B5-RULE-applications.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{remark}
\label{remark-local-ring-fibre}
Let $R \to S$ be a ring map. Let $\mathfrak q$ be a prime
ideal of $S$ lying over the prime ideal $\mathfrak p$ of $R$.
According to Remark \ref{remark-fundamental-diagram}
the prime $\mathfrak q$ corresponds to a unique prime
$\overline{\mathfrak q}$ of the fibre ring
$F = S \otimes_R \kappa(\mathfrak p)$.
Then we have
$$
F_{\overline{\mathfrak q}}
\cong S_\mathfrak q \otimes_{R_\mathfrak p} \kappa(\mathfrak p)
\cong S_\mathfrak q/\mathfrak p S_\mathfrak q
$$
Namely, there is an obvious ring map
$F \to S_\mathfrak q \otimes_{R_\mathfrak p} \kappa(\mathfrak p)$
which is easily seen to be isomorphic to $F \to F_{\overline{\mathfrak q}}$.
The second isomorphism follows from the fact that $\kappa(\mathfrak p)$
is the quotient of $R_\mathfrak p$ by $\mathfrak pR_\mathfrak p$.
\end{remark}
```

Français conservé :
```tex
\begin{remark}
\label{remark-local-ring-fibre}
Soit $R \to S$ un morphisme d'anneaux. Soit $\mathfrak q$ un idéal premier
de $S$ au-dessus de l'idéal premier $\mathfrak p$ de $R$.
D'après la remarque \ref{remark-fundamental-diagram},
l'idéal premier $\mathfrak q$ correspond à un unique idéal premier
$\overline{\mathfrak q}$ de l'anneau de la fibre
$F = S \otimes_R \kappa(\mathfrak p)$.
Alors nous avons
$$
F_{\overline{\mathfrak q}}
\cong S_\mathfrak q \otimes_{R_\mathfrak p} \kappa(\mathfrak p)
\cong S_\mathfrak q/\mathfrak p S_\mathfrak q
$$
En effet, il existe un morphisme d'anneaux évident
$F \to S_\mathfrak q \otimes_{R_\mathfrak p} \kappa(\mathfrak p)$
qui s'identifie aisément à $F \to F_{\overline{\mathfrak q}}$.
Le second isomorphisme résulte du fait que $\kappa(\mathfrak p)$
est le quotient de $R_\mathfrak p$ par $\mathfrak pR_\mathfrak p$.
\end{remark}
```

</details>

### 09 — section-radical

Anglais L3546–3553 ; français L3515–3522.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3546) · `FR-ALGEBRA-B5-CHOICE-0009`.

Radical de Jacobson est attesté avec la même intersection des maximaux chez Debarre II.3 p.46. Il ne devient pas le nilradical, intersection des premiers. L'identification au maximal reste conditionnée par la localité.

Règles : FR-ALGEBRA-B5-RULE-local, FR-ALGEBRA-B5-RULE-unites.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{The Jacobson radical of a ring}
\label{section-radical}

\noindent
We recall that the {\it Jacobson radical} $\text{rad}(R)$ of a ring $R$
is the intersection of all maximal ideals of $R$. If $R$ is local
then $\text{rad}(R)$ is the maximal ideal of $R$.
```

Français conservé :
```tex
\section{Le radical de Jacobson d'un anneau}
\label{section-radical}

\noindent
Rappelons que le {\it radical de Jacobson} $\text{rad}(R)$ d'un anneau $R$
est l'intersection de tous les idéaux maximaux de $R$. Si $R$ est local,
alors $\text{rad}(R)$ est l'idéal maximal de $R$.
```

</details>

### 10 — lemma-contained-in-radical

Anglais L3554–3585 ; français L3523–3556.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3554) · `FR-ALGEBRA-B5-CHOICE-0010`.

Unité signifie élément inversible, non élément 1. La condition porte sur tous les éléments de 1+I. Les trois parties de preuve sont conservées : exclusion des maximaux, contradiction avec I+m=R, relèvement d'un inverse modulo I. Debarre II.3.8 atteste le mécanisme, mais sa formulation et son hypothèse d'anneau non nul ne remplacent pas celles de Stacks.

Règles : FR-ALGEBRA-B5-RULE-local, FR-ALGEBRA-B5-RULE-unites, FR-ALGEBRA-B5-RULE-applications.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-contained-in-radical}
Let $R$ be a ring with Jacobson radical $\text{rad}(R)$.
Let $I \subset R$ be an ideal. The following are
equivalent
\begin{enumerate}
\item $I \subset \text{rad}(R)$, and
\item every element of $1 + I$ is a unit in $R$.
\end{enumerate}
In this case every element of $R$ which maps to a unit of $R/I$ is a unit.
\end{lemma}

\begin{proof}
If $f \in \text{rad}(R)$, then $f \in \mathfrak m$ for all
maximal ideals $\mathfrak m$ of $R$. Hence $1 + f \not \in \mathfrak m$
for all maximal ideals $\mathfrak m$ of $R$. Thus the closed
subset $V(1 + f)$ of $\Spec(R)$ is empty. This implies
that $1 + f$ is a unit, see Lemma \ref{lemma-Zariski-topology}.

\medskip\noindent
Conversely, assume that $1 + f$ is a unit for all $f \in I$.
If $\mathfrak m$ is a maximal ideal and $I \not \subset \mathfrak m$,
then $I + \mathfrak m = R$. Hence $1 = f + g$ for some $g \in \mathfrak m$
and $f \in I$. Then $g = 1 + (-f)$ is not a unit, contradiction.

\medskip\noindent
For the final statement let $f \in R$ map to a unit in $R/I$.
Then we can find $g \in R$ mapping to the multiplicative inverse
of $f \bmod I$. Then $fg = 1 \bmod I$. Hence $fg$ is a unit of $R$
by (2) which implies that $f$ is a unit.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-contained-in-radical}
Soit $R$ un anneau de radical de Jacobson $\text{rad}(R)$.
Soit $I \subset R$ un idéal. Les conditions suivantes sont
équivalentes :
\begin{enumerate}
\item $I \subset \text{rad}(R)$, et
\item tout élément de $1 + I$ est une unité de $R$.
\end{enumerate}
Dans ce cas, tout élément de $R$ dont l'image est une unité de $R/I$
est une unité.
\end{lemma}

\begin{proof}
Si $f \in \text{rad}(R)$, alors $f \in \mathfrak m$ pour tout
idéal maximal $\mathfrak m$ de $R$. Ainsi $1 + f \not \in \mathfrak m$
pour tout idéal maximal $\mathfrak m$ de $R$. Le fermé
$V(1 + f)$ de $\Spec(R)$ est donc vide. Cela entraîne
que $1 + f$ est une unité ; voir le lemme \ref{lemma-Zariski-topology}.

\medskip\noindent
Réciproquement, supposons que $1 + f$ soit une unité pour tout $f \in I$.
Si $\mathfrak m$ est un idéal maximal et si $I \not \subset \mathfrak m$,
alors $I + \mathfrak m = R$. Par conséquent,
$1 = f + g$ pour un certain $g \in \mathfrak m$ et un certain
$f \in I$. Mais $g = 1 + (-f)$ n'est pas une unité, contradiction.

\medskip\noindent
Pour la dernière assertion, soit $f \in R$ dont l'image est une unité de $R/I$.
Nous pouvons trouver $g \in R$ dont l'image est l'inverse multiplicatif
de $f \bmod I$. Alors $fg = 1 \bmod I$. Ainsi $fg$ est une unité de $R$
d'après (2), ce qui entraîne que $f$ est une unité.
\end{proof}
```

</details>

### 11 — lemma-surjective-on-spec-units

Anglais L3586–3605 ; français L3557–3585.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3586) · `FR-ALGEBRA-B5-CHOICE-0011`.

La surjectivité porte sur les spectres, non sur le morphisme d'anneaux. Aucune platitude ni injectivité n'est ajoutée. La preuve utilise tous les premiers et le point (17) exact. Unité et inversible sont ici synonymes.

Règles : FR-ALGEBRA-B5-RULE-unites, FR-ALGEBRA-B5-RULE-applications.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-surjective-on-spec-units}
Let $\varphi : R \to S$ be a ring map such that the induced map
$\Spec(S) \to \Spec(R)$ is surjective. Then an element $x \in R$
is a unit if and only if $\varphi(x) \in S$ is a unit.
\end{lemma}

\begin{proof}
If $x$ is a unit, then so is $\varphi(x)$. Conversely, if $\varphi(x)$
is a unit, then $\varphi(x) \not \in \mathfrak q$ for all
$\mathfrak q \in \Spec(S)$. Hence
$x \not \in \varphi^{-1}(\mathfrak q) = \Spec(\varphi)(\mathfrak q)$
for all $\mathfrak q \in \Spec(S)$. Since $\Spec(\varphi)$ is surjective
we conclude that $x$ is a unit by
part (17) of Lemma \ref{lemma-Zariski-topology}.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-surjective-on-spec-units}
Soit $\varphi : R \to S$ un morphisme d'anneaux tel que l'application induite
$\Spec(S) \to \Spec(R)$ soit surjective. Alors un élément $x \in R$
est une unité si et seulement si $\varphi(x) \in S$ est une unité.
\end{lemma}

\begin{proof}
Si $x$ est une unité, alors $\varphi(x)$ l'est aussi. Réciproquement, si
$\varphi(x)$ est une unité, alors
$\varphi(x) \not \in \mathfrak q$ pour tout
$\mathfrak q \in \Spec(S)$. Par conséquent,
$x \not \in \varphi^{-1}(\mathfrak q) = \Spec(\varphi)(\mathfrak q)$
pour tout $\mathfrak q \in \Spec(S)$. Puisque $\Spec(\varphi)$ est surjective,
nous concluons que $x$ est une unité d'après
la partie (17) du lemme \ref{lemma-Zariski-topology}.
\end{proof}
```

</details>

### 12 — section-nakayama

Anglais L3606–3614 ; français L3586–3594.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3606) · `FR-ALGEBRA-B5-CHOICE-0012`.

La citation historique est traduite depuis sa présence dans Stacks, sans prétendre avoir consulté Matsumura. Simple mais important, priorité obscure et le professeur défunt qui n'aimait pas ce nom restent attribués. La note historique de Debarre ne remplace pas cette citation.

Point particulier à relire : Matsumura n'a pas été consulté directement : seule sa citation dans Stacks est comparée.

Règles : FR-ALGEBRA-B5-RULE-nakayama.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Nakayama's lemma}
\label{section-nakayama}

\noindent
We quote from \cite{MatCA}: ``This simple but
important lemma is due to T.~Nakayama, G.~Azumaya and W.~Krull. Priority
is obscure, and although it is usually called the Lemma of Nakayama, late
Prof.~Nakayama did not like the name.''
```

Français conservé :
```tex
\section{Le lemme de Nakayama}
\label{section-nakayama}

\noindent
Nous citons \cite{MatCA} : « Ce lemme simple mais
important est dû à T.~Nakayama, G.~Azumaya et W.~Krull. La question de la priorité
est obscure et, bien qu'il soit habituellement appelé lemme de Nakayama, feu
le professeur Nakayama n'aimait pas ce nom. »
```

</details>

### 13 — lemma-NAK

Anglais L3615–3697 ; français L3595–3677.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3615) · `FR-ALGEBRA-B5-CHOICE-0013`.

Les douze variantes sont comparées une à une. De type fini rend finite, non cardinal fini. Dans (3) et (4), N' est de type fini, non M ; dans (9) à (12), aucune finitude n'est ajoutée et nilpotent ne devient pas nil. Engendrent le quotient garde les images implicites de la famille. Les renvois, la preuve déterminantielle et les déductions par quotient et image restent intacts. Annule M signifie multiplication nulle, non inversibilité. La citation MatCA garde 1.M, (NAK), page 11 et sa clé ; seuls Lemma/Lemme et une virgule diffèrent. La citation répétée dans history reste répétée. Ducros 2.3.2–4 et Debarre II.3.5–9 attestent le registre, sans remplacer les douze formes ni leur preuve.

Point particulier à relire : Les douze formes ne sont pas réduites à la forme locale usuelle. Nilpotence et finitude gardent leurs portées distinctes.

Règles : FR-ALGEBRA-B5-RULE-unites, FR-ALGEBRA-B5-RULE-finitude, FR-ALGEBRA-B5-RULE-localisation, FR-ALGEBRA-B5-RULE-applications, FR-ALGEBRA-B5-RULE-nakayama.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}[Nakayama's lemma]
\label{lemma-NAK}
\begin{reference}
\cite[1.M Lemma (NAK) page 11]{MatCA}
\end{reference}
\begin{history}
We quote from \cite{MatCA}: ``This simple but
important lemma is due to T.~Nakayama, G.~Azumaya and W.~Krull. Priority
is obscure, and although it is usually called the Lemma of Nakayama, late
Prof.~Nakayama did not like the name.''
\end{history}
Let $R$ be a ring with Jacobson radical $\text{rad}(R)$.
Let $M$ be an $R$-module. Let $I \subset R$
be an ideal.
\begin{enumerate}
\item
\label{item-nakayama}
If $IM = M$ and $M$ is finite, then there exists an $f \in 1 + I$ such that
$fM = 0$.
\item If $IM = M$, $M$ is finite, and $I \subset \text{rad}(R)$, then $M = 0$.
\item If $N, N' \subset M$, $M = N + IN'$, and $N'$ is finite,
then there exists an $f \in 1 + I$ such that $fM \subset N$ and $M_f = N_f$.
\item If $N, N' \subset M$, $M = N + IN'$, $N'$ is finite, and
$I \subset \text{rad}(R)$, then $M = N$.
\item If $N \to M$ is a module map, $N/IN \to M/IM$ is
surjective, and $M$ is finite, then there exists an $f \in 1 + I$
such that $N_f \to M_f$ is surjective.
\item If $N \to M$ is a module map, $N/IN \to M/IM$ is
surjective, $M$ is finite, and $I \subset \text{rad}(R)$,
then $N \to M$ is surjective.
\item If $x_1, \ldots, x_n \in M$ generate $M/IM$ and $M$ is finite,
then there exists an $f \in 1 + I$ such that $x_1, \ldots, x_n$
generate $M_f$ over $R_f$.
\item If $x_1, \ldots, x_n \in M$ generate $M/IM$, $M$ is finite, and
$I \subset \text{rad}(R)$, then $M$ is generated by $x_1, \ldots, x_n$.
\item If $IM = M$, $I$ is nilpotent, then $M = 0$.
\item If $N, N' \subset M$, $M = N + IN'$, and $I$ is nilpotent then $M = N$.
\item If $N \to M$ is a module map, $I$ is nilpotent, and $N/IN \to M/IM$
is surjective, then $N \to M$ is surjective.
\item If $\{x_\alpha\}_{\alpha \in A}$ is a set of elements of $M$
which generate $M/IM$ and $I$ is nilpotent, then $M$ is generated
by the $x_\alpha$.
\end{enumerate}
\end{lemma}

\begin{proof}
Proof of (\ref{item-nakayama}). Choose generators $y_1, \ldots, y_m$ of $M$
over $R$. For each $i$ we can write $y_i = \sum z_{ij} y_j$ with
$z_{ij} \in I$ (since $M = IM$).
In other words $\sum_j (\delta_{ij} - z_{ij})y_j = 0$.
Let $f$ be the determinant of the $m \times m$ matrix
$A = (\delta_{ij} - z_{ij})$. Note that $f \in 1 + I$
(since the matrix $A$ is entrywise congruent to the
$m \times m$ identity matrix modulo $I$).
By Lemma \ref{lemma-matrix-left-inverse} (1),
there exists an $m \times m$
matrix $B$ such that $BA = f 1_{m \times m}$. Writing out we see that
$\sum_{i} b_{hi} a_{ij} = f \delta_{hj}$ for all
$h$ and $j$; hence, $\sum_{i, j} b_{hi} a_{ij} y_j
= \sum_{j} f \delta_{hj} y_j = f y_h$ for every $h$.
In other words, $0 = f y_h$ for every $h$ (since each
$i$ satisfies $\sum_j a_{ij} y_j = 0$).
This implies that $f$ annihilates $M$.

\medskip\noindent
By Lemma \ref{lemma-contained-in-radical} an element of $1 + \text{rad}(R)$ is
invertible element of $R$. Hence we see that (\ref{item-nakayama}) implies
(2). We obtain (3) by applying (1) to $M/N$ which is finite as $N'$ is finite.
We obtain (4) by applying (2) to $M/N$ which is finite as $N'$ is finite.
We obtain (5) by applying (3) to $M$ and the submodules $\Im(N \to M)$
and $M$. We obtain (6) by applying (4) to $M$ and the submodules
$\Im(N \to M)$ and $M$.
We obtain (7) by applying (5) to the map $R^{\oplus n} \to M$,
$(a_1, \ldots, a_n) \mapsto a_1x_1 + \ldots + a_nx_n$.
We obtain (8) by applying (6) to the map $R^{\oplus n} \to M$,
$(a_1, \ldots, a_n) \mapsto a_1x_1 + \ldots + a_nx_n$.

\medskip\noindent
Part (9) holds because if $M = IM$ then $M = I^nM$ for all $n \geq 0$
and $I$ being nilpotent means $I^n = 0$ for some $n \gg 0$. Parts
(10), (11), and (12) follow from (9) by the arguments used above.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}[Lemme de Nakayama]
\label{lemma-NAK}
\begin{reference}
\cite[1.M Lemme (NAK), page 11]{MatCA}
\end{reference}
\begin{history}
Nous citons \cite{MatCA} : « Ce lemme simple mais
important est dû à T.~Nakayama, G.~Azumaya et W.~Krull. La question de la priorité
est obscure et, bien qu'il soit habituellement appelé lemme de Nakayama, feu
le professeur Nakayama n'aimait pas ce nom. »
\end{history}
Soit $R$ un anneau de radical de Jacobson $\text{rad}(R)$.
Soit $M$ un $R$-module. Soit $I \subset R$
un idéal.
\begin{enumerate}
\item
\label{item-nakayama}
Si $IM = M$ et si $M$ est de type fini, alors il existe $f \in 1 + I$ tel que
$fM = 0$.
\item Si $IM = M$, si $M$ est de type fini et si $I \subset \text{rad}(R)$, alors $M = 0$.
\item Si $N, N' \subset M$, si $M = N + IN'$ et si $N'$ est de type fini,
alors il existe $f \in 1 + I$ tel que $fM \subset N$ et $M_f = N_f$.
\item Si $N, N' \subset M$, si $M = N + IN'$, si $N'$ est de type fini et si
$I \subset \text{rad}(R)$, alors $M = N$.
\item Si $N \to M$ est un morphisme de modules, si $N/IN \to M/IM$ est
surjectif et si $M$ est de type fini, alors il existe $f \in 1 + I$
tel que $N_f \to M_f$ soit surjectif.
\item Si $N \to M$ est un morphisme de modules, si $N/IN \to M/IM$ est
surjectif, si $M$ est de type fini et si $I \subset \text{rad}(R)$,
alors $N \to M$ est surjectif.
\item Si $x_1, \ldots, x_n \in M$ engendrent $M/IM$ et si $M$ est de type fini,
alors il existe $f \in 1 + I$ tel que $x_1, \ldots, x_n$
engendrent $M_f$ comme $R_f$-module.
\item Si $x_1, \ldots, x_n \in M$ engendrent $M/IM$, si $M$ est de type fini et si
$I \subset \text{rad}(R)$, alors $M$ est engendré par $x_1, \ldots, x_n$.
\item Si $IM = M$ et si $I$ est nilpotent, alors $M = 0$.
\item Si $N, N' \subset M$, si $M = N + IN'$ et si $I$ est nilpotent, alors $M = N$.
\item Si $N \to M$ est un morphisme de modules, si $I$ est nilpotent et si $N/IN \to M/IM$
est surjectif, alors $N \to M$ est surjectif.
\item Si $\{x_\alpha\}_{\alpha \in A}$ est un ensemble d'éléments de $M$
qui engendrent $M/IM$ et si $I$ est nilpotent, alors $M$ est engendré
par les $x_\alpha$.
\end{enumerate}
\end{lemma}

\begin{proof}
Démonstration de (\ref{item-nakayama}). Choisissons des générateurs $y_1, \ldots, y_m$ de $M$
comme $R$-module. Pour chaque $i$, nous pouvons écrire $y_i = \sum z_{ij} y_j$ avec
$z_{ij} \in I$ (puisque $M = IM$).
Autrement dit, $\sum_j (\delta_{ij} - z_{ij})y_j = 0$.
Soit $f$ le déterminant de la matrice $m \times m$
$A = (\delta_{ij} - z_{ij})$. Notons que $f \in 1 + I$
(puisque la matrice $A$ est congrue terme à terme à la
matrice identité $m \times m$ modulo $I$).
D'après le lemme \ref{lemma-matrix-left-inverse} (1),
il existe une matrice $m \times m$
$B$ telle que $BA = f 1_{m \times m}$. En développant, nous voyons que
$\sum_{i} b_{hi} a_{ij} = f \delta_{hj}$ pour tous
$h$ et $j$ ; ainsi, $\sum_{i, j} b_{hi} a_{ij} y_j
= \sum_{j} f \delta_{hj} y_j = f y_h$ pour tout $h$.
Autrement dit, $0 = f y_h$ pour tout $h$ (puisque chaque
$i$ vérifie $\sum_j a_{ij} y_j = 0$).
Cela entraîne que $f$ annule $M$.

\medskip\noindent
D'après le lemme \ref{lemma-contained-in-radical}, tout élément de $1 + \text{rad}(R)$ est
un élément inversible de $R$. Nous voyons donc que (\ref{item-nakayama}) entraîne
(2). Nous obtenons (3) en appliquant (1) à $M/N$, qui est de type fini puisque $N'$ l'est.
Nous obtenons (4) en appliquant (2) à $M/N$, qui est de type fini puisque $N'$ l'est.
Nous obtenons (5) en appliquant (3) à $M$ et aux sous-modules $\Im(N \to M)$
et $M$. Nous obtenons (6) en appliquant (4) à $M$ et aux sous-modules
$\Im(N \to M)$ et $M$.
Nous obtenons (7) en appliquant (5) au morphisme $R^{\oplus n} \to M$,
$(a_1, \ldots, a_n) \mapsto a_1x_1 + \ldots + a_nx_n$.
Nous obtenons (8) en appliquant (6) au morphisme $R^{\oplus n} \to M$,
$(a_1, \ldots, a_n) \mapsto a_1x_1 + \ldots + a_nx_n$.

\medskip\noindent
L'assertion (9) est vraie car, si $M = IM$, alors $M = I^nM$ pour tout $n \geq 0$,
et la nilpotence de $I$ signifie que $I^n = 0$ pour un certain $n \gg 0$. Les assertions
(10), (11) et (12) résultent de (9) par les arguments utilisés ci-dessus.
\end{proof}
```

</details>

### 14 — lemma-NAK-localization

Anglais L3698–3734 ; français L3678–3714.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3698) · `FR-ALGEBRA-B5-CHOICE-0014`.

Partie multiplicative, de type fini et engendrer sont attestés chez Ducros 2.2.14–17 et 2.3.4. Les deux cas particuliers en note sont complets, notamment le corps résiduel et f hors du premier. Le premier argument distingue égalité dans le localisé puis dans M après multiplication par t_i. Le produit fini donne un seul élément de localisation. Dans le cas général, R_s puis (R_s)_g sont explicitement les anneaux de base. Les formules de g et f restent exactes ; les détails omis et la précision implicite sur s' ne sont pas ajoutés au texte.

Point particulier à relire : Les précisions implicites sur g=1+i/s' ne sont pas ajoutées. La source marque les détails omis.

Règles : FR-ALGEBRA-B5-RULE-finitude, FR-ALGEBRA-B5-RULE-localisation.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-NAK-localization}
Let $R$ be a ring, let $S \subset R$ be a multiplicative subset,
let $I \subset R$ be an ideal, and let $M$ be a finite $R$-module.
If $x_1, \ldots, x_r \in M$ generate $S^{-1}(M/IM)$
as an $S^{-1}(R/I)$-module, then there exists an $f \in S + I$
such that $x_1, \ldots, x_r$ generate $M_f$ as an
$R_f$-module.\footnote{Special cases: (I) $I = 0$. The lemma says
if $x_1, \ldots, x_r$ generate $S^{-1}M$, then $x_1, \ldots, x_r$
generate $M_f$ for some $f \in S$. (II) $I = \mathfrak p$ is
a prime ideal and $S = R \setminus \mathfrak p$. The lemma says if
$x_1, \ldots, x_r$ generate $M \otimes_R \kappa(\mathfrak p)$
then $x_1, \ldots, x_r$ generate $M_f$ for some
$f \in R$, $f \not \in \mathfrak p$.}
\end{lemma}

\begin{proof}
Special case $I = 0$. Let $y_1, \ldots, y_s$ be generators for $M$ over $R$.
Since $S^{-1}M$ is generated by $x_1, \ldots, x_r$, for each $i$
we can write $y_i = \sum (a_{ij}/s_{ij})x_j$ in $S^{-1}M$
for some $a_{ij} \in R$ and $s_{ij} \in S$. Multiplying by the product
$s \in S$ of the $s_{ij}$ we see that $sy_i = \sum a'_{ij}x_j$
in $S^{-1}M$ for some $a'_{ij} \in R$.
This in turn means there exist $t_i \in S$ such that
$t_isy_i = \sum t_ia'_{ij}x_j$ in $M$. Thus if $t \in S$
is the product of the $t_i$, then we
see that $y_i$ is in the $R_{st}$-submodule generated by $x_1, \ldots, x_r$
of $M_{st}$. Hence $x_1, \ldots, x_r$ generates $M_{st}$.

\medskip\noindent
General case. By the special case, we can find an $s \in S$
such that $x_1, \ldots, x_r$ generate $(M/IM)_s$ over $(R/I)_s$.
By Lemma \ref{lemma-NAK} we can find a $g \in 1 + I_s \subset R_s$
such that $x_1, \ldots, x_r$ generate $(M_s)_g$ over $(R_s)_g$.
Write $g = 1 + i/s'$. Then $f = ss' + is$ works; details omitted.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-NAK-localization}
Soit $R$ un anneau, soit $S \subset R$ une partie multiplicative,
soit $I \subset R$ un idéal et soit $M$ un $R$-module de type fini.
Si $x_1, \ldots, x_r \in M$ engendrent $S^{-1}(M/IM)$
comme $S^{-1}(R/I)$-module, alors il existe $f \in S + I$
tel que $x_1, \ldots, x_r$ engendrent $M_f$ comme
$R_f$-module.\footnote{Cas particuliers : (I) $I = 0$. Le lemme affirme que,
si $x_1, \ldots, x_r$ engendrent $S^{-1}M$, alors $x_1, \ldots, x_r$
engendrent $M_f$ pour un certain $f \in S$. (II) $I = \mathfrak p$ est
un idéal premier et $S = R \setminus \mathfrak p$. Le lemme affirme que, si
$x_1, \ldots, x_r$ engendrent $M \otimes_R \kappa(\mathfrak p)$,
alors $x_1, \ldots, x_r$ engendrent $M_f$ pour un certain
$f \in R$, $f \not \in \mathfrak p$.}
\end{lemma}

\begin{proof}
Cas particulier $I = 0$. Soient $y_1, \ldots, y_s$ des générateurs de $M$ comme $R$-module.
Puisque $S^{-1}M$ est engendré par $x_1, \ldots, x_r$, pour chaque $i$,
nous pouvons écrire $y_i = \sum (a_{ij}/s_{ij})x_j$ dans $S^{-1}M$
pour certains $a_{ij} \in R$ et $s_{ij} \in S$. En multipliant par le produit
$s \in S$ des $s_{ij}$, nous voyons que $sy_i = \sum a'_{ij}x_j$
dans $S^{-1}M$ pour certains $a'_{ij} \in R$.
Cela signifie à son tour qu'il existe des $t_i \in S$ tels que
$t_isy_i = \sum t_ia'_{ij}x_j$ dans $M$. Ainsi, si $t \in S$
est le produit des $t_i$, alors nous
voyons que $y_i$ appartient au sous-$R_{st}$-module engendré par $x_1, \ldots, x_r$
dans $M_{st}$. Par conséquent, $x_1, \ldots, x_r$ engendrent $M_{st}$.

\medskip\noindent
Cas général. D'après le cas particulier, nous pouvons trouver $s \in S$
tel que $x_1, \ldots, x_r$ engendrent $(M/IM)_s$ comme $(R/I)_s$-module.
D'après le lemme \ref{lemma-NAK}, nous pouvons trouver $g \in 1 + I_s \subset R_s$
tel que $x_1, \ldots, x_r$ engendrent $(M_s)_g$ comme $(R_s)_g$-module.
Écrivons $g = 1 + i/s'$. Alors $f = ss' + is$ convient ; nous omettons les détails.
\end{proof}
```

</details>

### 15 — lemma-when-surjective-local

Anglais L3735–3766 ; français L3715–3746.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3735) · `FR-ALGEBRA-B5-CHOICE-0015`.

Les quatre hypothèses restent distinctes. B est de type fini comme A-module, m_B comme idéal de B ; on n'ajoute ni finitude de m_A ni noethérianité. Isomorphisme des corps résiduels et surjectivité sur m/m² ne sont pas intervertis. Nakayama (6) s'applique d'abord sur A puis sur B, structures nommées explicitement. L'égalité des corps résiduels est le raccourci source pour l'isomorphisme donné. Dénominateurs et références restent exacts.

Règles : FR-ALGEBRA-B5-RULE-local, FR-ALGEBRA-B5-RULE-residuel, FR-ALGEBRA-B5-RULE-finitude, FR-ALGEBRA-B5-RULE-applications.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-when-surjective-local}
Let $A \to B$ be a local homomorphism of local rings.
Assume
\begin{enumerate}
\item $B$ is finite as an $A$-module,
\item $\mathfrak m_B$ is a finitely generated ideal,
\item $A \to B$ induces an isomorphism on residue fields, and
\item $\mathfrak m_A/\mathfrak m_A^2 \to \mathfrak m_B/\mathfrak m_B^2$
is surjective.
\end{enumerate}
Then $A \to B$ is surjective.
\end{lemma}

\begin{proof}
To show that $A \to B$ is surjective, we view it as a map of $A$-modules
and apply Lemma \ref{lemma-NAK} (6). We conclude it suffices
to show that $A/\mathfrak m_A \to B/\mathfrak m_AB$ is surjective.
As $A/\mathfrak m_A = B/\mathfrak m_B$ it suffices to show that
$\mathfrak m_AB \to \mathfrak m_B$ is surjective. View
$\mathfrak m_AB \to \mathfrak m_B$ as a map of $B$-modules and apply
Lemma \ref{lemma-NAK} (6). We conclude it suffices to see that
$\mathfrak m_AB/\mathfrak m_A\mathfrak m_B \to \mathfrak m_B/\mathfrak m_B^2$
is surjective. This follows from assumption (4).
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-when-surjective-local}
Soit $A \to B$ un morphisme local d'anneaux locaux.
Supposons que
\begin{enumerate}
\item $B$ soit de type fini comme $A$-module,
\item $\mathfrak m_B$ soit un idéal de type fini,
\item $A \to B$ induise un isomorphisme sur les corps résiduels, et
\item $\mathfrak m_A/\mathfrak m_A^2 \to \mathfrak m_B/\mathfrak m_B^2$
soit surjectif.
\end{enumerate}
Alors $A \to B$ est surjectif.
\end{lemma}

\begin{proof}
Pour montrer que $A \to B$ est surjectif, considérons-le comme un morphisme de $A$-modules
et appliquons le lemme \ref{lemma-NAK} (6). Nous en concluons qu'il suffit
de montrer que $A/\mathfrak m_A \to B/\mathfrak m_AB$ est surjectif.
Comme $A/\mathfrak m_A = B/\mathfrak m_B$, il suffit de montrer que
$\mathfrak m_AB \to \mathfrak m_B$ est surjectif. Considérons
$\mathfrak m_AB \to \mathfrak m_B$ comme un morphisme de $B$-modules et appliquons
le lemme \ref{lemma-NAK} (6). Nous en concluons qu'il suffit de voir que
$\mathfrak m_AB/\mathfrak m_A\mathfrak m_B \to \mathfrak m_B/\mathfrak m_B^2$
est surjectif. Cela résulte de l'hypothèse (4).
\end{proof}
```

</details>

## Contrôles exacts

Les 365 régions mathématiques de ce lot concordent sans exception de texte lecteur ni masque général, après la normalisation d’espaces et de commentaires du vérificateur. Les 2 691 régions du préfixe cumulatif passent avec les huit seules exceptions linguistiques déjà enregistrées aux lots 2 et 3.

Labels, références, citations, commandes invariantes, environnements, contrôles TeX et items concordent. Le fichier cible entier est inchangé. Le retour inverse des opérations antérieures reproduit tous les octets du témoin public. Les 131 intervalles successifs couvrent tout le préfixe sans lacune ni chevauchement.

Prochaine lecture : Sous-ensembles ouverts et fermés des spectres, source L3767 / français L3747. Aucun nouveau PDF, aucune publication, aucune approbation humaine et aucune certification du chapitre entier ne sont revendiqués.

