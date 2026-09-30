# Chapitre 75 — fidélité au témoin officiel

**Réparation locale partielle : ni chapitre intégralement vérifié, ni PDF reconstruit, ni publication corrigée.**

Ces modifications ne décident pas que la lecture officielle est mathématiquement meilleure. Elles retirent des interventions éditoriales de la traduction de référence. Les propositions initiales restent lisibles ci-dessous et dans le dossier machine. Les corrections de la source appartiennent à une édition distincte.

[Source de travail](staged/fr/075_spaces-perfect.fr.tex) · [Contrôles](SPACES-PERFECT_PARTIAL_VALIDATION.json) · [Contextes complets](SPACES-PERFECT_CONTEXTUAL_RESTORATIONS.json)

## Rétablissements lus et exactement délimités

### FR-SPACES-PERFECT-FIDELITY-001 — `lemma-base-change-module-support-proper-over-base`

[Source officielle, ligne 1084](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L1084)

L'astérisque sans exposant est exactement la lecture de la première phrase de la preuve officielle. L'énoncé et la formule du support gardent leurs vrais exposants : aucune substitution globale.

Témoin officiel :
```tex
$(g')*\mathcal{F}$
```
Avant :
```tex
$(g')^*\mathcal{F}$ est de type fini
```
Après :
```tex
$(g')*\mathcal{F}$ est de type fini
```

### FR-SPACES-PERFECT-FIDELITY-002 — `lemma-direct-image-coherent`

[Source officielle, ligne 1210](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L1210)

La traduction avait remplacé l'objet E par son image directe dérivée dans la conclusion intermédiaire. Même si la modification semble rendre la preuve cohérente, elle n'est pas la lecture du témoin officiel.

Témoin officiel :
```tex
$E \in D_{\textit{Coh}}(\mathcal{O}_Y)$
```
Avant :
```tex
$Rf_*E \in D_{\textit{Coh}}(\mathcal{O}_Y)$
```
Après :
```tex
$E \in D_{\textit{Coh}}(\mathcal{O}_Y)$
```

### FR-SPACES-PERFECT-FIDELITY-003 — `lemma-direct-image-coherent-bdd-below`

[Source officielle, ligne 1225](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L1225)

Rétablir la base S de l'hypothèse de propreté. Changer S en Y est une modification d'hypothèse, non une traduction.

Témoin officiel :
```tex
is proper over $S$ for all $i$.
```
Avant :
```tex
soit propre au-dessus de $Y$ pour tout $i$.
```
Après :
```tex
soit propre au-dessus de $S$ pour tout $i$.
```

### FR-SPACES-PERFECT-FIDELITY-004 — `lemma-induction-principle`

[Source officielle, ligne 1418](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L1418)

Rétablir l'indice 1 de la phrase officielle, sans changer la famille indexée ailleurs dans la preuve.

Témoin officiel :
```tex
P$ holds for each $V_{p, 1}$
```
Avant :
```tex
chaque $V_{p, i}$
```
Après :
```tex
chaque $V_{p, 1}$
```

### FR-SPACES-PERFECT-FIDELITY-005 — `lemma-induction-principle-enlarge`

[Source officielle, ligne 1524](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L1524)

L'union est cohérente avec la définition précédente, mais le témoin officiel imprime ici une intersection. Conserver cette discordance dans la traduction de référence et l'isoler comme proposition de correction.

Témoin officiel :
```tex
$W_{n + 1} = W \cap U_{n + 1} = W$
```
Avant :
```tex
$W_{n + 1} = W \cup U_{n + 1} = W$
```
Après :
```tex
$W_{n + 1} = W \cap U_{n + 1} = W$
```

### FR-SPACES-PERFECT-FIDELITY-006 — `lemma-unbounded-relative-mayer-vietoris`

[Source officielle, ligne 1785](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L1785)

L'intersection de la phrase de prose avait été remplacée par un produit fibré. Restaurer cette seule phrase ; les produits fibrés des triangles restent tels quels.

Témoin officiel :
```tex
Similarly for $U$, $V$, and $U \cap V$
```
Avant :
```tex
sur $U$, $V$ et $U \times_X V$,
```
Après :
```tex
sur $U$, $V$ et $U \cap V$,
```

### FR-SPACES-PERFECT-FIDELITY-007 — `lemma-restrict-lower-shriek`

[Source officielle, ligne 1904](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L1904)

Rétablir Y dans le morphisme donné. Ne pas confondre fidélité au témoin et correction du codomaine attendu par le produit fibré suivant.

Témoin officiel :
```tex
Given an \'etale morphism $V \to Y$
```
Avant :
```tex
Pour tout morphisme \'etale $V \to X$
```
Après :
```tex
Pour tout morphisme \'etale $V \to Y$
```

### FR-SPACES-PERFECT-FIDELITY-008 — `lemma-argument-proves`

[Source officielle, ligne 2279](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L2279)

Le premier domaine affiché est U dans la source, malgré V dans le diagramme et dans le foncteur sous-jacent. Conserver les deux lectures à leurs emplacements respectifs.

Témoin officiel :
```tex
\Phi : D(\QCoh(\mathcal{O}_U)) \to D(\QCoh(\mathcal{O}_W))
```
Avant :
```tex
\Phi : D(\QCoh(\mathcal{O}_V)) \to D(\QCoh(\mathcal{O}_W))
```
Après :
```tex
\Phi : D(\QCoh(\mathcal{O}_U)) \to D(\QCoh(\mathcal{O}_W))
```

### FR-SPACES-PERFECT-FIDELITY-009 — `lemma-argument-proves`

[Source officielle, ligne 2398](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L2398)

Rétablir l'absence de degré à cette occurrence seulement. Les autres occurrences du complexe A avec un point en exposant ne sont pas modifiées.

Témoin officiel :
```tex
$\mathcal{A} \to j_{U, *}\mathcal{C}^\bullet$.
```
Avant :
```tex
morphisme de complexes
$\mathcal{A}^\bullet \to j_{U, *}\mathcal{C}^\bullet$. Autrement dit
```
Après :
```tex
morphisme de complexes
$\mathcal{A} \to j_{U, *}\mathcal{C}^\bullet$. Autrement dit
```

### FR-SPACES-PERFECT-FIDELITY-010 — `lemma-lift-map-from-perfect-complex-with-support`

[Source officielle, ligne 3633](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L3633)

Rétablir le produit sans base X dans le deuxième terme de ce seul affichage. Les autres produits fibrés restent inchangés.

Témoin officiel :
```tex
Q|_{W \times_X V} \to (P \oplus P[1])|_{W \times V}
```
Avant :
```tex
Q|_{W \times_X V} \to (P \oplus P[1])|_{W \times_X V}
```
Après :
```tex
Q|_{W \times_X V} \to (P \oplus P[1])|_{W \times V}
```

### FR-SPACES-PERFECT-FIDELITY-011 — `lemma-compact-is-perfect-with-support`

[Source officielle, ligne 3962](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L3962)

La restriction à la sous-catégorie quasi-cohérente est une correction de l'argument, non une simple francisation. La traduire comme si elle venait de la source était une liberté éditoriale.

Témoin officiel :
```tex
the perfect objects define compact objects of $D(\mathcal{O}_X)$
```
Avant :
```tex
$D_\QCoh(\mathcal{O}_X)$, et donc a fortiori
```
Après :
```tex
$D(\mathcal{O}_X)$, et donc a fortiori
```

### FR-SPACES-PERFECT-FIDELITY-012 — `lemma-better-coherator`

[Source officielle, ligne 4459](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L4459)

Rétablir le nom K quantifié par la source, sans renommer le triangle. Le défaut de cohérence éventuel appartient au dossier d'errata.

Témoin officiel :
```tex
for every object $K$ of
```
Avant :
```tex
pour tout objet $E$ de
```
Après :
```tex
pour tout objet $K$ de
```

### FR-SPACES-PERFECT-FIDELITY-013 — `lemma-locally-closed-where-H0-locally-free`

[Source officielle, ligne 6592](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L6592)

Le degré 0 de la condition (4)(b) a été remplacé par a. Restaurer 0 à cet emplacement, pas dans les conditions (1)–(3).

Témoin officiel :
```tex
$H^0(Lf^*E)$ is a locally free
```
Avant :
```tex
\item $H^a(Lf^*E)$ est un
```
Après :
```tex
\item $H^0(Lf^*E)$ est un
```

### FR-SPACES-PERFECT-FIDELITY-014 — `lemma-locally-closed-where-H0-locally-free`

[Source officielle, ligne 6596](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L6596)

Les deux degrés de la condition (4)(c) redeviennent 0 comme dans la source. La proposition de degré a est conservée dans le passage avant correction de ce dossier.

Témoin officiel :
```tex
\SheafHom_{\mathcal{O}_Y}(H^0(Lf^*E), H^0(Lf^*E))
```
Avant :
```tex
\SheafHom_{\mathcal{O}_Y}(H^a(Lf^*E),H^a(Lf^*E))
```
Après :
```tex
\SheafHom_{\mathcal{O}_Y}(H^0(Lf^*E),H^0(Lf^*E))
```

### FR-SPACES-PERFECT-FIDELITY-015 — `lemma-direct-image-coherator`

[Source officielle, ligne 2586](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L2586)

Rétablir X dans le codomaine écrit dans cette invocation de l'adjonction ; la base W du contexte n'autorise pas une correction silencieuse.

Témoin officiel :
```tex
j_* : \QCoh(\mathcal{O}_U) \to \QCoh(\mathcal{O}_X)
```
Avant :
```tex
j_* : \QCoh(\mathcal{O}_U) \to \QCoh(\mathcal{O}_W)
```
Après :
```tex
j_* : \QCoh(\mathcal{O}_U) \to \QCoh(\mathcal{O}_X)
```

### FR-SPACES-PERFECT-FIDELITY-016 — `lemma-direct-image-coherator`

[Source officielle, ligne 2588](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L2588)

Rétablir également le domaine X du foncteur adjoint, au même emplacement.

Témoin officiel :
```tex
j^* : \QCoh(\mathcal{O}_X) \to \QCoh(\mathcal{O}_U)
```
Avant :
```tex
j^* : \QCoh(\mathcal{O}_W) \to \QCoh(\mathcal{O}_U)
```
Après :
```tex
j^* : \QCoh(\mathcal{O}_X) \to \QCoh(\mathcal{O}_U)
```

### FR-SPACES-PERFECT-FIDELITY-017 — `lemma-affine-injective-colimit-direct-sum-pushforwards-artin`

[Source officielle, ligne 2638](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L2638)

La première notation de l'anneau quotient omet p dans la source. Le p ajouté par la traduction est retiré seulement à cet emplacement ; la formule définissant Z_n reste complète.

Témoin officiel :
```tex
over
$A_\mathfrak/\mathfrak p^nA_\mathfrak p$
```
Avant :
```tex
sur
$A_\mathfrak p/\mathfrak p^nA_\mathfrak p$
```
Après :
```tex
sur
$A_\mathfrak/\mathfrak p^nA_\mathfrak p$
```

### FR-SPACES-PERFECT-FIDELITY-018 — `lemma-affine-injective-colimit-direct-sum-pushforwards-artin`

[Source officielle, ligne 2645](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L2645)

Même omission du témoin dans l'anneau agissant sur le module fini ; restauration à cette seconde occurrence exactement délimitée.

Témoin officiel :
```tex
finite $A_\mathfrak/\mathfrak p^nA_\mathfrak p$-module
```
Avant :
```tex
$A_\mathfrak p/\mathfrak p^nA_\mathfrak p$-module fini
```
Après :
```tex
$A_\mathfrak/\mathfrak p^nA_\mathfrak p$-module fini
```

### FR-SPACES-PERFECT-FIDELITY-019 — `lemma-affine-injective-colimit-direct-sum-pushforwards-artin`

[Source officielle, ligne 2642](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L2642)

Le témoin imprime X comme cible à cet endroit, alors que S est l'espace initial. Garder le défaut du témoin hors d'une correction éditoriale silencieuse.

Témoin officiel :
```tex
$(Z_n \to X)_*\mathcal{G}_n$
```
Avant :
```tex
$(Z_n \to S)_*\mathcal{G}_n$
```
Après :
```tex
$(Z_n \to X)_*\mathcal{G}_n$
```

### FR-SPACES-PERFECT-FIDELITY-020 — `lemma-affine-injective-colimit-direct-sum-pushforwards-artin`

[Source officielle, ligne 2644](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L2644)

La variante de fonte mathfrak G_n est celle du témoin anglais ; ne pas la normaliser silencieusement en mathcal G_n.

Témoin officiel :
```tex
$\mathfrak G_n$ the coherent sheaf
```
Avant :
```tex
$\mathcal{G}_n$ est le faisceau
```
Après :
```tex
$\mathfrak G_n$ est le faisceau
```

### FR-SPACES-PERFECT-FIDELITY-021 — `equation-E-is-OK`

[Source officielle, ligne 4215](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L4215)

La preuve source invoque ici la compacité dans D(O_X), non dans sa sous-catégorie quasi-cohérente.

Témoin officiel :
```tex
$D(\mathcal{O}_X)$, see Proposition
```
Avant :
```tex
$D_\QCoh(\mathcal{O}_X)$; voir la proposition
```
Après :
```tex
$D(\mathcal{O}_X)$; voir la proposition
```

### FR-SPACES-PERFECT-FIDELITY-022 — `equation-E-is-OK`

[Source officielle, ligne 4216](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L4216)

Retirer la restriction de codomaine ajoutée dans la prose de l'argument ; elle change précisément l'affirmation de pleine fidélité de la source.

Témoin officiel :
```tex
the functor above is fully
faithful
```
Avant :
```tex
ci-dessus \`a valeurs dans $D_\QCoh(\mathcal{O}_X)$ est pleinement fid\`ele
```
Après :
```tex
ci-dessus est pleinement fid\`ele
```

### FR-SPACES-PERFECT-FIDELITY-023 — `equation-E-is-OK`

[Source officielle, ligne 4221](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L4221)

Rétablir le domaine complet de RHom au premier affichage. La restriction quasi-cohérente ultérieure reste à son emplacement officiel.

Témoin officiel :
```tex
R\Hom(K^\bullet, - ) : D(\mathcal{O}_X) \longrightarrow D(E, \text{d})
```
Avant :
```tex
R\Hom(K^\bullet, - ) : D_\QCoh(\mathcal{O}_X) \longrightarrow D(E, \text{d})
```
Après :
```tex
R\Hom(K^\bullet, - ) : D(\mathcal{O}_X) \longrightarrow D(E, \text{d})
```

### FR-SPACES-PERFECT-FIDELITY-024 — `remark-explain-consequence`

[Source officielle, ligne 4561](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L4561)

Le terme final du triangle, naturellement implicite, avait été ajouté explicitement. Reprendre l'affichage incomplet du témoin, sans ajouter de nouveau contenu à la traduction de référence.

Témoin officiel :
```tex
\to Rj_{U \times_X V, *}DQ_{U \times_X V}(K|_{U \times_X V}) \to
$$
```
Avant :
```tex
\to Rj_{U \times_X V, *}DQ_{U \times_X V}(K|_{U \times_X V})
\to DQ_X(K)[1]
$$
```
Après :
```tex
\to Rj_{U \times_X V, *}DQ_{U \times_X V}(K|_{U \times_X V}) \to
$$
```

### FR-SPACES-PERFECT-FIDELITY-025 — `lemma-boundedness-better-coherator`

[Source officielle, ligne 4598](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L4598)

La traduction avait réparé simultanément l'espace ambiant et un conflit de variables W/T. Rétablir les deux phrases officielles comme unité, sans modifier l'énoncé du lemme.

Témoin officiel :
```tex
Now suppose $K$ is in $D(\mathcal{O}_X)$ with
$H^i(W, K) = 0$ for all affine $W$ \'etale over $X$
```
Avant :
```tex
Supposons maintenant que $K$ appartienne à $D(\mathcal{O}_W)$ et que
$H^i(T, K) = 0$ pour tout $T$ affine étale sur $W$
```
Après :
```tex
Supposons maintenant que $K$ appartienne à $D(\mathcal{O}_X)$ et que
$H^i(W, K) = 0$ pour tout $W$ affine étale sur $X$
```

### FR-SPACES-PERFECT-FIDELITY-026 — `lemma-boundedness-better-coherator`

[Source officielle, ligne 4601](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L4601)

Rétablir RQ plutôt que DQ aux deux premières occurrences de ce paragraphe. Les DQ des images directes du paragraphe suivant sont officiels et restent inchangés.

Témoin officiel :
```tex
$RQ_U(K|_U)$ and $RQ_V(K|_V)$
```
Avant :
```tex
Il en résulte que $DQ_U(K|_U)$, $DQ_V(K|_V)$ et
```
Après :
```tex
Il en résulte que $RQ_U(K|_U)$, $RQ_V(K|_V)$ et
```

### FR-SPACES-PERFECT-FIDELITY-027 — `lemma-boundedness-better-coherator`

[Source officielle, ligne 4602](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L4602)

Rétablir simultanément le nom RQ et l'indice U cap V à cette troisième occurrence, sans toucher à l'argument du foncteur.

Témoin officiel :
```tex
$RQ_{U \cap V}(K|_{U \times_W V})$
```
Avant :
```tex
$DQ_{U \times_W V}(K|_{U \times_W V})$ ont leurs
```
Après :
```tex
$RQ_{U \cap V}(K|_{U \times_W V})$ ont leurs
```

### FR-SPACES-PERFECT-FIDELITY-028 — `lemma-boundedness-better-coherator`

[Source officielle, ligne 4603](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L4603)

Le crochet fermant ajouté était une réparation typographique de la source mathématique ; il est retiré dans la copie diplomatique et reste proposé séparément.

Témoin officiel :
```tex
$[a, b + \max(N(U), N(V), N(U \times_W V))$
```
Avant :
```tex
$[a, b + \max(N(U), N(V), N(U \times_W V))]$
```
Après :
```tex
$[a, b + \max(N(U), N(V), N(U \times_W V))$
```

### FR-SPACES-PERFECT-FIDELITY-029 — `lemma-boundedness-better-coherator`

[Source officielle, ligne 4609](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L4609)

Rétablir l'indice de l'image directe dans la dernière phrase, en conservant le DQ et le produit fibré de son argument.

Témoin officiel :
```tex
$Rj_{U \cap V, *}DQ_{U \times_W V}(K|_{U \times_W V})$
```
Avant :
```tex
$Rj_{U \times_W V, *}DQ_{U \times_W V}(K|_{U \times_W V})$ aient
```
Après :
```tex
$Rj_{U \cap V, *}DQ_{U \times_W V}(K|_{U \times_W V})$ aient
```

### FR-SPACES-PERFECT-FIDELITY-030 — `lemma-generator-with-support`

[Source officielle, ligne 3812](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L3812)

Rétablir r dans cette équation, bien que la liste qui précède et le complexe de Koszul utilisent s. La traduction de référence ne doit pas résoudre silencieusement cette discordance.

Témoin officiel :
```tex
$f^{-1}(Z \cap T) = V(g_1, \ldots, g_r)$
```
Avant :
```tex
$f^{-1}(Z\cap T)=V(g_1,\ldots,g_s)$
```
Après :
```tex
$f^{-1}(Z\cap T)=V(g_1,\ldots,g_r)$
```

### FR-SPACES-PERFECT-FIDELITY-031 — `lemma-generator-with-support`

[Source officielle, ligne 3836](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L3836)

Les deux objets du diagramme avaient été remplacés par leurs images inverses. Rétablir ensemble les deux sommets officiels, sans changer la discussion du support autour du diagramme.

Témoin officiel :
```tex
W \ar[r]_j & V & Z \cap T \ar[l] \ar[d] \\
V \setminus f^{-1}Z \ar[u]^{j'} \ar[ru]_{j''} & & Z \ar[lu]
```
Avant :
```tex
W \ar[r]_j & V & f^{-1}(Z \cap T) \ar[l] \ar[d] \\
V \setminus f^{-1}Z \ar[u]^{j'} \ar[ru]_{j''} & & f^{-1}Z \ar[lu]
```
Après :
```tex
W \ar[r]_j & V & Z \cap T \ar[l] \ar[d] \\
V \setminus f^{-1}Z \ar[u]^{j'} \ar[ru]_{j''} & & Z \ar[lu]
```

### FR-SPACES-PERFECT-FIDELITY-032 — `lemma-generator-with-support`

[Source officielle, ligne 3844](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L3844)

Les deux restrictions de cet affichage reprennent U cap V, comme le témoin. Le remplacement par le produit fibré était une intervention mathématique et non un changement d'ordre des mots français.

Témoin officiel :
```tex
E|_V = Rj_*(E|_W) = Rj_*(Rj'_*(E|_{U \cap V})) = Rj''_*(E|_{U \cap V})
```
Avant :
```tex
E|_V = Rj_*(E|_W) = Rj_*(Rj'_*(E|_{U \times_X V})) =
Rj''_*(E|_{U \times_X V})
```
Après :
```tex
E|_V = Rj_*(E|_W) = Rj_*(Rj'_*(E|_{U \cap V})) =
Rj''_*(E|_{U \cap V})
```

### FR-SPACES-PERFECT-FIDELITY-033 — `lemma-tor-independent`

[Source officielle, ligne 4857](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L4857)

La source répète le morphisme vers les sections de X. Restaurer cette répétition au second morphisme ; la correction attendue vers Y reste dans le dossier séparé.

Témoin officiel :
```tex
and
$\Gamma(B, \mathcal{O}_B) \to \Gamma(X, \mathcal{O}_X)$
```
Avant :
```tex
$\Gamma(B,\mathcal{O}_B)\to\Gamma(Y,\mathcal{O}_Y)$, montre alors
```
Après :
```tex
$\Gamma(B,\mathcal{O}_B)\to\Gamma(X,\mathcal{O}_X)$, montre alors
```

### FR-SPACES-PERFECT-FIDELITY-034 — `lemma-descend-finite-type`

[Source officielle, ligne 2891](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L2891)

Le second prime avait été ajouté pour corriger le choix de voisinage. Rétablir la condition effectivement écrite ; les autres morphismes de source X'' restent inchangés.

Témoin officiel :
```tex
in the image of $X' \to X$ and such that
```
Avant :
```tex
\`a l'image de $X'' \to X$ et que
```
Après :
```tex
\`a l'image de $X' \to X$ et que
```

### FR-SPACES-PERFECT-FIDELITY-035 — `lemma-tor-dimension-rel`

[Source officielle, ligne 3040](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L3040)

Le point géométrique remplaçait X dans une phrase dont la source porte manifestement une anomalie. La copie de référence reprend X ; la proposition de correction n'est pas perdue.

Témoin officiel :
```tex
Since the stalk of $\mathcal{O}_{X_\etale}$ at $X$ is
```
Avant :
```tex
Comme la fibre de $\mathcal{O}_{X_\etale}$ en $\overline{x}$ est
```
Après :
```tex
Comme la fibre de $\mathcal{O}_{X_\etale}$ en $X$ est
```

### FR-SPACES-PERFECT-FIDELITY-036 — `remark-DQCoh-is-Ddga-with-support`

[Source officielle, ligne 4243](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L4243)

Retirer seulement la structure sur S ajoutée dans cette phrase. Le schéma S introduit par la première phrase officielle reste présent.

Témoin officiel :
```tex
Let $X$ be a quasi-compact and quasi-separated algebraic space.
```
Avant :
```tex
quasi-s\'epar\'e sur $S$. Soit $T\subset|X|$
```
Après :
```tex
quasi-s\'epar\'e. Soit $T\subset|X|$
```

### FR-SPACES-PERFECT-FIDELITY-037 — `lemma-proper-flat-h0`

[Source officielle, ligne 6651](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L6651)

Retirer le codomaine ajouté à la notation de la projection, sans altérer la section diagonale ni les morphismes de l'affichage suivant.

Témoin officiel :
```tex
The morphism $\text{pr}_1 : X \times_Y X$ has a section
```
Avant :
```tex
Le morphisme $\text{pr}_1:X\times_YX\to X$ poss\`ede
```
Après :
```tex
Le morphisme $\text{pr}_1:X\times_YX$ poss\`ede
```

### FR-SPACES-PERFECT-FIDELITY-038 — `lemma-resolution-property-goes-down-finite-flat`

[Source officielle, ligne 6999](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L6999)

La traduction avait développé et réparé l'étape de preuve au lieu de traduire « Taking duals ». La lecture officielle est rétablie. « En passant aux duaux » est attesté chez J.-L. Verdier, Classe d'homologie associée à un cycle, Astérisque 36–37 (1976), p. 148, avant la définition 3.6.1 (https://www.numdam.org/article/AST_1976__36-37__101_0.pdf#page=49), passage consulté avant ce choix. Cette attestation justifie la locution française, pas la validité de l'étape de preuve de Stacks.

Témoin officiel :
```tex
Taking duals we get a surjection
```
Avant :
```tex
En tensorisant cette surjection par le dual de $f_*\mathcal{O}_X$, puis en composant avec l'évaluation, on obtient une surjection
```
Après :
```tex
En passant aux duaux, on obtient une surjection
```

### FR-SPACES-PERFECT-FIDELITY-039 — `lemma-affine-morphism-and-hom-out-of-perfect`

[Source officielle, ligne 4978](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L4978)

Rétablir l'indice X de la source dans l'égalité de changement de base ; S' était une correction du typage.

Témoin officiel :
```tex
Lf^*g_*\mathcal{O}_X
```
Avant :
```tex
Lf^*g_*\mathcal{O}_{S'}
```
Après :
```tex
Lf^*g_*\mathcal{O}_X
```

### FR-SPACES-PERFECT-FIDELITY-040 — `lemma-affine-morphism-and-hom-out-of-perfect`

[Source officielle, ligne 4988](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L4988)

La dernière réduction emploie A et A' dans la source, même si les anneaux introduits sont R et R'. Garder cette discordance à son emplacement.

Témoin officiel :
```tex
R\Gamma(X, K) \otimes^\mathbf{L}_A A' \longrightarrow
```
Avant :
```tex
R\Gamma(X, K) \otimes^\mathbf{L}_R R' \longrightarrow
```
Après :
```tex
R\Gamma(X, K) \otimes^\mathbf{L}_A A' \longrightarrow
```

### FR-SPACES-PERFECT-FIDELITY-041 — `lemma-tor-independence-and-tor-amplitude`

[Source officielle, ligne 5030](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L5030)

Retirer le prime et ses parenthèses ajoutés à f dans la conclusion (1), sans toucher au carré cartésien.

Témoin officiel :
```tex
$f^{-1}\mathcal{O}_{Y'}$-modules.
```
Avant :
```tex
$(f')^{-1}\mathcal{O}_{Y'}$-modules.
```
Après :
```tex
$f^{-1}\mathcal{O}_{Y'}$-modules.
```

### FR-SPACES-PERFECT-FIDELITY-042 — `lemma-single-complex-base-change-condition`

[Source officielle, ligne 5194](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L5194)

Restaurer g à cette occurrence de la preuve. Le g' de l'énoncé reste inchangé : la source distingue effectivement ces deux passages.

Témoin officiel :
```tex
Moreover, the map $Lg^*K \to K'$
```
Avant :
```tex
De plus, le morphisme $L(g')^*K \to K'$
```
Après :
```tex
De plus, le morphisme $Lg^*K \to K'$
```

### FR-SPACES-PERFECT-FIDELITY-043 — `lemma-single-complex-base-change-condition-inherited`

[Source officielle, ligne 5401](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L5401)

Le point interne de l'indice est une coquille source et non une ponctuation de phrase. La version diplomatique le conserve ; la virgule proposée reste documentée séparément.

Témoin officiel :
```tex
$\mathcal{O}_{X. x}$-modules
```
Avant :
```tex
$\mathcal{O}_{X, x}$-modules
```
Après :
```tex
$\mathcal{O}_{X. x}$-modules
```

### FR-SPACES-PERFECT-FIDELITY-044 — `lemma-base-change-RHom`

[Source officielle, ligne 5481](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L5481)

Le diagramme nomme h la flèche supérieure dans le témoin, contrairement aux g' de la suite. Rétablir le nom du diagramme uniquement.

Témoin officiel :
```tex
X' \ar[r]_h \ar[d]_{f'} &
```
Avant :
```tex
X' \ar[r]_{g'} \ar[d]_{f'} &
```
Après :
```tex
X' \ar[r]_h \ar[d]_{f'} &
```

### FR-SPACES-PERFECT-FIDELITY-045 — `lemma-tensor-perfect`

[Source officielle, ligne 5597](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L5597)

Le point indiquant le complexe avait été ajouté dans l'expression de cohomologie ; le témoin n'en porte pas à cette occurrence.

Témoin officiel :
```tex
$H^i(E \otimes^\mathbf{L}_{\mathcal{O}_X} \mathcal{G})$
```
Avant :
```tex
$H^i(E\otimes^\mathbf{L}_{\mathcal{O}_X}\mathcal{G}^\bullet)$
```
Après :
```tex
$H^i(E\otimes^\mathbf{L}_{\mathcal{O}_X}\mathcal{G})$
```

### FR-SPACES-PERFECT-FIDELITY-046 — `lemma-tensor-perfect`

[Source officielle, ligne 5599](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L5599)

Rétablir Y dans la dernière phrase, bien que le morphisme initial ait B pour but.

Témoin officiel :
```tex
$f^{-1}\mathcal{O}_Y$
```
Avant :
```tex
$f^{-1}\mathcal{O}_B$
```
Après :
```tex
$f^{-1}\mathcal{O}_Y$
```

### FR-SPACES-PERFECT-FIDELITY-047 — `lemma-ext-perfect`

[Source officielle, ligne 5609](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L5609)

Rétablir G sans point dans la définition de K de l'énoncé, sans altérer les complexes de la preuve.

Témoin officiel :
```tex
$K = Rf_*R\SheafHom(E, \mathcal{G})$
```
Avant :
```tex
$K=Rf_*R\SheafHom(E,\mathcal{G}^\bullet)$
```
Après :
```tex
$K=Rf_*R\SheafHom(E,\mathcal{G})$
```

### FR-SPACES-PERFECT-FIDELITY-048 — `lemma-compute-ext`

[Source officielle, ligne 5795](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L5795)

La première phrase de la source introduit F, tandis que l'hypothèse (4) utilise G. La traduction avait uniformisé les deux ; la distinction du témoin est restaurée.

Témoin officiel :
```tex
and $\mathcal{F}^\bullet$ a complex
```
Avant :
```tex
et soit $\mathcal{G}^\bullet$ un complexe de
```
Après :
```tex
et soit $\mathcal{F}^\bullet$ un complexe de
```

### FR-SPACES-PERFECT-FIDELITY-049 — `lemma-compute-ext`

[Source officielle, ligne 5878](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L5878)

Première occurrence de Y dans la preuve (B) : la base B substituée pour cohérence est retirée.

Témoin officiel :
```tex
perfect on $Y$, see Lemma
```
Avant :
```tex
d'objets parfaits sur $B$ ; voir le lemme
```
Après :
```tex
d'objets parfaits sur $Y$ ; voir le lemme
```

### FR-SPACES-PERFECT-FIDELITY-050 — `lemma-compute-ext`

[Source officielle, ligne 5881](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L5881)

Rétablir Y comme base des faisceaux de ce paragraphe (B) uniquement.

Témoin officiel :
```tex
for any quasi-coherent $\mathcal{F}$ on $Y$ we have
```
Avant :
```tex
$\mathcal{F}$ quasi-coh\'erent sur $B$, on dispose
```
Après :
```tex
$\mathcal{F}$ quasi-coh\'erent sur $Y$, on dispose
```

### FR-SPACES-PERFECT-FIDELITY-051 — `lemma-compute-ext`

[Source officielle, ligne 5888](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L5888)

Les deux sommets inférieurs du diagramme reprennent Y et O_Y. Aucun autre diagramme n'est modifié.

Témoin officiel :
```tex
H^i(Y, K_{n + 1} \otimes_{\mathcal{O}_Y}^\mathbf{L} \mathcal{F})
\ar[rr] & &
H^i(Y, K_n \otimes_{\mathcal{O}_Y}^\mathbf{L} \mathcal{F})
```
Avant :
```tex
H^i(B, K_{n + 1} \otimes_{\mathcal{O}_B}^\mathbf{L} \mathcal{F})
\ar[rr] & &
H^i(B, K_n \otimes_{\mathcal{O}_B}^\mathbf{L} \mathcal{F})
```
Après :
```tex
H^i(Y, K_{n + 1} \otimes_{\mathcal{O}_Y}^\mathbf{L} \mathcal{F})
\ar[rr] & &
H^i(Y, K_n \otimes_{\mathcal{O}_Y}^\mathbf{L} \mathcal{F})
```

### FR-SPACES-PERFECT-FIDELITY-052 — `lemma-compute-ext`

[Source officielle, ligne 5896](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L5896)

Rétablir ensemble la catégorie et la base des faisceaux dans cette phrase ; les B de l'énoncé restent inchangés.

Témoin officiel :
```tex
is a system of perfect objects in $D(\mathcal{O}_Y)$
such that for any quasi-coherent $\mathcal{F}$ on $Y$
```
Avant :
```tex
$D(\mathcal{O}_B)$ tel que, pour tout $\mathcal{F}$ quasi-coh\'erent sur $B$
```
Après :
```tex
$D(\mathcal{O}_Y)$ tel que, pour tout $\mathcal{F}$ quasi-coh\'erent sur $Y$
```

### FR-SPACES-PERFECT-FIDELITY-053 — `lemma-compute-ext`

[Source officielle, ligne 5900](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L5900)

Les deux Ext de cet affichage sont indexés par O_Y dans la source.

Témoin officiel :
```tex
\Ext^i_{\mathcal{O}_Y}(L_{n + 1}, \mathcal{F})
\longrightarrow
\Ext^i_{\mathcal{O}_Y}(L_n, \mathcal{F})
```
Avant :
```tex
\Ext^i_{\mathcal{O}_B}(L_{n + 1}, \mathcal{F})
\longrightarrow
\Ext^i_{\mathcal{O}_B}(L_n, \mathcal{F})
```
Après :
```tex
\Ext^i_{\mathcal{O}_Y}(L_{n + 1}, \mathcal{F})
\longrightarrow
\Ext^i_{\mathcal{O}_Y}(L_n, \mathcal{F})
```

### FR-SPACES-PERFECT-FIDELITY-054 — `lemma-compute-ext`

[Source officielle, ligne 5911](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L5911)

La dernière égalité de la preuve reprend elle aussi O_Y, sans correction silencieuse en O_B.

Témoin officiel :
```tex
$\Ext^i_{\mathcal{O}_Y}(L, \mathcal{F}) =
\Ext^i_{\mathcal{O}_Y}(L_n, \mathcal{F})$
```
Avant :
```tex
$\Ext^i_{\mathcal{O}_B}(L,\mathcal{F})=
\Ext^i_{\mathcal{O}_B}(L_n,\mathcal{F})$
```
Après :
```tex
$\Ext^i_{\mathcal{O}_Y}(L,\mathcal{F})=
\Ext^i_{\mathcal{O}_Y}(L_n,\mathcal{F})$
```

### FR-SPACES-PERFECT-FIDELITY-055 — `remark-base-change-of-L`

[Source officielle, ligne 5933](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L5933)

Le second Ext est indexé par O_X dans le témoin. Le prime ajouté pour corriger son espace est retiré à cette seule occurrence.

Témoin officiel :
```tex
\Ext^i_{\mathcal{O}_X}(L(g')^*E,
```
Avant :
```tex
\Ext^i_{\mathcal{O}_{X'}}(L(g')^*E,
```
Après :
```tex
\Ext^i_{\mathcal{O}_X}(L(g')^*E,
```

### FR-SPACES-PERFECT-FIDELITY-056 — `lemma-base-change-tensor-pseudo-coherent`

[Source officielle, ligne 6199](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L6199)

Rétablir G sans point dans l'image directe du cône, comme dans la phrase officielle.

Témoin officiel :
```tex
$Rf_*(C \otimes^\mathbf{L} \mathcal{G})$
```
Avant :
```tex
$Rf_*(C \otimes^\mathbf{L} \mathcal{G}^\bullet)$
```
Après :
```tex
$Rf_*(C \otimes^\mathbf{L} \mathcal{G})$
```

### FR-SPACES-PERFECT-FIDELITY-057 — `lemma-base-change-tensor-pseudo-coherent`

[Source officielle, ligne 6202](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L6202)

Les deux points ajoutés à G dans cet affichage sont retirés. Les points présents dans les autres affichages officiels restent inchangés.

Témoin officiel :
```tex
Rf_*(P \otimes^\mathbf{L} \mathcal{G}) \to
Rf_*(E \otimes^\mathbf{L} \mathcal{G})
```
Avant :
```tex
Rf_*(P \otimes^\mathbf{L} \mathcal{G}^\bullet) \to
Rf_*(E \otimes^\mathbf{L} \mathcal{G}^\bullet)
```
Après :
```tex
Rf_*(P \otimes^\mathbf{L} \mathcal{G}) \to
Rf_*(E \otimes^\mathbf{L} \mathcal{G})
```

### FR-SPACES-PERFECT-FIDELITY-058 — `lemma-flat-proper-perfect-direct-image-general`

[Source officielle, ligne 6233](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L6233)

L'hypothèse (2) porte sur la platitude sur S dans la source. Remplacer S par Y est une modification de l'énoncé, non une traduction.

Témoin officiel :
```tex
flat over $S$. Then $Rf_*\mathcal{G}$
```
Avant :
```tex
plat sur $Y$. Alors $Rf_*\mathcal{G}$
```
Après :
```tex
plat sur $S$. Alors $Rf_*\mathcal{G}$
```

### FR-SPACES-PERFECT-FIDELITY-059 — `lemma-base-change-RHom-perfect`

[Source officielle, ligne 6400](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/spaces-perfect.tex#L6400)

Retirer le point ajouté à cette occurrence de G dans l'approximation noethérienne ; conserver les complexes de toutes les autres occurrences.

Témoin officiel :
```tex
pullback to $X$ is $\mathcal{G}$.
```
Avant :
```tex
l'image inverse sur $X$ est $\mathcal{G}^\bullet$.
```
Après :
```tex
l'image inverse sur $X$ est $\mathcal{G}$.
```

## Limites

La comparaison est produite par IA, sans relecture humaine experte. Les identités des propositions dans les anciens registres restent à rapprocher ; leur attribution n'est pas inventée. Le reste des écarts de ce chapitre doit encore être examiné. Aucun fichier public ni témoin anglais n'a été modifié.
