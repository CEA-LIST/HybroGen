#!/usr/bin/env python3

from H2Utils import *
from HybroGen.GenGeneratorFromDb   import GenGeneratorFromDb
from HybroLang.H2Aarch64Rewrite    import H2Aarch64Rewrite
from HybroLang.H2RiscvRewrite      import H2RiscvRewrite
from HybroLang.H2PowerRewrite      import H2PowerRewrite
from HybroLang.H2CxRAMRewrite      import H2CxRAMRewrite
from HybroLang.H2TransformToMac    import H2TransformToMac
from HybroLang.H2CodeGeneration    import H2CodeGeneration
from HybroLang.H2ConstantOptimizer import H2ConstantOptimizer
from HybroLang.H2LabelTable        import H2LabelTable
from HybroLang.H2MovOptimize       import H2MovOptimize
from HybroLang.H2Node              import H2Node
from HybroLang.H2NodeType          import H2NodeType
from HybroLang.H2SymbolTable       import H2SymbolTable
from HybroLang.H2Type              import H2Type
from HybroLang.H2WindowRewrite     import H2WindowRewrite
from HybroLang.H2RegCSI            import H2RegCSI
from HybroLang.H2RegAllocTmp       import H2RegAllocTmp
from HybroLang.H2Debug             import H2Debug

class H2IR2():
    """Intermediate representation for HybroLang. Composed of list of
    expression tree, and the code generation"""

    def __init__(self, platform, sTable, args, dbIds = None):
        self.IList = []
        self.platform = platform
        self.archMaster = self.platform["arch"][0]
        self.verbose = args.verboseIR
        self.tmpVarNumber = 0
        self.labelNumber = 0
        self.dbIds = dbIds
        self.sTable = sTable
        self.doShowTree = args.graphviz
        self.args = args

    def __str__(self):
        tmp = "%s nodes :\n"%str(len(self.IList))
        for i in range(len(self.IList)):
            tmp += "%d %s\n"%(i, str(self.IList[i]))
        return tmp

    def addNode(self, node: H2Node):
        self.IList.append (node)

    def trace (self, msg):
        if self.verbose:
            print (msg)

    def printIR (self, irList, messsage):
        print(messsage)
        for i in range(len(irList)):
            print("%d:%s\n"%(i, irList[i]))

    def generateCodeGeneration(self, sTable, regTmp, lTable, regIn):
        """ Generate C code generator from an IR representation + symbol table """
        insnCode = ""     # Code generator code
        callbackCode = "" # Callback for branch resolution


        debug = H2Debug()
        if self.verbose :   self.printIR(self.IList,"IR before code generation")
        if self.doShowTree: debug.showTree(self.archMaster+": Initial IR", self.IList)
        # Generic optimization
        # * Simple mov transformation
        p = H2MovOptimize(self.IList, self.sTable, self.verbose)
        self.IList = p.getNewInsnList()
        if self.doShowTree: debug.showTree(self.archMaster+": after Mv Optimize", self.IList)
        # Rewrite pass for exclusive different master architecture
        if self.archMaster in ("power"):
            p = H2PowerRewrite(self.platform, self.IList, self.verbose)
            self.IList = p.getNewInsnList()
        elif self.archMaster in ("aarch64"):
            p = H2Aarch64Rewrite(self.archMaster, self.IList, self.verbose)
            self.IList = p.getNewInsnList()
            p = H2TransformToMac(self.IList, self.verbose)
            self.IList = p.getNewInsnList()
        elif self.archMaster in ("riscv"):
            p = H2RiscvRewrite(self.archMaster, self.IList, self.verbose)
            self.IList = p.getNewInsnList()
            p = H2TransformToMac(self.IList, self.verbose)
            self.IList = p.getNewInsnList()
        elif self.platform["abi"] in ("CXRAM"):
        # Rewrite pass for second architecture
            p = H2CxRAMRewrite(self.platform, lTable, sTable, regTmp, regIn, verbose=self.verbose, dbIds = self.dbIds)
            self.IList = p.rewriteInsns(self.IList)
            if self.verbose :
                self.printIR (self.IList, "IR after H2CxRAMRewrite pass")
        else:
            self.trace("No specific rewrite for %s"%(self.platform))
        if self.doShowTree: debug.showTree(self.archMaster+": After Arch specific optim.", self.IList)

        new = []
        p = H2ConstantOptimizer(self.archMaster, verbose=self.verbose)
        for i in self.IList :
            new += p.rewriteInsn(i)
        self.IList = new
        if self.verbose :   self.printIR (self.IList, "IR after H2ConstantOptimizer pass")
        if self.doShowTree: debug.showTree(self.archMaster+": After constant optim", self.IList)

        p = H2WindowRewrite(self.IList, self.archMaster, verbose=self.verbose)
        self.IList = p.getOptimizedInsnList()
        if self.verbose :   self.printIR (self.IList, "IR after Window Rewrite")
        if self.doShowTree: debug.showTree(self.archMaster+": after Window Rewrite", self.IList)

        r = H2RegCSI(self.IList, sTable, regTmp, regIn, self.args)
        if self.verbose :   self.printIR (self.IList, "IR after reg alloc for sub expressions")
        if self.doShowTree: debug.showTree(self.archMaster+": after regAlloc subexpressions", self.IList)

        r = H2RegAllocTmp(self.IList, sTable, regTmp, regIn, self.args)
        self.IList = r.getNewList()
        if self.verbose :   self.printIR (self.IList, "IR after regAllocTmp")
        if self.doShowTree: debug.showTree(self.archMaster+": after regAlloc tmp", self.IList)

        cG = H2CodeGeneration (self.IList, sTable, regTmp, regIn, lTable, self.args)
        return cG.getCode ()

    def gatherOpsAndTypes(self):
        prefixTuple = dict()
        def visit(insn: H2Node):
            if insn.isOperatorOrMem():
                arith = insn.opType['arith']
                opName = insn.getSemName()
                prefixTuple.setdefault(arith, set()).add(opName)
                # print(prefixTuple)
                # print(self)
                for child in insn.sonsList:
                    visit(child)
            elif insn.isB() or insn.isCmp():
                opName = insn.nodeType.name
                prefixTuple.setdefault("int", set()).add(opName)
        for insn in self.IList:
            visit(insn)
        if "int" in prefixTuple and "MUL" in prefixTuple['int']:
            prefixTuple.setdefault("int", set()).add("SL")
        return prefixTuple

    def getPrefixCode(self):
        opsTypesDict   = self.gatherOpsAndTypes()
        opsTypesTuples = list()
        for arith in opsTypesDict.keys():
            opsTypesTuples += [ (op, arith[0]) for op in opsTypesDict[arith]]
        extList = self.platform["extension"][0]
        abi = self.platform["abi"]
        gen = GenGeneratorFromDb(self.archMaster, extList, abi, self.dbIds)
        prefixCode = gen.genAndGetCode(opsTypesTuples)
        return prefixCode
