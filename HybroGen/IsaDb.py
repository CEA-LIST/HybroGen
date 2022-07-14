#!/usr/bin/env python3

from HybroGen.ProxyDb import *

class IsaDb:
    """Define an instruction set for an architecture. Generate generator
    for multiple languages"""

    def __init__ (self, db, archname, extList):
        self.archname = archname
        self.extList = extList
        self.db = db
        self.insnList = []
        self.regList = []

    def __str__(self):
        s = "%s / %d \n"%(self.archname, self.sizeList)
        s += str(self.db.getColumnsName())+"\n"
        formatString = "{semname:10} {vectorlen:3} {wordlen:2} {arith:10} {archname:5}/{extension:10} {name:10} {macroname}\n"
        insnList = self.db.getInsnList(self.archname)
        for i in insnList:
            s += formatString.format(**i)
        return s

    def getCheck(self):
        semNameList = self.db.getInsnSemList(self.archname)
        r = ""
        for insnSemName in semNameList:
            variants = self.db.getInsnVariant(self.archname, insnSemName[0])
            r += "%10s %s\n"%(insnSemName[0], variants)
        return r

    def getWordSizeFromDb(self):
        return self.db.getWordSize(self.archname)

    def addwSizeList(self, wSizeList):
        for i in wSizeList:
            self.db.setInstructionLen(self.archname, i)

    def addInsn(self, insn):
        self.insnList.append(insn)

    def flush(self):
        for i in self.insnList:
            self.db.setInstruction(i, self.archname)

    def getInsnList(self):
        return self.db.getInsnList(self.archname)

    def getInsnListSem(self, semname, arith):
        return self.db.getInsnSemantic(self.archname, self.extList, semname, arith)

    def getInsnParameters(self, semname):
        return self.db.getInsnParameters(self.archname, semname)


if __name__ == '__main__':
    print("main from Isa")
