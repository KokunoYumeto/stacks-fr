# Homéomorphismes universels et irréductibilité géométrique

## Résultat et portée

Deux sections entièrement comparées : anglais L10604–11483 (880 lignes), français L10559–11441 (883 lignes), soit 27 paires complètes avec preuves et transitions. 277 occurrences sont reliées à des choix contextualisés. La lecture continue atteint 47 sections, 401 paires et 3287 occurrences ; ni le chapitre ni l’édition ne sont terminés.

Quatre réparations propres au français : deux occurrences de domaines deviennent anneaux intègres ; un antécédent est explicité pour que le diviseur de zéro appartienne à l’anneau, non au spectre ; le libellé bibliographique Lemma devient Lemme. Aucun symbole mathématique, numéro bibliographique ni identifiant de référence ne change.

Un lapsus de variable du texte anglais, T pour t, est signalé séparément et reste dans la traduction. Une autre phrase sur les puissances dans une fibre appelle une lecture attentive, mais n’est pas déclarée fausse et n’est pas comptée comme erratum.

Lecture, réparations et dossier produits par OpenAI Codex — GPT-6 Astra, Ultra effort ; travail assisté par IA, sans relecture humaine. Les attestations du canon ont été consultées rétrospectivement, dans les limites indiquées ci-dessous.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch15.fr.tex) · [État français précédent](staged/fr/010_algebra.prose-batch14.fr.tex) · [Lot précédent](ALGEBRA_PROSE_BATCH14_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH15_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH15_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH15_OCCURRENCES.json) · [Avant/après](ALGEBRA_PROSE_BATCH15_REPAIRS.json) · [Exception en formule](ALGEBRA_PROSE_BATCH15_MATH_EXCEPTIONS.json) · [Libellé bibliographique](ALGEBRA_PROSE_BATCH15_CITATION_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH15_COVERAGE.json) · [Observation séparée](ALGEBRA_PROSE_BATCH15_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Grothendieck et Dieudonné — EGA IV seconde partie

[Source consultée](https://www.numdam.org/item/PMIHES_1965__24__5_0.pdf) · [Fichier conservé](canon-consulted/fr-algebra/ega-iv2-numdam.pdf)

Pages PDF 16–17, 57–58 et 64–65, imprimées 19–20, 60–61 et 67–68, entièrement lues ; définitions 2.4.2 et 4.5.2, propositions 2.4.4–5, 4.5.1 et 4.5.21. Page imprimée 20 rendue avec Poppler et inspectée.

Attestations courtes : « homéomorphisme universel », « entier, surjectif et radiciel », « géométriquement irréductible », « composantes irréductibles ».

Atteste le titre, les propriétés topologiques stables par changement de base et l'irréductibilité géométrique. Distingue morphisme entier et anneau intègre, homéomorphisme sur son image et sur tout le but.

Limites : L'OCR déforme certaines formules ; elles ne servent pas à réécrire Stacks. Les hypothèses de finitude ou de noethérianité du contexte EGA ne sont pas importées dans les énoncés plus généraux de Stacks. Consultation rétrospective, pas certification humaine.

SHA-256 : C3E960AA1C5C37046E8892D8A3CAC098E2738164136B5CDAA5D5D893F89931DA.

### Antoine Ducros — Introduction à la théorie des schémas

[Source consultée](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages 23 et 103 entièrement lues ; définition 0.1.3 et compatibilités 2.6.7.1–5.

Attestations courtes : « anneau intègre », « produit tensoriel », « anneau localisé ».

Intègre désigne un anneau non nul sans diviseurs de zéro. Les isomorphismes tensoriels éclairent le registre des quotients, localisations et changements de base dans les preuves.

Limites : Ces pages attestent les termes et leurs sens ; elles ne remplacent pas les arguments ni les quantificateurs du texte anglais. Consultation rétrospective.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

### Jean-François Dat — Algèbre ENS 2016–2017

[Source consultée](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/AlgebreM1/ENS1617.pdf) · [Fichier conservé](canon-consulted/fr-algebra/dat-algebre-ens1617.pdf)

Page 118 entièrement lue, section 2.6.3 et ses définitions de clôture séparable.

Attestations courtes : « extensions purement inséparables », « séparablement clos », « clôture séparable ».

Distingue extension purement inséparable, clôture séparable relative et clôture séparable absolue. La terminologie des éléments et des extensions est relue dans chaque occurrence.

Limites : Le passage porte sur des extensions algébriques ; il n'autorise pas à supposer algébrique toute extension de corps rencontrée dans Stacks. Quelques ligatures sont mal extraites ; les définitions en prose restent lisibles.

SHA-256 : DB5B7FD8139D62C37D0DDDDC90EF22D3EDCF74CC663C5267815E4EA3CECBBB18.

## Les quatre réparations françaises

### FR-ALGEBRA-B15-REPAIR-0001

Anglais L10635 ; français L10591.

Avant :
```tex
\cite[Lemma 3.1.6]{Alper-adequate}
```

Après :
```tex
\cite[Lemme 3.1.6]{Alper-adequate}
```

Localisation du libellé bibliographique uniquement : Lemme 3.1.6 remplace Lemma 3.1.6 ; la clé et le numéro restent exacts. L'article cité lui-même n'a pas été relu pour ce lot, et n'est pas revendiqué comme canon consulté.

### FR-ALGEBRA-B15-REPAIR-0002

Anglais L11125 ; français L11082.

Avant :
```tex
Nous pouvons donc supposer que $R$ et $S$ sont des domaines.
```

Après :
```tex
Nous pouvons donc supposer que $R$ et $S$ sont des anneaux intègres.
```

Deux calques lexicaux et un antécédent ambigu propres à la formulation française sont réparés. Cet anneau est R⊗_k S ; on ne dit pas qu'un espace topologique contient des diviseurs de zéro. Aucune hypothèse ni conclusion nouvelle.

### FR-ALGEBRA-B15-REPAIR-0003

Anglais L11127 ; français L11084.

Avant :
```tex
Son spectre est donc réductible si et seulement s'il contient un diviseur
de zéro non nul.
```

Après :
```tex
Son spectre est donc réductible si et seulement si cet anneau contient un diviseur
de zéro non nul.
```

Deux calques lexicaux et un antécédent ambigu propres à la formulation française sont réparés. Cet anneau est R⊗_k S ; on ne dit pas qu'un espace topologique contient des diviseurs de zéro. Aucune hypothèse ni conclusion nouvelle.

### FR-ALGEBRA-B15-REPAIR-0004

Anglais L11129 ; français L11086.

Avant :
```tex
ramenons au cas où $R$ et $S$ sont des domaines de type fini sur le corps
```

Après :
```tex
ramenons au cas où $R$ et $S$ sont des anneaux intègres de type fini sur le corps
```

Deux calques lexicaux et un antécédent ambigu propres à la formulation française sont réparés. Cet anneau est R⊗_k S ; on ne dit pas qu'un espace topologique contient des diviseurs de zéro. Aucune hypothèse ni conclusion nouvelle.

## Règles contextualisées

### FR-ALGEBRA-B15-RULE-HOMEO

Homéomorphisme conserve la topologie, contrairement à bijection seule ; sur son image et sur le but sont distingués.

Canon : FR-ALGEBRA-B15-CANON-EGA.

### FR-ALGEBRA-B15-RULE-BASE

Arbitraire signifie toute application de base permise par l'énoncé, sans restriction nouvelle de finitude.

Canon : FR-ALGEBRA-B15-CANON-EGA, FR-ALGEBRA-B15-CANON-DUCROS.

### FR-ALGEBRA-B15-RULE-PURE

Le qualificatif est attaché aux extensions ou aux éléments appropriés, sans le confondre avec simplement inséparable.

Canon : FR-ALGEBRA-B15-CANON-DAT.

### FR-ALGEBRA-B15-RULE-SEP

Le corps séparablement clos n'est pas supposé parfait ; toutes les occurrences sont comparées à la phrase anglaise entière.

Canon : FR-ALGEBRA-B15-CANON-DAT.

### FR-ALGEBRA-B15-RULE-DOMAIN

Domain est rendu par anneau intègre ; intégralité d'un morphisme est une autre notion.

Canon : FR-ALGEBRA-B15-CANON-DUCROS.

### FR-ALGEBRA-B15-RULE-INTEGRAL

Entier peut qualifier un nombre, un élément ou un morphisme ; le passage complet détermine le sens, pas le mot isolé.

Canon : FR-ALGEBRA-B15-CANON-EGA.

### FR-ALGEBRA-B15-RULE-IRRED

Irréductible porte sur le spectre et inclut sa non-vacuité. Le qualificatif géométrique exige l'extension du corps de base.

Canon : FR-ALGEBRA-B15-CANON-EGA.

### FR-ALGEBRA-B15-RULE-PRIME

Les premiers, premiers minimaux et composantes ne sont pas interchangeables ; chaque bijection est contrôlée.

Canon : FR-ALGEBRA-B15-CANON-EGA.

### FR-ALGEBRA-B15-RULE-TENSOR

Produit tensoriel, quotient et localisation restent trois opérations distinctes.

Canon : FR-ALGEBRA-B15-CANON-DUCROS.

### FR-ALGEBRA-B15-RULE-RESIDUE

Appui direct dans la source : résidus aux premiers désignés ; localement nilpotent n'est pas un exposant global unique.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B15-RULE-LOGIC

Portée des quantificateurs, unicité et sens des applications vérifiés dans toutes les paires, non déduits d'une concordance lexicale.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B15-RULE-FINITE

Type fini comme extension de corps, finitude vectorielle et présentation finie ne sont pas confondus.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-universal-homeomorphism

Anglais L10604–10613 ; français L10559–10568.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10604) · FR-ALGEBRA-B15-CHOICE-0001.

Homéomorphisme universel est attesté dans EGA IV, 2.4.2. Le titre ne transforme pas la première assertion en définition : le texte commence par le cas d'une extension algébrique purement inséparable et renvoie au lemme plus général. Le quantificateur toute k-algèbre est conservé.

Règles : FR-ALGEBRA-B15-RULE-HOMEO, FR-ALGEBRA-B15-RULE-PURE, FR-ALGEBRA-B15-RULE-SEP, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Universal homeomorphisms}
\label{section-universal-homeomorphism}

\noindent
Let $k'/k$ be an algebraic purely inseparable field
extension. Then for any $k$-algebra $R$ the ring map
$R \to k' \otimes_k R$ induces a homeomorphism of spectra.
The reason for this is the slightly more general
Lemma \ref{lemma-p-ring-map} below.
```

Français restauré :
```tex
\section{Homéomorphismes universels}
\label{section-universal-homeomorphism}

\noindent
Soit $k'/k$ une extension de corps algébrique purement inséparable.
Alors, pour toute $k$-algèbre $R$, l'application d'anneaux
$R \to k' \otimes_k R$ induit un homéomorphisme des spectres.
La raison en est le
Lemme \ref{lemma-p-ring-map} un peu plus général ci-dessous.
```

</details>

### 02 — lemma-surjective-locally-nilpotent-kernel

Anglais L10614–10631 ; français L10569–10587.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10614) · FR-ALGEBRA-B15-CHOICE-0002.

Surjectivité, noyau localement nilpotent et isomorphismes sur les corps résiduels restent trois informations distinctes. Localement nilpotent n'est pas remplacé par nilpotent : il n'est pas affirmé qu'un exposant unique annule tout le noyau. La preuve conserve le fermé V du noyau puis l'exactitude à droite du produit tensoriel.

Règles : FR-ALGEBRA-B15-RULE-HOMEO, FR-ALGEBRA-B15-RULE-PRIME, FR-ALGEBRA-B15-RULE-TENSOR, FR-ALGEBRA-B15-RULE-RESIDUE, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-surjective-locally-nilpotent-kernel}
Let $\varphi : R \to S$ be a surjective map with locally nilpotent kernel.
Then $\varphi$ induces a homeomorphism of spectra and isomorphisms
on residue fields. For any ring map $R \to R'$ the ring map
$R' \to R' \otimes_R S$ is surjective with locally nilpotent kernel.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-spec-closed} the map $\Spec(S) \to \Spec(R)$ is
a homeomorphism onto the closed subset $V(\Ker(\varphi))$. Of course
$V(\Ker(\varphi)) = \Spec(R)$ because every prime ideal of $R$ contains
every nilpotent element of $R$. This also implies the statement on
residue fields. By right exactness of tensor product we see that
$\Ker(\varphi)R'$ is the kernel of the surjective map $R' \to R' \otimes_R S$.
Hence the final statement by Lemma \ref{lemma-locally-nilpotent}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-surjective-locally-nilpotent-kernel}
Soit $\varphi : R \to S$ un homomorphisme surjectif à noyau localement nilpotent.
Alors $\varphi$ induit un homéomorphisme des spectres et des isomorphismes
sur les corps résiduels. Pour toute application d'anneaux $R \to R'$, l'application
$R' \to R' \otimes_R S$ est surjective à noyau localement nilpotent.
\end{lemma}

\begin{proof}
D'après le Lemme \ref{lemma-spec-closed}, l'application
$\Spec(S) \to \Spec(R)$ est un homéomorphisme sur le sous-ensemble fermé
$V(\Ker(\varphi))$. Bien sûr, $V(\Ker(\varphi)) = \Spec(R)$, car tout idéal
premier de $R$ contient tout élément nilpotent de $R$. Cela implique également
l'assertion sur les corps résiduels. Par l'exactitude à droite du produit
tensoriel, nous voyons que $\Ker(\varphi)R'$ est le noyau de l'application
surjective $R' \to R' \otimes_R S$. La dernière assertion résulte donc du
Lemme \ref{lemma-locally-nilpotent}.
\end{proof}
```

</details>

### 03 — lemma-powers-field

Anglais L10632–10716 ; français L10588–10672.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10632) · FR-ALGEBRA-B15-CHOICE-0003.

L'alternative est k′=k, ou caractéristique positive avec soit pure inséparabilité, soit deux extensions algébriques du corps premier fini. Le français n'impose pas la pure inséparabilité au second de ces deux cas. Toute la preuve par plongements et racines de l'unité est conservée, y compris le dernier argument en caractéristique zéro. Lemma dans le localisateur bibliographique devient Lemme ; numéro 3.1.6 et clé Alper-adequate ne changent pas.

Point particulier à relire : Localisation du libellé bibliographique uniquement : Lemme 3.1.6 remplace Lemma 3.1.6 ; la clé et le numéro restent exacts. L'article cité lui-même n'a pas été relu pour ce lot, et n'est pas revendiqué comme canon consulté.

Règles : FR-ALGEBRA-B15-RULE-PURE, FR-ALGEBRA-B15-RULE-SEP, FR-ALGEBRA-B15-RULE-LOGIC, FR-ALGEBRA-B15-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-powers-field}
\begin{reference}
\cite[Lemma 3.1.6]{Alper-adequate}
\end{reference}
Let $k'/k$ be a field extension. The following are equivalent
\begin{enumerate}
\item for each $x \in k'$ there exists an $n > 0$ such that $x^n \in k$, and
\item $k' = k$ or $k$ and $k'$ have characteristic $p > 0$ and
either $k'/k$ is a purely inseparable extension or
$k$ and $k'$ are algebraic extensions of $\mathbf{F}_p$.
\end{enumerate}
\end{lemma}

\begin{proof}
Observe that each of the possibilities listed in (2) satisfies (1).
Thus we assume $k'/k$ satisfies (1) and we prove that we are in
one of the cases of (2). Discarding the case $k = k'$ we may assume
$k' \not = k$. It is clear that $k'/k$ is algebraic.
Hence we may assume that $k'/k$ is a nontrivial finite extension.
Let $k'/k'_{sep}/k$ be the separable subextension
found in Fields, Lemma \ref{fields-lemma-separable-first}.
We have to show that $k = k'_{sep}$ or that $k$ is an algebraic over
$\mathbf{F}_p$. Thus we may assume that $k'/k$
is a nontrivial finite separable extension and we have to show
$k$ is algebraic over $\mathbf{F}_p$.

\medskip\noindent
Pick $x \in k'$, $x \not \in k$. Pick $n, m > 0$ such that
$x^n \in k$ and $(x + 1)^m \in k$. Let $\overline{k}$ be an
algebraic closure of $k$. We can choose embeddings
$\sigma, \tau : k' \to \overline{k}$ with $\sigma(x) \not = \tau(x)$.
This follows from the discussion in
Fields, Section \ref{fields-section-separable-extensions}
(more precisely, after replacing $k'$ by the $k$-extension
generated by $x$ it follows from
Fields, Lemma \ref{fields-lemma-count-embeddings}).
Then we see that $\sigma(x) = \zeta \tau(x)$ for some
$n$th root of unity $\zeta$ in $\overline{k}$.
Similarly, we see that $\sigma(x + 1) = \zeta' \tau(x + 1)$
for some $m$th root of unity $\zeta' \in \overline{k}$.
Since $\sigma(x + 1) \not = \tau(x + 1)$ we see $\zeta' \not = 1$.
Then
$$
\zeta' (\tau(x) + 1) =
\zeta' \tau(x + 1) =
\sigma(x + 1) =
\sigma(x) + 1 =
\zeta \tau(x) + 1
$$
implies that
$$
\tau(x) (\zeta' - \zeta) = 1 - \zeta'
$$
hence $\zeta' \not = \zeta$ and
$$
\tau(x) = (1 - \zeta')/(\zeta' - \zeta)
$$
Hence every element of $k'$ which is not in $k$ is algebraic over the prime
subfield. Since $k'$ is generated over the prime subfield by the elements
of $k'$ which are not in $k$, we conclude that $k'$ (and hence $k$)
is algebraic over the prime subfield.

\medskip\noindent
Finally, if the characteristic of $k$ is $0$, the above leads to a
contradiction as follows (we encourage the reader to find their own proof).
For every rational number $y$ we similarly get a root of unity
$\zeta_y$ such that $\sigma(x + y) = \zeta_y\tau(x + y)$.
Then we find
$$
\zeta \tau(x) + y = \zeta_y(\tau(x) + y)
$$
and by our formula for $\tau(x)$ above we conclude
$\zeta_y \in \mathbf{Q}(\zeta, \zeta')$. Since the number field
$\mathbf{Q}(\zeta, \zeta')$ contains only a finite number of roots of
unity we find two distinct rational numbers $y, y'$ with
$\zeta_y = \zeta_{y'}$. Then we conclude that
$$
y - y' =
\sigma(x + y) - \sigma(x + y') =
\zeta_y(\tau(x + y)) - \zeta_{y'}\tau(x + y') = \zeta_y(y - y')
$$
which implies $\zeta_y = 1$ a contradiction.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-powers-field}
\begin{reference}
\cite[Lemme 3.1.6]{Alper-adequate}
\end{reference}
Soit $k'/k$ une extension de corps. Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item pour tout $x \in k'$, il existe un $n > 0$ tel que $x^n \in k$, et
\item $k' = k$, ou bien $k$ et $k'$ sont de caractéristique $p > 0$ et
soit $k'/k$ est une extension purement inséparable, soit
$k$ et $k'$ sont des extensions algébriques de $\mathbf{F}_p$.
\end{enumerate}
\end{lemma}

\begin{proof}
Remarquons que chacune des possibilités énumérées en (2) satisfait (1).
Supposons donc que $k'/k$ satisfasse (1), et montrons que l'un des cas de (2)
se produit. En écartant le cas $k = k'$, nous pouvons supposer que
$k' \not = k$. Il est clair que $k'/k$ est algébrique.
Nous pouvons donc supposer que $k'/k$ est une extension finie non triviale.
Soit $k'/k'_{sep}/k$ la sous-extension séparable
trouvée dans le lemme \ref{fields-lemma-separable-first} de Corps.
Nous devons montrer que $k = k'_{sep}$ ou que $k$ est algébrique sur
$\mathbf{F}_p$. Nous pouvons donc supposer que $k'/k$
est une extension finie séparable non triviale et nous devons montrer
que $k$ est algébrique sur $\mathbf{F}_p$.

\medskip\noindent
Choisissons $x \in k'$, $x \not \in k$. Choisissons $n, m > 0$ tels que
$x^n \in k$ et $(x + 1)^m \in k$. Soit $\overline{k}$ une clôture
algébrique de $k$. Nous pouvons choisir des plongements
$\sigma, \tau : k' \to \overline{k}$ tels que $\sigma(x) \not = \tau(x)$.
Cela résulte de la discussion de la
section \ref{fields-section-separable-extensions} de Corps
(plus précisément, après avoir remplacé $k'$ par l'extension de $k$
engendrée par $x$, cela résulte du
lemme \ref{fields-lemma-count-embeddings} de Corps).
Nous voyons alors que $\sigma(x) = \zeta \tau(x)$ pour une
racine $n$-ième de l'unité $\zeta$ dans $\overline{k}$.
De même, $\sigma(x + 1) = \zeta' \tau(x + 1)$
pour une racine $m$-ième de l'unité $\zeta' \in \overline{k}$.
Comme $\sigma(x + 1) \not = \tau(x + 1)$, nous voyons que $\zeta' \not = 1$.
Alors
$$
\zeta' (\tau(x) + 1) =
\zeta' \tau(x + 1) =
\sigma(x + 1) =
\sigma(x) + 1 =
\zeta \tau(x) + 1
$$
implique que
$$
\tau(x) (\zeta' - \zeta) = 1 - \zeta'
$$
d'où $\zeta' \not = \zeta$ et
$$
\tau(x) = (1 - \zeta')/(\zeta' - \zeta)
$$
Ainsi, tout élément de $k'$ qui n'appartient pas à $k$ est algébrique
sur le sous-corps premier. Comme $k'$ est engendré sur le sous-corps premier
par les éléments de $k'$ qui n'appartiennent pas à $k$, nous concluons que
$k'$ (et donc $k$) est algébrique sur le sous-corps premier.

\medskip\noindent
Enfin, si la caractéristique de $k$ est $0$, ce qui précède conduit à une
contradiction comme suit (nous encourageons le lecteur à trouver sa propre preuve).
Pour tout nombre rationnel $y$, nous obtenons de même une racine de l'unité
$\zeta_y$ telle que $\sigma(x + y) = \zeta_y\tau(x + y)$.
Nous trouvons alors
$$
\zeta \tau(x) + y = \zeta_y(\tau(x) + y)
$$
et, grâce à la formule ci-dessus pour $\tau(x)$, nous concluons que
$\zeta_y \in \mathbf{Q}(\zeta, \zeta')$. Comme le corps de nombres
$\mathbf{Q}(\zeta, \zeta')$ ne contient qu'un nombre fini de racines de
l'unité, il existe deux nombres rationnels distincts $y, y'$ tels que
$\zeta_y = \zeta_{y'}$. Nous concluons alors que
$$
y - y' =
\sigma(x + y) - \sigma(x + y') =
\zeta_y(\tau(x + y)) - \zeta_{y'}\tau(x + y') = \zeta_y(y - y')
$$
ce qui implique $\zeta_y = 1$, contradiction.
\end{proof}
```

</details>

### 04 — lemma-powers

Anglais L10717–10768 ; français L10673–10724.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10717) · FR-ALGEBRA-B15-CHOICE-0004.

Pour chaque élément, l'exposant peut varier. La surjectivité et l'injectivité sur les spectres sont démontrées séparément, puis les ouverts principaux donnent l'homéomorphisme. Pour les corps résiduels, les deux exposants n et m sont combinés en nm, exactement comme dans la source. Entière qualifie l'application, non la propriété d'être un anneau intègre.

Règles : FR-ALGEBRA-B15-RULE-HOMEO, FR-ALGEBRA-B15-RULE-INTEGRAL, FR-ALGEBRA-B15-RULE-PRIME, FR-ALGEBRA-B15-RULE-RESIDUE, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-powers}
Let $\varphi : R \to S$ be a ring map. If
\begin{enumerate}
\item for any $x \in S$ there exists $n > 0$ such that
$x^n$ is in the image of $\varphi$, and
\item $\Ker(\varphi)$ is locally nilpotent,
\end{enumerate}
then $\varphi$ induces a homeomorphism on spectra and induces residue
field extensions satisfying the equivalent conditions of
Lemma \ref{lemma-powers-field}.
\end{lemma}

\begin{proof}
Assume (1) and (2). Let $\mathfrak q, \mathfrak q'$ be primes of $S$
lying over the same prime ideal $\mathfrak p$ of $R$. Suppose $x \in S$ with
$x \in \mathfrak q$, $x \not \in \mathfrak q'$. Then $x^n \in \mathfrak q$
and $x^n \not \in \mathfrak q'$ for all $n > 0$. If $x^n = \varphi(y)$ with
$y \in R$ for some $n > 0$ then
$$
x^n \in \mathfrak q \Rightarrow y \in \mathfrak p \Rightarrow
x^n \in \mathfrak q'
$$
which is a contradiction. Hence there does not exist an $x$ as above and
we conclude that $\mathfrak q = \mathfrak q'$, i.e., the map on spectra
is injective. By assumption (2) the kernel $I = \Ker(\varphi)$ is
contained in every prime, hence $\Spec(R) = \Spec(R/I)$ as
topological spaces. As the induced map $R/I \to S$ is integral by
assumption (1)
Lemma \ref{lemma-integral-overring-surjective}
shows that $\Spec(S) \to \Spec(R/I)$ is surjective. Combining
the above we see that $\Spec(S) \to \Spec(R)$ is bijective.
If $x \in S$ is arbitrary, and we pick $y \in R$ such that
$\varphi(y) = x^n$ for some $n > 0$, then we see that the open
$D(x) \subset \Spec(S)$ corresponds to the open
$D(y) \subset \Spec(R)$ via the bijection above. Hence we see that
the map $\Spec(S) \to \Spec(R)$ is a homeomorphism.

\medskip\noindent
To see the statement on residue fields, let $\mathfrak q \subset S$
be a prime lying over a prime ideal $\mathfrak p \subset R$. Let
$x \in \kappa(\mathfrak q)$. If we think of $\kappa(\mathfrak q)$
as the residue field of the local ring $S_\mathfrak q$, then we
see that $x$ is the image of some $y/z \in S_\mathfrak q$
with $y \in S$, $z \in S$, $z \not \in \mathfrak q$.
Choose $n, m > 0$ such that $y^n, z^m$ are in the image of $\varphi$.
Then $x^{nm}$ is the residue of $(y/z)^{nm} = (y^n)^m/(z^m)^n$
which is in the image of $R_\mathfrak p \to S_\mathfrak q$.
Hence $x^{nm}$ is in the image of
$\kappa(\mathfrak p) \to \kappa(\mathfrak q)$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-powers}
Soit $\varphi : R \to S$ une application d'anneaux. Supposons que
\begin{enumerate}
\item pour tout $x \in S$, il existe $n > 0$ tel que
$x^n$ appartienne à l'image de $\varphi$, et
\item $\Ker(\varphi)$ soit localement nilpotent,
\end{enumerate}
alors $\varphi$ induit un homéomorphisme des spectres et induit des
extensions de corps résiduels satisfaisant aux conditions équivalentes du
Lemme \ref{lemma-powers-field}.
\end{lemma}

\begin{proof}
Supposons (1) et (2). Soient $\mathfrak q, \mathfrak q'$ des idéaux premiers
de $S$ au-dessus du même idéal premier $\mathfrak p$ de $R$. Supposons que
$x \in S$ vérifie $x \in \mathfrak q$, $x \not \in \mathfrak q'$. Alors
$x^n \in \mathfrak q$ et $x^n \not \in \mathfrak q'$ pour tout $n > 0$. Si
$x^n = \varphi(y)$ avec $y \in R$ pour un certain $n > 0$, alors
$$
x^n \in \mathfrak q \Rightarrow y \in \mathfrak p \Rightarrow
x^n \in \mathfrak q'
$$
ce qui est une contradiction. Il n'existe donc pas de $x$ comme ci-dessus,
et nous concluons que $\mathfrak q = \mathfrak q'$, c'est-à-dire que
l'application sur les spectres est injective. D'après (2), le noyau
$I = \Ker(\varphi)$ est contenu dans tout idéal premier, donc
$\Spec(R) = \Spec(R/I)$ comme espaces topologiques. Comme l'application
induite $R/I \to S$ est entière par (1), le
Lemme \ref{lemma-integral-overring-surjective} montre que
$\Spec(S) \to \Spec(R/I)$ est surjective. En combinant ce qui précède, nous
voyons que $\Spec(S) \to \Spec(R)$ est bijective.
Si $x \in S$ est quelconque et si nous choisissons $y \in R$ tel que
$\varphi(y) = x^n$ pour un certain $n > 0$, alors l'ouvert
$D(x) \subset \Spec(S)$ correspond à l'ouvert
$D(y) \subset \Spec(R)$ par la bijection ci-dessus. Ainsi
l'application $\Spec(S) \to \Spec(R)$ est un homéomorphisme.

\medskip\noindent
Pour l'assertion sur les corps résiduels, soit
$\mathfrak q \subset S$ un idéal premier au-dessus d'un idéal premier
$\mathfrak p \subset R$. Soit $x \in \kappa(\mathfrak q)$. Si nous considérons
$\kappa(\mathfrak q)$ comme le corps résiduel de l'anneau local
$S_\mathfrak q$, nous voyons que $x$ est l'image d'un certain
$y/z \in S_\mathfrak q$ avec $y \in S$, $z \in S$, $z \not \in \mathfrak q$.
Choisissons $n, m > 0$ tels que $y^n, z^m$ appartiennent à l'image de $\varphi$.
Alors $x^{nm}$ est le résidu de $(y/z)^{nm} = (y^n)^m/(z^m)^n$,
qui appartient à l'image de $R_\mathfrak p \to S_\mathfrak q$.
Ainsi $x^{nm}$ appartient à l'image de
$\kappa(\mathfrak p) \to \kappa(\mathfrak q)$.
\end{proof}
```

</details>

### 05 — lemma-2-3-ring-map

Anglais L10769–10812 ; français L10725–10770.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10769) · FR-ALGEBRA-B15-CHOICE-0005.

Les carrés et les cubes des générateurs appartiennent à l'image, sans hypothèse supplémentaire sur leur inversibilité. Le français conserve l'argument sur les résidus et celui qui distingue deux premiers au-dessus du même premier. La stabilité de (b) par changement de base est déduite de la surjectivité spectrale ; elle n'est pas affirmée pour un noyau arbitraire.

Règles : FR-ALGEBRA-B15-RULE-HOMEO, FR-ALGEBRA-B15-RULE-BASE, FR-ALGEBRA-B15-RULE-INTEGRAL, FR-ALGEBRA-B15-RULE-PRIME, FR-ALGEBRA-B15-RULE-RESIDUE, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-2-3-ring-map}
Let $\varphi : R \to S$ be a ring map. Assume
\begin{enumerate}
\item[(a)] $S$ is generated as an $R$-algebra by elements $x$ such
that $x^2, x^3 \in \varphi(R)$, and
\item[(b)] $\Ker(\varphi)$ is locally nilpotent,
\end{enumerate}
Then $\varphi$ induces isomorphisms on residue fields and
a homeomorphism of spectra. For any ring map $R \to R'$
the ring map $R' \to R' \otimes_R S$ also satisfies (a) and (b).
\end{lemma}

\begin{proof}
Assume (a) and (b). The map on spectra is closed as $S$ is integral
over $R$, see Lemmas \ref{lemma-going-up-closed} and
\ref{lemma-integral-going-up}. The image is dense by
Lemma \ref{lemma-image-dense-generic-points}. Thus $\Spec(S) \to \Spec(R)$
is surjective. If $\mathfrak q \subset S$ is a prime lying over
$\mathfrak p \subset R$ then the field extension
$\kappa(\mathfrak q)/\kappa(\mathfrak p)$ is generated by elements
$\alpha \in \kappa(\mathfrak q)$ whose square and cube are
in $\kappa(\mathfrak p)$. Thus clearly $\alpha \in \kappa(\mathfrak p)$
and we find that $\kappa(\mathfrak q) = \kappa(\mathfrak p)$.
If $\mathfrak q, \mathfrak q'$ were two distinct primes lying over
$\mathfrak p$, then at least one of the generators $x$ of $S$ as
in (a) would have distinct images in
$\kappa(\mathfrak q) = \kappa(\mathfrak p)$ and
$\kappa(\mathfrak q') = \kappa(\mathfrak p)$.
This would contradict the fact that both $x^2$ and $x^3$
do have the same image. This proves that $\Spec(S) \to \Spec(R)$
is injective hence a homeomorphism (by what was already shown).

\medskip\noindent
Since $\varphi$ induces a homeomorphism on spectra, it is in particular
surjective on spectra which is a property preserved under any base change, see
Lemma \ref{lemma-surjective-spec-radical-ideal}.
Therefore for any $R \to R'$ the kernel of the ring map
$R' \to R' \otimes_R S$ consists of nilpotent elements, see
Lemma \ref{lemma-image-dense-generic-points},
in other words (b) holds for $R' \to R' \otimes_R S$.
It is clear that (a) is preserved under base change.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-2-3-ring-map}
Soit $\varphi : R \to S$ une application d'anneaux. Supposons que
\begin{enumerate}
\item[(a)] $S$ soit engendrée comme $R$-algèbre par des éléments $x$ tels que
$x^2, x^3 \in \varphi(R)$, et
\item[(b)] $\Ker(\varphi)$ soit localement nilpotent,
\end{enumerate}
Alors $\varphi$ induit des isomorphismes sur les corps résiduels et
un homéomorphisme des spectres. Pour toute application d'anneaux $R \to R'$,
l'application $R' \to R' \otimes_R S$ satisfait également (a) et (b).
\end{lemma}

\begin{proof}
Supposons (a) et (b). L'application sur les spectres est fermée, car $S$ est
entière sur $R$, voir les Lemmes \ref{lemma-going-up-closed} et
\ref{lemma-integral-going-up}. L'image est dense d'après le
Lemme \ref{lemma-image-dense-generic-points}. Ainsi
$\Spec(S) \to \Spec(R)$ est surjective. Si
$\mathfrak q \subset S$ est un idéal premier au-dessus de
$\mathfrak p \subset R$, alors l'extension de corps
$\kappa(\mathfrak q)/\kappa(\mathfrak p)$ est engendrée par des éléments
$\alpha \in \kappa(\mathfrak q)$ dont le carré et le cube appartiennent à
$\kappa(\mathfrak p)$. Il est alors clair que
$\alpha \in \kappa(\mathfrak p)$ et nous obtenons
$\kappa(\mathfrak q) = \kappa(\mathfrak p)$.
Si $\mathfrak q, \mathfrak q'$ étaient deux idéaux premiers distincts
au-dessus de $\mathfrak p$, au moins l'un des générateurs $x$ de $S$ comme
dans (a) aurait des images distinctes dans
$\kappa(\mathfrak q) = \kappa(\mathfrak p)$ et
$\kappa(\mathfrak q') = \kappa(\mathfrak p)$.
Cela contredirait le fait que $x^2$ et $x^3$ ont bien la même image.
Cela montre que $\Spec(S) \to \Spec(R)$ est injective, donc un homéomorphisme
(d'après ce qui a déjà été démontré).

\medskip\noindent
Puisque $\varphi$ induit un homéomorphisme des spectres, elle est en particulier
surjective sur les spectres, propriété préservée par tout changement de base,
voir le Lemme \ref{lemma-surjective-spec-radical-ideal}.
Par conséquent, pour toute application $R \to R'$, le noyau de l'application
d'anneaux $R' \to R' \otimes_R S$ est constitué d'éléments nilpotents,
voir le Lemme \ref{lemma-image-dense-generic-points}; autrement dit, (b) est
satisfaite pour $R' \to R' \otimes_R S$.
Il est clair que (a) est préservée par changement de base.
\end{proof}
```

</details>

### 06 — lemma-help-with-powers

Anglais L10813–10846 ; français L10771–10805.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10813) · FR-ALGEBRA-B15-CHOICE-0006.

La valuation p-adique du nombre rationnel et la divisibilité du coefficient entier ne sont pas confondues. Les deux restes, les deux cas non nuls et le choix final de a sont conservés. La seule différence dans une formule de ce lot est divides rendu par divise dans le texte destiné au lecteur ; tous les symboles et indices sont identiques.

Règles : FR-ALGEBRA-B15-RULE-INTEGRAL, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-help-with-powers}
Let $p$ be a prime number. Let $n, m > 0$ be two integers. There exists
an integer $a$ such that
$(x + y)^{p^a}, p^a(x + y) \in \mathbf{Z}[x^{p^n}, p^nx, y^{p^m}, p^my]$.
\end{lemma}

\begin{proof}
This is clear for $p^a(x + y)$ as soon as $a \geq n, m$.
In fact, pick $a \gg n, m$. Write
$$
(x + y)^{p^a}  = \sum\nolimits_{i, j \geq 0, i + j = p^a}
{p^a \choose i, j} x^iy^j
$$
For every $i, j \geq 0$ with $i + j = p^a$ write
$i = q p^n + r$ with $r \in \{0, \ldots, p^n - 1\}$ and
$j = q' p^m + r'$ with $r' \in \{0, \ldots, p^m - 1\}$.
The condition $(x + y)^{p^a} \in \mathbf{Z}[x^{p^n}, p^nx, y^{p^m}, p^my]$
holds if
$$
p^{nr + mr'} \text{ divides } {p^a \choose i, j}
$$
If $r = r' = 0$ then the divisibility holds. If $r \not = 0$, then
we write
$$
{p^a \choose i, j} = \frac{p^a}{i} {p^a - 1 \choose i - 1, j}
$$
Since $r \not = 0$ the rational number $p^a/i$ has $p$-adic
valuation at least $a - (n - 1)$ (because $i$ is not divisible by $p^n$).
Thus ${p^a \choose i, j}$ is divisible by $p^{a - n + 1}$ in this case.
Similarly, we see that if $r' \not = 0$, then ${p^a \choose i, j}$ is
divisible by $p^{a - m + 1}$. Picking $a = np^n + mp^m + n + m$ will work.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-help-with-powers}
Soit $p$ un nombre premier. Soient $n, m > 0$ deux entiers. Il existe
un entier $a$ tel que
$(x + y)^{p^a}, p^a(x + y) \in \mathbf{Z}[x^{p^n}, p^nx, y^{p^m}, p^my]$.
\end{lemma}

\begin{proof}
C'est clair pour $p^a(x + y)$ dès que $a \geq n, m$.
En fait, choisissons $a \gg n, m$. Écrivons
$$
(x + y)^{p^a}  = \sum\nolimits_{i, j \geq 0, i + j = p^a}
{p^a \choose i, j} x^iy^j
$$
Pour tous $i, j \geq 0$ tels que $i + j = p^a$, écrivons
$i = q p^n + r$ avec $r \in \{0, \ldots, p^n - 1\}$ et
$j = q' p^m + r'$ avec $r' \in \{0, \ldots, p^m - 1\}$.
La condition $(x + y)^{p^a} \in \mathbf{Z}[x^{p^n}, p^nx, y^{p^m}, p^my]$
est satisfaite si
$$
p^{nr + mr'} \text{ divise } {p^a \choose i, j}
$$
Si $r = r' = 0$, la divisibilité est satisfaite. Si $r \not = 0$, nous
écrivons
$$
{p^a \choose i, j} = \frac{p^a}{i} {p^a - 1 \choose i - 1, j}
$$
Comme $r \not = 0$, le nombre rationnel $p^a/i$ a une valuation
$p$-adique au moins égale à $a - (n - 1)$ (car $i$ n'est pas divisible par
$p^n$). Ainsi ${p^a \choose i, j}$ est divisible par $p^{a - n + 1}$
dans ce cas. De même, si $r' \not = 0$, alors ${p^a \choose i, j}$ est
divisible par $p^{a - m + 1}$. Le choix
$a = np^n + mp^m + n + m$ convient.
\end{proof}
```

</details>

### 07 — lemma-p-ring-map-field

Anglais L10847–10866 ; français L10806–10825.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10847) · FR-ALGEBRA-B15-CHOICE-0007.

Le nombre premier p est fixé sans supposer d'emblée qu'il est la caractéristique. En caractéristique différente, p^n est inversible dans le corps et l'élément appartient déjà à k ; en caractéristique p, on obtient la pure inséparabilité. Le français conserve cette distinction et la génération comme extension de corps.

Règles : FR-ALGEBRA-B15-RULE-PURE, FR-ALGEBRA-B15-RULE-SEP, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-p-ring-map-field}
Let $k'/k$ be a field extension. Let $p$ be a prime number.
The following are equivalent
\begin{enumerate}
\item $k'$ is generated as a field extension of $k$ by elements
$x$ such that there exists an $n > 0$ with $x^{p^n} \in k$ and
$p^nx \in k$, and
\item $k = k'$ or the characteristic of $k$
and $k'$ is $p$ and $k'/k$ is purely inseparable.
\end{enumerate}
\end{lemma}

\begin{proof}
Let $x \in k'$. If there exists an $n > 0$ with $x^{p^n} \in k$ and
$p^nx \in k$ and if the characteristic is not $p$, then $x \in k$.
If the characteristic is $p$, then we find $x^{p^n} \in k$
and hence $x$ is purely inseparable over $k$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-p-ring-map-field}
Soit $k'/k$ une extension de corps. Soit $p$ un nombre premier.
Les assertions suivantes sont équivalentes
\begin{enumerate}
\item $k'$ est engendré comme extension de corps de $k$ par des éléments
$x$ tels qu'il existe un $n > 0$ avec $x^{p^n} \in k$ et
$p^nx \in k$, et
\item $k = k'$ ou bien la caractéristique de $k$ et de $k'$ est $p$
et $k'/k$ est purement inséparable.
\end{enumerate}
\end{lemma}

\begin{proof}
Soit $x \in k'$. S'il existe un $n > 0$ tel que $x^{p^n} \in k$ et
$p^nx \in k$ et si la caractéristique n'est pas $p$, alors $x \in k$.
Si la caractéristique est $p$, alors $x^{p^n} \in k$ et donc $x$ est
purement inséparable sur $k$.
\end{proof}
```

</details>

### 08 — lemma-p-ring-map

Anglais L10867–10911 ; français L10826–10872.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10867) · FR-ALGEBRA-B15-CHOICE-0008.

La sous-algèbre T est montrée stable par produits puis par sommes, avec des exposants adaptés. Le syntagme sous-algèbre sur R de l'algèbre ambiante est un peu long mais exact ; il n'est pas modifié pour fabriquer une correction. La fin traite séparément le noyau après changement de base et les générateurs des extensions résiduelles.

Règles : FR-ALGEBRA-B15-RULE-HOMEO, FR-ALGEBRA-B15-RULE-BASE, FR-ALGEBRA-B15-RULE-INTEGRAL, FR-ALGEBRA-B15-RULE-RESIDUE, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-p-ring-map}
Let $\varphi : R \to S$ be a ring map. Let $p$ be a prime number. Assume
\begin{enumerate}
\item[(a)] $S$ is generated as an $R$-algebra by elements $x$ such
that there exists an $n > 0$ with $x^{p^n} \in \varphi(R)$ and
$p^nx \in \varphi(R)$, and
\item[(b)] $\Ker(\varphi)$ is locally nilpotent,
\end{enumerate}
Then $\varphi$ induces a homeomorphism of spectra and induces
residue field extensions satisfying the equivalent conditions
of Lemma \ref{lemma-p-ring-map-field}. For any ring map $R \to R'$
the ring map $R' \to R' \otimes_R S$ also satisfies (a) and (b).
\end{lemma}

\begin{proof}
Assume (a) and (b). Note that (b) is equivalent to condition (2)
of Lemma \ref{lemma-powers}. Let $T \subset S$ be the set of
elements $x \in S$ such that there exists an
integer $n > 0$ such that $x^{p^n} , p^n x \in \varphi(R)$.
We claim that $T = S$. This will prove that condition (1) of
Lemma \ref{lemma-powers} holds and hence $\varphi$ induces
a homeomorphism on spectra.
By assumption (a) it suffices to show that $T \subset S$ is an $R$-sub algebra.
If $x \in T$ and $y \in R$, then it is clear that $yx \in T$.
Suppose $x, y \in T$ and $n, m > 0$ such that
$x^{p^n}, y^{p^m}, p^n x, p^m y \in \varphi(R)$.
Then $(xy)^{p^{n + m}}, p^{n + m}xy \in \varphi(R)$
hence $xy \in T$. We have $x + y \in T$ by Lemma \ref{lemma-help-with-powers}
and the claim is proved.

\medskip\noindent
Since $\varphi$ induces a homeomorphism on spectra, it is in particular
surjective on spectra which is a property preserved under any base change, see
Lemma \ref{lemma-surjective-spec-radical-ideal}.
Therefore for any $R \to R'$ the kernel of the ring map
$R' \to R' \otimes_R S$ consists of nilpotent elements, see
Lemma \ref{lemma-image-dense-generic-points},
in other words (b) holds for $R' \to R' \otimes_R S$.
It is clear that (a) is preserved under base change.
Finally, the condition on residue fields follows from (a)
as generators for $S$ as an $R$-algebra map to generators for
the residue field extensions.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-p-ring-map}
Soit $\varphi : R \to S$ une application d'anneaux. Soit $p$ un nombre
premier. Supposons
\begin{enumerate}
\item[(a)] que $S$ soit engendrée comme $R$-algèbre par des éléments $x$
tels qu'il existe un $n > 0$ avec $x^{p^n} \in \varphi(R)$ et
$p^nx \in \varphi(R)$, et
\item[(b)] que $\Ker(\varphi)$ soit localement nilpotent,
\end{enumerate}
Alors $\varphi$ induit un homéomorphisme des spectres et des extensions
de corps résiduels satisfaisant aux conditions équivalentes du
Lemme \ref{lemma-p-ring-map-field}. Pour toute application d'anneaux
$R \to R'$, l'application d'anneaux $R' \to R' \otimes_R S$ satisfait
également (a) et (b).
\end{lemma}

\begin{proof}
Supposons (a) et (b). Remarquons que (b) équivaut à la condition (2)
du Lemme \ref{lemma-powers}. Soit $T \subset S$ l'ensemble des
éléments $x \in S$ tels qu'il existe un entier
$n > 0$ tel que $x^{p^n} , p^n x \in \varphi(R)$.
Nous affirmons que $T = S$. Cela montrera que la condition (1) du
Lemme \ref{lemma-powers} est satisfaite et donc que $\varphi$ induit
un homéomorphisme sur les spectres.
Par (a), il suffit de montrer que $T \subset S$ est une sous-algèbre sur
$R$ de l'algèbre ambiante. Si $x \in T$ et $y \in R$, il est clair que $yx \in T$.
Supposons $x, y \in T$ et $n, m > 0$ tels que
$x^{p^n}, y^{p^m}, p^n x, p^m y \in \varphi(R)$.
Alors $(xy)^{p^{n + m}}, p^{n + m}xy \in \varphi(R)$,
d'où $xy \in T$. Nous avons $x + y \in T$ par le
Lemme \ref{lemma-help-with-powers}, ce qui prouve l'affirmation.

\medskip\noindent
Puisque $\varphi$ induit un homéomorphisme sur les spectres, elle est en
particulier surjective sur les spectres, propriété préservée par tout
changement de base, voir le Lemme \ref{lemma-surjective-spec-radical-ideal}.
Par conséquent, pour toute application $R \to R'$, le noyau de
l'application d'anneaux $R' \to R' \otimes_R S$ est constitué d'éléments
nilpotents, voir le Lemme \ref{lemma-image-dense-generic-points};
autrement dit, (b) est satisfaite pour $R' \to R' \otimes_R S$.
Il est clair que (a) est préservée par changement de base.
Enfin, la condition sur les corps résiduels découle de (a), car les
générateurs de $S$ comme $R$-algèbre donnent des générateurs des
extensions de corps résiduels.
\end{proof}
```

</details>

### 09 — lemma-radicial

Anglais L10912–10967 ; français L10873–10930.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10912) · FR-ALGEBRA-B15-CHOICE-0009.

Le caractère radiciel est ici exprimé par ses deux conditions, injectivité spectrale et pure inséparabilité résiduelle, sans ajouter le mot au texte. EGA IV confirme le registre radiciel et changement de base, mais les identifications du diagramme restent celles de Stacks. L'ordre des flèches, la composée et la seconde flèche, puis la conclusion pour la première sont conservés.

Règles : FR-ALGEBRA-B15-RULE-PURE, FR-ALGEBRA-B15-RULE-SEP, FR-ALGEBRA-B15-RULE-PRIME, FR-ALGEBRA-B15-RULE-RESIDUE, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-radicial}
Let $\varphi : R \to S$ be a ring map. Assume
\begin{enumerate}
\item $\varphi$ induces an injective map of spectra,
\item $\varphi$ induces purely inseparable residue field extensions.
\end{enumerate}
Then for any ring map $R \to R'$ properties (1) and (2) are true for
$R' \to R' \otimes_R S$.
\end{lemma}

\begin{proof}
Set $S' = R' \otimes_R S$ so that we have a commutative diagram
of continuous maps of spectra of rings
$$
\xymatrix{
\Spec(S') \ar[r] \ar[d] & \Spec(S) \ar[d] \\
\Spec(R') \ar[r] & \Spec(R)
}
$$
Let $\mathfrak p' \subset R'$ be a prime ideal lying over
$\mathfrak p \subset R$. If there is no prime ideal of $S$
lying over $\mathfrak p$, then there is no prime ideal of
$S'$ lying over $\mathfrak p'$. Otherwise, by
Remark \ref{remark-fundamental-diagram} there is a unique
prime ideal $\mathfrak r$ of $F = S \otimes_R \kappa(\mathfrak p)$
whose residue field is purely inseparable over $\kappa(\mathfrak p)$.
Consider the ring maps
$$
\kappa(\mathfrak p) \to F \to \kappa(\mathfrak r)
$$
By Lemma \ref{lemma-minimal-prime-reduced-ring} the ideal
$\mathfrak r \subset F$ is locally nilpotent, hence
we may apply Lemma \ref{lemma-surjective-locally-nilpotent-kernel}
to the ring map $F \to \kappa(\mathfrak r)$.
We may apply Lemma \ref{lemma-p-ring-map}
to the ring map $\kappa(\mathfrak p) \to \kappa(\mathfrak r)$.
Hence the composition and the second arrow in the maps
$$
\kappa(\mathfrak p') \to
\kappa(\mathfrak p') \otimes_{\kappa(\mathfrak p)} F \to
\kappa(\mathfrak p') \otimes_{\kappa(\mathfrak p)} \kappa(\mathfrak r)
$$
induces bijections on spectra and purely inseparable residue
field extensions. This implies the same thing for the first
map. Since
$$
\kappa(\mathfrak p') \otimes_{\kappa(\mathfrak p)} F =
\kappa(\mathfrak p') \otimes_{\kappa(\mathfrak p)}
\kappa(\mathfrak p) \otimes_R S =
\kappa(\mathfrak p') \otimes_R S =
\kappa(\mathfrak p') \otimes_{R'} R' \otimes_R S
$$
we conclude by the discussion in Remark \ref{remark-fundamental-diagram}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-radicial}
Soit $\varphi : R \to S$ une application d'anneaux. Supposons que
\begin{enumerate}
\item $\varphi$ induise une application injective sur les spectres,
\item $\varphi$ induise des extensions de corps résiduels purement
inséparables.
\end{enumerate}
Alors, pour toute application d'anneaux $R \to R'$, les propriétés (1) et
(2) sont vraies pour $R' \to R' \otimes_R S$.
\end{lemma}

\begin{proof}
Posons $S' = R' \otimes_R S$, de sorte que nous ayons un diagramme
commutatif d'applications continues de spectres d'anneaux
$$
\xymatrix{
\Spec(S') \ar[r] \ar[d] & \Spec(S) \ar[d] \\
\Spec(R') \ar[r] & \Spec(R)
}
$$
Soit $\mathfrak p' \subset R'$ un idéal premier au-dessus de
$\mathfrak p \subset R$. S'il n'existe aucun idéal premier de $S$
au-dessus de $\mathfrak p$, alors il n'existe aucun idéal premier de
$S'$ au-dessus de $\mathfrak p'$. Sinon, d'après la
Remarque \ref{remark-fundamental-diagram}, il existe un unique idéal
premier $\mathfrak r$ de $F = S \otimes_R \kappa(\mathfrak p)$ dont le
corps résiduel est une extension purement inséparable de
$\kappa(\mathfrak p)$. Considérons les applications d'anneaux
$$
\kappa(\mathfrak p) \to F \to \kappa(\mathfrak r)
$$
Par le Lemme \ref{lemma-minimal-prime-reduced-ring}, l'idéal
$\mathfrak r \subset F$ est localement nilpotent; nous pouvons donc
appliquer le Lemme \ref{lemma-surjective-locally-nilpotent-kernel}
à l'application d'anneaux $F \to \kappa(\mathfrak r)$.
Nous pouvons appliquer le Lemme \ref{lemma-p-ring-map}
à l'application $\kappa(\mathfrak p) \to \kappa(\mathfrak r)$.
Ainsi, la composée et la seconde flèche des applications
$$
\kappa(\mathfrak p') \to
\kappa(\mathfrak p') \otimes_{\kappa(\mathfrak p)} F \to
\kappa(\mathfrak p') \otimes_{\kappa(\mathfrak p)} \kappa(\mathfrak r)
$$
induisent des bijections sur les spectres et des extensions de corps
résiduels purement inséparables. Il en est donc de même pour la première
application. Comme
$$
\kappa(\mathfrak p') \otimes_{\kappa(\mathfrak p)} F =
\kappa(\mathfrak p') \otimes_{\kappa(\mathfrak p)}
\kappa(\mathfrak p) \otimes_R S =
\kappa(\mathfrak p') \otimes_R S =
\kappa(\mathfrak p') \otimes_{R'} R' \otimes_R S
$$
nous concluons par la discussion de la
Remarque \ref{remark-fundamental-diagram}.
\end{proof}
```

</details>

### 10 — lemma-radicial-integral

Anglais L10968–10987 ; français L10931–10952.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10968) · FR-ALGEBRA-B15-CHOICE-0010.

Homéomorphisme sur un sous-ensemble fermé n'est pas homéomorphisme sur tout le spectre. Le français préserve exactement cette restriction et les trois propriétés stables par changement de base. Entière garde son sens de morphisme entier.

Règles : FR-ALGEBRA-B15-RULE-HOMEO, FR-ALGEBRA-B15-RULE-BASE, FR-ALGEBRA-B15-RULE-PURE, FR-ALGEBRA-B15-RULE-SEP, FR-ALGEBRA-B15-RULE-INTEGRAL, FR-ALGEBRA-B15-RULE-RESIDUE, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-radicial-integral}
Let $\varphi : R \to S$ be a ring map. Assume
\begin{enumerate}
\item $\varphi$ is integral,
\item $\varphi$ induces an injective map of spectra,
\item $\varphi$ induces purely inseparable residue field extensions.
\end{enumerate}
Then $\varphi$ induces a homeomorphism from $\Spec(S)$ onto a closed
subset of $\Spec(R)$ and for any ring map
$R \to R'$ properties (1), (2), (3) are true for $R' \to R' \otimes_R S$.
\end{lemma}

\begin{proof}
The map on spectra is closed by
Lemmas \ref{lemma-going-up-closed} and \ref{lemma-integral-going-up}.
The properties are preserved under base change by
Lemmas \ref{lemma-radicial} and \ref{lemma-base-change-integral}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-radicial-integral}
Soit $\varphi : R \to S$ une application d'anneaux. Supposons que
\begin{enumerate}
\item $\varphi$ soit entière,
\item $\varphi$ induise une application injective sur les spectres,
\item $\varphi$ induise des extensions de corps résiduels purement
inséparables.
\end{enumerate}
Alors $\varphi$ induit un homéomorphisme de $\Spec(S)$ sur un sous-ensemble
fermé de $\Spec(R)$ et, pour toute application d'anneaux
$R \to R'$, les propriétés (1), (2), (3) sont vraies pour
$R' \to R' \otimes_R S$.
\end{lemma}

\begin{proof}
L'application sur les spectres est fermée par les
Lemmes \ref{lemma-going-up-closed} et \ref{lemma-integral-going-up}.
Les propriétés sont préservées par changement de base, par les
Lemmes \ref{lemma-radicial} et \ref{lemma-base-change-integral}.
\end{proof}
```

</details>

### 11 — lemma-radicial-integral-bijective

Anglais L10988–11004 ; français L10953–10971.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10988) · FR-ALGEBRA-B15-CHOICE-0011.

La bijectivité remplace ici l'injectivité du lemme précédent et donne un homéomorphisme sur le spectre entier. Les deux références et la preuve brève restent telles quelles. Le mauvais article anglais an devant bijective n'est pas reproduit comme faute française et n'autorise aucun changement mathématique.

Règles : FR-ALGEBRA-B15-RULE-HOMEO, FR-ALGEBRA-B15-RULE-PURE, FR-ALGEBRA-B15-RULE-SEP, FR-ALGEBRA-B15-RULE-INTEGRAL, FR-ALGEBRA-B15-RULE-RESIDUE, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-radicial-integral-bijective}
Let $\varphi : R \to S$ be a ring map. Assume
\begin{enumerate}
\item $\varphi$ is integral,
\item $\varphi$ induces an bijective map of spectra,
\item $\varphi$ induces purely inseparable residue field extensions.
\end{enumerate}
Then $\varphi$ induces a homeomorphism on spectra and for any ring map
$R \to R'$ properties (1), (2), (3) are true for $R' \to R' \otimes_R S$.
\end{lemma}

\begin{proof}
Follows from Lemmas \ref{lemma-radicial-integral} and
\ref{lemma-surjective-spec-radical-ideal}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-radicial-integral-bijective}
Soit $\varphi : R \to S$ une application d'anneaux. Supposons que
\begin{enumerate}
\item $\varphi$ soit entière,
\item $\varphi$ induise une application bijective sur les spectres,
\item $\varphi$ induise des extensions de corps résiduels purement
inséparables.
\end{enumerate}
Alors $\varphi$ induit un homéomorphisme sur les spectres et, pour toute
application d'anneaux $R \to R'$, les propriétés (1), (2), (3) sont vraies
pour $R' \to R' \otimes_R S$.
\end{lemma}

\begin{proof}
Cela résulte des Lemmes \ref{lemma-radicial-integral} et
\ref{lemma-surjective-spec-radical-ideal}.
\end{proof}
```

</details>

### 12 — lemma-universally-bijective

Anglais L11005–11072 ; français L10972–11029.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11005) · FR-ALGEBRA-B15-CHOICE-0012.

Les générateurs satisfont une condition sur un polynôme dont l'image est une puissance de T−x ; le texte ne suppose pas initialement R injecté dans S. La preuve commence par quotienter le noyau puis distingue les caractéristiques des corps résiduels. La phrase mx^{p^k}∈R est conservée littéralement ; le calcul affiché a lieu dans la fibre. Aucun remplacement de cette phrase par une nouvelle démonstration n'est incorporé.

Point particulier à relire : La portée de mx^{p^k}∈R mérite une lecture attentive puisque la comparaison affichée vient d'être faite après passage à une fibre. Ce lot ne produit ni contre-exemple ni admission d'erreur pour cette phrase. Elle reste inchangée ; l'observation ne doit pas être comptée comme un erratum établi.

Règles : FR-ALGEBRA-B15-RULE-HOMEO, FR-ALGEBRA-B15-RULE-BASE, FR-ALGEBRA-B15-RULE-PURE, FR-ALGEBRA-B15-RULE-SEP, FR-ALGEBRA-B15-RULE-INTEGRAL, FR-ALGEBRA-B15-RULE-PRIME, FR-ALGEBRA-B15-RULE-RESIDUE, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-universally-bijective}
Let $\varphi : R \to S$ be a ring map such that
\begin{enumerate}
\item the kernel of $\varphi$ is locally nilpotent, and
\item $S$ is generated as an $R$-algebra by elements $x$
such that there exist $n > 0$ and a polynomial $P(T) \in R[T]$
whose image in $S[T]$ is $(T - x)^n$.
\end{enumerate}
Then $\Spec(S) \to \Spec(R)$ is a homeomorphism and $R \to S$
induces purely inseparable extensions of residue fields.
Moreover, conditions (1) and (2) remain true on arbitrary base change.
\end{lemma}

\begin{proof}
We may replace $R$ by $R/\Ker(\varphi)$, see
Lemma \ref{lemma-surjective-locally-nilpotent-kernel}.
Assumption (2) implies $S$ is generated over $R$ by
elements which are integral over $R$.
Hence $R \subset S$ is integral
(Lemma \ref{lemma-integral-closure-is-ring}).
In particular $\Spec(S) \to \Spec(R)$ is surjective and closed
(Lemmas \ref{lemma-integral-overring-surjective},
\ref{lemma-going-up-closed}, and
\ref{lemma-integral-going-up}).

\medskip\noindent
Let $x \in S$ be one of the generators in (2), i.e., there exists an
$n > 0$ be such that $(T - x)^n \in R[T]$.
Let $\mathfrak p \subset R$ be a prime.
The $\kappa(\mathfrak p) \otimes_R S$ ring is nonzero by
the above and Lemma \ref{lemma-in-image}.
If the characteristic of $\kappa(\mathfrak p)$ is zero
then we see that $nx \in R$ implies $1 \otimes x$ is in the image
of $\kappa(\mathfrak p) \to \kappa(\mathfrak p) \otimes_R S$.
Hence $\kappa(\mathfrak p) \to \kappa(\mathfrak p) \otimes_R S$
is an isomorphism.
If the characteristic of $\kappa(\mathfrak p)$ is $p > 0$,
then write $n = p^k m$ with $m$ prime to $p$.
In $\kappa(\mathfrak p) \otimes_R S[T]$ we have
$$
(T - 1 \otimes x)^n = ((T - 1 \otimes x)^{p^k})^m =
(T^{p^k} - 1 \otimes x^{p^k})^m
$$
and we see that $mx^{p^k} \in R$. This implies that
$1 \otimes x^{p^k}$ is in the image of
$\kappa(\mathfrak p) \to \kappa(\mathfrak p) \otimes_R S$.
Hence Lemma \ref{lemma-p-ring-map} applies to
$\kappa(\mathfrak p) \to \kappa(\mathfrak p) \otimes_R S$.
In both cases we conclude that $\kappa(\mathfrak p) \otimes_R S$
has a unique prime ideal with residue field purely inseparable
over $\kappa(\mathfrak p)$. By Remark \ref{remark-fundamental-diagram}
we conclude that $\varphi$ is bijective on spectra.

\medskip\noindent
The statement on base change is immediate.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-universally-bijective}
Soit $\varphi : R \to S$ une application d'anneaux telle que
\begin{enumerate}
\item le noyau de $\varphi$ soit localement nilpotent, et
\item $S$ soit engendrée comme $R$-algèbre par des éléments $x$
tels qu'il existe un $n > 0$ et un polynôme $P(T) \in R[T]$
dont l'image dans $S[T]$ soit $(T - x)^n$.
\end{enumerate}
Alors $\Spec(S) \to \Spec(R)$ est un homéomorphisme et $R \to S$
induit des extensions de corps résiduels purement inséparables.
De plus, les conditions (1) et (2) restent vraies après tout changement
de base.
\end{lemma}

\begin{proof}
Nous pouvons remplacer $R$ par $R/\Ker(\varphi)$, voir le
Lemme \ref{lemma-surjective-locally-nilpotent-kernel}.
L'hypothèse (2) implique que $S$ est engendrée sur $R$ par des éléments
entiers sur $R$. Ainsi $R \subset S$ est une extension entière
(Lemme \ref{lemma-integral-closure-is-ring}).
En particulier, $\Spec(S) \to \Spec(R)$ est surjective et fermée
(Lemmes \ref{lemma-integral-overring-surjective},
\ref{lemma-going-up-closed} et \ref{lemma-integral-going-up}).

\medskip\noindent
Soit $x \in S$ l'un des générateurs de (2), c'est-à-dire qu'il existe un
$n > 0$ tel que $(T - x)^n \in R[T]$.
Soit $\mathfrak p \subset R$ un idéal premier.
L'anneau $\kappa(\mathfrak p) \otimes_R S$ est non nul d'après ce qui
précède et le Lemme \ref{lemma-in-image}.
Si la caractéristique de $\kappa(\mathfrak p)$ est nulle,
nous voyons que $nx \in R$ implique que $1 \otimes x$ appartient à l'image
de $\kappa(\mathfrak p) \to \kappa(\mathfrak p) \otimes_R S$.
Ainsi $\kappa(\mathfrak p) \to \kappa(\mathfrak p) \otimes_R S$
est un isomorphisme.
Si la caractéristique de $\kappa(\mathfrak p)$ est $p > 0$,
écrivons $n = p^k m$ avec $m$ premier à $p$.
Dans $\kappa(\mathfrak p) \otimes_R S[T]$, nous avons
$$
(T - 1 \otimes x)^n = ((T - 1 \otimes x)^{p^k})^m =
(T^{p^k} - 1 \otimes x^{p^k})^m
$$
et nous voyons que $mx^{p^k} \in R$. Cela implique que
$1 \otimes x^{p^k}$ appartient à l'image de
$\kappa(\mathfrak p) \to \kappa(\mathfrak p) \otimes_R S$.
Le Lemme \ref{lemma-p-ring-map} s'applique donc à
$\kappa(\mathfrak p) \to \kappa(\mathfrak p) \otimes_R S$.
Dans les deux cas, nous concluons que
$\kappa(\mathfrak p) \otimes_R S$ possède un unique idéal premier dont
le corps résiduel est une extension purement inséparable de
$\kappa(\mathfrak p)$. Par la Remarque \ref{remark-fundamental-diagram},
nous concluons que $\varphi$ est bijective sur les spectres.

\medskip\noindent
L'assertion sur le changement de base est immédiate.
\end{proof}
```

</details>

### 13 — section-algebras-over-fields

Anglais L11073–11081 ; français L11030–11038.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11073) · FR-ALGEBRA-B15-CHOICE-0013.

Géométriquement irréductible s'applique au spectre après toute extension du corps de base. EGA IV, 4.5.1–2, atteste l'expression et les critères par extension algébriquement close. Le français conserve ici la formulation algébrique avec un unique premier minimal, non une nouvelle définition par intégrité.

Règles : FR-ALGEBRA-B15-RULE-IRRED, FR-ALGEBRA-B15-RULE-PRIME, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Geometrically irreducible algebras}
\label{section-algebras-over-fields}

\noindent
An algebra $S$ over a field $k$ is geometrically irreducible if
the algebra $S \otimes_k k'$ has a unique minimal prime for
every field extension $k'/k$. In this section we develop a bit
of theory relevant to this notion.
```

Français restauré :
```tex
\section{Algèbres géométriquement irréductibles}
\label{section-algebras-over-fields}

\noindent
Une algèbre $S$ sur un corps $k$ est dite géométriquement irréductible si
l'algèbre $S \otimes_k k'$ possède un unique idéal premier minimal pour
toute extension de corps $k'/k$. Dans cette section, nous développons
quelques éléments de théorie pertinents pour cette notion.
```

</details>

### 14 — lemma-flat-fibres-irreducible

Anglais L11082–11104 ; français L11039–11061.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11082) · FR-ALGEBRA-B15-CHOICE-0014.

La famille dense concerne les idéaux premiers dont les fibres sont irréductibles. La formulation plus générale remplace exactement la paire platitude et présentation finie par ouverture ; elle ne supprime pas l'hypothèse d'irréductibilité de la base ni celle sur les fibres. Les deux références de la preuve sont conservées.

Règles : FR-ALGEBRA-B15-RULE-IRRED, FR-ALGEBRA-B15-RULE-PRIME, FR-ALGEBRA-B15-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-flat-fibres-irreducible}
Let $R \to S$ be a ring map. Assume
\begin{enumerate}
\item[(a)] $\Spec(R)$ is irreducible,
\item[(b)] $R \to S$ is flat,
\item[(c)] $R \to S$ is of finite presentation,
\item[(d)] the fibre rings $S \otimes_R \kappa(\mathfrak p)$
have irreducible spectra for a dense collection of primes $\mathfrak p$ of $R$.
\end{enumerate}
Then $\Spec(S)$ is irreducible.
This is true more generally with (b) $+$ (c)
replaced by ``the map $\Spec(S) \to \Spec(R)$ is open''.
\end{lemma}

\begin{proof}
The assumptions (b) and (c) imply that the map on spectra is open,
see
Proposition \ref{proposition-fppf-open}.
Hence the lemma follows from
Topology, Lemma \ref{topology-lemma-irreducible-on-top}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-flat-fibres-irreducible}
Soit $R \to S$ une application d'anneaux. Supposons que
\begin{enumerate}
\item[(a)] $\Spec(R)$ soit irréductible,
\item[(b)] $R \to S$ soit plate,
\item[(c)] $R \to S$ soit de présentation finie,
\item[(d)] les anneaux fibres $S \otimes_R \kappa(\mathfrak p)$ aient des
spectres irréductibles pour une famille dense d'idéaux premiers
$\mathfrak p$ de $R$.
\end{enumerate}
Alors $\Spec(S)$ est irréductible.
Cela reste vrai plus généralement si (b) $+$ (c) est remplacé par
« l'application $\Spec(S) \to \Spec(R)$ est ouverte ».
\end{lemma}

\begin{proof}
Les hypothèses (b) et (c) impliquent que l'application sur les spectres
est ouverte, voir la Proposition \ref{proposition-fppf-open}.
Le lemme résulte donc du
lemme \ref{topology-lemma-irreducible-on-top} de Topologie.
\end{proof}
```

</details>

### 15 — lemma-separably-closed-irreducible

Anglais L11105–11144 ; français L11062–11102.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11105) · FR-ALGEBRA-B15-CHOICE-0015.

Deux occurrences de domaines sont remplacées par anneaux intègres, conformément à Ducros 0.1.3. L'irréductibilité seule ne suffit pas à l'intégrité : on passe d'abord aux réductions. La phrase sur les diviseurs de zéro désigne maintenant explicitement cet anneau, et non son spectre. Le raisonnement par type fini, Nullstellensatz, densité des maximaux et ouverture garde toutes ses étapes.

Point particulier à relire : Deux calques lexicaux et un antécédent ambigu propres à la formulation française sont réparés. Cet anneau est R⊗_k S ; on ne dit pas qu'un espace topologique contient des diviseurs de zéro. Aucune hypothèse ni conclusion nouvelle.

Règles : FR-ALGEBRA-B15-RULE-SEP, FR-ALGEBRA-B15-RULE-DOMAIN, FR-ALGEBRA-B15-RULE-IRRED, FR-ALGEBRA-B15-RULE-PRIME, FR-ALGEBRA-B15-RULE-LOGIC, FR-ALGEBRA-B15-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-separably-closed-irreducible}
Let $k$ be a separably closed field.
Let $R$, $S$ be $k$-algebras. If $R$, $S$ have a unique
minimal prime, so does $R \otimes_k S$.
\end{lemma}

\begin{proof}
Let $k \subset \overline{k}$ be a perfect closure, see
Definition \ref{definition-perfection}.
By assumption $\overline{k}$ is algebraically closed.
The ring maps $R \to R \otimes_k \overline{k}$ and
$S \to S \otimes_k \overline{k}$ and
$R \otimes_k S \to (R \otimes_k S) \otimes_k \overline{k}
= (R \otimes_k \overline{k}) \otimes_{\overline{k}} (S \otimes_k \overline{k})$
satisfy the assumptions of Lemma \ref{lemma-p-ring-map}.
Hence we may assume $k$ is algebraically closed.

\medskip\noindent
We may replace $R$ and $S$ by their reductions.
Hence we may assume that $R$ and $S$ are domains.
By Lemma \ref{lemma-perfect-reduced} we see that $R \otimes_k S$ is
reduced. Hence its spectrum is reducible if and only if it contains a nonzero
zerodivisor. By Lemma \ref{lemma-limit-argument} we reduce to the case where
$R$ and $S$ are domains of finite type over $k$ algebraically closed.

\medskip\noindent
Note that the ring map $R \to R \otimes_k S$ is of finite
presentation and flat. Moreover, for every maximal ideal
$\mathfrak m$ of $R$ we have
$(R \otimes_k S) \otimes_R R/\mathfrak m \cong S$ because
$k \cong R/\mathfrak m$ by the Hilbert Nullstellensatz Theorem
\ref{theorem-nullstellensatz}. Moreover, the set of
maximal ideals is dense in the spectrum of $R$ since
$\Spec(R)$ is Jacobson, see Lemma \ref{lemma-finite-type-field-Jacobson}.
Hence we see that Lemma \ref{lemma-flat-fibres-irreducible} applies
to the ring map $R \to R \otimes_k S$ and we conclude that
the spectrum of $R \otimes_k S$ is irreducible as desired.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-separably-closed-irreducible}
Soit $k$ un corps séparablement clos.
Soient $R$ et $S$ des $k$-algèbres. Si $R$ et $S$ possèdent un unique
idéal premier minimal, il en est de même pour $R \otimes_k S$.
\end{lemma}

\begin{proof}
Soit $k \subset \overline{k}$ une clôture parfaite, voir la
Définition \ref{definition-perfection}.
D'après l'hypothèse, $\overline{k}$ est algébriquement clos.
Les applications d'anneaux $R \to R \otimes_k \overline{k}$ et
$S \to S \otimes_k \overline{k}$ ainsi que
$R \otimes_k S \to (R \otimes_k S) \otimes_k \overline{k}
= (R \otimes_k \overline{k}) \otimes_{\overline{k}} (S \otimes_k \overline{k})$
satisfont aux hypothèses du Lemme \ref{lemma-p-ring-map}.
Nous pouvons donc supposer que $k$ est algébriquement clos.

\medskip\noindent
Nous pouvons remplacer $R$ et $S$ par leurs réductions.
Nous pouvons donc supposer que $R$ et $S$ sont des anneaux intègres.
Par le Lemme \ref{lemma-perfect-reduced}, $R \otimes_k S$ est réduit.
Son spectre est donc réductible si et seulement si cet anneau contient un diviseur
de zéro non nul. Par le Lemme \ref{lemma-limit-argument}, nous nous
ramenons au cas où $R$ et $S$ sont des anneaux intègres de type fini sur le corps
$k$ algébriquement clos.

\medskip\noindent
Remarquons que l'application d'anneaux $R \to R \otimes_k S$ est de
présentation finie et plate. De plus, pour tout idéal maximal
$\mathfrak m$ de $R$, nous avons
$(R \otimes_k S) \otimes_R R/\mathfrak m \cong S$ car
$k \cong R/\mathfrak m$ par le théorème des zéros de Hilbert,
Théorème \ref{theorem-nullstellensatz}. En outre, l'ensemble des idéaux
maximaux est dense dans le spectre de $R$ puisque $\Spec(R)$ est un
espace de Jacobson, voir le Lemme \ref{lemma-finite-type-field-Jacobson}.
Le Lemme \ref{lemma-flat-fibres-irreducible} s'applique donc à
l'application $R \to R \otimes_k S$, et nous concluons que le spectre de
$R \otimes_k S$ est irréductible, comme voulu.
\end{proof}
```

</details>

### 16 — lemma-geometrically-irreducible

Anglais L11145–11205 ; français L11103–11164.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11145) · FR-ALGEBRA-B15-CHOICE-0016.

Les quatre critères gardent leur ordre : extension quelconque, finie séparable, clôture séparable, clôture algébrique. La descente des premiers minimaux utilise la platitude ; le changement purement inséparable utilise un homéomorphisme. Le corps commun F est lu comme une extension compatible de k, sans ajouter une assertion de canonicité. Chaque sens de la preuve est conservé.

Règles : FR-ALGEBRA-B15-RULE-HOMEO, FR-ALGEBRA-B15-RULE-PURE, FR-ALGEBRA-B15-RULE-SEP, FR-ALGEBRA-B15-RULE-IRRED, FR-ALGEBRA-B15-RULE-PRIME, FR-ALGEBRA-B15-RULE-LOGIC, FR-ALGEBRA-B15-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-geometrically-irreducible}
Let $k$ be a field.
Let $R$ be a $k$-algebra.
The following are equivalent
\begin{enumerate}
\item for every field extension $k'/k$ the
spectrum of $R \otimes_k k'$ is irreducible,
\item for every finite separable field extension $k'/k$ the
spectrum of $R \otimes_k k'$ is irreducible,
\item the spectrum of $R \otimes_k \overline{k}$ is irreducible
where $\overline{k}$ is the separable algebraic closure of $k$, and
\item the spectrum of $R \otimes_k \overline{k}$ is irreducible
where $\overline{k}$ is the algebraic closure of $k$.
\end{enumerate}
\end{lemma}

\begin{proof}
It is clear that (1) implies (2).

\medskip\noindent
Assume (2) and let $\overline{k}$ is the separable algebraic closure of $k$.
Suppose $\mathfrak q_i \subset R \otimes_k \overline{k}$, $i = 1, 2$
are two minimal prime ideals. For every finite subextension
$\overline{k}/k'/k$ the extension $k'/k$ is separable and
the ring map $R \otimes_k k' \to R \otimes_k \overline{k}$
is flat. Hence $\mathfrak p_i = (R \otimes_k k') \cap \mathfrak q_i$
are minimal prime ideals (as we have going down for flat ring maps
by Lemma \ref{lemma-flat-going-down}). Thus we see that
$\mathfrak p_1 = \mathfrak p_2$
by assumption (2). Since $\overline{k} = \bigcup k'$ we conclude
$\mathfrak q_1 = \mathfrak q_2$. Hence $\Spec(R \otimes_k \overline{k})$
is irreducible.

\medskip\noindent
Assume (3) and let $\overline{k}$ be the algebraic closure of $k$.
Let $\overline{k}/\overline{k}'/k$ be the corresponding
separable algebraic closure of $k$. Then $\overline{k}/\overline{k}'$
is purely inseparable (in positive characteristic) or trivial.
Hence $R \otimes_k \overline{k}' \to R \otimes_k \overline{k}$
induces a homeomorphism on spectra, for example by
Lemma \ref{lemma-p-ring-map}. Thus we have (4).

\medskip\noindent
Assume (4). Let $k'/k$ be an arbitrary field extension and let
$\overline{k}$ be the algebraic closure of $k$. We may choose a
field $F$ such that both $k'$ and $\overline{k}$ are isomorphic
to subfields of $F$. Then
$$
R \otimes_k F = (R \otimes_k \overline{k}) \otimes_{\overline{k}} F
$$
and hence we see from Lemma \ref{lemma-separably-closed-irreducible}
that $R \otimes_k F$ has a unique minimal prime. Finally, the
ring map $R \otimes_k k' \to R \otimes_k F$ is flat and injective
and hence any minimal prime of $R \otimes_k k'$ is the image of
a minimal prime of $R \otimes_k F$ (by
Lemma \ref{lemma-injective-minimal-primes-in-image}
and going down). We conclude that there is only one
such minimal prime and the proof is complete.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-geometrically-irreducible}
Soit $k$ un corps.
Soit $R$ une $k$-algèbre.
Les assertions suivantes sont équivalentes
\begin{enumerate}
\item pour toute extension de corps $k'/k$, le spectre de
$R \otimes_k k'$ est irréductible,
\item pour toute extension de corps finie et séparable $k'/k$, le spectre de
$R \otimes_k k'$ est irréductible,
\item le spectre de $R \otimes_k \overline{k}$ est irréductible,
où $\overline{k}$ est la clôture algébrique séparable de $k$, et
\item le spectre de $R \otimes_k \overline{k}$ est irréductible,
où $\overline{k}$ est la clôture algébrique de $k$.
\end{enumerate}
\end{lemma}

\begin{proof}
Il est clair que (1) implique (2).

\medskip\noindent
Supposons (2) et soit $\overline{k}$ la clôture algébrique séparable de $k$.
Supposons que $\mathfrak q_i \subset R \otimes_k \overline{k}$, $i = 1, 2$,
soient deux idéaux premiers minimaux. Pour toute sous-extension finie
$\overline{k}/k'/k$, l'extension $k'/k$ est séparable et l'application
$R \otimes_k k' \to R \otimes_k \overline{k}$ est plate.
Ainsi $\mathfrak p_i = (R \otimes_k k') \cap \mathfrak q_i$ sont des
idéaux premiers minimaux (car nous avons la descente des idéaux premiers
pour les applications d'anneaux plates, par le
Lemme \ref{lemma-flat-going-down}). Nous avons donc
$\mathfrak p_1 = \mathfrak p_2$ par (2). Comme
$\overline{k} = \bigcup k'$, nous concluons que
$\mathfrak q_1 = \mathfrak q_2$. Ainsi $\Spec(R \otimes_k \overline{k})$
est irréductible.

\medskip\noindent
Supposons (3) et soit $\overline{k}$ la clôture algébrique de $k$.
Soit $\overline{k}/\overline{k}'/k$ la clôture algébrique séparable
correspondante de $k$. Alors $\overline{k}/\overline{k}'$ est purement
inséparable (en caractéristique positive) ou triviale.
Ainsi $R \otimes_k \overline{k}' \to R \otimes_k \overline{k}$
induit un homéomorphisme sur les spectres, par exemple par le
Lemme \ref{lemma-p-ring-map}. Nous obtenons donc (4).

\medskip\noindent
Supposons (4). Soit $k'/k$ une extension de corps quelconque et soit
$\overline{k}$ la clôture algébrique de $k$. Choisissons un corps $F$
tel que $k'$ et $\overline{k}$ soient tous deux isomorphes à des
sous-corps de $F$. Alors
$$
R \otimes_k F = (R \otimes_k \overline{k}) \otimes_{\overline{k}} F
$$
et, par le Lemme \ref{lemma-separably-closed-irreducible},
$R \otimes_k F$ possède un unique idéal premier minimal.
Enfin, l'application d'anneaux $R \otimes_k k' \to R \otimes_k F$ est
plate et injective, et tout idéal premier minimal de $R \otimes_k k'$ est
donc l'image d'un idéal premier minimal de $R \otimes_k F$ (par le
Lemme \ref{lemma-injective-minimal-primes-in-image} et la descente).
Nous concluons qu'il n'existe qu'un seul idéal premier minimal, ce qui
achève la démonstration.
\end{proof}
```

</details>

### 17 — definition-geometrically-irreducible

Anglais L11206–11219 ; français L11165–11178.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11206) · FR-ALGEBRA-B15-CHOICE-0017.

Le quantificateur toute extension est maintenu. La note indiquant qu'un espace irréductible est non vide est indispensable et conservée ; une simple absence de deux composantes ne suffit pas dans le cas vide. Le critère par les extensions finies séparables reste une conséquence, pas la définition remplaçante.

Règles : FR-ALGEBRA-B15-RULE-SEP, FR-ALGEBRA-B15-RULE-IRRED, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-geometrically-irreducible}
Let $k$ be a field.
Let $S$ be a $k$-algebra.
We say $S$ is {\it geometrically irreducible over $k$}
if for every field extension $k'/k$ the spectrum of
$S \otimes_k k'$ is irreducible\footnote{An irreducible space is nonempty.}.
\end{definition}

\noindent
By Lemma \ref{lemma-geometrically-irreducible} it suffices
to check this for finite separable field extensions $k'/k$
or for $k'$ equal to the separable algebraic closure of $k$.
```

Français restauré :
```tex
\begin{definition}
\label{definition-geometrically-irreducible}
Soit $k$ un corps.
Soit $S$ une $k$-algèbre.
Nous disons que $S$ est {\it géométriquement irréductible sur $k$}
si, pour toute extension de corps $k'/k$, le spectre de
$S \otimes_k k'$ est irréductible\footnote{Un espace irréductible est non vide.}.
\end{definition}

\noindent
Par le Lemme \ref{lemma-geometrically-irreducible}, il suffit de vérifier
cette propriété pour les extensions de corps finies et séparables $k'/k$
ou pour $k'$ égal à la clôture algébrique séparable de $k$.
```

</details>

### 18 — lemma-separably-closed-irreducible-implies-geometric

Anglais L11220–11233 ; français L11179–11192.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11220) · FR-ALGEBRA-B15-CHOICE-0018.

La clôture séparable, non nécessairement la clôture algébrique, est l'hypothèse. La formulation séparablement algébriquement clos est peu légère mais source-fidèle et comprise comme séparablement clos, attesté chez Dat. L'équivalence et le renvoi suivant la définition sont conservés.

Point particulier à relire : La formulation source est conservée. Une simplification stylistique possible n'est pas une erreur démontrée.

Règles : FR-ALGEBRA-B15-RULE-SEP, FR-ALGEBRA-B15-RULE-IRRED, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-separably-closed-irreducible-implies-geometric}
Let $k$ be a field.
Let $R$ be a $k$-algebra.
If $k$ is separably algebraically closed then $R$ is
geometrically irreducible over $k$ if and only if the
spectrum of $R$ is irreducible.
\end{lemma}

\begin{proof}
Immediate from the remark following
Definition \ref{definition-geometrically-irreducible}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-separably-closed-irreducible-implies-geometric}
Soit $k$ un corps.
Soit $R$ une $k$-algèbre.
Si $k$ est séparablement algébriquement clos, alors $R$ est
géométriquement irréductible sur $k$ si et seulement si le spectre de
$R$ est irréductible.
\end{lemma}

\begin{proof}
Cela résulte immédiatement de la remarque qui suit la
Définition \ref{definition-geometrically-irreducible}.
\end{proof}
```

</details>

### 19 — lemma-subalgebra-geometrically-irreducible

Anglais L11234–11255 ; français L11193–11215.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11234) · FR-ALGEBRA-B15-CHOICE-0019.

Les trois assertions portent respectivement sur une sous-algèbre, toutes les sous-algèbres de type fini, puis une colimite filtrante. Le français énonce bien la conclusion de la première assertion : l'est également. La preuve par injection et image irréductible, puis commutation du produit tensoriel aux colimites, reste entière.

Règles : FR-ALGEBRA-B15-RULE-IRRED, FR-ALGEBRA-B15-RULE-TENSOR, FR-ALGEBRA-B15-RULE-LOGIC, FR-ALGEBRA-B15-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-subalgebra-geometrically-irreducible}
Let $k$ be a field. Let $S$ be a $k$-algebra.
\begin{enumerate}
\item If $S$ is geometrically irreducible over $k$ so is every
$k$-subalgebra.
\item If all finitely generated $k$-subalgebras of $S$ are
geometrically irreducible, then $S$ is geometrically irreducible.
\item A directed colimit of geometrically irreducible $k$-algebras
is geometrically irreducible.
\end{enumerate}
\end{lemma}

\begin{proof}
Let $S' \subset S$ be a subalgebra. Then for any extension $k'/k$
the ring map $S' \otimes_k k' \to S \otimes_k k'$ is injective also.
Hence (1) follows from Lemma \ref{lemma-injective-minimal-primes-in-image}
(and the fact that the image of an irreducible space under a continuous
map is irreducible). The second and third property follow from the fact
that tensor product commutes with colimits.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-subalgebra-geometrically-irreducible}
Soit $k$ un corps. Soit $S$ une $k$-algèbre.
\begin{enumerate}
\item Si $S$ est géométriquement irréductible sur $k$, toute
$k$-sous-algèbre l'est également.
\item Si toutes les $k$-sous-algèbres de type fini de $S$ sont
géométriquement irréductibles, alors $S$ est géométriquement irréductible.
\item Une colimite filtrante de $k$-algèbres géométriquement
irréductibles est géométriquement irréductible.
\end{enumerate}
\end{lemma}

\begin{proof}
Soit $S' \subset S$ une sous-algèbre. Alors, pour toute extension $k'/k$,
l'application d'anneaux $S' \otimes_k k' \to S \otimes_k k'$ est également
injective. Ainsi (1) résulte du
Lemme \ref{lemma-injective-minimal-primes-in-image}
(et du fait que l'image d'un espace irréductible par une application
continue est irréductible). Les deuxième et troisième assertions résultent
du fait que le produit tensoriel commute aux colimites.
\end{proof}
```

</details>

### 20 — lemma-geometrically-irreducible-any-base-change

Anglais L11256–11295 ; français L11216–11255.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11256) · FR-ALGEBRA-B15-CHOICE-0020.

La bijection concerne les composantes irréductibles, et non tous les points. Le corps de base est fixe, R est quelconque. Premiers minimaux, platitude, passage au quotient puis au corps résiduel sont conservés ; le mot minimal entre parenthèses a la même portée que dans la source.

Règles : FR-ALGEBRA-B15-RULE-IRRED, FR-ALGEBRA-B15-RULE-PRIME, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-geometrically-irreducible-any-base-change}
Let $k$ be a field.
Let $S$ be a geometrically irreducible $k$-algebra.
Let $R$ be any $k$-algebra.
The map
$$
\Spec(R \otimes_k S) \longrightarrow \Spec(R)
$$
induces a bijection on irreducible components.
\end{lemma}

\begin{proof}
Recall that irreducible components correspond to minimal primes
(Lemma \ref{lemma-irreducible}).
As $R \to R \otimes_k S$ is flat we see by going down
(Lemma \ref{lemma-flat-going-down}) that
any minimal prime of $R \otimes_k S$ lies over a minimal prime of $R$.
Conversely, if $\mathfrak p \subset R$ is a (minimal) prime then
$$
R \otimes_k S/\mathfrak p(R \otimes_k S)
=
(R/\mathfrak p) \otimes_k S
\subset
\kappa(\mathfrak p) \otimes_k S
$$
by flatness of $R \to R \otimes_k S$. The ring
$\kappa(\mathfrak p) \otimes_k S$ has irreducible spectrum
by assumption. It follows that
$R \otimes_k S/\mathfrak p(R \otimes_k S)$ has a single minimal
prime (Lemma \ref{lemma-injective-minimal-primes-in-image}).
In other words, the inverse image of the irreducible set
$V(\mathfrak p)$ is irreducible.
Hence the lemma follows.
\end{proof}

\noindent
Let us make some remarks on the notion of geometrically irreducible
field extensions.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-geometrically-irreducible-any-base-change}
Soit $k$ un corps.
Soit $S$ une $k$-algèbre géométriquement irréductible.
Soit $R$ une $k$-algèbre quelconque.
L'application
$$
\Spec(R \otimes_k S) \longrightarrow \Spec(R)
$$
induit une bijection sur les composantes irréductibles.
\end{lemma}

\begin{proof}
Rappelons que les composantes irréductibles correspondent aux idéaux
premiers minimaux (Lemme \ref{lemma-irreducible}).
Comme $R \to R \otimes_k S$ est plate, la descente montre
(Lemme \ref{lemma-flat-going-down}) que tout idéal premier minimal de
$R \otimes_k S$ est au-dessus d'un idéal premier minimal de $R$.
Réciproquement, si $\mathfrak p \subset R$ est un idéal premier
(minimal), alors
$$
R \otimes_k S/\mathfrak p(R \otimes_k S)
=
(R/\mathfrak p) \otimes_k S
\subset
\kappa(\mathfrak p) \otimes_k S
$$
par platitude de $R \to R \otimes_k S$. L'anneau
$\kappa(\mathfrak p) \otimes_k S$ a un spectre irréductible
par hypothèse. Il s'ensuit que
$R \otimes_k S/\mathfrak p(R \otimes_k S)$ possède un unique idéal
premier minimal (Lemme \ref{lemma-injective-minimal-primes-in-image}).
Autrement dit, l'image inverse de l'ensemble irréductible $V(\mathfrak p)$
est irréductible. Le lemme en résulte.
\end{proof}

\noindent
Faisons maintenant quelques remarques sur la notion d'extensions de corps
géométriquement irréductibles.
```

</details>

### 21 — lemma-field-extension-geometrically-irreducible

Anglais L11296–11321 ; français L11256–11279.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11296) · FR-ALGEBRA-B15-CHOICE-0021.

Algébriquement clos dans K est une propriété relative : elle ne dit pas que k est algébriquement clos absolument. L'argument conserve l'élément primitif et la factorisation du polynôme minimal. Le choix usuel de facteurs unitaires est implicite dans la source ; on ne l'insère pas comme une nouvelle hypothèse du lemme.

Point particulier à relire : La normalisation des facteurs est implicite ; pas d'affirmation d'un nouvel erratum ni d'insertion dans la traduction.

Règles : FR-ALGEBRA-B15-RULE-SEP, FR-ALGEBRA-B15-RULE-IRRED, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-field-extension-geometrically-irreducible}
Let $K/k$ be a field extension. If $k$ is algebraically closed in $K$, then
$K$ is geometrically irreducible over $k$.
\end{lemma}

\begin{proof}
Assume $k$ is algebraically closed in $K$. By
Definition \ref{definition-geometrically-irreducible}
and Lemma \ref{lemma-geometrically-irreducible} it suffices to show
that the spectrum of $K \otimes_k k'$ is irreducible for every
finite separable extension $k'/k$. Say $k'$ is generated by $\alpha \in k'$
over $k$, see
Fields, Lemma \ref{fields-lemma-primitive-element}. Let
$P = T^d + a_1 T^{d - 1} + \ldots + a_d \in k[T]$ be the minimal
polynomial of $\alpha$. Then $K \otimes_k k' \cong K[T]/(P)$.
The only way the spectrum of $K[T]/(P)$ can be reducible
is if $P$ is reducible in $K[T]$. Assume $P = P_1 P_2$ is a nontrivial
factorization in $K[T]$ to get a contradiction.
By Lemma \ref{lemma-polynomials-divide} we see that
the coefficients of $P_1$ and $P_2$ are algebraic over $k$.
Our assumption implies the coefficients of $P_1$ and $P_2$
are in $k$ which contradicts the fact that $P$ is irreducible
over $k$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-field-extension-geometrically-irreducible}
Soit $K/k$ une extension de corps. Si $k$ est algébriquement clos dans $K$,
alors $K$ est géométriquement irréductible sur $k$.
\end{lemma}

\begin{proof}
Supposons que $k$ soit algébriquement clos dans $K$. Par la
Définition \ref{definition-geometrically-irreducible} et le
Lemme \ref{lemma-geometrically-irreducible}, il suffit de montrer que le
spectre de $K \otimes_k k'$ est irréductible pour toute extension séparable
finie $k'/k$. Disons que $k'$ est engendré par $\alpha \in k'$ sur $k$, voir
le lemme \ref{fields-lemma-primitive-element} de Corps. Soit
$P = T^d + a_1 T^{d - 1} + \ldots + a_d \in k[T]$ le polynôme minimal
de $\alpha$. Alors $K \otimes_k k' \cong K[T]/(P)$.
La seule façon pour que le spectre de $K[T]/(P)$ soit réductible est que
$P$ soit réductible dans $K[T]$. Supposons donc que $P = P_1 P_2$ soit une
factorisation non triviale dans $K[T]$, afin d'obtenir une contradiction.
Par le Lemme \ref{lemma-polynomials-divide}, les coefficients de $P_1$ et
$P_2$ sont algébriques sur $k$. Notre hypothèse implique que les
coefficients de $P_1$ et $P_2$ appartiennent à $k$, ce qui contredit le fait
que $P$ soit irréductible sur $k$.
\end{proof}
```

</details>

### 22 — lemma-geometrically-irreducible-transitive

Anglais L11322–11339 ; français L11280–11297.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11322) · FR-ALGEBRA-B15-CHOICE-0022.

La première extension K/k est géométriquement irréductible et S l'est comme K-algèbre ; la conclusion est relative à k. La finitude et la séparabilité de K′ concernent K′/K, sans transformer l'extension initiale K/k en extension finie. Les anneaux de base des produits tensoriels restent identiques.

Règles : FR-ALGEBRA-B15-RULE-SEP, FR-ALGEBRA-B15-RULE-IRRED, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-geometrically-irreducible-transitive}
Let $K/k$ be a geometrically irreducible field extension.
Let $S$ be a geometrically irreducible $K$-algebra.
Then $S$ is geometrically irreducible over $k$.
\end{lemma}

\begin{proof}
By Definition \ref{definition-geometrically-irreducible}
and Lemma \ref{lemma-geometrically-irreducible} it suffices to show
that the spectrum of $S \otimes_k k'$ is irreducible for every
finite separable extension $k'/k$. Since $K$ is geometrically irreducible
over $k$ we see that $K' = K \otimes_k k'$
is a finite, separable field extension of $K$.
Hence the spectrum of $S \otimes_k k' = S \otimes_K K'$ is
irreducible as $S$ is assumed geometrically irreducible over $K$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-geometrically-irreducible-transitive}
Soit $K/k$ une extension de corps géométriquement irréductible.
Soit $S$ une $K$-algèbre géométriquement irréductible.
Alors $S$ est géométriquement irréductible sur $k$.
\end{lemma}

\begin{proof}
Par la Définition \ref{definition-geometrically-irreducible} et le
Lemme \ref{lemma-geometrically-irreducible}, il suffit de montrer que le
spectre de $S \otimes_k k'$ est irréductible pour toute extension séparable
finie $k'/k$. Comme $K$ est géométriquement irréductible sur $k$, nous
voyons que $K' = K \otimes_k k'$ est une extension de corps finie et
séparable de $K$. Par conséquent, le spectre de
$S \otimes_k k' = S \otimes_K K'$ est irréductible, puisque $S$ est,
par hypothèse, géométriquement irréductible sur $K$.
\end{proof}
```

</details>

### 23 — lemma-geometrically-irreducible-base-change-transcendental

Anglais L11340–11376 ; français L11298–11334.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11340) · FR-ALGEBRA-B15-CHOICE-0023.

Les deux sens de l'équivalence sont conservés, ainsi que la mention détails omis pour l'injection finale. Le T majuscule de k(T) dans la source est conservé dans la traduction et signalé à part : le corriger silencieusement confondrait traduction et édition. Localisation ne devient pas un quotient.

Point particulier à relire : T au lieu de t est un lapsus de variable proposé au dossier extérieur ; le texte traduit garde T. Aucune correction de formule n'est ajoutée à cette édition officielle-source.

Règles : FR-ALGEBRA-B15-RULE-IRRED, FR-ALGEBRA-B15-RULE-PRIME, FR-ALGEBRA-B15-RULE-TENSOR, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-geometrically-irreducible-base-change-transcendental}
Let $K/k$ be a field extension. The following are equivalent
\begin{enumerate}
\item $K$ is geometrically irreducible over $k$, and
\item the induced extension $K(t)/k(t)$ of purely transcendental extensions
is geometrically irreducible.
\end{enumerate}
\end{lemma}

\begin{proof}
Assume (1). Denote $\Omega$ an algebraic closure of $k(t)$.
By Definition \ref{definition-geometrically-irreducible}
we find that the spectrum of
$$
K \otimes_k \Omega = K \otimes_k k(t) \otimes_{k(t)} \Omega
$$
is irreducible. Since $K(t)$ is a localization of $K \otimes_k k(T)$
we conclude that the spectrum of $K(t) \otimes_{k(t)} \Omega$
is irreducible. Thus by Lemma \ref{lemma-geometrically-irreducible}
we find that $K(t)/k(t)$ is geometrically irreducible.

\medskip\noindent
Assume (2). Let $k'/k$ be a field extension.
We have to show that $K \otimes_k k'$ has a unique minimal prime.
We know that the spectrum of
$$
K(t) \otimes_{k(t)} k'(t)
$$
is irreducible, i.e., has a unique minimal prime.
Since there is an injective map
$K \otimes_k k' \to K(t) \otimes_{k(t)} k'(t)$ (details omitted)
we conclude by
Lemmas \ref{lemma-injective-minimal-primes-in-image} and
\ref{lemma-minimal-prime-image-minimal-prime}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-geometrically-irreducible-base-change-transcendental}
Soit $K/k$ une extension de corps. Les assertions suivantes sont équivalentes
\begin{enumerate}
\item $K$ est géométriquement irréductible sur $k$, et
\item l'extension induite $K(t)/k(t)$ d'extensions purement transcendantes
est géométriquement irréductible.
\end{enumerate}
\end{lemma}

\begin{proof}
Supposons (1). Notons $\Omega$ une clôture algébrique de $k(t)$.
Par la Définition \ref{definition-geometrically-irreducible}, nous obtenons
que le spectre de
$$
K \otimes_k \Omega = K \otimes_k k(t) \otimes_{k(t)} \Omega
$$
est irréductible. Comme $K(t)$ est une localisation de
$K \otimes_k k(T)$, nous concluons que le spectre de
$K(t) \otimes_{k(t)} \Omega$ est irréductible. Ainsi, par le
Lemme \ref{lemma-geometrically-irreducible}, $K(t)/k(t)$ est
géométriquement irréductible.

\medskip\noindent
Supposons (2). Soit $k'/k$ une extension de corps.
Nous devons montrer que $K \otimes_k k'$ possède un unique idéal premier
minimal. Nous savons que le spectre de
$$
K(t) \otimes_{k(t)} k'(t)
$$
est irréductible, c'est-à-dire qu'il possède un unique idéal premier minimal.
Comme il existe une application injective
$K \otimes_k k' \to K(t) \otimes_{k(t)} k'(t)$ (détails omis), nous
concluons par les Lemmes \ref{lemma-injective-minimal-primes-in-image} et
\ref{lemma-minimal-prime-image-minimal-prime}.
\end{proof}
```

</details>

### 24 — lemma-geometrically-irreducible-add-transcendental

Anglais L11377–11390 ; français L11335–11348.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11377) · FR-ALGEBRA-B15-CHOICE-0024.

x doit être transcendant sur L, donc aussi sur M. La conclusion porte sur L(x)/M(x), et non K/M. La preuve conserve seulement le renvoi et l'identification des deux extensions purement transcendantes, sans extrapolation.

Règles : FR-ALGEBRA-B15-RULE-IRRED.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-geometrically-irreducible-add-transcendental}
Let $K/L/M$ be a tower of fields with $L/M$ geometrically irreducible.
Let $x \in K$ be transcendental over $L$. Then $L(x)/M(x)$ is geometrically
irreducible.
\end{lemma}

\begin{proof}
This follows from
Lemma \ref{lemma-geometrically-irreducible-base-change-transcendental}
because the fields $L(x)$ and $M(x)$ are purely transcendental
extensions of $L$ and $M$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-geometrically-irreducible-add-transcendental}
Soit $K/L/M$ une tour de corps telle que $L/M$ soit géométriquement
irréductible. Soit $x \in K$ transcendant sur $L$. Alors $L(x)/M(x)$ est
géométriquement irréductible.
\end{lemma}

\begin{proof}
Cela résulte du
Lemme \ref{lemma-geometrically-irreducible-base-change-transcendental},
car les corps $L(x)$ et $M(x)$ sont des extensions purement transcendantes
de $L$ et $M$.
\end{proof}
```

</details>

### 25 — lemma-geometrically-irreducible-separable-elements

Anglais L11391–11426 ; français L11349–11383.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11391) · FR-ALGEBRA-B15-CHOICE-0025.

Algébrique séparable n'est pas synonyme d'algébrique tout court. Dans le second sens, k′ contient tous les éléments algébriques de K sur k ; l'hypothèse sur leurs parties séparables force alors la pure inséparabilité. Le nombre de facteurs du produit de corps et celui des plongements sont conservés.

Règles : FR-ALGEBRA-B15-RULE-PURE, FR-ALGEBRA-B15-RULE-SEP, FR-ALGEBRA-B15-RULE-IRRED, FR-ALGEBRA-B15-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-geometrically-irreducible-separable-elements}
Let $K/k$ be a field extension. The following are equivalent
\begin{enumerate}
\item $K/k$ is geometrically irreducible, and
\item every element $\alpha \in K$ separably algebraic over $k$ is
in $k$.
\end{enumerate}
\end{lemma}

\begin{proof}
Assume (1) and let $\alpha \in K$ be separably algebraic over $k$.
Then $k' = k(\alpha)$ is a finite separable extension of $k$ contained
in $K$. By Lemma \ref{lemma-subalgebra-geometrically-irreducible}
the extension $k'/k$ is geometrically irreducible.
In particular, we see that the spectrum of $k' \otimes_k \overline{k}$
is irreducible (and hence if it is a product of fields, then there
is exactly one factor).
By Fields, Lemma \ref{fields-lemma-finite-separable-tensor-alg-closed}
it follows that $\Hom_k(k', \overline{k})$ has one element which in turn
implies that $k' = k$ by
Fields, Lemma \ref{fields-lemma-separable-equality}.
Thus (2) holds.

\medskip\noindent
Assume (2). Let $k' \subset K$ be the subfield consisting of elements
algebraic over $k$. By
Lemma \ref{lemma-field-extension-geometrically-irreducible}
the extension $K/k'$ is geometrically irreducible.
By assumption $k'/k$ is a purely inseparable extension.
By Lemma \ref{lemma-p-ring-map} the extension
$k'/k$ is geometrically irreducible. Hence by
Lemma \ref{lemma-geometrically-irreducible-transitive}
we see that $K/k$ is geometrically irreducible.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-geometrically-irreducible-separable-elements}
Soit $K/k$ une extension de corps. Les assertions suivantes sont équivalentes
\begin{enumerate}
\item $K/k$ est géométriquement irréductible, et
\item tout élément $\alpha \in K$ qui est algébrique séparable sur $k$
appartient à $k$.
\end{enumerate}
\end{lemma}

\begin{proof}
Supposons (1) et soit $\alpha \in K$ algébrique séparable sur $k$.
Alors $k' = k(\alpha)$ est une extension finie et séparable de $k$ contenue
dans $K$. Par le Lemme \ref{lemma-subalgebra-geometrically-irreducible},
l'extension $k'/k$ est géométriquement irréductible.
En particulier, le spectre de $k' \otimes_k \overline{k}$ est
irréductible (et donc, s'il s'agit d'un produit de corps, il n'y a
exactement qu'un seul facteur). Par le
lemme \ref{fields-lemma-finite-separable-tensor-alg-closed} de Corps,
$\Hom_k(k', \overline{k})$ possède un seul élément, ce qui implique à son
tour que $k' = k$ par le
lemme \ref{fields-lemma-separable-equality} de Corps. L'assertion (2)
en résulte.

\medskip\noindent
Supposons (2). Soit $k' \subset K$ le sous-corps constitué des éléments
algébriques sur $k$. Par le
Lemme \ref{lemma-field-extension-geometrically-irreducible}, l'extension
$K/k'$ est géométriquement irréductible. Par hypothèse, $k'/k$ est une
extension purement inséparable. Par le Lemme \ref{lemma-p-ring-map},
l'extension $k'/k$ est géométriquement irréductible. Ainsi, par le
Lemme \ref{lemma-geometrically-irreducible-transitive}, $K/k$ est
géométriquement irréductible.
\end{proof}
```

</details>

### 26 — lemma-make-geometrically-irreducible

Anglais L11427–11444 ; français L11384–11401.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11427) · FR-ALGEBRA-B15-CHOICE-0026.

La sous-extension est constituée des éléments algébriques séparables, non de tous les éléments algébriques. La finitude de son degré n'est affirmée que si K/k est de type fini comme extension de corps. Type fini et extension finie restent distincts.

Règles : FR-ALGEBRA-B15-RULE-SEP, FR-ALGEBRA-B15-RULE-IRRED, FR-ALGEBRA-B15-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-make-geometrically-irreducible}
Let $K/k$ be a field extension. Consider the subextension $K/k'/k$ consisting
of elements separably algebraic over $k$. Then $K$ is geometrically irreducible
over $k'$. If $K/k$ is a finitely generated field extension, then
$[k' : k] < \infty$.
\end{lemma}

\begin{proof}
The first statement is immediate from
Lemma \ref{lemma-geometrically-irreducible-separable-elements}
and the fact that elements separably algebraic over $k'$
are in $k'$ by the transitivity of separable algebraic
extensions, see Fields, Lemma \ref{fields-lemma-separable-permanence}.
If $K/k$ is finitely generated, then $k'$ is finite over $k$ by
Fields, Lemma \ref{fields-lemma-algebraic-closure-in-finitely-generated}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-make-geometrically-irreducible}
Soit $K/k$ une extension de corps. Considérons la sous-extension
$K/k'/k$ constituée des éléments algébriques séparables sur $k$.
Alors $K$ est géométriquement irréductible sur $k'$. Si $K/k$ est une
extension de corps de type fini, alors $[k' : k] < \infty$.
\end{lemma}

\begin{proof}
La première assertion résulte immédiatement du
Lemme \ref{lemma-geometrically-irreducible-separable-elements} et du fait
que les éléments algébriques séparables sur $k'$ appartiennent à $k'$ par
transitivité des extensions algébriques séparables, voir le
lemme \ref{fields-lemma-separable-permanence} de Corps.
Si $K/k$ est de type fini, alors $k'$ est une extension finie de $k$ par le
lemme \ref{fields-lemma-algebraic-closure-in-finitely-generated} de Corps.
\end{proof}
```

</details>

### 27 — lemma-Galois-orbit

Anglais L11445–11483 ; français L11402–11441.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11445) · FR-ALGEBRA-B15-CHOICE-0027.

Agit transitivement concerne les idéaux premiers du produit tensoriel, non une action simplement transitive ni nécessairement les éléments du corps. La preuve conserve le passage aux idéaux maximaux, la bijection des spectres puis l'identification aux plongements par leurs noyaux. Une formule mise en hors-texte au lieu d'en ligne est une différence de mise en page déjà présente, sans modification de son contenu.

Règles : FR-ALGEBRA-B15-RULE-SEP, FR-ALGEBRA-B15-RULE-INTEGRAL, FR-ALGEBRA-B15-RULE-IRRED, FR-ALGEBRA-B15-RULE-PRIME, FR-ALGEBRA-B15-RULE-RESIDUE, FR-ALGEBRA-B15-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Galois-orbit}
Let $K/k$ be an extension of fields.
Let $\overline{k}/k$ be a separable algebraic closure.
Then $\text{Gal}(\overline{k}/k)$ acts transitively on the
primes of $\overline{k} \otimes_k K$.
\end{lemma}

\begin{proof}
Let $K/k'/k$ be the subextension found in
Lemma \ref{lemma-make-geometrically-irreducible}.
Note that as $k \subset \overline{k}$ is integral all the prime ideals
of $\overline{k} \otimes_k K$ and $\overline{k} \otimes_k k'$ are maximal, see
Lemma \ref{lemma-integral-no-inclusion}.
By Lemma \ref{lemma-geometrically-irreducible-any-base-change}
the map
$$
\Spec(\overline{k} \otimes_k K) \to \Spec(\overline{k} \otimes_k k')
$$
is bijective because (1) all primes are minimal primes, (2)
$\overline{k} \otimes_k K = (\overline{k} \otimes_k k') \otimes_{k'} K$,
and (3) $K$ is geometrically irreducible over $k'$.
Hence it suffices to prove the lemma for the action of
$\text{Gal}(\overline{k}/k)$ on the primes of $\overline{k} \otimes_k k'$.

\medskip\noindent
As every prime of $\overline{k} \otimes_k k'$ is maximal, the residue fields
are isomorphic to $\overline{k}$. Hence the prime ideals of
$\overline{k} \otimes_k k'$ correspond one to one to elements of
$\Hom_k(k', \overline{k})$ with $\sigma \in \Hom_k(k', \overline{k})$
corresponding to the kernel $\mathfrak p_\sigma$ of
$1 \otimes \sigma : \overline{k} \otimes_k k' \to \overline{k}$.
In particular $\text{Gal}(\overline{k}/k)$ acts transitively on
this set as desired.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-Galois-orbit}
Soit $K/k$ une extension de corps.
Soit $\overline{k}/k$ une clôture algébrique séparable.
Alors $\text{Gal}(\overline{k}/k)$ agit transitivement sur les idéaux
premiers de $\overline{k} \otimes_k K$.
\end{lemma}

\begin{proof}
Soit $K/k'/k$ la sous-extension obtenue dans le
Lemme \ref{lemma-make-geometrically-irreducible}.
Remarquons que, comme $k \subset \overline{k}$ est entière, tous les
idéaux premiers de $\overline{k} \otimes_k K$ et
$\overline{k} \otimes_k k'$ sont maximaux, voir le
Lemme \ref{lemma-integral-no-inclusion}.
Par le Lemme \ref{lemma-geometrically-irreducible-any-base-change},
l'application
$$
\Spec(\overline{k} \otimes_k K) \to \Spec(\overline{k} \otimes_k k')
$$
est bijective car (1) tous les idéaux premiers sont minimaux, (2)
$$
\overline{k} \otimes_k K = (\overline{k} \otimes_k k') \otimes_{k'} K
$$
et (3) $K$ est géométriquement irréductible sur $k'$.
Il suffit donc de démontrer le lemme pour l'action de
$\text{Gal}(\overline{k}/k)$ sur les idéaux premiers de
$\overline{k} \otimes_k k'$.

\medskip\noindent
Comme tout idéal premier de $\overline{k} \otimes_k k'$ est maximal, les
corps résiduels sont isomorphes à $\overline{k}$. Les idéaux premiers de
$\overline{k} \otimes_k k'$ correspondent donc bijectivement aux éléments
de $\Hom_k(k', \overline{k})$, où $\sigma \in \Hom_k(k', \overline{k})$
correspond au noyau $\mathfrak p_\sigma$ de
$1 \otimes \sigma : \overline{k} \otimes_k k' \to \overline{k}$.
En particulier, $\text{Gal}(\overline{k}/k)$ agit transitivement sur cet
ensemble, comme voulu.
\end{proof}
```

</details>

## Observation extérieure au texte traduit

### FR-ALGEBRA-B15-SOURCE-NOTE-0001

[Source L11357](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11357) — lemma-geometrically-irreducible-base-change-transcendental.

```tex
$K \otimes_k k(T)$
```

Le lemme et ses deux preuves utilisent la variable t de K(t)/k(t). La seule occurrence k(T) introduit une majuscule sans identification de variables. La lecture attendue est k(t), donnant la localisation de K⊗_k k(t) dans K(t). Il s'agit d'un lapsus de notation, non d'une réfutation du lemme. Le français conserve exactement k(T) ; la proposition est extérieure au texte et n'est pas présentée comme une admission nouvelle au registre.

Confiance éditoriale forte pour ce lapsus local, non probabilité calibrée. Aucune admission nouvelle au registre, aucune découverte originale ni déduplication globale revendiquée.

## Contrôles et suite

Les 590 régions mathématiques du lot concordent avec la seule exception linguistique divides → divise, déjà présente avant cette relecture. Le préfixe compte 8 155 régions et vingt-deux exceptions linguistiques exactes, dont vingt et une antérieures. L’égalité brute sans ces exceptions n’est pas revendiquée.

Le localisateur bibliographique Alper-adequate, numéro 3.1.6, est préservé ; seul Lemma devient Lemme. La clé reste identique. Un passage en ligne devenu hors-texte est une différence de disposition déjà présente ; son contenu mathématique est exact. Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items sont préservés. Aucune région mathématique du français entier ne change depuis le lot précédent.

Les opérations inverses retrouvent le lot précédent puis le témoin public conservé. Les 401 paires sont contiguës, sans lacune ni chevauchement. Les octets du préfixe déjà relu et ceux du suffixe encore non relu sont inchangés. Les contrôles mécaniques complètent la lecture sémantique et ne la remplacent pas.

Prochaine lecture : Algèbres géométriquement connexes, anglais L11484 / français L11442. Aucun nouveau PDF, aucune publication et aucune certification globale du chapitre ou de l’édition dans ce lot.

