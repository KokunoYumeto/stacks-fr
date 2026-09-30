# Algèbre commutative : noethérianité, nilpotence et Nullstellensatz

## Résultat et portée

Quatre sections entièrement comparées : anglais L5980–6648 et français L5960–6628, soit 669 lignes de chaque témoin. Les 26 paires comprennent les preuves complètes, les exemples et les transitions. 195 occurrences sont reliées à des règles contextualisées. Le préfixe atteint 34 sections, 227 paires et 1724 occurrences. Le chapitre et l’édition restent inachevés.

Deux opérations seulement : retrait de la qualification naturel ajoutée à entier, pour fidélité diplomatique ; remplacement du calque isolé ouvert standard par ouvert principal, attesté dans le canon français. La première n’est pas la découverte d’un faux théorème ; la seconde ne change pas la désignation de D(f). Aucune formule, hypothèse symbolique ni référence ne change.

Trois observations séparées expliquent une convention de coefficient nul, une ambiguïté conditionnelle d’indice zéro et un raisonnement canonique condensé. Ce ne sont pas trois nouveaux théorèmes faux ni trois admissions d’errata.

Comparaison assistée par IA, sans relecture humaine. Le canon est consulté rétrospectivement pour cette décision ; aucune consultation antérieure n’est inventée. Les expressions non attestées dans les pages effectivement lues sont explicitement signalées, sans bloquer une décision provisoire motivée.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch9.fr.tex) · [État français précédent](staged/fr/010_algebra.prose-batch8.fr.tex) · [Lot précédent](ALGEBRA_PROSE_BATCH8_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH9_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH9_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH9_OCCURRENCES.json) · [Avant/après](ALGEBRA_PROSE_BATCH9_REPAIRS.json) · [Exceptions de texte dans les formules](ALGEBRA_PROSE_BATCH9_MATH_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH9_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH9_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Antoine Ducros — Cours de théorie des schémas

[Source universitaire](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [PDF conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages PDF/imprimées 25–26 et 135–136 lues intégralement : 0.1.8.2, 0.2.5–0.2.5.1, 2.10.5–2.10.9. Page 136 également rendue et inspectée.

Attestations courtes : « anneau noethérien », « de présentation finie », « théorème des zéros de Hilbert », « une extension finie de k ».

Appui au registre des anneaux et modules noethériens, à la distinction type fini/présentation finie et aux formulations du Nullstellensatz sur un corps quelconque.

Limites : La démonstration de Ducros n'est pas substituée à celle de Stacks. Aucune attestation exhaustive de réduction noethérienne absolue, localement nilpotent ou de toutes les tournures du lot n'est revendiquée. La page 135 comporte une plage d'indices Ym+1,…,Ym manifestement tronquée ; la page 136 alterne T et X. Ces détails ne sont pas importés.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

### Jean-François Dat — Théorie des schémas

[Source universitaire](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/Schemas/Schemas.pdf) · [PDF conservé](canon-consulted/fr-algebra/dat-schemas.pdf)

Pages PDF/imprimées 7–8 lues intégralement : définitions topologiques, composantes irréductibles, 1.2.4 et 1.2.5. Page 8 rendue et inspectée, notamment les barres d’adhérence perdues dans l’extraction.

Attestations courtes : « Ouverts principaux », « espace topologique noethérien », « partie multiplicative ».

D(f) est explicitement appelé ouvert principal : attestation directe pour la réparation du calque standard. Appui à composante irréductible, idéal premier minimal et localisation.

Limites : L'exemple p.7 présente la même écriture Xn^n avec n dans N : cette récurrence d'usage ne tranche pas la convention de zéro. La phrase tout ouvert dense omet manifestement non vide ; elle n'est pas utilisée comme autorité mathématique. L'image adhérente p.8 doit être lue sur le rendu, non sur l'extraction seule.

SHA-256 : 9298B062AC2BDF64161A107980A30F98E1F2DF6DEB4DA98E1FEB21BA494D26A1.

## Les deux opérations exactes

### FR-ALGEBRA-B9-REPAIR-0001

Anglais L6038 ; français L6018.

Avant :
```tex
Pour tout entier naturel
```

Après :
```tex
Pour tout entier
```

La précision naturel était mathématiquement motivée mais explicite seulement dans le français. Son retrait est une restauration diplomatique minime, pas une correction du théorème. Réduction noethérienne absolue reste une proposition lexicale sans attestation indépendante acquise.

### FR-ALGEBRA-B9-REPAIR-0002

Anglais L6579 ; français L6559.

Avant :
```tex
un ouvert
standard $D(f)$
```

Après :
```tex
un ouvert
principal $D(f)$
```

Ouvert principal est une réparation terminologique attestée, non une nouvelle correction mathématique. Les deux expressions anglaise et française désignent exactement D(f).

## Règles contextualisées

### FR-ALGEBRA-B9-RULE-NOETHERIEN

Noethérien garde sa définition algébrique ou topologique selon l'objet de la paire ; aucune équivalence inverse anneau/spectre n'est introduite.

Canon : FR-ALGEBRA-B9-CANON-DUCROS, FR-ALGEBRA-B9-CANON-DAT.

### FR-ALGEBRA-B9-RULE-FINITE

Distinguer génération finie comme module, algèbre ou corps et degré fini. La paire complète détermine le sens, non le mot isolé.

Canon : FR-ALGEBRA-B9-CANON-DUCROS.

### FR-ALGEBRA-B9-RULE-SPECTRE

Les composantes du spectre correspondent aux premiers minimaux ; générique se rapporte à la composante dans le slogan.

Canon : FR-ALGEBRA-B9-CANON-DAT.

### FR-ALGEBRA-B9-RULE-PRINCIPAL

D(f) est un ouvert principal. Standard est un calque compréhensible mais incohérent avec l'usage attesté et le reste du chapitre ; une occurrence est normalisée.

Canon : FR-ALGEBRA-B9-CANON-DAT.

### FR-ALGEBRA-B9-RULE-LOCALISATION

La localisation inverse la partie multiplicative ; son image spectrale n'est pas nécessairement ouverte. Les hypothèses supplémentaires sont vérifiées dans chaque paire.

Canon : FR-ALGEBRA-B9-CANON-DAT.

### FR-ALGEBRA-B9-RULE-NILPOTENCE

Choix gouverné par la définition source : exposant dépendant de l'élément versus exposant uniforme de l'idéal. Attestation française externe du syntagme localement nilpotent non acquise ici.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B9-RULE-LIFT

Choix compositionnel appuyé par les constructions source e↦ē et e²=e ; pas de revendication d'attestation indépendante dans les pages lues. Existence et unicité sont comparées séparément.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B9-RULE-UNIT

Unité signifie élément multiplicativement inversible ; non nul ne suffit pas. Choix confirmé directement par les équations du passage, sans attestation externe nouvelle.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B9-RULE-SERIES

Série formelle et ordre supérieur sont déterminés par les puissances de x ; aucune convergence analytique n'est impliquée. Le nom de la technique finale reste provisoire faute d'attestation française consultée.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B9-RULE-NULLSTELLENSATZ

Le nom allemand est attesté en français, avec théorème des zéros de Hilbert comme alternative. Maintien du nom existant sans uniformisation superflue.

Canon : FR-ALGEBRA-B9-CANON-DUCROS.

### FR-ALGEBRA-B9-RULE-LOGIQUE

Portée et dépendance des quantificateurs, sens des implications et hypothèse de récurrence vérifiés par comparaison des arguments complets ; ce contrôle n'est pas une attestation lexicale externe.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-Noetherian

Anglais L5980–5989 ; français L5960–5969.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5980) · FR-ALGEBRA-B9-CHOICE-0001.

Noethérien qualifie l'anneau par la génération finie de ses idéaux, non par sa cardinalité. La condition de chaîne ascendante et la réduction aux idéaux premiers par le lemme de Cohen sont conservées. Ducros 0.1.8.2 atteste le registre noethérien dans ce cadre.

Règles : FR-ALGEBRA-B9-RULE-NOETHERIEN, FR-ALGEBRA-B9-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Noetherian rings}
\label{section-Noetherian}

\noindent
A ring $R$ is {\it Noetherian} if any ideal of $R$ is finitely generated.
This is clearly equivalent to the ascending chain condition for ideals of $R$.
By
Lemma \ref{lemma-cohen}
it suffices to check that every prime ideal of $R$ is finitely generated.
```

Français restauré :
```tex
\section{Anneaux noethériens}
\label{section-Noetherian}

\noindent
Un anneau $R$ est {\it noethérien} si tout idéal de $R$ est de type fini.
Cela équivaut clairement à la condition de chaîne ascendante pour les idéaux de $R$.
D'après le
lemme \ref{lemma-cohen},
il suffit de vérifier que tout idéal premier de $R$ est de type fini.
```

</details>

### 02 — lemma-Noetherian-permanence

Anglais L5990–6026 ; français L5970–6006.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L5990) · FR-ALGEBRA-B9-CHOICE-0002.

Le slogan, les localisations, les quotients et l'extension polynomiale sont tous conservés. Anneau de type fini traduit finitely generated ring over sans le confondre avec un module fini. Dans la preuve, la monotonie porte sur les deux indices ; la suite croissante dans N×N permet la stabilisation uniforme, puis la soustraction de deux polynômes de même coefficient dominant abaisse le degré. Le résultat s'ensuit restitue we win sans ajout d'argument. La convention sur le coefficient nul est signalée à part.

Point particulier à relire : La description des coefficients dominants requiert la convention incluant zéro ; conserver la formulation officielle et voir l'observation séparée.

Règles : FR-ALGEBRA-B9-RULE-NOETHERIEN, FR-ALGEBRA-B9-RULE-FINITE, FR-ALGEBRA-B9-RULE-LOCALISATION, FR-ALGEBRA-B9-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Noetherian-permanence}
\begin{slogan}
Noetherian property is stable by passage to finite type extension
and localization.
\end{slogan}
Any finitely generated ring over a Noetherian ring
is Noetherian. Any localization of a Noetherian ring
is Noetherian.
\end{lemma}

\begin{proof}
The statement on localizations follows from the fact
that any ideal $J \subset S^{-1}R$ is of the form
$I \cdot S^{-1}R$. Any quotient $R/I$ of a Noetherian
ring $R$ is Noetherian because any ideal $\overline{J} \subset R/I$
is of the form $J/I$ for some ideal $I \subset J \subset R$.
Thus it suffices to show that if $R$ is Noetherian so
is $R[X]$. Suppose $J_1 \subset J_2 \subset \ldots$ is an
ascending chain of ideals in $R[X]$. Consider the ideals $I_{i, d}$
defined as the ideal of elements of $R$ which occur as leading
coefficients of degree $d$ polynomials in $J_i$.
Clearly $I_{i, d} \subset I_{i', d'}$ whenever
$i \leq i'$ and $d \leq d'$. By the ascending chain condition
in $R$ there are at most finitely many distinct ideals among all of
the $I_{i, d}$.
(Hint: Any infinite set of elements of
$\mathbf{N} \times \mathbf{N}$ contains an increasing
infinite sequence.)
Take $i_0$ so large that $I_{i, d} = I_{i_0, d}$
for all $i \geq i_0$ and all $d$. Suppose $f \in J_i$ for some $i \geq i_0$.
By induction on the degree $d = \deg(f)$ we show that $f \in J_{i_0}$.
Namely, there exists a $g\in J_{i_0}$ whose degree is $d$ and which
has the same leading coefficient as $f$. By induction
$f - g \in J_{i_0}$ and we win.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-Noetherian-permanence}
\begin{slogan}
La propriété noethérienne est stable par extension de type fini
et par localisation.
\end{slogan}
Tout anneau de type fini sur un anneau noethérien
est noethérien. Toute localisation d'un anneau noethérien
est noethérienne.
\end{lemma}

\begin{proof}
L'assertion sur les localisations résulte du fait
que tout idéal $J \subset S^{-1}R$ est de la forme
$I \cdot S^{-1}R$. Tout quotient $R/I$ d'un anneau noethérien
$R$ est noethérien, car tout idéal $\overline{J} \subset R/I$
est de la forme $J/I$ pour un certain idéal $I \subset J \subset R$.
Il suffit donc de montrer que, si $R$ est noethérien, alors
$R[X]$ l'est aussi. Supposons que $J_1 \subset J_2 \subset \ldots$ soit une
chaîne ascendante d'idéaux de $R[X]$. Considérons les idéaux $I_{i, d}$
définis comme les idéaux constitués des éléments de $R$ qui apparaissent comme coefficients
dominants de polynômes de degré $d$ appartenant à $J_i$.
Il est clair que $I_{i, d} \subset I_{i', d'}$ dès que
$i \leq i'$ et $d \leq d'$. Par la condition de chaîne ascendante
dans $R$, il n'y a qu'un nombre fini d'idéaux distincts parmi tous les
$I_{i, d}$.
(Indication : tout ensemble infini d'éléments de
$\mathbf{N} \times \mathbf{N}$ contient une suite infinie
croissante.)
Prenons $i_0$ assez grand pour que $I_{i, d} = I_{i_0, d}$
pour tous $i \geq i_0$ et tout $d$. Supposons que $f \in J_i$ pour un certain $i \geq i_0$.
Par récurrence sur le degré $d = \deg(f)$, montrons que $f \in J_{i_0}$.
En effet, il existe un $g\in J_{i_0}$ de degré $d$ ayant
le même coefficient dominant que $f$. Par récurrence,
$f - g \in J_{i_0}$, et le résultat s'ensuit.
\end{proof}
```

</details>

### 03 — lemma-Noetherian-power-series

Anglais L6027–6073 ; français L6007–6053.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6027) · FR-ALGEBRA-B9-CHOICE-0003.

Séries formelles ne devient pas séries convergentes : les coefficients sont construits par ordre croissant, sans norme analytique. Les deux écritures h.o.t. sont traduites explicitement par termes d'ordre supérieur, sans changement de symboles. Entier remplace entier naturel pour retrouver exactement l'absence de qualification dans la prose anglaise ; la non-négativité implicitement utilisée reste expliquée ici. Ce n'est pas la découverte d'un faux théorème. Réduction noethérienne absolue est une traduction compositionnelle motivée du nom anglais ; aucune attestation française indépendante de cette expression n'a été acquise dans les pages consultées.

Point particulier à relire : La précision naturel était mathématiquement motivée mais explicite seulement dans le français. Son retrait est une restauration diplomatique minime, pas une correction du théorème. Réduction noethérienne absolue reste une proposition lexicale sans attestation indépendante acquise.

Règles : FR-ALGEBRA-B9-RULE-NOETHERIEN, FR-ALGEBRA-B9-RULE-FINITE, FR-ALGEBRA-B9-RULE-SERIES, FR-ALGEBRA-B9-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Noetherian-power-series}
If $R$ is a Noetherian ring, then so is the formal power
series ring $R[[x_1, \ldots, x_n]]$.
\end{lemma}

\begin{proof}
Since $R[[x_1, \ldots, x_{n + 1}]] \cong R[[x_1, \ldots, x_n]][[x_{n + 1}]]$
it suffices to prove the statement that $R[[x]]$ is Noetherian if
$R$ is Noetherian. Let $I \subset R[[x]]$ be an ideal.
We have to show that $I$ is a finitely generated ideal.
For each integer
$d$ denote $I_d = \{a \in R \mid ax^d + \text{h.o.t.} \in I\}$.
Then we see that $I_0 \subset I_1 \subset \ldots$ stabilizes as $R$
is Noetherian. Choose $d_0$ such that $I_{d_0} = I_{d_0 + 1} = \ldots$.
For each $d \leq d_0$ choose elements $f_{d, j} \in I \cap (x^d)$,
$j = 1, \ldots, n_d$ such that if we write
$f_{d, j} = a_{d, j}x^d + \text{h.o.t}$ then $I_d = (a_{d, j})$.
Denote $I' = (\{f_{d, j}\}_{d = 0, \ldots, d_0, j = 1, \ldots, n_d})$.
Then it is clear that $I' \subset I$. Pick $f \in I$.
First we may choose $c_{d, i} \in R$ such that
$$
f - \sum c_{d, i} f_{d, i} \in (x^{d_0 + 1}) \cap I.
$$
Next, we can choose $c_{i, 1} \in R$, $i = 1, \ldots, n_{d_0}$ such that
$$
f - \sum c_{d, i} f_{d, i} - \sum c_{i, 1}xf_{d_0, i} \in (x^{d_0 + 2}) \cap I.
$$
Next, we can choose $c_{i, 2} \in R$, $i = 1, \ldots, n_{d_0}$ such that
$$
f - \sum c_{d, i} f_{d, i} - \sum c_{i, 1}xf_{d_0, i}
- \sum c_{i, 2}x^2f_{d_0, i}
\in (x^{d_0 + 3}) \cap I.
$$
And so on. In the end we see that
$$
f = \sum c_{d, i} f_{d, i} +
\sum\nolimits_i (\sum\nolimits_e c_{i, e} x^e)f_{d_0, i}
$$
is contained in $I'$ as desired.
\end{proof}

\noindent
The following lemma, although easy, is useful because
finite type $\mathbf{Z}$-algebras come up quite often in
a technique called ``absolute Noetherian reduction''.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-Noetherian-power-series}
Si $R$ est un anneau noethérien, alors l'anneau de séries
formelles $R[[x_1, \ldots, x_n]]$ l'est également.
\end{lemma}

\begin{proof}
Puisque $R[[x_1, \ldots, x_{n + 1}]] \cong R[[x_1, \ldots, x_n]][[x_{n + 1}]]$,
il suffit de montrer que $R[[x]]$ est noethérien lorsque
$R$ l'est. Soit $I \subset R[[x]]$ un idéal.
Nous devons montrer que $I$ est un idéal de type fini.
Pour tout entier
$d$, notons $I_d = \{a \in R \mid ax^d + \text{termes d'ordre supérieur} \in I\}$.
Alors nous voyons que $I_0 \subset I_1 \subset \ldots$ se stabilise, puisque $R$
est noethérien. Choisissons $d_0$ tel que $I_{d_0} = I_{d_0 + 1} = \ldots$.
Pour tout $d \leq d_0$, choisissons des éléments $f_{d, j} \in I \cap (x^d)$,
$j = 1, \ldots, n_d$, tels que, si nous écrivons
$f_{d, j} = a_{d, j}x^d + \text{termes d'ordre supérieur}$, alors $I_d = (a_{d, j})$.
Notons $I' = (\{f_{d, j}\}_{d = 0, \ldots, d_0, j = 1, \ldots, n_d})$.
Il est alors clair que $I' \subset I$. Choisissons $f \in I$.
Nous pouvons d'abord choisir des $c_{d, i} \in R$ tels que
$$
f - \sum c_{d, i} f_{d, i} \in (x^{d_0 + 1}) \cap I.
$$
Ensuite, nous pouvons choisir $c_{i, 1} \in R$, $i = 1, \ldots, n_{d_0}$, tels que
$$
f - \sum c_{d, i} f_{d, i} - \sum c_{i, 1}xf_{d_0, i} \in (x^{d_0 + 2}) \cap I.
$$
Ensuite, nous pouvons choisir $c_{i, 2} \in R$, $i = 1, \ldots, n_{d_0}$, tels que
$$
f - \sum c_{d, i} f_{d, i} - \sum c_{i, 1}xf_{d_0, i}
- \sum c_{i, 2}x^2f_{d_0, i}
\in (x^{d_0 + 3}) \cap I.
$$
Et ainsi de suite. Finalement, nous voyons que
$$
f = \sum c_{d, i} f_{d, i} +
\sum\nolimits_i (\sum\nolimits_e c_{i, e} x^e)f_{d_0, i}
$$
appartient à $I'$, comme voulu.
\end{proof}

\noindent
Le lemme suivant, quoique facile, est utile, car les
$\mathbf{Z}$-algèbres de type fini apparaissent assez souvent dans
une technique appelée « réduction noethérienne absolue ».
```

</details>

### 04 — lemma-obvious-Noetherian

Anglais L6074–6086 ; français L6054–6066.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6074) · FR-ALGEBRA-B9-CHOICE-0004.

Les deux bases, un corps et Z, restent distinctes. Anneau principal traduit principal ideal domain ici pour Z, qui est intègre ; on n'introduit pas cette convention dans un anneau arbitraire. Ducros 0.1.8.2 donne précisément ces deux conséquences. L'article manquant dans l'anglais est rendu normalement en français.

Règles : FR-ALGEBRA-B9-RULE-NOETHERIEN, FR-ALGEBRA-B9-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-obvious-Noetherian}
Any finite type algebra over a field is Noetherian.
Any finite type algebra over $\mathbf{Z}$ is Noetherian.
\end{lemma}

\begin{proof}
This is immediate from Lemma \ref{lemma-Noetherian-permanence}
and the fact that fields are Noetherian rings and that
$\mathbf{Z}$ is Noetherian ring (because it is a
principal ideal domain).
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-obvious-Noetherian}
Toute algèbre de type fini sur un corps est noethérienne.
Toute algèbre de type fini sur $\mathbf{Z}$ est noethérienne.
\end{lemma}

\begin{proof}
Cela résulte immédiatement du lemme \ref{lemma-Noetherian-permanence}
et du fait que les corps sont des anneaux noethériens et que
$\mathbf{Z}$ est un anneau noethérien (car c'est un
anneau principal).
\end{proof}
```

</details>

### 05 — lemma-Noetherian-finite-type-is-finite-presentation

Anglais L6087–6118 ; français L6067–6098.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6087) · FR-ALGEBRA-B9-CHOICE-0005.

Les trois assertions distinguent module de type fini, sous-module et algèbre de type fini. Fini ne veut pas dire ensemble fini. Ducros 0.2.5–0.2.5.1 atteste type fini et présentation finie, ainsi que leur relation sur un anneau noethérien. La preuve garde la filtration à quotients R/I, l'extension et l'usage exact de la partie (5) pour le noyau.

Règles : FR-ALGEBRA-B9-RULE-NOETHERIEN, FR-ALGEBRA-B9-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Noetherian-finite-type-is-finite-presentation}
Let $R$ be a Noetherian ring.
\begin{enumerate}
\item Any finite $R$-module is of finite presentation.
\item Any submodule of a finite $R$-module is finite.
\item Any finite type $R$-algebra is of finite presentation over $R$.
\end{enumerate}
\end{lemma}

\begin{proof}
Let $M$ be a finite $R$-module. By
Lemma \ref{lemma-trivial-filter-finite-module}
we can find a finite filtration of $M$ whose successive quotients are
of the form $R/I$. Since any ideal is finitely generated, each of
the quotients $R/I$ is finitely presented. Hence $M$ is finitely
presented by
Lemma \ref{lemma-extension}.
This proves (1).

\medskip\noindent
Let $N \subset M$ be a submodule. As $M$ is finite, the quotient
$M/N$ is finite. Thus $M/N$ is of finite presentation by part (1).
Thus we see that $N$ is finite by Lemma \ref{lemma-extension} part (5).
This proves part (2).

\medskip\noindent
To see (3) note that any ideal of
$R[x_1, \ldots, x_n]$ is finitely generated by
Lemma \ref{lemma-Noetherian-permanence}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-Noetherian-finite-type-is-finite-presentation}
Soit $R$ un anneau noethérien.
\begin{enumerate}
\item Tout $R$-module de type fini est de présentation finie.
\item Tout sous-module d'un $R$-module de type fini est de type fini.
\item Toute $R$-algèbre de type fini est de présentation finie sur $R$.
\end{enumerate}
\end{lemma}

\begin{proof}
Soit $M$ un $R$-module de type fini. D'après le
lemme \ref{lemma-trivial-filter-finite-module},
nous pouvons trouver une filtration finie de $M$ dont les quotients successifs sont
de la forme $R/I$. Puisque tout idéal est de type fini, chacun des
quotients $R/I$ est de présentation finie. Ainsi, $M$ est de présentation
finie d'après le
lemme \ref{lemma-extension}.
Cela démontre (1).

\medskip\noindent
Soit $N \subset M$ un sous-module. Puisque $M$ est de type fini, le quotient
$M/N$ est de type fini. Ainsi, $M/N$ est de présentation finie d'après la partie (1).
Nous voyons donc que $N$ est de type fini d'après le lemme \ref{lemma-extension}, partie (5).
Cela démontre la partie (2).

\medskip\noindent
Pour voir (3), notons que tout idéal de
$R[x_1, \ldots, x_n]$ est de type fini d'après le
lemme \ref{lemma-Noetherian-permanence}.
\end{proof}
```

</details>

### 06 — lemma-Noetherian-topology

Anglais L6119–6133 ; français L6099–6113.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6119) · FR-ALGEBRA-B9-CHOICE-0006.

Espace topologique noethérien est attesté chez Dat p.7. La correspondance entre idéaux radicaux et fermés renverse les inclusions ; c'est elle qui transforme la condition ascendante en condition descendante. Aucune réciproque anneau/spectre n'est ajoutée : Dat en souligne expressément la fausseté.

Règles : FR-ALGEBRA-B9-RULE-NOETHERIEN.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Noetherian-topology}
If $R$ is a Noetherian ring then $\Spec(R)$
is a Noetherian topological space, see Topology,
Definition \ref{topology-definition-noetherian}.
\end{lemma}

\begin{proof}
This is because any closed subset of $\Spec(R)$
is uniquely of the form $V(I)$ with $I$ a radical ideal,
see Lemma \ref{lemma-Zariski-topology}.
And this correspondence is inclusion reversing.
Thus the result follows from the definitions.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-Noetherian-topology}
Si $R$ est un anneau noethérien, alors $\Spec(R)$
est un espace topologique noethérien, voir Topologie,
définition \ref{topology-definition-noetherian}.
\end{lemma}

\begin{proof}
Cela vient du fait que tout fermé de $\Spec(R)$
s'écrit de manière unique sous la forme $V(I)$, où $I$ est un idéal radical,
voir le lemme \ref{lemma-Zariski-topology}.
Et cette correspondance renverse les inclusions.
Le résultat découle donc des définitions.
\end{proof}
```

</details>

### 07 — lemma-Noetherian-irreducible-components

Anglais L6134–6151 ; français L6114–6131.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6134) · FR-ALGEBRA-B9-CHOICE-0007.

Composantes irréductibles et idéaux premiers minimaux ont le même sens que chez Dat p.7. Points génériques, dans le slogan, désigne ceux des composantes, non tous les points considérés comme génériques de leur propre adhérence. Le slogan et la preuve sont traduits sans renforcer l'énoncé ni remplacer minimaux par maximaux.

Règles : FR-ALGEBRA-B9-RULE-NOETHERIEN, FR-ALGEBRA-B9-RULE-SPECTRE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Noetherian-irreducible-components}
\begin{slogan}
A Noetherian affine scheme has finitely many generic points.
\end{slogan}
If $R$ is a Noetherian ring then $\Spec(R)$
has finitely many irreducible components. In other words
$R$ has finitely many minimal primes.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-Noetherian-topology} and
Topology, Lemma \ref{topology-lemma-Noetherian}
we see there are finitely many irreducible components.
By Lemma \ref{lemma-irreducible} these correspond to
minimal primes of $R$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-Noetherian-irreducible-components}
\begin{slogan}
Un schéma affine noethérien possède un nombre fini de points génériques.
\end{slogan}
Si $R$ est un anneau noethérien, alors $\Spec(R)$
possède un nombre fini de composantes irréductibles. Autrement dit,
$R$ possède un nombre fini d'idéaux premiers minimaux.
\end{lemma}

\begin{proof}
D'après le lemme \ref{lemma-Noetherian-topology} et
Topologie, lemme \ref{topology-lemma-Noetherian},
nous voyons qu'il n'y a qu'un nombre fini de composantes irréductibles.
D'après le lemme \ref{lemma-irreducible}, celles-ci correspondent aux
idéaux premiers minimaux de $R$.
\end{proof}
```

</details>

### 08 — lemma-Noetherian-base-change-finite-type

Anglais L6152–6164 ; français L6132–6144.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6152) · FR-ALGEBRA-B9-CHOICE-0008.

Les quantificateurs et les deux morphismes sont conservés : R→R' est de type fini, S est noethérien. Il n'est pas supposé que R est noethérien. Le produit tensoriel est le changement de base et devient de type fini sur S ; la permanence s'applique à cette dernière base.

Règles : FR-ALGEBRA-B9-RULE-NOETHERIEN, FR-ALGEBRA-B9-RULE-FINITE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Noetherian-base-change-finite-type}
Let $R \to S$ be a ring map. Let $R \to R'$ be of finite type.
If $S$ is Noetherian, then the base change $S' = R' \otimes_R S$
is Noetherian.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-base-change-finiteness} finite type is stable under
base change. Thus $S \to S'$ is of finite type. Since $S$ is Noetherian we
can apply Lemma \ref{lemma-Noetherian-permanence}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-Noetherian-base-change-finite-type}
Soit $R \to S$ un morphisme d'anneaux. Supposons que $R \to R'$ soit de type fini.
Si $S$ est noethérien, alors le changement de base $S' = R' \otimes_R S$
est noethérien.
\end{lemma}

\begin{proof}
D'après le lemme \ref{lemma-base-change-finiteness}, le caractère de type fini est stable par
changement de base. Ainsi, $S \to S'$ est de type fini. Puisque $S$ est noethérien, nous
pouvons appliquer le lemme \ref{lemma-Noetherian-permanence}.
\end{proof}
```

</details>

### 09 — lemma-Noetherian-field-extension

Anglais L6165–6185 ; français L6145–6165.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6165) · FR-ALGEBRA-B9-CHOICE-0009.

Extension de corps de type fini signifie engendrée comme corps, pas nécessairement algébrique ni finie. La preuve choisit une sous-algèbre B de type fini puis inverse ses éléments non nuls. Le français garde ce détour ; remplacer type fini par finie affaiblirait le résultat. Le corps des fractions n'est pas assimilé à une algèbre de type fini avant localisation.

Point particulier à relire : Ne pas confondre génération finie comme corps, génération finie comme algèbre et degré fini.

Règles : FR-ALGEBRA-B9-RULE-NOETHERIEN, FR-ALGEBRA-B9-RULE-FINITE, FR-ALGEBRA-B9-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Noetherian-field-extension}
Let $k$ be a field and let $R$ be a Noetherian $k$-algebra.
If $K/k$ is a finitely generated field extension then
$K \otimes_k R$ is Noetherian.
\end{lemma}

\begin{proof}
Since $K/k$ is a finitely generated field extension, there exists
a finitely generated $k$-algebra $B \subset K$ such that $K$ is
the fraction field of $B$. In other words, $K = S^{-1}B$
with $S = B \setminus \{0\}$. Then $K \otimes_k R = S^{-1}(B \otimes_k R)$.
Then $B \otimes_k R$ is Noetherian by
Lemma \ref{lemma-Noetherian-base-change-finite-type}.
Finally, $K \otimes_k R = S^{-1}(B \otimes_k R)$ is Noetherian by
Lemma \ref{lemma-Noetherian-permanence}.
\end{proof}

\noindent
Here are some fun lemmas that are sometimes useful.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-Noetherian-field-extension}
Soit $k$ un corps et soit $R$ une $k$-algèbre noethérienne.
Si $K/k$ est une extension de corps de type fini, alors
$K \otimes_k R$ est noethérien.
\end{lemma}

\begin{proof}
Puisque $K/k$ est une extension de corps de type fini, il existe
une $k$-algèbre de type fini $B \subset K$ telle que $K$ soit
le corps des fractions de $B$. Autrement dit, $K = S^{-1}B$,
où $S = B \setminus \{0\}$. Alors $K \otimes_k R = S^{-1}(B \otimes_k R)$.
Puis, $B \otimes_k R$ est noethérien d'après le
lemme \ref{lemma-Noetherian-base-change-finite-type}.
Enfin, $K \otimes_k R = S^{-1}(B \otimes_k R)$ est noethérien d'après le
lemme \ref{lemma-Noetherian-permanence}.
\end{proof}

\noindent
Voici quelques lemmes amusants qui sont parfois utiles.
```

</details>

### 10 — lemma-subring-of-local-ring

Anglais L6186–6217 ; français L6166–6197.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6186) · FR-ALGEBRA-B9-CHOICE-0010.

Chacune des trois hypothèses est suffisante séparément. Anneau intègre rend domain, réduit ne signifie pas intègre. Le produit des fi est pris seulement pour les premiers minimaux non contenus dans p ; la réduction assure l'injection dans le produit de corps citée à la fin. La mention de détails omis demeure explicite. Aucun argument supplémentaire n'entre dans la traduction.

Règles : FR-ALGEBRA-B9-RULE-NOETHERIEN, FR-ALGEBRA-B9-RULE-FINITE, FR-ALGEBRA-B9-RULE-SPECTRE, FR-ALGEBRA-B9-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-subring-of-local-ring}
Let $R$ be a ring and $\mathfrak p \subset R$ be a prime.
There exists an $f \in R$, $f \not \in \mathfrak p$ such
that $R_f \to R_\mathfrak p$ is injective in each of the
following cases
\begin{enumerate}
\item $R$ is a domain,
\item $R$ is Noetherian, or
\item $R$ is reduced and has finitely many minimal primes.
\end{enumerate}
\end{lemma}

\begin{proof}
If $R$ is a domain, then $R \subset R_\mathfrak p$, hence $f = 1$ works.
If $R$ is Noetherian, then the kernel $I$ of $R \to R_\mathfrak p$
is a finitely generated ideal and we can find
$f \in R$, $f \not \in \mathfrak p$ such that $IR_f = 0$.
For this $f$ the map $R_f \to R_\mathfrak p$ is injective
and $f$ works. If $R$ is reduced with finitely
many minimal primes $\mathfrak p_1, \ldots, \mathfrak p_n$,
then we can choose
$f \in \bigcap_{\mathfrak p_i \not \subset \mathfrak p} \mathfrak p_i$,
$f \not \in \mathfrak p$. Indeed, if $\mathfrak{p}_i\not\subset
\mathfrak{p}$ then there exist $f_i \in \mathfrak{p}_i$,
$f_i \not\in \mathfrak{p}$ and $f = \prod f_i$ works.
For this $f$ we have $R_f \subset R_\mathfrak p$ because the minimal
primes of $R_f$ correspond to minimal primes of $R_\mathfrak p$
and we can apply Lemma \ref{lemma-reduced-ring-sub-product-fields}
(some details omitted).
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-subring-of-local-ring}
Soient $R$ un anneau et $\mathfrak p \subset R$ un idéal premier.
Il existe un $f \in R$, $f \not \in \mathfrak p$, tel
que $R_f \to R_\mathfrak p$ soit injectif dans chacun des
cas suivants :
\begin{enumerate}
\item $R$ est un anneau intègre,
\item $R$ est noethérien, ou
\item $R$ est réduit et possède un nombre fini d'idéaux premiers minimaux.
\end{enumerate}
\end{lemma}

\begin{proof}
Si $R$ est un anneau intègre, alors $R \subset R_\mathfrak p$, et donc $f = 1$ convient.
Si $R$ est noethérien, alors le noyau $I$ de $R \to R_\mathfrak p$
est un idéal de type fini, et nous pouvons trouver
$f \in R$, $f \not \in \mathfrak p$, tel que $IR_f = 0$.
Pour ce $f$, le morphisme $R_f \to R_\mathfrak p$ est injectif,
et $f$ convient. Si $R$ est réduit et possède un nombre
fini d'idéaux premiers minimaux $\mathfrak p_1, \ldots, \mathfrak p_n$,
alors nous pouvons choisir
$f \in \bigcap_{\mathfrak p_i \not \subset \mathfrak p} \mathfrak p_i$,
$f \not \in \mathfrak p$. En effet, si $\mathfrak{p}_i\not\subset
\mathfrak{p}$, alors il existe $f_i \in \mathfrak{p}_i$,
$f_i \not\in \mathfrak{p}$, et $f = \prod f_i$ convient.
Pour ce $f$, nous avons $R_f \subset R_\mathfrak p$, car les idéaux premiers
minimaux de $R_f$ correspondent aux idéaux premiers minimaux de $R_\mathfrak p$
et nous pouvons appliquer le lemme \ref{lemma-reduced-ring-sub-product-fields}
(certains détails sont omis).
\end{proof}
```

</details>

### 11 — lemma-surjective-endo-noetherian-ring-is-iso

Anglais L6218–6237 ; français L6198–6217.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6218) · FR-ALGEBRA-B9-CHOICE-0011.

Endomorphisme surjectif conserve l'hypothèse essentielle. Si le noyau est non nul, la surjectivité fournit des antécédents qui rendent strictes les inclusions des noyaux itérés ; la contradiction est l'ascendance infinie. Aucun énoncé inverse sur les endomorphismes injectifs n'est suggéré.

Règles : FR-ALGEBRA-B9-RULE-NOETHERIEN, FR-ALGEBRA-B9-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-surjective-endo-noetherian-ring-is-iso}
Any surjective endomorphism of a Noetherian ring is an isomorphism.
\end{lemma}

\begin{proof}
If $f : R \to R$ were such an endomorphism but not injective, then
$$
\Ker(f) \subset \Ker(f \circ f) \subset
\Ker(f \circ f \circ f) \subset \ldots
$$
would be a strictly increasing chain of ideals.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-surjective-endo-noetherian-ring-is-iso}
Tout endomorphisme surjectif d'un anneau noethérien est un isomorphisme.
\end{lemma}

\begin{proof}
Si $f : R \to R$ était un tel endomorphisme sans être injectif, alors
$$
\Ker(f) \subset \Ker(f \circ f) \subset
\Ker(f \circ f \circ f) \subset \ldots
$$
serait une chaîne strictement croissante d'idéaux.
\end{proof}
```

</details>

### 12 — section-locally-nilpotent

Anglais L6238–6243 ; français L6218–6223.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6238) · FR-ALGEBRA-B9-CHOICE-0012.

Le titre et la transition annoncent la définition locale au sens élément par élément. Localement ne renvoie ici ni à une localisation en un premier ni à un voisinage topologique. La définition anglaise gouverne ce sens.

Règles : FR-ALGEBRA-B9-RULE-NILPOTENCE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Locally nilpotent ideals}
\label{section-locally-nilpotent}

\noindent
Here is the definition.
```

Français restauré :
```tex
\section{Idéaux localement nilpotents}
\label{section-locally-nilpotent}

\noindent
Voici la définition.
```

</details>

### 13 — definition-locally-nilpotent-ideal

Anglais L6244–6252 ; français L6224–6232.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6244) · FR-ALGEBRA-B9-CHOICE-0013.

La différence de portée est conservée mot à mot au niveau logique : pour chaque x existe n, contre il existe n tel que I^n=0. Localement nilpotent est retenu avec sa définition explicite, sans prétendre que les pages françaises lues attestent ce syntagme. Idéal de nilpotents serait descriptif mais effacerait le nom choisi par la source.

Point particulier à relire : Le terme localement nilpotent est conservé par définition ; attestation française spécialisée non acquise dans ce lot.

Règles : FR-ALGEBRA-B9-RULE-NILPOTENCE, FR-ALGEBRA-B9-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-locally-nilpotent-ideal}
Let $R$ be a ring. Let $I \subset R$ be an ideal.
We say $I$ is {\it locally nilpotent} if for every
$x \in I$ there exists an $n \in \mathbf{N}$ such
that $x^n = 0$. We say $I$ is {\it nilpotent} if
there exists an $n \in \mathbf{N}$ such that $I^n = 0$.
\end{definition}
```

Français restauré :
```tex
\begin{definition}
\label{definition-locally-nilpotent-ideal}
Soit $R$ un anneau. Soit $I \subset R$ un idéal.
Nous disons que $I$ est {\it localement nilpotent} si, pour tout
$x \in I$, il existe un $n \in \mathbf{N}$ tel
que $x^n = 0$. Nous disons que $I$ est {\it nilpotent} s'il
existe un $n \in \mathbf{N}$ tel que $I^n = 0$.
\end{definition}
```

</details>

### 14 — example-locally-nilpotent-not-nilpotent

Anglais L6253–6266 ; français L6233–6246.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6253) · FR-ALGEBRA-B9-CHOICE-0014.

L'infinité des générateurs permet l'absence d'exposant uniforme ; chaque combinaison linéaire reste finie. Les trois indices n, n+1 et les exposants demeurent inchangés. L'ambiguïté de N contenant ou non zéro est documentée séparément, sans introduire n≥1 dans le corps de la traduction.

Point particulier à relire : Si N contient zéro, x0^0=1 détruit l'exemple. L'observation est conditionnelle à la convention d'indices, non une admission d'erratum.

Règles : FR-ALGEBRA-B9-RULE-NILPOTENCE, FR-ALGEBRA-B9-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{example}
\label{example-locally-nilpotent-not-nilpotent}
Let $R = k[x_n | n \in \mathbf{N}]$ be the polynomial ring in infinitely
many variables over a field $k$. Let $I$ be the ideal generated by
the elements $x_n^n$ for $n \in \mathbf{N}$ and $S = R/I$. Then the ideal
$J \subset S$ generated by the images of $x_n$, $n \in \mathbf{N}$
is locally nilpotent, but not nilpotent. Indeed, since $S$-linear
combinations of nilpotents are nilpotent, to prove that $J$ is locally
nilpotent it is enough to observe that all its generators are nilpotent
(which they obviously are). On the other hand, for each $n \in \mathbf{N}$
it holds that $x_{n + 1}^n \not \in I$, so that $J^n \not = 0$.
It follows that $J$ is not nilpotent.
\end{example}
```

Français restauré :
```tex
\begin{example}
\label{example-locally-nilpotent-not-nilpotent}
Soit $R = k[x_n | n \in \mathbf{N}]$ l'anneau de polynômes en une infinité
de variables sur un corps $k$. Soit $I$ l'idéal engendré par
les éléments $x_n^n$ pour $n \in \mathbf{N}$, et soit $S = R/I$. Alors l'idéal
$J \subset S$ engendré par les images des $x_n$, $n \in \mathbf{N}$,
est localement nilpotent, mais n'est pas nilpotent. En effet, puisque les combinaisons
$S$-linéaires d'éléments nilpotents sont nilpotentes, pour prouver que $J$ est localement
nilpotent, il suffit d'observer que tous ses générateurs sont nilpotents
(ce qu'ils sont manifestement). D'autre part, pour tout $n \in \mathbf{N}$,
nous avons $x_{n + 1}^n \not \in I$, de sorte que $J^n \not = 0$.
Il s'ensuit que $J$ n'est pas nilpotent.
\end{example}
```

</details>

### 15 — lemma-locally-nilpotent

Anglais L6267–6278 ; français L6247–6258.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6267) · FR-ALGEBRA-B9-CHOICE-0015.

L'idéal étendu IR' reste localement nilpotent ; cela utilise les combinaisons finies et la commutativité dans R'. La somme des deux éléments nilpotents est traitée avec l'exposant n+m−1 exact. On ne transpose pas ce raisonnement sans hypothèse au cas non commutatif du lemme ultérieur.

Règles : FR-ALGEBRA-B9-RULE-NILPOTENCE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-locally-nilpotent}
Let $R \to R'$ be a ring map and let $I \subset R$ be a locally nilpotent
ideal. Then $IR'$ is a locally nilpotent ideal of $R'$.
\end{lemma}

\begin{proof}
This follows from the fact that if $x, y \in R'$ are nilpotent, then
$x + y$ is nilpotent too. Namely, if $x^n = 0$ and $y^m = 0$, then
$(x + y)^{n + m - 1} = 0$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-locally-nilpotent}
Soit $R \to R'$ un morphisme d'anneaux et soit $I \subset R$ un idéal localement
nilpotent. Alors $IR'$ est un idéal localement nilpotent de $R'$.
\end{lemma}

\begin{proof}
Cela résulte du fait que, si $x, y \in R'$ sont nilpotents, alors
$x + y$ l'est aussi. En effet, si $x^n = 0$ et $y^m = 0$, alors
$(x + y)^{n + m - 1} = 0$.
\end{proof}
```

</details>

### 16 — lemma-locally-nilpotent-unit

Anglais L6279–6298 ; français L6259–6278.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6279) · FR-ALGEBRA-B9-CHOICE-0016.

Unité signifie élément inversible, non élément non nul. Les deux implications, l'inverse modulo I et la congruence modulo xR sont conservés. Le passage à z^N utilise un exposant dépendant de z ; aucune nilpotence uniforme de I n'est présupposée.

Règles : FR-ALGEBRA-B9-RULE-NILPOTENCE, FR-ALGEBRA-B9-RULE-UNIT, FR-ALGEBRA-B9-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-locally-nilpotent-unit}
Let $R$ be a ring and let $I \subset R$ be a locally nilpotent
ideal.
An element $x$ of $R$ is a unit if and only if the image of $x$
in $R/I$ is a unit.
\end{lemma}

\begin{proof}
If $x$ is a unit in $R$, then its image is clearly a unit in $R/I$.
It remains to prove the converse.
Assume the image of $y \in R$ in $R/I$ is the inverse of the image of $x$.
Then $xy = 1 - z$ for some $z \in I$.
This means that $1\equiv z$ modulo $xR$.
Since $z$ lies in the locally nilpotent ideal
$I$, we have $z^N = 0$ for some sufficiently large $N$.
It follows that $1 = 1^N \equiv z^N = 0$ modulo $xR$.
In other words, $x$ divides $1$ and is hence a unit.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-locally-nilpotent-unit}
Soit $R$ un anneau et soit $I \subset R$ un idéal localement
nilpotent.
Un élément $x$ de $R$ est une unité si et seulement si l'image de $x$
dans $R/I$ est une unité.
\end{lemma}

\begin{proof}
Si $x$ est une unité de $R$, alors son image est clairement une unité de $R/I$.
Il reste à démontrer la réciproque.
Supposons que l'image de $y \in R$ dans $R/I$ soit l'inverse de l'image de $x$.
Alors $xy = 1 - z$ pour un certain $z \in I$.
Cela signifie que $1\equiv z$ modulo $xR$.
Puisque $z$ appartient à l'idéal localement nilpotent
$I$, nous avons $z^N = 0$ pour un certain $N$ assez grand.
Il s'ensuit que $1 = 1^N \equiv z^N = 0$ modulo $xR$.
Autrement dit, $x$ divise $1$ et est donc une unité.
\end{proof}
```

</details>

### 17 — lemma-Noetherian-power

Anglais L6299–6317 ; français L6279–6297.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6299) · FR-ALGEBRA-B9-CHOICE-0017.

Le résultat général J contenu dans le radical de I précède le cas particulier de la nilpotence. Le caractère noethérien donne une liste finie de générateurs de J. L'exposant somme des di plus 1 est conservé : il est suffisant, même s'il n'est pas optimal. Aucun raccourcissement esthétique de la borne n'est autorisé.

Règles : FR-ALGEBRA-B9-RULE-NOETHERIEN, FR-ALGEBRA-B9-RULE-NILPOTENCE, FR-ALGEBRA-B9-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Noetherian-power}
\begin{slogan}
An ideal in a Noetherian ring is nilpotent if each element
of the ideal is nilpotent.
\end{slogan}
Let $R$ be a Noetherian ring. Let $I, J$ be ideals of $R$.
Suppose $J \subset \sqrt{I}$. Then $J^n \subset I$ for some $n$.
In particular, in a Noetherian ring the notions of
``locally nilpotent ideal''
and ``nilpotent ideal'' coincide.
\end{lemma}

\begin{proof}
Say $J = (f_1, \ldots, f_s)$.
By assumption $f_i^{d_i} \in I$.
Take $n = d_1 + d_2 + \ldots + d_s + 1$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-Noetherian-power}
\begin{slogan}
Un idéal d'un anneau noethérien est nilpotent si chacun de ses éléments
est nilpotent.
\end{slogan}
Soit $R$ un anneau noethérien. Soient $I, J$ des idéaux de $R$.
Supposons que $J \subset \sqrt{I}$. Alors $J^n \subset I$ pour un certain $n$.
En particulier, dans un anneau noethérien, les notions d'
« idéal localement nilpotent »
et d'« idéal nilpotent » coïncident.
\end{lemma}

\begin{proof}
Écrivons $J = (f_1, \ldots, f_s)$.
Par hypothèse, $f_i^{d_i} \in I$.
Prenons $n = d_1 + d_2 + \ldots + d_s + 1$.
\end{proof}
```

</details>

### 18 — lemma-lift-idempotents

Anglais L6318–6384 ; français L6298–6364.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6318) · FR-ALGEBRA-B9-CHOICE-0018.

Relèvement rend lift ; les deux preuves restent complètes. La première compare les spectres, non les anneaux eux-mêmes. La seconde ne suppose nilpotent que l'idéal principal J engendré par f²−f, puis double l'ordre d'erreur. Les identités polynomiales et l'argument d'unicité par les puissances impaires du nilpotent e1−e2 sont conservés. Première et Seconde démonstration sont des titres optionnels traduits et vérifiés séparément.

Point particulier à relire : La réduction modulo un idéal nilpotent donne le même espace spectral, pas un isomorphisme d'anneaux. Les deux preuves et leur ordre sont conservés.

Règles : FR-ALGEBRA-B9-RULE-NILPOTENCE, FR-ALGEBRA-B9-RULE-LIFT, FR-ALGEBRA-B9-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-lift-idempotents}
Let $R$ be a ring. Let $I \subset R$ be a locally nilpotent ideal.
Then $R \to R/I$ induces a bijection on idempotents.
\end{lemma}

\begin{proof}[First proof of Lemma \ref{lemma-lift-idempotents}]
As $I$ is locally nilpotent it is contained in every prime ideal.
Hence $\Spec(R/I) = V(I) = \Spec(R)$. Hence the
lemma follows from Lemma \ref{lemma-disjoint-decomposition}.
\end{proof}

\begin{proof}[Second proof of Lemma \ref{lemma-lift-idempotents}]
Suppose $\overline{e} \in R/I$ is an idempotent.
We have to lift $\overline{e}$ to an idempotent of $R$.

\medskip\noindent
First, choose any lift $f \in R$ of $\overline{e}$, and set
$x = f^2 - f$. Then, $x \in I$, so $x$ is nilpotent (since $I$
is locally nilpotent). Let now $J$ be the ideal of $R$ generated
by $x$. Then, $J$ is nilpotent (not just locally nilpotent),
since it is generated by the nilpotent $x$.

\medskip\noindent
Now, assume that we have found a lift $e \in R$ of $\overline{e}$
such that $e^2 - e \in J^k$ for some $k \geq 1$.
Let $e' = e - (2e - 1)(e^2 - e) = 3e^2 - 2e^3$, which is another
lift of $\overline{e}$ (since the idempotency of $\overline{e}$
yields $e^2 - e \in I$). Then
$$
(e')^2 - e' = (4e^2 - 4e - 3)(e^2 - e)^2 \in J^{2k}
$$
by a simple computation.

\medskip\noindent
We thus have started with a lift $e$ of $\overline{e}$ such
that $e^2 - e \in J^k$, and obtained a lift $e'$ of
$\overline{e}$ such that $(e')^2 - e' \in J^{2k}$.
This way we can successively improve the approximation
(starting with $e = f$, which fits the bill for $k = 1$).
Eventually, we reach a stage where $J^k = 0$, and at that
stage we have a lift $e$ of $\overline{e}$ such that
$e^2 - e \in J^k = 0$, that is, this $e$ is idempotent.

\medskip\noindent
We thus have seen that if $\overline{e} \in R/I$ is any
idempotent, then there exists a lift of $\overline{e}$
which is an idempotent of $R$.
It remains to prove that this lift is unique. Indeed, let
$e_1$ and $e_2$ be two such lifts. We
need to show that $e_1 = e_2$.

\medskip\noindent
By definition of $e_1$ and $e_2$, we have $e_1 \equiv e_2
\mod I$, and both $e_1$ and $e_2$ are idempotent. From
$e_1 \equiv e_2 \mod I$, we see that $e_1 - e_2 \in I$,
so that $e_1 - e_2$ is nilpotent (since $I$ is locally nilpotent).
A straightforward
computation (using the idempotency of $e_1$ and $e_2$)
reveals that $(e_1 - e_2)^3 = e_1 - e_2$. Using this and
induction, we obtain $(e_1 - e_2)^k = e_1 - e_2$ for any
positive odd integer $k$. Since all high enough $k$ satisfy
$(e_1 - e_2)^k = 0$ (since $e_1 - e_2$ is nilpotent),
this shows $e_1 - e_2 = 0$, so that $e_1 = e_2$, which
completes our proof.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-lift-idempotents}
Soit $R$ un anneau. Soit $I \subset R$ un idéal localement nilpotent.
Alors $R \to R/I$ induit une bijection sur les idempotents.
\end{lemma}

\begin{proof}[Première démonstration du lemme \ref{lemma-lift-idempotents}]
Puisque $I$ est localement nilpotent, il est contenu dans tout idéal premier.
Ainsi, $\Spec(R/I) = V(I) = \Spec(R)$. Le
lemme résulte donc du lemme \ref{lemma-disjoint-decomposition}.
\end{proof}

\begin{proof}[Seconde démonstration du lemme \ref{lemma-lift-idempotents}]
Supposons que $\overline{e} \in R/I$ soit un idempotent.
Nous devons relever $\overline{e}$ en un idempotent de $R$.

\medskip\noindent
Choisissons d'abord un relèvement quelconque $f \in R$ de $\overline{e}$ et posons
$x = f^2 - f$. Alors $x \in I$, donc $x$ est nilpotent (puisque $I$
est localement nilpotent). Soit maintenant $J$ l'idéal de $R$ engendré
par $x$. Alors $J$ est nilpotent (et pas seulement localement nilpotent),
puisqu'il est engendré par l'élément nilpotent $x$.

\medskip\noindent
Supposons maintenant que nous ayons trouvé un relèvement $e \in R$ de $\overline{e}$
tel que $e^2 - e \in J^k$ pour un certain $k \geq 1$.
Soit $e' = e - (2e - 1)(e^2 - e) = 3e^2 - 2e^3$, qui est un autre
relèvement de $\overline{e}$ (car l'idempotence de $\overline{e}$
donne $e^2 - e \in I$). Alors
$$
(e')^2 - e' = (4e^2 - 4e - 3)(e^2 - e)^2 \in J^{2k}
$$
par un calcul direct.

\medskip\noindent
Nous sommes donc partis d'un relèvement $e$ de $\overline{e}$ tel
que $e^2 - e \in J^k$, et nous avons obtenu un relèvement $e'$ de
$\overline{e}$ tel que $(e')^2 - e' \in J^{2k}$.
Nous pouvons ainsi améliorer successivement l'approximation
(en commençant par $e = f$, qui convient pour $k = 1$).
Nous finissons par atteindre un stade où $J^k = 0$, et à ce
stade nous disposons d'un relèvement $e$ de $\overline{e}$ tel que
$e^2 - e \in J^k = 0$, c'est-à-dire que cet $e$ est idempotent.

\medskip\noindent
Nous avons ainsi vu que, si $\overline{e} \in R/I$ est un
idempotent quelconque, il existe un relèvement de $\overline{e}$
qui est un idempotent de $R$.
Il reste à montrer que ce relèvement est unique. En effet, soient
$e_1$ et $e_2$ deux tels relèvements. Nous
devons montrer que $e_1 = e_2$.

\medskip\noindent
Par définition de $e_1$ et de $e_2$, nous avons $e_1 \equiv e_2
\mod I$, et $e_1$ et $e_2$ sont tous deux idempotents. De
$e_1 \equiv e_2 \mod I$, nous déduisons que $e_1 - e_2 \in I$,
de sorte que $e_1 - e_2$ est nilpotent (puisque $I$ est localement nilpotent).
Un calcul direct
(utilisant l'idempotence de $e_1$ et de $e_2$)
montre que $(e_1 - e_2)^3 = e_1 - e_2$. En utilisant cela et
une récurrence, nous obtenons $(e_1 - e_2)^k = e_1 - e_2$ pour tout
entier impair positif $k$. Comme tout $k$ assez grand vérifie
$(e_1 - e_2)^k = 0$ (puisque $e_1 - e_2$ est nilpotent),
cela montre que $e_1 - e_2 = 0$, et donc que $e_1 = e_2$, ce qui
achève la démonstration.
\end{proof}
```

</details>

### 19 — lemma-lift-idempotents-noncommutative

Anglais L6385–6400 ; français L6365–6380.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6385) · FR-ALGEBRA-B9-CHOICE-0019.

Éventuellement non commutative préserve la portée plus large de A. La réduction à Z[e]/((e²−e)^n) est licite parce que tous les polynômes utilisés sont dans un seul élément. Le lemme affirme l'existence d'un relèvement de la forme donnée, et non une unicité générale dans A. Le français n'importe pas l'unicité du cas commutatif.

Règles : FR-ALGEBRA-B9-RULE-NILPOTENCE, FR-ALGEBRA-B9-RULE-LIFT, FR-ALGEBRA-B9-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-lift-idempotents-noncommutative}
Let $A$ be a possibly noncommutative algebra.
Let $e \in A$ be an element such that $x = e^2 - e$ is nilpotent.
Then there exists an idempotent of the form
$e' = e + x(\sum a_{i, j}e^ix^j) \in A$
with $a_{i, j} \in \mathbf{Z}$.
\end{lemma}

\begin{proof}
Consider the ring $R_n = \mathbf{Z}[e]/((e^2 - e)^n)$. It is clear that
if we can prove the result for each $R_n$ then the lemma follows.
In $R_n$ consider the ideal $I = (e^2 - e)$ and apply
Lemma \ref{lemma-lift-idempotents}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-lift-idempotents-noncommutative}
Soit $A$ une algèbre éventuellement non commutative.
Soit $e \in A$ un élément tel que $x = e^2 - e$ soit nilpotent.
Il existe alors un idempotent de la forme
$e' = e + x(\sum a_{i, j}e^ix^j) \in A$,
avec $a_{i, j} \in \mathbf{Z}$.
\end{lemma}

\begin{proof}
Considérons l'anneau $R_n = \mathbf{Z}[e]/((e^2 - e)^n)$. Il est clair que,
si nous pouvons démontrer le résultat pour chaque $R_n$, le lemme en résulte.
Dans $R_n$, considérons l'idéal $I = (e^2 - e)$ et appliquons le
lemme \ref{lemma-lift-idempotents}.
\end{proof}
```

</details>

### 20 — lemma-lift-nth-roots

Anglais L6401–6444 ; français L6381–6424.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6401) · FR-ALGEBRA-B9-CHOICE-0020.

L'élévation à la puissance n-ième est une bijection sur 1+I, pas sur tout R. L'hypothèse n inversible dans R/I et sa remontée dans R sont préservées. La série binomiale est finie après substitution d'un nilpotent ; il ne s'agit pas de convergence analytique. Les coefficients dans Z[1/n] restent ceux de la source : les dénominateurs affichés ne conduisent pas à ajouter l'inversibilité de toutes les factorielles.

Point particulier à relire : Le contrôle de structure n'est pas une démonstration automatique de l'intégralité des coefficients binomiaux ; cette assertion et ses détails omis restent ceux de la source.

Règles : FR-ALGEBRA-B9-RULE-NILPOTENCE, FR-ALGEBRA-B9-RULE-UNIT, FR-ALGEBRA-B9-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-lift-nth-roots}
Let $R$ be a ring. Let $I \subset R$ be a locally nilpotent ideal.
Let $n \geq 1$ be an integer which is invertible in $R/I$. Then
\begin{enumerate}
\item the $n$th power map $1 + I \to 1 + I$, $1 + x \mapsto (1 + x)^n$
is a bijection,
\item a unit of $R$ is a $n$th power if and only if its image in $R/I$
is an $n$th power.
\end{enumerate}
\end{lemma}

\begin{proof}
Let $a \in R$ be a unit whose image in $R/I$ is the same as the image
of $b^n$ with $b \in R$. Then $b$ is a unit
(Lemma \ref{lemma-locally-nilpotent-unit}) and
$ab^{-n} = 1 + x$ for some $x \in I$. Hence $ab^{-n} = c^n$ by
part (1). Thus (2) follows from (1).

\medskip\noindent
Proof of (1). This is true because there is an inverse to the
map $1 + x \mapsto (1 + x)^n$. Namely, we can consider the map
which sends $1 + x$ to
\begin{align*}
(1 + x)^{1/n}
& =
1 + {1/n \choose 1}x +
{1/n \choose 2}x^2 +
{1/n \choose 3}x^3 + \ldots \\
& =
1 + \frac{1}{n} x + \frac{1 - n}{2n^2}x^2 +
\frac{(1 - n)(1 - 2n)}{6n^3}x^3 + \ldots
\end{align*}
as in elementary calculus. This makes sense because the series is finite
as $x^k = 0$ for all $k \gg 0$ and each coefficient
${1/n \choose k} \in \mathbf{Z}[1/n]$ (details omitted; observe that
$n$ is invertible in $R$ by Lemma \ref{lemma-locally-nilpotent-unit}).
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-lift-nth-roots}
Soit $R$ un anneau. Soit $I \subset R$ un idéal localement nilpotent.
Soit $n \geq 1$ un entier inversible dans $R/I$. Alors
\begin{enumerate}
\item l'application d'élévation à la puissance $n$-ième $1 + I \to 1 + I$, $1 + x \mapsto (1 + x)^n$
est une bijection,
\item une unité de $R$ est une puissance $n$-ième si et seulement si son image dans $R/I$
est une puissance $n$-ième.
\end{enumerate}
\end{lemma}

\begin{proof}
Soit $a \in R$ une unité dont l'image dans $R/I$ est égale à l'image
de $b^n$, avec $b \in R$. Alors $b$ est une unité
(lemme \ref{lemma-locally-nilpotent-unit}) et
$ab^{-n} = 1 + x$ pour un certain $x \in I$. Ainsi, $ab^{-n} = c^n$ d'après
la partie (1). La partie (2) résulte donc de la partie (1).

\medskip\noindent
Démontrons (1). Cela est vrai parce que l'application
$1 + x \mapsto (1 + x)^n$ possède une inverse. Nous pouvons en effet considérer l'application
qui envoie $1 + x$ sur
\begin{align*}
(1 + x)^{1/n}
& =
1 + {1/n \choose 1}x +
{1/n \choose 2}x^2 +
{1/n \choose 3}x^3 + \ldots \\
& =
1 + \frac{1}{n} x + \frac{1 - n}{2n^2}x^2 +
\frac{(1 - n)(1 - 2n)}{6n^3}x^3 + \ldots
\end{align*}
comme en calcul élémentaire. Cette expression a un sens, car la série est finie,
puisque $x^k = 0$ pour tout $k \gg 0$, et que chaque coefficient
$ {1/n \choose k} \in \mathbf{Z}[1/n]$ (détails omis ; observons que
$n$ est inversible dans $R$ d'après le lemme \ref{lemma-locally-nilpotent-unit}).
\end{proof}
```

</details>

### 21 — section-curiosity

Anglais L6445–6454 ; français L6425–6434.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6445) · FR-ALGEBRA-B9-CHOICE-0021.

Curiosité est un titre non technique maintenu. L'introduction oppose V(I) ouvert et l'image d'un spectre localisé fermée. Réponse partielle et la référence aux idéaux purs sont conservées ; on ne transforme pas ces deux lemmes en classification complète.

Règles : Titre et contexte directement comparés.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Curiosity}
\label{section-curiosity}

\noindent
Lemma \ref{lemma-disjoint-implies-product}
explains what happens if $V(I)$ is open for some ideal $I \subset R$.
But what if $\Spec(S^{-1}R)$ is closed in $\Spec(R)$?
The next two lemmas give a partial answer. For more information see
Section \ref{section-pure-ideals}.
```

Français restauré :
```tex
\section{Curiosité}
\label{section-curiosity}

\noindent
Le lemme \ref{lemma-disjoint-implies-product}
explique ce qui se passe lorsque $V(I)$ est ouvert pour un certain idéal $I \subset R$.
Mais qu'en est-il si $\Spec(S^{-1}R)$ est fermé dans $\Spec(R)$ ?
Les deux lemmes suivants donnent une réponse partielle. Pour plus d'informations, voir la
section \ref{section-pure-ideals}.
```

</details>

### 22 — lemma-invert-closed-quotient

Anglais L6455–6478 ; français L6435–6458.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6455) · FR-ALGEBRA-B9-CHOICE-0022.

Partie multiplicative et localisation correspondent à l'usage de Dat p.8. I est le noyau tandis que I' définit initialement le fermé image : leurs rôles restent distincts. L'argument identifie V(I') à V(I), puis les éléments de S sont inversibles modulo I. La conclusion par deux morphismes injectifs est une compression de source ; leur caractère canonique les rend inverses, ce qui est expliqué en note séparée sans récrire la preuve.

Point particulier à relire : Des injections réciproques ne suffisent pas en général à donner un isomorphisme. Ici les deux applications canoniques sont inverses ; ce complément explicatif reste hors traduction.

Règles : FR-ALGEBRA-B9-RULE-LOCALISATION, FR-ALGEBRA-B9-RULE-UNIT.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-invert-closed-quotient}
Let $R$ be a ring. Let $S \subset R$ be a multiplicative subset.
Assume the image of the map $\Spec(S^{-1}R) \to \Spec(R)$
is closed. Then $S^{-1}R \cong R/I$ for some ideal $I \subset R$.
\end{lemma}

\begin{proof}
Let $I = \Ker(R \to S^{-1}R)$ so that $V(I)$ contains the image.
Say the image is the closed subset $V(I') \subset \Spec(R)$ for
some ideal $I' \subset R$. So $V(I') \subset V(I)$.
For $f \in I'$ we see that $f/1 \in S^{-1}R$
is contained in every prime ideal. Hence $f^n$ maps to zero in $S^{-1}R$
for some $n \geq 1$ (Lemma \ref{lemma-Zariski-topology}).
Hence $V(I') = V(I)$.
Then this implies every $g \in S$ is invertible mod $I$.
Hence we get ring maps $R/I \to S^{-1}R$ and $S^{-1}R \to R/I$.
The first map is injective by choice of $I$.
The second is the map $S^{-1}R \to S^{-1}(R/I) = R/I$ which
has kernel $S^{-1}I$ because localization is exact.
Since $S^{-1}I = 0$ we see also the second map is injective.
Hence $S^{-1}R \cong R/I$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-invert-closed-quotient}
Soit $R$ un anneau. Soit $S \subset R$ une partie multiplicative.
Supposons que l'image du morphisme $\Spec(S^{-1}R) \to \Spec(R)$
soit fermée. Alors $S^{-1}R \cong R/I$ pour un certain idéal $I \subset R$.
\end{lemma}

\begin{proof}
Soit $I = \Ker(R \to S^{-1}R)$, de sorte que $V(I)$ contient l'image.
Disons que l'image est le fermé $V(I') \subset \Spec(R)$ pour
un certain idéal $I' \subset R$. Ainsi, $V(I') \subset V(I)$.
Pour $f \in I'$, nous voyons que $f/1 \in S^{-1}R$
appartient à tout idéal premier. Ainsi, $f^n$ s'envoie sur zéro dans $S^{-1}R$
pour un certain $n \geq 1$ (lemme \ref{lemma-Zariski-topology}).
Par conséquent, $V(I') = V(I)$.
Cela implique que tout $g \in S$ est inversible modulo $I$.
Nous obtenons donc des morphismes d'anneaux $R/I \to S^{-1}R$ et $S^{-1}R \to R/I$.
Le premier morphisme est injectif par le choix de $I$.
Le second est le morphisme $S^{-1}R \to S^{-1}(R/I) = R/I$, qui
a pour noyau $S^{-1}I$, car la localisation est exacte.
Puisque $S^{-1}I = 0$, nous voyons que le second morphisme est lui aussi injectif.
Ainsi, $S^{-1}R \cong R/I$.
\end{proof}
```

</details>

### 23 — lemma-invert-closed-split

Anglais L6479–6519 ; français L6459–6499.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6479) · FR-ALGEBRA-B9-CHOICE-0023.

Les trois hypothèses alternatives sont conservées, avec S de type fini comme monoïde, non comme idéal. Le cas noethérien topologique utilise la quasi-compacité du complémentaire ; le cas monoïde utilise le produit des générateurs. La décomposition est un produit d'anneaux obtenu après que V(I) est aussi ouvert. Le mot fermé concerne l'image dans le spectre, pas une prétendue application fermée arbitraire.

Règles : FR-ALGEBRA-B9-RULE-NOETHERIEN, FR-ALGEBRA-B9-RULE-FINITE, FR-ALGEBRA-B9-RULE-LOCALISATION, FR-ALGEBRA-B9-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-invert-closed-split}
Let $R$ be a ring. Let $S \subset R$ be a multiplicative subset.
Assume the image of the map $\Spec(S^{-1}R) \to \Spec(R)$
is closed. If $R$ is Noetherian, or $\Spec(R)$ is a
Noetherian topological space, or $S$ is finitely generated as a monoid,
then $R \cong S^{-1}R \times R'$ for some ring $R'$.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-invert-closed-quotient} we have $S^{-1}R \cong R/I$
for some ideal $I \subset R$. By Lemma \ref{lemma-disjoint-implies-product}
it suffices to show that $V(I)$ is open.
If $R$ is Noetherian then $\Spec(R)$ is a Noetherian
topological space, see Lemma \ref{lemma-Noetherian-topology}.
If $\Spec(R)$ is a Noetherian topological space,
then the complement $\Spec(R) \setminus V(I)$ is quasi-compact, see
Topology, Lemma \ref{topology-lemma-Noetherian-quasi-compact}.
Hence there exist finitely many $f_1, \ldots, f_n \in I$ such
that $V(I) = V(f_1, \ldots, f_n)$.
Since each $f_i$ maps to zero in $S^{-1}R$
there exists a $g \in S$ such that $gf_i = 0$ for
$i = 1, \ldots, n$. Hence $D(g) = V(I)$ as desired.
In case $S$ is finitely generated as a monoid, say $S$ is generated
by $g_1, \ldots, g_m$, then $S^{-1}R \cong R_{g_1 \ldots g_m}$
and we conclude that $V(I) = D(g_1 \ldots g_m)$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-invert-closed-split}
Soit $R$ un anneau. Soit $S \subset R$ une partie multiplicative.
Supposons que l'image du morphisme $\Spec(S^{-1}R) \to \Spec(R)$
soit fermée. Si $R$ est noethérien, ou si $\Spec(R)$ est un
espace topologique noethérien, ou si $S$ est de type fini comme monoïde,
alors $R \cong S^{-1}R \times R'$ pour un certain anneau $R'$.
\end{lemma}

\begin{proof}
D'après le lemme \ref{lemma-invert-closed-quotient}, nous avons $S^{-1}R \cong R/I$
pour un certain idéal $I \subset R$. D'après le lemme \ref{lemma-disjoint-implies-product},
il suffit de montrer que $V(I)$ est ouvert.
Si $R$ est noethérien, alors $\Spec(R)$ est un espace topologique
noethérien, voir le lemme \ref{lemma-Noetherian-topology}.
Si $\Spec(R)$ est un espace topologique noethérien,
alors le complémentaire $\Spec(R) \setminus V(I)$ est quasi-compact, voir
Topologie, lemme \ref{topology-lemma-Noetherian-quasi-compact}.
Il existe donc un nombre fini d'éléments $f_1, \ldots, f_n \in I$ tels
que $V(I) = V(f_1, \ldots, f_n)$.
Puisque chaque $f_i$ s'envoie sur zéro dans $S^{-1}R$,
il existe un $g \in S$ tel que $gf_i = 0$ pour
$i = 1, \ldots, n$. Ainsi, $D(g) = V(I)$, comme voulu.
Dans le cas où $S$ est de type fini comme monoïde, disons que $S$ est engendré
par $g_1, \ldots, g_m$, nous avons $S^{-1}R \cong R_{g_1 \ldots g_m}$,
et nous concluons que $V(I) = D(g_1 \ldots g_m)$.
\end{proof}
```

</details>

### 24 — section-nullstellensatz

Anglais L6520–6522 ; français L6500–6502.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6520) · FR-ALGEBRA-B9-CHOICE-0024.

Nullstellensatz de Hilbert conserve le nom historique du titre. Ducros 2.10.5 emploie aussi théorème des zéros de Hilbert. Les deux formes sont recevables ; la première est maintenue pour sa proximité avec la source, sans imposer une harmonisation inutile.

Règles : FR-ALGEBRA-B9-RULE-NULLSTELLENSATZ.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Hilbert Nullstellensatz}
\label{section-nullstellensatz}
```

Français restauré :
```tex
\section{Nullstellensatz de Hilbert}
\label{section-nullstellensatz}
```

</details>

### 25 — theorem-nullstellensatz

Anglais L6523–6609 ; français L6503–6589.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6523) · FR-ALGEBRA-B9-CHOICE-0025.

Le corps k n'est pas supposé algébriquement clos : le corps résiduel est une extension finie, pas nécessairement k. Ducros 2.10.6–2.10.9 confirme cette distinction et le vocabulaire. La récurrence, les deux cas pour p et les deux assertions restent intacts. Dans le diagramme, surjection qualifie la composée vers κ(m), non la première flèche seule. D(f) est infini au sens du spectre, même sur un corps fini, grâce aux polynômes irréductibles ; ce n'est pas une assertion sur une infinité de points k-rationnels. Ouvert principal remplace le calque isolé ouvert standard, d'après Dat 1.2.4 et l'usage du reste du chapitre. Les extensions résiduelles et l'argument final de maximalité ne changent pas.

Point particulier à relire : Ouvert principal est une réparation terminologique attestée, non une nouvelle correction mathématique. Les deux expressions anglaise et française désignent exactement D(f).

Règles : FR-ALGEBRA-B9-RULE-FINITE, FR-ALGEBRA-B9-RULE-PRINCIPAL, FR-ALGEBRA-B9-RULE-NULLSTELLENSATZ, FR-ALGEBRA-B9-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{theorem}[Hilbert Nullstellensatz]
\label{theorem-nullstellensatz}
Let $k$ be a field.
\begin{enumerate}
\item
\label{item-finite-kappa}
For any maximal ideal $\mathfrak m \subset k[x_1, \ldots, x_n]$
the field extension $\kappa(\mathfrak m)/k$ is finite.
\item
\label{item-polynomial-ring-Jacobson}
Any radical ideal $I \subset k[x_1, \ldots, x_n]$
is the intersection of maximal ideals containing it.
\end{enumerate}
The same is true in any finite type $k$-algebra.
\end{theorem}

\begin{proof}
It is enough to prove part (\ref{item-finite-kappa}) of
the theorem for the case of a polynomial
algebra $k[x_1, \ldots, x_n]$, because any finitely generated
$k$-algebra is a quotient of such a polynomial algebra.
We prove this by induction on $n$. The case $n = 0$ is clear.
Suppose that $\mathfrak m$ is a maximal ideal in $k[x_1, \ldots, x_n]$.
Let $\mathfrak p \subset k[x_n]$ be the intersection
of $\mathfrak m$ with $k[x_n]$.

\medskip\noindent
If $\mathfrak p \not = (0)$,
then $\mathfrak p$ is maximal and generated by an irreducible
monic polynomial $P$ (because of the Euclidean algorithm
in $k[x_n]$). Then
$k' = k[x_n]/\mathfrak p$ is a finite field extension of $k$
and contained in $\kappa(\mathfrak m)$. In this case
we get a surjection
$$
k'[x_1, \ldots, x_{n-1}]
\to
k'[x_1, \ldots, x_n] =
k' \otimes_k k[x_1, \ldots, x_n]
\longrightarrow
\kappa(\mathfrak m)
$$
and hence we see that $\kappa(\mathfrak m)$ is a finite
extension  of $k'$ by induction hypothesis. Thus $\kappa(\mathfrak m)$
is finite over $k$ as well.

\medskip\noindent
If $\mathfrak p = (0)$ we consider the ring
extension $k[x_n] \subset k[x_1, \ldots, x_n]/\mathfrak m$.
This is a finitely generated ring extension, hence
of finite presentation by
Lemmas \ref{lemma-obvious-Noetherian} and
\ref{lemma-Noetherian-finite-type-is-finite-presentation}.
Thus the image of $\Spec(k[x_1, \ldots, x_n]/\mathfrak m)$
in $\Spec(k[x_n])$ is constructible by
Theorem \ref{theorem-chevalley}. Since the image
contains $(0)$ we conclude that it contains a standard
open $D(f)$ for some $f\in k[x_n]$ nonzero. Since clearly
$D(f)$ is infinite we get a contradiction with the
assumption that $k[x_1, \ldots, x_n]/\mathfrak m$ is
a field (and hence has a spectrum consisting of one point).

\medskip\noindent
Proof of (\ref{item-polynomial-ring-Jacobson}). Let
$I \subset R$ be a radical ideal, with $R$ of finite type over $k$.
Let $f \in R$, $f \not \in I$. We have to find a maximal ideal
$\mathfrak m \subset R$ with $I \subset \mathfrak m$ and
$f \not \in \mathfrak m$. The ring $(R/I)_f$ is nonzero, since
$1 = 0$ in this ring would mean $f^n \in I$ and since $I$ is
radical this would mean $f \in I$ contrary to our assumption on $f$.
Thus we may choose a maximal ideal $\mathfrak m'$
in $(R/I)_f$, see Lemma \ref{lemma-Zariski-topology}.
Let $\mathfrak m \subset R$
be the inverse image of $\mathfrak m'$ in $R$. We see that
$I \subset \mathfrak m$
and $f \not \in \mathfrak m$. If we show that $\mathfrak m$ is a maximal
ideal of $R$, then we are done. We clearly have
$$
k \subset R/\mathfrak m \subset \kappa(\mathfrak m').
$$
By part (\ref{item-finite-kappa}) the field extension
$\kappa(\mathfrak m')/k$ is finite. Hence
$R/\mathfrak m$ is a field by Fields, Lemma
\ref{fields-lemma-subalgebra-algebraic-extension-field}.
Thus $\mathfrak m$ is maximal and the proof is complete.
\end{proof}
```

Français restauré :
```tex
\begin{theorem}[Nullstellensatz de Hilbert]
\label{theorem-nullstellensatz}
Soit $k$ un corps.
\begin{enumerate}
\item
\label{item-finite-kappa}
Pour tout idéal maximal $\mathfrak m \subset k[x_1, \ldots, x_n]$,
l'extension de corps $\kappa(\mathfrak m)/k$ est finie.
\item
\label{item-polynomial-ring-Jacobson}
Tout idéal radical $I \subset k[x_1, \ldots, x_n]$
est l'intersection des idéaux maximaux qui le contiennent.
\end{enumerate}
Il en va de même dans toute $k$-algèbre de type fini.
\end{theorem}

\begin{proof}
Il suffit de démontrer la partie (\ref{item-finite-kappa}) du
théorème dans le cas d'une algèbre polynomiale
$k[x_1, \ldots, x_n]$, car toute $k$-algèbre de type fini
est un quotient d'une telle algèbre polynomiale.
Nous le démontrons par récurrence sur $n$. Le cas $n = 0$ est clair.
Supposons que $\mathfrak m$ soit un idéal maximal de $k[x_1, \ldots, x_n]$.
Soit $\mathfrak p \subset k[x_n]$ l'intersection
de $\mathfrak m$ avec $k[x_n]$.

\medskip\noindent
Si $\mathfrak p \not = (0)$,
alors $\mathfrak p$ est maximal et engendré par un polynôme
irréductible unitaire $P$ (grâce à l'algorithme d'Euclide
dans $k[x_n]$). Alors
$k' = k[x_n]/\mathfrak p$ est une extension finie de $k$
et est contenu dans $\kappa(\mathfrak m)$. Dans ce cas,
nous obtenons une surjection
$$
k'[x_1, \ldots, x_{n-1}]
\to
k'[x_1, \ldots, x_n] =
k' \otimes_k k[x_1, \ldots, x_n]
\longrightarrow
\kappa(\mathfrak m)
$$
et nous voyons donc que $\kappa(\mathfrak m)$ est une extension finie
de $k'$ par l'hypothèse de récurrence. Ainsi, $\kappa(\mathfrak m)$
est également finie sur $k$.

\medskip\noindent
Si $\mathfrak p = (0)$, nous considérons l'extension d'anneaux
$k[x_n] \subset k[x_1, \ldots, x_n]/\mathfrak m$.
Cette extension d'anneaux est de type fini, donc
de présentation finie d'après les
lemmes \ref{lemma-obvious-Noetherian} et
\ref{lemma-Noetherian-finite-type-is-finite-presentation}.
Ainsi, l'image de $\Spec(k[x_1, \ldots, x_n]/\mathfrak m)$
dans $\Spec(k[x_n])$ est constructible d'après le
théorème \ref{theorem-chevalley}. Puisque l'image
contient $(0)$, nous concluons qu'elle contient un ouvert
principal $D(f)$ pour un certain $f\in k[x_n]$ non nul. Comme
$D(f)$ est manifestement infini, nous obtenons une contradiction avec
l'hypothèse que $k[x_1, \ldots, x_n]/\mathfrak m$ est
un corps (et a donc un spectre constitué d'un seul point).

\medskip\noindent
Démonstration de (\ref{item-polynomial-ring-Jacobson}). Soit
$I \subset R$ un idéal radical, où $R$ est de type fini sur $k$.
Soit $f \in R$, $f \not \in I$. Nous devons trouver un idéal maximal
$\mathfrak m \subset R$ tel que $I \subset \mathfrak m$ et
$f \not \in \mathfrak m$. L'anneau $(R/I)_f$ est non nul, car
$1 = 0$ dans cet anneau signifierait que $f^n \in I$ et, puisque $I$ est
radical, cela signifierait que $f \in I$, contrairement à notre hypothèse sur $f$.
Nous pouvons donc choisir un idéal maximal $\mathfrak m'$
de $(R/I)_f$, voir le lemme \ref{lemma-Zariski-topology}.
Soit $\mathfrak m \subset R$
l'image réciproque de $\mathfrak m'$ dans $R$. Nous voyons que
$I \subset \mathfrak m$
et $f \not \in \mathfrak m$. Si nous montrons que $\mathfrak m$ est un idéal
maximal de $R$, alors nous avons terminé. Nous avons manifestement
$$
k \subset R/\mathfrak m \subset \kappa(\mathfrak m').
$$
D'après la partie (\ref{item-finite-kappa}), l'extension de corps
$\kappa(\mathfrak m')/k$ est finie. Ainsi,
$R/\mathfrak m$ est un corps d'après Corps, lemme
\ref{fields-lemma-subalgebra-algebraic-extension-field}.
Par conséquent, $\mathfrak m$ est maximal, ce qui achève la démonstration.
\end{proof}
```

</details>

### 26 — lemma-field-finite-type-over-domain

Anglais L6610–6648 ; français L6590–6628.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6610) · FR-ALGEBRA-B9-CHOICE-0026.

L'inclusion R dans le corps K implique que R est intègre ; elle n'est pas remplacée par un morphisme quelconque. Le type fini porte sur K comme R-algèbre, puis sur K comme Rf-algèbre. Le choix d'un ouvert principal réduit au point générique donne un anneau intègre de spectre singleton, donc un corps. L'extension finale est finie par le Nullstellensatz, non supposée finie dès le départ.

Règles : FR-ALGEBRA-B9-RULE-FINITE, FR-ALGEBRA-B9-RULE-NULLSTELLENSATZ, FR-ALGEBRA-B9-RULE-LOGIQUE.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-field-finite-type-over-domain}
Let $R$ be a ring. Let $K$ be a field.
If $R \subset K$ and $K$ is of finite type over $R$,
then there exists an $f \in R$ such that $R_f$ is a field,
and $K/R_f$ is a finite field extension.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-characterize-image-finite-type} there
exist a nonempty open $U \subset \Spec(R)$
contained in the image $\{(0)\}$ of $\Spec(K) \to \Spec(R)$.
Choose $f \in R$, $f \not = 0$ such that $D(f) \subset U$, i.e.,
$D(f) = \{(0)\}$. Then $R_f$ is a domain whose spectrum has exactly one
point and $R_f$ is a field. Then $K$ is a finitely generated algebra
over the field $R_f$ and hence a finite field extension of
$R_f$ by the Hilbert Nullstellensatz (Theorem \ref{theorem-nullstellensatz}).
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-field-finite-type-over-domain}
Soit $R$ un anneau. Soit $K$ un corps.
Si $R \subset K$ et si $K$ est de type fini sur $R$,
alors il existe un $f \in R$ tel que $R_f$ soit un corps
et que $K/R_f$ soit une extension finie de corps.
\end{lemma}

\begin{proof}
D'après le lemme \ref{lemma-characterize-image-finite-type}, il
existe un ouvert non vide $U \subset \Spec(R)$
contenu dans l'image $\{(0)\}$ de $\Spec(K) \to \Spec(R)$.
Choisissons $f \in R$, $f \not = 0$, tel que $D(f) \subset U$, c'est-à-dire
$D(f) = \{(0)\}$. Alors $R_f$ est un anneau intègre dont le spectre a exactement un
point, et $R_f$ est un corps. Ensuite, $K$ est une algèbre de type fini
sur le corps $R_f$, donc une extension finie de
$R_f$ d'après le Nullstellensatz de Hilbert (théorème \ref{theorem-nullstellensatz}).
\end{proof}
```

</details>

## Observations extérieures au texte traduit

### FR-ALGEBRA-B9-SOURCE-NOTE-0001

[Source L6010](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6010) — lemma-Noetherian-permanence.

```tex
defined as the ideal of elements of $R$ which occur as leading
coefficients of degree $d$ polynomials in $J_i$.
```

Au sens strict, le coefficient dominant d'un polynôme de degré exactement d n'est pas zéro. Pour obtenir l'idéal annoncé, il faut y inclure zéro ou considérer les coefficients de X^d des polynômes de degré au plus d. La preuve utilise cette convention usuelle. On signale le raccourci, sans conclure que le théorème est faux et sans modifier le témoin.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

### FR-ALGEBRA-B9-SOURCE-NOTE-0002

[Source L6257](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6257) — example-locally-nilpotent-not-nilpotent.

```tex
the elements $x_n^n$ for $n \in \mathbf{N}$ and $S = R/I$.
```

Si N commence à zéro, le générateur x0^0 vaut 1, donc I=R et S=0 ; J n'est alors pas un exemple d'idéal non nilpotent. Avec n≥1, pour chaque r≥1 la classe de x(r+1)^r est non nulle et l'exemple fonctionne. Cette observation reste conditionnelle : aucune convention globale excluant ou incluant zéro n'a été établie dans ce lot. Dat p.7 présente une écriture similaire, ce qui n'est pas une preuve de convention. Aucun indice n'est modifié.

Confiance éditoriale : modérée, conditionnelle à une convention non établie ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

### FR-ALGEBRA-B9-SOURCE-NOTE-0003

[Source L6475](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L6475) — lemma-invert-closed-quotient.

```tex
Since $S^{-1}I = 0$ we see also the second map is injective.
Hence $S^{-1}R \cong R/I$.
```

L'existence de deux injections en sens opposés ne suffit pas à elle seule pour deux anneaux arbitraires. Ici les applications construites sont les applications canoniques : elles envoient r modulo I vers r/1 et r/s vers (r modulo I)(s modulo I)^−1. Les deux composées sont donc les identités. C'est un complément au raisonnement condensé, pas un contre-exemple au résultat, et il reste dans cette note extérieure.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

## Contrôles et suite

Les 459 régions mathématiques du lot sont égales après deux exceptions exactes traduisant h.o.t. et h.o.t par termes d’ordre supérieur. Le préfixe comporte 4 816 régions et dix-huit exceptions linguistiques exactes. Sans ces exceptions la comparaison brute est fausse ; aucun masque général des formules n’est employé.

Le titre du théorème et les deux titres de preuve sont vérifiés séparément. Labels, références, contrôles TeX, environnements et items concordent. L’ensemble des régions mathématiques du fichier français demeure inchangé par rapport au lot 8. Les opérations inverses restituent exactement ce lot puis le témoin public antérieur, qui reste préservé.

Les 227 paires couvrent le préfixe sans lacune ni chevauchement ; les octets antérieurs au lot et ceux du suffixe non relu sont inchangés. La validation structurelle complète la lecture sémantique, elle ne la remplace pas.

Prochaine lecture : Anneaux de Jacobson, anglais L6649 / français L6629. Aucun nouveau PDF ni nouvelle publication, aucune certification globale du chapitre ou de l’édition.

