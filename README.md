# Lotzi-Resume

Lotzi Bölöni's CV and the material it is built from. This repository is the single
source of truth for the CV and for the bibliography that the webpage
(`Lotzi-Webpage/update-all.sh`) turns into the publication pages. The import from
Google Drive is described in [design/PLAN.md](design/PLAN.md).

## Setup

- TeX Live with `xelatex`, `biber` and `latexmk` (the CV uses `fontspec` and `fontawesome5`).
- Git LFS for the PDFs and other binary files: run `git lfs install` once before cloning.
- Python 3 (standard library only) for the scripts in `tools/`.

## Build

From the repository root:

```sh
latexmk -outdir=output variants/full-cv/CV-LotziBoloni.tex variants/full-cv/CV-LotziBoloni_WithFunding.tex
```

| PDF in `output/` | Content |
|---|---|
| `CV-LotziBoloni.pdf` | the default full CV, **without** funding |
| `CV-LotziBoloni_WithFunding.pdf` | the same CV with the Research Grants section after Publications |

`latexmk -C -outdir=output variants/full-cv/*.tex` removes the build products. `output/` is not in git.

## Layout

| Path | Content |
|---|---|
| `source/bib/Boloni.bib` | master bibliography; also read by the webpage (keep the `bib2html_*` fields) |
| `source/bib/Boloni-Additional.bib` | theses and other entries the CV does not use |
| `source/publists/` | the hand-selected `\nocite` lists: books, chapters, journals, conferences |
| `source/sections/` | one file per CV section; `students.tex` and `service.tex` include their parts |
| `source/data/metrics.tex` | Google Scholar citations, h-index, i10-index |
| `source/papers/` | paper PDFs, named `<bibkey>.pdf` (Git LFS) |
| `source/bios/` | bios (the 2019 NSF biosketches, as Markdown) |
| `style/lotzicv.sty` | the layout, and the `\ifwithfunding` switch and `\toconfirm` mark |
| `variants/full-cv/` | `body.tex` (section order) and one main file per PDF |
| `archive/` | older CVs, resumes and bios, frozen; never edited |
| `tools/` | checking scripts |
| `design/` | plans and review reports |

## Common updates

- **A new paper.** Add the entry to `source/bib/Boloni.bib` with a key `FirstAuthor-Year-Venue`, then add `\nocite{key}` under its year in the right file in `source/publists/`. Put the PDF in `source/papers/<key>.pdf`.
- **A grant.** Add an `\item` at the top of `source/sections/grants.tex` (newest first): role, title, agency and award number, period, total and my share. Update the total line. It appears only in the `_WithFunding` PDF.
- **A talk, student, committee or service item.** Edit the matching file in `source/sections/` (`talks`, `students-*`, `committees-*`, `service-*`).
- **Metrics.** Update the three numbers and the date together in `source/data/metrics.tex`.
- **A section that is not printed.** `service-agencies.tex` (Service with Funding Agencies) exists but is not included, as in the Drive CV; add `\input{source/sections/service-agencies}` to `service.tex` to show it.

## Checks

```sh
python3 tools/bibcheck.py      # duplicate/missing \nocite keys, uncited entries, inventory and damla.bib comparison
python3 tools/check_papers.py  # which bib entries have a PDF in source/papers/
```

Both print Markdown reports and change nothing. After a change to `style/` or `body.tex`,
compare the new PDF with the previous one (`pdftotext`, then `diff`).
