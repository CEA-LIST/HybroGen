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

* Grammar use ANTLR4 to being generate 
  * `sudo apt install antlr4`

* Grammar use ANTLR4 with python4 backend
   * `pip3 install antlr4-python3-runtime==<versionOfAntlr4>`

* Compilation need a sqlite database. To install sqlite and his dev lib you can use this commands :
   * `sudo apt install -y sqlite3 libsqlite3-dev`

* Debuging need graphviz https://graphviz.readthedocs.io/en/stable/
	* `sudo apt install python3-pygraphviz`

* Qemu build need ninja
  * `sudo apt install ninja-build`

# Hybrogen installation

## Create cross-compilers, debugger and emulator for supported platforms

* Clone HybroGen in a directory to extract the source files (with git or fetch / tar)
* `git clone git@github.com:CEA-LIST/HybroGen.git`
* or
  * `wget https://github.com/CEA-LIST/HybroGen/archive/refs/tags/v5.1.tar.gz`
  * `tar xf v5.1.tar.gz`
* Choose a target directory to install the release e.g. `/opt/H5.1/`
* For each platforms riscv, aarch64, powerpc, cxram-linux

  Run `./GenCrossTools.py -a <platform> -p /opt/H5.1/ -w /opt/H5.1/tmp`

  This command will generate the cross-compiler environment (gcc, gdb,
  qemu, linux-headers). This command could take some time to run.


  * Run `./GenCrossTools.py -a <platform> -p /opt/H5.1/ -w /opt/H5.1/tmp -s`
    * This will generate the shell environment (csh like or bash like)
    * A full installation could be :
```
./GenCrossTools.py -a aarch64 -p /opt/H5.0/ -w /opt/H5.0/tmp
./GenCrossTools.py -a aarch64 -p /opt/H5.0/ -w /opt/H5.0/tmp -s

./GenCrossTools.py -a riscv   -p /opt/H5.0/ -w /opt/H5.0/tmp
./GenCrossTools.py -a riscv   -p /opt/H5.0/ -w /opt/H5.0/tmp -s

./GenCrossTools.py -a power   -p /opt/H5.0/ -w /opt/H5.0/tmp
./GenCrossTools.py -a power   -p /opt/H5.0/ -w /opt/H5.0/tmp -s

./GenCrossTools.py -a cxram-linux   -p /opt/H5.0/ -w /opt/H5.0/tmp
./GenCrossTools.py -a cxram-linux   -p /opt/H5.0/ -w /opt/H5.0/tmp -s

```

This step could take time. Count between 5mn and 20mn for each
architecture depending on your computing power and bandwith.

## Build HybroGen

HybroGen is mainly written in with python but need some build

* Run `make buildGrammar` to build the ANTLR lexer / parser / visitorBase
* Run `make DbPopulate` to populate the SQL database with instructions description
* Congratulation, HybroGen is ready to work !


## Check if installation has work well

Hybrogen has a global check to see if everything is working fine.

* Go to Hybrogen directory and Run `make check`
* If everything work it's good.
  * If not Retry the installation
  * If it's still not work contact us : henri-pierre.charles@cea.fr

## For Computing in memory platform aka CXRAM

For this platform we need a qemu plugin which emulate the C-SRAM
accelerator and give statistics about executed instructions.

Follow instructions on this repository : https://github.com/CEA-LIST/csram-qemu-plugin

## Run Demo

* All of the  Experimentation/Demonstration of application case are in the Demos Directory.

So for a simplier use you can just go to the Demos directory `cd Demos` 
Next you can just Run the command `make buildAll`

Next i will describe how to run all working Demo

Note : the cxram-linux architecture is not supported by any Demos.

### Newton-SquareRoot-VariablePrecision

#### How to launch Demo

So to access you just need to go into the Newton-SquareRoot-VariablePrecision Directory using `cd Newton-SquareRoot-VariablePrecision`.
You can just play the demo on each arch by using the command : `demo-<archName>`


#### How to interpret result


### VectorMatrix

So to access you just need to go into the VectorMatrix Directory using `cd VectorMatrix`.

Once you are in the `VectorMatrix` demo directory, you can run the experiment on QEMU for the desired architecture.

For AArch64, run:

```bash
make runaarch64Qemu
```

For PowerPC, run:

```bash
make runpowerQemu
```

The experiment is run with both `-O0` and `-O3`. Two log files will be generated, following this naming format:

```text
{architecture}-qemu-{date}-O0.log
{architecture}-qemu-{date}-O3.log
```

These log files contain the experimental results for each repetition count of the `VectorMatrix` operations.

You can then generate a plot from the two log files using:

```bash
python3 PlotResults.py file1.log file2.log size
```

Replace `file1.log` and `file2.log` with the generated `O0` and `O3` log files.

The `size` argument corresponds to the number of repetitions to plot. The available values are:

```text
10
100
1000
10000
100000
1000000
```

For example:

```bash
python3 PlotResults.py aarch64-qemu-2026-09-21-O0.log aarch64-qemu-2026-09-21-O3.log 100000
```


### Stencil

Now that you are in the Stencil Demo Matrix, you can run the experiments for each architecture using the following commands:

- `make allAarch64Qemu` runs the AArch64 experiments using QEMU.
- `make allRiscvQemu` runs the RISC-V experiments using QEMU.
- `make allPowerQemu` runs the PowerPC experiments using QEMU.
- `make allAarch64Native` runs the AArch64 experiments natively.
- `make allRiscvNative` runs the RISC-V experiments natively.

For each architecture, the experiments are run with both `-O0` and `-O3` compiler optimization levels.

The experiment uses several image sizes, from `13x10` up to `1280x960`, and tests five different filters for both `3x3` and `5x5` kernels:

- Null
- Identity
- Blur
- Gaussian Filter
- Synthetic

The results are stored in log files named according to the architecture, execution mode, optimization level, and timestamp.

Once the experiments are completed, you can generate the plots with:

`make plot ARCH=aarch64`

or:

`make plot ARCH=riscv`

The generated plots will be stored using the architecture name as the output identifier.

To generate the plots from the native experiment results, run:

`cd ./Results/ && make all DATAFILES="../${ARCH}-native-O0.log ../${ARCH}-native-O3.log"`

Replace `${ARCH}` with the architecture you want to process, for example `aarch64` or `riscv`.



## What vector Operation and on which vector and wordLen size is supported by HybroGen

So HybroGen has a good strategy to show the user what it supported and what is currently working inside of the compiler. With that our user can know what is currently working and which version of our software to take. This take place in the CodeExample Directory so go into it using `cd CodeExample`.


# Execution dependencies

GenCrossTools used to generate compiler / debugger and qemu has it's
own documentation :

* Read the [GenCrossTools documentation](README.GenCrossTools.md)
