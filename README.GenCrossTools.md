# Build, maintain and reproduct experiments in cross compilation environment

## Why

Build, debug and run binary application on multiple platforms
(powerpc, riscv, kalray, riscv with hardware accelerators) need
compilers, debuggers and simulators for each platforms. [Wikipedia, as
usual is very useful explaining what is a
cross-compiler](https://en.wikipedia.org/wiki/Cross_compiler).

The notions should be simple (compile for a target A
on a platform B) but the realization overcomplicated. Software package
are big (could need hours of compilation), there is dependency between
packages, there are problems between versions, operating system
version interact, optionnal switches are not coherent ...

For my research purposes I need to have cross-compilers and emulator
for multiple platforms, mainly RISCV, POWER, RISCV with
accelerators. Each host platforms provide a lot of pre-packaged
ones. For example
[Ubuntu linux distribution](https://packages.ubuntu.com/search?keywords=gcc) provide this
list, [FreeBSD operating system](https://www.freshports.org/search.php?query=gcc&amp;search=go) this one.

But for research and industrial reproducibility and mastering /
understanding the build configuration I do not want to use packaged
tools, i.e. build from sources, understand the configuration
options.

## What it does

* This script build those tools :
   * gcc and dependencies (gmp, isl, mpfr, mpc)
   * linux headers
   * glibc	or newlib depending on the platform
   * gdb
   * qemu
   * Check that the compiler / emulator works on small examples
   * Create PATH & LD_LIBRARY_PATH variables

in order to compile, run and debug code in cross environment, with a
coherent release set.

For this initial release the release set is :
~~~
>GenCrossTools.py -a riscv --config
      mpfr : 4.1.0
       gmp : 6.2.1
       mpc : 1.2.1
       gcc : 10.2.0
  binutils : 2.36.1
       gdb : 9.2
     linux : 5.4.60
    newlib : 4.1.0
     glibc : 2.33
      qemu : 5.2.0
       isl : 0.23
~~~

## How : GenCrossTools documentation

~~~
>GenCrossTools.py --help
usage: GenCrossTools.py [-h] -a {riscv,powerpc,cxram-linux,cxram-bm} [{riscv,powerpc,cxram-linux,cxram-bm} ...]
                        [-p ARCHPREFIX] [-w WORKINGDIR] [-v] [-n] [-c] [-t] [-C] [-f] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -a {riscv,powerpc,cxram-linux,cxram-bm} [{riscv,powerpc,cxram-linux,cxram-bm} ...], --arch {riscv,powerpc,cxram-linux,cxram-bm} [{riscv,powerpc,cxram-linux,cxram-bm} ...]
                        Target architectures
  -p ARCHPREFIX, --archprefix ARCHPREFIX
                        Installation prefix
  -w WORKINGDIR, --workingdir WORKINGDIR
                        Working directory
  -v, --verbose         Verbose
  -n, --donot           Do nothing, just print actions
  -c, --clean           Clean build directories
  -t, --test            Test a cross build installation
  -C, --cleandist       Clean build directories
  -f, --config          Show tools configuration
  -s, --shell           Generate shell configuration
~~~

Build configuration example :

* `GenCrossTools.py -a riscv` will build the tools for the riscv architecture
* `GenCrossTools.py -a riscv -t` will test the tools with some small
  code examples
* `GenCrossTools.py -a riscv -C` will remove both the build directory and tool directory
* `GenCrossTools.py -a riscv -c` will remove the build directory to gains space
* The tool try to not rebuild already installed tools. If you want to rebuild you can either use
   * use -C as shown previously or
   * remove the files  `${PREFIX}/.alreadyinstalled-TOOL`
* `GenCrossTools.py -a riscv -s` shows PATH & LD_LIBRARY_PATH for riscv
   * Could use multiple environment : `GenCrossTools.py -a riscv -a powerpc -s`
   * Be carrefull with aliases : `riscv32` and `cxram-linux` share the same compiler name ...

## Inspiring documentations and tools

* https://preshing.com/20141119/how-to-build-a-gcc-cross-compiler/
* http://crosstool-ng.github.io
* https://buildroot.org/
* https://github.com/narke/gcc-cross-compiler/blob/master/toolchain.py
* https://wiki.osdev.org/GCC_Cross-Compiler
* for linux on embedded platforms : https://elinux.org/Toolchains
* http://www.linuxfromscratch.org/lfs/downloads/stable/LFS-BOOK-10.0.pdf
