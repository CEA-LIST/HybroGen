#!/usr/bin/env python3

def error(msg):
    print (msg)
    sys.exit(-1)

if __name__ == "__main__":
    import os, re, sys, csv, pprint
    import matplotlib.pyplot as plt

    if len(sys.argv) < 2:
        error("Give csv filename")
    results = {}
    fileName = sys.argv[1]
    with open (fileName, 'r') as csvfile:
        reader = csv.reader (csvfile, delimiter =';')
        # Format : FilterName ; ImgSize ; StaticTimeExecution ; DynamicTimeExecution ; CodeGenerationTime ; InsnNumer ; ErrorNumber
        #          Filter/Null-3x3.pgm ; 3x3 ; 320x240 ; 12388250 ; 7516938 ; 293938 ; 68 ; 0
        #           0          1       2                  3                       4                5             6
        for line in reader:
            if len(line) > 1: # avoid "segfault"
                filterName = line[0]
                if filterName in results:
                    results[filterName] += [line[2:]] #
                else:
                    results[filterName] = []
    pprint.pprint(results)
    fig, ax = plt.subplots(figsize=(6, 6))
    imgSizeListMax = []
    imgSizeListMaxName = []
    for filterName in results:
        print (filterName)
        imgList = [data[0] for data in results[filterName] ]
        imgSizeList = []
        for data in results[filterName]: # Transform "1920x1200" in 2304000
            w, h = data[0].split("x")
            imgSizeList += [int(w)*int(h)]
        if len (imgList) > len(imgSizeListMax):
            imgSizeListMaxName = imgList
            imgSizeListMax = imgSizeList
        speedups= [100*int(data[1])/int(data[2]) for data in results[filterName] ]
        print (imgList)
        print (imgSizeList)
        print (speedups)
        plt.plot(imgSizeList, speedups, "-D", label=filterName)
    print(imgSizeListMax)
    plt.xticks(imgSizeListMax, imgSizeListMaxName, rotation=45)
    ax.legend()
    print (f"Results in {fileName}.png")
    plt.savefig(fileName+".png")
