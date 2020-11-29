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
	output/natl-srms.html \
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
	sed -i 's/"src\/smu-rhu\.pmd"/"https:\/\/github\.com\/UWCHR\/nwdc-seg\/blob\/master\/write\/src\/smu-rhu\.pmd"/' 'output/smu-rhu.html'

output/smu-rhu-srms-compare.html: \
		src/smu-rhu-srms-compare.pmd \
		input/smu.csv.gz \
		input/rhu.csv.gz \
		input/srms-1.csv.gz \
		input/srms-2.csv.gz
	pweave src/smu-rhu-srms-compare.pmd -f md2html -o output/smu-rhu-srms-compare.html
	sed -i 's/"src\/smu-rhu-srms-compare\.pmd"/"https:\/\/github\.com\/UWCHR\/nwdc-seg\/blob\/master\/write\/src\/smu-rhu-srms-compare\.pmd"/' 'output/smu-rhu-srms-compare.html'

output/natl-srms.html: \
		src/natl-srms.pmd \
		frozen/facil-list.csv.gz \
		input/srms-1.csv.gz \
		input/pogo.csv.gz \
		input/icij.csv.gz
	pweave src/natl-srms.pmd -f md2html -o output/natl-srms.html
	sed -i 's/"src\/natl-srms\.pmd"/"https:\/\/github\.com\/UWCHR\/nwdc-seg\/blob\/master\/write\/src\/natl-srms\.pmd"/' 'output/natl-srms.html'

output/nwdc-srms-2.html: \
		src/nwdc-srms-2.pmd \
		frozen/facil-list.csv.gz \
		input/srms-2.csv.gz \
		input/pogo.csv.gz \
		input/icij.csv.gz
	pweave src/nwdc-srms-2.pmd -f md2html -o output/nwdc-srms-2.html
	sed -i 's/"src\/nwdc-srms-2\.pmd"/"https:\/\/github\.com\/UWCHR\/nwdc-seg\/blob\/master\/write\/src\/nwdc-srms-2\.pmd"/' 'output/nwdc-srms-2.html'

output/nwdc-srms-1.html: \
		src/nwdc-srms-1.pmd \
		frozen/facil-list.csv.gz \
		input/srms-1.csv.gz \
		input/pogo.csv.gz \
		input/icij.csv.gz
	pweave src/nwdc-srms-1.pmd -f md2html -o output/nwdc-srms-1.html
	sed -i 's/"src\/nwdc-srms-1\.pmd"/"https:\/\/github\.com\/UWCHR\/nwdc-seg\/blob\/master\/write\/src\/nwdc-srms-1\.pmd"/' 'output/nwdc-srms-1.html'

output/index.html: \
		src/index.pmd \
		output/nwdc-srms-1.html
	pweave src/index.pmd -f md2html -o output/index.html
	sed -i 's/"src\/index\.pmd"/"https:\/\/github\.com\/UWCHR\/nwdc-seg\/blob\/master\/write\/src\/index\.pmd"/' 'output/index.html'
	cp -r output/* ../docs/.

# done.
