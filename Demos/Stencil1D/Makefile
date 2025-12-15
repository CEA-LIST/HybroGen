H2FLAGS= -g
CFLAGS =-Wall -O0 -g -DH2_DEBUG_REGISTER -DH2_DEBUG_INSN
CFLAGS =-Wall -O0 -g # -DH2_DEBUG_REGISTER -DH2_DEBUG_INSN
# CFLAGS =-Wall -O3 # -DH2_DEBUG_REGISTER  -DH2_DEBUG_INSN
FILE = stencil_1d_mk2

all:
	echo "which target ? make [power|aarch64|riscv]"

power:
	../../HybroLang.py -c -a power -i ${FILE}.hl        ${H2FLAGS}
	powerpc64le-linux-gnu-gcc -o ${FILE} ${FILE}.c ${CFLAGS}
	make QEMU=qemu-ppc64le CODE=${FILE} run

aarch64:
	../../HybroLang.py -c -a aarch64 -i ${FILE}.hl  ${H2FLAGS}
	aarch64-linux-gnu-gcc -o ${FILE} ${FILE}.c ${CFLAGS}
	make QEMU=qemu-aarch64 CODE=${FILE} run

riscv:
	../../HybroLang.py -c -a riscv -i ${FILE}.hl  ${H2FLAGS}
	riscv32-linux-gnu-gcc -o ${FILE} ${FILE}.c ${CFLAGS}
	make QEMU=qemu-riscv32 CODE=${FILE} run

run:
	${QEMU} ${CODE} 10 1 1 1
	${QEMU} ${CODE} 10 7 7 7 
	${QEMU} ${CODE} 10 8 8 8
	${QEMU} ${CODE} 10 0 0 0 

clean:
	-rm ${FILE}.c ${FILE}
