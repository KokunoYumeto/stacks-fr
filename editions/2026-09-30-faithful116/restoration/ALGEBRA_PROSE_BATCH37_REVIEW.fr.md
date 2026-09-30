# Groupes Ext

## Résultat et portée

Comparaison complète : anglais L17402–17758 /français L17168–17524, 357 lignes chacun, dix paires et 224 occurrences contextualisées. Couverture continue : 71 sections, 644 paires et 6502 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Une notice d’omission est normalisée : Omis devient Démonstration omise. Aucun argument, résultat, symbole, hypothèse ni formule ne change. Le français fidèle des autres passages est conservé après comparaison intégrale.

Sept observations anglaises restent séparées : un indice de différentielle, la contravariance Hom à trois lieux liés, H_i au lieu de H^i et quatre défauts d’orthographe ou de grammaire. Pas de correction mathématique cachée dans la traduction.

Lecture produite par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. Le canon est consulté rétrospectivement, non présenté comme consulté lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch37.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH36_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH37_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH37_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH37_OCCURRENCES.json) · [Opérations](ALGEBRA_PROSE_BATCH37_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH37_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH37_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH37_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH37_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH37_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Yves Laszlo — Introduction à l'algèbre commutative et homologique, maîtrise2003–2004

[Source consultée](https://www.cmls.polytechnique.fr/perso/laszlo/maitrise/maitrisefin.pdf) · [Fichier conservé](canon-consulted/fr-algebra/laszlo-commutative-homologique-2003.pdf)

Pages PDF/imprimées1,16,64–73 et77–79 entièrement lues. Exemple16.2 ; partieVII, définitions et suite exacte ; VIII.1, VIII.3.1, définition3.2, proposition3.3, corollaires3.4–3.5 et exercice5.1 ; X.1–2, calcul des Ext p79. PDF70 et72 rendus et inspectés visuellement.

Attestations courtes : « résolution libre », « morphisme de complexes », « homotopie », « suite exacte courte », « foncteur contravariant ».

Atteste le vocabulaire du complexe, de la résolution et de l'homotopie ; expose les relèvements et les suites exactes de cohomologie. L'exemple16.2 définit Hom(-,c) par précomposition ; X.2 présente le calcul de Ext via résolutions.

Limites : Consultation rétrospective. Les indices cohomologiques négatifs ne remplacent pas ceux de Stacks. Les erreurs de variables H(L)/H(P) p70, et les formules incohérentes de dérivation/ordre de suite p78–79, ne sont pas adoptées. La terminologie est attestée, mais chaque formule est vérifiée contre ses domaines. Aucune relecture humaine.

SHA-256 : 6CE611DFE7265C9658269EEE371803873B6ECEA26FEAC86E3455075F8D0A6D79.

### Christian Peskine — Introduction algébrique à la géométrie projective

[Source consultée](https://perso.univ-rennes1.fr/matthieu.romagny/M2_0708/bouquin.pdf) · [Fichier conservé](canon-consulted/fr-algebra/peskine-geometrie-projective-2007.pdf)

Pages PDF138–143 /imprimées137–142 entièrement relues. Section16.1 ; notamment définition16.7, lemme16.17, corollaire16.18 et démonstration16.19.

Attestations courtes : « profondeur », « modules libres de type fini », « diagramme du serpent ».

Appui au registre de profondeur, de type fini et des arguments sur Hom près du but de la section. La présentation dans16.19 confirme le sens de libre de type fini.

Limites : Ces pages ne définissent pas Ext et ne sont pas citées comme preuve de sa variance. Leur contexte local/noethérien ne restreint pas la définition générale des résolutions de Stacks. Consultation rétrospective ; pas de relecture humaine.

SHA-256 : C84D597457282B22B993F523791F4A3E391A74554FF76F7F49878640789435BA.

## Modifications et motifs

Une normalisation de notice, réversible et sans changement de formule. L’ellipse ancienne peut évoquer un argument omis ; la formulation retenue explicite Démonstration et son accord. Les anomalies anglaises restent visibles dans le français diplomatique et motivées séparément.

### FR-ALGEBRA-B37-REPAIR-0001

Anglais L17496 ; français L17262.

Avant :
```tex
Omis.
```

Après :
```tex
Démonstration omise.
```

Le quantificateur porte sur deux morphismes homotopes quelconques et leur action en (co)homologie. Laszlo VIII.3.2 explique la même propriété, mais sa preuve n'est pas importée. Omis est remplacé par Démonstration omise : le substantif explicite l'objet de l'omission et donne l'accord féminin. Aucun argument absent n'est ajouté ; c'est une normalisation de notice, pas une correction de théorème.

Omis peut être compris comme une ellipse d'argument omis. La formulation explicite choisie correspond à Démonstration dans l'édition et évite cet accord implicite. Pas d'attestation externe revendiquée pour cette simple notice française.

## Observations séparées sur la source

Les sept observations distinguent types et variance, notation et syntaxe. La direction de Hom est examinée dans l’énoncé, dans la preuve et dans la composition, avec les extraits liés. Aucun registre n’est admis, aucune déduplication globale ni première découverte revendiquée.

### definition-finite-free-resolution

[Anglais officiel L17466](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17466) · FR-ALGEBRA-B37-SOURCE-NOTE-0001.

```tex
$\alpha_{i-1} \circ d_{F, i} = d_{G, i-1} \circ \alpha_i$.
```

alpha_i a pour but G_i, tandis que d_{G,i-1} a pour source G_{i-1}. Le membre droit ne compose donc pas avec les types définis. d_{G,i} donne bien F_i→G_{i-1}, comme le membre gauche. Correction minimale proposée : remplacer l'indice i-1 par i sur cette différentielle seulement. La formule reste littérale dans le français.

Confiance forte par les domaines et buts explicites ; aucune admission ni mutation source.

### lemma-ext-welldefined

[Anglais officiel L17586](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17586) · FR-ALGEBRA-B37-SOURCE-NOTE-0002.

```tex
H^i(\alpha) :
H^i(\Hom_R(F_{\bullet}, N))
\longrightarrow
H^i(\Hom_R(G_{\bullet}, N))
```

Pour alpha:F→G, précomposer u:G_i→N par alpha_i donne u∘alpha_i:F_i→N. L'application des complexes Hom va donc de Hom(G,N) à Hom(F,N), non dans le sens affiché. En degré0, cela est déjà Hom(M2,N)→Hom(M1,N). Le même renversement fautif est répété dans la preuve L17601–17602. Avec beta:G→F, on a (alpha∘beta)*=beta*∘alpha* comme endomorphisme de Hom(G,N), alors que L17614–17617 écrit alpha*∘beta*= (alpha∘beta)*. Corriger ensemble les deux directions et l'ordre de la composition rend la preuve d'inversibilité correctement typée. Les trois extraits liés sont conservés dans ce dossier ; aucune de ces corrections n'entre dans la traduction diplomatique.

Confiance forte par la précomposition explicite, déjà en degré0 ; constat lié, sans déduplication globale ni première découverte.

[Pièce primaire algebra.tex L17601–17602](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17601)
SHA-256 du fichier : FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.

```tex
maps $\Hom_R(F_\bullet, N) \to
\Hom_R(G_\bullet, N)$ are homotopic.
```

[Pièce primaire algebra.tex L17614–17617](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17614)
SHA-256 du fichier : FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.

```tex
$H^i(\alpha) \circ H^i(\beta) =
H^i(\alpha \circ \beta)$. By the above the
map $H^i(\alpha \circ \beta)$ is the {\it same}
as the map $H^i(\text{id}_{G_{\bullet}}) = \text{id}$.
```

### lemma-ext-welldefined

[Anglais officiel L17594](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17594) · FR-ALGEBRA-B37-SOURCE-NOTE-0003.

```tex
$\varphi$ is the identity, so are all the maps $H_i(\alpha)$.
```

L'application visée a été définie comme H^i(alpha) sur le complexe cohomologique Hom. H_i(alpha) avait été défini plus haut sur l'homologie du complexe F→G, objet distinct. Le cas identité concerne les mêmes applications Ext, donc l'exposant H^i doit remplacer H_i ici. La typo reste source-littérale en français.

Confiance forte sur la notation contextuelle ; pas de correction source admise.

### lemma-compare-resolutions

[Anglais officiel L17562](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17562) · FR-ALGEBRA-B37-SOURCE-NOTE-0004.

```tex
it would perhaps be more appropriate to say ``an'' in stead
```

Le mot instead s'écrit en un seul mot. La note française un plutôt que le garde correctement sa prudence avant la preuve d'indépendance ; aucune portée mathématique ne change.

Confiance forte sur l'orthographe, observation séparée.

### lemma-ext-welldefined

[Anglais officiel L17610](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17610) · FR-ALGEBRA-B37-SOURCE-NOTE-0005.

```tex
be a map inducing $\psi :
```

La construction Choose beta be a map exige to be, ou simplement une apposition. Le français choisissons beta qui induit psi traduit déjà l'opération correctement sans imiter la faute anglaise.

Confiance forte sur la syntaxe ; aucun changement de relèvement.

### lemma-long-exact-seq-ext

[Anglais officiel L17646](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17646) · FR-ALGEBRA-B37-SOURCE-NOTE-0006.

```tex
Since each of the $F_i$ are free
```

Each est le sujet singulier : écrire is free. Le français chacun des F_i est libre est déjà accordé et conserve l'exactitude terme par terme.

Confiance forte sur l'accord, sans portée mathématique.

### lemma-reverse-long-exact-seq-ext

[Anglais officiel L17698](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17698) · FR-ALGEBRA-B37-SOURCE-NOTE-0007.

```tex
$0 \to K' \to K \to K'' \to 0$ is short exact sequence of $R$-modules.
```

La phrase exige is a short exact sequence. Le français est une suite exacte courte est idiomatique et complet ; le scindage n'est pas ajouté à la suite des noyaux.

Confiance forte sur l'article ; observation séparée, pas d'admission source.

## Règles contextualisées

### FR-ALGEBRA-B37-RULE-RESOLUTION

Chaque résolution et complexe est vérifié avec ses propres conditions : libre, exact ou de type fini ne s'ajoutent pas par substitution lexicale.

Canon : FR-ALGEBRA-B37-CANON-LASZLO, FR-ALGEBRA-B37-CANON-PESKINE.

### FR-ALGEBRA-B37-RULE-HOMOLOGY

L'homologie en indices et la cohomologie en exposants sont distinguées. Les anomalies de notation de la source restent explicitement documentées, non dissimulées.

Canon : FR-ALGEBRA-B37-CANON-LASZLO.

### FR-ALGEBRA-B37-RULE-MAP

Domaines, buts, sens de variance et compositions sont contrôlés dans les passages complets ; l'attestation terminologique ne certifie pas une formule source ill-typée.

Canon : FR-ALGEBRA-B37-CANON-LASZLO.

### FR-ALGEBRA-B37-RULE-EXACT

Exactitude degré par degré, suites longues et courtes, scindage construit et renversement par Hom sont distingués sans renforcer les hypothèses.

Canon : FR-ALGEBRA-B37-CANON-LASZLO, FR-ALGEBRA-B37-CANON-PESKINE.

### FR-ALGEBRA-B37-RULE-DEPTH

La finalité locale/noethérienne ne restreint pas les lemmes sur un anneau arbitraire. Les deux hypothèses de finitude de Ext sont conservées.

Canon : FR-ALGEBRA-B37-CANON-PESKINE, FR-ALGEBRA-B37-CANON-LASZLO.

### FR-ALGEBRA-B37-RULE-LOGIC

Chaque condition, alternative et quantificateur est contrôlé dans son contexte complet, avec les deux arguments distincts de Ext.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B37-RULE-OMISSION

Notice d'omission explicitée et accordée au substantif Démonstration ; aucune preuve ajoutée et aucune attestation externe inventée.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-ext

Anglais L17402–17409 ; français L17168–17175.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17402) · FR-ALGEBRA-B37-CHOICE-0001.

Algèbre homologique, groupes Ext et profondeur sont confrontés à leur contexte : quelques outils pour les anneaux locaux noethériens, non un nouveau traité ajouté à la traduction. Le titre conserve Ext sans expansion inventée.

Règles : FR-ALGEBRA-B37-RULE-HOMOLOGY, FR-ALGEBRA-B37-RULE-DEPTH.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Ext groups}
\label{section-ext}

\noindent
In this section we do a tiny bit of homological algebra,
in order to establish some fundamental properties of
depth over Noetherian local rings.
```

Français restauré :
```tex
\section{Groupes Ext}
\label{section-ext}

\noindent
Dans cette section, nous faisons un peu d'algèbre homologique
afin d'établir quelques propriétés fondamentales de la
profondeur sur les anneaux locaux noethériens.
```

</details>

### 02 — lemma-resolution-by-finite-free

Anglais L17410–17436 ; français L17176–17202.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17410) · FR-ALGEBRA-B37-CHOICE-0002.

Les deux conclusions sont distinctes : résolution libre pour tout module, puis termes libres de type fini sous les deux hypothèses R noethérien et M de type fini. Libre de type fini ne signifie ni module fini comme ensemble ni résolution de longueur finie. Toute la construction successive des surjections est comparée ; Laszlo VIII.1 atteste résolution libre, Peskine16 atteste le registre de type fini.

Point particulier à relire : Le rang est fini dans chaque degré ; la longueur de la résolution peut être infinie. La preuve source n'explicite que le cas noethérien, ce que le français conserve.

Règles : FR-ALGEBRA-B37-RULE-RESOLUTION, FR-ALGEBRA-B37-RULE-EXACT, FR-ALGEBRA-B37-RULE-DEPTH, FR-ALGEBRA-B37-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-resolution-by-finite-free}
Let $R$ be a ring. Let $M$ be an $R$-module.
\begin{enumerate}
\item There exists an exact complex
$$
\ldots \to F_2 \to F_1 \to F_0 \to M \to 0.
$$
with $F_i$ free $R$-modules.
\item If $R$ is Noetherian and $M$ finite over $R$, then we
can choose the complex such that $F_i$ is finite free.
In other words, we can find an exact complex
$$
\ldots \to R^{\oplus n_2} \to R^{\oplus n_1} \to R^{\oplus n_0} \to M \to 0.
$$
\end{enumerate}
\end{lemma}

\begin{proof}
Let us explain only the Noetherian case.
As a first step choose a surjection $R^{n_0} \to M$.
Then having constructed an exact complex of length
$e$ we simply choose a surjection $R^{n_{e + 1}} \to
\Ker(R^{n_e} \to R^{n_{e-1}})$ which is possible
because $R$ is Noetherian.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-resolution-by-finite-free}
Soit $R$ un anneau. Soit $M$ un $R$-module.
\begin{enumerate}
\item Il existe un complexe exact
$$
\ldots \to F_2 \to F_1 \to F_0 \to M \to 0.
$$
où les $F_i$ sont des $R$-modules libres.
\item Si $R$ est noethérien et si $M$ est de type fini sur $R$, on
peut choisir le complexe de sorte que les $F_i$ soient libres de type fini.
Autrement dit, on peut trouver un complexe exact
$$
\ldots \to R^{\oplus n_2} \to R^{\oplus n_1} \to R^{\oplus n_0} \to M \to 0.
$$
\end{enumerate}
\end{lemma}

\begin{proof}
Expliquons seulement le cas noethérien.
On choisit d'abord une surjection $R^{n_0} \to M$.
Puis, après avoir construit un complexe exact de longueur
$e$, il suffit de choisir une surjection $R^{n_{e + 1}} \to
\Ker(R^{n_e} \to R^{n_{e-1}})$, ce qui est possible
puisque $R$ est noethérien.
\end{proof}
```

</details>

### 03 — definition-finite-free-resolution

Anglais L17437–17488 ; français L17203–17254.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17437) · FR-ALGEBRA-B37-CHOICE-0003.

Les trois clauses de définition et les paragraphes suivants sont entièrement comparés. Résolution à gauche, morphisme de complexes, homologie, cohomologie et homotopie gardent leurs domaines et conventions d'indices. Laszlo VII et VIII.3.1 attestent ce registre mais utilisent des degrés cohomologiques, non les indices homologiques de Stacks. Le d_{G,i-1} ill-typé dans l'anglais reste identique en français et est signalé séparément.

Point particulier à relire : L'indice anglais d_{G,i-1} ne peut composer avec alpha_i : F_i→G_i. La formule française n'est pas un défaut nouveau de traduction. L'indexation cohomologique du canon consulté n'est pas imposée à Stacks.

Règles : FR-ALGEBRA-B37-RULE-RESOLUTION, FR-ALGEBRA-B37-RULE-HOMOLOGY, FR-ALGEBRA-B37-RULE-MAP, FR-ALGEBRA-B37-RULE-EXACT, FR-ALGEBRA-B37-RULE-DEPTH, FR-ALGEBRA-B37-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-finite-free-resolution}
Let $R$ be a ring. Let $M$ be an $R$-module.
\begin{enumerate}
\item A (left) {\it resolution} $F_\bullet \to M$ of $M$ is an exact complex
$$
\ldots \to F_2 \to F_1 \to F_0 \to M \to 0
$$
of $R$-modules.
\item A {\it resolution of $M$ by free $R$-modules} is a resolution
$F_\bullet \to M$ where each $F_i$ is a free $R$-module.
\item A {\it resolution of $M$ by finite free $R$-modules} is a resolution
$F_\bullet \to M$ where each $F_i$ is a finite free $R$-module.
\end{enumerate}
\end{definition}

\noindent
We often use the notation $F_{\bullet}$ to denote a complex
of $R$-modules
$$
\ldots \to F_i \to F_{i-1} \to \ldots
$$
In this case we often use $d_i$ or $d_{F, i}$ to denote the map
$F_i \to F_{i-1}$. In this section we are always going to
assume that $F_0$ is the last nonzero term in the complex.
The {\it $i$th homology group of the complex} $F_{\bullet}$
is the group $H_i = \Ker(d_{F, i})/\Im(d_{F, i + 1})$.
A {\it map of complexes $\alpha : F_{\bullet} \to G_{\bullet}$}
is given by maps $\alpha_i : F_i \to G_i$ such that
$\alpha_{i-1} \circ d_{F, i} = d_{G, i-1} \circ \alpha_i$.
Such a map induces a map on homology $H_i(\alpha) :
H_i(F_{\bullet}) \to H_i(G_{\bullet})$. If $\alpha, \beta
:  F_{\bullet} \to G_{\bullet}$ are maps of complexes, then
a {\it homotopy} between $\alpha$ and $\beta$ is given by
a collection of maps $h_i : F_i \to G_{i + 1}$ such that
$\alpha_i - \beta_i = d_{G, i + 1} \circ h_i +
h_{i-1} \circ d_{F, i}$.
Two maps $\alpha, \beta : F_{\bullet} \to G_{\bullet}$ are
said to be {\it homotopic} if a homotopy between $\alpha$
and $\beta$ exists.

\medskip\noindent
We will use a very similar notation regarding complexes
of the form $F^{\bullet}$ which look like
$$
\ldots \to F^i \xrightarrow{d^i} F^{i + 1} \to \ldots
$$
There are maps of complexes, homotopies, etc.
In this case we set $H^i(F^{\bullet}) =
\Ker(d^i)/\Im(d^{i - 1})$ and we call it
the {\it $i$th cohomology group}.
```

Français restauré :
```tex
\begin{definition}
\label{definition-finite-free-resolution}
Soit $R$ un anneau. Soit $M$ un $R$-module.
\begin{enumerate}
\item Une {\it résolution} (à gauche) $F_\bullet \to M$ de $M$ est un complexe exact
$$
\ldots \to F_2 \to F_1 \to F_0 \to M \to 0
$$
de $R$-modules.
\item Une {\it résolution de $M$ par des $R$-modules libres} est une résolution
$F_\bullet \to M$ dans laquelle chaque $F_i$ est un $R$-module libre.
\item Une {\it résolution de $M$ par des $R$-modules libres de type fini} est une résolution
$F_\bullet \to M$ dans laquelle chaque $F_i$ est un $R$-module libre de type fini.
\end{enumerate}
\end{definition}

\noindent
Nous employons souvent la notation $F_{\bullet}$ pour désigner un complexe
de $R$-modules
$$
\ldots \to F_i \to F_{i-1} \to \ldots
$$
Dans ce cas, nous notons souvent $d_i$ ou $d_{F, i}$ l'application
$F_i \to F_{i-1}$. Dans cette section, nous supposerons toujours
que $F_0$ est le dernier terme non nul du complexe.
Le {\it $i$-ième groupe d'homologie du complexe} $F_{\bullet}$
est le groupe $H_i = \Ker(d_{F, i})/\Im(d_{F, i + 1})$.
Un {\it morphisme de complexes $\alpha : F_{\bullet} \to G_{\bullet}$}
est donné par des applications $\alpha_i : F_i \to G_i$ telles que
$\alpha_{i-1} \circ d_{F, i} = d_{G, i-1} \circ \alpha_i$.
Un tel morphisme induit en homologie une application $H_i(\alpha) :
H_i(F_{\bullet}) \to H_i(G_{\bullet})$. Si $\alpha, \beta
:  F_{\bullet} \to G_{\bullet}$ sont des morphismes de complexes, une
{\it homotopie} entre $\alpha$ et $\beta$ est donnée par
une famille d'applications $h_i : F_i \to G_{i + 1}$ telles que
$\alpha_i - \beta_i = d_{G, i + 1} \circ h_i +
h_{i-1} \circ d_{F, i}$.
Deux morphismes $\alpha, \beta : F_{\bullet} \to G_{\bullet}$ sont dits
{\it homotopes} s'il existe une homotopie entre $\alpha$
et $\beta$.

\medskip\noindent
Nous emploierons des notations tout à fait analogues pour les complexes
de la forme $F^{\bullet}$ qui s'écrivent
$$
\ldots \to F^i \xrightarrow{d^i} F^{i + 1} \to \ldots
$$
On dispose de morphismes de complexes, d'homotopies, etc.
Dans ce cas, nous posons $H^i(F^{\bullet}) =
\Ker(d^i)/\Im(d^{i - 1})$ et nous l'appelons le
{\it $i$-ième groupe de cohomologie}.
```

</details>

### 04 — lemma-homotopic-equal-homology

Anglais L17489–17498 ; français L17255–17264.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17489) · FR-ALGEBRA-B37-CHOICE-0004.

Le quantificateur porte sur deux morphismes homotopes quelconques et leur action en (co)homologie. Laszlo VIII.3.2 explique la même propriété, mais sa preuve n'est pas importée. Omis est remplacé par Démonstration omise : le substantif explicite l'objet de l'omission et donne l'accord féminin. Aucun argument absent n'est ajouté ; c'est une normalisation de notice, pas une correction de théorème.

Point particulier à relire : Omis peut être compris comme une ellipse d'argument omis. La formulation explicite choisie correspond à Démonstration dans l'édition et évite cet accord implicite. Pas d'attestation externe revendiquée pour cette simple notice française.

Règles : FR-ALGEBRA-B37-RULE-RESOLUTION, FR-ALGEBRA-B37-RULE-HOMOLOGY, FR-ALGEBRA-B37-RULE-MAP, FR-ALGEBRA-B37-RULE-LOGIC, FR-ALGEBRA-B37-RULE-OMISSION.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-homotopic-equal-homology}
Any two homotopic maps of complexes induce the same maps on
(co)homology groups.
\end{lemma}

\begin{proof}
Omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-homotopic-equal-homology}
Deux morphismes de complexes homotopes quelconques induisent les mêmes applications sur les
groupes de (co)homologie.
\end{lemma}

\begin{proof}
Démonstration omise.
\end{proof}
```

</details>

### 05 — lemma-compare-resolutions

Anglais L17499–17573 ; français L17265–17339.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17499) · FR-ALGEBRA-B37-CHOICE-0005.

Les deux conclusions et les deux récurrences sont comparées intégralement. Le complexe F n'est pas supposé être une résolution ; seule la résolution cible est exacte et tous les F_i sont libres. Relèvement, noyau, image et homotope à zéro décrivent exactement les factorisations utilisées. Laszlo VIII.3.3–3.4 appuie le registre du changement de résolution, sans importer son hypothèse de résolution projective à la place du complexe source de Stacks. La définition de Ext, les deux conventions de degré, la note un/le et l'identification Ext0=Hom sont incluses dans cette paire.

Point particulier à relire : Ne pas supposer le complexe F exact ni ses termes de rang fini. L'usage du singulier un groupe Ext dans la note est intentionnel avant la preuve d'indépendance, non une faute à normaliser.

Règles : FR-ALGEBRA-B37-RULE-RESOLUTION, FR-ALGEBRA-B37-RULE-HOMOLOGY, FR-ALGEBRA-B37-RULE-MAP, FR-ALGEBRA-B37-RULE-EXACT, FR-ALGEBRA-B37-RULE-DEPTH, FR-ALGEBRA-B37-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-compare-resolutions}
Let $R$ be a ring. Let $M \to N$ be a map of $R$-modules.
Let $N_\bullet \to N$ be an arbitrary resolution.
Let
$$
\ldots \to F_2 \to F_1 \to F_0 \to M
$$
be a complex of $R$-modules where each $F_i$ is a free $R$-module. Then
\begin{enumerate}
\item there exists a map of complexes $F_\bullet \to N_\bullet$ such that
$$
\xymatrix{
F_0 \ar[r] \ar[d] & M \ar[d] \\
N_0 \ar[r] & N
}
$$
is commutative, and
\item any two maps $\alpha, \beta : F_\bullet \to N_\bullet$ as in (1)
are homotopic.
\end{enumerate}
\end{lemma}

\begin{proof}
Proof of (1). Because $F_0$ is free we can find a map $F_0 \to N_0$
lifting the map $F_0 \to M \to N$. We obtain an induced
map $F_1 \to F_0 \to N_0$ which ends up in the image
of $N_1 \to N_0$. Since $F_1$ is free we may lift this
to a map $F_1 \to N_1$. This in turn induces a map
$F_2 \to F_1 \to N_1$ which maps to zero into
$N_0$. Since $N_\bullet$ is exact we see that
the image of this map is contained in the image
of $N_2 \to N_1$. Hence we may lift to get a map
$F_2 \to N_2$. Repeat.

\medskip\noindent
Proof of (2). To show that $\alpha, \beta$ are homotopic it suffices
to show the difference $\gamma = \alpha - \beta$ is homotopic
to zero. Note that the image of $\gamma_0 : F_0 \to N_0$
is contained in the image of $N_1 \to N_0$. Hence we may lift
$\gamma_0$ to a map $h_0 : F_0 \to N_1$. Consider the map
$\gamma_1' = \gamma_1 - h_0 \circ d_{F, 1}$. By our choice of $h_0$
we see that the image of $\gamma_1'$ is contained in
the kernel of $N_1 \to N_0$. Since $N_\bullet$ is exact
we may lift $\gamma_1'$ to a map $h_1 : F_1 \to N_2$.
At this point we have $\gamma_1 = h_0 \circ d_{F, 1}
+ d_{N, 2} \circ h_1$. Repeat.
\end{proof}

\noindent
At this point we are ready to define the groups
$\Ext^i_R(M, N)$. Namely, choose a resolution
$F_{\bullet}$ of $M$ by free $R$-modules, see Lemma
\ref{lemma-resolution-by-finite-free}. Consider
the (cohomological) complex
$$
\Hom_R(F_\bullet, N) :
\Hom_R(F_0, N) \to
\Hom_R(F_1, N) \to
\Hom_R(F_2, N) \to \ldots
$$
We define $\Ext^i_R(M, N)$ for $i \geq 0$ to be the $i$th
cohomology group of this complex\footnote{At this point
it would perhaps be more appropriate to say ``an'' in stead
of ``the'' Ext-group.}. For $i < 0$ we set $\Ext^i_R(M, N) = 0$.
Before we continue we point out that
$$
\Ext^0_R(M, N) = \Ker(\Hom_R(F_0, N) \to \Hom_R(F_1, N)) =
\Hom_R(M, N)
$$
because we can apply part (1) of Lemma \ref{lemma-hom-exact} to
the exact sequence $F_1 \to F_0 \to M \to 0$.
The following lemma explains
in what sense this is well defined.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-compare-resolutions}
Soit $R$ un anneau. Soit $M \to N$ un homomorphisme de $R$-modules.
Soit $N_\bullet \to N$ une résolution quelconque.
Soit
$$
\ldots \to F_2 \to F_1 \to F_0 \to M
$$
un complexe de $R$-modules dans lequel chaque $F_i$ est un $R$-module libre. Alors
\begin{enumerate}
\item il existe un morphisme de complexes $F_\bullet \to N_\bullet$ tel que
$$
\xymatrix{
F_0 \ar[r] \ar[d] & M \ar[d] \\
N_0 \ar[r] & N
}
$$
soit commutatif, et
\item deux morphismes quelconques $\alpha, \beta : F_\bullet \to N_\bullet$ comme en (1)
sont homotopes.
\end{enumerate}
\end{lemma}

\begin{proof}
Démonstration de (1). Puisque $F_0$ est libre, on peut trouver une application $F_0 \to N_0$
qui relève l'application $F_0 \to M \to N$. On obtient une application induite
$F_1 \to F_0 \to N_0$ dont l'image est contenue dans l'image
de $N_1 \to N_0$. Puisque $F_1$ est libre, on peut la relever
en une application $F_1 \to N_1$. Celle-ci induit à son tour une application
$F_2 \to F_1 \to N_1$ dont l'image dans
$N_0$ est nulle. Comme $N_\bullet$ est exact, on voit que
l'image de cette application est contenue dans l'image
de $N_2 \to N_1$. On peut donc la relever en une application
$F_2 \to N_2$. On poursuit ainsi.

\medskip\noindent
Démonstration de (2). Pour montrer que $\alpha, \beta$ sont homotopes, il suffit
de montrer que la différence $\gamma = \alpha - \beta$ est homotope
à zéro. Remarquons que l'image de $\gamma_0 : F_0 \to N_0$
est contenue dans l'image de $N_1 \to N_0$. On peut donc relever
$\gamma_0$ en une application $h_0 : F_0 \to N_1$. Considérons l'application
$\gamma_1' = \gamma_1 - h_0 \circ d_{F, 1}$. Par le choix de $h_0$,
on voit que l'image de $\gamma_1'$ est contenue dans
le noyau de $N_1 \to N_0$. Comme $N_\bullet$ est exact,
on peut relever $\gamma_1'$ en une application $h_1 : F_1 \to N_2$.
À ce stade, on a $\gamma_1 = h_0 \circ d_{F, 1}
+ d_{N, 2} \circ h_1$. On poursuit ainsi.
\end{proof}

\noindent
Nous sommes maintenant en mesure de définir les groupes
$\Ext^i_R(M, N)$. Choisissons une résolution
$F_{\bullet}$ de $M$ par des $R$-modules libres, voir le Lemme
\ref{lemma-resolution-by-finite-free}. Considérons
le complexe (cohomologique)
$$
\Hom_R(F_\bullet, N) :
\Hom_R(F_0, N) \to
\Hom_R(F_1, N) \to
\Hom_R(F_2, N) \to \ldots
$$
On définit $\Ext^i_R(M, N)$, pour $i \geq 0$, comme le $i$-ième
groupe de cohomologie de ce complexe\footnote{À ce stade,
il conviendrait peut-être davantage de dire ``un'' plutôt
que ``le'' groupe Ext.}. Pour $i < 0$, on pose $\Ext^i_R(M, N) = 0$.
Avant de poursuivre, signalons que
$$
\Ext^0_R(M, N) = \Ker(\Hom_R(F_0, N) \to \Hom_R(F_1, N)) =
\Hom_R(M, N)
$$
car on peut appliquer la partie (1) du Lemme \ref{lemma-hom-exact} à
la suite exacte $F_1 \to F_0 \to M \to 0$.
Le lemme suivant précise
en quel sens cette définition est bien définie.
```

</details>

### 06 — lemma-ext-welldefined

Anglais L17574–17621 ; français L17340–17387.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17574) · FR-ALGEBRA-B37-CHOICE-0006.

Énoncé, indépendance du relèvement, cas isomorphisme, cas identité et preuve entière sont comparés. Bien définie, homotope et application induite sont idiomatiques ; l'indépendance ne signifie pas une identité littérale des complexes. Les directions Hom et l'ordre de composition de l'anglais ne respectent pas la contravariance du premier argument : ils restent littéraux dans le français diplomatique, avec justification séparée par précomposition. H_i au lieu de H^i est également signalé, non rectifié silencieusement. L'exemple16.2 de Laszlo confirme la précomposition ; sa propre prose ne remplace pas l'autorité mathématique.

Point particulier à relire : La contravariance exige Hom(G,N)→Hom(F,N), donc (alpha∘beta)*=beta*∘alpha*. La correction de ces formules appartient à un texte éditorial distinct ; elle n'est pas introduite dans cette traduction diplomatique. Les trois lieux liés sont explicitement fournis dans l'observation source.

Règles : FR-ALGEBRA-B37-RULE-RESOLUTION, FR-ALGEBRA-B37-RULE-HOMOLOGY, FR-ALGEBRA-B37-RULE-MAP, FR-ALGEBRA-B37-RULE-DEPTH, FR-ALGEBRA-B37-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ext-welldefined}
Let $R$ be a ring. Let $M_1, M_2, N$ be $R$-modules.
Suppose that $F_{\bullet}$ is a free resolution of the module $M_1$,
and $G_{\bullet}$ is a free resolution of the module $M_2$.
Let $\varphi : M_1 \to M_2$ be a module map.
Let $\alpha : F_{\bullet} \to G_{\bullet}$ be
a map of complexes inducing $\varphi$ on
$M_1 = \Coker(d_{F, 1}) \to M_2 = \Coker(d_{G, 1})$,
see Lemma \ref{lemma-compare-resolutions}.
Then the induced maps
$$
H^i(\alpha) :
H^i(\Hom_R(F_{\bullet}, N))
\longrightarrow
H^i(\Hom_R(G_{\bullet}, N))
$$
are independent of the choice of $\alpha$.
If $\varphi$ is an isomorphism, so are all the maps
$H^i(\alpha)$. If $M_1 = M_2$, $F_\bullet = G_\bullet$, and
$\varphi$ is the identity, so are all the maps $H_i(\alpha)$.
\end{lemma}

\begin{proof}
Another map $\beta : F_{\bullet} \to G_{\bullet}$
inducing $\varphi$ is homotopic to $\alpha$ by
Lemma \ref{lemma-compare-resolutions}. Hence the
maps $\Hom_R(F_\bullet, N) \to
\Hom_R(G_\bullet, N)$ are homotopic.
Hence the independence result follows from
Lemma \ref{lemma-homotopic-equal-homology}.

\medskip\noindent
Suppose that $\varphi$ is an isomorphism.
Let $\psi : M_2 \to M_1$ be an inverse.
Choose $\beta : G_{\bullet} \to F_{\bullet}$
be a map inducing $\psi :
M_2 = \Coker(d_{G, 1}) \to M_1 = \Coker(d_{F, 1})$,
see Lemma \ref{lemma-compare-resolutions}.
OK, and now consider the map
$H^i(\alpha) \circ H^i(\beta) =
H^i(\alpha \circ \beta)$. By the above the
map $H^i(\alpha \circ \beta)$ is the {\it same}
as the map $H^i(\text{id}_{G_{\bullet}}) = \text{id}$.
Similarly for the composition $H^i(\beta) \circ H^i(\alpha)$.
Hence $H^i(\alpha)$ and $H^i(\beta)$ are inverses of each other.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ext-welldefined}
Soit $R$ un anneau. Soient $M_1, M_2, N$ des $R$-modules.
Supposons que $F_{\bullet}$ soit une résolution libre du module $M_1$,
et que $G_{\bullet}$ soit une résolution libre du module $M_2$.
Soit $\varphi : M_1 \to M_2$ un homomorphisme de modules.
Soit $\alpha : F_{\bullet} \to G_{\bullet}$
un morphisme de complexes qui induit $\varphi$ sur
$M_1 = \Coker(d_{F, 1}) \to M_2 = \Coker(d_{G, 1})$,
voir le Lemme \ref{lemma-compare-resolutions}.
Alors les applications induites
$$
H^i(\alpha) :
H^i(\Hom_R(F_{\bullet}, N))
\longrightarrow
H^i(\Hom_R(G_{\bullet}, N))
$$
ne dépendent pas du choix de $\alpha$.
Si $\varphi$ est un isomorphisme, toutes les applications
$H^i(\alpha)$ sont des isomorphismes. Si $M_1 = M_2$, $F_\bullet = G_\bullet$, et
si $\varphi$ est l'identité, toutes les applications $H_i(\alpha)$ le sont aussi.
\end{lemma}

\begin{proof}
Un autre morphisme $\beta : F_{\bullet} \to G_{\bullet}$
qui induit $\varphi$ est homotope à $\alpha$ d'après le
Lemme \ref{lemma-compare-resolutions}. Les
applications $\Hom_R(F_\bullet, N) \to
\Hom_R(G_\bullet, N)$ sont donc homotopes.
L'indépendance résulte alors du
Lemme \ref{lemma-homotopic-equal-homology}.

\medskip\noindent
Supposons que $\varphi$ soit un isomorphisme.
Soit $\psi : M_2 \to M_1$ un inverse.
Choisissons $\beta : G_{\bullet} \to F_{\bullet}$
qui induit $\psi :
M_2 = \Coker(d_{G, 1}) \to M_1 = \Coker(d_{F, 1})$,
voir le Lemme \ref{lemma-compare-resolutions}.
Considérons maintenant l'application
$H^i(\alpha) \circ H^i(\beta) =
H^i(\alpha \circ \beta)$. D'après ce qui précède, l'application
$H^i(\alpha \circ \beta)$ est la {\it même}
que l'application $H^i(\text{id}_{G_{\bullet}}) = \text{id}$.
Il en va de même de la composée $H^i(\beta) \circ H^i(\alpha)$.
Ainsi $H^i(\alpha)$ et $H^i(\beta)$ sont inverses l'une de l'autre.
\end{proof}
```

</details>

### 07 — lemma-long-exact-seq-ext

Anglais L17622–17658 ; français L17388–17424.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17622) · FR-ALGEBRA-B37-CHOICE-0007.

La suite exacte longue est covariante en N. Les trois termes Hom et Ext1, leur ordre et la continuation sont conservés. La liberté de chacun des F_i donne l'exactitude de Hom(F_i,-). La preuve par suite courte de complexes et lemme du serpent reste entière ; Laszlo VII.3 atteste cette construction et son registre. Le singulier français chacun est correctement accordé, malgré each…are dans l'anglais.

Règles : FR-ALGEBRA-B37-RULE-RESOLUTION, FR-ALGEBRA-B37-RULE-EXACT, FR-ALGEBRA-B37-RULE-DEPTH, FR-ALGEBRA-B37-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-long-exact-seq-ext}
Let $R$ be a ring. Let $M$ be an $R$-module.
Let $0 \to N' \to N \to N'' \to 0$ be a
short exact sequence. Then we get a long exact
sequence
$$
\begin{matrix}
0
\to \Hom_R(M, N')
\to \Hom_R(M, N)
\to \Hom_R(M, N'')
\\
\phantom{0\ }
\to \Ext^1_R(M, N')
\to \Ext^1_R(M, N)
\to \Ext^1_R(M, N'')
\to \ldots
\end{matrix}
$$
\end{lemma}

\begin{proof}
Pick a free resolution $F_{\bullet} \to M$.
Since each of the $F_i$ are free we see that
we get a short exact sequence of complexes
$$
0 \to
\Hom_R(F_{\bullet}, N') \to
\Hom_R(F_{\bullet}, N) \to
\Hom_R(F_{\bullet}, N'') \to
0
$$
Thus we get the long exact sequence from
the snake lemma applied to this.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-long-exact-seq-ext}
Soit $R$ un anneau. Soit $M$ un $R$-module.
Soit $0 \to N' \to N \to N'' \to 0$ une
suite exacte courte. On obtient alors une suite exacte
longue
$$
\begin{matrix}
0
\to \Hom_R(M, N')
\to \Hom_R(M, N)
\to \Hom_R(M, N'')
\\
\phantom{0\ }
\to \Ext^1_R(M, N')
\to \Ext^1_R(M, N)
\to \Ext^1_R(M, N'')
\to \ldots
\end{matrix}
$$
\end{lemma}

\begin{proof}
Choisissons une résolution libre $F_{\bullet} \to M$.
Comme chacun des $F_i$ est libre, on obtient
une suite exacte courte de complexes
$$
0 \to
\Hom_R(F_{\bullet}, N') \to
\Hom_R(F_{\bullet}, N) \to
\Hom_R(F_{\bullet}, N'') \to
0
$$
La suite exacte longue résulte alors du
lemme du serpent appliqué à cette suite.
\end{proof}
```

</details>

### 08 — lemma-reverse-long-exact-seq-ext

Anglais L17659–17722 ; français L17425–17488.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17659) · FR-ALGEBRA-B37-CHOICE-0008.

La suite exacte longue est contravariante en M. Toute la construction par générateurs et relèvements, les deux diagrammes, la suite de noyaux et l'itération sont comparés. Chaque degré est exact scindé par construction, sans supposer la suite originale scindée. Appliquer Hom(-,N) renverse correctement cette suite. Laszlo VIII.5.1 atteste la construction de résolutions pour une suite courte ; aucune démonstration externe n'est ajoutée.

Point particulier à relire : Exacte scindée concerne les suites de termes libres construites, pas 0→M'→M→M''→0. L'ordre inversé des arguments est vérifié, contrairement aux flèches du lemme bien-définition.

Règles : FR-ALGEBRA-B37-RULE-RESOLUTION, FR-ALGEBRA-B37-RULE-MAP, FR-ALGEBRA-B37-RULE-EXACT, FR-ALGEBRA-B37-RULE-DEPTH, FR-ALGEBRA-B37-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-reverse-long-exact-seq-ext}
Let $R$ be a ring. Let $N$ be an $R$-module.
Let $0 \to M' \to M \to M'' \to 0$ be a
short exact sequence. Then we get a long exact
sequence
$$
\begin{matrix}
0
\to \Hom_R(M'', N)
\to \Hom_R(M, N)
\to \Hom_R(M', N)
\\
\phantom{0\ }
\to \Ext^1_R(M'', N)
\to \Ext^1_R(M, N)
\to \Ext^1_R(M', N)
\to \ldots
\end{matrix}
$$
\end{lemma}

\begin{proof}
Pick sets of generators $\{m'_{i'}\}_{i' \in I'}$ and
$\{m''_{i''}\}_{i'' \in I''}$ of $M'$ and $M''$.
For each $i'' \in I''$ choose a lift $\tilde m''_{i''} \in M$
of the element $m''_{i''} \in M''$. Set $F' = \bigoplus_{i' \in I'} R$,
$F'' = \bigoplus_{i'' \in I''} R$ and $F = F' \oplus F''$.
Mapping the generators of these free modules to the corresponding
chosen generators gives surjective $R$-module maps $F' \to M'$,
$F'' \to M''$, and $F \to M$. We obtain a map of short exact sequences
$$
\begin{matrix}
0 & \to & M' & \to & M & \to & M'' & \to & 0 \\
& & \uparrow & & \uparrow & & \uparrow \\
0 & \to & F' & \to & F & \to & F'' & \to & 0 \\
\end{matrix}
$$
By the snake lemma we see that the sequence of kernels
$0 \to K' \to K \to K'' \to 0$ is short exact sequence of $R$-modules.
Hence we can continue this process indefinitely. In other words
we obtain a short exact sequence of resolutions fitting into the diagram
$$
\begin{matrix}
0 & \to & M' & \to & M & \to & M'' & \to & 0 \\
& & \uparrow & & \uparrow & & \uparrow \\
0 & \to & F_\bullet' & \to & F_\bullet & \to & F_\bullet'' & \to & 0 \\
\end{matrix}
$$
Because each of the sequences $0 \to F'_n \to F_n \to F''_n \to 0$
is split exact (by construction) we obtain a short exact sequence of
complexes
$$
0 \to
\Hom_R(F''_{\bullet}, N) \to
\Hom_R(F_{\bullet}, N) \to
\Hom_R(F'_{\bullet}, N) \to
0
$$
by applying the $\Hom_R(-, N)$ functor.
Thus we get the long exact sequence from
the snake lemma applied to this.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-reverse-long-exact-seq-ext}
Soit $R$ un anneau. Soit $N$ un $R$-module.
Soit $0 \to M' \to M \to M'' \to 0$ une
suite exacte courte. On obtient alors une suite exacte
longue
$$
\begin{matrix}
0
\to \Hom_R(M'', N)
\to \Hom_R(M, N)
\to \Hom_R(M', N)
\\
\phantom{0\ }
\to \Ext^1_R(M'', N)
\to \Ext^1_R(M, N)
\to \Ext^1_R(M', N)
\to \ldots
\end{matrix}
$$
\end{lemma}

\begin{proof}
Choisissons des systèmes de générateurs $\{m'_{i'}\}_{i' \in I'}$ et
$\{m''_{i''}\}_{i'' \in I''}$ de $M'$ et de $M''$.
Pour chaque $i'' \in I''$, choisissons un relèvement $\tilde m''_{i''} \in M$
de l'élément $m''_{i''} \in M''$. Posons $F' = \bigoplus_{i' \in I'} R$,
$F'' = \bigoplus_{i'' \in I''} R$ et $F = F' \oplus F''$.
En envoyant les générateurs de ces modules libres sur les générateurs choisis
correspondants, on obtient des homomorphismes surjectifs de $R$-modules $F' \to M'$,
$F'' \to M''$ et $F \to M$. On obtient un morphisme de suites exactes courtes
$$
\begin{matrix}
0 & \to & M' & \to & M & \to & M'' & \to & 0 \\
& & \uparrow & & \uparrow & & \uparrow \\
0 & \to & F' & \to & F & \to & F'' & \to & 0 \\
\end{matrix}
$$
Le lemme du serpent montre que la suite des noyaux
$0 \to K' \to K \to K'' \to 0$ est une suite exacte courte de $R$-modules.
On peut donc poursuivre indéfiniment ce procédé. Autrement dit,
on obtient une suite exacte courte de résolutions qui s'insère dans le diagramme
$$
\begin{matrix}
0 & \to & M' & \to & M & \to & M'' & \to & 0 \\
& & \uparrow & & \uparrow & & \uparrow \\
0 & \to & F_\bullet' & \to & F_\bullet & \to & F_\bullet'' & \to & 0 \\
\end{matrix}
$$
Comme chacune des suites $0 \to F'_n \to F_n \to F''_n \to 0$
est exacte scindée (par construction), on obtient une suite exacte courte de
complexes
$$
0 \to
\Hom_R(F''_{\bullet}, N) \to
\Hom_R(F_{\bullet}, N) \to
\Hom_R(F'_{\bullet}, N) \to
0
$$
en appliquant le foncteur $\Hom_R(-, N)$.
La suite exacte longue résulte alors du
lemme du serpent appliqué à cette suite.
\end{proof}
```

</details>

### 09 — lemma-annihilate-ext

Anglais L17723–17742 ; français L17489–17508.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17723) · FR-ALGEBRA-B37-CHOICE-0009.

Les deux conditions alternatives xN=0 ou xM=0 sont conservées. Annule ne signifie pas seulement une action nilpotente : x agit par zéro sur chaque Ext. Le premier cas utilise le complexe Hom, le second l'indépendance du relèvement et l'homotopie à l'application nulle. Les formules source restent exactes et l'anomalie de variance du lemme précédent n'est pas masquée.

Règles : FR-ALGEBRA-B37-RULE-RESOLUTION, FR-ALGEBRA-B37-RULE-HOMOLOGY, FR-ALGEBRA-B37-RULE-MAP, FR-ALGEBRA-B37-RULE-DEPTH, FR-ALGEBRA-B37-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-annihilate-ext}
Let $R$ be a ring. Let $M$, $N$ be $R$-modules.
Any $x\in R$ such that either $xN = 0$, or $xM = 0$
annihilates each of the modules $\Ext^i_R(M, N)$.
\end{lemma}

\begin{proof}
Pick a free resolution $F_{\bullet}$ of $M$.
Since $\Ext^i_R(M, N)$
is defined as the cohomology of the complex
$\Hom_R(F_{\bullet}, N)$ the lemma is
clear when $xN = 0$. If $xM = 0$, then
we see that multiplication by $x$ on $F_{\bullet}$
lifts the zero map on $M$. Hence by Lemma
\ref{lemma-ext-welldefined} we see that it
induces the same map on Ext groups as the
zero map.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-annihilate-ext}
Soit $R$ un anneau. Soient $M$, $N$ des $R$-modules.
Tout $x\in R$ tel que $xN = 0$ ou $xM = 0$
annule chacun des modules $\Ext^i_R(M, N)$.
\end{lemma}

\begin{proof}
Choisissons une résolution libre $F_{\bullet}$ de $M$.
Puisque $\Ext^i_R(M, N)$
est défini comme la cohomologie du complexe
$\Hom_R(F_{\bullet}, N)$, le lemme est
clair lorsque $xN = 0$. Si $xM = 0$, alors
la multiplication par $x$ sur $F_{\bullet}$
relève l'application nulle sur $M$. Ainsi, d'après le Lemme
\ref{lemma-ext-welldefined}, elle induit
la même application sur les groupes Ext que l'application
nulle.
\end{proof}
```

</details>

### 10 — lemma-ext-noetherian

Anglais L17743–17758 ; français L17509–17524.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17743) · FR-ALGEBRA-B37-CHOICE-0010.

Les deux modules M et N sont de type fini et l'anneau est noethérien. La finitude de chaque terme Hom d'une résolution à termes libres de type fini donne la finitude des sous-quotients de cohomologie ; il n'est pas affirmé que la résolution est bornée. Chaque i inclut les degrés négatifs, où Ext est nul par la convention précédente. Type fini est attesté chez Peskine et Laszlo ; aucune dimension projective finie n'est ajoutée.

Règles : FR-ALGEBRA-B37-RULE-RESOLUTION, FR-ALGEBRA-B37-RULE-HOMOLOGY, FR-ALGEBRA-B37-RULE-DEPTH, FR-ALGEBRA-B37-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ext-noetherian}
Let $R$ be a Noetherian ring. Let $M$, $N$ be finite $R$-modules.
Then $\Ext^i_R(M, N)$ is a finite $R$-module for all $i$.
\end{lemma}

\begin{proof}
This holds because $\Ext^i_R(M, N)$ is computed as the
cohomology groups of a complex $\Hom_R(F_\bullet, N)$
with each $F_n$ a finite free $R$-module, see
Lemma \ref{lemma-resolution-by-finite-free}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ext-noetherian}
Soit $R$ un anneau noethérien. Soient $M$, $N$ des $R$-modules de type fini.
Alors $\Ext^i_R(M, N)$ est un $R$-module de type fini pour tout $i$.
\end{lemma}

\begin{proof}
Cela résulte de ce que $\Ext^i_R(M, N)$ se calcule comme les
groupes de cohomologie d'un complexe $\Hom_R(F_\bullet, N)$
où chaque $F_n$ est un $R$-module libre de type fini ; voir le
Lemme \ref{lemma-resolution-by-finite-free}.
\end{proof}
```

</details>

## Contrôles et suite

Les 202 régions mathématiques nouvelles sont exactement identiques. Le préfixe de 12 593 régions passe avec quarante-trois exceptions linguistiques antérieures précisément recensées dans leur ordre et avec leurs multiplicités.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items sont identiques. Aucun titre facultatif ni citation dans ce lot. L’opération inverse retrouve le lot précédent puis tous les octets du témoin public préservé ; préfixe antérieur et suffixe ultérieur restent inchangés.

Les 644 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Profondeur, anglais L17759 /français L17525. Aucun PDF nouveau ni publication ; restauration globale en cours.

