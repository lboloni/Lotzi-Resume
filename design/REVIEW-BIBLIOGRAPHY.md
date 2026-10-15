# Bibliography review (2026-10-15)

Output of `python3 tools/bibcheck.py`, run during the import (design/PLAN.md, step 5).
The two duplicated `\nocite` keys (`Khan-2003-ISJC` in journals, `Boloni-2013-IRS` in
conferences) were removed; they did not change the printed CV. Nothing else in
`Boloni.bib` was changed. **For Lotzi to decide:**

- Section 2: should any of the 8 uncited entries go into the CV? (`Matloob-2023-Waterberry`
  is typed `article`; check whether it is the arXiv version of a cited paper.)
- Section 4: Damla's bib was corrected against her cv26 in October 2026, so where it has a
  DOI that Boloni.bib lacks, the DOI can be copied. The author-order differences
  (`Wang-2006-BookChapter`, `Gjanci-2018-TMC`, `Zehtabian-2022-W3PHIAI`) and the
  `Razgandi`/`Razghandi` spelling need a check against the published papers; the
  `Gjanci-2018-TMC` title in Boloni.bib ("Maximum the Value") looks like a typo.

---


`source/bib/Boloni.bib`: 238 entries.

## 1. Publication lists

- `books.tex`: 2 keys
- `chapters.tex`: 15 keys
- `conferences.tex`: 160 keys
- `journals.tex`: 53 keys

No duplicated or missing keys.

## 2. Bib entries not cited by any list

- `Boloni-2011-XapagyCognitiveArchitecture` (article, 2011): Xapagy: a cognitive architecture for narrative reasoning
- `Boloni-2013-Globecom` (inproceedings, 2013): Scheduling Data Transmissions of Underwater Sensor Nodes for Maximizing Value of Information
- `Ling-2019-GLOBECOM` (inproceedings, 2019): Predicting the temperature dynamics of scaled model and real-world {IoT}-enabled smart homes
- `Luo-2008-CollaborateCom` (inproceedings, 2008): Learning models of the negotiation partner in spatio-temporal collaboration
- `Luo-2009-ACAN` (inproceedings, 2009): Acting while negotiating in the convoy formation problem
- `Matloob-2023-Waterberry` (article, 2023): Waterberry Farms: A Novel Benchmark For Informative Path Planning
- `Sheikh-2018-GoalsRL` (inproceedings, 2018): Designing a Multi-Objective Reward Function for Creating Teams of Robotic Bodyguards Using Deep Reinforcement Learning
- `White-2009-PAIR` (inproceedings, 2009): Automatic Analysis of Embodied Team Actions

## 3. 2025-2026 papers in the inventory that are not in Boloni.bib

None.

## 4. Joint papers with damla.bib

81 damla.bib entries have Bölöni as an author; 81 match a Boloni.bib entry (by DOI, title or key).

- `Wang-2006-BookChapter` = damla `Wang-2006-BookChapter`: authors: Boloni.bib `G. Wang and Y. Ji and D.C. Marinescu and D. Turgut and L. Bölöni` / damla.bib `G. Wang and Y. Ji and D. Turgut and L. B{\"o}l{\"o}ni and D. C. Marinescu`
- `Wang-2008-JPDC` = damla `Wang-2008-JPDC`: DOI: Boloni.bib `(none)` / damla.bib `10.1016/j.jpdc.2007.07.006`
- `Pryyma-2010-ComNet` = damla `Pryyma-2010-ComNet`: DOI: Boloni.bib `(none)` / damla.bib `10.1016/j.comnet.2009.08.004`
- `Khan-2011-JAAMAS` = damla `Khan-2011-JAAMAS`: DOI: Boloni.bib `(none)` / damla.bib `10.1007/s10458-010-9134-5`
- `Boukerche-2011-ComputerNetworks` = damla `Boukerche-2011-ComputerNetworks`: DOI: Boloni.bib `(none)` / damla.bib `10.1016/j.comnet.2011.05.010`
- `Turgut-2011-CompJournal` = damla `Turgut-2011-CompJournal`: DOI: Boloni.bib `(none)` / damla.bib `10.1093/comjnl/bxp110`
- `Gjanci-2018-TMC` = damla `Gjanci-2018-TMC`: authors: Boloni.bib `P. Gjanci and C. Petrioli and S. Basagni and C.A. Phillips and L. Bölöni and D. Turgut` / damla.bib `P. Gjanci and S. Basagni and C. Petrioli and C. A. Phillips and L. B{\"o}l{\"o}ni and D. Turgut`; title: Boloni.bib `Path Finding for Maximum the Value of Sensed Information in Multi-modal Underwater Wireless Sensor Networks` / damla.bib `Path Finding for Maximizing the Value of Sensed Information in Multi-modal Underwater Wireless Sensor Networks`; DOI: Boloni.bib `(none)` / damla.bib `10.1109/TMC.2017.2706689`
- `Zehtabian-2020-ICNC` = damla `Zehtabian-2020-ICNC`: authors: Boloni.bib `S. Zehtabian and M. Razgandi and L. Bölöni and D. Turgut` / damla.bib `S. Zehtabian and M. Razghandi and L. B{\"o}l{\"o}ni and D. Turgut`
- `Zehtabian-2022-W3PHIAI` = damla `Zehtabian-2022-W3PHIAI`: authors: Boloni.bib `S. Zehtabian and S. Khodadadeh and D. Turgut and L. Bölöni` / damla.bib `S. Zehtabian and S. Khodadadeh and L. B{\"o}l{\"o}ni and D. Turgut`

