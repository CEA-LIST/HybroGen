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
    """ Parse a register line definition containing:
    * BankSet (or extension name)
    * Arithmetic used
    * Reg # range
    * Register width
    * Textual description
    Example :
    A64     i      $r0-7      64      O0-7    # Function Ouput registers
    A64     i      $r9-28     64      T9-28   # Temporaries registers
    """
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

def initDb(dbId):
    db = ProxyDb(dbIds["host"], dbIds["dbname"], dbIds["user"], dbIds["pwd"])

def insertDb(archName, dbId):
    filename = "HybroGen/arch/%s/h2-%s.register"%(archName, archName)
    db = ProxyDb(dbIds["host"], dbIds["dbname"], dbIds["user"], dbIds["pwd"])
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

def dropDb(dbIds):
    db = ProxyDb(dbIds["host"], dbIds["dbname"], dbIds["user"], dbIds["pwd"])
    db.dropDb()

def usage(msg):
    print("Error : %s"%msg)
    print("%s %s [ArchName] "%("H2Register", argList.keys()))
    for k in argList.keys():
        print("%s : %s"%(k, argList[k]))
    sys.exit(0)

if __name__ == '__main__':
    import argparse

    p = argparse.ArgumentParser("Hybrogen register handling")
    p.add_argument ("-a", "--arch",     nargs=1,  default="none", help="Give arch name")
    p.add_argument ('-p', '--dropDb',   action='store_true',  help="Delete all database tables")
    p.add_argument ('-i', '--insertDb', action='store_true', help="Insert a register in the database")
    p.add_argument ('-n', '--initDb',   action='store_true',  help="Init DB")
    p.add_argument ('-d', '--dbIds',    default="localhost:hybrogen:hybrogen:hybrogen", help="give quadruplet database identification host:dbName:dbUser:dbpasswd")
    args = p.parse_args()
    archName = args.arch[0]
    ids = args.dbIds.split(":")
    dbIds = {"host": ids[0], "dbname": ids[1], "user": ids[2],"pwd": ids[3]}
    if args.initDb:
        initDb (archName)
    elif args.dropDb:
        dropDb (dbIds)
    elif args.insertDb:
        insertDb (archName, dbIds)
