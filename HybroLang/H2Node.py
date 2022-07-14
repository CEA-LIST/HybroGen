#!/usr/bin/env python3

from HybroLang.H2SymbolTable  import H2SymbolTable
from HybroLang.H2LabelTable   import H2LabelTable
from HybroLang.H2NodeType     import H2NodeType
import sys

class H2Node():
    """Expression node for HybroLang intermediate representation"""

    def __init__(self, nodeType, sonsList=None, constValue = None, variableName = None, opName = None, opType = None, labelName = None, targetName = None, sourceName = None):
        """Initialise a node"""
        self.nodeType  = nodeType
        if sonsList == None:
            self.sonsList  = []
        else:
            self.sonsList = sonsList
        self.opName = opName
        self.setConstValue(constValue)
        self.setVariableName(variableName)
        self.setLabelName(labelName)
        self.setTargetName(targetName)
        self.setSourceName(sourceName)
        self.setNodeType (opType)
        self.regId = None

    def __iter__(self):
        return self.sonsList.__iter__()

    def getStr(self, i = 0):
        s = str(self.nodeType)
        if self.nodeType == H2NodeType.OPERATOR or self.nodeType == H2NodeType.W or self.nodeType == H2NodeType.R :
            s += ": %s"%(str(self.getOpName()))
            if None != self.regId:
                s += " : reg %s"%self.getRegister()
            if self.hasType():
                s += ": %s"%(self.getNodeType())
            s += "\n"
            for son in self.sonsList:
                if son != None:
                    s += "%s%s"%("\t"*(i+1), son.getStr(i+1))
                else:
                    s += "%s%s"%("\t"*(i+1), str(son))
        elif self.nodeType == H2NodeType.VARIABLE:
            s += ": %s\n"%(self.getVariableName())
        elif self.nodeType == H2NodeType.LABEL:
            s += ": %s\n"%(self.getLabelName())
        elif self.nodeType == H2NodeType.CALLBACK:
            s += ": %s\n"%(self.getCallbackName())
        elif self.nodeType == H2NodeType.RTN:
            s += ": %s\n"%("RETURN")
        elif self.nodeType == H2NodeType.CONST:
            s += ": %s"%(self.getConstValue())
            if self.hasType():
                s += ": %s"%(self.getNodeType())
            s += "\n"
        elif self.isB() or self.isCmp():
            s += ": %s %s"%(self.nodeType, self.targetName)
            s += ": %s %s"%(self.nodeType, self.sourceName)
            for son in self.sonsList:
                if son != None:
                    s += "%s%s"%("\t"*(i+1), son.getStr(i+1))
                else:
                    s += "%s%s"%("\t"*(i+1), str(son))
        else:
            self.fatalError("Unknown node %s"%self.nodeType)
        return s

    def fatalError (self, msg):
        print ("Fatal error: %s"%msg)
        sys.exit(-1)

    def __str__(self, i = 0):
        return self.getStr(i)

    def setRegister (self, regId):      self.regId = regId
    def getRegister (self):        	return self.regId

    def setConstValue(self, constValue): self.constValue = constValue
    def getConstValue(self):         	return self.constValue

    def setVariableName (self, variableName):   self.variableName = variableName
    def getVariableName (self):        		return self.variableName
    def hasVariableName (self):        		return None != self.variableName

    def setTargetName (self, targetName):       self.targetName = targetName
    def getTargetName (self):        		return self.targetName
    def hasTargetName (self):        		return None != self.targetName
    def setSourceName (self, sourceName):       self.sourceName = sourceName
    def getSourceName (self):        		return self.sourceName
    def hasSourceName (self):        		return None != self.sourceName

    def setLabelName (self, labelName):        	self.labelName = labelName
    def getLabelName (self):        		return self.labelName
    def hasLabelName (self):        		return None != self.labelName
    def isLabel(self):         			return self.hasLabelName()

    def setNodeType (self, opType):        self.opType = opType
    def getNodeType (self):        	   return self.opType
    def hasType (self):        		   return self.opType != None

    def isOperator (self):     return self.nodeType == H2NodeType.OPERATOR
    def isConst (self):        return self.nodeType == H2NodeType.CONST
    def isRtn (self):          return self.nodeType == H2NodeType.RTN
    def isR (self):            return self.nodeType == H2NodeType.R
    def isW (self):            return self.nodeType == H2NodeType.W
    def isCmp (self):          return self.nodeType in ( H2NodeType.CMP, H2NodeType.CMPEQ, H2NodeType.CMPNE, H2NodeType.CMPLT, H2NodeType.CMPGT, H2NodeType.CMPGE, H2NodeType.CMPLE)
    def isVariable (self):     return self.nodeType == H2NodeType.VARIABLE
    def isOperatorOrMem(self): return self.isMem() or (self.nodeType == H2NodeType.OPERATOR)
    def isB(self):             return self.nodeType == H2NodeType.BA or self.isBcc()
    def isBcc(self):           return self.nodeType in (H2NodeType.BEQ, H2NodeType.BNE, H2NodeType.BLT, H2NodeType.BGT, H2NodeType.BGE, H2NodeType.BLE, H2NodeType.BEQZ, H2NodeType.BNEZ)
    def isMem(self):           return (self.nodeType == H2NodeType.W) or (self.nodeType == H2NodeType.R)


    sem = {"*": "MUL", "+":"ADD", "/":"DIV", "-":"SUB", "=":"MV", "W":"W", "R":"R", "L":"LOOP",
           "&&":"AND", "||":"OR", "SL":"SL",  "SR":"SR", "<<":"SL", ">>":"SR", "LUI":"LUI", "INV":"INV", "NEG": "NEG", "MVIF":"MVIF", "MVFI":"MVFI",
           "SL":"SL",  "SR":"SR", "OR":"OR", "AND":"AND", # TODO this line should be removed
    }
    def setOpName (self, opName):       self.opName = self.sem[opName]
    def getOpName (self):        	return self.opName
    def getSemName (self):        	return self.sem[self.opName]

    def isVector(self): return (isinstance(self.opType['vectorLen'], int) and self.opType['vectorLen'] > 1) or (isinstance(self.opType['vectorLen'], str) and  self.opType['vectorLen'].isdigit() and int(self.opType['vectorLen']) > 1)
