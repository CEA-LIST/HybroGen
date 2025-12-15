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
    def __init__(self, archName):
        self.QEMUMasks ={}
        self.archName = archName

    def getMasksList(self):
        returnList = """
static InsnClass_t %sInsnClass [] = {
"""%self.archName
        for insn in self.QEMUMasks:
            mask = ""
            for c in self.QEMUMasks[insn]:
                if c in ["0", "1"]: mask += "1"
                elif c in ["X", "x"] : mask += "0"
            pattern = ""
            for c in self.QEMUMasks[insn]:
                if c in ["0", "1"]: pattern += c
                elif c in ["X", "x"] : pattern += "0"
            opSplit = insn.split("-")
            if opSplit[0] == "r":               opClass = "COUNT_LD"
            elif opSplit[0] == "w":             opClass = "COUNT_ST"
            elif opSplit[1] == "i" and opSplit[0] in ["add","sub", "mul", "div"]:
                opClass = "COUNT_IOP"
            elif opSplit[1] == "i" and opSplit[0] in ["ba","blt", "ble", "bgt", "bge", "bne", "beq", "cmp",]:
                opClass = "COUNT_BR"
            elif opSplit[1] == "i" and opSplit[0] in ["or","and", "xor"]:
                opClass = "COUNT_BIT"
            elif opSplit[1] == "f" :                opClass = "COUNT_FLOP"
            else:
                opClass = "COUNT_TBD"
            returnList += '{"%s",  %s, 0x%x, 0x%x, %d},\n'%(insn, opClass, int("0b"+mask, 2), int("0b"+pattern, 2), int(opSplit[2]))
        returnList += "};"

        return returnList
    def initNewLine(self):
        self.newLine = ""

    def addToNewLine(self, part):
        self.newLine += " " + part

    def enterAsmdescr(self, ctx:IsaDescriptionParser.AsmdescrContext):
        self.insnName = "%s-%s-%s-%s"%(ctx.semname().getText(), ctx.arith().getText(), ctx.INT(0), ctx.INT(1))

    def enterBindescr(self, ctx:IsaDescriptionParser.BindescrContext):
        self.initNewLine()

    def exitIsaline(self, ctx:IsaDescriptionParser.IsalineContext):
        self.QEMUMasks[self.insnName] = self.newLine
#        print ("%s:%s"%(self.insnName, self.newLine))

    def enterBinvalue(self, ctx:IsaDescriptionParser.BinvalueContext):
        self.addToNewLine(str(ctx.INT()))

    def enterRegbin(self, ctx:IsaDescriptionParser.RegbinContext):
        sizeEnd   = int(str(ctx.INT(0)))
        if None != ctx.INT(1):
            sizeBegin = int(str(ctx.INT(1)))
        else:
            sizeBegin = sizeEnd
        self.addToNewLine("X"*(sizeEnd + 1 - sizeBegin))

def parse(archName):
    # print("Generate QEMU plugin instructions masks: %s"%archName)
    fileName = "HybroGen/arch/%s/h2-%s.isa"%(archName, archName)
    try:
        l = IsaDescriptionLexer(antlr4.FileStream(fileName, "utf8"))
    except FileNotFoundError:
        print("Error : no file %s"%(fileName))
        sys.exit(0)
    s = CommonTokenStream(l)
    p = IsaDescriptionParser(s)
    t = p.isadescription()
    w = ParseTreeWalker()
    lInsn = []
    lis = IsaListener(archName)
    w.walk(lis, t)
    return lis.getMasksList()

def usage(msg):
    print("Error : %s"%msg)
    for k in argList.keys():
        print("%s : %s"%(k, argList[k]))
    sys.exit(0)

if __name__ == '__main__':
    import argparse

    p = argparse.ArgumentParser("Hybrogen ISA to QEMU mask")
    p.add_argument ("-a", "--arch",   nargs=1,  default=["riscv"], help="Give arch name")
    args = p.parse_args()

    maskList = parse(args.arch[0])
    print(maskList)
