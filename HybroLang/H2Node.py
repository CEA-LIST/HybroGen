#!/usr/bin/env python3

from H2Utils import *
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
        self.setOpType (opType)
        self.regId = None

    def __iter__(self):
        return self.sonsList.__iter__()

    def getNodeName(self):
        t = str(self.getNodeType())
        if self.nodeType == H2NodeType.OPERATOR or self.nodeType == H2NodeType.W or self.nodeType == H2NodeType.R :
            name = "_%s"%(self.getOpName())
        elif self.nodeType == H2NodeType.VARIABLE: name = "_%s"%(self.getVariableName())
        elif self.nodeType == H2NodeType.LABEL:    name = "_%s"%(self.getLabelName())
        elif self.nodeType == H2NodeType.CALLBACK: name = "_%s"%(self.getCallbackName())
        elif self.nodeType == H2NodeType.RTN:      name = "_%s"%("RETURN")
        elif self.nodeType == H2NodeType.CONST:    name = "_%s"%(self.getConstValue())
        elif self.isB() or self.isCmp():           name = "_%s"%(self.nodeType)
        else:
            fatalError("Unknown node %s"%self.nodeType)
        return t+name

    def getStr(self, i = 0):
        s = str(self.nodeType)
        if self.nodeType == H2NodeType.OPERATOR or self.nodeType == H2NodeType.W or self.nodeType == H2NodeType.R :
            s += ": %s"%(str(self.getOpName()))
            if None != self.regId:
                s += " : reg %s"%self.getRegister()
            if self.hasOpType():
                s += ": %s"%(self.getOpType())
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
        elif self.nodeType == H2NodeType.VCONF:
            s += ": %s"%("VCONF")
            s += ": %s\n"%(self.getOpType())
        elif self.nodeType == H2NodeType.RTN:
            s += ": %s\n"%("RETURN")
        elif self.nodeType == H2NodeType.CONST:
            s += ": %s"%(self.getConstValue())
            if self.hasOpType():
                s += ": %s"%(self.getOpType())
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
            fatalError("Unknown node %s"%self.nodeType)
        return s

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

    def setNodeType (self, nodeType):   self.nodeType = nodeType
    def getNodeType (self):        	return self.nodeType
    def hasType (self):        		return self.nodeType != None

    def setOpType (self, opType):	self.opType = opType
    def getOpType (self):		return self.opType
    def hasOpType (self):		return self.opType != None

    def setOpName (self, opName):       self.opName = self.sem[opName]
    def getOpName (self):        	return self.opName

    def isOperator (self):     return self.nodeType == H2NodeType.OPERATOR
    def isConst (self):        return self.nodeType == H2NodeType.CONST
    def isRtn (self):          return self.nodeType == H2NodeType.RTN
    def isR (self):            return self.nodeType == H2NodeType.R
    def isW (self):            return self.nodeType == H2NodeType.W
    def isCmp (self):          return self.nodeType in ( H2NodeType.CMP, H2NodeType.CMPEQ, H2NodeType.CMPNE, H2NodeType.CMPLT, H2NodeType.CMPGT, H2NodeType.CMPGE, H2NodeType.CMPLE)
    def isVariable (self):     return self.nodeType == H2NodeType.VARIABLE
    def isOperatorOrMem(self): return self.isMem() or (self.nodeType == H2NodeType.OPERATOR)
    def isB(self):             return self.nodeType == H2NodeType.BA or self.isBcc()
    def isBA(self):            return self.nodeType == H2NodeType.BA
    def isBcc(self):           return self.nodeType in (H2NodeType.BEQ, H2NodeType.BNE, H2NodeType.BLT, H2NodeType.BGT, H2NodeType.BGE, H2NodeType.BLE, H2NodeType.BEQZ, H2NodeType.BNEZ)
    def isMem(self):           return (self.nodeType == H2NodeType.W) or (self.nodeType == H2NodeType.R)
    def isVCONF (self):        return self.nodeType == H2NodeType.VCONF

    sem = {"*": "MUL", "+":"ADD", "/":"DIV", "-":"SUB", "=":"MV", "RTN":"RET",
           "W":"W", "R":"R", "L":"LOOP", "MAC":"MAC", "^": "XOR",
           "&":"AND", "|":"OR", "SL":"SL", "SR":"SR", "<<":"SL",
           ">>":"SR", "LUI":"LUI", "INV":"INV", "NEG": "NEG",
           "MVIF":"MVIF", "MVFI":"MVFI", "SL":"SL", "SR":"SR",
           "OR":"OR", "AND":"AND", # TODO this line should be removed
           }

    def getSemName (self):
        if self.nodeType == H2NodeType.OPERATOR: return self.sem[self.opName]
        else: return str(self.nodeType).split(".")[1] # Remove "HyNodeType." from node type

    def isVector(self): return (isinstance(self.opType['vectorLen'], int) and self.opType['vectorLen'] > 1) or (isinstance(self.opType['vectorLen'], str) and  self.opType['vectorLen'].isdigit() and int(self.opType['vectorLen']) > 1)

    def areNodesEquals(self, other):
        if self.nodeType != other.getNodeType(): return False
        if self.labelName != other.getLabelName(): return False
        if self.opName != other.getOpName(): return False
        if self.constValue != other.getConstValue(): return False
        if self.variableName != other.getVariableName(): return False
        return True

    def isSameTree(self, other):
        if self.areNodesEquals(other):
            if self.sonsList == [] and other.sonsList == []:
                return True
            else :
                for i in range (len(self.sonsList)):
                    if self.sonsList[i].isSameTree(other.sonsList[i]) == False :
                        return False
                return True
        else:
            return False
