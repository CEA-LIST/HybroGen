#!/usr/bin/env python3

class SwConfig():
    """
    Central database for software (gcc and qemu) configurations build & use
    """
    def __init__(self, configFileName = "SwConfig.csv"):
        import csv
        self.dataBase = {}
        try: # Search file configuration in current dir or parent
            reader = csv.DictReader(open(configFileName))
        except FileNotFoundError:
            reader = csv.DictReader(open("../"+configFileName))
        for r in reader:
            self.dataBase[r["archList"]] = r

    def getKeys(self):
        return self.dataBase.keys()

    def getCompilerForArch (self, archName):
        return self.dataBase[archName]["triplet"]+"-gcc"

    def getTripletForArch (self, archName):
        return self.dataBase[archName]["triplet"]

    def getQemuForArch(self, archName):
        return self.dataBase[archName]["exec"]

    def getQemuTripletForArch(self, archName):
        return self.dataBase[archName]["qemu-triplet"]

if __name__ == '__main__' :
    c = SwConfig()
    archList = c.getKeys()
    print (archList)
    print ("%25s %25s %20s %25s"%("Compiler", "Triplet", "Qemu-Exec", "Qemu-Triplet"))
    for a in archList:
        print ("%25s %25s %20s %25s"%(c.getCompilerForArch(a), c.getTripletForArch(a), c.getQemuForArch(a), c.getQemuTripletForArch(a), ))
