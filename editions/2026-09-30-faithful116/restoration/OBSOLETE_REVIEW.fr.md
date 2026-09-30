# Chapitre 115 — Matériaux obsolètes : fidélité à la source officielle

**Restaurations locales en cours, sans certification ni remplacement de l’édition publique.**

[LaTeX de travail](staged/fr/115_obsolete.fr.tex) · [Contrôles](OBSOLETE_PARTIAL_VALIDATION.json) · [Contextes complets](OBSOLETE_CONTEXTUAL_RESTORATIONS.json)

Traduction non officielle assistée par IA, sans relecture experte humaine. Les propositions de correction mathématique restent lisibles ici : rétablir la lecture de référence ne signifie pas la préférer mathématiquement. Aucun témoin officiel ou public n’a été modifié.

## FR-OBSOLETE-FIDELITY-001 — `lemma-lift-elements-ideal`

[Source officielle, ligne 167](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L167)

La borne n de la condition officielle avait été corrigée en e. Le dossier conserve cette proposition, mais le corps fidèle reprend n.

Source :
```tex
$i \leq n$ maps
```
Traduction publiée :
```tex
$i \leq e$,
```
Lecture retenue :
```tex
$i \leq n$,
```

## FR-OBSOLETE-FIDELITY-002 — `lemma-lift-elements-ideal`

[Source officielle, ligne 218](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L218)

Première occurrence : le premier indice primé est n dans la source, non n+1. Les autres indices de la construction restent inchangés.

Source :
```tex
It is clear that $y_1, \ldots, y_n, y_n', \ldots, y_{n + m}'$
```
Traduction publiée :
```tex
Il est clair que $y_1, \ldots, y_n, y_{n + 1}', \ldots, y_{n + m}'$
```
Lecture retenue :
```tex
Il est clair que $y_1, \ldots, y_n, y_n', \ldots, y_{n + m}'$
```

## FR-OBSOLETE-FIDELITY-003 — `lemma-lift-elements-ideal`

[Source officielle, ligne 240](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L240)

Deuxième occurrence distincte dans la justification de la surjectivité : même restauration du premier indice primé.

Source :
```tex
$y_1, \ldots, y_n, y_n', \ldots, y_{n + m}'$ above.
```
Traduction publiée :
```tex
$y_1, \ldots, y_n, y_{n + 1}', \ldots, y_{n + m}'$.
```
Lecture retenue :
```tex
$y_1, \ldots, y_n, y_n', \ldots, y_{n + m}'$.
```

## FR-OBSOLETE-FIDELITY-004 — `lemma-bound-primes`

[Source officielle, ligne 445](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L445)

La parenthèse fermante ajoutée réparait la formule source. L’absence dans le témoin officiel est reproduite, sans prétendre que cette typographie soit correcte.

Source :
```tex
M & = \text{length}_A(A/(f + g, h)
```
Traduction publiée :
```tex
M & = \text{length}_A(A/(f + g, h))
```
Lecture retenue :
```tex
M & = \text{length}_A(A/(f + g, h)
```

## FR-OBSOLETE-FIDELITY-005 — `lemma-bound-primes`

[Source officielle, ligne 449](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L449)

La première somme porte i dans la source. L’uniformisation en j est une correction éditoriale séparée.

Source :
```tex
\sum\nolimits_i e_A(A/\mathfrak q_j^{(m_j)}, 0, h)
```
Traduction publiée :
```tex
\sum\nolimits_j e_A(A/\mathfrak q_j^{(m_j)}, 0, h)
```
Lecture retenue :
```tex
\sum\nolimits_i e_A(A/\mathfrak q_j^{(m_j)}, 0, h)
```

## FR-OBSOLETE-FIDELITY-006 — `lemma-bound-primes`

[Source officielle, ligne 451](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L451)

Restauration de i dans la seconde somme, distincte de la précédente ; la ponctuation finale française est conservée.

Source :
```tex
\sum\nolimits_i \sum\nolimits_{m = 0, \ldots, m_j - 1}
```
Traduction publiée :
```tex
\sum\nolimits_j \sum\nolimits_{m = 0, \ldots, m_j - 1}
```
Lecture retenue :
```tex
\sum\nolimits_i \sum\nolimits_{m = 0, \ldots, m_j - 1}
```

## FR-OBSOLETE-FIDELITY-007 — `lemma-P1-localize`

[Source officielle, ligne 736](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L736)

La dernière famille de flèches réemploie d dans la source malgré le quantificateur sur n. On retire la correction silencieuse en n.

Source :
```tex
$G : S_d \to S_{d + e}$, $n \geq d$ are
```
Traduction publiée :
```tex
$G : S_n \to S_{n + e}$, $n \geq d$, sont
```
Lecture retenue :
```tex
$G : S_d \to S_{d + e}$, $n \geq d$, sont
```

## FR-OBSOLETE-FIDELITY-008 — `lemma-finite-after-localization`

[Source officielle, ligne 809](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L809)

Le témoin nomme bêta à cette occurrence. Alpha donne le bon anneau cible dans le contexte, mais constitue précisément une proposition de correction source.

Source :
```tex
in $S'$ but are not zero. In this case $\beta(h)$
```
Traduction publiée :
```tex
dans $S'$ sans \^etre eux-m\^emes nuls. Dans ce cas, $\alpha(h)$
```
Lecture retenue :
```tex
dans $S'$ sans \^etre eux-m\^emes nuls. Dans ce cas, $\beta(h)$
```

## FR-OBSOLETE-FIDELITY-009 — `lemma-finite-after-localization`

[Source officielle, ligne 810](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L810)

La seconde occurrence de bêta, dans l’égalité d’annulation, est également rétablie. Les définitions d’alpha et de bêta restent celles du témoin.

Source :
```tex
$f^N \beta(h) = 0$
```
Traduction publiée :
```tex
$f^N \alpha(h) = 0$
```
Lecture retenue :
```tex
$f^N \beta(h) = 0$
```

## FR-OBSOLETE-FIDELITY-010 — `lemma-get-morphism-general`

[Source officielle, ligne 933](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L933)

La parenthèse ouvrante supplémentaire figure dans la source. Sa suppression était une réparation typographique du texte source, maintenant explicitement séparée.

Source :
```tex
\frac{(d(\text{Gr}_I(C))n}{t}
```
Traduction publiée :
```tex
\frac{d(\text{Gr}_I(C))n}{t}
```
Lecture retenue :
```tex
\frac{(d(\text{Gr}_I(C))n}{t}
```

## FR-OBSOLETE-FIDELITY-011 — `lemma-stein-projective`

[Source officielle, ligne 1598](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L1598)

Retour au symbole k de la fibre spéciale dans la conclusion officielle ; le corps résiduel kappa des hypothèses n’est pas modifié.

Source :
```tex
$X_k$ is geometrically connected.
```
Traduction publiée :
```tex
$X_\kappa$ est géométriquement connexe.
```
Lecture retenue :
```tex
$X_k$ est géométriquement connexe.
```

## FR-OBSOLETE-FIDELITY-012 — `lemma-property-irreducible-higher-rank`

[Source officielle, ligne 1641](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L1641)

Le renvoi interne (3) avait été corrigé en (4). Cette différence de prose n’apparaît pas dans un contrôle limité aux formules.

Source :
```tex
Consider a coherent sheaf $\mathcal{G}$ as in (3).
```
Traduction publiée :
```tex
Considérons un faisceau cohérent $\mathcal{G}$ comme en (4).
```
Lecture retenue :
```tex
Considérons un faisceau cohérent $\mathcal{G}$ comme en (3).
```

## FR-OBSOLETE-FIDELITY-013 — `lemma-property-irreducible-higher-rank`

[Source officielle, ligne 1653](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L1653)

Restauration de Z dans cette justification, sans normaliser silencieusement avec Z indice zéro dans les hypothèses.

Source :
```tex
because the support of $\mathcal{G}$ is equal to $Z$.
```
Traduction publiée :
```tex
car le support de $\mathcal{G}$ est égal à $Z_0$.
```
Lecture retenue :
```tex
car le support de $\mathcal{G}$ est égal à $Z$.
```

## FR-OBSOLETE-FIDELITY-014 — `lemma-preserves-Coh`

[Source officielle, ligne 1839](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L1839)

Le foncteur F avait été ajouté sous la cohomologie pour réparer le raisonnement. La proposition demeure dans ce dossier et n’est plus confondue avec la source traduite.

Source :
```tex
$H^i(\mathcal{O}_x) \not = 0$
```
Traduction publiée :
```tex
$H^i(F(\mathcal{O}_x)) \not = 0$
```
Lecture retenue :
```tex
$H^i(\mathcal{O}_x) \not = 0$
```

## FR-OBSOLETE-FIDELITY-015 — `lemma-preserves-Coh`

[Source officielle, ligne 1941](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L1941)

Le premier terme du calcul de F′(M) utilise K dans la source ; l’uniformisation avec M avait modifié ce terme.

Source :
```tex
R\text{pr}_{2, *}(L\text{pr}_1^*K \otimes \mathcal{K})
```
Traduction publiée :
```tex
R\text{pr}_{2, *}(L\text{pr}_1^*M \otimes \mathcal{K})
```
Lecture retenue :
```tex
R\text{pr}_{2, *}(L\text{pr}_1^*K \otimes \mathcal{K})
```

## FR-OBSOLETE-FIDELITY-016 — `lemma-preserves-Coh`

[Source officielle, ligne 1970](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L1970)

Le sous-indice x ajouté à cet idéal est retiré uniquement dans l’égalité avec Hom. Les autres occurrences sources de m indice x sont conservées.

Source :
```tex
$\mathcal{O}_{X, x}/\mathfrak m^n =
```
Traduction publiée :
```tex
$\mathcal{O}_{X, x}/\mathfrak m_x^n =
```
Lecture retenue :
```tex
$\mathcal{O}_{X, x}/\mathfrak m^n =
```

## FR-OBSOLETE-FIDELITY-017 — `lemma-preserves-Coh`

[Source officielle, ligne 1981](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L1981)

La traduction avait remplacé la justification officielle « immersion ouverte » par une conclusion directe d’isomorphisme. La phrase source, sa conclusion et son raisonnement sont rétablis sans certifier la justesse de ce raisonnement.

Source :
```tex
Finally, we conclude $f$ is an isomorphism
as Descent, Lemma
\ref{descent-lemma-flat-surjective-quasi-compact-monomorphism-isomorphism}
tells us it is an open immersion.
```
Traduction publiée :
```tex
Enfin, Descente, Lemme
\ref{descent-lemma-flat-surjective-quasi-compact-monomorphism-isomorphism}
montre que $f$ est un isomorphisme.
```
Lecture retenue :
```tex
Enfin, nous concluons que $f$ est un isomorphisme, car Descente, Lemme
\ref{descent-lemma-flat-surjective-quasi-compact-monomorphism-isomorphism}
nous dit que c’est une immersion ouverte.
```

## FR-OBSOLETE-FIDELITY-018 — `equation-object`

[Source officielle, ligne 2518](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L2518)

La flèche mapsto de ce foncteur avait été corrigée en to. Le symbole du témoin officiel est restauré.

Source :
```tex
\mathcal{C}_{X/Y} \mapsto Y_{Zar},
```
Traduction publiée :
```tex
\mathcal{C}_{X/Y} \to Y_{Zar},
```
Lecture retenue :
```tex
\mathcal{C}_{X/Y} \mapsto Y_{Zar},
```

## FR-OBSOLETE-FIDELITY-019 — `lemma-category-fibred`

[Source officielle, ligne 2564](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L2564)

L’identification explicite du foncteur remplaçait le nom u non défini dans ce passage source. Cette explicitation est séparée ; le symbole source u est rétabli.

Source :
```tex
The functor $u$ defines a morphism of topoi
```
Traduction publiée :
```tex
Le foncteur d'oubli vers $X_{Zar}$ définit un
morphisme de topos
```
Lecture retenue :
```tex
Le foncteur $u$ définit un
morphisme de topos
```

## FR-OBSOLETE-FIDELITY-020 — `remark-different-topologies`

[Source officielle, ligne 2640](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L2640)

La source inverse X et Y dans cette occurrence de la catégorie. La cohérence restaurée par le traducteur reste une proposition d’erratum, non une lecture attribuée au texte officiel.

Source :
```tex
$Y_{Zar}$ gives a sheaf $\underline{\mathcal{F}}$ on $\mathcal{C}_{Y/X}$
```
Traduction publiée :
```tex
$\mathcal{F}$ sur $Y_{Zar}$ définit un faisceau $\underline{\mathcal{F}}$ sur
$\mathcal{C}_{X/Y}$
```
Lecture retenue :
```tex
$\mathcal{F}$ sur $Y_{Zar}$ définit un faisceau $\underline{\mathcal{F}}$ sur
$\mathcal{C}_{Y/X}$
```

## FR-OBSOLETE-FIDELITY-021 — `lemma-equivalence`

[Source officielle, ligne 2735](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L2735)

La base et le second facteur tensoriels A et A′ avaient été échangés pour corriger le typage. Les positions du témoin sont rétablies ; le FIXME source est déjà conservé.

Source :
```tex
\gamma : \mathcal{H}' \otimes_A A' \to \mathcal{H}
```
Traduction publiée :
```tex
\gamma : \mathcal{H}' \otimes_{A'} A \to \mathcal{H}
```
Lecture retenue :
```tex
\gamma : \mathcal{H}' \otimes_A A' \to \mathcal{H}
```

## FR-OBSOLETE-FIDELITY-022 — `remark-construction-ob`

[Source officielle, ligne 2980](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L2980)

La source nomme B dans B′, tandis que la traduction corrigeait ces deux noms en U dans U′. Retour aux noms effectivement imprimés.

Source :
```tex
ideals cutting out $B$ in $B'$.
```
Traduction publiée :
```tex
définissant $U$ dans $U'$.
```
Lecture retenue :
```tex
définissant $B$ dans $B'$.
```

## FR-OBSOLETE-FIDELITY-023 — `lemma-blowing-up-intersections`

[Source officielle, ligne 3685](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L3685)

Le paramètre n avait été ajouté aux deux diviseurs de cette définition. Il est retiré pour reproduire le témoin officiel.

Source :
```tex
D_{n + 1, \{i, i'\}} = b_n^{-1}(D_i \cap D_{i'})
```
Traduction publiée :
```tex
D_{n + 1, \{i, i'\}} = b_n^{-1}(D_{n, i} \cap D_{n, i'})
```
Lecture retenue :
```tex
D_{n + 1, \{i, i'\}} = b_n^{-1}(D_i \cap D_{i'})
```

## FR-OBSOLETE-FIDELITY-024 — `lemma-blowing-up-intersections`

[Source officielle, ligne 3692](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L3692)

Cette occurrence source écrit b sans indice. La formule précédente avec b indice n était déjà fidèle et reste inchangée.

Source :
```tex
$b^{-1}(D_{n, i}) = D_{n + 1, i} +
```
Traduction publiée :
```tex
on voit que l'on a bien $b_n^{-1}(D_{n, i}) = D_{n + 1, i} +
```
Lecture retenue :
```tex
on voit que l'on a bien $b^{-1}(D_{n, i}) = D_{n + 1, i} +
```

## FR-OBSOLETE-FIDELITY-025 — `equation-invariant`

[Source officielle, ligne 3732](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L3732)

La virgule source avait été remplacée par une intersection. La correction est proposée à part, plutôt que d’être silencieusement attribuée à la source.

Source :
```tex
\dim_\delta(D_{n, i}, D_{n, i'}) \leq d - 2
```
Traduction publiée :
```tex
\dim_\delta(D_{n, i} \cap D_{n, i'}) \leq d - 2
```
Lecture retenue :
```tex
\dim_\delta(D_{n, i}, D_{n, i'}) \leq d - 2
```

## FR-OBSOLETE-FIDELITY-026 — `equation-invariant`

[Source officielle, ligne 3819](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L3819)

Première occurrence ultérieure : le but officiel est X indice n. La flèche vers U indice n introduite auparavant est déjà présente dans la source et n’est pas touchée.

Source :
```tex
and we let $b_n : X_{n + 1} \to X_n$ be the blowup in $Z_n$.
```
Traduction publiée :
```tex
et soit $b_n : X_{n + 1} \to U_n$ l'éclatement de centre $Z_n$.
```
Lecture retenue :
```tex
et soit $b_n : X_{n + 1} \to X_n$ l'éclatement de centre $Z_n$.
```

## FR-OBSOLETE-FIDELITY-027 — `equation-invariant`

[Source officielle, ligne 3821](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L3821)

Seconde occurrence distincte : on rétablit encore X indice n, sans uniformiser les trois flèches de la preuve.

Source :
```tex
applies to the morphism $b_n : X_{n + 1} \to X_n$ locally around
```
Traduction publiée :
```tex
s'applique au morphisme $b_n : X_{n + 1} \to U_n$, localement au voisinage
```
Lecture retenue :
```tex
s'applique au morphisme $b_n : X_{n + 1} \to X_n$, localement au voisinage
```

## FR-OBSOLETE-FIDELITY-028 — `equation-invariant`

[Source officielle, ligne 3830](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L3830)

Le facteur b zéro avait été ajouté pour compléter la composition. Son omission source est conservée et l’ajout reste une proposition explicite.

Source :
```tex
j_0 \circ \ldots \circ j_{n - 1} \circ b_{n - 1}
```
Traduction publiée :
```tex
j_0 \circ b_0 \circ \ldots \circ j_{n - 1} \circ b_{n - 1}
```
Lecture retenue :
```tex
j_0 \circ \ldots \circ j_{n - 1} \circ b_{n - 1}
```

## FR-OBSOLETE-FIDELITY-029 — `lemma-extensions-of-ringed-topoi`

[Source officielle, ligne 4638](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L4638)

La parenthèse fermant Sh avait été ajoutée. La lecture diplomatique reprend la parenthésation source, sans la qualifier de mathématiquement bien formée.

Source :
```tex
(\Sh(\mathcal{B}, \mathcal{O}_{\mathcal{B}'})
```
Traduction publiée :
```tex
(\Sh(\mathcal{B}), \mathcal{O}_{\mathcal{B}'})$ s'inscrivant
```
Lecture retenue :
```tex
(\Sh(\mathcal{B}, \mathcal{O}_{\mathcal{B}'})$ s'inscrivant
```

## Traductions ou explicitations conservées

### `lemma-directed-colimit-finite-type`

« Soit X un schéma quasi-compact et quasi-séparé » réunit les deux phrases officielles sans perdre d’hypothèse. L’occurrence répétée de X n’a pas à être reproduite artificiellement.

### `lemma-bound-primes`

La virgule après la flèche c et le point final du calcul sont de la ponctuation française, non de nouveaux termes mathématiques. Ils sont conservés indépendamment des indices et de la parenthèse rétablis.

### `equation-object`

L’expression « de dimension éventuellement infinie » explicite la portée de la parenthèse source dans le contexte d’un ensemble quelconque de variables. Les trois conditions de la définition et l’isomorphisme avec l’espace affine sont inchangés.

### `lemma-preserves-Coh`

Un complexe parfait égal à un module en degré zéro est traduit « isomorphe à » dans ce contexte de catégorie dérivée : cela explicite la même identification, sans ajouter de propriété au complexe. Cette décision locale ne certifie pas tout le vocabulaire du chapitre.

## Limites

Chaque opération est liée à un contexte lu. Le reste de la prose, la terminologie générale, les autres candidats et les éditions complètes restent à contrôler. Le rapprochement des identifiants producteurs n’est pas encore établi. Une relecture humaine experte est bienvenue, sans constituer un préalable aux réparations justifiées.
