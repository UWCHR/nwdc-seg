#
# Authors:     PN
# Maintainers: PN
# Copyright:   2019, UWCHR, GPL v2 or later
# ============================================
# nwdc/write/src/Makefile

.PHONY: all clean

all: \
	output/nwdc.html \
	output/memo.html

clean:
	rm -r output/*

output/memo.html: \
		src/memo.pmd \
		hand/alos_dict.yaml \
		hand/adp_dict.yaml \
		input/uwchr.csv.gz \
		input/pogo.csv.gz \
		input/icij.csv.gz
	pweave src/memo.pmd -f md2html -o output/memo.html

output/nwdc.html: \
		src/nwdc.pmd \
		hand/alos_dict.yaml \
		hand/adp_dict.yaml \
		input/uwchr.csv.gz \
		input/pogo.csv.gz \
		input/icij.csv.gz
	pweave src/nwdc.pmd -f md2html -o output/nwdc.html

# done.
