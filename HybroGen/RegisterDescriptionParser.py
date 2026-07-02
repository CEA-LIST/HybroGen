# Generated from RegisterDescription.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("Y\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\3\3\3\6\3&\n\3\r")
        buf.write("\3\16\3\'\3\4\3\4\3\5\3\5\3\6\3\6\3\6\6\6\61\n\6\r\6\16")
        buf.write("\6\62\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7<\n\7\3\b\3\b\3\t")
        buf.write("\3\t\3\t\5\tC\n\t\3\n\3\n\5\nG\n\n\3\13\3\13\3\f\3\f\3")
        buf.write("\f\5\fN\n\f\3\r\5\rQ\n\r\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\20\2\2\21\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36\2")
        buf.write("\3\3\2\5\6\2S\2 \3\2\2\2\4%\3\2\2\2\6)\3\2\2\2\b+\3\2")
        buf.write("\2\2\n\60\3\2\2\2\f\64\3\2\2\2\16=\3\2\2\2\20?\3\2\2\2")
        buf.write("\22F\3\2\2\2\24H\3\2\2\2\26J\3\2\2\2\30P\3\2\2\2\32R\3")
        buf.write("\2\2\2\34T\3\2\2\2\36V\3\2\2\2 !\5\4\3\2!\"\5\n\6\2\"")
        buf.write("\3\3\2\2\2#&\5\6\4\2$&\5\b\5\2%#\3\2\2\2%$\3\2\2\2&\'")
        buf.write("\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(\5\3\2\2\2)*\7\b\2\2*\7")
        buf.write("\3\2\2\2+,\7\f\2\2,\t\3\2\2\2-\61\5\6\4\2.\61\5\f\7\2")
        buf.write("/\61\5\b\5\2\60-\3\2\2\2\60.\3\2\2\2\60/\3\2\2\2\61\62")
        buf.write("\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\13\3\2\2\2\64")
        buf.write("\65\5\36\20\2\65\66\5\30\r\2\66\67\5\32\16\2\678\5\16")
        buf.write("\b\289\5\34\17\29;\5\22\n\2:<\7\f\2\2;:\3\2\2\2;<\3\2")
        buf.write("\2\2<\r\3\2\2\2=>\5\20\t\2>\17\3\2\2\2?B\7\r\2\2@A\7\3")
        buf.write("\2\2AC\7\t\2\2B@\3\2\2\2BC\3\2\2\2C\21\3\2\2\2DG\5\24")
        buf.write("\13\2EG\5\26\f\2FD\3\2\2\2FE\3\2\2\2G\23\3\2\2\2HI\7\n")
        buf.write("\2\2I\25\3\2\2\2JM\7\13\2\2KL\7\3\2\2LN\7\t\2\2MK\3\2")
        buf.write("\2\2MN\3\2\2\2N\27\3\2\2\2OQ\7\4\2\2PO\3\2\2\2PQ\3\2\2")
        buf.write("\2Q\31\3\2\2\2RS\t\2\2\2S\33\3\2\2\2TU\7\t\2\2U\35\3\2")
        buf.write("\2\2VW\7\16\2\2W\37\3\2\2\2\13%\'\60\62;BFMP")
        return buf.getvalue()


class RegisterDescriptionParser ( Parser ):

    grammarFileName = "RegisterDescription.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'v'", "'i'", "'f'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS", "COMMENT", "INT", "FUNCNAME", "REGWN", 
                      "NEWLINE", "PREFIX", "NAME" ]

    RULE_registerdescription = 0
    RULE_headerlines = 1
    RULE_commentline = 2
    RULE_emptyline = 3
    RULE_registerlines = 4
    RULE_registerline = 5
    RULE_registerlist = 6
    RULE_registerprefix = 7
    RULE_registerfunctionlist = 8
    RULE_registerfunction = 9
    RULE_registerfunctionwn = 10
    RULE_regbankvec = 11
    RULE_regbank = 12
    RULE_registerwidth = 13
    RULE_extension = 14

    ruleNames =  [ "registerdescription", "headerlines", "commentline", 
                   "emptyline", "registerlines", "registerline", "registerlist", 
                   "registerprefix", "registerfunctionlist", "registerfunction", 
                   "registerfunctionwn", "regbankvec", "regbank", "registerwidth", 
                   "extension" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    WS=5
    COMMENT=6
    INT=7
    FUNCNAME=8
    REGWN=9
    NEWLINE=10
    PREFIX=11
    NAME=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RegisterdescriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def headerlines(self):
            return self.getTypedRuleContext(RegisterDescriptionParser.HeaderlinesContext,0)


        def registerlines(self):
            return self.getTypedRuleContext(RegisterDescriptionParser.RegisterlinesContext,0)


        def getRuleIndex(self):
            return RegisterDescriptionParser.RULE_registerdescription

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegisterdescription" ):
                listener.enterRegisterdescription(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegisterdescription" ):
                listener.exitRegisterdescription(self)




    def registerdescription(self):

        localctx = RegisterDescriptionParser.RegisterdescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_registerdescription)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.headerlines()
            self.state = 31
            self.registerlines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HeaderlinesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commentline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegisterDescriptionParser.CommentlineContext)
            else:
                return self.getTypedRuleContext(RegisterDescriptionParser.CommentlineContext,i)


        def emptyline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegisterDescriptionParser.EmptylineContext)
            else:
                return self.getTypedRuleContext(RegisterDescriptionParser.EmptylineContext,i)


        def getRuleIndex(self):
            return RegisterDescriptionParser.RULE_headerlines

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderlines" ):
                listener.enterHeaderlines(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderlines" ):
                listener.exitHeaderlines(self)




    def headerlines(self):

        localctx = RegisterDescriptionParser.HeaderlinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_headerlines)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 35
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [RegisterDescriptionParser.COMMENT]:
                        self.state = 33
                        self.commentline()
                        pass
                    elif token in [RegisterDescriptionParser.NEWLINE]:
                        self.state = 34
                        self.emptyline()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 37 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(RegisterDescriptionParser.COMMENT, 0)

        def getRuleIndex(self):
            return RegisterDescriptionParser.RULE_commentline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentline" ):
                listener.enterCommentline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentline" ):
                listener.exitCommentline(self)




    def commentline(self):

        localctx = RegisterDescriptionParser.CommentlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_commentline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(RegisterDescriptionParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EmptylineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(RegisterDescriptionParser.NEWLINE, 0)

        def getRuleIndex(self):
            return RegisterDescriptionParser.RULE_emptyline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyline" ):
                listener.enterEmptyline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyline" ):
                listener.exitEmptyline(self)




    def emptyline(self):

        localctx = RegisterDescriptionParser.EmptylineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_emptyline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(RegisterDescriptionParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RegisterlinesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commentline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegisterDescriptionParser.CommentlineContext)
            else:
                return self.getTypedRuleContext(RegisterDescriptionParser.CommentlineContext,i)


        def registerline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegisterDescriptionParser.RegisterlineContext)
            else:
                return self.getTypedRuleContext(RegisterDescriptionParser.RegisterlineContext,i)


        def emptyline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RegisterDescriptionParser.EmptylineContext)
            else:
                return self.getTypedRuleContext(RegisterDescriptionParser.EmptylineContext,i)


        def getRuleIndex(self):
            return RegisterDescriptionParser.RULE_registerlines

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegisterlines" ):
                listener.enterRegisterlines(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegisterlines" ):
                listener.exitRegisterlines(self)




    def registerlines(self):

        localctx = RegisterDescriptionParser.RegisterlinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_registerlines)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [RegisterDescriptionParser.COMMENT]:
                    self.state = 43
                    self.commentline()
                    pass
                elif token in [RegisterDescriptionParser.NAME]:
                    self.state = 44
                    self.registerline()
                    pass
                elif token in [RegisterDescriptionParser.NEWLINE]:
                    self.state = 45
                    self.emptyline()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 48 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RegisterDescriptionParser.COMMENT) | (1 << RegisterDescriptionParser.NEWLINE) | (1 << RegisterDescriptionParser.NAME))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RegisterlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def extension(self):
            return self.getTypedRuleContext(RegisterDescriptionParser.ExtensionContext,0)


        def regbankvec(self):
            return self.getTypedRuleContext(RegisterDescriptionParser.RegbankvecContext,0)


        def regbank(self):
            return self.getTypedRuleContext(RegisterDescriptionParser.RegbankContext,0)


        def registerlist(self):
            return self.getTypedRuleContext(RegisterDescriptionParser.RegisterlistContext,0)


        def registerwidth(self):
            return self.getTypedRuleContext(RegisterDescriptionParser.RegisterwidthContext,0)


        def registerfunctionlist(self):
            return self.getTypedRuleContext(RegisterDescriptionParser.RegisterfunctionlistContext,0)


        def NEWLINE(self):
            return self.getToken(RegisterDescriptionParser.NEWLINE, 0)

        def getRuleIndex(self):
            return RegisterDescriptionParser.RULE_registerline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegisterline" ):
                listener.enterRegisterline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegisterline" ):
                listener.exitRegisterline(self)




    def registerline(self):

        localctx = RegisterDescriptionParser.RegisterlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_registerline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.extension()
            self.state = 51
            self.regbankvec()
            self.state = 52
            self.regbank()
            self.state = 53
            self.registerlist()
            self.state = 54
            self.registerwidth()
            self.state = 55
            self.registerfunctionlist()
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 56
                self.match(RegisterDescriptionParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RegisterlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def registerprefix(self):
            return self.getTypedRuleContext(RegisterDescriptionParser.RegisterprefixContext,0)


        def getRuleIndex(self):
            return RegisterDescriptionParser.RULE_registerlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegisterlist" ):
                listener.enterRegisterlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegisterlist" ):
                listener.exitRegisterlist(self)




    def registerlist(self):

        localctx = RegisterDescriptionParser.RegisterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_registerlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.registerprefix()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RegisterprefixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREFIX(self):
            return self.getToken(RegisterDescriptionParser.PREFIX, 0)

        def INT(self):
            return self.getToken(RegisterDescriptionParser.INT, 0)

        def getRuleIndex(self):
            return RegisterDescriptionParser.RULE_registerprefix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegisterprefix" ):
                listener.enterRegisterprefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegisterprefix" ):
                listener.exitRegisterprefix(self)




    def registerprefix(self):

        localctx = RegisterDescriptionParser.RegisterprefixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_registerprefix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(RegisterDescriptionParser.PREFIX)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RegisterDescriptionParser.T__0:
                self.state = 62
                self.match(RegisterDescriptionParser.T__0)
                self.state = 63
                self.match(RegisterDescriptionParser.INT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RegisterfunctionlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def registerfunction(self):
            return self.getTypedRuleContext(RegisterDescriptionParser.RegisterfunctionContext,0)


        def registerfunctionwn(self):
            return self.getTypedRuleContext(RegisterDescriptionParser.RegisterfunctionwnContext,0)


        def getRuleIndex(self):
            return RegisterDescriptionParser.RULE_registerfunctionlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegisterfunctionlist" ):
                listener.enterRegisterfunctionlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegisterfunctionlist" ):
                listener.exitRegisterfunctionlist(self)




    def registerfunctionlist(self):

        localctx = RegisterDescriptionParser.RegisterfunctionlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_registerfunctionlist)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RegisterDescriptionParser.FUNCNAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.registerfunction()
                pass
            elif token in [RegisterDescriptionParser.REGWN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.registerfunctionwn()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RegisterfunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCNAME(self):
            return self.getToken(RegisterDescriptionParser.FUNCNAME, 0)

        def getRuleIndex(self):
            return RegisterDescriptionParser.RULE_registerfunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegisterfunction" ):
                listener.enterRegisterfunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegisterfunction" ):
                listener.exitRegisterfunction(self)




    def registerfunction(self):

        localctx = RegisterDescriptionParser.RegisterfunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_registerfunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(RegisterDescriptionParser.FUNCNAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RegisterfunctionwnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REGWN(self):
            return self.getToken(RegisterDescriptionParser.REGWN, 0)

        def INT(self):
            return self.getToken(RegisterDescriptionParser.INT, 0)

        def getRuleIndex(self):
            return RegisterDescriptionParser.RULE_registerfunctionwn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegisterfunctionwn" ):
                listener.enterRegisterfunctionwn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegisterfunctionwn" ):
                listener.exitRegisterfunctionwn(self)




    def registerfunctionwn(self):

        localctx = RegisterDescriptionParser.RegisterfunctionwnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_registerfunctionwn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(RegisterDescriptionParser.REGWN)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RegisterDescriptionParser.T__0:
                self.state = 73
                self.match(RegisterDescriptionParser.T__0)
                self.state = 74
                self.match(RegisterDescriptionParser.INT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RegbankvecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegisterDescriptionParser.RULE_regbankvec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegbankvec" ):
                listener.enterRegbankvec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegbankvec" ):
                listener.exitRegbankvec(self)




    def regbankvec(self):

        localctx = RegisterDescriptionParser.RegbankvecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_regbankvec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RegisterDescriptionParser.T__1:
                self.state = 77
                self.match(RegisterDescriptionParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RegbankContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RegisterDescriptionParser.RULE_regbank

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegbank" ):
                listener.enterRegbank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegbank" ):
                listener.exitRegbank(self)




    def regbank(self):

        localctx = RegisterDescriptionParser.RegbankContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_regbank)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            _la = self._input.LA(1)
            if not(_la==RegisterDescriptionParser.T__2 or _la==RegisterDescriptionParser.T__3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RegisterwidthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(RegisterDescriptionParser.INT, 0)

        def getRuleIndex(self):
            return RegisterDescriptionParser.RULE_registerwidth

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegisterwidth" ):
                listener.enterRegisterwidth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegisterwidth" ):
                listener.exitRegisterwidth(self)




    def registerwidth(self):

        localctx = RegisterDescriptionParser.RegisterwidthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_registerwidth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(RegisterDescriptionParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExtensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(RegisterDescriptionParser.NAME, 0)

        def getRuleIndex(self):
            return RegisterDescriptionParser.RULE_extension

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtension" ):
                listener.enterExtension(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtension" ):
                listener.exitExtension(self)




    def extension(self):

        localctx = RegisterDescriptionParser.ExtensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_extension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(RegisterDescriptionParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





