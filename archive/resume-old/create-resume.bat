taskkill /im acrobat.exe
taskkill /im acrord32.exe

mkdir Resume\Generated
latex Bibliography\GenerateBookList.tex
latex Bibliography\GenerateBookList.tex
bibtex GenerateBookList >>bibtex.err
copy GenerateBookList.bbl Resume\Generated\Book.tex

latex Bibliography\GenerateChapterList.tex
latex Bibliography\GenerateChapterList.tex
bibtex GenerateChapterList >>bibtex.err
copy GenerateChapterList.bbl Resume\Generated\Chapter.tex

latex Bibliography\GenerateJournalList.tex
latex Bibliography\GenerateJournalList.tex
bibtex GenerateJournalList >bibtex.err
copy GenerateJournalList.bbl Resume\Generated\Journal.tex

latex Bibliography\GenerateConferenceList.tex
latex Bibliography\GenerateConferenceList.tex
bibtex GenerateConferenceList >>bibtex.err
copy GenerateConferenceList.bbl Resume\Generated\Conference.tex

latex Bibliography\GenerateWorkshopList.tex
latex Bibliography\GenerateWorkshopList.tex
bibtex GenerateWorkshopList >>bibtex.err
copy GenerateWorkshopList.bbl Resume\Generated\Workshop.tex


rem Clean up the temporary files of the generated stuff
del Generate*

rem proceed to compile the main resume
latex Resume\Resume.tex
latex Resume\Resume.tex
dvipdfm Resume
rem clean the temporary
rem del Resume.log Resume.dvi Resume.aux

rem show the errors
type bibtex.err
start Resume.pdf

