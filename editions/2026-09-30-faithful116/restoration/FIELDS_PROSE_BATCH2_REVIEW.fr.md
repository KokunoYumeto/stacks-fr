# Chapitre 9 — Corps : extensions et clôtures algébriques

**Quatre sections entièrement comparées, source lignes 601–1122. Aucun nouveau changement du français n’est nécessaire dans ce lot. La lecture continue cumulée atteint 11 sections et la ligne 1122 ; elle n’est pas achevée pour le chapitre.**

[LaTeX de travail inchangé](staged/fr/009_fields.prose-batch1.fr.tex) · [Validation](FIELDS_PROSE_BATCH2_VALIDATION.json) · [Paires et choix](FIELDS_PROSE_BATCH2_CHOICES.json) · [Occurrences](FIELDS_PROSE_BATCH2_OCCURRENCES.json) · [Premier lot conservé](FIELDS_PROSE_BATCH1_REVIEW.fr.md)

## Ce qui est vérifié

Lecture comparée intégrale des sections Extensions algébriques, Polynômes minimaux, Clôture algébrique et Polynômes premiers entre eux : énoncés, preuves, slogans, exemples, avertissements et transitions. Les 26 paires ci-dessous partitionnent exactement le périmètre, sans trou ni doublon. Les frontières d'étiquettes servent de repères, pas nécessairement de fins de phrases.

Les 356 régions mathématiques du lot sont identiques à la source officielle, dans le même ordre. Le fichier français entier reste identique à celui du premier lot. L'inversion de sa réparation supplémentaire puis des 19 restaurations historiques retrouve tous les octets du témoin public. Ces contrôles ne remplacent pas la lecture de la prose, et ne prouvent pas la fidélité des passages encore non lus.

## Canon français effectivement consulté

Marc Reversat et Benoît Zhang, [Cours de théorie des corps](https://www.math.univ-toulouse.fr/~reversat/galois.pdf), 24 mars 2003. §§1.3–1.4 et §1.5 jusqu'à la proposition 1.5.11 et sa preuve : pages imprimées 5–13, pages PDF 13–21. Les pages 5 et 12 ont aussi été rendues et inspectées. La suite de la remarque 1.5.13 n'est pas revendiquée lue.

Témoin : 816199 octets ; SHA-256 `73A1D0DCD0B7F11625293615E693B198C0C33BAE3A57C78A705153CE33942E8A`. [Passages, limites et règles](FIELDS_PROSE_BATCH2_CONSULTED_CANON.json). Cette consultation est rétrospective ; elle ne prétend pas décrire le travail du traducteur initial.

Ce cours est un témoin de langue et de concepts, non une autorité infaillible. Sa preuve 1.5.8 rédige le contrôle d'inductivité pour une suite ; cette limitation n'est pas copiée dans la preuve de Stacks sur les chaînes quelconques. La formule de composition au bas de p.12 est également ill-typée telle qu'imprimée. Ni cette formule ni la preuve alternative d'existence ne sont importées. Le libellé complet du lemme 1.5.10 est lu ; on ne remplace pas pour autant le choix de P de Stacks par un polynôme minimal.

## Points importants pour une relecture experte

La fidélité demandée ne signifie pas approbation des erreurs du témoin anglais. Les points suivants restent hors du texte traduit et ne bloquent pas la production :

- `lemma-algebraic-elements` : Quotient : hypothèse de dénominateur non nul laissée implicite par la source. Corps composés : attestation lexicale externe non obtenue dans ce lot.
- `lemma-algebraic-permanence` : Sous-extension de k est une tournure source imprécise ; le paragraphe fournit k(S) avec S dans E. La traduction garde cette lecture et son explication.
- `lemma-algebraic-extension-self-map` : Choix de P sans qualification non nul dans l'anglais ; ne pas importer la version par polynôme minimal du canon français.
- `definition-minimal-polynomial` : Nonconstant multiple peut décrire le multiple plutôt que son multiplicateur. Lecture anglaise conservée, point source ouvert à examen.
- `theorem-existence-algebraic-closure` : La traduction idiomatique de red herring est discutable stylistiquement ; aucune attestation externe de cette tournure exacte n'est revendiquée.
- `section-relatively-prime` : Deux erreurs sources identifiées : c qualifié de terme constant au lieu de coefficient dominant, et k au lieu de K. Elles restent dans le témoin traduit fidèle et dans les errata séparés.
- `definition-relatively-prime` : Premiers entre eux et idéal unité sont justifiés par leur définition exacte ici ; ces lexèmes ne sont pas attestés dans le périmètre du cours consulté.

Les variantes coefficient dominant et K sont conservées dans le dossier historique des propositions, non réappliquées au texte fidèle. Aucun nouvel identifiant d'erratum ne duplique FIELDS-006 ou FIELDS-007. Les autres réserves ci-dessus sont des observations contextuelles, pas de nouvelles admissions au registre canonique.

## Règles terminologiques et occurrences

### algebraic

Vérifier élément, extension ou nombre selon chaque phrase ; ne pas confondre algébrique et fini.

Occurrences contextuellement contrôlées : 85. Appui : Définition 1.3.1, p.5 ; corollaire 1.3.5, p.7.

### minimal

Le polynôme est le générateur unitaire de l'idéal d'annulation ; minimal se rapporte au degré.

Occurrences contextuellement contrôlées : 10. Appui : Définition 1.3.2 et paragraphe précédent, p.5.

### finite-degree

Le degré d'extension est vectoriel, pas le cardinal du corps ; le degré de polynôme est identifié uniquement là où la source l'affirme.

Occurrences contextuellement contrôlées : 30. Appui : Théorème 1.3.3, p.6 ; corollaire 1.3.5, p.7.

### algebraic-closure

Distinguer une extension algébrique algébriquement close d'un corps simplement clos ; garder la réserve sur la non-canonicité.

Occurrences contextuellement contrôlées : 26. Appui : Proposition 1.5.1, définitions 1.5.2 et 1.5.4, pp.9–10.

### morphism-extension

Prolongement conserve la restriction sur le corps de base. Maximal ne signifie pas maximum. Automorphisme inclut la surjectivité.

Occurrences contextuellement contrôlées : 5. Appui : Proposition 1.5.8 et lemme 1.5.9, p.12 ; lemme 1.5.10, p.13.

### source-defined-lexicon

Sens relu dans les définitions et preuves officielles ; pas d'attestation externe obtenue pour ces expressions dans les passages consultés. Maintien motivé, non certification bibliographique.

Occurrences contextuellement contrôlées : 9. Appui : définition et contexte officiels ; attestation externe non obtenue dans ce périmètre.

### expository-choices

Traduction d'une réserve ou d'un commentaire de méthode. Pas d'attestation de la tournure exacte revendiquée ; le contexte source gouverne le choix.

Occurrences contextuellement contrôlées : 3. Appui : définition et contexte officiels ; attestation externe non obtenue dans ce périmètre.

## Tous les passages comparés

### FR-FIELDS-B2-PROSE-0001

`frontmatter` — source 601–601, français 602–602.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L601) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le titre Extensions algébriques correspond à la nouvelle section. Il ne modifie pas le périmètre des extensions finies déjà traité.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\section{Algebraic extensions}
```

```tex
\section{Extensions algébriques}
```

</details>

### FR-FIELDS-B2-PROSE-0002

`section-algebraic-extensions` — source 602–608, français 603–609.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L602) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

La phrase introductive porte sur chaque élément pris séparément : chacun engendre une extension finie. Elle ne déclare pas toute l'extension finie.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-algebraic-extensions}

\noindent
An important class of extensions are those where every element generates
a finite extension.

\begin{definition}
```

```tex
\label{section-algebraic-extensions}

\noindent
Une classe importante d'extensions est formée de celles dans lesquelles chaque élément engendre
une extension finie.

\begin{definition}
```

</details>

### FR-FIELDS-B2-PROSE-0003

`definition-algebraic` — source 609–626, français 610–627.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L609) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Non nul porte bien sur le polynôme ; les coefficients restent dans E et tous les éléments sont requis pour une extension algébrique. Le commentaire conserve les deux possibilités E(t) et E[t]/(P), l'irréductibilité et le choix de P annulant alpha. Il ne confond pas anneau quotient et corps de fonctions rationnelles.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-algebraic}
Consider a field extension $F/E$. An element $\alpha \in F$ is said to be
{\it algebraic} over $E$ if $\alpha$ is the root of some nonzero polynomial
with coefficients in $E$. If all elements of $F$ are algebraic then $F$ is
said to be an {\it algebraic extension} of $E$.
\end{definition}

\noindent
By Lemma \ref{lemma-field-extension-generated-by-one-element}, the
subextension $E(\alpha)$ is isomorphic either to the rational function
field $E(t)$ or to a quotient ring $E[t]/(P)$ for $P \in E[t]$ an
irreducible polynomial. In the latter case, $\alpha$ is algebraic over
$E$ (in fact, the proof of
Lemma \ref{lemma-field-extension-generated-by-one-element}
shows that we can pick $P$ such that $\alpha$ is a root of $P$);
in the former case, it is not.

\begin{example}
```

```tex
\label{definition-algebraic}
Considérons une extension de corps $F/E$. Un élément $\alpha \in F$ est dit
{\it algébrique} sur $E$ si $\alpha$ est racine d'un polynôme non nul
à coefficients dans $E$. Si tous les éléments de $F$ sont algébriques, on dit que $F$ est
une {\it extension algébrique} de $E$.
\end{definition}

\noindent
D'après le Lemme \ref{lemma-field-extension-generated-by-one-element}, la
sous-extension $E(\alpha)$ est isomorphe soit au corps des fonctions rationnelles
$E(t)$, soit à un anneau quotient $E[t]/(P)$, où $P \in E[t]$ est un
polynôme irréductible. Dans le second cas, $\alpha$ est algébrique sur
$E$ (en fait, la preuve du
Lemme \ref{lemma-field-extension-generated-by-one-element}
montre que l'on peut choisir $P$ de sorte que $\alpha$ soit une racine de $P$) ;
dans le premier cas, il ne l'est pas.

\begin{example}
```

</details>

### FR-FIELDS-B2-PROSE-0004

`example-C-algebraic-over-R` — source 627–633, français 628–634.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L627) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

La relation quadratique et ses coefficients réels sont exactement conservés. L'équation satisfaite par alpha exprime bien son caractère algébrique, sans ajouter de résultat sur le degré de tout élément.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{example-C-algebraic-over-R}
The field $\mathbf{C}$ is algebraic over $\mathbf{R}$. Namely, if
$\alpha = a + ib$ in $\mathbf{C}$, then $\alpha^2 - 2a\alpha + a^2 + b^2 = 0$
is a polynomial equation for $\alpha$ over $\mathbf{R}$.
\end{example}

\begin{example}
```

```tex
\label{example-C-algebraic-over-R}
Le corps $\mathbf{C}$ est algébrique sur $\mathbf{R}$. En effet, si
$\alpha = a + ib$ dans $\mathbf{C}$, alors $\alpha^2 - 2a\alpha + a^2 + b^2 = 0$
est une équation polynomiale satisfaite par $\alpha$ sur $\mathbf{R}$.
\end{example}

\begin{example}
```

</details>

### FR-FIELDS-B2-PROSE-0005

`example-compact-riemann-surface-is-finite-over-P1` — source 634–642, français 635–643.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L634) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

La surface reste compacte et la fonction méromorphe non constante. La conclusion en prose est algébrique, comme dans l'anglais, malgré le nom de l'étiquette qui mentionne finite. La preuve demeure explicitement omise ; ni connexité ni conclusion plus forte ne sont ajoutées.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{example-compact-riemann-surface-is-finite-over-P1}
Let $X$ be a compact Riemann surface, and let
$f \in \mathbf{C}(X) - \mathbf{C}$ any nonconstant meromorphic function
on $X$ (see Example \ref{example-field-of-meromorphic-functions}). Then it is
known that $\mathbf{C}(X)$ is algebraic over the subextension
$\mathbf{C}(f)$ generated by $f$. We shall not prove this.
\end{example}

\begin{lemma}
```

```tex
\label{example-compact-riemann-surface-is-finite-over-P1}
Soient $X$ une surface de Riemann compacte et
$f \in \mathbf{C}(X) - \mathbf{C}$ une fonction méromorphe non constante quelconque
sur $X$ (voir l'Exemple \ref{example-field-of-meromorphic-functions}). On sait alors
que $\mathbf{C}(X)$ est algébrique sur la sous-extension
$\mathbf{C}(f)$ engendrée par $f$. Nous ne le démontrerons pas.
\end{example}

\begin{lemma}
```

</details>

### FR-FIELDS-B2-PROSE-0006

`lemma-algebraic-goes-up` — source 643–660, français 644–661.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L643) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Les deux assertions conservent le passage de F à E dans K/E/F, pour un élément puis pour le corps entier. La preuve immédiate et la transition annonçant le lien avec la finitude sont conservées. Tour ne devient pas une hypothèse de degrés finis.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-algebraic-goes-up}
Let $K/E/F$ be a tower of field extensions.
\begin{enumerate}
\item If $\alpha \in K$ is algebraic over $F$, then $\alpha$ is algebraic
over $E$.
\item If $K$ is algebraic over $F$, then $K$ is algebraic over $E$.
\end{enumerate}
\end{lemma}

\begin{proof}
This is immediate from the definitions.
\end{proof}

\noindent
We now show that there is a deep connection between finiteness and being
algebraic.

\begin{lemma}
```

```tex
\label{lemma-algebraic-goes-up}
Soit $K/E/F$ une tour d'extensions de corps.
\begin{enumerate}
\item Si $\alpha \in K$ est algébrique sur $F$, alors $\alpha$ est algébrique
sur $E$.
\item Si $K$ est algébrique sur $F$, alors $K$ est algébrique sur $E$.
\end{enumerate}
\end{lemma}

\begin{proof}
Cela résulte immédiatement des définitions.
\end{proof}

\noindent
Montrons à présent qu'il existe un lien étroit entre la finitude et le caractère
algébrique.

\begin{lemma}
```

</details>

### FR-FIELDS-B2-PROSE-0007

`lemma-finite-is-algebraic` — source 661–692, français 662–693.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L661) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

La finitude implique l'algébricité, puis l'équivalence est locale aux sous-extensions engendrées par un élément. L'avertissement contre la réciproque générale reste explicite. La preuve garde la dépendance des n+1 puissances, la référence aux deux exemples, les deux sens et l'observation utilisée ensuite. Monogène est interprété selon la définition antérieure de Stacks, non comme une nouvelle hypothèse d'algèbre finie.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-finite-is-algebraic}
A finite extension is algebraic. In fact, an extension $E/k$ is algebraic
if and only if every subextension $k(\alpha)/k$ generated by some
$\alpha \in E$ is finite.
\end{lemma}

\noindent
In general, it is very false that an algebraic extension is finite.

\begin{proof}
Let $E/k$ be finite, say of degree $n$. Choose $\alpha \in E$. Then the
elements $1, \alpha, \ldots, \alpha^n$ are linearly
dependent over $k$, or we would necessarily have $[E : k] > n$. A relation of
linear dependence now gives the desired polynomial that $\alpha$ must satisfy.

\medskip\noindent
For the last assertion, note that a monogenic extension $k(\alpha)/k$ is
finite if and only if $\alpha$ is algebraic over $k$, by
Examples \ref{example-degree-rational-function-field} and
\ref{example-degree-simple-algebraic-extension}.
So if $E/k$ is algebraic, then each $k(\alpha)/k$, $\alpha \in E$, is a finite
extension, and conversely.
\end{proof}

\noindent
We can extract a lemma of the last proof (really of
Examples \ref{example-degree-rational-function-field} and
\ref{example-degree-simple-algebraic-extension}):
a monogenic extension is finite if and only if it is algebraic.
We shall use this observation in the next result.

\begin{lemma}
```

```tex
\label{lemma-finite-is-algebraic}
Toute extension finie est algébrique. En fait, une extension $E/k$ est algébrique
si et seulement si toute sous-extension $k(\alpha)/k$ engendrée par un
$\alpha \in E$ est finie.
\end{lemma}

\noindent
En général, il est tout à fait faux qu'une extension algébrique soit finie.

\begin{proof}
Soit $E/k$ finie, de degré $n$. Choisissons $\alpha \in E$. Les
éléments $1, \alpha, \ldots, \alpha^n$ sont linéairement
dépendants sur $k$, sans quoi on aurait nécessairement $[E : k] > n$. Une relation de
dépendance linéaire fournit alors le polynôme recherché que $\alpha$ doit annuler.

\medskip\noindent
Pour la dernière assertion, remarquons qu'une extension monogène $k(\alpha)/k$ est
finie si et seulement si $\alpha$ est algébrique sur $k$, d'après les
Exemples \ref{example-degree-rational-function-field} et
\ref{example-degree-simple-algebraic-extension}.
Ainsi, si $E/k$ est algébrique, chaque $k(\alpha)/k$, pour $\alpha \in E$, est une extension
finie, et réciproquement.
\end{proof}

\noindent
Nous pouvons extraire un lemme de la preuve précédente (en réalité, des
Exemples \ref{example-degree-rational-function-field} et
\ref{example-degree-simple-algebraic-extension}) :
une extension monogène est finie si et seulement si elle est algébrique.
Nous utiliserons cette observation dans le résultat suivant.

\begin{lemma}
```

</details>

### FR-FIELDS-B2-PROSE-0008

`lemma-algebraic-finitely-generated` — source 693–720, français 694–721.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L693) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le slogan et l'énoncé disent tous deux de type fini, pas seulement fini. La tour successive conserve le caractère algébrique de chaque générateur et la multiplicativité. Le paragraphe sur les nombres algébriques conserve sqrt(2), i, pi et la difficulté d'une preuve directe par équations. Manipuler les équations explicite le mode de preuve suggéré, sans lui substituer un nouvel argument.

Choix écartés :

- Remplacer de type fini par finie dès l'hypothèse rendrait la proposition tautologique et perdrait sa portée.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-algebraic-finitely-generated}
\begin{slogan}
A finitely generated algebraic extension is finite.
\end{slogan}
Let $k$ be a field, and let $\alpha_1, \alpha_2, \ldots, \alpha_n$ be elements
of some extension field such that each $\alpha_i$ is algebraic over $k$. Then
the extension $k(\alpha_1, \ldots, \alpha_n)/k$ is finite.
That is, a finitely generated algebraic extension is finite.
\end{lemma}

\begin{proof}
Indeed, each extension
$k(\alpha_{1}, \ldots, \alpha_{i+1})/k(\alpha_1, \ldots, \alpha_{i})$
is generated by one element and algebraic, hence finite.
By multiplicativity of degree (Lemma \ref{lemma-multiplicativity-degrees})
we obtain the result.
\end{proof}

\noindent
The set of complex numbers that are algebraic over $\mathbf{Q}$ are simply
called the {\it algebraic numbers.} For instance, $\sqrt{2}$ is algebraic,
$i$ is algebraic, but $\pi$ is not.
It is a basic fact that the algebraic numbers form a field, although it is not
obvious how to prove this from the definition that a number is algebraic
precisely when it satisfies a nonzero polynomial equation with rational
coefficients (e.g. by polynomial equations).

\begin{lemma}
```

```tex
\label{lemma-algebraic-finitely-generated}
\begin{slogan}
Une extension algébrique de type fini est finie.
\end{slogan}
Soient $k$ un corps et $\alpha_1, \alpha_2, \ldots, \alpha_n$ des éléments
d'un corps d'extension tels que chaque $\alpha_i$ soit algébrique sur $k$. Alors
l'extension $k(\alpha_1, \ldots, \alpha_n)/k$ est finie.
Autrement dit, une extension algébrique de type fini est finie.
\end{lemma}

\begin{proof}
En effet, chaque extension
$k(\alpha_{1}, \ldots, \alpha_{i+1})/k(\alpha_1, \ldots, \alpha_{i})$
est engendrée par un élément et algébrique, donc finie.
La multiplicativité du degré (Lemme \ref{lemma-multiplicativity-degrees})
donne le résultat.
\end{proof}

\noindent
L'ensemble des nombres complexes qui sont algébriques sur $\mathbf{Q}$ est simplement
appelé l'ensemble des {\it nombres algébriques.} Par exemple, $\sqrt{2}$ est algébrique,
$i$ est algébrique, mais $\pi$ ne l'est pas.
C'est un fait fondamental que les nombres algébriques forment un corps, bien qu'il ne soit pas
évident de le démontrer à partir de la définition selon laquelle un nombre est algébrique
exactement lorsqu'il satisfait une équation polynomiale non nulle à coefficients
rationnels (par exemple, en manipulant des équations polynomiales).

\begin{lemma}
```

</details>

### FR-FIELDS-B2-PROSE-0009

`lemma-algebraic-elements` — source 721–739, français 722–740.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L721) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Les éléments algébriques de E forment bien une sous-extension de E/k. La preuve de fermeture par somme passe par k(alpha,beta), puis invoque les autres opérations comme la source. Elle n'ajoute pas au texte la condition de dénominateur non nul, implicite pour le quotient. Corps composés traduit composita dans la transition ; cette variante n'est pas attestée par les pages françaises consultées pour ce lot.

**Réserve :** Quotient : hypothèse de dénominateur non nul laissée implicite par la source. Corps composés : attestation lexicale externe non obtenue dans ce lot.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-algebraic-elements}
Let $E/k$ be a field extension. Then the elements of $E$ algebraic over $k$
form a subextension of $E/k$.
\end{lemma}

\begin{proof}
Let $\alpha, \beta \in E$ be algebraic over $k$. Then $k(\alpha, \beta)/k$
is a finite extension by Lemma \ref{lemma-algebraic-finitely-generated}.
It follows that $k(\alpha + \beta) \subset k(\alpha, \beta)$ is a finite
extension, which implies that $\alpha + \beta$ is algebraic by
Lemma \ref{lemma-finite-is-algebraic}. Similarly for the difference,
product and quotient of $\alpha$ and $\beta$.
\end{proof}

\noindent
Many nice properties of field extensions, like those of rings, will have the
property that they will be preserved by towers and composita.

\begin{lemma}
```

```tex
\label{lemma-algebraic-elements}
Soit $E/k$ une extension de corps. Les éléments de $E$ algébriques sur $k$
forment une sous-extension de $E/k$.
\end{lemma}

\begin{proof}
Soient $\alpha, \beta \in E$ algébriques sur $k$. Alors $k(\alpha, \beta)/k$
est une extension finie d'après le Lemme \ref{lemma-algebraic-finitely-generated}.
Il s'ensuit que $k(\alpha + \beta) \subset k(\alpha, \beta)$ est une extension
finie, ce qui implique que $\alpha + \beta$ est algébrique d'après le
Lemme \ref{lemma-finite-is-algebraic}. Il en va de même pour la différence,
le produit et le quotient de $\alpha$ et $\beta$.
\end{proof}

\noindent
De nombreuses propriétés remarquables des extensions de corps, tout comme celles des anneaux, sont
préservées par les tours et les corps composés.

\begin{lemma}
```

</details>

### FR-FIELDS-B2-PROSE-0010

`lemma-algebraic-permanence` — source 740–768, français 741–769.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L740) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

La transitivité est conservée avec l'ordre k, E, F. Le choix fini S contient les coefficients du polynôme ; les deux extensions finies et la multiplicativité sont présents. Sous-extension de type fini de k reprend le libellé ambigu de la source, éclairé immédiatement par k(S) avec S contenu dans E. Descendait reste une méthode de réduction à des données finies, non l'assertion d'un théorème de descente supplémentaire. La remarque sur le cas noethérien est conservée.

**Réserve :** Sous-extension de k est une tournure source imprécise ; le paragraphe fournit k(S) avec S dans E. La traduction garde cette lecture et son explication.

Choix écartés :

- Remplacer descendait par un énoncé nouveau de descente noethérienne modifierait le commentaire de méthode de la source.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-algebraic-permanence}
Let $E/k$ and $F/E$ be algebraic extensions of fields. Then $F/k$ is an
algebraic extension of fields.
\end{lemma}

\begin{proof}
Choose $\alpha \in F$. Then $\alpha$ is algebraic over $E$.
The key observation is that $\alpha$ is algebraic over a
finitely generated subextension of $k$.
That is, there is a finite set $S \subset E$ such that $\alpha $ is algebraic
over $k(S)$: this is clear because being algebraic means that a certain
polynomial in $E[x]$ that $\alpha$ satisfies exists, and as $S$ we can take the
coefficients of this polynomial. It follows that $\alpha$ is algebraic over
$k(S)$. In particular, the extension $k(S, \alpha)/ k(S)$ is finite.
Since $S$ is a finite set, and $k(S)/k$ is algebraic,
Lemma \ref{lemma-algebraic-finitely-generated} shows that
$k(S)/k$ is finite. Using multiplicativity
(Lemma \ref{lemma-multiplicativity-degrees})
we find that $k(S,\alpha)/k$ is finite, so $\alpha$ is algebraic over $k$.
\end{proof}

\noindent
The method of proof in the previous argument --- that being algebraic
over $E$ was a property that {\it descended} to a finitely generated
subextension of $E$ --- is an idea that recurs throughout algebra.
It often allows one to reduce general commutative algebra questions
to the Noetherian case for example.

\begin{lemma}
```

```tex
\label{lemma-algebraic-permanence}
Soient $E/k$ et $F/E$ des extensions algébriques de corps. Alors $F/k$ est une
extension algébrique de corps.
\end{lemma}

\begin{proof}
Choisissons $\alpha \in F$. Alors $\alpha$ est algébrique sur $E$.
L'observation essentielle est que $\alpha$ est algébrique sur une
sous-extension de type fini de $k$.
Autrement dit, il existe un ensemble fini $S \subset E$ tel que $\alpha $ soit algébrique
sur $k(S)$ : cela est clair, puisque le fait d'être algébrique signifie qu'il existe un
polynôme de $E[x]$ annulé par $\alpha$, et l'on peut prendre pour $S$ l'ensemble des
coefficients de ce polynôme. Il en résulte que $\alpha$ est algébrique sur
$k(S)$. En particulier, l'extension $k(S, \alpha)/ k(S)$ est finie.
Comme $S$ est un ensemble fini et que $k(S)/k$ est algébrique, le
Lemme \ref{lemma-algebraic-finitely-generated} montre que
$k(S)/k$ est finie. En utilisant la multiplicativité
(Lemme \ref{lemma-multiplicativity-degrees}),
on trouve que $k(S,\alpha)/k$ est finie ; ainsi $\alpha$ est algébrique sur $k$.
\end{proof}

\noindent
La méthode de la preuve précédente --- le fait que la propriété d'être algébrique
sur $E$ {\it descendait} à une sous-extension de type fini
de $E$ --- est une idée récurrente en algèbre.
Elle permet souvent, par exemple, de ramener des questions générales d'algèbre commutative
au cas noethérien.

\begin{lemma}
```

</details>

### FR-FIELDS-B2-PROSE-0011

`lemma-size-algebraic-extension` — source 769–785, français 770–786.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L769) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

La borne cardinale est la même. Les polynômes sont non constants, leurs ensembles de racines finis et leur réunion couvre E. Réunion dénombrable de produits finis conserve la distinction entre finitude de chaque produit et cardinal de F. Les détails omis ne sont pas inventés.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-size-algebraic-extension}
Let $E/F$ be an algebraic extension of fields. Then the cardinality $|E|$
of $E$ is at most $\max(\aleph_0, |F|)$.
\end{lemma}

\begin{proof}
Let $S$ be the set of nonconstant polynomials with coefficients in $F$.
For every $P \in S$ the set of roots
$r(P, E) = \{\alpha \in E \mid P(\alpha) = 0\}$
is finite (details omitted). Moreover, the fact that $E$ is algebraic
over $F$ implies that $E = \bigcup_{P \in S} r(P, E)$.
It is clear that $S$ has cardinality bounded by $\max(\aleph_0, |F|)$
because it is a countable union of finite products of copies of $F$.
Thus so does $E$.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-size-algebraic-extension}
Soit $E/F$ une extension algébrique de corps. Alors le cardinal $|E|$
de $E$ est au plus $\max(\aleph_0, |F|)$.
\end{lemma}

\begin{proof}
Soit $S$ l'ensemble des polynômes non constants à coefficients dans $F$.
Pour tout $P \in S$, l'ensemble des racines
$r(P, E) = \{\alpha \in E \mid P(\alpha) = 0\}$
est fini (les détails sont omis). De plus, le fait que $E$ soit algébrique
sur $F$ implique que $E = \bigcup_{P \in S} r(P, E)$.
Il est clair que le cardinal de $S$ est majoré par $\max(\aleph_0, |F|)$,
car cet ensemble est une réunion dénombrable de produits finis de copies de $F$.
Il en va donc de même pour $E$.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B2-PROSE-0012

`lemma-subalgebra-algebraic-extension-field` — source 786–806, français 787–807.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L786) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le sous-anneau contient F ; non nul qualifie alpha, et les coefficients de la relation appartiennent à F. La réduction au terme a0 non nul et l'expression de l'inverse sont exactes. Aucune exigence de fermeture supplémentaire n'est substituée à la preuve.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-subalgebra-algebraic-extension-field}
Let $E/F$ be a finite or more generally an algebraic extension of fields.
Any subring $F \subset R \subset E$ is a field.
\end{lemma}

\begin{proof}
Let $\alpha \in R$ be nonzero. Then $1, \alpha, \alpha^2, \ldots$
are contained in $R$. By Lemma \ref{lemma-finite-is-algebraic}
we find a nontrivial relation
$a_0 + a_1 \alpha + \ldots + a_d \alpha^d = 0$ with $a_i \in F$.
We may assume $a_0 \not = 0$ because if not we can divide the relation
by $\alpha$ to decrease $d$. Then we see that
$$
a_0 = \alpha (- a_1  - \ldots - a_d \alpha^{d - 1})
$$
which proves that the inverse of $\alpha$ is the element
$a_0^{-1} (- a_1  - \ldots - a_d \alpha^{d - 1})$
of $R$.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-subalgebra-algebraic-extension-field}
Soit $E/F$ une extension finie, ou plus généralement algébrique, de corps.
Tout sous-anneau $F \subset R \subset E$ est un corps.
\end{lemma}

\begin{proof}
Soit $\alpha \in R$ non nul. Alors $1, \alpha, \alpha^2, \ldots$
appartiennent à $R$. D'après le Lemme \ref{lemma-finite-is-algebraic},
il existe une relation non triviale
$a_0 + a_1 \alpha + \ldots + a_d \alpha^d = 0$, avec $a_i \in F$.
Nous pouvons supposer $a_0 \not = 0$, car sinon nous pouvons diviser la relation
par $\alpha$ afin de diminuer $d$. On obtient alors
$$
a_0 = \alpha (- a_1  - \ldots - a_d \alpha^{d - 1})
$$
ce qui prouve que l'inverse de $\alpha$ est l'élément
$a_0^{-1} (- a_1  - \ldots - a_d \alpha^{d - 1})$
de $R$.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B2-PROSE-0013

`lemma-algebraic-extension-self-map` — source 807–833, français 808–836.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L807) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Morphisme de F-algèbres rend la compatibilité au corps de base. Le cas fini utilise l'injectivité et la dimension, puis le cas général le sous-corps engendré par les racines, sa stabilité et la surjectivité sur alpha. La source ne dit pas explicitement que P est non nul ; la traduction ne complète pas cette lacune. Le témoin terminologique français utilise le polynôme minimal, mais cet argument alternatif ne remplace pas celui de Stacks.

**Réserve :** Choix de P sans qualification non nul dans l'anglais ; ne pas importer la version par polynôme minimal du canon français.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-algebraic-extension-self-map}
Let $E/F$ an algebraic extension of fields. Any $F$-algebra map
$f : E \to E$ is an automorphism.
\end{lemma}

\begin{proof}
If $E/F$ is finite, then $f : E \to E$ is an $F$-linear
injective map (Lemma \ref{lemma-field-maps-injective})
of finite dimensional vector spaces, and hence bijective.
In general we still see that $f$ is injective.
Let $\alpha \in E$ and let $P \in F[x]$ be a
polynomial such that $P(\alpha) = 0$.
Let $E' \subset E$ be the subfield of $E$ generated
by the roots $\alpha = \alpha_1, \ldots, \alpha_n$ of $P$ in $E$.
Then $E'$ is finite over $F$ by Lemma \ref{lemma-algebraic-finitely-generated}.
Since $f$ preserves the set of roots, we find that
$f|_{E'} : E' \to E'$. Hence $f|_{E'}$ is an isomorphism
by the first part of the proof and we conclude that $\alpha$
is in the image of $f$.
\end{proof}






\section{Minimal polynomials}
```

```tex
\label{lemma-algebraic-extension-self-map}
Soit $E/F$ une extension algébrique de corps. Tout morphisme de $F$-algèbres
$f : E \to E$ est un automorphisme.
\end{lemma}

\begin{proof}
Si $E/F$ est finie, alors $f : E \to E$ est une application $F$-linéaire
injective (Lemme \ref{lemma-field-maps-injective})
entre espaces vectoriels de dimension finie, donc est bijective.
Dans le cas général, on voit encore que $f$ est injective.
Soit $\alpha \in E$, et soit $P \in F[x]$ un
polynôme tel que $P(\alpha) = 0$.
Soit $E' \subset E$ le sous-corps de $E$ engendré
par les racines $\alpha = \alpha_1, \ldots, \alpha_n$ de $P$ dans $E$.
Alors $E'$ est fini sur $F$ d'après le Lemme \ref{lemma-algebraic-finitely-generated}.
Comme $f$ préserve l'ensemble des racines, on a
$f|_{E'} : E' \to E'$. Ainsi $f|_{E'}$ est un isomorphisme
d'après la première partie de la preuve, et l'on conclut que $\alpha$
appartient à l'image de $f$.
\end{proof}








\section{Polynômes minimaux}
```

</details>

### FR-FIELDS-B2-PROSE-0014

`section-minimal-polynomials` — source 834–850, français 837–853.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L834) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Anneau principal rend PID, et unitaire rend monic. L'idéal est le noyau de l'évaluation ; son générateur unitaire est unique. L'annulation d'alpha ne se transforme pas en une propriété de toutes les racines. Le lexique est directement attesté en 1.3.2 du cours consulté.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-minimal-polynomials}

\noindent
Let $E/k$ be a field extension, and let $\alpha \in E$ be algebraic over $k$.
Then $\alpha$ satisfies a (nontrivial) polynomial equation in $k[x]$.
Consider the set of polynomials $P \in k[x]$ such that $P(\alpha) = 0$; by
hypothesis, this set does not just contain the zero polynomial.
It is easy to see that this set is an {\it ideal.} Indeed, it is the kernel
of the map
$$
k[x] \to E, \quad x \mapsto \alpha
$$
Since $k[x]$ is a PID, there is a {\it generator} $P \in k[x]$ of this
ideal. If we assume $P$ monic, without loss of generality, then $P$ is
uniquely determined.

\begin{definition}
```

```tex
\label{section-minimal-polynomials}

\noindent
Soient $E/k$ une extension de corps et $\alpha \in E$ algébrique sur $k$.
Alors $\alpha$ satisfait une équation polynomiale (non triviale) dans $k[x]$.
Considérons l'ensemble des polynômes $P \in k[x]$ tels que $P(\alpha) = 0$ ; par
hypothèse, cet ensemble ne contient pas seulement le polynôme nul.
On vérifie facilement que cet ensemble est un {\it idéal.} C'est en effet le noyau
du morphisme
$$
k[x] \to E, \quad x \mapsto \alpha
$$
Puisque $k[x]$ est un anneau principal, il existe un {\it générateur} $P \in k[x]$ de cet
idéal. Si l'on suppose, sans perte de généralité, que $P$ est unitaire, alors $P$ est
déterminé de manière unique.

\begin{definition}
```

</details>

### FR-FIELDS-B2-PROSE-0015

`definition-minimal-polynomial` — source 851–869, français 854–872.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L851) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Polynôme minimal, degré minimal, irréductibilité et idéal premier sont conservés, avec la justification par un morphisme vers un anneau intègre. La phrase multiple non constant reste ambiguë comme l'anglais : le raisonnement exige un multiplicateur de degré positif. Cette difficulté est signalée séparément, non corrigée dans le texte traduit.

**Réserve :** Nonconstant multiple peut décrire le multiple plutôt que son multiplicateur. Lecture anglaise conservée, point source ouvert à examen.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-minimal-polynomial}
The polynomial $P$ above is called the {\it minimal polynomial}
of $\alpha$ over $k$.
\end{definition}

\noindent
The minimal polynomial has the following characterization: it is the monic
polynomial, of smallest degree, that annihilates $\alpha$. Any nonconstant
multiple of $P$ will have larger degree, and only multiples of $P$ can
annihilate $\alpha$. This explains the name {\it minimal}.

\medskip\noindent
Clearly the minimal polynomial is {\it irreducible}. This is equivalent to the
assertion that the ideal in $k[x]$ consisting of polynomials annihilating
$\alpha$ is prime. This follows from the fact that the map
$k[x] \to E, x \mapsto \alpha$ is a map into a domain (even a field), so the
kernel is a prime ideal.

\begin{lemma}
```

```tex
\label{definition-minimal-polynomial}
Le polynôme $P$ ci-dessus est appelé le {\it polynôme minimal}
de $\alpha$ sur $k$.
\end{definition}

\noindent
Le polynôme minimal possède la caractérisation suivante : c'est le polynôme unitaire,
de plus petit degré, qui annule $\alpha$. Tout multiple non constant de $P$
sera de degré plus grand, et seuls les multiples de $P$ peuvent
annuler $\alpha$. Cela explique le qualificatif {\it minimal}.

\medskip\noindent
Le polynôme minimal est manifestement {\it irréductible}. Cela équivaut à affirmer
que l'idéal de $k[x]$ formé des polynômes qui annulent
$\alpha$ est premier. Ce fait résulte de ce que le morphisme
$k[x] \to E, x \mapsto \alpha$ prend ses valeurs dans un anneau intègre (et même dans un corps), de sorte que son
noyau est un idéal premier.

\begin{lemma}
```

</details>

### FR-FIELDS-B2-PROSE-0016

`lemma-degree-minimal-polynomial` — source 870–891, français 873–894.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L870) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le degré est celui de k(alpha)/k. L'évaluation quotient est un isomorphisme, et le renvoi à la base calculée antérieurement est inchangé. La conclusion après la preuve est également préservée, sans remplacer l'isomorphisme par une égalité d'ensembles.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-degree-minimal-polynomial}
The degree of the minimal polynomial is $[k(\alpha) : k]$.
\end{lemma}

\begin{proof}
This is just a restatement of the argument in
Lemma \ref{lemma-field-extension-generated-by-one-element}: the observation
is that if $P$ is the minimal polynomial of $\alpha$, then the map
$$
k[x]/(P) \to k(\alpha), \quad x \mapsto \alpha
$$
is an isomorphism as in the aforementioned proof, and we have counted the
degree of such an extension (see
Example \ref{example-degree-simple-algebraic-extension}).
\end{proof}

\noindent
So the observation of the above proof is that if $\alpha \in E$ is algebraic,
then $k(\alpha) \subset E$ is isomorphic to $k[x]/(P)$.


\section{Algebraic closure}
```

```tex
\label{lemma-degree-minimal-polynomial}
Le degré du polynôme minimal est $[k(\alpha) : k]$.
\end{lemma}

\begin{proof}
Il s'agit simplement d'une reformulation de l'argument donné dans le
Lemme \ref{lemma-field-extension-generated-by-one-element} : l'observation
est que, si $P$ est le polynôme minimal de $\alpha$, le morphisme
$$
k[x]/(P) \to k(\alpha), \quad x \mapsto \alpha
$$
est un isomorphisme comme dans la preuve précitée, et nous avons calculé le
degré d'une telle extension (voir
l'Exemple \ref{example-degree-simple-algebraic-extension}).
\end{proof}

\noindent
L'observation de la preuve ci-dessus est donc que, si $\alpha \in E$ est algébrique,
alors $k(\alpha) \subset E$ est isomorphe à $k[x]/(P)$.


\section{Clôture algébrique}
```

</details>

### FR-FIELDS-B2-PROSE-0017

`section-algebraic-closure` — source 892–900, français 895–903.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L892) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le théorème fondamental de l'algèbre et la preuve utilisant Liouville restent distingués de la preuve annoncée plus loin. Aucun argument analytique nouveau n'est fourni.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-algebraic-closure}

\noindent
The ``fundamental theorem of algebra'' states that $\mathbf{C}$ is
algebraically closed. A beautiful proof of this result uses
Liouville's theorem in complex analysis, we shall give another
proof (see Lemma \ref{lemma-C-algebraically-closed}).

\begin{definition}
```

```tex
\label{section-algebraic-closure}

\noindent
Le ``théorème fondamental de l'algèbre'' affirme que $\mathbf{C}$ est
algébriquement clos. Une belle démonstration de ce résultat utilise
le théorème de Liouville en analyse complexe ; nous en donnerons une autre
(voir le Lemme \ref{lemma-C-algebraically-closed}).

\begin{definition}
```

</details>

### FR-FIELDS-B2-PROSE-0018

`definition-algebraically-closed` — source 901–910, français 904–913.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L901) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

La définition choisie par Stacks est l'absence d'extension algébrique non triviale. La réserve sur d'autres définitions usuelles demeure. Le canon français confirme l'équivalence, sans imposer de changer l'ordre d'exposition.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-algebraically-closed}
A field $F$ is said to be {\it algebraically closed} if every algebraic
extension $E/F$ is trivial, i.e., $E = F$.
\end{definition}

\noindent
This may not be the definition in every text. Here is the lemma comparing
it with the other one.

\begin{lemma}
```

```tex
\label{definition-algebraically-closed}
On dit qu'un corps $F$ est {\it algébriquement clos} si toute extension algébrique
$E/F$ est triviale, c'est-à-dire si $E = F$.
\end{definition}

\noindent
Ce n'est peut-être pas la définition retenue dans tous les ouvrages. Le lemme suivant
la compare à l'autre définition usuelle.

\begin{lemma}
```

</details>

### FR-FIELDS-B2-PROSE-0019

`lemma-algebraically-closed` — source 911–952, français 914–955.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L911) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Les quatre assertions et chaque implication développée sont conservées. Linéaire est correctement rendu par de degré un pour les polynômes. La division euclidienne et la récurrence produisent les facteurs ; la dernière étape porte sur toutes les sous-extensions simples. Le commentaire suivant distingue très explicitement unicité à isomorphisme près et unicité à unique isomorphisme près, avec la réserve non fonctorielle : aucune propriété universelle n'est ajoutée.

Choix écartés :

- Unicité canonique ou propriété universelle : rejetées, car la source avertit expressément du contraire.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-algebraically-closed}
Let $F$ be a field. The following are equivalent
\begin{enumerate}
\item $F$ is algebraically closed,
\item every irreducible polynomial over $F$ is linear,
\item every nonconstant polynomial over $F$ has a root,
\item every nonconstant polynomial over $F$ is a product of linear factors.
\end{enumerate}
\end{lemma}

\begin{proof}
If $F$ is algebraically closed, then every irreducible polynomial is linear.
Namely, if there exists an irreducible polynomial of degree $> 1$, then
this generates a nontrivial finite (hence algebraic) field extension, see
Example \ref{example-degree-simple-algebraic-extension}.
Thus (1) implies (2). If every irreducible polynomial
is linear, then every irreducible polynomial has a root, whence every
nonconstant polynomial has a root. Thus (2) implies (3).

\medskip\noindent
Assume every nonconstant polynomial has a root. Let $P \in F[x]$
be nonconstant. If $P(\alpha) = 0$ with $\alpha \in F$, then we see
that $P = (x - \alpha)Q$ for some $Q \in F[x]$ (by division with remainder).
Thus we can argue by induction on the degree that any nonconstant
polynomial can be written as a product $c \prod (x - \alpha_i)$.

\medskip\noindent
Finally, suppose that every nonconstant polynomial over $F$ is a product of
linear factors. Let $E/F$ be an algebraic extension. Then all the simple
subextensions $F(\alpha)/F$ of $E$ are necessarily trivial (because the
only irreducible polynomials are linear by assumption). Thus $E = F$.
We see that (4) implies (1) and we are done.
\end{proof}

\noindent
Now we want to define a ``universal'' algebraic extension of a field.
Actually, we should be careful: the algebraic closure is {\it not} a
universal object. That is, the algebraic closure is not unique up to
{\it unique} isomorphism: it is only unique up to isomorphism. But still,
it will be very handy, if not functorial.

\begin{definition}
```

```tex
\label{lemma-algebraically-closed}
Soit $F$ un corps. Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item $F$ est algébriquement clos,
\item tout polynôme irréductible sur $F$ est de degré un,
\item tout polynôme non constant sur $F$ possède une racine,
\item tout polynôme non constant sur $F$ est un produit de facteurs de degré un.
\end{enumerate}
\end{lemma}

\begin{proof}
Si $F$ est algébriquement clos, alors tout polynôme irréductible est de degré un.
En effet, s'il existe un polynôme irréductible de degré $> 1$, celui-ci
engendre une extension de corps finie non triviale (donc algébrique) ; voir
l'Exemple \ref{example-degree-simple-algebraic-extension}.
Ainsi (1) implique (2). Si tout polynôme irréductible
est de degré un, alors tout polynôme irréductible possède une racine, et par conséquent tout
polynôme non constant possède une racine. Ainsi (2) implique (3).

\medskip\noindent
Supposons que tout polynôme non constant possède une racine. Soit $P \in F[x]$
non constant. Si $P(\alpha) = 0$ avec $\alpha \in F$, on voit alors
que $P = (x - \alpha)Q$ pour un certain $Q \in F[x]$ (par division euclidienne).
On peut donc raisonner par récurrence sur le degré pour écrire tout polynôme non constant
sous la forme d'un produit $c \prod (x - \alpha_i)$.

\medskip\noindent
Supposons enfin que tout polynôme non constant sur $F$ soit un produit de
facteurs de degré un. Soit $E/F$ une extension algébrique. Toutes les sous-extensions
simples $F(\alpha)/F$ de $E$ sont alors nécessairement triviales (car, par
hypothèse, les seuls polynômes irréductibles sont de degré un). Ainsi $E = F$.
Nous voyons que (4) implique (1), ce qui achève la preuve.
\end{proof}

\noindent
Nous voulons maintenant définir une extension algébrique ``universelle'' d'un corps.
En réalité, il convient d'être prudent : la clôture algébrique n'est {\it pas} un
objet universel. En effet, la clôture algébrique n'est pas unique à
{\it unique} isomorphisme près : elle n'est unique qu'à isomorphisme près. Elle
n'en sera pas moins très utile, bien que non fonctorielle.

\begin{definition}
```

</details>

### FR-FIELDS-B2-PROSE-0020

`definition-algebraic-closure` — source 953–966, français 956–969.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L953) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Clôture algébrique conserve les deux conditions indépendantes : être algébrique sur F et être algébriquement clos. Contenant F reste une inclusion. Le cas d'un corps déjà clos et la transition vers l'existence sont présents.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-algebraic-closure}
Let $F$ be a field. An {\it algebraic closure} of $F$ is a field
$\overline{F}$ containing $F$ such that:
\begin{enumerate}
\item $\overline{F}$ is algebraic over $F$.
\item $\overline{F}$ is algebraically closed.
\end{enumerate}
\end{definition}

\noindent
If $F$ is algebraically closed, then $F$ is its own algebraic closure.
We now prove the basic existence result.

\begin{theorem}
```

```tex
\label{definition-algebraic-closure}
Soit $F$ un corps. Une {\it clôture algébrique} de $F$ est un corps
$\overline{F}$ contenant $F$ tel que :
\begin{enumerate}
\item $\overline{F}$ est algébrique sur $F$.
\item $\overline{F}$ est algébriquement clos.
\end{enumerate}
\end{definition}

\noindent
Si $F$ est algébriquement clos, alors $F$ est sa propre clôture algébrique.
Démontrons maintenant le résultat fondamental d'existence.

\begin{theorem}
```

</details>

### FR-FIELDS-B2-PROSE-0021

`theorem-existence-algebraic-closure` — source 967–1022, français 970–1025.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L967) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le commentaire red herring est rendu par sans rapport avec le reste du chapitre : il signale une preuve peu utilisée ensuite, non une preuve fausse. La preuve entière conserve le choix strictement plus grand de S, l'ensemble de structures I, les restrictions des deux opérations, les chaînes, leur réunion, le majorant, Zorn et l'extension contradictoire. Élément maximal ne devient pas maximum. L'injection E' vers S prolonge bien celle de E. Le cours français n'est pas utilisé pour substituer sa construction par anneau polynomial à celle de Stacks.

**Réserve :** La traduction idiomatique de red herring est discutable stylistiquement ; aucune attestation externe de cette tournure exacte n'est revendiquée.

Choix écartés :

- Fausse piste au sens d'argument erroné : rejeté, car le commentaire vise l'utilité ultérieure de la preuve, non sa vérité.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{theorem-existence-algebraic-closure}
Every field has an algebraic closure.
\end{theorem}

\noindent
The proof will mostly be a red herring to the rest of the chapter. However, we
will want to know that it is {\it possible} to embed a field inside an
algebraically closed field, and we will often assume it done.

\begin{proof}
Let $F$ be a field. By Lemma \ref{lemma-size-algebraic-extension} the
cardinality of an algebraic extension of $F$ is bounded by
$\max(\aleph_0, |F|)$. Choose a set $S$ containing $F$ with
$|S| > \max(\aleph_0, |F|)$. Let's consider triples
$(E, \sigma_E, \mu_E)$ where
\begin{enumerate}
\item $E$ is a set with $F \subset E \subset S$, and
\item $\sigma_E : E \times E \to E$ and $\mu_E : E \times E \to E$
are maps of sets such that $(E, \sigma_E, \mu_E)$ defines the structure
of a field extension of $F$ (in particular $\sigma_E(a, b) = a +_F b$
for $a, b \in F$ and similarly for $\mu_E$), and
\item $E/F$ is an algebraic field extension.
\end{enumerate}
The collection of all triples $(E, \sigma_E, \mu_E)$ forms a set $I$.
For $i \in I$ we will denote $E_i = (E_i, \sigma_i, \mu_i)$ the
corresponding field extension to $F$. We define a partial ordering on
$I$ by declaring $i \leq i'$ if and only if $E_i \subset E_{i'}$
(this makes sense as $E_i$ and $E_{i'}$ are subsets of the same set $S$)
and we have $\sigma_i = \sigma_{i'}|_{E_i \times E_i}$ and
$\mu_i = \mu_{i'}|_{E_i \times E_i}$, in other words, $E_{i'}$ is a field
extension of $E_i$.

\medskip\noindent
Let $T \subset I$ be a totally ordered subset. Then it is clear that
$E_T = \bigcup_{i \in T} E_i$ with induced maps $\sigma_T = \bigcup \sigma_i$
and $\mu_T = \bigcup \mu_i$ is another element of $I$. In other words
every totally order subset of $I$ has a upper bound in $I$. By Zorn's lemma
there exists a maximal element $(E, \sigma_E, \mu_E)$ in $I$. We claim that
$E$ is an algebraic closure. Since by definition of $I$ the extension
$E/F$ is algebraic, it suffices to show that $E$ is algebraically closed.

\medskip\noindent
To see this we argue by contradiction. Namely, suppose that $E$ is not
algebraically closed. Then there exists an irreducible polynomial
$P$ over $E$ of degree $> 1$, see Lemma \ref{lemma-algebraically-closed}.
By Lemma \ref{lemma-finite-is-algebraic} we obtain a nontrivial finite
extension $E' = E[x]/(P)$. Observe that $E'/F$ is algebraic by
Lemma \ref{lemma-algebraic-permanence}.
Thus the cardinality of $E'$ is $\leq \max(\aleph_0, |F|)$.
By elementary set theory we can extend the given injection
$E \subset S$ to an injection $E' \to S$. In other words, we may
think of $E'$ as an element of our set $I$ contradicting the
maximality of $E$. This contradiction completes the proof.
\end{proof}

\begin{lemma}
```

```tex
\label{theorem-existence-algebraic-closure}
Tout corps possède une clôture algébrique.
\end{theorem}

\noindent
La preuve sera pour l'essentiel sans rapport avec le reste du chapitre. Nous voudrons toutefois
savoir qu'il est {\it possible} de plonger un corps dans un
corps algébriquement clos, et nous supposerons souvent ce plongement effectué.

\begin{proof}
Soit $F$ un corps. D'après le Lemme \ref{lemma-size-algebraic-extension}, le
cardinal d'une extension algébrique de $F$ est majoré par
$\max(\aleph_0, |F|)$. Choisissons un ensemble $S$ contenant $F$ tel que
$|S| > \max(\aleph_0, |F|)$. Considérons les triplets
$(E, \sigma_E, \mu_E)$ où
\begin{enumerate}
\item $E$ est un ensemble tel que $F \subset E \subset S$, et
\item $\sigma_E : E \times E \to E$ et $\mu_E : E \times E \to E$
sont des applications d'ensembles telles que $(E, \sigma_E, \mu_E)$ définisse la structure
d'une extension de corps de $F$ (en particulier, $\sigma_E(a, b) = a +_F b$
pour $a, b \in F$, et de même pour $\mu_E$), et
\item $E/F$ est une extension algébrique de corps.
\end{enumerate}
La collection de tous les triplets $(E, \sigma_E, \mu_E)$ forme un ensemble $I$.
Pour $i \in I$, nous noterons $E_i = (E_i, \sigma_i, \mu_i)$ l'extension de corps
de $F$ correspondante. Nous définissons un ordre partiel sur
$I$ en déclarant que $i \leq i'$ si et seulement si $E_i \subset E_{i'}$
(cela a un sens puisque $E_i$ et $E_{i'}$ sont des sous-ensembles du même ensemble $S$)
et si $\sigma_i = \sigma_{i'}|_{E_i \times E_i}$ et
$\mu_i = \mu_{i'}|_{E_i \times E_i}$ ; autrement dit, $E_{i'}$ est une extension de corps
de $E_i$.

\medskip\noindent
Soit $T \subset I$ un sous-ensemble totalement ordonné. Il est alors clair que
$E_T = \bigcup_{i \in T} E_i$, muni des applications induites $\sigma_T = \bigcup \sigma_i$
et $\mu_T = \bigcup \mu_i$, est un autre élément de $I$. Autrement dit,
tout sous-ensemble totalement ordonné de $I$ possède un majorant dans $I$. D'après le lemme de Zorn,
il existe un élément maximal $(E, \sigma_E, \mu_E)$ de $I$. Nous affirmons que
$E$ est une clôture algébrique. Puisque, par définition de $I$, l'extension
$E/F$ est algébrique, il suffit de montrer que $E$ est algébriquement clos.

\medskip\noindent
Pour le voir, raisonnons par l'absurde. Supposons donc que $E$ ne soit pas
algébriquement clos. Il existe alors un polynôme irréductible
$P$ sur $E$ de degré $> 1$ ; voir le Lemme \ref{lemma-algebraically-closed}.
D'après le Lemme \ref{lemma-finite-is-algebraic}, on obtient une extension finie
non triviale $E' = E[x]/(P)$. Remarquons que $E'/F$ est algébrique d'après le
Lemme \ref{lemma-algebraic-permanence}.
Le cardinal de $E'$ est donc $\leq \max(\aleph_0, |F|)$.
La théorie élémentaire des ensembles permet de prolonger l'injection donnée
$E \subset S$ en une injection $E' \to S$. Autrement dit, nous pouvons
considérer $E'$ comme un élément de notre ensemble $I$, ce qui contredit la
maximalité de $E$. Cette contradiction achève la preuve.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B2-PROSE-0022

`lemma-map-into-algebraic-closure` — source 1023–1051, français 1026–1054.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1023) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le morphisme reste au-dessus de F. Les paires et leur ordre, l'union sur une chaîne, la maximalité, alpha manquant, le polynôme transporté et le prolongement envoyant x sur beta sont tous conservés. La source traite une chaîne quelconque ; on ne la réduit pas à une suite dénombrable en suivant le cours consulté. Prolonger est attesté dans la proposition 1.5.8 et le lemme 1.5.9.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-map-into-algebraic-closure}
Let $F$ be a field. Let $\overline{F}$ be an algebraic closure of $F$.
Let $M/F$ be an algebraic extension. Then there is a morphism of
$F$-extensions $M \to \overline{F}$.
\end{lemma}

\begin{proof}
Consider the set $I$ of pairs $(E, \varphi)$ where $F \subset E \subset M$
is a subextension and $\varphi : E \to \overline{F}$ is a morphism of
$F$-extensions. We partially order the set $I$ by declaring
$(E, \varphi) \leq (E', \varphi')$ if and only if $E \subset E'$ and
$\varphi'|_E = \varphi$. If $T = \{(E_t,  \varphi_t)\} \subset I$
is a totally ordered subset, then
$\bigcup \varphi_t : \bigcup E_t \to \overline{F}$ is an element of $I$.
Thus every totally ordered subset of $I$ has an upper bound.
By Zorn's lemma there exists a maximal element $(E, \varphi)$ in $I$.
We claim that $E = M$, which will finish the proof. If not, then
pick $\alpha \in M$, $\alpha \not \in E$. The $\alpha$ is algebraic
over $E$, see Lemma \ref{lemma-algebraic-goes-up}.
Let $P$ be the minimal polynomial of $\alpha$ over $E$.
Let $P^\varphi$ be the image of $P$ by $\varphi$ in $\overline{F}[x]$.
Since $\overline{F}$ is algebraically closed there is a root $\beta$
of $P^\varphi$ in $\overline{F}$. Then we can extend $\varphi$ to
$\varphi' : E(\alpha) = E[x]/(P) \to \overline{F}$ by mapping
$x$ to $\beta$. This contradicts the maximality of $(E, \varphi)$
as desired.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-map-into-algebraic-closure}
Soit $F$ un corps. Soit $\overline{F}$ une clôture algébrique de $F$.
Soit $M/F$ une extension algébrique. Il existe alors un morphisme
d'extensions de $F$, $M \to \overline{F}$.
\end{lemma}

\begin{proof}
Considérons l'ensemble $I$ des couples $(E, \varphi)$, où $F \subset E \subset M$
est une sous-extension et $\varphi : E \to \overline{F}$ un morphisme
d'extensions de $F$. Munissons $I$ de l'ordre partiel défini en déclarant que
$(E, \varphi) \leq (E', \varphi')$ si et seulement si $E \subset E'$ et
$\varphi'|_E = \varphi$. Si $T = \{(E_t,  \varphi_t)\} \subset I$
est un sous-ensemble totalement ordonné, alors
$\bigcup \varphi_t : \bigcup E_t \to \overline{F}$ est un élément de $I$.
Ainsi, tout sous-ensemble totalement ordonné de $I$ possède un majorant.
Le lemme de Zorn assure l'existence d'un élément maximal $(E, \varphi)$ de $I$.
Nous affirmons que $E = M$, ce qui achèvera la preuve. Sinon,
choisissons $\alpha \in M$, $\alpha \not \in E$. Alors $\alpha$ est algébrique
sur $E$ ; voir le Lemme \ref{lemma-algebraic-goes-up}.
Soit $P$ le polynôme minimal de $\alpha$ sur $E$.
Soit $P^\varphi$ l'image de $P$ par $\varphi$ dans $\overline{F}[x]$.
Comme $\overline{F}$ est algébriquement clos, il existe une racine $\beta$
de $P^\varphi$ dans $\overline{F}$. On peut alors prolonger $\varphi$ en
$\varphi' : E(\alpha) = E[x]/(P) \to \overline{F}$ en envoyant
$x$ sur $\beta$. Cela contredit la maximalité de $(E, \varphi)$,
comme voulu.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B2-PROSE-0023

`lemma-algebraic-closures-isomorphic` — source 1052–1071, français 1055–1074.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1052) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

La conclusion est l'existence d'un isomorphisme, non son unicité. La preuve conserve le morphisme entre clôtures, l'image algébriquement close et l'extension algébrique de cette image, donc l'égalité finale. Les positions de M et F-barre ne sont pas inversées.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-algebraic-closures-isomorphic}
Any two algebraic closures of a field are isomorphic.
\end{lemma}

\begin{proof}
Let $F$ be a field. If $M$ and $\overline{F}$ are algebraic closures of
$F$, then there exists a morphism of $F$-extensions
$\varphi : M \to \overline{F}$ by
Lemma \ref{lemma-map-into-algebraic-closure}.
Now the image $\varphi(M)$ is algebraically closed.
On the other hand, the extension $\varphi(M) \subset \overline{F}$
is algebraic by Lemma \ref{lemma-algebraic-goes-up}.
Thus $\varphi(M) = \overline{F}$.
\end{proof}





\section{Relatively prime polynomials}
```

```tex
\label{lemma-algebraic-closures-isomorphic}
Deux clôtures algébriques quelconques d'un corps sont isomorphes.
\end{lemma}

\begin{proof}
Soit $F$ un corps. Si $M$ et $\overline{F}$ sont des clôtures algébriques de
$F$, il existe alors un morphisme d'extensions de $F$
$\varphi : M \to \overline{F}$ d'après le
Lemme \ref{lemma-map-into-algebraic-closure}.
Or l'image $\varphi(M)$ est algébriquement close.
D'autre part, l'extension $\varphi(M) \subset \overline{F}$
est algébrique d'après le Lemme \ref{lemma-algebraic-goes-up}.
Ainsi $\varphi(M) = \overline{F}$.
\end{proof}





\section{Polynômes premiers entre eux}
```

</details>

### FR-FIELDS-B2-PROSE-0024

`section-relatively-prime` — source 1072–1086, français 1075–1089.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1072) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Les deux restaurations historiques FIELDS-006 et FIELDS-007 sont confirmées dans le passage complet. Terme constant et la minuscule k sont ceux du texte anglais, même si la factorisation appelle un coefficient dominant et que le corps introduit est K. Les racines comptées avec multiplicité et les seuls irréductibles de degré un sont conservés. Il ne s'agit pas d'approuver mathématiquement ces deux anomalies.

**Réserve :** Deux erreurs sources identifiées : c qualifié de terme constant au lieu de coefficient dominant, et k au lieu de K. Elles restent dans le témoin traduit fidèle et dans les errata séparés.

Choix écartés :

- Rétablir coefficient dominant et K dans cette édition : rejeté ici, bien que mathématiquement motivé ; ce serait réappliquer les emendations retirées.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-relatively-prime}

\noindent
Let $K$ be an algebraically closed field. Then the ring $K[x]$ has a very
simple ideal structure as we saw in Lemma \ref{lemma-algebraically-closed}.
In particular, every polynomial $P \in K[x]$ can be written as
$$
P = c(x - \alpha_1) \ldots (x - \alpha_n),
$$
where $c$ is the constant term and the $\alpha_1, \ldots, \alpha_n \in k$
are the roots of $P$ (counted with multiplicity). Clearly, the only irreducible
polynomials in $K[x]$ are the linear polynomials $c(x - \alpha)$,
$c, \alpha \in K$ (and $c \neq 0$).

\begin{definition}
```

```tex
\label{section-relatively-prime}

\noindent
Soit $K$ un corps algébriquement clos. L'anneau $K[x]$ possède alors une structure
d'idéaux très simple, comme nous l'avons vu au Lemme \ref{lemma-algebraically-closed}.
En particulier, tout polynôme $P \in K[x]$ peut s'écrire
$$
P = c(x - \alpha_1) \ldots (x - \alpha_n),
$$
où $c$ est le terme constant et où les $\alpha_1, \ldots, \alpha_n \in k$
sont les racines de $P$ (comptées avec multiplicité). Manifestement, les seuls polynômes
irréductibles de $K[x]$ sont les polynômes de degré un $c(x - \alpha)$,
$c, \alpha \in K$ (avec $c \neq 0$).

\begin{definition}
```

</details>

### FR-FIELDS-B2-PROSE-0025

`definition-relatively-prime` — source 1087–1104, français 1090–1107.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1087) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Premiers entre eux signifie engendrer l'idéal unité, non être chacun irréductible. La discussion garde les deux sens du critère par racines communes sur un corps algébriquement clos, les idéaux maximaux et la transition au cas non clos. Aucune équivalence par racines dans le seul corps k n'est affirmée.

**Réserve :** Premiers entre eux et idéal unité sont justifiés par leur définition exacte ici ; ces lexèmes ne sont pas attestés dans le périmètre du cours consulté.

Choix écartés :

- Polynômes premiers pris séparément : rejeté, car le texte définit une relation entre deux polynômes.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-relatively-prime}
If $k$ is any field, we say that two polynomials in $k[x]$ are
{\it relatively prime} if they generate the unit ideal in $k[x]$.
\end{definition}

\noindent
Continuing the discussion above, if $K$ is an algebraically closed field,
two polynomials in $K[x]$ are relatively prime if and only if they have no
common roots. This follows because the maximal ideals of $K[x]$ are of the form
$(x - \alpha)$, $\alpha \in K$. So if $F, G \in K[x]$ have no common root,
then $(F, G)$ cannot be contained in any $(x - \alpha)$ (as then they would
have a common root at $\alpha$).

\medskip\noindent
If $k$ is {\it not} algebraically closed, then this still gives
information about when two polynomials in $k[x]$ generate the unit ideal.

\begin{lemma}
```

```tex
\label{definition-relatively-prime}
Si $k$ est un corps quelconque, nous disons que deux polynômes de $k[x]$ sont
{\it premiers entre eux} s'ils engendrent l'idéal unité de $k[x]$.
\end{definition}

\noindent
Poursuivons la discussion précédente. Si $K$ est un corps algébriquement clos,
deux polynômes de $K[x]$ sont premiers entre eux si et seulement s'ils n'ont aucune
racine commune. Cela résulte du fait que les idéaux maximaux de $K[x]$ sont de la forme
$(x - \alpha)$, $\alpha \in K$. Ainsi, si $F, G \in K[x]$ n'ont aucune racine commune,
alors $(F, G)$ ne peut être contenu dans aucun $(x - \alpha)$ (car ils auraient alors
une racine commune en $\alpha$).

\medskip\noindent
Si $k$ n'est {\it pas} algébriquement clos, ceci fournit encore des
informations permettant de déterminer quand deux polynômes de $k[x]$ engendrent l'idéal unité.

\begin{lemma}
```

</details>

### FR-FIELDS-B2-PROSE-0026

`lemma-relatively-prime-polynomials` — source 1105–1122, français 1108–1125.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1105) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Les racines communes sont cherchées dans une clôture algébrique. Le passage de k à sa clôture conserve la génération de (1) ; l'argument reste celui des systèmes linéaires et de leur solvabilité après extension. Il n'est ni remplacé par une preuve de Bézout développée ni amputé de sa réciproque.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-relatively-prime-polynomials}
Two polynomials in $k[x]$ are relatively prime precisely when they
have no common roots in an algebraic closure $\overline{k}$ of $k$.
\end{lemma}

\begin{proof}
The claim is that any two polynomials $P, Q$ generate $(1)$ in $k[x]$ if and
only if they generate $(1)$ in $\overline{k}[x]$. This is a piece of
linear algebra: a system of linear equations with coefficients in $k$ has
a solution if and only if it has a solution in any extension of $k$.
Consequently, we can reduce to the case of an algebraically closed field, in
which case the result is clear from what we have already proved.
\end{proof}
```

```tex
\label{lemma-relatively-prime-polynomials}
Deux polynômes de $k[x]$ sont premiers entre eux si et seulement s'ils
n'ont aucune racine commune dans une clôture algébrique $\overline{k}$ de $k$.
\end{lemma}

\begin{proof}
L'affirmation est que deux polynômes quelconques $P, Q$ engendrent $(1)$ dans $k[x]$ si et
seulement s'ils engendrent $(1)$ dans $\overline{k}[x]$. C'est une question
d'algèbre linéaire : un système d'équations linéaires à coefficients dans $k$ possède
une solution si et seulement s'il possède une solution dans une extension quelconque de $k$.
On peut par conséquent se ramener au cas d'un corps algébriquement clos ; dans
ce cas, le résultat découle clairement de ce qui précède.
\end{proof}
```

</details>

## Limites et suite

Aucune relecture humaine experte n'est revendiquée. Analyse assistée par OpenAI Codex ; l'identité exacte du modèle n'est pas attestée par ce reçu et n'est pas inventée. Les choix sans attestation externe sont justifiés par le contexte, pas présentés comme des citations. Ni le chapitre entier ni le corpus ne sont certifiés, reconstruits ou publiés.

Prochaine section : Extensions algébriques séparables, ligne officielle 1123. Ne pas recommencer les onze sections déjà comparées tant que leurs octets restent inchangés. L'ancienne édition éditorialisée demeure préservée séparément ; une traduction ultérieure de l'édition intégrée par IA exigerait son propre alignement.
