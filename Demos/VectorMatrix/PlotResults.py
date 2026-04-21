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
# 0  Transformation Matrix Name
# 1  Vectors Number
# 2  clockCPU
# 3  clockCompilette
# 4  InsnCodeGenerationTime
# 5  InstructionCount
# 6  Error (true / false)
# 7  Dummy value to avoid optimization
    dataSet = {}
    with open (noOptCVSFile, 'r') as csvfile:
        reader = csv.reader (csvfile, delimiter =';')
        for line in reader:
            # breakpoint()
            if len(line) == 7: # avoid comment & error lines
                if line[6] != "false": print (f"Warning {line[6]} error for {line[0]}")
                matrixName = line[0]
                vectorNumber  = line[1]
                data = {# "imageSize":  line[2],
                        "matrixName":           line[0],
                        "clockNoOpt":           line[2],
                        "clockCompiletteNoOpt": line[3],
                        "clockCodeGenNoOpt":    line[4],
                        "insnCount":            line[5],
                        }
                putInDict2(dataSet, matrixName, vectorNumber, data)
    with open (optCVSFile, 'r') as csvfile:
        reader = csv.reader (csvfile, delimiter =';')
        for line in reader:
            if len(line) == 7: # avoid comment & error lines
                if line[6] != "false": print (f"Warning {line[6]} error for {line[0]}")
                matrixName = line[0]
                vectorNumber  = line[1]
                data = {# "imageSize":  line[2],
                        "clockOpt":           line[2],
                        "clockCompiletteOpt": line[3],
                        "clockCodeGenOpt":    line[4],
                        }
                putInDict2(dataSet, matrixName, vectorNumber, data)
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
    vectorNumber     = sys.argv[3]
    vectorNumberSet = ("10", "100", "1000", "10000", "100000", "1000000")
    if '-O0' not in fileNameNoOpt:
        error (f"No -O0 in {fileNameNoOpt}")
    if '-O3' not in fileNameOpt:
        error (f"No -O3 in {fileNameOpt}")
    if vectorNumber not in (vectorNumberSet):
        error (f"Image size should be in {vectorNumberSet}")
    d = mergeCVS (fileNameNoOpt, fileNameOpt)
    printDict(d)

    imgSizeListMax = []
    imgSizeListMaxName = []
    filterNames = [k for k in d.keys()]
    #    print (filterNames)
    r = {}
    r["O0"]          = [int(d[x][vectorNumber]["clockNoOpt"])         for x in d.keys()]
    r["O3"]          = [int(d[x][vectorNumber]["clockOpt"])           for x in d.keys()]
    r["Compilette"]  = [int(d[x][vectorNumber]["clockCompiletteOpt"]) for x in d.keys()]
    r["clockCodeGen"]= [int(d[x][vectorNumber]["clockCodeGenOpt"])    for x in d.keys()]
    print (r)
    width = 0.25
    multiplier = 0
    x = [l for l in range(len(filterNames))]
    # print (x)
    fig, ax = plt.subplots(layout='constrained')
    for key in ("O0", "O3", "Compilette"):
        print (key, r[key])
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
    print (f"Results in {fileNameOpt}-{vectorNumber}.png")
    plt.savefig(f'{fileNameOpt}-{vectorNumber}.png')
