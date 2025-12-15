H2FLAGS= -g
CFLAGS =-Wall -O0 -g -DH2_DEBUG_REGISTER -DH2_DEBUG_INSN
CFLAGS =-Wall -O0 -g # -DH2_DEBUG_REGISTER -DH2_DEBUG_INSN
# CFLAGS =-Wall -O3 # -DH2_DEBUG_REGISTER  -DH2_DEBUG_INSN
FILE = VectorMatrix

all:
	echo "which tartet ? make [power|aarch64|riscv]"

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
	${QEMU} ${CODE} Null      0  0  0  0   0  0  0  0   0  0  0  0   0  0  0  0
	${QEMU} ${CODE} Id        1  0  0  0   0  1  0  0   0  0  1  0   0  0  0  1
	${QEMU} ${CODE} Translate 1  0  0  4   0  1  0  5   0  0  1  6   0  0  0  1
	${QEMU} ${CODE} Tran+Scal 4  0  0  4   0  5  0  5   0  0  6  6   0  0  0  1
	${QEMU} ${CODE} General   4  2  3  4   5  6  7  8   9 10 11 12  13 14 15 16

clean:
	-rm ${FILE}.c ${FILE}
