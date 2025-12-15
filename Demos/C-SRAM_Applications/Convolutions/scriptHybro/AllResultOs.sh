#!/bin/bash

# préparation
mkdir resOs

##########################################################
#conv basic
mkdir resOs/basic

#compilation
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution32 CxRAM-Convolution32.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution32Br CxRAM-Convolution32Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution16 CxRAM-Convolution16.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution16Br CxRAM-Convolution16Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution8 CxRAM-Convolution8.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution8Br CxRAM-Convolution8Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o Convolution Convolution.c 

#execution
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8Br
/opt/hybrotools/cxram/QiM/qim.py --run Convolution

#copie résulats
cp CxRAM-Convolution32.csv ./resOs/basic/CxRAM-Convolution32SansBc.csv
cp CxRAM-Convolution32Br.csv ./resOs/basic/CxRAM-Convolution32AvecBc.csv
cp CxRAM-Convolution16.csv ./resOs/basic/CxRAM-Convolution16SansBc.csv
cp CxRAM-Convolution16Br.csv ./resOs/basic/CxRAM-Convolution16AvecBc.csv
cp CxRAM-Convolution8.csv ./resOs/basic/CxRAM-Convolution8SansBc.csv
cp CxRAM-Convolution8Br.csv ./resOs/basic/CxRAM-Convolution8AvecBc.csv
cp Convolution.csv ./resOs/basic/Convolution.csv

##########################################################
#conv long
mkdir resOs/long

#tenseur d'entrée
mv TensorConvLong.h TensorConv.h

#compilation
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution32 CxRAM-Convolution32.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution32Br CxRAM-Convolution32Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution16 CxRAM-Convolution16.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution16Br CxRAM-Convolution16Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution8 CxRAM-Convolution8.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution8Br CxRAM-Convolution8Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o Convolution Convolution.c 

#execution
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8Br
/opt/hybrotools/cxram/QiM/qim.py --run Convolution

#copie résulats
cp CxRAM-Convolution32.csv ./resOs/long/CxRAM-Convolution32SansBc.csv
cp CxRAM-Convolution32Br.csv ./resOs/long/CxRAM-Convolution32AvecBc.csv
cp CxRAM-Convolution16.csv ./resOs/long/CxRAM-Convolution16SansBc.csv
cp CxRAM-Convolution16Br.csv ./resOs/long/CxRAM-Convolution16AvecBc.csv
cp CxRAM-Convolution8.csv ./resOs/long/CxRAM-Convolution8SansBc.csv
cp CxRAM-Convolution8Br.csv ./resOs/long/CxRAM-Convolution8AvecBc.csv
cp Convolution.csv ./resOs/long/Convolution.csv

##########################################################
#conv pad
mkdir resOs/pad

#tenseur d'entrée
mv TensorConvPad.h TensorConv.h

#compilation
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution32 CxRAM-Convolution32.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution32Br CxRAM-Convolution32Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution16 CxRAM-Convolution16.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution16Br CxRAM-Convolution16Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution8 CxRAM-Convolution8.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution8Br CxRAM-Convolution8Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o Convolution Convolution.c 

#execution
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8Br
/opt/hybrotools/cxram/QiM/qim.py --run Convolution

#copie résulats
cp CxRAM-Convolution32.csv ./resOs/pad/CxRAM-Convolution32SansBc.csv
cp CxRAM-Convolution32Br.csv ./resOs/pad/CxRAM-Convolution32AvecBc.csv
cp CxRAM-Convolution16.csv ./resOs/pad/CxRAM-Convolution16SansBc.csv
cp CxRAM-Convolution16Br.csv ./resOs/pad/CxRAM-Convolution16AvecBc.csv
cp CxRAM-Convolution8.csv ./resOs/pad/CxRAM-Convolution8SansBc.csv
cp CxRAM-Convolution8Br.csv ./resOs/pad/CxRAM-Convolution8AvecBc.csv
cp Convolution.csv ./resOs/pad/Convolution.csv

##########################################################
#conv stride
mkdir resOs/stride

#tenseur d'entrée
mv TensorConvStride.h TensorConv.h

#compilation
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution32 CxRAM-Convolution32.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution32Br CxRAM-Convolution32Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution16 CxRAM-Convolution16.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution16Br CxRAM-Convolution16Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution8 CxRAM-Convolution8.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o CxRAM-Convolution8Br CxRAM-Convolution8Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -Os -o Convolution Convolution.c 

#execution
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8Br
/opt/hybrotools/cxram/QiM/qim.py --run Convolution

#copie résulats
cp CxRAM-Convolution32.csv ./resOs/stride/CxRAM-Convolution32SansBc.csv
cp CxRAM-Convolution32Br.csv ./resOs/stride/CxRAM-Convolution32AvecBc.csv
cp CxRAM-Convolution16.csv ./resOs/stride/CxRAM-Convolution16SansBc.csv
cp CxRAM-Convolution16Br.csv ./resOs/stride/CxRAM-Convolution16AvecBc.csv
cp CxRAM-Convolution8.csv ./resOs/stride/CxRAM-Convolution8SansBc.csv
cp CxRAM-Convolution8Br.csv ./resOs/stride/CxRAM-Convolution8AvecBc.csv
cp Convolution.csv ./resOs/stride/Convolution.csv
