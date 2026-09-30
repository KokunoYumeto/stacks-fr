# Algèbre commutative : divers, Cayley-Hamilton et spectre d’un anneau

## Résultat et portée

Trois sections entièrement comparées : source L2543–3304 et français L2509–3274. Les 24 paires ci-dessous contiennent tous les énoncés, preuves, slogans et transitions, notamment les dix-sept assertions du lemme de topologie de Zariski. 168 occurrences sont reliées à des règles contextualisées. La lecture cumulative atteint 17 sections, 116 paires et 668 occurrences ; le chapitre entier et l’édition restent inachevés.

Aucun nouveau changement du français n’est nécessaire dans ce lot. Aucun fichier source de traduction n’est recopié pour fabriquer une version différente. Les anciens états et les propositions de corrections mathématiques restent séparés ; cette lecture de fidélité ne certifie pas la vérité de tous les arguments officiels.

Comparaison assistée par IA, sans relecture humaine. La consultation du canon est rétrospective et n’est pas attribuée au traducteur initial. Les variantes, limites et points délicats restent visibles pour une éventuelle relecture experte, sans attente imposée.

Autorité : commit `a04446e57ec1fbc252a871afcec7752fb2807b14`, SHA-256 `FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3`.
[LaTeX conservé](staged/fr/010_algebra.prose-batch3.fr.tex) · [Lot précédent](ALGEBRA_PROSE_BATCH3_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH4_VALIDATION.json) · [Choix structurés](ALGEBRA_PROSE_BATCH4_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH4_OCCURRENCES.json) · [Couverture](ALGEBRA_PROSE_BATCH4_COVERAGE.json).

## Canon français effectivement consulté

### Olivier Debarre, Algèbre 2, ENS, 2012–2013

[Source universitaire](https://www.math.ens.psl.eu/~debarre/Algebre2.pdf) · [PDF conservé](canon-consulted/fr-fields/debarre-algebre2.pdf)

Pages imprimées 43–46,67–69,74–75 lues en entier. II.1.1, II.3.2–3.3 avec preuves ; III.4.4 avec preuve, exercices III.4.5–4.6 ; III.5.1–5.2. La preuve de Nakayama continuant après p.46 et celle de III.4.12 après p.69 ne sont pas dites lues en entier.

Attestations courtes : « Lemme d’évitement », « Théorème des restes chinois », « transposée de la comatrice », « de type fini ».

Noms des lemmes et opérations matricielles, génération finie et rang, annulation des endomorphismes, spectre et radicaux.

Limites : L'exercice d'évitement ne donne pas la généralité des deux idéaux non premiers de Stacks. La preuve matricielle et celle du rang ne remplacent pas celles de Stacks. Les coquilles pour pour et les notations locales de l'ouvrage ne sont pas importées.

SHA-256 : `3FF86D7FD86BA2F1A349ACABE9E4FDDE57282B7A58D66A741CC78BE40E971CC0`.

### Antoine Ducros, Introduction à la théorie des schémas, juillet 2021

[Source universitaire](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [PDF conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages indiquées lues en entier ; surtout 4.1.3–12,4.1.22–26 avec démonstrations. Les développements sur les points géométriques coupés par pp.190–191 et la suite de 4.1.29 après p.196 ne sont pas dits entièrement lus.

Attestations courtes : « topologie de Zariski », « quasi-compact », « foncteur contravariant », « homéomorphisme ».

Spectre de tous les premiers, distinction quasi-compact/compact, fonctorialité inverse, topologie des quotients et localisés.

Limites : La présentation par points et corps résiduels ne s'ajoute pas au texte officiel. E appartenant à A au lieu d'une partie en 4.1.7 et la parenthèse supplémentaire en 4.1.22 ne sont pas importés. Les remarques philosophiques et exemples nouveaux du cours restent hors traduction.

SHA-256 : `8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66`.

### Jean-François Dat, Introduction à la théorie des Schémas, Sorbonne Université, M2, 2025–2026

[Source universitaire](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/Schemas/Schemas.pdf) · [PDF conservé](canon-consulted/fr-algebra/dat-schemas.pdf)

Couverture/table p.1 et pp.7–9 entières. Surtout 1.2.4, définition des ouverts principaux et preuve de quasi-compacité ; 1.2.5 et début de 1.2.6.

Attestations courtes : « ouverts principaux », « polynôme unitaire ».

Attestation explicite de ouvert principal pour D(f), définition par non-appartenance, quasi-compacité et monic/unitaire.

Limites : L'hypothèse f non nilpotent du cas particulier p.8 n'est pas ajoutée à Stacks. La définition d'irréductible p.7 omet non vide et écrit tout ouvert dense : elle n'est pas importée. Les barres d'adhérence perdues à l'extraction dans 1.2.5 ont été vérifiées sur le rendu ; la continuation du cours au-delà de p.9 n'est pas prétendue lue.

SHA-256 : `9298B062AC2BDF64161A107980A30F98E1F2DF6DEB4DA98E1FEB21BA494D26A1`.

## Règles contextualisées

### FR-ALGEBRA-B4-RULE-ideaux

Distinguer premier, maximal et minimal ; ordre, inclusion et radical restent ceux de chaque assertion. Debarre III.5 et Ducros 4.1.

Canon : FR-ALGEBRA-B4-CANON-DEBARRE, FR-ALGEBRA-B4-CANON-DUCROS.

### FR-ALGEBRA-B4-RULE-evitement-chinois

Debarre III.4.5–4.6 atteste les noms. Cofinaux est vérifié dans le slogan source, pas comme un terme attesté dans ces exercices ; garder leurs hypothèses distinctes.

Canon : FR-ALGEBRA-B4-CANON-DEBARRE.

### FR-ALGEBRA-B4-RULE-matrices

La transposée des cofacteurs est l'objet de Debarre II.3, non une adjointe hermitienne ; garder tailles et indices. Changement de base désigne ici des bases de modules libres, pas des scalaires.

Canon : FR-ALGEBRA-B4-CANON-DEBARRE.

### FR-ALGEBRA-B4-RULE-modules

Debarre II.1–3 atteste le cadre. Ne pas substituer cardinal fini, espace vectoriel ou anneau intègre ; conserver l'anneau non nul là où il est demandé.

Canon : FR-ALGEBRA-B4-CANON-DEBARRE.

### FR-ALGEBRA-B4-RULE-polynomes

Cayley–Hamilton sur un module donne un annulateur unitaire, pas un polynôme caractéristique canonique du module. Debarre II.3.2–3.3 ; Dat 1.2.6 pour unitaire.

Canon : FR-ALGEBRA-B4-CANON-DEBARRE, FR-ALGEBRA-B4-CANON-DAT.

### FR-ALGEBRA-B4-RULE-spectre

Ducros 4.1.3–12 et Dat 1.2.4 : tous les premiers, D(f), recouvrement fini sans séparation. Ouvert principal n'est pas synonyme de tout ouvert affine.

Canon : FR-ALGEBRA-B4-CANON-DUCROS, FR-ALGEBRA-B4-CANON-DAT.

### FR-ALGEBRA-B4-RULE-topologie

Ducros 4.1.22–26 et Dat 1.2.4–5 : contravariance et topologie du sous-espace, ne pas confondre bijection et homéomorphisme ni image générale d'une localisation et ouvert.

Canon : FR-ALGEBRA-B4-CANON-DUCROS, FR-ALGEBRA-B4-CANON-DAT.

### FR-ALGEBRA-B4-RULE-preuves

Contrôle direct des étapes contre le texte officiel ; pas de preuve nouvelle ajoutée pour compléter une ellipse. Les attestations lexicales exactes non acquises dans ces pages ne sont pas inventées.

Canon : Comparaison directe ; attestation externe exacte non acquise.

## Passages parallèles complets

### 01 — section-miscellany

Anglais L2543–2549 ; français L2509–2515.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2543) · `FR-ALGEBRA-B4-CHOICE-0001`.

Divers rend le titre de rassemblement Miscellany sans inventer un sujet unique. La consigne limitant les références aux notions de base reste présente, même si la suite anglaise cite aussi la localisation ; cette discordance source n'est pas harmonisée.

Point particulier à relire : La restriction annoncée aux résultats de base et les références ultérieures ne sont pas harmonisées.

Règles : Titre et contexte directement comparés.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Miscellany}
\label{section-miscellany}

\noindent
The proofs in this section should not refer to any results except
those from the section on basic notions, Section \ref{section-rings-basic}.
```

Français conservé :
```tex
\section{Divers}
\label{section-miscellany}

\noindent
Les démonstrations de cette section ne doivent faire appel à aucun résultat
autre que ceux de la section sur les notions de base, la section \ref{section-rings-basic}.
```

</details>

### 02 — lemma-product-ideals-in-prime

Anglais L2550–2562 ; français L2516–2528.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2550) · `FR-ALGEBRA-B4-CHOICE-0002`.

Premier qualifie l'idéal, non un élément ni un ordre. Contient et appartient à conservent la différence entre inclusion et appartenance. Le raisonnement par contradiction et les deux choix hors de l'idéal restent identiques ; aucune hypothèse d'intégrité de R n'est ajoutée.

Règles : FR-ALGEBRA-B4-RULE-ideaux.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-product-ideals-in-prime}
Let $R$ be a ring, $I$ and $J$ two ideals and $\mathfrak p$ a prime ideal
containing the product $IJ$. Then $\mathfrak{p}$ contains $I$ or $J$.
\end{lemma}

\begin{proof}
Assume the contrary and take $x \in I \setminus \mathfrak p$ and
$y \in J \setminus \mathfrak p$. Their product is an element of
$IJ \subset \mathfrak p$, which contradicts the assumption that
$\mathfrak p$ was prime.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-product-ideals-in-prime}
Soient $R$ un anneau, $I$ et $J$ deux idéaux, et $\mathfrak p$ un idéal premier
contenant le produit $IJ$. Alors $\mathfrak{p}$ contient $I$ ou $J$.
\end{lemma}

\begin{proof}
Supposons le contraire et choisissons $x \in I \setminus \mathfrak p$ et
$y \in J \setminus \mathfrak p$. Leur produit appartient à
$IJ \subset \mathfrak p$, ce qui contredit le fait que
$\mathfrak p$ est premier.
\end{proof}
```

</details>

### 03 — lemma-silly

Anglais L2563–2595 ; français L2529–2563.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2563) · `FR-ALGEBRA-B4-CHOICE-0003`.

Évitement des idéaux premiers est motivé par le lemme d'évitement de Debarre III, exercice 4.5. Le Stacks permet deux idéaux non premiers : cette généralité est conservée, contrairement à l'exercice où ils sont tous premiers. Les deux slogans restent distincts, les ouverts affines ne deviennent pas tous principaux. Cofinaux s'interprète selon les voisinages ordonnés par raffinement, non comme inclusion croissante imposée. Les cas r=1, r=2 puis la récurrence et les produits d'idéaux restent présents.

Règles : FR-ALGEBRA-B4-RULE-ideaux, FR-ALGEBRA-B4-RULE-evitement-chinois, FR-ALGEBRA-B4-RULE-spectre, FR-ALGEBRA-B4-RULE-preuves.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}[Prime avoidance]
\label{lemma-silly}
\begin{slogan}
1. In an affine scheme if a finite number of points are contained in an
open subset then they are contained in a smaller principal open subset.
2. Affine opens are cofinal among the neighborhoods of a given finite set
of an affine scheme
\end{slogan}
Let $R$ be a ring. Let $I_i \subset R$, $i = 1, \ldots, r$,
and $J \subset R$ be ideals. Assume
\begin{enumerate}
\item $J \not\subset I_i$ for $i = 1, \ldots, r$, and
\item all but two of $I_i$ are prime ideals.
\end{enumerate}
Then there exists an $x \in J$, $x\not\in I_i$ for all $i$.
\end{lemma}

\begin{proof}
The result is true for $r = 1$. If $r = 2$, then let $x, y \in J$ with
$x \not \in I_1$ and $y \not \in I_2$. We are done unless $x \in I_2$
and $y \in I_1$. Then the element $x + y$ cannot be in $I_1$ (since that
would mean $x + y - y \in I_1$) and it also cannot be in $I_2$.

\medskip\noindent
For $r \geq 3$, assume the result holds for $r - 1$. After renumbering
we may assume that $I_r$ is prime. We may also assume there are no
inclusions among the $I_i$. Pick $x \in J$, $x \not \in I_i$ for all
$i = 1, \ldots, r - 1$. If $x \not\in I_r$ we are done. So assume
$x \in I_r$. If $J I_1 \ldots I_{r - 1} \subset I_r$ then
$J \subset I_r$ (by Lemma \ref{lemma-product-ideals-in-prime}) a contradiction.
Pick $y \in J I_1 \ldots I_{r - 1}$, $y \not \in I_r$. Then $x + y$ works.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}[Évitement des idéaux premiers]
\label{lemma-silly}
\begin{slogan}
1. Dans un schéma affine, tout ensemble fini de points contenu dans un
ouvert est contenu dans un ouvert principal plus petit.
2. Les ouverts affines sont cofinaux parmi les voisinages d'une partie finie
donnée d'un schéma affine.
\end{slogan}
Soit $R$ un anneau. Soient $I_i \subset R$, $i = 1, \ldots, r$,
et $J \subset R$ des idéaux. Supposons que
\begin{enumerate}
\item $J \not\subset I_i$ pour $i = 1, \ldots, r$, et
\item tous les $I_i$ sauf deux sont des idéaux premiers.
\end{enumerate}
Alors il existe $x \in J$ tel que $x\not\in I_i$ pour tout $i$.
\end{lemma}

\begin{proof}
Le résultat est vrai pour $r = 1$. Si $r = 2$, choisissons $x, y \in J$ tels que
$x \not \in I_1$ et $y \not \in I_2$. Nous avons conclu, sauf si $x \in I_2$
et $y \in I_1$. Mais alors l'élément $x + y$ ne peut appartenir à $I_1$
(car cela entraînerait $x + y - y \in I_1$), ni à $I_2$.

\medskip\noindent
Pour $r \geq 3$, supposons le résultat vrai pour $r - 1$. Après renumérotation,
nous pouvons supposer que $I_r$ est premier. Nous pouvons aussi supposer
qu'il n'existe aucune inclusion entre les $I_i$. Choisissons $x \in J$ tel que
$x \not \in I_i$ pour tout $i = 1, \ldots, r - 1$. Si $x \not\in I_r$,
nous avons conclu. Supposons donc $x \in I_r$. Si
$J I_1 \ldots I_{r - 1} \subset I_r$, alors
$J \subset I_r$ (par le lemme \ref{lemma-product-ideals-in-prime}), contradiction.
Choisissons $y \in J I_1 \ldots I_{r - 1}$ tel que $y \not \in I_r$.
Alors $x + y$ convient.
\end{proof}
```

</details>

### 04 — lemma-silly-silly

Anglais L2596–2614 ; français L2564–2583.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2596) · `FR-ALGEBRA-B4-CHOICE-0004`.

Le translaté x+I, l'ordre des indices autour de s et l'élément fy restent les mêmes. N'appartient à aucun rend sans ambiguïté l'évitement simultané de chaque idéal énuméré. La possibilité de choisir f et la récurrence sont condensées comme dans l'anglais ; aucune justification supplémentaire n'est insérée dans la traduction.

Règles : FR-ALGEBRA-B4-RULE-ideaux, FR-ALGEBRA-B4-RULE-preuves.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-silly-silly}
Let $R$ be a ring. Let $x \in R$, $I \subset R$ an ideal, and
$\mathfrak p_i$, $i = 1, \ldots, r$ be prime ideals.
Suppose that $x + I \not \subset \mathfrak p_i$ for
$i = 1, \ldots, r$. Then there exists a $y \in I$
such that $x + y \not \in \mathfrak p_i$ for all $i$.
\end{lemma}

\begin{proof}
We may assume there are no inclusions among the $\mathfrak p_i$.
After reordering we may assume $x \not \in \mathfrak p_i$ for $i < s$
and $x \in \mathfrak p_i$ for $i \geq s$. If $s = r + 1$ then we are done.
If not, then we can find $y \in I$ with $y \not \in \mathfrak p_s$.
Choose $f \in \bigcap_{i < s} \mathfrak p_i$ with $f \not \in \mathfrak p_s$.
Then $x + fy$ is not contained in $\mathfrak p_1, \ldots, \mathfrak p_s$.
Thus we win by induction on $s$.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-silly-silly}
Soit $R$ un anneau. Soient $x \in R$, $I \subset R$ un idéal, et
$\mathfrak p_i$, $i = 1, \ldots, r$, des idéaux premiers.
Supposons que $x + I \not \subset \mathfrak p_i$ pour
$i = 1, \ldots, r$. Alors il existe $y \in I$
tel que $x + y \not \in \mathfrak p_i$ pour tout $i$.
\end{lemma}

\begin{proof}
Nous pouvons supposer qu'il n'existe aucune inclusion entre les $\mathfrak p_i$.
Après réordonnement, nous pouvons supposer $x \not \in \mathfrak p_i$ pour $i < s$
et $x \in \mathfrak p_i$ pour $i \geq s$. Si $s = r + 1$, nous avons conclu.
Sinon, nous pouvons trouver $y \in I$ tel que $y \not \in \mathfrak p_s$.
Choisissons $f \in \bigcap_{i < s} \mathfrak p_i$ tel que
$f \not \in \mathfrak p_s$.
Alors $x + fy$ n'appartient à aucun de $\mathfrak p_1, \ldots, \mathfrak p_s$.
Nous concluons donc par récurrence sur $s$.
\end{proof}
```

</details>

### 05 — lemma-chinese-remainder

Anglais L2615–2666 ; français L2584–2636.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2615) · `FR-ALGEBRA-B4-CHOICE-0005`.

Théorème des restes chinois est attesté chez Debarre III, exercice 4.6, mais l'environnement lemma officiel reste intact. La condition deux à deux porte sur les sommes d'idéaux, pas sur leur primauté. Les deux inclusions, la décomposition de 1, l'image de chaque a_i et l'antécédent construit sont intégralement conservés. Élément unité nomme ici 1, pas une unité quelconque ; on ne remplace pas la preuve par l'exercice du canon.

Règles : FR-ALGEBRA-B4-RULE-ideaux, FR-ALGEBRA-B4-RULE-evitement-chinois, FR-ALGEBRA-B4-RULE-polynomes, FR-ALGEBRA-B4-RULE-preuves.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}[Chinese remainder]
\label{lemma-chinese-remainder}
Let $R$ be a ring.
\begin{enumerate}
\item If $I_1, \ldots, I_r$ are ideals such that $I_a + I_b = R$
when $a \not = b$, then $I_1 \cap \ldots \cap I_r =
I_1I_2\ldots I_r$ and $R/(I_1I_2\ldots I_r)
\cong R/I_1 \times \ldots \times R/I_r$.
\item If $\mathfrak m_1, \ldots, \mathfrak m_r$ are pairwise distinct maximal
ideals then $\mathfrak m_a + \mathfrak m_b = R$ for $a \not = b$ and the
above applies.
\end{enumerate}
\end{lemma}

\begin{proof}
Let us first prove $I_1 \cap \ldots \cap I_r = I_1 \ldots I_r$
as this will also imply the injectivity of the induced ring
homomorphism $R/(I_1 \ldots I_r) \rightarrow R/I_1 \times \ldots \times R/I_r$.
The inclusion $I_1 \cap \ldots \cap I_r \supset I_1 \ldots I_r$ is always
fulfilled since ideals are closed under multiplication with arbitrary ring
elements. To prove the other inclusion, we claim that the ideals
$$
I_1 \ldots \hat I_i \ldots I_r,\quad i = 1, \ldots, r
$$
generate the ring $R$. We prove this by induction on $r$. It holds when
$r = 2$. If $r > 2$, then we see that $R$ is the sum of the ideals
$I_1 \ldots \hat I_i \ldots I_{r - 1}$, $i = 1, \ldots, r - 1$.
Hence $I_r$ is the sum of the ideals
$I_1 \ldots \hat I_i \ldots I_r$, $i = 1, \ldots, r - 1$.
Applying the same argument with the reverse ordering on the ideals
we see that $I_1$ is the sum of the ideals
$I_1 \ldots \hat I_i \ldots I_r$, $i = 2, \ldots, r$.
Since $R = I_1 + I_r$ by assumption we see that $R$ is the sum of the
ideals displayed above. Therefore we can find elements
$a_i \in I_1 \ldots \hat I_i \ldots I_r$
such that their sum is one. Multiplying this equation by an element
of $I_1 \cap \ldots \cap I_r$ gives the other inclusion.
It remains to show that the canonical map
$R/(I_1 \ldots I_r) \rightarrow R/I_1 \times \ldots \times R/I_r$
is surjective. For this, consider its action on the equation
$1 = \sum_{i=1}^r a_i$ we derived above. On the one hand, a
ring morphism sends 1 to 1 and on the other hand, the image of any
$a_i$ is zero in $R/I_j$ for $j \neq i$. Therefore, the image of $a_i$
in $R/I_i$ is the identity. So given any element
$(\bar{b_1}, \ldots, \bar{b_r}) \in R/I_1 \times \ldots \times R/I_r$,
the element $\sum_{i=1}^r a_i \cdot b_i$ is an inverse image in $R$.

\medskip\noindent
To see (2), by the very definition of being distinct maximal ideals, we have
$\mathfrak{m}_a + \mathfrak{m}_b = R$ for $a \neq b$ and so the above applies.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}[Théorème des restes chinois]
\label{lemma-chinese-remainder}
Soit $R$ un anneau.
\begin{enumerate}
\item Si $I_1, \ldots, I_r$ sont des idéaux tels que $I_a + I_b = R$
lorsque $a \not = b$, alors $I_1 \cap \ldots \cap I_r =
I_1I_2\ldots I_r$ et $R/(I_1I_2\ldots I_r)
\cong R/I_1 \times \ldots \times R/I_r$.
\item Si $\mathfrak m_1, \ldots, \mathfrak m_r$ sont des idéaux maximaux
deux à deux distincts, alors $\mathfrak m_a + \mathfrak m_b = R$ pour
$a \not = b$, et ce qui précède s'applique.
\end{enumerate}
\end{lemma}

\begin{proof}
Démontrons d'abord $I_1 \cap \ldots \cap I_r = I_1 \ldots I_r$,
car cela entraînera aussi l'injectivité du morphisme d'anneaux induit
$R/(I_1 \ldots I_r) \rightarrow R/I_1 \times \ldots \times R/I_r$.
L'inclusion $I_1 \cap \ldots \cap I_r \supset I_1 \ldots I_r$ est toujours
vraie, puisque les idéaux sont stables par multiplication par des éléments
quelconques de l'anneau. Pour démontrer l'autre inclusion, affirmons que les idéaux
$$
I_1 \ldots \hat I_i \ldots I_r,\quad i = 1, \ldots, r
$$
engendrent l'anneau $R$. Nous le démontrons par récurrence sur $r$.
C'est vrai pour $r = 2$. Si $r > 2$, nous voyons que $R$ est la somme des idéaux
$I_1 \ldots \hat I_i \ldots I_{r - 1}$, $i = 1, \ldots, r - 1$.
Par conséquent, $I_r$ est la somme des idéaux
$I_1 \ldots \hat I_i \ldots I_r$, $i = 1, \ldots, r - 1$.
En appliquant le même argument aux idéaux pris dans l'ordre inverse,
nous voyons que $I_1$ est la somme des idéaux
$I_1 \ldots \hat I_i \ldots I_r$, $i = 2, \ldots, r$.
Puisque $R = I_1 + I_r$ par hypothèse, nous voyons que $R$ est la somme
des idéaux affichés ci-dessus. Nous pouvons donc trouver des éléments
$a_i \in I_1 \ldots \hat I_i \ldots I_r$
dont la somme vaut un. En multipliant cette égalité par un élément
de $I_1 \cap \ldots \cap I_r$, nous obtenons l'autre inclusion.
Il reste à montrer que l'application canonique
$R/(I_1 \ldots I_r) \rightarrow R/I_1 \times \ldots \times R/I_r$
est surjective. Pour cela, considérons son action sur l'égalité
$1 = \sum_{i=1}^r a_i$ obtenue ci-dessus. D'une part, un
morphisme d'anneaux envoie 1 sur 1 ; d'autre part, l'image de tout
$a_i$ est nulle dans $R/I_j$ pour $j \neq i$. L'image de $a_i$
dans $R/I_i$ est donc l'élément unité. Ainsi, pour tout élément
$(\bar{b_1}, \ldots, \bar{b_r}) \in R/I_1 \times \ldots \times R/I_r$,
l'élément $\sum_{i=1}^r a_i \cdot b_i$ en est un antécédent dans $R$.

\medskip\noindent
Pour voir (2), la définition même d'idéaux maximaux distincts donne
$\mathfrak{m}_a + \mathfrak{m}_b = R$ pour $a \neq b$,
et ce qui précède s'applique.
\end{proof}
```

</details>

### 06 — lemma-matrix-left-inverse

Anglais L2667–2704 ; français L2637–2674.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2667) · `FR-ALGEBRA-B4-CHOICE-0006`.

Mineurs désigne les déterminants sélectionnés, avec les mêmes lignes I. Matrice adjointe est immédiatement définie comme la transposée de la matrice des cofacteurs : elle n'est donc pas une adjointe hermitienne. Debarre II.3 emploie transposée de la comatrice pour la même opération ; cette variante est signalée, sans remplacement stylistique indispensable. Les tailles m par n, les produits B_I E_I et l'exposant f^m de Cauchy–Binet restent exacts.

Point particulier à relire : Variante canonique disponible : transposée de la comatrice. Le syntagme adjointe est gardé seulement avec sa définition explicite, jamais interprété au sens hermitien.

Règles : FR-ALGEBRA-B4-RULE-matrices.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-matrix-left-inverse}
Let $R$ be a ring. Let $n \geq m$. Let $A$ be an
$n \times m$ matrix with coefficients in $R$. Let $J \subset R$
be the ideal generated by the $m \times m$ minors of $A$.
\begin{enumerate}
\item For any $f \in J$ there exists a $m \times n$ matrix $B$
such that $BA = f 1_{m \times m}$.
\item If $f \in R$ and $BA = f 1_{m \times m}$ for some $m \times n$ matrix
$B$, then $f^m \in J$.
\end{enumerate}
\end{lemma}

\begin{proof}
For $I \subset \{1, \ldots, n\}$ with $|I| = m$, we denote
by $E_I$ the $m \times n$ matrix of the projection
$$
R^{\oplus n} = \bigoplus\nolimits_{i \in \{1, \ldots, n\}} R
\longrightarrow \bigoplus\nolimits_{i \in I} R
$$
and set $A_I = E_I A$, i.e., $A_I$ is the $m \times m$ matrix
whose rows are the rows of $A$ with indices in $I$.
Let $B_I$ be the adjugate (transpose of
cofactor) matrix to $A_I$, i.e., such that
$A_I B_I = B_I A_I = \det(A_I) 1_{m \times m}$.
The $m \times m$ minors of $A$ are the determinants $\det A_I$
for all the $I \subset \{1, \ldots, n\}$ with $|I| = m$.
If $f \in J$ then we can write $f = \sum c_I \det(A_I)$ for some
$c_I \in R$. Set $B = \sum c_I B_I E_I$ to see that (1) holds.

\medskip\noindent
If $f 1_{m \times m} = BA$ then by the
Cauchy-Binet formula (\ref{item-cauchy-binet}) we
have $f^m = \sum b_I \det(A_I)$ where $b_I$ is the determinant
of the $m \times m$ matrix whose columns are the columns of $B$ with
indices in $I$.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-matrix-left-inverse}
Soit $R$ un anneau. Soit $n \geq m$. Soit $A$ une matrice
$n \times m$ à coefficients dans $R$. Soit $J \subset R$
l'idéal engendré par les mineurs $m \times m$ de $A$.
\begin{enumerate}
\item Pour tout $f \in J$, il existe une matrice $m \times n$, $B$,
telle que $BA = f 1_{m \times m}$.
\item Si $f \in R$ et $BA = f 1_{m \times m}$ pour une matrice
$m \times n$, $B$, alors $f^m \in J$.
\end{enumerate}
\end{lemma}

\begin{proof}
Pour $I \subset \{1, \ldots, n\}$ avec $|I| = m$, notons
$E_I$ la matrice $m \times n$ de la projection
$$
R^{\oplus n} = \bigoplus\nolimits_{i \in \{1, \ldots, n\}} R
\longrightarrow \bigoplus\nolimits_{i \in I} R
$$
et posons $A_I = E_I A$ ; ainsi, $A_I$ est la matrice $m \times m$
dont les lignes sont celles de $A$ d'indices appartenant à $I$.
Soit $B_I$ la matrice adjointe (transposée de la matrice
des cofacteurs) de $A_I$, c'est-à-dire telle que
$A_I B_I = B_I A_I = \det(A_I) 1_{m \times m}$.
Les mineurs $m \times m$ de $A$ sont les déterminants $\det A_I$
pour tous les $I \subset \{1, \ldots, n\}$ tels que $|I| = m$.
Si $f \in J$, nous pouvons écrire $f = \sum c_I \det(A_I)$ avec
$c_I \in R$. Posons $B = \sum c_I B_I E_I$ ; cela démontre (1).

\medskip\noindent
Si $f 1_{m \times m} = BA$, la formule de Cauchy-Binet
(\ref{item-cauchy-binet}) donne
$f^m = \sum b_I \det(A_I)$, où $b_I$ est le déterminant
de la matrice $m \times m$ dont les colonnes sont celles de $B$
d'indices appartenant à $I$.
\end{proof}
```

</details>

### 07 — lemma-matrix-right-inverse

Anglais L2705–2745 ; français L2675–2714.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2705) · `FR-ALGEBRA-B4-CHOICE-0007`.

Le découpage vertical de A et la matrice des cofacteurs sont conservés. Au signe près ne devient pas un signe fixé. La source abrège l'identité matricielle en f et écrit A_1^{ij} devant une description en j,k ; les deux lectures restent littérales. Transposée de la comatrice serait la variante attestée chez Debarre, mais la définition actuelle explicite déjà exactement l'objet.

Point particulier à relire : Incohérence d'indices A_1^{ij}/j,k et raccourci f de la source maintenus ; ce dossier n'est pas une nouvelle admission d'erratum.

Règles : FR-ALGEBRA-B4-RULE-matrices.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-matrix-right-inverse}
Let $R$ be a ring. Let $n \geq m$. Let $A = (a_{ij})$ be an
$n \times m$ matrix with coefficients in $R$, written in block form
as
$$
A =
\left(
\begin{matrix}
A_1 \\
A_2
\end{matrix}
\right)
$$
where $A_1$ has size $m \times m$. Let $B$ be the adjugate (transpose of
cofactor) matrix to $A_1$. Then
$$
AB = 
\left(
\begin{matrix}
f 1_{m \times m} \\
C
\end{matrix}
\right)
$$
where $f = \det(A_1)$ and $c_{ij}$ is (up to sign) the determinant of the
$m \times m$ minor of $A$ corresponding to the rows
$1, \ldots, \hat j, \ldots, m, i$.
\end{lemma}

\begin{proof}
Since the adjugate has the property $A_1B = B A_1 = f$ the first block
of the expression for $AB$ is correct. Note that
$$
c_{ij} = \sum\nolimits_k a_{ik}b_{kj} = \sum (-1)^{j + k}a_{ik} \det(A_1^{jk})
$$
where $A_1^{ij}$ means $A_1$ with the $j$th row and $k$th column removed.
This last expression is the row expansion of the determinant of the matrix
in the statement of the lemma.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-matrix-right-inverse}
Soit $R$ un anneau. Soit $n \geq m$. Soit $A = (a_{ij})$ une matrice
$n \times m$ à coefficients dans $R$, écrite par blocs sous la forme
$$
A =
\left(
\begin{matrix}
A_1 \\
A_2
\end{matrix}
\right)
$$
où $A_1$ est de taille $m \times m$. Soit $B$ la matrice adjointe
(transposée de la matrice des cofacteurs) de $A_1$. Alors
$$
AB = 
\left(
\begin{matrix}
f 1_{m \times m} \\
C
\end{matrix}
\right)
$$
où $f = \det(A_1)$ et où $c_{ij}$ est, au signe près, le déterminant du
mineur $m \times m$ de $A$ correspondant aux lignes
$1, \ldots, \hat j, \ldots, m, i$.
\end{lemma}

\begin{proof}
Puisque la matrice adjointe vérifie $A_1B = B A_1 = f$, le premier bloc
de l'expression de $AB$ est correct. Remarquons que
$$
c_{ij} = \sum\nolimits_k a_{ik}b_{kj} = \sum (-1)^{j + k}a_{ik} \det(A_1^{jk})
$$
où $A_1^{ij}$ désigne la matrice $A_1$ privée de sa $j$-ième ligne
et de sa $k$-ième colonne. Cette dernière expression est le développement
suivant une ligne du déterminant de la matrice de l'énoncé du lemme.
\end{proof}
```

</details>

### 08 — lemma-map-cannot-be-injective

Anglais L2746–2787 ; français L2715–2758.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2746) · `FR-ALGEBRA-B4-CHOICE-0008`.

Source et but désignent les modules du morphisme, et de type fini ne veut pas dire ensemble fini. L'anneau non nul est essentiel et conservé. Changement de base dans les deux modules libres désigne ici le changement des bases qui réduit la matrice, pas une nouvelle extension des scalaires ; la localisation a été effectuée juste avant. Relèvement, exactitude, cas nilpotent et dernier exposant non nul restent ceux de l'anglais. Debarre II.1 atteste rang et module libre, sans substituer sa preuve par quotient maximal.

Règles : FR-ALGEBRA-B4-RULE-matrices, FR-ALGEBRA-B4-RULE-modules, FR-ALGEBRA-B4-RULE-polynomes, FR-ALGEBRA-B4-RULE-preuves.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-map-cannot-be-injective}
\begin{slogan}
A map of finite free modules cannot be injective if the source has
rank bigger than the target.
\end{slogan}
Let $R$ be a nonzero ring. Let $n \geq 1$. Let $M$ be an $R$-module generated
by $< n$ elements. Then any $R$-module map $f : R^{\oplus n} \to M$ has a
nonzero kernel.
\end{lemma}

\begin{proof}
Choose a surjection $R^{\oplus n - 1} \to M$.
We may lift the map $f$ to a map $f' : R^{\oplus n} \to R^{\oplus n - 1}$
(Lemma \ref{lemma-lift-map}).
It suffices to prove $f'$ has a nonzero kernel.
The map $f' : R^{\oplus n} \to R^{\oplus n - 1}$ is given by a
matrix $A = (a_{ij})$. If one of the $a_{ij}$ is not nilpotent, say
$a = a_{ij}$ is not, then we can replace $R$ by the localization $R_a$
and we may assume $a_{ij}$ is a unit. Since if we find a nonzero kernel
after localization then there was a nonzero kernel to start with as
localization is exact, see Proposition \ref{proposition-localization-exact}.
In this case we can do a base change on both $R^{\oplus n}$
and $R^{\oplus n - 1}$ and reduce to the case where
$$
A =
\left(
\begin{matrix}
1 & 0 & 0 & \ldots \\
0 & a_{22} & a_{23} & \ldots \\
0 & a_{32} & \ldots \\
\ldots & \ldots
\end{matrix}
\right)
$$
Hence in this case we win by induction on $n$. If not then each
$a_{ij}$ is nilpotent. Set $I = (a_{ij}) \subset R$. Note that
$I^{m + 1} = 0$ for some $m \geq 0$. Let $m$ be the largest integer
such that $I^m \not = 0$. Then we see that $(I^m)^{\oplus n}$ is
contained in the kernel of the map and we win.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-map-cannot-be-injective}
\begin{slogan}
Un morphisme de modules libres de type fini ne peut être injectif si la source
est de rang strictement supérieur à celui du but.
\end{slogan}
Soit $R$ un anneau non nul. Soit $n \geq 1$. Soit $M$ un $R$-module engendré
par un nombre d'éléments $< n$. Alors tout morphisme de $R$-modules
$f : R^{\oplus n} \to M$ a un noyau non nul.
\end{lemma}

\begin{proof}
Choisissons une surjection $R^{\oplus n - 1} \to M$.
Nous pouvons relever le morphisme $f$ en un morphisme
$f' : R^{\oplus n} \to R^{\oplus n - 1}$
(lemme \ref{lemma-lift-map}).
Il suffit de démontrer que $f'$ a un noyau non nul.
Le morphisme $f' : R^{\oplus n} \to R^{\oplus n - 1}$ est donné par une
matrice $A = (a_{ij})$. Si l'un des $a_{ij}$ n'est pas nilpotent, disons
que $a = a_{ij}$ ne l'est pas, nous pouvons remplacer $R$ par la localisation
$R_a$ et supposer que $a_{ij}$ est une unité. En effet, si nous trouvons un
noyau non nul après localisation, il existait déjà un noyau non nul,
car la localisation est exacte ; voir la proposition
\ref{proposition-localization-exact}.
Dans ce cas, nous pouvons effectuer un changement de base à la fois dans
$R^{\oplus n}$ et dans $R^{\oplus n - 1}$ et nous ramener au cas où
$$
A =
\left(
\begin{matrix}
1 & 0 & 0 & \ldots \\
0 & a_{22} & a_{23} & \ldots \\
0 & a_{32} & \ldots \\
\ldots & \ldots
\end{matrix}
\right)
$$
Nous concluons alors par récurrence sur $n$. Sinon, chaque
$a_{ij}$ est nilpotent. Posons $I = (a_{ij}) \subset R$. Remarquons que
$I^{m + 1} = 0$ pour un certain $m \geq 0$. Soit $m$ le plus grand entier
tel que $I^m \not = 0$. Alors $(I^m)^{\oplus n}$ est
contenu dans le noyau du morphisme, ce qui conclut.
\end{proof}
```

</details>

### 09 — lemma-rank

Anglais L2788–2805 ; français L2759–2772.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2788) · `FR-ALGEBRA-B4-CHOICE-0009`.

Le rang est bien défini pour un module libre sur un anneau non nul, comme dans Debarre II.1.1. Aucun passage au corps des fractions ni hypothèse d'intégrité n'est ajouté. La preuve reste le renvoi bref au lemme précédent.

Règles : FR-ALGEBRA-B4-RULE-modules.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-rank}
\begin{slogan}
The rank of a finite free module is well defined.
\end{slogan}
Let $R$ be a nonzero ring. Let $n, m \geq 0$ be integers.
If $R^{\oplus n}$ is isomorphic to $R^{\oplus m}$ as
$R$-modules, then $n = m$.
\end{lemma}

\begin{proof}
Immediate from Lemma \ref{lemma-map-cannot-be-injective}.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-rank}
\begin{slogan}
Le rang d'un module libre de type fini est bien défini.
\end{slogan}
Soit $R$ un anneau non nul. Soient $n, m \geq 0$ des entiers.
Si $R^{\oplus n}$ est isomorphe à $R^{\oplus m}$ comme
$R$-modules, alors $n = m$.
\end{lemma}

\begin{proof}
C'est immédiat d'après le lemme \ref{lemma-map-cannot-be-injective}.
\end{proof}
```

</details>

### 10 — section-cayley-hamilton

Anglais L2806–2808 ; français L2773–2775.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2806) · `FR-ALGEBRA-B4-CHOICE-0010`.

Le titre propre Cayley-Hamilton et son label sont conservés. Il ne devient ni un chapitre sur les seuls espaces vectoriels ni une nouvelle désignation de résultat.

Règles : FR-ALGEBRA-B4-RULE-polynomes.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Cayley-Hamilton}
\label{section-cayley-hamilton}
```

Français conservé :
```tex
\section{Cayley-Hamilton}
\label{section-cayley-hamilton}
```

</details>

### 11 — lemma-charpoly

Anglais L2809–2833 ; français L2776–2800.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2809) · `FR-ALGEBRA-B4-CHOICE-0011`.

Polynôme caractéristique garde la convention det(x id-A), pas det(A-x id). La descente le long d'un morphisme, le passage par un morphisme injectif et la matrice universelle sont trois étapes distinctes. On ne suppose pas que le morphisme du premier item est surjectif : seuls les antécédents des coefficients y sont demandés. La référence au théorème classique reste sans citation supplémentaire.

Règles : FR-ALGEBRA-B4-RULE-polynomes.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-charpoly}
Let $R$ be a ring. Let $A = (a_{ij})$ be an $n \times n$
matrix with coefficients in $R$. Let $P(x) \in R[x]$
be the characteristic polynomial of $A$ (defined
as $\det(x\text{id}_{n \times n} - A)$).
Then $P(A) = 0$ in $\text{Mat}(n \times n, R)$.
\end{lemma}

\begin{proof}
We reduce the question to the well-known Cayley-Hamilton
theorem from linear algebra in several steps:
\begin{enumerate}
\item If $\phi :S \rightarrow R$ is a ring morphism and $b_{ij}$
are inverse images of the $a_{ij}$ under this map, then it suffices
to show the statement for $S$ and $(b_{ij})$ since $\phi$ is a ring morphism.
\item If $\psi :R \hookrightarrow S$ is an injective ring morphism, it
clearly suffices to show the result for $S$ and the $a_{ij}$ considered as
elements of $S$. 
\item Thus we may first reduce to the case $R = \mathbf{Z}[X_{ij}]$,
$a_{ij} = X_{ij}$ of a polynomial ring and then further to
the case $R = \mathbf{Q}(X_{ij})$ where we may finally apply Cayley-Hamilton.
\end{enumerate}
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-charpoly}
Soit $R$ un anneau. Soit $A = (a_{ij})$ une matrice $n \times n$
à coefficients dans $R$. Soit $P(x) \in R[x]$
le polynôme caractéristique de $A$ (défini
comme $\det(x\text{id}_{n \times n} - A)$).
Alors $P(A) = 0$ dans $\text{Mat}(n \times n, R)$.
\end{lemma}

\begin{proof}
Nous ramenons la question au théorème de Cayley-Hamilton bien connu
d'algèbre linéaire, en plusieurs étapes :
\begin{enumerate}
\item Si $\phi :S \rightarrow R$ est un morphisme d'anneaux et si les $b_{ij}$
sont des antécédents des $a_{ij}$ par ce morphisme, il suffit de démontrer
l'énoncé pour $S$ et $(b_{ij})$, puisque $\phi$ est un morphisme d'anneaux.
\item Si $\psi :R \hookrightarrow S$ est un morphisme injectif d'anneaux,
il suffit clairement de démontrer le résultat pour $S$ et pour les $a_{ij}$
considérés comme éléments de $S$.
\item Nous pouvons donc d'abord nous ramener au cas $R = \mathbf{Z}[X_{ij}]$,
$a_{ij} = X_{ij}$, d'un anneau de polynômes, puis au
cas $R = \mathbf{Q}(X_{ij})$, où nous pouvons enfin appliquer Cayley-Hamilton.
\end{enumerate}
\end{proof}
```

</details>

### 12 — lemma-charpoly-module

Anglais L2834–2859 ; français L2801–2826.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2834) · `FR-ALGEBRA-B4-CHOICE-0012`.

Finite devient de type fini ; monic devient unitaire. Debarre II.3.2 traite le même type d'annulation d'un endomorphisme, et Dat 1.2.6 atteste polynôme unitaire. Existence d'un polynôme annulateur ne signifie pas existence d'un polynôme caractéristique canonique du module. Les coefficients et le diagramme restent ceux de la source, y compris sa convention d'indices qui peut paraître transposée si l'on représente les vecteurs en colonnes.

Point particulier à relire : Le choix lignes/colonnes de la matrice du relèvement n'est pas silencieusement rectifié ; la preuve du canon n'est pas substituée.

Règles : FR-ALGEBRA-B4-RULE-modules, FR-ALGEBRA-B4-RULE-polynomes.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-charpoly-module}
Let $R$ be a ring.
Let $M$ be a finite $R$-module.
Let $\varphi : M \to M$ be an endomorphism.
Then there exists a monic polynomial $P \in R[T]$ such that
$P(\varphi) = 0$ as an endomorphism of $M$.
\end{lemma}

\begin{proof}
Choose a surjective $R$-module map $R^{\oplus n} \to M$, given by
$(a_1, \ldots, a_n) \mapsto \sum a_ix_i$ for some generators $x_i \in M$.
Choose $(a_{i1}, \ldots, a_{in}) \in R^{\oplus n}$ such that
$\varphi(x_i) = \sum a_{ij} x_j$. In other words the diagram
$$
\xymatrix{
R^{\oplus n} \ar[d]_A \ar[r] & M \ar[d]^\varphi \\
R^{\oplus n} \ar[r] & M
}
$$
is commutative where $A = (a_{ij})$. By
Lemma \ref{lemma-charpoly}
there exists a monic polynomial $P$ such that $P(A) = 0$.
Then it follows that $P(\varphi) = 0$.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-charpoly-module}
Soit $R$ un anneau.
Soit $M$ un $R$-module de type fini.
Soit $\varphi : M \to M$ un endomorphisme.
Alors il existe un polynôme unitaire $P \in R[T]$ tel que
$P(\varphi) = 0$ comme endomorphisme de $M$.
\end{lemma}

\begin{proof}
Choisissons un morphisme surjectif de $R$-modules $R^{\oplus n} \to M$, donné par
$(a_1, \ldots, a_n) \mapsto \sum a_ix_i$, pour des générateurs $x_i \in M$.
Choisissons $(a_{i1}, \ldots, a_{in}) \in R^{\oplus n}$ tels que
$\varphi(x_i) = \sum a_{ij} x_j$. Autrement dit, le diagramme
$$
\xymatrix{
R^{\oplus n} \ar[d]_A \ar[r] & M \ar[d]^\varphi \\
R^{\oplus n} \ar[r] & M
}
$$
est commutatif, où $A = (a_{ij})$. D'après
le lemme \ref{lemma-charpoly},
il existe un polynôme unitaire $P$ tel que $P(A) = 0$.
Il s'ensuit que $P(\varphi) = 0$.
\end{proof}
```

</details>

### 13 — lemma-charpoly-module-ideal

Anglais L2860–2891 ; français L2827–2858.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2860) · `FR-ALGEBRA-B4-CHOICE-0013`.

L'inclusion de l'image dans IM et les coefficients dans I^j sont conservés sans les affaiblir en I. Debarre II.3.2 atteste cette précision, mais sa preuve n'est pas importée. Le t minuscule dans le polynôme et R[T] majuscule viennent du témoin anglais. L'application plaisante finale garde le ton introductif de la source ; elle n'est pas un nouvel exemple mathématique.

Point particulier à relire : Même réserve sur lignes/colonnes ; t/T reste la notation du témoin.

Règles : FR-ALGEBRA-B4-RULE-modules, FR-ALGEBRA-B4-RULE-polynomes.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-charpoly-module-ideal}
Let $R$ be a ring. Let $I \subset R$ be an ideal.
Let $M$ be a finite $R$-module.
Let $\varphi : M \to M$ be an endomorphism such
that $\varphi(M) \subset IM$.
Then there exists a monic polynomial
$P = t^n + a_1 t^{n - 1} + \ldots + a_n \in R[T]$
such that $a_j \in I^j$ and $P(\varphi) = 0$ as an endomorphism of $M$.
\end{lemma}

\begin{proof}
Choose a surjective $R$-module map $R^{\oplus n} \to M$, given by
$(a_1, \ldots, a_n) \mapsto \sum a_ix_i$ for some generators $x_i \in M$.
Choose $(a_{i1}, \ldots, a_{in}) \in I^{\oplus n}$ such that
$\varphi(x_i) = \sum a_{ij} x_j$. In other words the diagram
$$
\xymatrix{
R^{\oplus n} \ar[d]_A \ar[r] & M \ar[d]^\varphi \\
I^{\oplus n} \ar[r] & M
}
$$
is commutative where $A = (a_{ij})$. By
Lemma \ref{lemma-charpoly}
the polynomial
$P(t) = \det(t\text{id}_{n \times n} - A)$
has all the desired properties.
\end{proof}

\noindent
As a fun example application we prove the following surprising lemma.
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-charpoly-module-ideal}
Soit $R$ un anneau. Soit $I \subset R$ un idéal.
Soit $M$ un $R$-module de type fini.
Soit $\varphi : M \to M$ un endomorphisme tel
que $\varphi(M) \subset IM$.
Alors il existe un polynôme unitaire
$P = t^n + a_1 t^{n - 1} + \ldots + a_n \in R[T]$
tel que $a_j \in I^j$ et que $P(\varphi) = 0$ comme endomorphisme de $M$.
\end{lemma}

\begin{proof}
Choisissons un morphisme surjectif de $R$-modules $R^{\oplus n} \to M$, donné par
$(a_1, \ldots, a_n) \mapsto \sum a_ix_i$, pour des générateurs $x_i \in M$.
Choisissons $(a_{i1}, \ldots, a_{in}) \in I^{\oplus n}$ tels que
$\varphi(x_i) = \sum a_{ij} x_j$. Autrement dit, le diagramme
$$
\xymatrix{
R^{\oplus n} \ar[d]_A \ar[r] & M \ar[d]^\varphi \\
I^{\oplus n} \ar[r] & M
}
$$
est commutatif, où $A = (a_{ij})$. D'après
le lemme \ref{lemma-charpoly},
le polynôme
$P(t) = \det(t\text{id}_{n \times n} - A)$
possède toutes les propriétés voulues.
\end{proof}

\noindent
À titre d'application plaisante, démontrons le lemme surprenant suivant.
```

</details>

### 14 — lemma-fun

Anglais L2892–2963 ; français L2859–2920.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2892) · `FR-ALGEBRA-B4-CHOICE-0014`.

Surjectif implique isomorphisme seulement dans le cadre du module de type fini énoncé ; aucune hypothèse noethérienne n'est ajoutée. Les deux preuves et leurs titres sont conservés. La première passe par l'action de x et l'identité, comme le mécanisme de Debarre II.3.3. La seconde distingue injectivité ensembliste, structure sur R[t], stabilité du sous-module, quotient et chasse au diagramme. Le masculin injectif se rapporte au morphisme déjà nommé ; les applications et la restriction restent au féminin. La colonne du milieu désigne sa flèche, comme dans l'anglais.

Règles : FR-ALGEBRA-B4-RULE-modules, FR-ALGEBRA-B4-RULE-polynomes, FR-ALGEBRA-B4-RULE-preuves.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-fun}
Let $R$ be a ring.
Let $M$ be a finite $R$-module.
Let $\varphi : M \to M$ be a surjective $R$-module map.
Then $\varphi$ is an isomorphism.
\end{lemma}

\begin{proof}[First proof]
Write $R' = R[x]$ and think of $M$ as a finite $R'$-module with
$x$ acting via $\varphi$. Set $I = (x) \subset R'$. By our assumption that
$\varphi$ is surjective we have $IM = M$. Hence we may apply
Lemma \ref{lemma-charpoly-module-ideal}
to $M$ as an $R'$-module, the ideal $I$ and the endomorphism $\text{id}_M$.
We conclude that
$(1 + a_1 + \ldots + a_n)\text{id}_M = 0$ with $a_j \in I$.
Write $a_j = b_j(x)x$ for some $b_j(x) \in R[x]$.
Translating back into $\varphi$ we see that
$\text{id}_M = -(\sum_{j = 1, \ldots, n} b_j(\varphi)) \varphi$, and hence
$\varphi$ is invertible.
\end{proof}

\begin{proof}[Second proof]
We perform induction on the number of generators of $M$ over $R$. If
$M$ is generated by one element, then $M \cong R/I$ for some ideal
$I \subset R$. In this case we may replace $R$ by $R/I$ so that $M = R$.
In this case $\varphi : R \to R$ is given by multiplication on $M$ by an
element $r \in R$. The surjectivity of $\varphi$ forces $r$ invertible,
since $\varphi$ must hit $1$, which implies that $\varphi$ is
invertible.

\medskip\noindent
Now assume that we have proven the lemma in the case of modules
generated by $n - 1$ elements, and are examining a module $M$ generated
by $n$ elements. Let $A$ mean the ring $R[t]$, and regard the module
$M$ as an $A$-module by letting $t$ act via $\varphi$; since $M$ is
finite over $R$, it is finite over $R[t]$ as well, and since we're
trying to prove $\varphi$ injective, a set-theoretic property, we might
as well prove the endomorphism $t : M \to M$ over $A$ injective. We have
reduced our problem to the case our endomorphism is multiplication by
an element of the ground ring. Let $M' \subset M$ denote the
sub-$A$-module generated by the first $n - 1$ of the generators of $M$,
and consider the diagram
$$
\xymatrix{
0 \ar[r] & M' \ar[r]\ar[d]^{\varphi\mid_{M'}} & M\ar[d]^\varphi \ar[r] &
M/M' \ar[d]^{\varphi \bmod M'} \ar[r] & 0 \\
0 \ar[r] & M' \ar[r]                                  & M \ar[r]
           & M/M' \ar[r]                                  & 0,
}
$$
where the restriction of $\varphi$ to $M'$ and the map induced by $\varphi$
on the quotient $M/M'$ are well-defined since $\varphi$ is multiplication
by an element in the base, and $M'$ and $M/M'$ are $A$-modules in
their own right. By the case $n = 1$ the map $M/M' \to M/M'$ is an
isomorphism. A diagram chase implies that $\varphi|_{M'}$ is surjective
hence by induction $\varphi|_{M'}$ is an isomorphism. This forces the
middle column to be an isomorphism by the snake lemma.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-fun}
Soit $R$ un anneau.
Soit $M$ un $R$-module de type fini.
Soit $\varphi : M \to M$ un morphisme surjectif de $R$-modules.
Alors $\varphi$ est un isomorphisme.
\end{lemma}

\begin{proof}[Première démonstration]
Écrivons $R' = R[x]$ et considérons $M$ comme un $R'$-module de type fini,
$x$ agissant par $\varphi$. Posons $I = (x) \subset R'$. L'hypothèse de
surjectivité de $\varphi$ donne $IM = M$. Nous pouvons donc appliquer
le lemme \ref{lemma-charpoly-module-ideal}
à $M$ considéré comme un $R'$-module, à l'idéal $I$ et à l'endomorphisme
$\text{id}_M$.
Nous en déduisons que
$(1 + a_1 + \ldots + a_n)\text{id}_M = 0$ avec $a_j \in I$.
Écrivons $a_j = b_j(x)x$ pour un certain $b_j(x) \in R[x]$.
En revenant à $\varphi$, nous voyons que
$\text{id}_M = -(\sum_{j = 1, \ldots, n} b_j(\varphi)) \varphi$,
et donc que $\varphi$ est inversible.
\end{proof}

\begin{proof}[Seconde démonstration]
Nous raisonnons par récurrence sur le nombre de générateurs de $M$ sur $R$. Si
$M$ est engendré par un élément, alors $M \cong R/I$ pour un certain idéal
$I \subset R$. Nous pouvons alors remplacer $R$ par $R/I$, de sorte que $M = R$.
Dans ce cas, $\varphi : R \to R$ est donné par la multiplication sur $M$ par un
élément $r \in R$. La surjectivité de $\varphi$ force $r$ à être inversible,
puisque $\varphi$ doit atteindre $1$ ; il s'ensuit que $\varphi$ est
inversible.

\medskip\noindent
Supposons maintenant le lemme démontré pour les modules
engendrés par $n - 1$ éléments, et considérons un module $M$ engendré
par $n$ éléments. Notons $A$ l'anneau $R[t]$ et regardons le module
$M$ comme un $A$-module en faisant agir $t$ par $\varphi$ ; comme $M$ est
de type fini sur $R$, il l'est aussi sur $R[t]$. Puisque nous cherchons
à démontrer que $\varphi$ est injectif, ce qui est une propriété ensembliste,
nous pouvons tout aussi bien démontrer que l'endomorphisme
$t : M \to M$ sur $A$ est injectif. Nous avons ramené le problème au cas
où notre endomorphisme est la multiplication par un élément de l'anneau de base.
Notons $M' \subset M$ le sous-$A$-module engendré par les $n - 1$ premiers
générateurs de $M$, et considérons le diagramme
$$
\xymatrix{
0 \ar[r] & M' \ar[r]\ar[d]^{\varphi\mid_{M'}} & M\ar[d]^\varphi \ar[r] &
M/M' \ar[d]^{\varphi \bmod M'} \ar[r] & 0 \\
0 \ar[r] & M' \ar[r]                                  & M \ar[r]
           & M/M' \ar[r]                                  & 0,
}
$$
où la restriction de $\varphi$ à $M'$ et l'application induite par $\varphi$
sur le quotient $M/M'$ sont bien définies, puisque $\varphi$ est la
multiplication par un élément de la base, et que $M'$ et $M/M'$ sont
eux-mêmes des $A$-modules. Par le cas $n = 1$, l'application
$M/M' \to M/M'$ est un isomorphisme. Une chasse au diagramme montre que
$\varphi|_{M'}$ est surjective ; par récurrence, $\varphi|_{M'}$ est donc
un isomorphisme. Le lemme du serpent impose alors à la colonne du milieu
d'être un isomorphisme.
\end{proof}
```

</details>

### 15 — section-spectrum-ring

Anglais L2964–2971 ; français L2921–2928.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2964) · `FR-ALGEBRA-B4-CHOICE-0015`.

La distinction éditoriale entre spectre comme espace topologique et schéma affine reste explicite. On ne rajoute pas de faisceau structural à cette section.

Règles : FR-ALGEBRA-B4-RULE-spectre.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{The spectrum of a ring}
\label{section-spectrum-ring}

\noindent
We arbitrarily decide that the spectrum of a ring as a topological space
is part of the algebra chapter, whereas an affine scheme is part of the
chapter on schemes.
```

Français conservé :
```tex
\section{Le spectre d'un anneau}
\label{section-spectrum-ring}

\noindent
Nous décidons arbitrairement que le spectre d'un anneau, considéré comme espace
topologique, relève du chapitre d'algèbre, tandis qu'un schéma affine relève du
chapitre sur les schémas.
```

</details>

### 16 — definition-spectrum-ring

Anglais L2972–2985 ; français L2929–2943.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2972) · `FR-ALGEBRA-B4-CHOICE-0016`.

Spectre est attesté chez Ducros 4.1.3 et Debarre III.5.1 comme ensemble de tous les idéaux premiers, pas seulement maximaux. V(T) contient les premiers contenant toute la partie T ; D(f) utilise la non-appartenance. Ensemble et partie gardent leur sens, avec exactement les mêmes quantificateurs.

Règles : FR-ALGEBRA-B4-RULE-ideaux, FR-ALGEBRA-B4-RULE-spectre.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-spectrum-ring}
Let $R$ be a ring.
\begin{enumerate}
\item The {\it spectrum} of $R$ is the set of prime ideals of $R$.
It is usually denoted $\Spec(R)$.
\item Given a subset $T \subset R$ we let $V(T) \subset \Spec(R)$
be the set of primes containing $T$, i.e., $V(T) = \{ \mathfrak p \in
\Spec(R) \mid \forall f\in T, f\in \mathfrak p\}$.
\item Given an element $f \in R$ we let $D(f) \subset \Spec(R)$
be the set of primes not containing $f$.
\end{enumerate}
\end{definition}
```

Français conservé :
```tex
\begin{definition}
\label{definition-spectrum-ring}
Soit $R$ un anneau.
\begin{enumerate}
\item Le {\it spectre} de $R$ est l'ensemble des idéaux premiers de $R$.
On le note habituellement $\Spec(R)$.
\item Étant donnée une partie $T \subset R$, nous notons
$V(T) \subset \Spec(R)$ l'ensemble des idéaux premiers contenant $T$,
c'est-à-dire $V(T) = \{ \mathfrak p \in
\Spec(R) \mid \forall f\in T, f\in \mathfrak p\}$.
\item Étant donné un élément $f \in R$, nous notons $D(f) \subset \Spec(R)$
l'ensemble des idéaux premiers ne contenant pas $f$.
\end{enumerate}
\end{definition}
```

</details>

### 17 — lemma-Zariski-topology

Anglais L2986–3110 ; français L2944–3082.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L2986) · `FR-ALGEBRA-B4-CHOICE-0017`.

Les dix-sept assertions et leurs dix-sept justifications ont été comparées une à une. Minimal au-dessus de I n'est pas remplacé par minimal absolu ; l'ordre opposé dans Zorn reste explicite. Idéal propre exclut R ; idéal unité vaut R. Radical, réunions et intersections gardent leur variance et leurs familles éventuellement infinies. Les relations f/f', a/f, I/J restent celles de chaque passage source. Famille rend un ensemble indexé sans ajouter d'hypothèse. La récurrence qualifiée boring devient immédiate : même étape logique, registre français moins familier. Le of anglais dans either I of J est rendu ou, faute grammaticale évidente sans nouvelle assertion. Les formules exactes, y compris la ponctuation dans les dollars et l'absence de traitement séparé des chaînes vides, ne sont pas retouchées.

Point particulier à relire : La lecture de fidélité ne certifie pas tous les détails omis dans l'argument de Zorn. La preuve anglaise, et non une version améliorée, gouverne le français.

Règles : FR-ALGEBRA-B4-RULE-ideaux, FR-ALGEBRA-B4-RULE-modules, FR-ALGEBRA-B4-RULE-polynomes, FR-ALGEBRA-B4-RULE-spectre, FR-ALGEBRA-B4-RULE-topologie, FR-ALGEBRA-B4-RULE-preuves.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Zariski-topology}
Let $R$ be a ring.
\begin{enumerate}
\item The spectrum of a ring $R$ is empty if and only if $R$
is the zero ring.
\item Every nonzero ring has a maximal ideal.
\item Every nonzero ring has a minimal prime ideal.
\item Given an ideal $I \subset R$ and a prime ideal
$I \subset \mathfrak p$ there exists a prime
$I \subset \mathfrak q \subset \mathfrak p$ such
that $\mathfrak q$ is minimal over $I$.
\item If $T \subset R$, and if $(T)$ is the ideal generated by
$T$ in $R$, then $V((T)) = V(T)$.
\item If $I$ is an ideal and $\sqrt{I}$ is its radical,
see basic notion (\ref{item-radical-ideal}), then $V(I) = V(\sqrt{I})$.
\item Given an ideal $I$ of $R$ we have $\sqrt{I} =
\bigcap_{I \subset \mathfrak p} \mathfrak p$.
\item If $I$ is an ideal then $V(I) = \emptyset$ if and only
if $I$ is the unit ideal.
\item If $I$, $J$ are ideals of $R$ then $V(I) \cup V(J) =
V(I \cap J)$.
\item If $(I_a)_{a\in A}$ is a set of ideals of $R$ then
$\bigcap_{a\in A} V(I_a) = V(\bigcup_{a\in A} I_a)$.
\item If $f \in R$, then $D(f) \amalg V(f) = \Spec(R)$.
\item If $f \in R$ then $D(f) = \emptyset$ if and only if $f$
is nilpotent.
\item If $f = u f'$ for some unit $u \in R$, then $D(f) = D(f')$.
\item If $I \subset R$ is an ideal, and $\mathfrak p$ is a prime of
$R$ with $\mathfrak p \not\in V(I)$, then there exists an $f \in R$
such that $\mathfrak p \in D(f)$, and $D(f) \cap V(I) = \emptyset$.
\item If $f, g \in R$, then $D(fg) = D(f) \cap D(g)$.
\item If $f_i \in R$ for $i \in I$, then
$\bigcup_{i\in I} D(f_i)$ is the complement of $V(\{f_i \}_{i\in I})$
in $\Spec(R)$.
\item If $f \in R$ and $D(f) = \Spec(R)$, then $f$ is a unit.
\end{enumerate}
\end{lemma}

\begin{proof}
We address each part in the corresponding item below.
\begin{enumerate}
\item This is a direct consequence of (2) or (3).
\item Let $\mathfrak{A}$ be the set of all proper ideals of $R$. This set is
ordered by inclusion and is non-empty, since $(0) \in \mathfrak{A}$ is a proper
ideal. Let $A$ be a totally ordered subset of $\mathfrak A$.
Then $\bigcup_{I \in A} I$ is in
fact an ideal. Since 1 $\notin I$ for all $I \in A$, the union does not contain
1 and thus is proper. Hence $\bigcup_{I \in A} I$ is in $\mathfrak{A}$ and is
an upper bound for the set $A$. Thus by Zorn's lemma $\mathfrak{A}$ has a
maximal element, which is the sought-after maximal ideal.
\item Since $R$ is nonzero, it contains a maximal ideal which is a prime ideal.
Thus the set $\mathfrak{A}$ of all prime ideals of $R$ is nonempty.
$\mathfrak{A}$ is ordered by reverse-inclusion. Let $A$ be a totally ordered
subset of $\mathfrak{A}$. It's pretty clear that $J = \bigcap_{I \in A} I$ is
in fact an ideal. Not so clear, however, is that it is prime. Let $xy \in J$.
Then $xy \in I$ for all $I \in A$. Now let $B = \{I \in A | y \in I\}$. Let $K
= \bigcap_{I \in B} I$. Since $A$ is totally ordered, either $K = J$ (and we're
done, since then $y \in J$) or $K \supset J$ and for all $I \in A$ such that
$I$ is properly contained in $K$, we have $y \notin I$. But that means that for
all those $I, x \in I$, since they are prime. Hence $x \in J$. In either case,
$J$ is prime as desired. Hence by Zorn's lemma we get a maximal element which
in this case is a minimal prime ideal.
\item This is the same exact argument as (3) except you only consider prime
ideals contained in $\mathfrak{p}$ and containing $I$.
\item $(T)$ is the smallest ideal containing $T$. Hence if $T \subset I$, some
ideal, then $(T) \subset I$ as well. Hence if $I \in V(T)$, then $I \in V((T))$
as well. The other inclusion is obvious.
\item Since $I \subset \sqrt{I}, V(\sqrt{I}) \subset V(I)$. Now let
$\mathfrak{p} \in V(I)$. Let $x \in \sqrt{I}$. Then $x^n \in I$ for some $n$.
Hence $x^n \in \mathfrak{p}$. But since $\mathfrak{p}$ is prime, a boring
induction argument gets you that $x \in \mathfrak{p}$. Hence $\sqrt{I} \subset
\mathfrak{p}$ and $\mathfrak{p} \in V(\sqrt{I})$.
\item Let $f \in R \setminus \sqrt{I}$. Then $f^n \notin I$ for all $n$. Hence
$S = \{1, f, f^2, \ldots\}$ is a multiplicative subset, not containing $0$.
Take a
prime ideal $\bar{\mathfrak{p}} \subset S^{-1}R$ containing $S^{-1}I$. Then the
pull-back $\mathfrak{p}$ in $R$ of $\bar{\mathfrak{p}}$ is a prime ideal
containing $I$ that does not intersect $S$. This shows that $\bigcap_{I \subset
\mathfrak p} \mathfrak p \subset \sqrt{I}$. Now if $a \in \sqrt{I}$, then $a^n
\in I$ for some $n$. Hence if $I \subset \mathfrak{p}$, then $a^n \in
\mathfrak{p}$. But since $\mathfrak{p}$ is prime, we have $a \in \mathfrak{p}$.
Thus the equality is shown.
\item $I$ is not the unit ideal if and only if $I$
is contained in some maximal ideal (to
see this, apply (2) to the ring $R/I$) which is therefore prime.
\item If $\mathfrak{p} \in V(I) \cup V(J)$, then $I \subset \mathfrak{p}$ or $J
\subset \mathfrak{p}$ which means that $I \cap J \subset \mathfrak{p}$. Now if
$I \cap J \subset \mathfrak{p}$, then $IJ \subset \mathfrak{p}$ and hence
either $I$ of $J$ is in $\mathfrak{p}$, since $\mathfrak{p}$ is prime.
\item $\mathfrak{p} \in \bigcap_{a \in A} V(I_a) \Leftrightarrow
I_a \subset \mathfrak{p}, \forall a \in A \Leftrightarrow
\mathfrak{p} \in V(\bigcup_{a\in A} I_a)$
\item If $\mathfrak{p}$ is a prime ideal and $f \in R$, then either $f \in
\mathfrak{p}$ or $f \notin \mathfrak{p}$ (strictly) which is what the disjoint
union says.
\item If $a \in R$ is nilpotent, then $a^n = 0$ for some $n$. Hence $a^n \in
\mathfrak{p}$ for any prime ideal. Thus $a \in \mathfrak{p}$ as can be shown by
induction and $D(a) = \emptyset$. Now, as shown in (7), if $a \in R$ is not
nilpotent, then there is a prime ideal that does not contain it.
\item $f \in \mathfrak{p} \Leftrightarrow uf \in \mathfrak{p}$, since $u$ is
invertible.
\item If $\mathfrak{p} \notin V(I)$, then $\exists f \in I \setminus
\mathfrak{p}$. Then $f \notin \mathfrak{p}$ so $\mathfrak{p} \in D(f)$. Also if
$\mathfrak{q} \in D(f)$, then $f \notin \mathfrak{q}$ and thus $I$ is not
contained in $\mathfrak{q}$. Thus $D(f) \cap V(I) = \emptyset$.
\item If $fg \in \mathfrak{p}$, then $f \in \mathfrak{p}$ or $g \in
\mathfrak{p}$. Hence if $f \notin \mathfrak{p}$ and $g \notin \mathfrak{p}$,
then $fg \notin \mathfrak{p}$. Since $\mathfrak{p}$ is an ideal, if $fg \notin
\mathfrak{p}$, then $f \notin \mathfrak{p}$ and $g \notin \mathfrak{p}$.
\item $\mathfrak{p} \in \bigcup_{i \in I} D(f_i) \Leftrightarrow \exists i \in
I, f_i \notin \mathfrak{p} \Leftrightarrow \mathfrak{p} \in \Spec(R)
\setminus V(\{f_i\}_{i \in I})$
\item If $D(f) = \Spec(R)$, then $V(f) = \emptyset$ and
hence $fR = R$, so $f$ is a unit.
\end{enumerate}
\end{proof}

\noindent
The lemma implies that the subsets $V(T)$ from
Definition \ref{definition-spectrum-ring} form the closed
subsets of a topology on $\Spec(R)$. And it also shows that
the sets $D(f)$ are open and form a basis for this
topology.
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-Zariski-topology}
Soit $R$ un anneau.
\begin{enumerate}
\item Le spectre d'un anneau $R$ est vide si et seulement si $R$
est l'anneau nul.
\item Tout anneau non nul possède un idéal maximal.
\item Tout anneau non nul possède un idéal premier minimal.
\item Étant donnés un idéal $I \subset R$ et un idéal premier vérifiant
$I \subset \mathfrak p$, il existe un idéal premier
$I \subset \mathfrak q \subset \mathfrak p$ tel que
$\mathfrak q$ soit minimal au-dessus de $I$.
\item Si $T \subset R$ et si $(T)$ est l'idéal engendré par
$T$ dans $R$, alors $V((T)) = V(T)$.
\item Si $I$ est un idéal et si $\sqrt{I}$ est son radical,
voir la notion de base (\ref{item-radical-ideal}), alors $V(I) = V(\sqrt{I})$.
\item Pour tout idéal $I$ de $R$, nous avons $\sqrt{I} =
\bigcap_{I \subset \mathfrak p} \mathfrak p$.
\item Si $I$ est un idéal, alors $V(I) = \emptyset$ si et seulement
si $I$ est l'idéal unité.
\item Si $I$ et $J$ sont des idéaux de $R$, alors $V(I) \cup V(J) =
V(I \cap J)$.
\item Si $(I_a)_{a\in A}$ est une famille d'idéaux de $R$, alors
$\bigcap_{a\in A} V(I_a) = V(\bigcup_{a\in A} I_a)$.
\item Si $f \in R$, alors $D(f) \amalg V(f) = \Spec(R)$.
\item Si $f \in R$, alors $D(f) = \emptyset$ si et seulement si $f$
est nilpotent.
\item Si $f = u f'$ pour une unité $u \in R$, alors $D(f) = D(f')$.
\item Si $I \subset R$ est un idéal et si $\mathfrak p$ est un idéal premier de
$R$ tel que $\mathfrak p \not\in V(I)$, alors il existe $f \in R$
tel que $\mathfrak p \in D(f)$ et $D(f) \cap V(I) = \emptyset$.
\item Si $f, g \in R$, alors $D(fg) = D(f) \cap D(g)$.
\item Si $f_i \in R$ pour $i \in I$, alors
$\bigcup_{i\in I} D(f_i)$ est le complémentaire de
$V(\{f_i \}_{i\in I})$ dans $\Spec(R)$.
\item Si $f \in R$ et $D(f) = \Spec(R)$, alors $f$ est une unité.
\end{enumerate}
\end{lemma}

\begin{proof}
Nous traitons chaque assertion dans l'item correspondant ci-dessous.
\begin{enumerate}
\item C'est une conséquence directe de (2) ou de (3).
\item Soit $\mathfrak{A}$ l'ensemble de tous les idéaux propres de $R$.
Cet ensemble est ordonné par inclusion et n'est pas vide, puisque
$(0) \in \mathfrak{A}$ est un idéal propre.
Soit $A$ une partie totalement ordonnée de $\mathfrak A$.
Alors $\bigcup_{I \in A} I$ est en fait un idéal. Comme 1 $\notin I$
pour tout $I \in A$, la réunion ne contient pas 1 et est donc propre.
Ainsi, $\bigcup_{I \in A} I$ appartient à $\mathfrak{A}$ et majore
la partie $A$. Le lemme de Zorn assure donc à $\mathfrak{A}$
l'existence d'un élément maximal, qui est l'idéal maximal recherché.
\item Puisque $R$ est non nul, il contient un idéal maximal, donc premier.
Ainsi, l'ensemble $\mathfrak{A}$ de tous les idéaux premiers de $R$
n'est pas vide. $\mathfrak{A}$ est ordonné par l'inclusion opposée.
Soit $A$ une partie totalement ordonnée de $\mathfrak{A}$. Il est clair que
$J = \bigcap_{I \in A} I$ est un idéal. Il est moins clair qu'il soit premier.
Soit $xy \in J$. Alors $xy \in I$ pour tout $I \in A$.
Posons $B = \{I \in A | y \in I\}$ et $K
= \bigcap_{I \in B} I$. Puisque $A$ est totalement ordonné, ou bien
$K = J$ (et nous avons conclu, car alors $y \in J$), ou bien $K \supset J$
et, pour tout $I \in A$ tel que $I$ soit strictement contenu dans $K$,
nous avons $y \notin I$. Mais cela signifie que, pour tous ces idéaux
$I, x \in I$, puisqu'ils sont premiers. Ainsi $x \in J$. Dans les deux cas,
$J$ est premier, comme voulu. Le lemme de Zorn fournit donc un élément
maximal, qui est ici un idéal premier minimal.
\item C'est exactement le même argument que dans (3), en ne considérant que
les idéaux premiers contenus dans $\mathfrak{p}$ et contenant $I$.
\item $(T)$ est le plus petit idéal contenant $T$. Par conséquent, si
$T \subset I$ pour un certain idéal, alors $(T) \subset I$ également.
Ainsi, si $I \in V(T)$, alors $I \in V((T))$ également.
L'autre inclusion est évidente.
\item Puisque $I \subset \sqrt{I}, V(\sqrt{I}) \subset V(I)$, prenons
$\mathfrak{p} \in V(I)$. Soit $x \in \sqrt{I}$. Alors $x^n \in I$
pour un certain $n$. Donc $x^n \in \mathfrak{p}$. Comme $\mathfrak{p}$
est premier, une récurrence immédiate donne $x \in \mathfrak{p}$.
Ainsi $\sqrt{I} \subset \mathfrak{p}$ et
$\mathfrak{p} \in V(\sqrt{I})$.
\item Soit $f \in R \setminus \sqrt{I}$. Alors $f^n \notin I$
pour tout $n$. Par conséquent,
$S = \{1, f, f^2, \ldots\}$ est une partie multiplicative ne contenant pas $0$.
Choisissons un idéal premier
$\bar{\mathfrak{p}} \subset S^{-1}R$ contenant $S^{-1}I$.
Alors $\mathfrak{p}$, image réciproque dans $R$ de $\bar{\mathfrak{p}}$,
est un idéal premier contenant $I$ et ne rencontrant pas $S$.
Cela montre que $\bigcap_{I \subset
\mathfrak p} \mathfrak p \subset \sqrt{I}$. Maintenant, si
$a \in \sqrt{I}$, alors $a^n \in I$ pour un certain $n$.
Ainsi, si $I \subset \mathfrak{p}$, alors $a^n \in
\mathfrak{p}$. Comme $\mathfrak{p}$ est premier, nous avons
$a \in \mathfrak{p}$. L'égalité est donc démontrée.
\item $I$ n'est pas l'idéal unité si et seulement si $I$
est contenu dans un idéal maximal (pour le voir, appliquer (2) à l'anneau
$R/I$), lequel est donc premier.
\item Si $\mathfrak{p} \in V(I) \cup V(J)$, alors $I \subset \mathfrak{p}$
ou $J \subset \mathfrak{p}$, ce qui signifie que
$I \cap J \subset \mathfrak{p}$. Réciproquement, si
$I \cap J \subset \mathfrak{p}$, alors $IJ \subset \mathfrak{p}$ ;
ainsi, soit $I$, soit $J$, est contenu dans $\mathfrak{p}$,
puisque $\mathfrak{p}$ est premier.
\item $\mathfrak{p} \in \bigcap_{a \in A} V(I_a) \Leftrightarrow
I_a \subset \mathfrak{p}, \forall a \in A \Leftrightarrow
\mathfrak{p} \in V(\bigcup_{a\in A} I_a)$
\item Si $\mathfrak{p}$ est un idéal premier et $f \in R$, alors ou bien
$f \in \mathfrak{p}$, ou bien $f \notin \mathfrak{p}$, de façon exclusive ;
c'est précisément ce qu'exprime la réunion disjointe.
\item Si $a \in R$ est nilpotent, alors $a^n = 0$ pour un certain $n$.
Ainsi $a^n \in \mathfrak{p}$ pour tout idéal premier. Une récurrence donne
donc $a \in \mathfrak{p}$ et $D(a) = \emptyset$. Réciproquement, comme
nous l'avons montré en (7), si $a \in R$ n'est pas nilpotent, il existe
un idéal premier qui ne le contient pas.
\item $f \in \mathfrak{p} \Leftrightarrow uf \in \mathfrak{p}$,
puisque $u$ est inversible.
\item Si $\mathfrak{p} \notin V(I)$, alors
$\exists f \in I \setminus \mathfrak{p}$. Ainsi
$f \notin \mathfrak{p}$, donc $\mathfrak{p} \in D(f)$. En outre, si
$\mathfrak{q} \in D(f)$, alors $f \notin \mathfrak{q}$, si bien que $I$
n'est pas contenu dans $\mathfrak{q}$. Ainsi
$D(f) \cap V(I) = \emptyset$.
\item Si $fg \in \mathfrak{p}$, alors $f \in \mathfrak{p}$ ou
$g \in \mathfrak{p}$. Par conséquent, si $f \notin \mathfrak{p}$ et
$g \notin \mathfrak{p}$, alors $fg \notin \mathfrak{p}$.
Puisque $\mathfrak{p}$ est un idéal, si $fg \notin
\mathfrak{p}$, alors $f \notin \mathfrak{p}$ et $g \notin \mathfrak{p}$.
\item $\mathfrak{p} \in \bigcup_{i \in I} D(f_i) \Leftrightarrow \exists i \in
I, f_i \notin \mathfrak{p} \Leftrightarrow \mathfrak{p} \in \Spec(R)
\setminus V(\{f_i\}_{i \in I})$
\item Si $D(f) = \Spec(R)$, alors $V(f) = \emptyset$ et donc
$fR = R$, de sorte que $f$ est une unité.
\end{enumerate}
\end{proof}

\noindent
Le lemme entraîne que les parties $V(T)$ de la
définition \ref{definition-spectrum-ring} sont les fermés
d'une topologie sur $\Spec(R)$. Il montre aussi que
les ensembles $D(f)$ sont ouverts et forment une base de cette
topologie.
```

</details>

### 18 — definition-Zariski-topology

Anglais L3111–3122 ; français L3083–3094.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3111) · `FR-ALGEBRA-B4-CHOICE-0018`.

Topologie de Zariski désigne exactement les fermés V(T). Ouverts principaux, pour standard opens, est attesté à définition identique dans Dat 1.2.4 ; ouvert standard serait une variante plus littérale, non une notion différente. Cela ne dit pas que chaque ouvert affine est principal. La phrase sur le rôle du contexte reste présente.

Règles : FR-ALGEBRA-B4-RULE-spectre.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-Zariski-topology}
Let $R$ be a ring.
The topology on $\Spec(R)$ whose closed sets are the
sets $V(T)$ is called the {\it Zariski} topology. The open
subsets $D(f)$ are called the {\it standard opens} of $\Spec(R)$.
\end{definition}

\noindent
It should be clear from context whether we consider $\Spec(R)$
just as a set or as a topological space.
```

Français conservé :
```tex
\begin{definition}
\label{definition-Zariski-topology}
Soit $R$ un anneau.
La topologie sur $\Spec(R)$ dont les fermés sont les
ensembles $V(T)$ est appelée topologie {\it de Zariski}. Les ouverts
$D(f)$ sont appelés les {\it ouverts principaux} de $\Spec(R)$.
\end{definition}

\noindent
Le contexte indiquera clairement si nous considérons $\Spec(R)$
seulement comme un ensemble ou comme un espace topologique.
```

</details>

### 19 — lemma-spec-functorial

Anglais L3123–3161 ; français L3095–3133.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3123) · `FR-ALGEBRA-B4-CHOICE-0019`.

Fonctorialité et foncteur contravariant sont attestés chez Ducros 4.1.22. Le morphisme d'anneaux et la flèche entre spectres ont des sens opposés ; image réciproque ne devient pas image directe. La composition et les deux niveaux de Spec restent dans le même ordre. La preuve utilise toujours le même renvoi et la même égalité sur D(f).

Règles : FR-ALGEBRA-B4-RULE-ideaux, FR-ALGEBRA-B4-RULE-spectre, FR-ALGEBRA-B4-RULE-topologie.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-spec-functorial}
\begin{slogan}
Functoriality of the spectrum
\end{slogan}
Suppose that $\varphi : R \to R'$ is a ring homomorphism.
The induced map
$$
\Spec(\varphi) : \Spec(R') \longrightarrow \Spec(R),
\quad
\mathfrak p' \longmapsto \varphi^{-1}(\mathfrak p')
$$
is continuous for the Zariski topologies. In fact, for any
element $f \in R$ we have
$\Spec(\varphi)^{-1}(D(f)) = D(\varphi(f))$.
\end{lemma}

\begin{proof}
It is basic notion (\ref{item-inverse-image-prime}) that
$\mathfrak p := \varphi^{-1}(\mathfrak p')$
is indeed a prime ideal of $R$. The last assertion
of the lemma follows directly from the definitions,
and implies the first.
\end{proof}

\noindent
If $\varphi' : R' \to R''$ is a second ring homomorphism
then the composition
$$
\Spec(R'')
\longrightarrow
\Spec(R')
\longrightarrow
\Spec(R)
$$
equals $\Spec(\varphi' \circ \varphi)$. In other
words, $\Spec$ is a contravariant functor from the
category of rings to the category of topological spaces.
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-spec-functorial}
\begin{slogan}
Fonctorialité du spectre
\end{slogan}
Supposons que $\varphi : R \to R'$ soit un morphisme d'anneaux.
L'application induite
$$
\Spec(\varphi) : \Spec(R') \longrightarrow \Spec(R),
\quad
\mathfrak p' \longmapsto \varphi^{-1}(\mathfrak p')
$$
est continue pour les topologies de Zariski. En fait, pour tout
élément $f \in R$, nous avons
$\Spec(\varphi)^{-1}(D(f)) = D(\varphi(f))$.
\end{lemma}

\begin{proof}
La notion de base (\ref{item-inverse-image-prime}) assure que
$\mathfrak p := \varphi^{-1}(\mathfrak p')$
est bien un idéal premier de $R$. La dernière assertion
du lemme résulte directement des définitions
et entraîne la première.
\end{proof}

\noindent
Si $\varphi' : R' \to R''$ est un second morphisme d'anneaux,
alors la composée
$$
\Spec(R'')
\longrightarrow
\Spec(R')
\longrightarrow
\Spec(R)
$$
est égale à $\Spec(\varphi' \circ \varphi)$. Autrement dit,
$\Spec$ est un foncteur contravariant de la catégorie des anneaux
vers la catégorie des espaces topologiques.
```

</details>

### 20 — lemma-spec-localization

Anglais L3162–3205 ; français L3134–3178.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3162) · `FR-ALGEBRA-B4-CHOICE-0020`.

Homéomorphisme signifie bijection continue à inverse continu, non seule bijection. La topologie induite sur les premiers évitant S est explicitement conservée. L'image n'est pas dite ouverte dans tout Spec(R) : la conclusion application ouverte concerne le but D muni de sa topologie, contrairement au cas particulier d'une seule localisation. Les preuves de primalité, injectivité et ouverture sont intactes. Le rôle de g et h/1 différant multiplicativement par une unité est explicité sans formule nouvelle ; Ducros 4.1.25 et Dat 1.2.5 confirment ce registre.

Règles : FR-ALGEBRA-B4-RULE-ideaux, FR-ALGEBRA-B4-RULE-polynomes, FR-ALGEBRA-B4-RULE-spectre, FR-ALGEBRA-B4-RULE-topologie.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-spec-localization}
Let $R$ be a ring. Let $S \subset R$ be a multiplicative subset.
The map $R \to S^{-1}R$ induces via the functoriality of $\Spec$
a homeomorphism
$$
\Spec(S^{-1}R)
\longrightarrow
\{\mathfrak p \in \Spec(R) \mid S \cap \mathfrak p = \emptyset \}
$$
where the topology on the right hand side is that induced from the
Zariski topology on $\Spec(R)$. The inverse map is given
by $\mathfrak p \mapsto S^{-1}\mathfrak p = \mathfrak p(S^{-1}R)$.
\end{lemma}

\begin{proof}
Denote the right hand side of the arrow of the lemma by $D$.
Choose a prime $\mathfrak p' \subset S^{-1}R$ and let $\mathfrak p$
the inverse image of $\mathfrak p'$ in $R$. Since $\mathfrak p'$
does not contain $1$ we see that $\mathfrak p$ does not contain
any element of $S$. Hence $\mathfrak p \in D$ and we see that
the image is contained in $D$. Let $\mathfrak p \in D$.
By assumption the image $\overline{S}$ does not contain $0$.
By basic notion (\ref{item-localization-zero})
$\overline{S}^{-1}(R/\mathfrak p)$ is not the zero ring.
By basic notion (\ref{item-localize-ideal}) we see
$S^{-1}R / S^{-1}\mathfrak p = \overline{S}^{-1}(R/\mathfrak p)$
is a domain, and hence $S^{-1}\mathfrak p$ is a prime.
The equality of rings also shows that the inverse image of
$S^{-1}\mathfrak p$ in $R$ is equal to $\mathfrak p$,
because $R/\mathfrak p \to \overline{S}^{-1}(R/\mathfrak p)$
is injective by basic notion (\ref{item-localize-nonzerodivisors}).
This proves that the map $\Spec(S^{-1}R) \to \Spec(R)$
is bijective onto $D$ with inverse as given.
It is continuous by Lemma \ref{lemma-spec-functorial}.
Finally, let $D(g) \subset \Spec(S^{-1}R)$ be a standard
open. Write $g = h/s$ for some $h\in R$ and $s\in S$.
Since $g$ and $h/1$ differ by a unit we have $D(g) =
D(h/1)$ in $\Spec(S^{-1}R)$.
Hence by Lemma \ref{lemma-spec-functorial} and the bijectivity
above the image of $D(g) = D(h/1)$ is $D \cap D(h)$.
This proves the map is open as well.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-spec-localization}
Soit $R$ un anneau. Soit $S \subset R$ une partie multiplicative.
Le morphisme $R \to S^{-1}R$ induit, par fonctorialité de $\Spec$,
un homéomorphisme
$$
\Spec(S^{-1}R)
\longrightarrow
\{\mathfrak p \in \Spec(R) \mid S \cap \mathfrak p = \emptyset \}
$$
où le membre de droite est muni de la topologie induite par la
topologie de Zariski sur $\Spec(R)$. L'application inverse est donnée
par $\mathfrak p \mapsto S^{-1}\mathfrak p = \mathfrak p(S^{-1}R)$.
\end{lemma}

\begin{proof}
Notons $D$ le membre de droite de la flèche du lemme.
Choisissons un idéal premier $\mathfrak p' \subset S^{-1}R$ et soit
$\mathfrak p$ l'image réciproque de $\mathfrak p'$ dans $R$.
Puisque $\mathfrak p'$ ne contient pas $1$, nous voyons que $\mathfrak p$
ne contient aucun élément de $S$. Ainsi $\mathfrak p \in D$, et nous voyons que
l'image est contenue dans $D$. Soit $\mathfrak p \in D$.
Par hypothèse, l'image $\overline{S}$ ne contient pas $0$.
D'après la notion de base (\ref{item-localization-zero}),
$\overline{S}^{-1}(R/\mathfrak p)$ n'est pas l'anneau nul.
D'après la notion de base (\ref{item-localize-ideal}), nous voyons que
$S^{-1}R / S^{-1}\mathfrak p = \overline{S}^{-1}(R/\mathfrak p)$
est un anneau intègre, et donc que $S^{-1}\mathfrak p$ est premier.
L'égalité d'anneaux montre aussi que l'image réciproque de
$S^{-1}\mathfrak p$ dans $R$ est égale à $\mathfrak p$,
car $R/\mathfrak p \to \overline{S}^{-1}(R/\mathfrak p)$
est injective d'après la notion de base
(\ref{item-localize-nonzerodivisors}).
Cela démontre que l'application $\Spec(S^{-1}R) \to \Spec(R)$
est une bijection sur $D$, dont l'inverse est celui indiqué.
Elle est continue d'après le lemme \ref{lemma-spec-functorial}.
Enfin, soit $D(g) \subset \Spec(S^{-1}R)$ un ouvert principal.
Écrivons $g = h/s$ pour certains $h\in R$ et $s\in S$.
Puisque $g$ s'obtient à partir de $h/1$ par multiplication par une unité, nous avons
$D(g) = D(h/1)$ dans $\Spec(S^{-1}R)$.
Le lemme \ref{lemma-spec-functorial} et la bijectivité ci-dessus montrent donc
que l'image de $D(g) = D(h/1)$ est $D \cap D(h)$.
Cela prouve que l'application est également ouverte.
\end{proof}
```

</details>

### 21 — lemma-standard-open

Anglais L3206–3225 ; français L3179–3199.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3206) · `FR-ALGEBRA-B4-CHOICE-0021`.

Ouvert principal traduit l'objet D(f) défini plus haut, attesté par Dat 1.2.4. L'homéomorphisme conserve son inverse p R_f. Aucune condition f non nilpotent n'est importée de la formulation plus restreinte de Dat. La mise en garde qui suit nie que tous les ouverts affines soient principaux, sans dire qu'aucun ne l'est.

Règles : FR-ALGEBRA-B4-RULE-spectre, FR-ALGEBRA-B4-RULE-topologie.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-standard-open}
Let $R$ be a ring. Let $f \in R$.
The map $R \to R_f$ induces via the functoriality of
$\Spec$ a homeomorphism
$$
\Spec(R_f) \longrightarrow D(f) \subset \Spec(R).
$$
The inverse is given by $\mathfrak p \mapsto \mathfrak p \cdot R_f$.
\end{lemma}

\begin{proof}
This is a special case of Lemma \ref{lemma-spec-localization}.
\end{proof}

\noindent
It is not the case that every ``affine open'' of a
spectrum is a standard open. See
Example \ref{example-affine-open-not-standard}.
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-standard-open}
Soit $R$ un anneau. Soit $f \in R$.
Le morphisme $R \to R_f$ induit, par fonctorialité de
$\Spec$, un homéomorphisme
$$
\Spec(R_f) \longrightarrow D(f) \subset \Spec(R).
$$
L'application inverse est donnée par
$\mathfrak p \mapsto \mathfrak p \cdot R_f$.
\end{lemma}

\begin{proof}
C'est un cas particulier du lemme \ref{lemma-spec-localization}.
\end{proof}

\noindent
Tout « ouvert affine » d'un spectre n'est pas nécessairement
un ouvert principal. Voir l'exemple
\ref{example-affine-open-not-standard}.
```

</details>

### 22 — lemma-spec-closed

Anglais L3226–3250 ; français L3200–3225.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3226) · `FR-ALGEBRA-B4-CHOICE-0022`.

Le quotient et le fermé V(I) gardent leur homeomorphisme et l'inverse p/I. Anneau intègre rend domain, pas corps ; le morphisme quotient n'est pas rendu injectif. La preuve utilise les mêmes ouverts images et le même théorème d'isomorphisme, sans ajouter les corps résiduels discutés dans le canon.

Règles : FR-ALGEBRA-B4-RULE-ideaux, FR-ALGEBRA-B4-RULE-topologie.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-spec-closed}
Let $R$ be a ring. Let $I \subset R$ be an ideal.
The map $R \to R/I$ induces via the functoriality of
$\Spec$ a homeomorphism
$$
\Spec(R/I) \longrightarrow V(I) \subset \Spec(R).
$$
The inverse is given by $\mathfrak p \mapsto \mathfrak p / I$.
\end{lemma}

\begin{proof}
It is immediate that the image is contained in $V(I)$.
On the other hand, if $\mathfrak p \in V(I)$
then $\mathfrak p \supset I$ and we may consider
the ideal $\mathfrak p /I \subset R/I$. Using
basic notion (\ref{item-isomorphism-theorem}) we see that
$(R/I)/(\mathfrak p/I) = R/\mathfrak p$ is a domain
and hence $\mathfrak p/I$ is a prime ideal. From this
it is immediately clear that the image of $D(f + I)$
is $D(f) \cap V(I)$, and hence the map is a homeomorphism.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-spec-closed}
Soit $R$ un anneau. Soit $I \subset R$ un idéal.
Le morphisme $R \to R/I$ induit, par fonctorialité de
$\Spec$, un homéomorphisme
$$
\Spec(R/I) \longrightarrow V(I) \subset \Spec(R).
$$
L'application inverse est donnée par
$\mathfrak p \mapsto \mathfrak p / I$.
\end{lemma}

\begin{proof}
Il est immédiat que l'image est contenue dans $V(I)$.
D'autre part, si $\mathfrak p \in V(I)$, alors
$\mathfrak p \supset I$, et nous pouvons considérer
l'idéal $\mathfrak p /I \subset R/I$. La notion de base
(\ref{item-isomorphism-theorem}) montre que
$(R/I)/(\mathfrak p/I) = R/\mathfrak p$ est un anneau intègre,
et donc que $\mathfrak p/I$ est un idéal premier. Il est alors
immédiat que l'image de $D(f + I)$ est
$D(f) \cap V(I)$, et donc que l'application est un homéomorphisme.
\end{proof}
```

</details>

### 23 — lemma-quasi-compact

Anglais L3251–3274 ; français L3226–3249.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3251) · `FR-ALGEBRA-B4-CHOICE-0023`.

Quasi-compact est attesté chez Ducros 4.1.10–12 et Dat 1.2.4 sans séparation requise. Extraire un recouvrement fini rend ici le raffinement fini annoncé par l'anglais : la preuve produit explicitement une sous-famille J des ouverts donnés. La somme finie de 1, l'idéal unité et toutes les étapes sont conservés. On n'écrit pas compact, qui pourrait importer la séparation.

Règles : FR-ALGEBRA-B4-RULE-ideaux, FR-ALGEBRA-B4-RULE-spectre, FR-ALGEBRA-B4-RULE-topologie.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-quasi-compact}
\begin{slogan}
The spectrum of a ring is quasi-compact
\end{slogan}
Let $R$ be a ring. The space $\Spec(R)$ is quasi-compact.
\end{lemma}

\begin{proof}
It suffices to prove that any covering of $\Spec(R)$
by standard opens can be refined by a finite covering.
Thus suppose that $\Spec(R) = \cup D(f_i)$
for a set of elements $\{f_i\}_{i\in I}$ of $R$. This means that
$\cap V(f_i) = \emptyset$. According to Lemma
\ref{lemma-Zariski-topology} this means that
$V(\{f_i \}) = \emptyset$. According to the
same lemma this means that the ideal generated
by the $f_i$ is the unit ideal of $R$. This means
that we can write $1$ as a {\it finite} sum:
$1 = \sum_{i \in J} r_i f_i$ with $J \subset I$ finite.
And then it follows that $\Spec(R)
= \cup_{i \in J} D(f_i)$.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-quasi-compact}
\begin{slogan}
Le spectre d'un anneau est quasi-compact
\end{slogan}
Soit $R$ un anneau. L'espace $\Spec(R)$ est quasi-compact.
\end{lemma}

\begin{proof}
Il suffit de démontrer que de tout recouvrement de $\Spec(R)$
par des ouverts principaux on peut extraire un recouvrement fini.
Supposons donc que $\Spec(R) = \cup D(f_i)$
pour une famille d'éléments $\{f_i\}_{i\in I}$ de $R$. Cela signifie que
$\cap V(f_i) = \emptyset$. D'après le lemme
\ref{lemma-Zariski-topology}, cela signifie que
$V(\{f_i \}) = \emptyset$. D'après le
même lemme, cela signifie que l'idéal engendré
par les $f_i$ est l'idéal unité de $R$. Nous pouvons donc
écrire $1$ comme une somme {\it finie} :
$1 = \sum_{i \in J} r_i f_i$ avec $J \subset I$ fini.
Il s'ensuit alors que $\Spec(R)
= \cup_{i \in J} D(f_i)$.
\end{proof}
```

</details>

### 24 — lemma-topology-spec

Anglais L3275–3304 ; français L3250–3274.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3275) · `FR-ALGEBRA-B4-CHOICE-0024`.

Les trois propriétés topologiques restent distinctes. Une base formée d'ouverts quasi-compacts ne signifie pas que tous les ouverts le sont. L'intersection de deux ouverts quasi-compacts est ramenée aux unions finies écrites, sans hypothèse de séparation. Première assertion renvoie au constat initial de la preuve que le spectre est quasi-compact, correspondant à first remark ; ce n'est pas la substitution d'un résultat cité. Les facteurs f_i g_j restent exacts.

Règles : FR-ALGEBRA-B4-RULE-spectre.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-topology-spec}
Let $R$ be a ring.
The topology on $X = \Spec(R)$ has the following properties:
\begin{enumerate}
\item $X$ is quasi-compact,
\item $X$ has a basis for the topology consisting of quasi-compact opens, and
\item the intersection of any two quasi-compact opens is quasi-compact.
\end{enumerate}
\end{lemma}

\begin{proof}
The spectrum of a ring is quasi-compact, see
Lemma \ref{lemma-quasi-compact}.
It has a basis for the topology consisting of the standard opens
$D(f) = \Spec(R_f)$
(Lemma \ref{lemma-standard-open})
which are quasi-compact by the first remark.
The intersection of two standard opens is quasi-compact
as $D(f) \cap D(g) = D(fg)$. Given any two quasi-compact opens
$U, V \subset X$ we may write $U = D(f_1) \cup \ldots \cup D(f_n)$
and $V = D(g_1) \cup \ldots \cup D(g_m)$. Then
$U \cap V = \bigcup D(f_ig_j)$ which is quasi-compact.
\end{proof}
```

Français conservé :
```tex
\begin{lemma}
\label{lemma-topology-spec}
Soit $R$ un anneau.
La topologie sur $X = \Spec(R)$ possède les propriétés suivantes :
\begin{enumerate}
\item $X$ est quasi-compact,
\item $X$ possède une base de la topologie formée d'ouverts quasi-compacts, et
\item l'intersection de deux ouverts quasi-compacts quelconques est quasi-compacte.
\end{enumerate}
\end{lemma}

\begin{proof}
Le spectre d'un anneau est quasi-compact ; voir le
lemme \ref{lemma-quasi-compact}.
Il possède une base de la topologie formée des ouverts principaux
$D(f) = \Spec(R_f)$
(lemme \ref{lemma-standard-open}),
qui sont quasi-compacts d'après la première assertion.
L'intersection de deux ouverts principaux est quasi-compacte,
car $D(f) \cap D(g) = D(fg)$. Étant donnés deux ouverts quasi-compacts
$U, V \subset X$, nous pouvons écrire $U = D(f_1) \cup \ldots \cup D(f_n)$
et $V = D(g_1) \cup \ldots \cup D(g_m)$. Alors
$U \cap V = \bigcup D(f_ig_j)$, qui est quasi-compact.
\end{proof}
```

</details>

## Contrôles exacts

Les 639 régions mathématiques de ce lot concordent sans exception de texte lecteur ni masque général, après la normalisation d’espaces et de commentaires du vérificateur. Les 2 326 régions du préfixe cumulatif passent avec les huit seules exceptions linguistiques déjà enregistrées aux lots 2 et 3.

Labels, références, citations, commandes invariantes, environnements, contrôles TeX et items concordent. Le fichier cible entier est inchangé. Le retour inverse des opérations antérieures reproduit tous les octets du témoin public. Les 116 intervalles successifs couvrent tout le préfixe sans lacune ni chevauchement.

Prochaine lecture : Anneaux locaux, source L3305 / français L3275. Aucun nouveau PDF, aucune publication, aucune approbation humaine et aucune certification du chapitre entier ne sont revendiqués.

