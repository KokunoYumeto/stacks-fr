# Chapitre 17 — lectures officielles rétablies

Copie de travail non reconstruite et non publiée. 4 opérations de contenu rétablies ; 3 choix de traduction idiomatique conservés. Les propositions ne sont pas déclarées fausses : elles restent séparées de la traduction de référence.

## MODULES-010

[Source officielle, ligne 4337](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/modules.tex#L4337) · `lemma-pic-set`.

Avant :
```tex
La collection de tous les recouvrements
$\mathcal{U} : X = \bigcup_{j \in J} U_j$
```

Lecture rétablie :
```tex
La collection de tous les recouvrements
$\mathcal{U} : X = \bigcup_{j \in J} U_i$
```

Rétablir la lecture exacte du texte officiel, sans appliquer la correction mathématique proposée. Celle-ci reste dans le dossier d'errata séparé.

## MODULES-001

[Source officielle, ligne 4629](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/modules.tex#L4629) · `lemma-simple-invert`.

Avant :
```tex
inversible de $\mathcal{S}^{-1}\mathcal{O}_X$.
```

Lecture rétablie :
```tex
inversible de $\mathcal{O}_X$.
```

Rétablir la lecture exacte du texte officiel, sans appliquer la correction mathématique proposée. Celle-ci reste dans le dossier d'errata séparé.

## MODULES-003

[Source officielle, ligne 5263](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/modules.tex#L5263) · `lemma-module-principal-parts`.

Avant :
```tex
[m + m'] - [m] - [m'],\quad
f[m] - [fm], \quad
```

Lecture rétablie :
```tex
[m + m' - [m] - [m'],\quad
f[m] - [fm], \quad
```

Rétablir la lecture exacte du texte officiel, sans appliquer la correction mathématique proposée. Celle-ci reste dans le dossier d'errata séparé.

## MODULES-006

[Source officielle, ligne 5895](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/modules.tex#L5895) · `definition-cotangent-complex-morphism-ringed-topoi`.

Avant :
```tex
$(g \circ g')^*\NL_{X/Y} \to \NL_{X''/Y''}$
```

Lecture rétablie :
```tex
$(g \circ g')^*\NL_{X''/Y''} \to \NL_{X/Y}$
```

Rétablir la lecture exacte du texte officiel, sans appliquer la correction mathématique proposée. Celle-ci reste dans le dossier d'errata séparé.

## Traductions idiomatiques conservées

- MODULES-008 : « Un voisinage ouvert U de x » explicite le référent du mot neighbourhood après Let x in X ; il ne s'agit pas d'une nouvelle hypothèse. La différence du jeton x est enregistrée séparément dans le contrôle.
- MODULES-009 : « Qui trivialise » traduit la proposition anglaise malgré la faute de flexion trivialization/trivializing, sans ajouter de condition.
- MODULES-011 : La graphie anglaise linebundle/line bundle ne modifie pas l'objet traduit par « fibré en droites ».

## Limites du contrôle

La structure mathématique et les identifiants sont comparés au texte anglais intact, sans lui appliquer de corrections. Les textes traduits à l’intérieur des formules sont énumérés dans le dossier de contrôle ; la validation structurelle seule ne certifie pas toute la prose.

### Équivalence entre formule et prose explicitement vérifiée

Au lemme lemma-invertible, la source vient de fixer x et demande un voisinage ouvert U. « De x » explicite en français le référent déjà imposé de ce voisinage ; ce n'est pas une hypothèse nouvelle. L'unique jeton mathématique ajouté x est reconnu par son passage exact, sans autoriser d'autres différences.

## Textes mathématiques traduits — comparaison lue

Les 21 paires ont été lues. Elles traduisent les conditions ensemblistes (support, sommes finies, image), les légendes de flèches, rang, coégalisateur, les cas d'une puissance tensorielle et les conjonctions. Les conditions, indices, signes et directions sont conservés ; la traduction ne change pas l'opération mathématique nommée. Le seul ajout de x dans la prose mathématique est contrôlé séparément. Contrôle rétrospectif limité à ces paires, non certification de toute la prose.

### Passage mathématique 45

Source :
```tex
\Ker(\varphi)(U) = \{ s \in \mathcal{F}(U) \mid \varphi(s) = 0 \text{ in } \mathcal{G}(U)\}
```

Traduction :
```tex
\Ker(\varphi)(U) = \{ s \in \mathcal{F}(U) \mid \varphi(s) = 0 \text{ dans } \mathcal{G}(U)\}
```

### Passage mathématique 198

Source :
```tex
U \longmapsto \{ \text{sums } \sum\nolimits_{i \in J} f_i (s_i|_U) \text{ where } J \text{ is finite, } U \subset U_i \text{ for } i\in J, \text{ and } f_i \in \mathcal{O}_X(U) \}
```

Traduction :
```tex
U \longmapsto \{ \text{sommes } \sum\nolimits_{i \in J} f_i (s_i|_U) \text{ où } J \text{ est fini, } U \subset U_i \text{ pour } i\in J, \text{ et } f_i \in \mathcal{O}_X(U) \}
```

### Passage mathématique 293

Source :
```tex
\mathcal{H}_Z(\mathcal{F})(U) = \{s \in \mathcal{F}(U) \mid \text{ the support of }s\text{ is contained in }Z \cap U\}.
```

Traduction :
```tex
\mathcal{H}_Z(\mathcal{F})(U) = \{s \in \mathcal{F}(U) \mid \text{ le support de }s\text{ est contenu dans }Z \cap U\}.
```

### Passage mathématique 300

Source :
```tex
\textit{Ab}(X) \longrightarrow \textit{Ab}(Z),\quad \mathcal{F} \longmapsto \mathcal{H}_Z(\mathcal{F}) \text{ viewed as abelian sheaf on }Z
```

Traduction :
```tex
\textit{Ab}(X) \longrightarrow \textit{Ab}(Z),\quad \mathcal{F} \longmapsto \mathcal{H}_Z(\mathcal{F}) \text{ considéré comme faisceau abélien sur }Z
```

### Passage mathématique 588

Source :
```tex
\xymatrix{ (Y, \mathcal{O}_Y) \ar[r]_-\pi \ar[d]_g & (\{*\}, \Gamma(Y, \mathcal{O}_Y)) \ar[d]^{\text{induced by }g^\sharp} \\ (X, \mathcal{O}_X) \ar[r]^-\pi & (\{*\}, \Gamma(X, \mathcal{O}_X)) }
```

Traduction :
```tex
\xymatrix{ (Y, \mathcal{O}_Y) \ar[r]_-\pi \ar[d]_g & (\{*\}, \Gamma(Y, \mathcal{O}_Y)) \ar[d]^{\text{induite par }g^\sharp} \\ (X, \mathcal{O}_X) \ar[r]^-\pi & (\{*\}, \Gamma(X, \mathcal{O}_X)) }
```

### Passage mathématique 1052

Source :
```tex
\textit{Mod}(\mathcal{O}_X) \longrightarrow \textit{Mod}(\mathcal{O}_X|_Z), \quad \mathcal{F} \longmapsto \mathcal{H}_Z(\mathcal{F}) \text{ viewed as an }\mathcal{O}_X|_Z\text{-module on }Z
```

Traduction :
```tex
\textit{Mod}(\mathcal{O}_X) \longrightarrow \textit{Mod}(\mathcal{O}_X|_Z), \quad \mathcal{F} \longmapsto \mathcal{H}_Z(\mathcal{F}) \text{ considéré comme }\mathcal{O}_X|_Z\text{-module sur }Z
```

### Passage mathématique 1097

Source :
```tex
\text{rank}_\mathcal{F} : X \longrightarrow \{0, 1, 2, \ldots\}\cup\{\infty\}
```

Traduction :
```tex
\text{rang}_\mathcal{F} : X \longrightarrow \{0, 1, 2, \ldots\}\cup\{\infty\}
```

### Passage mathématique 1103

Source :
```tex
\text{rank}_\mathcal{F}(x)
```

Traduction :
```tex
\text{rang}_\mathcal{F}(x)
```

### Passage mathématique 1443

Source :
```tex
\mathcal{F} \xrightarrow{\eta \otimes 1} \mathcal{F} \otimes_{\mathcal{O}_X} \mathcal{G} \otimes_{\mathcal{O}_X} \mathcal{F} \xrightarrow{1 \otimes \epsilon} \mathcal{F} \quad\text{and}\quad \mathcal{G} \xrightarrow{1 \otimes \eta} \mathcal{G} \otimes_{\mathcal{O}_X} \mathcal{F} \otimes_{\mathcal{O}_X} \mathcal{G} \xrightarrow{\epsilon \otimes 1} \mathcal{G}
```

Traduction :
```tex
\mathcal{F} \xrightarrow{\eta \otimes 1} \mathcal{F} \otimes_{\mathcal{O}_X} \mathcal{G} \otimes_{\mathcal{O}_X} \mathcal{F} \xrightarrow{1 \otimes \epsilon} \mathcal{F} \quad\text{et}\quad \mathcal{G} \xrightarrow{1 \otimes \eta} \mathcal{G} \otimes_{\mathcal{O}_X} \mathcal{F} \otimes_{\mathcal{O}_X} \mathcal{G} \xrightarrow{\epsilon \otimes 1} \mathcal{G}
```

### Passage mathématique 1572

Source :
```tex
\mathcal{G} = \text{Coequalizer}\left( \xymatrix{ \coprod\nolimits_{b = 1, \ldots, m} j_{V_{b, i}!}\underline{S_b} \ar@<1ex>[r] \ar@<-1ex>[r] & \coprod\nolimits_{a = 1, \ldots, n} j_{U_{a, i}!}\underline{S_a} } \right)
```

Traduction :
```tex
\mathcal{G} = \text{Coégalisateur}\left( \xymatrix{ \coprod\nolimits_{b = 1, \ldots, m} j_{V_{b, i}!}\underline{S_b} \ar@<1ex>[r] \ar@<-1ex>[r] & \coprod\nolimits_{a = 1, \ldots, n} j_{U_{a, i}!}\underline{S_a} } \right)
```

### Passage mathématique 1648

Source :
```tex
\text{T}^n(\mathcal{F}) = \mathcal{F} \otimes_{\mathcal{O}_X} \ldots \otimes_{\mathcal{O}_X} \mathcal{F} \ \ (n\text{ factors})
```

Traduction :
```tex
\text{T}^n(\mathcal{F}) = \mathcal{F} \otimes_{\mathcal{O}_X} \ldots \otimes_{\mathcal{O}_X} \mathcal{F} \ \ (n\text{ facteurs})
```

### Passage mathématique 1890

Source :
```tex
\Hom_X(\mathcal{G}, \mathcal{F}) = \Gamma(X, \mathcal{H}) \quad\text{and}\quad \Hom_X(\mathcal{G}, \mathcal{F}_i) = \Gamma(X, \mathcal{H}_i)
```

Traduction :
```tex
\Hom_X(\mathcal{G}, \mathcal{F}) = \Gamma(X, \mathcal{H}) \quad\text{et}\quad \Hom_X(\mathcal{G}, \mathcal{F}_i) = \Gamma(X, \mathcal{H}_i)
```

### Passage mathématique 2079

Source :
```tex
\mathcal{L}^{\otimes n} = \left\{ \begin{matrix} \mathcal{O}_X & \text{if} & n = 0 \\ \SheafHom_{\mathcal{O}_X}(\mathcal{L}, \mathcal{O}_X) & \text{if} & n = -1\\ \mathcal{L} \otimes_{\mathcal{O}_X} \ldots \otimes_{\mathcal{O}_X} \mathcal{L} & \text{if} & n > 0 \\ \mathcal{L}^{\otimes -1} \otimes_{\mathcal{O}_X} \ldots \otimes_{\mathcal{O}_X} \mathcal{L}^{\otimes -1} & \text{if} & n < -1 \end{matrix} \right.
```

Traduction :
```tex
\mathcal{L}^{\otimes n} = \left\{ \begin{matrix} \mathcal{O}_X & \text{si} & n = 0 \\ \SheafHom_{\mathcal{O}_X}(\mathcal{L}, \mathcal{O}_X) & \text{si} & n = -1\\ \mathcal{L} \otimes_{\mathcal{O}_X} \ldots \otimes_{\mathcal{O}_X} \mathcal{L} & \text{si} & n > 0 \\ \mathcal{L}^{\otimes -1} \otimes_{\mathcal{O}_X} \ldots \otimes_{\mathcal{O}_X} \mathcal{L}^{\otimes -1} & \text{si} & n < -1 \end{matrix} \right.
```

### Passage mathématique 2147

Source :
```tex
X_s = \{x \in X \mid \text{image }s \not\in \mathfrak m_x\mathcal{L}_x\}
```

Traduction :
```tex
X_s = \{x \in X \mid \text{image de }s \not\in \mathfrak m_x\mathcal{L}_x\}
```

### Passage mathématique 2202

Source :
```tex
\text{rank}_\mathcal{E} : X \longrightarrow \mathbf{Z}_{\geq 0},\quad x \longmapsto \text{rank}_{\mathcal{O}_{X, x}} \mathcal{E}_x
```

Traduction :
```tex
\text{rang}_\mathcal{E} : X \longrightarrow \mathbf{Z}_{\geq 0},\quad x \longmapsto \text{rang}_{\mathcal{O}_{X, x}} \mathcal{E}_x
```

### Passage mathématique 2203

Source :
```tex
\text{rank}_\mathcal{E}
```

Traduction :
```tex
\text{rang}_\mathcal{E}
```

### Passage mathématique 2206

Source :
```tex
\text{rank}_\mathcal{E} = \text{rank}_{\mathcal{E}'} + \text{rank}_{\mathcal{E}''}
```

Traduction :
```tex
\text{rang}_\mathcal{E} = \text{rang}_{\mathcal{E}'} + \text{rang}_{\mathcal{E}''}
```

### Passage mathématique 2207

Source :
```tex
K_0(\textit{Vect}(X)) \longrightarrow \text{Map}_{cont}(X, \mathbf{Z}),\quad [\mathcal{E}] \longmapsto \text{rank}_\mathcal{E}
```

Traduction :
```tex
K_0(\textit{Vect}(X)) \longrightarrow \text{Map}_{cont}(X, \mathbf{Z}),\quad [\mathcal{E}] \longmapsto \text{rang}_\mathcal{E}
```

### Passage mathématique 2215

Source :
```tex
\text{rank}_\mathcal{E}
```

Traduction :
```tex
\text{rang}_\mathcal{E}
```

### Passage mathématique 2241

Source :
```tex
s'_1 \wedge \ldots \wedge s'_{r'} \otimes s''_1 \wedge \ldots \wedge s''_{r''} \quad\text{to}\quad s'_1 \wedge \ldots \wedge s'_{r'} \wedge \tilde s''_1 \wedge \ldots \wedge \tilde s''_{r''}
```

Traduction :
```tex
s'_1 \wedge \ldots \wedge s'_{r'} \otimes s''_1 \wedge \ldots \wedge s''_{r''} \quad\text{sur}\quad s'_1 \wedge \ldots \wedge s'_{r'} \wedge \tilde s''_1 \wedge \ldots \wedge \tilde s''_{r''}
```

### Passage mathématique 2879

Source :
```tex
\label{equation-towards-constructible-sets} \text{Coequalizer}\left( \xymatrix{ \coprod\nolimits_{b = 1, \ldots, m} j_{V_b!}\underline{S_b} \ar@<1ex>[r] \ar@<-1ex>[r] & \coprod\nolimits_{a = 1, \ldots, n} j_{U_a!}\underline{S_a} } \right)
```

Traduction :
```tex
\label{equation-towards-constructible-sets} \text{Coégalisateur}\left( \xymatrix{ \coprod\nolimits_{b = 1, \ldots, m} j_{V_b!}\underline{S_b} \ar@<1ex>[r] \ar@<-1ex>[r] & \coprod\nolimits_{a = 1, \ldots, n} j_{U_a!}\underline{S_a} } \right)
```

