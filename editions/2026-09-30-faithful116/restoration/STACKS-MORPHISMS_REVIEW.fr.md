# Chapitre 101 — Morphismes de champs algébriques : fidélité au texte officiel

**Réparation locale en cours ; aucune édition publique corrigée n’est encore certifiée.**

[LaTeX de travail](staged/fr/101_stacks-morphisms.fr.tex) · [Contrôles](STACKS-MORPHISMS_PARTIAL_VALIDATION.json) · [Contextes complets](STACKS-MORPHISMS_CONTEXTUAL_RESTORATIONS.json)

La traduction est non officielle et assistée par IA, sans relecture experte humaine. Le dossier sépare les propositions mathématiques des réparations propres à la traduction. Rétablir un passage ne signifie pas préférer sa mathématique à celle de la proposition écartée. Le témoin officiel reste inchangé.

## FR-STACKS-MORPHISMS-FIDELITY-001 — `lemma-separated-implies-morphism-separated`

[Source officielle, ligne 879](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L879)

Les deux noms simples X et Y de cette phrase source avaient été harmonisés avec les noms calligraphiques de l’énoncé. Cette normalisation est séparée du corps fidèle.

Source :
```tex
think of $X$ and $Y$ as algebraic stacks over
```
Traduction publiée :
```tex
$\mathcal{X}$ et $\mathcal{Y}$ comme des champs algébriques sur
```
Lecture retenue :
```tex
$X$ et $Y$ comme des champs algébriques sur
```

## FR-STACKS-MORPHISMS-FIDELITY-002 — `lemma-characterize-representable-quasi-compact`

[Source officielle, ligne 1744](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L1744)

La source nomme Z comme deuxième facteur dans cette égalité. Le remplacement par X calligraphique corrige la preuve, ce qui est distinct d’une traduction.

Source :
```tex
$p^{-1}(U) = U \times_\mathcal{Y} Z$
```
Traduction publiée :
```tex
$p^{-1}(U) = U \times_\mathcal{Y} \mathcal{X}$
```
Lecture retenue :
```tex
$p^{-1}(U) = U \times_\mathcal{Y} Z$
```

## FR-STACKS-MORPHISMS-FIDELITY-003 — `lemma-characterize-representable-quasi-compact`

[Source officielle, ligne 1745](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L1745)

Même restauration du facteur Z dans la phrase immédiatement suivante, sans modifier les produits antérieurs déjà conformes.

Source :
```tex
and the algebraic space $U \times_\mathcal{Y} Z$
```
Traduction publiée :
```tex
et l'espace algébrique $U \times_\mathcal{Y} \mathcal{X}$ est quasi-compact
```
Lecture retenue :
```tex
et l'espace algébrique $U \times_\mathcal{Y} Z$ est quasi-compact
```

## FR-STACKS-MORPHISMS-FIDELITY-004 — `lemma-locally-closed-in-noetherian`

[Source officielle, ligne 2022](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L2022)

Le sens de l’immersion de cette phrase officielle est V vers U. Le sens corrigé U vers V est gardé dans le dossier d’errata, non dans la traduction diplomatique.

Source :
```tex
$V \to U$ is an immersion, see
```
Traduction publiée :
```tex
$U \to V$ est une immersion;
```
Lecture retenue :
```tex
$V \to U$ est une immersion;
```

## FR-STACKS-MORPHISMS-FIDELITY-005 — `lemma-universally-closed-local`

[Source officielle, ligne 2588](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L2588)

Le second diagramme porte Z simple dans ce coin ; restauration de ce seul nom, indépendamment des Z calligraphiques correctement présents ailleurs.

Source :
```tex
|Z \times_\mathcal{Y} \mathcal{X}| \ar[d]
```
Traduction publiée :
```tex
|\mathcal{Z} \times_\mathcal{Y} \mathcal{X}| \ar[d] \\
```
Lecture retenue :
```tex
|Z \times_\mathcal{Y} \mathcal{X}| \ar[d] \\
```

## FR-STACKS-MORPHISMS-FIDELITY-006 — `lemma-local-source-target`

[Source officielle, ligne 3121](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L3121)

Retour à la base X simple dans la dernière application de la descente ; la correction typographique ne reste pas silencieuse.

Source :
```tex
Finally, since $U \times_X U' \to U'$
```
Traduction publiée :
```tex
Enfin, puisque $U \times_\mathcal{X} U' \to U'$
```
Lecture retenue :
```tex
Enfin, puisque $U \times_X U' \to U'$
```

## FR-STACKS-MORPHISMS-FIDELITY-007 — `lemma-finite-type-permanence`

[Source officielle, ligne 3414](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L3414)

La source porte V dans ce produit fibré. W serait une correction de l’argument, pas une traduction du nom source.

Source :
```tex
$U \to \mathcal{X} \times_\mathcal{Z} V$
```
Traduction publiée :
```tex
$U \to \mathcal{X} \times_\mathcal{Z} W$
```
Lecture retenue :
```tex
$U \to \mathcal{X} \times_\mathcal{Z} V$
```

## FR-STACKS-MORPHISMS-FIDELITY-008 — `lemma-point-finite-type-monomorphism`

[Source officielle, ligne 3623](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L3623)

Restauration du facteur X simple à la fin de la composition ; les autres facteurs calligraphiques sont déjà conformes.

Source :
```tex
u \times_\mathcal{X} X = u
```
Traduction publiée :
```tex
u \times_\mathcal{X} \mathcal{X} = u
```
Lecture retenue :
```tex
u \times_\mathcal{X} X = u
```

## FR-STACKS-MORPHISMS-FIDELITY-009 — `theorem-quasi-DM`

[Source officielle, ligne 4156](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L4156)

La source nomme ici varphi, même si le morphisme précédent est noté p dièse. L’identification silencieuse est retirée.

Source :
```tex
$\varphi(f_1), \ldots, \varphi(f_d)$
```
Traduction publiée :
```tex
$p^\sharp(f_1), \ldots, p^\sharp(f_d)$
```
Lecture retenue :
```tex
$\varphi(f_1), \ldots, \varphi(f_d)$
```

## FR-STACKS-MORPHISMS-FIDELITY-010 — `lemma-check-property-after-fppf-base-change`

[Source officielle, ligne 5555](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L5555)

La troisième expression source emploie V, non W. Retour à cette lecture dans la définition affichée.

Source :
```tex
V = W \times_\mathcal{Z} \mathcal{W} = V \times_\mathcal{Y} \mathcal{X}
```
Traduction publiée :
```tex
V = W \times_\mathcal{Z} \mathcal{W} = W \times_\mathcal{Y} \mathcal{X}
```
Lecture retenue :
```tex
V = W \times_\mathcal{Z} \mathcal{W} = V \times_\mathcal{Y} \mathcal{X}
```

## FR-STACKS-MORPHISMS-FIDELITY-011 — `lemma-check-property-after-fppf-base-change`

[Source officielle, ligne 5558](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L5558)

Le nom de propriété est calligraphique dans cette phrase source, contrairement à l’énoncé. L’harmonisation a été séparée.

Source :
```tex
$f$ has $\mathcal{P}$ if and only if $V \to W$ does
```
Traduction publiée :
```tex
$f$ possède $P$ si et seulement si $V \to W$ la possède
```
Lecture retenue :
```tex
$f$ possède $\mathcal{P}$ si et seulement si $V \to W$ la possède
```

## FR-STACKS-MORPHISMS-FIDELITY-012 — `lemma-check-property-after-fppf-base-change`

[Source officielle, ligne 5559](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L5559)

Même restauration du nom calligraphique à la seconde occurrence, sans changer P dans l’énoncé.

Source :
```tex
$\mathcal{W} \to \mathcal{Z}$ has $\mathcal{P}$
```
Traduction publiée :
```tex
$\mathcal{W} \to \mathcal{Z}$ possède $P$
```
Lecture retenue :
```tex
$\mathcal{W} \to \mathcal{Z}$ possède $\mathcal{P}$
```

## FR-STACKS-MORPHISMS-FIDELITY-013 — `lemma-surjective-family-flat-locally-finite-presentation`

[Source officielle, ligne 5708](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L5708)

La source conclut avec y restreint ; le x de la traduction corrige un nom non défini et reste une proposition séparée.

Source :
```tex
f_{a(i)}(x_i) \cong y|_{U_i}
```
Traduction publiée :
```tex
f_{a(i)}(x_i) \cong x|_{U_i}
```
Lecture retenue :
```tex
f_{a(i)}(x_i) \cong y|_{U_i}
```

## FR-STACKS-MORPHISMS-FIDELITY-014 — `lemma-noetherian-singleton-stack-gerbe`

[Source officielle, ligne 6372](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L6372)

Restauration du sous-indice Z simple dans le premier morphisme de la preuve ; les sous-indices calligraphiques ultérieurs sont conformes.

Source :
```tex
\mathcal{I}_Z \times_\mathcal{Z} \Spec(k) \to \Spec(k)
```
Traduction publiée :
```tex
\mathcal{I}_\mathcal{Z} \times_\mathcal{Z} \Spec(k) \to \Spec(k)
```
Lecture retenue :
```tex
\mathcal{I}_Z \times_\mathcal{Z} \Spec(k) \to \Spec(k)
```

## FR-STACKS-MORPHISMS-FIDELITY-015 — `lemma-gerbe-bijection-points`

[Source officielle, ligne 6424](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L6424)

Le sens de la flèche a été inversé pour corriger cette conclusion source. On rétablit le sens source sans reproduire son point grammatical parasite.

Source :
```tex
$|\mathcal{Y}| \to |\mathcal{X}|$. is surjective.
```
Traduction publiée :
```tex
$|\mathcal{X}| \to |\mathcal{Y}|$ est donc surjective.
```
Lecture retenue :
```tex
$|\mathcal{Y}| \to |\mathcal{X}|$ est donc surjective.
```

## FR-STACKS-MORPHISMS-FIDELITY-016 — `lemma-gerbe-bijection-points`

[Source officielle, ligne 6425](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L6425)

Deuxième flèche corrigée dans la même preuve. Les flèches X vers Y du début et de la fin étaient déjà officielles et restent intactes.

Source :
```tex
$|\mathcal{Y}| \to |\mathcal{X}|$ is also injective.
```
Traduction publiée :
```tex
$|\mathcal{X}| \to |\mathcal{Y}|$ est aussi injective.
```
Lecture retenue :
```tex
$|\mathcal{Y}| \to |\mathcal{X}|$ est aussi injective.
```

## FR-STACKS-MORPHISMS-FIDELITY-017 — `lemma-every-point-in-a-stratum`

[Source officielle, ligne 6682](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L6682)

L’indice U_alpha avait été remplacé par la construction U(T_alpha). Retour à la notation réellement écrite.

Source :
```tex
I = \{\alpha \mid \mathcal{U}_\alpha \not = \emptyset \}.
```
Traduction publiée :
```tex
I = \{\alpha \mid \mathcal{U}(T_\alpha) \not = \emptyset \}.
```
Lecture retenue :
```tex
I = \{\alpha \mid \mathcal{U}_\alpha \not = \emptyset \}.
```

## FR-STACKS-MORPHISMS-FIDELITY-018 — `lemma-every-point-in-a-stratum`

[Source officielle, ligne 6685](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L6685)

Même restauration à la définition de U_i, sans toucher les autres occurrences source de U(T_alpha).

Source :
```tex
\mathcal{U}_i = \mathcal{U}_\alpha
```
Traduction publiée :
```tex
\mathcal{U}_i = \mathcal{U}(T_\alpha)
```
Lecture retenue :
```tex
\mathcal{U}_i = \mathcal{U}_\alpha
```

## FR-STACKS-MORPHISMS-FIDELITY-019 — `lemma-every-point-in-a-stratum`

[Source officielle, ligne 6687](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L6687)

Le sous-indice alpha a été ajouté par correction éditoriale. La lecture source T alpha reste dans le corps fidèle et l’ajout d’indice dans le dossier.

Source :
```tex
T_i = T\alpha
```
Traduction publiée :
```tex
T_i = T_\alpha
```
Lecture retenue :
```tex
T_i = T\alpha
```

## FR-STACKS-MORPHISMS-FIDELITY-020 — `lemma-etale-local-quasi-DM`

[Source officielle, ligne 7201](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L7201)

Retour à u non primé dans la phrase source qui suit le choix du voisinage primé.

Source :
```tex
is quasi-split over $u$.
```
Traduction publiée :
```tex
soit quasi-scind\'ee au-dessus de $u'$.
```
Lecture retenue :
```tex
soit quasi-scind\'ee au-dessus de $u$.
```

## FR-STACKS-MORPHISMS-FIDELITY-021 — `lemma-etale-local-quasi-DM-at-x`

[Source officielle, ligne 7259](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L7259)

Même changement de point dans la version scindée : la correction par u primé est retirée du corps fidèle.

Source :
```tex
is split over $u$.
```
Traduction publiée :
```tex
soit scind\'ee au-dessus de $u'$.
```
Lecture retenue :
```tex
soit scind\'ee au-dessus de $u$.
```

## FR-STACKS-MORPHISMS-FIDELITY-022 — `lemma-etale-smooth-local-source-target`

[Source officielle, ligne 7587](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L7587)

La traduction limitait la conclusion source aux seules données géométriques, corrigeant une anticipation de la preuve. Le texte fidèle reprend l’affirmation source de (2) sans cette restriction.

Source :
```tex
Thus we see that (2) holds.
```
Traduction publiée :
```tex
Nous disposons ainsi des données géométriques requises en (2).
```
Lecture retenue :
```tex
Nous voyons ainsi que (2) est vérifiée.
```

## FR-STACKS-MORPHISMS-FIDELITY-023 — `lemma-etale-smooth-local-source-target`

[Source officielle, ligne 7680](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L7680)

Retour au but X calligraphique dans la dernière vérification source ; le but Y avait été substitué.

Source :
```tex
$Z$ and morphism $Z \to \mathcal{X}$ the base change
```
Traduction publiée :
```tex
$Z$ et tout morphisme $Z \to \mathcal{Y}$, le changement de base
```
Lecture retenue :
```tex
$Z$ et tout morphisme $Z \to \mathcal{X}$, le changement de base
```

## FR-STACKS-MORPHISMS-FIDELITY-024 — `remark-etale-smooth-base-change`

[Source officielle, ligne 7772](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L7772)

Les deux bases Y et Y primé avaient été échangées pour rendre les produits typés. Restauration conjointe de la formule officielle ; la correction est conservée comme telle.

Source :
```tex
V' \times_V U \to V' \times_\mathcal{Y}
(\mathcal{Y}' \times_{\mathcal{Y}'} \mathcal{X}) =
```
Traduction publiée :
```tex
V' \times_V U \to V' \times_{\mathcal{Y}'}
(\mathcal{Y}' \times_\mathcal{Y} \mathcal{X}) =
```
Lecture retenue :
```tex
V' \times_V U \to V' \times_\mathcal{Y}
(\mathcal{Y}' \times_{\mathcal{Y}'} \mathcal{X}) =
```

## FR-STACKS-MORPHISMS-FIDELITY-025 — `lemma-etale-permanence`

[Source officielle, ligne 8010](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L8010)

Le but W de cette réduction source avait été corrigé en V. Les autres morphismes vers W sont inchangés.

Source :
```tex
Hence it suffices to show that $U \to W$
```
Traduction publiée :
```tex
Il suffit donc de montrer que $U \to V$
```
Lecture retenue :
```tex
Il suffit donc de montrer que $U \to W$
```

## FR-STACKS-MORPHISMS-FIDELITY-026 — `lemma-image-proper-is-proper`

[Source officielle, ligne 8504](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L8504)

Une phrase définissant explicitement q primé avait été ajoutée. Bien que naturelle dans la preuve, elle ne figure pas dans le témoin officiel ; elle reste lisible dans ce dossier et est retirée du corps fidèle.

Source :
```tex
If $T \subset |\mathcal{Y}'|$ is closed, then
```
Traduction publiée :
```tex
Notons $q' : \mathcal{Y}' \to \mathcal{Z}'$ le changement de base de $q$.
Si $T
```
Lecture retenue :
```tex
Si $T
```

## FR-STACKS-MORPHISMS-FIDELITY-027 — `lemma-scheme-theoretic-image-existence`

[Source officielle, ligne 8621](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L8621)

L’anneau structural porte X dans cette seconde image source. La substitution de U, motivée par le contexte, est une correction distincte de la traduction.

Source :
```tex
\bigoplus\nolimits_{\alpha \in A} \mathcal{I}_\alpha \to \mathcal{O}_X
```
Traduction publiée :
```tex
\bigoplus\nolimits_{\alpha \in A} \mathcal{I}_\alpha \to \mathcal{O}_U
```
Lecture retenue :
```tex
\bigoplus\nolimits_{\alpha \in A} \mathcal{I}_\alpha \to \mathcal{O}_X
```

## FR-STACKS-MORPHISMS-FIDELITY-028 — `lemma-topology-scheme-theoretic-image`

[Source officielle, ligne 8800](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L8800)

Restauration de la notation source sans barres dans cette observation. Le reste de la preuve utilise déjà les barres conformément au témoin.

Source :
```tex
Observe that $v \in Z$.
```
Traduction publiée :
```tex
Remarquons que $v \in |Z|$.
```
Lecture retenue :
```tex
Remarquons que $v \in Z$.
```

## FR-STACKS-MORPHISMS-FIDELITY-029 — `lemma-scheme-theoretic-image-of-partial-section`

[Source officielle, ligne 8819](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L8819)

La preuve source porte Y comme but, tandis que son énoncé porte X. On sépare la correction de cette incohérence, sans modifier l’énoncé déjà conforme.

Source :
```tex
the morphism $s : \mathcal{V} \to \mathcal{Y}$ is quasi-compact.
```
Traduction publiée :
```tex
le morphisme $s : \mathcal{V} \to \mathcal{X}$ est quasi-compact.
```
Lecture retenue :
```tex
le morphisme $s : \mathcal{V} \to \mathcal{Y}$ est quasi-compact.
```

## FR-STACKS-MORPHISMS-FIDELITY-030 — `lemma-specialization`

[Source officielle, ligne 10152](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L10152)

Le prime de X calligraphique figure à cette occurrence source ; il avait été supprimé pour harmoniser la notation. Les deux autres flèches non primées restent intactes.

Source :
```tex
Namely, this image is the fibre of $|U| \to |\mathcal{X}'|$
```
Traduction publiée :
```tex
En effet, cette image est la fibre de $|U| \to |\mathcal{X}|$
```
Lecture retenue :
```tex
En effet, cette image est la fibre de $|U| \to |\mathcal{X}'|$
```

## FR-STACKS-MORPHISMS-FIDELITY-031 — `lemma-representable-decent`

[Source officielle, ligne 10214](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L10214)

L’hypothèse source emploie Y simple ; la preuve conserve ses Y calligraphiques. La traduction ne les harmonise plus silencieusement.

Source :
```tex
of algebraic stacks. Assume $Y$ is decent
```
Traduction publiée :
```tex
de champs algébriques. Supposons que $\mathcal{Y}$ soit décent
```
Lecture retenue :
```tex
de champs algébriques. Supposons que $Y$ soit décent
```

## FR-STACKS-MORPHISMS-FIDELITY-032 — `lemma-factor-through-residual-space`

[Source officielle, ligne 10605](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L10605)

La réduction source conserve X primé dans cette inclusion. Restauration locale du prime, sans harmoniser les paragraphes de la preuve.

Source :
```tex
$\mathcal{U} \subset \mathcal{X}'$ which is a gerbe.
```
Traduction publiée :
```tex
$\mathcal{U} \subset \mathcal{X}$ qui est une gerbe.
```
Lecture retenue :
```tex
$\mathcal{U} \subset \mathcal{X}'$ qui est une gerbe.
```

## FR-STACKS-MORPHISMS-FIDELITY-033 — `lemma-residual-space-closed`

[Source officielle, ligne 10649](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L10649)

Restauration du Z simple dans la première définition du sous-champ réduit ; la seconde égalité calligraphique est déjà conforme et reste inchangée.

Source :
```tex
be the reduced closed substack with $|Z| = \{x\}$
```
Traduction publiée :
```tex
le sous-champ ferm\'e r\'eduit tel que $|\mathcal{Z}| = \{x\}$
```
Lecture retenue :
```tex
le sous-champ ferm\'e r\'eduit tel que $|Z| = \{x\}$
```

## FR-STACKS-MORPHISMS-FIDELITY-034 — `definition-etale-smooth-P`

[Source officielle, ligne 7711](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-morphisms.tex#L7711)

La définition source renvoie au lemme local-source-target. La traduction substituait un autre lemme, vraisemblablement pour réparer ce renvoi. Le renvoi officiel est rétabli et les deux identifiants restent visibles pour examen.

Source :
```tex
\ref{lemma-local-source-target}
```
Traduction publiée :
```tex
\ref{lemma-etale-smooth-local-source-target}
```
Lecture retenue :
```tex
\ref{lemma-local-source-target}
```

## Explicitations conservées

### `lemma-existence-plus-flat-base-change`

La correspondance 1 à 1 entre sous-champs fermés et sous-espaces invariants est traduite par correspondance bijective. Les deux chiffres ne constituent pas des hypothèses indépendantes. Le contexte complet, les deux classes mises en correspondance, les trois assertions (a)–(c) et la preuve du changement de base sont conservés.

### `lemma-lift-valuation-ring-through-flat-morphism`

La barre fermante passe de l’argument de mathcal à sa suite. Cela conserve X calligraphique entre deux barres, la même application vers |Y| et toute l’hypothèse. C’est une correction de groupement TeX sans changement d’objet mathématique ; aucune erreur de la proposition n’est corrigée par ce déplacement.

## Limites

Les contextes de chaque opération ont été lus. Il reste à comparer les autres candidats, toute la prose et la terminologie, puis à reconstruire et publier les éditions complètes. Les identifiants historiques producteurs ne sont pas inventés : leur rapprochement reste à faire. Les mathématiques sources gouvernent ces restaurations ; aucune consultation initiale du canon terminologique n’est affirmée rétrospectivement. Une expertise humaine ultérieure est bienvenue, mais ne bloque pas le travail.
