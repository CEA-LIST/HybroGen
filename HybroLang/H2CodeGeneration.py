#!/usr/bin/env python3

from HybroGen.GenGeneratorFromDb import GenGeneratorFromDb
from HybroLang.H2SymbolTable  import H2SymbolTable
from HybroLang.H2LabelTable   import H2LabelTable
from HybroLang.H2Node         import H2Node
from HybroLang.H2NodeType     import H2NodeType
from HybroLang.H2Type         import H2Type
from HybroLang.H2GenGen       import H2GenGen

class H2CodeGeneration:
    """Generate code generators from internal IR recursively on the one instruction syntax tree"""
    def __init__(self, IList, sTable, regTmp, regIn, lTable, args):
        """"""
        self.verbose = args.verboseBackend
        self.regTmp = regTmp
        if self.verbose:
            print("PASS : Code generation")
        self.insnCode = []
        self.archName  = args.arch[0]
        self.g = H2GenGen(args.arch[0])
        self.callbackCode = []
        self.regMask = 0xFFFFFFFF # Collect available register
        self.regMask = regTmp.getCMask(self.regMask) # From tmp bank
        self.regMask = regIn.getCMask(self.regMask)  # From in bank
        for i in range(len(IList)): # For all instructions, generate generators
            insn = IList[i]
            if self.verbose :
                print ("Insn %d before code generation : \n%s\n"%(i, insn))
            tmpCode, tmpCallbackCode = self.codeGeneration (insn, sTable, 0)
            # breakpoint()
            tmpRegReset = ["#ifdef H2_DEBUG_REGISTER",
                           'printf("Tmp registers mask reset\\n");',
                           "#endif // H2_DEBUG_REGISTER",
                           "h2_resetRegisterMasks();",
                           ]
            self.insnCode += tmpCode + tmpRegReset
            if len(tmpCallbackCode) > 1: # Avoid empty insn
                self.callbackCode += tmpCallbackCode
            if self.verbose :
                print("Generated code for insn %d:\n%s"%(i, tmpCode))
        self.initCode = [ # Initialisation code before codegeneration
 "/* Code Generation of %d instructions */"%len (IList),
 "/* Symbol table :*/\n%s"%(sTable.getCDecl()),
 "/* Label  table :*/\n%s"%(lTable.getCDecl()),
 "h2_asm_pc = (h2_insn_t *) ptr;",
 "h2_codeGenerationOK = true;",
 "h2_start_codeGen = h2_getticks();", # Start count ticks for code gen
 "h2_initRegisterMasks(0x%X, 0, 0, 0);"%(self.regMask),
 "h2_resetRegisterMasks();",
 "#ifdef H2_DEBUG_REGISTER",
 'printf("Tmp registers mask initialization\\n");',
 "#endif // H2_DEBUG_REGISTER",
        ]
        self.callBack = [                 # General pattern for the code generation
 "/* Call back code for loops */",
 "h2_save_asm_pc = h2_asm_pc;",] + self.callbackCode + [ 	  # Callback code for branch resolution
 "h2_asm_pc = h2_save_asm_pc;",
 "h2_end_codeGen = h2_getticks();", # Ends count ticks for code gen
 "h2_iflush(ptr, h2_asm_pc);",      # Possible d-cache flush
        ]

    def getCode (self):
        return self.g.formatCode(self.initCode) + self.g.formatCode(self.insnCode) + self.g.formatCode(self.callBack)

    def getDestination (self, insn:H2Node):
        if insn.isVariable():    return insn.getVariableName()
        elif insn.isR(): 	 return insn.sonsList[1].getVariableName()
        elif insn.isOperator():
            if insn.hasVariableName():
                return insn.getVariableName()
            else:
                d = insn.getOpType()
                regNro = insn.getRegister()
                t = H2Type(d['arith'], d['wordLen'], d['vectorLen'])
                arith = t.typeCorrespondances[d['arith']]
                return "(h2_sValue_t) {REGISTER, '%s', %s, %s, %s, %s, 0}"%(arith, d["vectorLen"], d["wordLen"], regNro, "false")
        elif insn.isConst(): # TODO différencier const et const expression
            d = insn.getOpType()
            value = insn.getConstValue()
            try:
                t = H2Type(d['arith'], d['wordLen'], d['vectorLen'])
                if len (d['arith']) > 1:
                    arith = t.typeCorrespondances[d['arith']]
                    t.t["arith"] = arith
            except: # Default for const expression
                t = H2Type("i", 32, 1)
            return self.g.genSValueFromType("H2VALUE", t, 0, value)

    def genTmpVarName(self):
        varName = "h2_%08d"%self.tmpVarNumber
        self.tmpVarNumber += 1
        return varName

    def getExpressionType(self, insn):
        return insn.sonsList[0].getVariableName()

    def codeGeneration(self, insn:H2Node, sTable, tab):
        """Recursively generate code generators"""
        code = [] # Instruction list for one node
        callback = []
        immValueZero = self.g.genImmValue(0) # TODO : optimize for const values
        for son in insn.sonsList: # Generate recursively code for sons first
            tmpCode, tmpCallback = self.codeGeneration (son, sTable, tab+1)
            code += tmpCode
            callback += tmpCallback
            # for grandSons in son: # Gather and free registers used at the level -1
            #     varName = grandSons.getVariableName()
            #     if varName != None and "tmp" in varName and 7 == len(varName) : # TODO change this test
            #         regsToBeFree += [varName]

        indentLevel = tab*"\t"
        self.g.setIndentLevel (tab)
        varName = insn.getVariableName()

        # Then for leaf instruction & operations with sons
        if insn.isOperator():
            insnSemName = insn.getSemName()
            if insnSemName in ["MV", "LUI"]:
                destReg = self.getDestination(insn.sonsList[0])
                srcR    = self.getDestination(insn.sonsList[1])
                if str(destReg) != str(srcR):
                    if self.archName == "aarch64":
                        code += self.g.codeGen3(insnSemName, destReg, srcR)
                    else:
                        code += self.g.codeGen2(insnSemName, destReg, srcR)
            elif insnSemName in ["INV", "NEG"]:
                destReg = self.getDestination(insn)
                src     = self.getDestination(insn.sonsList[0])
                code   += self.g.codeGen2(archMaster, insn.getSemName(), destReg, src)
            else:
                destReg = self.getDestination(insn)
                srcL    = self.getDestination(insn.sonsList[0])
                srcR    = self.getDestination(insn.sonsList[1])
                if self.archName in ("riscv",) and insnSemName in ("MUL", "DIV"):
                    code += self.g.codeGen4(insn.getSemName(), destReg, srcL, srcR, immValueZero)
                else:
                    code += self.g.codeGen3(insn.getSemName(), destReg, srcL, srcR)
        elif insn.isR():
            destReg = self.getDestination(insn.sonsList[0])
            srcReg  = self.getDestination(insn.sonsList[1])
            # invert src & dest as R/LD has format LD result, [addr]
            code   += self.g.codeGen3Inv(insn.getSemName(), srcReg, destReg)
        elif insn.isW():
            destReg = self.getDestination(insn.sonsList[0])
            srcReg  = self.getDestination(insn.sonsList[1])
            code   += self.g.codeGen3W(insn.getSemName(), destReg, srcReg, immValueZero)
        elif insn.isCmp():
            srcLeft  = insn.sonsList[0].getVariableName()  # TODO improve varorvalue handling
            srcRight = insn.sonsList[1].getVariableName()
            if None == srcRight: # In case where loop limit is a CONST
                srcRight = self.g.genImmValue(insn.sonsList[1].getConstValue())
                #val0 = "(h2_sValue_t) {H2VALUE, 'i', 1, 32, 0, 0}" # Hardwired 0
            code += self.g.codeGen2(insn.getSemName(), srcLeft, srcRight)
        elif insn.isBA(): # Branch always management
            reg0 = f"{indentLevel}(h2_sValue_t) {{H2REGISTER, 'i', 1, 32, 0, 0}}" # Hardwired 0
            if self.archName in ("power", "aarch64"):
                target = self.g.genImmValue ("(labelAddresses ["+insn.getTargetName()+"] - h2_asm_pc)")
                code += self.g.codeGen1W(insn.getSemName(), target)
                callback += [f'{indentLevel}h2_asm_pc = labelAddresses [%s];'%(insn.getSourceName())] # TODO not necessary if label defined before
                callback += self.g.codeGen1W(insn.getSemName(), target)
            elif  self.archName== "riscv":
                target = self.g.genImmValue ("(labelAddresses ["+insn.getTargetName()+"] - h2_asm_pc)*4")
                code += self.g.codeGen2("BA", reg0, target)
                callback += [f'{indentLevel}h2_asm_pc = labelAddresses [%s];'%(insn.getSourceName())] # TODO not necessary if label defined before
                callback += self.g.codeGen2("BA", reg0, target)
        elif insn.isBcc(): # Conditionnal branch management
            branchCond = str(insn.nodeType).split (".")[1]
            if self.archName in ("power", "aarch64"):
                target = self.g.genImmValue ("(labelAddresses ["+insn.getTargetName()+"] - h2_asm_pc)")
                code += self.g.codeGen1W(insn.getSemName(), target)               # Generate dummy branch insn
                callback += [f'{indentLevel}h2_asm_pc = labelAddresses [%s] + 1;'%(insn.getSourceName())] # Get bactracked addresss
                callback += self.g.codeGen1W(insn.getSemName(), target)                        # (re)Generate branc instruction
            else:
                target = self.g.genImmValue ("(labelAddresses ["+insn.getTargetName()+"] - h2_asm_pc)*4")
                srcLeft  = insn.sonsList[0].getVariableName()  # TODO improve varorvalue handling
                srcRight = insn.sonsList[1].getVariableName()
                if None == srcRight: # In case where loop limit is a CONST
                    srcRight = self.g.genImmValue(insn.sonsList[1].getConstValue())
                code += self.g.codeGen3(branchCond, srcLeft, srcRight, target)
                callback += [f'{indentLevel}h2_asm_pc = labelAddresses [%s];'%(insn.getSourceName())] # TODO not necessary if label defined before
                callback += self.g.codeGen3(branchCond, srcLeft, srcRight, target)
        elif insn.isLabel():
            code += self.g.codeGen1W(insn.getSemName(), insn.getLabelName())
        elif insn.isRtn():
            # code += self.calleeSaveRestore(list(range(9, 28)))
            code += self.g.codeGen0W("RET")
        else:
            if self.verbose:
                print ("No code to generated for this node %s"%insn)
                # print(code)

        regsToBeFree = []
        for sons in insn.sonsList:
            varName = sons.getVariableName()
            if varName != None and "tmp" in varName and 7 == len(varName) and not insn.isR(): # i.e. varName = tmp000xxx
                regsToBeFree += [varName]
        for r in regsToBeFree:
            indent = tab*"\t"
            regIndice = int(r[4:])
            varName = insn.getVariableName()
            if None != varName :
                code += [f"{indent}if (!{varName}.dontFree) h2_freeReg({r}.regNro);"]
        return code, callback

if __name__ == "__main__":
    print (__name__)
