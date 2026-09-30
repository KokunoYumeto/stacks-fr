# Chapitre 60 — Formules et texte des formules

**Contrôle délimité, non certification intégrale du chapitre.**

[Réparations](CRYSTALLINE_FR_REVIEW.fr.md) · [Contrôles](CRYSTALLINE_FR_CANDIDATE_RECONCILIATION.json) · [Paires exactes](CRYSTALLINE_FR_READER_TEXT_CANDIDATES.json)

Après les 26 restaurations de lecture et la réparation grammaticale, les squelettes mathématiques concordent dans chacun des 174 blocs étiquetés. Les 22 paires ci-dessous ont été lues, et non acceptées du seul fait que leur texte était masqué par le comparateur. Les 174 labels, 457 références, dix citations et les autres commandes suivies concordent. Les 494 événements d’environnement ont le même ordre.

## FR-CRYSTALLINE-MATH-TEXT-001 — `lemma-divided-power-envelope`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L54)

Ens désigne la même catégorie des ensembles que Sets ; ni le foncteur ni sa cible mathématique ne changent.

```tex
F : \mathcal{C} \longrightarrow \textit{Sets}
```
```tex
F : \mathcal{C} \longrightarrow \textit{Ens}
```

## FR-CRYSTALLINE-MATH-TEXT-002 — `lemma-divided-power-envelope`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L54)

Lecture du tableau entier : phi reste un homomorphisme d’anneaux à puissances divisées ; psi reste un homomorphisme de A-algèbres soumis à la même inclusion.

```tex
F(C, K, \delta) = \left\{ (\varphi, \psi) \middle| \begin{matrix} \varphi : (A, I, \gamma) \to (C, K, \delta) \text{ homomorphism of divided power rings} \\ \psi : (B, J) \to (C, K)\text{ an } A\text{-algebra homomorphism with }\psi(J) \subset K \end{matrix} \right\}
```
```tex
F(C, K, \delta) = \left\{ (\varphi, \psi) \middle| \begin{matrix} \varphi : (A, I, \gamma) \to (C, K, \delta) \text{ homomorphisme d'anneaux à puissances divisées} \\ \psi : (B, J) \to (C, K)\text{ un homomorphisme de } A\text{-algèbres tel que }\psi(J) \subset K \end{matrix} \right\}
```

## FR-CRYSTALLINE-MATH-TEXT-003 — `definition-divided-power-envelope`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L111)

Les deux côtés de la correspondance gardent les mêmes types de morphismes, les mêmes idéaux et le même sens de flèche.

```tex
\begin{matrix} \text{ring maps }B \to C \\ \text{ which map }J\text{ into }K \end{matrix} \longleftrightarrow \begin{matrix} \text{divided power homomorphisms} \\ (D, \bar J, \bar \gamma) \to (C, K, \delta) \end{matrix}
```
```tex
\begin{matrix} \text{homomorphismes d'anneaux }B \to C \\ \text{ qui envoient }J\text{ dans }K \end{matrix} \longleftrightarrow \begin{matrix} \text{homomorphismes à puissances divisées} \\ (D, \bar J, \bar \gamma) \to (C, K, \delta) \end{matrix}
```

## FR-CRYSTALLINE-MATH-TEXT-004 — `lemma-describe-divided-power-envelope`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L184)

Dans B situe la relation dans le même anneau.

```tex
\mathcal{R} = \{(r_0, r_t) \in I \oplus \bigoplus\nolimits_{t \in T} B \mid \sum r_t f_t = r_0 \text{ in }B\}
```
```tex
\mathcal{R} = \{(r_0, r_t) \in I \oplus \bigoplus\nolimits_{t \in T} B \mid \sum r_t f_t = r_0 \text{ dans }B\}
```

## FR-CRYSTALLINE-MATH-TEXT-005 — `lemma-flat-extension-divided-power-envelope`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L370)

Dans B situe la relation dans le même anneau à cette deuxième occurrence.

```tex
\mathcal{R} = \{(r_0, r_t) \in I \oplus \bigoplus\nolimits_{t \in T} B \mid \sum r_t f_t = r_0 \text{ in }B\}
```
```tex
\mathcal{R} = \{(r_0, r_t) \in I \oplus \bigoplus\nolimits_{t \in T} B \mid \sum r_t f_t = r_0 \text{ dans }B\}
```

## FR-CRYSTALLINE-MATH-TEXT-006 — `equation-base-change`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L397)

Dans B prime conserve le changement de base de la relation.

```tex
\mathcal{R}' = \{(r'_0, r'_t) \in I' \oplus \bigoplus\nolimits_{t \in T} B' \mid \sum r'_t f'_t = r'_0 \text{ in }B'\}
```
```tex
\mathcal{R}' = \{(r'_0, r'_t) \in I' \oplus \bigoplus\nolimits_{t \in T} B' \mid \sum r'_t f'_t = r'_0 \text{ dans }B'\}
```

## FR-CRYSTALLINE-MATH-TEXT-007 — `equation-base-change`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L397)

Pour conserve la portée sur la liste j=1,...,m.

```tex
r_{j0} = \sum\nolimits_t r_{jt} f_t \in I \text{ for } j = 1, \ldots, m
```
```tex
r_{j0} = \sum\nolimits_t r_{jt} f_t \in I \text{ pour } j = 1, \ldots, m
```

## FR-CRYSTALLINE-MATH-TEXT-008 — `equation-base-change`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L397)

Pour tout conserve le quantificateur universel sur t.

```tex
i'_t = r'_t - \sum\nolimits_j c_j r_{jt} \in I' \text{ for all }t
```
```tex
i'_t = r'_t - \sum\nolimits_j c_j r_{jt} \in I' \text{ pour tout }t
```

## FR-CRYSTALLINE-MATH-TEXT-009 — `definition-compatible`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L609)

Et relie les deux mêmes homomorphismes.

```tex
(A, I, \gamma) \to (B, J + IB, \bar \gamma)\quad\text{and}\quad (B, J, \delta) \to (B, J + IB, \bar \gamma)
```
```tex
(A, I, \gamma) \to (B, J + IB, \bar \gamma)\quad\text{et}\quad (B, J, \delta) \to (B, J + IB, \bar \gamma)
```

## FR-CRYSTALLINE-MATH-TEXT-010 — `lemma-omega`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L939)

Idéal engendré par, avec et et conservent les générateurs et les deux contraintes simultanées.

```tex
I^{[n]} = \text{ideal generated by } \gamma_{e_1}(x_1) \ldots \gamma_{e_t}(x_t) \text{ with }\sum e_j \geq n\text{ and }x_j \in I.
```
```tex
I^{[n]} = \text{idéal engendré par } \gamma_{e_1}(x_1) \ldots \gamma_{e_t}(x_t) \text{ avec }\sum e_j \geq n\text{ et }x_j \in I.
```

## FR-CRYSTALLINE-MATH-TEXT-011 — `section-sheaves`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L1942)

Ou conserve les deux sites possibles et ne les identifie pas.

```tex
\mathcal{C} = \text{CRIS}(X/S) \quad\text{or}\quad \mathcal{C} = \text{Cris}(X/S).
```
```tex
\mathcal{C} = \text{CRIS}(X/S) \quad\text{ou}\quad \mathcal{C} = \text{Cris}(X/S).
```

## FR-CRYSTALLINE-MATH-TEXT-012 — `lemma-crystals-on-affine`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L2997)

Le tableau est lu comme un tout : quasi-cohérents qualifie les O-modules, et les quatre conditions numérotées restent conjointes.

```tex
\begin{matrix} \text{crystals in quasi-coherent} \\ \mathcal{O}_{X/S}\text{-modules on }\text{Cris}(X/S) \end{matrix} \longrightarrow \begin{matrix} \text{pairs }(M, \nabla)\text{ satisfying} \\ \text{(\ref{item-complete}), (\ref{item-connection}), (\ref{item-integrable}), and (\ref{item-topologically-quasi-nilpotent})} \end{matrix}
```
```tex
\begin{matrix} \text{cristaux en} \\ \mathcal{O}_{X/S}\text{-modules quasi-cohérents sur }\text{Cris}(X/S) \end{matrix} \longrightarrow \begin{matrix} \text{couples }(M, \nabla)\text{ vérifiant} \\ \text{(\ref{item-complete}), (\ref{item-connection}), (\ref{item-integrable}) et (\ref{item-topologically-quasi-nilpotent})} \end{matrix}
```

## FR-CRYSTALLINE-MATH-TEXT-013 — `proposition-crystals-on-affine`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L3109)

Même tableau dans la proposition suivante ; même portée et mêmes quatre références.

```tex
\begin{matrix} \text{crystals in quasi-coherent} \\ \mathcal{O}_{X/S}\text{-modules on }\text{Cris}(X/S) \end{matrix} \longrightarrow \begin{matrix} \text{pairs }(M, \nabla)\text{ satisfying} \\ \text{(\ref{item-complete}), (\ref{item-connection}), (\ref{item-integrable}), and (\ref{item-topologically-quasi-nilpotent})} \end{matrix}
```
```tex
\begin{matrix} \text{cristaux en} \\ \mathcal{O}_{X/S}\text{-modules quasi-cohérents sur }\text{Cris}(X/S) \end{matrix} \longrightarrow \begin{matrix} \text{couples }(M, \nabla)\text{ vérifiant} \\ \text{(\ref{item-complete}), (\ref{item-connection}), (\ref{item-integrable}) et (\ref{item-topologically-quasi-nilpotent})} \end{matrix}
```

## FR-CRYSTALLINE-MATH-TEXT-014 — `lemma-crystals-on-affine-smooth`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L3191)

Et sépare les deux mêmes foncteurs, sans modifier les produits tensoriels complétés.

```tex
F : (M, \nabla) \longmapsto (M \otimes^\wedge_{D, a} D', \nabla') \quad\text{and}\quad G : (M', \nabla') \longmapsto (M' \otimes^\wedge_{D', b} D, \nabla)
```
```tex
F : (M, \nabla) \longmapsto (M \otimes^\wedge_{D, a} D', \nabla') \quad\text{et}\quad G : (M', \nabla') \longmapsto (M' \otimes^\wedge_{D', b} D, \nabla)
```

## FR-CRYSTALLINE-MATH-TEXT-015 — `lemma-complete`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L3418)

Si, si et sinon conservent les trois branches p=0, p=1 et le cas restant.

```tex
R^pg_*\mathcal{F}(B \to C, \delta) = \left\{ \begin{matrix} \lim_e \mathcal{F}(B_e \to C, \delta) & \text{if }p = 0 \\ R^1\lim_e \mathcal{F}(B_e \to C, \delta) & \text{if }p = 1 \\ 0 & \text{else} \end{matrix} \right.
```
```tex
R^pg_*\mathcal{F}(B \to C, \delta) = \left\{ \begin{matrix} \lim_e \mathcal{F}(B_e \to C, \delta) & \text{si }p = 0 \\ R^1\lim_e \mathcal{F}(B_e \to C, \delta) & \text{si }p = 1 \\ 0 & \text{sinon} \end{matrix} \right.
```

## FR-CRYSTALLINE-MATH-TEXT-016 — `example-cosimplicial-module`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L3512)

Si et sinon conservent les deux branches de la définition de h_n.

```tex
h_n(e_i)(\alpha^n_j) = \left\{ \begin{matrix} e_{i} & \text{if} & i < j \\ 0 & \text{else} \end{matrix} \right.
```
```tex
h_n(e_i)(\alpha^n_j) = \left\{ \begin{matrix} e_{i} & \text{si} & i < j \\ 0 & \text{sinon} \end{matrix} \right.
```

## FR-CRYSTALLINE-MATH-TEXT-017 — `equation-cosimplicial-morphism`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L3547)

Les deux branches évaluées à f(i) sont inchangées.

```tex
h_m(e_{f(i)})(\alpha^m_j) = \left\{ \begin{matrix} e_{f(i)} & \text{if} & f(i) < j \\ 0 & \text{else} \end{matrix} \right.
```
```tex
h_m(e_{f(i)})(\alpha^m_j) = \left\{ \begin{matrix} e_{f(i)} & \text{si} & f(i) < j \\ 0 & \text{sinon} \end{matrix} \right.
```

## FR-CRYSTALLINE-MATH-TEXT-018 — `equation-cosimplicial-morphism`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L3547)

Les deux branches évaluées à i sont inchangées ; la parenthèse source omise a été restaurée séparément.

```tex
M_*(f)(h_n(e_i)(\alpha^m_j \circ f) = M_*(f)(h_n(e_i)(\alpha^n_{j'})) = \left\{ \begin{matrix} e_{f(i)} & \text{if} & i < j' \\ 0 & \text{else} \end{matrix} \right.
```
```tex
M_*(f)(h_n(e_i)(\alpha^m_j \circ f) = M_*(f)(h_n(e_i)(\alpha^n_{j'})) = \left\{ \begin{matrix} e_{f(i)} & \text{si} & i < j' \\ 0 & \text{sinon} \end{matrix} \right.
```

## FR-CRYSTALLINE-MATH-TEXT-019 — `lemma-compute-cohomology-crystal-smooth`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L3991)

Et conserve les deux morphismes de changement de base.

```tex
M' \otimes^\wedge_{D'} \Omega^*_{D'} \longrightarrow M \otimes^\wedge_D \Omega^*_D \quad\text{and}\quad M \otimes^\wedge_D \Omega^*_D \longrightarrow M' \otimes^\wedge_{D'} \Omega^*_{D'}
```
```tex
M' \otimes^\wedge_{D'} \Omega^*_{D'} \longrightarrow M \otimes^\wedge_D \Omega^*_D \quad\text{et}\quad M \otimes^\wedge_D \Omega^*_D \longrightarrow M' \otimes^\wedge_{D'} \Omega^*_{D'}
```

## FR-CRYSTALLINE-MATH-TEXT-020 — `example-affine-n-space`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L4174)

Avec introduit la même définition de P.

```tex
C = P/J = P/pP\quad\text{with}\quad P = \mathbf{Z}_p[x_1, \ldots, x_r]
```
```tex
C = P/J = P/pP\quad\text{avec}\quad P = \mathbf{Z}_p[x_1, \ldots, x_r]
```

## FR-CRYSTALLINE-MATH-TEXT-021 — `lemma-find-homotopy`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L5053)

Et relie les mêmes définitions de epsilon et epsilon prime.

```tex
\epsilon(f) = af - \theta(\partial_z(f)) \quad\text{and}\quad \epsilon'(f) = (\theta \otimes 1)(\text{d}_1(f)) - \text{d}_1(\theta(f))
```
```tex
\epsilon(f) = af - \theta(\partial_z(f)) \quad\text{et}\quad \epsilon'(f) = (\theta \otimes 1)(\text{d}_1(f)) - \text{d}_1(\theta(f))
```

## FR-CRYSTALLINE-MATH-TEXT-022 — `remark-F-crystal-variants`

[Source](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L5548)

Rang traduit rank sans changer la borne stricte ni le facteur i.

```tex
N > i \cdot \text{rank}(\mathcal{E})
```
```tex
N > i \cdot \text{rang}(\mathcal{E})
```

## Limites

Le texte ordinaire hors des contextes effectivement lus peut encore contenir des écarts. Les références rétablies, la restitution littérale intégrale et la grammaire française sont distinguées dans le dossier de réparation. Aucun PDF reconstruit ni remplacement public n’est revendiqué.
