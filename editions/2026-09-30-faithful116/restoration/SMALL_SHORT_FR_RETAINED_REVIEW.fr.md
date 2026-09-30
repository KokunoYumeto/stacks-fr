# Cinq chapitres — vérification délimitée des formules

**91 paires de texte dans les formules ont été lues. Ce contrôle n’est pas une relecture complète de la prose.**

[Réparations des chapitres 22 et 92](SMALL_FR_REVIEW.fr.md) · [Autres restaurations](SHORT_FR_REVIEW.fr.md) · [Contrôles](SMALL_SHORT_FR_CANDIDATE_RECONCILIATION.json)

| Chapitre | Blocs comparés | Variantes de formule conservées | Paires de texte lues |
|---|---:|---:|---:|
| 22 — dga | 195 | 0 | 26 |
| 92 — cotangent | 150 | 0 | 10 |
| 65 — spaces | 86 | 1 | 21 |
| 112 — guide | 22 | 0 | 0 |
| 111 — exercises | 517 | 1 | 34 |

Deux différences de structure restent explicitement conservées : la mise en lignes du tableau de catégories au chapitre 65 et la traduction du connecteur ou au chapitre 111. Le tableau entier a été lu. Les noms de catégories et les autres textes masqués ne sont pas acceptés par simple égalité automatique ; les motifs individuels suivent.

## Variante conservée — spaces / `lemma-category-of-spaces-over-smaller-base-scheme`

Le tableau a été lu intégralement et avec sa preuve : les espaces sur S correspondent aux mêmes couples F prime sur S prime munis du même morphisme vers S. Le retour à la ligne et l’environnement gathered ne changent pas l’équivalence. Les fragments français doivent être lus ensemble, non comparés mot à mot.

```tex
\left\{ \begin{matrix} \text{category of algebraic}\\ \text{spaces over }S \end{matrix} \right\} \leftrightarrow \left\{ \begin{matrix} \text{category of pairs }(F', F' \to S)\text{ consisting}\\ \text{of an algebraic space }F'\text{ over }S'\text{ and a}\\ \text{morphism }F' \to S\text{ of algebraic spaces over }S' \end{matrix} \right\}
```
```tex
\begin{gathered} \left\{ \begin{matrix} \text{catégorie des espaces}\\ \text{algébriques sur }S \end{matrix} \right\}\\[4pt] \leftrightarrow\\[4pt] \left\{ \begin{matrix} \text{catégorie des couples }(F', F' \to S)\text{ formés}\\ \text{d'un espace algébrique }F'\text{ sur }S'\\ \text{et d'un morphisme }F' \to S\text{ d'espaces algébriques}\\ \text{sur }S' \end{matrix} \right\} \end{gathered}
```

## Variante conservée — exercises / `exercise-valuation`

Le mot ou conserve la disjonction, la valeur zéro et l’inégalité stricte. Les hypothèses de l’exercice et ses cinq questions restent inchangées. Le changement de la définition voisine de l’idempotent non trivial est traité distinctement comme restauration.

```tex
\{f \mid f = 0, \ or\ \nu(f) > 0\}
```
```tex
\{f \mid f = 0, \ \text{ou}\ \nu(f) > 0\}
```

## FR-DGA-MATH-TEXT-001 — `lemma-nilpotent`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L624)

Et conserve les deux diagrammes composables et ne modifie aucune flèche.

```tex
\vcenter{ \xymatrix{ K_1 \ar[d]_0 \ar[r] & L_1 \ar[r] \ar[d]_b & M_1 \ar[d]_0 \\ K_2 \ar[r] & L_2 \ar[r] & M_2 } } \quad\text{and}\quad \vcenter{ \xymatrix{ K_2 \ar[d]^0 \ar[r] & L_2 \ar[r] \ar[d]^{b'} & M_2 \ar[d]^0 \\ K_3 \ar[r] & L_3 \ar[r] & M_3 } }
```
```tex
\vcenter{ \xymatrix{ K_1 \ar[d]_0 \ar[r] & L_1 \ar[r] \ar[d]_b & M_1 \ar[d]_0 \\ K_2 \ar[r] & L_2 \ar[r] & M_2 } } \quad\text{et}\quad \vcenter{ \xymatrix{ K_2 \ar[d]^0 \ar[r] & L_2 \ar[r] \ar[d]^{b'} & M_2 \ar[d]^0 \\ K_3 \ar[r] & L_3 \ar[r] & M_3 } }
```

## FR-DGA-MATH-TEXT-002 — `lemma-rotate-triangle`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L762)

Et relie les deux mêmes triangles, avec leurs degrés et morphismes.

```tex
(M[-1], K, L, \delta[-1], \alpha, \beta) \quad\text{and}\quad (M[-1], K, C(\delta[-1]), \delta[-1], i, p)
```
```tex
(M[-1], K, L, \delta[-1], \alpha, \beta) \quad\text{et}\quad (M[-1], K, C(\delta[-1]), \delta[-1], i, p)
```

## FR-DGA-MATH-TEXT-003 — `definition-opposite-dga`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L1187)

Le diagramme entier conserve les multiplications de A opposée et de A et la même contrainte de commutativité.

```tex
\xymatrix{ \text{Tot}(A^\bullet \otimes_R A^\bullet) \ar[rrr]_-{\text{multiplication of }A^{opp}} \ar[d]_{\text{commutativity constraint}} & & & A^\bullet \ar[d]^{\text{id}} \\ \text{Tot}(A^\bullet \otimes_R A^\bullet) \ar[rrr]^-{\text{multiplication of }A} & & & A^\bullet }
```
```tex
\xymatrix{ \text{Tot}(A^\bullet \otimes_R A^\bullet) \ar[rrr]_-{\text{multiplication de }A^{opp}} \ar[d]_{\text{contrainte de commutativité}} & & & A^\bullet \ar[d]^{\text{id}} \\ \text{Tot}(A^\bullet \otimes_R A^\bullet) \ar[rrr]^-{\text{multiplication de }A} & & & A^\bullet }
```

## FR-DGA-MATH-TEXT-004 — `definition-opposite-dga`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L1187)

Même lecture pour l’action sur M opposé et sur M ; aucun côté du module n’est interverti.

```tex
\xymatrix{ \text{Tot}(M^\bullet \otimes_R A^\bullet) \ar[rrr]_-{\text{multiplication on }M^{opp}} \ar[d]_{\text{commutativity constraint}} & & & M^\bullet \ar[d]^{\text{id}} \\ \text{Tot}(A^\bullet \otimes_R M^\bullet) \ar[rrr]^-{\text{multiplication on }M} & & & M^\bullet }
```
```tex
\xymatrix{ \text{Tot}(M^\bullet \otimes_R A^\bullet) \ar[rrr]_-{\text{multiplication sur }M^{opp}} \ar[d]_{\text{contrainte de commutativité}} & & & M^\bullet \ar[d]^{\text{id}} \\ \text{Tot}(A^\bullet \otimes_R M^\bullet) \ar[rrr]^-{\text{multiplication sur }M} & & & M^\bullet }
```

## FR-DGA-MATH-TEXT-005 — `section-tensor-product`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L1389)

R-modules gradués est la même catégorie que graded R-modules ; GradedBilinear reste un nom de notation anglais.

```tex
\text{GradedBilinear}_A(M \times N, Q) = \Hom_{\text{graded }R\text{-modules}}(M \otimes_A N, Q)
```
```tex
\text{GradedBilinear}_A(M \times N, Q) = \Hom_{\text{}R\text{-modules gradués}}(M \otimes_A N, Q)
```

## FR-DGA-MATH-TEXT-006 — `lemma-characterize-hom-other-side`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L1668)

A-modules différentiels gradués à gauche préserve à la fois la différentielle, la graduation et le côté gauche.

```tex
\Hom_{\text{left diff graded }A\text{-modules}}(M', \Hom(M, N^\bullet)) = \Hom_{\text{Comp}(R)}(M \otimes_A M', N^\bullet)
```
```tex
\Hom_{\text{}A\text{-modules différentiels gradués à gauche}}(M', \Hom(M, N^\bullet)) = \Hom_{\text{Comp}(R)}(M \otimes_A M', N^\bullet)
```

## FR-DGA-MATH-TEXT-007 — `section-modules-noncommutative-graded`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L1988)

Application d’évaluation désigne la même flèche ; le signe (-1)^n reste exact.

```tex
ev : M \longrightarrow (M^\vee)^\vee, \quad ev^n = (-1)^n \text{ the evaluation map }M^n \to ((M^n)^\vee)^\vee
```
```tex
ev : M \longrightarrow (M^\vee)^\vee, \quad ev^n = (-1)^n \text{ l'application d'évaluation }M^n \to ((M^n)^\vee)^\vee
```

## FR-DGA-MATH-TEXT-008 — `lemma-construction`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L3412)

Et relie les deux functorialités, sur complexes et sur homotopie.

```tex
\text{Comp}(\mathcal{A}) \to \text{Mod}_{(A, \text{d})} \quad\text{and}\quad K(\mathcal{A}) \to K(\text{Mod}_{(A, \text{d})})
```
```tex
\text{Comp}(\mathcal{A}) \to \text{Mod}_{(A, \text{d})} \quad\text{et}\quad K(\mathcal{A}) \to K(\text{Mod}_{(A, \text{d})})
```

## FR-DGA-MATH-TEXT-009 — `lemma-cone`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L3562)

Catégorie triangulée conserve exactement l’assertion encadrée.

```tex
\boxed{ K(\mathcal{A})\text{ is a triangulated category} }
```
```tex
\boxed{ K(\mathcal{A})\text{ est une catégorie triangulée} }
```

## FR-DGA-MATH-TEXT-010 — `lemma-homo-change`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L3684)

Puisque justifie la même égalité par d(f)=0.

```tex
b'f = bf - d(h\pi)f = & bf - d(h\pi f) \quad (\text{since }d(f) = 0) \\ = & bf-d(h) \\ = & ga
```
```tex
b'f = bf - d(h\pi)f = & bf - d(h\pi f) \quad (\text{puisque }d(f) = 0) \\ = & bf-d(h) \\ = & ga
```

## FR-DGA-MATH-TEXT-011 — `lemma-factor`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L3721)

D’après le lemme conserve le même renvoi, attaché à la même ligne de calcul.

```tex
1_{\tilde{y}} - s\pi = & tp \\ = & t(dh)p\quad\text{(by Lemma \ref{lemma-id-cone-null})} \\ = & d(thp)
```
```tex
1_{\tilde{y}} - s\pi = & tp \\ = & t(dh)p\quad\text{(d'après le lemme \ref{lemma-id-cone-null})} \\ = & d(thp)
```

## FR-DGA-MATH-TEXT-012 — `lemma-triseq`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L3833)

Et relie les deux mêmes diagrammes de suites.

```tex
\vcenter{ \xymatrix{ x_1 \ar[d]_0 \ar[r] & y_1 \ar[r] \ar[d]_b & z_1 \ar[d]_0 \\ x_2 \ar[r] & y_2 \ar[r] & z_2 } } \quad\text{and}\quad \vcenter{ \xymatrix{ x_2 \ar[d]^0 \ar[r] & y_2 \ar[r] \ar[d]^{b'} & z_2 \ar[d]^0 \\ x_3 \ar[r] & y_3 \ar[r] & z_3 } }
```
```tex
\vcenter{ \xymatrix{ x_1 \ar[d]_0 \ar[r] & y_1 \ar[r] \ar[d]_b & z_1 \ar[d]_0 \\ x_2 \ar[r] & y_2 \ar[r] & z_2 } } \quad\text{et}\quad \vcenter{ \xymatrix{ x_2 \ar[d]^0 \ar[r] & y_2 \ar[r] \ar[d]^{b'} & z_2 \ar[d]^0 \\ x_3 \ar[r] & y_3 \ar[r] & z_3 } }
```

## FR-DGA-MATH-TEXT-013 — `lemma-cone-rotate-isom`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L3950)

Et relie les deux mêmes triangles, sans changer le décalage.

```tex
(z[-1], x, y, \delta[-1], \alpha, \beta) \quad\text{and}\quad (z[-1], x, c(\delta[-1]), \delta[-1], i, p)
```
```tex
(z[-1], x, y, \delta[-1], \alpha, \beta) \quad\text{et}\quad (z[-1], x, c(\delta[-1]), \delta[-1], i, p)
```

## FR-DGA-MATH-TEXT-014 — `equation-cone-isom-triangle`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L4117)

Et sépare les deux triangles associés aux morphismes alpha et alpha tilde.

```tex
x \xrightarrow{\alpha} y \to C(\alpha) \to x[1] \quad\text{and}\quad x \xrightarrow{\tilde{\alpha}} \tilde{y} \to C(\tilde{\alpha}) \to x[1]
```
```tex
x \xrightarrow{\alpha} y \to C(\alpha) \to x[1] \quad\text{et}\quad x \xrightarrow{\tilde{\alpha}} \tilde{y} \to C(\tilde{\alpha}) \to x[1]
```

## FR-DGA-MATH-TEXT-015 — `equation-cone-isom-triangle`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L4117)

Les justifications des six lignes sont lues conjointement : les deux premières identités puis la troisième, sans interversion ni conclusion ajoutée.

```tex
1_{C(\alpha)} = & bp + \sigma c \quad (\text{from }y \xrightarrow{b} C(\alpha) \xrightarrow{c} x[1]) \\ = & b(\alpha\pi + s\beta)p + \sigma(\pi\alpha)c \quad (\text{from }x \xrightarrow{\alpha} y \xrightarrow{\beta} z) \\ = & d(\sigma)\pi p + bs\beta p - \sigma\pi d(p) \quad (\text{by the first two identities above}) \\ = & d(\sigma)\pi p + bs\beta p - \sigma\delta\beta p + \sigma\delta\beta p - \sigma\pi d(p) \\ = & (bs - \sigma\delta)\beta p + d(\sigma)\pi p - \sigma d(\pi)p - \sigma\pi d(p)\quad (\text{by the third identity above}) \\ = & fe + d(\sigma \pi p)
```
```tex
1_{C(\alpha)} = & bp + \sigma c \quad (\text{d'après }y \xrightarrow{b} C(\alpha) \xrightarrow{c} x[1]) \\ = & b(\alpha\pi + s\beta)p + \sigma(\pi\alpha)c \quad (\text{d'après }x \xrightarrow{\alpha} y \xrightarrow{\beta} z) \\ = & d(\sigma)\pi p + bs\beta p - \sigma\pi d(p) \quad (\text{d'après les deux premières identités ci-dessus}) \\ = & d(\sigma)\pi p + bs\beta p - \sigma\delta\beta p + \sigma\delta\beta p - \sigma\pi d(p) \\ = & (bs - \sigma\delta)\beta p + d(\sigma)\pi p - \sigma d(\pi)p - \sigma\pi d(p)\quad (\text{d'après la troisième identité ci-dessus}) \\ = & fe + d(\sigma \pi p)
```

## FR-DGA-MATH-TEXT-016 — `lemma-dgc-analogue-tr4`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L4360)

Puisque conserve l’hypothèse pi_3 beta=0 de cette ligne.

```tex
p_1\pi_3s_2d(p_2s_3) = & p_1\pi_3s_2p_2d(s_3) \\ = & p_1\pi_3(1-\beta\alpha\pi_1\pi_3)d(s_3) \\ = & p_1\pi_3d(s_3)\quad (\text{since }\pi_3\beta = 0) \\ = & p_1\delta_3
```
```tex
p_1\pi_3s_2d(p_2s_3) = & p_1\pi_3s_2p_2d(s_3) \\ = & p_1\pi_3(1-\beta\alpha\pi_1\pi_3)d(s_3) \\ = & p_1\pi_3d(s_3)\quad (\text{puisque }\pi_3\beta = 0) \\ = & p_1\delta_3
```

## FR-DGA-MATH-TEXT-017 — `definition-bimodule`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L4524)

Et relie l’action à gauche de A et l’action à droite de B.

```tex
A \times M \to M, (a, x) \mapsto ax \quad\text{and}\quad M \times B \to M, (x, b) \mapsto xb
```
```tex
A \times M \to M, (a, x) \mapsto ax \quad\text{et}\quad M \times B \to M, (x, b) \mapsto xb
```

## FR-DGA-MATH-TEXT-018 — `lemma-bimodule-over-tensor`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L4607)

Le tableau entier oppose les mêmes bimodules (A,B) et modules à droite sur A opposée tensor B ; la permutation syntaxique française ne déplace pas à droite.

```tex
\begin{matrix} \text{differential graded}\\ (A, B)\text{-bimodules} \end{matrix} \longleftrightarrow \begin{matrix} \text{right differential graded }\\ A^{opp} \otimes_R B\text{-modules} \end{matrix}
```
```tex
\begin{matrix} \text{bimodules différentiels gradués sur}\\ (A, B)\text{} \end{matrix} \longleftrightarrow \begin{matrix} \text{modules différentiels gradués à droite sur }\\ A^{opp} \otimes_R B\text{} \end{matrix}
```

## FR-DGA-MATH-TEXT-019 — `lemma-tensor`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L4728)

Et relie les deux foncteurs induits par tensorisation.

```tex
\text{Mod}_{(A, \text{d})} \to \text{Mod}_{(B, \text{d})} \quad\text{and}\quad K(\text{Mod}_{(A, \text{d})}) \to K(\text{Mod}_{(B, \text{d})})
```
```tex
\text{Mod}_{(A, \text{d})} \to \text{Mod}_{(B, \text{d})} \quad\text{et}\quad K(\text{Mod}_{(A, \text{d})}) \to K(\text{Mod}_{(B, \text{d})})
```

## FR-DGA-MATH-TEXT-020 — `section-bimodules-hom`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L4813)

Est A-linéaire traduit la même contrainte sur f.

```tex
\Hom_A(M, M') = \{f : M \to M' \mid f \text{ is }A\text{-linear}\}
```
```tex
\Hom_A(M, M') = \{f : M \to M' \mid f \text{ est }A\text{-linéaire}\}
```

## FR-DGA-MATH-TEXT-021 — `lemma-hom`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L4879)

Et relie les deux foncteurs Hom, de B vers A.

```tex
\text{Mod}_{(B, \text{d})} \to \text{Mod}_{(A, \text{d})} \quad\text{and}\quad K(\text{Mod}_{(B, \text{d})}) \to K(\text{Mod}_{(A, \text{d})})
```
```tex
\text{Mod}_{(B, \text{d})} \to \text{Mod}_{(A, \text{d})} \quad\text{et}\quad K(\text{Mod}_{(B, \text{d})}) \to K(\text{Mod}_{(A, \text{d})})
```

## FR-DGA-MATH-TEXT-022 — `lemma-restriction-homotopy`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L5016)

Voir ci-dessus renvoie à la construction précédente de la même flèche horizontale.

```tex
\xymatrix{ K(\text{Mod}_{(B, \text{d})}) \ar[d] \ar[rr]_{\text{see above}} \ar[rrd]_F & & K(\text{Mod}_{(A, \text{d})}) \ar[d] \\ D(B, \text{d}) \ar@{..>}[rr] & & D(A, \text{d}) }
```
```tex
\xymatrix{ K(\text{Mod}_{(B, \text{d})}) \ar[d] \ar[rr]_{\text{voir ci-dessus}} \ar[rrd]_F & & K(\text{Mod}_{(A, \text{d})}) \ar[d] \\ D(B, \text{d}) \ar@{..>}[rr] & & D(A, \text{d}) }
```

## FR-DGA-MATH-TEXT-023 — `lemma-rickard`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L6585)

Les trois si gardent les branches i<0, i=0 et i>0 et leurs valeurs.

```tex
(E')^i = \left\{ \begin{matrix} E^i & \text{if }i < 0 \\ \Ker(E^0 \to E^1) & \text{if }i = 0 \\ 0 & \text{if }i > 0 \end{matrix} \right.
```
```tex
(E')^i = \left\{ \begin{matrix} E^i & \text{si }i < 0 \\ \Ker(E^0 \to E^1) & \text{si }i = 0 \\ 0 & \text{si }i > 0 \end{matrix} \right.
```

## FR-DGA-MATH-TEXT-024 — `proposition-rickard`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L6686)

Même vérification des trois branches dans la proposition suivante.

```tex
(E')^i = \left\{ \begin{matrix} E^i & \text{if }i < 0 \\ \Ker(E^0 \to E^1) & \text{if }i = 0 \\ 0 & \text{if }i > 0 \end{matrix} \right.
```
```tex
(E')^i = \left\{ \begin{matrix} E^i & \text{si }i < 0 \\ \Ker(E^0 \to E^1) & \text{si }i = 0 \\ 0 & \text{si }i > 0 \end{matrix} \right.
```

## FR-DGA-MATH-TEXT-025 — `section-resolution-dgas`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L6855)

Les algèbres et ensembles sont tous deux gradués ; aucun qualificatif n’est perdu.

```tex
\Mor_{\text{graded }R\text{-alg}}(R\langle S \rangle, A) \to \text{Map}_{\text{graded sets}}(S, A),\quad \varphi \longmapsto (s \mapsto \varphi(s))
```
```tex
\Mor_{\text{}R\text{-alg graduées}}(R\langle S \rangle, A) \to \text{Map}_{\text{ensembles gradués}}(S, A),\quad \varphi \longmapsto (s \mapsto \varphi(s))
```

## FR-DGA-MATH-TEXT-026 — `section-resolution-dgas`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/dga.tex#L6855)

Même portée des graduations dans les deux Hom et le facteur des applications.

```tex
\Mor_{\text{graded }R\text{-alg}}(A\langle S \rangle, B) \to \Mor_{\text{graded }R\text{-alg}}(A, B) \times \text{Map}_{\text{graded sets}}(S, B),
```
```tex
\Mor_{\text{}R\text{-alg graduées}}(A\langle S \rangle, B) \to \Mor_{\text{}R\text{-alg graduées}}(A, B) \times \text{Map}_{\text{ensembles gradués}}(S, B),
```

## FR-COTANGENT-MATH-TEXT-001 — `section-cotangent-ring-map`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/cotangent.tex#L81)

Ensembles nomme la catégorie d’arrivée du même foncteur V.

```tex
V : \textit{Alg}_A \to \textit{Sets}
```
```tex
V : \textit{Alg}_A \to \textit{Ensembles}
```

## FR-COTANGENT-MATH-TEXT-002 — `section-cotangent-ring-map`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/cotangent.tex#L81)

Ensembles nomme la catégorie de départ du même foncteur U.

```tex
U : \textit{Sets} \to \textit{Alg}_A
```
```tex
U : \textit{Ensembles} \to \textit{Alg}_A
```

## FR-COTANGENT-MATH-TEXT-003 — `remark-variant-cotangent-complex`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/cotangent.tex#L136)

Le diagramme conserve le couple adjoint et les quatre catégories ; Sets devient Ensembles.

```tex
\xymatrix{ \mathcal{A} \ar[d] \ar[r] & \mathcal{S} \ar@<1ex>[l] \ar[d] \\ \textit{Alg}_A \ar[r] & \textit{Sets} \ar@<1ex>[l] }
```
```tex
\xymatrix{ \mathcal{A} \ar[d] \ar[r] & \mathcal{S} \ar@<1ex>[l] \ar[d] \\ \textit{Alg}_A \ar[r] & \textit{Ensembles} \ar@<1ex>[l] }
```

## FR-COTANGENT-MATH-TEXT-004 — `lemma-colimit-cotangent-complex`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/cotangent.tex#L157)

Le foncteur V garde les algèbres sur A et la catégorie des ensembles.

```tex
V : A\textit{-Alg} \to \textit{Sets}
```
```tex
V : A\textit{-Alg} \to \textit{Ensembles}
```

## FR-COTANGENT-MATH-TEXT-005 — `lemma-colimit-cotangent-complex`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/cotangent.tex#L157)

Le foncteur U garde la direction inverse.

```tex
U : \textit{Sets} \to A\textit{-Alg}
```
```tex
U : \textit{Ensembles} \to A\textit{-Alg}
```

## FR-COTANGENT-MATH-TEXT-006 — `lemma-identify-pi-shriek`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/cotangent.tex#L229)

Les morphismes d’ensembles sont les mêmes, avec les deux mêmes objets pointés par beta et epsilon.

```tex
S_\bullet = \Mor_{\textit{Sets}}((E, \beta|_E), (P_\bullet, \epsilon))
```
```tex
S_\bullet = \Mor_{\textit{Ensembles}}((E, \beta|_E), (P_\bullet, \epsilon))
```

## FR-COTANGENT-MATH-TEXT-007 — `lemma-apply-O-B-comparison`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/cotangent.tex#L737)

Et juxtapose les deux mêmes identifications dérivées.

```tex
L\pi_!(\mathcal{O}) = L\pi_!(\underline{B}) = B \quad\text{and}\quad L_{B/A} = L\pi_!(\Omega_{\mathcal{O}/A} \otimes_\mathcal{O} \underline{B}) = L\pi_!(\Omega_{\mathcal{O}/A})
```
```tex
L\pi_!(\mathcal{O}) = L\pi_!(\underline{B}) = B \quad\text{et}\quad L_{B/A} = L\pi_!(\Omega_{\mathcal{O}/A} \otimes_\mathcal{O} \underline{B}) = L\pi_!(\Omega_{\mathcal{O}/A})
```

## FR-COTANGENT-MATH-TEXT-008 — `lemma-triangle-ses`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/cotangent.tex#L1173)

Sur conserve, ligne par ligne, les trois sites C_{B/A}, C_{C/A}, C_{C/B}.

```tex
\begin{matrix} \Omega_1 = \Omega_{\mathcal{O}/A} \otimes_\mathcal{O} \underline{B} \text{ on }\mathcal{C}_{B/A} \\ \Omega_2 = \Omega_{\mathcal{O}/A} \otimes_\mathcal{O} \underline{C} \text{ on }\mathcal{C}_{C/A} \\ \Omega_3 = \Omega_{\mathcal{O}/B} \otimes_\mathcal{O} \underline{C} \text{ on }\mathcal{C}_{C/B} \end{matrix}
```
```tex
\begin{matrix} \Omega_1 = \Omega_{\mathcal{O}/A} \otimes_\mathcal{O} \underline{B} \text{ sur }\mathcal{C}_{B/A} \\ \Omega_2 = \Omega_{\mathcal{O}/A} \otimes_\mathcal{O} \underline{C} \text{ sur }\mathcal{C}_{C/A} \\ \Omega_3 = \Omega_{\mathcal{O}/B} \otimes_\mathcal{O} \underline{C} \text{ sur }\mathcal{C}_{C/B} \end{matrix}
```

## FR-COTANGENT-MATH-TEXT-009 — `lemma-tensor-product`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/cotangent.tex#L2847)

Les deux si gardent exactement i>=-1 et i=-2 ; aucun autrement n’est ajouté.

```tex
H^i(E) = \left\{ \begin{matrix} 0 & \text{if} & i \geq -1 \\ \text{Tor}_1^R(A, B) & \text{if} & i = -2 \end{matrix} \right.
```
```tex
H^i(E) = \left\{ \begin{matrix} 0 & \text{si} & i \geq -1 \\ \text{Tor}_1^R(A, B) & \text{si} & i = -2 \end{matrix} \right.
```

## FR-COTANGENT-MATH-TEXT-010 — `lemma-compute-L-morphism-sheaves-rings`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/cotangent.tex#L3198)

Les deux flèches verticales prennent les sections sur U ; Ensembles reste le même coin du diagramme.

```tex
\xymatrix{ \mathcal{A}\textit{-Alg} \ar[d]_{\text{sections over }U} \ar[r] & \Sh(\mathcal{C}) \ar@<1ex>[l] \ar[d]^{\text{sections over }U} \\ \mathcal{A}(U)\textit{-Alg} \ar[r] & \textit{Sets} \ar@<1ex>[l] }
```
```tex
\xymatrix{ \mathcal{A}\textit{-Alg} \ar[d]_{\text{sections sur }U} \ar[r] & \Sh(\mathcal{C}) \ar@<1ex>[l] \ar[d]^{\text{sections sur }U} \\ \mathcal{A}(U)\textit{-Alg} \ar[r] & \textit{Ensembles} \ar@<1ex>[l] }
```

## FR-SPACES-MATH-TEXT-001 — `section-representable`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L113)

Ens est la catégorie des ensembles ; le domaine, la variance et la liste des foncteurs restent inchangés.

```tex
F, G : (\Sch/S)_{fppf}^{opp} \to \textit{Sets}
```
```tex
F, G : (\Sch/S)_{fppf}^{opp} \to \textit{Ens}
```

## FR-SPACES-MATH-TEXT-002 — `lemma-composition-representable-transformations`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L157)

Ens est la catégorie des ensembles ; le domaine, la variance et la liste des foncteurs restent inchangés.

```tex
F, G, H : (\Sch/S)_{fppf}^{opp} \to \textit{Sets}
```
```tex
F, G, H : (\Sch/S)_{fppf}^{opp} \to \textit{Ens}
```

## FR-SPACES-MATH-TEXT-003 — `lemma-base-change-representable-transformations`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L173)

Ens est la catégorie des ensembles ; le domaine, la variance et la liste des foncteurs restent inchangés.

```tex
F, G, H : (\Sch/S)_{fppf}^{opp} \to \textit{Sets}
```
```tex
F, G, H : (\Sch/S)_{fppf}^{opp} \to \textit{Ens}
```

## FR-SPACES-MATH-TEXT-004 — `lemma-product-representable-transformations`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L193)

Ens est la catégorie des ensembles ; le domaine, la variance et la liste des foncteurs restent inchangés.

```tex
F_i, G_i : (\Sch/S)_{fppf}^{opp} \to \textit{Sets}
```
```tex
F_i, G_i : (\Sch/S)_{fppf}^{opp} \to \textit{Ens}
```

## FR-SPACES-MATH-TEXT-005 — `lemma-representable-transformation-to-sheaf`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L217)

Ens est la catégorie des ensembles ; le domaine, la variance et la liste des foncteurs restent inchangés.

```tex
F, G : (\Sch/S)_{fppf}^{opp} \to \textit{Sets}
```
```tex
F, G : (\Sch/S)_{fppf}^{opp} \to \textit{Ens}
```

## FR-SPACES-MATH-TEXT-006 — `lemma-representable-transformation-diagonal`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L240)

Ens est la catégorie des ensembles ; le domaine, la variance et la liste des foncteurs restent inchangés.

```tex
F, G : (\Sch/S)_{fppf}^{opp} \to \textit{Sets}
```
```tex
F, G : (\Sch/S)_{fppf}^{opp} \to \textit{Ens}
```

## FR-SPACES-MATH-TEXT-007 — `lemma-composition-representable-transformations-property`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L559)

Ens est la catégorie des ensembles ; le domaine, la variance et la liste des foncteurs restent inchangés.

```tex
F, G, H : (\Sch/S)_{fppf}^{opp} \to \textit{Sets}
```
```tex
F, G, H : (\Sch/S)_{fppf}^{opp} \to \textit{Ens}
```

## FR-SPACES-MATH-TEXT-008 — `lemma-base-change-representable-transformations-property`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L577)

Ens est la catégorie des ensembles ; le domaine, la variance et la liste des foncteurs restent inchangés.

```tex
F, G, H : (\Sch/S)_{fppf}^{opp} \to \textit{Sets}
```
```tex
F, G, H : (\Sch/S)_{fppf}^{opp} \to \textit{Ens}
```

## FR-SPACES-MATH-TEXT-009 — `lemma-descent-representable-transformations-property`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L602)

Ens est la catégorie des ensembles ; le domaine, la variance et la liste des foncteurs restent inchangés.

```tex
F, G, H : (\Sch/S)_{fppf}^{opp} \to \textit{Sets}
```
```tex
F, G, H : (\Sch/S)_{fppf}^{opp} \to \textit{Ens}
```

## FR-SPACES-MATH-TEXT-010 — `lemma-product-representable-transformations-property`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L644)

Ens est la catégorie des ensembles ; le domaine, la variance et la liste des foncteurs restent inchangés.

```tex
F_i, G_i : (\Sch/S)_{fppf}^{opp} \to \textit{Sets}
```
```tex
F_i, G_i : (\Sch/S)_{fppf}^{opp} \to \textit{Ens}
```

## FR-SPACES-MATH-TEXT-011 — `lemma-representable-transformations-property-implication`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L664)

Ens est la catégorie des ensembles ; le domaine, la variance et la liste des foncteurs restent inchangés.

```tex
F, G : (\Sch/S)_{fppf}^{opp} \to \textit{Sets}
```
```tex
F, G : (\Sch/S)_{fppf}^{opp} \to \textit{Ens}
```

## FR-SPACES-MATH-TEXT-012 — `lemma-surjective-flat-locally-finite-presentation`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L681)

Ens est la catégorie des ensembles ; le domaine, la variance et la liste des foncteurs restent inchangés.

```tex
F, G : (\Sch/S)_{fppf}^{opp} \to \textit{Sets}
```
```tex
F, G : (\Sch/S)_{fppf}^{opp} \to \textit{Ens}
```

## FR-SPACES-MATH-TEXT-013 — `definition-algebraic-space`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L804)

Ens est la catégorie des ensembles ; le domaine, la variance et la liste des foncteurs restent inchangés.

```tex
F : (\Sch/S)^{opp}_{fppf} \longrightarrow \textit{Sets}
```
```tex
F : (\Sch/S)^{opp}_{fppf} \longrightarrow \textit{Ens}
```

## FR-SPACES-MATH-TEXT-014 — `example-infinite-product`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L2480)

La phrase française conserve tous sauf un nombre fini de x_n nuls, et non seulement un nombre fini de termes nuls.

```tex
I = \{x = (x_n) \in A \mid \text{all but a finite number of }x_n\text{ are zero}\}
```
```tex
I = \{x = (x_n) \in A \mid \text{tous les }x_n\text{ sauf un nombre fini d'entre eux sont nuls}\}
```

## FR-SPACES-MATH-TEXT-015 — `lemma-fully-faithful`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L2609)

Espaces/S est le nom français de la même catégorie.

```tex
\textit{Spaces}/S
```
```tex
\textit{Espaces}/S
```

## FR-SPACES-MATH-TEXT-016 — `lemma-fully-faithful`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L2609)

Espaces prime/S conserve la catégorie associée au plus grand site.

```tex
\textit{Spaces}'/S
```
```tex
\textit{Espaces}'/S
```

## FR-SPACES-MATH-TEXT-017 — `lemma-fully-faithful`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L2609)

Les deux catégories et le sens du foncteur sont inchangés.

```tex
\textit{Spaces}/S \longrightarrow \textit{Spaces}'/S
```
```tex
\textit{Espaces}/S \longrightarrow \textit{Espaces}'/S
```

## FR-SPACES-MATH-TEXT-018 — `lemma-fully-faithful`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L2609)

L’appartenance de X prime concerne la même catégorie prime.

```tex
X' \in \Ob(\textit{Spaces}'/S)
```
```tex
X' \in \Ob(\textit{Espaces}'/S)
```

## FR-SPACES-MATH-TEXT-019 — `lemma-fully-faithful`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L2609)

Et conserve les deux morphismes U vers X prime et R vers le produit fibré.

```tex
U \longrightarrow X' \quad\text{and}\quad R \longrightarrow U \times_{X'} U
```
```tex
U \longrightarrow X' \quad\text{et}\quad R \longrightarrow U \times_{X'} U
```

## FR-SPACES-MATH-TEXT-020 — `lemma-fully-faithful`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L2609)

Même catégorie d’appartenance dans la preuve.

```tex
X' \in \Ob(\textit{Spaces}'/S)
```
```tex
X' \in \Ob(\textit{Espaces}'/S)
```

## FR-SPACES-MATH-TEXT-021 — `lemma-fully-faithful`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L2609)

La catégorie finale est bien Espaces/S sans prime.

```tex
\textit{Spaces}/S
```
```tex
\textit{Espaces}/S
```

## FR-EXERCISES-MATH-TEXT-001 — `exercise-prime-in-colimit`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L196)

Et garde l’idéal premier et la compatibilité à toutes les transitions i<=j.

```tex
\Spec(A) = \{(\mathfrak p_i)_{i \in I} \mid \mathfrak p_i \subset A_i \text{ and } \mathfrak p_i = \varphi_{ij}^{-1}(\mathfrak p_j)\ \forall i \leq j\} \subset \prod\nolimits_{i \in I} \Spec(A_i)
```
```tex
\Spec(A) = \{(\mathfrak p_i)_{i \in I} \mid \mathfrak p_i \subset A_i \text{ et } \mathfrak p_i = \varphi_{ij}^{-1}(\mathfrak p_j)\ \forall i \leq j\} \subset \prod\nolimits_{i \in I} \Spec(A_i)
```

## FR-EXERCISES-MATH-TEXT-002 — `exercise-radical-ideals-closed`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L472)

Tel que qualifie I=radical(I) ; fermée qualifie la partie T du spectre. Domaine et codomaine restent identiques.

```tex
\{I\subset A\text{ with }I = \sqrt{I}\} \longrightarrow \{T\subset \Spec(A)\text{ closed}\}
```
```tex
\{I\subset A\text{ tel que }I = \sqrt{I}\} \longrightarrow \{T\subset \Spec(A)\text{ fermée}\}
```

## FR-EXERCISES-MATH-TEXT-003 — `definition-length`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L794)

Longueur conserve la même borne supérieure sur les chaînes strictes ; la discordance R/A en prose est restaurée séparément.

```tex
\text{length}_A(M) = \sup \{ n \mid \exists\ 0 = M_0 \subset M_1 \subset \ldots \subset M_n = M, \text{ }M_i \not = M_{i + 1} \}.
```
```tex
\text{longueur}_A(M) = \sup \{ n \mid \exists\ 0 = M_0 \subset M_1 \subset \ldots \subset M_n = M, \text{ }M_i \not = M_{i + 1} \}.
```

## FR-EXERCISES-MATH-TEXT-004 — `exercise-compute-depth`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L960)

Prof abrège profondeur, le même invariant depth_I(M).

```tex
\text{depth}_I(M)
```
```tex
\text{prof}_I(M)
```

## FR-EXERCISES-MATH-TEXT-005 — `exercise-depth-not-inherited-localization`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L976)

Même profondeur, même localisation et borne >=1.

```tex
\text{depth}_\mathfrak m(R) \geq 1
```
```tex
\text{prof}_\mathfrak m(R) \geq 1
```

## FR-EXERCISES-MATH-TEXT-006 — `exercise-depth-not-inherited-localization`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L976)

Même profondeur, égalité zéro conservée.

```tex
\text{depth}_\mathfrak p(R_\mathfrak p) = 0
```
```tex
\text{prof}_\mathfrak p(R_\mathfrak p) = 0
```

## FR-EXERCISES-MATH-TEXT-007 — `exercise-depth-examples`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L998)

Même profondeur, égalité n conservée.

```tex
\text{depth}(R) = n
```
```tex
\text{prof}(R) = n
```

## FR-EXERCISES-MATH-TEXT-008 — `exercise-make-depth-1`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1004)

Même profondeur de Q et même borne >=1.

```tex
\text{depth}(Q) \geq 1
```
```tex
\text{prof}(Q) \geq 1
```

## FR-EXERCISES-MATH-TEXT-009 — `exercise-make-depth-1`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1004)

Longueur_R(K) garde l’exigence de finitude.

```tex
\text{length}_R(K) < \infty
```
```tex
\text{longueur}_R(K) < \infty
```

## FR-EXERCISES-MATH-TEXT-010 — `exercise-make-depth-2`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1023)

Profondeur de N : la borne >=1 reste inchangée.

```tex
\text{depth}(N) \geq 1
```
```tex
\text{prof}(N) \geq 1
```

## FR-EXERCISES-MATH-TEXT-011 — `exercise-make-depth-2`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1023)

Profondeur de N : l’égalité 1 reste inchangée.

```tex
\text{depth}(N) = 1
```
```tex
\text{prof}(N) = 1
```

## FR-EXERCISES-MATH-TEXT-012 — `exercise-make-depth-2`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1023)

Profondeur du quotient M/N : l’égalité zéro reste inchangée.

```tex
\text{depth}(M/N) = 0
```
```tex
\text{prof}(M/N) = 0
```

## FR-EXERCISES-MATH-TEXT-013 — `exercise-make-depth-2`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1023)

La longueur finie concerne le même quotient N prime/N.

```tex
\text{length}_R(N'/N) < \infty
```
```tex
\text{longueur}_R(N'/N) < \infty
```

## FR-EXERCISES-MATH-TEXT-014 — `exercise-Hartshorne-reduced`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1040)

Profondeur de R : la borne >=2 reste exacte, première occurrence.

```tex
\text{depth}(R) \geq 2
```
```tex
\text{prof}(R) \geq 2
```

## FR-EXERCISES-MATH-TEXT-015 — `exercise-Hartshorne-reduced`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1040)

Même borne >=2, seconde occurrence.

```tex
\text{depth}(R) \geq 2
```
```tex
\text{prof}(R) \geq 2
```

## FR-EXERCISES-MATH-TEXT-016 — `exercise-Hartshorne-reduced`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1040)

La mention abrégée garde le même invariant et la même borne >=2.

```tex
\text{depth} \geq 2
```
```tex
\text{prof} \geq 2
```

## FR-EXERCISES-MATH-TEXT-017 — `exercise-product-matrices-ring`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1285)

Et sépare les matrices X et Y, avec les mêmes coefficients.

```tex
X = \left( \begin{matrix} x_{11} & x_{12}\\ x_{21} & x_{22} \end{matrix} \right) \quad\text{and}\quad Y = \left( \begin{matrix} y_{11} & y_{12}\\ y_{21} & y_{22} \end{matrix} \right).
```
```tex
X = \left( \begin{matrix} x_{11} & x_{12}\\ x_{21} & x_{22} \end{matrix} \right) \quad\text{et}\quad Y = \left( \begin{matrix} y_{11} & y_{12}\\ y_{21} & y_{22} \end{matrix} \right).
```

## FR-EXERCISES-MATH-TEXT-018 — `exercise-algebraic-extension`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1439)

Deg.tr. abrège degré de transcendance ; le corps de base k et les extensions K/K prime restent identiques.

```tex
\text{trdeg}_k(K) = \text{trdeg}_k(K')
```
```tex
\text{deg.tr.}_k(K) = \text{deg.tr.}_k(K')
```

## FR-EXERCISES-MATH-TEXT-019 — `exercise-algebraic-extension`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1439)

Même invariant et même inégalité stricte d<deg.tr.

```tex
d < \text{trdeg}_k(K')
```
```tex
d < \text{deg.tr.}_k(K')
```

## FR-EXERCISES-MATH-TEXT-020 — `exercise-growth-powers-subvector-space`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1448)

Pour un certain n conserve l’existence d’une somme finie de produits v_i w_i, avec les mêmes espaces.

```tex
VW = \{f \in K \mid f = \sum\nolimits_{i = 1, \ldots, n} v_i w_i \text{ for some }n\text{ and }v_i \in V, w_i \in W\}
```
```tex
VW = \{f \in K \mid f = \sum\nolimits_{i = 1, \ldots, n} v_i w_i \text{ pour un certain }n\text{ et }v_i \in V, w_i \in W\}
```

## FR-EXERCISES-MATH-TEXT-021 — `exercise-trace-det-rings`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1605)

Norme_{B/A} est la même application que Norm_{B/A}.

```tex
\text{Norm}_{B/A}
```
```tex
\text{Norme}_{B/A}
```

## FR-EXERCISES-MATH-TEXT-022 — `exercise-trace-det-rings`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1605)

Le lieu fermé est défini par la même norme de b.

```tex
\pi(V(b)) = V(\text{Norm}_{B/A}(b))
```
```tex
\pi(V(b)) = V(\text{Norme}_{B/A}(b))
```

## FR-EXERCISES-MATH-TEXT-023 — `exercise-trace-det-rings`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1605)

La même norme est composée avec i.

```tex
i(\text{Norm}_{B/A}(b))
```
```tex
i(\text{Norme}_{B/A}(b))
```

## FR-EXERCISES-MATH-TEXT-024 — `exercise-trace-det-rings`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1605)

La norme après changement de base concerne B prime/A prime et b tensor 1.

```tex
\text{Norm}_{B'/A'}(b \otimes 1)
```
```tex
\text{Norme}_{B'/A'}(b \otimes 1)
```

## FR-EXERCISES-MATH-TEXT-025 — `exercise-trace-det-rings`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1605)

Même norme initiale B/A au membre correspondant.

```tex
\text{Norm}_{B/A}(b)
```
```tex
\text{Norme}_{B/A}(b)
```

## FR-EXERCISES-MATH-TEXT-026 — `exercise-cover-ring-map`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L1658)

Et relie les deux mêmes recouvrements principaux.

```tex
\Spec(A) = \bigcup D(f_i) \quad\text{and}\quad \Spec(B) = \bigcup D(g_j).
```
```tex
\Spec(A) = \bigcup D(f_i) \quad\text{et}\quad \Spec(B) = \bigcup D(g_j).
```

## FR-EXERCISES-MATH-TEXT-027 — `exercise-modified-product-over-points`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L2770)

Le tableau entier garde pour tout x dans U, il existe V dans B, puis x dans V contenu dans U et la contrainte sur la famille de sections.

```tex
\mathcal{F}(U) = \left\{ (s_x)_{x \in U} \middle| \begin{matrix} \text{ for every }x\text{ in }U\text{ there exists } V \in \mathcal{B} \\ x \in V \subset U\text{ such that } (s_y)_{y \in V} \in A_V \end{matrix} \right\}
```
```tex
\mathcal{F}(U) = \left\{ (s_x)_{x \in U} \middle| \begin{matrix} \text{ pour tout }x\text{ dans }U\text{ il existe } V \in \mathcal{B} \\ x \in V \subset U\text{ tel que } (s_y)_{y \in V} \in A_V \end{matrix} \right\}
```

## FR-EXERCISES-MATH-TEXT-028 — `exercise-exact-but-not-a-stalk-functor`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L2796)

Ensembles garde la catégorie d’arrivée du foncteur.

```tex
F : \Sh(X) \longrightarrow \textit{Sets}
```
```tex
F : \Sh(X) \longrightarrow \textit{Ensembles}
```

## FR-EXERCISES-MATH-TEXT-029 — `exercise-cohomology-coordinate-axes`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L4105)

Pour conserve les deux inégalités strictes i>j>0.

```tex
T_i T_j = 0\text{ for }i > j > 0
```
```tex
T_i T_j = 0\text{ pour }i > j > 0
```

## FR-EXERCISES-MATH-TEXT-030 — `exercise-Noetherian`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L4203)

Il existe un n>=1 tel que I^n x=0 conserve la portée du quantificateur.

```tex
M[I^\infty] = \{x \in M \mid \text{ there exists an }n \geq 1\text{ such that }I^nx = 0\}
```
```tex
M[I^\infty] = \{x \in M \mid \text{ il existe un }n \geq 1\text{ tel que }I^nx = 0\}
```

## FR-EXERCISES-MATH-TEXT-031 — `exercise-one-divisor-in-another`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L4483)

Et relie les deux mêmes inclusions de diviseurs.

```tex
D_1 \subset X \times T \quad\text{and}\quad D_2 \subset X \times T
```
```tex
D_1 \subset X \times T \quad\text{et}\quad D_2 \subset X \times T
```

## FR-EXERCISES-MATH-TEXT-032 — `exercise-node-in-the-plane`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L5805)

Et relie les deux profils de valuations v et w ; toutes les bornes restent exactes.

```tex
v(x) = 1, v(y) > 1 \quad\text{and}\quad w(x) > 1, w(y) = 1
```
```tex
v(x) = 1, v(y) > 1 \quad\text{et}\quad w(x) > 1, w(y) = 1
```

## FR-EXERCISES-MATH-TEXT-033 — `exercise-two-vectors`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L6673)

Images linéairement dépendantes conserve la condition sur a,b dans le même espace résiduel à trois coordonnées.

```tex
Z = \{\mathfrak p \in \Spec(A) \mid a, b \text{ map to linearly dependent vectors of } \kappa(\mathfrak p)^{\oplus 3}\}
```
```tex
Z = \{\mathfrak p \in \Spec(A) \mid a, b \text{ ont des images linéairement dépendantes dans } \kappa(\mathfrak p)^{\oplus 3}\}
```

## FR-EXERCISES-MATH-TEXT-034 — `exercise-cubics`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L6743)

Dans précise le même anneau polynomial complexe où l’identité doit tenir.

```tex
(*)\quad F(\lambda x + \mu y + \nu z) = 0 \text{ in } \mathbf{C}[\lambda, \mu, \nu]
```
```tex
(*)\quad F(\lambda x + \mu y + \nu z) = 0 \text{ dans } \mathbf{C}[\lambda, \mu, \nu]
```

## Limites

Les fichiers publics restent inchangés. Les textes en dehors des passages lus peuvent encore contenir des écarts. Cette vérification de fidélité n’invente ni consultation antérieure de canon ni attestation externe pour chaque terme. Les opérations de restauration et les reliquats linguistiques signalés restent distincts. Les éditions complètes doivent encore être reconstruites et vérifiées.
