# Dernières différences françaises conservées

Les sept fichiers ci-dessous complètent le classement des candidats mathématiques signalés par l’inventaire existant. Leurs huit sections candidates ne révèlent pas de modification éditoriale à annuler. Les fichiers français restent strictement identiques à leurs témoins publics. Cette comparaison ciblée ne prétend pas certifier chaque phrase ou chaque choix terminologique.

[Contrôles et passages](FINAL_FR_CANDIDATE_CLOSURE.json) · [Procédure actuelle](ACTIVE_FRENCH_RESTORATION_SCOPE.json)

## resolve

Les mots something et unit sont des indications verbales de coefficients, non des variables nommées. Le français les traduit par un élément et une unité, dans des commandes textuelles. Les coefficients restent non spécifiés ; les facteurs, le signe moins, le carré et la condition d’unité ne changent pas.

[Témoin français](https://raw.githubusercontent.com/KokunoYumeto/stacks-fr/0d1d1ef4d7b31c1c82a3471aedc42b99303369d4/editions/2026-09-21-complete116/chapters/054_resolve.fr.tex) · [Copie conservée](public-sources/fr/resolve.tex)

[Section officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/resolve.tex#L3061)

Anglais :
```tex
y_3^2 - x_1((something)x_1 + (something)y_3 + (unit)g)
```

Français conservé :
```tex
y_3^2 - x_1((\text{un élément})x_1 + (\text{un élément})y_3 + (\text{une unité})g)
```

## equiv

Le nom anglais $5$-lemma devient lemme des cinq dans la même phrase, avec le même renvoi à homology-lemma-five-lemma. Le nombre n’est pas supprimé du raisonnement : il est écrit en toutes lettres dans le nom français du résultat.

[Témoin français](https://raw.githubusercontent.com/KokunoYumeto/stacks-fr/0d1d1ef4d7b31c1c82a3471aedc42b99303369d4/editions/2026-09-21-complete116/chapters/057_equiv.fr.tex) · [Copie conservée](public-sources/fr/equiv.tex)

[Section officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/equiv.tex#L1966)

Anglais :
```tex
$5$-lemma
```

Français conservé :
```tex
le lemme des cinq
```

## spaces-divisors

Seul le libellé anglais restrict de la flèche verticale devient restriction. Son sens, son origine, son but, les sections globales, les deux flèches psi et la flèche theta sont identiques.

[Témoin français](https://raw.githubusercontent.com/KokunoYumeto/stacks-fr/0d1d1ef4d7b31c1c82a3471aedc42b99303369d4/editions/2026-09-21-complete116/chapters/071_spaces-divisors.fr.tex) · [Copie conservée](public-sources/fr/spaces-divisors.tex)

[Section officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-divisors.tex#L2771)

Anglais :
```tex
\xymatrix{ \mathcal{A}_d(V) \ar[d]_{\psi} \ar[r]_{\psi} & \Gamma(V \times_Y X, \mathcal{L}^{\otimes d}) \ar[d]^{restrict} \\ \Gamma(V \times_Y \underline{\text{Proj}}_Y(\mathcal{A}), \mathcal{O}_{\underline{\text{Proj}}_Y(\mathcal{A})}(d)) \ar[r]^-\theta & \Gamma(V \times_Y U(\psi), \mathcal{L}^{\otimes d}) }
```

Français conservé :
```tex
\xymatrix{ \mathcal{A}_d(V) \ar[d]_{\psi} \ar[r]_{\psi} & \Gamma(V \times_Y X, \mathcal{L}^{\otimes d}) \ar[d]^{restriction} \\ \Gamma(V \times_Y \underline{\text{Proj}}_Y(\mathcal{A}), \mathcal{O}_{\underline{\text{Proj}}_Y(\mathcal{A})}(d)) \ar[r]^-\theta & \Gamma(V \times_Y U(\psi), \mathcal{L}^{\otimes d}) }
```

## groupoids-quotients

Dans les deux descriptions de l’orbite, les expressions verbales tels que, et, pour tout et tel qu’il existe traduisent les connecteurs et le quantificateur imprimés. Les indices, les extrémités, les alternatives et le sens des flèches restent identiques. Deux occurrences du mot anglais or restent non traduites dans la matrice ; cela constitue une limite linguistique visible, pas une correction du contenu officiel.

[Témoin français](https://raw.githubusercontent.com/KokunoYumeto/stacks-fr/0d1d1ef4d7b31c1c82a3471aedc42b99303369d4/editions/2026-09-21-complete116/chapters/083_groupoids-quotients.fr.tex) · [Copie conservée](public-sources/fr/groupoids-quotients.tex)

[Section officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids-quotients.tex#L414)

Anglais :
```tex
O_u = \left\{ u' \in |U|\ : \begin{matrix} \exists n \geq 1, \ \exists u_0, \ldots, u_n \in |U|\text{ such that } u_0 = u \text{ and } u_n = u' \\ \text{and for all }i \in \{0, \ldots, n - 1\}\text{ either } u_i = u_{i + 1}\text{ or } \\ \exists r \in |R|, \ s(r) = u_i, t(r) = u_{i + 1} \text{ or } \\ \exists r \in |R|, \ t(r) = u_i, s(r) = u_{i + 1} \end{matrix} \right\}
```

Français conservé :
```tex
O_u = \left\{ u' \in |U|\ : \begin{matrix} \exists n \geq 1, \ \exists u_0, \ldots, u_n \in |U|\text{ tels que } u_0 = u \text{ et } u_n = u' \\ \text{et, pour tout }i \in \{0, \ldots, n - 1\},\text{ soit } u_i = u_{i + 1}\text{ or } \\ \exists r \in |R|, \ s(r) = u_i, t(r) = u_{i + 1} \text{ or } \\ \exists r \in |R|, \ t(r) = u_i, s(r) = u_{i + 1} \end{matrix} \right\}
```

[Section officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/groupoids-quotients.tex#L414)

Anglais :
```tex
O_u = \{u' \in |U| \text{ such that } \exists r \in |R|, \ s(r) = u, \ t(r) = u'\}.
```

Français conservé :
```tex
O_u = \{u' \in |U| \text{ tel qu'il existe } r \in |R|, \ s(r) = u, \ t(r) = u'\}.
```

## formal-spaces

La propriété countably indexed and classical devient à indexation dénombrable et classique dans la deuxième ligne de la même liste. Les quatre autres propriétés et les deux conditions équivalentes ne sont pas remplacées. Plusieurs noms anglais restent dans la formule : il s’agit d’une localisation incomplète, pas d’une modification mathématique.

[Témoin français](https://raw.githubusercontent.com/KokunoYumeto/stacks-fr/0d1d1ef4d7b31c1c82a3471aedc42b99303369d4/editions/2026-09-21-complete116/chapters/087_formal-spaces.fr.tex) · [Copie conservée](public-sources/fr/formal-spaces.tex)

[Section officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/formal-spaces.tex#L4314)

Anglais :
```tex
P \in \left\{ \begin{matrix} countably\ indexed,\\ countably\ indexed\ and\ classical,\\ weakly\ adic,\ adic*,\ Noetherian \end{matrix} \right\}
```

Français conservé :
```tex
P \in \left\{ \begin{matrix} countably\ indexed,\\ \text{à indexation dénombrable et classique},\\ weakly\ adic,\ adic*,\ Noetherian \end{matrix} \right\}
```

## stacks-sheaves

Les quatre commandes allowbreak ajoutent seulement des possibilités de coupure après les virgules de la liste des topologies. Aucun membre n’est ajouté ou retiré et les mêmes identifiants restent utilisés dans les indices des sites.

[Témoin français](https://raw.githubusercontent.com/KokunoYumeto/stacks-fr/0d1d1ef4d7b31c1c82a3471aedc42b99303369d4/editions/2026-09-21-complete116/chapters/096_stacks-sheaves.fr.tex) · [Copie conservée](public-sources/fr/stacks-sheaves.tex)

[Section officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/stacks-sheaves.tex#L4411)

Anglais :
```tex
\tau \in \{Zariski, \etale, smooth, syntomic, fppf\}
```

Français conservé :
```tex
\tau \in \{Zariski,\allowbreak \etale,\allowbreak smooth,\allowbreak syntomic,\allowbreak fppf\}
```

## moduli-curves

La correspondance $1$-to-$1$ est exprimée par correspondent bijectivement, dans la même phrase sur les automorphismes infinitésimaux et les dérivations. Les deux chiffres ne sont pas deux hypothèses omises. Dans l’autre passage, stabilization devient stabilisation ; le genre, la source et le but du morphisme restent identiques.

[Témoin français](https://raw.githubusercontent.com/KokunoYumeto/stacks-fr/0d1d1ef4d7b31c1c82a3471aedc42b99303369d4/editions/2026-09-21-complete116/chapters/109_moduli-curves.fr.tex) · [Copie conservée](public-sources/fr/moduli-curves.tex)

[Section officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/moduli-curves.tex#L545)

Anglais :
```tex
correspond $1$-to-$1$
```

Français conservé :
```tex
correspondent bijectivement
```

[Section officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/moduli-curves.tex#L2626)

Anglais :
```tex
stabilization : \Curvesstack^{prestable}_g \longrightarrow \overline{\mathcal{M}}_g
```

Français conservé :
```tex
stabilisation : \Curvesstack^{prestable}_g \longrightarrow \overline{\mathcal{M}}_g
```
