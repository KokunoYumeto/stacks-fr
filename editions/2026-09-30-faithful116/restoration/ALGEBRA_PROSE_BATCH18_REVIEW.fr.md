# Autres anneaux noethériens

## Résultat et portée

Une section entièrement comparée : anglais L12149–12345 (197 lignes), français L12078–12251 (174 lignes), soit huit paires complètes avec preuves et transitions. 103 occurrences sont reliées à des choix contextualisés. La lecture continue atteint 51 sections, 440 paires et 3653 occurrences ; ni le chapitre ni l’édition ne sont terminés.

Deux constructions françaises défectueuses sont corrigées en R-sous-modules ; idéal non unité devient idéal propre. Ces trois opérations réparent la grammaire et le registre, sans changer les résultats, les formules ou les références. Les preuves complètes d’Artin-Rees, de l’intersection de Krull et d’Artin-Tate ont été comparées.

Aucune proposition nouvelle de correction de la source dans ce lot. Les raccourcis de preuve sont explicités pour le lecteur du dossier, non complétés dans le texte traduit. Module fini reste le synonyme technique de module de type fini ; il ne signifie pas un ensemble de cardinal fini.

Lecture, corrections et dossier produits par OpenAI Codex, sans relecture humaine. Les instructions demandent Ultra ; l’identifiant exact du modèle de cette reprise n’est pas attesté par une métadonnée consultée dans ce lot. Ne pas lui attribuer automatiquement le modèle d’un lot antérieur. Les attestations sont consultées rétrospectivement.

Autorité : commit a04446e57ec1fbc252a871afcec7752fb2807b14, SHA-256 FA8BB92E58A4F78A2BD01B3B6A4A87DE0A0D279F5DD90641B574DD5FBFFFA4F3.
[LaTeX restauré](staged/fr/010_algebra.prose-batch18.fr.tex) · [État français précédent](staged/fr/010_algebra.prose-batch17.fr.tex) · [Lot précédent](ALGEBRA_PROSE_BATCH17_REVIEW.fr.md).
[Validation](ALGEBRA_PROSE_BATCH18_VALIDATION.json) · [Choix](ALGEBRA_PROSE_BATCH18_CHOICES.json) · [Occurrences](ALGEBRA_PROSE_BATCH18_OCCURRENCES.json) · [Avant/après](ALGEBRA_PROSE_BATCH18_REPAIRS.json) · [Connecteur en formule](ALGEBRA_PROSE_BATCH18_MATH_EXCEPTIONS.json) · [Libellés bibliographiques](ALGEBRA_PROSE_BATCH18_CITATION_EXCEPTIONS.json) · [Titre facultatif](ALGEBRA_PROSE_BATCH18_HEADER_EXCEPTIONS.json) · [Couverture](ALGEBRA_PROSE_BATCH18_COVERAGE.json) · [Observations séparées](ALGEBRA_PROSE_BATCH18_SOURCE_OBSERVATIONS.json).

## Canon effectivement consulté

### Antoine Ducros — Introduction à la théorie des schémas

[Source consultée](https://webusers.imj-prg.fr/~antoine.ducros/Cours-schemas.pdf) · [Fichier conservé](canon-consulted/fr-algebra/ducros-cours-schemas.pdf)

Pages 25,26,82,83 entièrement lues ; §§0.1.8.2, 0.2.2–0.2.6, 2.3.2–2.3.5. Page 26 rendue avec Poppler et inspectée.

Attestations courtes : « anneau noethérien », « sous-module », « de type fini », « de présentation finie », « Lemme de Nakayama ».

Appuie la construction R-sous-module, la différence entre type fini et présentation finie, les sommes directes et l'usage du lemme de Nakayama.

Limites : Les pages n'attestent pas le nom français du théorème d'intersection de Krull ni radical de Jacobson. Consultation rétrospective, non relecture humaine.

SHA-256 : 8F47303A58CCB5412F7ED5AAFD154CD87A31FB11903DA362CC8823D050066F66.

### Jean-François Dat — Algèbre ENS 2016–2017

[Source consultée](https://webusers.imj-prg.fr/~jean-francois.dat/enseignement/AlgebreM1/ENS1617.pdf) · [Fichier conservé](canon-consulted/fr-algebra/dat-algebre-ens1617.pdf)

Page 8 entièrement lue, théorème de Dedekind et discussion des idéaux premiers.

Attestations courtes : « idéal propre non nul ».

Atteste propre pour un idéal strictement distinct de l'anneau ; non nul est une qualification supplémentaire distincte.

Limites : La situation arithmétique de la page n'est pas importée dans les lemmes noethériens. Consultation rétrospective.

SHA-256 : DB5B7FD8139D62C37D0DDDDC90EF22D3EDCF74CC663C5267815E4EA3CECBBB18.

## Les trois corrections françaises

### FR-ALGEBRA-B18-REPAIR-0001

Anglais L12158 ; français L12087.

Avant :
```tex
La condition de chaîne ascendante est satisfaite pour les sous-modules
$R$-d'un $R$-module fini.
```

Après :
```tex
La condition de chaîne ascendante est satisfaite pour les
$R$-sous-modules d'un $R$-module fini.
```

Réparation grammaticale de deux expressions seulement. Module fini est conservé comme synonyme technique de type fini ; l'argument ne parle pas d'un cardinal fini.

### FR-ALGEBRA-B18-REPAIR-0002

Anglais L12182 ; français L12111.

Avant :
```tex
sous-modules $R$ de $M$ est équivalente à la condition que tout sous-module
```

Après :
```tex
$R$-sous-modules de $M$ est équivalente à la condition que tout sous-module
```

Réparation grammaticale de deux expressions seulement. Module fini est conservé comme synonyme technique de type fini ; l'argument ne parle pas d'un cardinal fini.

### FR-ALGEBRA-B18-REPAIR-0003

Anglais L12285 ; français L12213.

Avant :
```tex
que $\bigcap_n I^n = (0)$ lorsque $I \subset R$ est un idéal non unité dans un
```

Après :
```tex
que $\bigcap_n I^n = (0)$ lorsque $I \subset R$ est un idéal propre dans un
```

Idéal propre signifie strictement distinct de l'anneau, non idéal ne contenant aucun élément ni idéal non principal.

## Règles contextualisées

### FR-ALGEBRA-B18-RULE-MODULE

Module fini signifie type fini dans ce texte. Distinguer cette finitude de la présentation finie et de la finitude comme algèbre.

Canon : FR-ALGEBRA-B18-CANON-DUCROS.

### FR-ALGEBRA-B18-RULE-NOETHER

La condition noethérienne est sur l'anneau ; son emploi pour les sous-modules et la finitude est vérifié dans chaque preuve.

Canon : FR-ALGEBRA-B18-CANON-DUCROS.

### FR-ALGEBRA-B18-RULE-IDEAL

Idéal propre traduit non-unit ideal. Radical de Jacobson est conservé avec justification source, sans attestation externe nouvelle revendiquée.

Canon : FR-ALGEBRA-B18-CANON-DAT.

### FR-ALGEBRA-B18-RULE-EXACT

Vérifier la portée de l'exactitude, l'image et l'image inverse ; ne pas ajouter une surjectivité finale absente.

Canon : FR-ALGEBRA-B18-CANON-DUCROS.

### FR-ALGEBRA-B18-RULE-LOGIC

Portée des quantificateurs, dépendance des choix et comparaisons relues dans chaque passage.

Canon : Comparaison source et justification directe ; pas d’attestation externe nouvelle.

### FR-ALGEBRA-B18-RULE-NAMED

Les noms propres restent identiques ; seul le libellé descriptif du théorème de Krull est traduit. Ducros atteste Nakayama, pas tous ces intitulés.

Canon : FR-ALGEBRA-B18-CANON-DUCROS.

### FR-ALGEBRA-B18-RULE-GENERATORS

Les générateurs de modules et d'algèbres restent distincts ; le degré homogène ne remplace pas un indice de générateur.

Canon : FR-ALGEBRA-B18-CANON-DUCROS.

## Passages parallèles complets

### 01 — section-Noetherian-again

Anglais L12149–12152 ; français L12078–12081.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12149) · FR-ALGEBRA-B18-CHOICE-0001.

Autres anneaux noethériens traduit le titre de reprise sans annoncer une classe différente. L'orthographe noethérien est attestée par Ducros. Toutes les transitions de la section sont incluses dans les paires.

Règles : FR-ALGEBRA-B18-RULE-NOETHER.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\section{More Noetherian rings}
\label{section-Noetherian-again}
```

Français restauré :
```tex
\section{Autres anneaux noethériens}
\label{section-Noetherian-again}
```

</details>

### 02 — lemma-Noetherian-basic

Anglais L12153–12185 ; français L12082–12114.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12153) · FR-ALGEBRA-B18-CHOICE-0002.

Les trois assertions distinguent présentation finie, finitude des sous-modules et condition de chaîne ascendante. Module fini est conservé dans le sens technique de module de type fini, non d'ensemble fini. Deux constructions grammaticales défectueuses sous-modules R sont réparées en R-sous-modules. La preuve complète conserve la récurrence, les suites exactes, les nombres de générateurs et le recours au noyau de la présentation. L'équivalence finale et la démonstration omise restent telles quelles.

Point particulier à relire : Réparation grammaticale de deux expressions seulement. Module fini est conservé comme synonyme technique de type fini ; l'argument ne parle pas d'un cardinal fini.

Règles : FR-ALGEBRA-B18-RULE-MODULE, FR-ALGEBRA-B18-RULE-NOETHER, FR-ALGEBRA-B18-RULE-IDEAL, FR-ALGEBRA-B18-RULE-EXACT, FR-ALGEBRA-B18-RULE-LOGIC, FR-ALGEBRA-B18-RULE-GENERATORS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-Noetherian-basic}
Let $R$ be a Noetherian ring.
Any finite $R$-module is of finite presentation.
Any submodule of a finite $R$-module is finite.
The ascending chain condition holds for $R$-submodules
of a finite $R$-module.
\end{lemma}

\begin{proof}
We first show that any submodule $N$ of a finite $R$-module
$M$ is finite. We do this by induction on the number of
generators of $M$. If this number is $1$, then $N = J/I \subset
M = R/I$ for some ideals $I \subset J \subset R$. Thus the definition
of Noetherian implies the result. If the number of generators of
$M$ is greater than $1$, then we can find a short exact sequence
$0 \to M' \to M \to M'' \to 0$ where $M'$ and $M''$ have fewer
generators. Note that setting $N' = M' \cap N$ and $N'' = \Im(N \to
M'')$ gives a similar short exact sequence for $N$. Hence the result
follows from the induction hypothesis
since the number of generators of $N$ is at most the number of
generators of $N'$ plus the number of generators of $N''$.

\medskip\noindent
To show that $M$ is finitely presented just apply the previous result
to the kernel of a presentation $R^n \to M$.

\medskip\noindent
It is well known and easy to prove that the ascending chain condition for
$R$-submodules of $M$ is equivalent to the condition that every submodule
of $M$ is a finite $R$-module. We omit the proof.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-Noetherian-basic}
Soit $R$ un anneau noethérien.
Tout $R$-module fini est de présentation finie.
Tout sous-module d'un $R$-module fini est fini.
La condition de chaîne ascendante est satisfaite pour les
$R$-sous-modules d'un $R$-module fini.
\end{lemma}

\begin{proof}
Montrons d'abord que tout sous-module $N$ d'un $R$-module fini
$M$ est fini. Nous procédons par récurrence sur le nombre de
générateurs de $M$. Si ce nombre vaut $1$, alors $N = J/I \subset
M = R/I$ pour certains idéaux $I \subset J \subset R$. Ainsi la définition
de noethérien donne le résultat. Si le nombre de générateurs de
$M$ est supérieur à $1$, nous pouvons trouver une suite exacte courte
$0 \to M' \to M \to M'' \to 0$ où $M'$ et $M''$ ont moins de
générateurs. Remarquons qu'en posant $N' = M' \cap N$ et
$N'' = \Im(N \to M'')$, nous obtenons une suite exacte courte analogue pour $N$.
Le résultat découle donc de l'hypothèse de récurrence
puisque le nombre de générateurs de $N$ est au plus le nombre de
générateurs de $N'$ plus le nombre de générateurs de $N''$.

\medskip\noindent
Pour montrer que $M$ est de présentation finie, il suffit d'appliquer le résultat précédent
au noyau d'une présentation $R^n \to M$.

\medskip\noindent
Il est bien connu et facile de démontrer que la condition de chaîne ascendante pour les
$R$-sous-modules de $M$ est équivalente à la condition que tout sous-module
de $M$ soit un $R$-module fini. Nous omettons la démonstration.
\end{proof}
```

</details>

### 03 — lemma-Artin-Rees

Anglais L12186–12219 ; français L12115–12148.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12186) · FR-ALGEBRA-B18-CHOICE-0003.

Artin-Rees, la constante c>0 et tous les exposants restent inchangés. La preuve construit un anneau puis un module gradués, les distingue et décompose les générateurs en composantes homogènes. Le choix c=max d_j peut être augmenté pour obtenir c>0 et le cas du module nul est implicite ; aucun détail nouveau n'est ajouté à la traduction. La relation d'inclusion finale est conservée dans son sens original.

Point particulier à relire : La constante peut être augmentée au besoin ; le cas nul est implicite. Ces raccourcis de preuve ne sont ni complétés silencieusement ni comptés comme erreurs du théorème.

Règles : FR-ALGEBRA-B18-RULE-MODULE, FR-ALGEBRA-B18-RULE-NOETHER, FR-ALGEBRA-B18-RULE-IDEAL, FR-ALGEBRA-B18-RULE-LOGIC, FR-ALGEBRA-B18-RULE-NAMED, FR-ALGEBRA-B18-RULE-GENERATORS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}[Artin-Rees]
\label{lemma-Artin-Rees}
Suppose that $R$ is Noetherian, $I \subset R$ an ideal.
Let $N \subset M$ be finite $R$-modules.
There exists a constant $c > 0$ such that
$I^n M \cap N  =  I^{n-c}(I^cM \cap N)$ for all $n \geq c$.
\end{lemma}

\begin{proof}
Consider the ring $S = R \oplus I \oplus I^2 \oplus \ldots
= \bigoplus_{n \geq 0} I^n$. Convention: $I^0 = R$.
Multiplication maps $I^n \times I^m$
into $I^{n + m}$ by multiplication in $R$.
Note that if $I = (f_1, \ldots, f_t)$
then $S$ is a quotient of the Noetherian ring $R[X_1, \ldots, X_t]$.
The map just sends the monomial $X_1^{e_1}\ldots X_t^{e_t}$
to $f_1^{e_1}\ldots f_t^{e_t}$. Thus $S$ is Noetherian.
Similarly, consider the module $M \oplus IM \oplus I^2M \oplus \ldots
= \bigoplus_{n \geq 0} I^nM$. This is a finitely generated $S$-module.
Namely, if $x_1, \ldots, x_r$ generate $M$ over $R$, then they also generate
$\bigoplus_{n \geq 0} I^nM$ over $S$. Next, consider the
submodule $\bigoplus_{n \geq 0} I^nM \cap N$.
This is an $S$-submodule, as is easily verified. By
Lemma \ref{lemma-Noetherian-basic} it is finitely generated as
an $S$-module,
say by $\xi_j \in \bigoplus_{n \geq 0} I^nM \cap N$, $j = 1, \ldots, s$.
We may assume by decomposing each $\xi_j$ into its homogeneous
pieces that each $\xi_j \in I^{d_j}M \cap N$ for some $d_j$.
Set $c = \max\{d_j\}$. Then for all $n \geq c$ every element
in $I^nM \cap N$ is of the form $\sum h_j \xi_j$ with
$h_j \in I^{n - d_j}$. The lemma now follows from this and the trivial
observation that $I^{n-d_j}(I^{d_j}M \cap N) \subset I^{n-c}(I^cM \cap N)$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}[Artin-Rees]
\label{lemma-Artin-Rees}
Supposons que $R$ soit noethérien et que $I \subset R$ soit un idéal.
Soient $N \subset M$ des $R$-modules finis.
Il existe une constante $c > 0$ telle que
$I^n M \cap N  =  I^{n-c}(I^cM \cap N)$ pour tout $n \geq c$.
\end{lemma}

\begin{proof}
Considérons l'anneau $S = R \oplus I \oplus I^2 \oplus \ldots
= \bigoplus_{n \geq 0} I^n$. Convention : $I^0 = R$.
La multiplication envoie $I^n \times I^m$
dans $I^{n + m}$ par la multiplication dans $R$.
Remarquons que si $I = (f_1, \ldots, f_t)$,
alors $S$ est un quotient de l'anneau noethérien $R[X_1, \ldots, X_t]$.
L'application envoie simplement le monôme $X_1^{e_1}\ldots X_t^{e_t}$
sur $f_1^{e_1}\ldots f_t^{e_t}$. Ainsi $S$ est noethérien.
De même, considérons le module $M \oplus IM \oplus I^2M \oplus \ldots
= \bigoplus_{n \geq 0} I^nM$. C'est un $S$-module de type fini.
En effet, si $x_1, \ldots, x_r$ engendrent $M$ sur $R$, ils engendrent aussi
$\bigoplus_{n \geq 0} I^nM$ sur $S$. Ensuite, considérons le
sous-module $\bigoplus_{n \geq 0} I^nM \cap N$.
Il s'agit d'un $S$-sous-module, comme on le vérifie facilement. Par le
Lemme \ref{lemma-Noetherian-basic}, il est de type fini comme
$S$-module,
disons engendré par $\xi_j \in \bigoplus_{n \geq 0} I^nM \cap N$, $j = 1, \ldots, s$.
Nous pouvons supposer, en décomposant chaque $\xi_j$ en ses composantes homogènes,
que $\xi_j \in I^{d_j}M \cap N$ pour un certain $d_j$.
Posons $c = \max\{d_j\}$. Alors, pour tout $n \geq c$, tout élément
de $I^nM \cap N$ est de la forme $\sum h_j \xi_j$ avec
$h_j \in I^{n - d_j}$. Le lemme résulte alors de cette observation et du fait trivial que
$I^{n-d_j}(I^{d_j}M \cap N) \subset I^{n-c}(I^cM \cap N)$.
\end{proof}
```

</details>

### 04 — lemma-map-AR

Anglais L12220–12239 ; français L12149–12168.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12220) · FR-ALGEBRA-B18-CHOICE-0004.

La suite est exacte mais n'est pas affirmée surjective sur N. La première relation est une égalité d'images inverses et la seconde une inclusion dans l'image de I^{n−c}M : elles ne sont pas interverties. La conjonction and devient et dans la formule sans changer celle-ci. Le recours à l'image de f et la surjectivité du morphisme restreint sont complets.

Point particulier à relire : La suite se termine à N sans flèche N→0 ; ne pas fabriquer une suite exacte courte.

Règles : FR-ALGEBRA-B18-RULE-MODULE, FR-ALGEBRA-B18-RULE-NOETHER, FR-ALGEBRA-B18-RULE-IDEAL, FR-ALGEBRA-B18-RULE-EXACT, FR-ALGEBRA-B18-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-map-AR}
Suppose that $0 \to K \to M \xrightarrow{f} N$ is an
exact sequence of finitely generated modules
over a Noetherian ring $R$. Let $I \subset R$ be an ideal.
Then there exists a $c$ such that
$$
f^{-1}(I^nN) = K + I^{n-c}f^{-1}(I^cN)
\quad\text{and}\quad
f(M) \cap I^nN \subset f(I^{n - c}M)
$$
for all $n \geq c$.
\end{lemma}

\begin{proof}
Apply Lemma \ref{lemma-Artin-Rees} to
$\Im(f) \subset N$ and note that
$f : I^{n-c}M \to I^{n-c}f(M)$ is surjective.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-map-AR}
Supposons que $0 \to K \to M \xrightarrow{f} N$ soit une
suite exacte de modules de type fini
sur un anneau noethérien $R$. Soit $I \subset R$ un idéal.
Alors il existe un $c$ tel que
$$
f^{-1}(I^nN) = K + I^{n-c}f^{-1}(I^cN)
\quad\text{et}\quad
f(M) \cap I^nN \subset f(I^{n - c}M)
$$
pour tout $n \geq c$.
\end{lemma}

\begin{proof}
Appliquer le Lemme \ref{lemma-Artin-Rees} à
$\Im(f) \subset N$ et remarquer que
$f : I^{n-c}M \to I^{n-c}f(M)$ est surjectif.
\end{proof}
```

</details>

### 05 — lemma-intersect-powers-ideal-module-zero

Anglais L12240–12255 ; français L12169–12184.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12240) · FR-ALGEBRA-B18-CHOICE-0005.

Le titre facultatif Krull's intersection theorem est traduit par théorème d'intersection de Krull ; l'identifiant et la référence n'en dépendent pas. R reste local noethérien, I propre et M de type fini. L'intersection est nulle par Artin-Rees et Nakayama ; le français conserve les étapes N=I^nM∩N et N inclus dans IN. L'intitulé français est une traduction descriptive, non une nouvelle attestation verbatim attribuée au canon lu.

Point particulier à relire : Titre traduit, pas de renommage d'identifiant. L'intitulé est justifié descriptivement ; pas de preuve d'attestation française de ce nom dans les pages consultées.

Règles : FR-ALGEBRA-B18-RULE-MODULE, FR-ALGEBRA-B18-RULE-NOETHER, FR-ALGEBRA-B18-RULE-IDEAL, FR-ALGEBRA-B18-RULE-LOGIC, FR-ALGEBRA-B18-RULE-NAMED.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}[Krull's intersection theorem]
\label{lemma-intersect-powers-ideal-module-zero}
Let $R$ be a Noetherian local ring. Let $I \subset R$ be
a proper ideal. Let $M$ be a finite $R$-module.
Then $\bigcap_{n \geq 0} I^nM = 0$.
\end{lemma}

\begin{proof}
Let $N = \bigcap_{n \geq 0} I^nM$.
Then $N = I^nM \cap N$ for all $n \geq 0$.
By the Artin-Rees Lemma \ref{lemma-Artin-Rees}
we see that $N = I^nM \cap N \subset IN$ for
some suitably large $n$. By Nakayama's Lemma \ref{lemma-NAK}
we see that $N = 0$.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}[théorème d'intersection de Krull]
\label{lemma-intersect-powers-ideal-module-zero}
Soit $R$ un anneau local noethérien. Soit $I \subset R$ un
idéal propre. Soit $M$ un $R$-module fini.
Alors $\bigcap_{n \geq 0} I^nM = 0$.
\end{lemma}

\begin{proof}
Soit $N = \bigcap_{n \geq 0} I^nM$.
Alors $N = I^nM \cap N$ pour tout $n \geq 0$.
Par le Lemme d'Artin-Rees \ref{lemma-Artin-Rees},
nous voyons que $N = I^nM \cap N \subset IN$
pour un certain $n$ suffisamment grand. Par le Lemme de Nakayama
\ref{lemma-NAK}, nous avons $N = 0$.
\end{proof}
```

</details>

### 06 — lemma-intersection-powers-ideal-module

Anglais L12256–12281 ; français L12185–12209.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12256) · FR-ALGEBRA-B18-CHOICE-0006.

R n'est plus supposé local. La première assertion fournit, pour chaque premier contenant I, un élément f extérieur au premier, puis l'annulation de N_f ; elle n'affirme pas un choix universel de f. La seconde demande I dans le radical de Jacobson. La finitude de N, les localisations puis le produit des g_i sont conservés. Radical de Jacobson est ici maintenu d'après la source et les conventions du chapitre ; pas d'attestation lexicale nouvelle prétendue.

Point particulier à relire : Le français conserve la dépendance de f envers le premier ; aucune commutation indue de l'intersection infinie et de la localisation n'est affirmée.

Règles : FR-ALGEBRA-B18-RULE-MODULE, FR-ALGEBRA-B18-RULE-NOETHER, FR-ALGEBRA-B18-RULE-IDEAL, FR-ALGEBRA-B18-RULE-EXACT, FR-ALGEBRA-B18-RULE-LOGIC, FR-ALGEBRA-B18-RULE-GENERATORS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}
\label{lemma-intersection-powers-ideal-module}
Let $R$ be a Noetherian ring. Let $I \subset R$ be an ideal.
Let $M$ be a finite $R$-module. Let $N = \bigcap_n I^n M$.
\begin{enumerate}
\item For every prime $\mathfrak p$, $I \subset \mathfrak p$ there
exists a $f \in R$, $f \not \in \mathfrak p$ such that $N_f = 0$.
\item If $I$ is contained in the Jacobson radical
of $R$, then $N = 0$.
\end{enumerate}
\end{lemma}

\begin{proof}
Proof of (1). Let $x_1, \ldots, x_n$ be generators for the module $N$,
see Lemma \ref{lemma-Noetherian-basic}. For every prime
$\mathfrak p$, $I \subset \mathfrak p$ we see that
the image of $N$ in the localization $M_{\mathfrak p}$
is zero, by Lemma \ref{lemma-intersect-powers-ideal-module-zero}.
Hence we can find $g_i \in R$, $g_i \not \in \mathfrak p$
such that $x_i$ maps to zero in $N_{g_i}$. Thus
$N_{g_1g_2\ldots g_n} = 0$.

\medskip\noindent
Part (2) follows from (1) and Lemma \ref{lemma-characterize-zero-local}.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}
\label{lemma-intersection-powers-ideal-module}
Soit $R$ un anneau noethérien. Soit $I \subset R$ un idéal.
Soit $M$ un $R$-module fini. Soit $N = \bigcap_n I^n M$.
\begin{enumerate}
\item Pour tout idéal premier $\mathfrak p$, $I \subset \mathfrak p$, il
existe un $f \in R$, $f \not \in \mathfrak p$, tel que $N_f = 0$.
\item Si $I$ est contenu dans le radical de Jacobson
de $R$, alors $N = 0$.
\end{enumerate}
\end{lemma}

\begin{proof}
Démontrons (1). Soient $x_1, \ldots, x_n$ des générateurs du module $N$,
voir le Lemme \ref{lemma-Noetherian-basic}. Pour tout idéal premier
$\mathfrak p$, $I \subset \mathfrak p$, l'image de $N$ dans la localisation $M_{\mathfrak p}$
est nulle, par le Lemme \ref{lemma-intersect-powers-ideal-module-zero}.
Nous pouvons donc trouver $g_i \in R$, $g_i \not \in \mathfrak p$
tel que $x_i$ s'envoie sur zéro dans $N_{g_i}$. Ainsi
$N_{g_1g_2\ldots g_n} = 0$.

\medskip\noindent
La partie (2) découle de (1) et du Lemme \ref{lemma-characterize-zero-local}.
\end{proof}
```

</details>

### 07 — remark-intersection-powers-ideal

Anglais L12282–12295 ; français L12210–12223.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12282) · FR-ALGEBRA-B18-CHOICE-0007.

Non-unit ideal signifie un idéal distinct de R, donc idéal propre, terme attesté par Dat. Idéal non unité est remplacé pour éviter un calque obscur. L'élément f appartient à toutes les puissances ; l'élément g dépend du premier. Le voisinage ouvert de V(I) et la traduction géométrique de l'annulation locale sont conservés, sans les confondre avec l'annulation sur tout le spectre.

Point particulier à relire : Idéal propre signifie strictement distinct de l'anneau, non idéal ne contenant aucun élément ni idéal non principal.

Règles : FR-ALGEBRA-B18-RULE-NOETHER, FR-ALGEBRA-B18-RULE-IDEAL, FR-ALGEBRA-B18-RULE-LOGIC.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{remark}
\label{remark-intersection-powers-ideal}
Lemma \ref{lemma-intersect-powers-ideal-module-zero} in particular implies
that $\bigcap_n I^n = (0)$ when $I \subset R$ is a non-unit ideal in a
Noetherian local ring $R$. More generally, let $R$ be a Noetherian ring and
$I \subset R$ an ideal. Suppose that $f \in \bigcap_{n \in \mathbf{N}} I^n$.
Then Lemma \ref{lemma-intersection-powers-ideal-module}
says that for every prime ideal $I \subset \mathfrak p$
there exists a $g \in R$, $g \not \in \mathfrak p$
such that $f$ maps to zero in $R_g$. In algebraic geometry we
express this by saying that ``$f$ is zero in an open neighbourhood
of the closed set $V(I)$ of $\Spec(R)$''.
\end{remark}
```

Français restauré :
```tex
\begin{remark}
\label{remark-intersection-powers-ideal}
Le Lemme \ref{lemma-intersect-powers-ideal-module-zero} implique en particulier
que $\bigcap_n I^n = (0)$ lorsque $I \subset R$ est un idéal propre dans un
anneau local noethérien $R$. Plus généralement, soit $R$ un anneau noethérien et
$I \subset R$ un idéal. Supposons que $f \in \bigcap_{n \in \mathbf{N}} I^n$.
Alors le Lemme \ref{lemma-intersection-powers-ideal-module}
dit que, pour tout idéal premier $I \subset \mathfrak p$,
il existe un $g \in R$, $g \not \in \mathfrak p$,
tel que $f$ s'envoie sur zéro dans $R_g$. En géométrie algébrique, nous
exprimons cela en disant que « $f$ est nul dans un voisinage ouvert
de l'ensemble fermé $V(I)$ de $\Spec(R)$ ».
\end{remark}
```

</details>

### 08 — lemma-Artin-Tate

Anglais L12296–12345 ; français L12224–12251.
[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L12296) · FR-ALGEBRA-B18-CHOICE-0008.

La finitude comme algèbre et celle comme module sont distinguées à chaque occurrence. S est une R-algèbre de type fini et un T-module de type fini ; c'est T qui doit devenir de type fini sur R. Les coefficients a_ij et b_ijk, la sous-algèbre T′, la présentation de S′, les générateurs 1,Y_i et la surjectivité sont conservés. Le x_j de la dernière partie est conservé comme dans l'anglais ; aucune renumérotation silencieuse. La conclusion finit par T fini sur T′ noethérien.

Point particulier à relire : Fini sur T′ se rapporte à la structure de module. De type fini sur R dans la conclusion désigne l'algèbre ; pas de glissement de sens.

Règles : FR-ALGEBRA-B18-RULE-MODULE, FR-ALGEBRA-B18-RULE-NOETHER, FR-ALGEBRA-B18-RULE-EXACT, FR-ALGEBRA-B18-RULE-LOGIC, FR-ALGEBRA-B18-RULE-NAMED, FR-ALGEBRA-B18-RULE-GENERATORS.

<details>
<summary>Lire les deux passages complets</summary>

Anglais officiel :
```tex
\begin{lemma}[Artin-Tate]
\label{lemma-Artin-Tate}
Let $R$ be a Noetherian ring. Let $S$ be a finitely
generated $R$-algebra. If $T \subset S$ is an $R$-subalgebra such
that $S$ is finitely generated as a $T$-module, then $T$ is of
finite type over $R$.
\end{lemma}

\begin{proof}
Choose elements $x_1, \ldots, x_n \in S$ which generate $S$ as an $R$-algebra.
Choose $y_1, \ldots, y_m$ in $S$ which generate $S$ as a $T$-module.
Thus there exist $a_{ij} \in T$ such that
$x_i = \sum a_{ij} y_j$. There also exist $b_{ijk} \in T$ such
that $y_i y_j = \sum b_{ijk} y_k$. Let $T' \subset T$ be the
sub $R$-algebra generated by $a_{ij}$ and $b_{ijk}$. This is a finitely
generated $R$-algebra, hence Noetherian. Consider the algebra
$$
S' = T'[Y_1, \ldots, Y_m]/(Y_i Y_j - \sum b_{ijk} Y_k).
$$
Note that $S'$ is finite over $T'$, namely as a $T'$-module it is
generated by the classes of $1, Y_1, \ldots, Y_m$.
Consider the $T'$-algebra homomorphism $S' \to S$ which maps
$Y_i$ to $y_i$. Because $a_{ij} \in T'$ we see that $x_j$ is
in the image of this map. Thus $S' \to S$ is surjective.
Therefore $S$ is finite over $T'$ as well. Since $T'$ is Noetherian
we conclude that $T \subset S$ is finite over $T'$ and
we win.
\end{proof}
```

Français restauré :
```tex
\begin{lemma}[Artin-Tate]
\label{lemma-Artin-Tate}
Soit $R$ un anneau noethérien. Soit $S$ une $R$-algèbre
de type fini. Si $T \subset S$ est une $R$-sous-algèbre telle que
$S$ soit de type fini comme $T$-module, alors $T$ est de
type fini sur $R$.
\end{lemma}

\begin{proof}
Choisissons des éléments $x_1, \ldots, x_n \in S$ qui engendrent $S$ comme $R$-algèbre.
Choisissons $y_1, \ldots, y_m$ dans $S$ qui engendrent $S$ comme $T$-module.
Il existe donc des $a_{ij} \in T$ tels que
$x_i = \sum a_{ij} y_j$. Il existe également des $b_{ijk} \in T$ tels
que $y_i y_j = \sum b_{ijk} y_k$. Soit $T' \subset T$ la
$R$-sous-algèbre engendrée par les $a_{ij}$ et $b_{ijk}$. Il s'agit d'une $R$-algèbre
de type fini, donc noethérienne. Considérons l'algèbre
$$
S' = T'[Y_1, \ldots, Y_m]/(Y_i Y_j - \sum b_{ijk} Y_k).
$$
Remarquons que $S'$ est fini sur $T'$, car en tant que $T'$-module il est
engendré par les classes de $1, Y_1, \ldots, Y_m$.
Considérons l'homomorphisme de $T'$-algèbres $S' \to S$ qui envoie
$Y_i$ sur $y_i$. Comme $a_{ij} \in T'$, nous voyons que $x_j$ appartient à l'image de cette application. Ainsi $S' \to S$ est surjectif.
Par conséquent, $S$ est également fini sur $T'$. Comme $T'$ est noethérien,
nous concluons que $T \subset S$ est fini sur $T'$ et nous avons terminé.
\end{proof}
```

</details>

## Contrôles et suite

Les 167 régions mathématiques du lot concordent après une traduction exacte and→et. Le préfixe compte 8 807 régions et vingt-six exceptions linguistiques exactes, dont vingt-cinq antérieures. L’égalité brute sans ces exceptions n’est pas revendiquée.

Le titre facultatif Krull’s intersection theorem est traduit par théorème d’intersection de Krull ; cette différence est isolée dans le registre des titres, non assimilée à une clé bibliographique. Les deux noms Artin-Rees et Artin-Tate restent identiques. Il n’y a pas de citation bibliographique dans ce lot. Labels, renvois, clés bibliographiques du fichier entier, entrées, contrôles TeX, environnements et items sont préservés. Aucune région mathématique du français entier ne change depuis le lot précédent.

Les opérations inverses retrouvent le lot précédent puis le témoin public conservé. Les octets du préfixe déjà relu et ceux du suffixe encore non relu sont inchangés. Les 440 paires sont contiguës, sans lacune ni chevauchement. Les contrôles mécaniques complètent la lecture sémantique et ne la remplacent pas.

Prochaine lecture : Longueur, anglais L12346 / français L12252. Aucun nouveau PDF, aucune publication et aucune certification globale du chapitre ou de l’édition dans ce lot.

