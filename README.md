% Hybrogen Hybrid Code Generation, fast and small as the hydrogen element
% HP Charles

# Introduction

* After [ccg](https://pages.lip6.fr/vvm/projects_realizations/ccg/),
  [hpbcg](https://code.google.com/archive/p/hpbcg/), deGoal, the new
  HybroGen tool to generate efficent binary code

* General idea : Hybrogen is a tool which helps to generate
  compilette, compilettes are small code generators able to regenerate
  a part of an application at run-time. It aims to be fast (~10 cycles
  to generate 1 instruction), small (KB code generator)

* How it works : it start from a instruction set database containing
  instruction encoding, arithmetic, data width and vector len, we
  create a programming language (HybroLang) which allow to express
  data set variation & build a compiler which take advantage of (1)
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

* Compilation need a postresql database. To install postgresql and configure it you can use this commands :
   * `sudo apt install postgresql`

* Install a python postgresql connector:
   * `sudo apt install python3-psycopg2`

* Initialize the database
   * `sudo -i -u postgres`
   * `createdb hybrogen`
   * `createuser --pwprompt hybrogen` # the default password in the code is "hybrogen"

  It is a good practice to not create the database under your own
  username. (The database could be multiuser accessible)


* Qemu build need ninja
  * `sudo apt install ninja-build`


# Hybrogen installation

## Create cross-compilers, debugger and emulator for supported platforms

* Clone HybroGen in a directory to extract the source files (with git or fetch / tar)
* `git clone git@github.com:CEA-LIST/HybroGen.git`
* or
  * `wget https://github.com/CEA-LIST/HybroGen/archive/refs/tags/v4.0.tar.gz`
  * `tar xf v4.0.tar.gz`
* Choose a target directory to install the release e.g. `/opt/H4.0/`
* For each platforms riscv, aarch64, powerpc, cxram-linux

  Run `./GenCrossTools.py -a <platform> -p /opt/H4.0/ -w /opt/H4.0/tmp`

  This command will generate the cross-compiler environment (gcc, gdb,
  qemu, linux-headers). This command could take some time to run.


  * Run `./GenCrossTools.py -a riscv -p /opt/H4.0/ -w /opt/H4.0/tmp -s`
    * This will generate the shell environment (csh like or bash like)
    * A full installation could be :
```
./GenCrossTools.py -a aarch64 -p /opt/H4.0/ -w /opt/H4.0/tmp
./GenCrossTools.py -a aarch64 -p /opt/H4.0/ -w /opt/H4.0/tmp -s

./GenCrossTools.py -a riscv   -p /opt/H4.0/ -w /opt/H4.0/tmp
./GenCrossTools.py -a riscv   -p /opt/H4.0/ -w /opt/H4.0/tmp -s

./GenCrossTools.py -a powerpc   -p /opt/H4.0/ -w /opt/H4.0/tmp
./GenCrossTools.py -a powerpc   -p /opt/H4.0/ -w /opt/H4.0/tmp -s

./GenCrossTools.py -a cxram-linux   -p /opt/H4.0/ -w /opt/H4.0/tmp
./GenCrossTools.py -a cxram-linux   -p /opt/H4.0/ -w /opt/H4.0/tmp -s

```

This step could take time. Count between 5mn and 20mn for each
architecture depending on your computing power and bandwith.

## Build HybroGen

HybroGen is mainly written in with python but need some build

* Run `make buildGrammar` to build the ANTLR lexer / parser
* Run `make DbPopulate` to populate the SQL database with instructions description
* Congratulation, HybroGen is ready to work !

## For Computing in memory platform aka CXRAM

For this platform we need a qemu plugin which emulate the C-SRAM
accelerator and give statistics about executed instructions.

Follow instructions on this repository : https://github.com/CEA-LIST/csram-qemu-plugin

## Run some examples / démonstration

* Some code examples are located in the this sub directory : CodeExamples

For example to run an demonstration for the power architecture here is
the command. Adapt for other architectures / demonstrations.

** `cd CodeExamples/`
** `source /opt/H4.0/powerpc/.cshrc`
** `./RunDemo.py -a power -i Array-Mult-Specialization`

* Regression can be run in the same directory : `./Regression.py power`


# Execution dependencies

GenCrossTools used to generate compiler / debugger and qemu has it's
own documentation :

* Read the [GenCrossTools documentation](README.GenCrossTools.md)
