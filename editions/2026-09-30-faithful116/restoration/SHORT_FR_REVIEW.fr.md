# Lectures officielles et différences françaises conservées

**12 restaurations locales dans 3 chapitres ; 10 contextes supplémentaires comparés. Aucune édition complète n’est certifiée.**

[Restaurations et contextes complets](SHORT_FR_CONTEXTUAL_RESTORATIONS.json) · [Variantes conservées et limites](SHORT_FR_RETAINED_CONTEXTS.json) · [Contrôles](SHORT_FR_PARTIAL_VALIDATION.json)

[Chapitre 65 : LaTeX de travail](staged/fr/065_spaces.fr.tex)

[Chapitre 112 : LaTeX de travail](staged/fr/112_guide.fr.tex)

[Chapitre 111 : LaTeX de travail](staged/fr/111_exercises.fr.tex)

## FR-SPACES-FIDELITY-001

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L628)

La restriction porte littéralement l’indice U dans la source. U_i est l’amélioration attendue dans ce contexte, mais ne doit pas être incorporée à la traduction de référence.

Source :
```tex
to $\xi|_U$ via $b$.
```
Avant :
```tex
qui sont envoyés sur $\xi|_{U_i}$ par $b$.
```
Après :
```tex
qui sont envoyés sur $\xi|_U$ par $b$.
```

## FR-SPACES-FIDELITY-002

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L2660)

La première des trois cibles de ce passage est X dans la source, quoique le contexte utilise X prime. Les autres occurrences de X prime ne sont pas changées.

Source :
```tex
Then $\coprod_{i \in I} U'_i \to X$ is surjective
```
Avant :
```tex
Alors $\coprod_{i \in I} U'_i \to X'$ est
```
Après :
```tex
Alors $\coprod_{i \in I} U'_i \to X$ est
```

## FR-SPACES-FIDELITY-003

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L2661)

Deuxième cible restaurée dans la justification de surjectivité : X, non X prime. Cela préserve l’incohérence source au lieu de l’imputer à la traduction.

Source :
```tex
because of our assumption that $U \to X$ and hence
```
Avant :
```tex
en vertu de notre hypothèse selon laquelle $U \to X'$ et donc
```
Après :
```tex
en vertu de notre hypothèse selon laquelle $U \to X$ et donc
```

## FR-SPACES-FIDELITY-004

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L2661)

Troisième cible, dans la même phrase. Les trois opérations sont liées et ne comptent pas comme trois théorèmes distincts.

Source :
```tex
$\coprod U_i \to X$
```
Avant :
```tex
$\coprod U_i \to X'$
```
Après :
```tex
$\coprod U_i \to X$
```

## FR-SPACES-FIDELITY-005

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L2799)

La preuve porte Y prime, tandis que l’énoncé porte déjà X prime. L’énoncé exact n’est pas modifié ; seule la lecture source de la preuve est rétablie.

Source :
```tex
$X'_S = S \times_{S'} Y'$ by
```
Avant :
```tex
$X'_S = S \times_{S'} X'$ d'après
```
Après :
```tex
$X'_S = S \times_{S'} Y'$ d'après
```

## FR-GUIDE-FIDELITY-001

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/guide.tex#L669)

Le témoin nomme X le schéma portant l’action, malgré le quotient X prime/G écrit auparavant. X prime dans la traduction réparait cette discordance ; la distinction est rétablie sans approuver la coquille.

Source :
```tex
for a finite group $G$ acting a normal scheme $X$.
```
Avant :
```tex
d'un schéma normal $X'$ par l'action d'un groupe fini $G$.
```
Après :
```tex
d'un schéma normal $X$ par l'action d'un groupe fini $G$.
```

## FR-GUIDE-FIDELITY-002

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/guide.tex#L679)

La notice d’Edidin–Hassett–Kresch–Vistoli contient littéralement F, non le champ calligraphique X. La cible corrigée ne doit pas se substituer silencieusement à ce témoignage.

Source :
```tex
morphism $X \to F$ from a scheme $X$.
```
Avant :
```tex
$X \to \mathcal{X}$ provenant d'un schéma $X$.
\end{quote}
\item Kresch
```
Après :
```tex
$X \to F$ provenant d'un schéma $X$.
\end{quote}
\item Kresch
```

## FR-GUIDE-FIDELITY-003

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/guide.tex#L793)

La première occurrence du champ de Hilbert est paramétrée par F calligraphique dans la source. La traduction avait remplacé F par X ; cette proposition d’amélioration demeure dans l’avant/après, non dans la traduction fidèle.

Source :
```tex
defines the Hilbert stack $\mathcal{H}\text{ilb}(\mathcal{F} / S)$
```
Avant :
```tex
définit le champ de Hilbert $\mathcal{H}\text{ilb}(\mathcal{X} / S)$
```
Après :
```tex
définit le champ de Hilbert $\mathcal{H}\text{ilb}(\mathcal{F} / S)$
```

## FR-GUIDE-FIDELITY-004

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/guide.tex#L795)

Même discordance dans la seconde occurrence, au sein de l’assertion sans démonstration. Les deux occurrences restent liées ; aucune affirmation supplémentaire sur le résultat cité n’est ajoutée.

Source :
```tex
It is claimed without proof that $\mathcal{H}\text{ilb}(\mathcal{F} / S)$
```
Avant :
```tex
$\mathcal{H}\text{ilb}(\mathcal{X} / S)$ est un champ algébrique.
```
Après :
```tex
$\mathcal{H}\text{ilb}(\mathcal{F} / S)$ est un champ algébrique.
```

## FR-GUIDE-FIDELITY-005

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/guide.tex#L850)

Le témoin porte G majuscule alors que le morphisme vient d’être nommé g. Rétablir G rend visible la lecture originale ; ce n’est pas une nouvelle notion d’amplitude.

Source :
```tex
$G$-ample line bundle $L$
```
Avant :
```tex
propre $T$ muni d'un fibré en droites $g$-ample $L$
```
Après :
```tex
propre $T$ muni d'un fibré en droites $G$-ample $L$
```

## FR-EXERCISES-FIDELITY-001

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L133)

Le paragraphe suivant l’exercice exclut seulement zéro dans sa définition. La traduction avait ajouté l’exclusion de l’unité : c’est une correction éditoriale substantielle en prose, invisible au simple comptage des formules. Le rétablissement suit le témoin, sans défendre cette définition comme usuelle.

Source :
```tex
A {\it nontrivial idempotent} is an idempotent which is not
equal to zero.
```
Avant :
```tex
Un {\it idempotent non trivial} est un idempotent distinct de zéro et de l'unité.
```
Après :
```tex
Un {\it idempotent non trivial} est un idempotent distinct de zéro.
```

## FR-EXERCISES-FIDELITY-002

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L796)

Le nom R, incohérent avec A dans la phrase précédente, figure bien dans le témoin. La formule longueur_A(M) reste inchangée : la discordance n’est pas réparée silencieusement.

Source :
```tex
{\it length} of $M$ as an $R$-module is
```
Avant :
```tex
{\it longueur} de $M$ comme $A$-module est
```
Après :
```tex
{\it longueur} de $M$ comme $R$-module est
```

## Lecture conservée — spaces / `lemma-category-of-spaces-over-smaller-base-scheme`

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L2864)

Le tableau a été lu intégralement et avec sa preuve : les espaces sur S correspondent aux mêmes couples F prime sur S prime munis du même morphisme vers S. Le retour à la ligne et l’environnement gathered ne changent pas l’équivalence. Les fragments français doivent être lus ensemble, non comparés mot à mot.

```tex
\text{category of pairs }(F', F' \to S)\text{ consisting}
```
```tex
\text{catégorie des couples }(F', F' \to S)\text{ formés}
```

## Lecture conservée — spaces / `lemma-change-base-scheme`

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces.tex#L2785)

Conoyau est attesté pour une paire parallèle en catégorie non additive par Brameret–Enguehard–Renault, définition 5.3.1, p.27-22. Le quotient de la relation d’équivalence est donc bien exprimé dans le registre ancien. La suspicion initiale d’une confusion avec un conoyau additif est rejetée après lecture de la page originale ; aucun remplacement automatique par coégalisateur.

```tex
because $j_!$ being right exact commutes with coequalizers,
```
```tex
puisque $j_!$, étant exact à droite, commute aux conoyaux ;
```

[Attestation réellement consultée](SPACES_CH65_CONSULTED_CANON.json)

## Lecture conservée — spaces-divisors / `lemma-invertible-map-into-relative-proj`

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-divisors.tex#L2820)

Restrict est ici le nom descriptif d’une flèche de restriction, non un identifiant arbitraire. Restriction conserve les mêmes espaces de sections et le même sens de flèche. La preuve, les trois conditions et les objets ont été lus conjointement. Aucune restauration en anglais.

```tex
\ar[d]^{restrict}
```
```tex
\ar[d]^{restriction}
```

## Lecture conservée — stacks-sheaves / `definition-alternative-inherited-topologies`

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-sheaves.tex#L4471)

Les quatre allowbreak autorisent uniquement des coupures de ligne. Les cinq topologies, leur ordre et les indices associés sont conservés. Les noms anglais smooth et syntomic désignent ici les indices déjà définis avec des intitulés français, non une nouvelle traduction de la définition.

```tex
$\tau \in \{Zariski, \etale, smooth, syntomic, fppf\}$
```
```tex
$\tau \in \{Zariski,\allowbreak \etale,\allowbreak smooth,\allowbreak
syntomic,\allowbreak fppf\}$
```

## Lecture conservée — moduli-curves / `lemma-in-DM-locus-vector-fields`

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/moduli-curves.tex#L727)

La suppression de deux délimiteurs autour de 1 n’enlève aucune hypothèse : correspondent bijectivement rend exactement correspond one-to-one. La phrase source précédente est inachevée ; la version française dit seulement considérer les automorphismes, sans inventer la conclusion manquante. Ce défaut source reste signalé séparément.

```tex
The infinitesimal automorphisms of $X$ correspond $1$-to-$1$
with derivations
```
```tex
Les automorphismes infinitésimaux de $X$ correspondent bijectivement
aux dérivations
```

Points encore ouverts :

- La phrase anglaise it suffices to show any automorphism ne donne pas explicitement ce qu’il faut montrer ; aucune conclusion mathématique n’est ajoutée.

## Lecture conservée — moduli-curves / `lemma-stabilization-morphism`

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/moduli-curves.tex#L2981)

Il s’agit du nom descriptif français du même morphisme. Le domaine, le codomaine, les familles préstables et stables, ainsi que l’argument de changement de base restent identiques. Aucun changement de définition.

```tex
stabilization :
```
```tex
stabilisation :
```

## Lecture conservée — groupoids-quotients / `definition-orbit`

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids-quotients.tex#L437)

La virgule après le quantificateur est de la ponctuation française. La chaîne, ses bornes et les trois alternatives sont inchangées. Les deux connecteurs or encore anglais constituent un reliquat linguistique à corriger, pas une variante mathématique à rétablir.

```tex
\text{and for all }i \in \{0, \ldots, n - 1\}\text{ either }
```
```tex
\text{et, pour tout }i \in \{0, \ldots, n - 1\},\text{ soit }
```

Points encore ouverts :

- Deux occurrences de \text{ or } restent anglaises dans cette définition.
- Le titre hybride Groupoïdes in Espaces doit être harmonisé avec le titre français effectivement publié, sans modifier son renvoi.

## Lecture conservée — groupoids-quotients / `lemma-pre-equivalence-equivalence-relation-points`

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids-quotients.tex#L461)

Il existe traduit le quantificateur existentiel au lieu de le répéter par un symbole. Le quantificateur conserve sa portée sur r, s(r)=u et t(r)=u prime. La preuve par partition en orbites est inchangée.

```tex
\text{ such that } \exists r
```
```tex
\text{ tel qu'il existe } r
```

Points encore ouverts :

- Le même titre hybride Groupoïdes in Espaces reste à localiser.

## Lecture conservée — formal-spaces / `lemma-type-local`

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/formal-spaces.tex#L4472)

La seule propriété déjà traduite dans la liste désigne exactement la conjonction de dénombrabilité de l’indexation et de classicité. Les autres propriétés restent en anglais et ne sont pas déclarées pleinement localisées. Aucun objet ni aucune condition du lemme n’est changé.

```tex
countably\ indexed\ and\ classical
```
```tex
\text{à indexation dénombrable et classique}
```

Points encore ouverts :

- countably indexed, weakly adic, adic* et Noetherian restent en anglais dans le tableau ; localisation mathématique complète à reprendre avec des attestations pertinentes.

## Lecture conservée — exercises / `exercise-valuation`

[Témoin officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/exercises.tex#L124)

Le mot ou conserve la disjonction, la valeur zéro et l’inégalité stricte. Les hypothèses de l’exercice et ses cinq questions restent inchangées. Le changement de la définition voisine de l’idempotent non trivial est traité distinctement comme restauration.

```tex
\{f \mid f = 0, \ or\ \nu(f) > 0\}
```
```tex
\{f \mid f = 0, \ \text{ou}\ \nu(f) > 0\}
```

## Limites

Les opérations rétablissent des symboles ou retirent une précision éditoriale absente de la source ; elles n’imposent pas une traduction mot à mot. Les comparaisons conservées ont été lues dans leurs passages complets. L’attestation de conoyau est rétrospective et localisée ; aucune consultation initiale ou attestation des autres termes n’est inventée. Les propositions de correction de la source restent visibles dans l’avant/après. Le reste de la prose, les choix terminologiques non attestés, les reliquats anglais, les éditions complètes et leur publication restent à traiter.
