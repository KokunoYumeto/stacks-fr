# Chapitre 115 — différences conservées après comparaison

**Contrôle limité des candidats mathématiques, non certification de toute la prose ou du registre.**

Les 29 restaurations figurent dans le [dossier avant/après](OBSOLETE_REVIEW.fr.md).
[Contextes complets](OBSOLETE_FORMULA_RETAINED_CANDIDATES.json) · [Contrôles](OBSOLETE_CANDIDATE_RECONCILIATION.json)

## `lemma-bound-primes`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L402)

La virgule après la flèche c et le point final du calcul sont de la ponctuation française, non de nouveaux termes mathématiques. Ils sont conservés indépendamment des indices et de la parenthèse rétablis.

Source :
```tex
c : A/(f + g) \longrightarrow \prod A/\mathfrak q_j^{(m_j)}
M & = \text{length}_A(A/(f + g, h) \\ & = e_A(A/(f + g), 0, h) \\ & = \sum\nolimits_i e_A(A/\mathfrak q_j^{(m_j)}, 0, h) \\ & = \sum\nolimits_i \sum\nolimits_{m = 0, \ldots, m_j - 1} e_A(\mathfrak q_j^{(m)}/\mathfrak q_j^{(m + 1)}, 0, h)
```

Traduction conservée :
```tex
c : A/(f + g) \longrightarrow \prod A/\mathfrak q_j^{(m_j)},
M & = \text{length}_A(A/(f + g, h) \\ & = e_A(A/(f + g), 0, h) \\ & = \sum\nolimits_i e_A(A/\mathfrak q_j^{(m_j)}, 0, h) \\ & = \sum\nolimits_i \sum\nolimits_{m = 0, \ldots, m_j - 1} e_A(\mathfrak q_j^{(m)}/\mathfrak q_j^{(m + 1)}, 0, h).
```

## `lemma-directed-colimit-finite-type`

[Source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/obsolete.tex#L4440)

« Soit X un schéma quasi-compact et quasi-séparé » réunit les deux phrases officielles sans perdre d’hypothèse. L’occurrence répétée de X n’a pas à être reproduite artificiellement.

Source :
```tex
X
```

Traduction conservée :
```tex

```

## Texte des formules

Les [12 paires alignées](OBSOLETE_READER_TEXT_CANDIDATES.json) ont été lues. Les règles ci-dessous expliquent leur conservation ; aucune attestation terminologique externe n’est inventée.

- « and » → « et » : Même conjonction : soit les deux annulations, soit les deux foncteurs, sans modification des objets ni des flèches.
- « if » → « si » : Les cas, degrés et valeurs du tableau cohomologique sont identiques.
- « in » → « dans » : La même suite de flèches appartient à la catégorie X calligraphique.
- « lying over » → « , au-dessus de » : La même suite est projetée sur les mêmes ouverts ; la virgule relève de la syntaxe française.
- « restriction of » → « restriction de » : Il s’agit de la restriction de la flèche x vers x indice n, non d’une nouvelle flèche.
- « irred.\ comp. with » → « comp.\ irr.\ avec » : Même ensemble de composantes irréductibles W avec la dimension prescrite ; ordre français du nom et de l’adjectif.
- « Sets » → « Ens » : Nom abrégé de la même catégorie des ensembles, cible du foncteur.
- « monomorphism » → « monomorphisme » : Même condition sur le morphisme Spec(k) vers X ; aucune condition de point n’est ajoutée.
- « -Sets » → « -Ens » : La catégorie reste celle des G-ensembles ; G et le tiret de la notation sont conservés.
- « length » → « longueur » : Même longueur de module sur R et même différence ordonnée des deux longueurs.

Les notations stables Bad et Good restent celles du témoin. Les mots français préexistants sont conservés pour ces occurrences seulement. La prose hors de ces passages, la terminologie complète, la reconstruction et la vérification publique des éditions restent à faire. Analyse assistée par IA, sans relecture experte humaine.
