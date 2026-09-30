# Chapitre 67 — restaurations de la source officielle

**Réparation locale partielle ; ce dossier ne certifie ni le chapitre entier ni une édition publiée.**

[LaTeX de travail](staged/fr/067_spaces-morphisms.fr.tex) · [Validation réversible](SPACES-MORPHISMS_PARTIAL_VALIDATION.json) · [Contextes complets](SPACES-MORPHISMS_CONTEXTUAL_RESTORATIONS.json)

Les propositions d’amélioration de la source sont conservées dans la colonne logique avant/après : elles ne sont pas incorporées silencieusement à cette traduction non officielle du texte de référence. Rétablir la lecture originale ne signifie pas la juger mathématiquement préférable. Le texte anglais reste intact.

## FR-SPACES-MORPHISMS-FIDELITY-001 — `lemma-characterize-representable-quasi-compact`

[Source officielle, ligne 1026](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L1026)

Le témoin officiel porte Z dans cette fibre. X rendrait la preuve cohérente avec la définition de p, mais ce serait une correction de la source ; Z est rétabli dans la traduction de référence.

Source :
```tex
p^{-1}(U) = U \times_Y Z
```
Traduction publiée :
```tex
p^{-1}(U) = U \times_Y X
```
Lecture rétablie :
```tex
p^{-1}(U) = U \times_Y Z
```

## FR-SPACES-MORPHISMS-FIDELITY-002 — `lemma-characterize-representable-quasi-compact`

[Source officielle, ligne 1027](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L1027)

La seconde occurrence du même produit fibré doit conserver le même Z officiel ; la proposition de remplacer Z par X reste lisible dans cet avant/après.

Source :
```tex
and the scheme $U \times_Y Z$ is quasi-compact
```
Traduction publiée :
```tex
et le schéma $U \times_Y X$ est quasi-compact
```
Lecture rétablie :
```tex
et le schéma $U \times_Y Z$ est quasi-compact
```

## FR-SPACES-MORPHISMS-FIDELITY-003 — `lemma-quasi-compact-is-quasi-compact`

[Source officielle, ligne 1066](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L1066)

La traduction avait supprimé une égalité intermédiaire mal typée dans la source. La suppression est une réparation mathématique, non une ellipse grammaticale ; la chaîne officielle est restaurée.

Source :
```tex
|X'| = |f|^{-1}(|X'|) = |f|^{-1}(V)
```
Traduction publiée :
```tex
|X'| = |f|^{-1}(V)
```
Lecture rétablie :
```tex
|X'| = |f|^{-1}(|X'|) = |f|^{-1}(V)
```

## FR-SPACES-MORPHISMS-FIDELITY-004 — `lemma-characterize-representable-universally-closed`

[Source officielle, ligne 1313](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L1313)

La source choisit une présentation de Y alors que le diagramme semble exiger Z. La traduction ne doit pas résoudre silencieusement cette incohérence.

Source :
```tex
V \to Y
```
Traduction publiée :
```tex
V \to Z
```
Lecture rétablie :
```tex
V \to Y
```

## FR-SPACES-MORPHISMS-FIDELITY-005 — `lemma-universally-closed-quasi-compact`

[Source officielle, ligne 1495](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L1495)

Rétablissement du Z du témoin dans le complément fermé, sans prétendre que cette lecture circulaire est mathématiquement préférable à X.

Source :
```tex
|T \times_Y Z| \setminus \bigcup_{i \in I} |T_i \times_Y X_i|
```
Traduction publiée :
```tex
|T \times_Y X| \setminus \bigcup_{i \in I} |T_i \times_Y X_i|
```
Lecture rétablie :
```tex
|T \times_Y Z| \setminus \bigcup_{i \in I} |T_i \times_Y X_i|
```

## FR-SPACES-MORPHISMS-FIDELITY-006 — `lemma-universally-closed-quasi-compact`

[Source officielle, ligne 1516](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L1516)

Le passage officiel nomme Y_V. Remplacer son objet par X_V est une correction de preuve qui doit rester séparée.

Source :
```tex
Y_V \to V
```
Traduction publiée :
```tex
X_V \to V
```
Lecture rétablie :
```tex
Y_V \to V
```

## FR-SPACES-MORPHISMS-FIDELITY-007 — `lemma-universally-closed-quasi-compact`

[Source officielle, ligne 1525](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L1525)

L’argument de q a été changé de t à z. Malgré la motivation par le diagramme, la traduction de référence reprend t et expose séparément la proposition z.

Source :
```tex
q(t) \in X_i
```
Traduction publiée :
```tex
q(z) \in X_i
```
Lecture rétablie :
```tex
q(t) \in X_i
```

## FR-SPACES-MORPHISMS-FIDELITY-008 — `lemma-factor-the-other-way`

[Source officielle, ligne 2169](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L2169)

Le produit fibré a été retapé avec le changement de base vraisemblablement voulu. La base U et le facteur X officiels sont rétablis.

Source :
```tex
T = Z \times_U X
```
Traduction publiée :
```tex
T = Z \times_X U
```
Lecture rétablie :
```tex
T = Z \times_U X
```

## FR-SPACES-MORPHISMS-FIDELITY-009 — `lemma-stalk-push-closed`

[Source officielle, ligne 2403](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L2403)

Les deux points géométriques ont été échangés pour corriger le type des fibres. La formule officielle est conservée dans la traduction ; la formule corrigée reste dans cet enregistrement.

Source :
```tex
(i_{small, *}\mathcal{F})_{\overline{z}} = \mathcal{F}_{\overline{x}}
```
Traduction publiée :
```tex
(i_{small, *}\mathcal{F})_{\overline{x}} = \mathcal{F}_{\overline{z}}
```
Lecture rétablie :
```tex
(i_{small, *}\mathcal{F})_{\overline{z}} = \mathcal{F}_{\overline{x}}
```

## FR-SPACES-MORPHISMS-FIDELITY-010 — `lemma-stalk-push-closed`

[Source officielle, ligne 2409](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L2409)

La preuve emploie également z dans le témoin officiel. La restauration est liée à celle de l’énoncé, non étendue à toutes les autres occurrences des points.

Source :
```tex
Then the stalk $(i_{small, *}\mathcal{F})_{\overline{z}}$
```
Traduction publiée :
```tex
Alors la fibre $(i_{small, *}\mathcal{F})_{\overline{x}}$
```
Lecture rétablie :
```tex
Alors la fibre $(i_{small, *}\mathcal{F})_{\overline{z}}$
```

## FR-SPACES-MORPHISMS-FIDELITY-011 — `lemma-i-star-equivalence`

[Source officielle, ligne 2526](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L2526)

L’image directe i_* a été insérée dans le second facteur. Il s’agit d’une précision mathématique de la source, pas de traduction ; elle est retirée de cette seule occurrence.

Source :
```tex
i_*i^*\mathcal{F} = \mathcal{F} \otimes_{\mathcal{O}_X} \mathcal{O}_Z
```
Traduction publiée :
```tex
i_*i^*\mathcal{F} = \mathcal{F} \otimes_{\mathcal{O}_X} i_*\mathcal{O}_Z
```
Lecture rétablie :
```tex
i_*i^*\mathcal{F} = \mathcal{F} \otimes_{\mathcal{O}_X} \mathcal{O}_Z
```

## FR-SPACES-MORPHISMS-FIDELITY-012 — `lemma-i-star-equivalence`

[Source officielle, ligne 2564](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L2564)

Le français avait remplacé l’argument sommaire par une justification via l’adjonction et son morphisme. On rétablit l’argument effectivement écrit, inverse à gauche, déjà employé dans le point (2) de ce même texte français. Ce n’est pas une approbation de sa suffisance logique.

Source :
```tex
It is clear from part (2) that $i^{QCoh}_*$ is fully faithful since
it has a left inverse, namely $i^*$.
```
Traduction publiée :
```tex
Il résulte de (2) que $i^{QCoh}_*$ est pleinement fidèle, puisque
$i^*$ est son adjoint à gauche et que le morphisme d'adjonction de (2) est un isomorphisme.
```
Lecture rétablie :
```tex
Il résulte de (2) que $i^{QCoh}_*$ est pleinement fidèle, puisqu'il
a un inverse à gauche, à savoir $i^*$.
```

## FR-SPACES-MORPHISMS-FIDELITY-013 — `lemma-i-upper-shriek`

[Source officielle, ligne 2647](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L2647)

La traduction explicitait ici une définition du faisceau I que cette phrase anglaise ne donne pas. L’explication ajoutée est retirée, sans retirer le symbole I officiel.

Source :
```tex
annihilated by $\mathcal{I}$.
```
Traduction publiée :
```tex
annulées par le faisceau d'idéaux $\mathcal{I}$ définissant $Z$.
```
Lecture rétablie :
```tex
annulées par $\mathcal{I}$.
```

## FR-SPACES-MORPHISMS-FIDELITY-014 — `lemma-i-upper-shriek`

[Source officielle, ligne 2666](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L2666)

L’anglais conclut subschemes et non subspaces. La substitution française réparait la terminologie du contexte ; le terme source est rétabli, avec le registre sous-schéma attesté dans le passage français voisin.

Source :
```tex
of closed subschemes.
```
Traduction publiée :
```tex
de sous-espaces fermés.
```
Lecture rétablie :
```tex
de sous-schémas fermés.
```

## FR-SPACES-MORPHISMS-FIDELITY-015 — `lemma-scheme-theoretic-union`

[Source officielle, ligne 2724](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L2724)

Le faisceau d’anneaux de l’énoncé a été changé de O_Z à O_X. La lecture de référence reste O_Z même si la preuve justifie la proposition de correction.

Source :
```tex
of $\mathcal{O}_Z$-modules, and the diagram
```
Traduction publiée :
```tex
de $\mathcal{O}_X$-modules, et le diagramme
```
Lecture rétablie :
```tex
de $\mathcal{O}_Z$-modules, et le diagramme
```

## FR-SPACES-MORPHISMS-FIDELITY-016 — `lemma-scheme-theoretic-image`

[Source officielle, ligne 2997](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L2997)

La source dit closed subscheme à ce point précis, non closed subspace. La correction de type avait été silencieusement incorporée ; sous-schéma est restauré.

Source :
```tex
closed subscheme determined by $\mathcal{I}$
```
Traduction publiée :
```tex
sous-espace fermé défini par $\mathcal{I}$
```
Lecture rétablie :
```tex
sous-schéma fermé défini par $\mathcal{I}$
```

## FR-SPACES-MORPHISMS-FIDELITY-017 — `lemma-scheme-theoretic-image`

[Source officielle, ligne 3012](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L3012)

Deux couples de références à X et à son site avaient été remplacés par Y. L’opération restaure les quatre occurrences dans ce paragraphe seulement.

Source :
```tex
$X_\etale$ and $X$. As the category of quasi-coherent modules
on $X_\etale$ and $X$ are the same
```
Traduction publiée :
```tex
$Y_\etale$ et $Y$. Comme les catégories des modules quasi-cohérents
sur $Y_\etale$ et $Y$ sont les mêmes
```
Lecture rétablie :
```tex
$X_\etale$ et $X$. Comme les catégories des modules quasi-cohérents
sur $X_\etale$ et $X$ sont les mêmes
```

## FR-SPACES-MORPHISMS-FIDELITY-018 — `lemma-quasi-compact-scheme-theoretic-image`

[Source officielle, ligne 3060](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L3060)

Le symbole O_X′ officiel, non défini ici, avait été remplacé par f′_*O_U. On conserve la lecture du témoin sans attribuer cette correction aux auteurs.

Source :
```tex
\mathcal{I} = \Ker(\mathcal{O}_Y \to \mathcal{O}_{X'})
```
Traduction publiée :
```tex
\mathcal{I} = \Ker(\mathcal{O}_Y \to f'_*\mathcal{O}_U)
```
Lecture rétablie :
```tex
\mathcal{I} = \Ker(\mathcal{O}_Y \to \mathcal{O}_{X'})
```

## FR-SPACES-MORPHISMS-FIDELITY-019 — `lemma-quasi-compact-scheme-theoretic-image`

[Source officielle, ligne 3063](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L3063)

La source emploie coherent et la traduction quasi-cohérents. Le préfixe change la propriété mathématique ; il est retiré ici, sans changer les autres occurrences de quasi-cohérent dans la preuve.

Source :
```tex
as a kernel of a map between coherent modules.
```
Traduction publiée :
```tex
comme noyau d'un morphisme de modules quasi-cohérents.
```
Lecture rétablie :
```tex
comme noyau d'un morphisme de modules cohérents.
```

## FR-SPACES-MORPHISMS-FIDELITY-020 — `lemma-characterize-quasi-affine`

[Source officielle, ligne 4064](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L4064)

Le qualificatif étale, absent de la phrase source, avait été ajouté pour justifier le changement de base utilisé ensuite. On retire cet ajout mathématique, sans retirer la surjectivité officielle.

Source :
```tex
Let $U \to X$ be a surjective morphism where $U$ is a scheme.
```
Traduction publiée :
```tex
Soit $U \to X$ un morphisme étale surjectif, où $U$ est un schéma.
```
Lecture rétablie :
```tex
Soit $U \to X$ un morphisme surjectif, où $U$ est un schéma.
```

## FR-SPACES-MORPHISMS-FIDELITY-021 — `lemma-characterize-quasi-affine`

[Source officielle, ligne 4066](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L4066)

L’ouvert ou schéma de restriction V est celui écrit par la source, même si seul U a été introduit. Le remplacement motivé par le contexte reste une proposition séparée.

Source :
```tex
f_*\mathcal{O}_Y|_V
```
Traduction publiée :
```tex
f_*\mathcal{O}_Y|_U
```
Lecture rétablie :
```tex
f_*\mathcal{O}_Y|_V
```

## FR-SPACES-MORPHISMS-FIDELITY-022 — `lemma-local-source-target`

[Source officielle, ligne 4171](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L4171)

Rétablissement du but X indiqué par la phrase officielle, sans remplacer le changement de base déjà écrit sur Y.

Source :
```tex
Z \to X
```
Traduction publiée :
```tex
Z \to Y
```
Lecture rétablie :
```tex
Z \to X
```

## FR-SPACES-MORPHISMS-FIDELITY-023 — `definition-P-at-point`

[Source officielle, ligne 4278](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L4278)

L’uniformisation typographique du nom de propriété corrige une incohérence de la source. La traduction de référence conserve Q à cette occurrence, sans modifier les autres Q calligraphiques.

Source :
```tex
$Q$ in the following lemma means
```
Traduction publiée :
```tex
$\mathcal{Q}$ du lemme suivant signifie
```
Lecture rétablie :
```tex
$Q$ du lemme suivant signifie
```

## FR-SPACES-MORPHISMS-FIDELITY-024 — `lemma-finite-type-local`

[Source officielle, ligne 4442](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L4442)

La preuve française ajoutait étale à la phrase officielle. La correction suggérée par le contexte ne fait pas partie du témoin à traduire.

Source :
```tex
union of affines and a surjective morphism $V \to Y$
```
Traduction publiée :
```tex
disjointe de schémas affines et un morphisme étale surjectif $V \to Y$
```
Lecture rétablie :
```tex
disjointe de schémas affines et un morphisme surjectif $V \to Y$
```

## FR-SPACES-MORPHISMS-FIDELITY-025 — `lemma-finite-type-local`

[Source officielle, ligne 4460](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L4460)

La traduction remplaçait U=X par une présentation étale et ajoutait l’argument relatif au composé. L’argument source, même inadapté à un espace non représentable, doit rester reconnaissable ; sa correction est conservée dans ce dossier.

Source :
```tex
For (6) we can take $U = X$ and we're done.
```
Traduction publiée :
```tex
Pour (6), prenons une présentation étale surjective $U \to X$ par un schéma ; le morphisme composé est alors localement de type fini.
```
Lecture rétablie :
```tex
Pour (6), on peut prendre $U = X$, ce qui termine la preuve.
```

## FR-SPACES-MORPHISMS-FIDELITY-026 — `lemma-large-enough`

[Source officielle, ligne 4686](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L4686)

Le premier point géométrique avait été renommé pour homogénéiser la preuve. La désignation officielle x barre est rétablie.

Source :
```tex
\overline{x} : \Spec(k_v) \to V \to Y
```
Traduction publiée :
```tex
\overline{y}_v : \Spec(k_v) \to V \to Y
```
Lecture rétablie :
```tex
\overline{x} : \Spec(k_v) \to V \to Y
```

## FR-SPACES-MORPHISMS-FIDELITY-027 — `lemma-large-enough`

[Source officielle, ligne 4700](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L4700)

La preuve avait été réécrite simultanément de u,X,x vers v,Y,y pour corriger son raccord avec le premier paragraphe. Cette opération liée rétablit tout le passage officiel ; il ne s’agit pas d’un simple changement uniforme de variable à travers le lemme.

Source :
```tex
implies that the fields $k_u$ constructed in the first paragraph
of the proof all have cardinality bounded by $\lambda(X)$. Hence
by (\romannumeral2) we can find extensions $k_u \subset k'_u$ such that
$|k'_u| = \aleph$. The morphisms
$\overline{x}' : \Spec(k'_u) \to X$ cover $|X|$ as desired.
```
Traduction publiée :
```tex
les corps $k_v$ construits au premier paragraphe
de la démonstration ont tous une cardinalité majorée par $\lambda(Y)$. Par suite,
d'après (\romannumeral2), il existe des extensions $k_v \subset k'_v$ telles que
$|k'_v| = \aleph$. Les morphismes
$\overline{y}'_v : \Spec(k'_v) \to Y$ recouvrent $|Y|$, comme voulu.
```
Lecture rétablie :
```tex
les corps $k_u$ construits au premier paragraphe
de la démonstration ont tous une cardinalité majorée par $\lambda(X)$. Par suite,
d'après (\romannumeral2), il existe des extensions $k_u \subset k'_u$ telles que
$|k'_u| = \aleph$. Les morphismes
$\overline{x}' : \Spec(k'_u) \to X$ recouvrent $|X|$, comme voulu.
```

## FR-SPACES-MORPHISMS-FIDELITY-028 — `lemma-large-enough`

[Source officielle, ligne 4706](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L4706)

La discussion ensembliste qui suit conserve le schéma Spec(k′_u) du témoin, en cohérence avec le passage restauré, non Spec(k′_v).

Source :
```tex
$\Spec(k'_u)$
```
Traduction publiée :
```tex
$\Spec(k'_v)$
```
Lecture rétablie :
```tex
$\Spec(k'_u)$
```

## FR-SPACES-MORPHISMS-FIDELITY-029 — `lemma-large-enough`

[Source officielle, ligne 4725](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L4725)

Le numéro de partie a été rectifié dans la traduction. La référence interne officielle (2) est restaurée et la proposition (3) conservée séparément.

Source :
```tex
Hence part (2) follows
```
Traduction publiée :
```tex
La partie (3) résulte donc
```
Lecture rétablie :
```tex
La partie (2) résulte donc
```

## FR-SPACES-MORPHISMS-FIDELITY-030 — `lemma-point-finite-type-monomorphism`

[Source officielle, ligne 4997](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L4997)

Le nom du point dans la conclusion de la preuve avait été changé. On rétablit z sans modifier les occurrences précédentes de u.

Source :
```tex
the image of $z$ is $x$.
```
Traduction publiée :
```tex
l'image de $u$ est $x$.
```
Lecture rétablie :
```tex
l'image de $z$ est $x$.
```

## FR-SPACES-MORPHISMS-FIDELITY-031 — `lemma-finite-type-nagata`

[Source officielle, ligne 5033](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L5033)

Le témoin dit V, même si la dernière implication vers X semble exiger U ; la réparation de l’argument ne doit pas rester silencieuse.

Source :
```tex
Hence $V$ is a Nagata scheme by
```
Traduction publiée :
```tex
Ainsi, $U$ est un schéma de Nagata d'après
```
Lecture rétablie :
```tex
Ainsi, $V$ est un schéma de Nagata d'après
```

## FR-SPACES-MORPHISMS-FIDELITY-032 — `lemma-smooth-flat`

[Source officielle, ligne 7278](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L7278)

Le renvoi officiel vise la présentation finie, alors que la traduction a choisi le lemme sur la platitude. On rétablit la référence exacte ; le meilleur renvoi proposé reste visible ici.

Source :
```tex
\ref{morphisms-lemma-smooth-locally-finite-presentation}
```
Traduction publiée :
```tex
\ref{morphisms-lemma-smooth-flat}
```
Lecture rétablie :
```tex
\ref{morphisms-lemma-smooth-locally-finite-presentation}
```

## FR-SPACES-MORPHISMS-FIDELITY-033 — `lemma-fpqc-quotient-topology`

[Source officielle, ligne 5911](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L5911)

Les barres autour de T avaient été supprimées dans l’énoncé. Même si T est déjà une partie topologique, la notation officielle est rétablie ; les autres f^{-1}(T) de la preuve restent inchangés.

Source :
```tex
$f^{-1}(|T|)$ is open (resp.\ closed) in $|X|$.
```
Traduction publiée :
```tex
$f^{-1}(T)$ est ouverte (resp.\ fermée) dans $|X|$.
```
Lecture rétablie :
```tex
$f^{-1}(|T|)$ est ouverte (resp.\ fermée) dans $|X|$.
```

## FR-SPACES-MORPHISMS-FIDELITY-034 — `lemma-fpqc-quotient-topology`

[Source officielle, ligne 5917](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L5917)

La traduction avait nommé g pour expliquer son emploi ultérieur. L’introduction de cette notation est un ajout éditorial, retiré de la traduction de référence sans effacer le g ultérieur de la source.

Source :
```tex
V = \coprod V_i \to Y
```
Traduction publiée :
```tex
g : V = \coprod V_i \to Y
```
Lecture rétablie :
```tex
V = \coprod V_i \to Y
```

## FR-SPACES-MORPHISMS-FIDELITY-035 — `lemma-flat-base-change-scheme-theoretic-image`

[Source officielle, ligne 6094](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L6094)

Le but du premier morphisme avait été corrigé de Y à X à la fin de la preuve. Le témoin porte Y à cette occurrence ; le changement de base de l’énoncé conserve son but X.

Source :
```tex
similarly for $V \times_Y X \to Y$ and $W \times_Y X \to X$.
```
Traduction publiée :
```tex
de même pour $V \times_Y X \to X$ et $W \times_Y X \to X$.
```
Lecture rétablie :
```tex
de même pour $V \times_Y X \to Y$ et $W \times_Y X \to X$.
```

## FR-SPACES-MORPHISMS-FIDELITY-036 — `lemma-pf-flat-module-open`

[Source officielle, ligne 6336](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L6336)

Le faisceau d’anneaux et le module ont été remplacés ensemble pour corriger le type du changement de base. On rétablit O_V et le tiré en arrière par varphi exactement tels qu’écrits, tout en conservant la proposition plus cohérente dans le dossier.

Source :
```tex
$\mathcal{O}_V$-module $\varphi^*\mathcal{F}$.
```
Traduction publiée :
```tex
$\mathcal{O}_U$-module quasi-cohérent $\mathcal{F}|_U$.
```
Lecture rétablie :
```tex
$\mathcal{O}_V$-module quasi-cohérent $\varphi^*\mathcal{F}$.
```

## FR-SPACES-MORPHISMS-FIDELITY-037 — `lemma-valuative-criterion-representable`

[Source officielle, ligne 8201](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L8201)

La définition officielle de X_A contient Y comme dernier facteur. La substitution par X corrige vraisemblablement une coquille, mais n’appartient pas à une traduction sans correction silencieuse.

Source :
```tex
X_A = \Spec(A) \times_Y Y
```
Traduction publiée :
```tex
X_A = \Spec(A) \times_Y X
```
Lecture rétablie :
```tex
X_A = \Spec(A) \times_Y Y
```

## FR-SPACES-MORPHISMS-FIDELITY-038 — `lemma-finite-separable-enough`

[Source officielle, ligne 8277](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L8277)

Le prime ajouté à B sélectionnait l’anneau local introduit juste avant. La source écrit B sans prime ; cette lecture est rétablie sans décider silencieusement de l’anneau voulu. L’article défini traduit the sans renforcer l’antécédent.

Source :
```tex
Let $\mathfrak m \subset B$
be the maximal ideal.
```
Traduction publiée :
```tex
Soit $\mathfrak m \subset B'$
son idéal maximal.
```
Lecture rétablie :
```tex
Soit $\mathfrak m \subset B$
l'idéal maximal.
```

## FR-SPACES-MORPHISMS-FIDELITY-039 — `lemma-push-down-solution`

[Source officielle, ligne 8389](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L8389)

La justification de surjectivité nomme X dans le témoin et Z dans la traduction publiée. La proposition Z peut être motivée par le contexte, mais reste extérieure au texte traduit de référence.

Source :
```tex
as $X \to \Spec(A)$ is surjective).
```
Traduction publiée :
```tex
puisque $Z \to \Spec(A)$ est surjectif).
```
Lecture rétablie :
```tex
puisque $X \to \Spec(A)$ est surjectif).
```

## FR-SPACES-MORPHISMS-FIDELITY-040 — `lemma-push-down-solution`

[Source officielle, ligne 8391](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L8391)

Le but X de la dernière reformulation avait été remplacé par Spec(A). La lecture officielle est restaurée ; les morphismes de la phrase précédente ne sont pas modifiés.

Source :
```tex
in other words, $V \to X$ is \'etale.
```
Traduction publiée :
```tex
autrement dit, $V \to \Spec(A)$ est étale.
```
Lecture rétablie :
```tex
autrement dit, $V \to X$ est étale.
```

## FR-SPACES-MORPHISMS-FIDELITY-041 — `equation-start-with`

[Source officielle, ligne 8831](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L8831)

Le troisième objet remplacé par son réduit est S dans le témoin, non Y. On retire la correction contextuelle silencieuse de la traduction.

Source :
```tex
replace $U$, $X$, and $S$ by their respective reductions
```
Traduction publiée :
```tex
remplacer $U$, $X$ et $Y$ par leurs réductions respectives
```
Lecture rétablie :
```tex
remplacer $U$, $X$ et $S$ par leurs réductions respectives
```

## FR-SPACES-MORPHISMS-FIDELITY-042 — `equation-start-with`

[Source officielle, ligne 8938](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L8938)

La base de la diagonale finale a été changée de S à Y. La traduction de référence conserve S et documente la proposition Y séparément.

Source :
```tex
\Delta : X \to X \times_S X
```
Traduction publiée :
```tex
\Delta : X \to X \times_Y X
```
Lecture rétablie :
```tex
\Delta : X \to X \times_S X
```

## FR-SPACES-MORPHISMS-FIDELITY-043 — `lemma-characterize-normalization`

[Source officielle, ligne 9854](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L9854)

Le domaine de g avait été rectifié conformément au diagramme. La phrase officielle porte X, et cette incohérence doit être visible sans être réparée dans la traduction.

Source :
```tex
g : X \to Z
```
Traduction publiée :
```tex
g : Y \to Z
```
Lecture rétablie :
```tex
g : X \to Z
```

## FR-SPACES-MORPHISMS-FIDELITY-044 — `lemma-nagata-normalization-finite`

[Source officielle, ligne 10006](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L10006)

Le second faisceau de sections est O_X dans cette inclusion source. La phrase suivante emploie déjà O_U et ne doit pas être modifiée par une substitution globale.

Source :
```tex
\Gamma(X, \mathcal{O}_X) \subset \Gamma(U, \mathcal{O}_X)
```
Traduction publiée :
```tex
\Gamma(X, \mathcal{O}_X) \subset \Gamma(U, \mathcal{O}_U)
```
Lecture rétablie :
```tex
\Gamma(X, \mathcal{O}_X) \subset \Gamma(U, \mathcal{O}_X)
```

## FR-SPACES-MORPHISMS-FIDELITY-045 — `lemma-flat-locally-finite-type-points-codimension-0`

[Source officielle, ligne 10129](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L10129)

La preuve officielle place ces points dans U, alors que la traduction avait corrigé U en V. La lecture source est rétablie dans cette proposition seulement.

Source :
```tex
codimension $0$ points in $U$ and these are locally finite by
```
Traduction publiée :
```tex
points de codimension $0$ de $V$, lesquels sont localement en nombre fini par
```
Lecture rétablie :
```tex
points de codimension $0$ de $U$, lesquels sont localement en nombre fini par
```

## FR-SPACES-MORPHISMS-FIDELITY-046 — `lemma-normalization`

[Source officielle, ligne 10188](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L10188)

Le passage rappelant la propriété (c) utilise X et Y dans le témoin, malgré ses variables U et V. L’uniformisation du français corrigeait le raccord ; on rétablit la chaîne officielle sans renommer le reste du lemme.

Source :
```tex
X^\nu \to X \to Y
```
Traduction publiée :
```tex
U^\nu \to U \to V
```
Lecture rétablie :
```tex
X^\nu \to X \to Y
```

## FR-SPACES-MORPHISMS-FIDELITY-047 — `lemma-normalization-normal`

[Source officielle, ligne 10377](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L10377)

La lettre f avait été ajoutée dans l’énoncé pour donner un antécédent à f(z). Cet ajout est utile mais éditorial ; le f(z) ultérieur reste tel que dans la source.

Source :
```tex
Let $Z \to X$ be a morphism.
```
Traduction publiée :
```tex
Soit $f : Z \to X$ un morphisme.
```
Lecture rétablie :
```tex
Soit $Z \to X$ un morphisme.
```

## FR-SPACES-MORPHISMS-FIDELITY-048 — `lemma-neighbourhood-scheme`

[Source officielle, ligne 10581](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L10581)

La source emploie ici U′ sans l’avoir explicitement nommé, et la traduction substituait le produit fibré vraisemblablement voulu. On conserve l’identifiant officiel, avec la proposition explicative séparée.

Source :
```tex
Because $U'$ is quasi-affine over $T'$
```
Traduction publiée :
```tex
Comme $T' \times_T U$ est quasi-affine sur $T'$
```
Lecture rétablie :
```tex
Comme $U'$ est quasi-affine sur $T'$
```

## FR-SPACES-MORPHISMS-FIDELITY-049 — `lemma-integral-universally-injective-push-pull`

[Source officielle, ligne 11016](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-morphisms.tex#L11016)

L’image essentielle est décrite sur Y_etale dans l’énoncé source. Le français la replaçait sur X_etale ; cette correction du site est retirée de la traduction de référence.

Source :
```tex
$Y_\etale$ whose support is contained in $f(|Y|)$.
```
Traduction publiée :
```tex
$X_\etale$ dont le support est contenu dans $f(|Y|)$.
```
Lecture rétablie :
```tex
$Y_\etale$ dont le support est contenu dans $f(|Y|)$.
```

## Différences conservées

### `equation-start-with`

Le point final dans la définition affichée de C est omis pour raccorder grammaticalement qui est un anneau de valuation. Aucun symbole algébrique ni aucune condition de cette définition n’est modifié ; les changements S/Y de ce même bloc sont, eux, restaurés séparément.

### `lemma-closed-immersion-rings`

Le point terminal après la formule a été omis parce que la phrase continue par est un isomorphisme. Les objets, le morphisme et son assertion sont identiques ; aucune restauration mathématique n’est requise.

## Portée de la preuve et travail restant

Les lectures sont justifiées par la comparaison exacte avec le Stacks Project gelé. Le vocabulaire français de ces passages est conservé, notamment inverse à gauche déjà présent au point (2), et sous-schéma déjà présent dans la comparaison avec les schémas. Ce dossier ne prétend pas que chaque mot possède une attestation externe ni que les producteurs avaient consulté un canon. L’audit terminologique intégral reste distinct.

Les identifiants des candidats producteurs restent à rapprocher. Les écarts ultérieurs, les références et la prose hors passages examinés, puis la reconstruction des lecteurs et la publication corrigée, restent à traiter. Dossier AI, sans validation humaine experte ; une relecture ultérieure est bienvenue sans constituer une attente bloquante.
