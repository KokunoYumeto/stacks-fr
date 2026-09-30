# Chapitre 53 — Courbes : restauration du texte de référence

**Réparation locale en cours ; aucun lecteur ni aucune édition publique corrigée n’est certifié.**

[LaTeX de travail](staged/fr/053_curves.fr.tex) · [Contrôles](CURVES_PARTIAL_VALIDATION.json) · [Contextes complets](CURVES_CONTEXTUAL_RESTORATIONS.json)

Cette traduction est non officielle. Rétablir la lecture du Stacks Project ne signifie pas la juger préférable mathématiquement à une correction proposée. Les propositions ne sont pas effacées : les passages publiés et les raisons restent dans ce dossier, séparés du corps traduit.

## FR-CURVES-FIDELITY-001 — `lemma-smooth-models`

[Source officielle, ligne 306](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L306)

Le texte officiel omet l’indice K à cette conclusion. La correction de notation ne doit pas être silencieusement intégrée à la traduction de référence.

Source :
```tex
Then $Y$ is a smooth variety by
```
Traduction publiée :
```tex
Ainsi $Y_K$ est une variété lisse
```
Lecture rétablie :
```tex
Ainsi $Y$ est une variété lisse
```

## FR-CURVES-FIDELITY-002 — `lemma-sanity-check-duality`

[Source officielle, ligne 734](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L734)

Le second corps a été changé de k à k′ pour donner à a′ un argument de la bonne catégorie. La lecture de la source est restaurée, et l’amélioration proposée demeure dans cet avant/après.

Source :
```tex
a(\mathcal{O}_{\Spec(k)}) \cong a'(\mathcal{O}_{\Spec(k)})
```
Traduction publiée :
```tex
a(\mathcal{O}_{\Spec(k)}) \cong a'(\mathcal{O}_{\Spec(k')})
```
Lecture rétablie :
```tex
a(\mathcal{O}_{\Spec(k)}) \cong a'(\mathcal{O}_{\Spec(k)})
```

## FR-CURVES-FIDELITY-003 — `lemma-closed-subscheme-reduced-gorenstein`

[Source officielle, ligne 807](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L807)

L’image directe par i, telle qu’imprimée dans le témoin, avait été remplacée par celle de j. La correction typée doit rester séparée de la traduction.

Source :
```tex
\mathcal{I} = i_*\mathcal{I}'
```
Traduction publiée :
```tex
\mathcal{I} = j_*\mathcal{I}'
```
Lecture rétablie :
```tex
\mathcal{I} = i_*\mathcal{I}'
```

## FR-CURVES-FIDELITY-004 — `lemma-closed-subscheme-reduced-gorenstein`

[Source officielle, ligne 809](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L809)

Seconde moitié de la permutation des images directes : la source donne j pour J. La conjonction française et est conservée.

Source :
```tex
\mathcal{J} = j_*\mathcal{J}'
```
Traduction publiée :
```tex
\mathcal{J} = i_*\mathcal{J}'
```
Lecture rétablie :
```tex
\mathcal{J} = j_*\mathcal{J}'
```

## FR-CURVES-FIDELITY-005 — `lemma-closed-subscheme-reduced-gorenstein`

[Source officielle, ligne 816](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L816)

Le tiré en arrière de l’énoncé porte i dans la source et j dans le français. Rétablissement du symbole officiel, sans changer les suites exactes qui suivent.

Source :
```tex
\omega_Z = \mathcal{I}'(i^*\omega_X)
```
Traduction publiée :
```tex
\omega_Z = \mathcal{I}'(j^*\omega_X)
```
Lecture rétablie :
```tex
\omega_Z = \mathcal{I}'(i^*\omega_X)
```

## FR-CURVES-FIDELITY-006 — `lemma-closed-subscheme-reduced-gorenstein`

[Source officielle, ligne 817](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L817)

Même restauration de l’image directe officielle i_* pour omega_Z ; il ne s’agit pas d’un changement uniforme des noms i et j dans le lemme.

Source :
```tex
i_*(\omega_Z) = \mathcal{I}\omega_X
```
Traduction publiée :
```tex
j_*(\omega_Z) = \mathcal{I}\omega_X
```
Lecture rétablie :
```tex
i_*(\omega_Z) = \mathcal{I}\omega_X
```

## FR-CURVES-FIDELITY-007 — `lemma-euler`

[Source officielle, ligne 981](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L981)

La traduction avait inséré la dualité vectorielle Hom_k(-,k), absente de cette égalité source. L’insertion mathématiquement motivée est retirée de la traduction et conservée comme proposition distincte.

Source :
```tex
H^{-i}(X, \mathcal{O}_X)
```
Traduction publiée :
```tex
\Hom_k(H^{-i}(X, \mathcal{O}_X), k)
```
Lecture rétablie :
```tex
H^{-i}(X, \mathcal{O}_X)
```

## FR-CURVES-FIDELITY-008 — `lemma-tensor-omega-with-globally-generated-invertible`

[Source officielle, ligne 1236](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L1236)

L’opérateur de dimension a été ajouté pour rendre l’inégalité bien typée. L’édition traduisant le témoin conserve son omission ; l’interprétation dimensionnelle reste dans le dossier.

Source :
```tex
H^0(X, \mathcal{Q}) \geq 2
```
Traduction publiée :
```tex
\dim_k H^0(X, \mathcal{Q}) \geq 2
```
Lecture rétablie :
```tex
H^0(X, \mathcal{Q}) \geq 2
```

## FR-CURVES-FIDELITY-009 — `lemma-criterion-very-ample-bis`

[Source officielle, ligne 1423](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L1423)

Le nom de l’application de multiplication a été corrigé de mu_n à mu_2. On rétablit le nom officiel sans modifier ses trois espaces de sections.

Source :
```tex
\mu_n :
```
Traduction publiée :
```tex
\mu_2 :
```
Lecture rétablie :
```tex
\mu_n :
```

## FR-CURVES-FIDELITY-010 — `section-plane-curves`

[Source officielle, ligne 1577](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L1577)

La répétition de T_2 dans l’anneau source avait été remplacée par T_1. On la conserve ici sans propager cette coquille aux autres anneaux correctement notés du passage.

Source :
```tex
k[T_0, T_2, T_2] \longrightarrow \bigoplus \Gamma(X, \mathcal{O}_X(n))
```
Traduction publiée :
```tex
k[T_0, T_1, T_2] \longrightarrow \bigoplus \Gamma(X, \mathcal{O}_X(n))
```
Lecture rétablie :
```tex
k[T_0, T_2, T_2] \longrightarrow \bigoplus \Gamma(X, \mathcal{O}_X(n))
```

## FR-CURVES-FIDELITY-011 — `section-plane-curves`

[Source officielle, ligne 1582](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L1582)

La seconde répétition officielle de T_2, dans Proj, est restaurée au même titre que celle de la définition de I(X).

Source :
```tex
X = \text{Proj}(k[T_0, T_2, T_2]/I)
```
Traduction publiée :
```tex
X = \text{Proj}(k[T_0, T_1, T_2]/I)
```
Lecture rétablie :
```tex
X = \text{Proj}(k[T_0, T_2, T_2]/I)
```

## FR-CURVES-FIDELITY-012 — `lemma-smooth-plane-curve-point-over-separable`

[Source officielle, ligne 1746](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L1746)

Le nom de coordonnée officiel est X_0 à ce locus, malgré les T_i précédents. La correction de cohérence ne doit pas être silencieuse.

Source :
```tex
Z \cap D_+(X_0)
```
Traduction publiée :
```tex
Z \cap D_+(T_0)
```
Lecture rétablie :
```tex
Z \cap D_+(X_0)
```

## FR-CURVES-FIDELITY-013 — `lemma-smooth-plane-curve-point-over-separable`

[Source officielle, ligne 1753](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L1753)

Même restauration de X_0 dans l’ouvert V ; les occurrences antérieures de T_0 non corrigées dans la source restent intactes.

Source :
```tex
V \subset Z \cap D_{+}(X_0)
```
Traduction publiée :
```tex
V \subset Z \cap D_{+}(T_0)
```
Lecture rétablie :
```tex
V \subset Z \cap D_{+}(X_0)
```

## FR-CURVES-FIDELITY-014 — `lemma-genus-zero`

[Source officielle, ligne 1914](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L1914)

La source situe la section dans la puissance tensorielle 2 avant de conclure d=2. Le remplacement par d répare cette anticipation et appartient au dossier d’errata, non au texte traduit de référence.

Source :
```tex
\mathcal{L}^{\otimes 2}
```
Traduction publiée :
```tex
\mathcal{L}^{\otimes d}
```
Lecture rétablie :
```tex
\mathcal{L}^{\otimes 2}
```

## FR-CURVES-FIDELITY-015 — `proposition-projective-line`

[Source officielle, ligne 1999](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L1999)

La définition explicite de L a été ajoutée au français. L’objet reste décrit par la même formule, mais la source ne lui attribue pas ici de nom ; ce complément éditorial est retiré.

Source :
```tex
\mathcal{O}_X(\sum a_i x_i)
```
Traduction publiée :
```tex
\mathcal{L} = \mathcal{O}_X(\sum a_i x_i)
```
Lecture rétablie :
```tex
\mathcal{O}_X(\sum a_i x_i)
```

## FR-CURVES-FIDELITY-016 — `lemma-genus-zero-singular`

[Source officielle, ligne 2033](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L2033)

La définition de n clarifie les calculs suivants mais ne figure pas dans le témoin officiel. Elle reste une proposition séparée plutôt qu’un ajout à la preuve traduite.

Source :
```tex
k' = H^0(X', \mathcal{O}_{X'})
```
Traduction publiée :
```tex
k' = H^0(X', \mathcal{O}_{X'}),\ n = [k' : k]
```
Lecture rétablie :
```tex
k' = H^0(X', \mathcal{O}_{X'})
```

## FR-CURVES-FIDELITY-017 — `section-riemann-hurewitz`

[Source officielle, ligne 2320](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L2320)

Le premier coefficient est e, sans indice, dans la formule source. La traduction avait uniformisé ce coefficient avec e_x ; cette correction doit être signalée séparément.

Source :
```tex
e s^{e_x - 1} u \text{d}s + s^{e_x} \text{d}u
```
Traduction publiée :
```tex
e_x s^{e_x - 1} u \text{d}s + s^{e_x} \text{d}u
```
Lecture rétablie :
```tex
e s^{e_x - 1} u \text{d}s + s^{e_x} \text{d}u
```

## FR-CURVES-FIDELITY-018 — `section-riemann-hurewitz`

[Source officielle, ligne 2325](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L2325)

Même omission officielle de l’indice dans le premier terme du quotient des différentielles ; on ne modifie pas le e_x de la factorisation finale.

Source :
```tex
= e s^{e_x - 1} u + s^{e_x} w =
```
Traduction publiée :
```tex
= e_x s^{e_x - 1} u + s^{e_x} w =
```
Lecture rétablie :
```tex
= e s^{e_x - 1} u + s^{e_x} w =
```

## FR-CURVES-FIDELITY-019 — `lemma-inseparable-linear-system`

[Source officielle, ligne 2724](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L2724)

La parenthèse extérieure ajoutée dans le français répare une notation source incomplète. Le témoin est conservé diplomatiquement ; les accolades TeX restent équilibrées.

Source :
```tex
\varphi = \varphi_{(\mathcal{L}', (s_0, \ldots, s_r)} :
```
Traduction publiée :
```tex
\varphi = \varphi_{(\mathcal{L}', (s_0, \ldots, s_r))} :
```
Lecture rétablie :
```tex
\varphi = \varphi_{(\mathcal{L}', (s_0, \ldots, s_r)} :
```

## FR-CURVES-FIDELITY-020 — `lemma-inseparable-linear-system`

[Source officielle, ligne 2737](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L2737)

L’espace projectif est de dimension 1 dans cette définition officielle, bien que le morphisme précédent ait pour but P^r. La correction de type reste extérieure au texte traduit.

Source :
```tex
\mathcal{N} = \psi^*\mathcal{O}_{\mathbf{P}^1_k}(1)
```
Traduction publiée :
```tex
\mathcal{N} = \psi^*\mathcal{O}_{\mathbf{P}^r_k}(1)
```
Lecture rétablie :
```tex
\mathcal{N} = \psi^*\mathcal{O}_{\mathbf{P}^1_k}(1)
```

## FR-CURVES-FIDELITY-021 — `lemma-point-over-separable-extension`

[Source officielle, ligne 2797](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L2797)

L’ajout de parenthèses change la quantité majorée et répare le calcul. La baseline doit conserver la formule réellement écrite dans la source et documenter séparément cette correction.

Source :
```tex
2g - 2/p \leq g - 1
```
Traduction publiée :
```tex
(2g - 2)/p \leq g - 1
```
Lecture rétablie :
```tex
2g - 2/p \leq g - 1
```

## FR-CURVES-FIDELITY-022 — `section-pushouts`

[Source officielle, ligne 2886](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L2886)

L’hypothèse (b) nomme i le morphisme que le diagramme nomme i′. La traduction avait harmonisé les noms ; on restaure la lecture de cette seule hypothèse.

Source :
```tex
i : Z' \to X'
```
Traduction publiée :
```tex
i' : Z' \to X'
```
Lecture rétablie :
```tex
i : Z' \to X'
```

## FR-CURVES-FIDELITY-023 — `lemma-no-in-between-over-k`

[Source officielle, ligne 2978](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L2978)

La variable du polynôme écrit P est t dans la source. Le passage à x est une correction de cohérence par rapport à k[x], non une nécessité de traduction.

Source :
```tex
P = \prod_{i = 1}^d (t - a_i)
```
Traduction publiée :
```tex
P = \prod_{i = 1}^d (x - a_i)
```
Lecture rétablie :
```tex
P = \prod_{i = 1}^d (t - a_i)
```

## FR-CURVES-FIDELITY-024 — `lemma-factor-almost-isomorphism`

[Source officielle, ligne 3095](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L3095)

Le texte officiel conclut cette réduction avec B, alors que la traduction remplace le membre gauche par A. La modification est mathématiquement motivée par la dichotomie précédente, mais appartient au dossier séparé et non à une traduction diplomatique.

Source :
```tex
B = A + \mathfrak m_A B
```
Traduction publiée :
```tex
A = A + \mathfrak m_A B
```
Lecture rétablie :
```tex
B = A + \mathfrak m_A B
```

## FR-CURVES-FIDELITY-025 — `lemma-multicross`

[Source officielle, ligne 3307](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L3307)

L’indice i est présent dans la notation officielle, malgré le u introduit auparavant. On restaure cette occurrence sans modifier les autres points du raisonnement.

Source :
```tex
we see that $u_i$ is a multicross singularity
```
Traduction publiée :
```tex
on voit que $u$ est une singularité en croisement multiple
```
Lecture rétablie :
```tex
on voit que $u_i$ est une singularité en croisement multiple
```

## FR-CURVES-FIDELITY-026 — `lemma-torsion-picard-becomes-visible`

[Source officielle, ligne 3463](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L3463)

Le témoin officiel omet la parenthèse fermante extérieure. La correction typographique est conservée dans cet avant/après, sans être rendue silencieusement dans la baseline.

Source :
```tex
\text{Aut}(\Pic(X_{k^{sep}})[n]
```
Traduction publiée :
```tex
\text{Aut}(\Pic(X_{k^{sep}})[n])
```
Lecture rétablie :
```tex
\text{Aut}(\Pic(X_{k^{sep}})[n]
```

## FR-CURVES-FIDELITY-027 — `proposition-torsion-picard-reduced-proper`

[Source officielle, ligne 3564](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L3564)

La source utilise x minuscule dans la dernière parenthèse. Le français l’avait remplacé par le schéma X ; on distingue désormais la lecture source de cette correction proposée.

Source :
```tex
all singular points of $x$
```
Traduction publiée :
```tex
tous les points singuliers de $X$
```
Lecture rétablie :
```tex
tous les points singuliers de $x$
```

## FR-CURVES-FIDELITY-028 — `lemma-nodal-algebraic`

[Source officielle, ligne 3956](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L3956)

Le corps des coefficients est k dans la dernière invocation du lemme, et non kappa comme dans les autres applications du passage. La correction de ce changement de corps reste séparée.

Source :
```tex
k[[x, y]] \to A
```
Traduction publiée :
```tex
\kappa[[x, y]] \to A
```
Lecture rétablie :
```tex
k[[x, y]] \to A
```

## FR-CURVES-FIDELITY-029 — `lemma-nodal`

[Source officielle, ligne 4231](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L4231)

La base écrite dans la source est le point x barre, et non le corps k barre. La correction du symbole ne peut pas être intégrée tacitement au témoin traduit.

Source :
```tex
In particular $Z_{\overline{x}}$ is geometrically reduced
```
Traduction publiée :
```tex
En particulier, $Z_{\overline{k}}$ est géométriquement réduit
```
Lecture rétablie :
```tex
En particulier, $Z_{\overline{x}}$ est géométriquement réduit
```

## FR-CURVES-FIDELITY-030 — `lemma-nodal`

[Source officielle, ligne 4290](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L4290)

La conclusion de ce paragraphe renvoie à (5) dans la source et à (6) dans le français. La correction de renvoi interne est conservée séparément ; elle n’est pas détectable comme différence de formule.

Source :
```tex
Thus (5) holds.
```
Traduction publiée :
```tex
Ainsi (6) est satisfaite.
```
Lecture rétablie :
```tex
Ainsi (5) est satisfaite.
```

## FR-CURVES-FIDELITY-031 — `lemma-nodal`

[Source officielle, ligne 4291](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L4291)

Même renvoi source (5) changé silencieusement en (6) dans l’implication réciproque. Le signe égal et la terminologie restent inchangés.

Source :
```tex
Conversely, if (2) $=$ (5) is true
```
Traduction publiée :
```tex
Réciproquement, si (2) $=$ (6) est vraie
```
Lecture rétablie :
```tex
Réciproquement, si (2) $=$ (5) est vraie
```

## FR-CURVES-FIDELITY-032 — `lemma-nodal`

[Source officielle, ligne 4298](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L4298)

Troisième restauration du numéro officiel (5), cette fois dans la dernière conclusion après extension de corps. La modification proposée reste lisible dans le dossier.

Source :
```tex
We conclude that (5) holds for
```
Traduction publiée :
```tex
Nous en concluons que (6) est satisfaite pour
```
Lecture rétablie :
```tex
Nous en concluons que (5) est satisfaite pour
```

## FR-CURVES-FIDELITY-033 — `lemma-node-field-extension`

[Source officielle, ligne 4394](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L4394)

La source passe sans définition de X_K à Y dans la seconde condition. La traduction avait harmonisé les noms ; l’édition de référence ne doit pas masquer cette différence.

Source :
```tex
$y$ is a closed point of $Y$ and a node.
```
Traduction publiée :
```tex
$y$ est un point fermé de $X_K$ et un nœud.
```
Lecture rétablie :
```tex
$y$ est un point fermé de $Y$ et un nœud.
```

## FR-CURVES-FIDELITY-034 — `lemma-node-field-extension`

[Source officielle, ligne 4401](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L4401)

Restauration de Y dans la discussion de la fermeture des points, sans modifier le X_K correctement présent au début de l’énoncé.

Source :
```tex
closed point of $Y$ maps to a nonclosed point of $X$
```
Traduction publiée :
```tex
un point fermé de $X_K$ s'envoie sur un point non fermé de $X$
```
Lecture rétablie :
```tex
un point fermé de $Y$ s'envoie sur un point non fermé de $X$
```

## FR-CURVES-FIDELITY-035 — `lemma-node-field-extension`

[Source officielle, ligne 4405](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L4405)

Restauration du nom Y dans l’argument sur les branches géométriques.

Source :
```tex
hence $Y$ is geometrically unibranch at $y$
```
Traduction publiée :
```tex
$X_K$ serait géométriquement unibranche en $y$
```
Lecture rétablie :
```tex
$Y$ serait géométriquement unibranche en $y$
```

## FR-CURVES-FIDELITY-036 — `lemma-node-field-extension`

[Source officielle, ligne 4419](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L4419)

Restauration du nom Y dans la comparaison des invariants delta et des nombres de branches.

Source :
```tex
of $X$ at $x$ and $Y$ at $y$ are the same.
```
Traduction publiée :
```tex
de $X$ en $x$ et de $X_K$ en $y$ sont les mêmes.
```
Lecture rétablie :
```tex
de $X$ en $x$ et de $Y$ en $y$ sont les mêmes.
```

## FR-CURVES-FIDELITY-037 — `lemma-node-field-extension`

[Source officielle, ligne 4426](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L4426)

Le complété est celui de Y dans la source. On restaure également cette occurrence, en cohérence avec les quatre autres lectures originales.

Source :
```tex
\mathcal{O}_{Y, y}^\wedge
```
Traduction publiée :
```tex
\mathcal{O}_{X_K, y}^\wedge
```
Lecture rétablie :
```tex
\mathcal{O}_{Y, y}^\wedge
```

## FR-CURVES-FIDELITY-038 — `lemma-nodal-lci`

[Source officielle, ligne 4513](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L4513)

La parenthèse surnuméraire est bien dans le témoin officiel. La correction typographique antérieure est conservée dans l’avant/après plutôt que silencieusement rendue.

Source :
```tex
\text{depth}(\mathcal{O}_{X, x})) = 1
```
Traduction publiée :
```tex
\text{depth}(\mathcal{O}_{X, x}) = 1
```
Lecture rétablie :
```tex
\text{depth}(\mathcal{O}_{X, x})) = 1
```

## FR-CURVES-FIDELITY-039 — `lemma-closed-subscheme-nodal-curve`

[Source officielle, ligne 4616](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L4616)

La source écrit x dans cette réduction locale alors que le point fixé s’appelle y. La correction de nom est séparée du texte officiel traduit.

Source :
```tex
neighbourhood of $x$ we may assume
```
Traduction publiée :
```tex
Après avoir remplacé $X$ par un voisinage ouvert de $y$
```
Lecture rétablie :
```tex
Après avoir remplacé $X$ par un voisinage ouvert de $x$
```

## FR-CURVES-FIDELITY-040 — `lemma-closed-subscheme-nodal-curve`

[Source officielle, ligne 4628](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L4628)

La source donne deux fois O_{Y,Y}. Cette opération restaure exactement le but de la branche u, tout en conservant les autres anneaux correctement écrits et la phrase française.

Source :
```tex
$\mathcal{O}_{X, y} \to \mathcal{O}_{Y, Y}$
corresponds to $\kappa(y)[[u, v]]/(uv) \to \kappa(y)[[u]]$
```
Traduction publiée :
```tex
$\mathcal{O}_{X, y} \to \mathcal{O}_{Y, y}$ correspond à $\kappa(y)[[u, v]]/(uv) \to \kappa(y)[[u]]$
```
Lecture rétablie :
```tex
$\mathcal{O}_{X, y} \to \mathcal{O}_{Y, Y}$ correspond à $\kappa(y)[[u, v]]/(uv) \to \kappa(y)[[u]]$
```

## FR-CURVES-FIDELITY-041 — `lemma-closed-subscheme-nodal-curve`

[Source officielle, ligne 4631](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L4631)

La source donne deux fois O_{Y,Y}. Cette opération restaure exactement le but de la branche v, tout en conservant les autres anneaux correctement écrits et la phrase française.

Source :
```tex
$\mathcal{O}_{X, y} \to \mathcal{O}_{Y, Y}$
corresponds to $\kappa(y)[[u, v]]/(uv) \to \kappa(y)[[v]]$
```
Traduction publiée :
```tex
$\mathcal{O}_{X, y} \to \mathcal{O}_{Z, y}$ correspond à $\kappa(y)[[u, v]]/(uv) \to \kappa(y)[[v]]$
```
Lecture rétablie :
```tex
$\mathcal{O}_{X, y} \to \mathcal{O}_{Y, Y}$ correspond à $\kappa(y)[[u, v]]/(uv) \to \kappa(y)[[v]]$
```

## FR-CURVES-FIDELITY-042 — `lemma-formal-local-structure-nodal-family`

[Source officielle, ligne 4953](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L4953)

La source attribue les deux images à x. Le français avait rétabli y pour la seconde ; ce correctif de définition reste hors du témoin traduit.

Source :
```tex
x \longmapsto \overline{v}
```
Traduction publiée :
```tex
y \longmapsto \overline{v}
```
Lecture rétablie :
```tex
x \longmapsto \overline{v}
```

## FR-CURVES-FIDELITY-043 — `lemma-etale-local-structure-nodal-family`

[Source officielle, ligne 5113](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L5113)

Le second but de f_i est S_i dans la source. La première occurrence Spec(R_i) reste intacte ; il ne s’agit pas d’un renommage global.

Source :
```tex
If we can prove the lemma for $f_i : X_i \to S_i$ and
```
Traduction publiée :
```tex
Si nous pouvons démontrer le lemme pour $f_i : X_i \to \Spec(R_i)$ et
```
Lecture rétablie :
```tex
Si nous pouvons démontrer le lemme pour $f_i : X_i \to S_i$ et
```

## FR-CURVES-FIDELITY-044 — `lemma-etale-local-structure-nodal-family`

[Source officielle, ligne 5160](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L5160)

L’anneau de la définition de Y_sigma porte t dans la liste des variables du témoin et a dans la relation. La traduction avait corrigé la liste ; l’avant/après garde cette proposition séparée.

Source :
```tex
Y_\sigma = \Spec(\mathbf{Z}[u, v, t]/(uv - a))
```
Traduction publiée :
```tex
Y_\sigma = \Spec(\mathbf{Z}[u, v, a]/(uv - a))
```
Lecture rétablie :
```tex
Y_\sigma = \Spec(\mathbf{Z}[u, v, t]/(uv - a))
```

## FR-CURVES-FIDELITY-045 — `lemma-contracting-rational-tails`

[Source officielle, ligne 5930](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L5930)

Le faisceau structural de la condition de genre 1 porte X, sans prime, dans la source. La correction de schéma support n’est pas une liberté de traduction.

Source :
```tex
\omega_{X'} \cong \mathcal{O}_X
```
Traduction publiée :
```tex
\omega_{X'} \cong \mathcal{O}_{X'}
```
Lecture rétablie :
```tex
\omega_{X'} \cong \mathcal{O}_X
```

## FR-CURVES-FIDELITY-046 — `example-rational-bridge`

[Source officielle, ligne 6076](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L6076)

La factorisation de la restriction de c se termine par X dans le témoin. Le but Y ajouté au français répare le type du morphisme, mais doit être présenté comme proposition d’erratum.

Source :
```tex
C \to \Spec(k') \to X
```
Traduction publiée :
```tex
C \to \Spec(k') \to Y
```
Lecture rétablie :
```tex
C \to \Spec(k') \to X
```

## FR-CURVES-FIDELITY-047 — `lemma-rational-bridge-canonical`

[Source officielle, ligne 6172](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L6172)

La seconde catégorie possède des homomorphismes de O_Y-modules dans la source, et non de O_X-modules. Cette restauration est circonscrite à sa définition.

Source :
```tex
$\mathcal{L}|_C \cong \mathcal{O}_C$ and whose maps are
$\mathcal{O}_Y$-module homomorphisms.
```
Traduction publiée :
```tex
$\mathcal{L}|_C \cong \mathcal{O}_C$ et dont les flèches sont les homomorphismes de $\mathcal{O}_X$-modules.
```
Lecture rétablie :
```tex
$\mathcal{L}|_C \cong \mathcal{O}_C$ et dont les flèches sont les homomorphismes de $\mathcal{O}_Y$-modules.
```

## FR-CURVES-FIDELITY-048 — `lemma-rational-bridge-canonical`

[Source officielle, ligne 6210](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L6210)

La source répète sud-est pour la seconde flèche. La traduction avait rectifié la direction d’après le diagramme ; ce correctif en prose est séparé de la baseline.

Source :
```tex
$\omega_X \in \Ob(\mathcal{C}_X)$ represents the south-east arrow
```
Traduction publiée :
```tex
$\omega_X \in \Ob(\mathcal{C}_X)$ représente la flèche sud-ouest
```
Lecture rétablie :
```tex
$\omega_X \in \Ob(\mathcal{C}_X)$ représente la flèche sud-est
```

## FR-CURVES-FIDELITY-049 — `lemma-tricanonical`

[Source officielle, ligne 6605](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L6605)

La base du degré est Z dans la source, malgré le corps k fixé auparavant. Le changement en k constitue une correction mathématique explicite à garder séparément.

Source :
```tex
a closed subscheme of degree $2$ over $Z$
```
Traduction publiée :
```tex
un sous-schéma fermé de degré $2$ sur $k$
```
Lecture rétablie :
```tex
un sous-schéma fermé de degré $2$ sur $Z$
```

## FR-CURVES-FIDELITY-050 — `lemma-tricanonical`

[Source officielle, ligne 6609](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L6609)

La source utilise un L non défini dans cette application de restriction. La traduction l’avait remplacé par omega_X au cube ; on conserve l’interprétation dans le dossier, non dans la formule source traduite.

Source :
```tex
H^0(X, \mathcal{L}) \to H^0(Z, \mathcal{L}|_Z)
```
Traduction publiée :
```tex
H^0(X, \omega_X^{\otimes 3}) \to H^0(Z, \omega_X^{\otimes 3}|_Z)
```
Lecture rétablie :
```tex
H^0(X, \mathcal{L}) \to H^0(Z, \mathcal{L}|_Z)
```

## FR-CURVES-FIDELITY-051 — `lemma-tricanonical`

[Source officielle, ligne 6612](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L6612)

Même restauration du L officiel dans le groupe de cohomologie dont on demande l’annulation. Le reste du critère numérique demeure intact.

Source :
```tex
H^1(X, \mathcal{I}\mathcal{L}) = 0
```
Traduction publiée :
```tex
H^1(X, \mathcal{I}\omega_X^{\otimes 3}) = 0
```
Lecture rétablie :
```tex
H^1(X, \mathcal{I}\mathcal{L}) = 0
```

## FR-CURVES-FIDELITY-052 — `lemma-stable-vector-fields`

[Source officielle, ligne 6772](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/curves.tex#L6772)

La contradiction finale attribue ces hypothèses à C dans la source. Les réattribuer à X corrige la preuve mais ne relève pas d’une traduction sans liberté éditoriale.

Source :
```tex
$C$ has genus $\geq 2$ and has no rational bridges, or rational tails.
```
Traduction publiée :
```tex
$X$ est de genre $\geq 2$ et ne possède ni pont rationnel ni queue rationnelle.
```
Lecture rétablie :
```tex
$C$ est de genre $\geq 2$ et ne possède ni pont rationnel ni queue rationnelle.
```

## Limites et suite

Le témoin officiel exact gouverne les restaurations mathématiques. Le vocabulaire français existant est conservé, sans inventer une consultation du canon lors de la traduction initiale ni une attestation externe pour chaque mot. Les références et formules ne suffisent pas à certifier toute la prose. Les candidats restants, les identifiants producteurs, la reconstruction et la publication demeurent à traiter. Travail assisté par IA, sans validation experte humaine ; une relecture est bienvenue sans constituer une attente.
