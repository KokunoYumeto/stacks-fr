# Algèbre commutative : connexité et recollement

## Résultat et portée

Quatre sections entièrement comparées : anglais L3767–4535 et français L3747–4515. Les 19 paires contiennent tous les énoncés, preuves, diagrammes et transitions, notamment les huit propriétés locales et leurs preuves. 251 occurrences sont reliées à des règles contextualisées. Le préfixe relu atteint 24 sections, 150 paires et 1098 occurrences. Le chapitre et l’édition restent inachevés.

Une seule précision éditoriale ajoutée est retirée : « Un idempotent non nul » revient à « Un idempotent ». Le contexte source établit déjà le non-zéro ; cette restauration ne prétend ni découvrir un faux théorème, ni approuver la phrase hors contexte. Les formules, renvois et hypothèses explicitement écrites dans la source restent identiques.

Comparaison assistée par IA, sans relecture humaine. Le canon a été consulté rétrospectivement ; rien n’attribue cette consultation au traducteur initial. Les points de relecture sont des invitations à examiner le travail, jamais des conditions d’avancement.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch6.fr.tex) · [État français précédent](staged/fr/010_algebra.prose-batch3.fr.tex) · [Lot précédent](ALGEBRA_PROSE_BATCH5_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH6_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH6_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH6_OCCURRENCES.json) · [Restauration avant/après](ALGEBRA_PROSE_BATCH6_REPAIRS.json) · [Exceptions linguistiques des formules](ALGEBRA_PROSE_BATCH6_MATH_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH6_COVERAGE.json).

## Canon français effectivement consulté

### Antoine Ducros — Introduction à la théorie des schémas, juillet 2021

[Source universitaire](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [PDF conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages PDF/imprimées 144,147,148,196,197 lues intégralement. Appui précis : 3.1.11–12 (faisceau, recollement), 3.1.22.2 (localement connexe, composantes connexes, ouverts fermés), 4.1.28.1–4 (spectre d'un produit, idempotents, localisés et quotients). Images de p.144 et p.196 inspectées.

Attestations courtes : « recollement », « composantes connexes », « réunion disjointe des ouverts fermés », « Spectre d’un produit ».

Le même registre français exprime la connexité topologique, les éléments idempotents et le recollement unique de sections. Les passages mathématiques cités ont été lus, pas seulement un glossaire.

Limites : La définition des faisceaux dans 3.1.11, pas l'ensemble du chapitre, est l'appui. La fin de 3.1.13 et de 3.1.22.3 n'a pas été lue ici. Les répétitions ou coquilles des exemples suivants ne deviennent pas une autorité contre les équations de Stacks. Aucun énoncé général sur les composantes connexes de spectres n'est attribué à ces seules pages. Consultation rétrospective, non preuve d'une consultation lors de la traduction initiale.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

### Jean-François Dat — Introduction à la théorie des Schémas, Sorbonne M2, 2025–2026

[Source universitaire](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/Schemas/Schemas.pdf) · [PDF conservé](canon-consulted/fr-algebra/dat-schemas.pdf)

Pages PDF/imprimées 12–15,18–19,27–29,32–33 lues intégralement. Appui précis : §1.3, 1.3.1–2 pour ouverts principaux, localisation, faisceau associé et suite exacte ; §1.7 pp.27–29 pour condition de cocycle, donnée de descente, locale pour Zariski ; 2.1.3 pour recollement et unicité à isomorphisme unique près. Images p.15 et p.28 inspectées.

Attestations courtes : « ouverts principaux », « condition de cocycle », « donnée de descente », « locale pour la topologie de Zariski ».

La suite de recollement de modules figure explicitement p.15 ; les formules et le sens de cocycle accompagnent les mots p.28. Ce sont des attestations contextualisées du même sujet.

Limites : La preuve par fidèle platitude annoncée p.15 et la fin du théorème p.29 ne sont pas déclarées lues ici. Dat impose un recouvrement dans la formulation de p.28, contrairement au dernier lemme Stacks de ce lot : ne pas importer cette hypothèse. Produits finis et sommes directes sont compatibles mais la notation officielle est conservée. Les glissements propres au cours (indices des restrictions, sens de faisceaux, cohérent/quasi-cohérent, morphisme au-dessus de S) ne sont pas copiés ; les équations de Stacks gouvernent. Aucun examen des ouvrages simplement cités par Dat n'est revendiqué.

SHA-256 : 9298B062AC2BDF64161A107980A30F98E1F2DF6DEB4DA98E1FEB21BA494D26A1.

## Règles contextualisées

### FR-ALGEBRA-B6-RULE-TOPOLOGIE

Les parties sont simultanément ouvertes et fermées ; les ouverts principaux sont les D(f). Quasi-compact ne suppose pas séparé. Réunion disjointe exprime le coproduit topologique. Chaque occurrence est relue dans la paire complète, pas validée par son seul mot.

Canon : FR-ALGEBRA-B6-CANON-DUCROS, FR-ALGEBRA-B6-CANON-DAT.

### FR-ALGEBRA-B6-RULE-IDEMPOTENTS

Idempotent signifie e²=e ; nilpotent signifie qu'une puissance s'annule. Orthogonaux se rapporte ici au produit nul des deux éléments complémentaires. La précision non nul absente de la phrase anglaise est retirée à un seul endroit et documentée ; les hypothèses officielles non nul restent intactes.

Canon : FR-ALGEBRA-B6-CANON-DUCROS.

### FR-ALGEBRA-B6-RULE-CONNEXITE

Connexe, localement connexe et irréductible ne sont pas interchangeables. La lecture conserve les unions et intersections éventuellement infinies ; ni chemins ni ouverture des composantes ne sont ajoutés.

Canon : FR-ALGEBRA-B6-CANON-DUCROS.

### FR-ALGEBRA-B6-RULE-LOCALISATION

Localiser ne signifie ni quotienter automatiquement ni passer au corps des fractions. Les bases R, R_f et S restent distinguées. Corps résiduel traduit residue field. Unité est un élément inversible ; idéal unité est l'anneau entier comme idéal.

Canon : FR-ALGEBRA-B6-CANON-DUCROS, FR-ALGEBRA-B6-CANON-DAT.

### FR-ALGEBRA-B6-RULE-FINITUDE

Le sens est contrôlé par la définition et les preuves de Stacks : finite module signifie engendré par un ensemble fini, finite type algebra génération finie comme algèbre, finite presentation un nombre fini de générateurs et relations. Les nouvelles pages de canon ne sont pas présentées comme une attestation exhaustive de chacune de ces expressions.

Canon : Définitions et comparaison directe ; attestation externe exhaustive non acquise.

### FR-ALGEBRA-B6-RULE-MORPHISMES

Morphism et map deviennent morphisme quand la catégorie est fixée (anneaux ou modules), application continue pour les espaces. Relèvement est un antécédent choisi, non une section globale. Injectif, surjectif, bijectif et isomorphisme ne sont pas fusionnés.

Canon : FR-ALGEBRA-B6-CANON-DUCROS, FR-ALGEBRA-B6-CANON-DAT.

### FR-ALGEBRA-B6-RULE-EXACTITUDE

Exactitude concerne la suite aux places indiquées ; aucun zéro ni aucune surjectivité finale ne sont ajoutés. Homologie garde Ker/Im. Le quotient S/T du passage est un module, pas un quotient d'anneaux.

Canon : FR-ALGEBRA-B6-CANON-DAT.

### FR-ALGEBRA-B6-RULE-RECOLLEMENT

Recollement conserve existence, unicité et compatibilité des restrictions lorsque la source les affirme. Faisceau n'est pas préfaisceau. Condition de cocycle contrôle le diagramme sur triples intersections, sans inverser les indices ; descente plate reste le cadre annoncé et n'ajoute pas d'hypothèse dans le lemme présent.

Canon : FR-ALGEBRA-B6-CANON-DUCROS, FR-ALGEBRA-B6-CANON-DAT.

## Passages parallèles complets

### 01 — section-open-and-closed

Anglais L3767–3773 ; français L3747–3753.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3767) · FR-ALGEBRA-B6-CHOICE-0001.

« À la fois ouverts et fermés » lève l'ambiguïté de la conjonction sans changer la propriété : il ne s'agit pas de deux classes distinctes de parties. « Idempotents » désigne les éléments e²=e, non des idéaux idempotents. Ducros 4.1.28.1 emploie ouverts fermés et idempotents dans cette même correspondance. La phrase introductive ne prétend pas que toutes les parties ouvertes possèdent cette forme.

Règles : FR-ALGEBRA-B6-RULE-TOPOLOGIE, FR-ALGEBRA-B6-RULE-IDEMPOTENTS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Open and closed subsets of spectra}
\label{section-open-and-closed}

\noindent
It turns out that open and closed subsets of a spectrum correspond to
idempotents of the ring.
```

Français restauré :
```tex
\section{Sous-ensembles ouverts et fermés des spectres}
\label{section-open-and-closed}

\noindent
Il se trouve que les sous-ensembles à la fois ouverts et fermés d'un spectre
correspondent aux idempotents de l'anneau.
```

</details>

### 02 — lemma-idempotent-spec

Anglais L3774–3820 ; français L3754–3800.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3774) · FR-ALGEBRA-B6-CHOICE-0002.

Le domaine anglais est un anneau intègre, non un domaine topologique. Le passage à chaque corps résiduel et les quatre égalités ou inégalités à 0 et 1 sont préservés. Dans les deux affichages, in devient dans quatre fois : ce sont des prépositions de lecture, pas des symboles. La réunion est disjointe, même si la dernière phrase de la preuve n'explicite que le recouvrement ; aucune étape n'est ajoutée. Ducros 4.1.28 confirme la terminologie sur les idempotents complémentaires.

Règles : FR-ALGEBRA-B6-RULE-IDEMPOTENTS, FR-ALGEBRA-B6-RULE-LOCALISATION.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-idempotent-spec}
Let $R$ be a ring. Let $e \in R$ be an idempotent.
In this case
$$
\Spec(R) = D(e) \amalg D(1-e).
$$
\end{lemma}

\begin{proof}
Note that an idempotent $e$ of a domain is either $1$ or $0$.
Hence we see that
\begin{eqnarray*}
D(e)
& = &
\{ \mathfrak p \in \Spec(R)
\mid
e \not\in \mathfrak p \} \\
& = &
\{ \mathfrak p \in \Spec(R)
\mid
e \not = 0\text{ in }\kappa(\mathfrak p) \} \\
& = &
\{ \mathfrak p \in \Spec(R)
\mid
e = 1\text{ in }\kappa(\mathfrak p) \}
\end{eqnarray*}
Similarly we have
\begin{eqnarray*}
D(1-e)
& = &
\{ \mathfrak p \in \Spec(R)
\mid
1 - e \not\in \mathfrak p \} \\
& = &
\{ \mathfrak p \in \Spec(R)
\mid
e \not = 1\text{ in }\kappa(\mathfrak p) \} \\
& = &
\{ \mathfrak p \in \Spec(R)
\mid
e = 0\text{ in }\kappa(\mathfrak p) \}
\end{eqnarray*}
Since the image of $e$ in any residue field is either $1$ or $0$
we deduce that $D(e)$ and $D(1-e)$ cover all of $\Spec(R)$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-idempotent-spec}
Soit $R$ un anneau. Soit $e \in R$ un idempotent.
Dans ce cas,
$$
\Spec(R) = D(e) \amalg D(1-e).
$$
\end{lemma}

\begin{proof}
Notons qu'un idempotent $e$ d'un anneau intègre est égal à $1$ ou à $0$.
Nous voyons donc que
\begin{eqnarray*}
D(e)
& = &
\{ \mathfrak p \in \Spec(R)
\mid
e \not\in \mathfrak p \} \\
& = &
\{ \mathfrak p \in \Spec(R)
\mid
e \not = 0\text{ dans }\kappa(\mathfrak p) \} \\
& = &
\{ \mathfrak p \in \Spec(R)
\mid
e = 1\text{ dans }\kappa(\mathfrak p) \}
\end{eqnarray*}
De même, nous avons
\begin{eqnarray*}
D(1-e)
& = &
\{ \mathfrak p \in \Spec(R)
\mid
1 - e \not\in \mathfrak p \} \\
& = &
\{ \mathfrak p \in \Spec(R)
\mid
e \not = 1\text{ dans }\kappa(\mathfrak p) \} \\
& = &
\{ \mathfrak p \in \Spec(R)
\mid
e = 0\text{ dans }\kappa(\mathfrak p) \}
\end{eqnarray*}
Puisque l'image de $e$ dans tout corps résiduel est égale à $1$ ou à $0$,
nous en déduisons que $D(e)$ et $D(1-e)$ recouvrent tout $\Spec(R)$.
\end{proof}
```

</details>

### 03 — lemma-spec-product

Anglais L3821–3856 ; français L3801–3836.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3821) · FR-ALGEBRA-B6-CHOICE-0003.

Les projections d'anneaux induisent les applications continues dans le sens contravariant indiqué. La réunion disjointe est topologique et l'application est un homéomorphisme, pas une simple bijection. Les deux localisés et l'étape laissée au lecteur sont conservés. Ducros 4.1.28.2–4 présente explicitement les deux descriptions, par quotient et par localisation. La transition annonçant une seconde preuve après le recollement des fonctions et son renvoi restent dans cette paire.

Règles : FR-ALGEBRA-B6-RULE-TOPOLOGIE, FR-ALGEBRA-B6-RULE-IDEMPOTENTS, FR-ALGEBRA-B6-RULE-LOCALISATION, FR-ALGEBRA-B6-RULE-MORPHISMES, FR-ALGEBRA-B6-RULE-RECOLLEMENT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-spec-product}
Let $R_1$ and $R_2$ be rings.
Let $R = R_1 \times R_2$.
The maps $R \to R_1$, $(x, y) \mapsto x$ and $R \to R_2$,
$(x, y) \mapsto y$
induce continuous maps $\Spec(R_1) \to \Spec(R)$ and
$\Spec(R_2) \to \Spec(R)$.
The induced map
$$
\Spec(R_1) \amalg \Spec(R_2)
\longrightarrow
\Spec(R)
$$
is a homeomorphism. In other words,
the spectrum of $R = R_1\times R_2$ is the
disjoint union of the spectrum of $R_1$ and the
spectrum of $R_2$.
\end{lemma}

\begin{proof}
Write $1 = e_1 + e_2$ with $e_1 = (1, 0)$ and $e_2 = (0, 1)$.
Note that $e_1$ and $e_2 = 1 - e_1$ are idempotents.
We leave it to the reader to show that
$R_1 = R_{e_1}$ is the localization of $R$ at $e_1$.
Similarly for $e_2$.
Thus the statement of the lemma follows from Lemma
\ref{lemma-idempotent-spec} combined with Lemma
\ref{lemma-standard-open}.
\end{proof}

\noindent
We reprove the following lemma later after introducing
a glueing lemma for functions. See Section
\ref{section-tilde-module-sheaf}.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-spec-product}
Soient $R_1$ et $R_2$ des anneaux.
Soit $R = R_1 \times R_2$.
Les morphismes $R \to R_1$, $(x, y) \mapsto x$ et $R \to R_2$,
$(x, y) \mapsto y$
induisent des applications continues $\Spec(R_1) \to \Spec(R)$ et
$\Spec(R_2) \to \Spec(R)$.
L'application ainsi obtenue
$$
\Spec(R_1) \amalg \Spec(R_2)
\longrightarrow
\Spec(R)
$$
est un homéomorphisme. Autrement dit,
le spectre de $R = R_1\times R_2$ est la
réunion disjointe du spectre de $R_1$ et du
spectre de $R_2$.
\end{lemma}

\begin{proof}
Écrivons $1 = e_1 + e_2$ avec $e_1 = (1, 0)$ et $e_2 = (0, 1)$.
Notons que $e_1$ et $e_2 = 1 - e_1$ sont des idempotents.
Nous laissons au lecteur le soin de montrer que
$R_1 = R_{e_1}$ est la localisation de $R$ en $e_1$.
Il en va de même pour $e_2$.
Ainsi, l'assertion du lemme résulte du lemme
\ref{lemma-idempotent-spec} combiné au lemme
\ref{lemma-standard-open}.
\end{proof}

\noindent
Nous redémontrerons le lemme suivant plus loin, après avoir introduit
un lemme de recollement pour les fonctions. Voir la section
\ref{section-tilde-module-sheaf}.
```

</details>

### 04 — lemma-disjoint-decomposition

Anglais L3857–3908 ; français L3837–3888.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3857) · FR-ALGEBRA-B6-CHOICE-0004.

Les deux implications de la bijection, son unicité et l'ensemble de la preuve ont été comparés. La quasi-compacité intervient pour obtenir deux familles finies ; la puissance N porte sur IJ, puis la puissance 2N sur I+J. Les idéaux I et J et les valeurs de x sur V(I) et V(J) ne sont pas intervertis. Une précision française non littérale est retirée : « Un idempotent non nul » redevient « Un idempotent », comme l'anglais. Le non-zéro est déjà établi dans la phrase précédente, mais sa réinsertion comme qualification générale serait une amélioration éditoriale du témoin. Le contexte correct et le danger d'une lecture isolée sont consignés séparément, sans affirmer que zéro n'est pas nilpotent.

Point particulier à relire : Restauration de fidélité, non découverte d'un faux théorème : les deux idempotents envisagés sont déjà non nuls dans la phrase précédente. Isolée de ce contexte, la phrase anglaise « An idempotent is not nilpotent » a l'exception e=0. La précision retirée reste consultable dans l'ancien état français et dans le journal de réparation. Le témoin officiel n'est pas modifié.

Règles : FR-ALGEBRA-B6-RULE-TOPOLOGIE, FR-ALGEBRA-B6-RULE-IDEMPOTENTS, FR-ALGEBRA-B6-RULE-LOCALISATION, FR-ALGEBRA-B6-RULE-FINITUDE, FR-ALGEBRA-B6-RULE-MORPHISMES.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-disjoint-decomposition}
Let $R$ be a ring. For each $U \subset \Spec(R)$
which is open and closed
there exists a unique idempotent $e \in R$ such that
$U = D(e)$. This induces a 1-1 correspondence between
open and closed subsets $U \subset \Spec(R)$ and
idempotents $e \in R$.
\end{lemma}

\begin{proof}
Let $U \subset \Spec(R)$ be open and closed.
Since $U$ is closed it is quasi-compact by
Lemma \ref{lemma-quasi-compact}, and similarly for
its complement.
Write $U = \bigcup_{i = 1}^n D(f_i)$ as a finite union of standard opens.
Similarly, write $\Spec(R) \setminus U = \bigcup_{j = 1}^m D(g_j)$
as a finite union of standard opens. Since $\emptyset =
D(f_i) \cap D(g_j) = D(f_i g_j)$ we see that $f_i g_j$ is
nilpotent by Lemma \ref{lemma-Zariski-topology}.
Let $I = (f_1, \ldots, f_n) \subset R$ and let
$J = (g_1, \ldots, g_m) \subset R$.
Note that $V(J)$ equals $U$, that $V(I)$
equals the complement of $U$, so $\Spec(R) = V(I) \amalg V(J)$.
By the remark on nilpotency above,
we see that $(IJ)^N = (0)$ for some sufficiently large integer $N$.
Since $\bigcup D(f_i) \cup \bigcup D(g_j) = \Spec(R)$
we see that $I + J = R$, see Lemma \ref{lemma-Zariski-topology}.
By raising this equation to the $2N$th power we conclude that
$I^N + J^N = R$. Write $1 = x + y$ with $x \in I^N$ and $y \in J^N$.
Then $0 = xy = x(1 - x)$ as $I^N J^N = (0)$. Thus $x = x^2$
is idempotent and contained
in $I^N \subset I$. The idempotent $y = 1 - x$ is contained in $J^N \subset J$. 
This shows that the idempotent $x$ maps to $1$ in every residue field
$\kappa(\mathfrak p)$ for $\mathfrak p \in V(J)$ and that $x$ maps to $0$
in $\kappa(\mathfrak p)$ for every $\mathfrak p \in V(I)$.

\medskip\noindent
To see uniqueness suppose that $e_1, e_2$ are
distinct idempotents in $R$. We have to show there
exists a prime $\mathfrak p$ such that $e_1 \in \mathfrak p$
and $e_2 \not \in \mathfrak p$, or conversely.
Write $e_i' = 1 - e_i$. If $e_1 \not = e_2$, then
$0 \not = e_1 - e_2  = e_1(e_2 + e_2') - (e_1 + e_1')e_2
= e_1 e_2' - e_1' e_2$. Hence either the idempotent
$e_1 e_2' \not = 0$ or $e_1' e_2 \not = 0$. An idempotent
is not nilpotent, and hence we find a prime
$\mathfrak p$ such that either $e_1e_2' \not \in \mathfrak p$
or $e_1'e_2 \not \in \mathfrak p$, by Lemma \ref{lemma-Zariski-topology}.
It is easy to see this gives the desired prime.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-disjoint-decomposition}
Soit $R$ un anneau. Pour tout $U \subset \Spec(R)$
qui est à la fois ouvert et fermé,
il existe un unique idempotent $e \in R$ tel que
$U = D(e)$. Cela induit une correspondance bijective entre les
sous-ensembles à la fois ouverts et fermés $U \subset \Spec(R)$ et les
idempotents $e \in R$.
\end{lemma}

\begin{proof}
Soit $U \subset \Spec(R)$ un sous-ensemble ouvert et fermé.
Puisque $U$ est fermé, il est quasi-compact d'après le
lemme \ref{lemma-quasi-compact}, et il en va de même pour
son complémentaire.
Écrivons $U = \bigcup_{i = 1}^n D(f_i)$ comme réunion finie d'ouverts principaux.
De même, écrivons $\Spec(R) \setminus U = \bigcup_{j = 1}^m D(g_j)$
comme réunion finie d'ouverts principaux. Puisque $\emptyset =
D(f_i) \cap D(g_j) = D(f_i g_j)$, nous voyons que $f_i g_j$ est
nilpotent d'après le lemme \ref{lemma-Zariski-topology}.
Soit $I = (f_1, \ldots, f_n) \subset R$ et soit
$J = (g_1, \ldots, g_m) \subset R$.
Notons que $V(J)$ est égal à $U$, que $V(I)$
est égal au complémentaire de $U$, de sorte que $\Spec(R) = V(I) \amalg V(J)$.
D'après la remarque ci-dessus concernant la nilpotence,
nous voyons que $(IJ)^N = (0)$ pour un entier $N$ suffisamment grand.
Puisque $\bigcup D(f_i) \cup \bigcup D(g_j) = \Spec(R)$,
nous voyons que $I + J = R$ ; voir le lemme \ref{lemma-Zariski-topology}.
En élevant cette égalité à la puissance $2N$, nous en concluons que
$I^N + J^N = R$. Écrivons $1 = x + y$ avec $x \in I^N$ et $y \in J^N$.
Alors $0 = xy = x(1 - x)$ puisque $I^N J^N = (0)$. Ainsi $x = x^2$
est idempotent et appartient
à $I^N \subset I$. L'idempotent $y = 1 - x$ appartient à $J^N \subset J$.
Cela montre que l'idempotent $x$ a pour image $1$ dans tout corps résiduel
$\kappa(\mathfrak p)$ pour $\mathfrak p \in V(J)$ et que $x$ a pour image $0$
dans $\kappa(\mathfrak p)$ pour tout $\mathfrak p \in V(I)$.

\medskip\noindent
Pour voir l'unicité, supposons que $e_1, e_2$ soient des
idempotents distincts de $R$. Nous devons montrer qu'il
existe un idéal premier $\mathfrak p$ tel que $e_1 \in \mathfrak p$
et $e_2 \not \in \mathfrak p$, ou l'inverse.
Écrivons $e_i' = 1 - e_i$. Si $e_1 \not = e_2$, alors
$0 \not = e_1 - e_2  = e_1(e_2 + e_2') - (e_1 + e_1')e_2
= e_1 e_2' - e_1' e_2$. Par conséquent, soit l'idempotent
$e_1 e_2' \not = 0$, soit $e_1' e_2 \not = 0$. Un idempotent
n'est pas nilpotent ; nous trouvons donc un idéal premier
$\mathfrak p$ tel que soit $e_1e_2' \not \in \mathfrak p$,
soit $e_1'e_2 \not \in \mathfrak p$, d'après le lemme \ref{lemma-Zariski-topology}.
Il est facile de voir que cela fournit l'idéal premier recherché.
\end{proof}
```

</details>

### 05 — lemma-characterize-spec-connected

Anglais L3909–3920 ; français L3889–3900.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3909) · FR-ALGEBRA-B6-CHOICE-0005.

L'hypothèse anneau non nul est explicitement présente dans l'anglais et reste donc ici, contrairement à la précision ajoutée dans le lemme précédent. Connexe n'est pas remplacé par irréductible ; « aucun idempotent non trivial » n'exclut ni 0 ni 1. Le renvoi à la définition topologique est gardé sans introduire de convention nouvelle sur le vide. Le vocabulaire de connexité est attesté chez Ducros 3.1.22.2, sans lui attribuer cette preuve algébrique.

Règles : FR-ALGEBRA-B6-RULE-IDEMPOTENTS, FR-ALGEBRA-B6-RULE-CONNEXITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-spec-connected}
Let $R$ be a nonzero ring. Then $\Spec(R)$ is
connected if and only if $R$ has no nontrivial
idempotents.
\end{lemma}

\begin{proof}
Obvious from Lemma \ref{lemma-disjoint-decomposition}
and the definition of a connected topological space.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-characterize-spec-connected}
Soit $R$ un anneau non nul. Alors $\Spec(R)$ est
connexe si et seulement si $R$ ne possède aucun idempotent
non trivial.
\end{lemma}

\begin{proof}
Cela résulte immédiatement du lemme \ref{lemma-disjoint-decomposition}
et de la définition d'un espace topologique connexe.
\end{proof}
```

</details>

### 06 — lemma-ideal-is-squared-union-connected

Anglais L3921–3957 ; français L3901–3937.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3921) · FR-ALGEBRA-B6-CHOICE-0006.

De type fini porte sur I comme idéal ; aucune hypothèse noethérienne sur R n'est introduite. Les trois conclusions (générateur idempotent, quotient identifié au localisé, partie ouverte et fermée) et leur ordre de preuve 1,3,2 sont préservés. Annulé par une puissance strictement positive traduit positive power, non une puissance simplement non négative. Les idempotents orthogonaux sont les deux éléments e,e' de produit nul ; ce sens vient des équations du passage. La tournure source qui appelle l'égalité e+e'=1 une paire reste identifiable plutôt que de remplacer ses formules.

Point particulier à relire : « e+e'=1 est une paire » est une compression maladroite héritée de l'anglais. Le contexte définit bien deux idempotents orthogonaux. Cette lecture ne transforme pas le témoin fidèle en une correction mathématique de l'original.

Règles : FR-ALGEBRA-B6-RULE-TOPOLOGIE, FR-ALGEBRA-B6-RULE-IDEMPOTENTS, FR-ALGEBRA-B6-RULE-FINITUDE, FR-ALGEBRA-B6-RULE-MORPHISMES, FR-ALGEBRA-B6-RULE-EXACTITUDE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-ideal-is-squared-union-connected}
Let $I \subset R$ be a finitely generated ideal of a ring $R$
such that $I = I^2$. Then
\begin{enumerate}
\item there exists an idempotent $e \in R$ such that $I = (e)$,
\item $R/I \cong R_{e'}$ for the idempotent $e' = 1 - e \in R$, and
\item $V(I)$ is open and closed in $\Spec(R)$.
\end{enumerate}
\end{lemma}

\begin{proof}
By Nakayama's Lemma \ref{lemma-NAK} there exists an element
$f = 1 + i$, $i \in I$ such that $fI = 0$. Then $f^2 = f + fi = f$
is an idempotent. Consider the idempotent $e = 1 - f = -i \in I$.
For $j \in I$ we have $ej = j - fj = j$ hence $I = (e)$.
This proves (1).

\medskip\noindent
Parts (2) and (3) follow from (1). Namely, we have
$V(I) = V(e) = \Spec(R) \setminus D(e)$ which is open and
closed by either Lemma \ref{lemma-idempotent-spec} or
Lemma \ref{lemma-disjoint-decomposition}. This proves (3).
For (2) observe that the map $R \to R_{e'}$ is surjective
since $x/(e')^n = x/e' = xe'/(e')^2 = xe'/e' = x/1$ in $R_{e'}$.
The kernel of the map $R \to R_{e'}$ is the set of elements of
$R$ annihilated by a positive power of $e'$. Since $e'$ is
idempotent this is the ideal of elements annihilated by $e'$
which is the ideal $I = (e)$ as $e + e' = 1$ is a pair
of orthogonal idempotents. This proves (2).
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-ideal-is-squared-union-connected}
Soit $I \subset R$ un idéal de type fini d'un anneau $R$
tel que $I = I^2$. Alors
\begin{enumerate}
\item il existe un idempotent $e \in R$ tel que $I = (e)$,
\item $R/I \cong R_{e'}$ pour l'idempotent $e' = 1 - e \in R$, et
\item $V(I)$ est ouvert et fermé dans $\Spec(R)$.
\end{enumerate}
\end{lemma}

\begin{proof}
D'après le lemme de Nakayama \ref{lemma-NAK}, il existe un élément
$f = 1 + i$, $i \in I$ tel que $fI = 0$. Alors $f^2 = f + fi = f$
est un idempotent. Considérons l'idempotent $e = 1 - f = -i \in I$.
Pour $j \in I$, nous avons $ej = j - fj = j$, donc $I = (e)$.
Cela démontre (1).

\medskip\noindent
Les parties (2) et (3) résultent de (1). En effet, nous avons
$V(I) = V(e) = \Spec(R) \setminus D(e)$, qui est ouvert et
fermé d'après le lemme \ref{lemma-idempotent-spec} ou le
lemme \ref{lemma-disjoint-decomposition}. Cela démontre (3).
Pour (2), observons que le morphisme $R \to R_{e'}$ est surjectif
puisque $x/(e')^n = x/e' = xe'/(e')^2 = xe'/e' = x/1$ dans $R_{e'}$.
Le noyau du morphisme $R \to R_{e'}$ est l'ensemble des éléments de
$R$ annulés par une puissance strictement positive de $e'$. Puisque $e'$ est
idempotent, c'est l'idéal des éléments annulés par $e'$,
qui est l'idéal $I = (e)$ puisque $e + e' = 1$ est une paire
d'idempotents orthogonaux. Cela démontre (2).
\end{proof}
```

</details>

### 07 — section-connected-components

Anglais L3958–3966 ; français L3938–3946.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3958) · FR-ALGEBRA-B6-CHOICE-0007.

Composantes connexes et localement connexe sont deux notions différentes, et le texte maintient précisément l'avertissement : un spectre général n'est pas localement connexe. Ducros 3.1.22.2 distingue aussi le cas localement connexe du cas général. Le français n'affirme pas que les composantes d'un spectre sont toujours ouvertes, ni que connexité signifie connexité par arcs.

Règles : FR-ALGEBRA-B6-RULE-CONNEXITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Connected components of spectra}
\label{section-connected-components}

\noindent
Connected components of spectra are not as easy to understand as one
may think at first. This is because we are used to the topology of
locally connected spaces, but the spectrum of a ring is in general
not locally connected.
```

Français restauré :
```tex
\section{Composantes connexes des spectres}
\label{section-connected-components}

\noindent
Les composantes connexes des spectres ne sont pas aussi faciles à comprendre
qu'on pourrait le penser de prime abord. Cela vient de ce que nous sommes habitués à la topologie des
espaces localement connexes, alors que le spectre d'un anneau n'est en général
pas localement connexe.
```

</details>

### 08 — lemma-closed-union-connected-components

Anglais L3967–4006 ; français L3947–3986.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L3967) · FR-ALGEBRA-B6-CHOICE-0008.

Les trois conditions concernent une partie T fermée : réunion de composantes connexes, intersection de parties ouvertes et fermées, puis V(I) pour un idéal engendré par des idempotents. Ni la famille d'idempotents ni l'intersection ne sont rendues finies. L'idéal est unique dans la classe décrite en (3), non parmi tous les idéaux ayant le même V(I). Les passages au complémentaire e↦1−e, la puissance e^n et les deux références topologiques restent exacts. La traduction « famille » pour collection ne transforme pas celle-ci en une famille finie.

Point particulier à relire : Ne pas déduire une ouverture des composantes ni une génération finie de I ; aucune de ces hypothèses n'est dans la source.

Règles : FR-ALGEBRA-B6-RULE-TOPOLOGIE, FR-ALGEBRA-B6-RULE-IDEMPOTENTS, FR-ALGEBRA-B6-RULE-CONNEXITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-closed-union-connected-components}
Let $R$ be a ring. Let $T \subset \Spec(R)$ be a subset of the spectrum.
The following are equivalent
\begin{enumerate}
\item $T$ is closed and is a union of connected components of
$\Spec(R)$,
\item $T$ is an intersection of open and closed subsets of
$\Spec(R)$, and
\item $T = V(I)$ where $I \subset R$ is an ideal generated by idempotents.
\end{enumerate}
Moreover, the ideal in (3) if it exists is unique.
\end{lemma}

\begin{proof}
By
Lemma \ref{lemma-topology-spec}
and
Topology, Lemma \ref{topology-lemma-closed-union-connected-components}
we see that (1) and (2) are equivalent.
Assume (2) and write $T = \bigcap U_\alpha$ with
$U_\alpha \subset \Spec(R)$ open and closed.
Then $U_\alpha = D(e_\alpha)$ for some idempotent $e_\alpha \in R$ by
Lemma \ref{lemma-disjoint-decomposition}.
Then setting $I = (1 - e_\alpha)$ we see that $T = V(I)$, i.e., (3) holds.
Finally, assume (3). Write $T = V(I)$ and $I = (e_\alpha)$ for some
collection of idempotents $e_\alpha$. Then it is clear that
$T = \bigcap V(e_\alpha) = \bigcap D(1 - e_\alpha)$.

\medskip\noindent
Suppose that $I$ is an ideal generated by idempotents.
Let $e \in R$ be an idempotent such that $V(I) \subset V(e)$. Then by
Lemma \ref{lemma-Zariski-topology}
we see that $e^n \in I$ for some $n \geq 1$. As $e$ is an idempotent
this means that $e \in I$. Hence we see that $I$ is generated by
exactly those idempotents $e$ such that $T \subset V(e)$.
In other words, the ideal $I$ is completely determined by the
closed subset $T$ which proves uniqueness.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-closed-union-connected-components}
Soit $R$ un anneau. Soit $T \subset \Spec(R)$ un sous-ensemble du spectre.
Les conditions suivantes sont équivalentes :
\begin{enumerate}
\item $T$ est fermé et est une réunion de composantes connexes de
$\Spec(R)$,
\item $T$ est une intersection de sous-ensembles ouverts et fermés de
$\Spec(R)$, et
\item $T = V(I)$, où $I \subset R$ est un idéal engendré par des idempotents.
\end{enumerate}
De plus, l'idéal de (3), s'il existe, est unique.
\end{lemma}

\begin{proof}
D'après
le lemme \ref{lemma-topology-spec}
et
Topologie, lemme \ref{topology-lemma-closed-union-connected-components},
nous voyons que (1) et (2) sont équivalentes.
Supposons (2) et écrivons $T = \bigcap U_\alpha$ avec
$U_\alpha \subset \Spec(R)$ ouvert et fermé.
Alors $U_\alpha = D(e_\alpha)$ pour un certain idempotent $e_\alpha \in R$ d'après le
lemme \ref{lemma-disjoint-decomposition}.
En posant alors $I = (1 - e_\alpha)$, nous voyons que $T = V(I)$, c'est-à-dire que (3) est satisfaite.
Enfin, supposons (3). Écrivons $T = V(I)$ et $I = (e_\alpha)$ pour une certaine
famille d'idempotents $e_\alpha$. Il est alors clair que
$T = \bigcap V(e_\alpha) = \bigcap D(1 - e_\alpha)$.

\medskip\noindent
Supposons que $I$ soit un idéal engendré par des idempotents.
Soit $e \in R$ un idempotent tel que $V(I) \subset V(e)$. Alors, d'après le
lemme \ref{lemma-Zariski-topology},
nous voyons que $e^n \in I$ pour un certain $n \geq 1$. Comme $e$ est un idempotent,
cela signifie que $e \in I$. Nous voyons donc que $I$ est engendré par
exactement les idempotents $e$ tels que $T \subset V(e)$.
Autrement dit, l'idéal $I$ est entièrement déterminé par le
sous-ensemble fermé $T$, ce qui démontre l'unicité.
\end{proof}
```

</details>

### 09 — lemma-connected-component

Anglais L4007–4040 ; français L3987–4020.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4007) · FR-ALGEBRA-B6-CHOICE-0009.

L'énoncé reste une description d'une composante par un quotient R/I ; il ne dit pas que R lui-même est connexe. Les idempotents qui s'annulent dans le corps résiduel du point engendrent I, et ceux hors de cette famille ont image 1 dans le quotient. Le français corrige uniquement la grammaire de « we have see » en « nous voyons », sans corriger un contenu mathématique. Les hypothèses et le renvoi au résultat topologique ne sont ni abrégés ni renforcés.

Règles : FR-ALGEBRA-B6-RULE-TOPOLOGIE, FR-ALGEBRA-B6-RULE-IDEMPOTENTS, FR-ALGEBRA-B6-RULE-CONNEXITE, FR-ALGEBRA-B6-RULE-LOCALISATION.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-connected-component}
Let $R$ be a ring.
A connected component of
$\Spec(R)$ is of the form $V(I)$,
where $I$ is an ideal generated by idempotents
such that every idempotent of $R$ either maps to
$0$ or $1$ in $R/I$.
\end{lemma}

\begin{proof}
Let $\mathfrak p$ be a prime of $R$. By
Lemma \ref{lemma-topology-spec}
we have see that the hypotheses of
Topology, Lemma \ref{topology-lemma-connected-component-intersection}
are satisfied for the topological space $\Spec(R)$.
Hence the connected component of $\mathfrak p$ in $\Spec(R)$
is the intersection of open and closed subsets of $\Spec(R)$
containing $\mathfrak p$. Hence it equals $V(I)$ where
$I$ is generated by the idempotents $e \in R$ such that $e$ maps to $0$
in $\kappa(\mathfrak p)$, see
Lemma \ref{lemma-disjoint-decomposition}.
Any idempotent $e$ which is not in this collection clearly maps to $1$
in $R/I$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-connected-component}
Soit $R$ un anneau.
Une composante connexe de
$\Spec(R)$ est de la forme $V(I)$,
où $I$ est un idéal engendré par des idempotents
tel que tout idempotent de $R$ ait pour image
$0$ ou $1$ dans $R/I$.
\end{lemma}

\begin{proof}
Soit $\mathfrak p$ un idéal premier de $R$. D'après le
lemme \ref{lemma-topology-spec},
nous voyons que les hypothèses de
Topologie, lemme \ref{topology-lemma-connected-component-intersection},
sont satisfaites pour l'espace topologique $\Spec(R)$.
Par conséquent, la composante connexe de $\mathfrak p$ dans $\Spec(R)$
est l'intersection des sous-ensembles ouverts et fermés de $\Spec(R)$
qui contiennent $\mathfrak p$. Elle est donc égale à $V(I)$, où
$I$ est engendré par les idempotents $e \in R$, tels que $e$ ait pour image $0$
dans $\kappa(\mathfrak p)$ ; voir le
lemme \ref{lemma-disjoint-decomposition}.
Tout idempotent $e$ qui n'appartient pas à cette famille a manifestement pour image $1$
dans $R/I$.
\end{proof}
```

</details>

### 10 — section-more-glueing

Anglais L4041–4049 ; français L4021–4029.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4041) · FR-ALGEBRA-B6-CHOICE-0010.

Le titre « Propriétés de recollement » et l'introduction portent sur la vérification locale d'une propriété, non sur l'existence automatique d'un recollement d'objets. Standard opens devient ouverts principaux, et all members conserve la quantification sur le recouvrement. Le texte distingue vérification sur ces ouverts et vérification aux anneaux locaux. L'emploi « locale pour la topologie de Zariski » chez Dat §1.7, p.29, appuie le registre ; ses hypothèses de descente ne sont pas importées.

Règles : FR-ALGEBRA-B6-RULE-TOPOLOGIE, FR-ALGEBRA-B6-RULE-RECOLLEMENT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Glueing properties}
\label{section-more-glueing}

\noindent
In this section we put a number of standard results of the
form: if something is true for all members of a standard open
covering then it is true. In fact, it often suffices to check
things on the level of local rings as in the following lemma.
```

Français restauré :
```tex
\section{Propriétés de recollement}
\label{section-more-glueing}

\noindent
Dans cette section, nous rassemblons plusieurs résultats classiques de la
forme suivante : si une propriété est vraie sur tous les membres d'un
recouvrement par des ouverts principaux, alors elle est vraie. En fait, il suffit souvent de vérifier
les propriétés au niveau des anneaux locaux, comme dans le lemme suivant.
```

</details>

### 11 — lemma-characterize-zero-local

Anglais L4050–4132 ; français L4030–4112.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4050) · FR-ALGEBRA-B6-CHOICE-0011.

Les six assertions et toutes leurs sous-conditions ont été comparées : nullité d'un élément, nullité d'un module, exactitude, injectivité, surjectivité et bijectivité. Les tests aux idéaux premiers et aux maximaux restent distincts et universels ; aucune finitude n'est ajoutée. L'annulateur est celui de x ; l'idéal unité n'est pas l'ensemble des seuls éléments inversibles. L'homologie Ker/Im et l'exactitude de la localisation fondent la réduction. Dat p.19 fournit une comparaison du langage local des faisceaux, mais ne remplace pas ce lemme de modules ni n'autorise à appeler les groupes abéliens des modules sur un anneau structural inexistant.

Règles : FR-ALGEBRA-B6-RULE-LOCALISATION, FR-ALGEBRA-B6-RULE-MORPHISMES, FR-ALGEBRA-B6-RULE-EXACTITUDE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-zero-local}
Let $R$ be a ring.
\begin{enumerate}
\item For an element $x$ of an $R$-module $M$ the following are equivalent
\begin{enumerate}
\item $x = 0$,
\item $x$ maps to zero in $M_\mathfrak p$ for all $\mathfrak p \in \Spec(R)$,
\item $x$ maps to zero in $M_{\mathfrak m}$ for all maximal ideals
$\mathfrak m$ of $R$.
\end{enumerate}
In other words, the map $M \to \prod_{\mathfrak m} M_{\mathfrak m}$
is injective.
\item Given an $R$-module $M$ the following are equivalent
\begin{enumerate}
\item $M$ is zero,
\item $M_{\mathfrak p}$ is zero for all $\mathfrak p \in \Spec(R)$,
\item $M_{\mathfrak m}$ is zero for all maximal ideals $\mathfrak m$ of $R$.
\end{enumerate}
\item Given a complex $M_1 \to M_2 \to M_3$
of $R$-modules the following are equivalent
\begin{enumerate}
\item $M_1 \to M_2 \to M_3$ is exact,
\item for every prime $\mathfrak p$ of $R$ the localization
$M_{1, \mathfrak p} \to M_{2, \mathfrak p} \to M_{3, \mathfrak p}$
is exact,
\item for every maximal ideal $\mathfrak m$ of $R$ the localization
$M_{1, \mathfrak m} \to M_{2, \mathfrak m} \to M_{3, \mathfrak m}$
is exact.
\end{enumerate}
\item Given a map $f : M \to M'$ of $R$-modules the following are equivalent
\begin{enumerate}
\item $f$ is injective,
\item $f_{\mathfrak p} : M_\mathfrak p \to M'_\mathfrak p$ is injective
for all primes $\mathfrak p$ of $R$,
\item $f_{\mathfrak m} : M_\mathfrak m \to M'_\mathfrak m$ is injective
for all maximal ideals $\mathfrak m$ of $R$.
\end{enumerate}
\item Given a map $f : M \to M'$ of $R$-modules the following are equivalent
\begin{enumerate}
\item $f$ is surjective,
\item $f_{\mathfrak p} : M_\mathfrak p \to M'_\mathfrak p$ is surjective
for all primes $\mathfrak p$ of $R$,
\item $f_{\mathfrak m} : M_\mathfrak m \to M'_\mathfrak m$ is surjective
for all maximal ideals $\mathfrak m$ of $R$.
\end{enumerate}
\item Given a map $f : M \to M'$ of $R$-modules the following are equivalent
\begin{enumerate}
\item $f$ is bijective,
\item $f_{\mathfrak p} : M_\mathfrak p \to M'_\mathfrak p$ is bijective
for all primes $\mathfrak p$ of $R$,
\item $f_{\mathfrak m} : M_\mathfrak m \to M'_\mathfrak m$ is bijective
for all maximal ideals $\mathfrak m$ of $R$.
\end{enumerate}
\end{enumerate}
\end{lemma}

\begin{proof}
Let $x \in M$ as in (1). Let $I = \{f \in R \mid fx = 0\}$.
It is easy to see that $I$ is an ideal (it is the
annihilator of $x$). Condition (1)(c) means that for
all maximal ideals $\mathfrak m$ there exists an
$f \in R \setminus \mathfrak m$ such that $fx =0$.
In other words, $V(I)$ does not contain a closed point.
By Lemma \ref{lemma-Zariski-topology} we see $I$ is the unit ideal.
Hence $x$ is zero, i.e., (1)(a) holds. This proves (1).

\medskip\noindent
Part (2) follows by applying (1) to all elements of $M$ simultaneously.

\medskip\noindent
Proof of (3). Let $H$ be the homology of the sequence, i.e.,
$H = \Ker(M_2 \to M_3)/\Im(M_1 \to M_2)$. By
Proposition \ref{proposition-localization-exact}
we have that $H_\mathfrak p$ is the homology of the sequence
$M_{1, \mathfrak p} \to M_{2, \mathfrak p} \to M_{3, \mathfrak p}$.
Hence (3) is a consequence of (2).

\medskip\noindent
Parts (4) and (5) are special cases of (3). Part (6) follows
formally on combining (4) and (5).
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-characterize-zero-local}
Soit $R$ un anneau.
\begin{enumerate}
\item Pour un élément $x$ d'un $R$-module $M$, les conditions suivantes sont équivalentes :
\begin{enumerate}
\item $x = 0$,
\item l'image de $x$ dans $M_\mathfrak p$ est nulle pour tout $\mathfrak p \in \Spec(R)$,
\item l'image de $x$ dans $M_{\mathfrak m}$ est nulle pour tout idéal maximal
$\mathfrak m$ de $R$.
\end{enumerate}
Autrement dit, le morphisme $M \to \prod_{\mathfrak m} M_{\mathfrak m}$
est injectif.
\item Pour un $R$-module $M$, les conditions suivantes sont équivalentes :
\begin{enumerate}
\item $M$ est nul,
\item $M_{\mathfrak p}$ est nul pour tout $\mathfrak p \in \Spec(R)$,
\item $M_{\mathfrak m}$ est nul pour tout idéal maximal $\mathfrak m$ de $R$.
\end{enumerate}
\item Pour un complexe $M_1 \to M_2 \to M_3$
de $R$-modules, les conditions suivantes sont équivalentes :
\begin{enumerate}
\item $M_1 \to M_2 \to M_3$ est exact,
\item pour tout idéal premier $\mathfrak p$ de $R$, le complexe localisé
$M_{1, \mathfrak p} \to M_{2, \mathfrak p} \to M_{3, \mathfrak p}$
est exact,
\item pour tout idéal maximal $\mathfrak m$ de $R$, le complexe localisé
$M_{1, \mathfrak m} \to M_{2, \mathfrak m} \to M_{3, \mathfrak m}$
est exact.
\end{enumerate}
\item Pour un morphisme $f : M \to M'$ de $R$-modules, les conditions suivantes sont équivalentes :
\begin{enumerate}
\item $f$ est injectif,
\item $f_{\mathfrak p} : M_\mathfrak p \to M'_\mathfrak p$ est injectif
pour tout idéal premier $\mathfrak p$ de $R$,
\item $f_{\mathfrak m} : M_\mathfrak m \to M'_\mathfrak m$ est injectif
pour tout idéal maximal $\mathfrak m$ de $R$.
\end{enumerate}
\item Pour un morphisme $f : M \to M'$ de $R$-modules, les conditions suivantes sont équivalentes :
\begin{enumerate}
\item $f$ est surjectif,
\item $f_{\mathfrak p} : M_\mathfrak p \to M'_\mathfrak p$ est surjectif
pour tout idéal premier $\mathfrak p$ de $R$,
\item $f_{\mathfrak m} : M_\mathfrak m \to M'_\mathfrak m$ est surjectif
pour tout idéal maximal $\mathfrak m$ de $R$.
\end{enumerate}
\item Pour un morphisme $f : M \to M'$ de $R$-modules, les conditions suivantes sont équivalentes :
\begin{enumerate}
\item $f$ est bijectif,
\item $f_{\mathfrak p} : M_\mathfrak p \to M'_\mathfrak p$ est bijectif
pour tout idéal premier $\mathfrak p$ de $R$,
\item $f_{\mathfrak m} : M_\mathfrak m \to M'_\mathfrak m$ est bijectif
pour tout idéal maximal $\mathfrak m$ de $R$.
\end{enumerate}
\end{enumerate}
\end{lemma}

\begin{proof}
Soit $x \in M$ comme dans (1). Soit $I = \{f \in R \mid fx = 0\}$.
Il est facile de voir que $I$ est un idéal (c'est
l'annulateur de $x$). La condition (1)(c) signifie que, pour
tout idéal maximal $\mathfrak m$, il existe
$f \in R \setminus \mathfrak m$ tel que $fx =0$.
Autrement dit, $V(I)$ ne contient aucun point fermé.
D'après le lemme \ref{lemma-Zariski-topology}, nous voyons que $I$ est l'idéal unité.
Ainsi $x$ est nul, c'est-à-dire que (1)(a) est satisfaite. Cela démontre (1).

\medskip\noindent
La partie (2) résulte de l'application simultanée de (1) à tous les éléments de $M$.

\medskip\noindent
Démonstration de (3). Soit $H$ l'homologie de la suite, c'est-à-dire
$H = \Ker(M_2 \to M_3)/\Im(M_1 \to M_2)$. D'après la
proposition \ref{proposition-localization-exact},
$H_\mathfrak p$ est l'homologie de la suite
$M_{1, \mathfrak p} \to M_{2, \mathfrak p} \to M_{3, \mathfrak p}$.
Ainsi (3) résulte de (2).

\medskip\noindent
Les parties (4) et (5) sont des cas particuliers de (3). La partie (6) résulte
formellement de la combinaison de (4) et (5).
\end{proof}
```

</details>

### 12 — lemma-cover

Anglais L4133–4218 ; français L4113–4198.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4133) · FR-ALGEBRA-B6-CHOICE-0012.

Les huit assertions et leurs huit preuves sont préservées. Finite module devient module de type fini, tandis que finitely presented devient de présentation finie ; ni l'un ni l'autre ne signifie un ensemble fini. Le slogan local pour Zariski garde son sens de vérification sur un recouvrement. Les éléments f_i sont dans R, et les algèbres localisées sont sur R_fi. Les antécédents choisis, la réunion finie Y, le module quotient S/T et le noyau idéal dans l'anneau de polynômes restent distincts. S/T n'est pas présenté comme un anneau quotient. Le n réemployé par la source pour le rang d'un libre et la longueur du recouvrement n'est pas renommé.

Point particulier à relire : Le registre « de type fini » ne certifie pas la preuve par une recherche de mots. Les huit démonstrations, notamment le quotient de modules S/T et les bases de localisation, ont été lues dans leur totalité.

Règles : FR-ALGEBRA-B6-RULE-LOCALISATION, FR-ALGEBRA-B6-RULE-FINITUDE, FR-ALGEBRA-B6-RULE-MORPHISMES, FR-ALGEBRA-B6-RULE-EXACTITUDE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-cover}
\begin{slogan}
Zariski-local properties of modules and algebras
\end{slogan}
Let $R$ be a ring. Let $M$ be an $R$-module. Let $S$ be an $R$-algebra.
Suppose that $f_1, \ldots, f_n$ is a finite list of
elements of $R$ such that $\bigcup D(f_i) = \Spec(R)$,
in other words $(f_1, \ldots, f_n) = R$.
\begin{enumerate}
\item If each $M_{f_i} = 0$ then $M = 0$.
\item If each $M_{f_i}$ is a finite $R_{f_i}$-module,
then $M$ is a finite $R$-module.
\item If each $M_{f_i}$ is a finitely presented $R_{f_i}$-module,
then $M$ is a finitely presented $R$-module.
\item Let $M \to N$ be a map of $R$-modules. If $M_{f_i} \to N_{f_i}$
is an isomorphism for each $i$ then $M \to N$ is an isomorphism.
\item Let $0 \to M'' \to M \to M' \to 0$ be a complex of $R$-modules.
If $0 \to M''_{f_i} \to M_{f_i} \to M'_{f_i} \to 0$ is exact for each $i$,
then $0 \to M'' \to M \to M' \to 0$ is exact.
\item If each $R_{f_i}$ is Noetherian, then $R$ is Noetherian.
\item If each $S_{f_i}$ is a finite type $R_{f_i}$-algebra, then
$S$ is a finite type $R$-algebra.
\item If each $S_{f_i}$ is of finite presentation over $R_{f_i}$, then
$S$ is a finitely presented $R$-algebra.
\end{enumerate}
\end{lemma}

\begin{proof}
We prove each of the parts in turn.
\begin{enumerate}
\item By Proposition \ref{proposition-localize-twice}
this implies $M_\mathfrak p = 0$ for all $\mathfrak p \in \Spec(R)$,
so we conclude by Lemma \ref{lemma-characterize-zero-local}.
\item For each $i$ take a finite generating set $X_i$ of $M_{f_i}$.
Without loss of generality, we may assume that the elements of $X_i$ are
in the image of the localization map $M \rightarrow M_{f_i}$, so we take
a finite set $Y_i$ of preimages of the elements of $X_i$ in $M$. Let $Y$
be the union of these sets. This is still a finite set.
Consider the obvious $R$-linear map $R^Y \rightarrow M$ sending the basis
element $e_y$ to $y$. By assumption this map is surjective after localizing
at an arbitrary prime ideal $\mathfrak p$ of $R$, so it is surjective by
Lemma \ref{lemma-characterize-zero-local}
and $M$ is finitely generated.
\item By (2) we have a short exact sequence
$$
0 \rightarrow K \rightarrow R^n \rightarrow M \rightarrow 0
$$
Since localization is an exact functor and $M_{f_i}$ is finitely
presented we see that $K_{f_i}$ is finitely generated for all
$1 \leq i \leq n$ by Lemma \ref{lemma-extension}.
By (2) this implies that $K$ is a finite $R$-module and therefore
$M$ is finitely presented.
\item By Proposition \ref{proposition-localize-twice}
the assumption implies that the induced morphism
on localizations at all prime ideals is an isomorphism, so we conclude
by Lemma \ref{lemma-characterize-zero-local}.
\item By Proposition \ref{proposition-localize-twice} the assumption
implies that the induced
sequence of localizations at all prime ideals is short exact, so we
conclude by Lemma \ref{lemma-characterize-zero-local}.
\item We will show that every ideal of $R$ has a finite generating set:
For this, let $I \subset R$ be an arbitrary ideal. By
Proposition \ref{proposition-localization-exact}
each $I_{f_i} \subset R_{f_i}$ is an ideal. These are all
finitely generated by assumption, so we conclude by (2).
\item For each $i$ take a finite generating set $X_i$ of $S_{f_i}$.
Without loss of generality, we may assume that the elements of $X_i$
are in the image of the localization map $S \rightarrow S_{f_i}$, so
we take a finite set $Y_i$ of preimages of the elements of $X_i$ in
$S$. Let $Y$ be the union of these sets. This is still a finite set.
Consider the algebra homomorphism $R[X_y]_{y \in Y} \rightarrow S$
induced by $Y$. Since it is an algebra homomorphism, the image $T$
is an $R$-submodule of the $R$-module $S$, so we can consider the
quotient module $S/T$. By assumption, this is zero if we localize
at the $f_i$, so it is zero by (1) and therefore $S$ is an
$R$-algebra of finite type.
\item By the previous item, there exists a surjective $R$-algebra
homomorphism $R[X_1, \ldots, X_n] \rightarrow S$. Let $K$ be the kernel
of this map. This is an ideal in $R[X_1, \ldots, X_n]$, finitely generated
in each localization at $f_i$. Since the $f_i$ generate the unit ideal
in $R$, they also generate the unit ideal in $R[X_1, \ldots, X_n]$, so an
application of (2) finishes the proof.
\end{enumerate}
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-cover}
\begin{slogan}
Propriétés locales pour Zariski des modules et des algèbres
\end{slogan}
Soit $R$ un anneau. Soit $M$ un $R$-module. Soit $S$ une $R$-algèbre.
Supposons que $f_1, \ldots, f_n$ soit une liste finie
d'éléments de $R$ telle que $\bigcup D(f_i) = \Spec(R)$,
autrement dit $(f_1, \ldots, f_n) = R$.
\begin{enumerate}
\item Si chaque $M_{f_i} = 0$, alors $M = 0$.
\item Si chaque $M_{f_i}$ est un $R_{f_i}$-module de type fini,
alors $M$ est un $R$-module de type fini.
\item Si chaque $M_{f_i}$ est un $R_{f_i}$-module de présentation finie,
alors $M$ est un $R$-module de présentation finie.
\item Soit $M \to N$ un morphisme de $R$-modules. Si $M_{f_i} \to N_{f_i}$
est un isomorphisme pour tout $i$, alors $M \to N$ est un isomorphisme.
\item Soit $0 \to M'' \to M \to M' \to 0$ un complexe de $R$-modules.
Si $0 \to M''_{f_i} \to M_{f_i} \to M'_{f_i} \to 0$ est exact pour tout $i$,
alors $0 \to M'' \to M \to M' \to 0$ est exact.
\item Si chaque $R_{f_i}$ est noethérien, alors $R$ est noethérien.
\item Si chaque $S_{f_i}$ est une $R_{f_i}$-algèbre de type fini, alors
$S$ est une $R$-algèbre de type fini.
\item Si chaque $S_{f_i}$ est de présentation finie sur $R_{f_i}$, alors
$S$ est une $R$-algèbre de présentation finie.
\end{enumerate}
\end{lemma}

\begin{proof}
Démontrons successivement chacune des parties.
\begin{enumerate}
\item D'après la proposition \ref{proposition-localize-twice},
cela entraîne que $M_\mathfrak p = 0$ pour tout $\mathfrak p \in \Spec(R)$ ;
nous concluons donc par le lemme \ref{lemma-characterize-zero-local}.
\item Pour chaque $i$, choisissons un ensemble fini de générateurs $X_i$ de $M_{f_i}$.
Nous pouvons supposer sans perte de généralité que les éléments de $X_i$
appartiennent à l'image du morphisme de localisation $M \rightarrow M_{f_i}$ ; prenons donc
un ensemble fini $Y_i$ d'antécédents des éléments de $X_i$ dans $M$. Soit $Y$
la réunion de ces ensembles. C'est encore un ensemble fini.
Considérons le morphisme $R$-linéaire évident $R^Y \rightarrow M$ qui envoie l'élément
de base $e_y$ sur $y$. D'après l'hypothèse, ce morphisme est surjectif après localisation
en tout idéal premier $\mathfrak p$ de $R$ ; il est donc surjectif d'après le
lemme \ref{lemma-characterize-zero-local},
et $M$ est de type fini.
\item D'après (2), nous avons une suite exacte courte
$$
0 \rightarrow K \rightarrow R^n \rightarrow M \rightarrow 0
$$
Puisque la localisation est un foncteur exact et que $M_{f_i}$ est de présentation
finie, nous voyons que $K_{f_i}$ est de type fini pour tout
$1 \leq i \leq n$ d'après le lemme \ref{lemma-extension}.
D'après (2), cela entraîne que $K$ est un $R$-module de type fini et donc que
$M$ est de présentation finie.
\item D'après la proposition \ref{proposition-localize-twice},
l'hypothèse entraîne que le morphisme induit
sur les localisés en tous les idéaux premiers est un isomorphisme ; nous concluons donc
par le lemme \ref{lemma-characterize-zero-local}.
\item D'après la proposition \ref{proposition-localize-twice}, l'hypothèse
entraîne que la
suite des localisés en tous les idéaux premiers est exacte courte ; nous
concluons donc par le lemme \ref{lemma-characterize-zero-local}.
\item Nous allons montrer que tout idéal de $R$ possède un ensemble fini de générateurs.
Pour cela, soit $I \subset R$ un idéal arbitraire. D'après la
proposition \ref{proposition-localization-exact},
chaque $I_{f_i} \subset R_{f_i}$ est un idéal. Ils sont tous
de type fini par hypothèse, et nous concluons donc par (2).
\item Pour chaque $i$, choisissons un ensemble fini de générateurs $X_i$ de $S_{f_i}$.
Nous pouvons supposer sans perte de généralité que les éléments de $X_i$
appartiennent à l'image du morphisme de localisation $S \rightarrow S_{f_i}$ ; prenons donc
un ensemble fini $Y_i$ d'antécédents des éléments de $X_i$ dans
$S$. Soit $Y$ la réunion de ces ensembles. C'est encore un ensemble fini.
Considérons le morphisme d'algèbres $R[X_y]_{y \in Y} \rightarrow S$
induit par $Y$. Puisqu'il s'agit d'un morphisme d'algèbres, l'image $T$
est un $R$-sous-module du $R$-module $S$ ; nous pouvons donc considérer le
module quotient $S/T$. D'après l'hypothèse, celui-ci est nul après localisation
en chacun des $f_i$ ; il est donc nul d'après (1), et $S$ est par conséquent une
$R$-algèbre de type fini.
\item D'après le point précédent, il existe un morphisme surjectif de $R$-algèbres
$R[X_1, \ldots, X_n] \rightarrow S$. Soit $K$ le noyau
de ce morphisme. C'est un idéal de $R[X_1, \ldots, X_n]$, de type fini
après chacune des localisations en $f_i$. Puisque les $f_i$ engendrent l'idéal unité
dans $R$, ils engendrent également l'idéal unité dans $R[X_1, \ldots, X_n]$ ; une
application de (2) achève donc la démonstration.
\end{enumerate}
\end{proof}
```

</details>

### 13 — lemma-cover-upstairs

Anglais L4219–4283 ; français L4199–4263.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4219) · FR-ALGEBRA-B6-CHOICE-0013.

Cette fois les g_i appartiennent à S, pas à R ; le type fini et la présentation finie restent relatifs à R. Les h_i garantissent que les g_i engendrent aussi l'idéal unité dans S'. Le français garde l'injectivité issue de l'exactitude, la surjectivité obtenue par les générateurs, puis la lecture comme morphisme de S'-modules. Pour (2), relèvement désigne le choix d'un antécédent polynomial, non un changement de base. Le détail omis, l'idéal J_i et la relation sum h'_ig'_i−1 sont présents. Aucune hypothèse de platitude n'est ajoutée.

Règles : FR-ALGEBRA-B6-RULE-LOCALISATION, FR-ALGEBRA-B6-RULE-FINITUDE, FR-ALGEBRA-B6-RULE-MORPHISMES, FR-ALGEBRA-B6-RULE-EXACTITUDE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-cover-upstairs}
Let $R \to S$ be a ring map.
Suppose that $g_1, \ldots, g_n$ is a finite list of
elements of $S$ such that $\bigcup D(g_i) = \Spec(S)$
in other words $(g_1, \ldots, g_n) = S$.
\begin{enumerate}
\item If each $S_{g_i}$ is of finite type over $R$, then $S$ is
of finite type over $R$.
\item If each $S_{g_i}$ is of finite presentation over $R$,
then $S$ is of finite presentation over $R$.
\end{enumerate}
\end{lemma}

\begin{proof}
Choose $h_1, \ldots, h_n \in S$ such that $\sum h_i g_i = 1$.

\medskip\noindent
Proof of (1). For each $i$ choose a finite list of elements
$x_{i, j} \in S_{g_i}$, $j = 1, \ldots, m_i$
which generate $S_{g_i}$ as an $R$-algebra.
Write $x_{i, j} = y_{i, j}/g_i^{n_{i, j}}$ for some $y_{i, j} \in S$ and
some $n_{i, j} \ge 0$. Consider the $R$-subalgebra $S' \subset S$
generated by $g_1, \ldots, g_n$, $h_1, \ldots, h_n$ and
$y_{i, j}$, $i = 1, \ldots, n$, $j = 1, \ldots, m_i$.
Since localization is exact (Proposition \ref{proposition-localization-exact}),
we see that $S'_{g_i} \to S_{g_i}$ is injective.
On the other hand, it is surjective by our choice of $y_{i, j}$.
The elements $g_1, \ldots, g_n$ generate the unit ideal in $S'$
as $h_1, \ldots, h_n \in S'$.
Thus $S' \to S$ viewed as an $S'$-module map is an isomorphism
by Lemma \ref{lemma-cover}.

\medskip\noindent
Proof of (2). We already know that $S$ is of finite type.
Write $S = R[x_1, \ldots, x_m]/J$ for some ideal $J$.
For each $i$ choose a lift $g'_i \in R[x_1, \ldots, x_m]$ of $g_i$
and we choose a lift $h'_i \in R[x_1, \ldots, x_m]$ of $h_i$.
Then we see that
$$
S_{g_i} = R[x_1, \ldots, x_m, y_i]/(J_i + (1 - y_ig'_i))
$$
where $J_i$ is the ideal of $R[x_1, \ldots, x_m, y_i]$
generated by $J$. Small detail omitted. By
Lemma \ref{lemma-finite-presentation-independent}
we may choose a finite list of elements
$f_{i, j} \in J$, $j = 1, \ldots, m_i$
such that the images of $f_{i, j}$ in $J_i$ and $1 - y_ig'_i$
generate the ideal $J_i + (1 - y_ig'_i)$.
Set
$$
S' = R[x_1, \ldots, x_m]/\left(\sum h'_ig'_i - 1, f_{i, j}; 
i = 1, \ldots, n, j = 1, \ldots, m_i\right)
$$
There is a surjective $R$-algebra map $S' \to S$.
The classes of the elements $g'_1, \ldots, g'_n$ in $S'$
generate the unit ideal and by construction the maps
$S'_{g'_i} \to S_{g_i}$ are injective.
Thus we conclude as in part (1).
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-cover-upstairs}
Soit $R \to S$ un morphisme d'anneaux.
Supposons que $g_1, \ldots, g_n$ soit une liste finie
d'éléments de $S$ telle que $\bigcup D(g_i) = \Spec(S)$,
autrement dit $(g_1, \ldots, g_n) = S$.
\begin{enumerate}
\item Si chaque $S_{g_i}$ est de type fini sur $R$, alors $S$ est
de type fini sur $R$.
\item Si chaque $S_{g_i}$ est de présentation finie sur $R$,
alors $S$ est de présentation finie sur $R$.
\end{enumerate}
\end{lemma}

\begin{proof}
Choisissons $h_1, \ldots, h_n \in S$ tels que $\sum h_i g_i = 1$.

\medskip\noindent
Démonstration de (1). Pour chaque $i$, choisissons une liste finie d'éléments
$x_{i, j} \in S_{g_i}$, $j = 1, \ldots, m_i$,
qui engendrent $S_{g_i}$ comme $R$-algèbre.
Écrivons $x_{i, j} = y_{i, j}/g_i^{n_{i, j}}$ pour un certain $y_{i, j} \in S$ et
un certain $n_{i, j} \ge 0$. Considérons la $R$-sous-algèbre $S' \subset S$
engendrée par $g_1, \ldots, g_n$, $h_1, \ldots, h_n$ et
les $y_{i, j}$, $i = 1, \ldots, n$, $j = 1, \ldots, m_i$.
Puisque la localisation est exacte (proposition \ref{proposition-localization-exact}),
nous voyons que $S'_{g_i} \to S_{g_i}$ est injectif.
D'autre part, il est surjectif par notre choix des $y_{i, j}$.
Les éléments $g_1, \ldots, g_n$ engendrent l'idéal unité dans $S'$
puisque $h_1, \ldots, h_n \in S'$.
Ainsi, $S' \to S$, considéré comme un morphisme de $S'$-modules, est un isomorphisme
d'après le lemme \ref{lemma-cover}.

\medskip\noindent
Démonstration de (2). Nous savons déjà que $S$ est de type fini.
Écrivons $S = R[x_1, \ldots, x_m]/J$ pour un certain idéal $J$.
Pour chaque $i$, choisissons un relèvement $g'_i \in R[x_1, \ldots, x_m]$ de $g_i$
et choisissons un relèvement $h'_i \in R[x_1, \ldots, x_m]$ de $h_i$.
Nous voyons alors que
$$
S_{g_i} = R[x_1, \ldots, x_m, y_i]/(J_i + (1 - y_ig'_i))
$$
où $J_i$ est l'idéal de $R[x_1, \ldots, x_m, y_i]$
engendré par $J$. Nous omettons un petit détail. D'après le
lemme \ref{lemma-finite-presentation-independent},
nous pouvons choisir une liste finie d'éléments
$f_{i, j} \in J$, $j = 1, \ldots, m_i$,
telle que les images des $f_{i, j}$ dans $J_i$ ainsi que $1 - y_ig'_i$
engendrent l'idéal $J_i + (1 - y_ig'_i)$.
Posons
$$
S' = R[x_1, \ldots, x_m]/\left(\sum h'_ig'_i - 1, f_{i, j}; 
i = 1, \ldots, n, j = 1, \ldots, m_i\right)
$$
Il existe un morphisme surjectif de $R$-algèbres $S' \to S$.
Les classes des éléments $g'_1, \ldots, g'_n$ dans $S'$
engendrent l'idéal unité et, par construction, les morphismes
$S'_{g'_i} \to S_{g_i}$ sont injectifs.
Nous concluons donc comme dans la partie (1).
\end{proof}
```

</details>

### 14 — section-tilde-module-sheaf

Anglais L4284–4305 ; français L4264–4285.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4284) · FR-ALGEBRA-B6-CHOICE-0014.

L'existence ET l'unicité de h, et l'égalité des images h_i,h_j sur les doubles intersections, restent explicitement formulées. Faisceau d'anneaux est la terminologie de Ducros 3.1.11 et Dat 1.3 : il ne faut pas affaiblir en préfaisceau. Les fonctions dites algébriques ou régulières sont une interprétation, conservée entre guillemets, et non l'affirmation que l'anneau est réduit. L'analogie distingue variétés topologiques/fonctions continues et variétés différentiables/fonctions différentiables ; le français ne les confond pas.

Règles : FR-ALGEBRA-B6-RULE-TOPOLOGIE, FR-ALGEBRA-B6-RULE-RECOLLEMENT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Glueing functions}
\label{section-tilde-module-sheaf}

\noindent
In this section we show that given an open covering
$$
\Spec(R) = \bigcup\nolimits_{i = 1}^n D(f_i)
$$
by standard opens, and given an element $h_i \in R_{f_i}$
for each $i$ such that $h_i = h_j$ as elements of $R_{f_i f_j}$
then there exists a unique $h \in R$ such that the image of
$h$ in $R_{f_i}$ is $h_i$. This result can be interpreted
in two ways:
\begin{enumerate}
\item The rule $D(f) \mapsto R_f$ is a sheaf of rings
on the standard opens, see Sheaves, Section \ref{sheaves-section-bases}.
\item If we think of elements of $R_f$ as the ``algebraic''
or ``regular'' functions on $D(f)$, then these glue
as would continuous, resp.\ differentiable functions
on a topological, resp.\ differentiable manifold.
\end{enumerate}
```

Français restauré :
```tex
\section{Recollement de fonctions}
\label{section-tilde-module-sheaf}

\noindent
Dans cette section, nous montrons qu'étant donné un recouvrement ouvert
$$
\Spec(R) = \bigcup\nolimits_{i = 1}^n D(f_i)
$$
par des ouverts principaux, et étant donné un élément $h_i \in R_{f_i}$
pour chaque $i$, tel que $h_i = h_j$ comme éléments de $R_{f_i f_j}$,
il existe un unique $h \in R$ tel que l'image de
$h$ dans $R_{f_i}$ soit $h_i$. Ce résultat peut s'interpréter
de deux manières :
\begin{enumerate}
\item La règle $D(f) \mapsto R_f$ est un faisceau d'anneaux
sur les ouverts principaux ; voir Faisceaux, section \ref{sheaves-section-bases}.
\item Si nous considérons les éléments de $R_f$ comme les fonctions « algébriques »
ou « régulières » sur $D(f)$, alors celles-ci se recollent
comme le feraient les fonctions continues, resp.\ différentiables,
sur une variété topologique, resp.\ différentiable.
\end{enumerate}
```

</details>

### 15 — lemma-cover-module

Anglais L4306–4352 ; français L4286–4332.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4306) · FR-ALGEBRA-B6-CHOICE-0015.

La suite est exacte aux deux places visées sans zéro ajouté à droite ; la surjectivité vers les doubles localisés ne serait pas autorisée. Le signe m_i−m_j et l'ordre des indices sont inchangés. La preuve localise en chaque idéal maximal puis remplace l'unité f_1 par 1 ; elle n'affirme pas que f_1 était inversible dans R avant localisation. Dat p.15 fournit une attestation directe de la suite et de son langage, avec produits finis plutôt que sommes directes. La traduction conserve les sommes de Stacks et sa preuve propre, non la preuve par fidèle platitude de Dat.

Règles : FR-ALGEBRA-B6-RULE-LOCALISATION, FR-ALGEBRA-B6-RULE-MORPHISMES, FR-ALGEBRA-B6-RULE-EXACTITUDE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-cover-module}
Let $R$ be a ring. Let $f_1, \ldots, f_n$ be elements of $R$
generating the unit ideal. Let $M$ be an $R$-module.
The sequence
$$
0 \to
M \xrightarrow{\alpha}
\bigoplus\nolimits_{i = 1}^n M_{f_i} \xrightarrow{\beta}
\bigoplus\nolimits_{i, j = 1}^n M_{f_i f_j}
$$
is exact, where $\alpha(m) = (m/1, \ldots, m/1)$
and $\beta(m_1/f_1^{e_1}, \ldots, m_n/f_n^{e_n})
= (m_i/f_i^{e_i} - m_j/f_j^{e_j})_{(i, j)}$.
\end{lemma}

\begin{proof}
It suffices to show that the localization of the sequence at
any maximal ideal $\mathfrak m$ is exact, see
Lemma \ref{lemma-characterize-zero-local}.
Since $f_1, \ldots, f_n$ generate the unit ideal,
there is an $i$ such that $f_i \not \in \mathfrak m$.
After renumbering we may assume $i = 1$.
Note that $(M_{f_i})_\mathfrak m = (M_\mathfrak m)_{f_i}$
and $(M_{f_if_j})_\mathfrak m = (M_\mathfrak m)_{f_if_j}$, see
Proposition \ref{proposition-localize-twice-module}.
In particular $(M_{f_1})_\mathfrak m = M_\mathfrak m$ and
$(M_{f_1 f_i})_\mathfrak m = (M_\mathfrak m)_{f_i}$, because
$f_1$ is a unit.
Note that the maps in the sequence are the canonical ones
coming from
Lemma \ref{lemma-universal-property-localization-module}
and the identity map on $M$.
Having said all of this, after replacing $R$ by $R_\mathfrak m$,
$M$ by $M_\mathfrak m$, and $f_i$ by their image in $R_\mathfrak m$,
and $f_1$ by $1 \in R_\mathfrak m$,
we reduce to the case where $f_1 = 1$.

\medskip\noindent
Assume $f_1 = 1$. Injectivity of $\alpha$ is now trivial. Let
$m = (m_i) \in \bigoplus_{i = 1}^n M_{f_i}$ be in the kernel of $\beta$.
Then $m_1 \in M_{f_1} = M$. Moreover, $\beta(m) = 0$
implies that $m_1$ and $m_i$ map to the same element of
$M_{f_1f_i} = M_{f_i}$. Thus $\alpha(m_1) = m$ and the
proof is complete.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-cover-module}
Soit $R$ un anneau. Soient $f_1, \ldots, f_n$ des éléments de $R$
qui engendrent l'idéal unité. Soit $M$ un $R$-module.
La suite
$$
0 \to
M \xrightarrow{\alpha}
\bigoplus\nolimits_{i = 1}^n M_{f_i} \xrightarrow{\beta}
\bigoplus\nolimits_{i, j = 1}^n M_{f_i f_j}
$$
est exacte, où $\alpha(m) = (m/1, \ldots, m/1)$
et $\beta(m_1/f_1^{e_1}, \ldots, m_n/f_n^{e_n})
= (m_i/f_i^{e_i} - m_j/f_j^{e_j})_{(i, j)}$.
\end{lemma}

\begin{proof}
Il suffit de montrer que la localisation de la suite en
tout idéal maximal $\mathfrak m$ est exacte ; voir le
lemme \ref{lemma-characterize-zero-local}.
Puisque $f_1, \ldots, f_n$ engendrent l'idéal unité,
il existe $i$ tel que $f_i \not \in \mathfrak m$.
Après renumérotation, nous pouvons supposer que $i = 1$.
Notons que $(M_{f_i})_\mathfrak m = (M_\mathfrak m)_{f_i}$
et que $(M_{f_if_j})_\mathfrak m = (M_\mathfrak m)_{f_if_j}$ ; voir la
proposition \ref{proposition-localize-twice-module}.
En particulier, $(M_{f_1})_\mathfrak m = M_\mathfrak m$ et
$(M_{f_1 f_i})_\mathfrak m = (M_\mathfrak m)_{f_i}$, car
$f_1$ est une unité.
Notons que les morphismes de la suite sont les morphismes canoniques
provenant du
lemme \ref{lemma-universal-property-localization-module}
et du morphisme identité de $M$.
Cela étant dit, après avoir remplacé $R$ par $R_\mathfrak m$,
$M$ par $M_\mathfrak m$, les $f_i$ par leurs images dans $R_\mathfrak m$
et $f_1$ par $1 \in R_\mathfrak m$,
nous nous ramenons au cas où $f_1 = 1$.

\medskip\noindent
Supposons $f_1 = 1$. L'injectivité de $\alpha$ est alors immédiate. Soit
$m = (m_i) \in \bigoplus_{i = 1}^n M_{f_i}$ un élément du noyau de $\beta$.
Alors $m_1 \in M_{f_1} = M$. De plus, $\beta(m) = 0$
entraîne que $m_1$ et $m_i$ ont la même image dans
$M_{f_1f_i} = M_{f_i}$. Ainsi $\alpha(m_1) = m$, ce qui
achève la démonstration.
\end{proof}
```

</details>

### 16 — lemma-standard-covering

Anglais L4353–4383 ; français L4333–4363.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4353) · FR-ALGEBRA-B6-CHOICE-0016.

Le cas des anneaux est explicitement déduit du cas des modules. Les deux morphismes et la différence de fractions sont conservés. Deux mots lisibles changent dans un seul affichage : and→et et in→dans ; le contrôle admet exactement ce bloc, pas un masque global du texte mathématique. Le passage annonçant la reformulation suivante reste joint à la preuve. L'exactitude ne devient pas une suite exacte courte.

Règles : FR-ALGEBRA-B6-RULE-LOCALISATION, FR-ALGEBRA-B6-RULE-MORPHISMES, FR-ALGEBRA-B6-RULE-EXACTITUDE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-standard-covering}
Let $R$ be a ring, and let $f_1, f_2, \ldots f_n\in R$ generate
the unit ideal in $R$.
Then the following sequence is exact:
$$
0 \longrightarrow
R \longrightarrow
\bigoplus\nolimits_i R_{f_i} \longrightarrow
\bigoplus\nolimits_{i, j}R_{f_if_j}
$$
where the maps $\alpha : R \longrightarrow \bigoplus_i R_{f_i}$
and $\beta : \bigoplus_i R_{f_i} \longrightarrow \bigoplus_{i, j} R_{f_if_j}$
are defined as
$$
\alpha(x) = \left(\frac{x}{1}, \ldots, \frac{x}{1}\right)
\text{ and }
\beta\left(\frac{x_1}{f_1^{r_1}}, \ldots, \frac{x_n}{f_n^{r_n}}\right)
=
\left(\frac{x_i}{f_i^{r_i}}-\frac{x_j}{f_j^{r_j}}~\text{in}~R_{f_if_j}\right).
$$
\end{lemma}

\begin{proof}
Special case of Lemma \ref{lemma-cover-module}.
\end{proof}

\noindent
The following we have already seen above, but we state it explicitly here
for convenience.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-standard-covering}
Soit $R$ un anneau, et soient $f_1, f_2, \ldots f_n\in R$ des éléments qui engendrent
l'idéal unité de $R$.
Alors la suite suivante est exacte :
$$
0 \longrightarrow
R \longrightarrow
\bigoplus\nolimits_i R_{f_i} \longrightarrow
\bigoplus\nolimits_{i, j}R_{f_if_j}
$$
où les morphismes $\alpha : R \longrightarrow \bigoplus_i R_{f_i}$
et $\beta : \bigoplus_i R_{f_i} \longrightarrow \bigoplus_{i, j} R_{f_if_j}$
sont définis par
$$
\alpha(x) = \left(\frac{x}{1}, \ldots, \frac{x}{1}\right)
\text{ et }
\beta\left(\frac{x_1}{f_1^{r_1}}, \ldots, \frac{x_n}{f_n^{r_n}}\right)
=
\left(\frac{x_i}{f_i^{r_i}}-\frac{x_j}{f_j^{r_j}}~\text{dans}~R_{f_if_j}\right).
$$
\end{lemma}

\begin{proof}
C'est un cas particulier du lemme \ref{lemma-cover-module}.
\end{proof}

\noindent
Nous avons déjà vu le résultat suivant ci-dessus, mais nous l'énonçons explicitement ici
pour plus de commodité.
```

</details>

### 17 — lemma-disjoint-implies-product

Anglais L4384–4403 ; français L4364–4383.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4384) · FR-ALGEBRA-B6-CHOICE-0017.

Les deux parties sont ouvertes et disjointes et recouvrent le spectre ; ainsi leurs localisations et quotients sont compatibles avec le produit d'anneaux. La traduction conserve les deux qualités localisations ET quotients, et le fait que R_e(1−e) est nul. La condition de recollement devient triviale dans ce cas précis, pas pour tout recouvrement. Ducros 4.1.28 explique les mêmes identifications ; aucune preuve externe n'est substituée à la preuve source.

Règles : FR-ALGEBRA-B6-RULE-IDEMPOTENTS, FR-ALGEBRA-B6-RULE-LOCALISATION, FR-ALGEBRA-B6-RULE-MORPHISMES, FR-ALGEBRA-B6-RULE-RECOLLEMENT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-disjoint-implies-product}
Let $R$ be a ring.
If $\Spec(R) = U \amalg V$ with both $U$ and $V$ open
then $R \cong R_1 \times R_2$ with $U \cong \Spec(R_1)$
and $V \cong \Spec(R_2)$ via the maps in Lemma \ref{lemma-spec-product}.
Moreover, both $R_1$ and $R_2$ are localizations as well as quotients
of the ring $R$.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-disjoint-decomposition} we have
$U = D(e)$ and $V = D(1-e)$ for some idempotent $e$.
By Lemma \ref{lemma-standard-covering} we see that
$R \cong R_e \times R_{1 - e}$ (since clearly $R_{e(1-e)} = 0$
so the glueing condition is trivial; of course it is
trivial to prove the product decomposition directly in this
case). The lemma follows.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-disjoint-implies-product}
Soit $R$ un anneau.
Si $\Spec(R) = U \amalg V$, où $U$ et $V$ sont tous deux ouverts,
alors $R \cong R_1 \times R_2$, avec $U \cong \Spec(R_1)$
et $V \cong \Spec(R_2)$ via les morphismes du lemme \ref{lemma-spec-product}.
De plus, $R_1$ et $R_2$ sont tous deux des localisations ainsi que des quotients
de l'anneau $R$.
\end{lemma}

\begin{proof}
D'après le lemme \ref{lemma-disjoint-decomposition}, nous avons
$U = D(e)$ et $V = D(1-e)$ pour un certain idempotent $e$.
D'après le lemme \ref{lemma-standard-covering}, nous voyons que
$R \cong R_e \times R_{1 - e}$ (puisque, manifestement, $R_{e(1-e)} = 0$,
de sorte que la condition de recollement est triviale ; bien entendu, il est
également immédiat de démontrer directement la décomposition en produit dans ce
cas). Le lemme en résulte.
\end{proof}
```

</details>

### 18 — lemma-when-injective-covering

Anglais L4404–4437 ; français L4384–4417.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4404) · FR-ALGEBRA-B6-CHOICE-0018.

Aucune hypothèse disant que les f_i engendrent l'idéal unité n'apparaît dans ce lemme et aucune n'est ajoutée. Le critère est une injectivité dans les deux sens, pas une surjectivité. Les exposants sont au moins 1 ; la récurrence porte sur leur somme, et le passage m'=f_i m conserve la distinction entre diminuer l'exposant pour appliquer la récurrence et le ramener ensuite à 1. « Achève la récurrence » traduit idiomatiquement « we win » sans supprimer cette dernière étape. La transition vers la descente plate est conservée.

Règles : FR-ALGEBRA-B6-RULE-MORPHISMES, FR-ALGEBRA-B6-RULE-RECOLLEMENT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-when-injective-covering}
Let $R$ be a ring.
Let $f_1, \ldots, f_n \in R$.
Let $M$ be an $R$-module.
Then $M \to \bigoplus M_{f_i}$ is injective if and only if
$$
M \longrightarrow \bigoplus\nolimits_{i = 1, \ldots, n} M, \quad
m \longmapsto (f_1m, \ldots, f_nm)
$$
is injective.
\end{lemma}

\begin{proof}
The map $M \to \bigoplus M_{f_i}$ is injective if and only if
for all $m \in M$ and $e_1, \ldots, e_n \geq 1$ such that
$f_i^{e_i}m = 0$, $i = 1, \ldots, n$ we have $m = 0$.
This clearly implies the displayed map is injective.
Conversely, suppose the displayed map is injective and
$m \in M$ and $e_1, \ldots, e_n \geq 1$ are such that
$f_i^{e_i}m = 0$, $i = 1, \ldots, n$. If $e_i = 1$ for all $i$,
then we immediately conclude that $m = 0$ from the injectivity of
the displayed map. Next, we prove this holds for any such data
by induction on $e = \sum e_i$. The base case is $e = n$, and we have
just dealt with this. If some $e_i > 1$, then set $m' = f_im$.
By induction we see that $m' = 0$. Hence we see that $f_i m = 0$,
i.e., we may take $e_i = 1$ which decreases $e$ and we win.
\end{proof}

\noindent
The following lemma is better stated and proved in the more general
context of flat descent. However, it makes sense to state it here
since it fits well with the above.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-when-injective-covering}
Soit $R$ un anneau.
Soient $f_1, \ldots, f_n \in R$.
Soit $M$ un $R$-module.
Alors $M \to \bigoplus M_{f_i}$ est injectif si et seulement si
$$
M \longrightarrow \bigoplus\nolimits_{i = 1, \ldots, n} M, \quad
m \longmapsto (f_1m, \ldots, f_nm)
$$
est injectif.
\end{lemma}

\begin{proof}
Le morphisme $M \to \bigoplus M_{f_i}$ est injectif si et seulement si,
pour tous $m \in M$ et $e_1, \ldots, e_n \geq 1$ tels que
$f_i^{e_i}m = 0$, $i = 1, \ldots, n$, nous avons $m = 0$.
Cela entraîne manifestement que le morphisme affiché est injectif.
Réciproquement, supposons le morphisme affiché injectif et que
$m \in M$ et $e_1, \ldots, e_n \geq 1$ soient tels que
$f_i^{e_i}m = 0$, $i = 1, \ldots, n$. Si $e_i = 1$ pour tout $i$,
alors l'injectivité du morphisme affiché donne immédiatement $m = 0$.
Démontrons ensuite que cela vaut pour toutes données de ce type
par récurrence sur $e = \sum e_i$. Le cas initial est $e = n$, et nous venons
de le traiter. Si un certain $e_i > 1$, posons $m' = f_im$.
Par récurrence, nous voyons que $m' = 0$. Ainsi $f_i m = 0$,
c'est-à-dire que nous pouvons prendre $e_i = 1$, ce qui diminue $e$ et achève la récurrence.
\end{proof}

\noindent
Le lemme suivant s'énonce et se démontre mieux dans le cadre plus général
de la descente plate. Il est néanmoins naturel de l'énoncer ici,
car il s'accorde bien avec ce qui précède.
```

</details>

### 19 — lemma-glue-modules

Anglais L4438–4535 ; français L4418–4515.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L4438) · FR-ALGEBRA-B6-CHOICE-0019.

Les données sont les modules M_i et les isomorphismes psi_ij satisfaisant la condition de cocycle sur les triples intersections. « Condition de cocycle » et « donnée de descente » sont attestés chez Dat §1.7, pp.27–28. Dans le noyau, c'est psi_ji qui intervient, tandis que la compatibilité finale utilise psi_ij : ces sens ne sont pas uniformisés. Contrairement au cas de Dat, la source n'impose pas ici un recouvrement de Spec(R) par les D(f_i) ; le français n'en invente pas. La preuve et le diagramme complets sont conservés, avec réduction locale à f_1=1, puis identifications canoniques.

Point particulier à relire : La tournure « Supposons données les données suivantes » est répétitive mais intelligible et fidèle ; elle n'est pas transformée artificiellement en faute mathématique. La référence de Dat a une hypothèse de recouvrement supplémentaire et une conclusion d'unicité ; elles ne sont pas ajoutées dans Stacks.

Règles : FR-ALGEBRA-B6-RULE-LOCALISATION, FR-ALGEBRA-B6-RULE-MORPHISMES, FR-ALGEBRA-B6-RULE-EXACTITUDE, FR-ALGEBRA-B6-RULE-RECOLLEMENT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-glue-modules}
Let $R$ be a ring. Let $f_1, \ldots, f_n \in R$. Suppose we are given
the following data:
\begin{enumerate}
\item For each $i$ an $R_{f_i}$-module $M_i$.
\item For each pair $i, j$ an $R_{f_if_j}$-module isomorphism
$\psi_{ij} : (M_i)_{f_j} \to (M_j)_{f_i}$.
\end{enumerate}
which satisfy the ``cocycle condition'' that all the diagrams
$$
\xymatrix{
(M_i)_{f_jf_k}
\ar[rd]_{\psi_{ij}}
\ar[rr]^{\psi_{ik}}
& &
(M_k)_{f_if_j} \\
&
(M_j)_{f_if_k} \ar[ru]_{\psi_{jk}}
}
$$
commute (for all triples $i, j, k$). Given this data define
$$
M = \Ker\left(
\bigoplus\nolimits_{1 \leq i \leq n} M_i
\longrightarrow
\bigoplus\nolimits_{1 \leq i, j \leq n} (M_i)_{f_j}
\right)
$$
where $(m_1, \ldots, m_n)$ maps to the element whose
$(i, j)$th entry is $m_i/1 - \psi_{ji}(m_j/1)$.
Then the natural map $M \to M_i$ induces an isomorphism
$M_{f_i} \to M_i$. Moreover $\psi_{ij}(m/1) = m/1$
for all $m \in M$ (with obvious notation).
\end{lemma}

\begin{proof}
To show that $M_{f_1} \to M_1$ is an isomorphism, it suffices
to show that its localization at every prime $\mathfrak p'$
of $R_{f_1}$ is an isomorphism, see
Lemma \ref{lemma-characterize-zero-local}.
Write $\mathfrak p' = \mathfrak p R_{f_1}$
for some prime $\mathfrak p \subset R$, $f_1 \not \in \mathfrak p$, see
Lemma \ref{lemma-standard-open}.
Since localization is exact
(Proposition \ref{proposition-localization-exact}),
we see that
\begin{align*}
(M_{f_1})_{\mathfrak p'} & =
M_\mathfrak p \\
& =
\Ker\left(
\bigoplus\nolimits_{1 \leq i \leq n} M_{i, \mathfrak p}
\longrightarrow
\bigoplus\nolimits_{1 \leq i, j \leq n} ((M_i)_{f_j})_\mathfrak p
\right) \\
& =
\Ker\left(
\bigoplus\nolimits_{1 \leq i \leq n} M_{i, \mathfrak p}
\longrightarrow
\bigoplus\nolimits_{1 \leq i, j \leq n} (M_{i, \mathfrak p})_{f_j}
\right)
\end{align*}
Here we also used Proposition \ref{proposition-localize-twice-module}.
Since $f_1$ is a unit in $R_\mathfrak p$, this reduces us to the case
where $f_1 = 1$ by replacing $R$ by $R_\mathfrak p$, $f_i$ by the
image of $f_i$ in $R_\mathfrak p$, $M$ by $M_\mathfrak p$, and
$f_1$ by $1$.

\medskip\noindent
Assume $f_1 = 1$. Then $\psi_{1j} : (M_1)_{f_j} \to M_j$
is an isomorphism for $j = 2, \ldots, n$. If we use these
isomorphisms to identify $M_j = (M_1)_{f_j}$, then we see
that $\psi_{ij} : (M_1)_{f_if_j} \to (M_1)_{f_if_j}$ is
the canonical identification. Thus the complex
$$
0 \to M_1 \to
\bigoplus\nolimits_{1 \leq i \leq n} (M_1)_{f_i}
\longrightarrow
\bigoplus\nolimits_{1 \leq i, j \leq n}
(M_1)_{f_if_j}
$$
is exact by Lemma \ref{lemma-cover-module}.
Thus the first map identifies $M_1$ with $M$ in this case
and everything is clear.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-glue-modules}
Soit $R$ un anneau. Soient $f_1, \ldots, f_n \in R$. Supposons données
les données suivantes :
\begin{enumerate}
\item Pour chaque $i$, un $R_{f_i}$-module $M_i$.
\item Pour chaque paire $i, j$, un isomorphisme de $R_{f_if_j}$-modules
$\psi_{ij} : (M_i)_{f_j} \to (M_j)_{f_i}$.
\end{enumerate}
qui satisfont la « condition de cocycle » selon laquelle tous les diagrammes
$$
\xymatrix{
(M_i)_{f_jf_k}
\ar[rd]_{\psi_{ij}}
\ar[rr]^{\psi_{ik}}
& &
(M_k)_{f_if_j} \\
&
(M_j)_{f_if_k} \ar[ru]_{\psi_{jk}}
}
$$
sont commutatifs (pour tous les triplets $i, j, k$). À partir de ces données, définissons
$$
M = \Ker\left(
\bigoplus\nolimits_{1 \leq i \leq n} M_i
\longrightarrow
\bigoplus\nolimits_{1 \leq i, j \leq n} (M_i)_{f_j}
\right)
$$
où $(m_1, \ldots, m_n)$ est envoyé sur l'élément dont
la composante d'indice $(i, j)$ est $m_i/1 - \psi_{ji}(m_j/1)$.
Alors le morphisme naturel $M \to M_i$ induit un isomorphisme
$M_{f_i} \to M_i$. De plus, $\psi_{ij}(m/1) = m/1$
pour tout $m \in M$ (avec les notations évidentes).
\end{lemma}

\begin{proof}
Pour montrer que $M_{f_1} \to M_1$ est un isomorphisme, il suffit
de montrer que sa localisation en tout idéal premier $\mathfrak p'$
de $R_{f_1}$ est un isomorphisme ; voir le
lemme \ref{lemma-characterize-zero-local}.
Écrivons $\mathfrak p' = \mathfrak p R_{f_1}$
pour un certain idéal premier $\mathfrak p \subset R$, avec $f_1 \not \in \mathfrak p$ ; voir le
lemme \ref{lemma-standard-open}.
Puisque la localisation est exacte
(proposition \ref{proposition-localization-exact}),
nous voyons que
\begin{align*}
(M_{f_1})_{\mathfrak p'} & =
M_\mathfrak p \\
& =
\Ker\left(
\bigoplus\nolimits_{1 \leq i \leq n} M_{i, \mathfrak p}
\longrightarrow
\bigoplus\nolimits_{1 \leq i, j \leq n} ((M_i)_{f_j})_\mathfrak p
\right) \\
& =
\Ker\left(
\bigoplus\nolimits_{1 \leq i \leq n} M_{i, \mathfrak p}
\longrightarrow
\bigoplus\nolimits_{1 \leq i, j \leq n} (M_{i, \mathfrak p})_{f_j}
\right)
\end{align*}
Nous avons également utilisé ici la proposition \ref{proposition-localize-twice-module}.
Puisque $f_1$ est une unité de $R_\mathfrak p$, nous nous ramenons au cas
où $f_1 = 1$ en remplaçant $R$ par $R_\mathfrak p$, les $f_i$ par les
images des $f_i$ dans $R_\mathfrak p$, $M$ par $M_\mathfrak p$ et
$f_1$ par $1$.

\medskip\noindent
Supposons $f_1 = 1$. Alors $\psi_{1j} : (M_1)_{f_j} \to M_j$
est un isomorphisme pour $j = 2, \ldots, n$. Si nous utilisons ces
isomorphismes pour identifier $M_j = (M_1)_{f_j}$, nous voyons alors
que $\psi_{ij} : (M_1)_{f_if_j} \to (M_1)_{f_if_j}$ est
l'identification canonique. Ainsi, le complexe
$$
0 \to M_1 \to
\bigoplus\nolimits_{1 \leq i \leq n} (M_1)_{f_i}
\longrightarrow
\bigoplus\nolimits_{1 \leq i, j \leq n}
(M_1)_{f_if_j}
$$
est exact d'après le lemme \ref{lemma-cover-module}.
Ainsi, le premier morphisme identifie $M_1$ à $M$ dans ce cas,
et tout est clair.
\end{proof}
```

</details>

## Contrôles exacts

Les 547 régions mathématiques concordent après trois exceptions exactes portant seulement sur six mots de liaison dans les affichages. Aucune suppression générique de texte mathématique n’est utilisée. Le préfixe de 3 238 régions passe avec ces trois exceptions et les huit déjà documentées aux lots 2–3. La comparaison brute sans exceptions est explicitement fausse.

Labels, références, commandes invariantes, environnements, contrôles TeX et items concordent. Le fichier cible ne diffère du précédent que par la précision retirée ; ses régions mathématiques sont inchangées. Le retour inverse recouvre exactement le précédent puis le témoin français publié. Les 150 paires couvrent tout le préfixe sans lacune ni chevauchement.

Prochaine lecture : Diviseurs de zéro et anneaux totaux des fractions, anglais L4536 / français L4516. Aucun nouveau PDF, aucune publication et aucune certification de l’ensemble du chapitre ou de l’édition ne sont revendiqués.

