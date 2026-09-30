# Chapitre 9 — Corps : normalité, décomposition et éléments primitifs

**Cinq sections complètes comparées, lignes source 1813–2358. Un accord grammatical réparé ; aucune nouvelle correction mathématique de la source. Lecture continue cumulée : dix-neuf sections, pas le chapitre entier.**

[LaTeX de travail](staged/fr/009_fields.prose-batch4.fr.tex) · [Validation](FIELDS_PROSE_BATCH4_VALIDATION.json) · [Choix et paires](FIELDS_PROSE_BATCH4_CHOICES.json) · [Occurrences](FIELDS_PROSE_BATCH4_OCCURRENCES.json) · [Lot précédent](FIELDS_PROSE_BATCH3_REVIEW.fr.md)

## Étendue effective

Les 24 paires partitionnent exactement les cinq sections, avec tous leurs énoncés, preuves, définitions, slogan et transitions. L'égalité mathématique brute est fausse pour un seul texte lecteur traduit : for some / pour un certain. Les 455 régions mathématiques sont en égalité ordonnée après cette seule exception exacte. Le préfixe cumulé conserve les trois exceptions déjà justifiées au lot 3.

Le nouveau fichier ne diffère de la copie antérieure que par l'accord normal / il après le corps M'. Les préfixe et suffixe hors lot restent identiques. Le retour inverse de cette réparation, puis de la première réparation de prose et des 19 restaurations historiques retrouve exactement les octets publics antérieurs.

## Réparation effectivement appliquée

Le nombre de facteurs tensoriels reste le degré séparable, borné par le degré total. Toutes les images sigma_i(L), le fait que la sous-algèbre algébrique est un corps, la permutation des plongements, la minimalité et la formule du morphisme surjectif restent exacts. Une seule phrase est réparée : après le corps M', normale / elle devient normal / il. L'accord est attesté en 2.2.1–2.2.2 du canon et ne change ni objet ni hypothèse.

[Opération réversible](FIELDS_PROSE_BATCH4_REPAIR.json)

Avant :

```tex
que $M'$ est normale sur $K$ et qu'elle est la
```

Après :

```tex
que $M'$ est normal sur $K$ et qu'il est la
```

## Canon effectivement consulté

Marc Reversat et Benoît Zhang, [Cours de théorie des corps](https://www.math.univ-toulouse.fr/~reversat/galois.pdf), 24 mars 2003. §§2.1–2.3 complets, pages imprimées 19–23 (PDF 27–31), plus les exercices de la page 24 ; §3.6 complet, pages 37–39 (PDF 45–47) ; 5.1.1–5.1.6 et leurs preuves, pages 59–60 (PDF 67–68) ; §5.2, introduction, 5.2.1–5.2.3 et leurs preuves, pages 62–63 (PDF 70–71). Les pages imprimées 21 et 37 ont aussi été rendues et inspectées. Le corollaire 5.2.4 est visible mais sa preuve n'est pas invoquée.

PDF : 816199 octets / SHA-256 `73A1D0DCD0B7F11625293615E693B198C0C33BAE3A57C78A705153CE33942E8A`. [Attestations, limites et règles](FIELDS_PROSE_BATCH4_CONSULTED_CANON.json). Consultation rétrospective : aucune consultation du traducteur initial n'est inventée.

Le cours comporte ses propres coquilles : numéros (vi)/(iii), sigma au lieu de son prolongement dans la preuve 2.1.4, base L au lieu de K dans le raisonnement 2.3.1, et condition impossible pour le plongement identité dans la remarque 3.6.4. Elles ne sont pas copiées. Scindé et la variante clôture normale ne sont pas présentés comme des citations lexicales exactes de ces pages. Les accords elliptiques et la syntaxe courante restent motivés par les passages comparés. Aucune lecture de tout le cours ni validation humaine n'est revendiquée.

## Points à examiner, sans attente de validation humaine

Les réserves suivantes distinguent les ambiguïtés de l'anglais et les choix de français. Elles ne constituent ni des corrections cachées, ni des errata admis automatiquement. Les variantes non attestées sont identifiées plutôt que dotées d'une citation fabriquée.

- `definition-normal` : Dans plusieurs phrases, une lettre de corps reprend elliptiquement l'extension et reçoit un accord féminin. Ce n'est pas une modification de la définition. La réparation isolée ci-dessous vise un antécédent explicite le corps, non un remplacement automatique de tous les accords du chapitre.
- `lemma-intersect-normal` : La source ne dit pas I non vide. Avec la convention intersection vide dans M, la conclusion demanderait M/F normale. Réserve de cas limite, non nouvelle hypothèse ajoutée au texte et non admission automatique d'un erratum.
- `lemma-normal-closure` : L'énoncé dit unique, mais sans fixer une clôture ambiante la preuve donne un isomorphisme. Cette réserve officielle est conservée hors traduction ; le canon précise l'ambiance, mais ne remplace pas la formulation de Stacks.
- `definition-normal-closure` : Fermeture normale est lexicalement attesté dans les pages consultées ; clôture normale est maintenu comme variante cohérente et définie par le même objet. Ne pas prétendre disposer ici d'une citation exacte pour cette variante.
- `lemma-normal-closure-inside-normal` : La preuve de (2) conclut explicitement la normalité, laissant la finitude suivre implicitement du nombre fini de racines. Le français n'ajoute pas une démonstration absente.
- `lemma-cyclic` : La preuve écrit e_1 et conclut r=1, sans séparer le cas A trivial (r=0). La conclusion est vraie dans ce cas, mais l'omission de preuve est celle du texte officiel ; elle n'est pas comblée clandestinement.
- `lemma-primitive-element` : La parenthèse sur une réunion finie de sous-espaces suppose le corps infini du paragraphe. Le dernier paragraphe réutilise cet argument ; le cas fini est déjà traité. Ne pas lire cette phrase isolément comme une assertion valable sur tout corps.

## Exception dans une formule

Pour un certain traduit for some, au même emplacement et pour le même polynôme P. Aucun symbole mathématique n'est modifié.

[Expressions intégrales et indices exacts](FIELDS_PROSE_BATCH4_MATH_EXCEPTIONS.json)

```tex
T = \{\beta \in \overline{F} \mid P(\beta) = 0\text{ for some }P \in \mathcal{P}\}
```

```tex
T = \{\beta \in \overline{F} \mid P(\beta) = 0\text{ pour un certain }P \in \mathcal{P}\}
```

## Règles et occurrences

### normality

Conserver base et algébricité ; distinguer corps normal et extension normale. Un adjectif elliptique ne modifie pas l'objet mathématique.

Occurrences vérifiées : 43. Appui : 2.2.1–2.2.2, p.21.

### splitting

Corps de décomposition et la factorisation sont attestés ; scindé n'est pas attesté lexicalement dans ces pages mais désigne ici cette même factorisation explicite.

Occurrences vérifiées : 13. Appui : 2.1.1–2.1.4, pp.19–21.

### normal-closure

Objet attesté sous fermeture normale ; variante conservée et explicitement définie, sans fabriquer une citation exacte.

Occurrences vérifiées : 7. Appui : 2.3.1–2.3.3, pp.22–23.

### embeddings-automorphisms

Contrôler source, cible et corps fixé ; un prolongement n'est pas déclaré unique s'il ne l'est pas dans la source.

Occurrences vérifiées : 20. Appui : 2.1.3–2.2.4, pp.20–22.

### roots-unity-cyclicity

Même groupe multiplicatif et mêmes ordres ; ne pas assimiler générateur de corps et générateur du groupe des unités.

Occurrences vérifiées : 6. Appui : 5.1.1–5.1.4, pp.59–60.

### finite-prime-fields

Corps fini concerne le cardinal, extension finie le degré. Corps premier désigne ici le sous-corps premier.

Occurrences vérifiées : 7. Appui : 5.2.1, pp.62–63.

### primitive-elements

Générateur de l'extension E/F, sans exigence de génération du groupe multiplicatif.

Occurrences vérifiées : 7. Appui : 3.6.1–3.6.3, pp.37–39.

### monic-factors

Coefficient dominant un ; ne pas confondre unitaire et unité du corps ou anneau de polynômes.

Occurrences vérifiées : 1. Appui : Exercice 2.7, p.24 ; 5.1.6, p.60.

## Toutes les paires lues

### FR-FIELDS-B4-PROSE-0001

`frontmatter` — source 1813–1813, français 1813–1813.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1813) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Le titre conserve les extensions normales, sans introduire la séparabilité ni la finitude.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\section{Normal extensions}
```

```tex
\section{Extensions normales}
```

</details>

### FR-FIELDS-B4-PROSE-0002

`section-normal` — source 1814–1826, français 1814–1826.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1814) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

La décomposition complète conserve le facteur constant non nul, n au moins un et toutes les racines dans le corps indiqué. Le cours français décrit la même décomposition en polynômes du premier degré. Scindé, employé plus loin, est le raccourci défini par cette factorisation ; aucune hypothèse de racines distinctes n'est ajoutée.

Choix écartés :

- Remplacer partout complètement décomposé par scindé : non nécessaire à la fidélité, les deux formulations renvoient ici à la factorisation explicitée ; pas d'attestation lexicale exacte de scindé revendiquée dans les pages retenues.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-normal}

\noindent
Let $P \in F[x]$ be a nonconstant polynomial over a field $F$. We say $P$
{\it splits completely into linear factors over $F$} or
{\it splits completely over $F$} if there exist
$c \in F^*$, $n \geq 1$, $\alpha_1, \ldots, \alpha_n \in F$ such that
$$
P = c(x - \alpha_1) \ldots (x - \alpha_n)
$$
in $F[x]$. Normal extensions are defined as follows.

\begin{definition}
```

```tex
\label{section-normal}

\noindent
Soit $P \in F[x]$ un polynôme non constant sur un corps $F$. Nous dirons que $P$
{\it se décompose complètement en facteurs linéaires sur $F$} ou
{\it est complètement décomposé sur $F$} s'il existe
$c \in F^*$, $n \geq 1$, $\alpha_1, \ldots, \alpha_n \in F$ tels que
$$
P = c(x - \alpha_1) \ldots (x - \alpha_n)
$$
dans $F[x]$. Les extensions normales sont définies comme suit.

\begin{definition}
```

</details>

### FR-FIELDS-B4-PROSE-0003

`definition-normal` — source 1827–1837, français 1827–1837.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1827) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

La normalité porte sur une extension algébrique et sur le polynôme minimal de chaque élément. La base du polynôme reste F et le corps de décomposition E. Normale s'accorde ici par ellipse avec extension ; ce choix de syntaxe est distingué de l'accord explicite avec le corps réparé plus loin. Le canon distingue également extension normale et corps normal.

**Réserve :** Dans plusieurs phrases, une lettre de corps reprend elliptiquement l'extension et reçoit un accord féminin. Ce n'est pas une modification de la définition. La réparation isolée ci-dessous vise un antécédent explicite le corps, non un remplacement automatique de tous les accords du chapitre.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-normal}
Let $E/F$ be an algebraic field extension. We say $E$ is {\it normal}
over $F$ if for all $\alpha \in E$ the minimal polynomial $P$
of $\alpha$ over $F$ splits completely into linear factors over $E$.
\end{definition}

\noindent
As in the case of separable extensions, it takes a bit of work to establish
the basic properties of this notion.

\begin{lemma}
```

```tex
\label{definition-normal}
Soit $E/F$ une extension algébrique de corps. Nous dirons que $E$ est {\it normale}
sur $F$ si, pour tout $\alpha \in E$, le polynôme minimal $P$
de $\alpha$ sur $F$ se décompose complètement en facteurs linéaires sur $E$.
\end{definition}

\noindent
Comme pour les extensions séparables, l'établissement des propriétés
fondamentales de cette notion demande un peu de travail.

\begin{lemma}
```

</details>

### FR-FIELDS-B4-PROSE-0004

`lemma-normal-goes-up` — source 1838–1850, français 1838–1850.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1838) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Les trois corps K/E/F restent algébriques. La normalité de K sur F entraîne celle de K sur E, non une transitivité de la normalité. La preuve conserve les deux polynômes minimaux, leur divisibilité dans E[x] et la décomposition de Q. Aucun contre-exemple ou argument du canon n'est ajouté au texte source.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-normal-goes-up}
Let $K/E/F$ be a tower of algebraic field extensions.
If $K$ is normal over $F$, then $K$ is normal over $E$.
\end{lemma}

\begin{proof}
Let $\alpha \in K$. Let $P$ be the minimal polynomial of $\alpha$ over $F$.
Let $Q$ be the minimal polynomial of $\alpha$ over $E$.
Then $Q$ divides $P$ in the polynomial ring $E[x]$, say $P = QR$.
Hence, if $P$ splits completely over $K$, then so does $Q$.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-normal-goes-up}
Soit $K/E/F$ une tour d'extensions algébriques de corps.
Si $K$ est normale sur $F$, alors $K$ est normale sur $E$.
\end{lemma}

\begin{proof}
Soit $\alpha \in K$. Soit $P$ le polynôme minimal de $\alpha$ sur $F$.
Soit $Q$ le polynôme minimal de $\alpha$ sur $E$.
Alors $Q$ divise $P$ dans l'anneau de polynômes $E[x]$, disons $P = QR$.
Par conséquent, si $P$ est complètement décomposé sur $K$, il en va de même de $Q$.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B4-PROSE-0005

`lemma-intersect-normal` — source 1851–1861, français 1851–1861.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1851) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

L'intersection des mêmes sous-extensions normales et la preuve immédiatement déduite des définitions sont conservées. On n'ajoute pas silencieusement une hypothèse de famille non vide ; le cas vide est signalé comme réserve sur la source.

**Réserve :** La source ne dit pas I non vide. Avec la convention intersection vide dans M, la conclusion demanderait M/F normale. Réserve de cas limite, non nouvelle hypothèse ajoutée au texte et non admission automatique d'un erratum.

Choix écartés :

- Ajouter I non vide : correction de l'énoncé source, donc non intégrée dans cette édition de référence.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-intersect-normal}
Let $F$ be a field. Let $M/F$ be an algebraic extension. Let
$M/E_i/F$, $i \in I$ be subextensions with
$E_i/F$ normal. Then $\bigcap E_i$ is normal over $F$.
\end{lemma}

\begin{proof}
Direct from the definitions.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-intersect-normal}
Soit $F$ un corps. Soit $M/F$ une extension algébrique. Soient
$M/E_i/F$, $i \in I$, des sous-extensions telles que
$E_i/F$ soit normale. Alors $\bigcap E_i$ est normale sur $F$.
\end{lemma}

\begin{proof}
Cela résulte directement des définitions.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B4-PROSE-0006

`lemma-separable-first-normal` — source 1862–1878, français 1862–1878.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1862) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

La sous-extension séparable déjà définie, les cas de caractéristique zéro et positive, la factorisation de P et la séparabilité de chacune de ses racines sont maintenus. La preuve française ne remplace pas la brièveté du texte anglais par un développement des deux étages de la tour.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-separable-first-normal}
Let $E/F$ be a normal algebraic field extension. Then the subextension
$E/E_{sep}/F$ of Lemma \ref{lemma-separable-first} is normal.
\end{lemma}

\begin{proof}
If the characteristic is zero, then $E_{sep} = E$, and the result
is clear. If the characteristic is $p > 0$, then $E_{sep}$
is the set of elements of $E$ which are separable over $F$.
Then if $\alpha \in E_{sep}$ has minimal polynomial $P$
write $P = c(x - \alpha)(x - \alpha_2) \ldots (x - \alpha_d)$
with $\alpha_2, \ldots, \alpha_d \in E$. Since
$P$ is a separable polynomial and since $\alpha_i$
is a root of $P$, we conclude $\alpha_i \in E_{sep}$ as desired.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-separable-first-normal}
Soit $E/F$ une extension algébrique de corps normale. Alors la sous-extension
$E/E_{sep}/F$ du Lemme \ref{lemma-separable-first} est normale.
\end{lemma}

\begin{proof}
Si la caractéristique est nulle, alors $E_{sep} = E$, et le résultat
est clair. Si la caractéristique vaut $p > 0$, alors $E_{sep}$
est l'ensemble des éléments de $E$ qui sont séparables sur $F$.
Alors, si $\alpha \in E_{sep}$ a pour polynôme minimal $P$,
écrivons $P = c(x - \alpha)(x - \alpha_2) \ldots (x - \alpha_d)$
avec $\alpha_2, \ldots, \alpha_d \in E$. Puisque
$P$ est un polynôme séparable et que $\alpha_i$
est une racine de $P$, nous en déduisons $\alpha_i \in E_{sep}$, comme voulu.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B4-PROSE-0007

`lemma-characterize-normal` — source 1879–1921, français 1879–1921.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1879) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

L'équivalence concerne les images de tous les F-plongements dans une clôture algébrique, non l'égalité des plongements eux-mêmes. Tous les éléments de T, les deux sens de la preuve, le prolongement de sigma_0 et le retour des racines par sigma sont conservés. Pour un certain traduit exactement for some dans la formule, sans toucher au quantificateur ni à l'ensemble de polynômes.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-characterize-normal}
Let $E/F$ be an algebraic extension of fields. Let $\overline{F}$ be an
algebraic closure of $F$. The following are equivalent
\begin{enumerate}
\item $E$ is normal over $F$, and
\item for every pair $\sigma, \sigma' \in \Mor_F(E, \overline{F})$ we
have $\sigma(E) = \sigma'(E)$.
\end{enumerate}
\end{lemma}

\begin{proof}
Let $\mathcal{P}$ be the set of all minimal polynomials over $F$ of
all elements of $E$. Set
$$
T =
\{\beta \in \overline{F} \mid P(\beta) = 0\text{ for some }P \in \mathcal{P}\}
$$
It is clear that if $E$ is normal over $F$, then $\sigma(E) = T$
for all $\sigma \in \Mor_F(E, \overline{F})$. Thus we see that (1)
implies (2).

\medskip\noindent
Conversely, assume (2). Pick $\beta \in T$.
We can find a corresponding $\alpha \in E$ whose minimal polynomial
$P \in \mathcal{P}$ annihilates $\beta$. Because $F(\alpha) = F[x]/(P)$
we can find an element $\sigma_0 \in \Mor_F(F(\alpha), \overline{F})$ mapping
$\alpha$ to $\beta$. By Lemma \ref{lemma-map-into-algebraic-closure}
we can extend $\sigma_0$ to a $\sigma \in \Mor_F(E, \overline{F})$.
Whence we see that $\beta$ is in the common image of all embeddings
$\sigma : E \to \overline{F}$. It follows that $\sigma(E) = T$
for any $\sigma$. Fix a $\sigma$. Now let $P \in \mathcal{P}$. Then we
can write
$$
P = (x - \beta_1) \ldots (x - \beta_n)
$$
for some $n$ and $\beta_i \in \overline{F}$ by
Lemma \ref{lemma-algebraically-closed}. Observe that $\beta_i \in T$.
Thus $\beta_i = \sigma(\alpha_i)$ for some $\alpha_i \in E$. Thus
$P = (x - \alpha_1) \ldots (x - \alpha_n)$ splits completely over $E$.
This finishes the proof.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-characterize-normal}
Soit $E/F$ une extension algébrique de corps. Soit $\overline{F}$ une
clôture algébrique de $F$. Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item $E$ est normale sur $F$ ;
\item pour toute paire $\sigma, \sigma' \in \Mor_F(E, \overline{F})$, on
a $\sigma(E) = \sigma'(E)$.
\end{enumerate}
\end{lemma}

\begin{proof}
Soit $\mathcal{P}$ l'ensemble de tous les polynômes minimaux sur $F$
de tous les éléments de $E$. Posons
$$
T =
\{\beta \in \overline{F} \mid P(\beta) = 0\text{ pour un certain }P \in \mathcal{P}\}
$$
Il est clair que, si $E$ est normale sur $F$, alors $\sigma(E) = T$
pour tout $\sigma \in \Mor_F(E, \overline{F})$. Nous voyons donc que (1)
implique (2).

\medskip\noindent
Réciproquement, supposons (2). Choisissons $\beta \in T$.
Nous pouvons trouver $\alpha \in E$ dont le polynôme minimal
$P \in \mathcal{P}$ annule $\beta$. Puisque $F(\alpha) = F[x]/(P)$,
nous pouvons trouver un élément $\sigma_0 \in \Mor_F(F(\alpha), \overline{F})$ qui envoie
$\alpha$ sur $\beta$. D'après le Lemme \ref{lemma-map-into-algebraic-closure},
nous pouvons prolonger $\sigma_0$ en un morphisme $\sigma \in \Mor_F(E, \overline{F})$.
Nous voyons ainsi que $\beta$ appartient à l'image commune de tous les plongements
$\sigma : E \to \overline{F}$. Il s'ensuit que $\sigma(E) = T$
pour tout $\sigma$. Fixons un $\sigma$. Soit maintenant $P \in \mathcal{P}$. Alors nous
pouvons écrire
$$
P = (x - \beta_1) \ldots (x - \beta_n)
$$
pour un certain $n$ et des $\beta_i \in \overline{F}$, d'après le
Lemme \ref{lemma-algebraically-closed}. Observons que $\beta_i \in T$.
Ainsi $\beta_i = \sigma(\alpha_i)$ pour un certain $\alpha_i \in E$. Par conséquent,
$P = (x - \alpha_1) \ldots (x - \alpha_n)$ se décompose complètement sur $E$.
Cela achève la démonstration.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B4-PROSE-0008

`lemma-normally-generated` — source 1922–1945, français 1922–1945.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1922) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

La famille de générateurs peut être infinie. Toutes les racines de chaque polynôme minimal, l'égalité des deux ensembles images et la conclusion sur le corps engendré sont présentes. Une permutation finie globale des générateurs ou une hypothèse de finitude ne sont pas introduites.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-normally-generated}
Let $E/F$ be an algebraic extension of fields.
If $E$ is generated by $\alpha_i \in E$, $i \in I$
over $F$ and if for each $i$ the minimal polynomial
of $\alpha_i$ over $F$ splits completely in $E$, then
$E/F$ is normal.
\end{lemma}

\begin{proof}
Let $P_i$ be the minimal polynomial of $\alpha_i$ over $F$.
Let $\alpha_i = \alpha_{i, 1}, \alpha_{i, 2}, \ldots, \alpha_{i, d_i}$
be the roots of $P_i$ over $E$. Given two embeddings
$\sigma, \sigma' : E \to \overline{F}$ over $F$ we see that
$$
\{\sigma(\alpha_{i, 1}), \ldots, \sigma(\alpha_{i, d_i})\} =
\{\sigma'(\alpha_{i, 1}), \ldots, \sigma'(\alpha_{i, d_i})\}
$$
because both sides are equal to the set of roots of $P_i$
in $\overline{F}$. The elements $\alpha_{i, j}$
generate $E$ over $F$ and we find that $\sigma(E) = \sigma'(E)$.
Hence $E/F$ is normal by Lemma \ref{lemma-characterize-normal}.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-normally-generated}
Soit $E/F$ une extension algébrique de corps.
Si $E$ est engendrée par les éléments $\alpha_i \in E$, $i \in I$,
sur $F$, et si, pour tout $i$, le polynôme minimal
de $\alpha_i$ sur $F$ se décompose complètement dans $E$, alors
$E/F$ est normale.
\end{lemma}

\begin{proof}
Soit $P_i$ le polynôme minimal de $\alpha_i$ sur $F$.
Soient $\alpha_i = \alpha_{i, 1}, \alpha_{i, 2}, \ldots, \alpha_{i, d_i}$
les racines de $P_i$ sur $E$. Étant donnés deux plongements
$\sigma, \sigma' : E \to \overline{F}$ au-dessus de $F$, on voit que
$$
\{\sigma(\alpha_{i, 1}), \ldots, \sigma(\alpha_{i, d_i})\} =
\{\sigma'(\alpha_{i, 1}), \ldots, \sigma'(\alpha_{i, d_i})\}
$$
car les deux membres sont égaux à l'ensemble des racines de $P_i$
dans $\overline{F}$. Les éléments $\alpha_{i, j}$
engendrent $E$ sur $F$, et l'on obtient $\sigma(E) = \sigma'(E)$.
Ainsi $E/F$ est normale d'après le Lemme \ref{lemma-characterize-normal}.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B4-PROSE-0009

`lemma-lift-maps` — source 1946–1981, français 1946–1981.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1946) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Les deux hypothèses de normalité ne sont pas interverties : M/K permet la restriction, L/K le prolongement. Le diagramme, les corps cibles et les deux usages de la caractérisation de la normalité restent exacts. Se prolonge ne signifie pas se prolonge de façon unique. Application reprend le mot map dans une catégorie explicitement fixée.

Choix écartés :

- Ajouter l'unicité du prolongement : rejeté, car ni la source ni la preuve ne l'affirment.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-lift-maps}
Let $L/M/K$ be a tower of algebraic extensions.
\begin{enumerate}
\item If $M/K$ is normal, then any automorphism $\tau$ of $L/K$
induces an automorphism $\tau|_M : M \to M$.
\item If $L/K$ is normal, then any $K$-algebra map $\sigma : M \to L$
extends to an automorphism of $L$.
\end{enumerate}
\end{lemma}

\begin{proof}
Choose an algebraic closure $\overline{L}$ of $L$
(Theorem \ref{theorem-existence-algebraic-closure}).

\medskip\noindent
Let $\tau$ be as in (1). Then $\tau(M) = M$ as subfields of $\overline{L}$
by Lemma \ref{lemma-characterize-normal} and hence
$\tau|_M : M \to M$ is an automorphism.

\medskip\noindent
Let $\sigma : M \to L$ be as in (2).
By Lemma \ref{lemma-map-into-algebraic-closure}
we can extend $\sigma$ to a map
$\tau : L \to \overline{L}$, i.e., such that
$$
\xymatrix{
L \ar[r]_\tau & \overline{L} \\
M \ar[u] \ar[ru]_\sigma & K \ar[l] \ar[u]
}
$$
is commutative. By Lemma \ref{lemma-characterize-normal} we see that
$\tau(L) = L$. Hence $\tau : L \to L$ is an automorphism which
extends $\sigma$.
\end{proof}

\begin{definition}
```

```tex
\label{lemma-lift-maps}
Soit $L/M/K$ une tour d'extensions algébriques.
\begin{enumerate}
\item Si $M/K$ est normale, alors tout automorphisme $\tau$ de $L/K$
induit un automorphisme $\tau|_M : M \to M$.
\item Si $L/K$ est normale, alors tout morphisme de $K$-algèbres $\sigma : M \to L$
se prolonge en un automorphisme de $L$.
\end{enumerate}
\end{lemma}

\begin{proof}
Choisissons une clôture algébrique $\overline{L}$ de $L$
(Théorème \ref{theorem-existence-algebraic-closure}).

\medskip\noindent
Soit $\tau$ comme en (1). Alors $\tau(M) = M$ comme sous-corps de $\overline{L}$
d'après le Lemme \ref{lemma-characterize-normal}, et donc
$\tau|_M : M \to M$ est un automorphisme.

\medskip\noindent
Soit $\sigma : M \to L$ comme en (2).
D'après le Lemme \ref{lemma-map-into-algebraic-closure},
nous pouvons prolonger $\sigma$ en une application
$\tau : L \to \overline{L}$, c'est-à-dire de telle sorte que le diagramme
$$
\xymatrix{
L \ar[r]_\tau & \overline{L} \\
M \ar[u] \ar[ru]_\sigma & K \ar[l] \ar[u]
}
$$
soit commutatif. D'après le Lemme \ref{lemma-characterize-normal}, on voit que
$\tau(L) = L$. Ainsi $\tau : L \to L$ est un automorphisme qui
prolonge $\sigma$.
\end{proof}

\begin{definition}
```

</details>

### FR-FIELDS-B4-PROSE-0010

`definition-automorphisms` — source 1982–1993, français 1982–1993.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1982) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Les deux notations du groupe et les deux noms des automorphismes sont conservés. Le groupe est celui de l'objet E dans la catégorie des F-extensions. Le cours emploie groupe de Galois pour une extension normale ; cette convention plus spécifique ne remplace pas la définition de Stacks.

Choix écartés :

- Remplacer Aut par Gal suivant la convention du cours : rejeté, car cela modifierait la notation officielle et son domaine.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-automorphisms}
Let $E/F$ be an extension of fields. Then $\text{Aut}(E/F)$ or
$\text{Aut}_F(E)$ denotes the automorphism group of $E$ as an object
of the category of $F$-extensions. Elements of $\text{Aut}(E/F)$
are called {\it automorphisms of $E$ over $F$} or
{\it automorphisms of $E/F$}.
\end{definition}

\noindent
Here is a characterization of normal extensions in terms of automorphisms.

\begin{lemma}
```

```tex
\label{definition-automorphisms}
Soit $E/F$ une extension de corps. Alors $\text{Aut}(E/F)$ ou
$\text{Aut}_F(E)$ désigne le groupe des automorphismes de $E$ comme objet
de la catégorie des $F$-extensions. Les éléments de $\text{Aut}(E/F)$
sont appelés {\it automorphismes de $E$ sur $F$} ou
{\it automorphismes de $E/F$}.
\end{definition}

\noindent
Voici une caractérisation des extensions normales en termes d'automorphismes.

\begin{lemma}
```

</details>

### FR-FIELDS-B4-PROSE-0011

`lemma-normal-and-automorphisms` — source 1994–2024, français 1994–2024.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1994) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

L'extension est finie et l'égalité concerne le degré séparable, pas nécessairement le degré total. L'injection par précomposition, son image commune, puis la surjection construite avec sigma_0 inverse composée avec sigma sont intégralement préservées. Le sens de la composition n'est pas inversé par le français.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-normal-and-automorphisms}
Let $E/F$ be a finite extension. We have
$$
|\text{Aut}(E/F)| \leq [E : F]_s
$$
with equality if and only if $E$ is normal over $F$.
\end{lemma}

\begin{proof}
Choose an algebraic closure $\overline{F}$ of $F$. Recall that
$[E : F]_s = |\Mor_F(E, \overline{F})|$. Pick an element
$\sigma_0 \in \Mor_F(E, \overline{F})$. Then the map
$$
\text{Aut}(E/F) \longrightarrow \Mor_F(E, \overline{F}),\quad
\tau \longmapsto \sigma_0 \circ \tau
$$
is injective. Thus the inequality. If equality holds, then
every $\sigma \in \Mor_F(E, \overline{F})$ is gotten by precomposing
$\sigma_0$ by an automorphism. Hence $\sigma(E) = \sigma_0(E)$.
Thus $E$ is normal over $F$ by Lemma \ref{lemma-characterize-normal}.

\medskip\noindent
Conversely, assume that $E/F$ is normal. Then by
Lemma \ref{lemma-characterize-normal} we have $\sigma(E) = \sigma_0(E)$
for all $\sigma \in \Mor_F(E, \overline{F})$.
Thus we get an automorphism of $E$ over $F$ by setting
$\tau = \sigma_0^{-1} \circ \sigma$. Whence the map displayed above
is surjective.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-normal-and-automorphisms}
Soit $E/F$ une extension finie. On a
$$
|\text{Aut}(E/F)| \leq [E : F]_s
$$
avec égalité si et seulement si $E$ est normale sur $F$.
\end{lemma}

\begin{proof}
Choisissons une clôture algébrique $\overline{F}$ de $F$. Rappelons que
$[E : F]_s = |\Mor_F(E, \overline{F})|$. Choisissons un élément
$\sigma_0 \in \Mor_F(E, \overline{F})$. Alors l'application
$$
\text{Aut}(E/F) \longrightarrow \Mor_F(E, \overline{F}),\quad
\tau \longmapsto \sigma_0 \circ \tau
$$
est injective. D'où l'inégalité. S'il y a égalité, tout
$\sigma \in \Mor_F(E, \overline{F})$ s'obtient en précomposant
$\sigma_0$ par un automorphisme. Ainsi $\sigma(E) = \sigma_0(E)$.
Donc $E$ est normale sur $F$ d'après le Lemme \ref{lemma-characterize-normal}.

\medskip\noindent
Réciproquement, supposons que $E/F$ est normale. Alors, d'après le
Lemme \ref{lemma-characterize-normal}, on a $\sigma(E) = \sigma_0(E)$
pour tout $\sigma \in \Mor_F(E, \overline{F})$.
On obtient donc un automorphisme de $E$ sur $F$ en posant
$\tau = \sigma_0^{-1} \circ \sigma$. Par conséquent, l'application ci-dessus
est surjective.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B4-PROSE-0012

`lemma-normal-embeddings-differ-by-aut` — source 2025–2042, français 2025–2042.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2025) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

L/K reste algébrique normale, tandis que E/K n'est pas supposée algébrique. L'alternative absence de plongement ou orbite par les automorphismes conserve le sens tau composé avec sigma. La preuve brève par remplacement de L par son image et référence reste brève.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-normal-embeddings-differ-by-aut}
Let $L/K$ be an algebraic normal extension of fields.
Let $E/K$ be an extension of fields. Then either
there is no $K$-embedding from $L$ to $E$ or
there is one $\tau : L \to E$ and every other
one is of the form $\tau \circ \sigma$ where $\sigma \in \text{Aut}(L/K)$.
\end{lemma}

\begin{proof}
Given $\tau$ replace $L$ by $\tau(L) \subset E$ and apply
Lemma \ref{lemma-lift-maps}.
\end{proof}





\section{Splitting fields}
```

```tex
\label{lemma-normal-embeddings-differ-by-aut}
Soit $L/K$ une extension algébrique normale de corps.
Soit $E/K$ une extension de corps. Alors, soit
il n'existe aucun $K$-plongement de $L$ dans $E$, soit
il en existe un $\tau : L \to E$ et tout autre
est de la forme $\tau \circ \sigma$, où $\sigma \in \text{Aut}(L/K)$.
\end{lemma}

\begin{proof}
Étant donné $\tau$, remplaçons $L$ par $\tau(L) \subset E$ et appliquons le
Lemme \ref{lemma-lift-maps}.
\end{proof}





\section{Corps de décomposition}
```

</details>

### FR-FIELDS-B4-PROSE-0013

`section-splitting-fieds` — source 2043–2048, français 2043–2048.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2043) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Corps de décomposition est attesté dans le titre et la définition 2.1.1 du cours. Le lemme est annoncé comme outil, pas comme nouvelle définition. L'identifiant historique splitting-fieds est conservé exactement malgré sa graphie.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-splitting-fieds}

\noindent
The following lemma is a useful tool for constructing normal field extensions.

\begin{lemma}
```

```tex
\label{section-splitting-fieds}

\noindent
Le lemme suivant est un outil utile pour construire des extensions normales de corps.

\begin{lemma}
```

</details>

### FR-FIELDS-B4-PROSE-0014

`lemma-splitting-field` — source 2049–2078, français 2049–2078.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2049) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Polynôme non constant, plus petite extension, normalité et unicité à isomorphisme non nécessairement unique sont tous conservés. Le français explicite la parenthèse nonunique sans la supprimer. La preuve garde le coefficient c, les deux familles de racines, la minimalité et la permutation induite par sigma, puis l'isomorphisme sur F.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-splitting-field}
Let $F$ be a field. Let $P \in F[x]$ be a nonconstant polynomial.
There exists a smallest field extension $E/F$ such that $P$
splits completely over $E$. Moreover, the field extension $E/F$ is normal
and unique up to (nonunique) isomorphism.
\end{lemma}

\begin{proof}
Choose an algebraic closure $\overline{F}$. Then we can write
$P = c (x - \beta_1) \ldots (x - \beta_n)$ in $\overline{F}[x]$, see
Lemma \ref{lemma-algebraically-closed}. Note that $c \in F^*$. Set
$E = F(\beta_1, \ldots, \beta_n)$. Then it is clear that $E$ is
minimal with the requirement that $P$ splits completely over $E$.

\medskip\noindent
Next, let $E'$ be another minimal field extension of $F$ such that
$P$ splits completely over $E'$. Write
$P = c (x - \alpha_1) \ldots (x - \alpha_n)$ with $c \in F$ and
$\alpha_i \in E'$. Again it follows from minimality that
$E' = F(\alpha_1, \ldots, \alpha_n)$. Moreover, if we pick
any $\sigma : E' \to \overline{F}$
(Lemma \ref{lemma-map-into-algebraic-closure})
then we immediately see that $\sigma(\alpha_i) = \beta_{\tau(i)}$
for some permutation $\tau : \{1, \ldots, n\} \to \{1, \ldots, n\}$.
Thus $\sigma(E') = E$. This implies that $E'$ is a normal extension
of $F$ by Lemma \ref{lemma-characterize-normal}
and that $E \cong E'$ as extensions of $F$ thereby finishing the proof.
\end{proof}

\begin{definition}
```

```tex
\label{lemma-splitting-field}
Soit $F$ un corps. Soit $P \in F[x]$ un polynôme non constant.
Il existe une plus petite extension de corps $E/F$ telle que $P$
soit scindé sur $E$. De plus, l'extension de corps $E/F$ est normale
et unique à isomorphisme près, cet isomorphisme n'étant pas nécessairement unique.
\end{lemma}

\begin{proof}
Choisissons une clôture algébrique $\overline{F}$. Nous pouvons alors écrire
$P = c (x - \beta_1) \ldots (x - \beta_n)$ dans $\overline{F}[x]$, voir le
Lemme \ref{lemma-algebraically-closed}. Notons que $c \in F^*$. Posons
$E = F(\beta_1, \ldots, \beta_n)$. Il est alors clair que $E$ est
minimale sous la condition que $P$ soit scindé sur $E$.

\medskip\noindent
Soit ensuite $E'$ une autre extension minimale de $F$ telle que
$P$ soit scindé sur $E'$. Écrivons
$P = c (x - \alpha_1) \ldots (x - \alpha_n)$ avec $c \in F$ et
$\alpha_i \in E'$. La minimalité entraîne de nouveau que
$E' = F(\alpha_1, \ldots, \alpha_n)$. De plus, si nous choisissons
un $\sigma : E' \to \overline{F}$ quelconque
(Lemme \ref{lemma-map-into-algebraic-closure}),
nous voyons immédiatement que $\sigma(\alpha_i) = \beta_{\tau(i)}$
pour une certaine permutation $\tau : \{1, \ldots, n\} \to \{1, \ldots, n\}$.
Ainsi $\sigma(E') = E$. Cela implique que $E'$ est une extension normale
de $F$ d'après le Lemme \ref{lemma-characterize-normal},
et que $E \cong E'$ comme extensions de $F$, ce qui achève la démonstration.
\end{proof}

\begin{definition}
```

</details>

### FR-FIELDS-B4-PROSE-0015

`definition-splitting-field` — source 2079–2085, français 2079–2085.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2079) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Le corps de décomposition est celui construit pour le polynôme P sur la base F. Il n'est pas confondu avec un corps de rupture, qui ne demande qu'une racine. La formulation du cours pour une famille de polynômes n'élargit pas ici la définition officielle pour un seul polynôme.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-splitting-field}
Let $F$ be a field. Let $P \in F[x]$ be a nonconstant polynomial.
The field extension $E/F$ constructed in Lemma \ref{lemma-splitting-field}
is called the {\it splitting field of $P$ over $F$}.
\end{definition}

\begin{lemma}
```

```tex
\label{definition-splitting-field}
Soit $F$ un corps. Soit $P \in F[x]$ un polynôme non constant.
L'extension de corps $E/F$ construite au Lemme \ref{lemma-splitting-field}
est appelée le {\it corps de décomposition de $P$ sur $F$}.
\end{definition}

\begin{lemma}
```

</details>

### FR-FIELDS-B4-PROSE-0016

`lemma-normal-closure` — source 2086–2123, français 2086–2123.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2086) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Le slogan, la finitude et la plus petite extension normale sur F restent ceux de l'anglais. Les générateurs, le produit des polynômes minimaux, le facteur Q et l'intersection de deux images dans une clôture sont conservés. Unique n'est pas silencieusement remplacé par unique à isomorphisme près : l'imprécision de la source est signalée, et la preuve conclut bien par un isomorphisme d'extensions de E.

**Réserve :** L'énoncé dit unique, mais sans fixer une clôture ambiante la preuve donne un isomorphisme. Cette réserve officielle est conservée hors traduction ; le canon précise l'ambiance, mais ne remplace pas la formulation de Stacks.

Choix écartés :

- Ajouter à isomorphisme près dans l'énoncé : clarification mathématique souhaitable mais extérieure à une traduction fidèle du témoin fixé.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-normal-closure}
\begin{slogan}
Existence of normal closure of finite extensions of fields.
\end{slogan}
Let $E/F$ be a finite extension of fields. There exists a unique
smallest finite extension $K/E$ such that $K$ is normal over $F$.
\end{lemma}

\begin{proof}
Choose generators $\alpha_1, \ldots, \alpha_n$ of $E$ over $F$.
Let $P_1, \ldots, P_n$ be the minimal polynomials of
$\alpha_1, \ldots, \alpha_n$ over $F$. Set $P = P_1 \ldots P_n$.
Observe that $(x - \alpha_1) \ldots (x - \alpha_n)$ divides $P$, since
each $(x - \alpha_i)$ divides $P_i$. Say
$P = (x - \alpha_1) \ldots (x - \alpha_n)Q$.
Let $K/E$ be the splitting field of $P$ over $E$.
We claim that $K$ is the splitting field of $P$ over $F$ as well
(which implies that $K$ is normal over $F$).
This is clear because $K/E$ is generated by the roots of
$Q$ over $E$ and $E$ is generated by the roots of
$(x - \alpha_1) \ldots (x - \alpha_n)$ over $F$, hence
$K$ is generated by the roots of $P$ over $F$.

\medskip\noindent
Uniqueness. Suppose that $K'/E$ is a second smallest extension such that
$K'/F$ is normal. Choose an algebraic closure $\overline{F}$ and an
embedding $\sigma_0 : E \to \overline{F}$. By
Lemma \ref{lemma-map-into-algebraic-closure}
we can extend $\sigma_0$ to $\sigma : K \to \overline{F}$ and
$\sigma' : K' \to \overline{F}$.
By Lemma \ref{lemma-intersect-normal} we see that
$\sigma(K) \cap \sigma'(K')$ is normal over $F$.
By minimality we conclude that $\sigma(K) = \sigma'(K')$.
Thus $\sigma^{-1} \circ \sigma' : K' \to K$ gives an isomorphism
of extensions of $E$.
\end{proof}

\begin{definition}
```

```tex
\label{lemma-normal-closure}
\begin{slogan}
Existence de la clôture normale des extensions finies de corps.
\end{slogan}
Soit $E/F$ une extension finie de corps. Il existe une unique
plus petite extension finie $K/E$ telle que $K$ soit normale sur $F$.
\end{lemma}

\begin{proof}
Choisissons des générateurs $\alpha_1, \ldots, \alpha_n$ de $E$ sur $F$.
Soient $P_1, \ldots, P_n$ les polynômes minimaux de
$\alpha_1, \ldots, \alpha_n$ sur $F$. Posons $P = P_1 \ldots P_n$.
Observons que $(x - \alpha_1) \ldots (x - \alpha_n)$ divise $P$, puisque
chaque $(x - \alpha_i)$ divise $P_i$. Écrivons
$P = (x - \alpha_1) \ldots (x - \alpha_n)Q$.
Soit $K/E$ le corps de décomposition de $P$ sur $E$.
Nous affirmons que $K$ est également le corps de décomposition de $P$ sur $F$
(ce qui implique que $K$ est normale sur $F$).
Cela est clair, car $K/E$ est engendrée par les racines de
$Q$ sur $E$, tandis que $E$ est engendrée par les racines de
$(x - \alpha_1) \ldots (x - \alpha_n)$ sur $F$ ; ainsi,
$K$ est engendrée par les racines de $P$ sur $F$.

\medskip\noindent
Unicité. Supposons que $K'/E$ soit une seconde extension minimale telle que
$K'/F$ soit normale. Choisissons une clôture algébrique $\overline{F}$ et un
plongement $\sigma_0 : E \to \overline{F}$. D'après le
Lemme \ref{lemma-map-into-algebraic-closure},
nous pouvons prolonger $\sigma_0$ en $\sigma : K \to \overline{F}$ et en
$\sigma' : K' \to \overline{F}$.
D'après le Lemme \ref{lemma-intersect-normal}, on voit que
$\sigma(K) \cap \sigma'(K')$ est normale sur $F$.
La minimalité donne $\sigma(K) = \sigma'(K')$.
Ainsi $\sigma^{-1} \circ \sigma' : K' \to K$ fournit un isomorphisme
d'extensions de $E$.
\end{proof}

\begin{definition}
```

</details>

### FR-FIELDS-B4-PROSE-0017

`definition-normal-closure` — source 2124–2133, français 2124–2133.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2124) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Clôture normale conserve le nom déjà défini et son objet E sur F. Le de absent de l'anglais normal closure E est une réparation de syntaxe nécessaire en français, non un changement mathématique. Le canon consulté dit fermeture normale : il atteste l'objet, mais pas cette variante lexicale exacte.

**Réserve :** Fermeture normale est lexicalement attesté dans les pages consultées ; clôture normale est maintenu comme variante cohérente et définie par le même objet. Ne pas prétendre disposer ici d'une citation exacte pour cette variante.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-normal-closure}
Let $E/F$ be a finite extension of fields. The field extension $K/E$
constructed in Lemma \ref{lemma-normal-closure}
is called the {\it normal closure $E$ over $F$}.
\end{definition}

\noindent
One can construct the normal closure inside any given normal extension.

\begin{lemma}
```

```tex
\label{definition-normal-closure}
Soit $E/F$ une extension finie de corps. L'extension de corps $K/E$
construite au Lemme \ref{lemma-normal-closure}
est appelée la {\it clôture normale de $E$ sur $F$}.
\end{definition}

\noindent
On peut construire la clôture normale à l'intérieur de toute extension normale donnée.

\begin{lemma}
```

</details>

### FR-FIELDS-B4-PROSE-0018

`lemma-normal-closure-inside-normal` — source 2134–2164, français 2134–2164.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2134) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Les deux tours et leurs bases de finitude sont distinctes et préservées. Dans (2), les polynômes minimaux sont sur K alors que les générateurs sont d'abord choisis sur M. Toutes leurs racines sont prises dans L ; M est inclus dans l'ensemble générateur. La brièveté de la justification de finitude demeure celle de la source, sans ajout de preuve.

**Réserve :** La preuve de (2) conclut explicitement la normalité, laissant la finitude suivre implicitement du nombre fini de racines. Le français n'ajoute pas une démonstration absente.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-normal-closure-inside-normal}
Let $L/K$ be an algebraic normal extension.
\begin{enumerate}
\item If $L/M/K$ is a subextension with $M/K$ finite, then there exists
a tower $L/M'/M/K$ with $M'/K$ finite and normal.
\item If $L/M'/M/K$ is a tower with $M/K$ normal and $M'/M$ finite,
then there exists a tower $L/M''/M'/M/K$ with $M''/M$
finite and $M''/K$ normal.
\end{enumerate}
\end{lemma}

\begin{proof}
Proof of (1). Let $M'$ be the smallest subextension of $L/K$ containing $M$
which is normal over $K$. By Lemma \ref{lemma-normal-closure}
this is the normal closure of $M/K$ and is finite over $K$.

\medskip\noindent
Proof of (2). Let $\alpha_1, \ldots, \alpha_n \in M'$ generate $M'$ over $M$.
Let $P_1, \ldots, P_n$ be the minimal polynomials of
$\alpha_1, \ldots, \alpha_n$ over $K$. Let $\alpha_{i, j}$ be the roots
of $P_i$ in $L$. Let $M''  = M(\alpha_{i, j})$. It follows from
Lemma \ref{lemma-normally-generated}
(applied with the set of generators $M \cup \{\alpha_{i, j}\}$)
that $M''$ is normal over $K$.
\end{proof}

\noindent
The following lemma can sometimes be used to prove properties
of the normal closure.

\begin{lemma}
```

```tex
\label{lemma-normal-closure-inside-normal}
Soit $L/K$ une extension algébrique normale.
\begin{enumerate}
\item Si $L/M/K$ est une sous-extension avec $M/K$ finie, alors il existe
une tour $L/M'/M/K$ telle que $M'/K$ soit finie et normale.
\item Si $L/M'/M/K$ est une tour telle que $M/K$ soit normale et $M'/M$ finie,
alors il existe une tour $L/M''/M'/M/K$ telle que $M''/M$ soit
finie et $M''/K$ normale.
\end{enumerate}
\end{lemma}

\begin{proof}
Démonstration de (1). Soit $M'$ la plus petite sous-extension de $L/K$ contenant $M$
qui soit normale sur $K$. D'après le Lemme \ref{lemma-normal-closure},
c'est la clôture normale de $M/K$, et elle est finie sur $K$.

\medskip\noindent
Démonstration de (2). Soient $\alpha_1, \ldots, \alpha_n \in M'$ des générateurs de $M'$ sur $M$.
Soient $P_1, \ldots, P_n$ les polynômes minimaux de
$\alpha_1, \ldots, \alpha_n$ sur $K$. Soient $\alpha_{i, j}$ les racines
de $P_i$ dans $L$. Posons $M''  = M(\alpha_{i, j})$. Il résulte du
Lemme \ref{lemma-normally-generated}
(appliqué à l'ensemble de générateurs $M \cup \{\alpha_{i, j}\}$)
que $M''$ est normale sur $K$.
\end{proof}

\noindent
Le lemme suivant peut parfois servir à démontrer des propriétés
de la clôture normale.

\begin{lemma}
```

</details>

### FR-FIELDS-B4-PROSE-0019

`lemma-normal-closure-tensor-product` — source 2165–2211, français 2165–2211.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2165) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Le nombre de facteurs tensoriels reste le degré séparable, borné par le degré total. Toutes les images sigma_i(L), le fait que la sous-algèbre algébrique est un corps, la permutation des plongements, la minimalité et la formule du morphisme surjectif restent exacts. Une seule phrase est réparée : après le corps M', normale / elle devient normal / il. L'accord est attesté en 2.2.1–2.2.2 du canon et ne change ni objet ni hypothèse.

Choix écartés :

- Conserver elle après le corps M' : accord incohérent avec l'antécédent explicite, corrigé sans changer la sous-extension désignée.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-normal-closure-tensor-product}
Let $L/K$ be a finite extension. Let $M/L$ be the normal
closure of $L$ over $K$. Then there is a surjective map
$$
L \otimes_K L \otimes_K \ldots \otimes_K L \longrightarrow M
$$
of $K$-algebras where the number of tensors can be taken
$[L : K]_s \leq [L : K]$.
\end{lemma}

\begin{proof}
Choose an algebraic closure $\overline{K}$ of $K$.
Set $n = [L : K]_s = |\Mor_K(L, \overline{K})|$ with equality by
Lemma \ref{lemma-separable-degree}.
Say $\Mor_K(L, \overline{K}) = \{\sigma_1, \ldots, \sigma_n\}$.
Let $M' \subset \overline{K}$ be the $K$-subalgebra
generated by $\sigma_i(L)$, $i = 1, \ldots, n$. Then $M'$ is
a field since any $K$-subalgebra of $\overline{K}$ is a field.
Any $K$-algebra map from $M'$ to $\overline{K}$ permutes the $\sigma_i$
so sends $M'$ into and onto $M'$. By construction the field $M'$
is generated by conjugates of elements of $\sigma_1(L)$. Having said
this it follows from Lemma \ref{lemma-characterize-normal}
that $M'$ is normal over $K$ and that it is the
smallest normal subextension of $\overline{K}$ containing
$\sigma_1(L)$. By uniqueness of normal closure we have $M \cong M'$.
Finally, there is a surjective map
$$
L \otimes_K L \otimes_K \ldots \otimes_K L \longrightarrow M',
\quad
\lambda_1 \otimes \ldots \otimes \lambda_n \longmapsto
\sigma_1(\lambda_1) \ldots \sigma_n(\lambda_n)
$$
and note that $n \leq [L : K]$ by definition.
\end{proof}












\section{Roots of unity}
```

```tex
\label{lemma-normal-closure-tensor-product}
Soit $L/K$ une extension finie. Soit $M/L$ la clôture
normale de $L$ sur $K$. Alors il existe une application surjective
$$
L \otimes_K L \otimes_K \ldots \otimes_K L \longrightarrow M
$$
de $K$-algèbres, où le nombre de facteurs tensoriels peut être pris égal à
$[L : K]_s \leq [L : K]$.
\end{lemma}

\begin{proof}
Choisissons une clôture algébrique $\overline{K}$ de $K$.
Posons $n = [L : K]_s = |\Mor_K(L, \overline{K})|$, l'égalité résultant du
Lemme \ref{lemma-separable-degree}.
Écrivons $\Mor_K(L, \overline{K}) = \{\sigma_1, \ldots, \sigma_n\}$.
Soit $M' \subset \overline{K}$ la $K$-sous-algèbre
engendrée par $\sigma_i(L)$, $i = 1, \ldots, n$. Alors $M'$ est
un corps, car toute $K$-sous-algèbre de $\overline{K}$ est un corps.
Tout morphisme de $K$-algèbres de $M'$ vers $\overline{K}$ permute les $\sigma_i$,
et envoie donc le sous-corps $M'$ sur $M'$. Par construction, le corps $M'$
est engendré par les conjugués d'éléments de $\sigma_1(L)$. Cela étant,
il résulte du Lemme \ref{lemma-characterize-normal}
que $M'$ est normal sur $K$ et qu'il est la
plus petite sous-extension normale de $\overline{K}$ contenant
$\sigma_1(L)$. Par unicité de la clôture normale, on a $M \cong M'$.
Enfin, il existe une application surjective
$$
L \otimes_K L \otimes_K \ldots \otimes_K L \longrightarrow M',
\quad
\lambda_1 \otimes \ldots \otimes \lambda_n \longmapsto
\sigma_1(\lambda_1) \ldots \sigma_n(\lambda_n)
$$
et notons que $n \leq [L : K]$ par définition.
\end{proof}












\section{Racines de l’unité}
```

</details>

### FR-FIELDS-B4-PROSE-0020

`section-roots-of-1` — source 2212–2232, français 2212–2232.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2212) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Le groupe des racines n-ièmes de l'unité, son opération multiplicative, son neutre, les majorations de cardinal et les sous-groupes pour d divisant n sont conservés. Le français distingue explicitement l'ensemble et ses éléments pour rendre les deux appellations anglaises ; il ne définit pas deux groupes différents. Le canon atteste le même terme et la même notation.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-roots-of-1}

\noindent
Let $F$ be a field. For an integer $n \geq 1$ we set
$$
\mu_n(F) = \{\zeta \in F \mid \zeta^n = 1\}
$$
This is called the {\it group of $n$th roots of unity} or
{\it $n$th roots of $1$}. It is an abelian group under multiplication
with neutral element given by $1$.
Observe that in a field the number of roots of a polynomial of degree $d$
is always at most $d$. Hence we see that $|\mu_n(F)| \leq n$
as it is defined by a polynomial equation of degree $n$.
Of course every element of $\mu_n(F)$ has order dividing $n$.
Moreover, the subgroups
$$
\mu_d(F) \subset \mu_n(F),\quad d | n
$$
each have at most $d$ elements. This implies that $\mu_n(F)$ is cyclic.

\begin{lemma}
```

```tex
\label{section-roots-of-1}

\noindent
Soit $F$ un corps. Pour un entier $n \geq 1$, posons
$$
\mu_n(F) = \{\zeta \in F \mid \zeta^n = 1\}
$$
On appelle cet ensemble le {\it groupe des racines $n$-ièmes de l'unité} ; ses
éléments sont les {\it racines $n$-ièmes de $1$}. C'est un groupe abélien pour la multiplication,
dont l'élément neutre est $1$.
Observons que, dans un corps, le nombre de racines d'un polynôme de degré $d$
est toujours au plus $d$. Ainsi $|\mu_n(F)| \leq n$,
puisque cet ensemble est défini par une équation polynomiale de degré $n$.
Bien entendu, tout élément de $\mu_n(F)$ est d'ordre divisant $n$.
En outre, les sous-groupes
$$
\mu_d(F) \subset \mu_n(F),\quad d | n
$$
ont chacun au plus $d$ éléments. Cela implique que $\mu_n(F)$ est cyclique.

\begin{lemma}
```

</details>

### FR-FIELDS-B4-PROSE-0021

`lemma-cyclic` — source 2233–2265, français 2233–2265.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2233) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Le critère concerne un groupe abélien d'exposant divisant n ; chaque sous-groupe annulé par d a le même majorant. La décomposition en facteurs cycliques et le calcul e_1^r sont conservés, y compris l'absence de traitement explicite du groupe trivial. L'application au corps premier, la transition vers les corps finis et l'observation en caractéristique p demeurent complètes. La preuve différente du cours n'est pas importée.

**Réserve :** La preuve écrit e_1 et conclut r=1, sans séparer le cas A trivial (r=0). La conclusion est vraie dans ce cas, mais l'omission de preuve est celle du texte officiel ; elle n'est pas comblée clandestinement.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-cyclic}
Let $A$ be an abelian group of exponent dividing $n$ such that
$\{x \in A \mid dx = 0\}$ has cardinality at most $d$ for all $d | n$.
Then $A$ is cyclic of order dividing $n$.
\end{lemma}

\begin{proof}
The conditions imply that $|A| \leq n$, in particular $A$ is finite.
The structure of finite abelian groups shows that
$A = \mathbf{Z}/e_1\mathbf{Z} \oplus \ldots \oplus \mathbf{Z}/e_r\mathbf{Z}$
for some integers $1 < e_1 | e_2 | \ldots | e_r$. This would imply
that $\{x \in A \mid e_1 x = 0\}$ has cardinality $e_1^r$. Hence
$r = 1$.
\end{proof}

\noindent
Applying this to the field $\mathbf{F}_p$ we obtain the celebrated result
that the group $(\mathbf{Z}/p\mathbf{Z})^*$ is a cyclic group. More about
this in the section on finite fields.

\medskip\noindent
One more observation is often useful: If $F$ has characteristic
$p > 0$, then $\mu_{p^n}(F) = \{1\}$. This is true because raising
to the $p$th power is an injective map on fields of characteristic $p$
as we have seen in the proof of Lemma \ref{lemma-nr-roots-unchanged}.
(Of course, it also follows from the statement of that lemma itself.)






\section{Finite fields}
```

```tex
\label{lemma-cyclic}
Soit $A$ un groupe abélien d'exposant divisant $n$ tel que
$\{x \in A \mid dx = 0\}$ soit de cardinal au plus $d$ pour tout $d | n$.
Alors $A$ est cyclique d'ordre divisant $n$.
\end{lemma}

\begin{proof}
Les conditions impliquent que $|A| \leq n$ ; en particulier, $A$ est fini.
La structure des groupes abéliens finis montre que
$A = \mathbf{Z}/e_1\mathbf{Z} \oplus \ldots \oplus \mathbf{Z}/e_r\mathbf{Z}$
pour des entiers $1 < e_1 | e_2 | \ldots | e_r$. Cela impliquerait
que $\{x \in A \mid e_1 x = 0\}$ est de cardinal $e_1^r$. Par conséquent,
$r = 1$.
\end{proof}

\noindent
Appliqué au corps $\mathbf{F}_p$, ceci donne le célèbre résultat
selon lequel le groupe $(\mathbf{Z}/p\mathbf{Z})^*$ est cyclique. Nous reviendrons sur
cette question dans la section consacrée aux corps finis.

\medskip\noindent
Une autre observation est souvent utile : si $F$ est de caractéristique
$p > 0$, alors $\mu_{p^n}(F) = \{1\}$. Cela tient à ce que l'élévation
à la puissance $p$ est une application injective sur les corps de caractéristique $p$,
comme nous l'avons vu dans la démonstration du Lemme \ref{lemma-nr-roots-unchanged}.
(Bien entendu, cela résulte aussi de l'énoncé même de ce lemme.)






\section{Corps finis}
```

</details>

### FR-FIELDS-B4-PROSE-0022

`section-finite` — source 2266–2293, français 2266–2293.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2266) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

La caractéristique positive, le cardinal p^f, l'exposant du groupe des unités et sa cyclicité sont distingués. Le générateur multiplicatif donne ensuite un générateur de l'extension de corps ; ces deux sens ne sont pas confondus. Le dernier argument porte sur toute extension de corps finis. Corps premier conserve l'objet attesté comme sous-corps premier dans le cours.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-finite}

\noindent
Let $F$ be a finite field. It is clear that $F$ has positive characteristic
as we cannot have an injection $\mathbf{Q} \to F$. Say the characteristic
of $F$ is $p$. The extension $\mathbf{F}_p \subset F$ is finite.
Hence we see that $F$ has $q = p^f$ elements for some $f \geq 1$.

\medskip\noindent
Let us think about the group of units $F^*$. This is a finite abelian
group, so it has some exponent $e$. Then $F^* = \mu_e(F)$ and we see
from the discussion in Section \ref{section-roots-of-1} that $F^*$
is a cyclic group of order $q - 1$. (A posteriori it follows that
$e = q - 1$ as well.) In particular, if $\alpha \in F^*$ is a generator
then it clearly is true that
$$
F = \mathbf{F}_p(\alpha)
$$
In other words, the extension $F/\mathbf{F}_p$ is generated by a single
element. Of course, the same thing is true for any extension of finite
fields $E/F$ (because $E$ is already generated by a single element over
the prime field).





\section{Primitive elements}
```

```tex
\label{section-finite}

\noindent
Soit $F$ un corps fini. Il est clair que $F$ est de caractéristique positive,
car il ne peut exister d'injection $\mathbf{Q} \to F$. Supposons que la caractéristique
de $F$ soit $p$. L'extension $\mathbf{F}_p \subset F$ est finie.
Nous voyons ainsi que $F$ possède $q = p^f$ éléments pour un certain $f \geq 1$.

\medskip\noindent
Considérons le groupe des unités $F^*$. C'est un groupe abélien
fini, il possède donc un certain exposant $e$. Alors $F^* = \mu_e(F)$, et la
discussion de la section \ref{section-roots-of-1} montre que $F^*$
est un groupe cyclique d'ordre $q - 1$. (A posteriori, il en résulte aussi que
$e = q - 1$.) En particulier, si $\alpha \in F^*$ est un générateur,
alors il est clair que
$$
F = \mathbf{F}_p(\alpha)
$$
Autrement dit, l'extension $F/\mathbf{F}_p$ est engendrée par un seul
élément. Bien entendu, il en va de même de toute extension de corps finis
$E/F$ (car $E$ est déjà engendré par un seul élément sur
le corps premier).





\section{Éléments primitifs}
```

</details>

### FR-FIELDS-B4-PROSE-0023

`section-primitive-element` — source 2294–2300, français 2294–2300.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2294) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Élément primitif signifie générateur de l'extension E/F, non nécessairement générateur du groupe multiplicatif. La finitude reste dans l'introduction de Stacks ; le cours définit aussi monogène dans une généralité plus large, qui n'est pas importée.

Choix écartés :

- Définir primitif par générateur du groupe multiplicatif : rejeté ; les deux concepts coïncident seulement dans certains usages et le critère officiel est E=F(alpha).

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-primitive-element}

\noindent
Let $E/F$ be a finite extension of fields. An element $\alpha \in E$
is called a {\it primitive element of $E$ over $F$} if $E = F(\alpha)$.

\begin{lemma}[Primitive element]
```

```tex
\label{section-primitive-element}

\noindent
Soit $E/F$ une extension finie de corps. Un élément $\alpha \in E$
est appelé {\it élément primitif de $E$ sur $F$} si $E = F(\alpha)$.

\begin{lemma}[Élément primitif]
```

</details>

### FR-FIELDS-B4-PROSE-0024

`lemma-primitive-element` — source 2301–2358, français 2301–2358.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2301) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Les deux assertions équivalentes et la suffisance de la séparabilité sont conservées. Le premier sens reconstruit le corps intermédiaire à partir des coefficients du polynôme minimal ; facteurs unitaires signifie facteurs de coefficient dominant un, non facteurs inversibles. Le sens réciproque distingue corps fini et infini. La dernière partie utilise les noyaux des différences de plongements et le dénombrement des images. Tous les paragraphes, les détails omis et les inégalités restent en place ; la preuve par combinaisons linéaires du cours ne leur est pas substituée.

**Réserve :** La parenthèse sur une réunion finie de sous-espaces suppose le corps infini du paragraphe. Le dernier paragraphe réutilise cet argument ; le cas fini est déjà traité. Ne pas lire cette phrase isolément comme une assertion valable sur tout corps.

Choix écartés :

- Remplacer facteurs unitaires par facteurs inversibles : rejeté, monic impose le coefficient dominant un, pas le statut d'unité dans E[x].
- Insérer la preuve du cours français : rejeté ; l'argument anglais doit rester celui qui est traduit.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-primitive-element}
Let $E/F$ be a finite extension of fields. The following are equivalent
\begin{enumerate}
\item there exists a primitive element for $E$ over $F$, and
\item there are finitely many subextensions $E/K/F$.
\end{enumerate}
Moreover, (1) and (2) hold if $E/F$ is separable.
\end{lemma}

\begin{proof}
Let $\alpha \in E$ be a primitive element. Let $P$ be the minimal
polynomial of $\alpha$ over $F$. Next, let $E/K/F$ be a subextension.
Let $Q$ be the minimal polynomial of $\alpha$ over $K$. Observe that
$\deg(Q) = [E : K]$. Writing $Q = x^d + \sum_{i < d} a_i x^i$ we claim that
$K$ is equal to $L = F(a_0, \ldots, a_{d - 1})$. Indeed $\alpha$ has degree
$d$ over $L$ and $L \subset K$. Hence $[E : L] = [E : K]$ and it follows
that $[K : L] = 1$, i.e., $K = L$.
Thus it suffices to show there are at most finitely many possibilities
for the polynomial $Q$. This is clear because we have a factorization
$P = QR$  in $K[x]$ in particular in $E[x]$. Since we have unique
factorization in $E[x]$ there are at most finitely many monic
factors of $P$ in $E[x]$.

\medskip\noindent
If $F$ is a finite field (equivalently $E$ is a finite field), then
$E/F$ has a primitive element by the discussion in
Section \ref{section-finite}.
Next, assume $F$ is infinite and there are at most finitely many proper
subfields $E/K/F$. List them, say $K_1, \ldots, K_N$. Then
each $K_i \subset E$ is a proper sub $F$-vector space. As $F$ is infinite
we can find a vector $\alpha \in E$ with $\alpha \not \in K_i$ for all $i$
(a vector space can never be equal to a finite union of proper subvector spaces;
details omitted). Then $\alpha$ is a primitive element for $E$ over $F$.

\medskip\noindent
Having established the equivalence of (1) and (2) we now turn to
the final statement of the lemma. Choose an algebraic closure
$\overline{F}$ of $F$. Enumerate the elements
$\sigma_1, \ldots, \sigma_n \in \Mor_F(E, \overline{F})$.
Since $E/F$ is separable we have $n = [E : F]$ by
Lemma \ref{lemma-separable-equality}.
Note that if $i \not = j$, then
$$
V_{ij} = \Ker(\sigma_i - \sigma_j : E \longrightarrow \overline{F})
$$
is not equal to $E$. Hence arguing as in the preceding paragraph
we can find $\alpha \in E$ with $\alpha \not \in V_{ij}$ for all
$i \not = j$. It follows that $|\Mor_F(F(\alpha), \overline{F})| \geq n$.
On the other hand $[F(\alpha) : F] \leq [E : F]$. Hence equality
by Lemma \ref{lemma-separable-equality}
and we conclude that $E = F(\alpha)$.
\end{proof}
```

```tex
\label{lemma-primitive-element}
Soit $E/F$ une extension finie de corps. Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item il existe un élément primitif de $E$ sur $F$ ;
\item il existe un nombre fini de sous-extensions $E/K/F$.
\end{enumerate}
De plus, (1) et (2) sont vérifiées si $E/F$ est séparable.
\end{lemma}

\begin{proof}
Soit $\alpha \in E$ un élément primitif. Soit $P$ le polynôme minimal
de $\alpha$ sur $F$. Soit ensuite $E/K/F$ une sous-extension.
Soit $Q$ le polynôme minimal de $\alpha$ sur $K$. Observons que
$\deg(Q) = [E : K]$. En écrivant $Q = x^d + \sum_{i < d} a_i x^i$, nous affirmons que
$K$ est égal à $L = F(a_0, \ldots, a_{d - 1})$. En effet, $\alpha$ est de degré
$d$ sur $L$ et $L \subset K$. Ainsi $[E : L] = [E : K]$, d'où
$[K : L] = 1$, c'est-à-dire $K = L$.
Il suffit donc de montrer qu'il n'existe qu'un nombre fini de possibilités
pour le polynôme $Q$. Cela est clair, puisque nous avons une factorisation
$P = QR$  dans $K[x]$, et en particulier dans $E[x]$. Comme la factorisation
est unique dans $E[x]$, le polynôme $P$ n'a qu'un nombre fini de facteurs
unitaires dans $E[x]$.

\medskip\noindent
Si $F$ est un corps fini (ce qui équivaut à dire que $E$ est un corps fini), alors
$E/F$ possède un élément primitif d'après la discussion de la
section \ref{section-finite}.
Supposons ensuite $F$ infini et qu'il n'existe qu'un nombre fini de sous-corps
propres $E/K/F$. Énumérons-les, disons $K_1, \ldots, K_N$. Alors
chaque $K_i \subset E$ est un sous-espace vectoriel propre sur $F$. Comme $F$ est infini,
nous pouvons trouver un vecteur $\alpha \in E$ tel que $\alpha \not \in K_i$ pour tout $i$
(un espace vectoriel ne peut jamais être la réunion d'un nombre fini de sous-espaces propres ;
nous omettons les détails). Alors $\alpha$ est un élément primitif de $E$ sur $F$.

\medskip\noindent
Après avoir établi l'équivalence de (1) et (2), démontrons maintenant
la dernière assertion du lemme. Choisissons une clôture algébrique
$\overline{F}$ de $F$. Énumérons les éléments
$\sigma_1, \ldots, \sigma_n \in \Mor_F(E, \overline{F})$.
Puisque $E/F$ est séparable, on a $n = [E : F]$ d'après le
Lemme \ref{lemma-separable-equality}.
Notons que, si $i \not = j$, alors
$$
V_{ij} = \Ker(\sigma_i - \sigma_j : E \longrightarrow \overline{F})
$$
n'est pas égal à $E$. En raisonnant comme au paragraphe précédent,
nous pouvons donc trouver $\alpha \in E$ tel que $\alpha \not \in V_{ij}$ pour tous
$i \not = j$. Il s'ensuit que $|\Mor_F(F(\alpha), \overline{F})| \geq n$.
D'autre part, $[F(\alpha) : F] \leq [E : F]$. Il y a donc égalité
d'après le Lemme \ref{lemma-separable-equality},
et nous concluons que $E = F(\alpha)$.
\end{proof}
```

</details>

## Limites et suite

Analyse assistée par OpenAI Codex ; l'identité exacte du modèle et de l'effort de cette exécution n'est pas attestée par ce reçu et n'est pas inventée. Ce dossier local n'est pas une publication de l'édition restaurée. Aucun expert humain ni corpus terminologique exhaustif n'est déclaré validé.

Prochaine section : Trace et norme, ligne officielle 2359. Les dix-neuf sections déjà lues restent acquises avec leurs réserves. Le reste du chapitre, les autres contrôles incomplets, la reconstruction et la publication cumulative restent à accomplir. L'ancienne édition éditorialisée est conservée pour un éventuel travail distinct, non réétiquetée comme une traduction vérifiée de l'anglais AI-intégré.
