# Chapitre 9 — Corps : séparabilité, caractères et inséparabilité

**Trois sections complètes comparées, source lignes 1123–1812. Aucun nouveau changement du français. La lecture continue cumulée atteint quatorze sections, sans certifier le chapitre entier.**

[LaTeX de travail](staged/fr/009_fields.prose-batch1.fr.tex) · [Validation](FIELDS_PROSE_BATCH3_VALIDATION.json) · [Choix et paires](FIELDS_PROSE_BATCH3_CHOICES.json) · [Occurrences](FIELDS_PROSE_BATCH3_OCCURRENCES.json) · [Lot précédent](FIELDS_PROSE_BATCH2_REVIEW.fr.md)

## Étendue effective

Tous les énoncés, preuves, notes, slogans et transitions des trois sections sont lus dans les deux langues. Les 30 paires partitionnent exactement le périmètre. Les limites d'étiquettes servent de repères techniques ; la continuité de la lecture ne dépend pas d'elles.

Les 560 régions mathématiques anglaises correspondent à 561 françaises. L'écart est un unique i explicitant for some ; deux autres paires ne traduisent que du texte lecteur. L'égalité brute est donc fausse et reste déclarée telle. Après seulement ces trois exceptions exactes, toutes les régions concordent en ordre, y compris le préfixe cumulé. Le fichier cible n'a pas changé ; les inversions retrouvent exactement l'ancienne copie de travail puis le témoin public.

## Canon effectivement consulté

Marc Reversat et Benoît Zhang, [Cours de théorie des corps](https://www.math.univ-toulouse.fr/~reversat/galois.pdf), 24 mars 2003. §§3.1–3.3 complets, pages imprimées 27–35 / PDF 35–43 ; lemme 3.7.6 d'Artin et sa preuve, page imprimée 42 / PDF 50. Les pages imprimées 30, 34 et 42 ont aussi été rendues et inspectées. Les paragraphes voisins sur la normalité et la trace ne sont pas invoqués comme preuve terminologique de ce lot.

Témoin : 816199 octets, SHA-256 `73A1D0DCD0B7F11625293615E693B198C0C33BAE3A57C78A705153CE33942E8A`. [Passages et règles](FIELDS_PROSE_BATCH3_CONSULTED_CANON.json). La consultation est rétrospective, pas attribuée au traducteur initial.

Ce témoin français contient lui-même des anomalies : sigma(L) dans 3.1.1 alors que sigma est défini sur K, sens des degrés Ki-1:Ki et ni=1 dans la preuve 3.2.3, sens Ls/L et sous-indice s omis dans 3.2.4. Elles ne sont pas transférées dans Stacks. Le cours atteste degré de séparabilité, non la variante exacte degré séparable ; ses preuves n'autorisent ni à corriger la source officielle ni à certifier tous les mots français. Les choix ordinaires de syntaxe restent motivés par les paires complètes, sans citations inventées.

## Réserves visibles pour les lecteurs experts

Ces réserves ne sont pas des corrections clandestines du témoin anglais. Elles sont séparées du corps de la traduction ; aucune nouvelle admission au registre d'errata ni validation humaine n'est revendiquée.

- `lemma-irreducible-polynomials` : Source 1146–1149 : l'argument sur le degré de R ne traite pas P'=0 ; la dichotomie exige une distinction que ce paragraphe omet. Le français conserve ce défaut source, sans le déclarer mathématiquement validé.
- `definition-separable-degree` : Le canon consulté dit degré de séparabilité. La variante degré séparable est définie sans ambiguïté ici, mais n'est pas lexicalement attestée dans ces pages.
- `lemma-independence-characters` : L'unique i supplémentaire est une explicitation de l'ellipse for some. Le canon cité porte sur un groupe et E*, alors que Stacks porte sur un monoïde et L ; ne pas transférer ces restrictions.
- `lemma-finite-separable-tensor-alg-closed` : Petit argument omis reste omis. A un noyau signifie ici noyau non trivial, comme le précise la phrase suivante ; l'ellipse n'est pas un ajout de traduction.
- `section-purely-inseparable` : L'introduction dit seulement caractéristique positive ; la définition inclut ensuite L=M dans toute caractéristique. Ne pas convertir l'annonce en une nouvelle restriction de la définition.
- `lemma-take-pth-root` : La factorisation non triviale est implicite dans la preuve source. Le qualificatif n'est pas ajouté au texte de cette édition.
- `lemma-purely-inseparable-elements` : Quotient présuppose un dénominateur non nul, laissé implicite. La définition des éléments en caractéristique zéro est également moins explicite que celle des extensions.
- `lemma-separable-first` : Choix interprétatif à revoir si nécessaire : separable algebraic appliqué à P est rendu par polynôme séparable, P étant déjà typé comme polynôme. Il ne s'agit pas de remplacer une racine algébrique par un polynôme.
- `definition-insep-degree` : L'entier est incompatible avec la généralité infinie évoquée ensuite. Les deux propositions de correction restent hors du texte fidèle ; pas de nouvelle admission canonique.
- `lemma-multiplicativity-all-degrees` : La preuve du cas infini est explicitement absente. Cette lecture vérifie la fidélité française ; elle ne certifie pas la généralité mathématique annoncée.

## Trois écarts mathématiques exactement circonscrits

[Registre des exceptions avec les expressions intégrales](FIELDS_PROSE_BATCH3_MATH_EXCEPTIONS.json). Les deux traductions de texte et l’explicitation d’indice ne permettent aucune substitution générale de symboles.

### Exception 1

Renvoi au n-uplet défini ensuite : seul as below devient comme ci-dessous.

```tex
\Mor_F(K, \overline{F}) \longrightarrow \{(\beta_1, \ldots, \beta_n)\text{ as below}\}, \quad \varphi \longmapsto (\varphi(\alpha_1), \ldots, \varphi(\alpha_n))
```

```tex
\Mor_F(K, \overline{F}) \longrightarrow \{(\beta_1, \ldots, \beta_n)\text{ comme ci-dessous}\}, \quad \varphi \longmapsto (\varphi(\alpha_1), \ldots, \varphi(\alpha_n))
```

### Exception 2

Un certain i explicite le même indice de lambda_i que l'ellipse anglaise ; domaine et quantificateur inchangés.

```tex
(aucune région supplémentaire dans la source)
```

```tex
i
```

### Exception 3

La conjonction and devient et entre les deux mêmes formules.

```tex
[K : F]_s = [K : E]_s [E : F]_s \quad\text{and}\quad [K : F]_i = [K : E]_i [E : F]_i
```

```tex
[K : F]_s = [K : E]_s [E : F]_s \quad\text{et}\quad [K : F]_i = [K : E]_i [E : F]_i
```

## Règles et occurrences

### separability

Distinguer polynôme, élément et extension à chaque occurrence ; conserver leurs bases et leurs hypothèses.

Occurrences contrôlées : 58. Appui : 3.1.8 et 3.2.1–3.2.3, pp.30–32.

### derivative-roots

La dérivée est formelle ; racine multiple ne veut pas dire racine située dans plusieurs corps.

Occurrences contrôlées : 3. Appui : 3.1.6–3.1.8, pp.28–30.

### pure-inseparability

Conserver la condition de puissance p et l'exception identité ; ne pas confondre inséparable et purement inséparable.

Occurrences contrôlées : 20. Appui : 3.2.6 et 3.3.1–3.3.3, pp.33–35.

### degree-variants

Le concept est attesté, mais la variante adjectivale n'est pas citée exactement dans le canon consulté. Les définitions source et la cohérence du chapitre motivent son maintien.

Occurrences contrôlées : 8. Appui : 3.1.3, 3.1.5 et 3.2.3, pp.27–31.

### characters-independence

Caractères désigne ici des homomorphismes multiplicatifs. Le mot caractère dans caractère bien défini n'est pas une occurrence de cette règle ; les hypothèses plus larges de Stacks restent gouvernantes.

Occurrences contrôlées : 7. Appui : Lemme 3.7.6, p.42.

### extension-morphisms

Un prolongement conserve la restriction au corps précédent ; l'unicité est seulement affirmée là où la source l'affirme.

Occurrences contrôlées : 10. Appui : 3.1.1, 3.2.5, pp.27 et 33.

### monoid-scope

Le canon lu ne fournit qu'un lemme de groupes. Le terme est conservé avec la définition multiplicative explicite de la source et son utilisation de zéro ; pas d'attestation externe revendiquée.

Occurrences contrôlées : 4. Appui : contexte officiel ; attestation externe non obtenue dans ces passages.

## Toutes les paires lues

### FR-FIELDS-B3-PROSE-0001

`frontmatter` — source 1123–1123, français 1126–1126.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1123) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le titre conserve le cadre des extensions algébriques séparables ; il n'étend pas la définition aux extensions transcendantes.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\section{Separable algebraic extensions}
```

```tex
\section{Extensions algébriques séparables}
```

</details>

### FR-FIELDS-B3-PROSE-0002

`section-separable-extensions` — source 1124–1130, français 1127–1133.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1124) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Phénomène curieux traduit le commentaire introductif something funny sans lui ajouter une assertion. Le corps et la caractéristique p restent les objets annoncés.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-separable-extensions}

\noindent
In characteristic $p$ something funny happens with irreducible polynomials
over fields. We explain this in the following lemma.

\begin{lemma}
```

```tex
\label{section-separable-extensions}

\noindent
En caractéristique $p$, un phénomène curieux se produit pour les polynômes irréductibles
sur un corps. Le lemme suivant l'explique.

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0003

`lemma-irreducible-polynomials` — source 1131–1164, français 1134–1167.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1131) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Polynôme dérivé est attesté dans le canon consulté. Les deux cas, la restriction à la caractéristique positive, la puissance q et l'irréductibilité de Q sont conservés. La preuve française suit chaque étape : dérivée, coefficients, divisibilité de i par p et récurrence sur le degré. Le premier paragraphe hérite toutefois d'une lacune de l'anglais ; il n'a pas été remplacé par la preuve correcte du cours français.

**Réserve :** Source 1146–1149 : l'argument sur le degré de R ne traite pas P'=0 ; la dichotomie exige une distinction que ce paragraphe omet. Le français conserve ce défaut source, sans le déclarer mathématiquement validé.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-irreducible-polynomials}
Let $F$ be a field. Let $P \in F[x]$ be an irreducible polynomial over $F$.
Let $P' = \text{d}P/\text{d}x$ be the derivative of $P$ with respect
to $x$. Then one of the following two cases happens
\begin{enumerate}
\item $P$ and $P'$ are relatively prime, or
\item $P'$ is the zero polynomial.
\end{enumerate}
The second case can only happen if $F$ has characteristic $p > 0$.
In this case $P(x) = Q(x^q)$ where $q = p^f$ is a power of $p$ and
$Q \in F[x]$ is an irreducible polynomial such that $Q$ and $Q'$
are relatively prime.
\end{lemma}

\begin{proof}
Note that $P'$ has degree $< \deg(P)$. Hence if $P$ and $P'$ are not relatively
prime, then $(P, P') = (R)$ where $R$ is a polynomial of degree $< \deg(P)$
contradicting the irreducibility of $P$. This proves we have the dichotomy
between (1) and (2).

\medskip\noindent
Assume we are in case (2) and $P = a_d x^d + \ldots + a_0$. Then
$P' = da_d x^{d - 1} + \ldots + a_1$. In characteristic $0$ we see
that this forces $a_d, \ldots, a_1 = 0$ which would mean $P$ is constant
a contradiction. Thus we conclude that the characteristic $p$ is positive.
In this case the condition $P' = 0$ forces $a_i = 0$ whenever $p$ does
not divide $i$.
In other words, $P(x) = P_1(x^p)$ for some nonconstant polynomial $P_1$.
Clearly, $P_1$ is irreducible as well. By induction on the degree we
see that $P_1(x) = Q(x^q)$ as in the statement of the lemma, hence
$P(x) = Q(x^{pq})$ and the lemma is proved.
\end{proof}

\begin{definition}
```

```tex
\label{lemma-irreducible-polynomials}
Soit $F$ un corps. Soit $P \in F[x]$ un polynôme irréductible sur $F$.
Soit $P' = \text{d}P/\text{d}x$ le polynôme dérivé de $P$ par rapport
à $x$. L'un des deux cas suivants se produit :
\begin{enumerate}
\item $P$ et $P'$ sont premiers entre eux, ou
\item $P'$ est le polynôme nul.
\end{enumerate}
Le second cas ne peut se produire que si $F$ est de caractéristique $p > 0$.
Dans ce cas, $P(x) = Q(x^q)$, où $q = p^f$ est une puissance de $p$ et
$Q \in F[x]$ un polynôme irréductible tel que $Q$ et $Q'$ soient
premiers entre eux.
\end{lemma}

\begin{proof}
Remarquons que $P'$ est de degré $< \deg(P)$. Par conséquent, si $P$ et $P'$ ne sont pas premiers
entre eux, alors $(P, P') = (R)$, où $R$ est un polynôme de degré $< \deg(P)$,
ce qui contredit l'irréductibilité de $P$. Cela établit la dichotomie
entre (1) et (2).

\medskip\noindent
Supposons que nous soyons dans le cas (2) et que $P = a_d x^d + \ldots + a_0$. Alors
$P' = da_d x^{d - 1} + \ldots + a_1$. En caractéristique $0$, on voit
que cela impose $a_d, \ldots, a_1 = 0$, ce qui signifierait que $P$ est constant,
une contradiction. On conclut donc que la caractéristique $p$ est positive.
Dans ce cas, la condition $P' = 0$ impose $a_i = 0$ chaque fois que $p$ ne
divise pas $i$.
Autrement dit, $P(x) = P_1(x^p)$ pour un certain polynôme non constant $P_1$.
Manifestement, $P_1$ est lui aussi irréductible. Par récurrence sur le degré, on
voit que $P_1(x) = Q(x^q)$ comme dans l'énoncé du lemme ; ainsi
$P(x) = Q(x^{pq})$, et le lemme est démontré.
\end{proof}

\begin{definition}
```

</details>

### FR-FIELDS-B3-PROSE-0004

`definition-separable` — source 1165–1186, français 1168–1189.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1165) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Les trois objets sont distingués : polynôme irréductible, élément algébrique, extension algébrique. La note excluant cette définition pour les extensions non algébriques et ses deux références restent complètes. La conséquence en caractéristique zéro conserve ses trois assertions. Le cours français définit aussi la séparabilité des polynômes non irréductibles ; cette généralité n'est pas importée ici.

Choix écartés :

- Supprimer irréductible pour suivre le cours français : rejeté, car cela élargirait cette définition officielle.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-separable}
Let $F$ be a field. Let $K/F$ be an extension of fields.
\begin{enumerate}
\item We say an irreducible polynomial $P$ over $F$ is {\it separable}
if it is relatively prime to its derivative.
\item Given $\alpha \in K$ algebraic over $F$ we say $\alpha$ is
{\it separable} over $F$ if its minimal polynomial is separable over $F$.
\item If $K$ is an algebraic extension of $F$, we say $K$ is
{\it separable}\footnote{For nonalgebraic extensions
this definition does not make sense and is not the correct one. We refer
the reader to Algebra, Sections \ref{algebra-section-separability} and
\ref{algebra-section-separability-continued}.}
over $F$ if every element of $K$ is separable over $F$.
\end{enumerate}
\end{definition}

\noindent
By Lemma \ref{lemma-irreducible-polynomials} in characteristic $0$ every
irreducible polynomial is separable, every algebraic element in an extension
is separable, and every algebraic extension is separable.

\begin{lemma}
```

```tex
\label{definition-separable}
Soit $F$ un corps. Soit $K/F$ une extension de corps.
\begin{enumerate}
\item On dit qu'un polynôme irréductible $P$ sur $F$ est {\it séparable}
s'il est premier avec son polynôme dérivé.
\item Étant donné $\alpha \in K$ algébrique sur $F$, on dit que $\alpha$ est
{\it séparable} sur $F$ si son polynôme minimal est séparable sur $F$.
\item Si $K$ est une extension algébrique de $F$, on dit que $K$ est
{\it séparable}\footnote{Pour les extensions non algébriques,
cette définition n'a pas de sens et n'est pas la bonne. Nous renvoyons
le lecteur à Algèbre, sections \ref{algebra-section-separability} et
\ref{algebra-section-separability-continued}.}
sur $F$ si tout élément de $K$ est séparable sur $F$.
\end{enumerate}
\end{definition}

\noindent
D'après le Lemme \ref{lemma-irreducible-polynomials}, en caractéristique $0$, tout
polynôme irréductible est séparable, tout élément algébrique d'une extension
est séparable et toute extension algébrique est séparable.

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0005

`lemma-separable-goes-up` — source 1187–1206, français 1190–1209.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1187) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

La tour K/E/F reste algébrique ; la base passe de F à E dans les deux clauses. Les polynômes minimaux P et Q, la factorisation, la dérivée et la contradiction implicite avec la séparabilité de P sont identiques. La seconde assertion demeure une conséquence immédiate, non une nouvelle preuve.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-separable-goes-up}
Let $K/E/F$ be a tower of algebraic field extensions.
\begin{enumerate}
\item If $\alpha \in K$ is separable over $F$, then $\alpha$ is separable
over $E$.
\item if $K$ is separable over $F$, then $K$ is separable over $E$.
\end{enumerate}
\end{lemma}

\begin{proof}
We will use Lemma \ref{lemma-irreducible-polynomials} without further mention.
Let $P$ be the minimal polynomial of $\alpha$ over $F$.
Let $Q$ be the minimal polynomial of $\alpha$ over $E$.
Then $Q$ divides $P$ in the polynomial ring $E[x]$, say $P = QR$.
Then $P' = Q'R + QR'$. Thus if $Q' = 0$, then $Q$ divides $P$ and $P'$
hence $P' = 0$ by the lemma. This proves (1). Part (2)
follows immediately from (1) and the definitions.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-separable-goes-up}
Soit $K/E/F$ une tour d'extensions algébriques de corps.
\begin{enumerate}
\item Si $\alpha \in K$ est séparable sur $F$, alors $\alpha$ est séparable
sur $E$.
\item Si $K$ est séparable sur $F$, alors $K$ est séparable sur $E$.
\end{enumerate}
\end{lemma}

\begin{proof}
Nous utiliserons le Lemme \ref{lemma-irreducible-polynomials} sans le mentionner davantage.
Soit $P$ le polynôme minimal de $\alpha$ sur $F$.
Soit $Q$ le polynôme minimal de $\alpha$ sur $E$.
Alors $Q$ divise $P$ dans l'anneau de polynômes $E[x]$, disons $P = QR$.
Alors $P' = Q'R + QR'$. Ainsi, si $Q' = 0$, alors $Q$ divise $P$ et $P'$,
donc $P' = 0$ d'après le lemme. Ceci démontre (1). L'assertion (2)
découle immédiatement de (1) et des définitions.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0006

`lemma-recognize-separable` — source 1207–1224, français 1210–1227.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1207) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Racines deux à deux distinctes et racine multiple expriment exactement les deux situations. Chaque sens de l'équivalence est conservé : dérivation de P=(x-alpha)Q, racine commune de P et P', puis divisibilité par le carré. La référence aux polynômes premiers entre eux garde son rôle.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-recognize-separable}
Let $F$ be a field. An irreducible polynomial $P$ over $F$
is separable if and only if $P$ has pairwise distinct roots in an
algebraic closure of $F$.
\end{lemma}

\begin{proof}
Suppose that $\alpha \in \overline{F}$ is a root of both $P$ and $P'$.
Then $P = (x - \alpha)Q$ for some polynomial $Q$. Taking derivatives
we obtain $P' = Q + (x - \alpha)Q'$. Thus $\alpha$ is a root of $Q$.
Hence we see that if $P$ and $P'$ have a common root, then $P$
does not have pairwise distinct roots. Conversely, if $P$ has
a repeated root, i.e., $(x - \alpha)^2$ divides $P$, then $\alpha$
is a root of both $P$ and $P'$. Combined with
Lemma \ref{lemma-relatively-prime-polynomials} this proves the lemma.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-recognize-separable}
Soit $F$ un corps. Un polynôme irréductible $P$ sur $F$
est séparable si et seulement si $P$ possède des racines deux à deux distinctes dans une
clôture algébrique de $F$.
\end{lemma}

\begin{proof}
Supposons que $\alpha \in \overline{F}$ soit une racine à la fois de $P$ et de $P'$.
Alors $P = (x - \alpha)Q$ pour un certain polynôme $Q$. En dérivant,
nous obtenons $P' = Q + (x - \alpha)Q'$. Ainsi $\alpha$ est une racine de $Q$.
On voit donc que si $P$ et $P'$ ont une racine commune, alors $P$
ne possède pas de racines deux à deux distinctes. Réciproquement, si $P$ possède
une racine multiple, c'est-à-dire si $(x - \alpha)^2$ divise $P$, alors $\alpha$
est une racine à la fois de $P$ et de $P'$. Conjointement avec le
Lemme \ref{lemma-relatively-prime-polynomials}, ceci démontre le lemme.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0007

`lemma-nr-roots-unchanged` — source 1225–1255, français 1228–1258.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1225) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le cardinal ne compte pas les multiplicités. Surjectivité par clôture algébrique et injectivité de la puissance p sont distinguées, avec l'argument du corps sans nilpotent. La transition P=Q(x^q), le cas de caractéristique zéro, la note 0^0=1 et le nombre de racines égal au degré de Q sont tous conservés.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-nr-roots-unchanged}
Let $F$ be a field and let $\overline{F}$ be an algebraic closure of $F$.
Let $p > 0$ be the characteristic of $F$. Let $P$ be a polynomial
over $F$. Then the set of roots of $P$ and $P(x^p)$ in $\overline{F}$
have the same cardinality (not counting multiplicity).
\end{lemma}

\begin{proof}
Clearly, $\alpha$ is a root of $P(x^p)$ if and only if $\alpha^p$ is a
root of $P$. In other words, the roots of $P(x^p)$ are the roots of
$x^p - \beta$, where $\beta$ is a root of $P$. Thus it suffices to show
that the map $\overline{F} \to \overline{F}$, $\alpha \mapsto \alpha^p$
is bijective. It is surjective, as $\overline{F}$ is algebraically closed
which means that every element has a $p$th root. It is injective because
$\alpha^p = \beta^p$ implies $(\alpha - \beta)^p = 0$ because
the characteristic is $p$. And of course in a field $x^p = 0$ implies
$x = 0$.
\end{proof}

\noindent
Let $F$ be a field and let $P$ be an irreducible polynomial over $F$.
Then we know that $P = Q(x^q)$ for some separable irreducible polynomial $Q$
(Lemma \ref{lemma-irreducible-polynomials}) where $q$ is a power of
the characteristic $p$ (and if the characteristic is zero, then
$q = 1$\footnote{A good convention for this chapter is to set $0^0 = 1$.}
and $Q = P$). By Lemma \ref{lemma-nr-roots-unchanged} the number of
roots of $P$ and $Q$ in any algebraic closure of $F$ is the same.
By Lemma \ref{lemma-recognize-separable} this number is equal to the degree
of $Q$.

\begin{definition}
```

```tex
\label{lemma-nr-roots-unchanged}
Soit $F$ un corps et soit $\overline{F}$ une clôture algébrique de $F$.
Soit $p > 0$ la caractéristique de $F$. Soit $P$ un polynôme
sur $F$. Alors les ensembles des racines de $P$ et de $P(x^p)$ dans $\overline{F}$
ont le même cardinal (sans compter les multiplicités).
\end{lemma}

\begin{proof}
Manifestement, $\alpha$ est une racine de $P(x^p)$ si et seulement si $\alpha^p$ est une
racine de $P$. Autrement dit, les racines de $P(x^p)$ sont les racines de
$x^p - \beta$, où $\beta$ est une racine de $P$. Il suffit donc de montrer
que l'application $\overline{F} \to \overline{F}$, $\alpha \mapsto \alpha^p$
est bijective. Elle est surjective, puisque $\overline{F}$ est algébriquement clos,
ce qui signifie que tout élément possède une racine $p$-ième. Elle est injective car
$\alpha^p = \beta^p$ implique $(\alpha - \beta)^p = 0$, puisque
la caractéristique est $p$. Et bien sûr, dans un corps, $x^p = 0$ implique
$x = 0$.
\end{proof}

\noindent
Soit $F$ un corps et soit $P$ un polynôme irréductible sur $F$.
Nous savons alors que $P = Q(x^q)$ pour un certain polynôme irréductible séparable $Q$
(Lemme \ref{lemma-irreducible-polynomials}), où $q$ est une puissance de
la caractéristique $p$ (et, si la caractéristique est nulle, alors
$q = 1$\footnote{Une bonne convention pour ce chapitre consiste à poser $0^0 = 1$.}
et $Q = P$). D'après le Lemme \ref{lemma-nr-roots-unchanged}, le nombre de
racines de $P$ et de $Q$ dans toute clôture algébrique de $F$ est le même.
D'après le Lemme \ref{lemma-recognize-separable}, ce nombre est égal au degré
de $Q$.

\begin{definition}
```

</details>

### FR-FIELDS-B3-PROSE-0008

`definition-separable-degree` — source 1256–1268, français 1259–1271.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1256) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le degré séparable du polynôme reste le cardinal des racines, indépendant du choix de clôture. La divisibilité et le quotient puissance de la caractéristique restent exactement ceux de l'anglais. Le cours atteste degré de séparabilité ; degré séparable est ici une variante conservée pour cohérence, non une citation lexicale exacte de ce cours.

**Réserve :** Le canon consulté dit degré de séparabilité. La variante degré séparable est définie sans ambiguïté ici, mais n'est pas lexicalement attestée dans ces pages.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-separable-degree}
Let $F$ be a field. Let $P$ be an irreducible polynomial over $F$.
The {\it separable degree} of $P$ is the cardinality of the
set of roots of $P$ in any algebraic closure of $F$ (see discussion
above). Notation $\deg_s(P)$.
\end{definition}

\noindent
The separable degree of $P$ always divides the degree and the quotient
is a power of the characteristic. If the characteristic is zero, then
$\deg_s(P) = \deg(P)$.

\begin{situation}
```

```tex
\label{definition-separable-degree}
Soit $F$ un corps. Soit $P$ un polynôme irréductible sur $F$.
Le {\it degré séparable} de $P$ est le cardinal de
l'ensemble des racines de $P$ dans toute clôture algébrique de $F$ (voir la discussion
ci-dessus). Notation $\deg_s(P)$.
\end{definition}

\noindent
Le degré séparable de $P$ divise toujours son degré, et le quotient
est une puissance de la caractéristique. Si la caractéristique est nulle, alors
$\deg_s(P) = \deg(P)$.

\begin{situation}
```

</details>

### FR-FIELDS-B3-PROSE-0009

`situation-finitely-generated` — source 1269–1290, français 1272–1293.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1269) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Les générateurs alpha_i définissent la même tour finie et P_i reste minimal sur K_{i-1}. Les restrictions phi_i et le transport des coefficients précèdent le dénombrement. Les fautes grammaticales anglaises Here F be et Denote P_i sont rendues par du français normal, sans modifier une hypothèse.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{situation-finitely-generated}
Here $F$ be a field and $K/F$ is a finite extension generated by elements
$\alpha_1, \ldots, \alpha_n \in K$. We set $K_0 = F$ and
$$
K_i = F(\alpha_1, \ldots, \alpha_i)
$$
to obtain a tower of finite extensions
$K = K_n / K_{n - 1} / \ldots / K_0 = F$.
Denote $P_i$ the minimal polynomial of $\alpha_i$ over $K_{i - 1}$.
Finally, we fix an algebraic closure $\overline{F}$ of $F$.
\end{situation}

\noindent
Let $F$, $K$, $\alpha_i$, and $\overline{F}$ be as in
Situation \ref{situation-finitely-generated}.
Suppose that $\varphi : K \to \overline{F}$ is a morphism of extensions
of $F$. Then we obtain maps $\varphi_i : K_i \to \overline{F}$.
The image of $P_i \in K_{i - 1}[x]$ by $\varphi_{i - 1}$
is a polynomial $P_i^{\varphi_{i - 1}} \in \overline{F}[x]$
and $\varphi(\alpha_i)$ is a root of this polynomial.

\begin{lemma}
```

```tex
\label{situation-finitely-generated}
Ici, $F$ est un corps et $K/F$ est une extension finie engendrée par des éléments
$\alpha_1, \ldots, \alpha_n \in K$. Nous posons $K_0 = F$ et
$$
K_i = F(\alpha_1, \ldots, \alpha_i)
$$
pour obtenir une tour d'extensions finies
$K = K_n / K_{n - 1} / \ldots / K_0 = F$.
Notons $P_i$ le polynôme minimal de $\alpha_i$ sur $K_{i - 1}$.
Enfin, fixons une clôture algébrique $\overline{F}$ de $F$.
\end{situation}

\noindent
Soient $F$, $K$, les $\alpha_i$ et $\overline{F}$ comme dans la
Situation \ref{situation-finitely-generated}.
Supposons que $\varphi : K \to \overline{F}$ soit un morphisme d'extensions
de $F$. Nous obtenons alors des applications $\varphi_i : K_i \to \overline{F}$.
L'image de $P_i \in K_{i - 1}[x]$ par $\varphi_{i - 1}$
est un polynôme $P_i^{\varphi_{i - 1}} \in \overline{F}[x]$
et $\varphi(\alpha_i)$ est une racine de ce polynôme.

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0010

`lemma-count-embeddings` — source 1291–1325, français 1294–1328.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1291) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

La bijection porte sur les n-uplets admissibles successifs, pas sur un produit de choix indépendants. Les images des coefficients dépendent des morphismes précédents ; existence et unicité proviennent du même quotient. Homomorphisme de F-algèbres traduit over F sans changer la catégorie. Comme ci-dessous est le seul texte lecteur traduit dans l'affichage ; les flèches et les coordonnées sont intactes.

Choix écartés :

- Un produit cartésien de tous les ensembles de racines choisis à l'avance : rejeté, puisque les polynômes transportés dépendent des choix précédents.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-count-embeddings}
In Situation \ref{situation-finitely-generated} the correspondence
$$
\Mor_F(K, \overline{F})
\longrightarrow
\{(\beta_1, \ldots, \beta_n)\text{ as below}\},
\quad
\varphi \longmapsto (\varphi(\alpha_1), \ldots, \varphi(\alpha_n))
$$
is a bijection. Here the right hand side is the set of $n$-tuples
$(\beta_1, \ldots, \beta_n)$ of elements of $\overline{F}$ having
the following property:
\begin{enumerate}
\item $\beta_1 \in \overline{F}$ is a root of $P_1$;
let $\varphi_1 : K_1 \to \overline{F}$ be the homomorphism
over $F$ sending $\alpha_1$ to $\beta_1$,
\item $\beta_2 \in \overline{F}$ is a root of $P_2^{\varphi_1}$;
let $\varphi_2 : K_2 \to \overline{F}$ be the homomorphism
extending $\varphi_1$ sending $\alpha_2$ to $\beta_2$,
\item and so on until,
\item $\beta_n \in \overline{F}$ is a root of $P_n^{\varphi_{n - 1}}$.
\end{enumerate}
In each step the homorphism $\varphi_i$ exists and is unique because
$K_i = K_{i - 1}[x]/(P_i)$ and $\beta_i$ is a root of $P_i^{\varphi_{i - 1}}$.
\end{lemma}

\begin{proof}
The map from left to right is discussed above the lemma.
Let $(\beta_1, \ldots, \beta_n)$ be an element of the right hand side.
Then we let $\varphi : K = K_n \to \overline{F}$ be the unique homorphism
extending $\varphi_{n - 1}$ sending $\alpha_n$ to $\beta_n$.
Uniqueness implies that the two constructions are mutually inverse.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-count-embeddings}
Dans la Situation \ref{situation-finitely-generated}, la correspondance
$$
\Mor_F(K, \overline{F})
\longrightarrow
\{(\beta_1, \ldots, \beta_n)\text{ comme ci-dessous}\},
\quad
\varphi \longmapsto (\varphi(\alpha_1), \ldots, \varphi(\alpha_n))
$$
est une bijection. Ici, le membre de droite est l'ensemble des $n$-uplets
$(\beta_1, \ldots, \beta_n)$ d'éléments de $\overline{F}$ possédant
la propriété suivante :
\begin{enumerate}
\item $\beta_1 \in \overline{F}$ est une racine de $P_1$ ;
soit $\varphi_1 : K_1 \to \overline{F}$ l'homomorphisme
de $F$-algèbres qui envoie $\alpha_1$ sur $\beta_1$,
\item $\beta_2 \in \overline{F}$ est une racine de $P_2^{\varphi_1}$ ;
soit $\varphi_2 : K_2 \to \overline{F}$ l'homomorphisme
qui prolonge $\varphi_1$ et envoie $\alpha_2$ sur $\beta_2$,
\item et ainsi de suite jusqu'au dernier cas,
\item $\beta_n \in \overline{F}$ est une racine de $P_n^{\varphi_{n - 1}}$.
\end{enumerate}
À chaque étape, l'homomorphisme $\varphi_i$ existe et est unique, car
$K_i = K_{i - 1}[x]/(P_i)$ et $\beta_i$ est une racine de $P_i^{\varphi_{i - 1}}$.
\end{lemma}

\begin{proof}
L'application de gauche à droite a été décrite avant le lemme.
Soit $(\beta_1, \ldots, \beta_n)$ un élément du membre de droite.
Nous définissons alors $\varphi : K = K_n \to \overline{F}$ comme l'unique homomorphisme
qui prolonge $\varphi_{n - 1}$ et envoie $\alpha_n$ sur $\beta_n$.
L'unicité implique que les deux constructions sont inverses l'une de l'autre.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0011

`lemma-count-embeddings-explicitly` — source 1326–1342, français 1329–1345.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1326) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le produit des degrés séparables et le renvoi à la bijection sont conservés. L'usage implicite du caractère bien défini du degré est expressément maintenu ; la transition vers la caractérisation des extensions séparables n'est pas supprimée.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-count-embeddings-explicitly}
In Situation \ref{situation-finitely-generated} we have
$|\Mor_F(K, \overline{F})| = \prod_{i = 1}^n \deg_s(P_i)$.
\end{lemma}

\begin{proof}
This follows immediately from Lemma \ref{lemma-count-embeddings}.
Observe that a key ingredient we are tacitly using here is the
well-definedness of the separable degree of an irreducible polynomial
which was observed just prior to
Definition \ref{definition-separable-degree}.
\end{proof}

\noindent
We now use the result above to characterize separable field extensions.

\begin{lemma}
```

```tex
\label{lemma-count-embeddings-explicitly}
Dans la Situation \ref{situation-finitely-generated}, nous avons
$|\Mor_F(K, \overline{F})| = \prod_{i = 1}^n \deg_s(P_i)$.
\end{lemma}

\begin{proof}
Ceci découle immédiatement du Lemme \ref{lemma-count-embeddings}.
Remarquons qu'un ingrédient essentiel que nous utilisons ici implicitement est le
caractère bien défini du degré séparable d'un polynôme irréductible,
qui a été constaté juste avant la
Définition \ref{definition-separable-degree}.
\end{proof}

\noindent
Nous utilisons maintenant le résultat précédent pour caractériser les extensions de corps séparables.

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0012

`lemma-separably-generated-separable` — source 1343–1383, français 1346–1386.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1343) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Chaque générateur est testé sur le corps précédent, non seulement sur F. L'égalité et l'inégalité stricte, les produits de degrés et le changement de famille génératrice commençant par gamma sont tous présents. Les deux parties déjà démontrées sont invoquées dans le même ordre ; aucune hypothèse de séparabilité de K n'est utilisée circulairement.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-separably-generated-separable}
Assumptions and notation as in Situation \ref{situation-finitely-generated}.
If each $P_i$ is separable, i.e., each $\alpha_i$ is separable over
$K_{i - 1}$, then
$$
|\Mor_F(K, \overline{F})| = [K : F]
$$
and the field extension $K/F$ is separable. If one of the $\alpha_i$ is
not separable over $K_{i - 1}$, then
$|\Mor_F(K, \overline{F})| < [K : F]$.
\end{lemma}

\begin{proof}
If $\alpha_i$ is separable over $K_{i - 1}$ then
$\deg_s(P_i) = \deg(P_i) = [K_i : K_{i - 1}]$
(last equality by Lemma \ref{lemma-degree-minimal-polynomial}).
By multiplicativity (Lemma \ref{lemma-multiplicativity-degrees}) we have
$$
[K : F] = \prod [K_i : K_{i - 1}] = \prod \deg(P_i) =
\prod \deg_s(P_i) = |\Mor_F(K, \overline{F})|
$$
where the last equality is Lemma \ref{lemma-count-embeddings-explicitly}.
By the exact same argument we get the strict inequality
$|\Mor_F(K, \overline{F})| < [K : F]$ if one of the $\alpha_i$ is
not separable over $K_{i - 1}$.

\medskip\noindent
Finally, assume again that each $\alpha_i$ is separable over $K_{i - 1}$.
We will show $K/F$ is separable.
Let $\gamma = \gamma_1 \in K$ be arbitrary. Then we can find additional
elements $\gamma_2, \ldots, \gamma_m$ such that
$K = F(\gamma_1, \ldots, \gamma_m)$ (for example we could take
$\gamma_2 = \alpha_1, \ldots, \gamma_{n + 1} = \alpha_n$).
Then we see by the last part of the lemma (already proven above)
that if $\gamma$ is not separable over $F$ we would have the
strict inequality $|\Mor_F(K, \overline{F})| < [K : F]$
contradicting the very first part of the lemma (already prove above
as well).
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-separably-generated-separable}
Hypothèses et notations comme dans la Situation \ref{situation-finitely-generated}.
Si chaque $P_i$ est séparable, c'est-à-dire si chaque $\alpha_i$ est séparable sur
$K_{i - 1}$, alors
$$
|\Mor_F(K, \overline{F})| = [K : F]
$$
et l'extension de corps $K/F$ est séparable. Si l'un des $\alpha_i$ n'est
pas séparable sur $K_{i - 1}$, alors
$|\Mor_F(K, \overline{F})| < [K : F]$.
\end{lemma}

\begin{proof}
Si $\alpha_i$ est séparable sur $K_{i - 1}$, alors
$\deg_s(P_i) = \deg(P_i) = [K_i : K_{i - 1}]$
(la dernière égalité résultant du Lemme \ref{lemma-degree-minimal-polynomial}).
Par multiplicativité (Lemme \ref{lemma-multiplicativity-degrees}), nous avons
$$
[K : F] = \prod [K_i : K_{i - 1}] = \prod \deg(P_i) =
\prod \deg_s(P_i) = |\Mor_F(K, \overline{F})|
$$
où la dernière égalité est le Lemme \ref{lemma-count-embeddings-explicitly}.
Par exactement le même raisonnement, nous obtenons l'inégalité stricte
$|\Mor_F(K, \overline{F})| < [K : F]$ si l'un des $\alpha_i$ n'est
pas séparable sur $K_{i - 1}$.

\medskip\noindent
Supposons enfin, à nouveau, que chaque $\alpha_i$ soit séparable sur $K_{i - 1}$.
Nous allons montrer que $K/F$ est séparable.
Soit $\gamma = \gamma_1 \in K$ quelconque. Nous pouvons alors trouver des éléments supplémentaires
$\gamma_2, \ldots, \gamma_m$ tels que
$K = F(\gamma_1, \ldots, \gamma_m)$ (nous pourrions par exemple prendre
$\gamma_2 = \alpha_1, \ldots, \gamma_{n + 1} = \alpha_n$).
La dernière partie du lemme (déjà démontrée ci-dessus) montre alors
que si $\gamma$ n'était pas séparable sur $F$, nous aurions l'inégalité
stricte $|\Mor_F(K, \overline{F})| < [K : F]$,
en contradiction avec la toute première partie du lemme (elle aussi déjà démontrée
ci-dessus).
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0013

`lemma-separable-equality` — source 1384–1408, français 1387–1411.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1384) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

L'extension est finie et la cible une clôture algébrique. Les deux sens de l'égalité sont conservés : choisir une famille génératrice et permettre que son premier élément soit arbitraire. Choisir une base demeure un exemple de famille, non une hypothèse supplémentaire.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-separable-equality}
Let $K/F$ be a finite extension of fields. Let $\overline{F}$ be an
algebraic closure of $F$. Then we have
$$
|\Mor_F(K, \overline{F})| \leq [K : F]
$$
with equality if and only if $K$ is separable over $F$.
\end{lemma}

\begin{proof}
This is a corollary of Lemma \ref{lemma-separably-generated-separable}.
Namely, since $K/F$ is finite we can find finitely many elements
$\alpha_1, \ldots, \alpha_n \in K$ generating $K$ over $F$ (for example
we can choose the $\alpha_i$ to be a basis of $K$ over $F$).
If $K/F$ is separable, then each $\alpha_i$ is separable over
$F(\alpha_1, \ldots, \alpha_{i - 1})$ by Lemma \ref{lemma-separable-goes-up}
and we get equality by Lemma \ref{lemma-separably-generated-separable}.
On the other hand, if we have equality, then no matter how we choose
$\alpha_1, \ldots, \alpha_n$ we get that $\alpha_1$ is separable over
$F$ by Lemma \ref{lemma-separably-generated-separable}. Since we
can start the sequence with an arbitrary element of $K$ it follows
that $K$ is separable over $F$.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-separable-equality}
Soit $K/F$ une extension finie de corps. Soit $\overline{F}$ une
clôture algébrique de $F$. Nous avons alors
$$
|\Mor_F(K, \overline{F})| \leq [K : F]
$$
avec égalité si et seulement si $K$ est séparable sur $F$.
\end{lemma}

\begin{proof}
C'est un corollaire du Lemme \ref{lemma-separably-generated-separable}.
En effet, puisque $K/F$ est finie, nous pouvons trouver un nombre fini d'éléments
$\alpha_1, \ldots, \alpha_n \in K$ qui engendrent $K$ sur $F$ (nous pouvons par exemple
choisir les $\alpha_i$ de manière à former une base de $K$ sur $F$).
Si $K/F$ est séparable, alors chaque $\alpha_i$ est séparable sur
$F(\alpha_1, \ldots, \alpha_{i - 1})$ d'après le Lemme \ref{lemma-separable-goes-up},
et le Lemme \ref{lemma-separably-generated-separable} donne l'égalité.
Réciproquement, si nous avons l'égalité, alors, quelle que soit la manière de choisir
$\alpha_1, \ldots, \alpha_n$, le Lemme \ref{lemma-separably-generated-separable}
montre que $\alpha_1$ est séparable sur $F$. Comme nous pouvons
commencer la suite par un élément arbitraire de $K$, il s'ensuit
que $K$ est séparable sur $F$.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0014

`lemma-separable-permanence` — source 1409–1434, français 1412–1437.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1409) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

La transitivité garde les extensions algébriques E/k et F/E. Les coefficients du polynôme minimal engendrent la même sous-extension finie ; les deux justifications, irréductibilité sur le corps plus petit et séparabilité, restent distinctes. Le mot algébrique qualifie les éléments et les extensions aux mêmes endroits.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-separable-permanence}
Let $E/k$ and $F/E$ be separable algebraic extensions of fields. Then $F/k$
is a separable extension of fields.
\end{lemma}

\begin{proof}
Choose $\alpha \in F$. Then $\alpha$ is separable algebraic over $E$.
Let $P = x^d + \sum_{i < d} a_i x^i$ be the minimal polynomial of
$\alpha$ over $E$. Each $a_i$ is separable algebraic over $k$.
Consider the tower of fields
$$
k \subset k(a_0) \subset k(a_0, a_1) \subset \ldots \subset
k(a_0, \ldots, a_{d - 1}) \subset k(a_0, \ldots, a_{d - 1}, \alpha)
$$
Because $a_i$ is separable algebraic over $k$ it is separable algebraic
over $k(a_0, \ldots, a_{i - 1})$ by Lemma \ref{lemma-separable-goes-up}.
Finally, $\alpha$ is separable algebraic over $k(a_0, \ldots, a_{d - 1})$
because it is a root of $P$ which is irreducible
(as it is irreducible over the possibly bigger field $E$)
and separable (as it is separable over $E$).
Thus $k(a_0, \ldots, a_{d - 1}, \alpha)$ is separable over $k$
by Lemma \ref{lemma-separably-generated-separable}
and we conclude that $\alpha$ is separable over $k$ as desired.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-separable-permanence}
Soient $E/k$ et $F/E$ des extensions algébriques séparables de corps. Alors $F/k$
est une extension séparable de corps.
\end{lemma}

\begin{proof}
Choisissons $\alpha \in F$. Alors $\alpha$ est algébrique séparable sur $E$.
Soit $P = x^d + \sum_{i < d} a_i x^i$ le polynôme minimal de
$\alpha$ sur $E$. Chaque $a_i$ est algébrique séparable sur $k$.
Considérons la tour de corps
$$
k \subset k(a_0) \subset k(a_0, a_1) \subset \ldots \subset
k(a_0, \ldots, a_{d - 1}) \subset k(a_0, \ldots, a_{d - 1}, \alpha)
$$
Puisque $a_i$ est algébrique séparable sur $k$, il est algébrique séparable
sur $k(a_0, \ldots, a_{i - 1})$ d'après le Lemme \ref{lemma-separable-goes-up}.
Enfin, $\alpha$ est algébrique séparable sur $k(a_0, \ldots, a_{d - 1})$
car c'est une racine de $P$, qui est irréductible
(puisqu'il est irréductible sur le corps éventuellement plus grand $E$)
et séparable (puisqu'il est séparable sur $E$).
Ainsi $k(a_0, \ldots, a_{d - 1}, \alpha)$ est séparable sur $k$
d'après le Lemme \ref{lemma-separably-generated-separable},
et nous concluons que $\alpha$ est séparable sur $k$, comme voulu.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0015

`lemma-separable-elements` — source 1435–1452, français 1438–1452.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1435) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Aucune hypothèse nouvelle d'algébricité de E/k n'est ajoutée. Les éléments dits séparables sont algébriques par la définition déjà donnée. La preuve passe par k(alpha,beta) et n=2 comme l'anglais ; elle ne remplace pas cette brièveté par des vérifications de fermeture ajoutées.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-separable-elements}
Let $E/k$ be a field extension. Then the elements of $E$ separable
over $k$ form a subextension of $E/k$.
\end{lemma}

\begin{proof}
Let $\alpha, \beta \in E$ be separable over $k$. Then $\beta$ is separable
over $k(\alpha)$ by Lemma \ref{lemma-separable-goes-up}.
By Lemma \ref{lemma-separably-generated-separable} (applied with $n = 2$,
$\alpha_1 = \alpha$, and $\alpha_2 = \beta$) we see that
$k(\alpha, \beta)$ is separable over $k$.
\end{proof}





\section{Linear independence of characters}
```

```tex
\label{lemma-separable-elements}
Soit $E/k$ une extension de corps. Alors les éléments de $E$ séparables
sur $k$ forment une sous-extension de $E/k$.
\end{lemma}

\begin{proof}

Soient $\alpha, \beta \in E$ séparables sur $k$. Alors $\beta$ est séparable
sur $k(\alpha)$ d'après le Lemme \ref{lemma-separable-goes-up}.
Le Lemme \ref{lemma-separably-generated-separable} (appliqué avec $n = 2$,
$\alpha_1 = \alpha$ et $\alpha_2 = \beta$) montre que
$k(\alpha, \beta)$ est séparable sur $k$.

\end{proof}
\section{Indépendance linéaire des caractères}
```

</details>

### FR-FIELDS-B3-PROSE-0016

`section-independence-characters` — source 1453–1458, français 1453–1458.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1453) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le titre indépendance linéaire des caractères correspond au contenu. La brève transition est conservée. Le lemme d'Artin du canon français atteste caractères et linéairement indépendants, mais sa formulation pour les groupes ne réduit pas le cadre des monoïdes de Stacks.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-independence-characters}

\noindent
Here is the statement.

\begin{lemma}
```

```tex
\label{section-independence-characters}

\noindent
Voici l'énoncé.

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0017

`lemma-independence-characters` — source 1459–1499, français 1459–1499.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1459) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

G reste un monoïde et L le monoïde multiplicatif entier : on ne remplace ni G par un groupe ni L par L*. Distincts deux à deux et coefficients non tous nuls gardent leur portée. Toute la récurrence, la normalisation lambda_n=-1, le choix arbitraire de h et la soustraction sont conservés. Un certain i explicite seulement l'indice déjà elliptique dans for some ; l'unique région mathématique supplémentaire i est identifiée et justifiée, non effacée du diagnostic brut.

**Réserve :** L'unique i supplémentaire est une explicitation de l'ellipse for some. Le canon cité porte sur un groupe et E*, alors que Stacks porte sur un monoïde et L ; ne pas transférer ces restrictions.

Choix écartés :

- Remplacer monoïde par groupe ou L par L* : rejeté ; la formulation de Stacks est volontairement plus générale.
- Supprimer i pour obtenir une égalité mécanique du nombre de formules : rejeté ; cet indice restitue une ellipse grammaticale sans modifier le quantificateur.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-independence-characters}
Let $L$ be a field. Let $G$ be a monoid, for example a group. Let
$\chi_1, \ldots, \chi_n : G \to L$ be pairwise distinct
homomorphisms of monoids where $L$ is regarded as a monoid
by multiplication. Then $\chi_1, \ldots, \chi_n$
are $L$-linearly independent: if $\lambda_1, \ldots, \lambda_n \in L$
not all zero, then $\sum \lambda_i\chi_i(g) \not = 0$
for some $g \in G$.
\end{lemma}

\begin{proof}
If $n = 1$ this is true because $\chi_1(e) = 1$ if $e \in G$ is the
neutral (identity) element. We prove the result by induction for $n > 1$.
Suppose that $\lambda_1, \ldots, \lambda_n \in L$ not all zero.
If $\lambda_i = 0$ for some, then we win by induction on $n$.
Since we want to show that $\sum \lambda_i\chi_i(g) \not = 0$
for some $g \in G$ we may after dividing by $-\lambda_n$
assume that $\lambda_n = -1$. Then the only way we get in trouble
is if
$$
\chi_n(g) = \sum\nolimits_{i = 1, \ldots, n - 1} \lambda_i\chi_i(g)
$$
for all $g \in G$. Fix $h \in G$. Then we would also get
\begin{align*}
\chi_n(h)\chi_n(g) & = \chi_n(hg) \\
& = \sum\nolimits_{i = 1, \ldots, n - 1} \lambda_i\chi_i(hg) \\
& = \sum\nolimits_{i = 1, \ldots, n - 1} \lambda_i\chi_i(h) \chi_i(g)
\end{align*}
Multiplying the previous relation by $\chi_n(h)$ and subtracting we obtain
$$
0 = \sum\nolimits_{i = 1, \ldots, n - 1}
\lambda_i (\chi_n(h) - \chi_i(h)) \chi_i(g)
$$
for all $g \in G$. Since $\lambda_i \not = 0$ we conclude that
$\chi_n(h) = \chi_i(h)$ for all $i$ by induction.
The choice of $h$ above was arbitrary, so we conclude
that $\chi_i = \chi_n$ for $i \leq n - 1$ which contradicts
the assumption that our characters $\chi_i$ are pairwise distinct.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-independence-characters}
Soit $L$ un corps. Soit $G$ un monoïde, par exemple un groupe.
Soient
$\chi_1, \ldots, \chi_n : G \to L$ des homomorphismes de monoïdes deux à deux
distincts, où $L$ est considéré comme un monoïde pour la multiplication.
Alors $\chi_1, \ldots, \chi_n$ sont linéairement indépendants sur $L$ :
si $\lambda_1, \ldots, \lambda_n \in L$ ne sont pas tous nuls, alors
$\sum \lambda_i\chi_i(g) \not = 0$ pour un certain $g \in G$.
\end{lemma}

\begin{proof}
Si $n = 1$, cela résulte de $\chi_1(e) = 1$, où $e \in G$ est l'élément
neutre (identité). Nous démontrons le résultat par récurrence pour $n > 1$.
Supposons que $\lambda_1, \ldots, \lambda_n \in L$ ne soient pas tous nuls.
Si $\lambda_i = 0$ pour un certain $i$, le résultat découle de la récurrence sur $n$.
Puisque nous voulons montrer que $\sum \lambda_i\chi_i(g) \not = 0$
pour un certain $g \in G$, nous pouvons, après division par $-\lambda_n$,
supposer que $\lambda_n = -1$. La seule difficulté possible
surviendrait si
$$
\chi_n(g) = \sum\nolimits_{i = 1, \ldots, n - 1} \lambda_i\chi_i(g)
$$
pour tout $g \in G$. Fixons $h \in G$. Nous aurions alors également
\begin{align*}
\chi_n(h)\chi_n(g) & = \chi_n(hg) \\
& = \sum\nolimits_{i = 1, \ldots, n - 1} \lambda_i\chi_i(hg) \\
& = \sum\nolimits_{i = 1, \ldots, n - 1} \lambda_i\chi_i(h) \chi_i(g)
\end{align*}
En multipliant la relation précédente par $\chi_n(h)$ puis en soustrayant, on obtient
$$
0 = \sum\nolimits_{i = 1, \ldots, n - 1}
\lambda_i (\chi_n(h) - \chi_i(h)) \chi_i(g)
$$
pour tout $g \in G$. Comme $\lambda_i \not = 0$, la récurrence donne
$\chi_n(h) = \chi_i(h)$ pour tout $i$.
Le choix de $h$ étant arbitraire, nous en déduisons
que $\chi_i = \chi_n$ pour $i \leq n - 1$, ce qui contredit
l'hypothèse selon laquelle les caractères $\chi_i$ sont deux à deux distincts.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0018

`lemma-sums-of-powers` — source 1500–1513, français 1500–1513.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1500) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Les alpha_i ne sont pas supposés non nuls ; e peut être zéro et n est au moins un. La preuve garde le monoïde des entiers positifs ou nuls, afin de ne pas restreindre implicitement le lemme à des caractères à valeurs inversibles. La convention 0^0 déjà énoncée dans ce chapitre n'est pas réécrite.

Choix écartés :

- Ajouter alpha_i non nuls : rejeté ; la source utilise précisément le monoïde multiplicatif et admet zéro.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-sums-of-powers}
Let $L$ be a field. Let $n \geq 1$ and $\alpha_1, \ldots, \alpha_n \in L$
pairwise distinct elements of $L$. Then there exists an
$e \geq 0$ such that $\sum_{i = 1, \ldots, n} \alpha_i^e \not = 0$.
\end{lemma}

\begin{proof}
Apply linear independence of characters
(Lemma \ref{lemma-independence-characters})
to the monoid homomorphisms $\mathbf{Z}_{\geq 0} \to L$,
$e \mapsto \alpha_i^e$.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-sums-of-powers}
Soient $L$ un corps, $n \geq 1$ et $\alpha_1, \ldots, \alpha_n \in L$
des éléments deux à deux distincts de $L$. Alors il existe un
$e \geq 0$ tel que $\sum_{i = 1, \ldots, n} \alpha_i^e \not = 0$.
\end{lemma}

\begin{proof}
Appliquons l'indépendance linéaire des caractères
(Lemme \ref{lemma-independence-characters})
aux homomorphismes de monoïdes $\mathbf{Z}_{\geq 0} \to L$,
$e \mapsto \alpha_i^e$.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0019

`lemma-independence-embeddings` — source 1514–1528, français 1514–1528.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1514) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Les deux extensions sont quelconques. Les morphismes respectent F et l'indépendance est sur L ; ni finitude ni séparabilité n'est ajoutée. Les groupes des unités n'interviennent que dans la preuve par restriction.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-independence-embeddings}
Let $K/F$ and $L/F$ be field extensions. Let
$\sigma_1, \ldots, \sigma_n : K \to L$ be pairwise distinct
morphisms of $F$-extensions. Then $\sigma_1, \ldots, \sigma_n$
are $L$-linearly independent: if $\lambda_1, \ldots, \lambda_n \in L$
not all zero, then $\sum \lambda_i\sigma_i(\alpha) \not = 0$
for some $\alpha \in K$.
\end{lemma}

\begin{proof}
Apply Lemma \ref{lemma-independence-characters} to
the restrictions of $\sigma_i$ to the groups of units.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-independence-embeddings}
Soient $K/F$ et $L/F$ des extensions de corps. Soient
$\sigma_1, \ldots, \sigma_n : K \to L$ des morphismes de $F$-extensions
deux à deux distincts. Alors $\sigma_1, \ldots, \sigma_n$ sont linéairement
indépendants sur $L$ : si $\lambda_1, \ldots, \lambda_n \in L$ ne sont pas
tous nuls, alors $\sum \lambda_i\sigma_i(\alpha) \not = 0$
pour un certain $\alpha \in K$.
\end{lemma}

\begin{proof}
Appliquons le Lemme \ref{lemma-independence-characters} aux restrictions
des $\sigma_i$ aux groupes des unités.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0020

`lemma-finite-separable-tensor-alg-closed` — source 1529–1572, français 1529–1572.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1529) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

L'isomorphisme est celui de L-algèbres donné par les images des tenseurs. La preuve garde sa base, les n morphismes, le petit argument explicitement omis et les deux noyaux linéaires successifs de la matrice. La phrase a un noyau reprend l'ellipse anglaise, immédiatement précisée par les coefficients non tous nuls. L'extension de la relation à tout alpha utilise toujours les beta_j dans F ; aucun nouvel argument de décomposition n'est ajouté.

**Réserve :** Petit argument omis reste omis. A un noyau signifie ici noyau non trivial, comme le précise la phrase suivante ; l'ellipse n'est pas un ajout de traduction.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-finite-separable-tensor-alg-closed}
Let $K/F$ and $L/F$ be field extensions with
$K/F$ finite separable and $L$ algebraically closed.
Then the map
$$
K \otimes_F L
\longrightarrow
\prod\nolimits_{\sigma \in \Hom_F(K, L)} L,\quad
\alpha \otimes \beta \mapsto (\sigma(\alpha)\beta)_\sigma
$$
is an isomorphism of $L$-algebras.
\end{lemma}

\begin{proof}
Choose a basis $\alpha_1, \ldots, \alpha_n$ of $K$ as a vector space over $F$.
By Lemma \ref{lemma-separable-equality} (and a tiny omitted argument) the set
$\Hom_F(K, L)$ has $n$ elements, say $\sigma_1, \ldots, \sigma_n$.
In particular, the two sides have the same dimension $n$ as vector
spaces over $L$. Thus if the map is not an isomorphism, then it
has a kernel. In other words, there would exist
$\mu_j \in L$, $j = 1, \ldots, n$ not all zero,
with $\sum \alpha_j \otimes \mu_j$ in the kernel.
In other words, $\sum \sigma_i(\alpha_j)\mu_j = 0$ for all $i$.
This would mean the $n \times n$ matrix with entries
$\sigma_i(\alpha_j)$ is not invertible. Thus we can find
$\lambda_1, \ldots, \lambda_n \in L$ not all zero,
such that $\sum \lambda_i\sigma_i(\alpha_j) = 0$ for all $j$.
Now any element $\alpha \in K$ can be written as
$\alpha = \sum \beta_j \alpha_j$ with $\beta_j \in F$ and we would get
$$
\sum \lambda_i\sigma_i(\alpha) =
\sum \lambda_i\sigma_i(\sum \beta_j \alpha_j) =
\sum \beta_j \sum \lambda_i\sigma_i(\alpha_j) = 0
$$
which contradicts Lemma \ref{lemma-independence-embeddings}.
\end{proof}







\section{Purely inseparable extensions}
```

```tex
\label{lemma-finite-separable-tensor-alg-closed}
Soient $K/F$ et $L/F$ des extensions de corps, avec
$K/F$ finie séparable et $L$ algébriquement clos.
Alors l'application
$$
K \otimes_F L
\longrightarrow
\prod\nolimits_{\sigma \in \Hom_F(K, L)} L,\quad
\alpha \otimes \beta \mapsto (\sigma(\alpha)\beta)_\sigma
$$
est un isomorphisme de $L$-algèbres.
\end{lemma}

\begin{proof}
Choisissons une base $\alpha_1, \ldots, \alpha_n$ de $K$ comme espace vectoriel sur $F$.
D'après le Lemme \ref{lemma-separable-equality} (et un petit argument omis), l'ensemble
$\Hom_F(K, L)$ possède $n$ éléments, disons $\sigma_1, \ldots, \sigma_n$.
En particulier, les deux membres ont la même dimension $n$ comme espaces
vectoriels sur $L$. Ainsi, si l'application n'est pas un isomorphisme, elle
a un noyau. Autrement dit, il existerait des
$\mu_j \in L$, $j = 1, \ldots, n$, non tous nuls,
tels que $\sum \alpha_j \otimes \mu_j$ appartienne au noyau.
Autrement dit, $\sum \sigma_i(\alpha_j)\mu_j = 0$ pour tout $i$.
Cela signifierait que la matrice $n \times n$ de coefficients
$\sigma_i(\alpha_j)$ n'est pas inversible. Nous pouvons donc trouver
$\lambda_1, \ldots, \lambda_n \in L$, non tous nuls,
tels que $\sum \lambda_i\sigma_i(\alpha_j) = 0$ pour tout $j$.
Or tout élément $\alpha \in K$ peut s'écrire
$\alpha = \sum \beta_j \alpha_j$ avec $\beta_j \in F$, et nous obtiendrions
$$
\sum \lambda_i\sigma_i(\alpha) =
\sum \lambda_i\sigma_i(\sum \beta_j \alpha_j) =
\sum \beta_j \sum \lambda_i\sigma_i(\alpha_j) = 0
$$
ce qui contredit le Lemme \ref{lemma-independence-embeddings}.
\end{proof}







\section{Extensions purement inséparables}
```

</details>

### FR-FIELDS-B3-PROSE-0021

`section-purely-inseparable` — source 1573–1580, français 1573–1580.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1573) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

À l'opposé traduit une opposition pédagogique, non une opération catégorique. L'annonce sur la caractéristique positive est conservée, même si la définition suivante inclut aussi l'extension identité en caractéristique zéro. Cette tension source est signalée séparément.

**Réserve :** L'introduction dit seulement caractéristique positive ; la définition inclut ensuite L=M dans toute caractéristique. Ne pas convertir l'annonce en une nouvelle restriction de la définition.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-purely-inseparable}

\noindent
Purely inseparable extensions are the opposite of the separable
extensions defined in the previous section. These extensions only
show up in positive characteristic.

\begin{definition}
```

```tex
\label{section-purely-inseparable}

\noindent
Les extensions purement inséparables sont à l'opposé des extensions
séparables définies à la section précédente. Elles n'apparaissent
qu'en caractéristique positive.

\begin{definition}
```

</details>

### FR-FIELDS-B3-PROSE-0022

`definition-purely-inseparable` — source 1581–1616, français 1581–1616.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1581) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Purement inséparable est attesté dans le cours, mais Stacks donne directement la condition par puissances p. Chaque élément est requis ; le cas L=M sans condition de caractéristique demeure. L'exemple par adjonction de racine, la base de puissances, le calcul de Frobenius et le corps de fonctions rationnelles sont conservés en entier.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-purely-inseparable}
Let $F$ be a field of characteristic $p > 0$. Let $K/F$ be an extension.
\begin{enumerate}
\item An element $\alpha \in K$ is {\it purely inseparable} over $F$
if there exists a power $q$ of $p$ such that $\alpha^q \in F$.
\item The extension $K/F$ is said to be {\it purely inseparable}
if and only if every element of $K$ is purely inseparable over $F$.
\end{enumerate}
If we have a field extension $L/M$ (with no condition on the characteristic
of $M$), then we will say the extension is {\it purely inseparable}
if either $L = M$ or the characteristic of $M$ is a prime number $p$
and $L/M$ is purely inseparable in the sense defined above.
\end{definition}

\noindent
Observe that a purely inseparable extension is necessarily algebraic.
Let $F$ be a field of characteristic $p > 0$.
An example of a purely inseparable extension is gotten by adjoining
the $p$th root of an element $t \in F$ which does not yet have one. Namely,
the lemma below shows that $P = x^p - t$ is irreducible, and hence
$$
K = F[x]/(P) = F[t^{1/p}]
$$
is a field. And $K$ is purely inseparable over $F$ because every element
$$
a_0 + a_1t^{1/p} + \ldots + a_{p - 1}t^{(p - 1)/p},\quad a_i \in F
$$
of $K$ has $p$th power equal to
$$
(a_0 + a_1t^{1/p} + \ldots + a_{p - 1}t^{(p - 1)/p})^p =
a_0^p + a_1^p t + \ldots + a_{p - 1}^pt^{p - 1} \in F
$$
This situation occurs for the field
$\mathbf{F}_p(t)$ of rational functions over $\mathbf{F}_p$.

\begin{lemma}
```

```tex
\label{definition-purely-inseparable}
Soit $F$ un corps de caractéristique $p > 0$. Soit $K/F$ une extension.
\begin{enumerate}
\item Un élément $\alpha \in K$ est dit {\it purement inséparable} sur $F$
s'il existe une puissance $q$ de $p$ telle que $\alpha^q \in F$.
\item L'extension $K/F$ est dite {\it purement inséparable}
si et seulement si tout élément de $K$ est purement inséparable sur $F$.
\end{enumerate}
Si $L/M$ est une extension de corps (sans condition sur la caractéristique
de $M$), nous dirons que l'extension est {\it purement inséparable}
si $L = M$, ou si la caractéristique de $M$ est un nombre premier $p$
et que $L/M$ est purement inséparable au sens défini ci-dessus.
\end{definition}

\noindent
Observons qu'une extension purement inséparable est nécessairement algébrique.
Soit $F$ un corps de caractéristique $p > 0$.
On obtient un exemple d'extension purement inséparable en adjoignant
la racine $p$-ième d'un élément $t \in F$ qui n'en possède pas encore. En effet,
le lemme ci-dessous montre que $P = x^p - t$ est irréductible, et donc
$$
K = F[x]/(P) = F[t^{1/p}]
$$
est un corps. De plus, $K$ est purement inséparable sur $F$, car tout élément
$$
a_0 + a_1t^{1/p} + \ldots + a_{p - 1}t^{(p - 1)/p},\quad a_i \in F
$$
de $K$ a pour puissance $p$-ième
$$
(a_0 + a_1t^{1/p} + \ldots + a_{p - 1}t^{(p - 1)/p})^p =
a_0^p + a_1^p t + \ldots + a_{p - 1}^pt^{p - 1} \in F
$$
Cette situation se présente pour le corps
$\mathbf{F}_p(t)$ des fonctions rationnelles sur $\mathbf{F}_p$.

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0023

`lemma-take-pth-root` — source 1617–1639, français 1617–1639.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1617) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

L'absence de racine dans F est la même hypothèse, et la conclusion reste l'irréductibilité. La preuve suit la factorisation, les dérivées, le facteur commun, la puissance d'un irréductible et l'utilisation de p premier. Elle laisse non triviale implicite dans factorisation, comme la source. La transition sur l'importance des racines p-ièmes est conservée.

**Réserve :** La factorisation non triviale est implicite dans la preuve source. Le qualificatif n'est pas ajouté au texte de cette édition.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-take-pth-root}
Let $p$ be a prime number. Let $F$ be a field of characteristic $p$.
Let $t \in F$ be an element which does not have a $p$th root in $F$.
Then the polynomial $x^p - t$ is irreducible over $F$.
\end{lemma}

\begin{proof}
To see this, suppose that we have a factorization
$x^p - t = f g$. Taking derivatives we get $f' g + f g' = 0$.
Note that neither $f' = 0$ nor $g' = 0$ as the degrees of $f$ and $g$
are smaller than $p$. Moreover, $\deg(f') < \deg(f)$ and $\deg(g') < \deg(g)$.
We conclude that $f$ and $g$ have a factor in common. Thus if $x^p - t$
is reducible, then it is of the form $x^p - t = c f^n$ for some irreducible
$f$, $c \in F^*$, and $n > 1$. Since $p$ is a prime number this
implies $n = p$ and $f$ linear, which would imply $x^p - t$ has a root
in $F$. Contradiction.
\end{proof}

\noindent
We will see that taking $p$th roots is a very important operation in
characteristic $p$.

\begin{lemma}
```

```tex
\label{lemma-take-pth-root}
Soit $p$ un nombre premier. Soit $F$ un corps de caractéristique $p$.
Soit $t \in F$ un élément qui n'a pas de racine $p$-ième dans $F$.
Alors le polynôme $x^p - t$ est irréductible sur $F$.
\end{lemma}

\begin{proof}
Pour le voir, supposons donnée une factorisation
$x^p - t = f g$. En dérivant, on obtient $f' g + f g' = 0$.
Notons que ni $f' = 0$ ni $g' = 0$, puisque les degrés de $f$ et de $g$
sont strictement inférieurs à $p$. En outre, $\deg(f') < \deg(f)$ et $\deg(g') < \deg(g)$.
Nous en déduisons que $f$ et $g$ ont un facteur commun. Ainsi, si $x^p - t$
est réductible, il est de la forme $x^p - t = c f^n$ pour un certain polynôme
irréductible $f$, un certain $c \in F^*$ et un certain $n > 1$. Comme $p$ est premier,
cela entraîne $n = p$ et $f$ linéaire, ce qui impliquerait que $x^p - t$ possède
une racine dans $F$. Contradiction.
\end{proof}

\noindent
Nous verrons que l'extraction de racines $p$-ièmes est une opération très importante
en caractéristique $p$.

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0024

`lemma-purely-inseparable-permanence` — source 1640–1651, français 1640–1651.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1640) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

La transitivité est prouvée par les puissances successives q et q', avec les mêmes corps intermédiaires. Notée q est une réorganisation française de some p-power q, non un nouveau choix. La convention de l'identité en caractéristique zéro reste celle du chapitre ; aucun paragraphe supplémentaire n'est inséré.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-purely-inseparable-permanence}
Let $E/k$ and $F/E$ be purely inseparable extensions of fields. Then $F/k$
is a purely inseparable extension of fields.
\end{lemma}

\begin{proof}
Say the characteristic of $k$ is $p$. Choose $\alpha \in F$. Then
$\alpha^q \in E$ for some $p$-power $q$. Whereupon $(\alpha^q)^{q'} \in k$
for some $p$-power $q'$. Hence $\alpha^{qq'} \in k$.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-purely-inseparable-permanence}
Soient $E/k$ et $F/E$ des extensions de corps purement inséparables. Alors $F/k$
est une extension de corps purement inséparable.
\end{lemma}

\begin{proof}
Disons que la caractéristique de $k$ est $p$. Choisissons $\alpha \in F$. Alors
$\alpha^q \in E$ pour une certaine puissance de $p$, notée $q$. Dès lors, $(\alpha^q)^{q'} \in k$
pour une certaine puissance de $p$, notée $q'$. Par conséquent, $\alpha^{qq'} \in k$.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0025

`lemma-purely-inseparable-elements` — source 1652–1668, français 1652–1668.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1652) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le corps engendré par les éléments purement inséparables est obtenu avec le même majorant q'' des puissances q et q'. Les opérations somme, différence, produit et quotient sont toutes conservées. La condition de dénominateur non nul reste implicite, comme dans l'anglais.

**Réserve :** Quotient présuppose un dénominateur non nul, laissé implicite. La définition des éléments en caractéristique zéro est également moins explicite que celle des extensions.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-purely-inseparable-elements}
Let $E/k$ be a field extension. Then the elements of $E$ purely-inseparable
over $k$ form a subextension of $E/k$.
\end{lemma}

\begin{proof}
Let $p$ be the characteristic of $k$.
Let $\alpha, \beta \in E$ be purely inseparable over $k$. Say
$\alpha^q \in k$ and $\beta^{q'} \in k$ for some $p$-powers $q, q'$.
If $q''$ is a $p$-power, then
$(\alpha + \beta)^{q''} = \alpha^{q''} + \beta^{q''}$.
Hence if $q'' \geq q, q'$, then we conclude that $\alpha + \beta$
is purely inseparable over $k$. Similarly for the difference,
product and quotient of $\alpha$ and $\beta$.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-purely-inseparable-elements}
Soit $E/k$ une extension de corps. Alors les éléments de $E$ purement inséparables
sur $k$ forment une sous-extension de $E/k$.
\end{lemma}

\begin{proof}
Soit $p$ la caractéristique de $k$.
Soient $\alpha, \beta \in E$ purement inséparables sur $k$. Écrivons
$\alpha^q \in k$ et $\beta^{q'} \in k$ pour certaines puissances de $p$, notées $q, q'$.
Si $q''$ est une puissance de $p$, alors
$(\alpha + \beta)^{q''} = \alpha^{q''} + \beta^{q''}$.
Par conséquent, si $q'' \geq q, q'$, nous en déduisons que $\alpha + \beta$
est purement inséparable sur $k$. Il en va de même de la différence,
du produit et du quotient de $\alpha$ et $\beta$.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0026

`lemma-finite-purely-inseparable` — source 1669–1703, français 1669–1703.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1669) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

La finitude, la caractéristique positive et le degré p de chaque étape sont conservés. Le choix minimal de r, le remplacement d'alpha, l'absence de racine p-ième dans F et la récurrence sur E/F(alpha) sont lus en entier. Le cas n=0 et la concaténation de la suite finale restent présents.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-finite-purely-inseparable}
Let $E/F$ be a finite purely inseparable field extension of
characteristic $p > 0$. Then there exists a sequence of elements
$\alpha_1, \ldots, \alpha_n \in E$ such that we obtain a tower
of fields
$$
E = F(\alpha_1, \ldots, \alpha_n) \supset
F(\alpha_1, \ldots, \alpha_{n - 1}) \supset
\ldots
\supset F(\alpha_1) \supset F
$$
such that each intermediate extension is of degree $p$ and comes
from adjoining a $p$th root. Namely,
$\alpha_i^p \in F(\alpha_1, \ldots, \alpha_{i - 1})$
is an element which does not have a $p$th root in
$F(\alpha_1, \ldots, \alpha_{i - 1})$ for $i = 1, \ldots, n$.
\end{lemma}

\begin{proof}
By induction on the degree of $E/F$. If the degree of the extension is $1$
then the result is clear (with $n = 0$). If not, then choose
$\alpha \in E$, $\alpha \not \in F$. Say $\alpha^{p^r} \in F$ for some
$r > 0$. Pick $r$ minimal and replace $\alpha$ by $\alpha^{p^{r - 1}}$.
Then $\alpha \not \in F$, but $\alpha^p \in F$. Then $t = \alpha^p$ is not
a $p$th power in $F$ (because that would imply $\alpha \in F$, see
Lemma \ref{lemma-nr-roots-unchanged} or its proof).
Thus $F \subset F(\alpha)$ is a subextension of degree $p$
(Lemma \ref{lemma-take-pth-root}). By induction we find
$\alpha_1, \ldots, \alpha_n \in E$ generating $E/F(\alpha)$
satisfying the conclusions of the lemma.
The sequence $\alpha, \alpha_1, \ldots, \alpha_n$ does the job
for the extension $E/F$.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-finite-purely-inseparable}
Soit $E/F$ une extension de corps finie purement inséparable de
caractéristique $p > 0$. Alors il existe une suite d'éléments
$\alpha_1, \ldots, \alpha_n \in E$ qui donne une tour
de corps
$$
E = F(\alpha_1, \ldots, \alpha_n) \supset
F(\alpha_1, \ldots, \alpha_{n - 1}) \supset
\ldots
\supset F(\alpha_1) \supset F
$$
telle que chaque extension intermédiaire soit de degré $p$ et s'obtienne
par adjonction d'une racine $p$-ième. Plus précisément,
$\alpha_i^p \in F(\alpha_1, \ldots, \alpha_{i - 1})$
est un élément qui ne possède pas de racine $p$-ième dans
$F(\alpha_1, \ldots, \alpha_{i - 1})$, pour $i = 1, \ldots, n$.
\end{lemma}

\begin{proof}
Raisonnons par récurrence sur le degré de $E/F$. Si ce degré vaut $1$,
le résultat est clair (avec $n = 0$). Sinon, choisissons
$\alpha \in E$, $\alpha \not \in F$. Écrivons $\alpha^{p^r} \in F$ pour un certain
$r > 0$. Prenons $r$ minimal et remplaçons $\alpha$ par $\alpha^{p^{r - 1}}$.
Alors $\alpha \not \in F$, mais $\alpha^p \in F$. Ainsi $t = \alpha^p$ n'est pas
une puissance $p$-ième dans $F$ (car cela entraînerait $\alpha \in F$, voir le
Lemme \ref{lemma-nr-roots-unchanged} ou sa démonstration).
Ainsi, $F \subset F(\alpha)$ est une sous-extension de degré $p$
(Lemme \ref{lemma-take-pth-root}). Par récurrence, nous trouvons
$\alpha_1, \ldots, \alpha_n \in E$ qui engendrent $E/F(\alpha)$
et satisfont aux conclusions du lemme.
La suite $\alpha, \alpha_1, \ldots, \alpha_n$ convient alors
pour l'extension $E/F$.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0027

`lemma-separable-first` — source 1704–1726, français 1704–1726.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1704) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le slogan et l'énoncé gardent l'ordre : extension séparable puis purement inséparable, avec unicité du corps intermédiaire. La preuve conserve la séparation caractéristique zéro/positive et l'élévation à une puissance p. L'anglais qualifie P de separable algebraic alors que P est un polynôme ; polynôme séparable est retenu comme mise en français de l'objet explicite P(x^q), sans ajouter ni supprimer une propriété définie de P. Ce choix interprétatif est rendu visible pour examen.

**Réserve :** Choix interprétatif à revoir si nécessaire : separable algebraic appliqué à P est rendu par polynôme séparable, P étant déjà typé comme polynôme. Il ne s'agit pas de remplacer une racine algébrique par un polynôme.

Choix écartés :

- Polynôme algébrique séparable : non retenu, car algébrique ne définit ici aucune propriété supplémentaire d'un polynôme et obscurcit son type ; réserve explicite plutôt que prétendue attestation.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-separable-first}
\begin{slogan}
Any algebraic field extension is uniquely a separable field extension
followed by a purely inseparable one.
\end{slogan}
Let $E/F$ be an algebraic field extension. There exists a unique subextension
$E/E_{sep}/F$ such that $E_{sep}/F$ is separable and $E/E_{sep}$ is
purely inseparable.
\end{lemma}

\begin{proof}
If the characteristic is zero we set $E_{sep} = E$. Assume the characteristic
is $p > 0$. Let $E_{sep}$ be the set of elements of $E$ which are separable
over $F$. This is a subextension by Lemma \ref{lemma-separable-elements}
and of course $E_{sep}$ is separable over $F$. Given an $\alpha$ in $E$
there exists a $p$-power $q$ such that $\alpha^q$ is separable over $F$.
Namely, $q$ is that power of $p$ such that the minimal polynomial of
$\alpha$ is of the form $P(x^q)$ with $P$ separable algebraic, see
Lemma \ref{lemma-irreducible-polynomials}. Hence $E/E_{sep}$ is purely
inseparable. Uniqueness is clear.
\end{proof}

\begin{definition}
```

```tex
\label{lemma-separable-first}
\begin{slogan}
Toute extension algébrique de corps est, de manière unique, une extension
séparable suivie d'une extension purement inséparable.
\end{slogan}
Soit $E/F$ une extension algébrique de corps. Il existe une unique sous-extension
$E/E_{sep}/F$ telle que $E_{sep}/F$ soit séparable et que $E/E_{sep}$ soit
purement inséparable.
\end{lemma}

\begin{proof}
Si la caractéristique est nulle, posons $E_{sep} = E$. Supposons désormais la caractéristique
égale à $p > 0$. Soit $E_{sep}$ l'ensemble des éléments de $E$ qui sont séparables
sur $F$. C'est une sous-extension d'après le Lemme \ref{lemma-separable-elements},
et bien entendu $E_{sep}$ est séparable sur $F$. Étant donné $\alpha$ dans $E$,
il existe une puissance de $p$, notée $q$, telle que $\alpha^q$ soit séparable sur $F$.
En effet, $q$ est la puissance de $p$ telle que le polynôme minimal de
$\alpha$ soit de la forme $P(x^q)$, où $P$ est un polynôme séparable, voir le
Lemme \ref{lemma-irreducible-polynomials}. Ainsi $E/E_{sep}$ est purement
inséparable. L'unicité est claire.
\end{proof}

\begin{definition}
```

</details>

### FR-FIELDS-B3-PROSE-0028

`definition-insep-degree` — source 1727–1750, français 1727–1750.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1727) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Les deux occurrences de l'entier reproduisent maintenant le texte officiel, même si le paragraphe suivant admet des degrés infinis. Les deux noms degré inséparable et degré d'inséparabilité sont conservés, avec toutes les notations et la multiplicativité. Les restaurations historiques FIELDS-041A et FIELDS-041B ne sont ni annulées ni comptées de nouveau.

**Réserve :** L'entier est incompatible avec la généralité infinie évoquée ensuite. Les deux propositions de correction restent hors du texte fidèle ; pas de nouvelle admission canonique.

Choix écartés :

- Le degré à la place de l'entier : correction source motivée mais retirée de cette édition fidèle, conservée dans le dossier historique.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-insep-degree}
Let $E/F$ be an algebraic field extension. Let $E_{sep}$ be the subextension
found in Lemma \ref{lemma-separable-first}.
\begin{enumerate}
\item The integer $[E_{sep} : F]$ is called the {\it separable
degree} of the extension. Notation $[E : F]_s$.
\item The integer $[E : E_{sep}]$ is called the {\it inseparable
degree}, or the {\it degree of inseparability} of the extension.
Notation $[E : F]_i$.
\end{enumerate}
\end{definition}

\noindent
Of course in characteristic $0$ we have $[E : F] = [E : F]_s$ and
$[E : F]_i = 1$. By multiplicativity
(Lemma \ref{lemma-multiplicativity-degrees}) we have
$$
[E : F] = [E : F]_s [E : F]_i
$$
even in case some of these degrees are infinite. In fact, the separable
degree and the inseparable degree are multiplicative too (see
Lemma \ref{lemma-multiplicativity-all-degrees}).

\begin{lemma}
```

```tex
\label{definition-insep-degree}
Soit $E/F$ une extension algébrique de corps. Soit $E_{sep}$ la sous-extension
obtenue au Lemme \ref{lemma-separable-first}.
\begin{enumerate}
\item L'entier $[E_{sep} : F]$ est appelé le {\it degré séparable}
de l'extension. Notation : $[E : F]_s$.
\item L'entier $[E : E_{sep}]$ est appelé le {\it degré inséparable},
ou le {\it degré d'inséparabilité} de l'extension.
Notation : $[E : F]_i$.
\end{enumerate}
\end{definition}

\noindent
Bien entendu, en caractéristique $0$, on a $[E : F] = [E : F]_s$ et
$[E : F]_i = 1$. Par multiplicativité
(Lemme \ref{lemma-multiplicativity-degrees}), on a
$$
[E : F] = [E : F]_s [E : F]_i
$$
même lorsque certains de ces degrés sont infinis. En fait, le degré séparable
et le degré inséparable sont eux aussi multiplicatifs (voir le
Lemme \ref{lemma-multiplicativity-all-degrees}).

\begin{lemma}
```

</details>

### FR-FIELDS-B3-PROSE-0029

`lemma-separable-degree` — source 1751–1778, français 1751–1778.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1751) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

Le lemme est fini. La preuve commence par le cas purement inséparable, puis compte les morphismes du sous-corps séparable et leur unique prolongement. Application garde ici la même ellipse que map ; les notations Mor_F et la suite du paragraphe fixent sa nature. Le cas identité en caractéristique zéro n'est pas développé davantage que dans l'anglais.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-separable-degree}
Let $K/F$ be a finite extension. Let $\overline{F}$ be an algebraic
closure of $F$. Then $[K : F]_s = |\Mor_F(K, \overline{F})|$.
\end{lemma}

\begin{proof}
We first prove this when $K/F$ is purely inseparable. Namely, we claim that
in this case there is a unique map $K \to \overline{F}$. This can be
seen by choosing a sequence of elements $\alpha_1, \ldots, \alpha_n \in K$
as in Lemma \ref{lemma-finite-purely-inseparable}. The irreducible polynomial
of $\alpha_i$ over $F(\alpha_1, \ldots, \alpha_{i - 1})$ is $x^p - \alpha_i^p$.
Applying Lemma \ref{lemma-count-embeddings-explicitly} we see that
$|\Mor_F(K, \overline{F})| = 1$. On the other hand, $[K : F]_s = 1$
in this case hence the equality holds.

\medskip\noindent
Let's return to a general finite extension $K/F$. In this case
choose $F \subset K_s \subset K$ as in Lemma \ref{lemma-separable-first}.
By Lemma \ref{lemma-separable-equality} we have
$|\Mor_F(K_s, \overline{F})| = [K_s : F] = [K : F]_s$.
On the other hand, every field map $\sigma' : K_s \to \overline{F}$
extends to a unique field map $\sigma : K \to \overline{F}$ by the
result of the previous paragraph. In other words
$|\Mor_F(K, \overline{F})| = |\Mor_F(K_s, \overline{F})|$
and the proof is done.
\end{proof}

\begin{lemma}[Multiplicativity]
```

```tex
\label{lemma-separable-degree}
Soit $K/F$ une extension finie. Soit $\overline{F}$ une clôture algébrique
de $F$. Alors $[K : F]_s = |\Mor_F(K, \overline{F})|$.
\end{lemma}

\begin{proof}
Démontrons d'abord ce résultat lorsque $K/F$ est purement inséparable. Nous affirmons
que, dans ce cas, il existe une unique application $K \to \overline{F}$. On peut le
voir en choisissant une suite d'éléments $\alpha_1, \ldots, \alpha_n \in K$
comme au Lemme \ref{lemma-finite-purely-inseparable}. Le polynôme irréductible
de $\alpha_i$ sur $F(\alpha_1, \ldots, \alpha_{i - 1})$ est $x^p - \alpha_i^p$.
En appliquant le Lemme \ref{lemma-count-embeddings-explicitly}, on voit que
$|\Mor_F(K, \overline{F})| = 1$. D'autre part, $[K : F]_s = 1$
dans ce cas, d'où l'égalité.

\medskip\noindent
Revenons à une extension finie générale $K/F$. Dans ce cas,
choisissons $F \subset K_s \subset K$ comme au Lemme \ref{lemma-separable-first}.
D'après le Lemme \ref{lemma-separable-equality}, on a
$|\Mor_F(K_s, \overline{F})| = [K_s : F] = [K : F]_s$.
D'autre part, tout morphisme de corps $\sigma' : K_s \to \overline{F}$
se prolonge de manière unique en un morphisme de corps $\sigma : K \to \overline{F}$, d'après le
résultat du paragraphe précédent. Autrement dit,
$|\Mor_F(K, \overline{F})| = |\Mor_F(K_s, \overline{F})|$,
ce qui achève la démonstration.
\end{proof}

\begin{lemma}[Multiplicativité]
```

</details>

### FR-FIELDS-B3-PROSE-0030

`lemma-multiplicativity-all-degrees` — source 1779–1812, français 1779–1812.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L1779) · [Français de travail](staged/fr/009_fields.prose-batch1.fr.tex)

L'énoncé conserve les deux produits pour une tour algébrique générale. La preuve ne traite que le cas fini : réduction à une formule, interprétation de la clôture via sigma, puis dénombrement des prolongements. La dernière phrase omettant la preuve infinie est gardée. Le et de l'affichage traduit seulement and ; aucune formule ni preuve de remplacement n'est introduite.

**Réserve :** La preuve du cas infini est explicitement absente. Cette lecture vérifie la fidélité française ; elle ne certifie pas la généralité mathématique annoncée.

Choix écartés :

- Ajouter une preuve ou limiter l'énoncé au cas fini : rejeté dans la traduction de référence ; ce serait un travail éditorial distinct.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-multiplicativity-all-degrees}
Suppose given a tower of algebraic field extensions $K/E/F$. Then
$$
[K : F]_s = [K : E]_s [E : F]_s
\quad\text{and}\quad
[K : F]_i = [K : E]_i [E : F]_i
$$
\end{lemma}

\begin{proof}
We first prove this in case $K$ is finite over $F$. Since we have
multiplicativity for the usual degree (by
Lemma \ref{lemma-multiplicativity-degrees}) it suffices to prove
one of the two formulas. By Lemma \ref{lemma-separable-degree} we have
$[K : F]_s = |\Mor_F(K, \overline{F})|$. By the same lemma,
given any $\sigma \in \Mor_F(E, \overline{F})$ the number of extensions
of $\sigma$ to a map $\tau : K \to \overline{F}$ is $[K : E]_s$.
Namely, via $E \cong \sigma(E) \subset \overline{F}$ we can view
$\overline{F}$ as an algebraic closure of $E$. Combined with the
fact that there are $[E : F]_s = |\Mor_F(E, \overline{F})|$ choices
for $\sigma$ we obtain the result.

\medskip\noindent
We omit the proof if the extensions are infinite.
\end{proof}
```

```tex
\label{lemma-multiplicativity-all-degrees}
Supposons donnée une tour d'extensions algébriques de corps $K/E/F$. Alors
$$
[K : F]_s = [K : E]_s [E : F]_s
\quad\text{et}\quad
[K : F]_i = [K : E]_i [E : F]_i
$$
\end{lemma}

\begin{proof}
Démontrons d'abord le résultat lorsque $K$ est fini sur $F$. Comme la
multiplicativité vaut pour le degré usuel (d'après le
Lemme \ref{lemma-multiplicativity-degrees}), il suffit de démontrer
l'une des deux formules. D'après le Lemme \ref{lemma-separable-degree}, on a
$[K : F]_s = |\Mor_F(K, \overline{F})|$. Par le même lemme,
pour tout $\sigma \in \Mor_F(E, \overline{F})$, le nombre de prolongements
de $\sigma$ en une application $\tau : K \to \overline{F}$ est $[K : E]_s$.
En effet, via $E \cong \sigma(E) \subset \overline{F}$, nous pouvons considérer
$\overline{F}$ comme une clôture algébrique de $E$. En combinant ceci avec le
fait qu'il existe $[E : F]_s = |\Mor_F(E, \overline{F})|$ choix
pour $\sigma$, on obtient le résultat.

\medskip\noindent
Nous omettons la démonstration lorsque les extensions sont infinies.
\end{proof}
```

</details>

## Limites et suite

Analyse assistée par OpenAI Codex ; l'identité exacte du modèle et de son effort n'est pas attestée par ce reçu et n'est pas inventée. La présente note n'est pas une publication de l'édition restaurée. Aucune expertise humaine ni attestation universelle du vocabulaire n'est revendiquée.

Prochaine section : Extensions normales, ligne officielle 1813. Les quatorze sections lues, leurs exceptions et les restaurations historiques demeurent conservées. Il reste la suite du chapitre, les autres dossiers incomplets et les validations cumulatives avant la publication. L'ancienne édition éditorialisée est préservée pour un éventuel travail ultérieur distinct.
