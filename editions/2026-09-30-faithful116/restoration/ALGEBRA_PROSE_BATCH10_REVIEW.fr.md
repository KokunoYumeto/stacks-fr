# Algèbre commutative : anneaux de Jacobson

## Résultat et portée

Une section entièrement comparée : anglais L6649–7433 et français L6629–7413, soit 785 lignes de chaque témoin. Les 25 paires comprennent les preuves complètes, les exemples et les transitions. 214 occurrences sont reliées à des règles contextualisées. Le préfixe atteint 35 sections, 252 paires et 1938 occurrences. Le chapitre et l’édition restent inachevés.

Deux opérations seulement : ouverts standards devient ouverts principaux, attesté dans le canon français ; idéal premier contenant devient idéal contenant pour restaurer le texte anglais. Ce second retrait rétablit une lacune de la phrase de preuve : la justification de premier reste dans une observation séparée, sans se faire passer pour le texte officiel. Aucune formule ni référence ne change.

Sept observations séparées distinguent une non-vacuité implicite, deux raccourcis sur les applications spectrales, une inversion de X et Y dans la preuve, le manque de primalité, une parenthèse excédentaire et une ambiguïté de taille de matrice. Ce ne sont pas sept nouveaux théorèmes faux ni sept admissions d’errata.

Comparaison assistée par IA, sans relecture humaine. Le canon est consulté rétrospectivement pour cette décision ; aucune consultation antérieure n’est inventée. Les expressions non attestées dans les pages effectivement lues sont explicitement signalées, sans bloquer une décision provisoire motivée.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch10.fr.tex) · [État français précédent](staged/fr/010_algebra.prose-batch9.fr.tex) · [Lot précédent](ALGEBRA_PROSE_BATCH9_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH10_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH10_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH10_OCCURRENCES.json) · [Avant/après](ALGEBRA_PROSE_BATCH10_REPAIRS.json) · [Exceptions de texte dans les formules](ALGEBRA_PROSE_BATCH10_MATH_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH10_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH10_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Jean-François Dat — Algèbre, ENS 2016–2017

[Source consultée](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/AlgebreM1/ENS1617.pdf) · [Fichier conservé](canon-consulted/fr-algebra/dat-algebre-ens1617.pdf)

Pages PDF/imprimées 98–99 lues entièrement ; p.98 rendue et inspectée. Définition des anneaux de Jacobson, critère par les premiers, densité des points maximaux dans les quotients, corollaire de type fini et exercice sur la contraction des maximaux.

Attestations courtes : « corps résiduel », « extension finie », « idéaux radiciels ».

Attestation française précise du registre Jacobson et des distinctions type fini, corps résiduel, extension finie et algébrique. Le cours donne des formulations équivalentes, pas une licence pour remplacer les démonstrations de Stacks.

Limites : Radiciel est une variante de radical dans ce passage ; on ne la substitue pas systématiquement. Le paragraphe sur un polynôme g premier aux dénominateurs appelle un choix non constant pour l'argument d'inversion ; il n'est pas importé. Ces pages ne justifient ni le Nullstellensatz non dénombrable ni toute la terminologie des orbites de matrices.

SHA-256 : DB5B7FD8139D62C37D0DDDDC90EF22D3EDCF74CC663C5267815E4EA3CECBBB18.

### Jean-François Dat — Théorie des schémas

[Source consultée](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/Schemas/Schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/dat-schemas.pdf)

Page PDF/imprimée 8 relue entièrement : 1.2.4 Ouverts principaux et 1.2.5 application spectrale. Son rendu a déjà été contrôlé au lot 9 ; pas de nouveau rendu revendiqué ici.

Attestations courtes : « Ouverts principaux », « partie multiplicative ».

D(f) est nommé ouvert principal et ces ouverts forment une base. La source explicite aussi Spec(B)→Spec(A), sens requis pour comprendre les deux exemples de localisation.

Limites : Les barres d'adhérence de 1.2.5 peuvent disparaître à l'extraction ; la version visuelle déjà consultée fait foi. Ce cours sert de canon de registre, pas de nouvelle autorité qui corrigerait silencieusement Stacks.

SHA-256 : 9298B062AC2BDF64161A107980A30F98E1F2DF6DEB4DA98E1FEB21BA494D26A1.

### Stacks Project officiel — Topology, définitions et propriétés des espaces de Jacobson

[Source consultée](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex#L3307) · [Fichier conservé](../../03_working_translations/stacks_cjk_20260821/upstream/src/stacks-project-a04446e57ec1fbc252a871afcec7752fb2807b14/topology.tex)

L3307–3329 et L3424–3538 lues : condition localement fermée non vide, espaces induits et correspondances des parties localement fermées ou constructibles.

Attestations courtes : « nonempty locally closed subset ».

Contrôle mathématique des références effectivement invoquées, notamment de la non-vacuité et de la correspondance E↦E0.

Limites : Témoin anglais officiel, pas une attestation du français. Sa présence ici documente la vérification des renvois, distincte de la consultation de registre.

SHA-256 : C6BAC8DCF8AD96DC47416BF34CB45BA4A10B894E40D67D3E1FA68D8EF0D9F872.

## Les deux opérations exactes

### FR-ALGEBRA-B10-REPAIR-0001

Anglais L6705 ; français L6685.

Avant :
```tex
les ouverts standards
```

Après :
```tex
les ouverts principaux
```

Ouverts principaux désigne exactement les D(f) de la source. Dat p.8 atteste ce terme ; remplacer le calque n'ajoute ni objet ni hypothèse.

### FR-ALGEBRA-B10-REPAIR-0002

Anglais L7250 ; français L7230.

Avant :
```tex
est un idéal premier contenant
```

Après :
```tex
est un idéal contenant
```

Le mot premier ajouté en français réparait réellement le raisonnement : l'idéal (xy) contient xy mais ni x ni y. Il est retiré pour que cette réparation ne soit pas attribuée à la source. On conserve explicitement sa justification dans le dossier de révision.

## Règles contextualisées

### FR-ALGEBRA-B10-RULE-JACOBSON

Anneau et espace de Jacobson sont distingués ; densité dans chaque fermé et intersection des maximaux contenant chaque radical sont comparées à leurs définitions. L'attestation Dat concerne directement l'anneau ; Topology gouverne la définition topologique.

Canon : FR-ALGEBRA-B10-CANON-DAT-ALGEBRE.

### FR-ALGEBRA-B10-RULE-RADICAL

Radical, premier et maximal ne sont pas interchangeables. Chaque occurrence est rattachée au quantificateur et à l'anneau du passage. Radiciel est une alternative attestée mais non imposée.

Canon : FR-ALGEBRA-B10-CANON-DAT-ALGEBRE.

### FR-ALGEBRA-B10-RULE-FINITE

Type fini est une génération d'algèbre ; finie est le degré de l'extension résiduelle quand la source le dit. Algébrique peut être de degré infini. Présentation finie requiert l'argument indiqué, non une synonymie.

Canon : FR-ALGEBRA-B10-CANON-DAT-ALGEBRE.

### FR-ALGEBRA-B10-RULE-PRINCIPAL

D(f) est un ouvert principal ; une occurrence plurielle est réparée. Le mot principal peut aussi qualifier un idéal ou un anneau ailleurs, mais cette règle ne vise que l'ouvert.

Canon : FR-ALGEBRA-B10-CANON-DAT-SCHEMAS.

### FR-ALGEBRA-B10-RULE-LOCALISATION

Inverser un élément et inverser une famille infinie sont distingués. Les assertions portent soit sur l'anneau, soit sur les points de son spectre ; elles ne sont pas confondues.

Canon : FR-ALGEBRA-B10-CANON-DAT-SCHEMAS.

### FR-ALGEBRA-B10-RULE-TOPOLOGIE

Le statut fermé peut être relatif à un sous-espace. Vérifier l'espace ambiant, la non-vacuité et la direction Spec(B)→Spec(A). Topology est un appui mathématique anglais, non un témoignage de langue.

Canon : FR-ALGEBRA-B10-CANON-DAT-SCHEMAS, FR-ALGEBRA-B10-CANON-TOPOLOGY.

### FR-ALGEBRA-B10-RULE-CARDINAL

Les bornes strictes et le caractère fini ou infini des index sont lus dans chaque argument. Les choix français restent compositionnels lorsqu'aucune attestation spécialisée n'a été acquise.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B10-RULE-MATRICES

La justification est le calcul source : action à trois facteurs ou conjugaison, rang, coefficients diagonaux, trace et puissance extérieure. Pas d'attestation française externe nouvelle pour toutes ces expressions ; raisonnement et incertitudes sont donnés par paire.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B10-RULE-LOGIQUE

Conserver la portée des quantificateurs, les exclusions zéro/vide et les deux sens des implications. Une précision mathématique absente de l'anglais n'est pas ajoutée silencieusement.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-ring-jacobson

Anglais L6649–6658 ; français L6629–6638.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6649) · FR-ALGEBRA-B10-CHOICE-0001.

Anneaux de Jacobson est le titre attesté chez Dat, Algèbre ENS, p.98–99. Le passage du Nullstellensatz à une propriété de tous les idéaux radicaux est conservé ; on ne remplace pas cette propriété par une seule égalité concernant le radical de Jacobson de R.

Règles : FR-ALGEBRA-B10-RULE-JACOBSON, FR-ALGEBRA-B10-RULE-RADICAL, FR-ALGEBRA-B10-RULE-FINITE, FR-ALGEBRA-B10-RULE-TOPOLOGIE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Jacobson rings}
\label{section-ring-jacobson}

\noindent
Let $R$ be a ring. The closed points of $\Spec(R)$ are the
maximal ideals of $R$. Often rings which occur naturally in algebraic
geometry have lots of maximal ideals. For example finite type algebras
over a field or over $\mathbf{Z}$. We will show that these
are examples of Jacobson rings.
```

Français restauré :
```tex
\section{Anneaux de Jacobson}
\label{section-ring-jacobson}

\noindent
Soit $R$ un anneau. Les points fermés de $\Spec(R)$ sont les
idéaux maximaux de $R$. Souvent, les anneaux qui apparaissent naturellement en
géométrie algébrique ont beaucoup d'idéaux maximaux. C'est par exemple le cas des algèbres
de type fini sur un corps ou sur $\mathbf{Z}$. Nous montrerons que celles-ci
sont des exemples d'anneaux de Jacobson.
```

</details>

### 02 — definition-ring-jacobson

Anglais L6659–6666 ; français L6639–6646.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6659) · FR-ALGEBRA-B10-CHOICE-0002.

La définition concerne chaque idéal radical, comme intersection des idéaux maximaux qui le contiennent. Dat p.98 donne la formulation équivalente pour le radical de tout idéal, puis pour tout idéal premier. Idéal radical est maintenu, plutôt que d'imposer la variante radiciel employée p.99 de ce cours. On n'ajoute pas de convention ni de commentaire dans la définition traduite.

Règles : FR-ALGEBRA-B10-RULE-JACOBSON, FR-ALGEBRA-B10-RULE-RADICAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-ring-jacobson}
Let $R$ be a ring. We say that $R$ is a
{\it Jacobson ring} if every radical
ideal $I$ is the intersection of the
maximal ideals containing it.
\end{definition}
```

Français restauré :
```tex
\begin{definition}
\label{definition-ring-jacobson}
Soit $R$ un anneau. Nous disons que $R$ est un
{\it anneau de Jacobson} si tout idéal
radical $I$ est l'intersection des
idéaux maximaux qui le contiennent.
\end{definition}
```

</details>

### 03 — lemma-finite-type-field-Jacobson

Anglais L6667–6676 ; français L6647–6656.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6667) · FR-ALGEBRA-B10-CHOICE-0003.

Algèbre de type fini sur un corps ne devient pas algèbre de dimension finie. Le renvoi au Nullstellensatz conserve exactement l'hypothèse. Dat p.99 énonce le même corollaire et fournit une attestation française directe.

Règles : FR-ALGEBRA-B10-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-finite-type-field-Jacobson}
Any algebra of finite type over a field is Jacobson.
\end{lemma}

\begin{proof}
This follows from Theorem \ref{theorem-nullstellensatz}
and Definition \ref{definition-ring-jacobson}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-finite-type-field-Jacobson}
Toute algèbre de type fini sur un corps est de Jacobson.
\end{lemma}

\begin{proof}
Cela résulte du théorème \ref{theorem-nullstellensatz}
et de la définition \ref{definition-ring-jacobson}.
\end{proof}
```

</details>

### 04 — lemma-jacobson-prime

Anglais L6677–6690 ; français L6657–6670.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6677) · FR-ALGEBRA-B10-CHOICE-0004.

L'implication énoncée réduit la vérification aux idéaux premiers. Elle repose sur le fait que tout idéal radical est l'intersection des premiers qui le contiennent ; ces premiers sont, par hypothèse, intersections de maximaux. La propriété s'applique à chaque premier, non seulement au nilradical. Le français garde cette seule implication, sans ajouter une réciproque à l'énoncé.

Règles : FR-ALGEBRA-B10-RULE-RADICAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-jacobson-prime}
Let $R$ be a ring. If every prime ideal of $R$ is the
intersection of the maximal ideals containing it,
then $R$ is Jacobson.
\end{lemma}

\begin{proof}
This is immediately clear from the fact that
every radical ideal $I \subset R$ is the
intersection of the primes containing it.
See Lemma \ref{lemma-Zariski-topology}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-jacobson-prime}
Soit $R$ un anneau. Si tout idéal premier de $R$ est
l'intersection des idéaux maximaux qui le contiennent,
alors $R$ est de Jacobson.
\end{lemma}

\begin{proof}
C'est immédiat du fait que
chaque idéal radical $I \subset R$ est
l'intersection des idéaux premiers qui le contiennent.
Voir le lemme \ref{lemma-Zariski-topology}.
\end{proof}
```

</details>

### 05 — lemma-jacobson

Anglais L6691–6726 ; français L6671–6706.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6691) · FR-ALGEBRA-B10-CHOICE-0005.

Espace de Jacobson est distingué d'anneau de Jacobson. La densité des points fermés est exigée dans chaque fermé ; le raisonnement teste les intersections non vides avec D(f). Ouverts principaux remplace ouverts standards : Dat, Schémas 1.2.4 p.8, désigne précisément ces mêmes D(f). La correspondance renversant les inclusions entre idéaux radicaux et fermés reste intacte.

Point particulier à relire : Ouverts principaux désigne exactement les D(f) de la source. Dat p.8 atteste ce terme ; remplacer le calque n'ajoute ni objet ni hypothèse.

Règles : FR-ALGEBRA-B10-RULE-JACOBSON, FR-ALGEBRA-B10-RULE-RADICAL, FR-ALGEBRA-B10-RULE-PRINCIPAL, FR-ALGEBRA-B10-RULE-TOPOLOGIE, FR-ALGEBRA-B10-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-jacobson}
A ring $R$ is Jacobson if and only if $\Spec(R)$
is Jacobson, see Topology,
Definition \ref{topology-definition-space-jacobson}.
\end{lemma}

\begin{proof}
Suppose $R$ is Jacobson. Let $Z \subset \Spec(R)$
be a closed subset. We have to show that the set of closed
points in $Z$ is dense in $Z$. Let $U \subset \Spec(R)$
be an open such that $U \cap Z$ is nonempty.
We have to show $Z \cap U$ contains a closed point
of $\Spec(R)$. We may
assume $U = D(f)$ as standard opens form a basis for the
topology on $\Spec(R)$. According to
Lemma \ref{lemma-Zariski-topology} we may assume that
$Z = V(I)$, where $I$ is a radical ideal. We see also
that $f \not \in I$. By assumption, there exists a
maximal ideal $\mathfrak m \subset R$ such that
$I \subset \mathfrak m$ but $f \not\in \mathfrak m$.
Hence $\mathfrak m \in D(f) \cap V(I) = U \cap Z$ as desired.

\medskip\noindent
Conversely, suppose that $\Spec(R)$ is Jacobson.
Let $I \subset R$ be a radical ideal. Let
$J = \cap_{I \subset \mathfrak m} \mathfrak m$
be the intersection of the maximal ideals containing $I$.
Clearly $J$ is a radical ideal, $V(J) \subset V(I)$, and
$V(J)$ is the smallest closed subset of $V(I)$ containing
all the closed points of $V(I)$. By assumption we see that
$V(J) = V(I)$. But Lemma \ref{lemma-Zariski-topology}
shows there is a bijection between Zariski closed
sets and radical ideals, hence $I = J$ as desired.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-jacobson}
Un anneau $R$ est de Jacobson si et seulement si $\Spec(R)$
est un espace de Jacobson, voir Topologie,
définition \ref{topology-definition-space-jacobson}.
\end{lemma}

\begin{proof}
Supposons que $R$ soit de Jacobson. Soit $Z \subset \Spec(R)$
un fermé. Nous devons montrer que l'ensemble des points
fermés de $Z$ est dense dans $Z$. Soit $U \subset \Spec(R)$
un ouvert tel que $U \cap Z$ soit non vide.
Nous devons montrer que $Z \cap U$ contient un point fermé
de $\Spec(R)$. Nous pouvons
supposer que $U = D(f)$, car les ouverts principaux forment une base de la
topologie de $\Spec(R)$. D'après le
lemme \ref{lemma-Zariski-topology}, nous pouvons supposer que
$Z = V(I)$, où $I$ est un idéal radical. Nous voyons également
que $f \not \in I$. Par hypothèse, il existe un
idéal maximal $\mathfrak m \subset R$ tel que
$I \subset \mathfrak m$ mais $f \not\in \mathfrak m$.
Ainsi, $\mathfrak m \in D(f) \cap V(I) = U \cap Z$, comme voulu.

\medskip\noindent
Réciproquement, supposons que $\Spec(R)$ soit un espace de Jacobson.
Soit $I \subset R$ un idéal radical. Soit
$J = \cap_{I \subset \mathfrak m} \mathfrak m$
l'intersection des idéaux maximaux qui contiennent $I$.
Manifestement, $J$ est un idéal radical, $V(J) \subset V(I)$, et
$V(J)$ est le plus petit fermé de $V(I)$ qui contient
tous les points fermés de $V(I)$. Par hypothèse, nous voyons que
$V(J) = V(I)$. Mais le lemme \ref{lemma-Zariski-topology}
montre qu'il existe une bijection entre les fermés de Zariski
et les idéaux radicaux ; ainsi, $I = J$, comme voulu.
\end{proof}
```

</details>

### 06 — lemma-characterize-jacobson

Anglais L6727–6777 ; français L6707–6757.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6727) · FR-ALGEBRA-B10-CHOICE-0006.

Les quatre propriétés du couple (p,f), puis la conclusion d'infinité dans le cas Jacobson, sont conservées séparément. Un point fermé dans le sous-espace T∩D(f) ne doit pas être confondu avec un point fermé de Spec(R). Les mots manquants dans deux généralisations informelles de la preuve ne sont pas ajoutés silencieusement ; le sous-espace effectivement utilisé est non vide et son anneau est non nul. Voir l'observation séparée.

Point particulier à relire : La phrase générale sur tout localement fermé omet non vide ; le singleton utilisé est non vide. Tout anneau possède un maximal présuppose ici l'anneau non nul donné par le spectre non vide. Ces précisions restent hors traduction.

Règles : FR-ALGEBRA-B10-RULE-JACOBSON, FR-ALGEBRA-B10-RULE-RADICAL, FR-ALGEBRA-B10-RULE-TOPOLOGIE, FR-ALGEBRA-B10-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-jacobson}
Let $R$ be a ring. If $R$ is not Jacobson there exist
a prime $\mathfrak p \subset R$, an element $f \in R$
such that the following hold
\begin{enumerate}
\item $\mathfrak p$ is not a maximal ideal,
\item $f \not \in \mathfrak p$,
\item $V(\mathfrak p) \cap D(f) = \{\mathfrak p\}$, and
\item $(R/\mathfrak p)_f$ is a field.
\end{enumerate}
On the other hand, if $R$ is Jacobson, then for any pair $(\mathfrak p, f)$
such that (1) and (2) hold the set $V(\mathfrak p) \cap D(f)$ is
infinite.
\end{lemma}

\begin{proof}
Assume $R$ is not Jacobson.
By Lemma \ref{lemma-jacobson} this means there exists an
closed subset $T \subset \Spec(R)$
whose set $T_0 \subset T$ of closed points is not dense in $T$.
Choose an $f \in R$ such that $T_0 \subset V(f)$ but
$T \not \subset V(f)$. Note that $T \cap D(f)$
is homeomorphic to $\Spec((R/I)_f)$ if $T = V(I)$, see
Lemmas \ref{lemma-spec-closed} and \ref{lemma-standard-open}.
As any ring has a maximal ideal
(Lemma \ref{lemma-Zariski-topology}) we can choose a closed point $t$ of
space $T \cap D(f)$. Then $t$ corresponds to a prime ideal
$\mathfrak p \subset R$ which is not maximal (as $t \not \in T_0$).
Thus (1) holds. By construction $f \not \in \mathfrak p$, hence (2).
As $t$ is a closed point of $T \cap D(f)$ we see that
$V(\mathfrak p) \cap D(f) = \{\mathfrak p\}$, i.e., (3) holds. Hence we
conclude that $(R/\mathfrak p)_f$ is a domain whose
spectrum has one point, hence (4) holds
(for example combine Lemmas \ref{lemma-characterize-local-ring} and
\ref{lemma-minimal-prime-reduced-ring}).

\medskip\noindent
Conversely, suppose that $R$ is Jacobson and $(\mathfrak p, f)$
satisfy (1) and (2). If
$V(\mathfrak p) \cap D(f) =
\{\mathfrak p, \mathfrak q_1, \ldots, \mathfrak q_t\}$
then $\mathfrak p \not = \mathfrak q_i$
implies there exists an element $g \in R$ such that $g \not \in \mathfrak p$
but $g \in \mathfrak q_i$ for all $i$. Hence
$V(\mathfrak p) \cap D(fg) = \{\mathfrak p\}$ which
is impossible since each locally closed subset of $\Spec(R)$
contains at least one closed point as $\Spec(R)$ is
a Jacobson topological space.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-characterize-jacobson}
Soit $R$ un anneau. Si $R$ n'est pas de Jacobson, il existe
un idéal premier $\mathfrak p \subset R$ et un élément $f \in R$
tels que les propriétés suivantes soient satisfaites :
\begin{enumerate}
\item $\mathfrak p$ n'est pas un idéal maximal,
\item $f \not \in \mathfrak p$,
\item $V(\mathfrak p) \cap D(f) = \{\mathfrak p\}$, et
\item $(R/\mathfrak p)_f$ est un corps.
\end{enumerate}
En revanche, si $R$ est de Jacobson, alors, pour toute paire $(\mathfrak p, f)$
qui satisfait (1) et (2), l'ensemble $V(\mathfrak p) \cap D(f)$ est
infini.
\end{lemma}

\begin{proof}
Supposons que $R$ ne soit pas de Jacobson.
D'après le lemme \ref{lemma-jacobson}, cela signifie qu'il existe un
fermé $T \subset \Spec(R)$
dont l'ensemble $T_0 \subset T$ des points fermés n'est pas dense dans $T$.
Choisissons un $f \in R$ tel que $T_0 \subset V(f)$ mais
$T \not \subset V(f)$. Notons que $T \cap D(f)$
est homéomorphe à $\Spec((R/I)_f)$ si $T = V(I)$, voir les
lemmes \ref{lemma-spec-closed} et \ref{lemma-standard-open}.
Comme tout anneau possède un idéal maximal
(lemme \ref{lemma-Zariski-topology}), nous pouvons choisir un point fermé $t$ de
l'espace $T \cap D(f)$. Alors $t$ correspond à un idéal premier
$\mathfrak p \subset R$ qui n'est pas maximal (car $t \not \in T_0$).
Ainsi, (1) est satisfaite. Par construction, $f \not \in \mathfrak p$, d'où (2).
Comme $t$ est un point fermé de $T \cap D(f)$, nous voyons que
$V(\mathfrak p) \cap D(f) = \{\mathfrak p\}$, c'est-à-dire que (3) est satisfaite. Nous
concluons donc que $(R/\mathfrak p)_f$ est un anneau intègre dont le
spectre a un seul point, d'où (4)
(on peut par exemple combiner les lemmes \ref{lemma-characterize-local-ring} et
\ref{lemma-minimal-prime-reduced-ring}).

\medskip\noindent
Réciproquement, supposons que $R$ soit de Jacobson et que $(\mathfrak p, f)$
satisfasse (1) et (2). Si
$V(\mathfrak p) \cap D(f) =
\{\mathfrak p, \mathfrak q_1, \ldots, \mathfrak q_t\}$,
alors $\mathfrak p \not = \mathfrak q_i$
implique qu'il existe un élément $g \in R$ tel que $g \not \in \mathfrak p$
mais $g \in \mathfrak q_i$ pour tout $i$. Ainsi,
$V(\mathfrak p) \cap D(fg) = \{\mathfrak p\}$, ce qui
est impossible puisque tout sous-ensemble localement fermé de $\Spec(R)$
contient au moins un point fermé, car $\Spec(R)$ est
un espace topologique de Jacobson.
\end{proof}
```

</details>

### 07 — lemma-pid-jacobson

Anglais L6778–6808 ; français L6758–6788.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6778) · FR-ALGEBRA-B10-CHOICE-0007.

Le label contient pid, mais l'énoncé ne suppose pas que R soit principal. Ses quatre hypothèses exactes sont intégrité, noethérianité, maximalité de chaque premier non nul et infinité des maximaux. Pour x non nul, R/xR n'a que des premiers minimaux ; la finitude des composantes du spectre noethérien rend V(x) fini. L'exemple Z satisfait ces conditions, sans donner la même conclusion pour toutes ses localisations.

Règles : FR-ALGEBRA-B10-RULE-JACOBSON, FR-ALGEBRA-B10-RULE-RADICAL, FR-ALGEBRA-B10-RULE-MATRICES, FR-ALGEBRA-B10-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-pid-jacobson}
The ring $\mathbf{Z}$ is a Jacobson ring.
More generally, let $R$ be a ring such that
\begin{enumerate}
\item $R$ is a domain,
\item $R$ is Noetherian,
\item any nonzero prime ideal is a maximal ideal, and
\item $R$ has infinitely many maximal ideals.
\end{enumerate}
Then $R$ is a Jacobson ring.
\end{lemma}

\begin{proof}
Let $R$ satisfy (1), (2), (3) and (4). The statement
means that $(0) = \bigcap_{\mathfrak m \subset R} \mathfrak m$.
Since $R$ has infinitely many maximal ideals it suffices to
show that any nonzero $x \in R$ is contained in at most
finitely many maximal ideals, in other words that $V(x)$ is finite.
By Lemma \ref{lemma-spec-closed}
we see that $V(x)$ is homeomorphic to $\Spec(R/xR)$.
By assumption (3) every prime of $R/xR$ is minimal and hence
corresponds to an irreducible component of $\Spec(R/xR)$
(Lemma \ref{lemma-irreducible}).
As $R/xR$ is Noetherian, the topological space $\Spec(R/xR)$
is Noetherian (Lemma \ref{lemma-Noetherian-topology})
and has finitely many irreducible components
(Topology, Lemma \ref{topology-lemma-Noetherian}).
Thus $V(x)$ is finite as desired.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-pid-jacobson}
L'anneau $\mathbf{Z}$ est un anneau de Jacobson.
Plus généralement, soit $R$ un anneau tel que
\begin{enumerate}
\item $R$ soit un anneau intègre,
\item $R$ soit noethérien,
\item tout idéal premier non nul soit un idéal maximal, et
\item $R$ possède une infinité d'idéaux maximaux.
\end{enumerate}
Alors $R$ est un anneau de Jacobson.
\end{lemma}

\begin{proof}
Soit $R$ satisfaisant (1), (2), (3) et (4). L'assertion
signifie que $(0) = \bigcap_{\mathfrak m \subset R} \mathfrak m$.
Puisque $R$ possède une infinité d'idéaux maximaux, il suffit de
montrer que tout $x \in R$ non nul appartient à seulement
un nombre fini d'idéaux maximaux, autrement dit que $V(x)$ est fini.
D'après le lemme \ref{lemma-spec-closed},
nous voyons que $V(x)$ est homéomorphe à $\Spec(R/xR)$.
Par l'hypothèse (3), tout idéal premier de $R/xR$ est minimal et
correspond donc à une composante irréductible de $\Spec(R/xR)$
(lemme \ref{lemma-irreducible}).
Comme $R/xR$ est noethérien, l'espace topologique $\Spec(R/xR)$
est noethérien (lemme \ref{lemma-Noetherian-topology})
et possède un nombre fini de composantes irréductibles
(Topologie, lemme \ref{topology-lemma-Noetherian}).
Ainsi, $V(x)$ est fini, comme voulu.
\end{proof}
```

</details>

### 08 — example-infinite-product-fields-jacobson

Anglais L6809–6828 ; français L6789–6808.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6809) · FR-ALGEBRA-B10-CHOICE-0008.

Le produit peut être infini et n'est pas supposé noethérien. La factorisation d'un élément comme unité fois idempotent permet de voir la localisation principale comme un quotient. Le raisonnement ne prétend pas que tous les idéaux maximaux du produit sont les noyaux des projections ; cette simplification serait fausse en général.

Règles : FR-ALGEBRA-B10-RULE-RADICAL, FR-ALGEBRA-B10-RULE-MATRICES.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-infinite-product-fields-jacobson}
Let $A$ be an infinite set.
For each $\alpha \in A$, let $k_\alpha$ be a field.
We claim that $R = \prod_{\alpha\in A} k_\alpha$ is Jacobson.
First, note that any element $f \in R$ has the form
$f = ue$, with $u \in R$ a unit and $e\in R$ an idempotent
(left to the reader).
Hence $D(f) = D(e)$, and $R_f = R_e = R/(1-e)$ is a quotient of $R$.
Actually, any ring with this property is Jacobson.
Namely, say $\mathfrak p \subset R$ is a prime ideal
and $f \in R$, $f \not \in \mathfrak p$. We have to find
a maximal ideal $\mathfrak m$ of $R$ such that
$\mathfrak p \subset \mathfrak m$ and $f \not\in \mathfrak m$.
Because $R_f$ is a quotient of $R$ we see that any maximal
ideal of $R_f$ corresponds to a maximal ideal of $R$
not containing $f$. Hence the result follows
by choosing a maximal ideal of $R_f$ containing $\mathfrak p R_f$.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-infinite-product-fields-jacobson}
Soit $A$ un ensemble infini.
Pour chaque $\alpha \in A$, soit $k_\alpha$ un corps.
Nous affirmons que $R = \prod_{\alpha\in A} k_\alpha$ est de Jacobson.
Remarquons d'abord que tout élément $f \in R$ est de la forme
$f = ue$, où $u \in R$ est une unité et $e\in R$ un idempotent
(laissé au lecteur).
Ainsi, $D(f) = D(e)$, et $R_f = R_e = R/(1-e)$ est un quotient de $R$.
En fait, tout anneau possédant cette propriété est de Jacobson.
En effet, soit $\mathfrak p \subset R$ un idéal premier
et $f \in R$, $f \not \in \mathfrak p$. Nous devons trouver
un idéal maximal $\mathfrak m$ de $R$ tel que
$\mathfrak p \subset \mathfrak m$ et $f \not\in \mathfrak m$.
Puisque $R_f$ est un quotient de $R$, nous voyons que tout idéal
maximal de $R_f$ correspond à un idéal maximal de $R$
ne contenant pas $f$. Le résultat s'obtient donc
en choisissant un idéal maximal de $R_f$ contenant $\mathfrak p R_f$.
\end{example}
```

</details>

### 09 — example-not-jacobson

Anglais L6829–6843 ; français L6809–6823.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6829) · FR-ALGEBRA-B10-CHOICE-0009.

Le premier argument concerne un anneau intègre semi-local qui n'est pas un corps. La conclusion concernant un anneau local ayant au moins deux premiers a sa propre justification : chaque premier devrait être l'intersection des maximaux qui le contiennent, alors qu'il n'y a qu'un maximal. Semi-local signifie nombre fini de maximaux, non nombre fini de tous les premiers.

Règles : FR-ALGEBRA-B10-RULE-JACOBSON, FR-ALGEBRA-B10-RULE-RADICAL, FR-ALGEBRA-B10-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-not-jacobson}
A domain $R$ with finitely many maximal ideals
$\mathfrak m_i$, $i = 1, \ldots, n$ is not a
Jacobson ring, except when it is a field.
Namely, in this case $(0)$ is not the intersection
of the maximal ideals $(0) \not =
\mathfrak m_1 \cap \mathfrak m_2 \cap \ldots \cap \mathfrak m_n
\supset \mathfrak m_1 \cdot \mathfrak m_2 \cdot \ldots
\cdot \mathfrak m_n \not = 0$.
In particular a discrete valuation ring, or any local ring with
at least two prime ideals is not a Jacobson
ring.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-not-jacobson}
Un anneau intègre $R$ possédant un nombre fini d'idéaux maximaux
$\mathfrak m_i$, $i = 1, \ldots, n$, n'est pas un
anneau de Jacobson, sauf s'il s'agit d'un corps.
En effet, dans ce cas, $(0)$ n'est pas l'intersection
des idéaux maximaux : $(0) \not =
\mathfrak m_1 \cap \mathfrak m_2 \cap \ldots \cap \mathfrak m_n
\supset \mathfrak m_1 \cdot \mathfrak m_2 \cdot \ldots
\cdot \mathfrak m_n \not = 0$.
En particulier, un anneau de valuation discrète, ou tout anneau local ayant
au moins deux idéaux premiers, n'est pas un anneau
de Jacobson.
\end{example}
```

</details>

### 10 — lemma-finite-residue-extension-closed

Anglais L6844–6871 ; français L6824–6851.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6844) · FR-ALGEBRA-B10-CHOICE-0010.

Le nom du label ne gouverne pas l'énoncé : l'extension résiduelle est algébrique, pas nécessairement finie. Le maximal m de R est donné ; le premier q de S situé au-dessus de m est celui dont on conclut la maximalité. L'anneau intermédiaire S/q entre κ(m) et l'extension algébrique κ(q) est un corps. Corps résiduel et extension algébrique ont le registre attesté chez Dat p.98–99.

Règles : FR-ALGEBRA-B10-RULE-RADICAL, FR-ALGEBRA-B10-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-finite-residue-extension-closed}
Let $R \to S$ be a ring map.
Let $\mathfrak m \subset R$ be a maximal ideal.
Let $\mathfrak q \subset S$ be a prime ideal
lying over $\mathfrak m$ such that $\kappa(\mathfrak q)/\kappa(\mathfrak m)$
is an algebraic field extension.
Then $\mathfrak q$ is a maximal ideal of $S$.
\end{lemma}

\begin{proof}
Consider the diagram
$$
\xymatrix{
S \ar[r] & S/\mathfrak q \ar[r] & \kappa(\mathfrak q) \\
R \ar[r] \ar[u] & R/\mathfrak m \ar[u]
}
$$
We see that $\kappa(\mathfrak m) \subset S/\mathfrak q \subset
\kappa(\mathfrak q)$. Because the field extension
$\kappa(\mathfrak m) \subset \kappa(\mathfrak q)$
is algebraic, any ring between $\kappa(\mathfrak m)$
and $\kappa(\mathfrak q)$ is a field
(Fields, Lemma \ref{fields-lemma-subalgebra-algebraic-extension-field}).
Thus $S/\mathfrak q$ is a field, and a posteriori equal
to $\kappa(\mathfrak q)$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-finite-residue-extension-closed}
Soit $R \to S$ un morphisme d'anneaux.
Soit $\mathfrak m \subset R$ un idéal maximal.
Soit $\mathfrak q \subset S$ un idéal premier
au-dessus de $\mathfrak m$ tel que $\kappa(\mathfrak q)/\kappa(\mathfrak m)$
soit une extension algébrique de corps.
Alors $\mathfrak q$ est un idéal maximal de $S$.
\end{lemma}

\begin{proof}
Considérons le diagramme
$$
\xymatrix{
S \ar[r] & S/\mathfrak q \ar[r] & \kappa(\mathfrak q) \\
R \ar[r] \ar[u] & R/\mathfrak m \ar[u]
}
$$
Nous voyons que $\kappa(\mathfrak m) \subset S/\mathfrak q \subset
\kappa(\mathfrak q)$. Puisque l'extension de corps
$\kappa(\mathfrak m) \subset \kappa(\mathfrak q)$
est algébrique, tout anneau compris entre $\kappa(\mathfrak m)$
et $\kappa(\mathfrak q)$ est un corps
(Corps, lemme \ref{fields-lemma-subalgebra-algebraic-extension-field}).
Ainsi, $S/\mathfrak q$ est un corps, et est donc égal
à $\kappa(\mathfrak q)$.
\end{proof}
```

</details>

### 11 — lemma-dimension

Anglais L6872–6890 ; français L6852–6870.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6872) · FR-ALGEBRA-B10-CHOICE-0011.

La dimension de V est strictement inférieure au cardinal de k ; V est non nul et n'est pas supposé de dimension finie. La conclusion est l'existence d'un polynôme unitaire P avec P(T) non inversible, et non P(T)=0 ni l'algébricité de tout endomorphisme. Si tous ces P(T) étaient inversibles, V deviendrait un espace sur k(t), dont les fractions 1/(t−λ) donnent une dimension sur k trop grande. Ces distinctions restent explicites dans la lecture de la traduction.

Point particulier à relire : Non nul pour V et strictement inférieur pour la dimension sont essentiels ; P(T) non inversible ne signifie pas P(T) nul. Pas d'attestation lexicale externe nouvelle pour chaque phrase de cette preuve.

Règles : FR-ALGEBRA-B10-RULE-CARDINAL, FR-ALGEBRA-B10-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-dimension}
Suppose that $k$ is a field and suppose that $V$ is a nonzero vector
space over $k$. Assume the dimension of $V$ (which is a cardinal number)
is smaller than the cardinality of $k$. Then for any linear operator
$T : V \to V$ there exists some monic polynomial $P(t) \in k[t]$ such that
$P(T)$ is not invertible.
\end{lemma}

\begin{proof}
If not then $V$ inherits the structure of a vector space over
the field $k(t)$. But the dimension of $k(t)$ over $k$ is
at least the cardinality of $k$ for example due to the fact that the elements
$\frac{1}{t - \lambda}$ are $k$-linearly independent.
\end{proof}

\noindent
Here is another version of Hilbert's Nullstellensatz.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-dimension}
Supposons que $k$ soit un corps et que $V$ soit un espace vectoriel non nul
sur $k$. Supposons que la dimension de $V$ (qui est un nombre cardinal)
soit strictement inférieure au cardinal de $k$. Alors, pour tout endomorphisme
$T : V \to V$, il existe un polynôme unitaire $P(t) \in k[t]$ tel que
$P(T)$ ne soit pas inversible.
\end{lemma}

\begin{proof}
Sinon, $V$ hérite d'une structure d'espace vectoriel sur
le corps $k(t)$. Or la dimension de $k(t)$ sur $k$ est
au moins égale au cardinal de $k$, par exemple parce que les éléments
$\frac{1}{t - \lambda}$ sont linéairement indépendants sur $k$.
\end{proof}

\noindent
Voici une autre version du Nullstellensatz de Hilbert.
```

</details>

### 12 — theorem-uncountable-nullstellensatz

Anglais L6891–6944 ; français L6871–6924.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6891) · FR-ALGEBRA-B10-CHOICE-0012.

La seule borne de l'énoncé est #I<#k ; k n'y est pas supposé non dénombrable. Si I est fini, le Nullstellensatz ordinaire suffit, y compris sur un corps fini ou dénombrable. Si I est infini, la borne force alors k à être non dénombrable ; les monômes ont le cardinal de I et ajouter une variable ne le change pas. La conclusion résiduelle est algébrique, sans degré fini imposé. Dat fournit le registre usuel mais ne prouve pas cette généralisation dans les pages lues.

Point particulier à relire : Ne pas renforcer algébrique en finie. La source française consultée atteste les termes usuels, non l'énoncé à nombre infini de générateurs.

Règles : FR-ALGEBRA-B10-RULE-JACOBSON, FR-ALGEBRA-B10-RULE-RADICAL, FR-ALGEBRA-B10-RULE-FINITE, FR-ALGEBRA-B10-RULE-CARDINAL, FR-ALGEBRA-B10-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{theorem}
\label{theorem-uncountable-nullstellensatz}
Let $k$ be a field. Let $S$ be a $k$-algebra generated over $k$
by the elements $\{x_i\}_{i \in I}$. Assume the cardinality of $I$
is smaller than the cardinality of $k$. Then
\begin{enumerate}
\item for all maximal ideals $\mathfrak m \subset S$ the field
extension $\kappa(\mathfrak m)/k$
is algebraic, and
\item $S$ is a Jacobson ring.
\end{enumerate}
\end{theorem}

\begin{proof}
If $I$ is finite then the result follows from the Hilbert Nullstellensatz,
Theorem \ref{theorem-nullstellensatz}. In the rest of the proof we assume
$I$ is infinite. It suffices to prove the result for
$\mathfrak m \subset k[\{x_i\}_{i \in I}]$ maximal in the polynomial
ring on variables $x_i$, since $S$ is a quotient of this.
As $I$ is infinite the set
of monomials $x_{i_1}^{e_1} \ldots x_{i_r}^{e_r}$, $i_1, \ldots, i_r \in I$
and $e_1, \ldots, e_r \geq 0$ has cardinality at most equal to the
cardinality of $I$. Because the cardinality of $I \times \ldots \times I$
is the cardinality of $I$, and also the cardinality of
$\bigcup_{n \geq 0} I^n$ has the same cardinality.
(If $I$ is finite, then this is not true and
in that case this proof only works if $k$ is uncountable.)

\medskip\noindent
To arrive at a contradiction pick $T \in \kappa(\mathfrak m)$ transcendental
over $k$. Note that the $k$-linear map
$T : \kappa(\mathfrak m) \to \kappa(\mathfrak m)$
given by multiplication by $T$ has the property that $P(T)$ is invertible
for all monic polynomials $P(t) \in k[t]$.
Also, $\kappa(\mathfrak m)$ has dimension at most the cardinality of $I$
over $k$ since it is a quotient of the vector space
$k[\{x_i\}_{i \in I}]$ over $k$ (whose dimension is $\# I$ as we saw above).
This is impossible by Lemma \ref{lemma-dimension}.

\medskip\noindent
To show that $S$ is Jacobson we argue as follows. If not then
there exists a prime $\mathfrak q \subset S$ and an element $f \in S$,
$f \not \in \mathfrak q$ such that $\mathfrak q$ is not maximal
and $(S/\mathfrak q)_f$ is a field, see
Lemma \ref{lemma-characterize-jacobson}.
But note that $(S/\mathfrak q)_f$ is generated by at most $\# I + 1$ elements.
Hence the field extension $(S/\mathfrak q)_f/k$ is algebraic
(by the first part of the proof).
This implies that $\kappa(\mathfrak q)$ is an algebraic extension of $k$
hence $\mathfrak q$ is maximal by
Lemma \ref{lemma-finite-residue-extension-closed}. This contradiction
finishes the proof.
\end{proof}
```

Français restauré :
```tex
\begin{theorem}
\label{theorem-uncountable-nullstellensatz}
Soit $k$ un corps. Soit $S$ une $k$-algèbre engendrée sur $k$
par les éléments $\{x_i\}_{i \in I}$. Supposons que le cardinal de $I$
soit strictement inférieur au cardinal de $k$. Alors
\begin{enumerate}
\item pour tout idéal maximal $\mathfrak m \subset S$, l'extension de corps
$\kappa(\mathfrak m)/k$
est algébrique, et
\item $S$ est un anneau de Jacobson.
\end{enumerate}
\end{theorem}

\begin{proof}
Si $I$ est fini, le résultat découle du Nullstellensatz de Hilbert,
théorème \ref{theorem-nullstellensatz}. Dans la suite de la démonstration, nous supposons
$I$ infini. Il suffit de démontrer le résultat lorsque
$\mathfrak m \subset k[\{x_i\}_{i \in I}]$ est maximal dans l'anneau
de polynômes en les variables $x_i$, puisque $S$ en est un quotient.
Puisque $I$ est infini, l'ensemble
des monômes $x_{i_1}^{e_1} \ldots x_{i_r}^{e_r}$, $i_1, \ldots, i_r \in I$
et $e_1, \ldots, e_r \geq 0$, est de cardinal inférieur ou égal au
cardinal de $I$. En effet, le cardinal de $I \times \ldots \times I$
est le cardinal de $I$, et le cardinal de
$\bigcup_{n \geq 0} I^n$ est lui aussi le même.
(Si $I$ est fini, cela n'est plus vrai et,
dans ce cas, cette démonstration ne fonctionne que si $k$ est non dénombrable.)

\medskip\noindent
Pour obtenir une contradiction, choisissons $T \in \kappa(\mathfrak m)$ transcendant
sur $k$. Notons que l'application $k$-linéaire
$T : \kappa(\mathfrak m) \to \kappa(\mathfrak m)$
donnée par la multiplication par $T$ possède la propriété que $P(T)$ est inversible
pour tout polynôme unitaire $P(t) \in k[t]$.
De plus, $\kappa(\mathfrak m)$ est de dimension au plus égale au cardinal de $I$
sur $k$, puisqu'il s'agit d'un quotient de l'espace vectoriel
$k[\{x_i\}_{i \in I}]$ sur $k$ (dont la dimension vaut $\# I$, comme vu ci-dessus).
C'est impossible d'après le lemme \ref{lemma-dimension}.

\medskip\noindent
Pour montrer que $S$ est de Jacobson, raisonnons comme suit. Sinon,
il existe un idéal premier $\mathfrak q \subset S$ et un élément $f \in S$,
$f \not \in \mathfrak q$, tels que $\mathfrak q$ ne soit pas maximal
et que $(S/\mathfrak q)_f$ soit un corps, voir le
lemme \ref{lemma-characterize-jacobson}.
Mais remarquons que $(S/\mathfrak q)_f$ est engendré par au plus $\# I + 1$ éléments.
Ainsi, l'extension de corps $(S/\mathfrak q)_f/k$ est algébrique
(d'après la première partie de la démonstration).
Cela implique que $\kappa(\mathfrak q)$ est une extension algébrique de $k$ ;
donc $\mathfrak q$ est maximal d'après le
lemme \ref{lemma-finite-residue-extension-closed}. Cette contradiction
achève la démonstration.
\end{proof}
```

</details>

### 13 — lemma-base-change-Jacobson

Anglais L6945–6964 ; français L6925–6944.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6945) · FR-ALGEBRA-B10-CHOICE-0013.

Changement de base signifie ici produit tensoriel sur k avec une extension K. La comparaison de cardinalités porte sur l'ensemble sous-jacent à S, non sur une dimension vectorielle arbitrairement substituée. L'hypothèse sur la taille de K reste visible ; il n'est pas affirmé que tout changement de corps produise la même situation.

Règles : FR-ALGEBRA-B10-RULE-JACOBSON, FR-ALGEBRA-B10-RULE-RADICAL, FR-ALGEBRA-B10-RULE-CARDINAL, FR-ALGEBRA-B10-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-base-change-Jacobson}
Let $k$ be a field. Let $S$ be a $k$-algebra.
For any field extension $K/k$ whose cardinality is larger
than the cardinality of $S$ we have
\begin{enumerate}
\item for every maximal ideal $\mathfrak m$ of $S_K$ the field
$\kappa(\mathfrak m)$ is algebraic over $K$, and
\item $S_K$ is a Jacobson ring.
\end{enumerate}
\end{lemma}

\begin{proof}
Choose $k \subset K$ such that the cardinality of $K$ is greater
than the cardinality of $S$. Since the elements of $S$ generate
the $K$-algebra $S_K$ we see that
Theorem \ref{theorem-uncountable-nullstellensatz}
applies.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-base-change-Jacobson}
Soit $k$ un corps. Soit $S$ une $k$-algèbre.
Pour toute extension de corps $K/k$ dont le cardinal est strictement supérieur
au cardinal de $S$, nous avons :
\begin{enumerate}
\item pour tout idéal maximal $\mathfrak m$ de $S_K$, le corps
$\kappa(\mathfrak m)$ est algébrique sur $K$, et
\item $S_K$ est un anneau de Jacobson.
\end{enumerate}
\end{lemma}

\begin{proof}
Considérons $k \subset K$ tel que le cardinal de $K$ soit supérieur
au cardinal de $S$. Puisque les éléments de $S$ engendrent
la $K$-algèbre $S_K$, nous voyons que le
théorème \ref{theorem-uncountable-nullstellensatz}
s'applique.
\end{proof}
```

</details>

### 14 — example-countable-trick-does-not-work

Anglais L6965–6979 ; français L6945–6959.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6965) · FR-ALGEBRA-B10-CHOICE-0014.

Le corps k et l'ensemble des générateurs sont ici dénombrables. Les relations fx_f=1 imposent l'inversion de tous les polynômes non nuls f de k[x], et non des seuls x−a ; cela donne R/I=k(x), déjà un corps. L'idéal maximal contenant I est donc I lui-même. La réutilisation de I comme index puis comme idéal, et la formulation condensée sur k⊂R/m, restent celles de la source. Aucun symbole n'est changé pour les simplifier.

Point particulier à relire : La collision de notation I est préservée ; elle n'est pas un échec de traduction ni une raison de renommer silencieusement.

Règles : FR-ALGEBRA-B10-RULE-RADICAL, FR-ALGEBRA-B10-RULE-CARDINAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-countable-trick-does-not-work}
The trick in the proof of
Theorem \ref{theorem-uncountable-nullstellensatz}
really does not work if $k$ is a countable field and $I$ is countable too.
Let $k$ be a countable field. Let $x$ be a variable,
and let $k(x)$ be the field of rational functions in $x$.
Consider the polynomial algebra $R = k[x, \{x_f\}_{f \in k[x]-\{0\}}]$.
Let $I = (\{fx_f - 1\}_{f\in k[x] - \{0\}})$. Note that
$I$ is a proper ideal in $R$.
Choose a maximal ideal $I \subset \mathfrak m$.
Then $k \subset R/\mathfrak m$ is isomorphic to
$k(x)$, and is not algebraic over $k$.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-countable-trick-does-not-work}
L'astuce employée dans la démonstration du
théorème \ref{theorem-uncountable-nullstellensatz}
ne fonctionne réellement pas si $k$ est un corps dénombrable et $I$ est lui aussi dénombrable.
Soit $k$ un corps dénombrable. Soit $x$ une indéterminée,
et soit $k(x)$ le corps des fractions rationnelles en $x$.
Considérons l'algèbre polynomiale $R = k[x, \{x_f\}_{f \in k[x]-\{0\}}]$.
Soit $I = (\{fx_f - 1\}_{f\in k[x] - \{0\}})$. Remarquons que
$I$ est un idéal propre de $R$.
Choisissons un idéal maximal $I \subset \mathfrak m$.
Alors $k \subset R/\mathfrak m$ est isomorphe à
$k(x)$, et n'est pas algébrique sur $k$.
\end{example}
```

</details>

### 15 — lemma-Jacobson-invert-element

Anglais L6980–6994 ; français L6960–6974.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6980) · FR-ALGEBRA-B10-CHOICE-0015.

La localisation par les puissances d'un seul élément conserve la propriété de Jacobson et identifie les maximaux avec ceux évitant cet élément. Il ne s'agit pas d'une bijection avec tous les maximaux de R. La preuve utilise l'héritage topologique sur l'ouvert D(f), puis l'équivalence anneau/espace de Jacobson ; on ne lui substitue pas la proposition ultérieure de permanence par type fini.

Règles : FR-ALGEBRA-B10-RULE-JACOBSON, FR-ALGEBRA-B10-RULE-RADICAL, FR-ALGEBRA-B10-RULE-TOPOLOGIE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Jacobson-invert-element}
Let $R$ be a Jacobson ring. Let $f \in R$. The ring $R_f$ is Jacobson and
maximal ideals of $R_f$ correspond to maximal ideals of $R$ not containing $f$.
\end{lemma}

\begin{proof}
By Topology, Lemma \ref{topology-lemma-jacobson-inherited}
we see that $D(f) = \Spec(R_f)$ is Jacobson and
that closed points of $D(f)$
correspond to closed points in $\Spec(R)$
which happen to lie in $D(f)$. Thus $R_f$ is Jacobson by
Lemma \ref{lemma-jacobson}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-Jacobson-invert-element}
Soit $R$ un anneau de Jacobson. Soit $f \in R$. L'anneau $R_f$ est de Jacobson, et
les idéaux maximaux de $R_f$ correspondent aux idéaux maximaux de $R$ qui ne contiennent pas $f$.
\end{lemma}

\begin{proof}
D'après Topologie, lemme \ref{topology-lemma-jacobson-inherited},
nous voyons que $D(f) = \Spec(R_f)$ est de Jacobson et
que les points fermés de $D(f)$
correspondent aux points fermés de $\Spec(R)$
qui appartiennent à $D(f)$. Ainsi, $R_f$ est de Jacobson d'après le
lemme \ref{lemma-jacobson}.
\end{proof}
```

</details>

### 16 — example-localize-not-preserve-closed-points

Anglais L6995–7006 ; français L6975–6986.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6995) · FR-ALGEBRA-B10-CHOICE-0016.

Le point fermé du spectre du corps Q est envoyé sur le point générique de Spec(Z_(2)) par l'application spectrale induite, non par une application directe sur les éléments des anneaux. Le raccourci de la source nomme le morphisme d'anneaux ; il reste littéral et est explicité séparément. L'exemple réfute la correspondance des points fermés sans Jacobson, pas le fait que Q soit de Jacobson.

Point particulier à relire : Lire la phrase par contravariance des spectres ; le raccourci reste explicité uniquement dans le dossier.

Règles : FR-ALGEBRA-B10-RULE-LOCALISATION, FR-ALGEBRA-B10-RULE-TOPOLOGIE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-localize-not-preserve-closed-points}
Here is a simple example that shows Lemma \ref{lemma-Jacobson-invert-element}
to be false if $R$ is not Jacobson.
Consider the ring $R = \mathbf{Z}_{(2)}$, i.e., the localization
of $\mathbf{Z}$ at the prime $(2)$. The localization of $R$ at
the element $2$ is isomorphic to $\mathbf{Q}$, in a formula:
$R_2 \cong \mathbf{Q}$. Clearly the map $R \to R_2$ maps the
closed point of $\Spec(\mathbf{Q})$ to the generic point
of $\Spec(R)$.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-localize-not-preserve-closed-points}
Voici un exemple simple qui montre que le lemme \ref{lemma-Jacobson-invert-element}
est faux si $R$ n'est pas de Jacobson.
Considérons l'anneau $R = \mathbf{Z}_{(2)}$, c'est-à-dire la localisation
de $\mathbf{Z}$ en l'idéal premier $(2)$. La localisation de $R$ par
l'élément $2$ est isomorphe à $\mathbf{Q}$ ; sous forme d'une formule :
$R_2 \cong \mathbf{Q}$. Manifestement, le morphisme $R \to R_2$ envoie le
point fermé de $\Spec(\mathbf{Q})$ sur le point générique
de $\Spec(R)$.
\end{example}
```

</details>

### 17 — example-infinite-localize-not-preserve-closed-points

Anglais L7007–7020 ; français L6987–7000.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7007) · FR-ALGEBRA-B10-CHOICE-0017.

Z est de Jacobson, mais inverser tous ses éléments non nuls ne conserve pas la propriété relative des points fermés annoncée pour une localisation principale. Q demeure un corps, donc un anneau de Jacobson. Le texte n'est pas interprété comme un contre-exemple à cette dernière propriété. Le même raccourci morphisme d'anneaux/application spectrale est documenté.

Point particulier à relire : L'échec concerne l'image des points fermés, non le caractère Jacobson du corps localisé.

Règles : FR-ALGEBRA-B10-RULE-LOCALISATION, FR-ALGEBRA-B10-RULE-TOPOLOGIE, FR-ALGEBRA-B10-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-infinite-localize-not-preserve-closed-points}
Here is a simple example that shows
Lemma \ref{lemma-Jacobson-invert-element}
is false if $R$ is Jacobson but we localize at infinitely
many elements.
Namely, let $R = \mathbf{Z}$ and consider the localization
$(R \setminus \{0\})^{-1}R \cong \mathbf{Q}$
of $R$ at the set of all nonzero elements.
Clearly the map $\mathbf{Z} \to \mathbf{Q}$ maps the
closed point of $\Spec(\mathbf{Q})$ to the generic point
of $\Spec(\mathbf{Z})$.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-infinite-localize-not-preserve-closed-points}
Voici un exemple simple qui montre que le
lemme \ref{lemma-Jacobson-invert-element}
est faux si $R$ est de Jacobson mais que nous localisons par une infinité
d'éléments.
En effet, soit $R = \mathbf{Z}$ et considérons la localisation
$(R \setminus \{0\})^{-1}R \cong \mathbf{Q}$
de $R$ par l'ensemble de tous les éléments non nuls.
Manifestement, le morphisme $\mathbf{Z} \to \mathbf{Q}$ envoie le
point fermé de $\Spec(\mathbf{Q})$ sur le point générique
de $\Spec(\mathbf{Z})$.
\end{example}
```

</details>

### 18 — lemma-Jacobson-mod-ideal

Anglais L7021–7032 ; français L7001–7012.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7021) · FR-ALGEBRA-B10-CHOICE-0018.

L'idéal du quotient est quelconque, sans hypothèse de génération finie. Les maximaux et les radicaux du quotient correspondent à ceux de l'anneau contenant cet idéal. Le choix quotient et le sens de contenant sont comparés avec la définition, pas seulement reconnus par un glossaire.

Règles : FR-ALGEBRA-B10-RULE-JACOBSON, FR-ALGEBRA-B10-RULE-RADICAL.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Jacobson-mod-ideal}
Let $R$ be a Jacobson ring. Let $I \subset R$ be an ideal.
The ring $R/I$ is Jacobson and maximal ideals
of $R/I$ correspond to maximal ideals of $R$ containing $I$.
\end{lemma}

\begin{proof}
The proof is the same as the proof of
Lemma \ref{lemma-Jacobson-invert-element}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-Jacobson-mod-ideal}
Soit $R$ un anneau de Jacobson. Soit $I \subset R$ un idéal.
L'anneau $R/I$ est de Jacobson, et les idéaux maximaux
de $R/I$ correspondent aux idéaux maximaux de $R$ qui contiennent $I$.
\end{lemma}

\begin{proof}
La démonstration est la même que celle du
lemme \ref{lemma-Jacobson-invert-element}.
\end{proof}
```

</details>

### 19 — lemma-silly-jacobson

Anglais L7033–7049 ; français L7013–7029.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7033) · FR-ALGEBRA-B10-CHOICE-0019.

L'inclusion R dans le corps K impose l'intégrité de R ; R est de Jacobson, sans hypothèse noethérienne supplémentaire. Type fini porte sur K comme algèbre sur R, tandis que finie dans la conclusion concerne le degré d'une extension de corps. La réduction à un ouvert principal et sa maximalité utilisent exactement les lemmes cités.

Règles : FR-ALGEBRA-B10-RULE-JACOBSON, FR-ALGEBRA-B10-RULE-RADICAL, FR-ALGEBRA-B10-RULE-FINITE, FR-ALGEBRA-B10-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-silly-jacobson}
Let $R$ be a Jacobson ring. Let $K$ be a field. Let $R \subset K$ and
$K$ is of finite type over $R$. Then $R$ is a field and $K/R$
is a finite field extension.
\end{lemma}

\begin{proof}
First note that $R$ is a domain.
By Lemma \ref{lemma-field-finite-type-over-domain}
we see that $R_f$ is a field and $K/R_f$ is a finite field extension
for some nonzero $f \in R$. Hence $(0)$ is a maximal ideal of $R_f$
and by
Lemma \ref{lemma-Jacobson-invert-element}
we conclude $(0)$ is a maximal ideal of $R$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-silly-jacobson}
Soit $R$ un anneau de Jacobson. Soit $K$ un corps. Supposons que $R \subset K$ et
que $K$ soit de type fini sur $R$. Alors $R$ est un corps et $K/R$
est une extension finie de corps.
\end{lemma}

\begin{proof}
Remarquons d'abord que $R$ est un anneau intègre.
D'après le lemme \ref{lemma-field-finite-type-over-domain},
nous voyons que $R_f$ est un corps et que $K/R_f$ est une extension finie de corps
pour un certain $f \in R$ non nul. Ainsi, $(0)$ est un idéal maximal de $R_f$
et, d'après le
lemme \ref{lemma-Jacobson-invert-element},
nous concluons que $(0)$ est un idéal maximal de $R$.
\end{proof}
```

</details>

### 20 — proposition-Jacobson-permanence

Anglais L7050–7088 ; français L7030–7068.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7050) · FR-ALGEBRA-B10-CHOICE-0020.

Le morphisme R→S de type fini n'est pas supposé injectif. R∩m′ désigne sa contraction selon la notation de la source. Les trois conclusions — Jacobson, maximalité de la contraction, extension résiduelle finie — sont conservées. Le fait que les points fermés ont des images fermées n'affirme pas que l'application spectrale soit une application fermée.

Règles : FR-ALGEBRA-B10-RULE-JACOBSON, FR-ALGEBRA-B10-RULE-RADICAL, FR-ALGEBRA-B10-RULE-FINITE, FR-ALGEBRA-B10-RULE-TOPOLOGIE, FR-ALGEBRA-B10-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{proposition}
\label{proposition-Jacobson-permanence}
Let $R$ be a Jacobson ring. Let $R \to S$ be a
ring map of finite type. Then
\begin{enumerate}
\item The ring $S$ is Jacobson.
\item The map $\Spec(S) \to \Spec(R)$ transforms
closed points to closed points.
\item For $\mathfrak m' \subset S$ maximal lying over $\mathfrak m \subset R$
the field extension $\kappa(\mathfrak m')/\kappa(\mathfrak m)$
is finite.
\end{enumerate}
\end{proposition}

\begin{proof}
Let $\mathfrak m' \subset S$ be a maximal ideal and
$R \cap \mathfrak m' = \mathfrak m$.
Then $R/\mathfrak m \to S/\mathfrak m'$ satisfies
the conditions of Lemma \ref{lemma-silly-jacobson}
by Lemma \ref{lemma-Jacobson-mod-ideal}.
Hence $R/\mathfrak m$ is a field and
$\mathfrak m$ a maximal ideal and the induced
residue field extension is finite. This proves (2) and (3).  

\medskip\noindent
If $S$ is not Jacobson, then by Lemma \ref{lemma-characterize-jacobson} there
exists a non-maximal prime ideal $\mathfrak q$ of $S$ and an
$g \in S$, $g \not\in \mathfrak q$ such that $(S/\mathfrak q)_g$ is a field.
To arrive at a contradiction we show that $\mathfrak q$ is a maximal ideal.
Let $\mathfrak p = \mathfrak q \cap R$. Then
$R/\mathfrak p \to (S/\mathfrak q)_g$ satisfies the conditions of
Lemma \ref{lemma-silly-jacobson} by
Lemma \ref{lemma-Jacobson-mod-ideal}.
Hence $R/\mathfrak p$ is a field and the field extension
$\kappa(\mathfrak p) \to (S/\mathfrak q)_g = \kappa(\mathfrak q)$ is
finite, thus algebraic. Then $\mathfrak q$ is a maximal ideal of $S$ by
Lemma \ref{lemma-finite-residue-extension-closed}. Contradiction.
\end{proof}
```

Français restauré :
```tex
\begin{proposition}
\label{proposition-Jacobson-permanence}
Soit $R$ un anneau de Jacobson. Soit $R \to S$ un
morphisme d'anneaux de type fini. Alors :
\begin{enumerate}
\item L'anneau $S$ est de Jacobson.
\item Le morphisme $\Spec(S) \to \Spec(R)$ envoie
les points fermés sur des points fermés.
\item Pour $\mathfrak m' \subset S$ maximal au-dessus de $\mathfrak m \subset R$,
l'extension de corps $\kappa(\mathfrak m')/\kappa(\mathfrak m)$
est finie.
\end{enumerate}
\end{proposition}

\begin{proof}
Soit $\mathfrak m' \subset S$ un idéal maximal, et
$R \cap \mathfrak m' = \mathfrak m$.
Alors $R/\mathfrak m \to S/\mathfrak m'$ satisfait
les conditions du lemme \ref{lemma-silly-jacobson}
d'après le lemme \ref{lemma-Jacobson-mod-ideal}.
Ainsi, $R/\mathfrak m$ est un corps,
$\mathfrak m$ est un idéal maximal et l'extension induite
des corps résiduels est finie. Cela démontre (2) et (3).  

\medskip\noindent
Si $S$ n'est pas de Jacobson, alors, d'après le lemme \ref{lemma-characterize-jacobson}, il
existe un idéal premier non maximal $\mathfrak q$ de $S$ et un
$g \in S$, $g \not\in \mathfrak q$, tels que $(S/\mathfrak q)_g$ soit un corps.
Pour obtenir une contradiction, nous montrons que $\mathfrak q$ est un idéal maximal.
Soit $\mathfrak p = \mathfrak q \cap R$. Alors
$R/\mathfrak p \to (S/\mathfrak q)_g$ satisfait les conditions du
lemme \ref{lemma-silly-jacobson} d'après le
lemme \ref{lemma-Jacobson-mod-ideal}.
Ainsi, $R/\mathfrak p$ est un corps et l'extension de corps
$\kappa(\mathfrak p) \to (S/\mathfrak q)_g = \kappa(\mathfrak q)$ est
finie, donc algébrique. Alors $\mathfrak q$ est un idéal maximal de $S$ d'après le
lemme \ref{lemma-finite-residue-extension-closed}. Contradiction.
\end{proof}
```

</details>

### 21 — lemma-corollary-jacobson

Anglais L7089–7098 ; français L7069–7078.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7089) · FR-ALGEBRA-B10-CHOICE-0021.

La conclusion porte sur toute algèbre de type fini sur Z. Les deux références combinent exactement le caractère Jacobson de Z et la permanence par morphisme de type fini. Aucune génération finie comme groupe abélien ni aucune dimension finie n'est affirmée.

Règles : FR-ALGEBRA-B10-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-corollary-jacobson}
Any finite type algebra over $\mathbf{Z}$ is Jacobson.
\end{lemma}

\begin{proof}
Combine Lemma \ref{lemma-pid-jacobson} and
Proposition \ref{proposition-Jacobson-permanence}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-corollary-jacobson}
Toute algèbre de type fini sur $\mathbf{Z}$ est de Jacobson.
\end{lemma}

\begin{proof}
Combiner le lemme \ref{lemma-pid-jacobson} et la
proposition \ref{proposition-Jacobson-permanence}.
\end{proof}
```

</details>

### 22 — lemma-image-finite-type-map-Jacobson-rings

Anglais L7099–7188 ; français L7079–7168.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7099) · FR-ALGEBRA-B10-CHOICE-0022.

La partie constructible E et ses points fermés E0 sont lus dans les espaces indiqués. Les trois inclusions, la densité et le passage à une algèbre de présentation finie restent entiers. Un morphisme de type fini n'est pas remplacé directement par un morphisme de présentation finie : l'algèbre auxiliaire fournit ce passage. Les correspondances topologiques des parties constructibles sont vérifiées dans le chapitre Topology officiel.

Règles : FR-ALGEBRA-B10-RULE-JACOBSON, FR-ALGEBRA-B10-RULE-FINITE, FR-ALGEBRA-B10-RULE-TOPOLOGIE, FR-ALGEBRA-B10-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-image-finite-type-map-Jacobson-rings}
Let $R \to S$ be a finite type ring map of Jacobson rings.
Denote $X = \Spec(R)$ and $Y = \Spec(S)$.
Write $f : Y \to X$ the induced
map of spectra. Let $E \subset Y = \Spec(S)$ be a
constructible set. Denote with a subscript ${}_0$ the set
of closed points of a topological space.
\begin{enumerate}
\item We have $f(E)_0 = f(E_0) = X_0 \cap f(E)$.
\item A point $\xi \in X$ is in $f(E)$ if and only if
$\overline{\{\xi\}} \cap f(E_0)$ is dense in $\overline{\{\xi\}}$.
\end{enumerate}
\end{lemma}

\begin{proof}
We have a commutative diagram of continuous maps
$$
\xymatrix{
E \ar[r] \ar[d] & Y \ar[d] \\
f(E) \ar[r] & X
}
$$
Suppose $x \in f(E)$ is closed in $f(E)$. Then $f^{-1}(\{x\})\cap E$
is nonempty and closed in $E$. Applying
Topology, Lemma \ref{topology-lemma-jacobson-inherited}
to both inclusions
$$
f^{-1}(\{x\}) \cap E \subset E \subset Y
$$
we find there exists a point $y \in f^{-1}(\{x\}) \cap E$ which is
closed in $Y$. In other words, there exists $y \in Y_0$ and $y \in E_0$
mapping to $x$. Hence $x \in f(E_0)$.
This proves that $f(E)_0 \subset f(E_0)$.
Proposition \ref{proposition-Jacobson-permanence} implies that
$f(E_0) \subset X_0 \cap f(E)$. The inclusion
$X_0 \cap f(E) \subset f(E)_0$ is trivial. This proves the
first assertion.

\medskip\noindent
Suppose that $\xi \in f(E)$. According to
Lemma \ref{lemma-characterize-image-finite-type}
the set $f(E) \cap \overline{\{\xi\}}$ contains a dense
open subset of $\overline{\{\xi\}}$. Since $X$ is Jacobson
we conclude that $f(E) \cap \overline{\{\xi\}}$ contains a
dense set of closed points, see Topology,
Lemma \ref{topology-lemma-jacobson-inherited}.
We conclude by part (1) of the lemma.

\medskip\noindent
On the other hand, suppose that $\overline{\{\xi\}} \cap f(E_0)$
is dense in $\overline{\{\xi\}}$. By
Lemma \ref{lemma-constructible-is-image}
there exists a ring map $S \to S'$ of finite presentation
such that $E$ is the image of $Y' := \Spec(S') \to Y$.
Then $E_0$ is the image of $Y'_0$ by the first part of the
lemma applied to the ring map $S \to S'$. Thus we may assume that
$E = Y$ by replacing $S$ by $S'$. Suppose $\xi$ corresponds
to $\mathfrak p \subset R$. Consider the diagram
$$
\xymatrix{
S \ar[r] & S/\mathfrak p S \\
R \ar[r] \ar[u] & R/\mathfrak p \ar[u]
}
$$
This diagram and the density of $f(Y_0) \cap V(\mathfrak p)$
in $V(\mathfrak p)$
shows that the morphism $R/\mathfrak p \to S/\mathfrak p S$
satisfies condition (2) of
Lemma \ref{lemma-domain-image-dense-set-points-generic-point}.
Hence we conclude
there exists a prime $\overline{\mathfrak q} \subset S/\mathfrak pS$
mapping to $(0)$. In other words the inverse image $\mathfrak q$
of $\overline{\mathfrak q}$ in $S$ maps to $\mathfrak p$ as desired.
\end{proof}

\noindent
The conclusion of the lemma above is that we can read off
the image of $f$ from the set of closed points of the image.
This is a little nicer in case the map is of finite presentation
because then we know that images of a constructible is constructible.
Before we state it we introduce some notation.
Denote $\text{Constr}(X)$ the set of constructible sets.
Let $R \to S$ be a ring map.
Denote $X = \Spec(R)$ and $Y = \Spec(S)$.
Write $f : Y \to X$ the induced map of spectra.
Denote with a subscript ${}_0$ the set
of closed points of a topological space.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-image-finite-type-map-Jacobson-rings}
Soit $R \to S$ un morphisme de type fini entre anneaux de Jacobson.
Posons $X = \Spec(R)$ et $Y = \Spec(S)$.
Notons $f : Y \to X$ le morphisme induit
sur les spectres. Soit $E \subset Y = \Spec(S)$ un ensemble
constructible. Notons par un indice ${}_0$ l'ensemble
des points fermés d'un espace topologique.
\begin{enumerate}
\item Nous avons $f(E)_0 = f(E_0) = X_0 \cap f(E)$.
\item Un point $\xi \in X$ appartient à $f(E)$ si et seulement si
$\overline{\{\xi\}} \cap f(E_0)$ est dense dans $\overline{\{\xi\}}$.
\end{enumerate}
\end{lemma}

\begin{proof}
Nous avons un diagramme commutatif d'applications continues
$$
\xymatrix{
E \ar[r] \ar[d] & Y \ar[d] \\
f(E) \ar[r] & X
}
$$
Supposons que $x \in f(E)$ soit fermé dans $f(E)$. Alors $f^{-1}(\{x\})\cap E$
est non vide et fermé dans $E$. En appliquant le
lemme \ref{topology-lemma-jacobson-inherited} de Topologie
aux deux inclusions
$$
f^{-1}(\{x\}) \cap E \subset E \subset Y
$$
nous trouvons qu'il existe un point $y \in f^{-1}(\{x\}) \cap E$ qui est
fermé dans $Y$. Autrement dit, il existe $y \in Y_0$ et $y \in E_0$
qui s'envoie sur $x$. Ainsi, $x \in f(E_0)$.
Cela démontre que $f(E)_0 \subset f(E_0)$.
La proposition \ref{proposition-Jacobson-permanence} implique que
$f(E_0) \subset X_0 \cap f(E)$. L'inclusion
$X_0 \cap f(E) \subset f(E)_0$ est triviale. Cela démontre la
première assertion.

\medskip\noindent
Supposons que $\xi \in f(E)$. D'après le
lemme \ref{lemma-characterize-image-finite-type},
l'ensemble $f(E) \cap \overline{\{\xi\}}$ contient un ouvert
dense de $\overline{\{\xi\}}$. Puisque $X$ est de Jacobson,
nous concluons que $f(E) \cap \overline{\{\xi\}}$ contient un
ensemble dense de points fermés, voir Topologie,
lemme \ref{topology-lemma-jacobson-inherited}.
Nous concluons par la partie (1) du lemme.

\medskip\noindent
Réciproquement, supposons que $\overline{\{\xi\}} \cap f(E_0)$
soit dense dans $\overline{\{\xi\}}$. D'après le
lemme \ref{lemma-constructible-is-image},
il existe un morphisme d'anneaux $S \to S'$ de présentation finie
tel que $E$ soit l'image de $Y' := \Spec(S') \to Y$.
Alors $E_0$ est l'image de $Y'_0$ d'après la première partie du
lemme appliquée au morphisme d'anneaux $S \to S'$. Nous pouvons donc supposer que
$E = Y$ en remplaçant $S$ par $S'$. Supposons que $\xi$ corresponde
à $\mathfrak p \subset R$. Considérons le diagramme
$$
\xymatrix{
S \ar[r] & S/\mathfrak p S \\
R \ar[r] \ar[u] & R/\mathfrak p \ar[u]
}
$$
Ce diagramme et la densité de $f(Y_0) \cap V(\mathfrak p)$
dans $V(\mathfrak p)$
montrent que le morphisme $R/\mathfrak p \to S/\mathfrak p S$
satisfait la condition (2) du
lemme \ref{lemma-domain-image-dense-set-points-generic-point}.
Nous en concluons
qu'il existe un idéal premier $\overline{\mathfrak q} \subset S/\mathfrak pS$
qui s'envoie sur $(0)$. Autrement dit, l'image réciproque $\mathfrak q$
de $\overline{\mathfrak q}$ dans $S$ s'envoie sur $\mathfrak p$, comme voulu.
\end{proof}

\noindent
La conclusion du lemme ci-dessus est que nous pouvons déterminer
l'image de $f$ à partir de l'ensemble des points fermés de l'image.
C'est un peu plus commode lorsque le morphisme est de présentation finie,
car nous savons alors que l'image d'une partie constructible est constructible.
Avant de l'énoncer, introduisons quelques notations.
Notons $\text{Constr}(X)$ l'ensemble des parties constructibles.
Soit $R \to S$ un morphisme d'anneaux.
Posons $X = \Spec(R)$ et $Y = \Spec(S)$.
Notons $f : Y \to X$ le morphisme induit sur les spectres.
Notons par un indice ${}_0$ l'ensemble
des points fermés d'un espace topologique.
```

</details>

### 23 — lemma-conclude-jacobson-Noetherian

Anglais L7189–7219 ; français L7169–7199.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7189) · FR-ALGEBRA-B10-CHOICE-0023.

Les flèches horizontales du diagramme sont des bijections ; les verticales sont des images directes pour f:Y→X. La noethérianité permet ici le passage de type fini à présentation finie. La phrase de preuve inverse X et Y dans la source et dans le français : elle n'est pas réparée clandestinement. L'observation séparée donne les types exacts des flèches et la correction proposée.

Point particulier à relire : La phrase X puis Y est inversée dans l'anglais officiel. Le français fidèle la conserve ; le diagramme fournit la correction proposée séparément.

Règles : FR-ALGEBRA-B10-RULE-JACOBSON, FR-ALGEBRA-B10-RULE-FINITE, FR-ALGEBRA-B10-RULE-TOPOLOGIE, FR-ALGEBRA-B10-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-conclude-jacobson-Noetherian}
With notation as above. Assume that $R$ is a Noetherian Jacobson ring.
Further assume $R \to S$ is of finite type.
There is a commutative diagram
$$
\xymatrix{
\text{Constr}(Y) \ar[r]^{E \mapsto E_0} \ar[d]^{E \mapsto f(E)} &
\text{Constr}(Y_0) \ar[d]^{E \mapsto f(E)} \\
\text{Constr}(X) \ar[r]^{E \mapsto E_0} &
\text{Constr}(X_0)
}
$$
where the horizontal arrows are the bijections from
Topology, Lemma \ref{topology-lemma-jacobson-equivalent-constructible}.
\end{lemma}

\begin{proof}
Since $R \to S$ is of finite type, it is of finite presentation,
see Lemma \ref{lemma-Noetherian-finite-type-is-finite-presentation}.
Thus the image of a constructible set in $X$ is constructible
in $Y$ by Chevalley's theorem
(Theorem \ref{theorem-chevalley}).
Combined with
Lemma \ref{lemma-image-finite-type-map-Jacobson-rings}
the lemma follows.
\end{proof}

\noindent
To illustrate the use of Jacobson rings, we give the following two examples.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-conclude-jacobson-Noetherian}
Avec les notations ci-dessus. Supposons que $R$ soit un anneau de Jacobson noethérien.
Supposons en outre que $R \to S$ soit de type fini.
Il existe un diagramme commutatif
$$
\xymatrix{
\text{Constr}(Y) \ar[r]^{E \mapsto E_0} \ar[d]^{E \mapsto f(E)} &
\text{Constr}(Y_0) \ar[d]^{E \mapsto f(E)} \\
\text{Constr}(X) \ar[r]^{E \mapsto E_0} &
\text{Constr}(X_0)
}
$$
où les flèches horizontales sont les bijections du
lemme \ref{topology-lemma-jacobson-equivalent-constructible} de Topologie.
\end{lemma}

\begin{proof}
Puisque $R \to S$ est de type fini, il est de présentation finie,
voir le lemme \ref{lemma-Noetherian-finite-type-is-finite-presentation}.
Ainsi, l'image d'une partie constructible dans $X$ est constructible
dans $Y$ d'après le théorème de Chevalley
(théorème \ref{theorem-chevalley}).
Combiné au
lemme \ref{lemma-image-finite-type-map-Jacobson-rings},
cela démontre le lemme.
\end{proof}

\noindent
Pour illustrer l'emploi des anneaux de Jacobson, donnons les deux exemples suivants.
```

</details>

### 24 — example-product-matrices-zero

Anglais L7220–7363 ; français L7200–7343.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7220) · FR-ALGEBRA-B10-CHOICE-0024.

L'exemple conserve le corps quelconque au départ, puis précise la clôture algébrique pour l'interprétation des points fermés. L'action sur les couples de matrices utilise trois copies de GL(2), pas la conjugaison d'une seule matrice. Les trois cas de rang, l'hypothèse Y non nul dans le deuxième et l'ouvert des deux matrices non nulles sont conservés. Premier est retiré d'une phrase où la traduction avait corrigé une lacune de l'anglais ; le contre-exemple (xy) et la correction nécessaire sont donnés à part. La parenthèse excédentaire de source n'est pas changée. Les cinq équations décrivent le lieu dans l'ouvert indiqué ; det(Y)=0 reste dans la description globale ultérieure.

Point particulier à relire : Le mot premier ajouté en français réparait réellement le raisonnement : l'idéal (xy) contient xy mais ni x ni y. Il est retiré pour que cette réparation ne soit pas attribuée à la source. On conserve explicitement sa justification dans le dossier de révision.

Règles : FR-ALGEBRA-B10-RULE-RADICAL, FR-ALGEBRA-B10-RULE-TOPOLOGIE, FR-ALGEBRA-B10-RULE-MATRICES, FR-ALGEBRA-B10-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-product-matrices-zero}
Let $k$ be a field. The space $\Spec(k[x, y]/(xy))$
has two irreducible components: namely the $x$-axis and the
$y$-axis. As a generalization, let
$$
R = k[x_{11}, x_{12}, x_{21}, x_{22}, y_{11}, y_{12}, y_{21}, y_{22}]/
\mathfrak a,
$$
where $\mathfrak a$ is the ideal in
$k[x_{11}, x_{12}, x_{21}, x_{22}, y_{11}, y_{12}, y_{21}, y_{22}]$
generated by the entries of the $2 \times 2$ product matrix
$$
\left(
\begin{matrix}
x_{11} & x_{12}\\
x_{21} & x_{22}
\end{matrix}
\right)
 \left(
\begin{matrix}
y_{11} & y_{12}\\
y_{21} & y_{22}
\end{matrix}
\right).
$$
In this example we will describe $\Spec(R)$.

\medskip\noindent
To prove the statement about $\Spec(k[x, y]/(xy))$ we argue as follows.
If $\mathfrak p \subset k[x, y]$ is any ideal containing $xy$, then either
$x$ or $y$ would be contained in $\mathfrak p$. Hence the minimal such
prime ideals are just $(x)$ and $(y)$. In case $k$ is
algebraically closed, the $\text{max-Spec}$ of these components
can then be visualized as the point sets of $y$- and $x$-axis.

\medskip\noindent
For the generalization, note that we may identify the closed
points of the spectrum of
$k[x_{11}, x_{12}, x_{21}, x_{22}, y_{11}, y_{12}, y_{21}, y_{22}])$
with the space of matrices
$$
\left\{ (X, Y) \in \text{Mat}(2, k)\times \text{Mat}(2, k) \mid
X = \left(
\begin{matrix}
x_{11} & x_{12}\\
x_{21} & x_{22}
\end{matrix}
\right),
Y= \left(
\begin{matrix}
y_{11} & y_{12}\\
y_{21} & y_{22}
\end{matrix}
\right)
\right\}
$$
at least if $k$ is algebraically closed.
Now define a group action of
$\text{GL}(2, k)\times \text{GL}(2, k)\times \text{GL}(2, k)$
on the space of matrices $\{(X, Y)\}$ by
$$
(g_1, g_2, g_3) \times (X, Y) \mapsto ((g_1Xg_2^{-1}, g_2Yg_3^{-1})).
$$
Here, also observe that the algebraic set
$$
\text{GL}(2, k)\times \text{GL}(2, k)\times \text{GL}(2, k) \subset
\text{Mat}(2, k)\times \text{Mat}(2, k) \times \text{Mat}(2, k)
$$
is irreducible since it is the max spectrum of the domain
$$
k[x_{11}, x_{12}, \ldots, z_{21}, z_{22}, (x_{11}x_{22}-x_{12}x_{21})^{-1}
, (y_{11}y_{22}-y_{12}y_{21})^{-1}, (z_{11}z_{22}-z_{12}z_{21})^{-1}].
$$
Since the image of irreducible an algebraic set is still
irreducible, it suffices to classify the orbits of the set
$\{(X, Y)\in \text{Mat}(2, k)\times \text{Mat}(2, k)|XY = 0\}$ and take their
closures. From standard linear algebra, we are reduced to the
following three cases:
\begin{enumerate}
\item $\exists (g_1, g_2)$ such that $g_1Xg_2^{-1} = I_{2\times 2}$.
Then $Y$ is necessarily $0$, which as an algebraic set is
invariant under the group action. It follows that this orbit is
contained in the irreducible algebraic set defined by the prime
ideal $(y_{11}, y_{12}, y_{21}, y_{22})$. Taking the closure, we see
that $(y_{11}, y_{12}, y_{21}, y_{22})$ is actually a component.
\item $\exists (g_1, g_2)$ such that
$$
g_1Xg_2^{-1} = \left(
\begin{matrix}
1 & 0 \\
0 & 0
\end{matrix}
\right).
$$
This case occurs if and only if $X$ is a rank 1 matrix,
and furthermore, $Y$ is killed by such an $X$ if and only if
$$
x_{11}y_{11}+x_{12}y_{21} = 0; \quad x_{11}y_{12}+x_{12}y_{22} = 0;
$$
$$
x_{21}y_{11}+x_{22}y_{21} = 0; \quad x_{21}y_{12}+x_{22}y_{22} = 0.
$$
Fix a rank 1 $X$, such non zero $Y$'s satisfying the above
equations form an irreducible algebraic set for the following
reason($Y = 0$ is contained the previous case):
$0 = g_1Xg_2^{-1}g_2Y$ implies that
$$
g_2Y = \left(
\begin{matrix}
0 & 0 \\
y_{21}' & y_{22}'
\end{matrix}
\right).
$$
With a further $\text{GL}(2, k)$-action on the right by $g_3$,
$g_2Y$ can be brought into
$$
g_2Yg_3^{-1} = \left(
\begin{matrix}
0 & 0 \\
0 & 1
\end{matrix}
\right),
$$
and thus such $Y$'s form an irreducible algebraic set
isomorphic to the image of $\text{GL}(2, k)$ under this action. Finally,
notice that the ``rank 1" condition for $X$'s forms an open dense
subset of the irreducible algebraic set
$\det X = x_{11}x_{22} - x_{12}x_{21} = 0$.
It now follows that all the five equations define an irreducible component
$(x_{11}y_{11}+x_{12}y_{21}, x_{11}y_{12}+x_{12}y_{22}, x_{21}y_{11}
+x_{22}y_{21}, x_{21}y_{12}+x_{22}y_{22}, x_{11}x_{22}-x_{12}x_{21})$
in the open subset of the space of pairs of nonzero matrices.
It can be shown that the pair of equations
$\det X = 0$, $\det Y = 0$ cuts $\Spec(R)$ in an irreducible component
with the above locus an open dense subset.
\item $\exists (g_1, g_2)$ such that $g_1Xg_2^{-1} = 0$, or
equivalently, $X = 0$. Then $Y$ can be arbitrary and this component
is thus defined by $(x_{11}, x_{12}, x_{21}, x_{22})$.
\end{enumerate}
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-product-matrices-zero}
Soit $k$ un corps. L'espace $\Spec(k[x, y]/(xy))$
possède deux composantes irréductibles : l'axe des $x$ et
l'axe des $y$. Comme généralisation, soit
$$
R = k[x_{11}, x_{12}, x_{21}, x_{22}, y_{11}, y_{12}, y_{21}, y_{22}]/
\mathfrak a,
$$
où $\mathfrak a$ est l'idéal de
$k[x_{11}, x_{12}, x_{21}, x_{22}, y_{11}, y_{12}, y_{21}, y_{22}]$
engendré par les coefficients du produit des matrices $2 \times 2$
$$
\left(
\begin{matrix}
x_{11} & x_{12}\\
x_{21} & x_{22}
\end{matrix}
\right)
 \left(
\begin{matrix}
y_{11} & y_{12}\\
y_{21} & y_{22}
\end{matrix}
\right).
$$
Dans cet exemple, nous allons décrire $\Spec(R)$.

\medskip\noindent
Pour démontrer l'assertion concernant $\Spec(k[x, y]/(xy))$, raisonnons comme suit.
Si $\mathfrak p \subset k[x, y]$ est un idéal contenant $xy$, alors
soit $x$, soit $y$ appartient à $\mathfrak p$. Les idéaux premiers minimaux
ayant cette propriété sont donc simplement $(x)$ et $(y)$. Lorsque $k$ est
algébriquement clos, le $\text{max-Spec}$ de ces composantes
se visualise alors comme les ensembles de points des axes des $y$ et des $x$.

\medskip\noindent
Pour la généralisation, remarquons que nous pouvons identifier les points
fermés du spectre de
$k[x_{11}, x_{12}, x_{21}, x_{22}, y_{11}, y_{12}, y_{21}, y_{22}])$
à l'espace des matrices
$$
\left\{ (X, Y) \in \text{Mat}(2, k)\times \text{Mat}(2, k) \mid
X = \left(
\begin{matrix}
x_{11} & x_{12}\\
x_{21} & x_{22}
\end{matrix}
\right),
Y= \left(
\begin{matrix}
y_{11} & y_{12}\\
y_{21} & y_{22}
\end{matrix}
\right)
\right\}
$$
du moins si $k$ est algébriquement clos.
Définissons maintenant une action du groupe
$\text{GL}(2, k)\times \text{GL}(2, k)\times \text{GL}(2, k)$
sur l'espace des matrices $\{(X, Y)\}$ par
$$
(g_1, g_2, g_3) \times (X, Y) \mapsto ((g_1Xg_2^{-1}, g_2Yg_3^{-1})).
$$
Observons également que l'ensemble algébrique
$$
\text{GL}(2, k)\times \text{GL}(2, k)\times \text{GL}(2, k) \subset
\text{Mat}(2, k)\times \text{Mat}(2, k) \times \text{Mat}(2, k)
$$
est irréductible, puisqu'il est le spectre maximal de l'anneau intègre
$$
k[x_{11}, x_{12}, \ldots, z_{21}, z_{22}, (x_{11}x_{22}-x_{12}x_{21})^{-1}
, (y_{11}y_{22}-y_{12}y_{21})^{-1}, (z_{11}z_{22}-z_{12}z_{21})^{-1}].
$$
Puisque l'image d'un ensemble algébrique irréductible est encore
irréductible, il suffit de classifier les orbites de l'ensemble
$\{(X, Y)\in \text{Mat}(2, k)\times \text{Mat}(2, k)|XY = 0\}$ et de prendre leurs
adhérences. L'algèbre linéaire usuelle nous ramène aux
trois cas suivants :
\begin{enumerate}
\item $\exists (g_1, g_2)$ tel que $g_1Xg_2^{-1} = I_{2\times 2}$.
Alors $Y$ vaut nécessairement $0$ ; cet ensemble algébrique est
invariant sous l'action du groupe. Il s'ensuit que cette orbite est
contenue dans l'ensemble algébrique irréductible défini par l'idéal premier
$(y_{11}, y_{12}, y_{21}, y_{22})$. En prenant l'adhérence, nous voyons
que $(y_{11}, y_{12}, y_{21}, y_{22})$ est effectivement une composante.
\item $\exists (g_1, g_2)$ tel que
$$
g_1Xg_2^{-1} = \left(
\begin{matrix}
1 & 0 \\
0 & 0
\end{matrix}
\right).
$$
Ce cas se produit si et seulement si $X$ est une matrice de rang 1,
et, de plus, $Y$ est annulée par une telle matrice $X$ si et seulement si
$$
x_{11}y_{11}+x_{12}y_{21} = 0; \quad x_{11}y_{12}+x_{12}y_{22} = 0;
$$
$$
x_{21}y_{11}+x_{22}y_{21} = 0; \quad x_{21}y_{12}+x_{22}y_{22} = 0.
$$
Fixons une matrice $X$ de rang 1 ; les matrices $Y$ non nulles qui satisfont les
équations ci-dessus forment un ensemble algébrique irréductible pour la
raison suivante ($Y = 0$ relève du cas précédent) :
$0 = g_1Xg_2^{-1}g_2Y$ implique que
$$
g_2Y = \left(
\begin{matrix}
0 & 0 \\
y_{21}' & y_{22}'
\end{matrix}
\right).
$$
À l'aide d'une autre action de $\text{GL}(2, k)$ à droite par $g_3$,
$g_2Y$ peut être amenée à la forme
$$
g_2Yg_3^{-1} = \left(
\begin{matrix}
0 & 0 \\
0 & 1
\end{matrix}
\right),
$$
et ces matrices $Y$ forment donc un ensemble algébrique irréductible
isomorphe à l'image de $\text{GL}(2, k)$ sous cette action. Enfin,
remarquons que la condition « de rang 1 » sur les matrices $X$ définit un ouvert dense
de l'ensemble algébrique irréductible
$\det X = x_{11}x_{22} - x_{12}x_{21} = 0$.
Il s'ensuit maintenant que les cinq équations définissent une composante irréductible
$(x_{11}y_{11}+x_{12}y_{21}, x_{11}y_{12}+x_{12}y_{22}, x_{21}y_{11}
+x_{22}y_{21}, x_{21}y_{12}+x_{22}y_{22}, x_{11}x_{22}-x_{12}x_{21})$
dans l'ouvert de l'espace des paires de matrices non nulles.
On peut montrer que les deux équations
$\det X = 0$, $\det Y = 0$ découpent $\Spec(R)$ suivant une composante irréductible
dont le lieu ci-dessus est un ouvert dense.
\item $\exists (g_1, g_2)$ tel que $g_1Xg_2^{-1} = 0$, ou,
de manière équivalente, $X = 0$. Alors $Y$ peut être arbitraire, et cette composante
est donc définie par $(x_{11}, x_{12}, x_{21}, x_{22})$.
\end{enumerate}
\end{example}
```

</details>

### 25 — example-idempotent-matrices

Anglais L7364–7433 ; français L7344–7413.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7364) · FR-ALGEBRA-B10-CHOICE-0025.

La conjugaison classe les idempotents par le rang, avec r uns et n−r zéros dans la diagonale affichée, et non dans l'ensemble des n² coefficients. Le français garde ce contexte. Orbites, composantes et fonctions séparatrices ne sont pas remplacées par une preuve nouvelle. La trace en caractéristique positive ne distingue pas toujours les rangs ; la dernière assertion utilisant Λ³ est signalée comme ambiguë hors de l'illustration 3×3. Les fautes de langue anglaise sont rendues normalement, sans modifier les symboles.

Point particulier à relire : La dernière assertion est correcte pour l'illustration 3×3 ; prise uniformément pour n≥4, elle échoue au rang 4 en caractéristique 3. Portée à revoir, pas une correction admise. Aucune source française spécialisée sur ce calcul d'orbites n'a été consultée dans ce lot.

Règles : FR-ALGEBRA-B10-RULE-MATRICES.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-idempotent-matrices}
For another example, consider
$R = k[\{t_{ij}\}_{i, j = 1}^{n}]/\mathfrak a$, where $\mathfrak a$ is
the ideal generated by the entries of the product matrix $T^2-T$,
$T = (t_{ij})$. From linear algebra, we know that under the
$GL(n, k)$-action defined by $g, T \mapsto gTg^{-1}$, $T$ is
classified by the its rank and each $T$ is conjugate to some
$\text{diag}(1, \ldots, 1, 0, \ldots, 0)$, which has $r$ 1's and $n-r$ 0's.
Thus each orbit of such a $\text{diag}(1, \ldots, 1, 0, \ldots, 0)$ under the
group action forms an irreducible component and every idempotent
matrix is contained in one such orbit. Next we will show that any
two different orbits are necessarily disjoint. For this purpose we
only need to cook up polynomial functions that take different
values on different orbits. In characteristic 0 cases, such a
function can be taken to be
$f(t_{ij}) = trace(T) = \sum_{i = 1}^nt_{ii}$. In positive
characteristic cases, things are slightly more tricky since we
might have $trace(T) = 0$ even if $T \neq 0$. For instance, $char = 3$
$$
trace\left(
\begin{matrix}
1 & & \\
& 1 & \\
& & 1
\end{matrix}
\right) = 3 = 0
$$
Anyway, these components can be separated using other functions.
For instance, in the characteristic 3 case, $tr(\wedge^3T)$ takes
value 1 on the components corresponding to $diag(1, 1, 1)$ and 0 on
other components.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-idempotent-matrices}
Pour un autre exemple, considérons
$R = k[\{t_{ij}\}_{i, j = 1}^{n}]/\mathfrak a$, où $\mathfrak a$ est
l'idéal engendré par les coefficients de la matrice produit $T^2-T$,
$T = (t_{ij})$. L'algèbre linéaire nous apprend que, sous
l'action de $GL(n, k)$ définie par $g, T \mapsto gTg^{-1}$, $T$ est
classifiée par son rang, et chaque $T$ est conjuguée à une matrice
$\text{diag}(1, \ldots, 1, 0, \ldots, 0)$, qui possède $r$ coefficients égaux à 1 et $n-r$ coefficients égaux à 0.
Ainsi, chaque orbite d'une telle matrice $\text{diag}(1, \ldots, 1, 0, \ldots, 0)$ sous
l'action du groupe forme une composante irréductible, et toute matrice
idempotente appartient à l'une de ces orbites. Montrons maintenant que deux
orbites distinctes sont nécessairement disjointes. Pour cela, il
suffit de construire des fonctions polynomiales qui prennent des
valeurs différentes sur des orbites différentes. En caractéristique 0, une telle
fonction peut être
$f(t_{ij}) = trace(T) = \sum_{i = 1}^nt_{ii}$. En caractéristique
positive, les choses sont un peu plus délicates, car nous
pouvons avoir $trace(T) = 0$ même si $T \neq 0$. Par exemple, $char = 3$
$$
trace\left(
\begin{matrix}
1 & & \\
& 1 & \\
& & 1
\end{matrix}
\right) = 3 = 0
$$
Quoi qu'il en soit, ces composantes peuvent être séparées à l'aide d'autres fonctions.
Par exemple, en caractéristique 3, $tr(\wedge^3T)$ prend
la valeur 1 sur les composantes correspondant à $diag(1, 1, 1)$ et 0 sur
les autres composantes.
\end{example}
```

</details>

## Observations extérieures au texte traduit

### FR-ALGEBRA-B10-SOURCE-NOTE-0001

[Source L6773](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6773) — lemma-characterize-jacobson.

```tex
is impossible since each locally closed subset of $\Spec(R)$
contains at least one closed point
```

La propriété correcte concerne un sous-ensemble localement fermé non vide, comme le dit explicitement Topology L3320–3322. L'ensemble vide ne contient aucun point. Ici le sous-ensemble est le singleton {p}, donc le raisonnement particulier est valide. La généralisation verbale omet une qualification, mais le lemme n'est pas réfuté. Plus haut, l'anneau auquel on applique l'existence d'un maximal est non nul puisque son spectre T∩D(f) est non vide. Aucun ajout n'est fait dans la traduction.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

### FR-ALGEBRA-B10-SOURCE-NOTE-0002

[Source L7002](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7002) — example-localize-not-preserve-closed-points.

```tex
Clearly the map $R \to R_2$ maps the
closed point of $\Spec(\mathbf{Q})$ to the generic point
of $\Spec(R)$.
```

Un morphisme d'anneaux n'agit pas directement sur les points dans ce sens : il induit Spec(R2)→Spec(R) par contraction des idéaux premiers. L'unique idéal premier (0) de Q se contracte en (0) de Z_(2), point générique non fermé. La phrase abrège cette construction ; ce n'est ni une inversion mathématique de la conclusion ni une nouvelle correction admise.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

### FR-ALGEBRA-B10-SOURCE-NOTE-0003

[Source L7016](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7016) — example-infinite-localize-not-preserve-closed-points.

```tex
Clearly the map $\mathbf{Z} \to \mathbf{Q}$ maps the
closed point of $\Spec(\mathbf{Q})$ to the generic point
of $\Spec(\mathbf{Z})$.
```

Il faut lire l'application spectrale Spec(Q)→Spec(Z) induite par Z→Q. Le corps Q reste de Jacobson ; ce qui échoue est la conservation du caractère fermé du point image. On documente ce raccourci au second lieu exact, sans le compter comme un second théorème faux.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

### FR-ALGEBRA-B10-SOURCE-NOTE-0004

[Source L7209](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7209) — lemma-conclude-jacobson-Noetherian.

```tex
Thus the image of a constructible set in $X$ is constructible
in $Y$ by Chevalley's theorem
```

Dans ce passage f:Y→X, et la verticale du diagramme part de Constr(Y) vers Constr(X). Chevalley affirme donc ici que l'image d'une partie constructible de Y est constructible dans X. La prose imprimée inverse ces deux espaces. Le diagramme et le théorème précédent donnent les types, sans conjecture de notation. Le français conserve le texte officiel ; la proposition de correction Y puis X reste dans ce dossier.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

### FR-ALGEBRA-B10-SOURCE-NOTE-0005

[Source L7250](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7250) — example-product-matrices-zero.

```tex
If $\mathfrak p \subset k[x, y]$ is any ideal containing $xy$, then either
$x$ or $y$ would be contained in $\mathfrak p$.
```

L'idéal (xy) de k[x,y] contient xy mais ne contient ni x ni y : le degré en y de xy·h interdit l'égalité avec x pour h polynomial non nul, et symétriquement pour y. La phrase devient correcte en exigeant que p soit premier. La traduction avait déjà ajouté premier ; ce mot est maintenant retiré pour rétablir le témoignage officiel, tout en conservant cette correction argumentée séparément. Les idéaux premiers minimaux (x) et (y) sont bien ceux du quotient : la lacune affecte cette phrase de preuve, pas la conclusion de l'exemple.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

### FR-ALGEBRA-B10-SOURCE-NOTE-0006

[Source L7259](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7259) — example-product-matrices-zero.

```tex
$k[x_{11}, x_{12}, x_{21}, x_{22}, y_{11}, y_{12}, y_{21}, y_{22}])$
```

La parenthèse après le crochet de l'anneau polynomial n'a pas d'ouverture correspondante dans cette expression. Elle est présente dans les deux témoins et reste inchangée. La proposition typographique est sa suppression, distincte du défaut sur les idéaux premiers.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

### FR-ALGEBRA-B10-SOURCE-NOTE-0007

[Source L7393](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L7393) — example-idempotent-matrices.

```tex
For instance, in the characteristic 3 case, $tr(\wedge^3T)$ takes
value 1 on the components corresponding to $diag(1, 1, 1)$ and 0 on
other components.
```

Pour une matrice idempotente de rang r, la trace sur la troisième puissance extérieure vaut le coefficient binomial (r choisi 3) dans le corps. L'illustration 3×3 est correcte : r=0,1,2 donne zéro et r=3 donne un. Si la phrase vise encore la taille générale n, un idempotent de rang 4 en caractéristique 3 donne (4 choisi 3)=4=1, pas zéro. La restriction à l'illustration 3×3 est plausible mais non explicite ; on classe donc la remarque comme ambiguïté de portée, sans altérer la traduction ni prétendre admettre un nouvel erratum.

Confiance éditoriale : modérée, conditionnelle à une convention non établie ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

## Contrôles et suite

Les 468 régions mathématiques du lot sont égales sans aucune exception nouvelle. Le préfixe comporte 5 284 régions et les dix-huit exceptions linguistiques exactes déjà documentées. Ces exceptions antérieures restent nécessaires pour la comparaison cumulée ; aucun masque général des formules n’est employé.

Le lot ne contient aucun titre optionnel de théorème ou de preuve, ni appel de citation ; cette absence est vérifiée. Labels, références, contrôles TeX, environnements et items concordent. L’ensemble des régions mathématiques du fichier français demeure inchangé par rapport au lot 9. Les opérations inverses restituent exactement ce lot puis le témoin public antérieur, qui reste préservé.

Les 252 paires couvrent le préfixe sans lacune ni chevauchement ; les octets antérieurs au lot et ceux du suffixe non relu sont inchangés. La validation structurelle complète la lecture sémantique, elle ne la remplace pas.

Prochaine lecture : Extensions d’anneaux finies et entières, anglais L7434 / français L7414. Aucun nouveau PDF ni nouvelle publication, aucune certification globale du chapitre ou de l’édition.

