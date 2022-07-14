# Generated from IsaDescription.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("]\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\f\6\f<\n\f\r\f\16\f=\3\f\3\f")
        buf.write("\3\r\3\r\7\rD\n\r\f\r\16\rG\13\r\3\r\3\r\3\16\6\16L\n")
        buf.write("\16\r\16\16\16M\3\17\3\17\7\17R\n\17\f\17\16\17U\13\17")
        buf.write("\3\20\5\20X\n\20\3\20\3\20\3\21\3\21\3E\2\22\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22\3\2\6\4\2\13\13\"\"\3\2\62;\4\2C\\c|")
        buf.write("\7\2\60\60\62;C\\aac|\2a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\3#\3\2\2\2\5(\3\2\2\2\7*\3\2\2\2\t,\3\2\2\2")
        buf.write("\13.\3\2\2\2\r\60\3\2\2\2\17\62\3\2\2\2\21\64\3\2\2\2")
        buf.write("\23\66\3\2\2\2\258\3\2\2\2\27;\3\2\2\2\31A\3\2\2\2\33")
        buf.write("K\3\2\2\2\35O\3\2\2\2\37W\3\2\2\2![\3\2\2\2#$\7C\2\2$")
        buf.write("%\7T\2\2%&\7E\2\2&\'\7J\2\2\'\4\3\2\2\2()\7~\2\2)\6\3")
        buf.write("\2\2\2*+\7]\2\2+\b\3\2\2\2,-\7_\2\2-\n\3\2\2\2./\7*\2")
        buf.write("\2/\f\3\2\2\2\60\61\7+\2\2\61\16\3\2\2\2\62\63\7/\2\2")
        buf.write("\63\20\3\2\2\2\64\65\7k\2\2\65\22\3\2\2\2\66\67\7w\2\2")
        buf.write("\67\24\3\2\2\289\7h\2\29\26\3\2\2\2:<\t\2\2\2;:\3\2\2")
        buf.write("\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>?\3\2\2\2?@\b\f\2\2@")
        buf.write("\30\3\2\2\2AE\7%\2\2BD\13\2\2\2CB\3\2\2\2DG\3\2\2\2EF")
        buf.write("\3\2\2\2EC\3\2\2\2FH\3\2\2\2GE\3\2\2\2HI\5\37\20\2I\32")
        buf.write("\3\2\2\2JL\t\3\2\2KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2")
        buf.write("\2\2N\34\3\2\2\2OS\t\4\2\2PR\t\5\2\2QP\3\2\2\2RU\3\2\2")
        buf.write("\2SQ\3\2\2\2ST\3\2\2\2T\36\3\2\2\2US\3\2\2\2VX\7\17\2")
        buf.write("\2WV\3\2\2\2WX\3\2\2\2XY\3\2\2\2YZ\7\f\2\2Z \3\2\2\2[")
        buf.write("\\\7<\2\2\\\"\3\2\2\2\b\2=EMSW\3\b\2\2")
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
    T__7 = 8
    T__8 = 9
    T__9 = 10
    WS = 11
    COMMENT = 12
    INT = 13
    NAME = 14
    NEWLINE = 15
    SEMICOL = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'ARCH'", "'|'", "'['", "']'", "'('", "')'", "'-'", "'i'", "'u'", 
            "'f'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "COMMENT", "INT", "NAME", "NEWLINE", "SEMICOL" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "WS", "COMMENT", "INT", "NAME", 
                  "NEWLINE", "SEMICOL" ]

    grammarFileName = "IsaDescription.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


