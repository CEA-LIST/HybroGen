
class PGen:
    def __init__(self, isa):
        self.isa = isa
        
    def getInsn(self, semantic, arithmetic, datawidth, vectorlen):
        found = False
        for i in self.isa.insnlist:
            print (i)
            if i.check(semantic, arithmetic, datawidth, vectorlen):
                found = True
                break
        if found :
            print("Insn Found")
        else:
            print("Insn no Found")
    def execBin(self):
        return 0

    def wordIsHexa(self, w):
        if len(w) != 2:
            return False
        if w[0] not in "0123456789abcdef" :
            return False
        if w[1] not in "0123456789abcdef" :
            return False
        return True

    def GenOpWithConst(self, functionname, value, op, datatype):
        import os
        code = "{datatype} {functionname}({datatype} a){{return {value} {op} a;}}".format(functionname = functionname, value =value, op=op, datatype=datatype)
        f = open("/tmp/a.c", "w")
        f.write(code)
        f.close()
        os.system("gcc -c -O3 /tmp/a.c -o /tmp/a.o")
        os.system("objdump -d /tmp/a.o > /tmp/a.txt")
        f = open("/tmp/a.txt")
        a = f.readlines()
        f.close()
        ok = False
        buffer= ""
        for l in a:
            if ok:
                m = l.split() 
                for w in m[1:]:
                    if self.wordIsHexa(w):
                  #      buffer.append(int(w, 16))
                        print('add '+w)
                        buffer += chr(int(w, 16))
            if functionname in l:
                ok = True
        buffer += chr(0)
        return buffer
    #        return bytearray(buffer)

    def execBin(self, value, op, datatype):
        import ctypes

        buff = self.GenOpWithConst("thefunction", value, op, datatype)
        lenbuff = len(buff)
        print ("%d %s" %(lenbuff, str(type(buff))))
        l = ctypes.cdll.LoadLibrary("./ExecBuffer.so")
        b = ctypes.create_string_buffer(buff.encode("latin1"), lenbuff)
        l.setBuffer(b, lenbuff)
        print("Apres set")
        print(l.execBuffer(32))
        return False
