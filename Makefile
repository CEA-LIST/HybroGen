# Main Hybrogen makefile

all:
	echo "What action do you target ?"
	echo "make buildGrammar # Build grammars (need antlr)"
	echo "make DbPopulate # "

# Uncomment if you whish to use distant database
# DBIDS = --dbIds "DistantHost:DataBaseName:UserDbName:DbPassword"

DbPopulate:
	./H2Isa.py -n ${DBIDS} # Create database schema
	make DbArch ARCH=aarch64
	make DbArch ARCH=riscv
	make DbArch ARCH=kalray
	make DbArch ARCH=power
	./H2Isa.py -i -a cxram ${DBIDS}	 # No register description for cxram
	echo "Need to generate environment ?\nExample : ./GenCrossTools.py -s -a cxram-linux -a powerpc\n"

DbArch:
	./H2Isa.py -i -a ${ARCH} ${DBIDS} # ISA description database insertion
	./H2Reg.py -i -a ${ARCH} ${DBIDS} # Register description database insertion

buildGrammar:
	(cd HybroGen  ; make all) # Lexers / parsers for input data
	(cd HybroLang ; make all) # Lexers / parsers for HybroLang language

clean:
	make buildGrammar
	./H2Isa.py -p ${DBIDS}
	-(cd HybroGen ;     make clean)
	-(cd HybroLang;     make clean)
	-(cd CodeExamples/; make clean)
	-(cd docs/;         make clean)

regression:
	make clean
	make DbPopulate
	make power riscv aarch64

aarch64:
	make doregression THEARCH=aarch64

kalray:
	make doregression THEARCH=kalray

riscv:
	make doregression THEARCH=riscv

power:
	make doregression THEARCH=power

cxram:
	make doregression THEARCH=cxram

doregression:
	(cd CodeExamples; ./RegressionSingleOp.py --arch ${THEARCH} > Status-Regression/${THEARCH}-`date "+%Y-%m-%d"`.txt)
	(cd CodeExamples; ./Regression.py ${THEARCH}               >> Status-Regression/${THEARCH}-`date "+%Y-%m-%d"`.txt)
	git add CodeExamples/Status-Regression/${THEARCH}-`date "+%Y-%m-%d"`.txt


installH2Default:
	./distrib.py --install /opt/H2/bin/

distrib: buildGrammar all
	mkdir -p /tmp/HybroGen/
	./distrib.py --distribution /tmp/HybroGen/
