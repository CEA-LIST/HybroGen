FILES = HybroLangLexer.py HybroLangListener.py HybroLangParser.py
ANTLRP = antlr4 -Dlanguage=Python3
ANTLRFLAGS = -package HybroLang -no-listener -visitor
ANTLRJ = antlr4
JDIR = /usr/share/java
CLASSP = ${JDIR}/antlr4-runtime.jar
GRUN = java -cp .:${JDIR}/antlr4.jar:${JDIR}/antlr4-runtime.jar:${JDIR}/treelayout.jar org.antlr.v4.gui.TestRig
all: ${FILES}

${FILES} : HybroLang.g4
	${ANTLRP} ${ANTLRFLAGS} HybroLang.g4

debuggui:
	make makedebug GRUNOPT=-gui

debuglex:
	make makedebug GRUNOPT=-tokens

debugtree: makedebug
	make makedebug GRUNOPT=-tree

makedebug:
	make clean
	${ANTLRJ} HybroLang.g4
	javac -cp ${CLASSP} HybroLang*.java
	${GRUN} HybroLang compilationunit ${GRUNOPT} <  ../CodeExamples/undertest.hll

clean:
	-rm ${FILES}
	-rm HybroLang.interp  HybroLangLexer.interp HybroLangLexer.tokens  HybroLang.tokens
	-rm HybroLang*.class HybroLang*.java
	-rm HybroLang*.dot
