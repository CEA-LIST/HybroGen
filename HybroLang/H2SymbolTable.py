#!/usr/bin/env python3

class H2SymbolTable:
    """HybroLang Symbol table """

    def __init__(self, archName):
        """Symbol table : name / register allocation correspondance"""
        self.symbolTable = {}
        self.regAlloc = {}
        self.tempsNo = 0

    def add(self, variableName, datatype, registerNumber=None):
        # print (f"New variable : {variableName}, {datatype}, {registerNumber})")
        # breakpoint()
        if variableName in self.symbolTable:
            raise Exception ("Symbol table error (add)", "Already existing var: "+variableName)
        self.symbolTable[variableName] = datatype
        if None != registerNumber:
            self.setRegister (variableName, registerNumber)

    def getTemps(self, dataType):
        tempsName = "tmp%04d"%self.tempsNo
        self.add (tempsName, dataType, -1)
        self.tempsNo += 1
        return tempsName

    def resetTemps(self, dataType):
        self.tempsNo = 0

    def get(self, variableName):
        if variableName in self.symbolTable:
            return self.symbolTable[variableName]
        else:
            raise Exception ("Symbol table error (get)", "Not existing var: "+variableName)

    def setRegister(self, varName, nro):
        self.regAlloc[varName] = nro

    def getCDecl (self):
        decl = "\t/*VarName = { ValOrLen, arith, vectorLen, wordLen, regNo, Value} */\n"
        for varName in self.symbolTable:
            v = self.get(varName)
            # print(varName, v)
            arith = v["arith"]
            vLen  = v["vectorLen"]
            wLen  = v["wordLen"]
            regNo = self.regAlloc[varName]
            if '[]' in arith:
                arith = "i"
                wLen = 32 # TODO or 64 for aarch64 ?
                vLen = 1
            else:
                arith = arith[0]
            decl += f"\th2_sValue_t {varName} = {{H2REGISTER, '{arith}', {vLen}, {wLen}, {regNo}, 0}};\n"
        return decl

    def __iter__(self):
        return self.symbolTable.__iter__()

    def __str__(self):
        tmp = ""
        for v in self.symbolTable:
            tmp += "%20s : %s"%(v, self.symbolTable[v])
            if v in self.regAlloc:
                tmp += " : reg : %d"%(self.regAlloc[v])
            tmp += "\n"
        return tmp

if __name__ == "__main__":
    a = H2SymbolTable("power")
    data = (
        ("i", "int", 32, 1, 0),
        ("AbsoluteLongVector", "flt", 64, 1024, 1),
        ("Variable", "unknownArithmetic", 64, 1024, 2),
        ("pixel", "flt", 32, 4, 3),
        ("i", "int", 32, 1, 4),
        )

    for d in data:
        try:
            print ("Add %s %s"%(d[0], d[1]))
            a.add (d[0], d[1], d[2], d[3], d[4])
        except Exception as e:
            print ("Exception:"+str(e))
            pass
    print(a)
