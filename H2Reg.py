#!/usr/bin/env python3

import antlr4
import inspect
import sys, os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from HybroGen.RegisterDescriptionLexer    import RegisterDescriptionLexer
from HybroGen.RegisterDescriptionParser   import RegisterDescriptionParser
from HybroGen.RegisterDescriptionListener import RegisterDescriptionListener
from HybroGen.Register import Register
from HybroGen.ProxyDb import *
import time
       
class RegisterListener(RegisterDescriptionListener):
    def __init__(self, archname, db):
        self.archname = archname
        self.db = db
    def enterRegisterline(self, ctx: RegisterDescriptionParser.RegisterlineContext):
        self.currentReg = Register(self.archname)
        self.currentReg.setRegisterType(ctx.regbank().getText())
        if len(ctx.regbankvec().getText()) == 1:
            self.currentReg.setIsVector(True)
    def enterExtension(self, ctx:RegisterDescriptionParser.ExtensionContext):
        self.currentReg.setExtension(ctx.NAME().getText())
    def enterRegisterprefix(self, ctx:RegisterDescriptionParser.RegisterprefixContext):
        tmp = str(ctx.PREFIX())
        try:
            registerNumber = int(tmp[1:])
        except ValueError:
            self.currentReg.setPrefix(tmp[1])
            self.currentReg.setRegisterName(int(tmp[2:]))
        else:
            self.currentReg.setRegisterName(int(tmp[1:]))
        if ctx.INT() != None:
            self.currentReg.setRegisterName(ctx.INT().getText())
 
    def enterRegisterfunction(self, ctx:RegisterDescriptionParser.RegisterfunctionContext):
        self.currentReg.setFunction(ctx.FUNCNAME())
        
    def enterRegisterfunctionwn(self, ctx:RegisterDescriptionParser.RegisterfunctionwnContext):
        if (ctx.INT() == None or len(ctx.INT().getText())== 0):
            self.currentReg.setFunction(ctx.REGWN())
        else:
            tmp = str(ctx.REGWN())
            functionType = tmp[0]
            indMin = int(tmp[1:])
            indMax = int(ctx.INT().getText())
            for i in range(indMin, indMax + 1):
                self.currentReg.setFunction(functionType + '{:02d}'.format(i))
    
    def enterRegisterwidth(self, ctx:RegisterDescriptionParser.RegisterwidthContext):
        self.currentReg.setRegisterWidth(ctx.INT().getText())
        
    def exitRegisterline(self, ctx:RegisterDescriptionParser.RegisterlineContext):
        prefix = self.currentReg.getPrefix()
        lRegisterName = self.currentReg.getRegisterName()
        lRegisterFunction = self.currentReg.getFunction()
        width = self.currentReg.getRegisterWidth()
        if self.currentReg.getIsVector():
            regType = 'v' + self.currentReg.getRegisterType()
        else:
            regType = self.currentReg.getRegisterType()
        extension = self.currentReg.getExtension()
        if len(lRegisterName) == 1:
            self.db.setRegister(self.archname, extension, lRegisterName[0], prefix + str(lRegisterName[0]),  width, regType, self.currentReg.getFunction()[0])
        elif len(lRegisterFunction) == 1:
            for elem in range(int(lRegisterName[0]), int(lRegisterName[1])+1):
                self.db.setRegister(self.archname, extension, elem, prefix + str(elem), width, regType, self.currentReg.getFunction()[0])
        else:
            for i,elem in enumerate(range(int(lRegisterName[0]), int(lRegisterName[1])+1)):
                self.db.setRegister(self.archname, extension, elem, prefix + str(elem),  width, regType, self.currentReg.getFunction()[i])

def initDb():
    db = ProxyDb("localhost", "hybrogen", "hybrogen", "hybrogen")

def insertDb(archName):
    filename = "HybroGen/arch/%s/h2-%s.register"%(archName, archName)
    db = ProxyDb("localhost", "hybrogen", "hybrogen", "hybrogen")
    try:
        l = RegisterDescriptionLexer(antlr4.FileStream(filename, "utf8"))
    except FileNotFoundError:        
        print("Error : no file HybroGen/arch/%s/h2-%s.register"%(archName, archName))
        sys.exit(0)
    
    s = CommonTokenStream(l)
    p = RegisterDescriptionParser(s)
    t = p.registerdescription()
    w = ParseTreeWalker()
    lis = RegisterListener(archName, db)
    w.walk(lis, t)
        

def dropDb():    
    db = ProxyDb("localhost", "hybrogen", "hybrogen", "hybrogen")
    db.dropDb()
    
argList = {
    "-d":("Delete all database",               dropDb),
    "-i":("Insert a register in the database", insertDb),
    "-s":("Initialize database",               initDb),
    "-x":("xperimetal stuff",                  usage),
}
    
def themain(argv):
    action = argv[0]
    if action not in argList.keys():
        usage("unknown action")
    elif len(argv) == 1:
        argList[action][1]()        
    else: 
        argList[action][1](argv[1])
    

def usage(msg):
    print("Error : %s"%msg)
    print("%s %s [ArchName] "%("H2Register", argList.keys()))
    for k in argList.keys():
        print("%s : %s"%(k, argList[k]))
    sys.exit(0)

if __name__ == '__main__':
    arglen = len(sys.argv)
    if arglen < 2:
        usage("Give a parameter")
    themain(sys.argv[1:])
