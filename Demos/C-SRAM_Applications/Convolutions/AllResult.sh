#!/bin/bash

if [ $# != "1" ]
then 
  echo -e "Nombre d'argument invalide"
  echo -e "Veuillez mettre le nom de votre session sur le PC GRE043934 (pc de kevin) en paramètre!"
  exit
fi

echo -e "H2 Compilation"
../../../HybroLang.py --toC --arch cxram --inputfile CxRAM-Convolution8.hl
../../../HybroLang.py --toC --arch cxram --inputfile CxRAM-Convolution8Br.hl
../../../HybroLang.py --toC --arch cxram --inputfile CxRAM-Convolution16.hl
../../../HybroLang.py --toC --arch cxram --inputfile CxRAM-Convolution16Br.hl
../../../HybroLang.py --toC --arch cxram --inputfile CxRAM-Convolution32.hl
../../../HybroLang.py --toC --arch cxram --inputfile CxRAM-Convolution32Br.hl
../../../HybroLang.py --toC --arch cxram --inputfile Convolution.hl

echo -e "\nPréparation et transfert machine distante"
mkdir scpDirectory
cp *.c scpDirectory/
cp *.h scpDirectory/
cp scriptHybro/* scpDirectory/
scp -r scpDirectory $1@gre043934:/home/$1/

echo -e "\nExécution des cript sur la machine distante"
ssh $1@gre043934 "cd /home/$1/scpDirectory/ && ./AllResultO1.sh"
ssh $1@gre043934 "cd /home/$1/scpDirectory/ && ./AllResultOs.sh"
ssh $1@gre043934 "cd /home/$1/scpDirectory/ && ./AllResultO3.sh"

echo -e "\nRécuperation des résulats"
rm -r Resultats
mkdir Resultats
scp -r $1@gre043934:/home/$1/scpDirectory/resO* Resultats/

echo -e "\nSupressions des fichier genéré"
ssh $1@gre043934 rm -r /home/$1/scpDirectory
rm *.c
rm -r scpDirectory