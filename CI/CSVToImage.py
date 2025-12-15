#!/usr/bin/env python3

def readCSVtoDict(fileName):
    svIn = csv.reader (open (fileName, "r"), delimiter=";")
    theList = {}
    next(svIn) # skip csv title
    for l in svIn:
        # print((l[0], l[1], l[2], l[3], l[4]))
        # print([r for r l l[5:] if len(r) > 0])
        if len(l) > 0: # If line non empty
            theList[(l[0], l[1], l[2], l[3], l[4])] = ([r for r in l[5:] if len(r) > 0])
    return theList


if __name__ == "__main__":
    import csv
    from PIL import Image, ImageDraw

    refDict  = readCSVtoDict("RegressionSingleOpReference.csv")
    cellSize = (10, 10)
    vLen = [1, 2, 4, 8, 16]
    wLen = [8, 16, 32, 64]
    i = Image.new (mode="RGB", size = (cellSize[0]*len (vLen)*len (wLen), 3*10+cellSize[1]))
    d = ImageDraw.Draw(i)
    cursor = (30, 0)
    for v in vLen:
        for w in wLen:
            print (cursor)
            key = ("aarch64", "value", "add", "int", str(v))
            print(key, refDict.get(key), str(w) in refDict.get(key))
            area = (cursor[0], cursor[1], cursor[0]+10, cursor[1]+10)
            print (area)
            color = (0, 255, 0) if str(w) in refDict.get(key) else (255, 0, 0)
            d.rectangle(area, fill=color)
            cursor = (cursor[0] + 10, cursor[1])
    i.show()
