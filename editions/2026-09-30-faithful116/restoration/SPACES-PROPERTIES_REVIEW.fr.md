# Chapitre 66 — Propriétés des espaces algébriques : fidélité au texte officiel

**Réparation locale en cours ; aucune édition publique corrigée n’est encore certifiée.**

[LaTeX de travail](staged/fr/066_spaces-properties.fr.tex) · [Contrôles](SPACES-PROPERTIES_PARTIAL_VALIDATION.json) · [Contextes complets](SPACES-PROPERTIES_CONTEXTUAL_RESTORATIONS.json)

La traduction est non officielle et assistée par IA, sans relecture experte humaine. Le dossier sépare les propositions mathématiques des réparations propres à la traduction. Rétablir un passage ne signifie pas préférer sa mathématique à celle de la proposition écartée. Le témoin officiel reste inchangé.

## FR-SPACES-PROPERTIES-FIDELITY-001 — `lemma-characterize-surjective`

[Source officielle, ligne 345](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L345)

Le morphisme à prouver surjectif est écrit vers T dans la source et vers Z dans la traduction ; cette correction de but est séparée du corps fidèle.

Source :
```tex
Z \times_X T \to T
```
Traduction publiée :
```tex
Z \times_X T \to Z
```
Lecture retenue :
```tex
Z \times_X T \to T
```

## FR-SPACES-PROPERTIES-FIDELITY-002 — `lemma-subspace-induced-topology`

[Source officielle, ligne 1407](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L1407)

La base Y de cette occurrence source avait été corrigée en X. Les autres produits sur X ne sont pas modifiés.

Source :
```tex
|Z \times_Y U| \to |Z|
```
Traduction publiée :
```tex
|Z \times_X U| \to |Z|
```
Lecture retenue :
```tex
|Z \times_Y U| \to |Z|
```

## FR-SPACES-PROPERTIES-FIDELITY-003 — `lemma-subspaces-presentation`

[Source officielle, ligne 1444](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L1444)

Retour au but Z de l’immersion imprimée. La proposition de remplacer ce but par U reste dans le dossier.

Source :
```tex
U \times_X Z \to Z
```
Traduction publiée :
```tex
U \times_X Z \to U
```
Lecture retenue :
```tex
U \times_X Z \to Z
```

## FR-SPACES-PROPERTIES-FIDELITY-004 — `lemma-map-into-reduction`

[Source officielle, ligne 1526](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L1526)

La conclusion officielle inverse les noms de l’énoncé. La traduction les avait corrigés ; cette correction n’appartient pas à une traduction diplomatique.

Source :
```tex
we conclude that $X \to Y$ factors
```
Traduction publiée :
```tex
on conclut que $Y \to X$ se factorise
```
Lecture retenue :
```tex
on conclut que $X \to Y$ se factorise
```

## FR-SPACES-PROPERTIES-FIDELITY-005 — `lemma-f-map`

[Source officielle, ligne 2736](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L2736)

La source indique Y étale pour le site de cette application ; restauration de ce site, sans modifier l’énoncé précédent.

Source :
```tex
is a map of sheaves on $Y_\etale$.
```
Traduction publiée :
```tex
soit un morphisme de faisceaux sur $X_\etale$.
```
Lecture retenue :
```tex
soit un morphisme de faisceaux sur $Y_\etale$.
```

## FR-SPACES-PROPERTIES-FIDELITY-006 — `lemma-f-map`

[Source officielle, ligne 2749](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L2749)

Le triplet de cette occurrence officielle est (V,U,g), non (U,V,g). L’uniformisation silencieuse est retirée.

Source :
```tex
$\varphi_{(V, U, g)} :
```
Traduction publiée :
```tex
$\varphi_{(U, V, g)} :
```
Lecture retenue :
```tex
$\varphi_{(V, U, g)} :
```

## FR-SPACES-PROPERTIES-FIDELITY-007 — `lemma-f-map`

[Source officielle, ligne 2775](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L2775)

Retour à U dans la base du produit fibré ; Y était une correction proposée de la source.

Source :
```tex
$U' \to X \times_U V'$ with $U'$ a scheme.
```
Traduction publiée :
```tex
$U' \to X \times_Y V'$ avec $U'$ schéma.
```
Lecture retenue :
```tex
$U' \to X \times_U V'$ avec $U'$ schéma.
```

## FR-SPACES-PROPERTIES-FIDELITY-008 — `lemma-f-map`

[Source officielle, ligne 2775](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L2775)

Les définitions explicites des deux symboles doublement primés ont été ajoutées dans la traduction. Elles sont gardées comme explication séparée ; le diagramme source reste intact.

Source :
```tex
We get a morphism of
schemes $g' : U' \to V'$ and also a morphism of schemes
```
Traduction publiée :
```tex
 Posons $U'' = U' \times_{X \times_Y V} U'$
et $V'' = V' \times_V V'$. Nous obtenons un morphisme de schémas $g' : U' \to V'$ ainsi qu'un morphisme de schémas
```
Lecture retenue :
```tex

Nous obtenons un morphisme de schémas $g' : U' \to V'$ ainsi qu'un morphisme de schémas
```

## FR-SPACES-PROPERTIES-FIDELITY-009 — `lemma-f-map`

[Source officielle, ligne 2786](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L2786)

Le coin inférieur gauche a été corrigé en G′(V). Le diagramme diplomatique reprend G′(X ×_Y V), avec la proposition conservée à part.

Source :
```tex
\mathcal{G}'(X \times_Y V) \ar[r] \ar@{..>}[u]
```
Traduction publiée :
```tex
\mathcal{G}'(V) \ar[r] \ar@{..>}[u]
```
Lecture retenue :
```tex
\mathcal{G}'(X \times_Y V) \ar[r] \ar@{..>}[u]
```

## FR-SPACES-PROPERTIES-FIDELITY-010 — `lemma-descent-sheaf`

[Source officielle, ligne 3017](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L3017)

La source écrit la projection zéro à la fois pour s et pour t. Restauration de l’indice source à s seulement.

Source :
```tex
s = \text{pr}_0
```
Traduction publiée :
```tex
s = \text{pr}_1
```
Lecture retenue :
```tex
s = \text{pr}_0
```

## FR-SPACES-PROPERTIES-FIDELITY-011 — `lemma-descent-sheaf`

[Source officielle, ligne 3026](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L3026)

La parenthèse fermante ajoutée répare une parenthèse manquante dans la source. Le texte de référence reste reproduit sans cette correction silencieuse ; le nom français du noyau du couple est conservé.

Source :
```tex
\mathcal{G}(V' \times_V V').
```
Traduction publiée :
```tex
\mathcal{G}(V' \times_V V')).
```
Lecture retenue :
```tex
\mathcal{G}(V' \times_V V').
```

## FR-SPACES-PROPERTIES-FIDELITY-012 — `definition-etale-neighbourhood`

[Source officielle, ligne 3097](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L3097)

Retour au nom singulier space effectivement présent à cette occurrence source ; les autres occurrences spaces restent inchangées.

Source :
```tex
X_{space, \etale}
```
Traduction publiée :
```tex
X_{spaces, \etale}
```
Lecture retenue :
```tex
X_{space, \etale}
```

## FR-SPACES-PROPERTIES-FIDELITY-013 — `lemma-cofinal-etale`

[Source officielle, ligne 3111](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L3111)

Le point géométrique s barre de la condition (2) a été corrigé en x barre. On rétablit la notation source de cette seule condition.

Source :
```tex
morphisms between \'etale neighborhoods of $\overline{s}$.
```
Traduction publiée :
```tex
morphismes entre voisinages \'etales de $\overline{x}$.
```
Lecture retenue :
```tex
morphismes entre voisinages \'etales de $\overline{s}$.
```

## FR-SPACES-PROPERTIES-FIDELITY-014 — `lemma-geometric-lift-to-cover`

[Source officielle, ligne 3224](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L3224)

L’image du point est nommée x dans la source et a été corrigée en u. La correction ne reste pas silencieusement dans la traduction.

Source :
```tex
$i$ and a point $u_i \in U_i$ mapping to $x$.
```
Traduction publiée :
```tex
$i$ et un point $u_i \in U_i$ envoyé sur $u$.
```
Lecture retenue :
```tex
$i$ et un point $u_i \in U_i$ envoyé sur $x$.
```

## FR-SPACES-PROPERTIES-FIDELITY-015 — `lemma-stalk-gives-point`

[Source officielle, ligne 3328](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L3328)

La dernière phrase de la preuve porte s barre dans la source. L’énoncé porte bien x barre et reste inchangé ; seule la correction silencieuse de cette dernière occurrence est retirée.

Source :
```tex
Finally, the our functor $\mathcal{F} \mapsto \mathcal{F}_{\overline{s}}$
```
Traduction publiée :
```tex
Enfin, notre foncteur $\mathcal{F} \mapsto \mathcal{F}_{\overline{x}}$
```
Lecture retenue :
```tex
Enfin, notre foncteur $\mathcal{F} \mapsto \mathcal{F}_{\overline{s}}$
```

## FR-SPACES-PROPERTIES-FIDELITY-016 — `theorem-exactness-stalks`

[Source officielle, ligne 3530](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L3530)

Restauration de S dans le critère d’exactitude des suites ; le critère d’injectivité ou de surjectivité précédent conserve X comme dans la source.

Source :
```tex
if and only if it is exact on all stalks at geometric points of $S$.
```
Traduction publiée :
```tex
si et seulement si elle est exacte sur toutes les fibres aux points géométriques de $X$.
```
Lecture retenue :
```tex
si et seulement si elle est exacte sur toutes les fibres aux points géométriques de $S$.
```

## FR-SPACES-PROPERTIES-FIDELITY-017 — `lemma-support-subsheaf-final`

[Source officielle, ligne 3624](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L3624)

Le but S figure dans l’indice de la réunion officielle. La correction en X est gardée comme proposition, non dans le texte diplomatique.

Source :
```tex
W = \bigcup_{\varphi : U \to S,
```
Traduction publiée :
```tex
W = \bigcup_{\varphi : U \to X,
```
Lecture retenue :
```tex
W = \bigcup_{\varphi : U \to S,
```

## FR-SPACES-PROPERTIES-FIDELITY-018 — `lemma-support-section-closed`

[Source officielle, ligne 3705](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L3705)

Retour à |X| dans la première assertion, même si les sections sont définies sur U dans les hypothèses.

Source :
```tex
The support of $\sigma$ is closed in $|X|$.
```
Traduction publiée :
```tex
Le support de $\sigma$ est fermé dans $|U|$.
```
Lecture retenue :
```tex
Le support de $\sigma$ est fermé dans $|X|$.
```

## FR-SPACES-PROPERTIES-FIDELITY-019 — `lemma-support-section-closed`

[Source officielle, ligne 3707](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L3707)

Retour à F(X) dans la deuxième assertion uniquement ; F(U) dans les hypothèses et dans la troisième assertion est déjà fidèle.

Source :
```tex
the supports of $\sigma, \sigma' \in \mathcal{F}(X)$.
```
Traduction publiée :
```tex
supports de $\sigma, \sigma' \in \mathcal{F}(U)$.
```
Lecture retenue :
```tex
supports de $\sigma, \sigma' \in \mathcal{F}(X)$.
```

## FR-SPACES-PROPERTIES-FIDELITY-020 — `lemma-etale-site-locally-ringed`

[Source officielle, ligne 3941](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L3941)

Le site est nommé S étale à cette occurrence de la preuve officielle ; l’uniformisation avec X étale est retirée du corps fidèle.

Source :
```tex
local, and because $S_\etale$ has enough points, see
```
Traduction publiée :
```tex
des anneaux locaux et que $X_\etale$ a assez de points ; voir le
```
Lecture retenue :
```tex
des anneaux locaux et que $S_\etale$ a assez de points ; voir le
```

## FR-SPACES-PROPERTIES-FIDELITY-021 — `lemma-quasi-separated-sober`

[Source officielle, ligne 1894](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L1894)

La source conserve des barres autour de T dans cette égalité. La simplification notationnelle est annulée sans modifier les autres occurrences de T.

Source :
```tex
$|Z| = |T|$
```
Traduction publiée :
```tex
$|Z| = T$
```
Lecture retenue :
```tex
$|Z| = |T|$
```

## FR-SPACES-PROPERTIES-FIDELITY-022 — `lemma-dimension-decent-invariant-under-etale`

[Source officielle, ligne 3979](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L3979)

L’ajout des barres explicite l’ensemble de points mais modifie la notation source. Retour à x dans X pour la version fidèle.

Source :
```tex
Let $x \in X$.
```
Traduction publiée :
```tex
Soit $x \in |X|$.
```
Lecture retenue :
```tex
Soit $x \in X$.
```

## FR-SPACES-PROPERTIES-FIDELITY-023 — `lemma-sheaf-gives-space`

[Source officielle, ligne 4678](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L4678)

Le passage à la catégorie des faisceaux a été ajouté dans la traduction. Restauration de la catégorie écrite dans la preuve officielle, avec cette proposition de correction conservée séparément.

Source :
```tex
$X \in \Ob((\Sch/S)_{fppf})$
```
Traduction publiée :
```tex
$X \in \Ob(\Sh((\Sch/S)_{fppf}))$
```
Lecture retenue :
```tex
$X \in \Ob((\Sch/S)_{fppf})$
```

## FR-SPACES-PROPERTIES-FIDELITY-024 — `lemma-2-morphism`

[Source officielle, ligne 4833](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L4833)

La source nomme seulement X comme espace sous-jacent aux deux noms primés. Le Y ajouté corrige implicitement cette phrase ; il reste dans la proposition d’erratum, pas dans le corps diplomatique.

Source :
```tex
Let $X'$, resp.\ $Y'$ be $X$ viewed as an algebraic space over
```
Traduction publiée :
```tex
Soient $X'$, resp.\ $Y'$, les espaces $X$, resp.\ $Y$, considérés comme espaces algébriques sur
```
Lecture retenue :
```tex
Soit $X'$, resp.\ $Y'$, l'espace $X$ considéré comme espace algébrique sur
```

## FR-SPACES-PROPERTIES-FIDELITY-025 — `lemma-isomorphism-ringed-topoi`

[Source officielle, ligne 5189](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L5189)

Retour au nom f de la composition dans la source ; g est une correction plausible, non une variante de traduction.

Source :
```tex
$q = f \circ p$
```
Traduction publiée :
```tex
$q = g \circ p$
```
Lecture retenue :
```tex
$q = f \circ p$
```

## FR-SPACES-PROPERTIES-FIDELITY-026 — `lemma-stalk-quasi-coherent`

[Source officielle, ligne 5312](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L5312)

Restauration du sous-indice u barre dans cette formule de la preuve, distinct de x barre dans l’énoncé qui était déjà fidèle.

Source :
```tex
\mathcal{F}_{\overline{u}} = \colim (\varphi^*\mathcal{F})_u
```
Traduction publiée :
```tex
\mathcal{F}_{\overline{x}} = \colim (\varphi^*\mathcal{F})_u
```
Lecture retenue :
```tex
\mathcal{F}_{\overline{u}} = \colim (\varphi^*\mathcal{F})_u
```

## FR-SPACES-PROPERTIES-FIDELITY-027 — `lemma-stalk-pullback-quasi-coherent`

[Source officielle, ligne 5357](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L5357)

Le diagramme officiel appelle a sa flèche du bas. La normalisation de ce nom en f est séparée du texte traduit.

Source :
```tex
X \ar[r]^a & Y
```
Traduction publiée :
```tex
X \ar[r]^f & Y
```
Lecture retenue :
```tex
X \ar[r]^a & Y
```

## FR-SPACES-PROPERTIES-FIDELITY-028 — `proposition-quasi-coherent`

[Source officielle, ligne 5783](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L5783)

La source répète la projection zéro pour s et t. Restauration de l’indice de s dans cette preuve seulement.

Source :
```tex
$s = \text{pr}_0$
```
Traduction publiée :
```tex
$s = \text{pr}_1$
```
Lecture retenue :
```tex
$s = \text{pr}_0$
```

## FR-SPACES-PROPERTIES-FIDELITY-029 — `proposition-quasi-coherent`

[Source officielle, ligne 5799](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L5799)

Le changement du sens de la flèche et l’image inverse ajoutée réparent le typage de la formule, mais constituent une correction source. Le texte fidèle reprend exactement les deux objets et le sens officiel.

Source :
```tex
c_f : \mathcal{F}_{V_1} \to \mathcal{F}_{V_2}
```
Traduction publiée :
```tex
c_f : f^*\mathcal{F}_{V_2} \to \mathcal{F}_{V_1}
```
Lecture retenue :
```tex
c_f : \mathcal{F}_{V_1} \to \mathcal{F}_{V_2}
```

## FR-SPACES-PROPERTIES-FIDELITY-030 — `proposition-quasi-coherent`

[Source officielle, ligne 5774](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-properties.tex#L5774)

La désignation lemme dans le corps officiel avait été corrigée en proposition. Même cette normalisation éditoriale reste séparée de la traduction de référence.

Source :
```tex
formula of the lemma.
```
Traduction publiée :
```tex
formule
affichée de la proposition.
```
Lecture retenue :
```tex
formule
affichée du lemme.
```

## Explicitations conservées

### `lemma-subspaces-presentation`

Le diagramme est disposé sur trois lignes dans gathered. Les mêmes sous-schémas Z′ de U stables par R correspondent aux mêmes sous-espaces Z de X. La réorganisation française et la mise en page sont conservées, indépendamment du but de l’immersion restauré dans la preuve.

### `lemma-subscheme`

La correspondance 1 - 1 est rendue par « correspondent biunivoquement ». La formule isolée devient du français sans perdre l’affirmation de bijectivité ; aucune modification des ouverts considérés ou de la preuve.

## Limites

Les contextes de chaque opération ont été lus. Il reste à comparer les autres candidats, toute la prose et la terminologie, puis à reconstruire et publier les éditions complètes. Les identifiants historiques producteurs ne sont pas inventés : leur rapprochement reste à faire. Les mathématiques sources gouvernent ces restaurations ; aucune consultation initiale du canon terminologique n’est affirmée rétrospectivement. Une expertise humaine ultérieure est bienvenue, mais ne bloque pas le travail.
