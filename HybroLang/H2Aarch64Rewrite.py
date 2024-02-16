#!/usr/bin/env python3

import random
import sys
from enum import Enum
from H2Utils import *
from HybroLang.H2SymbolTable import H2SymbolTable
from HybroLang.H2LabelTable  import H2LabelTable
from HybroLang.H2Node  import H2Node
from HybroLang.H2NodeType  import H2NodeType

class H2Aarch64Rewrite():

    def __init__(self, platform, instructionList, verbose):
        if platform != "aarch64":
            fatalError ("H2Aarch64Rewrite called for %s"%platform)
        if verbose:
            print("H2Aarch64Rewrite pass")
        self.archName = platform
        self.oldList = instructionList
        self.newList = []
        self.rewriteInsn()
        if verbose :
            print("IR after H2Aarch64Rewrite pass")
            for i in range(len(self.newList)):
                print ("%d:%s\n"%(i, self.newList[i]))

    def rewriteInsn(self):
        for insn in self.oldList :
            self.newList += self.createCMPandBCC (insn)
        self.loadOptimize()
        # More to come !

    def getNewInsnList(self):
        return self.newList

    def createCMPandBCC (self, initialBCC):
        """ Filter a BCC instruction (compare and branch) and rewrite it on a sequence of CMP + BCC nodes"""
        i = initialBCC
        if i.isB() and i.hasTargetName() and i.hasSourceName() and not i.isBA():
            # print ("Add cmp")
            cmpNode = H2Node (H2NodeType.CMP, sonsList = i.sonsList)
            bccNode = H2Node (i.nodeType, opName = i.getOpName(), targetName = i.getTargetName(), sourceName = i.getSourceName())
            return [cmpNode, bccNode]
        else:
            return [initialBCC]
    
    def loadOptimize(self):
        for i in range(0, len(self.oldList)):
            new = self.oldList[i]
            #print("Node :", str(i) + "\n", new)
            if new.isOperator() and self.archName == "aarch64" and new.sonsList[1].isR() and new.isVector() :
                #print("Node avant transforamtion :", str(i) + "\n", new)
                new.sonsList[1] = new.sonsList[1].sonsList[0].sonsList[0]
                new.nodeType = H2NodeType.R
                new.opName = "R"
                #print("Node apres transformation :\n", new)