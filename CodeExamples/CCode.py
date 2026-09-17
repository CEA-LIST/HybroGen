#!/usr/bin/env python3

class CCode():
    """C code generation which contains a compilette.
    for single operation regression tests
    """

    def __init__(self, op, arith, vLen, wLen, ctype, address=""):
        # print (f"op : {op}, arith : {arith}, vlen : {vLen}, wLen : {wLen}")
        self.op = op
        self.arith = arith
        self.vLen = vLen
        self.wLen = wLen
        self.text = []
        self.add("// -*- c -*-")
        self.addIncludes(("stdio.h", "stdlib.h"))
        if vLen == 1:
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

    def addMain(self, arith, address=None):

        d = {}
        if arith == "int":
            d['arithLetter'] = "i"
            d['printLetter'] = "d"
        else:
            d['arithLetter'] = "f"
            d['printLetter'] = "f"
        d['vLen2'] = 2*int(self.vLen) + 1
        d['vLen']  = self.vLen
        d['wLen']  = self.wLen
        d['ctype'] = self.ctype
        d['op'] = self.op
        if self.vLen > 1:
            d['in0indice'] = "[i]"
            d['in1indice'] = "[i]"
            d['in0argv']   = "1+i"
            d['in1argv']   = "1+i+%d"%self.vLen
        else:
            d['in0indice'] = ""
            d['in1indice'] = ""
            d['in0argv']   = "1"
            d['in1argv']   = "2"
        template = '''int main(int argc, char * argv[])

{{
  functionPointer fPtr;
  int returnValue;
  if (argc < {vLen2})
    {{
      printf("Give {vLen2} values\\n");
      exit(-1);
   }}
  {ctype} in0, in1, res;
  for (int i = 0; i < {vLen}; i++)
  {{
        in0{in0indice} = ato{arithLetter}(argv[{in0argv}]);
        in1{in1indice} = ato{arithLetter}(argv[{in1argv}]);
  }}
  fPtr  = h2_malloc (1024);
  fPtr = (functionPointer) genSingleOp(fPtr);
  res = fPtr(in0, in1);
  printf ("Simple operation on 2 variables (wordLen: {wLen}, vectorLen {vLen}):\\n");
  returnValue = 0;
  for (int i = 0; i < {vLen}; i++)
  {{
       printf ("%{printLetter} {op} %{printLetter} = %{printLetter}\\n", in0{in0indice}, in1{in0indice}, res{in0indice});
       if (res{in0indice} != in0{in0indice} {op} in1{in0indice})
        returnValue = -1;
  }}
  return returnValue;
}}'''
        self.add(template.format(**d))

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
