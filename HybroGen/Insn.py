#!/usr/bin/env python3

class Insn:
    """Define an instruction structure :
    * binary encoding,
    * name (isa version), semantic name
    * isa variant
    * acessed registers,
    * used arithmetic,
    """
    def __init__(self):
        self.binEncodingAndPosition = []
        self.data = {}
        self.data["extName"] = "noext"
        self.data["name"] = "noname"
        self.data["semname"] = "nosem"
        self.data["arith"] = "noarit"
        self.binInsnLen = 0
        self.thePosition = 0
        self.parameters = ""
        self.lParameters = []
        self.lOperand = []
        self.VLen = 0
        self.regList = []
        self.WSize = -1
    def __str__(self):
        tmp = ""
        for e in self.binEncodingAndPosition:
            tmp += "%s[%s:%s]"%(e["name"], e["begin"], e["end"]) + " "
        f = "%s : %3d %10s %5s %s %3d %3d %s %s"
        return f%(self.data["extName"], self.binInsnLen, self.data["name"], self.data["semname"], self.data["arith"], self.WSize, self.VLen, tmp, self.getMacroName())

    def addBinLen(self, value):
        self.binInsnLen += value
    def getBinLen(self):
        return self.binInsnLen
    def setSemName(self, name):
        self.data["semname"] = name
    def setExtName(self, name):
        self.data["extName"] = name
    def getExtName(self):
        return self.data["extName"]
    def getSemName(self):
        return self.data["semname"]
    def addToParameter(self, param):
        if param not in self.lParameters:
            self.lParameters.append(param)
            letter = param[0]
            if letter == 'r':
                self.parameters = letter + self.parameters
            else:
                self.parameters += letter

    def getParameter(self):
        return self.parameters
    def getJsonEncoding(self):
        import json
        return json.dumps(self.binEncodingAndPosition)
    def getBinEncoding(self):
        return self.binEncodingAndPosition
    def addBinEncoding(self, name, begin, end):
        self.thePosition += begin - end + 1
        self.addBinLen(begin - end + 1)
        onlybin = True
        for i in name:
            if i not in "01":
                onlybin = False
                break
        #concate 2 binary constant
        if onlybin and self.binEncodingAndPosition and self.binEncodingAndPosition[-1]["onlybin"]:
            self.binEncodingAndPosition[-1]["name"] += name
            self.binEncodingAndPosition[-1]["begin"] += begin + 1
            self.binEncodingAndPosition[-1]["end"] += end
            self.binEncodingAndPosition[-1]["position"] = self.thePosition
        else:
            a = {}
            a["onlybin"] = onlybin
            a["name"]  = name
            a["begin"] = begin
            a["end"]   = end
            a["position"] = self.thePosition
            self.binEncodingAndPosition.append(a)
    def addOpBinEncoding(self, op):
        self.binEncodingAndPosition[-1]["name"] = op + self.binEncodingAndPosition[-1]["name"]
    def setName(self, name):
        self.data["name"] = name
    def getName(self):
        return self.data["name"]
    def setArith(self, arith):
        self.data["arith"] = arith
    def getArith(self):
        return self.data["arith"]
    def setWSize(self, WSize):
        self.WSize = WSize
    def getWSize(self):
        return self.WSize
    def setRegList(self, regList):
        self.regList = regList
    def addRegName(self, regName):
        self.regList.append(regName)
    def getRegList(self):
        return ','.join(self.regList)
    def setVLen(self, VLen):
        self.VLen = VLen
    def getVLen(self):
        return self.VLen
    def getMacroName(self):
        n = self.data["name"].replace (".", "_")
        p = self.data["extName"].replace (".", "_")
        macroName = "%s_%s_%s_%s_%s_%s"%(p, n, self.parameters, self.data["arith"], self.WSize, self.VLen)
        return macroName.upper()
    def setOperand(self, op):
        self.lOperand.append(op)
    def getOperand(self):
        return self.lOperand
    def check(self, semantic, arithmetic, datawidth, vectorlen):
        print ("%s %s %d %d %d"%(self.getSemName(), self.getArith(), self.getWSize(), self.getVLen()))
        if semantic == self.getSemName() and arithmetic == self.getArith() and datawidth == self.getWSize() and vectorlen == self.getVLen() :
            return True
        return False
