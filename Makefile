# Main Hybrogen makefile

all:
	echo "What action do you target ?"
	echo "make buildGrammar # Build grammars (need antlr)"
	echo "make DbPopulate # "

DbPopulate:
	./H2Isa.py -s # Create database schema
	make DbArch ARCH=riscv
	make DbArch ARCH=kalray
	make DbArch ARCH=power
	./H2Isa.py -i cxram 	 # No register description for cxram
	echo "Need to generate environment ?\nExample : ./GenCrossTools.py -s -a cxram-linux -a powerpc\n"

DbArch:
	./H2Isa.py -i ${ARCH}; ./H2Reg.py -i ${ARCH}

buildGrammar:
	(cd HybroGen  ; make all) # Lexers / parsers for input data
	(cd HybroLang ; make all) # Lexers / parsers for HybroLang language

clean:
	./H2Isa.py -d
	-(cd HybroGen ;     make clean)
	-(cd HybroLang;     make clean)
	-(cd CodeExamples/; make clean)
	-(cd docs/;         make clean)

kalray:
	make buildGrammar
	make clean
	make buildGrammar
	make DbArch ARCH=kalray
	(cd CodeExamples; ./Regression.py kalray)

riscv:
	make buildGrammar
	make clean
	make buildGrammar
	make DbArch ARCH=riscv
	(cd CodeExamples; ./Regression.py riscv)

cxram:
	make buildGrammar
	make clean
	make buildGrammar
	make DbArch ARCH=riscv
	./H2Isa.py -i cxram
	(cd CodeExamples; ./RunDemo.py -a cxram -i CxRAM-SimpleAdd)
	(cd CodeExamples; ./RunDemo.py -a cxram -i CxRAM-SimpleSub)
	(cd CodeExamples; ./RunDemo.py -a cxram -i CxRAM-SimpleMul)
	(cd CodeExamples; ./RunDemo.py -a cxram -i CxRAM-ImageDiff)

power:
	make buildGrammar
	make clean
	make buildGrammar
	make DbArch ARCH=power
	(cd CodeExamples; ./Regression.py power)

installH2Default:
	make installH2 INSTALLDIR=/opt/H2/

installH2:
#	Directory tree
	install -d ${INSTALLDIR}/hybrogen/bin/HybroLang
	install -d ${INSTALLDIR}/hybrogen/bin/HybroGen/arch
	install -d ${INSTALLDIR}/hybrogen/bin/HybroGen/include
	install -d ${INSTALLDIR}/hybrogen/bin/CodeExamples
# 	Generic files
	install ${FILESMAIN} ${INSTALLDIR}/hybrogen/bin/
# 	HybroLang
	install ${FILESHYBROLANG} ${INSTALLDIR}/hybrogen/bin/HybroLang
	install ${FILESGHYBROLANG} ${INSTALLDIR}/hybrogen/bin/HybroLang
# 	Hybrogen
	install ${FILESHYBROGEN} ${INSTALLDIR}/hybrogen/bin/HybroGen/
	install ${FILESGHYBROGEN} ${INSTALLDIR}/hybrogen/bin/HybroGen/
	install ${FILESINCLUDE} ${INSTALLDIR}/hybrogen/bin/HybroGen/include

#	ISA files
	install -d ${INSTALLDIR}/hybrogen/bin/HybroGen/arch/kalray
	install ${FILESISA_K} ${INSTALLDIR}/hybrogen/bin/HybroGen/arch/kalray
	install -d ${INSTALLDIR}/hybrogen/bin/HybroGen/arch/riscv
	install ${FILESISA_RV} ${INSTALLDIR}/hybrogen/bin/HybroGen/arch/riscv
	install -d ${INSTALLDIR}/hybrogen/bin/HybroGen/arch/power
	install ${FILESISA_P} ${INSTALLDIR}/hybrogen/bin/HybroGen/arch/power
	install -d ${INSTALLDIR}/hybrogen/bin/HybroGen/arch/cxram
	install ${FILESISA_C} ${INSTALLDIR}/hybrogen/bin/HybroGen/arch/cxram
#	Grammar files

FILESISA_K = HybroGen/arch/kalray/h2-kalray.isa	\
HybroGen/arch/kalray/h2-kalray.register
FILESISA_RV = HybroGen/arch/riscv/h2-riscv.isa	\
HybroGen/arch/riscv/h2-riscv.register
FILESISA_P = HybroGen/arch/power/h2-power.isa	\
HybroGen/arch/power/h2-power.register
FILESISA_C = HybroGen/arch/cxram/h2-cxram.isa

FILESINCLUDE = HybroGen/include/h2-common.h								\
HybroGen/include/h2-kalray-kalray.h HybroGen/include/h2-riscv-CXRAM.h	\
HybroGen/include/h2-tile-cxram.h HybroGen/include/h2-riscv-RV32G.h		\
HybroGen/include/h2-riscv-GAP9.h HybroGen/include/h2-power-power.h

FILESEXAMPLES = CodeExamples/RunDemo.py CodeExamples/Regression.py	\
CodeExamples/*.hl CodeExamples/MonOeilGrisFermé.pgm					\
CodeExamples/MonOeilGris.pgm

FILESHYBROLANG = HybroLang/Makefile HybroLang/__init__.py			\
HybroLang/HybroLang.g4 HybroLang/H2ConstantOptimizer.py				\
HybroLang/H2CxRAMRewrite.py HybroLang/H2Node.py HybroLang/H2IR2.py	\
HybroLang/H2SymbolTable.py HybroLang/H2LabelTable.py				\
HybroLang/H2RegisterAllocator.py HybroLang/H2NodeType.py			\
HybroLang/H2PowerRewrite.py HybroLang/DemoTranformIR.py				\
HybroLang/H2RegisterBank.py HybroLang/H2KalrayRewrite.py			\
HybroLang/H2MovOptimize.py HybroLang/H2IRFlattener.py

FILESHYBROGEN = HybroGen/Makefile HybroGen/__init__.py				\
HybroGen/RegisterDescription.g4 HybroGen/IsaDescription.g4			\
HybroGen/Register.py HybroGen/Insn.py HybroGen/Counter.py			\
HybroGen/GenGeneratorFromDb.py HybroGen/PGen.py HybroGen/IsaDb.py	\
HybroGen/IsaDescriptionListener.py HybroGen/H2DemoAdd.py			\
HybroGen/ProxyDb.py

FILESGHYBROLANG = HybroLang/HybroLangVisitor.py				\
HybroLang/HybroLang.interp HybroLang/HybroLangLexer.interp	\
HybroLang/HybroLangLexer.py HybroLang/HybroLangLexer.tokens	\
HybroLang/HybroLangParser.py HybroLang/HybroLang.tokens

FILESGHYBROGEN = HybroGen/IsaDescriptionParser.py						\
HybroGen/RegisterDescriptionLexer.py									\
HybroGen/RegisterDescriptionListener.py									\
HybroGen/RegisterDescriptionParser.py HybroGen/IsaDescriptionLexer.py	\
HybroGen/IsaDescriptionListener.py

FILESMAIN = Makefile GenCrossTools.py H2Isa.py H2Reg.py HybroLang.py	\
LICENCE.txt ChangeLog

FILESLIST = ${FILESMAIN} ${FILESISA_K} ${FILESISA_RV} ${FILESISA_P}	\
${FILESISA_C} ${FILESHYBROLANG} ${FILESHYBROGEN} ${FILESGHYBROLANG}	\
${FILESGHYBROGEN} ${FILESEXAMPLES} ${FILESISA} ${FILESINCLUDE}

DOCS = README.GenCrossTools.md README.md docs/

distrib: buildGrammar all
	tar cvfz HybroGen-V2.0.tgz ${FILESLIST} ${CODEEXAMPLES} ${DOCS}
