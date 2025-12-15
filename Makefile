# Main Hybrogen makefile

all:
	echo "What action do you target ?"
	echo "make buildGrammar # Build grammars (need antlr)"
	echo "make DbPopulate   # Fill database with instruction sets"
	echo "make clean buildGrammar DbPopulate "

# Uncomment if you whish to use distant database
# DBIDS = --dbIds "DistantHost:DataBaseName:UserDbName:DbPassword"

DbPopulate:
	./H2Isa.py -n ${DBIDS} # Create database schema
	make DbArch ARCH=aarch64
	make DbArch ARCH=riscv
	make DbArch ARCH=power
	./H2Isa.py -i -a cxram ${DBIDS}	 # No register description for cxram
	@echo "Need to generate environment ?"
	@echo "Example : ./GenCrossTools.py -s -a cxram-linux -a powerpc"

DbArch:
	./H2Isa.py -i -a ${ARCH} ${DBIDS} # ISA description database insertion
	./H2Reg.py -i -a ${ARCH} ${DBIDS} # Register description database insertion

buildGrammar:
	(cd HybroGen  ; make all) # Lexers / parsers for input data
	(cd HybroLang ; make all) # Lexers / parsers for HybroLang language

stats:
	wc -l *.py HybroLang/*.py HybroGen/*.py

clean:
	make buildGrammar
	./H2Isa.py -p ${DBIDS}
	./H2Reg.py -p ${DBIDS}
	-(cd HybroGen ;     make clean)
	-(cd HybroLang;     make clean)
	-(cd CodeExamples/; make clean)
	-(cd docs/;         make clean)

aarch64:
	make doregression THEARCH=aarch64

riscv:
	make doregression THEARCH=riscv

power:
	make doregression THEARCH=power

cxram:
	make doregression THEARCH=cxram

installH2Default:
	./distrib.py --install /opt/H2/bin/

distrib: buildGrammar all
	mkdir -p /tmp/HybroGen/
	./distrib.py --distribution /tmp/HybroGen/
