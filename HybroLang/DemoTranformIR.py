#!/usr/bin/env python3

from HybroLang.HybroLangLexer    import HybroLangLexer
from HybroLang.HybroLangParser   import HybroLangParser
from HybroLang.HybroLangVisitor  import HybroLangVisitor
from HybroLang.H2RegisterBank    import H2RegisterBank
from HybroLang.H2SymbolTable     import H2SymbolTable
from HybroLang.H2LabelTable      import H2LabelTable
from HybroLang.H2IR2             import *



archName = "POWER"

def createCMPandBCC (initialBCC):
    i = initialBCC
    if i.isB() and i.hasTargetName() and i.hasSourceName() and archName == "POWER":
        cmpNode = H2Node (H2NodeType.CMP, sonsList = i.sonsList)
        bccNode = H2Node (i.nodeType, opName = i.getOpName(), targetName = i.getTargetName(), sourceName = i.getSourceName())
        return [cmpNode, bccNode]
    else:
        print("Failed transformation")
        sys.exit(0)

def createCMPNode(opName, variableName, constValue, labelEnd, labelBegin):
    var =    H2Node (H2NodeType.VARIABLE, variableName = variableName)
    limite = H2Node (H2NodeType.CONST, constValue = constValue)
    bcc = H2Node (H2NodeType.BNE, opName = opName, sonsList = [var, limite])
    bcc.setTargetName(labelEnd)
    bcc.setSourceName(labelBegin)
    return bcc

if __name__ =="__main__":
    import sys
    a = createCMPandBCC(createCMPNode("==", "i", 42, "LabelEnd", "LabelBegin"))
    print(a[0])
    print(a[1])
    a = createCMPandBCC(createCMPNode("==", "i", 42, None, "LabelBegin"))
    print(a)
