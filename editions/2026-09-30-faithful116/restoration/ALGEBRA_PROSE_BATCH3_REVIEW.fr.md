# Algèbre commutative : produits tensoriels, algèbres et changement de base

## Résultat et portée

Trois sections entièrement comparées : source officielle L1702–2542 et français L1693–2508. Les 30 paires ci-dessous contiennent tous les énoncés, preuves, exemples, slogans et transitions. 146 occurrences sont reliées à des règles contextualisées. La lecture cumulative atteint 14 sections et 92 paires ; le reste du chapitre et de l’édition reste inachevé.

Une réparation linguistique de modalité précise nécessairement vrai que. Aucune formule, hypothèse, preuve, référence ou assertion mathématique n’est changée. Aucun nouvel erratum mathématique n’est intégré au texte de référence ; les anomalies anglaises sont signalées à part.

Comparaison assistée par IA, sans relecture humaine ; consultation du canon rétrospective, non attribuée au traducteur initial. Les attestations manquantes et les choix délicats sont explicités pour une éventuelle revue experte, qui n’est pas une condition d’attente.

Autorité : commit `a04446e57ec1fbc252a871afcec7752fb2807b14`, `algebra.tex`, SHA-256 `FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3`.
[LaTeX actuel](staged/fr/010_algebra.prose-batch3.fr.tex) · [Prédécesseur conservé](staged/fr/010_algebra.prose-batch2.fr.tex) · [Lot précédent](ALGEBRA_PROSE_BATCH2_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH3_VALIDATION.json) · [Choix structurés](ALGEBRA_PROSE_BATCH3_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH3_OCCURRENCES.json) · [Couverture](ALGEBRA_PROSE_BATCH3_COVERAGE.json).

## Réparation linguistique

Source L2035 : exact, then it is not necessarily true that

Avant :
```tex
exacte, il n'est pas nécessaire que
```
Après :
```tex
exacte, il n'est pas nécessairement vrai que
```

La source nie que l'exactitude découle nécessairement des hypothèses. Nécessaire que peut évoquer l'absence d'une exigence ; nécessairement vrai que garde sans ambiguïté la modalité logique de not necessarily true. Ce n'est ni l'affirmation d'un échec pour tout N, ni une correction du théorème anglais.

Alternative : N'est pas forcément exacte serait également idiomatique, mais exigerait de réordonner la phrase et sa formule. Le changement local choisi conserve la structure existante.

## Canon français effectivement consulté

### Antoine Ducros, Introduction à la théorie des schémas, juillet 2021

[Source universitaire](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [PDF conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages 84–93 et 95–98 lues en entier ; surtout 2.4.1–3, 2.4.8, 2.4.12–17 et 2.5.1–6. Le début de 2.5.7 p.98 est vu, pas sa suite.

Attestations courtes : « produit tensoriel », « tenseurs purs », « exact à droite », « restriction des scalaires », « extension des scalaires ».

Atteste le registre de la construction bilinéaire universelle, de l'exactitude à droite, de la platitude et de l'adjonction par extension des scalaires.

Limites : Le cours contient ses propres coquilles, notamment un codomaine M au lieu de N en 2.4.5.1, et N/M/P dans 2.5.3 ; elles ne sont pas importées. La théorie d'une famille quelconque en 2.4.12 ne remplace pas les familles finies de Stacks. Les preuves de Stacks restent l'autorité mathématique.

SHA-256 : `8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66`.

### Algèbre 1, notes du 6 janvier 2016 hébergées sur la page ENS d’Olivier Debarre

[Source universitaire](https://www.math.ens.psl.eu/~debarre/Algebre1.pdf) · [PDF conservé](canon-consulted/fr-algebra/debarre-algebre1.pdf)

III.2.1–2.3 pp.104–105 ; III.3 pp.108–110 ; III.5 pp.117–118. Toutes les pages indiquées sont lues en entier. La preuve de 3.5 se poursuit p.111, non lue ici.

Attestations courtes : « algèbre tensorielle », « idéal bilatère », « puissance extérieure », « algèbre symétrique ».

Atteste les noms des trois algèbres et la distinction alterné/symétrique. Le quotient extérieur annule les répétitions ; le quotient symétrique identifie les permutations.

Limites : Texte sur les espaces vectoriels, non preuve externe pour tous les modules de Stacks. Le passage dual en p.108 et la coquille IA inclus A de sa note ne sont pas importés. La symétrisation en caractéristique zéro p.118 ne s'ajoute pas à la définition générale de Stacks.

SHA-256 : `E841AB625A98E2954D49DB0CF00574D1404F01B58FB8FCF0D545B74EEBAAAE77`.

## Règles contextualisées

### FR-ALGEBRA-B3-RULE-tensoriel

Contrôler produit universel, tenseur pur et somme de tenseurs sans les confondre avec le produit cartésien. Ducros 2.4.1–3 ; Algèbre 1 III.2.1.

Canon : FR-ALGEBRA-B3-CANON-DUCROS, FR-ALGEBRA-B3-CANON-ALGEBRE1.

### FR-ALGEBRA-B3-RULE-linearite

Chaque argument est traité séparément ; l'application induite est linéaire et son unicité garde la compatibilité prescrite. Ducros 2.4.2 ; Algèbre 1 III.2.1.

Canon : FR-ALGEBRA-B3-CANON-DUCROS, FR-ALGEBRA-B3-CANON-ALGEBRE1.

### FR-ALGEBRA-B3-RULE-actions

Vérifier l'anneau, le côté d'action et les compatibilités contre les formules sources. Aucun canon lexical externe exact du mot bimodule n'est prétendu consulté ici.

Canon : Comparaison directe ; attestation externe exacte non acquise.

### FR-ALGEBRA-B3-RULE-adjonction

Ducros 2.4.8 et 2.5.4 atteste l'adjonction et la commutation aux colimites. Distinguer le facteur fixé, les algèbres tensorielles et le second adjoint contrôlé directement dans Stacks.

Canon : FR-ALGEBRA-B3-CANON-DUCROS.

### FR-ALGEBRA-B3-RULE-exactitude

Ducros 2.4.14–17 distingue exactitude à droite, injectivité et platitude. Une négation de nécessité ne devient ni une obligation ni une négation universelle.

Canon : FR-ALGEBRA-B3-CANON-DUCROS.

### FR-ALGEBRA-B3-RULE-finitude

Les générateurs et relations sont transportés, comme en Ducros 2.5.5.3 ; les hypothèses précises et les preuves de finitude restent celles de Stacks, pas une citation d'un théorème externe non lu.

Canon : FR-ALGEBRA-B3-CANON-DUCROS.

### FR-ALGEBRA-B3-RULE-algebres

Algèbre 1 III.2.3, III.3 et III.5 atteste les constructions et noms. N'importer ni dimension finie, ni caractéristique zéro, ni remplacement d'alterné par la seule antisymétrie.

Canon : FR-ALGEBRA-B3-CANON-ALGEBRE1.

### FR-ALGEBRA-B3-RULE-base

Ducros 2.5.1–6 atteste restriction et extension des scalaires ; changement de base est interprété selon la définition de Stacks. Conserver les anneaux sous Hom et tensor, sans ajouter de platitude ni d'intégrité.

Canon : FR-ALGEBRA-B3-CANON-DUCROS.

## Passages parallèles complets

### 01 — section-tensor-product

Anglais L1702–1704 ; français L1693–1695.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1702) · `FR-ALGEBRA-B3-CHOICE-0001`.

Produit tensoriel correspond à la construction universelle bilinéaire qui suit, non à un produit cartésien. Ducros 2.4.1-2 atteste ce nom ; le titre et son identifiant sont conservés.

Règles : FR-ALGEBRA-B3-RULE-tensoriel.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Tensor products}
\label{section-tensor-product}
```

Français actuel :
```tex
\section{Produits tensoriels}
\label{section-tensor-product}
```

</details>

### 02 — definition-bilinear

Anglais L1705–1714 ; français L1696–1705.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1705) · `FR-ALGEBRA-B3-CHOICE-0002`.

Les deux conditions de linéarité sont séparées et quantifiées pour chaque argument fixé. Le produit cartésien reste explicitement distingué du futur module tensoriel ; aucun quotient ou objet supplémentaire n'est anticipé. Application bilinéaire est attesté chez Ducros 2.4.1-2.

Règles : FR-ALGEBRA-B3-RULE-linearite.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-bilinear}
Let $R$ be a ring, $M, N, P$ be three $R$-modules.
A mapping $f : M \times N \to P$ (where $M \times N$
is viewed only as Cartesian product of two $R$-modules) is said to be
{\it $R$-bilinear} if for each $x \in M$
the mapping $y\mapsto f(x, y)$ of $N$ into $P$ is $R$-linear, and for each
$y\in N$ the mapping $x\mapsto f(x, y)$ is also $R$-linear.
\end{definition}
```

Français actuel :
```tex
\begin{definition}
\label{definition-bilinear}
Soient $R$ un anneau et $M, N, P$ trois $R$-modules.
Une application $f : M \times N \to P$ (où $M \times N$
est considéré uniquement comme le produit cartésien de deux $R$-modules) est dite
{\it $R$-bilinéaire} si, pour tout $x \in M$,
l'application $y\mapsto f(x, y)$ de $N$ dans $P$ est $R$-linéaire et si, pour tout
$y\in N$, l'application $x\mapsto f(x, y)$ est également $R$-linéaire.
\end{definition}
```

</details>

### 03 — lemma-tensor-product

Anglais L1715–1777 ; français L1706–1768.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1715) · `FR-ALGEBRA-B3-CHOICE-0003`.

La propriété universelle conserve existence, unicité et compatibilité de l'isomorphisme. Le quotient du module libre par les quatre familles de relations, les générateurs et chaque étape de preuve sont traduits. Système générateur rend generating sets sans changer l'ensemble écrit. Les compositions mal typées de la preuve anglaise sont préservées, pas réparées au moyen de la preuve différente de Ducros 2.4.2.

Point particulier à relire : Les compositions (j∘j')∘g et (j'∘j)∘g' de la source ont leurs ordres inversés par rapport aux domaines. La traduction les conserve ; ce constat n'est pas une admission nouvelle dans un registre d'errata.

Règles : FR-ALGEBRA-B3-RULE-tensoriel, FR-ALGEBRA-B3-RULE-linearite, FR-ALGEBRA-B3-RULE-finitude.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-tensor-product}
Let $M, N$ be $R$-modules. Then there exists a pair $(T, g)$
where $T$ is an $R$-module, and
$g : M \times N \to T$ an $R$-bilinear
mapping, with the following universal property:
For any $R$-module $P$ and any $R$-bilinear mapping
$f : M \times N \to P$, there
exists a unique $R$-linear
mapping $\tilde{f} : T \to P$ such that $f = \tilde{f} \circ g$.
In other words, the following diagram commutes:
$$
\xymatrix{
M \times N \ar[rr]^f \ar[dr]_g & & P\\
& T \ar[ur]_{\tilde f}
}
$$
Moreover, if $(T, g)$ and $(T', g')$
are two pairs with this property, then there
exists a unique isomorphism
$j : T \to T'$ such that $j\circ g = g'$.
\end{lemma}

\noindent
The $R$-module $T$ which satisfies the above universal property is called
the  {\it tensor product} of $R$-modules $M$ and $N$, denoted as
$M \otimes_R N$.

\begin{proof}
We first prove the existence of such $R$-module $T$.
Let $M, N$ be $R$-modules.
Let $T$ be the quotient module
$P/Q$, where $P$ is the free $R$-module $R^{(M \times N)}$ and $Q$ is the
$R$-module generated by all elements of
the following types: ($x\in M, y\in N$)
\begin{align*}
(x + x', y) - (x, y) - (x', y), \\
(x, y + y') - (x, y) - (x, y'), \\
(ax, y) - a(x, y), \\
(x, ay) - a(x, y)
\end{align*}
Let $\pi : M \times N \to T$ denote the natural map.
This map is $R$-bilinear, as
implied by the above relations
when we check the bilinearity conditions. Denote the image
$\pi(x, y) = x \otimes
y$, then these elements generate
$T$. Now let $f : M \times N \to P$ be an $R$-bilinear map,
then we can define
$f' : T \to P$ by extending the mapping
$f'(x \otimes y) = f(x, y)$. Clearly $f = f'\circ \pi$. Moreover, $f'$ is
uniquely determined by the value on the
generating sets $\{x \otimes y : x\in M, y\in N\}$.
Suppose there is another pair $(T', g')$ satisfying the same properties.
Then there is a unique $j : T \to T'$ and
also $j' : T' \to T$ such that $g' = j\circ g$, $g = j'\circ g'$.
But then both the maps $(j\circ j') \circ g$ and $g$
satisfies the universal properties, so by uniqueness they are equal,
and hence $j'\circ j$ is identity on $T$.
Similarly $(j'\circ j) \circ g' = g'$ and $j\circ j'$ is identity on $T'$.
So $j$ is an isomorphism.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-tensor-product}
Soient $M, N$ des $R$-modules. Il existe alors une paire $(T, g)$,
où $T$ est un $R$-module et
$g : M \times N \to T$ une application $R$-bilinéaire,
qui possède la propriété universelle suivante :
pour tout $R$-module $P$ et toute application $R$-bilinéaire
$f : M \times N \to P$, il
existe une unique application $R$-linéaire
$\tilde{f} : T \to P$ telle que $f = \tilde{f} \circ g$.
Autrement dit, le diagramme suivant est commutatif :
$$
\xymatrix{
M \times N \ar[rr]^f \ar[dr]_g & & P\\
& T \ar[ur]_{\tilde f}
}
$$
De plus, si $(T, g)$ et $(T', g')$
sont deux paires possédant cette propriété, il
existe un unique isomorphisme
$j : T \to T'$ tel que $j\circ g = g'$.
\end{lemma}

\noindent
Le $R$-module $T$ qui satisfait à la propriété universelle ci-dessus est appelé
le {\it produit tensoriel} des $R$-modules $M$ et $N$, et est noté
$M \otimes_R N$.

\begin{proof}
Démontrons d'abord l'existence d'un tel $R$-module $T$.
Soient $M, N$ des $R$-modules.
Soit $T$ le module quotient
$P/Q$, où $P$ est le $R$-module libre $R^{(M \times N)}$ et où $Q$ est le
$R$-module engendré par tous les éléments
des types suivants : ($x\in M, y\in N$)
\begin{align*}
(x + x', y) - (x, y) - (x', y), \\
(x, y + y') - (x, y) - (x, y'), \\
(ax, y) - a(x, y), \\
(x, ay) - a(x, y)
\end{align*}
Notons $\pi : M \times N \to T$ l'application canonique.
Cette application est $R$-bilinéaire, comme
le montrent les relations ci-dessus
lorsque l'on vérifie les conditions de bilinéarité. Notons l'image
$\pi(x, y) = x \otimes
y$ ; ces éléments engendrent alors
$T$. Soit maintenant $f : M \times N \to P$ une application $R$-bilinéaire ;
nous pouvons définir
$f' : T \to P$ en prolongeant l'application
$f'(x \otimes y) = f(x, y)$. Il est clair que $f = f'\circ \pi$. De plus, $f'$ est
uniquement déterminée par ses valeurs sur le
système générateur $\{x \otimes y : x\in M, y\in N\}$.
Supposons qu'il existe une autre paire $(T', g')$ satisfaisant aux mêmes propriétés.
Il existe alors un unique $j : T \to T'$, ainsi
qu'un $j' : T' \to T$, tels que $g' = j\circ g$, $g = j'\circ g'$.
Mais les deux applications $(j\circ j') \circ g$ et $g$
satisfont alors aux propriétés universelles ; par unicité, elles sont donc égales,
et par conséquent $j'\circ j$ est l'identité sur $T$.
De même, $(j'\circ j) \circ g' = g'$ et $j\circ j'$ est l'identité sur $T'$.
Ainsi, $j$ est un isomorphisme.
\end{proof}
```

</details>

### 04 — lemma-flip-tensor-product

Anglais L1778–1804 ; français L1769–1795.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1778) · `FR-ALGEBRA-B3-CHOICE-0004`.

Les trois applications et les trois isomorphismes restent dans le même ordre. La notation x+y pour la somme directe est celle de l'anglais ; elle n'est pas remplacée par une paire dans la formule. La démonstration reste omise. Le paragraphe suivant conserve la généralisation à un nombre fini de modules ; multitensoriel désigne ici le même produit itéré, sans lui attribuer une notion nouvelle.

Règles : FR-ALGEBRA-B3-RULE-tensoriel, FR-ALGEBRA-B3-RULE-linearite.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-flip-tensor-product}
Let $M, N, P$ be $R$-modules, then the bilinear maps
\begin{align*}
(x, y) & \mapsto y \otimes x\\
(x + y, z) & \mapsto x \otimes z + y \otimes z\\
(r, x) & \mapsto rx
\end{align*}
induce unique isomorphisms
\begin{align*}
M \otimes_R N & \to N \otimes_R M, \\
(M\oplus N)\otimes_R P & \to (M \otimes_R P)\oplus(N \otimes_R P),  \\
R \otimes_R M & \to M
\end{align*}
\end{lemma}

\begin{proof}
Omitted.
\end{proof}

\noindent
We may generalize the tensor product of two $R$-modules to finitely many
$R$-modules, and set up a
correspondence between the multi-tensor product with multilinear mappings.
Using almost the same construction
one can prove that:
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-flip-tensor-product}
Soient $M, N, P$ des $R$-modules ; les applications bilinéaires
\begin{align*}
(x, y) & \mapsto y \otimes x\\
(x + y, z) & \mapsto x \otimes z + y \otimes z\\
(r, x) & \mapsto rx
\end{align*}
induisent des isomorphismes uniques
\begin{align*}
M \otimes_R N & \to N \otimes_R M, \\
(M\oplus N)\otimes_R P & \to (M \otimes_R P)\oplus(N \otimes_R P),  \\
R \otimes_R M & \to M
\end{align*}
\end{lemma}

\begin{proof}
Démonstration omise.
\end{proof}

\noindent
Nous pouvons généraliser le produit tensoriel de deux $R$-modules à un nombre fini de
$R$-modules et établir une
correspondance entre le produit multitensoriel et les applications multilinéaires.
Une construction presque identique
permet de démontrer le résultat suivant :
```

</details>

### 05 — lemma-multilinear

Anglais L1805–1821 ; français L1796–1812.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1805) · `FR-ALGEBRA-B3-CHOICE-0005`.

Chaque facteur apparaît une seule fois dans l'application universelle ; le morphisme induit est linéaire sur R et unique. Multilinéaire est vérifié contre la définition par linéarité dans chaque argument, illustrée par Algèbre 1, III.2.1. Le T imprimé hors math dans l'anglais reste tel quel. La preuve n'est pas complétée.

Point particulier à relire : Le T hors mode math et la formule abrégée unique à isomorphisme unique près viennent du texte officiel ; aucune assertion sur les automorphismes sans compatibilité n'est ajoutée.

Règles : FR-ALGEBRA-B3-RULE-linearite.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-multilinear}
Let $M_1, \ldots, M_r$ be $R$-modules. Then there exists a pair $(T, g)$
consisting of an $R$-module T and an $R$-multilinear mapping
$g : M_1\times \ldots \times M_r \to T$ with the universal
property: For any $R$-multilinear mapping
$f : M_1\times \ldots \times M_r \to P$ there exists a unique $R$-module
homomorphism $f' : T \to P$ such that $f'\circ g = f$.
Such a module $T$ is unique up to unique isomorphism. We denote it
$M_1\otimes_R \ldots \otimes_R M_r$ and we denote the universal
multilinear map $(m_1, \ldots, m_r) \mapsto m_1 \otimes \ldots \otimes m_r$.
\end{lemma}

\begin{proof}
Omitted.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-multilinear}
Soient $M_1, \ldots, M_r$ des $R$-modules. Il existe alors une paire $(T, g)$
constituée d'un $R$-module T et d'une application $R$-multilinéaire
$g : M_1\times \ldots \times M_r \to T$ possédant la propriété
universelle suivante : pour toute application $R$-multilinéaire
$f : M_1\times \ldots \times M_r \to P$, il existe un unique homomorphisme de $R$-modules
$f' : T \to P$ tel que $f'\circ g = f$.
Un tel module $T$ est unique à isomorphisme unique près. Nous le notons
$M_1\otimes_R \ldots \otimes_R M_r$ et nous notons l'application
multilinéaire universelle $(m_1, \ldots, m_r) \mapsto m_1 \otimes \ldots \otimes m_r$.
\end{lemma}

\begin{proof}
Démonstration omise.
\end{proof}
```

</details>

### 06 — lemma-transitive

Anglais L1822–1867 ; français L1813–1858.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1822) · `FR-ALGEBRA-B3-CHOICE-0006`.

Bien défini se rapporte à l'homomorphisme f, donc le masculin est motivé. Les applications f_z, f et h, les deux identités de composition et l'ordre des facteurs sont conservés. Considérons ensuite la flèche donnée par garde l'ellipse application de la source. Les adjectifs associative, commutative et distributive restent ceux du texte anglais ; on n'ajoute pas dans la traduction une rectification catégorique sur les isomorphismes de cohérence.

Règles : FR-ALGEBRA-B3-RULE-tensoriel, FR-ALGEBRA-B3-RULE-linearite.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-transitive}
The homomorphisms
$$
(M \otimes_R N)\otimes_R P \to
M \otimes_R N \otimes_R P \to
M \otimes_R (N \otimes_R P)
$$
such that
$f((x \otimes y)\otimes z) = x \otimes y \otimes z$
and $g(x \otimes y \otimes z) = x \otimes (y \otimes z)$,
$x\in M, y\in N, z\in P$ are well-defined and are isomorphisms.
\end{lemma}

\begin{proof}
We shall prove $f$ is well-defined and is an isomorphism, and this proof
carries analogously to $g$. Fix any
$z\in P$, then the mapping $(x, y)\mapsto x \otimes y \otimes z$,
$x\in M, y\in N$, is $R$-bilinear in $x$ and $y$,
and hence induces homomorphism $f_z : M \otimes N \to M \otimes N \otimes P$
which sends
$f_z(x \otimes y) = x \otimes y \otimes z$.
Then consider $(M \otimes N)\times P \to M \otimes N \otimes P$ given by
$(w, z)\mapsto f_z(w)$. The map is
$R$-bilinear and thus induces
$f : (M \otimes_R N)\otimes_R P \to M \otimes_R N \otimes_R P$
and $f((x \otimes y)\otimes z) = x \otimes y \otimes z$.
To construct the inverse, we note that the map
$\pi : M \times N \times P \to (M \otimes N)\otimes P$ is
$R$-trilinear.
Therefore, it induces an $R$-linear map
$h : M \otimes N \otimes P \to (M \otimes N)\otimes P$ which
agrees with the universal property. Here we see that
$h(x \otimes y \otimes z) = (x \otimes y)\otimes z$.
From the explicit expression of $f$ and $h$, $f\circ h$ and $h\circ f$ are
identity maps of $M \otimes N \otimes
P$ and $(M \otimes N)\otimes P$ respectively, hence $f$ is our desired
isomorphism.
\end{proof}

\noindent
Doing induction we see that this extends to multi-tensor products. Combined
with Lemma \ref{lemma-flip-tensor-product} we see that
the tensor product operation on the category of $R$-modules is associative,
commutative and distributive.
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-transitive}
Les homomorphismes
$$
(M \otimes_R N)\otimes_R P \to
M \otimes_R N \otimes_R P \to
M \otimes_R (N \otimes_R P)
$$
tels que
$f((x \otimes y)\otimes z) = x \otimes y \otimes z$
et $g(x \otimes y \otimes z) = x \otimes (y \otimes z)$,
$x\in M, y\in N, z\in P$, sont bien définis et sont des isomorphismes.
\end{lemma}

\begin{proof}
Nous allons montrer que $f$ est bien défini et est un isomorphisme ; la démonstration
s'applique de manière analogue à $g$. Fixons un
$z\in P$ quelconque. L'application $(x, y)\mapsto x \otimes y \otimes z$,
$x\in M, y\in N$, est alors $R$-bilinéaire en $x$ et $y$,
et induit donc un homomorphisme $f_z : M \otimes N \to M \otimes N \otimes P$
qui vérifie
$f_z(x \otimes y) = x \otimes y \otimes z$.
Considérons ensuite $(M \otimes N)\times P \to M \otimes N \otimes P$ donnée par
$(w, z)\mapsto f_z(w)$. Cette application est
$R$-bilinéaire et induit donc
$f : (M \otimes_R N)\otimes_R P \to M \otimes_R N \otimes_R P$,
avec $f((x \otimes y)\otimes z) = x \otimes y \otimes z$.
Pour construire l'inverse, remarquons que l'application
$\pi : M \times N \times P \to (M \otimes N)\otimes P$ est
$R$-trilinéaire.
Elle induit donc une application $R$-linéaire
$h : M \otimes N \otimes P \to (M \otimes N)\otimes P$ qui
s'accorde avec la propriété universelle. Nous voyons ici que
$h(x \otimes y \otimes z) = (x \otimes y)\otimes z$.
D'après les expressions explicites de $f$ et de $h$, $f\circ h$ et $h\circ f$ sont
les applications identiques de $M \otimes N \otimes
P$ et de $(M \otimes N)\otimes P$, respectivement ; ainsi, $f$ est bien
l'isomorphisme recherché.
\end{proof}

\noindent
En raisonnant par récurrence, nous voyons que cela s'étend aux produits multitensoriels. En combinant
ce résultat avec le Lemme \ref{lemma-flip-tensor-product}, nous voyons que
l'opération de produit tensoriel sur la catégorie des $R$-modules est associative,
commutative et distributive.
```

</details>

### 07 — definition-bimodule

Anglais L1868–1879 ; français L1859–1870.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1868) · `FR-ALGEBRA-B3-CHOICE-0007`.

Bimodule garde deux actions compatibles sur un groupe abélien ; écrire l'action de B à droite ne change pas son sens. Les lettres, les côtés d'action et la condition de commutation sont tous conservés. L'attestation lexicale exacte de bimodule n'a pas été recherchée dans une troisième référence ; le choix est contrôlé par la définition explicite, sans prétendre une consultation exhaustive.

Point particulier à relire : Attestation exacte du mot bimodule non acquise dans les pages consultées ; sens vérifié par les deux actions commutantes. Revue terminologique ultérieure bienvenue, sans attente.

Règles : FR-ALGEBRA-B3-RULE-actions.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-bimodule}
An abelian group $N$ is called an {\it $(A, B)$-bimodule} if it is both an
$A$-module and a $B$-module and for all $a \in A$ and $b \in B$ the
multiplication by $a$ and $b$ commute, so $b(an) = a(bn)$ for all $n \in N$.
In this situation we usually write the $B$-action on the right: so
for $b \in B$ and $n \in N$ the result of multiplying $n$ by $b$
is denoted $nb$. With this convention the compatibility above is
that $(ax)b = a(xb)$ for all $a\in A, b\in B, x\in N$.
The shorthand $_AN_B$ is used to denote an $(A, B)$-bimodule $N$.
\end{definition}
```

Français actuel :
```tex
\begin{definition}
\label{definition-bimodule}
Un groupe abélien $N$ est appelé un {\it $(A, B)$-bimodule} s'il est à la fois un
$A$-module et un $B$-module et si, pour tous $a \in A$ et $b \in B$, les
multiplications par $a$ et par $b$ commutent, de sorte que $b(an) = a(bn)$ pour tout $n \in N$.
Dans cette situation, nous écrivons habituellement l'action de $B$ à droite : ainsi,
pour $b \in B$ et $n \in N$, le résultat de la multiplication de $n$ par $b$
est noté $nb$. Avec cette convention, la compatibilité ci-dessus s'écrit
$(ax)b = a(xb)$ pour tous $a\in A, b\in B, x\in N$.
La notation abrégée $_AN_B$ désigne un $(A, B)$-bimodule $N$.
\end{definition}
```

</details>

### 08 — lemma-tensor-with-bimodule

Anglais L1880–1904 ; français L1871–1895.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1880) · `FR-ALGEBRA-B3-CHOICE-0008`.

Les anneaux sous les trois produits tensoriels restent A puis B dans l'ordre prescrit. Muni d'une structure exprime une action construite, non une hypothèse manquante imposée après coup. La preuve garde la même application simultanément A-linéaire et B-linéaire. L'article répété as both as est normalisé grammaticalement, sans changer l'assertion.

Règles : FR-ALGEBRA-B3-RULE-actions.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-tensor-with-bimodule}
For $A$-module $M$, $B$-module $P$ and $(A, B)$-bimodule $N$, the modules
$(M \otimes_A N)\otimes_B P$ and $M \otimes_A(N \otimes_B P)$ can both be
given $(A, B)$-bimodule structure,
and moreover
$$
(M \otimes_A N)\otimes_B P \cong M \otimes_A(N \otimes_B P).
$$
\end{lemma}

\begin{proof}
A priori $M \otimes_A N$ is an $A$-module, but we can give it a
$B$-module structure by letting
$$
(x \otimes y)b = x \otimes yb, \quad x\in M, y\in N, b\in B
$$
Thus $M \otimes_A N$ becomes an $(A, B)$-bimodule. Similarly for
$N \otimes_B P$, and thus for
$(M \otimes_A N)\otimes_B P$ and $M \otimes_A(N \otimes_B P)$. By
Lemma \ref{lemma-transitive}, these two
modules are isomorphic as both as $A$-module and $B$-module via the same
mapping.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-tensor-with-bimodule}
Pour un $A$-module $M$, un $B$-module $P$ et un $(A, B)$-bimodule $N$, les modules
$(M \otimes_A N)\otimes_B P$ et $M \otimes_A(N \otimes_B P)$ peuvent tous deux être
munis d'une structure de $(A, B)$-bimodule,
et de plus
$$
(M \otimes_A N)\otimes_B P \cong M \otimes_A(N \otimes_B P).
$$
\end{lemma}

\begin{proof}
A priori, $M \otimes_A N$ est un $A$-module, mais nous pouvons le munir d'une
structure de $B$-module en posant
$$
(x \otimes y)b = x \otimes yb, \quad x\in M, y\in N, b\in B
$$
Ainsi, $M \otimes_A N$ devient un $(A, B)$-bimodule. Il en va de même pour
$N \otimes_B P$, et donc pour
$(M \otimes_A N)\otimes_B P$ et $M \otimes_A(N \otimes_B P)$. D'après le
Lemme \ref{lemma-transitive}, ces deux
modules sont isomorphes à la fois comme $A$-modules et comme $B$-modules par la même
application.
\end{proof}
```

</details>

### 09 — lemma-hom-from-tensor-product

Anglais L1905–1932 ; français L1896–1923.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1905) · `FR-ALGEBRA-B3-CHOICE-0009`.

Bijection naturelle rend one-to-one correspondence, et non la seule injectivité. La formule prouve la linéarité en x ; les deux arguments de f conservent leur ordre. L'adjonction Hom-produit tensoriel est attestée chez Ducros 2.4.8, avec des lettres et un ordre d'écriture différents qui ne sont pas importés.

Règles : FR-ALGEBRA-B3-RULE-linearite, FR-ALGEBRA-B3-RULE-adjonction.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-hom-from-tensor-product}
For any three $R$-modules $M, N, P$,
$$
\Hom_R(M \otimes_R N, P) \cong \Hom_R(M, \Hom_R(N, P))
$$
\end{lemma}

\begin{proof}
An $R$-linear map $\hat{f}\in \Hom_R(M \otimes_R N, P)$ corresponds to an
$R$-bilinear map $f : M \times N \to P$. For
each $x\in M$ the mapping $y\mapsto f(x, y)$ is $R$-linear by the universal
property. Thus $f$ corresponds to a
map $\phi_f : M \to \Hom_R(N, P)$. This map is $R$-linear since
$$
\phi_f(ax + y)(z) =
f(ax + y, z) = af(x, z)+f(y, z) =
(a\phi_f(x)+\phi_f(y))(z),
$$
for all $a \in R$, $x \in M$, $y \in M$ and
$z \in N$. Conversely, any
$f \in \Hom_R(M, \Hom_R(N, P))$ defines an $R$-bilinear
map $M \times N \to P$, namely $(x, y)\mapsto f(x)(y)$.
So this is a natural one-to-one correspondence between the
two modules
$\Hom_R(M \otimes_R N, P)$ and $\Hom_R(M, \Hom_R(N, P))$.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-hom-from-tensor-product}
Pour trois $R$-modules quelconques $M, N, P$,
$$
\Hom_R(M \otimes_R N, P) \cong \Hom_R(M, \Hom_R(N, P))
$$
\end{lemma}

\begin{proof}
Une application $R$-linéaire $\hat{f}\in \Hom_R(M \otimes_R N, P)$ correspond à une
application $R$-bilinéaire $f : M \times N \to P$. Pour
tout $x\in M$, l'application $y\mapsto f(x, y)$ est $R$-linéaire par la propriété
universelle. Ainsi, $f$ correspond à une
application $\phi_f : M \to \Hom_R(N, P)$. Cette application est $R$-linéaire puisque
$$
\phi_f(ax + y)(z) =
f(ax + y, z) = af(x, z)+f(y, z) =
(a\phi_f(x)+\phi_f(y))(z),
$$
pour tous $a \in R$, $x \in M$, $y \in M$ et
$z \in N$. Réciproquement, tout
$f \in \Hom_R(M, \Hom_R(N, P))$ définit une application $R$-bilinéaire
$M \times N \to P$, à savoir $(x, y)\mapsto f(x)(y)$.
Nous obtenons donc une bijection naturelle entre les
deux modules
$\Hom_R(M \otimes_R N, P)$ et $\Hom_R(M, \Hom_R(N, P))$.
\end{proof}
```

</details>

### 10 — lemma-tensor-products-commute-with-limits

Anglais L1933–1992 ; français L1924–1983.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1933) · `FR-ALGEBRA-B3-CHOICE-0010`.

Le titre dit colimites malgré le mot limits dans l'identifiant immuable. La première preuve garde l'adjoint à gauche ; la seconde conserve coprojections, diagrammes, construction de l'inverse et les deux identités. Le système est seulement sur un préordre : la traduction n'ajoute pas de filtrance. Le raisonnement condensé pour construire l'application bilinéaire n'est pas remplacé par une preuve nouvelle. Le g en prose hors math reste une particularité typographique, non un nouvel objet.

Point particulier à relire : Le nom technique limits du label et le g typographique de prose restent inchangés. La preuve directe contient une étape condensée ; la fidélité n'en est pas une certification de détail.

Règles : FR-ALGEBRA-B3-RULE-tensoriel, FR-ALGEBRA-B3-RULE-linearite, FR-ALGEBRA-B3-RULE-adjonction.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}[Tensor products commute with colimits]
\label{lemma-tensor-products-commute-with-limits}
Let $(M_i, \mu_{ij})$ be a system over the preordered set $I$.
Let $N$ be an $R$-module. Then
$$
\colim (M_i \otimes N) \cong (\colim M_i)\otimes N.
$$
Moreover, the isomorphism is induced by the homomorphisms
$\mu_i \otimes 1: M_i \otimes N \to M \otimes N$
where $M = \colim_i M_i$ with natural maps $\mu_i : M_i \to M$.
\end{lemma}

\begin{proof}
First proof. The functor $M' \mapsto M' \otimes_R N$ is left adjoint
to the functor $N' \mapsto \Hom_R(N, N')$ by
Lemma \ref{lemma-hom-from-tensor-product}. Thus $M' \mapsto M' \otimes_R N$
commutes with all colimits, see
Categories, Lemma \ref{categories-lemma-adjoint-exact}.

\medskip\noindent
Second direct proof. Let $P = \colim (M_i \otimes N)$ with coprojections
$\lambda_i : M_i \otimes N \to P$. Let $M = \colim M_i$ with coprojections
$\mu_i : M_i \to M$. Then for all $i\leq j$, the following diagram commutes:
$$
\xymatrix{
M_i \otimes N \ar[r]_{\mu_i \otimes 1} \ar[d]_{\mu_{ij} \otimes 1} &
M \otimes N \ar[d]^{\text{id}} \\
M_j \otimes N \ar[r]^{\mu_j \otimes 1} &
M \otimes N
}
$$
By Lemma \ref{lemma-homomorphism-limit} these maps induce a unique homomorphism
$\psi : P \to M \otimes N$ such that
$\mu_i \otimes 1 = \psi \circ \lambda_i$.

\medskip\noindent
To construct the inverse map, for each $i\in I$, there is the canonical
$R$-bilinear mapping $g_i : M_i \times N \to
M_i \otimes N$. This induces a unique mapping
$\widehat{\phi} : M \times N \to P$
such that $\widehat{\phi} \circ (\mu_i \times 1) = \lambda_i \circ g_i$.
It is $R$-bilinear. Thus it induces an
$R$-linear mapping $\phi : M \otimes N \to P$.
From the commutative diagram below:
$$
\xymatrix{
M_i \times N \ar[r]^{g_i} \ar[d]^{\mu_i \times \text{id}} &
M_i \otimes N\ar[r]_{\text{id}} \ar[d]_{\lambda_i} &
M_i \otimes N \ar[d]_{\mu_i \otimes \text{id}} \ar[rd]^{\lambda_i} \\
M \times N \ar[r]^{\widehat{\phi}} &
P \ar[r]^{\psi} & M \otimes N \ar[r]^{\phi} & P
}
$$
we see that $\psi\circ\widehat{\phi} = g$, the canonical $R$-bilinear mapping
$g : M \times N \to M \otimes N$. So
$\psi\circ\phi$ is identity on $M \otimes N$. From the right-hand square and
triangle, $\phi\circ\psi$ is also
identity on $P$.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}[Les produits tensoriels commutent aux colimites]
\label{lemma-tensor-products-commute-with-limits}
Soit $(M_i, \mu_{ij})$ un système sur l'ensemble préordonné $I$.
Soit $N$ un $R$-module. Alors
$$
\colim (M_i \otimes N) \cong (\colim M_i)\otimes N.
$$
De plus, l'isomorphisme est induit par les homomorphismes
$\mu_i \otimes 1: M_i \otimes N \to M \otimes N$,
où $M = \colim_i M_i$ et où $\mu_i : M_i \to M$ sont les applications canoniques.
\end{lemma}

\begin{proof}
Première démonstration. Le foncteur $M' \mapsto M' \otimes_R N$ est adjoint à gauche
du foncteur $N' \mapsto \Hom_R(N, N')$ d'après le
Lemme \ref{lemma-hom-from-tensor-product}. Ainsi, $M' \mapsto M' \otimes_R N$
commute à toutes les colimites ; voir
Catégories, Lemme \ref{categories-lemma-adjoint-exact}.

\medskip\noindent
Seconde démonstration directe. Soit $P = \colim (M_i \otimes N)$, muni des coprojections
$\lambda_i : M_i \otimes N \to P$. Soit $M = \colim M_i$, muni des coprojections
$\mu_i : M_i \to M$. Alors, pour tous $i\leq j$, le diagramme suivant est commutatif :
$$
\xymatrix{
M_i \otimes N \ar[r]_{\mu_i \otimes 1} \ar[d]_{\mu_{ij} \otimes 1} &
M \otimes N \ar[d]^{\text{id}} \\
M_j \otimes N \ar[r]^{\mu_j \otimes 1} &
M \otimes N
}
$$
D'après le Lemme \ref{lemma-homomorphism-limit}, ces applications induisent un unique homomorphisme
$\psi : P \to M \otimes N$ tel que
$\mu_i \otimes 1 = \psi \circ \lambda_i$.

\medskip\noindent
Pour construire l'application inverse, il existe, pour tout $i\in I$, l'application canonique
$R$-bilinéaire $g_i : M_i \times N \to
M_i \otimes N$. Celle-ci induit une unique application
$\widehat{\phi} : M \times N \to P$
telle que $\widehat{\phi} \circ (\mu_i \times 1) = \lambda_i \circ g_i$.
Elle est $R$-bilinéaire et induit donc une
application $R$-linéaire $\phi : M \otimes N \to P$.
Le diagramme commutatif ci-dessous :
$$
\xymatrix{
M_i \times N \ar[r]^{g_i} \ar[d]^{\mu_i \times \text{id}} &
M_i \otimes N\ar[r]_{\text{id}} \ar[d]_{\lambda_i} &
M_i \otimes N \ar[d]_{\mu_i \otimes \text{id}} \ar[rd]^{\lambda_i} \\
M \times N \ar[r]^{\widehat{\phi}} &
P \ar[r]^{\psi} & M \otimes N \ar[r]^{\phi} & P
}
$$
montre que $\psi\circ\widehat{\phi} = g$, où g est l'application $R$-bilinéaire canonique
$g : M \times N \to M \otimes N$. Ainsi,
$\psi\circ\phi$ est l'identité de $M \otimes N$. Le carré et le
triangle de droite montrent que $\phi\circ\psi$ est également
l'identité de $P$.
\end{proof}
```

</details>

### 11 — lemma-tensor-product-exact

Anglais L1993–2030 ; français L1984–2021.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L1993) · `FR-ALGEBRA-B3-CHOICE-0011`.

Exact à droite concerne la suite terminée par zéro ; aucun zéro n'est ajouté à gauche. La double utilisation de Hom et la variance inversée sont conservées. Ducros 2.4.14-15 atteste exact à droite ; sa preuve par colimites n'est pas substituée à la preuve officielle par Hom.

Règles : FR-ALGEBRA-B3-RULE-exactitude.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-tensor-product-exact}
Let
\begin{align*}
M_1\xrightarrow{f} M_2\xrightarrow{g} M_3 \to 0
\end{align*}
be an exact sequence of $R$-modules and homomorphisms, and let $N$ be any
$R$-module. Then the sequence
\begin{equation}
\label{equation-2ndex}
M_1\otimes N\xrightarrow{f \otimes 1} M_2\otimes N \xrightarrow{g \otimes 1}
M_3\otimes N \to 0
\end{equation}
is exact. In other words, the functor $- \otimes_R N$ is
{\it right exact}, in the sense that tensoring
each term in the original right exact sequence preserves the exactness.
\end{lemma}

\begin{proof}
For every $R$-module $P$
we apply the functor $\Hom(-, \Hom(N, P))$ to the first exact
sequence. We obtain
$$
0 \to
\Hom(M_3, \Hom(N, P)) \to
\Hom(M_2, \Hom(N, P)) \to
\Hom(M_1, \Hom(N, P))
$$
which is exact by Lemma \ref{lemma-hom-exact} (1).
By Lemma \ref{lemma-hom-from-tensor-product} this becomes the sequence
$$
0 \to \Hom(M_3 \otimes N, P) \to
\Hom(M_2 \otimes N, P) \to \Hom(M_1 \otimes N, P)
$$
which is therefore also exact. Then using
Lemma \ref{lemma-hom-exact} (1) again, we arrive at the desired exact sequence.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-tensor-product-exact}
Soit
\begin{align*}
M_1\xrightarrow{f} M_2\xrightarrow{g} M_3 \to 0
\end{align*}
une suite exacte de $R$-modules et d'homomorphismes, et soit $N$ un
$R$-module quelconque. Alors la suite
\begin{equation}
\label{equation-2ndex}
M_1\otimes N\xrightarrow{f \otimes 1} M_2\otimes N \xrightarrow{g \otimes 1}
M_3\otimes N \to 0
\end{equation}
est exacte. Autrement dit, le foncteur $- \otimes_R N$ est
{\it exact à droite}, au sens où tensoriser
chaque terme de la suite exacte à droite initiale préserve l'exactitude.
\end{lemma}

\begin{proof}
Pour tout $R$-module $P$,
appliquons le foncteur $\Hom(-, \Hom(N, P))$ à la première suite
exacte. Nous obtenons
$$
0 \to
\Hom(M_3, \Hom(N, P)) \to
\Hom(M_2, \Hom(N, P)) \to
\Hom(M_1, \Hom(N, P))
$$
qui est exacte d'après le Lemme \ref{lemma-hom-exact} (1).
D'après le Lemme \ref{lemma-hom-from-tensor-product}, cette suite devient
$$
0 \to \Hom(M_3 \otimes N, P) \to
\Hom(M_2 \otimes N, P) \to \Hom(M_1 \otimes N, P)
$$
et est donc elle aussi exacte. En appliquant de nouveau le
Lemme \ref{lemma-hom-exact} (1), nous obtenons la suite exacte recherchée.
\end{proof}
```

</details>

### 12 — remark-tensor-product-not-exact

Anglais L2031–2039 ; français L2022–2030.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2031) · `FR-ALGEBRA-B3-CHOICE-0012`.

La négation porte sur la nécessité de l'exactitude pour un module N arbitraire. La réparation nécessairement vrai que lève l'ambiguïté d'une absence d'exigence, sans prétendre que tous les produits tensoriels échouent. Les capitales NE/PAS rendent l'emphase source NOT ; les trois termes et les flèches restent inchangés.

Règles : FR-ALGEBRA-B3-RULE-tensoriel, FR-ALGEBRA-B3-RULE-exactitude.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{remark}
\label{remark-tensor-product-not-exact}
However, tensor product does NOT preserve exact sequences in general.
In other words, if $M_1 \to M_2 \to M_3$ is
exact, then it is not necessarily true that
$M_1 \otimes N \to M_2 \otimes N \to M_3 \otimes N$
is exact for arbitrary $R$-module $N$.
\end{remark}
```

Français actuel :
```tex
\begin{remark}
\label{remark-tensor-product-not-exact}
Cependant, le produit tensoriel NE préserve PAS les suites exactes en général.
Autrement dit, si $M_1 \to M_2 \to M_3$ est
exacte, il n'est pas nécessairement vrai que
$M_1 \otimes N \to M_2 \otimes N \to M_3 \otimes N$
soit exacte pour un $R$-module $N$ arbitraire.
\end{remark}
```

</details>

### 13 — example-tensor-product-not-exact

Anglais L2040–2053 ; français L2031–2044.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2040) · `FR-ALGEBRA-B3-CHOICE-0013`.

L'application de départ est la multiplication par 2 sur Z, pas une application de source Z/2. Le module tensorisé est Z/2 ; le calcul donne l'application nulle sur un module non nul. Tout le contre-exemple reste présent. Ducros 2.4.16 donne le même mécanisme avec l'ordre des facteurs inversé ; aucun échange n'est fait dans le témoin officiel.

Règles : FR-ALGEBRA-B3-RULE-exactitude.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-tensor-product-not-exact}
Consider the injective map $2 : \mathbf{Z}\to \mathbf{Z}$
viewed as a map of $\mathbf{Z}$-modules.
Let $N = \mathbf{Z}/2$. Then the induced map
$\mathbf{Z} \otimes \mathbf{Z}/2 \to \mathbf{Z} \otimes \mathbf{Z}/2$
is NOT injective. This is because for
$x \otimes y\in \mathbf{Z} \otimes \mathbf{Z}/2$,
$$
(2 \otimes 1)(x \otimes y) = 2x \otimes y = x \otimes 2y = x \otimes 0 = 0
$$
Therefore the induced map is the zero map while $\mathbf{Z} \otimes N\neq 0$.
\end{example}
```

Français actuel :
```tex
\begin{example}
\label{example-tensor-product-not-exact}
Considérons l'application injective $2 : \mathbf{Z}\to \mathbf{Z}$
comme une application de $\mathbf{Z}$-modules.
Soit $N = \mathbf{Z}/2$. L'application induite
$\mathbf{Z} \otimes \mathbf{Z}/2 \to \mathbf{Z} \otimes \mathbf{Z}/2$
n'est PAS injective. En effet, pour
$x \otimes y\in \mathbf{Z} \otimes \mathbf{Z}/2$,
$$
(2 \otimes 1)(x \otimes y) = 2x \otimes y = x \otimes 2y = x \otimes 0 = 0
$$
L'application induite est donc l'application nulle, tandis que $\mathbf{Z} \otimes N\neq 0$.
\end{example}
```

</details>

### 14 — remark-flat-module

Anglais L2054–2062 ; français L2045–2053.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2054) · `FR-ALGEBRA-B3-CHOICE-0014`.

Plat est la propriété du module N pour laquelle la tensorisation préserve les suites exactes, non une propriété de dimension ou de rang. La définition et le renvoi ultérieur restent inchangés. Ducros 2.4.17 atteste le terme, mais sa formulation par préservation des injections ne remplace pas le texte anglais.

Règles : FR-ALGEBRA-B3-RULE-exactitude.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{remark}
\label{remark-flat-module}
For $R$-modules $N$, if the
functor $-\otimes_R N$ is exact, i.e. tensoring
with $N$ preserves all exact
sequences, then $N$ is said to be {\it flat} $R$-module.
We will discuss this later in Section \ref{section-flat}.
\end{remark}
```

Français actuel :
```tex
\begin{remark}
\label{remark-flat-module}
Pour un $R$-module $N$, si le
foncteur $-\otimes_R N$ est exact, c'est-à-dire si la tensorisation
par $N$ préserve toutes les suites
exactes, alors $N$ est appelé un $R$-module {\it plat}.
Nous étudierons cette notion plus loin dans la section \ref{section-flat}.
\end{remark}
```

</details>

### 15 — lemma-tensor-finiteness

Anglais L2063–2086 ; français L2054–2077.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2063) · `FR-ALGEBRA-B3-CHOICE-0015`.

Finite est rendu par de type fini, jamais par cardinal fini. La présentation finie reste distincte ; le noyau K est de type fini seulement dans la seconde partie. Quotient par un module reproduit l'expression abrégée anglaise : on n'ajoute ni une injection de K tensor N, ni une autre suite exacte. Les deux renvois sont conservés.

Règles : FR-ALGEBRA-B3-RULE-exactitude, FR-ALGEBRA-B3-RULE-finitude.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-tensor-finiteness}
Let $R$ be a ring. Let $M$ and $N$ be $R$-modules.
\begin{enumerate}
\item If $N$ and $M$ are finite, then so is $M \otimes_R N$.
\item If $N$ and $M$ are finitely presented, then so is $M \otimes_R N$.
\end{enumerate}
\end{lemma}

\begin{proof}
Suppose $M$ is finite. Then choose a presentation
$0 \to K \to R^{\oplus n} \to M \to 0$. This gives an exact sequence
$K \otimes_R N \to N^{\oplus n} \to M \otimes_R N \to 0$ by
Lemma \ref{lemma-tensor-product-exact}.
We conclude that if $N$ is finite too then $M \otimes_R N$
is a quotient of a finite module, hence finite, see
Lemma \ref{lemma-extension}.
Similarly, if both $N$ and $M$ are finitely presented, then
we see that $K$ is finite and that $M \otimes_R N$
is a quotient of the finitely presented module $N^{\oplus n}$ by
a finite module, namely $K \otimes_R N$, and hence finitely presented, see
Lemma \ref{lemma-extension}.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-tensor-finiteness}
Soit $R$ un anneau. Soient $M$ et $N$ des $R$-modules.
\begin{enumerate}
\item Si $N$ et $M$ sont de type fini, alors $M \otimes_R N$ l'est aussi.
\item Si $N$ et $M$ sont de présentation finie, alors $M \otimes_R N$ l'est aussi.
\end{enumerate}
\end{lemma}

\begin{proof}
Supposons $M$ de type fini. Choisissons alors une présentation
$0 \to K \to R^{\oplus n} \to M \to 0$. Elle donne une suite exacte
$K \otimes_R N \to N^{\oplus n} \to M \otimes_R N \to 0$ d'après le
Lemme \ref{lemma-tensor-product-exact}.
Nous en concluons que, si $N$ est également de type fini, alors $M \otimes_R N$
est un quotient d'un module de type fini, donc est de type fini ; voir le
Lemme \ref{lemma-extension}.
De même, si $N$ et $M$ sont tous deux de présentation finie,
nous voyons que $K$ est de type fini et que $M \otimes_R N$
est le quotient du module de présentation finie $N^{\oplus n}$ par
un module de type fini, à savoir $K \otimes_R N$, et est donc de présentation finie ; voir le
Lemme \ref{lemma-extension}.
\end{proof}
```

</details>

### 16 — lemma-tensor-localization

Anglais L2087–2122 ; français L2078–2113.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2087) · `FR-ALGEBRA-B3-CHOICE-0016`.

L'isomorphisme est linéaire sur le localisé S inverse R, pas seulement sur R. Le passage à un dénominateur commun conserve les s, t_k et m exacts du texte. L'absence d'une définition explicite des t_k est déjà celle de la preuve source et reste signalée plutôt que comblée. Surjectif/injectif peuvent se rapporter au morphisme f ; aucune réparation automatique d'accord n'est nécessaire.

Point particulier à relire : Les dénominateurs communs t_k sont utilisés sans définition explicite dans le texte anglais. On ne complète pas la preuve sous couvert de traduction.

Règles : FR-ALGEBRA-B3-RULE-linearite, FR-ALGEBRA-B3-RULE-exactitude.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-tensor-localization}
Let $M$ be an $R$-module. Then the $S^{-1}R$-modules $S^{-1}M$
and $S^{-1}R \otimes_R M$ are canonically isomorphic, and the
canonical isomorphism $f : S^{-1}R \otimes_R M \to S^{-1}M$
is given by
$$
f((a/s) \otimes m) = am/s, \forall a \in R, m \in M, s \in S
$$
\end{lemma}

\begin{proof}
Obviously, the map
$f' : S^{-1}R \times M \to S^{-1}M$ given by $f'(a/s, m) = am/s$ is
bilinear, and thus by the
universal property, this map induces a unique $S^{-1}R$-module homomorphism
$f : S^{-1}R \otimes_R M \to S^{-1}M$ as in the statement of the lemma.
Actually every element in $S^{-1}M$ is of the form $m/s$, $m\in M, s\in S$ and
every element in
$S^{-1}R \otimes_R M$ is of the form $1/s \otimes m$. To see the latter fact,
write an element in
$S^{-1}R \otimes_R M$ as
$$
\sum_k \frac{a_k}{s_k} \otimes m_k =
\sum_k \frac{a_k t_k}{s} \otimes m_k =
\frac{1}{s} \otimes \sum_k {a_k t_k}m_k = \frac{1}{s} \otimes m
$$
Where $m = \sum_k {a_k t_k}m_k$. Then it is obvious that $f$ is surjective,
and if $f(\frac{1}{s} \otimes m) = m/s = 0$ then there exists $t \in S$ with
$tm = 0$ in $M$. Then we have
$$
\frac{1}{s} \otimes m = \frac{1}{st} \otimes tm = \frac{1}{st} \otimes 0 = 0
$$
Therefore $f$ is injective.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-tensor-localization}
Soit $M$ un $R$-module. Alors les $S^{-1}R$-modules $S^{-1}M$
et $S^{-1}R \otimes_R M$ sont canoniquement isomorphes, et
l'isomorphisme canonique $f : S^{-1}R \otimes_R M \to S^{-1}M$
est donné par
$$
f((a/s) \otimes m) = am/s, \forall a \in R, m \in M, s \in S
$$
\end{lemma}

\begin{proof}
Il est évident que l'application
$f' : S^{-1}R \times M \to S^{-1}M$ donnée par $f'(a/s, m) = am/s$ est
bilinéaire ; par la
propriété universelle, elle induit donc un unique homomorphisme de $S^{-1}R$-modules
$f : S^{-1}R \otimes_R M \to S^{-1}M$ comme dans l'énoncé du lemme.
En fait, tout élément de $S^{-1}M$ est de la forme $m/s$, $m\in M, s\in S$, et
tout élément de
$S^{-1}R \otimes_R M$ est de la forme $1/s \otimes m$. Pour voir ce dernier fait,
écrivons un élément de
$S^{-1}R \otimes_R M$ sous la forme
$$
\sum_k \frac{a_k}{s_k} \otimes m_k =
\sum_k \frac{a_k t_k}{s} \otimes m_k =
\frac{1}{s} \otimes \sum_k {a_k t_k}m_k = \frac{1}{s} \otimes m
$$
où $m = \sum_k {a_k t_k}m_k$. Il est alors évident que $f$ est surjectif,
et si $f(\frac{1}{s} \otimes m) = m/s = 0$, il existe $t \in S$ tel que
$tm = 0$ dans $M$. Nous avons alors
$$
\frac{1}{s} \otimes m = \frac{1}{st} \otimes tm = \frac{1}{st} \otimes 0 = 0
$$
Par conséquent, $f$ est injectif.
\end{proof}
```

</details>

### 17 — lemma-tensor-product-localization

Anglais L2123–2163 ; français L2114–2140.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2123) · `FR-ALGEBRA-B3-CHOICE-0017`.

L'anneau de base S inverse R dans le premier produit est essentiel et conservé. La chaîne de cinq isomorphismes garde la structure de bimodule et les deux références. L'expression des fractions et le produit st sont identiques ; aucune hypothèse d'intégrité n'est ajoutée.

Règles : FR-ALGEBRA-B3-RULE-actions.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-tensor-product-localization}
Let $M, N$ be $R$-modules, then there is a canonical
$S^{-1}R$-module isomorphism
$f : S^{-1}M \otimes_{S^{-1}R}S^{-1}N \to S^{-1}(M \otimes_R N)$,
given by
$$
f((m/s)\otimes(n/t)) = (m \otimes n)/st
$$
\end{lemma}

\begin{proof}
We may use Lemma \ref{lemma-tensor-with-bimodule}
and Lemma \ref{lemma-tensor-localization} repeatedly to
see that these two
$S^{-1}R$-modules are isomorphic, noting that $S^{-1}R$ is an
$(R, S^{-1}R)$-bimodule:
\begin{align*}
S^{-1}(M \otimes_R N) & \cong S^{-1}R \otimes_R (M \otimes_R N)\\
 & \cong S^{-1}M \otimes_R N\\
 & \cong (S^{-1}M \otimes_{S^{-1}R}S^{-1}R)\otimes_R N\\
 & \cong S^{-1}M \otimes_{S^{-1}R}(S^{-1}R \otimes_R N)\\
 & \cong S^{-1}M \otimes_{S^{-1}R}S^{-1}N
\end{align*}
This isomorphism is easily seen to be the one stated in the lemma.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-tensor-product-localization}
Soient $M, N$ des $R$-modules. Il existe alors un
isomorphisme canonique de $S^{-1}R$-modules
$f : S^{-1}M \otimes_{S^{-1}R}S^{-1}N \to S^{-1}(M \otimes_R N)$,
donné par
$$
f((m/s)\otimes(n/t)) = (m \otimes n)/st
$$
\end{lemma}

\begin{proof}
Nous pouvons utiliser à plusieurs reprises le Lemme \ref{lemma-tensor-with-bimodule}
et le Lemme \ref{lemma-tensor-localization} pour
voir que ces deux
$S^{-1}R$-modules sont isomorphes, en remarquant que $S^{-1}R$ est un
$(R, S^{-1}R)$-bimodule :
\begin{align*}
S^{-1}(M \otimes_R N) & \cong S^{-1}R \otimes_R (M \otimes_R N)\\
 & \cong S^{-1}M \otimes_R N\\
 & \cong (S^{-1}M \otimes_{S^{-1}R}S^{-1}R)\otimes_R N\\
 & \cong S^{-1}M \otimes_{S^{-1}R}(S^{-1}R \otimes_R N)\\
 & \cong S^{-1}M \otimes_{S^{-1}R}S^{-1}N
\end{align*}
On vérifie aisément que cet isomorphisme est bien celui énoncé dans le lemme.
\end{proof}
```

</details>

### 18 — section-tensor-algebra

Anglais L2164–2229 ; français L2141–2206.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2164) · `FR-ALGEBRA-B3-CHOICE-0018`.

Algèbre tensorielle, algèbre extérieure, idéal bilatère et algèbre symétrique sont attestés dans Algèbre 1, III.2.3, III.3 et III.5. Le livre y traite des espaces vectoriels ; ses hypothèses ne sont pas importées dans les modules sur R. Les tenseurs purs (Ducros 2.4.3.1), les relations x tensor x et xy-yx restent distingués. Alterné signifie nul lorsque deux arguments coïncident, même en caractéristique 2. La commutativité graduée est conservée sous la formulation abrégée de l'anglais, sans ajouter une règle de signes plus générale. Les exemples libres restent des exemples, non des hypothèses universelles.

Point particulier à relire : Le canon complémentaire porte sur des espaces vectoriels ; ne pas importer sa dimension finie ni sa symétrisation divisant par n!. La définition par x tensor x garde son sens sur un anneau quelconque, notamment en caractéristique 2.

Règles : FR-ALGEBRA-B3-RULE-tensoriel, FR-ALGEBRA-B3-RULE-linearite, FR-ALGEBRA-B3-RULE-actions, FR-ALGEBRA-B3-RULE-finitude, FR-ALGEBRA-B3-RULE-algebres.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Tensor algebra}
\label{section-tensor-algebra}

\noindent
Let $R$ be a ring. Let $M$ be an $R$-module.
We define the {\it tensor algebra of $M$ over $R$} to
be the noncommutative $R$-algebra
$$
\text{T}(M) = \text{T}_R(M) =
\bigoplus\nolimits_{n \geq 0} \text{T}^n(M)
$$
with
$\text{T}^0(M) = R$,
$\text{T}^1(M) = M$,
$\text{T}^2(M) = M \otimes_R M$,
$\text{T}^3(M) = M \otimes_R M \otimes_R M$, and so on.
Multiplication is defined by the rule that on pure tensors we have
$$
(x_1 \otimes x_2 \otimes \ldots \otimes x_n)
\cdot
(y_1 \otimes y_2 \otimes \ldots \otimes y_m)
=
x_1 \otimes x_2 \otimes \ldots \otimes x_n \otimes
y_1 \otimes y_2 \otimes \ldots \otimes y_m
$$
and we extend this by linearity.

\medskip\noindent
We define the {\it exterior algebra $\wedge(M)$ of $M$ over $R$}
to be the quotient of $\text{T}(M)$ by the two sided
ideal generated by the elements $x \otimes x \in \text{T}^2(M)$.
The image of a pure tensor $x_1 \otimes \ldots \otimes x_n$
in $\wedge^n(M)$ is denoted $x_1 \wedge \ldots \wedge x_n$.
These elements generate $\wedge^n(M)$, they are $R$-linear
in each $x_i$ and they are zero when two of the $x_i$ are equal
(i.e., they are alternating as functions of
$x_1, x_2, \ldots, x_n$). The multiplication on $\wedge(M)$ is
graded commutative, i.e., every $x \in M$ and $y \in M$
satisfy $x \wedge y = - y \wedge x$.

\medskip\noindent
An example of this is when $M = Rx_1 \oplus \ldots \oplus Rx_n$
is a finite free module. In this case $\wedge(M)$ is free over
$R$ with basis the elements
$$
x_{i_1} \wedge \ldots \wedge x_{i_r}
$$
with $0 \leq r \leq n$ and $1 \leq i_1 < i_2 < \ldots < i_r \leq n$.

\medskip\noindent
We define the {\it symmetric algebra $\text{Sym}(M)$ of $M$ over $R$}
to be the quotient of $\text{T}(M)$ by the two sided
ideal generated by the elements $x \otimes y - y \otimes x \in \text{T}^2(M)$.
The image of a pure tensor $x_1 \otimes \ldots \otimes x_n$
in $\text{Sym}^n(M)$ is denoted just $x_1 \ldots x_n$.
These elements generate $\text{Sym}^n(M)$, these are $R$-linear
in each $x_i$ and $x_1 \ldots x_n = x_1' \ldots x_n'$ if the
sequence of elements $x_1, \ldots, x_n$ is a permutation of the
sequence $x_1', \ldots, x_n'$. Thus we see that $\text{Sym}(M)$
is commutative.

\medskip\noindent
An example of this is when $M = Rx_1 \oplus \ldots \oplus Rx_n$
is a finite free module. In this case
$\text{Sym}(M) = R[x_1, \ldots, x_n]$ is a polynomial algebra.
```

Français actuel :
```tex
\section{Algèbre tensorielle}
\label{section-tensor-algebra}

\noindent
Soit $R$ un anneau. Soit $M$ un $R$-module.
Nous définissons l'{\it algèbre tensorielle de $M$ sur $R$}
comme la $R$-algèbre non commutative
$$
\text{T}(M) = \text{T}_R(M) =
\bigoplus\nolimits_{n \geq 0} \text{T}^n(M)
$$
où
$\text{T}^0(M) = R$,
$\text{T}^1(M) = M$,
$\text{T}^2(M) = M \otimes_R M$,
$\text{T}^3(M) = M \otimes_R M \otimes_R M$, et ainsi de suite.
La multiplication est définie par la règle suivante sur les tenseurs purs :
$$
(x_1 \otimes x_2 \otimes \ldots \otimes x_n)
\cdot
(y_1 \otimes y_2 \otimes \ldots \otimes y_m)
=
x_1 \otimes x_2 \otimes \ldots \otimes x_n \otimes
y_1 \otimes y_2 \otimes \ldots \otimes y_m
$$
et nous l'étendons par linéarité.

\medskip\noindent
Nous définissons l'{\it algèbre extérieure $\wedge(M)$ de $M$ sur $R$}
comme le quotient de $\text{T}(M)$ par l'idéal bilatère
engendré par les éléments $x \otimes x \in \text{T}^2(M)$.
L'image d'un tenseur pur $x_1 \otimes \ldots \otimes x_n$
dans $\wedge^n(M)$ est notée $x_1 \wedge \ldots \wedge x_n$.
Ces éléments engendrent $\wedge^n(M)$, ils dépendent $R$-linéairement
de chaque $x_i$ et ils sont nuls lorsque deux des $x_i$ sont égaux
(autrement dit, ils sont alternés en
$x_1, x_2, \ldots, x_n$). La multiplication sur $\wedge(M)$ est
commutative au sens gradué, c'est-à-dire que tous $x \in M$ et $y \in M$
vérifient $x \wedge y = - y \wedge x$.

\medskip\noindent
Considérons le cas où $M = Rx_1 \oplus \ldots \oplus Rx_n$
est un module libre de type fini. Alors $\wedge(M)$ est libre sur
$R$, de base formée des éléments
$$
x_{i_1} \wedge \ldots \wedge x_{i_r}
$$
où $0 \leq r \leq n$ et $1 \leq i_1 < i_2 < \ldots < i_r \leq n$.

\medskip\noindent
Nous définissons l'{\it algèbre symétrique $\text{Sym}(M)$ de $M$ sur $R$}
comme le quotient de $\text{T}(M)$ par l'idéal bilatère
engendré par les éléments $x \otimes y - y \otimes x \in \text{T}^2(M)$.
L'image d'un tenseur pur $x_1 \otimes \ldots \otimes x_n$
dans $\text{Sym}^n(M)$ est simplement notée $x_1 \ldots x_n$.
Ces éléments engendrent $\text{Sym}^n(M)$, ils dépendent $R$-linéairement
de chaque $x_i$, et $x_1 \ldots x_n = x_1' \ldots x_n'$ si la
suite d'éléments $x_1, \ldots, x_n$ est une permutation de la
suite $x_1', \ldots, x_n'$. Ainsi, $\text{Sym}(M)$
est commutative.

\medskip\noindent
Considérons le cas où $M = Rx_1 \oplus \ldots \oplus Rx_n$
est un module libre de type fini. Alors
$\text{Sym}(M) = R[x_1, \ldots, x_n]$ est une algèbre polynomiale.
```

</details>

### 19 — lemma-free-tensor-algebra

Anglais L2230–2239 ; français L2207–2217.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2230) · `FR-ALGEBRA-B3-CHOICE-0019`.

Chacune des puissances symétriques et extérieures d'un module libre est libre ; on ne restreint pas le lemme au rang fini. La référence au cas fini appartient seulement à l'indication de preuve. Les résultats vectoriels du canon justifient le registre, pas une réduction silencieuse du module général à un espace vectoriel.

Règles : FR-ALGEBRA-B3-RULE-finitude, FR-ALGEBRA-B3-RULE-algebres.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-free-tensor-algebra}
Let $R$ be a ring. Let $M$ be an $R$-module.
If $M$ is a free $R$-module, so is each symmetric and exterior power.
\end{lemma}

\begin{proof}
Omitted, but see above for the finite free case.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-free-tensor-algebra}
Soit $R$ un anneau. Soit $M$ un $R$-module.
Si $M$ est un $R$-module libre, chacune de ses puissances symétriques
et extérieures l'est aussi.
\end{lemma}

\begin{proof}
La démonstration est omise ; voir toutefois ci-dessus le cas libre de type fini.
\end{proof}
```

</details>

### 20 — lemma-presentation-sym-exterior

Anglais L2240–2269 ; français L2218–2247.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2240) · `FR-ALGEBRA-B3-CHOICE-0020`.

Les deux suites exactes conservent le facteur M_2 et l'exposant n-1. Elles ne commencent pas par zéro. L'absence d'une borne explicitement énoncée sur n reste celle de l'anglais ; aucune condition nouvelle n'est introduite dans la traduction. La preuve reste omise.

Point particulier à relire : Aucune borne sur n n'est imprimée ici malgré l'exposant n-1. Conserver ce point source ; il ne justifie pas de supprimer ou compléter une formule.

Règles : FR-ALGEBRA-B3-RULE-exactitude.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-presentation-sym-exterior}
Let $R$ be a ring.
Let $M_2 \to M_1 \to M \to 0$ be an exact sequence of $R$-modules.
There are exact sequences
$$
M_2 \otimes_R \text{Sym}^{n - 1}(M_1)
\to
\text{Sym}^n(M_1)
\to
\text{Sym}^n(M)
\to
0
$$
and similarly
$$
M_2 \otimes_R \wedge^{n - 1}(M_1)
\to
\wedge^n(M_1)
\to
\wedge^n(M)
\to
0
$$
\end{lemma}

\begin{proof}
Omitted.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-presentation-sym-exterior}
Soit $R$ un anneau.
Soit $M_2 \to M_1 \to M \to 0$ une suite exacte de $R$-modules.
Il existe des suites exactes
$$
M_2 \otimes_R \text{Sym}^{n - 1}(M_1)
\to
\text{Sym}^n(M_1)
\to
\text{Sym}^n(M)
\to
0
$$
et, de même,
$$
M_2 \otimes_R \wedge^{n - 1}(M_1)
\to
\wedge^n(M_1)
\to
\wedge^n(M)
\to
0
$$
\end{lemma}

\begin{proof}
La démonstration est omise.
\end{proof}
```

</details>

### 21 — lemma-present-sym-wedge

Anglais L2270–2352 ; français L2248–2330.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2270) · `FR-ALGEBRA-B3-CHOICE-0021`.

Les deux familles de relations extérieures (permutation avec signe plus et répétition) sont distinctes de la relation symétrique avec signe moins. Facteur direct désigne un sommant de la somme directe affichée, pas un produit infini. Les sous-accolades traduisent uniquement with, and, occupying slots et in the tensor ; les places j_1 et j_2 et l'ordre des x_i sont vérifiés individuellement. La borne n>=2 et l'ensemble I restent inchangés.

Règles : FR-ALGEBRA-B3-RULE-tensoriel, FR-ALGEBRA-B3-RULE-exactitude, FR-ALGEBRA-B3-RULE-finitude.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-present-sym-wedge}
Let $R$ be a ring.
Let $M$ be an $R$-module.
Let $x_i$, $i \in I$ be a given system of generators of
$M$ as an $R$-module. Let $n \geq 2$.
There exists a canonical exact sequence
$$
\bigoplus_{1 \leq j_1 < j_2 \leq n}
\bigoplus_{i_1, i_2 \in I}
\text{T}^{n - 2}(M)
\oplus
\bigoplus_{1 \leq j_1 < j_2 \leq n}
\bigoplus_{i \in I}
\text{T}^{n - 2}(M)
\to
\text{T}^n(M)
\to
\wedge^n(M)
\to
0
$$
where the pure tensor $m_1 \otimes \ldots \otimes m_{n - 2}$ in the first
summand maps to
\begin{align*}
\underbrace{
m_1 \otimes \ldots \otimes x_{i_1} \otimes \ldots
\otimes x_{i_2} \otimes \ldots \otimes m_{n - 2}
}_{\text{with } x_{i_1} \text{ and } x_{i_2}
\text{ occupying slots } j_1 \text{ and } j_2
\text{ in the tensor}} \\
+
\underbrace{
m_1 \otimes \ldots \otimes x_{i_2} \otimes \ldots
\otimes x_{i_1} \otimes \ldots \otimes m_{n - 2}
}_{\text{with } x_{i_2} \text{ and } x_{i_1}
\text{ occupying slots } j_1 \text{ and } j_2
\text{ in the tensor}}
\end{align*}
and $m_1 \otimes \ldots \otimes m_{n - 2}$ in the second
summand maps to
$$
\underbrace{
m_1 \otimes \ldots \otimes x_i \otimes \ldots
\otimes x_i \otimes \ldots \otimes m_{n - 2}
}_{\text{with } x_{i} \text{ and } x_{i}
\text{ occupying slots } j_1 \text{ and } j_2
\text{ in the tensor}}
$$
There is also a canonical exact sequence
$$
\bigoplus_{1 \leq j_1 < j_2 \leq n}
\bigoplus_{i_1, i_2 \in I}
\text{T}^{n - 2}(M)
\to
\text{T}^n(M)
\to
\text{Sym}^n(M)
\to
0
$$
where the pure tensor $m_1 \otimes \ldots \otimes m_{n - 2}$ maps to
\begin{align*}
\underbrace{
m_1 \otimes \ldots \otimes x_{i_1} \otimes \ldots
\otimes x_{i_2} \otimes \ldots \otimes m_{n - 2}
}_{\text{with } x_{i_1} \text{ and } x_{i_2}
\text{ occupying slots } j_1 \text{ and } j_2
\text{ in the tensor}} \\
-
\underbrace{
m_1 \otimes \ldots \otimes x_{i_2} \otimes \ldots
\otimes x_{i_1} \otimes \ldots \otimes m_{n - 2}
}_{\text{with } x_{i_2} \text{ and } x_{i_1}
\text{ occupying slots } j_1 \text{ and } j_2
\text{ in the tensor}}
\end{align*}
\end{lemma}

\begin{proof}
Omitted.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-present-sym-wedge}
Soit $R$ un anneau.
Soit $M$ un $R$-module.
Soit $x_i$, $i \in I$, une famille donnée de générateurs de
$M$ comme $R$-module. Soit $n \geq 2$.
Il existe une suite exacte canonique
$$
\bigoplus_{1 \leq j_1 < j_2 \leq n}
\bigoplus_{i_1, i_2 \in I}
\text{T}^{n - 2}(M)
\oplus
\bigoplus_{1 \leq j_1 < j_2 \leq n}
\bigoplus_{i \in I}
\text{T}^{n - 2}(M)
\to
\text{T}^n(M)
\to
\wedge^n(M)
\to
0
$$
où le tenseur pur $m_1 \otimes \ldots \otimes m_{n - 2}$ du premier
facteur direct est envoyé sur
\begin{align*}
\underbrace{
m_1 \otimes \ldots \otimes x_{i_1} \otimes \ldots
\otimes x_{i_2} \otimes \ldots \otimes m_{n - 2}
}_{\text{avec } x_{i_1} \text{ et } x_{i_2}
\text{ occupant les places } j_1 \text{ et } j_2
\text{ dans le tenseur}} \\
+
\underbrace{
m_1 \otimes \ldots \otimes x_{i_2} \otimes \ldots
\otimes x_{i_1} \otimes \ldots \otimes m_{n - 2}
}_{\text{avec } x_{i_2} \text{ et } x_{i_1}
\text{ occupant les places } j_1 \text{ et } j_2
\text{ dans le tenseur}}
\end{align*}
et $m_1 \otimes \ldots \otimes m_{n - 2}$ du second
facteur direct est envoyé sur
$$
\underbrace{
m_1 \otimes \ldots \otimes x_i \otimes \ldots
\otimes x_i \otimes \ldots \otimes m_{n - 2}
}_{\text{avec } x_{i} \text{ et } x_{i}
\text{ occupant les places } j_1 \text{ et } j_2
\text{ dans le tenseur}}
$$
Il existe aussi une suite exacte canonique
$$
\bigoplus_{1 \leq j_1 < j_2 \leq n}
\bigoplus_{i_1, i_2 \in I}
\text{T}^{n - 2}(M)
\to
\text{T}^n(M)
\to
\text{Sym}^n(M)
\to
0
$$
où le tenseur pur $m_1 \otimes \ldots \otimes m_{n - 2}$ est envoyé sur
\begin{align*}
\underbrace{
m_1 \otimes \ldots \otimes x_{i_1} \otimes \ldots
\otimes x_{i_2} \otimes \ldots \otimes m_{n - 2}
}_{\text{avec } x_{i_1} \text{ et } x_{i_2}
\text{ occupant les places } j_1 \text{ et } j_2
\text{ dans le tenseur}} \\
-
\underbrace{
m_1 \otimes \ldots \otimes x_{i_2} \otimes \ldots
\otimes x_{i_1} \otimes \ldots \otimes m_{n - 2}
}_{\text{avec } x_{i_2} \text{ et } x_{i_1}
\text{ occupant les places } j_1 \text{ et } j_2
\text{ dans le tenseur}}
\end{align*}
\end{lemma}

\begin{proof}
La démonstration est omise.
\end{proof}
```

</details>

### 22 — lemma-present-wedge

Anglais L2353–2369 ; français L2331–2347.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2353) · `FR-ALGEBRA-B3-CHOICE-0022`.

Les produits tensoriels sont sur A, alors que la puissance extérieure est sur B. Le noyau est engendré comme A-module par exactement les deux types d'éléments écrits. La phrase pour i différent de j n'est pas renforcée en une condition pour tous les indices ; les formules source fixent la portée. Le b appartient à B, sans hypothèse supplémentaire.

Règles : Titre et contexte directement comparés.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-present-wedge}
Let $A \to B$ be a ring map. Let $M$ be a $B$-module.
Let $n > 1$. The kernel of the $A$-linear map
$M \otimes_A \ldots \otimes_A M \to \wedge^n_B(M)$
is generated as an $A$-module by the elements
$m_1 \otimes \ldots \otimes m_n$ with $m_i = m_j$
for $i \not = j$, $m_1, \ldots, m_n \in M$ and the elements
$m_1 \otimes \ldots \otimes bm_i \otimes \ldots \otimes m_n -
m_1 \otimes \ldots \otimes bm_j \otimes \ldots \otimes m_n$
for $i \not = j$, $m_1, \ldots, m_n \in M$, and $b \in B$.
\end{lemma}

\begin{proof}
Omitted.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-present-wedge}
Soit $A \to B$ un morphisme d'anneaux. Soit $M$ un $B$-module.
Soit $n > 1$. Le noyau de l'application $A$-linéaire
$M \otimes_A \ldots \otimes_A M \to \wedge^n_B(M)$
est engendré comme $A$-module par les éléments
$m_1 \otimes \ldots \otimes m_n$ tels que $m_i = m_j$
pour $i \not = j$, avec $m_1, \ldots, m_n \in M$, et par les éléments
$m_1 \otimes \ldots \otimes bm_i \otimes \ldots \otimes m_n -
m_1 \otimes \ldots \otimes bm_j \otimes \ldots \otimes m_n$
pour $i \not = j$, $m_1, \ldots, m_n \in M$ et $b \in B$.
\end{lemma}

\begin{proof}
La démonstration est omise.
\end{proof}
```

</details>

### 23 — lemma-colimit-tensor-algebra

Anglais L2370–2384 ; français L2348–2362.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2370) · `FR-ALGEBRA-B3-CHOICE-0023`.

La formation de traduit taking sans ajout de construction. La filtrance reste explicite dans le slogan et le système de modules ; elle n'est pas omise au motif que le produit tensoriel avec un facteur fixé commute aux colimites quelconques. L'égalité écrite, les analogues symétrique/extérieur et l'indication de preuve sont conservés.

Règles : FR-ALGEBRA-B3-RULE-adjonction, FR-ALGEBRA-B3-RULE-algebres.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-colimit-tensor-algebra}
\begin{slogan}
Taking tensor algebras commutes with filtered colimits.
\end{slogan}
Let $R$ be a ring. Let $M_i$ be a directed system of
$R$-modules. Then
$\colim_i \text{T}(M_i) = \text{T}(\colim_i M_i)$
and similarly for the symmetric and exterior algebras.
\end{lemma}

\begin{proof}
Omitted. Hint: Apply Lemma \ref{lemma-tensor-products-commute-with-limits}.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-colimit-tensor-algebra}
\begin{slogan}
La formation des algèbres tensorielles commute aux colimites filtrantes.
\end{slogan}
Soit $R$ un anneau. Supposons que les $M_i$ forment un système filtrant de
$R$-modules. Alors
$\colim_i \text{T}(M_i) = \text{T}(\colim_i M_i)$,
et il en va de même pour les algèbres symétriques et extérieures.
\end{lemma}

\begin{proof}
La démonstration est omise. Indication : appliquer le lemme \ref{lemma-tensor-products-commute-with-limits}.
\end{proof}
```

</details>

### 24 — lemma-tensor-algebra-localization

Anglais L2385–2403 ; français L2363–2373.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2385) · `FR-ALGEBRA-B3-CHOICE-0024`.

Partie multiplicative et localisation gardent le même anneau et la même action sur M. Les deux analogues et l'indication avec son renvoi exact sont présents. Le T sans commande text est celui du témoin anglais ; aucune uniformisation mathématique n'est faite.

Règles : FR-ALGEBRA-B3-RULE-algebres, FR-ALGEBRA-B3-RULE-base.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-tensor-algebra-localization}
Let $R$ be a ring and let $S \subset R$ be a multiplicative subset.
Then $S^{-1}T_R(M) = T_{S^{-1}R}(S^{-1}M)$ for any $R$-module $M$.
Similar for symmetric and exterior algebras.
\end{lemma}

\begin{proof}
Omitted. Hint: Apply Lemma \ref{lemma-tensor-product-localization}.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-tensor-algebra-localization}
Soit $R$ un anneau et soit $S \subset R$ une partie multiplicative.
Alors $S^{-1}T_R(M) = T_{S^{-1}R}(S^{-1}M)$ pour tout $R$-module $M$.
Il en va de même pour les algèbres symétriques et extérieures.
\end{lemma}

\begin{proof}
La démonstration est omise. Indication : appliquer le lemme \ref{lemma-tensor-product-localization}.
\end{proof}
```

</details>

### 25 — section-base-change

Anglais L2404–2409 ; français L2374–2379.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2404) · `FR-ALGEBRA-B3-CHOICE-0025`.

Changement de base est ici l'opération algébrique définie ensuite, non le seul changement d'une base de module libre. Le paragraphe introductif ne devient pas une hypothèse supplémentaire.

Règles : FR-ALGEBRA-B3-RULE-base.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Base change}
\label{section-base-change}

\noindent
We formally introduce base change in algebra as follows.
```

Français actuel :
```tex
\section{Changement de base}
\label{section-base-change}

\noindent
Nous introduisons formellement le changement de base en algèbre comme suit.
```

</details>

### 26 — definition-base-change

Anglais L2410–2426 ; français L2380–2396.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2410) · `FR-ALGEBRA-B3-CHOICE-0026`.

Le changement de base porte d'abord sur le morphisme R vers S puis sur un S-module ; le module obtenu est sur S prime, pas seulement sur R prime. La présentation polynomiale conserve les familles I,J éventuellement infinies et le transport des coefficients. Extension des scalaires (Ducros 2.5) est une terminologie apparentée, non une raison de remplacer tous les noms changement de base du chapitre.

Règles : FR-ALGEBRA-B3-RULE-base.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-base-change}
Let $\varphi : R \to S$ be a ring map. Let $M$ be an $S$-module.
Let $R \to R'$ be any ring map. The {\it base change} of $\varphi$
by $R \to R'$ is the ring map $R' \to S \otimes_R R'$. In this situation
we often write $S' = S \otimes_R R'$.
The {\it base change} of the $S$-module $M$ is the $S'$-module
$M \otimes_R R'$.
\end{definition}

\noindent
If $S = R[x_i]/(f_j)$ for some collection of variables $x_i$, $i \in I$
and some collection of polynomials $f_j \in R[x_i]$, $j \in J$, then
$S \otimes_R R' = R'[x_i]/(f'_j)$, where $f'_j \in R'[x_i]$ is the image
of $f_j$ under the map $R[x_i] \to R'[x_i]$ induced by $R \to R'$.
This simple remark is the key to understanding base change.
```

Français actuel :
```tex
\begin{definition}
\label{definition-base-change}
Soit $\varphi : R \to S$ un morphisme d'anneaux. Soit $M$ un $S$-module.
Soit $R \to R'$ un morphisme d'anneaux quelconque. Le {\it changement de base}
de $\varphi$ par $R \to R'$ est le morphisme d'anneaux $R' \to S \otimes_R R'$.
Dans cette situation, nous écrivons souvent $S' = S \otimes_R R'$.
Le {\it changement de base} du $S$-module $M$ est le $S'$-module
$M \otimes_R R'$.
\end{definition}

\noindent
Si $S = R[x_i]/(f_j)$ pour une famille de variables $x_i$, $i \in I$,
et une famille de polynômes $f_j \in R[x_i]$, $j \in J$, alors
$S \otimes_R R' = R'[x_i]/(f'_j)$, où $f'_j \in R'[x_i]$ est l'image
de $f_j$ par le morphisme $R[x_i] \to R'[x_i]$ induit par $R \to R'$.
Cette remarque simple est la clé de la compréhension du changement de base.
```

</details>

### 27 — lemma-base-change-finiteness

Anglais L2427–2466 ; français L2397–2437.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2427) · `FR-ALGEBRA-B3-CHOICE-0027`.

Les quatre assertions gardent leurs catégories : module de type fini, module de présentation finie, algèbre de type fini et algèbre de présentation finie. Tensoriser ne demande aucune platitude ici, car les présentations sont exactes à droite. Les preuves (3) et (4) conservent la distinction entre I fini et I,J finis. Nous pouvons supposer fini signifie choisir la présentation permise par l'hypothèse, non renforcer cette hypothèse.

Règles : FR-ALGEBRA-B3-RULE-exactitude, FR-ALGEBRA-B3-RULE-finitude, FR-ALGEBRA-B3-RULE-base.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-base-change-finiteness}
Let $R \to S$ be a ring map. Let $M$ be an $S$-module.
Let $R \to R'$ be a ring map and let $S' = S \otimes_R R'$ and
$M' = M \otimes_R R'$ be the base changes.
\begin{enumerate}
\item If $M$ is a finite $S$-module, then the base change
$M'$ is a finite $S'$-module.
\item If $M$ is an $S$-module of finite presentation, then
the base change $M'$ is an $S'$-module of finite presentation.
\item If $R \to S$ is of finite type, then the base change
$R' \to S'$ is of finite type.
\item If $R \to S$ is of finite presentation, then
the base change $R' \to S'$ is of finite presentation.
\end{enumerate}
\end{lemma}

\begin{proof}
Proof of (1). Take a surjective, $S$-linear map
$S^{\oplus n} \to M \to 0$.
By Lemma \ref{lemma-flip-tensor-product} and \ref{lemma-tensor-product-exact}
the result after tensoring with $R^\prime$ is a surjection
${S^\prime}^{\oplus n} \to M^\prime \rightarrow 0$,
so $M^\prime$ is a finitely generated $S^\prime$-module.
Proof of (2). Take a presentation
$S^{\oplus m} \to S^{\oplus n} \to M \to 0$.
By Lemma \ref{lemma-flip-tensor-product} and \ref{lemma-tensor-product-exact}
the result after tensoring with $R^\prime$ gives a finite presentation
${S^\prime}^{\oplus m} \to {S^\prime}^{\oplus n} \to M^\prime \to 0$, of
the $S^\prime$-module $M^\prime$. Proof of (3). This follows by the remark
preceding the lemma as we can take $I$ to be finite by assumption.
Proof of (4). This follows by the remark preceding the lemma
as we can take $I$ and $J$ to be finite by assumption.
\end{proof}

\noindent
Let $\varphi : R \to S$ be a ring map. Given an $S$-module $N$ we
obtain an $R$-module $N_R$ by the rule $r \cdot n = \varphi(r)n$.
This is sometimes called the {\it restriction} of $N$ to $R$.
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-base-change-finiteness}
Soit $R \to S$ un morphisme d'anneaux. Soit $M$ un $S$-module.
Soit $R \to R'$ un morphisme d'anneaux, et soient
$S' = S \otimes_R R'$ et $M' = M \otimes_R R'$ les changements de base.
\begin{enumerate}
\item Si $M$ est un $S$-module de type fini, alors son changement de base
$M'$ est un $S'$-module de type fini.
\item Si $M$ est un $S$-module de présentation finie, alors son
changement de base $M'$ est un $S'$-module de présentation finie.
\item Si $R \to S$ est de type fini, alors son changement de base
$R' \to S'$ est de type fini.
\item Si $R \to S$ est de présentation finie, alors son
changement de base $R' \to S'$ est de présentation finie.
\end{enumerate}
\end{lemma}

\begin{proof}
Démonstration de (1). Choisissons une application $S$-linéaire surjective
$S^{\oplus n} \to M \to 0$.
Par les lemmes \ref{lemma-flip-tensor-product} et \ref{lemma-tensor-product-exact},
sa tensorisation par $R^\prime$ donne une surjection
${S^\prime}^{\oplus n} \to M^\prime \rightarrow 0$,
de sorte que $M^\prime$ est un $S^\prime$-module de type fini.
Démonstration de (2). Choisissons une présentation
$S^{\oplus m} \to S^{\oplus n} \to M \to 0$.
Par les lemmes \ref{lemma-flip-tensor-product} et \ref{lemma-tensor-product-exact},
sa tensorisation par $R^\prime$ donne une présentation finie
${S^\prime}^{\oplus m} \to {S^\prime}^{\oplus n} \to M^\prime \to 0$
du $S^\prime$-module $M^\prime$. Démonstration de (3). Cela résulte
de la remarque précédant le lemme, puisque nous pouvons supposer $I$ fini.
Démonstration de (4). Cela résulte de la remarque précédant le lemme,
puisque nous pouvons supposer $I$ et $J$ finis.
\end{proof}

\noindent
Soit $\varphi : R \to S$ un morphisme d'anneaux. Étant donné un $S$-module
$N$, nous obtenons un $R$-module $N_R$ par la règle
$r \cdot n = \varphi(r)n$.
On l'appelle parfois la {\it restriction des scalaires} de $N$ à $R$.
```

</details>

### 28 — lemma-adjoint-tensor-restrict

Anglais L2467–2490 ; français L2438–2462.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2467) · `FR-ALGEBRA-B3-CHOICE-0028`.

Restriction des scalaires précise le nom anglais restriction sans modifier l'action donnée juste avant. Ce syntagme est attesté par Ducros 2.5.1. Le changement de base est l'adjoint à gauche ; la formule Hom, l'action s alpha(m) et l'évaluation en m tensor 1 gardent leur direction. Les vérifications omises restent omises, et la transition vers l'adjoint à droite est conservée.

Règles : FR-ALGEBRA-B3-RULE-adjonction, FR-ALGEBRA-B3-RULE-base.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-adjoint-tensor-restrict}
Let $R \to S$ be a ring map. The functors
$\text{Mod}_S \to \text{Mod}_R$, $N \mapsto N_R$ (restriction)
and $\text{Mod}_R \to \text{Mod}_S$, $M \mapsto M \otimes_R S$
(base change) are adjoint functors. In a formula
$$
\Hom_R(M, N_R) = \Hom_S(M \otimes_R S, N)
$$
\end{lemma}

\begin{proof}
If $\alpha : M \to N_R$ is an $R$-module map, then we define
$\alpha' : M \otimes_R S \to N$ by the rule
$\alpha'(m \otimes s) = s\alpha(m)$. If $\beta : M \otimes_R S \to N$
is an $S$-module map, we define $\beta' : M \to N_R$ by the rule
$\beta'(m) = \beta(m \otimes 1)$.
We omit the verification that these constructions are mutually inverse.
\end{proof}

\noindent
The lemma above tells us that restriction has a left adjoint, namely
base change. It also has a right adjoint.
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-adjoint-tensor-restrict}
Soit $R \to S$ un morphisme d'anneaux. Les foncteurs
$\text{Mod}_S \to \text{Mod}_R$, $N \mapsto N_R$ (restriction des scalaires),
et $\text{Mod}_R \to \text{Mod}_S$, $M \mapsto M \otimes_R S$
(changement de base) sont adjoints. Plus précisément,
$$
\Hom_R(M, N_R) = \Hom_S(M \otimes_R S, N)
$$
\end{lemma}

\begin{proof}
Si $\alpha : M \to N_R$ est un morphisme de $R$-modules, nous définissons
$\alpha' : M \otimes_R S \to N$ par la règle
$\alpha'(m \otimes s) = s\alpha(m)$. Si $\beta : M \otimes_R S \to N$
est un morphisme de $S$-modules, nous définissons
$\beta' : M \to N_R$ par la règle
$\beta'(m) = \beta(m \otimes 1)$.
Nous omettons la vérification que ces constructions sont inverses l'une de l'autre.
\end{proof}

\noindent
Le lemme précédent nous dit que la restriction des scalaires admet un adjoint
à gauche, à savoir le changement de base. Elle admet aussi un adjoint à droite.
```

</details>

### 29 — lemma-adjoint-hom-restrict

Anglais L2491–2510 ; français L2463–2483.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2491) · `FR-ALGEBRA-B3-CHOICE-0029`.

L'adjoint à droite de la restriction est Hom_R(S,-), à ne pas confondre avec le changement de base. L'action sn et l'évaluation en 1 sont inchangées. Le canon de ce lot atteste le vocabulaire d'adjonction, mais aucune preuve externe particulière de ce second adjoint n'est revendiquée ; le contrôle est direct contre l'anglais.

Règles : FR-ALGEBRA-B3-RULE-adjonction, FR-ALGEBRA-B3-RULE-base.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-adjoint-hom-restrict}
Let $R \to S$ be a ring map. The functors
$\text{Mod}_S \to \text{Mod}_R$, $N \mapsto N_R$ (restriction)
and $\text{Mod}_R \to \text{Mod}_S$, $M \mapsto \Hom_R(S, M)$
are adjoint functors. In a formula
$$
\Hom_R(N_R, M) = \Hom_S(N, \Hom_R(S, M))
$$
\end{lemma}

\begin{proof}
If $\alpha : N_R \to M$ is an $R$-module map, then we define
$\alpha' : N \to \Hom_R(S, M)$ by the rule
$\alpha'(n) = (s \mapsto \alpha(sn))$. If $\beta : N \to \Hom_R(S, M)$
is an $S$-module map, we define $\beta' : N_R \to M$ by the rule
$\beta'(n) = \beta(n)(1)$.
We omit the verification that these constructions are mutually inverse.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-adjoint-hom-restrict}
Soit $R \to S$ un morphisme d'anneaux. Les foncteurs
$\text{Mod}_S \to \text{Mod}_R$, $N \mapsto N_R$ (restriction des scalaires),
et $\text{Mod}_R \to \text{Mod}_S$, $M \mapsto \Hom_R(S, M)$
sont adjoints. Plus précisément,
$$
\Hom_R(N_R, M) = \Hom_S(N, \Hom_R(S, M))
$$
\end{lemma}

\begin{proof}
Si $\alpha : N_R \to M$ est un morphisme de $R$-modules, nous définissons
$\alpha' : N \to \Hom_R(S, M)$ par la règle
$\alpha'(n) = (s \mapsto \alpha(sn))$. Si $\beta : N \to \Hom_R(S, M)$
est un morphisme de $S$-modules, nous définissons
$\beta' : N_R \to M$ par la règle
$\beta'(n) = \beta(n)(1)$.
Nous omettons la vérification que ces constructions sont inverses l'une de l'autre.
\end{proof}
```

</details>

### 30 — lemma-hom-from-tensor-product-variant

Anglais L2511–2542 ; français L2484–2508.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2511) · `FR-ALGEBRA-B3-CHOICE-0030`.

M et N sont sur S ; P est sur R. Chaque indice de Hom et de tensorisation de la chaîne est conservé. La preuve réutilise exactement les deux lemmes nommés et n'ajoute aucune hypothèse de finitude ou de platitude. Étant donnés explicite grammaticalement les trois objets déjà présents dans la source.

Règles : Titre et contexte directement comparés.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-hom-from-tensor-product-variant}
Let $R \to S$ be a ring map. Given $S$-modules $M, N$ and an $R$-module $P$
we have
$$
\Hom_R(M \otimes_S N, P) = \Hom_S(M, \Hom_R(N, P))
$$
\end{lemma}

\begin{proof}
This can be proved directly, but it is also a consequence of
Lemmas \ref{lemma-adjoint-hom-restrict} and \ref{lemma-hom-from-tensor-product}.
Namely, we have
\begin{align*}
\Hom_R(M \otimes_S N, P)
& =
\Hom_S(M \otimes_S N, \Hom_R(S, P)) \\
& =
\Hom_S(M, \Hom_S(N, \Hom_R(S, P))) \\
& =
\Hom_S(M, \Hom_R(N, P))
\end{align*}
as desired.
\end{proof}
```

Français actuel :
```tex
\begin{lemma}
\label{lemma-hom-from-tensor-product-variant}
Soit $R \to S$ un morphisme d'anneaux. Étant donnés des $S$-modules $M, N$
et un $R$-module $P$, nous avons
$$
\Hom_R(M \otimes_S N, P) = \Hom_S(M, \Hom_R(N, P))
$$
\end{lemma}

\begin{proof}
On peut le démontrer directement, mais c'est aussi une conséquence
des lemmes \ref{lemma-adjoint-hom-restrict} et \ref{lemma-hom-from-tensor-product}.
En effet, nous avons
\begin{align*}
\Hom_R(M \otimes_S N, P)
& =
\Hom_S(M \otimes_S N, \Hom_R(S, P)) \\
& =
\Hom_S(M, \Hom_S(N, \Hom_R(S, P))) \\
& =
\Hom_S(M, \Hom_R(N, P))
\end{align*}
comme voulu.
\end{proof}
```

</details>

## Contrôles exacts

Les 513 régions mathématiques du lot correspondent après trois exceptions exactes de texte sous les accolades. L’égalité brute est fausse ; les textes sont comparés, pas masqués. Les 1 687 régions du préfixe cumulatif passent avec ces trois exceptions et les cinq du lot précédent. Le fichier entier garde ses formules antérieures.

[Exceptions détaillées](ALGEBRA_PROSE_BATCH3_MATH_EXCEPTIONS.json). Labels, renvois, citations, commandes invariantes, environnements, contrôles TeX et items passent. Le préfixe déjà relu et le suffixe ultérieur sont inchangés. Le retour inverse reproduit le lot 2, puis les anciens états jusqu’à tous les octets du témoin public.

Prochaine lecture : Divers, source L2543 / français L2509. Aucun nouveau PDF, aucune publication et aucune certification de l’édition complète ne sont revendiqués.

