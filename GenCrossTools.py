#!/usr/bin/env python3
# -*- coding: utf-8 -*-

urlDataBase = {}                # Will contain rootDatabase + platform dependent modifications
rootDataBase = {
    'mpfr' :     {
        'url': 'https://ftp.gnu.org/gnu/mpfr/mpfr-{RELEASE}.tar.xz',
        'release':'4.2.0',
        'confargs' : ('--prefix={PREFIX}', '--program-prefix={TARGET}-', "--with-gmp={PREFIX}"),
        'targetbuild':'all',
        'targetinstall':'install',
    },
    'gmp' :     {
        'url': 'http://ftp.gnu.org/pub/gnu/gmp/gmp-{RELEASE}.tar.xz',
        'release':'6.2.1',
        'confargs' : ('--prefix={PREFIX}', '--program-prefix={TARGET}-'),
        'targetbuild':'all',
        'targetinstall':'install',
    },
    'mpc' :     {
        'url': 'http://www.multiprecision.org/downloads/mpc-{RELEASE}.tar.gz',
        'release':'1.3.1',
        'confargs' : ('--prefix={PREFIX}', '--program-prefix={TARGET}-', '--with-mpfr={PREFIX}', '--with-gmp={PREFIX}'),
        'targetbuild':'all',
        'targetinstall':'install',
    },
    'gcc'  :     {'url':'https://ftp.gnu.org/gnu/gcc/gcc-{RELEASE}/gcc-{RELEASE}.tar.gz',
                  'release':'13.2.0',
                  'confargs': ( '--prefix={PREFIX}', '--program-prefix={TARGET}-',
                                '--target={TARGET}', '--build=x86_64-linux-gnu', '--host=x86_64-linux-gnu',
                                '--with-gnu-as', '--with-gnu-ld', '--disable-nls',
                                '--enable-languages=c,c++',
                                '--without-headers',
                                '--disable-threads', '--disable-multilib',
                                '--disable-libgcj', '--disable-libgomp',
                                '--disable-shared',
                                '--enable-lto',
                        #         '--disable-werror',
                                '--with-gmp={PREFIX}', '--with-mpc={PREFIX}', '--with-isl={PREFIX}', '--with-mpfr={PREFIX}',
                                #'--with-sysroot={PREFIX}'
                  	),
                  'targetbuild':   'all-gcc',
                  'targetinstall': 'install-gcc',
    },
    # Links between binutils & gcc : https://wiki.osdev.org/Cross-Compiler_Successful_Builds
    'binutils' : {'url':'https://ftp.lip6.fr/pub/gnu/binutils/binutils-{RELEASE}.tar.gz',
                  'release':'2.40',
                  'confargs':  ('--prefix={PREFIX}', '--program-prefix={TARGET}-', '--target={TARGET}'
                                '--disable-nls', '--disable-werror', '--target={TARGET}'
                  ),
                  'targetbuild': 'all',
                  'targetinstall': 'install',
    },
    'gdb'  :     {'url':'https://ftp.lip6.fr/pub/gnu/gdb/gdb-{RELEASE}.tar.gz',
                  'release':'10.1',
                  'confargs': ('--prefix={PREFIX}', '--target={TARGET}',  '--program-prefix={TARGET}-',
                               '--enable-werror=no',
                  ),
                  'targetbuild':   'all',
                  'targetinstall': 'install',
    },
    'linux' :  {
        'url': 'https://mirrors.edge.kernel.org/pub/linux/kernel/v5.x/linux-{RELEASE}.tar.gz',
        'release': '5.18.17',
        'confargs': '',
        'targetbuild':   'headers_install',
        },
    'newlib': { 'url':'https://sourceware.org/pub/newlib/newlib-{RELEASE}.tar.gz',
                'release' : '4.3.0.20230120',
                'confargs' : ('--prefix={PREFIX}', '--target={TARGET}', '--disable-multilib', '--enable-lite-exit'),
                # --enable-newlib-register-fini --enable-newlib-global-atexit # Other interesting configuration parameters
                'targetbuild':   'all',
                'targetinstall': 'install',
    },
    'glibc': { 'url':'https://ftp.gnu.org/gnu/glibc/glibc-{RELEASE}.tar.gz',
               'release' : '2.37',
               'confargs' : ('--prefix={PREFIX}/{TARGET}', '--build=x86_64-pc-linux-gnu', '--host={TARGET}', '--target={TARGET}',
                             '--with-headers={PREFIX}/{TARGET}/include/',
                             '--disable-multilib', 'libc_cv_forced_unwind=yes',
               ),
               # 'targetbuild':   ('install-bootstrap-headers=yes', 'install-headers'),
               # 'targetinstall': 'install',
    },
    'qemu' : {
        'url':'https://download.qemu.org/qemu-{RELEASE}.tar.xz',
        'release': '8.0.3',
        'confargs' : ('--prefix={PREFIX}', '--target-list={TARGET}',
                      '--enable-plugins', '--gdb={PREFIX}/bin/{TARGET}-gdb'),
        'targetbuild':   'all',
        'targetinstall': 'install',
    },
    'isl' : {
        'url': 'https://sourceforge.net/projects/libisl/files/isl-{RELEASE}.tar.gz',
        'release': '0.26',
        'confargs' : ('--prefix={PREFIX}', '--with-gmp-prefix={PREFIX}', '--with-gmp=system'),
        'targetbuild':   'all',
        'targetinstall': 'install',
    },
}


def cmd(cmdAndArgs, doPrint = True, wdir=None, doExec = True, environ = None):
    if (doPrint):
        if wdir != None:
            print("-->cd %s"%(wdir))
        # if environ != None :
        #     for P in ("PATH", "LD_LIBRARY_PATH"):
        #         print("%s=%s"%(P, environ[P]))
        print("-->%s"%(" ".join(cmdAndArgs)))
    returncode = 0
    data = "Success"
    if doExec:
        process = subprocess.Popen(cmdAndArgs, cwd=wdir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env= environ)
        data = process.stdout.read()
        returncode = process.wait()
    if 0 == returncode:
        return data
    else:
        print("Error :")
        lines = data.decode ("utf8").split("\n")
        print('\n'.join(lines[-30:-1]))
        sys.exit(-1)

def usage(message):
    print(message)
    sys.exit(-1)

def Trace(message, args, verbose = False):
    if verbose:
        print("-->%s"%message)

def Step(message, tool, archTriplet, verbose = False):
    print("%10s %20s ==>%s"%(tool, archTriplet, message))

def getFilename(tool, release, args):
    nameFromUrl = urlDataBase[tool]["url"].split('/')[-1].format(RELEASE=release)
    # print(nameFromUrl)
    return args.workingdir+"/tgz/"+nameFromUrl

def downloadTool(tool, arch, args):
    release = urlDataBase[tool]["release"]
    fichier = getFilename(tool, release, args)
    url = urlDataBase[tool]["url"].format(RELEASE=release)
    if not os.path.isfile(fichier):
        cmd(["wget", "-O", fichier, url], args.verbose, doExec = args.donot)
        Trace ("%s fetched"%fichier, args)
    else:
        Trace("%s already exist"%fichier, args)
    return fichier

def cleanBuild(args, buildDir):
    """Clean install directories"""
    Trace("Clean build directories", args, args.verbose)
    cmd (["rm", "-rf", buildDir], args.verbose, doExec = args.donot)

def getEnv(archTriplet, args):
    myEnv = os.environ.copy()
    myEnv['PATH'] += ':%s/bin:'%args.prefix
    myEnv['PATH'] += ':%s/%s/bin:'%(args.prefix, archTriplet)
    ld = '%s/lib:%s/%s/lib'%(args.prefix, args.prefix, archTriplet)
    if 'LD_LIBRARY_PATH' in myEnv:
        myEnv['LD_LIBRARY_PATH'] += ":"+ld
    else:
        myEnv['LD_LIBRARY_PATH'] = ld
    return myEnv

def buildTool(tool, archTriplet, arch, args):
    """Build tools"""
    Step("Build tools ", tool, archTriplet)
    release = urlDataBase[tool]["release"]
    jobMax = str(multiprocessing.cpu_count()*4)
    toolName = tool + '-'+release
    buildDir = "%s/build/%s/%s/"%(args.workingdir, toolName, archTriplet)
    srcdir =   "%s/src/%s/"%(args.workingdir, toolName)
    cleanBuild (args, buildDir)
    cmd (["mkdir", "-p", srcdir, buildDir], args.verbose,   doExec = args.donot)
    cmd (["tar", "xf", getFilename (tool, release, args)], args.verbose, srcdir, doExec = args.donot)
    commande = "%s/%s/configure"%(srcdir, toolName)
    myEnv = getEnv(archTriplet, args)
    aList = [p.format(PREFIX=args.prefix, TARGET=archTriplet) for p in urlDataBase[tool]["confargs"]]
    cmd ([commande] + aList, args.verbose, buildDir, environ=myEnv, doExec = args.donot)
    target = urlDataBase[tool]["targetbuild"]
    cmd (["make", "-j", jobMax, target],  args.verbose, buildDir, environ=myEnv, doExec = args.donot)

def installQemuPlugin (tool, args):
    print("Install CxRAM qemu plugin from it' repository")
#     buildDir = "%s/tmp/build/%s/%s/"%(args.workingdir, tool, tool)
#     cmd (["mkdir", "-p", buildDir], True,   doExec = args.donot)
#     cmd (["tar", "xf", "%s/tgz/csram-qemu-plugin-V1.4.tgz"%args.workingdir], True, buildDir,  doExec = args.donot)
# #    cmd (['git' ,'clone', 'git@git-dscin.intra.cea.fr:hybrogen/csram-qemu-plugin.git'], True,  wdir = buildDir)
#     installDir = '%s/libexec/qemu/'%args.prefix
#     cmd (['make', 'getQemuSrc', 'all', 'install', 'QEMUINSTALLDIR=%s'%installDir], True, buildDir)

def installTool(tool, archTriplet, arch, args):
    """Install tools"""
    Step("Install tools", tool, archTriplet)
    release = urlDataBase[tool]["release"]
    toolName = tool + '-'+release
    buildDir = "%s/build/%s/%s/"%(args.workingdir, toolName, archTriplet)
    srcdir =   "%s/src/%s/"%(args.workingdir, toolName)
    myEnv = getEnv(archTriplet, args)
    target = urlDataBase[tool]["targetinstall"]
    jobMax = str(multiprocessing.cpu_count()*4)
    cmd (["make", "-j", jobMax, target],  args.verbose, buildDir, environ=myEnv, doExec = args.donot)

def buildLinuxIncludes(tool, archTriplet, arch, args):
    """Build tools"""
    flagFile = args.prefix+".alreadyinstalled-%s"%tool
    if (os.path.isfile (flagFile)):
        Trace ("--> %s for %s already installed"%(tool, arch), args)
        return
    Step("Build tools", tool, archTriplet)
    release = urlDataBase[tool]["release"]
    toolName = tool + '-'+release
    srcdir =   "%s/src/%s/"%(args.workingdir, toolName)
    downloadTool (tool, archTriplet, args)
    cmd (["mkdir", "-p", srcdir], args.verbose,   doExec = args.donot)
    cmd (["tar", "xf", getFilename (tool, release, args)], args.verbose, srcdir, doExec = args.donot)
    myEnv = getEnv(archTriplet, args)
    target = urlDataBase[tool]["targetbuild"]
    cmd (("make", "ARCH="+arch, "INSTALL_HDR_PATH="+args.prefix+archTriplet, target), args.verbose, srcdir+toolName, environ=myEnv, doExec = args.donot)
    cmd (("touch", flagFile), args.verbose)

def buildGlibcAndGcc(tool, archTriplet, arch, args):
    """Build tools"""
    flagFile = args.prefix+".alreadyinstalled-%s"%tool
    if (os.path.isfile (flagFile)):
        Trace ("--> %s for %s already installed"%(tool, arch), args)
        return
    Step("Build glibc 1st step", tool, archTriplet)
    release = urlDataBase[tool]["release"]
    toolName = tool + '-'+release
    srcdir =   "%s/src/%s/"%(args.workingdir, toolName)
    buildDir = "%s/build/%s/%s/"%(args.workingdir, toolName, archTriplet)
    jobMax = str(multiprocessing.cpu_count()*4)
    downloadTool (tool, archTriplet, args)
    cmd (["mkdir", "-p", srcdir, buildDir], args.verbose,   doExec = args.donot)
    cmd (["tar", "xf", getFilename (tool, release, args)], args.verbose, srcdir, doExec = args.donot)
    myEnv = getEnv(archTriplet, args)
    commande = "%s/%s/configure"%(srcdir, toolName)
    aList = [p.format(PREFIX=args.prefix, TARGET=archTriplet) for p in urlDataBase[tool]["confargs"]]
    cmd (([commande] + aList), args.verbose, buildDir, environ=myEnv, doExec = args.donot)
    cmd (("make", "install-bootstrap-headers=yes", "install-headers"), args.verbose, buildDir, environ=myEnv, doExec = args.donot)
    cmd (("make", "csu/subdir_lib"), args.verbose, buildDir, environ=myEnv, doExec = args.donot)
    cmd (("install", "csu/crt1.o", "csu/crti.o", "csu/crtn.o", args.prefix+archTriplet+"/lib"), args.verbose, buildDir, environ=myEnv, doExec = args.donot)
    cmd ((args.prefix+"/bin/"+archTriplet+"-gcc", "-nostdlib", "-nostartfiles", "-shared", "-x", "c", "/dev/null", "-o", args.prefix+"/lib/libc.so"), args.verbose, buildDir, environ=myEnv, doExec = args.donot)
    cmd (("touch",  args.prefix+archTriplet+"/include/gnu/stubs.h"), args.verbose, buildDir, environ=myEnv, doExec = args.donot)

    Step("Build gcc 2nd (last) step", "gcc", archTriplet)
    toolName2 = 'gcc-'+ urlDataBase["gcc"]["release"]
    buildDir2 = "%s/build/%s/%s/"%(args.workingdir, toolName2, archTriplet)
    cmd (("make", "-j", jobMax, "all-target-libgcc"),     args.verbose, buildDir2, environ=myEnv, doExec = args.donot)
    cmd (("make",               "install-target-libgcc"), args.verbose, buildDir2, environ=myEnv, doExec = args.donot)

    Step("Build glibc 2nd (last) step", "gcc", archTriplet)
    cmd (("make", "-j", jobMax),    args.verbose,  buildDir, environ=myEnv, doExec = args.donot)
    cmd (("make",               "install"), args.verbose, buildDir, environ=myEnv, doExec = args.donot)
    cmd (("touch", flagFile), args.verbose, doExec = args.donot)


def install(tool, archTriplet, arch, args):
    flagFile = args.prefix+".alreadyinstalled-%s"%tool
    if (os.path.isfile (flagFile)):
        Trace ("--> %s for %s already installed"%(tool, arch), args)
    else:
        downloadTool (tool, archTriplet, args)
        buildTool    (tool, archTriplet, arch, args)
        installTool  (tool, archTriplet, arch, args)
        cmd (("touch", flagFile), args.verbose)
targetsAlias = {
    'aarch64':       {'triplet': 'aarch64-linux-gnu',        'qemu':'aarch64-linux-user'},
    'riscv':         {'triplet': 'riscv32-linux-gnu',        'qemu':'riscv32-linux-user'},
    'powerpc':       {'triplet': 'powerpc64le-linux-gnu',    'qemu':'ppc64le-linux-user'},
    'cxram-linux':   {'triplet': 'riscv32-unknown-linux',    'qemu':'riscv32-linux-user'},
    'cxram-bm':      {'triplet': 'riscv32-unknown-elf',      'qemu':'riscv32-linux-user'},
    'kalray':        {'triplet': 'kvx-elf'},
    }
optSubDirs = ("src", "build", "tgz")

def checkDependency(args):
    """ Check needed software """
    Trace("==> Check tools dependency", args, args.verbose)
    BdDeps = (("wget", "for GenCrossTools"),
              ("m4",   "for gmp"),
              ("make", "all packages"),
              ("bash", "all packages"),
              ("ninja","for qemu"),
              ("bison","for glibc (sudo apt install bison)"),
              ("gcc",  "all packages"),
    )
    fail = False
    for dep in BdDeps:
        try:
            cmd(["which", dep[0]], doPrint=False)
        except:
            print("%s is a dependency for %s"%(dep[0], dep[1]))
            fail = True
            pass

    # fileList =(("/usr/lib/x86_64-linux-gnu/libglib-2.0.so", "for qemu (apt install libglib2.0-dev)"),)
    # /usr/lib/libglib-2.0.so : machines aar

    # for f in fileList:
    #     if not os.path.isfile(f[0]):
    #         print("%s is a dependency for %s"%(f[0], f[1]))
    #         fail = True
    #         pass
    if fail:
        sys.exit(-1)

def checkDirs(args):
    """Check directories"""
    Trace("==> Check directories", args, args.verbose)
    # if not os.path.exists (args.workingdir):
    #     usage ("Inexistant working dir: %s"% args.workingdir)
    if not os.path.exists (args.prefix):
        cmd(["mkdir", "-p", args.prefix], args.verbose)
    for d in optSubDirs:
        dd = args.workingdir+"/"+d
        if not os.path.exists (dd):
            cmd(["mkdir", "-p", dd], args.verbose)

codeToTest = (
    ("HelloWorld", '#include <stdio.h>\nint main(int argc, char * argv[]){printf("Hello World\\n");\nreturn 0;\n} ', b'Hello World\n' ),
    ("Add", '#include <stdio.h>\nint main(int argc, char * argv[]){int a = 3, b = 39; printf("%d\\n", a+b);\n;\nreturn 0;\n} ', b'42\n'
),
    ("FAdd", '#include <stdio.h>\nint main(int argc, char * argv[]){float a = 3.0, b = 39.0; printf("%f\\n", a+b);\n;\nreturn 0;\n} ', b'42.000000\n'
),
)

def writeSourceFile(testList):
    fileName = testList[0]+".c"
    f = open("/tmp/"+fileName, "w")
    f.write(testList[1])
    f.close()

def testInstall(archName, archTriplet, args):
    myEnv = getEnv(archTriplet, args)
    for testSrc in codeToTest:
        print("Test %s for %s"%(testSrc[0], archName))
        writeSourceFile(testSrc)
        result = testCompile(archName, archTriplet, args, testSrc[0], myEnv)
        if (result == testSrc[2]):
            print ("OK")
        else:
            print ("FAIL")
def testCompile(archName, archTriplet, args, fileName, env):
    cCode = "/tmp/"+fileName+".c"
    binCode = "/tmp/"+fileName
    cmd(['%s/bin/%s-gcc'%(args.prefix, archTriplet), "-v"], environ=env)
    cmd(['%s/bin/%s-gcc'%(args.prefix, archTriplet), "-c", cCode, ], environ=env)
    cmd(['%s/bin/%s-gcc'%(args.prefix, archTriplet), cCode, "-o", binCode], environ=env)
    if archName == "powerpc":
        qname = "qemu-ppc64le"
    elif archName in ("riscv", "cxram-bm", "cxram-linux"):
        qname = "qemu-riscv32"
    elif archName == "aarch64":
        qname = "qemu-aarch64"
    else:
        usage("Which qemu for %s ?"%archName)
    return cmd(['%s/bin/%s'%(args.prefix, qname), binCode], environ=env)


def removeSubDirs(args):
    for d in optSubDirs:
        if d == "tgz":
            continue
        commande = ["rm", "-rf", args.workingdir+"/"+d]
        cmd (commande, args.verbose, doExec = args.donot)

def writeIfNotExist(outputFileName, data):
    if not os.path.isfile(outputFileName):
        print("Writed in : "+outputFileName)
        f = open(outputFileName, "w")
        f.write(data)
        f.close()
    else:
        print ("File exists : "+outputFileName)
def removeInstallDirs(args):
    for d in args.arch:
        triplet = targetsAlias[d[0]]['triplet']
        commande = ["rm", "-rf", args.archprefix+"/"+d[0]]
        cmd (commande, args.verbose, doExec = args.donot)

if __name__ == '__main__' :
    import argparse, os, sys, subprocess, multiprocessing

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--arch', help='Target architectures',
                        choices=targetsAlias.keys(), nargs="+", action="append", required=True)
    parser.add_argument('-p', '--archprefix', help='Installation prefix', default="/opt/H2/")
    parser.add_argument('-w', '--workingdir', help='Working directory',   default="/opt/H2/tmp/")
    parser.add_argument('-v', '--verbose',    help='Verbose',                      action='store_true')
    parser.add_argument('-n', '--donot',      help='Do nothing, just print actions', action='store_false')
    parser.add_argument('-c', '--clean',      help='Clean build directories',      action='store_true')
    parser.add_argument('-t', '--test',       help='Test a cross build installation', action='store_true')
    parser.add_argument('-C', '--cleandist',  help='Clean build directories',      action='store_true')
    parser.add_argument('-f', '--config',     help='Show tools configuration',     action='store_true')
    parser.add_argument('-s', '--shell',      help='Generate shell configuration', action='store_true')
    args = parser.parse_args()

#    print(args)
    if not args.workingdir.endswith("/"):
         args.workingdir += "/"
    if not args.archprefix.endswith("/"):
         args.archprefix += "/"

    # Argument semantic
    if args.clean:
        answer = input ("Clean build directories (yes or ..) ? ")
        if "yes" != answer:
            print("abort clean")
        else:
            removeSubDirs(args)
    elif args.test:
        for a in args.arch:
            archName = a[0]
            args.prefix = "%s%s/"%(args.archprefix, archName)
            testInstall(archName, targetsAlias[archName]['triplet'], args)
    elif args.shell:            # Generate shell environment for args.arch
        binList = []
        libList = []
        for a in args.arch:     # Find installed directory
            thePrefix = args.archprefix
            binList.append("%s%s/bin/"%(thePrefix, a[0]))
            libList.append("%s%s/lib/"%(thePrefix, a[0]))
            libList.append("%s%s/%s/lib/"%(thePrefix, a[0], targetsAlias[a[0]]["triplet"]))
            fail = False
            # Generate environment variable depending on the parent shell
            binList.append ("/bin/") # Needed on CEA aar environment
            binList.append ("%s/hybrogen/bin/"%(thePrefix))
            ppid = os.getppid()
            fInput = open('/proc/%d/cmdline'%ppid, "r")
            parentProcessName = fInput.read().split('\x00')[0]
            if parentProcessName in ("bash", "-bash", "sh"):
                shEnv =  "export PATH=%s:${PATH}\n"% ":".join(binList)
                shEnv += "export LD_LIBRARY_PATH=%s:${LD_LIBRARY_PATH}\n"% ":".join(libList)
                if a[0] in ("cxram-linux", "cxram-bm", ):
                    qemuPlugin = "%s%s/libexec/qemu/libCxRAM-qemu-plugin.so"%(args.archprefix, a[0])
                    shEnv += "export QEMU_PLUGIN=%s\n"%qemuPlugin
                writeIfNotExist(args.archprefix+a[0]+"/.bashrc", shEnv)
            elif parentProcessName in ("csh", "-csh", "tcsh", "-tcsh"):
                cshEnv  = "setenv PATH %s:${PATH}\n"% ":".join(binList)
                cshEnv += "setenv LD_LIBRARY_PATH %s:${LD_LIBRARY_PATH}\n"% ":".join(libList)
                if a[0] in ("cxram-linux", "cxram-bm", ):
                    qemuPlugin = "%s%s/libexec/qemu/libCxRAM-qemu-plugin.so"%(args.archprefix, a[0])
                    cshEnv += "setenv QEMU_PLUGIN %s\n"%qemuPlugin
                writeIfNotExist(args.archprefix+a[0]+"/.cshrc", cshEnv)
            else:
                print ("Unknown environment for %s"%parentProcessName)
    elif args.config:
        for a in rootDataBase.keys():
            print ("%10s : %s"%(a, rootDataBase[a]["release"]))
    elif args.cleandist:
        answer = input ("Clean build directories & previously install (yes or ..) ? ")
        if "yes" != answer:
            print("abort clean")
        else:
            removeSubDirs(args)
            removeInstallDirs(args)
    else:
        checkDependency(args)
        for a in args.arch:
            archName = a[0]
            if archName not in targetsAlias.keys():
                usage("Unknown arch")
        for a in args.arch:
            urlDataBase = {}
            for k in rootDataBase: # Copy sub dictionnary = or copy is not enough !
                urlDataBase[k] = rootDataBase[k].copy()
            archName = a[0]
            args.prefix = "%s%s/"%(args.archprefix, archName)
            Step("== Start build ==", "cross tools", archName)
            checkDirs(args)
            # gcc dependencies
            archTriplet = targetsAlias[archName]['triplet']
            install("binutils", archTriplet, archName, args)
            install("gmp",      archTriplet, archName, args)
            install("isl",      archTriplet, archName, args)
            install("mpfr",     archTriplet, archName, args)
            install("mpc",      archTriplet, archName, args)
            theArch = archName
            if archName in ("cxram-bm", "cxram-linux"):
                theArch = "riscv"
            elif archName == "aarch64":
                theArch = "arm64"
            buildLinuxIncludes("linux", archTriplet, theArch, args)

            # Additionnal configuration parameter
            urlDataBase['qemu']['confargs'] += ('--interp-prefix=%s/%s/'%(args.prefix, archTriplet),)
            if archName == "cxram-bm":
                urlDataBase['gcc']['confargs'] += ("--with-newlib", "--with-arch=rv32gc", "--with-abi=ilp32",)
            elif archName == "cxram-linux":
                urlDataBase['gcc']['confargs'] += ("--with-arch=rv32gc", "--with-abi=ilp32",)
            elif archName == "powerpc":
                urlDataBase['gcc']['confargs'] += ('--with-long-double-128', ) #'--with-long-double-format=ibm', # for power)

            # Build 1st gcc steps
            install("gcc",      archTriplet, archName, args)
            # Build glibc (power) or newlib (riscv & csram) and gcc last steps
            if archName in ("powerpc", "cxram-linux", "aarch64", "riscv"):
                buildGlibcAndGcc("glibc",      archTriplet, archName, args) # glibc 1 step, gcc last step, glibc laststep
            elif archName in ("cxram-bm"):
                install("newlib",   archTriplet, theArch, args) # newlib
                Step("Build gcc last step", "gcc", archTriplet)
                toolName2 = 'gcc-'+ urlDataBase["gcc"]["release"]
                buildDir2 = "%s/build/%s/%s/"%(args.workingdir, toolName2, archTriplet)
                myEnv = getEnv(archTriplet, args)
                jobMax = str(multiprocessing.cpu_count()*4)
                cmd (("make", "-j", jobMax, "all-target-libgcc"),     args.verbose, buildDir2, environ=myEnv, doExec = args.donot)
                cmd (("make",               "install-target-libgcc"), args.verbose, buildDir2, environ=myEnv, doExec = args.donot)
            else:
                usage("Which libc / includes for architecture %s ?"%archName)
            install("gdb",      archTriplet, archName, args)
            install("qemu",     targetsAlias[archName]['qemu'], archName, args)
            # Additionnal stuff
            if archName in ("cxram-bm", "cxram-linux"):
                installQemuPlugin("csram-qemu-plugin", args)
            if archName == "powerpc" : #and (not os.path.islink(linkFile)):
                linkFile = "%s/%s/lib64"%(args.prefix, archTriplet)
                cmd (("ln", "-s", "lib", "lib64"), args.verbose, "%s/%s/"%(args.prefix, archTriplet), doExec = args.donot)
#
