# Improvements to the full CV

Review of the full CV (`variants/full-cv`, 30 pages; 31 pages with funding) as of 2026-10-15.

**Assumption:** a general-purpose CV for a full professor in computer science (AI and robotics), with no specific target position.

Nothing below has been changed yet:
- §1 needs Lotzi's decisions;
- §3 and §4 are mechanical fixes that can be made at any time;
- §5 proposes an order of work.

## 0. Top priorities

1. **Visible rendering bugs.** A reader sees these on the first pages:
   - The web address in the header prints as `https://www.cs.ucf.edu/ lboloni`: the `~` became a space.
   - "Professional societies" has a garbled line: "Member of the IEEE Computer Society (since 2000) Systems of the IEEE Systems, Man and Cybernetics Society."
   - Three publications show literal HTML: `<b>Best Paper Award</b>`, `<b>Kurzweil Best AGI Idea Prize 2014</b>` and `<b>IAAI-05 Deployed Application Award</b>`.
   - Teaching has a stray section number "8.1" next to Spring 2011.
   - Full list in §3.
2. **The first page undersells current work.**
   - The Research Interests still lead with themes from 10–20 years ago: social behavior modeling, networking, AGI.
   - The current work is missing or hidden: visual proprioception and robot learning, informative path planning, LLMs and hate-speech detection, AI for medical imaging, energy-efficient (green) AI.
   - The page has no Google Scholar or ORCID link.
   - The citation metrics have no date.
3. **The strongest service roles are buried.**
   - Area Chair for ICLR 2027, Senior PC for AAAI 2022, AAAI 2027 and IJCAI 2025, and Senior TPC for LCN 2014, 2015 and 2017 are scattered among about 195 program-committee items.
   - The list is in **oldest-first** order, while every other list in the CV is newest first.
   - The ICML 2026 Silver Reviewer recognition is buried at the end of one item.
4. **Work Experience has a factual error.**
   - CPlane Inc. shows "August 2002 – August 2008", the same dates as the UCF Assistant Professor position.
   - The commented-out source says May 2000 – June 2002.
5. **Volume hides substance.** These lists dominate the page count but say little about current impact:
   - Teaching: about 3.5 pages, one course per line.
   - Program committees: about 6.5 pages.
   - PhD committees: 57 entries over about 3 pages.
   - Journal reviewer list: 46 entries.

## 1. Structure (decisions needed)

### 1.1 Funding in the default CV
- **Problem:** the default PDF has no funding at all, by design.
  - For a general faculty CV, a missing grants section is unusual; readers will assume there is no funding.
  - The record is solid: NSF HCC (PI), NSF CPS (PI), NSF EAGER (PI), NSF CHS (co-PI), and seven years of Army Research Laboratory RCTA projects.
- **Options:**
  - (a) Keep the two versions and use `_WithFunding` as the general CV.
  - (b) Print a short grants list (title, agency, role, years) in the default version and keep the amounts only in `_WithFunding`.
- **Recommendation:** (b).
- **Before either option:** confirm the "[to confirm]" items in `grants.tex`.

### 1.2 Profile paragraph at the top (optional)
Three or four lines after the header:
- the position and lab;
- the two or three current research directions;
- headline numbers: publications, citations and h-index, PhD graduates and where they work (DeepMind, Intel, Pinterest, YouTube), funding total.

This is common and costs no space in a 30-page CV.

### 1.3 Section order
- **Current order:** Education, Interests, Experience, Societies, Awards, Publications, Talks, Teaching, Students, Service.
- **Proposed order:**
  1. Contact
  2. (Profile)
  3. Research Interests
  4. Appointments (now "Work Experience")
  5. Education
  6. Honors and Awards
  7. Research Grants (see 1.1)
  8. Publications
  9. Students and Mentoring
  10. Teaching
  11. Talks
  12. Professional Service
  13. Professional Societies
- **Why:** for a full professor, the appointment and research come before the degrees. Students move ahead of teaching because they are a strength: 13 PhD graduates.

### 1.4 Split the conference list
- 46 of the 160 entries in "Conference papers" are workshop papers, symposium papers, a demo or a meeting abstract. Examples: ATSE@AAAI-2016, the NeurIPS DRL workshop, "Demoed at AAMAS 2009", the ISPN-2026 abstract.
- Readers who count publications will discount the whole list if the two kinds are mixed.
- **Proposal:** two lists, "Refereed conference papers" and "Workshop papers, demos and abstracts". Use a bib keyword (`workshop`) and `\printbibliography[keyword=workshop]` / `[notkeyword=workshop]`, as Damla-Resume does.

### 1.5 The same work in two categories
Nine papers appear twice under the same title:

| First listing | Second listing |
|---|---|
| journal `Khan-2011-JAAMAS` | workshop `Khan-2008-OptMAS` |
| journal `Boloni-2007-IJICS` | conference `Boloni-2006-DIS` |
| journal `Semmel-2006-AIMagazine` | conference `Semmel-2005-IAAI` |
| journal `Boloni-2014-BICA` | symposium `Boloni-2013-IntCog` |
| journal `Khan-2003-ISJC` | workshop `Khan-2003-CIPC` |
| journal `Boloni-2002-JoS` | workshop `Boloni-1999-Robust` |
| journal `Marinescu-2000-MathCompSim` | chapter `Marinescu-2002-ProblemSolving` |
| chapter `Luotsinen-2007-PROMAS-PostProceedings` | workshop `Luotsinen-2006-PROMAS` |
| chapter `Boloni-2004-MutabilityChapter` | workshop `Boloni-2003-SELMAS` |

- Listing a conference version and an extended journal version is normal, but identical titles look like double counting.
- **Options:**
  - keep both and add "(extended version of ...)" to the later entry; or
  - drop the earlier workshop version.
- A third NESTA entry, "NASA engineering shuttle telemetry agent", is in the KSC 2005 Annual Report and is counted as a book chapter (see 2.6).

### 1.6 Selected publications and student co-authors (optional)
- **Selected publications:** a short "Selected publications" list (8–10 papers) at the start of Publications helps a reader who will not read 230 entries. Examples: CVPR-2019, NeurIPS-2019, ICLR-2021, ICLR-2022, ICRA-2018 and ICRA-2020, AAAI-2018, PLOS ONE, IEEE TITS.
- **Student co-authors:** many CVs mark the authors who are the PI's students, for example with an asterisk or underline. This makes the mentoring visible inside the publication list.

### 1.7 Page furniture
- The footer has only a page number. Add "Ladislau Bölöni — Curriculum Vitae" to each page.
- "Last updated: \today" changes at every build. A fixed month, `\cvmetricsdate`, is better: it also dates the metrics.

## 2. Section by section

### 2.1 Contact (`contact.tex`)
- **Web address:** the `~` in the displayed URL is lost (§3).
- **Phone:**
  - The `tel:` link is a placeholder, `+000000000000`.
  - The displayed number is unformatted: "+4078232320". It should be "+1 (407) 823-2320".
- **Missing links:** Google Scholar, ORCID and the lab or group page.
- **LinkedIn** shows "lotzi.boloni", but the link is `in/lotzi-boloni`. Check which one is right.

### 2.2 Research Interests (`interests.tex`)
- **Lead with current themes**, visible in the 2023–2026 papers and talks:
  - robot learning: visual proprioception, behavior cloning and active perception, learning from demonstration;
  - multi-robot informative path planning and agricultural robotics (Waterberry Farms);
  - LLMs and NLP: implicit hate-speech detection, small language models for control;
  - AI for medicine: pediatric neurosurgery imaging;
  - energy-efficient AI and blockchain for robots.
- **Move legacy themes to one closing line**, or drop them: social behavior modeling, cloud and grid scheduling, AGI and narrative reasoning.

### 2.3 Work Experience (`experience.tex`)
- **CPlane dates are wrong** (§0.4).
- **Rename** the section "Appointments" or "Professional Experience".
- **Mark the overlaps:**
  - Composure.ai (2015–2017) overlapped the professorship; label it "consulting".
  - KTH (2018–2019) and Toulouse (2019) were during a sabbatical; label them so.
- **Name:** "University of Rome 'La Sapientia'" should be "Sapienza University of Rome".
- **Imperial College:** the dates are "April 2011 – December 2011", but an older commented line says "August 2011". Check.
- **Missing roles:** Purdue research assistant (1997–2000), and the Hungarian Academy of Sciences research visit (1994–95, now under Awards). Add them if relevant.
- **Lab:** the lab or group that the PhD students belong to is not named.

### 2.4 Professional Societies (`societies.tex`)
- **Garbled line** (§3).
- **Names:**
  - "Association **of** Computing Machinery" should be "Association **for** Computing Machinery".
  - "American Association for Artificial Intelligence" has been the "Association for the Advancement of Artificial Intelligence" since 2007.
- **Dates:** three dates are marked "approximate" in comments. Check them, or drop the years.
- **Placement:** move the section near the end; it adds little up front.

### 2.5 Honors and Awards (`awards.tex`)
- **Missing years:** the WiT Best Abstract Award (2021, the 2nd annual workshop; check) and the XPrize Pandemic Response Challenge finalist (2021) have no year.
- **Missing award:** ICML 2026 Silver Reviewer is only in the service list.
- **Not awards:**
  - Upsilon Pi Epsilon membership (undated) is a membership.
  - The 1990s scholarships and the 1990–92 programming-contest prizes can go into a short "Earlier honors" group.
- **Format:**
  - Each item should end with its year in the same place.
  - One item has wrong quotes: ”A Privacy-Preserving ...”.
  - Use one style: Award, venue or organization, year.

### 2.6 Publications (`publications.tex`, `publists/`, `Boloni.bib`)
- **Metrics:** the citation numbers have no date and may be stale. Use `\cvmetricsdate` (§1.7).
- **Book chapters that are not research chapters:**
  - `Boloni-2006-Foreword` is a foreword.
  - `Semmel-2006-Report` is a section of the NASA KSC 2005 Annual Report.
  - Move them to an "Other" group, or drop them.
- **Stale statuses:**
  - CAI-2026 is still "to be published" (the conference was in May 2026).
  - ICRA-2026, ISPN-2026, ASAB-2026 and MM-SpatialAI-2026 need page numbers and DOIs once these are available.
- **Wrong dates:**
  - ICLR-2021 shows "Jul. 2021"; ICLR 2021 was in May.
  - The TNSM 2022 journal paper is listed above two 2023 papers.
- **Missing DOIs:** 29 entries from 2016 or later have none. The list is in `tools/bibcheck.py` output and `REVIEW-BIBLIOGRAPHY.md`. The five DOIs that `damla.bib` has can be copied directly.
- **Untidy fields:**
  - DOI fields carry prefixes: "doi: doi : 10.1109", "DOI:10.1109", "https://doi.org/...". Store only the bare DOI.
  - Some entries print a `url` next to the DOI (Kakar-2026-IoT, Gyenes-2023-Genetic, the IJCNLP paper).
  - Some entries print an ISBN; FuturePlay prints a URL in the booktitle; HCW'00 prints a CiteSeer link.
- **Number fields** that print as "8 Aug.", "9 2017", "4 2008" or "2 Feb." are `number`/`month` mix-ups. JPDC 2001 shows "vol. 6, no. 61"; it should be vol. 61, no. 6.
- **The rest** (typos in titles, author names and venues) is in §4.

### 2.7 Talks (`talks.tex`)
- **Group them:** keynotes or invited talks, then seminars, then panels. All 31 items are now "Guest seminar" or "Invited lecture".
- **Duplicates:** the AGI-2014 and I2CE/IoTDI-2018 panels are listed both here and under Service > Panel discussions. Keep them in one place.
- **Repeated titles:** "Apply AI in your field of choice for fun and profit" appears six times (2018–2019). One line with the list of venues is shorter.
- **No talks after April 2025.** Add recent ones, if any.
- **Small fixes:**
  - the AGI-2014 YouTube URL runs past the right margin (`\verb`), so it is cut off;
  - leading spaces in two titles ("“ A pragmatic");
  - stray quote before "University of New South Wales";
  - "a complex social interactions".

### 2.8 Teaching (`teaching.tex`)
- **Too long:** about 3.5 pages, with each semester as a numberless `\subsection`. A table with one row per course and the semesters taught (or a two-column list) fits on half a page.
- **Errors:**
  - Spring 2011 uses `\subsection` and prints "8.1" (§3);
  - Fall 2005 and Spring 2008 each appear twice;
  - "EEL 4781:" and "EEL 4781 -" mix separators;
  - CNT 5008 has two names.
- **Missing:** courses developed (CAP 1931 AI for All, CAP 5636 Advanced AI, the AI-focused EEL 6788 topics); teaching evaluations or awards, if any; sabbatical semesters, to explain the gaps.

### 2.9 Students (`students*.tex`, `committees-*.tex`)
- **PhD alumni:**
  - Order them newest first: Zehtabian (Fall 2021) is listed after Khodadadeh (Summer 2021).
  - Use one format: "PhD CS, Fall 2021" vs "PhD, May 2011" vs "PhD., May 2006".
  - Add "Currently at" where it is missing (Bulumulle, Bai).
- **Names:**
  - "Taranjeet Singh" is "T. S. Bhatia" in the papers. Use "Taranjeet Singh Bhatia".
  - "Scott Vander Welde" should be "Scott Vander Weide".
- **MSc alumni** are not in date order: 2014, 2008, 2004, 2005.
- **PhD committees:**
  - 57 entries mix completed defenses with ongoing ones (no date).
  - Split them into "Completed" (with term) and "Current".
  - Use one format: "Dissertation:", "Topic:", or none.
  - Alternative: give only the count, e.g. "Member of 57 PhD committees (2005–2026)", with the list in an appendix variant.
- **MSc committees:** four entries say "planned Spring 2021/2022/2025". Update or drop them.
- **Undergraduate advising:** names only. Add the outcome where there is one: REU, honors thesis, paper, award.
- **Small fixes:** "allience", "milimeter", a stray closing quote in "communities”".

### 2.10 Service (`service*.tex`)
- **Leadership first:** start Service with a short "Leadership and senior roles" list:
  - Area Chair ICLR 2027;
  - Senior PC AAAI 2022, AAAI 2027 and IJCAI 2025;
  - Senior TPC LCN 2014, 2015 and 2017;
  - Local Arrangements Chair MSWiM 2011, CollaborateCom 2008 and MSAN 2005;
  - workshop co-chair KES 2004, KES 2006 and CollaborateCom 2011;
  - P&T Committee Chair (2023–2024);
  - AI Initiative search committee chair (2022–2023);
  - Faculty Senate.
- **Program committees:**
  - Reverse the order to newest first.
  - Consider grouping by venue with years: "AAMAS (2014–2026)", "NeurIPS (2021–2026)", "ICML (2021–2026)", "IEEE Globecom (2012–2024)". That would turn about 6.5 pages into about 1.
  - Drop the dates, cities and symposium names.
- **Journal editorial activity:** every role ended by 2021. If there is no current role, the section is fine but reads as past. The THRI Senior Editor role (2010–2014) is the strongest; keep it first.
- **Journal reviewer list:**
  - The newest year is 2024.
  - It also needs grouping. Use one line per journal with years, ordered by importance, or replace it with "Reviewer for 40+ journals, including ...".
- **Service with funding agencies is not printed at all:** `service-agencies.tex` exists but `service.tex` leaves it out. It holds NSF panels 2005–2023, NIST, NIH SBIR and NASA, which is significant service. Include it.
- **Committees:**
  - Four undated department items sit between dated ones. Add dates, or "(ongoing)".
  - The headings say "commitees" (twice).
  - The two DAT cluster search committees (2018–19 and 2019–20) can be one line.
  - "COVID-19 App for UCF Workgroup (2019)": 2020?
- **Typos in the PC list:** see §4.

## 3. Rendering bugs (fix first)

| Where | What the PDF shows | Cause | Fix |
|---|---|---|---|
| Header | `https://www.cs.ucf.edu/ lboloni` | `~` in the link text is a non-breaking space | `\textasciitilde{}lboloni` or `\url{}` |
| Header | phone link dials `+000000000000` | placeholder `tel:` | real number |
| Professional societies | "…(since 2000) Systems of the IEEE Systems, Man and Cybernetics Society." | the second line of a commented-out item is not commented | comment out that line in `societies.tex` |
| Publications | `<b>Best Paper Award</b>` and two more | HTML in the bib `note`, meant for the webpage | print the `note` without tags: a biblatex source map that strips `<b>`/`</b>`, or a separate field for the web (`bib2html_award`) |
| Teaching | "8.1" next to Spring 2011 | `\subsection {Spring 2011}` (numbered) | `\subsection*` |
| Talks | AGI-2014 URL cut off at the right margin | `\verb` does not break | `\url{}` |
| Last line | `\center{...}` | `\center` is an environment, not a command | `\begin{center}...\end{center}` or `\centering` |

## 4. Data quality (mechanical)

### Typos in publications (`Boloni.bib`)
- **Chapters:**
  - "A. Duta" should be "A. Dutta" (`Kulbaka-2025-BookChapter`);
  - "Kluwer Publising House".
- **Journals:**
  - "manuevering" (`Szots-2024-RoboMech`);
  - "Special Issue on Special Issue Security" (`Castellon-2023-Electronics`);
  - "maximum the value" (`Gjanci-2018-TMC`, see `REVIEW-BIBLIOGRAPHY.md`);
  - "G. Marinescu" in `Bai-2005-Coordination`: check.
- **Conferences:**
  - "Prof. of IEEE Global" (`Mayle-2017-GLOBECOM`);
  - "Comunications" (`Turgut-2013-ICC-IVE`);
  - "43nd" (`Xu-2018-LCN`);
  - "Lousiana" (`Rahmatizadeh-2018-RealVirtual`);
  - "21th" (`SAKhan-2012-BRIMS`);
  - "FLAIRS Conference,," (`White-2009-FLAIRS`);
  - "Environmnents" (`Zehtabian-2020-ICAT-EGVE`);
  - "genetic programing" (`Khan-2013-FLAIRS`);
  - "Razgandi" (`Zehtabian-2020-ICNC`; elsewhere "Razghandi");
  - "Tsompanopolou" vs "Tsompanopoulu";
  - "Maheshwaran" vs "Maheswaran";
  - "B. Rakos, Zarándy" (missing initial);
  - "K.K.Jun", "J.Hámori" (missing spaces);
  - "Ubiquituous".
- **Venue formatting:**
  - "Proc of", "Proc. of", "Proceedings of" and "in Demoed at" are mixed;
  - some entries add a full address ("Los Alamitos, CA 90720-1314").

### Typos in service and committees
- **Venue names and places:**
  - "Ultrecht";
  - "Ubiquituous";
  - "onPrinciples";
  - "Philadephia";
  - "luj-Napoca";
  - "Aucland";
  - "Dubai, United Emirates";
  - "Xinyi District, Taipei City" (drop the district).
- **Ordinal numbers:**
  - "3nd International Conference";
  - "IEEE 40h";
  - "Eight International Workshop";
  - "23nd IEEE ICMLA";
  - "IEEE 22st".
- **Dates:**
  - "IEEE ICC-2021 ... June 7-11, 2020";
  - BMVC 2022 is listed between ICLR-2023 and AAMAS-2023.
- **Headings:**
  - "commitees" (twice);
  - capitalization varies: "Work Experience" vs "Professional societies" vs "Department and college level commitees".

## 5. Proposed order of work

1. **§3 rendering bugs and the CPlane dates.** About an hour, and no decisions needed. Each fix can be checked by rebuilding and diffing the text.
2. **§4 typos and bib field clean-up,** together with the `REVIEW-BIBLIOGRAPHY.md` items.
3. **Decisions in §1:**
   - funding in the default CV;
   - profile paragraph;
   - section order;
   - the workshop split;
   - duplicate titles;
   - selected publications;
   - marking student co-authors.
4. **Rewrite the Research Interests** and add the Google Scholar and ORCID links (needs Lotzi's input).
5. **Compress Teaching, Program committees, the reviewer list and PhD committees** (§2.8–2.10). These are the largest page savings: an estimated 30 pages down to about 20.
6. **Sort the lists newest first,** using a script like `Damla-Resume/tools/sortitems.py`.

After each step: rebuild both variants, check the publication counts with `tools/bibcheck.py`, and compare the text with the previous PDF.
