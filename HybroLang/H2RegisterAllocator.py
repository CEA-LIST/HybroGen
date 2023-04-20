import sys
from HybroLang.H2SymbolTable import H2SymbolTable
from HybroLang.H2RegisterBank import H2RegisterBank
from HybroLang.H2Node import H2Node
from HybroLang.H2IR2 import H2Type
from HybroLang.H2NodeType import H2NodeType

class H2RegisterAllocator:
    """
    "Unspilled linear scan" register allocator
    --- Kevin Mambu, CEA Grenoble
    """
    def __init__(self, archName: str, sTable: H2SymbolTable, regTmp:H2RegisterBank, verbose=False):
        self.archName            = archName
        self.verbose             = verbose
        self.sTable              = sTable
        self.regTmp              = regTmp
        self.scan_bounds         = dict()
        self.ariths              = dict()
        self.arg_registers       = self.sTable.symbolTable.keys()
        self.allocated_regs      = dict()

    def linear_scan(self, IList: list):
        insn: H2Node
        for idx, insn in enumerate(IList):
            if insn.isRtn():
                continue
            if insn.isB() or insn.isBcc() or insn.isLabel():
                continue
            insn_name = insn.variableName
            if insn.isOperatorOrMem():
                if insn.variableName is not None:
                    self.scan_bounds.setdefault(insn_name, [idx,idx])
                    self.ariths[insn_name] = insn.getOpType()
                    self.scan_bounds[insn_name][1] = idx
            child: H2Node
            for child in insn.sonsList:
                child_name:str = child.variableName
                if child_name is None:
                    continue
                self.scan_bounds.setdefault(child_name, [idx,idx])
                self.ariths[child_name] = child.opType
                self.scan_bounds[child_name][1] = idx
                gchild: H2Node
                for gchild in child.sonsList:
                    gchild_name:str = gchild.variableName
                    if gchild_name is None:
                        continue
                    self.scan_bounds.setdefault(gchild_name, [idx,idx])
                    self.ariths[gchild_name] = gchild.opType
                    self.scan_bounds[gchild_name][1] = idx
    def alloc_registers(self, IList: list):
        bounds_of_allocated = dict()
        allocated_regs      = dict()
        for var_name, bounds in self.scan_bounds.items():
            # We skip argument variables and special variables
            if var_name in self.arg_registers:
                continue
            arith = self.ariths[var_name]['arith']
            if not len(bounds_of_allocated):
                regNo = self.regTmp.getNextRegister(arith)
                bounds_of_allocated[var_name] = bounds
                allocated_regs.setdefault(regNo, []).append(var_name)
                continue
            regNo = None
            candidates = list()
            # we check for each reg if its owner variables have
            # no conflicting bounds with the current variable
            for reg, others in allocated_regs.items():
                is_reg_free = True
                for other in others:
                    other_bounds = bounds_of_allocated[other]
                    if not ((bounds[0] >= other_bounds[1])
                        or  (bounds[1] <= other_bounds[0])):
                        is_reg_free = False
                        break
                if is_reg_free:
                    regNo = reg
                    break
            # if no already attributed register was usable within
            # the bounds of the variable, we allocate a new register
            if regNo is None:
                regNo = self.regTmp.getNextRegister(arith)
            self.sTable.setRegister(var_name, regNo)
            allocated_regs.setdefault(regNo, []).append(var_name)
            bounds_of_allocated[var_name] = bounds
        # with all variables attributed to a register, we update the
        # symbol table appropriately
        for reg, variables in allocated_regs.items():
            for var in variables:
                opType = self.ariths[var]
                self.sTable.add(var, opType, reg)
        self.allocated_regs = allocated_regs
    def rewriteInsns(self, IList: list):
        self.linear_scan(IList)
        # print("Linear scan bounds:")
        # for var, bounds in self.scan_bounds.items():
        #     print("%s: %s"%(var, str(bounds)))
        self.alloc_registers(IList)
        # print("Register allocation results:")
        # for reg, variables in self.allocated_regs.items():
        #     print("Register #%d"%reg)
        #     for var in variables:
        #         print("- %s"%var)
        return IList
