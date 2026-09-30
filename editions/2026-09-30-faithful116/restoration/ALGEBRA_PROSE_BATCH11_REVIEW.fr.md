# Algèbre commutative : extensions entières et anneaux normaux

## Résultat et portée

Deux sections entièrement comparées : anglais L7434–8338 et français L7414–8318, soit 905 lignes de chaque témoin. Les 43 paires comprennent tous les énoncés, preuves et transitions. 323 occurrences sont reliées à des règles contextualisées. Le préfixe atteint 37 sections, 295 paires et 2261 occurrences. Le chapitre et l’édition restent inachevés.

Cinq opérations exactes : réparation grammaticale de Soient … un ensemble ; deux substitutions complètement normal → complètement intégralement clos, à définition identique ; système inductif → système filtrant pour traduire directed ; retrait de non nul ajouté à une preuve anglaise. Ce dernier retrait restaure une lacune documentée hors traduction. Aucune formule ni référence ne change.

Trois observations séparées concernent cette condition non nulle, la convention incluant zéro dans un idéal de coefficients dominants, et un renvoi à Categories sans son préfixe. Ce ne sont pas trois nouveaux errata admis ou trois théorèmes faux.

Lecture, réparations et dossier produits par OpenAI Codex — GPT-6 Astra, Ultra effort ; comparaison assistée par IA, sans relecture humaine. Les attestations sont rétrospectives et limitées aux passages effectivement lus. Elles ne constituent pas une certification générale du français de toute l’édition.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch11.fr.tex) · [État français précédent](staged/fr/010_algebra.prose-batch10.fr.tex) · [Lot précédent](ALGEBRA_PROSE_BATCH10_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH11_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH11_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH11_OCCURRENCES.json) · [Avant/après](ALGEBRA_PROSE_BATCH11_REPAIRS.json) · [Exceptions linguistiques en formule](ALGEBRA_PROSE_BATCH11_MATH_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH11_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH11_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Antoine Ducros — Introduction à la théorie des schémas

[Source consultée](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages entières 62–63, 116–119 : 1.6.11.1–2 et 2.8.1–2.8.10.2 ; p.119 rendue et inspectée.

Attestations courtes : « diagramme commutatif filtrant », « polynôme unitaire », « fermeture intégrale », « clôture intégrale », « intégralement clos ».

Finitude comme module, intégralité, localisation et normalité. La condition filtrante est explicitement non vide avec majorants communs ; elle justifie la précision traduite dans le dernier lemme.

Limites : Le cours réserve clôture au corps des fractions contrairement à Dat. La mention 1⊗c de C p.119 est une coquille de type non importée. P.62, la première équation de cocône et la désignation pi du cône comportent aussi des indices incohérents ; seuls les passages correctement typés servent ici. L'exemple de p.118 et la discussion de p.63 se poursuivent hors page ; aucune lecture de leurs suites non consultées n'est revendiquée.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

### Jean-François Dat — Algèbre, ENS 2016–2017

[Source consultée](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/AlgebreM1/ENS1617.pdf) · [Fichier conservé](canon-consulted/fr-algebra/dat-algebre-ens1617.pdf)

Pages PDF/imprimées 144–145 entièrement lues : corollaire Cayley-Hamilton, 2.12.2, 2.12.3 et définition de normal.

Attestations courtes : « clôture intégrale de A dans B », « normalisation », « intégralement clos ».

Attestation de clôture intégrale pour une A-algèbre générale ; distinction type fini de module et entier ; normal dans le cas intègre.

Limites : L'exemple avec (1+√−3)/2 porte X³−1 au lieu de X³+1 ; le commentaire sur le coefficient am de la caractéristique oublie le signe (−1)^m. Ces expressions ne sont pas utilisées comme autorité de formules. La fin de l'exemple de courbe se poursuit p.146 non lue ici.

SHA-256 : DB5B7FD8139D62C37D0DDDDC90EF22D3EDCF74CC663C5267815E4EA3CECBBB18.

### Yves André — Le lemme d’Abhyankar perfectoïde

[Source consultée](https://numdam.org/item/10.1007/s10240-017-0096-x.pdf) · [Fichier conservé](canon-consulted/fr-algebra/andre-abhyankar-perfectoide.pdf)

Pages entières 14–15 et 57 ; définition 2.3.1 p.15 et expression de 4.2.6 p.57 ; p.15 rendue et inspectée.

Attestations courtes : « presque entier », « complètement intégralement fermé », « complètement intégralement clos ».

La définition par puissances dans un module fini est comparée à celle par dénominateur commun dans un corps des fractions ; l'équivalence est démontrée dans le motif du choix, pas présumée par homonymie.

Limites : Le cadre perfectoïde des résultats de p.57 n'est pas transféré à Stacks. Seuls le vocabulaire et la définition générale de 2.3.1 servent. Les passages avant et après 4.2.6 se poursuivent sur des pages non consultées : aucune revue complète de l'article ni validation de ses théorèmes n'est revendiquée.

SHA-256 : 087521436778EED56E5BAC98F6F2B441BC2898EEF35EBBA9DA1C1575BF00F96A.

### Stacks Project officiel — Categories, systèmes filtrants

[Source consultée](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex#L2692) · [Fichier conservé](../../03_working_translations/stacks_cjk_20260821/upstream/src/stacks-project-a04446e57ec1fbc252a871afcec7752fb2807b14/categories.tex)

Définition definition-directed-system L2692 et paragraphe suivant lus ; comparaison avec le label homonyme dans Algebra L715.

Attestations courtes : « directed system », « I is nonempty ».

Contrôle du quantificateur de filtrance et constat de la collision entre référence locale et chapitre Categories.

Limites : Source anglaise de contenu, non attestation du registre français. Le préfixe absent est signalé seulement dans les observations séparées.

SHA-256 : 62F7611AF4C3FEEBD041DB4728B42C7112004CFBB9FA5ECB643C6F5D90DB3F25.

## Les cinq opérations exactes

### FR-ALGEBRA-B11-REPAIR-0001

Anglais L7483 ; français L7463.

Avant :
```tex
un ensemble fini d'éléments de $S$.
```

Après :
```tex
des éléments de $S$ en nombre fini.
```

Réparation grammaticale : les si sont des éléments en nombre fini, pas un ensemble singulier après Soient. Aucun générateur n'est ajouté.

### FR-ALGEBRA-B11-REPAIR-0002

Anglais L7805 ; français L7785.

Avant :
```tex
Choisissons $s\in S$ non nul.
```

Après :
```tex
Choisissons $s\in S$.
```

L'anglais choisit s sans préciser s≠0 à cet endroit. Le français retirera son ajout non nul, mais la note séparée montre que multiplication par zéro n'est pas surjective dans un corps non nul. La traduction n'est pas une édition mathématique corrigée.

### FR-ALGEBRA-B11-REPAIR-0003

Anglais L8007 ; français L7987.

Avant :
```tex
{\it complètement normal}
```

Après :
```tex
{\it complètement intégralement clos}
```

Deux occurrences seulement de complètement normal figurent dans le témoin du chapitre ; toutes deux appartiennent à ce passage. Choix de complètement intégralement clos plutôt que complètement intégralement fermé pour cohérence avec intégralement clos ; les deux variantes sont attestées chez André. Ce choix lexical ne remplace ni la définition ni l'hypothèse noethérienne.

### FR-ALGEBRA-B11-REPAIR-0004

Anglais L8015 ; français L7995.

Avant :
```tex
si et seulement s'il est complètement normal.
```

Après :
```tex
si et seulement s'il est complètement intégralement clos.
```

Deux occurrences seulement de complètement normal figurent dans le témoin du chapitre ; toutes deux appartiennent à ce passage. Choix de complètement intégralement clos plutôt que complètement intégralement fermé pour cohérence avec intégralement clos ; les deux variantes sont attestées chez André. Ce choix lexical ne remplace ni la définition ni l'hypothèse noethérienne.

### FR-ALGEBRA-B11-REPAIR-0005

Anglais L8313 ; français L8293.

Avant :
```tex
Soit $(R_i, \varphi_{ii'})$ un système inductif
```

Après :
```tex
Soit $(R_i, \varphi_{ii'})$ un système filtrant
```

Système filtrant traduit la qualification explicite directed et reprend la définition déjà donnée. Le renvoi sans categories- reste une anomalie officielle distincte, non réparée dans le témoin fidèle.

## Règles contextualisées

### FR-ALGEBRA-B11-RULE-INTEGRAL

Entier qualifie un élément ou morphisme annulant des équations unitaires ; distinguer l'adjectif entier du nom entier dans un indice. Les contextes complets donnent le référent.

Canon : FR-ALGEBRA-B11-CANON-DUCROS, FR-ALGEBRA-B11-CANON-DAT.

### FR-ALGEBRA-B11-RULE-CLOTURE

Clôture relative dans S ou dans Frac(R), selon le passage. Les variantes fermeture/clôture sont attestées ; le choix de Dat est maintenu sans exclusivité prétendue.

Canon : FR-ALGEBRA-B11-CANON-DAT, FR-ALGEBRA-B11-CANON-DUCROS.

### FR-ALGEBRA-B11-RULE-PRESQUE

Condition uniforme sur toutes les puissances ; équivalence des définitions justifiée dans Frac(R). Aucun sens de presque-algèbre n'est importé.

Canon : FR-ALGEBRA-B11-CANON-ANDRE.

### FR-ALGEBRA-B11-RULE-FINITE

Toujours identifier module, algèbre, dimension vectorielle ou ensemble de points. Ces notions de finitude ne sont pas substituables.

Canon : FR-ALGEBRA-B11-CANON-DUCROS, FR-ALGEBRA-B11-CANON-DAT.

### FR-ALGEBRA-B11-RULE-NORMAL

Définition dans le corps des fractions pour un domaine, définition locale pour un anneau général ; pas d'intégrité globale ajoutée.

Canon : FR-ALGEBRA-B11-CANON-DUCROS, FR-ALGEBRA-B11-CANON-DAT.

### FR-ALGEBRA-B11-RULE-LOCAL

Dénominateurs, base et anneau ambiant sont vérifiés ; corps des fractions est réservé au cas intègre. Les localisations peuvent avoir des diviseurs de zéro avant passage au cas normal local.

Canon : FR-ALGEBRA-B11-CANON-DUCROS.

### FR-ALGEBRA-B11-RULE-POLYNOME

La monicité et les puissances sont exactes. Une famille génératrice de monômes n'est appelée base que là où la source prouve la liberté. Aucune interprétation analytique des séries.

Canon : FR-ALGEBRA-B11-CANON-DUCROS, FR-ALGEBRA-B11-CANON-DAT.

### FR-ALGEBRA-B11-RULE-FILTRANT

La filtrance est la condition de majorants communs, non l'injectivité des transitions. Le nombre fini de coefficients et relations permet le stade commun.

Canon : FR-ALGEBRA-B11-CANON-DUCROS, FR-ALGEBRA-B11-CANON-CATEGORIES.

### FR-ALGEBRA-B11-RULE-LOGIQUE

Portée des quantificateurs et conditions zéro/non-zéro comparées dans chaque paire. Une correction de preuve anglaise n'est pas introduite silencieusement.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B11-RULE-PREMIERS

Distinguer contraction, fibre spectrale et localisation ; montée décrit l'inclusion ascendante fixée par la source. Appui compositionnel explicite lorsque les pages consultées n'attestent pas le terme exact.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-finite-ring-extensions

Anglais L7434–7440 ; français L7414–7420.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7434) · FR-ALGEBRA-B11-CHOICE-0001.

Le titre distingue les extensions finies des extensions entières. Le paragraphe emploie morphisme plutôt que de supposer une inclusion : l'anglais traite des ring maps quelconques. Élémentaires rend ici trivial sans déprécier la lecture.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Finite and integral ring extensions}
\label{section-finite-ring-extensions}

\noindent
Trivial lemmas concerning finite and integral ring maps.
We recall the definition.
```

Français restauré :
```tex
\section{Extensions d'anneaux finies et entières}
\label{section-finite-ring-extensions}

\noindent
Lemmes élémentaires concernant les morphismes d'anneaux finis et entiers.
Rappelons la définition.
```

</details>

### 02 — definition-integral-ring-map

Anglais L7441–7454 ; français L7421–7434.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7441) · FR-ALGEBRA-B11-CHOICE-0002.

Entier sur R traduit la propriété d'annuler un polynôme unitaire, non l'appartenance aux entiers. Ducros 2.8.3 et Dat 2.12.2 attestent ce sens et unitaire. Le changement de coefficients par φ et la quantification sur tout s sont conservés, sans injectivité ajoutée.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-POLYNOME, FR-ALGEBRA-B11-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-integral-ring-map}
Let $\varphi : R \to S$ be a ring map.
\begin{enumerate}
\item An element $s \in S$
is {\it integral over $R$} if there exists a monic
polynomial $P(x) \in R[x]$ such that
$P^\varphi(s) = 0$, where $P^\varphi(x) \in S[x]$
is the image of $P$ under $\varphi : R[x] \to S[x]$.
\item  The ring map $\varphi$ is {\it integral}
if every $s \in S$ is integral over $R$.
\end{enumerate}
\end{definition}
```

Français restauré :
```tex
\begin{definition}
\label{definition-integral-ring-map}
Soit $\varphi : R \to S$ un morphisme d'anneaux.
\begin{enumerate}
\item Un élément $s \in S$
est {\it entier sur $R$} s'il existe un polynôme
unitaire $P(x) \in R[x]$ tel que
$P^\varphi(s) = 0$, où $P^\varphi(x) \in S[x]$
est l'image de $P$ par $\varphi : R[x] \to S[x]$.
\item Le morphisme d'anneaux $\varphi$ est {\it entier}
si tout $s \in S$ est entier sur $R$.
\end{enumerate}
\end{definition}
```

</details>

### 03 — lemma-characterize-integral-element

Anglais L7455–7468 ; français L7435–7448.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7455) · FR-ALGEBRA-B11-CHOICE-0003.

Finite R-submodule devient sous-R-module de type fini, et non ensemble fini. La stabilité sous multiplication et 1∈M sont toutes deux conservées ; évaluer P(φ) en 1 est l'étape qui conclut. Dat p.144 et Ducros p.117 donnent le registre de cet argument. Le réemploi de φ pour l'endomorphisme reste celui de la source.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-FINITE, FR-ALGEBRA-B11-RULE-POLYNOME, FR-ALGEBRA-B11-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-integral-element}
Let $\varphi : R \to S$ be a ring map. Let $y \in S$. If there exists a
finite $R$-submodule $M$ of $S$ such that $1 \in M$ and $yM \subset M$,
then $y$ is integral over $R$.
\end{lemma}

\begin{proof}
Consider the map $\varphi : M \to M$, $x \mapsto y \cdot x$.
By Lemma \ref{lemma-charpoly-module} there exists a monic polynomial
$P \in R[T]$ with $P(\varphi) = 0$. In the ring $S$ we get
$P(y) = P(y) \cdot 1 = P(\varphi)(1) = 0$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-characterize-integral-element}
Soit $\varphi : R \to S$ un morphisme d'anneaux. Soit $y \in S$. S'il existe un
sous-$R$-module de type fini $M$ de $S$ tel que $1 \in M$ et $yM \subset M$,
alors $y$ est entier sur $R$.
\end{lemma}

\begin{proof}
Considérons l'application $\varphi : M \to M$, $x \mapsto y \cdot x$.
D'après le lemme \ref{lemma-charpoly-module}, il existe un polynôme unitaire
$P \in R[T]$ tel que $P(\varphi) = 0$. Dans l'anneau $S$, nous obtenons
$P(y) = P(y) \cdot 1 = P(\varphi)(1) = 0$.
\end{proof}
```

</details>

### 04 — lemma-finite-is-integral

Anglais L7469–7479 ; français L7449–7459.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7469) · FR-ALGEBRA-B11-CHOICE-0004.

Fini qualifie le morphisme par la génération du module cible. L'application au module S entier, et non à une sous-algèbre choisie arbitrairement, reste explicite. Le théorème est attesté chez Ducros 2.8.4.1.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-finite-is-integral}
A finite ring map is integral.
\end{lemma}

\begin{proof}
Let $R \to S$ be finite. Let $y \in S$. Apply
Lemma \ref{lemma-characterize-integral-element}
to $M = S$ to see that $y$ is integral over $R$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-finite-is-integral}
Un morphisme d'anneaux fini est entier.
\end{lemma}

\begin{proof}
Soit $R \to S$ fini. Soit $y \in S$. Appliquons le
lemme \ref{lemma-characterize-integral-element}
à $M = S$ pour voir que $y$ est entier sur $R$.
\end{proof}
```

</details>

### 05 — lemma-characterize-integral

Anglais L7480–7501 ; français L7460–7481.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7480) · FR-ALGEBRA-B11-CHOICE-0005.

La famille finie s1,…,sn est contenue dans une sous-algèbre finie comme module. La phrase Soient … un ensemble est réparée en Soient … des éléments … en nombre fini. Les monômes bornés sont des générateurs, pas une base : aucune indépendance linéaire n'est ajoutée. Les deux implications et les bornes ei≤di−1 sont conservées.

Point particulier à relire : Réparation grammaticale : les si sont des éléments en nombre fini, pas un ensemble singulier après Soient. Aucun générateur n'est ajouté.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-FINITE, FR-ALGEBRA-B11-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-integral}
Let $\varphi : R \to S$ be a ring map. Let $s_1, \ldots, s_n$
be a finite set of elements of $S$.
In this case $s_i$ is integral over $R$ for all $i = 1, \ldots, n$
if and only if
there exists an $R$-subalgebra $S' \subset S$ finite over $R$
containing all of the $s_i$.
\end{lemma}

\begin{proof}
If each $s_i$ is integral, then the subalgebra
generated by $\varphi(R)$ and the $s_i$ is finite
over $R$. Namely, if $s_i$ satisfies a monic equation
of degree $d_i$ over $R$, then this subalgebra is generated as an
$R$-module by the elements $s_1^{e_1} \ldots s_n^{e_n}$
with $0 \leq e_i \leq d_i - 1$.
Conversely, suppose given a finite $R$-subalgebra
$S'$ containing all the $s_i$. Then all of the
$s_i$ are integral by Lemma \ref{lemma-finite-is-integral}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-characterize-integral}
Soit $\varphi : R \to S$ un morphisme d'anneaux. Soient $s_1, \ldots, s_n$
des éléments de $S$ en nombre fini.
Alors les $s_i$ sont entiers sur $R$ pour tout $i = 1, \ldots, n$
si et seulement s'il
existe une $R$-sous-algèbre $S' \subset S$ finie sur $R$
qui contient tous les $s_i$.
\end{lemma}

\begin{proof}
Si chaque $s_i$ est entier, alors la sous-algèbre
engendrée par $\varphi(R)$ et les $s_i$ est finie
sur $R$. En effet, si $s_i$ satisfait une équation unitaire
de degré $d_i$ sur $R$, alors cette sous-algèbre est engendrée comme
$R$-module par les éléments $s_1^{e_1} \ldots s_n^{e_n}$
avec $0 \leq e_i \leq d_i - 1$.
Réciproquement, supposons donnée une $R$-sous-algèbre finie
$S'$ qui contient tous les $s_i$. Alors tous les
$s_i$ sont entiers d'après le lemme \ref{lemma-finite-is-integral}.
\end{proof}
```

</details>

### 06 — lemma-characterize-finite-in-terms-of-integral

Anglais L7502–7516 ; français L7482–7496.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7502) · FR-ALGEBRA-B11-CHOICE-0006.

Les trois conditions sont distinctes : finitude du module, intégralité avec type fini d'algèbre, génération par un nombre fini d'éléments entiers. Ducros 2.8.5 énonce précisément cette équivalence. Type fini seul n'est jamais rendu par fini dans cette argumentation.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-FINITE, FR-ALGEBRA-B11-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-finite-in-terms-of-integral}
Let $R \to S$ be a ring map. The following are equivalent
\begin{enumerate}
\item $R \to S$ is finite,
\item $R \to S$ is integral and of finite type, and
\item there exist $x_1, \ldots, x_n \in S$ which generate $S$ as an
algebra over $R$ such that each $x_i$ is integral over $R$.
\end{enumerate}
\end{lemma}

\begin{proof}
Clear from Lemma \ref{lemma-characterize-integral}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-characterize-finite-in-terms-of-integral}
Soit $R \to S$ un morphisme d'anneaux. Les propriétés suivantes sont équivalentes :
\begin{enumerate}
\item $R \to S$ est fini,
\item $R \to S$ est entier et de type fini, et
\item il existe $x_1, \ldots, x_n \in S$ qui engendrent $S$ comme
algèbre sur $R$ et tels que chaque $x_i$ soit entier sur $R$.
\end{enumerate}
\end{lemma}

\begin{proof}
C'est clair d'après le lemme \ref{lemma-characterize-integral}.
\end{proof}
```

</details>

### 07 — lemma-integral-transitive

Anglais L7517–7540 ; français L7497–7520.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7517) · FR-ALGEBRA-B11-CHOICE-0007.

Intégralité et composée rendent les morphismes, sans supposer toutes les algèbres finies. On réduit à la liste finie des coefficients de P, puis aux sous-algèbres S′ et T′, seules déclarées finies. Ducros 2.8.7 confirme ce vocabulaire et cette réduction, sans remplacer la preuve source.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-FINITE, FR-ALGEBRA-B11-RULE-POLYNOME.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-integral-transitive}
\begin{slogan}
A composition of integral ring maps is integral
\end{slogan}
Suppose that $R \to S$ and $S \to T$ are integral
ring maps. Then $R \to T$ is integral.
\end{lemma}

\begin{proof}
Let $t \in T$. Let $P(x) \in S[x]$ be a
monic polynomial such that $P(t) = 0$.
Apply Lemma \ref{lemma-characterize-integral}
to the finite set of coefficients of $P$.
Hence $t$ is integral over some subalgebra
$S' \subset S$ finite over $R$. Apply Lemma
\ref{lemma-characterize-integral} again to find
a subalgebra $T' \subset T$ finite over $S'$ and
containing $t$. Lemma \ref{lemma-finite-transitive}
applied to $R \to S' \to T'$ shows that $T'$ is finite
over $R$. The integrality of $t$ over $R$
now follows from Lemma \ref{lemma-finite-is-integral}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-integral-transitive}
\begin{slogan}
Une composée de morphismes d'anneaux entiers est entière
\end{slogan}
Supposons que $R \to S$ et $S \to T$ soient des
morphismes d'anneaux entiers. Alors $R \to T$ est entier.
\end{lemma}

\begin{proof}
Soit $t \in T$. Soit $P(x) \in S[x]$ un
polynôme unitaire tel que $P(t) = 0$.
Appliquons le lemme \ref{lemma-characterize-integral}
à l'ensemble fini des coefficients de $P$.
Ainsi, $t$ est entier sur une certaine sous-algèbre
$S' \subset S$ finie sur $R$. Appliquons à nouveau le lemme
\ref{lemma-characterize-integral} pour trouver
une sous-algèbre $T' \subset T$ finie sur $S'$ et
contenant $t$. Le lemme \ref{lemma-finite-transitive}
appliqué à $R \to S' \to T'$ montre que $T'$ est finie
sur $R$. L'intégralité de $t$ sur $R$
résulte alors du lemme \ref{lemma-finite-is-integral}.
\end{proof}
```

</details>

### 08 — lemma-integral-closure-is-ring

Anglais L7541–7555 ; français L7521–7535.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7541) · FR-ALGEBRA-B11-CHOICE-0008.

La propriété entier sur R à l'intérieur du texte de la formule est traduite, mais le domaine S et la condition définissant S′ sont identiques. Une exception exacte, limitée à cette région, distingue traduction de texte et changement de mathématiques. Clôture sous les opérations résulte des deux lemmes indiqués ; aucune nouvelle preuve n'est insérée.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-integral-closure-is-ring}
Let $R \to S$ be a ring homomorphism.
The set
$$
S' = \{s \in S \mid s\text{ is integral over }R\}
$$
is an $R$-subalgebra of $S$.
\end{lemma}

\begin{proof}
This is clear from Lemmas \ref{lemma-characterize-integral}
and \ref{lemma-finite-is-integral}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-integral-closure-is-ring}
Soit $R \to S$ un morphisme d'anneaux.
L'ensemble
$$
S' = \{s \in S \mid s\text{ est entier sur }R\}
$$
est une $R$-sous-algèbre de $S$.
\end{lemma}

\begin{proof}
C'est clair d'après les lemmes \ref{lemma-characterize-integral}
et \ref{lemma-finite-is-integral}.
\end{proof}
```

</details>

### 09 — lemma-finite-product-integral

Anglais L7556–7567 ; français L7536–7547.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7556) · FR-ALGEBRA-B11-CHOICE-0009.

Les produits comportent les n facteurs indiqués ; l'équivalence est composante par composante, sans extension au produit infini. Respectivement préserve les deux familles R et S. La démonstration omise reste signalée comme omise.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-finite-product-integral}
Let $R_i\to S_i$ be ring maps $i = 1, \ldots, n$.
Let $R$ and $S$ denote the product of the $R_i$ and $S_i$ respectively.
Then an element $s = (s_1, \ldots, s_n) \in S$ is integral over $R$
if and only if each $s_i$ is integral over $R_i$.
\end{lemma}

\begin{proof}
Omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-finite-product-integral}
Soient $R_i\to S_i$ des morphismes d'anneaux, $i = 1, \ldots, n$.
Notons respectivement $R$ et $S$ les produits des $R_i$ et des $S_i$.
Alors un élément $s = (s_1, \ldots, s_n) \in S$ est entier sur $R$
si et seulement si chaque $s_i$ est entier sur $R_i$.
\end{lemma}

\begin{proof}
Omis.
\end{proof}
```

</details>

### 10 — definition-integral-closure

Anglais L7568–7581 ; français L7548–7561.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7568) · FR-ALGEBRA-B11-CHOICE-0010.

Clôture intégrale dans une algèbre quelconque est explicitement attesté par Dat 2.12.3 ; Ducros appelle ce cas fermeture intégrale et réserve clôture à l'anneau dans son corps des fractions. On conserve ici le choix cohérent et attesté de Dat. La condition R⊂S ne concerne que la définition intégralement clos, pas le morphisme initial.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-CLOTURE, FR-ALGEBRA-B11-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-integral-closure}
Let $R \to S$ be a ring map.
The ring $S' \subset S$ of elements integral over
$R$, see Lemma \ref{lemma-integral-closure-is-ring},
is called the {\it integral closure} of $R$
in $S$. If $R \subset S$ we say that $R$ is
{\it integrally closed} in $S$ if $R = S'$.
\end{definition}

\noindent
In particular, we see that $R \to S$ is integral if and only
if the integral closure of $R$ in $S$ is all of $S$.
```

Français restauré :
```tex
\begin{definition}
\label{definition-integral-closure}
Soit $R \to S$ un morphisme d'anneaux.
L'anneau $S' \subset S$ des éléments entiers sur
$R$, voir le lemme \ref{lemma-integral-closure-is-ring},
est appelé la {\it clôture intégrale} de $R$
dans $S$. Si $R \subset S$, nous disons que $R$ est
{\it intégralement clos} dans $S$ si $R = S'$.
\end{definition}

\noindent
En particulier, nous voyons que $R \to S$ est entier si et seulement
si la clôture intégrale de $R$ dans $S$ est $S$ tout entier.
```

</details>

### 11 — lemma-finite-product-integral-closure

Anglais L7582–7595 ; français L7562–7575.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7582) · FR-ALGEBRA-B11-CHOICE-0011.

La clôture du produit est le produit des clôtures, sans changer les indices ou la finitude. Le texte appelle ensuite le morphisme intégralement clos : c'est la terminologie elliptique anglaise, alors que la définition précédente formule cette propriété pour une inclusion. Aucune hypothèse injective n'est subrepticement ajoutée.

Règles : FR-ALGEBRA-B11-RULE-CLOTURE, FR-ALGEBRA-B11-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-finite-product-integral-closure}
Let $R_i\to S_i$ be ring maps $i = 1, \ldots, n$.
Denote the integral closure of $R_i$ in $S_i$ by $S'_i$.
Further let $R$ and $S$ denote the product of the $R_i$ and $S_i$ respectively.
Then the integral closure of $R$ in $S$
is the product of the $S'_i$. In particular $R \to S$ is
integrally closed if and only if each $R_i \to S_i$ is integrally closed.
\end{lemma}

\begin{proof}
This follows immediately from Lemma \ref{lemma-finite-product-integral}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-finite-product-integral-closure}
Soient $R_i\to S_i$ des morphismes d'anneaux, $i = 1, \ldots, n$.
Notons la clôture intégrale de $R_i$ dans $S_i$ par $S'_i$.
Notons en outre respectivement $R$ et $S$ les produits des $R_i$ et des $S_i$.
Alors la clôture intégrale de $R$ dans $S$
est le produit des $S'_i$. En particulier, $R \to S$ est
intégralement clos si et seulement si chaque $R_i \to S_i$ est intégralement clos.
\end{lemma}

\begin{proof}
Cela résulte immédiatement du lemme \ref{lemma-finite-product-integral}.
\end{proof}
```

</details>

### 12 — lemma-integral-closure-localize

Anglais L7596–7628 ; français L7576–7608.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7596) · FR-ALGEBRA-B11-CHOICE-0012.

Partie multiplicative et localisation sont gardés distincts de complément d'un seul idéal premier. L'exactitude fournit l'inclusion après localisation même si A→B n'est pas injectif. Les facteurs f, f′, fi et toutes leurs puissances sont contrôlés dans la chasse aux dénominateurs ; la réciproque donne un multiple entier avant de retrouver x/f.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-CLOTURE, FR-ALGEBRA-B11-RULE-LOCAL, FR-ALGEBRA-B11-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-integral-closure-localize}
Integral closure commutes with localization: If $A \to B$ is a ring
map, and $S \subset A$ is a multiplicative subset, then the integral
closure of $S^{-1}A$ in $S^{-1}B$ is $S^{-1}B'$, where $B' \subset B$
is the integral closure of $A$ in $B$.
\end{lemma}

\begin{proof}
Since localization is exact we see that $S^{-1}B' \subset S^{-1}B$.
Suppose $x \in B'$ and $f \in S$. Then
$x^d + \sum_{i = 1, \ldots, d} a_i x^{d - i} = 0$
in $B$ for some $a_i \in A$. Hence also
$$
(x/f)^d + \sum\nolimits_{i = 1, \ldots, d} a_i/f^i (x/f)^{d - i} = 0
$$
in $S^{-1}B$. In this way we see that $S^{-1}B'$ is contained in
the integral closure of $S^{-1}A$ in $S^{-1}B$. Conversely, suppose
that $x/f \in S^{-1}B$ is integral over $S^{-1}A$. Then we have
$$
(x/f)^d + \sum\nolimits_{i = 1, \ldots, d} (a_i/f_i) (x/f)^{d - i} = 0
$$
in $S^{-1}B$ for some $a_i \in A$ and $f_i \in S$. This means that
$$
(f'f_1 \ldots f_d x)^d +
\sum\nolimits_{i = 1, \ldots, d}
f^i(f')^if_1^i \ldots f_i^{i - 1} \ldots f_d^i a_i
(f'f_1 \ldots f_dx)^{d - i} = 0
$$
for a suitable $f' \in S$. Hence $f'f_1\ldots f_dx \in B'$ and thus
$x/f \in S^{-1}B'$ as desired.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-integral-closure-localize}
La clôture intégrale commute à la localisation : si $A \to B$ est un
morphisme d'anneaux et $S \subset A$ une partie multiplicative, alors la clôture
intégrale de $S^{-1}A$ dans $S^{-1}B$ est $S^{-1}B'$, où $B' \subset B$
est la clôture intégrale de $A$ dans $B$.
\end{lemma}

\begin{proof}
Puisque la localisation est exacte, nous voyons que $S^{-1}B' \subset S^{-1}B$.
Supposons que $x \in B'$ et $f \in S$. Alors
$x^d + \sum_{i = 1, \ldots, d} a_i x^{d - i} = 0$
dans $B$ pour certains $a_i \in A$. Ainsi,
$$
(x/f)^d + \sum\nolimits_{i = 1, \ldots, d} a_i/f^i (x/f)^{d - i} = 0
$$
dans $S^{-1}B$. Nous voyons ainsi que $S^{-1}B'$ est contenu dans
la clôture intégrale de $S^{-1}A$ dans $S^{-1}B$. Réciproquement, supposons
que $x/f \in S^{-1}B$ soit entier sur $S^{-1}A$. Alors nous avons
$$
(x/f)^d + \sum\nolimits_{i = 1, \ldots, d} (a_i/f_i) (x/f)^{d - i} = 0
$$
dans $S^{-1}B$ pour certains $a_i \in A$ et $f_i \in S$. Cela signifie que
$$
(f'f_1 \ldots f_d x)^d +
\sum\nolimits_{i = 1, \ldots, d}
f^i(f')^if_1^i \ldots f_i^{i - 1} \ldots f_d^i a_i
(f'f_1 \ldots f_dx)^{d - i} = 0
$$
pour un $f' \in S$ convenable. Ainsi, $f'f_1\ldots f_dx \in B'$ et donc
$x/f \in S^{-1}B'$, comme voulu.
\end{proof}
```

</details>

### 13 — lemma-integral-closure-stalks

Anglais L7629–7663 ; français L7609–7643.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7629) · FR-ALGEBRA-B11-CHOICE-0013.

Localement signifie ici en chaque idéal premier de R, pas en chaque premier de S. La quasi-compacité réduit ensuite aux ouverts dont les éléments engendrent l'idéal unité. Les localisations de φ sur les coefficients sont les raccourcis de la source, non un changement de domaine.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-FINITE, FR-ALGEBRA-B11-RULE-LOCAL, FR-ALGEBRA-B11-RULE-LOGIQUE, FR-ALGEBRA-B11-RULE-PREMIERS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-integral-closure-stalks}
\begin{slogan}
An element of an algebra over a ring is integral over the ring
if and only if it is locally integral at every prime ideal of the ring.
\end{slogan}
Let $\varphi : R \to S$ be a ring map.
Let $x \in S$. The following are equivalent:
\begin{enumerate}
\item $x$ is integral over $R$, and
\item for every prime ideal $\mathfrak p \subset R$ the element
$x \in S_{\mathfrak p}$ is integral over $R_{\mathfrak p}$.
\end{enumerate}
\end{lemma}

\begin{proof}
It is clear that (1) implies (2). Assume (2). Consider the $R$-algebra
$S' \subset S$ generated by $\varphi(R)$ and $x$. Let $\mathfrak p$ be
a prime ideal of $R$. Then we know that
$x^d + \sum_{i = 1, \ldots, d} \varphi(a_i) x^{d - i} = 0$
in $S_{\mathfrak p}$ for some $a_i \in R_{\mathfrak p}$. Hence we see,
by looking at which denominators occur, that
for some $f \in R$, $f \not \in \mathfrak p$ we have
$a_i \in R_f$ and
$x^d + \sum_{i = 1, \ldots, d} \varphi(a_i) x^{d - i} = 0$
in $S_f$. This implies that $S'_f$ is finite over $R_f$.
Since $\mathfrak p$ was arbitrary and $\Spec(R)$ is quasi-compact
(Lemma \ref{lemma-quasi-compact}) we can find finitely many elements
$f_1, \ldots, f_n \in R$
which generate the unit ideal of $R$ such that $S'_{f_i}$ is finite
over $R_{f_i}$. Hence we conclude from Lemma \ref{lemma-cover} that
$S'$ is finite over $R$. Hence $x$ is integral over $R$ by
Lemma \ref{lemma-characterize-integral}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-integral-closure-stalks}
\begin{slogan}
Un élément d'une algèbre sur un anneau est entier sur cet anneau
si et seulement s'il est localement entier en tout idéal premier de l'anneau.
\end{slogan}
Soit $\varphi : R \to S$ un morphisme d'anneaux.
Soit $x \in S$. Les propriétés suivantes sont équivalentes :
\begin{enumerate}
\item $x$ est entier sur $R$, et
\item pour tout idéal premier $\mathfrak p \subset R$, l'élément
$x \in S_{\mathfrak p}$ est entier sur $R_{\mathfrak p}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Il est clair que (1) implique (2). Supposons (2). Considérons la $R$-algèbre
$S' \subset S$ engendrée par $\varphi(R)$ et $x$. Soit $\mathfrak p$ un
idéal premier de $R$. Nous savons alors que
$x^d + \sum_{i = 1, \ldots, d} \varphi(a_i) x^{d - i} = 0$
dans $S_{\mathfrak p}$ pour certains $a_i \in R_{\mathfrak p}$. En examinant
les dénominateurs qui interviennent, nous voyons donc que,
pour un certain $f \in R$, $f \not \in \mathfrak p$, nous avons
$a_i \in R_f$ et
$x^d + \sum_{i = 1, \ldots, d} \varphi(a_i) x^{d - i} = 0$
dans $S_f$. Cela implique que $S'_f$ est fini sur $R_f$.
Puisque $\mathfrak p$ était arbitraire et que $\Spec(R)$ est quasi-compact
(lemme \ref{lemma-quasi-compact}), nous pouvons trouver un nombre fini d'éléments
$f_1, \ldots, f_n \in R$
qui engendrent l'idéal unité de $R$ tels que $S'_{f_i}$ soit fini
sur $R_{f_i}$. Nous concluons donc du lemme \ref{lemma-cover} que
$S'$ est fini sur $R$. Ainsi, $x$ est entier sur $R$ d'après le
lemme \ref{lemma-characterize-integral}.
\end{proof}
```

</details>

### 14 — lemma-base-change-integral

Anglais L7664–7687 ; français L7644–7667.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7664) · FR-ALGEBRA-B11-CHOICE-0014.

Le changement de base est le produit tensoriel R′⊗R S, avec les nouveaux générateurs 1⊗si. Aucune finitude de la famille des si n'est exigée dans la partie entière. La preuve de la partie finie reste omise, comme en anglais. Ducros 2.8.9 atteste les deux propriétés.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-base-change-integral}
\begin{slogan}
Integrality and finiteness are preserved under base change.
\end{slogan}
Let $R \to S$ and $R \to R'$ be ring maps.
Set $S' = R' \otimes_R S$.
\begin{enumerate}
\item If $R \to S$ is integral so is $R' \to S'$.
\item If $R \to S$ is finite so is $R' \to S'$.
\end{enumerate}
\end{lemma}

\begin{proof}
We prove (1).
Let $s_i \in S$ be generators for $S$ over $R$.
Each of these satisfies a monic polynomial equation $P_i$
over $R$. Hence the elements $1 \otimes s_i \in S'$ generate
$S'$ over $R'$ and satisfy the corresponding polynomial
$P_i'$ over $R'$. Since these elements generate $S'$ over $R'$
we see that $S'$ is integral over $R'$.
Proof of (2) omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-base-change-integral}
\begin{slogan}
L'intégralité et la finitude sont préservées par changement de base.
\end{slogan}
Soient $R \to S$ et $R \to R'$ des morphismes d'anneaux.
Posons $S' = R' \otimes_R S$.
\begin{enumerate}
\item Si $R \to S$ est entier, alors $R' \to S'$ l'est aussi.
\item Si $R \to S$ est fini, alors $R' \to S'$ l'est aussi.
\end{enumerate}
\end{lemma}

\begin{proof}
Nous démontrons (1).
Soient $s_i \in S$ des générateurs de $S$ sur $R$.
Chacun d'eux satisfait une équation polynomiale unitaire $P_i$
sur $R$. Ainsi, les éléments $1 \otimes s_i \in S'$ engendrent
$S'$ sur $R'$ et satisfont le polynôme correspondant
$P_i'$ sur $R'$. Puisque ces éléments engendrent $S'$ sur $R'$,
nous voyons que $S'$ est entier sur $R'$.
Démonstration de (2) omise.
\end{proof}
```

</details>

### 15 — lemma-integral-local

Anglais L7688–7708 ; français L7668–7688.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7688) · FR-ALGEBRA-B11-CHOICE-0015.

Les fi engendrent l'idéal unité ; cette condition n'est pas réduite à leur non-nullité. Les puissances f_i^{n_i} apparaissent après chasse aux dénominateurs. Le point d'exclamation anglais à idéal est maintenu. La convention sur zéro dans l'idéal des coefficients dominants est explicitée hors traduction.

Point particulier à relire : Même convention des coefficients dominants incluant zéro que dans le dossier B9 ; ce n'est pas une revendication de nouvel erratum.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-FINITE, FR-ALGEBRA-B11-RULE-POLYNOME, FR-ALGEBRA-B11-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-integral-local}
Let $R \to S$ be a ring map.
Let $f_1, \ldots, f_n \in R$ generate the unit ideal.
\begin{enumerate}
\item If each $R_{f_i} \to S_{f_i}$ is integral, so is $R \to S$.
\item If each $R_{f_i} \to S_{f_i}$ is finite, so is $R \to S$.
\end{enumerate}
\end{lemma}

\begin{proof}
Proof of (1).
Let $s \in S$. Consider the ideal $I \subset R[x]$ of
polynomials $P$ such that $P(s) = 0$. Let $J \subset R$
denote the ideal (!) of leading coefficients of elements of $I$.
By assumption and clearing denominators
we see that $f_i^{n_i} \in J$ for all $i$
and certain $n_i \geq 0$. Hence $J$ contains $1$ and we see
$s$ is integral over $R$. Proof of (2) omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-integral-local}
Soit $R \to S$ un morphisme d'anneaux.
Soient $f_1, \ldots, f_n \in R$ engendrant l'idéal unité.
\begin{enumerate}
\item Si chaque $R_{f_i} \to S_{f_i}$ est entier, alors $R \to S$ l'est aussi.
\item Si chaque $R_{f_i} \to S_{f_i}$ est fini, alors $R \to S$ l'est aussi.
\end{enumerate}
\end{lemma}

\begin{proof}
Démonstration de (1).
Soit $s \in S$. Considérons l'idéal $I \subset R[x]$ des
polynômes $P$ tels que $P(s) = 0$. Notons $J \subset R$
l'idéal (!) des coefficients dominants des éléments de $I$.
Par hypothèse et en chassant les dénominateurs,
nous voyons que $f_i^{n_i} \in J$ pour tout $i$
et certains $n_i \geq 0$. Ainsi, $J$ contient $1$, et nous voyons que
$s$ est entier sur $R$. Démonstration de (2) omise.
\end{proof}
```

</details>

### 16 — lemma-integral-permanence

Anglais L7709–7721 ; français L7689–7701.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7709) · FR-ALGEBRA-B11-CHOICE-0016.

À partir de A→B→C, les deux conclusions portent sur B→C, non sur A→B. L'extension du jeu de scalaires conserve intégralité ou génération finie. Les deux assertions et l'omission de preuve sont conservées.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-integral-permanence}
Let $A \to B \to C$ be ring maps.
\begin{enumerate}
\item If $A \to C$ is integral so is $B \to C$.
\item If $A \to C$ is finite so is $B \to C$.
\end{enumerate}
\end{lemma}

\begin{proof}
Omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-integral-permanence}
Soient $A \to B \to C$ des morphismes d'anneaux.
\begin{enumerate}
\item Si $A \to C$ est entier, alors $B \to C$ l'est aussi.
\item Si $A \to C$ est fini, alors $B \to C$ l'est aussi.
\end{enumerate}
\end{lemma}

\begin{proof}
Omis.
\end{proof}
```

</details>

### 17 — lemma-integral-closure-transitive

Anglais L7722–7733 ; français L7702–7713.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7722) · FR-ALGEBRA-B11-CHOICE-0017.

C′ est la clôture de B′ dans C, et non celle de B dans C. Les trois anneaux et les deux anneaux intermédiaires restent distincts. Le mot clôture suit Dat ; la transitivité mathématique est exactement celle de l'énoncé officiel.

Règles : FR-ALGEBRA-B11-RULE-CLOTURE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-integral-closure-transitive}
Let $A \to B \to C$ be ring maps.
Let $B'$ be the integral closure of $A$ in $B$,
let $C'$ be the integral closure of $B'$ in $C$. Then
$C'$ is the integral closure of $A$ in $C$.
\end{lemma}

\begin{proof}
Omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-integral-closure-transitive}
Soient $A \to B \to C$ des morphismes d'anneaux.
Soit $B'$ la clôture intégrale de $A$ dans $B$,
et soit $C'$ la clôture intégrale de $B'$ dans $C$. Alors
$C'$ est la clôture intégrale de $A$ dans $C$.
\end{lemma}

\begin{proof}
Omis.
\end{proof}
```

</details>

### 18 — lemma-integral-overring-surjective

Anglais L7734–7763 ; français L7714–7743.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7734) · FR-ALGEBRA-B11-CHOICE-0018.

L'inclusion R⊂S est une hypothèse expresse, nécessaire à la surjectivité spectrale. On localise en p, conserve l'injection puis applique Nakayama à la sous-algèbre S′ finie. La contradiction S′=0 utilise l'inclusion du local non nul, pas une hypothèse noethérienne absente.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-FINITE, FR-ALGEBRA-B11-RULE-LOCAL, FR-ALGEBRA-B11-RULE-PREMIERS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-integral-overring-surjective}
Suppose that $R \to S$ is an integral
ring extension with $R \subset S$.
Then $\varphi : \Spec(S) \to \Spec(R)$
is surjective.
\end{lemma}

\begin{proof}
Let $\mathfrak p \subset R$ be a prime ideal.
We have to show $\mathfrak pS_{\mathfrak p} \not = S_{\mathfrak p}$, see
Lemma \ref{lemma-in-image}.
The localization $R_{\mathfrak p} \to S_{\mathfrak p}$ is injective
(as localization is exact) and integral by
Lemma \ref{lemma-integral-closure-localize} or
\ref{lemma-base-change-integral}.
Hence we may replace $R$, $S$ by $R_{\mathfrak p}$, $S_{\mathfrak p}$ and
we may assume $R$ is local with maximal ideal $\mathfrak m$ and
it suffices to show that $\mathfrak mS \not = S$.
Suppose $1 = \sum f_i s_i$ with $f_i \in \mathfrak m$
and $s_i \in S$ in order to get a contradiction.
Let $R \subset S' \subset S$
be such that $R \to S'$ is finite and $s_i \in S'$, see
Lemma \ref{lemma-characterize-integral}.
The equation $1 = \sum f_i s_i$ implies that
the finite $R$-module $S'$ satisfies $S' = \mathfrak m S'$. Hence by
Nakayama's Lemma \ref{lemma-NAK}
we see $S' = 0$. Contradiction.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-integral-overring-surjective}
Supposons que $R \to S$ soit une extension
d'anneaux entière avec $R \subset S$.
Alors $\varphi : \Spec(S) \to \Spec(R)$
est surjective.
\end{lemma}

\begin{proof}
Soit $\mathfrak p \subset R$ un idéal premier.
Nous devons montrer que $\mathfrak pS_{\mathfrak p} \not = S_{\mathfrak p}$, voir le
lemme \ref{lemma-in-image}.
La localisation $R_{\mathfrak p} \to S_{\mathfrak p}$ est injective
(car la localisation est exacte) et entière d'après le
lemme \ref{lemma-integral-closure-localize} ou
\ref{lemma-base-change-integral}.
Nous pouvons donc remplacer $R$, $S$ par $R_{\mathfrak p}$, $S_{\mathfrak p}$ et
supposer que $R$ est local d'idéal maximal $\mathfrak m$ ; il
suffit alors de montrer que $\mathfrak mS \not = S$.
Supposons que $1 = \sum f_i s_i$, avec $f_i \in \mathfrak m$
et $s_i \in S$, afin d'obtenir une contradiction.
Soit $R \subset S' \subset S$
tel que $R \to S'$ soit fini et que $s_i \in S'$, voir le
lemme \ref{lemma-characterize-integral}.
L'équation $1 = \sum f_i s_i$ implique que
le $R$-module de type fini $S'$ satisfait $S' = \mathfrak m S'$. Le
lemme de Nakayama \ref{lemma-NAK} donne donc
$S' = 0$. Contradiction.
\end{proof}
```

</details>

### 19 — lemma-integral-under-field

Anglais L7764–7780 ; français L7744–7760.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7764) · FR-ALGEBRA-B11-CHOICE-0019.

Corps et extension algébrique rendent deux conclusions distinctes. L'intégralité n'impose pas un degré fini ; la seconde assertion ajoute précisément la finitude du module. L'argument par spectre à un point et anneau intègre est préservé.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-integral-under-field}
Let $R$ be a ring. Let $K$ be a field.
If $R \subset K$ and $K$ is integral over $R$,
then $R$ is a field and $K$ is an algebraic extension.
If $R \subset K$ and $K$ is finite over $R$,
then $R$ is a field and $K$ is a finite algebraic extension.
\end{lemma}

\begin{proof}
Assume that $R \subset K$ is integral.
By Lemma \ref{lemma-integral-overring-surjective} we see that
$\Spec(R)$ has $1$ point. Since clearly $R$ is a domain we see
that $R = R_{(0)}$ is a field (Lemma \ref{lemma-minimal-prime-reduced-ring}).
The other assertions are immediate from this.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-integral-under-field}
Soit $R$ un anneau. Soit $K$ un corps.
Si $R \subset K$ et si $K$ est entier sur $R$,
alors $R$ est un corps et $K$ est une extension algébrique.
Si $R \subset K$ et si $K$ est fini sur $R$,
alors $R$ est un corps et $K$ est une extension algébrique finie.
\end{lemma}

\begin{proof}
Supposons que $R \subset K$ soit entier.
D'après le lemme \ref{lemma-integral-overring-surjective}, nous voyons que
$\Spec(R)$ possède $1$ point. Comme $R$ est manifestement un anneau intègre, nous voyons
que $R = R_{(0)}$ est un corps (lemme \ref{lemma-minimal-prime-reduced-ring}).
Les autres assertions en résultent immédiatement.
\end{proof}
```

</details>

### 20 — lemma-integral-over-field

Anglais L7781–7811 ; français L7761–7791.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7781) · FR-ALGEBRA-B11-CHOICE-0020.

Les trois assertions distinguent domaine de dimension finie, domaine entier sur un corps, et algèbre entière quelconque dont les premiers sont maximaux. La réduction par S′ est conservée. Le français avait ajouté non nul au second choix de s, absent de l'anglais : retrait diplomatique, avec démonstration séparée de la lacune de la preuve.

Point particulier à relire : L'anglais choisit s sans préciser s≠0 à cet endroit. Le français retirera son ajout non nul, mais la note séparée montre que multiplication par zéro n'est pas surjective dans un corps non nul. La traduction n'est pas une édition mathématique corrigée.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-FINITE, FR-ALGEBRA-B11-RULE-LOGIQUE, FR-ALGEBRA-B11-RULE-PREMIERS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-integral-over-field}
Let $k$ be a field. Let $S$ be a $k$-algebra over $k$.
\begin{enumerate}
\item If $S$ is a domain and finite dimensional over $k$,
then $S$ is a field.
\item If $S$ is integral over $k$ and a domain,
then $S$ is a field.
\item If $S$ is integral over $k$ then every prime of
$S$ is a maximal ideal (see
Lemma \ref{lemma-ring-with-only-minimal-primes}
for more consequences).
\end{enumerate}
\end{lemma}

\begin{proof}
The statement on primes follows from the statement
``integral $+$ domain $\Rightarrow$ field''.
Let $S$ integral over $k$ and assume $S$ is a domain,
Take $s \in S$. By Lemma
\ref{lemma-characterize-integral} we may find a
finite dimensional $k$-subalgebra $k \subset S' \subset S$
containing $s$. Hence $S$ is a field if we can prove the
first statement. Assume $S$ finite dimensional
over $k$ and a domain. Pick $s\in S$.
Since $S$ is a domain the multiplication
map $s : S \to S$ is surjective by dimension
reasons. Hence there exists an element $s_1 \in S$
such that $ss_1 = 1$. So $S$ is a field.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-integral-over-field}
Soit $k$ un corps. Soit $S$ une $k$-algèbre sur $k$.
\begin{enumerate}
\item Si $S$ est un anneau intègre de dimension finie sur $k$,
alors $S$ est un corps.
\item Si $S$ est entier sur $k$ et est un anneau intègre,
alors $S$ est un corps.
\item Si $S$ est entier sur $k$, alors tout idéal premier de
$S$ est un idéal maximal (voir le
lemme \ref{lemma-ring-with-only-minimal-primes}
pour d'autres conséquences).
\end{enumerate}
\end{lemma}

\begin{proof}
L'assertion sur les idéaux premiers résulte de l'assertion
« entier $+$ intègre $\Rightarrow$ corps ».
Soit $S$ entier sur $k$ et supposons que $S$ soit un anneau intègre.
Prenons $s \in S$. D'après le lemme
\ref{lemma-characterize-integral}, nous pouvons trouver une
$k$-sous-algèbre de dimension finie $k \subset S' \subset S$
qui contient $s$. Ainsi, $S$ est un corps si nous pouvons démontrer la
première assertion. Supposons $S$ de dimension finie
sur $k$ et intègre. Choisissons $s\in S$.
Puisque $S$ est un anneau intègre, l'application de multiplication
$s : S \to S$ est surjective pour des raisons de
dimension. Il existe donc un élément $s_1 \in S$
tel que $ss_1 = 1$. Ainsi, $S$ est un corps.
\end{proof}
```

</details>

### 21 — lemma-integral-no-inclusion

Anglais L7812–7830 ; français L7792–7810.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7812) · FR-ALGEBRA-B11-CHOICE-0021.

Distincts, même image et ni…ni expriment l'incomparabilité de deux premiers au-dessus du même p. On conserve le passage à l'algèbre fibre sur κ(p) et le renvoi au résultat sur les corps ; il ne s'agit pas d'affirmer que tous les premiers de S sont maximaux.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-PREMIERS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-integral-no-inclusion}
Suppose $R \to S$ is integral.
Let $\mathfrak q, \mathfrak q' \in \Spec(S)$
be distinct primes
having the same image in $\Spec(R)$.
Then neither $\mathfrak q \subset \mathfrak q'$
nor $\mathfrak q' \subset \mathfrak q$.
\end{lemma}

\begin{proof}
Let $\mathfrak p \subset R$ be the image.
By Remark \ref{remark-fundamental-diagram}
the primes $\mathfrak q, \mathfrak q'$
correspond to ideals in
$S \otimes_R \kappa(\mathfrak p)$.
Thus the lemma follows from Lemma \ref{lemma-integral-over-field}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-integral-no-inclusion}
Supposons que $R \to S$ soit entier.
Soient $\mathfrak q, \mathfrak q' \in \Spec(S)$
deux idéaux premiers distincts
ayant la même image dans $\Spec(R)$.
Alors ni $\mathfrak q \subset \mathfrak q'$
ni $\mathfrak q' \subset \mathfrak q$.
\end{lemma}

\begin{proof}
Soit $\mathfrak p \subset R$ l'image.
D'après la remarque \ref{remark-fundamental-diagram},
les idéaux premiers $\mathfrak q, \mathfrak q'$
correspondent à des idéaux de
$S \otimes_R \kappa(\mathfrak p)$.
Le lemme résulte donc du lemme \ref{lemma-integral-over-field}.
\end{proof}
```

</details>

### 22 — lemma-finite-finite-fibres

Anglais L7831–7851 ; français L7811–7831.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7831) · FR-ALGEBRA-B11-CHOICE-0022.

Fibres finies signifie ici un nombre fini de points du spectre, non que le morphisme de corps soit injectif ou que R soit noethérien. Le module fini sur κ(p) rend chaque anneau fibre noethérien, puis ses premiers minimaux sont en nombre fini. Toutes ces étapes restent dans le français.

Règles : FR-ALGEBRA-B11-RULE-FINITE, FR-ALGEBRA-B11-RULE-PREMIERS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-finite-finite-fibres}
Suppose $R \to S$ is finite.
Then the fibres of $\Spec(S) \to \Spec(R)$ are finite.
\end{lemma}

\begin{proof}
By the discussion in
Remark \ref{remark-fundamental-diagram}
the fibres are the spectra of the rings $S \otimes_R \kappa(\mathfrak p)$.
As $R \to S$ is finite, these fibre rings are finite over
$\kappa(\mathfrak p)$ hence Noetherian by
Lemma \ref{lemma-Noetherian-permanence}.
By
Lemma \ref{lemma-integral-no-inclusion}
every prime of $S \otimes_R \kappa(\mathfrak p)$ is a minimal
prime. Hence by
Lemma \ref{lemma-Noetherian-irreducible-components}
there are at most finitely many.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-finite-finite-fibres}
Supposons que $R \to S$ soit fini.
Alors les fibres de $\Spec(S) \to \Spec(R)$ sont finies.
\end{lemma}

\begin{proof}
D'après la discussion de la
remarque \ref{remark-fundamental-diagram},
les fibres sont les spectres des anneaux $S \otimes_R \kappa(\mathfrak p)$.
Comme $R \to S$ est fini, ces anneaux fibres sont finis sur
$\kappa(\mathfrak p)$, donc noethériens d'après le
lemme \ref{lemma-Noetherian-permanence}.
D'après le
lemme \ref{lemma-integral-no-inclusion},
tout idéal premier de $S \otimes_R \kappa(\mathfrak p)$ est
minimal. Ainsi, d'après le
lemme \ref{lemma-Noetherian-irreducible-components},
il n'y en a qu'un nombre fini.
\end{proof}
```

</details>

### 23 — lemma-integral-going-up

Anglais L7852–7874 ; français L7832–7854.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7852) · FR-ALGEBRA-B11-CHOICE-0023.

Propriété de montée désigne la possibilité de relever p⊂p′ à partir du premier q fixé. La preuve passe aux quotients puis à la surjectivité spectrale ; elle ne postule pas une inclusion initiale R⊂S. Ducros p.119 atteste le nom going-up, mais pas le syntagme français montée sur cette page : ce dernier reste un choix compositionnel motivé par les inclusions et la définition interne.

Point particulier à relire : Montée est justifié compositionnellement, non faussement attribué à la page de Ducros qui utilise going-up.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-LOGIQUE, FR-ALGEBRA-B11-RULE-PREMIERS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-integral-going-up}
Let $R \to S$ be a ring map such that
$S$ is integral over $R$.
Let $\mathfrak p \subset \mathfrak p' \subset R$
be primes. Let $\mathfrak q$ be a prime of $S$ mapping
to $\mathfrak p$. Then there exists a prime $\mathfrak q'$
with $\mathfrak q \subset \mathfrak q'$
mapping to $\mathfrak p'$.
\end{lemma}

\begin{proof}
We may replace $R$ by $R/\mathfrak p$ and $S$ by $S/\mathfrak q$.
This reduces us to the situation of having an integral
extension of domains $R \subset S$ and a prime $\mathfrak p' \subset R$.
By Lemma \ref{lemma-integral-overring-surjective} we win.
\end{proof}

\noindent
The property expressed in the lemma above is called
the ``going up property'' for the ring map $R \to S$,
see Definition \ref{definition-going-up-down}.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-integral-going-up}
Soit $R \to S$ un morphisme d'anneaux tel que
$S$ soit entier sur $R$.
Soient $\mathfrak p \subset \mathfrak p' \subset R$
des idéaux premiers. Soit $\mathfrak q$ un idéal premier de $S$ qui s'envoie
sur $\mathfrak p$. Alors il existe un idéal premier $\mathfrak q'$
tel que $\mathfrak q \subset \mathfrak q'$
et qui s'envoie sur $\mathfrak p'$.
\end{lemma}

\begin{proof}
Nous pouvons remplacer $R$ par $R/\mathfrak p$ et $S$ par $S/\mathfrak q$.
Cela nous ramène à une extension entière d'anneaux
intègres $R \subset S$ et à un idéal premier $\mathfrak p' \subset R$.
Le lemme \ref{lemma-integral-overring-surjective} permet de conclure.
\end{proof}

\noindent
La propriété exprimée dans le lemme ci-dessus est appelée
la « propriété de montée » pour le morphisme d'anneaux $R \to S$,
voir la définition \ref{definition-going-up-down}.
```

</details>

### 24 — lemma-finite-finitely-presented-extension

Anglais L7875–7926 ; français L7855–7906.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7875) · FR-ALGEBRA-B11-CHOICE-0024.

Présentation finie de morphisme d'anneaux et présentation finie de module ne sont pas confondues. Le noyau de S^n→M est fini sur R parce qu'il est image de S^m, non parce que tout sous-module d'un module fini serait fini. La preuve intermédiaire rend S′ libre sur R par des équations unitaires en variables séparées. Les détails que la source omet restent omis.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-FINITE, FR-ALGEBRA-B11-RULE-POLYNOME, FR-ALGEBRA-B11-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-finite-finitely-presented-extension}
Let $R \to S$ be a finite and finitely presented ring map.
Let $M$ be an $S$-module.
Then $M$ is finitely presented as an $R$-module if and only if
$M$ is finitely presented as an $S$-module.
\end{lemma}

\begin{proof}
One of the implications follows from
Lemma \ref{lemma-finitely-presented-over-subring}.
To see the other assume that $M$ is finitely presented as an $S$-module.
Pick a presentation
$$
S^{\oplus m} \longrightarrow
S^{\oplus n} \longrightarrow
M \longrightarrow 0
$$
As $S$ is finite as an $R$-module, the kernel of
$S^{\oplus n} \to M$ is a finite $R$-module. Thus from
Lemma \ref{lemma-extension}
we see that it suffices to prove that $S$ is finitely presented as an
$R$-module.

\medskip\noindent
Pick $y_1, \ldots, y_n \in S$ such that $y_1, \ldots, y_n$ generate $S$
as an $R$-module. By Lemma \ref{lemma-characterize-integral-element}
each $y_i$ is integral over $R$. Choose monic polynomials
$P_i(x) \in R[x]$ with $P_i(y_i) = 0$. Consider the ring
$$
S' = R[x_1, \ldots, x_n]/(P_1(x_1), \ldots, P_n(x_n))
$$
Then we see that $S$ is of finite presentation as an $S'$-algebra
by Lemma \ref{lemma-compose-finite-type}. Since $S' \to S$ is surjective,
the kernel $J = \Ker(S' \to S)$ is finitely generated as an ideal by
Lemma \ref{lemma-finite-presentation-independent}. Hence $J$ is a finite
$S'$-module (immediate from the definitions).
Thus $S = \Coker(J \to S')$ is  of finite presentation as an $S'$-module
by Lemma \ref{lemma-extension}.
Hence, arguing as in the first paragraph, it suffices to show that $S'$ is
of finite presentation as an $R$-module. Actually, $S'$ is free as an
$R$-module with basis the monomials $x_1^{e_1} \ldots x_n^{e_n}$
for $0 \leq e_i < \deg(P_i)$. Namely, write $R \to S'$ as the composition
$$
R \to R[x_1]/(P_1(x_1)) \to R[x_1, x_2]/(P_1(x_1), P_2(x_2)) \to
\ldots \to S'
$$
This shows that the $i$th ring in this sequence is free as a module over the
$(i - 1)$st one with basis $1, x_i, \ldots, x_i^{\deg(P_i) - 1}$. The result
follows easily from this by induction. Some details omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-finite-finitely-presented-extension}
Soit $R \to S$ un morphisme d'anneaux fini et de présentation finie.
Soit $M$ un $S$-module.
Alors $M$ est de présentation finie comme $R$-module si et seulement si
$M$ est de présentation finie comme $S$-module.
\end{lemma}

\begin{proof}
L'une des implications résulte du
lemme \ref{lemma-finitely-presented-over-subring}.
Pour voir l'autre, supposons que $M$ soit de présentation finie comme $S$-module.
Choisissons une présentation
$$
S^{\oplus m} \longrightarrow
S^{\oplus n} \longrightarrow
M \longrightarrow 0
$$
Comme $S$ est fini comme $R$-module, le noyau de
$S^{\oplus n} \to M$ est un $R$-module de type fini. Ainsi, le
lemme \ref{lemma-extension}
montre qu'il suffit de démontrer que $S$ est de présentation finie comme
$R$-module.

\medskip\noindent
Choisissons $y_1, \ldots, y_n \in S$ tels que $y_1, \ldots, y_n$ engendrent $S$
comme $R$-module. D'après le lemme \ref{lemma-characterize-integral-element},
chaque $y_i$ est entier sur $R$. Choisissons des polynômes unitaires
$P_i(x) \in R[x]$ tels que $P_i(y_i) = 0$. Considérons l'anneau
$$
S' = R[x_1, \ldots, x_n]/(P_1(x_1), \ldots, P_n(x_n))
$$
Nous voyons alors que $S$ est de présentation finie comme $S'$-algèbre
d'après le lemme \ref{lemma-compose-finite-type}. Puisque $S' \to S$ est surjectif,
le noyau $J = \Ker(S' \to S)$ est engendré par un nombre fini d'éléments comme idéal d'après le
lemme \ref{lemma-finite-presentation-independent}. Ainsi, $J$ est un
$S'$-module de type fini (cela découle immédiatement des définitions).
Par conséquent, $S = \Coker(J \to S')$ est de présentation finie comme $S'$-module
d'après le lemme \ref{lemma-extension}.
Ainsi, en raisonnant comme dans le premier paragraphe, il suffit de montrer que $S'$ est
de présentation finie comme $R$-module. En fait, $S'$ est libre comme
$R$-module, de base les monômes $x_1^{e_1} \ldots x_n^{e_n}$
pour $0 \leq e_i < \deg(P_i)$. En effet, écrivons $R \to S'$ comme la composée
$$
R \to R[x_1]/(P_1(x_1)) \to R[x_1, x_2]/(P_1(x_1), P_2(x_2)) \to
\ldots \to S'
$$
Cela montre que le $i$-ème anneau de cette suite est libre comme module sur le
$(i - 1)$-ième, de base $1, x_i, \ldots, x_i^{\deg(P_i) - 1}$. Le résultat
s'en déduit aisément par récurrence. Certains détails sont omis.
\end{proof}
```

</details>

### 25 — lemma-silly-normal

Anglais L7927–7970 ; français L7907–7950.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7927) · FR-ALGEBRA-B11-CHOICE-0025.

Non-diviseurs de zéro ne devient pas anneau intègre. On garde la clôture relative dans Rx ou Ry, les signes (−1,1) et (1,1), puis les deux écritures de α dans l'intersection. Les puissances de part et d'autre donnent un module stable contenant 1. La dernière phrase traite Rx ; le cas Ry se lit par symétrie, sans ajout à la preuve.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-CLOTURE, FR-ALGEBRA-B11-RULE-FINITE, FR-ALGEBRA-B11-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-silly-normal}
Let $R$ be a ring. Let $x, y \in R$ be nonzerodivisors.
Let $R[x/y] \subset R_{xy}$ be the $R$-subalgebra generated
by $x/y$, and similarly for the subalgebras $R[y/x]$ and $R[x/y, y/x]$.
If $R$ is integrally closed in $R_x$ or $R_y$, then the sequence
$$
0 \to R \xrightarrow{(-1, 1)} R[x/y] \oplus R[y/x] \xrightarrow{(1, 1)}
R[x/y, y/x] \to 0
$$
is a short exact sequence of $R$-modules.
\end{lemma}

\begin{proof}
Since $x/y \cdot y/x = 1$ it is clear that the map
$R[x/y] \oplus R[y/x] \to R[x/y, y/x]$ is surjective.
Let $\alpha \in R[x/y] \cap R[y/x]$. To show exactness in the middle
we have to prove that $\alpha \in R$. By assumption we may write
$$
\alpha = a_0 + a_1 x/y + \ldots + a_n (x/y)^n =
b_0 + b_1 y/x + \ldots + b_m(y/x)^m
$$
for some $n, m \geq 0$ and $a_i, b_j \in R$.
Pick some $N > \max(n, m)$.
Consider the finite $R$-submodule $M$ of $R_{xy}$ generated by the elements
$$
(x/y)^N, (x/y)^{N - 1}, \ldots, x/y, 1, y/x, \ldots, (y/x)^{N - 1}, (y/x)^N
$$
We claim that $\alpha M \subset M$. Namely, it is clear that
$(x/y)^i (b_0 + b_1 y/x + \ldots + b_m(y/x)^m) \in M$ for
$0 \leq i \leq N$ and that
$(y/x)^i (a_0 + a_1 x/y + \ldots + a_n(x/y)^n) \in M$ for
$0 \leq i \leq N$. Hence $\alpha$ is integral over $R$ by
Lemma \ref{lemma-characterize-integral-element}. Note that
$\alpha \in R_x$, so if $R$ is integrally closed in $R_x$
then $\alpha \in R$ as desired.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-silly-normal}
Soit $R$ un anneau. Soient $x, y \in R$ des non-diviseurs de zéro.
Soit $R[x/y] \subset R_{xy}$ la $R$-sous-algèbre engendrée
par $x/y$, et de même pour les sous-algèbres $R[y/x]$ et $R[x/y, y/x]$.
Si $R$ est intégralement clos dans $R_x$ ou $R_y$, alors la suite
$$
0 \to R \xrightarrow{(-1, 1)} R[x/y] \oplus R[y/x] \xrightarrow{(1, 1)}
R[x/y, y/x] \to 0
$$
est une suite exacte courte de $R$-modules.
\end{lemma}

\begin{proof}
Puisque $x/y \cdot y/x = 1$, il est clair que l'application
$R[x/y] \oplus R[y/x] \to R[x/y, y/x]$ est surjective.
Soit $\alpha \in R[x/y] \cap R[y/x]$. Pour montrer l'exactitude au milieu,
nous devons prouver que $\alpha \in R$. Par hypothèse, nous pouvons écrire
$$
\alpha = a_0 + a_1 x/y + \ldots + a_n (x/y)^n =
b_0 + b_1 y/x + \ldots + b_m(y/x)^m
$$
pour certains $n, m \geq 0$ et $a_i, b_j \in R$.
Choisissons un $N > \max(n, m)$.
Considérons le $R$-sous-module de type fini $M$ de $R_{xy}$ engendré par les éléments
$$
(x/y)^N, (x/y)^{N - 1}, \ldots, x/y, 1, y/x, \ldots, (y/x)^{N - 1}, (y/x)^N
$$
Nous affirmons que $\alpha M \subset M$. En effet, il est clair que
$(x/y)^i (b_0 + b_1 y/x + \ldots + b_m(y/x)^m) \in M$ pour
$0 \leq i \leq N$ et que
$(y/x)^i (a_0 + a_1 x/y + \ldots + a_n(x/y)^n) \in M$ pour
$0 \leq i \leq N$. Ainsi, $\alpha$ est entier sur $R$ d'après le
lemme \ref{lemma-characterize-integral-element}. Remarquons que
$\alpha \in R_x$ ; si $R$ est intégralement clos dans $R_x$,
alors $\alpha \in R$, comme voulu.
\end{proof}
```

</details>

### 26 — section-normal-rings

Anglais L7971–7977 ; français L7951–7957.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7971) · FR-ALGEBRA-B11-CHOICE-0026.

L'introduction distingue volontairement anneau intègre normal et anneau normal au sens local général. La seconde notion ne doit pas être réduite à la première : les produits finis qui suivent en dépendent.

Règles : FR-ALGEBRA-B11-RULE-NORMAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Normal rings}
\label{section-normal-rings}

\noindent
We first introduce the notion of a normal domain, and then we
introduce the (very general) notion of a normal ring.
```

Français restauré :
```tex
\section{Anneaux normaux}
\label{section-normal-rings}

\noindent
Introduisons d'abord la notion d'anneau intègre normal, puis
la notion (très générale) d'anneau normal.
```

</details>

### 27 — definition-domain-normal

Anglais L7978–7983 ; français L7958–7963.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7978) · FR-ALGEBRA-B11-CHOICE-0027.

Anneau intègre normal signifie intégralement clos dans son propre corps des fractions. Ducros 2.8.10 et Dat p.145 attestent directement cette définition. On ne remplace pas corps des fractions par clôture algébrique.

Règles : FR-ALGEBRA-B11-RULE-CLOTURE, FR-ALGEBRA-B11-RULE-LOCAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-domain-normal}
A domain $R$ is called {\it normal} if it is integrally
closed in its field of fractions.
\end{definition}
```

Français restauré :
```tex
\begin{definition}
\label{definition-domain-normal}
Un anneau intègre $R$ est dit {\it normal} s'il est intégralement
clos dans son corps des fractions.
\end{definition}
```

</details>

### 28 — lemma-integral-closure-in-normal

Anglais L7984–7998 ; français L7964–7978.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7984) · FR-ALGEBRA-B11-CHOICE-0028.

L'anneau S est intègre normal ; sa sous-algèbre d'éléments entiers sur R l'est aussi. R→S n'est pas rendu injectif. La preuve omise et la transition vers la notion suivante restent deux éléments du passage complet.

Règles : FR-ALGEBRA-B11-RULE-CLOTURE, FR-ALGEBRA-B11-RULE-NORMAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-integral-closure-in-normal}
Let $R \to S$ be a ring map.
If $S$ is a normal domain, then the integral closure of $R$
in $S$ is a normal domain.
\end{lemma}

\begin{proof}
Omitted.
\end{proof}

\noindent
The following notion is occasionally useful when
studying normality.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-integral-closure-in-normal}
Soit $R \to S$ un morphisme d'anneaux.
Si $S$ est un anneau intègre normal, alors la clôture intégrale de $R$
dans $S$ est un anneau intègre normal.
\end{lemma}

\begin{proof}
Omis.
\end{proof}

\noindent
La notion suivante est parfois utile dans l'étude
de la normalité.
```

</details>

### 29 — definition-almost-integral

Anglais L7999–8016 ; français L7979–7996.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7999) · FR-ALGEBRA-B11-CHOICE-0029.

Presque entier exige un r non nul unique pour toutes les puissances, non un r variable avec n. André 2.3.1 p.15 le définit par inclusion des puissances dans un module de type fini. Dans Frac(R), les définitions coïncident : un dénominateur commun des générateurs donne r, et réciproquement (1/r)R contient toutes les puissances. Complètement normal est remplacé, dans ses deux occurrences, par complètement intégralement clos, directement attesté p.57 d'André ; la propriété et ses quantificateurs sont inchangés.

Point particulier à relire : Deux occurrences seulement de complètement normal figurent dans le témoin du chapitre ; toutes deux appartiennent à ce passage. Choix de complètement intégralement clos plutôt que complètement intégralement fermé pour cohérence avec intégralement clos ; les deux variantes sont attestées chez André. Ce choix lexical ne remplace ni la définition ni l'hypothèse noethérienne.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-CLOTURE, FR-ALGEBRA-B11-RULE-PRESQUE, FR-ALGEBRA-B11-RULE-LOCAL, FR-ALGEBRA-B11-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-almost-integral}
Let $R$ be a domain.
\begin{enumerate}
\item An element $g$ of the fraction
field of $R$ is called {\it almost integral over $R$}
if there exists an element $r \in R$, $r\not = 0$
such that $rg^n \in R$ for all $n \geq 0$.
\item The domain $R$ is called {\it completely normal} if every
almost integral element of the fraction field of $R$ is
contained in $R$.
\end{enumerate}
\end{definition}

\noindent
The following lemma shows that a Noetherian domain is normal
if and only if it is completely normal.
```

Français restauré :
```tex
\begin{definition}
\label{definition-almost-integral}
Soit $R$ un anneau intègre.
\begin{enumerate}
\item Un élément $g$ du corps des
fractions de $R$ est dit {\it presque entier sur $R$}
s'il existe un élément $r \in R$, $r\not = 0$,
tel que $rg^n \in R$ pour tout $n \geq 0$.
\item L'anneau intègre $R$ est dit {\it complètement intégralement clos} si tout
élément presque entier du corps des fractions de $R$
appartient à $R$.
\end{enumerate}
\end{definition}

\noindent
Le lemme suivant montre qu'un anneau intègre noethérien est normal
si et seulement s'il est complètement intégralement clos.
```

</details>

### 30 — lemma-almost-integral

Anglais L8017–8046 ; français L7997–8026.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8017) · FR-ALGEBRA-B11-CHOICE-0030.

La clôture sous addition et multiplication utilise le produit non nul rr′. Un dénominateur commun de la famille génératrice rend un élément entier presque entier. La réciproque exige R noethérien pour rendre R[g] fini dans (1/r)R. Le français conserve cette restriction, également visible dans la distinction d'André.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-PRESQUE, FR-ALGEBRA-B11-RULE-FINITE, FR-ALGEBRA-B11-RULE-LOCAL, FR-ALGEBRA-B11-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-almost-integral}
Let $R$ be a domain with fraction field $K$.
If $u, v \in K$ are almost integral over $R$, then so are
$u + v$ and $uv$. Any element $g \in K$ which is integral over $R$
is almost integral over $R$. If $R$ is Noetherian
then the converse holds as well.
\end{lemma}

\begin{proof}
If $ru^n \in R$ for all $n \geq 0$ and
$v^nr' \in R$ for all $n \geq 0$, then
$(uv)^nrr'$ and $(u + v)^nrr'$ are in $R$ for
all $n \geq 0$. Hence the first assertion.
Suppose $g \in K$ is integral over $R$.
In this case there exists an $d > 0$ such that
the ring $R[g]$ is generated by $1, g, \ldots, g^d$ as an $R$-module.
Let $r \in R$ be a common denominator of the elements
$1, g, \ldots, g^d \in K$. It follows that $rR[g] \subset R$,
and hence $g$ is almost integral over $R$.

\medskip\noindent
Suppose $R$ is Noetherian and $g \in K$ is almost integral over $R$.
Let $r \in R$, $r\not = 0$ be as in the definition.
Then $R[g] \subset \frac{1}{r}R$ as an $R$-module.
Since $R$ is Noetherian this implies that $R[g]$ is
finite over $R$. Hence $g$ is integral over $R$, see
Lemma \ref{lemma-finite-is-integral}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-almost-integral}
Soit $R$ un anneau intègre de corps des fractions $K$.
Si $u, v \in K$ sont presque entiers sur $R$, alors
$u + v$ et $uv$ le sont aussi. Tout élément $g \in K$ qui est entier sur $R$
est presque entier sur $R$. Si $R$ est noethérien,
alors la réciproque est également vraie.
\end{lemma}

\begin{proof}
Si $ru^n \in R$ pour tout $n \geq 0$ et
$v^nr' \in R$ pour tout $n \geq 0$, alors
$(uv)^nrr'$ et $(u + v)^nrr'$ appartiennent à $R$ pour
tout $n \geq 0$. D'où la première assertion.
Supposons que $g \in K$ soit entier sur $R$.
Dans ce cas, il existe un $d > 0$ tel que
l'anneau $R[g]$ soit engendré par $1, g, \ldots, g^d$ comme $R$-module.
Soit $r \in R$ un dénominateur commun des éléments
$1, g, \ldots, g^d \in K$. Il s'ensuit que $rR[g] \subset R$,
et donc que $g$ est presque entier sur $R$.

\medskip\noindent
Supposons que $R$ soit noethérien et que $g \in K$ soit presque entier sur $R$.
Soit $r \in R$, $r\not = 0$, comme dans la définition.
Alors $R[g] \subset \frac{1}{r}R$ comme $R$-module.
Puisque $R$ est noethérien, cela implique que $R[g]$ est
fini sur $R$. Ainsi, $g$ est entier sur $R$, voir le
lemme \ref{lemma-finite-is-integral}.
\end{proof}
```

</details>

### 31 — lemma-localize-normal-domain

Anglais L8047–8064 ; français L8027–8044.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8047) · FR-ALGEBRA-B11-CHOICE-0031.

Toute localisation garde la normalité. Le polynôme de sg est unitaire et ses coefficients s^{d−j}aj sont dans R. Le corps des fractions sert à ce raisonnement lorsque la localisation n'est pas nulle ; le cas où S contient zéro est trivial pour la définition générale ultérieure. Aucune exclusion nouvelle n'est ajoutée.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-NORMAL, FR-ALGEBRA-B11-RULE-LOCAL, FR-ALGEBRA-B11-RULE-POLYNOME, FR-ALGEBRA-B11-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-localize-normal-domain}
Any localization of a normal domain is normal.
\end{lemma}

\begin{proof}
Let $R$ be a normal domain, and let $S \subset R$ be
a multiplicative subset. Suppose $g$ is an element
of the fraction field of $R$ which is integral over $S^{-1}R$.
Let $P = x^d + \sum_{j < d} a_j x^j$ be a polynomial
with $a_i \in S^{-1}R$ such that $P(g) = 0$.
Choose $s \in S$ such that $sa_i \in R$ for all $i$.
Then $sg$ satisfies the monic polynomial
$x^d + \sum_{j < d} s^{d-j}a_j x^j$ which has coefficients
$s^{d-j}a_j$ in $R$. Hence $sg \in R$ because $R$ is normal.
Hence $g \in S^{-1}R$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-localize-normal-domain}
Toute localisation d'un anneau intègre normal est normale.
\end{lemma}

\begin{proof}
Soit $R$ un anneau intègre normal, et soit $S \subset R$ une
partie multiplicative. Supposons que $g$ soit un élément
du corps des fractions de $R$ qui soit entier sur $S^{-1}R$.
Soit $P = x^d + \sum_{j < d} a_j x^j$ un polynôme
avec $a_i \in S^{-1}R$ tel que $P(g) = 0$.
Choisissons $s \in S$ tel que $sa_i \in R$ pour tout $i$.
Alors $sg$ satisfait le polynôme unitaire
$x^d + \sum_{j < d} s^{d-j}a_j x^j$, dont les coefficients
$s^{d-j}a_j$ appartiennent à $R$. Ainsi, $sg \in R$ puisque $R$ est normal.
Donc $g \in S^{-1}R$.
\end{proof}
```

</details>

### 32 — lemma-PID-normal

Anglais L8065–8080 ; français L8045–8060.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8065) · FR-ALGEBRA-B11-CHOICE-0032.

Anneau principal traduit principal ideal domain selon la convention française intégrale, déjà fixée dans le chapitre ; il ne vise pas tout anneau à idéaux principaux avec diviseurs de zéro. L'argument annule le facteur commun de a,b, puis force b inversible. Dat p.145 atteste le raisonnement voisin pour les anneaux factoriels, pas une nouvelle preuve source.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-LOCAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-PID-normal}
A principal ideal domain is normal.
\end{lemma}

\begin{proof}
Let $R$ be a principal ideal domain.
Let $g = a/b$ be an element of the fraction field
of $R$ integral over $R$. Because $R$ is a principal ideal domain
we may divide out a common factor of $a$ and $b$
and assume $(a, b) = R$. In this case, any equation
$(a/b)^n + r_{n-1} (a/b)^{n-1} + \ldots + r_0 = 0$
with $r_i \in R$ would imply $a^n \in (b)$. This
contradicts $(a, b) = R$ unless $b$ is a unit in $R$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-PID-normal}
Un anneau principal est normal.
\end{lemma}

\begin{proof}
Soit $R$ un anneau principal.
Soit $g = a/b$ un élément du corps des fractions
de $R$ qui soit entier sur $R$. Puisque $R$ est un anneau principal,
nous pouvons diviser $a$ et $b$ par un facteur commun
et supposer que $(a, b) = R$. Dans ce cas, toute équation
$(a/b)^n + r_{n-1} (a/b)^{n-1} + \ldots + r_0 = 0$
avec $r_i \in R$ impliquerait que $a^n \in (b)$. Cela
contredit $(a, b) = R$, sauf si $b$ est une unité de $R$.
\end{proof}
```

</details>

### 33 — lemma-prepare-polynomial-ring-normal

Anglais L8081–8128 ; français L8061–8108.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8081) · FR-ALGEBRA-B11-CHOICE-0033.

L'assertion presque entière est prouvée d'abord par le coefficient dominant et récurrence ; le cas f=0 est immédiat, non une hypothèse retranchée. Pour l'intégralité, la réduction noethérienne absolue choisit une sous-Z-algèbre de type fini contenant tous les coefficients et dénominateurs utilisés. Ce nom spécialisé n'est pas attesté dans les nouvelles pages françaises consultées ; la construction source justifie le choix provisoire.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-PRESQUE, FR-ALGEBRA-B11-RULE-FINITE, FR-ALGEBRA-B11-RULE-LOCAL, FR-ALGEBRA-B11-RULE-POLYNOME, FR-ALGEBRA-B11-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-prepare-polynomial-ring-normal}
Let $R$ be a domain with fraction field $K$.
Suppose $f = \sum \alpha_i x^i$ is an
element of $K[x]$.
\begin{enumerate}
\item If $f$ is integral over $R[x]$
then all $\alpha_i$ are integral over $R$, and
\item If $f$ is almost integral over $R[x]$
then all $\alpha_i$ are almost integral over $R$.
\end{enumerate}
\end{lemma}

\begin{proof}
We first prove the second statement.
Write $f = \alpha_0 + \alpha_1 x + \ldots + \alpha_r x^r$
with $\alpha_r \not = 0$.
By assumption there exists $h = b_0 + b_1 x + \ldots + b_s x^s \in R[x]$,
$b_s \not = 0$ such that $f^n h \in R[x]$ for all
$n \geq 0$. This implies that $b_s \alpha_r^n \in R$
for all $n \geq 0$. Hence $\alpha_r$ is almost
integral over $R$. Since the set of almost integral
elements form a subring (Lemma \ref{lemma-almost-integral}) we deduce that
$f - \alpha_r x^r = \alpha_0 + \alpha_1 x + \ldots + \alpha_{r - 1} x^{r - 1}$
is almost integral over $R[x]$. By induction on $r$ we win.

\medskip\noindent
In order to prove the first statement we will use absolute Noetherian
reduction. Namely, write $\alpha_i = a_i / b_i$ and
let $P(t) = t^d + \sum_{j < d} f_j t^j$ be a polynomial
with coefficients $f_j \in R[x]$ such that $P(f) = 0$.
Let $f_j = \sum f_{ji}x^i$. Consider the subring
$R_0 \subset R$ generated by the finite list of elements
$a_i, b_i, f_{ji}$ of $R$. It is a domain; let
$K_0$ be its field of fractions. Since $R_0$ is a finite type
$\mathbf{Z}$-algebra it is Noetherian, see
Lemma \ref{lemma-obvious-Noetherian}. It is still
the case that $f \in K_0[x]$ is integral over $R_0[x]$,
because all the identities in $R$
among the elements $a_i, b_i, f_{ji}$ also hold in $R_0$.
By Lemma \ref{lemma-almost-integral} the element
$f$ is almost integral over $R_0[x]$. By the second statement of
the lemma, the elements $\alpha_i$ are almost integral
over $R_0$. And since $R_0$ is Noetherian, they are
integral over $R_0$, see Lemma \ref{lemma-almost-integral}.
Of course, then they are integral over $R$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-prepare-polynomial-ring-normal}
Soit $R$ un anneau intègre de corps des fractions $K$.
Supposons que $f = \sum \alpha_i x^i$ soit un
élément de $K[x]$.
\begin{enumerate}
\item Si $f$ est entier sur $R[x]$,
alors tous les $\alpha_i$ sont entiers sur $R$, et
\item Si $f$ est presque entier sur $R[x]$,
alors tous les $\alpha_i$ sont presque entiers sur $R$.
\end{enumerate}
\end{lemma}

\begin{proof}
Démontrons d'abord la seconde assertion.
Écrivons $f = \alpha_0 + \alpha_1 x + \ldots + \alpha_r x^r$
avec $\alpha_r \not = 0$.
Par hypothèse, il existe $h = b_0 + b_1 x + \ldots + b_s x^s \in R[x]$,
$b_s \not = 0$, tel que $f^n h \in R[x]$ pour tout
$n \geq 0$. Cela implique que $b_s \alpha_r^n \in R$
pour tout $n \geq 0$. Ainsi, $\alpha_r$ est presque
entier sur $R$. Puisque l'ensemble des éléments presque
entiers forme un sous-anneau (lemme \ref{lemma-almost-integral}), nous en déduisons que
$f - \alpha_r x^r = \alpha_0 + \alpha_1 x + \ldots + \alpha_{r - 1} x^{r - 1}$
est presque entier sur $R[x]$. Une récurrence sur $r$ permet de conclure.

\medskip\noindent
Pour démontrer la première assertion, nous utiliserons une réduction
noethérienne absolue. Écrivons $\alpha_i = a_i / b_i$ et
soit $P(t) = t^d + \sum_{j < d} f_j t^j$ un polynôme
à coefficients $f_j \in R[x]$ tel que $P(f) = 0$.
Soit $f_j = \sum f_{ji}x^i$. Considérons le sous-anneau
$R_0 \subset R$ engendré par la liste finie des éléments
$a_i, b_i, f_{ji}$ de $R$. C'est un anneau intègre ; soit
$K_0$ son corps des fractions. Puisque $R_0$ est une
$\mathbf{Z}$-algèbre de type fini, il est noethérien, voir le
lemme \ref{lemma-obvious-Noetherian}. Il est toujours
vrai que $f \in K_0[x]$ est entier sur $R_0[x]$,
car toutes les identités dans $R$
entre les éléments $a_i, b_i, f_{ji}$ sont également valables dans $R_0$.
D'après le lemme \ref{lemma-almost-integral}, l'élément
$f$ est presque entier sur $R_0[x]$. D'après la seconde assertion du
lemme, les éléments $\alpha_i$ sont presque entiers
sur $R_0$. Et puisque $R_0$ est noethérien, ils sont
entiers sur $R_0$, voir le lemme \ref{lemma-almost-integral}.
Ils sont alors bien sûr entiers sur $R$.
\end{proof}
```

</details>

### 34 — lemma-polynomial-domain-normal

Anglais L8129–8148 ; français L8109–8128.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8129) · FR-ALGEBRA-B11-CHOICE-0034.

Le passage par K[x] montre que g est un polynôme à coefficients dans K, avant d'appliquer le lemme sur les coefficients. Anneau euclidien, principal puis normal ne sont pas trois hypothèses indépendantes. Le français conserve la chaîne de conséquences et la conclusion coefficient par coefficient.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-NORMAL, FR-ALGEBRA-B11-RULE-LOCAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-polynomial-domain-normal}
Let $R$ be a normal domain.
Then $R[x]$ is a normal domain.
\end{lemma}

\begin{proof}
The result is true if $R$ is a field $K$ because
$K[x]$ is a euclidean domain and hence a principal ideal
domain and hence normal by Lemma \ref{lemma-PID-normal}.
Let $g$ be an element of the fraction field of
$R[x]$ which is integral over $R[x]$. Because $g$
is integral over $K[x]$ where $K$ is the fraction
field of $R$ we may write $g = \alpha_d x^d + \alpha_{d-1}x^{d-1} +
\ldots + \alpha_0$ with $\alpha_i \in K$.
By Lemma \ref{lemma-prepare-polynomial-ring-normal}
the elements $\alpha_i$ are integral over $R$ and
hence are in $R$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-polynomial-domain-normal}
Soit $R$ un anneau intègre normal.
Alors $R[x]$ est un anneau intègre normal.
\end{lemma}

\begin{proof}
Le résultat est vrai si $R$ est un corps $K$, car
$K[x]$ est un anneau euclidien, donc un anneau principal,
et donc normal d'après le lemme \ref{lemma-PID-normal}.
Soit $g$ un élément du corps des fractions de
$R[x]$ qui soit entier sur $R[x]$. Puisque $g$
est entier sur $K[x]$, où $K$ est le corps des
fractions de $R$, nous pouvons écrire $g = \alpha_d x^d + \alpha_{d-1}x^{d-1} +
\ldots + \alpha_0$ avec $\alpha_i \in K$.
D'après le lemme \ref{lemma-prepare-polynomial-ring-normal},
les éléments $\alpha_i$ sont entiers sur $R$ et
appartiennent donc à $R$.
\end{proof}
```

</details>

### 35 — lemma-power-series-over-Noetherian-normal-domain

Anglais L8149–8175 ; français L8129–8155.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8149) · FR-ALGEBRA-B11-CHOICE-0035.

Séries formelles et séries de Laurent sont distinguées ; aucune convergence analytique n'est suggérée. Le même h fonctionne pour toutes les puissances e, imposant n≥0 puis la presque-intégralité des coefficients. Noethérianité donne leur intégralité et normalité leur appartenance à R : la dernière condition est implicite dans la phrase abrégée anglaise, non une nouvelle conclusion indépendante.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-NORMAL, FR-ALGEBRA-B11-RULE-LOCAL, FR-ALGEBRA-B11-RULE-POLYNOME, FR-ALGEBRA-B11-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-power-series-over-Noetherian-normal-domain}
Let $R$ be a Noetherian normal domain. Then $R[[x]]$ is
a Noetherian normal domain.
\end{lemma}

\begin{proof}
The power series ring is Noetherian by
Lemma \ref{lemma-Noetherian-power-series}.
Let $f, g \in R[[x]]$ be nonzero elements such that
$w = f/g$ is integral over $R[[x]]$.
Let $K$ be the fraction field of $R$. Since the ring of Laurent series
$K((x)) = K[[x]][1/x]$ is a field, we can write
$w = a_n x^n + a_{n + 1} x^{n + 1} + \ldots$
for some $n \in \mathbf{Z}$, $a_i \in K$, and $a_n \not = 0$.
By Lemma \ref{lemma-almost-integral} we see there exists a
nonzero element $h = b_m x^m + b_{m + 1} x^{m + 1} + \ldots$
in $R[[x]]$ with $b_m \not = 0$ such that
$w^e h \in R[[x]]$ for all $e \geq 1$. We conclude that $n \geq 0$ and that
$b_m a_n^e \in R$ for all $e \geq 1$.
Since $R$ is Noetherian this implies that $a_n \in R$ by
the same lemma. Now, if $a_n, a_{n + 1}, \ldots, a_{N - 1} \in R$,
then we can apply the same argument to
$w - a_n x^n - \ldots - a_{N - 1} x^{N - 1} = a_N x^N + \ldots$.
In this way we see that all $a_i \in R$ and the lemma is proved.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-power-series-over-Noetherian-normal-domain}
Soit $R$ un anneau intègre noethérien normal. Alors $R[[x]]$ est
un anneau intègre noethérien normal.
\end{lemma}

\begin{proof}
L'anneau de séries formelles est noethérien d'après le
lemme \ref{lemma-Noetherian-power-series}.
Soient $f, g \in R[[x]]$ des éléments non nuls tels que
$w = f/g$ soit entier sur $R[[x]]$.
Soit $K$ le corps des fractions de $R$. Puisque l'anneau des séries de Laurent
$K((x)) = K[[x]][1/x]$ est un corps, nous pouvons écrire
$w = a_n x^n + a_{n + 1} x^{n + 1} + \ldots$
pour certains $n \in \mathbf{Z}$, $a_i \in K$, et $a_n \not = 0$.
D'après le lemme \ref{lemma-almost-integral}, nous voyons qu'il existe un
élément non nul $h = b_m x^m + b_{m + 1} x^{m + 1} + \ldots$
de $R[[x]]$, avec $b_m \not = 0$, tel que
$w^e h \in R[[x]]$ pour tout $e \geq 1$. Nous concluons que $n \geq 0$ et que
$b_m a_n^e \in R$ pour tout $e \geq 1$.
Puisque $R$ est noethérien, le même lemme implique que $a_n \in R$.
Maintenant, si $a_n, a_{n + 1}, \ldots, a_{N - 1} \in R$,
nous pouvons appliquer le même argument à
$w - a_n x^n - \ldots - a_{N - 1} x^{N - 1} = a_N x^N + \ldots$.
Nous voyons ainsi que tous les $a_i \in R$, ce qui démontre le lemme.
\end{proof}
```

</details>

### 36 — lemma-normality-is-local

Anglais L8176–8204 ; français L8156–8184.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8176) · FR-ALGEBRA-B11-CHOICE-0036.

Les trois conditions concernent d'abord un anneau intègre et ses localisations. L'intersection se prend dans le même corps des fractions. L'idéal des dénominateurs égal à R conclut sans hypothèse noethérienne. Le renvoi EGA garde numéros et clé ; seul and devient et dans son texte optionnel, contrôlé séparément des formules.

Règles : FR-ALGEBRA-B11-RULE-NORMAL, FR-ALGEBRA-B11-RULE-LOCAL, FR-ALGEBRA-B11-RULE-LOGIQUE, FR-ALGEBRA-B11-RULE-PREMIERS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-normality-is-local}
Let $R$ be a domain. The following are equivalent:
\begin{enumerate}
\item The domain $R$ is a normal domain,
\item for every prime $\mathfrak p \subset R$ the local ring
$R_{\mathfrak p}$ is a normal domain, and
\item for every maximal ideal $\mathfrak m$ the ring $R_{\mathfrak m}$
is a normal domain.
\end{enumerate}
\end{lemma}

\begin{proof}
We deduce (1) $\Rightarrow$ (2) from Lemma \ref{lemma-localize-normal-domain}.
The implication (2) $\Rightarrow$ (3) is immediate. The implication
(3) $\Rightarrow$ (1) follows from the fact that for any domain $R$ we have
$$
R = \bigcap\nolimits_{\mathfrak m} R_{\mathfrak m}
$$
inside the fraction field of $R$. Namely, if $g$ is an element of
the right hand side then the ideal $I = \{x \in R \mid xg \in R\}$
is not contained in any maximal ideal $\mathfrak m$, whence $I = R$.
\end{proof}

\noindent
Lemma \ref{lemma-normality-is-local} shows that the following definition
is compatible with Definition \ref{definition-domain-normal}. (It is the
definition from EGA -- see \cite[IV, 5.13.5 and 0, 4.1.4]{EGA}.)
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-normality-is-local}
Soit $R$ un anneau intègre. Les propriétés suivantes sont équivalentes :
\begin{enumerate}
\item L'anneau intègre $R$ est normal,
\item pour tout idéal premier $\mathfrak p \subset R$, l'anneau local
$R_{\mathfrak p}$ est un anneau intègre normal, et
\item pour tout idéal maximal $\mathfrak m$, l'anneau $R_{\mathfrak m}$
est un anneau intègre normal.
\end{enumerate}
\end{lemma}

\begin{proof}
Nous déduisons (1) $\Rightarrow$ (2) du lemme \ref{lemma-localize-normal-domain}.
L'implication (2) $\Rightarrow$ (3) est immédiate. L'implication
(3) $\Rightarrow$ (1) résulte du fait que, pour tout anneau intègre $R$, nous avons
$$
R = \bigcap\nolimits_{\mathfrak m} R_{\mathfrak m}
$$
dans le corps des fractions de $R$. En effet, si $g$ est un élément du
membre de droite, alors l'idéal $I = \{x \in R \mid xg \in R\}$
n'est contenu dans aucun idéal maximal $\mathfrak m$, d'où $I = R$.
\end{proof}

\noindent
Le lemme \ref{lemma-normality-is-local} montre que la définition suivante
est compatible avec la définition \ref{definition-domain-normal}. (Il s'agit de la
définition d'EGA -- voir \cite[IV, 5.13.5 et 0, 4.1.4]{EGA}.)
```

</details>

### 37 — definition-ring-normal

Anglais L8205–8216 ; français L8185–8196.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8205) · FR-ALGEBRA-B11-CHOICE-0037.

La définition locale impose un anneau intègre normal en chaque premier ; elle n'impose pas que R soit intègre. Le produit des localisations sert à prouver que R est réduit. L'anneau nul satisfait cette définition sans premier, ce qui n'autorise pas à l'appeler un domaine.

Règles : FR-ALGEBRA-B11-RULE-NORMAL, FR-ALGEBRA-B11-RULE-LOCAL, FR-ALGEBRA-B11-RULE-LOGIQUE, FR-ALGEBRA-B11-RULE-PREMIERS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-ring-normal}
A ring $R$ is called {\it normal} if for every prime
$\mathfrak p \subset R$ the localization $R_{\mathfrak p}$ is
a normal domain (see Definition \ref{definition-domain-normal}).
\end{definition}

\noindent
Note that a normal ring is a reduced ring, as $R$ is a subring of the product
of its localizations at all primes (see for example
Lemma \ref{lemma-characterize-zero-local}).
```

Français restauré :
```tex
\begin{definition}
\label{definition-ring-normal}
Un anneau $R$ est dit {\it normal} si, pour tout idéal premier
$\mathfrak p \subset R$, la localisation $R_{\mathfrak p}$ est
un anneau intègre normal (voir la définition \ref{definition-domain-normal}).
\end{definition}

\noindent
Remarquons qu'un anneau normal est réduit, puisque $R$ est un sous-anneau du produit
de ses localisations en tous les idéaux premiers (voir par exemple le
lemme \ref{lemma-characterize-zero-local}).
```

</details>

### 38 — lemma-normal-ring-integrally-closed

Anglais L8217–8236 ; français L8197–8216.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8217) · FR-ALGEBRA-B11-CHOICE-0038.

Anneau total des fractions traduit total ring of fractions, non corps des fractions de R qui peut être non intègre. La platitude donne l'inclusion localisée ; l'idéal I contient un produit ff′ évitant chaque p. La conclusion I=R est préservée. La terminologie est motivée par cette construction source ; les pages françaises nouvelles ne sont pas citées comme attestation exhaustive du terme.

Règles : FR-ALGEBRA-B11-RULE-INTEGRAL, FR-ALGEBRA-B11-RULE-CLOTURE, FR-ALGEBRA-B11-RULE-NORMAL, FR-ALGEBRA-B11-RULE-LOGIQUE, FR-ALGEBRA-B11-RULE-PREMIERS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-normal-ring-integrally-closed}
A normal ring is integrally closed in its total ring of fractions.
\end{lemma}

\begin{proof}
Let $R$ be a normal ring. Let $x \in Q(R)$ be an element of the total ring
of fractions of $R$ integral over $R$. Set $I = \{f \in R, fx \in R\}$. Let
$\mathfrak p \subset R$ be a prime. As $R \to R_{\mathfrak p}$ is
flat we see that $R_{\mathfrak p} \subset Q(R) \otimes_R R_{\mathfrak p}$. As
$R_{\mathfrak p}$ is a normal domain we see that $x \otimes 1$ is an element of
$R_{\mathfrak p}$. Hence we can find $a, f \in R$, $f \not \in \mathfrak p$
such that $x \otimes 1 = a \otimes 1/f$. This means that $fx - a$ maps to
zero in $Q(R) \otimes_R R_{\mathfrak p} = Q(R)_{\mathfrak p}$, which
in turn means that there exists an $f' \in R$, $f' \not \in \mathfrak p$
such that $f'fx = f'a$ in $R$. In other words, $ff' \in I$. Thus $I$
is an ideal which isn't contained in any of the prime ideals of $R$, i.e.,
$I = R$ and $x \in R$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-normal-ring-integrally-closed}
Un anneau normal est intégralement clos dans son anneau total des fractions.
\end{lemma}

\begin{proof}
Soit $R$ un anneau normal. Soit $x \in Q(R)$ un élément de l'anneau total
des fractions de $R$ entier sur $R$. Posons $I = \{f \in R, fx \in R\}$. Soit
$\mathfrak p \subset R$ un idéal premier. Comme $R \to R_{\mathfrak p}$ est
plat, nous voyons que $R_{\mathfrak p} \subset Q(R) \otimes_R R_{\mathfrak p}$. Comme
$R_{\mathfrak p}$ est un anneau intègre normal, nous voyons que $x \otimes 1$ est un élément de
$R_{\mathfrak p}$. Nous pouvons donc trouver $a, f \in R$, $f \not \in \mathfrak p$,
tels que $x \otimes 1 = a \otimes 1/f$. Cela signifie que $fx - a$ s'envoie sur
zéro dans $Q(R) \otimes_R R_{\mathfrak p} = Q(R)_{\mathfrak p}$, ce qui
signifie à son tour qu'il existe un $f' \in R$, $f' \not \in \mathfrak p$,
tel que $f'fx = f'a$ dans $R$. Autrement dit, $ff' \in I$. Ainsi, $I$
est un idéal qui n'est contenu dans aucun idéal premier de $R$, c'est-à-dire
$I = R$ et $x \in R$.
\end{proof}
```

</details>

### 39 — lemma-localization-normal-ring

Anglais L8237–8245 ; français L8217–8225.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8237) · FR-ALGEBRA-B11-CHOICE-0039.

La localisation porte maintenant sur un anneau normal général. On ne réintroduit pas l'intégrité globale de la définition précédente. La preuve demeure omise.

Règles : FR-ALGEBRA-B11-RULE-NORMAL, FR-ALGEBRA-B11-RULE-LOCAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-localization-normal-ring}
A localization of a normal ring is a normal ring.
\end{lemma}

\begin{proof}
Omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-localization-normal-ring}
Une localisation d'un anneau normal est un anneau normal.
\end{lemma}

\begin{proof}
Omis.
\end{proof}
```

</details>

### 40 — lemma-polynomial-ring-normal

Anglais L8246–8258 ; français L8226–8238.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8246) · FR-ALGEBRA-B11-CHOICE-0040.

Le premier q de R[x] se contracte en p de R. C'est R_p[x], puis son localisé, qui est un domaine normal ; R lui-même n'est pas rendu intègre. Chaque domaine et codomaine du passage local est conservé.

Règles : FR-ALGEBRA-B11-RULE-NORMAL, FR-ALGEBRA-B11-RULE-PREMIERS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-polynomial-ring-normal}
Let $R$ be a normal ring. Then $R[x]$ is a normal ring.
\end{lemma}

\begin{proof}
Let $\mathfrak q$ be a prime of $R[x]$. Set $\mathfrak p = R \cap \mathfrak q$.
Then we see that $R_{\mathfrak p}[x]$ is a normal domain by
Lemma \ref{lemma-polynomial-domain-normal}.
Hence $(R[x])_{\mathfrak q}$ is a normal domain by
Lemma \ref{lemma-localize-normal-domain}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-polynomial-ring-normal}
Soit $R$ un anneau normal. Alors $R[x]$ est un anneau normal.
\end{lemma}

\begin{proof}
Soit $\mathfrak q$ un idéal premier de $R[x]$. Posons $\mathfrak p = R \cap \mathfrak q$.
Nous voyons alors que $R_{\mathfrak p}[x]$ est un anneau intègre normal d'après le
lemme \ref{lemma-polynomial-domain-normal}.
Ainsi, $(R[x])_{\mathfrak q}$ est un anneau intègre normal d'après le
lemme \ref{lemma-localize-normal-domain}.
\end{proof}
```

</details>

### 41 — lemma-finite-product-normal

Anglais L8259–8273 ; français L8239–8253.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8259) · FR-ALGEBRA-B11-CHOICE-0041.

Produit fini n'est ni somme directe de modules ni produit infini. Les deux types de premiers de R×S et leurs localisations expliquent la normalité ; le produit global peut avoir des diviseurs de zéro. De même pour S conserve l'étape symétrique abrégée.

Règles : FR-ALGEBRA-B11-RULE-FINITE, FR-ALGEBRA-B11-RULE-NORMAL, FR-ALGEBRA-B11-RULE-LOCAL, FR-ALGEBRA-B11-RULE-LOGIQUE, FR-ALGEBRA-B11-RULE-PREMIERS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-finite-product-normal}
A finite product of normal rings is normal.
\end{lemma}

\begin{proof}
It suffices to show that the product of two normal rings, say $R$ and $S$, is
normal. By Lemma \ref{lemma-disjoint-decomposition} the prime ideals of
$R\times S$ are of the form $\mathfrak{p}\times S$ and $R\times
\mathfrak{q}$, where $\mathfrak{p}$ and $\mathfrak{q}$ are primes of $R$
and $S$ respectively. Localization yields 
$(R\times S)_{\mathfrak{p}\times S}=R_{\mathfrak{p}}$ which is a normal domain
by assumption. Similarly for $S$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-finite-product-normal}
Un produit fini d'anneaux normaux est normal.
\end{lemma}

\begin{proof}
Il suffit de montrer que le produit de deux anneaux normaux, disons $R$ et $S$, est
normal. D'après le lemme \ref{lemma-disjoint-decomposition}, les idéaux premiers de
$R\times S$ sont de la forme $\mathfrak{p}\times S$ et $R\times
\mathfrak{q}$, où $\mathfrak{p}$ et $\mathfrak{q}$ sont des idéaux premiers respectivement de $R$
et de $S$. La localisation donne
$(R\times S)_{\mathfrak{p}\times S}=R_{\mathfrak{p}}$, qui est un anneau intègre normal
par hypothèse. De même pour $S$.
\end{proof}
```

</details>

### 42 — lemma-characterize-reduced-ring-normal

Anglais L8274–8310 ; français L8254–8290.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8274) · FR-ALGEBRA-B11-CHOICE-0042.

Réduit et nombre fini de premiers minimaux sont les hypothèses de l'équivalence. L'anneau total des fractions est un produit fini de corps ; les idempotents entiers y reviennent dans R et donnent sa décomposition. On garde la remarque que deux implications sont générales, sans étendre la troisième au-delà des hypothèses.

Règles : FR-ALGEBRA-B11-RULE-CLOTURE, FR-ALGEBRA-B11-RULE-FINITE, FR-ALGEBRA-B11-RULE-NORMAL, FR-ALGEBRA-B11-RULE-LOCAL, FR-ALGEBRA-B11-RULE-PREMIERS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-reduced-ring-normal}
Let $R$ be a ring. Assume $R$ is reduced and has finitely many
minimal primes. Then the following are equivalent:
\begin{enumerate}
\item $R$ is a normal ring,
\item $R$ is integrally closed in its total ring of fractions, and
\item $R$ is a finite product of normal domains.
\end{enumerate}
\end{lemma}

\begin{proof}
The implications (1) $\Rightarrow$ (2) and
(3) $\Rightarrow$ (1) hold in general,
see Lemmas \ref{lemma-normal-ring-integrally-closed} and
\ref{lemma-finite-product-normal}.

\medskip\noindent
Let $\mathfrak p_1, \ldots, \mathfrak p_n$ be the minimal primes of $R$.
By Lemmas \ref{lemma-reduced-ring-sub-product-fields} and
\ref{lemma-total-ring-fractions-no-embedded-points} we have
$Q(R) = R_{\mathfrak p_1} \times \ldots \times R_{\mathfrak p_n}$, and
by Lemma \ref{lemma-minimal-prime-reduced-ring} each factor is a field.
Denote $e_i = (0, \ldots, 0, 1, 0, \ldots, 0)$ the $i$th idempotent
of $Q(R)$.

\medskip\noindent
If $R$ is integrally closed in $Q(R)$, then it contains in particular
the idempotents $e_i$, and we see that $R$ is a product of $n$
domains (see Sections \ref{section-connected-components} and
\ref{section-tilde-module-sheaf}). Each factor is of the form
$R/\mathfrak p_i$ with field of fractions $R_{\mathfrak p_i}$. 
By Lemma \ref{lemma-finite-product-integral-closure} each map
$R/\mathfrak p_i \to R_{\mathfrak p_i}$ is integrally closed. 
Hence $R$ is a finite product of normal domains.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-characterize-reduced-ring-normal}
Soit $R$ un anneau. Supposons que $R$ soit réduit et possède un nombre fini
d'idéaux premiers minimaux. Alors les propriétés suivantes sont équivalentes :
\begin{enumerate}
\item $R$ est un anneau normal,
\item $R$ est intégralement clos dans son anneau total des fractions, et
\item $R$ est un produit fini d'anneaux intègres normaux.
\end{enumerate}
\end{lemma}

\begin{proof}
Les implications (1) $\Rightarrow$ (2) et
(3) $\Rightarrow$ (1) sont vraies en général,
voir les lemmes \ref{lemma-normal-ring-integrally-closed} et
\ref{lemma-finite-product-normal}.

\medskip\noindent
Soient $\mathfrak p_1, \ldots, \mathfrak p_n$ les idéaux premiers minimaux de $R$.
D'après les lemmes \ref{lemma-reduced-ring-sub-product-fields} et
\ref{lemma-total-ring-fractions-no-embedded-points}, nous avons
$Q(R) = R_{\mathfrak p_1} \times \ldots \times R_{\mathfrak p_n}$, et,
d'après le lemme \ref{lemma-minimal-prime-reduced-ring}, chaque facteur est un corps.
Notons $e_i = (0, \ldots, 0, 1, 0, \ldots, 0)$ le $i$-ème idempotent
de $Q(R)$.

\medskip\noindent
Si $R$ est intégralement clos dans $Q(R)$, alors il contient en particulier
les idempotents $e_i$, et nous voyons que $R$ est un produit de $n$
anneaux intègres (voir les sections \ref{section-connected-components} et
\ref{section-tilde-module-sheaf}). Chaque facteur est de la forme
$R/\mathfrak p_i$, de corps des fractions $R_{\mathfrak p_i}$.
D'après le lemme \ref{lemma-finite-product-integral-closure}, chaque morphisme
$R/\mathfrak p_i \to R_{\mathfrak p_i}$ est intégralement clos.
Ainsi, $R$ est un produit fini d'anneaux intègres normaux.
\end{proof}
```

</details>

### 43 — lemma-colimit-normal-ring

Anglais L8311–8338 ; français L8291–8318.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8311) · FR-ALGEBRA-B11-CHOICE-0043.

Directed system est rendu système filtrant, conformément à la définition française interne et à Ducros 1.6.11.2, plutôt que système inductif seul qui laisse la condition de majorant implicite. Cela restitue une hypothèse anglaise, sans supposer les transitions injectives. Les localisés aux premiers contractés se comparent puis les données polynomiales finies descendent à un stade commun. Le mauvais préfixe du renvoi Categories est conservé et expliqué séparément.

Point particulier à relire : Système filtrant traduit la qualification explicite directed et reprend la définition déjà donnée. Le renvoi sans categories- reste une anomalie officielle distincte, non réparée dans le témoin fidèle.

Règles : FR-ALGEBRA-B11-RULE-NORMAL, FR-ALGEBRA-B11-RULE-POLYNOME, FR-ALGEBRA-B11-RULE-FILTRANT, FR-ALGEBRA-B11-RULE-PREMIERS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-colimit-normal-ring}
Let $(R_i, \varphi_{ii'})$ be a directed system
(Categories, Definition \ref{definition-directed-system})
of rings. If each $R_i$ is a normal ring so is
$R = \colim_i R_i$.
\end{lemma}

\begin{proof}
Let $\mathfrak p \subset R$ be a prime ideal.
Set $\mathfrak p_i = R_i \cap \mathfrak p$ (usual abuse of notation).
Then we see that
$R_{\mathfrak p} = \colim_i (R_i)_{\mathfrak p_i}$.
Since each $(R_i)_{\mathfrak p_i}$ is a normal domain we
reduce to proving the statement of the lemma for normal
domains. If $a, b \in R$ and $a/b$ satisfies a monic polynomial
$P(T) \in R[T]$, then we can find a (sufficiently large) $i \in I$
such that $a, b$ come from objects $a_i, b_i$ over $R_i$, $P$ comes from a
monic polynomial $P_i\in R_i[T]$ and $P_i(a_i/b_i)=0$. Since $R_i$ is normal we
see $a_i/b_i \in R_i$ and hence also $a/b \in R$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-colimit-normal-ring}
Soit $(R_i, \varphi_{ii'})$ un système filtrant
(Catégories, définition \ref{definition-directed-system})
d'anneaux. Si chaque $R_i$ est un anneau normal, alors
$R = \colim_i R_i$ l'est aussi.
\end{lemma}

\begin{proof}
Soit $\mathfrak p \subset R$ un idéal premier.
Posons $\mathfrak p_i = R_i \cap \mathfrak p$ (abus de notation usuel).
Nous voyons alors que
$R_{\mathfrak p} = \colim_i (R_i)_{\mathfrak p_i}$.
Puisque chaque $(R_i)_{\mathfrak p_i}$ est un anneau intègre normal, nous
nous ramenons à démontrer l'énoncé du lemme pour des anneaux intègres
normaux. Si $a, b \in R$ et si $a/b$ satisfait un polynôme unitaire
$P(T) \in R[T]$, alors nous pouvons trouver un $i \in I$ (suffisamment grand)
tel que $a, b$ proviennent d'éléments $a_i, b_i$ sur $R_i$, que $P$ provienne d'un
polynôme unitaire $P_i\in R_i[T]$ et que $P_i(a_i/b_i)=0$. Puisque $R_i$ est normal, nous
voyons que $a_i/b_i \in R_i$, et donc aussi que $a/b \in R$.
\end{proof}
```

</details>

## Observations extérieures au texte traduit

### FR-ALGEBRA-B11-SOURCE-NOTE-0001

[Source L7805](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7805) — lemma-integral-over-field.

```tex
over $k$ and a domain. Pick $s\in S$.
Since $S$ is a domain the multiplication
map $s : S \to S$ is surjective by dimension
reasons.
```

Pour S=k et s=0, multiplication par s est l'application nulle d'un espace vectoriel de dimension un : elle n'est pas surjective. Il faut choisir s non nul ; l'intégrité rend alors cette application injective, et la dimension finie la rend surjective. Le théorème reste vrai. Le français avait déjà réparé ce défaut de prose ; la version fidèle retire non nul et conserve ici la proposition de correction. Le premier choix de s plus haut sert à trouver S′ ; il n'est pas modifié.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

### FR-ALGEBRA-B11-SOURCE-NOTE-0002

[Source L7702](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7702) — lemma-integral-local.

```tex
denote the ideal (!) of leading coefficients of elements of $I$.
```

L'ensemble des coefficients dominants non nuls doit être complété par zéro pour constituer l'idéal J. Pour l'addition, on égalise les degrés par multiplication par des puissances de x ; si les coefficients dominants s'annulent, le résultat zéro est nécessaire. Même convention que dans B9, non un nouvel erratum dédoublonné. Le point d'exclamation et la formulation officielle restent dans la traduction.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

### FR-ALGEBRA-B11-SOURCE-NOTE-0003

[Source L8314](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L8314) — lemma-colimit-normal-ring.

```tex
(Categories, Definition \ref{definition-directed-system})
```

Le label local definition-directed-system existe dans Algebra L715 et définit des systèmes de modules. Le même label existe dans Categories L2692 et traite les systèmes dans une catégorie, y compris les anneaux. Le nom Categories exige le renvoi categories-definition-directed-system pour atteindre cette seconde définition dans le projet multi-chapitres. La chaîne imprimée sans préfixe est conservée dans la traduction fidèle ; la correction proposée est identifiée séparément. La définition française est néanmoins réparée pour traduire directed par filtrant, hypothèse déjà explicite en anglais.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

## Contrôles et suite

Les 705 régions mathématiques concordent après une seule exception exacte de texte traduit dans la définition ensembliste de S′. Le préfixe contient 5 989 régions et dix-neuf exceptions linguistiques, dont dix-huit antérieures. La comparaison brute sans ces exceptions est différente ; aucun masque général ne la remplace.

La citation EGA conserve IV, 5.13.5, 0, 4.1.4 et sa clé EGA ; and devient et dans le texte optionnel. Aucun titre optionnel de théorème ou de preuve dans ce lot. Labels, références, contrôles TeX, environnements et items concordent. Les régions mathématiques du fichier français entier restent inchangées depuis le lot 10. Les opérations inverses retrouvent exactement ce lot puis le témoin public conservé.

Les 295 paires couvrent le préfixe sans lacune ni chevauchement ; les octets avant ce lot et ceux du suffixe non relu sont préservés. La validation structurelle complète la lecture sémantique, elle ne la remplace pas.

Prochaine lecture : Descente pour une extension entière au-dessus d’un anneau normal, anglais L8339 / français L8319. Aucun nouveau PDF ni publication, aucune certification globale du chapitre ou de l’édition.

