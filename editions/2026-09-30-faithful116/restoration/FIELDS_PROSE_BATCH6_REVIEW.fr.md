# Chapitre 9 — Galois infini, nombres complexes, Kummer et Artin–Schreier

**Quatre sections complètes comparées : lignes anglaises 2852–3361, françaises 2848–3354. Une seule réparation grammaticale ; aucune correction mathématique ajoutée. La lecture continue atteint vingt-cinq sections, sans prétendre le chapitre ou l’édition achevés.**

[LaTeX de travail](staged/fr/009_fields.prose-batch6.fr.tex) · [Validation](FIELDS_PROSE_BATCH6_VALIDATION.json) · [Choix et paires](FIELDS_PROSE_BATCH6_CHOICES.json) · [Occurrences](FIELDS_PROSE_BATCH6_OCCURRENCES.json) · [Réparation](FIELDS_PROSE_BATCH6_REPAIR.json) · [Lot précédent](FIELDS_PROSE_BATCH5_REVIEW.fr.md)

## Résultat et périmètre

Tous les énoncés, preuves, transitions et titres de ces quatre sections ont été lus dans les deux langues. Quinze paires disjointes couvrent exactement le périmètre ; un début d'environnement peut relever techniquement de la paire précédente, mais aucun texte n'est omis.

Le gérondif En appliquant était rattaché à aucun polynôme dans la preuve d'Artin–Schreier. D'après répare ce seul défaut de français. Les formules du fichier entier restent inchangées. Le retour inverse retrouve exactement le lot précédent, puis le témoin public après inversion des restaurations antérieures.

Les 371 régions mathématiques du lot concordent après trois traductions exactes du texte lecteur. Le préfixe entier contient 2 432 régions anglaises et 2 433 françaises ; douze exceptions exactes, dont les neuf déjà documentées, expliquent la différence. Ce n'est pas une égalité brute ni un contrôle par masquage général.

## Canon effectivement consulté

[Passages, extraits limités, identités et règles](FIELDS_PROSE_BATCH6_CONSULTED_CANON.json). Consultation rétrospective ; aucune consultation initiale du traducteur ou validation humaine n’est inventée.

### Cours de théorie des corps

Marc Reversat, Benoît Zhang — [Source](https://www.math.univ-toulouse.fr/~reversat/galois.pdf) · [PDF préservé](canon-consulted/fr-fields/reversat-zhang-galois.pdf).

§5.3 complet, définition 5.3.1, Hilbert 90 et théorèmes 5.3.3–5.3.4 avec leurs preuves ; §5.4 complet, théorème 5.4.1, preuve et remarques 5.4.2–5.4.3. Pages imprimées 66–69 / PDF 74–77. Page 67 rendue et inspectée.

La variante adjectivale n'est pas une citation exacte du titre français retenu. Les preuves par Hilbert 90 ne remplacent pas celles de Stacks. Le cours laisse aussi le cas nul implicite dans Kummer, omet un signe dans un produit, emploie n dans une preuve de degré p et abrège la finitude et le corps de base dans 5.4.1. Il sert de témoin linguistique, non de garantie automatique de vérité.

816199 octets ; SHA-256 `73A1D0DCD0B7F11625293615E693B198C0C33BAE3A57C78A705153CE33942E8A`.

### Théorie des nombres

François Charles — [Source](https://www.imo.universite-paris-saclay.fr/~francois.charles/coursTN1920.pdf) · [PDF préservé](canon-consulted/fr-fields/charles-theorie-nombres-20200117.pdf).

Couverture et §1.1.8 complet, pp.37–39 ; pour les choix présents, définitions 1.1.75–1.1.77, proposition 1.1.78, théorème 1.1.79 et remarque 1.1.80, pp.37–38. Page 37 rendue et inspectée.

Le cours annonce les résultats sans preuves. Sa convention définit les extensions infinies par réunion, non dans l'ordre choisi par Stacks. Deux coquilles visibles concernent le corps des automorphismes en 1.1.75 et la base de l'extension fixe en 1.1.79. Elles ne sont pas importées. Distingué y est une variante de normal ; le document ne justifie pas de remplacer la preuve officielle.

779404 octets ; SHA-256 `FB45221BEFCF99AA187BA7C2DB82E00849A2B049779D671ADCA95B0AF33F1F08`.

### Notes du cours de Topologie en M1 ESR UPS 2019

Francesco Costantino — [Source](https://www.math.univ-toulouse.fr/~fcostant/Notes_du_cours_de_Topologie_M1_UPS_2019-Chapitre_1.pdf) · [PDF préservé](canon-consulted/fr-fields/costantino-topologie-m1-2019-ch1.pdf).

§2.7.5, Espaces de fonctions, pp.12–13, lu sur les deux pages complètes ; p.12 rendue et inspectée. L'auteur et le titre sont vérifiés sur la couverture. Les résultats de topologie différentielle visibles p.13 ne sont pas mobilisés.

Attestation du nom et de la définition par images de compacts dans des ouverts, avec variation typographique du trait d'union. Cette définition sur les applications continues ne fournit pas à elle seule la propriété universelle utilisée dans Stacks ; celle-ci garde son renvoi officiel. Aucun théorème d'Ascoli n'est ajouté.

864929 octets ; SHA-256 `3D0016408E2A151C43FF7CBEEADB36CA8804EA06BAEFEAF65E09D83FCE17026C`.

## Points délicats pour une éventuelle revue

Les anomalies anglaises ne sont pas corrigées sous couvert de traduction. Elles ne deviennent pas pour autant des résultats certifiés. La revue humaine est une possibilité ultérieure, pas une condition pour poursuivre.

- `lemma-galois-profinite` : Le polynôme évoqué comme ayant un nombre fini de racines est le polynôme minimal, donc non nul dans ce contexte. Cette qualification implicite n'est pas ajoutée. Aut(E) est le groupe des permutations de l'ensemble discret E ; ne pas le confondre avec Aut(E/F).
- `lemma-infinite-galois-limit` : Limite inductive pour les corps et projective pour les groupes ne sont pas interchangeables. L'attestation lexicale d'ensemble ordonné filtrant n'a pas été obtenue dans les pages effectivement consultées pour ce lot.
- `theorem-inifinite-galois-theory` : FIELDS-028, source 3098 : le quantificateur sur s dans S manque dans U_S(g). La lecture officielle est conservée, l'ancienne correction reste récupérable. Cette fidélité ne certifie pas la formule isolée comme énoncé bien formé.
- `section-complex-numbers` : Les passages de théorie des groupes et le fait que chaque complexe admet une racine carrée restent condensés comme dans Stacks. Le canon français comporte ses propres glissements de finitude et de corps de base ; ils ne sont pas importés.
- `section-Kummer` : FIELDS-035, source 3219 : a appartient à K, sans exclusion de zéro, alors que l'application affichée divise par b. Garder l'ambiguïté source et sa proposition séparée, non ajouter a non nul.
- `lemma-subfields-kummer` : FIELDS-029A/B, source 3305 et 3309 : le signe (-1)^d absent des formules officielles n'est pas réintroduit. Le raisonnement divisant par alpha^d laisse aussi implicite le traitement du cas alpha=0 ; aucune condition supplémentaire n'est insérée. La citation Radical n'a pas été consultée ici comme nouveau canon.
- `lemma-Artin-Schreier` : La réparation est syntaxique : l'application de l'indépendance est faite par le raisonnement, non par aucun polynôme. Elle n'introduit pas une nouvelle étape de preuve et ne corrige pas l'anglais.

## Réparation grammaticale réversible

Le gérondif En appliquant aurait grammaticalement pour sujet aucun polynôme. D'après rattache correctement la conclusion au résultat cité, sans sujet fictif, nouvelle hypothèse ni argument ajouté. L'anglais emploie lui-même une construction participiale condensée ; la traduction n'a pas à reproduire ce défaut de syntaxe.

Avant :

```tex
En appliquant l'indépendance linéaire des caractères
(Lemme \ref{lemma-independence-characters}),
aucun polynôme
```

Après :

```tex
D'après l'indépendance linéaire des caractères
(Lemme \ref{lemma-independence-characters}),
aucun polynôme
```

## Exceptions de comparaison exactes

[Expressions intégrales et positions](FIELDS_PROSE_BATCH6_MATH_EXCEPTIONS.json)

Expression 23 du lot (indice initial zéro).

Traduction bornée du texte lecteur ; symboles, quantificateurs écrits, variables et flèches inchangés. La comparaison n'utilise aucun masquage général.

```tex
G(S) = \{ f : S \to E \mid \begin{matrix} f(\alpha)\text{ is a root of the minimal polynomial}\\ \text{of }\alpha\text{ over }F\text{ for all }\alpha \in S \end{matrix} \}
```

```tex
G(S) = \{ f : S \to E \mid \begin{matrix} f(\alpha)\text{ est une racine du polynôme minimal}\\ \text{de }\alpha\text{ sur }F\text{ pour tout }\alpha \in S \end{matrix} \}
```

Expression 31 du lot (indice initial zéro).

Traduction bornée du texte lecteur ; symboles, quantificateurs écrits, variables et flèches inchangés. La comparaison n'utilise aucun masquage général.

```tex
G = \lim_{S \subset E\text{ finite}} G(S)
```

```tex
G = \lim_{S \subset E\text{ fini}} G(S)
```

Expression 115 du lot (indice initial zéro).

Traduction bornée du texte lecteur ; symboles, quantificateurs écrits, variables et flèches inchangés. La comparaison n'utilise aucun masquage général.

```tex
\{\text{closed subgroups of }G\} \longrightarrow \{\text{subextensions }L/M/K\},\quad H \longmapsto L^H
```

```tex
\{\text{sous-groupes fermés de }G\} \longrightarrow \{\text{extensions intermédiaires }L/M/K\},\quad H \longmapsto L^H
```

Référence optionnelle :

```tex
\cite[Theorem 5.2]{Radical}
\cite[Théorème 5.2]{Radical}
```

Seul le nom du type d'énoncé est traduit ; numéro 5.2 et clé Radical identiques. Aucune substitution de référence.

## Règles et occurrences

### profinite

Profini et limite projective sont attestés ; système projectif désigne ici les restrictions vers les petits sous-corps, sans inversion des flèches.

Occurrences vérifiées : 16. Appui : CHARLES-PROFINITE-B6, 1.1.78, p.37.

### compact-open

Même topologie des applications ; seul le trait d'union diffère du témoin. E est discret dans Stacks.

Occurrences vérifiées : 3. Appui : COSTANTINO-COMPACT-OPEN-B6, §2.7.5, pp.12–13.

### galois-topology

Vérifier pour chaque occurrence le groupe, l'extension intermédiaire et la portée de fermé, ouvert ou discret.

Occurrences vérifiées : 11. Appui : CHARLES-PROFINITE-B6, 1.1.76–1.1.80, pp.37–38.

### directed-colimits

Choix motivés par les définitions et flèches de Stacks ; pas d'attestation lexicale exacte dans les nouvelles pages du canon.

Occurrences vérifiées : 3. Appui : SOURCE-OFFICIAL, lemma-infinite-galois-limit.

### cyclic-extensions

Même classe d'extensions et même nom Artin-Schreier ; de Kummer est la variante par nom propre, non une citation exacte de kummeriennes.

Occurrences vérifiées : 9. Appui : REVERSAT-ZHANG-FIELDS-B6, 5.3.1–5.3.4, pp.66–68.

### roots-unity

La primitivité n'est pas remplacée par la seule propriété d'être une racine de l'unité ; les ordres sont vérifiés dans les formules.

Occurrences vérifiées : 6. Appui : REVERSAT-ZHANG-FIELDS-B6, 5.3.3, p.67.

### complex-field

Clos et 2-sous-groupe de Sylow sont attestés ; quadratique exprime le degré deux du contexte, sans prétendre une citation lexicale exacte dans ces pages.

Occurrences vérifiées : 5. Appui : REVERSAT-ZHANG-FIELDS-B6, 5.4.1 et remarques, pp.68–69.

### exactness-universality

Termes vérifiés sur les définitions et la suite officielle ; absence d'attestation externe exacte dans les pages de ce lot, sans attente de revue humaine.

Occurrences vérifiées : 6. Appui : SOURCE-OFFICIAL, lemma-galois-profinite ; lemma-ses-infinite-galois.

## Toutes les paires comparées

### FR-FIELDS-B6-PROSE-0001

`frontmatter` — source 2852–2852, français 2848–2848.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2852) · [Français de travail](staged/fr/009_fields.prose-batch6.fr.tex)

Le titre annonce la théorie de Galois infinie ; la notation et la portée de la section restent celles de la source.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\section{Infinite Galois theory}
```

```tex
\section{Théorie de Galois infinie}
```

</details>

### FR-FIELDS-B6-PROSE-0002

`section-infinite-galois` — source 2853–2858, français 2849–2854.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2853) · [Français de travail](staged/fr/009_fields.prose-batch6.fr.tex)

L'unique phrase introductive annonce la topologie canonique, sans définition concurrente ni nouvel éponyme.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-infinite-galois}

\noindent
The Galois group comes with a canonical topology.

\begin{lemma}
```

```tex
\label{section-infinite-galois}

\noindent
Le groupe de Galois est muni d'une topologie canonique.

\begin{lemma}
```

</details>

### FR-FIELDS-B6-PROSE-0003

`lemma-galois-profinite` — source 2859–2950, français 2855–2945.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2859) · [Français de travail](staged/fr/009_fields.prose-batch6.fr.tex)

La moins fine rend coarsest ; la topologie discrète porte sur E, non sur le groupe entier. L'espace X de la propriété universelle est quelconque. La preuve conserve toutes ses étapes : topologie des applications, passage aux bijections, injection de Gal, ensembles finis G(S), restrictions, limite projective, puis équations additives et multiplicatives fermées. Aut(E) désigne les bijections de l'espace discret sous-jacent, non uniquement les automorphismes du corps : la précision française explicite le self maps anglais sans renforcer l'énoncé. Les trois types d'applications Map, Aut et Gal ne sont pas confondus. Le caractère non standard de l'ordre de la preuve est conservé. Les phrases françaises autour de G(S) n'ajoutent pas de condition au polynôme minimal. Compacte-ouverte est attesté, à l'espacement près, par Costantino ; profini et limite projective sont attestés par Charles. Les références de Stacks demeurent les justifications mathématiques.

**Réserve :** Le polynôme évoqué comme ayant un nombre fini de racines est le polynôme minimal, donc non nul dans ce contexte. Cette qualification implicite n'est pas ajoutée. Aut(E) est le groupe des permutations de l'ensemble discret E ; ne pas le confondre avec Aut(E/F).

Choix écartés :

- Interpréter Aut(E) comme automorphismes du corps : rejeté, la source parle des applications inversibles de l'espace discret.
- Mettre la topologie discrète sur Gal(E/F) : rejeté, l'adjectif porte sur E.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-galois-profinite}
Let $E/F$ be a Galois extension. Endow $\text{Gal}(E/F)$ with the coarsest
topology such that
$$
\text{Gal}(E/F) \times E \longrightarrow E
$$
is continuous when $E$ is given the discrete topology. Then
\begin{enumerate}
\item for any topological space $X$ and map $X \to \text{Gal}(E/F)$
such that the action $X \times E \to E$ is continuous the induced map
$X \to \text{Gal}(E/F)$ is continuous,
\item this topology turns $\text{Gal}(E/F)$ into
a profinite topological group.
\end{enumerate}
\end{lemma}

\begin{proof}
Throughout this proof we think of $E$ as a discrete topological space.
Recall that the compact open topology on the set of self maps
$\text{Map}(E, E)$ is the universal topology such that the action
$\text{Map}(E, E) \times E \to E$ is continuous. See
Topology, Example \ref{topology-example-automorphisms-of-a-set}
for a precise statement. The topology of the lemma on
$\text{Gal}(E/F)$ is the induced topology coming from the
injective map $\text{Gal}(E/F) \to \text{Map}(E, E)$.
Hence the universal property (1) follows from the corresponding
universal property of the compact open topology.
Since the set of invertible self maps $\text{Aut}(E)$
endowed with the compact open topology forms a topological group, see
Topology, Example \ref{topology-example-automorphisms-of-a-set},
and since $\text{Gal}(E/F) = \text{Aut}(E/F) \to \text{Map}(E, E)$
factors through $\text{Aut}(E)$ we obtain a topological group.
In other words, we are using the injection
$$
\text{Gal}(E/F) \subset \text{Aut}(E)
$$
to endow $\text{Gal}(E/F)$ with the induced structure of a topological group
(see Topology, Section \ref{topology-section-topological-groups})
and by construction this is the coarsest structure of a topological
group such that the action $\text{Gal}(E/F) \times E \to E$ is continuous.

\medskip\noindent
To show that $\text{Gal}(E/F)$ is profinite we argue as follows
(our argument is necessarily nonstandard because we have defined
the topology before showing that the Galois group is an inverse
limit of finite groups).
By Topology, Lemma \ref{topology-lemma-profinite-group}
it suffices to show that the underlying
topological space of $\text{Gal}(E/F)$ is profinite.
For any subset $S \subset E$ consider the set
$$
G(S) = \{ f : S \to E \mid
\begin{matrix}
f(\alpha)\text{ is a root of the minimal polynomial}\\
\text{of }\alpha\text{ over }F\text{ for all }\alpha \in S
\end{matrix}
\}
$$
Since a polynomial has only a finite number of roots we see that
$G(S)$ is finite for all $S \subset E$ finite. If $S \subset S'$
then restriction gives a map $G(S') \to G(S)$. Also, observe
that if $\alpha \in S \cap F$ and $f \in G(S)$, then $f(\alpha) = \alpha$
because the minimal polynomial is linear in this case.
Consider the profinite topological space
$$
G = \lim_{S \subset E\text{ finite}} G(S)
$$
Consider the canonical map
$$
c : \text{Gal}(E/F) \longrightarrow G,\quad
\sigma \longmapsto (\sigma|_S : S \to E)_S
$$
This is injective and unwinding the definitions the
reader sees the topology on $\text{Gal}(E/F)$ as defined above
is the induced topology from $G$. An element $(f_S) \in G$ is in
the image of $c$ exactly if
(A) $f_S(\alpha) + f_S(\beta) = f_S(\alpha + \beta)$ and
(M) $f_S(\alpha)f_S(\beta) = f_S(\alpha\beta)$ whenever
this makes sense (i.e.,
$\alpha, \beta, \alpha + \beta, \alpha\beta \in S$).
Namely, this means
$\lim f_S : E \to E$ will be an $F$-algebra map
and hence an automorphism by
Lemma \ref{lemma-algebraic-extension-self-map}.
The conditions (A) and (M) for a given triple
$(S, \alpha, \beta)$ define a closed subset of
$G$ and hence $\text{Gal}(E/F)$ is homeomorphic
to a closed subset of a profinite space and therefore
profinite itself.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-galois-profinite}
Soit $E/F$ une extension galoisienne. Munissons $\text{Gal}(E/F)$ de la topologie
la moins fine telle que
$$
\text{Gal}(E/F) \times E \longrightarrow E
$$
soit continue lorsque $E$ est muni de la topologie discrète. Alors
\begin{enumerate}
\item pour tout espace topologique $X$ et toute application $X \to \text{Gal}(E/F)$
tels que l'action $X \times E \to E$ soit continue, l'application induite
$X \to \text{Gal}(E/F)$ est continue,
\item cette topologie fait de $\text{Gal}(E/F)$
un groupe topologique profini.
\end{enumerate}
\end{lemma}

\begin{proof}
Dans toute cette démonstration, nous considérons $E$ comme un espace topologique discret.
Rappelons que la topologie compacte-ouverte sur l'ensemble des applications d'un ensemble dans lui-même
$\text{Map}(E, E)$ est la topologie universelle telle que l'action
$\text{Map}(E, E) \times E \to E$ soit continue. Voir
Topologie, Exemple \ref{topology-example-automorphisms-of-a-set}
pour un énoncé précis. La topologie du lemme sur
$\text{Gal}(E/F)$ est la topologie induite par l'application injective
$\text{Gal}(E/F) \to \text{Map}(E, E)$.
La propriété universelle (1) découle donc de la propriété universelle
correspondante de la topologie compacte-ouverte.
Comme l'ensemble des applications bijectives de l'espace discret considéré, $\text{Aut}(E)$,
muni de la topologie compacte-ouverte, forme un groupe topologique, voir
Topologie, Exemple \ref{topology-example-automorphisms-of-a-set},
et comme $\text{Gal}(E/F) = \text{Aut}(E/F) \to \text{Map}(E, E)$
se factorise par $\text{Aut}(E)$, nous obtenons un groupe topologique.
Autrement dit, nous utilisons l'injection
$$
\text{Gal}(E/F) \subset \text{Aut}(E)
$$
pour munir $\text{Gal}(E/F)$ de la structure induite de groupe topologique
(voir Topologie, section \ref{topology-section-topological-groups})
et, par construction, il s'agit de la structure de groupe topologique
la moins fine pour laquelle l'action $\text{Gal}(E/F) \times E \to E$ est continue.

\medskip\noindent
Pour montrer que $\text{Gal}(E/F)$ est profini, nous raisonnons comme suit
(notre argument est nécessairement non standard, car nous avons défini
la topologie avant de montrer que le groupe de Galois est une limite
projective de groupes finis).
D'après Topologie, Lemme \ref{topology-lemma-profinite-group},
il suffit de montrer que l'espace topologique
sous-jacent à $\text{Gal}(E/F)$ est profini.
Pour toute partie $S \subset E$, considérons l'ensemble
$$
G(S) = \{ f : S \to E \mid
\begin{matrix}
f(\alpha)\text{ est une racine du polynôme minimal}\\
\text{de }\alpha\text{ sur }F\text{ pour tout }\alpha \in S
\end{matrix}
\}
$$
Comme un polynôme n'a qu'un nombre fini de racines, nous voyons que
$G(S)$ est fini pour toute partie finie $S \subset E$. Si $S \subset S'$,
la restriction fournit une application $G(S') \to G(S)$. Observons également
que si $\alpha \in S \cap F$ et $f \in G(S)$, alors $f(\alpha) = \alpha$
car le polynôme minimal est linéaire dans ce cas.
Considérons l'espace topologique profini
$$
G = \lim_{S \subset E\text{ fini}} G(S)
$$
Considérons l'application canonique
$$
c : \text{Gal}(E/F) \longrightarrow G,\quad
\sigma \longmapsto (\sigma|_S : S \to E)_S
$$
Elle est injective et, en explicitant les définitions, le lecteur constate
que la topologie sur $\text{Gal}(E/F)$ définie ci-dessus
est la topologie induite par $G$. Un élément $(f_S) \in G$ appartient à
l'image de $c$ exactement lorsque
(A) $f_S(\alpha) + f_S(\beta) = f_S(\alpha + \beta)$ et
(M) $f_S(\alpha)f_S(\beta) = f_S(\alpha\beta)$ chaque fois que
ces expressions ont un sens (c'est-à-dire lorsque
$\alpha, \beta, \alpha + \beta, \alpha\beta \in S$).
En effet, cela signifie que
$\lim f_S : E \to E$ sera un morphisme de $F$-algèbres,
et donc un automorphisme d'après le
Lemme \ref{lemma-algebraic-extension-self-map}.
Les conditions (A) et (M) pour un triplet donné
$(S, \alpha, \beta)$ définissent un fermé de
$G$ ; ainsi $\text{Gal}(E/F)$ est homéomorphe
à un fermé d'un espace profini, et est donc lui-même profini.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B6-PROSE-0004

`lemma-galois-infinite` — source 2951–2979, français 2946–2974.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2951) · [Français de travail](staged/fr/009_fields.prose-batch6.fr.tex)

Les deux étages L/K et M/K, non uniquement L/M, restent galoisiens. La restriction fournit le même homomorphisme surjectif continu. L'action sur M sert à démontrer la continuité par la même propriété universelle ; la dernière phrase conserve la preuve séparée de surjectivité. L'ordre des adjectifs français ne change pas leurs portées. Le passage à la présentation classique est conservé.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-galois-infinite}
Let $L/M/K$ be a tower of fields. Assume both $L/K$ and
$M/K$ are Galois. Then there is a canonical surjective continuous
homomorphism $c : \text{Gal}(L/K) \to \text{Gal}(M/K)$.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-lift-maps} given $\tau : L \to L$ in
$\text{Gal}(L/K)$ the restriction $\tau|_M : M \to M$
is an element of $\text{Gal}(M/K)$. This defines the homomorphism $c$.
Continuity follows from the universal property of the topology:
the action
$$
\text{Gal}(L/K) \times M \longrightarrow M,\quad
(\tau, x) \longmapsto \tau(x) = c(\tau)(x)
$$
is continuous as $M \subset L$ and the action
$\text{Gal}(L/K) \times L \to L$ is continuous.
Hence continuity of $c$ by part (1) of
Lemma \ref{lemma-galois-profinite}.
Lemma \ref{lemma-lift-maps} also
shows that the map is surjective.
\end{proof}

\noindent
Here is a more standard way to think about
the Galois group of an infinite Galois extension.

\begin{lemma}
```

```tex
\label{lemma-galois-infinite}
Soit $L/M/K$ une tour de corps. Supposons que $L/K$ et
$M/K$ soient toutes deux galoisiennes. Alors il existe un homomorphisme canonique
continu surjectif $c : \text{Gal}(L/K) \to \text{Gal}(M/K)$.
\end{lemma}

\begin{proof}
D'après le Lemme \ref{lemma-lift-maps}, pour $\tau : L \to L$ appartenant à
$\text{Gal}(L/K)$, la restriction $\tau|_M : M \to M$
est un élément de $\text{Gal}(M/K)$. Cela définit l'homomorphisme $c$.
La continuité découle de la propriété universelle de la topologie :
l'action
$$
\text{Gal}(L/K) \times M \longrightarrow M,\quad
(\tau, x) \longmapsto \tau(x) = c(\tau)(x)
$$
est continue puisque $M \subset L$ et que l'action
$\text{Gal}(L/K) \times L \to L$ est continue.
La continuité de $c$ résulte donc de la partie (1) du
Lemme \ref{lemma-galois-profinite}.
Le Lemme \ref{lemma-lift-maps} montre également
que l'application est surjective.
\end{proof}

\noindent
Voici une manière plus classique de considérer
le groupe de Galois d'une extension galoisienne infinie.

\begin{lemma}
```

</details>

### FR-FIELDS-B6-PROSE-0005

`lemma-infinite-galois-limit` — source 2980–3053, français 2975–3048.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L2980) · [Français de travail](staged/fr/009_fields.prose-batch6.fr.tex)

L'ensemble ordonné filtrant garde l'ordre par inclusion des sous-corps : les corps forment un système inductif, les groupes un système projectif avec flèches de restriction dans le sens opposé. Toutes les assertions, y compris non-vacuité, cofinalité sur les parties finies, surjectivité des transitions et des projections, sont présentes. La preuve de la dernière identification distingue la bijection ensembliste, la continuité, puis l'homéomorphisme des espaces profinis. Foncteur d'oubli n'est pas traduit par effacement de structure dans le raisonnement. La locution filtrant est motivée par la définition citée ; les pages françaises consultées ici attestent projectif, pas cette locution exacte.

**Réserve :** Limite inductive pour les corps et projective pour les groupes ne sont pas interchangeables. L'attestation lexicale d'ensemble ordonné filtrant n'a pas été obtenue dans les pages effectivement consultées pour ce lot.

Choix écartés :

- Employer système inductif pour les groupes : rejeté, inversion des flèches de restriction.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-infinite-galois-limit}
Let $L/K$ be a Galois extension with Galois group $G$.
Let $\Lambda$ be the set of finite Galois subextensions,
i.e., $\lambda \in \Lambda$ corresponds to $L/L_\lambda/K$
with $L_\lambda/K$ finite Galois with Galois group $G_\lambda$.
Define a partial ordering on $\Lambda$ by the rule
$\lambda \geq \lambda'$ if and only if
$L_\lambda \supset L_{\lambda'}$. Then
\begin{enumerate}
\item $\Lambda$ is a directed partially ordered set,
\item $L_\lambda$ is a system of $K$-extensions over $\Lambda$
and $L = \colim L_\lambda$,
\item $G_\lambda$ is an inverse system of finite groups over $\Lambda$,
the transition maps are surjective, and
$$
G = \lim_{\lambda \in \Lambda} G_\lambda
$$
as a profinite group, and
\item each of the projections $G \to G_\lambda$ is continuous and surjective.
\end{enumerate}
\end{lemma}

\begin{proof}
Every subfield of $L$ containing $K$ is separable over $K$
(follows immediately from the definition). Let $S \subset L$
be a finite subset. Then $K(S)/K$ is finite and there exists
a tower $L/E/K(S)/K$ such that $E/K$ is finite Galois, see
Lemma \ref{lemma-normal-closure-inside-normal}.
Hence $E = L_\lambda$ for some $\lambda \in \Lambda$.
This certainly implies the set $\Lambda$ is not empty.
Also, given $\lambda_1, \lambda_2 \in \Lambda$ we can
write $L_{\lambda_i} = K(S_i)$ for finite sets
$S_1, S_2 \subset L$ (Lemma \ref{lemma-finite-finitely-generated}).
Then there exists a $\lambda \in \Lambda$ such that
$K(S_1 \cup S_2) \subset L_\lambda$. Hence
$\lambda \geq \lambda_1, \lambda_2$ and
$\Lambda$ is directed (Categories, Definition
\ref{categories-definition-directed-system}).
Finally, since every element in $L$ is contained in
$L_\lambda$ for some $\lambda \in \Lambda$, it follows
from the description of filtered colimits in
Categories, Section \ref{categories-section-directed-colimits}
that $\colim L_\lambda = L$.

\medskip\noindent
If $\lambda \geq \lambda'$ in $\Lambda$, then we obtain a
canonical surjective map $G_\lambda \to G_{\lambda'}$,
$\sigma \mapsto \sigma|_{L_{\lambda'}}$
by Lemma \ref{lemma-ses-galois}. Thus we get an inverse
system of finite groups with surjective transition maps.

\medskip\noindent
Recall that $G = \text{Aut}(L/K)$. By Lemma \ref{lemma-galois-infinite}
the restriction $\sigma|_{L_\lambda}$ of a $\sigma \in G$ to $L_\lambda$
is an element of $G_\lambda$. Moreover, this procedure gives a continuous
surjection $G \to G_\lambda$. Since the transition mappings
in the inverse system of $G_\lambda$ are given by restriction
also, it is clear that we obtain a canonical continuous map
$$
G \longrightarrow \lim_{\lambda \in \Lambda} G_\lambda
$$
Continuity by definition of limits in the category of topological
groups; recall that these limits commute with the forgetful functor
to the categories of sets and topological spaces by
Topology, Lemma \ref{topology-lemma-topological-group-limits}.
On the other hand, since $L = \colim L_\lambda$ it is clear
that any element of the inverse limit (viewed as a set) defines an
automorphism of $L$. Thus the map is bijective. Since the topology
on both sides is profinite, and since a bijective continuous map
of profinite spaces is a homeomorphism
(Topology, Lemma \ref{topology-lemma-bijective-map}), the proof is complete.
\end{proof}

\begin{theorem}[Fundamental theorem of infinite Galois theory]
```

```tex
\label{lemma-infinite-galois-limit}
Soit $L/K$ une extension galoisienne de groupe de Galois $G$.
Soit $\Lambda$ l'ensemble des extensions intermédiaires finies galoisiennes,
c'est-à-dire que $\lambda \in \Lambda$ correspond à $L/L_\lambda/K$,
où $L_\lambda/K$ est finie galoisienne de groupe de Galois $G_\lambda$.
Définissons un ordre partiel sur $\Lambda$ par la règle
$\lambda \geq \lambda'$ si et seulement si
$L_\lambda \supset L_{\lambda'}$. Alors
\begin{enumerate}
\item $\Lambda$ est un ensemble ordonné filtrant,
\item les $L_\lambda$ forment un système d'extensions de $K$ indexé par $\Lambda$
et $L = \colim L_\lambda$,
\item les $G_\lambda$ forment un système projectif de groupes finis indexé par $\Lambda$,
les morphismes de transition sont surjectifs, et
$$
G = \lim_{\lambda \in \Lambda} G_\lambda
$$
comme groupe profini, et
\item chacune des projections $G \to G_\lambda$ est continue et surjective.
\end{enumerate}
\end{lemma}

\begin{proof}
Tout sous-corps de $L$ contenant $K$ est séparable sur $K$
(cela résulte immédiatement de la définition). Soit $S \subset L$
une partie finie. Alors $K(S)/K$ est finie et il existe
une tour $L/E/K(S)/K$ telle que $E/K$ soit finie galoisienne, voir le
Lemme \ref{lemma-normal-closure-inside-normal}.
Ainsi $E = L_\lambda$ pour un certain $\lambda \in \Lambda$.
Cela implique en particulier que l'ensemble $\Lambda$ n'est pas vide.
De plus, étant donnés $\lambda_1, \lambda_2 \in \Lambda$, nous pouvons
écrire $L_{\lambda_i} = K(S_i)$ pour des ensembles finis
$S_1, S_2 \subset L$ (Lemme \ref{lemma-finite-finitely-generated}).
Il existe alors un $\lambda \in \Lambda$ tel que
$K(S_1 \cup S_2) \subset L_\lambda$. Par conséquent,
$\lambda \geq \lambda_1, \lambda_2$ et
$\Lambda$ est filtrant (Catégories, Définition
\ref{categories-definition-directed-system}).
Enfin, puisque tout élément de $L$ appartient à
$L_\lambda$ pour un certain $\lambda \in \Lambda$, il résulte
de la description des limites inductives filtrantes dans
Catégories, section \ref{categories-section-directed-colimits},
que $\colim L_\lambda = L$.

\medskip\noindent
Si $\lambda \geq \lambda'$ dans $\Lambda$, nous obtenons une
application canonique surjective $G_\lambda \to G_{\lambda'}$,
$\sigma \mapsto \sigma|_{L_{\lambda'}}$,
d'après le Lemme \ref{lemma-ses-galois}. Nous obtenons ainsi un système
projectif de groupes finis dont les morphismes de transition sont surjectifs.

\medskip\noindent
Rappelons que $G = \text{Aut}(L/K)$. D'après le Lemme \ref{lemma-galois-infinite},
la restriction $\sigma|_{L_\lambda}$ d'un $\sigma \in G$ à $L_\lambda$
est un élément de $G_\lambda$. De plus, ce procédé fournit une surjection
continue $G \to G_\lambda$. Puisque les morphismes de transition
du système projectif des $G_\lambda$ sont eux aussi donnés par restriction,
il est clair que nous obtenons une application continue canonique
$$
G \longrightarrow \lim_{\lambda \in \Lambda} G_\lambda
$$
La continuité résulte de la définition des limites dans la catégorie des groupes
topologiques ; rappelons que ces limites commutent avec le foncteur d'oubli
vers les catégories des ensembles et des espaces topologiques d'après
Topologie, Lemme \ref{topology-lemma-topological-group-limits}.
D'autre part, puisque $L = \colim L_\lambda$, il est clair
que tout élément de la limite projective (considérée comme un ensemble) définit un
automorphisme de $L$. L'application est donc bijective. Comme la topologie
des deux membres est profinie et qu'une application continue bijective
entre espaces profinis est un homéomorphisme
(Topologie, Lemme \ref{topology-lemma-bijective-map}), la démonstration est achevée.
\end{proof}

\begin{theorem}[Théorème fondamental de la théorie de Galois infinie]
```

</details>

### FR-FIELDS-B6-PROSE-0006

`theorem-inifinite-galois-theory` — source 3054–3136, français 3049–3131.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3054) · [Français de travail](staged/fr/009_fields.prose-batch6.fr.tex)

La correspondance garde les sous-groupes fermés, les extensions intermédiaires quelconques, puis ouverts/finies et fermés normaux/galoisiennes. L'identifiant source mal orthographié est inchangé. Chaque paragraphe de preuve est conservé : union des extensions finies galoisiennes, invariants, sous-groupe fermé associé à M, réciproque par voisinages et fermeture, cas ouvert, noyau d'une restriction, puis cas normal par images finies. Ici g fixe L^H point par point : contrairement à la stabilité ensembliste discutée au lot précédent, fixe est correct pour un élément du groupe de Galois de L/L^H. La formule U_S(g) reste la formule officielle, sans le quantificateur ajouté dans l'ancienne édition. La réunion finale n'est pas remplacée par une nouvelle preuve. Charles atteste le vocabulaire de la correspondance mais emploie distingué, non normal, pour le sous-groupe.

**Réserve :** FIELDS-028, source 3098 : le quantificateur sur s dans S manque dans U_S(g). La lecture officielle est conservée, l'ancienne correction reste récupérable. Cette fidélité ne certifie pas la formule isolée comme énoncé bien formé.

Choix écartés :

- Compléter le quantificateur de U_S(g) : mathématiquement motivé mais exclu de la traduction diplomatique.
- Traduire fixe L^H par stabilise L^H : insuffisant ici, où la fixation est point par point.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{theorem-inifinite-galois-theory}
Let $L/K$ be a Galois extension. Let $G = \text{Gal}(L/K)$
be the Galois group viewed as a profinite topological group
(Lemma \ref{lemma-galois-profinite}). Then we have $K = L^G$ and the map
$$
\{\text{closed subgroups of }G\}
\longrightarrow
\{\text{subextensions }L/M/K\},\quad
H \longmapsto L^H
$$
is a bijection whose inverse maps $M$ to $\text{Gal}(L/M)$.
The finite subextensions $M$ correspond exactly to the open
subgroups $H \subset G$. The normal closed subgroups $H$ of $G$
correspond exactly to subextensions $M$ Galois over $K$.
\end{theorem}

\begin{proof}
We will use the result of finite Galois theory
(Theorem \ref{theorem-galois-theory})
without further mention.
Let $S \subset L$ be a finite subset. There exists a tower
$L/E/K$ such that $K(S) \subset E$ and such that
$E/K$ is finite Galois, see Lemma \ref{lemma-normal-closure-inside-normal}.
In other words, we see that $L/K$ is the union of its finite
Galois subextensions.
For such an $E$, by Lemma \ref{lemma-galois-infinite}
the map $\text{Gal}(L/K) \to \text{Gal}(E/K)$ is surjective
and continuous, i.e., the kernel is open because the topology
on $\text{Gal}(E/K)$ is discrete.
In particular we see that no element of $L \setminus K$ is fixed by
$\text{Gal}(L/K)$ as $E^{\text{Gal}(E/K)} = K$.
This proves that $L^G = K$.

\medskip\noindent
By Lemma \ref{lemma-galois-goes-up} given a subextension $L/M/K$
the extension $L/M$ is Galois. It is immediate from the definition
of the topology on $G$ that the subgroup $\text{Gal}(L/M)$ is closed.
By the above applied to $L/M$ we see that $L^{\text{Gal}(L/M)} = M$.

\medskip\noindent
Conversely, let $H \subset G$ be a closed subgroup. We claim that
$H = \text{Gal}(L/L^H)$. The inclusion $H \subset \text{Gal}(L/L^H)$
is clear. Suppose that $g \in \text{Gal}(L/L^H)$. Let $S \subset L$
be a finite subset. We will show that the open neighbourhood
$U_S(g) = \{g' \in G \mid g'(s) = g(s)\}$ of $g$ meets $H$.
This implies that $g \in H$ because $H$ is closed.
Let $L/E/K$ be a finite Galois subextension containing $K(S)$
as in the first paragraph of the proof and consider the homomorphism
$c : \text{Gal}(L/K) \to \text{Gal}(E/K)$.
Then $L^H \cap E = E^{c(H)}$. Since $g$ fixes $L^H$ it fixes
$E^{c(H)}$ and hence $c(g) \in c(H)$ by finite Galois theory.
Pick $h \in H$ with $c(h) = c(g)$. Then $h \in U_S(g)$ as desired.

\medskip\noindent
At this point we have established the correspondence between closed
subgroups and subextensions.

\medskip\noindent
Assume $H \subset G$ is open. Arguing as above we find that
$H$ contains $\text{Gal}(L/E)$ for some large enough finite
Galois subextension $E$ and we find that $L^H$ is contained
in $E$ whence finite over $K$. Conversely, if $M$ is a finite
subextension, then $M$ is generated by a finite subset $S$
and the corresponding subgroup is the open subset $U_S(e)$
where $e \in G$ is the neutral element.

\medskip\noindent
Assume that $K \subset M \subset L$ with $M/K$ Galois.
By Lemma \ref{lemma-galois-infinite} there is a surjective
continuous homomorphism of Galois groups
$\text{Gal}(L/K) \to \text{Gal}(M/K)$ whose
kernel is $\text{Gal}(L/M)$. Thus $\text{Gal}(L/M)$ is a normal
closed subgroup.

\medskip\noindent
Finally, assume $N \subset G$ is normal and closed. For any
$L/E/K$ as in the first paragraph of the proof, the image
$c(N) \subset \text{Gal}(E/K)$ is a normal subgroup.
Hence $L^N = \bigcup E^{c(N)}$ is a union of Galois extensions
of $K$ (by finite Galois theory) whence Galois over $K$.
\end{proof}

\begin{lemma}
```

```tex
\label{theorem-inifinite-galois-theory}
Soit $L/K$ une extension galoisienne. Soit $G = \text{Gal}(L/K)$
le groupe de Galois considéré comme un groupe topologique profini
(Lemme \ref{lemma-galois-profinite}). Alors $K = L^G$ et l'application
$$
\{\text{sous-groupes fermés de }G\}
\longrightarrow
\{\text{extensions intermédiaires }L/M/K\},\quad
H \longmapsto L^H
$$
est une bijection dont l'inverse envoie $M$ sur $\text{Gal}(L/M)$.
Les extensions intermédiaires finies $M$ correspondent exactement aux sous-groupes
ouverts $H \subset G$. Les sous-groupes fermés normaux $H$ de $G$
correspondent exactement aux extensions intermédiaires $M$ galoisiennes sur $K$.
\end{theorem}

\begin{proof}
Nous utiliserons le résultat de la théorie de Galois finie
(Théorème \ref{theorem-galois-theory})
sans autre mention.
Soit $S \subset L$ une partie finie. Il existe une tour
$L/E/K$ telle que $K(S) \subset E$ et que
$E/K$ soit finie galoisienne, voir le Lemme \ref{lemma-normal-closure-inside-normal}.
Autrement dit, $L/K$ est la réunion de ses extensions intermédiaires
finies galoisiennes.
Pour un tel $E$, d'après le Lemme \ref{lemma-galois-infinite},
l'application $\text{Gal}(L/K) \to \text{Gal}(E/K)$ est surjective
et continue, c'est-à-dire que son noyau est ouvert puisque la topologie
sur $\text{Gal}(E/K)$ est discrète.
En particulier, aucun élément de $L \setminus K$ n'est fixé par
$\text{Gal}(L/K)$, car $E^{\text{Gal}(E/K)} = K$.
Cela prouve que $L^G = K$.

\medskip\noindent
D'après le Lemme \ref{lemma-galois-goes-up}, pour toute extension intermédiaire $L/M/K$,
l'extension $L/M$ est galoisienne. Il résulte immédiatement de la définition
de la topologie sur $G$ que le sous-groupe $\text{Gal}(L/M)$ est fermé.
En appliquant ce qui précède à $L/M$, nous voyons que $L^{\text{Gal}(L/M)} = M$.

\medskip\noindent
Réciproquement, soit $H \subset G$ un sous-groupe fermé. Nous affirmons que
$H = \text{Gal}(L/L^H)$. L'inclusion $H \subset \text{Gal}(L/L^H)$
est claire. Supposons que $g \in \text{Gal}(L/L^H)$. Soit $S \subset L$
une partie finie. Nous allons montrer que le voisinage ouvert
$U_S(g) = \{g' \in G \mid g'(s) = g(s)\}$ de $g$ rencontre $H$.
Cela implique que $g \in H$, puisque $H$ est fermé.
Soit $L/E/K$ une extension intermédiaire finie galoisienne contenant $K(S)$,
comme dans le premier paragraphe de la démonstration, et considérons l'homomorphisme
$c : \text{Gal}(L/K) \to \text{Gal}(E/K)$.
Alors $L^H \cap E = E^{c(H)}$. Puisque $g$ fixe $L^H$, il fixe
$E^{c(H)}$ et donc $c(g) \in c(H)$ par la théorie de Galois finie.
Choisissons $h \in H$ tel que $c(h) = c(g)$. Alors $h \in U_S(g)$, comme voulu.

\medskip\noindent
À ce stade, nous avons établi la correspondance entre sous-groupes fermés
et extensions intermédiaires.

\medskip\noindent
Supposons $H \subset G$ ouvert. En raisonnant comme ci-dessus, nous voyons que
$H$ contient $\text{Gal}(L/E)$ pour une extension intermédiaire finie
galoisienne $E$ assez grande, et que $L^H$ est contenu
dans $E$, donc fini sur $K$. Réciproquement, si $M$ est une extension
intermédiaire finie, alors $M$ est engendré par une partie finie $S$,
et le sous-groupe correspondant est l'ouvert $U_S(e)$,
où $e \in G$ est l'élément neutre.

\medskip\noindent
Supposons que $K \subset M \subset L$ et que $M/K$ soit galoisienne.
D'après le Lemme \ref{lemma-galois-infinite}, il existe un homomorphisme surjectif
continu de groupes de Galois
$\text{Gal}(L/K) \to \text{Gal}(M/K)$ dont le
noyau est $\text{Gal}(L/M)$. Ainsi $\text{Gal}(L/M)$ est un sous-groupe
fermé normal.

\medskip\noindent
Enfin, supposons $N \subset G$ normal et fermé. Pour toute
extension intermédiaire $L/E/K$ comme dans le premier paragraphe de la démonstration, l'image
$c(N) \subset \text{Gal}(E/K)$ est un sous-groupe normal.
Par conséquent, $L^N = \bigcup E^{c(N)}$ est une réunion d'extensions galoisiennes
de $K$ (par la théorie de Galois finie), et est donc galoisienne sur $K$.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B6-PROSE-0007

`lemma-ses-infinite-galois` — source 3137–3155, français 3132–3149.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3137) · [Français de travail](staged/fr/009_fields.prose-batch6.fr.tex)

La suite exacte courte est conservée avec ses quatre flèches, son noyau et les topologies profinies. La preuve reste un renvoi, sans développement importé du canon. Le mot courte est vérifié sur cette suite précise ; aucune attestation lexicale indépendante de cette locution dans les pages nouvelles n'est revendiquée. Le titre de la section suivante appartient au découpage mais ne modifie pas ce lemme.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-ses-infinite-galois}
Let $L/M/K$ be a tower of fields. Assume $L/K$ and $M/K$ are Galois.
Then we obtain a short exact sequence
$$
1 \to \text{Gal}(L/M) \to \text{Gal}(L/K) \to \text{Gal}(M/K) \to 1
$$
of profinite topological groups.
\end{lemma}

\begin{proof}
This is a reformulation of Lemma \ref{lemma-galois-infinite}.
\end{proof}






\section{The complex numbers}
```

```tex
\label{lemma-ses-infinite-galois}
Soit $L/M/K$ une tour de corps. Supposons $L/K$ et $M/K$ galoisiennes.
Alors nous obtenons une suite exacte courte
$$
1 \to \text{Gal}(L/M) \to \text{Gal}(L/K) \to \text{Gal}(M/K) \to 1
$$
de groupes topologiques profinis.
\end{lemma}

\begin{proof}
C'est une reformulation du Lemme \ref{lemma-galois-infinite}.
\end{proof}





\section{Les nombres complexes}
```

</details>

### FR-FIELDS-B6-PROSE-0008

`section-complex-numbers` — source 3156–3201, français 3150–3194.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3156) · [Français de travail](staged/fr/009_fields.prose-batch6.fr.tex)

Calculus est rendu par résultats d'analyse, et non par calcul formel. La preuve complète reste celle de Stacks : signe à l'infini, valeurs intermédiaires, absence d'extension impaire non triviale, 2-Sylow, 2-groupe, unique extension quadratique réelle, puis racines carrées complexes et clôture normale. Aucune démonstration du théorème de Sylow ni des racines carrées n'est importée. Le passage de groupe non trivial à C contenu dans K demeure à isomorphisme près. Reversat–Zhang atteste le même vocabulaire de 2-sous-groupe de Sylow, sans fournir l'autorité pour modifier les phrases anglaises.

**Réserve :** Les passages de théorie des groupes et le fait que chaque complexe admet une racine carrée restent condensés comme dans Stacks. Le canon français comporte ses propres glissements de finitude et de corps de base ; ils ne sont pas importés.

Choix écartés :

- Remplacer le titre du lemme par un éponyme absent de Stacks : non nécessaire pour traduire fidèlement.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-complex-numbers}

\noindent
The fundamental theorem of algebra states that the field of complex numbers
is an algebraically closed field. In this section we discuss this
briefly.

\medskip\noindent
The first remark we'd like to make is that you need to use a little
bit of input from calculus in order to prove this. We will use the
intuitively clear fact that every odd degree polynomial over
the reals has a real root. Namely, let
$P(x) = a_{2k + 1} x^{2k + 1} + \ldots + a_0 \in \mathbf{R}[x]$
for some $k \geq 0$ and $a_{2k + 1} \not = 0$.
We may and do assume $a_{2k + 1} > 0$. Then for $x \in \mathbf{R}$
very large (positive) we see that $P(x) > 0$ as the term
$a_{2k + 1} x^{2k + 1}$ dominates all the other terms. Similarly,
if $x \ll 0$, then $P(x) < 0$ by the same reason (and this is where
we use that the degree is odd). Hence by the intermediate value
theorem there is an $x \in \mathbf{R}$ with $P(x) = 0$.

\medskip\noindent
A conclusion we can draw from the above is that $\mathbf{R}$ has
no nontrivial odd degree field extensions, as elements of such extensions
would have odd degree minimal polynomials.

\medskip\noindent
Next, let $K/\mathbf{R}$ be a finite Galois extension with Galois group $G$.
Let $P \subset G$ be a $2$-sylow subgroup. Then $K^P/\mathbf{R}$ is an
odd degree extension, hence by the above $K^P = \mathbf{R}$,
which in turn implies
$G = P$. (All of these arguments rely on Galois theory of course.)
Thus $G$ is a $2$-group. If $G$ is nontrivial, then we see that
$\mathbf{C} \subset K$ as $\mathbf{C}$ is (up to isomorphism) the only
degree $2$ extension of $\mathbf{R}$. If $G$ has more than $2$ elements
we would obtain a quadratic extension of $\mathbf{C}$.
This is absurd as every complex number has a square root.

\medskip\noindent
The conclusion: $\mathbf{C}$ is algebraically closed. Namely, if not
then we'd get a nontrivial finite extension $K/\mathbf{C}$
which we could assume normal (hence Galois) over $\mathbf{R}$ by
Lemma \ref{lemma-normal-closure}. But we've seen above that then
$K = \mathbf{C}$.

\begin{lemma}[Fundamental theorem of algebra]
```

```tex
\label{section-complex-numbers}

\noindent
Le théorème fondamental de l'algèbre affirme que le corps des nombres complexes
est algébriquement clos. Nous en discutons brièvement dans cette section.

\medskip\noindent
La première remarque que nous souhaitons faire est qu'il faut utiliser quelques
résultats d'analyse pour le démontrer. Nous utiliserons le fait intuitivement
clair que tout polynôme de degré impair à coefficients réels possède une racine réelle.
En effet, soit
$P(x) = a_{2k + 1} x^{2k + 1} + \ldots + a_0 \in \mathbf{R}[x]$
pour un certain $k \geq 0$ et avec $a_{2k + 1} \not = 0$.
Nous pouvons supposer, et supposons, que $a_{2k + 1} > 0$. Alors, pour
$x \in \mathbf{R}$ positif et très grand, nous avons $P(x) > 0$, car le terme
$a_{2k + 1} x^{2k + 1}$ domine tous les autres termes. De même,
si $x \ll 0$, alors $P(x) < 0$ pour la même raison (et c'est ici
que nous utilisons que le degré est impair). Le théorème des valeurs
intermédiaires donne donc un $x \in \mathbf{R}$ tel que $P(x) = 0$.

\medskip\noindent
Une conséquence de ce qui précède est que $\mathbf{R}$ ne possède
aucune extension de corps non triviale de degré impair, car les éléments de telles extensions
auraient des polynômes minimaux de degré impair.

\medskip\noindent
Soit ensuite $K/\mathbf{R}$ une extension finie galoisienne de groupe de Galois $G$.
Soit $P \subset G$ un $2$-sous-groupe de Sylow. Alors $K^P/\mathbf{R}$ est une
extension de degré impair, donc $K^P = \mathbf{R}$ d'après ce qui précède,
ce qui implique à son tour
$G = P$. (Tous ces arguments reposent bien entendu sur la théorie de Galois.)
Ainsi $G$ est un $2$-groupe. Si $G$ est non trivial, nous voyons alors que
$\mathbf{C} \subset K$, puisque $\mathbf{C}$ est (à isomorphisme près) l'unique
extension de degré $2$ de $\mathbf{R}$. Si $G$ avait plus de $2$ éléments,
nous obtiendrions une extension quadratique de $\mathbf{C}$.
C'est absurde, car tout nombre complexe possède une racine carrée.

\medskip\noindent
Conclusion : $\mathbf{C}$ est algébriquement clos. En effet, sinon
nous obtiendrions une extension finie non triviale $K/\mathbf{C}$
que nous pourrions supposer normale (donc galoisienne) sur $\mathbf{R}$ d'après le
Lemme \ref{lemma-normal-closure}. Mais nous avons vu ci-dessus qu'alors
$K = \mathbf{C}$.

\begin{lemma}[Théorème fondamental de l'algèbre]
```

</details>

### FR-FIELDS-B6-PROSE-0009

`lemma-C-algebraically-closed` — source 3202–3214, français 3195–3207.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3202) · [Français de travail](staged/fr/009_fields.prose-batch6.fr.tex)

L'énoncé et la preuve renvoyant à la discussion sont conservés. Le titre traduit littéralement le nom donné dans Stacks, sans remplacer celui-ci par un autre éponyme français. Algébriquement clos est confirmé par le théorème 5.4.1 du canon ; aucune preuve supplémentaire n'est ajoutée sous le lemme.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-C-algebraically-closed}
The field $\mathbf{C}$ is algebraically closed.
\end{lemma}

\begin{proof}
See discussion above.
\end{proof}





\section{Kummer extensions}
```

```tex
\label{lemma-C-algebraically-closed}
Le corps $\mathbf{C}$ est algébriquement clos.
\end{lemma}

\begin{proof}
Voir la discussion ci-dessus.
\end{proof}





\section{Extensions de Kummer}
```

</details>

### FR-FIELDS-B6-PROSE-0010

`section-Kummer` — source 3215–3230, français 3208–3223.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3215) · [Français de travail](staged/fr/009_fields.prose-batch6.fr.tex)

L'adjonction d'une racine, l'hypothèse de racine primitive, l'homomorphisme injectif et l'ordre divisant n sont traduits sans confondre diviseur et ordre exactement n. Le cas a=0 reste autorisé par les mots officiels, bien que la formule sigma(b)/b soit alors indéfinie : la correction historique FIELDS-035 reste hors du texte. S'identifie à un sous-groupe rend l'injection déjà affichée, non une hypothèse supplémentaire. Extensions de Kummer est le nom français retenu ; le canon consulté utilise la variante adjectivale kummeriennes.

**Réserve :** FIELDS-035, source 3219 : a appartient à K, sans exclusion de zéro, alors que l'application affichée divise par b. Garder l'ambiguïté source et sa proposition séparée, non ajouter a non nul.

Choix écartés :

- Rétablir a dans K* : correction source, pas traduction.
- Extensions kummeriennes : variante attestée, sans nécessité d'abandonner le nom propre de Kummer.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-Kummer}

\noindent
Let $K$ be a field. Let $n \geq 2$ be an integer such that $K$ contains
a primitive $n$th root of $1$. Let $a \in K$. Let $L$ be an extension
of $K$ obtained by adjoining a root $b$ of the equation $x^n = a$.
Then $L/K$ is Galois. If $G = \text{Gal}(L/K)$ is the Galois group, then
the map
$$
G \longrightarrow \mu_n(K),\quad \sigma \longmapsto \sigma(b)/b
$$
is an injective homomorphism of groups. In particular, $G$ is cyclic
of order dividing $n$ as a subgroup of the cyclic group $\mu_n(K)$.
Kummer theory gives a converse.

\begin{lemma}[Kummer extensions]
```

```tex
\label{section-Kummer}

\noindent
Soit $K$ un corps. Soit $n \geq 2$ un entier tel que $K$ contienne
une racine primitive $n$-ième de $1$. Soit $a \in K$. Soit $L$ une extension
de $K$ obtenue en adjoignant une racine $b$ de l'équation $x^n = a$.
Alors $L/K$ est galoisienne. Si $G = \text{Gal}(L/K)$ est le groupe de Galois,
l'application
$$
G \longrightarrow \mu_n(K),\quad \sigma \longmapsto \sigma(b)/b
$$
est un homomorphisme injectif de groupes. En particulier, $G$ est cyclique
et son ordre divise $n$, puisqu'il s'identifie à un sous-groupe du groupe cyclique $\mu_n(K)$.
La théorie de Kummer fournit une réciproque.

\begin{lemma}[Extensions de Kummer]
```

</details>

### FR-FIELDS-B6-PROSE-0011

`lemma-Kummer` — source 3231–3258, français 3224–3251.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3231) · [Français de travail](staged/fr/009_fields.prose-batch6.fr.tex)

La réciproque garde exactement le groupe Z/nZ, la condition de caractéristique et la racine primitive. La preuve par l'opérateur sigma et l'indépendance des caractères est intégrale : polynôme minimal, vecteur propre non nul, invariance de z^n et n conjugués distincts. La liste d'éléments juxtaposée à une égalité est conservée telle qu'en anglais. Le canon prouve un résultat apparenté par Hilbert 90 ; cette autre preuve n'est pas substituée. Premier à n se rapporte à la caractéristique, non au degré seul.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-Kummer}
Let $L/K$ be a Galois extension of fields whose Galois group is
$\mathbf{Z}/n\mathbf{Z}$. Assume moreover that the characteristic of $K$
is prime to $n$ and that $K$ contains a primitive $n$th root of $1$.
Then $L = K[z]$ with $z^n \in K$.
\end{lemma}

\begin{proof}
Let $\zeta \in K$ be a primitive $n$th root of $1$.
Let $\sigma$ be a generator of $\text{Gal}(L/K)$.
Consider $\sigma : L \to L$ as a $K$-linear operator.
Note that $\sigma^n - 1 = 0$ as a linear operator.
Applying linear independence of characters
(Lemma \ref{lemma-independence-characters}), we see
that there cannot be a polynomial over $K$ of degree $< n$
annihilating $\sigma$. Hence the minimal polynomial of $\sigma$
as a linear operator is $x^n - 1$. 
Since $\zeta$ is a root of $x^n - 1$ by linear algebra
there is a $0 \neq z \in L$ such that $\sigma(z) = \zeta z$.
This $z$ satisfies $z^n \in K$ because
$\sigma(z^n) = (\zeta z)^n = z^n$. Moreover, we see that
$z, \sigma(z), \ldots, \sigma^{n - 1}(z) =
z, \zeta z, \ldots \zeta^{n - 1} z$ are pairwise distinct
which guarantees that $z$ generates $L$ over $K$.
Hence $L = K[z]$ as required.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-Kummer}
Soit $L/K$ une extension galoisienne de corps dont le groupe de Galois est
$\mathbf{Z}/n\mathbf{Z}$. Supposons de plus que la caractéristique de $K$
soit première à $n$ et que $K$ contienne une racine primitive $n$-ième de $1$.
Alors $L = K[z]$ avec $z^n \in K$.
\end{lemma}

\begin{proof}
Soit $\zeta \in K$ une racine primitive $n$-ième de $1$.
Soit $\sigma$ un générateur de $\text{Gal}(L/K)$.
Considérons $\sigma : L \to L$ comme un opérateur $K$-linéaire.
Notons que $\sigma^n - 1 = 0$ comme opérateur linéaire.
En appliquant l'indépendance linéaire des caractères
(Lemme \ref{lemma-independence-characters}), nous voyons
qu'aucun polynôme sur $K$ de degré $< n$ ne peut
annuler $\sigma$. Le polynôme minimal de $\sigma$
comme opérateur linéaire est donc $x^n - 1$. 
Puisque $\zeta$ est une racine de $x^n - 1$, l'algèbre linéaire
donne un $0 \neq z \in L$ tel que $\sigma(z) = \zeta z$.
Cet élément $z$ vérifie $z^n \in K$, car
$\sigma(z^n) = (\zeta z)^n = z^n$. De plus, les éléments
$z, \sigma(z), \ldots, \sigma^{n - 1}(z) =
z, \zeta z, \ldots \zeta^{n - 1} z$ sont deux à deux distincts,
ce qui garantit que $z$ engendre $L$ sur $K$.
Ainsi $L = K[z]$, ce qu'il fallait démontrer.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B6-PROSE-0012

`lemma-adjoint-pth-root-unity` — source 3259–3276, français 3252–3270.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3259) · [Français de travail](staged/fr/009_fields.prose-batch6.fr.tex)

Le nombre premier p reste distinct de la caractéristique, et le degré divise p-1, sans égalité renforcée. Tous les arguments sont présents : décomposition de x^p-1, normalité, séparabilité, action par puissances de zeta et inclusion dans le groupe multiplicatif modulo p. La source appelle l'extension un splitting field ; le français identifie correctement le corps supérieur comme corps de décomposition, puis l'extension comme normale. C'est une reformulation de type grammatical, non un théorème ajouté.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-adjoint-pth-root-unity}
Let $K$ be a field with algebraic closure $\overline{K}$.
Let $p$ be a prime different from the characteristic of $K$.
Let $\zeta \in \overline{K}$ be a primitive $p$th root
of $1$. Then $K(\zeta)/K$ is a Galois extension of degree dividing $p - 1$.
\end{lemma}

\begin{proof}
The polynomial $x^p - 1$ splits completely over
$K(\zeta)$ as its roots are $1, \zeta, \zeta^2, \ldots, \zeta^{p - 1}$.
Hence $K(\zeta)/K$ is a splitting field and hence normal.
The extension is separable as $x^p - 1$ is a separable polynomial.
Thus the extension is Galois. Any automorphism of $K(\zeta)$ over $K$
sends $\zeta$ to $\zeta^i$ for some $1 \leq i \leq p - 1$.
Thus the Galois group is a subgroup of $(\mathbf{Z}/p\mathbf{Z})^*$.
\end{proof}

\begin{lemma}
```

```tex
\label{lemma-adjoint-pth-root-unity}
Soit $K$ un corps, muni d'une clôture algébrique $\overline{K}$.
Soit $p$ un nombre premier distinct de la caractéristique de $K$.
Soit $\zeta \in \overline{K}$ une racine primitive $p$-ième
de $1$. Alors $K(\zeta)/K$ est une extension galoisienne dont le degré divise $p - 1$.
\end{lemma}

\begin{proof}
Le polynôme $x^p - 1$ se décompose entièrement sur
$K(\zeta)$, ses racines étant $1, \zeta, \zeta^2, \ldots, \zeta^{p - 1}$.
Ainsi, dans l'extension $K(\zeta)/K$, le corps supérieur est un corps de
décomposition ; cette extension est donc normale.
L'extension est séparable, car $x^p - 1$ est un polynôme séparable.
Elle est donc galoisienne. Tout automorphisme de $K(\zeta)$ sur $K$
envoie $\zeta$ sur $\zeta^i$ pour un certain $1 \leq i \leq p - 1$.
Le groupe de Galois est donc un sous-groupe de $(\mathbf{Z}/p\mathbf{Z})^*$.
\end{proof}

\begin{lemma}
```

</details>

### FR-FIELDS-B6-PROSE-0013

`lemma-subfields-kummer` — source 3277–3315, français 3271–3309.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3277) · [Français de travail](staged/fr/009_fields.prose-batch6.fr.tex)

Le lemme concerne une extension finie engendrée par alpha, sans hypothèse de séparabilité ou de Galois ajoutée. La condition sur les racines de l'unité porte sur celles contenues dans L. Les deux degrés, le polynôme minimal sur L', sa factorisation avec multiplicité éventuelle, le coefficient constant et le produit des racines restent exacts par rapport à la source. Les deux signes précédemment rétablis sous FIELDS-029A/B ne sont pas recorrigés. La référence conserve la clé Radical et le numéro 5.2 ; seul Theorem devient Théorème dans l'argument optionnel. Ce lemme n'est pas prétendu démontré par les passages du canon lus ici.

**Réserve :** FIELDS-029A/B, source 3305 et 3309 : le signe (-1)^d absent des formules officielles n'est pas réintroduit. Le raisonnement divisant par alpha^d laisse aussi implicite le traitement du cas alpha=0 ; aucune condition supplémentaire n'est insérée. La citation Radical n'a pas été consultée ici comme nouveau canon.

Choix écartés :

- Réintroduire les signes ou supposer l'extension galoisienne : modifications mathématiques exclues.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-subfields-kummer}
\begin{reference}
\cite[Theorem 5.2]{Radical}
\end{reference}
Let $K$ be a field. Let $L/K$ be a finite extension of degree $e$
which is generated by an element $\alpha$ with $a = \alpha^e \in K$.
If every $e$th root of unity in $L$ is contained in $K$, then 
any sub extension $L/L'/K$ is generated by $\alpha^d$ for some $d | e$.
\end{lemma}

\begin{proof}
Observe that for $d | e$ the subfield $K(\alpha^d)$ has
$[K(\alpha^d) : K] = e/d$ and $[L : K(\alpha^d)] = d$.
Let $L/L'/K$ be a subextension. Say $d = [L : L']$. If $\alpha^d \in L'$,
then we have $L' = K(\alpha^d)$ for degree reasons.
Let $P \in L'[x]$ be the minimal polynomial of $\alpha$ over $L'$.
Then $P$ divides $x^e - a$ and $P$ has degree $d$.
Let us write
$$
x^e - a = \prod\nolimits_{i = 1, \ldots, e} (x - \zeta_i \alpha)
$$
in a splitting field of $x^e - a$ over $L$. The $\zeta_i$ are $e$th roots
of unity and after renumbering we have
$$
P = \prod\nolimits_{i = 1, \ldots, d} (x - \zeta_i \alpha)
$$
The constant term of $P$ is equal to
$$
c = (\prod\nolimits_{i = 1, \ldots, d} \zeta_i) \alpha^d
$$
and is in $L' \subset L$. Since $\alpha \in L$ this implies that
$\zeta = \prod_{i = 1, \ldots, d} \zeta_i$ is in $L$ and hence in $K$ by
our assumption. Thus $\alpha^d = \zeta^{-1}c \in L'$ and we conclude.
\end{proof}




\section{Artin-Schreier extensions}
```

```tex
\label{lemma-subfields-kummer}
\begin{reference}
\cite[Théorème 5.2]{Radical}
\end{reference}
Soit $K$ un corps. Soit $L/K$ une extension finie de degré $e$
engendrée par un élément $\alpha$ tel que $a = \alpha^e \in K$.
Si toute racine $e$-ième de l'unité appartenant à $L$ est contenue dans $K$, alors 
toute extension intermédiaire $L/L'/K$ est engendrée par $\alpha^d$ pour un certain $d | e$.
\end{lemma}

\begin{proof}
Observons que, pour $d | e$, le sous-corps $K(\alpha^d)$ vérifie
$[K(\alpha^d) : K] = e/d$ et $[L : K(\alpha^d)] = d$.
Soit $L/L'/K$ une extension intermédiaire. Posons $d = [L : L']$. Si $\alpha^d \in L'$,
alors $L' = K(\alpha^d)$ pour des raisons de degré.
Soit $P \in L'[x]$ le polynôme minimal de $\alpha$ sur $L'$.
Alors $P$ divise $x^e - a$ et $P$ est de degré $d$.
Écrivons
$$
x^e - a = \prod\nolimits_{i = 1, \ldots, e} (x - \zeta_i \alpha)
$$
dans un corps de décomposition de $x^e - a$ sur $L$. Les $\zeta_i$ sont des racines
$e$-ièmes de l'unité et, après renumérotation, nous avons
$$
P = \prod\nolimits_{i = 1, \ldots, d} (x - \zeta_i \alpha)
$$
Le terme constant de $P$ est égal à
$$
c = (\prod\nolimits_{i = 1, \ldots, d} \zeta_i) \alpha^d
$$
et appartient à $L' \subset L$. Comme $\alpha \in L$, cela implique que
$\zeta = \prod_{i = 1, \ldots, d} \zeta_i$ appartient à $L$, et donc à $K$ par
notre hypothèse. Ainsi $\alpha^d = \zeta^{-1}c \in L'$, ce qui conclut.
\end{proof}




\section{Extensions d’Artin–Schreier}
```

</details>

### FR-FIELDS-B6-PROSE-0014

`section-Artin-Schreier` — source 3316–3331, français 3310–3325.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3316) · [Français de travail](staged/fr/009_fields.prose-batch6.fr.tex)

L'équation x^p-x=a, le morphisme sigma(b)-b et l'ordre divisant p sont conservés, y compris la possibilité d'une extension triviale dans l'introduction. La réciproque annoncée n'est pas confondue avec une équivalence exigeant toujours le degré p. Le nom des extensions est attesté par le canon.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{section-Artin-Schreier}

\noindent
Let $K$ be a field of characteristic $p > 0$. Let $a \in K$. Let $L$ be an
extension of $K$ obtained by adjoining a root $b$ of the equation
$x^p - x = a$. Then $L/K$ is Galois. If $G = \text{Gal}(L/K)$ is the Galois
group, then the map
$$
G \longrightarrow \mathbf{Z}/p\mathbf{Z},\quad
\sigma \longmapsto \sigma(b) - b
$$
is an injective homomorphism of groups. In particular, $G$ is cyclic
of order dividing $p$ as a subgroup of $\mathbf{Z}/p\mathbf{Z}$.
The theory of Artin-Schreier extensions gives a converse.

\begin{lemma}[Artin-Schreier extensions]
```

```tex
\label{section-Artin-Schreier}

\noindent
Soit $K$ un corps de caractéristique $p > 0$. Soit $a \in K$. Soit $L$ une
extension de $K$ obtenue en adjoignant une racine $b$ de l'équation
$x^p - x = a$. Alors $L/K$ est galoisienne. Si $G = \text{Gal}(L/K)$ est le groupe
de Galois, alors l'application
$$
G \longrightarrow \mathbf{Z}/p\mathbf{Z},\quad
\sigma \longmapsto \sigma(b) - b
$$
est un homomorphisme injectif de groupes. En particulier, $G$ est cyclique
d'ordre divisant $p$ en tant que sous-groupe de $\mathbf{Z}/p\mathbf{Z}$.
La théorie des extensions d'Artin–Schreier fournit une réciproque.

\begin{lemma}[Extensions d'Artin–Schreier]
```

</details>

### FR-FIELDS-B6-PROSE-0015

`lemma-Artin-Schreier` — source 3332–3361, français 3326–3354.

[Anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/fields.tex#L3332) · [Français de travail](staged/fr/009_fields.prose-batch6.fr.tex)

L'énoncé de la réciproque exige le groupe Z/pZ. Toute la preuve par l'opérateur est conservée, avec x^p-1=(x-1)^p, choix de w, y non nul fixé, définition de z, translation de z par 1, engendrement et invariance de z^p-z. L'exposant p-2 inclut correctement p=2. Seul le gérondif mal rattaché est remplacé par D'après, conformément au relevé réversible. Aucun usage de Hilbert 90 du canon ni explication mathématique supplémentaire n'est inséré.

**Réserve :** La réparation est syntaxique : l'application de l'indépendance est faite par le raisonnement, non par aucun polynôme. Elle n'introduit pas une nouvelle étape de preuve et ne corrige pas l'anglais.

Choix écartés :

- Conserver le gérondif : rattachement maladroit au polynôme.
- En appliquant..., nous voyons qu'aucun... : formulation également fidèle, mais plus longue que la réparation retenue.

<details>
<summary>Textes complets effectivement comparés</summary>

```tex
\label{lemma-Artin-Schreier}
Let $L/K$ be a Galois extension of fields of characteristic $p > 0$
with Galois group $\mathbf{Z}/p\mathbf{Z}$. Then $L = K[z]$ with
$z^p - z \in K$.
\end{lemma}

\begin{proof}
Let $\sigma$ be a generator of $\text{Gal}(L/K)$.
Consider $\sigma : L \to L$ as a $K$-linear operator.
Observe that $\sigma^p - 1 = 0$ as a linear operator.
Applying linear independence of characters
(Lemma \ref{lemma-independence-characters}),
there cannot be a polynomial of degree $< p$
annihilating $\sigma$. We conclude that the minimal
polynomial of $\sigma$ is $x^p - 1 = (x - 1)^p$.
This implies that there exists $w \in L$ such that
$(\sigma - 1)^{p - 1}(w) = y$ is nonzero. Then
$\sigma(y) = y$, i.e., $y \in K$. Thus
$z = y^{-1}(\sigma - 1)^{p - 2}(w)$ satisfies
$\sigma(z) = z + 1$. Since $z \not \in K$ we have $L = K[z]$.
Moreover since $\sigma(z^p - z) = (z + 1)^p - (z + 1) = z^p - z$
we see that $z^p - z \in K$ and the proof is complete.
\end{proof}
```

```tex
\label{lemma-Artin-Schreier}
Soit $L/K$ une extension galoisienne de corps de caractéristique $p > 0$
de groupe de Galois $\mathbf{Z}/p\mathbf{Z}$. Alors $L = K[z]$ avec
$z^p - z \in K$.
\end{lemma}

\begin{proof}
Soit $\sigma$ un générateur de $\text{Gal}(L/K)$.
Considérons $\sigma : L \to L$ comme un opérateur $K$-linéaire.
Observons que $\sigma^p - 1 = 0$ comme opérateur linéaire.
D'après l'indépendance linéaire des caractères
(Lemme \ref{lemma-independence-characters}),
aucun polynôme de degré $< p$ ne peut
annuler $\sigma$. Nous en concluons que le polynôme minimal
de $\sigma$ est $x^p - 1 = (x - 1)^p$.
Cela implique qu'il existe $w \in L$ tel que
$(\sigma - 1)^{p - 1}(w) = y$ soit non nul. Alors
$\sigma(y) = y$, c'est-à-dire $y \in K$. Ainsi
$z = y^{-1}(\sigma - 1)^{p - 2}(w)$ vérifie
$\sigma(z) = z + 1$. Comme $z \not \in K$, nous avons $L = K[z]$.
De plus, puisque $\sigma(z^p - z) = (z + 1)^p - (z + 1) = z^p - z$,
nous voyons que $z^p - z \in K$, ce qui achève la démonstration.
\end{proof}
```

</details>

## Limites et suite

Travail assisté par OpenAI Codex. L'identité exacte du modèle et de son effort n'est pas attestée dans ces pièces locales et n'est pas inventée. Aucun PDF reconstruit ni nouvelle publication n'est revendiqué. Les attestations de registre restent bornées aux passages réellement consultés.

Prochaine section : Transcendance, ligne anglaise 3362 / française 3355. Préserver les vingt-cinq sections achevées ; poursuivre le reste du chapitre et de l'édition, puis reconstruction, contrôle visuel et publication avec LaTeX complet. L'ancienne édition éditorialisée demeure un matériau possible d'une édition AI-intégrée distincte, non une traduction déjà validée de celle-ci.
