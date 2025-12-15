#!/usr/bin/env python3

class H2GenGen:
    """ Helper for code generation """
    def __init__(self, archName):
        self.archName = archName
        self.indentLevel = 0

    def formatCode (self, code):
        """ Format a code line to make it readable"""
        tmp = ""
        for c in code:
            tmp += "\t%s\n"%c
        return tmp

    def setIndentLevel (self, indentLevel):
        self.indentLevel = indentLevel
        self.tabLevel = indentLevel*'\t'

    def genSValue(self, sType, arith, vLen, wLen, regNo, value):
        return f"(h2_sValue_t) {{{sType}, '{arith}', {vLen}, {wLen}, {regNo}, (int)({value})}}"

    def genSValueFromType(self, sType, H2, regNo, value):
        arith = H2['arith']
        vLen =  H2['vectorLen']
        wLen =  H2['wordLen']
        return f"(h2_sValue_t) {{{sType}, '{arith}', {vLen}, {wLen}, {regNo}, (int)({value})}}"

    def genImmValue(self, value):
        if 0 == value :
            return "immValueZero"
        else:
            return self.genSValue("H2VALUE", 'i', 1, 32, 0, value)

    def genFixedRegister(self, regNo):
        return self.genSValue("H2REGISTER", 'i', 1, 32, regNo, 0)

    def codeGen4(self, semName, destReg, srcL, srcR = "immValueZero", option=""):
        return self.codeGen(4, semName, destReg, srcL, srcR, option)

    def codeGen3(self, semName, destReg, srcL, srcR = "immValueZero"):
        return self.codeGen(3, semName, destReg, srcL, srcR)

    def codeGen3Inv(self, semName, destReg, srcL, srcR = "immValueZero"):
        """ Special code generator for LD: set srcL as destination register"""
        genF =  f"{self.tabLevel}{destReg} = {self.archName}_gen{semName}_3({destReg}, {srcL}, {srcR});"
        return [genF]

    def codeGen2(self, semName, destReg, srcL):
        return self.codeGen(2, semName, destReg, srcL)
    def codeGen1(self, semName, destReg):
        return self.codeGen(1, semName, destReg)

    def codeGen0(self, semName):
        return self.codeGen(0, semName)

    def codeGen(self, opN, semName, destReg="", srcL="", srcR = "", option=""):
        if   opN == 0: genF =  f"{self.tabLevel}{destReg} = {self.archName}_gen{semName}_0();"
        elif opN == 1: genF =  f"{self.tabLevel}{destReg} = {self.archName}_gen{semName}_1({destReg});"
        elif opN == 2: genF =  f"{self.tabLevel}{destReg} = {self.archName}_gen{semName}_2({destReg}, {srcL});"
        elif opN == 3: genF =  f"{self.tabLevel}{destReg} = {self.archName}_gen{semName}_3({destReg}, {srcL}, {srcR});"
        elif opN == 4: genF =  f"{self.tabLevel}{destReg} = {self.archName}_gen{semName}_4({destReg}, {srcL}, {srcR}, {option});"
        else: genF = "Unknown operand number"
        return [genF]

    def codeGen4W(self, semName, destReg, srcL, srcR = "immValueZero", option=""):
        return self.codeGenW(4, semName, destReg, srcL, srcR, option)

    def codeGen3W(self, semName, destReg, srcL, srcR = "immValueZero"):
        return self.codeGenW(3, semName, destReg, srcL, srcR)

    def codeGen2W(self, semName, destReg, srcL):
        return self.codeGenW(2, semName, destReg, srcL)

    def codeGen1W(self, semName, destReg):
        return self.codeGenW(1, semName, destReg)

    def codeGen0W(self, semName):
        return self.codeGenW(0, semName)

    def codeGenW(self, opN, semName, destReg="", srcL="", srcR = "", option=""):
        if   opN == 0: genF =  f"{self.tabLevel}{self.archName}_gen{semName}_0();"
        elif opN == 1: genF =  f"{self.tabLevel}{self.archName}_gen{semName}_1({destReg});"
        elif opN == 2: genF =  f"{self.tabLevel}{self.archName}_gen{semName}_2({destReg}, {srcL});"
        elif opN == 3: genF =  f"{self.tabLevel}{self.archName}_gen{semName}_3({destReg}, {srcL}, {srcR});"
        elif opN == 4: genF =  f"{self.tabLevel}{self.archName}_gen{semName}_4({destReg}, {srcL}, {srcR}, {option});"
        else: genF = "Unknown operand number"
        return [genF]
