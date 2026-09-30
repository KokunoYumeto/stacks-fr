# Groupoïdes : mise en page conservée après comparaison

**LaTeX local ; aucune édition publique corrigée à ce stade.**

[LaTeX](staged/fr/039_groupoids.fr.tex) · [Contrôles](GROUPOIDS_FR_VALIDATION.json) · [Contextes complets](GROUPOIDS_FR_REPAIRS.json)

Les dix contextes candidats ont été lus intégralement dans les deux langues. Aucune opération éditoriale n’est justifiée par leurs différences ; la copie de travail reste identique au témoin public. Les noms smooth et syntomic de la liste mathématique restent des identifiants du témoin et ne valent pas certification de la localisation terminologique complète. Les contrôles ci-dessous sont délimités, non une approbation de chaque phrase du chapitre.

## Différences fidèles conservées

### `lemma-etale-equivalence-relation`

Le seul changement du diagramme est @C-1pc, qui resserre les colonnes. Les objets, flèches, étiquettes, trois conditions et la preuve par la diagonale sont conservés.

### `section-principal-homogeneous`

Les allowbreak autorisent des coupures dans la liste des cinq topologies sans changer ses membres ni leur ordre. La comparaison plus fine que traduit stronger than, même si le sens de cette comparaison appelle un erratum de source séparé ; elle n’est pas inversée silencieusement.

### `definition-principal-homogeneous-space`

Les coupures de ligne ne changent pas les quatre clauses. Le choix fpqc par défaut, la note SGA3, puis les variantes étale et Zariski restent explicites et distincts.

### `lemma-torsor`

Seules des coupures sont ajoutées à la liste des topologies ; les deux sens de l’équivalence et la preuve omise sont conservés.

### `lemma-colimit-coherent`

Deux tuples QCoh reçoivent allowbreak et leur paragraphe un réglage emergencystretch. Ni les deux hypothèses ni les produits fibrés, l’injectivité ou les limites filtrantes ne changent. Le réglage local est une mise en page, pas une nouvelle démonstration.

### `section-quotient-sheaves`

La liste des topologies reçoit des coupures ; le but Sets devient Ensembles. La prérelation, la relation engendrée et le quotient qui définit le préfaisceau gardent leur portée.

### `lemma-quotient-pre-equivalence`

Les coupures ne modifient pas la liste. Les deux conditions équivalentes, la surjectivité de faisceaux et l’indication de preuve sont conservées.

### `lemma-quotient-pre-equivalence-relation-restrict`

Coupures uniquement dans la liste ; l’injectivité générale puis l’isomorphisme sous l’hypothèse de surjectivité des faisceaux restent distincts. Les raffinements de recouvrements dans la preuve sont conservés.

### `lemma-quotient-groupoid-restrict`

Les coupures dans la liste ne changent ni la condition sur le composé h ni ses trois conditions suffisantes. Les projections 0 et 1 dans la preuve sont conservées avec leur source.

### `lemma-criterion-fibre-product`

Les coupures dans la liste ne changent pas les deux diagrammes ni les preuves d’injectivité et de surjectivité. La lecture source t(r prime), sans prime sur t dans la dernière partie, reste fidèle et n’est pas corrigée tacitement.

## Texte des formules vérifié

### `example-constant-group`

Localement constante qualifie bien l’application f de T vers G ; aucune condition de constance globale n’est substituée.

```tex
T/S \longmapsto G_S(T) = \{f : T \to G \text{ locally constant}\}
```
```tex
T/S \longmapsto G_S(T) = \{f : T \to G \text{ localement constante}\}
```

### `lemma-algebraic-center`

Intersection schématique maintient la précision scheme theoretic ; ni H ni les noyaux des automorphismes intérieurs ne changent.

```tex
C = H \cap \bigcap\nolimits_i \Ker(\text{inn}_{g_i} : G \to G) \quad (\text{scheme theoretic intersection})
```
```tex
C = H \cap \bigcap\nolimits_i \Ker(\text{inn}_{g_i} : G \to G) \quad (\text{intersection schématique})
```

### `lemma-degree-multiplication-by-d`

Respectivement conserve l’ordre des deux polynômes et leurs exposants nd² et n.

```tex
n \longmapsto \chi(A, \mathcal{N}^{\otimes nd^2}),\quad \text{respectively}\quad n \longmapsto \chi(A, \mathcal{N}^{\otimes n})
```
```tex
n \longmapsto \chi(A, \mathcal{N}^{\otimes nd^2}),\quad \text{respectivement}\quad n \longmapsto \chi(A, \mathcal{N}^{\otimes n})
```

### `lemma-complete-reducibility-Gm`

Dans conserve l’anneau ambiant, les coefficients f_n et l’égalité avec les sections globales.

```tex
a^\sharp(f) = \sum\nolimits_{n \in \mathbf{Z}} f_n \otimes x^n \quad\text{in}\quad A \otimes \mathbf{Z}[x, x^{-1}] = \Gamma(\mathbf{G}_m \times X, \mathcal{O}_{\mathbf{G}_m \times X})
```
```tex
a^\sharp(f) = \sum\nolimits_{n \in \mathbf{Z}} f_n \otimes x^n \quad\text{dans}\quad A \otimes \mathbf{Z}[x, x^{-1}] = \Gamma(\mathbf{G}_m \times X, \mathcal{O}_{\mathbf{G}_m \times X})
```

### `lemma-pushforward`

Et relie les deux diagrammes : le premier utilise t et t prime, le second s et s prime ; leurs flèches restent intactes.

```tex
\vcenter{ \xymatrix{ R \ar[d]_t \ar[r]_f & R' \ar[d]^{t'} \\ U \ar[r]^f & U' } } \quad\text{and}\quad \vcenter{ \xymatrix{ R \ar[d]_s \ar[r]_f & R' \ar[d]^{s'} \\ U \ar[r]^f & U' } }
```
```tex
\vcenter{ \xymatrix{ R \ar[d]_t \ar[r]_f & R' \ar[d]^{t'} \\ U \ar[r]^f & U' } } \quad\text{et}\quad \vcenter{ \xymatrix{ R \ar[d]_s \ar[r]_f & R' \ar[d]^{s'} \\ U \ar[r]^f & U' } }
```

### `lemma-colimit-kappa`

Et relie les deux recouvrements sans confondre les ensembles d’indices I_ij et J_ij.

```tex
U_i \cap U_j = \bigcup\nolimits_{k \in I_{ij}} U_{ijk} \quad\text{and}\quad s^{-1}(U_i) \cap t^{-1}(U_j) = \bigcup\nolimits_{k \in J_{ij}} W_{ijk}.
```
```tex
U_i \cap U_j = \bigcup\nolimits_{k \in I_{ij}} U_{ijk} \quad\text{et}\quad s^{-1}(U_i) \cap t^{-1}(U_j) = \bigcup\nolimits_{k \in J_{ij}} W_{ijk}.
```

### `lemma-colimit-kappa`

Ou reste une alternative entre les deux développements, et n’est pas remplacé par et ; les coefficients a et b sont distingués.

```tex
m \otimes 1 = \sum\nolimits_{m' \in S(i, j, k, m)} m' \otimes a_{m'} \quad\text{or}\quad \alpha(m \otimes 1) = \sum\nolimits_{m' \in S(i, j, k, m)} m' \otimes b_{m'}
```
```tex
m \otimes 1 = \sum\nolimits_{m' \in S(i, j, k, m)} m' \otimes a_{m'} \quad\text{ou}\quad \alpha(m \otimes 1) = \sum\nolimits_{m' \in S(i, j, k, m)} m' \otimes b_{m'}
```

### `lemma-colimit-kappa`

Tel que porte sur la condition m appartient à S_i dans l’indice de la réunion.

```tex
S'_j = \bigcup\nolimits_{(i, j, k, m)\text{ such that }m \in S_i} S(i, j, k, m)
```
```tex
S'_j = \bigcup\nolimits_{(i, j, k, m)\text{ tel que }m \in S_i} S(i, j, k, m)
```

### `lemma-colimit-kappa`

Sous-module de M_i engendré par S_i à l’étape infinie conserve le module, l’anneau des scalaires et les générateurs.

```tex
N_i = A_i\text{-submodule of }M_i\text{ generated by }S^{(\infty)}_i
```
```tex
N_i = A_i\text{-sous-module de }M_i\text{ engendré par }S^{(\infty)}_i
```

### `lemma-colimit-kappa`

Et relie les deux compatibilités ; les bases A_i,A_j et les morphismes t,s dans les produits tensoriels restent distincts.

```tex
N_i \otimes_{A_i} A_{ijk} = N_j \otimes_{A_j} A_{ijk} \quad\text{and}\quad \alpha(N_i \otimes_{A_i, t} B_{ijk}) = N_j \otimes_{A_j, s} B_{ijk}
```
```tex
N_i \otimes_{A_i} A_{ijk} = N_j \otimes_{A_j} A_{ijk} \quad\text{et}\quad \alpha(N_i \otimes_{A_i, t} B_{ijk}) = N_j \otimes_{A_j, s} B_{ijk}
```

### `section-quotient-sheaves`

Ensembles rend le nom de catégorie Sets ; les deux foncteurs restent contravariants.

```tex
h_U, h_R : (\Sch/S)_\tau^{opp} \longrightarrow \textit{Sets}.
```
```tex
h_U, h_R : (\Sch/S)_\tau^{opp} \longrightarrow \textit{Ensembles}.
```

### `lemma-cartesian-equivalent-descent-datum`

La catégorie source est celle des schémas en groupoïdes cartésiens au-dessus du groupoïde indiqué ; le but est celle des données de descente relatives à X/Y. Le sens de la flèche ne change pas.

```tex
\begin{matrix} \text{category of groupoid schemes} \\ \text{cartesian over } (X, X \times_Y X, \ldots) \end{matrix} \longrightarrow \begin{matrix} \text{ category of descent data} \\ \text{ relative to } X/Y \end{matrix}
```
```tex
\begin{matrix} \text{catégorie des schémas en groupoïdes} \\ \text{cartésiens au-dessus de } (X, X \times_Y X, \ldots) \end{matrix} \longrightarrow \begin{matrix} \text{ catégorie des données de descente} \\ \text{ relatives à } X/Y \end{matrix}
```

## Limites

Chaque contexte modifié et chaque différence conservée ci-dessus a été lu dans les deux langues. Les contrôles sur tous les blocs étiquetés ne certifient pas l’intégralité de la prose ni de la terminologie. Les anomalies du témoin officiel restaurées ne sont pas présentées comme mathématiquement correctes. L’inversion des opérations reproduit exactement la version publique. La construction et la vérification publique du lecteur complet restent à effectuer.
