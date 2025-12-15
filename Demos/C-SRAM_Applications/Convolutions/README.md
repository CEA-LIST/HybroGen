# Kernel Convolution optimisée pour la CSRAM (stage Thaddée BRICOUT)


## Utilisation des fonctions de convolution

### OUTIL NÉCESSAIRE
/!\ Sans les outils suivant vous ne pourrait pas exécuter les convolutions :

* Un cross compilateur riscv32 gcc Linux fonctionnel pour l'architecture C-SRAM
* Une version d'Hybrogen avec un jeu d'instruction contenant les instructions nécessaire a la fonction (MUL ou MAC 8, 16 ou 32 bits en fonction de la convolution)
* Une version de QEMU capable d'émuler le même jeu d'instruction

1. Pré-Compilation Hybrogen du fichier 

```
../../../HybroLang.py --toC --arch cxram --inputfile <fichier.hl>
```

1. CrossCompilation GCC du fichier C généré en RISCV32
```
riscv32-unknown-linux-gcc -Wall -o <fichier> <fichier.c>
```

### Exécution du programme avec QEMU
```
qemu-riscv32 <fichier>
```

### Suppression des fichiers générer 
```
rm -f <fichier> <fichier.c>
```

### Script de compilation et exécution d'un fichier .hl
Le script 'Reslut.sh' compile et exécute sur QEMU un fichier .hl.
Pour cela il faut lancer le script avec le nom du fichier **sans extension** comme paramètre tel que : 
```
./Result.sh <fichier>
```
Ce script permet d'exécuter en une seule fois toutes les étapes décrites au-dessus. 

### Visualisation des instructions exécutées avec le plugin
Si vous souhaitez visualiser les instructions exécutées avec le plugin, il faut charger les variables d'environnement suivantes (modifier la commande "export" en fonction du shell)

```
export QEMU_CXRAM_VERBOSE='yes'
export QEMU_CXRAM_TRACE='yes'
```

## Extraction des résultats de performance des convolutions
/!\ Les scripts présents dans ce répertoire permette d'extraire et de mettre en forme les résultats si vous avez la version du jeu d'instruction de la C-SRAM V1.5 installé et un accès au PC de Kevin (gre 043934) avec un accès a la dernière version de QIM

### Lancement de l'extraction des résultats
Pour extraire les résultats vous devez avoir une session sur le PC GRE043934 (PC de Kevin) avec : 

* Un acces au répertoire de QIM
* Un moyen de connexion sans mot de passe entre votre session locale et distante (type clé ssh)
* Mettre le nom de cette sessions comme parametres du script comme indiqué ci-dessous
```
./AllResult.sh <nomDeSession>
```
Le script ci-dessus compilera l'ensemble des fichiers avec les flags de compilation GCC O1, Os et O3 et fournira les résultats issus de QIM dans le dossier résultat
/!\ Pour que l'extraction fonctionne il faut mettre à 1 la ligne suivante dans les 6 fichiers CxRAM-Convolution*.hl : 
```
#define RESULT_WITH_QIM 1
```
et désactivez tous les affichages :
```
#define AFFICHAGE_CSRAM 0
#define AFFICHAGE_PARAMETRES 0
```

### Mise en forme des résultats
```
python3 miseEnForme.py
```
Ce script met à jour la figure de résultats "figure.jpg" avec les résultats que vous venez d'extraire

## Contenus du répertoire 

### Les 6 fichiers hybrolang de convolution optimisé pour la CSRAM

  La convolution est déclinée en 3 versions en fonction de la taille des opérateurs utilisée (8, 16 ou 32 bits)

  Chaque version est ensuite déclinée en deux en fonction de la façon dont les tenseurs d'entrée sont chargé en mémoire. 
  * Une version simple ou l'ensemble des chargements mémoire est effectué par le processeur
  * une version dans laquelle les copies de données en mémoire utilise l'instruction C-SRAM broadcast

### La convolution scalaire issue de TensorFlow lite

  Ce fichier est la fonction présente dans TensorFlow Lite, elle sert de référence pour la performance des fonctions optimisées. 

### Les données pour les Convolutions

  Nous avons 4 types de données pour tester les fonctions de 
  convolution, ils ont différentes caractéristiques :
  
  * TensorConv.h est un tenseur de petite taille sans paramètres particulier
  * TensorConvLong.h est un tenseur de grande taille sans paramètres particulier
  * TensorConvPad.h est un tenseur qui utilise le parametre de Padding
  * TensorConvStride.h est un tenseur qui utilise le parametre de Stride

### Fichier nécessaire à l'extraction des résulats 

csram_utils.h permet d'extraire les résultats avec qim. 

### Les scripts d'extractions et de mise en formes des résultats 
Le script AllResult.sh appel les scripts présents dans le dossier scriptHybro et place les résultats dans le dossier du même nom sous forme de CSV. 

Ces résultats peuvent être mis sous forme de figure à l'aide du script miseEnForme.py, le fichier figure.jpg contiens la figure en question. 