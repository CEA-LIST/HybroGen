#!/usr/bin/env python3
import datetime
from pathlib import Path

everythingPass : bool = True


def cmd(cmdAndArgs, Verbose, doPrint = True, wdir = None, doExec = True):
#    print (cmdAndArgs)
    if (doPrint):
        if wdir != None:
            print("-->cd %s"%(wdir))
        print("-->%s"%(" ".join(cmdAndArgs)))
    returncode = 0
    data = ""
    if not doExec:
        return 0,""

    process = subprocess.Popen(cmdAndArgs, cwd=wdir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,text=True)
    stdout, _ = process.communicate()
    returncode = process.returncode
    if Verbose:
        print (stdout)
        print (f"Return code {returncode}")
    return returncode,stdout

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
    o,stdout = cmd (commH, False, doExec= realExec, doPrint = realPrint)
    if o != 0:
        print("error HybroLang Compil" + stdout)
        rmFiles (fileName, keep)
        return False,stdout
    commC = tuple([config.getCompilerForArch(arch), "-g", "-DH2_DEBUG", "-o", fileName, fileName+"."+arch+".c"])

    o,stdout = cmd (commC, False, doExec= realExec, doPrint = realPrint)
    if o != 0:
        print("compiler for arch failed" + stdout)
        rmFiles (fileName, keep)
        return False,stdout
    commR = tuple([config.getQemuForArch(arch), fileName]+dataset)
    o,stdout = cmd (commR, False, doExec= realExec, doPrint = realPrint)
    rmFiles (fileName, keep)
    if o != 0:
        # print("Fail at runtime bad result" + stdout)
        return False,stdout
    else:
        return True,stdout

def genAndRunValueOnce(testCase, keep):
    dataset = [str(i) for i in range (1,34)]
    resultDb = ""
    returnCode = 0
    fileName = f'./Tests/Test-{testCase["operator"]}-{testCase["arithmetic"]}-{testCase["wordLen"]}-{testCase["vectorLen"]}'
    c = CCodeValue(opArith[testCase["operator"]], testCase["arithmetic"],
                   testCase["wordLen"],  testCase["vectorLen"],
                   CTypeArray[testCase["arithmetic"]][testCase["wordLen"]])
    c.write(fileName+".hl")
    returnCode,msg = compileAndRun(fileName, archName, dataset[0:2*int(testCase["vectorLen"])], keep)
    resultDb  = msg
    return returnCode,resultDb

opArith = {"add":"+", "mul":"*", "sub":"-", "div":"/", "mod":"%", "or":"|", "xor":"^", "and":"&", "sl":"<<", "sr":">>"}
CTypeArray = {
    'int': {"8": 'int8_t',  "16":'int16_t', "32": 'int32_t', "64":'int64_t'},
    'flt': {"8": '_Float8', "16":'_Float16',"32": 'float',   "64":'double',},
}

def parseDataBase(archName):
    import csv
    fileName = f"RegressionSingleOp-{archName}.csv"
    csvRef = csv.DictReader(open (fileName, "r"), delimiter=";")
    return csvRef

if __name__ == "__main__":
    import sys, subprocess, argparse, os
    from CCode import CCodeValue
    sys.path.append("..")
    from SwConfig import SwConfig
    config = SwConfig()

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--arch',        nargs="+",           help='Architecture name list : %s'%config.getKeys())
    parser.add_argument('-k', '--keep',        action='store_true', help='Keep intermediate files')
    parser.add_argument('-c', '--clean',       action='store_true', help="Clear Result json file")
    parser.add_argument('-d', '--doRegression',action='store_true', help="Do regression")
    parser.add_argument('-v', '--verbose',     action='store_true', help='Verbose Mode')
    a = parser.parse_args()

    if None == a.arch:
        print ("Give at least one arch name %s"%config.getKeys())
        sys.exit(-1)
    if a.clean:
        print (f"Clean database for {'/'.join(a.arch)}")
        for archName in a.arch:
            clear_result("./json/RegressionSingleOp-"+archName+".json")
    elif a.doRegression:
        if not os.path.exists ("./Tests"):
            cmd(["mkdir", "-p", "./Tests"], True)
        print (f"Regression singleop for {'/'.join(a.arch)}")
        for archName in a.arch:
            print("try regression single op on " + archName)
            dataSet = parseDataBase(archName)
            for testCase in dataSet:
                result, msg = genAndRunValueOnce (testCase, a.keep)
                for k in testCase: print (f"{testCase[k]:8s}  ", end="")
                print (result)
                # if not result: print (msg)
        exit(everythingPass)
    else:
        print ("Give an action --clean --doRegression")
