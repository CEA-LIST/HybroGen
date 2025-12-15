#!/usr/bin/env python3

class CCode():
    """C code generation which contains a compilette.
    for single operation regression tests
    """

    def __init__(self, op, arith, vLen, wLen, ctype, address=""):
        self.op = op
        self.arith = arith
        self.vLen = vLen
        self.wLen = wLen
        self.text = []
        self.add("// -*- c -*-")
        self.addIncludes(("stdio.h", "stdlib.h"))
        if vLen == '1':
            self.ctype = ctype
            self.add("/* C compilette prototype scalar version*/")
        else:
            self.ctype = "v%s_%s_%s_t" % (wLen, vLen, arith)
            self.add("/* C compilette prototype vector version*/")
            self.add("typedef %s %s __attribute__ ((vector_size (%s*sizeof (%s))));" %
                     (ctype, self.ctype, self.vLen, ctype))

    def getC(self):
        # print (self.text)
        return "\n".join(self.text)

    def write(self, fileName):
        # print ("write : %s"%fileName)
        f = open(fileName, "w")
        f.write(self.getC())
        f.close()

    def add(self, text):
        self.text.append(text)

    def addIncludes(self, includeList):
        for i in includeList:
            self.add("#include <%s>" % i)

    def addMain(self, arith, address=""):
        if arith == "int":
            arithLetter = "i"
            printLetter = "d"
        else:
            arithLetter = "f"
            printLetter = "f"
        main = ['int main(int argc, char * argv[])',
                '{',
                '  functionPointer fPtr;',
                '  int i, returnValue;',
                '  if (argc < %d)' % (2*int(self.vLen)),
                '    {',
                '      printf("Give %d values\\n");' % (2*int(self.vLen)),
                '      exit(-1);',
                '   }',
                '  {ctype} in0, in1, res;'.format(ctype=self.ctype, vLen=self.vLen),
                '  for (int i = 0; i < %s; i++)' % (self.vLen),
                '  {',
                '      in0 = ato%s (argv[1]); ' % (arithLetter) if self.vLen == '1' and address == '' else '  in0[i]  = ato%s (argv[1+i]);' % (arithLetter),
                '      in1 = ato%s (argv[1]); ' % (arithLetter) if self.vLen == '1' and address == '' else '  in1[i]  = ato%s (argv[1+%s+i]);' % (arithLetter, self.vLen),
                '  }',
                '  fPtr  = h2_malloc (1024);',
                '  fPtr = (functionPointer) genSingleOp(fPtr);',
                '  fPtr(&in0, &in1, &res);' if address == "&" else '  res = fPtr(in0, in1);',
                '  printf ("Simple operation on 2 variables (wordLen: %s, vectorLen %s):\\n");' % (self.wLen, self.vLen),
                '  returnValue = 0;',
                '  for (i= 0; i < {vLen}; i++)'.format(vLen=self.vLen),
                '     {',
                '       printf("%{letter} {op} %{letter} = %{letter}\\n", in0, in1, res);'.format(letter=printLetter, op=self.op) if self.vLen == '1' and address == '' else 'printf("%{letter} {op} %{letter} = %{letter}\\n", in0[i], in1[i], res[i]);'.format(letter=printLetter, op=self.op),
                '       if (res != (in0 {op} in1))'.format(op=self.op) if self.vLen == '1' and address == '' else 'if (res[i] != (in0[i] {op} in1[i]))'.format(op=self.op),
                '	    returnValue = -1;',
                '     }',
                '  return returnValue;',
                '}',]
        for line in main:
            self.add(line)

class CCodeAddress(CCode):
    """C code generation which contains a compilette.

    This compilette will generate a binary function containint
    a single instructrution.

    Arguments are passed by address (for add arch + CxRAM)
    """

    def __init__(self, op, arith, vLen, wLen, ctype):
        super().__init__(op, arith, vLen, wLen, ctype, "Address")
        self.addTypeDef()
        self.addCompilette()
        self.addMain(arith, address="&")

    def addTypeDef(self):
        typeDef = 'typedef void (*functionPointer)({arith}*, {arith}*,  {arith}*);'.format(
            arith=self.ctype)
        self.add(typeDef)

    def addCompilette(self):
        proto = "functionPointer genSingleOp(functionPointer ptr) /* C compilette prototype */\n{\n"
        head = "int 32 1 compilette({arith}[] {wLen} {vLen} a, {arith}[] {wLen} {vLen} b, {arith}[] {wLen} {vLen} r)".format(
            arith=self.arith, vLen=self.vLen, wLen=self.wLen, op=self.op, ctype=self.ctype)

        code = "\n\tr[0] = a[0] {op} b[0];\n\treturn 1;\n".format(
            arith=self.arith, vLen=self.vLen, wLen=self.wLen, op=self.op)
        self.add(proto)
        self.add("#[")
        self.add(head)
        self.add('{'+code+'}')
        self.add("]#")
        self.add("\treturn ptr;\n}")


class CCodeValue(CCode):
    """C code generation which contains a compilette.

    This compilette will generate a binary function containint
    a single instructrution.

    Arguments are passed by value (for all arch exept CxRAM)
    """

    def __init__(self, op, arith, vLen, wLen, ctype):
        super().__init__(op, arith, vLen, wLen, ctype)
        self.addTypeDef()
        self.addCompilette()
        self.addMain(arith)

    def addTypeDef(self):
        typeDef = 'typedef {arith} (*functionPointer)({arith}, {arith});'.format(
            arith=self.ctype)
        self.add(typeDef)

    def addCompilette(self):
        proto = "functionPointer genSingleOp(h2_insn_t * ptr) /* C compilette prototype */\n{\n"
        head = "{arith} {wLen} {vLen} compilette({arith} {wLen} {vLen} a, {arith} {wLen} {vLen} b)".format(
            arith=self.arith, vLen=self.vLen, wLen=self.wLen, op=self.op, ctype=self.ctype)

        code = "\n\t{arith} {wLen} {vLen} r;\n\tr = a {op} b;\n\treturn r;\n".format(
            arith=self.arith, vLen=self.vLen, wLen=self.wLen, op=self.op)
        self.add(proto)
        self.add("#[")
        self.add(head)
        self.add('{'+code+'}')
        self.add("]#")
        self.add("\treturn (functionPointer) ptr;\n}")


if __name__ == "__main__":
    import sys
    import subprocess
    import argparse

    opArith = {"add": "+", "mul": "*", "sub": "-", "div": "/"}
    opLogic = {"mod": "%", "or": "|", "xor": "^", "and": "&"}
    CTypeArray = {
        'int': {8: 'int8_t', 16: 'int16_t', 32: 'int32_t', 64: 'int64_t', },
        'flt': {32: 'float', 64: 'double', },
    }

    wLen = 32
    vLen = 1
    operation = "add"
    dataType = "flt"

    c = CCodeAddress(opArith[operation], dataType,
                     vLen, wLen, CTypeArray[dataType][wLen])
    fileName = "Test-%s-%s-%s-%s" % (operation, vLen, wLen, 1)
    c.write(fileName+".hl")
    print("../HybroLang.py -a power -i %s.hl -c" % (fileName))
    print("powerpc64le-linux-gnu-gcc -o %s %s.c" % (fileName, fileName))
    print("qemu-ppc64le %s 39 3" % fileName)
