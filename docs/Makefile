.SUFFIXES : .svg .md .pdf

.md.pdf:
	m4 $< | pandoc -V geometry:a4paper --bibliography HybroRef.bib --filter pandoc-citeproc --to=latex --toc --number-sections --output=$@ 

INKSCAPEFLAGS  = --without-gui --export-area-drawing --export-text-to-path 
.svg.pdf:	
	inkscape ${INKSCAPEFLAGS} --export-pdf=$@ $< 

FILES = Imgs/GlobalScheme.pdf HybrogenDescription.pdf ProgrammingGuide.pdf

all: ${FILES}

clean:
	-rm ${FILES}
