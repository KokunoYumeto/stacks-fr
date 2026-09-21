# Rebuilding the complete French reader

The directly downloadable cumulative source
`stacks_fr_complete_116.tex` contains the complete translated text and generated
index. It requires the adjacent files `stacks-project-book.cls` and `my.bib`.

With a TeX distribution providing `latexmk`, pdfLaTeX, BibTeX, AMS packages,
French Babel support, `xy`, `multicol`, `hyperref`, and Latin Modern, run:

```text
latexmk -norc -pdf -bibtex -interaction=nonstopmode -halt-on-error -file-line-error -recorder stacks_fr_complete_116.tex
```

The verified release build produced 8,374 pages. Its exact PDF, TeX, log, FLS,
and build-receipt hashes are recorded in the release checksum file and the
provenance archive.

The `chapters/` directory preserves all 116 independently editable French
chapter sources selected by `FINAL_CUMULATIVE_SOURCE_MANIFEST.csv`. The
`parts/` directory preserves the twelve chapter-complete part readers and their
selection manifests. The deterministic assembler and its hash-bound input
contract are included under `tools/` and `manifests/` for source-level replay.

The source basis is upstream Stacks Project commit
`a04446e57ec1fbc252a871afcec7752fb2807b14`. This is an independent translation,
not an official Stacks Project publication or endorsement. See `COPYING` and
`CONTRIBUTORS` for license and attribution.

