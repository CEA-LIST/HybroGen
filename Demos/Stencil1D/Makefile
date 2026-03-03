H2FLAGS= -g
CFLAGS =-Wall -O0 -g -DH2_DEBUG_REGISTER -DH2_DEBUG_INSN
CFLAGS =-Wall -O0 -g # -DH2_DEBUG_REGISTER -DH2_DEBUG_INSN
# CFLAGS =-Wall -O3 # -DH2_DEBUG_REGISTER  -DH2_DEBUG_INSN
FILE = stencil_1d_mk2

all:
	echo "which target ? make [power|aarch64|riscv]"

power:
	make compileAndRun ARCH=power CC=powerpc64le-linux-gnu-gcc QEMU=qemu-ppc64le

aarch64:
	make compileAndRun ARCH=aarch64 CC=aarch64-linux-gnu-gcc QEMU=qemu-aarch64

riscv:
	make compileAndRun ARCH=riscv CC=riscv32-linux-gnu-gcc QEMU=qemu-riscv32

compileAndRun:
	../../HybroLang.py -c -a ${ARCH} -i ${FILE}.hl  ${H2FLAGS}
	cp ${FILE}.c ${FILE}.${ARCH}.c 
	${CC} -o ${FILE}.${ARCH} ${FILE}.${ARCH}.c ${CFLAGS}
	make run QEMU=${QEMU} CODE=${FILE}.${ARCH}

run: # <Array Len> <convolution value #1> <value #2> <value #3>
	@echo "# 7 7 7 : regular value, no optimization"
	${QEMU} ${CODE} 10 7 7 7 
	@echo "# 1 1 1 : use mv instead of mul"
	${QEMU} ${CODE} 10 1 1 1
	@echo "# 8 8 8 : use shift instead of mul"
	${QEMU} ${CODE} 10 8 8 8
	@echo "# Null convolution : should return 0 vector"
	${QEMU} ${CODE} 10 0 0 0 
	@echo "# Id convolution : should return same values"
	${QEMU} ${CODE} 10 0 1 0 

clean:
	-rm ${FILE}.*.c ${FILE}.riscv ${FILE}.aarch64 ${FILE}.power
