#!/usr/bin/env python3

import copy

class H2WindowRewrite():
    ''' Optimize mov on the flat IR
    Replace :
86 H2NodeType.OPERATOR: =: {'arith': 'int', 'wordLen': '32', 'vectorLen': '1'}
	H2NodeType.VARIABLE: h2_00000127
	H2NodeType.CONST: 16: {'arith': 'int', 'wordLen': '32', 'vectorLen': '1'}

87 H2NodeType.OPERATOR: =: {'arith': 'int', 'wordLen': '32', 'vectorLen': '1'}
	H2NodeType.VARIABLE: h2_00000127
	H2NodeType.OPERATOR: SL: {'arith': 'int', 'wordLen': '32', 'vectorLen': '1'}
		H2NodeType.VARIABLE: h2_00000126
		H2NodeType.VARIABLE: h2_00000127
by

86 H2NodeType.OPERATOR: =: {'arith': 'int', 'wordLen': '32', 'vectorLen': '1'}
	H2NodeType.VARIABLE: h2_00000127
	H2NodeType.OPERATOR: SL: {'arith': 'int', 'wordLen': '32', 'vectorLen': '1'}
		H2NodeType.VARIABLE: h2_00000126
		H2NodeType.CONST: 16: {'arith': 'int', 'wordLen': '32', 'vectorLen': '1'}

Gain 1 instruction & (1 physical register)
'''

    def __init__(self, insnList, archName, verbose):
        self.oldList = insnList
        self.archName = archName
        self.newList = []
        self.optimizeCount = 0
        self.doMoveOptimize()
        if verbose:
            print ("Window Rewrite : insn len before %d / after %d (gain %d insn)"%(len(self.oldList), len(self.newList), self.optimizeCount))

    def isMovConst(self, insn):
        return insn.isOperator() and "=" == insn.getOpName() and insn.sonsList[1].isConst()

    def isOpWithVar(self, insn):
        return insn.isOperator() 	 \
            and 2 == len(insn.sonsList) \
            and 2 == len(insn.sonsList[1].sonsList)

    def getRegNo(self, insn):
        return insn.sonsList[0]

    def getConstValue(self, insn):
        return insn.sonsList[1]

    def haveSameReg (self, first, next):
        nameFirst = first.sonsList[0].variableName
        nameNext =  next.sonsList[1].sonsList[1].variableName
        return nameFirst == nameNext

    # Instruction without immediate parameter
    # Should be extracted from database
    insnWithoutConst = {
        "riscv"   : ("*", "/", "-"),
        "power"   : ("/",),
        "aarch64" : ("/", "*"),
    }

    def doMoveOptimize(self):
        i = 1
        listLen = len(self.oldList)
        while i < listLen:
            previous = self.oldList[i-1]
            insn     = self.oldList[i]
            if self.isMovConst(previous)     \
               and insn.isOperator()         \
               and self.isOpWithVar(insn)    \
               and self.haveSameReg(previous, insn) \
               and insn.sonsList[1].getOpName() not in self.insnWithoutConst[self.archName]:
                # print (insn.sonsList[1].getOpName())
                new = copy.deepcopy(insn)
                new.sonsList[1].sonsList[1] = copy.deepcopy(previous.sonsList[1])
                self.optimizeCount += 1
                # print ("New", i, new)
                self.newList += [new]
                i += 2
            else:
                self.newList += [previous]
                i += 1
        self.newList += [self.oldList[-1]]

    def getOptimizedInsnList(self):
        return self.newList
