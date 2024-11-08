# nwdc-seg

Descriptive analysis of datasets, primarily from ICE's Segregation Review Management System (SRMS), regarding solitary confinement (segregation) at the Northwest Detention Center (a.k.a. Northwest ICE Processing Center) in Tacoma, Washington for the report ["Human Rights Conditions at the Northwest Detention Center: Solitary Confinement"](https://jsis.washington.edu/humanrights/2020/11/30/nwdc-solitary/), published November 30, 2020 by the University of Washington Center for Human Rights. Data appendices published to [https://uwchr.github.io/nwdc-seg/](https://uwchr.github.io/nwdc-seg/).

Further descriptive analysis of data obtained by Phyisicans for Human Rights/Harvard for the March 15, 2024 report ["NWDC Conditions Research Update: Charles Leo Daniel’s Death at NWDC in Context"](https://jsis.washington.edu/humanrights/2024/03/15/nwdc-conditions-research-update-daniel-death-in-context/) is published here: [https://uwchr.github.io/nwdc-seg/phr-srms.html](https://uwchr.github.io/nwdc-seg/phr-srms.html).

## Repository description

This repo uses [Git LFS](https://git-lfs.github.com/).

This project uses "Principled Data Processing" techniques and tools developed by [@HRDAG](https://github.com/HRDAG); see for example ["The Task Is A Quantum of Workflow."](https://hrdag.org/2016/06/14/the-task-is-a-quantum-of-workflow/)

### Tasks

Project tasks, in order of workflow:

- `import/`: Convenience task for importing datasets. Input files in `import/input/` have been previously modified in a private repository to drop fields containing potentially sensitive unredacted information, and subjected to minimal cleaning and standardization (code available for review by request). Input files are symlinked to `import/output/` and then to `input/` of downstream task for transformation and analysis.
  - `import/frozen/`: Contains original PDF and XLSX versions of interal GEO Group reports which do not contain sensitive fields.
- `analyze/`: Contains various exploratory Jupyter notebooks. These notebooks and their outputs are exploratory and do not necessarily reflect the findings of UWCHR's report.
  - `analyze/output/`: contains various versions of figures and data subsets; currently none of these are used in any downstream tasks.
- `write/`: Writes out data appendices including all figures cited in UWCHR report to HTML using [Pweave](http://mpastell.com/pweave/).
- `docs/`: Data appendices published to [https://uwchr.github.io/nwdc-seg/](https://uwchr.github.io/nwdc-seg/)

## Data and sources

### Nationwide ICE SRMS data
- `import/input/SRMS_spreadsheet_9.1.2018_-_9.1.2023_Redacted.csv.gz`: Data obtained students and faculty of the Immigration and Refugee Clinical Program at Harvard Law School, members of the Peeler Immigration Lab at Harvard Medical School, and Physicians for Human Rights. "'Endless Nightmare': Torture and Inhuman Treatment in Solitary Confinement in U.S. Immigration Detention", Physicians for Human Rights, February 6, 2024: [https://phr.org/our-work/resources/endless-nightmare-solitary-confinement-in-us-immigration-detention/](https://phr.org/our-work/resources/endless-nightmare-solitary-confinement-in-us-immigration-detention/).
  - Replication data: Ardalan, Sabi; Avedian, Arevik; Torrey, Phil, 2024, "Replication data and analysis for '“Endless Nightmare” Torture and Inhuman Treatment in Solitary Confinement in U.S. Immigration Detention'", https://doi.org/10.7910/DVN/AT7YFA, Harvard Dataverse, V2, UNF:6:OwNnKS9lAhTt1Sbm4FHxjg== [fileUNF] 
- `import/input/pogo.csv.gz`: Data obtained by Project On Government Oversight. Nick Schwellenbach, Mia Steinle, Katherine Hawkins, Andrea Peterson, "ISOLATED: ICE Confines Some Detainees with Mental Illness in Solitary for Months", POGO, August 14, 2019: [https://www.pogo.org/investigations/isolated-ice-confines-some-detainees-with-mental-illness-in-solitary-for-months](https://www.pogo.org/investigations/isolated-ice-confines-some-detainees-with-mental-illness-in-solitary-for-months)
- `import/input/icij.csv.gz`: Data obtained by International Consortium of Investigative Journalists. Spencer Woodman, Karrie Kehoe, Maryam Saleh and Hannah Rappleye, "Thousands of Immigrants Suffer In US Solitary Confinement", ICIJ, May 21, 2019: [https://www.icij.org/investigations/solitary-voices/thousands-of-immigrants-suffer-in-us-solitary-confinement/](https://www.icij.org/investigations/solitary-voices/thousands-of-immigrants-suffer-in-us-solitary-confinement/)

### Northwest Detention Center (NWDC)
- `import/input/srms-1.csv.gz`: ICE SRMS data for NWDC obtained by UW Center for Human Rights.
- `import/input/srms-2.csv.gz`: ICE SRMS data for NWDC obtained by UW Center for Human Rights.
- `import/input/rhu.csv.gz`: GEO Group "Restricted Housing Unit" log of completed segregation placements.
- `import/input/smu.csv.gz`: GEO Group "GEOtrack" report of detainee housing assignments within segregation.
