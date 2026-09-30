# Fonctorialités de Ext et application au scindage

## Résultat et portée

Comparaison complète : anglais L18087–18214 /français L17853–17980, 128 lignes chacun, quatre paires et 71 occurrences contextualisées. Couverture continue : 74 sections, 660 paires et 6816 occurrences. Ni le chapitre ni l’édition ne sont terminés.

Deux raccords de phrase autour des formules sont réparés en français. Les formules et tous les arguments restent identiques ; aucune correction du résultat anglais n’est ajoutée.

Trois observations anglaises de dénomination, article et ponctuation sont séparées. Elles ne sont ni admises au registre ni incorporées clandestinement dans les mathématiques françaises.

Lecture produite par OpenAI Codex, sans relecture humaine. Ultra est demandé par les instructions ; aucun identifiant exact de modèle n’est attesté par une métadonnée consultée ici. Le canon est consulté rétrospectivement, non présenté comme consulté lors de la traduction initiale.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX réparé](staged/fr/010_algebra.prose-batch39.fr.tex) · [Dossier précédent](ALGEBRA_PROSE_BATCH38_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH39_VALIDATION.json) · [Choix justifiés](ALGEBRA_PROSE_BATCH39_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH39_OCCURRENCES.json) · [Opérations](ALGEBRA_PROSE_BATCH39_REPAIRS.json) · [Texte dans les formules](ALGEBRA_PROSE_BATCH39_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH39_CITATION_EXCEPTIONS.json) · [Titres facultatifs](ALGEBRA_PROSE_BATCH39_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH39_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH39_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Yves Laszlo — Introduction à l'algèbre commutative et homologique, maîtrise2003–2004

[Source consultée](https://www.cmls.polytechnique.fr/perso/laszlo/maitrise/maitrisefin.pdf) · [Fichier conservé](canon-consulted/fr-algebra/laszlo-commutative-homologique-2003.pdf)

Page PDF/imprimée19 entièrement lue maintenant : sections19/20, définition19.1 et lemme19.3. Pages67–68 et71–73 entièrement relues maintenant. Les autres pages1,16,64–66,69–70,77–79 ont été lues dans ce même tour pour B37 et sont réutilisées explicitement, sans inventer une consultation par le traducteur initial.

Attestations courtes : « résolution libre », « suite exacte courte », « Scindages », « est dite scindée ».

Atteste résolution, exactitude, fonctorialité et type fini ; la définition19.1 explique le scindage par une section et19.3 la somme directe. Ces usages appuient le français de la rétraction et des suites du présent lot.

Limites : Consultation rétrospective. Le changement d'anneau Ext et le théorème de scindage I-adique sont vérifiés sur la source officielle, non prétendus établis par ces pages. Les indices et erreurs propres à ce manuel ne sont pas adoptés. Définition19.1 porte directement sur la suite scindée ; injection scindée est l'expression pour sa flèche gauche possédant une rétraction. Aucune relecture humaine.

SHA-256 : 6CE611DFE7265C9658269EEE371803873B6ECEA26FEAC86E3455075F8D0A6D79.

## Modifications et motifs

La phrase Cela implique que… est continuait après un point ; elle devient On obtient la suite exacte courte…, avec la formule inchangée. Le fragment pour cet entier n devient une phrase complète qui précise que cette inclusion vaut pour le même n. Ces réparations de syntaxe ne changent pas l’exactitude ni l’obstruction au scindage.

### FR-ALGEBRA-B39-REPAIR-0001

Anglais L18174 ; français L17940.

Avant :
```tex
Cela implique que
$$
0 \to N/I^nN \to M/I^nM \to Q/I^nQ \to 0.
$$
est encore une suite exacte courte. De plus, la suite
```

Après :
```tex
On obtient la suite exacte courte
$$
0 \to N/I^nN \to M/I^nM \to Q/I^nQ \to 0.
$$
De plus, la suite
```

Anneau noethérien, I dans le radical de Jacobson, modules de type fini et entiers n arbitrairement grands sont tous essentiels et conservés. Injection scindée signifie rétraction R-linéaire de l'injection ; Laszlo19.1/19.3 atteste le scindage d'une suite exacte et sa décomposition. Le noyau est nul par intersection des I^nN, puis la classe d'extension dans Ext^1(Q,N) est l'obstruction. Les relèvements de gamma_n, l'image Hom plus I^nHom et la finitude du conoyau sont vérifiés ; arbitrairement grand n ne devient ni tout n ni un système compatible. Résolution libre de type fini décrit ici des termes libres de rang fini, sans affirmer une résolution bornée de tous les modules. Deux raccords de phrases françaises autour de formules sont réparés sans changer les formules, la portée ni le raisonnement.

La suite après réduction est exacte parce que l'injection réduite est supposée scindée ; ce n'est pas une affirmation d'exactitude à gauche de toute réduction. La résolution de type fini ne signifie pas nécessairement de longueur finie. Le contexte détermine chaque rang fini. La preuve ne requiert aucune compatibilité préalable des scindages pour différents n.

### FR-ALGEBRA-B39-REPAIR-0002

Anglais L18194 ; français L17960.

Avant :
```tex
pour cet entier $n$.
```

Après :
```tex
Cette inclusion vaut pour cet entier $n$.
```

Anneau noethérien, I dans le radical de Jacobson, modules de type fini et entiers n arbitrairement grands sont tous essentiels et conservés. Injection scindée signifie rétraction R-linéaire de l'injection ; Laszlo19.1/19.3 atteste le scindage d'une suite exacte et sa décomposition. Le noyau est nul par intersection des I^nN, puis la classe d'extension dans Ext^1(Q,N) est l'obstruction. Les relèvements de gamma_n, l'image Hom plus I^nHom et la finitude du conoyau sont vérifiés ; arbitrairement grand n ne devient ni tout n ni un système compatible. Résolution libre de type fini décrit ici des termes libres de rang fini, sans affirmer une résolution bornée de tous les modules. Deux raccords de phrases françaises autour de formules sont réparés sans changer les formules, la portée ni le raisonnement.

La suite après réduction est exacte parce que l'injection réduite est supposée scindée ; ce n'est pas une affirmation d'exactitude à gauche de toute réduction. La résolution de type fini ne signifie pas nécessairement de longueur finie. Le contexte détermine chaque rang fini. La preuve ne requiert aucune compatibilité préalable des scindages pour différents n.

## Observations séparées sur la source

Homology dans le calcul des Ext, article omis et ponctuation interrompant les phrases sont documentés séparément. Aucun résultat faux n’est prétendu par ces seuls points ; aucune admission, déduplication globale ou première découverte n’est revendiquée.

### lemma-flat-base-change-ext

[Anglais officiel L18125](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18125) · FR-ALGEBRA-B39-SOURCE-NOTE-0001.

```tex
induces an isomorphism on homology groups
```

Le complexe Hom de la résolution libre est cohomologique et calcule Ext^i. Homology est donc une dénomination impropre si l'on distingue les deux conventions ; le mot attendu serait cohomology. Le français garde groupes d'homologie, en accord avec la source. Aucune flèche ni groupe n'est changé ; réserve de dénomination, pas revendication d'un théorème faux.

Confiance forte sur la convention du complexe ; observation séparée, aucune admission.

### lemma-split-injection-after-completion

[Anglais officiel L18156](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18156) · FR-ALGEBRA-B39-SOURCE-NOTE-0002.

```tex
is injection.
```

La source omet l'article devant injection ; is an injection ou is injective sont grammaticaux. Le français est injectif est déjà correct et reste inchangé. Observation grammaticale anglaise seulement.

Confiance forte, observation séparée sans admission ni première découverte.

### lemma-split-injection-after-completion

[Anglais officiel L18176](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18176) · FR-ALGEBRA-B39-SOURCE-NOTE-0003.

```tex
0 \to N/I^nN \to M/I^nM \to Q/I^nQ \to 0.
$$
is still short exact.
```

La source place un point dans la formule puis poursuit par is still short exact ; plus loin, le point dans la formule beta laisse for this n isolé. Le français réorganise les raccords de phrase autour des formules, qui restent exactement identiques. Il s'agit de ponctuation et de syntaxe, non d'une objection à l'exactitude ou à l'inclusion démontrée.

Confiance forte sur le raccord syntaxique ; mathématiques conservées, aucune admission.

[Pièce primaire algebra.tex L18191–18194](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18191)
SHA-256 du fichier : FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.

```tex
\beta \in
\Im\Big(\Hom_R(F_0, N) \to \Hom_R(F_1, N)\Big) + I^n\Hom_R(F_1, N).
$$
for this $n$.
```

## Règles contextualisées

### FR-ALGEBRA-B39-RULE-EXT

Les deux arguments, les anneaux de linéarité et les changements de scalaires sont vérifiés dans chaque passage entier.

Canon : FR-ALGEBRA-B39-CANON-LASZLO.

### FR-ALGEBRA-B39-RULE-EXACT

Plat ne devient pas fidèlement plat ; résolution de type fini ne devient pas résolution de longueur finie. L'exactitude réduite utilise l'hypothèse d'injection scindée.

Canon : FR-ALGEBRA-B39-CANON-LASZLO.

### FR-ALGEBRA-B39-RULE-SPLIT

Injection scindée et extension scindée sont confrontées aux rétractions, à la classe Ext et au diagramme complet, pas assimilées à une simple injection.

Canon : FR-ALGEBRA-B39-CANON-LASZLO.

### FR-ALGEBRA-B39-RULE-RING

Finitude des modules est attestée ; noethérianité et radical de Jacobson sont conservés comme hypothèses explicites de la source, pas revendiqués comme attestés dans les seules pages de scindage.

Canon : FR-ALGEBRA-B39-CANON-LASZLO.

### FR-ALGEBRA-B39-RULE-LOGIC

Portée conditionnelle, arbitrairement grands et obstruction équivalente sont directement vérifiés ; les raccords grammaticaux réparent le français, non les théorèmes.

Canon : Analyse source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-functoriality-ext

Anglais L18087–18105 ; français L17853–17871.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18087) · FR-ALGEBRA-B39-CHOICE-0001.

Fonctorialité, changement d'anneau, structure de module et homomorphisme canonique sont distingués. La liste source est annoncée comme des points à développer, non comme deux théorèmes nouveaux prouvés ici. L'homomorphisme du premier point est R'-linéaire ; celui du second est R-linéaire. Les domaines, codomaines et les deux arguments Ext sont comparés intégralement.

Règles : FR-ALGEBRA-B39-RULE-EXT, FR-ALGEBRA-B39-RULE-RING.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Functorialities for Ext}
\label{section-functoriality-ext}

\noindent
In this section we briefly discuss the functoriality
of $\Ext$ with respect to change of ring, etc.
Here is a list of items to work out.
\begin{enumerate}
\item Given $R \to R'$, an $R$-module
$M$ and an $R'$-module $N'$
the $R$-module $\Ext^i_R(M, N')$
has a natural $R'$-module structure. Moreover, there is a
canonical $R'$-linear map $\Ext^i_{R'}(M \otimes_R R', N') \to
\Ext^i_R(M, N')$.
\item Given $R \to R'$ and $R$-modules $M$, $N$ there is a natural
$R$-module map
$\Ext^i_R(M, N) \to \text{Ext}^i_R(M, N \otimes_R R')$.
\end{enumerate}
```

Français restauré :
```tex
\section{Fonctorialités de Ext}
\label{section-functoriality-ext}

\noindent
Dans cette section, nous examinons brièvement la fonctorialité
de $\Ext$ par rapport au changement d'anneau, etc.
Voici une liste de points à développer.
\begin{enumerate}
\item Étant donnés $R \to R'$, un $R$-module
$M$ et un $R'$-module $N'$,
le $R$-module $\Ext^i_R(M, N')$
possède une structure naturelle de $R'$-module. De plus, il existe un
homomorphisme canonique $R'$-linéaire $\Ext^i_{R'}(M \otimes_R R', N') \to
\Ext^i_R(M, N')$.
\item Étant donnés $R \to R'$ et des $R$-modules $M$, $N$, il existe un
homomorphisme naturel de $R$-modules
$\Ext^i_R(M, N) \to \text{Ext}^i_R(M, N \otimes_R R')$.
\end{enumerate}
```

</details>

### 02 — lemma-flat-base-change-ext

Anglais L18106–18134 ; français L17872–17900.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18106) · FR-ALGEBRA-B39-CHOICE-0002.

L'homomorphisme d'anneaux est plat, pas nécessairement fidèlement plat. Aucun module de type fini n'est imposé. La résolution libre tensorisée reste une résolution par platitude, et l'adjonction extension/restriction des scalaires donne un isomorphisme de complexes. Chaque formule et le degré i≥0 sont conservés. Laszlo atteste résolution libre, isomorphisme de complexes et le registre exact ; sa convention cohomologique n'est pas substituée au mot homology de Stacks. Le décalage de dénomination est signalé séparément.

Point particulier à relire : La source dit groupes d'homologie pour un complexe Hom qui calcule Ext en cohomologie. Le français traduit fidèlement cette dénomination et ne répare pas silencieusement la source.

Règles : FR-ALGEBRA-B39-RULE-EXT, FR-ALGEBRA-B39-RULE-EXACT, FR-ALGEBRA-B39-RULE-RING.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-flat-base-change-ext}
Given a flat ring map $R \to R'$, an $R$-module $M$, and an
$R'$-module $N'$ the natural map
$$
\Ext^i_{R'}(M \otimes_R R', N') \to \text{Ext}^i_R(M, N')
$$
is an isomorphism for $i \geq 0$.
\end{lemma}

\begin{proof}
Choose a free resolution $F_\bullet$ of $M$.
Since $R \to R'$ is flat we see that $F_\bullet \otimes_R R'$ is
a free resolution of $M \otimes_R R'$ over $R'$.
The statement is that the map
$$
\Hom_{R'}(F_\bullet \otimes_R R', N') \to
\Hom_R(F_\bullet, N')
$$
induces an isomorphism on homology groups, which is true because
it is an isomorphism of complexes by
Lemma \ref{lemma-adjoint-tensor-restrict}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-flat-base-change-ext}
Étant donnés un homomorphisme plat d'anneaux $R \to R'$, un $R$-module $M$ et un
$R'$-module $N'$, l'homomorphisme naturel
$$
\Ext^i_{R'}(M \otimes_R R', N') \to \text{Ext}^i_R(M, N')
$$
est un isomorphisme pour $i \geq 0$.
\end{lemma}

\begin{proof}
Choisissons une résolution libre $F_\bullet$ de $M$.
Comme $R \to R'$ est plat, $F_\bullet \otimes_R R'$ est
une résolution libre de $M \otimes_R R'$ sur $R'$.
L'énoncé affirme que l'homomorphisme
$$
\Hom_{R'}(F_\bullet \otimes_R R', N') \to
\Hom_R(F_\bullet, N')
$$
induit un isomorphisme sur les groupes d'homologie, ce qui est vrai puisqu'il
est un isomorphisme de complexes d'après le
Lemme \ref{lemma-adjoint-tensor-restrict}.
\end{proof}
```

</details>

### 03 — section-ext-application

Anglais L18135–18140 ; français L17901–17906.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18135) · FR-ALGEBRA-B39-CHOICE-0003.

Le titre et La voici traduisent l'introduction sans ajouter de théorème, d'application géométrique ou de commentaire pédagogique absent. Les groupes Ext restent le nom propre de la construction.

Règles : FR-ALGEBRA-B39-RULE-EXT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{An application of Ext groups}
\label{section-ext-application}

\noindent
Here it is.
```

Français restauré :
```tex
\section{Une application des groupes Ext}
\label{section-ext-application}

\noindent
La voici.
```

</details>

### 04 — lemma-split-injection-after-completion

Anglais L18141–18214 ; français L17907–17980.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L18141) · FR-ALGEBRA-B39-CHOICE-0004.

Anneau noethérien, I dans le radical de Jacobson, modules de type fini et entiers n arbitrairement grands sont tous essentiels et conservés. Injection scindée signifie rétraction R-linéaire de l'injection ; Laszlo19.1/19.3 atteste le scindage d'une suite exacte et sa décomposition. Le noyau est nul par intersection des I^nN, puis la classe d'extension dans Ext^1(Q,N) est l'obstruction. Les relèvements de gamma_n, l'image Hom plus I^nHom et la finitude du conoyau sont vérifiés ; arbitrairement grand n ne devient ni tout n ni un système compatible. Résolution libre de type fini décrit ici des termes libres de rang fini, sans affirmer une résolution bornée de tous les modules. Deux raccords de phrases françaises autour de formules sont réparés sans changer les formules, la portée ni le raisonnement.

Point particulier à relire : La suite après réduction est exacte parce que l'injection réduite est supposée scindée ; ce n'est pas une affirmation d'exactitude à gauche de toute réduction. La résolution de type fini ne signifie pas nécessairement de longueur finie. Le contexte détermine chaque rang fini. La preuve ne requiert aucune compatibilité préalable des scindages pour différents n.

Règles : FR-ALGEBRA-B39-RULE-EXACT, FR-ALGEBRA-B39-RULE-SPLIT, FR-ALGEBRA-B39-RULE-RING, FR-ALGEBRA-B39-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-split-injection-after-completion}
Let $R$ be a Noetherian ring. Let $I \subset R$ be an ideal
contained in the Jacobson radical of $R$.
Let $N \to M$ be a homomorphism of finite $R$-modules.
Suppose that there exists arbitrarily large $n$ such that
$N/I^nN \to M/I^nM$ is a split injection.
Then $N \to M$ is a split injection.
\end{lemma}

\begin{proof}
Assume $\varphi : N \to M$ satisfies the assumptions of the lemma.
Note that this implies that $\Ker(\varphi) \subset I^nN$
for arbitrarily large $n$. Hence by
Lemma \ref{lemma-intersection-powers-ideal-module} we see that $\varphi$
is injection. Let $Q = M/N$ so that we have a short exact sequence
$$
0 \to N \to M \to Q \to 0.
$$
Let
$$
F_2 \xrightarrow{d_2} F_1 \xrightarrow{d_1} F_0 \to Q \to 0
$$
be a finite free resolution of $Q$. We can choose a map
$\alpha : F_0 \to M$ lifting the map $F_0 \to Q$. This induces a map
$\beta : F_1 \to N$ such that $\beta \circ d_2 = 0$. The extension
above is split if and only if there exists a map $\gamma : F_0 \to N$
such that $\beta = \gamma \circ d_1$. In other words, the class of
$\beta$ in $\Ext^1_R(Q, N)$ is the obstruction to splitting
the short exact sequence above.

\medskip\noindent
Suppose $n$ is a large integer such that $N/I^nN \to M/I^nM$ is a
split injection. This implies
$$
0 \to N/I^nN \to M/I^nM \to Q/I^nQ \to 0.
$$
is still short exact. Also, the sequence
$$
F_1/I^nF_1 \xrightarrow{d_1} F_0/I^nF_0 \to Q/I^nQ \to 0
$$
is still exact. Arguing as above we see that the map
$\overline{\beta} : F_1/I^nF_1 \to N/I^nN$
induced by $\beta$ is equal to $\overline{\gamma_n} \circ d_1$ for some
map $\overline{\gamma_n} : F_0/I^nF_0 \to N/I^nN$.
Since $F_0$ is free we can lift $\overline{\gamma_n}$ to a map
$\gamma_n : F_0 \to N$ and then we see that
$\beta - \gamma_n \circ d_1$ is a map from $F_1$ into $I^nN$.
In other words we conclude that
$$
\beta \in
\Im\Big(\Hom_R(F_0, N) \to \Hom_R(F_1, N)\Big) + I^n\Hom_R(F_1, N).
$$
for this $n$.

\medskip\noindent
Since we have this property for arbitrarily large $n$ by assumption
we conclude that the image of $\beta$ in the cokernel of
$\Hom_R(F_0, N) \to \Hom_R(F_1, N)$ is zero by 
Lemma \ref{lemma-intersection-powers-ideal-module}. Hence
$\beta$ is in the image of the map $\Hom_R(F_0, N) \to \Hom_R(F_1, N)$ as
desired.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-split-injection-after-completion}
Soit $R$ un anneau noethérien. Soit $I \subset R$ un idéal
contenu dans le radical de Jacobson de $R$.
Soit $N \to M$ un homomorphisme de $R$-modules de type fini.
Supposons qu'il existe des entiers $n$ arbitrairement grands tels que
$N/I^nN \to M/I^nM$ soit une injection scindée.
Alors $N \to M$ est une injection scindée.
\end{lemma}

\begin{proof}
Supposons que $\varphi : N \to M$ satisfasse les hypothèses du lemme.
Remarquons que cela implique $\Ker(\varphi) \subset I^nN$
pour des entiers $n$ arbitrairement grands. Ainsi, d'après le
Lemme \ref{lemma-intersection-powers-ideal-module}, on voit que $\varphi$
est injectif. Posons $Q = M/N$, de sorte que l'on ait une suite exacte courte
$$
0 \to N \to M \to Q \to 0.
$$
Soit
$$
F_2 \xrightarrow{d_2} F_1 \xrightarrow{d_1} F_0 \to Q \to 0
$$
une résolution libre de type fini de $Q$. On peut choisir une application
$\alpha : F_0 \to M$ qui relève l'application $F_0 \to Q$. Elle induit une application
$\beta : F_1 \to N$ telle que $\beta \circ d_2 = 0$. L'extension
ci-dessus est scindée si et seulement s'il existe une application $\gamma : F_0 \to N$
telle que $\beta = \gamma \circ d_1$. Autrement dit, la classe de
$\beta$ dans $\Ext^1_R(Q, N)$ est l'obstruction au scindage
de la suite exacte courte ci-dessus.

\medskip\noindent
Supposons que $n$ soit un entier assez grand tel que $N/I^nN \to M/I^nM$ soit une
injection scindée. On obtient la suite exacte courte
$$
0 \to N/I^nN \to M/I^nM \to Q/I^nQ \to 0.
$$
De plus, la suite
$$
F_1/I^nF_1 \xrightarrow{d_1} F_0/I^nF_0 \to Q/I^nQ \to 0
$$
est encore exacte. En raisonnant comme ci-dessus, on voit que l'application
$\overline{\beta} : F_1/I^nF_1 \to N/I^nN$
induite par $\beta$ est égale à $\overline{\gamma_n} \circ d_1$ pour une certaine
application $\overline{\gamma_n} : F_0/I^nF_0 \to N/I^nN$.
Comme $F_0$ est libre, on peut relever $\overline{\gamma_n}$ en une application
$\gamma_n : F_0 \to N$, et l'on voit alors que
$\beta - \gamma_n \circ d_1$ est une application de $F_1$ dans $I^nN$.
Autrement dit, on conclut que
$$
\beta \in
\Im\Big(\Hom_R(F_0, N) \to \Hom_R(F_1, N)\Big) + I^n\Hom_R(F_1, N).
$$
Cette inclusion vaut pour cet entier $n$.

\medskip\noindent
Puisque, par hypothèse, cette propriété vaut pour des entiers $n$ arbitrairement grands,
on conclut que l'image de $\beta$ dans le conoyau de
$\Hom_R(F_0, N) \to \Hom_R(F_1, N)$ est nulle d'après le
Lemme \ref{lemma-intersection-powers-ideal-module}. Ainsi
$\beta$ appartient à l'image de l'application $\Hom_R(F_0, N) \to \Hom_R(F_1, N)$,
comme souhaité.
\end{proof}
```

</details>

## Contrôles et suite

Les 76 régions mathématiques nouvelles sont exactement identiques. Le préfixe de 12 923 régions passe avec quarante-trois exceptions linguistiques antérieures précisément recensées dans leur ordre et avec leurs multiplicités.

Labels, renvois, clés bibliographiques, entrées, contrôles TeX, environnements et items sont identiques. Aucun titre facultatif ni citation dans ce lot. Les seules modifications sont les deux réparations de phrase ; leur inverse exact retrouve le lot précédent et l’inverse complet retrouve le témoin public préservé.

Les 660 paires sont contiguës, sans lacune ni chevauchement. La comparaison mécanique complète la lecture du sens. Prochaine lecture : Groupes Tor et platitude, anglais L18215 /français L17981. Aucun PDF nouveau ni publication ; restauration globale en cours.

