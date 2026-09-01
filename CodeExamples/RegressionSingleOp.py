#!/usr/bin/env python3
import datetime
import json
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
        print("Fail at runtime bad result" + stdout)
        return False,stdout
    else:
        return True,stdout

def genAndRunAddress(singleArith, opList, wordLenList, vectorLen, archName, keep=False):
    dataset = [str(i) for i in range (1,34)]
    resultDb = {}
    for op in opList:
        for wordLen in wordLenList:
#            print ("%5s : %5s(%03s)"%(singleArith, op, wordLen), end="")
            for vLen in vectorLen:
                if wordLen in CTypeArray[singleArith]:
                    theWordLen = "%03d"%int(wordLen)
                    theVectorLen = "%03d"%int(vLen)
                    fileName = "Tests/Test-Address-%s-%s-%s-%s-%s"%(op, singleArith, theWordLen, theVectorLen, archName)
                    print (fileName)
                    c = CCodeAddress(opList[op], singleArith, vLen, wordLen, CTypeArray[singleArith][wordLen])
                    c.write(fileName+".hl")
                    msg = compileAndRun(fileName, archName, dataset[0:2*int(vLen)], keep)
                    resultDb[op, singleArith, wordLen, vLen, "address", archName] = msg
    return resultDb

def genAndRunValue(singleArith, opList, wordLenList, vectorLen, archName, keep):
    dataset = [str(i) for i in range (1,34)]
    resultDb = {}
    for op in opList:
        for wordLen in wordLenList:
#            print ("%5s : %5s(%03s)"%(singleArith, op, wordLen), end="")
            for vLen in vectorLen:
                if wordLen in CTypeArray[singleArith]:
                    theWordLen = "%03d"%int(wordLen)
                    theVectorLen = "%03d"%int(vLen)
                    fileName = "Tests/Test-Value-%s-%s-%s-%s-%s"%(op, singleArith, theWordLen, theVectorLen, archName)
                    print (fileName)
                    c = CCodeValue(opList[op], singleArith, vLen, wordLen, CTypeArray[singleArith][wordLen])
                    c.write(fileName+".hl")
                    msg = compileAndRun(fileName, archName, dataset[0:2*int(vLen)], keep)
                    resultDb[op, singleArith, wordLen, vLen, "value", archName] = msg
    return resultDb



def genAndRunValueOnce(singleArith, op, opName, wordLen, vLen, archName, keep):
    dataset = [str(i) for i in range (1,34)]
    resultDb = ""
    wordLen = str(wordLen);
    returnCode = 0
    if wordLen in CTypeArray[singleArith]:
        fileName = "./Tests/Test-Value-%s-%s-%s-%s"%(opName, singleArith, wordLen, vLen)
        c = CCodeValue(op, singleArith, vLen, wordLen, CTypeArray[singleArith][wordLen])
        c.write(fileName+".hl")
        returnCode,msg = compileAndRun(fileName, archName, dataset[0:2*int(vLen)], keep)
        resultDb  = msg
    else : 
        print("error")
    return returnCode,resultDb

opArith = {"add":"+", "mul":"*", "sub":"-", "div":"/"}
opLogic = {"mod":"%", "or":"|", "xor":"^", "and":"&"}
opAritmeticalShift = {"sl":"<<", "sr":">>"}
CTypeArray = {
    'int': {"8": 'int8_t', "16":'int16_t', "32":'int32_t', "64":'int64_t',},
    'flt': {                               "32": 'float',  "64":'double',},
}




def check_file_access(filename):
    path = Path(filename)

    # Vérifie que le fichier existe
    if not path.is_file():
        raise FileNotFoundError(
            f"Le fichier '{filename}' n'existe pas."
        )

    # Vérifie les droits de lecture
    if not os.access(path, os.R_OK):
        raise PermissionError(
            f"Pas de droit de lecture sur '{filename}'."
        )

    # Vérifie les droits d'écriture
    if not os.access(path, os.W_OK):
        raise PermissionError(
            f"Pas de droit d'écriture sur '{filename}'."
        )

def clear_result(filename):
    try:
            check_file_access(filename)
            with open(filename, "r") as f:
                data = json.load(f)
            operators = data["operator"]
            for category, operations in operators.items():
                for operation, tests in operations.items():
                    for test in tests:
                        test["results"].clear()
            with open(filename, "w") as f:
                json.dump(data, f, indent=2)
            return 0
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        return -1
    except PermissionError as e:
        print(f"ERROR: {e}")
        return -2
    except json.JSONDecodeError as e:
        print(f"ERROR: JSON invalide : {e}")
        return -3
    except Exception as e:
        print(f"ERROR inattendue : {e}")
        return -99

def parse_operations(filename,archName,keep):
    try:
        check_file_access(filename)
        with open(filename, "r") as f:
            data = json.load(f)

        operators = data["operator"]

        for category, operations in operators.items():

            for operation, tests in operations.items():

                print(f"\n===== {category}/{operation} =====")

                for test in tests:

                    vLen = test["vLen"]
                    wLen = test["wLen"]
                    result = 0
                    msg = ""
                    if category == "arith":
                        result,msg = genAndRunValueOnce("int",opArith[operation],operation,wLen,vLen,archName,keep)
                    elif category == "logic":
                        result,msg = genAndRunValueOnce("int",opLogic[operation],operation,wLen,vLen,archName,keep)
                    elif category == "shift":
                        result,msg = genAndRunValueOnce("int",opAritmeticalShift[operation],operation,wLen,vLen,archName,keep)
                    else :
                        print("bad category found problem in json file")

                    if result :
                        result = "SUCCESS"
                        msg = ""
                    else :
                        result = "FAIL"
                        everythingPass = False
                    print(
                        f"vLen={vLen}, "
                        f"wLen={wLen}, "
                        f"result={result}, "
                        f"msg={msg}"
                    )

                    commit = subprocess.check_output(
                        ["git", "rev-parse", "--short", "HEAD"],
                        text=True
                    ).strip()
                    test["results"].append({
                    "date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "success": result,
                    "commit": commit,
                    "message": msg
                })
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        return 0
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        return -1
    except PermissionError as e:
        print(f"ERROR: {e}")
        return -2
    except json.JSONDecodeError as e:
        print(f"ERROR: JSON invalide : {e}")
        return -3
    except Exception as e:
        print(f"ERROR inattendue : {e}")
        return -99


if __name__ == "__main__":
    import sys, subprocess, argparse, os
    from CCode import CCodeValue
    from CCode import CCodeAddress
    sys.path.append("..")
    from SwConfig import SwConfig
    config = SwConfig()

    parser = argparse.ArgumentParser()
    if not os.path.exists ("./Tests"):
        cmd(["mkdir", "-p", "./Tests"], True)

    #Liste fichier json ajouter arch: architectureName dans json
    parser.add_argument('-a',   '--arch',     nargs="+",    default=config.getKeys(), help='Architecture name list')
    parser.add_argument('-k',   '--keep',     action='store_true', help='Keep intermediate files')
    parser.add_argument('-c', '--clean', action='store_true', help="Clear Result json file")
    parser.add_argument('-v', '--verbose', action='store_true',help='Verbose Mode')
    a = parser.parse_args()

    for archName in a.arch:
        print("Arch " + archName)


    if a.verbose==False:
        sys.stdout = open(os.devnull, 'w')

    if a.clean:
        for archName in a.arch:
            clear_result("./json/RegressionSingleOp-"+archName+".json")    
        exit(0)

    for archName in a.arch:
        print("try regression single op on " + archName)
        parse_operations("./json/RegressionSingleOp-"+archName+".json",archName,a.keep)

    exit(everythingPass)

