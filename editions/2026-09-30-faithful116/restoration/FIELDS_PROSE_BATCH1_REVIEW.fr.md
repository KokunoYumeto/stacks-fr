# Chapitre 9 — Corps : première lecture continue de fidélité

**Sept premières sections entièrement comparées, source lignes 1–600. Le chapitre entier reste à relire ; cette copie n’est ni reconstruite ni publiée.**

[LaTeX de travail](staged/fr/009_fields.prose-batch1.fr.tex) · [Validation](FIELDS_PROSE_BATCH1_VALIDATION.json) · [Paires et décisions](FIELDS_PROSE_BATCH1_CHOICES.json) · [Occurrences](FIELDS_PROSE_BATCH1_OCCURRENCES.json) · [Dossier historique conservé](FIELDS_REVIEW.fr.md)

## Réparation réellement effectuée

La traduction avait transformé une liste de noms anglais en règle éditoriale interdisant certains calques. Cette règle ne figure pas dans Stacks. Le terme français est conservé et les trois dénominations sources sont rendues explicitement comme noms anglais. Aucun énoncé, hypothèse ou argument mathématique n'est modifié par cette réparation.

Avant :

```tex
Le corps $F$ est appelé le {\it corps des fractions} de $A$ ; les calques
{\it corps quotient} et {\it corps de fractions} ne seront pas employés.
```

Après :

```tex
Le corps $F$ est appelé le corps des fractions de $A$ (en anglais
{\it quotient field}, {\it field of fractions} ou {\it fraction field}).
```

Une intervention éditoriale française est retirée : la source donne trois noms anglais et ne déclare pas certains noms interdits. La désignation française attestée est maintenue ; les trois noms originaux sont explicitement identifiés comme anglais. Le plongement, les classes de fractions, l'universalité, l'unicité et la justification du dénominateur sont tous conservés. La parenthèse est un alignement lexical, non une amélioration mathématique.

Solutions écartées :

- Conserver l'interdiction des noms : aucun appui dans le passage officiel.
- Énumérer les trois calques comme trois appellations françaises usuelles : les passages consultés ne justifient pas cette présentation.
- Ne garder que le nom français sans rendre compte de la liste : cela perd l'information nomenclaturale explicite de la source.

## Périmètre et preuves

Le lot contient la partie liminaire et 38 intervalles d'étiquettes, soit 39 paires disjointes. Toutes les introductions, définitions, preuves, remarques, transitions et l'exercice de ces sept sections ont été lus en regard. Les frontières d'étiquettes sont des repères de fichier et non nécessairement des fins de phrase. Les sept sections vont de l'introduction aux extensions finies ; la prochaine est Extensions algébriques, ligne source 601.

Les 19 restaurations historiques et les quatre choix idiomatiques ne sont pas refaits. Le retour inverse du nouveau changement puis des anciens retrouve exactement la copie publique préservée. La suite du chapitre après la frontière est identique à la copie de travail précédente. L'exception mathématique historique — un indice i explicité dans une ellipse française — reste unique et inchangée ; elle se situe hors de ce lot. Les contrôles mécaniques ne prouvent pas seuls la fidélité de la prose.

## Canon réellement consulté

Marc Reversat et Benoît Zhang, [Cours de théorie des corps](https://www.math.univ-toulouse.fr/~reversat/galois.pdf), 24 mars 2003. Introduction du chapitre 1 et §§1.1–1.2 ; pages imprimées 1–5, pages PDF 9–13. Lecture textuelle locale ; page imprimée 3 également rendue et inspectée. Le début de §1.3 est visible mais ne certifie pas la suite du chapitre Stacks.

Témoin téléchargé : 816199 octets, SHA-256 `73A1D0DCD0B7F11625293615E693B198C0C33BAE3A57C78A705153CE33942E8A`. [Identité locale](canon-consulted/fr-fields/READBACK.json).

La remarque 1.1.8 appuie le nom français du corps des fractions ; les définitions 1.1.4 et 1.1.11 distinguent degré fini et génération finie ; la définition 1.2.3 fixe le nom du sous-corps premier. Ces passages ne justifient ni une convention éditoriale de noms interdits ni tous les mots de la traduction. La consultation est rétrospective.

## Points ouverts à une relecture spécialisée, sans attente d’approbation

- **Présentation des synonymes anglais** : la solution adoptée conserve l’information source avec un nom français explicite. Le choix stylistique reste réversible.
- **De nature morphique** : sens catégorique conservé en contexte, mais tournure non attestée dans le canon consulté ; à discuter stylistiquement, sans la déclarer erreur mathématique.
- **Conventions du texte source** : la connexité de la surface de Riemann, la convention sur le diviseur de zéro et la restriction au polynôme non nul de degré minimal ne sont pas ajoutées à la traduction.
- **Portée de la preuve de multiplicativité** : les bases finies de la preuve ne conduisent pas à restreindre silencieusement l’énoncé général. Le raisonnement par pôles sur C et les détails de Zorn omis restent également dans leur portée originale.

## Règles et occurrences

### fraction-field

Nom français attesté ; les trois synonymes anglais de la source ne deviennent pas trois notions distinctes. Leur identification dans une parenthèse évite la déclaration éditoriale de noms interdits.

Occurrences repérées et relues : 7. Appui : Remarque 1.1.8, p.3.

### finitely-generated-field

Génération finie comme corps ; ne pas substituer la dimension finie, qui est une condition plus forte.

Occurrences repérées et relues : 3. Appui : Définition 1.1.11 et Remarque 1.1.12, p.4.

### finite-degree

Contrôle du degré vectoriel et du sens de fini ; degré du polynôme est distingué du degré d'extension dans les passages qui les égalent.

Occurrences repérées et relues : 22. Appui : Définition 1.1.4, p.2.

### prime-subfield

La caractéristique et le sous-corps premier sont liés sans être confondus ; les morphismes d'inclusion et le cas nul restent ceux de Stacks.

Occurrences repérées et relues : 8. Appui : §1.2, pp.4–5.

### generating-field

Vérifier le type d'objet à chaque occurrence : idéal, sous-corps ou sous-espace. La citation atteste l'usage pour les corps ; le type précis des autres occurrences vient du contexte officiel.

Occurrences repérées et relues : 15. Appui : Définition 1.1.6, p.3, et Définition 1.1.4, p.2.

### simple-monogenic

Engendrement par un élément explicitement défini dans Stacks. La distinction simple/monogène n'est pas attestée indépendamment dans le périmètre consulté ; maintien raisonné de l'usage existant, non certification bibliographique.

Occurrences repérées et relues : 3. Appui : contexte officiel seulement ; attestation externe non obtenue dans ce lot.

### categorical-prose

Sens vérifié dans l'énoncé et sa preuve : exactitude catégorique, scindement, projectivité. La formulation de nature morphique reste signalée comme stylistiquement discutable, sans faux appui bibliographique.

Occurrences repérées et relues : 3. Appui : contexte officiel seulement ; attestation externe non obtenue dans ce lot.

## Index complet des passages lus

### FR-FIELDS-B1-PROSE-0001

`frontmatter` — source 1–12, cible 1–12.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le titre Corps est conservé. Préambule et commandes de document ne changent pas ; les commentaires techniques ne sont pas du texte destiné au lecteur.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\input{preamble}

% OK, start here.
%
\begin{document}

\title{Fields}


\maketitle

\phantomsection
```

```tex
\input{preamble}

% OK, start here.
%
\begin{document}

\title{Corps}


\maketitle

\phantomsection
```

</details>

### FR-FIELDS-B1-PROSE-0002

`section-phantom` — source 13–18, cible 13–18.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L13) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Ancre, table des matières et titre Introduction sont conservés. Ce segment n'ajoute aucun contenu mathématique.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{section-phantom}

\tableofcontents


\section{Introduction}
```

```tex
\label{section-phantom}

\tableofcontents


\section{Introduction}
```

</details>

### FR-FIELDS-B1-PROSE-0003

`section-introduction` — source 19–41, cible 19–41.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L19) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Non-nullité du corps, inversibilité, deux idéaux et réduction de questions d'anneaux aux corps sont présents. Le corps résiduel reste le quotient par l'unique idéal maximal ; la réserve indiquant que le terme anneau local n'est pas encore défini est conservée. Aucune nouvelle hypothèse n'est insérée.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{section-introduction}

\noindent
In this chapter, we shall discuss the theory of fields. Recall that a
{\it field} is a nonzero ring in which all nonzero elements are invertible.
Equivalently, the only two ideals of a field are $(0)$ and $(1)$
since any nonzero element is a unit. Consequently fields will be the
simplest cases of much of the theory developed later.

\medskip\noindent
The theory of field extensions has a different feel from standard commutative
algebra since, for instance, any morphism of fields is injective. Nonetheless,
it turns out that questions involving rings can often be reduced to questions
about fields. For instance, any domain can be embedded in a field
(its quotient field), and any {\it local ring} (that is, a ring with a unique
maximal ideal; we have not defined this term yet) has associated to it its
residue field (that is, its quotient by the maximal ideal).
A knowledge of field extensions will thus be useful.




\section{Basic definitions}
```

```tex
\label{section-introduction}

\noindent
Dans ce chapitre, nous étudierons la théorie des corps. Rappelons qu'un
{\it corps} est un anneau non nul dans lequel tout élément non nul est inversible.
De manière équivalente, les deux seuls idéaux d'un corps sont $(0)$ et $(1)$,
puisque tout élément non nul est une unité. Les corps constitueront donc les
cas les plus simples d'une grande partie de la théorie développée ultérieurement.

\medskip\noindent
La théorie des extensions de corps présente un aspect différent de l'algèbre
commutative classique puisque, par exemple, tout morphisme de corps est injectif.
Il s'avère néanmoins que des questions portant sur les anneaux peuvent souvent
se ramener à des questions sur les corps. Par exemple, tout anneau intègre se plonge dans un corps
(son corps des fractions), et à tout {\it anneau local} (c'est-à-dire un anneau possédant un unique
idéal maximal ; nous n'avons pas encore défini ce terme) est associé son
corps résiduel (c'est-à-dire son quotient par l'idéal maximal).
La connaissance des extensions de corps sera donc utile.




\section{Définitions de base}
```

</details>

### FR-FIELDS-B1-PROSE-0004

`section-definitions` — source 42–49, cible 42–49.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L42) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

L'explication de l'ordre pédagogique des chapitres est conservée ; elle demeure attribuable à l'ouvrage source, non à un plan inventé par le traducteur.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{section-definitions}

\noindent
Because we have placed this chapter before the chapter discussing
commutative algebra we need to introduce some of the basic definitions
here before we discuss these in greater detail in the algebra chapters.

\begin{definition}
```

```tex
\label{section-definitions}

\noindent
Comme nous avons placé ce chapitre avant celui consacré à l'algèbre
commutative, nous devons introduire ici certaines définitions élémentaires
avant de les étudier plus en détail dans les chapitres d'algèbre.

\begin{definition}
```

</details>

### FR-FIELDS-B1-PROSE-0005

`definition-field` — source 50–60, cible 50–60.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L50) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le corps est un anneau non nul et tous ses éléments non nuls sont inversibles. Sous-corps garde les deux conditions de sous-anneau et de corps. La notation k* et son lien au groupe des unités de R sont inchangés.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{definition-field}
A {\it field} is a nonzero ring where every nonzero element is invertible.
Given a field a {\it subfield} is a subring that is itself a field.
\end{definition}

\noindent
For a field $k$, we write $k^*$ for the subset $k \setminus \{0\}$.
This generalizes the usual notation $R^*$ that refers to the group of
invertible elements in a ring $R$.

\begin{definition}
```

```tex
\label{definition-field}
Un {\it corps} est un anneau non nul dont tout élément non nul est inversible.
Étant donné un corps, un {\it sous-corps} est un sous-anneau qui est lui-même un corps.
\end{definition}

\noindent
Pour un corps $k$, nous notons $k^*$ le sous-ensemble $k \setminus \{0\}$.
Cette notation généralise la notation usuelle $R^*$ qui désigne le groupe des
éléments inversibles d'un anneau $R$.

\begin{definition}
```

</details>

### FR-FIELDS-B1-PROSE-0006

`definition-domain` — source 61–68, cible 61–68.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L61) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Anneau intègre correspond à integral domain. La variante domaine d'intégrité est conservée : elle n'ajoute pas une propriété. La formulation avec zéro comme seul diviseur de zéro reste celle du témoin anglais ; aucune convention corrective n'est importée.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{definition-domain}
A {\it domain} or an {\it integral domain} is a nonzero ring where $0$
is the only zerodivisor.
\end{definition}



\section{Examples of fields}
```

```tex
\label{definition-domain}
Un {\it anneau intègre}, ou un {\it domaine d'intégrité}, est un anneau non nul dans lequel $0$
est le seul diviseur de zéro.
\end{definition}



\section{Exemples de corps}
```

</details>

### FR-FIELDS-B1-PROSE-0007

`section-examples` — source 69–76, cible 69–76.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L69) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

L'équivalence entre quotient corps et idéal maximal est préservée, dans les deux sens. Le statut de rappel au lecteur est conservé.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{section-examples}

\noindent
To get started, let us begin by providing several examples of fields. The
reader should recall that if $R$ is a ring and $I \subset R$ an
ideal, then $R/I$ is a field precisely when $I$ is a maximal ideal.

\begin{example}[Rational numbers]
```

```tex
\label{section-examples}

\noindent
Pour commencer, donnons plusieurs exemples de corps. Le lecteur se rappellera
que, si $R$ est un anneau et $I \subset R$ un idéal, alors $R/I$ est un corps
si et seulement si $I$ est un idéal maximal.

\begin{example}[Nombres rationnels]
```

</details>

### FR-FIELDS-B1-PROSE-0008

`example-rational-numbers` — source 77–82, cible 77–82.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L77) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le nom corps des nombres rationnels et la notation Q désignent le même objet que la source ; aucune construction supplémentaire n'est ajoutée.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{example-rational-numbers}
The rational numbers form a field. It is called the
{\it field of rational numbers} and denoted $\mathbf{Q}$.
\end{example}

\begin{example}[Prime fields]
```

```tex
\label{example-rational-numbers}
Les nombres rationnels forment un corps. On l'appelle le
{\it corps des nombres rationnels} et on le note $\mathbf{Q}$.
\end{example}

\begin{example}[Corps premiers]
```

</details>

### FR-FIELDS-B1-PROSE-0009

`example-prime-field` — source 83–90, cible 83–90.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L83) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le nombre premier, l'idéal maximal et le cardinal p sont tous conservés. Corps premiers au pluriel traduit le titre de l'exemple, sans déclarer tous les corps finis premiers.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{example-prime-field}
If $p$ is a prime number, then $\mathbf{Z}/(p)$ is a field, denoted
$\mathbf{F}_p$. Indeed, $(p)$ is a
maximal ideal in $\mathbf{Z}$. Thus, fields may be finite: $\mathbf{F}_p$
contains $p$ elements.
\end{example}

\begin{example}
```

```tex
\label{example-prime-field}
Si $p$ est un nombre premier, alors $\mathbf{Z}/(p)$ est un corps, noté
$\mathbf{F}_p$. En effet, $(p)$ est un
idéal maximal de $\mathbf{Z}$. Ainsi, un corps peut être fini : $\mathbf{F}_p$
contient $p$ éléments.
\end{example}

\begin{example}
```

</details>

### FR-FIELDS-B1-PROSE-0010

`example-quotient-polymial-ring` — source 91–103, cible 91–103.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L91) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Anneau principal rend principal ideal domain dans le registre commutatif. La définition du polynôme irréductible, l'inclusion de k et la construction des complexes sont conservées. L'étiquette historiquement mal orthographiée reste inchangée.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{example-quotient-polymial-ring}
In a principal ideal domain, an ideal generated by an irreducible element
is maximal. Now, if $k$ is a field, then the polynomial ring $k[x]$ is a
principal ideal domain. It follows that if $P \in k[x]$ is an irreducible
polynomial (that is, a nonconstant polynomial
that does not admit a factorization into terms of smaller degrees), then
$k[x]/(P)$ is a field. It contains a copy of $k$ in a natural way.
This is a very general way of constructing fields. For instance, the
complex numbers $\mathbf{C}$
can be constructed as $\mathbf{R}[x]/(x^2 + 1)$.
\end{example}

\begin{example}[Quotient fields]
```

```tex
\label{example-quotient-polymial-ring}
Dans un anneau principal, tout idéal engendré par un élément irréductible
est maximal. Or, si $k$ est un corps, l'anneau de polynômes $k[x]$ est un
anneau principal. Il s'ensuit que, si $P \in k[x]$ est un polynôme irréductible
(c'est-à-dire un polynôme non constant
qui n'admet pas de factorisation en facteurs de degrés plus petits), alors
$k[x]/(P)$ est un corps. Il contient naturellement une copie de $k$.
C'est une méthode très générale pour construire des corps. Par exemple, les
nombres complexes $\mathbf{C}$
peuvent être construits sous la forme $\mathbf{R}[x]/(x^2 + 1)$.
\end{example}

\begin{example}[Corps des fractions]
```

</details>

### FR-FIELDS-B1-PROSE-0011

`example-quotient-field` — source 104–126, cible 104–126.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L104) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Une intervention éditoriale française est retirée : la source donne trois noms anglais et ne déclare pas certains noms interdits. La désignation française attestée est maintenue ; les trois noms originaux sont explicitement identifiés comme anglais. Le plongement, les classes de fractions, l'universalité, l'unicité et la justification du dénominateur sont tous conservés. La parenthèse est un alignement lexical, non une amélioration mathématique.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{example-quotient-field}
Recall that, given a domain $A$, there is an imbedding $A \to F$ into a
field $F$ constructed from $A$ in exactly the same manner that
$\mathbf{Q}$ is constructed from $\mathbf{Z}$. Formally the elements
of $F$ are (equivalence classes of) fractions $a/b$,
$a, b \in A$, $b \not = 0$. As usual $a/b = a'/b'$ if and only if $ab' = ba'$.
The field $F$ is called the {\it quotient field}, or {\it field of fractions},
or {\it fraction field} of $A$.
The quotient field has the following universal property: given an
injective ring map $\varphi : A \to K$ to a field $K$, there is a unique
map $\psi : F \to K$ making
$$
\xymatrix{
F \ar[r]_\psi & K \\
A \ar[u] \ar[ru]_\varphi
}
$$
commute. Indeed, it is clear how to define such a map: we set
$\psi(a/b) = \varphi(a)\varphi(b)^{-1}$ where injectivity of $\varphi$
assures that $\varphi(b) \not = 0$ if $ b \not = 0$.
\end{example}

\begin{example}[Field of rational functions]
```

```tex
\label{example-quotient-field}
Rappelons qu'étant donné un anneau intègre $A$, il existe un plongement $A \to F$ dans un
corps $F$ construit à partir de $A$ exactement de la même manière que
$\mathbf{Q}$ est construit à partir de $\mathbf{Z}$. Formellement, les éléments
de $F$ sont des fractions $a/b$ (ou, plus précisément, leurs classes d'équivalence),
$a, b \in A$, $b \not = 0$. Comme d'habitude, $a/b = a'/b'$ si et seulement si $ab' = ba'$.
Le corps $F$ est appelé le corps des fractions de $A$ (en anglais
{\it quotient field}, {\it field of fractions} ou {\it fraction field}).
Le corps des fractions possède la propriété universelle suivante : pour tout
morphisme injectif d'anneaux $\varphi : A \to K$ vers un corps $K$, il existe un unique
morphisme $\psi : F \to K$ qui rende le diagramme
$$
\xymatrix{
F \ar[r]_\psi & K \\
A \ar[u] \ar[ru]_\varphi
}
$$
commutatif. En effet, la façon de définir un tel morphisme est claire : on pose
$\psi(a/b) = \varphi(a)\varphi(b)^{-1}$, l'injectivité de $\varphi$
assurant que $\varphi(b) \not = 0$ si $ b \not = 0$.
\end{example}

\begin{example}[Corps des fonctions rationnelles]
```

</details>

### FR-FIELDS-B1-PROSE-0012

`example-field-of-rational-functions` — source 127–134, cible 127–134.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L127) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Fonctions rationnelles et corps des fractions du polynôme désignent le même objet ici. La condition de dénominateur non nul et la relation d'équivalence restent présentes ; la variante fractions rationnelles est également attestée mais n'impose aucun changement.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{example-field-of-rational-functions}
If $k$ is a field, then we can consider the field $k(x)$ of rational
functions over $k$. This is the quotient field of the polynomial ring
$k[x]$. In other words, it is the set of quotients $F/G$ for
$F, G \in k[x]$, $G \not = 0$ with the obvious equivalence relation.
\end{example}

\begin{example}
```

```tex
\label{example-field-of-rational-functions}
Si $k$ est un corps, on peut considérer le corps $k(x)$ des fonctions
rationnelles sur $k$. C'est le corps des fractions de l'anneau de polynômes
$k[x]$. Autrement dit, c'est l'ensemble des quotients $F/G$ avec
$F, G \in k[x]$, $G \not = 0$, muni de la relation d'équivalence évidente.
\end{example}

\begin{example}
```

</details>

### FR-FIELDS-B1-PROSE-0013

`example-field-of-meromorphic-functions` — source 135–147, cible 135–147.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L135) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le passage entier, y compris l'inversion d'une fonction non nulle et l'exemple de la sphère, est conservé. On n'ajoute pas une condition de connexité absente du texte de Stacks ; la convention sur surface de Riemann appartient à la source.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{example-field-of-meromorphic-functions}
Let $X$ be a Riemann surface. Let $\mathbf{C}(X)$ denote the
set of meromorphic functions on $X$. Then $\mathbf{C}(X)$ is a ring under
multiplication and addition of functions. It turns out that in fact
$\mathbf{C}(X)$ is a field. Namely, if a nonzero function $f(z)$ is
meromorphic, so is $1/f(z)$. For example, let $S^2$ be the Riemann
sphere; then we know from complex analysis that the ring of meromorphic
functions $\mathbf{C}(S^2)$ is the field of rational functions $\mathbf{C}(z)$.
\end{example}



\section{Vector spaces}
```

```tex
\label{example-field-of-meromorphic-functions}
Soit $X$ une surface de Riemann. Notons $\mathbf{C}(X)$
l'ensemble des fonctions méromorphes sur $X$. Alors $\mathbf{C}(X)$ est un anneau pour
la multiplication et l'addition des fonctions. Il s'avère qu'en fait
$\mathbf{C}(X)$ est un corps. En effet, si une fonction non nulle $f(z)$ est
méromorphe, il en va de même de $1/f(z)$. Par exemple, soit $S^2$ la sphère
de Riemann ; l'analyse complexe nous apprend que l'anneau des fonctions méromorphes
$\mathbf{C}(S^2)$ est le corps des fonctions rationnelles $\mathbf{C}(z)$.
\end{example}



\section{Espaces vectoriels}
```

</details>

### FR-FIELDS-B1-PROSE-0014

`section-vector-spaces` — source 148–154, cible 148–154.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L148) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le lien entre modules sur un corps et espaces vectoriels est conservé, sans confondre liberté et absence de coût ni ajouter une hypothèse de dimension finie.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{section-vector-spaces}

\noindent
One reason fields are so nice is that the theory of modules over fields
(i.e. vector spaces), is very simple.

\begin{lemma}
```

```tex
\label{section-vector-spaces}

\noindent
L'une des raisons pour lesquelles les corps sont si commodes est que la théorie des modules sur un corps
(c'est-à-dire des espaces vectoriels) est très simple.

\begin{lemma}
```

</details>

### FR-FIELDS-B1-PROSE-0015

`lemma-vector-space-is-free` — source 155–165, cible 155–165.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L155) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

L'énoncé est universel et la preuve utilise une base sans la supposer finie. L'isomorphisme a bien pour source l'espace vectoriel libre sur cette base et pour but V.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{lemma-vector-space-is-free}
If $k$ is a field, then every $k$-module is free.
\end{lemma}

\begin{proof}
Indeed, by linear algebra we know that a $k$-module (i.e. vector space)
$V$ has a {\it basis} $\mathcal{B} \subset V$, which defines an isomorphism
from the free vector space on $\mathcal{B}$ to $V$.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-vector-space-is-free}
Si $k$ est un corps, tout $k$-module est libre.
\end{lemma}

\begin{proof}
En effet, l'algèbre linéaire nous apprend qu'un $k$-module (c'est-à-dire un espace vectoriel)
$V$ possède une {\it base} $\mathcal{B} \subset V$, laquelle définit un isomorphisme
de l'espace vectoriel libre sur $\mathcal{B}$ vers $V$.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B1-PROSE-0016

`lemma-field-semi-simple` — source 166–189, cible 166–189.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L166) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Suite exacte scindée et module projectif conservent le sens du texte. On n'insère pas courte dans l'énoncé. La tournure de nature morphique est compréhensible grâce à l'explication catégorique qui suit ; elle reste stylistiquement discutable, sans attestation indépendante revendiquée ici. Les deux paragraphes de transition sont conservés.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{lemma-field-semi-simple}
Every exact sequence of modules over a field splits.
\end{lemma}

\begin{proof}
This follows from Lemma \ref{lemma-vector-space-is-free} as every vector
space is a projective module.
\end{proof}

\noindent
This is another reason why much of the theory in future chapters will not say
very much about fields, since modules behave in such a simple manner.
Note that Lemma \ref{lemma-field-semi-simple} is a statement about the
{\it category} of $k$-modules (for $k$ a field), because the notion of
exactness is inherently arrow-theoretic, i.e., makes use of purely categorical
notions, and can in fact be phrased within a so-called {\it abelian category}.

\medskip\noindent
Henceforth, since the study of modules over a field is linear algebra, and
since the ideal theory of fields is not very interesting, we shall study what
this chapter is really about: {\it extensions} of fields.


\section{The characteristic of a field}
```

```tex
\label{lemma-field-semi-simple}
Toute suite exacte de modules sur un corps est scindée.
\end{lemma}

\begin{proof}
Cela résulte du Lemme \ref{lemma-vector-space-is-free}, puisque tout espace
vectoriel est un module projectif.
\end{proof}

\noindent
C'est une autre raison pour laquelle une grande partie de la théorie des chapitres ultérieurs dira
peu de choses sur les corps, puisque les modules s'y comportent de manière si simple.
Notons que le Lemme \ref{lemma-field-semi-simple} est un énoncé portant sur la
{\it catégorie} des $k$-modules (où $k$ est un corps), car la notion
d'exactitude est intrinsèquement de nature morphique, c'est-à-dire qu'elle ne fait intervenir que des notions
catégoriques, et peut en fait se formuler dans ce que l'on appelle une {\it catégorie abélienne}.

\medskip\noindent
Désormais, puisque l'étude des modules sur un corps relève de l'algèbre linéaire et
que la théorie des idéaux d'un corps présente peu d'intérêt, nous étudierons le véritable
objet de ce chapitre : les {\it extensions} de corps.


\section{La caractéristique d’un corps}
```

</details>

### FR-FIELDS-B1-PROSE-0017

`section-more-fields` — source 190–224, cible 190–224.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L190) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Les sens des flèches sont vérifiés : Z est envoyé dans chaque anneau, et le corps premier est envoyé dans le corps étudié. Les cas noyau nul et noyau (p), le passage aux fractions et la minimalité sont conservés, sans confondre sous-anneau et quotient.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{section-more-fields}

\noindent
In the category of rings, there is an {\it initial object} $\mathbf{Z}$: any
ring $R$ has a map from $\mathbf{Z}$ into it in precisely one way. For fields,
there is no such initial object.
Nonetheless, there is a family of objects such that every field can be mapped
into in exactly one way by exactly one of them, and in no way by the others.

\medskip\noindent
Let $F$ be a field. Think of $F$ as a ring to get a ring map
$f : \mathbf{Z} \to F$. The image of this ring map is a domain
(as a subring of a field) hence the kernel of $f$ is a prime ideal
in $\mathbf{Z}$. Hence the kernel of $f$ is either $(0)$ or $(p)$ for
some prime number $p$.

\medskip\noindent
In the first case we see that $f$ is injective, and in this case
we think of $\mathbf{Z}$ as a subring of $F$. Moreover, since every
nonzero element of $F$ is invertible we see that it makes sense to
talk about $p/q \in F$ for $p, q \in \mathbf{Z}$ with $q \not = 0$.
Hence in this case we may and we do think of $\mathbf{Q}$ as a subring of $F$.
One can easily see that this is the smallest subfield of $F$ in this case.

\medskip\noindent
In the second case, i.e., when $\Ker(f) = (p)$ we see that
$\mathbf{Z}/(p) = \mathbf{F}_p$ is a subring of $F$. Clearly it is the
smallest subfield of $F$.

\medskip\noindent
Arguing in this way we see that every field contains a smallest subfield
which is either $\mathbf{Q}$ or finite equal to $\mathbf{F}_p$ for some
prime number $p$.

\begin{definition}
```

```tex
\label{section-more-fields}

\noindent
Dans la catégorie des anneaux, il existe un {\it objet initial} $\mathbf{Z}$ : tout
anneau $R$ reçoit un morphisme de $\mathbf{Z}$ d'une manière et d'une seule. Pour les corps,
il n'existe pas d'objet initial.
Il existe néanmoins une famille d'objets telle que tout corps reçoive d'une manière
unique un morphisme provenant d'exactement l'un d'entre eux, et aucun morphisme provenant des autres.

\medskip\noindent
Soit $F$ un corps. Considérons $F$ comme un anneau afin d'obtenir un morphisme d'anneaux
$f : \mathbf{Z} \to F$. L'image de ce morphisme d'anneaux est un anneau intègre
(en tant que sous-anneau d'un corps) ; le noyau de $f$ est donc un idéal premier
de $\mathbf{Z}$. Par conséquent, le noyau de $f$ est soit $(0)$, soit $(p)$ pour
un certain nombre premier $p$.

\medskip\noindent
Dans le premier cas, $f$ est injectif, et nous considérons alors
$\mathbf{Z}$ comme un sous-anneau de $F$. De plus, puisque tout
élément non nul de $F$ est inversible, il est légitime de
parler de $p/q \in F$ pour $p, q \in \mathbf{Z}$ avec $q \not = 0$.
Dans ce cas, nous pouvons donc considérer, et nous considérons, $\mathbf{Q}$ comme un sous-anneau de $F$.
On vérifie aisément que c'est alors le plus petit sous-corps de $F$.

\medskip\noindent
Dans le second cas, c'est-à-dire lorsque $\Ker(f) = (p)$, on voit que
$\mathbf{Z}/(p) = \mathbf{F}_p$ est un sous-anneau de $F$. C'est manifestement le
plus petit sous-corps de $F$.

\medskip\noindent
Ce raisonnement montre que tout corps contient un plus petit sous-corps,
qui est soit $\mathbf{Q}$, soit le corps fini $\mathbf{F}_p$ pour un certain
nombre premier $p$.

\begin{definition}
```

</details>

### FR-FIELDS-B1-PROSE-0018

`definition-characteristic` — source 225–237, cible 225–237.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L225) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Caractéristique nulle ou première et sous-corps premier restent distingués. Les deux inclusions conditionnelles sont présentes. L'égalité des caractéristiques pour un sous-corps est conservée.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{definition-characteristic}
The {\it characteristic} of a field $F$ is $0$ if
$\mathbf{Z} \subset F$, or is a prime $p$ if $p = 0$ in $F$.
The {\it prime subfield of $F$} is the smallest subfield of $F$
which is either $\mathbf{Q} \subset F$ if the characteristic is zero, or
$\mathbf{F}_p \subset F$ if the characteristic is $p > 0$.
\end{definition}

\noindent
It is easy to see that if $E \subset F$ is a subfield, then the
characteristic of $E$ is the same as the characteristic of $F$.

\begin{example}
```

```tex
\label{definition-characteristic}
La {\it caractéristique} d'un corps $F$ est $0$ si
$\mathbf{Z} \subset F$, et est un nombre premier $p$ si $p = 0$ dans $F$.
Le {\it sous-corps premier de $F$} est le plus petit sous-corps de $F$ ;
il s'agit soit de $\mathbf{Q} \subset F$ si la caractéristique est nulle, soit de
$\mathbf{F}_p \subset F$ si la caractéristique est $p > 0$.
\end{definition}

\noindent
Il est facile de voir que, si $E \subset F$ est un sous-corps, la
caractéristique de $E$ est la même que celle de $F$.

\begin{example}
```

</details>

### FR-FIELDS-B1-PROSE-0019

`example-characteristic` — source 238–243, cible 238–243.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L238) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Les deux valeurs de caractéristique sont inchangées. La transition au chapitre des extensions ne formule aucun nouveau résultat.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{example-characteristic}
The characteristic of $\mathbf{F}_p$ is $p$, and that of $\mathbf{Q}$ is $0$.
\end{example}


\section{Field extensions}
```

```tex
\label{example-characteristic}
La caractéristique de $\mathbf{F}_p$ est $p$, et celle de $\mathbf{Q}$ est $0$.
\end{example}


\section{Extensions de corps}
```

</details>

### FR-FIELDS-B1-PROSE-0020

`section-extensions` — source 244–253, cible 244–253.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L244) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

L'analogie avec les algèbres sur un anneau fixé et le caractère relatif de l'étude sont conservés ; il s'agit d'un commentaire d'exposition, non d'une nouvelle assertion d'équivalence de catégories.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{section-extensions}

\noindent
In general, though, we are interested not so much in fields by themselves but
in field {\it extensions}. This is perhaps analogous to studying not rings
but {\it algebras} over a fixed ring.
The nice thing for fields is that the notion of a ``field over another field''
just recovers the notion of a field extension, by the next result.

\begin{lemma}
```

```tex
\label{section-extensions}

\noindent
En général, cependant, ce ne sont pas tant les corps eux-mêmes qui nous intéressent que leurs
{\it extensions}. Cette démarche est peut-être analogue à celle qui consiste à étudier non les anneaux,
mais les {\it algèbres} sur un anneau fixé.
Dans le cas des corps, la notion de ``corps sur un autre corps''
redonne simplement celle d'extension de corps, comme le montre le résultat suivant.

\begin{lemma}
```

</details>

### FR-FIELDS-B1-PROSE-0021

`lemma-field-maps-injective` — source 254–265, cible 254–265.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L254) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le destinataire R reste non nul. La preuve par contradiction conserve l'élément non nul du noyau, son inverse et la conséquence 1=0 ; aucune hypothèse d'injectivité n'est présupposée.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{lemma-field-maps-injective}
If $F$ is a field and $R$ is a nonzero ring, then any ring homomorphism
$\varphi : F \to R$ is injective.
\end{lemma}

\begin{proof}
Indeed, let $a \in \Ker(\varphi)$ be a nonzero element. Then we have
$\varphi(1) = \varphi(a^{-1} a) = \varphi(a^{-1}) \varphi(a) = 0$.
Thus $1 = \varphi(1) = 0$ and $R$ is the zero ring.
\end{proof}

\begin{definition}
```

```tex
\label{lemma-field-maps-injective}
Si $F$ est un corps et $R$ un anneau non nul, alors tout homomorphisme d'anneaux
$\varphi : F \to R$ est injectif.
\end{lemma}

\begin{proof}
En effet, soit $a \in \Ker(\varphi)$ un élément non nul. On a alors
$\varphi(1) = \varphi(a^{-1} a) = \varphi(a^{-1}) \varphi(a) = 0$.
Ainsi $1 = \varphi(1) = 0$, et $R$ est l'anneau nul.
\end{proof}

\begin{definition}
```

</details>

### FR-FIELDS-B1-PROSE-0022

`definition-extension` — source 266–298, cible 266–298.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L266) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

L'inclusion de corps définit l'extension, puis le texte explique l'abus consistant à identifier via une injection. Les morphismes de la catégorie restent des morphismes de k-algèbres. Le diagramme et les orientations sont identiques.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{definition-extension}
If $F$ is a field contained in a field $E$, then $E$ is said
to be a {\it field extension} of $F$. We shall write $E/F$ to indicate
that $E$ is an extension of $F$.
\end{definition}

\noindent
So if $F, F'$ are fields, and $F \to F'$ is any ring-homomorphism, we see by
Lemma \ref{lemma-field-maps-injective} that it is injective, and $F'$ can be
regarded as an extension of $F$, by a slight abuse of language. Alternatively,
a field extension of $F$ is just an $F$-algebra that happens to be a field.
This is completely different than the situation for general rings, since a
ring homomorphism is not necessarily injective.

\medskip\noindent
Let $k$ be a field. There is a {\it category} of field extensions of $k$.
An object of this category is an extension $E/k$, that is a
(necessarily injective) morphism of fields
$$
k \to E,
$$
while a morphism between extensions $E/k$ and $E'/k$ is a $k$-algebra
morphism $E \to E'$; alternatively, it is a commutative diagram
$$
\xymatrix{
E \ar[rr] & & E' \\
& k \ar[ru] \ar[lu] &
}
$$
The set of morphisms from $E \to E'$ in the category of extensions of $k$
will be denoted by $\Mor_k(E, E')$.

\begin{definition}
```

```tex
\label{definition-extension}
Si $F$ est un corps contenu dans un corps $E$, on dit que $E$ est
une {\it extension de corps} de $F$. Nous écrirons $E/F$ pour indiquer
que $E$ est une extension de $F$.
\end{definition}

\noindent
Ainsi, si $F, F'$ sont des corps et $F \to F'$ un homomorphisme d'anneaux quelconque, le
Lemme \ref{lemma-field-maps-injective} montre qu'il est injectif, et $F'$ peut être
considéré comme une extension de $F$, par un léger abus de langage. De façon équivalente,
une extension de corps de $F$ n'est autre qu'une $F$-algèbre qui est un corps.
La situation est entièrement différente pour les anneaux généraux, puisqu'un
homomorphisme d'anneaux n'est pas nécessairement injectif.

\medskip\noindent
Soit $k$ un corps. Il existe une {\it catégorie} des extensions de corps de $k$.
Un objet de cette catégorie est une extension $E/k$, c'est-à-dire un
morphisme de corps (nécessairement injectif)
$$
k \to E,
$$
tandis qu'un morphisme entre les extensions $E/k$ et $E'/k$ est un morphisme de
$k$-algèbres $E \to E'$ ; de façon équivalente, c'est un diagramme commutatif
$$
\xymatrix{
E \ar[rr] & & E' \\
& k \ar[ru] \ar[lu] &
}
$$
L'ensemble des morphismes $E \to E'$ dans la catégorie des extensions de $k$
sera noté $\Mor_k(E, E')$.

\begin{definition}
```

</details>

### FR-FIELDS-B1-PROSE-0023

`definition-tower` — source 299–308, cible 299–308.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L299) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Tour traduit la suite d'extensions emboîtées dans le même ordre. Ce mot n'implique pas par lui-même une finitude des degrés.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{definition-tower}
A {\it tower} of fields $E_n/E_{n - 1}/\ldots/E_0$ consists of a sequence of
extensions of fields
$E_n/E_{n - 1}$, $E_{n - 1}/E_{n - 2}$, $\ldots$, $E_1/E_0$.
\end{definition}

\noindent
Let us give a few examples of field extensions.

\begin{example}
```

```tex
\label{definition-tower}
Une {\it tour} de corps $E_n/E_{n - 1}/\ldots/E_0$ consiste en une suite
d'extensions de corps
$E_n/E_{n - 1}$, $E_{n - 1}/E_{n - 2}$, $\ldots$, $E_1/E_0$.
\end{definition}

\noindent
Donnons quelques exemples d'extensions de corps.

\begin{example}
```

</details>

### FR-FIELDS-B1-PROSE-0024

`example-monogenic-extension` — source 309–315, cible 309–315.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L309) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le quotient par un polynôme irréductible est considéré comme k-algèbre, puis extension. Le renvoi antérieur et l'irréductibilité sont conservés.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{example-monogenic-extension}
Let $k$ be a field, and $P \in k[x]$ an irreducible polynomial. We have
seen that $k[x]/(P)$ is a field (Example \ref{example-quotient-polymial-ring}).
Since it is also a $k$-algebra in the obvious way, it is an extension of $k$.
\end{example}

\begin{example}
```

```tex
\label{example-monogenic-extension}
Soient $k$ un corps et $P \in k[x]$ un polynôme irréductible. Nous avons
vu que $k[x]/(P)$ est un corps (Exemple \ref{example-quotient-polymial-ring}).
Comme c'est aussi une $k$-algèbre de façon évidente, il s'agit d'une extension de $k$.
\end{example}

\begin{example}
```

</details>

### FR-FIELDS-B1-PROSE-0025

`example-field-of-meromorphic-functions-extension-C` — source 316–333, cible 316–333.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L316) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Les constantes sont bien holomorphes, donc méromorphes. Le paragraphe suivant construit le sous-corps engendré par intersection puis par opérations élémentaires finies ; les objets k, S et F ne sont pas permutés.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{example-field-of-meromorphic-functions-extension-C}
If $X$ is a Riemann surface, then the field of meromorphic functions
$\mathbf{C}(X)$ (Example \ref{example-field-of-meromorphic-functions})
is an extension field of $\mathbf{C}$, because any element of $\mathbf{C}$
induces a meromorphic --- indeed, holomorphic --- constant function on $X$.
\end{example}

\noindent
Let $F/k$ be a field extension. Let $S \subset F$ be any subset.
Then there is a {\it smallest} subextension of $F$ (that is, a subfield of
$F$ containing $k$) that contains $S$. To see this, consider the family of
subfields of $F $ containing $S$ and $k$, and take their intersection; one
checks that this is a field. By a standard argument one shows, in fact, that
this is the set of elements of $F$ that can be obtained via a finite number
of elementary algebraic operations (addition, multiplication, subtraction,
and division) involving elements of $k$ and $S$.

\begin{definition}
```

```tex
\label{example-field-of-meromorphic-functions-extension-C}
Si $X$ est une surface de Riemann, le corps des fonctions méromorphes
$\mathbf{C}(X)$ (Exemple \ref{example-field-of-meromorphic-functions})
est une extension de corps de $\mathbf{C}$, car tout élément de $\mathbf{C}$
définit sur $X$ une fonction constante méromorphe --- et même holomorphe.
\end{example}

\noindent
Soit $F/k$ une extension de corps. Soit $S \subset F$ un sous-ensemble quelconque.
Il existe alors une {\it plus petite} sous-extension de $F$ (c'est-à-dire un sous-corps de
$F$ contenant $k$) qui contienne $S$. Pour le voir, considérons la famille des
sous-corps de $F $ contenant $S$ et $k$, puis prenons leur intersection ; on
vérifie qu'il s'agit d'un corps. Un argument classique montre en fait que
c'est l'ensemble des éléments de $F$ que l'on peut obtenir au moyen d'un nombre fini
d'opérations algébriques élémentaires (addition, multiplication, soustraction
et division) portant sur des éléments de $k$ et de $S$.

\begin{definition}
```

</details>

### FR-FIELDS-B1-PROSE-0026

`definition-generated-by` — source 334–347, cible 334–347.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L334) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Engendrer une extension est distingué de l'engendrement d'un espace vectoriel. De type fini signifie un ensemble fini de générateurs de corps, et non une extension de degré fini. Le cas singleton et l'exemple complexe sont conservés.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{definition-generated-by}
Let $k$ be a field. If $F/k$ is an extension of fields and
$S \subset F$, we write $k(S)$ for the smallest subfield of $F$
containing $k$ and $S$. We will say that $S$ {\it generates the
field extension} $k(S)/k$. If $S = \{\alpha\}$ is a singleton, then we
write $k(\alpha)$ instead of $k(\{\alpha\})$. We say $F/k$ is a
{\it finitely generated field extension} if there exists a
finite subset $S \subset F$ with $F = k(S)$.
\end{definition}

\noindent
For instance, $\mathbf{C}$ is generated by $i$ over $\mathbf{R}$.

\begin{exercise}
```

```tex
\label{definition-generated-by}
Soit $k$ un corps. Si $F/k$ est une extension de corps et
$S \subset F$, nous notons $k(S)$ le plus petit sous-corps de $F$
contenant $k$ et $S$. Nous dirons que $S$ {\it engendre
l'extension de corps} $k(S)/k$. Si $S = \{\alpha\}$ est un singleton, nous
écrirons $k(\alpha)$ au lieu de $k(\{\alpha\})$. On dit que $F/k$ est une
{\it extension de corps de type fini} s'il existe un
sous-ensemble fini $S \subset F$ tel que $F = k(S)$.
\end{definition}

\noindent
Par exemple, $\mathbf{C}$ est engendré par $i$ sur $\mathbf{R}$.

\begin{exercise}
```

</details>

### FR-FIELDS-B1-PROSE-0027

`exercise-C-not-countably-generated` — source 348–356, cible 348–356.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L348) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

L'exercice demande bien l'absence d'un ensemble dénombrable de générateurs sur Q, et non seulement l'absence d'un ensemble fini. Aucune solution n'a été ajoutée.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{exercise-C-not-countably-generated}
Show that $\mathbf{C}$ does not have a countable set of generators over
$\mathbf{Q}$.
\end{exercise}

\noindent
Let us now classify extensions generated by one element.

\begin{lemma}[Classification of simple extensions]
```

```tex
\label{exercise-C-not-countably-generated}
Montrer que $\mathbf{C}$ ne possède pas de famille dénombrable de générateurs sur
$\mathbf{Q}$.
\end{exercise}

\noindent
Classifions maintenant les extensions engendrées par un élément.

\begin{lemma}[Classification des extensions simples]
```

</details>

### FR-FIELDS-B1-PROSE-0028

`lemma-field-extension-generated-by-one-element` — source 357–394, cible 357–394.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L357) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Simple signifie engendrée par un élément dans ce contexte. Les deux cas du noyau, le passage au quotient ou aux fractions et la surjectivité sont intégralement conservés. La condition portant sur Q(alpha) est inchangée ; aucune hypothèse algébrique n'est imposée au cas rationnel.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{lemma-field-extension-generated-by-one-element}
If a field extension $F/k$ is generated by one element, then it is
$k$-isomorphic either to the rational function field $k(t)/k$ or to one
of the extensions $k[t]/(P)$ for $P \in k[t]$ irreducible.
\end{lemma}

\noindent
We will see that many of the most important cases of field extensions are
generated by one element, so this is actually useful.

\begin{proof}
Let $\alpha \in F$ be such that $F = k(\alpha)$; by assumption, such an
$\alpha$ exists. There is a morphism of rings
$$
k[t] \to F
$$
sending the indeterminate $t$ to $\alpha$. The image is a domain, so the
kernel is a prime ideal. Thus, it is either $(0)$ or $(P)$ for $P \in k[t]$
irreducible.

\medskip\noindent
If the kernel is $(P)$ for $P \in k[t]$ irreducible, then the map factors
through $k[t]/(P)$, and induces a morphism of fields $k[t]/(P) \to F$. Since
the image contains $\alpha$, we see easily that the map is surjective, hence
an isomorphism. In this case, $k[t]/(P) \simeq F$.

\medskip\noindent
If the kernel is trivial, then we have an injection $k[t] \to F$.
One may thus define a morphism of the quotient field $k(t)$ into $F$; given a
quotient $R(t)/Q(t)$ with $R(t), Q(t) \in k[t]$, we map this to
$R(\alpha)/Q(\alpha)$. The hypothesis that $k[t] \to F$ is injective implies
that $Q(\alpha) \neq 0$ unless $Q$ is the zero polynomial.
The quotient field of $k[t]$ is the rational function field $k(t)$, so we get
a morphism $k(t) \to F$
whose image contains $\alpha$. It is thus surjective, hence an isomorphism.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-field-extension-generated-by-one-element}
Si une extension de corps $F/k$ est engendrée par un élément, alors elle est
$k$-isomorphe soit au corps des fonctions rationnelles $k(t)/k$, soit à l'une
des extensions $k[t]/(P)$, où $P \in k[t]$ est irréductible.
\end{lemma}

\noindent
Nous verrons que bon nombre des cas les plus importants d'extensions de corps sont
engendrés par un élément ; ce résultat est donc effectivement utile.

\begin{proof}
Soit $\alpha \in F$ tel que $F = k(\alpha)$ ; par hypothèse, un tel
$\alpha$ existe. Il existe un morphisme d'anneaux
$$
k[t] \to F
$$
qui envoie l'indéterminée $t$ sur $\alpha$. Son image est un anneau intègre, donc son
noyau est un idéal premier. Celui-ci est donc soit $(0)$, soit $(P)$ pour un $P \in k[t]$
irréductible.

\medskip\noindent
Si le noyau est $(P)$ pour un $P \in k[t]$ irréductible, le morphisme se factorise
par $k[t]/(P)$ et induit un morphisme de corps $k[t]/(P) \to F$. Puisque
l'image contient $\alpha$, on voit aisément que ce morphisme est surjectif, donc
est un isomorphisme. Dans ce cas, $k[t]/(P) \simeq F$.

\medskip\noindent
Si le noyau est trivial, on obtient une injection $k[t] \to F$.
On peut donc définir un morphisme du corps des fractions $k(t)$ dans $F$ ; à un
quotient $R(t)/Q(t)$ avec $R(t), Q(t) \in k[t]$, on associe
$R(\alpha)/Q(\alpha)$. L'hypothèse selon laquelle $k[t] \to F$ est injectif implique
que $Q(\alpha) \neq 0$, sauf si $Q$ est le polynôme nul.
Le corps des fractions de $k[t]$ est le corps des fonctions rationnelles $k(t)$ ; on obtient donc
un morphisme $k(t) \to F$
dont l'image contient $\alpha$. Il est par conséquent surjectif, donc est un isomorphisme.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B1-PROSE-0029

`lemma-common-extension-field` — source 395–428, cible 395–429.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L395) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

L'extension commune conserve les deux morphismes au-dessus de k. La preuve reste limitée au cas de type fini et signale l'argument de Zorn omis ; elle n'est pas présentée comme entièrement développée. Les deux constructions simples et la récurrence sur les générateurs sont conservées.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{lemma-common-extension-field}
Let $k$ be a field and let $E/k$ and $F/k$ be field extensions.
Then there exists a common field extension $M/k$, i.e., an extension
field such that there exist maps $E \to M$ and $F \to M$ of extensions of $k$.
\end{lemma}

\begin{proof}
We only prove this when $E$ is a finitely generated field extension
of $k$; the general case follows from this by a Zorn's lemma type argument
(details omitted).

\medskip\noindent
First, suppose that $E$ is a simple extension of $k$. By
Lemma \ref{lemma-field-extension-generated-by-one-element}
this means either $E = k(t)$ is the rational function field
or $E = k[t]/(P)$ for some irreducible polynomial $P \in k[t]$.
In the first case, we take $M = F(t)$ the rational function field
with obvious maps $E \to M$ and $F \to M$. In the second case, we
choose an irreducible factor $Q$ of the image of $P$ in $F[t]$
and we take $M = F[t]/(Q)$ with obvious maps $E \to M$ and $F \to M$.

\medskip\noindent
If $E = k(\alpha_1, \ldots, \alpha_n)$, then by induction on $n$
we can find an extension $M/k$ and maps $F \to M$ and
$k(\alpha_1, \ldots, \alpha_{n - 1}) \to M$. By the simple
case discussed in the previous paragraph,
we can find an extension $M'/k(\alpha_1, \ldots, \alpha_{n - 1})$
and maps $M \to M'$ and $k(\alpha_1, \ldots, \alpha_n) \to M'$.
Then $M'$ viewed as an extension of $k$ works.
\end{proof}



\section{Finite extensions}
```

```tex
\label{lemma-common-extension-field}
Soient $k$ un corps et $E/k$, $F/k$ des extensions de corps.
Il existe alors une extension de corps commune $M/k$, c'est-à-dire une extension
de corps telle qu'il existe des morphismes $E \to M$ et $F \to M$ d'extensions de $k$.
\end{lemma}

\begin{proof}
Nous ne démontrons ce résultat que lorsque $E$ est une extension de corps de type fini
de $k$ ; le cas général s'en déduit par un argument de type lemme de Zorn
(les détails sont omis).

\medskip\noindent
Supposons d'abord que $E$ soit une extension simple de $k$. D'après le
Lemme \ref{lemma-field-extension-generated-by-one-element},
cela signifie soit que $E = k(t)$ est le corps des fonctions rationnelles,
soit que $E = k[t]/(P)$ pour un certain polynôme irréductible $P \in k[t]$.
Dans le premier cas, prenons pour $M = F(t)$ le corps des fonctions rationnelles,
muni des morphismes évidents $E \to M$ et $F \to M$. Dans le second cas, nous
choisissons un facteur irréductible $Q$ de l'image de $P$ dans $F[t]$
et prenons $M = F[t]/(Q)$, muni des morphismes évidents $E \to M$ et $F \to M$.

\medskip\noindent
Si $E = k(\alpha_1, \ldots, \alpha_n)$, une récurrence sur $n$
permet de trouver une extension $M/k$ et des morphismes $F \to M$ et
$k(\alpha_1, \ldots, \alpha_{n - 1}) \to M$. En appliquant le cas simple
étudié au paragraphe précédent,
on trouve une extension $M'/k(\alpha_1, \ldots, \alpha_{n - 1})$
et des morphismes $M \to M'$ et $k(\alpha_1, \ldots, \alpha_n) \to M'$.
Alors $M'$, considéré comme une extension de $k$, convient.
\end{proof}




\section{Extensions finies}
```

</details>

### FR-FIELDS-B1-PROSE-0030

`section-finite-extensions` — source 429–435, cible 430–436.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L429) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

L'action scalaire est la multiplication dans F ; aucune propriété de cardinal fini n'est substituée à la structure vectorielle.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{section-finite-extensions}

\noindent
If $F/E$ is a field extension, then evidently $F$ is also a vector space
over $E$ (the scalar action is just multiplication in $F$).

\begin{definition}
```

```tex
\label{section-finite-extensions}

\noindent
Si $F/E$ est une extension de corps, alors $F$ est aussi, de manière évidente, un espace vectoriel
sur $E$ (l'action scalaire n'est autre que la multiplication dans $F$).

\begin{definition}
```

</details>

### FR-FIELDS-B1-PROSE-0031

`definition-degree` — source 436–443, cible 437–444.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L436) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le degré est la dimension vectorielle et fini qualifie le degré, pas le cardinal du corps. Cette distinction est contrôlée avec la définition française consultée.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{definition-degree}
Let $F/E$ be an extension of fields. The dimension of $F$ considered as an
$E$-vector space is called the {\it degree} of the extension and is
denoted $[F : E]$. If $[F : E] < \infty$ then $F$ is said to be a
{\it finite} extension of $E$.
\end{definition}

\begin{example}
```

```tex
\label{definition-degree}
Soit $F/E$ une extension de corps. La dimension de $F$, considéré comme un
$E$-espace vectoriel, est appelée le {\it degré} de l'extension et est
notée $[F : E]$. Si $[F : E] < \infty$, on dit que $F$ est une extension
{\it finie} de $E$.
\end{definition}

\begin{example}
```

</details>

### FR-FIELDS-B1-PROSE-0032

`example-C-over-R` — source 444–450, cible 445–451.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L444) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Base 1,i et degré deux sont conservés. Le corps complexe n'est pas décrit comme un ensemble fini.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{example-C-over-R}
The field $\mathbf{C}$ is a two dimensional vector space over $\mathbf{R}$
with basis $1, i$. Thus $\mathbf{C}$ is a finite extension of $\mathbf{R}$
of degree 2.
\end{example}

\begin{lemma}
```

```tex
\label{example-C-over-R}
Le corps $\mathbf{C}$ est un espace vectoriel de dimension deux sur $\mathbf{R}$,
de base $1, i$. Ainsi $\mathbf{C}$ est une extension finie de $\mathbf{R}$
de degré 2.
\end{example}

\begin{lemma}
```

</details>

### FR-FIELDS-B1-PROSE-0033

`lemma-finite-goes-up` — source 451–465, cible 452–466.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L451) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

L'hypothèse algébrique, bien que superflue pour cet argument, reste présente parce qu'elle figure dans la source. Le sens de la montée de finitude et la preuve très brève sont conservés.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{lemma-finite-goes-up}
Let $K/E/F$ be a tower of algebraic field extensions.
If $K$ is finite over $F$, then $K$ is finite over $E$.
\end{lemma}

\begin{proof}
Direct from the definition.
\end{proof}

\noindent
Let us now consider the degree in the most important special example, that
given by Lemma \ref{lemma-field-extension-generated-by-one-element}, in the
next two examples.

\begin{example}[Degree of a rational function field]
```

```tex
\label{lemma-finite-goes-up}
Soit $K/E/F$ une tour d'extensions algébriques de corps.
Si $K$ est fini sur $F$, alors $K$ est fini sur $E$.
\end{lemma}

\begin{proof}
Cela résulte directement de la définition.
\end{proof}

\noindent
Calculons maintenant le degré dans l'exemple particulier le plus important, celui
fourni par le Lemme \ref{lemma-field-extension-generated-by-one-element}, au moyen
des deux exemples suivants.

\begin{example}[Degré d'un corps de fonctions rationnelles]
```

</details>

### FR-FIELDS-B1-PROSE-0034

`example-degree-rational-function-field` — source 466–489, cible 467–490.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L466) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Les puissances indexées par Z et la famille de fractions ont le même rôle. Non dénombrable concerne la dimension. Le raisonnement par pôles est explicitement donné sur C dans la source ; il n'est ni complété ni généralisé par le traducteur. Le renvoi au Nullstellensatz est conservé.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{example-degree-rational-function-field}
If $k$ is any field, then the rational function field $k(t)$ is
{\it not} a finite extension. For example the elements
$\left\{t^n, n \in \mathbf{Z}\right\}$ are linearly independent over $k$.

\medskip\noindent
In fact, if $k$ is uncountable, then $k(t)$ is {\it uncountably} dimensional
as a $k$-vector space. To show this, we claim that the family of elements
$\{1/(t- \alpha), \alpha \in k\} \subset k(t)$ is linearly independent over
$k$. A nontrivial relation between them would lead to a contradiction: for
instance, if one works over $\mathbf{C}$, then this follows because
$\frac{1}{t-\alpha}$, when considered as a meromorphic function on
$\mathbf{C}$, has a pole at $\alpha$ and nowhere else.
Consequently any sum $\sum c_i \frac{1}{t - \alpha_i}$ for the $c_i \in k^*$,
and $\alpha_i \in k$ distinct, would have poles at each of the $\alpha_i$.
In particular, it could not be zero.

\medskip\noindent
Amusingly, this leads to a quick proof of the Hilbert Nullstellensatz over
the complex numbers. For a slightly more general result, see
Algebra, Theorem \ref{algebra-theorem-uncountable-nullstellensatz}.
\end{example}

\begin{lemma}
```

```tex
\label{example-degree-rational-function-field}
Si $k$ est un corps quelconque, le corps des fonctions rationnelles $k(t)$ n'est
{\it pas} une extension finie. Par exemple, les éléments
$\left\{t^n, n \in \mathbf{Z}\right\}$ sont linéairement indépendants sur $k$.

\medskip\noindent
En fait, si $k$ est non dénombrable, alors $k(t)$ est de dimension {\it non dénombrable}
comme $k$-espace vectoriel. Pour le montrer, affirmons que la famille d'éléments
$\{1/(t- \alpha), \alpha \in k\} \subset k(t)$ est linéairement indépendante sur
$k$. Une relation non triviale entre eux conduirait à une contradiction : par
exemple, si l'on travaille sur $\mathbf{C}$, cela résulte du fait que
$\frac{1}{t-\alpha}$, considéré comme une fonction méromorphe sur
$\mathbf{C}$, possède un pôle en $\alpha$ et nulle part ailleurs.
Par conséquent, toute somme $\sum c_i \frac{1}{t - \alpha_i}$, où les $c_i \in k^*$
et les $\alpha_i \in k$ sont distincts, aurait un pôle en chacun des $\alpha_i$.
Elle ne pourrait notamment pas être nulle.

\medskip\noindent
Fait amusant, ceci donne une démonstration rapide du Nullstellensatz de Hilbert sur
les nombres complexes. Pour un résultat légèrement plus général, voir
Algèbre, Théorème \ref{algebra-theorem-uncountable-nullstellensatz}.
\end{example}

\begin{lemma}
```

</details>

### FR-FIELDS-B1-PROSE-0035

`lemma-finite-finitely-generated` — source 490–503, cible 491–504.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L490) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le sens fini implique de type fini, et l'échec de la réciproque, sont conservés. La base vectorielle fournit des générateurs de corps. Aucun glissement vers un module de type fini n'est introduit.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{lemma-finite-finitely-generated}
A finite extension of fields is a finitely generated field extension.
The converse is not true.
\end{lemma}

\begin{proof}
Let $F/E$ be a finite extension of fields. Let $\alpha_1, \ldots, \alpha_n$
be a basis of $F$ as a vector space over $E$. Then
$F = E(\alpha_1, \ldots, \alpha_n)$ hence $F/E$ is a finitely generated
field extension. The converse is not true as follows from
Example \ref{example-degree-rational-function-field}.
\end{proof}

\begin{example}[Degree of a simple algebraic extension]
```

```tex
\label{lemma-finite-finitely-generated}
Toute extension finie de corps est une extension de corps de type fini.
La réciproque est fausse.
\end{lemma}

\begin{proof}
Soit $F/E$ une extension finie de corps. Soient $\alpha_1, \ldots, \alpha_n$
une base de $F$ comme espace vectoriel sur $E$. Alors
$F = E(\alpha_1, \ldots, \alpha_n)$ ; ainsi $F/E$ est une extension de corps
de type fini. La réciproque est fausse d'après
l'Exemple \ref{example-degree-rational-function-field}.
\end{proof}

\begin{example}[Degré d'une extension algébrique simple]
```

</details>

### FR-FIELDS-B1-PROSE-0036

`example-degree-simple-algebraic-extension` — source 504–510, cible 505–511.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L504) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Monogène est employé pour l'extension engendrée par la classe de t ; ce n'est pas un énoncé d'algèbre monogène pour des extensions transcendantes quelconques. Le degré annoncé et le polynôme irréductible sont inchangés. L'attestation externe de monogène n'est pas revendiquée dans les passages effectivement consultés de ce lot.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{example-degree-simple-algebraic-extension}
Consider a monogenic field extension $E/k$ of the form discussed in
Example \ref{example-monogenic-extension}.
In other words, $E = k[t]/(P)$ for $P \in k[t]$ an irreducible polynomial.
Then the degree $[E : k]$ is just the degree $d = \deg(P)$ of the
polynomial $P$. Indeed, say
\begin{equation}
```

```tex
\label{example-degree-simple-algebraic-extension}
Considérons une extension de corps monogène $E/k$ de la forme étudiée dans
l'Exemple \ref{example-monogenic-extension}.
Autrement dit, $E = k[t]/(P)$, où $P \in k[t]$ est un polynôme irréductible.
Alors le degré $[E : k]$ est simplement le degré $d = \deg(P)$ du
polynôme $P$. Écrivons en effet
\begin{equation}
```

</details>

### FR-FIELDS-B1-PROSE-0037

`equation-P` — source 511–541, cible 512–542.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L511) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Les deux directions de la preuve de base sont lues : indépendance par le degré, puis génération par récurrence. La restriction implicite au polynôme non nul de degré minimal n'est pas ajoutée à la phrase source. Le paragraphe sur les extensions quadratiques garde la condition non-carré et ne rajoute aucune restriction de caractéristique.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{equation-P}
P = a_d t^d + a_{d - 1} t^{d - 1} + \ldots + a_0.
\end{equation}
with $a_d \not = 0$. Then the images of $1, t, \ldots, t^{d - 1}$ in
$k[t]/(P)$ are linearly independent over $k$, because any relation involving
them would have degree strictly smaller than that of $P$, and $P$ is the
element of smallest degree in the ideal $(P)$.

\medskip\noindent
Conversely, the set $S = \{1, t, \ldots, t^{d - 1}\}$ (or more
properly their images) spans $k[t]/(P)$ as a vector space.
Indeed, we have by (\ref{equation-P}) that $a_d t^d$ lies in the span of $S$.
Since $a_d$ is invertible, we see that $t^d$ is in the span of $S$.
Similarly, the relation $t P(t) = 0$ shows that the image of $t^{d + 1}$
lies in the span of $\{1, t, \ldots, t^d\}$ --- by what was just shown, thus
in the span of $S$. Working upward inductively, we find
that the image of $t^n$ for $n \geq d$ lies in the span of $S$.
\end{example}

\noindent
This confirms the observation that $[\mathbf{C}: \mathbf{R}] = 2$, for
instance. More generally, if $k$ is a field, and $\alpha \in k$ is not a
square, then the irreducible polynomial $x^2 - \alpha \in k[x]$ allows one
to construct an extension $k[x]/(x^2 - \alpha)$ of degree two.
We shall write this as $k(\sqrt{\alpha})$. Such extensions will be called
{\it quadratic,} for obvious reasons.

\medskip\noindent
The basic fact about the degree is that it is {\it multiplicative in towers.}

\begin{lemma}[Multiplicativity]
```

```tex
\label{equation-P}
P = a_d t^d + a_{d - 1} t^{d - 1} + \ldots + a_0.
\end{equation}
avec $a_d \not = 0$. Les images de $1, t, \ldots, t^{d - 1}$ dans
$k[t]/(P)$ sont alors linéairement indépendantes sur $k$, car toute relation entre
elles serait de degré strictement inférieur à celui de $P$, alors que $P$ est
l'élément de plus petit degré de l'idéal $(P)$.

\medskip\noindent
Réciproquement, l'ensemble $S = \{1, t, \ldots, t^{d - 1}\}$ (ou, plus
précisément, l'ensemble de leurs images) engendre $k[t]/(P)$ comme espace vectoriel.
En effet, il résulte de (\ref{equation-P}) que $a_d t^d$ appartient au sous-espace engendré par $S$.
Comme $a_d$ est inversible, on voit que $t^d$ appartient au sous-espace engendré par $S$.
De même, la relation $t P(t) = 0$ montre que l'image de $t^{d + 1}$
appartient au sous-espace engendré par $\{1, t, \ldots, t^d\}$ --- donc, d'après ce qui précède,
au sous-espace engendré par $S$. Une récurrence ascendante montre alors
que l'image de $t^n$, pour $n \geq d$, appartient au sous-espace engendré par $S$.
\end{example}

\noindent
Ceci confirme, par exemple, que $[\mathbf{C}: \mathbf{R}] = 2$. Plus généralement,
si $k$ est un corps et $\alpha \in k$ n'est pas un carré, le polynôme irréductible
$x^2 - \alpha \in k[x]$ permet de construire une extension $k[x]/(x^2 - \alpha)$
de degré deux.
Nous noterons celle-ci $k(\sqrt{\alpha})$. De telles extensions seront dites
{\it quadratiques,} pour des raisons évidentes.

\medskip\noindent
Le fait fondamental concernant le degré est qu'il est {\it multiplicatif dans les tours.}

\begin{lemma}[Multiplicativité]
```

</details>

### FR-FIELDS-B1-PROSE-0038

`lemma-multiplicativity-degrees` — source 542–587, cible 543–588.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L542) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

L'énoncé de multiplicativité et les deux calculs de la preuve sont conservés, avec les bases prises sur les bons corps. La source énonce une tour générale mais écrit sa preuve avec des bases finies ; on ne restreint pas silencieusement son énoncé. Le lecteur peut examiner cette différence de portée séparément.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{lemma-multiplicativity-degrees}
Suppose given a tower of fields $F/E/k$. Then
$$
[F:k] = [F:E][E:k]
$$
\end{lemma}

\begin{proof}
Let $\alpha_1, \ldots, \alpha_n \in F$ be an $E$-basis for $F$. Let
$\beta_1, \ldots, \beta_m \in E$ be a $k$-basis for $E$. Then the claim is
that the set of products
$\{\alpha_i \beta_j, 1 \leq i \leq n, 1 \leq j \leq m\}$
is a $k$-basis for $F$. Indeed, let us check first that they span $F$ over $k$.

\medskip\noindent
By assumption, the $\{\alpha_i\}$ span $F$ over $E$. So if
$f \in F$, there are $a_i \in E$ with
$$
f = \sum\nolimits_i a_i \alpha_i,
$$
and, for each $i$, we can write $a_i = \sum b_{ij} \beta_j$ for some
$b_{ij} \in k$. Putting these together, we find
$$
f = \sum\nolimits_{i,j} b_{ij} \alpha_i \beta_j,
$$
proving that the $\{\alpha_i \beta_j\}$ span $F$ over $k$.

\medskip\noindent
Suppose now that there existed a nontrivial relation
$$
\sum\nolimits_{i,j} c_{ij} \alpha_i \beta_j = 0
$$
for the $c_{ij} \in k$. In that case, we would have
$$
\sum\nolimits_i \alpha_i \left( \sum\nolimits_j c_{ij} \beta_j \right) = 0,
$$
and the inner terms lie in $E$ as the $\beta_j$ do. Now $E$-linear
independence of the $\{\alpha_i\}$ shows that the inner sums are all zero.
Then $k$-linear independence of the $\{\beta_j\}$ shows that the
$c_{ij}$ all vanish.
\end{proof}

\noindent
We sidetrack to a slightly tangential definition.

\begin{definition}
```

```tex
\label{lemma-multiplicativity-degrees}
Supposons donnée une tour de corps $F/E/k$. Alors
$$
[F:k] = [F:E][E:k]
$$
\end{lemma}

\begin{proof}
Soient $\alpha_1, \ldots, \alpha_n \in F$ une $E$-base de $F$, et
$\beta_1, \ldots, \beta_m \in E$ une $k$-base de $E$. L'affirmation est
que l'ensemble des produits
$\{\alpha_i \beta_j, 1 \leq i \leq n, 1 \leq j \leq m\}$
est une $k$-base de $F$. Vérifions d'abord qu'ils engendrent $F$ sur $k$.

\medskip\noindent
Par hypothèse, les $\{\alpha_i\}$ engendrent $F$ sur $E$. Ainsi, si
$f \in F$, il existe des $a_i \in E$ tels que
$$
f = \sum\nolimits_i a_i \alpha_i,
$$
et, pour chaque $i$, on peut écrire $a_i = \sum b_{ij} \beta_j$ avec des
$b_{ij} \in k$. En regroupant ces égalités, on obtient
$$
f = \sum\nolimits_{i,j} b_{ij} \alpha_i \beta_j,
$$
ce qui prouve que les $\{\alpha_i \beta_j\}$ engendrent $F$ sur $k$.

\medskip\noindent
Supposons maintenant qu'il existe une relation non triviale
$$
\sum\nolimits_{i,j} c_{ij} \alpha_i \beta_j = 0
$$
avec des $c_{ij} \in k$. On aurait alors
$$
\sum\nolimits_i \alpha_i \left( \sum\nolimits_j c_{ij} \beta_j \right) = 0,
$$
et les termes entre parenthèses appartiennent à $E$, puisque les $\beta_j$ y appartiennent.
L'indépendance $E$-linéaire des $\{\alpha_i\}$ montre que toutes les sommes intérieures sont nulles.
Puis l'indépendance $k$-linéaire des $\{\beta_j\}$ montre que tous les
$c_{ij}$ sont nuls.
\end{proof}

\noindent
Ouvrons une parenthèse pour donner une définition quelque peu tangente à notre propos.

\begin{definition}
```

</details>

### FR-FIELDS-B1-PROSE-0039

`definition-number-field` — source 588–600, cible 589–601.

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L588) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Corps de nombres conserve les deux conditions : caractéristique zéro et finitude sur Q. Le commentaire prudent sur la factorisation unique reste prudent ; aucune version plus forte du théorème n'est ajoutée.

<details>
<summary>Anglais officiel et français effectivement comparés</summary>

```tex
\label{definition-number-field}
A field $K$ is said to be a {\it number field} if it has characteristic
$0$ and the extension $K/\mathbf{Q}$ is finite.
\end{definition}

\noindent
Number fields are the basic objects in algebraic number theory. We shall see
later that,
for the analog of the integers $\mathbf{Z}$ in a number field, something kind
of like unique factorization still holds (though strict unique factorization
generally does not!).
```

```tex
\label{definition-number-field}
On dit qu'un corps $K$ est un {\it corps de nombres} s'il est de caractéristique
$0$ et si l'extension $K/\mathbf{Q}$ est finie.
\end{definition}

\noindent
Les corps de nombres sont les objets fondamentaux de la théorie algébrique des nombres. Nous verrons
plus loin que,
pour l'analogue des entiers $\mathbf{Z}$ dans un corps de nombres, une propriété
assez proche de la factorisation unique subsiste (bien qu'il n'y ait généralement
pas de factorisation unique au sens strict !).
```

</details>

## Limites et suite

Analyse assistée par OpenAI Codex ; aucune relecture humaine experte n'est revendiquée. L'identité exacte du modèle et de l'effort n'est pas attestée par ce reçu local : elle n'est pas inventée et doit être documentée honnêtement pour une publication. La confiance repose sur les passages comparés et non sur un score probabiliste.

Ce lot ne certifie ni la suite du chapitre, ni toute la terminologie, ni l'absence absolue d'erreurs, ni un PDF final. Poursuivre à la ligne source 601 sans recommencer les passages inchangés déjà lus. La version antérieure éditorialisée reste conservée séparément ; aucun renommage en traduction de l'édition anglaise intégrée par IA n'est effectué.
