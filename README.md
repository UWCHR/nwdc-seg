# nwdc-seg

Descriptive analysis of datasets regarding solitary confinement (segregation) at the Northwest ICE Processing Center (a.k.a. Northwest Detention Center) in Tacoma, Washington for the report "Solitary Confinement at the Northwest Detention Center" by the University of Washington Center for Human Rights.

## Repository description

This repo uses [Git LFS](https://git-lfs.github.com/).

This project uses "Principled Data Processing" techniques and tools developed by [@HRDAG](https://github.com/HRDAG); see for example ["The Task Is A Quantum of Workflow."](https://hrdag.org/2016/06/14/the-task-is-a-quantum-of-workflow/)

### Tasks

Project tasks, in order of workflow (not all tasks will be present in all projects):

- `import/` - Convenience task for importing datasets. Input files in `import/input/` have been previously modified in a private repository to drop fields containing potentially sensitive unredacted information, and subjected to minimal cleaning and standardization (code available for review by request). Input files are symlinked to `import/output/` and then to `input/` of downstream task for transformation and analysis.
  - `import/frozen/` - Contains original PDF and XLSX versions of interal GEO Group reports which do not contain sensitive fields.
- `analyze/` - Contains various exploratory Jupyter notebooks. These notebooks and their outputs are exploratory and do not necessarily reflect the findings of UWCHR's report.
  - `analyze/output/` contains various versions of figures and data subsets; currently none of these are used in any downstream tasks.
- `write/` - Writes out data appendices including all figures cited in UWCHR report to HTML using [Pweave](http://mpastell.com/pweave/).
- `docs/` - Data appendices published to [https://uwchr.github.io/nwdc-seg/](https://uwchr.github.io/nwdc-seg/)

### To do:

- [x] Add recids in nwdc-dev/clean/
- [x] Write cleanstats in nwdc-dev/clean
- [x] Check for duplicates in SMU - 14
- [x] Check for duplicates in RHU - 75
- [x] Check for duplicates in SRMS 1 - 0
- [x] Check for duplicates in SRMS 2 - 6
- [x] Refresh nwdc-seg/ with cleaned datasets
- [x] smu.pmd: `citizenship` -> `hashid`
- [x] rhu.ipynb to smu-rhu.pmd
- [x] National comparisons based on POGO to separate .pmd
- [x] Fix inputs for nwdc-srms-1.pmd, remove national comparison section
- [ ] Basic qualitiatve descriptive stats for SMU/RHU?
- [x] smu-rhu-srms-compare.ipynb to .pmd
- [x] DHS comparisons to natl-srms.pmd
- [x] Check dropping null release dates
- [x] Update report stats after drop duplicates
- [ ] Links to relevant data appendix sections in report text 
- [ ] Links between appendices 
- [ ] Clean up remaining notebooks
