# Plan: importing and organizing Lotzi Bölöni's resume material

## Goal

Bring Lotzi's CV material from Google Drive (`My Drive/Academic/Resume/Lotzi`) into this repository, with the layout of `Damla-Resume`. After the import, this repository is the single source of truth: the CV is built from it, and the webpage's publication pages read the bibliography from it. The current work is the generic full CV, in two builds: without funding (the default) and with funding. Other versions are listed briefly under [Versions](#versions).

Decisions (Lotzi, 2026-10-15):
- The CV gets a **Research Grants** section, but only in a second build. The default CV, `CV-LotziBoloni.pdf`, has no funding; `CV-LotziBoloni_WithFunding.pdf` has the Research Grants section.
- The repository is private, so the contact details, including the phone number, stay in.
- The Google Drive folder is **not touched**: nothing is moved, renamed, deleted or added there. Lotzi archives it separately. The import only reads from it.

## Starting point

The Drive folder (checked 2026-10-15) has five parts.

- **`CV/`** is the current CV (May 2024 design, last built 2026-05-27, 30 pages). It is already split into one file per section:
  - `cvp*.tex` for the profile, awards, talks and teaching;
  - `pub*.tex` for the publication lists;
  - `srv*.tex` for service;
  - `stu*.tex` for students.
  
  `CV-LotziBoloni.tex` holds the preamble (from Jitin Nair's MIT-licensed template) and the header. It builds with `latexmk -xelatex` and biber, because it uses `fontspec` and `fontawesome5`.
- **Publications** are selected by hand, not taken from the whole bib. Each `pub*.tex` is a list of `\nocite{key}` lines grouped by year, printed with `\printbibliography` in a `refsection`, IEEE style.
  - The lists cite 2 books, 15 chapters, 53 journal papers and 160 conference papers.
  - `pubJournals.tex` cites `Khan-2003-ISJC` twice, and `pubConferences.tex` also has one duplicated key.
  - Every cited key is in `Boloni.bib`.
- **`Bibliography/`**:
  - `Boloni.bib` has 238 entries: 165 inproceedings, 55 article, 15 incollection, 2 book, 1 inbook. 8 entries are not cited by the CV. No entry has a `keywords` field. Entries carry `bib2html_*` fields (PDF and video links, research category) used by the webpage.
  - `Boloni-Additional.bib` has 40 entries (theses, misc, some papers); one key is also in `Boloni.bib`. The CV does not use it.
- **Metrics** (8626 citations, h-index 41, i10-index 105) are typed into `cvpPublications.tex`, with no date.
- **`2PageResume/`** is a short resume in the old `resume.cls`, last changed in 2019. It has a `Funding.tex`; the current CV has **no grants section**.
- **`_obsolete/`**:
  - `CV-old/`: the old Resume sources, including `Funding.tex` and `FundingAllAttempts.tex`, and an old CV PDF;
  - `NSF_Resume/`: two bios (`.docx`);
  - the Perl/XSLT `Bib2Html` web generator, with its generated `Html/`;
  - old `Generate*List.tex` files.
- **`Papers/`** holds 69 PDFs (2000–2016), 31 MB, named `FirstAuthor-Year-Venue.pdf` like the bib keys. 137 bib entries have a `bib2html_dl_pdf` link to `www.cs.ucf.edu/~lboloni/Publications/Download/<key>.pdf`.

**Dependency:** `Lotzi-Webpage/update-all.sh` runs `bibweb.py --input ../../Resume/Lotzi/Bibliography/Boloni.bib`. The publication pages therefore depend on where `Boloni.bib` lives.

## Layout

```
Lotzi-Resume/
├── README.md              how to build each variant; how to add a paper, talk, student
├── .gitattributes         Git LFS for *.pdf, *.doc(x), *.xlsx, *.jp(e)g, *.png (set up 2026-10-15)
├── .gitignore             output/ and LaTeX build products
├── .latexmkrc             xelatex + biber, TEXINPUTS=./style//, run from the repo root
├── source/                ← single source of truth
│   ├── bib/
│   │   ├── Boloni.bib             master bibliography (keeps the bib2html_* fields)
│   │   └── Boloni-Additional.bib
│   ├── sections/          the current cvp/srv/stu files, renamed by content
│   │   ├── contact  education  interests  experience  societies  awards
│   │   ├── publications  grants (new)  talks  teaching
│   │   ├── students-current  students-phd-alumni  students-ms-alumni
│   │   ├── committees-phd  committees-ms  students-undergraduate
│   │   └── service-*  (editor, reviewer, conferences, panels, department, university, advisory, agencies)
│   ├── publists/          the hand-selected \nocite lists: books, chapters, journals, conferences
│   ├── papers/            the paper PDFs, <bibkey>.pdf (Git LFS)
│   ├── data/metrics.tex   citations, h-index, i10-index and their "as of" date
│   └── bios/              bios (from NSF_Resume, converted to .tex or .md)
├── style/lotzicv.sty      the preamble of CV-LotziBoloni.tex: same look as now
├── variants/
│   └── full-cv/
│       ├── body.tex                       the section list, shared by both builds
│       ├── CV-LotziBoloni.tex             default: \withfundingfalse, then \input{body}
│       └── CV-LotziBoloni_WithFunding.tex \withfundingtrue, then \input{body}
├── archive/               frozen, never edited
│   ├── cv/                the CV-LotziBoloni.pdf of 2026-05-27, and the old CV PDF
│   ├── 2page-resume-2019/ the 2PageResume sources
│   ├── resume-old/        _obsolete/CV-old/Resume (incl. Funding.tex, FundingAllAttempts.tex)
│   └── bios/              the .docx bios
├── tools/                 checking scripts (steps 5 and 6)
├── design/                plans
└── output/                CV-LotziBoloni.pdf, CV-LotziBoloni_WithFunding.pdf (gitignored)
```

Differences from Damla-Resume:
- The style keeps Lotzi's current look (xelatex, the Nair template) and does not take over `damlacv.sty`.
- Publications stay **hand-selected** by `\nocite` lists, as now. This keeps what Lotzi chose to show. Keywords in the bib are added only where a variant needs them (see Versions).

## Large files (Git LFS)

The paper PDFs and the other binary files are stored with **Git LFS** (Large File Storage, GitHub's system for large files). Git keeps a small pointer file in the history, and GitHub stores the file content separately.
- Set up on 2026-10-15: `git lfs install --local`, and `.gitattributes` tracks `*.pdf`, `*.docx`, `*.doc`, `*.xlsx`, `*.jpg`, `*.jpeg` and `*.png`. `.gitattributes` must be committed **before** the first binary file, or that file goes into normal git history.
- Size: about 31 MB of papers plus a few MB of archive PDFs and bios. This is far below GitHub's free LFS quota for storage and bandwidth.
- On another computer, run `git lfs install` once before cloning.
- Check after each import commit: `git lfs ls-files` lists every PDF, and `git lfs status` shows no binary file committed outside LFS.

## Status

Steps 1-9 were done on 2026-10-15.
- **Build.** Both PDFs build with no LaTeX warnings: the default has 30 pages, `_WithFunding` has 31.
- **Content check.** The May 27 PDF turned out to be out of date: the bib and the conference list were changed after it was built. The check therefore used a fresh build of the current Drive sources. All 30 pages of the default build are **pixel-identical** to it (`pdftoppm` + `compare`), and the publication counts are 2 / 15 / 53 / 160.
  - The header needed a `%` after `\input{contact}`: a stray space after the full-width table had added an empty line on page 1.
  - The Drive files had CRLF line endings. `source/` was converted to LF; `archive/` is unchanged.
- **Unprinted section.** `service-agencies.tex` was also not printed in the Drive CV. It is imported but not included.
- **Bibliography.** The two duplicated `\nocite` keys were removed. The review is in [REVIEW-BIBLIOGRAPHY.md](REVIEW-BIBLIOGRAPHY.md).
- **Paper PDFs.** 67 PDFs were imported, not 69: two Drive files were byte-identical copies under an old name. Two files were renamed to their bib keys.
- **Grants.** The sources are `Funding.tex` (to 2016), the NSF award database, and the acknowledgments in the 2017-2026 papers. New items are marked `\toconfirm` (red) in the `_WithFunding` PDF.
- **Webpage.** `update-all.sh` reads the bib through `$LOTZI_RESUME`, because this checkout is at `~/Lotzi-Resume`, not next to Lotzi-Webpage. `bibweb.py` generates the same 239 files from the new location.
- **Google Drive** was only read.

## Steps

1. **Repository set-up.** Commit `.gitattributes` and `.gitignore` as the first commit after the initial README.
2. **Archive import.** Copy the archive material in unchanged (`archive/` above) and commit it on its own.
3. **Source import.**
   - Copy the two `.bib` files and the `CV/` sections into `source/`, renaming them by content.
   - Move the preamble into `style/lotzicv.sty` and the metrics into `source/data/metrics.tex`, adding an "as of" date.
   - Write `variants/full-cv/body.tex` with the same section order as now, and the two main files. `lotzicv.sty` defines the switch `\newif\ifwithfunding`; `body.tex` has `\ifwithfunding\input{source/sections/grants}\fi` after Publications.
   - Build both with `latexmk -outdir=output variants/full-cv/CV-LotziBoloni.tex variants/full-cv/CV-LotziBoloni_WithFunding.tex` from the repository root. The PDF names follow the main file names.
   - Drop `CV-LotziBoloni 2.bbl` (empty Drive duplicate) and the build products.
4. **Full CV check.**
   - The default build (without funding) must build with no errors and match the 2026-05-27 PDF in content: same sections, same items, and the same publication counts (2 / 15 / 53 / 160).
   - Compare the text of the two PDFs (`pdftotext`, then `diff`); only the "Last updated" date may differ.
5. **Bibliography clean-up.**
   - Remove the duplicated `\nocite` keys.
   - List the 8 uncited bib entries, and the 2025–2026 papers in `Lotzi-Literature-Review/OurPapers/INVENTORY.tsv` that are not in `Boloni.bib`, for Lotzi to decide.
   - Check the bib against Damla's `damla.bib` for the joint papers (author lists, DOIs).
   - Put the checks in `tools/`.
6. **Paper PDFs.**
   - Copy the 69 PDFs from `Papers/` into `source/papers/` and commit them on their own, through LFS.
   - Keep the names. Where a name differs from its bib key, rename the copy to the bib key.
   - Write `tools/check_papers.py`, which lists:
     - bib entries that have no PDF;
     - PDFs that have no bib entry;
     - for the cited entries, which of them are missing a PDF.
     
     It is a list for Lotzi; it does not fetch PDFs.
   - PDFs for the papers after 2016 can be added later from the Drive year folders listed in `Lotzi-Literature-Review/OurPapers/INVENTORY.tsv`, one commit per batch.
7. **Research Grants section.**
   - Add `source/sections/grants.tex`, newest first. Only the `_WithFunding` build prints it, after Publications. Each item gives the agency and program, the title, the role (PI or co-PI, with the other investigators), the period and the amount.
   - The old sources: `Funding.tex` (Lotzi's list of awarded grants, up to 2016) and `FundingAllAttempts.tex` (2002-2007, including pending and declined proposals). For the later years, draft the list from the NSF Award Search and other public award databases, and from the funding acknowledgments in the group's papers.
   - Mark each drafted item "to confirm". Lotzi confirms or corrects the list, and adds grants that are not public (industry, internal UCF).
   - List only awarded grants. Pending and declined proposals stay out.
   - Check: the two PDFs differ only in the Research Grants section (`pdftotext` and `diff`).
8. **Webpage link.**
   - Point `Lotzi-Webpage/update-all.sh` at `../Lotzi-Resume/source/bib/Boloni.bib`, so the CV and the webpage use the same file.
   - Check that `bibweb.py` still produces the same pages.
   - This is a change in the webpage repository and is committed there.
9. **Finishing.** Write the README: how to build the two PDFs, how to add a paper, a grant, a talk or a student, and how to update the metrics.

## Versions

Not part of the current work. The layout allows them later without changing `source/`:
- each version is a small `variants/<name>/main.tex` that picks its sections;
- a subset of papers comes from bib keywords (for example `selected`) or a separate `\nocite` list;
- a subset of items inside a section comes from tags, as in Damla-Resume.

Likely versions: a short CV (to replace the 2019 two-page resume), an NSF biosketch, a bio, and per-application versions.

## Not imported

- `_obsolete/Bib2Html` and `_obsolete/Html`, which `Lotzi-Webpage/bibweb.py` replaced.
- `_obsolete/Bibliography`: `Generate*List.tex`, `old-Boloni.bib`, `.bst` files, `Boloni.ris`, `Citations.xls`.
- Build products: `.aux`, `.log`, `.bbl` and `.fdb_latexmk` files.

## Open questions for Lotzi

1. **Grants.** Confirm the items marked [to confirm] in `CV-LotziBoloni_WithFunding.pdf`:
   - NSF 2114948 and NSF 1931767 (PI);
   - the 2022 end date of NSF 1409823;
   - the new total.

   Also: is Cyber Florida #220408 one of Lotzi's grants? Are there grants after 2016 that are not in public records, such as industry or internal UCF grants?
2. **Bibliography.** Decide on the items in [REVIEW-BIBLIOGRAPHY.md](REVIEW-BIBLIOGRAPHY.md): the 8 uncited entries, the missing DOIs, and the author and title differences with damla.bib.
