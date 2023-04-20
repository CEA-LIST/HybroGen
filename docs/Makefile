.SUFFIXES : .svg .md .pdf .pov .png

.md.pdf:
	m4 $< | pandoc -V geometry:a4paper --bibliography HybroRef.bib --filter pandoc-citeproc --to=latex --toc --number-sections --output=$@ 

.pov.png:
	povray +I$< +V +W800 +H800

INKSCAPEFLAGS  = --without-gui --export-area-drawing --export-text-to-path 
.svg.pdf:	
	inkscape ${INKSCAPEFLAGS} --export-pdf=$@ $< 

FILES = Imgs/GlobalScheme.pdf HybrogenDescription.pdf ProgrammingGuide.pdf Img/HybroGen-Logo.png

all: ${FILES}

clean:
	-rm ${FILES}
