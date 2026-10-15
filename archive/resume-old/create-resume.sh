mkdir Resume/Generated
pdflatex Bibliography/GenerateBookList.tex
pdflatex Bibliography/GenerateBookList.tex
bibtex GenerateBookList >>bibtex.err
cp GenerateBookList.bbl Resume/Generated/Book.tex

pdflatex Bibliography/GenerateChapterList.tex
pdflatex Bibliography/GenerateChapterList.tex
bibtex GenerateChapterList >>bibtex.err
cp GenerateChapterList.bbl Resume/Generated/Chapter.tex

pdflatex Bibliography/GenerateJournalList.tex
pdflatex Bibliography/GenerateJournalList.tex
bibtex GenerateJournalList >bibtex.err
cp GenerateJournalList.bbl Resume/Generated/Journal.tex

pdflatex Bibliography/GenerateConferenceList.tex
pdflatex Bibliography/GenerateConferenceList.tex
bibtex GenerateConferenceList >>bibtex.err
cp GenerateConferenceList.bbl Resume/Generated/Conference.tex

pdflatex Bibliography/GenerateWorkshopList.tex
pdflatex Bibliography/GenerateWorkshopList.tex
bibtex GenerateWorkshopList >>bibtex.err
cp GenerateWorkshopList.bbl Resume/Generated/Workshop.tex

# proceed to compile the main resume
pdflatex Resume/Resume.tex
pdflatex Resume/Resume.tex
# Clean up the temporary files of the generated stuff
rm Generate*
# clean the temporary
# rm Resume.log Resume.aux
# show the errors
cat bibtex.err
