// Generated from /homelocal/qm280442/HybroGen/HybroLang/HybroLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link HybroLangParser}.
 */
public interface HybroLangListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#compilationunit}.
	 * @param ctx the parse tree
	 */
	void enterCompilationunit(HybroLangParser.CompilationunitContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#compilationunit}.
	 * @param ctx the parse tree
	 */
	void exitCompilationunit(HybroLangParser.CompilationunitContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(HybroLangParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(HybroLangParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#fndcl}.
	 * @param ctx the parse tree
	 */
	void enterFndcl(HybroLangParser.FndclContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#fndcl}.
	 * @param ctx the parse tree
	 */
	void exitFndcl(HybroLangParser.FndclContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#fnprototype}.
	 * @param ctx the parse tree
	 */
	void enterFnprototype(HybroLangParser.FnprototypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#fnprototype}.
	 * @param ctx the parse tree
	 */
	void exitFnprototype(HybroLangParser.FnprototypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#fnbody}.
	 * @param ctx the parse tree
	 */
	void enterFnbody(HybroLangParser.FnbodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#fnbody}.
	 * @param ctx the parse tree
	 */
	void exitFnbody(HybroLangParser.FnbodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#paramdcllist}.
	 * @param ctx the parse tree
	 */
	void enterParamdcllist(HybroLangParser.ParamdcllistContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#paramdcllist}.
	 * @param ctx the parse tree
	 */
	void exitParamdcllist(HybroLangParser.ParamdcllistContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#localvardef}.
	 * @param ctx the parse tree
	 */
	void enterLocalvardef(HybroLangParser.LocalvardefContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#localvardef}.
	 * @param ctx the parse tree
	 */
	void exitLocalvardef(HybroLangParser.LocalvardefContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#vardcllist}.
	 * @param ctx the parse tree
	 */
	void enterVardcllist(HybroLangParser.VardcllistContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#vardcllist}.
	 * @param ctx the parse tree
	 */
	void exitVardcllist(HybroLangParser.VardcllistContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#vardcl}.
	 * @param ctx the parse tree
	 */
	void enterVardcl(HybroLangParser.VardclContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#vardcl}.
	 * @param ctx the parse tree
	 */
	void exitVardcl(HybroLangParser.VardclContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#actionlist}.
	 * @param ctx the parse tree
	 */
	void enterActionlist(HybroLangParser.ActionlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#actionlist}.
	 * @param ctx the parse tree
	 */
	void exitActionlist(HybroLangParser.ActionlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#condexpr}.
	 * @param ctx the parse tree
	 */
	void enterCondexpr(HybroLangParser.CondexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#condexpr}.
	 * @param ctx the parse tree
	 */
	void exitCondexpr(HybroLangParser.CondexprContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#action}.
	 * @param ctx the parse tree
	 */
	void enterAction(HybroLangParser.ActionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#action}.
	 * @param ctx the parse tree
	 */
	void exitAction(HybroLangParser.ActionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#returnexpr}.
	 * @param ctx the parse tree
	 */
	void enterReturnexpr(HybroLangParser.ReturnexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#returnexpr}.
	 * @param ctx the parse tree
	 */
	void exitReturnexpr(HybroLangParser.ReturnexprContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#affectexpr}.
	 * @param ctx the parse tree
	 */
	void enterAffectexpr(HybroLangParser.AffectexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#affectexpr}.
	 * @param ctx the parse tree
	 */
	void exitAffectexpr(HybroLangParser.AffectexprContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#unaryexpr}.
	 * @param ctx the parse tree
	 */
	void enterUnaryexpr(HybroLangParser.UnaryexprContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#unaryexpr}.
	 * @param ctx the parse tree
	 */
	void exitUnaryexpr(HybroLangParser.UnaryexprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code varorvalueArray}
	 * labeled alternative in {@link HybroLangParser#varorvalue}.
	 * @param ctx the parse tree
	 */
	void enterVarorvalueArray(HybroLangParser.VarorvalueArrayContext ctx);
	/**
	 * Exit a parse tree produced by the {@code varorvalueArray}
	 * labeled alternative in {@link HybroLangParser#varorvalue}.
	 * @param ctx the parse tree
	 */
	void exitVarorvalueArray(HybroLangParser.VarorvalueArrayContext ctx);
	/**
	 * Enter a parse tree produced by the {@code varorvalueConst}
	 * labeled alternative in {@link HybroLangParser#varorvalue}.
	 * @param ctx the parse tree
	 */
	void enterVarorvalueConst(HybroLangParser.VarorvalueConstContext ctx);
	/**
	 * Exit a parse tree produced by the {@code varorvalueConst}
	 * labeled alternative in {@link HybroLangParser#varorvalue}.
	 * @param ctx the parse tree
	 */
	void exitVarorvalueConst(HybroLangParser.VarorvalueConstContext ctx);
	/**
	 * Enter a parse tree produced by the {@code varorvalueVar}
	 * labeled alternative in {@link HybroLangParser#varorvalue}.
	 * @param ctx the parse tree
	 */
	void enterVarorvalueVar(HybroLangParser.VarorvalueVarContext ctx);
	/**
	 * Exit a parse tree produced by the {@code varorvalueVar}
	 * labeled alternative in {@link HybroLangParser#varorvalue}.
	 * @param ctx the parse tree
	 */
	void exitVarorvalueVar(HybroLangParser.VarorvalueVarContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#datatype}.
	 * @param ctx the parse tree
	 */
	void enterDatatype(HybroLangParser.DatatypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#datatype}.
	 * @param ctx the parse tree
	 */
	void exitDatatype(HybroLangParser.DatatypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#intconstvalue}.
	 * @param ctx the parse tree
	 */
	void enterIntconstvalue(HybroLangParser.IntconstvalueContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#intconstvalue}.
	 * @param ctx the parse tree
	 */
	void exitIntconstvalue(HybroLangParser.IntconstvalueContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#constvalue}.
	 * @param ctx the parse tree
	 */
	void enterConstvalue(HybroLangParser.ConstvalueContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#constvalue}.
	 * @param ctx the parse tree
	 */
	void exitConstvalue(HybroLangParser.ConstvalueContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#constinline}.
	 * @param ctx the parse tree
	 */
	void enterConstinline(HybroLangParser.ConstinlineContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#constinline}.
	 * @param ctx the parse tree
	 */
	void exitConstinline(HybroLangParser.ConstinlineContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#typebase}.
	 * @param ctx the parse tree
	 */
	void enterTypebase(HybroLangParser.TypebaseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#typebase}.
	 * @param ctx the parse tree
	 */
	void exitTypebase(HybroLangParser.TypebaseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HybroLangParser#condOperator}.
	 * @param ctx the parse tree
	 */
	void enterCondOperator(HybroLangParser.CondOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HybroLangParser#condOperator}.
	 * @param ctx the parse tree
	 */
	void exitCondOperator(HybroLangParser.CondOperatorContext ctx);
}