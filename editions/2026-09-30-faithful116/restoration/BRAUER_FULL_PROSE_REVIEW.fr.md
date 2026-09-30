# Chapitre 11 — lecture intégrale de fidélité : Groupes de Brauer

**Lecture comparée du chapitre entier terminée ; aucune reconstruction ni publication de cette copie à ce stade.**

La copie restaurée a été lue du titre à la fermeture du document, avec l'anglais officiel. Les sept opérations source déjà recensées restent justifiées ; aucun changement français supplémentaire n'a été jugé nécessaire. Conserver un passage fidèle est un résultat de contrôle, non une nouvelle traduction.

[Copie LaTeX](staged/fr/011_brauer.fr.tex) · [Validation](BRAUER_FULL_PROSE_VALIDATION.json) · [43 blocs et avant-propos, textes complets](BRAUER_FULL_PROSE_CHOICES.json) · [Occurrences des règles](BRAUER_FULL_PROSE_OCCURRENCES.json) · [Restaurations historiques](BRAUER_REVIEW.fr.md)

## Ce qui a réellement été contrôlé

Les 44 intervalles disjoints couvrent tous les octets des deux fichiers : partie liminaire et 43 blocs d'étiquettes. Les frontières servent de repères ; elles ne sont pas des phrases. Chaque preuve, introduction, note, slogan et passage entre environnements a été lu. Les contrôles de structure sont des appuis séparés, non la preuve automatique de cette lecture. Le reçu historique qui indiquait une prose non auditée reste inchangé ; ce supplément précise la portée nouvellement achevée.

Analyse assistée par OpenAI Codex, sans relecture humaine experte. L'identité exacte du modèle et de l'effort de ce contrôle n'est pas attestée par ce reçu local et devra être consignée avant une publication de ce dossier. Les choix terminologiques sont réexaminés maintenant ; aucune consultation initiale de canon n'est inventée.

## Passages français effectivement consultés

### SERRE-6 — Jean-Pierre Serre

[Applications algébriques de la cohomologie des groupes. II : théorie des algèbres simples, premier exposé](https://www.numdam.org/item/SHC_1950-1951__3__A6_0.pdf)

Exposé 6, §§1–6, pages imprimées 6-01 à 6-09 ; texte extrait consulté via NUMDAM.

Atteste le registre historique des algèbres simples. Les formules OCR sont parfois corrompues : elles ne remplacent jamais les formules du témoin officiel de Stacks.

Témoin local : 1108209 octets ; SHA-256 `944E6F04FBEF935ED9F0D58AEB23C1860EDDA9027E0A954D277365996C7643BD`.

### SERRE-7 — Jean-Pierre Serre

[Applications algébriques de la cohomologie des groupes. II : théorie des algèbres simples, second exposé](https://www.numdam.org/item/SHC_1950-1951__3__A7_0.pdf)

Exposé 7, §§7–10, pages imprimées 7-01 à 7-05 ; les développements ultérieurs sur les produits croisés ne fondent pas cet audit.

Appuie le vocabulaire de conjugaison et de neutralisation ; le corollaire de §7 précise les automorphismes sur k. Cette précision n'est pas importée dans le texte traduit.

Témoin local : 1348682 octets ; SHA-256 `DAAF989D326D5B9A49655F401ABD3B5F55BDFE3279F77112DA78525270FF0FA2`.

### KAHN-A — Bruno Kahn

[Formes quadratiques sur un corps](https://webusers.imj-prg.fr/~bruno.kahn/preprints/fqbook.pdf)

Appendice A, A.1.1–A.1.5 et A.2.1–A.2.8(a), pages imprimées 133–135, pages PDF 145–147 ; pas de lecture intégrale revendiquée.

L'attestation de neutralisant est lue avec la définition de neutre et de similitude. Les possibles coquilles de cet appendice ne modifient pas l'autorité de Stacks.

Témoin local : 1378241 octets ; SHA-256 `D4A18D1B7A8D98D54A6425543678092D9D6E77542EDF5823B9596256D75B4E7F`.

## Points à examiner en priorité lors d’une éventuelle relecture

Ces points ne constituent pas une attente d'approbation. Ils distinguent les anomalies source, les conventions d'écriture et les limites d'attestation. Les corrections proposées demeurent séparées du texte traduit.

- **Convention de simplicité et cas nul** — BRAUER-003 retire une restriction qui ne figure pas dans la définition anglaise. Les conséquences dans lemma-simple-module sont à lire avec cette convention ; ne pas introduire une correction sous couvert de traduction. [Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L59) · [Décision](#fr-brauer-prose-0007)
- **Termes matriciels dits égaux** — Le texte officiel identifie les termes e_ii J e_jj. L'ancienne traduction avait remplacé cela par leurs ensembles de coefficients. Le rétablissement n'atteste pas la validité littérale de l'identification. [Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L260) · [Décision](#fr-brauer-prose-0019)
- **Cas N nul** — La restriction non nul de l'ancienne traduction a été retirée de (6). Le dossier conserve la proposition corrective au lieu de l'insérer. [Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L281) · [Décision](#fr-brauer-prose-0020)
- **Automorphismes et corps de base** — La source ne répète pas la restriction aux k-automorphismes que Serre explicite. Les deux additions françaises ont été retirées ; le problème reste visible dans le dossier de restauration. [Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L511) · [Décision](#fr-brauer-prose-0032)
- **Égalité ou isomorphisme naturel** — La convention d'égalité est conservée ; la preuve énonce un isomorphisme. Ce n'est pas compté comme un nouveau théorème erroné. [Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L567) · [Décision](#fr-brauer-prose-0035)
- **Portée de la supposition absurde** — La source dit aucun élément de K, sans exclure k. La restauration conserve K. L'objection au quantificateur est séparée du texte diplomatique. [Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L706) · [Décision](#fr-brauer-prose-0043)
- **Variante centralisateur** — Sens contrôlé par la définition ; aucune attestation lexicale de cette variante dans les trois passages cités. Commutant/centralisateur ne doit pas être présenté comme un choix confirmé par une citation qui ne contient pas ce mot. [Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L167) · [Décision](#fr-brauer-prose-0014)

## Règles terminologiques et emplois contrôlés

### corps-gauche

Le corps non commutatif possible, avec inverse de tout élément non nul. Algèbre à division est une alternative attestée ; maintenir la forme cohérente déjà employée.

Appuis : SERRE-6, KAHN-A. Occurrences précisément repérées : 30. Nature de la preuve : terme attesté et emploi relu en contexte.

### ideal-bilatere

Stabilité à gauche et à droite ; ne pas remplacer par idéal à droite. Les définitions du chapitre fixent chaque emploi.

Appuis : SERRE-6. Occurrences précisément repérées : 12. Nature de la preuve : terme attesté et emploi relu en contexte.

### algebre-opposee

Multiplication renversée, non changement de signe ; les occurrences et les formules avec op ont été lues dans leurs actions à gauche/droite.

Appuis : SERRE-6, KAHN-A. Occurrences précisément repérées : 2. Nature de la preuve : terme attesté et emploi relu en contexte.

### bicommutant

Double commutant défini dans la preuve de Rieffel ; les conventions d'action restent celles de Stacks.

Appuis : SERRE-6. Occurrences précisément repérées : 2. Nature de la preuve : terme attesté et emploi relu en contexte.

### similitude

Équivalence de Brauer définie par les algèbres de matrices ; ne pas confondre avec les seules classes d'isomorphisme.

Appuis : SERRE-6, KAHN-A. Occurrences précisément repérées : 10. Nature de la preuve : terme attesté et emploi relu en contexte.

### neutralisation

Après extension, l'algèbre devient matricielle. Corps de décomposition est l'alternative chez Serre ; neutralisant est directement attesté chez Kahn.

Appuis : SERRE-7, KAHN-A. Occurrences précisément repérées : 11. Nature de la preuve : terme attesté et emploi relu en contexte.

### centralisateur

Les passages consultés attestent commutant, pas ce mot. Maintien de centralisateur fondé sur le contexte : la définition explicite et chaque argument fixent le même objet ; attestation lexicale indépendante de cette variante non obtenue ici.

Appuis : SERRE-6, SERRE-7, KAHN-A. Occurrences précisément repérées : 17. Nature de la preuve : variante non attestée dans les passages consultés ; justification contextuelle explicite.

### dimension-finie

Contrôle contextuel entre dimension sur k, rang sur un corps gauche et génération finie : ces propriétés ne sont pas interchangées hors de leurs hypothèses.

Appuis : SERRE-6. Occurrences précisément repérées : 55. Nature de la preuve : sens vérifié, sans prétendre à une attestation mot à mot.

### interieur

Automorphisme réalisé par conjugaison. La question des automorphismes fixant k reste un avertissement sur le texte source, pas une correction intégrée.

Appuis : SERRE-7. Occurrences précisément repérées : 2. Nature de la preuve : terme attesté et emploi relu en contexte.

### integre

Dans la preuve pour un corps algébriquement clos, le sous-anneau d'un corps gauche est sans diviseur de zéro. Intègre, plutôt qu'entière, correspond à ce sens d'integral. Justification par le contexte officiel, sans attestation externe supplémentaire.

Appuis : contexte anglais officiel seulement. Occurrences précisément repérées : 1. Nature de la preuve : argument fondé sur le passage officiel.

### sous-corps-commutatif

Field est commutatif dans l'anglais de Stacks, distinct de skew field. L'explicitation française commutatif ne réduit pas l'énoncé source.

Appuis : SERRE-7, KAHN-A. Occurrences précisément repérées : 4. Nature de la preuve : terme attesté et emploi relu en contexte.

## Index de la lecture intégrale

### FR-BRAUER-PROSE-0001

`frontmatter` — source 1–12, cible 1–12.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L1) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Titre traduit par Groupes de Brauer ; préambule, ouverture du document et commande de titre conservés. Les commentaires techniques anglais ne font pas partie du texte destiné au lecteur. Aucune attribution de traduction aux auteurs du Stacks Project n'est ajoutée.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\input{preamble}

% OK, start here.
%
\begin{document}

\title{Brauer groups}


\maketitle

\phantomsection
```

Français restauré :

```tex
\input{preamble}

% OK, start here.
%
\begin{document}

\title{Groupes de Brauer}


\maketitle

\phantomsection
```

</details>

### FR-BRAUER-PROSE-0002

`section-phantom` — source 13–17, cible 13–17.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L13) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Ancre et table des matières conservées. Le titre Introduction est identique dans les deux langues. Ce segment est de structure, sans assertion mathématique.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{section-phantom}

\tableofcontents

\section{Introduction}
```

Français restauré :

```tex
\label{section-phantom}

\tableofcontents

\section{Introduction}
```

</details>

### FR-BRAUER-PROSE-0003

`section-introduction` — source 18–29, cible 18–29.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L18) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Les trois références et la recommandation de lire Serre sont conservées. Le nous qui décrit le changement de preuve par Rieffel est celui des auteurs du Stacks Project, non une revendication du traducteur. Élégant rend ici l'appréciation fun ; il ne modifie pas l'argument. La réserve selon laquelle la modification n'est probablement pas une amélioration reste explicite.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{section-introduction}

\noindent
A reference is the lectures by Serre in the Seminaire Cartan, see
\cite{Serre-Cartan}. Serre in turn refers to
\cite{Deuring} and \cite{ANT}. We changed some of the proofs, in particular
we used a fun argument of Rieffel to prove Wedderburn's theorem.
Very likely this change is not an improvement and we strongly
encourage the reader to read the original exposition by Serre.


\section{Noncommutative algebras}
```

Français restauré :

```tex
\label{section-introduction}

\noindent
On pourra consulter les exposés de Serre au Séminaire Cartan, voir
\cite{Serre-Cartan}. Serre renvoie lui-même à
\cite{Deuring} et \cite{ANT}. Nous avons modifié certaines démonstrations ; en particulier,
nous avons utilisé un élégant argument de Rieffel pour démontrer le théorème de Wedderburn.
Il est très probable que cette modification ne constitue pas une amélioration, et nous
encourageons vivement le lecteur à lire l'exposé original de Serre.


\section{Algèbres non commutatives}
```

</details>

### FR-BRAUER-PROSE-0004

`section-algebras` — source 30–39, cible 30–39.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L30) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Le corps de base est envoyé dans le centre, l'homomorphisme préserve l'unité et la convention des modules à droite unitaires est conservée. Éventuellement non commutatif porte sur l'anneau ; aucune commutativité n'est imposée subrepticement. Le vocabulaire est contrôlé par les définitions elles-mêmes, et non par substitution isolée.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{section-algebras}

\noindent
Let $k$ be a field. In this chapter an {\it algebra} $A$ over $k$ is
a possibly noncommutative ring $A$ together with a ring map
$k \to A$ such that $k$ maps into the center of $A$ and such that
$1$ maps to an identity element of $A$. An {\it $A$-module} is a right
$A$-module such that the identity of $A$ acts as the identity.

\begin{definition}
```

Français restauré :

```tex
\label{section-algebras}

\noindent
Soit $k$ un corps. Dans ce chapitre, une {\it algèbre} $A$ sur $k$ est
un anneau $A$, éventuellement non commutatif, muni d'un homomorphisme d'anneaux
$k \to A$ tel que l'image de $k$ soit contenue dans le centre de $A$ et qui
envoie $1$ sur l'élément unité de $A$. Un {\it $A$-module} est un
$A$-module à droite sur lequel l'élément unité de $A$ agit comme l'identité.

\begin{definition}
```

</details>

### FR-BRAUER-PROSE-0005

`definition-finite` — source 40–45, cible 40–45.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L40) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Finie signifie de dimension finie sur k dans cette définition, non de cardinal fini. La formule définissant la notation est inchangée. Les emplois ultérieurs de dimension finie sont confrontés à cette convention.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{definition-finite}
Let $A$ be a $k$-algebra. We say $A$ is {\it finite} if $\dim_k(A) < \infty$.
In this case we write $[A : k] = \dim_k(A)$.
\end{definition}

\begin{definition}
```

Français restauré :

```tex
\label{definition-finite}
Soit $A$ une $k$-algèbre. Nous disons que $A$ est {\it finie} si $\dim_k(A) < \infty$.
Dans ce cas, nous écrivons $[A : k] = \dim_k(A)$.
\end{definition}

\begin{definition}
```

</details>

### FR-BRAUER-PROSE-0006

`definition-skew-field` — source 46–58, cible 46–58.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L46) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Corps gauche conserve la possibilité de non-commutativité, l'unité non nulle et l'inversibilité de tout élément non nul. Le paragraphe sur le sous-corps premier, la liberté des modules et la base obtenue par Zorn est intégralement conservé. L'alternative algèbre à division est attestée chez Kahn, mais changer la terminologie cohérente du chapitre n'est pas nécessaire.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{definition-skew-field}
A {\it skew field} is a possibly noncommutative ring with an identity
element $1$, with $1 \not = 0$, in which every nonzero element
has a multiplicative inverse.
\end{definition}

\noindent
A skew field is a $k$-algebra for some $k$ (e.g., for the prime field
contained in it). We will use below that any module over a skew field
is free because a maximal linearly independent set of vectors forms a
basis and exists by Zorn's lemma.

\begin{definition}
```

Français restauré :

```tex
\label{definition-skew-field}
Un {\it corps gauche} est un anneau éventuellement non commutatif, muni d'un élément unité
$1$, avec $1 \not = 0$, dans lequel tout élément non nul
possède un inverse multiplicatif.
\end{definition}

\noindent
Un corps gauche est une $k$-algèbre pour un certain $k$ (par exemple pour le sous-corps premier
qu'il contient). Nous utiliserons ci-dessous que tout module sur un corps gauche
est libre : une famille maximale de vecteurs linéairement indépendants constitue une
base, et une telle famille existe d'après le lemme de Zorn.

\begin{definition}
```

</details>

### FR-BRAUER-PROSE-0007

`definition-simple` — source 59–67, cible 59–68.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L59) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

La condition non nul est bien conservée pour le module. La restriction ajoutée à l'algèbre a déjà été retirée par BRAUER-003, car elle n'est pas écrite dans la source. Les idéaux bilatères sont distingués des sous-modules à droite. Le résultat est une fidélité à la convention imprimée, non l'approbation de ses conséquences pour l'algèbre nulle.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{definition-simple}
Let $A$ be a $k$-algebra.
We say an $A$-module $M$ is {\it simple} if it is nonzero and
the only $A$-submodules are $0$ and $M$.
We say $A$ is {\it simple} if the only two-sided ideals of $A$ are
$0$ and $A$.
\end{definition}

\begin{definition}
```

Français restauré :

```tex
\label{definition-simple}
Soit $A$ une $k$-algèbre.
Nous disons qu'un $A$-module $M$ est {\it simple} s'il est non nul et si
ses seuls sous-$A$-modules sont $0$ et $M$.
Nous disons que $A$ est {\it simple} si les seuls
idéaux bilatères de $A$ sont
$0$ et $A$.
\end{definition}

\begin{definition}
```

</details>

### FR-BRAUER-PROSE-0008

`definition-central` — source 68–73, cible 69–74.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L68) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Centrale qualifie l'algèbre dont le centre est exactement l'image du corps, et non seulement une algèbre contenant cette image. Le texte conserve la formulation par l'application k vers A sans remplacer celle-ci par une identification supplémentaire.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{definition-central}
A $k$-algebra $A$ is {\it central} if the center of $A$ is the image of
$k \to A$.
\end{definition}

\begin{definition}
```

Français restauré :

```tex
\label{definition-central}
Une $k$-algèbre $A$ est {\it centrale} si le centre de $A$ est l'image de
$k \to A$.
\end{definition}

\begin{definition}
```

</details>

### FR-BRAUER-PROSE-0009

`definition-opposite` — source 74–83, cible 75–84.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L74) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Algèbre opposée désigne l'inversion de l'ordre de multiplication ; il ne s'agit pas d'un changement de signe. La notation op est inchangée. Le titre du théorème suivant est conservé sans nouvelle attribution.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{definition-opposite}
Given a $k$-algebra $A$ we denote $A^{op}$ the $k$-algebra we get by
reversing the order of multiplication in $A$. This is called the
{\it opposite algebra}.
\end{definition}




\section{Wedderburn's theorem}
```

Français restauré :

```tex
\label{definition-opposite}
Étant donnée une $k$-algèbre $A$, nous notons $A^{op}$ la $k$-algèbre obtenue
en renversant l'ordre de la multiplication dans $A$. On l'appelle
l'{\it algèbre opposée}.
\end{definition}




\section{Théorème de Wedderburn}
```

</details>

### FR-BRAUER-PROSE-0010

`section-wedderburn` — source 84–91, cible 85–92.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L84) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

La référence à Rieffel et l'attribution de l'appréciation à Carl Faith sont toutes deux conservées. Pourrait difficilement être plus simple est une tournure française idiomatique, non un ajout de preuve. Aucune attestation externe particulière de cette tournure stylistique n'est revendiquée.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{section-wedderburn}

\noindent
The following cute argument can be found in a paper of Rieffel, see
\cite{Rieffel}. The proof could not be simpler (quote from
Carl Faith's review).

\begin{lemma}
```

Français restauré :

```tex
\label{section-wedderburn}

\noindent
L'élégant argument qui suit se trouve dans un article de Rieffel, voir
\cite{Rieffel}. La démonstration pourrait difficilement être plus simple (pour reprendre
les mots du compte rendu de Carl Faith).

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0011

`lemma-rieffel` — source 92–119, cible 93–120.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L92) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Énoncé, démonstration et note sont lus ensemble. M reste un idéal à droite non nul ; A' agit à gauche et A'' à droite. La note explicite la multiplication opposée dans A''. Les étapes injectivité de R, idéal à droite R(M), idéal bilatère AM, puis présence de l'unité dans R(A) sont toutes présentes. Bicommutant est attesté par Serre, mais sa preuve n'a pas été substituée à celle de Rieffel.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-rieffel}
Let $A$ be a possibly noncommutative ring with $1$ which contains no
nontrivial two-sided ideal. Let $M$ be a nonzero right ideal in $A$,
and view $M$ as a right $A$-module. Then $A$ coincides with the
bicommutant of $M$.
\end{lemma}

\begin{proof}
Let $A' = \text{End}_A(M)$, so $M$ is a left $A'$-module.
Set $A'' = \text{End}_{A'}(M)$ (the bicommutant of $M$).
We view $M$ as a right $A''$-module\footnote{This
means that given $a'' \in A''$ and $m \in M$ we have a product
$m a'' \in M$. In particular, the multiplication in $A''$
is the opposite of what you'd get if you wrote elements of $A''$
as endomorphisms acting on the left.}.
Let $R : A \to A''$ be the natural homomorphism such that
$mR(a) = ma$. Then $R$ is injective, since $R(1) = \text{id}_M$
and $A$ contains no nontrivial two-sided ideal. We claim that $R(M)$
is a right ideal in $A''$. Namely, $R(m)a'' = R(ma'')$ for $a'' \in A''$
and $m$ in $M$, because {\it left} multiplication of $M$ by any element $n$
of $M$ represents an element of $A'$, and so
$(nm)a'' = n(ma'')$ for all $n$ in $M$.
Finally, the product ideal $AM$ is a two-sided ideal, and so
$A = AM$. Thus $R(A) = R(A)R(M)$, so that $R(A)$ is a right ideal in $A''$.
But $R(A)$ contains the identity element of $A''$, and so $R(A) = A''$.
\end{proof}

\begin{lemma}
```

Français restauré :

```tex
\label{lemma-rieffel}
Soit $A$ un anneau éventuellement non commutatif, muni de $1$, qui ne possède aucun
idéal bilatère non trivial. Soit $M$ un idéal à droite non nul de $A$,
et considérons $M$ comme un $A$-module à droite. Alors $A$ coïncide avec le
bicommutant de $M$.
\end{lemma}

\begin{proof}
Soit $A' = \text{End}_A(M)$, de sorte que $M$ est un $A'$-module à gauche.
Posons $A'' = \text{End}_{A'}(M)$ (le bicommutant de $M$).
Considérons $M$ comme un $A''$-module à droite\footnote{Cela
signifie que, pour $a'' \in A''$ et $m \in M$, nous avons un produit
$m a'' \in M$. En particulier, la multiplication dans $A''$
est l'opposée de celle que l'on obtiendrait en écrivant les éléments de $A''$
comme des endomorphismes agissant à gauche.}.
Soit $R : A \to A''$ l'homomorphisme naturel défini par
$mR(a) = ma$. Alors $R$ est injectif, puisque $R(1) = \text{id}_M$
et que $A$ ne possède aucun idéal bilatère non trivial. Nous affirmons que $R(M)$
est un idéal à droite de $A''$. En effet, $R(m)a'' = R(ma'')$ pour $a'' \in A''$
et $m$ dans $M$, car la multiplication {\it à gauche} sur $M$ par tout élément $n$
de $M$ définit un élément de $A'$, de sorte que
$(nm)a'' = n(ma'')$ pour tout $n$ dans $M$.
Enfin, l'idéal produit $AM$ est un idéal bilatère, et donc
$A = AM$. Ainsi $R(A) = R(A)R(M)$, si bien que $R(A)$ est un idéal à droite de $A''$.
Mais $R(A)$ contient l'élément unité de $A''$, donc $R(A) = A''$.
\end{proof}

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0012

`lemma-simple-module` — source 120–140, cible 121–141.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L120) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Les quatre assertions et leurs justifications sont conservées : existence, inclusion dans un module non nul, finitude dimensionnelle et corps des endomorphismes. La preuve source parle d'un sous-module de dimension minimale sans répéter non nul ; la traduction ne complète pas cette condition. La phrase qui dit A non nul est également conservée comme lecture source, malgré la réserve sur sa définition.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-simple-module}
Let $A$ be a $k$-algebra. If $A$ is finite, then
\begin{enumerate}
\item $A$ has a simple module,
\item any nonzero module contains a simple submodule,
\item a simple module over $A$ has finite dimension over $k$, and
\item if $M$ is a simple $A$-module, then $\text{End}_A(M)$ is a
skew field.
\end{enumerate}
\end{lemma}

\begin{proof}
Of course (1) follows from (2) since $A$ is a nonzero $A$-module.
For (2), any submodule of minimal (finite) dimension as a $k$-vector
space will be simple. There exists a finite dimensional one
because a cyclic submodule is one. If $M$ is simple, then
$mA \subset M$ is a sub-module, hence we see (3). Any nonzero element
of $\text{End}_A(M)$ is an isomorphism, hence (4) holds.
\end{proof}

\begin{theorem}
```

Français restauré :

```tex
\label{lemma-simple-module}
Soit $A$ une $k$-algèbre. Si $A$ est finie, alors
\begin{enumerate}
\item $A$ possède un module simple,
\item tout module non nul contient un sous-module simple,
\item tout module simple sur $A$ est de dimension finie sur $k$, et
\item si $M$ est un $A$-module simple, alors $\text{End}_A(M)$ est un
corps gauche.
\end{enumerate}
\end{lemma}

\begin{proof}
Bien sûr, (1) résulte de (2), puisque $A$ est un $A$-module non nul.
Pour (2), tout sous-module de dimension (finie) minimale comme espace vectoriel sur $k$
est simple. Il en existe un de dimension finie,
car un sous-module cyclique est de dimension finie. Si $M$ est simple, alors
$mA \subset M$ est un sous-module, ce qui donne (3). Tout élément non nul
de $\text{End}_A(M)$ est un isomorphisme, d'où (4).
\end{proof}

\begin{theorem}
```

</details>

### FR-BRAUER-PROSE-0013

`theorem-wedderburn` — source 141–166, cible 142–164.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L141) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Le slogan et l'énoncé gardent la finitude dimensionnelle. La preuve choisit M, définit K par les endomorphismes puis utilise le bicommutant. Le module libre est à gauche sur K ; la conclusion emploie K opposé. Libre de rang fini rend finite free, sans interprétation financière ni suppression de la génération finie.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{theorem-wedderburn}
\begin{slogan}
Simple finite algebras over a field are matrix algebras over a skew field.
\end{slogan}
Let $A$ be a simple finite $k$-algebra. Then $A$ is a matrix algebra over
a finite $k$-algebra $K$ which is a skew field.
\end{theorem}

\begin{proof}
We may choose a simple submodule $M \subset A$ and then
the $k$-algebra $K = \text{End}_A(M)$ is a skew field, see
Lemma \ref{lemma-simple-module}.
By
Lemma \ref{lemma-rieffel}
we see that $A = \text{End}_K(M)$. Since $K$ is a skew field and
$M$ is finitely generated (since $\dim_k(M) < \infty$) we see that
$M$ is finite free as a left $K$-module. It follows immediately that
$A \cong \text{Mat}(n \times n, K^{op})$.
\end{proof}






\section{Lemmas on algebras}
```

Français restauré :

```tex
\label{theorem-wedderburn}
\begin{slogan}
Les algèbres simples de dimension finie sur un corps sont des algèbres de matrices sur un corps gauche.
\end{slogan}
Soit $A$ une $k$-algèbre simple et finie. Alors $A$ est une algèbre de matrices sur
une $k$-algèbre finie $K$ qui est un corps gauche.
\end{theorem}

\begin{proof}
Nous pouvons choisir un sous-module simple $M \subset A$ ; alors
la $k$-algèbre $K = \text{End}_A(M)$ est un corps gauche, voir
le lemme \ref{lemma-simple-module}.
D'après le
lemme \ref{lemma-rieffel},
nous avons $A = \text{End}_K(M)$. Comme $K$ est un corps gauche et que
$M$ est de type fini (puisque $\dim_k(M) < \infty$), nous voyons que
$M$ est libre de rang fini comme $K$-module à gauche. Il en résulte immédiatement que
$A \cong \text{Mat}(n \times n, K^{op})$.
\end{proof}



\section{Lemmes sur les algèbres}
```

</details>

### FR-BRAUER-PROSE-0014

`section-lemmas` — source 167–177, cible 165–175.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L167) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

La définition du centralisateur conserve l'universel pour tout et l'égalité xy=yx pour les éléments de B. Le seul texte traduit à l'intérieur d'une formule dans tout ce chapitre est for all vers pour tout. Serre et Kahn utilisent commutant pour cette notion ; les passages consultés n'attestent pas le mot centralisateur. Son maintien est justifié ici par la définition explicite et la cohérence interne, pas par une citation lexicale inventée.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{section-lemmas}

\noindent
Let $A$ be a $k$-algebra. Let $B \subset A$ be a subalgebra.
The {\it centralizer of $B$ in $A$} is the subalgebra
$$
C  = \{y \in A \mid xy = yx \text{ for all }x \in B\}.
$$
It is a $k$-algebra.

\begin{lemma}
```

Français restauré :

```tex
\label{section-lemmas}

\noindent
Soit $A$ une $k$-algèbre. Soit $B \subset A$ une sous-algèbre.
Le {\it centralisateur de $B$ dans $A$} est la sous-algèbre
$$
C  = \{y \in A \mid xy = yx \text{ pour tout }x \in B\}.
$$
C'est une $k$-algèbre.

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0015

`lemma-centralizer` — source 178–192, cible 176–190.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L178) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Les deux inclusions de la preuve par commutation et l'intersection finale sont préservées. Les indices des quatre algèbres et de leurs centralisateurs ne sont pas échangés. Le choix commute à, plutôt que commute avec, est grammatical et exprime la même égalité des produits.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-centralizer}
Let $A$, $A'$ be $k$-algebras. Let $B \subset A$, $B' \subset A'$ be
subalgebras with centralizers $C$, $C'$. Then the centralizer of
$B \otimes_k B'$ in $A \otimes_k A'$ is $C \otimes_k C'$.
\end{lemma}

\begin{proof}
Denote $C'' \subset A \otimes_k A'$ the centralizer of $B \otimes_k B'$.
It is clear that $C \otimes_k C' \subset C''$. Conversely, every element
of $C''$ commutes with $B \otimes 1$ hence is contained in $C \otimes_k A'$.
Similarly $C'' \subset A \otimes_k C'$. Thus
$C'' \subset C \otimes_k A' \cap A \otimes_k C' = C \otimes_k C'$.
\end{proof}

\begin{lemma}
```

Français restauré :

```tex
\label{lemma-centralizer}
Soient $A$, $A'$ des $k$-algèbres. Soient $B \subset A$, $B' \subset A'$ des
sous-algèbres de centralisateurs respectifs $C$, $C'$. Alors le centralisateur de
$B \otimes_k B'$ dans $A \otimes_k A'$ est $C \otimes_k C'$.
\end{lemma}

\begin{proof}
Notons $C'' \subset A \otimes_k A'$ le centralisateur de $B \otimes_k B'$.
Il est clair que $C \otimes_k C' \subset C''$. Réciproquement, tout élément
de $C''$ commute à $B \otimes 1$ et appartient donc à $C \otimes_k A'$.
De même, $C'' \subset A \otimes_k C'$. Ainsi
$C'' \subset C \otimes_k A' \cap A \otimes_k C' = C \otimes_k C'$.
\end{proof}

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0016

`lemma-center-csa` — source 193–208, cible 191–206.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L193) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Centre rendu comme corps extension finie, non comme sous-espace quelconque. La réduction matricielle, le centre de K et le produit tensoriel k avec k' suivent exactement la source. On n'a pas remplacé la preuve par une formule de centre plus développée.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-center-csa}
Let $A$ be a finite simple $k$-algebra. Then the center $k'$ of $A$
is a finite field extension of $k$.
\end{lemma}

\begin{proof}
Write $A = \text{Mat}(n \times n, K)$ for some skew field $K$ finite
over $k$, see
Theorem \ref{theorem-wedderburn}.
By
Lemma \ref{lemma-centralizer}
the center of $A$ is $k \otimes_k k'$ where $k' \subset K$ is the
center of $K$. Since the center of a skew field is a field, we win.
\end{proof}

\begin{lemma}
```

Français restauré :

```tex
\label{lemma-center-csa}
Soit $A$ une $k$-algèbre simple de dimension finie. Alors le centre $k'$ de
$A$ est une extension finie de $k$.
\end{lemma}

\begin{proof}
Écrivons $A = \text{Mat}(n \times n, K)$ pour un corps gauche $K$ de
dimension finie sur $k$ ; voir le
théorème \ref{theorem-wedderburn}.
D'après le
lemme \ref{lemma-centralizer},
le centre de $A$ est $k \otimes_k k'$, où $k' \subset K$ est le centre de
$K$. Puisque le centre d'un corps gauche est un corps, le résultat en découle.
\end{proof}

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0017

`lemma-generate-two-sided-sub` — source 209–245, cible 207–243.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L209) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Two-sided devient à gauche et à droite pour un sous-espace sur un corps gauche : les deux stabilités sont nécessaires et préservées. Le quotient par V', la réduction à une intersection non nulle, le choix de n minimal, la multiplication à droite par l'inverse de k_1 et le commutateur avec tout c sont conservés. La contradiction finale n'est ni abrégée ni réorientée.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-generate-two-sided-sub}
Let $V$ be a $k$ vector space. Let $K$ be a central $k$-algebra
which is a skew field. Let $W \subset V \otimes_k K$ be a two-sided
$K$-sub vector space. Then $W$ is generated as a left $K$-vector
space by $W \cap (V \otimes 1)$.
\end{lemma}

\begin{proof}
Let $V' \subset V$ be the $k$-sub vector space generated by $v \in V$
such that $v \otimes 1 \in W$. Then $V' \otimes_k K \subset W$ and
we have
$$
W/(V' \otimes_k K)  \subset  (V/V') \otimes_k K.
$$
If $\overline{v} \in V/V'$ is a nonzero vector such that
$\overline{v} \otimes 1$ is contained in $W/(V' \otimes_k K)$,
then we see that $v \otimes 1 \in W$ where $v \in V$ lifts $\overline{v}$.
This contradicts our construction of $V'$. Hence we may replace
$V$ by $V/V'$ and $W$ by $W/(V' \otimes_k K)$ and it suffices to prove
that $W \cap (V \otimes 1)$ is nonzero if $W$ is nonzero.

\medskip\noindent
To see this let $w \in W$ be a nonzero element which can be written
as $w = \sum_{i = 1, \ldots, n} v_i \otimes k_i$ with $n$ minimal.
We may right multiply with $k_1^{-1}$ and assume that $k_1 = 1$.
If $n = 1$, then we win because $v_1 \otimes 1 \in W$.
If $n > 1$, then we see that for any $c \in K$
$$
c w - w c = \sum\nolimits_{i = 2, \ldots, n} v_i \otimes (c k_i - k_i c) \in W
$$
and hence $c k_i - k_i c = 0$ by minimality of $n$.
This implies that $k_i$ is in the center of $K$ which is $k$ by
assumption. Hence $w = (v_1 + \sum k_i v_i) \otimes 1$ contradicting
the minimality of $n$.
\end{proof}

\begin{lemma}
```

Français restauré :

```tex
\label{lemma-generate-two-sided-sub}
Soit $V$ un espace vectoriel sur $k$. Soit $K$ une $k$-algèbre centrale qui
est un corps gauche. Soit $W \subset V \otimes_k K$ un sous-espace vectoriel
à gauche et à droite sur $K$. Alors $W$ est engendré, comme espace vectoriel
à gauche sur $K$, par $W \cap (V \otimes 1)$.
\end{lemma}

\begin{proof}
Soit $V' \subset V$ le sous-espace vectoriel sur $k$ engendré par les
$v \in V$ tels que $v \otimes 1 \in W$. Alors $V' \otimes_k K \subset W$ et
nous avons
$$
W/(V' \otimes_k K)  \subset  (V/V') \otimes_k K.
$$
S'il existe un vecteur non nul $\overline{v} \in V/V'$ tel que
$\overline{v} \otimes 1$ appartienne à $W/(V' \otimes_k K)$,
alors $v \otimes 1 \in W$, où $v \in V$ est un relèvement de $\overline{v}$.
Cela contredit la construction de $V'$. Nous pouvons donc remplacer
$V$ par $V/V'$ et $W$ par $W/(V' \otimes_k K)$ ; il suffit alors de montrer
que $W \cap (V \otimes 1)$ est non nul si $W$ est non nul.

\medskip\noindent
Pour le voir, choisissons un élément non nul $w \in W$ qui puisse s'écrire
$w = \sum_{i = 1, \ldots, n} v_i \otimes k_i$, avec $n$ minimal.
En multipliant à droite par $k_1^{-1}$, nous pouvons supposer $k_1 = 1$.
Si $n = 1$, la conclusion est acquise puisque $v_1 \otimes 1 \in W$.
Si $n > 1$, alors, pour tout $c \in K$,
$$
c w - w c = \sum\nolimits_{i = 2, \ldots, n} v_i \otimes (c k_i - k_i c) \in W
$$
et donc $c k_i - k_i c = 0$ par minimalité de $n$.
Il s'ensuit que $k_i$ appartient au centre de $K$, qui est $k$ par
hypothèse. Ainsi $w = (v_1 + \sum k_i v_i) \otimes 1$, ce qui contredit
la minimalité de $n$.
\end{proof}

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0018

`lemma-generate-two-sided-ideal` — source 246–259, cible 244–257.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L246) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Idéal bilatère distingue les deux actions. Le quantificateur pour un certain idéal J reste existentiel. La définition de J et l'appel au lemme précédent sont conservés, ainsi que la conséquence sur la simplicité. Aucune finitude de A ou de K n'est ajoutée.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-generate-two-sided-ideal}
Let $A$ be a $k$-algebra. Let $K$ be a central $k$-algebra
which is a skew field. Then any two-sided ideal $I \subset A \otimes_k K$
is of the form $J \otimes_k K$ for some two-sided ideal $J \subset A$.
In particular, if $A$ is simple, then so is $A \otimes_k K$.
\end{lemma}

\begin{proof}
Set $J = \{a \in A \mid a \otimes 1 \in I\}$. This is a two-sided ideal
of $A$. And $I = J \otimes_k K$ by
Lemma \ref{lemma-generate-two-sided-sub}.
\end{proof}

\begin{lemma}
```

Français restauré :

```tex
\label{lemma-generate-two-sided-ideal}
Soit $A$ une $k$-algèbre. Soit $K$ une $k$-algèbre centrale qui est un corps
gauche. Alors tout idéal bilatère $I \subset A \otimes_k K$ est de la forme
$J \otimes_k K$ pour un idéal bilatère $J \subset A$.
En particulier, si $A$ est simple, alors $A \otimes_k K$ l'est aussi.
\end{lemma}

\begin{proof}
Posons $J = \{a \in A \mid a \otimes 1 \in I\}$. C'est un idéal bilatère
de $A$. En outre, $I = J \otimes_k K$ d'après le
lemme \ref{lemma-generate-two-sided-sub}.
\end{proof}

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0019

`lemma-matrix-algebras` — source 260–280, cible 258–278.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L260) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Les trois assertions et les deux foncteurs sont conservés. BRAUER-002 avait réécrit la preuve avec des ensembles de coefficients ; la copie restaurée revient à l'égalité des termes et à la somme non indexée de la source. Cette formulation pose une question d'identification des sous-espaces matriciels : elle est signalée séparément, non certifiée comme preuve correcte.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-matrix-algebras}
Let $R$ be a possibly noncommutative ring. Let $n \geq 1$ be an integer.
Let $R_n = \text{Mat}(n \times n, R)$.
\begin{enumerate}
\item The functors $M \mapsto M^{\oplus n}$ and
$N \mapsto Ne_{11}$ define quasi-inverse equivalences of categories
$\text{Mod}_R \leftrightarrow \text{Mod}_{R_n}$.
\item A two-sided ideal of $R_n$ is of the form $IR_n$ for some
two-sided ideal $I$ of $R$.
\item The center of $R_n$ is equal to the center of $R$.
\end{enumerate}
\end{lemma}

\begin{proof}
Part (1) proves itself. If $J \subset R_n$ is a two-sided ideal, then
$J = \bigoplus e_{ii}Je_{jj}$ and all of the summands $e_{ii}Je_{jj}$ are
equal to each other and are a two-sided ideal $I$ of $R$. This proves (2).
Part (3) is clear.
\end{proof}

\begin{lemma}
```

Français restauré :

```tex
\label{lemma-matrix-algebras}
Soit $R$ un anneau, éventuellement non commutatif. Soit $n \geq 1$ un entier.
Posons $R_n = \text{Mat}(n \times n, R)$.
\begin{enumerate}
\item Les foncteurs $M \mapsto M^{\oplus n}$ et
$N \mapsto Ne_{11}$ définissent des équivalences de catégories quasi inverses
$\text{Mod}_R \leftrightarrow \text{Mod}_{R_n}$.
\item Tout idéal bilatère de $R_n$ est de la forme $IR_n$ pour un certain
idéal bilatère $I$ de $R$.
\item Le centre de $R_n$ est égal au centre de $R$.
\end{enumerate}
\end{lemma}

\begin{proof}
Le point (1) est immédiat. Si $J \subset R_n$ est un idéal bilatère, alors
$J = \bigoplus e_{ii}Je_{jj}$, et tous les termes $e_{ii}Je_{jj}$ sont
égaux entre eux et constituent un idéal bilatère $I$ de $R$. Cela prouve (2).
Le point (3) est clair.
\end{proof}

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0020

`lemma-simple-module-unique` — source 281–320, cible 279–319.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L281) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Les six assertions et la preuve entière ont été comparées. Unicité à isomorphisme près, sommes directes, équivalence des dimensions, actions à gauche, opposé de K et formule dimensionnelle restent identiques. La condition non nul ajoutée à N en (6) a été retirée par BRAUER-004 ; le cas N nul reste une difficulté du texte de référence, pas une erreur de français nouvellement créée.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-simple-module-unique}
Let $A$ be a finite simple $k$-algebra.
\begin{enumerate}
\item There exists exactly one simple $A$-module $M$ up to isomorphism.
\item Any finite $A$-module is a direct sum of copies of a simple module.
\item Two finite $A$-modules are isomorphic if and only if they
have the same dimension over $k$.
\item If $A = \text{Mat}(n \times n, K)$ with $K$ a finite skew field
extension of $k$, then $M = K^{\oplus n}$ is a simple $A$-module and
$\text{End}_A(M) = K^{op}$.
\item If $M$ is a simple $A$-module, then $L = \text{End}_A(M)$
is a skew field finite over $k$ acting on the left on $M$, we have
$A = \text{End}_L(M)$, and the centers of $A$ and $L$ agree.
Also $[A : k] [L : k] = \dim_k(M)^2$.
\item For a finite $A$-module $N$ the algebra $B = \text{End}_A(N)$ is a
matrix algebra over the skew field $L$ of (5). Moreover $\text{End}_B(N) = A$.
\end{enumerate}
\end{lemma}

\begin{proof}
By
Theorem \ref{theorem-wedderburn}
we can write $A = \text{Mat}(n \times n, K)$ for some finite skew
field extension $K$ of $k$. By
Lemma \ref{lemma-matrix-algebras}
the category of modules over $A$ is equivalent to the category of
modules over $K$. Thus (1), (2), and (3) hold
because every module over $K$ is free. Part (4) holds
because the equivalence transforms the $K$-module $K$
to $M = K^{\oplus n}$. Using $M = K^{\oplus n}$ in (5)
we see that $L = K^{op}$. The statement about the center of $L = K^{op}$
follows from
Lemma \ref{lemma-matrix-algebras}.
The statement about $\text{End}_L(M)$ follows from the explicit form
of $M$. The formula of dimensions is clear.
Part (6) follows as $N$ is isomorphic to a direct sum of
copies of a simple module.
\end{proof}

\begin{lemma}
```

Français restauré :

```tex
\label{lemma-simple-module-unique}
Soit $A$ une $k$-algèbre simple de dimension finie.
\begin{enumerate}
\item Il existe, à isomorphisme près, un unique $A$-module simple $M$.
\item Tout $A$-module de dimension finie est somme directe de copies
d'un module simple.
\item Deux $A$-modules de dimension finie sont isomorphes si et
seulement s'ils ont même dimension sur $k$.
\item Si $A = \text{Mat}(n \times n, K)$, où $K$ est un corps gauche de
dimension finie sur $k$, alors $M = K^{\oplus n}$ est un $A$-module simple et
$\text{End}_A(M) = K^{op}$.
\item Si $M$ est un $A$-module simple, alors $L = \text{End}_A(M)$ est un
corps gauche de dimension finie sur $k$ qui agit à gauche sur $M$, nous avons
$A = \text{End}_L(M)$, et les centres de $A$ et de $L$ coïncident.
En outre, $[A : k] [L : k] = \dim_k(M)^2$.
\item Pour tout $A$-module $N$ de dimension finie, l'algèbre
$B = \text{End}_A(N)$ est une algèbre de matrices sur le corps gauche $L$ du
point (5). De plus, $\text{End}_B(N) = A$.
\end{enumerate}
\end{lemma}

\begin{proof}
D'après le
théorème \ref{theorem-wedderburn},
nous pouvons écrire $A = \text{Mat}(n \times n, K)$ pour un corps gauche $K$
de dimension finie sur $k$. D'après le
lemme \ref{lemma-matrix-algebras},
la catégorie des modules sur $A$ est équivalente à celle des modules sur
$K$. Les points (1), (2) et (3) en résultent, puisque tout module sur $K$ est
libre. Le point (4) résulte de ce que cette équivalence transforme le $K$-module
$K$ en $M = K^{\oplus n}$. En prenant $M = K^{\oplus n}$ dans (5),
nous voyons que $L = K^{op}$. L'assertion sur le centre de $L = K^{op}$
résulte du
lemme \ref{lemma-matrix-algebras}.
L'assertion sur $\text{End}_L(M)$ résulte de la forme explicite de $M$.
La formule des dimensions est claire.
Le point (6) résulte du fait que $N$ est isomorphe à une somme directe de
copies d'un module simple.
\end{proof}

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0021

`lemma-tensor-simple` — source 321–337, cible 320–336.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L321) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Une seule des deux algèbres doit être à la fois finie et centrale ; le français conserve cette portée. Le choix de A' dans la preuve, sa présentation matricielle et les deux renvois sont inchangés. Il n'est pas ajouté de finitude à l'autre facteur.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-tensor-simple}
Let $A$, $A'$ be two simple $k$-algebras one of which is finite and central
over $k$. Then $A \otimes_k A'$ is simple.
\end{lemma}

\begin{proof}
Suppose that $A'$ is finite and central over $k$.
Write $A' = \text{Mat}(n \times n, K')$, see
Theorem \ref{theorem-wedderburn}.
Then the center of $K'$ is $k$ and we conclude that
$A \otimes_k K'$ is simple by
Lemma \ref{lemma-generate-two-sided-ideal}.
Hence $A \otimes_k A' = \text{Mat}(n \times n, A \otimes_k K')$ is simple
by Lemma \ref{lemma-matrix-algebras}.
\end{proof}

\begin{lemma}
```

Français restauré :

```tex
\label{lemma-tensor-simple}
Soient $A$ et $A'$ deux $k$-algèbres simples, dont l'une est centrale et de
dimension finie sur $k$. Alors $A \otimes_k A'$ est simple.
\end{lemma}

\begin{proof}
Supposons que $A'$ soit centrale et de dimension finie sur $k$.
Écrivons $A' = \text{Mat}(n \times n, K')$ ; voir le
théorème \ref{theorem-wedderburn}.
Le centre de $K'$ est alors $k$, et nous concluons que
$A \otimes_k K'$ est simple d'après le
lemme \ref{lemma-generate-two-sided-ideal}.
Par conséquent, $A \otimes_k A' = \text{Mat}(n \times n, A \otimes_k K')$
est simple d'après le lemme \ref{lemma-matrix-algebras}.
\end{proof}

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0022

`lemma-tensor-central-simple` — source 338–347, cible 337–346.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L338) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Le produit de deux algèbres correspond au produit binaire traité par les deux lemmes cités ; le pluriel anglais n'énonce pas ici un produit infini. La simplicité, la centralité et la finitude sont toutes conservées. Aucun développement mathématique n'est ajouté à la preuve par combinaison des deux résultats.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-tensor-central-simple}
The tensor product of finite central simple algebras over $k$ is finite,
central, and simple.
\end{lemma}

\begin{proof}
Combine Lemmas \ref{lemma-centralizer} and \ref{lemma-tensor-simple}.
\end{proof}

\begin{lemma}
```

Français restauré :

```tex
\label{lemma-tensor-central-simple}
Le produit tensoriel de deux algèbres centrales simples sur $k$ et de
dimension finie est une algèbre centrale simple de dimension finie.
\end{lemma}

\begin{proof}
Combiner les lemmes \ref{lemma-centralizer} et \ref{lemma-tensor-simple}.
\end{proof}

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0023

`lemma-base-change` — source 348–358, cible 347–357.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L348) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

L'extension k'/k reste quelconque : seule A est de dimension finie. La conclusion porte sur k', et non sur k. La preuve demeure le même renvoi aux deux lemmes. Les sources françaises attestent le cadre d'extension du corps de base sans remplacer les conventions de Stacks.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-base-change}
Let $A$ be a finite central simple algebra over $k$.
Let $k'/k$ be a field extension. Then $A' = A \otimes_k k'$ is
a finite central simple algebra over $k'$.
\end{lemma}

\begin{proof}
Combine Lemmas \ref{lemma-centralizer} and \ref{lemma-tensor-simple}.
\end{proof}

\begin{lemma}
```

Français restauré :

```tex
\label{lemma-base-change}
Soit $A$ une $k$-algèbre centrale simple de dimension finie.
Soit $k'/k$ une extension de corps. Alors $A' = A \otimes_k k'$ est une
$k'$-algèbre centrale simple de dimension finie.
\end{lemma}

\begin{proof}
Combiner les lemmes \ref{lemma-centralizer} et \ref{lemma-tensor-simple}.
\end{proof}

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0024

`lemma-inverse` — source 359–380, cible 358–379.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L359) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

L'algèbre opposée agit par multiplication à droite dans l'application vers les endomorphismes. La simplicité donne l'injectivité, puis l'égalité des dimensions conclut. La valeur n=[A:k] est conservée ; elle n'est pas remplacée par le degré défini plus loin.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-inverse}
Let $A$ be a finite central simple algebra over $k$.
Then $A \otimes_k A^{op} \cong \text{Mat}(n \times n, k)$
where $n = [A : k]$.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-tensor-central-simple} the algebra $A \otimes_k A^{op}$
is simple. Hence the map
$$
A \otimes_k A^{op} \longrightarrow \text{End}_k(A),\quad
a \otimes a' \longmapsto (x \mapsto axa')
$$
is injective. Since both sides of the arrow have the same dimension
we win.
\end{proof}





\section{The Brauer group of a field}
```

Français restauré :

```tex
\label{lemma-inverse}
Soit $A$ une $k$-algèbre centrale simple de dimension finie.
Alors $A \otimes_k A^{op} \cong \text{Mat}(n \times n, k)$,
où $n = [A : k]$.
\end{lemma}

\begin{proof}
D'après le lemme \ref{lemma-tensor-central-simple}, l'algèbre
$A \otimes_k A^{op}$ est simple. L'application
$$
A \otimes_k A^{op} \longrightarrow \text{End}_k(A),\quad
a \otimes a' \longmapsto (x \mapsto axa')
$$
est donc injective. Comme la source et le but de la flèche ont même dimension,
on conclut.
\end{proof}





\section{Le groupe de Brauer d'un corps}
```

</details>

### FR-BRAUER-PROSE-0025

`section-brauer` — source 381–390, cible 380–389.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L381) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Semblables traduit similar, avec les deux entiers strictement positifs et un isomorphisme de k-algèbres. Cette similitude de Brauer est distincte d'une simple ressemblance ou d'une conjugaison de matrices. Le vocabulaire est attesté chez Serre et Kahn ; la définition exacte reste celle de Stacks.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{section-brauer}

\noindent
Let $k$ be a field. Consider two finite central simple algebras
$A$ and $B$ over $k$. We say $A$ and $B$ are {\it similar} if there
exist $n, m > 0$ such that
$\text{Mat}(n \times n, A) \cong \text{Mat}(m \times m, B)$
as $k$-algebras.

\begin{lemma}
```

Français restauré :

```tex
\label{section-brauer}

\noindent
Soit $k$ un corps. Considérons deux algèbres centrales simples $A$ et $B$,
de dimension finie sur $k$. Nous disons que $A$ et $B$ sont {\it semblables}
s'il existe $n, m > 0$ tels que
$\text{Mat}(n \times n, A) \cong \text{Mat}(m \times m, B)$
comme $k$-algèbres.

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0026

`lemma-similar` — source 391–430, cible 390–432.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L391) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Les trois assertions, leur réduction à la troisième et l'usage des algèbres opposées sont conservés. Le paragraphe qui construit la loi de groupe est également lu : compatibilité du produit avec la similitude, associativité, commutativité, inverse et classe neutre. Il n'a pas été omis au motif qu'il se trouve hors d'un environnement de preuve.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-similar}
Similarity.
\begin{enumerate}
\item Similarity defines an equivalence relation on the set of isomorphism
classes of finite central simple algebras over $k$.
\item Every similarity class contains a unique (up to isomorphism)
finite central skew field extension of $k$.
\item If $A = \text{Mat}(n \times n, K)$ and $B = \text{Mat}(m \times m, K')$
for some finite central skew fields $K$, $K'$ over $k$
then $A$ and $B$ are similar if and only if $K \cong K'$ as $k$-algebras.
\end{enumerate}
\end{lemma}

\begin{proof}
Note that by Wedderburn's theorem (Theorem \ref{theorem-wedderburn})
we can always write a finite central simple algebra as a matrix
algebra over a finite central skew field. Hence it suffices to prove
the third assertion. To see this it suffices to show that if
$A = \text{Mat}(n \times n, K) \cong \text{Mat}(m \times m, K') = B$
then $K \cong K'$. To see this note that for a simple module $M$ of $A$
we have $\text{End}_A(M) = K^{op}$, see
Lemma \ref{lemma-simple-module-unique}.
Hence $A \cong B$ implies $K^{op} \cong (K')^{op}$ and we win.
\end{proof}

\noindent
Given two finite central simple $k$-algebras $A$, $B$ the tensor
product $A \otimes_k B$ is another, see
Lemma \ref{lemma-tensor-central-simple}.
Moreover if $A$ is similar to $A'$, then $A \otimes_k B$ is similar
to $A' \otimes_k B$ because tensor products and taking matrix
algebras commute. Hence tensor product defines an operation on
equivalence classes of finite central simple algebras which is clearly
associative and commutative. Finally,
Lemma \ref{lemma-inverse}
shows that $A \otimes_k A^{op}$ is isomorphic to a matrix algebra, i.e.,
that $A \otimes_k A^{op}$ is in the similarity class of $k$.
Thus we obtain an abelian group.

\begin{definition}
```

Français restauré :

```tex
\label{lemma-similar}
Similitude.
\begin{enumerate}
\item La similitude définit une relation d'équivalence sur l'ensemble des
classes d'isomorphisme de $k$-algèbres centrales simples de dimension finie.
\item Chaque classe de similitude contient, à isomorphisme près, un unique
corps gauche central de dimension finie sur $k$.
\item Si $A = \text{Mat}(n \times n, K)$ et
$B = \text{Mat}(m \times m, K')$ pour des corps gauches centraux $K$, $K'$
de dimension finie sur $k$, alors $A$ et $B$ sont semblables si et seulement
si $K \cong K'$ comme $k$-algèbres.
\end{enumerate}
\end{lemma}

\begin{proof}
Remarquons que, d'après le théorème de Wedderburn
(théorème \ref{theorem-wedderburn}), toute algèbre centrale simple de
dimension finie s'écrit comme une algèbre de matrices sur un corps gauche
central de dimension finie. Il suffit donc de prouver la troisième assertion.
Pour cela, il suffit de montrer que, si
$A = \text{Mat}(n \times n, K) \cong \text{Mat}(m \times m, K') = B$,
alors $K \cong K'$. En effet, si $M$ est un module simple sur $A$, nous avons
$\text{End}_A(M) = K^{op}$ ; voir le
lemme \ref{lemma-simple-module-unique}.
Par conséquent, $A \cong B$ implique $K^{op} \cong (K')^{op}$, d'où le
résultat.
\end{proof}

\noindent
Étant données deux $k$-algèbres centrales simples de dimension finie $A$ et
$B$, le produit tensoriel $A \otimes_k B$ en est encore une ; voir le
lemme \ref{lemma-tensor-central-simple}.
De plus, si $A$ est semblable à $A'$, alors $A \otimes_k B$ est semblable à
$A' \otimes_k B$, car le produit tensoriel commute à la formation des
algèbres de matrices. Le produit tensoriel définit donc une loi sur les
classes d'équivalence des algèbres centrales simples de dimension finie,
manifestement associative et commutative. Enfin, le
lemme \ref{lemma-inverse}
montre que $A \otimes_k A^{op}$ est isomorphe à une algèbre de matrices,
autrement dit que $A \otimes_k A^{op}$ appartient à la classe de similitude
de $k$. Nous obtenons ainsi un groupe abélien.

\begin{definition}
```

</details>

### FR-BRAUER-PROSE-0027

`definition-brauer-group` — source 431–449, cible 433–450.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L431) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

La définition concerne les classes de similitude, non les classes d'isomorphisme. L'application sous extension des scalaires, la variance covariante et la caractérisation du groupe nul sont conservées dans le paragraphe suivant. Nul est ici la trivialité du groupe ; trivial qualifie l'extension par un corps gauche.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{definition-brauer-group}
Let $k$ be a field. The {\it Brauer group} of $k$ is the abelian group
of similarity classes of finite central simple $k$-algebras defined
above. Notation $\text{Br}(k)$.
\end{definition}

\noindent
For any map of fields $k \to k'$ we obtain a group homomorphism
$$
\text{Br}(k) \longrightarrow \text{Br}(k'),\quad
A \longmapsto A \otimes_k k'
$$
see Lemma \ref{lemma-base-change}. In other words, $\text{Br}(-)$ is
a functor from the category of fields to the category of abelian groups.
Observe that the Brauer group
of a field is zero if and only if every finite central skew field
extension $k \subset K$ is trivial.

\begin{lemma}
```

Français restauré :

```tex
\label{definition-brauer-group}
Soit $k$ un corps. Le {\it groupe de Brauer} de $k$ est le groupe abélien des
classes de similitude des $k$-algèbres centrales simples de dimension finie
défini ci-dessus. On le note $\text{Br}(k)$.
\end{definition}

\noindent
Tout homomorphisme de corps $k \to k'$ fournit un homomorphisme de groupes
$$
\text{Br}(k) \longrightarrow \text{Br}(k'),\quad
A \longmapsto A \otimes_k k'
$$
par le lemme \ref{lemma-base-change}. Autrement dit, $\text{Br}(-)$ est un
foncteur de la catégorie des corps vers celle des groupes abéliens.
Remarquons que le groupe de Brauer d'un corps est nul si et seulement si toute
extension $k \subset K$, finie et centrale, par un corps gauche est triviale.

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0028

`lemma-brauer-algebraically-closed` — source 450–463, cible 451–464.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L450) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Integral devient intègre : il s'agit du sous-anneau commutatif de K, sans diviseur de zéro, et non seulement de l'intégralité d'une extension. La finitude dimensionnelle et le renvoi au lemme d'Algèbre restent présents. Le raisonnement pour chaque x, puis pour tout K, est inchangé. Ce choix est justifié par ce contexte et le lemme cité, sans nouvelle attestation externe revendiquée.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-brauer-algebraically-closed}
The Brauer group of an algebraically closed field is zero.
\end{lemma}

\begin{proof}
Let $k \subset K$ be a finite central skew field extension.
For any element $x \in K$ the subring $k[x] \subset K$ is a
commutative finite integral $k$-sub algebra, hence a field, see
Algebra, Lemma \ref{algebra-lemma-integral-over-field}.
Since $k$ is algebraically closed we conclude that
$k[x] = k$. Since $x$ was arbitrary we conclude $k = K$.
\end{proof}

\begin{lemma}
```

Français restauré :

```tex
\label{lemma-brauer-algebraically-closed}
Le groupe de Brauer d'un corps algébriquement clos est nul.
\end{lemma}

\begin{proof}
Soit $k \subset K$ une extension, finie et centrale, par un corps gauche.
Pour tout élément $x \in K$, le sous-anneau $k[x] \subset K$ est une
sous-$k$-algèbre commutative, intègre et de dimension finie ; c'est donc un
corps, voir Algèbre, lemme \ref{algebra-lemma-integral-over-field}.
Puisque $k$ est algébriquement clos, nous en déduisons que
$k[x] = k$. Comme $x$ était arbitraire, nous concluons que $k = K$.
\end{proof}

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0029

`lemma-dimension-square` — source 464–478, cible 465–475.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L464) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Carré conserve l'assertion sur la dimension totale de A. La preuve passe à la clôture algébrique et utilise le même résultat sur le groupe de Brauer. Elle ne prétend pas que A était déjà une algèbre de matrices sur k.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-dimension-square}
Let $A$ be a finite central simple algebra over a field $k$.
Then $[A : k]$ is a square.
\end{lemma}

\begin{proof}
This is true because $A \otimes_k \overline{k}$ is a matrix
algebra over $\overline{k}$ by
Lemma \ref{lemma-brauer-algebraically-closed}.
\end{proof}




\section{Skolem-Noether}
```

Français restauré :

```tex
\label{lemma-dimension-square}
Soit $A$ une algèbre centrale simple de dimension finie sur un corps $k$.
Alors $[A : k]$ est un carré.
\end{lemma}

\begin{proof}
Cela résulte de ce que $A \otimes_k \overline{k}$ est une algèbre de matrices
sur $\overline{k}$ d'après le
lemme \ref{lemma-brauer-algebraically-closed}.
\end{proof}
\section{Skolem-Noether}
```

</details>

### FR-BRAUER-PROSE-0030

`section-skolem-noether` — source 479–483, cible 476–480.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L479) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Titre et ouverture du théorème conservés. Aucun commentaire historique, hypothèse ou résultat n'est inséré dans cet intervalle de structure.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{section-skolem-noether}



\begin{theorem}
```

Français restauré :

```tex
\label{section-skolem-noether}



\begin{theorem}
```

</details>

### FR-BRAUER-PROSE-0031

`theorem-skolem-noether` — source 484–510, cible 481–507.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L484) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Les deux applications restent des homomorphismes de k-algèbres et la conjugaison garde le même sens. La preuve conserve les deux structures sur M, la finitude déduite pour B, l'isomorphisme des modules, l'application qui entrelace les actions et son appartenance au commutant de L. Entrelacer traduit la relation d'intertwining, non une simple bijection non compatible aux actions.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{theorem-skolem-noether}
Let $A$ be a finite central simple $k$-algebra. Let $B$ be a simple
$k$-algebra. Let $f, g : B \to A$ be two $k$-algebra homomorphisms.
Then there exists an invertible element $x \in A$ such that
$f(b) = xg(b)x^{-1}$ for all $b \in B$.
\end{theorem}

\begin{proof}
Choose a simple $A$-module $M$. Set $L = \text{End}_A(M)$.
Then $L$ is a skew field with center $k$ which acts on the left on $M$, see
Lemmas \ref{lemma-simple-module} and \ref{lemma-simple-module-unique}.
Then $M$ has two $B \otimes_k L^{op}$-module structures defined by
$m \cdot_1 (b \otimes l) = lmf(b)$ and $m \cdot_2 (b \otimes l) = lmg(b)$.
The $k$-algebra $B \otimes_k L^{op}$ is simple by
Lemma \ref{lemma-tensor-simple}. Since $B$ is simple, the existence of a
$k$-algebra homomorphism $B \to A$ implies that $B$ is finite. Thus
$B \otimes_k L^{op}$ is finite simple and we conclude the two
$B \otimes_k L^{op}$-module structures on $M$
are isomorphic by Lemma \ref{lemma-simple-module-unique}.
Hence we find $\varphi : M \to M$ intertwining these operations.
In particular $\varphi$ is in the commutant of $L$ which implies that
$\varphi$ is multiplication by some $x \in A$, see
Lemma \ref{lemma-simple-module-unique}. Working out the definitions we see
that $x$ is a solution to our problem.
\end{proof}

\begin{lemma}
```

Français restauré :

```tex
\label{theorem-skolem-noether}
Soit $A$ une $k$-algèbre centrale simple de dimension finie. Soit $B$ une
$k$-algèbre simple. Soient $f, g : B \to A$ deux homomorphismes de $k$-algèbres.
Alors il existe un élément inversible $x \in A$ tel que
$f(b) = xg(b)x^{-1}$ pour tout $b \in B$.
\end{theorem}

\begin{proof}
Choisissons un $A$-module simple $M$. Posons $L = \text{End}_A(M)$.
Alors $L$ est un corps gauche de centre $k$ qui agit à gauche sur $M$; voir les
lemmes \ref{lemma-simple-module} et \ref{lemma-simple-module-unique}.
Alors $M$ possède deux structures de $B \otimes_k L^{op}$-module définies par
$m \cdot_1 (b \otimes l) = lmf(b)$ et $m \cdot_2 (b \otimes l) = lmg(b)$.
La $k$-algèbre $B \otimes_k L^{op}$ est simple d'après le
lemme \ref{lemma-tensor-simple}. Comme $B$ est simple, l'existence d'un
homomorphisme de $k$-algèbres $B \to A$ implique que $B$ est de dimension finie. Ainsi
$B \otimes_k L^{op}$ est simple de dimension finie, et les deux structures de
$B \otimes_k L^{op}$-module sur $M$
sont isomorphes d'après le lemme \ref{lemma-simple-module-unique}.
Il existe donc $\varphi : M \to M$ entrelaçant ces actions.
En particulier, $\varphi$ appartient au centralisateur de $L$, ce qui implique que
$\varphi$ est la multiplication par un certain $x \in A$; voir le
lemme \ref{lemma-simple-module-unique}. En explicitant les définitions, on voit
que $x$ résout notre problème.
\end{proof}

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0032

`lemma-automorphism-inner` — source 511–524, cible 508–521.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L511) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Intérieur est attesté chez Serre. Les ajouts de k-algèbre ont déjà été retirés aux deux loci BRAUER-005A/B pour retrouver la généralité verbale de la source. Le corollaire de Serre précise au contraire k-automorphisme : c'est un motif d'avertissement séparé, pas une permission de modifier clandestinement Stacks. La preuve par Skolem-Noether est conservée.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-automorphism-inner}
Let $A$ be a finite central simple $k$-algebra. Any automorphism of $A$ is
inner. In particular, any automorphism of $\text{Mat}(n \times n, k)$
is inner.
\end{lemma}

\begin{proof}
The Skolem-Noether theorem (Theorem \ref{theorem-skolem-noether})
applies.
\end{proof}



\section{The centralizer theorem}
```

Français restauré :

```tex
\label{lemma-automorphism-inner}
Soit $A$ une $k$-algèbre centrale simple de dimension finie. Tout automorphisme de $A$ est
intérieur. En particulier, tout automorphisme de $\text{Mat}(n \times n, k)$
est intérieur.
\end{lemma}

\begin{proof}
Le théorème de Skolem-Noether (théorème \ref{theorem-skolem-noether})
s'applique.
\end{proof}



\section{Le théorème du centralisateur}
```

</details>

### FR-BRAUER-PROSE-0033

`section-centralizer` — source 525–528, cible 522–525.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L525) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Le titre annonce le centralisateur déjà défini. Il ne prétend pas introduire un autre objet que le commutant des sources françaises consultées. Aucun développement supplémentaire n'est ajouté.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{section-centralizer}


\begin{theorem}
```

Français restauré :

```tex
\label{section-centralizer}


\begin{theorem}
```

</details>

### FR-BRAUER-PROSE-0034

`theorem-centralizer` — source 529–566, cible 526–563.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L529) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Les trois assertions et les trois parties de preuve sont conservées. Les côtés des actions, les deux tailles matricielles m et n et les quatre égalités de dimensions sont inchangés. L'argument du double centralisateur et la comparaison des dimensions restent présents. La parenthèse déplacée dans B inclus dans C' provient du texte officiel ; elle n'est pas silencieusement déplacée dans une formule.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{theorem-centralizer}
Let $A$ be a finite central simple algebra over $k$, and let
$B$ be a simple subalgebra of $A$. Then
\begin{enumerate}
\item the centralizer $C$ of $B$ in $A$ is simple,
\item $[A : k] = [B : k][C : k]$, and
\item the centralizer of $C$ in $A$ is $B$.
\end{enumerate}
\end{theorem}

\begin{proof}
Throughout this proof we use the results of
Lemma \ref{lemma-simple-module-unique} freely.
Choose a simple $A$-module $M$. Set $L = \text{End}_A(M)$.
Then $L$ is a skew field with center $k$ which acts on the left on $M$
and $A = \text{End}_L(M)$.
Then $M$ is a right $B \otimes_k L^{op}$-module and
$C = \text{End}_{B \otimes_k L^{op}}(M)$.
Since the algebra $B \otimes_k L^{op}$ is simple by
Lemma \ref{lemma-tensor-simple} we see that $C$ is simple (by
Lemma \ref{lemma-simple-module-unique} again).

\medskip\noindent
Write $B \otimes_k L^{op} = \text{Mat}(m \times m, K)$ for some
skew field $K$ finite over $k$. Then $C = \text{Mat}(n \times n, K^{op})$
if $M$ is isomorphic to a direct sum of $n$ copies of the simple
$B \otimes_k L^{op}$-module $K^{\oplus m}$ (the lemma again). Thus we have
$\dim_k(M) = nm [K : k]$, $[B : k] [L : k] = m^2 [K : k]$,
$[C : k] = n^2 [K : k]$, and $[A : k] [L : k] = \dim_k(M)^2$ (by
the lemma again). We conclude that (2) holds.

\medskip\noindent
Part (3) follows because of (2) applied to $C \subset A$ shows
that $[B : k] = [C' : k]$ where $C'$ is the centralizer of $C$ in $A$
(and the obvious fact that $B \subset C')$.
\end{proof}

\begin{lemma}
```

Français restauré :

```tex
\label{theorem-centralizer}
Soit $A$ une algèbre centrale simple de dimension finie sur $k$, et soit
$B$ une sous-algèbre simple de $A$. Alors
\begin{enumerate}
\item le centralisateur $C$ de $B$ dans $A$ est simple,
\item $[A : k] = [B : k][C : k]$, et
\item le centralisateur de $C$ dans $A$ est $B$.
\end{enumerate}
\end{theorem}

\begin{proof}
Dans toute cette démonstration, nous utilisons librement les résultats du
lemme \ref{lemma-simple-module-unique}.
Choisissons un $A$-module simple $M$. Posons $L = \text{End}_A(M)$.
Alors $L$ est un corps gauche de centre $k$ qui agit à gauche sur $M$
et $A = \text{End}_L(M)$.
Alors $M$ est un $B \otimes_k L^{op}$-module à droite et
$C = \text{End}_{B \otimes_k L^{op}}(M)$.
Comme l'algèbre $B \otimes_k L^{op}$ est simple d'après le
lemme \ref{lemma-tensor-simple}, on voit que $C$ est simple (encore d'après le
lemme \ref{lemma-simple-module-unique}).

\medskip\noindent
Écrivons $B \otimes_k L^{op} = \text{Mat}(m \times m, K)$ pour un certain
corps gauche $K$ de dimension finie sur $k$. Alors $C = \text{Mat}(n \times n, K^{op})$
si $M$ est isomorphe à une somme directe de $n$ copies du
$B \otimes_k L^{op}$-module simple $K^{\oplus m}$ (encore d'après le lemme). Ainsi,
$\dim_k(M) = nm [K : k]$, $[B : k] [L : k] = m^2 [K : k]$,
$[C : k] = n^2 [K : k]$, et $[A : k] [L : k] = \dim_k(M)^2$ (encore d'après
le lemme). On en déduit (2).

\medskip\noindent
L'assertion (3) découle de (2) appliquée à $C \subset A$, qui montre
que $[B : k] = [C' : k]$, où $C'$ est le centralisateur de $C$ dans $A$
(ainsi que du fait évident que $B \subset C')$.
\end{proof}

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0035

`lemma-when-tensor-is-equal` — source 567–582, cible 564–579.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L567) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

La centralité de B demeure une hypothèse conditionnelle. La proposition incidente centrale simple sur C est déployée en français sans nouvelle hypothèse. BRAUER-006 a rétabli le signe égal de l'énoncé ; la preuve conclut toujours à un isomorphisme naturel. Cette différence de convention est documentée, sans présentation comme théorème faux.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-when-tensor-is-equal}
Let $A$ be a finite central simple algebra over $k$, and let
$B$ be a simple subalgebra of $A$. If $B$ is a central
$k$-algebra, then $A = B \otimes_k C$ where $C$ is the (central simple)
centralizer of $B$ in $A$.
\end{lemma}

\begin{proof}
We have $\dim_k(A) = \dim_k(B \otimes_k C)$ by
Theorem \ref{theorem-centralizer}. By
Lemma \ref{lemma-tensor-simple}
the tensor product is simple. Hence the natural map
$B \otimes_k C \to A$ is injective hence an isomorphism.
\end{proof}

\begin{lemma}
```

Français restauré :

```tex
\label{lemma-when-tensor-is-equal}
Soit $A$ une algèbre centrale simple de dimension finie sur $k$, et soit
$B$ une sous-algèbre simple de $A$. Si $B$ est une
$k$-algèbre centrale, alors $A = B \otimes_k C$, où $C$ est le centralisateur
de $B$ dans $A$, et ce centralisateur est central simple.
\end{lemma}

\begin{proof}
Nous avons $\dim_k(A) = \dim_k(B \otimes_k C)$ d'après le
théorème \ref{theorem-centralizer}. D'après le
lemme \ref{lemma-tensor-simple},
le produit tensoriel est simple. L'application naturelle
$B \otimes_k C \to A$ est donc injective, et par conséquent un isomorphisme.
\end{proof}

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0036

`lemma-self-centralizing-subfield` — source 583–599, cible 580–596.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L583) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Les trois conditions sont bien équivalentes, et non seulement impliquées dans un sens. Le centralisateur propre et le sous-anneau commutatif maximal sont distingués. Les deux phrases de preuve restent aussi brèves que dans la source ; aucune démonstration nouvelle n'est importée de Serre.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-self-centralizing-subfield}
Let $A$ be a finite central simple algebra over $k$.
If $K \subset A$ is a subfield, then the following are equivalent
\begin{enumerate}
\item $[A : k] = [K : k]^2$,
\item $K$ is its own centralizer, and
\item $K$ is a maximal commutative subring.
\end{enumerate}
\end{lemma}

\begin{proof}
Theorem \ref{theorem-centralizer}
shows that (1) and (2) are equivalent.
It is clear that (3) and (2) are equivalent.
\end{proof}

\begin{lemma}
```

Français restauré :

```tex
\label{lemma-self-centralizing-subfield}
Soit $A$ une algèbre centrale simple de dimension finie sur $k$.
Si $K \subset A$ est un sous-corps, les assertions suivantes sont équivalentes :
\begin{enumerate}
\item $[A : k] = [K : k]^2$,
\item $K$ est son propre centralisateur, et
\item $K$ est un sous-anneau commutatif maximal.
\end{enumerate}
\end{lemma}

\begin{proof}
Le théorème \ref{theorem-centralizer}
montre que (1) et (2) sont équivalentes.
Il est clair que (3) et (2) sont équivalentes.
\end{proof}

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0037

`lemma-maximal-subfield` — source 600–618, cible 597–615.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L600) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Sous-corps commutatif maximal rend maximal subfield dans un corps gauche : field est commutatif dans la source anglaise. Commutatif n'ajoute donc pas une restriction nouvelle à une notion anglaise de division ring. Le slogan, la dimension au carré et la preuve par le lemme précédent sont conservés.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-maximal-subfield}
\begin{slogan}
The dimension of a finite central skew field is the square of the dimension
of any maximal subfield.
\end{slogan}
Let $A$ be a finite central skew field over $k$.
Then every maximal subfield $K \subset A$ satisfies
$[A : k] = [K : k]^2$.
\end{lemma}

\begin{proof}
Special case of Lemma \ref{lemma-self-centralizing-subfield}.
\end{proof}





\section{Splitting fields}
```

Français restauré :

```tex
\label{lemma-maximal-subfield}
\begin{slogan}
La dimension d'un corps gauche central de dimension finie est le carré de celle
de tout sous-corps commutatif maximal.
\end{slogan}
Soit $A$ un corps gauche central de dimension finie sur $k$.
Alors tout sous-corps commutatif maximal $K \subset A$ satisfait
$[A : k] = [K : k]^2$.
\end{lemma}

\begin{proof}
C'est un cas particulier du lemme \ref{lemma-self-centralizing-subfield}.
\end{proof}





\section{Corps neutralisants}
```

</details>

### FR-BRAUER-PROSE-0038

`section-splitting` — source 619–622, cible 616–619.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L619) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Le titre Corps neutralisants suit la définition immédiatement suivante. Kahn atteste ce terme ; le corps de décomposition de Serre est une alternative historique équivalente dans ce contexte. Aucune préférence de source externe n'impose de retraduire un titre déjà fidèle.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{section-splitting}


\begin{definition}
```

Français restauré :

```tex
\label{section-splitting}


\begin{definition}
```

</details>

### FR-BRAUER-PROSE-0039

`definition-splitting` — source 623–634, cible 620–631.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L623) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Neutraliser signifie obtenir une algèbre de matrices après extension des scalaires ; cela ne signifie ni corps de décomposition d'un polynôme donné, ni clôture algébrique. La caractérisation par l'annulation de la classe de Brauer est conservée. Kahn A.2.1 et A.2.4 donnent l'attestation pertinente ; elle a été consultée rétrospectivement.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{definition-splitting}
Let $A$ be a finite central simple $k$-algebra.
We say a field extension $k'/k$ {\it splits} $A$, or
$k'$ is a {\it splitting field} for $A$ if $A \otimes_k k'$ is
a matrix algebra over $k'$.
\end{definition}

\noindent
Another way to say this is that the class of $A$ maps to zero
under the map $\text{Br}(k) \to \text{Br}(k')$.

\begin{theorem}
```

Français restauré :

```tex
\label{definition-splitting}
Soit $A$ une $k$-algèbre centrale simple de dimension finie.
On dit qu'une extension $k'/k$ {\it neutralise} $A$, ou que
$k'$ est un {\it corps neutralisant} de $A$, si $A \otimes_k k'$ est
une algèbre de matrices sur $k'$.
\end{definition}

\noindent
Autrement dit, la classe de $A$ a pour image zéro
par l'application $\text{Br}(k) \to \text{Br}(k')$.

\begin{theorem}
```

</details>

### FR-BRAUER-PROSE-0040

`theorem-splitting` — source 635–678, cible 632–675.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L635) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Les deux conditions, l'extension finie et la similitude sont conservées. La première direction passe par le centralisateur et les endomorphismes k'-linéaires. La seconde construit B, calcule les dimensions et obtient d'abord la classe opposée ; cette dernière réserve et le passage à l'algèbre opposée ne sont pas supprimés.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{theorem-splitting}
Let $A$ be a finite central simple $k$-algebra.
Let $k'/k$ be a finite field extension.
The following are equivalent
\begin{enumerate}
\item $k'$ splits $A$, and
\item there exists a finite central simple algebra $B$ similar to $A$
such that $k' \subset B$ and $[B : k] = [k' : k]^2$.
\end{enumerate}
\end{theorem}

\begin{proof}
Assume (2). It suffices to show that $B \otimes_k k'$ is a matrix
algebra. We know that $B \otimes_k B^{op} \cong \text{End}_k(B)$.
Since $k'$ is the centralizer of $k'$ in $B^{op}$ by
Lemma \ref{lemma-self-centralizing-subfield}
we see that $B \otimes_k k'$ is the centralizer of $k \otimes k'$
in $B \otimes_k B^{op} = \text{End}_k(B)$. Of course this centralizer
is just $\text{End}_{k'}(B)$ where we view $B$ as a $k'$ vector space
via the embedding $k' \to B$. Thus the result.

\medskip\noindent
Assume (1). This means that we have an isomorphism
$A \otimes_k k' \cong \text{End}_{k'}(V)$ for some $k'$-vector space $V$.
Let $B$ be the commutant of $A$ in $\text{End}_k(V)$. Note that
$k'$ sits in $B$. By
Lemma \ref{lemma-when-tensor-is-equal}
the classes of $A$ and $B$ add up to zero in $\text{Br}(k)$.
From the dimension formula in
Theorem \ref{theorem-centralizer}
we see that
$$
[B : k] [A : k] =
\dim_k(V)^2 =
[k' : k]^2 \dim_{k'}(V)^2 =
[k' : k]^2 [A : k].
$$
Hence $[B : k] = [k' : k]^2$. Thus we have proved the result for the
opposite to the Brauer class of $A$. However, $k'$ splits the Brauer
class of $A$ if and only if it splits
the Brauer class of the opposite algebra, so we win anyway.
\end{proof}

\begin{lemma}
```

Français restauré :

```tex
\label{theorem-splitting}
Soit $A$ une $k$-algèbre centrale simple de dimension finie.
Soit $k'/k$ une extension de corps finie.
Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item $k'$ neutralise $A$, et
\item il existe une algèbre $B$ centrale simple de dimension finie, semblable à $A$,
telle que $k' \subset B$ et $[B : k] = [k' : k]^2$.
\end{enumerate}
\end{theorem}

\begin{proof}
Supposons (2). Il suffit de montrer que $B \otimes_k k'$ est une algèbre de
matrices. Nous savons que $B \otimes_k B^{op} \cong \text{End}_k(B)$.
Comme $k'$ est le centralisateur de $k'$ dans $B^{op}$ d'après le
lemme \ref{lemma-self-centralizing-subfield},
on voit que $B \otimes_k k'$ est le centralisateur de $k \otimes k'$
dans $B \otimes_k B^{op} = \text{End}_k(B)$. Bien entendu, ce centralisateur
n'est autre que $\text{End}_{k'}(B)$, où l'on considère $B$ comme un espace vectoriel sur $k'$
au moyen du plongement $k' \to B$. D'où le résultat.

\medskip\noindent
Supposons (1). Cela signifie qu'il existe un isomorphisme
$A \otimes_k k' \cong \text{End}_{k'}(V)$ pour un certain espace vectoriel sur $k'$, noté $V$.
Soit $B$ le centralisateur de $A$ dans $\text{End}_k(V)$. Remarquons que
$k'$ est contenu dans $B$. D'après le
lemme \ref{lemma-when-tensor-is-equal},
la somme des classes de $A$ et de $B$ est nulle dans $\text{Br}(k)$.
La formule des dimensions du
théorème \ref{theorem-centralizer}
donne
$$
[B : k] [A : k] =
\dim_k(V)^2 =
[k' : k]^2 \dim_{k'}(V)^2 =
[k' : k]^2 [A : k].
$$
Ainsi, $[B : k] = [k' : k]^2$. Nous avons donc démontré le résultat pour la
classe opposée à la classe de Brauer de $A$. Cependant, $k'$ neutralise la classe de Brauer
de $A$ si et seulement s'il neutralise
la classe de Brauer de l'algèbre opposée, ce qui conclut dans tous les cas.
\end{proof}

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0041

`lemma-maximal-subfield-splits` — source 679–689, cible 676–686.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L679) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Le sous-corps est commutatif au même sens que dans la source ; sa maximalité implique la neutralisation par les deux résultats cités. La phrase n'est pas inversée : tout corps neutralisant n'est pas présenté comme un sous-corps maximal de K.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-maximal-subfield-splits}
A maximal subfield of a finite central skew field $K$ over $k$ is
a splitting field for $K$.
\end{lemma}

\begin{proof}
Combine Lemma \ref{lemma-maximal-subfield} with
Theorem \ref{theorem-splitting}.
\end{proof}

\begin{lemma}
```

Français restauré :

```tex
\label{lemma-maximal-subfield-splits}
Tout sous-corps commutatif maximal d'un corps gauche central $K$ de dimension finie sur $k$ est
un corps neutralisant de $K$.
\end{lemma}

\begin{proof}
Combiner le lemme \ref{lemma-maximal-subfield} avec le
théorème \ref{theorem-splitting}.
\end{proof}

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0042

`lemma-splitting-field-degree` — source 690–705, cible 687–702.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L690) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Divisible par d garde le sens de la divisibilité ; d n'est pas la dimension totale d². La preuve conserve B dans la même classe de Brauer, sa présentation matricielle et le calcul final. Aucune hypothèse de séparabilité ou de Galois n'est ajoutée au corps neutralisant.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-splitting-field-degree}
Consider a finite central skew field $K$ over $k$. Let $d^2 = [K : k]$.
For any finite splitting field $k'$ for $K$ the degree $[k' : k]$ is
divisible by $d$.
\end{lemma}

\begin{proof}
By Theorem \ref{theorem-splitting} there exists a finite central
simple algebra $B$ in the Brauer class of $K$ such that
$[B : k] = [k' : k]^2$. By
Lemma \ref{lemma-similar}
we see that $B = \text{Mat}(n \times n, K)$ for some $n$.
Then $[k' : k]^2 = n^2d^2$ whence the result.
\end{proof}

\begin{proposition}
```

Français restauré :

```tex
\label{lemma-splitting-field-degree}
Considérons un corps gauche central $K$ de dimension finie sur $k$. Soit $d^2 = [K : k]$.
Pour tout corps neutralisant fini $k'$ de $K$, le degré $[k' : k]$ est
divisible par $d$.
\end{lemma}

\begin{proof}
D'après le théorème \ref{theorem-splitting}, il existe une algèbre centrale
simple de dimension finie, notée $B$, dans la classe de Brauer de $K$, telle que
$[B : k] = [k' : k]^2$. D'après le
lemme \ref{lemma-similar},
on a $B = \text{Mat}(n \times n, K)$ pour un certain $n$.
Alors $[k' : k]^2 = n^2d^2$, d'où le résultat.
\end{proof}

\begin{proposition}
```

</details>

### FR-BRAUER-PROSE-0043

`proposition-separable-splitting-field` — source 706–767, cible 703–764.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L706) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Énoncé et démonstration entière lus. La séparabilité, la maximalité commutative, les cas de caractéristique nulle ou de corps fini, puis le cas infini de caractéristique positive sont conservés. Le domaine K de la supposition absurde est celui restauré par BRAUER-007, même s'il inclut k. La puissance uniforme, les polynômes, l'extension à la clôture algébrique et l'idempotent final sont présents. La coquille spitting ne demande pas une absurdité française : neutralisant conserve le sens du paragraphe. Les détails que Stacks omet restent annoncés comme omis.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{proposition-separable-splitting-field}
Consider a finite central skew field $K$ over $k$.
There exists a maximal subfield $k \subset k' \subset K$ which
is separable over $k$.
In particular, every Brauer class has a finite separable
spitting field.
\end{proposition}

\begin{proof}
Since every Brauer class is represented by a finite central skew
field over $k$, we see that the second statement follows from the
first by
Lemma \ref{lemma-maximal-subfield-splits}.

\medskip\noindent
To prove the first statement, suppose that we are given a separable
subfield $k' \subset K$. Then the centralizer $K'$ of $k'$ in $K$
has center $k'$, and the problem reduces to finding a maximal
subfield of $K'$ separable over $k'$. Thus it suffices to prove, if
$k \not = K$, that we can find an element $x \in K$, $x \not \in k$
which is separable over $k$. This statement is clear in characteristic
zero. Hence we may assume that $k$ has characteristic $p > 0$. If the
ground field $k$ is finite then, the result is clear as well (because
extensions of finite fields are always separable). Thus we may assume
that $k$ is an infinite field of positive characteristic.

\medskip\noindent
To get a contradiction assume no element of $K$ is separable over $k$.
By the discussion in
Fields, Section \ref{fields-section-algebraic}
this means the minimal polynomial of any $x \in K$ is of the form
$T^q - a$ where $q$ is a power of $p$ and $a \in k$. Since it is
clear that every element of $K$ has a minimal polynomial of degree
$\leq \dim_k(K)$ we conclude that there exists a fixed $p$-power
$q$ such that $x^q \in k$ for all $x \in K$.

\medskip\noindent
Consider the map
$$
(-)^q : K \longrightarrow K
$$
and write it out in terms of a $k$-basis $\{a_1, \ldots, a_n\}$ of $K$
with $a_1 = 1$. So
$$
(\sum x_i a_i)^q = \sum f_i(x_1, \ldots, x_n)a_i.
$$
Since multiplication on $K$ is $k$-bilinear we see that each $f_i$
is a polynomial in $x_1, \ldots, x_n$ (details omitted).
The choice of $q$ above and the fact that $k$ is infinite shows that
$f_i$ is identically zero for $i \geq 2$. Hence we see that it remains
zero on extending $k$ to its algebraic closure $\overline{k}$. But the
algebra $K \otimes_k \overline{k}$ is a matrix algebra (for example by
Lemmas \ref{lemma-base-change} and \ref{lemma-brauer-algebraically-closed}),
which implies there are some elements whose $q$th power is not central
(e.g., $e_{11}$). This is the desired contradiction.
\end{proof}

\noindent
The results above allow us to characterize finite central simple algebras
as follows.

\begin{lemma}
```

Français restauré :

```tex
\label{proposition-separable-splitting-field}
Considérons un corps gauche central $K$ de dimension finie sur $k$.
Il existe un sous-corps commutatif maximal $k \subset k' \subset K$ qui
est séparable sur $k$.
En particulier, toute classe de Brauer possède un corps neutralisant
fini et séparable.
\end{proposition}

\begin{proof}
Comme toute classe de Brauer est représentée par un corps gauche central de dimension
finie sur $k$, la seconde assertion découle de la
première et du
lemme \ref{lemma-maximal-subfield-splits}.

\medskip\noindent
Pour démontrer la première assertion, supposons donné un sous-corps séparable
$k' \subset K$. Alors le centralisateur $K'$ de $k'$ dans $K$
a pour centre $k'$, et le problème se ramène à trouver un sous-corps commutatif
maximal de $K'$ qui soit séparable sur $k'$. Il suffit donc de montrer que, si
$k \not = K$, on peut trouver un élément $x \in K$, $x \not \in k$,
qui soit séparable sur $k$. Cette assertion est claire en caractéristique
zéro. Nous pouvons donc supposer que $k$ est de caractéristique $p > 0$. Si le
corps de base $k$ est fini, le résultat est également clair (car les
extensions de corps finis sont toujours séparables). Nous pouvons donc supposer
que $k$ est un corps infini de caractéristique positive.

\medskip\noindent
Pour obtenir une contradiction, supposons qu'aucun élément de $K$ ne soit séparable sur $k$.
D'après la discussion de
Corps, section \ref{fields-section-algebraic},
cela signifie que le polynôme minimal de tout $x \in K$ est de la forme
$T^q - a$, où $q$ est une puissance de $p$ et $a \in k$. Comme il est
clair que tout élément de $K$ a un polynôme minimal de degré
$\leq \dim_k(K)$, on en conclut qu'il existe une puissance fixée de $p$, notée
$q$, telle que $x^q \in k$ pour tout $x \in K$.

\medskip\noindent
Considérons l'application
$$
(-)^q : K \longrightarrow K
$$
et exprimons-la dans une $k$-base $\{a_1, \ldots, a_n\}$ de $K$
avec $a_1 = 1$. Ainsi,
$$
(\sum x_i a_i)^q = \sum f_i(x_1, \ldots, x_n)a_i.
$$
Comme la multiplication dans $K$ est $k$-bilinéaire, chaque $f_i$
est un polynôme en $x_1, \ldots, x_n$ (nous omettons les détails).
Le choix de $q$ ci-dessus et le fait que $k$ soit infini montrent que
$f_i$ est identiquement nul pour $i \geq 2$. Cette annulation subsiste donc
après extension de $k$ à sa clôture algébrique $\overline{k}$. Mais
l'algèbre $K \otimes_k \overline{k}$ est une algèbre de matrices (par exemple d'après les
lemmes \ref{lemma-base-change} et \ref{lemma-brauer-algebraically-closed}),
ce qui implique qu'il existe des éléments dont la puissance $q$-ième n'est pas centrale
(par exemple $e_{11}$). C'est la contradiction cherchée.
\end{proof}

\noindent
Les résultats précédents permettent de caractériser les algèbres centrales simples de dimension
finie comme suit.

\begin{lemma}
```

</details>

### FR-BRAUER-PROSE-0044

`lemma-finite-central-simple-algebra` — source 768–817, cible 765–814.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L768) · [Français local](staged/fr/011_brauer.fr.tex) · [Paire exacte dans le registre](BRAUER_FULL_PROSE_CHOICES.json)

Les six conditions, les deux clôtures distinctes et l'extension galoisienne finie sont conservées. Le degré est d, non la dimension de A. La preuve garde toutes les implications, y compris la conclusion immédiate de (3) vers (1), sans l'étendre. Les commandes d'inclusion finale, bibliographie, style bibliographique et fermeture du document sont présentes. Aucun texte de fin n'est perdu.

<details>
<summary>Textes effectivement comparés : anglais et français</summary>

Anglais officiel :

```tex
\label{lemma-finite-central-simple-algebra}
Let $k$ be a field. For a $k$-algebra $A$ the following are equivalent
\begin{enumerate}
\item $A$ is finite central simple $k$-algebra,
\item $A$ is a finite dimensional $k$-vector space, $k$ is the center of $A$,
and $A$ has no nontrivial two-sided ideal,
\item there exists $d \geq 1$ such that
$A \otimes_k \bar k \cong \text{Mat}(d \times d, \bar k)$,
\item there exists $d \geq 1$ such that
$A \otimes_k k^{sep} \cong \text{Mat}(d \times d, k^{sep})$,
\item there exist $d \geq 1$ and a finite Galois extension $k'/k$
such that
$A \otimes_k k' \cong \text{Mat}(d \times d, k')$,
\item there exist $n \geq 1$ and a finite central skew field $K$
over $k$ such that $A \cong \text{Mat}(n \times n, K)$.
\end{enumerate}
The integer $d$ is called the {\it degree} of $A$.
\end{lemma}

\begin{proof}
The equivalence of (1) and (2) is a consequence of the definitions, see
Section \ref{section-algebras}.
Assume (1). By
Proposition \ref{proposition-separable-splitting-field}
there exists a separable splitting field $k \subset k'$ for $A$.
Of course, then a Galois closure of $k'/k$ is a splitting field also.
Thus we see that (1) implies (5). It is clear that (5) $\Rightarrow$ (4)
$\Rightarrow$ (3). Assume (3). Then $A \otimes_k \overline{k}$
is a finite central simple $\overline{k}$-algebra for example by
Lemma \ref{lemma-matrix-algebras}.
This trivially implies that $A$ is a finite central simple $k$-algebra.
Finally, the equivalence of (1) and (6) is Wedderburn's theorem, see
Theorem \ref{theorem-wedderburn}.
\end{proof}










\input{chapters}

\bibliography{my}
\bibliographystyle{amsalpha}

\end{document}
```

Français restauré :

```tex
\label{lemma-finite-central-simple-algebra}
Soit $k$ un corps. Pour une $k$-algèbre $A$, les assertions suivantes sont équivalentes :
\begin{enumerate}
\item $A$ est une $k$-algèbre centrale simple de dimension finie,
\item $A$ est un espace vectoriel de dimension finie sur $k$, $k$ est le centre de $A$,
et $A$ n'a aucun idéal bilatère non trivial,
\item il existe $d \geq 1$ tel que
$A \otimes_k \bar k \cong \text{Mat}(d \times d, \bar k)$,
\item il existe $d \geq 1$ tel que
$A \otimes_k k^{sep} \cong \text{Mat}(d \times d, k^{sep})$,
\item il existe $d \geq 1$ et une extension galoisienne finie $k'/k$
tels que
$A \otimes_k k' \cong \text{Mat}(d \times d, k')$,
\item il existe $n \geq 1$ et un corps gauche central $K$ de dimension finie
sur $k$ tels que $A \cong \text{Mat}(n \times n, K)$.
\end{enumerate}
L'entier $d$ est appelé le {\it degré} de $A$.
\end{lemma}

\begin{proof}
L'équivalence de (1) et (2) résulte des définitions; voir la
section \ref{section-algebras}.
Supposons (1). D'après la
proposition \ref{proposition-separable-splitting-field},
il existe un corps neutralisant séparable $k \subset k'$ de $A$.
Bien entendu, une clôture galoisienne de $k'/k$ est encore un corps neutralisant.
Ainsi, (1) implique (5). Il est clair que (5) $\Rightarrow$ (4)
$\Rightarrow$ (3). Supposons (3). Alors $A \otimes_k \overline{k}$
est une $\overline{k}$-algèbre centrale simple de dimension finie, par exemple d'après le
lemme \ref{lemma-matrix-algebras}.
Cela implique immédiatement que $A$ est une $k$-algèbre centrale simple de dimension finie.
Enfin, l'équivalence de (1) et (6) est le théorème de Wedderburn; voir le
théorème \ref{theorem-wedderburn}.
\end{proof}










\input{chapters}

\bibliography{my}
\bibliographystyle{amsalpha}

\end{document}
```

</details>

## Limites et suite

Ce contrôle conclut à la fidélité de la copie restaurée dans le périmètre lu. Il ne certifie pas la vérité des anomalies anglaises, une absence absolue d'erreur, toutes les attestations du registre, ni les autres chapitres. Les sept propositions source restent réversibles dans le dossier historique. La version française précédemment éditorialisée reste préservée et ne devient pas, par renommage, une traduction d'une révision déterminée de l'édition anglaise enrichie par IA.

Les vérifications cumulatives, les PDF, le LaTeX direct, les archives sources et la vérification des versions publiques restent à effectuer. Une relecture spécialisée est bienvenue ultérieurement, sans être une condition de poursuite.
