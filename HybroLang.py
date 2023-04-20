#!/usr/bin/env python3

import antlr4
from antlr4 import *
from HybroLang.HybroLangLexer    import HybroLangLexer
from HybroLang.HybroLangParser   import HybroLangParser
from HybroLang.HybroLangVisitor  import HybroLangVisitor
from HybroLang.H2RegisterBank    import H2RegisterBank, regCorrespondances
from HybroLang.H2SymbolTable     import H2SymbolTable
from HybroLang.H2LabelTable      import H2LabelTable
from HybroLang.H2IR2             import *
from HybroGen.GenGeneratorFromDb import GenGeneratorFromDb

H2_RELEASE = "v3.0"

class HybrogenTreeCompiler(HybroLangVisitor):

    def __init__(self, inputCompilette, platform, verbose, debug, dbIds):
        self.platform = platform
        self.archMaster = self.platform["arch"][0]
        self.abi = self.platform["abi"]
        self.tab = 0
        self.verbose = verbose
        self.debug = debug
        self.Trace()
        self.dbIds = dbIds
        archMaster = platform["arch"][0]
        extList = platform["extension"][0]
        abi = platform["abi"]
        self.gen = GenGeneratorFromDb (archMaster, extList[0], abi, dbIds, verbose, debug)         # Connect to backend only for master architecture
        self.printIfVerbose ("HybrogenVisitor for %s Verbose : %s Debug : %s"%(archList, verbose, debug))
        if self.verbose:
            print ("HybrogenVisitor for %s Verbose : %s Debug : %s"%(archList, verbose, debug))

        l = HybroLangLexer(antlr4.InputStream(inputCompilette)) # Initialize ANTLR lexer, tokenizer, parse, tree
        s = CommonTokenStream(l)
        p = HybroLangParser(s)
        syntaxTree = p.compilationunit()
        self.tree = self.visit(syntaxTree)                         # Visit syntax tree & build IR

    def gatherOpsAndTypes(self):
        return self.IR.gatherOpsAndTypes()

    def getTree(self):
        cCode = self.IR.generateCodeGeneration (self.sTable, self.regTmp, self.lTable, self.regIn)
        return cCode

    def printIfVerbose (self, msg):
        if self.verbose:
            print (msg, file=sys.stderr)

    def Trace(self):
        fname = sys._getframe(1).f_code.co_name
        self.printIfVerbose ("\t"*self.tab + fname)

    def visitFndcl(self, ctx:HybroLangParser.FndclContext):
        self.Trace()
        self.tab += 1
        returnType = self.visit (ctx.datatype())
        functionName = ctx.Name().getText()
        self.visit (ctx.fnprototype())
        regOutput = self.regOut.getNextRegister(returnType["arith"])
        varType = H2Type(returnType["arith"], returnType["wordLen"], returnType["vectorLen"])
        self.sTable.add("h2_outputVarName", varType, regOutput)
        self.tab -= 1

    def visitLocalvardef(self, ctx:HybroLangParser.LocalvardefContext):
        self.Trace()
        self.regCurrent = self.regTmp
        self.tab += 1
        self.visit (ctx.vardcllist())
        self.tab -= 1

    def visitDatatype(self, ctx:HybroLangParser.DatatypeContext):
        self.Trace()
        a = self.removeDieze (ctx.typebase().getText())
        w = self.removeDieze (ctx.wordlen.getText())
        l = self.removeDieze (ctx.vectorlen.getText())
        h = H2Type (a, w, l)
        return h

    def visitFunction(self, ctx:HybroLangParser.FunctionContext):
        self.Trace()
        self.tab += 1
        archMaster = self.platform["arch"][0]
        self.sTable = H2SymbolTable(self.archMaster)   	# Initialize symbol table & register
        self.lTable = H2LabelTable(self.archMaster)   	#
        self.IR = H2IR2(self.platform, self.sTable, self.verbose, self.dbIds)
        regin, regout, regtmp = self.gen.getRegisterIOT("f")
        self.regIn  = H2RegisterBank("In",  "flt", regin, verbose=self.verbose)
        self.regOut = H2RegisterBank("Out", "flt", regout, verbose=self.verbose)
        self.regTmp = H2RegisterBank("Tmp", "flt", regtmp, verbose=self.verbose)
        regin, regout, regtmp = self.gen.getRegisterIOT("i")
        self.regIn.add("int", regin)
        self.regOut.add("int", regout)
        self.regTmp.add("int", regtmp)
        regin, regout, regtmp = self.gen.getRegisterIOT("vi")
        self.regIn.add("vint", regin)
        self.regOut.add("vint", regout)
        self.regTmp.add("vint", regtmp)
        regin, regout, regtmp = self.gen.getRegisterIOT("vf")
        self.regIn.add("vflt", regin)
        self.regOut.add("vflt", regout)
        self.regTmp.add("vflt", regtmp)
        self.regCurrent = self.regIn
        self.hasReturn = False
        decl = self.visit(ctx.fndcl())                	# Visit function
        body = self.visit(ctx.fnbody())
        for i in body:
            self.IR.addNode(i)
        if not self.hasReturn :  # Return insn if no return value (void function)
            self.IR.addNode(H2Node(H2NodeType.RTN))
        self.tab -= 1
        return body

    def visitFnbody(self, ctx:HybroLangParser.FnbodyContext):
        self.Trace()
        self.tab += 1
        for localVarDef in ctx.localvardef():
            self.visit (localVarDef)
        IR = self.visit (ctx.actionlist())
        if ctx.returnexpr():
            IR += self.visit (ctx.returnexpr())
        self.tab -= 1
        return IR

    def visitActionlist(self, ctx:HybroLangParser.ActionlistContext):
        self.Trace()
        self.tab += 1
        IR = []
        for action in ctx.action():
            insn = self.visit (action)
            IR += insn
        self.tab -= 1
        return IR

    def visitAction(self, ctx:HybroLangParser.ActionContext):
        self.Trace()
        self.tab += 1
        IR = []
        if ctx.getChildCount() == 2: # Affectexpr
            insn = self.visit (ctx.affectexpr(0))
            IR += [insn]
        elif ctx.getChildCount() == 11: # For loop
            treeLoopPrelude =  self.visit(ctx.affectexpr(0))
            treeLoopCond =     self.visit(ctx.condexpr())
            treeLoopContinue = self.visit(ctx.affectexpr(1))
            treeLoopAction =   self.visit(ctx.actionlist())
            labelPrologue = self.lTable.genLabelName("prologue")
            labelBegin = self.lTable.genLabelName("begin")
            labelEnd = self.lTable.genLabelName("end")
            IR += [H2Node(H2NodeType.LABEL, labelName  = labelPrologue)]
            IR += [treeLoopPrelude]
            IR += [H2Node(H2NodeType.LABEL, labelName  = labelBegin)]
            treeLoopCond.setTargetName(labelEnd)
            treeLoopCond.setSourceName(labelBegin)
            IR += [treeLoopCond]
            IR += treeLoopAction
            IR += [treeLoopContinue]
            IR += [H2Node(H2NodeType.BA,    targetName = labelBegin)]
            IR += [H2Node(H2NodeType.LABEL, labelName  = labelEnd)]
        else:
            fatalError("visitAction : unknown child count %d"%ctx.getChildCount())
        self.tab -= 1
        return IR

    def visitAffectexpr(self, ctx:HybroLangParser.AffectexprContext):
        self.Trace()
        self.tab += 1
        if ctx.getChildCount() == 3: # Simple affectation
            nodeVar  = H2Node(H2NodeType.VARIABLE, variableName = ctx.Name().getText())
            opType = self.sTable.get(nodeVar.getVariableName())
            nodeVar.setOpType(opType)
            nodeExpr = self.visit(ctx.unaryexpr(0))
            nodeExpr.setOpType(opType)
            IRnode   = H2Node(H2NodeType.OPERATOR,  opName = "=", sonsList = [nodeVar, nodeExpr], opType=opType)
        elif ctx.getChildCount() == 6: # Array affectation STORE
            arrayName = ctx.Name().getText()
            nodeArrayIndex = self.visit(ctx.unaryexpr(0))
            nodeValue = self.visit(ctx.unaryexpr(1))
            # @ store = @nodeVar + nodeArrayIndex * wordLen / 8
            opType = self.sTable.get(arrayName)
            wordLen = opType['wordLen']
            vectorLen = opType['vectorLen']
            nodeVar   = H2Node(H2NodeType.VARIABLE, variableName = arrayName)
            nodeConst = H2Node(H2NodeType.CONST, constValue = "(%s * %s) / 8" % (vectorLen, wordLen))
            nodeMul   = H2Node(H2NodeType.OPERATOR, opName = "*", sonsList = [nodeArrayIndex, nodeConst])
            nodeAdd   = H2Node(H2NodeType.OPERATOR, opName = "+", sonsList = [nodeVar, nodeMul])
            zeroNode  = H2Node(H2NodeType.CONST, constValue = 0)
            IRnode    = H2Node(H2NodeType.W, opName = "W", sonsList = [nodeAdd, nodeValue, zeroNode], opType=opType)
        else:
            fatalError("visitAffectexpr unknown child count %d"%ctx.getChildCount())
        self.tab -= 1
        return IRnode

    def visitCondexpr(self, ctx:HybroLangParser.CondexprContext):
        condToNode = {"==": H2NodeType.BNE, "!=": H2NodeType.BEQ,
                      "<": H2NodeType.BGE, ">=":H2NodeType.BLT,
                      ">": H2NodeType.BLE, "<=": H2NodeType.BGT,
                      }

        nodeLeft = self.visit(ctx.varorvalue(0))
        self.visit(ctx.condOperator())
        condExpr = ctx.condOperator().getText()
        nodeRight = self.visit(ctx.varorvalue(1))

        return H2Node(condToNode[condExpr], opName  = condExpr, sonsList = [nodeLeft, nodeRight])

    typeCorrespondances = {"int":"int","uint":"int","flt":"flt","sint":"int","suint":"int"}
    def visitVardcllist(self, ctx:HybroLangParser.VardcllistContext):
        self.Trace()
        self.tab += 1
        dataType = self.visit(ctx.vardcl())
        for varobj in ctx.Name():
            varName = varobj.getText()
            self.sTable.add (varName, dataType)
            self.sTable.setRegister (varName, self.regCurrent.getNextRegister(dataType["arith"][0:3]) )
            if self.abi == "power" and self.regCurrent == self.regIn:
                if dataType["arith"][0:3] == "int":
                    self.regCurrent.getNextRegister("flt")
                elif dataType["arith"][0:3] == "flt":
                    self.regCurrent.getNextRegister("int")
        self.tab -= 1

    def visitVardcl(self, ctx:HybroLangParser.VardclContext):
        typeCorrespondances = HybrogenTreeCompiler.typeCorrespondances
        self.Trace()
        self.tab += 1
        dataType = self.visit(ctx.datatype())
        self.tab -= 1
        varName = ctx.Name().getText()
        if self.verbose:
            print("[visitVarDecl] allocating on \"%s\" bank for variable '%s'" % (self.regCurrent.bankName, varName))
        self.sTable.add (varName, dataType)
        #arith = typeCorrespondances[dataType["arith"].replace("[]","")]
        #self.sTable.setRegister (varName, self.regCurrent.getNextRegister(arith))
        if dataType["arith"][-1] != "]":
            self.sTable.setRegister (varName, self.regCurrent.getNextRegister(dataType["arith"][0:3]) )
        else:
            #declaration of pointer -> change datatype to addr
            self.sTable.setRegister (varName,  self.regCurrent.getNextRegister("int"))

        return dataType

    def visitVarorvalueArray(self, ctx:HybroLangParser.VarorvalueArrayContext): # LOAD
        self.Trace()
        self.tab += 1
        treeArrayIndex = self.visit(ctx.unaryexpr())
        arrayName = ctx.Name().getText()
        # @ R = @nodeVar + treeArrayIndex * wordLen / 8
        array_opType = self.sTable.get(arrayName)
        R_opType = H2Type(array_opType["arith"].replace("[]",""), array_opType["wordLen"], array_opType["vectorLen"])
        # NOTE : this only stands true for 32-bit architectures, the width of the data type should be given as
        # a parameter
        addrOpType = H2Type("int", 32, 1)
        nodeVar   = H2Node(H2NodeType.VARIABLE, variableName=arrayName, opType=addrOpType)
        wordLen = array_opType['wordLen']
        vectorLen = array_opType['vectorLen']
        nodeConst = H2Node(H2NodeType.CONST, constValue = "(%s * %s) / 8" % (vectorLen, wordLen), opType=addrOpType)
        nodeMul   = H2Node(H2NodeType.OPERATOR, opName = "*", sonsList = [treeArrayIndex, nodeConst], opType=addrOpType)
        nodeAdd   = H2Node(H2NodeType.OPERATOR, opName = "+", sonsList = [nodeVar, nodeMul], opType=addrOpType)
        self.tab -= 1
        return H2Node(H2NodeType.R, opName = "R", sonsList = [nodeAdd], opType=R_opType)

    def visitVarorvalueConst(self, ctx:HybroLangParser.VarorvalueConstContext):
        self.Trace()
        self.tab += 1
        constStr = self.removeDieze (ctx.getText())
        n = H2Node(H2NodeType.CONST, constValue = constStr)
        self.tab -= 1
        return n

    def removeDieze (self, word:str):
        if "#" == word[0]:
            return word[1:]
        else:
            return word

    def visitVarorvalueVar(self, ctx:HybroLangParser.VarorvalueVarContext):
        self.Trace()
        n = H2Node(H2NodeType.VARIABLE, variableName = ctx.getText())
        return n

    def visitReturnexpr(self, ctx:HybroLangParser.ReturnexprContext):
        self.Trace()
        self.tab += 1
        nodeRetExpr   = self.visit(ctx.unaryexpr())
        opType = self.sTable.get("h2_outputVarName")
        nodeRetVar    = H2Node(H2NodeType.VARIABLE, variableName = "h2_outputVarName", opType=opType)
        returnValue   = H2Node(H2NodeType.OPERATOR, opName = "=", sonsList = [nodeRetVar, nodeRetExpr], opType=opType)
        returnNode    = H2Node(H2NodeType.RTN)
        self.hasReturn = True
        self.tab -= 1
        return [returnValue, returnNode]

    def visitUnaryexpr(self, ctx:HybroLangParser.UnaryexprContext):
        self.Trace()
        self.tab += 1
        if ctx.getChildCount() == 3:
            l = self.visit(ctx.unaryexpr(0))
            r = self.visit(ctx.unaryexpr(1))
            l_varName = l.getVariableName()
            r_varName = r.getVariableName()
            # If the LHS and the RHS own variable names, we use them to get their opTypes
            # otherwise we default it to None
            l_opType = self.sTable.get(l_varName) if l_varName is not None else None
            r_opType = self.sTable.get(r_varName) if r_varName is not None else None
            l.setOpType(l_opType)
            r.setOpType(r_opType)
            node = H2Node(H2NodeType.OPERATOR, opName = ctx.op.text, sonsList = [l, r])
        else:
            node = self.visit(ctx.varorvalue())
        self.tab -= 1
        return node

def fatalError (msg):
    print ("Fatal error: %s"%msg)
    sys.exit(-1)

def BuildTreeAndCompile (inputCompilette, platform, verbose, debug, dbIds):
    v = HybrogenTreeCompiler(inputCompilette, platform, verbose, debug, dbIds)
    cCode = v.getTree()
    prefixDict = v.gatherOpsAndTypes()
    return prefixDict, cCode

def writeCandParseCompilette(fileIn, platform, verbose, debug, dbIds):
    """ Interleave C and rewrited compilette
    """
    BEGIN = "#["
    END = "]#"
    outsideCompilette = True
    cCode = ""
    prefixDict = dict()
    for line in fileIn:
        if (BEGIN in line and outsideCompilette):
            outsideCompilette = False
            line, compiletteCode = line.split(BEGIN)
        elif END in line and not outsideCompilette:
            outsideCompilette = True
            endCompilette, line = line.split(END)
            compiletteCode += endCompilette
            pDict, compiledCompilette = BuildTreeAndCompile(compiletteCode, platform, verbose, debug, dbIds)
            for arith, prefixes in pDict.items():
                prefixDict.setdefault(arith, set()).update(prefixes)
            cCode += str(compiledCompilette)
        elif (BEGIN in line and not outsideCompilette) or (END in line and outsideCompilette):
            fatalError ("Something weird append on line: "+line)
        if outsideCompilette:
            cCode += line
        else:
            compiletteCode += line
    return prefixDict, cCode

class HybrogenTreeGather(HybroLangVisitor):

    sem = {"*": "MUL", "+":"ADD", "/":"DIV", "-":"SUB",
           "R":"R", "W":"W", "CMP":"CMP",
           "==": "BNE", "!=":"BEQ",
           "<": "BGE" , ">=":"BLT",
           ">": "BLE",  "<=":"BGT",
           "BA":"BA",
           "INV":"INV",
           "NEG":"NEG",
           "CMPGE": "CMPGE", "CMPGT": "CMPGT",
           "CMPLE": "CMPLE", "CMPLT": "CMPLT",
           "CMPNE": "CMPNE", "CMPEQ": "CMPEQ",
           "BEQZ": "BEQZ", "BNEZ": "BNEZ" }

    def __init__(self, inputCompilette, archList, verbose, debug):
        self.tab = 0
        self.archList = archList
        self.archMaster = archList[0]
        self.verbose = verbose
        self.debug = debug
        self.datatype = {}
        self.operatorList = set()
        #create H2SymbolTable only for master architecture ?
        self.sTable = H2SymbolTable(self.archMaster)
        self.Trace()
        if self.verbose:
            print ("HybrogenVisitor for %s Verbose : %s Debug : %s"%(self.archMaster, verbose, debug))
        l = HybroLangLexer(antlr4.InputStream(inputCompilette)) # Initialize ANTLR lexer, tokenizer, parse, tree
        s = CommonTokenStream(l)
        p = HybroLangParser(s)
        syntaxTree = p.compilationunit()
        self.tree = self.visit(syntaxTree)                      # Visit syntax tree & gather Op & dataType

    def getPrefixTuple(self):
        tupleOperateurType = []
        for o in self.operatorList:
            op = self.sem[o]
            for t in self.datatype:
                tupleOperateurType.append ((op, t))
        if self.verbose:
            print ("Tuple Operator Type :"+str(tupleOperateurType))
        return tupleOperateurType

    def printIfVerbose (self, msg):
        if self.verbose:
            print (msg, file=sys.stderr)

    def Trace(self):
        fname = sys._getframe(1).f_code.co_name
        self.printIfVerbose(fname)

    def visitAffectexpr(self, ctx:HybroLangParser.AffectexprContext):
        self.Trace()
        if ctx.getChildCount() == 3:
            self.visit (ctx.unaryexpr(0))
        elif ctx.getChildCount() == 6:
            self.visit (ctx.unaryexpr(0))
            self.visit (ctx.unaryexpr(1))
            self.operatorList.add ("W")
            self.operatorList.add ("+")

    def visitDatatype(self, ctx:HybroLangParser.DatatypeContext):
        self.Trace()
        h = H2Type (ctx.typebase().getText(), ctx.wordlen.getText(), ctx.vectorlen.getText())
        a = h["arith"][0]
        if a not in self.datatype:
            self.datatype[a] = set()
        self.datatype[a].add ((h["wordLen"], h["vectorLen"]))

    def visitVarorvalueArray(self, ctx:HybroLangParser.VarorvalueArrayContext):
        self.Trace()
        self.visit (ctx.unaryexpr())
        self.operatorList.add ("R")
        self.operatorList.add ("+")

    def visitAction(self, ctx:HybroLangParser.ActionContext):
        self.Trace()
        if ctx.getChildCount() == 2: # Affectexpr
            self.visit (ctx.affectexpr(0))
        elif ctx.getChildCount() == 11: # For loop
            self.visit(ctx.affectexpr(0))
            self.visit(ctx.condexpr())
            self.visit(ctx.affectexpr(1))
            self.visit(ctx.actionlist())
        else:
            fatalError("visitAction : unknown child count %d"%ctx.getChildCount())

    def visitCondexpr(self, ctx:HybroLangParser.CondexprContext):
        self.visit(ctx.varorvalue(0))
        self.visit(ctx.condOperator())
        if "power" in self.archList:
            self.operatorList.add ("CMP")
        if "kalray" in self.archList:
            self.operatorList.add ("CMPGE")
            self.operatorList.add ("CMPGT")
            self.operatorList.add ("CMPLE")
            self.operatorList.add ("CMPLT")
            self.operatorList.add ("CMPEQ")
            self.operatorList.add ("CMPNE")
            self.operatorList.add ("BNEZ")
            self.operatorList.add ("BEQZ")
        self.operatorList.add ("BA")
        self.operatorList.add (ctx.condOperator().getText())
        self.visit(ctx.varorvalue(1))

    def visitUnaryexpr(self, ctx:HybroLangParser.UnaryexprContext):
        self.Trace()
        if "kalray" in self.archList:
            self.operatorList.add ("INV")
            self.operatorList.add ("NEG")
        if ctx.getChildCount() == 3:
            l = self.visit(ctx.unaryexpr(0))
            r = self.visit(ctx.unaryexpr(1))
            self.operatorList.add (ctx.op.text)
        else:
            node = self.visit(ctx.varorvalue())
            self.operatorList.add ("*")

def BuildTreeAndGather (inputCompilette, archList, verbose, debug):
    v = HybrogenTreeGather(inputCompilette, archList, verbose, debug)
    return v.getPrefixTuple()

def gatherOpsAndTypes(fileIn, archList, verbose, debug):
    """ Extract DataType and operators
    """
    BEGIN = "#["
    END = "]#"
    outsideCompilette = True
    prefixTuple = []
    for line in fileIn:
        if (BEGIN in line and outsideCompilette):
            outsideCompilette = False
            line, compiletteCode = line.split(BEGIN)
        elif END in line and not outsideCompilette:
            outsideCompilette = True
            endCompilette, line = line.split(END)
            compiletteCode += endCompilette
            prefixTuple += BuildTreeAndGather(compiletteCode, archList, verbose, debug)
        elif (BEGIN in line and not outsideCompilette) or (END in line and outsideCompilette):
            fatalError ("Something weird append on line: "+line)
        if not outsideCompilette:
            compiletteCode += line
    return prefixTuple

def extractCompilette(fileIn):
    """ Compilette code
    """
    BEGIN = "#["
    END = "]#"
    outsideCompilette = True
    for line in fileIn:
        if (BEGIN in line and outsideCompilette):
            outsideCompilette = False
            line, compiletteCode = line.split(BEGIN)
        elif END in line and not outsideCompilette:
            outsideCompilette = True
            endCompilette, line = line.split(END)
            compiletteCode += endCompilette
        elif (BEGIN in line and not outsideCompilette) or (END in line and outsideCompilette):
            fatalError ("Something weird append on line: "+line)
        if not outsideCompilette:
            compiletteCode += line
    return compiletteCode

if __name__ == '__main__':
    import sys, os, argparse

    archList = ("riscv", "power", "kalray", "cxram", "aarch64")
    aliasDict = { "riscv": { "arch":["riscv", ],
                             "extension": [["RV32I", "RV32F", "RV32M", "RV32D"],],
                             "abi": "RV32G"},
                 "power": { "arch":["power",],
                            "extension": [["p1", "ppc", "v2.03", "v2.07", "v3.0", "3.0b"],],
                             "abi": "power" },
                 "kalray": { "arch":["kalray",],
                             "extension": [["kalray",], ],
                             "abi": "kalray" },
                  "gap9":{ "arch":["riscv", ],
                             "extension": [["RV32I", "RV32F", "RV32M", "RV32Xf16"], ],
                             "abi": "GAP9"},
                  "cxram":{ "arch":["riscv", "cxram"],
                            "extension": [["RV32I", "RV32F", "RV32M", "RV32D"], ["cxram"]],
                            "abi": "CXRAM"},
                  "aarch64":{ "arch":["aarch64"],
                          "extension": [["A64", "A32", "T32"], ],
                          "abi": "A64"},
    }
    parser = argparse.ArgumentParser("Hybrogen to C rewriter")
    group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument ('-i', '--inputfile', required=True, help="give input file name")
#    parser.add_argument('fileName', type=str, help='file name')
    parser.add_argument ('-a', '--arch', required=True, nargs='+', help="give arch parameter (archname & extension(s)) or alias : "+str(archList))
    parser.add_argument ('-b', '--abi',    help="give abi parameter")
#    group.add_argument ('-t', '--tree',    action='store_true', help="shows syntax tree")
    group.add_argument ('-c',  '--toC',      action='store_true', help="rewrite to C")
    group.add_argument ('-e',  '--extract',  action='store_true', help="extract compilettes source code")
    parser.add_argument ('-v', '--verbose', action='store_true', help="verbose")
    parser.add_argument ('-g', '--debug',   action='store_true', help="add function version instead of macros")
    parser.add_argument ('-d', '--dbIds',   default="localhost:hybrogen:hybrogen:hybrogen", help="give quadruplet database identification host:dbName:dbUser:dbpasswd")

    args = parser.parse_args()
    if args.arch[0] in aliasDict:
        arch = aliasDict[args.arch[0]]["arch"]
        extension = aliasDict[args.arch[0]]["extension"]
        abi = aliasDict[args.arch[0]]["abi"]
    elif (args.arch[0] not in archList):
        fatalError ("Unsupported architecture:"+args.arch[0])
    else:
        arch = args.arch[0]
        extension = args.arch[1:]
        abi = args.abi
    platform = {"arch": arch, "extension":extension, "abi":abi}
    if args.extract:
        fileIn  = open(args.inputfile, 'r')
        compiletteCode = extractCompilette(fileIn)
        print(compiletteCode)
    elif args.toC:
        outFileName, ext = os.path.splitext(args.inputfile)
        outFileName += ".c"
        # Passe 1 construction de l'arbre
        ids = args.dbIds.split(":")
        dbIds = {"host": ids[0], "dbname": ids[1], "user": ids[2],"pwd": ids[3]}
        print('HybroLang Compiler %s (host=%s dbname=%s user=%s)'%(H2_RELEASE, dbIds["host"], dbIds["dbname"], dbIds["user"]))
        fileIn  = open(args.inputfile, 'r')
        prefixDict, cCode = writeCandParseCompilette(fileIn, platform, args.verbose, args.debug, dbIds)
        fileIn.close()

        prefixTuples = list()
        for arith in prefixDict.keys():
            prefixTuples += [ (op, arith[0]) for op in prefixDict[arith]]
        if args.verbose:
            print("PrefixTuples after compilation and optimization:")
            print(prefixTuples)
        # Connect to backend only for master architecture ?
        gen = GenGeneratorFromDb (arch[0], extension[0], abi, dbIds, args.verbose, args.debug)
        prefixCode = gen.genAndGetCode(prefixTuples)

        fileOut = open(outFileName, 'w')
        fileOut.write (prefixCode)
        fileOut.write (cCode)
        fileOut.close()
    else:
        fatalError ("action not recognized")
