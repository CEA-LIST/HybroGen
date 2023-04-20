#!/usr/bin/env python3

from enum import Enum
from HybroLang.H2SymbolTable import H2SymbolTable
from HybroLang.H2LabelTable  import H2LabelTable
from HybroLang.H2Node  import H2Node
from HybroLang.H2NodeType  import H2NodeType

class H2KalrayRewrite():

    def __init__(self, archname, instructionList, verbose):
        if verbose:
            print("H2KalrayRewrite pass")
        self.archName = archname
        self.oldList = instructionList
        self.newList = []
        for i in self.oldList :
            self.newList += self.rewriteInsn(i)
        if verbose :
            print("IR after H2KalrayRewrite pass")
            for i in range(len(self.newList)):
                print ("%d:%s\n"%(i, self.newList[i]))

    def getNewInsnList(self):
        return self.newList

    def rewriteInsn(self, insn):
        if self.archName != "kalray":
            return [insn]
        i = [insn]
        if (insn.isOperator()):
            #son[0] -> destination, son[1] -> operator
            op = insn.sonsList[1]
            if op.isOperator():
                i = [self.rewriteOperator(insn)]
        elif insn.isB():
            i = self.createCMPandBCC(insn)
        return i

    def rewriteOperator(self, insn):
        """ Filter a oprator intruction and rewrite : DIV, SUB float"""
        if insn == None:
            return None
        for i, son in enumerate(insn.sonsList):
            newSon = self.rewriteOperator(son)
            insn.sonsList.pop(i)
            insn.sonsList.insert(i, newSon)
        if insn.isOperator():
            if insn.getSemName() == "DIV":
                invNode = H2Node(H2NodeType.OPERATOR, sonsList = [insn.sonsList[1]], opName="INV", opType = insn.getOpType())
                mulNode = H2Node(H2NodeType.OPERATOR, opType = insn.getOpType(), sonsList = [insn.sonsList[0], invNode], opName= "*")
                return mulNode
            elif insn.getSemName() == "SUB" and insn.getOpType()['arith'] == 'flt':
                negNode = H2Node(H2NodeType.OPERATOR, sonsList = [insn.sonsList[1]], opName="NEG", opType = insn.getOpType())
                addNode = H2Node(H2NodeType.OPERATOR, opType = insn.getOpType(), sonsList = [insn.sonsList[0], negNode], opName= "+")
                return addNode
        return insn

    def createCMPandBCC (self, initialBCC):
        """ Filter a BCC instruction (compare and branch) and rewrite it on a sequence of CMP + BCC nodes"""
        i = initialBCC
        if i.hasTargetName() and i.hasSourceName():
            nodeType = i.nodeType
            if nodeType == H2NodeType.BGE:
                cmpNode = H2Node (H2NodeType.CMPLE, sonsList = i.sonsList)
            elif nodeType == H2NodeType.BGT:
                cmpNode = H2Node (H2NodeType.CMPLT, sonsList = i.sonsList)
            elif nodeType == H2NodeType.BLE:
                cmpNode = H2Node (H2NodeType.CMPGE, sonsList = i.sonsList)
            elif nodeType == H2NodeType.BLT:
                cmpNode = H2Node (H2NodeType.CMPGT, sonsList = i.sonsList)
            elif nodeType == H2NodeType.BNE:
                cmpNode = H2Node (H2NodeType.CMPEQ, sonsList = i.sonsList)
            elif nodeType == H2NodeType.BEQ:
                cmpNode = H2Node (H2NodeType.CMPNE, sonsList = i.sonsList)

            bccNode = H2Node (H2NodeType.BNEZ, opName = i.getOpName(), targetName = i.getTargetName(), sourceName = i.getSourceName())
            return [cmpNode, bccNode]
        else:
            return [initialBCC]
