# Anneaux de valuation

## Résultat et portée

Une section entièrement comparée : anglais L11723–12148 (426 lignes), français L11672–12077 (406 lignes), soit 19 paires complètes avec preuves et transitions. 171 occurrences sont reliées à des choix contextualisés. La lecture continue atteint 50 sections, 432 paires et 3550 occurrences ; ni le chapitre ni l’édition ne sont terminés.

Sept emplois de domaine deviennent anneau intègre, avec les qualificatifs local et normal lorsque requis ; le sigle anglais PID devient anneau principal. Ces huit changements relèvent du registre français, non de huit corrections mathématiques. Aucun symbole, quantificateur, résultat ou renvoi ne change.

Deux réserves de source restent séparées : une localisation peut être nulle si sa partie multiplicative contient zéro ; la liste des idéaux I_n dans la preuve du critère noethérien omet littéralement l’idéal nul. La traduction ne corrige ni ne complète ces phrases. Aucun erratum n’est admis dans un registre global par ce dossier.

Lecture, normalisation et dossier produits par OpenAI Codex, sans relecture humaine. Les instructions demandent Ultra ; l’identifiant exact du modèle de cette reprise n’est pas attesté par une métadonnée consultée dans ce lot. Ne pas lui attribuer automatiquement le modèle d’un lot antérieur. Les attestations françaises ont été consultées rétrospectivement, dans les limites indiquées ci-dessous.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch17.fr.tex) · [État français précédent](staged/fr/010_algebra.prose-batch16.fr.tex) · [Lot précédent](ALGEBRA_PROSE_BATCH16_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH17_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH17_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH17_OCCURRENCES.json) · [Avant/après](ALGEBRA_PROSE_BATCH17_REPAIRS.json) · [Connecteurs en formule](ALGEBRA_PROSE_BATCH17_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH17_CITATION_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH17_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH17_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Jean-François Dat — Théorie des schémas

[Source consultée](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/Schemas/Schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/dat-schemas.pdf)

Pages 11, 52 et 53 lues intégralement ; §2.6.5 Critères valuatifs. Page 52 rendue avec Poppler et inspectée visuellement.

Attestations courtes : « anneau de valuation », « corps des fractions », « ordre de dominance », « colimites filtrantes ».

Atteste le registre des valuations, de la domination, des idéaux de type fini et des limites filtrantes ; expose le quotient ordonné et le cas discret.

Limites : La page 52 imprime max dans l'inégalité de valuation : cette formule fautive n'est pas importée. Groupe des valeurs et centré ne sont pas prétendus attestés mot pour mot ici. Consultation rétrospective ; pas de relecture humaine.

SHA-256 : 9298B062AC2BDF64161A107980A30F98E1F2DF6DEB4DA98E1FEB21BA494D26A1.

### Antoine Ducros — Introduction à la théorie des schémas

[Source consultée](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages 23 et 24 lues intégralement ; définition 0.1.3 et rappel 0.1.8.1.

Attestations courtes : « anneau intègre », « anneau principal », « anneau factoriel ».

Appuie anneau intègre pour domain, avec la non-nullité, et anneau principal pour le sigle anglais PID.

Limites : Ne constitue pas une preuve des énoncés de Stacks. Domaine reste un emprunt reconnaissable ; les changements visent le registre français et ne sont pas des corrections de théorèmes. Consultation rétrospective.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

## Les huit normalisations françaises

### FR-ALGEBRA-B17-REPAIR-0001

Anglais L11737 ; français L11686.

Avant :
```tex
si $A$ est un domaine local et si $A$ est maximal
```

Après :
```tex
si $A$ est un anneau local intègre et si $A$ est maximal
```

Anneau local intègre explicite le sens mathématique de local domain dans le registre français. Centré est une traduction définitionnelle provisoire : la page consultée n'en fournit pas l'attestation lexicale.

### FR-ALGEBRA-B17-REPAIR-0002

Anglais L11785 ; français L11734.

Avant :
```tex
Alors $A$ est un domaine normal.
```

Après :
```tex
Alors $A$ est un anneau intègre normal.
```

Normalisation de registre, non correction de l'anglais. K désigne implicitement le corps des fractions ; la traduction ne prétend pas réparer ce raccourci source.

### FR-ALGEBRA-B17-REPAIR-0003

Anglais L11854 ; français L11804.

Avant :
```tex
Il est clair que $A$ est un domaine. Soient $a, b \in A$.
```

Après :
```tex
Il est clair que $A$ est un anneau intègre. Soient $a, b \in A$.
```

Anneau intègre remplace domaine. Ensemble dirigé et limites directes filtrantes restent intelligibles et mathématiquement exacts dans ce contexte ; pas de remplacement automatique.

### FR-ALGEBRA-B17-REPAIR-0004

Anglais L11887 ; français L11837.

Avant :
```tex
Cela contredit le fait que $B$ est un domaine local et n'est pas un corps.
```

Après :
```tex
Cela contredit le fait que $B$ est un anneau local intègre et n'est pas un corps.
```

Anneau local intègre remplace domaine local. Algébrique n'est pas remplacé par fini.

### FR-ALGEBRA-B17-REPAIR-0005

Anglais L11925 ; français L11875.

Avant :
```tex
Soit $A$ un domaine normal de corps des fractions $K$.
```

Après :
```tex
Soit $A$ un anneau intègre normal de corps des fractions $K$.
```

Anneau intègre normal est une normalisation de registre ; les deux clauses et leur différence de portée sont conservées.

### FR-ALGEBRA-B17-REPAIR-0006

Anglais L12025 ; français L11975.

Avant :
```tex
\item $A$ est un domaine local et tout idéal
```

Après :
```tex
\item $A$ est un anneau local intègre et tout idéal
```

La preuve choisit v(f_i) et simplifie par h sans détailler les cas nuls. Ceux-ci sont élémentaires, mais l'édition fidèle ne les ajoute pas ; ne pas compter cette note de lecture comme une réfutation du critère.

### FR-ALGEBRA-B17-REPAIR-0007

Anglais L12034 ; français L11984.

Avant :
```tex
un domaine local et que tout idéal de $A$ engendré par un nombre fini d'éléments soit principal.
```

Après :
```tex
un anneau local intègre et que tout idéal de $A$ engendré par un nombre fini d'éléments soit principal.
```

La preuve choisit v(f_i) et simplifie par h sans détailler les cas nuls. Ceux-ci sont élémentaires, mais l'édition fidèle ne les ajoute pas ; ne pas compter cette note de lecture comme une réfutation du critère.

### FR-ALGEBRA-B17-REPAIR-0008

Anglais L12109 ; français L12059.

Avant :
```tex
Ainsi $A$ est un PID, donc certainement noethérien.
```

Après :
```tex
Ainsi $A$ est un anneau principal, donc certainement noethérien.
```

PID est un sigle anglais restant à traduire. La réserve sur l'idéal nul concerne une phrase de preuve, pas la validité de l'équivalence.

## Règles contextualisées

### FR-ALGEBRA-B17-RULE-VALUATION

Valuation, anneau de valuation et cas discret sont distingués ; un corps reste un anneau de valuation au sens de la source.

Canon : FR-ALGEBRA-B17-CANON-DAT.

### FR-ALGEBRA-B17-RULE-DOMAIN

Domain se lit anneau intègre, avec non-nullité ; local et normal restent des propriétés supplémentaires.

Canon : FR-ALGEBRA-B17-CANON-DUCROS.

### FR-ALGEBRA-B17-RULE-DOMINATION

La domination inclut la contraction de l'idéal maximal. Centré conserve sa définition source ; attestation lexicale externe non revendiquée pour ce dernier mot.

Canon : FR-ALGEBRA-B17-CANON-DAT.

### FR-ALGEBRA-B17-RULE-FIELD

Le corps des fractions et le corps résiduel ne sont pas interchangés. Algébrique n'impose pas la finitude.

Canon : FR-ALGEBRA-B17-CANON-DAT.

### FR-ALGEBRA-B17-RULE-GROUP

Le quotient ordonné est écrit additivement. Groupe des valeurs repose sur la construction source ; sa locution exacte n'est pas attestée par les pages lues.

Canon : FR-ALGEBRA-B17-CANON-DAT.

### FR-ALGEBRA-B17-RULE-IDEAL

Vérifier le sens d'idéal dans A ou dans Γ, la distinction premier/maximal, et principal/type fini. PID devient anneau principal.

Canon : FR-ALGEBRA-B17-CANON-DAT, FR-ALGEBRA-B17-CANON-DUCROS.

### FR-ALGEBRA-B17-RULE-COLIMIT

Le système dirigé est conservé ; l'attestation colimites filtrantes appuie le sens sans imposer une substitution de synonymes.

Canon : FR-ALGEBRA-B17-CANON-DAT.

### FR-ALGEBRA-B17-RULE-LOGIC

Quantificateurs, exceptions de non-nullité, disjonctions inclusives et sens des bijections vérifiés dans chaque passage complet.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B17-RULE-INTEGRAL

Entier sur un anneau, extension algébrique, finitude de module et type fini d'un idéal restent distingués par le contexte source.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B17-RULE-ORDER

Conserver le sens de l'ordre, la positivité stricte et la condition de chaîne ; le minimum dans l'inégalité reste celui de Stacks.

Canon : FR-ALGEBRA-B17-CANON-DAT.

## Passages parallèles complets

### 01 — section-valuation-rings

Anglais L11723–11728 ; français L11672–11677.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11723) · FR-ALGEBRA-B17-CHOICE-0001.

Anneaux de valuation est attesté exactement par Dat, §2.6.5. L'annonce des définitions est conservée ; aucune interprétation supplémentaire n'est insérée dans le texte.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-INTEGRAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Valuation rings}
\label{section-valuation-rings}

\noindent
Here are some definitions.
```

Français restauré :
```tex
\section{Anneaux de valuation}
\label{section-valuation-rings}

\noindent
Voici quelques définitions.
```

</details>

### 02 — definition-valuation-ring

Anglais L11729–11748 ; français L11678–11697.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11729) · FR-ALGEBRA-B17-CHOICE-0002.

Domine conserve les deux conditions : inclusion des anneaux et contraction de l'idéal maximal. La maximalité porte sur cette relation, dans le corps des fractions fixé. Domaine local devient anneau local intègre. Centré sur R conserve la définition R inclus dans A, sans la confondre avec la domination de R. Le corps est explicitement admis comme anneau de valuation.

Point particulier à relire : Anneau local intègre explicite le sens mathématique de local domain dans le registre français. Centré est une traduction définitionnelle provisoire : la page consultée n'en fournit pas l'attestation lexicale.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-DOMAIN, FR-ALGEBRA-B17-RULE-DOMINATION, FR-ALGEBRA-B17-RULE-FIELD, FR-ALGEBRA-B17-RULE-INTEGRAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-valuation-ring}
Valuation rings.
\begin{enumerate}
\item Let $K$ be a field. Let $A$, $B$ be local rings contained
in $K$. We say that $B$ {\it dominates} $A$ if $A \subset B$
and $\mathfrak m_A = A \cap \mathfrak m_B$.
\item Let $A$ be a ring. We say $A$ is a {\it valuation ring}
if $A$ is a local domain and if $A$ is maximal
for the relation of domination among local rings contained in
the fraction field of $A$.
\item Let $A$ be a valuation ring with fraction field $K$.
If $R \subset K$ is a subring of $K$, then we say $A$
is {\it centered} on $R$ if $R \subset A$.
\end{enumerate}
\end{definition}

\noindent
With this definition a field is a valuation ring.
```

Français restauré :
```tex
\begin{definition}
\label{definition-valuation-ring}
Anneaux de valuation.
\begin{enumerate}
\item Soit $K$ un corps. Soient $A$, $B$ des anneaux locaux contenus
dans $K$. Nous disons que $B$ {\it domine} $A$ si $A \subset B$
et si $\mathfrak m_A = A \cap \mathfrak m_B$.
\item Soit $A$ un anneau. Nous disons que $A$ est un {\it anneau de valuation}
si $A$ est un anneau local intègre et si $A$ est maximal
pour la relation de domination parmi les anneaux locaux contenus dans
le corps des fractions de $A$.
\item Soit $A$ un anneau de valuation de corps des fractions $K$.
Si $R \subset K$ est un sous-anneau de $K$, nous disons que $A$
est {\it centré} sur $R$ si $R \subset A$.
\end{enumerate}
\end{definition}

\noindent
Avec cette définition, un corps est un anneau de valuation.
```

</details>

### 03 — lemma-dominate

Anglais L11749–11781 ; français L11698–11730.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11749) · FR-ALGEBRA-B17-CHOICE-0003.

L'existence concerne un anneau dominant A et dont le corps des fractions est exactement K, pas seulement un sous-corps de K. L'ordre partiel, la chaîne totalement ordonnée, la réunion et le recours à Zorn sont intégralement conservés. Les cas transcendant et algébrique sont distincts ; entier et fini restent des propriétés différentes. La contradiction finale porte sur t dans le corps des fractions initial.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-DOMINATION, FR-ALGEBRA-B17-RULE-FIELD, FR-ALGEBRA-B17-RULE-IDEAL, FR-ALGEBRA-B17-RULE-LOGIC, FR-ALGEBRA-B17-RULE-INTEGRAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-dominate}
Let $K$ be a field. Let $A \subset K$ be a local subring.
Then there exists a valuation ring with fraction field $K$
dominating $A$.
\end{lemma}

\begin{proof}
We consider the collection of local subrings
of $K$ as a partially ordered set using the relation of domination.
Suppose that $\{A_i\}_{i \in I}$ is a totally ordered
collection of local subrings of $K$. Then $B = \bigcup A_i$
is a local subring which dominates all of the $A_i$.
Hence by Zorn's Lemma, it suffices to show that if $A \subset K$
is a local ring whose fraction field is not $K$, then there
exists a local ring $B \subset K$, $B \not = A$ dominating $A$.

\medskip\noindent
Pick $t \in K$ which is not in the fraction field of $A$.
If $t$ is transcendental over $A$, then $A[t] \subset K$
and hence $A[t]_{(t, \mathfrak m)} \subset K$ is a local ring
distinct from $A$ dominating $A$. Suppose $t$ is algebraic over $A$.
Then for some nonzero $a \in A$ the element $at$ is integral over $A$.
In this case the subring $A' \subset K$ generated by $A$ and
$ta$ is finite over $A$.
By Lemma \ref{lemma-integral-overring-surjective} there exists
a prime ideal $\mathfrak m' \subset A'$ lying over
$\mathfrak m$. Then $A'_{\mathfrak m'}$ dominates
$A$. If $A = A'_{\mathfrak m'}$, then $t$
is in the fraction field of $A$ which we assumed not to be the case.
Thus $A \not = A'_{\mathfrak m'}$ as desired.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-dominate}
Soit $K$ un corps. Soit $A \subset K$ un sous-anneau local.
Alors il existe un anneau de valuation de corps des fractions $K$
qui domine $A$.
\end{lemma}

\begin{proof}
Nous considérons l'ensemble des sous-anneaux locaux
de $K$ comme un ensemble partiellement ordonné par la relation de domination.
Supposons que $\{A_i\}_{i \in I}$ soit une famille totalement ordonnée
de sous-anneaux locaux de $K$. Alors $B = \bigcup A_i$
est un sous-anneau local qui domine tous les $A_i$.
Par conséquent, par le lemme de Zorn, il suffit de montrer que si $A \subset K$
est un anneau local dont le corps des fractions n'est pas $K$, alors il
existe un anneau local $B \subset K$, $B \not = A$, qui domine $A$.

\medskip\noindent
Choisissons $t \in K$ qui n'appartient pas au corps des fractions de $A$.
Si $t$ est transcendant sur $A$, alors $A[t] \subset K$
et donc $A[t]_{(t, \mathfrak m)} \subset K$ est un anneau local
distinct de $A$ qui domine $A$. Supposons que $t$ soit algébrique sur $A$.
Alors, pour un certain $a \in A$ non nul, l'élément $at$ est entier sur $A$.
Dans ce cas, le sous-anneau $A' \subset K$ engendré par $A$ et
$ta$ est fini sur $A$.
Par le Lemme \ref{lemma-integral-overring-surjective}, il existe
un idéal premier $\mathfrak m' \subset A'$ au-dessus de
$\mathfrak m$. Alors $A'_{\mathfrak m'}$ domine
$A$. Si $A = A'_{\mathfrak m'}$, alors $t$
appartient au corps des fractions de $A$, ce que nous avons supposé faux.
Ainsi $A \not = A'_{\mathfrak m'}$, comme voulu.
\end{proof}
```

</details>

### 04 — lemma-valuation-ring-normal

Anglais L11782–11799 ; français L11731–11748.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11782) · FR-ALGEBRA-B17-CHOICE-0004.

Domaine normal devient anneau intègre normal. La normalité est prouvée par l'appartenance à A de tout élément du corps des fractions entier sur A. Extension entière, idéal premier au-dessus de l'idéal maximal et domination restent distincts. La lettre K est implicite dans la source ; aucune nouvelle déclaration de variable n'est ajoutée à la traduction.

Point particulier à relire : Normalisation de registre, non correction de l'anglais. K désigne implicitement le corps des fractions ; la traduction ne prétend pas réparer ce raccourci source.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-DOMAIN, FR-ALGEBRA-B17-RULE-DOMINATION, FR-ALGEBRA-B17-RULE-FIELD, FR-ALGEBRA-B17-RULE-IDEAL, FR-ALGEBRA-B17-RULE-LOGIC, FR-ALGEBRA-B17-RULE-INTEGRAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-valuation-ring-normal}
Let $A$ be a valuation ring.
Then $A$ is a normal domain.
\end{lemma}

\begin{proof}
Suppose $x$ is in the field of fractions of $A$ and integral over $A$.
Let $A'$ denote the subring of $K$ generated by $A$ and $x$.
Since $A\subset A'$ is an integral extension, we see by
Lemma \ref{lemma-integral-overring-surjective} that there is
a prime ideal $\mathfrak m' \subset A'$ lying over
$\mathfrak m$. Then $A'_{\mathfrak m'}$ dominates
$A$. Since $A$ is a valuation ring we conclude that $A=A'_{\mathfrak m'}$
and therefore that $x\in A$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-valuation-ring-normal}
Soit $A$ un anneau de valuation.
Alors $A$ est un anneau intègre normal.
\end{lemma}

\begin{proof}
Supposons que $x$ appartienne au corps des fractions de $A$ et soit entier sur $A$.
Soit $A'$ le sous-anneau de $K$ engendré par $A$ et $x$.
Comme $A\subset A'$ est une extension entière, le
Lemme \ref{lemma-integral-overring-surjective} montre qu'il existe
un idéal premier $\mathfrak m' \subset A'$ au-dessus de
$\mathfrak m$. Alors $A'_{\mathfrak m'}$ domine
$A$. Comme $A$ est un anneau de valuation, nous concluons que $A=A'_{\mathfrak m'}$
et donc que $x\in A$.
\end{proof}
```

</details>

### 05 — lemma-valuation-ring-x-or-x-inverse

Anglais L11800–11821 ; français L11749–11770.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11800) · FR-ALGEBRA-B17-CHOICE-0005.

La disjonction est inclusive : x ou son inverse, ou les deux. Les idéaux premiers, la vacuité du fermé et la relation entière sont conservés avec les mêmes indices. La preuve part de x hors de A, donc non nul ; la formulation de l'énoncé pour x nul est laissée telle quelle, sans ajouter une hypothèse.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-FIELD, FR-ALGEBRA-B17-RULE-IDEAL, FR-ALGEBRA-B17-RULE-LOGIC, FR-ALGEBRA-B17-RULE-INTEGRAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-valuation-ring-x-or-x-inverse}
Let $A$ be a valuation ring with maximal ideal $\mathfrak m$ and
fraction field $K$.
Let $x \in K$. Then either $x \in A$ or $x^{-1} \in A$ or both.
\end{lemma}

\begin{proof}
Assume that $x$ is not in $A$.
Let $A'$ denote the subring of $K$ generated by $A$ and $x$.
Since $A$ is a valuation ring we see that there is no prime
of $A'$ lying over $\mathfrak m$. Since $\mathfrak m$ is maximal
we see that $V(\mathfrak m A') = \emptyset$. Then $\mathfrak m A' = A'$
by Lemma \ref{lemma-Zariski-topology}.
Hence we can write
$1 = \sum_{i = 0}^d t_i x^i$ with $t_i \in \mathfrak m$.
This implies that $(1 - t_0) (x^{-1})^d - \sum t_i (x^{-1})^{d - i} = 0$.
In particular we see that $x^{-1}$ is integral over $A$, and hence
$x^{-1} \in A$ by
Lemma \ref{lemma-valuation-ring-normal}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-valuation-ring-x-or-x-inverse}
Soit $A$ un anneau de valuation d'idéal maximal $\mathfrak m$ et de
corps des fractions $K$.
Soit $x \in K$. Alors $x \in A$ ou bien $x^{-1} \in A$, ou les deux.
\end{lemma}

\begin{proof}
Supposons que $x$ n'appartienne pas à $A$.
Soit $A'$ le sous-anneau de $K$ engendré par $A$ et $x$.
Comme $A$ est un anneau de valuation, aucun idéal premier de $A'$
n'est au-dessus de $\mathfrak m$. Comme $\mathfrak m$ est maximal,
nous avons $V(\mathfrak m A') = \emptyset$. Alors $\mathfrak m A' = A'$
par le Lemme \ref{lemma-Zariski-topology}.
Nous pouvons donc écrire
$1 = \sum_{i = 0}^d t_i x^i$ avec $t_i \in \mathfrak m$.
Cela implique que $(1 - t_0) (x^{-1})^d - \sum t_i (x^{-1})^{d - i} = 0$.
En particulier, $x^{-1}$ est entier sur $A$, et donc
$x^{-1} \in A$ par le
Lemme \ref{lemma-valuation-ring-normal}.
\end{proof}
```

</details>

### 06 — lemma-x-or-x-inverse-valuation-ring

Anglais L11822–11842 ; français L11771–11792.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11822) · FR-ALGEBRA-B17-CHOICE-0006.

La réciproque conserve la quantification sur les éléments du corps ambiant et la conclusion sur le corps des fractions. Les deux idéaux maximaux distincts donnent les deux fractions contradictoires. La dernière contradiction utilise précisément la contraction de l'idéal maximal dans la domination, pas la seule inclusion des anneaux.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-DOMINATION, FR-ALGEBRA-B17-RULE-FIELD, FR-ALGEBRA-B17-RULE-IDEAL, FR-ALGEBRA-B17-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-x-or-x-inverse-valuation-ring}
Let $A \subset K$ be a subring of a field $K$ such that for all
$x \in K$ either $x \in A$ or $x^{-1} \in A$ or both.
Then $A$ is a valuation ring with fraction field $K$.
\end{lemma}

\begin{proof}
If $A$ is not $K$, then $A$ is not a field and there is a nonzero
maximal ideal $\mathfrak m$.
If $\mathfrak m'$ is a second maximal ideal, then choose $x, y \in A$
with $x \in \mathfrak m$, $y \not \in \mathfrak m$,
$x \not \in \mathfrak m'$, and $y \in \mathfrak m'$.
Then neither $x/y \in A$ nor $y/x \in A$
contradicting the assumption of the lemma. Thus we see that $A$ is
a local ring. Suppose that $A'$ is a local ring contained in $K$ which
dominates $A$. Let $x \in A'$. We have to show that $x \in A$. If not, then
$x^{-1} \in A$, and of course $x^{-1} \in \mathfrak m_A$. But then
$x^{-1} \in \mathfrak m_{A'}$ which contradicts $x \in A'$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-x-or-x-inverse-valuation-ring}
Soit $A \subset K$ un sous-anneau d'un corps $K$ tel que, pour tout
$x \in K$, on ait $x \in A$ ou bien $x^{-1} \in A$, ou les deux.
Alors $A$ est un anneau de valuation de corps des fractions $K$.
\end{lemma}

\begin{proof}
Si $A$ n'est pas $K$, alors $A$ n'est pas un corps et possède un idéal
maximal non nul $\mathfrak m$.
Si $\mathfrak m'$ est un second idéal maximal, choisissons $x, y \in A$
tels que $x \in \mathfrak m$, $y \not \in \mathfrak m$,
$x \not \in \mathfrak m'$, et $y \in \mathfrak m'$.
Alors ni $x/y \in A$ ni $y/x \in A$,
ce qui contredit l'hypothèse du lemme. Ainsi $A$ est
un anneau local. Supposons que $A'$ soit un anneau local contenu dans $K$
qui domine $A$. Soit $x \in A'$. Nous devons montrer que $x \in A$. Sinon,
$x^{-1} \in A$, et bien sûr $x^{-1} \in \mathfrak m_A$. Mais alors
$x^{-1} \in \mathfrak m_{A'}$, ce qui contredit $x \in A'$.
\end{proof}
```

</details>

### 07 — lemma-colimit-valuation-rings

Anglais L11843–11861 ; français L11793–11811.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11843) · FR-ALGEBRA-B17-CHOICE-0007.

Le slogan limites directes filtrantes, l'ensemble dirigé et le système indexé expriment le même système orienté ; ensemble dirigé est conservé, sans normalisation gratuite. Domaine devient anneau intègre dans la preuve. Les morphismes du système ne sont pas silencieusement supposés injectifs ou locaux. La divisibilité comparée de deux éléments est transportée depuis un indice commun.

Point particulier à relire : Anneau intègre remplace domaine. Ensemble dirigé et limites directes filtrantes restent intelligibles et mathématiquement exacts dans ce contexte ; pas de remplacement automatique.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-DOMAIN, FR-ALGEBRA-B17-RULE-COLIMIT, FR-ALGEBRA-B17-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-colimit-valuation-rings}
\begin{slogan}
Valuation rings are stable under filtered direct limits
\end{slogan}
Let $I$ be a directed set. Let $(A_i, \varphi_{ij})$
be a system of valuation rings over $I$.
Then $A = \colim A_i$ is a valuation ring.
\end{lemma}

\begin{proof}
It is clear that $A$ is a domain. Let $a, b \in A$.
Lemma \ref{lemma-x-or-x-inverse-valuation-ring} tells us we have
to show that either $a | b$ or $b | a$ in $A$. Choose $i$
so large that there exist $a_i, b_i \in A_i$ mapping to $a, b$.
Then Lemma \ref{lemma-valuation-ring-x-or-x-inverse}
applied to $a_i, b_i$ in $A_i$ implies the result for $a, b$ in $A$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-colimit-valuation-rings}
\begin{slogan}
Les anneaux de valuation sont stables par limites directes filtrantes
\end{slogan}
Soit $I$ un ensemble dirigé. Soit $(A_i, \varphi_{ij})$
un système d'anneaux de valuation indexé par $I$.
Alors $A = \colim A_i$ est un anneau de valuation.
\end{lemma}

\begin{proof}
Il est clair que $A$ est un anneau intègre. Soient $a, b \in A$.
Le Lemme \ref{lemma-x-or-x-inverse-valuation-ring} nous dit qu'il faut
montrer que $a | b$ ou $b | a$ dans $A$. Choisissons $i$
assez grand pour qu'il existe $a_i, b_i \in A_i$ dont les images soient $a, b$.
Alors le Lemme \ref{lemma-valuation-ring-x-or-x-inverse}
appliqué à $a_i, b_i$ dans $A_i$ donne le résultat pour $a, b$ dans $A$.
\end{proof}
```

</details>

### 08 — lemma-valuation-ring-cap-field

Anglais L11862–11874 ; français L11812–11824.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11862) · FR-ALGEBRA-B17-CHOICE-0008.

L'intersection avec K est prise dans L. La preuve permet que L soit plus grand que le corps des fractions de B et remplace aussi K par K intersecté avec F ; ces deux remplacements sont conservés. Aucune hypothèse d'algébricité n'est ajoutée ici.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-FIELD.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-valuation-ring-cap-field}
Let $L/K$ be an extension of fields. If $B \subset L$
is a valuation ring, then $A = K \cap B$ is a valuation ring.
\end{lemma}

\begin{proof}
We can replace $L$ by the fraction field $F$ of $B$ and $K$ by
$K \cap F$. Then the lemma follows from a combination of
Lemmas \ref{lemma-valuation-ring-x-or-x-inverse} and
\ref{lemma-x-or-x-inverse-valuation-ring}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-valuation-ring-cap-field}
Soit $L/K$ une extension de corps. Si $B \subset L$
est un anneau de valuation, alors $A = K \cap B$ est un anneau de valuation.
\end{lemma}

\begin{proof}
Nous pouvons remplacer $L$ par le corps des fractions $F$ de $B$ et $K$ par
$K \cap F$. Le lemme résulte alors d'une combinaison des
Lemmes \ref{lemma-valuation-ring-x-or-x-inverse} et
\ref{lemma-x-or-x-inverse-valuation-ring}.
\end{proof}
```

</details>

### 09 — lemma-valuation-ring-cap-field-finite

Anglais L11875–11889 ; français L11825–11839.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11875) · FR-ALGEBRA-B17-CHOICE-0009.

L'extension est algébrique, sans hypothèse de finitude malgré le nom interne du label. Le corps des fractions de B est L et B n'est pas un corps ; la conclusion non-corps pour A est préservée. Domaine local devient anneau local intègre. Les inclusions propres entre idéaux premiers ne deviennent pas une affirmation qu'il n'existe aucun idéal premier.

Point particulier à relire : Anneau local intègre remplace domaine local. Algébrique n'est pas remplacé par fini.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-DOMAIN, FR-ALGEBRA-B17-RULE-FIELD, FR-ALGEBRA-B17-RULE-IDEAL, FR-ALGEBRA-B17-RULE-INTEGRAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-valuation-ring-cap-field-finite}
Let $L/K$ be an algebraic extension of fields. If $B \subset L$
is a valuation ring with fraction field $L$ and not a field, then
$A = K \cap B$ is a valuation ring and not a field.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-valuation-ring-cap-field} the ring $A$ is a valuation
ring. If $A$ is a field, then $A = K$. Then $A = K \subset B$ is an integral
extension, hence there are no proper inclusions among the primes of $B$
(Lemma \ref{lemma-integral-no-inclusion}).
This contradicts the assumption that $B$ is a local domain and not a field.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-valuation-ring-cap-field-finite}
Soit $L/K$ une extension algébrique de corps. Si $B \subset L$
est un anneau de valuation de corps des fractions $L$ et n'est pas un corps, alors
$A = K \cap B$ est un anneau de valuation et n'est pas un corps.
\end{lemma}

\begin{proof}
Par le Lemme \ref{lemma-valuation-ring-cap-field}, l'anneau $A$ est un anneau de
valuation. Si $A$ est un corps, alors $A = K$. Alors $A = K \subset B$ est une extension
entière, donc il n'y a pas d'inclusions propres entre les idéaux premiers de $B$
(Lemme \ref{lemma-integral-no-inclusion}).
Cela contredit le fait que $B$ est un anneau local intègre et n'est pas un corps.
\end{proof}
```

</details>

### 10 — lemma-make-valuation-rings

Anglais L11890–11901 ; français L11840–11851.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11890) · FR-ALGEBRA-B17-CHOICE-0010.

Le quotient est par un idéal premier ; la localisation au premier est distinguée de toute localisation. Cette dernière expression est traduite littéralement malgré la réserve sur une partie multiplicative contenant zéro, consignée séparément. On n'ajoute pas non nulle dans l'édition fidèle.

Point particulier à relire : La réserve sur toute localisation dépend de la convention autorisant zéro dans une partie multiplicative ; la définition officielle a été vérifiée. La réserve ne modifie pas la traduction.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-IDEAL, FR-ALGEBRA-B17-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-make-valuation-rings}
Let $A$ be a valuation ring. For any prime ideal $\mathfrak p \subset A$ the
quotient $A/\mathfrak p$ is a valuation ring. The same is true for the
localization $A_\mathfrak p$ and in fact any localization of $A$.
\end{lemma}

\begin{proof}
Use the characterization of valuation rings given
in Lemma \ref{lemma-x-or-x-inverse-valuation-ring}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-make-valuation-rings}
Soit $A$ un anneau de valuation. Pour tout idéal premier $\mathfrak p \subset A$, le
quotient $A/\mathfrak p$ est un anneau de valuation. Il en va de même pour la
localisation $A_\mathfrak p$ et, en fait, pour toute localisation de $A$.
\end{lemma}

\begin{proof}
Utiliser la caractérisation des anneaux de valuation donnée
dans le Lemme \ref{lemma-x-or-x-inverse-valuation-ring}.
\end{proof}
```

</details>

### 11 — lemma-stack-valuation-rings

Anglais L11902–11922 ; français L11852–11872.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11902) · FR-ALGEBRA-B17-CHOICE-0011.

K est le corps résiduel de A′, mais le corps des fractions de A. C est l'image inverse de A par la réduction modulo l'idéal maximal de A′. Les deux usages du critère x ou son inverse et la distinction unité/élément de l'idéal maximal sont conservés ; les corps résiduels ne sont pas remplacés par des corps des fractions.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-FIELD.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-stack-valuation-rings}
Let $A'$ be a valuation ring with residue field $K$.
Let $A$ be a valuation ring with fraction field $K$.
Then
$C = \{\lambda \in A' \mid \lambda \bmod \mathfrak m_{A'} \in A\}$
is a valuation ring.
\end{lemma}

\begin{proof}
Note that $\mathfrak m_{A'} \subset C$ and $C/\mathfrak m_{A'} = A$.
In particular, the fraction field of $C$ is equal to the fraction field
of $A'$. We will use the criterion of
Lemma \ref{lemma-x-or-x-inverse-valuation-ring} to prove the lemma.
Let $x$ be an element of the fraction field of $C$.
By the lemma we may assume $x \in A'$. If $x \in \mathfrak m_{A'}$,
then we see $x \in C$. If not, then $x$ is a unit of $A'$ and we
also have $x^{-1} \in A'$. Hence either $x$ or $x^{-1}$ maps to
an element of $A$ by the lemma again.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-stack-valuation-rings}
Soit $A'$ un anneau de valuation de corps résiduel $K$.
Soit $A$ un anneau de valuation de corps des fractions $K$.
Alors
$C = \{\lambda \in A' \mid \lambda \bmod \mathfrak m_{A'} \in A\}$
est un anneau de valuation.
\end{lemma}

\begin{proof}
Remarquons que $\mathfrak m_{A'} \subset C$ et que $C/\mathfrak m_{A'} = A$.
En particulier, le corps des fractions de $C$ est égal au corps des fractions
de $A'$. Nous utiliserons le critère du
Lemme \ref{lemma-x-or-x-inverse-valuation-ring} pour démontrer le lemme.
Soit $x$ un élément du corps des fractions de $C$.
D'après le lemme, nous pouvons supposer que $x \in A'$. Si $x \in \mathfrak m_{A'}$,
alors $x \in C$. Sinon, $x$ est une unité de $A'$ et nous avons
également $x^{-1} \in A'$. Ainsi $x$ ou $x^{-1}$ s'envoie sur
un élément de $A$, à nouveau par le lemme.
\end{proof}
```

</details>

### 12 — lemma-find-valuation-rings

Anglais L11923–11968 ; français L11873–11918.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11923) · FR-ALGEBRA-B17-CHOICE-0012.

Anneau intègre normal remplace domaine normal. L'existence pour chaque élément extérieur à A est distinguée du choix dominant A lorsque A est local. Le sens des deux descriptions par intersection est inchangé. La preuve par x inverse, les deux relations polynomiales et l'inversibilité de 1−a′0 sont conservées. Le paragraphe suivant définit un groupe abélien totalement ordonné, avec compatibilité de l'ordre à la translation.

Point particulier à relire : Anneau intègre normal est une normalisation de registre ; les deux clauses et leur différence de portée sont conservées.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-DOMAIN, FR-ALGEBRA-B17-RULE-DOMINATION, FR-ALGEBRA-B17-RULE-FIELD, FR-ALGEBRA-B17-RULE-GROUP, FR-ALGEBRA-B17-RULE-IDEAL, FR-ALGEBRA-B17-RULE-LOGIC, FR-ALGEBRA-B17-RULE-INTEGRAL, FR-ALGEBRA-B17-RULE-ORDER.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-find-valuation-rings}
Let $A$ be a normal domain with fraction field $K$.
\begin{enumerate}
\item For every $x \in K$, $x \not \in A$ there exists a valuation ring
$A \subset V \subset K$ with fraction field $K$ such that $x \not \in V$.
\item If $A$ is local, we can moreover choose $V$ which dominates $A$.
\end{enumerate}
In other words, $A$ is the intersection of all valuation rings in $K$
containing $A$ and if $A$ is local, then $A$ is the intersection of
all valuation rings in $K$ dominating $A$.
\end{lemma}

\begin{proof}
Suppose $x \in K$, $x \not \in A$. Consider $B = A[x^{-1}]$.
Then $x \not \in B$. Namely, if $x = a_0 + a_1x^{-1} + \ldots + a_d x^{-d}$
then $x^{d + 1} - a_0x^d - \ldots - a_d = 0$ and $x$ is integral
over $A$ in contradiction with the fact that $A$ is normal.
Thus $x^{-1}$ is not a unit in $B$. Thus $V(x^{-1}) \subset \Spec(B)$
is not empty (Lemma \ref{lemma-Zariski-topology}), and we can choose a prime
$\mathfrak p \subset B$ with $x^{-1} \in \mathfrak p$.
Choose a valuation ring $V \subset K$ dominating $B_\mathfrak p$
(Lemma \ref{lemma-dominate}).
Then $x \not \in V$ as $x^{-1} \in \mathfrak m_V$.

\medskip\noindent
If $A$ is local, then we claim that $x^{-1} B + \mathfrak m_A B \not = B$.
Namely, if $1 = (a_0 + a_1x^{-1} + \ldots + a_d x^{-d})x^{-1} +
a'_0 + \ldots + a'_d x^{-d}$ with $a_i \in A$ and $a'_i \in \mathfrak m_A$,
then we'd get
$$
(1 - a'_0) x^{d + 1} - (a_0 + a'_1) x^d - \ldots - a_d = 0
$$
Since $a'_0 \in \mathfrak m_A$ we see that $1 - a'_0$ is a unit in $A$
and we conclude that $x$ would be integral over $A$, a contradiction as
before. Then choose the prime $\mathfrak p \supset x^{-1} B + \mathfrak m_A B$
we find $V$ dominating $A$.
\end{proof}

\noindent
An {\it totally ordered abelian group} is a pair $(\Gamma, \geq)$
consisting of an abelian group $\Gamma$ endowed with a total
ordering $\geq$ such that $\gamma \geq \gamma' \Rightarrow
\gamma + \gamma'' \geq \gamma' + \gamma''$ for all
$\gamma, \gamma', \gamma'' \in \Gamma$.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-find-valuation-rings}
Soit $A$ un anneau intègre normal de corps des fractions $K$.
\begin{enumerate}
\item Pour tout $x \in K$, $x \not \in A$, il existe un anneau de valuation
$A \subset V \subset K$ de corps des fractions $K$ tel que $x \not \in V$.
\item Si $A$ est local, nous pouvons de plus choisir $V$ qui domine $A$.
\end{enumerate}
Autrement dit, $A$ est l'intersection de tous les anneaux de valuation dans $K$
contenant $A$ et, si $A$ est local, $A$ est l'intersection de tous les anneaux de
valuation dans $K$ qui dominent $A$.
\end{lemma}

\begin{proof}
Supposons que $x \in K$, $x \not \in A$. Considérons $B = A[x^{-1}]$.
Alors $x \not \in B$. En effet, si $x = a_0 + a_1x^{-1} + \ldots + a_d x^{-d}$
alors $x^{d + 1} - a_0x^d - \ldots - a_d = 0$ et $x$ est entier
sur $A$, contradiction avec le fait que $A$ est normal.
Ainsi $x^{-1}$ n'est pas une unité de $B$. Donc $V(x^{-1}) \subset \Spec(B)$
n'est pas vide (Lemme \ref{lemma-Zariski-topology}), et nous pouvons choisir un idéal premier
$\mathfrak p \subset B$ tel que $x^{-1} \in \mathfrak p$.
Choisissons un anneau de valuation $V \subset K$ dominant $B_\mathfrak p$
(Lemme \ref{lemma-dominate}).
Alors $x \not \in V$ puisque $x^{-1} \in \mathfrak m_V$.

\medskip\noindent
Si $A$ est local, nous affirmons que $x^{-1} B + \mathfrak m_A B \not = B$.
En effet, si $1 = (a_0 + a_1x^{-1} + \ldots + a_d x^{-d})x^{-1} +
a'_0 + \ldots + a'_d x^{-d}$ avec $a_i \in A$ et $a'_i \in \mathfrak m_A$,
alors nous obtenons
$$
(1 - a'_0) x^{d + 1} - (a_0 + a'_1) x^d - \ldots - a_d = 0
$$
Comme $a'_0 \in \mathfrak m_A$, $1 - a'_0$ est une unité de $A$
et nous concluons que $x$ serait entier sur $A$, contradiction comme
précédemment. Choisissons alors l'idéal premier $\mathfrak p \supset x^{-1} B + \mathfrak m_A B$ ;
nous trouvons $V$ dominant $A$.
\end{proof}

\noindent
Un {\it groupe abélien totalement ordonné} est un couple $(\Gamma, \geq)$
constitué d'un groupe abélien $\Gamma$ muni d'un
ordre total $\geq$ tel que $\gamma \geq \gamma' \Rightarrow
\gamma + \gamma'' \geq \gamma' + \gamma''$ pour tous
$\gamma, \gamma', \gamma'' \in \Gamma$.
```

</details>

### 13 — lemma-valuation-group

Anglais L11969–11985 ; français L11919–11935.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11969) · FR-ALGEBRA-B17-CHOICE-0013.

Le quotient K*/A* est écrit additivement bien que ses représentants se multiplient. Le signe de la relation d'ordre, l'image des éléments non nuls de A et le cas du groupe nul lorsque A est un corps sont conservés. La preuve annoncée omise reste omise.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-FIELD, FR-ALGEBRA-B17-RULE-GROUP, FR-ALGEBRA-B17-RULE-LOGIC, FR-ALGEBRA-B17-RULE-INTEGRAL, FR-ALGEBRA-B17-RULE-ORDER.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-valuation-group}
Let $A$ be a valuation ring with field of fractions $K$.
Set $\Gamma = K^*/A^*$ (with group law written additively).
For $\gamma, \gamma' \in \Gamma$
define $\gamma \geq \gamma'$ if and only if
$\gamma - \gamma'$ is in the image of $A - \{0\} \to \Gamma$.
Then $(\Gamma, \geq)$ is a totally ordered abelian group.
\end{lemma}

\begin{proof}
Omitted, but follows easily from
Lemma \ref{lemma-valuation-ring-x-or-x-inverse}.
Note that in case $A = K$ we obtain the zero group $\Gamma = \{0\}$
endowed with its unique total ordering.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-valuation-group}
Soit $A$ un anneau de valuation de corps des fractions $K$.
Posons $\Gamma = K^*/A^*$ (la loi de groupe étant écrite additivement).
Pour $\gamma, \gamma' \in \Gamma$,
définissons $\gamma \geq \gamma'$ si et seulement si
$\gamma - \gamma'$ appartient à l'image de $A - \{0\} \to \Gamma$.
Alors $(\Gamma, \geq)$ est un groupe abélien totalement ordonné.
\end{lemma}

\begin{proof}
Démonstration omise, mais le résultat découle facilement du
Lemme \ref{lemma-valuation-ring-x-or-x-inverse}.
Remarquons que dans le cas $A = K$, on obtient le groupe nul
$\Gamma = \{0\}$ muni de son unique ordre total.
\end{proof}
```

</details>

### 14 — definition-value-group

Anglais L11986–12004 ; français L11936–11954.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11986) · FR-ALGEBRA-B17-CHOICE-0014.

Groupe des valeurs traduit value group et désigne exactement le quotient ordonné construit. Les deux domaines de définition de v sont maintenus. Discrète exige le groupe Z, pas le groupe nul d'un corps. L'isomorphisme compatible avec l'ordre usuel est conservé. La locution groupe des valeurs est justifiée ici par la construction et le sens de la source, non par une attestation verbatim prétendue dans les pages consultées.

Point particulier à relire : Pas d'attestation verbatim nouvelle de groupe des valeurs. Choix fondé sur la construction K*/A*, la source et la cohérence terminologique ; révisable.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-GROUP, FR-ALGEBRA-B17-RULE-LOGIC, FR-ALGEBRA-B17-RULE-INTEGRAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-value-group}
Let $A$ be a valuation ring.
\begin{enumerate}
\item The totally ordered abelian group $(\Gamma, \geq)$ of
Lemma \ref{lemma-valuation-group} is called the
{\it value group} of the valuation ring $A$.
\item The map $v : A - \{0\} \to \Gamma$ and also $v : K^* \to \Gamma$ is
called the {\it valuation} associated to $A$.
\item The valuation ring $A$ is called a {\it discrete valuation ring}
if $\Gamma \cong \mathbf{Z}$.
\end{enumerate}
\end{definition}

\noindent
Note that if $\Gamma \cong \mathbf{Z}$ then there is a unique such
isomorphism such that $1 \geq 0$. If the isomorphism is chosen in this
way, then the ordering becomes the usual ordering of the integers.
```

Français restauré :
```tex
\begin{definition}
\label{definition-value-group}
Soit $A$ un anneau de valuation.
\begin{enumerate}
\item Le groupe abélien totalement ordonné $(\Gamma, \geq)$ du
Lemme \ref{lemma-valuation-group} est appelé le
{\it groupe des valeurs} de l'anneau de valuation $A$.
\item L'application $v : A - \{0\} \to \Gamma$ et aussi $v : K^* \to \Gamma$ est
appelée la {\it valuation} associée à $A$.
\item L'anneau de valuation $A$ est appelé un {\it anneau de valuation discrète}
si $\Gamma \cong \mathbf{Z}$.
\end{enumerate}
\end{definition}

\noindent
Remarquons que si $\Gamma \cong \mathbf{Z}$, il existe un unique isomorphisme de ce type
tel que $1 \geq 0$. Si l'isomorphisme est choisi de cette manière,
l'ordre devient l'ordre usuel des entiers.
```

</details>

### 15 — lemma-properties-valuation

Anglais L12005–12019 ; français L11955–11969.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12005) · FR-ALGEBRA-B17-CHOICE-0015.

Le domaine de v exclut zéro. Les unités, l'additivité du produit et l'inégalité avec le minimum restent exacts ; la clause a+b non nul est essentielle et conservée. Dat p.52 imprime max, contrairement à la source Stacks ; cette coquille de la référence linguistique n'est pas importée.

Point particulier à relire : La référence française imprime max au lieu de min. Elle atteste des termes, non une autorité permettant de changer l'inégalité de Stacks.

Règles : FR-ALGEBRA-B17-RULE-VALUATION.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-properties-valuation}
Let $A$ be a valuation ring. The valuation $v : A -\{0\} \to \Gamma_{\geq 0}$
has the following properties:
\begin{enumerate}
\item $v(a) = 0 \Leftrightarrow a \in A^*$,
\item $v(ab) = v(a) + v(b)$,
\item $v(a + b) \geq \min(v(a), v(b))$ provided $a + b \not = 0$.
\end{enumerate}
\end{lemma}

\begin{proof}
Omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-properties-valuation}
Soit $A$ un anneau de valuation. La valuation $v : A -\{0\} \to \Gamma_{\geq 0}$
possède les propriétés suivantes :
\begin{enumerate}
\item $v(a) = 0 \Leftrightarrow a \in A^*$,
\item $v(ab) = v(a) + v(b)$,
\item $v(a + b) \geq \min(v(a), v(b))$ pourvu que $a + b \not = 0$.
\end{enumerate}
\end{lemma}

\begin{proof}
Démonstration omise.
\end{proof}
```

</details>

### 16 — lemma-characterize-valuation-ring

Anglais L12020–12041 ; français L11970–11991.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12020) · FR-ALGEBRA-B17-CHOICE-0016.

Deux occurrences de domaine local deviennent anneau local intègre. Finitely generated est développé en engendré par un nombre fini d'éléments ; il ne signifie pas que l'idéal est un ensemble fini. L'équivalence, le choix d'un générateur de valuation minimale et la conclusion par une unité sont complets. Les cas nuls implicitement écartés dans la preuve source sont signalés pour la lecture, sans ajouter une démonstration.

Point particulier à relire : La preuve choisit v(f_i) et simplifie par h sans détailler les cas nuls. Ceux-ci sont élémentaires, mais l'édition fidèle ne les ajoute pas ; ne pas compter cette note de lecture comme une réfutation du critère.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-DOMAIN, FR-ALGEBRA-B17-RULE-IDEAL, FR-ALGEBRA-B17-RULE-INTEGRAL, FR-ALGEBRA-B17-RULE-ORDER.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-valuation-ring}
Let $A$ be a ring. The following are equivalent
\begin{enumerate}
\item $A$ is a valuation ring,
\item $A$ is a local domain and every finitely generated
ideal of $A$ is principal.
\end{enumerate}
\end{lemma}

\begin{proof}
Assume $A$ is a valuation ring and let $f_1, \ldots, f_n \in A$.
Choose $i$ such that $v(f_i)$ is minimal among $v(f_j)$.
Then $(f_i) = (f_1, \ldots, f_n)$. Conversely, assume $A$ is
a local domain and every finitely generated ideal of $A$ is principal.
Pick $f, g \in A$ and write $(f, g) = (h)$. Then $f = ah$ and $g = bh$
and $h = cf + dg$ for some $a, b, c, d \in A$. Thus $ac + bd = 1$
and we see that either $a$ or $b$ is a unit, i.e., either
$g/f$ or $f/g$ is an element of $A$. This shows $A$ is a valuation ring
by Lemma \ref{lemma-x-or-x-inverse-valuation-ring}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-characterize-valuation-ring}
Soit $A$ un anneau. Les assertions suivantes sont équivalentes
\begin{enumerate}
\item $A$ est un anneau de valuation,
\item $A$ est un anneau local intègre et tout idéal
de $A$ engendré par un nombre fini d'éléments est principal.
\end{enumerate}
\end{lemma}

\begin{proof}
Supposons que $A$ soit un anneau de valuation et soient $f_1, \ldots, f_n \in A$.
Choisissons $i$ tel que $v(f_i)$ soit minimal parmi les $v(f_j)$.
Alors $(f_i) = (f_1, \ldots, f_n)$. Réciproquement, supposons que $A$ soit
un anneau local intègre et que tout idéal de $A$ engendré par un nombre fini d'éléments soit principal.
Prenons $f, g \in A$ et écrivons $(f, g) = (h)$. Alors $f = ah$ et $g = bh$
et $h = cf + dg$ pour certains $a, b, c, d \in A$. Ainsi $ac + bd = 1$
et nous voyons que $a$ ou $b$ est une unité, c'est-à-dire que $g/f$
ou $f/g$ appartient à $A$. Cela montre que $A$ est un anneau de valuation
par le Lemme \ref{lemma-x-or-x-inverse-valuation-ring}.
\end{proof}
```

</details>

### 17 — lemma-valuation-valuation-ring

Anglais L12042–12083 ; français L11992–12033.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12042) · FR-ALGEBRA-B17-CHOICE-0017.

Le groupe des valeurs est l'image de v, pas nécessairement tout Γ. Les ensembles définissant l'anneau, l'idéal maximal et les unités conservent respectivement ≥0, >0 et =0, ainsi que les domaines K/K*. Les trois or→ou dans cette paire, dont celui du paragraphe définissant les idéaux de Γ, sont des traductions de connecteurs dans les formules, sans changement symbolique. Un idéal de Γ est ici une partie supérieure positive, non un sous-groupe.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-GROUP, FR-ALGEBRA-B17-RULE-IDEAL, FR-ALGEBRA-B17-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-valuation-valuation-ring}
Let $(\Gamma, \geq)$ be a totally ordered abelian group.
Let $K$ be a field. Let $v : K^* \to \Gamma$ be a homomorphism
of abelian groups such that $v(a + b) \geq \min(v(a), v(b))$ for
$a, b \in K$ with $a, b, a + b$ not zero. Then
$$
A =
\{
x \in K \mid x = 0 \text{ or } v(x) \geq 0
\}
$$
is a valuation ring with value group $\Im(v) \subset \Gamma$,
with maximal ideal
$$
\mathfrak m =
\{
x \in K \mid x = 0 \text{ or } v(x) > 0
\}
$$
and with group of units
$$
A^* =
\{
x \in K^* \mid v(x) = 0
\}.
$$
\end{lemma}

\begin{proof}
Omitted.
\end{proof}

\noindent
Let $(\Gamma, \geq)$ be a totally ordered abelian group.
An {\it ideal of $\Gamma$} is a subset $I \subset \Gamma$ such
that all elements of $I$ are $\geq 0$ and $\gamma \in I$,
$\gamma' \geq \gamma$ implies $\gamma' \in I$. We say that such
an ideal is {\it prime} if $0 \not \in I$ and if
$\gamma + \gamma' \in I, \gamma, \gamma' \geq 0
\Rightarrow \gamma \in I \text{ or } \gamma' \in I$.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-valuation-valuation-ring}
Soit $(\Gamma, \geq)$ un groupe abélien totalement ordonné.
Soit $K$ un corps. Soit $v : K^* \to \Gamma$ un homomorphisme
de groupes abéliens tel que $v(a + b) \geq \min(v(a), v(b))$ pour
$a, b \in K$ avec $a, b, a + b$ non nuls. Alors
$$
A =
\{
x \in K \mid x = 0 \text{ ou } v(x) \geq 0
\}
$$
est un anneau de valuation de groupe des valeurs $\Im(v) \subset \Gamma$,
d'idéal maximal
$$
\mathfrak m =
\{
x \in K \mid x = 0 \text{ ou } v(x) > 0
\}
$$
et de groupe des unités
$$
A^* =
\{
x \in K^* \mid v(x) = 0
\}.
$$
\end{lemma}

\begin{proof}
Démonstration omise.
\end{proof}

\noindent
Soit $(\Gamma, \geq)$ un groupe abélien totalement ordonné.
Un {\it idéal de $\Gamma$} est un sous-ensemble $I \subset \Gamma$ tel
que tous les éléments de $I$ soient $\geq 0$ et que, si $\gamma \in I$,
$\gamma' \geq \gamma$ implique $\gamma' \in I$. Nous disons qu'un tel
idéal est {\it premier} si $0 \not \in I$ et si
$\gamma + \gamma' \in I, \gamma, \gamma' \geq 0
\Rightarrow \gamma \in I \text{ ou } \gamma' \in I$.
```

</details>

### 18 — lemma-ideals-valuation-ring

Anglais L12084–12095 ; français L12034–12045.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12084) · FR-ALGEBRA-B17-CHOICE-0018.

La correspondance 1−1 est une bijection préservant l'inclusion et les idéaux premiers. L'idéal vide de Γ correspond à l'idéal nul de A ; 0 hors de I définit un idéal premier de Γ. Aucun sens habituel différent du mot idéal n'est importé dans cette définition particulière.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-IDEAL, FR-ALGEBRA-B17-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ideals-valuation-ring}
Let $A$ be a valuation ring.
Ideals in $A$ correspond $1 - 1$ with ideals of $\Gamma$.
This bijection is inclusion preserving, and maps prime
ideals to prime ideals.
\end{lemma}

\begin{proof}
Omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ideals-valuation-ring}
Soit $A$ un anneau de valuation.
Les idéaux de $A$ correspondent $1 - 1$ aux idéaux de $\Gamma$.
Cette bijection respecte l'inclusion et envoie les idéaux premiers
sur les idéaux premiers.
\end{lemma}

\begin{proof}
Démonstration omise.
\end{proof}
```

</details>

### 19 — lemma-valuation-ring-Noetherian-discrete

Anglais L12096–12148 ; français L12046–12077.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12096) · FR-ALGEBRA-B17-CHOICE-0019.

Le critère conserve la disjonction anneau de valuation discrète ou corps. PID est traduit par anneau principal, attesté par Ducros. La preuve utilise la condition de chaîne ascendante et le plus petit élément strictement positif ; ni les inégalités ni le dernier indice ne changent. La liste I_n de la première partie omet littéralement l'idéal nul pour n entier fini : réserve séparée, sans correction clandestine ni remise en cause du théorème.

Point particulier à relire : PID est un sigle anglais restant à traduire. La réserve sur l'idéal nul concerne une phrase de preuve, pas la validité de l'équivalence.

Règles : FR-ALGEBRA-B17-RULE-VALUATION, FR-ALGEBRA-B17-RULE-GROUP, FR-ALGEBRA-B17-RULE-IDEAL, FR-ALGEBRA-B17-RULE-LOGIC, FR-ALGEBRA-B17-RULE-ORDER.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-valuation-ring-Noetherian-discrete}
A valuation ring is Noetherian if and only if it is
a discrete valuation ring or a field.
\end{lemma}

\begin{proof}
Suppose $A$ is a discrete valuation ring
with valuation $v : A \setminus \{0\} \to \mathbf{Z}$
normalized so that $\Im(v) = \mathbf{Z}_{\geq 0}$.
By Lemma \ref{lemma-ideals-valuation-ring} the ideals of $A$ are the subsets
$I_n = \{0\} \cup v^{-1}(\mathbf{Z}_{\geq n})$. It is clear
that any element $x \in A$ with $v(x) = n$ generates $I_n$.
Hence $A$ is a PID so certainly Noetherian.

\medskip\noindent
Suppose $A$ is a Noetherian valuation ring with value group $\Gamma$.
By Lemma \ref{lemma-ideals-valuation-ring} we see the ascending chain
condition holds for ideals in $\Gamma$.
We may assume $A$ is not a field, i.e., there is a $\gamma \in \Gamma$
with $\gamma > 0$. Applying the ascending chain condition to the subsets
$\gamma + \Gamma_{\geq 0}$ with $\gamma > 0$ we see
there exists a smallest element $\gamma_0$ which is bigger than $0$.
Let $\gamma \in \Gamma$ be an element $\gamma > 0$. Consider the sequence
of elements $\gamma$, $\gamma - \gamma_0$, $\gamma - 2\gamma_0$,
etc. By the ascending chain condition these cannot all be $> 0$.
Let $\gamma - n \gamma_0$ be the last one $\geq 0$. By minimality
of $\gamma_0$ we see that $0 = \gamma - n \gamma_0$. Hence $\Gamma$
is a cyclic group as desired.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-valuation-ring-Noetherian-discrete}
Un anneau de valuation est noethérien si et seulement si c'est
un anneau de valuation discrète ou un corps.
\end{lemma}

\begin{proof}
Supposons que $A$ soit un anneau de valuation discrète
de valuation $v : A \setminus \{0\} \to \mathbf{Z}$
normalisée de sorte que $\Im(v) = \mathbf{Z}_{\geq 0}$.
Par le Lemme \ref{lemma-ideals-valuation-ring}, les idéaux de $A$ sont les sous-ensembles
$I_n = \{0\} \cup v^{-1}(\mathbf{Z}_{\geq n})$. Il est clair
que tout élément $x \in A$ tel que $v(x) = n$ engendre $I_n$.
Ainsi $A$ est un anneau principal, donc certainement noethérien.

\medskip\noindent
Supposons que $A$ soit un anneau de valuation noethérien de groupe des valeurs $\Gamma$.
Par le Lemme \ref{lemma-ideals-valuation-ring}, la condition de chaîne ascendante
est satisfaite pour les idéaux de $\Gamma$.
Nous pouvons supposer que $A$ n'est pas un corps, c'est-à-dire qu'il existe un $\gamma \in \Gamma$
tel que $\gamma > 0$. En appliquant la condition de chaîne ascendante aux sous-ensembles
$\gamma + \Gamma_{\geq 0}$ avec $\gamma > 0$, nous voyons
qu'il existe un plus petit élément $\gamma_0$ strictement supérieur à $0$.
Soit $\gamma \in \Gamma$ un élément tel que $\gamma > 0$. Considérons la suite
des éléments $\gamma$, $\gamma - \gamma_0$, $\gamma - 2\gamma_0$,
etc. Par la condition de chaîne ascendante, ils ne peuvent pas tous être $> 0$.
Soit $\gamma - n \gamma_0$ le dernier qui soit $\geq 0$. Par minimalité
de $\gamma_0$, nous voyons que $0 = \gamma - n \gamma_0$. Ainsi $\Gamma$
est un groupe cyclique, comme voulu.
\end{proof}
```

</details>

## Réserves sur la source anglaise

### FR-ALGEBRA-B17-SOURCE-NOTE-0001

[Source L11894](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11894) — lemma-make-valuation-rings.

```tex
localization $A_\mathfrak p$ and in fact any localization of $A$.
```

Le membre toute localisation demande une réserve de non-nullité selon les définitions de ce témoin. La définition officielle d'une partie multiplicative (L1041–1047) exige 1 et la stabilité multiplicative, mais n'exclut pas 0. Pour A=k corps et S={0,1}, S^{-1}k est l'anneau nul, donc n'est pas un anneau intègre ni un anneau de valuation selon la définition L11729–11744. Le localisé en un idéal premier reste non nul. Correction candidate minimale : any nonzero localization. Réserve adverse : une convention tacite limitant cette phrase aux localisations non nulles expliquerait le raccourci, mais elle n'est pas déclarée ici. Aucune correction n'est appliquée au français ou à l'anglais.

Confiance éditoriale motivée, non probabilité calibrée. Proposition non admise et non dédupliquée globalement ; aucune découverte originale revendiquée.

[Définition officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1041) — algebra.tex L1041–1047 ; SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.

```tex
\begin{definition}
\label{definition-multiplicative-subset}
Let $R$ be a ring, $S$ a subset of $R$.
We say $S$ is a {\it multiplicative subset of $R$} if
$1\in S$ and $S$ is closed
under multiplication, i.e., $s, s' \in S \Rightarrow ss' \in S$.
\end{definition}
```

### FR-ALGEBRA-B17-SOURCE-NOTE-0002

[Source L12106](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12106) — lemma-valuation-ring-Noetherian-discrete.

```tex
By Lemma \ref{lemma-ideals-valuation-ring} the ideals of $A$ are the subsets
$I_n = \{0\} \cup v^{-1}(\mathbf{Z}_{\geq n})$. It is clear
```

Pour n entier fini positif ou nul, I_n contient un élément de valuation n et ne vaut pas l'idéal nul. L'énumération littérale de tous les idéaux omet donc (0). Le critère noethérien reste correct, l'idéal nul étant principal. Correction candidate minimale : the nonzero ideals, ou ajouter explicitement (0). Réserve adverse : un indice ∞ ou le traitement tacite du cas nul rendrait la phrase acceptable comme raccourci, mais ni l'un ni l'autre n'est déclaré. Le texte traduit conserve la phrase de la source ; cette observation n'est pas une réfutation du théorème.

Confiance éditoriale motivée, non probabilité calibrée. Proposition non admise et non dédupliquée globalement ; aucune découverte originale revendiquée.

## Contrôles et suite

Les 347 régions mathématiques du lot concordent après trois traductions exactes or→ou. Le préfixe compte 8 640 régions et vingt-cinq exceptions linguistiques exactes, dont vingt-deux antérieures. L’égalité brute sans ces exceptions n’est pas revendiquée.

Ce lot ne contient ni citation bibliographique ni intitulé facultatif de lemme. Labels, renvois, clés bibliographiques du fichier entier, entrées, contrôles TeX, environnements et items sont préservés. Aucune région mathématique du français entier ne change depuis le lot précédent.

Les opérations inverses retrouvent le lot précédent puis le témoin public conservé. Les octets du préfixe déjà relu et ceux du suffixe encore non relu sont inchangés. Les contrôles mécaniques complètent la lecture sémantique et ne la remplacent pas.

Prochaine lecture : Autres anneaux noethériens, anglais L12149 / français L12078. Aucun nouveau PDF, aucune publication et aucune certification globale du chapitre ou de l’édition dans ce lot.

