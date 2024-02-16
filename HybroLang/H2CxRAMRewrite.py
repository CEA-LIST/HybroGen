#!/usr/bin/env python3

# IsaDb Structures and Methods
from HybroGen.IsaDb  import IsaDb
from HybroGen.Insn import Insn
from HybroGen.ProxyDb import *

# H2IR2 SStructures and Methods
from H2Utils import *
from HybroLang.H2LabelTable import H2LabelTable
from HybroLang.H2SymbolTable import H2SymbolTable
from HybroLang.H2Node import H2Node
from HybroLang.H2IR2 import H2Type
from HybroLang.H2RegisterBank import H2RegisterBank
from HybroLang.H2NodeType import H2NodeType

import random
import sys
from enum import Enum
from collections import OrderedDict

opType = H2Type ("int", "32", "1")
supportedArith = (
    ("int[]", 16, 8), ("int[]", 8, 16), ("int[]", 32, 4),
    ("sint[]", 16, 8), ("sint[]", 8, 16), ("sint[]", 32, 4),
    ("int[]", 128, 1),
)
class H2CxRAMRewrite():
    """
    The H2CxRAMRewrite pass converts every vector operation into C-SRAM instructions,
    further improvement will be implemented later on (^_^) Let's do our best !
    --- Kevin Mambu, CEA Grenoble, 2020
    """
    def __init__(self, platform: dict, lTable: H2LabelTable, sTable: H2SymbolTable, regTmp: H2RegisterBank, regIn: H2RegisterBank,  verbose=False, dbIds = None):

        self.verbose = verbose
        arch = platform["arch"]
        extension = platform["extension"]
        self.archName = arch[1] if len(arch) > 1 else None
        self.extList = extension[1] if len(extension) > 1 else None

        self.invalid_platform = False

        self.sTable = sTable
        self.regTmp = regTmp
        self.lTable = lTable
        self.regIn = regIn

        db = ProxyDb(dbIds["host"], dbIds["dbname"], dbIds["user"], dbIds["pwd"])
        isa = IsaDb(db, "cxram", None)
        self.insnLenList = isa.getWordSizeFromDb()
        self.insnLenList.sort()
        self.insnList = isa.getInsnList()
        # for i in  self.insnList:
        #     print ("%10s/%4d/%4d"%(i["semname"], i["wordlen"], i["vectorlen"]))
        self.csram_insns = list()
        self.nb_csram_insns = 0
        self.csram_variables = list()
        self.prologueBlock = list()
        self.prologueName = self.lTable.genLabelName("csram")
        self.prologueLabel = H2Node(H2NodeType.LABEL, labelName=self.prologueName)
        self.iteratorsStack = list()

    def createConstNode(self, n, str=0):
        global opType
        if str :
            node = H2Node(H2NodeType.CONST, constValue=n, opType=opType)
        else:
            node = H2Node(H2NodeType.CONST, constValue=hex(n), opType=opType)
        return node

    def createVariableNode(self, n):
        global opType
        node = H2Node(H2NodeType.VARIABLE, variableName=n, opType=opType)
        return node

    def createOrNode(self, op1, op2):
        global opType
        node = H2Node(H2NodeType.OPERATOR, sonsList=[op1, op2], opType=opType, opName="OR")
        return node

    def createLuiNode(self, op1, op2):
        global opType
        node = H2Node(H2NodeType.OPERATOR, sonsList=[op1, op2], opType=opType, opName="LUI")
        return node

    def createAndNode(self, op1, op2):
        global opType
        node = H2Node(H2NodeType.OPERATOR, sonsList=[op1, op2], opType=opType, opName="AND")
        return node

    def createSubNode(self, op1, op2):
        global opType
        node = H2Node(H2NodeType.OPERATOR, sonsList=[op1, op2], opType=opType, opName="-")
        return node

    def createSlNode(self, op1, op2):
        global opType
        node = H2Node(H2NodeType.OPERATOR, sonsList=[op1, op2], opType=opType, opName="SL")
        return node

    def createSrNode(self, op1, op2):
        global opType
        node = H2Node(H2NodeType.OPERATOR, sonsList=[op1, op2], opType=opType, opName="SR")
        return node

    def createAddNode(self, op1, op2):
        global opType
        node = H2Node(H2NodeType.OPERATOR, sonsList=[op1, op2], opType=opType, opName="+")
        return node

    def createAssignNode(self, var, val):
        global opType
        node = H2Node(H2NodeType.OPERATOR, sonsList=[var, val], opType=opType, opName="=")
        return node

    def query(self, opType, wordLen, vectorLen, format_):
        # print ("%s %s %s %s"%(opType, wordLen, vectorLen, format_))
        for insn in self.insnList:
            # print ("\t%s %s %s %s"%(insn['name'].upper(),insn['wordlen'], insn['vectorlen'], insn['parameters']))
            opOK        = insn['name'].upper() == opType
            wordLenOK   = insn['wordlen']      == wordLen
            vectorLenOK = insn['vectorlen']    == vectorLen
            formatOK    = insn['parameters']   == format_
            #extOK       = insn['extension'].replace(".","_") in self.extList
            if opOK and wordLenOK and vectorLenOK and formatOK:
                return insn
        return None

    def logicalAddressToPhysical(self, addr_node):
        c4    = self.createConstNode(0x4)
        base = self.createVariableNode('base')
        mask  = self.createSubNode(addr_node, base)
        shft  = self.createSrNode(mask, c4)
        return shft

    def baseAddrToRegister(self):
        baseNode = self.createVariableNode('base')
        zeroNode = self.createConstNode(0x0)
        constNode = self.createConstNode('((CXRAM_BASE_ADDR) >> 12)',str=1)
        andNode = self.createAndNode(baseNode, zeroNode)
        node1 = self.createAssignNode(baseNode, andNode)
        node2 = self.createLuiNode(baseNode, constNode)
        self.prologueBlock += [node1]
        self.prologueBlock += [node2]

    def setNmcEnableAndOpcode(self, opcode):
        return self.createConstNode(opcode << 18)

    def setDestField(self, insn, dest):
        c2 = self.createConstNode(2)
        shift = self.createSlNode(dest, c2)
        return self.createOrNode(insn, shift)

    def setSrc2Field(self, src2):
        c16 = self.createConstNode(16)
        return self.createSlNode(src2, c16)

    def setImm16Field(self, imm16):
        return self.setSrc2Field(imm16)

    def setSrc1Field(self, insn, src1):
        return self.createOrNode(src1, insn)

    def setImm32Field(self, value):
        return value

    def genW(self, addr, val):
        c0 = self.createConstNode(0)
        node = H2Node(H2NodeType.W, sonsList=[addr, val, c0], opType=opType, opName="W")
        return node

    def trace (self, mesg):
        if self.verbose:
            print (mesg)

    def transformInsn(self, opcode, dest, src2=None, imm16=None, imm32=None, src1=None):
        try:
            if imm32 is not None:
                assert src2 is None and src1 is None and imm16 is None
            if src2 is not None or src1 is not None or imm16 is not None:
                assert imm32 is None
        except AssertionError as e:
            print("Error : discrepancy in arguments passed to transformInsn :")
            print("src2  :")
            print(src2)
            print("src1  :")
            print(src1)
            print("imm16 :")
            print(imm16)
            print("imm32 :")
            print(imm32)
            raise
        global opType
        ret = list()
        # Update of the 'dest' argument
        dest_var : H2Node = dest.sonsList[0]
        dest_idx : H2Node = dest.sonsList[1].sonsList[0]
        if not self.csram_variables:
            # node = self.baseAddrToRegister()
            # self.prologueBlock += [node]
            self.baseAddrToRegister()
        if dest_var.getVariableName() not in self.csram_variables:
            node = self.createAssignNode(dest_var, self.logicalAddressToPhysical(dest_var))
            self.prologueBlock += [node]
            self.csram_variables += [dest_var.getVariableName()]
            self.sTable.symbolTable[dest_var.getVariableName()] = opType
        dest = self.createAddNode(dest_var, dest_idx)
        # Update of the 'src2' argument
        try:
            src2_var : H2Node = src2.sonsList[0]
            src2_idx : H2Node = src2.sonsList[1].sonsList[0]
            if src2_var.getVariableName() not in self.csram_variables:
                node = self.createAssignNode(src2_var, self.logicalAddressToPhysical(src2_var))
                self.prologueBlock += [node]
                self.csram_variables += [src2_var.getVariableName()]
                self.sTable.symbolTable[src2_var.getVariableName()] = opType
            src2 = self.createAddNode(src2_var, src2_idx)
        except:
            pass
        # Update of the 'src1' argument
        try:
            src1_var : H2Node = src1.sonsList[0]
            src1_idx : H2Node = src1.sonsList[1].sonsList[0]
            if src1_var.getVariableName() not in self.csram_variables:
                node = self.createAssignNode(src1_var, self.logicalAddressToPhysical(src1_var))
                self.prologueBlock += [node]
                self.csram_variables += [src1_var.getVariableName()]
                self.sTable.symbolTable[src1_var.getVariableName()] = opType
            src1 = self.createAddNode(src1_var, src1_idx)
        except:
            pass
        # Generation of AAA instructions
        if imm32 is None and imm16 is None:
            new_insn = self.genW(
                self.setDestField(
                    self.setNmcEnableAndOpcode(opcode),
                    dest),
                self.setSrc1Field(
                    self.setSrc2Field(src2),
                    src1))
        # Generation of AAI instructions
        elif imm32 is None:
            new_insn = self.genW(
                self.setDestField(
                    self.setNmcEnableAndOpcode(opcode),
                    dest),
                self.setSrc1Field(
                    self.setImm16Field(src2),
                    src1))
        # Generation of AI instructions
        else:
            new_insn = self.genW(
                self.setDestField(
                    self.setNmcEnableAndOpcode(opcode),
                    dest),
                self.setImm32Field(imm32))
        return [new_insn]

    def print(self, s):
        print("[H2CxRAMRewrite] %s" % str(s)) if self.verbose else None

    def isInsnCompatible(self, insn):
        global opType
        if self.archName != "cxram":
            self.print("Exiting, target heterogeneous architecture is not CxRAM")
            return False
        if self.extList is None:
            self.print("Exiting, no extensions to use were specified")
            return False
        if not insn.isW():
            self.print("Exiting, instruction root is not 'W'")
            return False
        arith     = insn.opType["arith"]
        wordLen   = insn.opType["wordLen"]
        vectorLen = insn.opType["vectorLen"]
        try:
            wordLen   = int(wordLen)
            vectorLen = int(vectorLen)
        except ValueError as ex:
            fatalError("Exiting, dynamically parameterable types are not supported (%s, %s, %s)" % (str(arith), str(wordLen), str(vectorLen)))
            return False
        dest = insn.sonsList[0]
        # print ("H2CxRAMRewrite: %s %s %s"%(arith, wordLen, vectorLen))
        if (arith, wordLen, vectorLen) not in supportedArith :
            fatalError("Exiting, data type %s %d %d is not supported on the CxRAM architecture" % (arith, wordLen, vectorLen))
            return False

        op = insn.sonsList[1]
        self.print("Instruction is compatible")
        return True

    def countCsramInstructions(self, IList: list):
        for insn in IList:
            if self.isInsnCompatible(insn):
                self.nb_csram_insns += 1
                self.csram_insns += [insn]
        return None

    def rewriteInsn(self, insn):
        if not self.isInsnCompatible(insn):
            return [insn]
        dest          = insn.sonsList[0]
        rhs           = insn.sonsList[1]
        src2_or_imm16 = None
        src1          = None
        imm32         = None
        src2          = None
        imm16         = None

        arith         = insn.opType["arith"]
        wordLen       = int(insn.opType["wordLen"])
        vectorLen     = int(insn.opType["vectorLen"])

        if not rhs.isOperator():
            if rhs.isR():
                vectorLenOK = int(rhs.opType['vectorLen']) == vectorLen
                arithOK = (rhs.opType['arith'] + "[]") == arith
                wordLenOK = int(rhs.opType['wordLen']) == wordLen
            if rhs.isR() and vectorLenOK and wordLenOK:
                vectorLen = 1
                wordLen = 128
                imm16 = self.createConstNode(0)
                src1 = rhs.sonsList[0]
                semName = "COPY"
            else:
                imm32   = rhs
                semName = "BCAST"
        else:
            src1          = rhs.sonsList[0].sonsList[0]
            if len(rhs.sonsList) == 1:
                imm16 = self.createConstNode(0)
            elif rhs.sonsList[1].isConst():
                imm16 = rhs.sonsList[1]
            else:
                src2  = rhs.sonsList[1].sonsList[0]
            semName = rhs.getSemName()
            if semName == "SL":
                semName = "SLLI"
            elif semName == "SR":
                semName = "SRLI"
            elif semName == "MUL":
                semName = "MULLO"

        if src2 is not None:
            format_ = "aaa"
        elif imm16 is not None:
            format_ = "aia"
        else:
            format_ = "ai"

        # Preparation of the query to the IsaDb InsnList
        dest_opType = self.sTable.get(dest.sonsList[0].variableName)
        # Use saturated arithmetic operators if specified
        # semName += "S" if dest_opType['arith'][0:4] == "sint" else ""
        insn_entry = self.query(semName, wordLen, vectorLen, format_)
        if insn_entry is None:
            fatalError("Operation '%s/%d/%d' (%s) not supported in CxRAM" % (semName, wordLen, vectorLen, format_.upper()))
        opcode = int(insn_entry['encoding'][0]['name'], 2)

        new_insns = self.transformInsn(opcode, dest,
                src2=src2, src1=src1, imm32=imm32, imm16=imm16)
        return new_insns

    def rewriteInsns(self, IList: list):
        if self.archName is None:
            self.print("No CxRAM architecture detected, aborting")
            return IList
        res = list()
        # Analysis / Transformation step
        self.countCsramInstructions(IList)
        if self.nb_csram_insns == 0:
            return IList
        self.trace("Found %d instructions" % self.nb_csram_insns)
        for insn in self.csram_insns:
            self.print(insn)
        insn: H2Node
        for idx, insn in enumerate(IList):
            if insn.isBcc():
                res += [insn]
                self.iteratorsStack += [insn.sonsList[0].getVariableName()]
            elif insn.nodeType == H2NodeType.BA:
                res += [insn]
                self.iteratorsStack = self.iteratorsStack[:-1]
            else:
                res += self.rewriteInsn(insn)
        # Post-transformation / Finish step
        prologue_indices = list()
        resume_index = 0
        res = [self.prologueLabel] + self.prologueBlock + res
        return res
