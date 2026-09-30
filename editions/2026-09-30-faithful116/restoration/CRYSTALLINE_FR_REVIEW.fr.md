# Chapitre 60 — Cohomologie cristalline : fidélité à la source officielle

**Réparations locales, sans certification de l’édition entière ni remplacement des fichiers publics.**

[LaTeX de travail](staged/fr/060_crystalline.fr.tex) · [Contrôles](CRYSTALLINE_FR_PARTIAL_VALIDATION.json) · [Contextes complets](CRYSTALLINE_FR_CONTEXTUAL_RESTORATIONS.json) · [Canon consulté](CRYSTALLINE_FR_CONSULTED_CANON.json)

Les propositions mathématiques restent lisibles ci-dessous. Rétablir un texte source fautif ne revient pas à approuver sa correction mathématique. Les fichiers officiels et les témoins publics ne sont pas modifiés. Les réparations présentes sont assistées par IA, sans relecture humaine experte.

## FR-CRYSTALLINE-FIDELITY-001 — `lemma-describe-divided-power-envelope`

[Source officielle, ligne 237](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L237)

Le témoin écrit I comme ensemble des indices, bien que T ait été défini plus haut. La réparation en T est une proposition source séparée.

Source :
```tex
$t', t \in I$
```
Traduction publiée :
```tex
$t', t \in T$
```
Lecture retenue :
```tex
$t', t \in I$
```

## FR-CRYSTALLINE-FIDELITY-002 — `lemma-crystal-quasi-coherent-modules`

[Source officielle, ligne 2096](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L2096)

La source dit objet, non morphisme. Cette correction de la catégorie grammaticale et mathématique de f est séparée du texte fidèle.

Source :
```tex
Let $f : (U', T', \delta') \to (U, T, \delta)$ be an object of
```
Traduction publiée :
```tex
Soit $f : (U', T', \delta') \to (U, T, \delta)$ un morphisme de
```
Lecture retenue :
```tex
Soit $f : (U', T', \delta') \to (U, T, \delta)$ un objet de
```

## FR-CRYSTALLINE-FIDELITY-003 — `lemma-crystal-quasi-coherent-modules`

[Source officielle, ligne 2100](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L2100)

L’ordre T,U du recouvrement officiel avait été uniformisé en U,T ; restauration à cette occurrence seulement.

Source :
```tex
$\{(T_i, U_i, \delta_i) \to (T, U, \delta)\}$
```
Traduction publiée :
```tex
$\{(U_i, T_i, \delta_i) \to (U, T, \delta)\}$
```
Lecture retenue :
```tex
$\{(T_i, U_i, \delta_i) \to (T, U, \delta)\}$
```

## FR-CRYSTALLINE-FIDELITY-004 — `lemma-crystal-quasi-coherent-modules`

[Source officielle, ligne 2101](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L2101)

Même restauration des objets de la catégorie localisée ; les autres présentations en U,T de la source sont conservées.

Source :
```tex
$\mathcal{C}/(T_i, U_i, \delta_i)$
```
Traduction publiée :
```tex
$\mathcal{C}/(U_i, T_i, \delta_i)$
```
Lecture retenue :
```tex
$\mathcal{C}/(T_i, U_i, \delta_i)$
```

## FR-CRYSTALLINE-FIDELITY-005 — `lemma-crystal-quasi-coherent-modules`

[Source officielle, ligne 2103](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L2103)

La deuxième occurrence de f inverse U et T dans le témoin. Elle ne doit pas être uniformisée avec la première.

Source :
```tex
replace $f : (T', U', \delta') \to (T, U, \delta)$
```
Traduction publiée :
```tex
remplacer $f : (U', T', \delta') \to (U, T, \delta)$
```
Lecture retenue :
```tex
remplacer $f : (T', U', \delta') \to (T, U, \delta)$
```

## FR-CRYSTALLINE-FIDELITY-006 — `lemma-crystal-quasi-coherent-modules`

[Source officielle, ligne 2104](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L2104)

Restauration du triplet de changement de base effectivement écrit dans la source.

Source :
```tex
base change to $(T_i, U_i, \delta_i)$
```
Traduction publiée :
```tex
changement de base à $(U_i, T_i, \delta_i)$
```
Lecture retenue :
```tex
changement de base à $(T_i, U_i, \delta_i)$
```

## FR-CRYSTALLINE-FIDELITY-007 — `lemma-crystal-quasi-coherent-modules`

[Source officielle, ligne 2105](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L2105)

La restriction dans cette phrase doit reprendre T,U, malgré les U,T des formules suivantes.

Source :
```tex
restricted to $\mathcal{C}/(T, U, \delta)$
```
Traduction publiée :
```tex
à $\mathcal{C}/(U, T, \delta)$ admet une
```
Lecture retenue :
```tex
à $\mathcal{C}/(T, U, \delta)$ admet une
```

## FR-CRYSTALLINE-FIDELITY-008 — `item-completion`

[Source officielle, ligne 2780](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L2780)

On rétablit la source M et la cible faisant intervenir N. L’harmonisation avec K et M était une correction du texte anglais.

Source :
```tex
$h : M_* \longrightarrow \Hom(\Delta[1], N_*)$
```
Traduction publiée :
```tex
$h : K_* \longrightarrow \Hom(\Delta[1], M_*)$
```
Lecture retenue :
```tex
$h : M_* \longrightarrow \Hom(\Delta[1], N_*)$
```

## FR-CRYSTALLINE-FIDELITY-009 — `item-completion`

[Source officielle, ligne 2785](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L2785)

La cible de h_n utilise K_n dans le témoin, non M_n.

Source :
```tex
\prod\nolimits_{\alpha \in \Delta[1]_n} K_n
```
Traduction publiée :
```tex
\prod\nolimits_{\alpha \in \Delta[1]_n} M_n
```
Lecture retenue :
```tex
\prod\nolimits_{\alpha \in \Delta[1]_n} K_n
```

## FR-CRYSTALLINE-FIDELITY-010 — `item-completion`

[Source officielle, ligne 2813](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L2813)

L’exposant i ajouté à la première puissance extérieure est retiré. L’exposant de la cible, présent dans la source, reste inchangé.

Source :
```tex
\wedge_{A_n}(K_n)
```
Traduction publiée :
```tex
\wedge^i_{A_n}(K_n)
```
Lecture retenue :
```tex
\wedge_{A_n}(K_n)
```

## FR-CRYSTALLINE-FIDELITY-011 — `lemma-category-with-covering`

[Source officielle, ligne 3483](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L3483)

L’indice cosimplicial n avait été corrigé en n+1 ; le complexe affiché est déjà identique et n’est pas modifié.

Source :
```tex
$[n] \mapsto \mathcal{F}(X^n)$
```
Traduction publiée :
```tex
$[n] \mapsto \mathcal{F}(X^{n + 1})$
```
Lecture retenue :
```tex
$[n] \mapsto \mathcal{F}(X^n)$
```

## FR-CRYSTALLINE-FIDELITY-012 — `equation-cosimplicial-morphism`

[Source officielle, ligne 3567](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L3567)

La parenthèse supplémentaire réparait la source. La lecture diplomatique conserve son omission sans la déclarer bien formée.

Source :
```tex
M_*(f)(h_n(e_i)(\alpha^m_j \circ f) =
```
Traduction publiée :
```tex
M_*(f)(h_n(e_i)(\alpha^m_j \circ f)) =
```
Lecture retenue :
```tex
M_*(f)(h_n(e_i)(\alpha^m_j \circ f) =
```

## FR-CRYSTALLINE-FIDELITY-013 — `lemma-relative-poincare`

[Source officielle, ligne 3747](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L3747)

La source distingue ici integral de son précédent integrable. Le canon consulté atteste connexion intégrable, et le contexte suggère une coquille anglaise ; néanmoins, la remplacer silencieusement ajouterait une condition déterminée au texte de référence. Intégrale est ici une restitution littérale provisoire, non un terme français attesté pour une nouvelle notion. Voir le dossier de consultation et l’original exact.

Source :
```tex
endowed with an integral connection
```
Traduction publiée :
```tex
sur $D$, muni d'une connexion intégrable
```
Lecture retenue :
```tex
sur $D$, muni d'une connexion intégrale
```

## FR-CRYSTALLINE-FIDELITY-014 — `lemma-relative-poincare`

[Source officielle, ligne 3782](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L3782)

Le module de la phrase utilise B/A dans la source, alors que la formule suivante utilise P/A. La traduction avait supprimé cette discordance.

Source :
```tex
as complexes. Thus we can define a filtration $F^*$ on
$M \otimes_B \Omega^*_{B/A, \delta}$ by setting
```
Traduction publiée :
```tex
comme complexes. On peut donc définir une filtration $F^*$ de
$M \otimes_B \Omega^*_{P/A, \delta}$ en posant
```
Lecture retenue :
```tex
comme complexes. On peut donc définir une filtration $F^*$ de
$M \otimes_B \Omega^*_{B/A, \delta}$ en posant
```

## FR-CRYSTALLINE-FIDELITY-015 — `lemma-cohomology-is-zero`

[Source officielle, ligne 3901](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L3901)

Les trois exposants i du calcul intermédiaire avaient été ajoutés. Leurs occurrences dans les autres formules sources restent conservées.

Source :
```tex
\lim_e M(n)_e \otimes_{D(n)_e} \Omega_{D(n)}/p^e\Omega_{D(n)} \\
& = \lim_e M(n)_e \otimes_{D(n)} \Omega_{D(n)}
```
Traduction publiée :
```tex
\lim_e M(n)_e \otimes_{D(n)_e} \Omega^i_{D(n)}/p^e\Omega^i_{D(n)} \\
& = \lim_e M(n)_e \otimes_{D(n)} \Omega^i_{D(n)}
```
Lecture retenue :
```tex
\lim_e M(n)_e \otimes_{D(n)_e} \Omega_{D(n)}/p^e\Omega_{D(n)} \\
& = \lim_e M(n)_e \otimes_{D(n)} \Omega_{D(n)}
```

## FR-CRYSTALLINE-FIDELITY-016 — `lemma-compute-cohomology-crystal-smooth`

[Source officielle, ligne 4007](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L4007)

Le premier produit tensoriel est non complété dans le témoin. Les produits explicitement complétés plus bas ne sont pas touchés.

Source :
```tex
base change $M = M' \otimes_{D', b} D$
```
Traduction publiée :
```tex
changement de base $M = M' \otimes^\wedge_{D', b} D$
```
Lecture retenue :
```tex
changement de base $M = M' \otimes_{D', b} D$
```

## FR-CRYSTALLINE-FIDELITY-017 — `lemma-compute-cohomology-crystal-smooth`

[Source officielle, ligne 4060](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L4060)

Première occurrence après sigma : le témoin écrit x_i et non xi_i. La factorisation avec xi_i plus haut reste intacte.

Source :
```tex
$M \otimes^\wedge_{D, \sigma} \Omega^*_{D\langle x_i \rangle^\wedge}$.
```
Traduction publiée :
```tex
$M \otimes^\wedge_{D, \sigma} \Omega^*_{D\langle \xi_i \rangle^\wedge}$.
```
Lecture retenue :
```tex
$M \otimes^\wedge_{D, \sigma} \Omega^*_{D\langle x_i \rangle^\wedge}$.
```

## FR-CRYSTALLINE-FIDELITY-018 — `lemma-compute-cohomology-crystal-smooth`

[Source officielle, ligne 4062](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L4062)

La cible de l’inverse à gauche est également rétablie avec x_i, sans uniformisation des variables.

Source :
```tex
$D \to D\langle x_i \rangle^\wedge$
```
Traduction publiée :
```tex
$D \to D\langle \xi_i \rangle^\wedge$
```
Lecture retenue :
```tex
$D \to D\langle x_i \rangle^\wedge$
```

## FR-CRYSTALLINE-FIDELITY-019 — `lemma-compute-cohomology-crystal-smooth`

[Source officielle, ligne 4065](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L4065)

Deuxième occurrence dans le quasi-isomorphisme induit par tau : même restauration du x_i source.

Source :
```tex
$M \otimes^\wedge_{D, \sigma} \Omega^*_{D\langle x_i \rangle^\wedge}$
with
```
Traduction publiée :
```tex
$M \otimes^\wedge_{D, \sigma} \Omega^*_{D\langle \xi_i \rangle^\wedge}$
vers
```
Lecture retenue :
```tex
$M \otimes^\wedge_{D, \sigma} \Omega^*_{D\langle x_i \rangle^\wedge}$
vers
```

## FR-CRYSTALLINE-FIDELITY-020 — `example-torsion`

[Source officielle, ligne 4170](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L4170)

Le changement de n en r anticipait la notation de l’exemple suivant. Le témoin emploie n dans cette phrase.

Source :
```tex
even for affine $n$-space
```
Traduction publiée :
```tex
même pour l'espace affine de dimension $r$
```
Lecture retenue :
```tex
même pour l'espace affine de dimension $n$
```

## FR-CRYSTALLINE-FIDELITY-021 — `example-torsion`

[Source officielle, ligne 4159](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L4159)

Réparation française uniquement : l’adjectif s’accorde avec endomorphisme, masculin. La négation et le résultat mathématique restent identiques.

Source :
```tex
\to H^0(\text{Cris}(X/S), \mathcal{O}_{X/S})$ is not injective.
```
Traduction publiée :
```tex
\to H^0(\text{Cris}(X/S), \mathcal{O}_{X/S})$ n'est pas injective.
```
Lecture retenue :
```tex
\to H^0(\text{Cris}(X/S), \mathcal{O}_{X/S})$ n'est pas injectif.
```

## FR-CRYSTALLINE-FIDELITY-022 — `remark-mayer-vietoris`

[Source officielle, ligne 4418](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L4418)

Le troisième symbole comporte deux primes dans la source. L’amélioration à trois primes demeure une proposition distincte.

Source :
```tex
Let $f'$, $f''$, and $f''$ be
```
Traduction publiée :
```tex
Soient $f'$, $f''$ et $f'''$ les
```
Lecture retenue :
```tex
Soient $f'$, $f''$ et $f''$ les
```

## FR-CRYSTALLINE-FIDELITY-023 — `remark-base-change-isomorphism`

[Source officielle, ligne 4749](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L4749)

Première borne de suite : n est le témoin littéral, c était une correction de cohérence.

Source :
```tex
$\xi_1 - f'_1, \ldots, \xi_n - f'_n$
```
Traduction publiée :
```tex
$\xi_1 - f'_1, \ldots, \xi_c - f'_c$
```
Lecture retenue :
```tex
$\xi_1 - f'_1, \ldots, \xi_n - f'_n$
```

## FR-CRYSTALLINE-FIDELITY-024 — `remark-base-change-isomorphism`

[Source officielle, ligne 4757](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L4757)

La deuxième suite non primée emploie elle aussi n dans la source, et non c.

Source :
```tex
$\xi_1 - f_1, \ldots, \xi_n - f_n$
```
Traduction publiée :
```tex
$\xi_1 - f_1, \ldots, \xi_c - f_c$
```
Lecture retenue :
```tex
$\xi_1 - f_1, \ldots, \xi_n - f_n$
```

## FR-CRYSTALLINE-FIDELITY-025 — `remark-base-change-isomorphism`

[Source officielle, ligne 4771](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L4771)

La source attribue la même base D′ aux deux modules. L’explicitation respective D′ et D change cette affirmation et doit être présentée séparément.

Source :
```tex
are free $D'$-modules on the same generators
```
Traduction publiée :
```tex
sont respectivement un $D'$-module et un $D$-module libres sur les mêmes générateurs
```
Lecture retenue :
```tex
sont des $D'$-modules libres sur les mêmes générateurs
```

## FR-CRYSTALLINE-FIDELITY-026 — `remark-F-crystal-variants`

[Source officielle, ligne 5565](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L5565)

Les trois déterminants utilisent M, non défini dans ce calcul source. K répare l’argument mais n’est pas une traduction du témoin.

Source :
```tex
L K' = L K \det(L) \det(M) = L K L L' \det(M) = L p^i L' \det(M) =
```
Traduction publiée :
```tex
L K' = L K \det(L) \det(K) = L K L L' \det(K) = L p^i L' \det(K) =
```
Lecture retenue :
```tex
L K' = L K \det(L) \det(M) = L K L L' \det(M) = L p^i L' \det(M) =
```

## FR-CRYSTALLINE-FIDELITY-027 — `remark-quasi-coherent`

[Source officielle, ligne 4593](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/crystalline.tex#L4593)

Le deuxième renvoi, distinct en français, remplaçait une répétition littérale de la source. La répétition officielle est restaurée ; le renvoi proposé reste identifiable dans ce dossier.

Source :
```tex
Schemes, Lemmas \ref{schemes-lemma-quasi-compact-permanence} and
\ref{schemes-lemma-quasi-compact-permanence}.
```
Traduction publiée :
```tex
Schémas, lemmes \ref{schemes-lemma-quasi-compact-permanence} et
\ref{schemes-lemma-compose-after-separated}.
```
Lecture retenue :
```tex
Schémas, lemmes \ref{schemes-lemma-quasi-compact-permanence} et
\ref{schemes-lemma-quasi-compact-permanence}.
```

## Formulations conservées

### `item-completion`

La consigne éditoriale Add more here est déjà conservée en français ; elle n’est pas supprimée pour améliorer le texte.

### `equation-cosimplicial-morphism`

Si, sinon et si et seulement si conservent les conditions et les deux sens des équivalences. La ponctuation française n’est pas une correction de source.

### `lemma-crystal-quasi-coherent-modules`

La dernière phrase anglaise elliptique est rendue par On obtient ainsi la présentation voulue ; aucun objet ni condition n’est ajouté.

### `example-torsion`

Le pluriel maladroit inverse limit ... are acyclic est traduit au singulier comme limite inverse ... est acyclique, sans changer le complexe considéré.

## Limites

Ces lectures contextualisées ne certifient pas toute la prose. Restent la vérification des autres candidats, le rapprochement des identifiants producteurs, la construction des éditions complètes et le contrôle public des fichiers et sources. Le choix littéral intégrale conserve expressément une anomalie source ; il ne constitue pas une recommandation terminologique.
