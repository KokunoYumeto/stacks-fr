# Algèbre commutative : idéaux premiers et images constructibles

## Résultat et portée

Trois sections entièrement comparées : anglais L5089–5979 et français L5069–5959. Les 35 paires contiennent tous les énoncés, preuves, exemples et transitions. 203 occurrences sont reliées à des règles contextualisées. Le préfixe relu atteint 30 sections, 201 paires et 1529 occurrences. Le chapitre et l’édition restent inachevés.

Deux opérations rétablissent les objets ambiants écrits dans la prose officielle : un élément décrit comme appartenant à κ(p), et un fermé décrit comme appartenant à R. Le français antérieur les avait mathématiquement corrigés. Le corps fidèle retrouve ces lectures officielles ; les propositions de correction et leur justification restent séparées. Aucun symbole mathématique ne change.

Sept observations distinguent deux corrections ambiantes, un symbole non défini, deux abus de contraction, une partition ensembliste et une énumération abrégée. Ce ne sont pas sept nouveaux théorèmes erronés ni sept admissions dans un registre. Aucune déduplication des propositions d’errata déjà connues n’est revendiquée.

Comparaison assistée par IA, sans relecture humaine. Le canon a été réellement consulté rétrospectivement ; aucune consultation ancienne n’est inventée. L’absence d’attestation pour famille d’Oka est signalée et ne bloque pas la décision motivée.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch8.fr.tex) · [État français précédent](staged/fr/010_algebra.prose-batch7.fr.tex) · [Lot précédent](ALGEBRA_PROSE_BATCH7_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH8_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH8_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH8_OCCURRENCES.json) · [Restaurations avant/après](ALGEBRA_PROSE_BATCH8_REPAIRS.json) · [Exceptions linguistiques des formules](ALGEBRA_PROSE_BATCH8_MATH_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH8_COVERAGE.json) · [Observations de source séparées](ALGEBRA_PROSE_BATCH8_SOURCE_OBSERVATIONS.json).

## Canon et définitions effectivement consultés

### Antoine Ducros — Cours sur les schémas

[Source universitaire](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [PDF conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages PDF et imprimées 24–26 et 70 lues intégralement ; 0.1.4–8, 0.2.1–6 et 2.1.3.1–4. Page 26 également rendue et inspectée.

Attestations courtes : « une famille génératrice finie », « de présentation finie », « partie multiplicative », « éléments nilpotents ».

Atteste le registre des modules de type fini, libres, de présentation finie, des éléments nilpotents et des parties multiplicatives. Les distinctions entre objet fini et génération finie, ainsi qu'entre anneau et corps, gouvernent les choix du lot.

Limites : N'atteste pas famille d'Oka ni la proposition qui la concerne. La page 26 définit la présentation finie des modules ; la définition pour les algèbres vient de Dat p.11. Aucune hypothèse d'intégrité ou noethérienne n'est importée depuis les exemples.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

### Jean-François Dat — Cours de schémas, M2

[Source universitaire](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/Schemas/Schemas.pdf) · [PDF conservé](canon-consulted/fr-algebra/dat-schemas.pdf)

Pages PDF et imprimées 9–13 lues intégralement : fin de 1.2.5, 1.2.6–8 et début de 1.3. Pages 11 et 13 également rendues et inspectées.

Attestations courtes : « Constructibilité et présentation finie », « ouverts principaux », « polynôme caractéristique de la multiplication », « point générique ».

Appui direct au vocabulaire et à la portée non noethérienne de la constructibilité, à l'énoncé de Chevalley, à sa preuve par récurrence, à la multiplication sur une algèbre libre finie et aux corps résiduels. Le texte distingue expressément type fini et présentation finie.

Limites : L'attestation ne rend pas chaque formule infaillible : la définition du morphisme local p.10 inverse les idéaux ; p.13 les indices de la réunion ne correspondent pas aux c1,...,cd et la lettre T succède à X. Ces anomalies ne sont pas importées. Les variantes de la preuve ne remplacent pas celle du témoin officiel. Rétrocompact et famille d'Oka ne sont pas attestés dans ces pages.

SHA-256 : 9298B062AC2BDF64161A107980A30F98E1F2DF6DEB4DA98E1FEB21BA494D26A1.

### Stacks Project officiel — définitions anglaises de contrôle

[Source universitaire](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L1627) · [PDF conservé](../../03_working_translations/stacks_cjk_20260821/upstream/src/stacks-project-a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex)

Définition quasi-compact L1627–1639 et définition constructible L2553–2568, avec sa note sur EGA I ; énoncé et preuve suivant L2570–2587 lus.

Attestations courtes : « retrocompact », « finite union », « locally constructible ».

Fixe la notion mathématique : l'inclusion rétrocompacte est quasi-compacte et une partie constructible est une réunion finie de U intersection complémentaire de V avec U,V ouverts rétrocompacts. La convention locale reste distincte.

Limites : Autorité de contenu en anglais, pas attestation lexicale française. La note compare une convention d'EGA I seconde édition, sans autoriser à renommer la notion de Stacks. La totalité du chapitre Topology n'est pas déclarée relue.

SHA-256 : C6BAC8DCF8AD96DC47416BF34CB45BA4A10B894E40D67D3E1FA68D8EF0D9F872.

## Règles contextualisées

### FR-ALGEBRA-B8-RULE-OKA

Nom propre et définition source conservés. Attestation française indépendante non acquise ; la cohérence des occurrences est vérifiée sans prétendre que la règle lexicale prouve la proposition.

Canon : Définitions et comparaison directe ; attestation externe exhaustive non acquise.

### FR-ALGEBRA-B8-RULE-IDEAL

Premier, maximal dans l'anneau et maximal relativement à une famille ont été distingués dans chaque paire complète. Principal qualifie un idéal sans imposer l'intégrité de R ; les formules de définitions gouvernent ces choix.

Canon : Définitions et comparaison directe ; attestation externe exhaustive non acquise.

### FR-ALGEBRA-B8-RULE-MAXIMALITE

Maximalité et complémentaire sont interprétés dans l'ensemble précis des idéaux de l'argument, ou dans l'espace topologique lorsqu'il s'agit d'un complémentaire d'ouvert. Aucun passage automatique de maximal relatif à idéal maximal.

Canon : Définitions et comparaison directe ; attestation externe exhaustive non acquise.

### FR-ALGEBRA-B8-RULE-MULTIPLICATIVE

Partie multiplicative reprend Ducros 2.1.3.3 : contient 1 et est stable par produit. Ni fermeture topologique ni groupe multiplicatif ne sont imposés.

Canon : FR-ALGEBRA-B8-CANON-DUCROS.

### FR-ALGEBRA-B8-RULE-FINITUDE

Le module/idéal de type fini a une famille génératrice finie ; pour une algèbre de présentation finie on exige aussi un nombre fini de relations. Les occurrences ont été lues selon leur objet, sans confondre module et algèbre.

Canon : FR-ALGEBRA-B8-CANON-DUCROS, FR-ALGEBRA-B8-CANON-DAT.

### FR-ALGEBRA-B8-RULE-CONSTRUCTIBLE

Dat p.11 et la définition de Topology sont compatibles sur Spec(R). Finitude des réunions et finitude des équations sont conservées, sans hypothèse noethérienne importée.

Canon : FR-ALGEBRA-B8-CANON-DAT, FR-ALGEBRA-B8-CANON-TOPOLOGY.

### FR-ALGEBRA-B8-RULE-QUASICOMPACT

Sens régi par les définitions officielles effectivement lues ; rétrocompact est une propriété de l'inclusion. La graphie française est retenue par continuité du témoin, sans attestation française indépendante nouvelle pour rétrocompact.

Canon : FR-ALGEBRA-B8-CANON-TOPOLOGY.

### FR-ALGEBRA-B8-RULE-OPEN

Ouvert principal correspond à D(f), ouvert dense n'est pas tout le spectre, fermé propre est une partie topologique. Le mauvais objet R dans une phrase officielle est conservé et signalé séparément.

Canon : FR-ALGEBRA-B8-CANON-DAT.

### FR-ALGEBRA-B8-RULE-POLYNOME

Le coefficient dominant inversible rend le quotient libre fini ; le polynôme caractéristique est celui de la multiplication comme endomorphisme. Unitaire ne remplace pas algébrique dans la dernière preuve.

Canon : FR-ALGEBRA-B8-CANON-DAT.

### FR-ALGEBRA-B8-RULE-NILPOTENT

Nilpotence de l'élément et nilpotence de son endomorphisme de multiplication sont distinguées par l'objet explicite. Un idéal constitué d'éléments nilpotents n'est pas déclaré nilpotent.

Canon : FR-ALGEBRA-B8-CANON-DUCROS, FR-ALGEBRA-B8-CANON-DAT.

### FR-ALGEBRA-B8-RULE-RESIDUEL

Le corps résiduel est attaché au premier ; le corps des fractions suppose l'intégrité. Les éléments de la fibre tensorisée ne sont pas assimilés aux scalaires, sauf dans la lecture source fautive signalée.

Canon : FR-ALGEBRA-B8-CANON-DAT, FR-ALGEBRA-B8-CANON-DUCROS.

### FR-ALGEBRA-B8-RULE-IMAGE

Le morphisme d'anneaux et l'application contravariante sur les spectres sont suivis dans les phrases et diagrammes. Image réciproque ne devient pas image directe ; la surjectivité des spectres ne signifie pas surjectivité des anneaux.

Canon : Définitions et comparaison directe ; attestation externe exhaustive non acquise.

### FR-ALGEBRA-B8-RULE-INTEGRE

Domain est rendu par anneau intègre et nonzerodivisor par non diviseur de zéro, selon les définitions déjà fixées dans le chapitre. Ce n'est ni corps ni unité en général ; les hypothèses non nul demeurent exactement où l'anglais les impose.

Canon : Définitions et comparaison directe ; attestation externe exhaustive non acquise.

### FR-ALGEBRA-B8-RULE-NOETHERIEN

Le mot noethérien qualifie soit l'anneau soit l'espace topologique selon le sujet explicite. La condition de chaîne ascendante concerne ici les idéaux radicaux ; aucune équivalence générale entre les deux noethérianités n'est ajoutée.

Canon : FR-ALGEBRA-B8-CANON-DUCROS.

### FR-ALGEBRA-B8-RULE-EXACT

Le contexte distingue suite exacte de modules et exactitude de la localisation. Les flèches et quotients complets sont lus ; la règle ne revendique pas une attestation française spécifique supplémentaire pour chaque construction.

Canon : Définitions et comparaison directe ; attestation externe exhaustive non acquise.

## Passages parallèles complets

### 01 — section-oka-families

Anglais L5089–5114 ; français L5069–5094.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5089) · FR-ALGEBRA-B8-CHOICE-0001.

L'attribution au projet CRing et la citation Lam–Reyes sont conservées ; cette citation n'est pas présentée comme une publication effectivement consultée. Maximal parmi les idéaux disjoints de S est une maximalité relative, non l'assertion que l'idéal est maximal dans R. Les deux définitions par conditions xa et xJ sont intégralement maintenues. Partie multiplicative est attesté chez Ducros 2.1.3.3. L'écriture R intersection m désigne une contraction par abus ; aucune injectivité de R vers son localisé n'est ajoutée.

Point particulier à relire : R intersection m est compris comme image réciproque par la localisation. La lecture ensembliste littérale exigerait une injection qui n'est pas donnée.

Règles : FR-ALGEBRA-B8-RULE-IDEAL, FR-ALGEBRA-B8-RULE-MAXIMALITE, FR-ALGEBRA-B8-RULE-MULTIPLICATIVE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{A meta-observation about prime ideals}
\label{section-oka-families}

\noindent
This section is taken from the CRing project. Let $R$ be a ring and
let $S \subset R$ be a multiplicative subset.
A consequence of
Lemma \ref{lemma-spec-localization}
is that an ideal $I \subset R$ maximal with respect to the property
of not intersecting $S$ is prime. The reason is that $I = R \cap \mathfrak m$
for some maximal ideal $\mathfrak m$ of the ring $S^{-1}R$.
It turns out that for many properties of ideals, the maximal ones
are prime. A general method of seeing this was developed in \cite{Lam-Reyes}.
In this section, we digress to explain this phenomenon.

\medskip\noindent
Let $R$ be a ring. If $I$ is an ideal of $R$ and $a \in R$, we
define
$$
(I : a) = \left\{ x \in R \mid xa \in I\right\}.
$$
More generally, if $J \subset R$ is an ideal, we define
$$
(I : J) = \left\{ x \in R \mid xJ \subset I\right\}.
$$
```

Français restauré :
```tex
\section{Une méta-observation sur les idéaux premiers}
\label{section-oka-families}

\noindent
Cette section est tirée du projet CRing. Soit $R$ un anneau et
soit $S \subset R$ une partie multiplicative.
Une conséquence du
lemme \ref{lemma-spec-localization}
est qu'un idéal $I \subset R$ maximal parmi ceux qui ne
rencontrent pas $S$ est premier. La raison en est que $I = R \cap \mathfrak m$
pour un certain idéal maximal $\mathfrak m$ de l'anneau $S^{-1}R$.
Il s'avère que, pour de nombreuses propriétés d'idéaux, les éléments maximaux
sont premiers. Une méthode générale permettant de le voir a été développée dans \cite{Lam-Reyes}.
Dans cette section, nous faisons une digression pour expliquer ce phénomène.

\medskip\noindent
Soit $R$ un anneau. Si $I$ est un idéal de $R$ et $a \in R$, nous
définissons
$$
(I : a) = \left\{ x \in R \mid xa \in I\right\}.
$$
Plus généralement, si $J \subset R$ est un idéal, nous définissons
$$
(I : J) = \left\{ x \in R \mid xJ \subset I\right\}.
$$
```

</details>

### 02 — lemma-colon

Anglais L5115–5133 ; français L5095–5113.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5115) · FR-ALGEBRA-B8-CHOICE-0002.

La principalité porte sur J et l'inclusion I dans J est essentielle. La preuve conserve séparément les deux inclusions, le générateur a et la condition x dans (I:a). L'identité I=J(I:J) n'est pas affirmée pour deux idéaux quelconques. La transition qui suit concerne les éléments maximaux du complémentaire d'une famille, et non ses éléments maximaux internes.

Règles : FR-ALGEBRA-B8-RULE-IDEAL, FR-ALGEBRA-B8-RULE-MAXIMALITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-colon}
Let $R$ be a ring. For a principal ideal $J \subset R$, and for any ideal
$I \subset J$ we have $I = J (I : J)$.
\end{lemma}

\begin{proof}
Say $J = (a)$. Then $(I : J) = (I : a)$.
Since $I \subset J$ we see that any $y \in I$ is of the form
$y = xa$ for some $x \in (I : a)$. Hence $I \subset J (I : J)$.
Conversely, if $x \in (I : a)$, then $xJ = (xa) \subset I$, which
proves the other inclusion.
\end{proof}

\noindent
Let $\mathcal{F}$ be a collection of ideals of $R$. We are interested in
conditions that will guarantee that the maximal elements in the complement
of $\mathcal{F}$ are prime.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-colon}
Soit $R$ un anneau. Pour un idéal principal $J \subset R$ et pour tout idéal
$I \subset J$, nous avons $I = J (I : J)$.
\end{lemma}

\begin{proof}
Écrivons $J = (a)$. Alors $(I : J) = (I : a)$.
Puisque $I \subset J$, nous voyons que tout $y \in I$ est de la forme
$y = xa$ pour un certain $x \in (I : a)$. Ainsi, $I \subset J (I : J)$.
Réciproquement, si $x \in (I : a)$, alors $xJ = (xa) \subset I$, ce qui
démontre l'autre inclusion.
\end{proof}

\noindent
Soit $\mathcal{F}$ une collection d'idéaux de $R$. Nous cherchons des
conditions garantissant que les éléments maximaux du complémentaire
de $\mathcal{F}$ sont premiers.
```

</details>

### 03 — definition-oka-family

Anglais L5134–5145 ; français L5114–5125.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5134) · FR-ALGEBRA-B8-CHOICE-0003.

Famille d'Oka reprend le nom propre et la définition anglaise, avec R membre de la famille et les deux conditions sur (I:a) et (I,a) pour un même a. Aucune attestation française indépendante de ce syntagme n'a été acquise dans les pages lues : choix provisoire transparent, non terme prétendument attesté par Dat ou Ducros. Famille convient à une collection d'idéaux ; famille ouverte ou idéale seraient des contresens.

Point particulier à relire : L'appellation française famille d'Oka reste une proposition motivée par le nom et la définition, sans attestation française externe acquise ici.

Règles : FR-ALGEBRA-B8-RULE-OKA.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-oka-family}
Let $R$ be a ring. Let $\mathcal{F}$ be a set of ideals of $R$. We say
$\mathcal{F}$ is an {\it Oka family} if $R \in \mathcal{F}$ and
whenever $I \subset R$ is an ideal and $(I : a), (I, a) \in \mathcal{F}$
for some $a \in R$, then $I \in \mathcal{F}$.
\end{definition}

\noindent
Let us give some examples of Oka families. The first example is the basic
example discussed in the introduction to this section.
```

Français restauré :
```tex
\begin{definition}
\label{definition-oka-family}
Soit $R$ un anneau. Soit $\mathcal{F}$ un ensemble d'idéaux de $R$. Nous disons
que $\mathcal{F}$ est une {\it famille d'Oka} si $R \in \mathcal{F}$ et si,
chaque fois que $I \subset R$ est un idéal et que $(I : a), (I, a) \in \mathcal{F}$
pour un certain $a \in R$, alors $I \in \mathcal{F}$.
\end{definition}

\noindent
Donnons quelques exemples de familles d'Oka. Le premier est l'exemple
fondamental présenté dans l'introduction de cette section.
```

</details>

### 04 — example-oka-family-not-meet-multiplicative-set

Anglais L5146–5155 ; français L5126–5135.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5146) · FR-ALGEBRA-B8-CHOICE-0004.

La famille contient précisément les idéaux qui rencontrent S, même si le label historique contient not-meet. Le complémentaire est utilisé ensuite dans la proposition. Les deux choix s et s' et le produit ss' restent dans le bon ordre d'appartenance. La traduction ne renverse pas le signe non vide pour harmoniser artificiellement le label et le texte.

Règles : FR-ALGEBRA-B8-RULE-OKA, FR-ALGEBRA-B8-RULE-MULTIPLICATIVE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-oka-family-not-meet-multiplicative-set}
Let $R$ be a ring and let $S$ be a multiplicative subset of $R$.
We claim that $\mathcal{F} = \{I \subset R \mid I \cap S \not = \emptyset\}$
is an Oka family. Namely, suppose that $(I : a), (I, a) \in \mathcal{F}$
for some $a \in R$. Then pick $s \in (I, a) \cap S$ and
$s' \in (I : a) \cap S$. Then $ss' \in I \cap S$ and hence
$I \in \mathcal{F}$. Thus $\mathcal{F}$ is an Oka family.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-oka-family-not-meet-multiplicative-set}
Soit $R$ un anneau et soit $S$ une partie multiplicative de $R$.
Nous affirmons que $\mathcal{F} = \{I \subset R \mid I \cap S \not = \emptyset\}$
est une famille d'Oka. En effet, supposons que $(I : a), (I, a) \in \mathcal{F}$
pour un certain $a \in R$. Choisissons alors $s \in (I, a) \cap S$ et
$s' \in (I : a) \cap S$. Alors $ss' \in I \cap S$, et donc
$I \in \mathcal{F}$. Ainsi, $\mathcal{F}$ est une famille d'Oka.
\end{example}
```

</details>

### 05 — example-oka-family-finitely-generated

Anglais L5156–5169 ; français L5136–5149.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5156) · FR-ALGEBRA-B8-CHOICE-0005.

De type fini traduit finitely generated pour l'idéal considéré comme module, conformément à Ducros 0.2.5. Le nombre fini de générateurs et l'appartenance des bj à I sont préservés. Le coefficient de a appartient à l'idéal quotient (I:a), et non à I par nécessité. Fini tout court serait faux : un idéal de type fini n'est pas un ensemble fini.

Règles : FR-ALGEBRA-B8-RULE-OKA, FR-ALGEBRA-B8-RULE-FINITUDE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-oka-family-finitely-generated}
Let $R$ be a ring, $I \subset R$ an ideal, and $a \in R$.
If $(I : a)$ is generated by $a_1, \ldots, a_n$ and $(I, a)$
is generated by $a, b_1, \ldots, b_m$ with
$b_1, \ldots, b_m \in I$, then $I$ is generated by
$aa_1, \ldots, aa_n, b_1, \ldots, b_m$.
To see this, note that if $x \in I$, then $x \in (I, a)$
is a linear combination of $a, b_1, \ldots, b_m$, but the
coefficient of $a$ must lie in $(I:a)$.
As a result, we deduce that
the family of finitely generated ideals is an Oka family.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-oka-family-finitely-generated}
Soient $R$ un anneau, $I \subset R$ un idéal et $a \in R$.
Si $(I : a)$ est engendré par $a_1, \ldots, a_n$ et si $(I, a)$
est engendré par $a, b_1, \ldots, b_m$, avec
$b_1, \ldots, b_m \in I$, alors $I$ est engendré par
$aa_1, \ldots, aa_n, b_1, \ldots, b_m$.
Pour le voir, notons que, si $x \in I$, alors $x \in (I, a)$
est une combinaison linéaire de $a, b_1, \ldots, b_m$, mais le
coefficient de $a$ doit appartenir à $(I:a)$.
Nous en déduisons que
la famille des idéaux de type fini est une famille d'Oka.
\end{example}
```

</details>

### 06 — example-oka-family-principal

Anglais L5170–5181 ; français L5150–5161.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5170) · FR-ALGEBRA-B8-CHOICE-0006.

Principaux qualifie les idéaux, sans déclarer l'anneau intègre. La preuve utilise J=(I,a), l'égalité des deux idéaux quotients puis le produit de deux idéaux principaux. Il n'est ajouté ni unicité des générateurs ni hypothèse factorielle. Le terme anneau principal n'est pas substitué à la conclusion sur les idéaux, car il comporte souvent une convention d'intégrité en français.

Règles : FR-ALGEBRA-B8-RULE-OKA, FR-ALGEBRA-B8-RULE-IDEAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-oka-family-principal}
Let us show that the family of principal ideals of a ring $R$ is an Oka family.
Indeed, suppose $I \subset R$ is an ideal, $a \in R$, and $(I, a)$ and
$(I : a)$ are principal. Note that $(I : a) = (I : (I, a))$.
Setting $J = (I, a)$, we find that $J$ is principal and $(I : J)$ is too. By
Lemma \ref{lemma-colon}
we have $I = J (I : J)$.
Thus we find in our situation that since $J = (I, a)$ and $(I : J)$
are principal, $I$ is principal.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-oka-family-principal}
Montrons que la famille des idéaux principaux d'un anneau $R$ est une famille d'Oka.
En effet, supposons que $I \subset R$ soit un idéal, que $a \in R$ et que $(I, a)$ et
$(I : a)$ soient principaux. Notons que $(I : a) = (I : (I, a))$.
En posant $J = (I, a)$, nous constatons que $J$ est principal et que $(I : J)$ l'est aussi. D'après
le lemme \ref{lemma-colon},
nous avons $I = J (I : J)$.
Ainsi, dans notre situation, puisque $J = (I, a)$ et $(I : J)$
sont principaux, $I$ est principal.
\end{example}
```

</details>

### 07 — example-oka-family-bound-cardinality

Anglais L5182–5191 ; français L5162–5171.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5182) · FR-ALGEBRA-B8-CHOICE-0007.

Au plus κ est conservé avec la condition cardinal infini. Ce n'est ni exactement κ générateurs distincts ni une famille finie. L'omission de la démonstration est traduite comme une omission de l'auteur, pas remplacée par une preuve nouvelle. Le passage français préserve le renvoi à l'exemple de type fini.

Règles : FR-ALGEBRA-B8-RULE-OKA.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-oka-family-bound-cardinality}
Let $R$ be a ring.
Let $\kappa$ be an infinite cardinal.
The family of ideals which can be generated by at most $\kappa$ elements
is an Oka family. The argument is analogous to the argument in
Example \ref{example-oka-family-finitely-generated}
and is omitted.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-oka-family-bound-cardinality}
Soit $R$ un anneau.
Soit $\kappa$ un cardinal infini.
La famille des idéaux qui peuvent être engendrés par au plus $\kappa$ éléments
est une famille d'Oka. L'argument est analogue à celui de
l'exemple \ref{example-oka-family-finitely-generated}
et est omis.
\end{example}
```

</details>

### 08 — example-oka-family-property-modules

Anglais L5192–5201 ; français L5172–5181.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5192) · FR-ALGEBRA-B8-CHOICE-0008.

Suite exacte courte, stable par extensions et vérifiée par le module nul traduisent les trois données distinctes. La première flèche est la multiplication par a, et le module auquel P s'applique est A/I, non I. Extensions signifie extensions de modules au sens des suites exactes, pas extensions de corps. La définition d'Oka s'applique grâce au cas I=A où A/I=0.

Règles : FR-ALGEBRA-B8-RULE-OKA, FR-ALGEBRA-B8-RULE-EXACT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-oka-family-property-modules}
Let $A$ be a ring, $I \subset A$ an ideal, and $a \in A$ an element.
There is a short exact sequence $0 \to A/(I : a) \to A/I \to A/(I, a) \to 0$
where the first arrow is given by multiplication by $a$. Thus if $P$
is a property of $A$-modules that is stable under extensions and holds
for $0$, then the family of ideals $I$ such that $A/I$ has $P$
is an Oka family.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-oka-family-property-modules}
Soient $A$ un anneau, $I \subset A$ un idéal et $a \in A$ un élément.
Il existe une suite exacte courte $0 \to A/(I : a) \to A/I \to A/(I, a) \to 0$
dont la première flèche est donnée par la multiplication par $a$. Ainsi, si $P$
est une propriété des $A$-modules qui est stable par extensions et qui est vérifiée
par $0$, alors la famille des idéaux $I$ tels que $A/I$ possède $P$
est une famille d'Oka.
\end{example}
```

</details>

### 09 — proposition-oka

Anglais L5202–5221 ; français L5182–5201.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5202) · FR-ALGEBRA-B8-CHOICE-0009.

Tout élément maximal du complémentaire reste une maximalité pour l'inclusion parmi les idéaux exclus. Dans la preuve, a et b sont tous deux hors de I, ab est dans I, et les deux idéaux agrandis contiennent strictement I. La contradiction vient de leur appartenance à la famille et de la condition d'Oka. L'argument entier et la transition finale sont conservés.

Règles : FR-ALGEBRA-B8-RULE-OKA, FR-ALGEBRA-B8-RULE-IDEAL, FR-ALGEBRA-B8-RULE-MAXIMALITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{proposition}
\label{proposition-oka}
If $\mathcal{F}$ is an Oka family of ideals, then any maximal element of
the complement of $\mathcal{F}$ is prime.
\end{proposition}

\begin{proof}
Suppose $I \not \in \mathcal{F}$ is maximal with respect to not being in
$\mathcal{F}$ but $I$ is not prime. Note that $I \not = R$ because
$R \in \mathcal{F}$. Since $I$ is not prime we can find $a, b \in R - I$
with $ab \in I$. It follows that $(I, a) \neq I$ and $(I : a)$ contains
$b \not \in I$ so also $(I : a) \neq I$. Thus $(I : a), (I, a)$ both
strictly contain $I$, so they must belong to $\mathcal{F}$.
By the Oka condition, we have $I \in \mathcal{F}$, a contradiction.
\end{proof}

\noindent
At this point we are able to turn most of the examples above into
a lemma about prime ideals in a ring.
```

Français restauré :
```tex
\begin{proposition}
\label{proposition-oka}
Si $\mathcal{F}$ est une famille d'Oka d'idéaux, alors tout élément maximal du
complémentaire de $\mathcal{F}$ est premier.
\end{proposition}

\begin{proof}
Supposons que $I \not \in \mathcal{F}$ soit maximal parmi les idéaux qui n'appartiennent pas à
$\mathcal{F}$, mais que $I$ ne soit pas premier. Notons que $I \not = R$, car
$R \in \mathcal{F}$. Puisque $I$ n'est pas premier, nous pouvons trouver $a, b \in R - I$
tels que $ab \in I$. Il s'ensuit que $(I, a) \neq I$ et que $(I : a)$ contient
$b \not \in I$, donc que $(I : a) \neq I$ également. Ainsi, $(I : a), (I, a)$ contiennent tous deux
strictement $I$ et doivent donc appartenir à $\mathcal{F}$.
Par la condition d'Oka, nous avons $I \in \mathcal{F}$, ce qui est une contradiction.
\end{proof}

\noindent
Nous pouvons maintenant convertir la plupart des exemples ci-dessus en
un lemme sur les idéaux premiers d'un anneau.
```

</details>

### 10 — lemma-simple

Anglais L5222–5236 ; français L5202–5216.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5222) · FR-ALGEBRA-B8-CHOICE-0010.

Maximal parmi ceux qui vérifient I intersection S vide ne devient pas idéal maximal de R. La preuve alternative garde exactement ses deux renvois. Le résultat n'exige pas que S soit le complémentaire d'un idéal premier : partie multiplicative garde la définition générale de Ducros 2.1.3.3.

Règles : FR-ALGEBRA-B8-RULE-MAXIMALITE, FR-ALGEBRA-B8-RULE-MULTIPLICATIVE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-simple}
Let $R$ be a ring. Let $S$ be a multiplicative subset of $R$.
An ideal $I \subset R$ which is maximal with respect to the property
that $I \cap S = \emptyset$ is prime.
\end{lemma}

\begin{proof}
This is the example discussed in the introduction to this section.
For an alternative proof, combine
Example \ref{example-oka-family-not-meet-multiplicative-set}
with
Proposition \ref{proposition-oka}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-simple}
Soit $R$ un anneau. Soit $S$ une partie multiplicative de $R$.
Un idéal $I \subset R$ maximal parmi ceux qui vérifient
$I \cap S = \emptyset$ est premier.
\end{lemma}

\begin{proof}
C'est l'exemple présenté dans l'introduction de cette section.
Pour une autre démonstration, combiner
l'exemple \ref{example-oka-family-not-meet-multiplicative-set}
avec la
proposition \ref{proposition-oka}.
\end{proof}
```

</details>

### 11 — lemma-cohen

Anglais L5237–5263 ; français L5217–5243.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5237) · FR-ALGEBRA-B8-CHOICE-0011.

Les deux assertions sont distinctes : maximalité d'un idéal non de type fini, puis critère par tous les idéaux premiers. Dans le raisonnement de Zorn, les générateurs en nombre fini appartiennent simultanément à un même membre de la chaîne totalement ordonnée. La note annonçant le mot noethérien plus loin est conservée. L'expression de type fini est justifiée par la définition de module chez Ducros ; aucune hypothèse noethérienne initiale n'est insérée.

Règles : FR-ALGEBRA-B8-RULE-IDEAL, FR-ALGEBRA-B8-RULE-MAXIMALITE, FR-ALGEBRA-B8-RULE-FINITUDE, FR-ALGEBRA-B8-RULE-NOETHERIEN.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-cohen}
Let $R$ be a ring.
\begin{enumerate}
\item An ideal $I \subset R$ maximal with respect to not being
finitely generated is prime.
\item If every prime ideal of $R$ is
finitely generated, then
every ideal of $R$ is finitely generated\footnote{Later we will say
that $R$ is Noetherian.}.
\end{enumerate}
\end{lemma}

\begin{proof}
The first assertion is an immediate consequence of
Example \ref{example-oka-family-finitely-generated} and
Proposition \ref{proposition-oka}. For the second,
suppose that there exists an ideal $I \subset R$ which is not finitely
generated. The union of a totally ordered chain $\left\{I_\alpha\right\}$
of ideals that are not finitely generated is not finitely generated;
indeed, if $I = \bigcup I_\alpha$ were generated by
$a_1, \ldots, a_n$, then all the generators would belong to some
$I_\alpha $ and would consequently generate it.
By Zorn's lemma, there is an ideal maximal with respect to being not finitely
generated. By the first part this ideal is prime.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-cohen}
Soit $R$ un anneau.
\begin{enumerate}
\item Un idéal $I \subset R$ maximal parmi ceux qui ne sont pas
de type fini est premier.
\item Si tout idéal premier de $R$ est
de type fini, alors
tout idéal de $R$ est de type fini\footnote{Nous dirons plus loin
que $R$ est noethérien.}.
\end{enumerate}
\end{lemma}

\begin{proof}
La première assertion est une conséquence immédiate de
l'exemple \ref{example-oka-family-finitely-generated} et de la
proposition \ref{proposition-oka}. Pour la seconde,
supposons qu'il existe un idéal $I \subset R$ qui ne soit pas de type
fini. La réunion d'une chaîne totalement ordonnée $\left\{I_\alpha\right\}$
d'idéaux qui ne sont pas de type fini n'est pas de type fini ;
en effet, si $I = \bigcup I_\alpha$ était engendré par
$a_1, \ldots, a_n$, alors tous les générateurs appartiendraient à un certain
$I_\alpha $ et l'engendreraient par conséquent.
D'après le lemme de Zorn, il existe un idéal maximal parmi ceux qui ne sont pas de type
fini. D'après la première partie, cet idéal est premier.
\end{proof}
```

</details>

### 12 — lemma-primes-principal

Anglais L5264–5287 ; français L5244–5267.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5264) · FR-ALGEBRA-B8-CHOICE-0012.

Le résultat porte sur la principalité de chaque idéal, sans supposer R intègre. La réunion d'une chaîne est non principale parce qu'un générateur de la réunion appartiendrait à l'un des membres et l'engendrerait. Le féminin principale se rapporte à réunion : adaptation grammaticale, pas modification du résultat. Dire directement R est un anneau principal pourrait introduire une convention supplémentaire et est donc évité.

Point particulier à relire : Ne pas convertir la conclusion en anneau principal si ce terme impose par convention l'intégrité : Z/4Z fournit un anneau non intègre dont tous les idéaux sont principaux.

Règles : FR-ALGEBRA-B8-RULE-IDEAL, FR-ALGEBRA-B8-RULE-MAXIMALITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-primes-principal}
Let $R$ be a ring.
\begin{enumerate}
\item An ideal $I \subset R$ maximal with respect to not being
principal is prime.
\item If every prime ideal of $R$ is principal, then
every ideal of $R$ is principal.
\end{enumerate}
\end{lemma}

\begin{proof}
The first part follows from
Example \ref{example-oka-family-principal} and
Proposition \ref{proposition-oka}.
For the second, suppose that there exists an ideal $I \subset R$
which is not principal. The union of a totally ordered chain
$\left\{I_\alpha\right\}$ of ideals that not principal is not principal;
indeed, if $I = \bigcup I_\alpha$ were generated by
$a$, then $a$ would belong to some $I_\alpha $ and $a$ would generate it.
By Zorn's lemma, there is an ideal maximal with respect to not being
principal. This ideal is necessarily prime by the first part.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-primes-principal}
Soit $R$ un anneau.
\begin{enumerate}
\item Un idéal $I \subset R$ maximal parmi ceux qui ne sont pas
principaux est premier.
\item Si tout idéal premier de $R$ est principal, alors
tout idéal de $R$ est principal.
\end{enumerate}
\end{lemma}

\begin{proof}
La première partie résulte de
l'exemple \ref{example-oka-family-principal} et de la
proposition \ref{proposition-oka}.
Pour la seconde, supposons qu'il existe un idéal $I \subset R$
qui ne soit pas principal. La réunion d'une chaîne totalement ordonnée
$\left\{I_\alpha\right\}$ d'idéaux qui ne sont pas principaux n'est pas principale ;
en effet, si $I = \bigcup I_\alpha$ était engendré par
$a$, alors $a$ appartiendrait à un certain $I_\alpha $ et $a$ l'engendrerait.
D'après le lemme de Zorn, il existe un idéal maximal parmi ceux qui ne sont pas
principaux. Cet idéal est nécessairement premier d'après la première partie.
\end{proof}
```

</details>

### 13 — lemma-characterize-domain

Anglais L5288–5307 ; français L5268–5287.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5288) · FR-ALGEBRA-B8-CHOICE-0013.

Non diviseur de zéro est conservé plutôt que régulier sans définition ; anneau intègre traduit domain. Dans la seconde assertion, R est non nul et l'hypothèse porte sur tout idéal premier non nul. Ces deux occurrences de non nul ne sont pas des ajouts éditoriaux. La preuve utilise la partie multiplicative des non-diviseurs ; elle n'exige pas qu'un tel élément soit inversible.

Règles : FR-ALGEBRA-B8-RULE-IDEAL, FR-ALGEBRA-B8-RULE-MAXIMALITE, FR-ALGEBRA-B8-RULE-INTEGRE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-domain}
Let $R$ be a ring.
\begin{enumerate}
\item An ideal maximal among the ideals which do not contain a
nonzerodivisor is prime.
\item If $R$ is nonzero and every nonzero prime ideal in $R$
contains a nonzerodivisor, then $R$ is a domain.
\end{enumerate}
\end{lemma}

\begin{proof}
Consider the set $S$ of nonzerodivisors. It is a multiplicative
subset of $R$. Hence any ideal maximal with respect to not intersecting
$S$ is prime, see
Lemma \ref{lemma-simple}.
Thus, if every nonzero prime ideal contains a nonzerodivisor, then
$(0)$ is prime, i.e., $R$ is a domain.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-characterize-domain}
Soit $R$ un anneau.
\begin{enumerate}
\item Un idéal maximal parmi les idéaux qui ne contiennent aucun
élément non diviseur de zéro est premier.
\item Si $R$ est non nul et si tout idéal premier non nul de $R$
contient un élément non diviseur de zéro, alors $R$ est un anneau intègre.
\end{enumerate}
\end{lemma}

\begin{proof}
Considérons l'ensemble $S$ des éléments non diviseurs de zéro. C'est une partie
multiplicative de $R$. Ainsi, tout idéal maximal parmi ceux qui ne rencontrent pas
$S$ est premier, voir le
lemme \ref{lemma-simple}.
Par conséquent, si tout idéal premier non nul contient un élément non diviseur de zéro, alors
$(0)$ est premier, c'est-à-dire que $R$ est un anneau intègre.
\end{proof}
```

</details>

### 14 — remark-cohen-bound-cardinality

Anglais L5308–5328 ; français L5288–5308.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5308) · FR-ALGEBRA-B8-CHOICE-0014.

La distinction entre existence d'idéaux maximaux exclus et génération de tous les idéaux est maintenue. La borne dénombrable pour les premiers ne devient pas une borne pour tous les idéaux. Les deux familles de variables, leurs plages d'indices et les relations sont inchangées. L'idéal unique premier est (xn) ; les z y appartiennent via la relation à l'indice suivant. Le mot local ne signifie pas corps.

Point particulier à relire : La relation mixte est interprétée pour n au moins 1, puisque z(t,n−1) apparaît ; la formule de source ne réénonce pas cette borne dans la liste des relations. Aucune nouvelle borne n'est insérée.

Règles : FR-ALGEBRA-B8-RULE-IDEAL, FR-ALGEBRA-B8-RULE-MAXIMALITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{remark}
\label{remark-cohen-bound-cardinality}
Let $R$ be a ring. Let $\kappa$ be an infinite cardinal.
By applying
Example \ref{example-oka-family-bound-cardinality} and
Proposition \ref{proposition-oka}
we see that any ideal maximal with respect to the property of not being
generated by $\kappa$ elements is prime. This result is not so
useful because there exists a ring for which every prime ideal
of $R$ can be generated by $\aleph_0$ elements, but some
ideal cannot. Namely, let $k$ be a field, let $T$ be a set whose
cardinality is greater than $\aleph_0$ and let
$$
R = k[\{x_n\}_{n \geq 1}, \{z_{t, n}\}_{t \in T, n \geq 0}]/
(x_n^2, z_{t, n}^2, x_n z_{t, n} - z_{t, n - 1})
$$
This is a local ring with unique prime ideal
$\mathfrak m = (x_n)$. But the ideal $(z_{t, n})$ cannot
be generated by countably many elements.
\end{remark}
```

Français restauré :
```tex
\begin{remark}
\label{remark-cohen-bound-cardinality}
Soit $R$ un anneau. Soit $\kappa$ un cardinal infini.
En appliquant
l'exemple \ref{example-oka-family-bound-cardinality} et la
proposition \ref{proposition-oka},
nous voyons que tout idéal maximal parmi ceux qui ne peuvent pas être
engendrés par $\kappa$ éléments est premier. Ce résultat n'est pas très
utile, car il existe un anneau $R$ dont tout idéal premier
peut être engendré par $\aleph_0$ éléments, mais dont un certain
idéal ne le peut pas. En effet, soit $k$ un corps, soit $T$ un ensemble dont
la cardinalité est strictement supérieure à $\aleph_0$, et posons
$$
R = k[\{x_n\}_{n \geq 1}, \{z_{t, n}\}_{t \in T, n \geq 0}]/
(x_n^2, z_{t, n}^2, x_n z_{t, n} - z_{t, n - 1})
$$
C'est un anneau local dont l'unique idéal premier est
$\mathfrak m = (x_n)$. Mais l'idéal $(z_{t, n})$ ne peut pas
être engendré par une famille dénombrable d'éléments.
\end{remark}
```

</details>

### 15 — example-noetherian-topology-on-spec

Anglais L5329–5370 ; français L5309–5350.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5329) · FR-ALGEBRA-B8-CHOICE-0015.

La référence nominative et sa date restent des données de source. ACC devient condition de chaîne ascendante ; radical ideas est rendu par idéaux radicaux, correction linguistique sans changement d'objet. Espace topologique noethérien n'est pas identifié à anneau noethérien. La famille concerne des radicaux d'idéaux de type fini, et les exposants peuvent être uniformisés parce que les fi sont en nombre fini. Les mots for some et and dans la formule sont traduits exactement, avec exception explicite au contrôle des formules. La promesse finale de l'auteur est traduite, non exécutée.

Point particulier à relire : La dernière promesse d'énoncer et démontrer plus tard appartient au texte officiel. Elle ne demande pas à ce travail de compléter la preuve.

Règles : FR-ALGEBRA-B8-RULE-OKA, FR-ALGEBRA-B8-RULE-IDEAL, FR-ALGEBRA-B8-RULE-NOETHERIEN, FR-ALGEBRA-B8-RULE-EXACT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-noetherian-topology-on-spec}
\begin{reference}
Comment by Lukas Heger of November 12, 2020.
\end{reference}
Let $R$ be a ring and $X = \Spec(R)$. Since closed subsets of $X$ correspond to
radical ideas of $R$ (Lemma \ref{lemma-Zariski-topology}) we see that $X$ is a
Noetherian topological space if and only if we have ACC for radical ideals.
This holds if and only if every radical ideal is the radical of a finitely
generated ideal (details omitted). Let
$$
\mathcal{F} = \{I \subset R \mid
\sqrt{I} = \sqrt{(f_1, \ldots, f_n)}\text{ for some }n
\text{ and }f_1, \ldots, f_n \in R\}.
$$
The reader can show that $\mathcal{F}$ is an Oka family by using the identity
$$
\sqrt{I} = \sqrt{(I, a)(I : a)}
$$
which holds for any ideal $I \subset R$ and any element $a \in R$.
On the other hand, if we have a totally ordered chain of ideals
$\{I_\alpha\}$ none of which are in $\mathcal{F}$, then the union
$I = \bigcup I_\alpha$ cannot be in $\mathcal{F}$ either. Otherwise
$\sqrt{I} = \sqrt{(f_1, \ldots, f_n)}$, then $f_i^e \in I$ for some $e$,
then $f_i^e \in I_\alpha$ for some $\alpha$ independent of $i$, then
$\sqrt{I_\alpha} = \sqrt{(f_1, \ldots, f_n)}$, contradiction.
Thus if the set of ideals not in $\mathcal{F}$ is nonempty, then it
has maximal elements and
exactly as in Lemma \ref{lemma-cohen} we conclude that $X$ is a
Noetherian topological space if and only if every prime ideal of $R$
is equal to $\sqrt{(f_1, \ldots, f_n)}$ for some $f_1, \ldots, f_n \in R$.
If we ever need this result we will carefully state and prove this
result here.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-noetherian-topology-on-spec}
\begin{reference}
Commentaire de Lukas Heger du 12 novembre 2020.
\end{reference}
Soient $R$ un anneau et $X = \Spec(R)$. Puisque les fermés de $X$ correspondent aux
idéaux radicaux de $R$ (lemme \ref{lemma-Zariski-topology}), nous voyons que $X$ est un
espace topologique noethérien si et seulement si les idéaux radicaux vérifient la condition de chaîne ascendante.
Cela équivaut à dire que tout idéal radical est le radical d'un idéal de type
fini (détails omis). Posons
$$
\mathcal{F} = \{I \subset R \mid
\sqrt{I} = \sqrt{(f_1, \ldots, f_n)}\text{ pour un certain }n
\text{ et }f_1, \ldots, f_n \in R\}.
$$
Le lecteur peut montrer que $\mathcal{F}$ est une famille d'Oka en utilisant l'identité
$$
\sqrt{I} = \sqrt{(I, a)(I : a)}
$$
qui vaut pour tout idéal $I \subset R$ et tout élément $a \in R$.
D'autre part, si nous avons une chaîne totalement ordonnée d'idéaux
$\{I_\alpha\}$ dont aucun n'appartient à $\mathcal{F}$, alors la réunion
$I = \bigcup I_\alpha$ ne peut pas non plus appartenir à $\mathcal{F}$. Sinon,
$\sqrt{I} = \sqrt{(f_1, \ldots, f_n)}$, puis $f_i^e \in I$ pour un certain $e$,
puis $f_i^e \in I_\alpha$ pour un certain $\alpha$ indépendant de $i$, et enfin
$\sqrt{I_\alpha} = \sqrt{(f_1, \ldots, f_n)}$, contradiction.
Ainsi, si l'ensemble des idéaux qui n'appartiennent pas à $\mathcal{F}$ est non vide, il
possède des éléments maximaux et,
exactement comme dans le lemme \ref{lemma-cohen}, nous concluons que $X$ est un
espace topologique noethérien si et seulement si tout idéal premier de $R$
est égal à $\sqrt{(f_1, \ldots, f_n)}$ pour certains $f_1, \ldots, f_n \in R$.
Si ce résultat nous est un jour nécessaire, nous l'énoncerons et le démontrerons
ici avec soin.
\end{example}
```

</details>

### 16 — section-images-finite-presentation

Anglais L5371–5381 ; français L5351–5361.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5371) · FR-ALGEBRA-B8-CHOICE-0016.

Morphismes d'anneaux de présentation finie, parties constructibles et théorème de Chevalley sont directement attestés chez Dat 1.2.8, p.11–13, dans le même cadre non nécessairement noethérien. Les définitions citées dans Topology ont également été lues. Rétrocompact n'est pas assimilé à quasi-compact dans un espace arbitraire ; leur équivalence pour les ouverts de Spec(R) est précisément le lemme suivant.

Règles : FR-ALGEBRA-B8-RULE-FINITUDE, FR-ALGEBRA-B8-RULE-CONSTRUCTIBLE, FR-ALGEBRA-B8-RULE-QUASICOMPACT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Images of ring maps of finite presentation}
\label{section-images-finite-presentation}

\noindent
In this section we prove some results on the
topology of maps $\Spec(S) \to \Spec(R)$
induced by ring maps $R \to S$, mainly Chevalley's Theorem.
In order to do this we will use the notions of constructible sets,
quasi-compact sets, retrocompact sets, and so on
which are defined in Topology, Section \ref{topology-section-constructible}.
```

Français restauré :
```tex
\section{Images des morphismes d'anneaux de présentation finie}
\label{section-images-finite-presentation}

\noindent
Dans cette section, nous démontrons quelques résultats sur la
topologie des applications $\Spec(S) \to \Spec(R)$
induites par des morphismes d'anneaux $R \to S$, principalement le théorème de Chevalley.
Pour ce faire, nous utiliserons les notions de parties constructibles,
de parties quasi-compactes, de parties rétrocompactes, etc.,
qui sont définies dans Topologie, section \ref{topology-section-constructible}.
```

</details>

### 17 — lemma-qc-open

Anglais L5382–5413 ; français L5362–5393.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5382) · FR-ALGEBRA-B8-CHOICE-0017.

Les quatre conditions, les quatre implications et la réunion finie d'intersections D(fi gj) sont conservées. Ouvert principal rend standard open, comme chez Dat 1.2.8. Rétrocompact signifie que l'inclusion est quasi-compacte, selon la définition officielle effectivement lue. Le symbole X non introduit dans la quatrième condition reste littéral : il est signalé à part, non remplacé par Spec(R).

Point particulier à relire : X n'est pas introduit dans l'énoncé. Le contexte désigne Spec(R) ; la formule X reste néanmoins préservée dans la traduction fidèle.

Règles : FR-ALGEBRA-B8-RULE-FINITUDE, FR-ALGEBRA-B8-RULE-QUASICOMPACT, FR-ALGEBRA-B8-RULE-OPEN.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-qc-open}
Let $U \subset \Spec(R)$ be open. The following
are equivalent:
\begin{enumerate}
\item $U$ is retrocompact in $\Spec(R)$,
\item $U$ is quasi-compact,
\item $U$ is a finite union of standard opens, and
\item there exists a finitely generated ideal $I \subset R$ such
that $X \setminus V(I) = U$.
\end{enumerate}
\end{lemma}

\begin{proof}
We have (1) $\Rightarrow$ (2) because $\Spec(R)$ is quasi-compact, see
Lemma \ref{lemma-quasi-compact}. We have (2) $\Rightarrow$ (3) because
standard opens form a basis for the topology. Proof of (3) $\Rightarrow$ (1).
Let $U = \bigcup_{i = 1\ldots n} D(f_i)$. To show that $U$ is retrocompact
in $\Spec(R)$ it suffices to show that $U \cap V$ is quasi-compact for any
quasi-compact open $V$ of $\Spec(R)$. Write
$V = \bigcup_{j = 1\ldots m} D(g_j)$ which is possible by (2) $\Rightarrow$
(3). Each standard open is homeomorphic to the spectrum of a ring and hence
quasi-compact, see Lemmas \ref{lemma-standard-open} and
\ref{lemma-quasi-compact}. Thus
$U \cap V =
(\bigcup_{i = 1\ldots n} D(f_i)) \cap (\bigcup_{j = 1\ldots m} D(g_j))
= \bigcup_{i, j} D(f_i g_j)$ is a finite union of quasi-compact opens
hence quasi-compact. To finish the proof note
that (4) is equivalent to (3) by 
Lemma \ref{lemma-Zariski-topology}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-qc-open}
Soit $U \subset \Spec(R)$ un ouvert. Les conditions suivantes
sont équivalentes :
\begin{enumerate}
\item $U$ est rétrocompact dans $\Spec(R)$,
\item $U$ est quasi-compact,
\item $U$ est une réunion finie d'ouverts principaux, et
\item il existe un idéal de type fini $I \subset R$ tel
que $X \setminus V(I) = U$.
\end{enumerate}
\end{lemma}

\begin{proof}
Nous avons (1) $\Rightarrow$ (2), car $\Spec(R)$ est quasi-compact, voir le
lemme \ref{lemma-quasi-compact}. Nous avons (2) $\Rightarrow$ (3), car les
ouverts principaux forment une base de la topologie. Démontrons (3) $\Rightarrow$ (1).
Soit $U = \bigcup_{i = 1\ldots n} D(f_i)$. Pour montrer que $U$ est rétrocompact
dans $\Spec(R)$, il suffit de montrer que $U \cap V$ est quasi-compact pour tout
ouvert quasi-compact $V$ de $\Spec(R)$. Écrivons
$V = \bigcup_{j = 1\ldots m} D(g_j)$, ce qui est possible par (2) $\Rightarrow$
(3). Tout ouvert principal est homéomorphe au spectre d'un anneau et est donc
quasi-compact, voir les lemmes \ref{lemma-standard-open} et
\ref{lemma-quasi-compact}. Ainsi,
$U \cap V =
(\bigcup_{i = 1\ldots n} D(f_i)) \cap (\bigcup_{j = 1\ldots m} D(g_j))
= \bigcup_{i, j} D(f_i g_j)$ est une réunion finie d'ouverts quasi-compacts,
donc est quasi-compact. Pour achever la démonstration, notons
que (4) équivaut à (3) d'après le
lemme \ref{lemma-Zariski-topology}.
\end{proof}
```

</details>

### 18 — lemma-affine-map-quasi-compact

Anglais L5414–5432 ; français L5394–5412.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5414) · FR-ALGEBRA-B8-CHOICE-0018.

Quasi-compact qualifie l'application continue induite, et image réciproque traduit inverse image. Le résultat vaut pour un morphisme d'anneaux quelconque ; aucune présentation finie n'est ajoutée. La faute anglaise finite open of standard opens est rendue par réunion finie d'ouverts principaux, dont le sens est confirmé par les deux phrases adjacentes. Il ne s'agit pas de corriger un argument mathématique ni de confondre image directe et image réciproque.

Règles : FR-ALGEBRA-B8-RULE-CONSTRUCTIBLE, FR-ALGEBRA-B8-RULE-QUASICOMPACT, FR-ALGEBRA-B8-RULE-OPEN, FR-ALGEBRA-B8-RULE-IMAGE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-affine-map-quasi-compact}
Let $\varphi : R \to S$ be a ring map.
The induced continuous map $f : \Spec(S) \to \Spec(R)$
is quasi-compact. For any constructible set $E \subset \Spec(R)$
the inverse image $f^{-1}(E)$ is constructible in $\Spec(S)$.
\end{lemma}

\begin{proof}
We first show that the inverse image of any quasi-compact
open $U \subset \Spec(R)$ is quasi-compact. By
Lemma \ref{lemma-qc-open} we may write $U$ as a finite
open of standard opens. Thus by Lemma \ref{lemma-spec-functorial}
we see that $f^{-1}(U)$ is a finite union of standard opens.
Hence $f^{-1}(U)$ is quasi-compact by Lemma \ref{lemma-qc-open} again.
The second assertion now follows from Topology, Lemma
\ref{topology-lemma-inverse-images-constructibles}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-affine-map-quasi-compact}
Soit $\varphi : R \to S$ un morphisme d'anneaux.
L'application continue induite $f : \Spec(S) \to \Spec(R)$
est quasi-compacte. Pour toute partie constructible $E \subset \Spec(R)$,
l'image réciproque $f^{-1}(E)$ est constructible dans $\Spec(S)$.
\end{lemma}

\begin{proof}
Montrons d'abord que l'image réciproque de tout ouvert quasi-compact
$U \subset \Spec(R)$ est quasi-compacte. D'après le
lemme \ref{lemma-qc-open}, nous pouvons écrire $U$ comme une réunion
finie d'ouverts principaux. Le lemme \ref{lemma-spec-functorial}
montre donc que $f^{-1}(U)$ est une réunion finie d'ouverts principaux.
Ainsi, $f^{-1}(U)$ est quasi-compact d'après le lemme \ref{lemma-qc-open}.
La seconde assertion résulte alors de Topologie, lemme
\ref{topology-lemma-inverse-images-constructibles}.
\end{proof}
```

</details>

### 19 — lemma-constructible

Anglais L5433–5452 ; français L5413–5432.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5433) · FR-ALGEBRA-B8-CHOICE-0019.

Réunion finie de D(f) intersection V(g1,...,gm) garde la finitude des équations aussi bien que celle de la réunion. Dat p.11 donne exactement cette définition sur le spectre d'un anneau arbitraire. Les ouverts rétrocompacts et les complémentaires restent ceux de la définition officielle de Topology. On n'importe pas une définition par seuls localement fermés qui serait insuffisante hors du cadre noethérien.

Règles : FR-ALGEBRA-B8-RULE-MAXIMALITE, FR-ALGEBRA-B8-RULE-CONSTRUCTIBLE, FR-ALGEBRA-B8-RULE-QUASICOMPACT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-constructible}
Let $R$ be a ring. A subset of $\Spec(R)$ is constructible if and only
if it can be written as a finite union of subsets of the form
$D(f) \cap V(g_1, \ldots, g_m)$ for $f, g_1, \ldots, g_m \in R$.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-qc-open} the subset $D(f)$ and the complement of
$V(g_1, \ldots, g_m)$ are retro-compact open. Hence
$D(f) \cap V(g_1, \ldots, g_m)$ is a constructible subset and so is
any finite union of such. Conversely, let $T \subset \Spec(R)$ be
constructible. By Topology, Definition \ref{topology-definition-constructible},
we may assume that $T = U \cap V^c$, where $U, V \subset \Spec(R)$
are retrocompact open. By Lemma \ref{lemma-qc-open} we may write
$U = \bigcup_{i = 1, \ldots, n} D(f_i)$ and
$V = \bigcup_{j = 1, \ldots, m} D(g_j)$. Then
$T = \bigcup_{i = 1, \ldots, n} \big(D(f_i) \cap V(g_1, \ldots, g_m)\big)$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-constructible}
Soit $R$ un anneau. Une partie de $\Spec(R)$ est constructible si et seulement
si elle peut s'écrire comme une réunion finie de parties de la forme
$D(f) \cap V(g_1, \ldots, g_m)$, où $f, g_1, \ldots, g_m \in R$.
\end{lemma}

\begin{proof}
D'après le lemme \ref{lemma-qc-open}, la partie $D(f)$ et le complémentaire de
$V(g_1, \ldots, g_m)$ sont des ouverts rétrocompacts. Ainsi,
$D(f) \cap V(g_1, \ldots, g_m)$ est une partie constructible, de même que
toute réunion finie de telles parties. Réciproquement, soit $T \subset \Spec(R)$ une
partie constructible. D'après Topologie, définition \ref{topology-definition-constructible},
nous pouvons supposer que $T = U \cap V^c$, où $U, V \subset \Spec(R)$
sont des ouverts rétrocompacts. D'après le lemme \ref{lemma-qc-open}, nous pouvons écrire
$U = \bigcup_{i = 1, \ldots, n} D(f_i)$ et
$V = \bigcup_{j = 1, \ldots, m} D(g_j)$. Alors
$T = \bigcup_{i = 1, \ldots, n} \big(D(f_i) \cap V(g_1, \ldots, g_m)\big)$.
\end{proof}
```

</details>

### 20 — lemma-constructible-is-image

Anglais L5453–5473 ; français L5433–5453.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5453) · FR-ALGEBRA-B8-CHOICE-0020.

La construction par produit fini d'anneaux représente une réunion d'images ; le produit donne une réunion disjointe des spectres, pas nécessairement une partition disjointe de T. Dat p.11 traite explicitement cette représentation par un morphisme de présentation finie. Le quotient par l'idéal de type fini puis la localisation en f sont conservés, ainsi que les deux références officielles.

Règles : FR-ALGEBRA-B8-RULE-CONSTRUCTIBLE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-constructible-is-image}
Let $R$ be a ring and let $T \subset \Spec(R)$
be constructible. Then there exists a ring map $R \to S$ of
finite presentation such that $T$ is the image of
$\Spec(S)$ in $\Spec(R)$.
\end{lemma}

\begin{proof}
The spectrum of a finite product of rings
is the disjoint union of the spectra, see
Lemma \ref{lemma-spec-product}. Hence if $T = T_1 \cup T_2$
and the result holds for $T_1$ and $T_2$, then the
result holds for $T$.
By Lemma \ref{lemma-constructible} we may assume
that $T = D(f) \cap V(g_1, \ldots, g_m)$.
In this case $T$ is the image of the map
$\Spec((R/(g_1, \ldots, g_m))_f) \to \Spec(R)$, see Lemmas
\ref{lemma-standard-open} and \ref{lemma-spec-closed}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-constructible-is-image}
Soit $R$ un anneau et soit $T \subset \Spec(R)$
une partie constructible. Il existe alors un morphisme d'anneaux $R \to S$ de
présentation finie tel que $T$ soit l'image de
$\Spec(S)$ dans $\Spec(R)$.
\end{lemma}

\begin{proof}
Le spectre d'un produit fini d'anneaux
est la réunion disjointe des spectres, voir le
lemme \ref{lemma-spec-product}. Par conséquent, si $T = T_1 \cup T_2$
et si le résultat vaut pour $T_1$ et $T_2$, alors il
vaut pour $T$.
D'après le lemme \ref{lemma-constructible}, nous pouvons supposer
que $T = D(f) \cap V(g_1, \ldots, g_m)$.
Dans ce cas, $T$ est l'image du morphisme
$\Spec((R/(g_1, \ldots, g_m))_f) \to \Spec(R)$, voir les lemmes
\ref{lemma-standard-open} et \ref{lemma-spec-closed}.
\end{proof}
```

</details>

### 21 — lemma-open-fp

Anglais L5474–5494 ; français L5454–5474.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5474) · FR-ALGEBRA-B8-CHOICE-0021.

Le morphisme est la localisation en un seul élément, non une immersion ouverte arbitraire sans condition de quasi-compacité. Sous Spec(Rf)=D(f), les ouverts U et V restent quasi-compacts dans l'espace ambiant. Les complémentaires sont pris dans les espaces appropriés ; U' contenu dans D(f) justifie la formule finale. Présentation finie et constructible gardent le sens attesté chez Dat.

Règles : FR-ALGEBRA-B8-RULE-CONSTRUCTIBLE, FR-ALGEBRA-B8-RULE-QUASICOMPACT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-open-fp}
Let $R$ be a ring.
Let $f$ be an element of $R$.
Let $S = R_f$.
Then the image of a constructible subset of $\Spec(S)$
is constructible in $\Spec(R)$.
\end{lemma}

\begin{proof}
We repeatedly use Lemma \ref{lemma-qc-open} without mention.
Let $U, V$ be quasi-compact open in $\Spec(S)$.
We will show that the image of $U \cap V^c$ is constructible.
Under the identification
$\Spec(S) = D(f)$ of Lemma \ref{lemma-standard-open}
the sets $U, V$ correspond to quasi-compact opens
$U', V'$ of $\Spec(R)$.
Hence it suffices to show that $U' \cap (V')^c$
is constructible in $\Spec(R)$ which is clear.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-open-fp}
Soit $R$ un anneau.
Soit $f$ un élément de $R$.
Soit $S = R_f$.
Alors l'image d'une partie constructible de $\Spec(S)$
est constructible dans $\Spec(R)$.
\end{lemma}

\begin{proof}
Nous utilisons à plusieurs reprises le lemme \ref{lemma-qc-open} sans le mentionner.
Soient $U, V$ des ouverts quasi-compacts de $\Spec(S)$.
Nous allons montrer que l'image de $U \cap V^c$ est constructible.
Sous l'identification
$\Spec(S) = D(f)$ du lemme \ref{lemma-standard-open},
les parties $U, V$ correspondent à des ouverts quasi-compacts
$U', V'$ de $\Spec(R)$.
Il suffit donc de montrer que $U' \cap (V')^c$
est constructible dans $\Spec(R)$, ce qui est clair.
\end{proof}
```

</details>

### 22 — lemma-closed-fp

Anglais L5495–5523 ; français L5475–5503.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5495) · FR-ALGEBRA-B8-CHOICE-0022.

L'idéal I est de type fini : cette hypothèse est conservée et ne devient pas seulement un idéal quelconque. Les barres désignent les images dans R/I, tandis que U et V sont des ouverts de Spec(R). Les images directes et le complémentaire final sont distingués. Dat p.12 confirme le même vocabulaire pour le quotient de noyau de type fini, sans remplacer la preuve de Stacks par sa démonstration.

Règles : FR-ALGEBRA-B8-RULE-MAXIMALITE, FR-ALGEBRA-B8-RULE-FINITUDE, FR-ALGEBRA-B8-RULE-CONSTRUCTIBLE, FR-ALGEBRA-B8-RULE-QUASICOMPACT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-closed-fp}
Let $R$ be a ring.
Let $I$ be a finitely generated ideal of $R$.
Let $S = R/I$.
Then the image of a constructible subset of $\Spec(S)$
is constructible in $\Spec(R)$.
\end{lemma}

\begin{proof}
If $I = (f_1, \ldots, f_m)$, then we see that
$V(I)$ is the complement of $\bigcup D(f_i)$,
see Lemma \ref{lemma-Zariski-topology}.
Hence it is constructible, by Lemma \ref{lemma-qc-open}.
Denote the map $R \to S$ by $f \mapsto \overline{f}$.
We have to show that if $\overline{U}, \overline{V}$
are retrocompact opens of $\Spec(S)$, then the
image of $\overline{U} \cap \overline{V}^c$
in $\Spec(R)$ is constructible.
By Lemma \ref{lemma-qc-open} we may write
$\overline{U} = \bigcup D(\overline{g_i})$.
Setting $U = \bigcup D({g_i})$ we see $\overline{U}$
has image $U \cap V(I)$ which is constructible in
$\Spec(R)$. Similarly the image of $\overline{V}$ equals
$V \cap V(I)$ for some retrocompact open $V$ of $\Spec(R)$.
Hence the image of $\overline{U} \cap \overline{V}^c$
equals $U \cap V(I) \cap V^c$ as desired.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-closed-fp}
Soit $R$ un anneau.
Soit $I$ un idéal de type fini de $R$.
Soit $S = R/I$.
Alors l'image d'une partie constructible de $\Spec(S)$
est constructible dans $\Spec(R)$.
\end{lemma}

\begin{proof}
Si $I = (f_1, \ldots, f_m)$, alors nous voyons que
$V(I)$ est le complémentaire de $\bigcup D(f_i)$,
voir le lemme \ref{lemma-Zariski-topology}.
Il est donc constructible, d'après le lemme \ref{lemma-qc-open}.
Notons le morphisme $R \to S$ par $f \mapsto \overline{f}$.
Nous devons montrer que, si $\overline{U}, \overline{V}$
sont des ouverts rétrocompacts de $\Spec(S)$, alors l'image de
$\overline{U} \cap \overline{V}^c$
dans $\Spec(R)$ est constructible.
D'après le lemme \ref{lemma-qc-open}, nous pouvons écrire
$\overline{U} = \bigcup D(\overline{g_i})$.
En posant $U = \bigcup D({g_i})$, nous voyons que $\overline{U}$
a pour image $U \cap V(I)$, qui est constructible dans
$\Spec(R)$. De même, l'image de $\overline{V}$ est égale à
$V \cap V(I)$ pour un certain ouvert rétrocompact $V$ de $\Spec(R)$.
Ainsi, l'image de $\overline{U} \cap \overline{V}^c$
est égale à $U \cap V(I) \cap V^c$, comme voulu.
\end{proof}
```

</details>

### 23 — lemma-affineline-open

Anglais L5524–5553 ; français L5504–5533.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5524) · FR-ALGEBRA-B8-CHOICE-0023.

Ouvert qualifie le morphisme topologique ; l'image de chaque ouvert principal est seulement un ouvert quasi-compact, pas forcément principal. Le critère sur la fibre donne la réunion des D(ai) des coefficients. Le passage non nul se rapporte à l'anneau de la fibre localisée, puis au polynôme sur le corps résiduel. La preuve de Dat p.12 fournit la même lecture et le même registre.

Règles : FR-ALGEBRA-B8-RULE-IDEAL, FR-ALGEBRA-B8-RULE-QUASICOMPACT, FR-ALGEBRA-B8-RULE-POLYNOME, FR-ALGEBRA-B8-RULE-EXACT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-affineline-open}
Let $R$ be a ring. The map $\Spec(R[x]) \to \Spec(R)$
is open, and the image of any standard open is a quasi-compact
open.
\end{lemma}

\begin{proof}
It suffices to show that the image of a standard open
$D(f)$, $f\in R[x]$ is quasi-compact open.
The image of $D(f)$ is the image of
$\Spec(R[x]_f) \to \Spec(R)$.
Let $\mathfrak p \subset R$ be a prime ideal.
Let $\overline{f}$ be the image of $f$ in
$\kappa(\mathfrak p)[x]$.
Recall, see Lemma \ref{lemma-in-image},
that $\mathfrak p$ is in the image
if and only if $R[x]_f \otimes_R \kappa(\mathfrak p) =
\kappa(\mathfrak p)[x]_{\overline{f}}$ is not the
zero ring. This is exactly the condition that $f$ does not map
to zero in $\kappa(\mathfrak p)[x]$, in other words, that
some coefficient of $f$ is not in $\mathfrak p$.
Hence we see: if $f = a_d x^d + \ldots + a_0$, then
the image of $D(f)$ is $D(a_d) \cup \ldots \cup D(a_0)$.
\end{proof}

\noindent
We prove a property of characteristic polynomials which
will be used below.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-affineline-open}
Soit $R$ un anneau. Le morphisme $\Spec(R[x]) \to \Spec(R)$
est ouvert, et l'image de tout ouvert principal est un ouvert
quasi-compact.
\end{lemma}

\begin{proof}
Il suffit de montrer que l'image d'un ouvert principal
$D(f)$, $f\in R[x]$, est un ouvert quasi-compact.
L'image de $D(f)$ est celle du morphisme
$\Spec(R[x]_f) \to \Spec(R)$.
Soit $\mathfrak p \subset R$ un idéal premier.
Soit $\overline{f}$ l'image de $f$ dans
$\kappa(\mathfrak p)[x]$.
Rappelons, voir le lemme \ref{lemma-in-image},
que $\mathfrak p$ appartient à l'image
si et seulement si $R[x]_f \otimes_R \kappa(\mathfrak p) =
\kappa(\mathfrak p)[x]_{\overline{f}}$ n'est pas l'anneau
nul. C'est exactement la condition que $f$ ne s'envoie pas
sur zéro dans $\kappa(\mathfrak p)[x]$, autrement dit qu'un
coefficient de $f$ n'appartienne pas à $\mathfrak p$.
Ainsi, si $f = a_d x^d + \ldots + a_0$, alors
l'image de $D(f)$ est $D(a_d) \cup \ldots \cup D(a_0)$.
\end{proof}

\noindent
Nous démontrons une propriété des polynômes caractéristiques qui
sera utilisée ci-dessous.
```

</details>

### 24 — lemma-characteristic-polynomial-prime

Anglais L5554–5596 ; français L5534–5576.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5554) · FR-ALGEBRA-B8-CHOICE-0024.

La finitude libre est une propriété de A comme R-module, non l'affirmation que A est une algèbre polynomiale libre. La matrice, le changement de corps résiduel, les coefficients et le critère de nilpotence sont conservés. Une réparation mathématique française a été retirée : dans cette algèbre sur κ(p) redevient considérée dans κ(p), comme l'anglais. Cette fidélité conserve un objet ambiant erroné, explicitement expliqué dans le dossier séparé. Dat p.13 atteste polynôme caractéristique de la multiplication et place correctement l'élément dans l'algèbre tensorisée ; il n'autorise pas à modifier le témoin officiel.

Point particulier à relire : Pour R=k, A=k[ε]/(ε²) et f=ε, l'élément f⊗1 appartient à A⊗k k, mais n'est pas un scalaire de k. La correction ambiante est justifiée mathématiquement et conservée seulement dans le dossier, pas appliquée au français officiel.

Règles : FR-ALGEBRA-B8-RULE-IDEAL, FR-ALGEBRA-B8-RULE-POLYNOME, FR-ALGEBRA-B8-RULE-NILPOTENT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characteristic-polynomial-prime}
Let $R \to A$ be a ring homomorphism.
Assume $A \cong R^{\oplus n}$ as an $R$-module.
Let $f \in A$. The multiplication map $m_f: A
\to A$ is $R$-linear and hence
has a characteristic polynomial
$P(T) = T^n + r_{n-1}T^{n-1} + \ldots + r_0 \in R[T]$.
For any prime
$\mathfrak{p} \in \Spec(R)$, $f$ acts nilpotently on $A
\otimes_R \kappa(\mathfrak{p})$ if and only if $\mathfrak p \in
V(r_0, \ldots, r_{n-1})$.
\end{lemma}

\begin{proof}
This follows quite easily once we prove that the characteristic
polynomial $\bar P(T) \in \kappa(\mathfrak p)[T]$ of the
multiplication map $m_{\bar f}: A \otimes_R \kappa(\mathfrak p) \to
A \otimes_R \kappa(\mathfrak p)$ which multiplies elements of $A
\otimes_R \kappa(\mathfrak p)$ by $\bar f$, the image of $f$ viewed in
$\kappa(\mathfrak p)$, is just the image of $P(T)$ in
$\kappa(\mathfrak p)[T]$. Let $(a_{ij})$ be the matrix of the map
$m_f$ with entries in $R$, using a basis $e_1, \ldots, e_n$
of $A$ as an $R$-module.
Then, $A \otimes_R \kappa(\mathfrak p) \cong (R \otimes_R
\kappa(\mathfrak p))^{\oplus n} = \kappa(\mathfrak p)^n$, which is
an $n$-dimensional vector space over $\kappa(\mathfrak p)$ with
basis $e_1 \otimes 1, \ldots, e_n \otimes 1$. The image $\bar f = f
\otimes 1$, and so the multiplication map $m_{\bar f}$ has matrix
$(a_{ij} \otimes 1)$. Thus, the characteristic polynomial is
precisely the image of $P(T)$.

\medskip\noindent
From linear algebra, we know that a linear transformation acts
nilpotently on an $n$-dimensional vector space if and only if the
characteristic polynomial is $T^n$ (since the characteristic
polynomial divides some power of the minimal polynomial). Hence,
$f$ acts nilpotently on $A \otimes_R \kappa(\mathfrak p)$ if and
only if $\bar P(T) = T^n$. This occurs if and only if $r_i \in
\mathfrak p$ for all $0 \leq i \leq n - 1$, that is when $\mathfrak p \in
V(r_0, \ldots, r_{n - 1}).$
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-characteristic-polynomial-prime}
Soit $R \to A$ un morphisme d'anneaux.
Supposons que $A \cong R^{\oplus n}$ comme $R$-module.
Soit $f \in A$. L'application de multiplication $m_f: A
\to A$ est $R$-linéaire et possède donc
un polynôme caractéristique
$P(T) = T^n + r_{n-1}T^{n-1} + \ldots + r_0 \in R[T]$.
Pour tout idéal premier
$\mathfrak{p} \in \Spec(R)$, $f$ agit de manière nilpotente sur $A
\otimes_R \kappa(\mathfrak{p})$ si et seulement si $\mathfrak p \in
V(r_0, \ldots, r_{n-1})$.
\end{lemma}

\begin{proof}
Cela résulte assez facilement du fait que le polynôme
caractéristique $\bar P(T) \in \kappa(\mathfrak p)[T]$ de l'application
de multiplication $m_{\bar f}: A \otimes_R \kappa(\mathfrak p) \to
A \otimes_R \kappa(\mathfrak p)$, qui multiplie les éléments de $A
\otimes_R \kappa(\mathfrak p)$ par $\bar f$, l'image de $f$ considérée dans
$\kappa(\mathfrak p)$, est précisément l'image de $P(T)$ dans
$\kappa(\mathfrak p)[T]$. Soit $(a_{ij})$ la matrice de l'application
$m_f$, à coefficients dans $R$, relativement à une base $e_1, \ldots, e_n$
de $A$ comme $R$-module.
Alors $A \otimes_R \kappa(\mathfrak p) \cong (R \otimes_R
\kappa(\mathfrak p))^{\oplus n} = \kappa(\mathfrak p)^n$, qui est
un espace vectoriel de dimension $n$ sur $\kappa(\mathfrak p)$, de
base $e_1 \otimes 1, \ldots, e_n \otimes 1$. L'image est $\bar f = f
\otimes 1$, et l'application de multiplication $m_{\bar f}$ a donc pour matrice
$(a_{ij} \otimes 1)$. Ainsi, le polynôme caractéristique est
précisément l'image de $P(T)$.

\medskip\noindent
Nous savons par l'algèbre linéaire qu'un endomorphisme agit
de manière nilpotente sur un espace vectoriel de dimension $n$ si et seulement si son
polynôme caractéristique est $T^n$ (car le polynôme caractéristique
divise une puissance du polynôme minimal). Ainsi,
$f$ agit de manière nilpotente sur $A \otimes_R \kappa(\mathfrak p)$ si et
seulement si $\bar P(T) = T^n$. Cela se produit si et seulement si $r_i \in
\mathfrak p$ pour tout $0 \leq i \leq n - 1$, c'est-à-dire lorsque $\mathfrak p \in
V(r_0, \ldots, r_{n - 1}).$
\end{proof}
```

</details>

### 25 — lemma-affineline-special

Anglais L5597–5644 ; français L5577–5624.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5597) · FR-ALGEBRA-B8-CHOICE-0025.

C'est le coefficient dominant de g qui est une unité, non nécessairement g dans R[x]. Libre de type fini garde la structure de module et sa base d éléments ; unité et inversible ont ici le même sens algébrique. Le texte de l'affichage sur la multiplication nilpotente est entièrement traduit sans changer ses symboles. Les deux directions, via le corps résiduel et un idéal premier évitant f, sont conservées. Dat p.13 est un appui de registre, mais sa borne d'indices fautive dans sa dernière réunion n'est pas copiée.

Point particulier à relire : La page 13 de Dat emploie c1,...,cd puis une réunion de i=0 à d−1 et remplace X par T dans une phrase ; ces écarts de notation sont visibles sur le PDF et ne servent pas de norme pour les formules de Stacks.

Règles : FR-ALGEBRA-B8-RULE-IDEAL, FR-ALGEBRA-B8-RULE-FINITUDE, FR-ALGEBRA-B8-RULE-POLYNOME, FR-ALGEBRA-B8-RULE-NILPOTENT, FR-ALGEBRA-B8-RULE-IMAGE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-affineline-special}
Let $R$ be a ring. Let $f, g \in R[x]$ be polynomials.
Assume the leading coefficient of $g$ is a unit of $R$.
There exists elements $r_i\in R$, $i = 1\ldots, n$ such that
the image of $D(f) \cap V(g)$ in $\Spec(R)$ is
$\bigcup_{i = 1, \ldots, n} D(r_i)$.
\end{lemma}

\begin{proof}
Write $g = ux^d + a_{d-1}x^{d-1} + \ldots + a_0$, where
$d$ is the degree of $g$, and hence $u \in R^*$.
Consider the ring $A = R[x]/(g)$.
It is, as an $R$-module, finite free with basis the images
of $1, x, \ldots, x^{d-1}$. Consider multiplication
by (the image of) $f$ on $A$. This is an $R$-module map.
Hence we can let $P(T) \in R[T]$ be the characteristic polynomial
of this map. Write $P(T) = T^d + r_{d-1} T^{d-1} + \ldots + r_0$.
We claim that $r_0, \ldots, r_{d-1}$ have the desired property.
We will use below the property of characteristic polynomials
that
$$
\mathfrak p \in V(r_0, \ldots, r_{d-1})
\Leftrightarrow
\text{multiplication by }f\text{ is nilpotent on }
A \otimes_R \kappa(\mathfrak p).
$$
This was proved in Lemma \ref{lemma-characteristic-polynomial-prime}.

\medskip\noindent
Suppose $\mathfrak q\in D(f) \cap V(g)$, and let
$\mathfrak p = \mathfrak q \cap R$. Then there is a nonzero map
$A \otimes_R \kappa(\mathfrak p) \to \kappa(\mathfrak q)$ which
is compatible with multiplication by $f$.
And $f$ acts as a unit on $\kappa(\mathfrak q)$.
Thus we conclude $\mathfrak p \not \in  V(r_0, \ldots, r_{d-1})$.

\medskip\noindent
On the other hand, suppose that $r_i \not\in \mathfrak p$ for some
prime $\mathfrak p$ of $R$ and some $0 \leq i \leq d - 1$.
Then multiplication by $f$ is not nilpotent on the algebra
$A \otimes_R \kappa(\mathfrak p)$.
Hence there exists a prime ideal $\overline{\mathfrak q} \subset
A \otimes_R \kappa(\mathfrak p)$ not containing the image of $f$.
The inverse image of $\overline{\mathfrak q}$ in $R[x]$
is an element of $D(f) \cap V(g)$ mapping to $\mathfrak p$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-affineline-special}
Soit $R$ un anneau. Soient $f, g \in R[x]$ des polynômes.
Supposons que le coefficient dominant de $g$ soit une unité de $R$.
Il existe des éléments $r_i\in R$, $i = 1\ldots, n$, tels que
l'image de $D(f) \cap V(g)$ dans $\Spec(R)$ soit
$\bigcup_{i = 1, \ldots, n} D(r_i)$.
\end{lemma}

\begin{proof}
Écrivons $g = ux^d + a_{d-1}x^{d-1} + \ldots + a_0$, où
$d$ est le degré de $g$, et donc $u \in R^*$.
Considérons l'anneau $A = R[x]/(g)$.
Comme $R$-module, il est libre de type fini, de base les images
de $1, x, \ldots, x^{d-1}$. Considérons la multiplication
par (l'image de) $f$ sur $A$. C'est un morphisme de $R$-modules.
Nous pouvons donc noter $P(T) \in R[T]$ le polynôme caractéristique
de ce morphisme. Écrivons $P(T) = T^d + r_{d-1} T^{d-1} + \ldots + r_0$.
Nous affirmons que $r_0, \ldots, r_{d-1}$ ont la propriété voulue.
Nous utiliserons ci-dessous la propriété des polynômes caractéristiques
selon laquelle
$$
\mathfrak p \in V(r_0, \ldots, r_{d-1})
\Leftrightarrow
\text{la multiplication par }f\text{ est nilpotente sur }
A \otimes_R \kappa(\mathfrak p).
$$
Elle a été démontrée dans le lemme \ref{lemma-characteristic-polynomial-prime}.

\medskip\noindent
Supposons que $\mathfrak q\in D(f) \cap V(g)$, et soit
$\mathfrak p = \mathfrak q \cap R$. Il existe alors un morphisme non nul
$A \otimes_R \kappa(\mathfrak p) \to \kappa(\mathfrak q)$ qui
est compatible avec la multiplication par $f$.
Et $f$ agit comme une unité sur $\kappa(\mathfrak q)$.
Nous en concluons que $\mathfrak p \not \in  V(r_0, \ldots, r_{d-1})$.

\medskip\noindent
D'autre part, supposons que $r_i \not\in \mathfrak p$ pour un certain
idéal premier $\mathfrak p$ de $R$ et un certain $0 \leq i \leq d - 1$.
Alors la multiplication par $f$ n'est pas nilpotente sur l'algèbre
$A \otimes_R \kappa(\mathfrak p)$.
Il existe donc un idéal premier $\overline{\mathfrak q} \subset
A \otimes_R \kappa(\mathfrak p)$ qui ne contient pas l'image de $f$.
L'image réciproque de $\overline{\mathfrak q}$ dans $R[x]$
est un élément de $D(f) \cap V(g)$ qui s'envoie sur $\mathfrak p$.
\end{proof}
```

</details>

### 26 — theorem-chevalley

Anglais L5645–5720 ; français L5625–5700.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5645) · FR-ALGEBRA-B8-CHOICE-0026.

Le titre Théorème de Chevalley traduit l'argument optionnel de l'environnement, expressément hors des formules. L'énoncé porte sur la présentation finie sans hypothèse noethérienne. Dat p.12 donne le même énoncé. La preuve entière conserve la réduction à une variable, les parties V(c) et D(c), la récurrence sur le nombre et les degrés, et ses deux cas de base. La réunion disjointe affichée est une partition ensembliste, non un produit d'anneaux ni une somme topologique. L'abréviation l.o.t dans les formules reste littérale ; elle signifie termes de degré inférieur. La grammaire anglaise des cas de base est rendue en français correct.

Point particulier à relire : V(c) et D(c) forment une partition, mais V(c) n'est pas généralement ouvert ; l'affichage ne doit pas être lu comme une somme topologique. L'abréviation anglaise l.o.t demeure dans les formules pour respecter le témoin.

Règles : FR-ALGEBRA-B8-RULE-FINITUDE, FR-ALGEBRA-B8-RULE-CONSTRUCTIBLE, FR-ALGEBRA-B8-RULE-POLYNOME.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{theorem}[Chevalley's Theorem]
\label{theorem-chevalley}
Suppose that $R \to S$ is of finite presentation.
The image of a constructible subset of
$\Spec(S)$ in $\Spec(R)$ is constructible.
\end{theorem}

\begin{proof}
Write $S = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$.
We may factor $R \to S$ as $R \to R[x_1] \to R[x_1, x_2]
\to \ldots \to R[x_1, \ldots, x_{n-1}] \to S$. Hence
we may assume that $S = R[x]/(f_1, \ldots, f_m)$.
In this case we factor the map as $R \to R[x] \to S$,
and by Lemma \ref{lemma-closed-fp} we reduce to
the case $S = R[x]$. By Lemma \ref{lemma-qc-open} suffices
to show that if
$T = (\bigcup_{i = 1\ldots n} D(f_i)) \cap V(g_1, \ldots, g_m)$
for $f_i , g_j \in R[x]$ then the image in $\Spec(R)$ is
constructible. Since finite unions of constructible sets
are constructible, it suffices to deal with the case $n = 1$,
i.e., when $T = D(f) \cap V(g_1, \ldots, g_m)$.

\medskip\noindent
Note that if $c \in R$, then we have
$$
\Spec(R) =
V(c) \amalg D(c) =
\Spec(R/(c)) \amalg \Spec(R_c),
$$
and correspondingly $\Spec(R[x]) =
V(c) \amalg D(c) = \Spec(R/(c)[x]) \amalg
\Spec(R_c[x])$. The intersection of $T = D(f) \cap V(g_1, \ldots, g_m)$
with each part still has the same shape, with $f$, $g_i$ replaced
by their images in $R/(c)[x]$, respectively $R_c[x]$.
Note that the image of $T$
in $\Spec(R)$ is the union of the image of
$T \cap V(c)$ and $T \cap D(c)$. Using Lemmas \ref{lemma-open-fp}
and \ref{lemma-closed-fp} it suffices to prove the images of both
parts are constructible in $\Spec(R/(c))$, respectively
$\Spec(R_c)$.

\medskip\noindent
Let us assume we have $T = D(f) \cap V(g_1, \ldots, g_m)$
as above, with $\deg(g_1) \leq \deg(g_2) \leq \ldots \leq \deg(g_m)$.
We are going to use induction on $m$, and on the
degrees of the $g_i$. Let $d_1 = \deg(g_1)$, i.e., $g_1 = c x^{d_1} + l.o.t$
with $c \in R$ not zero. Cutting $R$ up into the pieces
$R/(c)$ and $R_c$ we either lower the degree of $g_1$ (and this
is covered by induction)
or we reduce to the case where $c$ is invertible.
If $c$ is invertible, and $m > 1$, then write
$g_2 = c' x^{d_2} + l.o.t$. In this case consider
$g_2' = g_2 - (c'/c) x^{d_2 - d_1} g_1$. Since the ideals
$(g_1, g_2, \ldots, g_m)$ and $(g_1, g_2', g_3, \ldots, g_m)$
are equal we see that $T = D(f) \cap V(g_1, g_2', g_3\ldots, g_m)$.
But here the degree of $g_2'$ is strictly less than the degree
of $g_2$ and hence this case is covered by induction.

\medskip\noindent
The bases case for the induction above are the cases
(a) $T = D(f) \cap V(g)$ where the leading coefficient
of $g$ is invertible, and (b) $T = D(f)$. These two cases
are dealt with in Lemmas \ref{lemma-affineline-special}
and \ref{lemma-affineline-open}.
\end{proof}
```

Français restauré :
```tex
\begin{theorem}[Théorème de Chevalley]
\label{theorem-chevalley}
Supposons que $R \to S$ soit de présentation finie.
L'image d'une partie constructible de
$\Spec(S)$ dans $\Spec(R)$ est constructible.
\end{theorem}

\begin{proof}
Écrivons $S = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$.
Nous pouvons factoriser $R \to S$ sous la forme $R \to R[x_1] \to R[x_1, x_2]
\to \ldots \to R[x_1, \ldots, x_{n-1}] \to S$. Nous pouvons donc
supposer que $S = R[x]/(f_1, \ldots, f_m)$.
Dans ce cas, nous factorisons le morphisme sous la forme $R \to R[x] \to S$
et, grâce au lemme \ref{lemma-closed-fp}, nous nous ramenons au
cas $S = R[x]$. D'après le lemme \ref{lemma-qc-open}, il suffit
de montrer que, si
$T = (\bigcup_{i = 1\ldots n} D(f_i)) \cap V(g_1, \ldots, g_m)$
pour $f_i , g_j \in R[x]$, alors l'image dans $\Spec(R)$ est
constructible. Puisque les réunions finies de parties constructibles
sont constructibles, il suffit de traiter le cas $n = 1$,
c'est-à-dire celui où $T = D(f) \cap V(g_1, \ldots, g_m)$.

\medskip\noindent
Notons que, si $c \in R$, alors
$$
\Spec(R) =
V(c) \amalg D(c) =
\Spec(R/(c)) \amalg \Spec(R_c),
$$
et, de façon correspondante, $\Spec(R[x]) =
V(c) \amalg D(c) = \Spec(R/(c)[x]) \amalg
\Spec(R_c[x])$. L'intersection de $T = D(f) \cap V(g_1, \ldots, g_m)$
avec chaque partie conserve la même forme, où $f$, $g_i$ sont remplacés
par leurs images dans $R/(c)[x]$ et $R_c[x]$, respectivement.
Notons que l'image de $T$
dans $\Spec(R)$ est la réunion des images de
$T \cap V(c)$ et de $T \cap D(c)$. D'après les lemmes \ref{lemma-open-fp}
et \ref{lemma-closed-fp}, il suffit de montrer que les images des deux
parties sont constructibles dans $\Spec(R/(c))$ et
$\Spec(R_c)$, respectivement.

\medskip\noindent
Supposons que $T = D(f) \cap V(g_1, \ldots, g_m)$
comme ci-dessus, avec $\deg(g_1) \leq \deg(g_2) \leq \ldots \leq \deg(g_m)$.
Nous allons raisonner par récurrence sur $m$ et sur les
degrés des $g_i$. Soit $d_1 = \deg(g_1)$, c'est-à-dire $g_1 = c x^{d_1} + l.o.t$
avec $c \in R$ non nul. En décomposant $R$ en les deux morceaux
$R/(c)$ et $R_c$, soit nous abaissons le degré de $g_1$ (et ce
cas est couvert par récurrence),
soit nous nous ramenons au cas où $c$ est inversible.
Si $c$ est inversible et si $m > 1$, écrivons
$g_2 = c' x^{d_2} + l.o.t$. Dans ce cas, considérons
$g_2' = g_2 - (c'/c) x^{d_2 - d_1} g_1$. Puisque les idéaux
$(g_1, g_2, \ldots, g_m)$ et $(g_1, g_2', g_3, \ldots, g_m)$
sont égaux, nous voyons que $T = D(f) \cap V(g_1, g_2', g_3\ldots, g_m)$.
Mais ici, le degré de $g_2'$ est strictement inférieur à celui
de $g_2$, et ce cas est donc couvert par récurrence.

\medskip\noindent
Les cas de base de la récurrence ci-dessus sont les cas
(a) $T = D(f) \cap V(g)$ où le coefficient dominant
de $g$ est inversible, et (b) $T = D(f)$. Ces deux cas
sont traités par les lemmes \ref{lemma-affineline-special}
et \ref{lemma-affineline-open}.
\end{proof}
```

</details>

### 27 — section-more-images

Anglais L5721–5728 ; français L5701–5708.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5721) · FR-ALGEBRA-B8-CHOICE-0027.

Compléments sur les images annonce des lemmes supplémentaires sur les applications entre spectres, sans transformer le titre en nouveau théorème de constructibilité. Le renvoi à going-up demeure exactement le renvoi officiel ; aucune propriété de relèvement des chaînes n'est importée dans ces deux phrases.

Règles : Titre et contexte directement comparés.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{More on images}
\label{section-more-images}

\noindent
In this section we collect a few additional lemmas concerning the image
on $\Spec$ for ring maps. See also Section \ref{section-going-up}
for example.
```

Français restauré :
```tex
\section{Compléments sur les images}
\label{section-more-images}

\noindent
Dans cette section, nous rassemblons quelques lemmes supplémentaires concernant l'image
au niveau de $\Spec$ pour les morphismes d'anneaux. Voir aussi, par exemple, la section
\ref{section-going-up}.
```

</details>

### 28 — lemma-generic-finite-presentation

Anglais L5729–5768 ; français L5709–5748.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5729) · FR-ALGEBRA-B8-CHOICE-0028.

Les anneaux sont intègres, l'inclusion est de type fini, et les deux localisations utilisent des éléments non nuls. La conclusion est de présentation finie après localisation, pas avant. La preuve conserve le polynôme de degré minimal, son coefficient inversé et le quotient rendu unitaire. Dat p.11 et Ducros p.26 distinguent les deux notions de finitude. La dernière étape laissée au lecteur reste omise, sans preuve ajoutée ni changement de la provenance de f',g'.

Règles : FR-ALGEBRA-B8-RULE-IDEAL, FR-ALGEBRA-B8-RULE-FINITUDE, FR-ALGEBRA-B8-RULE-POLYNOME, FR-ALGEBRA-B8-RULE-INTEGRE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-generic-finite-presentation}
Let $R \subset S$ be an inclusion of domains.
Assume that $R \to S$ is of finite type.
There exists a nonzero $f \in R$, and a nonzero $g \in S$
such that $R_f \to S_{fg}$ is of finite presentation.
\end{lemma}

\begin{proof}
By induction on the number of generators of $S$ over $R$.
During the proof we may replace $R$ by $R_f$ and $S$ by $S_f$
for some nonzero $f \in R$.

\medskip\noindent
Suppose that $S$ is generated by a single element
over $R$. Then $S = R[x]/\mathfrak q$ for some
prime ideal $\mathfrak q \subset R[x]$. If $\mathfrak q = (0)$
there is nothing to prove. If $\mathfrak q \not = (0)$,
then let $h \in \mathfrak q$ be a nonzero element with minimal
degree in $x$. Write $h = f x^d + a_{d - 1} x^{d - 1} + \ldots + a_0$
with $a_i \in R$ and $f \not = 0$. After inverting $f$
in $R$ and $S$ we may assume that $h$ is monic. We obtain
a surjective $R$-algebra map $R[x]/(h) \to S$.
We have $R[x]/(h) = R \oplus Rx \oplus \ldots \oplus Rx^{d - 1}$
as an $R$-module and by minimality of $d$ we see that
$R[x]/(h)$ maps injectively into $S$. Thus $R[x]/(h) \cong S$
is finitely presented over $R$.

\medskip\noindent
Suppose that $S$ is generated by $n > 1$ elements over $R$.
Say $x_1, \ldots, x_n \in S$ generate $S$. Denote $S' \subset S$
the $R$-subalgebra generated by $x_1, \ldots, x_{n-1}$. By induction
hypothesis we see that there exist $f\in R$ and $g \in S'$
nonzero such that $R_f \to S'_{fg}$ is of finite presentation.
Next we apply the induction hypothesis to $S'_{fg} \to S_{fg}$
to see that there exist $f' \in S'_{fg}$ and
$g' \in S_{fg}$ such that $S'_{fgf'} \to S_{fgf'g'}$
is of finite presentation. We leave it to the reader to conclude.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-generic-finite-presentation}
Soit $R \subset S$ une inclusion d'anneaux intègres.
Supposons que $R \to S$ soit de type fini.
Il existe un élément non nul $f \in R$ et un élément non nul $g \in S$
tels que $R_f \to S_{fg}$ soit de présentation finie.
\end{lemma}

\begin{proof}
Nous raisonnons par récurrence sur le nombre de générateurs de $S$ sur $R$.
Au cours de la démonstration, nous pouvons remplacer $R$ par $R_f$ et $S$ par $S_f$
pour un certain élément non nul $f \in R$.

\medskip\noindent
Supposons que $S$ soit engendré par un seul élément
sur $R$. Alors $S = R[x]/\mathfrak q$ pour un certain
idéal premier $\mathfrak q \subset R[x]$. Si $\mathfrak q = (0)$,
il n'y a rien à démontrer. Si $\mathfrak q \not = (0)$,
soit $h \in \mathfrak q$ un élément non nul de degré minimal
en $x$. Écrivons $h = f x^d + a_{d - 1} x^{d - 1} + \ldots + a_0$,
avec $a_i \in R$ et $f \not = 0$. Après avoir inversé $f$
dans $R$ et $S$, nous pouvons supposer que $h$ est unitaire. Nous obtenons
un morphisme surjectif de $R$-algèbres $R[x]/(h) \to S$.
Nous avons $R[x]/(h) = R \oplus Rx \oplus \ldots \oplus Rx^{d - 1}$
comme $R$-module et, par minimalité de $d$, nous voyons que
$R[x]/(h)$ s'injecte dans $S$. Ainsi, $R[x]/(h) \cong S$
est de présentation finie sur $R$.

\medskip\noindent
Supposons que $S$ soit engendré par $n > 1$ éléments sur $R$.
Disons que $x_1, \ldots, x_n \in S$ engendrent $S$. Notons $S' \subset S$
la sous-$R$-algèbre engendrée par $x_1, \ldots, x_{n-1}$. Par l'hypothèse
de récurrence, nous voyons qu'il existe des éléments non nuls $f\in R$ et $g \in S'$
tels que $R_f \to S'_{fg}$ soit de présentation finie.
Nous appliquons ensuite l'hypothèse de récurrence à $S'_{fg} \to S_{fg}$
pour voir qu'il existe $f' \in S'_{fg}$ et
$g' \in S_{fg}$ tels que $S'_{fgf'} \to S_{fgf'g'}$
soit de présentation finie. Nous laissons au lecteur le soin de conclure.
\end{proof}
```

</details>

### 29 — lemma-characterize-image-finite-type

Anglais L5769–5820 ; français L5749–5800.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5769) · FR-ALGEBRA-B8-CHOICE-0029.

L'hypothèse est ici de type fini et non de présentation finie. La conclusion est relative à l'adhérence du point ξ appartenant déjà à l'image : elle ne déclare pas toute l'image constructible. Le diagramme complet, les quotients intègres, les deux ouverts denses et le passage au théorème de Chevalley sont maintenus. Point générique est attesté chez Dat p.13 ; un ouvert dense de l'adhérence n'est pas nécessairement ouvert dans tout X.

Règles : FR-ALGEBRA-B8-RULE-IDEAL, FR-ALGEBRA-B8-RULE-FINITUDE, FR-ALGEBRA-B8-RULE-CONSTRUCTIBLE, FR-ALGEBRA-B8-RULE-OPEN, FR-ALGEBRA-B8-RULE-RESIDUEL, FR-ALGEBRA-B8-RULE-INTEGRE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-image-finite-type}
Let $R \to S$ be a finite type ring map.
Denote $X = \Spec(R)$ and $Y = \Spec(S)$.
Write $f : Y \to X$ the induced
map of spectra. Let $E \subset Y = \Spec(S)$ be a
constructible set.
If a point $\xi \in X$ is in $f(E)$, then
$\overline{\{\xi\}} \cap f(E)$ contains an open
dense subset of $\overline{\{\xi\}}$.
\end{lemma}

\begin{proof}
Let $\xi \in X$ be a point of $f(E)$. Choose a point $\eta \in E$
mapping to $\xi$. Let $\mathfrak p \subset R$ be the prime
corresponding to $\xi$ and let $\mathfrak q \subset S$ be the
prime corresponding to $\eta$. Consider the diagram
$$
\xymatrix{
\eta \ar[r] \ar@{|->}[d] & E \cap Y' \ar[r] \ar[d] &
Y' = \Spec(S/\mathfrak q) \ar[r] \ar[d] &
Y \ar[d] \\
\xi \ar[r] & f(E) \cap X' \ar[r] &
X' = \Spec(R/\mathfrak p) \ar[r] &
X
}
$$
By Lemma \ref{lemma-affine-map-quasi-compact} the set $E \cap Y'$
is constructible in $Y'$.
It follows that we may replace $X$ by $X'$ and
$Y$ by $Y'$. Hence we may assume that $R \subset S$ is an
inclusion of domains, $\xi$ is the generic
point of $X$, and $\eta$ is the generic point of $Y$.
By Lemma \ref{lemma-generic-finite-presentation}
combined with Chevalley's theorem
(Theorem \ref{theorem-chevalley})
we see that there exist dense opens $U \subset X$,
$V \subset Y$ such that $f(V) \subset U$ and
such that $f : V \to U$ maps constructible sets
to constructible sets. Note that $E \cap V$ is
constructible in $V$, see Topology,
Lemma \ref{topology-lemma-open-immersion-constructible-inverse-image}.
Hence $f(E \cap V)$ is constructible in $U$ and contains $\xi$.
By Topology, Lemma \ref{topology-lemma-generic-point-in-constructible}
we see that $f(E \cap V)$ contains a dense open $U' \subset U$.
\end{proof}

\noindent
At the end of this section we present a few more results on
images of maps on Spectra that have nothing to do with constructible
sets.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-characterize-image-finite-type}
Soit $R \to S$ un morphisme d'anneaux de type fini.
Notons $X = \Spec(R)$ et $Y = \Spec(S)$.
Notons $f : Y \to X$ le morphisme induit
sur les spectres. Soit $E \subset Y = \Spec(S)$ une
partie constructible.
Si un point $\xi \in X$ appartient à $f(E)$, alors
$\overline{\{\xi\}} \cap f(E)$ contient un sous-ensemble ouvert
dense de $\overline{\{\xi\}}$.
\end{lemma}

\begin{proof}
Soit $\xi \in X$ un point de $f(E)$. Choisissons un point $\eta \in E$
qui s'envoie sur $\xi$. Soit $\mathfrak p \subset R$ l'idéal premier
correspondant à $\xi$, et soit $\mathfrak q \subset S$ l'idéal premier
correspondant à $\eta$. Considérons le diagramme
$$
\xymatrix{
\eta \ar[r] \ar@{|->}[d] & E \cap Y' \ar[r] \ar[d] &
Y' = \Spec(S/\mathfrak q) \ar[r] \ar[d] &
Y \ar[d] \\
\xi \ar[r] & f(E) \cap X' \ar[r] &
X' = \Spec(R/\mathfrak p) \ar[r] &
X
}
$$
D'après le lemme \ref{lemma-affine-map-quasi-compact}, la partie $E \cap Y'$
est constructible dans $Y'$.
Il s'ensuit que nous pouvons remplacer $X$ par $X'$ et
$Y$ par $Y'$. Nous pouvons donc supposer que $R \subset S$ est une
inclusion d'anneaux intègres, que $\xi$ est le point générique
de $X$ et que $\eta$ est le point générique de $Y$.
En combinant le lemme \ref{lemma-generic-finite-presentation}
avec le théorème de Chevalley
(théorème \ref{theorem-chevalley}),
nous voyons qu'il existe des ouverts denses $U \subset X$ et
$V \subset Y$ tels que $f(V) \subset U$ et
que $f : V \to U$ envoie les parties constructibles
sur des parties constructibles. Notons que $E \cap V$ est
constructible dans $V$, voir Topologie,
lemme \ref{topology-lemma-open-immersion-constructible-inverse-image}.
Ainsi, $f(E \cap V)$ est constructible dans $U$ et contient $\xi$.
D'après Topologie, lemme \ref{topology-lemma-generic-point-in-constructible},
nous voyons que $f(E \cap V)$ contient un ouvert dense $U' \subset U$.
\end{proof}

\noindent
À la fin de cette section, nous présentons quelques résultats supplémentaires sur les
images des applications entre spectres qui n'ont rien à voir avec les parties
constructibles.
```

</details>

### 30 — lemma-surjective-spec-radical-ideal

Anglais L5821–5870 ; français L5801–5850.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5821) · FR-ALGEBRA-B8-CHOICE-0030.

La surjectivité est celle de l'application sur les spectres, pas celle du morphisme d'anneaux. Les quatre conditions distinguent tous les idéaux, les idéaux radicaux et les idéaux premiers. Le changement de base est quelconque ; la preuve s'appuie sur une extension de corps résiduels, pas sur une platitude supposée de S sur R. Dat p.10 traite un critère sous hypothèse de platitude : cette hypothèse externe n'est pas importée. L'énumération finale anglaise (1),(2),(3) reste telle quelle, sans ajouter (4) implicitement.

Point particulier à relire : L'omission de (4) dans la liste finale n'est pas une assertion fausse : (4) suit déjà des trois conditions équivalentes. Elle est enregistrée comme décalage de numérotation, pas comme nouveau faux théorème.

Règles : FR-ALGEBRA-B8-RULE-IDEAL, FR-ALGEBRA-B8-RULE-RESIDUEL, FR-ALGEBRA-B8-RULE-IMAGE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-surjective-spec-radical-ideal}
Let $\varphi : R \to S$ be a ring map.
The following are equivalent:
\begin{enumerate}
\item The map $\Spec(S) \to \Spec(R)$ is surjective.
\item For any ideal $I \subset R$
the inverse image of $\sqrt{IS}$ in $R$ is equal to $\sqrt{I}$.
\item For any radical ideal $I \subset R$ the inverse image
of $IS$ in $R$ is equal to $I$.
\item For every prime $\mathfrak p$ of $R$ the inverse
image of $\mathfrak p S$ in $R$ is $\mathfrak p$.
\end{enumerate}
In this case the same is true after any base change: Given a ring map
$R \to R'$ the ring map $R' \to R' \otimes_R S$ has the equivalent
properties (1), (2), (3) as well.
\end{lemma}

\begin{proof}
If $J \subset S$ is an ideal, then
$\sqrt{\varphi^{-1}(J)} = \varphi^{-1}(\sqrt{J})$. This shows that (2)
and (3) are equivalent.
The implication (3) $\Rightarrow$ (4) is immediate.
If $I \subset R$ is a radical ideal, then
Lemma \ref{lemma-Zariski-topology}
guarantees that $I = \bigcap_{I \subset \mathfrak p} \mathfrak p$.
Hence (4) $\Rightarrow$ (2). By
Lemma \ref{lemma-in-image}
we have $\mathfrak p = \varphi^{-1}(\mathfrak p S)$ if and only if
$\mathfrak p$ is in the image. Hence (1) $\Leftrightarrow$ (4).
Thus (1), (2), (3), and (4) are equivalent.

\medskip\noindent
Assume (1) holds. Let $R \to R'$ be a ring map. Let
$\mathfrak p' \subset R'$ be a prime ideal lying over the prime
$\mathfrak p$ of $R$. To see that $\mathfrak p'$ is in the image
of $\Spec(R' \otimes_R S) \to \Spec(R')$ we have to show
that $(R' \otimes_R S) \otimes_{R'} \kappa(\mathfrak p')$ is not zero, see
Lemma \ref{lemma-in-image}.
But we have
$$
(R' \otimes_R S) \otimes_{R'} \kappa(\mathfrak p') =
S \otimes_R \kappa(\mathfrak p)
\otimes_{\kappa(\mathfrak p)} \kappa(\mathfrak p')
$$
which is not zero as $S \otimes_R \kappa(\mathfrak p)$ is not zero
by assumption and $\kappa(\mathfrak p) \to \kappa(\mathfrak p')$ is
an extension of fields.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-surjective-spec-radical-ideal}
Soit $\varphi : R \to S$ un morphisme d'anneaux.
Les conditions suivantes sont équivalentes :
\begin{enumerate}
\item L'application $\Spec(S) \to \Spec(R)$ est surjective.
\item Pour tout idéal $I \subset R$,
l'image réciproque de $\sqrt{IS}$ dans $R$ est égale à $\sqrt{I}$.
\item Pour tout idéal radical $I \subset R$, l'image réciproque
de $IS$ dans $R$ est égale à $I$.
\item Pour tout idéal premier $\mathfrak p$ de $R$, l'image
réciproque de $\mathfrak p S$ dans $R$ est $\mathfrak p$.
\end{enumerate}
Dans ce cas, il en va de même après tout changement de base : étant donné un morphisme d'anneaux
$R \to R'$, le morphisme d'anneaux $R' \to R' \otimes_R S$ possède lui aussi les
propriétés équivalentes (1), (2), (3).
\end{lemma}

\begin{proof}
Si $J \subset S$ est un idéal, alors
$\sqrt{\varphi^{-1}(J)} = \varphi^{-1}(\sqrt{J})$. Cela montre que (2)
et (3) sont équivalentes.
L'implication (3) $\Rightarrow$ (4) est immédiate.
Si $I \subset R$ est un idéal radical, alors le
lemme \ref{lemma-Zariski-topology}
garantit que $I = \bigcap_{I \subset \mathfrak p} \mathfrak p$.
Ainsi, (4) $\Rightarrow$ (2). D'après le
lemme \ref{lemma-in-image},
nous avons $\mathfrak p = \varphi^{-1}(\mathfrak p S)$ si et seulement si
$\mathfrak p$ appartient à l'image. Ainsi, (1) $\Leftrightarrow$ (4).
Les conditions (1), (2), (3) et (4) sont donc équivalentes.

\medskip\noindent
Supposons que (1) soit vérifiée. Soit $R \to R'$ un morphisme d'anneaux. Soit
$\mathfrak p' \subset R'$ un idéal premier au-dessus de l'idéal premier
$\mathfrak p$ de $R$. Pour voir que $\mathfrak p'$ appartient à l'image
de $\Spec(R' \otimes_R S) \to \Spec(R')$, nous devons montrer
que $(R' \otimes_R S) \otimes_{R'} \kappa(\mathfrak p')$ n'est pas nul, voir le
lemme \ref{lemma-in-image}.
Mais nous avons
$$
(R' \otimes_R S) \otimes_{R'} \kappa(\mathfrak p') =
S \otimes_R \kappa(\mathfrak p)
\otimes_{\kappa(\mathfrak p)} \kappa(\mathfrak p')
$$
qui n'est pas nul, car $S \otimes_R \kappa(\mathfrak p)$ n'est pas nul
par hypothèse et $\kappa(\mathfrak p) \to \kappa(\mathfrak p')$ est
une extension de corps.
\end{proof}
```

</details>

### 31 — lemma-domain-image-dense-set-points-generic-point

Anglais L5871–5904 ; français L5851–5884.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5871) · FR-ALGEBRA-B8-CHOICE-0031.

Intègre est une hypothèse sur R, non S. Les trois conditions concernent injection, densité et existence d'un premier contracté en zéro. La localisation exacte et le point générique sont conservés. Le français avait réparé proper closed subset of R en fermé propre du spectre de R ; il revient au libellé fermé propre de R. Le dossier précise que le fermé est en réalité dans Spec(R), sans déguiser cette correction proposée en traduction.

Point particulier à relire : La restauration conserve le mot R où le contexte exige Spec(R). Une correction souhaitable ne devient pas une correction autorisée du témoin dans cette édition fidèle.

Règles : FR-ALGEBRA-B8-RULE-IDEAL, FR-ALGEBRA-B8-RULE-OPEN, FR-ALGEBRA-B8-RULE-RESIDUEL, FR-ALGEBRA-B8-RULE-IMAGE, FR-ALGEBRA-B8-RULE-INTEGRE, FR-ALGEBRA-B8-RULE-EXACT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-domain-image-dense-set-points-generic-point}
Let $R$ be a domain. Let $\varphi : R \to S$ be a ring map.
The following are equivalent:
\begin{enumerate}
\item The ring map $R \to S$ is injective.
\item The image $\Spec(S) \to \Spec(R)$
contains a dense set of points.
\item There exists a prime ideal $\mathfrak q \subset S$
whose inverse image in $R$ is $(0)$.
\end{enumerate}
\end{lemma}

\begin{proof}
Let $K$ be the field of fractions of the domain $R$.
Assume that $R \to S$ is injective. Since localization
is exact we see that $K \to S \otimes_R K$ is injective.
Hence there is a prime mapping to $(0)$ by
Lemma \ref{lemma-in-image}.

\medskip\noindent
Note that $(0)$ is dense in $\Spec(R)$, so that the
last condition implies the second.

\medskip\noindent
Suppose the second condition holds. Let $f \in R$,
$f \not = 0$. As $R$ is a domain we see that $V(f)$
is a proper closed subset of $R$. By assumption
there exists a prime $\mathfrak q$
of $S$ such that $\varphi(f) \not \in \mathfrak q$.
Hence $\varphi(f) \not = 0$.
Hence $R \to S$ is injective.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-domain-image-dense-set-points-generic-point}
Soit $R$ un anneau intègre. Soit $\varphi : R \to S$ un morphisme d'anneaux.
Les conditions suivantes sont équivalentes :
\begin{enumerate}
\item Le morphisme d'anneaux $R \to S$ est injectif.
\item L'image de $\Spec(S) \to \Spec(R)$
contient un ensemble dense de points.
\item Il existe un idéal premier $\mathfrak q \subset S$
dont l'image réciproque dans $R$ est $(0)$.
\end{enumerate}
\end{lemma}

\begin{proof}
Soit $K$ le corps des fractions de l'anneau intègre $R$.
Supposons que $R \to S$ soit injectif. Puisque la localisation
est exacte, nous voyons que $K \to S \otimes_R K$ est injectif.
Il existe donc un idéal premier s'envoyant sur $(0)$ d'après le
lemme \ref{lemma-in-image}.

\medskip\noindent
Notons que $(0)$ est dense dans $\Spec(R)$, de sorte que la
dernière condition implique la seconde.

\medskip\noindent
Supposons que la seconde condition soit vérifiée. Soit $f \in R$,
$f \not = 0$. Puisque $R$ est un anneau intègre, nous voyons que $V(f)$
est un fermé propre de $R$. Par hypothèse,
il existe un idéal premier $\mathfrak q$
de $S$ tel que $\varphi(f) \not \in \mathfrak q$.
Ainsi, $\varphi(f) \not = 0$.
Le morphisme $R \to S$ est donc injectif.
\end{proof}
```

</details>

### 32 — lemma-injective-minimal-primes-in-image

Anglais L5905–5919 ; français L5885–5899.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5905) · FR-ALGEBRA-B8-CHOICE-0032.

Atteint tous les idéaux premiers minimaux traduit hits all the minimal primes sans affirmer une surjectivité sur tout le spectre. Le premier p est minimal dans R et devient l'unique premier de Rp. L'exactitude de la localisation conserve la non-nullité requise ; R n'est pas supposé intègre. La preuve courte est intégralement retenue.

Règles : FR-ALGEBRA-B8-RULE-IDEAL, FR-ALGEBRA-B8-RULE-EXACT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-injective-minimal-primes-in-image}
Let $R \subset S$ be an injective ring map.
Then $\Spec(S) \to \Spec(R)$
hits all the minimal primes.
\end{lemma}

\begin{proof}
Let $\mathfrak p \subset R$ be a minimal prime.
In this case $R_{\mathfrak p}$ has a unique prime ideal.
Hence it suffices to show that $S_{\mathfrak p}$ is not zero.
And this follows from the fact that localization is exact,
see Proposition \ref{proposition-localization-exact}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-injective-minimal-primes-in-image}
Soit $R \subset S$ un morphisme d'anneaux injectif.
Alors $\Spec(S) \to \Spec(R)$
atteint tous les idéaux premiers minimaux.
\end{lemma}

\begin{proof}
Soit $\mathfrak p \subset R$ un idéal premier minimal.
Dans ce cas, $R_{\mathfrak p}$ possède un unique idéal premier.
Il suffit donc de montrer que $S_{\mathfrak p}$ n'est pas nul.
Cela résulte du fait que la localisation est exacte,
voir la proposition \ref{proposition-localization-exact}.
\end{proof}
```

</details>

### 33 — lemma-image-dense-generic-points

Anglais L5920–5945 ; français L5900–5925.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5920) · FR-ALGEBRA-B8-CHOICE-0033.

Constitué d'éléments nilpotents est retenu, et non noyau nilpotent : aucun exposant uniforme sur tout l'idéal n'est donné. Ducros 0.1.7 distingue la nilpotence élément par élément. L'adhérence de l'image est V(I), les trois équivalences sont conservées et le quotient par I ne modifie pas la topologie sous l'hypothèse indiquée. La notation de contraction R intersection q reste l'abus de notation source, sans injectivité initiale ajoutée.

Point particulier à relire : Nilpotence de chaque élément n'implique pas nilpotence de l'idéal. Une contraction par un morphisme non injectif n'est pas une intersection littérale de sous-ensembles du même anneau.

Règles : FR-ALGEBRA-B8-RULE-IDEAL, FR-ALGEBRA-B8-RULE-NILPOTENT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-image-dense-generic-points}
Let $R \to S$ be a ring map. The following are equivalent:
\begin{enumerate}
\item The kernel of $R \to S$ consists of nilpotent elements.
\item The minimal primes of $R$ are in the image of
$\Spec(S) \to \Spec(R)$.
\item The image of $\Spec(S) \to \Spec(R)$ is dense
in $\Spec(R)$.
\end{enumerate}
\end{lemma}

\begin{proof}
Let $I = \Ker(R \to S)$. Note that
$\sqrt{(0)} = \bigcap_{\mathfrak q \subset S} \mathfrak q$, see
Lemma \ref{lemma-Zariski-topology}.
Hence $\sqrt{I} = \bigcap_{\mathfrak q \subset S} R \cap \mathfrak q$.
Thus $V(I) = V(\sqrt{I})$ is the closure of the image of
$\Spec(S) \to \Spec(R)$.
This shows that (1) is equivalent to (3). It is clear that
(2) implies (3). Finally, assume (1). We may replace
$R$ by $R/I$ and $S$ by $S/IS$ without affecting the topology
of the spectra and the map. Hence the implication (1) $\Rightarrow$ (2)
follows from Lemma \ref{lemma-injective-minimal-primes-in-image}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-image-dense-generic-points}
Soit $R \to S$ un morphisme d'anneaux. Les conditions suivantes sont équivalentes :
\begin{enumerate}
\item Le noyau de $R \to S$ est constitué d'éléments nilpotents.
\item Les idéaux premiers minimaux de $R$ appartiennent à l'image de
$\Spec(S) \to \Spec(R)$.
\item L'image de $\Spec(S) \to \Spec(R)$ est dense
dans $\Spec(R)$.
\end{enumerate}
\end{lemma}

\begin{proof}
Soit $I = \Ker(R \to S)$. Notons que
$\sqrt{(0)} = \bigcap_{\mathfrak q \subset S} \mathfrak q$, voir le
lemme \ref{lemma-Zariski-topology}.
Ainsi, $\sqrt{I} = \bigcap_{\mathfrak q \subset S} R \cap \mathfrak q$.
Donc $V(I) = V(\sqrt{I})$ est l'adhérence de l'image de
$\Spec(S) \to \Spec(R)$.
Cela montre que (1) équivaut à (3). Il est clair que
(2) implique (3). Enfin, supposons (1). Nous pouvons remplacer
$R$ par $R/I$ et $S$ par $S/IS$ sans changer la topologie
des spectres ni l'application. Ainsi, l'implication (1) $\Rightarrow$ (2)
résulte du lemme \ref{lemma-injective-minimal-primes-in-image}.
\end{proof}
```

</details>

### 34 — lemma-minimal-prime-image-minimal-prime

Anglais L5946–5960 ; français L5926–5940.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5946) · FR-ALGEBRA-B8-CHOICE-0034.

L'énoncé est conditionnel : le premier minimal p de R appartient déjà à l'image. On choisit ensuite un premier minimal r de S contenu dans q, et sa contraction est p par minimalité de p. L'expression image d'un premier minimal renvoie à S, non au localisé ni au même anneau. Aucun théorème d'intégralité ou de surjectivité générale n'est ajouté.

Règles : FR-ALGEBRA-B8-RULE-IDEAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-minimal-prime-image-minimal-prime}
Let $R \to S$ be a ring map. If a minimal prime $\mathfrak p \subset R$
is in the image of $\Spec(S) \to \Spec(R)$, then it is the image
of a minimal prime.
\end{lemma}

\begin{proof}
Say $\mathfrak p = \mathfrak q \cap R$. Then choose a minimal
prime $\mathfrak r \subset S$ with $\mathfrak r \subset \mathfrak q$, see
Lemma \ref{lemma-Zariski-topology}.
By minimality of $\mathfrak p$ we see that
$\mathfrak p = \mathfrak r \cap R$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-minimal-prime-image-minimal-prime}
Soit $R \to S$ un morphisme d'anneaux. Si un idéal premier minimal $\mathfrak p \subset R$
appartient à l'image de $\Spec(S) \to \Spec(R)$, alors il est l'image
d'un idéal premier minimal.
\end{lemma}

\begin{proof}
Écrivons $\mathfrak p = \mathfrak q \cap R$. Choisissons alors un
idéal premier minimal $\mathfrak r \subset S$ tel que $\mathfrak r \subset \mathfrak q$, voir le
lemme \ref{lemma-Zariski-topology}.
Par minimalité de $\mathfrak p$, nous voyons que
$\mathfrak p = \mathfrak r \cap R$.
\end{proof}
```

</details>

### 35 — lemma-intersection-not-zero

Anglais L5961–5979 ; français L5941–5959.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5961) · FR-ALGEBRA-B8-CHOICE-0035.

L'extension algébrique porte sur les corps des fractions ; elle n'est pas remplacée par une extension entière des anneaux. La relation polynomiale a des coefficients dans A après dénominateurs communs, et ses coefficients extrêmes sont non nuls, sans exiger qu'elle soit unitaire. Le terme constant appartient à A intersection J. La conclusion sur un fermé propre et sa non-densité garde exactement la direction de la source.

Règles : FR-ALGEBRA-B8-RULE-OPEN, FR-ALGEBRA-B8-RULE-RESIDUEL, FR-ALGEBRA-B8-RULE-INTEGRE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-intersection-not-zero}
Let $A \subset B$ be an inclusion of domains inducing an algebraic extension
of fraction fields. If $J \subset B$ is a nonzero ideal, then $A \cap J$
is nonzero too. Thus the image of a proper closed subset of $\Spec(B)$
is not dense in $\Spec(A)$.
\end{lemma}

\begin{proof}
Let $x \in J$ be a nonzero element. Since $x$ is algebraic over the fraction
field of $A$, there exists a $d \geq 1$ and $a_0, \ldots, a_d \in A$
with $a_0, a_d \not = 0$ such that
$a_d x^d + a_{d - 1} x^{d - 1} + \ldots + a_0 = 0$ in $B$.
Then $a_0 \in A \cap J$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-intersection-not-zero}
Soit $A \subset B$ une inclusion d'anneaux intègres induisant une extension algébrique
des corps des fractions. Si $J \subset B$ est un idéal non nul, alors $A \cap J$
est également non nul. Ainsi, l'image d'un fermé propre de $\Spec(B)$
n'est pas dense dans $\Spec(A)$.
\end{lemma}

\begin{proof}
Soit $x \in J$ un élément non nul. Puisque $x$ est algébrique sur le corps des
fractions de $A$, il existe un $d \geq 1$ et des $a_0, \ldots, a_d \in A$
tels que $a_0, a_d \not = 0$ et que
$a_d x^d + a_{d - 1} x^{d - 1} + \ldots + a_0 = 0$ dans $B$.
Alors $a_0 \in A \cap J$.
\end{proof}
```

</details>

## Observations sur le texte source sans modification du témoin

Ces notes ne font pas partie de la traduction. Le statut proposé ne signifie ni examen humain ni admission comme nouvel erratum.

### FR-ALGEBRA-B8-SOURCE-NOTE-0001

[Source L5098](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5098) — section-oka-families.

```tex
I = R \cap \mathfrak m
```

Le morphisme R vers S⁻¹R n'est pas supposé injectif. L'intersection se lit comme la contraction de m ; par exemple localiser Z/6Z en les puissances de 2 tue l'élément 3. Il s'agit d'un abus de notation interprétable, pas d'une nouvelle hypothèse à ajouter.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B8-SOURCE-NOTE-0002

[Source L5391](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5391) — lemma-qc-open.

```tex
$X \setminus V(I) = U$
```

L'énoncé introduit U inclus dans Spec(R), mais pas X. Remplacer X par Spec(R) est la réparation naturelle ; le symbole officiel reste dans la traduction fidèle et cette proposition demeure externe.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B8-SOURCE-NOTE-0003

[Source L5573](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5573) — lemma-characteristic-polynomial-prime.

```tex
\otimes_R \kappa(\mathfrak p)$ by $\bar f$, the image of $f$ viewed in
$\kappa(\mathfrak p)$,
```

L'image f⊗1 vit dans A⊗Rκ(p), non en général dans κ(p). Pour R=k, A=k[ε]/(ε²) et f=ε, c'est un élément non scalaire de l'algèbre de dimension deux. La matrice et la phrase suivante de la source confirment f⊗1. La correction française antérieure est retirée du texte fidèle, mais son motif est conservé ici.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B8-SOURCE-NOTE-0004

[Source L5670](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5670) — theorem-chevalley.

```tex
\Spec(R) =
V(c) \amalg D(c) =
\Spec(R/(c)) \amalg \Spec(R_c),
```

Le signe désigne une partition ensembliste. En général V(c) n'est pas ouvert : pour R=Z et c=2, {(2)} n'est pas ouvert dans Spec(Z). La lire comme une somme topologique ou comme un produit de R/(c) et Rc serait faux. Le texte et le signe sont préservés ; cette note explique la portée, sans déclarer erronée la partition.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B8-SOURCE-NOTE-0005

[Source L5836](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5836) — lemma-surjective-spec-radical-ideal.

```tex
properties (1), (2), (3) as well.
```

Quatre conditions précèdent, mais la phrase finale n'en énumère que trois. La quatrième suit déjà des équivalences. Une harmonisation de numérotation est possible ; aucune nouvelle erreur de théorème ni admission d'erratum n'est revendiquée.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B8-SOURCE-NOTE-0006

[Source L5898](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5898) — lemma-domain-image-dense-set-points-generic-point.

```tex
is a proper closed subset of $R$. By assumption
```

V(f) est un fermé de Spec(R), pas un fermé de l'anneau R doté ici d'aucune topologie. Le contexte et le point générique imposent Spec(R). La restauration de fermé propre de R maintient cette coquille officielle dans le corps fidèle, avec la correction clairement séparée.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

### FR-ALGEBRA-B8-SOURCE-NOTE-0007

[Source L5936](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5936) — lemma-image-dense-generic-points.

```tex
Hence $\sqrt{I} = \bigcap_{\mathfrak q \subset S} R \cap \mathfrak q$.
```

R vers S n'est pas supposé injectif ; R intersection q doit être compris comme l'image réciproque de q. C'est une contraction, pas une nouvelle inclusion d'anneaux. La notation source reste intacte et n'est pas comptée comme une nouvelle découverte.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Témoin conservé.

## Contrôles exacts

Les 629 régions mathématiques du lot concordent après deux exceptions exactes de texte français, comportant quatre substitutions de mots. Les 4 357 régions du préfixe concordent avec seize exceptions exactes au total. La comparaison brute sans exceptions est fausse ; aucun masque général du contenu mathématique n’est utilisé.

La clé Lam-Reyes est conservée. Le titre optionnel Chevalley’s Theorem devient Théorème de Chevalley ; il est explicitement vérifié séparément. Les labels, références, environnements, contrôles TeX et items concordent. Les régions mathématiques du fichier cible entier ne changent pas par rapport au lot précédent.

Le retour inverse retrouve exactement le lot précédent puis le témoin français publié. Les 201 paires couvrent le préfixe sans lacune ni chevauchement ; la partie antérieure et le suffixe non relu sont inchangés. Ces contrôles de structure ne remplacent pas la comparaison sémantique documentée ci-dessus.

Prochaine lecture : Anneaux noethériens, anglais L5980 / français L5960. Aucun nouveau PDF, aucune publication ni certification globale du chapitre ou de l’édition ne sont revendiqués.

