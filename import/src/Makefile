#
# :author: PN
# :date: 2020-02-06
# :license: GPL 2.0 or greater
#
# 
# nwdc-seg/import/src/Makefile
#

all: \
	output/2018-ICFO-00515-Highlighted_PUBLIC.csv.gz \
	output/POGO_ICE-Solitary-Confinement-FOIA-Data_01-2016--05-2018.csv.gz \
	output/icij-solitary-voices-final-dataset-for-publication.csv.gz

PHONY: all

output/2018-ICFO-00515-Highlighted_PUBLIC.csv.gz: \
		input/2018-ICFO-00515-Highlighted_PUBLIC.csv.gz
	cd output && ln -sf ../input/2018-ICFO-00515-Highlighted_PUBLIC.csv.gz .

output/POGO_ICE-Solitary-Confinement-FOIA-Data_01-2016--05-2018.csv.gz: \
		input/POGO_ICE-Solitary-Confinement-FOIA-Data_01-2016--05-2018.csv.gz
	cd output && ln -sf ../input/POGO_ICE-Solitary-Confinement-FOIA-Data_01-2016--05-2018.csv.gz .

output/icij-solitary-voices-final-dataset-for-publication.csv.gz: \
	input/icij-solitary-voices-final-dataset-for-publication.csv.gz
	cd output && ln -sf ../input/icij-solitary-voices-final-dataset-for-publication.csv.gz .

# End.
