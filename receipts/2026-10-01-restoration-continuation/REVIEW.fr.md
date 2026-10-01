# Vérification ponctuelle de la restauration française

Le contrôle du 1er octobre 2026 confirme sept lectures ciblées dans trois chapitres de l'édition française restaurée. Aucune nouvelle intervention dans le texte n'est nécessaire à ces endroits. Les trois fichiers téléchargés publiquement, les fichiers locaux sélectionnés et leurs objets Git publiés sont identiques octet par octet.

Il s'agit d'un contrôle de fidélité à la source, non d'une nouvelle révision mathématique. Le résultat ne certifie ni toute la prose des 116 chapitres ni chaque choix de traduction. Aucun avis d'expert humain n'est revendiqué. Contrôle réalisé par OpenAI Codex — GPT-6.1 Sol, effort Ultra. La traduction initiale et ses interventions antérieures restent décrites dans les notices de l'édition.

## Corrections éditoriales déjà retirées

1. **Isomorphisme ou quasi-isomorphisme.** La [conclusion officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L5459) dit « is an isomorphism ». La [conclusion française publiée](https://github.com/KokunoYumeto/stacks-fr/blob/0fca0328aaf6a995831bb95be7ee243563bc6658/editions/2026-09-30-faithful116/chapters/013_derived.fr.tex#L5233) dit donc « est un isomorphisme ». La proposition de remplacer ce mot par « quasi-isomorphisme » demeure séparée. Réintroduire cette correction dans le texte de base reviendrait à corriger la source, et non à la traduire.

2. **Pleine fidélité ou plénitude.** La [source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L6197) mentionne la pleine fidélité après avoir prouvé la fidélité. Le [français publié](https://github.com/KokunoYumeto/stacks-fr/blob/0fca0328aaf6a995831bb95be7ee243563bc6658/editions/2026-09-30-faithful116/chapters/013_derived.fr.tex#L5957) conserve « La pleine fidélité se démontre exactement de la même manière ». Remplacer cette propriété par la seule plénitude serait une intervention mathématique, même si cette correction paraît naturelle dans le contexte.

## Commentaires qui appartiennent déjà à Stacks

Ces passages ont été examinés parce qu'ils peuvent ressembler à des notes ajoutées lors de la traduction. Ils proviennent pourtant de la source officielle et doivent être conservés.

3. **Note sur les résolutions.** La note expliquant que la classe contient zéro figure déjà dans la [source anglaise](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/derived.tex#L5429). La [note française](https://github.com/KokunoYumeto/stacks-fr/blob/0fca0328aaf6a995831bb95be7ee243563bc6658/editions/2026-09-30-faithful116/chapters/013_derived.fr.tex#L5200) n'est pas un complément de démonstration ajouté par le traducteur.

4. **Correction d'une construction par recollement.** L'expression « Corrigeons cela » traduit [« correct this by glueing in an affine line instead »](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L262). Le [passage français](https://github.com/KokunoYumeto/stacks-fr/blob/0fca0328aaf6a995831bb95be7ee243563bc6658/editions/2026-09-30-faithful116/chapters/110_examples.fr.tex#L262) reprend donc la démarche de l'auteur, pas une correction éditoriale de cette édition.

5. **Erreur dans un argument de descente de la projectivité.** La remarque sur Gruson et Raynaud se trouve dans [l'anglais officiel](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/algebra.tex#L19566). Sa [traduction française](https://github.com/KokunoYumeto/stacks-fr/blob/0fca0328aaf6a995831bb95be7ee243563bc6658/editions/2026-09-30-faithful116/chapters/010_algebra.fr.tex#L19332) doit rester.

6. **Contre-exemple à un énoncé d'EGA.** Le contre-exemple et le commentaire relatif aux errata sont dans [Stacks](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L3105). Le [français](https://github.com/KokunoYumeto/stacks-fr/blob/0fca0328aaf6a995831bb95be7ee243563bc6658/editions/2026-09-30-faithful116/chapters/110_examples.fr.tex#L3105) ne les ajoute pas de sa propre initiative.

7. **Remarque sur l'erratum d'Aoki.** Le commentaire est présent dans la [source officielle](https://github.com/stacks/stacks-project/blob/a04446e57ec1fbc252a871afcec7752fb2807b14/examples.tex#L6152) et dans sa [traduction](https://github.com/KokunoYumeto/stacks-fr/blob/0fca0328aaf6a995831bb95be7ee243563bc6658/editions/2026-09-30-faithful116/chapters/110_examples.fr.tex#L6157). Le retirer supprimerait du contenu de Stacks.

## Reproduction et portée

Le [résultat détaillé](VALIDATION.json) donne les citations comparées, leurs lignes, les empreintes SHA-256 et les liens publics. Le [vérificateur](verify.py) vérifie ces occurrences dans les trois fichiers, leur identité avec la sélection restaurée et leurs téléchargements anonymes. Il ne modifie pas les sources.

Aucune compilation, nouvelle édition, nouvelle version Zenodo ni modification du lecteur n'a été nécessaire. L'[édition restaurée](https://zenodo.org/records/23069850) et le [lecteur français](https://kokunoyumeto.github.io/stacks-zh-hans-cn/fr/index.html) restent les points d'accès actuels. Les témoins de l'ancienne édition éditoriale demeurent distincts et conservés.

