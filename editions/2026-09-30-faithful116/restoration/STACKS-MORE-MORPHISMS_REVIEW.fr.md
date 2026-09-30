# Compléments sur les morphismes de champs : fidélité au témoin officiel

**LaTeX local ; aucune édition publique corrigée à ce stade.**

[LaTeX](staged/fr/106_stacks-more-morphisms.fr.tex) · [Contrôles](STACKS-MORE-MORPHISMS_FR_VALIDATION.json) · [Contextes complets](STACKS-MORE-MORPHISMS_FR_REPAIRS.json)

Les sens de flèches, bases, objets et formulations ci-dessous sont ramenés au texte anglais officiel. Les renvois et diagrammes ne sont pas harmonisés avec les anomalies ainsi restaurées. Les propositions de correction restent consultables dans les comparaisons avant/après, séparément de la traduction de base. Les renommages et explicitations équivalentes sont distingués des modifications mathématiques substantielles.

## FR-STACKS-MORE-MORPHISMS-001 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L695)

Rétablit le sens de la flèche entre objets imprimé avant le diagramme. Ce sens est incohérent avec le diagramme suivant, qui demeure inchangé ; sa correction ne relève pas de la traduction de base.

Avant :
```tex
(V, V', b, j, y', \beta) \to (U, U', a, i, x', \alpha)
```
Après :
```tex
(U, U', a, i, x', \alpha) \to (V, V', b, j, y', \beta)
```

## FR-STACKS-MORE-MORPHISMS-002 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L697)

Rétablit le sens donné à f dans la même définition.

Avant :
```tex
$f : V \to U$
```
Après :
```tex
$f : U \to V$
```

## FR-STACKS-MORE-MORPHISMS-003 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L698)

Rétablit le sens donné à f prime dans la même définition.

Avant :
```tex
$f' : V' \to U'$
```
Après :
```tex
$f' : U' \to V'$
```

## FR-STACKS-MORE-MORPHISMS-004 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L699)

Rétablit U comme domaine de restriction imprimé, avec les autres lectures de cette définition.

Avant :
```tex
à $V$ donne $f$
```
Après :
```tex
à $U$ donne $f$
```

## FR-STACKS-MORE-MORPHISMS-005 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L755)

Rétablit U vers V dans le seul premier cas de la preuve. Le morphisme V vers U considéré au paragraphe suivant reste inchangé.

Avant :
```tex
tel que $f : V \to U$
```
Après :
```tex
tel que $f : U \to V$
```

## FR-STACKS-MORE-MORPHISMS-006 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L1008)

Rétablit le sens officiel du 2-morphisme gamma_k de l’énoncé. La construction ultérieure du 2-morphisme universel de sens inverse reste telle qu’elle est imprimée.

Avant :
```tex
$\gamma_k : x' \circ f'_k \to x'' \circ f''_k$
```
Après :
```tex
$\gamma_k : x'' \circ f''_k \to x' \circ f'_k$
```

## FR-STACKS-MORE-MORPHISMS-007 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L1020)

Rétablit i prime dans la première description de delta, malgré i sans prime défini auparavant.

Avant :
```tex
$\delta : x' \circ i \to x'' \circ i''$
```
Après :
```tex
$\delta : x' \circ i' \to x'' \circ i''$
```

## FR-STACKS-MORE-MORPHISMS-008 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L1037)

Rétablit i prime dans la seconde composition, alors que i double prime était le nom donné initialement.

Avant :
```tex
soient respectivement $i : W \to W'$ et $i'' : W \to W''$
```
Après :
```tex
soient respectivement $i : W \to W'$ et $i' : W \to W''$
```

## FR-STACKS-MORE-MORPHISMS-009 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L1044)

Retire l’argument W ajouté à l’image inverse incomplète du témoin. Le dossier conserve l’argument proposé ; la formule incomplète n’est pas certifiée correcte.

Avant :
```tex
$W_k = (f'_k)^{-1}(W)$
```
Après :
```tex
$W_k = (f'_k)^{-1}$
```

## FR-STACKS-MORE-MORPHISMS-010 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L1156)

Rétablit W prime, non U prime, dans la justification de la lissité de p prime. U prime était la correction cohérente avec le produit fibré défini plus haut.

Avant :
```tex
Puisque $U' \to \mathcal{X}'$ est lisse
```
Après :
```tex
Puisque $W' \to \mathcal{X}'$ est lisse
```

## FR-STACKS-MORE-MORPHISMS-011 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L1262)

Rétablit l’écriture littérale sans caractère de sous-indice après la barre. Il s’agit d’une normalisation de notation retirée, non d’un théorème distinct.

Avant :
```tex
$\delta'_i|_U = \Delta_U$
```
Après :
```tex
$\delta'_i|U = \Delta_U$
```

## FR-STACKS-MORE-MORPHISMS-012 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L1787)

Rétablit l’ordre et la base du produit fibré imprimé dans cette restriction. Le produit correctement typé proposé reste visible dans le dossier.

Avant :
```tex
$x|_{T \times_{T'} W'}$
```
Après :
```tex
$x|_{T \times_{W'} T'}$
```

## FR-STACKS-MORE-MORPHISMS-013 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L2197)

Rétablit le nom s_ij utilisé par cette phrase officielle, sans le remplacer tacitement par le phi_ij défini avant elle.

Avant :
```tex
$p_{ij} : Y_{ij} \to Y$ tels que $\varphi_{ij}$
```
Après :
```tex
$p_{ij} : Y_{ij} \to Y$ tels que $s_{ij}$
```

## FR-STACKS-MORE-MORPHISMS-014 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L2227)

Rétablit W_j dans le but imprimé de I_ik ; le remplacement par W_k corrigeait une discordance d’indices.

Avant :
```tex
$I_{ik} \to W_i \cap W_k$
```
Après :
```tex
$I_{ik} \to W_i \cap W_j$
```

## FR-STACKS-MORE-MORPHISMS-015 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L3365)

Rétablit U dans le produit définissant ici R prime, au lieu de lui substituer R pour corriger l’identification du groupoïde.

Avant :
```tex
$R' = M' \times_M R$
```
Après :
```tex
$R' = M' \times_M U$
```

## FR-STACKS-MORE-MORPHISMS-016 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L3723)

Rétablit M sans indice dans ce changement de base, bien que M_i soit le but du morphisme considéré. Aucun autre M_i n’est altéré.

Avant :
```tex
un morphisme $M' \to M_i$
```
Après :
```tex
un morphisme $M' \to M$
```

## FR-STACKS-MORE-MORPHISMS-017 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L4131)

Rétablit I comme nom local de l’espace d’isomorphismes. Le renommage cohérent en J évitait un conflit avec l’ensemble d’indices I, sans changer le raisonnement ; il est distingué des erreurs mathématiques.

Avant :
```tex
$J = \mathit{Isom}(x, y)$
```
Après :
```tex
$I = \mathit{Isom}(x, y)$
```

## FR-STACKS-MORE-MORPHISMS-018 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L4132)

Rétablit I comme nom local de l’espace d’isomorphismes. Le renommage cohérent en J évitait un conflit avec l’ensemble d’indices I, sans changer le raisonnement ; il est distingué des erreurs mathématiques.

Avant :
```tex
de sections de $J$ sur
```
Après :
```tex
de sections de $I$ sur
```

## FR-STACKS-MORE-MORPHISMS-019 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L4333)

Retire la borne i dans I explicitée seulement dans cette union. Les mêmes indices figurent plus loin ; l’explicitation n’était pas une erreur de contenu.

Avant :
```tex
$\mathcal{F}' = \bigcup_{i \in I} \mathcal{F}'_i$
```
Après :
```tex
$\mathcal{F}' = \bigcup \mathcal{F}'_i$
```

## FR-STACKS-MORE-MORPHISMS-020 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L4401)

Rétablit kappa(r) dans le diagramme malgré a dans la phrase qui le précède. Les occurrences kappa(a) hors de ces deux étiquettes restent inchangées.

Avant :
```tex
\ar[d]_{\kappa(a) \otimes 1}
```
Après :
```tex
\ar[d]_{\kappa(r) \otimes 1}
```

## FR-STACKS-MORE-MORPHISMS-021 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L4402)

Rétablit kappa(r) dans le diagramme malgré a dans la phrase qui le précède. Les occurrences kappa(a) hors de ces deux étiquettes restent inchangées.

Avant :
```tex
\ar[d]^{\kappa(a)}
```
Après :
```tex
\ar[d]^{\kappa(r)}
```

## FR-STACKS-MORE-MORPHISMS-022 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L4394)

Rétablit map par application à cet endroit. La qualification d’homomorphisme d’anneaux pouvait se déduire du contexte, mais était ajoutée à cette phrase ; la conclusion finale qui dit ring map demeure un homomorphisme d’anneaux.

Avant :
```tex
Remarquons que nous avons un homomorphisme d'anneaux
```
Après :
```tex
Remarquons que nous avons une application
```

## FR-STACKS-MORE-MORPHISMS-023 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L4409)

Rétablit map par application à cet endroit. La qualification d’homomorphisme d’anneaux pouvait se déduire du contexte, mais était ajoutée à cette phrase ; la conclusion finale qui dit ring map demeure un homomorphisme d’anneaux.

Avant :
```tex
Il s'ensuit que l'on obtient un homomorphisme d'anneaux
```
Après :
```tex
Il s'ensuit que l'on obtient une application
```

## FR-STACKS-MORE-MORPHISMS-024 — Erreur de traduction réparée

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L3303)

Harmonise la construction grammaticale après Supposons que avec soient dans la proposition coordonnée précédente. Les deux hypothèses restent exactement les mêmes ; il ne s’agit pas d’un erratum de la source.

Avant :
```tex
que $h$ est \'etale et que $h$ induit
```
Après :
```tex
que $h$ soit \'etale et que $h$ induise
```

## FR-STACKS-MORE-MORPHISMS-025 — Erreur de traduction réparée

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-more-morphisms.tex#L3639)

Emploie soit après Supposons que ; la finitude du même morphisme n’est ni ajoutée ni retirée.

Avant :
```tex
$\mathcal{I}_\mathcal{X} \to \mathcal{X}$ est fini.
```
Après :
```tex
$\mathcal{I}_\mathcal{X} \to \mathcal{X}$ soit fini.
```

## Différences fidèles conservées

### `lemma-etale-local-lifts-isomorphic`

W_k prime et W prime indice k composent exactement le même symbole TeX : la position du prime par rapport au sous-indice est sans effet. La lecture de tout le contexte n’indique aucun changement d’objet.

### `lemma-sheaf-of-infinitesimal-lifts`

La virgule ajoutée après les points de suspension sépare le même dernier indice n ; elle ne modifie ni la famille ni sa borne.

### `lemma-make-section`

La virgule après les points de suspension de l’indice d’union ne change aucun ouvert ni la borne n. Les autres écarts du bloc font l’objet des deux restaurations explicites.

### `definition-categorical-quotient`

Le f explicite répare une ellipse grammaticale de We say is a, dans la quatrième clause parallèle aux trois précédentes. Aucun nouvel objet n’est introduit : le même morphisme f a été fixé au début. La phrase française complète est conservée, sans qualifier cela de nouvel énoncé.

## Texte des formules vérifié

### `equation-morphism`

Espaces traduit le nom de la catégorie Spaces ; le même champ X prime reste sa base.

```tex
\textit{Spaces}/\mathcal{X}'
```
```tex
\textit{Espaces}/\mathcal{X}'
```

### `lemma-sheaf-of-infinitesimal-lifts`

Relèvements de… à B prime, modulo isomorphismes, conserve l’objet restreint à B prime tensorisé sur A prime avec A et la même relation d’équivalence.

```tex
F : B' \longmapsto \{\text{lifts of }x|_{B' \otimes_{A'} A}\text{ to } B'\}/\text{isomorphisms}
```
```tex
F : B' \longmapsto \{\text{relèvements de }x|_{B' \otimes_{A'} A}\text{ à } B'\}/\text{isomorphismes}
```

### `lemma-flatten-stack`

Et relie les deux carrés, avec s et t aux mêmes positions ; aucun morphisme du diagramme ne change.

```tex
\vcenter{ \xymatrix{ R' \ar[r] \ar[d] & R_{Y'} \ar[d]^{s_{Y'}} \\ U' \ar[r] & U_{Y'} } } \quad\text{and}\quad \vcenter{ \xymatrix{ R' \ar[r] \ar[d] & R_{Y'} \ar[d]^{t_{Y'}} \\ U' \ar[r] & U_{Y'} } }
```
```tex
\vcenter{ \xymatrix{ R' \ar[r] \ar[d] & R_{Y'} \ar[d]^{s_{Y'}} \\ U' \ar[r] & U_{Y'} } } \quad\text{et}\quad \vcenter{ \xymatrix{ R' \ar[r] \ar[d] & R_{Y'} \ar[d]^{t_{Y'}} \\ U' \ar[r] & U_{Y'} } }
```

### `lemma-make-section`

Et relie les deux types de paires de l’induction. Les intersections, produits fibrés et indices de 1 à n restent intacts.

```tex
(\mathcal{X} \to Y, W_1 \cap \ldots \cap W_n \cap V) \quad\text{and}\quad (\mathcal{X} \times_Y Y_i \to Y_i, V \cap Y_i),\quad i = 1, \ldots, n
```
```tex
(\mathcal{X} \to Y, W_1 \cap \ldots \cap W_n \cap V) \quad\text{et}\quad (\mathcal{X} \times_Y Y_i \to Y_i, V \cap Y_i),\quad i = 1, \ldots, n
```

### `lemma-refined-valuative-criterion-separated`

Et relie le morphisme U vers X et la diagonale relative à Y, sans changer leur relation logique.

```tex
\mathcal{U} \to \mathcal{X} \quad\text{and}\quad \Delta : \mathcal{X} \to \mathcal{X} \times_\mathcal{Y} \mathcal{X}
```
```tex
\mathcal{U} \to \mathcal{X} \quad\text{et}\quad \Delta : \mathcal{X} \to \mathcal{X} \times_\mathcal{Y} \mathcal{X}
```

### `lemma-etale-separated-over-keel-mori`

Et relie deux diagrammes distincts : les primes, indices et buts M prime et M sont conservés.

```tex
\xymatrix{ \mathcal{X}'_i \ar[d]_{f'_i} \ar[r]_{g'_i} & \mathcal{X}' \ar[d]^{f'} \\ M'_i \ar[r] & M' } \quad\text{and}\quad \xymatrix{ \mathcal{X}'_i \ar[d]_{f'_i} \ar[r]_{g_i} & \mathcal{X} \ar[d]^f \\ M'_i \ar[r] & M }
```
```tex
\xymatrix{ \mathcal{X}'_i \ar[d]_{f'_i} \ar[r]_{g'_i} & \mathcal{X}' \ar[d]^{f'} \\ M'_i \ar[r] & M' } \quad\text{et}\quad \xymatrix{ \mathcal{X}'_i \ar[d]_{f'_i} \ar[r]_{g_i} & \mathcal{X} \ar[d]^f \\ M'_i \ar[r] & M }
```

### `lemma-extend`

Fini qualifie J prime, le sous-ensemble de J qui indexe la limite inductive ; il ne qualifie ni les modules ni le foncteur.

```tex
\mathcal{F} = \colim_{J' \subset J\text{ finite}} \bigoplus_{j \in J'} \mathcal{H}_j
```
```tex
\mathcal{F} = \colim_{J' \subset J\text{ fini}} \bigoplus_{j \in J'} \mathcal{H}_j
```

### `lemma-extend`

Les deux mentions fini qualifient les mêmes sous-ensembles J prime dans les deux limites inductives. La dernière somme sur tout J reste inchangée.

```tex
F(\mathcal{F}) & = \colim_{J' \subset J\text{ finite}} F(\bigoplus\nolimits_{j \in J'} \mathcal{H}_j) \\ & = \colim_{J' \subset J\text{ finite}} \bigoplus\nolimits_{j \in J'} F(\mathcal{H}_j) \\ & = \bigoplus\nolimits_{j \in J} F(\mathcal{H}_j)
```
```tex
F(\mathcal{F}) & = \colim_{J' \subset J\text{ fini}} F(\bigoplus\nolimits_{j \in J'} \mathcal{H}_j) \\ & = \colim_{J' \subset J\text{ fini}} \bigoplus\nolimits_{j \in J'} F(\mathcal{H}_j) \\ & = \bigoplus\nolimits_{j \in J} F(\mathcal{H}_j)
```

## Limites

Chaque contexte modifié et chaque différence conservée ci-dessus a été lu dans les deux langues. Les contrôles sur tous les blocs étiquetés ne certifient pas l’intégralité de la prose ni de la terminologie. Les anomalies du témoin officiel restaurées ne sont pas présentées comme mathématiquement correctes. L’inversion des opérations reproduit exactement la version publique. La construction et la vérification publique du lecteur complet restent à effectuer.
