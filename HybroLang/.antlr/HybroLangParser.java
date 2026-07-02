// Generated from /homelocal/qm280442/HybroGen/HybroLang/HybroLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class HybroLangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		DecimalFloatingConstant=39, IntegerConstant=40, DecimalConstant=41, Name=42, 
		INLINE=43, WhiteSpace=44, LineComment=45, NewLine=46;
	public static final int
		RULE_compilationunit = 0, RULE_function = 1, RULE_fndcl = 2, RULE_fnprototype = 3, 
		RULE_fnbody = 4, RULE_paramdcllist = 5, RULE_localvardef = 6, RULE_vardcllist = 7, 
		RULE_vardcl = 8, RULE_actionlist = 9, RULE_condexpr = 10, RULE_action = 11, 
		RULE_returnexpr = 12, RULE_affectexpr = 13, RULE_unaryexpr = 14, RULE_varorvalue = 15, 
		RULE_datatype = 16, RULE_intconstvalue = 17, RULE_constvalue = 18, RULE_constinline = 19, 
		RULE_typebase = 20, RULE_condOperator = 21;
	private static String[] makeRuleNames() {
		return new String[] {
			"compilationunit", "function", "fndcl", "fnprototype", "fnbody", "paramdcllist", 
			"localvardef", "vardcllist", "vardcl", "actionlist", "condexpr", "action", 
			"returnexpr", "affectexpr", "unaryexpr", "varorvalue", "datatype", "intconstvalue", 
			"constvalue", "constinline", "typebase", "condOperator"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "','", "';'", "'for'", "'if'", "'else'", 
			"'return'", "'='", "'['", "']'", "'*'", "'/'", "'+'", "'-'", "'<<'", 
			"'>>'", "'&'", "'|'", "'^'", "'int'", "'uint'", "'sint'", "'suint'", 
			"'flt'", "'cpl'", "'pix'", "'ipv4'", "'ipv6'", "'[]'", "'=='", "'!='", 
			"'<'", "'>'", "'<='", "'>='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "DecimalFloatingConstant", "IntegerConstant", "DecimalConstant", 
			"Name", "INLINE", "WhiteSpace", "LineComment", "NewLine"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "HybroLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public HybroLangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CompilationunitContext extends ParserRuleContext {
		public List<FunctionContext> function() {
			return getRuleContexts(FunctionContext.class);
		}
		public FunctionContext function(int i) {
			return getRuleContext(FunctionContext.class,i);
		}
		public CompilationunitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compilationunit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterCompilationunit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitCompilationunit(this);
		}
	}

	public final CompilationunitContext compilationunit() throws RecognitionException {
		CompilationunitContext _localctx = new CompilationunitContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_compilationunit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(44);
				function();
				}
				}
				setState(47); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 4286578688L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionContext extends ParserRuleContext {
		public FndclContext fndcl() {
			return getRuleContext(FndclContext.class,0);
		}
		public FnbodyContext fnbody() {
			return getRuleContext(FnbodyContext.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterFunction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitFunction(this);
		}
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_function);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(49);
			fndcl();
			setState(50);
			fnbody();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FndclContext extends ParserRuleContext {
		public DatatypeContext datatype() {
			return getRuleContext(DatatypeContext.class,0);
		}
		public TerminalNode Name() { return getToken(HybroLangParser.Name, 0); }
		public FnprototypeContext fnprototype() {
			return getRuleContext(FnprototypeContext.class,0);
		}
		public FndclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fndcl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterFndcl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitFndcl(this);
		}
	}

	public final FndclContext fndcl() throws RecognitionException {
		FndclContext _localctx = new FndclContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_fndcl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			datatype();
			setState(53);
			match(Name);
			setState(54);
			fnprototype();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FnprototypeContext extends ParserRuleContext {
		public ParamdcllistContext paramdcllist() {
			return getRuleContext(ParamdcllistContext.class,0);
		}
		public FnprototypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fnprototype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterFnprototype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitFnprototype(this);
		}
	}

	public final FnprototypeContext fnprototype() throws RecognitionException {
		FnprototypeContext _localctx = new FnprototypeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_fnprototype);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			match(T__0);
			setState(57);
			paramdcllist();
			setState(58);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FnbodyContext extends ParserRuleContext {
		public ActionlistContext actionlist() {
			return getRuleContext(ActionlistContext.class,0);
		}
		public List<LocalvardefContext> localvardef() {
			return getRuleContexts(LocalvardefContext.class);
		}
		public LocalvardefContext localvardef(int i) {
			return getRuleContext(LocalvardefContext.class,i);
		}
		public ReturnexprContext returnexpr() {
			return getRuleContext(ReturnexprContext.class,0);
		}
		public FnbodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fnbody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterFnbody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitFnbody(this);
		}
	}

	public final FnbodyContext fnbody() throws RecognitionException {
		FnbodyContext _localctx = new FnbodyContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_fnbody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(T__2);
			setState(64);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4286578688L) != 0)) {
				{
				{
				setState(61);
				localvardef();
				}
				}
				setState(66);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(67);
			actionlist();
			setState(69);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__9) {
				{
				setState(68);
				returnexpr();
				}
			}

			setState(71);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamdcllistContext extends ParserRuleContext {
		public List<VardclContext> vardcl() {
			return getRuleContexts(VardclContext.class);
		}
		public VardclContext vardcl(int i) {
			return getRuleContext(VardclContext.class,i);
		}
		public ParamdcllistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramdcllist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterParamdcllist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitParamdcllist(this);
		}
	}

	public final ParamdcllistContext paramdcllist() throws RecognitionException {
		ParamdcllistContext _localctx = new ParamdcllistContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_paramdcllist);
		int _la;
		try {
			setState(82);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__22:
			case T__23:
			case T__24:
			case T__25:
			case T__26:
			case T__27:
			case T__28:
			case T__29:
			case T__30:
				enterOuterAlt(_localctx, 1);
				{
				setState(73);
				vardcl();
				setState(78);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__4) {
					{
					{
					setState(74);
					match(T__4);
					setState(75);
					vardcl();
					}
					}
					setState(80);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case T__1:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LocalvardefContext extends ParserRuleContext {
		public VardcllistContext vardcllist() {
			return getRuleContext(VardcllistContext.class,0);
		}
		public LocalvardefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_localvardef; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterLocalvardef(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitLocalvardef(this);
		}
	}

	public final LocalvardefContext localvardef() throws RecognitionException {
		LocalvardefContext _localctx = new LocalvardefContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_localvardef);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			vardcllist();
			setState(85);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VardcllistContext extends ParserRuleContext {
		public VardclContext vardcl() {
			return getRuleContext(VardclContext.class,0);
		}
		public List<TerminalNode> Name() { return getTokens(HybroLangParser.Name); }
		public TerminalNode Name(int i) {
			return getToken(HybroLangParser.Name, i);
		}
		public VardcllistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardcllist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterVardcllist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitVardcllist(this);
		}
	}

	public final VardcllistContext vardcllist() throws RecognitionException {
		VardcllistContext _localctx = new VardcllistContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_vardcllist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			vardcl();
			setState(92);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__4) {
				{
				{
				setState(88);
				match(T__4);
				setState(89);
				match(Name);
				}
				}
				setState(94);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VardclContext extends ParserRuleContext {
		public DatatypeContext datatype() {
			return getRuleContext(DatatypeContext.class,0);
		}
		public TerminalNode Name() { return getToken(HybroLangParser.Name, 0); }
		public VardclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardcl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterVardcl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitVardcl(this);
		}
	}

	public final VardclContext vardcl() throws RecognitionException {
		VardclContext _localctx = new VardclContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_vardcl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			datatype();
			setState(96);
			match(Name);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ActionlistContext extends ParserRuleContext {
		public List<ActionContext> action() {
			return getRuleContexts(ActionContext.class);
		}
		public ActionContext action(int i) {
			return getRuleContext(ActionContext.class,i);
		}
		public ActionlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_actionlist; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterActionlist(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitActionlist(this);
		}
	}

	public final ActionlistContext actionlist() throws RecognitionException {
		ActionlistContext _localctx = new ActionlistContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_actionlist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4398046511488L) != 0)) {
				{
				{
				setState(98);
				action();
				}
				}
				setState(103);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondexprContext extends ParserRuleContext {
		public List<VarorvalueContext> varorvalue() {
			return getRuleContexts(VarorvalueContext.class);
		}
		public VarorvalueContext varorvalue(int i) {
			return getRuleContext(VarorvalueContext.class,i);
		}
		public CondOperatorContext condOperator() {
			return getRuleContext(CondOperatorContext.class,0);
		}
		public CondexprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condexpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterCondexpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitCondexpr(this);
		}
	}

	public final CondexprContext condexpr() throws RecognitionException {
		CondexprContext _localctx = new CondexprContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_condexpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			varorvalue();
			setState(105);
			condOperator();
			setState(106);
			varorvalue();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ActionContext extends ParserRuleContext {
		public List<AffectexprContext> affectexpr() {
			return getRuleContexts(AffectexprContext.class);
		}
		public AffectexprContext affectexpr(int i) {
			return getRuleContext(AffectexprContext.class,i);
		}
		public CondexprContext condexpr() {
			return getRuleContext(CondexprContext.class,0);
		}
		public List<ActionlistContext> actionlist() {
			return getRuleContexts(ActionlistContext.class);
		}
		public ActionlistContext actionlist(int i) {
			return getRuleContext(ActionlistContext.class,i);
		}
		public ActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_action; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterAction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitAction(this);
		}
	}

	public final ActionContext action() throws RecognitionException {
		ActionContext _localctx = new ActionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_action);
		try {
			setState(135);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Name:
				enterOuterAlt(_localctx, 1);
				{
				setState(108);
				affectexpr();
				setState(109);
				match(T__5);
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 2);
				{
				setState(111);
				match(T__6);
				setState(112);
				match(T__0);
				setState(113);
				affectexpr();
				setState(114);
				match(T__5);
				setState(115);
				condexpr();
				setState(116);
				match(T__5);
				setState(117);
				affectexpr();
				setState(118);
				match(T__1);
				setState(119);
				match(T__2);
				setState(120);
				actionlist();
				setState(121);
				match(T__3);
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 3);
				{
				setState(123);
				match(T__7);
				setState(124);
				match(T__0);
				setState(125);
				condexpr();
				setState(126);
				match(T__1);
				setState(127);
				match(T__2);
				setState(128);
				actionlist();
				setState(129);
				match(T__3);
				setState(130);
				match(T__8);
				setState(131);
				match(T__2);
				setState(132);
				actionlist();
				setState(133);
				match(T__3);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnexprContext extends ParserRuleContext {
		public UnaryexprContext unaryexpr() {
			return getRuleContext(UnaryexprContext.class,0);
		}
		public ReturnexprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnexpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterReturnexpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitReturnexpr(this);
		}
	}

	public final ReturnexprContext returnexpr() throws RecognitionException {
		ReturnexprContext _localctx = new ReturnexprContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_returnexpr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			match(T__9);
			setState(138);
			unaryexpr(0);
			setState(139);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AffectexprContext extends ParserRuleContext {
		public TerminalNode Name() { return getToken(HybroLangParser.Name, 0); }
		public List<UnaryexprContext> unaryexpr() {
			return getRuleContexts(UnaryexprContext.class);
		}
		public UnaryexprContext unaryexpr(int i) {
			return getRuleContext(UnaryexprContext.class,i);
		}
		public AffectexprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_affectexpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterAffectexpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitAffectexpr(this);
		}
	}

	public final AffectexprContext affectexpr() throws RecognitionException {
		AffectexprContext _localctx = new AffectexprContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_affectexpr);
		try {
			setState(151);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(141);
				match(Name);
				setState(142);
				match(T__10);
				setState(143);
				unaryexpr(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(144);
				match(Name);
				setState(145);
				match(T__11);
				setState(146);
				unaryexpr(0);
				setState(147);
				match(T__12);
				setState(148);
				match(T__10);
				setState(149);
				unaryexpr(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnaryexprContext extends ParserRuleContext {
		public Token op;
		public VarorvalueContext varorvalue() {
			return getRuleContext(VarorvalueContext.class,0);
		}
		public List<UnaryexprContext> unaryexpr() {
			return getRuleContexts(UnaryexprContext.class);
		}
		public UnaryexprContext unaryexpr(int i) {
			return getRuleContext(UnaryexprContext.class,i);
		}
		public UnaryexprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryexpr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterUnaryexpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitUnaryexpr(this);
		}
	}

	public final UnaryexprContext unaryexpr() throws RecognitionException {
		return unaryexpr(0);
	}

	private UnaryexprContext unaryexpr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		UnaryexprContext _localctx = new UnaryexprContext(_ctx, _parentState);
		UnaryexprContext _prevctx = _localctx;
		int _startState = 28;
		enterRecursionRule(_localctx, 28, RULE_unaryexpr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(154);
			varorvalue();
			}
			_ctx.stop = _input.LT(-1);
			setState(170);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(168);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
					case 1:
						{
						_localctx = new UnaryexprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_unaryexpr);
						setState(156);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(157);
						((UnaryexprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__13 || _la==T__14) ) {
							((UnaryexprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(158);
						unaryexpr(6);
						}
						break;
					case 2:
						{
						_localctx = new UnaryexprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_unaryexpr);
						setState(159);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(160);
						((UnaryexprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__15 || _la==T__16) ) {
							((UnaryexprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(161);
						unaryexpr(5);
						}
						break;
					case 3:
						{
						_localctx = new UnaryexprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_unaryexpr);
						setState(162);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(163);
						((UnaryexprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==T__17 || _la==T__18) ) {
							((UnaryexprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(164);
						unaryexpr(4);
						}
						break;
					case 4:
						{
						_localctx = new UnaryexprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_unaryexpr);
						setState(165);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(166);
						((UnaryexprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7340032L) != 0)) ) {
							((UnaryexprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(167);
						unaryexpr(3);
						}
						break;
					}
					} 
				}
				setState(172);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarorvalueContext extends ParserRuleContext {
		public VarorvalueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varorvalue; }
	 
		public VarorvalueContext() { }
		public void copyFrom(VarorvalueContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VarorvalueVarContext extends VarorvalueContext {
		public TerminalNode Name() { return getToken(HybroLangParser.Name, 0); }
		public VarorvalueVarContext(VarorvalueContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterVarorvalueVar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitVarorvalueVar(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VarorvalueArrayContext extends VarorvalueContext {
		public TerminalNode Name() { return getToken(HybroLangParser.Name, 0); }
		public UnaryexprContext unaryexpr() {
			return getRuleContext(UnaryexprContext.class,0);
		}
		public VarorvalueArrayContext(VarorvalueContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterVarorvalueArray(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitVarorvalueArray(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VarorvalueConstContext extends VarorvalueContext {
		public ConstvalueContext constvalue() {
			return getRuleContext(ConstvalueContext.class,0);
		}
		public VarorvalueConstContext(VarorvalueContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterVarorvalueConst(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitVarorvalueConst(this);
		}
	}

	public final VarorvalueContext varorvalue() throws RecognitionException {
		VarorvalueContext _localctx = new VarorvalueContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_varorvalue);
		try {
			setState(180);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				_localctx = new VarorvalueArrayContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(173);
				match(Name);
				setState(174);
				match(T__11);
				setState(175);
				unaryexpr(0);
				setState(176);
				match(T__12);
				}
				break;
			case 2:
				_localctx = new VarorvalueConstContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(178);
				constvalue();
				}
				break;
			case 3:
				_localctx = new VarorvalueVarContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(179);
				match(Name);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DatatypeContext extends ParserRuleContext {
		public IntconstvalueContext wordlen;
		public IntconstvalueContext vectorlen;
		public TypebaseContext typebase() {
			return getRuleContext(TypebaseContext.class,0);
		}
		public List<IntconstvalueContext> intconstvalue() {
			return getRuleContexts(IntconstvalueContext.class);
		}
		public IntconstvalueContext intconstvalue(int i) {
			return getRuleContext(IntconstvalueContext.class,i);
		}
		public DatatypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_datatype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterDatatype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitDatatype(this);
		}
	}

	public final DatatypeContext datatype() throws RecognitionException {
		DatatypeContext _localctx = new DatatypeContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_datatype);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			typebase();
			setState(183);
			((DatatypeContext)_localctx).wordlen = intconstvalue();
			setState(184);
			((DatatypeContext)_localctx).vectorlen = intconstvalue();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IntconstvalueContext extends ParserRuleContext {
		public TerminalNode IntegerConstant() { return getToken(HybroLangParser.IntegerConstant, 0); }
		public ConstinlineContext constinline() {
			return getRuleContext(ConstinlineContext.class,0);
		}
		public IntconstvalueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_intconstvalue; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterIntconstvalue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitIntconstvalue(this);
		}
	}

	public final IntconstvalueContext intconstvalue() throws RecognitionException {
		IntconstvalueContext _localctx = new IntconstvalueContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_intconstvalue);
		try {
			setState(188);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IntegerConstant:
				enterOuterAlt(_localctx, 1);
				{
				setState(186);
				match(IntegerConstant);
				}
				break;
			case INLINE:
				enterOuterAlt(_localctx, 2);
				{
				setState(187);
				constinline();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstvalueContext extends ParserRuleContext {
		public TerminalNode IntegerConstant() { return getToken(HybroLangParser.IntegerConstant, 0); }
		public TerminalNode DecimalFloatingConstant() { return getToken(HybroLangParser.DecimalFloatingConstant, 0); }
		public ConstinlineContext constinline() {
			return getRuleContext(ConstinlineContext.class,0);
		}
		public ConstvalueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constvalue; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterConstvalue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitConstvalue(this);
		}
	}

	public final ConstvalueContext constvalue() throws RecognitionException {
		ConstvalueContext _localctx = new ConstvalueContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_constvalue);
		try {
			setState(193);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IntegerConstant:
				enterOuterAlt(_localctx, 1);
				{
				setState(190);
				match(IntegerConstant);
				}
				break;
			case DecimalFloatingConstant:
				enterOuterAlt(_localctx, 2);
				{
				setState(191);
				match(DecimalFloatingConstant);
				}
				break;
			case INLINE:
				enterOuterAlt(_localctx, 3);
				{
				setState(192);
				constinline();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConstinlineContext extends ParserRuleContext {
		public TerminalNode INLINE() { return getToken(HybroLangParser.INLINE, 0); }
		public ConstinlineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constinline; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterConstinline(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitConstinline(this);
		}
	}

	public final ConstinlineContext constinline() throws RecognitionException {
		ConstinlineContext _localctx = new ConstinlineContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_constinline);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(195);
			match(INLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypebaseContext extends ParserRuleContext {
		public TypebaseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typebase; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterTypebase(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitTypebase(this);
		}
	}

	public final TypebaseContext typebase() throws RecognitionException {
		TypebaseContext _localctx = new TypebaseContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_typebase);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(197);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4286578688L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(199);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__31) {
				{
				setState(198);
				match(T__31);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondOperatorContext extends ParserRuleContext {
		public CondOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).enterCondOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HybroLangListener ) ((HybroLangListener)listener).exitCondOperator(this);
		}
	}

	public final CondOperatorContext condOperator() throws RecognitionException {
		CondOperatorContext _localctx = new CondOperatorContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_condOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 541165879296L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 14:
			return unaryexpr_sempred((UnaryexprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean unaryexpr_sempred(UnaryexprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		case 2:
			return precpred(_ctx, 3);
		case 3:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001.\u00cc\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0001\u0000\u0004\u0000.\b\u0000\u000b\u0000\f\u0000/\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0005"+
		"\u0004?\b\u0004\n\u0004\f\u0004B\t\u0004\u0001\u0004\u0001\u0004\u0003"+
		"\u0004F\b\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0005\u0005M\b\u0005\n\u0005\f\u0005P\t\u0005\u0001\u0005\u0003"+
		"\u0005S\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0005\u0007[\b\u0007\n\u0007\f\u0007^\t\u0007\u0001"+
		"\b\u0001\b\u0001\b\u0001\t\u0005\td\b\t\n\t\f\tg\t\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u0088\b\u000b"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u0098\b\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0005\u000e\u00a9\b\u000e\n\u000e\f\u000e\u00ac"+
		"\t\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0003\u000f\u00b5\b\u000f\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0003\u0011\u00bd\b\u0011\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u00c2\b\u0012\u0001\u0013\u0001"+
		"\u0013\u0001\u0014\u0001\u0014\u0003\u0014\u00c8\b\u0014\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0000\u0001\u001c\u0016\u0000\u0002\u0004\u0006\b\n"+
		"\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*\u0000"+
		"\u0006\u0001\u0000\u000e\u000f\u0001\u0000\u0010\u0011\u0001\u0000\u0012"+
		"\u0013\u0001\u0000\u0014\u0016\u0001\u0000\u0017\u001f\u0001\u0000!&\u00c9"+
		"\u0000-\u0001\u0000\u0000\u0000\u00021\u0001\u0000\u0000\u0000\u00044"+
		"\u0001\u0000\u0000\u0000\u00068\u0001\u0000\u0000\u0000\b<\u0001\u0000"+
		"\u0000\u0000\nR\u0001\u0000\u0000\u0000\fT\u0001\u0000\u0000\u0000\u000e"+
		"W\u0001\u0000\u0000\u0000\u0010_\u0001\u0000\u0000\u0000\u0012e\u0001"+
		"\u0000\u0000\u0000\u0014h\u0001\u0000\u0000\u0000\u0016\u0087\u0001\u0000"+
		"\u0000\u0000\u0018\u0089\u0001\u0000\u0000\u0000\u001a\u0097\u0001\u0000"+
		"\u0000\u0000\u001c\u0099\u0001\u0000\u0000\u0000\u001e\u00b4\u0001\u0000"+
		"\u0000\u0000 \u00b6\u0001\u0000\u0000\u0000\"\u00bc\u0001\u0000\u0000"+
		"\u0000$\u00c1\u0001\u0000\u0000\u0000&\u00c3\u0001\u0000\u0000\u0000("+
		"\u00c5\u0001\u0000\u0000\u0000*\u00c9\u0001\u0000\u0000\u0000,.\u0003"+
		"\u0002\u0001\u0000-,\u0001\u0000\u0000\u0000./\u0001\u0000\u0000\u0000"+
		"/-\u0001\u0000\u0000\u0000/0\u0001\u0000\u0000\u00000\u0001\u0001\u0000"+
		"\u0000\u000012\u0003\u0004\u0002\u000023\u0003\b\u0004\u00003\u0003\u0001"+
		"\u0000\u0000\u000045\u0003 \u0010\u000056\u0005*\u0000\u000067\u0003\u0006"+
		"\u0003\u00007\u0005\u0001\u0000\u0000\u000089\u0005\u0001\u0000\u0000"+
		"9:\u0003\n\u0005\u0000:;\u0005\u0002\u0000\u0000;\u0007\u0001\u0000\u0000"+
		"\u0000<@\u0005\u0003\u0000\u0000=?\u0003\f\u0006\u0000>=\u0001\u0000\u0000"+
		"\u0000?B\u0001\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000@A\u0001\u0000"+
		"\u0000\u0000AC\u0001\u0000\u0000\u0000B@\u0001\u0000\u0000\u0000CE\u0003"+
		"\u0012\t\u0000DF\u0003\u0018\f\u0000ED\u0001\u0000\u0000\u0000EF\u0001"+
		"\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000GH\u0005\u0004\u0000\u0000"+
		"H\t\u0001\u0000\u0000\u0000IN\u0003\u0010\b\u0000JK\u0005\u0005\u0000"+
		"\u0000KM\u0003\u0010\b\u0000LJ\u0001\u0000\u0000\u0000MP\u0001\u0000\u0000"+
		"\u0000NL\u0001\u0000\u0000\u0000NO\u0001\u0000\u0000\u0000OS\u0001\u0000"+
		"\u0000\u0000PN\u0001\u0000\u0000\u0000QS\u0001\u0000\u0000\u0000RI\u0001"+
		"\u0000\u0000\u0000RQ\u0001\u0000\u0000\u0000S\u000b\u0001\u0000\u0000"+
		"\u0000TU\u0003\u000e\u0007\u0000UV\u0005\u0006\u0000\u0000V\r\u0001\u0000"+
		"\u0000\u0000W\\\u0003\u0010\b\u0000XY\u0005\u0005\u0000\u0000Y[\u0005"+
		"*\u0000\u0000ZX\u0001\u0000\u0000\u0000[^\u0001\u0000\u0000\u0000\\Z\u0001"+
		"\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]\u000f\u0001\u0000\u0000"+
		"\u0000^\\\u0001\u0000\u0000\u0000_`\u0003 \u0010\u0000`a\u0005*\u0000"+
		"\u0000a\u0011\u0001\u0000\u0000\u0000bd\u0003\u0016\u000b\u0000cb\u0001"+
		"\u0000\u0000\u0000dg\u0001\u0000\u0000\u0000ec\u0001\u0000\u0000\u0000"+
		"ef\u0001\u0000\u0000\u0000f\u0013\u0001\u0000\u0000\u0000ge\u0001\u0000"+
		"\u0000\u0000hi\u0003\u001e\u000f\u0000ij\u0003*\u0015\u0000jk\u0003\u001e"+
		"\u000f\u0000k\u0015\u0001\u0000\u0000\u0000lm\u0003\u001a\r\u0000mn\u0005"+
		"\u0006\u0000\u0000n\u0088\u0001\u0000\u0000\u0000op\u0005\u0007\u0000"+
		"\u0000pq\u0005\u0001\u0000\u0000qr\u0003\u001a\r\u0000rs\u0005\u0006\u0000"+
		"\u0000st\u0003\u0014\n\u0000tu\u0005\u0006\u0000\u0000uv\u0003\u001a\r"+
		"\u0000vw\u0005\u0002\u0000\u0000wx\u0005\u0003\u0000\u0000xy\u0003\u0012"+
		"\t\u0000yz\u0005\u0004\u0000\u0000z\u0088\u0001\u0000\u0000\u0000{|\u0005"+
		"\b\u0000\u0000|}\u0005\u0001\u0000\u0000}~\u0003\u0014\n\u0000~\u007f"+
		"\u0005\u0002\u0000\u0000\u007f\u0080\u0005\u0003\u0000\u0000\u0080\u0081"+
		"\u0003\u0012\t\u0000\u0081\u0082\u0005\u0004\u0000\u0000\u0082\u0083\u0005"+
		"\t\u0000\u0000\u0083\u0084\u0005\u0003\u0000\u0000\u0084\u0085\u0003\u0012"+
		"\t\u0000\u0085\u0086\u0005\u0004\u0000\u0000\u0086\u0088\u0001\u0000\u0000"+
		"\u0000\u0087l\u0001\u0000\u0000\u0000\u0087o\u0001\u0000\u0000\u0000\u0087"+
		"{\u0001\u0000\u0000\u0000\u0088\u0017\u0001\u0000\u0000\u0000\u0089\u008a"+
		"\u0005\n\u0000\u0000\u008a\u008b\u0003\u001c\u000e\u0000\u008b\u008c\u0005"+
		"\u0006\u0000\u0000\u008c\u0019\u0001\u0000\u0000\u0000\u008d\u008e\u0005"+
		"*\u0000\u0000\u008e\u008f\u0005\u000b\u0000\u0000\u008f\u0098\u0003\u001c"+
		"\u000e\u0000\u0090\u0091\u0005*\u0000\u0000\u0091\u0092\u0005\f\u0000"+
		"\u0000\u0092\u0093\u0003\u001c\u000e\u0000\u0093\u0094\u0005\r\u0000\u0000"+
		"\u0094\u0095\u0005\u000b\u0000\u0000\u0095\u0096\u0003\u001c\u000e\u0000"+
		"\u0096\u0098\u0001\u0000\u0000\u0000\u0097\u008d\u0001\u0000\u0000\u0000"+
		"\u0097\u0090\u0001\u0000\u0000\u0000\u0098\u001b\u0001\u0000\u0000\u0000"+
		"\u0099\u009a\u0006\u000e\uffff\uffff\u0000\u009a\u009b\u0003\u001e\u000f"+
		"\u0000\u009b\u00aa\u0001\u0000\u0000\u0000\u009c\u009d\n\u0005\u0000\u0000"+
		"\u009d\u009e\u0007\u0000\u0000\u0000\u009e\u00a9\u0003\u001c\u000e\u0006"+
		"\u009f\u00a0\n\u0004\u0000\u0000\u00a0\u00a1\u0007\u0001\u0000\u0000\u00a1"+
		"\u00a9\u0003\u001c\u000e\u0005\u00a2\u00a3\n\u0003\u0000\u0000\u00a3\u00a4"+
		"\u0007\u0002\u0000\u0000\u00a4\u00a9\u0003\u001c\u000e\u0004\u00a5\u00a6"+
		"\n\u0002\u0000\u0000\u00a6\u00a7\u0007\u0003\u0000\u0000\u00a7\u00a9\u0003"+
		"\u001c\u000e\u0003\u00a8\u009c\u0001\u0000\u0000\u0000\u00a8\u009f\u0001"+
		"\u0000\u0000\u0000\u00a8\u00a2\u0001\u0000\u0000\u0000\u00a8\u00a5\u0001"+
		"\u0000\u0000\u0000\u00a9\u00ac\u0001\u0000\u0000\u0000\u00aa\u00a8\u0001"+
		"\u0000\u0000\u0000\u00aa\u00ab\u0001\u0000\u0000\u0000\u00ab\u001d\u0001"+
		"\u0000\u0000\u0000\u00ac\u00aa\u0001\u0000\u0000\u0000\u00ad\u00ae\u0005"+
		"*\u0000\u0000\u00ae\u00af\u0005\f\u0000\u0000\u00af\u00b0\u0003\u001c"+
		"\u000e\u0000\u00b0\u00b1\u0005\r\u0000\u0000\u00b1\u00b5\u0001\u0000\u0000"+
		"\u0000\u00b2\u00b5\u0003$\u0012\u0000\u00b3\u00b5\u0005*\u0000\u0000\u00b4"+
		"\u00ad\u0001\u0000\u0000\u0000\u00b4\u00b2\u0001\u0000\u0000\u0000\u00b4"+
		"\u00b3\u0001\u0000\u0000\u0000\u00b5\u001f\u0001\u0000\u0000\u0000\u00b6"+
		"\u00b7\u0003(\u0014\u0000\u00b7\u00b8\u0003\"\u0011\u0000\u00b8\u00b9"+
		"\u0003\"\u0011\u0000\u00b9!\u0001\u0000\u0000\u0000\u00ba\u00bd\u0005"+
		"(\u0000\u0000\u00bb\u00bd\u0003&\u0013\u0000\u00bc\u00ba\u0001\u0000\u0000"+
		"\u0000\u00bc\u00bb\u0001\u0000\u0000\u0000\u00bd#\u0001\u0000\u0000\u0000"+
		"\u00be\u00c2\u0005(\u0000\u0000\u00bf\u00c2\u0005\'\u0000\u0000\u00c0"+
		"\u00c2\u0003&\u0013\u0000\u00c1\u00be\u0001\u0000\u0000\u0000\u00c1\u00bf"+
		"\u0001\u0000\u0000\u0000\u00c1\u00c0\u0001\u0000\u0000\u0000\u00c2%\u0001"+
		"\u0000\u0000\u0000\u00c3\u00c4\u0005+\u0000\u0000\u00c4\'\u0001\u0000"+
		"\u0000\u0000\u00c5\u00c7\u0007\u0004\u0000\u0000\u00c6\u00c8\u0005 \u0000"+
		"\u0000\u00c7\u00c6\u0001\u0000\u0000\u0000\u00c7\u00c8\u0001\u0000\u0000"+
		"\u0000\u00c8)\u0001\u0000\u0000\u0000\u00c9\u00ca\u0007\u0005\u0000\u0000"+
		"\u00ca+\u0001\u0000\u0000\u0000\u000f/@ENR\\e\u0087\u0097\u00a8\u00aa"+
		"\u00b4\u00bc\u00c1\u00c7";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}