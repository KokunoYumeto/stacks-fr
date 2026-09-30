# Chapitre 58 — variantes conservées après comparaison

**Examen des candidats mathématiques ; la prose entière et la terminologie ne sont pas certifiées.**

60 rétablissements du témoin officiel figurent dans le [dossier avant/après](PIONE_REVIEW.fr.md). Les huit blocs ci-dessous sont conservés pour les raisons explicites données après lecture des passages.

[Contextes et différences exactes](PIONE_FORMULA_RETAINED_CANDIDATES.json) · [Contrôles](PIONE_CANDIDATE_RECONCILIATION.json)

## `definition-G-set-continuous`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L44)

La seconde occurrence de G dans « If G is an abstract group G » est une répétition grammaticale supprimée en français. Le groupe abstrait, la topologie discrète et l'identification avec la définition précédente restent tous explicitement présents.

## `lemma-finite-etale-on-proper-over-henselian`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L1622)

Appliquer la surjectivité essentielle au schéma U ×_X V traduit ici la substitution de paramètre écrite « applied to X = U ×_X V ». Ce n'est pas la suppression d'une égalité portant sur le X fixé : le rôle de schéma auquel on applique le résultat est explicitement conservé.

## `lemma-finite-etale-on-proper-over-henselian-pair`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L1749)

Même substitution de paramètre : « au schéma U ×_X V » conserve le sens de l'application de la surjectivité essentielle. Les autres restaurations de ce bloc sont consignées séparément.

## `lemma-ses-field`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L3469)

Spec{k'} et Spec(k') désignent le spectre du même corps ; les parenthèses sont notationnelles. L'indice σ ∈ Gal(k̄/k) sous la réunion reprend exactement la quantification qui introduit s^σ dans la phrase précédente. Aucun automorphisme, corps ou domaine d'indexation n'est ajouté au raisonnement.

## `lemma-reformulate-purity-normal`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L4793)

Le tableau français place A devant algèbres, puis conserve finies, normales, la flèche Spec(B) vers X et son caractère étale au-dessus de U. L'application V vers Γ(V,O_V), l'équivalence et la condition finale sont inchangées. Le déplacement de A autour du texte traduit n'est pas une modification mathématique.

## `proposition-specialization-map-isomorphism`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L6623)

La sous-extension finie séparable L/K de la clôture algébrique est une explicitation linguistique de la tour notée K̄/L/K, non une modification des corps ni de l'hypothèse. Les deux autres changements de ce bloc sont traités séparément.

## `theorem-specialization-map-isomorphism-prime-to-p`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L6743)

L'occurrence supplémentaire de $p$ ne fait que mettre en mode mathématique le p de l'expression anglaise prime-to-p ; aucune hypothèse ou lettre nouvelle n'est ajoutée.

## `lemma-extend-covering`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L7198)

Dans le passage « This is a normal integral scheme », le démonstratif vise V_0 : sa définition, son image dans σ(S) et son identification à σ(U) l'établissent dans les deux témoins. Le français nomme V_0 au lieu de répéter ce démonstratif. C'est une résolution d'anaphore, non une assertion supplémentaire. Les quatre autres différences de ce bloc sont restaurées séparément.

## Texte lisible dans les formules

Les 64 [paires de formules alignées](PIONE_READER_TEXT_CANDIDATES.json) ont été lues intégralement. Le registre lie chaque occurrence à sa différence exacte et à sa raison. Le préfixe notationnel Finite- reste inchangé ; sa localisation stylistique n’est pas assimilée ici à une erreur mathématique.

- « -Sets » → « -Ensembles » : Même catégorie des ensembles munis de l’action du groupe préfixé.
- « Sets » → « Ensembles » : Même catégorie des ensembles et mêmes foncteurs.
- « schemes \'etale over » → « schémas étales sur » : Même classe de schémas étales sur le corps affiché.
- « open, normal, finite index » → « ouvert, distingué, d'indice fini » : Les trois conditions sur le sous-groupe sont conservées.
- « open, normal, finite idex » → « ouvert, distingué, d'indice fini » : Même condition que précédemment ; la coquille anglaise idex est traduite idiomatiquement, sans changement d’indice.
- « and » → « et » : Conjonction des mêmes conditions ou identités.
- « the underlying set of points of the scheme » → « l'ensemble sous-jacent des points du schéma » : Même ensemble de points de la fibre schématique affichée.
- « base change » → « changement de base » : Même foncteur de changement de base, dans le même diagramme.
- « F\'et » → « F\'Et » : Majuscule typographique dans la même abréviation de catégorie de revêtements finis étales ; ni catégorie ni foncteur n’est changé.
- « prime to » → « premier à » : Même condition de coprimalité de n et p, non une hypothèse de primalité de n.
- « open » → « ouvert » : Même système d’ouverts dans l’indice de colimite.
- « open, » → « ouvert, » : Même condition sur l’ouvert dans l’indice de colimite ; U_0 ⊂ U a été restauré séparément.
- « category of schemes finite \'etale over » → « catégorie des schémas finis étales sur » : La finitude, le caractère étale et la base U prime sont tous conservés.
- « for » → « pour » : Même condition i > 0 portant sur le degré de cohomologie.
- « open, normal, index prime to » → « ouvert, distingué, d'indice premier à » : Même quotient par les sous-groupes ouverts distingués dont l’indice est premier à p.
- « in » → « dans » : Même égalité dans l’anneau C.
- « element of » → « élément de » : Même élément de l’idéal (z), sans ajout d’une égalité particulière.

Le tableau « commutative / diagrams » devient « diagrammes / commutatifs » : les deux lignes sont traduites ensemble, avec l’ordre nominal français.

## Portée et incertitudes

Cette relecture rétrospective ne prétend ni qu’un canon externe avait été consulté lors de la traduction initiale, ni que chaque mot a maintenant une attestation externe. Les arguments de conservation ci-dessus viennent des passages comparés. Le canon effectivement consulté pour la réparation de target est indiqué dans le dossier avant/après. Une revue experte humaine reste bienvenue et n’est pas une condition préalable à la poursuite. Aucun lecteur reconstruit ni nouvelle édition publique n’est annoncé.
