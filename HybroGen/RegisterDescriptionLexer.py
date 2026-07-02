# Generated from RegisterDescription.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("`\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\6\6%\n\6\r\6\16\6&\3")
        buf.write("\6\3\6\3\7\3\7\7\7-\n\7\f\7\16\7\60\13\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\6\b\67\n\b\r\b\16\b8\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\5\tG\n\t\3\n\3\n\3\n\3\13\5\13")
        buf.write("M\n\13\3\13\3\13\3\f\3\f\7\fS\n\f\f\f\16\fV\13\f\3\f\3")
        buf.write("\f\3\r\3\r\7\r\\\n\r\f\r\16\r_\13\r\3.\2\16\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\3\2\7")
        buf.write("\4\2\13\13\"\"\3\2\62;\5\2KKQQVV\4\2C\\c|\7\2\60\60\62")
        buf.write(";C\\aac|\2k\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\3\33\3\2\2\2\5\35\3\2\2\2\7\37\3\2\2\2\t!\3\2\2\2\13")
        buf.write("$\3\2\2\2\r*\3\2\2\2\17\66\3\2\2\2\21F\3\2\2\2\23H\3\2")
        buf.write("\2\2\25L\3\2\2\2\27P\3\2\2\2\31Y\3\2\2\2\33\34\7/\2\2")
        buf.write("\34\4\3\2\2\2\35\36\7x\2\2\36\6\3\2\2\2\37 \7k\2\2 \b")
        buf.write("\3\2\2\2!\"\7h\2\2\"\n\3\2\2\2#%\t\2\2\2$#\3\2\2\2%&\3")
        buf.write("\2\2\2&$\3\2\2\2&\'\3\2\2\2\'(\3\2\2\2()\b\6\2\2)\f\3")
        buf.write("\2\2\2*.\7%\2\2+-\13\2\2\2,+\3\2\2\2-\60\3\2\2\2./\3\2")
        buf.write("\2\2.,\3\2\2\2/\61\3\2\2\2\60.\3\2\2\2\61\62\5\25\13\2")
        buf.write("\62\63\3\2\2\2\63\64\b\7\2\2\64\16\3\2\2\2\65\67\t\3\2")
        buf.write("\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\29\20")
        buf.write("\3\2\2\2:G\7\\\2\2;<\7T\2\2<G\7C\2\2=>\7H\2\2>G\7R\2\2")
        buf.write("?@\7U\2\2@G\7R\2\2AB\7I\2\2BG\7R\2\2CD\7V\2\2DG\7R\2\2")
        buf.write("EG\7Z\2\2F:\3\2\2\2F;\3\2\2\2F=\3\2\2\2F?\3\2\2\2FA\3")
        buf.write("\2\2\2FC\3\2\2\2FE\3\2\2\2G\22\3\2\2\2HI\t\4\2\2IJ\5\17")
        buf.write("\b\2J\24\3\2\2\2KM\7\17\2\2LK\3\2\2\2LM\3\2\2\2MN\3\2")
        buf.write("\2\2NO\7\f\2\2O\26\3\2\2\2PT\7&\2\2QS\t\5\2\2RQ\3\2\2")
        buf.write("\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2UW\3\2\2\2VT\3\2\2\2W")
        buf.write("X\5\17\b\2X\30\3\2\2\2Y]\t\5\2\2Z\\\t\6\2\2[Z\3\2\2\2")
        buf.write("\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^\32\3\2\2\2_]\3\2\2\2")
        buf.write("\n\2&.8FLT]\3\b\2\2")
        return buf.getvalue()


class RegisterDescriptionLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    WS = 5
    COMMENT = 6
    INT = 7
    FUNCNAME = 8
    REGWN = 9
    NEWLINE = 10
    PREFIX = 11
    NAME = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'-'", "'v'", "'i'", "'f'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "COMMENT", "INT", "FUNCNAME", "REGWN", "NEWLINE", "PREFIX", 
            "NAME" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "WS", "COMMENT", "INT", 
                  "FUNCNAME", "REGWN", "NEWLINE", "PREFIX", "NAME" ]

    grammarFileName = "RegisterDescription.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


