#
# Authors:     PN
# Maintainers: PN
# Copyright:   2019, UWCHR, GPL v2 or later
# ============================================
# nwdc/write/src/Makefile

.PHONY: all clean

all: \
	output/nwdc.html

clean:
	rm -r output/*

output/nwdc.html: \
		src/nwdc.pmd \
		frozen/alos_dict.yaml \
		frozen/adp_dict.yaml \
		input/uwchr.csv.gz \
		input/pogo.csv.gz \
		input/icij.csv.gz
	pweave src/nwdc.pmd -f md2html -o output/nwdc.html

# done.
