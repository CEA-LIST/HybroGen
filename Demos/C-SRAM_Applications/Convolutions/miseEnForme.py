# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%% chargement O1
basicO1 = pd.read_csv('Resultats/resO1/basic/Convolution.csv', names = ['scalaire'], index_col = 0, sep = ";")
basicO1 = pd.concat([basicO1,pd.read_csv('Resultats/resO1/basic/CxRAM-Convolution32SansBc.csv', names = ['32'], index_col = 0, sep = ";")], axis=1)
basicO1 = pd.concat([basicO1,pd.read_csv('Resultats/resO1/basic/CxRAM-Convolution32AvecBc.csv', names = ['32Br'], index_col = 0, sep = ";")], axis=1)
basicO1 = pd.concat([basicO1,pd.read_csv('Resultats/resO1/basic/CxRAM-Convolution16SansBc.csv', names = ['16'], index_col = 0, sep = ";")], axis=1)
basicO1 = pd.concat([basicO1,pd.read_csv('Resultats/resO1/basic/CxRAM-Convolution16AvecBc.csv', names = ['16Br'], index_col = 0, sep = ";")], axis=1)
basicO1 = pd.concat([basicO1,pd.read_csv('Resultats/resO1/basic/CxRAM-Convolution8SansBc.csv', names = ['8'], index_col = 0, sep = ";")], axis=1)
basicO1 = pd.concat([basicO1,pd.read_csv('Resultats/resO1/basic/CxRAM-Convolution8AvecBc.csv', names = ['8Br'], index_col = 0, sep = ";")], axis=1)

longO1 = pd.read_csv('Resultats/resO1/long/Convolution.csv', names = ['scalaire'], index_col = 0, sep = ";")
longO1 = pd.concat([longO1,pd.read_csv('Resultats/resO1/long/CxRAM-Convolution32SansBc.csv', names = ['32'], index_col = 0, sep = ";")], axis=1)
longO1 = pd.concat([longO1,pd.read_csv('Resultats/resO1/long/CxRAM-Convolution32AvecBc.csv', names = ['32Br'], index_col = 0, sep = ";")], axis=1)
longO1 = pd.concat([longO1,pd.read_csv('Resultats/resO1/long/CxRAM-Convolution16SansBc.csv', names = ['16'], index_col = 0, sep = ";")], axis=1)
longO1 = pd.concat([longO1,pd.read_csv('Resultats/resO1/long/CxRAM-Convolution16AvecBc.csv', names = ['16Br'], index_col = 0, sep = ";")], axis=1)
longO1 = pd.concat([longO1,pd.read_csv('Resultats/resO1/long/CxRAM-Convolution8SansBc.csv', names = ['8'], index_col = 0, sep = ";")], axis=1)
longO1 = pd.concat([longO1,pd.read_csv('Resultats/resO1/long/CxRAM-Convolution8AvecBc.csv', names = ['8Br'], index_col = 0, sep = ";")], axis=1)

padO1 = pd.read_csv('Resultats/resO1/pad/Convolution.csv', names = ['scalaire'], index_col = 0, sep = ";")
padO1 = pd.concat([padO1,pd.read_csv('Resultats/resO1/pad/CxRAM-Convolution32SansBc.csv', names = ['32'], index_col = 0, sep = ";")], axis=1)
padO1 = pd.concat([padO1,pd.read_csv('Resultats/resO1/pad/CxRAM-Convolution32AvecBc.csv', names = ['32Br'], index_col = 0, sep = ";")], axis=1)
padO1 = pd.concat([padO1,pd.read_csv('Resultats/resO1/pad/CxRAM-Convolution16SansBc.csv', names = ['16'], index_col = 0, sep = ";")], axis=1)
padO1 = pd.concat([padO1,pd.read_csv('Resultats/resO1/pad/CxRAM-Convolution16AvecBc.csv', names = ['16Br'], index_col = 0, sep = ";")], axis=1)
padO1 = pd.concat([padO1,pd.read_csv('Resultats/resO1/pad/CxRAM-Convolution8SansBc.csv', names = ['8'], index_col = 0, sep = ";")], axis=1)
padO1 = pd.concat([padO1,pd.read_csv('Resultats/resO1/pad/CxRAM-Convolution8AvecBc.csv', names = ['8Br'], index_col = 0, sep = ";")], axis=1)

strideO1 = pd.read_csv('Resultats/resO1/stride/Convolution.csv', names = ['scalaire'], index_col = 0, sep = ";")
strideO1 = pd.concat([strideO1,pd.read_csv('Resultats/resO1/stride/CxRAM-Convolution32SansBc.csv', names = ['32'], index_col = 0, sep = ";")], axis=1)
strideO1 = pd.concat([strideO1,pd.read_csv('Resultats/resO1/stride/CxRAM-Convolution32AvecBc.csv', names = ['32Br'], index_col = 0, sep = ";")], axis=1)
strideO1 = pd.concat([strideO1,pd.read_csv('Resultats/resO1/stride/CxRAM-Convolution16SansBc.csv', names = ['16'], index_col = 0, sep = ";")], axis=1)
strideO1 = pd.concat([strideO1,pd.read_csv('Resultats/resO1/stride/CxRAM-Convolution16AvecBc.csv', names = ['16Br'], index_col = 0, sep = ";")], axis=1)
strideO1 = pd.concat([strideO1,pd.read_csv('Resultats/resO1/stride/CxRAM-Convolution8SansBc.csv', names = ['8'], index_col = 0, sep = ";")], axis=1)
strideO1 = pd.concat([strideO1,pd.read_csv('Resultats/resO1/stride/CxRAM-Convolution8AvecBc.csv', names = ['8Br'], index_col = 0, sep = ";")], axis=1)

O1 = {'basic' : basicO1, 'long' : longO1, 'pad' : padO1, 'stride' : strideO1}

#%% chargement Os
basicOs = pd.read_csv('Resultats/resOs/basic/Convolution.csv', names = ['scalaire'], index_col = 0, sep = ";")
basicOs = pd.concat([basicOs,pd.read_csv('Resultats/resOs/basic/CxRAM-Convolution32SansBc.csv', names = ['32'], index_col = 0, sep = ";")], axis=1)
basicOs = pd.concat([basicOs,pd.read_csv('Resultats/resOs/basic/CxRAM-Convolution32AvecBc.csv', names = ['32Br'], index_col = 0, sep = ";")], axis=1)
basicOs = pd.concat([basicOs,pd.read_csv('Resultats/resOs/basic/CxRAM-Convolution16SansBc.csv', names = ['16'], index_col = 0, sep = ";")], axis=1)
basicOs = pd.concat([basicOs,pd.read_csv('Resultats/resOs/basic/CxRAM-Convolution16AvecBc.csv', names = ['16Br'], index_col = 0, sep = ";")], axis=1)
basicOs = pd.concat([basicOs,pd.read_csv('Resultats/resOs/basic/CxRAM-Convolution8SansBc.csv', names = ['8'], index_col = 0, sep = ";")], axis=1)
basicOs = pd.concat([basicOs,pd.read_csv('Resultats/resOs/basic/CxRAM-Convolution8AvecBc.csv', names = ['8Br'], index_col = 0, sep = ";")], axis=1)

longOs = pd.read_csv('Resultats/resOs/long/Convolution.csv', names = ['scalaire'], index_col = 0, sep = ";")
longOs = pd.concat([longOs,pd.read_csv('Resultats/resOs/long/CxRAM-Convolution32SansBc.csv', names = ['32'], index_col = 0, sep = ";")], axis=1)
longOs = pd.concat([longOs,pd.read_csv('Resultats/resOs/long/CxRAM-Convolution32AvecBc.csv', names = ['32Br'], index_col = 0, sep = ";")], axis=1)
longOs = pd.concat([longOs,pd.read_csv('Resultats/resOs/long/CxRAM-Convolution16SansBc.csv', names = ['16'], index_col = 0, sep = ";")], axis=1)
longOs = pd.concat([longOs,pd.read_csv('Resultats/resOs/long/CxRAM-Convolution16AvecBc.csv', names = ['16Br'], index_col = 0, sep = ";")], axis=1)
longOs = pd.concat([longOs,pd.read_csv('Resultats/resOs/long/CxRAM-Convolution8SansBc.csv', names = ['8'], index_col = 0, sep = ";")], axis=1)
longOs = pd.concat([longOs,pd.read_csv('Resultats/resOs/long/CxRAM-Convolution8AvecBc.csv', names = ['8Br'], index_col = 0, sep = ";")], axis=1)

padOs = pd.read_csv('Resultats/resOs/pad/Convolution.csv', names = ['scalaire'], index_col = 0, sep = ";")
padOs = pd.concat([padOs,pd.read_csv('Resultats/resOs/pad/CxRAM-Convolution32SansBc.csv', names = ['32'], index_col = 0, sep = ";")], axis=1)
padOs = pd.concat([padOs,pd.read_csv('Resultats/resOs/pad/CxRAM-Convolution32AvecBc.csv', names = ['32Br'], index_col = 0, sep = ";")], axis=1)
padOs = pd.concat([padOs,pd.read_csv('Resultats/resOs/pad/CxRAM-Convolution16SansBc.csv', names = ['16'], index_col = 0, sep = ";")], axis=1)
padOs = pd.concat([padOs,pd.read_csv('Resultats/resOs/pad/CxRAM-Convolution16AvecBc.csv', names = ['16Br'], index_col = 0, sep = ";")], axis=1)
padOs = pd.concat([padOs,pd.read_csv('Resultats/resOs/pad/CxRAM-Convolution8SansBc.csv', names = ['8'], index_col = 0, sep = ";")], axis=1)
padOs = pd.concat([padOs,pd.read_csv('Resultats/resOs/pad/CxRAM-Convolution8AvecBc.csv', names = ['8Br'], index_col = 0, sep = ";")], axis=1)

strideOs = pd.read_csv('Resultats/resOs/stride/Convolution.csv', names = ['scalaire'], index_col = 0, sep = ";")
strideOs = pd.concat([strideOs,pd.read_csv('Resultats/resOs/stride/CxRAM-Convolution32SansBc.csv', names = ['32'], index_col = 0, sep = ";")], axis=1)
strideOs = pd.concat([strideOs,pd.read_csv('Resultats/resOs/stride/CxRAM-Convolution32AvecBc.csv', names = ['32Br'], index_col = 0, sep = ";")], axis=1)
strideOs = pd.concat([strideOs,pd.read_csv('Resultats/resOs/stride/CxRAM-Convolution16SansBc.csv', names = ['16'], index_col = 0, sep = ";")], axis=1)
strideOs = pd.concat([strideOs,pd.read_csv('Resultats/resOs/stride/CxRAM-Convolution16AvecBc.csv', names = ['16Br'], index_col = 0, sep = ";")], axis=1)
strideOs = pd.concat([strideOs,pd.read_csv('Resultats/resOs/stride/CxRAM-Convolution8SansBc.csv', names = ['8'], index_col = 0, sep = ";")], axis=1)
strideOs = pd.concat([strideOs,pd.read_csv('Resultats/resOs/stride/CxRAM-Convolution8AvecBc.csv', names = ['8Br'], index_col = 0, sep = ";")], axis=1)

Os = {'basic' : basicOs, 'long' : longOs, 'pad' : padOs, 'stride' : strideOs}

#%% chargement Os
basicO3 = pd.read_csv('Resultats/resO3/basic/Convolution.csv', names = ['scalaire'], index_col = 0, sep = ";")
basicO3 = pd.concat([basicO3,pd.read_csv('Resultats/resO3/basic/CxRAM-Convolution32SansBc.csv', names = ['32'], index_col = 0, sep = ";")], axis=1)
basicO3 = pd.concat([basicO3,pd.read_csv('Resultats/resO3/basic/CxRAM-Convolution32AvecBc.csv', names = ['32Br'], index_col = 0, sep = ";")], axis=1)
basicO3 = pd.concat([basicO3,pd.read_csv('Resultats/resO3/basic/CxRAM-Convolution16SansBc.csv', names = ['16'], index_col = 0, sep = ";")], axis=1)
basicO3 = pd.concat([basicO3,pd.read_csv('Resultats/resO3/basic/CxRAM-Convolution16AvecBc.csv', names = ['16Br'], index_col = 0, sep = ";")], axis=1)
basicO3 = pd.concat([basicO3,pd.read_csv('Resultats/resO3/basic/CxRAM-Convolution8SansBc.csv', names = ['8'], index_col = 0, sep = ";")], axis=1)
basicO3 = pd.concat([basicO3,pd.read_csv('Resultats/resO3/basic/CxRAM-Convolution8AvecBc.csv', names = ['8Br'], index_col = 0, sep = ";")], axis=1)

longO3 = pd.read_csv('Resultats/resO3/long/Convolution.csv', names = ['scalaire'], index_col = 0, sep = ";")
longO3 = pd.concat([longO3,pd.read_csv('Resultats/resO3/long/CxRAM-Convolution32SansBc.csv', names = ['32'], index_col = 0, sep = ";")], axis=1)
longO3 = pd.concat([longO3,pd.read_csv('Resultats/resO3/long/CxRAM-Convolution32AvecBc.csv', names = ['32Br'], index_col = 0, sep = ";")], axis=1)
longO3 = pd.concat([longO3,pd.read_csv('Resultats/resO3/long/CxRAM-Convolution16SansBc.csv', names = ['16'], index_col = 0, sep = ";")], axis=1)
longO3 = pd.concat([longO3,pd.read_csv('Resultats/resO3/long/CxRAM-Convolution16AvecBc.csv', names = ['16Br'], index_col = 0, sep = ";")], axis=1)
longO3 = pd.concat([longO3,pd.read_csv('Resultats/resO3/long/CxRAM-Convolution8SansBc.csv', names = ['8'], index_col = 0, sep = ";")], axis=1)
longO3 = pd.concat([longO3,pd.read_csv('Resultats/resO3/long/CxRAM-Convolution8AvecBc.csv', names = ['8Br'], index_col = 0, sep = ";")], axis=1)

padO3 = pd.read_csv('Resultats/resO3/pad/Convolution.csv', names = ['scalaire'], index_col = 0, sep = ";")
padO3 = pd.concat([padO3,pd.read_csv('Resultats/resO3/pad/CxRAM-Convolution32SansBc.csv', names = ['32'], index_col = 0, sep = ";")], axis=1)
padO3 = pd.concat([padO3,pd.read_csv('Resultats/resO3/pad/CxRAM-Convolution32AvecBc.csv', names = ['32Br'], index_col = 0, sep = ";")], axis=1)
padO3 = pd.concat([padO3,pd.read_csv('Resultats/resO3/pad/CxRAM-Convolution16SansBc.csv', names = ['16'], index_col = 0, sep = ";")], axis=1)
padO3 = pd.concat([padO3,pd.read_csv('Resultats/resO3/pad/CxRAM-Convolution16AvecBc.csv', names = ['16Br'], index_col = 0, sep = ";")], axis=1)
padO3 = pd.concat([padO3,pd.read_csv('Resultats/resO3/pad/CxRAM-Convolution8SansBc.csv', names = ['8'], index_col = 0, sep = ";")], axis=1)
padO3 = pd.concat([padO3,pd.read_csv('Resultats/resO3/pad/CxRAM-Convolution8AvecBc.csv', names = ['8Br'], index_col = 0, sep = ";")], axis=1)

strideO3 = pd.read_csv('Resultats/resO3/stride/Convolution.csv', names = ['scalaire'], index_col = 0, sep = ";")
strideO3 = pd.concat([strideO3,pd.read_csv('Resultats/resO3/stride/CxRAM-Convolution32SansBc.csv', names = ['32'], index_col = 0, sep = ";")], axis=1)
strideO3 = pd.concat([strideO3,pd.read_csv('Resultats/resO3/stride/CxRAM-Convolution32AvecBc.csv', names = ['32Br'], index_col = 0, sep = ";")], axis=1)
strideO3 = pd.concat([strideO3,pd.read_csv('Resultats/resO3/stride/CxRAM-Convolution16SansBc.csv', names = ['16'], index_col = 0, sep = ";")], axis=1)
strideO3 = pd.concat([strideO3,pd.read_csv('Resultats/resO3/stride/CxRAM-Convolution16AvecBc.csv', names = ['16Br'], index_col = 0, sep = ";")], axis=1)
strideO3 = pd.concat([strideO3,pd.read_csv('Resultats/resO3/stride/CxRAM-Convolution8SansBc.csv', names = ['8'], index_col = 0, sep = ";")], axis=1)
strideO3 = pd.concat([strideO3,pd.read_csv('Resultats/resO3/stride/CxRAM-Convolution8AvecBc.csv', names = ['8Br'], index_col = 0, sep = ";")], axis=1)

O3 = {'basic' : basicO3, 'long' : longO3, 'pad' : padO3, 'stride' : strideO3}

#%%calcul des delta de données (division par rapport a la référance)

deltaO1 = {}
for i in O1:
    deltaO1[i] = O1[i].iloc[47:51]
    
for i in deltaO1:
    deltaO1[i] = deltaO1[i].astype('float64')
    for j in reversed(deltaO1[i].columns):
        deltaO1[i][j] = deltaO1[i]['scalaire'] / deltaO1[i][j]
        
deltaOs = {}
for i in Os:
    deltaOs[i] = Os[i].iloc[47:51]
    
for i in deltaOs:
    deltaOs[i] = deltaOs[i].astype('float64')
    for j in reversed(deltaOs[i].columns):
        deltaOs[i][j] = deltaOs[i]['scalaire'] / deltaOs[i][j]

deltaO3 = {}
for i in O3:
    deltaO3[i] = O3[i].iloc[47:51]
    
for i in deltaO3:
    deltaO3[i] = deltaO3[i].astype('float64')
    for j in reversed(deltaO3[i].columns):
        deltaO3[i][j] = deltaO3[i]['scalaire'] / deltaO3[i][j]
        
#%%regrouperment en tableau pour l'affichage

delta_O1 = pd.concat(deltaO1).swaplevel()
speed_up_O1 = delta_O1.loc['TOTAL_NCYCLES']
energy_gain_O1 = delta_O1.loc['TOTAL_ENERGY_COST']

delta_Os = pd.concat(deltaOs).swaplevel()
speed_up_Os = delta_Os.loc['TOTAL_NCYCLES']
energy_gain_Os = delta_Os.loc['TOTAL_ENERGY_COST']

delta_O3 = pd.concat(deltaO3).swaplevel()
speed_up_O3 = delta_O3.loc['TOTAL_NCYCLES']
energy_gain_O3 = delta_O3.loc['TOTAL_ENERGY_COST']

#%% affichage des résultats

resulat = [energy_gain_O1,energy_gain_Os,energy_gain_O3,speed_up_O1,speed_up_Os,speed_up_O3]
titre = ['O1','Os','O3']
plt.figure(0,figsize=(14,10))
x = np.arange(4)
for i in range(3):
    plt.subplot(2,3,i+1)
    plt.bar(x-0.3,resulat[i]["scalaire"],0.1)
    plt.bar(x-0.2,resulat[i]["32"],0.1)
    plt.bar(x-0.1,resulat[i]["32Br"],0.1)
    plt.bar(x,resulat[i]["16"],0.1)
    plt.bar(x+0.1,resulat[i]["16Br"],0.1)
    plt.bar(x+0.2,resulat[i]["8"],0.1)
    plt.bar(x+0.3,resulat[i]["8Br"],0.1)
    plt.legend(["scalaire", "32", "32Br", "16", "16Br", "8", "8Br"], loc = 2)
    plt.title(titre[i])
    plt.xticks(x, ['basic', 'long', 'pad', 'stride'])
    plt.yticks(np.arange(9))
    if i==0 :
        plt.ylabel("Energy Gain",rotation='horizontal',horizontalalignment = 'right')
for i in range(3,6):
    plt.subplot(2,3,i+1)
    plt.bar(x-0.3,resulat[i]["scalaire"],0.1)
    plt.bar(x-0.2,resulat[i]["32"],0.1)
    plt.bar(x-0.1,resulat[i]["32Br"],0.1)
    plt.bar(x,resulat[i]["16"],0.1)
    plt.bar(x+0.1,resulat[i]["16Br"],0.1)
    plt.bar(x+0.2,resulat[i]["8"],0.1)
    plt.bar(x+0.3,resulat[i]["8Br"],0.1)
    plt.legend(["scalaire", "32", "32Br", "16", "16Br", "8", "8Br"], loc = 2)
    plt.xticks(x, ['basic', 'long', 'pad', 'stride'])
    plt.yticks(np.arange(0,6,0.5))
    if i==3 :
        plt.ylabel("Speed Up",rotation='horizontal',horizontalalignment = 'right')
# plt.show()
plt.savefig("figure.jpg")



#%%
# resulat = [energy_gain_O1,energy_gain_Os,energy_gain_O3,speed_up_O1,speed_up_Os,speed_up_O3]
# titre = ['O1','Os','O3']
# plt.figure(1)
# x = np.arange(4)
# for i in range(3):
#     plt.subplot(2,3,i+1)
#     plt.bar(x-0.2,resulat[i]["scalaire"],0.1)
#     plt.bar(x-0.1,resulat[i]["32"],0.1)
#     plt.bar(x,resulat[i]["32Br"],0.1)
#     plt.bar(x+0.1,resulat[i]["16"],0.1)
#     plt.bar(x+0.2,resulat[i]["16Br"],0.1)
#     plt.legend(["scalaire", "32", "32Br", "16", "16Br"], loc = 2)
#     plt.title(titre[i])
#     plt.xticks(x, ['basic', 'long', 'pad', 'stride'])
#     plt.yticks(np.arange(9))
#     if i==0 :
#         plt.ylabel("Energy Gain",rotation='horizontal',horizontalalignment = 'right')
# for i in range(3,6):
#     plt.subplot(2,3,i+1)
#     plt.bar(x-0.2,resulat[i]["scalaire"],0.1)
#     plt.bar(x-0.1,resulat[i]["32"],0.1)
#     plt.bar(x,resulat[i]["32Br"],0.1)
#     plt.bar(x+0.1,resulat[i]["16"],0.1)
#     plt.bar(x+0.2,resulat[i]["16Br"],0.1)
#     plt.legend(["scalaire", "32", "32Br", "16", "16Br"], loc = 2)
#     plt.xticks(x, ['basic', 'long', 'pad', 'stride'])
#     plt.yticks(np.arange(0,6,0.5))
#     if i==3 :
#         plt.ylabel("Speed Up",rotation='horizontal',horizontalalignment = 'right')
# plt.show()


