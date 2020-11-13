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
- `write/` - Writes out data appendices HTML using [Pweave](http://mpastell.com/pweave/).
- `docs/` - Data appendices published to [https://uwchr.github.io/nwdc-seg/](https://uwchr.github.io/nwdc-seg/)