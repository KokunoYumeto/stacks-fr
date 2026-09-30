# Topologies sur les espaces : lectures officielles rétablies

**LaTeX local ; aucune édition publique corrigée à ce stade.**

[LaTeX](staged/fr/073_spaces-topologies.fr.tex) · [Contrôles](SPACES-TOPOLOGIES_FR_VALIDATION.json) · [Contextes complets](SPACES-TOPOLOGIES_FR_REPAIRS.json)

Les neuf contextes candidats ont été lus dans les deux langues. Les restaurations concernent les bases, les objets et une hypothèse ajoutée dans la prose. Trois suppressions ne sont que le retrait de noms de flèches explicités par le traducteur. La correction probable d’une anomalie de la source reste proposée dans le dossier, mais ne remplace pas son texte dans la traduction diplomatique. Aucun fichier anglais officiel n’est modifié.

## FR-SPACES-TOPOLOGIES-001 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-topologies.tex#L315)

Rétablit les lettres T et S imprimées dans la définition de u. Le contexte fixe pourtant Y et X ; leur substitution était une correction de la source et non une simple traduction.

Avant :
```tex
$u(U \to Y) = (f \circ j : U \to X)$
```
Après :
```tex
$u(U \to T) = (f \circ j : U \to S)$
```

## FR-SPACES-TOPOLOGIES-002 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-topologies.tex#L446)

Rétablit i_T dans la première clause seulement ; la preuve emploie aussi i_Y et ces autres occurrences officielles restent intactes.

Avant :
```tex
\item Nous avons $i_f = f_{big} \circ i_Y$
```
Après :
```tex
\item Nous avons $i_f = f_{big} \circ i_T$
```

## FR-SPACES-TOPOLOGIES-003 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-topologies.tex#L447)

Même lecture i_T rétablie dans la désignation du morphisme de la première clause.

Avant :
```tex
le lemme \ref{lemma-put-in-T-etale} et $i_Y$
```
Après :
```tex
le lemme \ref{lemma-put-in-T-etale} et $i_T$
```

## FR-SPACES-TOPOLOGIES-004 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-topologies.tex#L449)

Rétablit le but T imprimé dans la deuxième clause, sans corriger la discordance avec Y dans la description qui suit.

Avant :
```tex
$X_{spaces, \etale} \to Y_{spaces, \etale}$
```
Après :
```tex
$X_{spaces, \etale} \to T_{spaces, \etale}$
```

## FR-SPACES-TOPOLOGIES-005 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-topologies.tex#L476)

Rétablit i_T dans l’égalité d’images inverses, en conservant la première égalité i_f=f_big composé avec i_Y telle que la source l’imprime.

Avant :
```tex
$i_f^{-1} = i_Y^{-1} \circ f_{big}^{-1}$
```
Après :
```tex
$i_f^{-1} = i_T^{-1} \circ f_{big}^{-1}$
```

## FR-SPACES-TOPOLOGIES-006 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-topologies.tex#L898)

Rétablit U vers Y dans la formule du foncteur v pour la topologie fppf. U vers X est mieux typé, mais modifie le témoin officiel.

Avant :
```tex
(U \to X) \longmapsto (U \times_X Y \to Y).
```
Après :
```tex
(U \to Y) \longmapsto (U \times_X Y \to Y).
```

## FR-SPACES-TOPOLOGIES-007 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-topologies.tex#L920)

Rétablit U/T dans la preuve d’adjonction (fppf), sans substituer silencieusement la base Y.

Avant :
```tex
pour $U/Y$ et $V/X$
```
Après :
```tex
pour $U/T$ et $V/X$
```

## FR-SPACES-TOPOLOGIES-008 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-topologies.tex#L1153)

Rétablit U vers Y dans la formule du foncteur v pour la topologie ph. U vers X est mieux typé, mais modifie le témoin officiel.

Avant :
```tex
(U \to X) \longmapsto (U \times_X Y \to Y).
```
Après :
```tex
(U \to Y) \longmapsto (U \times_X Y \to Y).
```

## FR-SPACES-TOPOLOGIES-009 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-topologies.tex#L1175)

Rétablit U/T dans la preuve d’adjonction (ph), sans substituer silencieusement la base Y.

Avant :
```tex
pour $U/Y$ et $V/X$
```
Après :
```tex
pour $U/T$ et $V/X$
```

## FR-SPACES-TOPOLOGIES-010 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-topologies.tex#L960)

Retire un nom de flèche ajouté explicitement à la définition, alors que la source l’utilise ensuite sans l’introduire ici. Cette explicitation ne changeait pas la mathématique ; le retour diplomatique est distingué d’une correction d’énoncé faux.

Avant :
```tex
$\{f_i : X_i \to X\}_{i \in I}$
```
Après :
```tex
$\{X_i \to X\}_{i \in I}$
```

## FR-SPACES-TOPOLOGIES-011 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-topologies.tex#L962)

Retire un nom de flèche ajouté explicitement à la définition, alors que la source l’utilise ensuite sans l’introduire ici. Cette explicitation ne changeait pas la mathématique ; le retour diplomatique est distingué d’une correction d’énoncé faux.

Avant :
```tex
$h : U \to X$
```
Après :
```tex
$U \to X$
```

## FR-SPACES-TOPOLOGIES-012 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-topologies.tex#L963)

Retire un nom de flèche ajouté explicitement à la définition, alors que la source l’utilise ensuite sans l’introduire ici. Cette explicitation ne changeait pas la mathématique ; le retour diplomatique est distingué d’une correction d’énoncé faux.

Avant :
```tex
$\{g_j : U_j \to U\}_{j = 1, \ldots, m}$
```
Après :
```tex
$\{U_j \to U\}_{j = 1, \ldots, m}$
```

## FR-SPACES-TOPOLOGIES-013 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-topologies.tex#L986)

Rétablit la base U de ce produit fibré imprimé ; X serait la base naturelle du changement de base, mais constitue une correction.

Avant :
```tex
$\{X_i \times_X U \to U\}_{i \in I}$
```
Après :
```tex
$\{X_i \times_U U \to U\}_{i \in I}$
```

## FR-SPACES-TOPOLOGIES-014 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-topologies.tex#L1009)

Rétablit la famille X produit sur Y avec U de la dernière phrase. La famille Y produit sur X avec U utilisée plus haut reste inchangée à cet autre endroit.

Avant :
```tex
$\{Y \times_X U \to U\}$
```
Après :
```tex
$\{X \times_Y U \to U\}$
```

## FR-SPACES-TOPOLOGIES-015 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-topologies.tex#L1213)

Retire l’hypothèse plat ajoutée au début de la preuve. La platitude est présente dans l’hypothèse du lemme mais absente de cette phrase officielle ; ce renforcement ne doit pas rester une modification tacite.

Avant :
```tex
Soit $U$ un espace algébrique séparé, plat et localement de présentation finie sur $X$.
```
Après :
```tex
Soit $U$ un espace algébrique séparé et localement de présentation finie sur $X$.
```

## FR-SPACES-TOPOLOGIES-016 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-topologies.tex#L1214)

Rétablit V_i dans cette clause de la preuve, alors que le recouvrement précédent est noté U_i. La proposition de corriger V_i reste dans le dossier avant/après.

Avant :
```tex
avec $U_i$
affine.
```
Après :
```tex
avec $V_i$
affine.
```

## FR-SPACES-TOPOLOGIES-017 — Lecture officielle rétablie

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-topologies.tex#L1376)

Rétablit X comme but de la dernière famille imprimée, sans substituer silencieusement Z, qui était le but corrigé dans la traduction.

Avant :
```tex
$\{Z \times_X X_i \to Z\}$
```
Après :
```tex
$\{Z \times_X X_i \to X\}$
```

## Différences fidèles conservées

## Texte des formules vérifié

### `section-procedure`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
\textit{Spaces}/S
```
```tex
\textit{Espaces}/S
```

### `section-procedure`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
\textit{Spaces}/S
```
```tex
\textit{Espaces}/S
```

### `section-procedure`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_\tau
```
```tex
(\textit{Espaces}/S)_\tau
```

### `section-procedure`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/X)_\tau
```
```tex
(\textit{Espaces}/X)_\tau
```

### `section-procedure`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
\textit{Spaces}/S
```
```tex
\textit{Espaces}/S
```

### `section-procedure`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
\textit{Spaces}/X
```
```tex
\textit{Espaces}/X
```

### `section-procedure`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
\textit{Spaces}/S
```
```tex
\textit{Espaces}/S
```

### `lemma-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/X)_\etale
```
```tex
(\textit{Espaces}/X)_\etale
```

### `lemma-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/X)_{smooth}
```
```tex
(\textit{Espaces}/X)_{smooth}
```

### `definition-big-etale-site`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_\etale
```
```tex
(\textit{Espaces}/S)_\etale
```

### `definition-big-etale-site`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
\textit{Spaces}/S
```
```tex
\textit{Espaces}/S
```

### `definition-big-etale-site`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
\textit{Spaces}/S
```
```tex
\textit{Espaces}/S
```

### `definition-big-small-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_\etale
```
```tex
(\textit{Espaces}/S)_\etale
```

### `definition-big-small-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_\etale
```
```tex
(\textit{Espaces}/S)_\etale
```

### `definition-big-small-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/X)_\etale
```
```tex
(\textit{Espaces}/X)_\etale
```

### `definition-big-small-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_\etale
```
```tex
(\textit{Espaces}/S)_\etale
```

### `lemma-put-in-T-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_\etale
```
```tex
(\textit{Espaces}/S)_\etale
```

### `lemma-put-in-T-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
Y_{spaces, \etale} \to (\textit{Spaces}/X)_\etale
```
```tex
Y_{spaces, \etale} \to (\textit{Espaces}/X)_\etale
```

### `lemma-put-in-T-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
i_f : \Sh(Y_\etale) \longrightarrow \Sh((\textit{Spaces}/X)_\etale)
```
```tex
i_f : \Sh(Y_\etale) \longrightarrow \Sh((\textit{Espaces}/X)_\etale)
```

### `lemma-put-in-T-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/X)_\etale
```
```tex
(\textit{Espaces}/X)_\etale
```

### `lemma-put-in-T-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
u : Y_{spaces, \etale} \to (\textit{Spaces}/X)_\etale
```
```tex
u : Y_{spaces, \etale} \to (\textit{Espaces}/X)_\etale
```

### `lemma-at-the-bottom-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_\etale
```
```tex
(\textit{Espaces}/S)_\etale
```

### `lemma-at-the-bottom-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
X_{spaces, \etale} \to (\textit{Spaces}/X)_\etale
```
```tex
X_{spaces, \etale} \to (\textit{Espaces}/X)_\etale
```

### `lemma-at-the-bottom-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
\pi_X : (\textit{Spaces}/X)_\etale \longrightarrow X_{spaces, \etale}
```
```tex
\pi_X : (\textit{Espaces}/X)_\etale \longrightarrow X_{spaces, \etale}
```

### `lemma-at-the-bottom-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
i_X : \Sh(X_\etale) \longrightarrow \Sh((\textit{Spaces}/X)_\etale)
```
```tex
i_X : \Sh(X_\etale) \longrightarrow \Sh((\textit{Espaces}/X)_\etale)
```

### `lemma-at-the-bottom-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
u : X_{spaces, \etale} \to (\textit{Spaces}/X)_\etale
```
```tex
u : X_{spaces, \etale} \to (\textit{Espaces}/X)_\etale
```

### `definition-restriction-small-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
\Mor_{\Sh(X_\etale)}( \mathcal{F}|_{X_\etale}, \mathcal{G}) & = \Mor_{\Sh((\textit{Spaces}/X)_\etale)}( \mathcal{F}, i_{X, *}\mathcal{G}) \\ \Mor_{\Sh(X_\etale)}( \mathcal{G}, \mathcal{F}|_{X_\etale}) & = \Mor_{\Sh((\textit{Spaces}/X)_\etale)}( \pi_X^{-1}\mathcal{G}, \mathcal{F})
```
```tex
\Mor_{\Sh(X_\etale)}( \mathcal{F}|_{X_\etale}, \mathcal{G}) & = \Mor_{\Sh((\textit{Espaces}/X)_\etale)}( \mathcal{F}, i_{X, *}\mathcal{G}) \\ \Mor_{\Sh(X_\etale)}( \mathcal{G}, \mathcal{F}|_{X_\etale}) & = \Mor_{\Sh((\textit{Espaces}/X)_\etale)}( \pi_X^{-1}\mathcal{G}, \mathcal{F})
```

### `lemma-morphism-big-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_\etale
```
```tex
(\textit{Espaces}/S)_\etale
```

### `lemma-morphism-big-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
u : (\textit{Spaces}/Y)_\etale \longrightarrow (\textit{Spaces}/X)_\etale, \quad V/Y \longmapsto V/X
```
```tex
u : (\textit{Espaces}/Y)_\etale \longrightarrow (\textit{Espaces}/X)_\etale, \quad V/Y \longmapsto V/X
```

### `lemma-morphism-big-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
v : (\textit{Spaces}/X)_\etale \longrightarrow (\textit{Spaces}/Y)_\etale, \quad (U \to X) \longmapsto (U \times_X Y \to Y).
```
```tex
v : (\textit{Espaces}/X)_\etale \longrightarrow (\textit{Espaces}/Y)_\etale, \quad (U \to X) \longmapsto (U \times_X Y \to Y).
```

### `lemma-morphism-big-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
f_{big} : \Sh((\textit{Spaces}/Y)_\etale) \longrightarrow \Sh((\textit{Spaces}/X)_\etale)
```
```tex
f_{big} : \Sh((\textit{Espaces}/Y)_\etale) \longrightarrow \Sh((\textit{Espaces}/X)_\etale)
```

### `lemma-morphism-big-small-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_\etale
```
```tex
(\textit{Espaces}/S)_\etale
```

### `lemma-morphism-big-small-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
\xymatrix{ Y_{spaces, \etale} \ar[d]_{f_{spaces, \etale}} & (\textit{Spaces}/Y)_\etale \ar[d]^{f_{big}} \ar[l]^-{\pi_Y}\\ X_{spaces, \etale} & (\textit{Spaces}/X)_\etale \ar[l]_-{\pi_X} }
```
```tex
\xymatrix{ Y_{spaces, \etale} \ar[d]_{f_{spaces, \etale}} & (\textit{Espaces}/Y)_\etale \ar[d]^{f_{big}} \ar[l]^-{\pi_Y}\\ X_{spaces, \etale} & (\textit{Espaces}/X)_\etale \ar[l]_-{\pi_X} }
```

### `lemma-composition-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_\etale
```
```tex
(\textit{Espaces}/S)_\etale
```

### `lemma-morphism-big-small-cartesian-diagram-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_\etale
```
```tex
(\textit{Espaces}/S)_\etale
```

### `lemma-morphism-big-small-cartesian-diagram-etale`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/Y)_\etale
```
```tex
(\textit{Espaces}/Y)_\etale
```

### `remark-change-topologies-ringed`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/X)_\etale
```
```tex
(\textit{Espaces}/X)_\etale
```

### `remark-change-topologies-ringed`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/X)_\etale
```
```tex
(\textit{Espaces}/X)_\etale
```

### `remark-change-topologies-ringed`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/X)_\etale
```
```tex
(\textit{Espaces}/X)_\etale
```

### `remark-change-topologies-ringed`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/Y)_\etale \to (\textit{Spaces}/X)_\etale
```
```tex
(\textit{Espaces}/Y)_\etale \to (\textit{Espaces}/X)_\etale
```

### `remark-change-topologies-ringed`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/X)_\etale
```
```tex
(\textit{Espaces}/X)_\etale
```

### `remark-change-topologies-ringed`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/Y)_\etale
```
```tex
(\textit{Espaces}/Y)_\etale
```

### `definition-big-fppf-site`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_{fppf}
```
```tex
(\textit{Espaces}/S)_{fppf}
```

### `definition-big-fppf-site`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
\textit{Spaces}/S
```
```tex
\textit{Espaces}/S
```

### `definition-big-fppf-site`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
\textit{Spaces}/S
```
```tex
\textit{Espaces}/S
```

### `definition-big-small-fppf`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_{fppf}
```
```tex
(\textit{Espaces}/S)_{fppf}
```

### `definition-big-small-fppf`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_{fppf}
```
```tex
(\textit{Espaces}/S)_{fppf}
```

### `definition-big-small-fppf`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/X)_{fppf}
```
```tex
(\textit{Espaces}/X)_{fppf}
```

### `definition-big-small-fppf`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_{fppf}
```
```tex
(\textit{Espaces}/S)_{fppf}
```

### `lemma-morphism-big-fppf`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
u : (\textit{Spaces}/Y)_{fppf} \longrightarrow (\textit{Spaces}/X)_{fppf}, \quad V/Y \longmapsto V/X
```
```tex
u : (\textit{Espaces}/Y)_{fppf} \longrightarrow (\textit{Espaces}/X)_{fppf}, \quad V/Y \longmapsto V/X
```

### `lemma-morphism-big-fppf`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
v : (\textit{Spaces}/X)_{fppf} \longrightarrow (\textit{Spaces}/Y)_{fppf}, \quad (U \to Y) \longmapsto (U \times_X Y \to Y).
```
```tex
v : (\textit{Espaces}/X)_{fppf} \longrightarrow (\textit{Espaces}/Y)_{fppf}, \quad (U \to Y) \longmapsto (U \times_X Y \to Y).
```

### `lemma-morphism-big-fppf`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
f_{big} : \Sh((\textit{Spaces}/Y)_{fppf}) \longrightarrow \Sh((\textit{Spaces}/X)_{fppf})
```
```tex
f_{big} : \Sh((\textit{Espaces}/Y)_{fppf}) \longrightarrow \Sh((\textit{Espaces}/X)_{fppf})
```

### `definition-big-ph-site`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_{ph}
```
```tex
(\textit{Espaces}/S)_{ph}
```

### `definition-big-ph-site`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
\textit{Spaces}/S
```
```tex
\textit{Espaces}/S
```

### `definition-big-ph-site`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
\textit{Spaces}/S
```
```tex
\textit{Espaces}/S
```

### `definition-big-small-ph`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_{ph}
```
```tex
(\textit{Espaces}/S)_{ph}
```

### `definition-big-small-ph`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_{ph}
```
```tex
(\textit{Espaces}/S)_{ph}
```

### `definition-big-small-ph`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/X)_{ph}
```
```tex
(\textit{Espaces}/X)_{ph}
```

### `definition-big-small-ph`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/S)_{ph}
```
```tex
(\textit{Espaces}/S)_{ph}
```

### `lemma-characterize-sheaf`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/X)_{ph}
```
```tex
(\textit{Espaces}/X)_{ph}
```

### `lemma-characterize-sheaf`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/X)_{ph}
```
```tex
(\textit{Espaces}/X)_{ph}
```

### `lemma-characterize-sheaf`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/X)_{ph}
```
```tex
(\textit{Espaces}/X)_{ph}
```

### `lemma-morphism-big-ph`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
u : (\textit{Spaces}/Y)_{ph} \longrightarrow (\textit{Spaces}/X)_{ph}, \quad V/Y \longmapsto V/X
```
```tex
u : (\textit{Espaces}/Y)_{ph} \longrightarrow (\textit{Espaces}/X)_{ph}, \quad V/Y \longmapsto V/X
```

### `lemma-morphism-big-ph`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
v : (\textit{Spaces}/X)_{ph} \longrightarrow (\textit{Spaces}/Y)_{ph}, \quad (U \to Y) \longmapsto (U \times_X Y \to Y).
```
```tex
v : (\textit{Espaces}/X)_{ph} \longrightarrow (\textit{Espaces}/Y)_{ph}, \quad (U \to Y) \longmapsto (U \times_X Y \to Y).
```

### `lemma-morphism-big-ph`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
f_{big} : \Sh((\textit{Spaces}/Y)_{ph}) \longrightarrow \Sh((\textit{Spaces}/X)_{ph})
```
```tex
f_{big} : \Sh((\textit{Espaces}/Y)_{ph}) \longrightarrow \Sh((\textit{Espaces}/X)_{ph})
```

### `lemma-cech-enough`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/X)_{fppf}
```
```tex
(\textit{Espaces}/X)_{fppf}
```

### `lemma-cech-enough`

Spaces devient Espaces dans le nom de la catégorie. La paire entière a été lue : aucun argument, indice de topologie, base, objet ou morphisme ne change. Les notations de topologie smooth et fppf restent celles du témoin ; cette paire ne vaut pas approbation de toute la terminologie environnante.

```tex
(\textit{Spaces}/X)_{fppf}
```
```tex
(\textit{Espaces}/X)_{fppf}
```

### `lemma-cech-enough`

Pour tous porte sur p supérieur ou égal à zéro et sur tous les indices i_0,…,i_p ; la portée du quantificateur et l’implication vers P(U) sont conservées.

```tex
P(U_{i_0} \times_U \ldots \times_U U_{i_p}) \text{ for all } p \geq 0,\ i_0, \ldots, i_p \in I \Rightarrow P(U)
```
```tex
P(U_{i_0} \times_U \ldots \times_U U_{i_p}) \text{ pour tous } p \geq 0,\ i_0, \ldots, i_p \in I \Rightarrow P(U)
```

## Limites

Chaque contexte modifié et chaque différence conservée ci-dessus a été lu dans les deux langues. Les contrôles sur tous les blocs étiquetés ne certifient pas l’intégralité de la prose ni de la terminologie. Les anomalies du témoin officiel restaurées ne sont pas présentées comme mathématiquement correctes. L’inversion des opérations reproduit exactement la version publique. La construction et la vérification publique du lecteur complet restent à effectuer.
