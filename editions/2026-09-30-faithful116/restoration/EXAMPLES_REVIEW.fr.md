# Exemples : séparer la traduction des corrections de la source

**LaTeX local ; aucune édition publique corrigée à ce stade.**

[LaTeX](staged/fr/110_examples.fr.tex) · [Contrôles](EXAMPLES_FR_VALIDATION.json) · [Contextes complets](EXAMPLES_FR_REPAIRS.json)

Les 22 contextes candidats ont été lus entièrement dans les deux langues. Le dossier distingue les retours au témoin officiel et quatre réparations de sens dans le français. En particulier, la restriction à une caractéristique première, le sujet qui admet un recouvrement lisse et la condition de torsion p-primaire doivent être conservés. Les propositions de corrections de la source restent lisibles dans les avant/après ; aucune anomalie officielle n’est pour autant certifiée correcte. Une seule mise en page sur deux lignes est conservée et contrôlée exactement.

## FR-EXAMPLES-001 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L617)

Rétablit le A imprimé, alors que l’anneau ambiant est R. Substituer R corrige la source ; ce n’est pas une nécessité de traduction.

Avant :
```tex
pour un certain $R$-module $C$
```
Après :
```tex
pour un certain $A$-module $C$
```

## FR-EXAMPLES-002 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L847)

Rétablit l’exposant n−1 de la série officielle. L’exposant n était une modification motivée par l’identité qui suit, et non une traduction du même exposant.

Avant :
```tex
f = \sum r \alpha^n x^n
```
Après :
```tex
f = \sum r \alpha^{n - 1} x^n
```

## FR-EXAMPLES-003 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L915)

Rétablit le R[z][[x]] du sous-module dans cette seule phrase ; les autres occurrences de k[z][[x]] restent celles de la source.

Avant :
```tex
le sous-$k[z][[x]]$-module
```
Après :
```tex
le sous-$R[z][[x]]$-module
```

## FR-EXAMPLES-004 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L1112)

Rétablit ensemble les deux signes moins de la même identité. Leur suppression était une correction du calcul, conservée comme proposition dans le dossier avant/après.

Avant :
```tex
$xe = (x, 0) \sim (0, z) = z(0, 1)$
```
Après :
```tex
$xe = (x, 0) \sim (0, -z) = z(0, -1)$
```

## FR-EXAMPLES-005 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L1187)

Le nombre de générateurs suggère 2^(i−1), mais le témoin affirme 2^i. La traduction diplomatique ne doit pas corriger tacitement ce nombre.

Avant :
```tex
dimension $2^{i - 1}$
```
Après :
```tex
dimension $2^i$
```

## FR-EXAMPLES-006 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L1223)

Rétablit l’indice i imprimé à gauche de l’identité, sans l’harmoniser tacitement avec n à droite.

Avant :
```tex
$D(f_n) = x^{-n}$
```
Après :
```tex
$D(f_i) = x^{-n}$
```

## FR-EXAMPLES-007 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L1280)

Rétablit l’ordre de composition imprimé. L’autre ordre constitue une correction du rôle de la section, non une variante linguistique.

Avant :
```tex
$\psi \circ i = \text{id}$
```
Après :
```tex
$i \circ \psi = \text{id}$
```

## FR-EXAMPLES-008 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L1280)

Rétablit D sans chapeau ; l’extension complétée est effectivement notée D chapeau plus haut, mais l’ajouter ici modifie la source.

Avant :
```tex
$\hat D \circ i = 0$
```
Après :
```tex
$D \circ i = 0$
```

## FR-EXAMPLES-009 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L1660)

Rétablit les deux X de la formule officielle. Le diviseur vient d’être défini sur Y, ce qui explique la proposition de correction mais n’autorise pas sa substitution silencieuse.

Avant :
```tex
$\mathcal{O}_Y(ND) \cong \mathcal{O}_Y$
```
Après :
```tex
$\mathcal{O}_X(ND) \cong \mathcal{O}_X$
```

## FR-EXAMPLES-010 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L2559)

Rétablit l’indice n de L dans cette phrase, en conservant i dans la définition précédente de L_{n,i}.

Avant :
```tex
$\text{pr}_i^*\mathcal{L}_i$
```
Après :
```tex
$\text{pr}_i^*\mathcal{L}_n$
```

## FR-EXAMPLES-011 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L2608)

Rétablit C_n dans la conclusion officielle ; les indices i de Q_i et Q_i prime restent inchangés.

Avant :
```tex
$(C_i)_K$
```
Après :
```tex
$(C_n)_K$
```

## FR-EXAMPLES-012 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L2782)

Rétablit B_g dans cette phrase seulement. Les nombreuses autres localisations B_{g prime} sont présentes dans la source et ne sont pas touchées.

Avant :
```tex
$B_{g'}$ est de présentation finie sur $A$ si et seulement si le noyau
```
Après :
```tex
$B_g$ est de présentation finie sur $A$ si et seulement si le noyau
```

## FR-EXAMPLES-013 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L3122)

Rétablit l’anneau A du produit imprimé dans la formule ; R est le but de phi, mais remplacer A par R est un erratum de source.

Avant :
```tex
(\varphi(J)R)^2
```
Après :
```tex
(\varphi(J)A)^2
```

## FR-EXAMPLES-014 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L3237)

Rétablit le P majuscule imprimé dans le premier indice uniquement. Le p minuscule à droite et dans le triangle suivant reste officiel.

Avant :
```tex
$L_{A/\mathbb{F}_p} \simeq \Omega_{A/\mathbb{F}_p}[0]$
```
Après :
```tex
$L_{A/\mathbb{F}_P} \simeq \Omega_{A/\mathbb{F}_p}[0]$
```

## FR-EXAMPLES-015 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L4076)

Rétablit T majuscule dans le corps de base de cette phrase. Le torseur précédent utilise t ; cette discordance est de la source.

Avant :
```tex
$T = \Spec(\mathbf{F}_p(t))$
```
Après :
```tex
$T = \Spec(\mathbf{F}_p(T))$
```

## FR-EXAMPLES-016 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L4172)

Rétablit sur Z, imprimé après la description du produit fibré. Sur T est une correction cohérente du texte, mais non son libellé.

Avant :
```tex
est un schéma plat et affine sur $T$
```
Après :
```tex
est un schéma plat et affine sur $Z$
```

## FR-EXAMPLES-017 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L4268)

Rétablit Z_i dans cette clause, sans transformer la variable en Z_j pour la rendre cohérente avec n_j.

Avant :
```tex
Comme les $n_j$ sont déterminés par l'irréductibilité de $Z_j$
```
Après :
```tex
Comme les $n_j$ sont déterminés par l'irréductibilité de $Z_i$
```

## FR-EXAMPLES-018 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L4280)

Rétablit les deux indices i de l’anneau local intermédiaire officiel. Les indices i−1 étaient une correction de la chaîne, non une traduction.

Avant :
```tex
\mathcal{O}_{Z_{i - 1}, z_{i - 1}} \to
```
Après :
```tex
\mathcal{O}_{Z_i, z_i} \to
```

## FR-EXAMPLES-019 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L4281)

Rétablit z dans le dernier anneau local malgré le point t choisi juste avant.

Avant :
```tex
\mathcal{O}_{W_i, t}
```
Après :
```tex
\mathcal{O}_{W_i, z}
```

## FR-EXAMPLES-020 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L4340)

Rétablit la ligne entière : la source omet l’argument c à gauche et inverse f/g à droite. La déclaration de contravariance correcte de la phrase précédente reste inchangée. Les deux réparations silencieuses sont gardées dans l’avant/après.

Avant :
```tex
F(g \circ f)(c)(x, x') = c(g(f(x)), g(f(x'))) = F(f)(F(g)(c))(x, x')
```
Après :
```tex
F(g \circ f)(x, x') = c(g(f(x)), g(f(x'))) = F(g)(F(f)(c))(x, x')
```

## FR-EXAMPLES-021 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L5976)

Rétablit la parenthèse surnuméraire du témoin. Il s’agit d’une anomalie typographique officielle, non d’un théorème différent.

Avant :
```tex
$\mathcal{X} = \underline{\Mor}_S(X, [S/A])$
```
Après :
```tex
$\mathcal{X} = \underline{\Mor}_S(X, [S/A]))$
```

## FR-EXAMPLES-022 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L6114)

Rétablit x_0 dans cette phrase, sans remplacer le point imprimé par le nœud x introduit plus haut.

Avant :
```tex
les deux points au-dessus de $x$.
```
Après :
```tex
les deux points au-dessus de $x_0$.
```

## FR-EXAMPLES-023 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L6116)

Rétablit les accolades de groupement TeX de x prime, que la source n’échappe pas pour afficher un singleton. Ce défaut typographique est distingué d’une modification de la construction.

Avant :
```tex
$A_0 \times \{x'\}$
```
Après :
```tex
$A_0 \times {x'}$
```

## FR-EXAMPLES-024 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L6230)

Rétablit la lettre O de la phrase officielle, distincte du chiffre 0 employé dans le diagramme et pour U.

Avant :
```tex
$0_V \in V$
```
Après :
```tex
$O_V \in V$
```

## FR-EXAMPLES-025 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L6770)

Rétablit Spec(A prime) dans la conclusion ; Spec(B) était une correction du nom de l’anneau de valuation de cette partie de la preuve.

Avant :
```tex
Cela impliquerait que $\Spec(B)$ est non connexe
```
Après :
```tex
Cela impliquerait que $\Spec(A')$ est non connexe
```

## FR-EXAMPLES-026 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L6855)

Rétablit l’argument officiel avec les seuls nombres premiers 2 et 3. Le remplacement par tous les nombres premiers est une réécriture substantielle de la justification. L’identité officielle n’est pas validée mathématiquement : pour M=Z, 1/5 appartient déjà aux deux localisés sans appartenir à Z.

Avant :
```tex
L'égalité ci-dessus est donc claire, puisque $M = \bigcap_{p \in P} M_{(p)}$.
```
Après :
```tex
L'égalité ci-dessus est donc claire, puisque déjà $M_{(2)} \cap M_{(3)} = M$.
```

## FR-EXAMPLES-027 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L6963)

Rétablit I_A sans prime dans la phrase officielle ; la source de la projection vers le quotient M_A devrait être distinguée dans un erratum séparé.

Avant :
```tex
redonne l'application $I'_A \to M_A$
```
Après :
```tex
redonne l'application $I_A \to M_A$
```

## FR-EXAMPLES-028 — Erreur de traduction réparée

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L3260)

Prime qualifie la caractéristique dans la source. Positive seul permettrait une caractéristique composée pour un anneau ; première rétablit la restriction perdue. Décision directement motivée par les deux phrases anglaises, sans attestation externe nouvelle revendiquée.

Avant :
```tex
anneaux de caractéristique positive,
```
Après :
```tex
anneaux de caractéristique première,
```

## FR-EXAMPLES-029 — Erreur de traduction réparée

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L3263)

Prime qualifie la caractéristique dans la source. Positive seul permettrait une caractéristique composée pour un anneau ; première rétablit la restriction perdue. Décision directement motivée par les deux phrases anglaises, sans attestation externe nouvelle revendiquée.

Avant :
```tex
anneau $A$ de caractéristique positive est dit
```
Après :
```tex
anneau $A$ de caractéristique première est dit
```

## FR-EXAMPLES-030 — Erreur de traduction réparée

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L4123)

Rattache le recouvrement lisse aux champs, non aux espaces représentant leur diagonale. Le contexte source pose immédiatement la question d’un recouvrement lisse U vers le champ ; la syntaxe française publiée changeait le rattachement de la condition.

Avant :
```tex
champs en groupoïdes pour la topologie étale dont la diagonale est
représentable par des espaces algébriques admettant un recouvrement lisse.
```
Après :
```tex
champs en groupoïdes pour la topologie étale dont la diagonale est
représentable par des espaces algébriques et qui admettent un recouvrement lisse.
```

## FR-EXAMPLES-031 — Erreur de traduction réparée

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L6951)

Rétablit la condition p-power torsion entièrement omise en français. p-primaire reprend la décomposition en composantes p-primaires de la phrase immédiatement précédente. Il n’est pas ajouté de borne commune sur les puissances de p ; chaque élément peut avoir son propre exposant.

Avant :
```tex
qu'il existe, pour chaque $p$, des
$R$-modules $M_p$ tels que
```
Après :
```tex
qu'il existe des
$R$-modules $M_p$ de torsion $p$-primaire tels que
```

## Différences fidèles conservées

### `section-sheaves-locally-Noetherian`

Une seule définition est disposée sur deux lignes. La localité fppf porte toujours sur l’existence de racines de degré p à une puissance arbitrairement grande. Aucune base, variable, appartenance ou négation n’est modifiée. Cette exception ne normalise pas les autres environnements du chapitre. La preuve conserve la nilpotence du nilradical et la négation aucune racine non triviale, puis l’injectivité de la multiplication par p.

## Texte des formules vérifié

### `section-nonsplit-locally-split`

Premier qualifie p dans l’indice de la somme ; les flèches et les quatre termes de la suite restent identiques.

```tex
0 \to M \to \bigoplus\nolimits_{p\text{ prime}} \mathbf{Z}_{(p)} \to \mathbf{Q} \to 0
```
```tex
0 \to M \to \bigoplus\nolimits_{p\text{ premier}} \mathbf{Z}_{(p)} \to \mathbf{Q} \to 0
```

### `section-another-local-completion-nonreduced`

Tel que et pour tout gardent la portée de la condition sur chaque n supérieur ou égal à zéro ; la famille des coefficients et la finitude du degré sont inchangées.

```tex
A = \left\{ \begin{matrix} \sum a_{i, j} x^iy^j \in k[[x, y]] \text{ such that for all }n \geq 0 \text{ we have } \\ [k^p(a_{n, n}, a_{n, n + 1}, a_{n + 1, n}, a_{n, n + 2}, a_{n + 2, n}, \ldots) : k^p] < \infty \end{matrix} \right\}
```
```tex
A = \left\{ \begin{matrix} \sum a_{i, j} x^iy^j \in k[[x, y]] \text{ tel que, pour tout }n \geq 0 \text{ on ait } \\ [k^p(a_{n, n}, a_{n, n + 1}, a_{n + 1, n}, a_{n, n + 2}, a_{n + 2, n}, \ldots) : k^p] < \infty \end{matrix} \right\}
```

### `section-bad`

Le nom de l’invariant depth devient profondeur, sans changer A ni la borne 1. Contrôle de cette paire, non attestation externe de toute la terminologie.

```tex
\text{depth}(A) \geq 1
```
```tex
\text{profondeur}(A) \geq 1
```

### `section-bad`

Même nom profondeur, avec la borne 2 conservée ; aucune implication n’est substituée à une inégalité.

```tex
\text{depth}(A) \geq 2
```
```tex
\text{profondeur}(A) \geq 2
```

### `section-non-chevalley`

Points où et est non nul conservent la condition de non-annulation du produit y_j(t−1)…(t−j).

```tex
U_j = \text{points where }y_j(t - 1)(t - 2) ... (t - j)\text{ is nonzero}
```
```tex
U_j = \text{points où }y_j(t - 1)(t - 2) ... (t - j)\text{ est non nul}
```

### `section-non-chevalley`

Sont nuls et conserve la conjonction : tous les x_1,…,x_j sont nuls et y_j ne l’est pas. La négation n’est pas distribuée aux mauvais termes.

```tex
f(Z \cap U_j) = \text{points where }x_1, \ldots, x_j\text{ are zero and }y_j\text{ is nonzero}
```
```tex
f(Z \cap U_j) = \text{points où }x_1, \ldots, x_j\text{ sont nuls et }y_j\text{ est non nul}
```

### `section-nonfree`

Premier reste la condition sur p dans la somme des sous-groupes (1/p)Z de Q.

```tex
M = \sum_{p \text{ prime}} \frac{1}{p} \mathbf{Z} \subset \mathbf{Q}
```
```tex
M = \sum_{p \text{ premier}} \frac{1}{p} \mathbf{Z} \subset \mathbf{Q}
```

### `lemma-chow-group-product`

Et relie les deux définitions de limites inductives ; les indices n et i restent à leur place.

```tex
B_\infty = \colim_n B_n \quad\text{and}\quad L_{\infty, i} = \colim_n L_{n, i}
```
```tex
B_\infty = \colim_n B_n \quad\text{et}\quad L_{\infty, i} = \colim_n L_{n, i}
```

### `section-topology-finite-type`

Pour porte sur i supérieur ou égal à 1 ; le coefficient constant dans k est distingué des autres coefficients dans k((y)).

```tex
A = \{a_0 + a_1 x + a_2 x^2 + \ldots \mid a_0 \in k, a_i \in k((y)) \text{ for }i\geq 1\}
```
```tex
A = \{a_0 + a_1 x + a_2 x^2 + \ldots \mid a_0 \in k, a_i \in k((y)) \text{ pour }i\geq 1\}
```

### `section-topology-finite-type`

Pour porte sur i supérieur ou égal à 1 ; le coefficient constant dans k[y], et non dans k, reste distinct de ceux dans k((y)).

```tex
C = \{a_0 + a_1 x + a_2 x^2 + \ldots \mid a_0 \in k[y], a_i \in k((y)) \text{ for }i\geq 1\}.
```
```tex
C = \{a_0 + a_1 x + a_2 x^2 + \ldots \mid a_0 \in k[y], a_i \in k((y)) \text{ pour }i\geq 1\}.
```

### `lemma-not-algebraic`

Ensembles remplace le nom de catégorie Sets. Le foncteur reste contravariant sur les schémas.

```tex
F : \Sch^{opp} \to \textit{Sets}
```
```tex
F : \Sch^{opp} \to \textit{Ensembles}
```

### `section-sheaves`

Si… n’est pas une spécialisation… sinon garde exactement la négation, les deux cas et l’ordre x,x prime. Cette définition n’est pas confondue avec la composition défectueuse restaurée plus bas.

```tex
F(f)(b)(x, x') = \left\{ \begin{matrix} 0 & \text{if }x\text{ is not a specialization of }x' \\ b(f(x), f(x')) & \text{else.} \end{matrix} \right.
```
```tex
F(f)(b)(x, x') = \left\{ \begin{matrix} 0 & \text{si }x\text{ n'est pas une spécialisation de }x' \\ b(f(x), f(x')) & \text{sinon.} \end{matrix} \right.
```

### `section-constructible-functions`

Fonction constructible au numérateur et fonctions localement constantes au dénominateur conservent les deux conditions distinctes et les mêmes applications de |X| vers A.

```tex
F(X) = \frac{\{a : |X| \to A \mid a \text{ is a constructible function}\}}{\{\text{locally constant functions }|X| \to A\}}
```
```tex
F(X) = \frac{\{a : |X| \to A \mid a \text{ est une fonction constructible}\}}{\{\text{fonctions localement constantes }|X| \to A\}}
```

### `section-lisse-etale-not-functorial`

Égaliseur remplace Equalizer dans les deux membres ; les deux flèches et leurs changements de base ne changent pas. La variation terminologique égaliseur/égalisateur dans la prose n’est pas déclarée résolue ici.

```tex
u_s \text{Equalizer}(h_a, h_b : h_{V_1} \to h_{V_2}) = \text{Equalizer}(h_{a \times 1}, h_{b \times 1} : h_{V_1 \times_Y X} \to h_{V_2 \times_Y X})
```
```tex
u_s \text{Égaliseur}(h_a, h_b : h_{V_1} \to h_{V_2}) = \text{Égaliseur}(h_{a \times 1}, h_{b \times 1} : h_{V_1 \times_Y X} \to h_{V_2 \times_Y X})
```

### `section-interesting-compact`

Et relie les deux flèches de cohomologie ; les degrés −1 et 0 et les objets M,N restent inchangés.

```tex
H^{-1}(N) \to H^0(M) \quad\text{and}\quad H^0(M) \to H^0(N)
```
```tex
H^{-1}(N) \to H^0(M) \quad\text{et}\quad H^0(M) \to H^0(N)
```

### `section-nongraded-differential-graded`

Impair est la condition exacte sur i ; les exposants 1/2 et (i−1)/2 et le carré extérieur sont conservés.

```tex
\text{d}(a_0 + a_1t + \ldots +a_dt^d) = (\sum\nolimits_{i\text{ odd}} a_i^{1/2} t^{(i - 1)/2})^2\text{d}t
```
```tex
\text{d}(a_0 + a_1t + \ldots +a_dt^d) = (\sum\nolimits_{i\text{ impair}} a_i^{1/2} t^{(i - 1)/2})^2\text{d}t
```

### `section-nongraded-differential-graded`

Les trois si gardent séparés les cas n<0, n=0 et n=1, avec les mêmes espaces de sections et le même facteur de différentielles.

```tex
\Hom_\mathcal{A}^n((\mathcal{F}, \nabla_\mathcal{F}), (\mathcal{G}, \nabla_\mathcal{G})) = \left\{ \begin{matrix} 0 & \text{if} & n < 0 \\ \Gamma(C, \mathcal{N}^{\otimes 2}) & \text{if} & n = 0 \\ \Gamma(C, \mathcal{N}^{\otimes 2} \otimes \Omega_{C/k}) & \text{if} & n = 1 \end{matrix} \right.
```
```tex
\Hom_\mathcal{A}^n((\mathcal{F}, \nabla_\mathcal{F}), (\mathcal{G}, \nabla_\mathcal{G})) = \left\{ \begin{matrix} 0 & \text{si} & n < 0 \\ \Gamma(C, \mathcal{N}^{\otimes 2}) & \text{si} & n = 0 \\ \Gamma(C, \mathcal{N}^{\otimes 2} \otimes \Omega_{C/k}) & \text{si} & n = 1 \end{matrix} \right.
```

### `section-Grothendieck-existence`

Support propre sur A rend la restriction support proper over A, sans affirmer que tout X est propre.

```tex
\textit{Coh}_{\text{support proper over } A}(X, \mathcal{I})
```
```tex
\textit{Coh}_{\text{support propre sur } A}(X, \mathcal{I})
```

### `lemma-affine-formal-functions-do-not-separate-points`

Image de… dans garde le même élément xi_u et le même module M_i.

```tex
x_u \epsilon_{i, u} = \text{image of }\xi_u\text{ in }M_i
```
```tex
x_u \epsilon_{i, u} = \text{image de }\xi_u\text{ dans }M_i
```

### `proposition-quotient-by-torsion-modules`

N’est pas un diviseur de zéro conserve la négation ; le sous-ensemble de A n’est pas remplacé par l’ensemble des diviseurs de zéro.

```tex
S = \{f \in A \mid f \text{ is not a zerodivisor in }A\}
```
```tex
S = \{f \in A \mid f \text{ n'est pas un diviseur de zéro dans }A\}
```

### `section-colimit-topology`

Les deux occurrences ouvert maintiennent l’équivalence et le quantificateur pour tout n.

```tex
U \subset G\text{ open} \Leftrightarrow G_n \cap U\text{ open }\forall n
```
```tex
U \subset G\text{ ouvert} \Leftrightarrow G_n \cap U\text{ ouvert }\forall n
```

### `section-colimit-topology`

Tels que et pour gardent la condition stricte sur |x_j| pour j>0, avec le rôle distinct de x_0.

```tex
U = \{(x_0, x_1, x_2, \ldots)\text{ such that } |x_j| < |\cos(jx_0)| \text{ for } j > 0\}
```
```tex
U = \{(x_0, x_1, x_2, \ldots)\text{ tels que } |x_j| < |\cos(jx_0)| \text{ pour } j > 0\}
```

### `section-canonical`

Égaliseur remplace Equalizer ; les indices A,B dans U et les localisations au-dessus de A union B sont conservés.

```tex
M = \text{Equalizer}\left( \xymatrix{ \prod\nolimits_{A \in U} M_A \ar@<1ex>[r] \ar@<-1ex>[r] & \prod\nolimits_{A, B \in U} M_{A \cup B} } \right)
```
```tex
M = \text{Égaliseur}\left( \xymatrix{ \prod\nolimits_{A \in U} M_A \ar@<1ex>[r] \ar@<-1ex>[r] & \prod\nolimits_{A, B \in U} M_{A \cup B} } \right)
```

### `section-canonical`

Dans garde le module ambiant M_P=M tensoriel Q pour l’intersection ; aucune borne n’est ajoutée.

```tex
M = \bigcap\nolimits_{A \in U} M_A\text{ inside }M_P = M \otimes \mathbf{Q}
```
```tex
M = \bigcap\nolimits_{A \in U} M_A\text{ dans }M_P = M \otimes \mathbf{Q}
```

### `lemma-non-fpqc-descent`

Égaliseur remplace Equalizer ; les produits indexés par i puis i,j et tous les produits tensoriels sur A sont inchangés.

```tex
M = \text{Equalizer}\left( \xymatrix{ \prod\nolimits_{i \in I} M \otimes_A A_i \ar@<1ex>[r] \ar@<-1ex>[r] & \prod\nolimits_{i, j \in I} M \otimes_A A_i \otimes_A A_j } \right)
```
```tex
M = \text{Égaliseur}\left( \xymatrix{ \prod\nolimits_{i \in I} M \otimes_A A_i \ar@<1ex>[r] \ar@<-1ex>[r] & \prod\nolimits_{i, j \in I} M \otimes_A A_i \otimes_A A_j } \right)
```

## Limites

Chaque contexte modifié et chaque différence conservée ci-dessus a été lu dans les deux langues. Les contrôles sur tous les blocs étiquetés ne certifient pas l’intégralité de la prose ni de la terminologie. Les anomalies du témoin officiel restaurées ne sont pas présentées comme mathématiquement correctes. L’inversion des opérations reproduit exactement la version publique. La construction et la vérification publique du lecteur complet restent à effectuer.
