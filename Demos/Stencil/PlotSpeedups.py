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
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html
    if len(sys.argv) < 4:
        error("Give 2 csv filename + image size")
    results = {}
    fileNameNoOpt = sys.argv[1]
    fileNameOpt   = sys.argv[2]
    imageSize     = sys.argv[3]
    imageSizeSet = ("13x10", "160x120", "320x240", "1024x768",)
    if '-O0' not in fileNameNoOpt:
        error (f"No -O0 in {fileNameNoOpt}")
    if '-O3' not in fileNameOpt:
        error (f"No -O3 in {fileNameOpt}")
    if imageSize not in (imageSizeSet):
        error (f"Image size should be in {imageSizeSet}")
    d = mergeCVS (fileNameNoOpt, fileNameOpt)
    #   printDict(d)

    imgSizeListMax = []
    imgSizeListMaxName = []
    filterNames = [k.split("/")[1] for k in d.keys()]
    #    print (filterNames)
    r = {}
    r["O0"]         = [int(d[x][imageSize]["clockNoOpt"])     for x in d.keys()]
    r["O3"]           = [int(d[x][imageSize]["clockOpt"])       for x in d.keys()]
    r["Compilette"] = [int(d[x][imageSize]["clockCompiletteOpt"]) for x in d.keys()]
    r["clockCodeGen"]= [int(d[x][imageSize]["clockCodeGenOpt"]) for x in d.keys()]
    width = 0.25
    multiplier = 0
    x = [l for l in range(len(filterNames))]
    # print (x)
    fig, ax = plt.subplots(layout='constrained')
    # print (r)
    for key in ("O0", "O3", "Compilette"):
        print (key)
        print (r[key])
        offset = width * multiplier
        rects = ax.bar([dx+offset for dx in x], r[key], width, label=key)
        # ax.bar_label(rects, padding=3)
        multiplier += 1
    rects = ax.bar([dx+offset for dx in x], r["clockCodeGen"], width, bottom = r["Compilette"], label="Code Generation")

#    plt.tight_layout()
#    plt.subplots_adjust(bottom=0.15)
    ax.set_ylabel("Clock cycle")
    ax.set_xticks([d+width for d in x], filterNames)
    plt.xticks(rotation=45)
#    plt.yscale("log")
    ax.legend (ncol=3)
    ax.set_title("Stencil execution time in clock cycle\n(-O0 versus -O3 versus Compilette + Code Generation time)")
#    plt.show()
    print (f"Results in {fileNameOpt}-{imageSize}.png")
    plt.savefig(f'{fileNameOpt}-{imageSize}.png')
