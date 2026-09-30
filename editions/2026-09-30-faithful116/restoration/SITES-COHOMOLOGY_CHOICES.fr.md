# Cohomologie sur les sites — texte de lecture dans les formules

## Portée

Consultation du 27 septembre 2026, pendant le rétablissement de la fidélité
au témoin officiel. Elle n'est pas présentée comme une consultation lors de
la traduction initiale. Les identités mathématiques restent gouvernées par
`sites-cohomology.tex`, commit `a04446e57ec1fbc252a871afcec7752fb2807b14`,
SHA-256 `5B335CE2C7208A128B3C744B8828D93508063F41A4FABBCE2E921F890928895C`.

La lecture des formules a révélé des fragments anglais non traduits. Leur
traduction est distincte du retrait des corrections mathématiques ajoutées.
Les passages avant/après, les numéros de ligne officiels et les identifiants
des réparations figurent dans [le journal](SITES-COHOMOLOGY_RESTORATIONS.json)
et [le dossier de lecture](SITES-COHOMOLOGY_REVIEW.fr.md).

## Usages effectivement consultés

- Laurent Moret-Bailly, *Pinceaux de variétés abéliennes*, Astérisque 129
  (1985), chapitre II, §0, p. 39, introduction :
  [notice stable NUMDAM](https://www.numdam.org/item/AST_1985__129__1_0/),
  [texte](https://www.numdam.org/item/AST_1985__129__1_0.pdf).
  Le passage rapproche explicitement les termes « faisceau inversible » et
  « torseur », au moyen du faisceau des isomorphismes depuis le faisceau
  structural. Il atteste ces termes dans un contexte directement pertinent.
  Il ne constitue pas à lui seul une preuve du lemme sur un site annelé général.
  Passage consulté dans l'extrait textuel de la source ; la notice bibliographique
  a été ouverte séparément. Aucune inspection visuelle du volume n'est revendiquée.
- André Galligo, Michel Granger et Philippe Maisonobe, *D-modules et faisceaux
  pervers dont le support singulier est un croisement normal*, Annales de
  l'Institut Fourier 35 (1985), no 1, p. 1–48,
  [DOI et résumé français](https://numdam.org/articles/10.5802/aif.996/).
  Le résumé français consulté emploie « à isomorphisme près » dans une
  classification d'objets. Cet usage justifie la locution ; il ne justifie
  aucune modification des objets ou du théorème de classification du Stacks Project.

## Choix appliqués et limites

Dans `lemma-h1-invertible`, les fragments restés anglais deviennent
« soit un isomorphisme », « ensemble des faisceaux inversibles sur »,
« ensemble des O*-torseurs » et « à isomorphisme près » (deux occurrences).
Le témoin nomme bien les mêmes objets et le même quotient par isomorphisme.
Le qualificatif *quasi-* n'est ni ajouté ni retiré ici. La notation O* n'est
pas remplacée par Gm : l'attestation terminologique ne permet pas de changer
la notation du témoin. « Fibrés en droites » n'est pas retenu, afin de conserver
la présentation en faisceaux sur un site annelé.

Dans `lemma-injective-trivial-cech` et `lemma-injective-module-trivial-cech`,
les quatre occurrences de *if* deviennent « si ». C'est une traduction
grammaticale ordinaire, non une terminologie nouvelle nécessitant une
attestation savante particulière. Les conditions et les valeurs restent exactes.

Confiance éditoriale élevée pour ces réparations ponctuelles, fondée sur
les témoins exacts et les usages ci-dessus ; ce n'est pas une probabilité
calibrée ni une certification de toute la prose du chapitre. Aucun relecteur
humain n'est revendiqué. Analyse et corrections : OpenAI Codex — GPT-6 Astra,
effort Ultra.
