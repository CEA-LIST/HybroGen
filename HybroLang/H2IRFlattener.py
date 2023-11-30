#!/usr/bin/env python3

from H2Utils import *
# H2IR2 SStructures and Methods
from HybroLang.H2LabelTable import H2LabelTable
from HybroLang.H2SymbolTable import H2SymbolTable
from HybroLang.H2Node import H2Node
from HybroLang.H2IR2 import H2Type
from HybroLang.H2RegisterBank import H2RegisterBank
from HybroLang.H2NodeType import H2NodeType
import sys

class H2IRFlattener():
    """
    Flattens the input list of trees to transform them into SSA form
    - Author: Kévin Mambu, CEA Grenoble, 2022
    """
    def __init__(self, platform: dict, sTable: H2SymbolTable, verbose=False):
        self.sTable = sTable
        self.verbose = verbose
        self.call_counter = -1

    def visitInsn(self, insn:H2Node, parent:H2Node, new_insns:list):
        self.call_counter += 1
        need_tmp = parent is not None and parent.opName != '='
        if insn.isOperator() and insn.opName == 'LUI':
            const:H2Node = insn.sonsList[0]
            const.opType = insn.opType
            if insn.sonsList[0].isVariable() and len(insn.sonsList) > 1:
                var_name = insn.sonsList[0].getVariableName()
            else :
                var_name = "h2_%08d" % (self.call_counter)
                var = H2Node(H2NodeType.VARIABLE,
                    variableName=var_name,
                    opType=insn.opType)
                insn.sonsList.insert(0, var)
            new_insns.append(insn)
            insn.variableName = var_name
        elif insn.isOperator():
            # We sanitize the global datatype of the current sub-tree
            # according to the following priority: >> insn >> lhs >> rhs >> parent
            # TODO : modify HybroLang AST generation to systematically add datatypes to nodes
            lhs: H2Node = insn.sonsList[0]
            lhs.opType = insn.opType
            # We skip depth-1 assignments (e.g <dst_var> = <src_var>, or <dst_var> = <const_val>)
            if len(insn.sonsList) > 1:
                rhs: H2Node = insn.sonsList[1]
            if insn.opName == '=' and (rhs.isConst() or rhs.isVariable()):
                new_insns.append(insn)
                rhs.opType = insn.opType
                lhs.opType = insn.opType
                return
            # Update of the left-hand side node
            self.visitInsn(lhs, insn, new_insns)
            # Update of the left-hand side reference
            if lhs.variableName is not None and insn.opType != '=':
                insn.sonsList[0] = H2Node(
                    H2NodeType.VARIABLE,
                    opType=lhs.opType,
                    variableName=lhs.variableName)
            if len(insn.sonsList) > 1:
                rhs: H2Node = insn.sonsList[1]
                rhs.opType = insn.opType
                # Update of the right-hand side node
                self.visitInsn(rhs, insn, new_insns)
                # Update of the right-hand side reference
                if rhs.variableName is not None and insn.opType != '=':
                    insn.sonsList[1] = H2Node(
                        H2NodeType.VARIABLE,
                        opType=rhs.opType,
                        variableName=rhs.variableName)
            # Update of the new instructions
            lhs: H2Node = insn.sonsList[0]
            if parent is not None and parent.opName == '=':
                pass
            elif parent is not None and parent.opName != '=':
                op_type = insn.opType
                var_name = "h2_%08d" % (self.call_counter)
                var = H2Node(H2NodeType.VARIABLE,
                    variableName=var_name,
                    opType=op_type)
                new_insn = H2Node(
                    H2NodeType.OPERATOR,
                    opName='=',
                    opType=op_type,
                    sonsList=[var, insn])
                new_insns.append(new_insn)
                insn.variableName = var_name
            elif parent is None:
                insn.variableName = lhs.variableName
                if len(insn.sonsList) > 1:
                    rhs: H2Node = insn.sonsList[1]
                    rhs.variableName = lhs.variableName
                new_insns.append(insn)
        elif insn.isR() and parent != None:
            addr = insn.sonsList[0]
            addr.opType = H2Type('int', 32, 1)
            self.visitInsn(addr, insn, new_insns)
            if addr.variableName is not None:
                op_type  = addr.opType
                addr_name = addr.variableName
                new_addr = H2Node(
                    H2NodeType.VARIABLE,
                    opType=op_type,
                    variableName=addr_name)
                insn.sonsList[0] = new_addr
            if need_tmp:
                op_type = insn.opType
                var_name = "h2_%08d" % (self.call_counter)
                dest = H2Node(H2NodeType.VARIABLE,
                    variableName=var_name,
                    opType=op_type)
            else:
                dest = parent.sonsList[0]
            insn.variableName = dest.variableName
            insn.sonsList.insert(0, dest)
            new_insns.append(insn)
        elif insn.isW():
            addr = insn.sonsList[0]
            addr.opType = H2Type('int', 32, 1)
            self.visitInsn(addr, insn, new_insns)
            if addr.variableName is not None:
                op_type  = addr.opType
                addr_name = addr.variableName
                new_addr = H2Node(
                    H2NodeType.VARIABLE,
                    opType=op_type,
                    variableName=addr_name)
                insn.sonsList[0] = new_addr
            data:H2Node = insn.sonsList[1]
            if '[]' in insn.opType['arith']:
                data.opType = H2Type(
                    insn.opType['arith'][:-2],
                    insn.opType['wordLen'],
                    insn.opType['vectorLen'])
            self.visitInsn(data, insn, new_insns)
            if data.variableName is not None:
                op_type  = data.opType
                data_name = data.variableName
                new_data = H2Node(
                    H2NodeType.VARIABLE,
                    opType=op_type,
                    variableName=data_name)
                insn.sonsList[1] = new_data
            new_insns.append(insn)
        elif insn.isConst():
            var_name = "h2_%08d" % (self.call_counter)
            if insn.opType is None and str(insn.constValue).isnumeric():
                insn.opType = H2Type('int', 32, 1)
            op_type=insn.opType
            lhs = H2Node(H2NodeType.VARIABLE,
                variableName=var_name,
                opType=op_type)
            new_insn = H2Node(
                H2NodeType.OPERATOR,
                opName='=',
                opType=op_type,
                sonsList=[lhs, insn])
            insn.variableName = lhs.variableName
            new_insn.variableName = lhs.variableName
            new_insns.append(new_insn)
        elif insn.isVariable():
            return
        else:
            new_insns.append(insn)
        return
    def purge_redundant_mvs(self, IList: list):
        new_insns = list()
        insn: H2Node
        prev_insn:H2Node = None
        for idx, insn in enumerate(IList):
            if not (insn.isR() or insn.opName == '='):
                new_insns.append(insn)
                prev_insn = None
                continue
            curr_lhs:H2Node = insn.sonsList[0]
            #TODO: can someone explain to me why using h2_outputVarName
            # for R operations doesn't work ?????
            if curr_lhs.variableName == "h2_outputVarName":
                prev_insn = insn
                new_insns.append(insn)
            curr_rhs:H2Node = insn.sonsList[1]
            if prev_insn is None or insn.isR():
                prev_insn = insn
                new_insns.append(insn)
                continue
            prev_lhs:H2Node = prev_insn.sonsList[0]
            if prev_lhs.variableName == curr_rhs.variableName:
                prev_insn.sonsList[0] = curr_lhs
                prev_insn.variableName = curr_lhs.variableName
            else:
                prev_insn = insn
                new_insns.append(insn)
        return new_insns
    def rewriteInsn(self, insn:H2Node):
        new_insns = list()
        self.visitInsn(insn, None, new_insns)
        return new_insns
    def rewriteInsns(self, IList: list):
        # TODO: implement variable versionning
        new_insns = list()
        insn: H2Node
        for insn in IList:
            if insn.isRtn():
                continue
            new_insns += self.rewriteInsn(insn)
        #for idx, insn in enumerate(new_insns):
        #    print("%d:%s"%(idx, str(insn)))
        #foo()
        #new_insns = self.purge_redundant_mvs(new_insns)
        return new_insns + [H2Node(H2NodeType.RTN)]
