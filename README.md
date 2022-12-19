% Hybrogen Hybrid Code Generation, fast and small as the hydrogen element
% HP Charles

# Introduction

* After [ccg](https://pages.lip6.fr/vvm/projects_realizations/ccg/),
  [hpbcg](https://code.google.com/archive/p/hpbcg/), deGoal, the new
  HybroGen tool to generate efficent binary code

* General idea : Hybrogen is a tool which helps to generate
  compilette, compilettes are small code generators able to regenerate
  a part of an application at run-time. It aims to be fast (~10 cycles
  to generate 1 instruction) and small (KB code generator).

* How it works : it starts from an instruction set database containing
  instruction encoding, arithmetic, data width and vector length, we
  create a programming language (HybroLang) which allows to express
  data set variation & build a compiler which takes advantage of (1)
  data set variation and (2) hardware capability to modify the binary
  code at runtime.

* Many ![authors contributed](AUTHORS.md) to this code

* Many publications about dynamic code generation
    * 2004 : The invention of the "Compilette" term (based on old ccg tool) : "Efficient data driven run-time code generation" https://dl.acm.org/doi/pdf/10.1145/1066650.1066653
    * 2018 : Using binary code generation against side channel attacks (based on deGoal tool) ["Automated software protection for the masses against side-channel attacks"](https://dl.acm.org/doi/pdf/10.1145/3281662)
    * 2021 : Transprecision example (using HybroLang) : ["Dynamic compilation for transprecision applications on heterogeneous platform"](https://mdpi-res.com/d_attachment/jlpea/jlpea-11-00028/article_deploy/jlpea-11-00028-v2.pdf?version=1625022977)
    * 2021 : (using HybroLang) ["Instruction Set Design Methodology for In-Memory
Computing through QEMU-based System Emulator"](https://hal.archives-ouvertes.fr/hal-03449840/document)
# Installation Dependency

* Grammar use ANTLR4 with python4 backend
   * `sudo apt install antlr4`
   * `pip3 install antlr4-python3-runtime==4.7.2`
   * `pip install psycopg2-binary`
* Compilation need a postresql database. To install postgresql and configure it you can use this commands :
   * `sudo apt install postgresql`
   * `sudo -i -u postgres`
   * `createdb hybrogen`
   * `createuser --pwprompt hybrogen` # the default password in the code is "hybrogen"

It is a good practice to not create the database under your own
username. (The database should be multiuser accessible)

* Install a python postgresql connector:
   * `sudo apt install python3-psycopg2`

# Hybrogen installation

## For all supported platforms

* Put the `HybroGen-V2.0.tgz` file in an empty directory
* `tar xfz HybroGen-V2.0.tgz` To extract the source files
* Choose a target directory to install the release (user mode)
  e.g. `/opt/H2/`
* Run`./GenCrossTools.py -a riscv -p /opt/H2/ -w /opt/H2/tmp`
    * This command will generate the cross-compiler environment (gcc, gdb, qemu, linux-headers)
* Run `./GenCrossTools.py -a riscv -p /opt/H2/ -w /opt/H2/tmp -s`
    * This will generate the shell environment (csh like or bash like)
  to use the previously build binaries. Put this variables in your
  environment.
* Run `make buildGrammar` to build the ANTLR lexer / parser
* Run `make DbPopulate` to populate the SQL database with instructions description
* `cd CodeExamples`
* Run demonstration examples
   * ./RunDemo.py -a riscv -i Add32x1-flt

## For Computing in memory platform aka CXRAM

* Put the `HybroGen-V2.0.tgz` file in an empty directory
* `tar xfz HybroGen-V2.0.tgz` To extract the source files
* Choose a target directory to install the release (user mode)
  e.g. `/opt/H2/`
* Put the `csram-qemu-plugin-V2.0.tgz` file in `/opt/H2/tmp/tgz`
* Run`./GenCrossTools.py -a cxram-linux -p /opt/H2/ -w /opt/H2/tmp`
    * This command will generate the cross-compiler environment (gcc, gdb, qemu, linux-headers)
* Run `./GenCrossTools.py -a cxram-linux -p /opt/H2/ -w
  /opt/H2/tmp -s`
    * This will generate the shell environment to use the previously
  build binaries. Put this variables in your environment
* Run `make buildGrammar` to build the ANTLR lexer / parser
* Run `make DbPopulate` to populate the SQL database with instructions description
* `cd CodeExamples`
* Run demonstration examples
   * ./RunDemo.py -a cxram -i CxRAM-SimpleMul
   * ./RunDemo.py -a cxram -i CxRAM-ImageDiff

# Platforms demonstrators


# Execution dependencies

Build, debug and run binary application on multiple platforms
(powerpc, riscv, kalray) need compilers, debuggers and simulation on
each platforms.

* Build tools:
   * Read the [GenCrossTools documentation](README.GenCrossTools.md)
