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

commonTestList = (
             "Add-With-Transprecision",
             "Add-With-Specialization",
             "Mult-With-Specialization",
             "Multiple-int",
             "Multiple-flt",
             "CelciusFarenheit",
             "Array-St",
             "Array-Ld",
             "Array-St-flt",
             "Array-Ld-flt",
             "Loop",
             "LoopNest",
)
cxramTestList =(
    "CxRAM-SimpleAnd",
    "CxRAM-SimpleAdd8",
    "CxRAM-SimpleAdd16",
    "CxRAM-SimpleAdd32",
    "CxRAM-SimpleSub8",
    "CxRAM-SimpleMul8",
    "CxRAM-SimpleMul16",
    "CxRAM-SimpleMul32",
    "CxRAM-ImageDiff",
    "CxRAM-ImagePixelAccumulation",
    "CxRAM-Broadcast32",
#    "CxRAM-Convolution8", # Convolution8 & 16 are not bit compatible
#    "CxRAM-Convolution16", # thus can not be used as regression test
    "CxRAM-Convolution32",
    "CxRAM-MatrixMultiplication"
    )
allArchList = ("aarch64", "riscv", "power", "kalray")
archExt= {"riscv": ["RV32I","RV32F", "RV32M", "RV32D"],
          "power": ["p1", "ppc"],
          "kalray": ["kalray"]}
errMsg = {0:    "OK",
          251 : "Failed code gen",
          252 : "Bad exec result",
          253 : "Bad static compil",
          254 : "Bad HybroLang compil",
          255 : "Bad C compiler environment",
}

if __name__ == "__main__":
    import sys, subprocess, argparse

    testList = commonTestList
    if len(sys.argv) > 1:
        archList = sys.argv[1:]
        if archList == ["cxram"]:
            testList = cxramTestList
    else:
        archList = allArchList
    print (" "*24, end="")
    for archName in archList:
        print ("%23s"%archName, end="")
    print()
    for testFile in testList:
        print ("%24s"%testFile, end="")
        for archName in archList:
            #commande = tuple(["./RunDemo.py", "-i", testFile, "-a", archName] + archExt[archName])
            commande = tuple(["./RunDemo.py", "-i", testFile, "-a", archName])
            o = cmd (commande, False, doPrint = False)
            print ("  %23s"%(errMsg[o]), end="")
        print()
    commande = tuple(["./RunDemo.py", "-c"])
    o = cmd (commande, False, doPrint = False)
