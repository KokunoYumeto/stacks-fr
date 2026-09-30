# Algèbres géométriquement réduites et corps parfaits

## Résultat et portée

Trois sections entièrement comparées : anglais L10037–10603 (567 lignes) et français L9993–10558 (566 lignes). Les 22 paires comprennent tous les énoncés, preuves et transitions. 225 occurrences sont reliées à des règles contextualisées. Le préfixe atteint 45 sections, 374 paires et 3010 occurrences. Le chapitre et l’édition restent inachevés.

Neuf réparations propres au français : une conclusion omise, la portée de not all, la préposition de l’adjonction de racines, quatre occurrences de anneau intègre et deux accords. Aucune formule ni référence ne change. Aucune correction proposée de l’anglais n’est incorporée.

Trois observations extérieures à la traduction signalent une somme manquante, un indice indéfini et une convention de caractéristique non explicitée. Ce ne sont ni trois errata nouvellement admis ni trois théorèmes réfutés ; la dernière observation reste conditionnelle.

Lecture, réparations et dossier produits par OpenAI Codex — GPT-6 Astra, Ultra effort ; comparaison assistée par IA, sans relecture humaine. Les attestations sont rétrospectives et limitées aux passages effectivement lus ; leur absence pour certains syntagmes est indiquée.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch14.fr.tex) · [État français précédent](staged/fr/010_algebra.prose-batch13.fr.tex) · [Lot précédent](ALGEBRA_PROSE_BATCH13_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH14_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH14_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH14_OCCURRENCES.json) · [Avant/après](ALGEBRA_PROSE_BATCH14_REPAIRS.json) · [Exceptions linguistiques en formule](ALGEBRA_PROSE_BATCH14_MATH_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH14_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH14_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Antoine Ducros — Introduction à la théorie des schémas

[Source consultée](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages 23, 103–105 entièrement lues : 0.1.3, 2.6.7–10. Pages 11 et 238 également lues comme contexte, sans attestation spécifique revendiquée pour géométriquement réduit.

Attestations courtes : « anneau intègre », « partie multiplicative », « produit tensoriel », « colimites ».

Le domaine de la source est l'anneau intègre non nul de 0.1.3. Le produit tensoriel et sa compatibilité avec localisation sont décrits au 2.6.7 ; 2.6.8.3 distingue réduction et comportement après extension de corps.

Limites : Quelques barres et signes sont perdus à l'extraction : aucune formule du cours n'est recopiée pour remplacer Stacks. Les lexèmes et leurs définitions explicites sont utilisés. Consultation rétrospective.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

### Jean-François Dat — Algèbre ENS 2016–2017

[Source consultée](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/AlgebreM1/ENS1617.pdf) · [Fichier conservé](canon-consulted/fr-algebra/dat-algebre-ens1617.pdf)

Pages 117–119 entièrement lues, notamment 2.6.1–3.

Attestations courtes : « Corps parfaits et imparfaits », « endomorphisme de Frobenius », « extensions purement inséparables ».

Atteste parfait, purement inséparable et le critère de Frobenius. Le contexte d'adjonction de racines permet de distinguer les éléments de k et ceux de l'extension.

Limites : La définition donnée par les extensions algébriques n'est pas substituée à toutes les extensions dans Stacks. Des ligatures sont mal extraites ; aucun exemple ni argument de cette page n'est copié comme correction du texte officiel.

SHA-256 : DB5B7FD8139D62C37D0DDDDC90EF22D3EDCF74CC663C5267815E4EA3CECBBB18.

### Patrick Polo — Différentielles lissité et séparabilité

[Source consultée](https://webusers.imj-prg.fr/~patrick.polo/M2/GA05ch4.pdf) · [Fichier conservé](canon-consulted/fr-algebra/polo-ga05ch4.pdf)

Pages PDF 9, 10, 12, 13, imprimées 77, 78, 80, 81, entièrement lues ; définitions 13.16 et 13.21.

Attestations courtes : « séparablement engendrée », « base de transcendance séparante », « corps parfait ».

Atteste les deux expressions de séparabilité avec la bonne définition, et le critère des corps parfaits. L'accord engendrée se rapporte chez Polo à extension, non au nom corps.

Limites : Le raisonnement de 13.22 contient des lapsus apparents, dont indépendants au lieu de dépendants ; il n'est pas utilisé pour corriger les preuves de Stacks. La formulation générale de séparable reste celle de Stacks.

SHA-256 : 3725CE2E3725B96E259F7FE6F67482E372E1841F0543C67B6A63295475133B53.

### Patrick Polo — Schémas en groupes géométriquement réduits

[Source consultée](https://webusers.imj-prg.fr/~patrick.polo/5MF32/ch3M2-29fev16.pdf) · [Fichier conservé](canon-consulted/fr-algebra/polo-ch3M2-29fev16.pdf)

Pages PDF/imprimées 9–10 entièrement lues ; définition 2.15 et proposition 2.16. Page 9 rendue avec Poppler et inspectée : barres de clôture algébrique vérifiées visuellement.

Attestations courtes : « géométriquement réduite », « élément nilpotent », « corps non parfait ».

Atteste le terme pour une algèbre et distingue sa réduction de celle après extension à une clôture algébrique.

Limites : Le critère par une clôture algébrique et les résultats de type fini de ce cours ne remplacent pas les quantificateurs généraux de Stacks. Citation lexicale courte ; pas de preuve reproduite. Consultation rétrospective.

SHA-256 : 61C1B32D5F7F7FFB239B048D0DBB30E44345AF5B0A1A3441ADC6EB9D0634AF22.

## Les neuf réparations françaises

### FR-ALGEBRA-B14-REPAIR-0001

Anglais L10067 ; français L10023.

Avant :
```tex
Si $S$ est géométriquement réduite sur $k$, toute
$k$-sous-algèbre.
```

Après :
```tex
Si $S$ est géométriquement réduite sur $k$, toute
$k$-sous-algèbre l'est aussi.
```

Réparation d'une omission propre au français : sans l'est aussi, la première assertion est inachevée et sa conclusion n'est pas énoncée. Aucune correction de l'anglais.

### FR-ALGEBRA-B14-REPAIR-0002

Anglais L10169 ; français L10125.

Avant :
```tex
Nous pouvons donc en fait supposer que $S$ est un domaine.
```

Après :
```tex
Nous pouvons donc en fait supposer que $S$ est un anneau intègre.
```

Anneau intègre est préféré à domaine, calque équivoque, sur attestation de Ducros. Les trois occurrences sont vérifiées individuellement dans leurs contextes ; la non-nullité fait partie de la notion, pas d'une nouvelle hypothèse.

### FR-ALGEBRA-B14-REPAIR-0003

Anglais L10175 ; français L10131.

Avant :
```tex
$k[x_1, \ldots, x_r] \otimes_k S = S[x_1, \ldots, x_r]$ est un domaine.
```

Après :
```tex
$k[x_1, \ldots, x_r] \otimes_k S = S[x_1, \ldots, x_r]$ est un anneau intègre.
```

Anneau intègre est préféré à domaine, calque équivoque, sur attestation de Ducros. Les trois occurrences sont vérifiées individuellement dans leurs contextes ; la non-nullité fait partie de la notion, pas d'une nouvelle hypothèse.

### FR-ALGEBRA-B14-REPAIR-0004

Anglais L10176 ; français L10132.

Avant :
```tex
Il s'ensuit que $k(x_1, \ldots, x_r) \otimes_k S$ est un domaine,
```

Après :
```tex
Il s'ensuit que $k(x_1, \ldots, x_r) \otimes_k S$ est un anneau intègre,
```

Anneau intègre est préféré à domaine, calque équivoque, sur attestation de Ducros. Les trois occurrences sont vérifiées individuellement dans leurs contextes ; la non-nullité fait partie de la notion, pas d'une nouvelle hypothèse.

### FR-ALGEBRA-B14-REPAIR-0005

Anglais L10318 ; français L10274.

Avant :
```tex
Nous affirmons que, pour un certain $i$, toutes les puissances de $X_i$
qui apparaissent dans $F$ ne sont pas multiples de $p$.
```

Après :
```tex
Nous affirmons que, pour un certain $i$, les puissances de $X_i$
qui apparaissent dans $F$ ne sont pas toutes multiples de $p$.
```

La portée de la négation est rendue explicite ; not all n'est pas none. Adjoindre à k ne suppose pas que les racines soient déjà dans k. Ces deux réparations françaises n'altèrent aucune formule.

### FR-ALGEBRA-B14-REPAIR-0006

Anglais L10355 ; français L10313.

Avant :
```tex
en adjoignant les racines $p$-ièmes de tous les éléments de $k$
dans $k$.
```

Après :
```tex
en adjoignant les racines $p$-ièmes de tous les éléments de $k$
à $k$.
```

La portée de la négation est rendue explicite ; not all n'est pas none. Adjoindre à k ne suppose pas que les racines soient déjà dans k. Ces deux réparations françaises n'altèrent aucune formule.

### FR-ALGEBRA-B14-REPAIR-0007

Anglais L10394 ; français L10354.

Avant :
```tex
et nous devons montrer que $K$ est séparablement
engendrée sur $k$.
```

Après :
```tex
et nous devons montrer que $K$ est séparablement
engendré sur $k$.
```

Accord grammatical réparé pour K. L'indice n de la source n'est pas normalisé vers d dans la traduction ; la proposition de correction est séparée.

### FR-ALGEBRA-B14-REPAIR-0008

Anglais L10537 ; français L10496.

Avant :
```tex
L'anneau $(k' \otimes_k K)_{red}$ est un domaine, car pour un certain
```

Après :
```tex
L'anneau $(k' \otimes_k K)_{red}$ est un anneau intègre, car pour un certain
```

Le quatrième domaine du lot devient anneau intègre. Compositum est conservé source-guidé ; pas d'attestation nouvelle prétendue dans les pages lues.

### FR-ALGEBRA-B14-REPAIR-0009

Anglais L10550 ; français L10509.

Avant :
```tex
$k'/k$ telle que $k'$ soit parfaite.
```

Après :
```tex
$k'/k$ telle que $k'$ soit parfait.
```

k′ est le corps qui est parfait, non l'extension qui serait parfaite. L'unicité et les flèches restent celles de l'auteur.

## Règles contextualisées

### FR-ALGEBRA-B14-RULE-GEO

Le qualificatif porte sur toutes les extensions dans la définition source ; ne pas confondre avec réduit seul.

Canon : FR-ALGEBRA-B14-CANON-POLOGEO.

### FR-ALGEBRA-B14-RULE-RED

Réduit exclut les nilpotents non nuls ; l'accord suit anneau, corps ou algèbre selon le contexte.

Canon : FR-ALGEBRA-B14-CANON-POLOGEO, FR-ALGEBRA-B14-CANON-DUCROS.

### FR-ALGEBRA-B14-RULE-DOMAIN

Intègre désigne un anneau non nul sans diviseurs de zéro ; les quatre occurrences réparées ont le sens anglais domain.

Canon : FR-ALGEBRA-B14-CANON-DUCROS.

### FR-ALGEBRA-B14-RULE-SEP

Distinguer algébrique séparable, séparablement engendrée et la notion générale de Stacks ; les hypothèses ne sont pas échangées.

Canon : FR-ALGEBRA-B14-CANON-POLO, FR-ALGEBRA-B14-CANON-DATALG.

### FR-ALGEBRA-B14-RULE-PURE

Purement inséparable concerne les éléments algébriques dont une puissance p^n appartient au corps de base.

Canon : FR-ALGEBRA-B14-CANON-DATALG.

### FR-ALGEBRA-B14-RULE-PERF

Parfait pour un corps est attesté ; clôture parfaite reste ici source-guidée faute de lecture externe complète de ce syntagme.

Canon : FR-ALGEBRA-B14-CANON-DATALG, FR-ALGEBRA-B14-CANON-POLO.

### FR-ALGEBRA-B14-RULE-TRANS

Une base séparante impose l'extension algébrique séparable sur le corps rationnel correspondant.

Canon : FR-ALGEBRA-B14-CANON-POLO.

### FR-ALGEBRA-B14-RULE-LOC

Localisation par une partie multiplicative ; ne pas traduire par quotient ni supposer l'inversibilité préalable.

Canon : FR-ALGEBRA-B14-CANON-DUCROS.

### FR-ALGEBRA-B14-RULE-TENSOR

Les compatibilités employées sont celles du texte, sans remplacer une injection vers un produit infini par une égalité.

Canon : FR-ALGEBRA-B14-CANON-DUCROS.

### FR-ALGEBRA-B14-RULE-GEN

Type fini comme algèbre ou extension de corps n'est pas finitude vectorielle ; chaque occurrence est relue dans le passage complet.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B14-RULE-LOGIC

Portée des quantificateurs et de la négation contrôlée directement sur l'anglais, sans prétendre qu'une attestation lexicale prouve la logique.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

## Passages parallèles complets

### 01 — section-geometrically-reduced

Anglais L10037–10044 ; français L9993–10000.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10037) · FR-ALGEBRA-B14-CHOICE-0001.

Le titre reprend algèbres géométriquement réduites, attesté par Polo 2.15. La suggestion de sauter au lemme principal reste une suggestion de lecture, pas une suppression des lemmes intermédiaires.

Règles : FR-ALGEBRA-B14-RULE-GEO, FR-ALGEBRA-B14-RULE-RED.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Geometrically reduced algebras}
\label{section-geometrically-reduced}

\noindent
The main result on geometrically reduced algebras is
Lemma \ref{lemma-geometrically-reduced-finite-purely-inseparable-extension}.
We suggest the reader skip to the lemma after reading the definition.
```

Français restauré :
```tex
\section{Algèbres géométriquement réduites}
\label{section-geometrically-reduced}

\noindent
Le résultat principal sur les algèbres géométriquement réduites est le
Lemme \ref{lemma-geometrically-reduced-finite-purely-inseparable-extension}.
Nous suggérons au lecteur de passer directement à ce lemme après avoir lu la définition.
```

</details>

### 02 — definition-geometrically-reduced

Anglais L10045–10061 ; français L10001–10017.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10045) · FR-ALGEBRA-B14-CHOICE-0002.

Le quantificateur porte sur toute extension de corps K/k. Le français conserve cette définition avant les critères équivalents annoncés. Polo 2.15 atteste le terme en prenant une clôture algébrique ; cette variante ne remplace pas la définition de Stacks. Le féminin renvoie à algèbre. Les deux critères annoncés et le renvoi prospectif sont présents.

Règles : FR-ALGEBRA-B14-RULE-GEO, FR-ALGEBRA-B14-RULE-RED, FR-ALGEBRA-B14-RULE-PURE, FR-ALGEBRA-B14-RULE-GEN, FR-ALGEBRA-B14-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-geometrically-reduced}
Let $k$ be a field. Let $S$ be a $k$-algebra.
We say $S$ is {\it geometrically reduced over $k$}
if for every field extension $K/k$ the
$K$-algebra $K \otimes_k S$ is reduced.
\end{definition}

\noindent
Let $k$ be a field and let $S$ be a reduced $k$-algebra.
To check that $S$ is geometrically reduced it will suffice
to check that $\overline{k} \otimes_k S$ is reduced (where
$\overline{k}$ denotes the algebraic closure of $k$).
In fact it is enough to check this for finite purely inseparable
field extensions $k'/k$. See
Lemma \ref{lemma-geometrically-reduced-finite-purely-inseparable-extension}.
```

Français restauré :
```tex
\begin{definition}
\label{definition-geometrically-reduced}
Soit $k$ un corps. Soit $S$ une $k$-algèbre.
On dit que $S$ est {\it géométriquement réduite sur $k$}
si, pour toute extension de corps $K/k$, la
$K$-algèbre $K \otimes_k S$ est réduite.
\end{definition}

\noindent
Soient $k$ un corps et $S$ une $k$-algèbre réduite.
Pour vérifier que $S$ est géométriquement réduite, il suffit
de vérifier que $\overline{k} \otimes_k S$ est réduite (où
$\overline{k}$ désigne la clôture algébrique de $k$).
En fait, il suffit de le vérifier pour les extensions de corps finies
purement inséparables $k'/k$. Voir le
Lemme \ref{lemma-geometrically-reduced-finite-purely-inseparable-extension}.
```

</details>

### 03 — lemma-subalgebra-separable

Anglais L10062–10082 ; français L10018–10038.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10062) · FR-ALGEBRA-B14-CHOICE-0003.

La première assertion française avait perdu sa conclusion : toute sous-algèbre l'est aussi restitue so is every k-subalgebra. Les quatre propriétés, y compris colimite filtrante et localisation, sont conservées. La deuxième ne suppose pas que S soit de type fini : elle porte sur toutes ses sous-algèbres de type fini. La preuve reste explicitement omise avec la même indication tensorielle.

Point particulier à relire : Réparation d'une omission propre au français : sans l'est aussi, la première assertion est inachevée et sa conclusion n'est pas énoncée. Aucune correction de l'anglais.

Règles : FR-ALGEBRA-B14-RULE-GEO, FR-ALGEBRA-B14-RULE-RED, FR-ALGEBRA-B14-RULE-LOC, FR-ALGEBRA-B14-RULE-TENSOR, FR-ALGEBRA-B14-RULE-GEN, FR-ALGEBRA-B14-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-subalgebra-separable}
Elementary properties of geometrically reduced algebras.
Let $k$ be a field. Let $S$ be a $k$-algebra.
\begin{enumerate}
\item If $S$ is geometrically reduced over $k$ so is every
$k$-subalgebra.
\item If all finitely generated $k$-subalgebras of $S$ are
geometrically reduced, then $S$ is geometrically reduced.
\item A directed colimit of geometrically reduced $k$-algebras
is geometrically reduced.
\item If $S$ is geometrically reduced over $k$, then any localization
of $S$ is geometrically reduced over $k$.
\end{enumerate}
\end{lemma}

\begin{proof}
Omitted. The second and third property follow from the fact that
tensor product commutes with colimits.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-subalgebra-separable}
Propriétés élémentaires des algèbres géométriquement réduites.
Soit $k$ un corps. Soit $S$ une $k$-algèbre.
\begin{enumerate}
\item Si $S$ est géométriquement réduite sur $k$, toute
$k$-sous-algèbre l'est aussi.
\item Si toutes les $k$-sous-algèbres de type fini de $S$ sont
géométriquement réduites, alors $S$ est géométriquement réduite.
\item Une colimite filtrante de $k$-algèbres géométriquement réduites
est géométriquement réduite.
\item Si $S$ est géométriquement réduite sur $k$, toute localisation
de $S$ est géométriquement réduite sur $k$.
\end{enumerate}
\end{lemma}

\begin{proof}
Omis. Les deuxième et troisième propriétés résultent du fait que
le produit tensoriel commute aux colimites.
\end{proof}
```

</details>

### 04 — lemma-geometrically-reduced-permanence

Anglais L10083–10104 ; français L10039–10060.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10083) · FR-ALGEBRA-B14-CHOICE-0004.

Partie multiplicative et localisation désignent les mêmes objets que multiplicative subset et localization ; Ducros 2.6.7.2 emploie ces termes ensemble. La stabilité pour R[x] reste séparée de celle pour S^{-1}R. La transition vers les lemmes suivants conserve l'injectivité simultanée pour deux inclusions de k-algèbres ; le fait que k est un corps n'est pas supprimé.

Règles : FR-ALGEBRA-B14-RULE-GEO, FR-ALGEBRA-B14-RULE-RED, FR-ALGEBRA-B14-RULE-LOC, FR-ALGEBRA-B14-RULE-TENSOR.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-geometrically-reduced-permanence}
Let $k$ be a field.
If $R$ is geometrically reduced over $k$,
and $S \subset R$ is a multiplicative subset, then the localization
$S^{-1}R$ is geometrically reduced over $k$.
If $R$ is geometrically reduced over $k$, then $R[x]$ is geometrically
reduced over $k$.
\end{lemma}

\begin{proof}
Omitted. Hints: A localization of a reduced ring is reduced, and
localization commutes with tensor products.
\end{proof}

\noindent
In the proofs of the following lemmas we will repeatedly use
the following observation: Suppose that $R' \subset R$ and
$S' \subset S$ are inclusions of $k$-algebras.
Then the map $R' \otimes_k S' \to R \otimes_k S$
is injective.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-geometrically-reduced-permanence}
Soit $k$ un corps.
Si $R$ est géométriquement réduite sur $k$
et si $S \subset R$ est une partie multiplicative, alors la localisation
$S^{-1}R$ est géométriquement réduite sur $k$.
Si $R$ est géométriquement réduite sur $k$, alors $R[x]$ est
géométriquement réduite sur $k$.
\end{lemma}

\begin{proof}
Omis. Indications : une localisation d'un anneau réduit est réduite,
et la localisation commute aux produits tensoriels.
\end{proof}

\noindent
Dans les preuves des lemmes suivants, nous utiliserons à plusieurs reprises
l'observation suivante : supposons que $R' \subset R$ et
$S' \subset S$ soient des inclusions de $k$-algèbres.
Alors l'application $R' \otimes_k S' \to R \otimes_k S$
est injective.
```

</details>

### 05 — lemma-limit-argument

Anglais L10105–10128 ; français L10061–10084.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10105) · FR-ALGEBRA-B14-CHOICE-0005.

Non réduit, diviseur de zéro non nul et idempotent non trivial restent trois défauts distincts. Les témoins sont des sous-algèbres de type fini des deux facteurs, non des quotients. La preuve par écriture tensorielle finie et la phrase de renvoi pour les deux autres cas restent aussi abrégées que l'original. Aucun développement nouveau n'est ajouté à cette traduction fidèle.

Règles : FR-ALGEBRA-B14-RULE-RED, FR-ALGEBRA-B14-RULE-GEN, FR-ALGEBRA-B14-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-limit-argument}
Let $k$ be a field. Let $R$, $S$ be $k$-algebras.
\begin{enumerate}
\item If $R \otimes_k S$ is nonreduced, then there exist
finitely generated subalgebras $R' \subset R$,
$S' \subset S$ such that $R' \otimes_k S'$ is not reduced.
\item If $R \otimes_k S$ contains a nonzero zerodivisor, then there exist
finitely generated subalgebras $R' \subset R$,
$S' \subset S$ such that $R' \otimes_k S'$ contains a nonzero zerodivisor.
\item If $R \otimes_k S$ contains a nontrivial idempotent, then there exist
finitely generated subalgebras $R' \subset R$,
$S' \subset S$ such that $R' \otimes_k S'$ contains a nontrivial idempotent.
\end{enumerate}
\end{lemma}

\begin{proof}
Suppose $z \in R \otimes_k S$ is nilpotent. We may write
$z = \sum_{i = 1, \ldots, n} x_i \otimes y_i$.
Thus we may take $R'$ the $k$-subalgebra generated by
the $x_i$ and $S'$ the $k$-subalgebra generated by the $y_i$.
The second and third statements are proved in the same way.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-limit-argument}
Soit $k$ un corps. Soient $R$ et $S$ des $k$-algèbres.
\begin{enumerate}
\item Si $R \otimes_k S$ n'est pas réduit, il existe des
sous-algèbres de type fini $R' \subset R$ et
$S' \subset S$ telles que $R' \otimes_k S'$ ne soit pas réduit.
\item Si $R \otimes_k S$ contient un diviseur de zéro non nul, il existe des
sous-algèbres de type fini $R' \subset R$ et
$S' \subset S$ telles que $R' \otimes_k S'$ contienne un diviseur de zéro non nul.
\item Si $R \otimes_k S$ contient un idempotent non trivial, il existe des
sous-algèbres de type fini $R' \subset R$ et
$S' \subset S$ telles que $R' \otimes_k S'$ contienne un idempotent non trivial.
\end{enumerate}
\end{lemma}

\begin{proof}
Supposons que $z \in R \otimes_k S$ soit nilpotent. On peut écrire
$z = \sum_{i = 1, \ldots, n} x_i \otimes y_i$.
On peut donc prendre pour $R'$ la $k$-sous-algèbre engendrée par
les $x_i$, et pour $S'$ la $k$-sous-algèbre engendrée par les $y_i$.
Les deuxième et troisième assertions se démontrent de la même manière.
\end{proof}
```

</details>

### 06 — lemma-geometrically-reduced-any-reduced-base-change

Anglais L10129–10150 ; français L10085–10106.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10129) · FR-ALGEBRA-B14-CHOICE-0006.

S est géométriquement réduite, R seulement réduite et quelconque. On ne remplace pas ces hypothèses par une assertion fausse sur deux algèbres simplement réduites sur un corps quelconque. La réduction au type fini, l'injection dans un produit fini de corps et les trois renvois sont conservés. Ducros 2.6.8.3 explique concrètement pourquoi réduit et géométriquement réduit ne doivent pas être confondus.

Règles : FR-ALGEBRA-B14-RULE-GEO, FR-ALGEBRA-B14-RULE-RED, FR-ALGEBRA-B14-RULE-GEN.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-geometrically-reduced-any-reduced-base-change}
Let $k$ be a field.
Let $S$ be a geometrically reduced $k$-algebra.
Let $R$ be any reduced $k$-algebra.
Then $R \otimes_k S$ is reduced.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-limit-argument}
we may assume that $R$ is of finite type over $k$.
Then $R$, as a reduced Noetherian ring, embeds into a finite
product of fields
(see Lemmas \ref{lemma-total-ring-fractions-no-embedded-points},
\ref{lemma-Noetherian-irreducible-components}, and
\ref{lemma-minimal-prime-reduced-ring}).
Hence we may assume $R$ is a finite product of
fields. In this case it follows from
Definition \ref{definition-geometrically-reduced}
that $R \otimes_k S$ is reduced.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-geometrically-reduced-any-reduced-base-change}
Soit $k$ un corps.
Soit $S$ une $k$-algèbre géométriquement réduite.
Soit $R$ une $k$-algèbre réduite quelconque.
Alors $R \otimes_k S$ est réduite.
\end{lemma}

\begin{proof}
D'après le Lemme \ref{lemma-limit-argument},
nous pouvons supposer que $R$ est de type fini sur $k$.
Alors, comme anneau réduit noethérien, $R$ se plonge dans un produit
fini de corps
(voir les Lemmes \ref{lemma-total-ring-fractions-no-embedded-points},
\ref{lemma-Noetherian-irreducible-components} et
\ref{lemma-minimal-prime-reduced-ring}).
Nous pouvons donc supposer que $R$ est un produit fini de corps.
Dans ce cas, la
Définition \ref{definition-geometrically-reduced}
montre que $R \otimes_k S$ est réduite.
\end{proof}
```

</details>

### 07 — lemma-separable-extension-preserves-reducedness

Anglais L10151–10195 ; français L10107–10155.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10151) · FR-ALGEBRA-B14-CHOICE-0007.

Les deux cas, extension séparable et extension séparablement engendrée, restent distincts à ce stade de la démonstration. Trois calques domaine deviennent anneau intègre : Ducros 0.1.3 donne exactement la notion non nulle sans diviseur de zéro. Le corps des fractions, le polynôme minimal séparable et la réduction par colimite sont conservés. Type fini sur k qualifie S comme algèbre, K comme extension de corps ; aucune finitude vectorielle de K n'est ajoutée.

Point particulier à relire : Anneau intègre est préféré à domaine, calque équivoque, sur attestation de Ducros. Les trois occurrences sont vérifiées individuellement dans leurs contextes ; la non-nullité fait partie de la notion, pas d'une nouvelle hypothèse.

Règles : FR-ALGEBRA-B14-RULE-RED, FR-ALGEBRA-B14-RULE-DOMAIN, FR-ALGEBRA-B14-RULE-SEP, FR-ALGEBRA-B14-RULE-TRANS, FR-ALGEBRA-B14-RULE-LOC, FR-ALGEBRA-B14-RULE-TENSOR, FR-ALGEBRA-B14-RULE-GEN, FR-ALGEBRA-B14-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-separable-extension-preserves-reducedness}
Let $k$ be a field.
Let $S$ be a reduced $k$-algebra.
Let $K/k$ be either a separable field extension,
or a separably generated field extension.
Then $K \otimes_k S$ is reduced.
\end{lemma}

\begin{proof}
Assume $k \subset K$ is separable.
By Lemma \ref{lemma-limit-argument}
we may assume that $S$ is of finite type over $k$
and $K$ is finitely generated over $k$.
Then $S$ embeds into a finite product of fields,
namely its total ring of fractions (see
Lemmas \ref{lemma-minimal-prime-reduced-ring} and
\ref{lemma-total-ring-fractions-no-embedded-points}).
Hence we may actually assume that $S$ is a domain.
We choose $x_1, \ldots, x_{r + 1} \in K$ as in
Lemma \ref{lemma-generating-finitely-generated-separable-field-extensions}.
Let $P \in k(x_1, \ldots, x_r)[T]$
be the minimal polynomial of $x_{r + 1}$. It is a separable polynomial.
It is easy to see that
$k[x_1, \ldots, x_r] \otimes_k S = S[x_1, \ldots, x_r]$ is a domain.
This implies $k(x_1, \ldots, x_r) \otimes_k S$ is a domain
as it is a localization of $S[x_1, \ldots, x_r]$.
The ring extension $k(x_1, \ldots, x_r) \otimes_k S \subset K \otimes_k S$
is generated by a single element $x_{r + 1}$ with a single
equation, namely $P$. Hence $K \otimes_k S$ embeds into
$F[T]/(P)$ where $F$ is the fraction field of $k(x_1, \ldots, x_r) \otimes_k S$.
Since $P$ is separable this is a finite product of fields and we win.

\medskip\noindent
At this point we do not yet know that a separably generated field
extension is separable, so we have to prove the lemma in this case also.
To do this suppose that $\{x_i\}_{i \in I}$ is a separating
transcendence basis for $K$ over $k$. For any finite set of elements
$\lambda_j \in K$ there exists a finite subset $T \subset I$ such
that $k(\{x_i\}_{i\in T}) \subset k(\{x_i\}_{i \in T} \cup \{\lambda_j\})$
is finite separable. Hence we see that $K$ is a directed colimit of
finitely generated and separably generated extensions of $k$. Thus
the argument of the preceding paragraph applies to this case as well.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-separable-extension-preserves-reducedness}
Soit $k$ un corps.
Soit $S$ une $k$-algèbre réduite.
Soit $K/k$ une extension de corps séparable
ou une extension de corps séparablement engendrée.
Alors $K \otimes_k S$ est réduite.
\end{lemma}

\begin{proof}
Supposons que $k \subset K$ soit séparable.
D'après le Lemme \ref{lemma-limit-argument},
nous pouvons supposer que $S$ est de type fini sur $k$
et que $K$ est de type fini sur $k$.
Alors $S$ se plonge dans un produit fini de corps,
à savoir son anneau total des fractions (voir les
Lemmes \ref{lemma-minimal-prime-reduced-ring} et
\ref{lemma-total-ring-fractions-no-embedded-points}).
Nous pouvons donc en fait supposer que $S$ est un anneau intègre.
Choisissons $x_1, \ldots, x_{r + 1} \in K$ comme dans le
Lemme \ref{lemma-generating-finitely-generated-separable-field-extensions}.
Soit $P \in k(x_1, \ldots, x_r)[T]$
le polynôme minimal de $x_{r + 1}$. C'est un polynôme séparable.
Il est facile de voir que
$k[x_1, \ldots, x_r] \otimes_k S = S[x_1, \ldots, x_r]$ est un anneau intègre.
Il s'ensuit que $k(x_1, \ldots, x_r) \otimes_k S$ est un anneau intègre,
car c'est une localisation de $S[x_1, \ldots, x_r]$.
L'extension d'anneaux
$k(x_1, \ldots, x_r) \otimes_k S \subset K \otimes_k S$
est engendrée par un seul élément $x_{r + 1}$ qui satisfait une seule
équation, à savoir $P$. Par conséquent, $K \otimes_k S$ se plonge dans
$F[T]/(P)$, où $F$ est le corps des fractions de
$k(x_1, \ldots, x_r) \otimes_k S$.
Comme $P$ est séparable, ceci est un produit fini de corps, et la conclusion s'ensuit.

\medskip\noindent
À ce stade, nous ne savons pas encore qu'une extension de corps
séparablement engendrée est séparable ; il faut donc aussi démontrer
le lemme dans ce cas.
Pour cela, supposons que $\{x_i\}_{i \in I}$ soit une base de
transcendance séparante de $K$ sur $k$. Pour tout ensemble fini
d'éléments $\lambda_j \in K$, il existe un sous-ensemble fini
$T \subset I$ tel que
$k(\{x_i\}_{i\in T}) \subset k(\{x_i\}_{i \in T} \cup \{\lambda_j\})$
soit finie et séparable. Il s'ensuit que $K$ est une colimite filtrante
d'extensions de $k$ de type fini et séparablement engendrées.
L'argument du paragraphe précédent s'applique donc également à ce cas.
\end{proof}
```

</details>

### 08 — lemma-generic-points-geometrically-reduced

Anglais L10196–10219 ; français L10156–10179.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10196) · FR-ALGEBRA-B14-CHOICE-0008.

Les localisations sont prises aux idéaux premiers minimaux, et S est supposée réduite. La deuxième flèche vers le produit des produits tensoriels est seulement dite injective ; on ne prétend pas que tensoriser commute à tout produit infini. Le français conserve l'argument utilisant K libre sur k, ainsi que le test de réduction dans un sous-anneau.

Règles : FR-ALGEBRA-B14-RULE-GEO, FR-ALGEBRA-B14-RULE-RED, FR-ALGEBRA-B14-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-generic-points-geometrically-reduced}
Let $k$ be a field and let $S$ be a $k$-algebra. Assume that
$S$ is reduced and that $S_{\mathfrak p}$ is geometrically
reduced for every minimal prime $\mathfrak p$ of $S$.
Then $S$ is geometrically reduced.
\end{lemma}

\begin{proof}
Since $S$ is reduced the map
$S \to \prod_{\mathfrak p\text{ minimal}} S_{\mathfrak p}$
is injective, see
Lemma \ref{lemma-reduced-ring-sub-product-fields}.
If $K/k$ is a field extension, then the maps
$$
S \otimes_k K \to (\prod S_\mathfrak p) \otimes_k K \to
\prod S_\mathfrak p \otimes_k K
$$
are injective: the first as $k \to K$ is flat and the second by inspection
because $K$ is a free $k$-module. As $S_\mathfrak p$ is geometrically
reduced the ring on the right is reduced. Thus we see that $S \otimes_k K$
is reduced as a subring of a reduced ring.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-generic-points-geometrically-reduced}
Soit $k$ un corps et soit $S$ une $k$-algèbre. Supposons que
$S$ soit réduite et que $S_{\mathfrak p}$ soit géométriquement
réduite pour tout idéal premier minimal $\mathfrak p$ de $S$.
Alors $S$ est géométriquement réduite.
\end{lemma}

\begin{proof}
Comme $S$ est réduite, l'application
$S \to \prod_{\mathfrak p\text{ minimal}} S_{\mathfrak p}$
est injective, voir le
Lemme \ref{lemma-reduced-ring-sub-product-fields}.
Si $K/k$ est une extension de corps, alors les applications
$$
S \otimes_k K \to (\prod S_\mathfrak p) \otimes_k K \to
\prod S_\mathfrak p \otimes_k K
$$
sont injectives : la première parce que $k \to K$ est plate, et la seconde
par inspection puisque $K$ est un $k$-module libre. Comme $S_\mathfrak p$ est
géométriquement réduite, l'anneau de droite est réduit. Ainsi $S \otimes_k K$
est réduit comme sous-anneau d'un anneau réduit.
\end{proof}
```

</details>

### 09 — lemma-separable-algebraic-diagonal

Anglais L10220–10256 ; français L10180–10216.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10220) · FR-ALGEBRA-B14-CHOICE-0009.

La multiplication est identifiée à une localisation, pas seulement à un quotient. Le cas fini utilise un élément primitif et la factorisation P=(x−α)Q ; le cas général utilise la réunion des sous-extensions finies et l'exactitude de la localisation. La formule où manque apparemment une somme au second membre est conservée telle quelle et discutée hors traduction. Corps traduit le titre du chapitre Fields, sans changer ses labels.

Point particulier à relire : Somme manquante au second membre conservée conformément au témoin officiel ; correction mathématique proposée uniquement dans le dossier.

Règles : FR-ALGEBRA-B14-RULE-SEP, FR-ALGEBRA-B14-RULE-LOC, FR-ALGEBRA-B14-RULE-GEN, FR-ALGEBRA-B14-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-separable-algebraic-diagonal}
Let $k'/k$ be a separable algebraic extension.
Then there exists a multiplicative subset $S \subset k' \otimes_k k'$
such that the multiplication map $k' \otimes_k k' \to k'$
is identified with $k' \otimes_k k' \to S^{-1}(k' \otimes_k k')$.
\end{lemma}

\begin{proof}
First assume $k'/k$ is finite separable. Then $k' = k(\alpha)$,
see Fields, Lemma \ref{fields-lemma-primitive-element}.
Let $P \in k[x]$ be the minimal polynomial of $\alpha$ over $k$.
Then $P$ is an irreducible, separable, monic polynomial, see
Fields, Section \ref{fields-section-separable-extensions}.
Then $k'[x]/(P) \to k' \otimes_k k'$,
$\sum \alpha_i x^i \mapsto \alpha_i \otimes \alpha^i$ is an isomorphism.
We can factor $P = (x - \alpha) Q$ in $k'[x]$ and since $P$
is separable we see that $Q(\alpha) \not = 0$.
Then it is clear that the multiplicative set $S'$ generated by
$Q$ in $k'[x]/(P)$ works, i.e., that $k' = (S')^{-1}(k'[x]/(P))$.
By transport of structure the image $S$ of $S'$ in $k' \otimes_k k'$
works.

\medskip\noindent
In the general case we write $k' = \bigcup k_i$ as the union
of its finite subfield extensions over $k$. For each $i$ there
is a multiplicative subset $S_i \subset k_i \otimes_k k_i$
such that $k_i = S_i^{-1}(k_i \otimes_k k_i)$. Let
$S$ be the multiplicative closure of $\bigcup S_i \subset k' \otimes_k k'$.
Clearly, the multiplication maps sends every element of $S$
to an invertible element of $k'$. Using that $k' \otimes_k k'$
is the union of the rings $k_i \otimes_k k_i$ we see that
every element in the kernel of the multiplication map is mapped to zero
in $S^{-1}(k' \otimes_k k')$. Using exactness of localization
the result follows.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-separable-algebraic-diagonal}
Soit $k'/k$ une extension algébrique séparable.
Alors il existe une partie multiplicative $S \subset k' \otimes_k k'$
telle que l'application de multiplication $k' \otimes_k k' \to k'$
s'identifie à $k' \otimes_k k' \to S^{-1}(k' \otimes_k k')$.
\end{lemma}

\begin{proof}
Supposons d'abord que $k'/k$ soit finie et séparable. Alors
$k' = k(\alpha)$, voir le lemme \ref{fields-lemma-primitive-element} de Corps.
Soit $P \in k[x]$ le polynôme minimal de $\alpha$ sur $k$.
Alors $P$ est un polynôme irréductible, séparable et unitaire, voir
la section \ref{fields-section-separable-extensions} de Corps.
Alors $k'[x]/(P) \to k' \otimes_k k'$,
$\sum \alpha_i x^i \mapsto \alpha_i \otimes \alpha^i$ est un isomorphisme.
On peut factoriser $P = (x - \alpha) Q$ dans $k'[x]$ et, puisque $P$
est séparable, on a $Q(\alpha) \not = 0$.
Il est alors clair que la partie multiplicative $S'$ engendrée par
$Q$ dans $k'[x]/(P)$ convient, c'est-à-dire
$k' = (S')^{-1}(k'[x]/(P))$.
Par transport de structure, l'image $S$ de $S'$ dans $k' \otimes_k k'$
convient.

\medskip\noindent
Dans le cas général, écrivons $k' = \bigcup k_i$ comme réunion
de ses sous-extensions finies sur $k$. Pour chaque $i$, il existe une
partie multiplicative $S_i \subset k_i \otimes_k k_i$
telle que $k_i = S_i^{-1}(k_i \otimes_k k_i)$. Soit $S$ la clôture
multiplicative de $\bigcup S_i \subset k' \otimes_k k'$.
Il est clair que l'application de multiplication envoie chaque élément de $S$
sur un élément inversible de $k'$. Comme $k' \otimes_k k'$ est la réunion
des anneaux $k_i \otimes_k k_i$, tout élément du noyau de l'application
de multiplication est envoyé sur zéro dans $S^{-1}(k' \otimes_k k')$.
Par exactitude de la localisation, le résultat s'ensuit.
\end{proof}
```

</details>

### 10 — lemma-geometrically-reduced-over-separable-algebraic

Anglais L10257–10287 ; français L10217–10243.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10257) · FR-ALGEBRA-B14-CHOICE-0010.

Le changement du corps de base k vers k′ est algébrique séparable dans les deux sens. Le premier sens applique le résultat sur une algèbre réduite arbitraire ; le second utilise la localisation de la diagonale. L'égalité tensorielle et son anneau de base sont préservés. Aucun argument alternatif ne se substitue à celui de la source.

Règles : FR-ALGEBRA-B14-RULE-GEO, FR-ALGEBRA-B14-RULE-RED, FR-ALGEBRA-B14-RULE-SEP, FR-ALGEBRA-B14-RULE-LOC, FR-ALGEBRA-B14-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-geometrically-reduced-over-separable-algebraic}
Let $k'/k$ be a separable algebraic field extension.
Let $A$ be an algebra over $k'$. Then $A$ is geometrically
reduced over $k$ if and only if it is geometrically reduced over $k'$.
\end{lemma}

\begin{proof}
Assume $A$ is geometrically reduced over $k'$.
Let $K/k$ be a field extension. Then $K \otimes_k k'$ is
a reduced ring by
Lemma \ref{lemma-separable-extension-preserves-reducedness}.
Hence by Lemma \ref{lemma-geometrically-reduced-any-reduced-base-change}
we find that $K \otimes_k A = (K \otimes_k k') \otimes_{k'} A$ is reduced.

\medskip\noindent
Assume $A$ is geometrically reduced over $k$. Let $K/k'$ be a field
extension. Then
$$
K \otimes_{k'} A = (K \otimes_k A) \otimes_{(k' \otimes_k k')} k'
$$
Since $k' \otimes_k k' \to k'$ is a localization by
Lemma \ref{lemma-separable-algebraic-diagonal},
we see that $K \otimes_{k'} A$
is a localization of a reduced algebra, hence reduced.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-geometrically-reduced-over-separable-algebraic}
Soit $k'/k$ une extension de corps algébrique séparable.
Soit $A$ une algèbre sur $k'$. Alors $A$ est géométriquement
réduite sur $k$ si et seulement si elle est géométriquement réduite sur $k'$.
\end{lemma}

\begin{proof}
Supposons que $A$ soit géométriquement réduite sur $k'$.
Soit $K/k$ une extension de corps. Alors $K \otimes_k k'$ est
un anneau réduit d'après le
Lemme \ref{lemma-separable-extension-preserves-reducedness}.
Ainsi, d'après le
Lemme \ref{lemma-geometrically-reduced-any-reduced-base-change},
nous obtenons que $K \otimes_k A = (K \otimes_k k') \otimes_{k'} A$ est réduit.

\medskip\noindent
Supposons que $A$ soit géométriquement réduite sur $k$. Soit $K/k'$ une extension
de corps. Alors
$$
K \otimes_{k'} A = (K \otimes_k A) \otimes_{(k' \otimes_k k')} k'
$$
Comme $k' \otimes_k k' \to k'$ est une localisation d'après le
Lemme \ref{lemma-separable-algebraic-diagonal}, nous voyons que
$K \otimes_{k'} A$ est une localisation d'une algèbre réduite, donc réduite.
\end{proof}
```

</details>

### 11 — section-separability-continued

Anglais L10288–10294 ; français L10244–10250.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10288) · FR-ALGEBRA-B14-CHOICE-0011.

Suite exprime la continuation annoncée et conserve le renvoi à la première section. Il ne s'agit pas d'une nouvelle définition concurrente.

Règles : FR-ALGEBRA-B14-RULE-SEP.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Separable extensions, continued}
\label{section-separability-continued}

\noindent
In this section we continue the discussion started in
Section \ref{section-separability}.
```

Français restauré :
```tex
\section{Extensions séparables, suite}
\label{section-separability-continued}

\noindent
Dans cette section, nous poursuivons la discussion commencée dans la
section \ref{section-separability}.
```

</details>

### 12 — lemma-mini-separability

Anglais L10295–10358 ; français L10251–10317.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10295) · FR-ALGEBRA-B14-CHOICE-0012.

Les deux hypothèses et le choix d'un des n+1 générateurs sont conservés. Ne sont pas toutes multiples de p exprime sans ambiguïté not all : au moins un exposant échappe à la divisibilité, non tous les exposants. La preuve par degré minimal, dépendance linéaire puis Gauss garde ses étapes. Dans la transition, adjoindre les racines à k remplace dans k : ces racines vivent dans l'extension et peuvent manquer dans k. La parenthèse identifiant le sous-corps d'une clôture algébrique reste présente.

Point particulier à relire : La portée de la négation est rendue explicite ; not all n'est pas none. Adjoindre à k ne suppose pas que les racines soient déjà dans k. Ces deux réparations françaises n'altèrent aucune formule.

Règles : FR-ALGEBRA-B14-RULE-SEP, FR-ALGEBRA-B14-RULE-TRANS, FR-ALGEBRA-B14-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-mini-separability}
Let $k$ be a field of characteristic $p > 1$. Let $K/k$
be a field extension generated by $x_1, \ldots, x_{n + 1} \in K$ such that
\begin{enumerate}
\item $\{x_1, \ldots, x_n\}$ is a transcendence base of $K/k$,
\item for every $k$-linearly independent subset
$\{a_1, \ldots, a_m\}$ of $K$ the set
$\{a^p_1, \ldots, a_m^p\}$ is $k$-linearly independent.
\end{enumerate}
Then there is $1 \leq j \leq n+1$ such that
$\{ x_1, \ldots, \widehat{x}_j, \ldots, x_{n+1}\}$
is a separating transcendence base for $K / k$.
\end{lemma}

\begin{proof}
By assumption $x_{n + 1}$ is algebraic over $k(x_1, \ldots, x_n)$
so there exists a non-zero polynomial $F \in k[X_1, \ldots, X_{n + 1}]$
such that $F(x_1, \ldots, x_{n+1}) = 0$. Choose $F$ of minimal total degree.
Then $F$ is irreducible, because at least one irreducible factor
must also have the same property.

\medskip\noindent
We claim that, for some $i$, not all powers of $X_i$ appearing in $F$
are multiples of $p$. Suppose for a contradiction that all the exponents
appearing in $F$ were multiples of $p$, then the set
$$
\{x_1^{\alpha_1} \ldots x^{\alpha_{n+1}}_{n+1} \mid \lambda_\alpha \neq 0\}
\subset
K
$$
is $k$-linearly dependent where $\lambda_\alpha$ are the coefficients of $F$.
By assumption (2) we conclude the set
$$
\{x_1^{\alpha_1 / p} \ldots x^{\alpha_{n+1} / p}_{n+1}
\mid \lambda_\alpha \neq 0 \}
$$
is also $k$-linearly dependent, contradicting minimality of $\deg(F)$.

\medskip\noindent
Choose $i$ for which a non-$p$th power of $X_i$ appears in $F$. Then we
see that $x_i$ is algebraic over
$L = k(x_1, \ldots, x_{i - 1}, x_{i + 1}, \ldots, x_{n+1})$.
By Fields, Lemma \ref{fields-lemma-transcendence-degree}
we see that $x_1, \ldots, x_{i - 1}, x_{i + 1}, \ldots, x_{n+1}$
is a transcendence base of $K/k$. Thus $L$ is the fraction field
of the polynomial ring over $k$ in
$x_1, \ldots, x_{i - 1}, x_{i + 1}, \ldots, x_{n + 1}$.
By Gauss' Lemma we conclude that
$$
P(T) =
F(x_1, \ldots, x_{i - 1}, T, x_{i + 1}, \ldots, x_{n + 1}) \in L[T]
$$
is irreducible. By construction $P(T)$ is not contained in $L[T^p]$.
Hence $K/L$ is separable as required.
\end{proof}

\noindent
Let $p$ be a prime number and let $k$ be a field of characteristic $p$.
In this case we write $k^{1/p}$ for the extension of $k$ gotten by
adjoining $p$th roots of all the elements of $k$ to $k$.
(In other words it is the subfield of an algebraic closure of
$k$ generated by the $p$th roots of elements of $k$.)
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-mini-separability}
Soit $k$ un corps de caractéristique $p > 1$. Soit $K/k$
une extension de corps engendrée par $x_1, \ldots, x_{n + 1} \in K$ telle que
\begin{enumerate}
\item $\{x_1, \ldots, x_n\}$ soit une base de transcendance de $K/k$,
\item pour tout sous-ensemble $k$-linéairement indépendant
$\{a_1, \ldots, a_m\}$ de $K$, l'ensemble
$\{a^p_1, \ldots, a_m^p\}$ soit linéairement indépendant sur $k$.
\end{enumerate}
Alors il existe $1 \leq j \leq n+1$ tel que
$\{ x_1, \ldots, \widehat{x}_j, \ldots, x_{n+1}\}$
soit une base de transcendance séparante de $K / k$.
\end{lemma}

\begin{proof}
Par hypothèse, $x_{n + 1}$ est algébrique sur $k(x_1, \ldots, x_n)$,
et il existe donc un polynôme non nul $F \in k[X_1, \ldots, X_{n + 1}]$
tel que $F(x_1, \ldots, x_{n+1}) = 0$. Choisissons $F$ de degré total minimal.
Alors $F$ est irréductible, car au moins un facteur irréductible
doit également avoir cette propriété.

\medskip\noindent
Nous affirmons que, pour un certain $i$, les puissances de $X_i$
qui apparaissent dans $F$ ne sont pas toutes multiples de $p$. Supposons par
contradiction que tous les exposants apparaissant dans $F$ soient
des multiples de $p$ ; alors l'ensemble
$$
\{x_1^{\alpha_1} \ldots x^{\alpha_{n+1}}_{n+1} \mid \lambda_\alpha \neq 0\}
\subset
K
$$
est linéairement dépendant sur $k$, où les $\lambda_\alpha$ sont les
coefficients de $F$. Par l'hypothèse (2), nous concluons que l'ensemble
$$
\{x_1^{\alpha_1 / p} \ldots x^{\alpha_{n+1} / p}_{n+1}
\mid \lambda_\alpha \neq 0 \}
$$
est également linéairement dépendant sur $k$, ce qui contredit la minimalité
de $\deg(F)$.

\medskip\noindent
Choisissons $i$ tel qu'une puissance non-$p$-ième de $X_i$ apparaisse
dans $F$. Alors $x_i$ est algébrique sur
$L = k(x_1, \ldots, x_{i - 1}, x_{i + 1}, \ldots, x_{n+1})$.
D'après le lemme \ref{fields-lemma-transcendence-degree} de Corps,
nous voyons que $x_1, \ldots, x_{i - 1}, x_{i + 1}, \ldots, x_{n+1}$
est une base de transcendance de $K/k$. Ainsi $L$ est le corps des fractions
de l'anneau de polynômes sur $k$ en
$x_1, \ldots, x_{i - 1}, x_{i + 1}, \ldots, x_{n + 1}$.
Par le Lemme de Gauss, nous concluons que
$$
P(T) =
F(x_1, \ldots, x_{i - 1}, T, x_{i + 1}, \ldots, x_{n + 1}) \in L[T]
$$
est irréductible. Par construction, $P(T)$ n'est pas contenu dans $L[T^p]$.
Ainsi $K/L$ est séparable, comme requis.
\end{proof}

\noindent
Soit $p$ un nombre premier et soit $k$ un corps de caractéristique $p$.
Dans ce cas, nous écrivons $k^{1/p}$ pour l'extension de $k$ obtenue
en adjoignant les racines $p$-ièmes de tous les éléments de $k$
à $k$.
(Autrement dit, c'est le sous-corps d'une clôture algébrique de
$k$ engendré par les racines $p$-ièmes des éléments de $k$.)
```

</details>

### 13 — lemma-characterize-separable-field-extensions

Anglais L10359–10408 ; français L10318–10369.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10359) · FR-ALGEBRA-B14-CHOICE-0013.

Les quatre critères gardent leur ordre et la caractéristique positive. m est un homomorphisme d'anneaux, non déclaré k-linéaire ; le Frobenius dans sa formule reste identique. La preuve par minimalité du degré d'inséparabilité n'est pas remplacée. Engendré s'accorde avec le corps K ; l'extension serait engendrée. L'indice n du dernier appel au lemme, incompatible avec d dans ce passage, reste celui de la source et fait l'objet d'une observation séparée.

Point particulier à relire : Accord grammatical réparé pour K. L'indice n de la source n'est pas normalisé vers d dans la traduction ; la proposition de correction est séparée.

Règles : FR-ALGEBRA-B14-RULE-GEO, FR-ALGEBRA-B14-RULE-RED, FR-ALGEBRA-B14-RULE-SEP, FR-ALGEBRA-B14-RULE-TRANS, FR-ALGEBRA-B14-RULE-GEN, FR-ALGEBRA-B14-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-characterize-separable-field-extensions}
Let $k$ be a field of characteristic $p > 0$.
Let $K/k$ be a field extension.
The following are equivalent:
\begin{enumerate}
\item $K$ is separable over $k$,
\item for every $k$-linearly independent subset $\{a_1, \ldots, a_m\}$
of $K$ the set $\{a^p_1, \ldots, a_m^p\}$ is $k$-linearly independent,
\item the ring $K \otimes_k k^{1/p}$ is reduced, and
\item $K$ is geometrically reduced over $k$.
\end{enumerate}
\end{lemma}

\begin{proof}
The implication (1) $\Rightarrow$ (4) follows from
Lemma \ref{lemma-separable-extension-preserves-reducedness}.
The implication (4) $\Rightarrow$ (3) is immediate.

\medskip\noindent
Assume (3). Consider the ring homomorphism
$m : K \otimes_k k^{1/p} \rightarrow K$ given by 
$$
\lambda \otimes \mu \rightarrow \lambda^p \mu^p
$$
Note that $x^p = m(x) \otimes 1$ for all $x \in K \otimes_k k^{1/p}$.
Since $K \otimes_k k^{1/p}$ is reduced
we see $m$ is injective. If $\{a_1, \ldots, a_m\} \subset K$
is $k$-linearly independent, then $\{a_1 \otimes 1, \ldots, a_m \otimes 1\}$
is $k^{1/p}$-linearly independent. By injectivity of $m$ we deduce
that no nontrivial $k$-linear combination of $a_1^p, \ldots, a_m^p$ is
is zero. Hence (3) implies (2).

\medskip\noindent
Assume (2). To prove (1) we may assume that $K$ is finitely generated over $k$
and we have to prove that $K$ is separably generated over $k$.
Let $\{x_1, \ldots, x_d\}$ be a transcendence base of $K/k$. By
Fields, Lemma \ref{fields-lemma-algebraic-finitely-generated}
we have $[K : K'] < \infty$ where $K' = k(x_1, \ldots, x_d)$.
Choose the transcendence base such that the degree of inseparability
$[K : K']_i$ is minimal. If $K / K'$ is separable then we win.
Assume this is not the case to get a contradiction. Then there exists
$x_{d + 1} \in K$ which is not separable over $K'$, and in particular
$[K'(x_{d+1}) : K']_i > 1$. Then by
Lemma \ref{lemma-mini-separability} there is $1 \leq j \leq n + 1$
such that $K'' = k(x_1, \ldots, \widehat{x}_j, \ldots, x_{d+1})$
satisfies $[K'(x_{d+1}) : K'']_i = 1$. By multiplicativity
$[K : K'']_i < [K : K']_i$ and we obtain the contradiction.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-characterize-separable-field-extensions}
Soit $k$ un corps de caractéristique $p > 0$.
Soit $K/k$ une extension de corps.
Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item $K$ est séparable sur $k$,
\item pour tout sous-ensemble $k$-linéairement indépendant
$\{a_1, \ldots, a_m\}$ de $K$, l'ensemble $\{a^p_1, \ldots, a_m^p\}$ est linéairement
indépendant sur $k$,
\item l'anneau $K \otimes_k k^{1/p}$ est réduit, et
\item $K$ est géométriquement réduit sur $k$.
\end{enumerate}
\end{lemma}

\begin{proof}
L'implication (1) $\Rightarrow$ (4) résulte du
Lemme \ref{lemma-separable-extension-preserves-reducedness}.
L'implication (4) $\Rightarrow$ (3) est immédiate.

\medskip\noindent
Supposons (3). Considérons l'homomorphisme d'anneaux
$m : K \otimes_k k^{1/p} \rightarrow K$ défini par
$$
\lambda \otimes \mu \rightarrow \lambda^p \mu^p
$$
Remarquons que $x^p = m(x) \otimes 1$ pour tout $x \in K \otimes_k k^{1/p}$.
Comme $K \otimes_k k^{1/p}$ est réduit, nous voyons que $m$ est injectif.
Si $\{a_1, \ldots, a_m\} \subset K$ est linéairement indépendant sur $k$,
alors $\{a_1 \otimes 1, \ldots, a_m \otimes 1\}$ est linéairement
indépendant sur $k^{1/p}$. Par injectivité de $m$, nous déduisons
qu'aucune combinaison $k$-linéaire non triviale de
$a_1^p, \ldots, a_m^p$ n'est nulle. Ainsi (3) implique (2).

\medskip\noindent
Supposons (2). Pour démontrer (1), nous pouvons supposer que $K$ est
de type fini sur $k$, et nous devons montrer que $K$ est séparablement
engendré sur $k$.
Soit $\{x_1, \ldots, x_d\}$ une base de transcendance de $K/k$.
D'après le lemme \ref{fields-lemma-algebraic-finitely-generated} de Corps,
nous avons $[K : K'] < \infty$, où $K' = k(x_1, \ldots, x_d)$.
Choisissons la base de transcendance de sorte que le degré d'inséparabilité
$[K : K']_i$ soit minimal. Si $K / K'$ est séparable, la conclusion est acquise.
Supposons le contraire afin d'obtenir une contradiction. Alors il existe
$x_{d + 1} \in K$ qui n'est pas séparable sur $K'$ et, en particulier,
$[K'(x_{d+1}) : K']_i > 1$. Alors, d'après le
Lemme \ref{lemma-mini-separability}, il existe $1 \leq j \leq n + 1$
tel que $K'' = k(x_1, \ldots, \widehat{x}_j, \ldots, x_{d+1})$
satisfasse $[K'(x_{d+1}) : K'']_i = 1$. Par multiplicativité,
$[K : K'']_i < [K : K']_i$, ce qui donne la contradiction.
\end{proof}
```

</details>

### 14 — lemma-separably-generated-separable

Anglais L10409–10423 ; français L10370–10384.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10409) · FR-ALGEBRA-B14-CHOICE-0014.

La phrase établit l'implication séparablement engendrée ⇒ séparable, et non une équivalence nouvelle. Le renvoi à deux lemmes et l'annonce de la clôture parfaite sont conservés. Polo 13.16 atteste la première expression ; le sens de la seconde pour des extensions non algébriques reste celui déjà défini dans Stacks.

Règles : FR-ALGEBRA-B14-RULE-SEP, FR-ALGEBRA-B14-RULE-PERF, FR-ALGEBRA-B14-RULE-GEN.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-separably-generated-separable}
A separably generated field extension is separable.
\end{lemma}

\begin{proof}
Combine Lemma \ref{lemma-separable-extension-preserves-reducedness}
with Lemma \ref{lemma-characterize-separable-field-extensions}.
\end{proof}

\noindent
In the following lemma we will use the notion of the perfect closure
which is defined in
Definition \ref{definition-perfection}.
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-separably-generated-separable}
Une extension de corps séparablement engendrée est séparable.
\end{lemma}

\begin{proof}
Combiner le Lemme \ref{lemma-separable-extension-preserves-reducedness}
avec le Lemme \ref{lemma-characterize-separable-field-extensions}.
\end{proof}

\noindent
Dans le lemme suivant, nous utiliserons la notion de clôture parfaite,
qui est définie dans la
Définition \ref{definition-perfection}.
```

</details>

### 15 — lemma-geometrically-reduced-finite-purely-inseparable-extension

Anglais L10424–10481 ; français L10385–10440.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10424) · FR-ALGEBRA-B14-CHOICE-0015.

Les cinq critères sont traduits intégralement, avec les quantificateurs et les inclusions de corps de la preuve. L'argument (1)⇒(5) passe par un diagramme fini, celui de (2)⇒(5) par les localisations aux premiers minimaux. L'emploi de k^{1/p} sans caractéristique positive dans l'énoncé général reste source-littéral ; une note précise la convention non explicitée, sans présenter cela comme un théorème réfuté.

Point particulier à relire : La définition locale de k^{1/p} suppose p premier et caractéristique p. Une convention k^{1/p}=k en caractéristique nulle n'est pas formulée dans le passage relu ; la note constate cette limite sans inventer une admission d'erratum.

Règles : FR-ALGEBRA-B14-RULE-GEO, FR-ALGEBRA-B14-RULE-RED, FR-ALGEBRA-B14-RULE-PURE, FR-ALGEBRA-B14-RULE-PERF, FR-ALGEBRA-B14-RULE-LOC, FR-ALGEBRA-B14-RULE-GEN, FR-ALGEBRA-B14-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-geometrically-reduced-finite-purely-inseparable-extension}
Let $k$ be a field. Let $S$ be a $k$-algebra.
The following are equivalent:
\begin{enumerate}
\item $k' \otimes_k S$ is reduced for every finite
purely inseparable extension $k'$ of $k$,
\item $k^{1/p} \otimes_k S$ is reduced,
\item $k^{perf} \otimes_k S$ is reduced, where $k^{perf}$ is the
perfect closure of $k$,
\item $\overline{k} \otimes_k S$ is reduced, where $\overline{k}$ is the
algebraic closure of $k$, and
\item $S$ is geometrically reduced over $k$.
\end{enumerate}
\end{lemma}

\begin{proof}
Note that any finite purely inseparable extension $k'/k$ embeds
in $k^{perf}$. Moreover, $k^{1/p}$ embeds into $k^{perf}$ which embeds
into $\overline{k}$. Thus it is
clear that (5) $\Rightarrow$ (4) $\Rightarrow$ (3) $\Rightarrow$ (2)
and that (3) $\Rightarrow$ (1).

\medskip\noindent
We prove that (1) $\Rightarrow$ (5).
Assume $k' \otimes_k S$ is reduced for every finite
purely inseparable extension $k'$ of $k$. Let $K/k$ be
an extension of fields. We have to show that $K \otimes_k S$
is reduced. By Lemma \ref{lemma-limit-argument} we reduce to the case where
$K/k$ is a finitely generated field extension. Choose a diagram
$$
\xymatrix{
K \ar[r] & K' \\
k \ar[u] \ar[r] & k' \ar[u]
}
$$
as in Lemma \ref{lemma-make-separably-generated}.
By assumption $k' \otimes_k S$ is reduced.
By Lemma \ref{lemma-separable-extension-preserves-reducedness}
it follows that $K' \otimes_k S$ is reduced.
Hence we conclude that $K \otimes_k S$ is reduced as desired.

\medskip\noindent
Finally we prove that (2) $\Rightarrow$ (5).
Assume $k^{1/p} \otimes_k S$ is reduced. Then $S$ is reduced.
Moreover, for each localization $S_{\mathfrak p}$ at a minimal
prime $\mathfrak p$, the ring $k^{1/p}\otimes_k S_{\mathfrak p}$
is a localization of $k^{1/p} \otimes_k S$ hence is reduced.
But $S_{\mathfrak p}$ is a field by
Lemma \ref{lemma-minimal-prime-reduced-ring},
hence $S_{\mathfrak p}$ is geometrically reduced by
Lemma \ref{lemma-characterize-separable-field-extensions}.
It follows from Lemma \ref{lemma-generic-points-geometrically-reduced}
that $S$ is geometrically reduced.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-geometrically-reduced-finite-purely-inseparable-extension}
Soit $k$ un corps. Soit $S$ une $k$-algèbre.
Les assertions suivantes sont équivalentes :
\begin{enumerate}
\item $k' \otimes_k S$ est réduit pour toute extension finie
purement inséparable $k'$ de $k$,
\item $k^{1/p} \otimes_k S$ est réduit,
\item $k^{perf} \otimes_k S$ est réduit, où $k^{perf}$ est la
clôture parfaite de $k$,
\item $\overline{k} \otimes_k S$ est réduit, où $\overline{k}$ est la
clôture algébrique de $k$, et
\item $S$ est géométriquement réduite sur $k$.
\end{enumerate}
\end{lemma}

\begin{proof}
Remarquons que toute extension finie purement inséparable $k'/k$ se plonge
dans $k^{perf}$. De plus, $k^{1/p}$ se plonge dans $k^{perf}$, qui se
plonge lui-même dans $\overline{k}$. Il est donc clair que
(5) $\Rightarrow$ (4) $\Rightarrow$ (3) $\Rightarrow$ (2)
et que (3) $\Rightarrow$ (1).

\medskip\noindent
Prouvons que (1) $\Rightarrow$ (5).
Supposons que $k' \otimes_k S$ soit réduit pour toute extension finie
purement inséparable $k'$ de $k$. Soit $K/k$ une extension de corps.
Nous devons montrer que $K \otimes_k S$ est réduit. D'après le
Lemme \ref{lemma-limit-argument}, nous nous ramenons au cas où
$K/k$ est une extension de corps de type fini. Choisissons un diagramme
$$
\xymatrix{
K \ar[r] & K' \\
k \ar[u] \ar[r] & k' \ar[u]
}
$$
comme dans le Lemme \ref{lemma-make-separably-generated}.
Par hypothèse, $k' \otimes_k S$ est réduit.
D'après le Lemme \ref{lemma-separable-extension-preserves-reducedness},
il s'ensuit que $K' \otimes_k S$ est réduit.
Nous concluons donc que $K \otimes_k S$ est réduit, comme voulu.

\medskip\noindent
Enfin, démontrons que (2) $\Rightarrow$ (5).
Supposons que $k^{1/p} \otimes_k S$ soit réduit. Alors $S$ est réduite.
De plus, pour chaque localisation $S_{\mathfrak p}$ en un idéal premier
minimal $\mathfrak p$, l'anneau $k^{1/p}\otimes_k S_{\mathfrak p}$
est une localisation de $k^{1/p} \otimes_k S$, donc est réduit.
Mais $S_{\mathfrak p}$ est un corps d'après le
Lemme \ref{lemma-minimal-prime-reduced-ring},
donc $S_{\mathfrak p}$ est géométriquement réduit d'après le
Lemme \ref{lemma-characterize-separable-field-extensions}.
Il s'ensuit du Lemme \ref{lemma-generic-points-geometrically-reduced}
que $S$ est géométriquement réduite.
\end{proof}
```

</details>

### 16 — section-perfect-fields

Anglais L10482–10487 ; français L10441–10446.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10482) · FR-ALGEBRA-B14-CHOICE-0016.

Corps parfaits est attesté par Dat 2.6 et Polo 13.21. L'introduction brève reste une introduction, sans ajout d'exemples ni d'exercice.

Règles : FR-ALGEBRA-B14-RULE-PERF.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{Perfect fields}
\label{section-perfect-fields}

\noindent
Here is the definition.
```

Français restauré :
```tex
\section{Corps parfaits}
\label{section-perfect-fields}

\noindent
Voici la définition.
```

</details>

### 17 — definition-perfect

Anglais L10488–10493 ; français L10447–10452.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10488) · FR-ALGEBRA-B14-CHOICE-0017.

La définition de Stacks porte sur toutes les extensions de corps, non seulement les extensions algébriques. Dat 2.6.1 utilise une formulation algébrique équivalente dans son contexte ; on ne la substitue pas ici. Parfait est gardé au masculin avec corps.

Règles : FR-ALGEBRA-B14-RULE-SEP, FR-ALGEBRA-B14-RULE-PERF.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-perfect}
Let $k$ be a field. We say $k$ is {\it perfect}
if every field extension of $k$ is separable over $k$.
\end{definition}
```

Français restauré :
```tex
\begin{definition}
\label{definition-perfect}
Soit $k$ un corps. On dit que $k$ est {\it parfait}
si toute extension de corps de $k$ est séparable sur $k$.
\end{definition}
```

</details>

### 18 — lemma-perfect

Anglais L10494–10511 ; français L10453–10470.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10494) · FR-ALGEBRA-B14-CHOICE-0018.

Le critère garde l'alternative caractéristique nulle ou caractéristique p avec une racine p-ième pour tout élément. La deuxième condition appartient au second cas. Dat 2.6.2 et Polo 13.21 attestent le même critère par surjectivité du Frobenius. Le français conserve l'aller-retour et le renvoi au critère de séparabilité, sans ajouter une hypothèse de finitude.

Règles : FR-ALGEBRA-B14-RULE-SEP, FR-ALGEBRA-B14-RULE-PERF.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-perfect}
A field $k$ is perfect if and only if it is a field of characteristic $0$
or a field of characteristic $p > 0$ such that every element has a $p$th
root.
\end{lemma}

\begin{proof}
The characteristic zero case is clear.
Assume the characteristic of $k$ is $p > 0$.
If $k$ is perfect, then all the field extensions where we adjoin
a $p$th root of an element of $k$ have to be trivial, hence every
element of $k$ has a $p$th root. Conversely if every element has a $p$th
root, then $k = k^{1/p}$ and every field extension of $k$ is
separable by
Lemma \ref{lemma-characterize-separable-field-extensions}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-perfect}
Un corps $k$ est parfait si et seulement s'il est de caractéristique $0$
ou de caractéristique $p > 0$ et si tout élément possède une
racine $p$-ième.
\end{lemma}

\begin{proof}
Le cas de caractéristique nulle est clair.
Supposons que la caractéristique de $k$ soit $p > 0$.
Si $k$ est parfait, toutes les extensions de corps obtenues en adjoignant
une racine $p$-ième d'un élément de $k$ doivent être triviales ; tout
élément de $k$ possède donc une racine $p$-ième. Réciproquement, si tout
élément possède une racine $p$-ième, alors $k = k^{1/p}$ et toute extension
de corps de $k$ est séparable d'après le
Lemme \ref{lemma-characterize-separable-field-extensions}.
\end{proof}
```

</details>

### 19 — lemma-make-separable

Anglais L10512–10543 ; français L10471–10502.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10512) · FR-ALGEBRA-B14-CHOICE-0019.

Finies purement inséparables qualifie k′/k et K′/K, séparable qualifie K′/k′. Le compositum et l'anneau réduit du produit tensoriel sont conservés. Domaine devient anneau intègre conformément à Ducros ; le passage d'anneau intègre à corps reste justifié par le même lemme d'intégralité. L'argument en puissances p^n n'est pas étendu silencieusement au cas de caractéristique nulle.

Point particulier à relire : Le quatrième domaine du lot devient anneau intègre. Compositum est conservé source-guidé ; pas d'attestation nouvelle prétendue dans les pages lues.

Règles : FR-ALGEBRA-B14-RULE-DOMAIN, FR-ALGEBRA-B14-RULE-SEP, FR-ALGEBRA-B14-RULE-PURE, FR-ALGEBRA-B14-RULE-GEN, FR-ALGEBRA-B14-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-make-separable}
Let $K/k$ be a finitely generated field extension.
There exists a diagram
$$
\xymatrix{
K \ar[r] & K' \\
k \ar[u] \ar[r] & k' \ar[u]
}
$$
where $k'/k$, $K'/K$ are finite purely inseparable field
extensions such that $K'/k'$ is a separable field extension.
In this situation we can assume that $K' = k'K$ is the compositum,
and also that $K' = (k' \otimes_k K)_{red}$.
\end{lemma}

\begin{proof}
By Lemma \ref{lemma-make-separably-generated}
we can find such a diagram with $K'/k'$ separably generated.
By
Lemma \ref{lemma-separably-generated-separable}
this implies that $K'$ is separable over $k'$.
The compositum $k'K$ is a subextension of $K'/k'$ and hence
$k' \subset k'K$ is separable by
Lemma \ref{lemma-subextensions-are-separable}.
The ring $(k' \otimes_k K)_{red}$ is a domain as for some
$n \gg 0$ the map $x \mapsto x^{p^n}$ maps it into $K$.
Hence it is a field by
Lemma \ref{lemma-integral-over-field}.
Thus $(k' \otimes_k K)_{red} \to K'$ maps it isomorphically onto $k'K$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-make-separable}
Soit $K/k$ une extension de corps de type fini.
Il existe un diagramme
$$
\xymatrix{
K \ar[r] & K' \\
k \ar[u] \ar[r] & k' \ar[u]
}
$$
où $k'/k$ et $K'/K$ sont des extensions de corps finies
purement inséparables telles que $K'/k'$ soit une extension de corps séparable.
Dans cette situation, on peut supposer que $K' = k'K$ est le compositum,
et aussi que $K' = (k' \otimes_k K)_{red}$.
\end{lemma}

\begin{proof}
D'après le Lemme \ref{lemma-make-separably-generated},
nous pouvons trouver un tel diagramme avec $K'/k'$ séparablement engendrée.
D'après le
Lemme \ref{lemma-separably-generated-separable},
il s'ensuit que $K'$ est séparable sur $k'$.
Le compositum $k'K$ est une sous-extension de $K'/k'$ et donc
$k' \subset k'K$ est séparable d'après le
Lemme \ref{lemma-subextensions-are-separable}.
L'anneau $(k' \otimes_k K)_{red}$ est un anneau intègre, car pour un certain
$n \gg 0$ l'application $x \mapsto x^{p^n}$ l'envoie dans $K$.
Il est donc un corps d'après le
Lemme \ref{lemma-integral-over-field}.
Ainsi $(k' \otimes_k K)_{red} \to K'$ l'envoie isomorphiquement sur $k'K$.
\end{proof}
```

</details>

### 20 — lemma-perfection

Anglais L10544–10567 ; français L10503–10528.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10544) · FR-ALGEBRA-B14-CHOICE-0020.

La clôture parfaite est unique à isomorphisme unique près comme extension de k, et non comme corps privé de sa structure sur k. Le slogan et le cas de caractéristique nulle restent présents. Le masculin parfait remplace parfaite pour k′. La construction via les copies abstraites de k et les flèches de Frobenius est conservée, y compris les détails omis. Le mot clôture n'est pas confondu avec une complétion topologique.

Point particulier à relire : k′ est le corps qui est parfait, non l'extension qui serait parfaite. L'unicité et les flèches restent celles de l'auteur.

Règles : FR-ALGEBRA-B14-RULE-PURE, FR-ALGEBRA-B14-RULE-PERF, FR-ALGEBRA-B14-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-perfection}
\begin{slogan}
Every field has a unique perfect closure.
\end{slogan}
For every field $k$ there exists a purely inseparable extension
$k'/k$ such that $k'$ is perfect. The field extension
$k'/k$ is unique up to unique isomorphism.
\end{lemma}

\begin{proof}
If the characteristic of $k$ is zero, then $k' = k$ is the
unique choice. Assume the characteristic of $k$ is $p > 0$.
For every $n > 0$ there exists a unique algebraic extension
$k \subset k^{1/p^n}$ such that (a) every element $\lambda \in k$
has a $p^n$th root in $k^{1/p^n}$ and (b) for every element
$\mu \in k^{1/p^n}$ we have $\mu^{p^n} \in k$.
Namely, consider the ring map $k \to k^{1/p^n} = k$, $x \mapsto x^{p^n}$.
This is injective and satisfies (a) and (b). It is clear that
$k^{1/p^n} \subset k^{1/p^{n + 1}}$ as extensions of $k$ via
the map $y \mapsto y^p$. Then we can take $k' = \bigcup k^{1/p^n}$.
Some details omitted.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-perfection}
\begin{slogan}
Tout corps possède une clôture parfaite unique.
\end{slogan}
Pour tout corps $k$, il existe une extension purement inséparable
$k'/k$ telle que $k'$ soit parfait. L'extension de corps
$k'/k$ est unique à isomorphisme unique près.
\end{lemma}

\begin{proof}
Si la caractéristique de $k$ est nulle, alors $k' = k$ est l'unique choix.
Supposons que la caractéristique de $k$ soit $p > 0$.
Pour tout $n > 0$, il existe une unique extension algébrique
$k \subset k^{1/p^n}$ telle que (a) tout élément $\lambda \in k$
possède une racine $p^n$-ième dans $k^{1/p^n}$ et (b) pour tout élément
$\mu \in k^{1/p^n}$, on ait $\mu^{p^n} \in k$.
C'est-à-dire, considérons l'application d'anneaux
$k \to k^{1/p^n} = k$, $x \mapsto x^{p^n}$.
Elle est injective et satisfait (a) et (b). Il est clair que
$k^{1/p^n} \subset k^{1/p^{n + 1}}$ comme extensions de $k$ via
l'application $y \mapsto y^p$. Nous pouvons donc prendre
$k' = \bigcup k^{1/p^n}$.
Quelques détails sont omis.
\end{proof}
```

</details>

### 21 — definition-perfection

Anglais L10568–10579 ; français L10529–10542.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10568) · FR-ALGEBRA-B14-CHOICE-0021.

Clôture parfaite conserve la distinction avec clôture algébrique et clôture séparable ; son sens précis est fixé par le lemme précédent. Une attestation française externe de l'expression existe dans la recherche, mais aucune page complète correspondante n'a été consultée pour ce lot : la décision reste explicitement source-guidée. La notation perf reste inchangée. La transition sur les sous-extensions purement inséparables est entièrement conservée.

Point particulier à relire : Clôture parfaite est justifiée par la définition source et le registre déjà retenu. Pas d'attestation externe complète nouvellement lue pour ces deux mots ensemble.

Règles : FR-ALGEBRA-B14-RULE-PURE, FR-ALGEBRA-B14-RULE-PERF.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{definition}
\label{definition-perfection}
Let $k$ be a field. The field extension $k'/k$ of Lemma \ref{lemma-perfection}
is called the {\it perfect closure} of $k$. Notation $k^{perf}/k$.
\end{definition}

\noindent
Note that if $k'/k$ is any algebraic purely inseparable extension, then
$k'$ is a subextension of $k^{perf}$, i.e., $k^{perf}/k'/k$. Namely,
$(k')^{perf}$ is isomorphic to $k^{perf}$ by the uniqueness of
Lemma \ref{lemma-perfection}.
```

Français restauré :
```tex
\begin{definition}
\label{definition-perfection}
Soit $k$ un corps. L'extension de corps $k'/k$ du
Lemme \ref{lemma-perfection} s'appelle la {\it clôture parfaite} de $k$.
Notation : $k^{perf}/k$.
\end{definition}

\noindent
Remarquons que si $k'/k$ est une extension algébrique purement inséparable,
alors $k'$ est une sous-extension de $k^{perf}$, c'est-à-dire
$k^{perf}/k'/k$. En effet, $(k')^{perf}$ est isomorphe à $k^{perf}$
par l'unicité du
Lemme \ref{lemma-perfection}.
```

</details>

### 22 — lemma-perfect-reduced

Anglais L10580–10603 ; français L10543–10558.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10580) · FR-ALGEBRA-B14-CHOICE-0022.

Le corps de base parfait est indispensable à la première assertion. La seconde concerne deux k-algèbres réduites, sans hypothèse de type fini. Polo 2.16 présente un cas sur une clôture algébrique avec finitude : il éclaire le vocabulaire, sans réduire la portée plus générale de Stacks. Les deux renvois constituent toute la preuve originale et sont préservés.

Règles : FR-ALGEBRA-B14-RULE-GEO, FR-ALGEBRA-B14-RULE-RED, FR-ALGEBRA-B14-RULE-PERF.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-perfect-reduced}
Let $k$ be a perfect field.
Any reduced $k$ algebra is geometrically reduced over $k$.
Let $R$, $S$ be $k$-algebras.
Assume both $R$ and $S$ are reduced.
Then the $k$-algebra $R \otimes_k S$ is reduced.
\end{lemma}

\begin{proof}
The first statement follows from
Lemma \ref{lemma-geometrically-reduced-finite-purely-inseparable-extension}.
For the second statement use the first statement and
Lemma \ref{lemma-geometrically-reduced-any-reduced-base-change}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-perfect-reduced}
Soit $k$ un corps parfait.
Toute $k$-algèbre réduite est géométriquement réduite sur $k$.
Soient $R$ et $S$ des $k$-algèbres.
Supposons que $R$ et $S$ soient toutes deux réduites.
Alors la $k$-algèbre $R \otimes_k S$ est réduite.
\end{lemma}

\begin{proof}
La première assertion résulte du
Lemme \ref{lemma-geometrically-reduced-finite-purely-inseparable-extension}.
Pour la seconde, utiliser la première assertion et le
Lemme \ref{lemma-geometrically-reduced-any-reduced-base-change}.
\end{proof}
```

</details>

## Observations extérieures au texte traduit

### FR-ALGEBRA-B14-SOURCE-NOTE-0001

[Source L10235](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10235) — lemma-separable-algebraic-diagonal.

```tex
$\sum \alpha_i x^i \mapsto \alpha_i \otimes \alpha^i$
```

L'isomorphisme annoncé est k′-linéaire et doit envoyer chaque monôme α_i x^i sur α_i⊗α^i, donc un polynôme sur la somme de ces tenseurs. La formule imprimée omet la somme au second membre et y laisse i libre. Ajouter \sum à droite est la correction proposée ; la traduction conserve exactement la formule officielle. Il ne s'agit pas d'un contre-exemple au lemme.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

### FR-ALGEBRA-B14-SOURCE-NOTE-0002

[Source L10403](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10403) — lemma-characterize-separable-field-extensions.

```tex
there is $1 \leq j \leq n + 1$
```

Le passage fixe une base x1,…,xd puis ajoute x_{d+1}. Le lemme précédent permet d'omettre l'un de ces d+1 éléments. n n'est pas défini dans cette preuve : remplacer n+1 par d+1 rétablit la borne localement justifiée. Le français garde n+1 et la proposition reste extérieure au texte.

Confiance éditoriale : forte ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

### FR-ALGEBRA-B14-SOURCE-NOTE-0003

[Source L10431](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L10431) — lemma-geometrically-reduced-finite-purely-inseparable-extension.

```tex
\item $k^{1/p} \otimes_k S$ is reduced,
```

L'énoncé commence par un corps k quelconque, tandis que k^{1/p} n'a été défini localement que pour k de caractéristique p premier. En caractéristique nulle, ce symbole demande une convention supplémentaire, par exemple k^{1/p}=k, ou un énoncé distinct de ce critère. La perfection en caractéristique nulle est ensuite traitée explicitement. Observation de portée notationnelle, non réfutation des critères de réduction ; une convention ailleurs dans l'ouvrage pourrait la résoudre. Aucune convention nouvelle n'est insérée dans la traduction.

Confiance éditoriale : modérée, conditionnelle à une convention non établie ; appréciation motivée, non probabilité calibrée. Source conservée, aucune nouvelle admission revendiquée.

## Contrôles et suite

Les 409 régions mathématiques du lot concordent exactement, sans exception nouvelle. Le préfixe contient 7 565 régions ; ses vingt et une exceptions linguistiques sont toutes antérieures. Le lot brut est égal ; le préfixe brut reste différent et ne passe qu’avec ces exceptions exactes.

Aucune citation bibliographique ni titre optionnel de lemme dans ce lot. Les renvois interchapitres sont préservés. Labels, références, contrôles TeX, environnements et items concordent. Les régions mathématiques du fichier français entier restent inchangées depuis le lot 13. Les opérations inverses retrouvent exactement ce lot puis le témoin public conservé.

Les 374 paires couvrent le préfixe sans lacune ni chevauchement ; les octets avant ce lot et ceux du suffixe non relu sont préservés. La validation structurelle complète la lecture sémantique, elle ne la remplace pas.

Prochaine lecture : Homéomorphismes universels, anglais L10604 / français L10559. Aucun nouveau PDF ni publication, aucune certification globale du chapitre ou de l’édition.

