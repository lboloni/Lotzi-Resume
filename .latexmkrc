# Run latexmk from the repository root, e.g.
#   latexmk -outdir=output variants/full-cv/CV-LotziBoloni.tex
# so that source/... paths resolve and style/lotzicv.sty is found.
$pdf_mode = 5;          # xelatex (fontspec, fontawesome5)
$bibtex_use = 2;        # run biber; delete the .bbl on clean
ensure_path('TEXINPUTS', './style//');
