# Chapitre 68 — différences conservées après comparaison

**Contrôle délimité des candidats mathématiques ; ce n’est pas une validation de toute la prose ni de toute la terminologie.**

[Restaurations avant/après](DECENT-SPACES_REVIEW.fr.md) · [Contextes](DECENT-SPACES_FORMULA_RETAINED_CANDIDATES.json) · [Contrôles](DECENT-SPACES_CANDIDATE_RECONCILIATION.json)

## `lemma-fun-property-reasonable`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L1107)

Le complément sur S explicite le cadre déjà fixé par la première phrase et la catégorie des faisceaux sur S. Il ne change ni base ni hypothèse ; contrairement aux changements de la formule A^n, cette explicitation est conservée.

Source :
```tex

```

Traduction conservée :
```tex
S
S
S
S
```

## `lemma-property-over-property`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L3746)

Les trois cas bêta, décent, raisonnable sont tous conservés, y compris raisonnable dans le dernier paragraphe. La différence de comparaison vient de mots anglais en mode mathématique traduits sous une commande text ; aucune propriété n’a été substituée.

Source :
```tex
\omega \in \{\beta, decent, reasonable\}
\omega = decent
\omega = reasonable
```

Traduction conservée :
```tex
\omega \in \{\beta, \text{décent}, \text{raisonnable}\}
\omega = \text{décent}
\omega = \text{raisonnable}
```

## `lemma-composition-relative-conditions`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L3802)

Les noms décent et raisonnable dans l’ensemble de propriétés traduisent les noms anglais, sans modifier les quantificateurs ni la composition.

Source :
```tex
\omega \in \{\beta, decent, reasonable\}
```

Traduction conservée :
```tex
\omega \in \{\beta, \text{décent}, \text{raisonnable}\}
```

## `lemma-descent-conditions`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L3839)

Les trois propriétés et leurs trois preuves sont conservées. Les noms français dans les formules restent français ; le dernier cas est bien raisonnable, et non un second cas décent.

Source :
```tex
\mathcal{P} \in \{(\beta), decent, reasonable\}
\mathcal{P} = decent
\mathcal{P} = reasonable
```

Traduction conservée :
```tex
\mathcal{P} \in \{(\beta), \text{décent}, \text{raisonnable}\}
\mathcal{P} = \text{décent}
\mathcal{P} = \text{raisonnable}
```

## `lemma-relative-conditions-local`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L3945)

Les deux listes gardent leur différence : très raisonnable figure dans la première, mais pas dans la seconde qui gouverne la condition (5). Les noms français sont conservés dans les formules.

Source :
```tex
\mathcal{P} \in \{(\beta), decent, reasonable, very\ reasonable\}
\mathcal{P} \in \{(\beta), decent, reasonable\}
```

Traduction conservée :
```tex
\mathcal{P} \in \{(\beta), \text{décent}, \text{raisonnable}, \text{très raisonnable}\}
\mathcal{P} \in \{(\beta), \text{décent}, \text{raisonnable}\}
```

## `lemma-generically-finite`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L4762)

Le point final du premier affichage est une ponctuation de phrase, conservée. Il ne faut pas le confondre avec les deux changements d’objets R vers U et U/R, qui sont rétablis séparément.

Source :
```tex
R = U \times_{V \times_Y X} U
```

Traduction conservée :
```tex
R = U \times_{V \times_Y X} U.
```

## `lemma-decent-Jacobson-ft-pts`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L5294)

Un point terminal est ajouté après U dans le diagramme de morphismes. C’est une ponctuation de phrase, non un nouvel objet.

Source :
```tex
\Spec(k') \times_X U \to \Spec(k) \times_X U \to U
```

Traduction conservée :
```tex
\Spec(k') \times_X U \to \Spec(k) \times_X U \to U.
```

## `lemma-punctured-spec`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/decent-spaces.tex#L5377)

Le point terminal après W dans la flèche affichée est conservé. Le changement du singleton en fibre dans la conclusion est, lui, une intervention sur l’argument et est rétabli séparément.

Source :
```tex
\Spec(\mathcal{O}_{U, u}/\mathfrak p') \setminus \{\mathfrak m_u/\mathfrak p'\} \longrightarrow W
```

Traduction conservée :
```tex
\Spec(\mathcal{O}_{U, u}/\mathfrak p') \setminus \{\mathfrak m_u/\mathfrak p'\} \longrightarrow W.
```

## Texte mathématique lisible

Les 14 [paires de texte alignées](DECENT-SPACES_READER_TEXT_CANDIDATES.json) et neuf [formules nommant des propriétés](DECENT-SPACES_PROPERTY_TEXT_PAIRS.json) ont été lues. Chaque occurrence reste liée à sa justification. Le masquage automatique ne suffit pas à distinguer décent de raisonnable ; les deux noms ont été vérifiés directement.

- « and » → « et » : Les mêmes membres sont reliés par une conjonction ; aucune alternative ni condition n’est ajoutée.
- « there exist » → « il existe » : Même quantification existentielle sur la chaîne ; ses indices sont restaurés séparément.
- « with » → « tels que » : Même subordination des contraintes à la chaîne quantifiée.
- « for all » → « pour tout » : Même quantificateur universel sur i et même borne n−1 après restauration.
- « fibres of \'etale morphisms from affines are finite » → « les fibres des morphismes étales issus d'affines sont finies » : La finitude porte sur les fibres des morphismes étales de source affine, pas sur les morphismes eux-mêmes.
- « points come from monomorphisms of spectra of fields » → « les points proviennent de monomorphismes de spectres de corps » : Le même critère de représentation des points par monomorphismes est conservé.
- « points come from quasi-compact monomorphisms of spectra of fields » → « les points proviennent de monomorphismes quasi-compacts de spectres de corps » : La quasi-compacité qualifie les monomorphismes dans les deux langues ; elle n’est pas perdue.
- « fibres of \'etale morphisms from affines are universally bounded » → « les fibres des morphismes étales issus d'affines sont universellement bornées » : Le qualificatif universellement distingue ce critère de la simple finitude du premier.
- « cover by \'etale morphisms from schemes quasi-compact onto their image » → « recouvrement par des morphismes étales issus de schémas, quasi-compacts sur leur image » : Le recouvrement étale de source schématique et la quasi-compacité sur l’image sont conservés ensemble.
- « representable » → « représentable » : Même propriété au sommet du diagramme ; les flèches ne changent pas.
- « very reasonable » → « très raisonnable » : Le premier degré de la chaîne de propriétés reste distinct de raisonnable et de décent.
- « reasonable » → « raisonnable » : Même propriété intermédiaire, non confondue avec décent.
- « decent » → « décent » : Même propriété, notamment celle portée par f sur la flèche d’implication.
- « quasi-separated » → « quasi-séparé » : Même hypothèse au second sommet du diagramme.
- « all diagonals » → « toutes les diagonales » : Le complément enlève toutes les diagonales, sans en sélectionner une sous-famille.
- « monomorphism where » → « monomorphisme où » : La condition porte sur le morphisme Spec(k) vers X.
- « is a field » → « est un corps » : La variable k garde la même restriction de corps.
- « lying over » → « au-dessus de » : Le même point x restreint les indices u de la somme disjointe.
- « locally constant maps » → « applications localement constantes » : Le spectre porte sur le même anneau d’applications G vers k ; localement n’est pas supprimé.

Les lectures françaises existantes sont conservées lorsque le contexte confirme leur sens. Aucune attestation externe pour chaque mot, ni consultation initiale du canon, n’est inventée. Travail assisté par IA sans relecture experte humaine ; les éditions complètes restent à reconstruire et publier.
