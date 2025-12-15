#!/usr/bin/env python3


if __name__ == "__main__":
    import sys

    inputFile = open (sys.argv[1])
    dataSet = inputFile.readlines()
    lineNumber = 0
    w, h = dataSet[2].split ()
    print ("Image %s (%sx%s)"%(sys.argv[1], w, h))
    for line in dataSet[4:]:
        lineNumber += 1
        print(line[:-1], end=';')
        if lineNumber % 8 == 0:
            print ()
