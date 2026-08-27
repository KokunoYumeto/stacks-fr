# Le projet Stacks — traduction française indépendante

Ce dépôt est la lignée publique unique de la traduction française indépendante
du Stacks Project. Il contient des lecteurs PDF, les sources TeX modifiables,
les manifests de provenance et les preuves de contrôle déterministe.

État de la première publication : 15 chapitres sur 116, fondés sur la révision
amont figée `a04446e57ec1fbc252a871afcec7752fb2807b14`.

| Partie | Chapitres | Pages | PDF SHA-256 | Archive source/provenance SHA-256 |
|---|---:|---:|---|---|
| 1 | 1–10 | 986 | `A07024FC128BF92A7E613364919FAD38939C92431BDF01C24658862E7B8C03EC` | `46AC4B292DE526EB9712CD5525368446532F3015E812E312DB5F86DEE4CF3E81` |
| 2 | 11–15 | 748 | `020E23158E5657DEF3B4AE97008741C6C47CF12867F3B8B3C2E44DC4D106582A` | `13B75960E1B2A64F608FDC4888E645AF49D0EE6A7E37F412238F337D0998ACA9` |

Les fichiers publics sont distribués dans les releases GitHub et dans la
lignée Zenodo liée au présent dépôt. La publication courante est
[10.5281/zenodo.22134073](https://doi.org/10.5281/zenodo.22134073), dans la
lignée conceptuelle permanente
[10.5281/zenodo.22134072](https://doi.org/10.5281/zenodo.22134072). Les
manifests exacts de chaque partie sont conservés sous `parts/`.

## Autorité

- Projet amont : <https://github.com/stacks/stacks-project>
- Commit figé : `a04446e57ec1fbc252a871afcec7752fb2807b14`
- Archive source figée, SHA-256 :
  `4FC59A86F1CE43C7D608224D165CB99E7A13B92D4AE892A65DF9B4BF1C477B6F`
- PDF officiel amont de 7 654 pages, SHA-256 :
  `5B3A46C20A9CD3C42E7F6746A30B655367DD544AA0AC837626C01E0F44DEB409`

## Licence et indépendance

La source et la traduction sont distribuées selon la GNU Free Documentation
License 1.2, ou toute version ultérieure publiée par la Free Software
Foundation, sans sections invariantes, sans texte de première de couverture et
sans texte de quatrième de couverture. Voir `COPYING`.

Cette traduction n'est ni produite ni approuvée par le Stacks Project. Les
sources anglaises figées ne sont jamais modifiées dans la voie française. Les
corrections nécessaires à une traduction lisible sont déclarées séparément,
liées aux empreintes de l'autorité, et restent auditables dans les archives de
provenance.

## Contrôles

Chaque partie publiée passe une reproduction de l'assemblage, une compilation
TeX/BibTeX liée par `.fls`, la vérification des structures, formules, références,
citations, polices, glyphes, extraction et liens, puis le rendu et l'inspection
visuelle de chaque page. Les archives ZIP sont rouvertes et chaque membre est
rejoué par nom, taille et SHA-256 avant publication, puis les octets publics sont
relus anonymement après publication.
