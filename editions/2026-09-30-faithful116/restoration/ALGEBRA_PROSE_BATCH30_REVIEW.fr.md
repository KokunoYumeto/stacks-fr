# Puissances symboliques

## Résultat et portée

La section complète est comparée : anglais L15542–15615 (74 lignes), français L15297–15369 (73 lignes), quatre paires complètes. 34 occurrences de règles sont contextualisées, non un décompte de tous les mots. Couverture continue : 64 sections, 568 paires et 5499 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Le français est fidèle et reste inchangé. Aucune copie identique du LaTeX précédent n’est créée. Puissance symbolique, noyau, localisation, platitude et sous-quotients gardent leur sens et leurs formules exacts.

Une affirmation excessive dans la preuve anglaise, acts invertibly, reste traduite littéralement. Le contre-exemple et la correction proposée vers acts injectively sont explicités hors traduction. Il ne s’agit pas d’une erreur française ni d’un résultat à améliorer silencieusement. Une coquille grammaticale anglaise est aussi notée séparément.

Lecture produite par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. Le canon est consulté pour cette révision rétrospective, non présenté comme consulté lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX conservé](staged/fr/010_algebra.prose-batch29.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH29_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH30_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH30_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH30_OCCURRENCES.json) · [Opérations](ALGEBRA_PROSE_BATCH30_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH30_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH30_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH30_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH30_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH30_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Christian Peskine — Introduction algébrique à la géométrie projective

[Source consultée](https://perso.univ-rennes1.fr/matthieu.romagny/M2_0708/bouquin.pdf) · [Fichier conservé](canon-consulted/fr-algebra/peskine-geometrie-projective-2007.pdf)

Pages PDF 64–65 / imprimées 63–64 lues complètement dans ce lot ; page PDF64 rendue et inspectée. Définition7.45 et propositions7.46–7.48 ; théorème7.49 pour la localisation et les premiers associés. La pagePDF138, définition16.3, a déjà été lue et inspectée dans cette même continuation.

Attestations courtes : « puissances symboliques », « application de localisation ».

La définition7.45 atteste le nom puissance symbolique et sa contraction depuis la puissance dans le localisé, sur un anneau non nécessairement noethérien. Les résultats voisins attestent premiers associés, idéal primaire, localisation et module de type fini.

Limites : Aucun résultat de Peskine n'est inséré dans Stacks. Le théorème7.49 a ses propres hypothèses noethériennes/de type fini, non importées. Le contre-exemple à acts invertibly est un calcul direct dans l'hypothèse source, non une affirmation imputée à Peskine.

SHA-256 : C84D597457282B22B993F523791F4A3E391A74554FF76F7F49878640789435BA.

## Modifications et motifs

Aucune opération nouvelle. La fidélité est justifiée par la lecture complète : conserver une bonne traduction est le résultat de ce lot. La réserve sur la preuve anglaise ne devient pas une liberté éditoriale française.

## Observations séparées sur la source

Deux observations sont distinctes : l’article manquant dans be flat ring map et la suraffirmation acts invertibly. Le français est grammatical pour la première et conserve la seconde. Aucune admission, déduplication globale ou première découverte n’est revendiquée.

### lemma-symbolic-power-flat-extension

[Anglais officiel L15579](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15579) · FR-ALGEBRA-B30-SOURCE-NOTE-0001.

```tex
Let $R \to S$ be flat ring map. Let $\mathfrak p \subset R$ be a prime
```

L'anglais be flat ring map omet l'article a. Le français un morphisme d'anneaux plat rend déjà le sens grammaticalement ; aucune correction française n'est nécessaire. La proposition d'article reste séparée, sans modifier l'hypothèse de platitude.

Confiance forte sur la coquille grammaticale, aucune admission au registre.

### lemma-symbolic-power-flat-extension

[Anglais officiel L15610](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15610) · FR-ALGEBRA-B30-SOURCE-NOTE-0002.

```tex
where $V$ is a $\kappa(\mathfrak p)$ vector space. Thus $f$
acts invertibly as desired.
```

Le résultat demandé est que f soit non-diviseur de zéro, donc agisse injectivement. L'inversibilité n'est pas vraie en général. Contre-exemple dans les hypothèses : R=k, p=(0), S=k[t], q=(0), n=1, f=t. R→S est plat et q=pS est premier ; S_p/pS_p=k[t]. Le sous-quotient avec i=0 a V=k et multiplication par t est injective mais non surjective (1 n'est pas dans t·k[t]). Proposition de correction anglaise : acts injectively. Le français manière inversible reste littéral ; aucune amélioration du résultat source n'est importée.

Confiance forte, calcul élémentaire explicite ; pas d'admission, déduplication globale ou première découverte revendiquée.

## Règles contextualisées

### FR-ALGEBRA-B30-RULE-POWER

L'idéal défini par le noyau et sa puissance symbolique gardent leur construction et leur exposant exacts.

Canon : FR-ALGEBRA-B30-CANON-PESKINE.

### FR-ALGEBRA-B30-RULE-LOCALIZATION

Localisation et filtration conservent leurs objets ; la platitude source n'est pas remplacée par une hypothèse noethérienne.

Canon : FR-ALGEBRA-B30-CANON-PESKINE.

### FR-ALGEBRA-B30-RULE-LOGIC

Hypothèses, portée et conclusion sont comparées intégralement. L'inversibilité annoncée dans l'anglais reste une réserve de source, pas une correction de traduction.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-symbolic-power

Anglais L15542–15547 ; français L15297–15302.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15542) · FR-ALGEBRA-B30-CHOICE-0001.

Le titre Puissances symboliques est attesté explicitement par Peskine ; l'introduction annonce la définition sans ajouter de motivation absente de la source.

Règles : FR-ALGEBRA-B30-RULE-POWER.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Symbolic powers}
\label{section-symbolic-power}

\noindent
Here is the definition.
```

Français restauré :
```tex
\section{Puissances symboliques}
\label{section-symbolic-power}

\noindent
Voici la définition.
```

</details>

### 02 — definition-symbolic-power

Anglais L15548–15558 ; français L15303–15313.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15548) · FR-ALGEBRA-B30-CHOICE-0002.

L'idéal est défini par le même noyau, pour n≥0. La distinction entre puissance ordinaire et puissance symbolique est conservée, tout comme l'avis de non-égalité possible. Peskine atteste cette terminologie et la contraction, sans remplacer le noyau officiel.

Point particulier à relire : La définition officielle vaut pour un anneau quelconque, non uniquement noethérien. La caractérisation de Peskine par contraction ne remplace pas la formule source.

Règles : FR-ALGEBRA-B30-RULE-POWER, FR-ALGEBRA-B30-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-symbolic-power}
Let $R$ be a ring. Let $\mathfrak p$ be a prime ideal. For $n \geq 0$ the
$n$th {\it symbolic power} of $\mathfrak p$ is the ideal
$\mathfrak p^{(n)} = \Ker(R \to R_\mathfrak p/\mathfrak p^nR_\mathfrak p)$.
\end{definition}

\noindent
Note that $\mathfrak p^n \subset \mathfrak p^{(n)}$ but equality does
not always hold.
```

Français restauré :
```tex
\begin{definition}
\label{definition-symbolic-power}
Soit $R$ un anneau. Soit $\mathfrak p$ un idéal premier. Pour $n \geq 0$, la
$n$-ième {\it puissance symbolique} de $\mathfrak p$ est l'idéal
$\mathfrak p^{(n)} = \Ker(R \to R_\mathfrak p/\mathfrak p^nR_\mathfrak p)$.
\end{definition}

\noindent
Remarquons que $\mathfrak p^n \subset \mathfrak p^{(n)}$, mais qu'il n'y a
pas toujours égalité.
```

</details>

### 03 — lemma-symbolic-power-associated

Anglais L15559–15576 ; français L15314–15331.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15559) · FR-ALGEBRA-B30-CHOICE-0003.

La noethérianité, n>0, le singleton de premiers associés, les deux inclusions et la multiplication par un élément hors p restent exacts. Le raccourci R∩p^nR_p désigne la contraction, même si l'application de localisation n'est pas injective ; aucune injection de R n'est ajoutée.

Règles : FR-ALGEBRA-B30-RULE-POWER, FR-ALGEBRA-B30-RULE-LOCALIZATION, FR-ALGEBRA-B30-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-symbolic-power-associated}
Let $R$ be a Noetherian ring.
Let $\mathfrak p$ be a prime ideal.
Let $n > 0$. Then $\text{Ass}(R/\mathfrak p^{(n)}) = \{\mathfrak p\}$.
\end{lemma}

\begin{proof}
If $\mathfrak q$ is an associated prime of $R/\mathfrak p^{(n)}$
then clearly $\mathfrak p \subset \mathfrak q$.
On the other hand, any element $x \in R$, $x \not \in \mathfrak p$
is a nonzerodivisor on $R/\mathfrak p^{(n)}$.
Namely, if $y \in R$ and
$xy \in \mathfrak p^{(n)} = R \cap \mathfrak p^nR_{\mathfrak p}$
then $y \in \mathfrak p^nR_{\mathfrak p}$, hence $y \in \mathfrak p^{(n)}$.
Hence the lemma follows.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-symbolic-power-associated}
Soit $R$ un anneau noethérien.
Soit $\mathfrak p$ un idéal premier.
Soit $n > 0$. Alors $\text{Ass}(R/\mathfrak p^{(n)}) = \{\mathfrak p\}$.
\end{lemma}

\begin{proof}
Si $\mathfrak q$ est un idéal premier associé à $R/\mathfrak p^{(n)}$, alors
$\mathfrak p \subset \mathfrak q$ manifestement.
D'autre part, tout élément $x \in R$, $x \not \in \mathfrak p$, est un
non-diviseur de zéro dans $R/\mathfrak p^{(n)}$.
En effet, si $y \in R$ et
$xy \in \mathfrak p^{(n)} = R \cap \mathfrak p^nR_{\mathfrak p}$, alors
$y \in \mathfrak p^nR_{\mathfrak p}$, d'où
$y \in \mathfrak p^{(n)}$. Le lemme en découle.
\end{proof}
```

</details>

### 04 — lemma-symbolic-power-flat-extension

Anglais L15577–15615 ; français L15332–15369.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15577) · FR-ALGEBRA-B30-CHOICE-0004.

La platitude et la primalité de pS restent explicites. Les deux noyaux, la flèche, la localisation et les sous-quotients filtrés sont comparés terme à terme. Le français final manière inversible rend exactement acts invertibly ; son excès mathématique vient de la source et est signalé séparément, pas réparé silencieusement.

Point particulier à relire : L'injectivité suffit, l'inversibilité peut échouer. Remplacer ici inversible par injective améliorerait la preuve source, ce qui est exclu pour cette traduction diplomatique. Il ne s'agit pas d'une faute introduite par le français. La phrase montrant la flèche et disant est injectif reste lisible comme elliptique pour le morphisme ; une réécriture de style n'est pas nécessaire.

Règles : FR-ALGEBRA-B30-RULE-POWER, FR-ALGEBRA-B30-RULE-LOCALIZATION, FR-ALGEBRA-B30-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-symbolic-power-flat-extension}
Let $R \to S$ be flat ring map. Let $\mathfrak p \subset R$ be a prime
such that $\mathfrak q = \mathfrak p S$ is a prime of $S$.
Then $\mathfrak p^{(n)} S = \mathfrak q^{(n)}$.
\end{lemma}

\begin{proof}
Since
$\mathfrak p^{(n)} = \Ker(R \to R_\mathfrak p/\mathfrak p^nR_\mathfrak p)$
we see using flatness that $\mathfrak p^{(n)} S$ is the kernel of the map
$S \to S_\mathfrak p/\mathfrak p^nS_\mathfrak p$. On the other hand
$\mathfrak q^{(n)}$ is the kernel of the map
$S \to S_\mathfrak q/\mathfrak q^nS_\mathfrak q =
S_\mathfrak q/\mathfrak p^nS_\mathfrak q$. Hence it suffices
to show that
$$
S_\mathfrak p/\mathfrak p^nS_\mathfrak p
\longrightarrow
S_\mathfrak q/\mathfrak p^nS_\mathfrak q
$$
is injective. Observe that the right hand module is the localization
of the left hand module by elements $f \in S$, $f \not \in \mathfrak q$.
Thus it suffices to show these elements are nonzerodivisors on
$S_\mathfrak p/\mathfrak p^nS_\mathfrak p$. By flatness, the module
$S_\mathfrak p/\mathfrak p^nS_\mathfrak p$ has a finite filtration whose
subquotients are
$$
\mathfrak p^iS_\mathfrak p/\mathfrak p^{i + 1}S_\mathfrak p
\cong \mathfrak p^iR_\mathfrak p/\mathfrak p^{i + 1}R_\mathfrak p
\otimes_{R_\mathfrak p} S_\mathfrak p \cong
V \otimes_{\kappa(\mathfrak p)} (S/\mathfrak q)_\mathfrak p
$$
where $V$ is a $\kappa(\mathfrak p)$ vector space. Thus $f$
acts invertibly as desired.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-symbolic-power-flat-extension}
Soit $R \to S$ un morphisme d'anneaux plat. Soit $\mathfrak p \subset R$ un
idéal premier tel que $\mathfrak q = \mathfrak p S$ soit un idéal premier de
$S$. Alors $\mathfrak p^{(n)} S = \mathfrak q^{(n)}$.
\end{lemma}

\begin{proof}
Puisque
$\mathfrak p^{(n)} = \Ker(R \to R_\mathfrak p/\mathfrak p^nR_\mathfrak p)$,
la platitude montre que $\mathfrak p^{(n)} S$ est le noyau du morphisme
$S \to S_\mathfrak p/\mathfrak p^nS_\mathfrak p$. D'autre part,
$\mathfrak q^{(n)}$ est le noyau du morphisme
$S \to S_\mathfrak q/\mathfrak q^nS_\mathfrak q =
S_\mathfrak q/\mathfrak p^nS_\mathfrak q$. Il suffit donc de montrer que
$$
S_\mathfrak p/\mathfrak p^nS_\mathfrak p
\longrightarrow
S_\mathfrak q/\mathfrak p^nS_\mathfrak q
$$
est injectif. Remarquons que le module de droite est le localisé du module de
gauche par les éléments $f \in S$, $f \not \in \mathfrak q$.
Il suffit donc de montrer que ces éléments sont des non-diviseurs de zéro dans
$S_\mathfrak p/\mathfrak p^nS_\mathfrak p$. Par platitude, le module
$S_\mathfrak p/\mathfrak p^nS_\mathfrak p$ possède une filtration finie dont
les sous-quotients sont
$$
\mathfrak p^iS_\mathfrak p/\mathfrak p^{i + 1}S_\mathfrak p
\cong \mathfrak p^iR_\mathfrak p/\mathfrak p^{i + 1}R_\mathfrak p
\otimes_{R_\mathfrak p} S_\mathfrak p \cong
V \otimes_{\kappa(\mathfrak p)} (S/\mathfrak q)_\mathfrak p
$$
où $V$ est un espace vectoriel sur $\kappa(\mathfrak p)$. Ainsi, $f$ agit de
manière inversible, comme voulu.
\end{proof}
```

</details>

## Contrôles et suite

Les 40 régions mathématiques de cette section sont identiques, sans exception. Le préfixe de 11 001 régions passe avec les quarante et une exceptions linguistiques antérieures ; les différences sont vérifiées dans leur ordre et avec leurs multiplicités exactes.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items restent identiques. Aucune citation ou titre facultatif différent ne figure dans ce lot. Les opérations inverses retrouvent le lot précédent puis tous les octets du témoin public préservé. Préfixe déjà relu et suffixe encore non relu sont inchangés.

Les 568 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Assassin relatif, anglais L15616 / français L15370. Aucun PDF nouveau ni publication ; restauration globale en cours.

