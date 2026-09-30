# Connexité et intégrité géométriques

## Résultat et portée

Deux sections entièrement comparées : anglais L11484–11722 (239 lignes), français L11442–11671 (230 lignes), soit 12 paires complètes avec preuves et transitions. 92 occurrences sont reliées à des choix contextualisés. La lecture continue atteint 49 sections, 413 paires et 3379 occurrences ; ni le chapitre ni l’édition ne sont terminés.

Six occurrences de domaine intègre deviennent anneau intègre, conformément au registre de Ducros et aux lots précédents. Le terme initial était compréhensible : il s’agit de cohérence terminologique, non de six erreurs mathématiques. Aucun symbole, quantificateur, résultat ou renvoi ne change.

Un candidat de correction de la source a été rejeté : S=0 ne contredit pas le lemme sur les composantes connexes, car Stacks exclut expressément l’espace vide de la définition de connexe. Le dossier conserve la preuve de ce rejet et la différence de convention avec EGA. Aucune nouvelle erreur source n’est admise.

Lecture, normalisation et dossier produits par OpenAI Codex, sans relecture humaine. Les instructions demandent Ultra ; l’identifiant exact du modèle de cette reprise n’est pas attesté par une métadonnée consultée dans ce lot. Ne pas lui attribuer automatiquement le modèle d’un lot antérieur. Les attestations françaises ont été consultées rétrospectivement, dans les limites indiquées ci-dessous.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch16.fr.tex) · [État français précédent](staged/fr/010_algebra.prose-batch15.fr.tex) · [Lot précédent](ALGEBRA_PROSE_BATCH15_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH16_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH16_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH16_OCCURRENCES.json) · [Avant/après](ALGEBRA_PROSE_BATCH16_REPAIRS.json) · [Exception en formule](ALGEBRA_PROSE_BATCH16_MATH_EXCEPTIONS.json) · [Libellé bibliographique](ALGEBRA_PROSE_BATCH16_CITATION_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH16_COVERAGE.json) · [Observation séparée](ALGEBRA_PROSE_BATCH16_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Grothendieck et Dieudonné — EGA IV seconde partie

[Source consultée](https://www.numdam.org/item/PMIHES_1965__24__5_0.pdf) · [Fichier conservé](canon-consulted/fr-algebra/ega-iv2-numdam.pdf)

Pages PDF 58 et 65, imprimées 61 et 68, entièrement lues ; définitions 4.5.2 et 4.6.2. La page imprimée 61 a été rendue avec Poppler et inspectée, notamment le signe n′≤1.

Attestations courtes : « géométriquement connexe », « géométriquement intègre », « composantes connexes ».

Atteste la terminologie des deux sections et la séparation entre intégrité, réduction et irréductibilité géométriques.

Limites : La convention EGA admet zéro composante connexe ; elle n'est pas importée dans Stacks, qui exige un espace non vide. L'OCR de certaines formules est dégradé : il ne sert pas à corriger Stacks. Consultation rétrospective, pas relecture humaine.

SHA-256 : C3E960AA1C5C37046E8892D8A3CAC098E2738164136B5CDAA5D5D893F89931DA.

### Antoine Ducros — Introduction à la théorie des schémas

[Source consultée](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages 23 et 103 entièrement lues, définition 0.1.3 et isomorphismes tensoriels 2.6.7.

Attestations courtes : « anneau intègre », « produit tensoriel », « morphisme structural ».

Justifie anneau intègre pour domain ou integral domain et rappelle la non-nullité. Appuie le vocabulaire des produits tensoriels, quotients et changements de base.

Limites : Une attestation de terme n'est pas une preuve des énoncés de Stacks. Domaine intègre n'est pas déclaré dénué de sens ; le choix vise ici un registre cohérent. Consultation rétrospective.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

### Jean-François Dat — Algèbre ENS 2016–2017

[Source consultée](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/AlgebreM1/ENS1617.pdf) · [Fichier conservé](canon-consulted/fr-algebra/dat-algebre-ens1617.pdf)

Page 118 entièrement lue, définitions finales de séparablement clos et de clôture séparable absolue.

Attestations courtes : « séparablement clos », « clôture séparable ».

Distingue clôture séparable et clôture algébrique et confirme le registre des extensions séparables.

Limites : Les définitions concernent le sens des termes ; aucune finitude ou algébricité absente de Stacks n'est ajoutée. Consultation rétrospective.

SHA-256 : DB5B7FD8139D62C37D0DDDDC90EF22D3EDCF74CC663C5267815E4EA3CECBBB18.

## Les six normalisations françaises

### FR-ALGEBRA-B16-REPAIR-0001

Anglais L11666 ; français L11616.

Avant :
```tex
$S \otimes_k k'$ est un domaine intègre.
```

Après :
```tex
$S \otimes_k k'$ est un anneau intègre.
```

Normalisation de registre : domaine intègre est un synonyme reconnaissable, non une modification mathématique avérée. Anneau intègre est choisi pour la cohérence avec le canon effectivement consulté et les lots précédents.

### FR-ALGEBRA-B16-REPAIR-0002

Anglais L11692 ; français L11644.

Avant :
```tex
$S \otimes_k k'$ est un domaine intègre,
```

Après :
```tex
$S \otimes_k k'$ est un anneau intègre,
```

Même normalisation dans deux conditions ; la restriction aux extensions finies et la clôture algébrique sont inchangées.

### FR-ALGEBRA-B16-REPAIR-0003

Anglais L11693 ; français L11645.

Avant :
```tex
\item $S \otimes_k \overline{k}$ est un domaine intègre,
```

Après :
```tex
\item $S \otimes_k \overline{k}$ est un anneau intègre,
```

Même normalisation dans deux conditions ; la restriction aux extensions finies et la clôture algébrique sont inchangées.

### FR-ALGEBRA-B16-REPAIR-0004

Anglais L11707 ; français L11659.

Avant :
```tex
Soit $R$ une $k$-algèbre qui est un domaine intègre. Alors
```

Après :
```tex
Soit $R$ une $k$-algèbre qui est un anneau intègre. Alors
```

Même normalisation dans l'hypothèse, la conclusion et la fin de la preuve. Aucun résultat nouveau.

### FR-ALGEBRA-B16-REPAIR-0005

Anglais L11707 ; français L11660.

Avant :
```tex
$R \otimes_k S$ est un domaine intègre.
\end{lemma}
```

Après :
```tex
$R \otimes_k S$ est un anneau intègre.
\end{lemma}
```

Même normalisation dans l'hypothèse, la conclusion et la fin de la preuve. Aucun résultat nouveau.

### FR-ALGEBRA-B16-REPAIR-0006

Anglais L11716 ; français L11668.

Avant :
```tex
irréductible), donc $R \otimes_k S$ est un domaine intègre.
```

Après :
```tex
irréductible), donc $R \otimes_k S$ est un anneau intègre.
```

Même normalisation dans l'hypothèse, la conclusion et la fin de la preuve. Aucun résultat nouveau.

## Règles contextualisées

### FR-ALGEBRA-B16-RULE-CONNECTED

Connexe traduit connected, mais avec la convention non vide de Stacks ; le nombre de composantes n'est pas un nombre de points.

Canon : FR-ALGEBRA-B16-CANON-EGA.

### FR-ALGEBRA-B16-RULE-INTEGRAL

L'intégrité inclut la non-nullité et l'absence de diviseurs de zéro ; géométriquement exige toutes les extensions du corps.

Canon : FR-ALGEBRA-B16-CANON-EGA, FR-ALGEBRA-B16-CANON-DUCROS.

### FR-ALGEBRA-B16-RULE-SEP

La clôture algébrique absolue et la clôture séparable sont distinguées selon chaque occurrence et la phrase source.

Canon : FR-ALGEBRA-B16-CANON-DAT.

### FR-ALGEBRA-B16-RULE-TENSOR

Les bases des produits tensoriels et leur rôle dans les changements de corps sont conservés.

Canon : FR-ALGEBRA-B16-CANON-DUCROS.

### FR-ALGEBRA-B16-RULE-IRRED

Réduction, irréductibilité et intégrité ne sont pas interchangeables ; la conjonction dans le critère est maintenue.

Canon : FR-ALGEBRA-B16-CANON-EGA.

### FR-ALGEBRA-B16-RULE-IDEMP

Appui direct dans les énoncés : ne possède pas d'idempotent non trivial ne veut pas dire aucun idempotent.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B16-RULE-COLIMIT

Choix justifié par la structure du système orienté source ; aucune attestation lexicale nouvelle n'est prétendue.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B16-RULE-LOGIC

Portée des quantificateurs, négations et bijections vérifiée dans le passage complet, non par simple remplacement de mots.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B16-RULE-FINITE

Finitude d'une extension, type fini d'une algèbre et présentation finie restent distincts.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-geometrically-connected

Anglais L11484–11486 ; français L11442–11444.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11484) · FR-ALGEBRA-B16-CHOICE-0001.

Le titre géométriquement connexe suit le registre attesté par EGA IV 4.5.2. Ce choix lexical ne transfère pas la convention topologique d'EGA : Stacks impose qu'un espace connexe soit non vide. Le sens mathématique reste celui de la source traduite.

Point particulier à relire : EGA IV 4.5.2 autorise zéro composante connexe ; Stacks non. Le canon français atteste la langue mais ne supplante pas les conventions du texte traduit.

Règles : FR-ALGEBRA-B16-RULE-CONNECTED.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Geometrically connected algebras}
\label{section-geometrically-connected}
```

Français restauré :
```tex
\section{Algèbres géométriquement connexes}
\label{section-geometrically-connected}
```

</details>

### 02 — lemma-separably-closed-connected

Anglais L11487–11529 ; français L11445–11486.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11487) · FR-ALGEBRA-B16-CHOICE-0002.

La clôture séparable n'est pas remplacée par une clôture algébrique. Les deux algèbres, la réduction au type fini, la récurrence sur la somme des nombres de composantes et le choix d'une composante dont le complément reste connexe sont conservés. Image inverse désigne les trois préimages utilisées pour recoller deux espaces connexes. Le cas n=0 ou m=0, superflu sous la convention non vide de Stacks, reste comme dans le texte source.

Règles : FR-ALGEBRA-B16-RULE-CONNECTED, FR-ALGEBRA-B16-RULE-SEP, FR-ALGEBRA-B16-RULE-IRRED, FR-ALGEBRA-B16-RULE-IDEMP, FR-ALGEBRA-B16-RULE-LOGIC, FR-ALGEBRA-B16-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-separably-closed-connected}
Let $k$ be a separably algebraically closed field.
Let $R$, $S$ be $k$-algebras. If $\Spec(R)$, and
$\Spec(S)$ are connected, then so is
$\Spec(R \otimes_k S)$.
\end{lemma}

\begin{proof}
Recall that $\Spec(R)$ is connected if and only if
$R$ has no nontrivial idempotents, see
Lemma \ref{lemma-characterize-spec-connected}.
Hence, by Lemma \ref{lemma-limit-argument} we may assume $R$ and $S$ are of
finite type over $k$.
In this case $R$ and $S$ are Noetherian,
and have finitely many minimal primes, see
Lemma \ref{lemma-Noetherian-irreducible-components}.
Thus we may argue by induction on $n + m$ where $n$, resp.\ $m$
is the number of irreducible components of $\Spec(R)$,
resp.\ $\Spec(S)$. Of course the case where either $n$ or
$m$ is zero is trivial. If $n = m = 1$, i.e.,
$\Spec(R)$ and $\Spec(S)$ both have one irreducible component,
then the result holds by Lemma \ref{lemma-separably-closed-irreducible}.
Suppose that $n > 1$. Let $\mathfrak p \subset R$ be a minimal prime
corresponding to the irreducible closed subset $T \subset \Spec(R)$.
Let $T' \subset \Spec(R)$ be the union of the other $n - 1$
irreducible components. Choose an ideal $I \subset R$
such that $T' = V(I) = \Spec(R/I)$ (Lemma \ref{lemma-spec-closed}).
By choosing our minimal prime carefully
we may in addition arrange it so that $T'$ is connected, see
Topology, Lemma \ref{topology-lemma-remove-irreducible-connected}.
Then $T \cup T' = \Spec(R)$ and
$T \cap T' = V(\mathfrak p + I) = \Spec(R/(\mathfrak p + I))$
is not empty as $\Spec(R)$ is assumed connected.
The inverse image of $T$ in $\Spec(R \otimes_k S)$
is $\Spec(R/\mathfrak p \otimes_k S)$, and the inverse
of $T'$ in $\Spec(R \otimes_k S)$
is $\Spec(R/I \otimes_k S)$. By induction these are both
connected. The inverse image of $T \cap T'$ is
$\Spec(R/(\mathfrak p + I) \otimes_k S)$ which is nonempty.
Hence $\Spec(R \otimes_k S)$ is connected.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-separably-closed-connected}
Soit $k$ un corps séparablement algébriquement clos.
Soient $R$ et $S$ des $k$-algèbres. Si $\Spec(R)$ et
$\Spec(S)$ sont connexes, il en est de même pour
$\Spec(R \otimes_k S)$.
\end{lemma}

\begin{proof}
Rappelons que $\Spec(R)$ est connexe si et seulement si
$R$ ne possède pas d'idempotent non trivial, voir le
Lemme \ref{lemma-characterize-spec-connected}.
Par conséquent, par le Lemme \ref{lemma-limit-argument}, nous pouvons
supposer que $R$ et $S$ sont de type fini sur $k$.
Dans ce cas, $R$ et $S$ sont noethériens et possèdent un nombre fini
d'idéaux premiers minimaux, voir le
Lemme \ref{lemma-Noetherian-irreducible-components}.
Nous pouvons donc raisonner par récurrence sur $n + m$, où $n$, resp.\ $m$,
est le nombre de composantes irréductibles de $\Spec(R)$, resp.\ $\Spec(S)$.
Le cas où $n$ ou $m$ est nul est bien entendu trivial. Si $n = m = 1$,
c'est-à-dire si $\Spec(R)$ et $\Spec(S)$ ont chacun une seule composante
irréductible, le résultat est donné par le
Lemme \ref{lemma-separably-closed-irreducible}.
Supposons $n > 1$. Soit $\mathfrak p \subset R$ un idéal premier minimal
correspondant au fermé irréductible $T \subset \Spec(R)$.
Soit $T' \subset \Spec(R)$ l'union des $n - 1$ autres composantes
irréductibles. Choisissons un idéal $I \subset R$ tel que
$T' = V(I) = \Spec(R/I)$ (Lemme \ref{lemma-spec-closed}).
En choisissant convenablement notre idéal premier minimal, nous pouvons
de plus faire en sorte que $T'$ soit connexe, voir le
lemme \ref{topology-lemma-remove-irreducible-connected} de Topologie.
Alors $T \cup T' = \Spec(R)$ et
$T \cap T' = V(\mathfrak p + I) = \Spec(R/(\mathfrak p + I))$
n'est pas vide puisque $\Spec(R)$ est supposé connexe.
L'image inverse de $T$ dans $\Spec(R \otimes_k S)$ est
$\Spec(R/\mathfrak p \otimes_k S)$, et l'image inverse de $T'$ dans
$\Spec(R \otimes_k S)$ est $\Spec(R/I \otimes_k S)$.
Par récurrence, ces deux espaces sont connexes. L'image inverse de
$T \cap T'$ est $\Spec(R/(\mathfrak p + I) \otimes_k S)$, qui n'est pas vide.
Ainsi $\Spec(R \otimes_k S)$ est connexe.
\end{proof}
```

</details>

### 03 — lemma-geometrically-connected

Anglais L11530–11559 ; français L11487–11514.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11530) · FR-ALGEBRA-B16-CHOICE-0003.

Les conditions portent respectivement sur toute extension de corps et sur toute extension finie séparable. Clôture algébrique séparable traduit le choix d'une extension algébrique séparablement close, pas d'une clôture algébrique absolue. L'argument d'extension des corps et la contradiction par un idempotent non trivial sont complets. Le critère par les idempotents est lu avec la non-nullité impliquée par la connexité selon Stacks.

Règles : FR-ALGEBRA-B16-RULE-CONNECTED, FR-ALGEBRA-B16-RULE-SEP, FR-ALGEBRA-B16-RULE-IDEMP, FR-ALGEBRA-B16-RULE-LOGIC, FR-ALGEBRA-B16-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-geometrically-connected}
Let $k$ be a field.
Let $R$ be a $k$-algebra.
The following are equivalent
\begin{enumerate}
\item for every field extension $k'/k$ the
spectrum of $R \otimes_k k'$ is connected, and
\item for every finite separable field extension $k'/k$ the
spectrum of $R \otimes_k k'$ is connected.
\end{enumerate}
\end{lemma}

\begin{proof}
For any extension of fields $k'/k$ the connectivity
of the spectrum of $R \otimes_k k'$ is equivalent to $R \otimes_k k'$
having no nontrivial idempotents, see
Lemma \ref{lemma-characterize-spec-connected}. Assume (2).
Let $k \subset \overline{k}$ be a separable algebraic closure of $k$.
Using Lemma \ref{lemma-limit-argument}
we see that (2) is equivalent to $R \otimes_k \overline{k}$
having no nontrivial idempotents.
For any field extension $k'/k$, there exists a field
extension $\overline{k}'/\overline{k}$ with
$k' \subset \overline{k}'$. By Lemma \ref{lemma-separably-closed-connected}
we see that $R \otimes_k \overline{k}'$ has no nontrivial idempotents.
If $R \otimes_k k'$ has a nontrivial idempotent,
then also $R \otimes_k \overline{k}'$, contradiction.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-geometrically-connected}
Soit $k$ un corps.
Soit $R$ une $k$-algèbre.
Les assertions suivantes sont équivalentes
\begin{enumerate}
\item pour toute extension de corps $k'/k$, le spectre de
$R \otimes_k k'$ est connexe, et
\item pour toute extension de corps finie et séparable $k'/k$, le spectre
de $R \otimes_k k'$ est connexe.
\end{enumerate}
\end{lemma}

\begin{proof}
Pour toute extension de corps $k'/k$, la connexité du spectre de
$R \otimes_k k'$ équivaut à l'absence d'idempotents non triviaux dans
$R \otimes_k k'$, voir le Lemme \ref{lemma-characterize-spec-connected}.
Supposons (2). Soit $k \subset \overline{k}$ une clôture algébrique
séparable de $k$. Par le Lemme \ref{lemma-limit-argument}, (2) équivaut
à l'absence d'idempotents non triviaux dans $R \otimes_k \overline{k}$.
Pour toute extension de corps $k'/k$, il existe une extension
$\overline{k}'/\overline{k}$ telle que $k' \subset \overline{k}'$.
Par le Lemme \ref{lemma-separably-closed-connected},
$R \otimes_k \overline{k}'$ ne possède pas d'idempotent non trivial.
Si $R \otimes_k k'$ possédait un idempotent non trivial, il en serait de
même dans $R \otimes_k \overline{k}'$, contradiction.
\end{proof}
```

</details>

### 04 — definition-geometrically-connected

Anglais L11560–11572 ; français L11515–11527.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11560) · FR-ALGEBRA-B16-CHOICE-0004.

La propriété est relative au corps k et exige la connexité après toute extension k′/k. Le renvoi qui suit réduit la vérification aux extensions finies séparables ; il ne remplace pas le quantificateur de la définition. Le mot connexe conserve la convention non vide de Stacks, malgré la convention différente d'EGA.

Règles : FR-ALGEBRA-B16-RULE-CONNECTED, FR-ALGEBRA-B16-RULE-SEP, FR-ALGEBRA-B16-RULE-LOGIC, FR-ALGEBRA-B16-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-geometrically-connected}
Let $k$ be a field.
Let $S$ be a $k$-algebra.
We say $S$ is {\it geometrically connected over $k$}
if for every field extension $k'/k$ the spectrum
of $S \otimes_k k'$ is connected.
\end{definition}

\noindent
By Lemma \ref{lemma-geometrically-connected} it suffices
to check this for finite separable field extensions $k'/k$.
```

Français restauré :
```tex
\begin{definition}
\label{definition-geometrically-connected}
Soit $k$ un corps.
Soit $S$ une $k$-algèbre.
Nous disons que $S$ est {\it géométriquement connexe sur $k$}
si, pour toute extension de corps $k'/k$, le spectre
de $S \otimes_k k'$ est connexe.
\end{definition}

\noindent
Par le Lemme \ref{lemma-geometrically-connected}, il suffit de vérifier
cette propriété pour les extensions de corps finies et séparables $k'/k$.
```

</details>

### 05 — lemma-separably-closed-connected-implies-geometric

Anglais L11573–11586 ; français L11528–11541.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11573) · FR-ALGEBRA-B16-CHOICE-0005.

Le corps k est séparablement algébriquement clos, et non nécessairement parfait. L'équivalence entre connexité géométrique de R et connexité de son spectre est inchangée. La preuve reste le seul renvoi à la remarque qui suit la définition ; aucune démonstration nouvelle n'est insérée.

Règles : FR-ALGEBRA-B16-RULE-CONNECTED, FR-ALGEBRA-B16-RULE-SEP, FR-ALGEBRA-B16-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-separably-closed-connected-implies-geometric}
Let $k$ be a field.
Let $R$ be a $k$-algebra.
If $k$ is separably algebraically closed then $R$ is
geometrically connected over $k$ if and only if the
spectrum of $R$ is connected.
\end{lemma}

\begin{proof}
Immediate from the remark following
Definition \ref{definition-geometrically-connected}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-separably-closed-connected-implies-geometric}
Soit $k$ un corps.
Soit $R$ une $k$-algèbre.
Si $k$ est séparablement algébriquement clos, alors $R$ est
géométriquement connexe sur $k$ si et seulement si le spectre de
$R$ est connexe.
\end{lemma}

\begin{proof}
Cela résulte immédiatement de la remarque qui suit la
Définition \ref{definition-geometrically-connected}.
\end{proof}
```

</details>

### 06 — lemma-subalgebra-geometrically-connected

Anglais L11587–11609 ; français L11542–11564.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11587) · FR-ALGEBRA-B16-CHOICE-0006.

Les trois assertions distinguent chaque sous-algèbre, toutes les sous-algèbres de type fini et une colimite filtrante. La conclusion de la première assertion est présente. Colimite filtrante est le choix de registre de cette édition pour directed colimit ; ici le système orienté fournit bien une catégorie filtrante, sans changer les objets ni affirmer un résultat pour une colimite arbitraire. Cette expression n'est pas attribuée aux pages françaises consultées pour ce lot.

Point particulier à relire : L'appui de colimite filtrante dans ce lot est la comparaison mathématique avec le système orienté source, non une prétendue occurrence dans les pages de canon citées.

Règles : FR-ALGEBRA-B16-RULE-CONNECTED, FR-ALGEBRA-B16-RULE-TENSOR, FR-ALGEBRA-B16-RULE-IDEMP, FR-ALGEBRA-B16-RULE-COLIMIT, FR-ALGEBRA-B16-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-subalgebra-geometrically-connected}
Let $k$ be a field. Let $S$ be a $k$-algebra.
\begin{enumerate}
\item If $S$ is geometrically connected over $k$ so is every
$k$-subalgebra.
\item If all finitely generated $k$-subalgebras of $S$ are
geometrically connected, then $S$ is geometrically connected.
\item A directed colimit of geometrically connected $k$-algebras
is geometrically connected.
\end{enumerate}
\end{lemma}

\begin{proof}
This follows from the characterization of connectedness in terms of the
nonexistence of nontrivial idempotents. The second and third property follow
from the fact that tensor product commutes with colimits.
\end{proof}

\noindent
The following lemma will be superseded by the more general
Varieties, Lemma \ref{varieties-lemma-bijection-connected-components}.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-subalgebra-geometrically-connected}
Soit $k$ un corps. Soit $S$ une $k$-algèbre.
\begin{enumerate}
\item Si $S$ est géométriquement connexe sur $k$, toute
$k$-sous-algèbre l'est également.
\item Si toutes les $k$-sous-algèbres de type fini de $S$ sont
géométriquement connexes, alors $S$ est géométriquement connexe.
\item Une colimite filtrante de $k$-algèbres géométriquement connexes
est géométriquement connexe.
\end{enumerate}
\end{lemma}

\begin{proof}
Cela résulte de la caractérisation de la connexité par l'absence
d'idempotents non triviaux. Les deuxième et troisième assertions résultent
du fait que le produit tensoriel commute aux colimites.
\end{proof}

\noindent
Le lemme suivant sera remplacé par le résultat plus général du
lemme \ref{varieties-lemma-bijection-connected-components} de Variétés.
```

</details>

### 07 — lemma-geometrically-connected-any-base-change

Anglais L11610–11653 ; français L11565–11603.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11610) · FR-ALGEBRA-B16-CHOICE-0007.

La première bijection porte sur les idempotents et la seconde sur les composantes connexes. Les directions contravariantes des spectres, les réductions au type fini, les composantes ouvertes et le recours aux fibres sont préservés. La phrase non nulle dans la preuve ne révèle pas une hypothèse manquante : Stacks définit un espace connexe comme non vide, donc la connexité géométrique force S≠0. Le candidat de correction fondé sur S=0 est rejeté et aucune hypothèse n'est ajoutée au français.

Point particulier à relire : Faux positif écarté après lecture de Topologie, définition des composantes connexes L623–636 : l'espace vide n'est pas connexe dans cette source. Le contre-exemple S=0 n'en satisfait donc pas l'hypothèse.

Règles : FR-ALGEBRA-B16-RULE-CONNECTED, FR-ALGEBRA-B16-RULE-IRRED, FR-ALGEBRA-B16-RULE-IDEMP, FR-ALGEBRA-B16-RULE-LOGIC, FR-ALGEBRA-B16-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-geometrically-connected-any-base-change}
Let $k$ be a field.
Let $S$ be a geometrically connected $k$-algebra.
Let $R$ be any $k$-algebra.
The map
$$
R \longrightarrow R \otimes_k S
$$
induces a bijection on idempotents, and the map
$$
\Spec(R \otimes_k S) \longrightarrow \Spec(R)
$$
induces a bijection on connected components.
\end{lemma}

\begin{proof}
The second assertion follows from the first combined with
Lemma \ref{lemma-connected-component}.
By Lemmas \ref{lemma-subalgebra-geometrically-connected}
and \ref{lemma-limit-argument} we may assume that $R$ and $S$
are of finite type over $k$. Then we see that also
$R \otimes_k S$ is of finite type over $k$. Note that in this
case all the rings are Noetherian and hence their spectra
have finitely many connected components (since they have
finitely many irreducible components, see
Lemma \ref{lemma-Noetherian-irreducible-components}).
In particular, all connected components in question are open!
Hence via Lemma \ref{lemma-disjoint-implies-product}
we see that the first statement of the
lemma in this case is equivalent to the second. Let's prove this.
As the algebra $S$ is geometrically connected
and nonzero we see that all fibres of $X = \Spec(R \otimes_k S)
\to \Spec(R) = Y$ are connected and nonempty. Also, as
$R \to R \otimes_k S$ is flat of finite presentation the map
$X \to Y$ is open
(Proposition \ref{proposition-fppf-open}).
Topology, Lemma \ref{topology-lemma-connected-fibres-connected-components}
shows that $X \to Y$ induces bijection on connected components.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-geometrically-connected-any-base-change}
Soit $k$ un corps.
Soit $S$ une $k$-algèbre géométriquement connexe.
Soit $R$ une $k$-algèbre quelconque.
L'application
$$
R \longrightarrow R \otimes_k S
$$
induit une bijection sur les idempotents, et l'application
$$
\Spec(R \otimes_k S) \longrightarrow \Spec(R)
$$
induit une bijection sur les composantes connexes.
\end{lemma}

\begin{proof}
La seconde assertion résulte de la première et du
Lemme \ref{lemma-connected-component}.
Par les Lemmes \ref{lemma-subalgebra-geometrically-connected} et
\ref{lemma-limit-argument}, nous pouvons supposer que $R$ et $S$ sont de
type fini sur $k$. Alors $R \otimes_k S$ est également de type fini sur $k$.
Remarquons que, dans ce cas, tous les anneaux sont noethériens et que leurs
spectres possèdent un nombre fini de composantes connexes (puisqu'ils ont
un nombre fini de composantes irréductibles, voir le
Lemme \ref{lemma-Noetherian-irreducible-components}).
En particulier, toutes les composantes connexes en question sont ouvertes !
Par le Lemme \ref{lemma-disjoint-implies-product}, la première assertion
du lemme est alors équivalente à la seconde. Démontrons cette dernière.
Comme l'algèbre $S$ est géométriquement connexe et non nulle, toutes les
fibres de $X = \Spec(R \otimes_k S) \to \Spec(R) = Y$ sont connexes
et non vides. De plus, comme $R \to R \otimes_k S$ est plate et de
présentation finie, l'application $X \to Y$ est ouverte
(Proposition \ref{proposition-fppf-open}).
Le Lemme \ref{topology-lemma-connected-fibres-connected-components} de
Topologie montre que $X \to Y$ induit une bijection sur les composantes
connexes.
\end{proof}
```

</details>

### 08 — section-geometrically-integral

Anglais L11654–11659 ; français L11604–11609.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11654) · FR-ALGEBRA-B16-CHOICE-0008.

Géométriquement intègre est attesté par EGA IV 4.6.2. L'annonce Voici la définition reste une annonce, non un développement ajouté. Le vocabulaire géométrique ne confond pas intégrité d'un anneau et intégralité d'un morphisme.

Règles : FR-ALGEBRA-B16-RULE-INTEGRAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Geometrically integral algebras}
\label{section-geometrically-integral}

\noindent
Here is the definition.
```

Français restauré :
```tex
\section{Algèbres géométriquement intègres}
\label{section-geometrically-integral}

\noindent
Voici la définition.
```

</details>

### 09 — definition-geometrically-integral

Anglais L11660–11672 ; français L11610–11623.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11660) · FR-ALGEBRA-B16-CHOICE-0009.

Pour toute extension de corps, le produit tensoriel doit être un anneau intègre. Domaine intègre était compréhensible mais anneau intègre est le terme adopté, attesté précisément par Ducros 0.1.3. Il s'agit de normalisation terminologique, pas d'une erreur de théorème. La phrase de transition sur les questions réduites et irréductibles et tous les quantificateurs sont conservés.

Point particulier à relire : Normalisation de registre : domaine intègre est un synonyme reconnaissable, non une modification mathématique avérée. Anneau intègre est choisi pour la cohérence avec le canon effectivement consulté et les lots précédents.

Règles : FR-ALGEBRA-B16-RULE-INTEGRAL, FR-ALGEBRA-B16-RULE-IRRED, FR-ALGEBRA-B16-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-geometrically-integral}
Let $k$ be a field.
Let $S$ be a $k$-algebra.
We say $S$ is {\it geometrically integral over $k$}
if for every field extension $k'/k$ the ring
of $S \otimes_k k'$ is a domain.
\end{definition}

\noindent
Any question about geometrically integral algebras can be translated
in a question about geometrically reduced and irreducible algebras.
```

Français restauré :
```tex
\begin{definition}
\label{definition-geometrically-integral}
Soit $k$ un corps.
Soit $S$ une $k$-algèbre.
Nous disons que $S$ est {\it géométriquement intègre sur $k$}
si, pour toute extension de corps $k'/k$, l'anneau
$S \otimes_k k'$ est un anneau intègre.
\end{definition}

\noindent
Toute question concernant les algèbres géométriquement intègres peut être
traduite en une question concernant les algèbres géométriquement réduites
et irréductibles.
```

</details>

### 10 — lemma-geometrically-integral

Anglais L11673–11684 ; français L11624–11636.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11673) · FR-ALGEBRA-B16-CHOICE-0010.

L'intégrité géométrique équivaut à la conjonction de la réduction géométrique et de l'irréductibilité géométrique, toutes relatives au même corps k. À la fois préserve la conjonction. Démonstration omise traduit Omitted ; on ne remplace pas ce choix du texte par une preuve ajoutée.

Règles : FR-ALGEBRA-B16-RULE-INTEGRAL, FR-ALGEBRA-B16-RULE-IRRED, FR-ALGEBRA-B16-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-geometrically-integral}
Let $k$ be a field.
Let $S$ be a $k$-algebra.
In this case $S$ is geometrically integral over $k$ if and only if
$S$ is geometrically irreducible as well as geometrically reduced over $k$.
\end{lemma}

\begin{proof}
Omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-geometrically-integral}
Soit $k$ un corps.
Soit $S$ une $k$-algèbre.
Alors $S$ est géométriquement intègre sur $k$ si et seulement si
$S$ est à la fois géométriquement irréductible et géométriquement réduite
sur $k$.
\end{lemma}

\begin{proof}
Démonstration omise.
\end{proof}
```

</details>

### 11 — lemma-characterize-geometrically-integral

Anglais L11685–11703 ; français L11637–11655.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11685) · FR-ALGEBRA-B16-CHOICE-0011.

Les trois conditions distinguent la propriété géométrique, toutes les extensions finies de corps et une clôture algébrique. Cette fois clôture algébrique n'est pas clôture séparable. Deux occurrences de domaine intègre sont normalisées en anneau intègre, avec hypothèses et renvois inchangés. Les références à la réduction et à l'irréductibilité restent exactement les mêmes.

Point particulier à relire : Même normalisation dans deux conditions ; la restriction aux extensions finies et la clôture algébrique sont inchangées.

Règles : FR-ALGEBRA-B16-RULE-INTEGRAL, FR-ALGEBRA-B16-RULE-SEP, FR-ALGEBRA-B16-RULE-LOGIC, FR-ALGEBRA-B16-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-geometrically-integral}
Let $k$ be a field. Let $S$ be a $k$-algebra.
The following are equivalent
\begin{enumerate}
\item $S$ is geometrically integral over $k$,
\item for every finite extension $k'/k$ of fields
the ring $S \otimes_k k'$ is a domain,
\item $S \otimes_k \overline{k}$ is a domain
where $\overline{k}$ is the algebraic closure of $k$.
\end{enumerate}
\end{lemma}

\begin{proof}
Follows from Lemmas \ref{lemma-geometrically-integral},
\ref{lemma-geometrically-reduced-finite-purely-inseparable-extension}, and
\ref{lemma-geometrically-irreducible}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-characterize-geometrically-integral}
Soit $k$ un corps. Soit $S$ une $k$-algèbre.
Les assertions suivantes sont équivalentes
\begin{enumerate}
\item $S$ est géométriquement intègre sur $k$,
\item pour toute extension finie de corps $k'/k$, l'anneau
$S \otimes_k k'$ est un anneau intègre,
\item $S \otimes_k \overline{k}$ est un anneau intègre,
où $\overline{k}$ est la clôture algébrique de $k$.
\end{enumerate}
\end{lemma}

\begin{proof}
Cela résulte des Lemmes \ref{lemma-geometrically-integral},
\ref{lemma-geometrically-reduced-finite-purely-inseparable-extension} et
\ref{lemma-geometrically-irreducible}.
\end{proof}
```

</details>

### 12 — lemma-geometrically-integral-any-integral-base-change

Anglais L11704–11722 ; français L11656–11671.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11704) · FR-ALGEBRA-B16-CHOICE-0012.

R est à la fois une k-algèbre et un anneau intègre ; S est géométriquement intègre. La conclusion porte sur R⊗_k S. Les trois occurrences de domaine intègre sont normalisées sans modifier cette hypothèse, la conclusion ou la preuve. L'expression anneau irréductible conserve l'explication source entre parenthèses sur son spectre ; on ne la remplace pas par une assertion différente.

Point particulier à relire : Même normalisation dans l'hypothèse, la conclusion et la fin de la preuve. Aucun résultat nouveau.

Règles : FR-ALGEBRA-B16-RULE-INTEGRAL, FR-ALGEBRA-B16-RULE-IRRED.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-geometrically-integral-any-integral-base-change}
Let $k$ be a field. Let $S$ be a geometrically integral $k$-algebra.
Let $R$ be a $k$-algebra and an integral domain. Then $R \otimes_k S$
is an integral domain.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-geometrically-reduced-any-reduced-base-change}
the ring $R \otimes_k S$ is reduced and by
Lemma \ref{lemma-geometrically-irreducible-any-base-change}
the ring $R \otimes_k S$ is irreducible (the spectrum
has just one irreducible component), so $R \otimes_k S$ is
an integral domain.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-geometrically-integral-any-integral-base-change}
Soit $k$ un corps. Soit $S$ une $k$-algèbre géométriquement intègre.
Soit $R$ une $k$-algèbre qui est un anneau intègre. Alors
$R \otimes_k S$ est un anneau intègre.
\end{lemma}

\begin{proof}
Par le Lemme \ref{lemma-geometrically-reduced-any-reduced-base-change},
l'anneau $R \otimes_k S$ est réduit et, par le
Lemme \ref{lemma-geometrically-irreducible-any-base-change}, l'anneau
$R \otimes_k S$ est irréductible (son spectre possède une seule composante
irréductible), donc $R \otimes_k S$ est un anneau intègre.
\end{proof}
```

</details>

## Candidat de correction rejeté

### FR-ALGEBRA-B16-SOURCE-NOTE-0001

[Source L11613](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L11613) — lemma-geometrically-connected-any-base-change.

```tex
Let $S$ be a geometrically connected $k$-algebra.
```

Le candidat « ajouter S non nul » est rejeté. Dans le même témoin officiel, topology.tex L623–636 exige explicitement X non vide pour le dire connected et précise The empty space is not connected. L'algèbre S=0 n'est donc pas géométriquement connexe au sens de cette source. Le contre-exemple envisagé R=k, S=0 est inadmissible. EGA IV 4.5.2 a une convention différente (n′≤1), ce qui ne justifie aucun changement du texte Stacks. L'énoncé, sa preuve et le français restent inchangés ; cette entrée n'est pas un erratum.

Rejet fondé sur la définition explicite du témoin officiel, non probabilité calibrée. Cette note ne doit pas être comptée comme un erratum. Aucune découverte originale ni déduplication globale revendiquée.

[Convention officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L623) — topology.tex L623–636 ; SHA-256 C6BAC8DCF8AD96DC47416BF34CB45BA4A10B894E40D67D3E1FA68D8EF0D9F872.

```tex
\begin{definition}
\label{definition-connected-components}
Let $X$ be a topological space.
\begin{enumerate}
\item We say $X$ is {\it connected} if $X$ is not empty and whenever
$X = T_1 \amalg T_2$ with $T_i \subset X$ open and closed, then either
$T_1 = \emptyset$ or $T_2 = \emptyset$.
\item We say $T \subset X$ is a {\it connected component} of $X$ if
$T$ is a maximal connected subset of $X$.
\end{enumerate}
\end{definition}

\noindent
The empty space is not connected.
```

## Contrôles et suite

Les 138 régions mathématiques du lot concordent exactement, sans exception nouvelle. Le préfixe compte 8 293 régions et les vingt-deux exceptions linguistiques déjà scellées dans les lots antérieurs. L’égalité brute du préfixe sans ces exceptions n’est pas revendiquée.

Ce lot ne contient ni citation bibliographique ni intitulé facultatif de lemme. Labels, renvois, clés bibliographiques du fichier entier, entrées, contrôles TeX, environnements et items sont préservés. Aucune région mathématique du français entier ne change depuis le lot précédent.

Les opérations inverses retrouvent le lot précédent puis le témoin public conservé. Les 413 paires sont contiguës, sans lacune ni chevauchement. Les octets du préfixe déjà relu et ceux du suffixe encore non relu sont inchangés. Les contrôles mécaniques complètent la lecture sémantique et ne la remplacent pas.

Prochaine lecture : Anneaux de valuation, anglais L11723 / français L11672. Aucun nouveau PDF, aucune publication et aucune certification globale du chapitre ou de l’édition dans ce lot.

