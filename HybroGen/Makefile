# Hybrogen general makefile
FILES = IsaDescriptionLexer.py IsaDescriptionListener.py IsaDescriptionParser.py
FILESR= RegisterDescriptionLexer.py RegisterDescriptionListener.py RegisterDescriptionParser.py
ANTLRP = antlr4 -Dlanguage=Python3

all: ${FILES} ${FILESR}

run: all

${FILES} : IsaDescription.g4
	${ANTLRP} IsaDescription.g4

reg: ${FILESR}
${FILESR} : RegisterDescription.g4
	${ANTLRP} RegisterDescription.g4

generateAllIsa:
	${MAKE} H2ISAPARAM=-a doForParam
	${MAKE} H2ISAPARAM=-c doForParam

verifyAllCode: generateAllIsa
	${MAKE} verifyOneCode ARCH=riscv
	${MAKE} verifyOneCode ARCH=k1
	${MAKE} verifyOneCode ARCH=power
	${MAKE} verifyOneCode ARCH=x86

verifyOneCode:
	clang -ferror-limit=2 -E include/h2-macro-${ARCH}.h
	clang -ferror-limit=2 -c include/h2-funct-${ARCH}.h
	clang -ferror-limit=2 -c include/h2-insn-${ARCH}.h -I include/

doForParam:
	../H2Isa.py ${H2ISAPARAM} ${ARCH}

riscv: all
	${MAKE} doForParam H2ISAPARAM=-a ARCH=riscv 
	${MAKE} doForParam H2ISAPARAM=-c ARCH=riscv
	${MAKE} doForParam H2ISAPARAM=-i ARCH=riscv
	${MAKE} verifyOneCode ARCH=riscv

k1: all
	${MAKE} doForParam H2ISAPARAM=-a ARCH=k1 
	${MAKE} doForParam H2ISAPARAM=-c ARCH=k1
	${MAKE} doForParam H2ISAPARAM=-i ARCH=k1
	${MAKE} verifyOneCode ARCH=k1

x86: all
	${MAKE} doForParam H2ISAPARAM=-a ARCH=x86
	${MAKE} doForParam H2ISAPARAM=-c ARCH=x86
	${MAKE} doForParam H2ISAPARAM=-i ARCH=x86
	${MAKE} verifyOneCode ARCH=x86

power: all
	${MAKE} doForParam H2ISAPARAM=-a ARCH=power
	${MAKE} doForParam H2ISAPARAM=-c ARCH=power
	${MAKE} doForParam H2ISAPARAM=-i ARCH=power
	${MAKE} verifyOneCode ARCH=power

alltargets:
	${MAKE} riscv k1 x86 power

debuggui: 
	${MAKE} makedebug GRUNOPT=-gui

debuglex: 
	${MAKE} makedebug GRUNOPT=-tokens

debugtree: makedebug
	${MAKE} makedebug GRUNOPT=-tree

makedebug :
	Antlr4 RegisterDescription.g4
	javac -target 1.11 -cp /home/hpc/Appli/Antlr4/antlr-4.7.1-complete.jar RegisterDescription*.java
	Grun RegisterDescription registeredescription ${GRUNOPT} <  arch/riscv/h2-riscv.register

clean:
	-rm RegisterDescriptionListener.* RegisterDescriptionVisitor.* RegisterDescriptionLexer.*
	-rm RegisterDescriptionParser.* RegisterDescription.interp  RegisterDescription.tokens
	-rm IsaDescriptionListener.* IsaDescriptionVisitor.* IsaDescriptionLexer.*
	-rm IsaDescriptionParser.* IsaDescription.interp  IsaDescription.tokens
	-rm *.java *.class
	-rm -rf __pycache__
	-rm include/h2-funct-*.h  include/h2-insn-*.h  include/h2-macro-*.h  include/h2-funct-*.gch
