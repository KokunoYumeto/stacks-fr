# Algèbre commutative : descente et platitude

## Résultat et portée

Deux sections entièrement comparées : anglais L8339–9306 et français L8319–9286, soit 968 lignes de chaque témoin. Les 29 paires comprennent tous les énoncés, preuves, notes et transitions. 311 occurrences sont reliées à des règles contextualisées. Le préfixe atteint 39 sections, 324 paires et 2572 occurrences. Le chapitre et l’édition restent inachevés.

Trois opérations exactes : homologie → cohomologie, conformément au mot anglais ; deux précisions morphisme d’anneaux locaux → morphisme local d’anneaux locaux, conformément à local ring map. Aucune formule ni référence ne change.

Trois observations séparées concernent le signe d’une égalité, le cas z=0 d’un changement de polynôme minimal et le sens d’une flèche dans une note. Elles ne sont ni trois nouveaux errata admis ni trois théorèmes réfutés.

Lecture, réparations et dossier produits par OpenAI Codex — GPT-6 Astra, Ultra effort ; comparaison assistée par IA, sans relecture humaine. Les attestations sont rétrospectives et limitées aux passages effectivement lus ; leur absence pour certains syntagmes est indiquée.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch12.fr.tex) · [État français précédent](staged/fr/010_algebra.prose-batch11.fr.tex) · [Lot précédent](ALGEBRA_PROSE_BATCH11_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH12_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH12_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH12_OCCURRENCES.json) · [Avant/après](ALGEBRA_PROSE_BATCH12_REPAIRS.json) · [Exceptions linguistiques en formule](ALGEBRA_PROSE_BATCH12_MATH_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH12_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH12_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Antoine Ducros — Introduction à la théorie des schémas

[Source consultée](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages 92–93 lues entièrement, 2.4.14–2.4.17.1 : exactitude des foncteurs, produit tensoriel, modules plats.

Attestations courtes : « exact à gauche », « exact à droite », « transforme les injections en injections ».

Attestation de plat, platitude, exactitude, colimites et de l'expression par conservation des injections. La lecture compare les définitions, pas seulement leurs mots.

Limites : Le cours annonce qu'il développe peu la platitude ; il n'atteste pas sur ces pages tous les critères du lot ni la fidèle platitude. Pas de nouveau rendu visuel de ces deux pages revendiqué.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

### Jean-François Dat — Théorie des schémas

[Source consultée](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/Schemas/Schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/dat-schemas.pdf)

Pages 9–11 lues entièrement ; sections 1.2.6–1.2.8. Page 10 rendue et inspectée.

Attestations courtes : « fidèlement plat », « Un morphisme local et plat entre anneaux locaux », « colimites filtrantes ».

Définition par tensorisation exacte et détection de zéro ; critère spectral ; distinction morphisme local/anneaux locaux ; localisation et généralisation.

Limites : La définition imprimée de local inverse m et n dans φ⁻¹(m)=n ; le rendu confirme cette coquille, qui n'est pas importée. Le corollaire et son application utilisent correctement la notion. Ces pages ne sont pas invoquées comme attestation de clôture intégrale d'un idéal ni du titre théorème de descente.

SHA-256 : 9298B062AC2BDF64161A107980A30F98E1F2DF6DEB4DA98E1FEB21BA494D26A1.

### Alexandre Bailleul — page d'enseignement, Algèbre avancée

[Source consultée](https://abailleul.perso.math.cnrs.fr/) · [Fichier conservé](canon-consulted/fr-algebra/bailleul-page-20260930.html)

Rubrique TD d'Algèbre Avancée, intitulé du DM lié à Enseignement/AlgAv/DM2.pdf ; HTML conservé, ligne 246.

Attestations courtes : « critère équationnel de platitude ».

Attestation primaire du nom français de ce critère dans un enseignement mathématique M1.

Limites : Seul l'intitulé est français. Le PDF lié, consulté, est anglais et ne sert pas d'attestation de syntaxe ou de registre français. Aucune attribution d'une traduction française intégrale à cet auteur.

SHA-256 : 4E25B8FADD4C018F9ED756A99CE2150F5F4FA714CCCC7A51150AA2116A7FF76F.

## Les trois opérations exactes

### FR-ALGEBRA-B12-REPAIR-0001

Anglais L9152 ; français L9132.

Avant :
```tex
Soit $H$ l'homologie du complexe,
```

Après :
```tex
Soit $H$ la cohomologie du complexe,
```

Restauration de désignation cohomologie ; aucune modification du quotient, des degrés ou de la preuve.

### FR-ALGEBRA-B12-REPAIR-0002

Anglais L9273 ; français L9253.

Avant :
```tex
D'après le lemme \ref{lemma-flat-localization}, le morphisme d'anneaux locaux
```

Après :
```tex
D'après le lemme \ref{lemma-flat-localization}, le morphisme local d'anneaux locaux
```

Deux précisions de portée lexicale, justifiées par le qualificatif local explicite de l'anglais et par le corollaire français de Dat.

### FR-ALGEBRA-B12-REPAIR-0003

Anglais L9275 ; français L9255.

Avant :
```tex
D'après le lemme \ref{lemma-local-flat-ff}, ce morphisme d'anneaux locaux est fidèlement
```

Après :
```tex
D'après le lemme \ref{lemma-local-flat-ff}, ce morphisme local d'anneaux locaux est fidèlement
```

Deux précisions de portée lexicale, justifiées par le qualificatif local explicite de l'anglais et par le corollaire français de Dat.

## Règles contextualisées

### FR-ALGEBRA-B12-RULE-INTEGRAL

Termes suivis dans l'équation unitaire et ses coefficients ; l'emploi sur un idéal est vérifié contre sa définition exacte, sans prétendre à une attestation externe nouvelle.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B12-RULE-NORMAL

Normalité, intégrité et corps des fractions sont distingués dans la preuve source et dans le registre déjà consulté au lot 11 ; pas de nouvelle lecture de ce canon antérieur revendiquée.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B12-RULE-FLAT

Plat conserve l'exactitude ; fidèlement plat ajoute sa réflexion. Les variantes d'accord dépendent du module, de l'algèbre ou de la composée, sans changer la propriété.

Canon : FR-ALGEBRA-B12-CANON-DAT, FR-ALGEBRA-B12-CANON-DUCROS.

### FR-ALGEBRA-B12-RULE-EXACT

Exactitude, injection et surjection sont contrôlées à chaque place ; l'argument ne confond ni noyau, ni image, ni conditions gauche/droite.

Canon : FR-ALGEBRA-B12-CANON-DUCROS, FR-ALGEBRA-B12-CANON-DAT.

### FR-ALGEBRA-B12-RULE-TENSOR

Chaque tensorisation garde son anneau de base et les hypothèses nécessaires à son exactitude.

Canon : FR-ALGEBRA-B12-CANON-DUCROS, FR-ALGEBRA-B12-CANON-DAT.

### FR-ALGEBRA-B12-RULE-FILTERED

Système/colimite filtrant(e) rend directed ; la commutation à toutes les colimites n'est pas confondue avec l'exactitude des seules colimites filtrantes.

Canon : FR-ALGEBRA-B12-CANON-DAT, FR-ALGEBRA-B12-CANON-DUCROS.

### FR-ALGEBRA-B12-RULE-LOCAL

Localisation et morphisme local ne sont pas synonymes. Le qualificatif de morphisme est explicité lorsqu'il est nécessaire et déjà présent dans l'anglais.

Canon : FR-ALGEBRA-B12-CANON-DAT.

### FR-ALGEBRA-B12-RULE-FINITE

Fini pour un module signifie de type fini, non cardinal fini ; type fini et présentation finie restent distincts.

Canon : FR-ALGEBRA-B12-CANON-DAT.

### FR-ALGEBRA-B12-RULE-CRITERION

Intitulé attesté sur la page de l'enseignant ; le sens de triviale reste celui de la définition source complète.

Canon : FR-ALGEBRA-B12-CANON-BAILLEUL.

### FR-ALGEBRA-B12-RULE-PROOF

Portée des quantificateurs, négations et implications vérifiée dans chaque paire complète. Ces formes usuelles ne reçoivent pas de fausses attestations individualisées.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B12-RULE-DESCENT

Going down relève les inclusions de premiers ; descente de la platitude réfléchit une propriété après changement de base. Le contexte tranche et les deux constructions ne sont pas assimilées.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B12-RULE-COHOMOLOGY

La désignation cohomologie suit exactement le texte officiel ; noyau/image et annulateur sont contrôlés dans leurs formules. Dat/Ducros attestent le registre noyau et annulateur, pas toute la terminologie cohomologique sur ces pages.

Canon : FR-ALGEBRA-B12-CANON-DAT, FR-ALGEBRA-B12-CANON-DUCROS.

## Passages parallèles complets

### 01 — section-going-down-integral-over-normal

Anglais L8339–8346 ; français L8319–8326.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8339) · FR-ALGEBRA-B12-CHOICE-0001.

Descente traduit going down par cohérence avec la définition interne des inclusions de premiers. Le titre garde les deux hypothèses, intégralité de l'extension et normalité de l'anneau de base. Le début annonce une préparation par les idéaux, sans ajouter de résultat. Les nouvelles pages françaises consultées ne donnent pas ce titre exact ; son choix reste compositionnel, non faussement attesté.

Règles : FR-ALGEBRA-B12-RULE-INTEGRAL, FR-ALGEBRA-B12-RULE-NORMAL, FR-ALGEBRA-B12-RULE-DESCENT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Going down for integral over normal}
\label{section-going-down-integral-over-normal}

\noindent
We first play around a little bit with the notion of elements
integral over an ideal, and then we prove the theorem referred
to in the section title.
```

Français restauré :
```tex
\section{Descente pour une extension entière au-dessus d'un anneau normal}
\label{section-going-down-integral-over-normal}

\noindent
Commençons par manipuler un peu la notion d'éléments
entiers sur un idéal, puis démontrons le théorème mentionné
dans le titre de la section.
```

</details>

### 02 — definition-integral-over-ideal

Anglais L8347–8364 ; français L8327–8344.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8347) · FR-ALGEBRA-B12-CHOICE-0002.

Entier sur I conserve la condition précise aj∈I^(d−j), plus forte que aj∈I. Le morphisme φ peut être non injectif. La clôture intégrale de l'idéal est introduite seulement dans le cas φ=idR ; le texte ne transforme pas ce cas particulier en hypothèse générale. Le choix clôture suit le registre établi dans le lot précédent, avec application à cette définition vérifiée ici ; aucune nouvelle attestation extérieure du syntagme entier sur un idéal n'est revendiquée.

Règles : FR-ALGEBRA-B12-RULE-INTEGRAL, FR-ALGEBRA-B12-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-integral-over-ideal}
Let $\varphi : R \to S$ be a ring map.
Let $I \subset R$ be an ideal.
We say an element $g \in S$ is
{\it integral over $I$} if
there exists a monic
polynomial $P = x^d + \sum_{j < d} a_j x^j$
with coefficients $a_j \in I^{d-j}$ such
that $P^\varphi(g) = 0$ in $S$.
\end{definition}

\noindent
This is mostly used when $\varphi = \text{id}_R : R \to R$.
In this case the set $I'$ of elements integral over $I$ is called
the {\it integral closure of $I$}. We will see that $I'$ is
an ideal of $R$ (and of course $I \subset I'$).
```

Français restauré :
```tex
\begin{definition}
\label{definition-integral-over-ideal}
Soit $\varphi : R \to S$ un morphisme d'anneaux.
Soit $I \subset R$ un idéal.
Nous disons qu'un élément $g \in S$ est
{\it entier sur $I$} s'il
existe un polynôme unitaire
$P = x^d + \sum_{j < d} a_j x^j$
à coefficients $a_j \in I^{d-j}$ tel
que $P^\varphi(g) = 0$ dans $S$.
\end{definition}

\noindent
Ceci est surtout utilisé lorsque $\varphi = \text{id}_R : R \to R$.
Dans ce cas, l'ensemble $I'$ des éléments entiers sur $I$ est appelé
la {\it clôture intégrale de $I$}. Nous verrons que $I'$ est
un idéal de $R$ (et, bien sûr, $I \subset I'$).
```

</details>

### 03 — lemma-characterize-integral-ideal

Anglais L8365–8397 ; français L8345–8377.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8365) · FR-ALGEBRA-B12-CHOICE-0003.

Sous-anneau engendré et partie de degré d−j conservent le rôle de la graduation en t. On extrait la composante homogène de degré d de l'équation entière de st ; on ne substitue pas un coefficient quelconque de aj. La réciproque homogénéise les coefficients par t^(d−j). Les deux polynômes et leurs variables restent distincts.

Règles : FR-ALGEBRA-B12-RULE-INTEGRAL, FR-ALGEBRA-B12-RULE-PROOF.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-integral-ideal}
Let $\varphi : R \to S$ be a ring map.
Let $I \subset R$ be an ideal.
Let $A = \sum I^nt^n \subset R[t]$ be the
subring of the polynomial ring
generated by $R \oplus It \subset R[t]$.
An element $s \in S$ is integral over $I$ if
and only if the element $st \in S[t]$
is integral over $A$.
\end{lemma}

\begin{proof}
Suppose $st$ is integral over $A$.
Let $P = x^d + \sum_{j < d} a_j x^j$
be a monic polynomial with coefficients in $A$
such that $P^\varphi(st) = 0$. Let $a_j' \in A$
be the degree $d-j$ part of $a_j$, in other
words $a_j' = a_j'' t^{d-j}$ with $a_j'' \in I^{d-j}$.
For degree reasons we still have
$(st)^d + \sum_{j < d} \varphi(a_j'') t^{d-j} (st)^j = 0$.
Hence $s^d + \sum_{j < d} \varphi(a_j'') s^j = 0$
and we see that $s$ is integral over $I$.

\medskip\noindent
Suppose that $s$ is integral over $I$.
Say $P = x^d + \sum_{j < d} a_j x^j$
with $a_j \in I^{d-j}$. Then we immediately find a
polynomial $Q = x^d + \sum_{j < d} (a_j t^{d-j}) x^j$
with coefficients in $A$ which proves that
$st$ is integral over $A$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-characterize-integral-ideal}
Soit $\varphi : R \to S$ un morphisme d'anneaux.
Soit $I \subset R$ un idéal.
Soit $A = \sum I^nt^n \subset R[t]$ le
sous-anneau de l'anneau de polynômes
engendré par $R \oplus It \subset R[t]$.
Un élément $s \in S$ est entier sur $I$ si
et seulement si l'élément $st \in S[t]$
est entier sur $A$.
\end{lemma}

\begin{proof}
Supposons que $st$ soit entier sur $A$.
Soit $P = x^d + \sum_{j < d} a_j x^j$
un polynôme unitaire à coefficients dans $A$
tel que $P^\varphi(st) = 0$. Soit $a_j' \in A$
la partie de degré $d-j$ de $a_j$, autrement
dit $a_j' = a_j'' t^{d-j}$ avec $a_j'' \in I^{d-j}$.
Pour des raisons de degré, nous avons encore
$(st)^d + \sum_{j < d} \varphi(a_j'') t^{d-j} (st)^j = 0$.
Ainsi, $s^d + \sum_{j < d} \varphi(a_j'') s^j = 0$,
et nous voyons que $s$ est entier sur $I$.

\medskip\noindent
Supposons que $s$ soit entier sur $I$.
Écrivons $P = x^d + \sum_{j < d} a_j x^j$
avec $a_j \in I^{d-j}$. Nous trouvons alors immédiatement un
polynôme $Q = x^d + \sum_{j < d} (a_j t^{d-j}) x^j$
à coefficients dans $A$ qui démontre que
$st$ est entier sur $A$.
\end{proof}
```

</details>

### 04 — lemma-integral-over-ideal-is-submodule

Anglais L8398–8420 ; français L8378–8400.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8398) · FR-ALGEBRA-B12-CHOICE-0004.

R-sous-module n'est pas remplacé par idéal de S. L'addition résulte de la clôture intégrale dans S[t], et la stabilité multiplicative ne porte que sur s entier sur R. Le passage de s à un élément de degré zéro ne change pas son anneau d'origine. La virgule terminale anglaise devient un point : ponctuation idiomatique, sans réparation mathématique.

Règles : FR-ALGEBRA-B12-RULE-INTEGRAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-integral-over-ideal-is-submodule}
Let $\varphi : R \to S$ be a ring map.
Let $I \subset R$ be an ideal.
The set of elements of $S$ which are integral
over $I$ form a $R$-submodule of $S$.
Furthermore, if $s \in S$ is integral over
$R$, and $s'$ is integral over $I$, then
$ss'$ is integral over $I$.
\end{lemma}

\begin{proof}
We will use Lemma \ref{lemma-integral-closure-is-ring} without
further mention. Closure under addition is clear from the
characterization of Lemma \ref{lemma-characterize-integral-ideal}
whose notation we adopt.
Any element $s \in S$ which is integral over
$R$ corresponds to the degree $0$ element $s$ of $S[t]$
which is integral over $A$ (because $R \subset A$).
Hence we see that multiplication by $s$ on $S[t]$
preserves the property of being integral over $A$,
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-integral-over-ideal-is-submodule}
Soit $\varphi : R \to S$ un morphisme d'anneaux.
Soit $I \subset R$ un idéal.
L'ensemble des éléments de $S$ qui sont entiers
sur $I$ forme un $R$-sous-module de $S$.
En outre, si $s \in S$ est entier sur
$R$ et si $s'$ est entier sur $I$, alors
$ss'$ est entier sur $I$.
\end{lemma}

\begin{proof}
Nous utiliserons le lemme \ref{lemma-integral-closure-is-ring} sans
autre mention. La stabilité par addition résulte clairement de la
caractérisation du lemme \ref{lemma-characterize-integral-ideal},
dont nous adoptons les notations.
Tout élément $s \in S$ qui est entier sur
$R$ correspond à l'élément de degré $0$, $s$, de $S[t]$,
qui est entier sur $A$ (car $R \subset A$).
Nous voyons donc que la multiplication par $s$ sur $S[t]$
préserve la propriété d'être entier sur $A$.
\end{proof}
```

</details>

### 05 — lemma-integral-integral-over-ideal

Anglais L8421–8431 ; français L8401–8411.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8421) · FR-ALGEBRA-B12-CHOICE-0005.

Le morphisme entier rend chacun des coefficients de S utilisable dans le lemme précédent ; tout élément de IS, somme finie de produits, est donc entier sur I. Le texte ne suppose pas S fini sur R. La preuve immédiate est conservée, sans lui substituer une nouvelle démonstration.

Règles : FR-ALGEBRA-B12-RULE-INTEGRAL, FR-ALGEBRA-B12-RULE-PROOF.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-integral-integral-over-ideal}
Suppose $\varphi : R \to S$ is integral.
Suppose $I \subset R$ is an ideal.
Then every element of $IS$ is integral over $I$.
\end{lemma}

\begin{proof}
Immediate from Lemma \ref{lemma-integral-over-ideal-is-submodule}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-integral-integral-over-ideal}
Supposons que $\varphi : R \to S$ soit entier.
Supposons que $I \subset R$ soit un idéal.
Alors tout élément de $IS$ est entier sur $I$.
\end{lemma}

\begin{proof}
C'est immédiat d'après le lemme \ref{lemma-integral-over-ideal-is-submodule}.
\end{proof}
```

</details>

### 06 — lemma-polynomials-divide

Anglais L8432–8497 ; français L8412–8477.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8432) · FR-ALGEBRA-B12-CHOICE-0006.

Les deux assertions sont distinctes : coefficients entiers sur R0, puis appartenance au radical dans R contenant aussi les ai. La preuve utilise les racines dans L pour l'intégralité, puis un quotient réduit et ses localisations aux premiers minimaux pour l'annulation. Anneau factoriel rend UFD ; unitaire explique pourquoi associé implique égal ici. Les degrés limites et familles éventuellement vides restent traités aussi elliptiquement que dans la source, sans hypothèse ajoutée.

Règles : FR-ALGEBRA-B12-RULE-INTEGRAL, FR-ALGEBRA-B12-RULE-LOCAL, FR-ALGEBRA-B12-RULE-PROOF, FR-ALGEBRA-B12-RULE-COHOMOLOGY.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-polynomials-divide}
Let $K$ be a field. Let $n, m \in \mathbf{N}$ and
$a_0, \ldots, a_{n - 1}, b_0, \ldots, b_{m - 1} \in K$.
If the polynomial $x^n + a_{n - 1}x^{n - 1} + \ldots + a_0$
divides the polynomial $x^m + b_{m - 1} x^{m - 1} + \ldots + b_0$
in $K[x]$ then
\begin{enumerate}
\item $a_0, \ldots, a_{n - 1}$ are integral over any subring
$R_0$ of $K$ containing the elements $b_0, \ldots, b_{m - 1}$, and
\item each $a_i$ lies in $\sqrt{(b_0, \ldots, b_{m-1})R}$
for any subring $R \subset K$ containing the elements
$a_0, \ldots, a_{n - 1}, b_0, \ldots, b_{m - 1}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Let $L/K$ be a field extension such that we can write
$x^m + b_{m - 1} x^{m - 1} + \ldots + b_0 =
\prod_{i = 1}^m (x - \beta_i)$ with $\beta_i \in L$.
See Fields, Section \ref{fields-section-splitting-fieds}.
Each $\beta_i$ is integral over $R_0$.
Since each $a_i$ is a homogeneous polynomial in $\beta_1, \ldots, \beta_m$
we deduce the same for the $a_i$
(use Lemma \ref{lemma-integral-closure-is-ring}). This proves (1).

\medskip\noindent
Let $R$ be as in (2). Choose $c_0, \ldots, c_{m - n - 1} \in K$ such that
$$
\begin{matrix}
x^m + b_{m - 1} x^{m - 1} + \ldots + b_0 =  \\
(x^n + a_{n - 1}x^{n - 1} + \ldots + a_0)
(x^{m - n} + c_{m - n - 1}x^{m - n - 1}+ \ldots + c_0).
\end{matrix}
$$
This equation implies
\begin{align*}
c_{m - n - 1} & = b_{m - 1} - a_{n - 1}, \\
c_{m - n - 2} & = b_{m - 2} - a_{n - 2} - a_{n - 1}c_{m - n - 1}, \\
\ldots
\end{align*}
Thus $c_j \in R$ for all $j$. Dividing out the radical
$\sqrt{(b_0, \ldots, b_{m - 1})}$ we get a reduced ring $\overline{R}$.
We have to show that the images $\overline{a}_i \in \overline{R}$
are zero. And in
$\overline{R}[x]$ we have the relation
$$
\begin{matrix}
x^m = x^m + \overline{b}_{m - 1} x^{m - 1} + \ldots + \overline{b}_0 = \\
(x^n + \overline{a}_{n - 1}x^{n - 1} + \ldots + \overline{a}_0)
(x^{m - n} + \overline{c}_{m - n - 1}x^{m - n - 1}+ \ldots + \overline{c}_0).
\end{matrix}
$$
It is easy to see that this implies $\overline{a}_i = 0$ for all $i$. Indeed
by Lemma \ref{lemma-minimal-prime-reduced-ring} the localization of
$\overline{R}$ at a minimal prime $\mathfrak{p}$ is a field and
$\overline{R}_{\mathfrak p}[x]$ a UFD. Thus
$f = x^n + \sum \overline{a}_i x^i$
is associated to $x^n$ and since $f$ is monic $f = x^n$
in $\overline{R}_{\mathfrak p}[x]$.
Then there exists an $s \in \overline{R}$, $s \not\in \mathfrak p$
such that $s(f - x^n) = 0$.  Therefore all $\overline{a}_i$ lie
in $\mathfrak p$ and we conclude by
Lemma \ref{lemma-reduced-ring-sub-product-fields}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-polynomials-divide}
Soit $K$ un corps. Soient $n, m \in \mathbf{N}$ et
$a_0, \ldots, a_{n - 1}, b_0, \ldots, b_{m - 1} \in K$.
Si le polynôme $x^n + a_{n - 1}x^{n - 1} + \ldots + a_0$
divise le polynôme $x^m + b_{m - 1} x^{m - 1} + \ldots + b_0$
dans $K[x]$, alors :
\begin{enumerate}
\item $a_0, \ldots, a_{n - 1}$ sont entiers sur tout sous-anneau
$R_0$ de $K$ contenant les éléments $b_0, \ldots, b_{m - 1}$, et
\item chaque $a_i$ appartient à $\sqrt{(b_0, \ldots, b_{m-1})R}$
pour tout sous-anneau $R \subset K$ contenant les éléments
$a_0, \ldots, a_{n - 1}, b_0, \ldots, b_{m - 1}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Soit $L/K$ une extension de corps telle que nous puissions écrire
$x^m + b_{m - 1} x^{m - 1} + \ldots + b_0 =
\prod_{i = 1}^m (x - \beta_i)$ avec $\beta_i \in L$.
Voir Corps, section \ref{fields-section-splitting-fieds}.
Chaque $\beta_i$ est entier sur $R_0$.
Puisque chaque $a_i$ est un polynôme homogène en $\beta_1, \ldots, \beta_m$,
nous en déduisons la même propriété pour les $a_i$
(utiliser le lemme \ref{lemma-integral-closure-is-ring}). Cela démontre (1).

\medskip\noindent
Soit $R$ comme dans (2). Choisissons $c_0, \ldots, c_{m - n - 1} \in K$ tels que
$$
\begin{matrix}
x^m + b_{m - 1} x^{m - 1} + \ldots + b_0 =  \\
(x^n + a_{n - 1}x^{n - 1} + \ldots + a_0)
(x^{m - n} + c_{m - n - 1}x^{m - n - 1}+ \ldots + c_0).
\end{matrix}
$$
Cette équation implique
\begin{align*}
c_{m - n - 1} & = b_{m - 1} - a_{n - 1}, \\
c_{m - n - 2} & = b_{m - 2} - a_{n - 2} - a_{n - 1}c_{m - n - 1}, \\
\ldots
\end{align*}
Ainsi, $c_j \in R$ pour tout $j$. En quotientant par le radical
$\sqrt{(b_0, \ldots, b_{m - 1})}$, nous obtenons un anneau réduit $\overline{R}$.
Nous devons montrer que les images $\overline{a}_i \in \overline{R}$
sont nulles. Et, dans
$\overline{R}[x]$, nous avons la relation
$$
\begin{matrix}
x^m = x^m + \overline{b}_{m - 1} x^{m - 1} + \ldots + \overline{b}_0 = \\
(x^n + \overline{a}_{n - 1}x^{n - 1} + \ldots + \overline{a}_0)
(x^{m - n} + \overline{c}_{m - n - 1}x^{m - n - 1}+ \ldots + \overline{c}_0).
\end{matrix}
$$
Il est facile de voir que cela implique $\overline{a}_i = 0$ pour tout $i$. En effet,
d'après le lemme \ref{lemma-minimal-prime-reduced-ring}, la localisation de
$\overline{R}$ en un idéal premier minimal $\mathfrak{p}$ est un corps et
$\overline{R}_{\mathfrak p}[x]$ est un anneau factoriel. Ainsi,
$f = x^n + \sum \overline{a}_i x^i$
est associé à $x^n$ et, puisque $f$ est unitaire, $f = x^n$
dans $\overline{R}_{\mathfrak p}[x]$.
Il existe alors un $s \in \overline{R}$, $s \not\in \mathfrak p$,
tel que $s(f - x^n) = 0$. Par conséquent, tous les $\overline{a}_i$ appartiennent
à $\mathfrak p$, et nous concluons par le
lemme \ref{lemma-reduced-ring-sub-product-fields}.
\end{proof}
```

</details>

### 07 — lemma-minimal-polynomial-normal-domain

Anglais L8498–8516 ; français L8478–8496.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8498) · FR-ALGEBRA-B12-CHOICE-0007.

Anneaux intègres, corps des fractions et polynôme minimal gardent leurs rôles distincts. La normalité de R ramène les coefficients, déjà dans Frac(R) et entiers sur R, à R. Le corps de définition du polynôme est précisé dans la preuve anglaise et française, pas ajouté à l'énoncé. La preuve source reste gouvernante.

Règles : FR-ALGEBRA-B12-RULE-INTEGRAL, FR-ALGEBRA-B12-RULE-NORMAL, FR-ALGEBRA-B12-RULE-PROOF.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-minimal-polynomial-normal-domain}
Let $R \subset S$ be an inclusion of domains.
Assume $R$ is normal. Let $g \in S$ be integral
over $R$. Then the minimal polynomial of $g$
has coefficients in $R$.
\end{lemma}

\begin{proof}
Let $P = x^m + b_{m-1} x^{m-1} + \ldots + b_0$
be a polynomial with coefficients in $R$
such that $P(g) = 0$. Let $Q = x^n + a_{n-1}x^{n-1} + \ldots + a_0$
be the minimal polynomial for $g$ over the fraction field
$K$ of $R$. Then $Q$ divides $P$ in $K[x]$. By Lemma
\ref{lemma-polynomials-divide} we see the $a_i$ are
integral over $R$. Since $R$ is normal this
means they are in $R$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-minimal-polynomial-normal-domain}
Soit $R \subset S$ une inclusion d'anneaux intègres.
Supposons que $R$ soit normal. Soit $g \in S$ entier
sur $R$. Alors le polynôme minimal de $g$
est à coefficients dans $R$.
\end{lemma}

\begin{proof}
Soit $P = x^m + b_{m-1} x^{m-1} + \ldots + b_0$
un polynôme à coefficients dans $R$
tel que $P(g) = 0$. Soit $Q = x^n + a_{n-1}x^{n-1} + \ldots + a_0$
le polynôme minimal de $g$ sur le corps des fractions
$K$ de $R$. Alors $Q$ divise $P$ dans $K[x]$. D'après le lemme
\ref{lemma-polynomials-divide}, nous voyons que les $a_i$ sont
entiers sur $R$. Puisque $R$ est normal, cela
signifie qu'ils appartiennent à $R$.
\end{proof}
```

</details>

### 08 — proposition-going-down-normal-integral

Anglais L8517–8586 ; français L8497–8566.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8517) · FR-ALGEBRA-B12-CHOICE-0008.

Le premier supérieur q′ est fixé, puis on cherche q⊂q′ au-dessus du premier inférieur p. On conserve la localisation en q′, l'intersection avec R et l'ordre des quantificateurs. Deux lacunes du calcul anglais restent visibles et sont expliquées séparément : signe devant la somme et cas z=0 dans le changement de polynôme minimal. Ni l'une ni l'autre ne justifie une correction silencieuse du français.

Point particulier à relire : Deux observations source, pas deux corrections intégrées : signe manquant et cas z=0. Le résultat de descente n'est pas déclaré faux.

Règles : FR-ALGEBRA-B12-RULE-INTEGRAL, FR-ALGEBRA-B12-RULE-NORMAL, FR-ALGEBRA-B12-RULE-FINITE, FR-ALGEBRA-B12-RULE-PROOF, FR-ALGEBRA-B12-RULE-DESCENT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{proposition}
\label{proposition-going-down-normal-integral}
Let $R \subset S$ be an inclusion of domains.
Assume $R$ is normal and $S$ integral over $R$.
Let $\mathfrak p \subset \mathfrak p' \subset R$
be primes. Let $\mathfrak q'$ be a prime of $S$
with $\mathfrak p' = R \cap \mathfrak q'$.
Then there exists a prime $\mathfrak q$
with $\mathfrak q \subset \mathfrak q'$
such that $\mathfrak p = R \cap \mathfrak q$. In other words:
the going down property holds for $R \to S$, see
Definition \ref{definition-going-up-down}.
\end{proposition}

\begin{proof}
Let $\mathfrak p$, $\mathfrak p'$ and $\mathfrak q'$
be as in the statement. We have to show there is a prime
$\mathfrak q$, with $\mathfrak q \subset \mathfrak q'$ and
$R \cap \mathfrak q = \mathfrak p$. This is the same
as finding a prime of
$S_{\mathfrak q'}$ mapping to $\mathfrak p$.
According to Lemma \ref{lemma-in-image} we have to show
that $\mathfrak p S_{\mathfrak q'} \cap R
= \mathfrak p$. Pick $z \in \mathfrak p S_{\mathfrak q'} \cap R$.
We may write $z = y/g$ with $y \in \mathfrak pS$ and
$g \in S$, $g \not\in \mathfrak q'$. Written
differently we have $zg = y$.

\medskip\noindent
By Lemma \ref{lemma-integral-integral-over-ideal}
there exists a monic polynomial
$P = x^m + b_{m-1} x^{m-1} + \ldots + b_0$
with $b_i \in \mathfrak p$ such that $P(y) = 0$.

\medskip\noindent
By Lemma \ref{lemma-minimal-polynomial-normal-domain}
the minimal polynomial of $g$ over $K$ has coefficients
in $R$. Write it as $Q = x^n + a_{n-1} x^{n-1} + \ldots
+ a_0$. Note that not all $a_i$, $i = n-1, \ldots, 0$
are in $\mathfrak p$ since that would imply
$g^n = \sum_{j < n} a_j g^j \in \mathfrak pS
\subset \mathfrak p'S
\subset \mathfrak q'$
which is a contradiction.

\medskip\noindent
Since $y = zg$ we see immediately from the above
that $Q' = x^n + za_{n-1} x^{n-1} + \ldots + z^{n}a_0$
is the minimal polynomial for $y$. Hence
$Q'$ divides $P$ and by Lemma \ref{lemma-polynomials-divide}
we see that $z^ja_{n - j} \in \sqrt{(b_0, \ldots, b_{m-1})}
\subset \mathfrak p$, $j =  1, \ldots, n$.
Because not all $a_i$, $i = n-1, \ldots, 0$
are in $\mathfrak p$ we conclude $z \in \mathfrak p$
as desired.
\end{proof}
```

Français restauré :
```tex
\begin{proposition}
\label{proposition-going-down-normal-integral}
Soit $R \subset S$ une inclusion d'anneaux intègres.
Supposons que $R$ soit normal et que $S$ soit entier sur $R$.
Soient $\mathfrak p \subset \mathfrak p' \subset R$
des idéaux premiers. Soit $\mathfrak q'$ un idéal premier de $S$
tel que $\mathfrak p' = R \cap \mathfrak q'$.
Alors il existe un idéal premier $\mathfrak q$
tel que $\mathfrak q \subset \mathfrak q'$
et $\mathfrak p = R \cap \mathfrak q$. Autrement dit,
la propriété de descente est satisfaite pour $R \to S$, voir la
définition \ref{definition-going-up-down}.
\end{proposition}

\begin{proof}
Soient $\mathfrak p$, $\mathfrak p'$ et $\mathfrak q'$
comme dans l'énoncé. Nous devons montrer qu'il existe un idéal premier
$\mathfrak q$, avec $\mathfrak q \subset \mathfrak q'$ et
$R \cap \mathfrak q = \mathfrak p$. Cela revient
à trouver un idéal premier de
$S_{\mathfrak q'}$ qui s'envoie sur $\mathfrak p$.
D'après le lemme \ref{lemma-in-image}, nous devons montrer
que $\mathfrak p S_{\mathfrak q'} \cap R
= \mathfrak p$. Choisissons $z \in \mathfrak p S_{\mathfrak q'} \cap R$.
Nous pouvons écrire $z = y/g$ avec $y \in \mathfrak pS$ et
$g \in S$, $g \not\in \mathfrak q'$. Autrement dit,
nous avons $zg = y$.

\medskip\noindent
D'après le lemme \ref{lemma-integral-integral-over-ideal},
il existe un polynôme unitaire
$P = x^m + b_{m-1} x^{m-1} + \ldots + b_0$
avec $b_i \in \mathfrak p$ tel que $P(y) = 0$.

\medskip\noindent
D'après le lemme \ref{lemma-minimal-polynomial-normal-domain},
le polynôme minimal de $g$ sur $K$ est à coefficients
dans $R$. Écrivons-le $Q = x^n + a_{n-1} x^{n-1} + \ldots
+ a_0$. Remarquons que les $a_i$, $i = n-1, \ldots, 0$,
n'appartiennent pas tous à $\mathfrak p$, car cela impliquerait que
$g^n = \sum_{j < n} a_j g^j \in \mathfrak pS
\subset \mathfrak p'S
\subset \mathfrak q'$,
ce qui est une contradiction.

\medskip\noindent
Puisque $y = zg$, ce qui précède montre immédiatement
que $Q' = x^n + za_{n-1} x^{n-1} + \ldots + z^{n}a_0$
est le polynôme minimal de $y$. Ainsi,
$Q'$ divise $P$ et, d'après le lemme \ref{lemma-polynomials-divide},
nous voyons que $z^ja_{n - j} \in \sqrt{(b_0, \ldots, b_{m-1})}
\subset \mathfrak p$, $j =  1, \ldots, n$.
Puisque les $a_i$, $i = n-1, \ldots, 0$,
n'appartiennent pas tous à $\mathfrak p$, nous concluons que $z \in \mathfrak p$,
comme voulu.
\end{proof}
```

</details>

### 09 — section-flat

Anglais L8587–8619 ; français L8567–8599.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8587) · FR-ALGEBRA-B12-CHOICE-0009.

Exact à droite, exact à gauche, produit tensoriel et commute aux colimites sont attestés dans Ducros 2.4.14–17. Les deux propriétés préliminaires sont distinguées de la platitude ; aucun produit tensoriel arbitraire n'est déclaré exact à gauche. Les anneaux et la portée quelconque de M restent identiques.

Règles : FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-FILTERED, FR-ALGEBRA-B12-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Flat modules and flat ring maps}
\label{section-flat}

\noindent
One often used result is that if $M = \colim_{i\in \mathcal{I}} M_i$
is a colimit of $R$-modules and if $N$ is an $R$-module then
$$
M \otimes N
=
\colim_{i\in \mathcal{I}} M_i \otimes_R N,
$$
see Lemma \ref{lemma-tensor-products-commute-with-limits}.
This property is usually expressed by saying
that {\it $\otimes$ commutes with colimits}.
Another often used result is that if $0 \to N_1 \to N_2 \to N_3 \to 0$
is an exact sequence and if $M$ is any $R$-module, then
$$
M \otimes_R N_1
\to
M \otimes_R N_2
\to
M \otimes_R N_3
\to
0
$$
is still exact, see Lemma \ref{lemma-tensor-product-exact}.
Both of these properties tell us that the functor
$N \mapsto M \otimes_R N$ {\it is right exact}.
See Categories, Section \ref{categories-section-exact-functor}
and Homology, Section \ref{homology-section-functors}.
An $R$-module $M$ is flat if $N \mapsto N \otimes_R M$ is also left exact,
i.e., if it is exact. Here is the precise definition.
```

Français restauré :
```tex
\section{Modules plats et morphismes d'anneaux plats}
\label{section-flat}

\noindent
Un résultat souvent utilisé est le suivant : si $M = \colim_{i\in \mathcal{I}} M_i$
est une colimite de $R$-modules et si $N$ est un $R$-module, alors
$$
M \otimes N
=
\colim_{i\in \mathcal{I}} M_i \otimes_R N,
$$
voir le lemme \ref{lemma-tensor-products-commute-with-limits}.
On exprime habituellement cette propriété en disant
que {\it $\otimes$ commute aux colimites}.
Un autre résultat souvent utilisé est le suivant : si $0 \to N_1 \to N_2 \to N_3 \to 0$
est une suite exacte et si $M$ est un $R$-module quelconque, alors
$$
M \otimes_R N_1
\to
M \otimes_R N_2
\to
M \otimes_R N_3
\to
0
$$
est encore exacte, voir le lemme \ref{lemma-tensor-product-exact}.
Ces deux propriétés nous disent que le foncteur
$N \mapsto M \otimes_R N$ {\it est exact à droite}.
Voir Catégories, section \ref{categories-section-exact-functor},
et Homologie, section \ref{homology-section-functors}.
Un $R$-module $M$ est plat si $N \mapsto N \otimes_R M$ est aussi exact à gauche,
c'est-à-dire s'il est exact. Voici la définition précise.
```

</details>

### 10 — definition-flat

Anglais L8620–8642 ; français L8600–8622.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8620) · FR-ALGEBRA-B12-CHOICE-0010.

Plat et fidèlement plat sont attestés chez Dat 1.2.7. L'équivalence avant/après tensorisation caractérise la fidèle platitude, plus forte que la seule conservation des suites exactes. Dat la formule par exactitude et détection des objets nuls ; la traduction garde la formulation de Stacks, sans remplacer la définition. Les morphismes sont qualifiés via S comme R-module.

Règles : FR-ALGEBRA-B12-RULE-FLAT, FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-FINITE, FR-ALGEBRA-B12-RULE-PROOF.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-flat}
Let $R$ be a ring.
\begin{enumerate}
\item An $R$-module $M$ is called {\it flat} if whenever
$N_1 \to N_2 \to N_3$ is an exact sequence of $R$-modules
the sequence $M \otimes_R N_1 \to M \otimes_R N_2 \to M \otimes_R N_3$
is exact as well.
\item An $R$-module $M$ is called {\it faithfully flat} if the
complex of $R$-modules
$N_1 \to N_2 \to N_3$ is exact if and only if
the sequence $M \otimes_R N_1 \to M \otimes_R N_2 \to M \otimes_R N_3$
is exact.
\item A ring map $R \to S$ is called {\it flat} if
$S$ is flat as an $R$-module.
\item A ring map $R \to S$ is called {\it faithfully flat} if
$S$ is faithfully flat as an $R$-module.
\end{enumerate}
\end{definition}

\noindent
Here is an example of how you can use the flatness condition.
```

Français restauré :
```tex
\begin{definition}
\label{definition-flat}
Soit $R$ un anneau.
\begin{enumerate}
\item Un $R$-module $M$ est dit {\it plat} si, chaque fois que
$N_1 \to N_2 \to N_3$ est une suite exacte de $R$-modules,
la suite $M \otimes_R N_1 \to M \otimes_R N_2 \to M \otimes_R N_3$
est également exacte.
\item Un $R$-module $M$ est dit {\it fidèlement plat} si le
complexe de $R$-modules
$N_1 \to N_2 \to N_3$ est exact si et seulement si
la suite $M \otimes_R N_1 \to M \otimes_R N_2 \to M \otimes_R N_3$
est exacte.
\item Un morphisme d'anneaux $R \to S$ est dit {\it plat} si
$S$ est plat comme $R$-module.
\item Un morphisme d'anneaux $R \to S$ est dit {\it fidèlement plat} si
$S$ est fidèlement plat comme $R$-module.
\end{enumerate}
\end{definition}

\noindent
Voici un exemple d'utilisation de la condition de platitude.
```

</details>

### 11 — lemma-flat-intersect-ideals

Anglais L8643–8658 ; français L8623–8638.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8643) · FR-ALGEBRA-B12-CHOICE-0011.

L'intersection concerne deux idéaux et leurs images dans le module, pas une famille infinie. La tensorisation de la suite exacte fournit l'injection ; le noyau de la flèche vers les deux quotients identifie ensuite IM∩JM. Tensoriser par est compatible avec le registre de produit tensoriel lu chez Ducros ; la preuve source est intégralement conservée.

Règles : FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-TENSOR, FR-ALGEBRA-B12-RULE-COHOMOLOGY.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-flat-intersect-ideals}
Let $R$ be a ring. Let $I, J \subset R$ be ideals. Let $M$ be a flat
$R$-module. Then $IM \cap JM = (I \cap J)M$.
\end{lemma}

\begin{proof}
Consider the exact sequence $0 \to I \cap J \to R \to R/I \oplus R/J$.
Tensoring with the flat module $M$ we obtain an exact sequence
$$
0 \to (I \cap J) \otimes_R M \to M \to M/IM \oplus M/JM
$$
Since the kernel of $M \to M/IM \oplus M/JM$ is equal to
$IM \cap JM$ we conclude.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-flat-intersect-ideals}
Soit $R$ un anneau. Soient $I, J \subset R$ des idéaux. Soit $M$ un
$R$-module plat. Alors $IM \cap JM = (I \cap J)M$.
\end{lemma}

\begin{proof}
Considérons la suite exacte $0 \to I \cap J \to R \to R/I \oplus R/J$.
En tensorisant par le module plat $M$, nous obtenons une suite exacte
$$
0 \to (I \cap J) \otimes_R M \to M \to M/IM \oplus M/JM
$$
Puisque le noyau de $M \to M/IM \oplus M/JM$ est égal à
$IM \cap JM$, nous concluons.
\end{proof}
```

</details>

### 12 — lemma-colimit-flat

Anglais L8659–8670 ; français L8639–8650.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8659) · FR-ALGEBRA-B12-CHOICE-0012.

Système filtrant conserve directed ; le texte n'affirme pas l'exactitude de toutes les colimites. La commutation du produit tensoriel et l'exactitude des colimites filtrantes jouent des rôles différents. Le registre colimites filtrantes figure aussi dans Dat p.11, sans que cette page soit prétendue prouver ce lemme.

Règles : FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-FILTERED.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-colimit-flat}
Let $R$ be a ring. Let $\{M_i, \varphi_{ii'}\}$ be a directed system of
flat $R$-modules. Then $\colim_i M_i$ is a flat $R$-module.
\end{lemma}

\begin{proof}
This follows as $\otimes$ commutes with colimits and because
directed colimits are exact, see
Lemma \ref{lemma-directed-colimit-exact}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-colimit-flat}
Soit $R$ un anneau. Soit $\{M_i, \varphi_{ii'}\}$ un système filtrant de
$R$-modules plats. Alors $\colim_i M_i$ est un $R$-module plat.
\end{lemma}

\begin{proof}
Cela résulte du fait que $\otimes$ commute aux colimites et que
les colimites filtrantes sont exactes, voir le
lemme \ref{lemma-directed-colimit-exact}.
\end{proof}
```

</details>

### 13 — lemma-composition-flat

Anglais L8671–8706 ; français L8651–8686.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8671) · FR-ALGEBRA-B12-CHOICE-0013.

Composée s'accorde au féminin, alors que les morphismes restent plats. Les trois bases R, R′ et R′ pour M′ sont suivies dans tous les produits tensoriels. La preuve de la fidèle platitude remonte les équivalences, et ne déduit pas la fidélité de la seule platitude. Les deux renvois et les isomorphismes fonctoriels sont conservés.

Règles : FR-ALGEBRA-B12-RULE-FLAT, FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-PROOF.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-composition-flat}
A composition of (faithfully) flat ring maps is
(faithfully) flat.
If $R \to R'$ is (faithfully) flat, and $M'$ is a
(faithfully) flat $R'$-module, then $M'$ is a
(faithfully) flat $R$-module.
\end{lemma}

\begin{proof}
The first statement of the lemma is a particular case of the
second, so it is clearly enough to prove the latter. Let
$R \to R'$ be a flat ring map, and $M'$ a flat $R'$-module.
We need to prove that $M'$ is a flat $R$-module. Let
$N_1 \to N_2 \to N_3$ be an exact complex of $R$-modules.
Then, the complex $R' \otimes_R N_1 \to
R' \otimes_R N_2 \to R' \otimes_R N_3$ is exact (since $R'$
is flat as an $R$-module), and so the complex
$M' \otimes_{R'} \left(R' \otimes_R N_1\right)
\to M' \otimes_{R'} \left(R' \otimes_R N_2\right)
\to M' \otimes_{R'} \left(R' \otimes_R N_3\right)$ is
exact (since $M'$ is a flat $R'$-module). Since
$M' \otimes_{R'} \left(R' \otimes_R N\right)
\cong \left(M' \otimes_{R'} R'\right) \otimes_R N
\cong M' \otimes_R N$ for any $R$-module $N$ functorially
(by Lemmas \ref{lemma-tensor-with-bimodule} and
\ref{lemma-flip-tensor-product}), this complex is isomorphic
to the complex
$M' \otimes_R N_1 \to M' \otimes_R N_2 \to M' \otimes_R N_3$,
which is therefore also exact. This shows that $M'$ is a flat
$R$-module. Tracing this argument backwards, we can show
that if $R \to R'$ is faithfully flat, and if $M'$ is
faithfully flat as an $R'$-module, then $M'$ is faithfully
flat as an $R$-module.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-composition-flat}
Une composée de morphismes d'anneaux (fidèlement) plats est
(fidèlement) plate.
Si $R \to R'$ est (fidèlement) plat et si $M'$ est un
$R'$-module (fidèlement) plat, alors $M'$ est un
$R$-module (fidèlement) plat.
\end{lemma}

\begin{proof}
La première assertion du lemme est un cas particulier de la
seconde, de sorte qu'il suffit clairement de démontrer cette dernière. Soit
$R \to R'$ un morphisme d'anneaux plat et soit $M'$ un $R'$-module plat.
Nous devons démontrer que $M'$ est un $R$-module plat. Soit
$N_1 \to N_2 \to N_3$ un complexe exact de $R$-modules.
Alors le complexe $R' \otimes_R N_1 \to
R' \otimes_R N_2 \to R' \otimes_R N_3$ est exact (puisque $R'$
est plat comme $R$-module), et le complexe
$M' \otimes_{R'} \left(R' \otimes_R N_1\right)
\to M' \otimes_{R'} \left(R' \otimes_R N_2\right)
\to M' \otimes_{R'} \left(R' \otimes_R N_3\right)$ est donc
exact (puisque $M'$ est un $R'$-module plat). Comme
$M' \otimes_{R'} \left(R' \otimes_R N\right)
\cong \left(M' \otimes_{R'} R'\right) \otimes_R N
\cong M' \otimes_R N$ pour tout $R$-module $N$, fonctoriellement
(d'après les lemmes \ref{lemma-tensor-with-bimodule} et
\ref{lemma-flip-tensor-product}), ce complexe est isomorphe
au complexe
$M' \otimes_R N_1 \to M' \otimes_R N_2 \to M' \otimes_R N_3$,
qui est donc lui aussi exact. Cela montre que $M'$ est un
$R$-module plat. En remontant cet argument, nous pouvons montrer
que, si $R \to R'$ est fidèlement plat et si $M'$ est
fidèlement plat comme $R'$-module, alors $M'$ est fidèlement
plat comme $R$-module.
\end{proof}
```

</details>

### 14 — lemma-flat

Anglais L8707–8855 ; français L8687–8835.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8707) · FR-ALGEBRA-B12-CHOICE-0014.

Lecture de toute la longue preuve et des deux notes. Fini devient de type fini pour K, N et leurs sous-modules, sans cardinalité finie ni noethérianité ajoutée. Les quatre critères restent distincts ; les deux reductions à des modules de type fini précèdent la récurrence sur le rang libre. Les numéros des flèches sont vérifiés dans la première note. La seconde contient une flèche officielle inversée, maintenue et signalée séparément ; on ne la corrige pas sous couvert de traduction.

Point particulier à relire : La flèche L′⊗M→L⊗M de la seconde note est celle imprimée dans l'autorité ; le sens attendu est expliqué hors traduction.

Règles : FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-TENSOR, FR-ALGEBRA-B12-RULE-FILTERED, FR-ALGEBRA-B12-RULE-FINITE, FR-ALGEBRA-B12-RULE-PROOF.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-flat}
Let $M$ be an $R$-module. The following are equivalent:
\begin{enumerate}
\item
\label{item-flat}
$M$ is flat over $R$.
\item
\label{item-injective}
for every injection of $R$-modules $N \subset N'$
the map $N \otimes_R M \to N'\otimes_R M$ is injective.
\item
\label{item-f-ideal}
for every ideal $I \subset R$ the map
$I \otimes_R M \to R \otimes_R M = M$ is injective.
\item
\label{item-ffg-ideal}
for every finitely generated ideal $I \subset R$
the map $I \otimes_R M \to R \otimes_R M = M$ is injective.
\end{enumerate}
\end{lemma}

\begin{proof}
The implications (\ref{item-flat}) implies (\ref{item-injective})
implies (\ref{item-f-ideal}) implies (\ref{item-ffg-ideal}) are all
trivial. Thus we prove (\ref{item-ffg-ideal}) implies (\ref{item-flat}).
Suppose that $N_1 \to N_2 \to N_3$ is exact.
Let $K = \Ker(N_2 \to N_3)$ and $Q = \Im(N_2 \to N_3)$.
Then we get maps
$$
N_1 \otimes_R M \to
K \otimes_R M \to
N_2 \otimes_R M \to
Q \otimes_R M \to
N_3 \otimes_R M
$$
Observe that the first and third arrows are surjective. Thus if we show
that the second and fourth arrows are injective, then we are
done\footnote{Here is the argument in more detail:
Assume that we know that the second and fourth arrows are
injective. Lemma \ref{lemma-tensor-product-exact} (applied
to the exact sequence $K \to N_2 \to Q \to 0$) yields that
the sequence $K \otimes_R M \to N_2 \otimes_R M \to
Q \otimes_R M \to 0$ is exact. Hence,
$\Ker \left(N_2 \otimes_R M \to Q \otimes_R M\right)
= \Im \left(K \otimes_R M \to N_2 \otimes_R M\right)$.
Since
$\Im \left(K \otimes_R M \to N_2 \otimes_R M\right)
= \Im \left(N_1 \otimes_R M \to N_2 \otimes_R M\right)$
(due to the surjectivity of $N_1 \otimes_R M \to
K \otimes_R M$) and
$\Ker \left(N_2 \otimes_R M \to Q \otimes_R M\right)
= \Ker \left(N_2 \otimes_R M \to N_3 \otimes_R M\right)$
(due to the injectivity of $Q \otimes_R M \to
N_3 \otimes_R M$), this becomes
$\Ker \left(N_2 \otimes_R M \to N_3 \otimes_R M\right)
= \Im \left(N_1 \otimes_R M \to N_2 \otimes_R M\right)$,
which shows that the functor $- \otimes_R M$ is exact,
whence $M$ is flat.}.
Hence it suffices to show that $- \otimes_R M$ transforms
injective $R$-module maps into injective $R$-module maps.

\medskip\noindent
Assume $K \to N$ is an injective $R$-module map and
let $x \in \Ker(K \otimes_R M \to N \otimes_R M)$.
We have to show that $x$ is zero.
The $R$-module $K$ is the union of its finite
$R$-submodules; hence, $K \otimes_R M$ is
the colimit of $R$-modules of the form
$K_i \otimes_R M$ where $K_i$ runs over all finite
$R$-submodules of $K$
(because tensor product commutes with colimits).
Thus, for some $i$ our $x$ comes from an element
$x_i \in K_i \otimes_R M$. Thus we may assume that $K$
is a finite $R$-module. Assume this. We regard the
injection $K \to N$ as an inclusion, so that
$K \subset N$.

\medskip\noindent
The $R$-module $N$ is the union of its finite
$R$-submodules that contain $K$. Hence, $N \otimes_R M$
is the colimit of $R$-modules of the form
$N_i \otimes_R M$ where $N_i$ runs over all finite
$R$-submodules of $N$ that contain $K$
(again since tensor product commutes with colimits).
Notice that this is a colimit over a directed system
(since the sum of two finite submodules of $N$ is
again finite).
Hence, (by Lemma \ref{lemma-zero-directed-limit})
the element $x \in K \otimes_R M$ maps to
zero in at least one of these $R$-modules
$N_i \otimes_R M$ (since $x$ maps to zero
in $N \otimes_R M$).
Thus we may assume $N$ is a finite $R$-module.

\medskip\noindent
Assume $N$ is a finite $R$-module. Write $N = R^{\oplus n}/L$ and $K = L'/L$
for some $L \subset L' \subset R^{\oplus n}$.
For any $R$-submodule $G \subset R^{\oplus n}$,
we have a canonical map $G \otimes_R M \to M^{\oplus n}$
obtained by composing
$G \otimes_R M \to R^n \otimes_R M = M^{\oplus n}$.
It suffices to prove that $L \otimes_R M \to M^{\oplus n}$
and $L' \otimes_R M \to M^{\oplus n}$ are injective.
Namely, if so, then we see that
$K \otimes_R M = L' \otimes_R M/L \otimes_R M \to M^{\oplus n}/L \otimes_R M$
is injective too\footnote{This becomes obvious if we
identify $L' \otimes_R M$ and $L \otimes_R M$ with
submodules of $M^{\oplus n}$ (which is legitimate since
the maps $L \otimes_R M \to M^{\oplus n}$
and $L' \otimes_R M \to M^{\oplus n}$ are injective and
commute with the obvious map $L' \otimes_R M \to L \otimes_R M$).}.

\medskip\noindent
Thus it suffices to show that $L \otimes_R M \to M^{\oplus n}$
is injective when $L \subset R^{\oplus n}$ is an $R$-submodule.
We do this by induction on $n$. The base case $n = 1$ we handle below.
For the induction step assume $n > 1$ and set
$L' = L \cap R \oplus 0^{\oplus n - 1}$. Then $L'' = L/L'$ is a submodule
of $R^{\oplus n - 1}$. We obtain a diagram
$$
\xymatrix{
&
L' \otimes_R M \ar[r] \ar[d] &
L \otimes_R M \ar[r] \ar[d] &
L'' \otimes_R M \ar[r] \ar[d] &
0 \\
0 \ar[r] &
M \ar[r] &
M^{\oplus n} \ar[r] &
M^{\oplus n - 1} \ar[r] & 0
}
$$
By induction hypothesis and the base case the left and right vertical
arrows are injective. The rows are exact. It follows that the middle vertical
arrow is injective too.

\medskip\noindent
The base case of the induction above is when $L \subset R$ is an ideal.
In other words, we have to show that $I \otimes_R M \to M$ is injective
for any ideal $I$ of $R$. We know this is true when $I$ is finitely
generated. However, $I = \bigcup I_\alpha$ is the union of the
finitely generated ideals $I_\alpha$ contained in it. In other words,
$I = \colim I_\alpha$. Since $\otimes$ commutes with colimits we see that
$I \otimes_R M = \colim I_\alpha \otimes_R M$ and since all
the morphisms $I_\alpha \otimes_R M \to M$ are injective by
assumption, the same is true for $I \otimes_R M \to M$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-flat}
Soit $M$ un $R$-module. Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item
\label{item-flat}
$M$ est plat sur $R$.
\item
\label{item-injective}
pour toute injection de $R$-modules $N \subset N'$,
l'application $N \otimes_R M \to N'\otimes_R M$ est injective.
\item
\label{item-f-ideal}
pour tout idéal $I \subset R$, l'application
$I \otimes_R M \to R \otimes_R M = M$ est injective.
\item
\label{item-ffg-ideal}
pour tout idéal de type fini $I \subset R$,
l'application $I \otimes_R M \to R \otimes_R M = M$ est injective.
\end{enumerate}
\end{lemma}

\begin{proof}
Les implications successives de (\ref{item-flat}) à (\ref{item-injective}), puis
à (\ref{item-f-ideal}) et à (\ref{item-ffg-ideal}), sont immédiates. Nous démontrons
donc que (\ref{item-ffg-ideal}) implique (\ref{item-flat}).
Supposons que $N_1 \to N_2 \to N_3$ soit exacte.
Posons $K = \Ker(N_2 \to N_3)$ et $Q = \Im(N_2 \to N_3)$.
Nous obtenons alors des applications
$$
N_1 \otimes_R M \to
K \otimes_R M \to
N_2 \otimes_R M \to
Q \otimes_R M \to
N_3 \otimes_R M
$$
Remarquons que les première et troisième flèches sont surjectives. Ainsi, si nous montrons
que les deuxième et quatrième flèches sont injectives, nous aurons
conclu\footnote{Voici l'argument plus en détail :
supposons que nous sachions que les deuxième et quatrième flèches sont
injectives. Le lemme \ref{lemma-tensor-product-exact} (appliqué
à la suite exacte $K \to N_2 \to Q \to 0$) donne que
la suite $K \otimes_R M \to N_2 \otimes_R M \to
Q \otimes_R M \to 0$ est exacte. Par conséquent,
$\Ker \left(N_2 \otimes_R M \to Q \otimes_R M\right)
= \Im \left(K \otimes_R M \to N_2 \otimes_R M\right)$.
Comme
$\Im \left(K \otimes_R M \to N_2 \otimes_R M\right)
= \Im \left(N_1 \otimes_R M \to N_2 \otimes_R M\right)$
(en raison de la surjectivité de $N_1 \otimes_R M \to
K \otimes_R M$) et
$\Ker \left(N_2 \otimes_R M \to Q \otimes_R M\right)
= \Ker \left(N_2 \otimes_R M \to N_3 \otimes_R M\right)$
(en raison de l'injectivité de $Q \otimes_R M \to
N_3 \otimes_R M$), cela devient
$\Ker \left(N_2 \otimes_R M \to N_3 \otimes_R M\right)
= \Im \left(N_1 \otimes_R M \to N_2 \otimes_R M\right)$,
ce qui montre que le foncteur $- \otimes_R M$ est exact,
et donc que $M$ est plat.}.
Il suffit donc de montrer que $- \otimes_R M$ transforme
les applications injectives de $R$-modules en applications injectives de $R$-modules.

\medskip\noindent
Supposons que $K \to N$ soit une application injective de $R$-modules et
soit $x \in \Ker(K \otimes_R M \to N \otimes_R M)$.
Nous devons montrer que $x$ est nul.
Le $R$-module $K$ est la réunion de ses
$R$-sous-modules de type fini ; par conséquent, $K \otimes_R M$ est
la colimite des $R$-modules de la forme
$K_i \otimes_R M$, où $K_i$ parcourt tous les
$R$-sous-modules de type fini de $K$
(car le produit tensoriel commute aux colimites).
Ainsi, pour un certain $i$, notre $x$ provient d'un élément
$x_i \in K_i \otimes_R M$. Nous pouvons donc supposer que $K$
est un $R$-module de type fini. Faisons cette hypothèse. Nous considérons
l'injection $K \to N$ comme une inclusion, de sorte que
$K \subset N$.

\medskip\noindent
Le $R$-module $N$ est la réunion de ses
$R$-sous-modules de type fini qui contiennent $K$. Par conséquent, $N \otimes_R M$
est la colimite des $R$-modules de la forme
$N_i \otimes_R M$, où $N_i$ parcourt tous les
$R$-sous-modules de type fini de $N$ qui contiennent $K$
(de nouveau parce que le produit tensoriel commute aux colimites).
Remarquons qu'il s'agit d'une colimite sur un système filtrant
(puisque la somme de deux sous-modules de type fini de $N$ est
encore de type fini).
Par conséquent, (d'après le lemme \ref{lemma-zero-directed-limit}),
l'élément $x \in K \otimes_R M$ s'envoie sur
zéro dans au moins un de ces $R$-modules
$N_i \otimes_R M$ (puisque $x$ s'envoie sur zéro
dans $N \otimes_R M$).
Nous pouvons donc supposer que $N$ est un $R$-module de type fini.

\medskip\noindent
Supposons $N$ de type fini sur $R$. Écrivons $N = R^{\oplus n}/L$ et $K = L'/L$
pour certains $L \subset L' \subset R^{\oplus n}$.
Pour tout $R$-sous-module $G \subset R^{\oplus n}$,
nous disposons d'une application canonique $G \otimes_R M \to M^{\oplus n}$
obtenue en composant
$G \otimes_R M \to R^n \otimes_R M = M^{\oplus n}$.
Il suffit de prouver que $L \otimes_R M \to M^{\oplus n}$
et $L' \otimes_R M \to M^{\oplus n}$ sont injectives.
En effet, si tel est le cas, nous voyons que
$K \otimes_R M = L' \otimes_R M/L \otimes_R M \to M^{\oplus n}/L \otimes_R M$
est elle aussi injective\footnote{Cela devient évident si nous
identifions $L' \otimes_R M$ et $L \otimes_R M$ à des
sous-modules de $M^{\oplus n}$ (ce qui est légitime puisque
les applications $L \otimes_R M \to M^{\oplus n}$
et $L' \otimes_R M \to M^{\oplus n}$ sont injectives et
commutent avec l'application évidente $L' \otimes_R M \to L \otimes_R M$).}.

\medskip\noindent
Il suffit donc de montrer que $L \otimes_R M \to M^{\oplus n}$
est injective lorsque $L \subset R^{\oplus n}$ est un $R$-sous-module.
Nous le faisons par récurrence sur $n$. Nous traitons ci-dessous le cas initial $n = 1$.
Pour l'étape de récurrence, supposons $n > 1$ et posons
$L' = L \cap R \oplus 0^{\oplus n - 1}$. Alors $L'' = L/L'$ est un sous-module
de $R^{\oplus n - 1}$. Nous obtenons un diagramme
$$
\xymatrix{
&
L' \otimes_R M \ar[r] \ar[d] &
L \otimes_R M \ar[r] \ar[d] &
L'' \otimes_R M \ar[r] \ar[d] &
0 \\
0 \ar[r] &
M \ar[r] &
M^{\oplus n} \ar[r] &
M^{\oplus n - 1} \ar[r] & 0
}
$$
D'après l'hypothèse de récurrence et le cas initial, les flèches verticales
de gauche et de droite sont injectives. Les lignes sont exactes. Il s'ensuit que la flèche verticale
du milieu est elle aussi injective.

\medskip\noindent
Le cas initial de la récurrence ci-dessus est celui où $L \subset R$ est un idéal.
Autrement dit, nous devons montrer que $I \otimes_R M \to M$ est injective
pour tout idéal $I$ de $R$. Nous savons que cela est vrai lorsque $I$ est de type
fini. Toutefois, $I = \bigcup I_\alpha$ est la réunion des
idéaux de type fini $I_\alpha$ qu'il contient. Autrement dit,
$I = \colim I_\alpha$. Puisque $\otimes$ commute aux colimites, nous voyons que
$I \otimes_R M = \colim I_\alpha \otimes_R M$ et, puisque toutes
les applications $I_\alpha \otimes_R M \to M$ sont injectives par
hypothèse, il en va de même de $I \otimes_R M \to M$.
\end{proof}
```

</details>

### 15 — lemma-colimit-rings-flat

Anglais L8856–8887 ; français L8836–8867.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8856) · FR-ALGEBRA-B12-CHOICE-0015.

Les anneaux de base varient avec i. φii′-linéaire n'est donc pas remplacé par linéaire sur un anneau fixe. Les données finies de l'idéal descendent à un stade, puis les applications injectives passent à la colimite filtrante. Aucune injectivité des transitions des Ri n'est postulée ; le cas constant des Mi reste le premier cas particulier.

Règles : FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-FILTERED, FR-ALGEBRA-B12-RULE-FINITE, FR-ALGEBRA-B12-RULE-PROOF.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-colimit-rings-flat}
Let $\{R_i, \varphi_{ii'}\}$ be a system of rings over the directed set $I$.
Let $R = \colim_i R_i$.
\begin{enumerate}
\item If $M$ is an $R$-module such that $M$ is flat as an $R_i$-module
for all $i$, then $M$ is flat as an $R$-module.
\item For $i \in I$ let $M_i$ be a flat $R_i$-module and
for $i' \geq i$ let $f_{ii'} : M_i \to M_{i'}$ be a $\varphi_{ii'}$-linear
map such that $f_{i' i''} \circ f_{i i'} = f_{i i''}$. Then
$M = \colim_{i \in I} M_i$ is a flat $R$-module.
\end{enumerate}
\end{lemma}

\begin{proof}
Part (1) is a special case of part (2) with $M_i = M$ for all $i$
and $f_{i i'} = \text{id}_M$. Proof of (2).
Let $\mathfrak a \subset R$ be a finitely generated ideal. By
Lemma \ref{lemma-flat}
it suffices to show that $\mathfrak a \otimes_R M \to M$ is
injective. We can find an $i \in I$ and a finitely generated ideal
$\mathfrak a' \subset R_i$ such that $\mathfrak a = \mathfrak a'R$.
Then $\mathfrak a = \colim_{i' \geq i} \mathfrak a'R_{i'}$.
Since $\otimes$ commutes with colimits the map $\mathfrak a \otimes_R M \to M$
is the colimit of the maps
$$
\mathfrak a'R_{i'} \otimes_{R_{i'}} M_{i'} \longrightarrow M_{i'}
$$
These maps are all injective by assumption. Since colimits over $I$
are exact by Lemma \ref{lemma-directed-colimit-exact} we win.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-colimit-rings-flat}
Soit $\{R_i, \varphi_{ii'}\}$ un système d'anneaux sur l'ensemble filtrant $I$.
Soit $R = \colim_i R_i$.
\begin{enumerate}
\item Si $M$ est un $R$-module tel que $M$ soit plat comme $R_i$-module
pour tout $i$, alors $M$ est plat comme $R$-module.
\item Pour $i \in I$, soit $M_i$ un $R_i$-module plat et,
pour $i' \geq i$, soit $f_{ii'} : M_i \to M_{i'}$ une application
$\varphi_{ii'}$-linéaire telle que $f_{i' i''} \circ f_{i i'} = f_{i i''}$.
Alors $M = \colim_{i \in I} M_i$ est un $R$-module plat.
\end{enumerate}
\end{lemma}

\begin{proof}
La partie (1) est un cas particulier de la partie (2), avec $M_i = M$ pour tout $i$
et $f_{i i'} = \text{id}_M$. Démontrons (2).
Soit $\mathfrak a \subset R$ un idéal de type fini. D'après le
lemme \ref{lemma-flat},
il suffit de montrer que $\mathfrak a \otimes_R M \to M$ est
injective. Nous pouvons trouver $i \in I$ et un idéal de type fini
$\mathfrak a' \subset R_i$ tels que $\mathfrak a = \mathfrak a'R$.
Alors $\mathfrak a = \colim_{i' \geq i} \mathfrak a'R_{i'}$.
Puisque $\otimes$ commute aux colimites, l'application
$\mathfrak a \otimes_R M \to M$ est la colimite des applications
$$
\mathfrak a'R_{i'} \otimes_{R_{i'}} M_{i'} \longrightarrow M_{i'}
$$
Toutes ces applications sont injectives par hypothèse. Puisque les colimites sur $I$
sont exactes d'après le lemme \ref{lemma-directed-colimit-exact}, nous concluons.
\end{proof}
```

</details>

### 16 — lemma-flat-base-change

Anglais L8888–8901 ; français L8868–8881.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8888) · FR-ALGEBRA-B12-CHOICE-0016.

Le changement de base R→R′ est quelconque ; c'est M qui est supposé (fidèlement) plat. Les N testés sont des R′-modules. L'isomorphisme de tensorisation transporte exactitude et réflexion de l'exactitude, sans imposer que R′ soit fidèlement plat sur R.

Règles : FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-PROOF.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-flat-base-change}
Suppose that $M$ is (faithfully) flat over $R$, and that $R \to R'$
is a ring map. Then $M \otimes_R R'$ is (faithfully) flat over $R'$.
\end{lemma}

\begin{proof}
For any $R'$-module $N$ we have a canonical
isomorphism $N \otimes_{R'} (R'\otimes_R M)
= N \otimes_R M$. Hence the desired exactness properties of the functor
$-\otimes_{R'}(R'\otimes_R M)$ follow from
the corresponding exactness properties of the functor $-\otimes_R M$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-flat-base-change}
Supposons que $M$ soit (fidèlement) plat sur $R$ et que $R \to R'$
soit un morphisme d'anneaux. Alors $M \otimes_R R'$ est (fidèlement) plat sur $R'$.
\end{lemma}

\begin{proof}
Pour tout $R'$-module $N$, nous avons un
isomorphisme canonique $N \otimes_{R'} (R'\otimes_R M)
= N \otimes_R M$. Les propriétés d'exactitude voulues du foncteur
$-\otimes_{R'}(R'\otimes_R M)$ résultent donc
des propriétés d'exactitude correspondantes du foncteur $-\otimes_R M$.
\end{proof}
```

</details>

### 17 — lemma-flatness-descends

Anglais L8902–8928 ; français L8882–8908.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8902) · FR-ALGEBRA-B12-CHOICE-0017.

La fidèle platitude de R→R′ sert dans la dernière implication, alors que la platitude suffit pour conserver la première suite exacte. La conclusion sur M′ porte sur R′, pas sur R. Le mot descente est ici vérifié par l'équivalence de propriétés après changement de base, distincte du going down des premiers.

Règles : FR-ALGEBRA-B12-RULE-FLAT, FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-PROOF.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-flatness-descends}
Let $R \to R'$ be a faithfully flat ring map.
Let $M$ be a module over $R$, and set $M' = R' \otimes_R M$.
Then $M$ is flat over $R$ if and only if $M'$ is flat over $R'$.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-flat-base-change} we see that if $M$ is flat
then $M'$ is flat. For the converse, suppose that $M'$ is flat.
Let $N_1 \to N_2 \to N_3$ be an exact sequence of $R$-modules.
We want to show that $N_1 \otimes_R M \to N_2 \otimes_R M \to N_3 \otimes_R M$
is exact. We know that
$N_1 \otimes_R R' \to N_2 \otimes_R R' \to N_3 \otimes_R R'$ is
exact, because $R \to R'$ is flat. Flatness of $M'$ implies that
$N_1 \otimes_R R' \otimes_{R'} M'
\to N_2 \otimes_R R' \otimes_{R'} M'
\to N_3 \otimes_R R' \otimes_{R'} M'$ is exact.
We may write this as
$N_1 \otimes_R M \otimes_R R'
\to N_2 \otimes_R M \otimes_R R'
\to N_3 \otimes_R M \otimes_R R'$.
Finally, faithful flatness implies that
$N_1 \otimes_R M \to N_2 \otimes_R M \to N_3 \otimes_R M$
is exact.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-flatness-descends}
Soit $R \to R'$ un morphisme d'anneaux fidèlement plat.
Soit $M$ un module sur $R$, et posons $M' = R' \otimes_R M$.
Alors $M$ est plat sur $R$ si et seulement si $M'$ est plat sur $R'$.
\end{lemma}

\begin{proof}
D'après le lemme \ref{lemma-flat-base-change}, si $M$ est plat,
alors $M'$ est plat. Réciproquement, supposons $M'$ plat.
Soit $N_1 \to N_2 \to N_3$ une suite exacte de $R$-modules.
Nous voulons montrer que $N_1 \otimes_R M \to N_2 \otimes_R M \to N_3 \otimes_R M$
est exacte. Nous savons que
$N_1 \otimes_R R' \to N_2 \otimes_R R' \to N_3 \otimes_R R'$ est
exacte, car $R \to R'$ est plat. La platitude de $M'$ implique que
$N_1 \otimes_R R' \otimes_{R'} M'
\to N_2 \otimes_R R' \otimes_{R'} M'
\to N_3 \otimes_R R' \otimes_{R'} M'$ est exacte.
Nous pouvons l'écrire
$N_1 \otimes_R M \otimes_R R'
\to N_2 \otimes_R M \otimes_R R'
\to N_3 \otimes_R M \otimes_R R'$.
Enfin, la fidèle platitude implique que
$N_1 \otimes_R M \to N_2 \otimes_R M \to N_3 \otimes_R M$
est exacte.
\end{proof}
```

</details>

### 18 — lemma-flatness-descends-more-general

Anglais L8929–8956 ; français L8909–8936.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8929) · FR-ALGEBRA-B12-CHOICE-0018.

S→S′ est un morphisme plat de R-algèbres ; M est un S-module, mais les conclusions visent la platitude sur R. La tensorisation du noyau se fait sur S. Cette distinction est conservée dans chacune des deux assertions et dans la preuve, sans intervertir les anneaux de base.

Règles : FR-ALGEBRA-B12-RULE-FLAT, FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-PROOF.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-flatness-descends-more-general}
Let $R$ be a ring. Let $S \to S'$ be a flat map of $R$-algebras.
Let $M$ be a module over $S$, and set $M' = S' \otimes_S M$.
\begin{enumerate}
\item If $M$ is flat over $R$, then $M'$ is flat over $R$.
\item If $S \to S'$ is faithfully flat, then $M$ is flat
over $R$ if and only if $M'$ is flat over $R$.
\end{enumerate}
\end{lemma}

\begin{proof}
Let $N \to N'$ be an injection of $R$-modules. By the flatness
of $S \to S'$ we have
$$
\Ker(N \otimes_R M \to N' \otimes_R M) \otimes_S S'
=
\Ker(N \otimes_R M' \to N' \otimes_R M')
$$
If $M$ is flat over $R$, then the left hand side is zero and
we find that $M'$ is flat over $R$ by the second characterization
of flatness in Lemma \ref{lemma-flat}.
If $M'$ is flat over $R$ then we have the vanishing of the right hand side
and if in addition $S \to S'$ is faithfully flat, this implies that
$\Ker(N \otimes_R M \to N' \otimes_R M)$ is zero which in turn
shows that $M$ is flat over $R$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-flatness-descends-more-general}
Soit $R$ un anneau. Soit $S \to S'$ un morphisme plat de $R$-algèbres.
Soit $M$ un module sur $S$, et posons $M' = S' \otimes_S M$.
\begin{enumerate}
\item Si $M$ est plat sur $R$, alors $M'$ est plat sur $R$.
\item Si $S \to S'$ est fidèlement plat, alors $M$ est plat
sur $R$ si et seulement si $M'$ est plat sur $R$.
\end{enumerate}
\end{lemma}

\begin{proof}
Soit $N \to N'$ une injection de $R$-modules. Par la platitude
de $S \to S'$, nous avons
$$
\Ker(N \otimes_R M \to N' \otimes_R M) \otimes_S S'
=
\Ker(N \otimes_R M' \to N' \otimes_R M')
$$
Si $M$ est plat sur $R$, alors le membre de gauche est nul et
nous trouvons que $M'$ est plat sur $R$ par la deuxième caractérisation
de la platitude dans le lemme \ref{lemma-flat}.
Si $M'$ est plat sur $R$, le membre de droite est nul et, si
en outre $S \to S'$ est fidèlement plat, cela implique que
$\Ker(N \otimes_R M \to N' \otimes_R M)$ est nul, ce qui
montre à son tour que $M$ est plat sur $R$.
\end{proof}
```

</details>

### 19 — lemma-flat-permanence

Anglais L8957–8993 ; français L8937–8973.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8957) · FR-ALGEBRA-B12-CHOICE-0019.

La fidèle platitude de M sur S permet de réfléchir l'exactitude de la suite tensorisée par S ; sa platitude sur R ne suffit pas seule. Le passage suivant définit relation triviale par factorisation finie avec des relations sur les coefficients. Triviale ne signifie pas que tous les xi sont nuls. Le mot and dans la formule est traduit par et, et c'est la seule exception linguistique exacte des formules de ce lot.

Règles : FR-ALGEBRA-B12-RULE-INTEGRAL, FR-ALGEBRA-B12-RULE-FLAT, FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-PROOF.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-flat-permanence}
Let $R \to S$ be a ring map. Let $M$ be an $S$-module.
If $M$ is flat as an $R$-module and faithfully flat as an $S$-module,
then $R \to S$ is flat.
\end{lemma}

\begin{proof}
Let $N_1 \to N_2 \to N_3$ be an exact sequence of $R$-modules.
By assumption $N_1 \otimes_R M \to N_2 \otimes_R M \to N_3 \otimes_R M$
is exact. We may write this as
$$
N_1 \otimes_R S \otimes_S M
\to
N_2 \otimes_R S \otimes_S M
\to
N_3 \otimes_R S \otimes_S M.
$$
By faithful flatness of $M$ over $S$ we conclude that
$N_1 \otimes_R S \to N_2 \otimes_R S \to N_3 \otimes_R S$ is exact.
Hence $R \to S$ is flat.
\end{proof}

\noindent
Let $R$ be a ring.
Let $M$ be an $R$-module.
Let $\sum f_i x_i = 0$ be a relation in $M$.
We say the relation $\sum f_i x_i$
is {\it trivial} if there exist an integer $m \geq 0$,
elements $y_j \in M$, $j = 1, \ldots, m$, and elements $a_{ij} \in R$,
$i = 1, \ldots, n$, $j = 1, \ldots, m$ such that
$$
x_i = \sum\nolimits_j a_{ij} y_j, \forall i,
\quad\text{and}\quad
0 = \sum\nolimits_i f_ia_{ij}, \forall j.
$$
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-flat-permanence}
Soit $R \to S$ un morphisme d'anneaux. Soit $M$ un $S$-module.
Si $M$ est plat comme $R$-module et fidèlement plat comme $S$-module,
alors $R \to S$ est plat.
\end{lemma}

\begin{proof}
Soit $N_1 \to N_2 \to N_3$ une suite exacte de $R$-modules.
Par hypothèse, $N_1 \otimes_R M \to N_2 \otimes_R M \to N_3 \otimes_R M$
est exacte. Nous pouvons l'écrire
$$
N_1 \otimes_R S \otimes_S M
\to
N_2 \otimes_R S \otimes_S M
\to
N_3 \otimes_R S \otimes_S M.
$$
Par fidèle platitude de $M$ sur $S$, nous concluons que
$N_1 \otimes_R S \to N_2 \otimes_R S \to N_3 \otimes_R S$ est exacte.
Ainsi $R \to S$ est plat.
\end{proof}

\noindent
Soit $R$ un anneau.
Soit $M$ un $R$-module.
Soit $\sum f_i x_i = 0$ une relation dans $M$.
Nous disons que la relation $\sum f_i x_i$
est {\it triviale} s'il existe un entier $m \geq 0$,
des éléments $y_j \in M$, $j = 1, \ldots, m$, et des éléments $a_{ij} \in R$,
$i = 1, \ldots, n$, $j = 1, \ldots, m$, tels que
$$
x_i = \sum\nolimits_j a_{ij} y_j, \forall i,
\quad\text{et}\quad
0 = \sum\nolimits_i f_ia_{ij}, \forall j.
$$
```

</details>

### 20 — lemma-flat-eq

Anglais L8994–9035 ; français L8974–9015.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8994) · FR-ALGEBRA-B12-CHOICE-0020.

Critère équationnel de platitude est attesté comme intitulé sur la page d'enseignement de Bailleul. Son PDF lié est en anglais, donc non invoqué comme attestation de prose française. La preuve garde K noyau de R^n→I, les éléments relevés de K⊗M et le calcul tensoriel final. Toute relation triviale renvoie à la définition précédente ; aucun sens familier du mot triviale n'est importé.

Point particulier à relire : L'attestation française extérieure porte seulement sur l'intitulé. Le PDF associé est anglais ; ne pas lui attribuer une prose française inexistante.

Règles : FR-ALGEBRA-B12-RULE-FLAT, FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-FINITE, FR-ALGEBRA-B12-RULE-CRITERION, FR-ALGEBRA-B12-RULE-PROOF, FR-ALGEBRA-B12-RULE-COHOMOLOGY.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}[Equational criterion of flatness]
\label{lemma-flat-eq}
A module $M$ over $R$ is flat if and only if
every relation in $M$ is trivial.
\end{lemma}

\begin{proof}
Assume $M$ is flat and let $\sum f_i x_i = 0$ be a relation in $M$.
Let $I = (f_1, \ldots, f_n)$, and let
$K = \Ker(R^n \to I, (a_1, \ldots, a_n) \mapsto \sum_i a_i f_i)$.
So we have the short exact sequence
$0 \to K \to R^n \to I \to 0$. Then $\sum f_i \otimes x_i$
is an element of $I \otimes_R M$ which maps
to zero in $R \otimes_R M = M$. By flatness
$\sum f_i \otimes x_i$ is zero in $I \otimes_R M$.
Thus there exists an element of $K \otimes_R M$ mapping
to $\sum e_i \otimes x_i \in R^n \otimes_R M$ where $e_i$
is the $i$th basis element of $R^n$.
Write this element as $\sum k_j \otimes y_j$
and then write the image of $k_j$ in $R^n$ as
$\sum a_{ij} e_i$ to get the result.

\medskip\noindent
Assume every relation is trivial, let $I$
be a finitely generated ideal, and let $x = \sum f_i \otimes x_i$
be an element of $I \otimes_R M$ mapping to zero in $R \otimes_R M = M$.
This just means exactly that $\sum f_i x_i$ is a relation in
$M$. And the fact that it is trivial implies easily that
$x$ is zero, because
$$
x
=
\sum f_i \otimes x_i
=
\sum f_i \otimes \left(\sum a_{ij}y_j\right)
=
\sum \left(\sum f_i a_{ij}\right) \otimes y_j
=
0
$$
\end{proof}
```

Français restauré :
```tex
\begin{lemma}[Critère équationnel de platitude]
\label{lemma-flat-eq}
Un module $M$ sur $R$ est plat si et seulement si
toute relation dans $M$ est triviale.
\end{lemma}

\begin{proof}
Supposons $M$ plat et soit $\sum f_i x_i = 0$ une relation dans $M$.
Posons $I = (f_1, \ldots, f_n)$ et
$K = \Ker(R^n \to I, (a_1, \ldots, a_n) \mapsto \sum_i a_i f_i)$.
Nous avons donc la suite exacte courte
$0 \to K \to R^n \to I \to 0$. Alors $\sum f_i \otimes x_i$
est un élément de $I \otimes_R M$ qui s'envoie
sur zéro dans $R \otimes_R M = M$. Par platitude,
$\sum f_i \otimes x_i$ est nul dans $I \otimes_R M$.
Il existe donc un élément de $K \otimes_R M$ dont l'image
est $\sum e_i \otimes x_i \in R^n \otimes_R M$, où $e_i$
est le $i$-ième vecteur de base de $R^n$.
Écrivons cet élément sous la forme $\sum k_j \otimes y_j$,
puis l'image de $k_j$ dans $R^n$ sous la forme
$\sum a_{ij} e_i$, ce qui donne le résultat.

\medskip\noindent
Supposons toute relation triviale, soit $I$
un idéal de type fini, et soit $x = \sum f_i \otimes x_i$
un élément de $I \otimes_R M$ qui s'envoie sur zéro dans $R \otimes_R M = M$.
Cela signifie exactement que $\sum f_i x_i$ est une relation dans
$M$. Le fait qu'elle soit triviale implique aisément que
$x$ est nul, car
$$
x
=
\sum f_i \otimes x_i
=
\sum f_i \otimes \left(\sum a_{ij}y_j\right)
=
\sum \left(\sum f_i a_{ij}\right) \otimes y_j
=
0
$$
\end{proof}
```

</details>

### 21 — lemma-flat-tor-zero

Anglais L9036–9069 ; français L9016–9049.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L9036) · FR-ALGEBRA-B12-CHOICE-0021.

La platitude porte sur le quotient M de la suite courte, non sur N ni nécessairement sur M′ ou M″. L'injectivité à gauche après tensorisation est la conclusion. Le diagramme distingue R^(I), somme directe libre, d'un produit ; son orientation et les lignes exactes restent inchangées. Lemme du serpent est un choix disciplinaire motivé par la source, sans nouvelle attestation exacte dans les pages consultées.

Règles : FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-TENSOR, FR-ALGEBRA-B12-RULE-PROOF, FR-ALGEBRA-B12-RULE-COHOMOLOGY.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-flat-tor-zero}
Suppose that $R$ is a ring, $0 \to M'' \to M' \to M \to 0$
a short exact sequence, and $N$ an $R$-module. If $M$ is flat
then $N \otimes_R M'' \to N \otimes_R M'$ is injective, i.e., the
sequence
$$
0 \to N \otimes_R M'' \to N \otimes_R M' \to N \otimes_R M \to 0
$$
is a short exact sequence.
\end{lemma}

\begin{proof}
Let $R^{(I)} \to N$ be a surjection from a free module
onto $N$ with kernel $K$. The result follows
from the snake lemma applied to the following diagram
$$
\begin{matrix}
 & & 0 & & 0 & & 0 & & \\
 & & \uparrow & & \uparrow & & \uparrow & & \\
 & & M''\otimes_R N & \to & M' \otimes_R N & \to & M \otimes_R N & \to & 0 \\
 & & \uparrow & & \uparrow & & \uparrow & & \\
0 & \to & (M'')^{(I)} & \to & (M')^{(I)} & \to & M^{(I)} & \to & 0 \\
 & & \uparrow & & \uparrow & & \uparrow & & \\
 & & M''\otimes_R K & \to & M' \otimes_R K & \to & M \otimes_R K & \to & 0 \\
 & & & & & & \uparrow & & \\
 & & & & & & 0 & &
\end{matrix}
$$
with exact rows and columns. The middle row is exact because tensoring
with the free module $R^{(I)}$ is exact.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-flat-tor-zero}
Supposons que $R$ soit un anneau, que $0 \to M'' \to M' \to M \to 0$
soit une suite exacte courte et que $N$ soit un $R$-module. Si $M$ est plat,
alors $N \otimes_R M'' \to N \otimes_R M'$ est injective, c'est-à-dire que la
suite
$$
0 \to N \otimes_R M'' \to N \otimes_R M' \to N \otimes_R M \to 0
$$
est une suite exacte courte.
\end{lemma}

\begin{proof}
Soit $R^{(I)} \to N$ une surjection d'un module libre
sur $N$, de noyau $K$. Le résultat découle
du lemme du serpent appliqué au diagramme suivant
$$
\begin{matrix}
 & & 0 & & 0 & & 0 & & \\
 & & \uparrow & & \uparrow & & \uparrow & & \\
 & & M''\otimes_R N & \to & M' \otimes_R N & \to & M \otimes_R N & \to & 0 \\
 & & \uparrow & & \uparrow & & \uparrow & & \\
0 & \to & (M'')^{(I)} & \to & (M')^{(I)} & \to & M^{(I)} & \to & 0 \\
 & & \uparrow & & \uparrow & & \uparrow & & \\
 & & M''\otimes_R K & \to & M' \otimes_R K & \to & M \otimes_R K & \to & 0 \\
 & & & & & & \uparrow & & \\
 & & & & & & 0 & &
\end{matrix}
$$
dont les lignes et les colonnes sont exactes. La ligne du milieu est exacte car tensoriser
par le module libre $R^{(I)}$ est exact.
\end{proof}
```

</details>

### 22 — lemma-flat-ses

Anglais L9070–9095 ; français L9050–9075.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L9070) · FR-ALGEBRA-B12-CHOICE-0022.

Les deux stabilités sont conservées : extensions de modules plats, puis noyau d'une surjection entre plats. On ne leur substitue pas une assertion fausse sur le quotient de deux plats. Dans la seconde implication, l'injectivité de la flèche inférieure gauche provient du quotient M″ plat et du lemme précédent.

Règles : FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-PROOF.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-flat-ses}
Suppose that $0 \to M' \to M \to M'' \to 0$ is
a short exact sequence of $R$-modules.
If $M'$ and $M''$ are flat so is $M$.
If $M$ and $M''$ are flat so is $M'$.
\end{lemma}

\begin{proof}
We will use the criterion that a module $N$ is flat if for
every ideal $I \subset R$ the map $N \otimes_R I \to N$ is injective,
see Lemma \ref{lemma-flat}.
Consider an ideal $I \subset R$.
Consider the diagram
$$
\begin{matrix}
0 & \to & M' & \to & M & \to & M'' & \to & 0 \\
& & \uparrow & & \uparrow & & \uparrow & & \\
& & M'\otimes_R I & \to & M \otimes_R I & \to & M''\otimes_R I & \to & 0
\end{matrix}
$$
with exact rows. This immediately proves the first assertion.
The second follows because if $M''$ is flat then the lower left
horizontal arrow is injective by Lemma \ref{lemma-flat-tor-zero}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-flat-ses}
Supposons que $0 \to M' \to M \to M'' \to 0$ soit
une suite exacte courte de $R$-modules.
Si $M'$ et $M''$ sont plats, alors $M$ l'est aussi.
Si $M$ et $M''$ sont plats, alors $M'$ l'est aussi.
\end{lemma}

\begin{proof}
Nous utiliserons le critère suivant : un module $N$ est plat si, pour
tout idéal $I \subset R$, l'application $N \otimes_R I \to N$ est injective ;
voir le lemme \ref{lemma-flat}.
Considérons un idéal $I \subset R$.
Considérons le diagramme
$$
\begin{matrix}
0 & \to & M' & \to & M & \to & M'' & \to & 0 \\
& & \uparrow & & \uparrow & & \uparrow & & \\
& & M'\otimes_R I & \to & M \otimes_R I & \to & M''\otimes_R I & \to & 0
\end{matrix}
$$
dont les lignes sont exactes. Cela démontre immédiatement la première assertion.
La seconde résulte du fait que, si $M''$ est plat, alors la flèche horizontale
inférieure gauche est injective d'après le lemme \ref{lemma-flat-tor-zero}.
\end{proof}
```

</details>

### 23 — lemma-easy-ff

Anglais L9096–9122 ; français L9076–9102.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L9096) · FR-ALGEBRA-B12-CHOICE-0023.

Les morphismes nuls sont détectés par tensorisation, et non toutes les applications non injectives. La réciproque teste la classe de x dans N2/Im(N1) au moyen de α:R→N2/Im(N1). L'expression anglaise complex −⊗M est reprise par complexe, même si elle désigne maladroitement le foncteur ou le complexe tensorisé ; le français ne prétend pas réparer cet abrégé de source.

Règles : FR-ALGEBRA-B12-RULE-FLAT, FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-TENSOR, FR-ALGEBRA-B12-RULE-PROOF, FR-ALGEBRA-B12-RULE-COHOMOLOGY.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-easy-ff}
Let $R$ be a ring.
Let $M$ be an $R$-module.
The following are equivalent
\begin{enumerate}
\item $M$ is faithfully flat, and
\item $M$ is flat and for all $R$-module homomorphisms $\alpha : N \to N'$
we have $\alpha = 0$ if and only if $\alpha \otimes \text{id}_M = 0$.
\end{enumerate}
\end{lemma}

\begin{proof}
If $M$ is faithfully flat, then
$0 \to \Ker(\alpha) \to N \to N'$ is exact if and only if the same holds
after tensoring with $M$. This proves (1) implies (2).
For the other, assume (2). Let $N_1 \to N_2 \to N_3$
be a complex, and assume the complex
$N_1 \otimes_R M \to N_2 \otimes_R M \to N_3\otimes_R M$
is exact. Take $x \in \Ker(N_2 \to N_3)$,
and consider the map $\alpha : R \to N_2/\Im(N_1)$,
$r \mapsto rx + \Im(N_1)$. By the exactness
of the complex $-\otimes_R M$ we see that $\alpha \otimes
\text{id}_M$ is zero. By assumption we get that $\alpha$ is
zero. Hence $x $ is in the image of $N_1 \to N_2$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-easy-ff}
Soit $R$ un anneau.
Soit $M$ un $R$-module.
Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item $M$ est fidèlement plat, et
\item $M$ est plat et, pour tous les homomorphismes de $R$-modules $\alpha : N \to N'$,
nous avons $\alpha = 0$ si et seulement si $\alpha \otimes \text{id}_M = 0$.
\end{enumerate}
\end{lemma}

\begin{proof}
Si $M$ est fidèlement plat, alors
$0 \to \Ker(\alpha) \to N \to N'$ est exacte si et seulement si elle le reste
après tensorisation par $M$. Cela démontre que (1) implique (2).
Réciproquement, supposons (2). Soit $N_1 \to N_2 \to N_3$
un complexe et supposons que le complexe
$N_1 \otimes_R M \to N_2 \otimes_R M \to N_3\otimes_R M$
soit exact. Prenons $x \in \Ker(N_2 \to N_3)$
et considérons l'application $\alpha : R \to N_2/\Im(N_1)$,
$r \mapsto rx + \Im(N_1)$. Par l'exactitude
du complexe $-\otimes_R M$, nous voyons que $\alpha \otimes
\text{id}_M$ est nulle. Par hypothèse, nous obtenons que $\alpha$ est
nulle. Ainsi $x $ appartient à l'image de $N_1 \to N_2$.
\end{proof}
```

</details>

### 24 — lemma-ff

Anglais L9123–9162 ; français L9103–9142.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L9123) · FR-ALGEBRA-B12-CHOICE-0024.

Fibres non nulles désigne M⊗κ(p), pas les localisés Mp. Le module M reste plat dans les quatre critères. La preuve passe de l'annulateur d'un élément de H à un idéal maximal pour conclure H=0. Homologie est remplacé par cohomologie, mot exact choisi par la source ; le quotient Ker/Im est inchangé. Les deux mots pourraient désigner ce quotient non gradué selon une convention, mais une traduction fidèle n'a aucune raison de changer la convention de l'auteur.

Point particulier à relire : Restauration de désignation cohomologie ; aucune modification du quotient, des degrés ou de la preuve.

Règles : FR-ALGEBRA-B12-RULE-FLAT, FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-TENSOR, FR-ALGEBRA-B12-RULE-PROOF, FR-ALGEBRA-B12-RULE-COHOMOLOGY.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ff}
\begin{slogan}
A flat module is faithfully flat if and only if it has nonzero fibers.
\end{slogan}
Let $M$ be a flat $R$-module.
The following are equivalent:
\begin{enumerate}
\item $M$ is faithfully flat,
\item for every nonzero $R$-module $N$, then tensor product $M \otimes_R N$
is nonzero,
\item for all $\mathfrak p \in \Spec(R)$
the tensor product $M \otimes_R \kappa(\mathfrak p)$ is nonzero, and
\item for all maximal ideals $\mathfrak m$ of $R$
the tensor product $M \otimes_R \kappa(\mathfrak m) = M/{\mathfrak m}M$
is nonzero.
\end{enumerate}
\end{lemma}

\begin{proof}
Assume $M$ faithfully flat and $N \not = 0$. By Lemma \ref{lemma-easy-ff}
the nonzero map $1 : N \to N$ induces a nonzero map
$M \otimes_R N \to M \otimes_R N$, so $M \otimes_R N \not = 0$.
Thus (1) implies (2). The implications (2) $\Rightarrow$ (3) $\Rightarrow$ (4)
are immediate.

\medskip\noindent
Assume (4). Suppose that $N_1 \to N_2 \to N_3$ is a complex and
suppose that $N_1 \otimes_R M \to N_2\otimes_R M \to
N_3\otimes_R M$ is exact. Let $H$ be the cohomology of the complex,
so $H = \Ker(N_2 \to N_3)/\Im(N_1 \to N_2)$. To finish the proof
we will show $H = 0$. By flatness we see that $H \otimes_R M = 0$.
Take $x \in H$ and let $I = \{f \in R \mid fx = 0 \}$
be its annihilator. Since $R/I \subset H$ we get
$M/IM \subset H \otimes_R M = 0$ by flatness of $M$.
If $I \not =  R$ we may choose
a maximal ideal $I \subset \mathfrak m \subset R$.
This immediately gives a contradiction.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ff}
\begin{slogan}
Un module plat est fidèlement plat si et seulement si ses fibres sont non nulles.
\end{slogan}
Soit $M$ un $R$-module plat.
Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item $M$ est fidèlement plat,
\item pour tout $R$-module non nul $N$, le produit tensoriel $M \otimes_R N$
est non nul,
\item pour tout $\mathfrak p \in \Spec(R)$,
le produit tensoriel $M \otimes_R \kappa(\mathfrak p)$ est non nul, et
\item pour tout idéal maximal $\mathfrak m$ de $R$,
le produit tensoriel $M \otimes_R \kappa(\mathfrak m) = M/{\mathfrak m}M$
est non nul.
\end{enumerate}
\end{lemma}

\begin{proof}
Supposons $M$ fidèlement plat et $N \not = 0$. D'après le lemme \ref{lemma-easy-ff},
l'application non nulle $1 : N \to N$ induit une application non nulle
$M \otimes_R N \to M \otimes_R N$, donc $M \otimes_R N \not = 0$.
Ainsi (1) implique (2). Les implications (2) $\Rightarrow$ (3) $\Rightarrow$ (4)
sont immédiates.

\medskip\noindent
Supposons (4). Supposons que $N_1 \to N_2 \to N_3$ soit un complexe et
que $N_1 \otimes_R M \to N_2\otimes_R M \to
N_3\otimes_R M$ soit exact. Soit $H$ la cohomologie du complexe,
donc $H = \Ker(N_2 \to N_3)/\Im(N_1 \to N_2)$. Pour achever la preuve,
nous allons montrer que $H = 0$. Par platitude, nous voyons que $H \otimes_R M = 0$.
Prenons $x \in H$ et soit $I = \{f \in R \mid fx = 0 \}$
son annulateur. Puisque $R/I \subset H$, nous obtenons
$M/IM \subset H \otimes_R M = 0$ par platitude de $M$.
Si $I \not =  R$, nous pouvons choisir
un idéal maximal $I \subset \mathfrak m \subset R$.
Cela donne immédiatement une contradiction.
\end{proof}
```

</details>

### 25 — lemma-ff-rings

Anglais L9163–9182 ; français L9143–9162.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L9163) · FR-ALGEBRA-B12-CHOICE-0025.

Dat p.10 atteste directement la même équivalence entre fidèle platitude et surjectivité spectrale pour un morphisme déjà plat. Point fermé signifie idéal maximal du spectre de R ; la troisième condition ne devient pas une surjectivité sur tous les points sans l'hypothèse de platitude. La preuve source par les corps résiduels est maintenue.

Règles : FR-ALGEBRA-B12-RULE-FLAT, FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-PROOF, FR-ALGEBRA-B12-RULE-COHOMOLOGY.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ff-rings}
Let $R \to S$ be a flat ring map.
The following are equivalent:
\begin{enumerate}
\item $R \to S$ is faithfully flat,
\item the induced map on $\Spec$ is surjective, and
\item any closed point $x \in \Spec(R)$ is
in the image of the map $\Spec(S) \to \Spec(R)$.
\end{enumerate}
\end{lemma}

\begin{proof}
This follows quickly from Lemma \ref{lemma-ff}, because we
saw in Remark \ref{remark-fundamental-diagram}
that $\mathfrak p$ is in the image
if and only if the ring $S \otimes_R \kappa(\mathfrak p)$
is nonzero.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ff-rings}
Soit $R \to S$ un morphisme d'anneaux plat.
Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item $R \to S$ est fidèlement plat,
\item l'application induite sur $\Spec$ est surjective, et
\item tout point fermé $x \in \Spec(R)$ appartient
à l'image de l'application $\Spec(S) \to \Spec(R)$.
\end{enumerate}
\end{lemma}

\begin{proof}
Cela résulte rapidement du lemme \ref{lemma-ff}, car nous
avons vu dans la remarque \ref{remark-fundamental-diagram}
que $\mathfrak p$ appartient à l'image
si et seulement si l'anneau $S \otimes_R \kappa(\mathfrak p)$
est non nul.
\end{proof}
```

</details>

### 26 — lemma-local-flat-ff

Anglais L9183–9194 ; français L9163–9174.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L9183) · FR-ALGEBRA-B12-CHOICE-0026.

Local qualifie le morphisme en plus des deux anneaux locaux ; le corollaire de Dat p.10 formule ces deux conditions séparément. Le qualificatif local ne doit pas être supprimé. La preuve immédiate reste celle de Stacks.

Règles : FR-ALGEBRA-B12-RULE-FLAT, FR-ALGEBRA-B12-RULE-LOCAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-local-flat-ff}
A flat local ring homomorphism of local rings is faithfully flat.
\end{lemma}

\begin{proof}
Immediate from Lemma \ref{lemma-ff-rings}.
\end{proof}

\noindent
Flatness meshes well with localization.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-local-flat-ff}
Un homomorphisme local plat d'anneaux locaux est fidèlement plat.
\end{lemma}

\begin{proof}
Cela résulte immédiatement du lemme \ref{lemma-ff-rings}.
\end{proof}

\noindent
La platitude se comporte bien avec la localisation.
```

</details>

### 27 — lemma-flat-localization

Anglais L9195–9263 ; français L9175–9243.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L9195) · FR-ALGEBRA-B12-CHOICE-0027.

Les sept critères distinguent localisations sur R et sur A. Les gi engendrent l'idéal unité de A, pas seulement un idéal non nul. Dans les deux derniers critères, p est la contraction d'un premier ou maximal de A, et n'est pas déclaré maximal de R. La preuve traite les morphismes comme A-linéaires puis leurs localisés ; les parties omises demeurent explicitement omises.

Règles : FR-ALGEBRA-B12-RULE-EXACT, FR-ALGEBRA-B12-RULE-TENSOR, FR-ALGEBRA-B12-RULE-LOCAL, FR-ALGEBRA-B12-RULE-PROOF, FR-ALGEBRA-B12-RULE-DESCENT, FR-ALGEBRA-B12-RULE-COHOMOLOGY.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-flat-localization}
Let $R$ be a ring. Let $S \subset R$ be a multiplicative subset.
\begin{enumerate}
\item The localization $S^{-1}R$ is a flat $R$-algebra.
\item If $M$ is an $S^{-1}R$-module, then $M$ is a flat $R$-module
if and only if $M$ is a flat $S^{-1}R$-module.
\item Suppose $M$ is an $R$-module. Then
$M$ is a flat $R$-module if and only if $M_{\mathfrak p}$ is a flat
$R_{\mathfrak p}$-module for all primes $\mathfrak p$ of $R$.
\item Suppose $M$ is an $R$-module. Then $M$ is a flat $R$-module if
and only if $M_{\mathfrak m}$ is a flat
$R_{\mathfrak m}$-module for all maximal ideals $\mathfrak m$ of $R$.
\item Suppose $R \to A$ is a ring map, $M$ is an $A$-module,
and $g_1, \ldots, g_m \in A$ are elements generating the unit
ideal of $A$. Then $M$ is flat over $R$ if and only if each localization
$M_{g_i}$ is flat over $R$.
\item Suppose $R \to A$ is a ring map, and $M$ is an $A$-module.
Then $M$ is a flat $R$-module if and only if the localization
$M_{\mathfrak q}$ is a flat $R_{\mathfrak p}$-module
(with $\mathfrak p$ the prime of $R$ lying under $\mathfrak q$)
for all primes $\mathfrak q$ of $A$.
\item Suppose $R \to A$ is a ring map, and $M$ is an $A$-module.
Then $M$ is a flat $R$-module if and only if the localization
$M_{\mathfrak m}$ is a flat $R_{\mathfrak p}$-module
(with $\mathfrak p = R \cap \mathfrak m$)
for all maximal ideals $\mathfrak m$ of $A$.
\end{enumerate}
\end{lemma}

\begin{proof}
Let us prove the last statement of the lemma.
In the proof we will use repeatedly that localization is exact
and commutes with tensor product, see Sections \ref{section-localization}
and \ref{section-tensor-product}.

\medskip\noindent
Suppose $R \to A$ is a ring map, and $M$ is an $A$-module.
Assume that $M_{\mathfrak m}$ is a flat $R_{\mathfrak p}$-module
for all maximal ideals $\mathfrak m$ of $A$ (with
$\mathfrak p = R \cap \mathfrak m$). Let $I \subset R$ be an ideal.
We have to show the map $I \otimes_R M \to M$ is injective.
We can think of this as a map of $A$-modules.
By assumption the localization
$(I \otimes_R M)_{\mathfrak m} \to M_{\mathfrak m}$ is injective
because
$(I \otimes_R M)_{\mathfrak m} =
I_{\mathfrak p} \otimes_{R_{\mathfrak p}} M_{\mathfrak m}$.
Hence the kernel of $I \otimes_R M \to M$ is zero by
Lemma \ref{lemma-characterize-zero-local}.
Hence $M$ is flat over $R$.

\medskip\noindent
Conversely, assume $M$ is flat over $R$. Pick a prime $\mathfrak q$
of $A$ lying over the prime $\mathfrak p$ of $R$. Suppose that
$I \subset R_{\mathfrak p}$ is an ideal. We have to show that
$I \otimes_{R_{\mathfrak p}} M_{\mathfrak q} \to M_{\mathfrak q}$
is injective. We can write $I = J_{\mathfrak p}$ for some
ideal $J \subset R$. Then the map
$I \otimes_{R_{\mathfrak p}} M_{\mathfrak q} \to M_{\mathfrak q}$
is just the localization (at $\mathfrak q$) of the map
$J \otimes_R M \to M$ which is injective. Since localization is exact
we see that $M_{\mathfrak q}$ is a flat $R_{\mathfrak p}$-module.

\medskip\noindent
This proves (7) and (6). The other statements follow in a straightforward
way from the last statement (proofs omitted).
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-flat-localization}
Soit $R$ un anneau. Soit $S \subset R$ une partie multiplicative.
\begin{enumerate}
\item La localisation $S^{-1}R$ est une $R$-algèbre plate.
\item Si $M$ est un $S^{-1}R$-module, alors $M$ est un $R$-module plat
si et seulement si $M$ est un $S^{-1}R$-module plat.
\item Supposons que $M$ soit un $R$-module. Alors
$M$ est un $R$-module plat si et seulement si $M_{\mathfrak p}$ est un
$R_{\mathfrak p}$-module plat pour tout idéal premier $\mathfrak p$ de $R$.
\item Supposons que $M$ soit un $R$-module. Alors $M$ est un $R$-module plat si
et seulement si $M_{\mathfrak m}$ est un
$R_{\mathfrak m}$-module plat pour tout idéal maximal $\mathfrak m$ de $R$.
\item Supposons que $R \to A$ soit un morphisme d'anneaux, que $M$ soit un $A$-module,
et que $g_1, \ldots, g_m \in A$ soient des éléments qui engendrent l'idéal
unité de $A$. Alors $M$ est plat sur $R$ si et seulement si chaque localisation
$M_{g_i}$ est plate sur $R$.
\item Supposons que $R \to A$ soit un morphisme d'anneaux et que $M$ soit un $A$-module.
Alors $M$ est un $R$-module plat si et seulement si la localisation
$M_{\mathfrak q}$ est un $R_{\mathfrak p}$-module plat
(où $\mathfrak p$ est l'idéal premier de $R$ situé sous $\mathfrak q$)
pour tout idéal premier $\mathfrak q$ de $A$.
\item Supposons que $R \to A$ soit un morphisme d'anneaux et que $M$ soit un $A$-module.
Alors $M$ est un $R$-module plat si et seulement si la localisation
$M_{\mathfrak m}$ est un $R_{\mathfrak p}$-module plat
(où $\mathfrak p = R \cap \mathfrak m$)
pour tout idéal maximal $\mathfrak m$ de $A$.
\end{enumerate}
\end{lemma}

\begin{proof}
Démontrons la dernière assertion du lemme.
Dans la preuve, nous utiliserons à plusieurs reprises le fait que la localisation est exacte
et commute au produit tensoriel, voir les sections \ref{section-localization}
et \ref{section-tensor-product}.

\medskip\noindent
Supposons que $R \to A$ soit un morphisme d'anneaux et que $M$ soit un $A$-module.
Supposons que $M_{\mathfrak m}$ soit un $R_{\mathfrak p}$-module plat
pour tout idéal maximal $\mathfrak m$ de $A$ (avec
$\mathfrak p = R \cap \mathfrak m$). Soit $I \subset R$ un idéal.
Nous devons montrer que l'application $I \otimes_R M \to M$ est injective.
Nous pouvons la considérer comme une application de $A$-modules.
Par hypothèse, la localisation
$(I \otimes_R M)_{\mathfrak m} \to M_{\mathfrak m}$ est injective
car
$(I \otimes_R M)_{\mathfrak m} =
I_{\mathfrak p} \otimes_{R_{\mathfrak p}} M_{\mathfrak m}$.
Ainsi, le noyau de $I \otimes_R M \to M$ est nul d'après le
lemme \ref{lemma-characterize-zero-local}.
Par conséquent, $M$ est plat sur $R$.

\medskip\noindent
Réciproquement, supposons $M$ plat sur $R$. Prenons un idéal premier
$\mathfrak q$ de $A$ situé au-dessus de l'idéal premier $\mathfrak p$ de $R$.
Supposons que $I \subset R_{\mathfrak p}$ soit un idéal. Nous devons montrer que
$I \otimes_{R_{\mathfrak p}} M_{\mathfrak q} \to M_{\mathfrak q}$
est injective. Nous pouvons écrire $I = J_{\mathfrak p}$ pour un certain
idéal $J \subset R$. Alors l'application
$I \otimes_{R_{\mathfrak p}} M_{\mathfrak q} \to M_{\mathfrak q}$
est simplement la localisation (en $\mathfrak q$) de l'application
$J \otimes_R M \to M$, qui est injective. Puisque la localisation est exacte,
nous voyons que $M_{\mathfrak q}$ est un $R_{\mathfrak p}$-module plat.

\medskip\noindent
Cela démontre (7) et (6). Les autres assertions résultent de manière immédiate
de la dernière assertion (preuves omises).
\end{proof}
```

</details>

### 28 — lemma-flat-going-down

Anglais L9264–9284 ; français L9244–9264.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L9264) · FR-ALGEBRA-B12-CHOICE-0028.

Deux occurrences de morphisme d'anneaux locaux sont précisées en morphisme local d'anneaux locaux pour rendre local ring map. Être entre anneaux locaux ne suffit pas en général : par exemple Z_(p)→Q n'est pas local au sens des idéaux maximaux. Ici la localisation en deux premiers correspondants produit bien un morphisme local, condition utilisée pour la fidèle platitude. Dat p.10 distingue expressément ce qualificatif. Aucun nouvel axiome n'est ajouté au théorème.

Point particulier à relire : Deux précisions de portée lexicale, justifiées par le qualificatif local explicite de l'anglais et par le corollaire français de Dat.

Règles : FR-ALGEBRA-B12-RULE-LOCAL, FR-ALGEBRA-B12-RULE-FINITE, FR-ALGEBRA-B12-RULE-PROOF, FR-ALGEBRA-B12-RULE-DESCENT, FR-ALGEBRA-B12-RULE-COHOMOLOGY.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-flat-going-down}
Let $R \to S$ be flat. Let $\mathfrak p \subset \mathfrak p'$
be primes of $R$. Let $\mathfrak q' \subset S$ be a prime of $S$
mapping to $\mathfrak p'$. Then there exists a prime
$\mathfrak q \subset \mathfrak q'$ mapping to $\mathfrak p$.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-flat-localization} the local ring map
$R_{\mathfrak p'} \to S_{\mathfrak q'}$ is flat.
By Lemma \ref{lemma-local-flat-ff} this local ring map is faithfully
flat. By Lemma \ref{lemma-ff-rings} there is a prime mapping to
$\mathfrak p R_{\mathfrak p'}$. The inverse image of this
prime in $S$ does the job.
\end{proof}

\noindent
The property of $R \to S$ described in the lemma is called the
``going down property''. See Definition \ref{definition-going-up-down}.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-flat-going-down}
Soit $R \to S$ plat. Soient $\mathfrak p \subset \mathfrak p'$
des idéaux premiers de $R$. Soit $\mathfrak q' \subset S$ un idéal premier de $S$
qui s'envoie sur $\mathfrak p'$. Alors il existe un idéal premier
$\mathfrak q \subset \mathfrak q'$ qui s'envoie sur $\mathfrak p$.
\end{lemma}

\begin{proof}
D'après le lemme \ref{lemma-flat-localization}, le morphisme local d'anneaux locaux
$R_{\mathfrak p'} \to S_{\mathfrak q'}$ est plat.
D'après le lemme \ref{lemma-local-flat-ff}, ce morphisme local d'anneaux locaux est fidèlement
plat. D'après le lemme \ref{lemma-ff-rings}, il existe un idéal premier qui s'envoie sur
$\mathfrak p R_{\mathfrak p'}$. L'image réciproque de cet
idéal premier dans $S$ convient.
\end{proof}

\noindent
La propriété de $R \to S$ décrite dans le lemme est appelée
« propriété de descente ». Voir la définition \ref{definition-going-up-down}.
```

</details>

### 29 — lemma-colimit-faithfully-flat

Anglais L9285–9306 ; français L9265–9286.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L9285) · FR-ALGEBRA-B12-CHOICE-0029.

La famille est filtrante et formée d'algèbres fidèlement plates. Après passage aux corps résiduels, 1≠0 subsiste dans la colimite d'anneaux unitaires non nuls : si 1 devenait nul, il le serait à un stade ultérieur. Cela ne serait pas un argument pour une colimite arbitraire de modules non nuls. Le texte garde sa preuve abrégée et ses références.

Règles : FR-ALGEBRA-B12-RULE-FLAT, FR-ALGEBRA-B12-RULE-FILTERED, FR-ALGEBRA-B12-RULE-COHOMOLOGY.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-colimit-faithfully-flat}
Let $R$ be a ring. Let $\{S_i, \varphi_{ii'}\}$ be a directed system of
faithfully flat $R$-algebras. Then $S = \colim_i S_i$ is a faithfully flat
$R$-algebra.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-colimit-flat} we see that $S$ is flat.
Let $\mathfrak m \subset R$ be a maximal ideal. By
Lemma \ref{lemma-ff-rings}
none of the rings $S_i/\mathfrak m S_i$ is zero.
Hence $S/\mathfrak mS = \colim S_i/\mathfrak mS_i$ is nonzero
as well because $1$ is not equal to zero. Thus the image of
$\Spec(S) \to \Spec(R)$ contains $\mathfrak m$ and we see that $R \to S$
is faithfully flat by Lemma \ref{lemma-ff-rings}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-colimit-faithfully-flat}
Soit $R$ un anneau. Soit $\{S_i, \varphi_{ii'}\}$ un système filtrant de
$R$-algèbres fidèlement plates. Alors $S = \colim_i S_i$ est une
$R$-algèbre fidèlement plate.
\end{lemma}

\begin{proof}
D'après le lemme \ref{lemma-colimit-flat}, nous voyons que $S$ est plate.
Soit $\mathfrak m \subset R$ un idéal maximal. D'après le
lemme \ref{lemma-ff-rings},
aucun des anneaux $S_i/\mathfrak m S_i$ n'est nul.
Ainsi $S/\mathfrak mS = \colim S_i/\mathfrak mS_i$ est lui aussi non nul,
car $1$ n'est pas égal à zéro. L'image de
$\Spec(S) \to \Spec(R)$ contient donc $\mathfrak m$, et nous voyons que
$R \to S$ est fidèlement plat d'après le lemme \ref{lemma-ff-rings}.
\end{proof}
```

</details>

## Observations extérieures au texte traduit

### FR-ALGEBRA-B12-SOURCE-NOTE-0001

[Source L8557](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8557) — proposition-going-down-normal-integral.

```tex
$g^n = \sum_{j < n} a_j g^j \in \mathfrak pS
```

Comme Q(g)=g^n+Σajg^j=0, l'égalité exige −Σajg^j. Exemple direct en caractéristique zéro : g=1 a pour polynôme minimal x−1, donc 1=−(−1), non 1=−1. L'appartenance à pS ne dépend pas du signe et l'argument de contradiction subsiste. On conserve la formule officielle dans la traduction et propose le signe moins seulement dans cette note.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

### FR-ALGEBRA-B12-SOURCE-NOTE-0002

[Source L8564](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8564) — proposition-going-down-normal-integral.

```tex
that $Q' = x^n + za_{n-1} x^{n-1} + \ldots + z^{n}a_0$
is the minimal polynomial for $y$.
```

Le changement d'échelle donne le polynôme minimal lorsque z≠0, car la substitution x↦x/z est un automorphisme de K[x]. Pour z=0, Q′=x^n alors que le polynôme minimal de y=0 est x ; par exemple R=Q, S=Q(√2), g=√2, p=p′=q′=0 et z=0 donnent n=2. La conclusion z∈p est cependant immédiate dans ce cas. Réparation proposée hors traduction : traiter z=0 d'abord, puis supposer z≠0. Aucun contre-exemple au théorème n'est allégué.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

### FR-ALGEBRA-B12-SOURCE-NOTE-0003

[Source L8818](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8818) — item-ffg-ideal.

```tex
commute with the obvious map $L' \otimes_R M \to L \otimes_R M$
```

La seconde note de la preuve de lemma-flat suppose L⊂L′⊂R^n. L'application induite par cette inclusion est L⊗M→L′⊗M, pas la flèche inverse imprimée. Les deux injections dans M^n doivent commuter avec cette flèche pour identifier le quotient. Pour L=0, L′=R, M=R non nul, une flèche R→0 ne pourrait pas commuter avec l'inclusion R→R. Source laissée inchangée ; sens opposé proposé seulement ici.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

## Contrôles et suite

Les 720 régions mathématiques concordent après la seule substitution exacte and→et dans la définition des relations triviales. Le préfixe contient 6 709 régions et vingt exceptions linguistiques, dont dix-neuf antérieures. La comparaison brute sans ces exceptions est différente ; aucun masque général ne la remplace.

Aucune citation dans ce lot. Le titre optionnel Equational criterion of flatness est traduit par Critère équationnel de platitude et contrôlé explicitement. Labels, références, contrôles TeX, environnements et items concordent. Les régions mathématiques du fichier français entier restent inchangées depuis le lot 11. Les opérations inverses retrouvent exactement ce lot puis le témoin public conservé.

Les 324 paires couvrent le préfixe sans lacune ni chevauchement ; les octets avant ce lot et ceux du suffixe non relu sont préservés. La validation structurelle complète la lecture sémantique, elle ne la remplace pas.

Prochaine lecture : Supports et annulateurs, anglais L9307 / français L9287. Aucun nouveau PDF ni publication, aucune certification globale du chapitre ou de l’édition.

