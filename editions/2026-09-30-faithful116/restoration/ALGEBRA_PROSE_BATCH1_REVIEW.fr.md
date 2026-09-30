# Algèbre commutative : fidélité des sept premières sections

## Portée exacte

Lecture complète des lignes anglaises 1-701 et françaises 1-696 : préambule, Introduction, Conventions, Notions de base, Lemme du serpent, Modules de type fini et de présentation finie, Morphismes de type fini et de présentation finie, Morphismes finis d’anneaux. Les 26 paires ci-dessous couvrent sans lacune tous les énoncés, preuves, listes et transitions de ce périmètre.

Quatre réparations de langue, aucune nouvelle correction mathématique du texte anglais. Les six restaurations historiques situées plus loin dans le chapitre sont conservées. Le suffixe à partir des Colimites est inchangé et n’est pas déclaré relu. Le chapitre entier, le PDF reconstruit et la publication restent inachevés.

Cette comparaison assistée par IA n’est pas une relecture humaine ni une certification de vérité mathématique. Les attestations ont été consultées rétrospectivement ; aucune consultation antérieure par le traducteur n’est inventée. Les points discutables sont signalés pour une éventuelle revue experte, sans attendre celle-ci pour poursuivre.

Référence immuable : `a04446e57ec1fbc252a871afcec7752fb2807b14`, `algebra.tex`, SHA-256 `FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3`.
Source française de travail : [010_algebra.prose-batch1.fr.tex](staged/fr/010_algebra.prose-batch1.fr.tex), 1,935,231 octets, SHA-256 `EA3D53F3C999780F46199C76F5A33BEF9270FF5CA2649E8CE4229E446B5ACE48`.
[Copie précédente conservée](staged/fr/010_algebra.fr.tex) · [Dossier historique](ALGEBRA_REVIEW.fr.md) · [Validation de ce lot](ALGEBRA_PROSE_BATCH1_VALIDATION.json) · [Choix structurés](ALGEBRA_PROSE_BATCH1_CHOICES.json) · [Occurrences exactes](ALGEBRA_PROSE_BATCH1_OCCURRENCES.json).

## Modifications limitées à la langue

### FR-ALGEBRA-B1-TRANSLATION-0001 — ligne française 129

Avant :
```tex
$I \subset R$ est {\it nilpotent} signifie que
```
Après :
```tex
Dire que l'idéal $I \subset R$ est {\it nilpotent} signifie que
```

Rétablir le sujet grammatical de signifie : c'est le fait de dire que l'idéal est nilpotent. L'existence d'un exposant commun reste celle de la source.

Alternative examinée : Des guillemets autour de la proposition auraient aussi réparé la syntaxe ; Dire que évite cette ponctuation longue.

### FR-ALGEBRA-B1-TRANSLATION-0002 — ligne française 133

Avant :
```tex
$I \subset R$ est {\it localement nilpotent} signifie que
```
Après :
```tex
Dire que l'idéal $I \subset R$ est {\it localement nilpotent} signifie que
```

Même réparation syntaxique. Tout élément est nilpotent reste une propriété élément par élément ; aucun exposant uniforme n'est ajouté.

Alternative examinée : Remplacer localement nilpotent par nilpotent changerait les mathématiques, non seulement le français.

### FR-ALGEBRA-B1-TRANSLATION-0003 — ligne française 307

Avant :
```tex
\cite[III, Lemma 3.3]{Cartan-Eilenberg}
```
Après :
```tex
\cite[III, Lemme 3.3]{Cartan-Eilenberg}
```

Localiser le nom du résultat cité. III, 3.3 et la clé Cartan-Eilenberg restent identiques ; l'ouvrage n'est pas prétendu nouvellement consulté.

Alternative examinée : Laisser Lemma conserverait le même renvoi mais un libellé anglais évitable.

### FR-ALGEBRA-B1-TRANSLATION-0004 — ligne française 624

Avant :
```tex
\section{Morphismes d'anneaux finis}
```
Après :
```tex
\section{Morphismes finis d'anneaux}
```

Rattacher sans ambiguïté finis à morphismes, comme dans Finite ring maps et la définition suivante. Il ne s'agit pas d'anneaux de cardinal fini.

Alternative examinée : L'ordre précédent se comprend en contexte mais peut faire lire anneaux finis. Ne pas remplacer fini par de type fini.

## Références françaises effectivement consultées

[Registre des passages, identités et limites](ALGEBRA_PROSE_BATCH1_CONSULTED_CANON.json).

### Olivier Debarre, Algèbre 2, ENS, 2012-2013

[FR-ALGEBRA-B1-CANON-DEBARRE](https://www.math.ens.psl.eu/~debarre/Algebre2.pdf) · [PDF préservé](canon-consulted/fr-fields/debarre-algebre2.pdf)

II.3, début p.44 ; III.1.1 et note 2 p.58 ; III.3.1 p.65 ; III.6 pp.82-84.

Courtes attestations : « de type fini », « anneau factoriel », « radical de I », « partie multiplicative », « corps résiduel ».

Génération finie des modules ; factoriel et UFD ; radical et réduit ; localisation permettant 0 ; corps résiduel comme corps des fractions du quotient premier.

Limites : Les passages servent au registre français, non à remplacer les conventions officielles. Les preuves continuant hors des pages lues ne sont pas dites entièrement consultées. Les fautes locales du cours, dont pour pour, ne sont pas copiées.

SHA-256 : `3FF86D7FD86BA2F1A349ACABE9E4FDDE57282B7A58D66A741CC78BE40E971CC0`.

### Henri Lombardi, Algèbre constructive, tutoriel JNCF, CIRM, novembre 2014

[FR-ALGEBRA-B1-CANON-LOMBARDI](https://www.cristal.univ-lille.fr/jncf2014/files/lecture-notes/lombardi.pdf) · [PDF préservé](canon-consulted/fr-algebra/lombardi-algebre-constructive-2014.pdf)

Définition 3.2 et fait 3.3 p.6 ; proposition 3.5 p.7. Couverture et deux pages complètes lues.

Courtes attestations : « de présentation finie », « module des relations », « annulateur ».

Présentation finie définie par une surjection libre à noyau de type fini ; nom du module des relations ; annulateur d’un élément.

Limites : La convention constructive de cohérence diffère explicitement de Bourbaki et n’est pas importée. La coquille A^n après A^m et la parenthèse manquante de 3.2 ne sont pas copiées. Les faits sans preuve ne valent pas lecture d’une preuve.

SHA-256 : `25FC73F21A24EF8AF8D19D3FA86A3156FC34D3CCD8D2A1556CE5DB993B46B723`.

### Coline Emprin, Topologie algébrique, TD8 : Algèbre homologique, ENS Paris, 2024-2025

[FR-ALGEBRA-B1-CANON-EMPRIN](https://www.math.ens.psl.eu/~cemprin/TD8-2025.pdf) · [PDF préservé](canon-consulted/fr-algebra/emprin-td8-2025.pdf)

Page 1 entière, exercices 1-2 ; surtout exercice 2 et ses diagrammes.

Courtes attestations : « Le lemme du serpent », « conoyau », « lignes sont exactes ».

Même configuration de noyaux/conoyaux et de suite exacte à six termes, dans des modules ; traduction des groupes abéliens de la source sans changement de diagramme.

Limites : Feuille d’exercices sans corrigé : aucune preuve du lemme n’est prétendue consultée. La faute de construction dans la dernière consigne n’est pas copiée.

SHA-256 : `752DDFE3EF4BB3AA5A454EB462DAF47D62903CE154DF756B9B6B7C57A7CB909D`.

## Règles de traduction et portée des attestations

### FR-ALGEBRA-B1-RULE-generation

Génération finie, non cardinalité finie. Le contexte distingue les coefficients de module et les générateurs d’algèbre ; les définitions anglaises fixent ces deux sens.

Références : FR-ALGEBRA-B1-CANON-DEBARRE, FR-ALGEBRA-B1-CANON-LOMBARDI.

### FR-ALGEBRA-B1-RULE-presentation

Attestation directe pour les modules en 3.2-3.3. Pour les algèbres, la définition officielle gouverne le contenu : relations idéales et non seulement module de relations.

Références : FR-ALGEBRA-B1-CANON-LOMBARDI.

### FR-ALGEBRA-B1-RULE-ideaux

Radical/réduit sont attestés p.65 ; idéaux premiers/maximaux pp.82-84. Le radical de Jacobson et la nilpotence locale suivent leurs définitions officielles sans attestation indépendante exhaustive revendiquée.

Références : FR-ALGEBRA-B1-CANON-DEBARRE.

### FR-ALGEBRA-B1-RULE-localisation

III.6 pp.82-84 : conserver les conditions sur S, les anneaux nuls et les images réciproques ; les notations ne créent pas une injection absente.

Références : FR-ALGEBRA-B1-CANON-DEBARRE.

### FR-ALGEBRA-B1-RULE-anneaux

Factoriel/UFD est attesté p.58, intégrité et diviseurs de zéro dans la localisation p.82. Unité désigne selon la phrase l’élément 1 ou un élément inversible ; ne pas confondre ces contextes.

Références : FR-ALGEBRA-B1-CANON-DEBARRE.

### FR-ALGEBRA-B1-RULE-exactitude

Emprin exercice 2, p.1 : noyaux, conoyaux et suite exacte. Courte est contrôlé par les deux zéros et les trois termes de la source ; ce qualificatif n’est pas cité comme attestation verbatim de cette feuille.

Références : FR-ALGEBRA-B1-CANON-EMPRIN.

### FR-ALGEBRA-B1-RULE-annulateur

Proposition 3.5 p.7 : annulateur d’un élément. Vérifier que l’élément et l’anneau de scalaires sont ceux de la formule.

Références : FR-ALGEBRA-B1-CANON-LOMBARDI.

### FR-ALGEBRA-B1-RULE-libre-cyclique

Libre est attesté p.44 et distingué de sans torsion. Pour cyclique, filtration et quotients successifs, le sens est contrôlé contre R/I et la chaîne de la source ; pas d’attestation externe nouvelle revendiquée.

Références : FR-ALGEBRA-B1-CANON-DEBARRE.

### FR-ALGEBRA-B1-RULE-morphisme-fini

La définition officielle definition-finite-ring-map gouverne : S est de type fini sur R comme module. Fini qualifie le morphisme et non la cardinalité des anneaux. Attestation externe exacte du syntagme non revendiquée dans ce lot.

Références : définition anglaise officielle, reproduite dans la paire.

## Passages complets, choix et motifs

Chaque bloc contient le passage anglais officiel et sa traduction actuelle, puis les motifs spécifiques. Les offsets exacts et les occurrences contextualisées sont dans les registres structurés. Les règles ne remplacent pas la lecture du passage.

### Passage 01 — Préambule

Source, lignes 1-19 ; français, lignes 1-20.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1) · identifiant `FR-ALGEBRA-B1-CHOICE-0001`.

Algèbre commutative traduit le titre sans élargissement. Préambule, ancre fantôme et table des matières sont conservés ; les lignes blanches n'ont pas de contenu mathématique.

Règles appliquées : traduction courante et contrôle direct du contenu.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\input{preamble}

% OK, start here.
%
\begin{document}

\title{Commutative Algebra}


\maketitle

\phantomsection
\label{section-phantom}

\tableofcontents
```

Texte français :
```tex
\input{preamble}

% OK, start here.
%
\begin{document}

\title{Algèbre commutative}


\maketitle

\phantomsection
\label{section-phantom}

\tableofcontents
```

</details>

### Passage 02 — section-introduction

Source, lignes 20-31 ; français, lignes 21-32.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L20) · identifiant `FR-ALGEBRA-B1-CHOICE-0002`.

L'annonce reste une introduction aux notions de base et conserve MatCA. Aucun programme plus vaste ni aucune référence nouvelle n'est ajouté.

Règles appliquées : traduction courante et contrôle direct du contenu.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\section{Introduction}
\label{section-introduction}

\noindent
Basic commutative algebra will be explained in this document.
A reference is \cite{MatCA}.
```

Texte français :
```tex
\section{Introduction}
\label{section-introduction}

\noindent
Les notions de base d'algèbre commutative seront exposées dans ce document.
Une référence est \cite{MatCA}.
```

</details>

### Passage 03 — section-conventions

Source, lignes 32-49 ; français, lignes 33-50.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L32) · identifiant `FR-ALGEBRA-B1-CHOICE-0003`.

Anneau commutatif avec unité inclut l'anneau nul. Premier est développé en idéal premier. L'intersection écrite R cap q désigne une image réciproque même pour un morphisme non injectif ; aucune inclusion n'est supposée. Debarre p.82 emploie un abus analogue pour la localisation, non une preuve de la convention générale.

Règles appliquées : FR-ALGEBRA-B1-RULE-ideaux, FR-ALGEBRA-B1-RULE-localisation, FR-ALGEBRA-B1-RULE-anneaux.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\section{Conventions}
\label{section-conventions}

\noindent
A ring is commutative with $1$. The zero ring is a ring. In fact it is
the only ring that does not have a prime ideal. The Kronecker
symbol $\delta_{ij}$ will be used. If $R \to S$ is a ring map and
$\mathfrak q$ a prime of $S$, then we use the notation
``$\mathfrak p = R \cap \mathfrak q$''
to indicate the prime which is the inverse image of $\mathfrak q$ under
$R \to S$ even if $R$ is not a subring of $S$ and even if $R \to S$
is not injective.
```

Texte français :
```tex
\section{Conventions}
\label{section-conventions}

\noindent
Un anneau est commutatif et possède un élément unité $1$. L'anneau nul est un anneau. En fait, c'est
le seul anneau qui ne possède pas d'idéal premier. Nous utiliserons le symbole
de Kronecker $\delta_{ij}$. Si $R \to S$ est un morphisme d'anneaux et si
$\mathfrak q$ est un idéal premier de $S$, nous employons alors la notation
``$\mathfrak p = R \cap \mathfrak q$''
pour désigner l'idéal premier qui est l'image réciproque de $\mathfrak q$ par
$R \to S$, même si $R$ n'est pas un sous-anneau de $S$ et même si $R \to S$
n'est pas injectif.
```

</details>

### Passage 04 — section-rings-basic

Source, lignes 50-60 ; français, lignes 51-61.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L50) · identifiant `FR-ALGEBRA-B1-CHOICE-0004`.

La liste ne prétend définir toutes les notions. Le conseil de consulter un texte élémentaire et la distinction entre notions définies et présupposées restent présents ; aucune explication mathématique n'est ajoutée.

Règles appliquées : traduction courante et contrôle direct du contenu.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\section{Basic notions}
\label{section-rings-basic}

\noindent
The following is a list of basic notions in commutative algebra. Some of these
notions are discussed in more detail in the text that follows and some are
defined in the list, but others are considered basic and will not be defined.
If you are not familiar with most of the italicized concepts, then we suggest
looking at an introductory text on algebra before continuing.

\begin{enumerate}
```

Texte français :
```tex
\section{Notions de base}
\label{section-rings-basic}

\noindent
Voici une liste de notions de base d'algèbre commutative. Certaines de ces
notions sont étudiées plus en détail dans la suite du texte et certaines sont
définies dans la liste, mais d'autres sont considérées comme élémentaires et ne seront pas définies.
Si la plupart des notions en italique ne vous sont pas familières, nous vous conseillons
de consulter un texte d'introduction à l'algèbre avant de poursuivre.

\begin{enumerate}
```

</details>

### Passage 05 — item-ring

Source, lignes 61-102 ; français, lignes 62-103.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L61) · identifiant `FR-ALGEBRA-B1-CHOICE-0005`.

Unité, diviseur de zéro, nilpotent et idempotent restent distincts ; les deux idempotents triviaux 0 et 1 sont conservés. Fini, de type fini et de présentation finie ne sont pas confondus. Anneau intègre et anneau factoriel évitent des calques ; Debarre III.1.1 et sa note 2 attestent précisément factoriel/UFD. Les sigles PID, UFD et dvr de la source demeurent. Aucune hypothèse supplémentaire d'intégrité n'est ajoutée.

Règles appliquées : FR-ALGEBRA-B1-RULE-generation, FR-ALGEBRA-B1-RULE-presentation, FR-ALGEBRA-B1-RULE-ideaux, FR-ALGEBRA-B1-RULE-anneaux, FR-ALGEBRA-B1-RULE-morphisme-fini.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\item $R$ is a {\it ring},
\label{item-ring}
\item $x\in R$ is {\it nilpotent},
\label{item-ring-element-nilpotent}
\item $x\in R$ is a {\it zerodivisor},
\label{item-ring-element-zerodivisor}
\item $x\in R$ is a {\it unit},
\label{item-ring-element-unit}
\item $e \in R$ is an {\it idempotent},
\label{item-ring-element-idempotent}
\item an idempotent $e \in R$ is called {\it trivial} if $e = 1$ or $e = 0$,
\label{item-idempotent-trivial}
\item $\varphi : R_1 \to R_2$ is a {\it ring homomorphism},
\label{item-ring-homomorphism}
\item
\label{item-ring-homomorphism-finite-presentation}
$\varphi : R_1 \to R_2$ is {\it of finite presentation}, or
{\it $R_2$ is a finitely presented $R_1$-algebra},
see Definition \ref{definition-finite-type},
\item
\label{item-ring-homomorphism-finite-type}
$\varphi : R_1 \to R_2$ is {\it of finite type}, or
{\it $R_2$ is a finite type $R_1$-algebra},
see Definition \ref{definition-finite-type},
\item
\label{item-ring-homomorphism-finite}
$\varphi : R_1 \to R_2$ is {\it finite}, or
{\it $R_2$ is a finite $R_1$-algebra},
\item $R$ is a {\it (integral) domain},
\label{item-ring-domain}
\item $R$ is {\it reduced},
\label{item-ring-reduced}
\item $R$ is {\it Noetherian},
\label{item-ring-Noetherian}
\item $R$ is a {\it principal ideal domain} or a {\it PID},
\label{item-ring-PID}
\item $R$ is a {\it Euclidean domain},
\label{item-ring-Euclidean}
\item $R$ is a {\it unique factorization domain} or a {\it UFD},
\label{item-ring-UFD}
\item $R$ is a {\it discrete valuation ring} or a {\it dvr},
\label{item-ring-dvr}
```

Texte français :
```tex
\item $R$ est un {\it anneau},
\label{item-ring}
\item $x\in R$ est {\it nilpotent},
\label{item-ring-element-nilpotent}
\item $x\in R$ est un {\it diviseur de zéro},
\label{item-ring-element-zerodivisor}
\item $x\in R$ est une {\it unité},
\label{item-ring-element-unit}
\item $e \in R$ est un {\it idempotent},
\label{item-ring-element-idempotent}
\item un idempotent $e \in R$ est dit {\it trivial} si $e = 1$ ou $e = 0$,
\label{item-idempotent-trivial}
\item $\varphi : R_1 \to R_2$ est un {\it homomorphisme d'anneaux},
\label{item-ring-homomorphism}
\item
\label{item-ring-homomorphism-finite-presentation}
$\varphi : R_1 \to R_2$ est {\it de présentation finie}, ou
{\it $R_2$ est une $R_1$-algèbre de présentation finie},
voir la Définition \ref{definition-finite-type},
\item
\label{item-ring-homomorphism-finite-type}
$\varphi : R_1 \to R_2$ est {\it de type fini}, ou
{\it $R_2$ est une $R_1$-algèbre de type fini},
voir la Définition \ref{definition-finite-type},
\item
\label{item-ring-homomorphism-finite}
$\varphi : R_1 \to R_2$ est {\it fini}, ou
{\it $R_2$ est une $R_1$-algèbre finie},
\item $R$ est un {\it anneau intègre},
\label{item-ring-domain}
\item $R$ est {\it réduit},
\label{item-ring-reduced}
\item $R$ est {\it noethérien},
\label{item-ring-Noetherian}
\item $R$ est un {\it anneau principal} ou un {\it PID},
\label{item-ring-PID}
\item $R$ est un {\it anneau euclidien},
\label{item-ring-Euclidean}
\item $R$ est un {\it anneau factoriel} ou un {\it UFD},
\label{item-ring-UFD}
\item $R$ est un {\it anneau de valuation discrète} ou un {\it dvr},
\label{item-ring-dvr}
```

</details>

### Passage 06 — item-field

Source, lignes 103-119 ; français, lignes 104-120.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L103) · identifiant `FR-ALGEBRA-B1-CHOICE-0006`.

Corps, extension algébrique, base et degré de transcendance gardent leurs objets et leur portée. Le prolongement dans un corps algébriquement clos conserve les deux hypothèses d'extension, sans finitude ajoutée. Les pages de canon nouvellement consultées ne sont pas présentées comme attestant tous ces termes.

Point à rendre visible pour la revue : Attestation externe non exhaustive dans ce lot ; les formules et hypothèses sont comparées directement à l'anglais.

Règles appliquées : traduction courante et contrôle direct du contenu.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\item $K$ is a {\it field},
\label{item-field}
\item $L/K$ is a {\it field extension},
\label{item-field-extension}
\item $L/K$ is an {\it algebraic field extension},
\label{item-field-extension-algebraic}
\item $\{t_i\}_{i\in I}$ is a {\it transcendence basis} for $L$ over $K$,
\label{item-transcendence-basis}
\item the {\it transcendence degree} $\text{trdeg}(L/K)$ of $L$ over $K$,
\label{item-transcendence-degree}
\item the field $k$ is {\it algebraically closed},
\label{item-algebraically-closed}
\item
\label{item-extend-into-algebraically-closed}
if $L/K$ is algebraic, and $\Omega/K$ an extension with $\Omega$
algebraically closed,
then there exists a ring map $L \to \Omega$ extending the map on $K$,
```

Texte français :
```tex
\item $K$ est un {\it corps},
\label{item-field}
\item $L/K$ est une {\it extension de corps},
\label{item-field-extension}
\item $L/K$ est une {\it extension algébrique de corps},
\label{item-field-extension-algebraic}
\item $\{t_i\}_{i\in I}$ est une {\it base de transcendance} de $L$ sur $K$,
\label{item-transcendence-basis}
\item le {\it degré de transcendance} $\text{trdeg}(L/K)$ de $L$ sur $K$,
\label{item-transcendence-degree}
\item le corps $k$ est {\it algébriquement clos},
\label{item-algebraically-closed}
\item
\label{item-extend-into-algebraically-closed}
si $L/K$ est algébrique et si $\Omega/K$ est une extension avec $\Omega$
algébriquement clos,
alors il existe un morphisme d'anneaux $L \to \Omega$ qui prolonge le morphisme sur $K$,
```

</details>

### Passage 07 — item-ideal

Source, lignes 120-175 ; français, lignes 121-176.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L120) · identifiant `FR-ALGEBRA-B1-CHOICE-0007`.

Idéal radical, radical d'un idéal et radical de Jacobson ne sont pas fusionnés. L'exposant commun de I puissance n nulle distingue nilpotent de localement nilpotent, propriété de chaque élément. Deux phrases mal construites sont réparées par Dire que, sans changer les quantificateurs. Le radical de Jacobson reste l'intersection des idéaux maximaux. Image réciproque d'un idéal et idéal engendré par son image ne sont pas intervertis. L'anneau non nul garde cette restriction.

Point à rendre visible pour la revue : Pas d'attestation exacte nouvelle pour localement nilpotent ou radical de Jacobson dans les pages lues. La définition officielle fixe le sens conservé.

Règles appliquées : FR-ALGEBRA-B1-RULE-ideaux.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\item $I \subset R$ is an {\it ideal},
\label{item-ideal}
\item $I \subset R$ is {\it radical},
\label{item-ideal-radical}
\item if $I$ is an ideal then we have its {\it radical} $\sqrt{I}$,
\label{item-radical-ideal}
\item
\label{item-ideal-nilpotent}
$I \subset R$ is {\it nilpotent} means that $I^n = 0$ for
some $n \in \mathbf{N}$,
\item
\label{item-ideal-locally-nilpotent}
$I \subset R$ is {\it locally nilpotent} means that every
element of $I$ is nilpotent,
\item $\mathfrak p \subset R$ is a {\it prime ideal},
\label{item-prime-ideal}
\item
\label{item-prime-product-ideals}
if $\mathfrak p \subset R$ is prime and if $I, J \subset R$
are ideal, and if $IJ\subset \mathfrak p$, then
$I \subset \mathfrak p$ or $J \subset \mathfrak p$.
\item $\mathfrak m \subset R$ is a {\it maximal ideal},
\label{item-maximal-ideal}
\item any nonzero ring has a maximal ideal,
\label{item-exists-maximal-ideal}
\item
\label{item-jacobson-radical}
the {\it Jacobson radical} of $R$ is $\text{rad}(R) =
\bigcap_{\mathfrak m \subset R} \mathfrak m$ the intersection
of all the maximal ideals of $R$,
\item the ideal $(T)$ {\it generated} by a subset $T \subset R$,
\label{item-ideal-generated-by}
\item the {\it quotient ring} $R/I$,
\label{item-quotient-ring}
\item an ideal $I$ in the ring $R$ is prime if and only if $R/I$ is a domain,
\label{item-characterize-prime-ideal}
\item
\label{item-characterize-maximal-ideal}
an ideal $I$ in the ring $R$ is maximal if and only if the
ring $R/I$ is a field,
\item
\label{item-inverse-image-ideal}
if $\varphi : R_1 \to R_2$ is a ring homomorphism, and if
$I \subset R_2$ is an ideal, then $\varphi^{-1}(I)$ is an
ideal of $R_1$,
\item
\label{item-image-ideal}
if $\varphi : R_1 \to R_2$ is a ring homomorphism, and if
$I \subset R_1$ is an ideal, then $\varphi(I) \cdot R_2$ (sometimes
denoted $I \cdot R_2$, or $IR_2$) is the ideal of $R_2$ generated
by $\varphi(I)$,
\item
\label{item-inverse-image-prime}
if $\varphi : R_1 \to R_2$ is a ring homomorphism, and if
$\mathfrak p \subset R_2$ is a prime ideal, then
$\varphi^{-1}(\mathfrak p)$ is a prime ideal of $R_1$,
```

Texte français :
```tex
\item $I \subset R$ est un {\it idéal},
\label{item-ideal}
\item $I \subset R$ est {\it radical},
\label{item-ideal-radical}
\item si $I$ est un idéal, nous disposons de son {\it radical} $\sqrt{I}$,
\label{item-radical-ideal}
\item
\label{item-ideal-nilpotent}
Dire que l'idéal $I \subset R$ est {\it nilpotent} signifie que $I^n = 0$ pour
un certain $n \in \mathbf{N}$,
\item
\label{item-ideal-locally-nilpotent}
Dire que l'idéal $I \subset R$ est {\it localement nilpotent} signifie que tout
élément de $I$ est nilpotent,
\item $\mathfrak p \subset R$ est un {\it idéal premier},
\label{item-prime-ideal}
\item
\label{item-prime-product-ideals}
si $\mathfrak p \subset R$ est premier, si $I, J \subset R$
sont des idéaux et si $IJ\subset \mathfrak p$, alors
$I \subset \mathfrak p$ ou $J \subset \mathfrak p$.
\item $\mathfrak m \subset R$ est un {\it idéal maximal},
\label{item-maximal-ideal}
\item tout anneau non nul possède un idéal maximal,
\label{item-exists-maximal-ideal}
\item
\label{item-jacobson-radical}
le {\it radical de Jacobson} de $R$ est $\text{rad}(R) =
\bigcap_{\mathfrak m \subset R} \mathfrak m$, l'intersection
de tous les idéaux maximaux de $R$,
\item l'idéal $(T)$ {\it engendré} par un sous-ensemble $T \subset R$,
\label{item-ideal-generated-by}
\item l'{\it anneau quotient} $R/I$,
\label{item-quotient-ring}
\item un idéal $I$ de l'anneau $R$ est premier si et seulement si $R/I$ est intègre,
\label{item-characterize-prime-ideal}
\item
\label{item-characterize-maximal-ideal}
un idéal $I$ de l'anneau $R$ est maximal si et seulement si
l'anneau $R/I$ est un corps,
\item
\label{item-inverse-image-ideal}
si $\varphi : R_1 \to R_2$ est un homomorphisme d'anneaux et si
$I \subset R_2$ est un idéal, alors $\varphi^{-1}(I)$ est un
idéal de $R_1$,
\item
\label{item-image-ideal}
si $\varphi : R_1 \to R_2$ est un homomorphisme d'anneaux et si
$I \subset R_1$ est un idéal, alors $\varphi(I) \cdot R_2$ (parfois
noté $I \cdot R_2$ ou $IR_2$) est l'idéal de $R_2$ engendré
par $\varphi(I)$,
\item
\label{item-inverse-image-prime}
si $\varphi : R_1 \to R_2$ est un homomorphisme d'anneaux et si
$\mathfrak p \subset R_2$ est un idéal premier, alors
$\varphi^{-1}(\mathfrak p)$ est un idéal premier de $R_1$,
```

</details>

### Passage 08 — item-module

Source, lignes 176-199 ; français, lignes 177-200.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L176) · identifiant `FR-ALGEBRA-B1-CHOICE-0008`.

Finite module devient module de type fini, jamais module de cardinal fini : Debarre II.3 p.44 donne la famille génératrice finie. L'annulateur concerne l'élément m et non le module entier, comme Lombardi 3.5. Libre n'est pas remplacé par sans torsion ; dans la suite exacte K et M libres impliquent L libre. Les quotients successifs du troisième théorème d'isomorphisme sont inchangés.

Règles appliquées : FR-ALGEBRA-B1-RULE-generation, FR-ALGEBRA-B1-RULE-presentation, FR-ALGEBRA-B1-RULE-exactitude, FR-ALGEBRA-B1-RULE-annulateur, FR-ALGEBRA-B1-RULE-libre-cyclique.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\item $M$ is an {\it $R$-module},
\label{item-module}
\item
\label{item-annihilator}
for $m \in M$ the {\it annihilator}
$I = \{f \in R \mid fm = 0\}$ of $m$ in $R$,
\item $N \subset M$ is an {\it $R$-submodule},
\label{item-submodule}
\item $M$ is a {\it Noetherian $R$-module},
\label{item-Noetherian-module}
\item $M$ is a {\it finite $R$-module},
\label{item-finite-module}
\item $M$ is a {\it finitely generated $R$-module},
\label{item-finitely-generated-module}
\item $M$ is a {\it finitely presented $R$-module},
\label{item-finitely-presented-module}
\item $M$ is a {\it free $R$-module},
\label{item-free-module}
\item
\label{item-extension-free}
if $0 \to K \to L \to M \to 0$ is a short exact sequence
of $R$-modules and $K$, $M$ are free, then $L$ is free,
\item if $N \subset M \subset L$ are $R$-modules, then $L/M = (L/N)/(M/N)$,
\label{item-isomorphism-theorem}
```

Texte français :
```tex
\item $M$ est un {\it $R$-module},
\label{item-module}
\item
\label{item-annihilator}
pour $m \in M$, l'{\it annulateur}
$I = \{f \in R \mid fm = 0\}$ de $m$ dans $R$,
\item $N \subset M$ est un {\it $R$-sous-module},
\label{item-submodule}
\item $M$ est un {\it $R$-module noethérien},
\label{item-Noetherian-module}
\item $M$ est un {\it $R$-module de type fini},
\label{item-finite-module}
\item $M$ est un {\it $R$-module engendré par un nombre fini d'éléments},
\label{item-finitely-generated-module}
\item $M$ est un {\it $R$-module de présentation finie},
\label{item-finitely-presented-module}
\item $M$ est un {\it $R$-module libre},
\label{item-free-module}
\item
\label{item-extension-free}
si $0 \to K \to L \to M \to 0$ est une suite exacte courte
de $R$-modules et si $K$, $M$ sont libres, alors $L$ est libre,
\item si $N \subset M \subset L$ sont des $R$-modules, alors $L/M = (L/N)/(M/N)$,
\label{item-isomorphism-theorem}
```

</details>

### Passage 09 — item-multiplicative-subset

Source, lignes 200-263 ; français, lignes 201-264.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L200) · identifiant `FR-ALGEBRA-B1-CHOICE-0009`.

Partie multiplicative permet 0, comme Debarre pp.82-84 ; ajouter son exclusion contredirait l'assertion sur l'anneau nul. L'injectivité exige des non-diviseurs de zéro. Les produits de parties, images, images réciproques, exactitude et surjectivité sont conservés sans hypothèse de finitude. S barre dans la formule des anneaux et S dans celle des modules restent tels qu'imprimés. Les notations R_f et R_p sont stables.

Règles appliquées : FR-ALGEBRA-B1-RULE-ideaux, FR-ALGEBRA-B1-RULE-localisation, FR-ALGEBRA-B1-RULE-anneaux.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\item $S$ is a {\it multiplicative subset of $R$},
\label{item-multiplicative-subset}
\item the {\it localization} $R \to S^{-1}R$ of $R$,
\label{item-localization-ring}
\item
\label{item-localization-zero}
if $R$ is a ring and $S$ is a multiplicative subset
of $R$ then $S^{-1}R$ is the zero ring if and only if $S$ contains $0$,
\item
\label{item-localize-nonzerodivisors}
if $R$ is a ring and if the multiplicative subset $S$
consists completely of nonzerodivisors, then $R \to S^{-1}R$
is injective,
\item if $\varphi : R_1 \to R_2$ is a ring homomorphism, and
$S$ is a multiplicative subset of $R_1$, then $\varphi(S)$ is
a multiplicative subset of $R_2$,
\item
\label{item-products-multiplicative-subsets}
if $S$, $S'$ are multiplicative subsets of $R$,
and if $SS'$ denotes the set of products $SS' =
\{r \in R \mid \exists s\in S, \exists s' \in S', r = ss'\}$
then $SS'$ is a multiplicative subset of $R$,
\item
\label{item-localization-localization}
if $S$, $S'$ are multiplicative subsets of $R$,
and if $\overline{S}$ denotes the image of $S$ in $(S')^{-1}R$,
then $(SS')^{-1}R = \overline{S}^{-1}((S')^{-1}R)$,
\item the {\it localization} $S^{-1}M$ of the $R$-module $M$,
\label{item-localization-module}
\item
\label{item-localization-exact}
the functor $M \mapsto S^{-1}M$ preserves injective maps,
surjective maps, and exactness,
\item
\label{item-localization-localization-module}
if $S$, $S'$ are multiplicative subsets of $R$,
and if $M$ is an $R$-module, then
$(SS')^{-1}M = S^{-1}((S')^{-1}M)$,
\item
\label{item-localize-ideal}
if $R$ is a ring, $I$ an ideal of $R$, and $S$ a multiplicative
subset of $R$, then $S^{-1}I$ is an ideal of $S^{-1}R$, and we have
$S^{-1}R/S^{-1}I = \overline{S}^{-1}(R/I)$, where $\overline{S}$
is the image of $S$ in $R/I$,
\item
\label{item-ideal-in-localization}
if $R$ is a ring, and $S$ a multiplicative
subset of $R$, then any ideal $I'$ of $S^{-1}R$ is
of the form $S^{-1}I$, where one can take $I$ to be
the inverse image of $I'$ in $R$,
\item
\label{item-submodule-in-localization}
if $R$ is a ring, $M$ an $R$-module, and $S$ a multiplicative
subset of $R$, then any submodule $N'$ of $S^{-1}M$ is of the form
$S^{-1}N$ for some submodule $N \subset M$, where
one can take $N$ to be the inverse image of $N'$ in $M$,
\item if $S = \{1, f, f^2, \ldots\}$ then $R_f = S^{-1}R$ and $M_f = S^{-1}M$,
\label{item-localize-f}
\item
\label{item-localize-p}
if $S = R \setminus \mathfrak p = \{x\in R \mid x\not\in \mathfrak p\}$
for some prime ideal $\mathfrak p$,
then it is customary to denote $R_{\mathfrak p} = S^{-1}R$
and $M_{\mathfrak p} = S^{-1}M$,
```

Texte français :
```tex
\item $S$ est une {\it partie multiplicative de $R$},
\label{item-multiplicative-subset}
\item la {\it localisation} $R \to S^{-1}R$ de $R$,
\label{item-localization-ring}
\item
\label{item-localization-zero}
si $R$ est un anneau et si $S$ est une partie multiplicative
de $R$, alors $S^{-1}R$ est l'anneau nul si et seulement si $S$ contient $0$,
\item
\label{item-localize-nonzerodivisors}
si $R$ est un anneau et si la partie multiplicative $S$
est entièrement constituée d'éléments non diviseurs de zéro, alors $R \to S^{-1}R$
est injectif,
\item si $\varphi : R_1 \to R_2$ est un homomorphisme d'anneaux et si
$S$ est une partie multiplicative de $R_1$, alors $\varphi(S)$ est
une partie multiplicative de $R_2$,
\item
\label{item-products-multiplicative-subsets}
si $S$, $S'$ sont des parties multiplicatives de $R$,
et si $SS'$ désigne l'ensemble des produits $SS' =
\{r \in R \mid \exists s\in S, \exists s' \in S', r = ss'\}$,
alors $SS'$ est une partie multiplicative de $R$,
\item
\label{item-localization-localization}
si $S$, $S'$ sont des parties multiplicatives de $R$,
et si $\overline{S}$ désigne l'image de $S$ dans $(S')^{-1}R$,
alors $(SS')^{-1}R = \overline{S}^{-1}((S')^{-1}R)$,
\item la {\it localisation} $S^{-1}M$ du $R$-module $M$,
\label{item-localization-module}
\item
\label{item-localization-exact}
le foncteur $M \mapsto S^{-1}M$ préserve les applications injectives,
les applications surjectives et l'exactitude,
\item
\label{item-localization-localization-module}
si $S$, $S'$ sont des parties multiplicatives de $R$,
et si $M$ est un $R$-module, alors
$(SS')^{-1}M = S^{-1}((S')^{-1}M)$,
\item
\label{item-localize-ideal}
si $R$ est un anneau, si $I$ est un idéal de $R$ et si $S$ est une partie multiplicative
de $R$, alors $S^{-1}I$ est un idéal de $S^{-1}R$, et nous avons
$S^{-1}R/S^{-1}I = \overline{S}^{-1}(R/I)$, où $\overline{S}$
est l'image de $S$ dans $R/I$,
\item
\label{item-ideal-in-localization}
si $R$ est un anneau et si $S$ est une partie multiplicative
de $R$, alors tout idéal $I'$ de $S^{-1}R$ est
de la forme $S^{-1}I$, où l'on peut prendre pour $I$
l'image réciproque de $I'$ dans $R$,
\item
\label{item-submodule-in-localization}
si $R$ est un anneau, si $M$ est un $R$-module et si $S$ est une partie multiplicative
de $R$, alors tout sous-module $N'$ de $S^{-1}M$ est de la forme
$S^{-1}N$ pour un certain sous-module $N \subset M$, où
l'on peut prendre pour $N$ l'image réciproque de $N'$ dans $M$,
\item si $S = \{1, f, f^2, \ldots\}$, alors $R_f = S^{-1}R$ et $M_f = S^{-1}M$,
\label{item-localize-f}
\item
\label{item-localize-p}
si $S = R \setminus \mathfrak p = \{x\in R \mid x\not\in \mathfrak p\}$
pour un certain idéal premier $\mathfrak p$,
alors on note usuellement $R_{\mathfrak p} = S^{-1}R$
et $M_{\mathfrak p} = S^{-1}M$,
```

</details>

### Passage 10 — item-local-ring

Source, lignes 264-278 ; français, lignes 265-279.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L264) · identifiant `FR-ALGEBRA-B1-CHOICE-0010`.

Local signifie exactement un idéal maximal ; semi-local en signifie un nombre fini. Le corps résiduel de l'idéal premier est le corps des fractions de R/p et non simplement R/p. Debarre p.83 atteste corps résiduel dans ce même contexte. Aucun remplacement de premier par maximal n'est effectué.

Règles appliquées : FR-ALGEBRA-B1-RULE-ideaux, FR-ALGEBRA-B1-RULE-localisation, FR-ALGEBRA-B1-RULE-anneaux.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\item a {\it local ring} is a ring with exactly one maximal ideal,
\label{item-local-ring}
\item a {\it semi-local ring} is a ring with finitely many maximal ideals,
\label{item-semi-local-ring}
\item
\label{item-localize-p-local-ring}
if $\mathfrak p$ is a prime in $R$, then $R_{\mathfrak p}$ is
a local ring with maximal ideal $\mathfrak p R_{\mathfrak p}$,
\item
\label{item-residue-field}
the {\it residue field}, denoted $\kappa(\mathfrak p)$,
of the prime $\mathfrak p$ in the ring $R$ is the
field of fractions of the domain $R/\mathfrak p$;
it is equal to $R_\mathfrak p/\mathfrak pR_\mathfrak p
= (R \setminus \mathfrak p)^{-1}R/\mathfrak p$,
```

Texte français :
```tex
\item un {\it anneau local} est un anneau qui possède exactement un idéal maximal,
\label{item-local-ring}
\item un {\it anneau semi-local} est un anneau qui possède un nombre fini d'idéaux maximaux,
\label{item-semi-local-ring}
\item
\label{item-localize-p-local-ring}
si $\mathfrak p$ est un idéal premier de $R$, alors $R_{\mathfrak p}$ est
un anneau local d'idéal maximal $\mathfrak p R_{\mathfrak p}$,
\item
\label{item-residue-field}
le {\it corps résiduel}, noté $\kappa(\mathfrak p)$,
de l'idéal premier $\mathfrak p$ de l'anneau $R$ est le
corps des fractions de l'anneau intègre $R/\mathfrak p$ ;
il est égal à $R_\mathfrak p/\mathfrak pR_\mathfrak p
= (R \setminus \mathfrak p)^{-1}R/\mathfrak p$,
```

</details>

### Passage 11 — item-tensor-product

Source, lignes 279-294 ; français, lignes 280-295.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L279) · identifiant `FR-ALGEBRA-B1-CHOICE-0011`.

Produit tensoriel garde ses deux modules et son anneau de base. Dans Cauchy-Binet, A a m lignes et n colonnes, B n lignes et m colonnes ; S choisit les colonnes de A et les lignes de B, avec cardinal m. Ni ces rôles ni l'ordre des facteurs ne sont inversés ; aucune preuve n'est ajoutée.

Règles appliquées : traduction courante et contrôle direct du contenu.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\item given $R$ and $M_1$, $M_2$ the {\it tensor product} $M_1 \otimes_R M_2$,
\label{item-tensor-product}
\item
\label{item-cauchy-binet}
given matrices $A$ and $B$ in a ring $R$ of sizes $m \times n$ and
$n \times m$ we have $\det(AB) = \sum \det(A_S)\det({}_SB)$ in $R$ where
the sum is over subsets $S \subset \{1, \ldots, n\}$ of size $m$
and $A_S$ is the $m \times m$ submatrix of $A$ with columns
corresponding to $S$ and ${}_SB$ is the $m \times m$ submatrix of $B$
with rows corresponding to $S$,
\item etc.
\end{enumerate}
```

Texte français :
```tex
\item étant donnés $R$ et $M_1$, $M_2$, le {\it produit tensoriel} $M_1 \otimes_R M_2$,
\label{item-tensor-product}
\item
\label{item-cauchy-binet}
étant données des matrices $A$ et $B$ dans un anneau $R$, de tailles $m \times n$ et
$n \times m$, nous avons $\det(AB) = \sum \det(A_S)\det({}_SB)$ dans $R$, où
la somme porte sur les sous-ensembles $S \subset \{1, \ldots, n\}$ de cardinal $m$,
et $A_S$ est la sous-matrice $m \times m$ de $A$ formée des colonnes
correspondant à $S$, tandis que ${}_SB$ est la sous-matrice $m \times m$ de $B$
formée des lignes correspondant à $S$,
\item etc.
\end{enumerate}
```

</details>

### Passage 12 — section-snake

Source, lignes 295-342 ; français, lignes 296-337.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L295) · identifiant `FR-ALGEBRA-B1-CHOICE-0012`.

Lemme du serpent, noyau, conoyau et lignes exactes sont attestés par Emprin, exercice 2 p.1. Les zéros du diagramme et les conditions séparées d'injectivité et de surjectivité sont conservés. La construction z, puis y, puis u et sa classe dans le conoyau suit la source. La preuve d'exactitude reste expressément omise. Seul le libellé de citation Lemma devient Lemme ; Cartan-Eilenberg III.3.3 n'est pas prétendu nouvellement consulté.

Règles appliquées : FR-ALGEBRA-B1-RULE-exactitude.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\section{Snake lemma}
\label{section-snake}

\noindent
The snake lemma and its variants are discussed in the setting of
abelian categories in
Homology, Section \ref{homology-section-abelian-categories}.

\begin{lemma}
\label{lemma-snake}
\begin{reference}
\cite[III, Lemma 3.3]{Cartan-Eilenberg}
\end{reference}
Given a commutative diagram
$$
\xymatrix{
& X \ar[r] \ar[d]^\alpha &
Y \ar[r] \ar[d]^\beta &
Z \ar[r] \ar[d]^\gamma &
0 \\
0 \ar[r] & U \ar[r] & V \ar[r] & W
}
$$
of abelian groups with exact rows, there is a canonical exact sequence
$$
\Ker(\alpha) \to \Ker(\beta) \to \Ker(\gamma)
\to
\Coker(\alpha) \to \Coker(\beta) \to \Coker(\gamma)
$$
Moreover: if $X \to Y$ is injective, then the first map is
injective; if $V \to W$ is surjective, then the last
map is surjective.
\end{lemma}

\begin{proof}
The map $\partial : \Ker(\gamma) \to \Coker(\alpha)$ is defined
as follows. Take $z \in \Ker(\gamma)$. Choose $y \in Y$ mapping to $z$.
Then $\beta(y) \in V$ maps to zero in $W$. Hence $\beta(y)$ is the image of
some $u \in U$. Set $\partial z = \overline{u}$, the class of $u$ in the
cokernel of $\alpha$. Proof of exactness is omitted.
\end{proof}
```

Texte français :
```tex
\section{Lemme du serpent}
\label{section-snake}

\noindent
Le lemme du serpent et ses variantes sont étudiés dans le cadre des
catégories abéliennes dans
Homologie, section \ref{homology-section-abelian-categories}.

\begin{lemma}
\label{lemma-snake}
\begin{reference}
\cite[III, Lemme 3.3]{Cartan-Eilenberg}
\end{reference}
Étant donné un diagramme commutatif
$$
\xymatrix{
& X \ar[r] \ar[d]^\alpha &
Y \ar[r] \ar[d]^\beta &
Z \ar[r] \ar[d]^\gamma &
0 \\
0 \ar[r] & U \ar[r] & V \ar[r] & W
}
$$
de groupes abéliens dont les lignes sont exactes, il existe une suite exacte canonique
$$
\Ker(\alpha) \to \Ker(\beta) \to \Ker(\gamma)
\to
\Coker(\alpha) \to \Coker(\beta) \to \Coker(\gamma)
$$
De plus, si $X \to Y$ est injectif, la première application est
injective ; si $V \to W$ est surjectif, la dernière
application est surjective.
\end{lemma}

\begin{proof}
L'application $\partial : \Ker(\gamma) \to \Coker(\alpha)$ est définie
comme suit. Soit $z \in \Ker(\gamma)$. Choisissons $y \in Y$ d'image $z$.
Alors $\beta(y) \in V$ s'envoie sur zéro dans $W$. Ainsi, $\beta(y)$ est l'image d'un
élément $u \in U$. Posons $\partial z = \overline{u}$, la classe de $u$ dans le
conoyau de $\alpha$. La démonstration de l'exactitude est omise.
\end{proof}
```

</details>

### Passage 13 — section-module-finite-type

Source, lignes 343-348 ; français, lignes 338-343.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L343) · identifiant `FR-ALGEBRA-B1-CHOICE-0013`.

Le titre distingue le nombre fini de générateurs et celui de relations ; il ne confond pas ces propriétés. L'annonce de quelques notations et lemmes reste sans contenu supplémentaire.

Règles appliquées : FR-ALGEBRA-B1-RULE-generation, FR-ALGEBRA-B1-RULE-presentation.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\section{Finite modules and finitely presented modules}
\label{section-module-finite-type}

\noindent
Just some basic notation and lemmas.
```

Texte français :
```tex
\section{Modules de type fini et modules de présentation finie}
\label{section-module-finite-type}

\noindent
Voici simplement quelques notations et lemmes élémentaires.
```

</details>

### Passage 14 — definition-module-finite-type

Source, lignes 349-373 ; français, lignes 344-368.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L349) · identifiant `FR-ALGEBRA-B1-CHOICE-0014`.

Les générateurs sont en nombre fini et la suite libre avec m,n finis reste exacte. Le module des relations est attesté par Lombardi 3.2-3.3. Les deux synonymes anglais finitely presented et of finite presentation aboutissent ici deux fois à de présentation finie : répétition stylistique conservée et signalée, non différence mathématique inventée. Aucune attestation nouvelle de finiment présenté n'est revendiquée.

Point à rendre visible pour la revue : Deux synonymes anglais ont la même traduction répétée. Une amélioration purement stylistique reste possible ; elle ne bloque ni la fidélité ni le travail suivant.

Règles appliquées : FR-ALGEBRA-B1-RULE-generation, FR-ALGEBRA-B1-RULE-presentation, FR-ALGEBRA-B1-RULE-exactitude.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\begin{definition}
\label{definition-module-finite-type}
Let $R$ be a ring. Let $M$ be an $R$-module.
\begin{enumerate}
\item We say $M$ is a {\it finite $R$-module}, or a {\it finitely generated
$R$-module} if there exist $n \in \mathbf{N}$ and $x_1, \ldots, x_n \in M$
such that every element of $M$ is an $R$-linear combination of the $x_i$.
Equivalently, this means there exists a surjection
$R^{\oplus n} \to M$ for some $n \in \mathbf{N}$.
\item We say $M$ is a {\it finitely presented $R$-module} or an
{\it $R$-module of finite presentation} if there exist integers
$n, m \in \mathbf{N}$ and an exact sequence
$$
R^{\oplus m} \longrightarrow R^{\oplus n} \longrightarrow M \longrightarrow 0
$$
\end{enumerate}
\end{definition}

\noindent
Informally, $M$ is a finitely presented $R$-module if and only if
it is finitely generated and the module of relations among these
generators is finitely generated as well.
A choice of an exact sequence as in the definition is called a
{\it presentation} of $M$.
```

Texte français :
```tex
\begin{definition}
\label{definition-module-finite-type}
Soit $R$ un anneau. Soit $M$ un $R$-module.
\begin{enumerate}
\item Nous disons que $M$ est un {\it $R$-module de type fini}, ou un {\it
$R$-module engendré par un nombre fini d'éléments}, s'il existe $n \in \mathbf{N}$ et $x_1, \ldots, x_n \in M$
tels que tout élément de $M$ soit une combinaison $R$-linéaire des $x_i$.
De manière équivalente, cela signifie qu'il existe une surjection
$R^{\oplus n} \to M$ pour un certain $n \in \mathbf{N}$.
\item Nous disons que $M$ est un {\it $R$-module de présentation finie} ou un
{\it $R$-module de présentation finie} s'il existe des entiers
$n, m \in \mathbf{N}$ et une suite exacte
$$
R^{\oplus m} \longrightarrow R^{\oplus n} \longrightarrow M \longrightarrow 0
$$
\end{enumerate}
\end{definition}

\noindent
De manière informelle, $M$ est un $R$-module de présentation finie si et seulement s'il
est de type fini et si le module des relations entre ces
générateurs est lui aussi de type fini.
Le choix d'une suite exacte comme dans la définition s'appelle une
{\it présentation} de $M$.
```

</details>

### Passage 15 — lemma-lift-map

Source, lignes 374-389 ; français, lignes 369-384.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L374) · identifiant `FR-ALGEBRA-B1-CHOICE-0015`.

L'hypothèse est l'inclusion des images, non la surjectivité de beta. Chaque vecteur de base reçoit un relèvement dans N ; la somme linéaire définit gamma et la composition beta après gamma est maintenue. Application et homomorphisme nomment ici le même morphisme de modules, pas une application ensembliste arbitraire.

Règles appliquées : traduction courante et contrôle direct du contenu.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\begin{lemma}
\label{lemma-lift-map}
Let $R$ be a ring. Let $\alpha : R^{\oplus n} \to M$ and $\beta : N \to M$ be
module maps. If $\Im(\alpha) \subset \Im(\beta)$, then there
exists an $R$-module map $\gamma : R^{\oplus n} \to N$ such that
$\alpha = \beta \circ \gamma$.
\end{lemma}

\begin{proof}
Let $e_i = (0, \ldots, 0, 1, 0, \ldots, 0)$ be the $i$th basis vector
of $R^{\oplus n}$. Let $x_i \in N$ be an element with
$\alpha(e_i) = \beta(x_i)$ which exists by assumption. Set
$\gamma(a_1, \ldots, a_n) = \sum a_i x_i$. By construction
$\alpha = \beta \circ \gamma$.
\end{proof}
```

Texte français :
```tex
\begin{lemma}
\label{lemma-lift-map}
Soit $R$ un anneau. Soient $\alpha : R^{\oplus n} \to M$ et $\beta : N \to M$ des
homomorphismes de modules. Si $\Im(\alpha) \subset \Im(\beta)$, il existe alors
un homomorphisme de $R$-modules $\gamma : R^{\oplus n} \to N$ tel que
$\alpha = \beta \circ \gamma$.
\end{lemma}

\begin{proof}
Soit $e_i = (0, \ldots, 0, 1, 0, \ldots, 0)$ le $i$-ème vecteur de base
de $R^{\oplus n}$. Soit $x_i \in N$ un élément tel que
$\alpha(e_i) = \beta(x_i)$ ; il existe par hypothèse. Posons
$\gamma(a_1, \ldots, a_n) = \sum a_i x_i$. Par construction,
$\alpha = \beta \circ \gamma$.
\end{proof}
```

</details>

### Passage 16 — lemma-extension

Source, lignes 390-476 ; français, lignes 385-471.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L390) · identifiant `FR-ALGEBRA-B1-CHOICE-0016`.

Les cinq assertions gardent chacune leurs hypothèses de finitude ou présentation finie. L'ordre des preuves 1,3,5,4,2, les deux diagrammes, la flèche pointillée, l'isomorphisme de conoyaux et les noyaux sont conservés. La présentation avec k+m relations reste exacte. Le dernier appel à (5) puis (4) reste aussi condensé que l'anglais : aucune hypothèse noethérienne ni preuve supplémentaire n'est introduite.

Point à rendre visible pour la revue : Le dernier appel à (4) est condensé. Une éventuelle explicitation appartiendrait à un commentaire séparé, pas à la traduction de cette preuve.

Règles appliquées : FR-ALGEBRA-B1-RULE-generation, FR-ALGEBRA-B1-RULE-presentation, FR-ALGEBRA-B1-RULE-exactitude.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\begin{lemma}
\label{lemma-extension}
Let $R$ be a ring.
Let
$$
0 \to M_1 \to M_2 \to M_3 \to 0
$$
be a short exact sequence of $R$-modules.
\begin{enumerate}
\item If $M_1$ and $M_3$ are finite $R$-modules, then $M_2$ is a finite
$R$-module.
\item If $M_1$ and $M_3$ are finitely presented $R$-modules, then $M_2$
is a finitely presented $R$-module.
\item If $M_2$ is a finite $R$-module, then $M_3$ is a finite $R$-module.
\item If $M_2$ is a finitely presented $R$-module and $M_1$ is a
finite $R$-module, then $M_3$ is a finitely presented $R$-module.
\item If $M_3$ is a finitely presented $R$-module and $M_2$ is a finite
$R$-module, then $M_1$ is a finite $R$-module.
\end{enumerate}
\end{lemma}

\begin{proof}
Proof of (1). If $x_1, \ldots, x_n$ are generators of $M_1$ and
$y_1, \ldots, y_m \in M_2$ are elements whose images in $M_3$ are
generators of $M_3$, then $x_1, \ldots, x_n, y_1, \ldots, y_m$
generate $M_2$.

\medskip\noindent
Part (3) is immediate from the definition.

\medskip\noindent
Proof of (5). Assume $M_3$ is finitely presented and $M_2$ finite.
Choose a presentation
$$
R^{\oplus m} \to R^{\oplus n} \to M_3 \to 0
$$
By Lemma \ref{lemma-lift-map} there exists a map
$R^{\oplus n} \to M_2$ such that
the solid diagram
$$
\xymatrix{
& R^{\oplus m} \ar[r] \ar@{..>}[d] & R^{\oplus n} \ar[r] \ar[d] &
M_3 \ar[r] \ar[d]^{\text{id}} & 0 \\
0 \ar[r] & M_1 \ar[r] & M_2 \ar[r] & M_3 \ar[r] & 0
}
$$
commutes. This produces the dotted arrow. By the snake lemma
(Lemma \ref{lemma-snake}) we see that we get an isomorphism
$$
\Coker(R^{\oplus m} \to M_1)
\cong
\Coker(R^{\oplus n} \to M_2)
$$
In particular we conclude that $\Coker(R^{\oplus m} \to M_1)$
is a finite $R$-module. Since $\Im(R^{\oplus m} \to M_1)$
is finite by (3), we see that $M_1$ is finite by part (1).

\medskip\noindent
Proof of (4). Assume $M_2$ is finitely presented and $M_1$ is finite.
Choose a presentation $R^{\oplus m} \to R^{\oplus n} \to M_2 \to 0$.
Choose a surjection $R^{\oplus k} \to M_1$. By Lemma \ref{lemma-lift-map}
there exists a factorization $R^{\oplus k} \to R^{\oplus n} \to M_2$
of the composition $R^{\oplus k} \to M_1 \to M_2$. Then
$R^{\oplus k + m} \to R^{\oplus n} \to M_3 \to 0$
is a presentation.

\medskip\noindent
Proof of (2). Assume that $M_1$ and $M_3$ are finitely presented.
The argument in the proof of part (1) produces a commutative diagram
$$
\xymatrix{
0 \ar[r] & R^{\oplus n} \ar[d] \ar[r] & R^{\oplus n + m} \ar[d] \ar[r] &
R^{\oplus m} \ar[d] \ar[r] & 0 \\
0 \ar[r] & M_1 \ar[r] & M_2 \ar[r] & M_3 \ar[r] & 0
}
$$
with surjective vertical arrows. By the snake lemma we obtain a short
exact sequence
$$
0 \to \Ker(R^{\oplus n} \to M_1) \to
\Ker(R^{\oplus n + m} \to M_2) \to
\Ker(R^{\oplus m} \to M_3) \to 0
$$
By part (5) we see that the outer two modules are finite. Hence the
middle one is finite too. By (4) we see that $M_2$ is of finite presentation.
\end{proof}
```

Texte français :
```tex
\begin{lemma}
\label{lemma-extension}
Soit $R$ un anneau.
Soit
$$
0 \to M_1 \to M_2 \to M_3 \to 0
$$
une suite exacte courte de $R$-modules.
\begin{enumerate}
\item Si $M_1$ et $M_3$ sont des $R$-modules de type fini, alors $M_2$ est un
$R$-module de type fini.
\item Si $M_1$ et $M_3$ sont des $R$-modules de présentation finie, alors $M_2$
est un $R$-module de présentation finie.
\item Si $M_2$ est un $R$-module de type fini, alors $M_3$ est un $R$-module de type fini.
\item Si $M_2$ est un $R$-module de présentation finie et si $M_1$ est un
$R$-module de type fini, alors $M_3$ est un $R$-module de présentation finie.
\item Si $M_3$ est un $R$-module de présentation finie et si $M_2$ est un
$R$-module de type fini, alors $M_1$ est un $R$-module de type fini.
\end{enumerate}
\end{lemma}

\begin{proof}
Démonstration de (1). Si $x_1, \ldots, x_n$ sont des générateurs de $M_1$ et si
$y_1, \ldots, y_m \in M_2$ sont des éléments dont les images dans $M_3$ sont des
générateurs de $M_3$, alors $x_1, \ldots, x_n, y_1, \ldots, y_m$
engendrent $M_2$.

\medskip\noindent
L'assertion (3) découle immédiatement de la définition.

\medskip\noindent
Démonstration de (5). Supposons $M_3$ de présentation finie et $M_2$ de type fini.
Choisissons une présentation
$$
R^{\oplus m} \to R^{\oplus n} \to M_3 \to 0
$$
D'après le Lemme \ref{lemma-lift-map}, il existe une application
$R^{\oplus n} \to M_2$ telle que
le diagramme en traits pleins
$$
\xymatrix{
& R^{\oplus m} \ar[r] \ar@{..>}[d] & R^{\oplus n} \ar[r] \ar[d] &
M_3 \ar[r] \ar[d]^{\text{id}} & 0 \\
0 \ar[r] & M_1 \ar[r] & M_2 \ar[r] & M_3 \ar[r] & 0
}
$$
soit commutatif. On obtient ainsi la flèche en pointillé. Par le lemme du serpent
(Lemme \ref{lemma-snake}), on voit que l'on obtient un isomorphisme
$$
\Coker(R^{\oplus m} \to M_1)
\cong
\Coker(R^{\oplus n} \to M_2)
$$
En particulier, nous en déduisons que $\Coker(R^{\oplus m} \to M_1)$
est un $R$-module de type fini. Puisque $\Im(R^{\oplus m} \to M_1)$
est de type fini d'après (3), on voit que $M_1$ est de type fini d'après l'assertion (1).

\medskip\noindent
Démonstration de (4). Supposons $M_2$ de présentation finie et $M_1$ de type fini.
Choisissons une présentation $R^{\oplus m} \to R^{\oplus n} \to M_2 \to 0$.
Choisissons une surjection $R^{\oplus k} \to M_1$. D'après le Lemme \ref{lemma-lift-map},
il existe une factorisation $R^{\oplus k} \to R^{\oplus n} \to M_2$
de la composée $R^{\oplus k} \to M_1 \to M_2$. Alors
$R^{\oplus k + m} \to R^{\oplus n} \to M_3 \to 0$
est une présentation.

\medskip\noindent
Démonstration de (2). Supposons $M_1$ et $M_3$ de présentation finie.
L'argument de la démonstration de l'assertion (1) fournit un diagramme commutatif
$$
\xymatrix{
0 \ar[r] & R^{\oplus n} \ar[d] \ar[r] & R^{\oplus n + m} \ar[d] \ar[r] &
R^{\oplus m} \ar[d] \ar[r] & 0 \\
0 \ar[r] & M_1 \ar[r] & M_2 \ar[r] & M_3 \ar[r] & 0
}
$$
dont les flèches verticales sont surjectives. Par le lemme du serpent, nous obtenons une suite
exacte courte
$$
0 \to \Ker(R^{\oplus n} \to M_1) \to
\Ker(R^{\oplus n + m} \to M_2) \to
\Ker(R^{\oplus m} \to M_3) \to 0
$$
D'après l'assertion (5), les deux modules extrêmes sont de type fini. Par conséquent, celui du
milieu l'est aussi. D'après (4), on voit que $M_2$ est de présentation finie.
\end{proof}
```

</details>

### Passage 17 — lemma-trivial-filter-finite-module

Source, lignes 477-499 ; français, lignes 472-494.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L477) · identifiant `FR-ALGEBRA-B1-CHOICE-0017`.

Le slogan et l'énoncé concernent des sous-modules de type fini et des quotients cycliques R/I, non des groupes cycliques finis. La récurrence est sur le nombre de générateurs ; M prime est Rx_1 et I_1 son annulateur. Le cas de base du module nul reste implicite comme dans la source : cette fidélité n'est pas une certification de complétude de la preuve.

Point à rendre visible pour la revue : Le cas nul de la récurrence n'est pas développé par la source. Il n'est pas ajouté clandestinement à cette traduction.

Règles appliquées : FR-ALGEBRA-B1-RULE-generation, FR-ALGEBRA-B1-RULE-libre-cyclique.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\begin{lemma}
\label{lemma-trivial-filter-finite-module}
\begin{slogan}
Finite modules have filtrations such that successive quotients are
cyclic modules.
\end{slogan}
Let $R$ be a ring, and let $M$ be a finite $R$-module.
There exists a filtration by finite $R$-submodules
$$
0 = M_0 \subset M_1 \subset \ldots \subset M_n = M
$$
such that each quotient $M_i/M_{i - 1}$ is isomorphic
to $R/I_i$ for some ideal $I_i$ of $R$.
\end{lemma}

\begin{proof}
By induction on the number of generators of $M$. Let
$x_1, \ldots, x_r \in M$ be generators.
Let $M' = Rx_1 \subset M$. Then $M/M'$ has $r - 1$ generators
and the induction hypothesis applies. And clearly $M' \cong R/I_1$
with $I_1 = \{f \in R \mid fx_1 = 0\}$.
\end{proof}
```

Texte français :
```tex
\begin{lemma}
\label{lemma-trivial-filter-finite-module}
\begin{slogan}
Les modules de type fini admettent des filtrations dont les quotients successifs sont des
modules cycliques.
\end{slogan}
Soit $R$ un anneau et soit $M$ un $R$-module de type fini.
Il existe une filtration par des $R$-sous-modules de type fini
$$
0 = M_0 \subset M_1 \subset \ldots \subset M_n = M
$$
telle que chaque quotient $M_i/M_{i - 1}$ soit isomorphe
à $R/I_i$ pour un certain idéal $I_i$ de $R$.
\end{lemma}

\begin{proof}
Nous raisonnons par récurrence sur le nombre de générateurs de $M$. Soient
$x_1, \ldots, x_r \in M$ des générateurs.
Posons $M' = Rx_1 \subset M$. Alors $M/M'$ possède $r - 1$ générateurs
et l'hypothèse de récurrence s'applique. De plus, il est clair que $M' \cong R/I_1$
avec $I_1 = \{f \in R \mid fx_1 = 0\}$.
\end{proof}
```

</details>

### Passage 18 — lemma-finite-over-subring

Source, lignes 500-513 ; français, lignes 495-509.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L500) · identifiant `FR-ALGEBRA-B1-CHOICE-0018`.

Malgré le nom technique de l'étiquette, R vers S n'est pas supposé injectif. Le texte indique justement l'image de R dans S. La propriété de génération est transportée dans un seul sens, sans réciproque non autorisée.

Règles appliquées : FR-ALGEBRA-B1-RULE-generation.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\begin{lemma}
\label{lemma-finite-over-subring}
Let $R \to S$ be a ring map.
Let $M$ be an $S$-module.
If $M$ is finite as an $R$-module, then $M$ is finite as an $S$-module.
\end{lemma}

\begin{proof}
In fact, any $R$-generating set of $M$ is also an $S$-generating set of
$M$, since the $R$-module structure is induced by the image of $R$ in $S$.
\end{proof}
```

Texte français :
```tex
\begin{lemma}
\label{lemma-finite-over-subring}
Soit $R \to S$ un morphisme d'anneaux.
Soit $M$ un $S$-module.
Si $M$ est de type fini comme $R$-module, alors $M$ est de type fini comme $S$-module.
\end{lemma}

\begin{proof}
En effet, tout système générateur sur $R$ de $M$ est aussi un système générateur sur $S$ de
$M$, puisque la structure de $R$-module est induite par l'image de $R$ dans $S$.
\end{proof}
```

</details>

### Passage 19 — section-finite-type

Source, lignes 514-538 ; français, lignes 510-534.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L514) · identifiant `FR-ALGEBRA-B1-CHOICE-0019`.

Type fini est défini par une surjection depuis une algèbre de polynômes, non depuis un module libre. Présentation finie exige un idéal de relations de type fini. Parfois appelé une présentation conserve la réserve de l'auteur au sujet d'une simple surjection ; le canon terminologique ne remplace pas cette convention.

Règles appliquées : FR-ALGEBRA-B1-RULE-generation, FR-ALGEBRA-B1-RULE-presentation.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\section{Ring maps of finite type and of finite presentation}
\label{section-finite-type}

\begin{definition}
\label{definition-finite-type}
Let $R \to S$ be a ring map.
\begin{enumerate}
\item We say $R \to S$ is of {\it finite type}, or that {\it $S$ is a finite
type $R$-algebra} if there exist an $n \in \mathbf{N}$ and an surjection
of $R$-algebras $R[x_1, \ldots, x_n] \to S$.
\item We say $R \to S$ is of {\it finite presentation} if there
exist integers $n, m \in \mathbf{N}$ and polynomials
$f_1, \ldots, f_m \in R[x_1, \ldots, x_n]$
and an isomorphism of $R$-algebras
$R[x_1, \ldots, x_n]/(f_1, \ldots, f_m) \cong S$.
\end{enumerate}
\end{definition}

\noindent
Informally, $R \to S$ is of finite presentation if and only if
$S$ is finitely generated as an $R$-algebra
and the ideal of relations among the generators is finitely generated.
A choice of a surjection $R[x_1, \ldots, x_n] \to S$ as in the definition
is sometimes called a {\it presentation} of $S$.
```

Texte français :
```tex
\section{Morphismes d'anneaux de type fini et de présentation finie}
\label{section-finite-type}

\begin{definition}
\label{definition-finite-type}
Soit $R \to S$ un morphisme d'anneaux.
\begin{enumerate}
\item Nous disons que $R \to S$ est de {\it type fini}, ou que {\it $S$ est une
$R$-algèbre de type fini}, s'il existe un $n \in \mathbf{N}$ et une surjection
de $R$-algèbres $R[x_1, \ldots, x_n] \to S$.
\item Nous disons que $R \to S$ est de {\it présentation finie} s'il
existe des entiers $n, m \in \mathbf{N}$, des polynômes
$f_1, \ldots, f_m \in R[x_1, \ldots, x_n]$
et un isomorphisme de $R$-algèbres
$R[x_1, \ldots, x_n]/(f_1, \ldots, f_m) \cong S$.
\end{enumerate}
\end{definition}

\noindent
De manière informelle, $R \to S$ est de présentation finie si et seulement si
$S$ est de type fini comme $R$-algèbre
et si l'idéal des relations entre les générateurs est de type fini.
Le choix d'une surjection $R[x_1, \ldots, x_n] \to S$ comme dans la définition
est parfois appelé une {\it présentation} de $S$.
```

</details>

### Passage 20 — lemma-compose-finite-type

Source, lignes 539-564 ; français, lignes 535-560.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L539) · identifiant `FR-ALGEBRA-B1-CHOICE-0020`.

Les quatre propriétés restent distinctes. La quatrième exige R vers S de présentation finie et R vers S prime de type fini. Seule cette assertion est prouvée. L'idéal I n'est pas déclaré de type fini ; les relations h_i moins y_i barre sont inchangées. Supposons que la classe s'envoie sur désigne le choix du représentant de l'image, sans ajouter d'hypothèse à l'énoncé.

Règles appliquées : FR-ALGEBRA-B1-RULE-generation, FR-ALGEBRA-B1-RULE-presentation.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\begin{lemma}
\label{lemma-compose-finite-type}
The notions finite type and finite presentation have the following
permanence properties.
\begin{enumerate}
\item A composition of ring maps of finite type is of finite type.
\item A composition of ring maps of finite presentation is of finite
presentation.
\item Given $R \to S' \to S$ with $R \to S$ of finite type,
then $S' \to S$ is of finite type.
\item Given $R \to S' \to S$, with $R \to S$ of finite presentation,
and $R \to S'$ of finite type, then $S' \to S$ is of finite presentation.
\end{enumerate}
\end{lemma}

\begin{proof}
We only prove the last assertion.
Write $S = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$
and $S' = R[y_1, \ldots, y_a]/I$. Say that the class
$\bar y_i$ of $y_i$ maps
to $h_i \bmod (f_1, \ldots, f_m)$ in $S$.
Then it is clear that
$S = S'[x_1, \ldots, x_n]/(f_1, \ldots, f_m,
h_1 - \bar y_1, \ldots, h_a - \bar y_a)$.
\end{proof}
```

Texte français :
```tex
\begin{lemma}
\label{lemma-compose-finite-type}
Les notions de type fini et de présentation finie possèdent les propriétés
de permanence suivantes.
\begin{enumerate}
\item Une composée de morphismes d'anneaux de type fini est de type fini.
\item Une composée de morphismes d'anneaux de présentation finie est de présentation
finie.
\item Étant donné $R \to S' \to S$ avec $R \to S$ de type fini,
le morphisme $S' \to S$ est alors de type fini.
\item Étant donné $R \to S' \to S$, avec $R \to S$ de présentation finie
et $R \to S'$ de type fini, le morphisme $S' \to S$ est alors de présentation finie.
\end{enumerate}
\end{lemma}

\begin{proof}
Nous ne démontrons que la dernière assertion.
Écrivons $S = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$
et $S' = R[y_1, \ldots, y_a]/I$. Supposons que la classe
$\bar y_i$ de $y_i$ s'envoie
sur $h_i \bmod (f_1, \ldots, f_m)$ dans $S$.
Il est alors clair que
$S = S'[x_1, \ldots, x_n]/(f_1, \ldots, f_m,
h_1 - \bar y_1, \ldots, h_a - \bar y_a)$.
\end{proof}
```

</details>

### Passage 21 — lemma-finite-presentation-independent

Source, lignes 565-582 ; français, lignes 561-578.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L565) · identifiant `FR-ALGEBRA-B1-CHOICE-0021`.

La conclusion porte sur toute surjection alpha, pas seulement sur une présentation choisie. Les relèvements g_i, les représentants h_j, le domaine et le but de psi sont conservés. Le noyau est l'image de l'idéal par psi, non son image réciproque. Ce qui conclut traduit we win sans supprimer d'argument.

Règles appliquées : FR-ALGEBRA-B1-RULE-generation, FR-ALGEBRA-B1-RULE-presentation, FR-ALGEBRA-B1-RULE-exactitude.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\begin{lemma}
\label{lemma-finite-presentation-independent}
Let $R \to S$ be a ring map of finite presentation.
For any surjection $\alpha : R[x_1, \ldots, x_n] \to S$ the
kernel of $\alpha$ is a finitely generated ideal in $R[x_1, \ldots, x_n]$.
\end{lemma}

\begin{proof}
Write $S = R[y_1, \ldots, y_m]/(f_1, \ldots, f_k)$.
Choose $g_i \in R[y_1, \ldots, y_m]$ which are lifts
of $\alpha(x_i)$. Then we see that $S = R[x_i, y_j]/(f_l, x_i - g_i)$.
Choose $h_j \in R[x_1, \ldots, x_n]$ such that $\alpha(h_j)$
corresponds to $y_j \bmod (f_1, \ldots, f_k)$. Consider
the map $\psi : R[x_i, y_j] \to R[x_i]$, $x_i \mapsto x_i$,
$y_j \mapsto h_j$. Then the kernel of $\alpha$
is the image of $(f_l, x_i - g_i)$ under $\psi$ and we win.
\end{proof}
```

Texte français :
```tex
\begin{lemma}
\label{lemma-finite-presentation-independent}
Soit $R \to S$ un morphisme d'anneaux de présentation finie.
Pour toute surjection $\alpha : R[x_1, \ldots, x_n] \to S$, le
noyau de $\alpha$ est un idéal de type fini de $R[x_1, \ldots, x_n]$.
\end{lemma}

\begin{proof}
Écrivons $S = R[y_1, \ldots, y_m]/(f_1, \ldots, f_k)$.
Choisissons des $g_i \in R[y_1, \ldots, y_m]$ qui relèvent
les $\alpha(x_i)$. On voit alors que $S = R[x_i, y_j]/(f_l, x_i - g_i)$.
Choisissons $h_j \in R[x_1, \ldots, x_n]$ tel que $\alpha(h_j)$
corresponde à $y_j \bmod (f_1, \ldots, f_k)$. Considérons
l'application $\psi : R[x_i, y_j] \to R[x_i]$, $x_i \mapsto x_i$,
$y_j \mapsto h_j$. Le noyau de $\alpha$
est alors l'image de $(f_l, x_i - g_i)$ par $\psi$, ce qui conclut.
\end{proof}
```

</details>

### Passage 22 — lemma-finitely-presented-over-subring

Source, lignes 583-628 ; français, lignes 579-623.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L583) · identifiant `FR-ALGEBRA-B1-CHOICE-0022`.

R vers S reste de type fini, non nécessairement fini ni injectif. Le module N a nm+t relations ; la surjection phi, la réduction du degré jusqu'aux coefficients dans R puis l'utilisation des relations a_ij sont conservées. L'idéal J n'acquiert aucune hypothèse de génération finie.

Règles appliquées : FR-ALGEBRA-B1-RULE-generation, FR-ALGEBRA-B1-RULE-presentation, FR-ALGEBRA-B1-RULE-exactitude.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\begin{lemma}
\label{lemma-finitely-presented-over-subring}
Let $R \to S$ be a ring map.
Let $M$ be an $S$-module.
Assume $R \to S$ is of finite type and
$M$ is finitely presented as an $R$-module.
Then $M$ is finitely presented as an $S$-module.
\end{lemma}

\begin{proof}
This is similar to the proof of part (4) of
Lemma \ref{lemma-compose-finite-type}.
We may assume $S = R[x_1, \ldots, x_n]/J$.
Choose $y_1, \ldots, y_m \in M$ which generate $M$ as an $R$-module
and choose relations $\sum a_{ij} y_j = 0$, $i = 1, \ldots, t$ which
generate the kernel of $R^{\oplus m} \to M$. For any
$i = 1, \ldots, n$ and $j = 1, \ldots, m$ write
$$
x_i y_j = \sum a_{ijk} y_k
$$
for some $a_{ijk} \in R$. Consider the $S$-module $N$ generated by
$y_1, \ldots, y_m$ subject to the relations
$\sum a_{ij} y_j = 0$, $i = 1, \ldots, t$ and
$x_i y_j = \sum a_{ijk} y_k$, $i = 1, \ldots, n$ and $j = 1, \ldots, m$.
Then $N$ has a presentation
$$
S^{\oplus nm + t} \longrightarrow S^{\oplus m} \longrightarrow N
\longrightarrow 0
$$
By construction there is a surjective map $\varphi : N \to M$.
To finish the proof we show $\varphi$ is injective.
Suppose $z = \sum b_j y_j \in N$ for some $b_j \in S$.
We may think of $b_j$ as a polynomial in $x_1, \ldots, x_n$
with coefficients in $R$.
By applying the relations of the form $x_i y_j = \sum a_{ijk} y_k$
we can inductively lower the degree of the polynomials.
Hence we see that $z = \sum c_j y_j$ for some $c_j \in R$.
Hence if $\varphi(z) = 0$ then the vector $(c_1, \ldots, c_m)$
is an $R$-linear combination of the vectors $(a_{i1}, \ldots, a_{im})$
and we conclude that $z = 0$ as desired.
\end{proof}
```

Texte français :
```tex
\begin{lemma}
\label{lemma-finitely-presented-over-subring}
Soit $R \to S$ un morphisme d'anneaux.
Soit $M$ un $S$-module.
Supposons $R \to S$ de type fini et
$M$ de présentation finie comme $R$-module.
Alors $M$ est de présentation finie comme $S$-module.
\end{lemma}

\begin{proof}
La démonstration est semblable à celle de l'assertion (4) du
Lemme \ref{lemma-compose-finite-type}.
Nous pouvons supposer $S = R[x_1, \ldots, x_n]/J$.
Choisissons $y_1, \ldots, y_m \in M$ qui engendrent $M$ comme $R$-module
et des relations $\sum a_{ij} y_j = 0$, $i = 1, \ldots, t$, qui
engendrent le noyau de $R^{\oplus m} \to M$. Pour tous
$i = 1, \ldots, n$ et $j = 1, \ldots, m$, écrivons
$$
x_i y_j = \sum a_{ijk} y_k
$$
pour certains $a_{ijk} \in R$. Considérons le $S$-module $N$ engendré par
$y_1, \ldots, y_m$ et soumis aux relations
$\sum a_{ij} y_j = 0$, $i = 1, \ldots, t$, ainsi que
$x_i y_j = \sum a_{ijk} y_k$, $i = 1, \ldots, n$ et $j = 1, \ldots, m$.
Alors $N$ possède une présentation
$$
S^{\oplus nm + t} \longrightarrow S^{\oplus m} \longrightarrow N
\longrightarrow 0
$$
Par construction, il existe une application surjective $\varphi : N \to M$.
Pour achever la démonstration, montrons que $\varphi$ est injective.
Supposons $z = \sum b_j y_j \in N$ pour certains $b_j \in S$.
Nous pouvons considérer les $b_j$ comme des polynômes en $x_1, \ldots, x_n$
à coefficients dans $R$.
En appliquant les relations de la forme $x_i y_j = \sum a_{ijk} y_k$,
nous pouvons abaisser par récurrence le degré des polynômes.
Nous voyons donc que $z = \sum c_j y_j$ pour certains $c_j \in R$.
Par conséquent, si $\varphi(z) = 0$, le vecteur $(c_1, \ldots, c_m)$
est une combinaison $R$-linéaire des vecteurs $(a_{i1}, \ldots, a_{im})$,
et nous concluons que $z = 0$, comme souhaité.
\end{proof}
```

</details>

### Passage 23 — section-finite

Source, lignes 629-640 ; français, lignes 624-635.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L629) · identifiant `FR-ALGEBRA-B1-CHOICE-0023`.

Le titre devient Morphismes finis d'anneaux pour rattacher fini au morphisme, et non à la cardinalité des anneaux. La définition dit que S est de type fini comme R-module, suivant le sens module attesté chez Debarre. Elle ne dit pas simplement algèbre de type fini.

Règles appliquées : FR-ALGEBRA-B1-RULE-generation, FR-ALGEBRA-B1-RULE-morphisme-fini.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\section{Finite ring maps}
\label{section-finite}

\noindent
Here is the definition.

\begin{definition}
\label{definition-finite-ring-map}
Let $\varphi : R \to S$ be a ring map. We say $\varphi : R \to S$ is
{\it finite} if $S$ is finite as an $R$-module.
\end{definition}
```

Texte français :
```tex
\section{Morphismes finis d'anneaux}
\label{section-finite}

\noindent
Voici la définition.

\begin{definition}
\label{definition-finite-ring-map}
Soit $\varphi : R \to S$ un morphisme d'anneaux. Nous disons que $\varphi : R \to S$ est
{\it fini} si $S$ est de type fini comme $R$-module.
\end{definition}
```

</details>

### Passage 24 — lemma-finite-module-over-finite-extension

Source, lignes 641-657 ; français, lignes 636-652.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L641) · identifiant `FR-ALGEBRA-B1-CHOICE-0024`.

La réciproque exige le morphisme d'anneaux fini. Les x_i engendrent S sur R, les y_j engendrent M sur S, et leurs produits engendrent M sur R. Ni la cardinalité de M ni celle de S n'est supposée finie.

Règles appliquées : FR-ALGEBRA-B1-RULE-generation, FR-ALGEBRA-B1-RULE-morphisme-fini.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\begin{lemma}
\label{lemma-finite-module-over-finite-extension}
Let $R \to S$ be a finite ring map.
Let $M$ be an $S$-module.
Then $M$ is finite as an $R$-module if and only if $M$ is finite
as an $S$-module.
\end{lemma}

\begin{proof}
One of the implications follows from
Lemma \ref{lemma-finite-over-subring}.
To see the other assume that $M$ is finite as an $S$-module.
Pick $x_1, \ldots, x_n \in S$ which generate $S$ as an $R$-module.
Pick $y_1, \ldots, y_m \in M$ which generate $M$ as an $S$-module.
Then $x_i y_j$ generate $M$ as an $R$-module.
\end{proof}
```

Texte français :
```tex
\begin{lemma}
\label{lemma-finite-module-over-finite-extension}
Soit $R \to S$ un morphisme d'anneaux fini.
Soit $M$ un $S$-module.
Alors $M$ est de type fini comme $R$-module si et seulement si $M$ est de type fini
comme $S$-module.
\end{lemma}

\begin{proof}
L'une des implications résulte du
Lemme \ref{lemma-finite-over-subring}.
Pour voir l'autre, supposons que $M$ soit de type fini comme $S$-module.
Choisissons $x_1, \ldots, x_n \in S$ qui engendrent $S$ comme $R$-module.
Choisissons $y_1, \ldots, y_m \in M$ qui engendrent $M$ comme $S$-module.
Alors les $x_i y_j$ engendrent $M$ comme $R$-module.
\end{proof}
```

</details>

### Passage 25 — lemma-finite-transitive

Source, lignes 658-670 ; français, lignes 653-665.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L658) · identifiant `FR-ALGEBRA-B1-CHOICE-0025`.

Finitude des deux morphismes et produits t_i s_j donnent la même conclusion sur R vers T. Le renvoi à l'autre preuve est conservé ; aucune injectivité ni intégrité n'est ajoutée.

Règles appliquées : FR-ALGEBRA-B1-RULE-morphisme-fini.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\begin{lemma}
\label{lemma-finite-transitive}
Suppose that $R \to S$ and $S \to T$ are finite ring maps.
Then $R \to T$ is finite.
\end{lemma}

\begin{proof}
If $t_i$ generate $T$ as an $S$-module and $s_j$ generate $S$ as an
$R$-module, then $t_i s_j$ generate $T$ as an $R$-module.
(Also follows from
Lemma \ref{lemma-finite-module-over-finite-extension}.)
\end{proof}
```

Texte français :
```tex
\begin{lemma}
\label{lemma-finite-transitive}
Supposons que $R \to S$ et $S \to T$ soient des morphismes d'anneaux finis.
Alors $R \to T$ est fini.
\end{lemma}

\begin{proof}
Si les $t_i$ engendrent $T$ comme $S$-module et si les $s_j$ engendrent $S$ comme
$R$-module, alors les $t_i s_j$ engendrent $T$ comme $R$-module.
(Cela résulte également du
Lemme \ref{lemma-finite-module-over-finite-extension}.)
\end{proof}
```

</details>

### Passage 26 — lemma-finite-finite-type

Source, lignes 671-701 ; français, lignes 666-696.
[Passage officiel immuable](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L671) · identifiant `FR-ALGEBRA-B1-CHOICE-0026`.

La finitude du module implique le type fini de l'algèbre ; la présentation finie du module implique celle du morphisme. Les relations linéaires, l'expression de 1 et la table de multiplication donnent les trois familles écrites dans la source. Les indices r_j^i et r_ij^k restent littéraux. Le renvoi final vers les extensions finies est conservé, sans développer la preuve.

Point à rendre visible pour la revue : Les sommations finales sont condensées dans l'anglais. Toute réécriture explicative devrait rester extérieure au texte traduit.

Règles appliquées : FR-ALGEBRA-B1-RULE-generation, FR-ALGEBRA-B1-RULE-presentation, FR-ALGEBRA-B1-RULE-morphisme-fini.

<details>
<summary>Lire le passage anglais et le passage français en entier</summary>

Texte anglais :
```tex
\begin{lemma}
\label{lemma-finite-finite-type}
Let $\varphi : R \to S$ be a ring map.
\begin{enumerate}
\item If $\varphi$ is finite, then $\varphi$ is of finite type.
\item If $S$ is of finite presentation as an $R$-module, then
$\varphi$ is of finite presentation.
\end{enumerate}
\end{lemma}

\begin{proof}
For (1) if $x_1, \ldots, x_n \in S$ generate $S$ as an $R$-module,
then $x_1, \ldots, x_n$ generate $S$ as an $R$-algebra. For (2),
suppose that $\sum r_j^ix_i = 0$, $j = 1, \ldots, m$ is a set
of generators of the relations among the $x_i$ when viewed as
$R$-module generators of $S$. Furthermore, write
$1 = \sum r_ix_i$ for some $r_i \in R$ and
$x_ix_j = \sum r_{ij}^k x_k$ for some $r_{ij}^k \in R$.
Then
$$
S = R[t_1, \ldots, t_n]/
(\sum r_j^it_i,\ 1 - \sum r_it_i,\ t_it_j - \sum r_{ij}^k t_k)
$$
as an $R$-algebra which proves (2).
\end{proof}

\noindent
For more information on finite ring maps, please see
Section \ref{section-finite-ring-extensions}.
```

Texte français :
```tex
\begin{lemma}
\label{lemma-finite-finite-type}
Soit $\varphi : R \to S$ un morphisme d'anneaux.
\begin{enumerate}
\item Si $\varphi$ est fini, alors $\varphi$ est de type fini.
\item Si $S$ est de présentation finie comme $R$-module, alors
$\varphi$ est de présentation finie.
\end{enumerate}
\end{lemma}

\begin{proof}
Pour (1), si $x_1, \ldots, x_n \in S$ engendrent $S$ comme $R$-module,
alors $x_1, \ldots, x_n$ engendrent $S$ comme $R$-algèbre. Pour (2),
supposons que $\sum r_j^ix_i = 0$, $j = 1, \ldots, m$, soit un système
de générateurs des relations entre les $x_i$ considérés comme des
générateurs du $R$-module $S$. Écrivons en outre
$1 = \sum r_ix_i$ pour certains $r_i \in R$, et
$x_ix_j = \sum r_{ij}^k x_k$ pour certains $r_{ij}^k \in R$.
Alors
$$
S = R[t_1, \ldots, t_n]/
(\sum r_j^it_i,\ 1 - \sum r_it_i,\ t_it_j - \sum r_{ij}^k t_k)
$$
comme $R$-algèbre, ce qui démontre (2).
\end{proof}

\noindent
Pour plus de renseignements sur les morphismes d'anneaux finis, voir
la section \ref{section-finite-ring-extensions}.
```

</details>

## Contrôles et suite

Les 518 régions mathématiques du périmètre concordent dans l’ordre après la seule normalisation des espaces du vérificateur, sans masque de texte ni exception mathématique. Les familles de commandes invariantes, les événements d’environnement, les mots de contrôle et le nombre d’items restent identiques. Les clés de citation ne changent pas ; le seul nouveau changement de libellé est Lemma vers Lemme.

L’inversion des quatre réparations retrouve exactement la copie précédente. L’inversion supplémentaire des six restaurations historiques retrouve chaque octet du témoin public préservé. Aucune source anglaise ni ancienne copie française n’a été modifiée.

Prochaine lecture : Colimites, ligne source 702, ligne française 697. Ne pas recommencer ces sept sections sans nouvel indice ou modification des octets. Reconstruction et publication suivent la réconciliation de l’édition, pas ce seul contrôle de préfixe.

