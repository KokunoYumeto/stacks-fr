# Descente et groupoïdes en espaces algébriques : contrôle délimité

**Copies locales seulement ; ni édition complète certifiée ni publication corrigée.**

[Contrôles](DESCENT_GROUPOIDS_FR_VALIDATION.json) · [Avant/après exacts](DESCENT_GROUPOIDS_FR_REPAIRS.json) · [Contextes conservés](DESCENT_GROUPOIDS_FR_RETAINED_CONTEXTS.json) · [Paires de texte dans les formules](DESCENT_GROUPOIDS_FR_READER_TEXT_PAIRS.json)

## Réparations propres à la traduction

Les changements ci-dessous réparent le français et sa fidélité. Ils ne corrigent pas les mathématiques de l’auteur. Les défauts du texte anglais, notamment T au lieu de S dans un raffinement et les indices de composition d’un groupoïde d’inertie, restent visibles.

La convention source-et-cible distingue le terme composé SP du couple de propriétés ST, distinction explicitement expliquée par le texte source. La définition et la remarque comparant ST, DM et SP ont été lues en entier, puis chacune des 21 occurrences dans son contexte. Deux recherches ciblées n’ont pas fourni d’attestation française pertinente ; cela ne prouve pas qu’il n’en existe aucune. Ce composé n’est donc pas présenté comme une terminologie consacrée. Il reste révisable, sans suspendre la réparation. Aucune consultation initiale du traducteur n’est inventée.

[Chapitre 78 — spaces-groupoids : LaTeX](staged/fr/078_spaces-groupoids.fr.tex)

[Chapitre 35 — descent : LaTeX](staged/fr/035_descent.fr.tex)

### FR-SPACES-GROUPOIDS-TRANSLATION-001

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-groupoids.tex#L2170)

La source demande de raffiner T, non de raffiner un objet implicite par T. La préposition par introduisait un autre rôle. On garde la lettre T malgré sa discordance avec S dans le texte officiel ; on ne corrige donc pas l’erratum source.

Avant :
```tex
après avoir raffiné par $\mathcal{T}$
```
Après :
```tex
après avoir raffiné $\mathcal{T}$
```

### FR-DESCENT-TRANSLATION-001

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L4581)

Le même invariant est appelé cohomology tout au long de ce passage. Homologie apparaissait une fois dans la traduction ; cohomologie restaure le terme source sans modifier la suite ou l’argument.

Avant :
```tex
donc d'homologie nulle.
```
Après :
```tex
donc de cohomologie nulle.
```

### FR-DESCENT-TRANSLATION-002

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L5413)

Les deux noms doivent être ceux de la liste française déjà définie, lisse et syntomique. Les hypothèses et les cinq correspondances demeurent inchangées.

Avant :
```tex
$\tau$ vaut fpqc, fppf, \'etale, smooth ou syntomic (comparer
```
Après :
```tex
$\tau$ vaut fpqc, fppf, \'etale, lisse ou syntomique (comparer
```

### FR-DESCENT-TRANSLATION-003

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L5421)

Les deux noms doivent être ceux de la liste française déjà définie, lisse et syntomique. Les hypothèses et les cinq correspondances demeurent inchangées.

Avant :
```tex
$\tau$ vaut fpqc, fppf, \'etale, smooth ou syntomic, et pour tout morphisme de
```
Après :
```tex
$\tau$ vaut fpqc, fppf, \'etale, lisse ou syntomique, et pour tout morphisme de
```

### FR-DESCENT-TRANSLATION-004

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7040)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
étés des morphismes locales sur la source et la cible pour la topologie \'etale}

```
Après :
```tex
étés des morphismes locales sur la source-et-cible pour la topologie \'etale}

```

### FR-DESCENT-TRANSLATION-005

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7139)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
n pour une propriété locale sur la source et
la cible pour la topologie \'etale ? Par analogie ave
```
Après :
```tex
n pour une propriété locale sur la source-et-cible pour la topologie \'etale ? Par analogie ave
```

### FR-DESCENT-TRANSLATION-006

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7146)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
mathcal{P}$ est {\it locale sur la source et la cible pour
la topologie \'etale} si
\begin{enumera
```
Après :
```tex
mathcal{P}$ est {\it locale sur la source-et-cible pour
la topologie \'etale} si
\begin{enumera
```

### FR-DESCENT-TRANSLATION-007

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7176)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
outre, une propriété locale sur la source et la cible pour la topologie
\'etale est locale sur la 
```
Après :
```tex
outre, une propriété locale sur la source-et-cible pour la topologie
\'etale est locale sur la 
```

### FR-DESCENT-TRANSLATION-008

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7184)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
s de schémas qui est locale sur
la source et la cible pour la topologie \'etale. Alors
\begin{enum
```
Après :
```tex
s de schémas qui est locale sur
la source-et-cible pour la topologie \'etale. Alors
\begin{enum
```

### FR-DESCENT-TRANSLATION-009

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7254)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
orphismes de schémas locale sur la source
et la cible pour la topologie \'etale. Soit $f : X \to Y
```
Après :
```tex
orphismes de schémas locale sur la source-et-cible pour la topologie \'etale. Soit $f : X \to Y
```

### FR-DESCENT-TRANSLATION-010

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7325)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
rs $\mathcal{P}$ est locale sur la source et la cible pour la topologie
\'etale.
\end{lemma}

\beg
```
Après :
```tex
rs $\mathcal{P}$ est locale sur la source-et-cible pour la topologie
\'etale.
\end{lemma}

\beg
```

### FR-DESCENT-TRANSLATION-011

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7498)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
ont la propriété est locale sur la source et la cible pour
la topologie \'etale. Dans chaque cas, 
```
Après :
```tex
ont la propriété est locale sur la source-et-cible pour
la topologie \'etale. Dans chaque cas, 
```

### FR-DESCENT-TRANSLATION-012

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7557)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
)] $\mathcal{P}$ est locale sur la source et la cible pour la
topologie \'etale.
\end{enumerate}
N
```
Après :
```tex
)] $\mathcal{P}$ est locale sur la source-et-cible pour la
topologie \'etale.
\end{enumerate}
N
```

### FR-DESCENT-TRANSLATION-013

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7572)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
orphismes de schémas locale sur la source
et la cible pour la topologie \'etale. Étant donné un di
```
Après :
```tex
orphismes de schémas locale sur la source-et-cible pour la topologie \'etale. Étant donné un di
```

### FR-DESCENT-TRANSLATION-014

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7746)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
ue $\mathcal{P}$ est locale sur la source et la
cible pour la topologie \'etale. Le
lemme \ref{lem
```
Après :
```tex
ue $\mathcal{P}$ est locale sur la source-et-cible pour la topologie \'etale. Le
lemme \ref{lem
```

### FR-DESCENT-TRANSLATION-015

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7818)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
ue $\mathcal{P}$ est locale sur la source et la cible pour la topologie
\'etale). Puisque $T_p : \
```
Après :
```tex
ue $\mathcal{P}$ est locale sur la source-et-cible pour la topologie
\'etale). Puisque $T_p : \
```

### FR-DESCENT-TRANSLATION-016

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7829)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
orphismes de germes locales sur la source et la cible
pour la topologie étale}

```
Après :
```tex
orphismes de germes locales sur la source-et-cible
pour la topologie étale}

```

### FR-DESCENT-TRANSLATION-017

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7840)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
mathcal{Q}$ est {\it locale sur la source et la cible pour la
topologie \'etale} si, pour tout dia
```
Après :
```tex
mathcal{Q}$ est {\it locale sur la source-et-cible pour la
topologie \'etale} si, pour tout dia
```

### FR-DESCENT-TRANSLATION-018

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7855)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
s de schémas
qui est locale sur la source et la cible pour la topologie \'etale.
Considérons la pr
```
Après :
```tex
s de schémas
qui est locale sur la source-et-cible pour la topologie \'etale.
Considérons la pr
```

### FR-DESCENT-TRANSLATION-019

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7864)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
rs $\mathcal{Q}$ est locale sur la source et la cible pour la topologie
\'etale au sens de la
défi
```
Après :
```tex
rs $\mathcal{Q}$ est locale sur la source-et-cible pour la topologie
\'etale au sens de la
défi
```

### FR-DESCENT-TRANSLATION-020

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7896)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
s de schémas qui est
locale sur la source et la cible pour la topologie \'etale. Soit $Q$ la
propr
```
Après :
```tex
s de schémas qui est
locale sur la source-et-cible pour la topologie \'etale. Soit $Q$ la
propr
```

### FR-DESCENT-TRANSLATION-021

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L7925)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
xt{ est plat}
$$
est locale sur la source et la cible pour la topologie \'etale.
\end{lemma}

\beg
```
Après :
```tex
xt{ est plat}
$$
est locale sur la source-et-cible pour la topologie \'etale.
\end{lemma}

\beg
```

### FR-DESCENT-TRANSLATION-022

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L8010)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
 dimension }d
$$
est locale sur la source et la cible pour la topologie \'etale.
\end{lemma}

\beg
```
Après :
```tex
 dimension }d
$$
est locale sur la source-et-cible pour la topologie \'etale.
\end{lemma}

\beg
```

### FR-DESCENT-TRANSLATION-023

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L8032)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
\kappa(x) = r
$$
est locale sur la source et la cible pour la topologie \'etale.
\end{lemma}

\beg
```
Après :
```tex
\kappa(x) = r
$$
est locale sur la source-et-cible pour la topologie \'etale.
\end{lemma}

\beg
```

### FR-DESCENT-TRANSLATION-024

[Passage officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/descent.tex#L8071)

La source distingue expressément la propriété composée source-and-target (SP) de la localité séparée sur la source et sur la cible (ST). Le composé source-et-cible préserve cette distinction, jusque dans les titres et les usages ultérieurs. C’est une convention de traduction provisoire fondée sur les définitions du chapitre, non une attestation revendiquée dans un traité français. Les conditions définitoires et les preuves ne sont pas modifiées.

Avant :
```tex
m_x (X_s) = d
$$
est locale sur la source et la cible pour la topologie \'etale.
\end{lemma}

\beg
```
Après :
```tex
m_x (X_s) = d
$$
est locale sur la source-et-cible pour la topologie \'etale.
\end{lemma}

\beg
```

## Différences conservées après comparaison

### spaces-groupoids — `section-notation`

Le second T est remplacé par c’est-à-dire à un schéma : le même schéma test porte toujours le morphisme vers B. Les ensembles de points et leur fonctorialité restent explicites.

### spaces-groupoids — `definition-pseudo-torsor`

Lui-même renvoie sans ambiguïté au groupe G qui agit par multiplication à gauche ; aucune action ni condition du pseudo-torseur ne disparaît.

### spaces-groupoids — `definition-principal-homogeneous-space`

Les noms de topologies lisse et syntomique traduisent smooth et syntomic. La distinction entre trivialité fpqc et torseur fppf, y compris la note, est conservée.

### spaces-groupoids — `lemma-pseudo-torsor-implications`

Sinon reprend X non vide dans la même disjonction. L’extension du corps et le point de X restent mentionnés.

### spaces-groupoids — `lemma-construct-quasi-coherent`

La virgule entre s,t devient et. Les deux hypothèses de platitude, quasi-compacité et quasi-séparation restent conjointes. Les adjoints et l’ordre des produits fibrés sont conservés.

### spaces-groupoids — `lemma-colimit-coherent`

s et t conserve la portée des trois hypothèses sur chacun des deux morphismes. Aucun changement dans les deux carrés ou le sous-module obtenu.

### spaces-groupoids — `lemma-crystals-in-quasi-coherent-modules`

Correspondent bijectivement traduit 1-to-1. Les deux familles de sous-modules sont les mêmes. Le défaut littéral m/m prime dans la règle de choix est conservé, non réparé.

### spaces-groupoids — `lemma-set-generators`

Correspondance bijective remplace 1-to-1 avec les mêmes sous-modules. Fidèle et pleinement fidèle dans la note restent distincts ; aucune équivalence n’est ajoutée.

### spaces-groupoids — `definition-representable-quotient`

Elle reprend la pré-relation j ; M est explicitement sujet de est muni dans la phrase suivante. Il ne s’agit pas d’un remplacement mathématique de j par M.

### spaces-groupoids — `lemma-criterion-quotient-representable`

Coégalise s et t conserve la même égalité des composés. Il dans la troisième phrase désigne le même morphisme U/R vers M ; les trois conditions sont conservées.

### spaces-groupoids — `lemma-quotient-pre-equivalence-relation-restrict`

La conjonction française entre les deux restrictions de xi et xi prime ne les change pas. Une erreur distincte, raffiner par T au lieu de raffiner T, est corrigée ; la lettre T elle-même reste celle du témoin.

### spaces-groupoids — `lemma-quotient-stack-functorial`

Un schéma variable T exprime en une occurrence le schéma T variable des points-valués. Les cinq données du troisième groupoïde restent exactes.

### spaces-groupoids — `lemma-quotient-stack-restrict`

Leurs images reprend x,y ; les autres virgules deviennent et sans changer les quatre objets, les composés ni la condition pleinement fidèle si et seulement si.

### spaces-groupoids — `lemma-presentation-inertia`

De (x,g) vers (y,h) exprime la même orientation que la flèche source. Les incohérences littérales des indices dans la dernière composition ne sont pas corrigées silencieusement.

### spaces-groupoids — `lemma-when-gerbe`

x,y explicite le sujet grammatical absent de assume that come from, déjà fixé dans les phrases précédentes. Aucune nouvelle paire ni hypothèse n’est introduite. La notation imprimée [U prime / prime R] reste intacte.

### descent — `lemma-qc-colimits`

Les cinq lignes de l’équivalence sont conservées dans leur ordre, notamment la répétition de H. Trois retours supplémentaires servent uniquement à loger les qualificatifs français ; les topologies et le rang fini sont inchangés.

### descent — `lemma-quasi-coherent-alternative-small`

La commande etale ajoute un accent au nom français de la même topologie dans un indice. Les présentations immédiatement voisines utilisent déjà cette commande. Il ne s’agit pas d’un autre site.

### descent — `lemma-curiosity`

Les trois expressions brutes sont plat, localement de type fini, localement de présentation finie. Le masque de comparaison les confondait sous un même représentant : elles sont vérifiées séparément. Une dérive cohomologie/homologie est corrigée dans la prose.

### descent — `lemma-Jacobson-local-fppf`

Un idéal maximal m contenant p est exactement p contenu dans m ; la direction de l’inclusion, la maximalité et le raisonnement par descente sont conservés.

### descent — `lemma-descending-properties-morphisms`

Lisse et syntomique désignent les deux mêmes topologies. Les deux restes anglais dans la prose sont harmonisés avec la liste définie, sans changer les cinq cas ni leur ordre.

### descent — `remark-compare-definitions`

La répétition de P omise dans ST est une ellipse française. En revanche, source-and-target désigne SP, notion distincte : son composé est désormais rendu source-et-cible. Les trois définitions et les implications non réversibles sont inchangées.

### descent — `definition-descending-types-morphisms`

Les noms lisse et syntomique traduisent les mêmes éléments de la liste ; toute donnée de descente et son effectivité conservent leurs quantificateurs.

### descent — `lemma-descending-types-morphisms`

Même ordre des cinq topologies et des conditions sur les morphismes affines. La preuve de descente affine puis générale et ses données sont inchangées.

### descent — `lemma-descent-data-sheaves`

Les noms des deux topologies sont traduits et un point final termine une formule ; l’équivalence des catégories, les objets représentables et l’exclusion explicite de fpqc restent intacts.

## Texte lisible dans les formules

### spaces-groupoids — `lemma-group-scheme-unramified-or-lqf`

Non ramifié aux deux points e et g garde la même équivalence.

```tex
G \to \Spec(k)\text{ is unramified at }e \Leftrightarrow G \to \Spec(k)\text{ is unramified at }g
```
```tex
G \to \Spec(k)\text{ est non ramifié en }e \Leftrightarrow G \to \Spec(k)\text{ est non ramifié en }g
```

### spaces-groupoids — `equation-pull`

Flèches traduit Arrows ; la base Ob et les deux indices t restent exacts.

```tex
\text{Arrows} \times_{t, \text{Ob}, t} \text{Arrows}
```
```tex
\text{Flèches} \times_{t, \text{Ob}, t} \text{Flèches}
```

### spaces-groupoids — `equation-pull`

Même ensemble de flèches, maintenant avec indices s,t inchangés.

```tex
\text{Arrows} \times_{s, \text{Ob}, t} \text{Arrows}
```
```tex
\text{Flèches} \times_{s, \text{Ob}, t} \text{Flèches}
```

### spaces-groupoids — `lemma-pushforward`

Et joint les deux mêmes carrés, avec les mêmes noms de morphismes.

```tex
\vcenter{ \xymatrix{ R \ar[d]_t \ar[r]_f & R' \ar[d]^{t'} \\ U \ar[r]^f & U' } } \quad\text{and}\quad \vcenter{ \xymatrix{ R \ar[d]_s \ar[r]_f & R' \ar[d]^{s'} \\ U \ar[r]^f & U' } }
```
```tex
\vcenter{ \xymatrix{ R \ar[d]_t \ar[r]_f & R' \ar[d]^{t'} \\ U \ar[r]^f & U' } } \quad\text{et}\quad \vcenter{ \xymatrix{ R \ar[d]_s \ar[r]_f & R' \ar[d]^{s'} \\ U \ar[r]^f & U' } }
```

### spaces-groupoids — `lemma-crystals-in-quasi-coherent-modules`

Ouvert affine qualifie exactement U contenu dans X_i.

```tex
J = \coprod\nolimits_{i \in I} \{U \subset X_i\text{ affine open}\}
```
```tex
J = \coprod\nolimits_{i \in I} \{U \subset X_i\text{ ouvert affine}\}
```

### spaces-groupoids — `lemma-crystals-in-quasi-coherent-modules`

Les deux familles gardent leurs inclusions et la condition sur f_phi ; aucune direction n’est renversée.

```tex
\Psi = & \coprod\nolimits_{\phi \in \Phi} \{ (U, V) \mid U \subset X_i, V \subset X_{i'}\text{ affine open with } f_\phi(U) \subset V \} \\ & \amalg \coprod\nolimits_{i \in I} \{ (U, U') \mid U, U' \subset X_i\text{ affine open with } U \subset U' \}
```
```tex
\Psi = & \coprod\nolimits_{\phi \in \Phi} \{ (U, V) \mid U \subset X_i, V \subset X_{i'}\text{ ouverts affines tels que } f_\phi(U) \subset V \} \\ & \amalg \coprod\nolimits_{i \in I} \{ (U, U') \mid U, U' \subset X_i\text{ ouverts affines tels que } U \subset U' \}
```

### spaces-groupoids — `remark-quotient-variant`

Espaces et Ens nomment les mêmes catégories ; la variance opposée et le quotient sont conservés.

```tex
\begin{matrix} (\textit{Spaces}/B)^{opp}_{fppf} & \longrightarrow & \textit{Sets}, \\ X & \longmapsto & U(X)/\sim_X \end{matrix}
```
```tex
\begin{matrix} (\textit{Espaces}/B)^{opp}_{fppf} & \longrightarrow & \textit{Ens}, \\ X & \longmapsto & U(X)/\sim_X \end{matrix}
```

### spaces-groupoids — `section-explicit-quotient-stacks`

Et relie les deux identités de source et cible, sans échanger les projections.

```tex
s \circ r_{ij} = u_i \circ \text{pr}_0 \quad\text{and}\quad t \circ r_{ij} = u_j \circ \text{pr}_1,
```
```tex
s \circ r_{ij} = u_i \circ \text{pr}_0 \quad\text{et}\quad t \circ r_{ij} = u_j \circ \text{pr}_1,
```

### spaces-groupoids — `section-explicit-quotient-stacks`

Et conserve les deux conditions portant sur u_i et u_i prime.

```tex
u_i = s \circ r_i \quad\text{and}\quad u'_i = t \circ r_i
```
```tex
u_i = s \circ r_i \quad\text{et}\quad u'_i = t \circ r_i
```

### spaces-groupoids — `lemma-quotient-stack-objects`

Le tableau est lu conjointement : morphismes de données de descente pour [U/R], mêmes deux données et mêmes objets x,y.

```tex
\Mor_{[U/R]_T}(x, y) \longleftrightarrow \left\{ \begin{matrix} \text{morphisms }(u_i, r_{ij}) \to (u'_i, r'_{ij})\\ \text{of }[U/R]\text{-descent data} \end{matrix} \right\}
```
```tex
\Mor_{[U/R]_T}(x, y) \longleftrightarrow \left\{ \begin{matrix} \text{morphismes }(u_i, r_{ij}) \to (u'_i, r'_{ij})\\ \text{de données de descente pour }[U/R]\text{} \end{matrix} \right\}
```

### descent — `section-galois-descent`

Et relie les deux identités de changements de base, doubles et triples.

```tex
X_{k'} \times_X X_{k'} = X_{k' \otimes_k k'} \quad\text{and}\quad X_{k'} \times_X X_{k'} \times_X X_{k'} = X_{k' \otimes_k k' \otimes_k k'}
```
```tex
X_{k'} \times_X X_{k'} = X_{k' \otimes_k k'} \quad\text{et}\quad X_{k'} \times_X X_{k'} \times_X X_{k'} = X_{k' \otimes_k k' \otimes_k k'}
```

### descent — `lemma-fully-faithful-associated`

Ou conserve l’alternative entre grand et petit sites.

```tex
\QCoh(\mathcal{O}_S) \to \QCoh((\Sch/S)_\tau, \mathcal{O}) \quad\text{or}\quad \QCoh(\mathcal{O}_S) \to \QCoh(S_\tau, \mathcal{O})
```
```tex
\QCoh(\mathcal{O}_S) \to \QCoh((\Sch/S)_\tau, \mathcal{O}) \quad\text{ou}\quad \QCoh(\mathcal{O}_S) \to \QCoh(S_\tau, \mathcal{O})
```

### descent — `lemma-equivalence-quasi-coherent-properties`

Et conserve les deux foncteurs sur le grand et le petit site.

```tex
\QCoh(\mathcal{O}_S) \longrightarrow \QCoh((\Sch/S)_\tau, \mathcal{O}) \quad\text{and}\quad \QCoh(\mathcal{O}_S) \longrightarrow \QCoh(S_\tau, \mathcal{O})
```
```tex
\QCoh(\mathcal{O}_S) \longrightarrow \QCoh((\Sch/S)_\tau, \mathcal{O}) \quad\text{et}\quad \QCoh(\mathcal{O}_S) \longrightarrow \QCoh(S_\tau, \mathcal{O})
```

### descent — `lemma-equivalence-quasi-coherent-properties`

Vérifie P garde la propriété du même module et sa version associée.

```tex
\mathcal{F}\text{ has }\mathcal{P} \Leftrightarrow \mathcal{F}^a\text{ has }\mathcal{P}\text{ as an }\mathcal{O}\text{-module}
```
```tex
\mathcal{F}\text{ vérifie }\mathcal{P} \Leftrightarrow \mathcal{F}^a\text{ vérifie }\mathcal{P}\text{ comme }\mathcal{O}\text{-module}
```

### descent — `lemma-equivalence-quasi-coherent-limits`

Et joint les deux foncteurs vers les modules, sans modifier leur cible.

```tex
\QCoh(\mathcal{O}_S) \longrightarrow \textit{Mod}((\Sch/S)_\tau, \mathcal{O}) \quad\text{and}\quad \QCoh(\mathcal{O}_S) \longrightarrow \textit{Mod}(S_\tau, \mathcal{O})
```
```tex
\QCoh(\mathcal{O}_S) \longrightarrow \textit{Mod}((\Sch/S)_\tau, \mathcal{O}) \quad\text{et}\quad \QCoh(\mathcal{O}_S) \longrightarrow \textit{Mod}(S_\tau, \mathcal{O})
```

### descent — `lemma-universal-effective-epimorphism-affine`

Égalisateur conserve les deux flèches parallèles et les mêmes produits de sections.

```tex
\Gamma(X, \mathcal{F}) = \text{Equalizer}\left( \xymatrix{ \prod\nolimits_{i \in I} \Gamma(X_i, f_i^*\mathcal{F}) \ar@<1ex>[r] \ar@<-1ex>[r] & \prod\nolimits_{i, j \in I} \Gamma(X_i \times_X X_j, (f_i \times f_j)^*\mathcal{F}) } \right)
```
```tex
\Gamma(X, \mathcal{F}) = \text{Égalisateur}\left( \xymatrix{ \prod\nolimits_{i \in I} \Gamma(X_i, f_i^*\mathcal{F}) \ar@<1ex>[r] \ar@<-1ex>[r] & \prod\nolimits_{i, j \in I} \Gamma(X_i \times_X X_j, (f_i \times f_j)^*\mathcal{F}) } \right)
```

### descent — `definition-property-local`

Chaque S_i conserve le quantificateur universel et l’équivalence.

```tex
S \text{ has }\mathcal{P} \Leftrightarrow \text{each }S_i \text{ has }\mathcal{P}.
```
```tex
S \text{ vérifie }\mathcal{P} \Leftrightarrow \text{chaque }S_i \text{ vérifie }\mathcal{P}.
```

### descent — `definition-property-morphisms-local`

Chaque changement de base Y_i fois_Y X vers Y_i conserve la même propriété.

```tex
f \text{ has }\mathcal{P} \Leftrightarrow \text{each }Y_i \times_Y X \to Y_i\text{ has }\mathcal{P}.
```
```tex
f \text{ vérifie }\mathcal{P} \Leftrightarrow \text{chaque }Y_i \times_Y X \to Y_i\text{ vérifie }\mathcal{P}.
```

### descent — `definition-property-morphisms-local-source`

Chaque X_i vers Y conserve la même propriété, sans remplacer source par cible.

```tex
f \text{ has }\mathcal{P} \Leftrightarrow \text{each }X_i \to Y\text{ has }\mathcal{P}.
```
```tex
f \text{ vérifie }\mathcal{P} \Leftrightarrow \text{chaque }X_i \to Y\text{ vérifie }\mathcal{P}.
```

### descent — `lemma-etale-etale-local-source-target`

Avec les points annonce le diagramme des mêmes quatre points.

```tex
\vcenter{ \xymatrix{ X' \ar[d]_{g'} \ar[r]_{f'} & Y' \ar[d]^g \\ X \ar[r]^f & Y } } \quad\text{with points}\quad \vcenter{ \xymatrix{ x' \ar[d] \ar[r] & y' \ar[d] \\ x \ar[r] & y } }
```
```tex
\vcenter{ \xymatrix{ X' \ar[d]_{g'} \ar[r]_{f'} & Y' \ar[d]^g \\ X \ar[r]^f & Y } } \quad\text{avec les points}\quad \vcenter{ \xymatrix{ x' \ar[d] \ar[r] & y' \ar[d] \\ x \ar[r] & y } }
```

### descent — `lemma-etale-tau-local-source-target`

Même vérification pour le deuxième diagramme avec points.

```tex
\vcenter{ \xymatrix{ X' \ar[d]_{g'} \ar[r]_{f'} & Y' \ar[d]^g \\ X \ar[r]^f & Y } } \quad\text{with points}\quad \vcenter{ \xymatrix{ x' \ar[d] \ar[r] & y' \ar[d] \\ x \ar[r] & y } }
```
```tex
\vcenter{ \xymatrix{ X' \ar[d]_{g'} \ar[r]_{f'} & Y' \ar[d]^g \\ X \ar[r]^f & Y } } \quad\text{avec les points}\quad \vcenter{ \xymatrix{ x' \ar[d] \ar[r] & y' \ar[d] \\ x \ar[r] & y } }
```

### descent — `lemma-local-source-target-global-implies-local`

Il existe un représentant garde le quantificateur existentiel et la propriété P.

```tex
\mathcal{Q}((X, x) \to (S, s)) \Leftrightarrow \text{there exists a representative }U \to S \text{ which has }\mathcal{P}
```
```tex
\mathcal{Q}((X, x) \to (S, s)) \Leftrightarrow \text{il existe un représentant }U \to S \text{ qui vérifie }\mathcal{P}
```

### descent — `lemma-flat-at-point`

Est plat porte sur le même homomorphisme d’anneaux locaux.

```tex
\mathcal{P}((X, x) \to (S, s)) = \mathcal{O}_{S, s} \to \mathcal{O}_{X, x}\text{ is flat}
```
```tex
\mathcal{P}((X, x) \to (S, s)) = \mathcal{O}_{S, s} \to \mathcal{O}_{X, x}\text{ est plat}
```

### descent — `lemma-dimension-local-ring-fibre`

L’anneau local de la fibre garde exactement sa dimension d.

```tex
\mathcal{P}_d((X, x) \to (S, s)) = \text{the local ring } \mathcal{O}_{X_s, x} \text{ of the fibre has dimension }d
```
```tex
\mathcal{P}_d((X, x) \to (S, s)) = \text{l'anneau local } \mathcal{O}_{X_s, x} \text{ de la fibre est de dimension }d
```

### descent — `lemma-family-is-one`

Les deux catégories de données de descente et le sens du foncteur sont inchangés.

```tex
\begin{matrix} \text{category of descent data } \\ \text{relative to the family } \{X_i \to S\}_{i \in I} \end{matrix} \longrightarrow \begin{matrix} \text{ category of descent data} \\ \text{ relative to } X/S \end{matrix}
```
```tex
\begin{matrix} \text{catégorie des données de descente } \\ \text{relativement à la famille } \{X_i \to S\}_{i \in I} \end{matrix} \longrightarrow \begin{matrix} \text{ catégorie des données de descente} \\ \text{ relativement à } X/S \end{matrix}
```

### descent — `lemma-fpqc-refinement-coverings-fully-faithful`

Le foncteur va toujours des données relatives à V aux données relatives à U.

```tex
\text{descent data relative to } \mathcal{V} \longrightarrow \text{descent data relative to } \mathcal{U}
```
```tex
\text{données de descente relativement à } \mathcal{V} \longrightarrow \text{données de descente relativement à } \mathcal{U}
```

### descent — `lemma-fpqc-refinement-coverings-fully-faithful`

Lemme garde les deux références exactes du diagramme.

```tex
\xymatrix{ DD(Y/S) \ar[r] & DD(X/S) \\ DD(\mathcal{V}) \ar[u]^{\text{Lemma }\ref{lemma-family-is-one}} \ar[r] & DD(\mathcal{U}) \ar[u]_{\text{Lemma }\ref{lemma-family-is-one}} }
```
```tex
\xymatrix{ DD(Y/S) \ar[r] & DD(X/S) \\ DD(\mathcal{V}) \ar[u]^{\text{lemme }\ref{lemma-family-is-one}} \ar[r] & DD(\mathcal{U}) \ar[u]_{\text{lemme }\ref{lemma-family-is-one}} }
```

### descent — `lemma-Zariski-refinement-coverings-equivalence`

Même sens du foncteur de restriction des données de descente.

```tex
\text{descent data relative to } \mathcal{V} \longrightarrow \text{descent data relative to } \mathcal{U}
```
```tex
\text{données de descente relativement à } \mathcal{V} \longrightarrow \text{données de descente relativement à } \mathcal{U}
```

### descent — `lemma-refine-coverings-fully-faithful`

Même sens du foncteur dans le lemme suivant.

```tex
\text{descent data relative to } \mathcal{V} \longrightarrow \text{descent data relative to } \mathcal{U}
```
```tex
\text{données de descente relativement à } \mathcal{V} \longrightarrow \text{données de descente relativement à } \mathcal{U}
```

### descent — `remark-morphisms-of-schemes-satisfy-fpqc-descent`

Ensembles est la catégorie Sets ; la variance et les morphismes sur T restent exacts.

```tex
(\Sch/S)^{opp} \longrightarrow \textit{Sets}, \quad T \longmapsto \Mor_T(X_T, Y_T)
```
```tex
(\Sch/S)^{opp} \longrightarrow \textit{Ensembles}, \quad T \longmapsto \Mor_T(X_T, Y_T)
```

### descent — `lemma-descent-data-sheaves`

Le tableau est lu comme une phrase entière : mêmes données, mêmes faisceaux et même condition de représentabilité de chaque produit.

```tex
\left\{ \begin{matrix} \text{descent data }(X_i, \varphi_{ii'})\text{ such that}\\ \text{each }X_i \in \Ob((\Sch/S)_\tau) \end{matrix} \right\} \leftrightarrow \left\{ \begin{matrix} \text{sheaves }F\text{ on }(\Sch/S)_\tau\text{ such that}\\ \text{each }h_{S_i} \times F\text{ is representable} \end{matrix} \right\}.
```
```tex
\left\{ \begin{matrix} \text{données de descente }(X_i, \varphi_{ii'})\text{ telles que}\\ \text{chaque }X_i \in \Ob((\Sch/S)_\tau) \end{matrix} \right\} \leftrightarrow \left\{ \begin{matrix} \text{faisceaux }F\text{ sur }(\Sch/S)_\tau\text{ tels que}\\ \text{chaque }h_{S_i} \times F\text{ est représentable} \end{matrix} \right\}.
```

## Limites

Les contrôles couvrent les candidats de formules de ces deux témoins et les passages explicitement lus, pas toute la prose ni tout le corpus. Leurs exceptions ne sont pas des règles de masquage générales. Le tableau localement libre de rang fini et les trois cas de la preuve de descente ont été lus à l’état brut, car un masque de texte ne suffit pas. Les fichiers officiels et publics n’ont pas été modifiés. Les nouveaux fichiers se reconstruisent exactement depuis les témoins et leur retour inverse est vérifié.
