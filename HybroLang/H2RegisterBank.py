#!/usr/bin/env python3
import sys

from enum import Enum

class H2RegisterAllocationType(Enum):
    """
    Enumeration type to manipulate the allocation flags of H2RegisterBank
    """
    FREE = 0
    USED = 1

regCorrespondances = {"int":"int","uint":"int","flt":"flt","sint":"int","suint":"int", "vint":"vint","int[]":"int"}
class H2RegisterBank():
    """
    The H2RegisterBank models the list of available registers of a given type,
    according to the format of the IsaDB database.
    """
    def __init__(self, name: str, arith: str, numberList: list, verbose=False):
        """
        The initialization method takes into parameters its name,
        the arithmetical type with which initalizazing the register bank
        and its list of register indices
        For the allocator to work, we create a second list containing
        allocation flags to check which ones are already allocated or not, e.g. :
        self.numberList {
            "int" : [ [2, 3, 5, 7, 9, 14, ...],
                      [FREE, USED, USED, FREE, FREE, FREE, ...] ]
        }
        The methods of H2RegisterBank should use H2RegisterAllocationType
        to manipulate the allocation flags
        """
        self.bankName = name
        self.verbose = verbose
        nb_registers = len(numberList[0])
        if 0 == nb_registers:
            self.fatalError ("Not enough defined registers (%d). Is the database initialized ?"%nb_registers)
        alloc_flags = [H2RegisterAllocationType.FREE] * nb_registers
        self.numberList = {arith: [numberList[0],numberList[1], alloc_flags]}

    def print(self, s):
        if self.verbose:
            print(str(self))

    def fatalError(self, s):
        print(s)
        sys.exit(-1)

    def getNextRegister(self, arith_: str):
        # global regCorrespondances
        arith = regCorrespondances[arith_]
        numberList = self.numberList[arith][0]
        regNameList = self.numberList[arith][1]
        alloc_flags = self.numberList[arith][2]
        try:
            index = alloc_flags.index(H2RegisterAllocationType.FREE)
            regNo = numberList[index]
            alloc_flags[index] = H2RegisterAllocationType.USED
            regName = regNameList[index]
            try:
                for other_arith in self.numberList.keys():
                    if arith != other_arith:
                        numberList = self.numberList[other_arith][0]
                        regNameList = self.numberList[other_arith][1]
                        alloc_flags = self.numberList[other_arith][2]
                        index = regNameList.index(regName)
                        if regNameList.index(regName) != None:
                            alloc_flags[index] = H2RegisterAllocationType.USED
            except ValueError as ex:
                pass
            self.print ("Allocated register %d for '%s'"%(regNo, arith))
            return regNo
        except ValueError as ex:
            self.fatalError("%s : No more register available for '%s'"%(self.bankName, arith))

    def freeRegister(self, arith_: str, regNo: int):
        arith = regCorrespondances[arith_]
        numberList = self.numberList[arith][0]
        regNameList = self.numberList[arith][1]
        alloc_flags = self.numberList[arith][2]
        try:
            index = numberList.index(regNo)
            alloc_flags[index] = H2RegisterAllocationType.FREE
            regName = regNameList[index]
            try:
                for other_arith in self.numberList.keys():
                    if arith != other_arith:
                        numberList = self.numberList[other_arith][0]
                        regNameList = self.numberList[other_arith][1]
                        alloc_flags = self.numberList[other_arith][2]
                        index = regNameList.index(regName)
                        if regNameList.index(regName) != None:
                            alloc_flags[index] = H2RegisterAllocationType.FREE
            except ValueError as ex:
                pass
        except ValueError as ex:
            self.fatalError("%s : Register #%d does not exist for '%s'"%(self.bankName, regNo, arith))
        self.print ("%s : Freed register %d for '%s'"%(self.bankName, regNo, arith))

    def add(self, arith, numberList):
         nb_registers = len(numberList[0])
         alloc_flags = [H2RegisterAllocationType.FREE] * nb_registers
         self.numberList.update({arith: [numberList[0],numberList[1], alloc_flags]})
         self.print("Adding arithmetic '%s' --->:" % arith)
         self.print("\n" + str(self))

    def __str__(self):
         s = "Register bank %s :\n" % self.bankName
         for arith in self.numberList.keys():
             s += "- %s\n" % arith
             s += "".join(map(lambda x: "%5d" % x, self.numberList[arith][0])) + "\n"
             s += "".join(map(lambda x: "%5s" % x.name, self.numberList[arith][2])) + "\n"
         return s
