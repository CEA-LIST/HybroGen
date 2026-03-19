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
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html
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

    imgSizeListMax = []
    imgSizeListMaxName = []
    filterNames = [k.split("/")[1] for k in d.keys()]
    print (filterNames)
    r = {}
    r["noOpt"]         = [int(d[x]["1024x768"]["clockNoOpt"])     for x in d.keys()]
    r["opt"]           = [int(d[x]["1024x768"]["clockOpt"])       for x in d.keys()]
    r["CompiletteOpt"] = [int(d[x]["1024x768"]["clockCompiletteOpt"]) for x in d.keys()]
    width = 0.25
    multiplier = 0
    x = [l for l in range(len(filterNames))]
    # print (x)
    fig, ax = plt.subplots(layout='constrained')
    # print (r)
    for key in r:
        print (key)
        print (r[key])
        offset = width * multiplier
        rects = ax.bar([dx+offset for dx in x], r[key], width, label=key)
        ax.bar_label(rects, padding=3)
        multiplier += 1
#    plt.tight_layout()
#    plt.subplots_adjust(bottom=0.15)
    ax.set_ylabel("Clock cycle")
    ax.set_xticks([d+width for d in x], filterNames)
    plt.xticks(rotation=45)
    ax.set_title("Stencil execution time speedups relative to cc -O0")
    print (f"Results in {fileNameOpt}.png")
    plt.savefig(fileNameOpt+".png")
