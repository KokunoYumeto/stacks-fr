# Suites quasi-régulières

## Résultat et portée

La section entière est comparée : anglais L16855–17135 et français L16621–16901, 281 lignes chacun et dix paires complètes. 110 occurrences de règles sont contextualisées, non un décompte de tous les mots. Couverture continue : 69 sections, 621 paires et 6138 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Aucune correction française nouvelle n’est nécessaire après comparaison complète. Le fichier précédent est conservé sans créer une copie identique. Application canonique, graduation, convention de quasi-régularité, changement de base, voisinage, troncature, réciproque locale et contre-exemple de concaténation restent fidèles. Un titre facultatif est localisé, avec la clé bibliographique Kabele inchangée.

Trois observations anglaises restent séparées : coefficients du module dans J au lieu de JM, module polynomial appelé algèbre et noté M/J, et by manquant après denote. Le français conserve les deux anomalies de contenu, tandis que notons est déjà idiomatique. Aucune correction source admise ni intégration mathématique cachée.

Lecture produite par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. Le canon est consulté rétrospectivement, non présenté comme consulté lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré inchangé](staged/fr/010_algebra.prose-batch34.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH34_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH35_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH35_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH35_OCCURRENCES.json) · [Opérations](ALGEBRA_PROSE_BATCH35_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH35_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH35_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH35_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH35_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH35_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Alexander Grothendieck — Éléments de géométrie algébrique IV, première partie, préliminaires15.1

[Source consultée](https://numdam.org/item/PMIHES_1964__20__5_0.pdf) · [Fichier conservé](canon-consulted/fr-algebra/ega-iv1-numdam.pdf)

Couverture PDF1 et pages PDF10–16 /imprimées11–17 intégralement lues ; PDF14 /imprimée15 rendu et inspecté. Construction15.1.1, définition15.1.7, propositions15.1.8–15.1.9 avec continuation, corollaire15.1.11 et remarques15.1.12.

Attestations courtes : « suite quasi-régulière », « M-quasi-régulière », « homomorphisme canonique », « module gradué ».

La définition15.1.7 atteste le terme et le critère canonique ;15.1.1 définit le module polynomial associé. Les résultats voisins séparent implication directe et réciproque sous hypothèses.

Limites : La convention régulière d'EGA n'impose pas le quotient final non nul : elle n'est pas importée dans Stacks. Ce témoin ne prouve pas toutes ses assertions et n'atteste pas les composés Koszul-régulière/H1-régulière. Consultation rétrospective de ces pages, pas du volume entier.

SHA-256 : DF11AFC6B6318FC491032B1239CD4AF9CBC2A7C73219DCC49BF65E5EE6C13140.

### Christian Peskine — Introduction algébrique à la géométrie projective

[Source consultée](https://perso.univ-rennes1.fr/matthieu.romagny/M2_0708/bouquin.pdf) · [Fichier conservé](canon-consulted/fr-algebra/peskine-geometrie-projective-2007.pdf)

Lecture intégrale PDF138–143 /imprimées137–142 effectuée dans B34 de cette continuation. Section16.1, définition16.3, lemme16.6, vocabulaire de suites exactes et profondeur.

Attestations courtes : « suite M-régulière », « non diviseur de 0 ».

Appui complémentaire pour le registre des suites régulières, modules de type fini, noyaux et quotients.

Limites : Ces pages ne constituent pas une attestation de quasi-régulière ni une preuve des lemmes généraux de Stacks ; leur cadre local/noethérien/de type fini reste explicitement restreint.

SHA-256 : C84D597457282B22B993F523791F4A3E391A74554FF76F7F49878640789435BA.

## Modifications et motifs

Zéro modification nouvelle du français : l’examen justifie sa conservation. Les conventions de régulière et quasi-régulière ne sont pas confondues. Le titre facultatif est traduit sans changer le sens ; les trois observations source ne deviennent pas une liberté éditoriale française.

## Observations séparées sur la source

Les trois observations distinguent type d’appartenance des coefficients, nature et notation du module polynomial, et préposition manquante. Le français reste conforme au témoin officiel. Aucune admission, déduplication globale ou première découverte n’est revendiquée.

### lemma-regular-quasi-regular

[Anglais officiel L16975](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16975) · FR-ALGEBRA-B35-SOURCE-NOTE-0001.

```tex
\in J^{n + 1}M$, then all the coefficients $m_I$ are in $J$.
```

Les coefficients m_I sont des éléments de M, tandis que J est un idéal de R. L'injectivité de l'application canonique signifie que tous les coefficients ont classe nulle dans M/JM, donc m_I∈JM. Remplacer le J final par JM rétablit le type et le critère ; ce n'est pas une exigence que m_I soient des scalaires. Le français conserve le J source.

Confiance forte par la définition de l'application, sans mutation, admission ni prétention de première découverte.

### lemma-truncate-quasi-regular

[Anglais officiel L17055](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17055) · FR-ALGEBRA-B35-SOURCE-NOTE-0002.

```tex
because $\bigoplus J^nM/J^{n + 1}M$ is the polynomial algebra
$M/J[X_1, \ldots, X_c]$ by assumption.
```

Pour M arbitraire, la définition identifie le membre gauche au module polynomial (M/JM)⊗_{R/J}(R/J)[X1,…,Xc], pas à une algèbre : M ne porte aucune multiplication dans les hypothèses. Le quotient M/J est également abrégé sans le sous-module JM. Écrire module polynomial M/JM[X1,…,Xc] rétablit les deux types liés dans cette phrase. L'égalité d'intersection précédente et le lemme ne sont pas déclarés faux ; le français conserve le mot algèbre et la formule source.

Confiance forte sur la nature de module et le quotient requis ; observation liée de notation et d'objet, non correction admise.

### lemma-quasi-regular-on-quotient

[Anglais officiel L17120](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17120) · FR-ALGEBRA-B35-SOURCE-NOTE-0003.

```tex
and denote
$\overline{f}_i$ the image of $f_i$ in $\overline{R}$.
```

Denote by X the image exige by après denote. Ajouter by corrige la syntaxe anglaise, sans toucher aux images ni aux quotients. Notons X l'image est déjà idiomatique en français : rien n'est modifié.

Confiance forte, correction grammaticale seulement ; pas d'admission, déduplication globale ou première découverte.

## Règles contextualisées

### FR-ALGEBRA-B35-RULE-QUASIREGULAR

Les conditions régulière, quasi-régulière et homologiques restent distinctes ; les restrictions de la réciproque et les conventions propres à Stacks sont préservées.

Canon : FR-ALGEBRA-B35-CANON-EGAIV1, FR-ALGEBRA-B35-CANON-PESKINE.

### FR-ALGEBRA-B35-RULE-GRADED

Le module gradué, l'application et les composantes restent leurs objets source. Le mot algèbre pour un module arbitraire est une réserve anglaise séparée.

Canon : FR-ALGEBRA-B35-CANON-EGAIV1.

### FR-ALGEBRA-B35-RULE-MODULE

Finitude, platitude, quotients et tenseurs conservent leurs hypothèses et bases. Aucun module n'est transformé en anneau par la traduction.

Canon : FR-ALGEBRA-B35-CANON-EGAIV1, FR-ALGEBRA-B35-CANON-PESKINE.

### FR-ALGEBRA-B35-RULE-LOGIC

Chaque sens d'implication, quantificateur, ordre et contre-exemple est contextualisé dans les dix passages complets.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-quasi-regular

Anglais L16855–16876 ; français L16621–16642.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16855) · FR-ALGEBRA-B35-CHOICE-0001.

Suites quasi-régulières et modules gradués sont directement attestés en EGA IV, préliminaires15.1. La construction entière de l'application canonique et sa surjectivité sont comparées, avec les degrés, le quotient M/JM, la base R/J et chaque exposant.

Règles : FR-ALGEBRA-B35-RULE-QUASIREGULAR, FR-ALGEBRA-B35-RULE-GRADED, FR-ALGEBRA-B35-RULE-MODULE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Quasi-regular sequences}
\label{section-quasi-regular}

\noindent
We introduce the notion of quasi-regular sequence which is slightly weaker
than that of a regular sequence and easier to use.
Let $R$ be a ring and let $f_1, \ldots, f_c \in R$.
Set $J = (f_1, \ldots, f_c)$. Let $M$ be an $R$-module.
Then there is a canonical map
\begin{equation}
\label{equation-quasi-regular}
M/JM \otimes_{R/J} R/J[X_1, \ldots, X_c]
\longrightarrow
\bigoplus\nolimits_{n \geq 0} J^nM/J^{n + 1}M
\end{equation}
of graded $R/J[X_1, \ldots, X_c]$-modules defined by the rule
$$
\overline{m} \otimes X_1^{e_1} \ldots X_c^{e_c} \longmapsto
f_1^{e_1} \ldots f_c^{e_c} m \bmod J^{e_1 + \ldots + e_c + 1}M.
$$
Note that (\ref{equation-quasi-regular}) is always surjective.
```

Français restauré :
```tex
\section{Suites quasi-régulières}
\label{section-quasi-regular}

\noindent
Nous introduisons la notion de suite quasi-régulière, légèrement plus faible
que celle de suite régulière et plus facile à utiliser.
Soit $R$ un anneau et soient $f_1, \ldots, f_c \in R$.
Posons $J = (f_1, \ldots, f_c)$. Soit $M$ un $R$-module.
Il existe alors une application canonique
\begin{equation}
\label{equation-quasi-regular}
M/JM \otimes_{R/J} R/J[X_1, \ldots, X_c]
\longrightarrow
\bigoplus\nolimits_{n \geq 0} J^nM/J^{n + 1}M
\end{equation}
de $R/J[X_1, \ldots, X_c]$-modules gradués définie par la règle
$$
\overline{m} \otimes X_1^{e_1} \ldots X_c^{e_c} \longmapsto
f_1^{e_1} \ldots f_c^{e_c} m \bmod J^{e_1 + \ldots + e_c + 1}M.
$$
Remarquons que (\ref{equation-quasi-regular}) est toujours surjective.
```

</details>

### 02 — definition-quasi-regular-sequence

Anglais L16877–16894 ; français L16643–16660.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16877) · FR-ALGEBRA-B35-CHOICE-0002.

M-quasi-régulière est attesté en EGA IV, définition15.1.7. La définition est exactement l'isomorphisme canonique, pour M arbitraire ; aucune condition de quotient non nul n'est ajoutée par analogie avec les suites régulières. Indépendance de l'ordre et cas M=R restent exacts.

Point particulier à relire : EGA IV ne demande pas le quotient non nul pour sa convention de régularité, tandis que Stacks le demande pour régulière. La quasi-régularité définie ici par isomorphisme ne reçoit pas cette condition. Les sources ne sont pas fusionnées.

Règles : FR-ALGEBRA-B35-RULE-QUASIREGULAR, FR-ALGEBRA-B35-RULE-GRADED, FR-ALGEBRA-B35-RULE-MODULE, FR-ALGEBRA-B35-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-quasi-regular-sequence}
Let $R$ be a ring.
Let $M$ be an $R$-module.
A sequence of elements $f_1, \ldots, f_c$ of $R$ is called
{\it $M$-quasi-regular} if (\ref{equation-quasi-regular})
is an isomorphism. If $M = R$, we call $f_1, \ldots, f_c$ simply a
{\it quasi-regular sequence}.
\end{definition}

\noindent
So if $f_1, \ldots, f_c$ is a quasi-regular sequence, then
$$
R/J[X_1, \ldots, X_c] = \bigoplus\nolimits_{n \geq 0} J^n/J^{n + 1}
$$
where $J = (f_1, \ldots, f_c)$. It is clear that being a quasi-regular
sequence is independent of the order of $f_1, \ldots, f_c$.
```

Français restauré :
```tex
\begin{definition}
\label{definition-quasi-regular-sequence}
Soit $R$ un anneau.
Soit $M$ un $R$-module.
Une suite d'éléments $f_1, \ldots, f_c$ de $R$ est dite
{\it $M$-quasi-régulière} si (\ref{equation-quasi-regular})
est un isomorphisme. Si $M = R$, nous appelons simplement $f_1, \ldots, f_c$ une
{\it suite quasi-régulière}.
\end{definition}

\noindent
Ainsi, si $f_1, \ldots, f_c$ est une suite quasi-régulière, alors
$$
R/J[X_1, \ldots, X_c] = \bigoplus\nolimits_{n \geq 0} J^n/J^{n + 1}
$$
où $J = (f_1, \ldots, f_c)$. Il est clair que la propriété d'être une suite
quasi-régulière ne dépend pas de l'ordre de $f_1, \ldots, f_c$.
```

</details>

### 03 — lemma-regular-quasi-regular

Anglais L16895–16979 ; français L16661–16745.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16895) · FR-ALGEBRA-B35-CHOICE-0003.

Les deux assertions et toute la preuve sont lues. Les récurrences sur c puis l, multi-indices primés, coefficients et changements de relation sont comparés dans leur ordre. Régulière implique quasi-régulière, pas l'inverse sans hypothèses. EGA IV15.1.9 atteste ce sens et distingue les hypothèses de séparation pour la réciproque. La faute source finale m_I dans J, au lieu de JM, reste littérale en français et documentée séparément.

Point particulier à relire : La seconde assertion parle de coefficients dans M. Leur appartenance à J, un idéal de R, est une faute de type dans la source ; le français reste diplomatique. Le cas de base des récurrences est elliptique, non déclaré faux.

Règles : FR-ALGEBRA-B35-RULE-QUASIREGULAR, FR-ALGEBRA-B35-RULE-GRADED, FR-ALGEBRA-B35-RULE-MODULE, FR-ALGEBRA-B35-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-regular-quasi-regular}
Let $R$ be a ring.
\begin{enumerate}
\item A regular sequence $f_1, \ldots, f_c$ of $R$ is a quasi-regular
sequence.
\item Suppose that $M$ is an $R$-module and that $f_1, \ldots, f_c$
is an $M$-regular sequence. Then $f_1, \ldots, f_c$ is an
$M$-quasi-regular sequence.
\end{enumerate}
\end{lemma}

\begin{proof}
Set $J = (f_1, \ldots, f_c)$.
We prove the first assertion by induction on $c$.
We have to show that given any relation
$\sum_{|I| = n} a_I f^I \in J^{n + 1}$ with $a_I \in R$ we
actually have $a_I \in J$ for all multi-indices $I$. Since
any element of $J^{n + 1}$ is of the form $\sum_{|I| = n} b_I f^I$
with $b_I \in J$ we may assume, after replacing $a_I$ by $a_I - b_I$,
the relation reads $\sum_{|I| = n} a_I f^I = 0$. We can rewrite
this as
$$
\sum\nolimits_{e = 0}^n
\left(
\sum\nolimits_{|I'| = n - e}
a_{I', e} f^{I'}
\right)
f_c^e
=
0
$$
Here and below the ``primed'' multi-indices $I'$ are required to be of the form
$I' = (i_1, \ldots, i_{c - 1}, 0)$. We will show by
induction on $l \in \{0, \ldots, n\}$
that if we have a relation
$$
\sum\nolimits_{e = 0}^l
\left(
\sum\nolimits_{|I'| = n - e}
a_{I', e} f^{I'}
\right)
f_c^e
=
0
$$
then $a_{I', e} \in J$ for all $I', e$.
Namely, set $J' = (f_1, \ldots, f_{c-1})$.
Observe that $\sum\nolimits_{|I'| = n - l} a_{I', l} f^{I'}$
is mapped into $(J')^{n - l + 1}$ by $f_c^{l}$.
By induction hypothesis (for the induction on $c$)
we see that $f_c^l a_{I', l} \in J'$.
Because $f_c$ is not a zerodivisor on $R/J'$ (as $f_1, \ldots, f_c$
is a regular sequence) we conclude that $a_{I', l} \in J'$.
This allows us to rewrite the term
$(\sum\nolimits_{|I'| = n - l} a_{I', l} f^{I'})f_c^l$
in the form $(\sum\nolimits_{|I'| = n - l + 1} f_c b_{I', l - 1}
f^{I'})f_c^{l-1}$. This gives a new relation of the form
$$
\left(\sum\nolimits_{|I'| = n - l + 1}
(a_{I', l-1} + f_c b_{I', l - 1}) f^{I'}\right)f_c^{l-1}
+
\sum\nolimits_{e = 0}^{l - 2}
\left(
\sum\nolimits_{|I'| = n - e}
a_{I', e} f^{I'}
\right)
f_c^e
=
0
$$
Now by the induction hypothesis (on $l$ this time) we see that
all $a_{I', l-1} + f_c b_{I', l - 1} \in J$ and
all $a_{I', e} \in J$ for $e \leq l - 2$. This, combined with
$a_{I', l} \in J' \subset J$ seen above, finishes the proof of the
induction step.

\medskip\noindent
The second assertion means that given any formal expression
$F = \sum_{|I| = n} m_I X^I$, $m_I \in M$ with $\sum m_I f^I
\in J^{n + 1}M$, then all the coefficients $m_I$ are in $J$.
This is proved in exactly the same way as we prove the corresponding
result for the first assertion above.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-regular-quasi-regular}
Soit $R$ un anneau.
\begin{enumerate}
\item Une suite régulière $f_1, \ldots, f_c$ de $R$ est une suite
quasi-régulière.
\item Supposons que $M$ soit un $R$-module et que $f_1, \ldots, f_c$
soit une suite $M$-régulière. Alors $f_1, \ldots, f_c$ est une suite
$M$-quasi-régulière.
\end{enumerate}
\end{lemma}

\begin{proof}
Posons $J = (f_1, \ldots, f_c)$.
Démontrons la première assertion par récurrence sur $c$.
Il faut montrer que, pour toute relation
$\sum_{|I| = n} a_I f^I \in J^{n + 1}$ avec $a_I \in R$, on a en fait
$a_I \in J$ pour tout multi-indice $I$. Puisque
tout élément de $J^{n + 1}$ est de la forme $\sum_{|I| = n} b_I f^I$
avec $b_I \in J$, on peut supposer, après avoir remplacé $a_I$ par $a_I - b_I$,
que la relation s'écrit $\sum_{|I| = n} a_I f^I = 0$. On peut la réécrire
sous la forme
$$
\sum\nolimits_{e = 0}^n
\left(
\sum\nolimits_{|I'| = n - e}
a_{I', e} f^{I'}
\right)
f_c^e
=
0
$$
Ici et ci-dessous, les multi-indices « primés » $I'$ sont supposés être de la forme
$I' = (i_1, \ldots, i_{c - 1}, 0)$. Nous allons montrer par
récurrence sur $l \in \{0, \ldots, n\}$
que, si l'on a une relation
$$
\sum\nolimits_{e = 0}^l
\left(
\sum\nolimits_{|I'| = n - e}
a_{I', e} f^{I'}
\right)
f_c^e
=
0
$$
alors $a_{I', e} \in J$ pour tous $I', e$.
En effet, posons $J' = (f_1, \ldots, f_{c-1})$.
Remarquons que $\sum\nolimits_{|I'| = n - l} a_{I', l} f^{I'}$
est envoyé dans $(J')^{n - l + 1}$ par $f_c^{l}$.
L'hypothèse de récurrence (pour la récurrence sur $c$)
montre que $f_c^l a_{I', l} \in J'$.
Comme $f_c$ n'est pas un diviseur de zéro sur $R/J'$ (car $f_1, \ldots, f_c$
est une suite régulière), on en déduit que $a_{I', l} \in J'$.
Cela permet de réécrire le terme
$(\sum\nolimits_{|I'| = n - l} a_{I', l} f^{I'})f_c^l$
 sous la forme $(\sum\nolimits_{|I'| = n - l + 1} f_c b_{I', l - 1}
f^{I'})f_c^{l-1}$. On obtient ainsi une nouvelle relation de la forme
$$
\left(\sum\nolimits_{|I'| = n - l + 1}
(a_{I', l-1} + f_c b_{I', l - 1}) f^{I'}\right)f_c^{l-1}
+
\sum\nolimits_{e = 0}^{l - 2}
\left(
\sum\nolimits_{|I'| = n - e}
a_{I', e} f^{I'}
\right)
f_c^e
=
0
$$
L'hypothèse de récurrence (sur $l$ cette fois) montre maintenant que
tous les $a_{I', l-1} + f_c b_{I', l - 1} \in J$ et que
tous les $a_{I', e} \in J$ pour $e \leq l - 2$. Avec la relation
$a_{I', l} \in J' \subset J$ obtenue ci-dessus, cela achève la démonstration du
pas de récurrence.

\medskip\noindent
La seconde assertion signifie que, pour toute expression formelle
$F = \sum_{|I| = n} m_I X^I$, avec $m_I \in M$ et $\sum m_I f^I
\in J^{n + 1}M$, tous les coefficients $m_I$ appartiennent à $J$.
Cela se démontre exactement comme le résultat correspondant
de la première assertion ci-dessus.
\end{proof}
```

</details>

### 04 — lemma-flat-base-change-quasi-regular

Anglais L16980–17003 ; français L16746–16769.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16980) · FR-ALGEBRA-B35-CHOICE-0004.

Changement de base plat, non nécessairement fidèlement plat, et M arbitraire sont conservés. Les deux suites exactes après tensorisation, les puissances de l'idéal étendu, les quotients et l'identification de l'application sont comparés. L'ordre écrit des facteurs tensoriels est celui de la source. Aucun sens réciproque ajouté.

Règles : FR-ALGEBRA-B35-RULE-QUASIREGULAR, FR-ALGEBRA-B35-RULE-GRADED, FR-ALGEBRA-B35-RULE-MODULE, FR-ALGEBRA-B35-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-flat-base-change-quasi-regular}
Let $R \to R'$ be a flat ring map. Let $M$ be an $R$-module.
Suppose that $f_1, \ldots, f_r \in R$ form an $M$-quasi-regular sequence.
Then the images of $f_1, \ldots, f_r$ in
$R'$ form a $M \otimes_R R'$-quasi-regular sequence.
\end{lemma}

\begin{proof}
Set $J = (f_1, \ldots, f_r)$, $J' = JR'$ and $M' = M \otimes_R R'$.
We have to show the canonical map
$\mu : R'/J'[X_1, \ldots X_r] \otimes_{R'/J'} M'/J'M' \to
\bigoplus (J')^nM'/(J')^{n + 1}M'$ is an isomorphism.
Because $R \to R'$ is flat the sequences
$0 \to J^nM \to M$ and
$0 \to J^{n + 1}M \to J^nM \to J^nM/J^{n + 1}M \to 0$
remain exact on tensoring with $R'$. This first implies that
$J^nM \otimes_R R' = (J')^nM'$ and then that
$(J')^nM'/(J')^{n + 1}M' = J^nM/J^{n + 1}M \otimes_R R'$.
Thus $\mu$ is the tensor product of (\ref{equation-quasi-regular}),
which is an isomorphism by assumption,
with $\text{id}_{R'}$ and we conclude.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-flat-base-change-quasi-regular}
Soit $R \to R'$ un homomorphisme plat d'anneaux. Soit $M$ un $R$-module.
Supposons que la suite $f_1, \ldots, f_r \in R$ soit $M$-quasi-régulière.
Alors les images de $f_1, \ldots, f_r$ dans
$R'$ forment une suite $M \otimes_R R'$-quasi-régulière.
\end{lemma}

\begin{proof}
Posons $J = (f_1, \ldots, f_r)$, $J' = JR'$ et $M' = M \otimes_R R'$.
Il faut montrer que l'application canonique
$\mu : R'/J'[X_1, \ldots X_r] \otimes_{R'/J'} M'/J'M' \to
\bigoplus (J')^nM'/(J')^{n + 1}M'$ est un isomorphisme.
Puisque $R \to R'$ est plat, les suites
$0 \to J^nM \to M$ et
$0 \to J^{n + 1}M \to J^nM \to J^nM/J^{n + 1}M \to 0$
restent exactes après tensorisation par $R'$. Cela implique d'abord
$J^nM \otimes_R R' = (J')^nM'$, puis
$(J')^nM'/(J')^{n + 1}M' = J^nM/J^{n + 1}M \otimes_R R'$.
Ainsi $\mu$ est le produit tensoriel de (\ref{equation-quasi-regular}),
qui est un isomorphisme par hypothèse,
avec $\text{id}_{R'}$, ce qui conclut.
\end{proof}
```

</details>

### 05 — lemma-quasi-regular-sequence-in-neighbourhood

Anglais L17004–17025 ; français L16770–16791.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17004) · FR-ALGEBRA-B35-CHOICE-0005.

Noethérianité de R et type fini de M permettent la finitude du noyau comme module sur l'anneau de polynômes quotient. Chaque générateur homogène reçoit un g_i hors p ; leur produit est conservé. La preuve entière ne remplace pas une famille homogène finie par une vérification arbitraire de chaque degré.

Règles : FR-ALGEBRA-B35-RULE-QUASIREGULAR, FR-ALGEBRA-B35-RULE-GRADED, FR-ALGEBRA-B35-RULE-MODULE, FR-ALGEBRA-B35-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-quasi-regular-sequence-in-neighbourhood}
Let $R$ be a Noetherian ring. Let $M$ be a finite $R$-module.
Let $\mathfrak p$ be a prime. Let $x_1, \ldots, x_c$ be a sequence
in $R$ whose image in $R_{\mathfrak p}$ forms an
$M_{\mathfrak p}$-quasi-regular sequence. Then there exists a
$g \in R$, $g \not \in \mathfrak p$
such that the image of $x_1, \ldots, x_c$ in $R_g$ forms
an $M_g$-quasi-regular sequence.
\end{lemma}

\begin{proof}
Consider the kernel $K$ of the map (\ref{equation-quasi-regular}).
As $M/JM \otimes_{R/J} R/J[X_1, \ldots, X_c]$ is a finite
$R/J[X_1, \ldots, X_c]$-module and as $R/J[X_1, \ldots, X_c]$ is
Noetherian, we see that $K$ is also a finite $R/J[X_1, \ldots, X_c]$-module.
Pick homogeneous generators $k_1, \ldots, k_t \in K$.
By assumption for each $i = 1, \ldots, t$ there exists a $g_i \in R$,
$g_i \not \in \mathfrak p$ such that $g_i k_i = 0$.
Hence $g = g_1 \ldots g_t$ works.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-quasi-regular-sequence-in-neighbourhood}
Soit $R$ un anneau noethérien. Soit $M$ un $R$-module de type fini.
Soit $\mathfrak p$ un idéal premier. Soit $x_1, \ldots, x_c$ une suite
dans $R$ dont l'image dans $R_{\mathfrak p}$ forme une suite
$M_{\mathfrak p}$-quasi-régulière. Alors il existe
$g \in R$, avec $g \not \in \mathfrak p$,
tel que l'image de $x_1, \ldots, x_c$ dans $R_g$ forme
une suite $M_g$-quasi-régulière.
\end{lemma}

\begin{proof}
Considérons le noyau $K$ de l'application (\ref{equation-quasi-regular}).
Comme $M/JM \otimes_{R/J} R/J[X_1, \ldots, X_c]$ est un
$R/J[X_1, \ldots, X_c]$-module de type fini et que $R/J[X_1, \ldots, X_c]$ est
noethérien, $K$ est aussi un $R/J[X_1, \ldots, X_c]$-module de type fini.
Choisissons des générateurs homogènes $k_1, \ldots, k_t \in K$.
Par hypothèse, pour tout $i = 1, \ldots, t$, il existe $g_i \in R$,
avec $g_i \not \in \mathfrak p$, tel que $g_i k_i = 0$.
Alors $g = g_1 \ldots g_t$ convient.
\end{proof}
```

</details>

### 06 — lemma-truncate-quasi-regular

Anglais L17026–17058 ; français L16792–16824.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17026) · FR-ALGEBRA-B35-CHOICE-0006.

La suite restante est dans R quotienté et agit sur M quotienté ; aucun passage à une sous-suite de M inchangé n'est ajouté. Les deux égalités de quotients, l'intersection avec f1M et le quotient gradué par X1 sont comparés. Le texte source appelle à tort une algèbre de polynômes un module polynomial et écrit M/J sans M ; ces réserves liées restent littérales dans le français, non transformées en corrections cachées.

Point particulier à relire : Un module M arbitraire n'a pas d'algèbre canonique. L'écriture M/J et le nom algèbre restent source-littéraux. La formule avec J^{n-1} porte sur les degrés positifs ; le degré0 se traite directement. Cette réserve de lecture n'est pas déclarée un défaut supplémentaire du résultat.

Règles : FR-ALGEBRA-B35-RULE-QUASIREGULAR, FR-ALGEBRA-B35-RULE-GRADED, FR-ALGEBRA-B35-RULE-MODULE, FR-ALGEBRA-B35-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-truncate-quasi-regular}
Let $R$ be a ring. Let $M$ be an $R$-module.
Let $f_1, \ldots, f_c \in R$ be an $M$-quasi-regular sequence.
For any $i$ the sequence
$\overline{f}_{i + 1}, \ldots, \overline{f}_c$
of $\overline{R} = R/(f_1, \ldots, f_i)$ is an
$\overline{M} = M/(f_1, \ldots, f_i)M$-quasi-regular sequence.
\end{lemma}

\begin{proof}
It suffices to prove this for $i = 1$. Set
$\overline{J} = (\overline{f}_2, \ldots, \overline{f}_c) \subset \overline{R}$.
Then
\begin{align*}
\overline{J}^n\overline{M}/\overline{J}^{n + 1}\overline{M}
& =
(J^nM + f_1M)/(J^{n + 1}M + f_1M) \\
& = J^nM / (J^{n + 1}M + J^nM \cap f_1M).
\end{align*}
Thus, in order to prove the lemma it suffices to show that
$J^{n + 1}M + J^nM \cap f_1M = J^{n + 1}M + f_1J^{n - 1}M$
because that will show that
$\bigoplus_{n \geq 0}
\overline{J}^n\overline{M}/\overline{J}^{n + 1}\overline{M}$
is the quotient of
$\bigoplus_{n \geq 0} J^nM/J^{n + 1}M \cong M/JM[X_1, \ldots, X_c]$
by $X_1$. Actually, we have $J^nM \cap f_1M = f_1J^{n - 1}M$.
Namely, if $m \not \in J^{n - 1}M$, then $f_1m \not \in J^nM$
because $\bigoplus J^nM/J^{n + 1}M$ is the polynomial algebra
$M/J[X_1, \ldots, X_c]$ by assumption.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-truncate-quasi-regular}
Soit $R$ un anneau. Soit $M$ un $R$-module.
Soit $f_1, \ldots, f_c \in R$ une suite $M$-quasi-régulière.
Pour tout $i$, la suite
$\overline{f}_{i + 1}, \ldots, \overline{f}_c$
de $\overline{R} = R/(f_1, \ldots, f_i)$ est une suite
$\overline{M} = M/(f_1, \ldots, f_i)M$-quasi-régulière.
\end{lemma}

\begin{proof}
Il suffit de le démontrer pour $i = 1$. Posons
$\overline{J} = (\overline{f}_2, \ldots, \overline{f}_c) \subset \overline{R}$.
Alors
\begin{align*}
\overline{J}^n\overline{M}/\overline{J}^{n + 1}\overline{M}
& =
(J^nM + f_1M)/(J^{n + 1}M + f_1M) \\
& = J^nM / (J^{n + 1}M + J^nM \cap f_1M).
\end{align*}
Ainsi, pour démontrer le lemme, il suffit de montrer que
$J^{n + 1}M + J^nM \cap f_1M = J^{n + 1}M + f_1J^{n - 1}M$
car cela montrera que
$\bigoplus_{n \geq 0}
\overline{J}^n\overline{M}/\overline{J}^{n + 1}\overline{M}$
est le quotient de
$\bigoplus_{n \geq 0} J^nM/J^{n + 1}M \cong M/JM[X_1, \ldots, X_c]$
par $X_1$. En fait, on a $J^nM \cap f_1M = f_1J^{n - 1}M$.
En effet, si $m \not \in J^{n - 1}M$, alors $f_1m \not \in J^nM$
car $\bigoplus J^nM/J^{n + 1}M$ est l'algèbre de polynômes
$M/J[X_1, \ldots, X_c]$ par hypothèse.
\end{proof}
```

</details>

### 07 — lemma-quasi-regular-regular

Anglais L17059–17082 ; français L16825–16848.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17059) · FR-ALGEBRA-B35-CHOICE-0007.

La réciproque utilise exactement anneau local noethérien, M non nul de type fini et éléments dans l'idéal maximal. Le théorème d'intersection de Krull donne le degré de x, puis la classe non nulle de f1x. Le lemme précédent et la récurrence sont préservés. EGA IV15.1.11 et remarque15.1.12(i) appuient ce registre et les restrictions, sans autoriser une réciproque générale.

Règles : FR-ALGEBRA-B35-RULE-QUASIREGULAR, FR-ALGEBRA-B35-RULE-MODULE, FR-ALGEBRA-B35-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-quasi-regular-regular}
Let $(R, \mathfrak m)$ be a local Noetherian ring.
Let $M$ be a nonzero finite $R$-module.
Let $f_1, \ldots, f_c \in \mathfrak m$ be an $M$-quasi-regular sequence.
Then $f_1, \ldots, f_c$ is an $M$-regular sequence.
\end{lemma}

\begin{proof}
Set $J = (f_1, \ldots, f_c)$.
Let us show that $f_1$ is a nonzerodivisor on $M$.
Suppose $x \in M$ is not zero.
By Krull's intersection theorem there exists an integer $r$
such that $x \in J^rM$ but $x \not \in J^{r + 1}M$, see
Lemma \ref{lemma-intersect-powers-ideal-module-zero}.
Then $f_1 x \in J^{r + 1}M$ is an element whose class in
$J^{r + 1}M/J^{r + 2}M$ is nonzero by the assumed structure of
$\bigoplus J^nM/J^{n + 1}M$. Whence $f_1x \not = 0$.

\medskip\noindent
Now we can finish the proof by induction on $c$ using
Lemma \ref{lemma-truncate-quasi-regular}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-quasi-regular-regular}
Soit $(R, \mathfrak m)$ un anneau local noethérien.
Soit $M$ un $R$-module de type fini non nul.
Soit $f_1, \ldots, f_c \in \mathfrak m$ une suite $M$-quasi-régulière.
Alors la suite $f_1, \ldots, f_c$ est $M$-régulière.
\end{lemma}

\begin{proof}
Posons $J = (f_1, \ldots, f_c)$.
Montrons que $f_1$ est un non-diviseur de zéro sur $M$.
Supposons $x \in M$ non nul.
D'après le théorème d'intersection de Krull, il existe un entier $r$
tel que $x \in J^rM$ mais $x \not \in J^{r + 1}M$ ; voir le
Lemme \ref{lemma-intersect-powers-ideal-module-zero}.
Alors $f_1 x \in J^{r + 1}M$ est un élément dont la classe dans
$J^{r + 1}M/J^{r + 2}M$ est non nulle, d'après la structure supposée de
$\bigoplus J^nM/J^{n + 1}M$. Par conséquent $f_1x \not = 0$.

\medskip\noindent
On peut maintenant achever la démonstration par récurrence sur $c$ en utilisant le
Lemme \ref{lemma-truncate-quasi-regular}.
\end{proof}
```

</details>

### 08 — remark-koszul-regular

Anglais L17083–17098 ; français L16849–16864.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17083) · FR-ALGEBRA-B35-CHOICE-0008.

Titre Autres types de suites régulières traduit le titre anglais et est recensé comme exception de titre facultatif, pas comme différence de mathématiques. Koszul-régulière, H1-régulière, les degrés d'homologie, les trois implications et leur non-réversibilité générale sont comparés. Le passage attribue les exemples à Kabele et garde la clé bibliographique ; l'article de Kabele n'est pas prétendu lu. Aucune nouvelle attestation externe de Koszul-régulière n'est inventée : nom propre et condition source motivent provisoirement la formulation.

Point particulier à relire : La clé Kabele et le renvoi à Compléments d'algèbre sont conservés. La convention sans quotient non nul pour les conditions homologiques explique pourquoi aucune réciproque ni convention supplémentaire ne peut être importée. Appui externe exact du composé Koszul-régulière non obtenu dans les pages consultées ; justification directe clairement provisoire.

Règles : FR-ALGEBRA-B35-RULE-QUASIREGULAR, FR-ALGEBRA-B35-RULE-MODULE, FR-ALGEBRA-B35-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{remark}[Other types of regular sequences]
\label{remark-koszul-regular}
In the paper \cite{Kabele} the author discusses two more
regularity conditions for sequences $x_1, \ldots, x_r$ of elements
of a ring $R$. Namely, we say the sequence is {\it Koszul-regular}
if $H_i(K_{\bullet}(R, x_{\bullet})) = 0$ for $i \geq 1$ where
$K_{\bullet}(R, x_{\bullet})$ is the Koszul complex. The sequence is
called {\it $H_1$-regular} if $H_1(K_{\bullet}(R, x_{\bullet})) = 0$.
One has the implications regular $\Rightarrow$ Koszul-regular $\Rightarrow$
$H_1$-regular $\Rightarrow$ quasi-regular. By examples the author shows that
these implications cannot be reversed in general even if $R$ is a
(non-Noetherian) local ring and the sequence generates the maximal ideal of
$R$. We introduce these notions in more detail in
More on Algebra, Section \ref{more-algebra-section-koszul-regular}.
\end{remark}
```

Français restauré :
```tex
\begin{remark}[Autres types de suites régulières]
\label{remark-koszul-regular}
Dans l'article \cite{Kabele}, l'auteur étudie deux autres
conditions de régularité pour les suites $x_1, \ldots, x_r$ d'éléments
d'un anneau $R$. On dit précisément que la suite est {\it Koszul-régulière}
si $H_i(K_{\bullet}(R, x_{\bullet})) = 0$ pour $i \geq 1$, où
$K_{\bullet}(R, x_{\bullet})$ est le complexe de Koszul. La suite est
dite {\it $H_1$-régulière} si $H_1(K_{\bullet}(R, x_{\bullet})) = 0$.
On a les implications régulière $\Rightarrow$ Koszul-régulière $\Rightarrow$
$H_1$-régulière $\Rightarrow$ quasi-régulière. Par des exemples, l'auteur montre que
ces implications ne sont en général pas réversibles, même si $R$ est un anneau local
(non noethérien) et si la suite engendre l'idéal maximal de
$R$. Nous présentons ces notions plus en détail dans
Compléments d'algèbre, section \ref{more-algebra-section-koszul-regular}.
\end{remark}
```

</details>

### 09 — remark-join-quasi-regular-sequences

Anglais L17099–17115 ; français L16865–16881.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17099) · FR-ALGEBRA-B35-CHOICE-0009.

Toutes les relations de l'anneau, le non-diviseur de zéro x, la suite de longueur1 après quotient et l'obstruction de rang2 restent identiques. La conclusion dit que l'analogue de concaténation échoue ; elle n'est pas changée en assertion que toute concaténation échoue. Le w non nul dans le quotient et le wx nul dans la conormale sont bien distincts.

Règles : FR-ALGEBRA-B35-RULE-QUASIREGULAR, FR-ALGEBRA-B35-RULE-MODULE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{remark}
\label{remark-join-quasi-regular-sequences}
Let $k$ be a field. Consider the ring
$$
A = k[x, y, w, z_0, z_1, z_2, \ldots]/
(y^2z_0 - wx, z_0 - yz_1, z_1 - yz_2, \ldots)
$$
In this ring $x$ is a nonzerodivisor and the image of $y$ in
$A/xA$ gives a quasi-regular sequence. But it is not true that
$x, y$ is a quasi-regular sequence in $A$ because $(x, y)/(x, y)^2$
isn't free of rank two over $A/(x, y)$ due to the fact that
$wx = 0$ in $(x, y)/(x, y)^2$ but $w$ isn't zero in $A/(x, y)$.
Hence the analogue of
Lemma \ref{lemma-join-regular-sequences}
does not hold for quasi-regular sequences.
\end{remark}
```

Français restauré :
```tex
\begin{remark}
\label{remark-join-quasi-regular-sequences}
Soit $k$ un corps. Considérons l'anneau
$$
A = k[x, y, w, z_0, z_1, z_2, \ldots]/
(y^2z_0 - wx, z_0 - yz_1, z_1 - yz_2, \ldots)
$$
Dans cet anneau, $x$ est un non-diviseur de zéro et l'image de $y$ dans
$A/xA$ donne une suite quasi-régulière. Mais il n'est pas vrai que la suite
$x, y$ soit quasi-régulière dans $A$, car $(x, y)/(x, y)^2$
n'est pas libre de rang deux sur $A/(x, y)$ : en effet,
$wx = 0$ dans $(x, y)/(x, y)^2$, tandis que $w$ n'est pas nul dans $A/(x, y)$.
Ainsi, l'analogue du
Lemme \ref{lemma-join-regular-sequences}
n'est pas vrai pour les suites quasi-régulières.
\end{remark}
```

</details>

### 10 — lemma-quasi-regular-on-quotient

Anglais L17116–17135 ; français L16882–16901.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17116) · FR-ALGEBRA-B35-CHOICE-0010.

Les intersections de toutes les puissances et les deux quotients, de l'anneau et du module, sont conservés. Les images et l'équivalence gardent leur sens. Le notons français est idiomatique malgré le by manquant dans denote de l'anglais, noté séparément ; aucune correction de contenu. L'isomorphisme des composantes graduées est comparé exactement.

Point particulier à relire : Notons l'image est retenu ; le by manquant de l'anglais n'est pas une omission mathématique du français. Pas d'amélioration de preuve.

Règles : FR-ALGEBRA-B35-RULE-QUASIREGULAR, FR-ALGEBRA-B35-RULE-MODULE, FR-ALGEBRA-B35-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-quasi-regular-on-quotient}
Let $R$ be a ring. Let $J = (f_1, \ldots, f_r)$ be an ideal of $R$.
Let $M$ be an $R$-module. Set $\overline{R} = R/\bigcap_{n \geq 0} J^n$,
$\overline{M} = M/\bigcap_{n \geq 0} J^nM$, and denote
$\overline{f}_i$ the image of $f_i$ in $\overline{R}$.
Then $f_1, \ldots, f_r$ is $M$-quasi-regular if and only if
$\overline{f}_1, \ldots, \overline{f}_r$ is $\overline{M}$-quasi-regular.
\end{lemma}

\begin{proof}
This is true because
$J^nM/J^{n + 1}M \cong
\overline{J}^n\overline{M}/\overline{J}^{n + 1}\overline{M}$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-quasi-regular-on-quotient}
Soit $R$ un anneau. Soit $J = (f_1, \ldots, f_r)$ un idéal de $R$.
Soit $M$ un $R$-module. Posons $\overline{R} = R/\bigcap_{n \geq 0} J^n$,
$\overline{M} = M/\bigcap_{n \geq 0} J^nM$, et notons
$\overline{f}_i$ l'image de $f_i$ dans $\overline{R}$.
Alors la suite $f_1, \ldots, f_r$ est $M$-quasi-régulière si et seulement si
la suite $\overline{f}_1, \ldots, \overline{f}_r$ est $\overline{M}$-quasi-régulière.
\end{lemma}

\begin{proof}
Cela est vrai parce que
$J^nM/J^{n + 1}M \cong
\overline{J}^n\overline{M}/\overline{J}^{n + 1}\overline{M}$.
\end{proof}
```

</details>

## Contrôles et suite

Les 197 régions mathématiques sont exactement identiques, sans exception nouvelle. Le préfixe de 12 176 régions passe avec quarante-trois exceptions linguistiques antérieures précisément recensées ; les différences sont vérifiées dans leur ordre et avec leurs multiplicités exactes.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items restent identiques. La citation Kabele est identique ; un titre facultatif de remarque est traduit, exactement enregistré. Les opérations inverses retrouvent le lot précédent puis tous les octets du témoin public préservé. Le fichier entier est inchangé dans ce lot.

Les 621 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Algèbres d’éclatement, anglais L17136 / français L16902. Aucun PDF nouveau ni publication ; restauration globale en cours.

