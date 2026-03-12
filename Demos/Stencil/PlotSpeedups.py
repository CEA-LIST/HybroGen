#!/usr/bin/env python3

def error(msg):
    print (msg)
    sys.exit(-1)

def putInDict2(d, key1, key2, value):
    if key1 not in d: # Create with 1st itération
        d[key1] = {key2:value}
    elif key2 not in d[key1]:             # Add with 2nd
        d[key1][key2] = value
    else:
        d[key1][key2].update(value)

def printDict(d):
    for k1 in d:
        print (f"{k1}:")
        for k2 in d[k1]:
            print (f"\t{k2}:{d[k1][k2]}")

def mergeCVS(noOptCVSFile, optCVSFile):
# Log Format :
# 0  FilterName
# 1  FilterSize
# 2  ImageSize
# 3  StaticTimeExecution
# 4  DynamicTimeExecution
# 5  InsnCodeGenerationTime
# 6  Error Number

    dataSet = {}
    with open (noOptCVSFile, 'r') as csvfile:
        reader = csv.reader (csvfile, delimiter =';')
        for line in reader:
            # breakpoint()
            if len(line) == 8: # avoid comment & error lines
                if line[7] != "0": print (f"Warning {line[7]} error for {line[0]}")
                filterName = line[0]
                imageSize  = line[2]
                data = {# "imageSize":  line[2],
                        "clockNoOpt":           line[3],
                        "clockCompiletteNoOpt": line[4],
                        "clockCodeGenNoOpt":    line[5],
                        "insnCount":            line[6],
                        }
                putInDict2(dataSet, filterName, imageSize, data)
    with open (optCVSFile, 'r') as csvfile:
        reader = csv.reader (csvfile, delimiter =';')
        for line in reader:
            if len(line) == 8: # avoid comment & error lines
                if line[7] != "0": print (f"Warning {line[7]} error for {line[0]}")
                filterName = line[0]
                imageSize  = line[2]
                data = {# "imageSize":  line[2],
                        "clockOpt":           line[3],
                        "clockCompiletteOpt": line[4],
                        "clockCodeGenOpt":    line[5],
                        }
                putInDict2(dataSet, filterName, imageSize, data)
    return dataSet

if __name__ == "__main__":
    import os, re, sys, csv, pprint
    import matplotlib.pyplot as plt

    if len(sys.argv) < 3:
        error("Give 2 csv filename")
    results = {}
    fileNameNoOpt = sys.argv[1]
    fileNameOpt   = sys.argv[2]
    if '-O0' not in fileNameNoOpt:
        error (f"No -O0 in {fileNameNoOpt}")
    if '-O3' not in fileNameOpt:
        error (f"No -O3 in {fileNameOpt}")
    d = mergeCVS (fileNameNoOpt, fileNameOpt)
    printDict(d)
    fig, ax = plt.subplots(figsize=(6, 6))
    imgSizeListMax = []
    imgSizeListMaxName = []
    for fName in d:
        # print (fName)
        imgSizeListName = d[fName].keys()
        imgSizeList = []
        print (imgSizeListName)
        for WxH in imgSizeListName: # Transform "1920x1200" in 2304000
            w, h = WxH.split("x")
            imgSizeList += [int(w)*int(h)]
        print (imgSizeList)
        speedupsOpt        = [100*int(d[fName][z]["clockNoOpt"])/int(d[fName][z]["clockOpt"]) for z in d[fName].keys()]
        speedupsCompilette = [100*int(d[fName][z]["clockNoOpt"])/int(d[fName][z]["clockCompiletteOpt"]) for z in d[fName].keys()]
        print (speedupsOpt)
        print (speedupsCompilette)
        plt.plot(imgSizeList, speedupsOpt, "-D", label=fName+"O3")
        plt.plot(imgSizeList, speedupsCompilette, "-D", label=fName+"Compilette")
    # print(imgSizeListMax)
    plt.xticks(imgSizeList, imgSizeListName, rotation=45)
    ax.legend()
    print (f"Results in {fileNameOpt}.png")
    plt.savefig(fileNameOpt+".png")
