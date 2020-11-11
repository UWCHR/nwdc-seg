#
# Authors:     PN
# Maintainers: PN
# Copyright:   2019, UWCHR, GPL v2 or later
# ============================================
# nwdc-seg/write/src/Makefile

.PHONY: all clean

all: \
	write/output/nwdc-srms-2.html \
	write/output/nwdc-srms-1.html \
	write/output/index.html

clean:
	rm -r write/output/*

write/output/nwdc-srms-2.html: \
		write/src/nwdc-srms-2.pmd \
		write/frozen/alos_dict.yaml \
		write/frozen/adp_dict.yaml \
		write/frozen/facil-list.csv.gz \
		write/input/srms-2.csv.gz \
		write/input/rhu.csv.gz \
		write/input/smu.csv.gz \
		write/input/pogo.csv.gz \
		write/input/icij.csv.gz
	pweave write/src/nwdc-srms-2.pmd -f md2html -o write/output/nwdc-srms-2.html

write/output/nwdc-srms-1.html: \
		write/src/nwdc-srms-1.pmd \
		write/frozen/alos_dict.yaml \
		write/frozen/adp_dict.yaml \
		write/frozen/facil-list.csv.gz \
		write/input/srms-1.csv.gz \
		write/input/rhu.csv.gz \
		write/input/smu.csv.gz \
		write/input/pogo.csv.gz \
		write/input/icij.csv.gz
	pweave write/src/nwdc-srms-1.pmd -f md2html -o write/output/nwdc-srms-1.html

write/output/index.html: \
		write/src/index.pmd \
		write/output/nwdc-srms-1.html
	pweave write/src/index.pmd -f md2html -o write/output/index.html
	cp -r write/output/* docs/.

# done.
