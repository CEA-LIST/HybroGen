#!/usr/bin/env python3

import sys, os
from IsaDb  import IsaDb
# from Insn import Insn
from ProxyDb import *
import H2Isa

def buildMask(begin, end):
    return hex((1 << (begin - end + 1 )) - 1)
    
def binToHexString(value):
    v = 0
    for c in value:
        v = v * 2
        if c == '1':
            v += 1
    return hex(v)

def genHeader(isa):
    insnLenList = isa.getWordSizeFromDb()
    insnLenList.sort()
    archname = isa.archname
    elemSize = insnLenList[0]
    mask = hex(2**elemSize - 1)
    t = """
#define {arch}_G{isize}(INSN){{ *(h2_asm_pc_{arch}++) = (INSN);}}
""".format(arch = archname, isize = elemSize)
    return t
    
def genMacro(isa, insns):
    archname = isa.archname
    insnLenList = isa.getWordSizeFromDb()
    insnLenList.sort()
    elemSize = insnLenList[0]
    maskElem = hex((1 << elemSize) - 1)
    s = ""
    for i in insns:
        binLen = 0
        paramList = []
        for p in i["encoding"]:
            binLen += p["begin"] - p["end"] + 1
            if p["name"][0] in "irf" and p["name"][1] in "0123456789" and p["name"] not in paramList:
                paramList.append(p["name"])
        s += """
#define {macro}({param}) /* {sem} */ \\
do {{ \\
""".format(macro= i["macroname"], param = ",".join(paramList) , sem = i["semname"])
        tmp = []
        nbBit = 0
        for e in i["encoding"]:
            if e["onlybin"]:
                value = binToHexString(e["name"])
            else:
                value = e["name"]
            valueSize =  e["begin"] - e["end"] + 1
            
            if valueSize < (elemSize - nbBit):
                if tmp == []:
                    s += "\t%s_G%s("%(archname, elemSize)
                    
                tmp.append("((%s & %s) << %s)"%(value, buildMask (e["begin"], e["end"]), str(elemSize - nbBit - valueSize)))
                nbBit += valueSize
                if nbBit == elemSize:                    
                    s += "|".join(tmp)
                    s += "); \\\n"
                    tmp = []
                    nbBit = 0

            else:
                if nbBit != 0:
                    tmp.append("(%s >> %s)"%(value, str(valueSize - (elemSize - nbBit))))
                    s += "|".join(tmp)
                    s += "); \\\n"
                    tmp = []
                    valueSize -= (elemSize - nbBit)
                    nbBit = 0
                if valueSize > 0:
                    for j in range(int(valueSize/elemSize)):
                        s += "\t%s_G%s("%(archname, elemSize)
                        s += "((%s >> %s) & %s)); \\\n"%(value, str(valueSize- elemSize), maskElem)
                        valueSize -= elemSize
                    if valueSize > 0:
                        s += "\t%s_G%s("%(archname, elemSize)
                        tmp.append("((%s & %s) << %s)"%(value, hex((1 << valueSize) - 1), str(elemSize - valueSize)))
                        nbBit += valueSize
                        valueSize = 0
        s += "} while(0) \n"
    return s
   
def genGenerator(isa, lSem, lInsns):
    s = ""
    archname = isa.archname    
    for semname in lSem:
        paramlist = list(set([len(i[0]) for i in isa.getInsnParameters(semname)]))
        for param in paramlist:
            params = []
            for i in range(param):
                params.append("h2_sValue_t P%d"%i)
            s += "void %s_gen%s_%s(%s)\n{\n"%(archname, semname, param, ", ".join(params))
            nb_if = 0
            for insn in lInsns:
                if insn["semname"].upper() == semname.upper():
                    #Instruction without parameter
                    if int(param) == 0:
                        s += """ 
    {mn}();
""".format(mn = insn["macroname"])
                        break
                    elif param == len(insn["parameters"]) and param > 0:
                        args = []
                        conds = []
                        nbr = 0
                        nbi = 0
                        for j, p in enumerate(insn["parameters"]):
                            if p == 'r':
                                args.append("P%d.regNro"%j)
                                conds.append("P%d.ValOrReg == 0"%j)
                                nbr += 1
                            elif p == 'i':                                
                                args.append("P%d.valueImm"%j)
                                conds.append("P%d.ValOrReg == 1"%j)
                                nbi += 1
                        if nb_if == 0:
                            nb_if += 1
                            s += """ 
if ((P0.arith == '{ar}') && (P0.wLen == {wl}) && (P0.vLen == {vl}) && {cond})
{{
    {mn}({arg});
}}
""".format (ar = insn["arith"], sn = insn["semname"], wl = insn["wordlen"], vl = insn["vectorlen"], cond = " && ".join(conds), mn = insn["macroname"], arg = ", ".join(args))
                        else:
                            nb_if += 1
                            s += """ 
else if ((P0.arith == '{ar}') && (P0.wLen == {wl}) && (P0.vLen == {vl}) && {cond})
{{
    {mn}({arg});
}}
""".format (ar = insn["arith"], sn = insn["semname"], wl = insn["wordlen"], vl = insn["vectorlen"], cond = " && ".join(conds), mn = insn["macroname"], arg = ", ".join(args))
            if param == 0:
                s += """
}
"""    
            elif nb_if == 0:
                s += """
printf("Warning, generation is not possible with this arguments");
}
"""
                     
                
            else:   
                s += """
else
{
exit(EXIT_FAILURE);
}
}
"""               
    return s
    
def outFile(filename, dataToWrite):
    f = open ("demo/add-float/" + filename, "w")
    f.write (dataToWrite)
    f.close
    print ("Generated: %s"%filename)

def themain(argv):
    #insert isa x86 and riscv into database
    lArch = ["x86", "riscv", "k1", "power"]
    dIsaDb = {}
    dInsns = {}
    db = ProxyDb("localhost", "hybrogen", "hybrogen", "hybrogen")
    for a in lArch:
        H2Isa.insertDb(a)
        dIsaDb[a] = IsaDb(db, a)
    
    #Search add float 
    lSem = ["ADD", "RET"]
    for a in lArch:
        dInsns[a] = dIsaDb[a].getInsnListSem("ADD", "f")
        dInsns[a].extend(dIsaDb[a].getInsnListSem("RET", "i"))
    
    #create the output file with h2 struct, macro and gen function
    output = """#include "../../include/h2-common.h"
"""
    for a in lArch:
        output += genHeader(dIsaDb[a])
    for a in lArch:
        output += genMacro(dIsaDb[a], dInsns[a])
    for a in lArch:
        output += genGenerator(dIsaDb[a], lSem, dInsns[a])

    outFile("h2-demo-add.h", output)
    
if __name__ == '__main__':
    themain(sys.argv[1:])
