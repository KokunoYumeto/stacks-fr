# Chapitre 9 — Transcendance, extensions linéairement disjointes et rappels

**La lecture comparée du chapitre entier est achevée : 28 sections, jusqu’à la fin du fichier officiel. Ce dernier lot couvre les lignes anglaises 3362–3792 et françaises 3355–3784. Une réparation grammaticale, aucune nouvelle correction mathématique. La reconstruction et la publication restent à faire.**

[LaTeX de travail](staged/fr/009_fields.prose-batch7.fr.tex) · [Validation](FIELDS_PROSE_BATCH7_VALIDATION.json) · [Couverture complète](FIELDS_PROSE_BATCH7_COVERAGE.json) · [Choix](FIELDS_PROSE_BATCH7_CHOICES.json) · [Occurrences](FIELDS_PROSE_BATCH7_OCCURRENCES.json) · [Réparation](FIELDS_PROSE_BATCH7_REPAIR.json) · [Lot précédent](FIELDS_PROSE_BATCH6_REVIEW.fr.md)

## Ce qui a été vérifié

Toutes les phrases, preuves, exemples, avertissements et transitions ont été comparés. Les sept lots couvrent sans lacune ni chevauchement 175 paires et les 28 sections. Les blocs de ce dernier lot incluent le diagramme et la fin bibliographique. Cela ne certifie ni la vérité des assertions sources, ni toute attestation terminologique indépendante, ni une revue humaine.

Les 357 régions mathématiques finales sont strictement identiques. À l'échelle du chapitre, les 2 789 régions anglaises et 2 790 françaises concordent après les douze exceptions exactes déjà consignées dans les lots 3–6 : textes lecteurs traduits et un indice explicité, pas un masquage général. Les références, commandes, environnements et listes restent contrôlés. La restauration inverse retrouve tous les octets du témoin public antérieur.

## Canon effectivement consulté

[Identités, passages, courtes attestations et règles](FIELDS_PROSE_BATCH7_CONSULTED_CANON.json). Consultation rétrospective, sans invention d’une consultation du traducteur initial.

### Algèbre 2

Olivier Debarre — [Source](https://www.math.ens.psl.eu/~debarre/Algebre2.pdf) · [PDF préservé](canon-consulted/fr-fields/debarre-algebre2.pdf).

Couverture ; §12, pages imprimées 105–107 / PDF 113–115, notamment définition 12.1, proposition 12.2 et sa preuve, exercices 12.3–12.4. Page 105 rendue et inspectée. La page 108 a été lue mais ses résultats ne sont pas mobilisés.

Appui lexical et contextuel, pas preuve substituée. Le traitement principal porte sur les bases finies ; les degrés infinis sont notés globalement infini. La preuve et la convention cardinales de Stacks demeurent intactes.

976676 octets ; SHA-256 `3FF86D7FD86BA2F1A349ACABE9E4FDDE57282B7A58D66A741CC78BE40E971CC0`.

### Examen 2ème Session 2019/2020 — MU4MA002, Algèbre et théorie de Galois

Anna Cadoret — [Source](https://webusers.imj-prg.fr/~anna.cadoret/ExamenR_2019.pdf) · [PDF préservé](canon-consulted/fr-fields/cadoret-examenr-2019.pdf).

Couverture et quatre pages lues ; seule la définition donnée dans l'exercice 2, question (3), p.2, et le contexte des plongements et de l'exemple précédent appuient les choix présents. Page 2 rendue et inspectée.

Le cadre est fini et le corps ambiant algébriquement clos. Ce sont des exercices, pas des preuves lues. Les questions suivantes emploient indépendantes pour ces extensions ; cette variation n'est pas importée. Le mot composé n'est pas attesté par ce passage.

205714 octets ; SHA-256 `973A18B523488C18BD5CF99842EA128C629FC4945CE2C463EAF5F919E1A12D82`.

### Cours de théorie des corps

Marc Reversat, Benoît Zhang — [Source](https://www.math.univ-toulouse.fr/~reversat/galois.pdf) · [PDF préservé](canon-consulted/fr-fields/reversat-zhang-galois.pdf).

Pages imprimées 30, 31 et 34 / PDF 38, 39 et 42 relues. Appui délimité : remarque 3.1.7, définition 3.1.8, définitions 3.2.1 et 3.3.1. Les preuves qui continuent hors de ces pages ne sont pas présentées comme relues intégralement dans ce lot.

Le vocabulaire appuie les choix, pas une harmonisation des conventions. Les degrés inversés et l'exposant n_i=1 visibles dans la preuve p.31 ne sont pas importés. Les définitions par degré de séparabilité ne remplacent pas celles de Stacks.

816199 octets ; SHA-256 `73A1D0DCD0B7F11625293615E693B198C0C33BAE3A57C78A705153CE33942E8A`.

## Réparation française

Le déterminant Le était laissé devant la formule sans le nom attendu. Polynôme reprend exactement le sujet explicite du sous-cas précédent et l'objet défini dans le texte anglais. Cette reprise répare le français sans modifier la dérivée, sa nullité, la caractéristique ni la conclusion.

Avant :

```tex
\item Le $\text{d}P/\text{d}T$ est identiquement nul.
```

Après :

```tex
\item Le polynôme $\text{d}P/\text{d}T$ est identiquement nul.
```

## Points signalés pour une revue ultérieure

Les questions source restent distinctes des défauts de traduction. Aucune réponse humaine n'est nécessaire pour poursuivre.

- `lemma-transcendence-degree` : L'égalité de cardinaux dans le cas infini et l'argument d'échange sont conservés dans leur forme condensée. Les compléter serait une intervention mathématique, non une réparation de traduction. Ceci n'est pas une admission automatique d'erratum.
- `definition-transcendence-degree` : Debarre rassemble les degrés infinis sous le symbole infini ; Stacks distingue les cardinaux. Ne pas importer cette différence de convention.
- `example-riemann-surface-transcendence` : Aucune nouvelle consultation de Forster ou Hartshorne n'est revendiquée. L'adéquation de la phrase française a été relue contre l'anglais ; l'attestation indépendante de chacun de ses termes reste incomplète.
- `equation-inside-omega` : La définition dépend d'un plongement commun. Le cas fini de Cadoret ne justifie pas un renforcement général du critère tensoriel.
- `definition-separable-algebraic` : Le traitement de l'extension identité en caractéristique zéro n'est pas harmonisé ici : la formulation positive de ce rappel appartient à la source officielle.

## Règles et occurrences

### transcendence

Même notion définie ; conserver le cardinal et la généralité de Stacks.

Occurrences : 31. Appui : DEBARRE-TRANSCENDENCE-B7, 12.1–12.2, pp.105–106.

### pure-transcendental

Expression conservée et définie ; aucune attestation exacte dans les nouvelles pages consultées n'est prétendue.

Occurrences : 4. Appui : SOURCE-OFFICIAL, definition-transcendence.

### relative-closure

Vérifier à chaque occurrence s'il s'agit de clôture absolue ou relative dans K ; la définition locale tranche.

Occurrences : 8. Appui : SOURCE-OFFICIAL, definition-algebraically-closed-in ; definition-separable-algebraic.

### linear-disjointness

Le mot et le rôle du plongement commun sont attestés dans le cas fini ; les restrictions de ce témoin ne sont pas transférées.

Occurrences : 3. Appui : CADORET-DISJOINT-B7, Exercice 2(3), p.2.

### compositum

Nom du plus petit sous-corps commun ; ne pas confondre avec la composition. Pas d'attestation lexicale indépendante dans les passages nouveaux.

Occurrences : 5. Appui : SOURCE-OFFICIAL, definition-compositum ; equation-inside-omega.

### geometry-example

Relecture contre les objets et morphismes anglais ; attestation externe nouvelle incomplète, sans inventer une consultation de Forster ou H.

Occurrences : 8. Appui : SOURCE-OFFICIAL, example-riemann-surface-transcendence.

### separability-review

Séparable, dérivé et purement inséparable sont attestés ; les autres expressions sont conservées en contexte, sans attribuer à ces pages une attestation exacte de chaque variante.

Occurrences : 16. Appui : REVERSAT-ZHANG-REVIEW-B7, 3.1.7–3.2.2, p.30 ; 3.3.1, p.34.

## Toutes les paires comparées

### FR-FIELDS-B7-PROSE-0001

`frontmatter` — source 3362–3362, français 3355–3355.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3362) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Transcendance traduit le titre, sans changer l'identifiant stable qui suit.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\section{Transcendence}
```

```tex
\section{Transcendance}
```

</details>

### FR-FIELDS-B7-PROSE-0002

`section-transcendence` — source 3363–3368, français 3356–3361.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3363) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

La transition annonce seulement le rappel des définitions usuelles ; elle n'introduit ni finitude ni nouvel objet.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-transcendence}

\noindent
We recall the standard definitions.

\begin{definition}
```

```tex
\label{section-transcendence}

\noindent
Rappelons les définitions usuelles.

\begin{definition}
```

</details>

### FR-FIELDS-B7-PROSE-0003

`definition-transcendence` — source 3369–3390, français 3362–3383.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3369) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Famille rend la collection indexée, et l'indépendance reste définie par l'injectivité de l'application de l'anneau de polynômes. L'ensemble d'indices n'est pas restreint au cas fini. Le corps des fractions et la condition algébrique après adjonction de la base sont intacts. Extension transcendante pure est conservé comme choix de registre cohérent avec sa définition explicite ; les pages nouvelles de Debarre attestent base de transcendance, non cette locution exacte.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-transcendence}
Let $K/k$ be a field extension.
\begin{enumerate}
\item A collection of elements $\{x_i\}_{i \in I}$ of $K$ is called
{\it algebraically independent} over $k$ if the map
$$
k[X_i; i\in I] \longrightarrow K
$$
which maps $X_i$ to $x_i$ is injective.
\item The field of fractions of a polynomial ring
$k[x_i; i \in I]$ is denoted $k(x_i; i\in I)$.
\item A {\it purely transcendental extension} of $k$ is any
field extension $K/k$ isomorphic to the field of
fractions of a polynomial ring over $k$.
\item A {\it transcendence basis} of $K/k$ is a
collection of elements $\{x_i\}_{i \in I}$ which are
algebraically independent over $k$ and such that
the extension $K/k(x_i; i\in I)$ is algebraic.
\end{enumerate}
\end{definition}

\begin{example}
```

```tex
\label{definition-transcendence}
Soit $K/k$ une extension de corps.
\begin{enumerate}
\item Une famille d'éléments $\{x_i\}_{i \in I}$ de $K$ est dite
{\it algébriquement indépendante} sur $k$ si l'application
$$
k[X_i; i\in I] \longrightarrow K
$$
qui envoie $X_i$ sur $x_i$ est injective.
\item Le corps des fractions d'un anneau de polynômes
$k[x_i; i \in I]$ est noté $k(x_i; i\in I)$.
\item Une {\it extension transcendante pure} de $k$ est toute
extension de corps $K/k$ isomorphe au corps des
fractions d'un anneau de polynômes sur $k$.
\item Une {\it base de transcendance} de $K/k$ est une
famille d'éléments $\{x_i\}_{i \in I}$ qui sont
algébriquement indépendants sur $k$ et tels que
l'extension $K/k(x_i; i\in I)$ soit algébrique.
\end{enumerate}
\end{definition}

\begin{example}
```

</details>

### FR-FIELDS-B7-PROSE-0004

`example-pi-transcendental` — source 3391–3397, français 3384–3390.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3391) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

La négation et la qualification non nul sont conservées. L'isomorphisme avec un corps rationnel reste le même ; aucune démonstration de la transcendance de pi n'est ajoutée.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{example-pi-transcendental}
The field $\mathbf{Q}(\pi)$ is purely transcendental because
$\pi$ isn't the root of a nonzero polynomial with rational coefficients.
In particular, $\mathbf{Q}(\pi) \cong \mathbf{Q}(x)$.
\end{example}

\begin{lemma}
```

```tex
\label{example-pi-transcendental}
Le corps $\mathbf{Q}(\pi)$ est une extension transcendante pure, car
$\pi$ n'est racine d'aucun polynôme non nul à coefficients rationnels.
En particulier, $\mathbf{Q}(\pi) \cong \mathbf{Q}(x)$.
\end{example}

\begin{lemma}
```

</details>

### FR-FIELDS-B7-PROSE-0005

`lemma-transcendence-degree` — source 3398–3473, français 3391–3466.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3398) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Toute la preuve est conservée : parties A et G, ordre par inclusion, chaînes et support fini des polynômes, Zorn, maximalité, puis comparaison des cardinaux dans les cas infini et fini. Le passage de F(G)=E à un générateur transcendant conserve sa portée. Dans l'échange fini, les polynômes f et g restent irréductibles, les variables effectivement présentes sont les mêmes, et la multiplicité des éléments de B* est explicitement conservée. Bases est rendu par bases de transcendance aux deux emplois abrégés de l'anglais : les objets sont ceux définis dans ce lemme, non des bases vectorielles. La preuve française ne remplace pas le raisonnement anglais par la preuve différente du cours consulté.

**Réserve :** L'égalité de cardinaux dans le cas infini et l'argument d'échange sont conservés dans leur forme condensée. Les compléter serait une intervention mathématique, non une réparation de traduction. Ceci n'est pas une admission automatique d'erratum.

Choix écartés :

- Bases vectorielles : exclu par les définitions et la preuve.
- Réécrire la preuve avec le résultat du canon : exclu de la traduction fidèle.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-transcendence-degree}
Let $E/F$ be a field extension. A transcendence basis of $E$ over $F$ exists.
Any two transcendence bases have the same cardinality.
\end{lemma}

\begin{proof}
Let $A$ be an algebraically independent subset of $E$. Let $G$ be a subset
of $E$ containing $A$ that generates $E/F$. We claim we can find a
transcendence basis $B$ such that $A \subset B \subset G$.
To prove this, consider the collection $\mathcal{B}$ of algebraically
independent subsets whose members are subsets of $G$ that contain $A$.
Define a partial ordering on $\mathcal{B}$ using inclusion.
Then $\mathcal{B}$ contains at least one element $A$.
The union of the elements of a totally ordered subset $T$ of $\mathcal{B}$
is an algebraically independent subset of $E$ over $F$ since any algebraic
dependence relation would have occurred in one of the elements of $T$
(since polynomials only involve finitely many variables). The union also
contains $A$ and is contained in $G$. By Zorn's lemma, there is a maximal
element $B \in \mathcal{B}$. Now we claim $E$ is algebraic over $F(B)$.
This is because if it wasn't then there would be an element
$f \in G$ transcendental over $F(B)$ since $F(G) = E$. Then
$B \cup\{f\}$ would be algebraically independent contradicting the
maximality of $B$. Thus $B$ is our transcendence basis.

\medskip\noindent
Let $B$ and $B'$ be two transcendence bases. Without loss of generality, we
can assume that $|B'| \leq |B|$. Now we divide the proof into two cases: the
first case is that $B$ is an infinite set. Then for each $\alpha \in B'$,
there is a finite set $B_{\alpha} \subset B$ such that $\alpha$ is algebraic
over
$F(B_{\alpha})$ since any algebraic dependence relation only uses finitely many
indeterminates. Then we define $B^* = \bigcup_{\alpha\in B'} B_{\alpha}$.
By construction, $B^* \subset B$, but we claim that in fact the two sets are
equal. To see this, suppose that they are not equal, say there is an element
$\beta \in B \setminus B^*$. We know $\beta$ is algebraic over $F(B')$ which
is algebraic over $F(B^*)$. Therefore $\beta$ is algebraic over $F(B^*)$, a
contradiction. So $|B| \leq |\bigcup_{\alpha \in B'} B_{\alpha}|$.
Now if $B'$ is finite, then so is $B$ so we can assume $B'$ is infinite;
this means
$$
|B| \leq |\bigcup\nolimits_{\alpha \in B'} B_{\alpha}| = |B'|
$$
because each $B_\alpha$ is finite and $B'$ is infinite. Therefore in the
infinite case, $|B| = |B'|$.

\medskip\noindent
Now we need to look at the case where $B$ is finite.
In this case, $B'$ is also finite, so suppose
$B = \{\alpha_1, \ldots, \alpha_n\}$ and
$B' = \{\beta_1, \ldots, \beta_m\}$ with $m \leq n$.
We perform induction on $m$: if $m = 0$ then $E/F$ is algebraic so
$B = \emptyset$ so $n = 0$. If $m > 0$, there is an irreducible polynomial
$f \in F[x, y_1, \ldots, y_n]$ such that
$f(\beta_1, \alpha_1, \ldots, \alpha_n) = 0$ and such that $x$ occurs in $f$.
Since $\beta_1$ is not algebraic over $F$, $f$ must involve some $y_i$
so without loss of generality, assume $f$ uses $y_1$.
Let $B^* = \{\beta_1, \alpha_2, \ldots, \alpha_n\}$.
We claim that $B^*$ is a basis for $E/F$. To prove this claim, we see that
we have a tower of algebraic extensions
$$
E/ F(B^*, \alpha_1) / F(B^*)
$$
since $\alpha_1$ is algebraic over $F(B^*)$.
Now we claim that $B^*$ (counting multiplicity of elements) is
algebraically independent over $F$ because if it weren't, then there would be an
irreducible $g\in F[x, y_2, \ldots, y_n]$ such that
$g(\beta_1, \alpha_2, \ldots, \alpha_n) = 0$
which must involve $x$ making $\beta_1$
algebraic over $F(\alpha_2, \ldots, \alpha_n)$ which would make $\alpha_1$
algebraic over $F(\alpha_2, \ldots, \alpha_n)$ which is impossible.
So this means that $\{\alpha_2, \ldots, \alpha_n\}$ and
$\{\beta_2, \ldots, \beta_m\}$ are bases for $E$ over $F(\beta_1)$
which means by induction, $m = n$.
\end{proof}

\begin{definition}
```

```tex
\label{lemma-transcendence-degree}
Soit $E/F$ une extension de corps. Il existe une base de transcendance de $E$ sur $F$.
Deux bases de transcendance quelconques ont même cardinal.
\end{lemma}

\begin{proof}
Soit $A$ une partie algébriquement indépendante de $E$. Soit $G$ une partie
de $E$ contenant $A$ qui engendre $E/F$. Nous affirmons qu'il existe une
base de transcendance $B$ telle que $A \subset B \subset G$.
Pour le démontrer, considérons l'ensemble $\mathcal{B}$ des parties
algébriquement indépendantes qui sont des parties de $G$ contenant $A$.
Ordonnons partiellement $\mathcal{B}$ par inclusion.
Alors $\mathcal{B}$ contient au moins l'élément $A$.
La réunion des éléments d'une partie totalement ordonnée $T$ de $\mathcal{B}$
est une partie de $E$ algébriquement indépendante sur $F$, car toute relation
de dépendance algébrique apparaîtrait déjà dans l'un des éléments de $T$
(puisque les polynômes ne font intervenir qu'un nombre fini de variables). Cette réunion
contient aussi $A$ et est contenue dans $G$. D'après le lemme de Zorn, il existe un
élément maximal $B \in \mathcal{B}$. Nous affirmons maintenant que $E$ est algébrique sur $F(B)$.
En effet, sinon il existerait un élément
$f \in G$ transcendant sur $F(B)$, puisque $F(G) = E$. Alors
$B \cup\{f\}$ serait algébriquement indépendante, contrairement à la
maximalité de $B$. Ainsi $B$ est la base de transcendance recherchée.

\medskip\noindent
Soient $B$ et $B'$ deux bases de transcendance. Sans perte de généralité, nous
pouvons supposer que $|B'| \leq |B|$. Divisons la démonstration en deux cas :
le premier est celui où $B$ est un ensemble infini. Alors, pour chaque $\alpha \in B'$,
il existe un ensemble fini $B_{\alpha} \subset B$ tel que $\alpha$ soit algébrique
sur
$F(B_{\alpha})$, puisque toute relation de dépendance algébrique n'utilise qu'un nombre fini
d'indéterminées. Posons alors $B^* = \bigcup_{\alpha\in B'} B_{\alpha}$.
Par construction, $B^* \subset B$, mais nous affirmons qu'en fait ces deux ensembles sont
égaux. Pour le voir, supposons qu'ils ne le soient pas et qu'il existe, par exemple, un élément
$\beta \in B \setminus B^*$. Nous savons que $\beta$ est algébrique sur $F(B')$, qui
est algébrique sur $F(B^*)$. Par conséquent, $\beta$ est algébrique sur $F(B^*)$, ce qui est
une contradiction. Ainsi $|B| \leq |\bigcup_{\alpha \in B'} B_{\alpha}|$.
Si $B'$ est fini, alors $B$ l'est également ; nous pouvons donc supposer $B'$ infini.
Il vient
$$
|B| \leq |\bigcup\nolimits_{\alpha \in B'} B_{\alpha}| = |B'|
$$
car chaque $B_\alpha$ est fini et $B'$ est infini. Par conséquent, dans le
cas infini, $|B| = |B'|$.

\medskip\noindent
Il reste à étudier le cas où $B$ est fini.
Dans ce cas, $B'$ est également fini ; écrivons
$B = \{\alpha_1, \ldots, \alpha_n\}$ et
$B' = \{\beta_1, \ldots, \beta_m\}$ avec $m \leq n$.
Raisonnons par récurrence sur $m$ : si $m = 0$, alors $E/F$ est algébrique, donc
$B = \emptyset$ et $n = 0$. Si $m > 0$, il existe un polynôme irréductible
$f \in F[x, y_1, \ldots, y_n]$ tel que
$f(\beta_1, \alpha_1, \ldots, \alpha_n) = 0$ et tel que $x$ intervienne dans $f$.
Puisque $\beta_1$ n'est pas algébrique sur $F$, $f$ doit faire intervenir un certain $y_i$ ;
sans perte de généralité, supposons que $f$ fasse intervenir $y_1$.
Posons $B^* = \{\beta_1, \alpha_2, \ldots, \alpha_n\}$.
Nous affirmons que $B^*$ est une base de transcendance de l'extension $E/F$. Pour le montrer, remarquons que
nous avons une tour d'extensions algébriques
$$
E/ F(B^*, \alpha_1) / F(B^*)
$$
puisque $\alpha_1$ est algébrique sur $F(B^*)$.
Nous affirmons maintenant que $B^*$ (en comptant les éléments avec multiplicité) est
algébriquement indépendante sur $F$ : en effet, sinon, il existerait un
polynôme irréductible $g\in F[x, y_2, \ldots, y_n]$ tel que
$g(\beta_1, \alpha_2, \ldots, \alpha_n) = 0$,
dans lequel $x$ devrait intervenir, rendant $\beta_1$
algébrique sur $F(\alpha_2, \ldots, \alpha_n)$, ce qui rendrait $\alpha_1$
algébrique sur $F(\alpha_2, \ldots, \alpha_n)$, chose impossible.
Cela signifie donc que $\{\alpha_2, \ldots, \alpha_n\}$ et
$\{\beta_2, \ldots, \beta_m\}$ sont des bases de transcendance de $E$ sur $F(\beta_1)$ ;
par récurrence, $m = n$.
\end{proof}

\begin{definition}
```

</details>

### FR-FIELDS-B7-PROSE-0006

`definition-transcendence-degree` — source 3474–3481, français 3467–3474.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3474) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Le degré est le cardinal d'une base, y compris un cardinal infini. On conserve la notation trdeg et le corps de base. Le vocabulaire de Debarre appuie le nom, pas le remplacement de tous les cardinaux infinis par un unique symbole infini.

**Réserve :** Debarre rassemble les degrés infinis sous le symbole infini ; Stacks distingue les cardinaux. Ne pas importer cette différence de convention.

Choix écartés :

- Remplacer tous les cardinaux infinis par infini : changerait la convention source.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-transcendence-degree}
Let $K/k$ be a field extension.
The {\it transcendence degree} of $K$ over $k$ is
the cardinality of a transcendence basis of $K$ over $k$.
It is denoted $\text{trdeg}_k(K)$.
\end{definition}

\begin{lemma}
```

```tex
\label{definition-transcendence-degree}
Soit $K/k$ une extension de corps.
Le {\it degré de transcendance} de $K$ sur $k$ est
le cardinal d'une base de transcendance de $K$ sur $k$.
Il est noté $\text{trdeg}_k(K)$.
\end{definition}

\begin{lemma}
```

</details>

### FR-FIELDS-B7-PROSE-0007

`lemma-transcendence-degree-tower` — source 3482–3499, français 3475–3492.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3482) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Les trois corps et la somme des degrés restent dans le même ordre. La preuve choisit A dans K et B dans L et garde la réunion A union B. La brièveté de la vérification reste celle de la source ; aucune hypothèse de type fini n'est importée du canon.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-transcendence-degree-tower}
Let $L/K/k$ be field extensions.
Then
$$
\text{trdeg}_k(L) =
\text{trdeg}_K(L) +
\text{trdeg}_k(K).
$$
\end{lemma}

\begin{proof}
Choose a transcendence basis $A \subset K$ of $K$ over $k$.
Choose a transcendence basis $B \subset L$ of $L$ over $K$.
Then it is straightforward to see that $A \cup B$ is a transcendence
basis of $L$ over $k$.
\end{proof}

\begin{example}
```

```tex
\label{lemma-transcendence-degree-tower}
Soient $L/K/k$ des extensions de corps.
Alors
$$
\text{trdeg}_k(L) =
\text{trdeg}_K(L) +
\text{trdeg}_k(K).
$$
\end{lemma}

\begin{proof}
Choisissons une base de transcendance $A \subset K$ de $K$ sur $k$.
Choisissons une base de transcendance $B \subset L$ de $L$ sur $K$.
Il est alors immédiat que $A \cup B$ est une base de transcendance
de $L$ sur $k$.
\end{proof}

\begin{example}
```

</details>

### FR-FIELDS-B7-PROSE-0008

`example-pi-e-transcendental` — source 3500–3510, français 3493–3503.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3500) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Au moins un et la possibilité du degré deux sont distingués. L'incertitude sur l'indépendance de e et pi est celle du témoin anglais daté, non une mise à jour bibliographique. La source évoque les nombres ensemble et non seulement leur transcendance individuelle.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{example-pi-e-transcendental}
Consider the field extension $\mathbf{Q}(e, \pi)$ formed by
adjoining the numbers $e$ and $\pi$. This field extension has transcendence
degree at least $1$ since both $e$ and $\pi$ are transcendental over the
rationals. However, this field extension might have transcendence
degree $2$ if $e$ and $\pi$ are algebraically independent. Whether or
not this is true is unknown and whence the problem of determining
$\text{trdeg}(\mathbf{Q}(e, \pi))$ is open.
\end{example}

\begin{example}
```

```tex
\label{example-pi-e-transcendental}
Considérons l'extension de corps $\mathbf{Q}(e, \pi)$ obtenue en
adjoignant les nombres $e$ et $\pi$. Cette extension de corps a un degré de transcendance
au moins égal à $1$, puisque $e$ et $\pi$ sont tous deux transcendants sur les
rationnels. Toutefois, cette extension de corps pourrait avoir un degré de transcendance
égal à $2$ si $e$ et $\pi$ sont algébriquement indépendants. On ignore si
c'est le cas ; le problème de la détermination de
$\text{trdeg}(\mathbf{Q}(e, \pi))$ est donc ouvert.
\end{example}

\begin{example}
```

</details>

### FR-FIELDS-B7-PROSE-0009

`example-function-field-not-unique-transcendence-basis` — source 3511–3521, français 3504–3514.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3511) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Les deux bases t et t², l'extension algébrique F(t)/F(t²) et la non-unicité de la décomposition sont présents. Pure porte sur l'extension transcendante ; il ne signifie ni algébrique ni purement inséparable. Aucune nouvelle restriction de caractéristique n'est ajoutée.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{example-function-field-not-unique-transcendence-basis}
Let $F$ be a field and $E = F(t)$. Then $\{t\}$ is a
transcendence basis since $E = F(t)$. However, $\{t^2\}$
is also a transcendence basis since $F(t)/F(t^2)$ is algebraic.
This illustrates that while we can always decompose an extension
$E/F$ into an algebraic extension $E/F'$ and a
purely transcendental extension $F'/F$, this decomposition is not unique and
depends on choice of transcendence basis.
\end{example}

\begin{example}
```

```tex
\label{example-function-field-not-unique-transcendence-basis}
Soit $F$ un corps et soit $E = F(t)$. Alors $\{t\}$ est une
base de transcendance puisque $E = F(t)$. Toutefois, $\{t^2\}$
est aussi une base de transcendance puisque $F(t)/F(t^2)$ est algébrique.
Cela montre que, bien que nous puissions toujours décomposer une extension
$E/F$ en une extension algébrique $E/F'$ et une
extension transcendante pure $F'/F$, cette décomposition n'est pas unique et
dépend du choix d'une base de transcendance.
\end{example}

\begin{example}
```

</details>

### FR-FIELDS-B7-PROSE-0010

`example-riemann-surface-transcendence` — source 3522–3546, français 3515–3539.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3522) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

La compacité de la surface, le degré un, le type fini et les applications non constantes sont tous conservés. La première équivalence utilise bien la catégorie opposée ; la seconde est une anti-équivalence. Dans le passage aux courbes, irréductible reste entre parenthèses, et le dénominateur ne doit pas s'annuler identiquement sur la courbe. Projectives lisses conserve les deux adjectifs de smooth projective. Les renvois Forster, H et celui du chapitre Courbes sont inchangés. Les nouvelles pages consultées ne constituent pas une attestation indépendante de tout ce vocabulaire analytique et catégorique : ce point est déclaré, pas couvert par une citation de pure apparence.

**Réserve :** Aucune nouvelle consultation de Forster ou Hartshorne n'est revendiquée. L'adéquation de la phrase française a été relue contre l'anglais ; l'attestation indépendante de chacun de ses termes reste incomplète.

Choix écartés :

- Omettre non constants ou la catégorie opposée : modifierait les morphismes et le sens de l'équivalence.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{example-riemann-surface-transcendence}
Let $X$ be a compact Riemann surface. Then the function field
$\mathbf{C}(X)$ (see Example \ref{example-field-of-meromorphic-functions})
has transcendence degree one over $\mathbf{C}$. In fact, {\it any}
finitely generated extension of $\mathbf{C}$ of transcendence degree
one arises from a Riemann surface. There is even an equivalence of
categories between the category of compact Riemann surfaces and
(non-constant) holomorphic maps and the opposite of the category of finitely
generated extensions of $\mathbf{C}$ of transcendence degree $1$
and morphisms of $\mathbf{C}$-algebras. See \cite{Forster}.

\medskip\noindent
There is an algebraic version of the above statement as well. Given an
(irreducible) algebraic curve in projective space over an algebraically
closed field $k$ (e.g. the complex numbers), one can consider its
``field of rational functions'': basically, functions that look like
quotients of polynomials, where the denominator does not identically
vanish on the curve. There is a similar anti-equivalence of categories
(Algebraic Curves, Theorem \ref{curves-theorem-curves-rational-maps})
between smooth projective curves and
non-constant morphisms of curves and finitely generated extensions of $k$ of
transcendence degree one. See \cite{H}.
\end{example}

\begin{definition}
```

```tex
\label{example-riemann-surface-transcendence}
Soit $X$ une surface de Riemann compacte. Alors le corps des fonctions
$\mathbf{C}(X)$ (voir Exemple \ref{example-field-of-meromorphic-functions})
est de degré de transcendance un sur $\mathbf{C}$. En fait, {\it toute}
extension de type fini de $\mathbf{C}$ de degré de transcendance
un provient d'une surface de Riemann. Il existe même une équivalence de
catégories entre la catégorie des surfaces de Riemann compactes et des
applications holomorphes (non constantes), et l'opposée de la catégorie des extensions
de type fini de $\mathbf{C}$ de degré de transcendance $1$
et des morphismes de $\mathbf{C}$-algèbres. Voir \cite{Forster}.

\medskip\noindent
Il existe également une version algébrique de l'énoncé précédent. Étant donnée une
courbe algébrique (irréductible) dans l'espace projectif sur un corps algébriquement
clos $k$ (par exemple le corps des nombres complexes), on peut considérer son
« corps des fonctions rationnelles » : il s'agit essentiellement des fonctions qui se présentent comme
des quotients de polynômes, dont le dénominateur ne s'annule pas identiquement
sur la courbe. Il existe une anti-équivalence analogue de catégories
(Courbes algébriques, Théorème \ref{curves-theorem-curves-rational-maps})
entre les courbes projectives lisses et
les morphismes non constants de courbes, et les extensions de type fini de $k$ de
degré de transcendance un. Voir \cite{H}.
\end{example}

\begin{definition}
```

</details>

### FR-FIELDS-B7-PROSE-0011

`definition-algebraically-closed-in` — source 3547–3558, français 3540–3551.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3547) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Dans K est essentiel : il s'agit de la clôture relative à l'intérieur de K, non du choix d'une clôture algébrique absolue. Chaque élément algébrique doit appartenir à k. La formulation française et les deux clauses ne renforcent pas cette condition.

Choix écartés :

- Clôture algébrique sans dans K : perdrait le caractère relatif de la définition.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-algebraically-closed-in}
Let $K/k$ be a field extension.
\begin{enumerate}
\item The {\it algebraic closure of $k$ in $K$} is the subfield
$k'$ of $K$ consisting of elements of $K$ which are algebraic over $k$.
\item We say $k$ is {\it algebraically closed in $K$} if
every element of $K$ which is algebraic over $k$ is
contained in $k$.
\end{enumerate}
\end{definition}

\begin{lemma}
```

```tex
\label{definition-algebraically-closed-in}
Soit $K/k$ une extension de corps.
\begin{enumerate}
\item La {\it clôture algébrique de $k$ dans $K$} est le sous-corps
$k'$ de $K$ formé des éléments de $K$ qui sont algébriques sur $k$.
\item Nous disons que $k$ est {\it algébriquement clos dans $K$} si
tout élément de $K$ qui est algébrique sur $k$
appartient à $k$.
\end{enumerate}
\end{definition}

\begin{lemma}
```

</details>

### FR-FIELDS-B7-PROSE-0012

`lemma-purely-transcendental-degree` — source 3559–3583, français 3552–3576.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3559) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Le degré fini k'/k, les mêmes indéterminées des deux côtés et l'égalité des degrés sont conservés. La preuve garde la réduction à un générateur par multiplicativité, le polynôme minimal, l'irréductibilité après extension rationnelle et l'esquisse par spécialisation puis Gauss. Unitaire traduit monic, non irréductible ou de degré un. La mention que la démonstration est seulement esquissée reste explicite.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-purely-transcendental-degree}
Let $k'/k$ be a finite extension of fields. Let
$k'(x_1, \ldots, x_r)/k(x_1, \ldots, x_r)$ be the
induced extension of purely transcendental extensions.
Then $[k'(x_1, \ldots, x_r) : k(x_1, \ldots, x_r)] = [k' : k] < \infty$.
\end{lemma}

\begin{proof}
By multiplicativity of degrees of extensions
(Lemma \ref{lemma-multiplicativity-degrees})
it suffices to prove this when $k'$ is generated by a single element
$\alpha \in k'$ over $k$. Let $f \in k[T]$ be the minimal polynomial
of $\alpha$ over $k$. Then $k'(x_1, \ldots, x_r)$ is generated
by $\alpha, x_1, \ldots, x_r$ over $k$ and hence $k'(x_1, \ldots, x_r)$
is generated by $\alpha$ over $k(x_1, \ldots, x_r)$.
Thus it suffices to show that $f$ is still irreducible as
an element of $k(x_1, \ldots, x_r)[T]$. We only sketch the proof.
It is clear that $f$ is irreducible as an element of
$k[x_1, \ldots, x_r, T]$ for example because $f$ is monic
as a polynomial in $T$ and any putative factorization in
$k[x_1, \ldots, x_r, T]$ would lead to a factorization in $k[T]$
by setting $x_i$ equal to $0$. By Gauss' lemma we conclude.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-purely-transcendental-degree}
Soit $k'/k$ une extension finie de corps. Soit
$k'(x_1, \ldots, x_r)/k(x_1, \ldots, x_r)$
l'extension induite des extensions transcendantes pures.
Alors $[k'(x_1, \ldots, x_r) : k(x_1, \ldots, x_r)] = [k' : k] < \infty$.
\end{lemma}

\begin{proof}
Par multiplicativité des degrés des extensions
(Lemme \ref{lemma-multiplicativity-degrees}),
il suffit de le démontrer lorsque $k'$ est engendré par un unique élément
$\alpha \in k'$ sur $k$. Soit $f \in k[T]$ le polynôme minimal
de $\alpha$ sur $k$. Alors $k'(x_1, \ldots, x_r)$ est engendré
par $\alpha, x_1, \ldots, x_r$ sur $k$, et donc $k'(x_1, \ldots, x_r)$
est engendré par $\alpha$ sur $k(x_1, \ldots, x_r)$.
Il suffit donc de montrer que $f$ reste irréductible comme
élément de $k(x_1, \ldots, x_r)[T]$. Nous ne faisons qu'esquisser la démonstration.
Il est clair que $f$ est irréductible comme élément de
$k[x_1, \ldots, x_r, T]$, par exemple parce que $f$ est unitaire
comme polynôme en $T$ et que toute factorisation éventuelle dans
$k[x_1, \ldots, x_r, T]$ conduirait à une factorisation dans $k[T]$
en posant les $x_i$ égaux à $0$. Le lemme de Gauss permet de conclure.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B7-PROSE-0013

`lemma-algebraic-closure-in-finitely-generated` — source 3584–3610, français 3577–3603.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3584) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Type fini qualifie l'extension K/k ; le degré n après choix d'une base de transcendance est fini. Supposons que les x_i forment une base est ici une introduction d'objets choisis, pas une hypothèse ajoutée au lemme. Le corps k' parcourt les extensions intermédiaires finies, et leur borne commune reste n. La conclusion condensée à partir de cette borne n'est pas remplacée par une preuve supplémentaire.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-algebraic-closure-in-finitely-generated}
Let $K/k$ be a finitely generated field extension.
The algebraic closure of $k$ in $K$ is finite over $k$.
\end{lemma}

\begin{proof}
Let $x_1, \ldots, x_r \in K$ be a transcendence basis for $K$
over $k$. Then $n = [K : k(x_1, \ldots, x_r)] < \infty$.
Suppose that $k \subset k' \subset K$ with $k'/k$ finite.
In this case
$[k'(x_1, \ldots, x_r) : k(x_1, \ldots, x_r)] = [k' : k] < \infty$, see
Lemma \ref{lemma-purely-transcendental-degree}.
Hence
$$
[k' : k] = [k'(x_1, \ldots, x_r) : k(x_1, \ldots, x_r)] \leq
[K : k(x_1, \ldots, x_r)] = n.
$$
In other words, the degrees of finite subextensions are bounded
and the lemma follows.
\end{proof}






\section{Linearly disjoint extensions}
```

```tex
\label{lemma-algebraic-closure-in-finitely-generated}
Soit $K/k$ une extension de corps de type fini.
La clôture algébrique de $k$ dans $K$ est finie sur $k$.
\end{lemma}

\begin{proof}
Supposons que $x_1, \ldots, x_r \in K$ forment une base de transcendance de $K$
sur $k$. Alors $n = [K : k(x_1, \ldots, x_r)] < \infty$.
Supposons que $k \subset k' \subset K$ et que $k'/k$ soit finie.
Dans ce cas,
$[k'(x_1, \ldots, x_r) : k(x_1, \ldots, x_r)] = [k' : k] < \infty$, voir le
Lemme \ref{lemma-purely-transcendental-degree}.
Par conséquent,
$$
[k' : k] = [k'(x_1, \ldots, x_r) : k(x_1, \ldots, x_r)] \leq
[K : k(x_1, \ldots, x_r)] = n.
$$
Autrement dit, les degrés des extensions intermédiaires finies sont bornés,
et le lemme en résulte.
\end{proof}






\section{Extensions linéairement disjointes}
```

</details>

### FR-FIELDS-B7-PROSE-0014

`section-linearly-disjoint` — source 3611–3617, français 3604–3610.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3611) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Les deux extensions sont plongées dans un même corps Omega. Cette donnée commune est conservée avant les définitions, sans exiger que Omega soit algébriquement clos comme dans l'exercice du canon consulté.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-linearly-disjoint}

\noindent
Let $k$ be a field, $K$ and $L$ field extensions of $k$.
Suppose also that $K$ and $L$ are embedded in some larger field $\Omega$.

\begin{definition}
```

```tex
\label{section-linearly-disjoint}

\noindent
Soit $k$ un corps, et soient $K$ et $L$ des extensions de corps de $k$.
Supposons aussi que $K$ et $L$ soient plongés dans un corps plus grand $\Omega$.

\begin{definition}
```

</details>

### FR-FIELDS-B7-PROSE-0015

`definition-compositum` — source 3618–3620, français 3611–3613.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3618) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Le diagramme annoncé fait partie de la définition ; son identifiant d'équation provoque seulement une frontière technique entre deux paires du relevé. Rien n'est omis.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-compositum}
Consider a diagram
\begin{equation}
```

```tex
\label{definition-compositum}
Considérons un diagramme
\begin{equation}
```

</details>

### FR-FIELDS-B7-PROSE-0016

`equation-inside-omega` — source 3621–3650, français 3614–3643.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3621) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Les quatre sommets et flèches sont identiques. Composé nomme le plus petit sous-corps contenant K et L, non une composition de fonctions. L'avertissement conserve la dépendance envers les plongements ainsi que les deux exemples de degrés 24 et 48 ; l'absence de preuve du second degré est annoncée comme dans l'original. Corps composé explicite le même objet lorsque l'anglais écrit composition : aucun objet mathématique n'est changé. Cadoret confirme le rôle des plongements et l'exemple, mais n'est pas présentée comme une attestation lexicale du mot composé.

**Réserve :** La définition dépend d'un plongement commun. Le cas fini de Cadoret ne justifie pas un renforcement général du critère tensoriel.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{equation-inside-omega}
\vcenter{
\xymatrix{
L \ar[r] & \Omega \\
k \ar[r] \ar[u] & K \ar[u]
}
}
\end{equation}
of field extensions. The {\it compositum of $K$ and $L$ in $\Omega$}
written $KL$ is the smallest subfield of $\Omega$ containing both
$L$ and $K$.
\end{definition}

\noindent
It is clear that $KL$ is generated by the set $K \cup L$ over $k$,
generated by the set $K$ over $L$, and generated by the set $L$ over $K$.

\medskip\noindent
{\bf Warning:} The (isomorphism class of the) composition depends on
the choice of the embeddings of $K$ and $L$ into $\Omega$. For example
consider the number fields $K = \mathbf{Q}(2^{1/8}) \subset \mathbf{R}$ and
$L = \mathbf{Q}(2^{1/12}) \subset \mathbf{R}$. The compositum inside
$\mathbf{R}$ is the field $\mathbf{Q}(2^{1/24})$ of degree $24$ over
$\mathbf{Q}$. However, if we embed $K = \mathbf{Q}[x]/(x^8 - 2)$ into
$\mathbf{C}$ by mapping $x$ to $2^{1/8}e^{2\pi i/8}$, then the compositum
$\mathbf{Q}(2^{1/12}, 2^{1/8}e^{2\pi i/8})$ contains $i = e^{2\pi i/4}$ and has
degree $48$ over $\mathbf{Q}$ (we omit showing the degree is $48$, but
the existence of $i$ certainly proves the two composita are not isomorphic).

\begin{definition}
```

```tex
\label{equation-inside-omega}
\vcenter{
\xymatrix{
L \ar[r] & \Omega \\
k \ar[r] \ar[u] & K \ar[u]
}
}
\end{equation}
d'extensions de corps. Le {\it composé de $K$ et $L$ dans $\Omega$},
noté $KL$, est le plus petit sous-corps de $\Omega$ contenant à la fois
$L$ et $K$.
\end{definition}

\noindent
Il est clair que $KL$ est engendré par l'ensemble $K \cup L$ sur $k$,
par l'ensemble $K$ sur $L$, et par l'ensemble $L$ sur $K$.

\medskip\noindent
{\bf Avertissement :} La classe d'isomorphisme du corps composé dépend du
choix des plongements de $K$ et $L$ dans $\Omega$. Considérons par exemple
les corps de nombres $K = \mathbf{Q}(2^{1/8}) \subset \mathbf{R}$ et
$L = \mathbf{Q}(2^{1/12}) \subset \mathbf{R}$. Leur composé dans
$\mathbf{R}$ est le corps $\mathbf{Q}(2^{1/24})$, de degré $24$ sur
$\mathbf{Q}$. Toutefois, si nous plongeons $K = \mathbf{Q}[x]/(x^8 - 2)$ dans
$\mathbf{C}$ en envoyant $x$ sur $2^{1/8}e^{2\pi i/8}$, alors le composé
$\mathbf{Q}(2^{1/12}, 2^{1/8}e^{2\pi i/8})$ contient $i = e^{2\pi i/4}$ et est de
degré $48$ sur $\mathbf{Q}$ (nous omettons de montrer que le degré vaut $48$, mais
l'existence de $i$ prouve assurément que les deux composés ne sont pas isomorphes).

\begin{definition}
```

</details>

### FR-FIELDS-B7-PROSE-0017

`definition-linearly-disjoint` — source 3651–3665, français 3644–3658.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3651) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Linéairement disjoints s'accorde avec les deux corps ; le titre au féminin s'accorde avec extensions. Le critère est l'injectivité de K tenseur L vers KL, avec la même règle sur les tenseurs. Il n'est remplacé ni par la surjectivité ni par la seule condition d'intersection. Le témoin français emploie ce nom dans un cas fini ; aucune finitude n'est importée ici.

Choix écartés :

- Remplacer injective par isomorphisme : importerait sans justification une formulation du cas fini.
- Remplacer le critère par K intersection L = k : ne traduit pas la définition donnée.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-linearly-disjoint}
Consider a diagram of fields as in (\ref{equation-inside-omega}).
We say that $K$ and $L$ are {\it linearly disjoint over $k$ in $\Omega$}
if the map
$$
K \otimes_k L \longrightarrow KL,\quad
\sum x_i \otimes y_i \longmapsto \sum x_i y_i
$$
is injective.
\end{definition}

\noindent
The following lemma does not seem to fit anywhere else.

\begin{lemma}
```

```tex
\label{definition-linearly-disjoint}
Considérons un diagramme de corps comme dans (\ref{equation-inside-omega}).
Nous disons que $K$ et $L$ sont {\it linéairement disjoints sur $k$ dans $\Omega$}
si l'application
$$
K \otimes_k L \longrightarrow KL,\quad
\sum x_i \otimes y_i \longmapsto \sum x_i y_i
$$
est injective.
\end{definition}

\noindent
Le lemme suivant ne semble trouver sa place nulle part ailleurs.

\begin{lemma}
```

</details>

### FR-FIELDS-B7-PROSE-0018

`lemma-normal-case` — source 3666–3691, français 3659–3684.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3666) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Algébrique et normale portent sur E/F sans ajout de finitude. Les deux ordres des étages séparables et purement inséparables restent distincts. L'identification tensorielle et le sous-corps des invariants de Aut(E/F) sont intacts. La preuve garde son renvoi et ses détails omis : le canon ne sert pas à développer une démonstration absente du texte officiel.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-normal-case}
Let $E/F$ be a normal algebraic field extension. There exist subextensions
$E / E_{sep} /F$ and $E / E_{insep} / F$ such that
\begin{enumerate}
\item $F \subset E_{sep}$ is Galois and $E_{sep} \subset E$
is purely inseparable,
\item $F \subset E_{insep}$ is purely inseparable and $E_{insep} \subset E$
is Galois,
\item $E = E_{sep} \otimes_F E_{insep}$.
\end{enumerate}
\end{lemma}

\begin{proof}
We found the subfield $E_{sep}$ in Lemma \ref{lemma-separable-first}.
We set $E_{insep} = E^{\text{Aut}(E/F)}$. Details omitted.
\end{proof}









\section{Review}
```

```tex
\label{lemma-normal-case}
Soit $E/F$ une extension algébrique normale de corps. Il existe des extensions intermédiaires
$E / E_{sep} /F$ et $E / E_{insep} / F$ telles que
\begin{enumerate}
\item $F \subset E_{sep}$ soit galoisienne et $E_{sep} \subset E$
soit purement inséparable,
\item $F \subset E_{insep}$ soit purement inséparable et $E_{insep} \subset E$
soit galoisienne,
\item $E = E_{sep} \otimes_F E_{insep}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Nous avons trouvé le sous-corps $E_{sep}$ dans le Lemme \ref{lemma-separable-first}.
Nous posons $E_{insep} = E^{\text{Aut}(E/F)}$. Les détails sont omis.
\end{proof}









\section{Rappels}
```

</details>

### FR-FIELDS-B7-PROSE-0019

`section-algebraic` — source 3692–3722, français 3685–3715.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3692) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Rappels est le titre idiomatique d'un résumé, non un nouveau contenu. Toutes les alternatives sur alpha, le polynôme minimal unitaire et sa caractérisation, les racines distinctes et le cas de dérivée nulle sont conservées. Seul le nom polynôme est rétabli après Le dans le deuxième sous-cas. La plus grande puissance q, et non une puissance arbitraire, reste celle qui donne un élément séparable.

Choix écartés :

- Supprimer seulement Le : formulation également fidèle, mais moins parallèle au sous-cas précédent.
- La dérivée : formulation possible ; conserver Le polynôme maintient le parallélisme immédiat sans autre réécriture.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-algebraic}

\noindent
In this section we give a quick review of what has transpired above.

\medskip\noindent
Let $K/k$ be a field extension. Let $\alpha \in K$. Then we have the
following possibilities:
\begin{enumerate}
\item The element $\alpha$ is transcendental over $k$.
\item The element $\alpha$ is algebraic over $k$. Denote
$P(T) \in k[T]$ its {\it minimal polynomial}. This is a monic polynomial
$P(T) = T^d + a_1 T^{d - 1} + \ldots + a_d$ with coefficients in
$k$. It is irreducible and $P(\alpha) = 0$. These properties
uniquely determine $P$, and the integer $d$ is called the
{\it degree of $\alpha$ over $k$}. There are two subcases:
\begin{enumerate}
\item The polynomial $\text{d}P/\text{d}T$ is not identically zero.
This is equivalent to the condition that
$P(T) = \prod_{i = 1, \ldots, d} (T - \alpha_i)$ for
pairwise distinct elements $\alpha_1, \ldots, \alpha_d$
in the algebraic closure of $k$.
In this case we say that $\alpha$ is {\it separable} over $k$.
\item The $\text{d}P/\text{d}T$ is identically zero. In this case the
characteristic $p$ of $k$ is $ > 0$, and $P$ is actually a polynomial
in $T^p$. Clearly there exists a largest power $q = p^e$ such that $P$ is
a polynomial in $T^q$. Then the element $\alpha^q$ is separable over $k$.
\end{enumerate}
\end{enumerate}

\begin{definition}
```

```tex
\label{section-algebraic}

\noindent
Dans cette section, nous récapitulons brièvement les résultats obtenus ci-dessus.

\medskip\noindent
Soit $K/k$ une extension de corps. Soit $\alpha \in K$. Les
possibilités suivantes se présentent :
\begin{enumerate}
\item L'élément $\alpha$ est transcendant sur $k$.
\item L'élément $\alpha$ est algébrique sur $k$. Notons
$P(T) \in k[T]$ son {\it polynôme minimal}. C'est un polynôme unitaire
$P(T) = T^d + a_1 T^{d - 1} + \ldots + a_d$ à coefficients dans
$k$. Il est irréductible et $P(\alpha) = 0$. Ces propriétés
déterminent $P$ de manière unique, et l'entier $d$ est appelé le
{\it degré de $\alpha$ sur $k$}. Il existe deux sous-cas :
\begin{enumerate}
\item Le polynôme $\text{d}P/\text{d}T$ n'est pas identiquement nul.
Cela équivaut à la condition
$P(T) = \prod_{i = 1, \ldots, d} (T - \alpha_i)$ pour des
éléments deux à deux distincts $\alpha_1, \ldots, \alpha_d$
de la clôture algébrique de $k$.
Dans ce cas, nous disons que $\alpha$ est {\it séparable} sur $k$.
\item Le polynôme $\text{d}P/\text{d}T$ est identiquement nul. Dans ce cas, la
caractéristique $p$ de $k$ est $ > 0$, et $P$ est en fait un polynôme
en $T^p$. Il existe manifestement une plus grande puissance $q = p^e$ telle que $P$ soit
un polynôme en $T^q$. Alors l'élément $\alpha^q$ est séparable sur $k$.
\end{enumerate}
\end{enumerate}

\begin{definition}
```

</details>

### FR-FIELDS-B7-PROSE-0020

`definition-separable-algebraic` — source 3723–3746, français 3716–3739.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3723) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Les cinq définitions récapitulatives conservent leurs quantificateurs : tout élément, toute racine et toutes les conditions de décomposition. La pure inséparabilité exige ici explicitement la caractéristique positive comme dans le témoin ; cette convention n'est pas harmonisée avec une autre définition au prix d'une modification silencieuse. Galois conserve les deux conditions, normale et séparable.

**Réserve :** Le traitement de l'extension identité en caractéristique zéro n'est pas harmonisé ici : la formulation positive de ce rappel appartient à la source officielle.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-separable-algebraic}
Algebraic field extensions.
\begin{enumerate}
\item A field extension $K/k$ is called {\it algebraic}
if every element of $K$ is algebraic over $k$.
\item An algebraic extension $k'/k$ is called {\it separable}
if every $\alpha \in k'$ is separable over $k$.
\item An algebraic
extension $k'/k$ is called {\it purely inseparable} if
the characteristic of $k$ is $p > 0$ and for every element
$\alpha \in k'$ there exists a power $q$ of $p$ such that
$\alpha^q \in k$.
\item An algebraic extension $k'/k$ is called {\it normal}
if for every $\alpha \in k'$ the minimal polynomial $P(T) \in k[T]$
of $\alpha$ over $k$ splits completely into linear factors over $k'$.
\item An algebraic extension $k'/k$ is called {\it Galois}
if it is separable and normal.
\end{enumerate}
\end{definition}

\noindent
The following lemma does not seem to fit anywhere else.

\begin{lemma}
```

```tex
\label{definition-separable-algebraic}
Extensions algébriques de corps.
\begin{enumerate}
\item Une extension de corps $K/k$ est dite {\it algébrique}
si tout élément de $K$ est algébrique sur $k$.
\item Une extension algébrique $k'/k$ est dite {\it séparable}
si tout $\alpha \in k'$ est séparable sur $k$.
\item Une extension algébrique
$k'/k$ est dite {\it purement inséparable} si
la caractéristique de $k$ est $p > 0$ et si, pour tout élément
$\alpha \in k'$, il existe une puissance $q$ de $p$ telle que
$\alpha^q \in k$.
\item Une extension algébrique $k'/k$ est dite {\it normale}
si, pour tout $\alpha \in k'$, le polynôme minimal $P(T) \in k[T]$
de $\alpha$ sur $k$ se décompose entièrement en facteurs linéaires sur $k'$.
\item Une extension algébrique $k'/k$ est dite {\it galoisienne}
si elle est séparable et normale.
\end{enumerate}
\end{definition}

\noindent
Le lemme suivant ne semble trouver sa place nulle part ailleurs.

\begin{lemma}
```

</details>

### FR-FIELDS-B7-PROSE-0021

`lemma-pth-root` — source 3747–3792, français 3740–3784.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3747) · [Français de travail](staged/fr/009_fields.prose-batch7.fr.tex)

Les deux conclusions concernent une puissance p-ième dans L. Dans la généralisation, les trois conditions (a), (b), (c) sont intactes. La preuve garde (2) implique (1), les coefficients a_i=b_i^p, les racines de Q, l'irréductibilité de T^p-alpha, la racine commune, la divisibilité et la contradiction avec les racines distinctes. Premiers entre eux désigne les polynômes, non la primalité d'un seul élément. Le renvoi, l'entrée des chapitres, la bibliographie, son style et la fin du document sont conservés jusqu'au dernier octet significatif.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-pth-root}
Let $K$ be a field of characteristic $p > 0$. Let $L/K$ be a separable
algebraic extension. Let $\alpha \in L$.
\begin{enumerate}
\item If the coefficients of the minimal polynomial of $\alpha$
over $K$ are $p$th powers in $K$ then $\alpha$ is a $p$th
power in $L$.
\item More generally, if $P \in K[T]$ is a polynomial such that (a) $\alpha$
is a root of $P$, (b) $P$ has pairwise distinct roots in an algebraic closure,
and (c) all coefficients of $P$ are $p$th powers, then $\alpha$ is a
$p$th power in $L$.
\end{enumerate}
\end{lemma}

\begin{proof}
It follows from the definitions that (2) implies (1). Assume $P$ is as in (2).
Write $P(T) = \sum\nolimits_{i = 0}^d a_i T^{d - i}$ and $a_i = b_i^p$.
The polynomial $Q(T) = \sum\nolimits_{i = 0}^d b_i T^{d - i}$ has distinct
roots in an algebraic closure as well, because the roots of $Q$
are the $p$th roots of the roots of $P$. If $\alpha$ is not a $p$th power,
then $T^p - \alpha$ is an irreducible polynomial over $L$
(Lemma \ref{lemma-take-pth-root}).
Moreover $Q$ and $T^p - \alpha$ have a root in common in
an algebraic closure $\overline{L}$.
Thus $Q$ and $T^p - \alpha$ are not relatively prime, which
implies $T^p - \alpha | Q$ in $L[T]$. This contradicts the fact that
the roots of $Q$ are pairwise distinct.
\end{proof}












\input{chapters}

\bibliography{my}
\bibliographystyle{amsalpha}

\end{document}
```

```tex
\label{lemma-pth-root}
Soit $K$ un corps de caractéristique $p > 0$. Soit $L/K$ une extension
algébrique séparable. Soit $\alpha \in L$.
\begin{enumerate}
\item Si les coefficients du polynôme minimal de $\alpha$
sur $K$ sont des puissances $p$-ièmes dans $K$, alors $\alpha$ est une puissance
$p$-ième dans $L$.
\item Plus généralement, si $P \in K[T]$ est un polynôme tel que (a) $\alpha$
soit une racine de $P$, (b) $P$ possède des racines deux à deux distinctes dans une clôture algébrique,
et (c) tous les coefficients de $P$ soient des puissances $p$-ièmes, alors $\alpha$ est une
puissance $p$-ième dans $L$.
\end{enumerate}
\end{lemma}

\begin{proof}
Il résulte des définitions que (2) implique (1). Supposons que $P$ satisfasse aux hypothèses de (2).
Écrivons $P(T) = \sum\nolimits_{i = 0}^d a_i T^{d - i}$ et $a_i = b_i^p$.
Le polynôme $Q(T) = \sum\nolimits_{i = 0}^d b_i T^{d - i}$ possède lui aussi des
racines distinctes dans une clôture algébrique, car les racines de $Q$
sont les racines $p$-ièmes des racines de $P$. Si $\alpha$ n'est pas une puissance $p$-ième,
alors $T^p - \alpha$ est un polynôme irréductible sur $L$
(Lemme \ref{lemma-take-pth-root}).
De plus, $Q$ et $T^p - \alpha$ ont une racine commune dans
une clôture algébrique $\overline{L}$.
Ainsi $Q$ et $T^p - \alpha$ ne sont pas premiers entre eux, ce qui
implique que $T^p - \alpha | Q$ dans $L[T]$. Cela contredit le fait que
les racines de $Q$ sont deux à deux distinctes.
\end{proof}











\input{chapters}

\bibliography{my}
\bibliographystyle{amsalpha}

\end{document}
```

</details>

## Limites et suite

Travail assisté par OpenAI Codex. Le modèle exact et son effort ne sont pas attestés par ces pièces locales et ne sont pas inventés. Aucune construction PDF ni publication nouvelle n'est revendiquée. Le contrôle intégral de fidélité de ce chapitre ne s'étend pas automatiquement aux autres chapitres.

Préserver les témoins et les sept dossiers. Poursuivre la réconciliation de l'édition française, puis reconstruire et contrôler le rendu, publier le PDF avec son LaTeX direct et son archive source complète dans la lignée existante, et vérifier les octets publics. L'ancienne édition éditorialisée reste conservée comme matériau possible pour une traduction distincte d'une révision déterminée de l'anglais AI-intégré.
