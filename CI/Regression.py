#!/usr/bin/env python3

def readCSV(fpath):
	d = []
	inputFile = open(fpath, 'r')
	csvReader = csv.reader(inputFile,delimiter=";")
	header = next(csvReader)[:]
	for row in csvReader:
		dic = dict (zip (header, row))
		d.append (dic)
	inputFile.close()
	return d

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
             "If",
             "If-in-Loop",
             "Loop-in-If",
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
    "CxRAM-Convolution32",
    "CxRAM-MatrixMultiplication"
    )

FailOK = { "cxram" : {"V2.2" : ("CxRAM-SimpleMul8",
                                "CxRAM-SimpleMul16",
                                "CxRAM-SimpleMul32",
                                "CxRAM-Convolution8",
                                "CxRAM-Convolution16",
                                "CxRAM-Convolution32",
                                "CxRAM-MatrixMultiplication"),
                      "V2.3" : ("CxRAM-SimpleMul32",
                                "CxRAM-SimpleMul32",
                                "CxRAM-Convolution32",
                                "CxRAM-MatrixMultiplication"),
                      "V3.0" : ("CxRAM-SimpleMul32",
                                "CxRAM-SimpleMul32",
                                "CxRAM-Convolution32",
                                "CxRAM-MatrixMultiplication")},
           "aarch64" : "",
           "riscv"   : "",
           "power"   : ""}

allArchList = ("aarch64", "riscv", "power")
archExt= {"riscv": ["RV32I","RV32F", "RV32M", "RV32D"],
          "power": ["p1", "ppc"],}

errMsg = {0:    "OK",
          251 : "Failed code gen",
          252 : "Bad exec result",
          253 : "Bad static compil",
          254 : "Bad HybroLang compil",
          255 : "Bad C compiler environment",
}

if __name__ == "__main__":
    import sys, subprocess, argparse, csv

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--isa', help='ISA version (ex : 2.3)', default='V2.3')
    parser.add_argument('-r', '--reportName', help='Path to the tests report', default='CI/Report/Report_kernel_test')
    parser.add_argument('-a', '--arch', help='Architecture (ex : aarch64, cxram)', required=True)
    only1param = parser.add_mutually_exclusive_group()
    only1param.add_argument('-t', '--test', help='Compile et lance les tests unitaires', action="store_true")
    only1param.add_argument('-z', '--analyse', help='Analyse test report and return fail instructions', action="store_true")
    arg = parser.parse_args()

    Verbose = False # To debug cmd
    printCmd = False
    if arg.test:
        testList = commonTestList
        if arg.arch == "cxram":
            testList = cxramTestList
        else:
            archList = allArchList
        cmd (["mkdir", "Report"], Verbose, wdir="CI/")
        file = open("%s_%s_%s.csv"%(arg.reportName, arg.arch, arg.isa), "w")
        file.write("kernel;result\n")
        print (" "*24 + "%23s"%arg.arch)
        for testFile in testList:
            print ("%24s"%testFile, end="")
            #commande = tuple(["./RunDemo.py", "-i", testFile, "-a", archName] + archExt[archName])
            commande = tuple(["./RunDemo.py", "-i", testFile, "-a", arg.arch],)
            o = cmd (commande, Verbose, doPrint = printCmd, wdir= "CodeExamples/")
            print ("  %23s"%(errMsg[o]))
            file.write("%s;%d\n"%(testFile, o))
        commande = tuple(["./RunDemo.py", "-c"])
        o = cmd (commande, Verbose, doPrint = printCmd, wdir="CodeExamples/")
        file.close()

    elif arg.analyse:
        report = readCSV("%s_%s_%s.csv"%(arg.reportName, arg.arch, arg.isa))
        tmp=""
        if arg.arch == "cxram" and arg.isa in FailOK["cxram"]:
            FailOKList = FailOK["cxram"][arg.isa]
        elif arg.isa != "cxram":
            FailOKList = FailOK[arg.arch]
        else :
            FailOKList = ("")
        for test in report:
            if test["kernel"] in FailOKList:
                continue
            if test["result"] != "0":
                tmp += "%s -> %s\n"%(test["kernel"], errMsg[int(test["result"])])
        if tmp!= "":
            print("TEST ECHEC !\nList of failed tests :\n%s"%tmp)
            sys.exit(-1)
        print("All TESTS SUCCES")

    else:
        sys.stderr.write("ERREUR: This script need args (-h for help)\n")
        sys.exit(-1)
