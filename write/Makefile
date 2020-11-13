#
# Authors:     PN
# Maintainers: PN
# Copyright:   2019, UWCHR, GPL v2 or later
# ============================================
# nwdc-seg/src/Makefile

.PHONY: all clean

all: \
	output/smu-rhu.html \
	output/smu-rhu-srms-compare.html \
	output/nwdc-srms-2.html \
	output/nwdc-srms-1.html \
	output/index.html

clean:
	rm -r output/*

output/smu-rhu.html: \
		src/smu-rhu.pmd \
		input/smu.csv.gz \
		input/rhu.csv.gz
	pweave src/smu-rhu.pmd -f md2html -o output/smu-rhu.html

output/smu-rhu-srms-compare.html: \
		src/smu-rhu.pmd \
		input/smu.csv.gz \
		input/rhu.csv.gz \
		input/srms-1.csv.gz \
		input/srms-2.csv.gz
	pweave src/smu-rhu-srms-compare.pmd -f md2html -o output/smu-rhu-srms-compare.html

output/nwdc-srms-2.html: \
		src/nwdc-srms-2.pmd \
		frozen/facil-list.csv.gz \
		input/srms-2.csv.gz \
		input/pogo.csv.gz \
		input/icij.csv.gz
	pweave src/nwdc-srms-2.pmd -f md2html -o output/nwdc-srms-2.html

output/nwdc-srms-1.html: \
		src/nwdc-srms-1.pmd \
		frozen/facil-list.csv.gz \
		input/srms-1.csv.gz \
		input/pogo.csv.gz \
		input/icij.csv.gz
	pweave src/nwdc-srms-1.pmd -f md2html -o output/nwdc-srms-1.html

output/index.html: \
		src/index.pmd \
		output/nwdc-srms-1.html
	pweave src/index.pmd -f md2html -o output/index.html
	cp -r output/* ../docs/.

# done.
