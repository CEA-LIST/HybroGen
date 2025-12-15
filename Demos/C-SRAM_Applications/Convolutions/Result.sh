#!/bin/bash

if [ $# != "1" ]; then 
  echo -e "Nombre d'argument invalide\n"
  echo -e "Veuillez mettre le nom du fichier que vous souhaiez compiler et exécuter, sans extention, en paramètre!"
  exit
fi

echo -e "Netoyage des ancien fichiers"
rm -f $1 $1.c

echo -e "\nH2 Compilation"
../../../HybroLang.py --toC --arch cxram --inputfile $1.hl

echo -e "\nC Compilation"
riscv32-unknown-linux-gcc -Wall -o $1 $1.c

echo -e "\nExécution sur QEMU"
qemu-riscv32 $1