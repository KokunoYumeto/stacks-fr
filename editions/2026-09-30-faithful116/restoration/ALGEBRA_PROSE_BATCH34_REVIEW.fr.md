# Suites régulières

## Résultat et portée

La section entière est comparée : anglais L16587–16854 et français L16353–16620, 268 lignes chacun et onze paires complètes. 153 occurrences de règles sont contextualisées, non un décompte de tous les mots. Couverture continue : 68 sections, 611 paires et 6028 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Deux corrections de langue rendent explicite le sujet suite et réparent un accord : les éléments f2,…,fr ne sont pas plusieurs suites ; les éléments a,b forment une suite. Le sens et toutes les formules restent identiques. La condition de quotient final non nul, l’ordre et chaque hypothèse source sont préservés. Le LaTeX est réversible, les versions antérieures conservées.

Deux observations anglaises restent séparées : un dénominateur de quotient écrit sans son module M, et x_i au lieu de x_{i+1} dans une étape polynomiale. La première est une réserve de notation ; un contre-exemple explicite motive la seconde. Aucune de ces suggestions ne corrige silencieusement le français.

Lecture produite par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. Le canon est consulté rétrospectivement, non présenté comme consulté lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch34.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH33_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH34_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH34_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH34_OCCURRENCES.json) · [Opérations](ALGEBRA_PROSE_BATCH34_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH34_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH34_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH34_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH34_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH34_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Christian Peskine — Introduction algébrique à la géométrie projective

[Source consultée](https://perso.univ-rennes1.fr/matthieu.romagny/M2_0708/bouquin.pdf) · [Fichier conservé](canon-consulted/fr-algebra/peskine-geometrie-projective-2007.pdf)

Pages PDF138–143 /imprimées137–142 intégralement lues ; PDF138 rendu et visuellement inspecté. Section16.1, proposition16.1, définition16.3, théorèmes16.4–16.5, lemme16.6 et preuve continuée PDF139, définition16.7, proposition16.9 et suites exactes, lemme16.17 et continuation.

Attestations courtes : « Suites régulières », « suite M-régulière », « profondeur », « non diviseur de 0 ».

Le titre et la définition attestent suite régulière, suite M-régulière et le critère d'injectivité sur les quotients successifs. La preuve du lemme16.6 atteste le raisonnement de permutation par Nakayama. Le vocabulaire de profondeur, des suites exactes et des quotients apparaît dans les passages effectivement lus.

Limites : La définition16.3 est locale, noethérienne et de type fini, avec éléments dans l'idéal maximal. La non-nullité des quotients suit dans ce cadre de Nakayama ; elle ne justifie pas de supprimer la condition explicite de Stacks pour un module général. Les pages lues n'attestent pas mot pour mot le slogan préservent et reflètent, ni tous les lemmes de Stacks. Aucune consultation du volume entier ni consultation lors de la traduction initiale n'est revendiquée.

SHA-256 : C84D597457282B22B993F523791F4A3E391A74554FF76F7F49878640789435BA.

## Modifications et motifs

Deux corrections de sujet et d’accord, sans changement de sens. Les autres formulations sont conservées après lecture complète. La liste est un seul objet ordonné, régulier pour deux modules dans le premier passage. Les observations source ne deviennent pas des modifications de la traduction.

### FR-ALGEBRA-B34-REPAIR-0001

Anglais L16774 ; français L16540.

Avant :
```tex
Alors, par récurrence, les éléments $f_2, \ldots, f_r$ sont des suites régulières sur $M/f_1M$ et
```

Après :
```tex
Alors, par récurrence, la suite $f_2, \ldots, f_r$ est régulière sur $M/f_1M$ et
```

L'équivalence avec des exposants strictement positifs et les deux récurrences, sur r puis e, sont comparées en entier. Une phrase est corrigée : la liste f2,…,fr est une seule suite régulière pour chacun des deux modules, non des éléments qui seraient plusieurs suites. Formules, flèches, quotients et implication réciproque ne changent pas. La non-nullité du quotient pour les puissances n'est pas supprimée ; dans le cas d'un élément, M=fM équivaut à M=f^eM. Les détails omis restent omis dans la traduction.

Les éléments ne sont pas chacun une suite : le sujet devient la suite et le verbe est au singulier. Même liste et mêmes deux modules. Aucune substitution d'indice ni ajout de preuve.

### FR-ALGEBRA-B34-REPAIR-0002

Anglais L16812 ; français L16578.

Avant :
```tex
$a, b \in R$ est une suite régulière et si $b$ est un non-diviseur de zéro, alors
```

Après :
```tex
les éléments $a, b \in R$ forment une suite régulière et si $b$ est un non-diviseur de zéro, alors
```

Les trois conditions restent distinctes : toutes permutations, toutes sous-suites dans l'ordre donné, et suite dans l'anneau de polynômes. L'idéal unité est explicitement exclu. Toute la preuve des permutations et de la décomposition par multi-indices est comparée. On remplace a,b est une suite par les éléments a,b forment une suite : accord et sujet rendus corrects, même proposition. L'indice erroné x_i dans la source reste littéral et séparément motivé ; pas de réparation mathématique cachée.

Accord forment appliqué aux deux éléments ; la liste b,a peut ensuite servir de sujet singulier collectif. La phrase sur E entièrement positif ne mentionne que la sous-suite initiale ; la condition pour tous E assure aussi les sous-suites sélectionnées. Ce détail elliptique n'est pas déclaré faux. L'erreur d'indice x_i est seule enregistrée comme défaut mathématique dans ce passage.

## Observations séparées sur la source

Deux observations sont distinctes : quotient de module abrégé et indice de variable incorrect. Le français reste conforme au témoin officiel. Un contre-exemple est donné pour le second ; le premier est qualifié de notation. Aucune admission, déduplication globale ou première découverte n’est revendiquée.

### lemma-permute-xi

[Anglais officiel L16671](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16671) · FR-ALGEBRA-B34-SOURCE-NOTE-0001.

```tex
just did applied to the module $M/(x_1, \ldots, x_{i-2})$
```

Le dénominateur affiché est un idéal de R, tandis que le quotient est celui du module M. Le cas de longueur2 doit s'appliquer à M/(x1,…,x_{i-2})M, quotient par le sous-module engendré. Ajouter le M final explicite ce type. L'écriture courte peut être une convention d'abus de notation ; il ne s'agit pas d'accuser le lemme d'être faux. Le français garde exactement le raccourci source.

Confiance forte sur le sous-module requis ; réserve de notation, non défaut du résultat ni nouvelle admission.

### lemma-regular-sequence-in-polynomial-ring

[Anglais officiel L16836](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16836) · FR-ALGEBRA-B34-SOURCE-NOTE-0002.

```tex
Hence $f_{i + 1}x_i$ is a nonzerodivisor on this if
```

L'étape suivante de la suite f1x1,…,frxr utilise f_{i+1}x_{i+1}, pas f_{i+1}x_i. Contre-exemple à la phrase littérale : R=k[a,b], f1=a, f2=b, i=1. Dans R[x1,x2]/(a x1), l'élément a est non nul (évaluer x1 à0 le conserve), mais (b x1)a=0. Pourtant b est un non-diviseur de zéro dans R et R/(a), les deux possibilités R/I_E. L'idéal (a,b) est propre. L'indice x_i rend donc la phrase d'équivalence fausse dans ce cas ; remplacer seulement par x_{i+1} rétablit l'étape de multiplication correspondant à la suite annoncée. Le français conserve x_i, observation et contre-exemple restant séparés.

Confiance forte, contre-exemple explicite et indice déterminé par l'énoncé. Aucune mutation du témoin, admission, déduplication globale ou première découverte.

## Règles contextualisées

### FR-ALGEBRA-B34-RULE-REGULAR

Suite désigne une liste ordonnée ; régularité et non-diviseur de zéro conservent le module et le quotient concernés. La condition de quotient final non nul n'est pas absorbée dans une autre convention.

Canon : FR-ALGEBRA-B34-CANON-PESKINE.

### FR-ALGEBRA-B34-RULE-MODULE

Anneaux, modules, noyaux et quotients restent distincts. Les restrictions de type fini/noethérien/local portent sur les mêmes objets que dans la source. Le slogan de platitude est justifié directement et son absence d'attestation exacte est signalée.

Canon : FR-ALGEBRA-B34-CANON-PESKINE.

### FR-ALGEBRA-B34-RULE-SEQUENCE

Suites exactes et listes régulières ne sont pas confondues. Chaque récurrence, permutation, sous-suite et puissance conserve ses quantificateurs et son ordre.

Canon : FR-ALGEBRA-B34-CANON-PESKINE.

### FR-ALGEBRA-B34-RULE-LOGIC

Les quantificateurs, équivalences, hypothèses et implications sont contrôlés dans les onze passages complets ; l'analyse de fidélité ne prétend pas à une attestation externe de chaque connecteur.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-regular-sequences

Anglais L16587–16592 ; français L16353–16358.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16587) · FR-ALGEBRA-B34-CHOICE-0001.

Suites régulières est directement attesté au titre16.1 de Peskine. L'introduction annonce des propriétés élémentaires, sans prétendre à une théorie complète.

Règles : FR-ALGEBRA-B34-RULE-REGULAR.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Regular sequences}
\label{section-regular-sequences}

\noindent
In this section we develop some basic properties of regular sequences.
```

Français restauré :
```tex
\section{Suites régulières}
\label{section-regular-sequences}

\noindent
Dans cette section, nous établissons quelques propriétés élémentaires des suites régulières.
```

</details>

### 02 — definition-regular-sequence

Anglais L16593–16619 ; français L16359–16385.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16593) · FR-ALGEBRA-B34-CHOICE-0002.

Lecture de la définition et de toute la mise en garde. Suite M-régulière garde l'ordre, les quotients successifs et le quotient final non nul. Peskine définition16.3 atteste le vocabulaire sous des hypothèses locales/noethériennes/de type fini ; celles-ci ne sont pas importées dans la définition générale de Stacks. La variante sans condition de non-nullité et la restriction à l'idéal maximal pour la profondeur restent expressément distinguées.

Point particulier à relire : Le canon restreint ne permet pas de retirer le quotient final non nul ni d'ajouter local/noethérien/type fini à la définition source. Consultation rétrospective explicitement déclarée.

Règles : FR-ALGEBRA-B34-RULE-REGULAR, FR-ALGEBRA-B34-RULE-MODULE, FR-ALGEBRA-B34-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-regular-sequence}
Let $R$ be a ring. Let $M$ be an $R$-module. A sequence of elements
$f_1, \ldots, f_r$ of $R$ is called an {\it $M$-regular sequence}
if the following conditions hold:
\begin{enumerate}
\item $f_i$ is a nonzerodivisor on
$M/(f_1, \ldots, f_{i - 1})M$
for each $i = 1, \ldots, r$, and
\item the module $M/(f_1, \ldots, f_r)M$ is not zero.
\end{enumerate}
If $I$ is an ideal of $R$ and $f_1, \ldots, f_r \in I$
then we call $f_1, \ldots, f_r$ an {\it $M$-regular sequence
in $I$}. If $M = R$, we call $f_1, \ldots, f_r$ simply a
{\it regular sequence} (in $I$).
\end{definition}

\noindent
Please pay attention to the fact that the definition depends on the order
of the elements $f_1, \ldots, f_r$ (see examples below). Some papers/books
drop the requirement that the module $M/(f_1, \ldots, f_r)M$ is nonzero.
This has the advantage that being a regular sequence is preserved under
localization. However, we will use this definition mainly to define the
depth of a module in case $R$ is local; in that case the $f_i$ are required
to be in the maximal ideal -- a condition which is not preserved under going
from $R$ to a localization $R_\mathfrak p$.
```

Français restauré :
```tex
\begin{definition}
\label{definition-regular-sequence}
Soit $R$ un anneau. Soit $M$ un $R$-module. Une suite d'éléments
$f_1, \ldots, f_r$ de $R$ est appelée une {\it suite $M$-régulière}
si les conditions suivantes sont satisfaites :
\begin{enumerate}
\item $f_i$ est un non-diviseur de zéro sur
$M/(f_1, \ldots, f_{i - 1})M$
pour tout $i = 1, \ldots, r$, et
\item le module $M/(f_1, \ldots, f_r)M$ n'est pas nul.
\end{enumerate}
Si $I$ est un idéal de $R$ et si $f_1, \ldots, f_r \in I$,
nous appelons $f_1, \ldots, f_r$ une {\it suite $M$-régulière
dans $I$}. Si $M = R$, nous appelons simplement $f_1, \ldots, f_r$ une
{\it suite régulière} (dans $I$).
\end{definition}

\noindent
Notons bien que la définition dépend de l'ordre
des éléments $f_1, \ldots, f_r$ (voir les exemples ci-dessous). Certains articles ou livres
ne demandent pas que le module $M/(f_1, \ldots, f_r)M$ soit non nul.
Cela présente l'avantage que la propriété d'être une suite régulière est préservée par
localisation. Cependant, nous utiliserons surtout cette définition pour définir la
profondeur d'un module lorsque $R$ est local ; dans ce cas, les $f_i$ doivent
appartenir à l'idéal maximal, condition qui n'est pas préservée lorsqu'on passe
de $R$ à une localisation $R_\mathfrak p$.
```

</details>

### 03 — example-global-regular

Anglais L16620–16626 ; français L16386–16392.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16620) · FR-ALGEBRA-B34-CHOICE-0003.

L'exemple polynomial garde les deux listes ordonnées et leur différence de régularité. La propriété n'est pas transformée en propriété invariante par permutation sur tout anneau.

Règles : FR-ALGEBRA-B34-RULE-MODULE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-global-regular}
Let $k$ be a field. In the ring $k[x, y, z]$
the sequence $x, y(1-x), z(1-x)$ is regular
but the sequence $y(1-x), z(1-x), x$ is not.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-global-regular}
Soit $k$ un corps. Dans l'anneau $k[x, y, z]$,
la suite $x, y(1-x), z(1-x)$ est régulière,
mais la suite $y(1-x), z(1-x), x$ ne l'est pas.
\end{example}
```

</details>

### 04 — example-local-regular

Anglais L16627–16637 ; français L16393–16403.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16627) · FR-ALGEBRA-B34-CHOICE-0004.

Tous les générateurs de l'idéal, la suite infinie et les deux assertions sur x,y sont comparés. L'exemple local est non noethérien : il ne contredit pas le lemme suivant. Le passage à l'idéal maximal est conservé, sans ajout d'une hypothèse noethérienne.

Règles : FR-ALGEBRA-B34-RULE-REGULAR, FR-ALGEBRA-B34-RULE-MODULE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-local-regular}
Let $k$ be a field. Consider the ring
$k[x, y, w_0, w_1, w_2, \ldots]/I$
where $I$ is generated by $yw_i$, $i = 0, 1, 2, \ldots$ and
$w_i - xw_{i + 1}$, $i = 0, 1, 2, \ldots$.
The sequence $x, y$ is regular, but $y$ is a zerodivisor.
Moreover you can localize at the maximal ideal
$(x, y, w_i)$ and still get an example.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-local-regular}
Soit $k$ un corps. Considérons l'anneau
$k[x, y, w_0, w_1, w_2, \ldots]/I$
où $I$ est engendré par les $yw_i$, $i = 0, 1, 2, \ldots$, et les
$w_i - xw_{i + 1}$, $i = 0, 1, 2, \ldots$.
La suite $x, y$ est régulière, mais $y$ est un diviseur de zéro.
On peut de plus localiser en l'idéal maximal
$(x, y, w_i)$ et obtenir encore un exemple.
\end{example}
```

</details>

### 05 — lemma-permute-xi

Anglais L16638–16674 ; français L16404–16440.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16638) · FR-ALGEBRA-B34-CHOICE-0005.

Énoncé et preuve entière comparés, y compris le noyau K, les deux injectivités, Nakayama et les transpositions adjacentes. Peskine lemme16.6 fournit une attestation de la formulation et un raisonnement analogue, dans le même contexte local noethérien et de type fini. La condition de quotient non nul force ici les éléments dans l'idéal maximal. Le dénominateur final sans M demeure littéral et est noté séparément comme raccourci de notation.

Point particulier à relire : M/(x1,…,x_{i-2}) est conservé comme dans la source ; la suggestion de compléter le dénominateur par M est une clarification de notation séparée, pas une modification de la traduction.

Règles : FR-ALGEBRA-B34-RULE-REGULAR, FR-ALGEBRA-B34-RULE-MODULE, FR-ALGEBRA-B34-RULE-SEQUENCE, FR-ALGEBRA-B34-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-permute-xi}
Let $R$ be a local Noetherian ring.
Let $M$ be a finite $R$-module.
Let $x_1, \ldots, x_c$ be an $M$-regular sequence.
Then any permutation of the $x_i$ is a regular
sequence as well.
\end{lemma}

\begin{proof}
First we do the case $c = 2$.
Consider $K \subset M$ the kernel of $x_2 : M \to M$.
For any $z \in K$ we know that $z = x_1 z'$
for some $z' \in M$ because
$x_2$ is a nonzerodivisor on $M/x_1M$.
Because $x_1$ is a nonzerodivisor on $M$ we see that $x_2 z' = 0$
as well. Hence $x_1 : K \to K$ is surjective.
Thus $K = 0$ by Nakayama's Lemma \ref{lemma-NAK}.
Next, consider multiplication by $x_1$ on $M/x_2M$.
If $z \in M$ maps to an element $\overline{z} \in M/x_2M$
in the kernel of this map, then $x_1 z = x_2 y$ for some $y \in M$.
But then since $x_1, x_2$ is a regular sequence we see that
$y = x_1 y'$ for some $y' \in M$. Hence $x_1 ( z - x_2 y' ) =0$
and hence $z = x_2 y'$ and hence $\overline{z} = 0$ as desired.

\medskip\noindent
For the general case, observe that any permutation is
a composition of transpositions of adjacent indices.
Hence it suffices to prove that
$$
x_1, \ldots, x_{i-2}, x_i, x_{i-1}, x_{i + 1}, \ldots, x_c
$$
is an $M$-regular sequence. This follows from the case we
just did applied to the module $M/(x_1, \ldots, x_{i-2})$
and the length $2$ regular sequence $x_{i-1}, x_i$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-permute-xi}
Soit $R$ un anneau local noethérien.
Soit $M$ un $R$-module de type fini.
Soit $x_1, \ldots, x_c$ une suite $M$-régulière.
Alors toute permutation des $x_i$ est elle aussi une suite
régulière.
\end{lemma}

\begin{proof}
Traitons d'abord le cas $c = 2$.
Considérons le noyau $K \subset M$ de $x_2 : M \to M$.
Pour tout $z \in K$, on sait que $z = x_1 z'$
pour un certain $z' \in M$, car
$x_2$ est un non-diviseur de zéro sur $M/x_1M$.
Comme $x_1$ est un non-diviseur de zéro sur $M$, on a aussi $x_2 z' = 0$.
Ainsi $x_1 : K \to K$ est surjectif.
Le Lemme de Nakayama \ref{lemma-NAK} donne donc $K = 0$.
Considérons ensuite la multiplication par $x_1$ sur $M/x_2M$.
Si $z \in M$ a pour image un élément $\overline{z} \in M/x_2M$
du noyau de cette application, alors $x_1 z = x_2 y$ pour un certain $y \in M$.
Mais, puisque $x_1, x_2$ est une suite régulière, on a alors
$y = x_1 y'$ pour un certain $y' \in M$. Ainsi $x_1 ( z - x_2 y' ) =0$,
puis $z = x_2 y'$, et donc $\overline{z} = 0$, comme voulu.

\medskip\noindent
Dans le cas général, remarquons que toute permutation est
une composée de transpositions d'indices adjacents.
Il suffit donc de démontrer que
$$
x_1, \ldots, x_{i-2}, x_i, x_{i-1}, x_{i + 1}, \ldots, x_c
$$
est une suite $M$-régulière. Cela résulte du cas que nous venons
de traiter, appliqué au module $M/(x_1, \ldots, x_{i-2})$
et à la suite régulière de longueur $2$ formée par $x_{i-1}, x_i$.
\end{proof}
```

</details>

### 06 — lemma-flat-increases-depth

Anglais L16675–16694 ; français L16441–16460.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16675) · FR-ALGEBRA-B34-CHOICE-0006.

Les deux assertions gardent leur équivalence, le caractère local/plat de l'homomorphisme et M arbitraire. Fidèlement plat traduit faithfully flat, sans changer plat en fidèlement plat dans l'hypothèse. Préservent et reflètent désigne les deux sens de l'équivalence, pas une réciproque pour tout homomorphisme plat. Aucune attestation externe exacte de ce slogan n'est revendiquée ; il est conservé sur sa justification sémantique directe.

Point particulier à relire : Préservent et reflètent : exactitude des deux sens vérifiée, mais aucune citation nouvelle n'atteste cette expression précise. Formulation conservée provisoirement sur analyse du sens ; à proposer à une relecture spécialisée sans en faire un blocage.

Règles : FR-ALGEBRA-B34-RULE-REGULAR, FR-ALGEBRA-B34-RULE-MODULE, FR-ALGEBRA-B34-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-flat-increases-depth}
\begin{slogan}
Flat local ring homomorphisms preserve and reflect regular sequences.
\end{slogan}
Let $R, S$ be local rings. Let $R \to S$ be a flat local ring homomorphism.
Let $x_1, \ldots, x_r$ be a sequence in $R$. Let $M$ be an $R$-module.
The following are equivalent
\begin{enumerate}
\item $x_1, \ldots, x_r$ is an $M$-regular sequence in $R$, and
\item the images of $x_1, \ldots, x_r$ in $S$ form a $M \otimes_R S$-regular
sequence.
\end{enumerate}
\end{lemma}

\begin{proof}
This is so because $R \to S$ is faithfully flat
by Lemma \ref{lemma-local-flat-ff}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-flat-increases-depth}
\begin{slogan}
Les homomorphismes locaux plats d'anneaux préservent et reflètent les suites régulières.
\end{slogan}
Soient $R, S$ des anneaux locaux. Soit $R \to S$ un homomorphisme local plat d'anneaux.
Soit $x_1, \ldots, x_r$ une suite dans $R$. Soit $M$ un $R$-module.
Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item $x_1, \ldots, x_r$ est une suite $M$-régulière dans $R$, et
\item les images de $x_1, \ldots, x_r$ dans $S$ forment une suite
$M \otimes_R S$-régulière.
\end{enumerate}
\end{lemma}

\begin{proof}
Cela vient de ce que $R \to S$ est fidèlement plat
d'après le Lemme \ref{lemma-local-flat-ff}.
\end{proof}
```

</details>

### 07 — lemma-regular-sequence-in-neighbourhood

Anglais L16695–16715 ; français L16461–16481.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16695) · FR-ALGEBRA-B34-CHOICE-0007.

Anneau noethérien, M de type fini, localisation en p et choix de g hors p restent exacts. Toute la preuve des noyaux de multiplication et de leur annulation sur un voisinage est comparée. La non-nullité du quotient sur R_g découle de sa localisation non nulle en p ; pas de condition supplémentaire inventée dans le texte.

Règles : FR-ALGEBRA-B34-RULE-MODULE, FR-ALGEBRA-B34-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-regular-sequence-in-neighbourhood}
Let $R$ be a Noetherian ring. Let $M$ be a finite $R$-module.
Let $\mathfrak p$ be a prime. Let $x_1, \ldots, x_r$ be a sequence
in $R$ whose image in $R_{\mathfrak p}$ forms an $M_{\mathfrak p}$-regular
sequence. Then there exists a $g \in R$, $g \not \in \mathfrak p$
such that the image of $x_1, \ldots, x_r$ in $R_g$ forms
an $M_g$-regular sequence.
\end{lemma}

\begin{proof}
Set
$$
K_i = \Ker\left(x_i : M/(x_1, \ldots, x_{i - 1})M \to
M/(x_1, \ldots, x_{i - 1})M\right).
$$
This is a finite $R$-module whose localization at $\mathfrak p$ is
zero by assumption. Hence there exists a $g \in R$, $g \not \in \mathfrak p$
such that $(K_i)_g = 0$ for all $i = 1, \ldots, r$. This $g$ works.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-regular-sequence-in-neighbourhood}
Soit $R$ un anneau noethérien. Soit $M$ un $R$-module de type fini.
Soit $\mathfrak p$ un idéal premier. Soit $x_1, \ldots, x_r$ une suite
dans $R$ dont l'image dans $R_{\mathfrak p}$ forme une suite
$M_{\mathfrak p}$-régulière. Alors il existe $g \in R$, avec $g \not \in \mathfrak p$,
tel que l'image de $x_1, \ldots, x_r$ dans $R_g$ forme
une suite $M_g$-régulière.
\end{lemma}

\begin{proof}
Posons
$$
K_i = \Ker\left(x_i : M/(x_1, \ldots, x_{i - 1})M \to
M/(x_1, \ldots, x_{i - 1})M\right).
$$
C'est un $R$-module de type fini dont la localisation en $\mathfrak p$ est
nulle par hypothèse. Il existe donc $g \in R$, avec $g \not \in \mathfrak p$,
tel que $(K_i)_g = 0$ pour tout $i = 1, \ldots, r$. Ce $g$ convient.
\end{proof}
```

</details>

### 08 — lemma-join-regular-sequences

Anglais L16716–16728 ; français L16482–16494.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16716) · FR-ALGEBRA-B34-CHOICE-0008.

La suite génératrice de I et les images régulières dans A/I restent deux objets distincts ; leur concaténation est dans A. La preuve renvoie seulement aux définitions. Aucun nouvel argument ni condition n'est ajouté.

Règles : FR-ALGEBRA-B34-RULE-REGULAR, FR-ALGEBRA-B34-RULE-MODULE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-join-regular-sequences}
Let $A$ be a ring. Let $I$ be an ideal generated by a regular
sequence $f_1, \ldots, f_n$ in $A$. Let $g_1, \ldots, g_m \in A$ be
elements whose images $\overline{g}_1, \ldots, \overline{g}_m$ form a
regular sequence in $A/I$. Then $f_1, \ldots, f_n, g_1, \ldots, g_m$
is a regular sequence in $A$.
\end{lemma}

\begin{proof}
This follows immediately from the definitions.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-join-regular-sequences}
Soit $A$ un anneau. Soit $I$ un idéal engendré par une suite régulière
$f_1, \ldots, f_n$ dans $A$. Soient $g_1, \ldots, g_m \in A$ des
éléments dont les images $\overline{g}_1, \ldots, \overline{g}_m$ forment une
suite régulière dans $A/I$. Alors la suite $f_1, \ldots, f_n, g_1, \ldots, g_m$
est régulière dans $A$.
\end{lemma}

\begin{proof}
Cela résulte immédiatement des définitions.
\end{proof}
```

</details>

### 09 — lemma-regular-sequence-short-exact-sequence

Anglais L16729–16746 ; français L16495–16512.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16729) · FR-ALGEBRA-B34-CHOICE-0009.

La suite exacte courte et les trois modules restent distincts. La régularité sur M1 et M3 entraîne celle sur M2, pas l'inverse. Le lemme du serpent fournit l'injectivité et la suite des quotients ; la récurrence et l'omission annoncée de certains détails sont préservées. Le quotient final de M2 est non nul puisqu'il surjecte sur celui de M3, non nul par hypothèse. Peskine emploie le même registre de suites exactes et de quotients, sans être invoqué comme preuve de cet énoncé général.

Point particulier à relire : Soit f1,…,fr désigne ici une liste unique, elliptique mais intelligible ; ce n'est pas traité comme une faute imposant Soient. Aucun remplacement cosmétique global.

Règles : FR-ALGEBRA-B34-RULE-MODULE, FR-ALGEBRA-B34-RULE-SEQUENCE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-regular-sequence-short-exact-sequence}
Let $R$ be a ring. Let $0 \to M_1 \to M_2 \to M_3 \to 0$
be a short exact sequence of $R$-modules. Let $f_1, \ldots, f_r \in R$.
If $f_1, \ldots, f_r$ is $M_1$-regular and $M_3$-regular, then
$f_1, \ldots, f_r$ is $M_2$-regular.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-snake}, if $f_1 : M_1 \to M_1$ and
$f_1 : M_3 \to M_3$ are injective, then so is $f_1 : M_2 \to M_2$
and we obtain a short exact sequence
$$
0 \to M_1/f_1M_1 \to M_2/f_1M_2 \to M_3/f_1M_3 \to 0
$$
The lemma follows from this and induction on $r$. Some details omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-regular-sequence-short-exact-sequence}
Soit $R$ un anneau. Soit $0 \to M_1 \to M_2 \to M_3 \to 0$
une suite exacte courte de $R$-modules. Soit $f_1, \ldots, f_r \in R$.
Si $f_1, \ldots, f_r$ est $M_1$-régulière et $M_3$-régulière, alors
$f_1, \ldots, f_r$ est $M_2$-régulière.
\end{lemma}

\begin{proof}
D'après le Lemme \ref{lemma-snake}, si $f_1 : M_1 \to M_1$ et
$f_1 : M_3 \to M_3$ sont injectifs, alors $f_1 : M_2 \to M_2$ l'est aussi,
et l'on obtient une suite exacte courte
$$
0 \to M_1/f_1M_1 \to M_2/f_1M_2 \to M_3/f_1M_3 \to 0
$$
Le lemme en résulte par récurrence sur $r$. Certains détails sont omis.
\end{proof}
```

</details>

### 10 — lemma-regular-sequence-powers

Anglais L16747–16795 ; français L16513–16561.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16747) · FR-ALGEBRA-B34-CHOICE-0010.

L'équivalence avec des exposants strictement positifs et les deux récurrences, sur r puis e, sont comparées en entier. Une phrase est corrigée : la liste f2,…,fr est une seule suite régulière pour chacun des deux modules, non des éléments qui seraient plusieurs suites. Formules, flèches, quotients et implication réciproque ne changent pas. La non-nullité du quotient pour les puissances n'est pas supprimée ; dans le cas d'un élément, M=fM équivaut à M=f^eM. Les détails omis restent omis dans la traduction.

Point particulier à relire : Les éléments ne sont pas chacun une suite : le sujet devient la suite et le verbe est au singulier. Même liste et mêmes deux modules. Aucune substitution d'indice ni ajout de preuve.

Règles : FR-ALGEBRA-B34-RULE-REGULAR, FR-ALGEBRA-B34-RULE-MODULE, FR-ALGEBRA-B34-RULE-SEQUENCE, FR-ALGEBRA-B34-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-regular-sequence-powers}
Let $R$ be a ring. Let $M$ be an $R$-module.
Let $f_1, \ldots, f_r \in R$ and $e_1, \ldots, e_r > 0$ integers.
Then $f_1, \ldots, f_r$ is an $M$-regular sequence
if and only if $f_1^{e_1}, \ldots, f_r^{e_r}$
is an $M$-regular sequence.
\end{lemma}

\begin{proof}
We will prove this by induction on $r$. If $r = 1$ this follows from the
following two easy facts: (a) a power of a nonzerodivisor on $M$
is a nonzerodivisor on $M$ and (b) a divisor of a nonzerodivisor on $M$
is a nonzerodivisor on $M$.
If $r > 1$, then by induction applied to $M/f_1M$ we have that
$f_1, f_2, \ldots, f_r$ is an $M$-regular sequence if and only if
$f_1, f_2^{e_2}, \ldots, f_r^{e_r}$ is an $M$-regular sequence.
Thus it suffices to show, given $e > 0$, that $f_1^e, f_2, \ldots, f_r$
is an $M$-regular sequence if and only if $f_1, \ldots, f_r$
is an $M$-regular sequence. We will prove this
by induction on $e$. The case $e = 1$ is trivial. Since $f_1$ is a
nonzerodivisor under both assumptions (by the case $r = 1$)
we have a short exact sequence
$$
0 \to M/f_1M \xrightarrow{f_1^{e - 1}} M/f_1^eM \to M/f_1^{e - 1}M \to 0
$$
Suppose that $f_1, f_2, \ldots, f_r$ is an $M$-regular sequence.
Then by induction the elements $f_2, \ldots, f_r$ are $M/f_1M$ and
$M/f_1^{e - 1}M$-regular sequences. By
Lemma \ref{lemma-regular-sequence-short-exact-sequence}
$f_2, \ldots, f_r$ is $M/f_1^eM$-regular. Hence $f_1^e, f_2, \ldots, f_r$
is $M$-regular. Conversely, suppose
that $f_1^e, f_2, \ldots, f_r$ is an $M$-regular sequence. Then
$f_2 : M/f_1^eM \to M/f_1^eM$ is injective, hence
$f_2 : M/f_1M \to M/f_1M$ is injective, hence by induction(!)
$f_2 : M/f_1^{e - 1}M \to M/f_1^{e - 1}M$ is injective, hence
$$
0 \to
M/(f_1, f_2)M \xrightarrow{f_1^{e - 1}}
M/(f_1^e, f_2)M \to
M/(f_1^{e - 1}, f_2)M \to 0
$$
is a short exact sequence by Lemma \ref{lemma-snake}. This proves the
converse for $r = 2$. If $r > 2$, then we have
$f_3 : M/(f_1^e, f_2)M \to M/(f_1^e, f_2)M$ is injective, hence
$f_3 : M/(f_1, f_2)M \to M/(f_1, f_2)M$ is injective, and so on.
Some details omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-regular-sequence-powers}
Soit $R$ un anneau. Soit $M$ un $R$-module.
Soient $f_1, \ldots, f_r \in R$ et des entiers $e_1, \ldots, e_r > 0$.
Alors la suite $f_1, \ldots, f_r$ est $M$-régulière
si et seulement si $f_1^{e_1}, \ldots, f_r^{e_r}$
est une suite $M$-régulière.
\end{lemma}

\begin{proof}
Nous le démontrons par récurrence sur $r$. Si $r = 1$, cela résulte des
deux faits élémentaires suivants : (a) une puissance d'un non-diviseur de zéro sur $M$
est un non-diviseur de zéro sur $M$, et (b) un diviseur d'un non-diviseur de zéro sur $M$
est un non-diviseur de zéro sur $M$.
Si $r > 1$, la récurrence appliquée à $M/f_1M$ montre que
$f_1, f_2, \ldots, f_r$ est une suite $M$-régulière si et seulement si
$f_1, f_2^{e_2}, \ldots, f_r^{e_r}$ est une suite $M$-régulière.
Il suffit donc de montrer, étant donné $e > 0$, que $f_1^e, f_2, \ldots, f_r$
est une suite $M$-régulière si et seulement si $f_1, \ldots, f_r$
est une suite $M$-régulière. Nous le démontrons
par récurrence sur $e$. Le cas $e = 1$ est trivial. Puisque $f_1$ est un
non-diviseur de zéro sous les deux hypothèses (d'après le cas $r = 1$),
on a une suite exacte courte
$$
0 \to M/f_1M \xrightarrow{f_1^{e - 1}} M/f_1^eM \to M/f_1^{e - 1}M \to 0
$$
Supposons que $f_1, f_2, \ldots, f_r$ soit une suite $M$-régulière.
Alors, par récurrence, la suite $f_2, \ldots, f_r$ est régulière sur $M/f_1M$ et
$M/f_1^{e - 1}M$. D'après le
Lemme \ref{lemma-regular-sequence-short-exact-sequence},
$f_2, \ldots, f_r$ est $M/f_1^eM$-régulière. Ainsi $f_1^e, f_2, \ldots, f_r$
est $M$-régulière. Réciproquement, supposons
que $f_1^e, f_2, \ldots, f_r$ soit une suite $M$-régulière. Alors
$f_2 : M/f_1^eM \to M/f_1^eM$ est injectif, donc
$f_2 : M/f_1M \to M/f_1M$ est injectif, puis, par récurrence (!),
$f_2 : M/f_1^{e - 1}M \to M/f_1^{e - 1}M$ est injectif, et donc
$$
0 \to
M/(f_1, f_2)M \xrightarrow{f_1^{e - 1}}
M/(f_1^e, f_2)M \to
M/(f_1^{e - 1}, f_2)M \to 0
$$
est une suite exacte courte d'après le Lemme \ref{lemma-snake}. Cela démontre la
réciproque pour $r = 2$. Si $r > 2$, alors
$f_3 : M/(f_1^e, f_2)M \to M/(f_1^e, f_2)M$ est injectif, donc
$f_3 : M/(f_1, f_2)M \to M/(f_1, f_2)M$ est injectif, et ainsi de suite.
Certains détails sont omis.
\end{proof}
```

</details>

### 11 — lemma-regular-sequence-in-polynomial-ring

Anglais L16796–16854 ; français L16562–16620.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16796) · FR-ALGEBRA-B34-CHOICE-0011.

Les trois conditions restent distinctes : toutes permutations, toutes sous-suites dans l'ordre donné, et suite dans l'anneau de polynômes. L'idéal unité est explicitement exclu. Toute la preuve des permutations et de la décomposition par multi-indices est comparée. On remplace a,b est une suite par les éléments a,b forment une suite : accord et sujet rendus corrects, même proposition. L'indice erroné x_i dans la source reste littéral et séparément motivé ; pas de réparation mathématique cachée.

Point particulier à relire : Accord forment appliqué aux deux éléments ; la liste b,a peut ensuite servir de sujet singulier collectif. La phrase sur E entièrement positif ne mentionne que la sous-suite initiale ; la condition pour tous E assure aussi les sous-suites sélectionnées. Ce détail elliptique n'est pas déclaré faux. L'erreur d'indice x_i est seule enregistrée comme défaut mathématique dans ce passage.

Règles : FR-ALGEBRA-B34-RULE-REGULAR, FR-ALGEBRA-B34-RULE-MODULE, FR-ALGEBRA-B34-RULE-SEQUENCE, FR-ALGEBRA-B34-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-regular-sequence-in-polynomial-ring}
Let $R$ be a ring. Let $f_1, \ldots, f_r \in R$ which do not generate
the unit ideal. The following are equivalent:
\begin{enumerate}
\item any permutation of $f_1, \ldots, f_r$ is a regular sequence,
\item any subsequence of $f_1, \ldots, f_r$ (in the given order) is
a regular sequence, and
\item $f_1x_1, \ldots, f_rx_r$ is a regular sequence in the polynomial
ring $R[x_1, \ldots, x_r]$.
\end{enumerate}
\end{lemma}

\begin{proof}
It is clear that (1) implies (2). We prove (2) implies (1) by induction
on $r$. The case $r = 1$ is trivial. The case $r = 2$ says that if
$a, b \in R$ are a regular sequence and $b$ is a nonzerodivisor, then
$b, a$ is a regular sequence. This is clear because the kernel of
$a : R/(b) \to R/(b)$ is isomorphic to the kernel of $b : R/(a) \to R/(a)$
if both $a$ and $b$ are nonzerodivisors. The case $r > 2$. Assume
(2) holds and say we want to prove $f_{\sigma(1)}, \ldots, f_{\sigma(r)}$
is a regular sequence for some permutation $\sigma$. We already know
that $f_{\sigma(1)}, \ldots, f_{\sigma(r - 1)}$ is a regular sequence
by induction. Hence it suffices to show that $f_s$ where $s = \sigma(r)$
is a nonzerodivisor modulo $f_1, \ldots, \hat f_s, \ldots, f_r$.
If $s = r$ we are done. If $s < r$, then note that $f_s$ and $f_r$
are both nonzerodivisors in the ring
$R/(f_1, \ldots, \hat f_s, \ldots, f_{r - 1})$
(by induction hypothesis again). Since we know $f_s, f_r$ is a
regular sequence in that ring we conclude by the case of sequence of length
$2$ that $f_r, f_s$ is too.

\medskip\noindent
Note that $R[x_1, \ldots, x_r]/(f_1x_1, \ldots, f_ix_i)$ as an $R$-module
is a direct sum of the modules
$$
R/I_E \cdot x_1^{e_1} \ldots x_r^{e_r}
$$
indexed by multi-indices $E = (e_1, \ldots, e_r)$ where
$I_E$ is the ideal generated by $f_j$ for $1 \leq j \leq i$
with $e_j > 0$. Hence $f_{i + 1}x_i$ is a nonzerodivisor on this if
and only if $f_{i + 1}$ is a nonzerodivisor on $R/I_E$ for all $E$.
Taking $E$ with all positive entries, we see that $f_{i + 1}$
is a nonzerodivisor on $R/(f_1, \ldots, f_i)$. Thus (3) implies (2).
Conversely, if (2) holds, then any subsequence of
$f_1, \ldots, f_i, f_{i + 1}$ is a regular sequence
in particular $f_{i + 1}$ is a nonzerodivisor on all $R/I_E$.
In this way we see that (2) implies (3).
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-regular-sequence-in-polynomial-ring}
Soit $R$ un anneau. Soient $f_1, \ldots, f_r \in R$ qui n'engendrent pas
l'idéal unité. Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item toute permutation de $f_1, \ldots, f_r$ est une suite régulière,
\item toute sous-suite de $f_1, \ldots, f_r$ (dans l'ordre donné) est
une suite régulière, et
\item $f_1x_1, \ldots, f_rx_r$ est une suite régulière dans l'anneau de
polynômes $R[x_1, \ldots, x_r]$.
\end{enumerate}
\end{lemma}

\begin{proof}
Il est clair que (1) implique (2). Montrons par récurrence sur $r$
que (2) implique (1). Le cas $r = 1$ est trivial. Pour $r = 2$, il s'agit de dire que si
les éléments $a, b \in R$ forment une suite régulière et si $b$ est un non-diviseur de zéro, alors
$b, a$ est une suite régulière. Cela est clair, car le noyau de
$a : R/(b) \to R/(b)$ est isomorphe au noyau de $b : R/(a) \to R/(a)$
si $a$ et $b$ sont tous deux des non-diviseurs de zéro. Supposons $r > 2$.
Supposons (2) vérifiée et cherchons à montrer que $f_{\sigma(1)}, \ldots, f_{\sigma(r)}$
est une suite régulière pour une permutation $\sigma$. Nous savons déjà
par récurrence que $f_{\sigma(1)}, \ldots, f_{\sigma(r - 1)}$ est une suite régulière.
Il suffit donc de montrer que $f_s$, où $s = \sigma(r)$,
est un non-diviseur de zéro modulo $f_1, \ldots, \hat f_s, \ldots, f_r$.
Si $s = r$, c'est terminé. Si $s < r$, remarquons que $f_s$ et $f_r$
sont tous deux des non-diviseurs de zéro dans l'anneau
$R/(f_1, \ldots, \hat f_s, \ldots, f_{r - 1})$
(encore par hypothèse de récurrence). Puisque $f_s, f_r$ est une
suite régulière dans cet anneau, le cas des suites de longueur
$2$ montre que $f_r, f_s$ l'est également.

\medskip\noindent
Remarquons que $R[x_1, \ldots, x_r]/(f_1x_1, \ldots, f_ix_i)$, comme $R$-module,
est une somme directe des modules
$$
R/I_E \cdot x_1^{e_1} \ldots x_r^{e_r}
$$
indexés par les multi-indices $E = (e_1, \ldots, e_r)$, où
$I_E$ est l'idéal engendré par les $f_j$ tels que $1 \leq j \leq i$
et $e_j > 0$. Ainsi $f_{i + 1}x_i$ est un non-diviseur de zéro sur ce module si
et seulement si $f_{i + 1}$ est un non-diviseur de zéro sur $R/I_E$ pour tout $E$.
En prenant $E$ dont toutes les composantes sont strictement positives, on voit que $f_{i + 1}$
est un non-diviseur de zéro sur $R/(f_1, \ldots, f_i)$. Ainsi (3) implique (2).
Réciproquement, si (2) est vérifiée, toute sous-suite de
$f_1, \ldots, f_i, f_{i + 1}$ est une suite régulière ;
en particulier, $f_{i + 1}$ est un non-diviseur de zéro sur tous les $R/I_E$.
On voit ainsi que (2) implique (3).
\end{proof}
```

</details>

## Contrôles et suite

Les 231 régions mathématiques sont exactement identiques, sans exception nouvelle. Le préfixe de 11 979 régions passe avec quarante-trois exceptions linguistiques antérieures précisément recensées ; les différences sont vérifiées dans leur ordre et avec leurs multiplicités exactes.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items restent identiques. Aucune citation ou titre facultatif différent ne figure dans ce lot. Les opérations inverses retrouvent le lot précédent puis tous les octets du témoin public préservé. Préfixe déjà relu et suffixe encore non relu sont inchangés.

Les 611 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Suites quasi-régulières, anglais L16855 / français L16621. Aucun PDF nouveau ni publication ; restauration globale en cours.

