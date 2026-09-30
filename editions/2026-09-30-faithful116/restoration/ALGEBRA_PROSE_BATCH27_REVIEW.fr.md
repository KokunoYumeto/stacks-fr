# Applications de la théorie de la dimension

## Résultat et portée

La section complète est comparée : anglais L14731–14908 (178 lignes), français L14533–14689 (157 lignes), cinq paires complètes. 107 occurrences de règles sont contextualisées, non un décompte de tous les mots. Couverture continue : 61 sections, 535 paires et 5205 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Quatre occurrences de domaine deviennent anneau intègre, avec leurs qualificatifs local et noethérien conservés en contexte. Cet emprunt était intelligible ; il ne rendait pas les théorèmes faux. La révision établit le registre français sur un passage réellement consulté, sans modifier les objets ou les hypothèses.

Les ouverts infinis, les anneaux ayant un nombre fini de premiers, les sept conditions équivalentes et les deux critères de Jacobson sont entièrement comparés. La région length/longueur est une traduction linguistique préexistante. Aucun symbole mathématique ou renvoi ne change. Trois observations sur la source restent séparées : l’exemple p-adique ambigu, l’item éditorial résiduel et la frontière q=p dans une preuve.

Lecture produite par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. Le canon est consulté pour cette révision rétrospective, non présenté comme consulté lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch27.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH26_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH27_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH27_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH27_OCCURRENCES.json) · [Opérations](ALGEBRA_PROSE_BATCH27_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH27_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH27_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH27_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH27_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH27_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Antoine Ducros — Introduction à la théorie des schémas

[Source consultée](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages 23–24 et 122 entièrement relues : définition 0.1.3 et ses conventions, définition 2.8.14 et remarque sur la dimension un. Page 23 rendue et inspectée visuellement.

Attestations courtes : « Un anneau A est dit intègre », « anneau intègre », « Anneaux intègres de dimension 1 ».

Atteste anneau intègre pour domain, y compris la non-nullité, et le registre français de dimension et d'idéaux premiers.

Limites : La source mathématique reste Stacks. Domaine reste un emprunt intelligible, non une erreur de théorème. Les passages lus ne fournissent pas d'attestation de anneau de Jacobson, sobre ou localement fermé ; ces choix existants sont vérifiés directement contre les définitions et arguments source, sans citation documentaire inventée.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

## Modifications et motifs

Les quatre changements de registre ne sont pas comptés comme des corrections de théorèmes. Les anciens octets restent conservés et chaque opération est réversible. Aucun nouveau résultat ni qualification de source n’est ajouté.

### FR-ALGEBRA-B27-REPAIR-0001

Anglais L14740 ; français L14543.

Avant :
```tex
Soit $R$ un domaine local noethérien de dimension $\geq 2$.
```

Après :
```tex
Soit $R$ un anneau local noethérien intègre de dimension $\geq 2$.
```

Domaine local noethérien devient anneau local noethérien intègre, selon le registre effectivement lu chez Ducros. L'intégrité, la localité, la noethérianité, dim(R)≥2 et l'ouverture non vide restent identiques. La preuve réduit à l'ouvert générique, choisit x, relève les paramètres et produit un idéal premier contenant y₂ sans contenir x. Tous les quotients, baisses de dimension et renvois sont conservés.

Domaine est un emprunt reconnaissable et ne rendait pas le théorème faux ; le changement porte sur le registre français. L'exemple anglais suivant parle de p-adic numbers, ambigu entre corps et anneau d'entiers ; la traduction conserve cette ambiguïté et la signale séparément.

### FR-ALGEBRA-B27-REPAIR-0002

Anglais L14779 ; français L14583.

Avant :
```tex
Si $R$ est un domaine local, le lemme découle du Lemme
```

Après :
```tex
Si $R$ est un anneau local intègre, le lemme découle du Lemme
```

Les deux occurrences de domaine sont rendues par anneau intègre, avec local dans le premier cas. Le raisonnement passe exactement du cas local au cas intègre, puis aux quotients par les idéaux premiers minimaux. La borne ≤1 et les renvois ne changent pas.

Le texte traite la finitude du nombre d'idéaux premiers, non la finitude de l'anneau. Les cas de quotient et de localisation conservent leurs hypothèses.

### FR-ALGEBRA-B27-REPAIR-0003

Anglais L14781 ; français L14585.

Avant :
```tex
Si $R$ est un domaine, alors $R_\mathfrak m$ est de dimension $\leq 1$ pour
```

Après :
```tex
Si $R$ est un anneau intègre, alors $R_\mathfrak m$ est de dimension $\leq 1$ pour
```

Les deux occurrences de domaine sont rendues par anneau intègre, avec local dans le premier cas. Le raisonnement passe exactement du cas local au cas intègre, puis aux quotients par les idéaux premiers minimaux. La borne ≤1 et les renvois ne changent pas.

Le texte traite la finitude du nombre d'idéaux premiers, non la finitude de l'anneau. Les cas de quotient et de localisation conservent leurs hypothèses.

### FR-ALGEBRA-B27-REPAIR-0004

Anglais L14845 ; français L14649.

Avant :
```tex
\item Tout domaine noethérien $R$ de dimension $1$ qui possède une infinité
```

Après :
```tex
\item Tout anneau noethérien intègre $R$ de dimension $1$ qui possède une infinité
```

Domaine noethérien devient anneau noethérien intègre ; les conditions de dimension un et d'infinité sont inchangées. La seconde assertion distingue maximal de contenu dans une infinité de premiers. Le français conserve sobre, localement fermé, l'idéal non maximal sans premier ajouté, les localisations et les égalités officielles. La réserve q=p dans la preuve est exposée à part et n'est pas corrigée silencieusement.

Le lemme cité donne dim≤1, alors que la preuve écrit =1 pour chaque q⊃p, y compris q=p sous la convention d'inclusion non stricte. Le localisé est alors un corps de dimension zéro. La correction proposée et la distinction q=p/q≠p restent hors du français. Aucune attestation externe exacte de tous les qualificatifs topologiques n'est revendiquée dans ce lot.

## Observations séparées sur la source

Ces observations ne sont ni des corrections insérées dans la traduction, ni des admissions nouvelles au registre. Aucune revendication de déduplication globale ou de première découverte n’est faite.

### lemma-Noetherian-local-domain-dim-2-infinite-opens

[Anglais officiel L14768](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14768) · FR-ALGEBRA-B27-SOURCE-NOTE-0001.

```tex
The rings $k[[t]]$ where $k$ is a field, or the ring of $p$-adic
numbers are Noetherian rings of dimension $1$ with finitely many primes.
```

L'exemple est ambigu : le corps Q_p des nombres p-adiques a dimension zéro et un seul idéal premier, tandis que l'anneau Z_p des entiers p-adiques a dimension un avec les idéaux premiers (0) et (p). Si p-adic numbers désigne Q_p, l'assertion de dimension un est fausse ; l'exemple visé paraît être Z_p. Remplacer numbers par integers serait une clarification de source, non une réparation de français. La traduction conserve donc nombres p-adiques et la réserve reste conditionnelle.

Confiance forte sur les deux exemples standard ; confiance interprétative, non certitude, sur l'objet visé. Pas de correction admise.

### lemma-finite-type-algebra-finite-nr-primes

[Anglais officiel L14803](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14803) · FR-ALGEBRA-B27-SOURCE-NOTE-0002.

```tex
\item add more here.
```

Cet item est une instruction éditoriale résiduelle, pas une condition équivalente. La preuve conclut seulement à l'équivalence des conditions (1)–(7). Suppression de cet item suggérée pour une édition corrigée ; l'édition française fidèle le traduit et le conserve, sans inventer un huitième résultat.

Confiance forte sur la présence et la nature du placeholder ; aucune admission nouvelle au registre.

### lemma-noetherian-dim-1-Jacobson

[Anglais officiel L14878](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14878) · FR-ALGEBRA-B27-SOURCE-NOTE-0003.

```tex
we conclude that $\dim((R/\mathfrak p)_{\mathfrak q}) = 1$.
```

Le texte choisit q avec p⊂q sans exiger q≠p, puis affirme l'égalité à un pour tous ces q. Si q=p, (R/p)_p est le corps des fractions de l'anneau intègre R/p et sa dimension est zéro. Le lemme cité établit ici la borne ≤1 ; l'égalité à un vaut pour q strictement supérieur à p, car le localisé possède alors son idéal nul et un idéal maximal non nul. La preuve peut garder ≤1 pour tous les q et utiliser l'infinité des premiers contenant p pour obtenir dim(R/p)=1. Cette réparation proposée n'est pas appliquée dans la traduction. L'idéal non maximal appelé p est premier dans le contexte du résultat topologique cité, mais ce qualificatif absent n'est pas ajouté au texte.

Confiance forte sur le cas q=p et la correction de portée ; réserve de preuve séparée et réversible, non admission d'errata.

## Règles contextualisées

### FR-ALGEBRA-B27-RULE-INTEGRAL

Intégrité, non-nullité et qualificatifs locaux/noethériens vérifiés pour chacune des quatre occurrences révisées.

Canon : FR-ALGEBRA-B27-CANON-DUCROS.

### FR-ALGEBRA-B27-RULE-DIMENSION

Dimensions des anneaux et quotients, paramètres relevés et longueur distingués de cardinal ou nombre d'idéaux.

Canon : FR-ALGEBRA-B27-CANON-DUCROS.

### FR-ALGEBRA-B27-RULE-SPECTRUM

Registre topologique relu en contexte source ; pas d'attestation externe prétendue pour tous les qualificatifs.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B27-RULE-IDEAL

Finitude des idéaux premiers, minimalité et maximalité distinguées ; aucune qualification source manquante ajoutée.

Canon : FR-ALGEBRA-B27-CANON-DUCROS.

### FR-ALGEBRA-B27-RULE-LOGIC

Portée de non nul, ouvert non vide, infini et pour tout vérifiée ; placeholders et réserves de preuve consignés séparément.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-applications-dimension-theory

Anglais L14731–14737 ; français L14533–14540.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14731) · FR-ALGEBRA-B27-CHOICE-0001.

Le titre et l'objectif de la section sont fidèles : spectres infinis et nouveaux anneaux de Jacobson. Aucun résultat pédagogique ou théorème extérieur n'est ajouté.

Point particulier à relire : Contrôle complet de cette section, mais pas fin du chapitre ni de l'édition. Les règles sont contextualisées, non un remplacement aveugle de mots.

Règles : FR-ALGEBRA-B27-RULE-DIMENSION, FR-ALGEBRA-B27-RULE-SPECTRUM, FR-ALGEBRA-B27-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Applications of dimension theory}
\label{section-applications-dimension-theory}

\noindent
We can use the results on dimension to prove certain rings
have infinite spectra and to produce more Jacobson rings.
```

Français restauré :
```tex
\section{Applications de la théorie de la dimension}
\label{section-applications-dimension-theory}

\noindent
Nous pouvons utiliser les résultats sur la dimension pour montrer que certains
anneaux ont un spectre infini et pour construire de nouveaux anneaux de
Jacobson.
```

</details>

### 02 — lemma-Noetherian-local-domain-dim-2-infinite-opens

Anglais L14738–14771 ; français L14541–14574.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14738) · FR-ALGEBRA-B27-CHOICE-0002.

Domaine local noethérien devient anneau local noethérien intègre, selon le registre effectivement lu chez Ducros. L'intégrité, la localité, la noethérianité, dim(R)≥2 et l'ouverture non vide restent identiques. La preuve réduit à l'ouvert générique, choisit x, relève les paramètres et produit un idéal premier contenant y₂ sans contenir x. Tous les quotients, baisses de dimension et renvois sont conservés.

Point particulier à relire : Domaine est un emprunt reconnaissable et ne rendait pas le théorème faux ; le changement porte sur le registre français. L'exemple anglais suivant parle de p-adic numbers, ambigu entre corps et anneau d'entiers ; la traduction conserve cette ambiguïté et la signale séparément.

Règles : FR-ALGEBRA-B27-RULE-INTEGRAL, FR-ALGEBRA-B27-RULE-DIMENSION, FR-ALGEBRA-B27-RULE-SPECTRUM, FR-ALGEBRA-B27-RULE-IDEAL, FR-ALGEBRA-B27-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Noetherian-local-domain-dim-2-infinite-opens}
Let $R$ be a Noetherian local domain of dimension $\geq 2$.
A nonempty open subset $U \subset \Spec(R)$ is
infinite.
\end{lemma}

\begin{proof}
To get a contradiction, assume that $U \subset \Spec(R)$ is finite.
In this case $(0) \in U$ and $\{(0)\}$ is an open subset of $U$ (because
the complement of $\{(0)\}$ is the union of the closures of the other points).
Thus we may assume $U = \{(0)\}$.
Let $\mathfrak m \subset R$ be the maximal ideal.
We can find an $x \in \mathfrak m$, $x \not = 0$ such that
$V(x) \cup U = \Spec(R)$. In other words we see that
$D(x) = \{(0)\}$. In particular we see
that $\dim(R/xR) = \dim(R) - 1 \geq 1$, see Lemma \ref{lemma-one-equation}.
Let $\overline{y}_2, \ldots, \overline{y}_{\dim(R)} \in R/xR$ generate
an ideal of definition of $R/xR$, see Proposition \ref{proposition-dimension}.
Choose lifts $y_2, \ldots, y_{\dim(R)} \in R$, so that
$x, y_2, \ldots, y_{\dim(R)}$ generate an ideal of definition in $R$.
This implies that $\dim(R/(y_2)) = \dim(R) - 1$ and
$\dim(R/(y_2, x)) = \dim(R) - 2$, see
Lemma \ref{lemma-elements-generate-ideal-definition}.
Hence there exists a prime
$\mathfrak p$ containing $y_2$ but not $x$. This contradicts
the fact that $D(x) = \{(0)\}$.
\end{proof}

\noindent
The rings $k[[t]]$ where $k$ is a field, or the ring of $p$-adic
numbers are Noetherian rings of dimension $1$ with finitely many primes.
This is the maximum dimension for which this can happen.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-Noetherian-local-domain-dim-2-infinite-opens}
Soit $R$ un anneau local noethérien intègre de dimension $\geq 2$.
Toute partie ouverte non vide $U \subset \Spec(R)$ est infinie.
\end{lemma}

\begin{proof}
Pour obtenir une contradiction, supposons que $U \subset \Spec(R)$ soit finie.
Dans ce cas, $(0) \in U$ et $\{(0)\}$ est une partie ouverte de $U$ (car le
complémentaire de $\{(0)\}$ est la réunion des adhérences des autres points).
Nous pouvons donc supposer que $U = \{(0)\}$.
Soit $\mathfrak m \subset R$ l'idéal maximal.
Nous pouvons trouver $x \in \mathfrak m$, $x \not = 0$, tel que
$V(x) \cup U = \Spec(R)$. Autrement dit,
$D(x) = \{(0)\}$. En particulier,
$\dim(R/xR) = \dim(R) - 1 \geq 1$, voir le Lemme \ref{lemma-one-equation}.
Soient $\overline{y}_2, \ldots, \overline{y}_{\dim(R)} \in R/xR$ des éléments
engendrant un idéal de définition de $R/xR$, voir la Proposition
\ref{proposition-dimension}. Choisissons des relèvements
$y_2, \ldots, y_{\dim(R)} \in R$, de sorte que
$x, y_2, \ldots, y_{\dim(R)}$ engendrent un idéal de définition de $R$.
Il s'ensuit que $\dim(R/(y_2)) = \dim(R) - 1$ et que
$\dim(R/(y_2, x)) = \dim(R) - 2$, voir le Lemme
\ref{lemma-elements-generate-ideal-definition}.
Il existe donc un idéal premier $\mathfrak p$ contenant $y_2$ mais pas $x$.
Cela contredit l'égalité $D(x) = \{(0)\}$.
\end{proof}

\noindent
Les anneaux $k[[t]]$, où $k$ est un corps, ainsi que l'anneau des nombres
$p$-adiques sont des anneaux noethériens de dimension $1$ qui n'ont qu'un
nombre fini d'idéaux premiers. C'est la plus grande dimension pour laquelle
cela puisse se produire.
```

</details>

### 03 — lemma-Noetherian-finite-nr-primes

Anglais L14772–14789 ; français L14575–14593.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14772) · FR-ALGEBRA-B27-CHOICE-0003.

Les deux occurrences de domaine sont rendues par anneau intègre, avec local dans le premier cas. Le raisonnement passe exactement du cas local au cas intègre, puis aux quotients par les idéaux premiers minimaux. La borne ≤1 et les renvois ne changent pas.

Point particulier à relire : Le texte traite la finitude du nombre d'idéaux premiers, non la finitude de l'anneau. Les cas de quotient et de localisation conservent leurs hypothèses.

Règles : FR-ALGEBRA-B27-RULE-INTEGRAL, FR-ALGEBRA-B27-RULE-DIMENSION, FR-ALGEBRA-B27-RULE-IDEAL, FR-ALGEBRA-B27-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Noetherian-finite-nr-primes}
A Noetherian ring with finitely many primes has dimension $\leq 1$.
\end{lemma}

\begin{proof}
Let $R$ be a Noetherian ring with finitely many primes.
If $R$ is a local domain, then the lemma follows from
Lemma \ref{lemma-Noetherian-local-domain-dim-2-infinite-opens}.
If $R$ is a domain, then $R_\mathfrak m$ has dimension $\leq 1$
for all maximal ideals $\mathfrak m$ by the local case.
Hence $\dim(R) \leq 1$ by Lemma \ref{lemma-dimension-height}.
If $R$ is general, then $\dim(R/\mathfrak q) \leq 1$
for every minimal prime $\mathfrak q$ of $R$.
Since every prime contains a minimal prime
(Lemma \ref{lemma-Zariski-topology}), this implies $\dim(R) \leq 1$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-Noetherian-finite-nr-primes}
Un anneau noethérien qui n'a qu'un nombre fini d'idéaux premiers est de
dimension $\leq 1$.
\end{lemma}

\begin{proof}
Soit $R$ un anneau noethérien qui n'a qu'un nombre fini d'idéaux premiers.
Si $R$ est un anneau local intègre, le lemme découle du Lemme
\ref{lemma-Noetherian-local-domain-dim-2-infinite-opens}.
Si $R$ est un anneau intègre, alors $R_\mathfrak m$ est de dimension $\leq 1$ pour
tout idéal maximal $\mathfrak m$, d'après le cas local.
Ainsi, $\dim(R) \leq 1$ d'après le Lemme \ref{lemma-dimension-height}.
Si $R$ est quelconque, alors $\dim(R/\mathfrak q) \leq 1$ pour tout idéal premier
minimal $\mathfrak q$ de $R$. Puisque tout idéal premier contient un idéal
premier minimal (Lemme \ref{lemma-Zariski-topology}), il s'ensuit que
$\dim(R) \leq 1$.
\end{proof}
```

</details>

### 04 — lemma-finite-type-algebra-finite-nr-primes

Anglais L14790–14840 ; français L14594–14644.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14790) · FR-ALGEBRA-B27-CHOICE-0004.

La non-nullité de S, le corps k et le type fini sont explicitement conservés. Les sept conditions mathématiques restent dans le même ordre ; l'huitième item, simple instruction éditoriale anglaise, demeure traduit comme tel. La preuve conserve les implications numérotées, le Nullstellensatz, la longueur et le passage à la dimension sur k. La remarque sur la normalisation de Noether reste une remarque, pas une preuve importée.

Point particulier à relire : La réserve R=0 du lot précédent ne s'importe pas ici : S est expressément non nul. L'item add more here n'est pas une huitième propriété mathématique ; il est marqué comme défaut éditorial dans le dossier. La région length/longueur est une différence linguistique préexistante.

Règles : FR-ALGEBRA-B27-RULE-DIMENSION, FR-ALGEBRA-B27-RULE-SPECTRUM, FR-ALGEBRA-B27-RULE-IDEAL, FR-ALGEBRA-B27-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-finite-type-algebra-finite-nr-primes}
Let $S$ be a nonzero finite type algebra over a field $k$.
The following are equivalent
\begin{enumerate}
\item $\dim(S) = 0$,
\item $S$ has finitely many primes,
\item $S$ has finitely many maximal ideals,
\item $\Spec(S)$ satisfies one of the equivalent conditions of
Lemma \ref{lemma-ring-with-only-minimal-primes},
\item $\dim_k(S) < \infty$,
\item $S$ is Artinian,
\item $\Spec(S)$ is a discrete topological space,
\item add more here.
\end{enumerate}
\end{lemma}

\begin{proof}
It is immediate from the definitions that (1) is equivalent to (4)
by looking at part (5) of Lemma \ref{lemma-ring-with-only-minimal-primes}.
Recall that $\Spec(S)$ is sober, Noetherian, and Jacobson, see
Lemmas \ref{lemma-spec-spectral}, \ref{lemma-Noetherian-topology},
\ref{lemma-finite-type-field-Jacobson}, and \ref{lemma-jacobson}.
If $S$ has dimension $0$, then every point defines an
irreducible component and there are only a finite number
of irreducible components (Topology, Lemma \ref{topology-lemma-Noetherian}).
Thus (1) implies (2). Trivially (2) implies (3).
If (3) holds, then $\Spec(S)$ is discrete by
Topology, Lemma \ref{topology-lemma-finite-jacobson}
and hence the dimension of $S$ is $0$.

\medskip\noindent
At this point we know that (1) -- (4) are equivalent.
The implication (5) $\Rightarrow$ (6) is
Lemma \ref{lemma-finite-dimensional-algebra}.
The implication (6) $\Rightarrow$ (7) follows from
Proposition \ref{proposition-dimension-zero-ring}.
The implication (7) $\Rightarrow$ (4) is immediate.
Conversely, if $S$ satisfies (1) -- (4), then $S$ has finitely
many primes $\mathfrak m_1, \ldots, \mathfrak m_r$ all maximal.
Note that $\kappa(\mathfrak m_i)$ is a finite extension of $k$ by the
Hilbert Nullstellensatz (Theorem \ref{theorem-nullstellensatz}).
By Proposition \ref{proposition-dimension-zero-ring} we also see
that $S$ is Artinian. Next, Lemma \ref{lemma-artinian-finite-length}
tells us that $\text{length}_S(S) < \infty$. Thus $\dim_k(S) < \infty$ by
Lemma \ref{lemma-pushdown-module}. We conclude that
(1) -- (7) are equivalent. (Note: another and more standard
way to prove $\dim(S) = 0 \Rightarrow \dim_k(S) < \infty$
is to use Noether normalization, but we don't have this available to us yet.)
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-finite-type-algebra-finite-nr-primes}
Soit $S$ une algèbre non nulle de type fini sur un corps $k$.
Les conditions suivantes sont équivalentes :
\begin{enumerate}
\item $\dim(S) = 0$,
\item $S$ n'a qu'un nombre fini d'idéaux premiers,
\item $S$ n'a qu'un nombre fini d'idéaux maximaux,
\item $\Spec(S)$ satisfait l'une des conditions équivalentes du
Lemme \ref{lemma-ring-with-only-minimal-primes},
\item $\dim_k(S) < \infty$,
\item $S$ est artinien,
\item $\Spec(S)$ est un espace topologique discret,
\item ajouter ici d'autres conditions.
\end{enumerate}
\end{lemma}

\begin{proof}
Il résulte immédiatement des définitions que (1) équivaut à (4), en
considérant l'assertion (5) du Lemme
\ref{lemma-ring-with-only-minimal-primes}.
Rappelons que $\Spec(S)$ est sobre, noethérien et de Jacobson, voir les Lemmes
\ref{lemma-spec-spectral}, \ref{lemma-Noetherian-topology},
\ref{lemma-finite-type-field-Jacobson} et \ref{lemma-jacobson}.
Si $S$ est de dimension $0$, chaque point définit une composante irréductible,
et il n'y a qu'un nombre fini de composantes irréductibles (Topologie,
Lemme \ref{topology-lemma-Noetherian}). Ainsi, (1) implique (2).
Il est clair que (2) implique (3). Si (3) est satisfaite, alors $\Spec(S)$ est
discret d'après Topologie, Lemme \ref{topology-lemma-finite-jacobson}, et la
dimension de $S$ est donc $0$.

\medskip\noindent
Nous savons à présent que (1) -- (4) sont équivalentes.
L'implication (5) $\Rightarrow$ (6) est le Lemme
\ref{lemma-finite-dimensional-algebra}.
L'implication (6) $\Rightarrow$ (7) résulte de la Proposition
\ref{proposition-dimension-zero-ring}.
L'implication (7) $\Rightarrow$ (4) est immédiate.
Réciproquement, si $S$ satisfait (1) -- (4), alors $S$ possède un nombre fini
d'idéaux premiers $\mathfrak m_1, \ldots, \mathfrak m_r$, tous maximaux.
Remarquons que $\kappa(\mathfrak m_i)$ est une extension finie de $k$ d'après
le Nullstellensatz de Hilbert (Théorème \ref{theorem-nullstellensatz}).
La Proposition \ref{proposition-dimension-zero-ring} montre également que
$S$ est artinien. Ensuite, le Lemme \ref{lemma-artinian-finite-length} donne
$\text{longueur}_S(S) < \infty$. Ainsi, $\dim_k(S) < \infty$ d'après le
Lemme \ref{lemma-pushdown-module}. Nous concluons que (1) -- (7) sont
équivalentes. (Remarque : une autre manière, plus classique, de démontrer que
$\dim(S) = 0 \Rightarrow \dim_k(S) < \infty$ consiste à utiliser la
normalisation de Noether, mais nous ne disposons pas encore de ce résultat.)
\end{proof}
```

</details>

### 05 — lemma-noetherian-dim-1-Jacobson

Anglais L14841–14908 ; français L14645–14689.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L14841) · FR-ALGEBRA-B27-CHOICE-0005.

Domaine noethérien devient anneau noethérien intègre ; les conditions de dimension un et d'infinité sont inchangées. La seconde assertion distingue maximal de contenu dans une infinité de premiers. Le français conserve sobre, localement fermé, l'idéal non maximal sans premier ajouté, les localisations et les égalités officielles. La réserve q=p dans la preuve est exposée à part et n'est pas corrigée silencieusement.

Point particulier à relire : Le lemme cité donne dim≤1, alors que la preuve écrit =1 pour chaque q⊃p, y compris q=p sous la convention d'inclusion non stricte. Le localisé est alors un corps de dimension zéro. La correction proposée et la distinction q=p/q≠p restent hors du français. Aucune attestation externe exacte de tous les qualificatifs topologiques n'est revendiquée dans ce lot.

Règles : FR-ALGEBRA-B27-RULE-INTEGRAL, FR-ALGEBRA-B27-RULE-DIMENSION, FR-ALGEBRA-B27-RULE-SPECTRUM, FR-ALGEBRA-B27-RULE-IDEAL, FR-ALGEBRA-B27-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-noetherian-dim-1-Jacobson}
Noetherian Jacobson rings.
\begin{enumerate}
\item Any Noetherian domain $R$ of dimension $1$
with infinitely many primes is Jacobson.
\item Any Noetherian ring such that every prime
$\mathfrak p$ is either maximal or contained in
infinitely many prime ideals is Jacobson.
\end{enumerate}
\end{lemma}

\begin{proof}
Part (1) is a reformulation of Lemma \ref{lemma-pid-jacobson}.

\medskip\noindent
Let $R$ be a Noetherian ring such that
every non-maximal prime $\mathfrak p$ is contained
in infinitely many prime ideals.
Assume $\Spec(R)$ is not Jacobson to get
a contradiction.
By Lemmas \ref{lemma-irreducible}
and \ref{lemma-Noetherian-topology}
we see that $\Spec(R)$ is a sober, Noetherian topological space.
By Topology, Lemma \ref{topology-lemma-non-jacobson-Noetherian-characterize}
we see that there exists a non-maximal ideal $\mathfrak p \subset R$
such that $\{\mathfrak p\}$ is a locally closed subset of
$\Spec(R)$. In other words, $\mathfrak p$ is not maximal
and $\{\mathfrak p\}$ is an open subset of $V(\mathfrak p)$.
Consider a prime $\mathfrak q \subset R$ with
$\mathfrak p \subset \mathfrak q$. Recall that the topology on the spectrum of
$(R/\mathfrak p)_{\mathfrak q} = R_{\mathfrak q}/\mathfrak pR_{\mathfrak q}$
is induced from that of $\Spec(R)$, see Lemmas
\ref{lemma-spec-localization} and \ref{lemma-spec-closed}.
Hence we see that $\{(0)\}$ is a locally closed subset of
$\Spec((R/\mathfrak p)_{\mathfrak q})$. By
Lemma \ref{lemma-Noetherian-local-domain-dim-2-infinite-opens}
we conclude that $\dim((R/\mathfrak p)_{\mathfrak q}) = 1$.
Since this holds for every $\mathfrak q \supset \mathfrak p$
we conclude that $\dim(R/\mathfrak p) = 1$. At this point we use
the assumption that $\mathfrak p$ is contained in infinitely many
primes to see that $\Spec(R/\mathfrak p)$ is infinite.
Hence by part (1) of the lemma we see that
$V(\mathfrak p) \cong \Spec(R/\mathfrak p)$
is the closure of its closed points.
This is the desired contradiction since it means that
$\{\mathfrak p\} \subset V(\mathfrak p)$ cannot be open.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-noetherian-dim-1-Jacobson}
Anneaux de Jacobson noethériens.
\begin{enumerate}
\item Tout anneau noethérien intègre $R$ de dimension $1$ qui possède une infinité
d'idéaux premiers est un anneau de Jacobson.
\item Tout anneau noethérien tel que chaque idéal premier $\mathfrak p$ soit
maximal ou soit contenu dans une infinité d'idéaux premiers est un anneau de
Jacobson.
\end{enumerate}
\end{lemma}

\begin{proof}
L'assertion (1) est une reformulation du Lemme \ref{lemma-pid-jacobson}.

\medskip\noindent
Soit $R$ un anneau noethérien tel que tout idéal premier non maximal
$\mathfrak p$ soit contenu dans une infinité d'idéaux premiers.
Supposons, pour obtenir une contradiction, que $\Spec(R)$ ne soit pas un
espace de Jacobson. Les Lemmes \ref{lemma-irreducible} et
\ref{lemma-Noetherian-topology} montrent que $\Spec(R)$ est un espace
topologique sobre et noethérien.
D'après Topologie, Lemme
\ref{topology-lemma-non-jacobson-Noetherian-characterize}, il existe un idéal
non maximal $\mathfrak p \subset R$ tel que $\{\mathfrak p\}$ soit une partie
localement fermée de $\Spec(R)$. Autrement dit, $\mathfrak p$ n'est pas
maximal et $\{\mathfrak p\}$ est une partie ouverte de $V(\mathfrak p)$.
Considérons un idéal premier $\mathfrak q \subset R$ tel que
$\mathfrak p \subset \mathfrak q$. Rappelons que la topologie du spectre de
$(R/\mathfrak p)_{\mathfrak q} = R_{\mathfrak q}/\mathfrak pR_{\mathfrak q}$
est induite par celle de $\Spec(R)$, voir les Lemmes
\ref{lemma-spec-localization} et \ref{lemma-spec-closed}.
Ainsi, $\{(0)\}$ est une partie localement fermée de
$\Spec((R/\mathfrak p)_{\mathfrak q})$. Le Lemme
\ref{lemma-Noetherian-local-domain-dim-2-infinite-opens} donne alors
$\dim((R/\mathfrak p)_{\mathfrak q}) = 1$.
Comme cela vaut pour tout $\mathfrak q \supset \mathfrak p$, nous concluons
que $\dim(R/\mathfrak p) = 1$. Utilisons maintenant l'hypothèse selon laquelle
$\mathfrak p$ est contenu dans une infinité d'idéaux premiers : elle montre
que $\Spec(R/\mathfrak p)$ est infini. L'assertion (1) du lemme implique donc
que $V(\mathfrak p) \cong \Spec(R/\mathfrak p)$ est l'adhérence de l'ensemble
de ses points fermés. C'est la contradiction recherchée, puisque cela signifie
que $\{\mathfrak p\} \subset V(\mathfrak p)$ ne peut pas être ouvert.
\end{proof}
```

</details>

## Contrôles et suite

Les 96 régions mathématiques correspondent exactement après une exception linguistique préexistante, liée à sa position et non remplacée indistinctement. Le préfixe de 10 499 régions passe avec quarante exceptions linguistiques au total ; les différences sont vérifiées dans leur ordre et avec leurs multiplicités exactes.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items restent identiques. Aucune citation ni titre facultatif ne figure dans ce lot. Les opérations inverses retrouvent le lot précédent puis tous les octets du témoin public préservé. Préfixe déjà relu et suffixe encore non relu sont inchangés.

Les 535 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Support et dimension des modules, anglais L14909 / français L14690. Aucun PDF nouveau ni publication ; restauration globale en cours.

