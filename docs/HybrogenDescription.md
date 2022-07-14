% Hybrogen documentations
% HP Charles
% Oct 2019

[comment]: changequote(`{{', `}}')

# Introduction #

This documentation aims to describe Hybrogen internals, it's not a
"User Guide"

This is a new code generator generator based on a vision showned in
the following figure (Initial Ideas).

![Hybrogen Initial Design Ideas](Imgs/InitialIdeas.pdf "Hybrogen Initial Design Ideas")

The main motivations are based on the necessity to

 * target multiple architecture (Instruction Set Processor) at
   run-time
 * adapt a running code to a new data type at run-time
 * adapt a running code to possible multipe processor extensions

# Global view#

Modern applications should push the dynamicity to the limits. At
run-time application should decide :

* to use the best possible accelerator
* choose vectors length
* inject data into binary code
* ...

To acheive this goal we need to generate binary code at run-time. We
don't need a full compiler of JITter, but only a small code generator
dedicated to an optimisation. Those code generators are called
"compilettes".

Write a "compilette" is complicated an need specific tools. Hybrogen
is a tool which help to build "compilettes" which include this
dynamicity inside the final application.

The following figure explain the global view of the Hybrogen
infrastructure.

TODO : describe different blocs / compilation time

![Global View of Hybrogen infrastructure](Imgs/GlobalScheme.pdf "Global View of Hybrogen infrastructure")

# HybroGen genealogy #

 * ccg [see @ccg] was the initial platform for initial
   experimentations and the invention of the "compilette" term.
 * HPBCG [see @HPBCG] https://code.google.com/archive/p/hpbcg/
 * deGoal [see @Degoal]

TODO : describe differences

# HybroGen input languages #

HybroGen contain multiple parts. A first part which describe
Instruction set of computer architectures and a second description
containing the registers role (HybroGen part), a third one which
describe the input programming language (HybroLang).

## Hybrogen for ISAs ##

An isa description is composed by a file describing instruction set
(example `riscv/h2-riscv.isa`) and a second file containing register
description (example : `riscv/h2-riscv.register`)

### Instruction Set Description ###

An Instruction Set Description file contain the description of each
processor instruction. The description is composed of 2 parts :

 * Left part : contains the instruction encoding
 * Right part : contains the instruction classification & syntax
 
The full description grammar is contained in the
`HybroGen/IsaDescription.g4` file. An illustrative example is
contained in the `HyboGen/arch/riscv/h2-riscv.isa` file.

### Register File Description ###

The full description is contained in the
`HybroGen/RegisterDescription.g4` grammar file

A Register Description file contain the description of each
processor register:

The full description grammar is contained in the
`HybroGen/RegisterDescription.g4` file. An illustrative example is
contained in the `HyboGen/arch/riscv/h2-riscv.register` file.

```lex
include({{../HybroGen/IsaDescription.g4}})
```
## Hybrogen for registers ##

Each line represent one or multiple registers the line is encoded with
multiple fields:

* Register bank (can be i as integer register set, f as floating point, v as vector)
* Register number
* Register width (8, 16, 32, ... 512 bits)
* Register role list

The register roles are encoded in the following manner :

* Z : Hard-wired zero
* GP : Global Pointer
* SP : Stack Pointer
* TP : Thread pointer
* RA : Return Address
* T[N] : Temporary (N = allocation order)
* I[N] : function call input register (N = parameter order)
* O[N] : function call output register (N = parameter order)

Note that a register could have multiple roles. 

Here is the input grammar :
```lex
include({{../HybroGen/RegisterDescription.g4}})
```

Here is the input example for RISCV :

```lex
include({{../HybroGen/arch/riscv/h2-riscv.register}})
```

# Hybro Lang input Language #

## Input grammar ##

```lex
include({{../HybroLang/HybroLang.g4}})
```

## Assumptions ##

### Register allocation ##

`HybroLang` variables should fit into internal processor
registers. For example a variable defined as `int 8 16` should fit
into a 128 bits register or in 16 registers of 8 bits.

On a small processor without enough register the compilation could fail.

### Instruction selection ##

`HybroLang` don't do complex code optimization on intermediate
representation, the only complex optimization is about vector
placement in register and usage of SIMD instructions when available.

### Optimization efficiency ##

`HybroLang` optimization rely on the compilette level. Allowing data
and instruction mix at run-time is a very powerfull run-time
optimization, order of magnitude higher than the classical static
compile time approach.


# Software dependencies #

## At install & source to source compilation time ##

 * ANTLR4 https://www.antlr.org/
 * postresql
 * python3 with some packages :
    * python3-antlr
    * psycopg2
 
## At compilation time ##

 * python3
 * postresql
 * python3 with some packages :
    * psycopg2
 
## At run-time ##

 * Nothing ! There is 
    * no external library to include in the binary, 
    * no specific tool
    * no file access

## For documentation ##

 * insckape
 * pandoc

# References



