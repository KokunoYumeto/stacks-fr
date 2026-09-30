# Idéaux premiers faiblement associés

## Résultat et portée

La section entière est comparée : anglais L15925–16444 et français L15691–16210, 520 lignes chacun, vingt paires complètes. 173 occurrences de règles sont contextualisées, non un décompte de tous les mots. Couverture continue : 66 sections, 595 paires et 5815 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Le français est fidèle et reste inchangé. Aucun LaTeX identique supplémentaire n’est créé. La distinction entre premier associé et faiblement associé, la minimalité relative à un annulateur, les cas sans noethérianité, les images sur les spectres et toute la preuve de changement de corps sont comparés intégralement.

Cinq observations anglaises restent hors traduction : the prove, objet S_q plutôt que M_q, p∈R, indice x_n et appartenance d’un élément du module à l’idéal annulateur. La réserve sur le cas z=0 de l’argument d’injectivité est également explicitée, sans déclarer l’énoncé faux.

Lecture produite par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. Le canon est consulté rétrospectivement, non présenté comme consulté lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX conservé](staged/fr/010_algebra.prose-batch29.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH31_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH32_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH32_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH32_OCCURRENCES.json) · [Opérations](ALGEBRA_PROSE_BATCH32_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH32_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH32_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH32_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH32_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH32_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### C. Picavet — Sur une généralisation de la notion de spectre d’anneau

[Source consultée](https://www.numdam.org/item/ASCFM_1970__44_7_81_0.pdf) · [Fichier conservé](canon-consulted/fr-algebra/weakly-associated-annales-1970.pdf)

Article1970, pp.81–101. Couverture PDF1 et pagesPDF2–3 / imprimées81–82 lues en entier ; PDF3 rendu et inspecté. Définition4, proposition3 et ses deux corollaires ; conventions de la page81. Manuscrit reçu le28avril1969, distinct de la publication1970.

Attestations courtes : « faiblement associé », « idéaux premiers faiblement associés », « partie multiplicative », « annulateur ».

La définition4 impose un premier minimal parmi ceux contenant l'annulateur d'un élément : même sens que WeakAss. La proposition3 relie les premiers faiblement associés de A/I à l'injectivité de l'homothétie ; appui du registre sur diviseurs de zéro, radical, réunion et intersection.

Limites : Seules ces pages sont consultées, non l'article entier. Ses notations Assf ne remplacent pas WeakAss. Le cas A/I ne sert pas à importer un résultat dans une assertion de Stacks pour un module arbitraire.

SHA-256 : CFFA9D9E1293F5D36A68E0896DA203B2964D5C70C6730E94D6F00753C32A3FEA.

### Christian Peskine — Introduction algébrique à la géométrie projective

[Source consultée](https://perso.univ-rennes1.fr/matthieu.romagny/M2_0708/bouquin.pdf) · [Fichier conservé](canon-consulted/fr-algebra/peskine-geometrie-projective-2007.pdf)

Pages PDF84,86,138,144 / imprimées83,85,137,143 effectivement relues dans le passage immédiatement précédent de cette même continuation ; théorème10.1, lemme10.4, proposition16.1 et définition16.3.

Attestations courtes : « anneau intègre », « non diviseur de 0 dans M ».

Le registre anneau intègre, corps des fractions et non-diviseur de zéro dans un module est pertinent aux deux derniers lemmes. La terminologie des premiers associés sert à distinguer Ass de WeakAss, pas à effacer cette différence.

Limites : Pas de nouvelle attestation de faiblement associé imputée à Peskine. Ses propres hypothèses noethériennes/de type fini ne deviennent pas celles de Stacks.

SHA-256 : C84D597457282B22B993F523791F4A3E391A74554FF76F7F49878640789435BA.

## Modifications et motifs

Aucune opération nouvelle. La fidélité est justifiée par la lecture complète : conserver une bonne traduction est le résultat de ce lot. Les réserves sur la notation anglaise ne deviennent pas une liberté éditoriale française.

## Observations séparées sur la source

Cinq observations sont distinctes : grammaire, objet du module, domaine d’un premier, indice de variable et appartenance à l’annulateur. Le français reste conforme au témoin officiel. Aucune admission, déduplication globale ou première découverte n’est revendiquée.

### lemma-ass-weakly-ass

[Anglais officiel L16128](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16128) · FR-ALGEBRA-B32-SOURCE-NOTE-0001.

```tex
It is enough the prove the implication
```

La phrase exige to prove, non the prove. Le français Il suffit de démontrer rend idiomatiquement la phrase ; aucune opération française.

Confiance forte sur la grammaire ; sans admission ou déduplication globale.

### lemma-weakly-ass-finite-ring-map

[Anglais officiel L16240](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16240) · FR-ALGEBRA-B32-SOURCE-NOTE-0002.

```tex
map to zero in $S_{\mathfrak q}$.
```

ym est un élément de M, module S arbitraire ; il n'a pas d'image canonique dans S_q. L'argument précédent et le suivant portent sur M_{q_i} et M_q. Correction proposée : M_q. Le français conserve S_q ; il s'agit d'une erreur d'objet source, non introduite par la traduction.

Confiance forte sur le type de l'objet ; pas d'admission ni première découverte.

### lemma-localize-weakly-ass

[Anglais officiel L16291](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16291) · FR-ALGEBRA-B32-SOURCE-NOTE-0003.

```tex
since for $\mathfrak p \in R$, $S \cap \mathfrak p = \emptyset$ we have
```

p est un idéal premier et l'expression S∩p et le localisé R_p le montrent. p∈R traite à tort le premier comme élément ; proposition : p∈Spec(R). Le français garde la formule officielle.

Confiance forte sur la convention de type ; aucune admission ni déduplication globale.

### lemma-weakly-ass-change-fields

[Anglais officiel L16421](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16421) · FR-ALGEBRA-B32-SOURCE-NOTE-0004.

```tex
of $\kappa(\mathfrak p)[x_1, \ldots, x_n]$ and
```

Le paragraphe a fixé K=k(x_1,...,x_r). Le localisé décrit R/p⊗_kK avec les r variables ; n venait du degré d'une extension finie dans une réduction antérieure et n'est pas le nombre de variables. Correction proposée : x_r dans la borne finale. Le français conserve x_n.

Confiance forte sur l'incohérence d'indice ; aucune admission ou première découverte.

### lemma-weakly-ass-change-fields

[Anglais officiel L16430](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16430) · FR-ALGEBRA-B32-SOURCE-NOTE-0005.

```tex
$g f^n z \in J$, i.e., $g f^n z = 0$.
```

J est l'idéal annulateur de z dans R⊗_kK, tandis que gf^nz est un élément du module M⊗_kK. Appartenir à J devrait porter sur gf^n : gf^n∈J est équivalent à gf^nz=0. La proposition est donc de supprimer z avant ∈J, et non dans l'égalité suivante. Le français garde les deux expressions de la source.

Confiance forte sur le typage et l'équivalence par définition d'annulateur ; aucune admission ou déduplication globale.

## Règles contextualisées

### FR-ALGEBRA-B32-RULE-ASSOCIATED

Minimal au-dessus de l'annulateur reste distinct d'égal à l'annulateur. Les occurrences sont vérifiées dans les passages complets.

Canon : FR-ALGEBRA-B32-CANON-PICAVET.

### FR-ALGEBRA-B32-RULE-MODULE

Les objets modules, parties finies et morphismes finis sont distingués ; aucune finitude manquante n'est ajoutée.

Canon : FR-ALGEBRA-B32-CANON-PESKINE.

### FR-ALGEBRA-B32-RULE-LOCALIZATION

Localisation et action injective conservent leurs rôles. Les résultats source généraux ne sont pas réduits aux conditions noethériennes du canon voisin.

Canon : FR-ALGEBRA-B32-CANON-PICAVET, FR-ALGEBRA-B32-CANON-PESKINE.

### FR-ALGEBRA-B32-RULE-LOGIC

Quantificateurs, minimalité relative, sens d'inclusion et dépendance des hypothèses sont lus dans leur contexte entier.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-weakly-ass

Anglais L15925–15931 ; français L15691–15697.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15925) · FR-ALGEBRA-B32-CHOICE-0001.

Idéaux premiers faiblement associés est directement attesté par Picavet. L'introduction conserve l'intérêt pour les anneaux non noethériens et les modules non de type fini ; aucune restriction supplémentaire.

Règles : FR-ALGEBRA-B32-RULE-ASSOCIATED, FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Weakly associated primes}
\label{section-weakly-ass}

\noindent
This is a variant on the notion of an associated prime that is useful
for non-Noetherian ring and non-finite modules.
```

Français restauré :
```tex
\section{Idéaux premiers faiblement associés}
\label{section-weakly-ass}

\noindent
Il s'agit d'une variante de la notion d'idéal premier associé qui est utile
pour les anneaux non noethériens et les modules qui ne sont pas de type fini.
```

</details>

### 02 — definition-weakly-associated

Anglais L15932–15946 ; français L15698–15712.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15932) · FR-ALGEBRA-B32-CHOICE-0002.

La définition conserve l'existence d'un élément et la minimalité parmi les premiers contenant son annulateur, non l'égalité du premier à l'annulateur. Picavet définition4 a exactement cette distinction. Les notations WeakAss restent identiques ; l'inclusion de Ass et la transition vers la localisation sont fidèles.

Point particulier à relire : Ne pas substituer premier associé à faiblement associé. Le canon de Picavet est lu rétrospectivement et ne prouve pas qu'il avait été consulté pendant la traduction initiale.

Règles : FR-ALGEBRA-B32-RULE-ASSOCIATED, FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOCALIZATION, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-weakly-associated}
Let $R$ be a ring. Let $M$ be an $R$-module.
A prime $\mathfrak p$ of $R$ is {\it weakly associated} to $M$
if there exists an element $m \in M$ such that $\mathfrak p$ is minimal
among the prime ideals containing the annihilator
$\text{Ann}(m) = \{f \in R \mid fm = 0\}$.
The set of all such primes is denoted $\text{WeakAss}_R(M)$
or $\text{WeakAss}(M)$.
\end{definition}

\noindent
Thus an associated prime is a weakly associated prime.
Here is a characterization in terms of the localization at the prime.
```

Français restauré :
```tex
\begin{definition}
\label{definition-weakly-associated}
Soit $R$ un anneau. Soit $M$ un $R$-module.
Un idéal premier $\mathfrak p$ de $R$ est {\it faiblement associé} à $M$
s'il existe un élément $m \in M$ tel que $\mathfrak p$ soit minimal
parmi les idéaux premiers contenant l'annulateur
$\text{Ann}(m) = \{f \in R \mid fm = 0\}$.
L'ensemble de tous ces idéaux premiers est noté $\text{WeakAss}_R(M)$
ou $\text{WeakAss}(M)$.
\end{definition}

\noindent
Ainsi, tout idéal premier associé est faiblement associé.
Voici une caractérisation à l'aide de la localisation en l'idéal premier.
```

</details>

### 03 — lemma-weakly-ass-local

Anglais L15947–15984 ; français L15713–15750.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15947) · FR-ALGEBRA-B32-CHOICE-0003.

Les trois conditions et les trois implications sont comparées intégralement. Radical de l'annulateur et annulateur lui-même ne sont pas confondus. L'exactitude de la localisation et la minimalité dans l'ensemble des premiers contenant I gardent leurs sens.

Point particulier à relire : Le premier minimal est minimal parmi ceux contenant l'annulateur ; le mot minimal ne doit pas devenir une minimalité absolue dans Spec(R).

Règles : FR-ALGEBRA-B32-RULE-ASSOCIATED, FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOCALIZATION, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-weakly-ass-local}
Let $R$ be a ring. Let $M$ be an $R$-module.
Let $\mathfrak p$ be a prime of $R$.
The following are equivalent:
\begin{enumerate}
\item $\mathfrak p$ is weakly associated to $M$,
\item $\mathfrak pR_{\mathfrak p}$ is weakly associated to $M_{\mathfrak p}$,
and
\item $M_{\mathfrak p}$ contains an element whose
annihilator has radical equal to $\mathfrak pR_{\mathfrak p}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Assume (1). Then there exists an element $m \in M$ such that
$\mathfrak p$ is minimal among the primes containing the annihilator
$I = \{x \in R \mid xm = 0\}$ of $m$. As localization is exact, the
annihilator of $m$ in $M_{\mathfrak p}$ is $I_{\mathfrak p}$.
Hence $\mathfrak pR_{\mathfrak p}$ is a minimal prime of
$R_{\mathfrak p}$ containing the annihilator $I_{\mathfrak p}$
of $m$ in $M_{\mathfrak p}$. This implies (2) holds, and also (3)
as it implies that $\sqrt{I_{\mathfrak p}} = \mathfrak pR_{\mathfrak p}$.

\medskip\noindent
Applying the implication (1) $\Rightarrow$ (3) to $M_{\mathfrak p}$
over $R_{\mathfrak p}$ we see that (2) $\Rightarrow$ (3).

\medskip\noindent
Finally, assume (3). This means there exists an element
$m/f \in M_{\mathfrak p}$ whose annihilator has radical equal
to $\mathfrak pR_{\mathfrak p}$. Then the annihilator
$I = \{x \in R \mid xm = 0\}$ of $m$ in $M$ is such that
$\sqrt{I_{\mathfrak p}} = \mathfrak pR_{\mathfrak p}$. Clearly
this means that $\mathfrak p$ contains $I$ and is minimal among the
primes containing $I$, i.e., (1) holds.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-weakly-ass-local}
Soit $R$ un anneau. Soit $M$ un $R$-module.
Soit $\mathfrak p$ un idéal premier de $R$.
Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item $\mathfrak p$ est faiblement associé à $M$,
\item $\mathfrak pR_{\mathfrak p}$ est faiblement associé à $M_{\mathfrak p}$,
et
\item $M_{\mathfrak p}$ contient un élément dont
l'annulateur a pour radical $\mathfrak pR_{\mathfrak p}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Supposons (1). Il existe alors un élément $m \in M$ tel que
$\mathfrak p$ soit minimal parmi les idéaux premiers contenant l'annulateur
$I = \{x \in R \mid xm = 0\}$ de $m$. Comme la localisation est exacte,
l'annulateur de $m$ dans $M_{\mathfrak p}$ est $I_{\mathfrak p}$.
Ainsi, $\mathfrak pR_{\mathfrak p}$ est un idéal premier minimal de
$R_{\mathfrak p}$ contenant l'annulateur $I_{\mathfrak p}$
de $m$ dans $M_{\mathfrak p}$. Ceci montre (2), ainsi que (3),
car $\sqrt{I_{\mathfrak p}} = \mathfrak pR_{\mathfrak p}$.

\medskip\noindent
En appliquant l'implication (1) $\Rightarrow$ (3) à $M_{\mathfrak p}$
sur $R_{\mathfrak p}$, on voit que (2) $\Rightarrow$ (3).

\medskip\noindent
Enfin, supposons (3). Il existe donc un élément
$m/f \in M_{\mathfrak p}$ dont l'annulateur a pour radical
$\mathfrak pR_{\mathfrak p}$. L'annulateur
$I = \{x \in R \mid xm = 0\}$ de $m$ dans $M$ vérifie alors
$\sqrt{I_{\mathfrak p}} = \mathfrak pR_{\mathfrak p}$. Cela signifie
clairement que $\mathfrak p$ contient $I$ et est minimal parmi les
idéaux premiers contenant $I$, c'est-à-dire que (1) est vérifiée.
\end{proof}
```

</details>

### 04 — lemma-reduced-weakly-ass-minimal

Anglais L15985–16002 ; français L15751–15768.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15985) · FR-ALGEBRA-B32-CHOICE-0004.

Réduit, local, inversible, nilpotence et corps traduisent les mêmes objets. La contradiction x=0 est conservée sans supposer une noethérianité absente. L'énoncé identifie les premiers minimaux, non tous les premiers.

Règles : FR-ALGEBRA-B32-RULE-ASSOCIATED.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-reduced-weakly-ass-minimal}
For a reduced ring the weakly associated primes of the ring are
the minimal primes.
\end{lemma}

\begin{proof}
Let $(R, \mathfrak m)$ be a reduced local ring.
Suppose $x \in R$ is an element whose annihilator
has radical $\mathfrak m$. If $\mathfrak m \not = 0$, then $x$
cannot be a unit, so $x \in \mathfrak m$. Then in particular $x^{1 + n} = 0$
for some $n \geq 0$. Hence $x = 0$. Which contradicts the assumption
that the annihilator of $x$ is contained in $\mathfrak m$.
Thus we see that $\mathfrak m = 0$, i.e., $R$ is a field.
By Lemma \ref{lemma-weakly-ass-local} this
implies the statement of the lemma.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-reduced-weakly-ass-minimal}
Pour un anneau réduit, les idéaux premiers faiblement associés à l'anneau sont
les idéaux premiers minimaux.
\end{lemma}

\begin{proof}
Soit $(R, \mathfrak m)$ un anneau local réduit.
Supposons que $x \in R$ soit un élément dont l'annulateur
a pour radical $\mathfrak m$. Si $\mathfrak m \not = 0$, alors $x$
ne peut pas être inversible, donc $x \in \mathfrak m$. En particulier, $x^{1 + n} = 0$
pour un certain $n \geq 0$. Ainsi $x = 0$, ce qui contredit l'hypothèse
selon laquelle l'annulateur de $x$ est contenu dans $\mathfrak m$.
On voit donc que $\mathfrak m = 0$, c'est-à-dire que $R$ est un corps.
Le Lemme \ref{lemma-weakly-ass-local} donne alors
l'assertion du lemme.
\end{proof}
```

</details>

### 05 — lemma-weakly-ass

Anglais L16003–16027 ; français L15769–15793.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16003) · FR-ALGEBRA-B32-CHOICE-0005.

La suite exacte courte et les deux inclusions gardent leur ordre. La preuve localisée distingue image nulle et image non nulle, avec le radical de l'annulateur dans les deux cas ; elle n'invoque pas l'égalité Ass=WeakAss.

Règles : FR-ALGEBRA-B32-RULE-ASSOCIATED, FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOCALIZATION, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-weakly-ass}
Let $R$ be a ring.
Let $0 \to M' \to M \to M'' \to 0$ be a short exact sequence
of $R$-modules.
Then $\text{WeakAss}(M') \subset \text{WeakAss}(M)$ and
$\text{WeakAss}(M) \subset \text{WeakAss}(M') \cup \text{WeakAss}(M'')$.
\end{lemma}

\begin{proof}
We will use the characterization of weakly associated primes of
Lemma \ref{lemma-weakly-ass-local}.
Let $\mathfrak p$ be a prime of $R$. As localization is exact we obtain
the short exact sequence
$0 \to M'_{\mathfrak p} \to M_{\mathfrak p} \to M''_{\mathfrak p} \to 0$.
Suppose that $m \in M_{\mathfrak p}$ is an element whose annihilator
has radical $\mathfrak pR_{\mathfrak p}$. Then either the image $\overline{m}$
of $m$ in $M''_{\mathfrak p}$ is zero and $m \in M'_{\mathfrak p}$, or the
radical of the annihilator of $\overline{m}$ is $\mathfrak pR_{\mathfrak p}$.
This proves that
$\text{WeakAss}(M) \subset \text{WeakAss}(M') \cup \text{WeakAss}(M'')$.
The inclusion $\text{WeakAss}(M') \subset \text{WeakAss}(M)$ is immediate
from the definitions.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-weakly-ass}
Soit $R$ un anneau.
Soit $0 \to M' \to M \to M'' \to 0$ une suite exacte courte
de $R$-modules.
Alors $\text{WeakAss}(M') \subset \text{WeakAss}(M)$ et
$\text{WeakAss}(M) \subset \text{WeakAss}(M') \cup \text{WeakAss}(M'')$.
\end{lemma}

\begin{proof}
Nous utiliserons la caractérisation des idéaux premiers faiblement associés du
Lemme \ref{lemma-weakly-ass-local}.
Soit $\mathfrak p$ un idéal premier de $R$. L'exactitude de la localisation donne
la suite exacte courte
$0 \to M'_{\mathfrak p} \to M_{\mathfrak p} \to M''_{\mathfrak p} \to 0$.
Supposons que $m \in M_{\mathfrak p}$ soit un élément dont l'annulateur
a pour radical $\mathfrak pR_{\mathfrak p}$. Alors, ou bien l'image $\overline{m}$
de $m$ dans $M''_{\mathfrak p}$ est nulle et $m \in M'_{\mathfrak p}$, ou bien le
radical de l'annulateur de $\overline{m}$ est $\mathfrak pR_{\mathfrak p}$.
Ceci montre que
$\text{WeakAss}(M) \subset \text{WeakAss}(M') \cup \text{WeakAss}(M'')$.
L'inclusion $\text{WeakAss}(M') \subset \text{WeakAss}(M)$ résulte immédiatement
des définitions.
\end{proof}
```

</details>

### 06 — lemma-weakly-ass-zero

Anglais L16028–16051 ; français L15794–15817.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16028) · FR-ALGEBRA-B32-CHOICE-0006.

Le slogan Tout module non nul possède conserve le résultat source ; aucun slogan n'est supprimé. Le cas nul, le choix d'un élément non nul, l'inclusion R/I→M et l'existence d'un premier minimal sont comparés avec leurs renvois.

Règles : FR-ALGEBRA-B32-RULE-ASSOCIATED, FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-weakly-ass-zero}
\begin{slogan}
Every nonzero module has a weakly associated prime.
\end{slogan}
Let $R$ be a ring. Let $M$ be an $R$-module. Then
$$
M = (0) \Leftrightarrow \text{WeakAss}(M) = \emptyset
$$
\end{lemma}

\begin{proof}
If $M = (0)$ then $\text{WeakAss}(M) = \emptyset$ by definition.
Conversely, suppose that $M \not = 0$. Pick a nonzero element $m \in M$.
Write $I = \{x \in R \mid xm = 0\}$ the annihilator of $m$.
Then $R/I \subset M$. Hence $\text{WeakAss}(R/I) \subset \text{WeakAss}(M)$ by
Lemma \ref{lemma-weakly-ass}.
But as $I \not = R$ we have $V(I) = \Spec(R/I)$ contains a minimal
prime, see
Lemmas \ref{lemma-Zariski-topology} and
\ref{lemma-spec-closed},
and we win.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-weakly-ass-zero}
\begin{slogan}
Tout module non nul possède un idéal premier faiblement associé.
\end{slogan}
Soit $R$ un anneau. Soit $M$ un $R$-module. Alors
$$
M = (0) \Leftrightarrow \text{WeakAss}(M) = \emptyset
$$
\end{lemma}

\begin{proof}
Si $M = (0)$, alors $\text{WeakAss}(M) = \emptyset$ par définition.
Réciproquement, supposons $M \not = 0$. Choisissons un élément non nul $m \in M$.
Notons $I = \{x \in R \mid xm = 0\}$ l'annulateur de $m$.
Alors $R/I \subset M$. Ainsi $\text{WeakAss}(R/I) \subset \text{WeakAss}(M)$ par le
Lemme \ref{lemma-weakly-ass}.
Or, puisque $I \not = R$, l'ensemble $V(I) = \Spec(R/I)$ contient un idéal premier
minimal ; voir les
Lemmes \ref{lemma-Zariski-topology} et
\ref{lemma-spec-closed},
ce qui conclut.
\end{proof}
```

</details>

### 07 — lemma-weakly-ass-support

Anglais L16052–16066 ; français L15818–15832.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16052) · FR-ALGEBRA-B32-CHOICE-0007.

Les deux inclusions Ass⊂WeakAss⊂Supp sont identiques. Le support est lié au localisé non nul, non à un annulateur unique de tout M.

Règles : FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-weakly-ass-support}
Let $R$ be a ring. Let $M$ be an $R$-module. Then
$$
\text{Ass}(M) \subset \text{WeakAss}(M) \subset \text{Supp}(M).
$$
\end{lemma}

\begin{proof}
The first inclusion is immediate from the definitions.
If $\mathfrak p \in \text{WeakAss}(M)$, then by
Lemma \ref{lemma-weakly-ass-local}
we have $M_{\mathfrak p} \not = 0$, hence $\mathfrak p \in \text{Supp}(M)$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-weakly-ass-support}
Soit $R$ un anneau. Soit $M$ un $R$-module. Alors
$$
\text{Ass}(M) \subset \text{WeakAss}(M) \subset \text{Supp}(M).
$$
\end{lemma}

\begin{proof}
La première inclusion résulte immédiatement des définitions.
Si $\mathfrak p \in \text{WeakAss}(M)$, alors, d'après le
Lemme \ref{lemma-weakly-ass-local},
on a $M_{\mathfrak p} \not = 0$, donc $\mathfrak p \in \text{Supp}(M)$.
\end{proof}
```

</details>

### 08 — lemma-weakly-ass-zero-divisors

Anglais L16067–16091 ; français L15833–15857.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16067) · FR-ALGEBRA-B32-CHOICE-0008.

La réunion des premiers faiblement associés reste exactement l'ensemble des diviseurs de zéro sur M. Picavet proposition3 confirme ce registre dans le cas A/I. La preuve conserve le choix du plus petit exposant n et l'élément non nul f^{n-1}gm ; l'inverse emploie le sous-module annulé par f.

Règles : FR-ALGEBRA-B32-RULE-ASSOCIATED, FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOCALIZATION, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-weakly-ass-zero-divisors}
Let $R$ be a ring.
Let $M$ be an $R$-module.
The union $\bigcup_{\mathfrak q \in \text{WeakAss}(M)} \mathfrak q$
is the set of elements of $R$ which are zerodivisors on $M$.
\end{lemma}

\begin{proof}
Suppose $f \in \mathfrak q \in \text{WeakAss}(M)$.
Then there exists an element $m \in M$ such that
$\mathfrak q$ is minimal over $I = \{x \in R \mid xm = 0\}$.
Hence there exists a $g \in R$, $g \not \in \mathfrak q$ and $n > 0$
such that $f^ngm = 0$. Note that $gm \not = 0$ as $g \not \in I$.
If we take $n$ minimal as above, then $f (f^{n - 1}gm) = 0$
and $f^{n - 1}gm \not = 0$, so $f$ is a zerodivisor on $M$.
Conversely, suppose $f \in R$ is a zerodivisor on $M$.
Consider the submodule $N = \{m \in M \mid fm = 0\}$.
Since $N$ is not zero it has a weakly associated prime $\mathfrak q$ by
Lemma \ref{lemma-weakly-ass-zero}.
Clearly $f \in \mathfrak q$ and by
Lemma \ref{lemma-weakly-ass}
$\mathfrak q$ is a weakly associated prime of $M$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-weakly-ass-zero-divisors}
Soit $R$ un anneau.
Soit $M$ un $R$-module.
La réunion $\bigcup_{\mathfrak q \in \text{WeakAss}(M)} \mathfrak q$
est l'ensemble des éléments de $R$ qui sont des diviseurs de zéro sur $M$.
\end{lemma}

\begin{proof}
Supposons $f \in \mathfrak q \in \text{WeakAss}(M)$.
Il existe un élément $m \in M$ tel que
$\mathfrak q$ soit minimal au-dessus de $I = \{x \in R \mid xm = 0\}$.
Il existe donc $g \in R$, avec $g \not \in \mathfrak q$, et $n > 0$
tels que $f^ngm = 0$. Remarquons que $gm \not = 0$ puisque $g \not \in I$.
Si l'on choisit $n$ minimal avec cette propriété, alors $f (f^{n - 1}gm) = 0$
et $f^{n - 1}gm \not = 0$ ; ainsi $f$ est un diviseur de zéro sur $M$.
Réciproquement, supposons que $f \in R$ soit un diviseur de zéro sur $M$.
Considérons le sous-module $N = \{m \in M \mid fm = 0\}$.
Comme $N$ n'est pas nul, il possède un idéal premier faiblement associé $\mathfrak q$ par le
Lemme \ref{lemma-weakly-ass-zero}.
On a clairement $f \in \mathfrak q$ et, d'après le
Lemme \ref{lemma-weakly-ass},
$\mathfrak q$ est un idéal premier faiblement associé à $M$.
\end{proof}
```

</details>

### 09 — lemma-weakly-ass-minimal-prime-support

Anglais L16092–16113 ; français L15858–15879.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16092) · FR-ALGEBRA-B32-CHOICE-0009.

La minimalité est dans Supp(M), pas dans Spec(R) tout entier. Le singleton du support localisé, la non-vacuité de WeakAss et le retour par localisation restent exacts.

Règles : FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-weakly-ass-minimal-prime-support}
Let $R$ be a ring.
Let $M$ be an $R$-module.
Any $\mathfrak p \in \text{Supp}(M)$ which is minimal among the elements
of $\text{Supp}(M)$ is an element of $\text{WeakAss}(M)$.
\end{lemma}

\begin{proof}
Note that $\text{Supp}(M_{\mathfrak p}) = \{\mathfrak pR_{\mathfrak p}\}$
in $\Spec(R_{\mathfrak p})$. In particular $M_{\mathfrak p}$
is nonzero, and hence $\text{WeakAss}(M_{\mathfrak p}) \not = \emptyset$ by
Lemma \ref{lemma-weakly-ass-zero}.
Since $\text{WeakAss}(M_{\mathfrak p}) \subset \text{Supp}(M_{\mathfrak p})$
by
Lemma \ref{lemma-weakly-ass-support}
we conclude that
$\text{WeakAss}(M_{\mathfrak p}) = \{\mathfrak pR_{\mathfrak p}\}$,
whence $\mathfrak p \in \text{WeakAss}(M)$ by
Lemma \ref{lemma-weakly-ass-local}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-weakly-ass-minimal-prime-support}
Soit $R$ un anneau.
Soit $M$ un $R$-module.
Tout $\mathfrak p \in \text{Supp}(M)$ qui est minimal parmi les éléments
de $\text{Supp}(M)$ appartient à $\text{WeakAss}(M)$.
\end{lemma}

\begin{proof}
Remarquons que $\text{Supp}(M_{\mathfrak p}) = \{\mathfrak pR_{\mathfrak p}\}$
dans $\Spec(R_{\mathfrak p})$. En particulier, $M_{\mathfrak p}$
est non nul, et donc $\text{WeakAss}(M_{\mathfrak p}) \not = \emptyset$ d'après le
Lemme \ref{lemma-weakly-ass-zero}.
Puisque $\text{WeakAss}(M_{\mathfrak p}) \subset \text{Supp}(M_{\mathfrak p})$
d'après le
Lemme \ref{lemma-weakly-ass-support},
on en déduit que
$\text{WeakAss}(M_{\mathfrak p}) = \{\mathfrak pR_{\mathfrak p}\}$,
d'où $\mathfrak p \in \text{WeakAss}(M)$ par le
Lemme \ref{lemma-weakly-ass-local}.
\end{proof}
```

</details>

### 10 — lemma-ass-weakly-ass

Anglais L16114–16145 ; français L15880–15911.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16114) · FR-ALGEBRA-B32-CHOICE-0010.

La génération finie porte sur p, non sur M. La noethérianité est une conséquence suffisante, non l'hypothèse initiale du lemme. La réduction de la somme des exposants et le passage de l'annulateur localisé à Ass sont lus complètement. Le français Il suffit de démontrer rend idiomatiquement la coquille enough the prove.

Règles : FR-ALGEBRA-B32-RULE-ASSOCIATED, FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ass-weakly-ass}
Let $R$ be a ring. Let $M$ be an $R$-module.
Let $\mathfrak p$ be a prime ideal of $R$ which is finitely generated.
Then
$$
\mathfrak p \in \text{Ass}(M) \Leftrightarrow
\mathfrak p \in \text{WeakAss}(M).
$$
In particular, if $R$ is Noetherian, then $\text{Ass}(M) = \text{WeakAss}(M)$.
\end{lemma}

\begin{proof}
Write $\mathfrak p = (g_1, \ldots, g_n)$ for some $g_i \in R$.
It is enough the prove the implication ``$\Leftarrow$'' as the other
implication holds in general, see
Lemma \ref{lemma-weakly-ass-support}.
Assume $\mathfrak p \in \text{WeakAss}(M)$.
By
Lemma \ref{lemma-weakly-ass-local}
there exists an element $m \in M_{\mathfrak p}$ such that
$I = \{x \in R_{\mathfrak p} \mid xm = 0\}$ has radical
$\mathfrak pR_{\mathfrak p}$. Hence for each $i$ there exists
a smallest $e_i > 0$ such that $g_i^{e_i}m = 0$ in $M_{\mathfrak p}$.
If $e_i > 1$ for some $i$, then we can replace $m$ by
$g_i^{e_i - 1} m \not = 0$ and decrease $\sum e_i$.
Hence we may assume that the annihilator of $m \in M_{\mathfrak p}$ is
$(g_1, \ldots, g_n)R_{\mathfrak p} = \mathfrak p R_{\mathfrak p}$. By
Lemma \ref{lemma-associated-primes-localize}
we see that $\mathfrak p \in \text{Ass}(M)$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ass-weakly-ass}
Soit $R$ un anneau. Soit $M$ un $R$-module.
Soit $\mathfrak p$ un idéal premier de $R$ qui est de type fini.
Alors
$$
\mathfrak p \in \text{Ass}(M) \Leftrightarrow
\mathfrak p \in \text{WeakAss}(M).
$$
En particulier, si $R$ est noethérien, alors $\text{Ass}(M) = \text{WeakAss}(M)$.
\end{lemma}

\begin{proof}
Écrivons $\mathfrak p = (g_1, \ldots, g_n)$ avec $g_i \in R$.
Il suffit de démontrer l'implication « $\Leftarrow$ », puisque l'autre
implication est toujours vraie ; voir le
Lemme \ref{lemma-weakly-ass-support}.
Supposons $\mathfrak p \in \text{WeakAss}(M)$.
D'après le
Lemme \ref{lemma-weakly-ass-local},
il existe un élément $m \in M_{\mathfrak p}$ tel que
$I = \{x \in R_{\mathfrak p} \mid xm = 0\}$ ait pour radical
$\mathfrak pR_{\mathfrak p}$. Pour tout $i$, il existe donc
un plus petit $e_i > 0$ tel que $g_i^{e_i}m = 0$ dans $M_{\mathfrak p}$.
Si $e_i > 1$ pour un certain $i$, on peut remplacer $m$ par
$g_i^{e_i - 1} m \not = 0$ et diminuer $\sum e_i$.
On peut donc supposer que l'annulateur de $m \in M_{\mathfrak p}$ est
$(g_1, \ldots, g_n)R_{\mathfrak p} = \mathfrak p R_{\mathfrak p}$. Le
Lemme \ref{lemma-associated-primes-localize}
montre alors que $\mathfrak p \in \text{Ass}(M)$.
\end{proof}
```

</details>

### 11 — remark-weakly-ass-not-functorial

Anglais L16146–16167 ; français L15912–15933.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16146) · FR-ALGEBRA-B32-CHOICE-0011.

La non-inclusion, l'anneau à une infinité de variables, le module S et le premier q sont inchangés. Les détails restent omis, comme dans l'anglais. Pas d'ajout d'une preuve ni de réparation de l'exemple. Homomorphisme et morphisme d'anneaux sont ici synonymes, non une différence de classe de morphismes.

Règles : FR-ALGEBRA-B32-RULE-ASSOCIATED, FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{remark}
\label{remark-weakly-ass-not-functorial}
Let $\varphi : R \to S$ be a ring map. Let $M$ be an $S$-module.
Then it is not always the case that
$\Spec(\varphi)(\text{WeakAss}_S(M)) \subset \text{WeakAss}_R(M)$
contrary to the case of associated primes (see
Lemma \ref{lemma-ass-functorial}).
An example is to consider the ring map
$$
R = k[x_1, x_2, x_3, \ldots] \to
S = k[x_1, x_2, x_3, \ldots, y_1, y_2, y_3, \ldots]/
(x_1y_1, x_2y_2, x_3y_3, \ldots)
$$
and $M = S$. In this case $\mathfrak q = \sum x_iS$ is a minimal prime of
$S$, hence a weakly associated prime of $M = S$ (see
Lemma \ref{lemma-weakly-ass-minimal-prime-support}).
But on the other hand, for any nonzero element of $S$ the annihilator
in $R$ is finitely generated, and hence does not
have radical equal to $R \cap \mathfrak q = (x_1, x_2, x_3, \ldots)$
(details omitted).
\end{remark}
```

Français restauré :
```tex
\begin{remark}
\label{remark-weakly-ass-not-functorial}
Soit $\varphi : R \to S$ un homomorphisme d'anneaux. Soit $M$ un $S$-module.
On n'a pas toujours
$\Spec(\varphi)(\text{WeakAss}_S(M)) \subset \text{WeakAss}_R(M)$
contrairement au cas des idéaux premiers associés (voir le
Lemme \ref{lemma-ass-functorial}).
Un exemple est donné par l'homomorphisme d'anneaux
$$
R = k[x_1, x_2, x_3, \ldots] \to
S = k[x_1, x_2, x_3, \ldots, y_1, y_2, y_3, \ldots]/
(x_1y_1, x_2y_2, x_3y_3, \ldots)
$$
et par $M = S$. Dans ce cas, $\mathfrak q = \sum x_iS$ est un idéal premier minimal de
$S$, donc un idéal premier faiblement associé à $M = S$ (voir le
Lemme \ref{lemma-weakly-ass-minimal-prime-support}).
Mais, d'autre part, pour tout élément non nul de $S$, son annulateur dans $R$
est de type fini et n'a donc pas
pour radical $R \cap \mathfrak q = (x_1, x_2, x_3, \ldots)$
(détails omis).
\end{remark}
```

</details>

### 12 — lemma-weakly-ass-reverse-functorial

Anglais L16168–16187 ; français L15934–15953.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16168) · FR-ALGEBRA-B32-CHOICE-0012.

Le sens inverse de l'inclusion sur les images de spectres est exact. S_p est localisé par les éléments de R hors p, non automatiquement par un premier de S. Annulateur, extension de l'idéal et premier minimal au-dessus de J restent les mêmes.

Règles : FR-ALGEBRA-B32-RULE-ASSOCIATED, FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-weakly-ass-reverse-functorial}
Let $\varphi : R \to S$ be a ring map. Let $M$ be an $S$-module.
Then we have
$\Spec(\varphi)(\text{WeakAss}_S(M)) \supset \text{WeakAss}_R(M)$.
\end{lemma}

\begin{proof}
Let $\mathfrak p$ be an element of $\text{WeakAss}_R(M)$.
Then there exists an $m \in M_{\mathfrak p}$ whose annihilator
$I = \{x \in R_{\mathfrak p} \mid xm = 0\}$ has radical
$\mathfrak pR_{\mathfrak p}$. Consider the annihilator
$J = \{x \in S_{\mathfrak p} \mid xm = 0 \}$ of $m$ in $S_{\mathfrak p}$.
As $IS_{\mathfrak p} \subset J$ we see that any minimal prime
$\mathfrak q \subset S_{\mathfrak p}$ over $J$ lies over $\mathfrak p$.
Moreover such a $\mathfrak q$ corresponds to a weakly associated prime
of $M$ for example by
Lemma \ref{lemma-weakly-ass-local}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-weakly-ass-reverse-functorial}
Soit $\varphi : R \to S$ un homomorphisme d'anneaux. Soit $M$ un $S$-module.
Alors on a
$\Spec(\varphi)(\text{WeakAss}_S(M)) \supset \text{WeakAss}_R(M)$.
\end{lemma}

\begin{proof}
Soit $\mathfrak p$ un élément de $\text{WeakAss}_R(M)$.
Il existe alors $m \in M_{\mathfrak p}$ dont l'annulateur
$I = \{x \in R_{\mathfrak p} \mid xm = 0\}$ a pour radical
$\mathfrak pR_{\mathfrak p}$. Considérons l'annulateur
$J = \{x \in S_{\mathfrak p} \mid xm = 0 \}$ de $m$ dans $S_{\mathfrak p}$.
Comme $IS_{\mathfrak p} \subset J$, tout idéal premier minimal
$\mathfrak q \subset S_{\mathfrak p}$ au-dessus de $J$ est au-dessus de $\mathfrak p$.
De plus, un tel $\mathfrak q$ correspond à un idéal premier faiblement associé
à $M$, par exemple d'après le
Lemme \ref{lemma-weakly-ass-local}.
\end{proof}
```

</details>

### 13 — remark-ass-functorial

Anglais L16188–16210 ; français L15954–15976.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16188) · FR-ALGEBRA-B32-CHOICE-0013.

La chaîne des quatre ensembles, la possibilité d'inclusions strictes et la condition S noethérien sont conservées. Les deux extrêmes sont égaux désigne les ensembles extérieurs, non seulement deux flèches. Aucune noethérianité de R n'est ajoutée.

Règles : FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOCALIZATION, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{remark}
\label{remark-ass-functorial}
Let $\varphi : R \to S$ be a ring map. Let $M$ be an $S$-module.
Denote $f : \Spec(S) \to \Spec(R)$ the associated map on spectra.
Then we have
$$
f(\text{Ass}_S(M)) \subset
\text{Ass}_R(M) \subset
\text{WeakAss}_R(M) \subset
f(\text{WeakAss}_S(M))
$$
see
Lemmas \ref{lemma-ass-functorial},
\ref{lemma-weakly-ass-reverse-functorial}, and
\ref{lemma-weakly-ass-support}.
In general all of the inclusions may be strict, see
Remarks \ref{remark-ass-reverse-functorial} and
\ref{remark-weakly-ass-not-functorial}.
If $S$ is Noetherian, then all the inclusions are equalities as
the outer two are equal by
Lemma \ref{lemma-ass-weakly-ass}.
\end{remark}
```

Français restauré :
```tex
\begin{remark}
\label{remark-ass-functorial}
Soit $\varphi : R \to S$ un homomorphisme d'anneaux. Soit $M$ un $S$-module.
Notons $f : \Spec(S) \to \Spec(R)$ l'application induite sur les spectres.
Alors on a
$$
f(\text{Ass}_S(M)) \subset
\text{Ass}_R(M) \subset
\text{WeakAss}_R(M) \subset
f(\text{WeakAss}_S(M))
$$
voir les
Lemmes \ref{lemma-ass-functorial},
\ref{lemma-weakly-ass-reverse-functorial} et
\ref{lemma-weakly-ass-support}.
En général, toutes les inclusions peuvent être strictes ; voir les
Remarques \ref{remark-ass-reverse-functorial} et
\ref{remark-weakly-ass-not-functorial}.
Si $S$ est noethérien, alors toutes les inclusions sont des égalités puisque,
d'après le
Lemme \ref{lemma-ass-weakly-ass}, les deux extrêmes sont égaux.
\end{remark}
```

</details>

### 14 — lemma-weakly-ass-finite-ring-map

Anglais L16211–16255 ; français L15977–16021.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16211) · FR-ALGEBRA-B32-CHOICE-0014.

Fini signifie S module de type fini sur R, non seulement morphisme de type fini. Les premiers au-dessus de p, le choix de x et y, le passage semi-local et le théorème de montée sont comparés dans la preuve entière. La phrase portant sur ym dans S_q est déjà dans la source ; son erreur d'objet est signalée à part et demeure littérale en français.

Point particulier à relire : Ne pas changer S_q en M_q : cela réparerait la source, pas le français. Le morphisme fini n'est pas remplacé par de type fini.

Règles : FR-ALGEBRA-B32-RULE-ASSOCIATED, FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOCALIZATION, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-weakly-ass-finite-ring-map}
Let $\varphi : R \to S$ be a ring map. Let $M$ be an $S$-module.
Denote $f : \Spec(S) \to \Spec(R)$ the associated map on spectra.
If $\varphi$ is a finite ring map, then
$$
\text{WeakAss}_R(M) = f(\text{WeakAss}_S(M)).
$$
\end{lemma}

\begin{proof}
One of the inclusions has already been proved, see
Remark \ref{remark-ass-functorial}.
To prove the other assume $\mathfrak q \in \text{WeakAss}_S(M)$
and let $\mathfrak p$ be the corresponding prime of $R$. Let $m \in M$
be an element such that $\mathfrak q$ is a minimal prime over
$J = \{g \in S \mid gm = 0\}$. Thus the radical of
$JS_{\mathfrak q}$ is $\mathfrak qS_{\mathfrak q}$.
As $R \to S$ is finite there are
finitely many primes
$\mathfrak q = \mathfrak q_1, \mathfrak q_2, \ldots, \mathfrak q_l$
over $\mathfrak p$, see
Lemma \ref{lemma-finite-finite-fibres}.
Pick $x \in \mathfrak q$ with $x \not \in \mathfrak q_i$ for $i > 1$, see
Lemma \ref{lemma-silly}.
By the above there exists an element $y \in S$, $y \not \in \mathfrak q$
and an integer $t > 0$ such that $y x^t m = 0$. Thus the element
$ym \in M$ is annihilated by $x^t$, hence $ym$ maps to zero in
$M_{\mathfrak q_i}$, $i = 2, \ldots, l$. To be sure, $ym$ does not
map to zero in $S_{\mathfrak q}$.

\medskip\noindent
The ring $S_{\mathfrak p}$ is semi-local with maximal ideals
$\mathfrak q_i S_{\mathfrak p}$ by going up for finite ring maps, see
Lemma \ref{lemma-integral-going-up}.
If $f \in \mathfrak pR_{\mathfrak p}$ then some power of $f$ ends
up in $JS_{\mathfrak q}$ hence for some $t > 0$ we see that
$f^t ym$ maps to zero in $M_{\mathfrak q}$. As $ym$ vanishes at the
other maximal ideals of $S_{\mathfrak p}$ we conclude that $f^t ym$ is zero
in $M_{\mathfrak p}$, see
Lemma \ref{lemma-characterize-zero-local}.
In this way we see that $\mathfrak p$ is a minimal prime over
the annihilator of $ym$ in $R$ and we win.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-weakly-ass-finite-ring-map}
Soit $\varphi : R \to S$ un homomorphisme d'anneaux. Soit $M$ un $S$-module.
Notons $f : \Spec(S) \to \Spec(R)$ l'application induite sur les spectres.
Si $\varphi$ est un homomorphisme d'anneaux fini, alors
$$
\text{WeakAss}_R(M) = f(\text{WeakAss}_S(M)).
$$
\end{lemma}

\begin{proof}
L'une des inclusions a déjà été démontrée ; voir la
Remarque \ref{remark-ass-functorial}.
Pour démontrer l'autre, supposons $\mathfrak q \in \text{WeakAss}_S(M)$
et soit $\mathfrak p$ l'idéal premier correspondant de $R$. Soit $m \in M$
un élément tel que $\mathfrak q$ soit un idéal premier minimal au-dessus de
$J = \{g \in S \mid gm = 0\}$. Le radical de
$JS_{\mathfrak q}$ est donc $\mathfrak qS_{\mathfrak q}$.
Comme $R \to S$ est fini, il n'existe qu'un nombre
fini d'idéaux premiers
$\mathfrak q = \mathfrak q_1, \mathfrak q_2, \ldots, \mathfrak q_l$
au-dessus de $\mathfrak p$ ; voir le
Lemme \ref{lemma-finite-finite-fibres}.
Choisissons $x \in \mathfrak q$ tel que $x \not \in \mathfrak q_i$ pour $i > 1$ ; voir le
Lemme \ref{lemma-silly}.
D'après ce qui précède, il existe un élément $y \in S$, avec $y \not \in \mathfrak q$,
et un entier $t > 0$ tels que $y x^t m = 0$. Ainsi, l'élément
$ym \in M$ est annulé par $x^t$ ; ainsi $ym$ a une image nulle dans
$M_{\mathfrak q_i}$ pour $i = 2, \ldots, l$. En revanche, l'image de $ym$ n'est
pas nulle dans $S_{\mathfrak q}$.

\medskip\noindent
L'anneau $S_{\mathfrak p}$ est semi-local, d'idéaux maximaux
$\mathfrak q_i S_{\mathfrak p}$, par le théorème de montée pour les homomorphismes
d'anneaux finis ; voir le Lemme \ref{lemma-integral-going-up}.
Si $f \in \mathfrak pR_{\mathfrak p}$, une puissance de $f$ appartient
à $JS_{\mathfrak q}$ ; ainsi, pour un certain $t > 0$, l'image de
$f^t ym$ est nulle dans $M_{\mathfrak q}$. Comme $ym$ s'annule aux
autres idéaux maximaux de $S_{\mathfrak p}$, on en déduit que $f^t ym$ est nul
dans $M_{\mathfrak p}$ ; voir le
Lemme \ref{lemma-characterize-zero-local}.
On voit ainsi que $\mathfrak p$ est un idéal premier minimal au-dessus de
l'annulateur de $ym$ dans $R$, ce qui conclut.
\end{proof}
```

</details>

### 15 — lemma-weakly-ass-quotient-ring

Anglais L16256–16269 ; français L16022–16035.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16256) · FR-ALGEBRA-B32-CHOICE-0015.

L'injection canonique des spectres et les deux anneaux de calcul de WeakAss sont inchangés. La preuve reste le cas particulier cité, sans nouvelle démonstration.

Règles : FR-ALGEBRA-B32-RULE-MODULE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-weakly-ass-quotient-ring}
Let $R$ be a ring.
Let $I$ be an ideal.
Let $M$ be an $R/I$-module.
Via the canonical injection
$\Spec(R/I) \to \Spec(R)$
we have $\text{WeakAss}_{R/I}(M) = \text{WeakAss}_R(M)$.
\end{lemma}

\begin{proof}
Special case of Lemma \ref{lemma-weakly-ass-finite-ring-map}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-weakly-ass-quotient-ring}
Soit $R$ un anneau.
Soit $I$ un idéal.
Soit $M$ un $R/I$-module.
Par l'injection canonique
$\Spec(R/I) \to \Spec(R)$
on a $\text{WeakAss}_{R/I}(M) = \text{WeakAss}_R(M)$.
\end{lemma}

\begin{proof}
C'est un cas particulier du Lemme \ref{lemma-weakly-ass-finite-ring-map}.
\end{proof}
```

</details>

### 16 — lemma-localize-weakly-ass

Anglais L16270–16294 ; français L16036–16060.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16270) · FR-ALGEBRA-B32-CHOICE-0016.

Partie multiplicative, correspondance bijective des premiers et deux égalités conservent leur sens. Le cas I=R est maintenu, les vérifications sont omises selon l'original. p∈R reste source-littéral, avec sa réserve de type distincte.

Point particulier à relire : p est un idéal premier, non un élément de R. Cette coquille est source-littérale et séparée.

Règles : FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOCALIZATION, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-localize-weakly-ass}
Let $R$ be a ring. Let $M$ be an $R$-module.
Let $S \subset R$ be a multiplicative subset.
Via the canonical injection $\Spec(S^{-1}R) \to \Spec(R)$
we have $\text{WeakAss}_R(S^{-1}M) = \text{WeakAss}_{S^{-1}R}(S^{-1}M)$
and
$$
\text{WeakAss}(M) \cap \Spec(S^{-1}R) = \text{WeakAss}(S^{-1}M).
$$
\end{lemma}

\begin{proof}
Suppose that $m \in S^{-1}M$. Let $I = \{x \in R \mid xm = 0\}$
and $I' = \{x' \in S^{-1}R \mid x'm = 0\}$. Then $I' = S^{-1}I$
and $I \cap S = \emptyset$ unless $I = R$ (verifications omitted).
Thus primes in $S^{-1}R$ minimal over $I'$ correspond bijectively
to primes in $R$ minimal over $I$ and avoiding $S$. This proves the
equality $\text{WeakAss}_R(S^{-1}M) = \text{WeakAss}_{S^{-1}R}(S^{-1}M)$.
The second equality follows from
Lemma \ref{lemma-weakly-ass-local}
since for $\mathfrak p \in R$, $S \cap \mathfrak p = \emptyset$ we have
$M_{\mathfrak p} = (S^{-1}M)_{S^{-1}\mathfrak p}$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-localize-weakly-ass}
Soit $R$ un anneau. Soit $M$ un $R$-module.
Soit $S \subset R$ une partie multiplicative.
Par l'injection canonique $\Spec(S^{-1}R) \to \Spec(R)$,
on a $\text{WeakAss}_R(S^{-1}M) = \text{WeakAss}_{S^{-1}R}(S^{-1}M)$
et
$$
\text{WeakAss}(M) \cap \Spec(S^{-1}R) = \text{WeakAss}(S^{-1}M).
$$
\end{lemma}

\begin{proof}
Supposons $m \in S^{-1}M$. Soient $I = \{x \in R \mid xm = 0\}$
et $I' = \{x' \in S^{-1}R \mid x'm = 0\}$. Alors $I' = S^{-1}I$
et $I \cap S = \emptyset$, sauf si $I = R$ (vérifications omises).
Ainsi, les idéaux premiers de $S^{-1}R$ minimaux au-dessus de $I'$ correspondent bijectivement
aux idéaux premiers de $R$ minimaux au-dessus de $I$ et disjoints de $S$. Ceci démontre
l'égalité $\text{WeakAss}_R(S^{-1}M) = \text{WeakAss}_{S^{-1}R}(S^{-1}M)$.
La seconde égalité résulte du
Lemme \ref{lemma-weakly-ass-local},
car, pour $\mathfrak p \in R$ tel que $S \cap \mathfrak p = \emptyset$, on a
$M_{\mathfrak p} = (S^{-1}M)_{S^{-1}\mathfrak p}$.
\end{proof}
```

</details>

### 17 — lemma-localize-weakly-ass-nonzero-divisors

Anglais L16295–16315 ; français L16061–16081.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16295) · FR-ALGEBRA-B32-CHOICE-0017.

L'action injective des éléments de S est la seule hypothèse supplémentaire. L'inclusion M→S^{-1}M, puis l'égalité des annulateurs de n et n/s, ne sont pas remplacées par une hypothèse de finitude ou d'inversibilité sur M.

Règles : FR-ALGEBRA-B32-RULE-ASSOCIATED, FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOCALIZATION, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-localize-weakly-ass-nonzero-divisors}
Let $R$ be a ring. Let $M$ be an $R$-module.
Let $S \subset R$ be a multiplicative subset.
Assume that every $s \in S$ is a nonzerodivisor on $M$.
Then
$$
\text{WeakAss}(M) = \text{WeakAss}(S^{-1}M).
$$
\end{lemma}

\begin{proof}
As $M \subset S^{-1}M$ by assumption we obtain
$\text{WeakAss}(M) \subset \text{WeakAss}(S^{-1}M)$ from
Lemma \ref{lemma-weakly-ass}.
Conversely, suppose that $n/s \in S^{-1}M$ is an element with annihilator
$I$ and $\mathfrak p$ a prime which is minimal over $I$.
Then the annihilator of $n \in M$ is $I$ and $\mathfrak p$ is a prime
minimal over $I$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-localize-weakly-ass-nonzero-divisors}
Soit $R$ un anneau. Soit $M$ un $R$-module.
Soit $S \subset R$ une partie multiplicative.
Supposons que tout $s \in S$ soit un non-diviseur de zéro sur $M$.
Alors
$$
\text{WeakAss}(M) = \text{WeakAss}(S^{-1}M).
$$
\end{lemma}

\begin{proof}
Puisque, par hypothèse, $M \subset S^{-1}M$, le
Lemme \ref{lemma-weakly-ass} donne
$\text{WeakAss}(M) \subset \text{WeakAss}(S^{-1}M)$.
Réciproquement, soit $n/s \in S^{-1}M$ un élément d'annulateur
$I$, et soit $\mathfrak p$ un idéal premier minimal au-dessus de $I$.
Alors l'annulateur de $n \in M$ est $I$, et $\mathfrak p$ est un idéal premier
minimal au-dessus de $I$.
\end{proof}
```

</details>

### 18 — lemma-zero-at-weakly-ass-zero

Anglais L16316–16337 ; français L16082–16103.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16316) · FR-ALGEBRA-B32-CHOICE-0018.

L'application au produit des localisés, non à leur somme directe, reste injective. L'argument suit le module cyclique Rx et la contradiction de son support au premier faiblement associé ; tous les renvois sont identiques.

Règles : FR-ALGEBRA-B32-RULE-ASSOCIATED, FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-zero-at-weakly-ass-zero}
Let $R$ be a ring. Let $M$ be an $R$-module. The map
$$
M
\longrightarrow
\prod\nolimits_{\mathfrak p \in \text{WeakAss}(M)} M_{\mathfrak p}
$$
is injective.
\end{lemma}

\begin{proof}
Let $x \in M$ be an element of the kernel of the map. Set
$N = Rx \subset M$. If $\mathfrak p$ is a weakly associated prime of $N$
we see on the one hand that $\mathfrak p \in \text{WeakAss}(M)$
(Lemma \ref{lemma-weakly-ass})
and on the other hand that $N_{\mathfrak p} \subset M_{\mathfrak p}$
is not zero. This contradiction shows that $\text{WeakAss}(N) = \emptyset$.
Hence $N = 0$, i.e., $x = 0$ by
Lemma \ref{lemma-weakly-ass-zero}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-zero-at-weakly-ass-zero}
Soit $R$ un anneau. Soit $M$ un $R$-module. L'application
$$
M
\longrightarrow
\prod\nolimits_{\mathfrak p \in \text{WeakAss}(M)} M_{\mathfrak p}
$$
est injective.
\end{lemma}

\begin{proof}
Soit $x \in M$ un élément du noyau de l'application. Posons
$N = Rx \subset M$. Si $\mathfrak p$ est un idéal premier faiblement associé à $N$,
on a d'une part $\mathfrak p \in \text{WeakAss}(M)$
(Lemme \ref{lemma-weakly-ass})
et, d'autre part, $N_{\mathfrak p} \subset M_{\mathfrak p}$
n'est pas nul. Cette contradiction montre que $\text{WeakAss}(N) = \emptyset$.
Ainsi $N = 0$, c'est-à-dire $x = 0$, d'après le
Lemme \ref{lemma-weakly-ass-zero}.
\end{proof}
```

</details>

### 19 — lemma-weak-post-bourbaki

Anglais L16338–16359 ; français L16104–16125.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16338) · FR-ALGEBRA-B32-CHOICE-0019.

R intègre et corps des fractions sont conformes au registre lu chez Peskine. N est plat, sans condition de fidélité ni de finitude. La multiplication par x non nul reste injective, pas bijective.

Règles : FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOCALIZATION, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-weak-post-bourbaki}
Let $R \to S$ be a ring map.
Let $N$ be an $S$-module.
Assume $N$ is flat as an $R$-module and
$R$ is a domain with fraction field $K$.
Then
$$
\text{WeakAss}_S(N) = \text{WeakAss}_{S \otimes_R K}(N \otimes_R K)
$$
via the canonical inclusion
$\Spec(S \otimes_R K) \subset \Spec(S)$.
\end{lemma}

\begin{proof}
Note that $S \otimes_R K = (R \setminus \{0\})^{-1}S$ and
$N \otimes_R K = (R \setminus \{0\})^{-1}N$.
For any nonzero $x \in R$ multiplication by $x$ on $N$ is injective as
$N$ is flat over $R$. Hence the lemma follows from
Lemma \ref{lemma-localize-weakly-ass-nonzero-divisors}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-weak-post-bourbaki}
Soit $R \to S$ un homomorphisme d'anneaux.
Soit $N$ un $S$-module.
Supposons que $N$ soit plat comme $R$-module et que
$R$ soit intègre, de corps des fractions $K$.
Alors
$$
\text{WeakAss}_S(N) = \text{WeakAss}_{S \otimes_R K}(N \otimes_R K)
$$
par l'inclusion canonique
$\Spec(S \otimes_R K) \subset \Spec(S)$.
\end{lemma}

\begin{proof}
Remarquons que $S \otimes_R K = (R \setminus \{0\})^{-1}S$ et
$N \otimes_R K = (R \setminus \{0\})^{-1}N$.
Pour tout $x \in R$ non nul, la multiplication par $x$ dans $N$ est injective, car
$N$ est plat sur $R$. Le lemme résulte donc du
Lemme \ref{lemma-localize-weakly-ass-nonzero-divisors}.
\end{proof}
```

</details>

### 20 — lemma-weakly-ass-change-fields

Anglais L16360–16444 ; français L16126–16210.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L16360) · FR-ALGEBRA-B32-CHOICE-0020.

La preuve entière conserve ses quatre réductions : sous-extension de type fini, extension finie après une base de transcendance, localisation en p, puis extension transcendante pure. Base de transcendance, théorème de descente, somme directe, module libre et lemme de Nakayama restent leurs objets exacts. Les écarts x_n au lieu de x_r et gf^nz∈J dans le texte anglais sont signalés séparément ; le français ne les améliore pas. La phrase sur un z arbitraire se comprend pour z non nul dans une preuve d'injectivité ; la réserve est explicitée sans ajouter une hypothèse à l'énoncé.

Point particulier à relire : Les variables r et n ont des rôles distincts. Dans le calcul d'injectivité, le choix z=0 ne donne pas de contradiction de Nakayama : la preuve doit traiter ce cas trivial à part. La conclusion mathématique n'est pas déclarée fausse. L'attestation externe de toutes les tournures de cette longue preuve n'est pas complète ; les décisions sont fondées sur le texte et les objets comparés.

Règles : FR-ALGEBRA-B32-RULE-ASSOCIATED, FR-ALGEBRA-B32-RULE-MODULE, FR-ALGEBRA-B32-RULE-LOCALIZATION, FR-ALGEBRA-B32-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-weakly-ass-change-fields}
Let $K/k$ be a field extension. Let $R$ be a $k$-algebra.
Let $M$ be an $R$-module. Let $\mathfrak q \subset R \otimes_k K$
be a prime lying over $\mathfrak p \subset R$. If
$\mathfrak q$ is weakly associated to $M \otimes_k K$,
then $\mathfrak p$ is weakly associated to $M$.
\end{lemma}

\begin{proof}
Let $z \in M \otimes_k K$ be an element such that $\mathfrak q$
is minimal over the annihilator $J \subset R \otimes_k K$ of $z$.
Choose a finitely generated subextension $K/L/k$ such that
$z \in M \otimes_k L$. Since $R \otimes_k L \to R \otimes_k K$
is flat we see that $J = I(R \otimes_k K)$ where $I \subset R \otimes_k L$
is the annihilator of $z$ in the smaller ring
(Lemma \ref{lemma-annihilator-flat-base-change}).
Thus $\mathfrak q \cap (R \otimes_k L)$ is minimal over $I$ by
going down (Lemma \ref{lemma-flat-going-down}).
In this way we reduce to the case described in the next paragraph.

\medskip\noindent
Assume $K/k$ is a finitely generated field extension.
Let $x_1, \ldots, x_r \in K$ be a transcendence basis
of $K$ over $k$, see Fields, Section \ref{fields-section-transcendence}.
Set $L = k(x_1, \ldots, x_r)$. Say $[K : L] = n$. Then
$R \otimes_k L \to R \otimes_k K$ is a finite ring map.
Hence $\mathfrak q \cap (R \otimes_k L)$
is a weakly associated prime of $M \otimes_k K$
viewed as a $R \otimes_k L$-module by
Lemma \ref{lemma-weakly-ass-finite-ring-map}.
Since $M \otimes_k K \cong (M \otimes_k L)^{\oplus n}$
as a $R \otimes_k L$-module, we see that
$\mathfrak q \cap (R \otimes_k L)$
is a weakly associated prime of $M \otimes_k L$
(for example by using Lemma \ref{lemma-weakly-ass} and induction).
In this way we reduce to the case discussed in the next paragraph.

\medskip\noindent
Assume $K = k(x_1, \ldots, x_r)$ is a purely transcendental field extension.
We may replace $R$ by $R_\mathfrak p$, $M$ by $M_\mathfrak p$
and $\mathfrak q$ by $\mathfrak q(R_\mathfrak p \otimes_k K)$.
See Lemma \ref{lemma-localize-weakly-ass}.
In this way we reduce to the case discussed in the next paragraph.

\medskip\noindent
Assume $K = k(x_1, \ldots, x_r)$ is a purely transcendental field extension
and $R$ is local with maximal ideal $\mathfrak p$. We claim that any
$f \in R \otimes_k K$, $f \not \in \mathfrak p(R \otimes_k K)$
is a nonzerodivisor on $M \otimes_k K$. Namely, let
$z \in M \otimes_k K$ be an element.
There is a finite $R$-submodule $M' \subset M$ such that
$z \in M' \otimes_k K$ and such that $M'$ is minimal with
this property: choose a basis $\{t_\alpha\}$ of $K$ as a
$k$-vector space, write $z = \sum m_\alpha \otimes t_\alpha$ and let
$M'$ be the $R$-submodule generated by the $m_\alpha$.
If $z \in \mathfrak p(M' \otimes_k K) = \mathfrak p M' \otimes_k K$,
then $\mathfrak pM' = M'$ and $M' = 0$ by Lemma \ref{lemma-NAK}
a contradiction.
Thus $z$ has nonzero image $\overline{z}$ in $M'/\mathfrak p M' \otimes_k K$
But $R/\mathfrak p \otimes_k K$ is a domain as a localization
of $\kappa(\mathfrak p)[x_1, \ldots, x_n]$ and
$M'/\mathfrak p M' \otimes_k K$ is a free module, hence
$f\overline{z} \not = 0$. This proves the claim.

\medskip\noindent
Finally, pick $z \in M \otimes_k K$ such that $\mathfrak q$
is minimal over the annihilator $J \subset R \otimes_k K$ of $z$.
For $f \in \mathfrak p$ there exists an $n \geq 1$ and a
$g \in R \otimes_k K$, $g \not \in \mathfrak q$ such that
$g f^n z \in J$, i.e., $g f^n z = 0$.
(This holds because $\mathfrak q$ lies over $\mathfrak p$
and $\mathfrak q$ is minimal over $J$.)
Above we have seen that $g$ is a nonzerodivisor hence $f^n z = 0$.
This means that $\mathfrak p$ is a weakly associated prime
of $M \otimes_k K$ viewed as an $R$-module.
Since $M \otimes_k K$ is a direct sum of copies of $M$
we conclude that $\mathfrak p$ is a weakly associated
prime of $M$ as before.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-weakly-ass-change-fields}
Soit $K/k$ une extension de corps. Soit $R$ une $k$-algèbre.
Soit $M$ un $R$-module. Soit $\mathfrak q \subset R \otimes_k K$
un idéal premier au-dessus de $\mathfrak p \subset R$. Si
$\mathfrak q$ est faiblement associé à $M \otimes_k K$,
alors $\mathfrak p$ est faiblement associé à $M$.
\end{lemma}

\begin{proof}
Soit $z \in M \otimes_k K$ un élément tel que $\mathfrak q$
soit minimal au-dessus de l'annulateur $J \subset R \otimes_k K$ de $z$.
Choisissons une sous-extension de type fini $K/L/k$ telle que
$z \in M \otimes_k L$. Comme $R \otimes_k L \to R \otimes_k K$
est plat, on a $J = I(R \otimes_k K)$, où $I \subset R \otimes_k L$
est l'annulateur de $z$ dans le plus petit anneau
(Lemme \ref{lemma-annihilator-flat-base-change}).
Ainsi, $\mathfrak q \cap (R \otimes_k L)$ est minimal au-dessus de $I$ par le
théorème de descente (Lemme \ref{lemma-flat-going-down}).
On se ramène ainsi au cas décrit dans le paragraphe suivant.

\medskip\noindent
Supposons que $K/k$ soit une extension de corps de type fini.
Soient $x_1, \ldots, x_r \in K$ une base de transcendance
de $K$ sur $k$ ; voir Corps, section \ref{fields-section-transcendence}.
Posons $L = k(x_1, \ldots, x_r)$. Écrivons $[K : L] = n$. Alors
$R \otimes_k L \to R \otimes_k K$ est un homomorphisme d'anneaux fini.
Le Lemme \ref{lemma-weakly-ass-finite-ring-map} montre donc que
$\mathfrak q \cap (R \otimes_k L)$
est un idéal premier faiblement associé à $M \otimes_k K$
considéré comme $R \otimes_k L$-module.
Comme $M \otimes_k K \cong (M \otimes_k L)^{\oplus n}$
en tant que $R \otimes_k L$-module, on voit que
$\mathfrak q \cap (R \otimes_k L)$
est un idéal premier faiblement associé à $M \otimes_k L$
(par exemple en utilisant le Lemme \ref{lemma-weakly-ass} et une récurrence).
On se ramène ainsi au cas examiné dans le paragraphe suivant.

\medskip\noindent
Supposons que $K = k(x_1, \ldots, x_r)$ soit une extension transcendante pure.
On peut remplacer $R$ par $R_\mathfrak p$, $M$ par $M_\mathfrak p$
et $\mathfrak q$ par $\mathfrak q(R_\mathfrak p \otimes_k K)$.
Voir le Lemme \ref{lemma-localize-weakly-ass}.
On se ramène ainsi au cas examiné dans le paragraphe suivant.

\medskip\noindent
Supposons que $K = k(x_1, \ldots, x_r)$ soit une extension transcendante pure
et que $R$ soit local d'idéal maximal $\mathfrak p$. Nous affirmons que tout
$f \in R \otimes_k K$, avec $f \not \in \mathfrak p(R \otimes_k K)$,
est un non-diviseur de zéro sur $M \otimes_k K$. En effet, soit
$z \in M \otimes_k K$ un élément.
Il existe un $R$-sous-module de type fini $M' \subset M$ tel que
$z \in M' \otimes_k K$ et tel que $M'$ soit minimal pour
cette propriété : choisissons une base $\{t_\alpha\}$ de $K$ comme
$k$-espace vectoriel, écrivons $z = \sum m_\alpha \otimes t_\alpha$ et prenons pour
$M'$ le $R$-sous-module engendré par les $m_\alpha$.
Si $z \in \mathfrak p(M' \otimes_k K) = \mathfrak p M' \otimes_k K$,
alors $\mathfrak pM' = M'$ et $M' = 0$ d'après le Lemme \ref{lemma-NAK},
ce qui est une contradiction.
Ainsi, $z$ a une image non nulle $\overline{z}$ dans $M'/\mathfrak p M' \otimes_k K$.
Or $R/\mathfrak p \otimes_k K$ est intègre, car c'est une localisation
de $\kappa(\mathfrak p)[x_1, \ldots, x_n]$, et
$M'/\mathfrak p M' \otimes_k K$ est un module libre ; par conséquent,
$f\overline{z} \not = 0$. Cela démontre l'affirmation.

\medskip\noindent
Enfin, choisissons $z \in M \otimes_k K$ tel que $\mathfrak q$
soit minimal au-dessus de l'annulateur $J \subset R \otimes_k K$ de $z$.
Pour $f \in \mathfrak p$, il existe $n \geq 1$ et
$g \in R \otimes_k K$, avec $g \not \in \mathfrak q$, tels que
$g f^n z \in J$, c'est-à-dire $g f^n z = 0$.
(Cela vient de ce que $\mathfrak q$ est au-dessus de $\mathfrak p$
et que $\mathfrak q$ est minimal au-dessus de $J$.)
On a vu plus haut que $g$ est un non-diviseur de zéro, donc $f^n z = 0$.
Ainsi, $\mathfrak p$ est un idéal premier faiblement associé
à $M \otimes_k K$ considéré comme $R$-module.
Comme $M \otimes_k K$ est une somme directe de copies de $M$,
on en déduit, comme précédemment, que $\mathfrak p$ est un idéal premier
faiblement associé à $M$.
\end{proof}
```

</details>

## Contrôles et suite

Les 420 régions mathématiques sont identiques sans exception. Le préfixe de 11 651 régions passe avec les quarante-deux exceptions linguistiques antérieures précisément recensées ; les différences sont vérifiées dans leur ordre et avec leurs multiplicités exactes.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items restent identiques. Aucune citation ou titre facultatif différent ne figure dans ce lot. Les opérations inverses retrouvent le lot précédent puis tous les octets du témoin public préservé. Préfixe déjà relu et suffixe encore non relu sont inchangés.

Les 595 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Idéaux premiers immergés, anglais L16445 / français L16211. Aucun PDF nouveau ni publication ; restauration globale en cours.

