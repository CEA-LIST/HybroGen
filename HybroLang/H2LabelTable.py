#!/usr/bin/env python3

class H2LabelTable:
    """HybroLang Label table """

    def __init__(self, archName):
        """Label table : label """
        self.labelTable = {}
        self.labelNumber = 0
        self.archName = archName
    def add(self, labelName, idValue):
        if labelName in self.labelTable:
            raise Exception ("Label table error (add)", "Already existing label: "+labelName)
        self.labelTable[labelName] = idValue

    def getCDecl (self):
        decl = "#define %s_genLABEL(LABEL_ID) labelAddresses[LABEL_ID] = h2_asm_pc;\n"%(self.archName)
        decl += "h2_insn_t   * labelAddresses []={\n"
        for labelName in self.labelTable:
            decl += "\t0, /* %s */\n"%labelName
            decl += "\t#define %s %d\n"%(labelName, self.labelTable[labelName])
        decl += "\t};\n"
        return decl

    def __iter__(self):
        return self.labelTable.__iter__()

    def __str__(self):
        tmp = ""
        for v in self.labelTable:
            tmp += "%s %d\n"%(v, self.labelTable[v])
        return tmp

    def genLabelName(self, prefix=""):
        varName = "h2_%s_%08d"%(prefix, self.labelNumber)
        self.add (varName, self.labelNumber)
        self.labelNumber += 1
        return varName

if __name__ == "__main__":
    l = H2LabelTable("power")

    l.add ("begin_0000", 0)
    l.add ("end_0001", 1)
    l.add ("begin_0002", 2)
    print(l)
    print(l.getCDecl())
