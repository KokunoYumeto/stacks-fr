# Sommes amalgamées d’espaces : fidélité à la source

**LaTeX local ; aucune édition publique corrigée à ce stade.**

[LaTeX](staged/fr/081_spaces-pushouts.fr.tex) · [Contrôles](SPACES-PUSHOUTS_FR_VALIDATION.json) · [Contextes complets](SPACES-PUSHOUTS_FR_REPAIRS.json)

Les rétablissements retirent les corrections tacites apportées au témoin officiel, sans les déclarer mauvaises mathématiquement. Les changements de catégories ou de propriétés dans la prose sont consignés au même titre que les formules. Deux retours de notation ne modifient pas la mathématique. Quatre réparations propres à la traduction emploient entier pour integral appliqué aux morphismes, d’après [EGA II, définition 6.1.1](https://www.numdam.org/item/PMIHES_1961__8__5_0.pdf), réellement consultée. [Identité et portée de cette consultation](SPACES-PUSHOUTS_FR_CONSULTED_CANON.json).

## FR-SPACES-PUSHOUTS-001 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L450)

Rétablit l’indice i que porte F dans cette donnée canonique imprimée, malgré le F sans indice fixé juste avant. Le correctif probable reste distinct de la traduction de base.

Avant :
```tex
$(f_{i, small}^{-1}\mathcal{F}, c_{ij})$
```
Après :
```tex
$(f_{i, small}^{-1}\mathcal{F}_i, c_{ij})$
```

## FR-SPACES-PUSHOUTS-002 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L721)

Rétablit Y comme premier terme du domaine de h. Le remplacement par Y prime rendait plausible la justification diagonale suivante, mais il modifiait la source.

Avant :
```tex
h : Y' \coprod E \times_Z E \longrightarrow Y' \times_Y Y'
```
Après :
```tex
h : Y \coprod E \times_Z E \longrightarrow Y' \times_Y Y'
```

## FR-SPACES-PUSHOUTS-003 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L1030)

La source répète catégorie des schémas dans cette conclusion. La traduction y avait substitué espaces algébriques ; cette réparation probable du raisonnement est retirée du texte de base.

Avant :
```tex
c'est aussi une somme amalgamée dans la catégorie des espaces algébriques
```
Après :
```tex
c'est aussi une somme amalgamée dans la catégorie des schémas
```

## FR-SPACES-PUSHOUTS-004 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L1049)

Rétablit ensemble le f sans prime et l’ordre X prime, puis Y des deux projections. La lecture publique inversait les projections et ajoutait la prime pour rendre les composées typées. Le contexte avant/après conserve explicitement cette proposition d’amélioration.

Avant :
```tex
les composées $\tilde g : V \to Z$ et $\tilde f' : U' \to Z$ de $g$ avec $Z \times_{Y'} Y \to Z$ et de $f'$ avec $Z \times_{Y'} X' \to Z$, respectivement.
```
Après :
```tex
les composées $\tilde g : V \to Z$ et $\tilde f' : U' \to Z$ de $g$ avec $Z \times_{Y'} X' \to Z$ et de $f$ avec $Z \times_{Y'} Y \to Z$, respectivement.
```

## FR-SPACES-PUSHOUTS-005 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L1207)

Rétablit la base X de la condition de platitude de F prime, sans la remplacer silencieusement par X prime.

Avant :
```tex
sur $X'$, et
```
Après :
```tex
sur $X$, et
```

## FR-SPACES-PUSHOUTS-006 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L1219)

Rétablit O_Y, et non O_V, dans la clause (a). La définition antérieure de G comme O_V-module demeure telle qu’elle figure dans le témoin.

Avant :
```tex
des $\mathcal{O}_V$- et $\mathcal{O}_{U'}$-modules de type fini
```
Après :
```tex
des $\mathcal{O}_Y$- et $\mathcal{O}_{U'}$-modules de type fini
```

## FR-SPACES-PUSHOUTS-007 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L1223)

Même restauration de O_Y dans la clause (b), sans harmoniser une incohérence de notation officielle.

Avant :
```tex
des $\mathcal{O}_V$- et $\mathcal{O}_{U'}$-modules de présentation finie
```
Après :
```tex
des $\mathcal{O}_Y$- et $\mathcal{O}_{U'}$-modules de présentation finie
```

## FR-SPACES-PUSHOUTS-008 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L1304)

Rétablit W sans prime dans le but de cette flèche finale de preuve. Les occurrences antérieures W prime sont conservées.

Avant :
```tex
$G_1(F_1(W'_1)) \to G(F(W'))$
```
Après :
```tex
$G_1(F_1(W'_1)) \to G(F(W))$
```

## FR-SPACES-PUSHOUTS-009 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L1305)

Rétablit les deux W sans prime de cette conclusion, malgré la notation W prime utilisée auparavant.

Avant :
```tex
Nous en concluons que $G(F(W')) \to W'$
```
Après :
```tex
Nous en concluons que $G(F(W)) \to W$
```

## FR-SPACES-PUSHOUTS-010 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L1307)

Même rétablissement dans la dernière phrase sur les espaces réduits associés.

Avant :
```tex
Mais $G(F(W')) \to W'$
```
Après :
```tex
Mais $G(F(W)) \to W$
```

## FR-SPACES-PUSHOUTS-011 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L1403)

Rétablit K sans prime dans la seconde mention des applications. La première mention K prime reste conforme à la source.

Avant :
```tex
$Lj^*M' \to M$ et $L(f')^*M' \to K'$ sont des isomorphismes.
```
Après :
```tex
$Lj^*M' \to M$ et $L(f')^*M' \to K$ sont des isomorphismes.
```

## FR-SPACES-PUSHOUTS-012 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L1405)

Le paragraphe officiel finit par étale, non affine ; le paragraphe suivant suppose pourtant affine. La traduction avait réparé cette discordance en prose, invisible à une simple comparaison des formules.

Avant :
```tex
supposer que $Y'$ est affine.
```
Après :
```tex
supposer que $Y'$ est \'etale.
```

## FR-SPACES-PUSHOUTS-013 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L1468)

Rétablit B prime comme anneau des complexes de cette suite, en conservant séparément la correction vers A prime.

Avant :
```tex
de complexes de $A'$-modules.
```
Après :
```tex
de complexes de $B'$-modules.
```

## FR-SPACES-PUSHOUTS-014 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L1723)

Rétablit F dans le membre droit imprimé, alors que G est le faisceau de l’énoncé. Le correctif G ne doit pas être implicite dans la traduction.

Avant :
```tex
\Gamma(Y \times_X \Spec(\mathcal{O}_{X, \overline{x}}), p^*\mathcal{G})
```
Après :
```tex
\Gamma(Y \times_X \Spec(\mathcal{O}_{X, \overline{x}}), p^*\mathcal{F})
```

## FR-SPACES-PUSHOUTS-015 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L1834)

Retrouve le nom x du point quantifié. Ce renommage de variable liée ne changeait pas la propriété ; il n’est pas compté comme un nouvel énoncé mathématique erroné.

Avant :
```tex
point $y \in |f^{-1}Z|$
```
Après :
```tex
point $x \in |f^{-1}Z|$
```

## FR-SPACES-PUSHOUTS-016 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L1985)

Rétablit le beta en x barre de cette conclusion. Gamma serait cohérent avec le domaine précédemment défini, mais cette correction ne figure pas dans le témoin.

Avant :
```tex
$\alpha_{\overline{x}}$, $\gamma_{\overline{x}}$
```
Après :
```tex
$\alpha_{\overline{x}}$, $\beta_{\overline{x}}$
```

## FR-SPACES-PUSHOUTS-017 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L2962)

Rétablit la parenthèse manquante du témoin, sans prétendre que sa formule est syntaxiquement équilibrée. La parenthèse ajoutée est documentée comme proposition séparée.

Avant :
```tex
\Ker(B \to \Gamma(X, f_*(\mathcal{O}_{X'}/I^{n + m + c}\mathcal{O}_{X'})))
```
Après :
```tex
\Ker(B \to \Gamma(X, f_*(\mathcal{O}_{X'}/I^{n + m + c}\mathcal{O}_{X'}))
```

## FR-SPACES-PUSHOUTS-018 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L3398)

Rétablit X_21 à cet endroit précis de la preuve. Toutes les autres occurrences de X_12, y compris le remplacement ultérieur, restent intactes.

Avant :
```tex
remplacer $X_2$ par un éclatement $W_2$-admissible et $X_{12}$
```
Après :
```tex
remplacer $X_2$ par un éclatement $W_2$-admissible et $X_{21}$
```

## FR-SPACES-PUSHOUTS-019 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L3563)

Retire la définition explicite f= ajoutée par la traduction. Elle expliquait le f utilisé ensuite par le texte, mais n’était pas imprimée à cet endroit ; la suppression n’est pas une correction d’un théorème faux.

Avant :
```tex
$f = f_p|_V : V \to X$
```
Après :
```tex
$f_p|_V : V \to X$
```

## FR-SPACES-PUSHOUTS-020 — Erreur de traduction réparée

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L581)

Integral qualifie ici un morphisme. Le terme français attesté est entier (EGA II, définition 6.1.1, p.110, réellement lue), et non intégral. La surjectivité ou l’injectivité universelle jointe à cette propriété reste inchangée. Les quatre occurrences du chapitre ont été vérifiées dans leur contexte.

Avant :
```tex
surjectif et intégral,
```
Après :
```tex
surjectif et entier,
```

## FR-SPACES-PUSHOUTS-021 — Erreur de traduction réparée

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L603)

Integral qualifie ici un morphisme. Le terme français attesté est entier (EGA II, définition 6.1.1, p.110, réellement lue), et non intégral. La surjectivité ou l’injectivité universelle jointe à cette propriété reste inchangée. Les quatre occurrences du chapitre ont été vérifiées dans leur contexte.

Avant :
```tex
propriétés suivantes : surjectif et intégral,
```
Après :
```tex
propriétés suivantes : surjectif et entier,
```

## FR-SPACES-PUSHOUTS-022 — Erreur de traduction réparée

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L1626)

Integral qualifie ici un morphisme. Le terme français attesté est entier (EGA II, définition 6.1.1, p.110, réellement lue), et non intégral. La surjectivité ou l’injectivité universelle jointe à cette propriété reste inchangée. Les quatre occurrences du chapitre ont été vérifiées dans leur contexte.

Avant :
```tex
intégral et universellement injectif.
```
Après :
```tex
entier et universellement injectif.
```

## FR-SPACES-PUSHOUTS-023 — Erreur de traduction réparée

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-pushouts.tex#L1668)

Integral qualifie ici un morphisme. Le terme français attesté est entier (EGA II, définition 6.1.1, p.110, réellement lue), et non intégral. La surjectivité ou l’injectivité universelle jointe à cette propriété reste inchangée. Les quatre occurrences du chapitre ont été vérifiées dans leur contexte.

Avant :
```tex
intégral et universellement injectif.
```
Après :
```tex
entier et universellement injectif.
```

## Différences fidèles conservées

### `lemma-glue-etale-sheaf-proper-surjective`

X prime = X inverse seulement l’ordre de l’égalité X = X prime. Le contexte choisit le même schéma X prime ; le morphisme entier et les trois cas du lemme sont inchangés.

### `lemma-separate-disjoint-locally-closed-by-blowing-up`

Z_1 et Z_2 remplace la liste Z_1,Z_2 ; leurs transformées strictes reprend ensuite les deux mêmes sous-espaces. L’anaphore ne supprime aucun objet et ne change ni centre ni admissibilité.

## Texte des formules vérifié

### `lemma-glue-etale-sheaf-etale`

Données de descente pour les faisceaux étales relativement à traduit le seul texte explicatif ; le site, la famille affichée et tous ses produits fibrés sont conservés. Contrôle de cette formule, sans attestation terminologique générale.

```tex
\Sh(X_\etale) \longrightarrow \text{descent data for \'etale sheaves wrt }\{f_i : X_i \to X\}
```
```tex
\Sh(X_\etale) \longrightarrow \text{données de descente pour les faisceaux \'etales relativement à }\{f_i : X_i \to X\}
```

### `lemma-reduce-to-scheme-base`

Données de descente pour les faisceaux étales relativement à traduit le seul texte explicatif ; le site, la famille affichée et tous ses produits fibrés sont conservés. Contrôle de cette formule, sans attestation terminologique générale.

```tex
\Sh(Y_{i, \etale}) \longrightarrow \text{descent data for \'etale sheaves wrt }\{X \times_Y Y_i \to Y_i\}
```
```tex
\Sh(Y_{i, \etale}) \longrightarrow \text{données de descente pour les faisceaux \'etales relativement à }\{X \times_Y Y_i \to Y_i\}
```

### `lemma-reduce-to-scheme-base`

Données de descente pour les faisceaux étales relativement à traduit le seul texte explicatif ; le site, la famille affichée et tous ses produits fibrés sont conservés. Contrôle de cette formule, sans attestation terminologique générale.

```tex
\Sh((Y_i \times_Y Y_j)_\etale) \longrightarrow \text{descent data for \'etale sheaves wrt } \{X \times_Y Y_i \times_Y Y_j \to Y_i \times_Y Y_j\}
```
```tex
\Sh((Y_i \times_Y Y_j)_\etale) \longrightarrow \text{données de descente pour les faisceaux \'etales relativement à } \{X \times_Y Y_i \times_Y Y_j \to Y_i \times_Y Y_j\}
```

### `lemma-reduce-to-scheme-base`

Données de descente pour les faisceaux étales relativement à traduit le seul texte explicatif ; le site, la famille affichée et tous ses produits fibrés sont conservés. Contrôle de cette formule, sans attestation terminologique générale.

```tex
\Sh(Y_\etale) \longrightarrow \text{descent data for \'etale sheaves wrt }\{X \to Y\}
```
```tex
\Sh(Y_\etale) \longrightarrow \text{données de descente pour les faisceaux \'etales relativement à }\{X \to Y\}
```

### `lemma-representable-case`

Données de descente pour les faisceaux étales relativement à traduit le seul texte explicatif ; le site, la famille affichée et tous ses produits fibrés sont conservés. Contrôle de cette formule, sans attestation terminologique générale.

```tex
\Sh(Y_\etale) \longrightarrow \text{descent data for \'etale sheaves wrt }\{X \to Y\}
```
```tex
\Sh(Y_\etale) \longrightarrow \text{données de descente pour les faisceaux \'etales relativement à }\{X \to Y\}
```

### `lemma-reduce-to-scheme-source`

Données de descente pour les faisceaux étales relativement à traduit le seul texte explicatif ; le site, la famille affichée et tous ses produits fibrés sont conservés. Contrôle de cette formule, sans attestation terminologique générale.

```tex
\Sh(Y_\etale) \longrightarrow \text{descent data for \'etale sheaves wrt }\{X \to Y\}
```
```tex
\Sh(Y_\etale) \longrightarrow \text{données de descente pour les faisceaux \'etales relativement à }\{X \to Y\}
```

### `lemma-glue-etale-sheaf-proper-surjective`

Données de descente pour les faisceaux étales relativement à traduit le seul texte explicatif ; le site, la famille affichée et tous ses produits fibrés sont conservés. Contrôle de cette formule, sans attestation terminologique générale.

```tex
\Sh(Y_\etale) \longrightarrow \text{descent data for \'etale sheaves wrt }\{X \to Y\}
```
```tex
\Sh(Y_\etale) \longrightarrow \text{données de descente pour les faisceaux \'etales relativement à }\{X \to Y\}
```

### `lemma-glue-etale-sheaf-fppf`

Données de descente pour les faisceaux étales relativement à traduit le seul texte explicatif ; le site, la famille affichée et tous ses produits fibrés sont conservés. Contrôle de cette formule, sans attestation terminologique générale.

```tex
\Sh(X_\etale) \longrightarrow \text{descent data for \'etale sheaves wrt }\{f_i : X_i \to X\}
```
```tex
\Sh(X_\etale) \longrightarrow \text{données de descente pour les faisceaux \'etales relativement à }\{f_i : X_i \to X\}
```

### `lemma-glue-etale-sheaf-modification`

Données de descente pour les faisceaux étales relativement à traduit le seul texte explicatif ; le site, la famille affichée et tous ses produits fibrés sont conservés. Contrôle de cette formule, sans attestation terminologique générale.

```tex
\Sh(Y'_\etale) \times_{\Sh(E_\etale)} \Sh(Z_\etale) \longrightarrow \text{descent data for \'etale sheaves wrt }\{X \to Y\}
```
```tex
\Sh(Y'_\etale) \times_{\Sh(E_\etale)} \Sh(Z_\etale) \longrightarrow \text{données de descente pour les faisceaux \'etales relativement à }\{X \to Y\}
```

### `lemma-pushout-along-thickening`

La conjonction and devient et entre les deux carrés cartésiens inchangés.

```tex
\vcenter{ \xymatrix{ U' \ar[d] \ar[r] & V' \ar[d]^h \\ X' \ar[r]^{a'} & Z } } \quad\text{and}\quad \vcenter{ \xymatrix{ V \ar[r] \ar[d] & V' \ar[d]^h \\ Y \ar[r]^b & Z } }
```
```tex
\vcenter{ \xymatrix{ U' \ar[d] \ar[r] & V' \ar[d]^h \\ X' \ar[r]^{a'} & Z } } \quad\text{et}\quad \vcenter{ \xymatrix{ V \ar[r] \ar[d] & V' \ar[d]^h \\ Y \ar[r]^b & Z } }
```

### `lemma-categories-spaces-over-pushout`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
F : (\textit{Spaces}/Y') \longrightarrow (\textit{Spaces}/Y) \times_{(\textit{Spaces}/Y')} (\textit{Spaces}/X')
```
```tex
F : (\textit{Espaces}/Y') \longrightarrow (\textit{Espaces}/Y) \times_{(\textit{Espaces}/Y')} (\textit{Espaces}/X')
```

### `lemma-categories-spaces-over-pushout`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
G : (\textit{Spaces}/Y) \times_{(\textit{Spaces}/Y')} (\textit{Spaces}/X') \longrightarrow (\textit{Spaces}/Y')
```
```tex
G : (\textit{Espaces}/Y) \times_{(\textit{Espaces}/Y')} (\textit{Espaces}/X') \longrightarrow (\textit{Espaces}/Y')
```

### `equation-cube`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\xymatrix{ (\Sch/Y_1') \ar@<-1ex>[r]_-{F_1} \ar[d] & (\Sch/Y_1) \times_{(\Sch/Y_1')} (\Sch/X_1') \ar[d] \ar@<-1ex>[l]_-{G_1} \\ (\textit{Spaces}/Y') \ar@<-1ex>[r]_-F & (\textit{Spaces}/Y) \times_{(\textit{Spaces}/Y')} (\textit{Spaces}/X') \ar@<-1ex>[l]_-G }
```
```tex
\xymatrix{ (\Sch/Y_1') \ar@<-1ex>[r]_-{F_1} \ar[d] & (\Sch/Y_1) \times_{(\Sch/Y_1')} (\Sch/X_1') \ar[d] \ar@<-1ex>[l]_-{G_1} \\ (\textit{Espaces}/Y') \ar@<-1ex>[r]_-F & (\textit{Espaces}/Y) \times_{(\textit{Espaces}/Y')} (\textit{Espaces}/X') \ar@<-1ex>[l]_-G }
```

### `equation-cube`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
(\textit{Spaces}/Y) \times_{(\textit{Spaces}/Y')} (\textit{Spaces}/X')
```
```tex
(\textit{Espaces}/Y) \times_{(\textit{Espaces}/Y')} (\textit{Espaces}/X')
```

### `lemma-equivalence-categories-spaces-pushout-flat`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
(\textit{Spaces}/Y) \times_{(\textit{Spaces}/Y')} (\textit{Spaces}/X')
```
```tex
(\textit{Espaces}/Y) \times_{(\textit{Espaces}/Y')} (\textit{Espaces}/X')
```

### `section-formal-glueing-spaces`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\textit{Spaces}(Y \to X, Z)
```
```tex
\textit{Espaces}(Y \to X, Z)
```

### `lemma-equivalence-on-affine`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\textit{Spaces}(Y \to X, Z)
```
```tex
\textit{Espaces}(Y \to X, Z)
```

### `lemma-equivalence-on-affine`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\textit{Spaces}(Y \to X, Z)
```
```tex
\textit{Espaces}(Y \to X, Z)
```

### `lemma-equivalence-on-affine`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\textit{Spaces}(Y \to X, Z)
```
```tex
\textit{Espaces}(Y \to X, Z)
```

### `lemma-fully-faithful-on-separated`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\Mor_X(X'_1, X'_2) \longrightarrow \Mor_{\textit{Spaces}(Y \to X, Z)}(F(X'_1), F(X'_2))
```
```tex
\Mor_X(X'_1, X'_2) \longrightarrow \Mor_{\textit{Espaces}(Y \to X, Z)}(F(X'_1), F(X'_2))
```

### `lemma-fully-faithful-on-separated`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\textit{Spaces}(Y \to X, Z)
```
```tex
\textit{Espaces}(Y \to X, Z)
```

### `lemma-fully-faithful-on-separated`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\textit{Spaces}(Y \times_X (X'_1 \times_X X'_2) \to X'_1 \times_X X'_2, Z \times_X (X'_1 \times_X X'_2))
```
```tex
\textit{Espaces}(Y \times_X (X'_1 \times_X X'_2) \to X'_1 \times_X X'_2, Z \times_X (X'_1 \times_X X'_2))
```

### `section-glueing-beauville-laszlo`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\textit{Spaces}(U \leftarrow U' \to X')
```
```tex
\textit{Espaces}(U \leftarrow U' \to X')
```

### `lemma-glueable`

Respectivement développe resp. entre les deux suites exactes, sans changer aucun terme ni leur ordre.

```tex
0 \to A \to A_f \oplus A' \to A'_f \to 0, \quad\text{resp.}\quad 0 \to B \to B_f \oplus B' \to B'_f \to 0,
```
```tex
0 \to A \to A_f \oplus A' \to A'_f \to 0, \quad\text{respectivement}\quad 0 \to B \to B_f \oplus B' \to B'_f \to 0,
```

### `lemma-glueing-affines`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\textit{Spaces}(U \leftarrow U' \to X')
```
```tex
\textit{Espaces}(U \leftarrow U' \to X')
```

### `lemma-glueing-affines`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\textit{Spaces}(U \leftarrow U' \to X')
```
```tex
\textit{Espaces}(U \leftarrow U' \to X')
```

### `lemma-glueing-affines`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\textit{Spaces}(U \leftarrow U' \to X')
```
```tex
\textit{Espaces}(U \leftarrow U' \to X')
```

### `lemma-glueing-f`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\textit{Spaces}(U \leftarrow U' \to X')
```
```tex
\textit{Espaces}(U \leftarrow U' \to X')
```

### `lemma-glueing-ff`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\textit{Spaces}(U \leftarrow U' \to X')
```
```tex
\textit{Espaces}(U \leftarrow U' \to X')
```

### `lemma-glueing-quasi-affines`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\textit{Spaces}(U \leftarrow U' \to X')
```
```tex
\textit{Espaces}(U \leftarrow U' \to X')
```

### `lemma-glueing-quasi-affines`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\textit{Spaces}(U \leftarrow U' \to X')
```
```tex
\textit{Espaces}(U \leftarrow U' \to X')
```

### `lemma-glueing-quasi-affines`

Et relie les deux mêmes flèches issues des produits fibrés ; leurs bases et buts sont inchangés.

```tex
U \times_X T \longrightarrow V \quad\text{and}\quad X' \times_X T \longrightarrow Y'
```
```tex
U \times_X T \longrightarrow V \quad\text{et}\quad X' \times_X T \longrightarrow Y'
```

### `lemma-glueing-quasi-affines`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\textit{Spaces}(U \leftarrow U' \to X')
```
```tex
\textit{Espaces}(U \leftarrow U' \to X')
```

### `lemma-glueing-quasi-affines`

Spaces devient Espaces dans le nom de la même catégorie. Les arguments, bases des produits fibrés et sens des flèches sont conservés, y compris les anomalies éventuelles du témoin.

```tex
\textit{Spaces}(U \leftarrow U' \to X')
```
```tex
\textit{Espaces}(U \leftarrow U' \to X')
```

### `lemma-coequalizer`

Et relie les deux mêmes images directes de faisceaux structuraux.

```tex
g_*\mathcal{O}_Y \quad\text{and}\quad h_*\mathcal{O}_R
```
```tex
g_*\mathcal{O}_Y \quad\text{et}\quad h_*\mathcal{O}_R
```

### `lemma-coequalizer`

Equalizer devient Égalisateur, sans remplacer cette opération par un conoyau. Les deux flèches, leurs domaines et leurs buts sont inchangés. Le présent contrôle porte sur la fidélité de cette formule ; il ne prétend pas arbitrer globalement les variantes égaliseur/égalisateur.

```tex
\mathcal{A} = \text{Equalizer}\left(s^\sharp, t^\sharp : g_*\mathcal{O}_Y \longrightarrow h_*\mathcal{O}_R\right)
```
```tex
\mathcal{A} = \text{Égalisateur}\left(s^\sharp, t^\sharp : g_*\mathcal{O}_Y \longrightarrow h_*\mathcal{O}_R\right)
```

### `lemma-coequalizer`

Equalizer devient Égalisateur, sans remplacer cette opération par un conoyau. Les deux flèches, leurs domaines et leurs buts sont inchangés. Le présent contrôle porte sur la fidélité de cette formule ; il ne prétend pas arbitrer globalement les variantes égaliseur/égalisateur.

```tex
\Mor_S(X, Z) \longrightarrow \text{Equalizer}(s, t : \Mor_S(Y, Z) \to \Mor_S(R, Z))
```
```tex
\Mor_S(X, Z) \longrightarrow \text{Égalisateur}(s, t : \Mor_S(Y, Z) \to \Mor_S(R, Z))
```

### `lemma-coequalizer`

Equalizer devient Égalisateur, sans remplacer cette opération par un conoyau. Les deux flèches, leurs domaines et leurs buts sont inchangés. Le présent contrôle porte sur la fidélité de cette formule ; il ne prétend pas arbitrer globalement les variantes égaliseur/égalisateur.

```tex
\Gamma(X, \mathcal{O}_X) = \text{Equalizer}\left( s^\sharp, t^\sharp : \Gamma(Y, \mathcal{O}_Y) \to \Gamma(R, \mathcal{O}_R) \right)
```
```tex
\Gamma(X, \mathcal{O}_X) = \text{Égalisateur}\left( s^\sharp, t^\sharp : \Gamma(Y, \mathcal{O}_Y) \to \Gamma(R, \mathcal{O}_R) \right)
```

### `lemma-essentially-constant`

Equalizer devient Égalisateur, sans remplacer cette opération par un conoyau. Les deux flèches, leurs domaines et leurs buts sont inchangés. Le présent contrôle porte sur la fidélité de cette formule ; il ne prétend pas arbitrer globalement les variantes égaliseur/égalisateur.

```tex
\mathcal{A} = \text{Equalizer}( \xymatrix{ f_*\mathcal{O}_{X'} \ar@<1ex>[r] \ar@<-1ex>[r] & (f \times f)_*\mathcal{O}_{X' \times_X X'} } )
```
```tex
\mathcal{A} = \text{Égalisateur}( \xymatrix{ f_*\mathcal{O}_{X'} \ar@<1ex>[r] \ar@<-1ex>[r] & (f \times f)_*\mathcal{O}_{X' \times_X X'} } )
```

### `lemma-essentially-constant`

Equalizer devient Égalisateur, sans remplacer cette opération par un conoyau. Les deux flèches, leurs domaines et leurs buts sont inchangés. Le présent contrôle porte sur la fidélité de cette formule ; il ne prétend pas arbitrer globalement les variantes égaliseur/égalisateur.

```tex
\mathcal{A}_n = \text{Equalizer}( \xymatrix{ \mathcal{A} \times \mathcal{O}_X/\mathcal{I}^n \ar@<1ex>[r] \ar@<-1ex>[r] & f_{n, *}\mathcal{O}_{X' \times_X Z_n} } )
```
```tex
\mathcal{A}_n = \text{Égalisateur}( \xymatrix{ \mathcal{A} \times \mathcal{O}_X/\mathcal{I}^n \ar@<1ex>[r] \ar@<-1ex>[r] & f_{n, *}\mathcal{O}_{X' \times_X Z_n} } )
```

### `lemma-blowup-etale-along`

And the diagram devient et le diagramme : les deux diagrammes, les barres et les indices sont inchangés.

```tex
\vcenter{ \xymatrix{ X_1 \ar[rr] \ar[rd] & & X \ar[ld] \\ & Y } } \quad\text{and the diagram}\quad \vcenter{ \xymatrix{ \overline{A}_1 \ar[rr] \ar[rd] & & \overline{A} \ar[ld] \\ & \overline{B} } }
```
```tex
\vcenter{ \xymatrix{ X_1 \ar[rr] \ar[rd] & & X \ar[ld] \\ & Y } } \quad\text{et le diagramme}\quad \vcenter{ \xymatrix{ \overline{A}_1 \ar[rr] \ar[rd] & & \overline{A} \ar[ld] \\ & \overline{B} } }
```

### `lemma-two-compactifications`

Et relie les mêmes projections p_1 et p_2 de X_12 vers X_1 et X_2.

```tex
p_1 : X_{12} \to X_1 \quad\text{and}\quad p_2 : X_{12} \to X_2
```
```tex
p_1 : X_{12} \to X_1 \quad\text{et}\quad p_2 : X_{12} \to X_2
```

## Limites

Chaque contexte modifié et chaque différence conservée ci-dessus a été lu dans les deux langues. Les contrôles sur tous les blocs étiquetés ne certifient pas l’intégralité de la prose ni de la terminologie. Les anomalies du témoin officiel restaurées ne sont pas présentées comme mathématiquement correctes. L’inversion des opérations reproduit exactement la version publique. La construction et la vérification publique du lecteur complet restent à effectuer.
