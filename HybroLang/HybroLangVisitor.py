# Generated from HybroLang.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HybroLangParser import HybroLangParser
else:
    from HybroLangParser import HybroLangParser

# This class defines a complete generic visitor for a parse tree produced by HybroLangParser.

class HybroLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HybroLangParser#compilationunit.
    def visitCompilationunit(self, ctx:HybroLangParser.CompilationunitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#function.
    def visitFunction(self, ctx:HybroLangParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#fndcl.
    def visitFndcl(self, ctx:HybroLangParser.FndclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#fnprototype.
    def visitFnprototype(self, ctx:HybroLangParser.FnprototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#fnbody.
    def visitFnbody(self, ctx:HybroLangParser.FnbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#paramdcllist.
    def visitParamdcllist(self, ctx:HybroLangParser.ParamdcllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#localvardef.
    def visitLocalvardef(self, ctx:HybroLangParser.LocalvardefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#vardcllist.
    def visitVardcllist(self, ctx:HybroLangParser.VardcllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#vardcl.
    def visitVardcl(self, ctx:HybroLangParser.VardclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#actionlist.
    def visitActionlist(self, ctx:HybroLangParser.ActionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#condexpr.
    def visitCondexpr(self, ctx:HybroLangParser.CondexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#action.
    def visitAction(self, ctx:HybroLangParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#returnexpr.
    def visitReturnexpr(self, ctx:HybroLangParser.ReturnexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#affectexpr.
    def visitAffectexpr(self, ctx:HybroLangParser.AffectexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#unaryexpr.
    def visitUnaryexpr(self, ctx:HybroLangParser.UnaryexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#varorvalueArray.
    def visitVarorvalueArray(self, ctx:HybroLangParser.VarorvalueArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#varorvalueConst.
    def visitVarorvalueConst(self, ctx:HybroLangParser.VarorvalueConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#varorvalueVar.
    def visitVarorvalueVar(self, ctx:HybroLangParser.VarorvalueVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#datatype.
    def visitDatatype(self, ctx:HybroLangParser.DatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#intconstvalue.
    def visitIntconstvalue(self, ctx:HybroLangParser.IntconstvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#constvalue.
    def visitConstvalue(self, ctx:HybroLangParser.ConstvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#constinline.
    def visitConstinline(self, ctx:HybroLangParser.ConstinlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#typebase.
    def visitTypebase(self, ctx:HybroLangParser.TypebaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HybroLangParser#condOperator.
    def visitCondOperator(self, ctx:HybroLangParser.CondOperatorContext):
        return self.visitChildren(ctx)



del HybroLangParser