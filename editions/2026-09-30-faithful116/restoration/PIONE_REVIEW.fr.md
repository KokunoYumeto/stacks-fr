# Chapitre 58 — rétablissement de la source officielle

**Réparation locale partielle ; relecture intégrale, reconstruction et publication non achevées.**

Les corrections proposées de la source sont conservées séparément ci-dessous. La traduction de référence ne les incorpore pas silencieusement. Une restauration du témoin ne certifie pas la justesse mathématique de ce dernier.

[LaTeX de travail](staged/fr/058_pione.fr.tex) · [Contrôles](PIONE_PARTIAL_VALIDATION.json) · [Contextes complets](PIONE_CONTEXTUAL_RESTORATIONS.json)

## FR-PIONE-FIDELITY-001 — `lemma-tame`

[Source officielle, ligne 555](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L555)

Le témoin écrit I_2, non i_2. La minuscule est une correction plausible de la source, mais non une liberté de traduction ; elle reste documentée séparément.

Source :
```tex
$i \geq i_1$, $i \geq I_2$
```
Traduction publiée :
```tex
$i \geq i_1$, $i \geq i_2$
```
Lecture rétablie :
```tex
$i \geq i_1$, $i \geq I_2$
```

## FR-PIONE-FIDELITY-002 — `lemma-functoriality-galois-ses`

[Source officielle, ligne 814](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L814)

Rétablir l'ordre de composition de l'assertion (3). La preuve emploie H' composé avec H : cette tension appartient à la source et n'autorise pas à changer silencieusement son énoncé.

Source :
```tex
\item $H$ is fully faithful, $H \circ H'$
```
Traduction publiée :
```tex
\item $H$ est pleinement fidèle, $H' \circ H$
```
Lecture rétablie :
```tex
\item $H$ est pleinement fidèle, $H \circ H'$
```

## FR-PIONE-FIDELITY-003 — `lemma-functoriality-galois-injective`

[Source officielle, ligne 865](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L865)

Le diagramme de l'assertion porte H dans le témoin ; le prime ajouté est une proposition de correction, conservée hors du texte diplomatique.

Source :
```tex
X'' \leftarrow Y'' \rightarrow H(X')
```
Traduction publiée :
```tex
X'' \leftarrow Y'' \rightarrow H'(X')
```
Lecture rétablie :
```tex
X'' \leftarrow Y'' \rightarrow H(X')
```

## FR-PIONE-FIDELITY-004 — `lemma-functoriality-galois-injective`

[Source officielle, ligne 868](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L868)

Même restauration dans la phrase qui précise la flèche du diagramme, sans toucher aux autres occurrences de H'.

Source :
```tex
$Y'' \to H(X')$ is a monomorphism.
```
Traduction publiée :
```tex
$Y'' \to H'(X')$ est un monomorphisme.
```
Lecture rétablie :
```tex
$Y'' \to H(X')$ est un monomorphisme.
```

## FR-PIONE-FIDELITY-005 — `lemma-finite-etale-on-proper-over-henselian`

[Source officielle, ligne 1707](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L1707)

Le passage d'approximation de la source désigne V. Le remplacement par U_i clarifie peut-être le raisonnement, mais modifie un objet explicitement nommé ; rétablir V et conserver la proposition séparément.

Source :
```tex
The base change $U \to X$ of $V \to X_{A_i}$
```
Traduction publiée :
```tex
Le changement de base $U \to X$ de $U_i \to X_{A_i}$
```
Lecture rétablie :
```tex
Le changement de base $U \to X$ de $V \to X_{A_i}$
```

## FR-PIONE-FIDELITY-006 — `lemma-finite-etale-on-proper-over-henselian-pair`

[Source officielle, ligne 1839](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L1839)

Le passage d'approximation de la source désigne V. Le remplacement par U_i clarifie peut-être le raisonnement, mais modifie un objet explicitement nommé ; rétablir V et conserver la proposition séparément.

Source :
```tex
The base change $U \to X$ of $V \to X_{A_i}$
```
Traduction publiée :
```tex
Le changement de base $U \to X$ de $U_i \to X_{A_i}$
```
Lecture rétablie :
```tex
Le changement de base $U \to X$ de $V \to X_{A_i}$
```

## FR-PIONE-FIDELITY-007 — `lemma-finite-etale-on-proper-over-henselian-pair`

[Source officielle, ligne 1844](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L1844)

La parenthèse fermante ajoutée est une correction typographique du témoin. Elle est retirée de cette lecture diplomatique et reste repérable dans ce dossier, sans modifier les autres couples (A,I).

Source :
```tex
Fully faithfulness when $(A, I$ is a henselian pair
```
Traduction publiée :
```tex
Pleine fidélité lorsque $(A, I)$ est un couple hensélien
```
Lecture rétablie :
```tex
Pleine fidélité lorsque $(A, I$ est un couple hensélien
```

## FR-PIONE-FIDELITY-008 — `lemma-dense-faithful`

[Source officielle, ligne 1947](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L1947)

La base explicitement écrite est X. La traduction l'avait remplacée par Y : rétablir l'original sans prétendre que cette lecture est mathématiquement préférable.

Source :
```tex
and a morphism $s : X \to W$ over $X$
```
Traduction publiée :
```tex
et un morphisme $s : X \to W$ sur $Y$
```
Lecture rétablie :
```tex
et un morphisme $s : X \to W$ sur $X$
```

## FR-PIONE-FIDELITY-009 — `lemma-quasi-compact-dense-open-connected-at-infinity`

[Source officielle, ligne 2129](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L2129)

La source écrit W', tandis que la traduction a écrit W''. Cette correction du domaine de recollement ne doit pas être incorporée silencieusement.

Source :
```tex
that $\varphi$ and $\varphi''$ agree over $U \cap W'$.
```
Traduction publiée :
```tex
que $\varphi$ et $\varphi''$ coïncident sur $U \cap W''$.
```
Lecture rétablie :
```tex
que $\varphi$ et $\varphi''$ coïncident sur $U \cap W'$.
```

## FR-PIONE-FIDELITY-010 — `lemma-quasi-compact-dense-open-connected-at-infinity`

[Source officielle, ligne 2139](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L2139)

Maximum et borne supérieure ne sont pas la même assertion : le maximum appartient au sous-ensemble ordonné. La source emploie explicitement maximum. La preuve par Zorn n'autorise pas la substitution silencieuse par une borne supérieure. Choix lexical littéral motivé par ce passage ; aucune attestation historique de la traduction initiale n'est prétendue.

Source :
```tex
is a totally ordered subset, then it has a maximum $(U', \varphi')$.
```
Traduction publiée :
```tex
forment une chaîne, celle-ci admet une borne supérieure $(U', \varphi')$.
```
Lecture rétablie :
```tex
forment une chaîne, celle-ci admet un maximum $(U', \varphi')$.
```

## FR-PIONE-FIDELITY-011 — `lemma-inertia-invariants-etale`

[Source officielle, ligne 2670](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L2670)

Rétablir l'indice de l'identité du témoin, au lieu de son développement éditorial en corps résiduel. La conjonction française et est conservée.

Source :
```tex
\text{ and } \sigma \bmod \mathfrak q = \text{id}_\mathfrak q\}
```
Traduction publiée :
```tex
\text{ et } \sigma \bmod \mathfrak q = \text{id}_{\kappa(\mathfrak q)}\}
```
Lecture rétablie :
```tex
\text{ et } \sigma \bmod \mathfrak q = \text{id}_\mathfrak q\}
```

## FR-PIONE-FIDELITY-012 — `lemma-inertia-invariants-etale`

[Source officielle, ligne 2677](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L2677)

Deux objets ont été corrigés dans cette phrase : R a été changé en R^G et p en q. Rétablir ce passage exact, sans altérer les nombreux R^G et q que le témoin emploie effectivement ailleurs.

Source :
```tex
reduce to the case where $R \to R^I$ is a local isomorphism at
$R^I \cap \mathfrak p$.
```
Traduction publiée :
```tex
se ramener au cas où $R^G \to R^I$ est un isomorphisme local en
$R^I \cap \mathfrak q$.
```
Lecture rétablie :
```tex
se ramener au cas où $R \to R^I$ est un isomorphisme local en
$R^I \cap \mathfrak p$.
```

## FR-PIONE-FIDELITY-013 — `lemma-identify-inertia`

[Source officielle, ligne 2975](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L2975)

Dans le paragraphe suivant la preuve, la définition de I_y emploie D sans indice. Le remplacement par D_y est une correction éditoriale, non une traduction.

Source :
```tex
I_y = \{\sigma \in D \mid \sigma \bmod \mathfrak m_y =
```
Traduction publiée :
```tex
I_y = \{\sigma \in D_y \mid \sigma \bmod \mathfrak m_y =
```
Lecture rétablie :
```tex
I_y = \{\sigma \in D \mid \sigma \bmod \mathfrak m_y =
```

## FR-PIONE-FIDELITY-014 — `lemma-internal-hom-finite-etale`

[Source officielle, ligne 1088](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L1088)

La traduction avait substitué une référence de descente des morphismes étales à celle de la séparation. La référence publiée dans l'anglais officiel doit être conservée ; la proposition de remplacement reste dans ce dossier.

Source :
```tex
and \ref{descent-lemma-descending-property-separated}).
```
Traduction publiée :
```tex
et \ref{descent-lemma-descending-property-etale}).
```
Lecture rétablie :
```tex
et \ref{descent-lemma-descending-property-separated}).
```

## FR-PIONE-FIDELITY-015 — `lemma-structure-decomposition`

[Source officielle, ligne 3179](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L3179)

Retirer la définition ajoutée du corps résiduel : elle peut expliquer une notation de la source, mais le témoin ne la donne pas ici. L'ajout est conservé comme note éditoriale dans ce dossier.

Source :
```tex
Let $\mathfrak m$ be a maximal ideal of $B$.
```
Traduction publiée :
```tex
Soit $\mathfrak m$ un idéal maximal de $B$ et posons $\kappa_A = A/(\mathfrak m \cap A)$.
```
Lecture rétablie :
```tex
Soit $\mathfrak m$ un idéal maximal de $B$.
```

## FR-PIONE-FIDELITY-016 — `lemma-structure-decomposition`

[Source officielle, ligne 3197](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L3197)

La convention p = 1 en caractéristique nulle a été ajoutée par la traduction. La retirer du texte de référence ; l'utilité de cette précision ne lui confère pas le statut de texte officiel.

Source :
```tex
is zero,
\item there is a multiplicatively directed
```
Traduction publiée :
```tex
est nulle (avec la convention $p = 1$ dans ce dernier cas),
```
Lecture rétablie :
```tex
est nulle,
```

## FR-PIONE-FIDELITY-017 — `lemma-structure-decomposition`

[Source officielle, ligne 3215](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L3215)

Dans cette phrase de preuve, la source emploie κ, non κ_A. Les autres κ_A de l'énoncé et les κ ultérieurs sont laissés à leur place exacte.

Source :
```tex
The surjectivity of the map $D \to \text{Aut}(\kappa(\mathfrak m)/\kappa)$ is
```
Traduction publiée :
```tex
La surjectivité de l'application $D \to \text{Aut}(\kappa(\mathfrak m)/\kappa_A)$ est le
```
Lecture rétablie :
```tex
La surjectivité de l'application $D \to \text{Aut}(\kappa(\mathfrak m)/\kappa)$ est le
```

## FR-PIONE-FIDELITY-018 — `lemma-structure-decomposition-separable-closure`

[Source officielle, ligne 3372](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L3372)

Rétablir les deux κ_A et retirer la convention p = 1, absente de la source. Le remplacement par κ harmonisait silencieusement la notation de l'énoncé avec ses définitions.

Source :
```tex
$\kappa_A$ is $p > 1$ and $P = \{1\}$ if the characteristic of $\kappa_A$
is zero,
```
Traduction publiée :
```tex
$\kappa$ est $p > 1$, et $P = \{1\}$ si la caractéristique de $\kappa$
est nulle (avec la convention $p = 1$ dans ce dernier cas),
```
Lecture rétablie :
```tex
$\kappa_A$ est $p > 1$, et $P = \{1\}$ si la caractéristique de $\kappa_A$
est nulle,
```

## FR-PIONE-FIDELITY-019 — `lemma-specialization-map-discrete-valuation-ring`

[Source officielle, ligne 3918](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L3918)

Le coin inférieur droit est X_s dans le diagramme original ; le groupe fondamental avait été ajouté pour corriger son type. La correction proposée reste séparée.

Source :
```tex
\pi_1(X_{\overline{s}'}) \ar[r]^{sp} & X_{\overline{s}}
```
Traduction publiée :
```tex
\pi_1(X_{\overline{s}'}) \ar[r]^{sp} & \pi_1(X_{\overline{s}})
```
Lecture rétablie :
```tex
\pi_1(X_{\overline{s}'}) \ar[r]^{sp} & X_{\overline{s}}
```

## FR-PIONE-FIDELITY-020 — `lemma-restriction-equivalence`

[Source officielle, ligne 4053](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L4053)

La formule locale du témoin utilise f^{n+1}O_X, non I^n. Rétablir le quotient exactement écrit, même si son adaptation aux hypothèses paraît souhaitable.

Source :
```tex
$(\mathcal{O}_X/f^{n + 1}\mathcal{O}_X)^{\oplus r}$.
```
Traduction publiée :
```tex
$(\mathcal{O}_X/\mathcal{I}^n)^{\oplus r}$.
```
Lecture rétablie :
```tex
$(\mathcal{O}_X/f^{n + 1}\mathcal{O}_X)^{\oplus r}$.
```

## FR-PIONE-FIDELITY-021 — `lemma-restriction-equivalence-general`

[Source officielle, ligne 4225](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L4225)

La formule locale du témoin utilise f^{n+1}O_X, non I^n. Rétablir le quotient exactement écrit, même si son adaptation aux hypothèses paraît souhaitable.

Source :
```tex
$(\mathcal{O}_X/f^{n + 1}\mathcal{O}_X)^{\oplus r}$.
```
Traduction publiée :
```tex
$(\mathcal{O}_X/\mathcal{I}^n)^{\oplus r}$.
```
Lecture rétablie :
```tex
$(\mathcal{O}_X/f^{n + 1}\mathcal{O}_X)^{\oplus r}$.
```

## FR-PIONE-FIDELITY-022 — `lemma-restriction-faithful`

[Source officielle, ligne 4281](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L4281)

Le schéma dont on prend une composante a été modifié. Rétablir X, conformément à la phrase officielle, sans normaliser silencieusement l'argument.

Source :
```tex
applied to the restriction of $U \to X$ to a connected component of $X$.
```
Traduction publiée :
```tex
appliqué à la restriction de $U \to X$ à une composante connexe de $U$.
```
Lecture rétablie :
```tex
appliqué à la restriction de $U \to X$ à une composante connexe de $X$.
```

## FR-PIONE-FIDELITY-023 — `lemma-fill-in-missing`

[Source officielle, ligne 4498](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L4498)

Le témoin emploie n pour la borne des indices, malgré les t générateurs précédents. Rétablir n et garder l'harmonisation proposée dans le dossier.

Source :
```tex
For $1 \leq i, j \leq n$
```
Traduction publiée :
```tex
Pour $1 \leq i, j \leq t$
```
Lecture rétablie :
```tex
Pour $1 \leq i, j \leq n$
```

## FR-PIONE-FIDELITY-024 — `lemma-fill-in-missing`

[Source officielle, ligne 4501](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L4501)

Rétablir Y sans prime dans cette égalité particulière ; les Y' effectivement écrits dans la source sont préservés.

Source :
```tex
Write $Y' = \Spec(B')$. Since $V \times_U U' = Y \times_{X'} U'$
```
Traduction publiée :
```tex
Écrivons $Y' = \Spec(B')$. Comme $V \times_U U' = Y' \times_{X'} U'$
```
Lecture rétablie :
```tex
Écrivons $Y' = \Spec(B')$. Comme $V \times_U U' = Y \times_{X'} U'$
```

## FR-PIONE-FIDELITY-025 — `lemma-fully-faithful-henselian-completion`

[Source officielle, ligne 4542](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L4542)

La traduction avait rectifié le lieu de restriction. Rétablir V'_0, lecture du témoin, sans importer cette correction de type dans la traduction de référence.

Source :
```tex
whose restriction to $V'_0$ is the base change $s'_0$ of $s_0$.
```
Traduction publiée :
```tex
dont la restriction à $U'_0$ est le changement de base $s'_0$ de $s_0$.
```
Lecture rétablie :
```tex
dont la restriction à $V'_0$ est le changement de base $s'_0$ de $s_0$.
```

## FR-PIONE-FIDELITY-026 — `lemma-ramification-quasi-finite-flat`

[Source officielle, ligne 5034](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L5034)

Le mot anglais est target, non source. Rétablir « but », usage mathématique français attesté notamment dans Andreatta–Iovita–Pilloni, Le halo spectral, §3.2.2, p.614 (doi:10.24033/asens.2362), où source et but désignent les deux objets d'un morphisme. Cette attestation lexicale ne valide pas l'argument de Stacks.

Source :
```tex
locally on the base and on the
target (Descent, Lemmas
```
Traduction publiée :
```tex
sur la base et sur la
source (Descente, lemmes
```
Lecture rétablie :
```tex
sur la base et sur le
but (Descente, lemmes
```

## FR-PIONE-FIDELITY-027 — `lemma-ramification-quasi-finite-flat`

[Source officielle, ligne 5048](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L5048)

Le discriminant a été renommé D_f dans la traduction alors que le témoin écrit D_π. Rétablir chaque occurrence exacte, sans supprimer l'explication française.

Source :
```tex
closed subscheme $D_\pi \subset Y$
```
Traduction publiée :
```tex
sous-schéma fermé localement principal $D_f \subset Y$
```
Lecture rétablie :
```tex
sous-schéma fermé localement principal $D_\pi \subset Y$
```

## FR-PIONE-FIDELITY-028 — `lemma-ramification-quasi-finite-flat`

[Source officielle, ligne 5049](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L5049)

Le discriminant a été renommé D_f dans la traduction alors que le témoin écrit D_π. Rétablir chaque occurrence exacte, sans supprimer l'explication française.

Source :
```tex
such that $y' \in D_\pi$ if and only if
```
Traduction publiée :
```tex
tel que $y' \in D_f$ si et seulement s'il
```
Lecture rétablie :
```tex
tel que $y' \in D_\pi$ si et seulement s'il
```

## FR-PIONE-FIDELITY-029 — `lemma-ramification-quasi-finite-flat`

[Source officielle, ligne 5051](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L5051)

Le discriminant a été renommé D_f dans la traduction alors que le témoin écrit D_π. Rétablir chaque occurrence exacte, sans supprimer l'explication française.

Source :
```tex
that $y \not \in D_\pi$. Assume $y \in D_\pi$
```
Traduction publiée :
```tex
que $y \not \in D_f$. Supposons $y \in D_f$
```
Lecture rétablie :
```tex
que $y \not \in D_\pi$. Supposons $y \in D_\pi$
```

## FR-PIONE-FIDELITY-030 — `lemma-ramification-quasi-finite-flat`

[Source officielle, ligne 5058](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L5058)

Le discriminant a été renommé D_f dans la traduction alors que le témoin écrit D_π. Rétablir chaque occurrence exacte, sans supprimer l'explication française.

Source :
```tex
we can find $y' \in D_\pi$ specializing to $y$
```
Traduction publiée :
```tex
on peut trouver $y' \in D_f$ se spécialisant en $y$
```
Lecture rétablie :
```tex
on peut trouver $y' \in D_\pi$ se spécialisant en $y$
```

## FR-PIONE-FIDELITY-031 — `lemma-extend-S2`

[Source officielle, ligne 5238](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L5238)

L'assertion finale (b) du témoin écrit Y' ; retirer sa correction silencieuse en Y.

Source :
```tex
then there is a unique isomorphism $Y' \times_X U' = V'$ over $U'$.
```
Traduction publiée :
```tex
alors il existe un unique isomorphisme $Y \times_X U' = V'$ au-dessus de $U'$.
```
Lecture rétablie :
```tex
alors il existe un unique isomorphisme $Y' \times_X U' = V'$ au-dessus de $U'$.
```

## FR-PIONE-FIDELITY-032 — `lemma-extend-S2`

[Source officielle, ligne 5278](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L5278)

Le témoin dit que la profondeur serait 2, et non au moins 2. La traduction avait affaibli cette assertion afin de suivre l'hypothèse ; rétablir ce qui est écrit et garder la réparation proposée séparément.

Source :
```tex
would be $2$ a contradiction by
```
Traduction publiée :
```tex
serait au moins égale à $2$, ce qui contredirait le
```
Lecture rétablie :
```tex
serait égale à $2$, ce qui contredirait le
```

## FR-PIONE-FIDELITY-033 — `lemma-faithful-general`

[Source officielle, ligne 5398](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L5398)

Rétablir le U non primé effectivement écrit dans cette phrase de preuve.

Source :
```tex
Thus the displayed functor is faithful for a $U$ as in the statement
```
Traduction publiée :
```tex
Ainsi, le foncteur affiché est fidèle pour un $U'$ comme dans l'énoncé,
```
Lecture rétablie :
```tex
Ainsi, le foncteur affiché est fidèle pour un $U$ comme dans l'énoncé,
```

## FR-PIONE-FIDELITY-034 — `remark-combine`

[Source officielle, ligne 5542](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L5542)

La condition d'indexation U_0 ⊂ U a été remplacée par U_0 ⊂ U'. Rétablir l'indice de la source tout en gardant ouvert en français.

Source :
```tex
\colim\nolimits_{U' \subset U\text{ open, }U_0 \subset U}
```
Traduction publiée :
```tex
\colim\nolimits_{U' \subset U\text{ ouvert, }U_0 \subset U'}
```
Lecture rétablie :
```tex
\colim\nolimits_{U' \subset U\text{ ouvert, }U_0 \subset U}
```

## FR-PIONE-FIDELITY-035 — `lemma-equivalence-better`

[Source officielle, ligne 5596](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L5596)

Le but de ce premier morphisme est U dans la source ; les U' des lignes suivantes ne doivent pas entraîner son harmonisation silencieuse.

Source :
```tex
a finite \'etale morphism $V' \to U$ whose base change to $U_0$
```
Traduction publiée :
```tex
un morphisme fini étale $V' \to U'$ dont le changement de base à $U_0$
```
Lecture rétablie :
```tex
un morphisme fini étale $V' \to U$ dont le changement de base à $U_0$
```

## FR-PIONE-FIDELITY-036 — `lemma-purity-smooth-over-depth2`

[Source officielle, ligne 5942](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L5942)

Rétablir s dans le choix du voisinage, comme dans le témoin ; la substitution par z est une correction mathématique proposée.

Source :
```tex
$\Spec(B) \subset X$ of $s$. Then $A \to B$ is a smooth ring
```
Traduction publiée :
```tex
$\Spec(B) \subset X$ de $z$. Alors $A \to B$ est un morphisme lisse
```
Lecture rétablie :
```tex
$\Spec(B) \subset X$ de $s$. Alors $A \to B$ est un morphisme lisse
```

## FR-PIONE-FIDELITY-037 — `lemma-key-purity-ramification`

[Source officielle, ligne 6221](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L6221)

La définition explicite de Y a été ajoutée pour compléter la preuve. Rétablir l'énoncé sans cet ajout ; conserver la clarification proposée dans le dossier.

Source :
```tex
Let $f : X \to \Spec(A)$ be a finite type morphism.
```
Traduction publiée :
```tex
Posons $Y = \Spec(A)$ et soit $f : X \to Y$ un morphisme de type fini.
```
Lecture rétablie :
```tex
Soit $f : X \to \Spec(A)$ un morphisme de type fini.
```

## FR-PIONE-FIDELITY-038 — `lemma-key-purity-ramification`

[Source officielle, ligne 6295](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L6295)

Le membre droit a été remplacé par O_X pour corriger le type de l'égalité. Rétablir O_Y, lecture du témoin officiel.

Source :
```tex
Since $\omega_{X/Y} = \mathcal{O}_Y$ we see that
```
Traduction publiée :
```tex
Puisque $\omega_{X/Y} = \mathcal{O}_X$, on voit que
```
Lecture rétablie :
```tex
Puisque $\omega_{X/Y} = \mathcal{O}_Y$, on voit que
```

## FR-PIONE-FIDELITY-039 — `lemma-purity-ramification`

[Source officielle, ligne 6375](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L6375)

Rétablir le but Y écrit dans la source, au lieu de Y_0 substitué par la traduction.

Source :
```tex
morphism $X'_0 \to Y$ is \'etale at $x'$.
```
Traduction publiée :
```tex
morphisme $X'_0 \to Y_0$ est \'etale en $x'$.
```
Lecture rétablie :
```tex
morphisme $X'_0 \to Y$ est \'etale en $x'$.
```

## FR-PIONE-FIDELITY-040 — `theorem-global`

[Source officielle, ligne 6535](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L6535)

La parenthèse manquante du témoin avait été ajoutée. La restauration diplomatique distingue cette correction typographique de la source originale ; la proposition reste disponible séparément.

Source :
```tex
$V \cap (X \setminus f^{-1}(\{y\}) \to X \setminus f^{-1}(\{y\})$
```
Traduction publiée :
```tex
$V \cap (X \setminus f^{-1}(\{y\})) \to X \setminus f^{-1}(\{y\})$
```
Lecture rétablie :
```tex
$V \cap (X \setminus f^{-1}(\{y\}) \to X \setminus f^{-1}(\{y\})$
```

## FR-PIONE-FIDELITY-041 — `proposition-specialization-map-isomorphism`

[Source officielle, ligne 6729](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L6729)

Dans la dernière phrase de preuve, la source écrit B, non B'. Rétablir ce nom sans modifier les B' effectivement présents dans les étapes précédentes.

Source :
```tex
the pullback to $B$ is isomorphic to $Z'$).
```
Traduction publiée :
```tex
le changement de base à $B'$ est isomorphe à $Z'$).
```
Lecture rétablie :
```tex
le changement de base à $B$ est isomorphe à $Z'$).
```

## FR-PIONE-FIDELITY-042 — `proposition-specialization-map-isomorphism`

[Source officielle, ligne 6717](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L6717)

Le texte anglais écrit away from, alors que la traduction énonce en codimension 1. Cette différence de portée n'est pas résolue par la preuve : celle-ci motive sans doute une correction de la phrase anglaise, mais pas son importation silencieuse. Rendu provisoire volontairement littéral « hors de », à signaler à l'examen expert ; ne pas le lire comme une certification de l'assertion officielle.

Source :
```tex
is \'etale away from codimension $1$.
```
Traduction publiée :
```tex
est \'etale en codimension $1$.
```
Lecture rétablie :
```tex
est \'etale hors de la codimension $1$.
```

## FR-PIONE-FIDELITY-043 — `section-tame`

[Source officielle, ligne 6799](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L6799)

Retirer le nom f ajouté au premier morphisme : le texte officiel l'utilise ensuite sans le nommer ici. Une définition supplémentaire est une clarification éditoriale, non le texte original.

Source :
```tex
Let $X \to Y$ be a finite \'etale morphism
```
Traduction publiée :
```tex
Soit $f : X \to Y$ un morphisme fini \'etale
```
Lecture rétablie :
```tex
Soit $X \to Y$ un morphisme fini \'etale
```

## FR-PIONE-FIDELITY-044 — `lemma-pullback-tame-codim1`

[Source officielle, ligne 6842](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L6842)

Retirer le nom g ajouté pour distinguer les deux morphismes que la source désigne ensuite par f.

Source :
```tex
Let $X' \to X$ be a morphism
```
Traduction publiée :
```tex
Soit $g : X' \to X$ un morphisme
```
Lecture rétablie :
```tex
Soit $X' \to X$ un morphisme
```

## FR-PIONE-FIDELITY-045 — `lemma-pullback-tame-codim1`

[Source officielle, ligne 6845](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L6845)

Rétablir f dans l'image réciproque, au lieu du renommage éditorial en g.

Source :
```tex
\item $U' = f^{-1}(U)$ is dense open
```
Traduction publiée :
```tex
\item $U' = g^{-1}(U)$ soit un ouvert dense
```
Lecture rétablie :
```tex
\item $U' = f^{-1}(U)$ soit un ouvert dense
```

## FR-PIONE-FIDELITY-046 — `lemma-pullback-tame-codim1`

[Source officielle, ligne 6852](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L6852)

Rétablir f dans l'image du point générique ; le même nom ambigu figure dans le témoin.

Source :
```tex
then $\xi = f(\xi')$ is as in (2).
```
Traduction publiée :
```tex
alors $\xi = g(\xi')$ soit comme en (2).
```
Lecture rétablie :
```tex
alors $\xi = f(\xi')$ soit comme en (2).
```

## FR-PIONE-FIDELITY-047 — `lemma-abhyankar-one-divisor`

[Source officielle, ligne 6966](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L6966)

La traduction avait changé le but en X privé de D et ajouté une restriction à cet ouvert. L'énoncé officiel écrit Y vers X et une réunion disjointe, sans cette restriction. Rétablir l'assertion effectivement écrite ; sa correction mathématique éventuelle reste distincte de la traduction.

Source :
```tex
\'etale locally on $X$ the morphism $Y \to X$ is as given
as a finite disjoint union of standard tamely ramified
```
Traduction publiée :
```tex
localement pour la topologie \'etale sur $X$, le morphisme $Y \to X \setminus D$ est la restriction
à $X \setminus D$ d'une réunion disjointe finie de morphismes standard modérément ramifiés
```
Lecture rétablie :
```tex
localement pour la topologie \'etale sur $X$, le morphisme $Y \to X$ est donné
par une réunion disjointe finie de morphismes standard modérément ramifiés
```

## FR-PIONE-FIDELITY-048 — `lemma-abhyankar-one-divisor`

[Source officielle, ligne 6974](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L6974)

Même intervention éditoriale au début de la preuve : le produit fibré et son but avaient été restreints hors du diviseur. Rétablir Y ×_X U vers U et supprimer la restriction ajoutée, tout en conservant la proposition avant/après dans ce dossier.

Source :
```tex
$Y \times_X U \to U$ is a finite disjoint union of standard tamely ramified
```
Traduction publiée :
```tex
$Y \times_{X \setminus D} (U \setminus D) \to U \setminus D$ soit une réunion disjointe finie de restrictions de morphismes standard
```
Lecture rétablie :
```tex
$Y \times_X U \to U$ soit une réunion disjointe finie de morphismes standard
```

## FR-PIONE-FIDELITY-049 — `lemma-tame-covering-split`

[Source officielle, ligne 7179](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L7179)

La source écrit f dans cette phrase après avoir écrit π dans le diagramme précédent. Rétablir cette seule occurrence de f ; le π du diagramme est officiel et reste inchangé.

Source :
```tex
The rings $R'[x]/(x^{e_i} - f)$ are discrete valuation rings
```
Traduction publiée :
```tex
Les anneaux $R'[x]/(x^{e_i} - \pi)$ sont des anneaux de valuation discrète
```
Lecture rétablie :
```tex
Les anneaux $R'[x]/(x^{e_i} - f)$ sont des anneaux de valuation discrète
```

## FR-PIONE-FIDELITY-050 — `lemma-extend-covering`

[Source officielle, ligne 7222](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L7222)

Le témoin écrit σ(y), alors que la traduction avait remplacé y par s pour correspondre au point fermé nommé plus haut. Rétablir le symbole effectivement écrit.

Source :
```tex
neighbourhood of $\sigma(y)$.
```
Traduction publiée :
```tex
ouvert de $\sigma(s)$.
```
Lecture rétablie :
```tex
ouvert de $\sigma(y)$.
```

## FR-PIONE-FIDELITY-051 — `lemma-extend-covering`

[Source officielle, ligne 7251](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L7251)

Rétablir Y' dans ce recollement, sans substituer le Y que le contexte semble appeler.

Source :
```tex
whose restriction to $U$ recovers $Y' \to U$ and
```
Traduction publiée :
```tex
dont la restriction à $U$ redonne $Y \to U$ et
```
Lecture rétablie :
```tex
dont la restriction à $U$ redonne $Y' \to U$ et
```

## FR-PIONE-FIDELITY-052 — `lemma-extend-covering`

[Source officielle, ligne 7260](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L7260)

Rétablir U sans prime dans le but de ce morphisme ; la correction vers U' reste documentée, non incorporée.

Source :
```tex
assume $Y'' \to U \times_S X$ is finite \'etale, see
```
Traduction publiée :
```tex
supposer que $Y'' \to U' \times_S X$ est fini \'etale, voir
```
Lecture rétablie :
```tex
supposer que $Y'' \to U \times_S X$ est fini \'etale, voir
```

## FR-PIONE-FIDELITY-053 — `lemma-extend-covering`

[Source officielle, ligne 7285](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L7285)

La phrase officielle attribue l'action à Y, non Y'. Ce dossier conserve la correction proposée sans la faire passer pour une traduction littérale.

Source :
```tex
$G$-action on $Y$. Thus all that remains is to show that $Y'$
```
Traduction publiée :
```tex
de $G$ sur $Y'$. Il reste donc seulement à montrer que $Y'$
```
Lecture rétablie :
```tex
de $G$ sur $Y$. Il reste donc seulement à montrer que $Y'$
```

## FR-PIONE-FIDELITY-054 — `lemma-affine-etale-over-affine-space`

[Source officielle, ligne 7579](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L7579)

La traduction avait harmonisé le nom de l'invariant en NF. Le témoin emploie N à cet endroit ; rétablir N sans altérer les NF officiels des autres passages.

Source :
```tex
that $N(C, \varphi, \tau)$ is minimal.
```
Traduction publiée :
```tex
que $NF(C, \varphi, \tau)$ soit minimal.
```
Lecture rétablie :
```tex
que $N(C, \varphi, \tau)$ soit minimal.
```

## FR-PIONE-FIDELITY-055 — `lemma-affine-etale-over-affine-space`

[Source officielle, ligne 7580](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L7580)

Même restauration du nom N dans l'égalité à zéro, conformément au passage officiel.

Source :
```tex
we get $N(C, \varphi, \tau) = 0$.
```
Traduction publiée :
```tex
nous obtenons $NF(C, \varphi, \tau) = 0$.
```
Lecture rétablie :
```tex
nous obtenons $N(C, \varphi, \tau) = 0$.
```

## FR-PIONE-FIDELITY-056 — `lemma-dominate-affine-space`

[Source officielle, ligne 7608](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L7608)

La traduction avait harmonisé le nom de l'invariant en NF. Le témoin emploie N à cet endroit ; rétablir N sans altérer les NF officiels des autres passages.

Source :
```tex
that $N(C, \varphi, \tau)$ is minimal.
```
Traduction publiée :
```tex
que $NF(C, \varphi, \tau)$ soit minimal.
```
Lecture rétablie :
```tex
que $N(C, \varphi, \tau)$ soit minimal.
```

## FR-PIONE-FIDELITY-057 — `lemma-dominate-affine-space`

[Source officielle, ligne 7609](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L7609)

Même restauration du nom N dans l'égalité à zéro, conformément au passage officiel.

Source :
```tex
we get $N(C, \varphi, \tau) = 0$.
```
Traduction publiée :
```tex
nous obtenons $NF(C, \varphi, \tau) = 0$.
```
Lecture rétablie :
```tex
nous obtenons $N(C, \varphi, \tau) = 0$.
```

## FR-PIONE-FIDELITY-058 — `proposition-injective`

[Source officielle, ligne 7639](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L7639)

Rétablir Y dans l'identification affine donnée par la source. Le remplacement par Z corrige probablement l'argument, mais dépasse la traduction officielle.

Source :
```tex
Write $Y = \Spec(A)$ and $X = \Spec(R)$ so the closed immersion
```
Traduction publiée :
```tex
Écrivons $Z = \Spec(A)$ et $X = \Spec(R)$, de sorte que l'immersion fermée
```
Lecture rétablie :
```tex
Écrivons $Y = \Spec(A)$ et $X = \Spec(R)$, de sorte que l'immersion fermée
```

## FR-PIONE-FIDELITY-059 — `proposition-injective`

[Source officielle, ligne 7640](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L7640)

Rétablir Y dans le morphisme associé à cette surjection ; le schéma Z reste dans les autres positions où le témoin l'emploie.

Source :
```tex
$Y \to X$ is given by a surjection $R \to A$.
```
Traduction publiée :
```tex
$Z \to X$ soit donnée par une surjection $R \to A$.
```
Lecture rétablie :
```tex
$Y \to X$ soit donnée par une surjection $R \to A$.
```

## FR-PIONE-FIDELITY-060 — `proposition-injective`

[Source officielle, ligne 7675](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/pione.tex#L7675)

La source dit right, mais la traduction affirme gauche. Cette substitution du carré concerné modifie une assertion du raisonnement et ne se détecte pas dans les seules formules. Rétablir droite, avec la proposition de correction conservée séparément.

Source :
```tex
whose right square is cartesian.
```
Traduction publiée :
```tex
dont le carré de gauche est cartésien.
```
Lecture rétablie :
```tex
dont le carré de droite est cartésien.
```

## Différences équivalentes conservées

### `lemma-finite-etale-on-proper-over-henselian`

Appliquer la surjectivité essentielle au schéma U ×_X V traduit ici la substitution de paramètre écrite « applied to X = U ×_X V ». Ce n'est pas la suppression d'une égalité portant sur le X fixé : le rôle de schéma auquel on applique le résultat est explicitement conservé.

### `lemma-finite-etale-on-proper-over-henselian-pair`

Même substitution de paramètre : « au schéma U ×_X V » conserve le sens de l'application de la surjectivité essentielle. Les autres restaurations de ce bloc sont consignées séparément.

### `proposition-specialization-map-isomorphism`

La sous-extension finie séparable L/K de la clôture algébrique est une explicitation linguistique de la tour notée K̄/L/K, non une modification des corps ni de l'hypothèse. Les deux autres changements de ce bloc sont traités séparément.

### `theorem-specialization-map-isomorphism-prime-to-p`

L'occurrence supplémentaire de $p$ ne fait que mettre en mode mathématique le p de l'expression anglaise prime-to-p ; aucune hypothèse ou lettre nouvelle n'est ajoutée.

### `lemma-extend-covering`

Dans le passage « This is a normal integral scheme », le démonstratif vise V_0 : sa définition, son image dans σ(S) et son identification à σ(U) l'établissent dans les deux témoins. Le français nomme V_0 au lieu de répéter ce démonstratif. C'est une résolution d'anaphore, non une assertion supplémentaire. Les quatre autres différences de ce bloc sont restaurées séparément.

### `definition-G-set-continuous`

La seconde occurrence de G dans « If G is an abstract group G » est une répétition grammaticale supprimée en français. Le groupe abstrait, la topologie discrète et l'identification avec la définition précédente restent tous explicitement présents.

### `lemma-ses-field`

Spec{k'} et Spec(k') désignent le spectre du même corps ; les parenthèses sont notationnelles. L'indice σ ∈ Gal(k̄/k) sous la réunion reprend exactement la quantification qui introduit s^σ dans la phrase précédente. Aucun automorphisme, corps ou domaine d'indexation n'est ajouté au raisonnement.

### `lemma-reformulate-purity-normal`

Le tableau français place A devant algèbres, puis conserve finies, normales, la flèche Spec(B) vers X et son caractère étale au-dessus de U. L'application V vers Γ(V,O_V), l'équivalence et la condition finale sont inchangées. Le déplacement de A autour du texte traduit n'est pas une modification mathématique.

[Contextes des choix conservés](PIONE_RETAINED_CANDIDATES.json)

## Canon effectivement consulté

[Fabrizio Andreatta, Adrian Iovita, Vincent Pilloni — Le halo spectral](https://www.numdam.org/item/10.24033/asens.2362.pdf#page=14)

Annales scientifiques de l’École normale supérieure, série 4, tome 51 (2018), pp.603–655, DOI 10.24033/asens.2362
§3.2.2, p.614 imprimée, page 14 du PDF, avant la proposition 3.5.

Court passage : « La source et le but du morphisme ». 
Lecture effectivement consultée pour traduire target par but, dans le contexte de morphismes en géométrie arithmétique. Ne justifie ni une correction de la source Stacks, ni le reste de la terminologie du chapitre.

## Limites

Dossier produit par IA, sans examen expert humain. Les preuves ici sont les témoins officiels et français cités, non une attestation inventée de consultation du canon lors de la traduction initiale. Les identifiants producteurs restent à rapprocher ; les autres différences et la terminologie complète restent à examiner. Aucune publication corrigée n'est revendiquée.
