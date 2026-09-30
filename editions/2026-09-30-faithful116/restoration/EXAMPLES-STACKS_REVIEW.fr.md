# Exemples de champs : différences fidèles conservées

**LaTeX local ; aucune édition publique corrigée à ce stade.**

[LaTeX](staged/fr/095_examples-stacks.fr.tex) · [Contrôles](EXAMPLES-STACKS_FR_VALIDATION.json) · [Contextes complets](EXAMPLES-STACKS_FR_REPAIRS.json)

Les cinq contextes candidats ont été lus intégralement dans les deux langues. Aucune opération de correction n’est justifiée par ces différences. La copie de travail conserve chaque octet du témoin public, y compris ses fins de ligne mixtes. Ce contrôle ne certifie pas toute la prose du chapitre.

## Différences fidèles conservées

### `lemma-quasi-coherent-strongly-cartesian`

La virgule finale du calcul est une ponctuation de phrase. Les deux implications, le relèvement canonique et son unicité à isomorphisme près restent identiques ; aucun argument mathématique n’est ajouté.

### `lemma-finite-type`

Le point final après la somme directe ne change pas le faisceau. Recouvrement ouvert avec un ensemble d’indices I=X restitue grammaticalement la phrase anglaise défectueuse sans ajouter d’hypothèse. La condition au plus r(i) et le raisonnement par les noyaux sont conservés.

### `lemma-spaces-strongly-cartesian`

La virgule finale et le nom français Espaces de la catégorie ne modifient pas le produit fibré. Les deux sens du critère fortement cartésien et leurs justifications sont préservés.

### `proposition-equal-quotient-stacks`

Les différences de formules sont le nom Groupoïdes et six signes de ponctuation terminant des phrases ou des lignes de calcul. Les actions, inverses, buts et bases ont été lus dans les deux preuves complètes. La pleine fidélité puis la surjectivité essentielle locale sont conservées. Ceci n’est pas une attestation externe de toute la terminologie du chapitre.

### `example-inertia-stack-of-picard`

Le point retiré après l’égalité finale permet à la phrase française de continuer. La condition d’isomorphisme, son caractère plus fort et les unités globales sont inchangés. Le placeholder officiel reste visible en français : insérer ici une référence ultérieure. Il n’est ni supprimé ni remplacé par une référence inventée.

## Texte des formules vérifié

### `lemma-finite-type`

Ouvert qualifie U dans l’indice du produit ; la condition U inclus dans X et le faisceau H(U) sont inchangés.

```tex
\prod_{U \subset X\text{ open}} \mathcal{H}(U)
```
```tex
\prod_{U \subset X\text{ ouvert}} \mathcal{H}(U)
```

### `section-stack-of-spaces`

Le nom de catégorie Spaces est traduit par Espaces. Les objets, bases et foncteurs de la paire entière restent identiques.

```tex
\textit{Spaces}/U
```
```tex
\textit{Espaces}/U
```

### `lemma-pre-stack-of-spaces`

Le nom de catégorie Spaces est traduit par Espaces. Les objets, bases et foncteurs de la paire entière restent identiques.

```tex
\textit{Spaces}/U_i
```
```tex
\textit{Espaces}/U_i
```

### `section-stack-associated-to-sheaf`

Sets devient Ensembles dans le but du foncteur. L’opposition de la catégorie source et la topologie fppf sont conservées.

```tex
F : (\Sch/S)_{fppf}^{opp} \to \textit{Sets}
```
```tex
F : (\Sch/S)_{fppf}^{opp} \to \textit{Ensembles}
```

### `subsection-variant-principal-homogeneous-spaces`

Le suffixe Schemes devient Schémas dans le nom de la sous-catégorie. L’indice G, le nom principal/torseur et, lorsqu’il figure, le sens de l’inclusion sont inchangés. Les noms conventionnels de ces catégories sont distingués de la prose.

```tex
G\textit{-Principal-Schemes} \subset G\textit{-Principal}
```
```tex
G\textit{-Principal-Schémas} \subset G\textit{-Principal}
```

### `subsection-variant-principal-homogeneous-spaces`

Le suffixe Schemes devient Schémas dans le nom de la sous-catégorie. L’indice G, le nom principal/torseur et, lorsqu’il figure, le sens de l’inclusion sont inchangés. Les noms conventionnels de ces catégories sont distingués de la prose.

```tex
G\textit{-Principal-Schemes}
```
```tex
G\textit{-Principal-Schémas}
```

### `subsection-variant-fppf-torsors`

Le suffixe Schemes devient Schémas dans le nom de la sous-catégorie. L’indice G, le nom principal/torseur et, lorsqu’il figure, le sens de l’inclusion sont inchangés. Les noms conventionnels de ces catégories sont distingués de la prose.

```tex
G\textit{-Torsors-Schemes} \subset G\textit{-Torsors}
```
```tex
G\textit{-Torsors-Schémas} \subset G\textit{-Torsors}
```

### `subsection-variant-fppf-torsors`

Le suffixe Schemes devient Schémas dans le nom de la sous-catégorie. L’indice G, le nom principal/torseur et, lorsqu’il figure, le sens de l’inclusion sont inchangés. Les noms conventionnels de ces catégories sont distingués de la prose.

```tex
G\textit{-Torsors-Schemes}
```
```tex
G\textit{-Torsors-Schémas}
```

## Limites

Chaque contexte modifié et chaque différence conservée ci-dessus a été lu dans les deux langues. Les contrôles sur tous les blocs étiquetés ne certifient pas l’intégralité de la prose ni de la terminologie. Les anomalies du témoin officiel restaurées ne sont pas présentées comme mathématiquement correctes. L’inversion des opérations reproduit exactement la version publique. La construction et la vérification publique du lecteur complet restent à effectuer.
