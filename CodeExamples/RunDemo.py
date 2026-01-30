#!/usr/bin/env python3

demo ={
    # CodeExample Name          | Tests datas sets
    "Or32":  			(("170", "85"), ("255", "255"), ("170", "255"),),
    "Simple-Mac":  		(("2", "5", "8"),),
    "And32":  			(("255", "0"), ("255", "255"), ("170", "255"),),
    "Add8x1":  			(("39.0", "3.0"),),
    "Add16xX":			(("-l", "2", "1", "2",  "3", "4"),
                                 ("-l", "4", "1", "2", "3", "4", "5", "6", "7", "8"),),
    "Add32x1-flt": 		(("39.0", "3.0"),    	     ("39.0e12", "3.0"),           ("39.0e24", "3.0")),
    "Add32x1-int": 		(("0", "1"),                 ("1", "0"),                   ("100", "100000")),
    "Sub32x1-int": 		(("39", "45",),              ("2", "44")),
    "Sub32x1-flt": 		(("39.0", "45.0",),              ("2.0", "44.0")),
    "Sub16xX":			(("-l", "2",  "3", "4", "1", "2"),
                                 ("-l", "4", "5", "6", "7", "8", "1", "2", "3", "4"),),
    "Mult32x1-int":		(("24", "3"),                ("3", "24"),             ("100000", "100")),
    "Mult32x1-flt":		(("24.5", "3"),              ("3", "24"),             ("100000", "100")),
    "Div32x1-int":		(("24", "3"),                ("3", "24"),             ("100000", "100")),
    "Div32x1-flt":		(("24.5", "3"),              ("3", "24"),             ("100000", "100")),
    "Multiple-int":		(("24", "3"),                ("3", "24"),             ("100000", "100")),
    "Multiple-flt":		(("24.5", "3"),              ("3", "24"),             ("100000", "100")),
    "Add-With-Transprecision":  (("39.0", "3.0"),            ("39e-6", "3e-6"),       ("39e-12", "3e-12"),
                                 ("39e-18", "3e-18"),        ("39e-24", "3e-24"),     ("39e-32", "3e-32"),
                                ),
    "TestAdd1632":  (("39.0", "3.0"),            ("39e-6", "3e-6"),       ("39e-12", "3e-12"),
                                 ("39e-18", "3e-18"),        ("39e-24", "3e-24"),     ("39e-32", "3e-32"),
                                ),
    "Add-With-Specialization" : (("3", "25"),),
    "Mult-With-Specialization" : (("3", "25"), ("4", "25"), ("3", "32"), ("8", "32")),
    "CelciusFarenheit" : (("3",), ("25",),),
    "Array-St" : (("3",), ("5",)),
    "Array-Ld" : (("3",), ("5",)),
    "Array-St-flt" : (("3","12.0"), ("5","132.00")),
    "Array-Ld-flt" : (("3",), ("5",)),
    "Array-Mult-Specialization": (("10", "42",),),
    "If"          : (("42", "42"), ("4", "4"), ),
    "If-in-Loop"  : (("42", "42"), ("4", "4"), ),
    "Loop-in-If"  : (("1", "10"), ("0", "10"), ),
    "Loop"        : (("6", "7"), ("1000", "2"), ("2", "1000"), ),
    "LoopNest"    : (("1",), ("7",), ("42",)),
    "Constants-Operations"  : (("1",), ("7",), ("42",)),
    "Add8x16"     : (("1.0", "2.0", "2.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", )),
    "CxRAM-SimpleSub8" : ( ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", ),
                          ("1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", ),
                          ("10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", ),
                          ),
    "CxRAM-SimpleAnd" :  (("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", ),
                          ("1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", ),
                         ),
    "CxRAM-SimpleAdd8" :  (("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", ),
                          ("1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", ),
                         ),
    "CxRAM-SimpleAdd16" :  (("1", "2", "3", "4", "5", "6", "7", "8", "9", ),
                            ("1", "1", "1", "1", "1", "1", "1", "1", "1", ),
                         ),
    "CxRAM-SimpleAdd32" :  (("1", "2", "3", "4", "5", "6", "7", "8", "9", ),
                            ("1", "1", "1", "1", "1", "1", "1", "1", "1", ),
                         ),
    "CxRAM-SimpleMul8" :  (("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", ),
                          ("1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", ),
                         ),
    "CxRAM-SimpleMul16" :  (("1", "2", "3", "4", "5", "6", "7", "8", ),
                          ("1", "1", "1", "1", "1", "1", "1", "1", ),
                         ),
    "CxRAM-SimpleMul32" :  (("1", "2", "3", "4", ),
                          ("1", "1", "1", "1", ),
                         ),
    "CxRAM-ImageDiff" :  (("MonOeilGrisFermé.pgm","MonOeilGris.pgm",),
                          ),
    "CxRAM-ImagePixelAccumulation" :(("MonOeilGrisFermé.pgm",),
                                     ("MonOeilGris.pgm", ),),
    "CxRAM-Convolution8" : (("",),),
    "CxRAM-Convolution16" : (("",),),
    "CxRAM-Convolution32" : (("",),),
    "CxRAM-Broadcast32" :  (("",),),
    "CxRAM-MatrixMultiplication" : (("",),),
    "CxRAM-BoucleTest" :  (("",),),
    "Simple-Vector-Add" : (("1", "2", "3", "4", "5", "6", "7", "8"),),
    "FloatMatrixMultiplication" : (("",),),
    "MatrixMultiplication" : (("",),)
}

def fatalError(msg, code):
    print ("Error %s"%msg)
    sys.exit(code)

def cmd(cmdAndArgs, Verbose, doPrint = True, wdir = None, doExec = True):
    print (cmdAndArgs)
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

def compile (File, Arch, Debug, Verbose):
    compilerAndArg = [config.getCompilerForArch(Arch[0])]
    cmd(("rm", "-f", File, File+".c"), Verbose)
    o1 = 0
    o2 = 0
    cmdH2 = tuple(["../HybroLang.py", "--toC", "--arch"] + Arch + ["--inputfile", File+".hl"])
    o0 = cmd (["which", compilerAndArg[0]], Verbose)
    if 0 != o0:
        fatalError ("C Compiler not found (environment pb ?)", -1)
    if Debug:
        cmdH2 += ("--debug",)
    if Verbose:
        cmdH2 += ("--verboseParsing",)
    o1 = cmd(cmdH2, Verbose)
    if 0 != o1:
        fatalError ("Hybrogen compiler error", -2)
    if Debug:
        compilerAndArg += ["-g", "-DH2_DEBUG_INSN", "-DH2_DEBUG_REGISTER"]
    o2 = cmd(compilerAndArg + ["-DQEMU_TARGET", "-Wall", "-o", File, File+".c"], Verbose)
    if o2 != 0:
        fatalError ("C compilation compiler error", -3)
    return 0

def run(File, Arch, Verbose):
    emulatorAndArgs = (config.getQemuForArch(Arch),)
#    print(emulatorAndArgs)
    output = 0
    if demo[File] is None:
        output = cmd(emulatorAndArgs + (File,), Verbose)
    else:
        for param in demo[File]:
            # print(demo[File])
            # print(File)
            print(param)
            output += cmd(emulatorAndArgs + (File,)+ param, Verbose)
    if output != 0:
        return -4

def clean(Verbose):
    for p in demo:
        cmd(("rm", "-f", p, p+".c"), Verbose)

if __name__ == "__main__":
    import sys, subprocess, argparse
    sys.path.append("..")
    from SwConfig import SwConfig

    config = SwConfig()
    exampleMsg = "Arch in : %s\nDemo in %s"%(config.getKeys(), str(demo.keys()))
    p = argparse.ArgumentParser("HybroLang Demo compiler / compiler / launcher", epilog = exampleMsg)
    p.add_argument ('-g', '--debug',  action='store_true', help="debug version")
    p.add_argument ('-c', '--clean',  action='store_true', help="clean directory")
    p.add_argument ('-a', '--arch',   nargs='+', help="give arch parameter (archname & extension(s))")
    p.add_argument ('-i', '--inputfile', action="append", help="give demo name")
    p.add_argument ('-v', '--verbose',   action="store_true", help="print error messages")
    a = p.parse_args()
    print(a)
    if 1 == len(sys.argv):
        p.print_help(sys.stderr)
        sys.exit(0)
    if (a.clean):
        clean(a.verbose)
        sys.exit(0)
    else:
        Architecture = a.arch
        for Program in a.inputfile:
            if not Program.endswith (".hl"):
                o = compile(Program, Architecture, a.debug, a.verbose)
                if o != 0:
                    sys.exit(o)
                o = run (Program, a.arch[0], a.verbose)
                if o != 0:
                    sys.exit(o)
            else:
                print ("Give program name without extension : %s"%Program)
