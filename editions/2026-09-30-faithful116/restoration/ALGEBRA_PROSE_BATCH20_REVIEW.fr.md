# Anneaux artiniens

## Résultat et portée

La section complète est comparée : anglais L12699–12828 (130 lignes), français L12597–12716 (120 lignes), soit sept paires complètes. 89 occurrences sont contextualisées. Couverture continue : 53 sections, 462 paires et 3909 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Aucune correction nécessaire dans cette section après lecture complète : le texte est conservé octet pour octet. Le dossier explique les distinctions entre dimension finie et type fini, nilpotence et nilpotence locale, ainsi que la longueur sur soi-même. Aucun résultat ni preuve ne sont réécrits.

Aucune nouvelle proposition de correction de source n’est admise. Le cas nul et le produit vide sont documentés comme convention implicite, sans modifier l’original. Le terme radical de Jacobson n’est pas faussement attesté par le passage de Dat sur les anneaux de Jacobson.

Lecture et réparations produites par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. L’appui documentaire est rétrospectif, non présenté comme une consultation lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch19.fr.tex) · [État précédent](staged/fr/010_algebra.prose-batch19.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH19_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH20_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH20_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH20_OCCURRENCES.json) · [Avant/après](ALGEBRA_PROSE_BATCH20_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH20_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH20_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH20_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH20_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH20_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Jean-François Dat — Algèbre ENS 2016–2017

[Source consultée](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/AlgebreM1/ENS1617.pdf) · [Fichier conservé](canon-consulted/fr-algebra/dat-algebre-ens1617.pdf)

Page 84 entièrement lue, rendue et inspectée ; §1.8.3 et §1.8.4. Page 98 entièrement lue pour distinguer anneau de Jacobson et radical de Jacobson.

Attestations courtes : « module est artinien », « suite décroissante de sous-modules », « de dimension finie », « idéaux maximaux ».

Condition artinienne, longueur et dimension finies ; produit des localisés d'une algèbre commutative de dimension finie.

Limites : La définition de l'exercice porte sur les modules ; la traduction considère l'anneau comme module sur lui-même. Page 98 n'atteste pas radical de Jacobson. Consultation rétrospective, aucune relecture humaine.

SHA-256 : DB5B7FD8139D62C37D0DDDDC90EF22D3EDCF74CC663C5267815E4EA3CECBBB18.

### Antoine Ducros — Introduction à la théorie des schémas

[Source consultée](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Page 24 entièrement lue, notamment §§0.1.7–0.1.7.2.

Attestations courtes : « nilpotent », « nilradical ».

Éléments nilpotents et anneau réduit ; la définition exacte de l'idéal localement nilpotent vient de Stacks L128–133.

Limites : Ne confondre ni nilradical et radical de Jacobson, ni nilpotence des éléments et puissance nulle de l'idéal. Stacks gouverne le contenu.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

## Décision de conservation

Les sept passages restent inchangés après comparaison ; aucun avant/après artificiel ni copie supplémentaire du fichier LaTeX.

## Règles contextualisées

### FR-ALGEBRA-B20-RULE-ARTIN

Condition descendante sur les idéaux ; local est une qualification supplémentaire.

Canon : FR-ALGEBRA-B20-CANON-DAT.

### FR-ALGEBRA-B20-RULE-LENGTH

Distinguer longueur, dimension et génération dans chaque preuve.

Canon : FR-ALGEBRA-B20-CANON-DAT.

### FR-ALGEBRA-B20-RULE-IDEAL

Conserver le rôle exact de chaque idéal ; pas d'attestation nouvelle du radical revendiquée.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B20-RULE-NIL

Distinguer puissance nulle de l'idéal et nilpotence de chaque élément.

Canon : FR-ALGEBRA-B20-CANON-DUCROS.

### FR-ALGEBRA-B20-RULE-LOCAL

Produit des localisations et spectre discret ; l'attestation de Dat porte sur le cas fini dimensionnel.

Canon : FR-ALGEBRA-B20-CANON-DAT.

### FR-ALGEBRA-B20-RULE-LOGIC

Quantificateurs, hypothèses et minimalité relative relus en contexte.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-artinian

Anglais L12699–12706 ; français L12597–12604.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12699) · FR-ALGEBRA-B20-CHOICE-0001.

Anneaux artiniens et artiniens locaux sont distingués ; la théorie des déformations reste un exemple de leur rôle, non un résultat ajouté. Le terme artinien est attesté chez Dat.

Règles : FR-ALGEBRA-B20-RULE-ARTIN, FR-ALGEBRA-B20-RULE-LOCAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Artinian rings}
\label{section-artinian}

\noindent
Artinian rings, and especially local Artinian rings,
play an important role in algebraic geometry, for example
in deformation theory.
```

Français restauré :
```tex
\section{Anneaux artiniens}
\label{section-artinian}

\noindent
Les anneaux artiniens, et en particulier les anneaux artiniens locaux,
jouent un rôle important en géométrie algébrique, par exemple
dans la théorie des déformations.
```

</details>

### 02 — definition-artinian

Anglais L12707–12712 ; français L12605–12610.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12707) · FR-ALGEBRA-B20-CHOICE-0002.

La condition descendante porte sur les idéaux. Dat définit artinien pour les modules par stationnarité des suites décroissantes ; appliqué au module R sur lui-même, ce vocabulaire justifie le français. On n'ajoute pas l'hypothèse noethérienne.

Point particulier à relire : Condition de chaîne descendante et stationnarité des suites décroissantes expriment la même condition ; pas de retouche stylistique nécessaire.

Règles : FR-ALGEBRA-B20-RULE-ARTIN, FR-ALGEBRA-B20-RULE-IDEAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-artinian}
A ring $R$ is {\it Artinian} if it satisfies the
descending chain condition for ideals.
\end{definition}
```

Français restauré :
```tex
\begin{definition}
\label{definition-artinian}
Un anneau $R$ est {\it artinien} s'il satisfait la
condition de chaîne descendante pour les idéaux.
\end{definition}
```

</details>

### 03 — lemma-finite-dimensional-algebra

Anglais L12713–12722 ; français L12611–12620.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12713) · FR-ALGEBRA-B20-CHOICE-0003.

Dimension finie signifie dimension vectorielle sur un corps, et non type fini comme algèbre. La preuve par condition descendante est aussi brève que l'original. Dat §1.8.4 appuie cette distinction.

Point particulier à relire : De dimension finie n'est pas de type fini.

Règles : FR-ALGEBRA-B20-RULE-ARTIN, FR-ALGEBRA-B20-RULE-LENGTH, FR-ALGEBRA-B20-RULE-IDEAL, FR-ALGEBRA-B20-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-finite-dimensional-algebra}
Suppose $R$ is a finite dimensional algebra over a field.
Then $R$ is Artinian.
\end{lemma}

\begin{proof}
The descending chain condition for ideals obviously holds.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-finite-dimensional-algebra}
Supposons que $R$ soit une algèbre de dimension finie sur un corps.
Alors $R$ est artinien.
\end{lemma}

\begin{proof}
La condition de chaîne descendante pour les idéaux est évidente.
\end{proof}
```

</details>

### 04 — lemma-artinian-finite-nr-max

Anglais L12723–12737 ; français L12621–12635.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12723) · FR-ALGEBRA-B20-CHOICE-0004.

Nombre fini d'idéaux maximaux ne signifie pas unicité. La famille deux à deux distincte, les intersections successives et les surjections données par les restes chinois sont conservées. Leur stricte décroissance explique la contradiction ; pas d'ajout à la preuve.

Point particulier à relire : La stricte décroissance suit des maximaux distincts et des surjections ; la formulation concise officielle est conservée.

Règles : FR-ALGEBRA-B20-RULE-ARTIN, FR-ALGEBRA-B20-RULE-IDEAL, FR-ALGEBRA-B20-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-artinian-finite-nr-max}
If $R$ is Artinian then $R$ has only finitely many maximal ideals.
\end{lemma}

\begin{proof}
Suppose that $\mathfrak m_i$, $i = 1, 2, 3, \ldots$ are
pairwise distinct maximal ideals.
Then $\mathfrak m_1 \supset \mathfrak m_1\cap \mathfrak m_2
\supset \mathfrak m_1 \cap \mathfrak m_2 \cap \mathfrak m_3 \supset \ldots$
is an infinite descending sequence (because by the Chinese
remainder theorem all the maps $R \to \oplus_{i = 1}^n R/\mathfrak m_i$
are surjective).
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-artinian-finite-nr-max}
Si $R$ est artinien, alors $R$ ne possède qu'un nombre fini d'idéaux maximaux.
\end{lemma}

\begin{proof}
Supposons que $\mathfrak m_i$, $i = 1, 2, 3, \ldots$, soient
des idéaux maximaux deux à deux distincts.
Alors $\mathfrak m_1 \supset \mathfrak m_1\cap \mathfrak m_2
\supset \mathfrak m_1 \cap \mathfrak m_2 \cap \mathfrak m_3 \supset \ldots$
est une suite descendante infinie (car, par le
théorème des restes chinois, toutes les applications
$R \to \oplus_{i = 1}^n R/\mathfrak m_i$ sont surjectives).
\end{proof}
```

</details>

### 05 — lemma-artinian-radical-nilpotent

Anglais L12738–12756 ; français L12636–12654.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12738) · FR-ALGEBRA-B20-CHOICE-0005.

La conclusion exige une puissance nulle de l'idéal, pas seulement des éléments nilpotents. I est le radical, J l'annulateur de I^n, et J′ un sur-idéal strict minimal. Le quotient simple, l'idéal maximal et l'annulation de J′ restent dans l'ordre source. Annule traduit correctement kills.

Point particulier à relire : Dat p.98 définit un anneau de Jacobson, non le radical de Jacobson : ne pas présenter cette autre notion comme attestation du radical. Ce dernier est conservé sur justification source.

Règles : FR-ALGEBRA-B20-RULE-ARTIN, FR-ALGEBRA-B20-RULE-IDEAL, FR-ALGEBRA-B20-RULE-NIL, FR-ALGEBRA-B20-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-artinian-radical-nilpotent}
Let $R$ be Artinian. The Jacobson radical of $R$ is a nilpotent ideal.
\end{lemma}

\begin{proof}
Let $I \subset R$ be the Jacobson radical.
Note that $I \supset I^2 \supset I^3 \supset \ldots$ is a descending
sequence. Thus $I^n = I^{n + 1}$ for some $n$.
Set $J = \{ x\in R \mid xI^n = 0\}$. We have to show $J = R$.
If not, choose an ideal $J' \not = J$, $J \subset J'$ minimal (possible
by the Artinian property). Then $J'/J$ is a simple $R$-module, hence
isomorphic to $R/\mathfrak m$ for some maximal ideal $\mathfrak m$,
see Lemma \ref{lemma-characterize-length-1}.
Then $\mathfrak m I^n$ kills $J'$. Since $I \subset \mathfrak m$
we conclude that $I^{n + 1} = I^n$ kills $J'$. Hence $J' = J$
which is a contradiction.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-artinian-radical-nilpotent}
Soit $R$ artinien. Le radical de Jacobson de $R$ est un idéal nilpotent.
\end{lemma}

\begin{proof}
Soit $I \subset R$ le radical de Jacobson.
Remarquons que $I \supset I^2 \supset I^3 \supset \ldots$ est une suite
descendante. Ainsi $I^n = I^{n + 1}$ pour un certain $n$.
Posons $J = \{ x\in R \mid xI^n = 0\}$. Nous devons montrer que $J = R$.
Sinon, choisissons un idéal $J' \not = J$, $J \subset J'$ minimal
(possible par la propriété artinienne). Alors $J'/J$ est un
$R$-module simple, donc isomorphe à $R/\mathfrak m$ pour un certain idéal maximal $\mathfrak m$,
voir le Lemme \ref{lemma-characterize-length-1}.
Alors $\mathfrak m I^n$ annule $J'$. Comme $I \subset \mathfrak m$,
nous concluons que $I^{n + 1} = I^n$ annule $J'$. Donc $J' = J$,
ce qui est une contradiction.
\end{proof}
```

</details>

### 06 — lemma-product-local

Anglais L12757–12785 ; français L12655–12683.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12757) · FR-ALGEBRA-B20-CHOICE-0006.

Localement nilpotent conserve la définition officielle L128–133 : chaque élément est nilpotent. La finitude du nombre d'idéaux maximaux est conservée. On identifie tous les premiers aux maximaux, puis on décompose le spectre discret et l'anneau en produit. Produit n'est pas remplacé par somme directe. La répétition chaque R_i / pour chaque i est stylistique et sans effet sur le sens ; texte conservé.

Point particulier à relire : L'anneau nul correspond au produit vide ; les n−1 applications décrites supposent implicitement n≥1. L'énoncé reste correct et ce raccourci n'est pas réécrit. Définition officielle de localement nilpotent relue.

Règles : FR-ALGEBRA-B20-RULE-IDEAL, FR-ALGEBRA-B20-RULE-NIL, FR-ALGEBRA-B20-RULE-LOCAL, FR-ALGEBRA-B20-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-product-local}
Any ring with finitely many maximal ideals and
locally nilpotent Jacobson radical is the product of its localizations
at its maximal ideals. Also, all primes are maximal.
\end{lemma}

\begin{proof}
Let $R$ be a ring with finitely many maximal ideals
$\mathfrak m_1, \ldots, \mathfrak m_n$.
Let $I = \bigcap_{i = 1}^n \mathfrak m_i$
be the Jacobson radical of $R$. Assume $I$ is locally nilpotent.
Let $\mathfrak p$ be a prime ideal of $R$.
Since every prime contains every nilpotent
element of $R$ we see
$ \mathfrak p \supset \mathfrak m_1 \cap \ldots \cap \mathfrak m_n$.
Since $\mathfrak m_1 \cap \ldots \cap \mathfrak m_n \supset
\mathfrak m_1 \ldots \mathfrak m_n$
we conclude $\mathfrak p \supset \mathfrak m_1 \ldots \mathfrak m_n$.
Hence $\mathfrak p \supset \mathfrak m_i$ for some $i$, and so
$\mathfrak p = \mathfrak m_i$. Thus the spectrum of $R$
is the discrete topological space $\{\mathfrak m_1, \ldots, \mathfrak m_n\}$.
By Lemma \ref{lemma-disjoint-implies-product} applied $n - 1$ times
we find that $R = R_1 \times \ldots \times R_n$ where the
spectrum of $R_i$ is a singleton for each $i$.
Thus $R_i$ is a local ring and since it is a localization of $R$
(by the lemma), it is one of the local rings of $R$ as desired.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-product-local}
Tout anneau ayant un nombre fini d'idéaux maximaux et
un radical de Jacobson localement nilpotent est le produit de ses localisations
en ses idéaux maximaux. De plus, tous les idéaux premiers sont maximaux.
\end{lemma}

\begin{proof}
Soit $R$ un anneau ayant un nombre fini d'idéaux maximaux
$\mathfrak m_1, \ldots, \mathfrak m_n$.
Soit $I = \bigcap_{i = 1}^n \mathfrak m_i$
le radical de Jacobson de $R$. Supposons que $I$ soit localement nilpotent.
Soit $\mathfrak p$ un idéal premier de $R$.
Comme tout idéal premier contient tout élément
nilpotent de $R$, nous voyons
$ \mathfrak p \supset \mathfrak m_1 \cap \ldots \cap \mathfrak m_n$.
Comme $\mathfrak m_1 \cap \ldots \cap \mathfrak m_n \supset
\mathfrak m_1 \ldots \mathfrak m_n$,
nous concluons $\mathfrak p \supset \mathfrak m_1 \ldots \mathfrak m_n$.
Donc $\mathfrak p \supset \mathfrak m_i$ pour un certain $i$, et ainsi
$\mathfrak p = \mathfrak m_i$. Le spectre de $R$
est donc l'espace topologique discret $\{\mathfrak m_1, \ldots, \mathfrak m_n\}$.
Par le Lemme \ref{lemma-disjoint-implies-product}, appliqué $n - 1$ fois,
nous trouvons que $R = R_1 \times \ldots \times R_n$, où le
spectre de chaque $R_i$ est un singleton pour chaque $i$.
Ainsi $R_i$ est un anneau local et, comme il est une localisation de $R$
(par le lemme), il est l'un des anneaux locaux de $R$, comme voulu.
\end{proof}
```

</details>

### 07 — lemma-artinian-finite-length

Anglais L12786–12828 ; français L12684–12716.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12786) · FR-ALGEBRA-B20-CHOICE-0007.

L'équivalence concerne R comme module sur lui-même. Noethérien est une conclusion, non une hypothèse. La réduction au cas local, la nilpotence de l'idéal maximal et les dimensions des quotients vectoriels sont conservées. Une dimension infinie donnerait une chaîne descendante infinie de sous-espaces et donc d'idéaux ; aucun corps fini n'est supposé.

Point particulier à relire : Longueur finie sur soi-même n'est ni un cardinal fini ni la seule génération finie sur soi-même.

Règles : FR-ALGEBRA-B20-RULE-ARTIN, FR-ALGEBRA-B20-RULE-LENGTH, FR-ALGEBRA-B20-RULE-IDEAL, FR-ALGEBRA-B20-RULE-LOCAL, FR-ALGEBRA-B20-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-artinian-finite-length}
A ring $R$ is Artinian if and only if it has finite length
as a module over itself. Any such ring $R$ is both Artinian and
Noetherian, any prime ideal of $R$ is a maximal ideal, and $R$ is equal
to the (finite) product of its localizations at its maximal ideals.
\end{lemma}

\begin{proof}
If $R$ has finite length over itself then it satisfies both
the ascending chain condition and the descending chain
condition for ideals. Hence it is both Noetherian and Artinian.
Any Artinian ring is equal to product of its localizations
at maximal ideals by Lemmas \ref{lemma-artinian-finite-nr-max},
\ref{lemma-artinian-radical-nilpotent}, and \ref{lemma-product-local}.

\medskip\noindent
Suppose that $R$ is Artinian. We will show $R$ has finite
length over itself. It suffices to exhibit a chain of
submodules whose successive quotients have finite length.
By what we said above
we may assume that $R$ is local, with maximal ideal $\mathfrak m$.
By Lemma \ref{lemma-artinian-radical-nilpotent} we have
$\mathfrak m^n =0$ for some $n$.
Consider the sequence
$0 = \mathfrak m^n \subset \mathfrak m^{n-1} \subset
\ldots \subset \mathfrak m \subset R$. By Lemma
\ref{lemma-dimension-is-length} the length of each subquotient
$\mathfrak m^j/\mathfrak m^{j + 1}$ is the dimension of this
as a vector space over $\kappa(\mathfrak m)$. This has to be
finite since otherwise we would have an infinite descending
chain of sub vector spaces which would correspond to an
infinite descending chain of ideals in $R$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-artinian-finite-length}
Un anneau $R$ est artinien si et seulement s'il est de longueur finie
comme module sur lui-même. Un tel anneau $R$ est à la fois artinien et
noethérien, tout idéal premier de $R$ est maximal, et $R$ est égal
au produit (fini) de ses localisations en ses idéaux maximaux.
\end{lemma}

\begin{proof}
Si $R$ est de longueur finie sur lui-même, il satisfait à la fois
la condition de chaîne ascendante et la condition de chaîne descendante
pour les idéaux. Il est donc à la fois noethérien et artinien.
Tout anneau artinien est égal au produit de ses localisations
en ses idéaux maximaux par les Lemmes \ref{lemma-artinian-finite-nr-max},
\ref{lemma-artinian-radical-nilpotent} et \ref{lemma-product-local}.

\medskip\noindent
Supposons que $R$ soit artinien. Nous allons montrer que $R$ est de longueur finie
sur lui-même. Il suffit d'exhiber une chaîne de
sous-modules dont les quotients successifs sont de longueur finie.
D'après ce qui précède, nous pouvons supposer que $R$ est local, d'idéal maximal $\mathfrak m$.
Par le Lemme \ref{lemma-artinian-radical-nilpotent}, nous avons
$\mathfrak m^n =0$ pour un certain $n$.
Considérons la suite
$0 = \mathfrak m^n \subset \mathfrak m^{n-1} \subset
\ldots \subset \mathfrak m \subset R$. Par le Lemme
\ref{lemma-dimension-is-length}, la longueur de chaque quotient successif
$\mathfrak m^j/\mathfrak m^{j + 1}$ est sa dimension
comme espace vectoriel sur $\kappa(\mathfrak m)$. Celle-ci doit être
finie, car sinon nous aurions une chaîne descendante infinie
de sous-espaces vectoriels, qui correspondrait à une chaîne descendante infinie d'idéaux dans $R$.
\end{proof}
```

</details>

## Contrôles et suite

Les 67 régions mathématiques sont strictement identiques sans exception nouvelle. Le préfixe de 9 095 régions passe avec vingt-sept exceptions linguistiques antérieures. Tous les octets français restent identiques au lot précédent.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items restent identiques. Il n’y a pas de citation bibliographique ni de titre facultatif traduit dans ce lot. Les opérations inverses retrouvent le lot précédent puis tous les octets du témoin public préservé. Préfixe déjà relu et suffixe encore non relu sont inchangés.

Les 462 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Homomorphismes essentiellement de type fini, anglais L12829 / français L12717. Aucun PDF nouveau ni publication ; restauration globale en cours.

