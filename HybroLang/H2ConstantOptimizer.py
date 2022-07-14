#!/usr/bin/env python3

import sys
from collections import OrderedDict
from HybroLang.H2SymbolTable import H2SymbolTable
from HybroLang.H2RegisterBank import H2RegisterBank
from HybroLang.H2Node import H2Node
from HybroLang.H2IR2 import H2Type
from HybroLang.H2NodeType import H2NodeType

# TODO : support floating-point
# ( this is *not* gonna be easy... (^_^;) )

class H2ConstantOptimizer:
    """
    The H2ConstantOptimizer sweeps through the IR tree and performs
    transformations to optimize constants
    --- Kevin Mambu, CEA Grenoble
    """
    # TODO : use H2Node.sem to refactor the code
    sem = {"ADD":"+","+":"+","SUB":"-","-":"-","MUL":"*","*":"*","DIV":"/","/":"/",
            "SL":"<<","<<":"<<","SR":">>",">>":">>","AND":"&","OR":"|"}

    # Integer ranges *must* be declared using OrderedDict Objects to preserve the
    # order of the encoding fields. This is used in archOptimize() to break down
    # constant delcarations into instruction sequences using an iterative loop
    # 'None' Object is used if no speicifc instruction different than MV is
    # required for a specific field of an integer range

    # TODO : support larger integer ranges (64-bit / 128-bit)
    # for now only 32-bit integer ranges are considered
    integer_ranges = {
        "riscv": OrderedDict({20: "LUI", 12: None})
    }

    def print(self, s):
        if self.verbose:
            print("[H2ConstantOptimizer] %s" % s)

    def __init__(self, archName: str, verbose=False):
        self.archName = archName
        self.verbose = verbose
        self.optiOK = archName in H2ConstantOptimizer.integer_ranges.keys()
        if not self.optiOK:
            self.print("!!! Warning !!! Integer ranges not defined for architecture %s" % archName)

    def computeConstants(self, insn: H2Node):
        """
        Visits the IR Tree and pre-computes every constant expression
        """
        if insn.isOperatorOrMem():
            for idx, child in enumerate(insn.sonsList):
                insn.sonsList[idx] = self.computeConstants(child)
            # TODO : properly implement LUI
            # TODO : precompute expression with only 1 son like inv
            if insn.isMem() or insn.opName == "LUI" or insn.opName == "INV" or insn.opName == "NEG":
                return insn
            lhs: H2Node = insn.sonsList[0]
            rhs: H2Node = insn.sonsList[1]
            is_lhs_const = lhs.isConst() if lhs is not None else False
            is_rhs_const = rhs.isConst() if rhs is not None else False
            if not (insn.isOperator() and is_lhs_const and is_rhs_const):
                return insn
            op  = H2ConstantOptimizer.sem[insn.getOpName()]
            try:
                lhs_val = int(eval(lhs.getConstValue()))
                rhs_val = int(eval(rhs.getConstValue()))
            except TypeError as ex:
                # The operation depends on run-time constants, we cannot
                # optimize that
                return insn
            val = eval("lhs_val %s rhs_val" % op)
            newNode = H2Node(H2NodeType.CONST, constValue=val)
            return newNode
        else:
            return insn

    def archOptimize(self, insn:H2Node):
        """
        Visits the IR tree and breaks down constants into architecture-specific
        instruction sequences (similar to 'Load Integer' pseudo-instructions
        in standard compilers. The hints to perform optimizations are stored
        in the 'integer_ranges' dict Object
        """
        # Arch-specific variables to select instructions
        archName = self.archName
        integer_range = self.integer_ranges[archName]
        # Recursion tree
        if insn.isOperatorOrMem():
            for idx, child in enumerate(insn.sonsList):
                insn.sonsList[idx] = self.archOptimize(child)
            return insn
        elif insn.isConst():
            try:
                lsb = int(str(insn.getConstValue()), 0)
            except ValueError as ex:
                # The constant is a run-time constant, we cannot
                # optimize that
                return insn
            new_insn = None
            # Break-down from Least Sufficient Bits to Most Suffient Bits
            for length, opName in reversed(integer_range.items()):
                mask = int('1' * length, 2)
                msb = lsb >> length
                lsb = lsb &  mask
                if lsb == 0:
                    lsb = msb
                    continue
                if opName is None:
                    LSBNode = H2Node(H2NodeType.CONST, constValue=lsb)
                    # RISC-V sign-extends every immediate operation, so we need to
                    # squash the sign extension
                    is_lsb_negative = (lsb >> (length - 1))
                    if is_lsb_negative and self.archName == "riscv":
                        c20 = H2Node(H2NodeType.CONST, constValue=20)
                        sl = H2Node(H2NodeType.OPERATOR, sonsList=[LSBNode, c20], opName="SL")
                        sr = H2Node(H2NodeType.OPERATOR, sonsList=[sl, c20], opName="SR")
                        LSBNode = sr
                else:
                    constNode = H2Node(H2NodeType.CONST, constValue=lsb)
                    LSBNode = H2Node(H2NodeType.OPERATOR, sonsList=[constNode], opName=opName)
                if new_insn is None:
                    # we initialize new_insn
                    new_insn = LSBNode
                else:
                    # we OR new_insn with the current lsb
                    new_insn = H2Node(H2NodeType.OPERATOR, sonsList=[new_insn, LSBNode], opName="OR")
                lsb = msb
            if new_insn is None:
                # Result is analog to zero
                new_insn = H2Node(H2NodeType.CONST, constValue=0)
            return new_insn
        else:
            return insn

    def rewriteInsn(self, insn: H2Node):
        self.print("Pre-computing constants")
        new_insn = self.computeConstants(insn)
        self.print("Result:\n%s" % str(new_insn))
        if self.optiOK:
            self.print("Optimizing constant initialization for architecture '%s'..." % self.archName)
            new_insn = self.archOptimize(new_insn)
            self.print("Result:\n%s" % str(new_insn))
        return [new_insn]
