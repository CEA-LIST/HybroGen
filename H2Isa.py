#!/usr/bin/env python3

import antlr4
import inspect
import sys, os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from HybroGen.IsaDescriptionLexer    import IsaDescriptionLexer
from HybroGen.IsaDescriptionParser   import IsaDescriptionParser
from HybroGen.IsaDescriptionListener import IsaDescriptionListener
from HybroGen.IsaDb  import IsaDb
from HybroGen.Insn import Insn
from HybroGen.Register import Register
from HybroGen.PGen import PGen
from HybroGen.ProxyDb import *
from HybroGen.Counter import Counter
import time

class IsaListener(IsaDescriptionListener):
    '''Listener abstrac class for ISA grammar'''
    def __init__(self):
        self.sizeList = []
        if type(self) is IsaListener:
            raise Exception("IsaListener is an abstract class")
    def enterArchline(self, ctx: IsaDescriptionParser.ArchlineContext):
        self.archName = ctx.NAME().getText()
        self.sizeList = [int(s.getText()) for s in ctx.INT()]
        print(self.archName, self.sizeList)
    def enterIsaline(self, ctx: IsaDescriptionParser.IsalineContext):
        self.currentInsn = Insn()
    def enterExtname(self, ctx:IsaDescriptionParser.OpnameContext):
        self.currentInsn.setExtName(ctx.NAME().getText())
    def enterBinvalue(self, ctx:IsaDescriptionParser.BinelemContext):
        l = len(ctx.INT().getText()) - 1
        self.currentInsn.addBinEncoding(ctx.INT().getText(), l, 0)
    def exitExpbin(self, ctx:IsaDescriptionParser.ExpbinContext):
        self.currentInsn.addOpBinEncoding(ctx.op().getText())
    def enterRegbin(self, ctx:IsaDescriptionParser.RegbinContext):
        regorconstname = ctx.NAME().getText()
        begin = int(ctx.INT()[0].getText())
        if len(ctx.INT()) > 1:
            end = int(ctx.INT()[1].getText())
        else:
            end = begin
        self.currentInsn.addBinEncoding(regorconstname, begin, end)
        self.currentInsn.addToParameter(regorconstname)
    def enterReglist(self, ctx:IsaDescriptionParser.ReglistContext):
        pass
    def enterRegName(self, ctx:IsaDescriptionParser.RegNameContext):
        pass
    def enterAsmdescr(self, ctx:IsaDescriptionParser.AsmdescrContext):
        self.currentInsn.setName(ctx.opname().getText())
        self.currentInsn.setSemName(ctx.semname().getText())
        self.currentInsn.setArith(ctx.arith().getText())
        self.currentInsn.setVLen(int(ctx.INT()[0].getText()))
        self.currentInsn.setWSize(int(ctx.INT()[1].getText()))

class IsaListenerDb(IsaListener):
    '''Listener implementation for ISA grammar'''
    def __init__(self, isa):
        self.isa = isa
        self.insnCount = 0
        super().__init__()
    def enterArchline(self, ctx: IsaDescriptionParser.ArchlineContext):
        self.archName = ctx.NAME().getText()
        self.sizeList = [int(s.getText()) for s in ctx.INT()]
        self.isa.addwSizeList(self.sizeList)

    def exitIsadescription(self, ctx:IsaDescriptionParser.IsadescriptionContext):
        print("Inserted ISA for %s (%s) bits, %d instructions"%(self.archName, self.sizeList, self.insnCount))
    def exitIsaline(self, ctx: IsaDescriptionParser.IsalineContext):
        self.insnCount += 1
        if (self.currentInsn.getBinLen() not in self.sizeList):
            print("Error on insn len:", self.currentInsn, file=sys.stderr)
            sys.exit(-1)
        self.isa.addInsn(self.currentInsn)
    def enterSemname(self, ctx:IsaDescriptionParser.OpnameContext):
        self.currentInsn.setSemName(ctx.NAME().getText())
    def enterRegName(self, ctx:IsaDescriptionParser.RegNameContext):
        self.currentInsn.addRegName(ctx.NAME().getText())
        self.currentInsn.setOperand(ctx.NAME().getText())

class IsaListenerPrettyPrint(IsaListener):
    '''Listener implementation for ISA grammar'''
    def __init__(self):
        self.SemName = Counter()
        self.Arith = Counter()
        self.SemArith = Counter()
        super().__init__()
    def exitIsaline(self, ctx: IsaDescriptionParser.IsalineContext):
        if (self.currentInsn.getBinLen() not in self.sizeList):
            print("Warning Len:",self.currentInsn, file=sys.stderr)
        else:
            print(self.currentInsn)
    def enterSemname(self, ctx:IsaDescriptionParser.OpnameContext):
        self.SemName.add(ctx.NAME().getText())
        self.currentInsn.setSemName(ctx.NAME().getText())
    def enterAsmdescr(self, ctx:IsaDescriptionParser.AsmdescrContext):
        self.currentInsn.setName(ctx.opname().getText())
        self.currentInsn.setSemName(ctx.semname().getText())
        self.currentInsn.setArith(ctx.arith().getText())
        self.Arith.add(ctx.arith().getText())
        self.currentInsn.setVLen(int(ctx.INT()[0].getText()))
        self.currentInsn.setWSize(int(ctx.INT()[1].getText()))
        self.SemArith.add(ctx.semname().getText()+' ' +ctx.arith().getText())

class IsaListenerListInsn(IsaListener):
    '''Listener implementation for ISA grammar'''
    def __init__(self, l):
        self.sizeList = ()
        self.lInsn = l
        super().__init__()
    def exitIsaline(self, ctx: IsaDescriptionParser.IsalineContext):
        self.lInsn.append(self.currentInsn)
    def getSizeList(self):
        return self.sizeList

def parseprint(archName):
    print("Parsing for :", archName)
    filename = "HybroGen/arch/%s/h2-%s.isa"%(archName, archName)
    try:
        l = IsaDescriptionLexer(antlr4.FileStream(filename, "utf8"))
    except FileNotFoundError:
        print("Error : no file HybroGen/arch/%s/h2-%s.isa"%(archName, archName))
        sys.exit(0)
    s = CommonTokenStream(l)
    p = IsaDescriptionParser(s)
    t = p.isadescription()
    w = ParseTreeWalker()
    lis = IsaListenerPrettyPrint()
    w.walk(lis, t)
    print("Semantic instructions:\n%s"%lis.SemName)
    print("Supported arithmetics:\n%s"%lis.Arith)
    print("Semantics instructions with artihmetics:\n%s"%lis.SemArith)

def parse(archName):
    filename = "HybroGen/arch/%s/h2-%s.isa"%(archName, archName)
    try:
        l = IsaDescriptionLexer(antlr4.FileStream(filename, "utf8"))
    except FileNotFoundError:
        print("Error : no file HybroGen/arch/%s/h2-%s.isa"%(archName, archName))
        sys.exit(0)
    s = CommonTokenStream(l)
    p = IsaDescriptionParser(s)
    t = p.isadescription()
    w = ParseTreeWalker()
    lInsn = []
    lis = IsaListenerListInsn(lInsn)
    w.walk(lis, t)
    isa = Isa(archName, lis.getSizeList() ,lInsn)
    return isa

def generateC(archName):
    print("Generate C code generators for:", archName)
    isa = parse(archName)
    g = GenFunction(isa)
    outFile("h2-funct-%s.h"%archName, str(g.getCMacro()))
    c = GenHeader(isa)
    outFile("h2-macro-%s.h"%archName, str(c.getCMacro()))
    g = GenGenerator(isa)
    outFile("h2-insn-%s.h"%archName, str(g.genGenerators()))

def initDb():
    db = ProxyDb("localhost", "hybrogen", "hybrogen", "hybrogen")

def insertDb(archName):
    filename = "HybroGen/arch/%s/h2-%s.isa"%(archName, archName)
    try:
        fileDate = os.path.getmtime (filename)
    except FileNotFoundError:
        print("Error : no file HybroGen/arch/%s/h2-%s.isa"%(archName, archName))
        sys.exit(0)

    db = ProxyDb("localhost", "hybrogen", "hybrogen", "hybrogen")
    lastDbDate = db.getLastInsertDate(archName)
    if len(lastDbDate) == 0  or ( len(lastDbDate) > 0 and (lastDbDate[0] <= fileDate)):
        isa = IsaDb(db, archName, [])
        db.setLastInsertDate (archName, fileDate)
        l = IsaDescriptionLexer(antlr4.FileStream(filename, "utf8"))
        s = CommonTokenStream(l)
        p = IsaDescriptionParser(s)
        t = p.isadescription()
        w = ParseTreeWalker()
        lis = IsaListenerDb(isa)
        w.walk(lis, t)
        isa.flush()

def testdb(archName):
    db = ProxyDb("localhost", "hybrogen", "hybrogen", "hybrogen")
    isa = IsaDb(db, archName, [])
    print("Search aDd instruction in %s"%archName)
    print(isa.getInsnListSem("aDd", "rrr"))
    print("\nWordSize ")
    print(isa.getWordSizeFromDb())
    #print("\nInstruction list for %s"%archName)
    #print(isa.getInsnList())

def dropDb():
    db = ProxyDb("localhost", "hybrogen", "hybrogen", "hybrogen")
    db.dropDb()

argList = {
    "-a":("Parse with antlr, give stats",      parseprint),
    "-c":("Generate C code generators",        generateC),
    "-d":("Delete all database",               dropDb),
    "-i":("Insert an ISA in the database",     insertDb),
    "-l":("Give name and len of instructions", usage),
    "-p":("Generate Python code generators",   usage),
    "-s":("Initialize database",               initDb),
    "-v":("Give semantical instruction list and variants", usage),
    "-x":("xperimetal stuff",                  testdb),
}

def themain(argv):
    action = argv[0]
    if action not in argList.keys():
        usage("unknown action")
    elif len(argv) == 1:
        argList[action][1]()
    else:
        argList[action][1](argv[1])

def outFile(filename, dataToWrite):
    f = open ("HybroGen/include/"+filename, "w")
    f.write (dataToWrite)
    f.close
    print ("Generated: %s"%filename)

def usage(msg):
    print("Error : %s"%msg)
    for k in argList.keys():
        print("%s : %s"%(k, argList[k]))
    sys.exit(0)

if __name__ == '__main__':
    arglen = len(sys.argv)
    if arglen < 2:
        usage("Give a parameter")
    themain(sys.argv[1:])
