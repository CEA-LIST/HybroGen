#!/usr/bin/env python3

from HybroLang.H2Debug import    H2Debug
from HybroLang.H2Node import     H2Node
from HybroLang.H2NodeType import H2NodeType
from HybroLang.H2Type import     H2Type

class H2RegAllocTmp():
    """Register allocation for temporarie

    Allocate temporaries at leaf level, let the register propagate
    with the code generator

    This register allocation is virtual, the real register allocation
    will be done at code generationi time
    """
    def __init__(self, IList, sTable, regTmp, regIn, args):
        if args.verboseBackend:
            print("PASS : reg alloc for temps")
        self.oldList = IList
        self.sTable = sTable
        self.regTmp = regTmp
        self.doShowTree = args.graphviz
        self.archName  = args.arch[0]
        # print (regIn)
        # print (regTmp)

    def getNewList(self):
        newList = []
        for i in self.oldList:
            newList += [self.genTemps (i)]
        if self.doShowTree:
            debug = H2Debug()
            debug.showTree(self.archName+": after regAlloc tmp", newList)
        return newList

    def getSonType(self, Insn):
        theType = Insn.getOpType()
        if None == theType and Insn.isVariable():
            theType = self.sTable.get(Insn.getVariableName())
        return theType

    def broadcastType(self, typeL, typeR):
        # Propagate leaf data type to the top
        if type(typeL['wordLen']) is str: # Prefer "dynamic" type aka defined by instructions
            localType = typeL
        elif type(typeR['wordLen']) is str:
            localType = typeR
        elif typeL['wordLen'] == typeR['wordLen']:
            localType = typeL
        else:
            print ("Warning incompatibles type size")
        return localType

    def genTemps(self, Insn):
        """ Recursive descent to find temporary at node level.
        """
        for sons in Insn.sonsList : # Descent first
            self.genTemps(sons)
            # self.sTable.resetTemps("i")
        if Insn.isOperator() and None == Insn.getRegister():
            if None == Insn.getOpType(): # A node without type
                # Propagate leaf data type to the top
                typeL = self.getSonType(Insn.sonsList[0])
                typeR = self.getSonType(Insn.sonsList[1])
                localType = self.broadcastType(typeL, typeR)
                Insn.setOpType(localType)
                Insn.setVariableName(self.sTable.getTemps(localType))
            else:
                # For all non terminal node, alloc register
                if Insn.getVariableName() != "h2_outputVarName":
                    localType = Insn.getOpType()
                    Insn.setVariableName(self.sTable.getTemps(localType))
        else: # Compare types
            if Insn.isW(): # For a store : force the right part dataType to the variable datatype
                typeN = Insn.getOpType()
                localType = H2Type(typeN["arith"], typeN["wordLen"], typeN["vectorLen"])
                localType.t["arith"] = localType.typeCorrespondances[typeN["arith"]]
                Insn.sonsList[1].setOpType(localType)
            elif Insn.isR(): # For a load : add destination register
                previousName = Insn.getVariableName()
                localType = Insn.getOpType()
                if None == previousName:
                    tmpName = self.sTable.getTemps(localType)
                    Insn.setVariableName(tmpName)
                else:
                    tmpName = previousName
                Insn.sonsList.append(H2Node(H2NodeType.VARIABLE, variableName = tmpName, opType = localType))
        return Insn
