#
# :author: PN
# :date: 2020-01-15
# :license: GPL 2.0 or greater
#
# nwdc/clean/src/Makefile
#
#

all: \
	output/uwchr.csv.gz \
	output/icij.csv.gz \
	output/pogo.csv.gz
	
PHONY: all

output/uwchr.csv.gz: \
	src/clean.py \
	hand/clean_rules.yaml \
	hand/icij-pogo-facilities.csv \
	input/2018-ICFO-00515-Highlighted_PUBLIC.csv.gz
	python $< \
		--facilities=hand/icij-pogo-facilities.csv \
		--cleanrules=hand/clean_rules.yaml \
		--input=input/2018-ICFO-00515-Highlighted_PUBLIC.csv.gz \
		--output=$@

output/icij.csv.gz: \
	src/clean.py \
	hand/clean_rules.yaml \
	hand/icij-pogo-facilities.csv \
	input/icij-solitary-voices-final-dataset-for-publication.csv.gz
	python $< \
		--facilities=hand/icij-pogo-facilities.csv \
		--cleanrules=hand/clean_rules.yaml \
		--input=input/icij-solitary-voices-final-dataset-for-publication.csv.gz \
		--output=$@

output/pogo.csv.gz: \
	src/clean.py \
	hand/clean_rules.yaml \
	hand/icij-pogo-facilities.csv \
	input/POGO_ICE-Solitary-Confinement-FOIA-Data_01-2016--05-2018.csv.gz
	python $< \
		--facilities=hand/icij-pogo-facilities.csv \
		--cleanrules=hand/clean_rules.yaml \
		--input=input/POGO_ICE-Solitary-Confinement-FOIA-Data_01-2016--05-2018.csv.gz \
		--output=$@

# End.