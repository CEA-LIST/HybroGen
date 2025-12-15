#!/usr/bin/env python3


class H2ContextHandling:
    def __init__(self, parameterNumber, localVariableNumber):
        """Generate code generator for stack handling"""

    def AarchCalleeSaveInit(self, regList):
        numberOfRegister = len(regList)
        stackSize = 8 + 4*numberOfRegister # P39 of aarch procudure call
        sValue = self.genImmValue(stackSize)
        initCode = ["aarch64_genSUB_3(H2Aarch64SP, H2Aarch64SP, %s);"%(sValue)]
        for i in range(len(regList)):
            aarch64RegToSave = self.genFixedRegister(regList[i])
            aarch64StackIndex = self.genImmValue(stackSize - (4 * i))
            initCode += ["aarch64_genW_3(H2Aarch64SP, %s, %s);"%(aarch64RegToSave, aarch64StackIndex)]
        return initCode

    def Aarch64CalleeSaveRestore(self, regList):
        numberOfRegister = len(regList)
        stackSize = 8 + 4*numberOfRegister # P39 of aarch procedure call
        sValue = self.genImmValue(stackSize)
        restoreCode = []
        for i in range(len(regList)):
            aarch64RegToSave = self.genFixedRegister(regList[i])
            aarch64StackIndex = self.genImmValue(stackSize - (4*i))
            restoreCode += ["aarch64_genR_3(%s, H2Aarch64SP, %s);"%(aarch64RegToSave, aarch64StackIndex)]
        restoreCode += ["aarch64_genADD_3(H2Aarch64SP, H2Aarch64SP, %s);"%(sValue)]
        return restoreCode
