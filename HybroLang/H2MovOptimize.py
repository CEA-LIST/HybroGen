#!/usr/bin/env python3

class H2MovOptimize():
    ''' Optimize mov to the previous instruction tree'''

    def __init__(self, insnList, sTable, verbose):
        self.oldList = insnList
        self.sTable = sTable
        self.newList = []
        if 1 != len(self.oldList):
            self.doMovOptimize()
        else:
            self.newList = self.oldList
        if verbose:
            print ("Mov optimize from old %d insn to new %d insn"%(len (self.oldList), len (self.newList)))
            for i in range(len(self.newList)):
                print("%d : %s \n"%(i, self.newList[i]))

    def areVariableSimilar(self, nodeA, nodeB):
        if nodeA.isVariable() and nodeB.isVariable() and nodeA.getVariableName() == nodeB.getVariableName():
            nodeAtype = self.sTable.get(nodeA.getVariableName())
            nodeBtype = self.sTable.get(nodeB.getVariableName())
            if nodeAtype['wordLen'] == nodeBtype['wordLen'] and nodeAtype['vectorLen'] == nodeBtype['vectorLen']:
                return True
        return False

    def  doMovOptimize(self):
        """Window optimization : if current operation is simple mv, place the
        dest register in the source reg of the preceding tree
        """
        current = self.oldList[0]
        i = 1
        while i < len(self.oldList):
            new  = self.oldList[i]
            if new.isOperator () and new.getOpName() == "=" and len(new.sonsList) > 1 and len(current.sonsList) > 1:
                destNode = new.sonsList[0]
                srcNode  = new.sonsList[1]
                replacedNode = current.sonsList[0]
                # print("Optimize opportunity %s <- %s"%(destNode.getVariableName(), srcNode.getVariableName()))
                # print(" %s %s "%(current.sonsList[0].getVariableName(),srcNode.getVariableName()))
                if self.areVariableSimilar(replacedNode, srcNode):
                    # destNode.setOpType (srcNode.getOpType ()) # Should we transfert datatype ?
                    current.sonsList[0] = destNode
                    self.newList += [current]
                    i += 1
                    current = self.oldList[i]
                else:
                    self.newList += [current]
                    current = new
            else:
                self.newList += [current]
                current = new
            i += 1
        self.newList += [current]

    def getNewInsnList(self):
        return self.newList
