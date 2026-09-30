# Assassin relatif

## Résultat et portée

La section entière est comparée : anglais L15616–15924 (309 lignes), français L15370–15690 (321 lignes), sept paires complètes. 143 occurrences de règles sont contextualisées, non un décompte de tous les mots. Couverture continue : 65 sections, 575 paires et 5642 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Le français est fidèle et reste inchangé. Aucun fichier LaTeX identique supplémentaire n’est créé. Les six ensembles, les hypothèses distinctes de platitude et de noethérianité, le calcul du produit tensoriel et les identifications par fibres sont comparés intégralement.

Les réserves sur deux notations anglaises restent hors traduction : N/p’ au lieu de N/p’N et Ass_S au lieu de Ass_{S_q}. Une coquille prove est également notée. L’absence d’attestation nouvelle du syntagme exact assassin relatif est déclarée, non masquée par une bibliographie.

Lecture produite par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. Le canon est consulté pour cette révision rétrospective, non présenté comme consulté lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX conservé](staged/fr/010_algebra.prose-batch29.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH30_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH31_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH31_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH31_OCCURRENCES.json) · [Opérations](ALGEBRA_PROSE_BATCH31_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH31_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH31_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH31_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH31_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH31_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Grothendieck et Dieudonné — Éléments de géométrie algébrique IV seconde partie

[Source consultée](https://www.numdam.org/item/PMIHES_1965__24__5_0/) · [Fichier conservé](canon-consulted/fr-algebra/ega-iv2-numdam.pdf)

Pages PDF40–43 / imprimées43–46 rendues et lues complètement. Section3.3 Relations avec la platitude, proposition3.3.1, corollaires3.3.2–3.3.3, proposition3.3.4 et proposition3.3.6 avec sa continuation. Tables PDF226–227 consultées pour localiser la section, pas comme preuve de terminologie.

Attestations courtes : « Relations avec la platitude », « fibre », « projection canonique ».

La proposition3.3.1 énonce le calcul de Ass d'un produit tensoriel par union des Ass des fibres sous platitude, et l'égalité sous noethérianité de la base. Le texte explique l'identification de la fibre à un sous-espace. Cela éclaire modules fibres, plat, union et identification des spectres ; les résultats3.3.6–3.3.9 attestent le même registre de projection et de fibres.

Limites : EGA parle de préschémas et de Modules quasi-cohérents ; Stacks traite ici d'anneaux et modules. Ni les hypothèses géométriques ni les assertions voisines ne sont ajoutées. Ces pages ne sont pas une attestation du syntagme exact assassin relatif. Les relations source gouvernent le contenu.

SHA-256 : C3E960AA1C5C37046E8892D8A3CAC098E2738164136B5CDAA5D5D893F89931DA.

### Christian Peskine — Introduction algébrique à la géométrie projective

[Source consultée](https://perso.univ-rennes1.fr/matthieu.romagny/M2_0708/bouquin.pdf) · [Fichier conservé](canon-consulted/fr-algebra/peskine-geometrie-projective-2007.pdf)

Pages PDF84,86,138,144 / imprimées83,85,137,143 relues complètement dans ce lot. Théorème10.1 et lemme10.4 ; proposition16.1 et définition16.3. Les accents décomposés de l'extraction ont été interprétés comme accents, non traités comme variantes lexicales.

Attestations courtes : « anneau intègre », « non diviseur de 0 dans M ».

Atteste anneau intègre, idéal premier associé, annulateur, corps des fractions et non-diviseur de zéro dans un module. La proposition16.1 donne le lien avec l'injectivité de la multiplication. La définition16.3 justifie que dans M n'est pas une préposition fautive.

Limites : Les conditions noethériennes et de type fini de ces propositions restent celles de Peskine. Elles ne sont pas importées dans les énoncés généraux de Stacks. Pas d'attestation externe nouvelle pour chaque connecteur de rédaction.

SHA-256 : C84D597457282B22B993F523791F4A3E391A74554FF76F7F49878640789435BA.

## Modifications et motifs

Aucune opération nouvelle. La fidélité est justifiée par la lecture complète : conserver une bonne traduction est le résultat de ce lot. Les réserves sur la notation anglaise ne deviennent pas une liberté éditoriale française.

## Observations séparées sur la source

Trois observations sont distinctes : accord du verbe prove, facteur N absent dans un quotient et sous-indice de l’anneau localisé. Le français conserve les deux formules officielles. Aucune admission, déduplication globale ou première découverte n’est revendiquée.

### lemma-compare-relative-assassins

[Anglais officiel L15675](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15675) · FR-ALGEBRA-B31-SOURCE-NOTE-0001.

```tex
Lemma \ref{lemma-localize-ass} part (1). This prove that $A = A'$.
```

Le sujet This exige proves, non prove. Le français Cela montre que est idiomatique et rend déjà le sens. Proposition grammaticale séparée : This proves that. Aucune opération dans la traduction.

Confiance forte sur la grammaire ; aucune admission ni déduplication globale.

### lemma-compare-relative-assassins

[Anglais officiel L15713](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15713) · FR-ALGEBRA-B31-SOURCE-NOTE-0002.

```tex
$N/\mathfrak p'$. Hence none of these elements can map to an element of
```

La phrase précédente définit N/p'N comme module plat sur R/p'. La phrase portant sur les non-diviseurs de zéro imprime N/p' sans le N final : p' est un idéal de R, pas le sous-module p'N de N. La phrase suivante retourne à N/p'N. Correction source proposée : N/p'N. La formule française reste N/p', selon le témoin officiel. Cette faute de notation ne provient pas du français.

Confiance forte sur le facteur omis, fondée sur les deux quotients voisins ; pas d'admission, de première découverte ou de déduplication globale.

### lemma-bourbaki

[Anglais officiel L15827](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15827) · FR-ALGEBRA-B31-SOURCE-NOTE-0003.

```tex
$\mathfrak qS_{\mathfrak q} \in \text{Ass}_S((M \otimes_R N)_{\mathfrak q})$.
```

Le membre qS_q est un idéal du localisé S_q, et l'hypothèse avait explicitement été énoncée plus haut avec Ass_{S_q}. Le dernier Ass_S est donc un sous-indice incompatible avec le premier considéré. Correction proposée : Ass_{S_q}. La contraction à S serait q, non qS_q. Le français conserve exactement Ass_S ; aucun changement mathématique de la source n'est importé.

Confiance forte, comparaison directe à l'hypothèse localisée du même paragraphe ; aucune admission ou découverte nouvelle revendiquée.

## Règles contextualisées

### FR-ALGEBRA-B31-RULE-ASSOCIATED

Ass, association et annulateur sont comparés à leur définition source. L'attestation externe du syntagme exact assassin relatif manque ; le maintien est explicitement motivé et réversible.

Canon : FR-ALGEBRA-B31-CANON-EGA, FR-ALGEBRA-B31-CANON-PESKINE.

### FR-ALGEBRA-B31-RULE-FIBRE

Corps résiduel et corps des fractions restent distincts ; les fibres et les spectres sont identifiés selon le morphisme source.

Canon : FR-ALGEBRA-B31-CANON-EGA, FR-ALGEBRA-B31-CANON-PESKINE.

### FR-ALGEBRA-B31-RULE-MODULE

Modules, sous-modules, colimites et sous-quotients conservent leurs objets. De type fini traduit la génération finie, pas la cardinalité du module.

Canon : FR-ALGEBRA-B31-CANON-EGA, FR-ALGEBRA-B31-CANON-PESKINE.

### FR-ALGEBRA-B31-RULE-FLAT

Plat ne devient pas fidèlement plat. R et S et leurs conditions noethériennes sont suivis séparément dans chaque clause.

Canon : FR-ALGEBRA-B31-CANON-EGA, FR-ALGEBRA-B31-CANON-PESKINE.

### FR-ALGEBRA-B31-RULE-LOGIC

Portée des conditions, sens des inclusions et égalités, et action injective sont comparés dans les passages complets, sans attribuer toute la syntaxe à un canon externe.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-relative-assassin

Anglais L15616–15641 ; français L15370–15395.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15616) · FR-ALGEBRA-B31-CHOICE-0001.

Les six ensembles A, A', A_fin, A'_fin, B et B_fin gardent exactement leurs conditions et leur ordre. La contraction R∩q est une notation de préimage, sans injectivité ajoutée. Il existe un module, il existe un premier et le premier imposé par contraction restent trois portées différentes. Le titre conserve le terme assassin du texte officiel ; le canon consulté explique le calcul par fibres, sans attestation nouvelle du syntagme complet assassin relatif.

Point particulier à relire : Ne pas remplacer R∩q par une intersection ensembliste exigeant R⊂S. Le syntagme complet assassin relatif n'a pas été retrouvé dans les pages du canon réellement consultées : maintien provisoire motivé par assassin pour Ass et relatif à S/R, non attestation inventée.

Règles : FR-ALGEBRA-B31-RULE-ASSOCIATED, FR-ALGEBRA-B31-RULE-FIBRE, FR-ALGEBRA-B31-RULE-MODULE, FR-ALGEBRA-B31-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Relative assassin}
\label{section-relative-assassin}

\noindent
Discussion of relative assassins. Let $R \to S$ be a ring map.
Let $N$ be an $S$-module. In this situation we can introduce the following
sets of primes $\mathfrak q$ of $S$:
\begin{enumerate}
\item $A$: with $\mathfrak p = R \cap \mathfrak q$ we have that
$\mathfrak q \in \text{Ass}_S(N \otimes_R \kappa(\mathfrak p))$,
\item $A'$: with $\mathfrak p = R \cap \mathfrak q$ we have that
$\mathfrak q$ is in the image of
$\text{Ass}_{S \otimes \kappa(\mathfrak p)}(N \otimes_R \kappa(\mathfrak p))$
under the canonical map
$\Spec(S \otimes_R \kappa(\mathfrak p)) \to \Spec(S)$,
\item $A_{fin}$: with $\mathfrak p = R \cap \mathfrak q$ we have that
$\mathfrak q \in \text{Ass}_S(N/\mathfrak pN)$,
\item $A'_{fin}$: for some prime $\mathfrak p' \subset R$ we have
$\mathfrak q \in \text{Ass}_S(N/\mathfrak p'N)$,
\item $B$: for some $R$-module $M$ we have
$\mathfrak q \in \text{Ass}_S(N \otimes_R M)$, and
\item $B_{fin}$: for some finite $R$-module $M$ we have
$\mathfrak q \in \text{Ass}_S(N \otimes_R M)$.
\end{enumerate}
Let us determine some of the relations between these sets.
```

Français restauré :
```tex
\section{Assassin relatif}
\label{section-relative-assassin}

\noindent
Discussion des assassins relatifs. Soit $R \to S$ un morphisme d'anneaux.
Soit $N$ un $S$-module. Dans cette situation, nous pouvons introduire les
ensembles suivants d'idéaux premiers $\mathfrak q$ de $S$ :
\begin{enumerate}
\item $A$ : en posant $\mathfrak p = R \cap \mathfrak q$, on a
$\mathfrak q \in \text{Ass}_S(N \otimes_R \kappa(\mathfrak p))$,
\item $A'$ : en posant $\mathfrak p = R \cap \mathfrak q$, l'idéal
$\mathfrak q$ appartient à l'image de
$\text{Ass}_{S \otimes \kappa(\mathfrak p)}(N \otimes_R \kappa(\mathfrak p))$
par le morphisme canonique
$\Spec(S \otimes_R \kappa(\mathfrak p)) \to \Spec(S)$,
\item $A_{fin}$ : en posant $\mathfrak p = R \cap \mathfrak q$, on a
$\mathfrak q \in \text{Ass}_S(N/\mathfrak pN)$,
\item $A'_{fin}$ : il existe un idéal premier $\mathfrak p' \subset R$ tel que
$\mathfrak q \in \text{Ass}_S(N/\mathfrak p'N)$,
\item $B$ : il existe un $R$-module $M$ tel que
$\mathfrak q \in \text{Ass}_S(N \otimes_R M)$, et
\item $B_{fin}$ : il existe un $R$-module de type fini $M$ tel que
$\mathfrak q \in \text{Ass}_S(N \otimes_R M)$.
\end{enumerate}
Déterminons quelques-unes des relations entre ces ensembles.
```

</details>

### 02 — lemma-compare-relative-assassins

Anglais L15642–15753 ; français L15396–15511.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15642) · FR-ALGEBRA-B31-CHOICE-0002.

Les cinq clauses, chacune avec ses hypothèses propres, et leurs cinq preuves sont lues intégralement. La noethérianité de S en (3) ne devient pas celle de R en (5) ; la platitude de N ne devient pas fidèlement plat. Colimite filtrante, annulateur, filtration et sous-quotient ont leurs objets exacts. Le mot finite est correctement rendu par de type fini pour les modules. La contraction p'=R∩q et le passage au corps résiduel conservent leurs arguments. Deux coquilles anglaises, prove et N/p' sans N final, sont signalées à part ; la seconde reste dans la formule française. L'introduction suivant la preuve conserve la réserve sur les anneaux fibres noethériens, non une hypothèse universelle ajoutée.

Point particulier à relire : N/p' devrait selon le contexte désigner N/p'N, mais la formule officielle est conservée. L'ellipse S⊗κ(p) sans base R dans l'introduction est une convention déterminée par le morphisme, pas une nouvelle erreur admise. Le lemme rappelle cinq noms et utilise aussi le sixième, déjà défini ; ne pas confondre ce rappel abrégé avec une disparition d'ensemble.

Règles : FR-ALGEBRA-B31-RULE-ASSOCIATED, FR-ALGEBRA-B31-RULE-FIBRE, FR-ALGEBRA-B31-RULE-MODULE, FR-ALGEBRA-B31-RULE-FLAT, FR-ALGEBRA-B31-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-compare-relative-assassins}
Let $R \to S$ be a ring map. Let $N$ be an $S$-module.
Let $A$, $A'$, $A_{fin}$, $B$, and $B_{fin}$ be the subsets of
$\Spec(S)$ introduced above.
\begin{enumerate}
\item We always have $A = A'$.
\item We always have $A_{fin} \subset A$,
$B_{fin} \subset B$, $A_{fin} \subset A'_{fin} \subset B_{fin}$
and $A \subset B$.
\item If $S$ is Noetherian, then $A = A_{fin}$ and $B = B_{fin}$.
\item If $N$ is flat over $R$, then $A = A_{fin} = A'_{fin}$ and $B = B_{fin}$.
\item If $R$ is Noetherian and $N$ is flat over $R$, then all of the sets
are equal, i.e., $A = A' = A_{fin} = A'_{fin} = B = B_{fin}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Some of the arguments in the proof will be repeated in the proofs of
later lemmas which are more precise than this one (because they deal
with a given module $M$ or a given prime $\mathfrak p$ and not with
the collection of all of them).

\medskip\noindent
Proof of (1). Let $\mathfrak p$ be a prime of $R$. Then we have
$$
\text{Ass}_S(N \otimes_R \kappa(\mathfrak p)) =
\text{Ass}_{S/\mathfrak pS}(N \otimes_R \kappa(\mathfrak p)) =
\text{Ass}_{S \otimes_R \kappa(\mathfrak p)}(N \otimes_R \kappa(\mathfrak p))
$$
the first equality by
Lemma \ref{lemma-ass-quotient-ring}
and the second by
Lemma \ref{lemma-localize-ass} part (1). This prove that $A = A'$.
The inclusion $A_{fin} \subset A'_{fin}$ is clear.

\medskip\noindent
Proof of (2). Each of the inclusions is immediate from the definitions
except perhaps $A_{fin} \subset A$ which follows from
Lemma \ref{lemma-localize-ass}
and the fact that we require $\mathfrak p = R \cap \mathfrak q$ in
the formulation of $A_{fin}$.

\medskip\noindent
Proof of (3). The equality $A = A_{fin}$ follows from
Lemma \ref{lemma-localize-ass} part (3)
if $S$ is Noetherian. Let $\mathfrak q = (g_1, \ldots, g_m)$ be a finitely
generated prime ideal of $S$.
Say $z \in N \otimes_R M$ is an element whose annihilator is $\mathfrak q$.
We may pick a finite submodule $M' \subset M$ such that $z$ is the
image of $z' \in N \otimes_R M'$. Then
$\text{Ann}_S(z') \subset \mathfrak q = \text{Ann}_S(z)$.
Since $N \otimes_R -$ commutes with colimits and since $M$ is the
directed colimit of finite $R$-modules we can find $M' \subset M'' \subset M$
such that the image $z'' \in N \otimes_R M''$ is annihilated by
$g_1, \ldots, g_m$. Hence $\text{Ann}_S(z'') = \mathfrak q$. This proves
that $B = B_{fin}$ if $S$ is Noetherian.

\medskip\noindent
Proof of (4). If $N$ is flat, then the functor $N \otimes_R -$ is exact.
In particular, if $M' \subset M$, then $N \otimes_R M' \subset N \otimes_R M$.
Hence if $z \in N \otimes_R M$ is an element whose annihilator
$\mathfrak q = \text{Ann}_S(z)$ is a prime, then we can pick any
finite $R$-submodule $M' \subset M$ such that $z \in N \otimes_R M'$
and we see that the annihilator of $z$ as an element of $N \otimes_R M'$
is equal to $\mathfrak q$. Hence $B = B_{fin}$. Let $\mathfrak p'$ be a
prime of $R$ and let $\mathfrak q$ be a prime of $S$ which is
an associated prime of $N/\mathfrak p'N$. This implies that
$\mathfrak p'S \subset \mathfrak q$. As $N$ is flat over $R$ we
see that $N/\mathfrak p'N$ is flat over the integral domain $R/\mathfrak p'$.
Hence every nonzero element of $R/\mathfrak p'$ is a nonzerodivisor on
$N/\mathfrak p'$. Hence none of these elements can map to an element of
$\mathfrak q$ and we conclude that $\mathfrak p' = R \cap \mathfrak q$.
Hence $A_{fin} = A'_{fin}$. Finally, by
Lemma \ref{lemma-localize-ass-nonzero-divisors}
we see that
$\text{Ass}_S(N/\mathfrak p'N) =
\text{Ass}_S(N \otimes_R \kappa(\mathfrak p'))$, i.e., $A'_{fin} = A$.

\medskip\noindent
Proof of (5). We only need to prove $A'_{fin} = B_{fin}$ as the other
equalities have been proved in (4). To see this let $M$ be a finite
$R$-module. By
Lemma \ref{lemma-filter-Noetherian-module}
there exists a filtration by $R$-submodules
$$
0 = M_0 \subset M_1 \subset \ldots \subset M_n = M
$$
such that each quotient $M_i/M_{i-1}$ is isomorphic
to $R/\mathfrak p_i$ for some prime ideal $\mathfrak p_i$
of $R$. Since $N$ is flat we obtain a filtration by $S$-submodules
$$
0 = N \otimes_R M_0 \subset N \otimes_R M_1 \subset \ldots \subset
N \otimes_R M_n = N \otimes_R M
$$
such that each subquotient is isomorphic to $N/\mathfrak p_iN$. By
Lemma \ref{lemma-ass}
we conclude that
$\text{Ass}_S(N \otimes_R M) \subset \bigcup \text{Ass}_S(N/\mathfrak p_iN)$.
Hence we see that $B_{fin} \subset A'_{fin}$. Since the other inclusion is part
of (2) we win.
\end{proof}

\noindent
We define the relative assassin of $N$ over $S/R$ to be the
set $A = A'$ above. As a motivation we point out that it depends
only on the fibre modules $N \otimes_R \kappa(\mathfrak p)$
over the fibre rings. As in the case of the assassin of a module we
warn the reader that this notion makes most sense when the fibre
rings $S \otimes_R \kappa(\mathfrak p)$ are Noetherian, for example
if $R \to S$ is of finite type.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-compare-relative-assassins}
Soit $R \to S$ un morphisme d'anneaux. Soit $N$ un $S$-module.
Soient $A$, $A'$, $A_{fin}$, $B$ et $B_{fin}$ les sous-ensembles de
$\Spec(S)$ introduits ci-dessus.
\begin{enumerate}
\item Nous avons toujours $A = A'$.
\item Nous avons toujours $A_{fin} \subset A$,
$B_{fin} \subset B$, $A_{fin} \subset A'_{fin} \subset B_{fin}$
et $A \subset B$.
\item Si $S$ est noethérien, alors $A = A_{fin}$ et $B = B_{fin}$.
\item Si $N$ est plat sur $R$, alors $A = A_{fin} = A'_{fin}$ et $B = B_{fin}$.
\item Si $R$ est noethérien et si $N$ est plat sur $R$, alors tous ces
ensembles sont égaux, c'est-à-dire
$A = A' = A_{fin} = A'_{fin} = B = B_{fin}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Certains arguments de la démonstration seront répétés dans les démonstrations
de lemmes ultérieurs, qui sont plus précis que celui-ci (car ils portent sur
un module $M$ donné ou sur un idéal premier $\mathfrak p$ donné, et non sur
l'ensemble de tous ces objets).

\medskip\noindent
Démonstration de (1). Soit $\mathfrak p$ un idéal premier de $R$. Nous avons
alors
$$
\text{Ass}_S(N \otimes_R \kappa(\mathfrak p)) =
\text{Ass}_{S/\mathfrak pS}(N \otimes_R \kappa(\mathfrak p)) =
\text{Ass}_{S \otimes_R \kappa(\mathfrak p)}(N \otimes_R \kappa(\mathfrak p))
$$
la première égalité d'après le
Lemme \ref{lemma-ass-quotient-ring}
et la seconde d'après le
Lemme \ref{lemma-localize-ass}, partie (1). Cela montre que $A = A'$.
L'inclusion $A_{fin} \subset A'_{fin}$ est claire.

\medskip\noindent
Démonstration de (2). Chacune des inclusions découle immédiatement des
définitions, à l'exception peut-être de $A_{fin} \subset A$, qui résulte du
Lemme \ref{lemma-localize-ass}
et du fait que nous imposons $\mathfrak p = R \cap \mathfrak q$ dans la
définition de $A_{fin}$.

\medskip\noindent
Démonstration de (3). L'égalité $A = A_{fin}$ découle du
Lemme \ref{lemma-localize-ass}, partie (3), si $S$ est noethérien.
Soit $\mathfrak q = (g_1, \ldots, g_m)$ un idéal premier de type fini de $S$.
Soit $z \in N \otimes_R M$ un élément dont l'annulateur est $\mathfrak q$.
Nous pouvons choisir un sous-module de type fini $M' \subset M$ tel que $z$
soit l'image d'un élément $z' \in N \otimes_R M'$. Alors
$\text{Ann}_S(z') \subset \mathfrak q = \text{Ann}_S(z)$.
Puisque $N \otimes_R -$ commute aux colimites et que $M$ est la colimite
filtrante de ses sous-$R$-modules de type fini, nous pouvons trouver
$M' \subset M'' \subset M$ tel que l'image
$z'' \in N \otimes_R M''$ soit annulée par $g_1, \ldots, g_m$. Ainsi,
$\text{Ann}_S(z'') = \mathfrak q$. Cela montre que $B = B_{fin}$ lorsque $S$
est noethérien.

\medskip\noindent
Démonstration de (4). Si $N$ est plat, le foncteur $N \otimes_R -$ est exact.
En particulier, si $M' \subset M$, alors
$N \otimes_R M' \subset N \otimes_R M$. Ainsi, si
$z \in N \otimes_R M$ est un élément dont l'annulateur
$\mathfrak q = \text{Ann}_S(z)$ est premier, nous pouvons choisir un
sous-$R$-module de type fini quelconque $M' \subset M$ tel que
$z \in N \otimes_R M'$ ; l'annulateur de $z$ comme élément de
$N \otimes_R M'$ est alors égal à $\mathfrak q$. Ainsi, $B = B_{fin}$.
Soit $\mathfrak p'$ un idéal premier de $R$, et soit $\mathfrak q$ un idéal
premier de $S$ associé à $N/\mathfrak p'N$. Cela implique que
$\mathfrak p'S \subset \mathfrak q$. Comme $N$ est plat sur $R$, le module
$N/\mathfrak p'N$ est plat sur l'anneau intègre $R/\mathfrak p'$.
Par conséquent, tout élément non nul de $R/\mathfrak p'$ est un
non-diviseur de zéro dans $N/\mathfrak p'$. L'image d'aucun de ces éléments
ne peut donc appartenir à $\mathfrak q$, et nous concluons que
$\mathfrak p' = R \cap \mathfrak q$. Ainsi, $A_{fin} = A'_{fin}$. Enfin, le
Lemme \ref{lemma-localize-ass-nonzero-divisors}
donne
$\text{Ass}_S(N/\mathfrak p'N) =
\text{Ass}_S(N \otimes_R \kappa(\mathfrak p'))$, c'est-à-dire
$A'_{fin} = A$.

\medskip\noindent
Démonstration de (5). Il suffit de prouver $A'_{fin} = B_{fin}$, puisque les
autres égalités ont été établies en (4). Pour cela, soit $M$ un $R$-module de
type fini. D'après le
Lemme \ref{lemma-filter-Noetherian-module},
il existe une filtration par des sous-$R$-modules
$$
0 = M_0 \subset M_1 \subset \ldots \subset M_n = M
$$
telle que chaque quotient $M_i/M_{i-1}$ soit isomorphe à
$R/\mathfrak p_i$ pour un certain idéal premier $\mathfrak p_i$ de $R$.
Puisque $N$ est plat, nous obtenons une filtration par des sous-$S$-modules
$$
0 = N \otimes_R M_0 \subset N \otimes_R M_1 \subset \ldots \subset
N \otimes_R M_n = N \otimes_R M
$$
dont chaque sous-quotient est isomorphe à $N/\mathfrak p_iN$. D'après le
Lemme \ref{lemma-ass},
nous en déduisons que
$\text{Ass}_S(N \otimes_R M) \subset \bigcup \text{Ass}_S(N/\mathfrak p_iN)$.
Ainsi, $B_{fin} \subset A'_{fin}$. L'inclusion réciproque faisant partie de
(2), l'égalité est démontrée.
\end{proof}

\noindent
Nous définissons l'assassin de $N$ relativement à $S/R$ comme
l'ensemble $A = A'$ ci-dessus. Pour motiver cette définition, remarquons
qu'il ne dépend que des modules fibres $N \otimes_R \kappa(\mathfrak p)$ sur
les anneaux fibres. Comme dans le cas de l'assassin d'un module, nous
avertissons le lecteur que cette notion est surtout pertinente lorsque les
anneaux fibres $S \otimes_R \kappa(\mathfrak p)$ sont noethériens, par exemple
lorsque $R \to S$ est de type fini.
```

</details>

### 03 — definition-relative-assassin

Anglais L15754–15772 ; français L15512–15530.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15754) · FR-ALGEBRA-B31-CHOICE-0003.

L'assassin relativement à S/R est le même ensemble défini à partir de la fibre au premier contracté. Le connecteur with devient avec dans le texte de la formule ; tous les symboles, indices et relations restent exacts. Les fibres ne sont pas remplacées par les seuls quotients N/pN. La phrase de transition ne crée pas de nouveau résultat.

Règles : FR-ALGEBRA-B31-RULE-ASSOCIATED, FR-ALGEBRA-B31-RULE-MODULE, FR-ALGEBRA-B31-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-relative-assassin}
Let $R \to S$ be a ring map. Let $N$ be an $S$-module.
The {\it relative assassin of $N$ over $S/R$} is the set
$$
\text{Ass}_{S/R}(N)
=
\{ \mathfrak q \subset S \mid
\mathfrak q \in \text{Ass}_S(N \otimes_R \kappa(\mathfrak p))
\text{ with }\mathfrak p = R \cap \mathfrak q\}.
$$
This is the set named $A$ in
Lemma \ref{lemma-compare-relative-assassins}.
\end{definition}

\noindent
The spirit of the next few results is that they are about the relative
assassin, even though this may not be apparent.
```

Français restauré :
```tex
\begin{definition}
\label{definition-relative-assassin}
Soit $R \to S$ un morphisme d'anneaux. Soit $N$ un $S$-module.
L'{\it assassin de $N$ relativement à $S/R$} est l'ensemble
$$
\text{Ass}_{S/R}(N)
=
\{ \mathfrak q \subset S \mid
\mathfrak q \in \text{Ass}_S(N \otimes_R \kappa(\mathfrak p))
\text{ avec }\mathfrak p = R \cap \mathfrak q\}.
$$
C'est l'ensemble noté $A$ dans le
Lemme \ref{lemma-compare-relative-assassins}.
\end{definition}

\noindent
L'esprit des quelques résultats suivants est qu'ils portent sur l'assassin
relatif, même si cela n'apparaît pas immédiatement.
```

</details>

### 04 — lemma-bourbaki

Anglais L15773–15852 ; français L15531–15609.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15773) · FR-ALGEBRA-B31-CHOICE-0004.

L'inclusion et l'égalité conditionnelle gardent leurs portées distinctes : l'égalité requiert R noethérien, l'inclusion seulement N plat. La preuve conserve l'injection R/p→M, le produit tensoriel, la réduction aux sous-modules de type fini, la localisation en q et la filtration. Le non-diviseur de zéro dans un module est un registre attesté par Peskine. La notation Ass_S appliquée à qS_q dans une phrase de contradiction est source-littérale ; sa réserve de typage est documentée séparément, non corrigée dans la traduction.

Point particulier à relire : La preuve emploie déjà Ass_{S_q} avant la phrase fautive Ass_S : distinguer cette incohérence de source d'une faute française. Ne pas transformer le français en preuve mathématique éditée.

Règles : FR-ALGEBRA-B31-RULE-ASSOCIATED, FR-ALGEBRA-B31-RULE-MODULE, FR-ALGEBRA-B31-RULE-FLAT, FR-ALGEBRA-B31-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-bourbaki}
Let $R \to S$ be a ring map.
Let $M$ be an $R$-module, and let $N$ be an $S$-module.
If $N$ is flat as $R$-module, then
$$
\text{Ass}_S(M \otimes_R N)
\supset
\bigcup\nolimits_{\mathfrak p \in \text{Ass}_R(M)} \text{Ass}_S(N/\mathfrak pN)
$$
and if $R$ is Noetherian then we have equality.
\end{lemma}

\begin{proof}
If $\mathfrak p \in \text{Ass}_R(M)$ then there exists an injection
$R/\mathfrak p \to M$. As $N$ is flat over $R$ we obtain an injection
$R/\mathfrak p \otimes_R N \to M \otimes_R N$. Since
$R/\mathfrak p \otimes_R N = N/\mathfrak pN$ we conclude that
$\text{Ass}_S(N/\mathfrak pN) \subset \text{Ass}_S(M \otimes_R N)$, see
Lemma \ref{lemma-ass}. Hence the right hand side is
contained in the left hand side.

\medskip\noindent
Write $M = \bigcup M_\lambda$ as the union of its finitely generated
$R$-submodules. Then also $N \otimes_R M = \bigcup N \otimes_R M_\lambda$
(as $N$ is $R$-flat). By definition of associated primes we see that
$\text{Ass}_S(N \otimes_R M) = \bigcup \text{Ass}_S(N \otimes_R M_\lambda)$
and $\text{Ass}_R(M) = \bigcup \text{Ass}(M_\lambda)$. Hence we may assume
$M$ is finitely generated.

\medskip\noindent
Let $\mathfrak q \in \text{Ass}_S(M \otimes_R N)$, and assume $R$ is
Noetherian and $M$
is a finite $R$-module. To finish the proof we have to show that
$\mathfrak q$ is an element of the right hand side. First we observe that
$\mathfrak qS_{\mathfrak q} \in
\text{Ass}_{S_{\mathfrak q}}((M \otimes_R N)_{\mathfrak q})$,
see Lemma \ref{lemma-associated-primes-localize}.
Let $\mathfrak p$ be the corresponding prime of $R$.
Note that
$$
(M \otimes_R N)_{\mathfrak q} = M \otimes_R N_{\mathfrak q}
= M_{\mathfrak p} \otimes_{R_{\mathfrak p}} N_{\mathfrak q}
$$
If
$\mathfrak pR_{\mathfrak p} \not \in
\text{Ass}_{R_{\mathfrak p}}(M_{\mathfrak p})$
then there exists an element $x \in \mathfrak pR_{\mathfrak p}$ which
is a nonzerodivisor in $M_{\mathfrak p}$ (see
Lemma \ref{lemma-ideal-nonzerodivisor}). Since
$N_{\mathfrak q}$ is flat over $R_{\mathfrak p}$ we see that
the image of $x$ in $\mathfrak qS_{\mathfrak q}$ is a nonzerodivisor on
$(M \otimes_R N)_{\mathfrak q}$. This is a contradiction
with the assumption that
$\mathfrak qS_{\mathfrak q} \in \text{Ass}_S((M \otimes_R N)_{\mathfrak q})$.
Hence we conclude that $\mathfrak p$ is one of the associated
primes of $M$.

\medskip\noindent
Continuing the argument we choose a filtration
$$
0 = M_0 \subset M_1 \subset \ldots \subset M_n = M
$$
such that each quotient $M_i/M_{i-1}$ is isomorphic
to $R/\mathfrak p_i$ for some prime ideal $\mathfrak p_i$
of $R$, see Lemma \ref{lemma-filter-Noetherian-module}.
(By Lemma \ref{lemma-ass-filter} we have $\mathfrak p_i = \mathfrak p$ for
at least one $i$.) This gives a filtration
$$
0 = M_0 \otimes_R N \subset M_1 \otimes_R N \subset \ldots
\subset M_n \otimes_R N = M \otimes_R N
$$
with subquotients isomorphic to $N/\mathfrak p_iN$. If
$\mathfrak p_i \not = \mathfrak p$ then $\mathfrak q$ cannot be
associated to the module $N/\mathfrak p_iN$ by the result of the
preceding paragraph (as $\text{Ass}_R(R/\mathfrak p_i) = \{\mathfrak p_i\}$).
Hence we conclude that $\mathfrak q$ is associated to
$N/\mathfrak pN$ as desired.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-bourbaki}
Soit $R \to S$ un morphisme d'anneaux.
Soit $M$ un $R$-module et soit $N$ un $S$-module.
Si $N$ est plat comme $R$-module, alors
$$
\text{Ass}_S(M \otimes_R N)
\supset
\bigcup\nolimits_{\mathfrak p \in \text{Ass}_R(M)} \text{Ass}_S(N/\mathfrak pN)
$$
et, si $R$ est noethérien, il y a égalité.
\end{lemma}

\begin{proof}
Si $\mathfrak p \in \text{Ass}_R(M)$, il existe une injection
$R/\mathfrak p \to M$. Comme $N$ est plat sur $R$, nous obtenons une
injection $R/\mathfrak p \otimes_R N \to M \otimes_R N$. Puisque
$R/\mathfrak p \otimes_R N = N/\mathfrak pN$, nous concluons que
$\text{Ass}_S(N/\mathfrak pN) \subset \text{Ass}_S(M \otimes_R N)$, voir le
Lemme \ref{lemma-ass}. Le membre de droite est donc contenu dans le membre de
gauche.

\medskip\noindent
Écrivons $M = \bigcup M_\lambda$ comme la réunion de ses sous-$R$-modules de
type fini. Alors $N \otimes_R M = \bigcup N \otimes_R M_\lambda$ également
(car $N$ est plat sur $R$). La définition des idéaux premiers associés donne
$\text{Ass}_S(N \otimes_R M) = \bigcup \text{Ass}_S(N \otimes_R M_\lambda)$
et $\text{Ass}_R(M) = \bigcup \text{Ass}(M_\lambda)$. Nous pouvons donc
supposer que $M$ est de type fini.

\medskip\noindent
Soit $\mathfrak q \in \text{Ass}_S(M \otimes_R N)$, et supposons que $R$ soit
noethérien et que $M$ soit un $R$-module de type fini. Pour achever la
démonstration, nous devons montrer que $\mathfrak q$ appartient au membre de
droite. Remarquons d'abord que
$\mathfrak qS_{\mathfrak q} \in
\text{Ass}_{S_{\mathfrak q}}((M \otimes_R N)_{\mathfrak q})$,
voir le Lemme \ref{lemma-associated-primes-localize}.
Soit $\mathfrak p$ l'idéal premier correspondant de $R$.
Remarquons que
$$
(M \otimes_R N)_{\mathfrak q} = M \otimes_R N_{\mathfrak q}
= M_{\mathfrak p} \otimes_{R_{\mathfrak p}} N_{\mathfrak q}
$$
Si
$\mathfrak pR_{\mathfrak p} \not \in
\text{Ass}_{R_{\mathfrak p}}(M_{\mathfrak p})$,
il existe un élément $x \in \mathfrak pR_{\mathfrak p}$ qui est un
non-diviseur de zéro dans $M_{\mathfrak p}$ (voir le
Lemme \ref{lemma-ideal-nonzerodivisor}). Comme
$N_{\mathfrak q}$ est plat sur $R_{\mathfrak p}$, l'image de $x$ dans
$\mathfrak qS_{\mathfrak q}$ est un non-diviseur de zéro dans
$(M \otimes_R N)_{\mathfrak q}$. Cela contredit l'hypothèse
$\mathfrak qS_{\mathfrak q} \in \text{Ass}_S((M \otimes_R N)_{\mathfrak q})$.
Nous concluons donc que $\mathfrak p$ est l'un des idéaux premiers associés à
$M$.

\medskip\noindent
Poursuivant l'argument, choisissons une filtration
$$
0 = M_0 \subset M_1 \subset \ldots \subset M_n = M
$$
telle que chaque quotient $M_i/M_{i-1}$ soit isomorphe à
$R/\mathfrak p_i$ pour un certain idéal premier $\mathfrak p_i$ de $R$, voir
le Lemme \ref{lemma-filter-Noetherian-module}.
(D'après le Lemme \ref{lemma-ass-filter}, nous avons
$\mathfrak p_i = \mathfrak p$ pour au moins un $i$.) Nous obtenons une
filtration
$$
0 = M_0 \otimes_R N \subset M_1 \otimes_R N \subset \ldots
\subset M_n \otimes_R N = M \otimes_R N
$$
dont les sous-quotients sont isomorphes à $N/\mathfrak p_iN$. Si
$\mathfrak p_i \not = \mathfrak p$, alors $\mathfrak q$ ne peut être associé
au module $N/\mathfrak p_iN$, d'après le résultat du paragraphe précédent
(car $\text{Ass}_R(R/\mathfrak p_i) = \{\mathfrak p_i\}$). Nous concluons
donc que $\mathfrak q$ est associé à $N/\mathfrak pN$, comme voulu.
\end{proof}
```

</details>

### 05 — lemma-post-bourbaki

Anglais L15853–15878 ; français L15610–15634.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15853) · FR-ALGEBRA-B31-CHOICE-0005.

Anneau intègre et corps des fractions rendent domain et fraction field. Le module N est plat, non supposé fidèle, et les trois ensembles associés sont identifiés par le même spectre de localisation. Toute multiplication par un élément non nul est injective ; le français ne la dit pas inversible. Les deux renvois restent identiques.

Point particulier à relire : R est non nul et sans diviseurs de zéro au sens source ; N peut être nul. La platitude n'est pas la fidèle platitude.

Règles : FR-ALGEBRA-B31-RULE-FIBRE, FR-ALGEBRA-B31-RULE-MODULE, FR-ALGEBRA-B31-RULE-FLAT, FR-ALGEBRA-B31-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-post-bourbaki}
Let $R \to S$ be a ring map.
Let $N$ be an $S$-module.
Assume $N$ is flat as an $R$-module and
$R$ is a domain with fraction field $K$.
Then
$$
\text{Ass}_S(N) =
\text{Ass}_S(N \otimes_R K) =
\text{Ass}_{S \otimes_R K}(N \otimes_R K)
$$
via the canonical inclusion
$\Spec(S \otimes_R K) \subset \Spec(S)$.
\end{lemma}

\begin{proof}
Note that $S \otimes_R K = (R \setminus \{0\})^{-1}S$ and
$N \otimes_R K = (R \setminus \{0\})^{-1}N$.
For any nonzero $x \in R$ multiplication by $x$ on $N$ is injective as
$N$ is flat over $R$. Hence the lemma follows from
Lemma \ref{lemma-localize-ass-nonzero-divisors}
combined with
Lemma \ref{lemma-localize-ass} part (1).
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-post-bourbaki}
Soit $R \to S$ un morphisme d'anneaux.
Soit $N$ un $S$-module.
Supposons que $N$ soit plat comme $R$-module et que $R$ soit un anneau
intègre de corps des fractions $K$. Alors
$$
\text{Ass}_S(N) =
\text{Ass}_S(N \otimes_R K) =
\text{Ass}_{S \otimes_R K}(N \otimes_R K)
$$
par l'inclusion canonique
$\Spec(S \otimes_R K) \subset \Spec(S)$.
\end{lemma}

\begin{proof}
Remarquons que $S \otimes_R K = (R \setminus \{0\})^{-1}S$ et
$N \otimes_R K = (R \setminus \{0\})^{-1}N$.
Pour tout élément non nul $x \in R$, la multiplication par $x$ dans $N$ est
injective, puisque $N$ est plat sur $R$. Le lemme résulte donc du
Lemme \ref{lemma-localize-ass-nonzero-divisors}
combiné avec le
Lemme \ref{lemma-localize-ass}, partie (1).
\end{proof}
```

</details>

### 06 — lemma-bourbaki-fibres

Anglais L15879–15904 ; français L15635–15660.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15879) · FR-ALGEBRA-B31-CHOICE-0006.

L'union indexée par les premiers associés de M est calculée sur les modules fibres et les anneaux fibres. L'identification de leurs spectres avec des sous-ensembles de Spec(S) et la condition R noethérien de l'égalité restent explicites. EGA IV, proposition3.3.1, fournit une formulation française géométrique analogue de ce calcul ; elle n'est pas importée comme une autre assertion ni une hypothèse supplémentaire.

Règles : FR-ALGEBRA-B31-RULE-FIBRE, FR-ALGEBRA-B31-RULE-MODULE, FR-ALGEBRA-B31-RULE-FLAT, FR-ALGEBRA-B31-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-bourbaki-fibres}
Let $R \to S$ be a ring map.
Let $M$ be an $R$-module, and let $N$ be an $S$-module.
Assume $N$ is flat as $R$-module. Then
$$
\text{Ass}_S(M \otimes_R N)
\supset
\bigcup\nolimits_{\mathfrak p \in \text{Ass}_R(M)}
\text{Ass}_{S \otimes_R \kappa(\mathfrak p)}(N \otimes_R \kappa(\mathfrak p))
$$
where we use
Remark \ref{remark-fundamental-diagram}
to think of the spectra of fibre rings as subsets of $\Spec(S)$.
If $R$ is Noetherian then this inclusion is an equality.
\end{lemma}

\begin{proof}
This is equivalent to
Lemma \ref{lemma-bourbaki}
by
Lemmas \ref{lemma-ass-quotient-ring},
\ref{lemma-flat-base-change}, and
\ref{lemma-post-bourbaki}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-bourbaki-fibres}
Soit $R \to S$ un morphisme d'anneaux.
Soit $M$ un $R$-module et soit $N$ un $S$-module.
Supposons que $N$ soit plat comme $R$-module. Alors
$$
\text{Ass}_S(M \otimes_R N)
\supset
\bigcup\nolimits_{\mathfrak p \in \text{Ass}_R(M)}
\text{Ass}_{S \otimes_R \kappa(\mathfrak p)}(N \otimes_R \kappa(\mathfrak p))
$$
où nous utilisons la
Remarque \ref{remark-fundamental-diagram}
pour considérer les spectres des anneaux fibres comme des sous-ensembles de
$\Spec(S)$. Si $R$ est noethérien, cette inclusion est une égalité.
\end{lemma}

\begin{proof}
Ceci équivaut au
Lemme \ref{lemma-bourbaki}
d'après les
Lemmes \ref{lemma-ass-quotient-ring},
\ref{lemma-flat-base-change} et
\ref{lemma-post-bourbaki}.
\end{proof}
```

</details>

### 07 — remark-bourbaki

Anglais L15905–15924 ; français L15661–15690.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L15905) · FR-ALGEBRA-B31-CHOICE-0007.

Les trois assassins sont identifiés par passage à l'anneau quotient puis localisation, selon les mêmes deux références. L'égalité des ensembles s'entend via les applications canoniques entre spectres, non comme une identification arbitraire des anneaux. La phrase française complète La première égalité résulte du traduit correctement le fragment anglais sans ajout mathématique.

Règles : FR-ALGEBRA-B31-RULE-MODULE, FR-ALGEBRA-B31-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{remark}
\label{remark-bourbaki}
Let $R \to S$ be a ring map. Let $N$ be an $S$-module.
Let $\mathfrak p$ be a prime of $R$. Then
$$
\text{Ass}_S(N \otimes_R \kappa(\mathfrak p)) =
\text{Ass}_{S/\mathfrak pS}(N \otimes_R \kappa(\mathfrak p)) =
\text{Ass}_{S \otimes_R \kappa(\mathfrak p)}(N \otimes_R \kappa(\mathfrak p)).
$$
The first equality by
Lemma \ref{lemma-ass-quotient-ring}
and the second by
Lemma \ref{lemma-localize-ass} part (1).
\end{remark}
```

Français restauré :
```tex
\begin{remark}
\label{remark-bourbaki}
Soit $R \to S$ un morphisme d'anneaux. Soit $N$ un $S$-module.
Soit $\mathfrak p$ un idéal premier de $R$. Alors
$$
\text{Ass}_S(N \otimes_R \kappa(\mathfrak p)) =
\text{Ass}_{S/\mathfrak pS}(N \otimes_R \kappa(\mathfrak p)) =
\text{Ass}_{S \otimes_R \kappa(\mathfrak p)}(N \otimes_R \kappa(\mathfrak p)).
$$
La première égalité résulte du
Lemme \ref{lemma-ass-quotient-ring}
et la seconde du
Lemme \ref{lemma-localize-ass}, partie (1).
\end{remark}
```

</details>

## Contrôles et suite

Les 230 régions mathématiques concordent avec une seule traduction préexistante du connecteur with en avec, à l’indice137. Le préfixe de 11 231 régions passe avec quarante-deux exceptions linguistiques précisément recensées ; les différences sont vérifiées dans leur ordre et avec leurs multiplicités exactes.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items restent identiques. Aucune citation ou titre facultatif différent ne figure dans ce lot. Les opérations inverses retrouvent le lot précédent puis tous les octets du témoin public préservé. Préfixe déjà relu et suffixe encore non relu sont inchangés.

Les 575 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Idéaux premiers faiblement associés, anglais L15925 / français L15691. Aucun PDF nouveau ni publication ; restauration globale en cours.

