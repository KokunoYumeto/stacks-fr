# Chapitre 11 — lectures officielles rétablies

Copie de travail non reconstruite et non publiée. Sept opérations de contenu rétablies, dont une réécriture de preuve ; quatre choix grammaticaux conservés. Les propositions ne sont pas déclarées fausses : elles restent séparées de la traduction de référence.

## BRAUER-002

[Source officielle, ligne 275](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L275) · `lemma-matrix-algebras`.

Avant :
```tex
$J = \bigoplus_{i,j} e_{ii}Je_{jj}$, et les ensembles de coefficients de tous les
termes $e_{ii}Je_{jj}$ coïncident et constituent un idéal bilatère $I$ de $R$.
Cela prouve (2).
```

Lecture rétablie :
```tex
$J = \bigoplus e_{ii}Je_{jj}$, et tous les termes $e_{ii}Je_{jj}$ sont
égaux entre eux et constituent un idéal bilatère $I$ de $R$. Cela prouve (2).
```

Rétablir non seulement la somme non indexée, mais aussi l'assertion source selon laquelle les termes sont égaux : la substitution des ensembles de coefficients réécrivait la preuve.

## BRAUER-003

[Source officielle, ligne 63](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L63) · `definition-simple`.

Avant :
```tex
Nous disons que $A$ est {\it simple} si elle est non nulle et si les seuls
```

Lecture rétablie :
```tex
Nous disons que $A$ est {\it simple} si les seuls
```

Retirer l'hypothèse non nulle ajoutée à l'algèbre. Conserver l'hypothèse non nulle du module dans la phrase précédente : celle-ci figure dans l'original.

## BRAUER-004

[Source officielle, ligne 295](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L295) · `lemma-simple-module-unique`.

Avant :
```tex
\item Pour tout $A$-module non nul $N$ de dimension finie,
```

Lecture rétablie :
```tex
\item Pour tout $A$-module $N$ de dimension finie,
```

Retirer la restriction non nulle absente de l'énoncé officiel.

## BRAUER-005A, BRAUER-005B

[Source officielle, ligne 512](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L512) · `lemma-automorphism-inner`.

Avant :
```tex
Tout automorphisme de la
$k$-algèbre $A$ est intérieur. En particulier, tout automorphisme de la
$k$-algèbre $\text{Mat}(n \times n, k)$
```

Lecture rétablie :
```tex
Tout automorphisme de $A$ est
intérieur. En particulier, tout automorphisme de $\text{Mat}(n \times n, k)$
```

Retirer les deux précisions ajoutées sur les automorphismes de k-algèbres, sans changer l'hypothèse initiale sur A.

## BRAUER-006

[Source officielle, ligne 570](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L570) · `lemma-when-tensor-is-equal`.

Avant :
```tex
$A \cong B \otimes_k C$
```

Lecture rétablie :
```tex
$A = B \otimes_k C$
```

Rétablir le signe égal employé par l'auteur ; ne pas le remplacer par un signe d'isomorphisme, même si cette lecture paraît plus précise.

## BRAUER-007

[Source officielle, ligne 733](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/brauer.tex#L733) · `proposition-separable-splitting-field`.

Avant :
```tex
supposons qu'aucun élément de $K \setminus k$ ne soit séparable sur $k$.
```

Lecture rétablie :
```tex
supposons qu'aucun élément de $K$ ne soit séparable sur $k$.
```

Rétablir le domaine K du quantificateur officiel ; conserver l'objection mathématique dans les errata séparés.

## Choix grammaticaux conservés

- BRAUER-001 : Coquille anglaise spitting/splitting : le français corps neutralisant garde le sens du titre et de l'énoncé.
- BRAUER-008 : Construction causale grammaticalement française ; même implication (2) vers (3).
- BRAUER-009 : Ponctuation française sans modification de la condition de finitude.
- BRAUER-010 : Article requis par la grammaire française ; mêmes propriétés de l'algèbre.

## Texte dans les formules

La seule différence textuelle (région 122) a été vérifiée : « for all » devient « pour tout ». Le quantificateur universel et les variables sont conservés.

Source :
```tex
C = \{y \in A \mid xy = yx \text{ for all }x \in B\}.
```
Traduction conservée :
```tex
C = \{y \in A \mid xy = yx \text{ pour tout }x \in B\}.
```

