#!/bin/bash

# préparation
mkdir resO3

##########################################################
#conv basic
mkdir resO3/basic

#compilation
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution32 CxRAM-Convolution32.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution32Br CxRAM-Convolution32Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution16 CxRAM-Convolution16.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution16Br CxRAM-Convolution16Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution8 CxRAM-Convolution8.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution8Br CxRAM-Convolution8Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o Convolution Convolution.c 

#execution
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8Br
/opt/hybrotools/cxram/QiM/qim.py --run Convolution

#copie résulats
cp CxRAM-Convolution32.csv ./resO3/basic/CxRAM-Convolution32SansBc.csv
cp CxRAM-Convolution32Br.csv ./resO3/basic/CxRAM-Convolution32AvecBc.csv
cp CxRAM-Convolution16.csv ./resO3/basic/CxRAM-Convolution16SansBc.csv
cp CxRAM-Convolution16Br.csv ./resO3/basic/CxRAM-Convolution16AvecBc.csv
cp CxRAM-Convolution8.csv ./resO3/basic/CxRAM-Convolution8SansBc.csv
cp CxRAM-Convolution8Br.csv ./resO3/basic/CxRAM-Convolution8AvecBc.csv
cp Convolution.csv ./resO3/basic/Convolution.csv

##########################################################
#conv long
mkdir resO3/long

#tenseur d'entrée
mv TensorConvLong.h TensorConv.h

#compilation
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution32 CxRAM-Convolution32.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution32Br CxRAM-Convolution32Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution16 CxRAM-Convolution16.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution16Br CxRAM-Convolution16Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution8 CxRAM-Convolution8.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution8Br CxRAM-Convolution8Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o Convolution Convolution.c 

#execution
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8Br
/opt/hybrotools/cxram/QiM/qim.py --run Convolution

#copie résulats
cp CxRAM-Convolution32.csv ./resO3/long/CxRAM-Convolution32SansBc.csv
cp CxRAM-Convolution32Br.csv ./resO3/long/CxRAM-Convolution32AvecBc.csv
cp CxRAM-Convolution16.csv ./resO3/long/CxRAM-Convolution16SansBc.csv
cp CxRAM-Convolution16Br.csv ./resO3/long/CxRAM-Convolution16AvecBc.csv
cp CxRAM-Convolution8.csv ./resO3/long/CxRAM-Convolution8SansBc.csv
cp CxRAM-Convolution8Br.csv ./resO3/long/CxRAM-Convolution8AvecBc.csv
cp Convolution.csv ./resO3/long/Convolution.csv

##########################################################
#conv pad
mkdir resO3/pad

#tenseur d'entrée
mv TensorConvPad.h TensorConv.h

#compilation
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution32 CxRAM-Convolution32.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution32Br CxRAM-Convolution32Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution16 CxRAM-Convolution16.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution16Br CxRAM-Convolution16Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution8 CxRAM-Convolution8.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution8Br CxRAM-Convolution8Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o Convolution Convolution.c 

#execution
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8Br
/opt/hybrotools/cxram/QiM/qim.py --run Convolution

#copie résulats
cp CxRAM-Convolution32.csv ./resO3/pad/CxRAM-Convolution32SansBc.csv
cp CxRAM-Convolution32Br.csv ./resO3/pad/CxRAM-Convolution32AvecBc.csv
cp CxRAM-Convolution16.csv ./resO3/pad/CxRAM-Convolution16SansBc.csv
cp CxRAM-Convolution16Br.csv ./resO3/pad/CxRAM-Convolution16AvecBc.csv
cp CxRAM-Convolution8.csv ./resO3/pad/CxRAM-Convolution8SansBc.csv
cp CxRAM-Convolution8Br.csv ./resO3/pad/CxRAM-Convolution8AvecBc.csv
cp Convolution.csv ./resO3/pad/Convolution.csv

##########################################################
#conv stride
mkdir resO3/stride

#tenseur d'entrée
mv TensorConvStride.h TensorConv.h

#compilation
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution32 CxRAM-Convolution32.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution32Br CxRAM-Convolution32Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution16 CxRAM-Convolution16.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution16Br CxRAM-Convolution16Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution8 CxRAM-Convolution8.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o CxRAM-Convolution8Br CxRAM-Convolution8Br.c 
/opt/hybrotools/cxram/bin/riscv32-unknown-linux-gnu-gcc -Wall -O3 -o Convolution Convolution.c 

#execution
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution32Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution16Br
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8
/opt/hybrotools/cxram/QiM/qim.py --run CxRAM-Convolution8Br
/opt/hybrotools/cxram/QiM/qim.py --run Convolution

#copie résulats
cp CxRAM-Convolution32.csv ./resO3/stride/CxRAM-Convolution32SansBc.csv
cp CxRAM-Convolution32Br.csv ./resO3/stride/CxRAM-Convolution32AvecBc.csv
cp CxRAM-Convolution16.csv ./resO3/stride/CxRAM-Convolution16SansBc.csv
cp CxRAM-Convolution16Br.csv ./resO3/stride/CxRAM-Convolution16AvecBc.csv
cp CxRAM-Convolution8.csv ./resO3/stride/CxRAM-Convolution8SansBc.csv
cp CxRAM-Convolution8Br.csv ./resO3/stride/CxRAM-Convolution8AvecBc.csv
cp Convolution.csv ./resO3/stride/Convolution.csv
