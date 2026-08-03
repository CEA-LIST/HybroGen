#!/usr/bin/env python3
# Script pour maia :
# En utilisant matplotlib, donne moi un script python permettant d’afficher les résultats suivants : dataSet = {
#    "O0/O0": {"LLVM":  7610,  "HybroGen":92}
#    "O0/O2": {"LLVM": 44414,  "HybroGen":92}
#    "O3/O0": {"LLVM":  7609,  "HybroGen":46}
#    "O3/O2": {"LLVM": 44867,  "HybroGen":46}
#    }
# Comment utiliser une échelle log ?

def error(msg):
    print (msg)
    sys.exit(-1)

dataSet = {
    "O0/O0": {"LLVM":  7610,  "HybroGen":92},
    "O2/O0": {"LLVM": 44414,  "HybroGen":92},
    "O0/O3": {"LLVM":  7609,  "HybroGen":46},
    "O2/O3": {"LLVM": 44867,  "HybroGen":46},
    }

if __name__ == "__main__":
    import os, re, sys, csv, pprint
    import matplotlib.pyplot as plt
    import numpy as np

    # Préparation des données pour le graphique
    labels = list(dataSet.keys())
    llvm_values = [dataSet[label]["LLVM"] for label in labels]
    hybrogen_values = [dataSet[label]["HybroGen"] for label in labels]

    x = np.arange(len(labels))  # Position des barres sur l'axe x
    width = 0.35  # Largeur des barres

    fig, ax = plt.subplots(figsize=(10, 6))

    # Création des barres
    rects1 = ax.bar(x - width/2, llvm_values, width, label='LLVM')
    rects2 = ax.bar(x + width/2, hybrogen_values, width, label='HybroGen')

    # Configuration des axes et des titres
    ax.set_xlabel('Compilation options : Static Compilation / Dynamic Compilation')
    ax.set_ylabel('Code Generation time (clock ticks) \n log scale')
#    ax.set_title('Comparaison des performances entre LLVM et HybroGen')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.set_yscale('log')
    # Affichage des valeurs sur les barres
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    autolabel(rects1)
    autolabel(rects2)
    # Affichage du graphique
    fig.tight_layout()
    figureName = 'Figure-Code-Gen-Speed.png'
    plt.savefig(figureName)
    print ("Figure saved in %s"%figureName)
    # plt.show()
