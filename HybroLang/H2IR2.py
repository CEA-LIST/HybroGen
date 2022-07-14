#!/usr/bin/env python3

from HybroGen.GenGeneratorFromDb import GenGeneratorFromDb

from HybroLang.H2SymbolTable  import H2SymbolTable
from HybroLang.H2LabelTable   import H2LabelTable
from HybroLang.H2Node         import H2Node
from HybroLang.H2NodeType     import H2NodeType
import random
import sys

class H2Type():
    typeCorrespondances = {'int' : 'i', 'flt' : 'f', 'uint': 'u', 'cpl': 'c',
            'pix' : 'p', 'ipv4': '4', 'ipv6': '6', 'sint': 'i', 'suint':'u', 'int[]':'i'}

    def __init__(self, a, w, v):
        self.t = {"arith":a, "wordLen":w, "vectorLen":v}

    def __iter__(self):
        return iter(self.t)

    def __str__(self):
        return str(self.t)

    def __getitem__(self, k):
        return self.t[k]

    def keys(self):
        return self.t

from HybroLang.H2PowerRewrite      import H2PowerRewrite
from HybroLang.H2CxRAMRewrite      import H2CxRAMRewrite
from HybroLang.H2KalrayRewrite     import H2KalrayRewrite
from HybroLang.H2ConstantOptimizer import H2ConstantOptimizer
from HybroLang.H2RegisterAllocator import H2RegisterAllocator
from HybroLang.H2MovOptimize       import H2MovOptimize
from HybroLang.H2IRFlattener       import H2IRFlattener

class H2IR2():
    """Intermediate representation for HybroLang. Composed of list of
    expression tree, and the code generation"""

    def __init__(self, platform, verbose = False, dbIds = None):
        self.IList = []
        self.platform = platform
        self.archMaster = self.platform["arch"][0]
        self.verbose = verbose
        self.tmpVarNumber = 0
        self.labelNumber = 0
        self.dbIds = dbIds

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

    def generateCodeGeneration(self, sTable, regTmp, lTable, regIn):
        """ Generate code generator for an IR representation + symbol table """
        insnCode = ""
        callbackCode = ""
        self.trace("IR before code generation")
        if self.verbose :
            for i in range(len(self.IList)):
                self.trace ("%d:%s\n"%(i, self.IList[i]))

        # Generic optimization
        # * Simple mov transformation
        #p = H2MovOptimize(self.IList, self.verbose)
        #self.IList = p.getNewInsnList()
        # Rewrite pass for exclusive different master architecture
        if self.archMaster in ("power"):
            p = H2PowerRewrite(self.platform, self.IList, self.verbose)
            self.IList = p.getNewInsnList()
        elif self.archMaster in ("kalray"):
            p = H2KalrayRewrite(self.archMaster, self.IList, self.verbose)
            self.IList = p.getNewInsnList()
        elif self.platform["abi"] in ("CXRAM"):
        # Rewrite pass for second architecture
            if self.verbose:
                print("H2CxRAMRewrite pass")
            p = H2CxRAMRewrite(self.platform, lTable, sTable, regTmp, regIn, verbose=self.verbose, dbIds = self.dbIds)
            self.IList = p.rewriteInsns(self.IList)
            if self.verbose :
                print("IR after H2CxRAMRewrite pass")
                for i in range(len(self.IList)):
                    print("%d:%s\n"%(i, self.IList[i]))
        else:
            self.trace("No specific rewrite for %s"%(self.platform))
        self.trace("H2ConstantOptimizer pass")
        new = []
        p = H2ConstantOptimizer(self.archMaster, verbose=self.verbose)
        for i in self.IList :
            new += p.rewriteInsn(i)
        self.IList = new
        if self.verbose :
            print("IR after H2ConstantOptimizer pass")
            for i in range(len(self.IList)):
                print ("%d:%s\n"%(i, self.IList[i]))
        self.trace("Now entering H2IRFlattener pass")
        p = H2IRFlattener(self.platform, sTable, verbose=self.verbose)
        self.IList = p.rewriteInsns(self.IList)
        if self.verbose :
            print("IR after H2IRFlattener pass")
            for i in range(len(self.IList)):
                print ("%d:%s\n"%(i, self.IList[i]))
        self.trace("Now entering H2RegisterAllocator pass")
        new = []
        p = H2RegisterAllocator(self.archMaster, sTable, regTmp, verbose=self.verbose)
        self.IList = p.rewriteInsns(self.IList)
        if self.verbose :
            print("IR after H2RegisterAllocator pass")
            for i in range(len(self.IList)):
                print ("%d:%s\n"%(i, self.IList[i]))
        # Code generation
        for i in range(len(self.IList)):
            insn = self.IList[i]
            if self.verbose :
                print ("Insn %d before code generation : \n%s\n"%(i, insn))
            tmpCode, tmpCallbackCode = self.codeGeneration (insn, sTable, self.archMaster, 0)
            insnCode += tmpCode
            callbackCode += tmpCallbackCode
            if self.verbose :
                print("Generated code for insn %d:\n%s"%(i, tmpCode))
        insnCode += "\t/* Call back code for loops */\n"
        insnCode += "\th2_save_asm_pc = h2_asm_pc;\n"
        insnCode += callbackCode
        insnCode += "\th2_asm_pc = h2_save_asm_pc;\n"
        insnCode += "\th2_iflush(ptr, h2_asm_pc);\n"

        initcode = "/* Code Generation of %d instructions */\n"%len (self.IList)
        initcode += "/* Symbol table :*/\n%s\n\n"%(sTable.getCDecl())
        initcode += "/* Label  table :*/\n%s\n\n"%(lTable.getCDecl())
        initcode +="\th2_asm_pc = (h2_insn_t *) ptr;\n"
        initcode +="\th2_codeGenerationOK = true;\n"
        self.trace(self)
        return initcode + insnCode

    def gatherOpsAndTypes(self):
        prefixTuple = dict()
        def visit(insn: H2Node):
            if insn.isOperatorOrMem():
                arith = insn.opType['arith']
                opName = insn.getSemName()
                prefixTuple.setdefault(arith, set()).add(opName)
                for child in insn.sonsList:
                    visit(child)
            elif insn.isB() or insn.isCmp():
                opName = insn.nodeType.name
                prefixTuple.setdefault("int", set()).add(opName)
        for insn in self.IList:
            visit(insn)
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

    def codeGeneration(self, insn:H2Node, sTable, archMaster, tab):
        """Generate code generators"""
        code = ""
        callback = ""
        # print(insn)
        for i in range(len(insn.sonsList)):
            tmpCode, tmpCallback = self.codeGeneration (insn.sonsList[i], sTable, archMaster, tab+1)
            code += tmpCode
            callback += tmpCallback
        if insn.isOperator():
            insnSemName = insn.getSemName()
            if insnSemName in ["MV", "LUI"]:
                destReg = self.getDestination(insn.sonsList[0])
                srcR    = self.getDestination(insn.sonsList[1])
                if str(destReg) != str(srcR):
                    code += "\t%s_gen%s_2(%s, %s);\n"%(archMaster, insn.getSemName(), destReg, srcR)
            elif insnSemName in ["INV", "NEG"]:
                destReg = self.getDestination(insn)
                src    = self.getDestination(insn.sonsList[0])
                code += "\t%s_gen%s_2(%s, %s);\n"%(archMaster, insn.getSemName(), destReg, src)

            elif "MV" != insnSemName:
                destReg = self.getDestination(insn)
                srcL    = self.getDestination(insn.sonsList[0])
                srcR    = self.getDestination(insn.sonsList[1])
                code += "\t%s_gen%s_3(%s, %s, %s);\n"%(archMaster, insn.getSemName(), destReg, srcL, srcR)
            else:
                self.fatal ("(codeGeneration) Unknown operator %s"%insn.getSemName())
        elif insn.isR():
            destReg = self.getDestination(insn.sonsList[0])
            srcReg = self.getDestination(insn.sonsList[1])
            immValue = self.genImmValue(0) # TODO : optimize for const values
            code += "\t%s_gen%s_3(%s, %s, %s);\n"%(archMaster, insn.getSemName(), destReg, srcReg, immValue)
        elif insn.isW():
            destReg = self.getDestination(insn.sonsList[0])
            srcReg = self.getDestination(insn.sonsList[1])
            immValue = self.genImmValue(0) # TODO : optimize for const values
            code += "\t%s_gen%s_3(%s, %s, %s);\n"%(archMaster, insn.getSemName(), destReg, srcReg, immValue)
        elif insn.isCmp():
            if self.archMaster== "kalray":
                cmpCond  = str(insn.nodeType).split (".")[1]
                regDest = "(h2_sValue_t) {REGISTER, 'i', 1, 32, 63, 0}" # Hardwired 63
                srcLeft  = insn.sonsList[0].getVariableName()  # TODO improve varorvalue handling
                srcRight = insn.sonsList[1].getVariableName()
                code += '\t%s_gen%s_3(%s, %s, %s);\n'%(archMaster,cmpCond, regDest, srcLeft, srcRight)
            else:
                srcLeft  = insn.sonsList[0].getVariableName()  # TODO improve varorvalue handling
                srcRight = insn.sonsList[1].getVariableName()
                #val0 = "(h2_sValue_t) {VALUE, 'i', 1, 32, 0, 0}" # Hardwired 0
                code += '\t%s_genCMP_2(%s, %s);\n'%(archMaster, srcLeft, srcRight)
        elif insn.isB():
            if insn.nodeType == H2NodeType.BA:
                reg0 = "(h2_sValue_t) {REGISTER, 'i', 1, 32, 0, 0}" # Hardwired 0
                if self.archMaster== "power" or archMaster== "kalray":
                    target = self.genImmValue ("(labelAddresses ["+insn.getTargetName()+"] - h2_asm_pc)")
                    code += '\t%s_genBA_1(%s);\n'%(archMaster, target)
                elif  self.archMaster== "riscv":
                    target = self.genImmValue ("(labelAddresses ["+insn.getTargetName()+"] - h2_asm_pc)*4")
                    code += '\t%s_genBA_2(%s, %s);\n'%(archMaster, reg0, target)
                # code += '\tprintf("h2_asm_pc : %p target\\n", h2_asm_pc);\n'
                # code += '\tprintf("target @  : %p\\n", labelAddresses ['+insn.getTargetName()+']);\n'
                # code += '\tprintf("diff @  : %d\\n", labelAddresses ['+insn.getTargetName()+'] - h2_asm_pc);\n'
            elif insn.isBcc():
                branchCond  = str(insn.nodeType).split (".")[1]
                if len(insn.sonsList) == 2:
                    #riscv
                    target = self.genImmValue ("(labelAddresses ["+insn.getTargetName()+"] - h2_asm_pc)*4")
                    srcLeft  = insn.sonsList[0].getVariableName()  # TODO improve varorvalue handling
                    srcRight = insn.sonsList[1].getVariableName()
                    code += '\t%s_gen%s_3(%s, %s, %s);\n'%(archMaster, branchCond, srcLeft, srcRight, target)
                    callback += '\th2_asm_pc = labelAddresses [%s];\n'%(insn.getSourceName())
                    callback += '\t%s_gen%s_3(%s, %s, %s);\n'%(archMaster, branchCond, srcLeft, srcRight, target)
                elif self.archMaster== "kalray":
                    target = self.genImmValue ("(labelAddresses ["+insn.getTargetName()+"] - h2_asm_pc)")
                    src = "(h2_sValue_t) {REGISTER, 'i', 1, 32, 63, 0}" # Hardwired 63
                    code += '\t%s_gen%s_2(%s, %s);\n'%(archMaster, branchCond, src, target)
                    callback += '\th2_asm_pc = labelAddresses [%s] + 1;\n'%(insn.getSourceName())
                    callback += '\t%s_gen%s_2(%s, %s);\n'%(archMaster, branchCond, src, target)
                else:
                    #power
                    target = self.genImmValue ("(labelAddresses ["+insn.getTargetName()+"] - h2_asm_pc)")
                    code += '\t%s_gen%s_1(%s);\n'%(archMaster, branchCond, target)
                    callback += '\th2_asm_pc = labelAddresses [%s] + 1;\n'%(insn.getSourceName())
                    callback += '\t%s_gen%s_1(%s);\n'%(archMaster, branchCond, target)
            else:
                self.fatalError("(codeGeneration) unknown branch type %s"%insn)
        elif insn.isLabel():
                code += '\t%s_genLABEL(%s);\n'%(archMaster, insn.getLabelName())
        elif insn.isRtn():
                code += "\t%s_genRET_0();\n"%archMaster
        return code, callback

    def genImmValue(self, value):
        return "(h2_sValue_t) {VALUE, 'i', 1, 32, 0, (int)(%s)}"%(value)

    def getDestination (self, insn:H2Node):
        if insn.isVariable():
            return insn.getVariableName()
        elif insn.isR():
            return insn.getVariableName()
        elif insn.isOperator():
            if insn.hasVariableName():
                return insn.getVariableName()
            else:
                d = insn.getNodeType()
                regNro = insn.getRegister()
                arith = H2Type.typeCorrespondances[d['arith']]
                return "(h2_sValue_t) {REGISTER, '%s', %s, %s, %s, 0}"%(arith, d["vectorLen"], d["wordLen"], regNro)
        elif insn.isConst():
            d = insn.getNodeType()
            value = insn.getConstValue()
            arith = H2Type.typeCorrespondances[d['arith']]
            return "(h2_sValue_t) {VALUE, '%s', %s, %s, 0, %s}"%(arith, d["vectorLen"], d["wordLen"], value)

    def fatalError (self, msg):
        print ("Fatal error: %s"%msg)
        sys.exit(-1)

    def genTmpVarName(self):
        varName = "h2_%08d"%self.tmpVarNumber
        self.tmpVarNumber += 1
        return varName

    def getExpressionType(self, insn):
        return insn.sonsList[0].getVariableName()
