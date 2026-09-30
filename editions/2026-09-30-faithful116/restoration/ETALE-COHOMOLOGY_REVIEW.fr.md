# Chapitre 59 — rétablissement du témoin officiel

**Réparation locale partielle. Ni relecture intégrale, ni reconstruction PDF, ni publication corrigée.**

Le but est une traduction de la source officielle, non une édition silencieusement corrigée. Les lectures remplacées sont conservées ci-dessous comme propositions distinctes. La grammaire française et les formulations équivalentes ne sont pas ramenées mécaniquement à la syntaxe anglaise.

[LaTeX de travail](staged/fr/059_etale-cohomology.fr.tex) · [Contrôles](ETALE-COHOMOLOGY_PARTIAL_VALIDATION.json) · [Contextes complets](ETALE-COHOMOLOGY_CONTEXTUAL_RESTORATIONS.json)

## Réparations délimitées

### FR-ETALE-COHOMOLOGY-FIDELITY-001 — `lemma-pullback-filtered-modules`

[Source officielle, ligne 10497](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L10497)

Rétablir V dans le groupe contenant G. L'homomorphisme vers Aut(M) reste inchangé : corriger le conflit de variables dans la traduction constituait une intervention sur la source.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$G \subset \text{Aut}(V)$
```
Avant :
```tex
$G \subset \text{Aut}(M)$
```
Après :
```tex
$G \subset \text{Aut}(V)$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-002 — `lemma-pullback-filtered-modules`

[Source officielle, ligne 10499](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L10499)

Retirer le motif supplémentaire « par continuité », absent de la phrase officielle. La traduction de finite module par module engendré par un nombre fini d'éléments est conservée ; ce n'est pas une nouvelle hypothèse.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
Observe that $G$ is finite as $M$ is a finite $\Lambda$-module
```
Avant :
```tex
Remarquons que $G$ est fini par continuit\'e et parce que
```
Après :
```tex
Remarquons que $G$ est fini parce que
```

### FR-ETALE-COHOMOLOGY-FIDELITY-003 — `lemma-nonvanishing-inherited`

[Source officielle, ligne 10557](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L10557)

Rétablir la formule de l'énoncé, même si elle contient une anomalie de variable. La formule F = g^{-1}G de la preuve, qui est bien dans la source, reste intacte.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$\mathcal{G}$ we can take $\mathcal{F} = g^{-1}\mathcal{F}$
```
Avant :
```tex
$\mathcal{G}$ nous pouvons prendre $\mathcal{F} = g^{-1}\mathcal{G}$,
```
Après :
```tex
$\mathcal{G}$ nous pouvons prendre $\mathcal{F} = g^{-1}\mathcal{F}$,
```

### FR-ETALE-COHOMOLOGY-FIDELITY-004 — `lemma-nonvanishing-inherited`

[Source officielle, ligne 10572](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L10572)

L'image inverse ajoutée au second membre de l'affichage réparait le type du faisceau. Elle est retirée à cet emplacement seulement, sans altérer les images inverses effectivement écrites ailleurs.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
H^n_\etale(X, \mathcal{G})
$$
```
Avant :
```tex
H^n_\etale(X, g^{-1}\mathcal{G})
$$
```
Après :
```tex
H^n_\etale(X, \mathcal{G})
$$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-005 — `proposition-serre-galois`

[Source officielle, ligne 10743](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L10743)

Rétablir K dans le groupe de Picard invoqué. Le K prime du témoin français était une correction de l'argument et non une traduction.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$\Pic(K) = (0)$
```
Avant :
```tex
$\Pic(K') = (0)$
```
Après :
```tex
$\Pic(K) = (0)$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-006 — `proposition-serre-galois`

[Source officielle, ligne 10745](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L10745)

L'hypothèse initiale sur les extensions finies est conservée, mais cette conclusion locale doit dire séparable comme la source. L'attestation consultée GIORGIUTTI-1962-SEPARABLE justifie l'expression française ; elle ne valide pas le passage de preuve de Stacks.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
any separable $K'/K$.
```
Avant :
```tex
toute extension finie $K'/K$. Soit maintenant
```
Après :
```tex
toute extension séparable $K'/K$. Soit maintenant
```

### FR-ETALE-COHOMOLOGY-FIDELITY-007 — `definition-extension-zero`

[Source officielle, ligne 11384](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L11384)

Rétablir le site X étale dans la remarque qui suit la définition. Les domaines U étale des foncteurs dans la définition sont corrects dans les deux témoins et restent inchangés.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
If $\mathcal{F}$ is an abelian sheaf on $X_\etale$, then
```
Avant :
```tex
Si $\mathcal{F}$ est un faisceau abélien sur $U_\etale$, alors
```
Après :
```tex
Si $\mathcal{F}$ est un faisceau abélien sur $X_\etale$, alors
```

### FR-ETALE-COHOMOLOGY-FIDELITY-008 — `lemma-decompose-quasi-finite-morphism`

[Source officielle, ligne 12155](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L12155)

La traduction avait remplacé une réunion de strates par l'alternative vide ou égal. Rétablir la construction de la source, sans appliquer ce changement à la dernière phrase, où l'alternative figure réellement. THOM-1965-STRATES atteste réunion de strates dans une stratification, non cet argument algébrique.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$X_j \times_X T_i$ is (set theoretically) a union of strata $X_j \times_X Z_i$.
```
Avant :
```tex
$X_j \times_X T_i$ soit vide ou soit, ensemblistement, \`egal \`a $X_j \times_X Z_i$.
```
Après :
```tex
$X_j \times_X T_i$ soit, ensemblistement, une r\'eunion de strates $X_j \times_X Z_i$.
```

### FR-ETALE-COHOMOLOGY-FIDELITY-009 — `lemma-decompose-quasi-finite-morphism`

[Source officielle, ligne 12161](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L12161)

Rétablir le symbole d'inclusion imprimé à cette occurrence. La proposition de remplacer ce symbole par l'appartenance reste dans le passage avant réparation du présent dossier.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$i, i' \subset I$
```
Avant :
```tex
$i, i' \in I$
```
Après :
```tex
$i, i' \subset I$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-010 — `lemma-locally-constant-on-connected-geom-unibranch`

[Source officielle, ligne 10274](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L10274)

Rétablir N_i lors de l'introduction du sous-groupe ouvert. La suite du témoin porte H_i et demeure inchangée ; cette incohérence est une proposition d'erratum, pas un permis de correction silencieuse.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$N_i$ of the profinite group
```
Avant :
```tex
$H_i$ du groupe profini
```
Après :
```tex
$N_i$ du groupe profini
```

### FR-ETALE-COHOMOLOGY-FIDELITY-011 — `theorem-vanishing-cohomology-Gm-curve`

[Source officielle, ligne 11090](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L11090)

Rétablir la notation sans virgule du premier affichage après la preuve. La ponctuation mathématique ajoutée n'est pas présentée comme celle de la source.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
j_*\mathbf{G}_{m\eta}
```
Avant :
```tex
j_*\mathbf{G}_{m, \eta}
```
Après :
```tex
j_*\mathbf{G}_{m\eta}
```

### FR-ETALE-COHOMOLOGY-FIDELITY-012 — `theorem-vanishing-cohomology-Gm-curve`

[Source officielle, ligne 11091](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L11091)

L'indice de la somme, absent dans cet affichage de la source, avait été complété. Il reste implicite dans la traduction de référence ; le complément reste visible dans le dossier.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
\bigoplus {i_x}_*\underline{\mathbf{Z}}
```
Avant :
```tex
\bigoplus\nolimits_{x \in X_0} {i_x}_*\underline{\mathbf{Z}}
```
Après :
```tex
\bigoplus {i_x}_*\underline{\mathbf{Z}}
```

### FR-ETALE-COHOMOLOGY-FIDELITY-013 — `lemma-finite-pushforward-constructible`

[Source officielle, ligne 12541](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L12541)

Le changement de base est écrit sur X dans la source, sur Y dans la traduction. Rétablir X sans prétendre que le défaut du témoin est mathématiquement préférable.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
affine scheme surjective over $X$.
```
Avant :
```tex
schéma affine surjectif sur $Y$.
```
Après :
```tex
schéma affine surjectif sur $X$.
```

### FR-ETALE-COHOMOLOGY-FIDELITY-014 — `lemma-category-is-colimit`

[Source officielle, ligne 12601](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L12601)

Reprendre l'affichage entier : les deux indices 0 de G et les parenthèses de regroupement ont été ajoutés. Le reste de la preuve garde ses G_0 effectivement écrits.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
f_0^{-1}\mathcal{G}(U) = \colim_{i \geq 0} f_{i0}^{-1}\mathcal{G}(U_i)
```
Avant :
```tex
(f_0^{-1}\mathcal{G}_0)(U) = \colim_{i \geq 0} (f_{i0}^{-1}\mathcal{G}_0)(U_i)
```
Après :
```tex
f_0^{-1}\mathcal{G}(U) = \colim_{i \geq 0} f_{i0}^{-1}\mathcal{G}(U_i)
```

### FR-ETALE-COHOMOLOGY-FIDELITY-015 — `lemma-category-is-colimit`

[Source officielle, ligne 12608](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L12608)

Rétablir F sans indice dans cette occurrence de la surjectivité essentielle. Ne pas modifier le F_i quantifié juste après.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
on $X$ is isomorphic to $f_i^{-1}\mathcal{F}$
```
Avant :
```tex
sur $X$ est isomorphe à $f_i^{-1}\mathcal{F}_i$
```
Après :
```tex
sur $X$ est isomorphe à $f_i^{-1}\mathcal{F}$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-016 — `lemma-zero-in-generic-point`

[Source officielle, ligne 12770](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L12770)

L'alternative d'égalité ajoutée répare la réflexivité de la relation, mais elle n'est pas dans le texte officiel. La retirer de la traduction de référence et la conserver comme proposition argumentée distincte.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
if and only if $i_1 \geq i'(i_2)$
```
Avant :
```tex
si et seulement si $i_1 = i_2\ \text{ou}\ i_1 \geq i'(i_2)$
```
Après :
```tex
si et seulement si $i_1 \geq i'(i_2)$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-017 — `remark-another-sp`

[Source officielle, ligne 13264](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L13264)

Rétablir l'indice t dans ce seul morphisme de comparaison. Les nombreux indices S de l'affichage principal restent intacts.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$\overline{t} \to \Spec(\mathcal{O}^{sh}_{t, \overline{t}})$
```
Avant :
```tex
$\overline{t} \to \Spec(\mathcal{O}^{sh}_{S, \overline{t}})$
```
Après :
```tex
$\overline{t} \to \Spec(\mathcal{O}^{sh}_{t, \overline{t}})$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-018 — `lemma-when-ctf`

[Source officielle, ligne 13796](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L13796)

Rétablir le degré b dans le morphisme final de la preuve, au lieu du degré b−1 corrigé par la traduction.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$\mathcal{F}^b \to \mathcal{F}$ annihilating
```
Avant :
```tex
$\mathcal{F}^{b-1} \to \mathcal{F}$ qui annule
```
Après :
```tex
$\mathcal{F}^b \to \mathcal{F}$ qui annule
```

### FR-ETALE-COHOMOLOGY-FIDELITY-019 — `lemma-when-ctf`

[Source officielle, ligne 13797](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L13797)

Rétablir les deux degrés de la flèche dont l'image est annulée, comme dans le témoin officiel.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$\mathcal{F}^{b - 1} \to \mathcal{F}^b$
```
Avant :
```tex
$\mathcal{F}^{b-2} \to \mathcal{F}^{b-1}$
```
Après :
```tex
$\mathcal{F}^{b - 1} \to \mathcal{F}^b$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-020 — `lemma-when-ctf`

[Source officielle, ligne 13797](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L13797)

Supprimer la définition supplémentaire F^b = F, qui achevait la réparation de l'argument mais ne figure pas dans la source. Le complexe affiché qui suit est conservé.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
Then it follows
from axiom TR3
```
Avant :
```tex
Posons $\mathcal{F}^b=\mathcal{F}$; il résulte alors
```
Après :
```tex
Il résulte alors
```

### FR-ETALE-COHOMOLOGY-FIDELITY-021 — `lemma-local-rings-strictly-henselian`

[Source officielle, ligne 14215](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L14215)

Rétablir X dans la fibre mentionnée par la source, malgré S dans l'énoncé.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$x \in X$
```
Avant :
```tex
$x \in S$
```
Après :
```tex
$x \in X$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-022 — `lemma-local-rings-strictly-henselian`

[Source officielle, ligne 14217](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L14217)

Rétablir le même indice X dans l'affichage de cohomologie, sans correction implicite de l'espace ambiant.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
H^p_\etale(\Spec(\mathcal{O}_{X, x}), \mathcal{G}_x)
```
Avant :
```tex
H^p_\etale(\Spec(\mathcal{O}_{S, x}), \mathcal{G}_x)
```
Après :
```tex
H^p_\etale(\Spec(\mathcal{O}_{X, x}), \mathcal{G}_x)
```

### FR-ETALE-COHOMOLOGY-FIDELITY-023 — `lemma-local-rings-strictly-henselian`

[Source officielle, ligne 14219](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L14219)

Rétablir X dans la phrase définissant G_x ; conserver séparément la proposition de remplacement par S.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
to $\Spec(\mathcal{O}_{X, x})$
```
Avant :
```tex
sur $\Spec(\mathcal{O}_{S, x})$
```
Après :
```tex
sur $\Spec(\mathcal{O}_{X, x})$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-024 — `lemma-local-rings-strictly-henselian`

[Source officielle, ligne 14221](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L14221)

La source parle des images directes supérieures de R^p epsilon_* F ; la traduction supprimait ce de pour rendre la conclusion correcte. Rétablir la portée de la phrase, sans attester la validité mathématique de la rédaction anglaise.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
Thus the higher direct images of $R^p\epsilon_*\mathcal{F}$ are
```
Avant :
```tex
Ainsi, les faisceaux d'images directes supérieures $R^p\epsilon_*\mathcal{F}$ sont
```
Après :
```tex
Ainsi, les faisceaux d'images directes supérieures de $R^p\epsilon_*\mathcal{F}$ sont
```

### FR-ETALE-COHOMOLOGY-FIDELITY-025 — `lemma-lift-points-H-to-G`

[Source officielle, ligne 14690](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L14690)

Rétablir A comme anneau contenant a dans la phrase du témoin. La correction en R est mathématique et doit rester distincte.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$a \in A$
```
Avant :
```tex
$a \in R$
```
Après :
```tex
$a \in A$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-026 — `lemma-lift-points-H-to-G`

[Source officielle, ligne 14691](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L14691)

Même rétablissement pour b à son occurrence unique ; les morphismes de A-algèbres vers R restent tels quels.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$b \in A$
```
Avant :
```tex
$b \in R$
```
Après :
```tex
$b \in A$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-027 — `lemma-h0-topological`

[Source officielle, ligne 15155](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L15155)

Rétablir X dans ce foncteur de sections, malgré la restriction du faisceau à Z. La traduction avait réparé l'espace sur lequel on prend les sections.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
\Gamma(X, (Z_i \to X)_*\underline{S_i}|_Z)
```
Avant :
```tex
\Gamma(Z, (Z_i \to X)_*\underline{S_i}|_Z)
```
Après :
```tex
\Gamma(X, (Z_i \to X)_*\underline{S_i}|_Z)
```

### FR-ETALE-COHOMOLOGY-FIDELITY-028 — `lemma-restrict-to-open`

[Source officielle, ligne 15507](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L15507)

Reprendre l'étoile du témoin dans la première égalité. Le second i étoile avait déjà été conservé, et les véritables i^{-1} du reste de la preuve restent inchangés.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$H^q_\etale(X, i_*i^{-1}\mathcal{F}) = H^q_\etale(Z, i^*\mathcal{F})$
```
Avant :
```tex
$H^q_\etale(X, i_*i^{-1}\mathcal{F}) = H^q_\etale(Z, i^{-1}\mathcal{F})$
```
Après :
```tex
$H^q_\etale(X, i_*i^{-1}\mathcal{F}) = H^q_\etale(Z, i^*\mathcal{F})$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-029 — `lemma-constant-statements-coefficients`

[Source officielle, ligne 15839](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L15839)

Rétablir n dans le premier module de cohomologie affiché, même si le sous-module de la suite exacte précédente est M[ell].

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
H^q_\etale(X, \underline{M[n]})
```
Avant :
```tex
H^q_\etale(X, \underline{M[\ell]})
```
Après :
```tex
H^q_\etale(X, \underline{M[n]})
```

### FR-ETALE-COHOMOLOGY-FIDELITY-030 — `lemma-constant-statements-coefficients`

[Source officielle, ligne 15849](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L15849)

La source emploie le faisceau F dans cette explication ; la traduction l'avait remplacé par le faisceau constant M. Reprendre les deux occurrences explicites de F. Aucun terme nouveau n'est introduit dans la terminologie française existante.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
Namely, the cohomology of $\mathcal{F}$
as a sheaf of $\Lambda$-modules is the same as the cohomology
of $\mathcal{F}$ as a sheaf of $\Lambda/\ell \Lambda$-modules,
```
Avant :
```tex
la cohomologie de $\underline{M}$ considéré comme faisceau de
$\Lambda$-modules est la même que sa cohomologie comme faisceau de
$\Lambda/\ell \Lambda$-modules,
```
Après :
```tex
la cohomologie de $\mathcal{F}$ considéré comme faisceau de
$\Lambda$-modules est la même que la cohomologie de $\mathcal{F}$ comme faisceau de
$\Lambda/\ell \Lambda$-modules,
```

### FR-ETALE-COHOMOLOGY-FIDELITY-031 — `lemma-constant-statements-coefficients`

[Source officielle, ligne 15886](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L15886)

Retirer l'indice supplémentaire du premier affichage de faisceaux. Il reste explicite dans le choix de base où la source le donne.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
\underline{\Lambda} = \bigoplus \underline{\mathbf{F}_\ell} e_i
```
Avant :
```tex
\underline{\Lambda} = \bigoplus_{i \in I} \underline{\mathbf{F}_\ell} e_i
```
Après :
```tex
\underline{\Lambda} = \bigoplus \underline{\mathbf{F}_\ell} e_i
```

### FR-ETALE-COHOMOLOGY-FIDELITY-032 — `lemma-constant-statements-coefficients`

[Source officielle, ligne 15891](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L15891)

Même reprise sans indice explicite dans le terme central de l'égalité de cohomologie.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
H^q_\etale(X, \bigoplus \underline{\mathbf{F}_\ell} e_i)
```
Avant :
```tex
H^q_\etale(X, \bigoplus_{i \in I} \underline{\mathbf{F}_\ell} e_i)
```
Après :
```tex
H^q_\etale(X, \bigoplus \underline{\mathbf{F}_\ell} e_i)
```

### FR-ETALE-COHOMOLOGY-FIDELITY-033 — `lemma-constant-statements-coefficients`

[Source officielle, ligne 15892](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L15892)

Même reprise au dernier terme. Ces suppressions d'indices explicitants ne sont pas comptées comme des théorèmes faux ; elles rapprochent la notation de la présentation officielle.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
\bigoplus H^q_\etale(X, \underline{\mathbf{F}_\ell})e_i
```
Avant :
```tex
\bigoplus_{i \in I} H^q_\etale(X, \underline{\mathbf{F}_\ell})e_i
```
Après :
```tex
\bigoplus H^q_\etale(X, \underline{\mathbf{F}_\ell})e_i
```

### FR-ETALE-COHOMOLOGY-FIDELITY-034 — `lemma-restrict-to-open-coefficients`

[Source officielle, ligne 15944](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L15944)

Rétablir l'étoile dans l'égalité du lemme avec coefficients. Ne pas imposer une notation corrigée uniforme à un témoin qui ne l'est pas.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$H^q_\etale(X, i_*i^{-1}\mathcal{F}) = H^q_\etale(Z, i^*\mathcal{F})$
```
Avant :
```tex
$H^q_\etale(X, i_*i^{-1}\mathcal{F}) = H^q_\etale(Z, i^{-1}\mathcal{F})$
```
Après :
```tex
$H^q_\etale(X, i_*i^{-1}\mathcal{F}) = H^q_\etale(Z, i^*\mathcal{F})$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-035 — `lemma-restrict-to-open-coefficients`

[Source officielle, ligne 15951](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L15951)

Rétablir aussi l'étoile dans l'annulation qui suit, seule autre occurrence modifiée ici.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$H^q_\etale(Z, i^*\mathcal{F}) = 0$
```
Avant :
```tex
$H^q_\etale(Z, i^{-1}\mathcal{F}) = 0$
```
Après :
```tex
$H^q_\etale(Z, i^*\mathcal{F}) = 0$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-036 — `lemma-restrict-to-open-coefficients`

[Source officielle, ligne 15968](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L15968)

Les isomorphismes finaux portent le degré 0 dans la source, malgré la condition q > 1. Reprendre les deux degrés officiels sans retoucher la suite exacte précédente.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$H^0_\etale(X, j_!j^{-1}\mathcal{F}) \to
H^0_\etale(X, \mathcal{F})$ for $q > 1$
```
Avant :
```tex
$H^q_\etale(X, j_!j^{-1}\mathcal{F}) \to
H^q_\etale(X, \mathcal{F})$ pour $q > 1$
```
Après :
```tex
$H^0_\etale(X, j_!j^{-1}\mathcal{F}) \to
H^0_\etale(X, \mathcal{F})$ pour $q > 1$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-037 — `lemma-base-change-Rf-star-colim`

[Source officielle, ligne 16461](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L16461)

Retirer le q ajouté au premier terme de cette égalité, sans altérer les R^q qui figurent dans les autres termes et dans l'énoncé.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
f^{-1}Rg_*\mathcal{F} =
f^{-1}\colim
```
Avant :
```tex
f^{-1}R^qg_*\mathcal{F} =
f^{-1}\colim
```
Après :
```tex
f^{-1}Rg_*\mathcal{F} =
f^{-1}\colim
```

### FR-ETALE-COHOMOLOGY-FIDELITY-038 — `lemma-base-change-f-star`

[Source officielle, ligne 16816](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L16816)

Les deux exposants −1 sur g_* avaient été supprimés dans la traduction. Rétablir la notation exacte du témoin à cet affichage, et seulement là.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
(f^{-1}g_*^{-1}\mathcal{F})_{\overline{x}} =
(g_*^{-1}\mathcal{F})_{f(\overline{x})}
```
Avant :
```tex
(f^{-1}g_*\mathcal{F})_{\overline{x}} =
(g_*\mathcal{F})_{f(\overline{x})}
```
Après :
```tex
(f^{-1}g_*^{-1}\mathcal{F})_{\overline{x}} =
(g_*^{-1}\mathcal{F})_{f(\overline{x})}
```

### FR-ETALE-COHOMOLOGY-FIDELITY-039 — `lemma-base-change-q-integral-top`

[Source officielle, ligne 16977](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L16977)

Rétablir le pi^{-1} supplémentaire de la source dans la première flèche de preuve. Le défaut de typage éventuel relève de l'erratum séparé.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$\mathcal{F} \to \pi_*\pi^{-1}\mathcal{F}'$
```
Avant :
```tex
$\mathcal{F} \to \pi_*\mathcal{F}'$
```
Après :
```tex
$\mathcal{F} \to \pi_*\pi^{-1}\mathcal{F}'$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-040 — `lemma-constructible-maps-into-constant`

[Source officielle, ligne 12962](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L12962)

Le but local de la preuve utilise S dans la source. L'identification silencieuse avec le faisceau constant E est retirée à cette seule occurrence ; le diagramme ultérieur garde E.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
(f_*S)_{\overline{x}}$ is injective
```
Avant :
```tex
(f_*\underline{E})_{\overline{x}}$ soit injectif
```
Après :
```tex
(f_*S)_{\overline{x}}$ soit injectif
```

### FR-ETALE-COHOMOLOGY-FIDELITY-041 — `lemma-constructible-maps-into-constant`

[Source officielle, ligne 12973](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L12973)

Retirer le nom h et la définition supplémentaire du composé f. Ils clarifiaient un conflit entre deux usages de f dans la source, au lieu de traduire ce qui était écrit.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
Let $Y \to Z$ be the normalization
of $Z$ in $\Spec(K)$.
```
Avant :
```tex
Soit $h : Y \to Z$ la normalisation
de $Z$ dans $\Spec(K)$, et notons $f : Y \to X$ le composé de $h$ avec $Z \to X$.
```
Après :
```tex
Soit $Y \to Z$ la normalisation
de $Z$ dans $\Spec(K)$.
```

### FR-ETALE-COHOMOLOGY-FIDELITY-042 — `lemma-constructible-maps-into-constant`

[Source officielle, ligne 12996](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L12996)

Reprendre le nom f de la source pour le morphisme entier vers Z. Le conflit éventuel avec la cible X reste visible dans le dossier d'errata.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
morphism $f : Y \to Z$ is integral
```
Avant :
```tex
morphisme $h : Y \to Z$ est entier
```
Après :
```tex
morphisme $f : Y \to Z$ est entier
```

### FR-ETALE-COHOMOLOGY-FIDELITY-043 — `lemma-constructible-maps-into-constant`

[Source officielle, ligne 13003](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L13003)

Retirer la définition des morphismes composés f_i ajoutée par la traduction. Les f_i du reste du témoin ne sont pas renommés.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
finite over $Z$. Namely, apply Properties, Lemma
```
Avant :
```tex
fini sur $Z$; notons $f_i : Y_i \to X$ les morphismes composés. Appliquons Properties, lemme
```
Après :
```tex
fini sur $Z$. Appliquons Properties, lemme
```

### FR-ETALE-COHOMOLOGY-FIDELITY-044 — `lemma-constructible-maps-into-constant`

[Source officielle, ligne 13005](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L13005)

Rétablir f_* dans l'application du lemme d'algèbre intégrale, au lieu du h_* introduit pour réparer la notation.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
to $f_*\mathcal{O}_Y$
```
Avant :
```tex
à $h_*\mathcal{O}_Y$
```
Après :
```tex
à $f_*\mathcal{O}_Y$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-045 — `lemma-base-change-does-not-hold-pre`

[Source officielle, ligne 17114](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L17114)

Rétablir q^{-1} dans la première fibre de la preuve. Les e^{-1} du morphisme comparé, imprimés dans la source, restent intacts.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
and an element $\xi$ of $(R^qh_*q^{-1}\mathcal{F})_{\overline{x}}$
```
Avant :
```tex
et un élément $\xi$ de $(R^qh_*e^{-1}\mathcal{F})_{\overline{x}}$
```
Après :
```tex
et un élément $\xi$ de $(R^qh_*q^{-1}\mathcal{F})_{\overline{x}}$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-046 — `lemma-base-change-does-not-hold-pre`

[Source officielle, ligne 17151](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L17151)

Le degré q manquait dans la définition de P(T') dans la source. Le retirer seulement de cette fibre ; ne pas le supprimer des formules voisines.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$(Rh'_*(e')^{-1}\mathcal{F}')_{\overline{x}}$ is
```
Avant :
```tex
$(R^qh'_*(e')^{-1}\mathcal{F}')_{\overline{x}}$ n'appartient
```
Après :
```tex
$(Rh'_*(e')^{-1}\mathcal{F}')_{\overline{x}}$ n'appartient
```

### FR-ETALE-COHOMOLOGY-FIDELITY-047 — `lemma-base-change-does-not-hold-pre`

[Source officielle, ligne 17153](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L17153)

Reprendre f sans prime dans le morphisme cité par la définition de P(T'). Cette opération est distincte du degré q précédent.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$(f^{-1}R^qg'_*\mathcal{F}')_{\overline{x}} \to
```
Avant :
```tex
$((f')^{-1}R^qg'_*\mathcal{F}')_{\overline{x}} \to
```
Après :
```tex
$(f^{-1}R^qg'_*\mathcal{F}')_{\overline{x}} \to
```

### FR-ETALE-COHOMOLOGY-FIDELITY-048 — `lemma-base-change-does-not-hold-pre`

[Source officielle, ligne 17176](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L17176)

Rétablir X et S dans le premier diagramme indexé par i, malgré les X' et S' des diagrammes antérieurs. Les flèches restent celles de ce diagramme officiel.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
X \ar[d]_{f'} & Y \ar[l]^h \ar[d]^e & Y_i \ar[l]^{\pi_i'} \ar[d]^{e_i} \\
S & T \ar[l]_g & T_i \ar[l]_{\pi_i}
```
Avant :
```tex
X' \ar[d]_{f'} & Y \ar[l]^h \ar[d]^e & Y_i \ar[l]^{\pi_i'} \ar[d]^{e_i} \\
S' & T \ar[l]_g & T_i \ar[l]_{\pi_i}
```
Après :
```tex
X \ar[d]_{f'} & Y \ar[l]^h \ar[d]^e & Y_i \ar[l]^{\pi_i'} \ar[d]^{e_i} \\
S & T \ar[l]_g & T_i \ar[l]_{\pi_i}
```

### FR-ETALE-COHOMOLOGY-FIDELITY-049 — `lemma-base-change-does-not-hold-pre`

[Source officielle, ligne 17183](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L17183)

Même reprise des deux sommets dans le diagramme composé adjacent. Aucun remplacement global des lettres primées n'est utilisé.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
X \ar[d]_{f'} & & Y_i \ar[ll]^{h_i = h \circ \pi_i'} \ar[d]^{e_i} \\
S & & T_i \ar[ll]_{g_i = g \circ \pi_i}
```
Avant :
```tex
X' \ar[d]_{f'} & & Y_i \ar[ll]^{h_i = h \circ \pi_i'} \ar[d]^{e_i} \\
S' & & T_i \ar[ll]_{g_i = g \circ \pi_i}
```
Après :
```tex
X \ar[d]_{f'} & & Y_i \ar[ll]^{h_i = h \circ \pi_i'} \ar[d]^{e_i} \\
S & & T_i \ar[ll]_{g_i = g \circ \pi_i}
```

### FR-ETALE-COHOMOLOGY-FIDELITY-050 — `lemma-base-change-does-not-hold-pre`

[Source officielle, ligne 17254](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L17254)

Rétablir les deux F sans prime dans les deux premiers termes de l'égalité. Le troisième terme conserve F' comme dans la source.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
R^qh'_*(e')^{-1}i_*i^{-1}\mathcal{F} =
R^qh'_*i'_*e_Z^{-1}i^{-1}\mathcal{F} =
```
Avant :
```tex
R^qh'_*(e')^{-1}i_*i^{-1}\mathcal{F}' =
R^qh'_*i'_*e_Z^{-1}i^{-1}\mathcal{F}' =
```
Après :
```tex
R^qh'_*(e')^{-1}i_*i^{-1}\mathcal{F} =
R^qh'_*i'_*e_Z^{-1}i^{-1}\mathcal{F} =
```

### FR-ETALE-COHOMOLOGY-FIDELITY-051 — `lemma-base-change-does-not-hold-pre`

[Source officielle, ligne 17274](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L17274)

Reprendre le dernier diagramme comme unité : sommets X/S/Y, flèche f et absence des noms h'/g'. La version française avait reconstruit le carré attendu ; cette reconstruction reste une proposition séparée.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
X \ar[d]_f & Y' \ar[l] \ar[d]_{e'} & Y \ar[l]^{j'} \ar[d]^{e_V} \\
S & T' \ar[l] & V \ar[l]_j
```
Avant :
```tex
X' \ar[d]_{f'} & Y' \ar[l]^{h'} \ar[d]_{e'} & Y' \times_{T'} V \ar[l]^{j'} \ar[d]^{e_V} \\
S' & T' \ar[l]_{g'} & V \ar[l]_j
```
Après :
```tex
X \ar[d]_f & Y' \ar[l] \ar[d]_{e'} & Y \ar[l]^{j'} \ar[d]^{e_V} \\
S & T' \ar[l] & V \ar[l]_j
```

### FR-ETALE-COHOMOLOGY-FIDELITY-052 — `lemma-base-change-does-not-hold-pre`

[Source officielle, ligne 17288](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L17288)

Rétablir xi sans prime dans la conclusion de l'argument. Les xi' qui figurent précédemment dans le témoin sont conservés.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
is injective. Thus $\xi$ maps to a nonzero element of
$(R^q(h' \circ j')_* e_V^{-1}\mathcal{J})_{\overline{x}}$
```
Avant :
```tex
est injectif. Ainsi, $\xi'$ a pour image un élément non nul de
$(R^q(h' \circ j')_* e_V^{-1}\mathcal{J})_{\overline{x}}$
```
Après :
```tex
est injectif. Ainsi, $\xi$ a pour image un élément non nul de
$(R^q(h' \circ j')_* e_V^{-1}\mathcal{J})_{\overline{x}}$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-053 — `theorem-smooth-base-change`

[Source officielle, ligne 17557](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L17557)

Le coin inférieur gauche du diagramme de Mayer–Vietoris porte q dans le témoin officiel. Reprendre ce degré à ce seul coin ; le q−1 du coin supérieur reste inchangé.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
R^qk_*e^{-1}\mathcal{F}|_{e^{-1}(W \cap W')}
```
Avant :
```tex
R^{q - 1}k_*e^{-1}\mathcal{F}|_{e^{-1}(W \cap W')}
```
Après :
```tex
R^qk_*e^{-1}\mathcal{F}|_{e^{-1}(W \cap W')}
```

### FR-ETALE-COHOMOLOGY-FIDELITY-054 — `theorem-smooth-base-change`

[Source officielle, ligne 17651](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L17651)

Rétablir q^{-1} dans le choix de la section au début de la récurrence sur la dimension. Les e^{-1} imprimés dans le reste de la preuve ne sont pas touchés.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
of $R^qh_*q^{-1}\mathcal{I}$ over $U$.
```
Avant :
```tex
de $R^qh_*e^{-1}\mathcal{I}$ sur $U$.
```
Après :
```tex
de $R^qh_*q^{-1}\mathcal{I}$ sur $U$.
```

### FR-ETALE-COHOMOLOGY-FIDELITY-055 — `theorem-smooth-base-change`

[Source officielle, ligne 17731](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L17731)

Dans la note, la source emploie i dans ce groupe de cohomologie, malgré le recouvrement indexé par j. Reprendre i seulement ici, sans renommer le recouvrement ni les facteurs ultérieurs.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$H^q(U'_i \times_{X'} Y, e^{-1}\mathcal{I})$, then by property (B)
```
Avant :
```tex
$H^q(U'_j \times_{X'} Y, e^{-1}\mathcal{I})$, alors, par la propriété (B)
```
Après :
```tex
$H^q(U'_i \times_{X'} Y, e^{-1}\mathcal{I})$, alors, par la propriété (B)
```

### FR-ETALE-COHOMOLOGY-FIDELITY-056 — `theorem-smooth-base-change`

[Source officielle, ligne 17844](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L17844)

Reprendre la notation I_V utilisée dans ce terme par la source. Les restrictions I|_V effectivement imprimées dans les termes voisins restent intactes ; ce rétablissement notationnel n'est pas compté comme un théorème erroné.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
H^q(Y \times_T V, e_V^{-1}\mathcal{I}_V) =
```
Avant :
```tex
H^q(Y \times_T V, e_V^{-1}(\mathcal{I}|_V)) =
```
Après :
```tex
H^q(Y \times_T V, e_V^{-1}\mathcal{I}_V) =
```

### FR-ETALE-COHOMOLOGY-FIDELITY-057 — `lemma-base-change-field-extension`

[Source officielle, ligne 18056](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L18056)

Rétablir la composition typographique du témoin à cette occurrence, qui omet le soulignement avant etale. Il s'agit d'une différence de notation, non d'une hypothèse mathématique nouvelle.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$(T_{L'})_\etale = (T_L)\etale$
```
Avant :
```tex
$(T_{L'})_\etale = (T_L)_\etale$
```
Après :
```tex
$(T_{L'})_\etale = (T_L)\etale$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-058 — `lemma-smooth-base-change-separably-closed`

[Source officielle, ligne 18085](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L18085)

La source passe à F dans cette égalité de preuve, alors que l'énoncé porte E. Rétablir ses deux occurrences de F au lieu de résoudre silencieusement cette incohérence.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
Thus $H^q_\etale(X, \mathcal{F}) =
H^q_\etale(X_{\overline{k}}, \mathcal{F}_{X_{\overline{k}}})$ by
```
Avant :
```tex
Ainsi $H^q_\etale(X, E) =
H^q_\etale(X_{\overline{k}}, E|_{X_{\overline{k}}})$ par
```
Après :
```tex
Ainsi $H^q_\etale(X, \mathcal{F}) =
H^q_\etale(X_{\overline{k}}, \mathcal{F}_{X_{\overline{k}}})$ par
```

### FR-ETALE-COHOMOLOGY-FIDELITY-059 — `lemma-strictly-henselian`

[Source officielle, ligne 19726](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L19726)

Rétablir le k minuscule dans cet anneau local, sans renommer les K de l'énoncé et du reste de la preuve. La régularisation de la variable appartient au dossier d'errata.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
\mathcal{O}_{\mathbf{A}^a_k, \eta}^{sh}
```
Avant :
```tex
\mathcal{O}_{\mathbf{A}^a_K, \eta}^{sh}
```
Après :
```tex
\mathcal{O}_{\mathbf{A}^a_k, \eta}^{sh}
```

### FR-ETALE-COHOMOLOGY-FIDELITY-060 — `lemma-strictly-henselian`

[Source officielle, ligne 19758](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L19758)

Reprendre l'indice du produit tensoriel dans la note, sans la virgule insérée. C'est un rétablissement typographique, pas un nouveau résultat mathématique.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$B = \colim B_j \otimes_{\psi_{i, j} A_i} A$
```
Avant :
```tex
$B = \colim B_j \otimes_{\psi_{i, j}, A_i} A$
```
Après :
```tex
$B = \colim B_j \otimes_{\psi_{i, j} A_i} A$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-061 — `proposition-cd-affine`

[Source officielle, ligne 19794](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L19794)

La source invoque pi_* à cet endroit malgré le nom f du morphisme fini. Rétablir pi_* ici seulement ; ne pas reconstruire la preuve par un renommage général.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
prove the result for $\pi_*\mathcal{F}$
```
Avant :
```tex
démontrer le résultat pour $f_*\mathcal{F}$
```
Après :
```tex
démontrer le résultat pour $\pi_*\mathcal{F}$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-062 — `lemma-interlude-II`

[Source officielle, ligne 19935](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L19935)

Rétablir la cible Z de la suite spectrale citée dans le témoin. X était une correction de son objet ambiant.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
for $Z_i \to Z$ to get
```
Avant :
```tex
de $Z_i \to X$ pour obtenir
```
Après :
```tex
de $Z_i \to Z$ pour obtenir
```

### FR-ETALE-COHOMOLOGY-FIDELITY-063 — `lemma-interlude-I`

[Source officielle, ligne 19977](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L19977)

Conserver dans ce produit fibré le A non gras du témoin officiel. Cette différence typographique n'est pas présentée comme une altération de théorème.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
H^q(\mathbf{A}^{n + m}_K \times_{A^n_K}
```
Avant :
```tex
H^q(\mathbf{A}^{n + m}_K \times_{\mathbf{A}^n_K}
```
Après :
```tex
H^q(\mathbf{A}^{n + m}_K \times_{A^n_K}
```

### FR-ETALE-COHOMOLOGY-FIDELITY-064 — `lemma-interlude-I`

[Source officielle, ligne 20009](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L20009)

Retirer le q ajouté au foncteur dérivé dans la dernière conclusion, tout en conservant la condition q > a−b imprimée.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$(Rf_*\mathcal{F})_{\overline{y}} = 0$ for $q > a - b$
```
Avant :
```tex
$(R^qf_*\mathcal{F})_{\overline{y}} = 0$ pour $q > a - b$
```
Après :
```tex
$(Rf_*\mathcal{F})_{\overline{y}} = 0$ pour $q > a - b$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-065 — `lemma-kunneth-localize-on-X`

[Source officielle, ligne 20452](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L20452)

Rétablir Rj'_* au second membre de la première flèche après changement de base. Le diagramme conserve h' ; la correction de typage ne doit pas se cacher dans la traduction.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$(q')^{-1}Rj'_*\mathcal{F}' \to Rj'_*(p')^{-1}\mathcal{F}'$ where
```
Avant :
```tex
$(q')^{-1}Rj'_*\mathcal{F}' \to Rh'_*(p')^{-1}\mathcal{F}'$, où
```
Après :
```tex
$(q')^{-1}Rj'_*\mathcal{F}' \to Rj'_*(p')^{-1}\mathcal{F}'$, où
```

### FR-ETALE-COHOMOLOGY-FIDELITY-066 — `lemma-kunneth-localize-on-X`

[Source officielle, ligne 20456](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L20456)

Même rétablissement à la deuxième occurrence, qui exprime le but de cette étape.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
that $(q')^{-1}Rj'_*\mathcal{F}' \to Rj'_*(p')^{-1}\mathcal{F}'$
```
Avant :
```tex
que $(q')^{-1}Rj'_*\mathcal{F}' \to Rh'_*(p')^{-1}\mathcal{F}'$
```
Après :
```tex
que $(q')^{-1}Rj'_*\mathcal{F}' \to Rj'_*(p')^{-1}\mathcal{F}'$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-067 — `lemma-kunneth-localize-on-X`

[Source officielle, ligne 20484](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L20484)

Reprendre à la troisième occurrence à la fois Rj'_* et le F sans prime du second membre, comme dans la conclusion officielle du paragraphe.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$(q')^{-1}Rj'_*\mathcal{F}' \to Rj'_*(p')^{-1}\mathcal{F}$ is an isomorphism.
```
Avant :
```tex
$(q')^{-1}Rj'_*\mathcal{F}' \to Rh'_*(p')^{-1}\mathcal{F}'$ est un isomorphisme.
```
Après :
```tex
$(q')^{-1}Rj'_*\mathcal{F}' \to Rj'_*(p')^{-1}\mathcal{F}$ est un isomorphisme.
```

### FR-ETALE-COHOMOLOGY-FIDELITY-068 — `lemma-kunneth-localize-on-X`

[Source officielle, ligne 20488](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L20488)

Rétablir X,x dans la définition de Y' imprimée, malgré le paragraphe consacré à y dans Y. L'autre définition avec X,x au paragraphe précédent reste intacte.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
Let $Y' = \Spec(\mathcal{O}_{X, x}^{sh})$.
```
Avant :
```tex
Soit $Y' = \Spec(\mathcal{O}_{Y, y}^{sh})$.
```
Après :
```tex
Soit $Y' = \Spec(\mathcal{O}_{X, x}^{sh})$.
```

### FR-ETALE-COHOMOLOGY-FIDELITY-069 — `lemma-punctual-base-change`

[Source officielle, ligne 20626](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L20626)

Rétablir les quatre sommets nommés dans la source, en particulier S_i et T_i. La traduction avait remplacé les deux derniers par les bases fixes.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
with corners $X_i, Y_i, S_i, T_i$.
```
Avant :
```tex
de sommets $X_i, Y_i, S', T$.
```
Après :
```tex
de sommets $X_i, Y_i, S_i, T_i$.
```

### FR-ETALE-COHOMOLOGY-FIDELITY-070 — `lemma-punctual-base-change`

[Source officielle, ligne 20648](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L20648)

Retirer le R ajouté devant g_* dans cette étape. Le Rg_* de l'énoncé officiel reste inchangé.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
Hence $(f')^{-1}g_*\mathcal{F} \to Rh_*e^{-1}\mathcal{F}$
```
Avant :
```tex
Ainsi, $(f')^{-1}Rg_*\mathcal{F} \to Rh_*e^{-1}\mathcal{F}$
```
Après :
```tex
Ainsi, $(f')^{-1}g_*\mathcal{F} \to Rh_*e^{-1}\mathcal{F}$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-071 — `lemma-punctual-base-change`

[Source officielle, ligne 20691](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L20691)

Le lecteur doit trouver colimit, donc limite inductive, comme dans la source, même si le diagramme invite à proposer limit à la place. SGA4-I-LIMITES atteste le sens catégorique du terme français ; il ne valide pas cet emploi mathématique dans Stacks.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
\quad\text{is the colimit of}\quad
```
Avant :
```tex
\quad\text{est la limite projective des}\quad
```
Après :
```tex
\quad\text{est la limite inductive des}\quad
```

### FR-ETALE-COHOMOLOGY-FIDELITY-072 — `lemma-punctual-base-change-upgrade`

[Source officielle, ligne 20867](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L20867)

Retirer l'image directe rho_{i,*} ajoutée pour typer l'égalité finale. Le terme précédent qui contient réellement rho_{i,*} est conservé.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
R^qh_*(\rho_i^{-1}e^{-1}\mathcal{F})
```
Avant :
```tex
R^qh_*\rho_{i, *}(\rho_i^{-1}e^{-1}\mathcal{F})
```
Après :
```tex
R^qh_*(\rho_i^{-1}e^{-1}\mathcal{F})
```

### FR-ETALE-COHOMOLOGY-FIDELITY-073 — `lemma-punctual-base-change-upgrade`

[Source officielle, ligne 20869](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L20869)

Rétablir la parenthèse finale du témoin dans ce seul affichage. Elle reste une anomalie de ponctuation documentée, non une correction incorporée à la traduction.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
\pi'_{i, *}R^qh_{i, *} \rho_i^{-1}e^{-1}\mathcal{F})
\end{align*}
```
Avant :
```tex
\pi'_{i, *}R^qh_{i, *} \rho_i^{-1}e^{-1}\mathcal{F}
\end{align*}
```
Après :
```tex
\pi'_{i, *}R^qh_{i, *} \rho_i^{-1}e^{-1}\mathcal{F})
\end{align*}
```

### FR-ETALE-COHOMOLOGY-FIDELITY-074 — `lemma-compare-ph-etale`

[Source officielle, ligne 22375](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L22375)

Le symbole d'image directe a été ajouté à f_small dans la comparaison ph/étale. Reprendre ici la formule officielle dépourvue de cette étoile.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$R^if_{small}\mathcal{F}$
```
Avant :
```tex
$R^if_{small, *}\mathcal{F}$
```
Après :
```tex
$R^if_{small}\mathcal{F}$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-075 — `lemma-compare-h-etale`

[Source officielle, ligne 22703](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L22703)

Même reprise dans le lemme distinct h/étale, vérifié séparément et non par remplacement global.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$R^if_{small}\mathcal{F}$
```
Avant :
```tex
$R^if_{small,*}\mathcal{F}$
```
Après :
```tex
$R^if_{small}\mathcal{F}$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-076 — `lemma-V-C-all-n-etale-ph`

[Source officielle, ligne 22432](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L22432)

Rétablir le second a_X^{-1} de la formule officielle dans la preuve ph, au lieu du pi_X^{-1} qui la corrige.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$a_X^{-1} = \epsilon_X^{-1} \circ a_X^{-1}$
```
Avant :
```tex
$a_X^{-1} = \epsilon_X^{-1} \circ \pi_X^{-1}$
```
Après :
```tex
$a_X^{-1} = \epsilon_X^{-1} \circ a_X^{-1}$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-077 — `lemma-V-C-all-n-etale-h`

[Source officielle, ligne 22761](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L22761)

Même restauration dans la preuve h, dont le texte a été comparé séparément.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$a_X^{-1} = \epsilon_X^{-1} \circ a_X^{-1}$
```
Avant :
```tex
$a_X^{-1} = \epsilon_X^{-1} \circ \pi_X^{-1}$
```
Après :
```tex
$a_X^{-1} = \epsilon_X^{-1} \circ a_X^{-1}$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-078 — `lemma-cohomological-descent-etale-ph`

[Source officielle, ligne 22469](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L22469)

Le sens de la composition avait été corrigé dans la preuve ph. Rétablir son ordre tel qu'imprimé, tout en conservant le correctif proposé dans ce dossier.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$a_X = \epsilon_X \circ \pi_X$
```
Avant :
```tex
$a_X = \pi_X \circ \epsilon_X$
```
Après :
```tex
$a_X = \epsilon_X \circ \pi_X$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-079 — `lemma-cohomological-descent-etale-h`

[Source officielle, ligne 22798](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L22798)

Reprendre aussi l'ordre imprimé dans la preuve h ; la cohérence des types relève de la proposition d'erratum séparée.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$a_X = \epsilon_X \circ \pi_X$
```
Avant :
```tex
$a_X = \pi_X \circ \epsilon_X$
```
Après :
```tex
$a_X = \epsilon_X \circ \pi_X$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-080 — `lemma-push-pull-h-etale`

[Source officielle, ligne 22607](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L22607)

Rétablir les indices X dans la définition imprimée de a_Y. Les indices Y des diagrammes, effectivement présents dans la source, ne sont pas changés.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$a_Y = \pi_X \circ \epsilon_X$
```
Avant :
```tex
$a_Y = \pi_Y \circ \epsilon_Y$
```
Après :
```tex
$a_Y = \pi_X \circ \epsilon_X$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-081 — `section-glueing-etale`

[Source officielle, ligne 22911](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L22911)

Rétablir F_i dans le couple désignant la donnée de descente canonique. Les F sans indice dans l'affichage de c_ij restent ceux du texte officiel.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$(f_{i, small}^{-1}\mathcal{F}_i, c_{ij})$
```
Avant :
```tex
$(f_{i, small}^{-1}\mathcal{F}, c_{ij})$
```
Après :
```tex
$(f_{i, small}^{-1}\mathcal{F}_i, c_{ij})$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-082 — `lemma-glue-etale-sheaf-modification`

[Source officielle, ligne 23203](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L23203)

Reprendre le f prime de cette flèche, bien que le morphisme de départ soit nommé f. Ne pas répercuter cette anomalie aux autres f_* de la preuve.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
and $f'_*\mathcal{F}' \to i_*g_*g^{-1}\mathcal{G}$.
```
Avant :
```tex
et $f_*\mathcal{F}' \to i_*g_*g^{-1}\mathcal{G}$.
```
Après :
```tex
et $f'_*\mathcal{F}' \to i_*g_*g^{-1}\mathcal{G}$.
```

### FR-ETALE-COHOMOLOGY-FIDELITY-083 — `lemma-blow-up-square-cohomological-descent`

[Source officielle, ligne 23379](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L23379)

Rétablir la notation b_ sans étoile dans le témoin. Le source TeX reste syntaxiquement lisible ; l'anomalie de notation est conservée et distinguée d'une nouvelle erreur de traduction.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$b_(\mathcal{I}^\bullet)_{\overline{x}} \to
```
Avant :
```tex
$b_*(\mathcal{I}^\bullet)_{\overline{x}} \to
```
Après :
```tex
$b_(\mathcal{I}^\bullet)_{\overline{x}} \to
```

### FR-ETALE-COHOMOLOGY-FIDELITY-084 — `lemma-blow-up-square-equivalence`

[Source officielle, ligne 23466](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L23466)

Reprendre le sens M vers K de la conclusion officielle. Le diagramme ultérieur allant dans l'autre sens reste inchangé ; cette divergence appartient à l'erratum séparé.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
Then there exists a morphism $M \to K$
```
Avant :
```tex
Alors il existe un morphisme $K \to M$
```
Après :
```tex
Alors il existe un morphisme $M \to K$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-085 — `lemma-blow-up-square-equivalence`

[Source officielle, ligne 23467](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L23467)

Rétablir a latin dans la première restriction de l'énoncé, sans modifier l'alpha grec des données.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
whose restriction to $X'$ is $a \circ f$
```
Avant :
```tex
dont la restriction à $X'$ est $\alpha \circ f$
```
Après :
```tex
dont la restriction à $X'$ est $a \circ f$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-086 — `lemma-blow-up-square-equivalence`

[Source officielle, ligne 23468](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L23468)

Rétablir b latin dans la seconde restriction, au lieu du bêta qui régularisait le nom.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
and whose restriction to $Z$ is $b \circ g$.
```
Avant :
```tex
et dont la restriction à $Z$ est $\beta \circ g$.
```
Après :
```tex
et dont la restriction à $Z$ est $b \circ g$.
```

### FR-ETALE-COHOMOLOGY-FIDELITY-087 — `lemma-blow-up-square-equivalence`

[Source officielle, ligne 23479](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L23479)

Rétablir E comme source du morphisme d'adjonction cité. Le choix de L était une correction mathématique, pas une traduction.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
adjunction mapping $E \to R\pi_*(L|_E)$
```
Avant :
```tex
morphisme d'adjonction $L \to R\pi_*(L|_E)$
```
Après :
```tex
morphisme d'adjonction $E \to R\pi_*(L|_E)$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-088 — `lemma-blow-up-square-equivalence`

[Source officielle, ligne 23481](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L23481)

Reprendre la parenthèse supplémentaire et le fragment = R de l'affichage officiel. Leur suppression est conservée dans le dossier comme suggestion éditoriale, non présentée comme texte de l'auteur.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$Rb_*(K') \to Rc_*(K'|_E)) = R$
```
Avant :
```tex
$Rb_*(K') \to Rc_*(K'|_E)$
```
Après :
```tex
$Rb_*(K') \to Rc_*(K'|_E)) = R$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-089 — `lemma-blow-up-square-equivalence`

[Source officielle, ligne 23484](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L23484)

Rétablir K sans prime dans cette phrase seulement. Les K' du triangle choisi sont réellement dans la source.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
then the map $Rb_*(K) \to Rc_*(L|_E)$
```
Avant :
```tex
alors le morphisme $Rb_*(K') \to Rc_*(L|_E)$
```
Après :
```tex
alors le morphisme $Rb_*(K) \to Rc_*(L|_E)$
```

### FR-ETALE-COHOMOLOGY-FIDELITY-090 — `lemma-h-sheaf-colim-F`

[Source officielle, ligne 23691](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L23691)

Rétablir le faisceau O_X dans le groupe sur Z. Le renommage local et uniforme du degré muet p en i est conservé : il ne change ni la quantification ni le résultat et évite la collision avec le nombre premier p de l'énoncé.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
H^p(Z, \mathcal{O}_X)
```
Avant :
```tex
H^i(Z, \mathcal{O}_Z)
```
Après :
```tex
H^i(Z, \mathcal{O}_X)
```

### FR-ETALE-COHOMOLOGY-FIDELITY-091 — `lemma-cohomology-with-support-quasi-coherent`

[Source officielle, ligne 14157](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L14157)

Retirer la définition ajoutée de i. Elle rend explicite une notation utilisée sans définition dans cet énoncé officiel ; utile comme note éditoriale séparée, elle ne doit pas être attribuée au texte source.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
Let $Z \subset X$ be a closed subscheme.
```
Avant :
```tex
Soit $Z \subset X$ un sous-schéma fermé, et soit $i : Z \to X$ l'immersion canonique.
```
Après :
```tex
Soit $Z \subset X$ un sous-schéma fermé.
```

### FR-ETALE-COHOMOLOGY-FIDELITY-092 — `lemma-reduce-to-l-group`

[Source officielle, ligne 10645](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L10645)

Rétablir la mention provisoire de référence que le témoin contient réellement. Sa suppression masquait le caractère inachevé de ce renvoi ; aucune référence n'est inventée.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
theory of finite groups; insert future reference here).
```
Avant :
```tex
des groupes finis).
```
Après :
```tex
des groupes finis ; ins\'erer ici une r\'ef\'erence ult\'erieure).
```

### FR-ETALE-COHOMOLOGY-FIDELITY-093 — `lemma-reduce-to-l-group-higher`

[Source officielle, ligne 10664](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L10664)

Le témoin distingue ici ell-torsion de ell-power torsion dans la preuve. Ne pas uniformiser silencieusement ces deux expressions en torsion primaire. Le terme français ell-torsion reprend l'expression source sans résoudre son éventuelle incohérence ; HARARI-2012-SYLOW-TORSION documente ce registre.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
$\ell$-torsion sheaves $\mathcal{F}$ if  and only if
```
Avant :
```tex
faisceau de torsion $\ell$-primaire $\mathcal{F}$ si et seulement si
```
Après :
```tex
faisceau de $\ell$-torsion $\mathcal{F}$ si et seulement si
```

### FR-ETALE-COHOMOLOGY-FIDELITY-094 — `lemma-reduce-to-l-group-higher`

[Source officielle, ligne 10688](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L10688)

Même distinction dans la dernière phrase de la preuve. La mention antérieure de torsion ell-primaire, correspondant à ell-power torsion, reste inchangée.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
clearly vanishes. Hence, as everything here is still $\ell$-torsion, we may use
```
Avant :
```tex
est manifestement nulle. Comme tout reste de torsion $\ell$-primaire, nous pouvons appliquer
```
Après :
```tex
est manifestement nulle. Comme tout reste de $\ell$-torsion, nous pouvons appliquer
```

### FR-ETALE-COHOMOLOGY-FIDELITY-095 — `lemma-gabber-h0`

[Source officielle, ligne 15018](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L15018)

Réparation d'une erreur de traduction, non restauration d'un défaut anglais : Sites est le titre du chapitre cité. La traduction en faisait à tort un morphisme de sites. Le nom du chapitre et l'identifiant du renvoi sont conservés ; aucun objet mathématique n'est ajouté.

Nature : réparation d’une erreur propre à la traduction.

Témoin officiel :
```tex
of Sites, Lemma \ref{sites-lemma-recover} combined with the map from
```
Avant :
```tex
de sites du lemme \ref{sites-lemma-recover}, composé avec le morphisme du
```
Après :
```tex
donné dans Sites, lemme \ref{sites-lemma-recover}, composé avec le morphisme du
```

### FR-ETALE-COHOMOLOGY-FIDELITY-096 — `item-finite-proper-coefficients`

[Source officielle, ligne 16079](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L16079)

La source commence la preuve par ce fragment. Retirer l'explication du dévissage ajoutée pour compléter une phrase manquante ; ne pas présenter cette reconstruction éditoriale comme une phrase de la source.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
without further mention.
```
Avant :
```tex
Nous appliquerons le dévissage par suites exactes sans autre mention.
```
Après :
```tex
Sans autre mention.
```

### FR-ETALE-COHOMOLOGY-FIDELITY-097 — `lemma-colimit-constructible`

[Source officielle, ligne 11923](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L11923)

Rétablir le renvoi officiel dans la preuve de (1). La traduction avait substitué le lemme sur les faisceaux constructibles au lemme cité sur les faisceaux localement constants finis. Même si cette substitution paraît pertinente, c'est une correction éditoriale du renvoi, non une traduction.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
and colimits of constructible sheaves are constructible
(Lemma \ref{lemma-kernel-finite-locally-constant}).
```
Avant :
```tex
et colimites finies de faisceaux constructibles sont constructibles
(lemme \ref{lemma-constructible-abelian}).
```
Après :
```tex
et colimites finies de faisceaux constructibles sont constructibles
(lemme \ref{lemma-kernel-finite-locally-constant}).
```

### FR-ETALE-COHOMOLOGY-FIDELITY-098 — `lemma-colimit-constructible`

[Source officielle, ligne 11961](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/etale-cohomology.tex#L11961)

Même rétablissement du renvoi officiel dans la preuve de (3), avec un témoin distinct et exact. La proposition de changement de référence demeure dans ce dossier, séparée du texte traduit.

Nature : rétablissement de la lecture officielle, proposition éditoriale conservée séparément.

Témoin officiel :
```tex
constructible sheaves of $\Lambda$-modules is abelian
(Lemma \ref{lemma-kernel-finite-locally-constant}).
```
Avant :
```tex
faisceaux constructibles de $\Lambda$-modules est abélienne
(lemme \ref{lemma-constructible-abelian}).
```
Après :
```tex
faisceaux constructibles de $\Lambda$-modules est abélienne
(lemme \ref{lemma-kernel-finite-locally-constant}).
```

## Variantes conservées après lecture

### `lemma-locally-constant-on-connected`

Les trois catégories correspondent réellement dans les deux témoins : ensembles, groupes abéliens, puis modules. Le comparateur qui masque le texte des formules confond les deux premiers tableaux ; ce n'est pas une preuve d'emendation. Action de pi_1 et notation pi_1-ensemble expriment la même structure dans le contexte. Aucun tableau ne doit être remplacé par une copie aveugle du premier.

### `lemma-torsion-cohomology`

La lettre d remplace une variable muette n dans la réunion des sous-faisceaux de torsion, et rend son index explicite. Le témoin utilise déjà F[d] dans la définition qui suit. Après lecture du paragraphe complet, il n'y a pas de changement de quantification, d'hypothèse ou de conclusion : cette variante notationnelle est conservée.

### `theorem-smooth-base-change`

Les deux preuves ont été lues dans leur intégralité en regard des témoins. Après les quatre restaurations délimitées, lemme des cinq exprime le 5-lemma, un U'_j conserve le quantificateur existentiel for some j, et pour tout d divisant n exprime le for d | n du contexte. Ces variantes et la grammaire française ne sont pas des corrections du contenu mathématique. Ce contrôle de fidélité ne prétend pas documenter rétrospectivement tout le canon terminologique de la traduction initiale.

### `lemma-punctual-base-change-upgrade`

Après restauration des deux termes du dernier calcul, les variantes résiduelles dans les formules sont équivalentes : E in D et E appartenant à D, somme sur i = 1,…,m et somme de i = 1 à m. La phrase de transition complétée par ci-dessous désigne le paragraphe immédiatement suivant ; aucune étape de preuve ni hypothèse n'est ajoutée.

### `lemma-h-sheaf-colim-F`

L'objet O_X a été restauré indépendamment. Dans le dernier paragraphe, tous les degrés p et leurs conditions p > 0 ont été uniformément renommés i ; il s'agit d'une variable de quantification locale. Aucun changement du nombre premier p ni des groupes énoncés n'en résulte.

[Témoins complets des variantes conservées](ETALE-COHOMOLOGY_RETAINED_CANDIDATES.json)

## Passages du canon effectivement consultés

### HARARI-2012-SYLOW-TORSION

[David Harari — Cohomologie galoisienne et théorie des nombres](https://www.imo.universite-paris-saclay.fr/~david.harari/enseignement/cogal/poly.pdf#page=35)

Cours spécialisé, Orsay, 2011–2012 ; version finale hébergée par l’auteur
Pages PDF 35–36, définition 3.4 et proposition 3.5 ; page PDF 68, théorème 6.5, p-torsion et F_p[G]-module.

Court passage : « Un p-groupe de Sylow (ou p-Sylow en abrégé) ». 
Passages lus rétrospectivement pour contrôler le registre. Dans un groupe profini, la définition et la proposition justifient le nom Sylow pour le sous-groupe pro-p maximal : conserver cet équivalent français, sans prétendre que le texte a été consulté par le traducteur initial. Le théorème 6.5 emploie p-torsion pour les modules sur F_p ; il justifie de ne pas effacer la distinction de mots avec power torsion. Il ne valide pas la preuve de Stacks ni ses éventuelles incohérences.

### SGA4-I-LIMITES

[A. Grothendieck et J. L. Verdier — SGA 4, exposé I, Préfaisceaux](https://www.cmls.polytechnique.fr/perso/laszlo/sga4/SGA4-1/sga41.pdf#page=59)

Texte français hébergé par Y. Laszlo au CMLS ; exposé I, § 8.7.1, formule (8.7.1.2)
Page PDF 59, page intérieure 53, § 8.7.1 : limite inductive représentable et propriété universelle Hom(lim Xi,Y).

Court passage : « limites inductives représentables ». 
Le passage a été consulté avant le rétablissement de colimit par limite inductive. Il établit le sens catégorique français, non la justesse du mot colimit dans la preuve de Stacks. Le témoin français avait substitué une limite projective : cette correction de la source est désormais séparée.

### GIORGIUTTI-1962-SEPARABLE

[I. Giorgiutti — Groupes de Grothendieck. Introduction](https://www.numdam.org/item/AFST_1962_4_26__151_0.pdf#page=31)

Annales de la faculté des sciences de Toulouse, série 4, tome 26 (1962), pp. 151–207
Page PDF 31, dernière remarque avant le § 2.3, condition b). Numéro de remarque mal reconnu par la couche textuelle ; aucun numéro inventé.

Court passage : « extension séparable de K ». 
Expression française d'une extension de corps séparable, distincte d'une extension finie. Passage effectivement lu avant la réparation ; attestation rétrospective, non preuve d'une consultation par le traducteur initial.

### THOM-1965-STRATES

[René Thom — Propriétés différentielles locales des ensembles analytiques](https://www.numdam.org/article/SB_1964-1966__9__69_0.pdf#page=3)

Séminaire Bourbaki, exposé 281 (1964–1965), volume 9, pp. 69–80
Page PDF 3, § 1, remarque (ii) après la partition en strates.

Court passage : « une réunion finie de strates ». 
Construction française réunion de strates. Le mot finie n'est pas ajouté au locus de Stacks, où il n'apparaît pas. L'attestation provient de la géométrie analytique et ne certifie pas l'argument sur les schémas.

## Limites et examen ultérieur

Dossier établi par IA, sans relecture experte humaine. Les identifiants des anciens registres ne sont pas inventés : leur rapprochement reste à faire. Toute difficulté restante doit être consignée ; l'avis humain ultérieur n'est pas un préalable à la réparation. La preuve des restaurations porte sur les passages cités, non sur toutes les phrases du chapitre.
