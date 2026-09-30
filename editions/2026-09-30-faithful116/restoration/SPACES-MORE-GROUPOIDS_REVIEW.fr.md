# Compléments sur les groupoïdes en espaces : rétablissements délimités

**Copie LaTeX locale ; pas encore une édition publique corrigée.**

[LaTeX](staged/fr/079_spaces-more-groupoids.fr.tex) · [Contrôles](SPACES-MORE-GROUPOIDS_FR_VALIDATION.json) · [Avant/après et contextes complets](SPACES-MORE-GROUPOIDS_FR_REPAIRS.json)

Les rétablissements conservent volontairement des anomalies du témoin officiel. Ils ne déclarent pas ces anomalies mathématiquement correctes. Les améliorations proposées restent séparément visibles dans les lectures antérieures, sans être incorporées à la traduction de base. Deux autres opérations réparent uniquement le français des points à valeurs dans un corps, conformément au contexte de la même preuve. Aucune consultation initiale ni nouvelle attestation externe n’est inventée.

## FR-SPACES-MORE-GROUPOIDS-001 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-more-groupoids.tex#L402)

La traduction avait remplacé la justification littérale I=Ker(I) par un autre argument utilisant K de carré nul. On rétablit la justification imprimée, malgré son anomalie ; le nouvel argument reste consultable dans cet avant/après, hors de la traduction de base.

Avant :
```tex
puisque $\delta_i(I) \subset K$ et $K^2 = 0$.
```
Après :
```tex
puisque $I = \Ker(I)$.
```

## FR-SPACES-MORE-GROUPOIDS-002 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-more-groupoids.tex#L1280)

La formule officielle utilise g_i alors que l’entrée est notée t_i. On rétablit les symboles imprimés sans présenter leur incohérence comme correcte.

Avant :
```tex
f(t_1) \ldots f(t_n)
```
Après :
```tex
f(g_1) \ldots f(g_n)
```

## FR-SPACES-MORE-GROUPOIDS-003 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-more-groupoids.tex#L1895)

Deux primes avaient été retirées dans la phrase rappelant V. Le lecteur doit retrouver la même discordance T/T prime que dans le témoin officiel.

Avant :
```tex
$V = T \setminus E$ est un sous-schéma ouvert de $T$
```
Après :
```tex
$V = T' \setminus E$ est un sous-schéma ouvert de $T'$
```

## FR-SPACES-MORE-GROUPOIDS-004 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-more-groupoids.tex#L1905)

Rétablit le changement de base T prime effectivement nommé à cet endroit de la preuve.

Avant :
```tex
fermés dans $T \times_Y X$
```
Après :
```tex
fermés dans $T' \times_Y X$
```

## FR-SPACES-MORE-GROUPOIDS-005 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-more-groupoids.tex#L1909)

Même restauration de T prime dans le changement de base invoqué pour la platitude et la présentation finie ; les autres occurrences de T restent intactes.

Avant :
```tex
$T \times_Y X$, et
```
Après :
```tex
$T' \times_Y X$, et
```

## FR-SPACES-MORE-GROUPOIDS-006 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-more-groupoids.tex#L2068)

Rétablit U prime dans la base et U dans le facteur comme dans cette phrase officielle seulement. Les produits fibrés précédents et le diagramme, différents mais imprimés ainsi, ne sont pas modifiés.

Avant :
```tex
est aussi fermé dans
$R \times_{s, U, g} U'$. Voici
```
Après :
```tex
est aussi fermé dans
$R \times_{s, U', g} U$. Voici
```

## FR-SPACES-MORE-GROUPOIDS-007 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-more-groupoids.tex#L2351)

La dernière composante du triplet finit littéralement par u. Son remplacement par z était une correction source, non une traduction.

Avant :
```tex
u'\circ s \circ z)$ comme morphismes
```
Après :
```tex
u'\circ s \circ u)$ comme morphismes
```

## FR-SPACES-MORE-GROUPOIDS-008 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-more-groupoids.tex#L2549)

La preuve imprimée parle des morphismes sur R prime, pas seulement de leurs restrictions à P. On conserve ce domaine officiel et consigne séparément le correctif proposé.

Avant :
```tex
$s'|_P, t'|_P : P \to U'$
```
Après :
```tex
$s', t' : R' \to U'$
```

## FR-SPACES-MORE-GROUPOIDS-009 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-more-groupoids.tex#L2550)

La raison donnée par le texte officiel est une hypothèse. La traduction ne doit pas lui substituer une justification par la définition du scindage.

Avant :
```tex
Ils sont finis par définition du scindage.
```
Après :
```tex
Ils sont finis par hypothèse.
```

## FR-SPACES-MORE-GROUPOIDS-010 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-more-groupoids.tex#L2550)

Rétablit les deux mêmes morphismes non restreints que nomme cette conclusion officielle, sans réparer le raisonnement.

Avant :
```tex
Ainsi, $s'|_P, t'|_P$ sont finis
```
Après :
```tex
Ainsi, $s', t'$ sont finis
```

## FR-SPACES-MORE-GROUPOIDS-011 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-more-groupoids.tex#L2553)

La source utilise ici t et s sans prime ni restriction à P. L’expression modifiée appartenait à une réécriture de la preuve.

Avant :
```tex
$(t'|_P)((s'|_P)^{-1}(u'))$
```
Après :
```tex
$t(s^{-1}(u'))$
```

## FR-SPACES-MORE-GROUPOIDS-012 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-more-groupoids.tex#L2583)

Rétablit la double prime de u telle qu’elle est imprimée ; l’intention probable u prime reste une proposition séparée.

Avant :
```tex
$R''$ au-dessus de $u'$ :
```
Après :
```tex
$R''$ au-dessus de $u''$ :
```

## FR-SPACES-MORE-GROUPOIDS-013 — Erreur de traduction réparée

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-more-groupoids.tex#L1256)

k points désigne les points à valeurs dans k, non les points du corps k vu comme ensemble. Cette lecture est explicitée auparavant dans la même preuve pour x et y ; aucun nouveau critère de rationalité n’est ajouté.

Avant :
```tex
au-dessus des points de $k$ sont finies.
```
Après :
```tex
au-dessus des points à valeurs dans $k$ sont finies.
```

## FR-SPACES-MORE-GROUPOIDS-014 — Erreur de traduction réparée

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-more-groupoids.tex#L1260)

Même réparation de la portée de k : il qualifie les points de Z. La densité, le corps supposé algébriquement clos et la référence citée restent ceux du témoin.

Avant :
```tex
les points de $k$ sont denses dans $Z$
```
Après :
```tex
les points à valeurs dans $k$ sont denses dans $Z$
```

## Différences fidèles conservées

### `lemma-property-invariant`

Lisse et syntomique sont les noms français des deux mêmes topologies. La localité sur le but, les deux recouvrements et l’ordre s/t de l’égalité finale restent inchangés.

### `lemma-property-G-invariant`

Les deux topologies sont traduites comme dans le lemme précédent ; la propriété de G_W et l’isomorphisme par conjugaison restent exacts.

### `lemma-quotient-power-P1`

Fini traduit finite dans l’étiquette de la même flèche. La projection, les exposants n,m, la séparabilité au sens séparé du morphisme et l’hypothèse de type fini ne changent pas. Les points à valeurs dans k sont clarifiés séparément.

### `lemma-strong-splitting`

Reste traduit le nom descriptif Rest pour la même composante ouverte et fermée complémentaire de Z_u. Le produit disjoint et le support de Z_u restent inchangés.

### `lemma-splitting`

Même nom descriptif Reste, sans modification du complément, du support G_u ni du point u prime. Est au-dessus de traduit maps to pour la même application vers U prime.

### `lemma-quasi-splitting`

Reste nomme le même complément ; le support e(u) et le critère final e prime(u prime) dans Z_univ sont conservés.

## Texte dans les formules

### `section-local`

Et joint les deux mêmes anneaux locaux A et B ; le point géométrique et la section e restent exacts.

```tex
A = \mathcal{O}_{U, \overline{u}} \quad\text{and}\quad B = \mathcal{O}_{R, e(\overline{u})}
```
```tex
A = \mathcal{O}_{U, \overline{u}} \quad\text{et}\quad B = \mathcal{O}_{R, e(\overline{u})}
```

### `section-groupoid-sections`

Flèches désigne Arrows dans les sept données du même groupoïde.

```tex
(\text{Ob}, \text{Arrows}, s, t, c, e, i)
```
```tex
(\text{Ob}, \text{Flèches}, s, t, c, e, i)
```

### `section-groupoid-sections`

Même renommage descriptif du but de delta ; le domaine Ob ne change pas.

```tex
\delta : \text{Ob} \to \text{Arrows}
```
```tex
\delta : \text{Ob} \to \text{Flèches}
```

### `lemma-finite-sheaf`

Satisfaisant garde la condition et son renvoi exact dans l’ensemble des couples.

```tex
\Mor_{\Sh((\Sch/S)_{fppf})}(T, (X/Y)_{fin}) = \{(a, Z)\text{ satisfying \ref{equation-finite-conditions}}\}
```
```tex
\Mor_{\Sh((\Sch/S)_{fppf})}(T, (X/Y)_{fin}) = \{(a, Z)\text{ satisfaisant \ref{equation-finite-conditions}}\}
```

### `lemma-finite-diagonal`

Comme sous-espaces conserve le même espace ambiant et la même équivalence.

```tex
h(T') \subset V \Leftrightarrow \Big(T' \times_T Z_1 = T' \times_T Z_2 \text{ as subspaces of }T' \times_Y X\Big)
```
```tex
h(T') \subset V \Leftrightarrow \Big(T' \times_T Z_1 = T' \times_T Z_2 \text{ comme sous-espaces de }T' \times_Y X\Big)
```

### `lemma-finite-separated-flat-locally-finite-presentation`

Se factorise par V garde le même morphisme h ; le membre droit garde l’espace ambiant T prime fois_Y X.

```tex
h \text{ factors through } V \Leftrightarrow \Big(T' \times_T Z_1 = T' \times_T Z_2 \text{ as subspaces of }T' \times_Y X\Big)
```
```tex
h \text{ se factorise par } V \Leftrightarrow \Big(T' \times_T Z_1 = T' \times_T Z_2 \text{ comme sous-espaces de }T' \times_Y X\Big)
```

### `section-finite-set-arrows`

Flèches est le nom descriptif français dans les mêmes sept données.

```tex
(\text{Ob}, \text{Arrows}, s, t, c, e, i)
```
```tex
(\text{Ob}, \text{Flèches}, s, t, c, e, i)
```

### `section-finite-set-arrows`

Z est toujours un sous-ensemble du même ensemble de flèches.

```tex
Z \subset \text{Arrows}
```
```tex
Z \subset \text{Flèches}
```

### `definition-split-at-point`

Est au-dessus de u garde la condition d’image par G vers U, sans changer la borne P.

```tex
\{g \in |G| : g\text{ maps to }u\} \subset |P|
```
```tex
\{g \in |G| : g\text{ est au-dessus de }u\} \subset |P|
```

### `situation-splitting`

Même condition d’image dans la situation du scindage.

```tex
\{g \in G : g\text{ maps to }u\}
```
```tex
\{g \in G : g\text{ est au-dessus de }u\}
```

### `lemma-splitting`

Même condition pour les objets primés dans la preuve du scindage.

```tex
\{g' \in |G'| : g'\text{ maps to }u'\}
```
```tex
\{g' \in |G'| : g'\text{ est au-dessus de }u'\}
```

## Limites

Les candidats de formules sont tous expliqués dans ce passage de contrôle ; cela ne certifie pas toute la prose ni toute la terminologie. Les identifiants, les renvois et les environnements concordent exactement avec le témoin officiel. L’inversion des opérations reproduit les octets publics. Aucun PDF n’a été reconstruit ni publié à ce stade.
