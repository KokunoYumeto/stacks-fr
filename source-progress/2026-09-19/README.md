# French Stacks — editable source progress snapshot

This snapshot puts the current French chapter work online without pretending that
the French translation is finished. **It is not a complete French edition.**
All 116 chapter positions have an editable source file, but several are explicitly
still in progress and may contain untranslated English suffixes. The table below
distinguishes direct completion evidence from source-preservation snapshots.

The already released Chapters 1–15 remain the verified public reading edition.
Their exact PDFs, direct cumulative LaTeX files and source archives remain in the
[existing release](https://github.com/KokunoYumeto/stacks-fr/releases/tag/2026-08-27-parts-01-02).
This new snapshot preserves the available later work; it replaces no published PDF.

- [Full current chapter-source ZIP](French_Stacks_Current_Chapter_Sources_2026-09-19.zip)
- [Machine-readable coverage and hashes](COVERAGE.json)
- [Standalone source directory](src/)

Each chapter remains in its native standalone form. Compile an individual chapter
from `src/` with pdfLaTeX and BibTeX, using its basename, then repeat pdfLaTeX until
references stabilize. Standard LaTeX packages must be installed. `preamble.tex`,
`chapters.tex`, the class and bibliography are included. External chapter AUX files
must be generated before cross-chapter links resolve; this snapshot does not claim
that a new cumulative reader has been built or passed layout QA.

No translation text was changed in preparing this public source snapshot.
The pinned Stacks Project source is commit
`a04446e57ec1fbc252a871afcec7752fb2807b14`. This unofficial translation inherits
GFDL 1.2-or-later without invariant sections or cover texts and implies no endorsement.

## Chapter coverage

| Chapter | Editable LaTeX | Current evidence |
|---:|---|---|
| 1 | [introduction.tex](src/introduction.tex) | Previously published complete chapter |
| 2 | [conventions.tex](src/conventions.tex) | Previously published complete chapter |
| 3 | [sets.tex](src/sets.tex) | Previously published complete chapter |
| 4 | [categories.tex](src/categories.tex) | Previously published complete chapter |
| 5 | [topology.tex](src/topology.tex) | Previously published complete chapter |
| 6 | [sheaves.tex](src/sheaves.tex) | Previously published complete chapter |
| 7 | [sites.tex](src/sites.tex) | Previously published complete chapter |
| 8 | [stacks.tex](src/stacks.tex) | Previously published complete chapter |
| 9 | [fields.tex](src/fields.tex) | Previously published complete chapter |
| 10 | [algebra.tex](src/algebra.tex) | Previously published complete chapter |
| 11 | [brauer.tex](src/brauer.tex) | Previously published complete chapter |
| 12 | [homology.tex](src/homology.tex) | Previously published complete chapter |
| 13 | [derived.tex](src/derived.tex) | Previously published complete chapter |
| 14 | [simplicial.tex](src/simplicial.tex) | Previously published complete chapter |
| 15 | [more-algebra.tex](src/more-algebra.tex) | Previously published complete chapter |
| 16 | [smoothing.tex](src/smoothing.tex) | Current source snapshot; see chapter production evidence for completion |
| 17 | [modules.tex](src/modules.tex) | Current source snapshot; see chapter production evidence for completion |
| 18 | [sites-modules.tex](src/sites-modules.tex) | Current source snapshot; see chapter production evidence for completion |
| 19 | [injectives.tex](src/injectives.tex) | Current source snapshot; see chapter production evidence for completion |
| 20 | [cohomology.tex](src/cohomology.tex) | Current source snapshot; see chapter production evidence for completion |
| 21 | [sites-cohomology.tex](src/sites-cohomology.tex) | Current source snapshot; see chapter production evidence for completion |
| 22 | [dga.tex](src/dga.tex) | Current source snapshot; see chapter production evidence for completion |
| 23 | [dpa.tex](src/dpa.tex) | Current source snapshot; see chapter production evidence for completion |
| 24 | [sdga.tex](src/sdga.tex) | Current source snapshot; see chapter production evidence for completion |
| 25 | [hypercovering.tex](src/hypercovering.tex) | Current source snapshot; see chapter production evidence for completion |
| 26 | [schemes.tex](src/schemes.tex) | Current source snapshot; see chapter production evidence for completion |
| 27 | [constructions.tex](src/constructions.tex) | Current source snapshot; see chapter production evidence for completion |
| 28 | [properties.tex](src/properties.tex) | Current source snapshot; see chapter production evidence for completion |
| 29 | [morphisms.tex](src/morphisms.tex) | Current source snapshot; see chapter production evidence for completion |
| 30 | [coherent.tex](src/coherent.tex) | Current source snapshot; see chapter production evidence for completion |
| 31 | [divisors.tex](src/divisors.tex) | Current source snapshot; see chapter production evidence for completion |
| 32 | [limits.tex](src/limits.tex) | Current source snapshot; see chapter production evidence for completion |
| 33 | [varieties.tex](src/varieties.tex) | Current source snapshot; see chapter production evidence for completion |
| 34 | [topologies.tex](src/topologies.tex) | Current source snapshot; see chapter production evidence for completion |
| 35 | [descent.tex](src/descent.tex) | Current source snapshot; see chapter production evidence for completion |
| 36 | [perfect.tex](src/perfect.tex) | Current source snapshot; see chapter production evidence for completion |
| 37 | [more-morphisms.tex](src/more-morphisms.tex) | Current source snapshot; see chapter production evidence for completion |
| 38 | [flat.tex](src/flat.tex) | Current source snapshot; see chapter production evidence for completion |
| 39 | [groupoids.tex](src/groupoids.tex) | Current source snapshot; see chapter production evidence for completion |
| 40 | [more-groupoids.tex](src/more-groupoids.tex) | Current source snapshot; see chapter production evidence for completion |
| 41 | [etale.tex](src/etale.tex) | Current source snapshot; see chapter production evidence for completion |
| 42 | [chow.tex](src/chow.tex) | Current source snapshot; see chapter production evidence for completion |
| 43 | [intersection.tex](src/intersection.tex) | Current source snapshot; see chapter production evidence for completion |
| 44 | [pic.tex](src/pic.tex) | Current source snapshot; see chapter production evidence for completion |
| 45 | [weil.tex](src/weil.tex) | Current source snapshot; see chapter production evidence for completion |
| 46 | [adequate.tex](src/adequate.tex) | Current source snapshot; see chapter production evidence for completion |
| 47 | [dualizing.tex](src/dualizing.tex) | Current source snapshot; see chapter production evidence for completion |
| 48 | [duality.tex](src/duality.tex) | Current source snapshot; see chapter production evidence for completion |
| 49 | [discriminant.tex](src/discriminant.tex) | Complete; final source/PDF receipt bound |
| 50 | [derham.tex](src/derham.tex) | Current source snapshot; see chapter production evidence for completion |
| 51 | [local-cohomology.tex](src/local-cohomology.tex) | Current source snapshot; see chapter production evidence for completion |
| 52 | [algebraization.tex](src/algebraization.tex) | Current source snapshot; see chapter production evidence for completion |
| 53 | [curves.tex](src/curves.tex) | Current source snapshot; see chapter production evidence for completion |
| 54 | [resolve.tex](src/resolve.tex) | Current source snapshot; see chapter production evidence for completion |
| 55 | [models.tex](src/models.tex) | Current source snapshot; see chapter production evidence for completion |
| 56 | [functors.tex](src/functors.tex) | Current source snapshot; see chapter production evidence for completion |
| 57 | [equiv.tex](src/equiv.tex) | Current source snapshot; see chapter production evidence for completion |
| 58 | [pione.tex](src/pione.tex) | Current source snapshot; see chapter production evidence for completion |
| 59 | [etale-cohomology.tex](src/etale-cohomology.tex) | Current source snapshot; see chapter production evidence for completion |
| 60 | [crystalline.tex](src/crystalline.tex) | Current source snapshot; see chapter production evidence for completion |
| 61 | [proetale.tex](src/proetale.tex) | Current source snapshot; see chapter production evidence for completion |
| 62 | [relative-cycles.tex](src/relative-cycles.tex) | Current source snapshot; see chapter production evidence for completion |
| 63 | [more-etale.tex](src/more-etale.tex) | Current source snapshot; see chapter production evidence for completion |
| 64 | [trace.tex](src/trace.tex) | Current source snapshot; see chapter production evidence for completion |
| 65 | [spaces.tex](src/spaces.tex) | Current source snapshot; see chapter production evidence for completion |
| 66 | [spaces-properties.tex](src/spaces-properties.tex) | Current source snapshot; see chapter production evidence for completion |
| 67 | [spaces-morphisms.tex](src/spaces-morphisms.tex) | Current source snapshot; see chapter production evidence for completion |
| 68 | [decent-spaces.tex](src/decent-spaces.tex) | Current source snapshot; see chapter production evidence for completion |
| 69 | [spaces-cohomology.tex](src/spaces-cohomology.tex) | Current source snapshot; see chapter production evidence for completion |
| 70 | [spaces-limits.tex](src/spaces-limits.tex) | Current source snapshot; see chapter production evidence for completion |
| 71 | [spaces-divisors.tex](src/spaces-divisors.tex) | Current source snapshot; see chapter production evidence for completion |
| 72 | [spaces-over-fields.tex](src/spaces-over-fields.tex) | Current source snapshot; see chapter production evidence for completion |
| 73 | [spaces-topologies.tex](src/spaces-topologies.tex) | Current source snapshot; see chapter production evidence for completion |
| 74 | [spaces-descent.tex](src/spaces-descent.tex) | Current source snapshot; see chapter production evidence for completion |
| 75 | [spaces-perfect.tex](src/spaces-perfect.tex) | Current source snapshot; see chapter production evidence for completion |
| 76 | [spaces-more-morphisms.tex](src/spaces-more-morphisms.tex) | Current source snapshot; see chapter production evidence for completion |
| 77 | [spaces-flat.tex](src/spaces-flat.tex) | Complete; live target hash matches terminal cursor |
| 78 | [spaces-groupoids.tex](src/spaces-groupoids.tex) | Complete; live target hash matches terminal cursor |
| 79 | [spaces-more-groupoids.tex](src/spaces-more-groupoids.tex) | Current source snapshot; see chapter production evidence for completion |
| 80 | [bootstrap.tex](src/bootstrap.tex) | Complete; live target hash matches terminal cursor |
| 81 | [spaces-pushouts.tex](src/spaces-pushouts.tex) | Current source snapshot; see chapter production evidence for completion |
| 82 | [spaces-chow.tex](src/spaces-chow.tex) | Current source snapshot; see chapter production evidence for completion |
| 83 | [groupoids-quotients.tex](src/groupoids-quotients.tex) | Current source snapshot; see chapter production evidence for completion |
| 84 | [spaces-more-cohomology.tex](src/spaces-more-cohomology.tex) | Current source snapshot; see chapter production evidence for completion |
| 85 | [spaces-simplicial.tex](src/spaces-simplicial.tex) | Current source snapshot; see chapter production evidence for completion |
| 86 | [spaces-duality.tex](src/spaces-duality.tex) | Current source snapshot; see chapter production evidence for completion |
| 87 | [formal-spaces.tex](src/formal-spaces.tex) | Complete; live target hash matches terminal cursor |
| 88 | [restricted.tex](src/restricted.tex) | Complete; live target hash matches terminal cursor |
| 89 | [spaces-resolve.tex](src/spaces-resolve.tex) | Current source snapshot; see chapter production evidence for completion |
| 90 | [formal-defos.tex](src/formal-defos.tex) | In progress; may include untranslated source text |
| 91 | [defos.tex](src/defos.tex) | Complete; live target hash matches terminal cursor |
| 92 | [cotangent.tex](src/cotangent.tex) | Complete; live target hash matches terminal cursor |
| 93 | [examples-defos.tex](src/examples-defos.tex) | Current source snapshot; see chapter production evidence for completion |
| 94 | [algebraic.tex](src/algebraic.tex) | Complete; live target hash matches terminal cursor |
| 95 | [examples-stacks.tex](src/examples-stacks.tex) | Complete; live target hash matches terminal cursor |
| 96 | [stacks-sheaves.tex](src/stacks-sheaves.tex) | Current source snapshot; see chapter production evidence for completion |
| 97 | [criteria.tex](src/criteria.tex) | Current source snapshot; see chapter production evidence for completion |
| 98 | [artin.tex](src/artin.tex) | In progress; may include untranslated source text |
| 99 | [quot.tex](src/quot.tex) | Current source snapshot; see chapter production evidence for completion |
| 100 | [stacks-properties.tex](src/stacks-properties.tex) | Complete; live target hash matches terminal cursor |
| 101 | [stacks-morphisms.tex](src/stacks-morphisms.tex) | Current source snapshot; see chapter production evidence for completion |
| 102 | [stacks-limits.tex](src/stacks-limits.tex) | Current source snapshot; see chapter production evidence for completion |
| 103 | [stacks-cohomology.tex](src/stacks-cohomology.tex) | Current source snapshot; see chapter production evidence for completion |
| 104 | [stacks-perfect.tex](src/stacks-perfect.tex) | Complete; live target hash matches terminal cursor |
| 105 | [stacks-introduction.tex](src/stacks-introduction.tex) | Complete; live target hash matches terminal cursor |
| 106 | [stacks-more-morphisms.tex](src/stacks-more-morphisms.tex) | In progress; may include untranslated source text |
| 107 | [stacks-geometry.tex](src/stacks-geometry.tex) | Complete; live target hash matches terminal cursor |
| 108 | [moduli.tex](src/moduli.tex) | Current source snapshot; see chapter production evidence for completion |
| 109 | [moduli-curves.tex](src/moduli-curves.tex) | Complete; live target hash matches terminal cursor |
| 110 | [examples.tex](src/examples.tex) | In progress; may include untranslated source text |
| 111 | [exercises.tex](src/exercises.tex) | In progress; may include untranslated source text |
| 112 | [guide.tex](src/guide.tex) | Current source snapshot; see chapter production evidence for completion |
| 113 | [desirables.tex](src/desirables.tex) | Current source snapshot; see chapter production evidence for completion |
| 114 | [coding.tex](src/coding.tex) | Current source snapshot; see chapter production evidence for completion |
| 115 | [obsolete.tex](src/obsolete.tex) | Complete; live target hash matches terminal cursor |
| 116 | [fdl.tex](src/fdl.tex) | Current source snapshot; see chapter production evidence for completion |
