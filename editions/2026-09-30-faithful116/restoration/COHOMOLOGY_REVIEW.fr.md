# Chapitre 20 — lectures officielles rétablies

Copie de travail non reconstruite et non publiée. 1 opérations de contenu rétablies ; 0 choix de traduction idiomatique conservés. Les propositions ne sont pas déclarées fausses : elles restent séparées de la traduction de référence.

## COHOMOLOGY-CH20-OP001

[Source officielle, ligne 12907](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/cohomology.tex#L12907) · `lemma-internal-hom-evaluate-isom`.

Avant :
```tex
R\SheafHom(R\SheafHom(K_2, L), M) \to
```

Lecture rétablie :
```tex
R\SheafHom(R\SheafHom(K_2, L), M)
```

Rétablir la lecture exacte du texte officiel, sans appliquer la correction mathématique proposée. Celle-ci reste dans le dossier d'errata séparé.

## Traductions idiomatiques conservées


## Autres réglages de mise en page conservés

```tex
\sectionmark{Cohomologie de {\v C}ech des préfaisceaux}
```

Ce titre courant abrégé répète le sujet du titre de section ; il ne change aucun énoncé, référence ou preuve. Il reste dans le fichier de lecture et n'est retiré que de la copie de comparaison structurelle. La différence brute de commandes reste signalée.


## Limites du contrôle

La structure mathématique et les identifiants sont comparés au texte anglais intact, sans lui appliquer de corrections. Les textes traduits à l’intérieur des formules sont énumérés dans le dossier de contrôle ; la validation structurelle seule ne certifie pas toute la prose.

## Textes mathématiques traduits — comparaison lue

Les 53 paires ont été lues : cas des définitions de cochaînes et d'homotopies, quantificateurs, conjonctions, légendes des flèches, degrés, conditions de finitude et de torsion. Aucun de ces écarts de texte n'applique une correction au contenu anglais. Deux limites de langue restent visibles, sans être confondues avec un changement mathématique : « torsors » n'est pas francisé dans une formule et la locution « I-sans torsion O-modules » est maladroite. La présente validation porte sur le sens et la frontière éditoriale, non sur une certification de toute la prose.

### Passage mathématique 37

Source :
```tex
K(\mathcal{O}_X) = K(\textit{Mod}(\mathcal{O}_X)) \quad \text{and} \quad D(\mathcal{O}_X) = D(\textit{Mod}(\mathcal{O}_X)).
```

Traduction :
```tex
K(\mathcal{O}_X) = K(\textit{Mod}(\mathcal{O}_X)) \quad \text{et} \quad D(\mathcal{O}_X) = D(\textit{Mod}(\mathcal{O}_X)).
```

### Passage mathématique 169

Source :
```tex
U \longmapsto \{s \in \mathcal{L}(U) \text{ such that } \mathcal{O}_U \xrightarrow{s \cdot -} \mathcal{L}_U \text{ is an isomorphism}\}
```

Traduction :
```tex
U \longmapsto \{s \in \mathcal{L}(U) \text{ tel que } \mathcal{O}_U \xrightarrow{s \cdot -} \mathcal{L}_U \text{ est un isomorphisme}\}
```

### Passage mathématique 179

Source :
```tex
\begin{matrix} \text{invertible sheaves on }(X, \mathcal{O}_X) \\ \text{ up to isomorphism} \end{matrix} \longrightarrow \begin{matrix} \mathcal{O}_X^*\text{-torsors} \\ \text{ up to isomorphism} \end{matrix}
```

Traduction :
```tex
\begin{matrix} \text{faisceaux inversibles sur }(X, \mathcal{O}_X) \\ \text{ à isomorphisme près} \end{matrix} \longrightarrow \begin{matrix} \mathcal{O}_X^*\text{-torsors} \\ \text{ à isomorphisme près} \end{matrix}
```

### Passage mathématique 478

Source :
```tex
(j_{p!}\mathcal{G})(W) = \left\{ \begin{matrix} \mathcal{G}(W) & \text{if } W \subset U \\ 0 & \text{else.} \end{matrix} \right.
```

Traduction :
```tex
(j_{p!}\mathcal{G})(W) = \left\{ \begin{matrix} \mathcal{G}(W) & \text{si } W \subset U \\ 0 & \text{sinon.} \end{matrix} \right.
```

### Passage mathématique 511

Source :
```tex
H_i(K(\mathcal{U})_\bullet) = \left\{ \begin{matrix} 0 & \text{if} & i \not = 0 \\ \mathcal{O}_\mathcal{U} & \text{if} & i = 0 \end{matrix} \right.
```

Traduction :
```tex
H_i(K(\mathcal{U})_\bullet) = \left\{ \begin{matrix} 0 & \text{si} & i \not = 0 \\ \mathcal{O}_\mathcal{U} & \text{si} & i = 0 \end{matrix} \right.
```

### Passage mathématique 533

Source :
```tex
h(s)_{i_0 \ldots i_{p + 1}} = \left\{ \begin{matrix} 0 & \text{if} & i_0 \not = i_{\text{fix}} \\ s_{i_1 \ldots i_{p + 1}} & \text{if} & i_0 = i_{\text{fix}} \end{matrix} \right.
```

Traduction :
```tex
h(s)_{i_0 \ldots i_{p + 1}} = \left\{ \begin{matrix} 0 & \text{si} & i_0 \not = i_{\text{fix}} \\ s_{i_1 \ldots i_{p + 1}} & \text{si} & i_0 = i_{\text{fix}} \end{matrix} \right.
```

### Passage mathématique 583

Source :
```tex
\check{H}^p(\mathcal{U}, \mathcal{I}) = \left\{ \begin{matrix} \mathcal{I}(U) & \text{if} & p = 0 \\ 0 & \text{if} & p > 0 \end{matrix} \right.
```

Traduction :
```tex
\check{H}^p(\mathcal{U}, \mathcal{I}) = \left\{ \begin{matrix} \mathcal{I}(U) & \text{si} & p = 0 \\ 0 & \text{si} & p > 0 \end{matrix} \right.
```

### Passage mathématique 650

Source :
```tex
i : \textit{Mod}(\mathcal{O}_X) \to \textit{PMod}(\mathcal{O}_X) \quad\text{and}\quad \check{H}^0(\mathcal{U}, - ) : \textit{PMod}(\mathcal{O}_X) \to \text{Mod}_{\mathcal{O}_X(U)}.
```

Traduction :
```tex
i : \textit{Mod}(\mathcal{O}_X) \to \textit{PMod}(\mathcal{O}_X) \quad\text{et}\quad \check{H}^0(\mathcal{U}, - ) : \textit{PMod}(\mathcal{O}_X) \to \text{Mod}_{\mathcal{O}_X(U)}.
```

### Passage mathématique 1019

Source :
```tex
\begin{matrix} R\Gamma(X, \mathcal{F}) & \text{is represented by} & \Gamma(X, \mathcal{I}^\bullet) \\ Rf_*\mathcal{F} & \text{is represented by} & f_*\mathcal{I}^\bullet \\ R\Gamma(Y, Rf_*\mathcal{F}) & \text{is represented by} & \Gamma(Y, f_*\mathcal{I}^\bullet) \end{matrix}
```

Traduction :
```tex
\begin{matrix} R\Gamma(X, \mathcal{F}) & \text{est représenté par} & \Gamma(X, \mathcal{I}^\bullet) \\ Rf_*\mathcal{F} & \text{est représenté par} & f_*\mathcal{I}^\bullet \\ R\Gamma(Y, Rf_*\mathcal{F}) & \text{est représenté par} & \Gamma(Y, f_*\mathcal{I}^\bullet) \end{matrix}
```

### Passage mathématique 1174

Source :
```tex
\check{H}^p(\mathcal{V}, \mathcal{F}) \to \check{H}^p(\mathcal{U}, \mathcal{F}) \xrightarrow{\text{Lemma \ref{lemma-cech-cohomology}}} H^p(X, \mathcal{F})
```

Traduction :
```tex
\check{H}^p(\mathcal{V}, \mathcal{F}) \to \check{H}^p(\mathcal{U}, \mathcal{F}) \xrightarrow{\text{Lemme \ref{lemma-cech-cohomology}}} H^p(X, \mathcal{F})
```

### Passage mathématique 1202

Source :
```tex
B^{p, q} = \check{\mathcal{C}}^p(\mathcal{V}, \mathcal{J}^q) \quad \text{and} \quad A^{p, q} = \check{\mathcal{C}}^p(\mathcal{U}, \mathcal{I}^q).
```

Traduction :
```tex
B^{p, q} = \check{\mathcal{C}}^p(\mathcal{V}, \mathcal{J}^q) \quad \text{et} \quad A^{p, q} = \check{\mathcal{C}}^p(\mathcal{U}, \mathcal{I}^q).
```

### Passage mathématique 1208

Source :
```tex
(B')^{p, q} = \check{\mathcal{C}}^p(\mathcal{V}, (\mathcal{J}')^q) \quad \text{and} \quad (B'')^{p, q} = \check{\mathcal{C}}^p(\mathcal{V}, f_*\mathcal{I}^q).
```

Traduction :
```tex
(B')^{p, q} = \check{\mathcal{C}}^p(\mathcal{V}, (\mathcal{J}')^q) \quad \text{et} \quad (B'')^{p, q} = \check{\mathcal{C}}^p(\mathcal{V}, f_*\mathcal{I}^q).
```

### Passage mathématique 1267

Source :
```tex
\delta(\overline{h}) = \text{class of }\text{d}(g)\text{ in } \check{H}^{n + 1}(\mathcal{V}, \mathcal{F})
```

Traduction :
```tex
\delta(\overline{h}) = \text{classe de }\text{d}(g)\text{ dans } \check{H}^{n + 1}(\mathcal{V}, \mathcal{F})
```

### Passage mathématique 1338

Source :
```tex
\mathcal{I}'(V) = \{s \in \mathcal{I}|_Z(V) \mid \exists (U, t),\ U \subset X\text{ open}, \ t \in \mathcal{I}(U),\ V = Z \cap U,\ s = t|_{Z \cap U} \}
```

Traduction :
```tex
\mathcal{I}'(V) = \{s \in \mathcal{I}|_Z(V) \mid \exists (U, t),\ U \subset X\text{ ouvert}, \ t \in \mathcal{I}(U),\ V = Z \cap U,\ s = t|_{Z \cap U} \}
```

### Passage mathématique 1834

Source :
```tex
\textit{Ab}(X) \longrightarrow \textit{Ab}(Z),\quad \mathcal{F} \longmapsto \mathcal{H}_Z(\mathcal{F})\text{ viewed as a sheaf on }Z
```

Traduction :
```tex
\textit{Ab}(X) \longrightarrow \textit{Ab}(Z),\quad \mathcal{F} \longmapsto \mathcal{H}_Z(\mathcal{F})\text{ considéré comme faisceau sur }Z
```

### Passage mathématique 1968

Source :
```tex
\check{\mathcal{C}}_{alt}^p(\mathcal{U}, \mathcal{F}) = \left\{ \begin{matrix} s \in \check{\mathcal{C}}^p(\mathcal{U}, \mathcal{F}) \text{ such that } s_{i_0 \ldots i_p} = 0 \text{ if } i_n = i_m \text{ for some } n \not = m\\ \text{ and } s_{i_0\ldots i_n \ldots i_m \ldots i_p} = -s_{i_0\ldots i_m \ldots i_n \ldots i_p} \text{ in any case.} \end{matrix} \right\}
```

Traduction :
```tex
\check{\mathcal{C}}_{alt}^p(\mathcal{U}, \mathcal{F}) = \left\{ \begin{matrix} s \in \check{\mathcal{C}}^p(\mathcal{U}, \mathcal{F}) \text{ tel que } s_{i_0 \ldots i_p} = 0 \text{ si } i_n = i_m \text{ pour certains } n \not = m\\ \text{ et } s_{i_0\ldots i_n \ldots i_m \ldots i_p} = -s_{i_0\ldots i_m \ldots i_n \ldots i_p} \text{ dans tous les cas.} \end{matrix} \right\}
```

### Passage mathématique 2002

Source :
```tex
c(s)_{i_0\ldots i_p} = \left\{ \begin{matrix} 0 & \text{if} & i_n = i_m \text{ for some } n \not = m\\ \text{sgn}(\sigma) s_{i_{\sigma(0)}\ldots i_{\sigma(p)}} & \text{if} & i_{\sigma(0)} < i_{\sigma(1)} < \ldots < i_{\sigma(p)} \end{matrix} \right.
```

Traduction :
```tex
c(s)_{i_0\ldots i_p} = \left\{ \begin{matrix} 0 & \text{si} & i_n = i_m \text{ pour certains } n \not = m\\ \text{sgn}(\sigma) s_{i_{\sigma(0)}\ldots i_{\sigma(p)}} & \text{si} & i_{\sigma(0)} < i_{\sigma(1)} < \ldots < i_{\sigma(p)} \end{matrix} \right.
```

### Passage mathématique 2036

Source :
```tex
i_{\sigma(0)} \leq i_{\sigma(1)} \leq \ldots \leq i_{\sigma(p)} \quad \text{and} \quad \sigma(j) < \sigma(j + 1) \quad \text{if} \quad i_{\sigma(j)} = i_{\sigma(j + 1)}.
```

Traduction :
```tex
i_{\sigma(0)} \leq i_{\sigma(1)} \leq \ldots \leq i_{\sigma(p)} \quad \text{et} \quad \sigma(j) < \sigma(j + 1) \quad \text{si} \quad i_{\sigma(j)} = i_{\sigma(j + 1)}.
```

### Passage mathématique 2049

Source :
```tex
\begin{matrix} \text{id} & 0 & 1 & 2 & 3 \\ \sigma & 3 & 2 & 1 & 0 \end{matrix} \quad \text{and} \quad \begin{matrix} \text{id} & 0 & 1 & 2 & 3 \\ \tau & 3 & 0 & 2 & 1 \end{matrix}
```

Traduction :
```tex
\begin{matrix} \text{id} & 0 & 1 & 2 & 3 \\ \sigma & 3 & 2 & 1 & 0 \end{matrix} \quad \text{et} \quad \begin{matrix} \text{id} & 0 & 1 & 2 & 3 \\ \tau & 3 & 0 & 2 & 1 \end{matrix}
```

### Passage mathématique 2050

Source :
```tex
\begin{matrix} \text{id} & 0 & 1 & 2 & 3 \\ \sigma_0 & 0 & 1 & 2 & 3 \\ \sigma_1 & 3 & 0 & 1 & 2 \\ \sigma_2 & 3 & 2 & 0 & 1 \\ \sigma_3 & 3 & 2 & 1 & 0 \\ \end{matrix} \quad \text{and} \quad \begin{matrix} \text{id} & 0 & 1 & 2 & 3 \\ \tau_0 & 0 & 1 & 2 & 3 \\ \tau_1 & 3 & 0 & 1 & 2 \\ \tau_2 & 3 & 0 & 1 & 2 \\ \tau_3 & 3 & 0 & 2 & 1 \\ \end{matrix}
```

Traduction :
```tex
\begin{matrix} \text{id} & 0 & 1 & 2 & 3 \\ \sigma_0 & 0 & 1 & 2 & 3 \\ \sigma_1 & 3 & 0 & 1 & 2 \\ \sigma_2 & 3 & 2 & 0 & 1 \\ \sigma_3 & 3 & 2 & 1 & 0 \\ \end{matrix} \quad \text{et} \quad \begin{matrix} \text{id} & 0 & 1 & 2 & 3 \\ \tau_0 & 0 & 1 & 2 & 3 \\ \tau_1 & 3 & 0 & 1 & 2 \\ \tau_2 & 3 & 0 & 1 & 2 \\ \tau_3 & 3 & 0 & 2 & 1 \\ \end{matrix}
```

### Passage mathématique 2086

Source :
```tex
(dh + hd)(s)_{i_0 \ldots i_p} = \left\{ \begin{matrix} 0 & \text{if} & i_0 < i_1 < \ldots < i_p \\ s_{i_0 \ldots i_p} & \text{else} & \end{matrix} \right.
```

Traduction :
```tex
(dh + hd)(s)_{i_0 \ldots i_p} = \left\{ \begin{matrix} 0 & \text{si} & i_0 < i_1 < \ldots < i_p \\ s_{i_0 \ldots i_p} & \text{sinon} & \end{matrix} \right.
```

### Passage mathématique 2112

Source :
```tex
h : \text{cochains of degree }p + 1 \to \text{cochains of degree }p
```

Traduction :
```tex
h : \text{cochaînes de degré }p + 1 \to \text{cochaînes de degré }p
```

### Passage mathématique 2113

Source :
```tex
h(s)_{i_0 \ldots i_p} = 0 \text{ if } i \in \{i_0, \ldots, i_p\} \text{ and } h(s)_{i_0 \ldots i_p} = (-1)^j s_{i_0 \ldots i_j i i_{j + 1} \ldots i_p} \text{ if not}
```

Traduction :
```tex
h(s)_{i_0 \ldots i_p} = 0 \text{ si } i \in \{i_0, \ldots, i_p\} \text{ et } h(s)_{i_0 \ldots i_p} = (-1)^j s_{i_0 \ldots i_j i i_{j + 1} \ldots i_p} \text{ sinon}
```

### Passage mathématique 2334

Source :
```tex
h(\alpha)_{i_0 \ldots i_p} = \sum\nolimits_{a = 0}^p \epsilon_p(a) \alpha_{i_0 \ldots i_a i_p \ldots i_a} \quad\text{with}\quad \epsilon_p(a) = (-1)^{\frac{(p - a)(p - a - 1)}{2} + p}
```

Traduction :
```tex
h(\alpha)_{i_0 \ldots i_p} = \sum\nolimits_{a = 0}^p \epsilon_p(a) \alpha_{i_0 \ldots i_a i_p \ldots i_a} \quad\text{avec}\quad \epsilon_p(a) = (-1)^{\frac{(p - a)(p - a - 1)}{2} + p}
```

### Passage mathématique 2340

Source :
```tex
(-1)^k \epsilon_{p - 1}(a) + \epsilon_p(a)(-1)^{p + a + 1 - k} = 0 \quad\text{and}\quad (-1)^k\epsilon_{p - 1}(a - 1) + \epsilon_p(a) (-1)^k = 0
```

Traduction :
```tex
(-1)^k \epsilon_{p - 1}(a) + \epsilon_p(a)(-1)^{p + a + 1 - k} = 0 \quad\text{et}\quad (-1)^k\epsilon_{p - 1}(a - 1) + \epsilon_p(a) (-1)^k = 0
```

### Passage mathématique 2418

Source :
```tex
0 \to {\mathcal F}_1^\bullet \to {\mathcal F}_2^\bullet \to {\mathcal F}_3^\bullet \to 0 \quad\text{and}\quad 0 \leftarrow {\mathcal G}_1^\bullet \leftarrow {\mathcal G}_2^\bullet \leftarrow {\mathcal G}_3^\bullet \leftarrow 0
```

Traduction :
```tex
0 \to {\mathcal F}_1^\bullet \to {\mathcal F}_2^\bullet \to {\mathcal F}_3^\bullet \to 0 \quad\text{et}\quad 0 \leftarrow {\mathcal G}_1^\bullet \leftarrow {\mathcal G}_2^\bullet \leftarrow {\mathcal G}_3^\bullet \leftarrow 0
```

### Passage mathématique 2475

Source :
```tex
\overline{d(\alpha_2)} = d(\bar \alpha_2) = 0 \quad\text{and}\quad \overline{d(\beta_2)} = d(\bar \beta_2) = 0.
```

Traduction :
```tex
\overline{d(\alpha_2)} = d(\bar \alpha_2) = 0 \quad\text{et}\quad \overline{d(\beta_2)} = d(\bar \beta_2) = 0.
```

### Passage mathématique 2881

Source :
```tex
H^n(X, F^p\mathcal{F}^\bullet) = 0\text{ for }p \gg 0 \quad\text{and}\quad H^n(X, F^p\mathcal{F}^\bullet) = H^n(X, \mathcal{F}^\bullet)\text{ for }p \ll 0
```

Traduction :
```tex
H^n(X, F^p\mathcal{F}^\bullet) = 0\text{ pour }p \gg 0 \quad\text{et}\quad H^n(X, F^p\mathcal{F}^\bullet) = H^n(X, \mathcal{F}^\bullet)\text{ pour }p \ll 0
```

### Passage mathématique 2884

Source :
```tex
\Gamma(X, \mathcal{J}^\bullet) \quad\text{with}\quad F^p\Gamma(X, \mathcal{J}^\bullet) = \Gamma(X, F^p\mathcal{J}^\bullet)
```

Traduction :
```tex
\Gamma(X, \mathcal{J}^\bullet) \quad\text{avec}\quad F^p\Gamma(X, \mathcal{J}^\bullet) = \Gamma(X, F^p\mathcal{J}^\bullet)
```

### Passage mathématique 2898

Source :
```tex
\Gamma(X, \mathcal{I}^\bullet) \quad\text{with}\quad F^p\Gamma(X, \mathcal{I}^\bullet) = \Gamma(X, F^p\mathcal{I}^\bullet)
```

Traduction :
```tex
\Gamma(X, \mathcal{I}^\bullet) \quad\text{avec}\quad F^p\Gamma(X, \mathcal{I}^\bullet) = \Gamma(X, F^p\mathcal{I}^\bullet)
```

### Passage mathématique 2931

Source :
```tex
R^nf_*F^p\mathcal{F}^\bullet = 0 \text{ for }p \gg 0 \quad\text{and}\quad R^nf_*F^p\mathcal{F}^\bullet = R^nf_*\mathcal{F}^\bullet \text{ for }p \ll 0
```

Traduction :
```tex
R^nf_*F^p\mathcal{F}^\bullet = 0 \text{ pour }p \gg 0 \quad\text{et}\quad R^nf_*F^p\mathcal{F}^\bullet = R^nf_*\mathcal{F}^\bullet \text{ pour }p \ll 0
```

### Passage mathématique 3021

Source :
```tex
H^i(R\Gamma(X, K)) = \Hom_{D(\mathcal{O}_X)}(\mathcal{O}_X[-i], K) \quad\text{and}\quad H^j(R\Gamma(X, M)) = \Hom_{D(\mathcal{O}_X)}(\mathcal{O}_X[-j], M)
```

Traduction :
```tex
H^i(R\Gamma(X, K)) = \Hom_{D(\mathcal{O}_X)}(\mathcal{O}_X[-i], K) \quad\text{et}\quad H^j(R\Gamma(X, M)) = \Hom_{D(\mathcal{O}_X)}(\mathcal{O}_X[-j], M)
```

### Passage mathématique 3025

Source :
```tex
\tilde \xi : \mathcal{O}_X[-i] \to K \quad\text{and}\quad \tilde \eta : \mathcal{O}_X[-j] \to M
```

Traduction :
```tex
\tilde \xi : \mathcal{O}_X[-i] \to K \quad\text{et}\quad \tilde \eta : \mathcal{O}_X[-j] \to M
```

### Passage mathématique 3067

Source :
```tex
\xymatrix{ f_*\mathcal{K}^\bullet \otimes_{\mathcal{O}_Y}^\mathbf{L} f_*\mathcal{M}^\bullet \ar[r] \ar[d] & Rf_*\mathcal{K}^\bullet \otimes_{\mathcal{O}_Y}^\mathbf{L} Rf_*\mathcal{M}^\bullet \ar[d]^{\text{Remark \ref{remark-cup-product}}} \\ \text{Tot}( f_*\mathcal{K}^\bullet \otimes_{\mathcal{O}_Y} f_*\mathcal{M}^\bullet) \ar[d]_{\text{naive cup product}} & Rf_*(\mathcal{K}^\bullet \otimes_{\mathcal{O}_X}^\mathbf{L} \mathcal{M}^\bullet) \ar[d] \\ f_*\text{Tot}(\mathcal{K}^\bullet \otimes_{\mathcal{O}_X} \mathcal{M}^\bullet) \ar[r] & Rf_*\text{Tot}(\mathcal{K}^\bullet \otimes_{\mathcal{O}_X} \mathcal{M}^\bullet) }
```

Traduction :
```tex
\xymatrix{ f_*\mathcal{K}^\bullet \otimes_{\mathcal{O}_Y}^\mathbf{L} f_*\mathcal{M}^\bullet \ar[r] \ar[d] & Rf_*\mathcal{K}^\bullet \otimes_{\mathcal{O}_Y}^\mathbf{L} Rf_*\mathcal{M}^\bullet \ar[d]^{\text{Remarque \ref{remark-cup-product}}} \\ \text{Tot}( f_*\mathcal{K}^\bullet \otimes_{\mathcal{O}_Y} f_*\mathcal{M}^\bullet) \ar[d]_{\text{cup-produit naïf}} & Rf_*(\mathcal{K}^\bullet \otimes_{\mathcal{O}_X}^\mathbf{L} \mathcal{M}^\bullet) \ar[d] \\ f_*\text{Tot}(\mathcal{K}^\bullet \otimes_{\mathcal{O}_X} \mathcal{M}^\bullet) \ar[r] & Rf_*\text{Tot}(\mathcal{K}^\bullet \otimes_{\mathcal{O}_X} \mathcal{M}^\bullet) }
```

### Passage mathématique 3442

Source :
```tex
\textit{Mod}(\mathcal{O}_X) \longrightarrow \textit{Mod}(\mathcal{O}_X|_Z), \quad \mathcal{F} \longmapsto \mathcal{H}_Z(\mathcal{F}) \text{ viewed as an }\mathcal{O}_X|_Z\text{-module on }Z
```

Traduction :
```tex
\textit{Mod}(\mathcal{O}_X) \longrightarrow \textit{Mod}(\mathcal{O}_X|_Z), \quad \mathcal{F} \longmapsto \mathcal{H}_Z(\mathcal{F}) \text{ considéré comme }\mathcal{O}_X|_Z\text{-module sur }Z
```

### Passage mathématique 4148

Source :
```tex
H^p(U, H^{m - p}(E)) = 0 \text{ for } U \in \mathfrak{U}_x \text{ and } p > p(x, m)
```

Traduction :
```tex
H^p(U, H^{m - p}(E)) = 0 \text{ pour } U \in \mathfrak{U}_x \text{ et } p > p(x, m)
```

### Passage mathématique 4167

Source :
```tex
H^{m - 1}(U, K_{n + 1}) \to H^{m - 1}(U, K_n) \quad\text{and}\quad H^m(U, K_{n + 1}) \to H^m(U, K_n)
```

Traduction :
```tex
H^{m - 1}(U, K_{n + 1}) \to H^{m - 1}(U, K_n) \quad\text{et}\quad H^m(U, K_{n + 1}) \to H^m(U, K_n)
```

### Passage mathématique 4181

Source :
```tex
H^p(U, H^q(E)) = 0 \text{ for } U \in \mathfrak{U}_x,\ p > d_x, \text{ and }q < 0
```

Traduction :
```tex
H^p(U, H^q(E)) = 0 \text{ pour } U \in \mathfrak{U}_x,\ p > d_x, \text{ et }q < 0
```

### Passage mathématique 4204

Source :
```tex
H^p(U, H^q(E)) = 0 \text{ for } U \in \mathcal{B},\ p > d, \text{ and }q < 0
```

Traduction :
```tex
H^p(U, H^q(E)) = 0 \text{ pour } U \in \mathcal{B},\ p > d, \text{ et }q < 0
```

### Passage mathématique 4342

Source :
```tex
(M \xrightarrow{f^n} M) \quad\text{and}\quad \Coker(f^n : M \to M)
```

Traduction :
```tex
(M \xrightarrow{f^n} M) \quad\text{et}\quad \Coker(f^n : M \to M)
```

### Passage mathématique 4495

Source :
```tex
H^0(\SheafHom^\bullet(\mathcal{L}^\bullet, (\mathcal{I}')^\bullet)) \quad\text{and}\quad H^0(\SheafHom^\bullet((\mathcal{L}')^\bullet, \mathcal{I}^\bullet))
```

Traduction :
```tex
H^0(\SheafHom^\bullet(\mathcal{L}^\bullet, (\mathcal{I}')^\bullet)) \quad\text{et}\quad H^0(\SheafHom^\bullet((\mathcal{L}')^\bullet, \mathcal{I}^\bullet))
```

### Passage mathématique 4654

Source :
```tex
R\SheafHom(K, K') \otimes_{\mathcal{O}_X}^\mathbf{L} K \to K' \quad\text{and}\quad R\SheafHom(M, M') \otimes_{\mathcal{O}_X}^\mathbf{L} M \to M'
```

Traduction :
```tex
R\SheafHom(K, K') \otimes_{\mathcal{O}_X}^\mathbf{L} K \to K' \quad\text{et}\quad R\SheafHom(M, M') \otimes_{\mathcal{O}_X}^\mathbf{L} M \to M'
```

### Passage mathématique 4844

Source :
```tex
(\{K_{U'}\}_{U' \in \mathcal{B}'}, \{\rho_{V'}^{U'}\}_{V' \subset U'\text{ with }U', V' \in \mathcal{B}'})
```

Traduction :
```tex
(\{K_{U'}\}_{U' \in \mathcal{B}'}, \{\rho_{V'}^{U'}\}_{V' \subset U'\text{ avec }U', V' \in \mathcal{B}'})
```

### Passage mathématique 4888

Source :
```tex
(\{K_{U'}\}_{U' \in \mathcal{B}'}, \{\rho_{V'}^{U'}\}_{V' \subset U'\text{ with }U', V' \in \mathcal{B}'})
```

Traduction :
```tex
(\{K_{U'}\}_{U' \in \mathcal{B}'}, \{\rho_{V'}^{U'}\}_{V' \subset U'\text{ avec }U', V' \in \mathcal{B}'})
```

### Passage mathématique 4915

Source :
```tex
(\{K_U\}_{U \in \mathcal{B}^*}, \{\rho_V^U\}_{V \subset U\text{ with }U, V \in \mathcal{B}^*})
```

Traduction :
```tex
(\{K_U\}_{U \in \mathcal{B}^*}, \{\rho_V^U\}_{V \subset U\text{ avec }U, V \in \mathcal{B}^*})
```

### Passage mathématique 5025

Source :
```tex
S_\alpha = (\{K_U\}_{U \in \mathcal{B}_\alpha}, \{\rho_V^U\}_{V \subset U\text{ with }U, V \in \mathcal{B}_\alpha})
```

Traduction :
```tex
S_\alpha = (\{K_U\}_{U \in \mathcal{B}_\alpha}, \{\rho_V^U\}_{V \subset U\text{ avec }U, V \in \mathcal{B}_\alpha})
```

### Passage mathématique 5037

Source :
```tex
(\{K_U\}_{U \in \mathcal{B}_\alpha^*}, \{\rho_V^U\}_{V \subset U\text{ with }U, V \in \mathcal{B}_\alpha^*})
```

Traduction :
```tex
(\{K_U\}_{U \in \mathcal{B}_\alpha^*}, \{\rho_V^U\}_{V \subset U\text{ avec }U, V \in \mathcal{B}_\alpha^*})
```

### Passage mathématique 5070

Source :
```tex
(\{K_V\}_{V \subset U, V \in \mathcal{B}_\beta\text{ for some }\beta < \alpha}, \{\rho_V^{V'}\}_{V \subset V'\text{ with }V, V' \subset U \text{ and }V, V' \in \mathcal{B}_\beta\text{ for some }\beta < \alpha})
```

Traduction :
```tex
(\{K_V\}_{V \subset U, V \in \mathcal{B}_\beta\text{ pour un certain }\beta < \alpha}, \{\rho_V^{V'}\}_{V \subset V'\text{ avec }V, V' \subset U \text{ et }V, V' \in \mathcal{B}_\beta\text{ pour un certain }\beta < \alpha})
```

### Passage mathématique 5820

Source :
```tex
U = \{x \in X \mid H^i(E)_x\text{ is a finite free } \mathcal{O}_{X, x}\text{-module for all }i\in \mathbf{Z}\}
```

Traduction :
```tex
U = \{x \in X \mid H^i(E)_x\text{ est un } \mathcal{O}_{X, x}\text{-module libre de type fini pour tout }i\in \mathbf{Z}\}
```

### Passage mathématique 5870

Source :
```tex
\eta : \mathcal{O}_X \to \text{Tot}(\mathcal{F}^\bullet \otimes_{\mathcal{O}_X} \mathcal{G}^\bullet) \quad\text{and}\quad \epsilon : \text{Tot}(\mathcal{G}^\bullet \otimes_{\mathcal{O}_X} \mathcal{F}^\bullet) \to \mathcal{O}_X
```

Traduction :
```tex
\eta : \mathcal{O}_X \to \text{Tot}(\mathcal{F}^\bullet \otimes_{\mathcal{O}_X} \mathcal{G}^\bullet) \quad\text{et}\quad \epsilon : \text{Tot}(\mathcal{G}^\bullet \otimes_{\mathcal{O}_X} \mathcal{F}^\bullet) \to \mathcal{O}_X
```

### Passage mathématique 6293

Source :
```tex
\alpha : \mathcal{O}_X \to \text{Tot}(\mathcal{E}^\bullet \otimes_{\mathcal{O}_X} \mathcal{F}^\bullet) \quad\text{and}\quad \beta : \text{Tot}(\mathcal{E}^\bullet \otimes_{\mathcal{O}_X} \mathcal{F}^\bullet) \to \mathcal{O}_X
```

Traduction :
```tex
\alpha : \mathcal{O}_X \to \text{Tot}(\mathcal{E}^\bullet \otimes_{\mathcal{O}_X} \mathcal{F}^\bullet) \quad\text{et}\quad \beta : \text{Tot}(\mathcal{E}^\bullet \otimes_{\mathcal{O}_X} \mathcal{F}^\bullet) \to \mathcal{O}_X
```

### Passage mathématique 6575

Source :
```tex
\eta_f : K(\mathcal{I}\text{-torsion free }\mathcal{O}_X\text{-modules}) \longrightarrow K(\mathcal{I}\text{-torsion free }\mathcal{O}_X\text{-modules})
```

Traduction :
```tex
\eta_f : K(\mathcal{I}\text{-sans torsion }\mathcal{O}_X\text{-modules}) \longrightarrow K(\mathcal{I}\text{-sans torsion }\mathcal{O}_X\text{-modules})
```

### Passage mathématique 6737

Source :
```tex
\label{equation-second-homotopy} h(s)_{i_0 \ldots i_p} = \left\{ \begin{matrix} 0 & \text{if} & i_0 < i_1 < \ldots < i_p \\ (-1)^a s_{i_0 \ldots i_{a - 1} i_a i_a i_{a + 1} \ldots i_p} & \text{if} & i_0 < i_1 < \ldots < i_{a - 1} < i_a = i_{a + 1} \end{matrix} \right.
```

Traduction :
```tex
\label{equation-second-homotopy} h(s)_{i_0 \ldots i_p} = \left\{ \begin{matrix} 0 & \text{si} & i_0 < i_1 < \ldots < i_p \\ (-1)^a s_{i_0 \ldots i_{a - 1} i_a i_a i_{a + 1} \ldots i_p} & \text{si} & i_0 < i_1 < \ldots < i_{a - 1} < i_a = i_{a + 1} \end{matrix} \right.
```

