# Chapitre 68 — Espaces algébriques décents : fidélité au texte officiel

**Réparation locale en cours ; aucune édition publique corrigée n’est encore certifiée.**

[LaTeX de travail](staged/fr/068_decent-spaces.fr.tex) · [Contrôles](DECENT-SPACES_PARTIAL_VALIDATION.json) · [Contextes complets](DECENT-SPACES_CONTEXTUAL_RESTORATIONS.json)

La traduction est non officielle et assistée par IA, sans relecture experte humaine. Le dossier sépare les propositions mathématiques des réparations propres à la traduction. Rétablir un passage ne signifie pas préférer sa mathématique à celle de la proposition écartée. Le témoin officiel reste inchangé.

## FR-DECENT-SPACES-FIDELITY-001 — `definition-universally-bounded`

[Source officielle, ligne 73](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L73)

La remarque officielle emploie Y et X, bien que la définition précédente emploie X et U. La traduction a corrigé les deux noms ; on conserve ces corrections proposées dans le dossier, et non dans le corps fidèle.

Source :
```tex
$\Spec(k) \times_Y X$ is a scheme. Moreover, if $Y$ is a scheme
```
Traduction publiée :
```tex
$\Spec(k) \times_X U$ est un schéma. De plus, si $X$ est un schéma,
```
Lecture retenue :
```tex
$\Spec(k) \times_Y X$ est un schéma. De plus, si $Y$ est un schéma,
```

## FR-DECENT-SPACES-FIDELITY-002 — `lemma-universally-bounded-permanence`

[Source officielle, ligne 189](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L189)

La flèche affichée a été renversée pour correspondre au morphisme f. On rétablit la flèche effectivement imprimée, sans prétendre que ce sens est mathématiquement préférable.

Source :
```tex
\Spec(k) \times_X V \longrightarrow \Spec(k) \times_X U
```
Traduction publiée :
```tex
\Spec(k) \times_X U \longrightarrow \Spec(k) \times_X V
```
Lecture retenue :
```tex
\Spec(k) \times_X V \longrightarrow \Spec(k) \times_X U
```

## FR-DECENT-SPACES-FIDELITY-003 — `lemma-U-finite-above-x`

[Source officielle, ligne 308](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L308)

Le but porte i dans le texte officiel et i_j dans la traduction. Rétablissement local de la notation source, sans modifier les autres indices.

Source :
```tex
p_{i_j}|_{W_{i_j}} : W_{i_j} \to U_i
```
Traduction publiée :
```tex
p_{i_j}|_{W_{i_j}} : W_{i_j} \to U_{i_j}
```
Lecture retenue :
```tex
p_{i_j}|_{W_{i_j}} : W_{i_j} \to U_i
```

## FR-DECENT-SPACES-FIDELITY-004 — `lemma-U-universally-bounded`

[Source officielle, ligne 660](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L660)

La traduction a remplacé la projection p par q dans cette égalité. Le diagramme explique la correction proposée, mais la traduction de référence doit garder p.

Source :
```tex
U = \bigcup p_{i_j}(W_j)
```
Traduction publiée :
```tex
U = \bigcup q_{i_j}(W_j)
```
Lecture retenue :
```tex
U = \bigcup p_{i_j}(W_j)
```

## FR-DECENT-SPACES-FIDELITY-005 — `lemma-representable-properties`

[Source officielle, ligne 983](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L983)

La conclusion du cas delta dit Y dans la source ; la traduction a changé cet objet en X. Le dossier garde la raison de la proposition sans la substituer silencieusement au texte.

Source :
```tex
applies and we see that $Y$ also has property $(\delta)$.
```
Traduction publiée :
```tex
s'applique donc, et nous voyons que $X$ possède lui aussi la propriété
```
Lecture retenue :
```tex
s'applique donc, et nous voyons que $Y$ possède lui aussi la propriété
```

## FR-DECENT-SPACES-FIDELITY-006 — `lemma-representable-properties`

[Source officielle, ligne 994](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L994)

Le produit fibré de cette phrase est écrit sur Y dans la source, et non sur X. L’égalité précédente sur X reste inchangée.

Source :
```tex
that the projections $U_i \times_Y U_i \to U_i$ are
```
Traduction publiée :
```tex
projections $U_i \times_X U_i \to U_i$ sont les changements de base des
```
Lecture retenue :
```tex
projections $U_i \times_Y U_i \to U_i$ sont les changements de base des
```

## FR-DECENT-SPACES-FIDELITY-007 — `lemma-fun-property-reasonable`

[Source officielle, ligne 1147](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L1147)

Réparation propre à la traduction : la commande d’accent anglais est restée devant M après traduction du titre. Le titre français existant « Morphismes étales » et le renvoi exact sont conservés ; aucun énoncé n’est corrigé.

Source :
```tex
\'Etale Morphisms, Proposition \ref{etale-proposition-properties-sections}.
```
Traduction publiée :
```tex
\'Morphismes étales, Proposition \ref{etale-proposition-properties-sections}.
```
Lecture retenue :
```tex
Morphismes étales, Proposition \ref{etale-proposition-properties-sections}.
```

## FR-DECENT-SPACES-FIDELITY-008 — `lemma-fun-property-reasonable`

[Source officielle, ligne 1159](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L1159)

La traduction a ajouté un second facteur U(k) à l’ensemble ambiant. On rétablit l’expression officielle, tout en conservant la proposition dans le comparatif.

Source :
```tex
A^n(k) = \left\{(u, u') \in U(k)
:
```
Traduction publiée :
```tex
A^n(k) = \left\{(u, u') \in U(k) \times U(k)
:
```
Lecture retenue :
```tex
A^n(k) = \left\{(u, u') \in U(k)
:
```

## FR-DECENT-SPACES-FIDELITY-009 — `lemma-fun-property-reasonable`

[Source officielle, ligne 1162](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L1162)

La traduction a ajouté l’extrémité u′ et remplacé n par n+1. Ce changement de la chaîne n’est pas un choix linguistique ; retour à la formule source.

Source :
```tex
\text{there exist } u = u_1, u_2, \ldots, u_n \in U(k)\text{ with}
```
Traduction publiée :
```tex
\text{il existe } u = u_1, u_2, \ldots, u_{n + 1} = u' \in U(k)
```
Lecture retenue :
```tex
\text{il existe } u = u_1, u_2, \ldots, u_n \in U(k)
```

## FR-DECENT-SPACES-FIDELITY-010 — `lemma-fun-property-reasonable`

[Source officielle, ligne 1163](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L1163)

La borne n avait remplacé la borne n−1 de la source. Le texte français « pour tout » demeure ; seule la borne est rétablie.

Source :
```tex
(u_i , u_{i + 1}) \in A \text{ for all }i = 1, \ldots, n - 1.
```
Traduction publiée :
```tex
(u_i , u_{i + 1}) \in A \text{ pour tout }i = 1, \ldots, n.
```
Lecture retenue :
```tex
(u_i , u_{i + 1}) \in A \text{ pour tout }i = 1, \ldots, n - 1.
```

## FR-DECENT-SPACES-FIDELITY-011 — `lemma-there-is-a-scheme-integral-over-refined`

[Source officielle, ligne 1897](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L1897)

La source utilise ensuite f sans le nommer ici. La désignation ajoutée f: est consignée à part, non insérée silencieusement dans la traduction diplomatique.

Source :
```tex
There exists a surjective integral morphism $Y \to X$ where $Y$
```
Traduction publiée :
```tex
Il existe un morphisme entier surjectif $f : Y \to X$, où $Y$
```
Lecture retenue :
```tex
Il existe un morphisme entier surjectif $Y \to X$, où $Y$
```

## FR-DECENT-SPACES-FIDELITY-012 — `lemma-there-is-a-scheme-integral-over-refined`

[Source officielle, ligne 1943](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L1943)

L’indice j ajouté à cette occurrence de phi corrige la notation source ; on rétablit cette occurrence sans toucher aux autres phi_j.

Source :
```tex
$m$, $\varphi : V_j \to X$, $j = 1, \ldots, m$ be as in $(H_d)$.
```
Traduction publiée :
```tex
$m$, $\varphi_j : V_j \to X$, $j = 1, \ldots, m$ comme dans $(H_d)$.
```
Lecture retenue :
```tex
$m$, $\varphi : V_j \to X$, $j = 1, \ldots, m$ comme dans $(H_d)$.
```

## FR-DECENT-SPACES-FIDELITY-013 — `lemma-there-is-a-scheme-integral-over-refined`

[Source officielle, ligne 1995](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L1995)

La base des espaces étales est nommée Y dans cette phrase officielle. Le remplacement par Y_j est une correction mathématique proposée, pas une traduction.

Source :
```tex
algebraic spaces \'etale over $Y$) and
```
Traduction publiée :
```tex
algébriques étales sur $Y_j$), et le second terme est le complémentaire
```
Lecture retenue :
```tex
algébriques étales sur $Y$), et le second terme est le complémentaire
```

## FR-DECENT-SPACES-FIDELITY-014 — `lemma-there-is-a-scheme-integral-over-refined`

[Source officielle, ligne 2018](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L2018)

Le terme intermédiaire de la composée officielle est Y ; la traduction l’avait corrigé en Y_j. Retour local au texte de référence.

Source :
```tex
as on each summand we have the composition $Y'_j \to Y \to X$
```
Traduction publiée :
```tex
car, sur chaque composante, nous avons la composition $Y'_j \to Y_j \to X$ de
```
Lecture retenue :
```tex
car, sur chaque composante, nous avons la composition $Y'_j \to Y \to X$ de
```

## FR-DECENT-SPACES-FIDELITY-015 — `lemma-when-quotient-scheme-at-point`

[Source officielle, ligne 2177](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L2177)

Les parenthèses ajoutées imposent une portée à la différence ensembliste que la formule source ne porte pas. Elles sont conservées comme proposition distincte, et retirées du corps fidèle.

Source :
```tex
Z = R \setminus s^{-1}(U) \cap t^{-1}(U)
```
Traduction publiée :
```tex
Z = R \setminus (s^{-1}(U) \cap t^{-1}(U))
```
Lecture retenue :
```tex
Z = R \setminus s^{-1}(U) \cap t^{-1}(U)
```

## FR-DECENT-SPACES-FIDELITY-016 — `lemma-finite-etale-cover-dense-open-scheme`

[Source officielle, ligne 2277](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L2277)

Le texte officiel dit W″ pour l’espace ambiant du complément. La traduction a remplacé cette notation par W′, qui semble mathématiquement attendue. La correction reste séparée.

Source :
```tex
Set $\Delta' = W' \setminus W''$. This is a nowhere dense closed subset of
$W''$.
```
Traduction publiée :
```tex
Posons $\Delta' = W' \setminus W''$. C'est une partie fermée rare de $W'$.
```
Lecture retenue :
```tex
Posons $\Delta' = W' \setminus W''$. C'est une partie fermée rare de $W''$.
```

## FR-DECENT-SPACES-FIDELITY-017 — `remark-functoriality-henselian-local-ring`

[Source officielle, ligne 2591](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L2591)

La phrase prescrivant le choix de points géométriques compatibles est une explication mathématique ajoutée. Le diagramme officiel est conservé, mais la phrase ajoutée est déplacée vers ce dossier comparatif.

Source :
```tex
over $S$. Let $x \in |X|$ with image $y \in |Y|$. Choose an elementary
```
Traduction publiée :
```tex
d'image $y \in |Y|$. Choisissons des points géométriques compatibles
$(\overline{x} \to X, \overline{y} = f(\overline{x}) \to Y)$
au-dessus de $(x, y)$.
Choisissons un voisinage étale élémentaire
```
Lecture retenue :
```tex
d'image $y \in |Y|$.
Choisissons un voisinage étale élémentaire
```

## FR-DECENT-SPACES-FIDELITY-018 — `proposition-reasonable-sober`

[Source officielle, ligne 2710](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L2710)

Le texte source porte des barres autour de T, même si T a déjà été défini comme partie topologique. La simplification de notation n’est pas reproduite silencieusement.

Source :
```tex
with $|Z| = |T|$.
```
Traduction publiée :
```tex
tel que $|Z| = T$.
```
Lecture retenue :
```tex
tel que $|Z| = |T|$.
```

## FR-DECENT-SPACES-FIDELITY-019 — `lemma-factor-through-residual-space-Noetherian`

[Source officielle, ligne 3165](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L3165)

Le dernier morphisme de cette étape a pour but X dans la source, U dans la traduction. On restaure seulement cette occurrence, l’autre morphisme vers X restant intact.

Source :
```tex
$\coprod_{u \in E} u \to X$. After replacing
```
Traduction publiée :
```tex
$\coprod_{u \in E} u \to U$. Après avoir remplacé
```
Lecture retenue :
```tex
$\coprod_{u \in E} u \to X$. Après avoir remplacé
```

## FR-DECENT-SPACES-FIDELITY-020 — `lemma-algebraic-residue-field-extension-closed-point`

[Source officielle, ligne 3372](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L3372)

Le U primé, non défini ici, a été corrigé silencieusement en U. La notation du texte officiel est rétablie ; la proposition reste lisible dans le dossier.

Source :
```tex
a point $u' \in U'$
```
Traduction publiée :
```tex
un point $u' \in U$
```
Lecture retenue :
```tex
un point $u' \in U'$
```

## FR-DECENT-SPACES-FIDELITY-021 — `lemma-monomorphism-toward-disjoint-union-dim-0-rings`

[Source officielle, ligne 4544](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L4544)

Le facteur B ajouté à l’idéal dénominateur explicite une extension d’idéal absente de cette formule source. Il est retiré ici seulement ; les autres quotients de la preuve restent inchangés.

Source :
```tex
\Spec(B) = \Spec(B/\mathfrak m_A)
```
Traduction publiée :
```tex
\Spec(B) = \Spec(B/\mathfrak m_A B)
```
Lecture retenue :
```tex
\Spec(B) = \Spec(B/\mathfrak m_A)
```

## FR-DECENT-SPACES-FIDELITY-022 — `lemma-get-reasonable`

[Source officielle, ligne 4687](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L4687)

Le point de l’ouvert est nommé x_i dans la source et a été renommé u_i pour rendre le raisonnement cohérent. Cette correction est séparée du corps traduit.

Source :
```tex
of $U$ and hence would contain one of the $x_i$.
```
Traduction publiée :
```tex
contiendrait donc l'un des $u_i$.
```
Lecture retenue :
```tex
contiendrait donc l'un des $x_i$.
```

## FR-DECENT-SPACES-FIDELITY-023 — `lemma-generically-finite`

[Source officielle, ligne 4810](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L4810)

Les deux projections sont écrites vers V à cette occurrence officielle. La traduction les avait corrigées en projections vers U ; rétablissement local.

Source :
```tex
$R \to V$ are finite
```
Traduction publiée :
```tex
projections $R \to U$ sont finies étales.
```
Lecture retenue :
```tex
projections $R \to V$ sont finies étales.
```

## FR-DECENT-SPACES-FIDELITY-024 — `lemma-generically-finite`

[Source officielle, ligne 4811](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L4811)

Le quotient V/R de la source avait été remplacé par U/R. Ce changement d’objet n’est pas un simple choix français et reste séparé.

Source :
```tex
V/R = V \times_Y X
```
Traduction publiée :
```tex
U/R = V \times_Y X
```
Lecture retenue :
```tex
V/R = V \times_Y X
```

## FR-DECENT-SPACES-FIDELITY-025 — `lemma-birational-generic-fibres`

[Source officielle, ligne 5033](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L5033)

Les barres autour de Y sont une précision absente de la notation source. Retour à cette notation sans changer la qualification de point générique.

Source :
```tex
If $y \in Y$ is the generic point of
```
Traduction publiée :
```tex
Si $y \in |Y|$ est le point générique
```
Lecture retenue :
```tex
Si $y \in Y$ est le point générique
```

## FR-DECENT-SPACES-FIDELITY-026 — `lemma-birational-induced-morphism-normalizations`

[Source officielle, ligne 5174](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L5174)

La traduction a inversé l’homomorphisme entre anneaux locaux conformément à la contravariance attendue. La flèche source est rétablie et la correction proposée reste distincte.

Source :
```tex
\mathcal{O}_{X, x} \to \mathcal{O}_{Y, y}
```
Traduction publiée :
```tex
\mathcal{O}_{Y, y} \to \mathcal{O}_{X, x}
```
Lecture retenue :
```tex
\mathcal{O}_{X, x} \to \mathcal{O}_{Y, y}
```

## FR-DECENT-SPACES-FIDELITY-027 — `lemma-birational-induced-morphism-normalizations`

[Source officielle, ligne 5180](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L5180)

Même inversion silencieuse dans la flèche entre anneaux des normalisations ; retour à la formule officielle.

Source :
```tex
\mathcal{O}_{X^\nu, x^\nu} \to \mathcal{O}_{Y^\nu, y^\nu}
```
Traduction publiée :
```tex
\mathcal{O}_{Y^\nu, y^\nu} \to \mathcal{O}_{X^\nu, x^\nu}
```
Lecture retenue :
```tex
\mathcal{O}_{X^\nu, x^\nu} \to \mathcal{O}_{Y^\nu, y^\nu}
```

## FR-DECENT-SPACES-FIDELITY-028 — `section-jacobson`

[Source officielle, ligne 5244](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L5244)

La source nomme ici l’espace algébrique par |X|. La suppression des barres corrige ce nom ; le dossier sépare cette proposition du texte diplomatique.

Source :
```tex
for general algebraic spaces $|X|$.
```
Traduction publiée :
```tex
pour un espace algébrique général $X$.
```
Lecture retenue :
```tex
pour un espace algébrique général $|X|$.
```

## FR-DECENT-SPACES-FIDELITY-029 — `lemma-punctured-spec`

[Source officielle, ligne 5438](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L5438)

La conclusion officielle affirme que le singleton est infini ; la traduction avait remplacé ce singleton par une fibre. Cette modification du raisonnement est retirée. Le français est ajusté uniquement pour traduire la phrase source, sans prétendre établir une nouvelle preuve.

Source :
```tex
is decent and we conclude that $\{x'\}$ is infinite.
```
Traduction publiée :
```tex
puisque $X$ est décent ; la
fibre au-dessus de $x'$ serait donc infinie. Cette contradiction achève la
```
Lecture retenue :
```tex
puisque $X$ est décent ;
on conclut donc que $\{x'\}$ est infini. Cette contradiction achève la
```

## FR-DECENT-SPACES-FIDELITY-030 — `lemma-nr-branches-local-ring`

[Source officielle, ligne 5523](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L5523)

L’exposant h ajouté dans la preuve corrige la notation de la source. On le retire à cette occurrence ; celui de l’énoncé (4) reste inchangé.

Source :
```tex
The ring $\mathcal{O}_{X, x}$ is the henselization
```
Traduction publiée :
```tex
L'anneau $\mathcal{O}_{X, x}^h$ est l'hensélisé
```
Lecture retenue :
```tex
L'anneau $\mathcal{O}_{X, x}$ est l'hensélisé
```

## FR-DECENT-SPACES-FIDELITY-031 — `lemma-check-dimension-function-finite-cover`

[Source officielle, ligne 5665](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L5665)

La source emploie mapsto pour cette première spécialisation et leadsto pour les suivantes. La traduction avait uniformisé cette occurrence ; on garde la distinction imprimée.

Source :
```tex
Let $x \mapsto x'$, $x \not = x'$ be a specialization
```
Traduction publiée :
```tex
Soit $x \leadsto x'$, avec $x \not = x'$, une spécialisation
```
Lecture retenue :
```tex
Soit $x \mapsto x'$, avec $x \not = x'$, une spécialisation
```

## Explicitations conservées

### `lemma-fun-property-reasonable`

Le complément sur S explicite le cadre déjà fixé par la première phrase et la catégorie des faisceaux sur S. Il ne change ni base ni hypothèse ; contrairement aux changements de la formule A^n, cette explicitation est conservée.

### `lemma-property-over-property`

Les trois cas bêta, décent, raisonnable sont tous conservés, y compris raisonnable dans le dernier paragraphe. La différence de comparaison vient de mots anglais en mode mathématique traduits sous une commande text ; aucune propriété n’a été substituée.

### `lemma-descent-conditions`

Les trois propriétés et leurs trois preuves sont conservées. Les noms français dans les formules restent français ; le dernier cas est bien raisonnable, et non un second cas décent.

### `lemma-generically-finite`

Le point final du premier affichage est une ponctuation de phrase, conservée. Il ne faut pas le confondre avec les deux changements d’objets R vers U et U/R, qui sont rétablis séparément.

### `lemma-composition-relative-conditions`

Les noms décent et raisonnable dans l’ensemble de propriétés traduisent les noms anglais, sans modifier les quantificateurs ni la composition.

### `lemma-relative-conditions-local`

Les deux listes gardent leur différence : très raisonnable figure dans la première, mais pas dans la seconde qui gouverne la condition (5). Les noms français sont conservés dans les formules.

### `lemma-decent-Jacobson-ft-pts`

Un point terminal est ajouté après U dans le diagramme de morphismes. C’est une ponctuation de phrase, non un nouvel objet.

### `lemma-punctured-spec`

Le point terminal après W dans la flèche affichée est conservé. Le changement du singleton en fibre dans la conclusion est, lui, une intervention sur l’argument et est rétabli séparément.

## Limites

Les contextes de chaque opération ont été lus. Il reste à comparer les autres candidats, toute la prose et la terminologie, puis à reconstruire et publier les éditions complètes. Les identifiants historiques producteurs ne sont pas inventés : leur rapprochement reste à faire. Les mathématiques sources gouvernent ces restaurations ; aucune consultation initiale du canon terminologique n’est affirmée rétrospectivement. Une expertise humaine ultérieure est bienvenue, mais ne bloque pas le travail.
