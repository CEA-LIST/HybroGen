#!/usr/bin/env python3

def cmd(cmdAndArgs, Verbose, doPrint = True, wdir = None, doExec = True):
#    print (cmdAndArgs)
    if (doPrint):
        if wdir != None:
            print("-->cd %s"%(wdir))
        print("-->%s"%(" ".join(cmdAndArgs)))
    returncode = 0
    data = ""
    if doExec:
        process = subprocess.Popen(cmdAndArgs, cwd=wdir, stdout=subprocess.PIPE,
 stderr=subprocess.STDOUT)
        data = process.stdout.read()
        returncode = process.wait()
        if Verbose:
            print (data.decode("utf-8"))
            print ("Return code %s"%returncode)
        return returncode
    return 0

def exitError (errorMsg):
    print (errorMsg)
    sys.exit(-1)

def rmFiles (fileName, keep=False):
    if not keep:
        commR = tuple(["rm", "-f", fileName, fileName+".hl", fileName+".c"])
        cmd (commR, False, doPrint=False)

def compileAndRun(fileName, arch, dataset, keep=False):
    realExec = True
    realPrint = False
    commH = tuple(["../HybroLang.py", "-g", "-a", arch, "-c", "-i", fileName+".hl"])
    o = cmd (commH, False, doExec= realExec, doPrint = realPrint)
    if o != 0:
        rmFiles (fileName, keep)
        return False
    commC = tuple([config.getCompilerForArch(arch), "-g", "-DH2_DEBUG", "-o", fileName, fileName+".c"])
    o = cmd (commC, False, doExec= realExec, doPrint = realPrint)
    if o != 0:
        rmFiles (fileName, keep)
        return False
    commR = tuple([config.getQemuForArch(arch), fileName]+dataset)
    o = cmd (commR, False, doExec= realExec, doPrint = realPrint)
    rmFiles (fileName, keep)
    if o != 0:
        return False
    else:
        return True

def genAndRunAddress(singleArith, opList, wordLenList, vectorLen, archName, keep=False):
    resultDb = {}
    for op in opList:
        for wordLen in wordLenList:
#            print ("%5s : %5s(%03s)"%(singleArith, op, wordLen), end="")
            for vLen in vectorLen:
                if wordLen in CTypeArray[singleArith]:
                    theWordLen = "%03d"%int(wordLen)
                    theVectorLen = "%03d"%int(vLen)
                    fileName = "Tests/Test-Address-%s-%s-%s-%s-%s"%(op, singleArith, theWordLen, theVectorLen, archName)
                    c = CCodeAddress(opList[op], singleArith, vLen, wordLen, CTypeArray[singleArith][wordLen])
                    c.write(fileName+".hl")
                    dataSet = [str(i+3) for i in range(0, int(vLen)*2)]
                    msg = compileAndRun(fileName, archName, dataSet, keep)
                    print (fileName, msg)
                    resultDb[archName, "address", op, singleArith, vLen, wordLen] = msg
    return resultDb

def genAndRunValue(singleArith, opList, wordLenList, vectorLen, archName, keep):
    resultDb = {}
    for op in opList:
        for wordLen in wordLenList:
#            print ("%5s : %5s(%03s)"%(singleArith, op, wordLen), end="")
            for vLen in vectorLen:
                if wordLen in CTypeArray[singleArith]:
                    theWordLen = "%03d"%int(wordLen)
                    theVectorLen = "%03d"%int(vLen)
                    fileName = "Tests/Test-Value-%s-%s-%s-%s-%s"%(op, singleArith, theWordLen, theVectorLen, archName)
                    c = CCodeValue(opList[op], singleArith, vLen, wordLen, CTypeArray[singleArith][wordLen])
                    c.write(fileName+".hl")
                    dataSet = [str(i) for i in range(0, int(vLen)*2)]
                    msg = compileAndRun(fileName, archName, dataSet, keep)
                    resultDb[archName, "value", op, singleArith, vLen, wordLen] = msg
                    print(fileName, msg)
    return resultDb


def readCSVtoDict(fileName):
    svIn = csv.reader (open (fileName, "r"), delimiter=";")
    theList = {}
    next(svIn) # skip csv title
    for l in svIn:
        # print((l[0], l[1], l[2], l[3], l[4]))
        # print([r for r l l[5:] if len(r) > 0])
        if len(l) > 0: # If line non empty
            theList[(l[0], l[1], l[2], l[3], l[4])] = ([r for r in l[5:] if len(r) > 0])
    return theList


opArith = {"add":"+", "mul":"*", "sub":"-", "div":"/"}
opLogic = {"mod":"%", "or":"|", "xor":"^", "and":"&"}
opAritmeticalShift = {"sl":"<<", "sr":">>"}
CTypeArray = {
    'int': {"8": 'int8_t', "16":'int16_t', "32":'int32_t', "64":'int64_t',},
    'flt': {                               "32": 'float',  "64":'double',},
}

if __name__ == "__main__":
    import sys, subprocess, argparse, os
    from CCode import CCodeValue
    from CCode import CCodeAddress
    import csv
    from SwConfig import SwConfig
    config = SwConfig()

    parser = argparse.ArgumentParser()
    if not os.path.exists ("./Tests"):
        cmd(["mkdir", "-p", "./Tests"], False)

    parser.add_argument('-w',   '--wLen',     nargs="+",    default=["8", "16", "32", "64", "128"], help='Word len')
    parser.add_argument('-v',   '--vLen',     nargs="+",    default=["1", "2", "4", "8", "16", "32", "64", "128"], help='Vector len')
    parser.add_argument('-o',   '--operator', nargs="+",    default=["add", "mul", "sub", "div"], help='Arithmetiec Operators')
    parser.add_argument('-l',   '--logic',    nargs="+",    default=["mod", "or", "and", "xor", "and"], help='Logic Operators')
    parser.add_argument('-s',   '--arithmShift', nargs="+", default=["sl", "sr"], help='Arithmetical Shift Operators')
    parser.add_argument('-a',   '--arch',     nargs="+",    default=config.getKeys(), help='Architecture name list')
    parser.add_argument('-p',   '--param',    nargs="+",    default=["value", "address"], help='Passing parameter type')
    parser.add_argument('-k',   '--keep',     action='store_true', help='Keep intermediate files')
    parser.add_argument('-z',   '--analyse',  action='store_true', help='Analyse result')
    parser.add_argument('-d',   '--dotests',  action='store_true', help='Generate results')
    a = parser.parse_args()
#    print (a)
    results = {}
    csvFileName = "RegressionSingleOp%s.csv"%a.arch[0]
    # File format :
    # Archname = aarch64|power|netc
    # Param = value|address
    # Op = add|sub ...
    # Arit = flt|int|..
    # vLen = vectorLen 1|2|4|..
    # wLen = wordLen list 32 | 8; 16; 32| ...
    headers = ["ArchName", "Param", "Op", "Arith", "vLen", "wLen"]
    if a.analyse :
        if len(a.arch) != 1:
            exitError("Could only analyse 1 architecture")
        else:
            print ("Compare %s and %s"%("RegressionSingleOpReference.csv", csvFileName))
            refDict  = readCSVtoDict("RegressionSingleOpReference.csv") # Read reference list
            archDict = readCSVtoDict(csvFileName) # Read the generated results
            failValue = 0
            for k in archDict:
                if k not in refDict:
                    print("More in arch %s: %s"%(str(k), str(archDict[k])))
                    failValue = -1
            for k in refDict:
                if a.arch[0] in k and k not in archDict:
                    print("More in ref : %s %s"%(str(k), str(refDict[k])))
                    failValue = -1
            sys.exit(failValue)
    elif a.dotests:
        if "value" in a.param:
            for archName in a.arch:
    #            print ("-- %20s (per value) -- "%archName)
    #            printRule(a.vLen)
                for arith in ("int", "flt"):
                    subList = {i:opArith[i] for i in a.operator}
                    results.update(genAndRunValue(arith, subList, a.wLen, a.vLen, archName, a.keep))
                subList = {i:opLogic[i] for i in a.logic}
                results.update(genAndRunValue("int", subList, a.wLen, a.vLen, archName, a.keep))
                subList = {i:opAritmeticalShift[i] for i in a.arithmShift}
                results.update(genAndRunValue("int", subList, a.wLen, a.vLen, archName, a.keep))
        if "address" in a.param:
            for archName in a.arch:
    #            print ("-- %20s (per address) -- "%archName)
    #            printRule(a.vLen)
                for arith in ("int", "flt"):
                    subList = {i:opArith[i] for i in a.operator}
                    results.update(genAndRunAddress(arith, subList, a.wLen, a.vLen, archName, a.keep))
                subList = {i:opLogic[i] for i in a.logic}
                results.update(genAndRunAddress("int", subList, a.wLen, a.vLen, archName, a.keep))
                subList = {i:opAritmeticalShift[i] for i in a.arithmShift}
                results.update(genAndRunAddress("int", subList, a.wLen, a.vLen, archName, a.keep))
        out = ""
    #    print (results)
        db = {}
        for k in results:
            if results[k]: # Keep only valid results
                try:
                    db[(k[0], k[1], k[2], k[3], k[4])].append(k[5])
                except KeyError:
                    try:
                        db[(k[0], k[1], k[2], k[3], k[4])] = [k[5],]
                    except :
                        print(k)
                        print((k[0], k[1], k[2], k[3], k[4]))
                        print(k[5])
                # for v in k:
                #     out += str(v) +";"
                # out += "\n"
        data = "ArchName;Param;Op;Arith;vLen;wLen\n"
        for l in db:
            data += "%s;%s\n"%(";".join(l), ";".join(db[l]))
        with open (csvFileName, "w") as f:
            f.write(data)
        print ("Results in "+csvFileName)
