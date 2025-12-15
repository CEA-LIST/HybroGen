#!/usr/bin/env python3

import random
import sys
from enum import Enum
from H2Utils import *
from HybroLang.H2SymbolTable import H2SymbolTable
from HybroLang.H2LabelTable  import H2LabelTable
from HybroLang.H2Node  import H2Node
from HybroLang.H2NodeType  import H2NodeType

class H2RiscvRewrite():

    def __init__(self, platform, instructionList, verbose):
        if platform != "riscv":
            fatalError ("H2RiscvRewrite called for %s"%platform)
        if verbose:
            print("H2RiscvRewrite pass")
        self.archName = platform
        self.oldList = instructionList
        self.newList = []
        self.rewriteInsn(verbose=verbose)
        if verbose :
            print("IR after H2RiscvRewrite pass")
            for i in range(len(self.newList)):
                print ("%d:%s\n"%(i, self.newList[i]))

    def rewriteInsn(self, verbose):
        for insn in self.oldList :
            self.newList += self.createVSET (insn, verbose)

    def getNewInsnList(self):
        return self.newList

    def createVSET (self, VectorOp, verbose):
        """ Filter a vector instruction and rewrite it on a sequence of vset + vector operation nodes"""
        i = VectorOp
        if i.isOperator() and i.opType['vectorLen'] != "1":
            vsetNode = H2Node(H2NodeType.VCONF, opType=i.opType)
            if verbose :
                print("Adding a VCONF node before the current node...")
                print("VCONF node :", vsetNode)
                print("Current node : ", i)
            return [vsetNode, VectorOp]
        else:
            return [VectorOp]
    