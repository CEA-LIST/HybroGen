#!/usr/bin/env python3

from HybroLang.H2Debug import    H2Debug
from HybroLang.H2Node import     H2Node
from HybroLang.H2NodeType import H2NodeType
from HybroLang.H2Type import     H2Type

class H2RegCSI():
    """Common sub expression identification / reg allocation.

    * Identify common sub expression in the tree. For now identify
    (R (+ (var const)))
    * Keep one and allocate a fixed register
    * Prune other sub expression by replacing the fixed register

    """
    def __init__(self, IList, sTable, regTmp, regIn, args):
        if args.verboseBackend:
            print("PASS : reg alloc for common sub expressions")
        self.oldList = IList
        self.sTable = sTable
        self.regTmp = regTmp
        self.doShowTree = args.graphviz
        self.archName  = args.arch[0]
        self.commonSubTrees = [] # List of subtree
        self.commonRegister = [] # Allocated registers
        for subTree in IList: self.idCaptureCommonRead(subTree)	# Collect common sub expressions
        for commonSub in self.commonSubTrees: 			# Allocate register in "in" bank
            self.commonRegister += [regIn.getNextRegister("int")]
        self.alreadyDone = [False] * len (self.commonRegister)
        # for idx, subTree in enumerate(self.commonSubTrees):
        #     print ("%d READ %s[%s] reg %d"%(idx, subTree.sonsList[0].getVariableName(), subTree.sonsList[1].getConstValue(), self.commonRegister[idx]))
        new = []
        for subTree in IList:
            # print ("Before", subTree)
            new = self.allocateRegAndPrune(subTree) #
            # print ("After", new)

    def isNodeReadArray(self, insn:H2Node):
        """ Identify a node as  (R (+ (var const)))"""
        if not insn.isR(): return False
        if not insn.sonsList[0].isOperator(): return False
        if not insn.sonsList[0].getOpName() == "+": return False
        if not insn.sonsList[0].sonsList[0].isVariable(): return False
        if not insn.sonsList[0].sonsList[1].isConst(): return False
        return True

    def allocateRegAndPrune (self, subTree:H2Node):
        if not self.isNodeReadArray(subTree): # Not on a Read node : copy & recurse
            for idx, sons in enumerate(subTree.sonsList) : # Descent first
                subTree.sonsList[idx] = self.allocateRegAndPrune(sons)
            return subTree
        else:	# On a READ subnode ?
            i = self.idAlreadySeen(subTree) # Get id of identidied subTree
            arrayName = subTree.sonsList[0].sonsList[0].getVariableName()
            constValue = subTree.sonsList[0].sonsList[1].getConstValue()
            vName = "READ_%s_%s"%(arrayName, constValue)
            if not self.alreadyDone[i]: # Seen the first time = allocate register & create variable
                subTree.setRegister(self.commonRegister[i])
                subTree.setVariableName(vName)
                self.alreadyDone[i] = True
                self.sTable.add (vName, subTree.getOpType (), self.commonRegister[i])
                return subTree 	# Unchanged subtree with reg allocation
            else: 		# Prune the subTree & replace by register value
                                # Create a dummy variable containing the previously loaded variable
                n = H2Node(H2NodeType.VARIABLE, variableName=vName, opType = subTree.getOpType())
                return n # Replace subTree by new variable

    def idAlreadySeen(self, insn):
        """ Identify a node as  (R (+ (var const)))"""
        varName    = insn.sonsList[0].sonsList[0].getVariableName()
        constValue = insn.sonsList[0].sonsList[1].getConstValue()
        for idx, seen in enumerate(self.commonSubTrees):
            localVarName    = seen.sonsList[0].getVariableName()
            localConstValue = seen.sonsList[1].getConstValue()
            if localVarName == varName and localConstValue == constValue:
                return idx
        return -1

    def idCaptureCommonRead(self, subTree):
        """ Recursive descent to find common read
        """
        for sons in subTree.sonsList : # Descent first
            self.idCaptureCommonRead(sons)
        if self.isNodeReadArray(subTree) and -1 == self.idAlreadySeen(subTree):
            self.commonSubTrees += subTree
