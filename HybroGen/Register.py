#!/usr/bin/env python3

class Register:
    """Define an register structure : 
    * archname
    * extension
    * registername
    * registerwidth
    * registertype
    * function   
 """
    def __init__(self, archname):
        self.archname = archname
        self.extension = -1
        self.registerName = []
        self.registerwidth = -1
        self.registerType = -1
        self.function = []
        self.prefix = ""
        self.isVector = False
                      
    def setExtension(self, extension):
        self.extension = extension
        
    def setRegisterName(self, name):
        self.registerName.append(name)

    def setRegisterWidth(self, width):
        self.registerwidth = width

    def setRegisterType(self, regtype):
        self.registerType = regtype

    def setFunction(self, regFunction):
        self.function.append(regFunction)
        
    def setPrefix  (self, prefix):
        self.prefix = prefix

    def setIsVector (self, vec):
        self.isVector = vec

    def getExtension(self):
        return self.extension
        
    def getRegisterName(self):
        return self.registerName

    def getRegisterWidth(self):
        return self.registerwidth

    def getRegisterType(self):
        return self.registerType

    def getFunction(self):
        return self.function

    def getPrefix  (self):
        return self.prefix

    def getIsVector (self):
        return self.isVector
    def __str__(self):
        return  "%s %s %s %s %s %s %s"%(self.archname, self.extension, self.registerwidth, self.registerType, self.isVector, self.registerName[0], self.function[0])
