#!/usr/bin/env python3

class H2SymbolTable:
    """HybroLang Symbol table """

    def __init__(self, archName):
        """Symbol table : name / register allocation correspondance"""
        self.symbolTable = {}
        self.regAlloc = {}

    def add(self, variableName, datatype, registerNumber=None):
        if variableName in self.symbolTable:
            raise Exception ("Symbol table error (add)", "Already existing var: "+variableName)
        self.symbolTable[variableName] = datatype
        if None != registerNumber:
            self.setRegister (variableName, registerNumber)

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
            #print(v)
            structDef = "h2_sValue_t %s = {%s, '%s', %s, %s, %s, %s};"%(varName, "REGISTER", v["arith"][0], v["vectorLen"], v["wordLen"], self.regAlloc[varName], 0)
            decl += "\t%s\n"%structDef
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
