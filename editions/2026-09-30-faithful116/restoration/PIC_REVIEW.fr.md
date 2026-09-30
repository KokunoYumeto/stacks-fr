# Foncteurs de Picard : retour au témoin officiel

**LaTeX local en cours de réparation ; aucune nouvelle édition publique à ce stade.**

[LaTeX](staged/fr/044_pic.fr.tex) · [Contrôles](PIC_FR_VALIDATION.json) · [Avant/après et contextes](PIC_FR_REPAIRS.json)

Les quinze opérations ne sont pas quinze théorèmes erronés : trois retirent des bornes de coproduit rendues explicites, une revient du mot unité au mot élément. Les autres rétablissent des symboles ou un numéro effectivement imprimés, parfois fautifs. La traduction de base ne les corrige pas silencieusement. Les lectures antérieures, y compris les améliorations plausibles, sont conservées dans ce dossier séparé. Aucun vocabulaire spécialisé nouveau n’est introduit ni aucune consultation externe inventée.

## FR-PIC-001 — `proposition-hilb-d-representable`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pic.tex#L355)

Rétablit le t minuscule imprimé dans cette restriction seulement. La majuscule T prime est probablement voulue, mais sa substitution est une correction de la source, non une traduction ; les autres T prime restent inchangés.

Avant :
```tex
la restriction $Z_{T'}$ a son image
```
Après :
```tex
la restriction $Z_{t'}$ a son image
```

## FR-PIC-002 — `lemma-sum-divisors-on-curves`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pic.tex#L496)

Retire les bornes explicites ajoutées à ce coproduit. Elles étaient déjà implicites dans les points x_1,…,x_n du paragraphe et ne changent pas le résultat : ce rétablissement de notation ne constitue pas un théorème corrigé.

Avant :
```tex
D_1 = \coprod_{i = 1}^n \Spec
```
Après :
```tex
D_1 = \coprod \Spec
```

## FR-PIC-003 — `lemma-sum-divisors-on-curves`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pic.tex#L498)

Retire les bornes explicites ajoutées à ce coproduit. Elles étaient déjà implicites dans les points x_1,…,x_n du paragraphe et ne changent pas le résultat : ce rétablissement de notation ne constitue pas un théorème corrigé.

Avant :
```tex
D_2 = \coprod_{i = 1}^n \Spec
```
Après :
```tex
D_2 = \coprod \Spec
```

## FR-PIC-004 — `lemma-sum-divisors-on-curves`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pic.tex#L502)

Retire les bornes explicites ajoutées à ce coproduit. Elles étaient déjà implicites dans les points x_1,…,x_n du paragraphe et ne changent pas le résultat : ce rétablissement de notation ne constitue pas un théorème corrigé.

Avant :
```tex
D = \coprod_{i = 1}^n \Spec
```
Après :
```tex
D = \coprod \Spec
```

## FR-PIC-005 — `lemma-flat-geometrically-connected-fibres-with-section`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pic.tex#L848)

Rétablit alpha_j sans inverse tel qu’il est imprimé. L’inverse rendrait la composition typée avec la définition précédente ; cette amélioration reste proposée séparément, et l’anomalie restaurée n’est pas cautionnée.

Avant :
```tex
\alpha_j^{-1}|_{T_i \times_T T_j}
```
Après :
```tex
\alpha_j|_{T_i \times_T T_j}
```

## FR-PIC-006 — `lemma-flat-geometrically-connected-fibres-with-section`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pic.tex#L869)

Rétablit X comme but du recouvrement mentionné par la source ; le remplacement par X_T était une correction implicite du texte.

Avant :
```tex
$\{X_{T_i} \to X_T\}$
```
Après :
```tex
$\{X_{T_i} \to X\}$
```

## FR-PIC-007 — `lemma-twist-with-general-divisor`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pic.tex#L1148)

Rétablit x dans cette phrase conclusive. L’occurrence précédente x_K reste inchangée, car elle figure déjà dans la source.

Avant :
```tex
Puisque $s$ ne s'annule pas en $x_K$, on en conclut
```
Après :
```tex
Puisque $s$ ne s'annule pas en $x$, on en conclut
```

## FR-PIC-008 — `lemma-twist-with-general-divisor`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pic.tex#L1150)

Rétablit le X non changé de base au but de cette flèche. Le faisceau est défini sur X_K dans le contexte ; cette incohérence du témoin est explicitement conservée, non validée mathématiquement.

Avant :
```tex
H^0(X_K, \mathcal{L}) \longrightarrow H^0(X_K, i_*i^*\mathcal{L})
```
Après :
```tex
H^0(X_K, \mathcal{L}) \longrightarrow H^0(X, i_*i^*\mathcal{L})
```

## FR-PIC-009 — `lemma-picard-pieces`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pic.tex#L1263)

Rétablit le K majuscule de cette phrase, malgré le corps k fixé dans le contexte. Les autres indices X/k ne sont pas changés.

Avant :
```tex
$\underline{\Hilbfunctor}^g_{X/k}$ est lisse de dimension $g$
```
Après :
```tex
$\underline{\Hilbfunctor}^g_{X/K}$ est lisse de dimension $g$
```

## FR-PIC-010 — `lemma-picard-pieces`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pic.tex#L1287)

Rétablit le numéro (2) effectivement écrit dans la source, sans le remplacer par le numéro (1) auquel semble se rapporter l’argument de propreté.

Avant :
```tex
Cela achève la démonstration de (1), car
```
Après :
```tex
Cela achève la démonstration de (2), car
```

## FR-PIC-011 — `lemma-pic-descends`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pic.tex#L1361)

Rétablit k_lambda sans prime dans cette occurrence. L’introduction initiale k prime = colim k prime_lambda reste intacte ; on ne résout pas silencieusement la discordance de notation du témoin.

Avant :
```tex
$X_{k'} = \lim X_{k'_\lambda}$
```
Après :
```tex
$X_{k'} = \lim X_{k_\lambda}$
```

## FR-PIC-012 — `lemma-pic-descends`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pic.tex#L1365)

Rétablit k_lambda sans prime dans cette occurrence. L’introduction initiale k prime = colim k prime_lambda reste intacte ; on ne résout pas silencieusement la discordance de notation du témoin.

Avant :
```tex
\Pic(X_{k'}) = \colim \Pic(X_{k'_\lambda})
```
Après :
```tex
\Pic(X_{k'}) = \colim \Pic(X_{k_\lambda})
```

## FR-PIC-013 — `lemma-pic-descends`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pic.tex#L1371)

Rétablit k_lambda sans prime dans cette occurrence. L’introduction initiale k prime = colim k prime_lambda reste intacte ; on ne résout pas silencieusement la discordance de notation du témoin.

Avant :
```tex
$\text{Gal}(k'/k'_\lambda)$
```
Après :
```tex
$\text{Gal}(k'/k_\lambda)$
```

## FR-PIC-014 — `lemma-torsion-descends`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pic.tex#L1459)

Rétablit pr_0 à la dernière flèche du composé, telle qu’elle est imprimée. Pr_1 serait compatible avec L_1 au départ de cette flèche ; le correctif reste lisible séparément.

Avant :
```tex
\xrightarrow{\text{pr}_1^*\alpha}
```
Après :
```tex
\xrightarrow{\text{pr}_0^*\alpha}
```

## FR-PIC-015 — `lemma-torsion-descends`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pic.tex#L1452)

Rétablit le mot élément employé par la source, sans y expliciter unité. Le contexte de l’isomorphisme motive la précision antérieure ; il ne s’agit pas d’une nouvelle erreur de théorème. La traduction de base conserve le degré d’explicitation de la phrase officielle.

Avant :
```tex
une unité convenable de $A$. Considérons l'application
```
Après :
```tex
un élément convenable de $A$. Considérons l'application
```

## Lecture fidèle conservée

Correspondance biunivoque traduit la bijection un-à-un sans garder deux nombres 1 isolés dans des formules. Les points rationnels, diviseurs effectifs, degrés et extensions de corps sont identiques ; le contexte complet a été lu.

## Texte des formules vérifié

### `section-hilbert-scheme-points`

La condition de sous-schéma fermé, fini localement libre de degré d sur T est la même dans les deux cases de définition.

```tex
\Hilbfunctor^d_{X/S}(T) = \left\{ \begin{matrix} Z \subset X_T\text{ closed subscheme such that }\\ Z \to T\text{ is finite locally free of degree }d \end{matrix} \right\}
```
```tex
\Hilbfunctor^d_{X/S}(T) = \left\{ \begin{matrix} Z \subset X_T\text{ sous-schéma fermé tel que }\\ Z \to T\text{ soit fini localement libre de degré }d \end{matrix} \right\}
```

### `section-hilbert-scheme-points`

Ensembles traduit le nom de la catégorie Sets ; le domaine (Sch/S) opposé reste inchangé.

```tex
\Hilbfunctor^d_{X/S} : (\Sch/S)^{opp} \longrightarrow \textit{Sets},\quad T \longrightarrow \Hilbfunctor^d_{X/S}(T)
```
```tex
\Hilbfunctor^d_{X/S} : (\Sch/S)^{opp} \longrightarrow \textit{Ensembles},\quad T \longrightarrow \Hilbfunctor^d_{X/S}(T)
```

### `lemma-sum-divisors-on-curves`

Et relie les mêmes expressions de D_1 et D_2 ; les trois coproduits ont retrouvé la notation non explicitée de la source.

```tex
D_1 = \coprod \Spec(\mathcal{O}_{X, x_i}/(f_{i, 1})) \quad\text{and}\quad D_2 = \coprod \Spec(\mathcal{O}_{X, x_i}/(f_{i, 2}))
```
```tex
D_1 = \coprod \Spec(\mathcal{O}_{X, x_i}/(f_{i, 1})) \quad\text{et}\quad D_2 = \coprod \Spec(\mathcal{O}_{X, x_i}/(f_{i, 2}))
```

### `definition-picard-functor`

Ensembles traduit Sets dans la définition du foncteur de Picard, sans modifier le domaine ni la fonctorialité.

```tex
(\Sch/S)_{fppf} \longrightarrow \textit{Sets},\quad T \longmapsto \Pic(X_T)
```
```tex
(\Sch/S)_{fppf} \longrightarrow \textit{Ensembles},\quad T \longmapsto \Pic(X_T)
```

### `lemma-flat-geometrically-connected-fibres-with-section`

De se rattache au mot endomorphisme qui précède la formule ; il rend on sans changer le faisceau sur lequel agit le composé.

```tex
\varphi_{ki}|_{X_{T_i \times_T T_j \times_T T_k}} \circ \varphi_{jk}|_{X_{T_i \times_T T_j \times_T T_k}} \circ \varphi_{ij}|_{X_{T_i \times_T T_j \times_T T_k}} \quad\text{on}\quad \mathcal{L}_i|_{X_{T_i \times_T T_j \times_T T_k}}
```
```tex
\varphi_{ki}|_{X_{T_i \times_T T_j \times_T T_k}} \circ \varphi_{jk}|_{X_{T_i \times_T T_j \times_T T_k}} \circ \varphi_{ij}|_{X_{T_i \times_T T_j \times_T T_k}} \quad\text{de}\quad \mathcal{L}_i|_{X_{T_i \times_T T_j \times_T T_k}}
```

### `lemma-criterion`

Groupes désigne Groups pour le même foncteur G et le même domaine de schémas.

```tex
G : (\Sch/k)^{opp} \to \textit{Groups}
```
```tex
G : (\Sch/k)^{opp} \to \textit{Groupes}
```

### `lemma-open-representable`

Correspond à une section s de conserve le même produit tensoriel et la même condition du sous-ensemble.

```tex
f_T^*\mathcal{N} \longrightarrow \mathcal{L} \quad\text{corresponds to a section }s\text{ of}\quad \mathcal{L} \otimes f_T^*\mathcal{N}^{\otimes -1}
```
```tex
f_T^*\mathcal{N} \longrightarrow \mathcal{L} \quad\text{correspond à une section }s\text{ de}\quad \mathcal{L} \otimes f_T^*\mathcal{N}^{\otimes -1}
```

### `lemma-torsion-descends`

Sur indique le même produit fibré triple sur lequel est demandée l’égalité de cocycle.

```tex
\text{pr}_{12}^*\varphi \circ \text{pr}_{01}^*\varphi = \text{pr}_{02}^*\varphi \quad\text{on}\quad X_{k'} \times_X X_{k'} \times_X X_{k'} = X_{k' \otimes_k k' \otimes_k k'}
```
```tex
\text{pr}_{12}^*\varphi \circ \text{pr}_{01}^*\varphi = \text{pr}_{02}^*\varphi \quad\text{sur}\quad X_{k'} \times_X X_{k'} \times_X X_{k'} = X_{k' \otimes_k k' \otimes_k k'}
```

## Limites

Les huit contextes complets concernés ont été comparés directement. Le contrôle de candidats couvre tous les blocs étiquetés ; il ne certifie pas l’intégralité de la prose ni de la terminologie du chapitre. L’inversion des opérations reproduit exactement les octets publiés. Les identifiants, renvois et environnements concordent avec la source. Construction du lecteur complet et vérification publique restent à faire.
