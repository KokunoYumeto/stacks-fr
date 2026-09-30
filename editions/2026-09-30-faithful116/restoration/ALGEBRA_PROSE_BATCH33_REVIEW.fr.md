# Idéaux premiers immergés

## Résultat et portée

La section entière est comparée : anglais L16445–16586 et français L16211–16352, 142 lignes chacun, cinq paires complètes. 60 occurrences de règles sont contextualisées, non un décompte de tous les mots. Couverture continue : 67 sections, 600 paires et 5875 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Une normalisation de langue remplace Omis par Démonstration omise. Les mathématiques ne changent pas : définition générale, suppression des premiers immergés sous les hypothèses noethériennes/de type fini, localisation et anneau quotient par l’annulateur sont comparés en entier. Le nouveau LaTeX est réversible et les versions antérieures restent conservées.

Deux observations anglaises restent hors traduction : K au lieu de K’ dans une implication de preuve et 0 pour une intersection vide de parties du spectre. La seconde est une réserve de notation, non une accusation de résultat faux.

Lecture produite par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. Le canon est consulté rétrospectivement, non présenté comme consulté lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch33.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH32_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH33_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH33_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH33_OCCURRENCES.json) · [Opérations](ALGEBRA_PROSE_BATCH33_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH33_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH33_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH33_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH33_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH33_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Christian Peskine — Introduction algébrique à la géométrie projective

[Source consultée](https://perso.univ-rennes1.fr/matthieu.romagny/M2_0708/bouquin.pdf) · [Fichier conservé](canon-consulted/fr-algebra/peskine-geometrie-projective-2007.pdf)

Pages PDF211–212 /imprimées210–211 intégralement lues ; PDF211 rendu et inspecté. Section23.4, définition23.17 et suite, définition23.18 et proposition23.19.

Attestations courtes : « idéaux premiers immergés », « composante immergée », « sans composante immergée ».

La définition23.17 oppose les premiers minimaux aux premiers immergés dans une décomposition primaire et justifie le registre retenu. La proposition23.19 emploie les annulateurs et les ouverts denses dans un schéma sans composante immergée.

Limites : Le vocabulaire est attesté dans ce contexte géométrique ; ses conventions sur les schémas irréductibles et ses restrictions ne remplacent pas la définition générale de Stacks pour les modules. Aucune preuve omise n'est fournie par le canon.

SHA-256 : C84D597457282B22B993F523791F4A3E391A74554FF76F7F49878640789435BA.

### Jean-Pierre Ferrier — Quelques thèmes d’exercices en Analyse suivis d’un Petit cours sauvage d’Analyse mathématique

[Source consultée](https://bibnum.publimath.fr/ILO/ILO07001.pdf) · [Fichier conservé](canon-consulted/fr-algebra/irem-lorraine-analyse-ilo07001.pdf)

Années2005–2006 et2006–2007, Université Henri Poincaré /IREM de Lorraine. Couverture PDF1 et pagePDF99 /page9 du Petit cours lues ; PDF99 rendu et inspecté. Définition initiale des espaces de Baire.

Attestations courtes : « rare », « son adhérence est d’intérieur vide ».

La définition vaut dans un espace topologique et atteste précisément rare pour nowhere dense, distinct de maigre. Appliquée au sous-espace Supp(M), elle justifie rare dans Supp(M) dans les trois occurrences du lemme.

Limites : Le résultat de Baire des espaces métriques complets n'est pas utilisé pour les spectres. Pas d'affirmation que cet ouvrage prouve le lemme algébrique. La couverture fixe auteur et période ; la date d'indexation web n'est pas sa date de rédaction.

SHA-256 : 4673046759F2285FA8EE42B186D3FE5249B0493B82FD32C4EE7F7800FFA060D4.

## Modifications et motifs

Une normalisation du libellé de preuve omise, sans ajouter sa démonstration. Les autres formulations sont conservées après lecture complète. Les deux réserves source ne deviennent pas une liberté éditoriale française.

### FR-ALGEBRA-B33-REPAIR-0001

Anglais L16545 ; français L16311.

Avant :
```tex
Omis.
```

Après :
```tex
Démonstration omise.
```

L'égalité de quotients après localisation reste identique, pour chaque f et avec le même renvoi. Omis devient Démonstration omise : explicitation du nom et accord, sans inventer la preuve absente. Omettre le nom rend le libellé télégraphique et ambigu ; la normalisation ne prétend pas corriger une faute mathématique.

La preuve demeure omise. Démonstration omise est une normalisation de langue explicitement enregistrée, pas l'ajout d'une démonstration.

## Observations séparées sur la source

Deux observations sont distinctes : mauvais sous-module dans un lien logique et notation ensembliste informelle. Le français reste conforme au témoin officiel. Aucune admission, déduplication globale ou première découverte n’est revendiquée.

### lemma-remove-embedded-primes

[Anglais officiel L16508](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16508) · FR-ALGEBRA-B33-SOURCE-NOTE-0001.

```tex
that $K_{\mathfrak q_j} = 0$. Hence if $m \in K'$,
```

Le texte introduit K' comme un autre sous-module à support rare, puis parle de m∈K'. Le localisé dont l'annulation résulte de cette hypothèse est K'_{q_j}, pas K_{q_j} déjà construit. La correction proposée ajoute une prime à K dans cette phrase ; elle rétablit le lien logique du raisonnement. K_{q_j}=0 est vrai séparément, mais ne justifie pas le passage sur un m de K'. Le français garde la notation source.

Confiance forte sur le mauvais nom dans ce lien de preuve ; aucune admission ou première découverte.

### lemma-remove-embedded-primes

[Anglais officiel L16531](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16531) · FR-ALGEBRA-B33-SOURCE-NOTE-0002.

```tex
$D(f) \cap \text{supp}(K) = 0$.
```

L'intersection est celle de deux parties de Spec(R). Sa vacuité devrait s'écrire ∅ plutôt que le scalaire0 ; la phrase suivante déduit K_f=0 de cette vacuité. C'est une réserve de notation, pas une assertion que le résultat est faux. L'usage informel de0 pour l'ensemble vide est possible ; proposé ∅ pour lever l'ambiguïté. Le français conserve0.

Confiance forte sur le type ensembliste ; portée éditoriale de la notation, pas correction mathématique admise.

## Règles contextualisées

### FR-ALGEBRA-B33-RULE-EMBEDDED

Premier immergé reste un premier associé non minimal ; l'annulateur et les premiers minimaux gardent leurs objets.

Canon : FR-ALGEBRA-B33-CANON-PESKINE.

### FR-ALGEBRA-B33-RULE-SUPPORT

Rare est topologique dans le support considéré. Quotient et localisation préservent les hypothèses et identités de la source.

Canon : FR-ALGEBRA-B33-CANON-PESKINE, FR-ALGEBRA-B33-CANON-FERRIER.

### FR-ALGEBRA-B33-RULE-MODULE

La noethérianité porte sur l'anneau et le type fini sur M ou K. Les sous-modules et l'anneau quotient ne sont pas confondus.

Canon : FR-ALGEBRA-B33-CANON-PESKINE.

### FR-ALGEBRA-B33-RULE-LOGIC

Les quantificateurs et inclusions sont comparés dans les cinq passages entiers ; aucun résultat plus fort ou preuve absente ajouté.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-embedded-primes

Anglais L16445–16450 ; français L16211–16216.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16445) · FR-ALGEBRA-B33-CHOICE-0001.

Idéaux premiers immergés est directement attesté chez Peskine. L'introduction Voici la définition est conservée ; pas d'ajout d'un résultat.

Règles : FR-ALGEBRA-B33-RULE-EMBEDDED.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Embedded primes}
\label{section-embedded-primes}

\noindent
Here is the definition.
```

Français restauré :
```tex
\section{Idéaux premiers immergés}
\label{section-embedded-primes}

\noindent
Voici la définition.
```

</details>

### 02 — definition-embedded-primes

Anglais L16451–16466 ; français L16217–16232.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16451) · FR-ALGEBRA-B33-CHOICE-0002.

Les premiers associés immergés sont ceux non minimaux parmi Ass(M), exactement comme dans la source, pour un anneau et un module arbitraires. Le cas de l'anneau est le cas M=R. L'attestation de Peskine concerne le vocabulaire dans une décomposition primaire, sans imposer ici ses hypothèses de schéma.

Point particulier à relire : La définition source générale n'est pas remplacée par non minimal dans Supp(M), qui requiert les conditions pertinentes. Le canon a été consulté rétrospectivement, non lors de la traduction initiale.

Règles : FR-ALGEBRA-B33-RULE-EMBEDDED, FR-ALGEBRA-B33-RULE-MODULE, FR-ALGEBRA-B33-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-embedded-primes}
Let $R$ be a ring.
Let $M$ be an $R$-module.
\begin{enumerate}
\item  The associated primes of $M$ which are
not minimal among the associated primes of $M$ are called the
{\it embedded associated primes} of $M$.
\item The {\it embedded primes of $R$}
are the embedded associated primes of $R$ as an $R$-module.
\end{enumerate}
\end{definition}

\noindent
Here is a way to get rid of these.
```

Français restauré :
```tex
\begin{definition}
\label{definition-embedded-primes}
Soit $R$ un anneau.
Soit $M$ un $R$-module.
\begin{enumerate}
\item  Les idéaux premiers associés à $M$ qui ne sont
pas minimaux parmi les idéaux premiers associés à $M$ sont appelés les
{\it idéaux premiers associés immergés} de $M$.
\item Les {\it idéaux premiers immergés de $R$}
sont les idéaux premiers associés immergés de $R$ considéré comme $R$-module.
\end{enumerate}
\end{definition}

\noindent
Voici une manière de les éliminer.
```

</details>

### 03 — lemma-remove-embedded-primes

Anglais L16467–16534 ; français L16233–16300.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16467) · FR-ALGEBRA-B33-CHOICE-0003.

Les trois conclusions et toute la preuve sont comparées. Rare dans Supp(M) signifie que l'adhérence a intérieur vide dans ce sous-espace, et non simplement non dense dans Spec(R) ; Ferrier atteste la définition topologique. Anneau noethérien, module de type fini, élément maximal, quotient et choix de f dans tous les premiers immergés restent exacts. La preuve distingue K construit et K' arbitraire ; la coquille source K au lieu de K' demeure littérale et séparée. La conclusion sans premier immergé n'est pas renforcée en module sans torsion.

Point particulier à relire : Rare n'est pas maigre ni seulement non dense. Les expressions anglaises K_q=0 dans le raisonnement sur K' et D(f)∩supp(K)=0 restent source-littérales ; réserves notées à part. Le mot maximal reste maximal plutôt que plus grand : pas d'amélioration éditoriale de l'énoncé.

Règles : FR-ALGEBRA-B33-RULE-EMBEDDED, FR-ALGEBRA-B33-RULE-SUPPORT, FR-ALGEBRA-B33-RULE-MODULE, FR-ALGEBRA-B33-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-remove-embedded-primes}
Let $R$ be a Noetherian ring.
Let $M$ be a finite $R$-module.
Consider the set of $R$-submodules
$$
\{
K \subset M
\mid
\text{Supp}(K)
\text{ nowhere dense in }
\text{Supp}(M)
\}.
$$
This set has a maximal element $K$ and the quotient
$M' = M/K$ has the following properties
\begin{enumerate}
\item $\text{Supp}(M) = \text{Supp}(M')$,
\item $M'$ has no embedded associated primes,
\item for any $f \in R$ which is contained in all
embedded associated primes of $M$ we have $M_f \cong M'_f$.
\end{enumerate}
\end{lemma}

\begin{proof}
We will use Lemma \ref{lemma-finite-ass} and
Proposition \ref{proposition-minimal-primes-associated-primes}
without further mention.
Let $\mathfrak q_1, \ldots, \mathfrak q_t$ denote the
minimal primes in the support of $M$. Let
$\mathfrak p_1, \ldots, \mathfrak p_s$ denote the
embedded associated primes of $M$. Then
$\text{Ass}(M) = \{\mathfrak q_j, \mathfrak p_i\}$.
Let
$$
K = \{m \in M \mid \text{Supp}(Rm) \subset \bigcup V(\mathfrak p_i)\}
$$
It is immediately seen to be a submodule. Since $M$ is finite over a
Noetherian ring, we know $K$ is finite too. Hence $\text{Supp}(K)$
is nowhere dense in $\text{Supp}(M)$. Let $K' \subset M$ be another submodule
with support nowhere dense in $\text{Supp}(M)$. This means
that $K_{\mathfrak q_j} = 0$. Hence if $m \in K'$,
then $m$ maps to zero in $M_{\mathfrak q_j}$ which
in turn implies $(Rm)_{\mathfrak q_j} = 0$.
On the other hand we have $\text{Ass}(Rm) \subset \text{Ass}(M)$.
Hence the support of $Rm$ is contained in $\bigcup V(\mathfrak p_i)$.
Therefore $m \in K$ and thus $K' \subset K$ as $m$ was arbitrary in $K'$.

\medskip\noindent
Let $M' = M/K$. Since $K_{\mathfrak q_j}=0$ we know
$M'_{\mathfrak q_j} = M_{\mathfrak q_j}$ for all $j$.
Hence $M$ and $M'$ have the same support. 

\medskip\noindent
Suppose $\mathfrak q = \text{Ann}(\overline{m}) \in \text{Ass}(M')$
where $\overline{m} \in M'$ is the image of $m \in M$.
Then $m \not \in K$ and hence the support of $Rm$ must contain one of the
$\mathfrak q_j$. Since $M_{\mathfrak q_j} = M'_{\mathfrak q_j}$,
we know $\overline{m}$ does not map to zero in $M'_{\mathfrak q_j}$.
Hence $\mathfrak q \subset \mathfrak q_j$ (actually we have equality),
which means that all the associated primes of $M'$ are not embedded.

\medskip\noindent
Let $f$ be an element contained in all $\mathfrak p_i$.
Then $D(f) \cap \text{supp}(K) = 0$. Hence $M_f = M'_f$
because $K_f = 0$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-remove-embedded-primes}
Soit $R$ un anneau noethérien.
Soit $M$ un $R$-module de type fini.
Considérons l'ensemble des $R$-sous-modules
$$
\{
K \subset M
\mid
\text{Supp}(K)
\text{ rare dans }
\text{Supp}(M)
\}.
$$
Cet ensemble possède un élément maximal $K$, et le quotient
$M' = M/K$ possède les propriétés suivantes :
\begin{enumerate}
\item $\text{Supp}(M) = \text{Supp}(M')$,
\item $M'$ n'a aucun idéal premier associé immergé,
\item pour tout $f \in R$ appartenant à tous les
idéaux premiers associés immergés de $M$, on a $M_f \cong M'_f$.
\end{enumerate}
\end{lemma}

\begin{proof}
Nous utiliserons le Lemme \ref{lemma-finite-ass} et la
Proposition \ref{proposition-minimal-primes-associated-primes}
sans les mentionner davantage.
Notons $\mathfrak q_1, \ldots, \mathfrak q_t$ les
idéaux premiers minimaux du support de $M$. Notons
$\mathfrak p_1, \ldots, \mathfrak p_s$ les
idéaux premiers associés immergés de $M$. Alors
$\text{Ass}(M) = \{\mathfrak q_j, \mathfrak p_i\}$.
Posons
$$
K = \{m \in M \mid \text{Supp}(Rm) \subset \bigcup V(\mathfrak p_i)\}
$$
On voit immédiatement que c'est un sous-module. Puisque $M$ est de type fini sur un
anneau noethérien, $K$ est lui aussi de type fini. Ainsi $\text{Supp}(K)$
est rare dans $\text{Supp}(M)$. Soit $K' \subset M$ un autre sous-module
dont le support est rare dans $\text{Supp}(M)$. Cela signifie
que $K_{\mathfrak q_j} = 0$. Ainsi, si $m \in K'$,
l'image de $m$ dans $M_{\mathfrak q_j}$ est nulle, ce qui
implique à son tour $(Rm)_{\mathfrak q_j} = 0$.
D'autre part, on a $\text{Ass}(Rm) \subset \text{Ass}(M)$.
Le support de $Rm$ est donc contenu dans $\bigcup V(\mathfrak p_i)$.
Ainsi $m \in K$, puis $K' \subset K$, puisque $m$ était arbitraire dans $K'$.

\medskip\noindent
Soit $M' = M/K$. Puisque $K_{\mathfrak q_j}=0$, on a
$M'_{\mathfrak q_j} = M_{\mathfrak q_j}$ pour tout $j$.
Ainsi $M$ et $M'$ ont le même support.

\medskip\noindent
Supposons $\mathfrak q = \text{Ann}(\overline{m}) \in \text{Ass}(M')$,
où $\overline{m} \in M'$ est l'image de $m \in M$.
Alors $m \not \in K$ ; le support de $Rm$ doit donc contenir l'un des
$\mathfrak q_j$. Puisque $M_{\mathfrak q_j} = M'_{\mathfrak q_j}$,
on sait que l'image de $\overline{m}$ dans $M'_{\mathfrak q_j}$ n'est pas nulle.
Ainsi $\mathfrak q \subset \mathfrak q_j$ (en fait, il y a égalité),
ce qui signifie qu'aucun des idéaux premiers associés à $M'$ n'est immergé.

\medskip\noindent
Soit $f$ un élément appartenant à tous les $\mathfrak p_i$.
Alors $D(f) \cap \text{supp}(K) = 0$. Ainsi $M_f = M'_f$
parce que $K_f = 0$.
\end{proof}
```

</details>

### 04 — lemma-remove-embedded-primes-localize

Anglais L16535–16547 ; français L16301–16313.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16535) · FR-ALGEBRA-B33-CHOICE-0004.

L'égalité de quotients après localisation reste identique, pour chaque f et avec le même renvoi. Omis devient Démonstration omise : explicitation du nom et accord, sans inventer la preuve absente. Omettre le nom rend le libellé télégraphique et ambigu ; la normalisation ne prétend pas corriger une faute mathématique.

Point particulier à relire : La preuve demeure omise. Démonstration omise est une normalisation de langue explicitement enregistrée, pas l'ajout d'une démonstration.

Règles : FR-ALGEBRA-B33-RULE-SUPPORT, FR-ALGEBRA-B33-RULE-MODULE, FR-ALGEBRA-B33-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-remove-embedded-primes-localize}
Let $R$ be a Noetherian ring.
Let $M$ be a finite $R$-module.
For any $f \in R$ we have $(M')_f = (M_f)'$ where
$M \to M'$ and $M_f \to (M_f)'$ are the quotients
constructed in Lemma \ref{lemma-remove-embedded-primes}.
\end{lemma}

\begin{proof}
Omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-remove-embedded-primes-localize}
Soit $R$ un anneau noethérien.
Soit $M$ un $R$-module de type fini.
Pour tout $f \in R$, on a $(M')_f = (M_f)'$, où
$M \to M'$ et $M_f \to (M_f)'$ sont les quotients
construits dans le Lemme \ref{lemma-remove-embedded-primes}.
\end{lemma}

\begin{proof}
Démonstration omise.
\end{proof}
```

</details>

### 05 — lemma-no-embedded-primes-endos

Anglais L16548–16586 ; français L16314–16352.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16548) · FR-ALGEBRA-B33-CHOICE-0005.

I est l'annulateur de M, et la conclusion porte sur l'anneau R/I, non sur tous ses quotients. L'action fidèle après quotient, l'égalité du support au spectre, le sous-module non nul xM et l'inclusion des premiers associés sont comparés entièrement. La non-minimalité se déduit des premiers minimaux communs du support ; aucune assertion d'injectivité ni résultat plus fort n'est ajouté.

Règles : FR-ALGEBRA-B33-RULE-EMBEDDED, FR-ALGEBRA-B33-RULE-SUPPORT, FR-ALGEBRA-B33-RULE-MODULE, FR-ALGEBRA-B33-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-no-embedded-primes-endos}
Let $R$ be a Noetherian ring.
Let $M$ be a finite $R$-module without embedded associated primes.
Let $I = \{x \in R \mid xM = 0\}$. Then the ring $R/I$ has no
embedded primes.
\end{lemma}

\begin{proof}
We may replace $R$ by $R/I$.
Hence we may assume every nonzero element
of $R$ acts nontrivially on $M$.
By Lemma \ref{lemma-support-closed} this implies that
$\Spec(R)$ equals the support of $M$.
Suppose that $\mathfrak p$ is an embedded prime of $R$.
Let $x \in R$ be an element whose annihilator is $\mathfrak p$.
Consider the nonzero module $N = xM \subset M$. It is annihilated
by $\mathfrak p$. Hence any associated prime $\mathfrak q$ of $N$
contains $\mathfrak p$ and is also an associated prime of $M$.
Then $\mathfrak q$ would be an embedded associated prime of
$M$ which contradicts the assumption of the lemma.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-no-embedded-primes-endos}
Soit $R$ un anneau noethérien.
Soit $M$ un $R$-module de type fini sans idéal premier associé immergé.
Soit $I = \{x \in R \mid xM = 0\}$. Alors l'anneau $R/I$ n'a aucun
idéal premier immergé.
\end{lemma}

\begin{proof}
On peut remplacer $R$ par $R/I$.
On peut donc supposer que tout élément non nul
de $R$ agit non trivialement sur $M$.
D'après le Lemme \ref{lemma-support-closed}, cela implique que
$\Spec(R)$ est égal au support de $M$.
Supposons que $\mathfrak p$ soit un idéal premier immergé de $R$.
Soit $x \in R$ un élément dont l'annulateur est $\mathfrak p$.
Considérons le module non nul $N = xM \subset M$. Il est annulé
par $\mathfrak p$. Tout idéal premier associé $\mathfrak q$ à $N$
contient donc $\mathfrak p$ et est aussi un idéal premier associé à $M$.
Alors $\mathfrak q$ serait un idéal premier associé immergé de
$M$, ce qui contredit l'hypothèse du lemme.
\end{proof}
```

</details>

## Contrôles et suite

Les 97 régions mathématiques concordent après une exception exacte préexistante : nowhere dense in → rare dans. Le préfixe de 11 748 régions passe avec quarante-trois exceptions linguistiques précisément recensées ; les différences sont vérifiées dans leur ordre et avec leurs multiplicités exactes.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items restent identiques. Aucune citation ou titre facultatif différent ne figure dans ce lot. Les opérations inverses retrouvent le lot précédent puis tous les octets du témoin public préservé. Préfixe déjà relu et suffixe encore non relu sont inchangés.

Les 600 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Suites régulières, anglais L16587 / français L16353. Aucun PDF nouveau ni publication ; restauration globale en cours.

