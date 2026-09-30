# Chapitre 9 — Corps : trace, norme et théorie de Galois

**Deux sections complètes comparées : lignes anglaises 2359–2851, françaises 2359–2847. Aucun nouveau changement du texte. La lecture continue atteint vingt et une sections ; le chapitre et l’édition ne sont pas encore entièrement vérifiés.**

[LaTeX de travail](staged/fr/009_fields.prose-batch4.fr.tex) · [Validation](FIELDS_PROSE_BATCH5_VALIDATION.json) · [Choix et paires](FIELDS_PROSE_BATCH5_CHOICES.json) · [Occurrences](FIELDS_PROSE_BATCH5_OCCURRENCES.json) · [Lot précédent](FIELDS_PROSE_BATCH4_REVIEW.fr.md)

## Ce qui a effectivement été lu

Toutes les définitions, assertions, preuves, l'exercice, les transitions et les titres des deux sections ont été comparés. Vingt paires disjointes, découpées aux identifiants stables, couvrent exactement le périmètre, sans intervalle omis. Le découpage technique peut rattacher un début d'environnement ou de titre à la paire précédente ; la lecture est continue.

Les 305 régions mathématiques de chaque langue ne sont pas brutes-identiques : cinq expressions contiennent du texte lecteur traduit. Les substitutions exactes ci-dessous donnent une égalité ordonnée, sans modifier les formules. Le préfixe complet compte 2 061 régions anglaises et 2 062 françaises ; la différence de compte et les quatre autres exceptions sont déjà justifiées dans les lots précédents.

Le fichier français reste strictement identique au lot 4. Le retour inverse de son unique réparation grammaticale, de la restauration de la liste des noms au lot 1 et des 19 opérations historiques reproduit exactement le témoin public préservé. Les réserves sur la source ne sont pas corrigées dans la traduction.

## Canon réellement consulté

Marc Reversat et Benoît Zhang, [Cours de théorie des corps](https://www.math.univ-toulouse.fr/~reversat/galois.pdf), 24 mars 2003. §3.4, lemme 3.4.1 et théorème 3.4.2 avec toute sa preuve, pages imprimées 35–36 / PDF 43–44 ; §3.7 complet, définition 3.7.1, résultats 3.7.2–3.7.7 et leurs preuves, exercice 3.2, pages 39–44 / PDF 47–52 ; définition 4.0.1, introduction et §4.1 complet avec la preuve de 4.1.1 et remarques 4.1.2–4.1.3, pages 49–51 / PDF 57–59. Les pages imprimées 41 et 49 ont aussi été rendues et inspectées. La partie de §4.2 visible au bas de la page 51 n'est pas citée comme preuve complète.

PDF préservé : 816199 octets, SHA-256 `73A1D0DCD0B7F11625293615E693B198C0C33BAE3A57C78A705153CE33942E8A`. [Passages, limites et règles](FIELDS_PROSE_BATCH5_CONSULTED_CANON.json). Consultation rétrospective, sans attribution fictive au traducteur initial.

Pas d'attestation exhaustive. Discriminant, polynôme caractéristique, matrices élémentaires et suite exacte courte sont motivés par les objets explicitement définis dans Stacks, sans citation lexicale fabriquée dans ces pages. Le cours a ses propres défauts : la composition inversée en 3.7.4 n'est pas bien typée en général ; la première ligne de la preuve 3.7.5 conclut y=0 là où l'argument conclut x=0 ; la remarque 4.1.3 dit topologie triviale dans le cas fini. Ces lectures ne sont pas importées. La terminologie de Gal pour toute extension normale dans le cours ne remplace pas celle de Stacks. Aucune consultation du traducteur initial, validation humaine ou lecture de tout le livre n'est inventée.

## Choix délicats et réserves pour une éventuelle revue

La lecture diplomatique conserve les propositions officielles, même lorsqu'une correction serait mathématiquement préférable. Les choix linguistiques interprétatifs sont motivés séparément. Ces remarques ne créent ni une attente de validation humaine ni un nouvel erratum admis.

- `section-trace-pairing` : Le canon définit d'abord trace et norme pour une extension séparable finie. Stacks les définit par multiplication pour toute extension finie ; ne pas importer la séparabilité.
- `lemma-trace-and-norm-linear` : Le texte abrège les cas de dimension zéro ou un et traite les matrices élémentaires dans un sens incluant la dilatation. Réserve de lecture de la source, non ajout de cas ni restriction de la traduction.
- `lemma-separable-trace-pairing` : La minuscule k de la source, ligne 2576, est conservée sous FIELDS-025. Le quotient K/(K*)² est celui des classes modulo multiplication par les carrés, avec la classe zéro ; ce n'est pas automatiquement un quotient de groupes. La preuve anglaise et son degré de détail ne sont pas remplacés par ceux du cours français.
- `definition-discriminant` : Discriminant est un choix défini par le texte source et cohérent dans ce chapitre ; absence d'attestation lexicale externe dans les seules pages consultées pour ce lot, non absence supposée d'usage français.
- `definition-galois-group` : Convention de notation différente du cours : Gal est défini ici seulement pour une extension galoisienne, pas pour toute extension normale.
- `lemma-galois-over-fixed-field` : La source dit degré sur K à la ligne 2777 et K^G(alpha)=L à la ligne 2779. Les propositions de correction sont déjà identifiées FIELDS-027/FIELDS-032 ; pas de duplication ni d'admission nouvelle. Sans agrandir L reprend la contradiction condensée du paragraphe précédent. La normalité est implicite dans les polynômes scindés.
- `theorem-galois-theory` : Choix potentiellement contestable de traduction : stable est interprété au sens ensembliste, non comme fixé point par point. La phrase anglaise est conservée dans le dossier pour examen. Traduire par fixé point par point contredirait l'action de G/H que la source construit aussitôt.
- `lemma-ses-galois` : L'expression suite exacte courte n'a pas été attestée lexicalement dans les pages de cette consultation ; sa portée est fixée par les morphismes et les noyaux explicitement présents. Aucun changement n'est requis pour continuer.

## Exceptions exactes du texte dans les formules

[Liste complète avec expressions et positions](FIELDS_PROSE_BATCH5_MATH_EXCEPTIONS.json)

Expression 5 du lot, indice commençant à zéro.

Seul le texte destiné au lecteur est traduit ; tous les symboles, objets, indices et sens de flèches restent identiques. Exception bornée à cette expression complète, non masquage général.

```tex
L \longrightarrow \text{Mat}(n \times n, K),\quad \alpha \longmapsto \text{matrix of multiplication by }\alpha
```

```tex
L \longrightarrow \text{Mat}(n \times n, K),\quad \alpha \longmapsto \text{matrice de la multiplication par }\alpha
```

Expression 48 du lot, indice commençant à zéro.

Seul le texte destiné au lecteur est traduit ; tous les symboles, objets, indices et sens de flèches restent identiques. Exception bornée à cette expression complète, non masquage général.

```tex
\text{Norm}_{L/K}(\alpha) = (-1)^{[L : K]} a_d^e \quad\text{and}\quad \text{Trace}_{L/K}(\alpha) = - e a_1
```

```tex
\text{Norm}_{L/K}(\alpha) = (-1)^{[L : K]} a_d^e \quad\text{et}\quad \text{Trace}_{L/K}(\alpha) = - e a_1
```

Expression 69 du lot, indice commençant à zéro.

Seul le texte destiné au lecteur est traduit ; tous les symboles, objets, indices et sens de flèches restent identiques. Exception bornée à cette expression complète, non masquage général.

```tex
E_{12}(\lambda) = \left( \begin{matrix} 1 & \lambda & \ldots \\ 0 & 1 & \ldots \\ \ldots & \ldots & \ldots \end{matrix} \right) \quad\text{or}\quad E_1(a) = \left( \begin{matrix} a & 0 & \ldots \\ 0 & 1 & \ldots \\ \ldots & \ldots & \ldots \end{matrix} \right)
```

```tex
E_{12}(\lambda) = \left( \begin{matrix} 1 & \lambda & \ldots \\ 0 & 1 & \ldots \\ \ldots & \ldots & \ldots \end{matrix} \right) \quad\text{ou}\quad E_1(a) = \left( \begin{matrix} a & 0 & \ldots \\ 0 & 1 & \ldots \\ \ldots & \ldots & \ldots \end{matrix} \right)
```

Expression 71 du lot, indice commençant à zéro.

Seul le texte destiné au lecteur est traduit ; tous les symboles, objets, indices et sens de flèches restent identiques. Exception bornée à cette expression complète, non masquage général.

```tex
\text{Trace}_{M/K} = \text{Trace}_{L/K} \circ \text{Trace}_{M/L} \quad\text{and}\quad \text{Norm}_{M/K} = \text{Norm}_{L/K} \circ \text{Norm}_{M/L}
```

```tex
\text{Trace}_{M/K} = \text{Trace}_{L/K} \circ \text{Trace}_{M/L} \quad\text{et}\quad \text{Norm}_{M/K} = \text{Norm}_{L/K} \circ \text{Norm}_{M/L}
```

Expression 272 du lot, indice commençant à zéro.

Seul le texte destiné au lecteur est traduit ; tous les symboles, objets, indices et sens de flèches restent identiques. Exception bornée à cette expression complète, non masquage général.

```tex
\{\text{subgroups of }G\} \longrightarrow \{\text{subextensions }L/M/K\},\quad H \longmapsto L^H
```

```tex
\{\text{sous-groupes de }G\} \longrightarrow \{\text{extensions intermédiaires }L/M/K\},\quad H \longmapsto L^H
```

## Règles et occurrences

### trace-norm

Trace additive et norme multiplicative, non norme métrique ; vérifier les corps source et cible.

Occurrences contextuellement vérifiées : 15. Appui : 3.7.1–3.7.3, pp.39–41.

### trace-form

Forme bilinéaire trace et base duale sont attestées ; forme trace en est l'abréviation explicitement définie.

Occurrences contextuellement vérifiées : 10. Appui : 3.7.5, pp.41–42 ; p.43.

### linear-algebra

Trace/déterminant de la multiplication sont attestés ; pas de citation exacte ici pour polynôme caractéristique ni matrices élémentaires. Leur définition et leur rôle sont vérifiés dans la paire source.

Occurrences contextuellement vérifiées : 10. Appui : Exercice 3.2, p.44.

### discriminant

Classe modulo les carrés, y compris zéro ; choix défini par le passage source, sans attestation lexicale indépendante dans ce lot.

Occurrences contextuellement vérifiées : 11. Appui : Source officielle, definition-discriminant et contexte.

### galois

Galoisienne signifie algébrique, normale et séparable, non nécessairement finie ; la convention Gal de Stacks est conservée.

Occurrences contextuellement vérifiées : 23. Appui : 4.0.1 et introduction, p.49.

### fixed-field

L'ensemble des éléments invariants est attesté ; les expressions condensées et la fidélité de l'action sont justifiées par leurs définitions exactes. Stable concerne ici le sous-corps comme ensemble.

Occurrences contextuellement vérifiées : 4. Appui : Introduction p.49 ; 4.1.1 et preuve pp.49–51.

### intermediate-normal

Préserver la tour et distinguer normalité du sous-groupe et normalité de l'extension ; ne pas intervertir les deux étages.

Occurrences contextuellement vérifiées : 7. Appui : 4.1.1, pp.49–51.

### exact-sequence

Noyau et surjectivité sont vérifiés dans chaque contexte, application linéaire ou homomorphisme de groupes. Le canon les atteste pour les groupes ici, non la locution suite exacte courte ; celle-ci est vérifiée sur la suite affichée et sa preuve.

Occurrences contextuellement vérifiées : 6. Appui : Source officielle, lemma-ses-galois ; preuve 4.1.1 p.51.

## Toutes les paires comparées

### FR-FIELDS-B5-PROSE-0001

`frontmatter` — source 2359–2359, français 2359–2359.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2359) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Le titre conserve les deux opérations trace et norme, sans les réserver aux extensions séparables.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\section{Trace and norm}
```

```tex
\section{Trace et norme}
```

</details>

### FR-FIELDS-B5-PROSE-0002

`section-trace-pairing` — source 2360–2379, français 2360–2379.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2360) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

L'extension reste finie, mais non supposée séparable. Le choix d'une base, la représentation dans les matrices, l'indépendance du choix et la description canonique par la multiplication sont intégralement présents. Le mot parasite for de l'anglais ne reçoit pas de calque grammatical. Le texte lecteur dans la formule nomme bien la multiplication par alpha, non une multiplication de matrices. L'exercice 3.2 du canon confirme ce vocabulaire, avec une hypothèse de séparabilité qui n'est pas importée.

**Réserve :** Le canon définit d'abord trace et norme pour une extension séparable finie. Stacks les définit par multiplication pour toute extension finie ; ne pas importer la séparabilité.

Choix écartés :

- Ajouter séparable en suivant le cours : rejeté, restriction absente de l'anglais officiel.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-trace-pairing}

\noindent
Let $L/K$ be a finite extension of fields. By
Lemma \ref{lemma-vector-space-is-free}
we can choose an isomorphism $L \cong K^{\oplus n}$ of $K$-modules.
Of course $n = [L : K]$ is the degree of the field extension.
Using this isomorphism we get for a $K$-algebra map
$$
L \longrightarrow \text{Mat}(n \times n, K),\quad
\alpha \longmapsto \text{matrix of multiplication by }\alpha
$$
Thus given $\alpha \in L$ we can take the trace and the determinant
of the corresponding matrix. Of course these quantities are independent
of the choice of the basis chosen above. More canonically, simply thinking
of $L$ as a finite dimensional $K$-vector space we have
$\text{Trace}_K(\alpha : L \to L)$ and the determinant
$\det_K(\alpha : L \to L)$.

\begin{definition}
```

```tex
\label{section-trace-pairing}

\noindent
Soit $L/K$ une extension finie de corps. D'après le
Lemme \ref{lemma-vector-space-is-free},
nous pouvons choisir un isomorphisme $L \cong K^{\oplus n}$ de $K$-modules.
Bien entendu, $n = [L : K]$ est le degré de l'extension de corps.
À l'aide de cet isomorphisme, nous obtenons un morphisme de $K$-algèbres
$$
L \longrightarrow \text{Mat}(n \times n, K),\quad
\alpha \longmapsto \text{matrice de la multiplication par }\alpha
$$
Ainsi, étant donné $\alpha \in L$, nous pouvons prendre la trace et le déterminant
de la matrice correspondante. Bien entendu, ces quantités ne dépendent pas
du choix de la base effectué ci-dessus. Plus canoniquement, en considérant simplement
$L$ comme un espace vectoriel de dimension finie sur $K$, nous avons
$\text{Trace}_K(\alpha : L \to L)$ et le déterminant
$\det_K(\alpha : L \to L)$.

\begin{definition}
```

</details>

### FR-FIELDS-B5-PROSE-0003

`definition-trace-norm` — source 2380–2398, français 2380–2398.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2380) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

La trace est celle de l'endomorphisme K-linéaire et la norme son déterminant. La linéarité, la multiplicativité, les deux formules pour les scalaires de K et les deux renvois aux exercices restent exacts. La répétition anglaise Exercises, Exercises n'est pas doublée en français ; les deux identifiants sont conservés. Aucune positivité ni norme d'espace métrique n'est suggérée.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-trace-norm}
Let $L/K$ be a finite extension of fields. For $\alpha \in L$ we define
the {\it trace}
$\text{Trace}_{L/K}(\alpha) = \text{Trace}_K(\alpha : L \to L)$
and the {\it norm}
$\text{Norm}_{L/K}(\alpha) = \det_K(\alpha : L \to L)$.
\end{definition}

\noindent
It is clear from the definition that
$\text{Trace}_{L/K}$ is $K$-linear and satisfies
$\text{Trace}_{L/K}(\alpha) = [L : K]\alpha$ for $\alpha \in K$.
Similarly $\text{Norm}_{L/K}$ is multiplicative and
$\text{Norm}_{L/K}(\alpha) = \alpha^{[L : K]}$ for $\alpha \in K$.
This is a special case of the more general construction discussed
in Exercises, Exercises \ref{exercises-exercise-trace-det} and
\ref{exercises-exercise-trace-det-rings}.

\begin{lemma}
```

```tex
\label{definition-trace-norm}
Soit $L/K$ une extension finie de corps. Pour $\alpha \in L$, nous définissons
la {\it trace}
$\text{Trace}_{L/K}(\alpha) = \text{Trace}_K(\alpha : L \to L)$
et la {\it norme}
$\text{Norm}_{L/K}(\alpha) = \det_K(\alpha : L \to L)$.
\end{definition}

\noindent
Il résulte clairement de la définition que
$\text{Trace}_{L/K}$ est $K$-linéaire et vérifie
$\text{Trace}_{L/K}(\alpha) = [L : K]\alpha$ pour $\alpha \in K$.
De même, $\text{Norm}_{L/K}$ est multiplicative et
$\text{Norm}_{L/K}(\alpha) = \alpha^{[L : K]}$ pour $\alpha \in K$.
C'est un cas particulier de la construction plus générale examinée
dans les Exercices \ref{exercises-exercise-trace-det} et
\ref{exercises-exercise-trace-det-rings}.

\begin{lemma}
```

</details>

### FR-FIELDS-B5-PROSE-0004

`lemma-characteristic-vs-minimal-polynomial` — source 2399–2425, français 2399–2425.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2399) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Polynôme minimal et polynôme caractéristique restent distincts. L'exposant e et son lien au degré total sont inchangés. Toute la preuve est conservée : base sur K(alpha), somme directe stable par alpha, produit des polynômes caractéristiques, réduction au cas monogène et Cayley-Hamilton. L'égalité de degré à la fin s'appuie implicitement sur les polynômes unitaires ; cette observation de lecture n'est pas ajoutée à la preuve.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-characteristic-vs-minimal-polynomial}
Let $L/K$ be a finite extension of fields. Let $\alpha \in L$ and let $P$
be the minimal polynomial of $\alpha$ over $K$. Then the characteristic
polynomial of the $K$-linear map $\alpha : L \to L$ is equal to
$P^e$ with $e \deg(P) = [L : K]$.
\end{lemma}

\begin{proof}
Choose a basis $\beta_1, \ldots, \beta_e$ of $L$ over $K(\alpha)$.
Then $e$ satisfies $e \deg(P) = [L : K]$ by
Lemmas \ref{lemma-degree-minimal-polynomial} and
\ref{lemma-multiplicativity-degrees}.
Then we see that $L = \bigoplus K(\alpha) \beta_i$ is a
direct sum decomposition into $\alpha$-invariant subspaces
hence the characteristic polynomial of $\alpha : L \to L$
is equal to the characteristic polynomial of
$\alpha : K(\alpha) \to K(\alpha)$ to the power $e$.

\medskip\noindent
To finish the proof we may assume that $L = K(\alpha)$.
In this case by Cayley-Hamilton we see that $\alpha$
is a root of the characteristic polynomial. And since the
characteristic polynomial has the same degree as the minimal
polynomial, we find that equality holds.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-characteristic-vs-minimal-polynomial}
Soit $L/K$ une extension finie de corps. Soit $\alpha \in L$, et soit $P$
le polynôme minimal de $\alpha$ sur $K$. Alors le polynôme caractéristique
de l'application $K$-linéaire $\alpha : L \to L$ est égal à
$P^e$, avec $e \deg(P) = [L : K]$.
\end{lemma}

\begin{proof}
Choisissons une base $\beta_1, \ldots, \beta_e$ de $L$ sur $K(\alpha)$.
Alors $e$ vérifie $e \deg(P) = [L : K]$ d'après les
Lemmes \ref{lemma-degree-minimal-polynomial} et
\ref{lemma-multiplicativity-degrees}.
Nous voyons alors que $L = \bigoplus K(\alpha) \beta_i$ est une
décomposition en somme directe de sous-espaces invariants par $\alpha$ ;
le polynôme caractéristique de $\alpha : L \to L$
est donc égal au polynôme caractéristique de
$\alpha : K(\alpha) \to K(\alpha)$ élevé à la puissance $e$.

\medskip\noindent
Pour achever la démonstration, nous pouvons supposer que $L = K(\alpha)$.
Dans ce cas, le théorème de Cayley-Hamilton montre que $\alpha$
est une racine du polynôme caractéristique. Et puisque le
polynôme caractéristique a le même degré que le polynôme
minimal, nous obtenons l'égalité.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B5-PROSE-0005

`lemma-trace-and-norm-from-minimal-polynomial` — source 2426–2443, français 2426–2443.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2426) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Le signe de la norme, la puissance e du coefficient constant, le facteur -e dans la trace et ed=[L:K] sont conservés. Le renvoi et la preuve immédiate restent ceux de la source. Le seul mot dans la formule qui change est and, rendu par et. Les formules du cours portent d'abord sur K(x)/K : elles ne remplacent pas ici les facteurs e de Stacks.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-trace-and-norm-from-minimal-polynomial}
Let $L/K$ be a finite extension of fields. Let $\alpha \in L$ and let
$P = x^d + a_1 x^{d - 1} + \ldots + a_d$
be the minimal polynomial of $\alpha$ over $K$. Then
$$
\text{Norm}_{L/K}(\alpha) = (-1)^{[L : K]} a_d^e
\quad\text{and}\quad
\text{Trace}_{L/K}(\alpha) = - e a_1
$$
where $e d = [L : K]$.
\end{lemma}

\begin{proof}
Follows immediately from Lemma \ref{lemma-characteristic-vs-minimal-polynomial}
and the definitions.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-trace-and-norm-from-minimal-polynomial}
Soit $L/K$ une extension finie de corps. Soit $\alpha \in L$, et soit
$P = x^d + a_1 x^{d - 1} + \ldots + a_d$
le polynôme minimal de $\alpha$ sur $K$. Alors
$$
\text{Norm}_{L/K}(\alpha) = (-1)^{[L : K]} a_d^e
\quad\text{et}\quad
\text{Trace}_{L/K}(\alpha) = - e a_1
$$
où $e d = [L : K]$.
\end{lemma}

\begin{proof}
Cela résulte immédiatement du Lemme \ref{lemma-characteristic-vs-minimal-polynomial}
et des définitions.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B5-PROSE-0006

`lemma-trace-and-norm-linear` — source 2444–2495, français 2444–2495.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2444) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

La restriction des scalaires de L à K est respectée dans les deux formules et V demeure de dimension finie sur L. Pour la trace, la réduction additive à une seule entrée non nulle est conservée. Pour la norme, le cas du noyau non nul, la réduction multiplicative aux matrices affichées, la permutation de la base et les deux calculs directs sont présents. Matrices élémentaires conserve le sens de la source, qui comprend ici une dilatation diagonale ; le terme n'est pas restreint silencieusement aux transvections. Ou traduit la seule alternative dans la formule.

**Réserve :** Le texte abrège les cas de dimension zéro ou un et traite les matrices élémentaires dans un sens incluant la dilatation. Réserve de lecture de la source, non ajout de cas ni restriction de la traduction.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-trace-and-norm-linear}
Let $L/K$ be a finite extension of fields. Let $V$ be a finite dimensional
vector space over $L$. Let $\varphi : V \to V$ be an $L$-linear map.
Then
$$
\text{Trace}_K(\varphi : V \to V) =
\text{Trace}_{L/K}(\text{Trace}_L(\varphi : V \to V))
$$
and
$$
\det\nolimits_K(\varphi : V \to V) =
\text{Norm}_{L/K}(\det\nolimits_L(\varphi : V \to V))
$$
\end{lemma}

\begin{proof}
Choose an isomorphism $V = L^{\oplus n}$ so that $\varphi$ corresponds
to an $n \times n$ matrix. In the case of traces, both sides of the formula
are additive in $\varphi$. Hence we can assume that $\varphi$
corresponds to the matrix with exactly one nonzero entry in the $(i, j)$ spot.
In this case a direct computation shows both sides are equal.

\medskip\noindent
In the case of norms both sides are zero if $\varphi$ has a nonzero kernel.
Hence we may assume $\varphi$ corresponds to an element of
$\text{GL}_n(L)$. Both sides of the formula are multiplicative in $\varphi$.
Since every element of $\text{GL}_n(L)$ is a product of elementary
matrices we may assume that $\varphi$ either looks like
$$
E_{12}(\lambda) =
\left(
\begin{matrix}
1 & \lambda & \ldots \\
0 & 1 & \ldots \\
\ldots & \ldots & \ldots
\end{matrix}
\right)
\quad\text{or}\quad
E_1(a) =
\left(
\begin{matrix}
a & 0 & \ldots \\
0 & 1 & \ldots \\
\ldots & \ldots & \ldots
\end{matrix}
\right)
$$
(because we may also permute the basis elements if we like).
In both cases the formula is easy to verify by direct computation.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-trace-and-norm-linear}
Soit $L/K$ une extension finie de corps. Soit $V$ un espace vectoriel de dimension
finie sur $L$. Soit $\varphi : V \to V$ une application $L$-linéaire.
Alors
$$
\text{Trace}_K(\varphi : V \to V) =
\text{Trace}_{L/K}(\text{Trace}_L(\varphi : V \to V))
$$
et
$$
\det\nolimits_K(\varphi : V \to V) =
\text{Norm}_{L/K}(\det\nolimits_L(\varphi : V \to V))
$$
\end{lemma}

\begin{proof}
Choisissons un isomorphisme $V = L^{\oplus n}$ de sorte que $\varphi$ corresponde
à une matrice $n \times n$. Dans le cas des traces, les deux membres de la formule
sont additifs en $\varphi$. Nous pouvons donc supposer que $\varphi$
corresponde à la matrice dont l'unique coefficient non nul est en position $(i, j)$.
Dans ce cas, un calcul direct montre que les deux membres sont égaux.

\medskip\noindent
Dans le cas des normes, les deux membres sont nuls si $\varphi$ possède un noyau non nul.
Nous pouvons donc supposer que $\varphi$ corresponde à un élément de
$\text{GL}_n(L)$. Les deux membres de la formule sont multiplicatifs en $\varphi$.
Puisque tout élément de $\text{GL}_n(L)$ est un produit de matrices
élémentaires, nous pouvons supposer que $\varphi$ soit de la forme
$$
E_{12}(\lambda) =
\left(
\begin{matrix}
1 & \lambda & \ldots \\
0 & 1 & \ldots \\
\ldots & \ldots & \ldots
\end{matrix}
\right)
\quad\text{ou}\quad
E_1(a) =
\left(
\begin{matrix}
a & 0 & \ldots \\
0 & 1 & \ldots \\
\ldots & \ldots & \ldots
\end{matrix}
\right)
$$
(car nous pouvons également permuter les éléments de la base à notre convenance).
Dans les deux cas, la formule se vérifie aisément par un calcul direct.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B5-PROSE-0007

`lemma-trace-and-norm-tower` — source 2496–2513, français 2496–2513.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2496) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

La composition des traces et celle des normes gardent leur ordre dans la même tour d'extensions finies. Le texte ne transforme pas cette propriété en une formule pour les degrés. La preuve par M vu comme espace vectoriel sur L et le renvoi sont inchangés. Le cours atteste les compositions dans le cas séparable, sans limiter l'énoncé officiel. La transition vers la forme trace est également conservée.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-trace-and-norm-tower}
Let $M/L/K$ be a tower of finite extensions of fields. Then
$$
\text{Trace}_{M/K} = \text{Trace}_{L/K} \circ \text{Trace}_{M/L}
\quad\text{and}\quad
\text{Norm}_{M/K} = \text{Norm}_{L/K} \circ \text{Norm}_{M/L}
$$
\end{lemma}

\begin{proof}
Think of $M$ as a vector space over $L$ and apply
Lemma \ref{lemma-trace-and-norm-linear}.
\end{proof}

\noindent
The trace pairing is defined using the trace.

\begin{definition}
```

```tex
\label{lemma-trace-and-norm-tower}
Soit $M/L/K$ une tour d'extensions finies de corps. Alors
$$
\text{Trace}_{M/K} = \text{Trace}_{L/K} \circ \text{Trace}_{M/L}
\quad\text{et}\quad
\text{Norm}_{M/K} = \text{Norm}_{L/K} \circ \text{Norm}_{M/L}
$$
\end{lemma}

\begin{proof}
Considérons $M$ comme un espace vectoriel sur $L$ et appliquons le
Lemme \ref{lemma-trace-and-norm-linear}.
\end{proof}

\noindent
La forme trace se définit au moyen de la trace.

\begin{definition}
```

</details>

### FR-FIELDS-B5-PROSE-0008

`definition-trace-pairing` — source 2514–2527, français 2514–2527.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2514) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Forme trace désigne la forme bilinéaire symétrique (alpha,beta) envoyée sur la trace du produit, non la trace linéaire seule. Le canon dit forme bilinéaire trace ; l'abréviation française est définie explicitement ici et n'est pas présentée comme une citation littérale. L'équivalence annoncée avec la séparabilité garde la finitude et les deux sens.

Choix écartés :

- Appariement trace : traduction possible, mais le choix forme trace conserve la définition bilinéaire explicite et le registre du canon.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-trace-pairing}
Let $L/K$ be a finite extension of fields. The {\it trace pairing}
for $L/K$ is the symmetric $K$-bilinear form
$$
Q_{L/K} : L \times L \longrightarrow K,\quad
(\alpha, \beta) \longmapsto \text{Trace}_{L/K}(\alpha\beta)
$$
\end{definition}

\noindent
It turns out that a finite extension of fields is separable if and only
if the trace pairing is nondegenerate.

\begin{lemma}
```

```tex
\label{definition-trace-pairing}
Soit $L/K$ une extension finie de corps. La {\it forme trace}
de $L/K$ est la forme $K$-bilinéaire symétrique
$$
Q_{L/K} : L \times L \longrightarrow K,\quad
(\alpha, \beta) \longmapsto \text{Trace}_{L/K}(\alpha\beta)
$$
\end{definition}

\noindent
Il se trouve qu'une extension finie de corps est séparable si et seulement
si la forme trace est non dégénérée.

\begin{lemma}
```

</details>

### FR-FIELDS-B5-PROSE-0009

`lemma-separable-trace-pairing` — source 2528–2607, français 2528–2607.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2528) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Les trois assertions et leurs quantificateurs sont conservés. Tous les paragraphes de preuve sont présents : gamma/alpha pour la non-dégénérescence, extension purement inséparable de degré p, dernier étage d'une tour non séparable, puis récurrence et valeurs propres dans le cas séparable. Le pluriel anglais linear maps devient le singulier pour l'unique endomorphisme affiché, sans changer d'objet. La lecture L/k déjà rétablie sous FIELDS-025 reste littérale. La discussion qui suit, sur le discriminant d'une forme, conserve le dual, la puissance extérieure, la base duale, la transformation par c carré et le déterminant de Gram. La classe dans K/(K*)² inclut le cas nul ; elle n'est pas remplacée par une classe dans le groupe des éléments non nuls.

**Réserve :** La minuscule k de la source, ligne 2576, est conservée sous FIELDS-025. Le quotient K/(K*)² est celui des classes modulo multiplication par les carrés, avec la classe zéro ; ce n'est pas automatiquement un quotient de groupes. La preuve anglaise et son degré de détail ne sont pas remplacés par ceux du cours français.

Choix écartés :

- Remplacer L/k par L/K : correction de la source, gardée hors de l'édition fidèle.
- Remplacer K/(K*)² par K*/(K*)² : exclurait le discriminant nul, donc rejeté.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-separable-trace-pairing}
Let $L/K$ be a finite extension of fields. The following are equivalent:
\begin{enumerate}
\item $L/K$ is separable,
\item $\text{Trace}_{L/K}$ is not identically zero, and
\item the trace pairing $Q_{L/K}$ is nondegenerate.
\end{enumerate}
\end{lemma}

\begin{proof}
It is clear that (3) implies (2). If (2) holds, then pick $\gamma \in L$
with $\text{Trace}_{L/K}(\gamma) \not = 0$. Then if $\alpha \in L$
is nonzero, we see that $Q_{L/K}(\alpha, \gamma/\alpha) \not = 0$.
Hence $Q_{L/K}$ is nondegenerate. This proves the equivalence of
(2) and (3).

\medskip\noindent
Suppose that $K$ has characteristic $p$ and $L = K(\alpha)$ with
$\alpha \not \in K$ and $\alpha^p \in K$. Then $\text{Trace}_{L/K}(1) = p = 0$.
For $i = 1, \ldots, p - 1$ we see that $x^p - \alpha^{pi}$ is the minimal
polynomial for $\alpha^i$ over $K$ and we find
$\text{Trace}_{L/K}(\alpha^i) = 0$ by
Lemma \ref{lemma-trace-and-norm-from-minimal-polynomial}.
Hence for this kind of purely inseparable degree $p$ extension
we see that $\text{Trace}_{L/K}$ is identically zero.

\medskip\noindent
Assume that $L/K$ is not separable. Then there exists a subfield
$L/K'/K$ such that $L/K'$ is a purely inseparable degree $p$ extension
as in the previous paragraph, see
Lemmas \ref{lemma-separable-first} and \ref{lemma-finite-purely-inseparable}.
Hence by Lemma \ref{lemma-trace-and-norm-tower}
we see that $\text{Trace}_{L/K}$ is identically zero.

\medskip\noindent
Assume on the other hand that $L/K$ is separable.
By induction on the degree we will show that
$\text{Trace}_{L/K}$ is not identically zero.
Thus by Lemma \ref{lemma-trace-and-norm-tower} we may assume that
$L/K$ is generated by a single element $\alpha$ (use that if
the trace is nonzero then it is surjective).
We have to show that $\text{Trace}_{L/K}(\alpha^e)$
is nonzero for some $e \geq 0$.
Let $P = x^d + a_1 x^{d - 1} + \ldots + a_d$ be the minimal
polynomial of $\alpha$ over $K$.
Then $P$ is also the characteristic polynomial of the linear
maps $\alpha : L \to L$, see
Lemma \ref{lemma-characteristic-vs-minimal-polynomial}.
Since $L/k$ is separable we see from Lemma \ref{lemma-recognize-separable}
that $P$ has $d$ pairwise distinct roots $\alpha_1, \ldots, \alpha_d$
in an algebraic closure $\overline{K}$ of $K$. Thus these are the
eigenvalues of $\alpha : L \to L$.
By linear algebra, the trace of $\alpha^e$ is
equal to $\alpha_1^e + \ldots + \alpha_d^e$.
Thus we conclude by Lemma \ref{lemma-sums-of-powers}.
\end{proof}

\noindent
Let $K$ be a field and let $Q : V \times V \to K$ be a bilinear form
on a finite dimensional vector space over $K$. Say $\dim_K(V) = n$.
Then $Q$ defines a linear map $Q : V \to V^*$, $v \mapsto Q(v, -)$
where $V^* = \Hom_K(V, K)$ is the dual vector space. Hence a linear map
$$
\det(Q) : \wedge^n(V) \longrightarrow \wedge^n(V)^*
$$
If we pick a basis element $\omega \in \wedge^n(V)$, then we can
write $\det(Q)(\omega) = \lambda \omega^*$, where $\omega^*$
is the dual basis element in $\wedge^n(V)^*$. If we change our
choice of $\omega$ into $c \omega$ for some $c \in K^*$, then
$\omega^*$ changes into $c^{-1} \omega^*$ and therefore
$\lambda$ changes into $c^2 \lambda$. Thus the class of
$\lambda$ in $K/(K^*)^2$ is well defined and is called the
{\it discriminant of $Q$}. Unwinding the definitions we see that
$$
\lambda = \det(Q(v_i, v_j)_{1 \leq i, j \leq n})
$$
if $\{v_1, \ldots, v_n\}$ is a basis for $V$ over $K$. Observe that
the discriminant is nonzero if and only if $Q$ is nondegenerate.

\begin{definition}
```

```tex
\label{lemma-separable-trace-pairing}
Soit $L/K$ une extension finie de corps. Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item $L/K$ est séparable,
\item $\text{Trace}_{L/K}$ n'est pas identiquement nulle, et
\item la forme trace $Q_{L/K}$ est non dégénérée.
\end{enumerate}
\end{lemma}

\begin{proof}
Il est clair que (3) implique (2). Si (2) est vérifiée, choisissons $\gamma \in L$
tel que $\text{Trace}_{L/K}(\gamma) \not = 0$. Alors, si $\alpha \in L$
est non nul, nous voyons que $Q_{L/K}(\alpha, \gamma/\alpha) \not = 0$.
Ainsi, $Q_{L/K}$ est non dégénérée. Cela démontre l'équivalence de
(2) et (3).

\medskip\noindent
Supposons que $K$ soit de caractéristique $p$ et que $L = K(\alpha)$ avec
$\alpha \not \in K$ et $\alpha^p \in K$. Alors $\text{Trace}_{L/K}(1) = p = 0$.
Pour $i = 1, \ldots, p - 1$, nous voyons que $x^p - \alpha^{pi}$ est le polynôme
minimal de $\alpha^i$ sur $K$, et nous obtenons
$\text{Trace}_{L/K}(\alpha^i) = 0$ d'après le
Lemme \ref{lemma-trace-and-norm-from-minimal-polynomial}.
Ainsi, pour ce type d'extension purement inséparable de degré $p$,
nous voyons que $\text{Trace}_{L/K}$ est identiquement nulle.

\medskip\noindent
Supposons que $L/K$ ne soit pas séparable. Il existe alors un corps intermédiaire
$L/K'/K$ tel que $L/K'$ soit une extension purement inséparable de degré $p$
comme au paragraphe précédent ; voir les
Lemmes \ref{lemma-separable-first} et \ref{lemma-finite-purely-inseparable}.
Ainsi, d'après le Lemme \ref{lemma-trace-and-norm-tower},
nous voyons que $\text{Trace}_{L/K}$ est identiquement nulle.

\medskip\noindent
Supposons au contraire que $L/K$ soit séparable.
Par récurrence sur le degré, nous allons montrer que
$\text{Trace}_{L/K}$ n'est pas identiquement nulle.
Ainsi, d'après le Lemme \ref{lemma-trace-and-norm-tower}, nous pouvons supposer que
$L/K$ est engendrée par un seul élément $\alpha$ (utiliser le fait que, si
la trace est non nulle, alors elle est surjective).
Nous devons montrer que $\text{Trace}_{L/K}(\alpha^e)$
est non nulle pour un certain $e \geq 0$.
Soit $P = x^d + a_1 x^{d - 1} + \ldots + a_d$ le polynôme
minimal de $\alpha$ sur $K$.
Alors $P$ est aussi le polynôme caractéristique de l'application linéaire
$\alpha : L \to L$ ; voir le
Lemme \ref{lemma-characteristic-vs-minimal-polynomial}.
Puisque $L/k$ est séparable, le Lemme \ref{lemma-recognize-separable} montre
que $P$ a $d$ racines deux à deux distinctes $\alpha_1, \ldots, \alpha_d$
dans une clôture algébrique $\overline{K}$ de $K$. Ce sont donc les
valeurs propres de $\alpha : L \to L$.
D'après l'algèbre linéaire, la trace de $\alpha^e$ est
égale à $\alpha_1^e + \ldots + \alpha_d^e$.
Nous concluons donc par le Lemme \ref{lemma-sums-of-powers}.
\end{proof}

\noindent
Soit $K$ un corps et soit $Q : V \times V \to K$ une forme bilinéaire
sur un espace vectoriel de dimension finie sur $K$. Posons $\dim_K(V) = n$.
Alors $Q$ définit une application linéaire $Q : V \to V^*$, $v \mapsto Q(v, -)$,
où $V^* = \Hom_K(V, K)$ est l'espace vectoriel dual. D'où une application linéaire
$$
\det(Q) : \wedge^n(V) \longrightarrow \wedge^n(V)^*
$$
Si nous choisissons un vecteur de base $\omega \in \wedge^n(V)$, nous pouvons
écrire $\det(Q)(\omega) = \lambda \omega^*$, où $\omega^*$
est le vecteur de base dual dans $\wedge^n(V)^*$. Si nous remplaçons notre
choix de $\omega$ par $c \omega$ pour un certain $c \in K^*$, alors
$\omega^*$ devient $c^{-1} \omega^*$ et, par conséquent,
$\lambda$ devient $c^2 \lambda$. Ainsi, la classe de
$\lambda$ dans $K/(K^*)^2$ est bien définie et s'appelle le
{\it discriminant de $Q$}. En développant les définitions, nous voyons que
$$
\lambda = \det(Q(v_i, v_j)_{1 \leq i, j \leq n})
$$
si $\{v_1, \ldots, v_n\}$ est une base de $V$ sur $K$. Notons que
le discriminant est non nul si et seulement si $Q$ est non dégénérée.

\begin{definition}
```

</details>

### FR-FIELDS-B5-PROSE-0010

`definition-discriminant` — source 2608–2621, français 2608–2621.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2608) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Le discriminant de l'extension reste celui de sa forme trace. La condition de non-nullité et l'avertissement sur le représentant a, par opposition à sa classe modulo les carrés, sont conservés. Le nom discriminant est défini sans ambiguïté par le passage officiel ; aucune attestation lexicale externe de ce nom dans les pages de canon lues ici n'est revendiquée.

**Réserve :** Discriminant est un choix défini par le texte source et cohérent dans ce chapitre ; absence d'attestation lexicale externe dans les seules pages consultées pour ce lot, non absence supposée d'usage français.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-discriminant}
Let $L/K$ be a finite extension of fields. The
{\it discriminant of $L/K$} is the discriminant of
the trace pairing $Q_{L/K}$.
\end{definition}

\noindent
By the discussion above and Lemma \ref{lemma-separable-trace-pairing}
we see that the discriminant is nonzero if and only
if $L/K$ is separable. For $a \in K$ we often say
``the discriminant is $a$'' when it would be more correct
to say the discriminant is the class of $a$ in $K/(K^*)^2$.

\begin{exercise}
```

```tex
\label{definition-discriminant}
Soit $L/K$ une extension finie de corps. Le
{\it discriminant de $L/K$} est le discriminant de
la forme trace $Q_{L/K}$.
\end{definition}

\noindent
D'après la discussion ci-dessus et le Lemme \ref{lemma-separable-trace-pairing},
nous voyons que le discriminant est non nul si et seulement
si $L/K$ est séparable. Pour $a \in K$, nous disons souvent
« le discriminant vaut $a$ » alors qu'il serait plus exact
de dire que le discriminant est la classe de $a$ dans $K/(K^*)^2$.

\begin{exercise}
```

</details>

### FR-FIELDS-B5-PROSE-0011

`exercise-quadratic-discriminant` — source 2622–2647, français 2622–2643.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2622) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Les trois cas sont exclusifs comme dans la source : caractéristique deux inséparable de discriminant nul, caractéristique deux séparable de discriminant un, et caractéristique différente de deux avec discriminant non carré. Prendre une racine carrée signifie ici l'adjoindre au corps ; le français précise l'opération sans ajouter d'hypothèse ni de solution. L'avertissement précédent sur la classe du discriminant demeure applicable. Le passage à la section de Galois n'ajoute aucune preuve à l'exercice.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{exercise-quadratic-discriminant}
Let $L/K$ be an extension of degree $2$. Show that exactly
one of the following happens
\begin{enumerate}
\item the discriminant is $0$, the characteristic of $K$ is $2$,
and $L/K$ is purely inseparable obtained by taking a square root
of an element of $K$,
\item the discriminant is $1$, the characteristic of $K$ is $2$, and
$L/K$ is separable of degree $2$,
\item the discriminant is not a square, the characteristic of $K$
is not $2$, and $L$ is obtained from $K$ by taking the square root
of the discriminant.
\end{enumerate}
\end{exercise}











\section{Galois theory}
```

```tex
\label{exercise-quadratic-discriminant}
Soit $L/K$ une extension de degré $2$. Montrer qu'il se produit exactement
l'un des cas suivants :
\begin{enumerate}
\item le discriminant vaut $0$, la caractéristique de $K$ vaut $2$,
et $L/K$ est purement inséparable et s'obtient en adjoignant une racine carrée
d'un élément de $K$,
\item le discriminant vaut $1$, la caractéristique de $K$ vaut $2$, et
$L/K$ est séparable de degré $2$,
\item le discriminant n'est pas un carré, la caractéristique de $K$
n'est pas $2$, et $L$ s'obtient à partir de $K$ en adjoignant la racine carrée
du discriminant.
\end{enumerate}
\end{exercise}







\section{Théorie de Galois}
```

</details>

### FR-FIELDS-B5-PROSE-0012

`section-galois-theory` — source 2648–2653, français 2644–2649.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2648) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

L'introduction reste l'annonce de la définition, sans ajouter d'histoire ou de convention.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-galois-theory}

\noindent
Here is the definition.

\begin{definition}
```

```tex
\label{section-galois-theory}

\noindent
Voici la définition.

\begin{definition}
```

</details>

### FR-FIELDS-B5-PROSE-0013

`definition-galois` — source 2654–2663, français 2650–2659.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2654) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

L'extension galoisienne reste algébrique, séparable et normale ; aucune finitude n'est ajoutée à la définition. Le critère annoncé ensuite concerne expressément une extension finie. La définition 4.0.1 du canon atteste exactement cette distinction.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-galois}
A field extension $E/F$ is called {\it Galois} if it is algebraic,
separable, and normal.
\end{definition}

\noindent
It turns out that a finite extension is Galois if and only if it has
the ``correct'' number of automorphisms.

\begin{lemma}
```

```tex
\label{definition-galois}
Une extension de corps $E/F$ est dite {\it galoisienne} si elle est algébrique,
séparable et normale.
\end{definition}

\noindent
On verra qu'une extension finie est galoisienne si et seulement si elle possède
le nombre « correct » d'automorphismes.

\begin{lemma}
```

</details>

### FR-FIELDS-B5-PROSE-0014

`lemma-finite-Galois` — source 2664–2682, français 2660–2678.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2664) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Le nombre d'automorphismes est comparé au degré total sous l'hypothèse de finitude. Les deux sens utilisent le lemme officiel sur normalité et automorphismes et l'égalité du degré séparable au degré total. Le féminin galoisienne reprend elliptiquement extension ; il ne modifie pas le corps de base. La transition vers la définition du groupe est conservée.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-finite-Galois}
Let $E/F$ be a finite extension of fields. Then $E$ is Galois over $F$
if and only if $|\text{Aut}(E/F)| = [E : F]$.
\end{lemma}

\begin{proof}
Assume $|\text{Aut}(E/F)| = [E : F]$. By
Lemma \ref{lemma-normal-and-automorphisms} this implies
that $E/F$ is separable and normal, hence Galois.
Conversely, if $E/F$ is separable then $[E : F] = [E : F]_s$ and
if $E/F$ is in addition normal, then
Lemma \ref{lemma-normal-and-automorphisms} implies that
$|\text{Aut}(E/F)| = [E : F]$.
\end{proof}

\noindent
Motivated by the lemma above we introduce the Galois group as follows.

\begin{definition}
```

```tex
\label{lemma-finite-Galois}
Soit $E/F$ une extension finie de corps. Alors $E$ est galoisienne sur $F$
si et seulement si $|\text{Aut}(E/F)| = [E : F]$.
\end{lemma}

\begin{proof}
Supposons que $|\text{Aut}(E/F)| = [E : F]$. D'après le
Lemme \ref{lemma-normal-and-automorphisms}, cela implique
que $E/F$ est séparable et normale, donc galoisienne.
Réciproquement, si $E/F$ est séparable, alors $[E : F] = [E : F]_s$, et
si $E/F$ est de plus normale, le
Lemme \ref{lemma-normal-and-automorphisms} implique que
$|\text{Aut}(E/F)| = [E : F]$.
\end{proof}

\noindent
Motivés par le lemme précédent, nous introduisons le groupe de Galois comme suit.

\begin{definition}
```

</details>

### FR-FIELDS-B5-PROSE-0015

`definition-galois-group` — source 2683–2693, français 2679–2689.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2683) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Stacks donne ici le nom et la notation Gal à une extension déjà galoisienne. Le cours les emploie aussi pour une extension seulement normale : cette convention différente n'est pas importée. Le commentaire sur les extensions infinies et la structure de groupe topologique, avec son renvoi, reste complet.

**Réserve :** Convention de notation différente du cours : Gal est défini ici seulement pour une extension galoisienne, pas pour toute extension normale.

Choix écartés :

- Étendre la définition à toute extension normale suivant le canon : rejeté, changement de convention source.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{definition-galois-group}
If $E/F$ is a Galois extension, then the group $\text{Aut}(E/F)$ is
called the {\it Galois group} and it is denoted $\text{Gal}(E/F)$.
\end{definition}

\noindent
If $L/K$ is an infinite Galois extension, then one should think of the
Galois group as a topological group. We will return to this in
Section \ref{section-infinite-galois}.

\begin{lemma}
```

```tex
\label{definition-galois-group}
Si $E/F$ est une extension galoisienne, le groupe $\text{Aut}(E/F)$ est
appelé le {\it groupe de Galois} et est noté $\text{Gal}(E/F)$.
\end{definition}

\noindent
Si $L/K$ est une extension galoisienne infinie, il faut considérer le
groupe de Galois comme un groupe topologique. Nous y reviendrons à la
section \ref{section-infinite-galois}.

\begin{lemma}
```

</details>

### FR-FIELDS-B5-PROSE-0016

`lemma-galois-goes-up` — source 2694–2703, français 2690–2699.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2694) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Dans K/E/F, la propriété de K sur F monte à K sur E. On ne déduit pas que E/F serait galoisienne. Les deux références à la normalité et à la séparabilité restent la preuve entière ; aucun argument plus fort n'est ajouté.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-galois-goes-up}
Let $K/E/F$ be a tower of algebraic field extensions.
If $K$ is Galois over $F$, then $K$ is Galois over $E$.
\end{lemma}

\begin{proof}
Combine Lemmas \ref{lemma-normal-goes-up} and \ref{lemma-separable-goes-up}.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-galois-goes-up}
Soit $K/E/F$ une tour d'extensions algébriques de corps.
Si $K$ est galoisienne sur $F$, alors $K$ est galoisienne sur $E$.
\end{lemma}

\begin{proof}
Il suffit de combiner les Lemmes \ref{lemma-normal-goes-up} et \ref{lemma-separable-goes-up}.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B5-PROSE-0017

`lemma-normal-closure-galois` — source 2704–2726, français 2700–2722.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2704) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

La clôture normale de l'extension finie séparable reste galoisienne. La preuve conserve M_sep, l'inclusion de L et l'égalité imposée par la minimalité. La transition définit K^G pour un groupe agissant par automorphismes ; corps des invariants est un raccourci du sous-corps des éléments invariants décrit dans le canon. Il ne s'agit pas d'un corps quotient. La variante clôture normale était déjà motivée, sans attestation lexicale exacte, au lot 4.

Choix écartés :

- Corps fixe : variante possible ; corps des invariants est conservé avec la définition complète de K^G.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-normal-closure-galois}
Let $L/K$ be a finite separable extension of fields.
Let $M$ be the normal closure of $L$ over $K$
(Definition \ref{definition-normal-closure}).
Then $M/K$ is Galois.
\end{lemma}

\begin{proof}
The subextension $M/M_{sep}/K$ of Lemma \ref{lemma-separable-first}
is normal by Lemma \ref{lemma-separable-first-normal}.
Since $L/K$ is separable we have $L \subset M_{sep}$.
By minimality $M = M_{sep}$ and the proof is done.
\end{proof}

\noindent
Let $G$ be a group acting on a field $K$ (by field automorphisms).
We will often use the notation
$$
K^G = \{x \in K \mid \sigma(x) = x \ \forall \sigma \in G\}
$$
and we will call this the {\it fixed field} for the action of $G$ on $K$.

\begin{lemma}
```

```tex
\label{lemma-normal-closure-galois}
Soit $L/K$ une extension finie séparable de corps.
Soit $M$ la clôture normale de $L$ sur $K$
(Définition \ref{definition-normal-closure}).
Alors $M/K$ est galoisienne.
\end{lemma}

\begin{proof}
L'extension intermédiaire $M/M_{sep}/K$ du Lemme \ref{lemma-separable-first}
est normale d'après le Lemme \ref{lemma-separable-first-normal}.
Puisque $L/K$ est séparable, nous avons $L \subset M_{sep}$.
Par minimalité, $M = M_{sep}$, ce qui achève la démonstration.
\end{proof}

\noindent
Soit $G$ un groupe agissant sur un corps $K$ (par automorphismes de corps).
Nous emploierons souvent la notation
$$
K^G = \{x \in K \mid \sigma(x) = x \ \forall \sigma \in G\}
$$
et appellerons ce corps le {\it corps des invariants} de l'action de $G$ sur $K$.

\begin{lemma}
```

</details>

### FR-FIELDS-B5-PROSE-0018

`lemma-galois-over-fixed-field` — source 2727–2783, français 2723–2779.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2727) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Le groupe est fini et l'action fidèle ; l'orbite est un ensemble de racines distinctes, et non un produit avec multiplicité sur tous les éléments du groupe. L'invariance des coefficients, l'algébricité, la séparabilité et la réduction à une sous-extension finie restent complètes. La normalité se lit implicitement dans le fait que les polynômes minimaux divisent les produits scindés ; aucune nouvelle phrase de preuve n'est insérée. La réduction par une famille détectant l'identité et le dernier argument par élément primitif sont conservés, y compris les deux lectures officielles sur K et K^G(alpha)=L déjà restaurées sous FIELDS-027 et FIELDS-032.

**Réserve :** La source dit degré sur K à la ligne 2777 et K^G(alpha)=L à la ligne 2779. Les propositions de correction sont déjà identifiées FIELDS-027/FIELDS-032 ; pas de duplication ni d'admission nouvelle. Sans agrandir L reprend la contradiction condensée du paragraphe précédent. La normalité est implicite dans les polynômes scindés.

Choix écartés :

- Réintroduire les corrections du corps de base et de L en K : rejeté pour la traduction officielle ; les anciennes propositions restent récupérables.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-galois-over-fixed-field}
Let $K$ be a field. Let $G$ be a finite group acting faithfully on $K$.
Then the extension $K/K^G$ is Galois, we have $[K : K^G] = |G|$,
and the Galois group of the extension is $G$.
\end{lemma}

\begin{proof}
Given $\alpha \in K$ consider the orbit $G \cdot \alpha \subset K$
of $\alpha$ under the group action. Consider the polynomial
$$
P = \prod\nolimits_{\beta \in G \cdot \alpha} (x - \beta) \in K[x]
$$
The key to the whole lemma is that this polynomial is invariant
under the action of $G$ and hence has coefficients in $K^G$.
Namely, for $\tau \in G$ we have
$$
P^\tau = \prod\nolimits_{\beta \in G \cdot \alpha} (x - \tau(\beta)) =
\prod\nolimits_{\beta \in G \cdot \alpha} (x - \beta) = P
$$
because the map $\beta \mapsto \tau(\beta)$ is a permutation of
the orbit $G \cdot \alpha$. Thus $P \in K^G[x]$. Since also
$P(\alpha) = 0$ as $\alpha$ is an element of its orbit
we conclude that the extension $K/K^G$ is algebraic. Moreover,
the minimal polynomial $Q$ of $\alpha$ over $K^G$ divides the
polynomial $P$ just constructed. Hence $Q$ is separable
(by Lemma \ref{lemma-recognize-separable} for example) and
we conclude that $K/K^G$ is separable. Thus $K/K^G$ is Galois.
To finish the proof it suffices to show that $[K : K^G] = |G|$
since then $G$ will be the Galois group by
Lemma \ref{lemma-finite-Galois}.

\medskip\noindent
Pick finitely many elements $\alpha_i \in K$, $i = 1, \ldots, n$
such that $\sigma(\alpha_i) = \alpha_i$ for $i = 1, \ldots, n$ implies
$\sigma$ is the neutral element of $G$. Set
$$
L = K^G(\{\sigma(\alpha_i); 1 \leq i \leq n, \sigma \in G\}) \subset K
$$
and observe that the action of $G$ on $K$ induces an action of $G$ on $L$.
We will show that $L$ has degree $|G|$ over $K^G$. This will finish the
proof, since if $L \subset K$ is proper, then we can add an element
$\alpha \in K$, $\alpha \not \in L$ to our list of elements
$\alpha_1, \ldots, \alpha_n$ without increasing $L$ which is absurd.
This reduces us to the case that $K/K^G$ is finite which is
treated in the next paragraph.

\medskip\noindent
Assume $K/K^G$ is finite. By Lemma \ref{lemma-primitive-element}
we can find $\alpha \in K$ such that $K = K^G(\alpha)$.
By the construction in the first paragraph of this proof we see
that $\alpha$ has degree at most $|G|$ over $K$. However, the
degree cannot be less than $|G|$ as $G$ acts faithfully on
$K^G(\alpha) = L$ by construction and the inequality of
Lemma \ref{lemma-normal-and-automorphisms}.
\end{proof}

\begin{theorem}[Fundamental theorem of Galois theory]
```

```tex
\label{lemma-galois-over-fixed-field}
Soit $K$ un corps. Soit $G$ un groupe fini agissant fidèlement sur $K$.
Alors l'extension $K/K^G$ est galoisienne, on a $[K : K^G] = |G|$,
et le groupe de Galois de l'extension est $G$.
\end{lemma}

\begin{proof}
Étant donné $\alpha \in K$, considérons l'orbite $G \cdot \alpha \subset K$
de $\alpha$ sous l'action du groupe. Considérons le polynôme
$$
P = \prod\nolimits_{\beta \in G \cdot \alpha} (x - \beta) \in K[x]
$$
Le point clé de tout le lemme est que ce polynôme est invariant
sous l'action de $G$ et possède donc ses coefficients dans $K^G$.
En effet, pour $\tau \in G$, nous avons
$$
P^\tau = \prod\nolimits_{\beta \in G \cdot \alpha} (x - \tau(\beta)) =
\prod\nolimits_{\beta \in G \cdot \alpha} (x - \beta) = P
$$
car l'application $\beta \mapsto \tau(\beta)$ est une permutation de
l'orbite $G \cdot \alpha$. Ainsi $P \in K^G[x]$. De plus,
$P(\alpha) = 0$, puisque $\alpha$ appartient à son orbite ;
nous en concluons que l'extension $K/K^G$ est algébrique. En outre,
le polynôme minimal $Q$ de $\alpha$ sur $K^G$ divise le
polynôme $P$ que nous venons de construire. Par conséquent, $Q$ est séparable
(par exemple d'après le Lemme \ref{lemma-recognize-separable}) et
nous en concluons que $K/K^G$ est séparable. Ainsi $K/K^G$ est galoisienne.
Pour achever la démonstration, il suffit de montrer que $[K : K^G] = |G|$,
car alors $G$ sera le groupe de Galois d'après le
Lemme \ref{lemma-finite-Galois}.

\medskip\noindent
Choisissons un nombre fini d'éléments $\alpha_i \in K$, $i = 1, \ldots, n$,
de sorte que les égalités $\sigma(\alpha_i) = \alpha_i$ pour $i = 1, \ldots, n$ impliquent
que $\sigma$ est l'élément neutre de $G$. Posons
$$
L = K^G(\{\sigma(\alpha_i); 1 \leq i \leq n, \sigma \in G\}) \subset K
$$
et observons que l'action de $G$ sur $K$ induit une action de $G$ sur $L$.
Nous allons montrer que $L$ est de degré $|G|$ sur $K^G$. Cela achèvera la
démonstration : en effet, si $L \subset K$ était stricte, nous pourrions ajouter un élément
$\alpha \in K$, $\alpha \not \in L$, à notre liste d'éléments
$\alpha_1, \ldots, \alpha_n$ sans agrandir $L$, ce qui est absurde.
Nous sommes ainsi ramenés au cas où $K/K^G$ est finie, lequel est
traité dans le paragraphe suivant.

\medskip\noindent
Supposons $K/K^G$ finie. D'après le Lemme \ref{lemma-primitive-element},
nous pouvons trouver $\alpha \in K$ tel que $K = K^G(\alpha)$.
La construction du premier paragraphe de cette démonstration montre
que $\alpha$ est de degré au plus $|G|$ sur $K$. Toutefois, ce
degré ne peut être inférieur à $|G|$, puisque $G$ agit fidèlement sur
$K^G(\alpha) = L$ par construction et en vertu de l'inégalité du
Lemme \ref{lemma-normal-and-automorphisms}.
\end{proof}

\begin{theorem}[Théorème fondamental de la théorie de Galois]
```

</details>

### FR-FIELDS-B5-PROSE-0019

`theorem-galois-theory` — source 2784–2824, français 2780–2820.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2784) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Les deux ensembles, la bijection et son inverse, puis le critère des sous-groupes normaux sont inchangés. Extensions intermédiaires traduit subextensions en conservant la tour L/M/K. Tous les arguments de degrés, de noyaux et de restriction demeurent. Dans la preuve, fixed by the action désigne L^H comme sous-corps globalement invariant : stable sous l'action rend ce sens, confirmé par l'action du quotient dans la phrase suivante, et ne prétend pas que chaque élément soit fixé par G. Cette interprétation linguistique est signalée pour examen ; le français n'ajoute ni preuve ni hypothèse. Le théorème 4.1.1 du canon fournit un contexte analogue, pas une nouvelle autorité pour réécrire Stacks.

**Réserve :** Choix potentiellement contestable de traduction : stable est interprété au sens ensembliste, non comme fixé point par point. La phrase anglaise est conservée dans le dossier pour examen. Traduire par fixé point par point contredirait l'action de G/H que la source construit aussitôt.

Choix écartés :

- Fixé point par point par G : rejeté, ce n'est pas le sens ensembliste requis par l'action du quotient dans la même phrase.
- Globalement fixé : variante fidèle possible, mais aucune nécessité de remplacer stable, qui rend ici exactement cette distinction.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{theorem-galois-theory}
Let $L/K$ be a finite Galois extension with Galois group $G$.
Then we have $K = L^G$ and the map
$$
\{\text{subgroups of }G\}
\longrightarrow
\{\text{subextensions }L/M/K\},\quad
H \longmapsto L^H
$$
is a bijection whose inverse maps $M$ to $\text{Gal}(L/M)$.
The normal subgroups $H$ of $G$ correspond exactly to those
subextensions $M$ with $M/K$ Galois.
\end{theorem}

\begin{proof}
By Lemma \ref{lemma-galois-goes-up} given a subextension $L/M/K$
the extension $L/M$ is Galois. Of course $L/M$ is also finite
(Lemma \ref{lemma-finite-goes-up}). Thus $|\text{Gal}(L/M)| = [L : M]$
by Lemma \ref{lemma-finite-Galois}.
Conversely, if $H \subset G$ is a finite subgroup, then
$[L : L^H] = |H|$ by Lemma \ref{lemma-galois-over-fixed-field}.
It follows formally from these two observations that we obtain
a bijective correspondence as in the theorem.

\medskip\noindent
If $H \subset G$ is normal, then $L^H$ is fixed by the action of
$G$ and we obtain a canonical map $G/H \to \text{Aut}(L^H/K)$.
This map has to be injective as $\text{Gal}(L/L^H) = H$. Hence
$|G/H| = [L^H : K]$ and $L^H$ is Galois by
Lemma \ref{lemma-finite-Galois}.

\medskip\noindent
Conversely, assume that $K \subset M \subset L$ with $M/K$ Galois.
By Lemma \ref{lemma-lift-maps} we see that every
element $\tau \in \text{Gal}(L/K)$ induces an element
$\tau|_M \in \text{Gal}(M/K)$. This induces a homomorphism
of Galois groups $\text{Gal}(L/K) \to \text{Gal}(M/K)$ whose
kernel is $H$. Thus $H$ is a normal subgroup.
\end{proof}

\begin{lemma}
```

```tex
\label{theorem-galois-theory}
Soit $L/K$ une extension galoisienne finie de groupe de Galois $G$.
Alors $K = L^G$ et l'application
$$
\{\text{sous-groupes de }G\}
\longrightarrow
\{\text{extensions intermédiaires }L/M/K\},\quad
H \longmapsto L^H
$$
est une bijection dont l'inverse envoie $M$ sur $\text{Gal}(L/M)$.
Les sous-groupes normaux $H$ de $G$ correspondent exactement aux
extensions intermédiaires $M$ telles que $M/K$ soit galoisienne.
\end{theorem}

\begin{proof}
D'après le Lemme \ref{lemma-galois-goes-up}, pour toute extension intermédiaire $L/M/K$,
l'extension $L/M$ est galoisienne. Bien entendu, $L/M$ est aussi finie
(Lemme \ref{lemma-finite-goes-up}). Ainsi $|\text{Gal}(L/M)| = [L : M]$
d'après le Lemme \ref{lemma-finite-Galois}.
Réciproquement, si $H \subset G$ est un sous-groupe fini, alors
$[L : L^H] = |H|$ d'après le Lemme \ref{lemma-galois-over-fixed-field}.
Il résulte formellement de ces deux observations que nous obtenons
la correspondance bijective annoncée dans le théorème.

\medskip\noindent
Si $H \subset G$ est normal, alors $L^H$ est stable sous l'action de
$G$ et nous obtenons une application canonique $G/H \to \text{Aut}(L^H/K)$.
Cette application est nécessairement injective puisque $\text{Gal}(L/L^H) = H$. Ainsi
$|G/H| = [L^H : K]$ et $L^H$ est galoisienne d'après le
Lemme \ref{lemma-finite-Galois}.

\medskip\noindent
Réciproquement, supposons que $K \subset M \subset L$ et que $M/K$ soit galoisienne.
D'après le Lemme \ref{lemma-lift-maps}, tout
élément $\tau \in \text{Gal}(L/K)$ induit un élément
$\tau|_M \in \text{Gal}(M/K)$. On obtient ainsi un homomorphisme
de groupes de Galois $\text{Gal}(L/K) \to \text{Gal}(M/K)$ dont le
noyau est $H$. Ainsi $H$ est un sous-groupe normal.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B5-PROSE-0020

`lemma-ses-galois` — source 2825–2851, français 2821–2847.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2825) · [Français de travail](staged/fr/009_fields.prose-batch4.fr.tex)

Les deux hypothèses de finitude galoisienne concernent L/K et M/K. La suite exacte courte garde les quatre flèches, le noyau et la restriction ; le groupe de gauche n'est pas remplacé par un quotient. Le français rend sizes par ordres pour les groupes finis. Les deux justifications de surjectivité, par les degrés et directement par prolongement, sont conservées. Suite exacte courte est motivé par cette suite explicite, sans attestation lexicale de cette expression dans le canon consulté ici.

**Réserve :** L'expression suite exacte courte n'a pas été attestée lexicalement dans les pages de cette consultation ; sa portée est fixée par les morphismes et les noyaux explicitement présents. Aucun changement n'est requis pour continuer.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-ses-galois}
Let $L/M/K$ be a tower of fields. Assume $L/K$ and $M/K$ are finite Galois.
Then we obtain a short exact sequence
$$
1 \to \text{Gal}(L/M) \to \text{Gal}(L/K) \to \text{Gal}(M/K) \to 1
$$
of finite groups.
\end{lemma}

\begin{proof}
Namely, by Lemma \ref{lemma-lift-maps}
we see that every element $\tau \in \text{Gal}(L/K)$ induces an element
$\tau|_M \in \text{Gal}(M/K)$ which gives us the homomorphism on the
right. The map on the left identifies the left group with the kernel
of the right arrow. The sequence is exact because the sizes
of the groups work out correctly by multiplicativity of degrees
in towers of finite extensions
(Lemma \ref{lemma-multiplicativity-degrees}).
One can also use Lemma \ref{lemma-lift-maps}
directly to see that the map on the right is surjective.
\end{proof}
```

```tex
\label{lemma-ses-galois}
Soit $L/M/K$ une tour de corps. Supposons $L/K$ et $M/K$ finies galoisiennes.
Alors nous obtenons une suite exacte courte
$$
1 \to \text{Gal}(L/M) \to \text{Gal}(L/K) \to \text{Gal}(M/K) \to 1
$$
de groupes finis.
\end{lemma}

\begin{proof}
En effet, d'après le Lemme \ref{lemma-lift-maps},
nous voyons que tout élément $\tau \in \text{Gal}(L/K)$ induit un élément
$\tau|_M \in \text{Gal}(M/K)$, ce qui fournit l'homomorphisme de
droite. L'application de gauche identifie le groupe de gauche au noyau
de la flèche de droite. La suite est exacte parce que les ordres
des groupes coïncident comme il convient, par multiplicativité des degrés
dans les tours d'extensions finies
(Lemme \ref{lemma-multiplicativity-degrees}).
On peut aussi appliquer directement le Lemme \ref{lemma-lift-maps}
pour voir que l'application de droite est surjective.
\end{proof}
```

</details>

## Limites et suite

Analyse assistée par OpenAI Codex. L'identité exacte du modèle et de son effort n'est pas attestée par ces pièces et n'est pas inventée. Ce dossier reste local et ne constitue pas une publication de l'édition restaurée. Pas de certification humaine ni d'attestation exhaustive du registre.

Prochaine section : Théorie de Galois infinie, ligne anglaise 2852 et française 2848. Conserver les vingt et une sections achevées avec leurs réserves. La suite du chapitre, les autres vérifications de fidélité, la reconstruction et la publication cumulative restent à accomplir. L'ancienne édition éditorialisée est préservée comme matériau potentiel d'une édition distincte, pas déjà validée comme traduction de notre édition AI-intégrée.
