#!/bin/bash

# préparation
mkdir ./resO1

##########################################################
#conv basic
mkdir ./resO1/basic

#compilation
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution32 CxRAM-Convolution32.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution32Br CxRAM-Convolution32Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution16 CxRAM-Convolution16.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution16Br CxRAM-Convolution16Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution8 CxRAM-Convolution8.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution8Br CxRAM-Convolution8Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o Convolution Convolution.c 

#execution
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8Br
/opt/hybrotools/cxram/QiM/qim.py --run Convolution

#copie résulats
cp CxRAM-Convolution32.csv ./resO1/basic/CxRAM-Convolution32SansBc.csv
cp CxRAM-Convolution32Br.csv ./resO1/basic/CxRAM-Convolution32AvecBc.csv
cp CxRAM-Convolution16.csv ./resO1/basic/CxRAM-Convolution16SansBc.csv
cp CxRAM-Convolution16Br.csv ./resO1/basic/CxRAM-Convolution16AvecBc.csv
cp CxRAM-Convolution8.csv ./resO1/basic/CxRAM-Convolution8SansBc.csv
cp CxRAM-Convolution8Br.csv ./resO1/basic/CxRAM-Convolution8AvecBc.csv
cp Convolution.csv ./resO1/basic/Convolution.csv

##########################################################
#conv long
mkdir resO1/long

#tenseur d'entrée
mv TensorConvLong.h TensorConv.h

#compilation
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution32 CxRAM-Convolution32.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution32Br CxRAM-Convolution32Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution16 CxRAM-Convolution16.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution16Br CxRAM-Convolution16Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution8 CxRAM-Convolution8.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution8Br CxRAM-Convolution8Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o Convolution Convolution.c 

#execution
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8Br
/opt/hybrotools/cxram/QiM/qim.py --run Convolution

#copie résulats
cp CxRAM-Convolution32.csv ./resO1/long/CxRAM-Convolution32SansBc.csv
cp CxRAM-Convolution32Br.csv ./resO1/long/CxRAM-Convolution32AvecBc.csv
cp CxRAM-Convolution16.csv ./resO1/long/CxRAM-Convolution16SansBc.csv
cp CxRAM-Convolution16Br.csv ./resO1/long/CxRAM-Convolution16AvecBc.csv
cp CxRAM-Convolution8.csv ./resO1/long/CxRAM-Convolution8SansBc.csv
cp CxRAM-Convolution8Br.csv ./resO1/long/CxRAM-Convolution8AvecBc.csv
cp Convolution.csv ./resO1/long/Convolution.csv

##########################################################
#conv pad
mkdir resO1/pad

#tenseur d'entrée
mv TensorConvPad.h TensorConv.h

#compilation
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution32 CxRAM-Convolution32.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution32Br CxRAM-Convolution32Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution16 CxRAM-Convolution16.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution16Br CxRAM-Convolution16Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution8 CxRAM-Convolution8.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution8Br CxRAM-Convolution8Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o Convolution Convolution.c 

#execution
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8Br
/opt/hybrotools/cxram/QiM/qim.py --run Convolution

#copie résulats
cp CxRAM-Convolution32.csv ./resO1/pad/CxRAM-Convolution32SansBc.csv
cp CxRAM-Convolution32Br.csv ./resO1/pad/CxRAM-Convolution32AvecBc.csv
cp CxRAM-Convolution16.csv ./resO1/pad/CxRAM-Convolution16SansBc.csv
cp CxRAM-Convolution16Br.csv ./resO1/pad/CxRAM-Convolution16AvecBc.csv
cp CxRAM-Convolution8.csv ./resO1/pad/CxRAM-Convolution8SansBc.csv
cp CxRAM-Convolution8Br.csv ./resO1/pad/CxRAM-Convolution8AvecBc.csv
cp Convolution.csv ./resO1/pad/Convolution.csv

##########################################################
#conv stride
mkdir resO1/stride

#tenseur d'entrée
mv TensorConvStride.h TensorConv.h

#compilation
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution32 CxRAM-Convolution32.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution32Br CxRAM-Convolution32Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution16 CxRAM-Convolution16.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution16Br CxRAM-Convolution16Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution8 CxRAM-Convolution8.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o CxRAM-Convolution8Br CxRAM-Convolution8Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O1 -o Convolution Convolution.c 

#execution
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8Br
/opt/hybrotools/cxram/QiM/qim.py --run Convolution

#copie résulats
cp CxRAM-Convolution32.csv ./resO1/stride/CxRAM-Convolution32SansBc.csv
cp CxRAM-Convolution32Br.csv ./resO1/stride/CxRAM-Convolution32AvecBc.csv
cp CxRAM-Convolution16.csv ./resO1/stride/CxRAM-Convolution16SansBc.csv
cp CxRAM-Convolution16Br.csv ./resO1/stride/CxRAM-Convolution16AvecBc.csv
cp CxRAM-Convolution8.csv ./resO1/stride/CxRAM-Convolution8SansBc.csv
cp CxRAM-Convolution8Br.csv ./resO1/stride/CxRAM-Convolution8AvecBc.csv
cp Convolution.csv ./resO1/stride/Convolution.csv
