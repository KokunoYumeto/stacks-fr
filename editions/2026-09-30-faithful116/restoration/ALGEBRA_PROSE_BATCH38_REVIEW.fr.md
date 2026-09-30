# Profondeur

## Résultat et portée

Comparaison complète : anglais L17759–18086 /français L17525–17852, 328 lignes chacun, douze paires et 243 occurrences contextualisées. Couverture continue : 72 sections, 656 paires et 6745 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Le français est fidèle et reste inchangé après comparaison intégrale. Aucune copie LaTeX identique supplémentaire n’est créée. Les conventions IM=M et profondeur du module nul égale à+∞ sont conservées.

Deux observations de notation ou de frontière de preuve restent séparées. Un faux positif est rejeté explicitement : an f est grammatical devant une lettre prononcée eff. Aucun de ces constats ne devient une correction mathématique cachée.

Lecture produite par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. Le canon est consulté rétrospectivement, non présenté comme consulté lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré conservé](staged/fr/010_algebra.prose-batch37.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH37_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH38_VALIDATION.json) · [Choix et faux positif rejeté](ALGEBRA_PROSE_BATCH38_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH38_OCCURRENCES.json) · [Opérations](ALGEBRA_PROSE_BATCH38_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH38_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH38_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH38_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH38_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH38_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Yves Laszlo — Introduction à l'algèbre commutative et homologique, maîtrise2003–2004

[Source consultée](https://www.cmls.polytechnique.fr/perso/laszlo/maitrise/maitrisefin.pdf) · [Fichier conservé](canon-consulted/fr-algebra/laszlo-commutative-homologique-2003.pdf)

Pages PDF/imprimées1,16,64–73 et77–79 entièrement lues. Exemple16.2 ; partieVII, définitions et suite exacte ; VIII.1, VIII.3.1, définition3.2, proposition3.3, corollaires3.4–3.5 et exercice5.1 ; X.1–2, calcul des Ext p79. PDF70 et72 rendus et inspectés visuellement. Réutilisation explicitement déclarée de la lecture complète effectuée dans ce même tour pour B37 ; pas de nouvelle lecture antérieure inventée.

Attestations courtes : « résolution libre », « morphisme de complexes », « homotopie », « suite exacte courte », « foncteur contravariant ».

Atteste le vocabulaire du complexe, de la résolution et de l'homotopie ; expose les relèvements et les suites exactes de cohomologie. L'exemple16.2 définit Hom(-,c) par précomposition ; X.2 présente le calcul de Ext via résolutions.

Limites : Consultation rétrospective. Les indices cohomologiques négatifs ne remplacent pas ceux de Stacks. Les erreurs de variables H(L)/H(P) p70, et les formules incohérentes de dérivation/ordre de suite p78–79, ne sont pas adoptées. La terminologie est attestée, mais chaque formule est vérifiée contre ses domaines. Aucune relecture humaine.

SHA-256 : 6CE611DFE7265C9658269EEE371803873B6ECEA26FEAC86E3455075F8D0A6D79.

### Christian Peskine — Introduction algébrique à la géométrie projective

[Source consultée](https://perso.univ-rennes1.fr/matthieu.romagny/M2_0708/bouquin.pdf) · [Fichier conservé](canon-consulted/fr-algebra/peskine-geometrie-projective-2007.pdf)

Pages PDF138–143 /imprimées137–142 entièrement relues. Section16.1 ; notamment définition16.7, lemme16.17, corollaire16.18 et démonstration16.19. Réutilisation explicitement déclarée de la lecture complète effectuée dans ce même tour pour B37 ; pas de nouvelle lecture antérieure inventée.

Attestations courtes : « profondeur », « modules libres de type fini », « diagramme du serpent ».

Appui au registre de profondeur, de type fini et des arguments sur Hom près du but de la section. La présentation dans16.19 confirme le sens de libre de type fini.

Limites : Ces pages ne définissent pas Ext et ne sont pas citées comme preuve de sa variance. Leur contexte local/noethérien ne restreint pas la définition générale des résolutions de Stacks. Consultation rétrospective ; pas de relecture humaine.

SHA-256 : C84D597457282B22B993F523791F4A3E391A74554FF76F7F49878640789435BA.

## Modifications et motifs

Aucune modification nécessaire. Les formulations retenues sont justifiées dans les paires complètes. Une liste de variables comprise comme suite collective ne constitue pas automatiquement un défaut d’accord. Les conventions propres à Stacks ne sont pas normalisées vers celles d’un autre manuel.

## Observations séparées sur la source

Deux observations prudentes : délimitation du quotient R/(p+(x)) et cas∞/famille vide dans la preuve finale. Elles ne prétendent ni que le théorème non nul est faux ni qu’un raccourci contextuel serait nécessairement incorrect. Aucun registre n’est admis, aucune déduplication globale ni première découverte revendiquée.

### lemma-inherit-minimal-primes

[Anglais officiel L17976](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17976) · FR-ALGEBRA-B38-SOURCE-NOTE-0001.

```tex
$\overline{N} \to N/xN = R/\mathfrak p + (x)$
```

N≅R/p donne N/xN≅R/(p+(x)), non un quotient suivi d'une addition indépendante. La notation R/p+(x) manque de délimitation visible ; le même raccourci apparaît dans la dimensionL18008. Ajouter les parenthèses autour de p+(x) rend l'objet non ambigu. Selon les habitudes typographiques, le contexte peut déjà faire comprendre ce quotient : constat de notation, pas preuve que le lemme est faux. Les deux écritures originales restent dans le français.

Confiance forte sur le quotient voulu ; confiance modérée sur la nécessité de qualifier le raccourci de faute. Observation séparée, aucune admission.

[Pièce primaire algebra.tex L18008–18008](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18008)
SHA-256 du fichier : FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.

```tex
$\dim(R/\mathfrak p + (x)) = \dim(R/\mathfrak p) - 1$.
```

### lemma-depth-goes-down-finite

[Anglais officiel L18065](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18065) · FR-ALGEBRA-B38-SOURCE-NOTE-0002.

```tex
$k = \min\nolimits_{i = 1, \ldots, n} \text{depth}(N_{\mathfrak m_i})$.
```

L'énoncé permet N=0, auquel cas les profondeurs valent∞. La récurrence ordinaire sur k ne couvre pas k=∞ ; pour une famille non vide l'égalité est directement∞=∞ et mérite un cas séparé. Pour N≠0, le support atteint au moins un idéal maximal, sa profondeur est finie, donc le minimum k est fini et la récurrence fonctionne. Si l'anneau S=0 est permis, n=0 et le minimum vide doit recevoir explicitement la convention∞ pour garder ce même énoncé. Ce sont précisions de frontière de preuve/convention, pas un contre-exemple au résultat non nul. Le français ne rajoute aucune restriction ni correction silencieuse.

Confiance forte sur la frontière∞ de la récurrence, réserve explicite sur la convention du minimum vide ; aucune nouvelle admission.

## Faux positif explicitement rejeté

### FR-ALGEBRA-B38-REJECTED-0001

[Source L17806](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17806)

```tex
an $f \in I$
```

La lettre f employée comme nom de variable se prononce généralement eff, mais l'article anglais dépend ici aussi de la lecture mathématique de la lettre ; an f est en fait idiomatique. Ce point n'est donc pas retenu comme défaut source : le français f sans article est déjà correct.

Faux positif rejeté après analyse de la prononciation ; aucune correction proposée.

## Règles contextualisées

### FR-ALGEBRA-B38-RULE-DEPTH

Supremum global, minimum local, dimensions et profondeurs ont les conventions propres à chaque énoncé, y compris∞ et0.

Canon : FR-ALGEBRA-B38-CANON-PESKINE.

### FR-ALGEBRA-B38-RULE-REGULAR

Le non-diviseur et les quotients successifs sont contrôlés avec le cas nul, le quotient final et les hypothèses de finitude.

Canon : FR-ALGEBRA-B38-CANON-PESKINE.

### FR-ALGEBRA-B38-RULE-EXACT

Chaque suite et localisation garde son sens, ses arguments et ses conditions ; les degrés et directions Ext sont vérifiés dans la paire entière.

Canon : FR-ALGEBRA-B38-CANON-LASZLO, FR-ALGEBRA-B38-CANON-PESKINE.

### FR-ALGEBRA-B38-RULE-PRIME

Association, support, minimalité et maximalité ne se substituent pas l'une à l'autre. Leur applicabilité contextuelle est contrôlée au-delà du vocabulaire attesté.

Canon : FR-ALGEBRA-B38-CANON-PESKINE.

### FR-ALGEBRA-B38-RULE-RING

Les conditions local, noethérien et type fini sont conservées. Le passage d'un S-module à son R-module sous-jacent est explicitement comparé.

Canon : FR-ALGEBRA-B38-CANON-PESKINE, FR-ALGEBRA-B38-CANON-LASZLO.

### FR-ALGEBRA-B38-RULE-LOGIC

Chaque sens d'implication et chaque récurrence est confronté à son domaine ; les cas∞ et vide sont documentés plutôt qu'exclus silencieusement.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-depth

Anglais L17759–17764 ; français L17525–17530.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17759) · FR-ALGEBRA-B38-CHOICE-0001.

Profondeur est directement attesté chez Peskine16. Le bref Voici notre définition garde la fonction introductive sans ajouter une définition locale concurrente.

Règles : FR-ALGEBRA-B38-RULE-DEPTH.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Depth}
\label{section-depth}

\noindent
Here is our definition.
```

Français restauré :
```tex
\section{Profondeur}
\label{section-depth}

\noindent
Voici notre définition.
```

</details>

### 02 — definition-depth

Anglais L17765–17795 ; français L17531–17561.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17765) · FR-ALGEBRA-B38-CHOICE-0002.

Définition entière et tous les commentaires comparés. Profondeur relativement à I explicite I-depth sans confondre cette notion avec la seule profondeur à l'idéal maximal. Borne supérieure, longueurs, suite M-régulière et cas IM=M gardent leur portée ; module0 a profondeur+∞, y compris lorsque la suite vide n'est pas régulière. Les cas I=R, radical de Jacobson, Nakayama, profondeur0 et les deux contre-exemples sont conservés. Peskine16.7 atteste profondeur mais ne remplace pas la convention explicite de Stacks pour le module nul.

Point particulier à relire : Ne pas importer une convention profondeur du module nul différente de +∞ ni oublier le cas IM=M. La suite vide n'est pas régulière sur0 selon la définition propre à Stacks.

Règles : FR-ALGEBRA-B38-RULE-DEPTH, FR-ALGEBRA-B38-RULE-REGULAR, FR-ALGEBRA-B38-RULE-EXACT, FR-ALGEBRA-B38-RULE-PRIME, FR-ALGEBRA-B38-RULE-RING, FR-ALGEBRA-B38-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-depth}
Let $R$ be a ring, and $I \subset R$ an ideal. Let $M$ be a finite $R$-module.
The {\it $I$-depth} of $M$, denoted $\text{depth}_I(M)$, is defined as follows:
\begin{enumerate}
\item if $IM \not = M$, then $\text{depth}_I(M)$ is the supremum in
$\{0, 1, 2, \ldots, \infty\}$ of the lengths of $M$-regular sequences in $I$,
\item if $IM = M$ we set $\text{depth}_I(M) = \infty$.
\end{enumerate}
If $(R, \mathfrak m)$ is local we call $\text{depth}_{\mathfrak m}(M)$ simply
the {\it depth} of $M$.
\end{definition}

\noindent
Explanation. By Definition \ref{definition-regular-sequence} the empty
sequence is not a regular sequence on the zero module, but for practical
purposes it turns out to be convenient to set the depth of the $0$ module
equal to $+\infty$. Note that if $I = R$, then $\text{depth}_I(M) = \infty$
for all finite $R$-modules $M$. If $I$ is contained in the Jacobson radical
of $R$ (e.g., if $R$ is local and $I \subset \mathfrak m_R$), then
$M \not = 0 \Rightarrow IM \not = M$ by Nakayama's lemma.
A module $M$ has $I$-depth $0$ if and only if $M$ is nonzero and $I$ does
not contain a nonzerodivisor on $M$.

\medskip\noindent
Example \ref{example-global-regular} shows depth does not
behave well even if the ring is Noetherian, and Example
\ref{example-local-regular} shows that it does not
behave well if the ring is local but non-Noetherian.
We will see depth behaves well if the ring is local Noetherian.
```

Français restauré :
```tex
\begin{definition}
\label{definition-depth}
Soit $R$ un anneau, et soit $I \subset R$ un idéal. Soit $M$ un $R$-module de type fini.
La {\it profondeur relativement à $I$} de $M$, notée $\text{depth}_I(M)$, est définie comme suit :
\begin{enumerate}
\item si $IM \not = M$, alors $\text{depth}_I(M)$ est la borne supérieure dans
$\{0, 1, 2, \ldots, \infty\}$ des longueurs des suites $M$-régulières dans $I$,
\item si $IM = M$, on pose $\text{depth}_I(M) = \infty$.
\end{enumerate}
Si $(R, \mathfrak m)$ est local, on appelle simplement $\text{depth}_{\mathfrak m}(M)$ la
{\it profondeur} de $M$.
\end{definition}

\noindent
Explication. D'après la Définition \ref{definition-regular-sequence}, la suite vide
n'est pas une suite régulière sur le module nul, mais, en pratique,
il s'avère commode de fixer la profondeur du module $0$
égale à $+\infty$. Remarquons que, si $I = R$, alors $\text{depth}_I(M) = \infty$
pour tout $R$-module de type fini $M$. Si $I$ est contenu dans le radical de Jacobson
de $R$ (par exemple, si $R$ est local et si $I \subset \mathfrak m_R$), alors
$M \not = 0 \Rightarrow IM \not = M$ d'après le lemme de Nakayama.
Un module $M$ a une profondeur relativement à $I$ égale à $0$ si et seulement si $M$ est non nul et si $I$
ne contient aucun non-diviseur de zéro sur $M$.

\medskip\noindent
L'Exemple \ref{example-global-regular} montre que la profondeur ne se comporte pas
bien, même si l'anneau est noethérien, et l'Exemple
\ref{example-local-regular} montre qu'elle ne se comporte pas
bien si l'anneau est local mais non noethérien.
Nous verrons que la profondeur se comporte bien si l'anneau est local noethérien.
```

</details>

### 03 — lemma-depth-weak-sequence

Anglais L17796–17812 ; français L17562–17578.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17796) · FR-ALGEBRA-B38-CHOICE-0003.

Chaque f_i est un non-diviseur de zéro sur le quotient précédent ; il n'est pas requis ici que le dernier quotient soit non nul. Le cas IM=M donne f agissant comme l'identité puis des zéros agissant injectivement sur le module nul. La suite infinie signifie longueurs finies arbitrairement grandes dans le supremum. Les deux quantités coïncident explicite correctement agreement sans modifier l'argument.

Point particulier à relire : Le quotient final peut être nul dans cette caractérisation faible. Sur le module nul, l'application multiplication par0 est injective ; cela explique les zéros successifs et évite un faux défaut.

Règles : FR-ALGEBRA-B38-RULE-DEPTH, FR-ALGEBRA-B38-RULE-REGULAR, FR-ALGEBRA-B38-RULE-EXACT, FR-ALGEBRA-B38-RULE-RING, FR-ALGEBRA-B38-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-depth-weak-sequence}
Let $R$ be a ring, $I \subset R$ an ideal, and $M$ a finite $R$-module.
Then $\text{depth}_I(M)$ is equal to the supremum of the lengths of
sequences $f_1, \ldots, f_r \in I$ such that $f_i$ is a nonzerodivisor
on $M/(f_1, \ldots, f_{i - 1})M$.
\end{lemma}

\begin{proof}
Suppose that $IM = M$. Then Lemma \ref{lemma-NAK} shows there exists
an $f \in I$ such that $f : M \to M$ is $\text{id}_M$. Hence
$f, 0, 0, 0, \ldots$ is an infinite sequence of successive
nonzerodivisors and we see agreement holds in this case.
If $IM \not =  M$, then we see that a sequence as in the lemma
is an $M$-regular sequence and we conclude that agreement holds as well.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-depth-weak-sequence}
Soit $R$ un anneau, $I \subset R$ un idéal, et $M$ un $R$-module de type fini.
Alors $\text{depth}_I(M)$ est égale à la borne supérieure des longueurs des
suites $f_1, \ldots, f_r \in I$ telles que $f_i$ soit un non-diviseur de zéro
sur $M/(f_1, \ldots, f_{i - 1})M$.
\end{lemma}

\begin{proof}
Supposons que $IM = M$. Alors le Lemme \ref{lemma-NAK} montre qu'il existe
$f \in I$ tel que $f : M \to M$ soit $\text{id}_M$. Ainsi
$f, 0, 0, 0, \ldots$ est une suite infinie de
non-diviseurs de zéro successifs, et les deux quantités coïncident dans ce cas.
Si $IM \not =  M$, une suite comme dans le lemme
est une suite $M$-régulière, et les deux quantités coïncident là encore.
\end{proof}
```

</details>

### 04 — lemma-bound-depth

Anglais L17813–17838 ; français L17579–17604.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17813) · FR-ALGEBRA-B38-CHOICE-0004.

M est non nul, de type fini, sur un anneau local noethérien. La dimension du support reste le majorant de la profondeur, non une égalité générale. Cas dimension0, idéaux associés et récurrence après quotient sont tous comparés. Peskine16.4/16.11 appuie le registre ; les hypothèses locales et la perte d'une dimension ne sont pas supprimées.

Règles : FR-ALGEBRA-B38-RULE-DEPTH, FR-ALGEBRA-B38-RULE-REGULAR, FR-ALGEBRA-B38-RULE-EXACT, FR-ALGEBRA-B38-RULE-RING, FR-ALGEBRA-B38-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-bound-depth}
Let $(R, \mathfrak m)$ be a Noetherian local ring.
Let $M$ be a nonzero finite $R$-module.
Then $\dim(\text{Supp}(M)) \geq \text{depth}(M)$.
\end{lemma}

\begin{proof}
The proof is by induction on $\dim(\text{Supp}(M))$.
If $\dim(\text{Supp}(M)) = 0$, then
$\text{Supp}(M) = \{\mathfrak m\}$, whence $\text{Ass}(M) = \{\mathfrak m\}$
(by Lemmas \ref{lemma-ass-support} and \ref{lemma-ass-zero}), and hence
the depth of $M$ is zero for example by
Lemma \ref{lemma-ideal-nonzerodivisor}.
For the induction step we assume $\dim(\text{Supp}(M)) > 0$.
Let $f_1, \ldots, f_d$ be a sequence of elements of $\mathfrak m$
such that $f_i$ is a nonzerodivisor on $M/(f_1, \ldots, f_{i - 1})M$.
According to Lemma \ref{lemma-depth-weak-sequence} it suffices to prove
$\dim(\text{Supp}(M)) \geq d$. We may assume
$d > 0$ otherwise the lemma holds. By
Lemma \ref{lemma-one-equation-module}
we have $\dim(\text{Supp}(M/f_1M)) = \dim(\text{Supp}(M)) - 1$.
By induction we conclude $\dim(\text{Supp}(M/f_1M)) \geq d - 1$
as desired.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-bound-depth}
Soit $(R, \mathfrak m)$ un anneau local noethérien.
Soit $M$ un $R$-module de type fini non nul.
Alors $\dim(\text{Supp}(M)) \geq \text{depth}(M)$.
\end{lemma}

\begin{proof}
La démonstration se fait par récurrence sur $\dim(\text{Supp}(M))$.
Si $\dim(\text{Supp}(M)) = 0$, alors
$\text{Supp}(M) = \{\mathfrak m\}$, d'où $\text{Ass}(M) = \{\mathfrak m\}$
(d'après les Lemmes \ref{lemma-ass-support} et \ref{lemma-ass-zero}), et donc
la profondeur de $M$ est nulle, par exemple d'après le
Lemme \ref{lemma-ideal-nonzerodivisor}.
Pour l'étape de récurrence, supposons $\dim(\text{Supp}(M)) > 0$.
Soit $f_1, \ldots, f_d$ une suite d'éléments de $\mathfrak m$
telle que $f_i$ soit un non-diviseur de zéro sur $M/(f_1, \ldots, f_{i - 1})M$.
D'après le Lemme \ref{lemma-depth-weak-sequence}, il suffit de montrer que
$\dim(\text{Supp}(M)) \geq d$. On peut supposer
$d > 0$, sans quoi le lemme est établi. D'après le
Lemme \ref{lemma-one-equation-module},
on a $\dim(\text{Supp}(M/f_1M)) = \dim(\text{Supp}(M)) - 1$.
Par récurrence, on conclut que $\dim(\text{Supp}(M/f_1M)) \geq d - 1$,
comme souhaité.
\end{proof}
```

</details>

### 05 — lemma-depth-finite-noetherian

Anglais L17839–17861 ; français L17605–17627.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17839) · FR-ALGEBRA-B38-CHOICE-0005.

Le lemme est global : R noethérien, IM≠M et M non nul de type fini. La preuve choisit p dans Supp(M/IM), garde le quotient localisé non nul et toutes les inégalités successives de profondeur. Localisation exacte et plate n'est pas remplacée par fidèle platitude ; le quotient non nul est établi séparément. Aucune régularité globale supplémentaire n'est imposée.

Règles : FR-ALGEBRA-B38-RULE-REGULAR, FR-ALGEBRA-B38-RULE-EXACT, FR-ALGEBRA-B38-RULE-RING, FR-ALGEBRA-B38-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-depth-finite-noetherian}
Let $R$ be a Noetherian ring, $I \subset R$ an ideal, and $M$ a
finite nonzero $R$-module such that $IM \not = M$. Then
$\text{depth}_I(M) < \infty$.
\end{lemma}

\begin{proof}
Since $M/IM$ is nonzero we can choose $\mathfrak p \in \text{Supp}(M/IM)$
by Lemma \ref{lemma-support-zero}. Then $(M/IM)_\mathfrak p \not = 0$
which implies $I \subset \mathfrak p$ and moreover implies
$M_\mathfrak p \not = IM_\mathfrak p$ as localization is exact.
Let $f_1, \ldots, f_r \in I$ be an $M$-regular sequence.
Then $M_\mathfrak p/(f_1, \ldots, f_r)M_\mathfrak p$ is
nonzero as $(f_1, \ldots, f_r) \subset I$. As localization is
flat we see that the images of $f_1, \ldots, f_r$ form a
$M_\mathfrak p$-regular sequence in $I_\mathfrak p$. Since this
works for every $M$-regular sequence in $I$ we conclude that
$\text{depth}_I(M) \leq \text{depth}_{I_\mathfrak p}(M_\mathfrak p)$.
The latter is $\leq \text{depth}(M_\mathfrak p)$ which is
$< \infty$ by Lemma \ref{lemma-bound-depth}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-depth-finite-noetherian}
Soit $R$ un anneau noethérien, $I \subset R$ un idéal, et $M$ un
$R$-module non nul de type fini tel que $IM \not = M$. Alors
$\text{depth}_I(M) < \infty$.
\end{lemma}

\begin{proof}
Puisque $M/IM$ est non nul, on peut choisir $\mathfrak p \in \text{Supp}(M/IM)$
d'après le Lemme \ref{lemma-support-zero}. Alors $(M/IM)_\mathfrak p \not = 0$,
ce qui implique $I \subset \mathfrak p$ et, de plus,
$M_\mathfrak p \not = IM_\mathfrak p$, puisque la localisation est exacte.
Soit $f_1, \ldots, f_r \in I$ une suite $M$-régulière.
Alors $M_\mathfrak p/(f_1, \ldots, f_r)M_\mathfrak p$ est
non nul, car $(f_1, \ldots, f_r) \subset I$. La localisation étant
plate, les images de $f_1, \ldots, f_r$ forment une
suite $M_\mathfrak p$-régulière dans $I_\mathfrak p$. Comme cela vaut
pour toute suite $M$-régulière dans $I$, on conclut que
$\text{depth}_I(M) \leq \text{depth}_{I_\mathfrak p}(M_\mathfrak p)$.
Ce dernier membre est $\leq \text{depth}(M_\mathfrak p)$, qui est
$< \infty$ d'après le Lemme \ref{lemma-bound-depth}.
\end{proof}
```

</details>

### 06 — lemma-depth-ext

Anglais L17862–17903 ; français L17628–17669.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17862) · FR-ALGEBRA-B38-CHOICE-0006.

Profondeur est le premier degré Ext non nul, avec tous les termes du complexe et de la suite longue comparés. κ est le corps résiduel utilisé pour R/m, pas un corps de coefficients ajouté. Le choix de x est possible comme premier terme d'une suite de longueur maximale : finitude acquise au lemme précédent, et une suite plus longue dans M/xM contredirait cette maximalité. Cela motive la preuve sans importer circulairement le lemme de diminution qui vient plus loin. Le raisonnement δ=0 et la récurrence δ>0 sont conservés.

Point particulier à relire : La condition profondeur(M/xM)=δ(M)-1 est obtenue ici à partir d'une suite de longueur maximale, non par le lemme ultérieur. La justification détaillée appartient au dossier de lecture, pas à une preuve supplémentaire insérée.

Règles : FR-ALGEBRA-B38-RULE-DEPTH, FR-ALGEBRA-B38-RULE-REGULAR, FR-ALGEBRA-B38-RULE-EXACT, FR-ALGEBRA-B38-RULE-PRIME, FR-ALGEBRA-B38-RULE-RING, FR-ALGEBRA-B38-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-depth-ext}
Let $R$ be a Noetherian local ring with maximal ideal $\mathfrak m$.
Let $M$ be a nonzero finite $R$-module. Then $\text{depth}(M)$
is equal to the smallest integer $i$ such that
$\Ext^i_R(R/\mathfrak m, M)$ is nonzero.
\end{lemma}

\begin{proof}
Let $\delta(M)$ denote the depth of $M$ and let $i(M)$ denote
the smallest integer $i$ such that $\Ext^i_R(R/\mathfrak m, M)$
is nonzero. We will see in a moment that $i(M) < \infty$.
By Lemma \ref{lemma-ideal-nonzerodivisor} we have
$\delta(M) = 0$ if and only if $i(M) = 0$, because
$\mathfrak m \in \text{Ass}(M)$ exactly means
that $i(M) = 0$. Hence if $\delta(M)$ or $i(M)$ is $> 0$, then we may
choose $x \in \mathfrak m$ such that (a) $x$ is a nonzerodivisor
on $M$, and (b) $\text{depth}(M/xM) = \delta(M) - 1$.
Consider the long exact sequence
of Ext-groups associated to the short exact sequence
$0 \to M \to M \to M/xM \to 0$ by Lemma \ref{lemma-long-exact-seq-ext}:
$$
\begin{matrix}
0
\to \Hom_R(\kappa, M)
\to \Hom_R(\kappa, M)
\to \Hom_R(\kappa, M/xM)
\\
\phantom{0\ }
\to \Ext^1_R(\kappa, M)
\to \Ext^1_R(\kappa, M)
\to \Ext^1_R(\kappa, M/xM)
\to \ldots
\end{matrix}
$$
Since $x \in \mathfrak m$ all the maps $\Ext^i_R(\kappa, M)
\to \Ext^i_R(\kappa, M)$ are zero, see
Lemma \ref{lemma-annihilate-ext}.
Thus it is clear that $i(M/xM) = i(M) - 1$. Induction on
$\delta(M)$ finishes the proof.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-depth-ext}
Soit $R$ un anneau local noethérien d'idéal maximal $\mathfrak m$.
Soit $M$ un $R$-module de type fini non nul. Alors $\text{depth}(M)$
est égale au plus petit entier $i$ tel que
$\Ext^i_R(R/\mathfrak m, M)$ soit non nul.
\end{lemma}

\begin{proof}
Notons $\delta(M)$ la profondeur de $M$ et $i(M)$ le
plus petit entier $i$ tel que $\Ext^i_R(R/\mathfrak m, M)$
soit non nul. Nous verrons dans un instant que $i(M) < \infty$.
D'après le Lemme \ref{lemma-ideal-nonzerodivisor}, on a
$\delta(M) = 0$ si et seulement si $i(M) = 0$, car
$\mathfrak m \in \text{Ass}(M)$ signifie exactement
que $i(M) = 0$. Ainsi, si $\delta(M)$ ou $i(M)$ est $> 0$, on peut
choisir $x \in \mathfrak m$ tel que (a) $x$ soit un non-diviseur de zéro
sur $M$, et (b) $\text{depth}(M/xM) = \delta(M) - 1$.
Considérons la suite exacte longue
de groupes Ext associée à la suite exacte courte
$0 \to M \to M \to M/xM \to 0$ par le Lemme \ref{lemma-long-exact-seq-ext} :
$$
\begin{matrix}
0
\to \Hom_R(\kappa, M)
\to \Hom_R(\kappa, M)
\to \Hom_R(\kappa, M/xM)
\\
\phantom{0\ }
\to \Ext^1_R(\kappa, M)
\to \Ext^1_R(\kappa, M)
\to \Ext^1_R(\kappa, M/xM)
\to \ldots
\end{matrix}
$$
Puisque $x \in \mathfrak m$, toutes les applications $\Ext^i_R(\kappa, M)
\to \Ext^i_R(\kappa, M)$ sont nulles ; voir le
Lemme \ref{lemma-annihilate-ext}.
Il est donc clair que $i(M/xM) = i(M) - 1$. Une récurrence sur
$\delta(M)$ achève la démonstration.
\end{proof}
```

</details>

### 07 — lemma-depth-in-ses

Anglais L17904–17938 ; français L17670–17704.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17904) · FR-ALGEBRA-B38-CHOICE-0007.

Les trois modules sont non nuls et de type fini. Les trois inégalités, leurs minima et les décalages -1/+1 sont exactement comparés. La suite Ext est covariante dans ce second argument, contrairement à la première variable du dossier précédent. Peskine16.17 atteste le lemme de profondeur et ses cas ; ce dossier conserve les trois inégalités propres à Stacks plutôt que de substituer son énoncé.

Règles : FR-ALGEBRA-B38-RULE-DEPTH, FR-ALGEBRA-B38-RULE-REGULAR, FR-ALGEBRA-B38-RULE-EXACT, FR-ALGEBRA-B38-RULE-RING.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-depth-in-ses}
Let $R$ be a local Noetherian ring. Let $0 \to N' \to N \to N'' \to 0$
be a short exact sequence of nonzero finite $R$-modules.
\begin{enumerate}
\item
$\text{depth}(N) \geq \min\{\text{depth}(N'), \text{depth}(N'')\}$
\item
$\text{depth}(N'') \geq \min\{\text{depth}(N), \text{depth}(N') - 1\}$
\item
$\text{depth}(N') \geq \min\{\text{depth}(N), \text{depth}(N'') + 1\}$
\end{enumerate}
\end{lemma}

\begin{proof}
Use the characterization of depth using the Ext groups
$\Ext^i(\kappa, N)$, see Lemma \ref{lemma-depth-ext},
and use the long exact cohomology sequence
$$
\begin{matrix}
0
\to \Hom_R(\kappa, N')
\to \Hom_R(\kappa, N)
\to \Hom_R(\kappa, N'')
\\
\phantom{0\ }
\to \Ext^1_R(\kappa, N')
\to \Ext^1_R(\kappa, N)
\to \Ext^1_R(\kappa, N'')
\to \ldots
\end{matrix}
$$
from Lemma \ref{lemma-long-exact-seq-ext}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-depth-in-ses}
Soit $R$ un anneau local noethérien. Soit $0 \to N' \to N \to N'' \to 0$
une suite exacte courte de $R$-modules non nuls de type fini.
\begin{enumerate}
\item
$\text{depth}(N) \geq \min\{\text{depth}(N'), \text{depth}(N'')\}$
\item
$\text{depth}(N'') \geq \min\{\text{depth}(N), \text{depth}(N') - 1\}$
\item
$\text{depth}(N') \geq \min\{\text{depth}(N), \text{depth}(N'') + 1\}$
\end{enumerate}
\end{lemma}

\begin{proof}
Utilisons la caractérisation de la profondeur par les groupes Ext
$\Ext^i(\kappa, N)$, voir le Lemme \ref{lemma-depth-ext},
ainsi que la suite exacte longue de cohomologie
$$
\begin{matrix}
0
\to \Hom_R(\kappa, N')
\to \Hom_R(\kappa, N)
\to \Hom_R(\kappa, N'')
\\
\phantom{0\ }
\to \Ext^1_R(\kappa, N')
\to \Ext^1_R(\kappa, N)
\to \Ext^1_R(\kappa, N'')
\to \ldots
\end{matrix}
$$
du Lemme \ref{lemma-long-exact-seq-ext}.
\end{proof}
```

</details>

### 08 — lemma-depth-drops-by-one

Anglais L17939–17959 ; français L17705–17725.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17939) · FR-ALGEBRA-B38-CHOICE-0008.

x appartient à m et est non-diviseur de zéro ; le quotient non nul suit de Nakayama. Diminuer d'au plus1 et d'au moins1 traduit correctement les deux bornes. La seconde clause prolonge une suite régulière jusqu'à la longueur profondeur. Les deux expressions x1,…,xr est une suite sont comprises comme sujet collectif mathématique, non comme un accord pluriel indépendant ; formulation conservée, sans normalisation cosmétique supplémentaire. Peskine16.9–16.10 atteste la baisse et les suites non prolongeables.

Point particulier à relire : Sujet collectif suite compris avec la liste de ses éléments. Aucun besoin mathématique ou linguistique substantiel de récrire cette formulation idiomatique ; la portée locale demeure.

Règles : FR-ALGEBRA-B38-RULE-DEPTH, FR-ALGEBRA-B38-RULE-REGULAR, FR-ALGEBRA-B38-RULE-EXACT, FR-ALGEBRA-B38-RULE-RING, FR-ALGEBRA-B38-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-depth-drops-by-one}
Let $R$ be a local Noetherian ring and $M$ a nonzero finite $R$-module.
\begin{enumerate}
\item If $x \in \mathfrak m$ is a nonzerodivisor on $M$, then
$\text{depth}(M/xM) = \text{depth}(M) - 1$.
\item Any $M$-regular sequence $x_1, \ldots, x_r$ can be extended to an
$M$-regular sequence of length $\text{depth}(M)$.
\end{enumerate}
\end{lemma}

\begin{proof}
Part (2) is a formal consequence of part (1). Let $x \in R$ be as in (1).
By the short exact sequence $0 \to M \to M \to M/xM \to 0$
and Lemma \ref{lemma-depth-in-ses} we see that the depth drops by at most 1.
On the other hand, if $x_1, \ldots, x_r \in \mathfrak m$
is a regular sequence for $M/xM$, then $x, x_1, \ldots, x_r$
is a regular sequence for $M$. Hence we see that the depth drops by
at least 1.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-depth-drops-by-one}
Soit $R$ un anneau local noethérien et $M$ un $R$-module de type fini non nul.
\begin{enumerate}
\item Si $x \in \mathfrak m$ est un non-diviseur de zéro sur $M$, alors
$\text{depth}(M/xM) = \text{depth}(M) - 1$.
\item Toute suite $M$-régulière $x_1, \ldots, x_r$ peut être prolongée en une
suite $M$-régulière de longueur $\text{depth}(M)$.
\end{enumerate}
\end{lemma}

\begin{proof}
La partie (2) est une conséquence formelle de la partie (1). Soit $x \in R$ comme en (1).
La suite exacte courte $0 \to M \to M \to M/xM \to 0$
et le Lemme \ref{lemma-depth-in-ses} montrent que la profondeur diminue d'au plus 1.
D'autre part, si $x_1, \ldots, x_r \in \mathfrak m$
est une suite régulière pour $M/xM$, alors $x, x_1, \ldots, x_r$
est une suite régulière pour $M$. On voit donc que la profondeur diminue
d'au moins 1.
\end{proof}
```

</details>

### 09 — lemma-inherit-minimal-primes

Anglais L17960–17983 ; français L17726–17749.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17960) · FR-ALGEBRA-B38-CHOICE-0009.

Idéal premier associé, minimal au-dessus de p+(x), image et support gardent leurs notions distinctes. L'entier n est existentiel et positif, pas n=1 ni un entier uniforme pour tous x. Toute la preuve Artin-Rees, la surjection, l'annulation et la minimalité dans le support est comparée. La notation de quotient R/p+(x) est ambiguë dans la source et reste telle quelle en français ; observation séparée sans prétendre que le théorème est faux.

Point particulier à relire : Le quotient attendu est R/(p+(x)). La notation sans parenthèses peut servir de raccourci contextuel, mais elle est aussi lisible comme une somme après quotient : observation de notation, non affirmation automatique de fausseté.

Règles : FR-ALGEBRA-B38-RULE-REGULAR, FR-ALGEBRA-B38-RULE-EXACT, FR-ALGEBRA-B38-RULE-PRIME, FR-ALGEBRA-B38-RULE-RING, FR-ALGEBRA-B38-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-inherit-minimal-primes}
Let $(R, \mathfrak m)$ be a local Noetherian ring and $M$ a finite $R$-module.
Let $x \in \mathfrak m$, $\mathfrak p \in \text{Ass}(M)$, and $\mathfrak q$
minimal over $\mathfrak p + (x)$. Then $\mathfrak q \in \text{Ass}(M/x^nM)$
for some $n \geq 1$.
\end{lemma}

\begin{proof}
Pick a submodule $N \subset M$ with $N \cong R/\mathfrak p$.
By the Artin-Rees lemma (Lemma \ref{lemma-Artin-Rees})
we can pick $n > 0$ such that $N \cap x^nM \subset xN$.
Let $\overline{N} \subset M/x^nM$ be the image of $N \to M \to M/x^nM$.
By Lemma \ref{lemma-ass} it suffices to show
$\mathfrak q \in \text{Ass}(\overline{N})$.
By our choice of $n$ there is a surjection
$\overline{N} \to N/xN = R/\mathfrak p + (x)$
and hence $\mathfrak q$ is in the support of $\overline{N}$.
Since $\overline{N}$ is annihilated by $x^n$ and $\mathfrak p$ we see that
$\mathfrak q$ is minimal among the primes in the support of $\overline{N}$.
Thus $\mathfrak q$ is an associated prime of $\overline{N}$ by
Lemma \ref{lemma-ass-minimal-prime-support}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-inherit-minimal-primes}
Soit $(R, \mathfrak m)$ un anneau local noethérien et $M$ un $R$-module de type fini.
Soient $x \in \mathfrak m$, $\mathfrak p \in \text{Ass}(M)$, et $\mathfrak q$
minimal au-dessus de $\mathfrak p + (x)$. Alors $\mathfrak q \in \text{Ass}(M/x^nM)$
pour un certain $n \geq 1$.
\end{lemma}

\begin{proof}
Choisissons un sous-module $N \subset M$ tel que $N \cong R/\mathfrak p$.
D'après le lemme d'Artin-Rees (Lemme \ref{lemma-Artin-Rees}),
on peut choisir $n > 0$ tel que $N \cap x^nM \subset xN$.
Soit $\overline{N} \subset M/x^nM$ l'image de $N \to M \to M/x^nM$.
D'après le Lemme \ref{lemma-ass}, il suffit de montrer que
$\mathfrak q \in \text{Ass}(\overline{N})$.
Par notre choix de $n$, il existe une surjection
$\overline{N} \to N/xN = R/\mathfrak p + (x)$,
et donc $\mathfrak q$ appartient au support de $\overline{N}$.
Puisque $\overline{N}$ est annulé par $x^n$ et $\mathfrak p$, on voit que
$\mathfrak q$ est minimal parmi les idéaux premiers du support de $\overline{N}$.
Ainsi $\mathfrak q$ est un idéal premier associé à $\overline{N}$ d'après le
Lemme \ref{lemma-ass-minimal-prime-support}.
\end{proof}
```

</details>

### 10 — lemma-depth-dim-associated-primes

Anglais L17984–18021 ; français L17750–17787.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L17984) · FR-ALGEBRA-B38-CHOICE-0010.

Chaque p associé vérifie la borne de dimension. Les cas profondeur0/1 et toute la récurrence, le choix de q, l'indication omise et le passage par x^n sont conservés. Peskine16.11 donne exactement le registre de la borne par dim(A/P). On gagne devient ce qui conclut, de même fonction argumentative, sans ajouter une nouvelle conséquence. La seconde notation R/p+(x) reste diplomatique et liée à l'observation précédente.

Règles : FR-ALGEBRA-B38-RULE-DEPTH, FR-ALGEBRA-B38-RULE-REGULAR, FR-ALGEBRA-B38-RULE-PRIME, FR-ALGEBRA-B38-RULE-RING, FR-ALGEBRA-B38-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-depth-dim-associated-primes}
Let $(R, \mathfrak m)$ be a local Noetherian ring and $M$ a finite $R$-module.
For $\mathfrak p \in \text{Ass}(M)$ we have
$\dim(R/\mathfrak p) \geq \text{depth}(M)$.
\end{lemma}

\begin{proof}
If $\mathfrak m \in \text{Ass}(M)$ then there is a nonzero element
$x \in M$ which is annihilated by all elements of $\mathfrak m$.
Thus $\text{depth}(M) = 0$. In particular the lemma holds in this case.

\medskip\noindent
If $\text{depth}(M) = 1$, then by the first paragraph
we find that $\mathfrak m \not \in \text{Ass}(M)$.
Hence $\dim(R/\mathfrak p) \geq 1$ for all $\mathfrak p \in \text{Ass}(M)$
and the lemma is true in this case as well.

\medskip\noindent
We will prove the lemma in general by induction on $\text{depth}(M)$
which we may and do assume to be $> 1$. Pick $x \in \mathfrak m$ which
is a nonzerodivisor on $M$. Note $x \not \in \mathfrak p$
(Lemma \ref{lemma-ass-zero-divisors}).
By Lemma \ref{lemma-one-equation} we have
$\dim(R/\mathfrak p + (x)) = \dim(R/\mathfrak p) - 1$.
Thus there exists a prime $\mathfrak q$ minimal over $\mathfrak p + (x)$ with
$\dim(R/\mathfrak q) = \dim(R/\mathfrak p) - 1$ (small argument omitted;
hint: the dimension of a Noetherian local ring $A$ is the maximum
of the dimensions of $A/\mathfrak r$ taken over the minimal
primes $\mathfrak r$ of $A$). Pick $n$ as in
Lemma \ref{lemma-inherit-minimal-primes} so that
$\mathfrak q$ is an associated prime of $M/x^nM$.
We may apply induction hypothesis to $M/x^nM$ and $\mathfrak q$
because $\text{depth}(M/x^nM) = \text{depth}(M) - 1$ by
Lemma \ref{lemma-depth-drops-by-one}. We find
$\dim(R/\mathfrak q) \geq \text{depth}(M/x^nM)$ and we win.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-depth-dim-associated-primes}
Soit $(R, \mathfrak m)$ un anneau local noethérien et $M$ un $R$-module de type fini.
Pour $\mathfrak p \in \text{Ass}(M)$, on a
$\dim(R/\mathfrak p) \geq \text{depth}(M)$.
\end{lemma}

\begin{proof}
Si $\mathfrak m \in \text{Ass}(M)$, il existe un élément non nul
$x \in M$ annulé par tous les éléments de $\mathfrak m$.
Ainsi $\text{depth}(M) = 0$. En particulier, le lemme est vrai dans ce cas.

\medskip\noindent
Si $\text{depth}(M) = 1$, alors le premier paragraphe
montre que $\mathfrak m \not \in \text{Ass}(M)$.
Ainsi $\dim(R/\mathfrak p) \geq 1$ pour tout $\mathfrak p \in \text{Ass}(M)$,
et le lemme est encore vrai dans ce cas.

\medskip\noindent
Démontrons le lemme en général par récurrence sur $\text{depth}(M)$,
que l'on peut et va supposer $> 1$. Choisissons $x \in \mathfrak m$ qui soit
un non-diviseur de zéro sur $M$. Remarquons que $x \not \in \mathfrak p$
(Lemme \ref{lemma-ass-zero-divisors}).
D'après le Lemme \ref{lemma-one-equation}, on a
$\dim(R/\mathfrak p + (x)) = \dim(R/\mathfrak p) - 1$.
Il existe donc un idéal premier $\mathfrak q$ minimal au-dessus de $\mathfrak p + (x)$ tel que
$\dim(R/\mathfrak q) = \dim(R/\mathfrak p) - 1$ (petit argument omis ;
indication : la dimension d'un anneau local noethérien $A$ est le maximum
des dimensions de $A/\mathfrak r$ lorsque $\mathfrak r$ parcourt les idéaux premiers
minimaux de $A$). Choisissons $n$ comme dans le
Lemme \ref{lemma-inherit-minimal-primes}, de sorte que
$\mathfrak q$ soit un idéal premier associé à $M/x^nM$.
On peut appliquer l'hypothèse de récurrence à $M/x^nM$ et $\mathfrak q$,
car $\text{depth}(M/x^nM) = \text{depth}(M) - 1$ d'après le
Lemme \ref{lemma-depth-drops-by-one}. On obtient
$\dim(R/\mathfrak q) \geq \text{depth}(M/x^nM)$, ce qui conclut.
\end{proof}
```

</details>

### 11 — lemma-depth-localization

Anglais L18022–18046 ; français L17788–17812.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18022) · FR-ALGEBRA-B38-CHOICE-0011.

La somme profondeur locale plus dim(R/p) majore la profondeur de M. Cas M_p nul, comparaison déjà satisfaite et choix de x sont intégralement comparés. La condition M_p non nul pour sa perte d'une unité demeure explicite. Pour M nul, le premier cas suffit ; pour M non nul la profondeur est finie et la récurrence est légitime. Pas d'égalité ni de monotonie isolée ajoutée.

Règles : FR-ALGEBRA-B38-RULE-REGULAR, FR-ALGEBRA-B38-RULE-PRIME, FR-ALGEBRA-B38-RULE-RING, FR-ALGEBRA-B38-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-depth-localization}
Let $R$ be a local Noetherian ring and $M$ a finite $R$-module.
For a prime ideal $\mathfrak p \subset R$ we have
$\text{depth}(M_\mathfrak p) + \dim(R/\mathfrak p) \geq \text{depth}(M)$.
\end{lemma}

\begin{proof}
If $M_\mathfrak p = 0$, then $\text{depth}(M_\mathfrak p) = \infty$ and
the lemma holds.
If $\text{depth}(M) \leq \dim(R/\mathfrak p)$, then the lemma is true.
If $\text{depth}(M) > \dim(R/\mathfrak p)$, then $\mathfrak p$ is not
contained in any associated prime $\mathfrak q$ of $M$ by
Lemma \ref{lemma-depth-dim-associated-primes}.
Hence we can find an $x \in \mathfrak p$ not contained in any
associated prime of $M$ by Lemma \ref{lemma-silly} and
Lemma \ref{lemma-finite-ass}. Then $x$ is a nonzerodivisor
on $M$, see Lemma \ref{lemma-ass-zero-divisors}.
Hence $\text{depth}(M/xM) = \text{depth}(M) - 1$ and
$\text{depth}(M_\mathfrak p / x M_\mathfrak p) =
\text{depth}(M_\mathfrak p) - 1$ provided $M_\mathfrak p$ is nonzero,
see Lemma \ref{lemma-depth-drops-by-one}.
Thus we conclude by induction on $\text{depth}(M)$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-depth-localization}
Soit $R$ un anneau local noethérien et $M$ un $R$-module de type fini.
Pour un idéal premier $\mathfrak p \subset R$, on a
$\text{depth}(M_\mathfrak p) + \dim(R/\mathfrak p) \geq \text{depth}(M)$.
\end{lemma}

\begin{proof}
Si $M_\mathfrak p = 0$, alors $\text{depth}(M_\mathfrak p) = \infty$, et
le lemme est établi.
Si $\text{depth}(M) \leq \dim(R/\mathfrak p)$, alors le lemme est vrai.
Si $\text{depth}(M) > \dim(R/\mathfrak p)$, alors $\mathfrak p$ n'est contenu
dans aucun idéal premier associé $\mathfrak q$ à $M$, d'après le
Lemme \ref{lemma-depth-dim-associated-primes}.
On peut donc trouver $x \in \mathfrak p$ qui n'appartient à aucun
idéal premier associé à $M$, d'après le Lemme \ref{lemma-silly} et le
Lemme \ref{lemma-finite-ass}. Alors $x$ est un non-diviseur de zéro
sur $M$ ; voir le Lemme \ref{lemma-ass-zero-divisors}.
Ainsi $\text{depth}(M/xM) = \text{depth}(M) - 1$ et
$\text{depth}(M_\mathfrak p / x M_\mathfrak p) =
\text{depth}(M_\mathfrak p) - 1$, pourvu que $M_\mathfrak p$ soit non nul ;
voir le Lemme \ref{lemma-depth-drops-by-one}.
On conclut donc par récurrence sur $\text{depth}(M)$.
\end{proof}
```

</details>

### 12 — lemma-depth-goes-down-finite

Anglais L18047–18086 ; français L17813–17852.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18047) · FR-ALGEBRA-B38-CHOICE-0012.

Homomorphisme fini d'anneaux ne signifie pas corps finis ni morphisme à fibres seules finies. Chaque profondeur gauche est prise sur le S localisé à m_i, alors que profondeur_m(N) à droite traite N comme R-module. Les idéaux maximaux au-dessus de m, leurs contractions associées, le cas0 et la perte d'une unité sont comparés. La preuve est écrite par récurrence sur k ; son cas∞ pour N nul et sa convention pour S nul sont signalés comme précisions source nécessaires, sans inventer une réparation française ni un contre-exemple au cas non nul.

Point particulier à relire : Pour N=0, toutes les profondeurs valent∞ et l'égalité est immédiate si le minimum porte sur une famille non vide ; une récurrence ordinaire sur∞ n'est pas une preuve. Pour S=0, la famille des idéaux maximaux est vide et la convention min vide=∞ doit être annoncée si ce cas est permis. Aucun de ces cas n'est exclu silencieusement de l'énoncé.

Règles : FR-ALGEBRA-B38-RULE-DEPTH, FR-ALGEBRA-B38-RULE-REGULAR, FR-ALGEBRA-B38-RULE-EXACT, FR-ALGEBRA-B38-RULE-PRIME, FR-ALGEBRA-B38-RULE-RING, FR-ALGEBRA-B38-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-depth-goes-down-finite}
Let $(R, \mathfrak m)$ be a Noetherian local ring. Let $R \to S$
be a finite ring map. Let $\mathfrak m_1, \ldots, \mathfrak m_n$
be the maximal ideals of $S$. Let $N$ be a finite $S$-module.
Then
$$
\min\nolimits_{i = 1, \ldots, n} \text{depth}(N_{\mathfrak m_i}) =
\text{depth}_\mathfrak m(N)
$$
\end{lemma}

\begin{proof}
By Lemmas \ref{lemma-integral-no-inclusion}, \ref{lemma-integral-going-up},
and Lemma \ref{lemma-finite-finite-fibres} the maximal ideals of
$S$ are exactly the primes of $S$ lying over $\mathfrak m$ and
there are finitely many of them. Hence the statement of the lemma
makes sense. We will prove the lemma by induction on
$k = \min\nolimits_{i = 1, \ldots, n} \text{depth}(N_{\mathfrak m_i})$.
If $k = 0$, then $\text{depth}(N_{\mathfrak m_i}) = 0$ for some $i$.
By Lemma \ref{lemma-depth-ext} this means
$\mathfrak m_i S_{\mathfrak m_i}$ is an associated prime
of $N_{\mathfrak m_i}$ and hence $\mathfrak m_i$ is an
associated prime of $N$ (Lemma \ref{lemma-localize-ass}).
By Lemma \ref{lemma-ass-functorial-Noetherian} we see that
$\mathfrak m$ is an associated prime of $N$ as an $R$-module.
Whence $\text{depth}_\mathfrak m(N) = 0$. This proves the base case.
If $k > 0$, then we see that $\mathfrak m_i \not \in \text{Ass}_S(N)$.
Hence $\mathfrak m \not \in \text{Ass}_R(N)$, again by
Lemma \ref{lemma-ass-functorial-Noetherian}.
Thus we can find $f \in \mathfrak m$ which is not a zerodivisor on
$N$, see Lemma \ref{lemma-ideal-nonzerodivisor}. By
Lemma \ref{lemma-depth-drops-by-one}
all the depths drop exactly by $1$ when passing from $N$ to
$N/fN$ and the induction hypothesis does the rest.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-depth-goes-down-finite}
Soit $(R, \mathfrak m)$ un anneau local noethérien. Soit $R \to S$
un homomorphisme fini d'anneaux. Soient $\mathfrak m_1, \ldots, \mathfrak m_n$
les idéaux maximaux de $S$. Soit $N$ un $S$-module de type fini.
Alors
$$
\min\nolimits_{i = 1, \ldots, n} \text{depth}(N_{\mathfrak m_i}) =
\text{depth}_\mathfrak m(N)
$$
\end{lemma}

\begin{proof}
D'après les Lemmes \ref{lemma-integral-no-inclusion}, \ref{lemma-integral-going-up},
et le Lemme \ref{lemma-finite-finite-fibres}, les idéaux maximaux de
$S$ sont exactement les idéaux premiers de $S$ au-dessus de $\mathfrak m$, et
ils sont en nombre fini. L'énoncé du lemme a donc
un sens. Nous allons démontrer le lemme par récurrence sur
$k = \min\nolimits_{i = 1, \ldots, n} \text{depth}(N_{\mathfrak m_i})$.
Si $k = 0$, alors $\text{depth}(N_{\mathfrak m_i}) = 0$ pour un certain $i$.
D'après le Lemme \ref{lemma-depth-ext}, cela signifie que
$\mathfrak m_i S_{\mathfrak m_i}$ est un idéal premier associé
à $N_{\mathfrak m_i}$, et donc que $\mathfrak m_i$ est un
idéal premier associé à $N$ (Lemme \ref{lemma-localize-ass}).
D'après le Lemme \ref{lemma-ass-functorial-Noetherian}, on voit que
$\mathfrak m$ est un idéal premier associé à $N$ comme $R$-module.
Ainsi $\text{depth}_\mathfrak m(N) = 0$. Cela établit le cas initial.
Si $k > 0$, alors $\mathfrak m_i \not \in \text{Ass}_S(N)$.
Ainsi $\mathfrak m \not \in \text{Ass}_R(N)$, encore d'après le
Lemme \ref{lemma-ass-functorial-Noetherian}.
On peut donc trouver $f \in \mathfrak m$ qui n'est pas un diviseur de zéro sur
$N$ ; voir le Lemme \ref{lemma-ideal-nonzerodivisor}. D'après le
Lemme \ref{lemma-depth-drops-by-one},
toutes les profondeurs diminuent exactement de $1$ lorsque l'on passe de $N$ à
$N/fN$, et l'hypothèse de récurrence conclut.
\end{proof}
```

</details>

## Contrôles et suite

Les 254 régions mathématiques nouvelles sont exactement identiques. Le préfixe de 12 847 régions passe avec quarante-trois exceptions linguistiques antérieures précisément recensées dans leur ordre et avec leurs multiplicités.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items sont identiques. Aucun titre facultatif ni citation dans ce lot. Le fichier conserve tous les octets du lot précédent et son inverse complet retrouve le témoin public préservé.

Les 656 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Fonctorialités de Ext, anglais L18087 /français L17853. Aucun PDF nouveau ni publication ; restauration globale en cours.

