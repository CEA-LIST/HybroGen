% Hybrogen Programming guide
% HP Charles
% Oct 2019

[comment]: changequote(`{{', `}}')

# Introduction #

This documentation aims to describe how to use Hybrogen.

Hybrogen is a new code generator generator.


# Compilation chain #

The HybroLang programming language is a DSL (Domain Specific
Language). This language is designed to build applications able to
reconfigure (regenerate) binary kernel at run-time depending on the
user input data set.

![Global View of Hybrogen infrastructure](Imgs/GlobalScheme.pdf "Global View of Hybrogen infrastructure")

The global flow has multiple "compilation time":

* Install time : the architecture description (ISA instruction set
  architecture) is injected in a relationnal database
* Static compilation time is separated in two phases :
 * source to source : from hybrolang to a C file where the HybroLang
   parts are replaced by C macro instructions & C function calls
 * C static compilation : classical compilation file
* Execution time : the application run and some part can be
  regenerated at run-time with depending on the user input

# Input Language #

The input language has the following grammar :

```yacc
include({{../HybroLang/HybroLang.g4}})
```
# Code Generation / Hybrolang usage #

## Flags and parameters ##

The `.hl` codes are transformed by the `Hybrolang` command.

For example a HelloWorld.hl program will be compiled by 

* `Hybrolang HelloWorld.hl` that will generate a HelloWorld.c
* `cc HelloWorld.c -o HelloWorld` will generate a `HelloWorld` binary application.

More specifically `Hybrolang` support the following switches 

* `--arch` to select the list of supported architectures. Examples 
    * `Hybrolang --arch RISCV` will generate an application able to
      generate RISCV binary code
    * `Hybrolang --arch RISCV --arch POWER` will generate an
      application able to generate both RISCV and POWER binary code
* `--arch ARCH,EXTENTION` will generate a code generator for ARCH
  containing EXTENTION instruction set extention
    * `Hybrolang --arch RISCV,RV32I` will generate a code for RISCV
      architecture and RV32I instruction set
    * `Hybrolang --arch RISCV,RV32I,RV32F` will generate a code for
      RISCV architecture and RV32I instruction set and RV32F floating
      point extension.

## Code transformation example ##

In this section we illustrate with a small example a code tranformation.


### Scalar addition ###

This section contains code examples that will generate binary code
function at run time. The source code example is an addition of two
floating point values (`CodeExamples/Add8x16.hl`):

```c
include({{../HybroLang/CodeExamples/Add8x1.hl}})
```

The tranformation of this example will provide the following C code
assuming a transformation via the following HybroLang invocation : 
`Hybrolang --arch RISCV,RV32I,Xf8 CodeExamples/Add8x1.hl`

The resulting code will be in  `Add8x1.c`

```c
include({{CodeTransformationExamples/Add8x1.c}})
```

### Vector addition ###


This section contains code examples that will generate binary code
function at run time. The source code example is an addition of two
floating poing vectors (`CodeExamples/Add8x16.hl`):

```c
include({{../HybroLang/CodeExamples/Add8x16.hl}})
```

The tranformation of this example will provide the following C code
assuming a transformation via the following HybroLang invocation : 
`Hybrolang --arch RISCV,RV32I,Xf8 CodeExamples/Add8x16.hl`

The resulting code will be in  `Add8x16.c`

```c
include({{CodeTransformationExamples/Add8x16.c}})
```



## Data type definition example ##

```c
include({{../HybroLang/CodeExamples/Add8x1.hl}})
```

## Data type definition ##

```c
include({{../HybroLang/CodeExamples/Add8x16.hl}})
```

## Code specialization ##

```c
include({{../HybroLang/CodeExamples/Add-With-Specialization.hl}})
```
## Simple Loop ##

```c
include({{../HybroLang/CodeExamples/Loop.hl}})
```

## Loop unrolling with transprecision ##

```c
include({{../HybroLang/CodeExamples/Loop-With-Transprecision.hl}})
```

## Simple applications ##

### RPN evaluation ###

```c
include({{../HybroLang/CodeExamples/RPN.hl}})
```

## Complex applications ##

### Sparse solve ###

### IA Application ###
