# Chapitre 64 — différences conservées après comparaison

**Comparaison délimitée des formules ; toute la prose et toute la terminologie ne sont pas certifiées.**

8 restaurations figurent dans le [dossier avant/après](TRACE_REVIEW.fr.md).

[Contextes complets](TRACE_FORMULA_RETAINED_CANDIDATES.json) · [Contrôles](TRACE_CANDIDATE_RECONCILIATION.json)

## `proposition-integral-normal-fundamental-group`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/trace.tex#L2891)

Le tableau matriciel est réparti en deux tableaux textuels lisibles. Après la précision de finitude enregistrée séparément, la première équivalence relie les faisceaux de Lambda-modules finis localement constants aux modules finis discrets avec action continue du groupe fondamental ; la seconde relie les faisceaux l-adiques lisses aux Z_l-modules de type fini avec action continue pour la topologie l-adique. Les deux anneaux, groupes, actions, conditions de finitude et topologies ont été lus conjointement. Les mathématiques passées de dollars à des délimiteurs parenthésés restent explicitement présentes dans le contexte complet. Cette exception de mise en page n’est pas une égalité des multiensembles bruts.

Source :
```tex
\begin{matrix} (\Lambda\text{ finite ring}) & \text{fin. loc. const. sheaves of } \atop \Lambda\text{-modules of }X_\etale & \leftrightarrow & \text{ finite (discrete) }\Lambda\text{-modules} \atop \text{ with continuous }\pi_1(X, \overline{x})\text{-action}\\ \\ (\ell\text{ a prime}) & \text{ lisse }\ell\text{-adic} \atop \text{ sheaves} & \leftrightarrow & \text{finitely generated }\mathbf{Z}_\ell \text{-modules }M\text{ with continuous} \atop \pi_1(X, \overline{x})\text{-action where we use } \ell\text{-adic topology on }M \end{matrix}
```

Traduction conservée :
```tex
\leftrightarrow
```

## `section-profinite-cohomology`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/trace.tex#L3095)

L’environnement aligned coupe sur deux lignes le même foncteur RH^0(G,-), entre les mêmes catégories dérivées bornées inférieurement de modules discrets avec action de Gamma et de Gamma/G. Le déplacement de modules et l’expression équivariants ne modifient pas l’action. La continuité reste donnée par le paragraphe introductif et les catégories précédentes.

Source :
```tex
RH^0(G, -) : D^{+}(\text{discrete }\Gamma\text{-modules}) \longrightarrow D^{+}(\text{discrete }\Gamma/G\text{-modules})
```

Traduction conservée :
```tex
\begin{aligned} RH^0(G, -) :\quad &D^{+}(\text{modules discrets }\Gamma\text{-équivariants})\\ &\longrightarrow D^{+}(\text{modules discrets }\Gamma/G\text{-équivariants}) \end{aligned}
```

## Texte dans les formules

Les 34 [paires alignées](TRACE_READER_TEXT_CANDIDATES.json) ont été lues. Chaque occurrence est reliée à sa règle ci-dessous ; ces comparaisons ne constituent pas des attestations externes.

- « conjugacy classes of » → « classes de conjugaison dans » : L’indice de somme reste les classes de conjugaison du même groupe G.
- « and » → « et » : Conjonction des mêmes morphismes, égalités ou conditions ; aucune condition n’est retirée.
- « forget filt » → « oubli de la filtration » : Le même complexe ou objet filtré est envoyé sur son objet sous-jacent ; les gradués et les limites de suite spectrale restent inchangés.
- « for » → « pour » : Même portée de n ou w dans les bornes de filtration ou de poids.
- « , and » → « , et » : Les deux conditions sur la filtration sont conjointes, avec leurs bornes exactes.
- « if » → « si » : Les branches par cas conservent exactement les mêmes indices et valeurs.
- « composition of » → « composition de » : Les endomorphismes alpha et beta et leur correspondant cyclique restent ceux du même tableau.
- « the trace form » → « la forme trace » : Même forme bilinéaire alpha,beta vers Tr(alpha beta), avec le même signe dans l’intégrale correspondante.
- « the Rosati involution » → « l'involution de Rosati » : Même involution alpha vers alpha daguerre et même opération sigma étoile dans le tableau.
- « positivity of Rosati » → « positivité de Rosati » : Même inégalité stricte pour la trace ; pas de modification du cas nul ni des hypothèses.
- « Hodge index theorem on » → « théorème de l'indice de Hodge sur » : Même renvoi au théorème appliqué à C fois C, avec la même inégalité écrite.
- « -conjugacy » → « -conjugaison » : Conservation de la conjugaison tordue par sigma dans l’indice ; la disposition source en fraction est inchangée.
- « in » → « dans » : Même espace affine A^3 pour le décompte de la famille de Legendre.
- « set of automorphisms of the functor » → « ensemble des automorphismes du foncteur » : Même définition du groupe fondamental à partir du même foncteur fibre.
- « profinite completion of » → « complété profini de » : Même complétion du groupe fondamental topologique, sans changer le groupe.
- « usual topology » → « topologie usuelle » : Même topologie sur X(C).
- « functoriality » → « fonctorialité » : Même justification de la flèche entre les groupes fondamentaux du point et de X.
- « on RHS » → « sur le membre de droite » : La torsion de l’action galoisienne porte sur le même membre de l’isomorphisme.
- « sheaf on » → « faisceau sur » : Même faisceau sur X, sans changer le quotient de coinvariants.
- « associated to » → « associé à » : Même association au module muni de son action indiqué immédiatement après.
- « irred. comp. of » → « composantes irréd. de » : Même indice de somme directe sur les composantes irréductibles de Y après changement de corps.
- « unr. cusp forms » → « formes cuspidales non ramifiées » : Même sous-ensemble de formes et mêmes relations avec U_v ; aucune ramification admise supplémentaire.
- « with coefficients in » → « à coefficients dans » : Même anneau Lambda de coefficients.
- « such that » → « telles que » : Les équations U_v f et leur quantification sur tous les v sont conservées.
- « abs irred » → « absolument irréductible » : L’irréductibilité absolue de la représentation, et non sa seule irréductibilité, est conservée.
- « eigen forms in » → « formes propres dans » : Même ensemble C(Lambda) et même correspondance avec les représentations.
- « finite » → « finie » : La finitude qualifie le même morphisme phi dans l’égalité cohomologique.
- « term for » → « terme pour » : Même terme correspondant à pi égal à 1.
- « error term (to be bounded by » → « terme d'erreur (à majorer par » : La même somme est le terme à majorer ; aucune borne supplémentaire n’est introduite.
- « set of all closed points of » → « ensemble de tous les points fermés de » : Le quantificateur tous et le caractère fermé des points sont conservés.
- « of degree » → « de degré » : Même borne de degré inférieur ou égal à N.
- « over » → « sur » : Même corps k sur lequel le degré des points est considéré.

## Limites

[Consultation réelle du canon](TRACE_CONSULTED_CANON.json) : Zoonekynd, pp.106–107, pour localement constant fini uniquement. Les tableaux et les changements d’ordre dans les paires 18, 20, 25 et 26 sont lus conjointement dans le fichier des paires, sans correspondance mot à mot fictive. Deux exceptions de mise en page sont localisées dans les contrôles ; les autres environnements ont le même ordre.

Les mots français préexistants sont conservés quand la comparaison en contexte en confirme le sens. Aucune consultation initiale du canon ni attestation externe pour chaque mot n’est inventée. Aucun lecteur reconstruit ni aucune édition publique corrigée n’est annoncé. Analyse assistée par IA, sans relecture experte humaine ; celle-ci reste bienvenue, sans être un préalable.
