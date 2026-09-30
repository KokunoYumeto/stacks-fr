# Chapitre 64 — Formules des traces : fidélité au texte officiel

**Réparation locale en cours ; aucune édition publique corrigée n’est encore certifiée.**

[LaTeX de travail](staged/fr/064_trace.fr.tex) · [Contrôles](TRACE_PARTIAL_VALIDATION.json) · [Contextes complets](TRACE_CONTEXTUAL_RESTORATIONS.json)

La traduction est non officielle et assistée par IA, sans relecture experte humaine. Le dossier sépare les propositions mathématiques des réparations propres à la traduction. Rétablir un passage ne signifie pas préférer sa mathématique à celle de la proposition écartée. Le témoin officiel reste inchangé.

## FR-TRACE-FIDELITY-001 — `proposition-integral-normal-fundamental-group`

[Source officielle, ligne 3051](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/trace.tex#L3051)

L’exposant i/2 corrige l’assertion source, qui porte 1/2. La correction est mathématiquement motivée mais ne doit pas rester silencieuse dans la traduction de cette version officielle.

Source :
```tex
$|\alpha|=q^{1/2}$
```
Traduction publiée :
```tex
$|\alpha|=q^{i/2}$
```
Lecture retenue :
```tex
$|\alpha|=q^{1/2}$
```

## FR-TRACE-FIDELITY-002 — `definition-unramified`

[Source officielle, ligne 3526](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/trace.tex#L3526)

Le signe égal isolé de la source avait été supprimé. On conserve ici même cette anomalie typographique dans le corps source-fidèle ; sa suppression reste proposée dans ce dossier.

Source :
```tex
and $dg = $ is the Haar measure
```
Traduction publiée :
```tex
et $dg$ désigne la mesure de Haar
```
Lecture retenue :
```tex
et $dg = $ désigne la mesure de Haar
```

## FR-TRACE-FIDELITY-003 — `section-chebotarev`

[Source officielle, ligne 3838](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/trace.tex#L3838)

Même restauration du signe égal source sans second membre. La proposition mathématique n’est pas réinterprétée : l’anomalie source reste explicitement identifiable.

Source :
```tex
Assume $Y_{\overline{k}} = $ irreducible.
```
Traduction publiée :
```tex
Supposons $Y_{\overline{k}}$ irréductible.
```
Lecture retenue :
```tex
Supposons $Y_{\overline{k}} = $ irréductible.
```

## FR-TRACE-FIDELITY-004 — `section-really`

[Source officielle, ligne 4012](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/trace.tex#L4012)

La source écrit k, non q, comme nombre d’éléments. La substitution naturelle par q est conservée comme correction proposée, non comme lecture officielle.

Source :
```tex
Fix $q$ and let $k$ be a field with $k$ elements.
```
Traduction publiée :
```tex
Fixons $q$ et soit $k$ un corps à $q$ éléments.
```
Lecture retenue :
```tex
Fixons $q$ et soit $k$ un corps à $k$ éléments.
```

## FR-TRACE-FIDELITY-005 — `proposition-integral-normal-fundamental-group`

[Source officielle, ligne 2913](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/trace.tex#L2913)

La source dit ici functions tandis qu’elle emploie functor ailleurs. La lecture littérale fonctions est restaurée pour ne pas harmoniser silencieusement cette occurrence ; ce choix n’affirme pas que fonctions est le terme catégorique correct.

Source :
```tex
there exists an isom. of fibre functions
```
Traduction publiée :
```tex
il existe un isomorphisme des foncteurs fibres
```
Lecture retenue :
```tex
il existe un isomorphisme des fonctions fibres
```

## FR-TRACE-FIDELITY-006 — `proposition-integral-normal-fundamental-group`

[Source officielle, ligne 3071](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/trace.tex#L3071)

La parenthèse source dit some, non same. La traduction explicitait une égalité en remplaçant cette parenthèse fragmentaire ; celle-ci est désormais traduite sans ajouter cette assertion.

Source :
```tex
compatible with $\rho$. (some char. polys of $F_x$'s)
```
Traduction publiée :
```tex
compatible avec $\rho$ (les polynômes caractéristiques des $F_x$ sont les mêmes).
```
Lecture retenue :
```tex
compatible avec $\rho$ (certains polynômes caractéristiques des $F_x$).
```

## FR-TRACE-FIDELITY-007 — `proposition-integral-normal-fundamental-group`

[Source officielle, ligne 2993](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/trace.tex#L2993)

La finitude est désormais explicite comme dans finite locally constant sheaves. Il ne s’agit pas d’affirmer que constructible était mathématiquement faux ; on évite de substituer silencieusement une caractérisation. Le registre localement constant fini est attesté par Zoonekynd, 2002, pp.106–107, réellement consultées après coup (TRACE_CONSULTED_CANON.json).

Source :
```tex
\text{fin. loc. const. sheaves of }
```
Traduction publiée :
```tex
faisceaux de \(\Lambda\)-modules localement constants constructibles sur
```
Lecture retenue :
```tex
faisceaux localement constants de \(\Lambda\)-modules finis sur
```

## FR-TRACE-FIDELITY-008 — `lemma-identify-h2c`

[Source officielle, ligne 3249](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/trace.tex#L3249)

La légende source est equivalent, non equivariant. La version française corrigeait le sens attendu de la flèche ; la lecture source est restaurée et la correction reste proposée séparément.

Source :
```tex
\text{equivalent}
```
Traduction publiée :
```tex
\text{équivariant}
```
Lecture retenue :
```tex
\text{équivalent}
```

## Explicitations conservées

### `proposition-integral-normal-fundamental-group`

Le tableau matriciel est réparti en deux tableaux textuels lisibles. Après la précision de finitude enregistrée séparément, la première équivalence relie les faisceaux de Lambda-modules finis localement constants aux modules finis discrets avec action continue du groupe fondamental ; la seconde relie les faisceaux l-adiques lisses aux Z_l-modules de type fini avec action continue pour la topologie l-adique. Les deux anneaux, groupes, actions, conditions de finitude et topologies ont été lus conjointement. Les mathématiques passées de dollars à des délimiteurs parenthésés restent explicitement présentes dans le contexte complet. Cette exception de mise en page n’est pas une égalité des multiensembles bruts.

### `section-profinite-cohomology`

L’environnement aligned coupe sur deux lignes le même foncteur RH^0(G,-), entre les mêmes catégories dérivées bornées inférieurement de modules discrets avec action de Gamma et de Gamma/G. Le déplacement de modules et l’expression équivariants ne modifient pas l’action. La continuité reste donnée par le paragraphe introductif et les catégories précédentes.

## Limites

Les contextes de chaque opération ont été lus. Il reste à comparer les autres candidats, toute la prose et la terminologie, puis à reconstruire et publier les éditions complètes. Les identifiants historiques producteurs ne sont pas inventés : leur rapprochement reste à faire. Les mathématiques sources gouvernent ces restaurations ; aucune consultation initiale du canon terminologique n’est affirmée rétrospectivement. Une expertise humaine ultérieure est bienvenue, mais ne bloque pas le travail.
