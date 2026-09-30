# Variétés : restauration de fidélité et réparation du français

**LaTeX local corrigé seulement. Le PDF et l’édition publique ne sont pas encore remplacés.**

[LaTeX](staged/fr/033_varieties.fr.tex) · [Validation](VARIETIES_FR_VALIDATION.json) · [Avant/après et contextes complets](VARIETIES_FR_REPAIRS.json) · [Canon consulté](VARIETIES_FR_CONSULTED_CANON.json)

Deux formules sont remises dans leur état officiel, même problématique. Les autres changements réparent la traduction, notamment des variables d remplacées par une et des mots français corrompus. Leur cause historique n’est pas attribuée sans preuve. Le décompte porte sur des opérations exactes, non sur autant de théorèmes.

La terminologie entier sur et corps des fractions de a été vérifiée rétrospectivement dans [le cours de Patrick Massot](https://www.imo.universite-paris-saclay.fr/~patrick.massot/enseignement/poly_alg/cha-extensions.html), définition 7.1.1 et remarque 7.1.4. Ce contrôle limité ne vaut pas consultation de tout le canon ni preuve d’une consultation par le traducteur initial.

## FR-VARIETIES-001 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L65)

Rétablit le mot français cadre dans une phrase décrivant la plus grande généralité ; aucune hypothèse ne change.

Avant :
```tex
caunere
```
Après :
```tex
cadre
```

## FR-VARIETIES-002 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L67)

Répare l’article corrompu ; la négation est conservée.

Avant :
```tex
nécessairement d variété non
```
Après :
```tex
nécessairement une variété non
```

## FR-VARIETIES-003 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L75)

Répare l’article sans modifier la non-irréductibilité de cet exemple.

Avant :
```tex
n'est pas d variété
```
Après :
```tex
n'est pas une variété
```

## FR-VARIETIES-004 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L92)

Répare l’article du lemme ; la condition de clôture algébrique reste inchangée.

Avant :
```tex
est d variété sur $k$
```
Après :
```tex
est une variété sur $k$
```

## FR-VARIETIES-005 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L121)

une_j n’est pas la variable définie dans le texte : d_j rétablit exactement le facteur source.

Avant :
```tex
c_j \otimes une_j
```
Après :
```tex
c_j \otimes d_j
```

## FR-VARIETIES-006 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L128)

Répare le nom propre, avec la même référence au théorème des zéros.

Avant :
```tex
Hqubert
```
Après :
```tex
Hilbert
```

## FR-VARIETIES-007 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L136)

Rétablit la même variable d_j après passage aux classes résiduelles ; ne change pas la formule officielle.

Avant :
```tex
\overline{c}_j une_j
```
Après :
```tex
\overline{c}_j d_j
```

## FR-VARIETIES-008 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L139)

Répare le mot familles dans l’argument d’indépendance linéaire.

Avant :
```tex
famqules
```
Après :
```tex
familles
```

## FR-VARIETIES-009 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L125)

Rétablit les deux bornes de la famille déjà définie d_1,...,d_m, non une nouvelle famille.

Avant :
```tex
et $une_1, \ldots, une_m$, ainsi que
```
Après :
```tex
et $d_1, \ldots, d_m$, ainsi que
```

## FR-VARIETIES-010 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L185)

Répare l’article ; l’unicité et la dominance ne changent pas.

Avant :
```tex
unique d application
```
Après :
```tex
unique une application
```

## FR-VARIETIES-011 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L190)

Répare le pronom et l’article sans changer le quantificateur existentiel.

Avant :
```tex
qu existe d $k$-algèbre
```
Après :
```tex
il existe une $k$-algèbre
```

## FR-VARIETIES-012 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L192)

Répare l’article. Le mot équivalente de l’énoncé reste celui de la source ; aucune anti-équivalence n’est ajoutée.

Avant :
```tex
$X = \Spec(A)$ est d variété
```
Après :
```tex
$X = \Spec(A)$ est une variété
```

## FR-VARIETIES-013 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L239)

Répare l’article ; le changement de corps et la platitude restent exacts.

Avant :
```tex
Soit $K/k$ d extension
```
Après :
```tex
Soit $K/k$ une extension
```

## FR-VARIETIES-014 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L379)

Et de rattachait à tort l’isomorphisme à au-dessus de. La source énonce une conjonction : le point existe et on a l’isomorphisme affiché.

Avant :
```tex
au-dessus de $x$ et de
```
Après :
```tex
au-dessus de $x$ et on a
```

## FR-VARIETIES-015 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L640)

Rétablit la restriction française ne...que portant sur le nombre fini de composantes.

Avant :
```tex
n'ait il'un nombre
```
Après :
```tex
n'ait qu'un nombre
```

## FR-VARIETIES-016 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L2612)

Localise le texte anglais resté dans la formule. Corps des fractions est attesté dans la remarque 7.1.4 du cours de Massot ; les anneaux et indices sont inchangés.

Avant :
```tex
\text{fraction field of }
```
Après :
```tex
\text{corps des fractions de }
```

## FR-VARIETIES-017 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L2614)

Entier sur est la propriété d’un élément annulé par un polynôme unitaire, attestée dans la définition 7.1.1 de Massot. Il ne s’agit ni d’une intégrale ni du caractère intègre de l’anneau.

Avant :
```tex
est intégral sur
```
Après :
```tex
est entier sur
```

## FR-VARIETIES-018 — official_source_reading_restoration

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L6264)

Rétablit X prime, symbole effectivement imprimé, au lieu de le remplacer silencieusement par le changement de base. Le témoin n’y définit pas X prime : cette difficulté source reste déclarée, non corrigée dans la traduction de base.

Avant :
```tex
\chi(X_{k'}, \mathcal{F}')
```
Après :
```tex
\chi(X', \mathcal{F}')
```

## FR-VARIETIES-019 — official_source_reading_restoration

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L6374)

La première ligne porte littéralement A puissance n, bien que les n+1 coordonnées et la suite emploient A puissance n+1. On conserve la discordance officielle et les occurrences suivantes n+1 ; on ne valide pas mathématiquement cette coquille.

Avant :
```tex
\mathbf{A}^{n + 1} = \Spec(k[x_0, \ldots, x_n])
```
Après :
```tex
\mathbf{A}^n = \Spec(k[x_0, \ldots, x_n])
```

## FR-VARIETIES-020 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L6368)

Accorde le verbe avec les deux sous-ensembles X et Y ; ne modifie aucune hypothèse.

Avant :
```tex
$X, Y \subset \mathbf{P}^n_k$ soit
```
Après :
```tex
$X, Y \subset \mathbf{P}^n_k$ soient
```

## FR-VARIETIES-021 — translation_specific_repair

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/varieties.tex#L6401)

Le pluriel français distingue les deux adhérences, déjà notées séparément dans la source. Les espaces ambiants et la formule suivante sont conservés.

Avant :
```tex
soient l'adhérence de $V$ et $W$
```
Après :
```tex
soient les adhérences de $V$ et $W$
```

## Différences conservées

### `definition-variety`

Le pronom relatif qui reprend le schéma X ; aucune hypothèse d’intégrité n’est perdue.

### `lemma-product-varieties`

De même pour la seconde famille reprend linéairement indépendants sur k dans B. Les deux classes résiduelles et les deux coefficients sont séparés par et sans changement. Un idéal maximal dans D(a_1c_1) désigne le même point du spectre : A est fixé dans la phrase précédente et dans A/m=k. Cette formulation française conserve l’identification usuelle d’un idéal premier avec le point correspondant, sans nouveau critère. Les quatre variables corrompues sont réparées séparément.

### `theorem-varieties-rational-maps`

Dont K est le corps des fractions reprend exactement l’algèbre A précédente ; la seconde occurrence symbolique de A n’est pas nécessaire en français.

### `lemma-finite-extension-geometrically-reduced`

Ses composantes reprend X, et chacun reprend les corps (K_i tensor k prime)_red. Le quantificateur pour chaque i et la séparabilité restent explicites.

### `example-geometrically-reduced-not-normal`

Un seul élément traduit exactement 1 élément ; le générateur y reste nommé. Les deux termes de langue sont corrigés séparément, sans changer l’élément ni son carré.

### `definition-embedding-dimension`

L’environnement aligned répartit la même chaîne de deux égalités sur plusieurs lignes ; il ne change ni le corps de base ni la complétion. Les trois expressions de dimension sont lues ensemble.

## Texte dans les formules

### `example-geometrically-reduced-not-normal`

Fermé et extension finie séparable gardent les deux conditions sur x et son corps résiduel.

```tex
\frac{y}{x - t'} \in (\text{fraction field of }\mathcal{O}_{V', v'_0})
```
```tex
\frac{y}{x - t'} \in (\text{corps des fractions de }\mathcal{O}_{V', v'_0})
```

### `lemma-smooth-separable-closed-points-dense`

Corps des fractions de localise l’expression anglaise, sans changer la fraction, l’anneau local ou ses indices.

```tex
\{x \in X\text{ closed such that }k \subset \kappa(x) \text{ is finite separable}\}
```
```tex
\{x \in X\text{ fermé tel que }k \subset \kappa(x) \text{ est finie séparable}\}
```

### `lemma-kunneth`

Et conserve les deux flèches de complexes de Čech et leurs projections.

```tex
\check{\mathcal{C}}^\bullet(\mathcal{U}, \mathcal{F}) \to \check{\mathcal{C}}^\bullet(\mathcal{W}, \text{pr}_1^*\mathcal{F}) \quad\text{and}\quad \check{\mathcal{C}}^\bullet(\mathcal{V}, \mathcal{G}) \to \check{\mathcal{C}}^\bullet(\mathcal{W}, \text{pr}_2^*\mathcal{G})
```
```tex
\check{\mathcal{C}}^\bullet(\mathcal{U}, \mathcal{F}) \to \check{\mathcal{C}}^\bullet(\mathcal{W}, \text{pr}_1^*\mathcal{F}) \quad\text{et}\quad \check{\mathcal{C}}^\bullet(\mathcal{V}, \mathcal{G}) \to \check{\mathcal{C}}^\bullet(\mathcal{W}, \text{pr}_2^*\mathcal{G})
```

### `lemma-automorphism`

Fermé et premier à n gardent les deux conditions et le degré du même corps résiduel.

```tex
S = \{x \in X\text{ closed such that }[\kappa(g(x)) : k] \text{ is prime to }n\}
```
```tex
S = \{x \in X\text{ fermé tel que }[\kappa(g(x)) : k] \text{ est premier à }n\}
```

### `lemma-degree-on-proper-curve`

Longueur désigne le même invariant du même anneau local.

```tex
m_i = \text{length}_{\mathcal{O}_{X, \xi_i}} \mathcal{O}_{X, \xi_i}
```
```tex
m_i = \text{longueur}_{\mathcal{O}_{X, \xi_i}} \mathcal{O}_{X, \xi_i}
```

### `lemma-degree-in-terms-of-components`

Les deux longueurs, la dimension de F et l’égalité r+m prime restent dans le même ordre.

```tex
m = \text{length}_{\mathcal{O}_{X, \xi}} \mathcal{O}_{X, \xi} = \dim_{\kappa(\xi)} \mathcal{F}_\xi + \text{length}_{\mathcal{O}_{X', \xi}} \mathcal{O}_{X', \xi} = r + m'
```
```tex
m = \text{longueur}_{\mathcal{O}_{X, \xi}} \mathcal{O}_{X, \xi} = \dim_{\kappa(\xi)} \mathcal{F}_\xi + \text{longueur}_{\mathcal{O}_{X', \xi}} \mathcal{O}_{X', \xi} = r + m'
```

### `lemma-degree-tensor-product`

Les deux rangs et les deux degrés restent couplés aux mêmes fibrés.

```tex
\deg(\mathcal{E} \otimes \mathcal{V}) = \text{rank}(\mathcal{E}) \deg(\mathcal{V}) + \text{rank}(\mathcal{V}) \deg(\mathcal{E})
```
```tex
\deg(\mathcal{E} \otimes \mathcal{V}) = \text{rang}(\mathcal{E}) \deg(\mathcal{V}) + \text{rang}(\mathcal{V}) \deg(\mathcal{E})
```

### `lemma-numerical-polynomial-leading-term`

Longueur conserve le même module F au même point générique xi_i.

```tex
m_i = \text{length}_{\mathcal{O}_{X, \xi_i}}(\mathcal{F}_{\xi_i})
```
```tex
m_i = \text{longueur}_{\mathcal{O}_{X, \xi_i}}(\mathcal{F}_{\xi_i})
```

### `lemma-numerical-polynomial-leading-term`

Longueur conserve le module F au point générique xi de Z.

```tex
m_Z = \text{length}_{\mathcal{O}_{X, \xi}}(\mathcal{F}_\xi)
```
```tex
m_Z = \text{longueur}_{\mathcal{O}_{X, \xi}}(\mathcal{F}_\xi)
```

### `lemma-intersection-number-in-terms-of-components`

Longueur garde le module O_Z au point xi_i sur le même anneau local.

```tex
m_i = \text{length}_{\mathcal{O}_{X, \xi_i}}(\mathcal{O}_{Z, \xi_i})
```
```tex
m_i = \text{longueur}_{\mathcal{O}_{X, \xi_i}}(\mathcal{O}_{Z, \xi_i})
```

### `definition-degree`

Autres termes n’ajoute aucun coefficient ou restriction au développement polynomial.

```tex
(n_1 + \ldots + n_{\dim(Z)})^{\dim(Z)} = \dim(Z)!\ n_1 \ldots n_{\dim(Z)} + \text{other terms}
```
```tex
(n_1 + \ldots + n_{\dim(Z)})^{\dim(Z)} = \dim(Z)!\ n_1 \ldots n_{\dim(Z)} + \text{autres termes}
```

### `lemma-bertini`

Singulier en x conserve le même critère d’appartenance au carré de l’idéal maximal.

```tex
H_v\text{ singular at }x \Leftrightarrow \psi(v)_x \in \mathfrak m_x^2\mathcal{L}_x
```
```tex
H_v\text{ est singulier en }x \Leftrightarrow \psi(v)_x \in \mathfrak m_x^2\mathcal{L}_x
```

### `lemma-vanishin-h1-negative`

Profondeur garde l’inégalité >=2 sur F_x.

```tex
\text{depth}(\mathcal{F}_x) \geq 2
```
```tex
\text{profondeur}(\mathcal{F}_x) \geq 2
```

### `lemma-vanishin-h1-negative`

Et garde côte à côte le même faisceau G et O(1), sans modifier les puissances.

```tex
\mathcal{G} = i_*(\mathcal{F} \oplus \mathcal{F} \otimes \mathcal{L} \oplus \ldots \oplus \mathcal{F} \otimes \mathcal{L}^{\otimes e - 1}) \quad\text{and}\quad \mathcal{O}(1)
```
```tex
\mathcal{G} = i_*(\mathcal{F} \oplus \mathcal{F} \otimes \mathcal{L} \oplus \ldots \oplus \mathcal{F} \otimes \mathcal{L}^{\otimes e - 1}) \quad\text{et}\quad \mathcal{O}(1)
```

### `lemma-vanishin-h1-negative`

Profondeur conserve la valeur infinie au point y.

```tex
\text{depth}(\mathcal{G}_y) = \infty
```
```tex
\text{profondeur}(\mathcal{G}_y) = \infty
```

### `lemma-vanishin-h1-negative`

Les deux profondeurs conservent la même égalité.

```tex
\text{depth}(\mathcal{G}_y) = \text{depth}(\mathcal{F}_x)
```
```tex
\text{profondeur}(\mathcal{G}_y) = \text{profondeur}(\mathcal{F}_x)
```

### `lemma-vanishin-h1-negative`

Profondeur conserve la borne >=1 et l’indice x.

```tex
\text{depth}(\mathcal{G}_x) \geq 1
```
```tex
\text{profondeur}(\mathcal{G}_x) \geq 1
```

### `lemma-vanishin-h1-negative`

Les profondeurs après extension du corps gardent la même égalité et la même inégalité.

```tex
\text{depth}(\mathcal{F}_{x_K}) = \text{depth}(\mathcal{F}_x \otimes_{\mathcal{O}_{X, x}} \mathcal{O}_{X_K, x_K}) \geq \text{depth}(\mathcal{F}_x)
```
```tex
\text{profondeur}(\mathcal{F}_{x_K}) = \text{profondeur}(\mathcal{F}_x \otimes_{\mathcal{O}_{X, x}} \mathcal{O}_{X_K, x_K}) \geq \text{profondeur}(\mathcal{F}_x)
```

### `lemma-connectedness-ample-divisor`

Profondeur de l’anneau local garde la borne >=2.

```tex
\text{depth}(\mathcal{O}_{X, x}) \geq 2
```
```tex
\text{profondeur}(\mathcal{O}_{X, x}) \geq 2
```

## Limites

Tous les candidats de formules de ce chapitre sont ici expliqués, mais toute la prose n’a pas été relue. Les dix familles d’identifiants et de renvois sont égales ; la seule paire begin/end supplémentaire est aligned pour la mise en page. Le témoin officiel, le témoin public et leur provenance sont inchangés. Chaque réparation est inversible et l’inversion reproduit exactement tous les octets du témoin public. Aucun avis humain ni approbation générale n’est revendiqué.
