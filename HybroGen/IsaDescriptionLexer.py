# Generated from IsaDescription.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("[\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\6\t\62\n\t\r\t\16\t")
        buf.write("\63\3\t\3\t\3\n\3\n\7\n:\n\n\f\n\16\n=\13\n\3\n\3\n\3")
        buf.write("\13\6\13B\n\13\r\13\16\13C\3\f\3\f\7\fH\n\f\f\f\16\fK")
        buf.write("\13\f\3\r\5\rN\n\r\3\r\3\r\3\16\3\16\3\17\3\17\6\17V\n")
        buf.write("\17\r\17\16\17W\3\17\3\17\3;\2\20\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\3\2\7")
        buf.write("\4\2\13\13\"\"\3\2\62;\4\2C\\c|\7\2\60\60\62;C\\aac|\3")
        buf.write("\2\177\177\2`\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5$\3\2\2\2")
        buf.write("\7&\3\2\2\2\t(\3\2\2\2\13*\3\2\2\2\r,\3\2\2\2\17.\3\2")
        buf.write("\2\2\21\61\3\2\2\2\23\67\3\2\2\2\25A\3\2\2\2\27E\3\2\2")
        buf.write("\2\31M\3\2\2\2\33Q\3\2\2\2\35S\3\2\2\2\37 \7C\2\2 !\7")
        buf.write("T\2\2!\"\7E\2\2\"#\7J\2\2#\4\3\2\2\2$%\7~\2\2%\6\3\2\2")
        buf.write("\2&\'\7]\2\2\'\b\3\2\2\2()\7_\2\2)\n\3\2\2\2*+\7k\2\2")
        buf.write("+\f\3\2\2\2,-\7w\2\2-\16\3\2\2\2./\7h\2\2/\20\3\2\2\2")
        buf.write("\60\62\t\2\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3\2\2")
        buf.write("\2\63\64\3\2\2\2\64\65\3\2\2\2\65\66\b\t\2\2\66\22\3\2")
        buf.write("\2\2\67;\7%\2\28:\13\2\2\298\3\2\2\2:=\3\2\2\2;<\3\2\2")
        buf.write("\2;9\3\2\2\2<>\3\2\2\2=;\3\2\2\2>?\5\31\r\2?\24\3\2\2")
        buf.write("\2@B\t\3\2\2A@\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2D")
        buf.write("\26\3\2\2\2EI\t\4\2\2FH\t\5\2\2GF\3\2\2\2HK\3\2\2\2IG")
        buf.write("\3\2\2\2IJ\3\2\2\2J\30\3\2\2\2KI\3\2\2\2LN\7\17\2\2ML")
        buf.write("\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\7\f\2\2P\32\3\2\2\2QR\7")
        buf.write("<\2\2R\34\3\2\2\2SU\7}\2\2TV\n\6\2\2UT\3\2\2\2VW\3\2\2")
        buf.write("\2WU\3\2\2\2WX\3\2\2\2XY\3\2\2\2YZ\7\177\2\2Z\36\3\2\2")
        buf.write("\2\t\2\63;CIMW\3\b\2\2")
        return buf.getvalue()


class IsaDescriptionLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    WS = 8
    COMMENT = 9
    INT = 10
    NAME = 11
    NEWLINE = 12
    SEMICOL = 13
    CINLINE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'ARCH'", "'|'", "'['", "']'", "'i'", "'u'", "'f'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "COMMENT", "INT", "NAME", "NEWLINE", "SEMICOL", "CINLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "WS", "COMMENT", "INT", "NAME", "NEWLINE", "SEMICOL", 
                  "CINLINE" ]

    grammarFileName = "IsaDescription.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


