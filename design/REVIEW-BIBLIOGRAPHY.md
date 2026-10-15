# Bibliography review (2026-10-15, updated after the clean-up)

Output of `python3 tools/bibcheck.py`. Resolved on 2026-10-15:
- the two duplicated `\nocite` keys were removed;
- the five DOIs that damla.bib had were copied (`Wang-2008-JPDC`, `Pryyma-2010-ComNet`,
  `Khan-2011-JAAMAS`, `Boukerche-2011-ComputerNetworks`, `Turgut-2011-CompJournal`);
- `Gjanci-2018-TMC`: title and DOI corrected from Crossref. Boloni.bib's author order
  (Petrioli before Basagni) is the published one; **damla.bib has the two swapped**;
- `Zehtabian-2020-ICNC`: "Razgandi" corrected to "Razghandi";
- `Bai-2005-Coordination`: the missing co-author H. Yu and the DOI added (Crossref).

**Still for Lotzi to decide:**
- Section 2: should any of the 8 uncited entries go into the CV? (`Matloob-2023-Waterberry`
  is typed `article`; check whether it is the arXiv version of a cited paper.)
- Section 4: the author order of `Wang-2006-BookChapter` and `Zehtabian-2022-W3PHIAI`
  differs from damla.bib; check against the published papers.

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
- `Gjanci-2018-TMC` = damla `Gjanci-2018-TMC`: authors: Boloni.bib `P. Gjanci and C. Petrioli and S. Basagni and C.A. Phillips and L. Bölöni and D. Turgut` / damla.bib `P. Gjanci and S. Basagni and C. Petrioli and C. A. Phillips and L. B{\"o}l{\"o}ni and D. Turgut`; title: Boloni.bib `Path Finding for Maximum Value of Information in Multi-Modal Underwater Wireless Sensor Networks` / damla.bib `Path Finding for Maximizing the Value of Sensed Information in Multi-modal Underwater Wireless Sensor Networks`
- `Zehtabian-2022-W3PHIAI` = damla `Zehtabian-2022-W3PHIAI`: authors: Boloni.bib `S. Zehtabian and S. Khodadadeh and D. Turgut and L. Bölöni` / damla.bib `S. Zehtabian and S. Khodadadeh and L. B{\"o}l{\"o}ni and D. Turgut`

