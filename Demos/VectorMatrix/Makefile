HLFLAGS= -g
CFLAGS =-Wall -O0 -g # -DH2_DEBUG_INSN # -DH2_DEBUG_REGISTER
CFLAGS =-Wall -O3 # -DH2_DEBUG_REGISTER  -DH2_DEBUG_INSN
FILE = VectorMatrix
# HLFLAGS=-g
all:
	@echo "make riscv"
	@echo "make aarch64"
	@echo "make power"

power:
	make build   ARCH=$@
	make compile ARCH=$@ CC=powerpc64le-linux-gnu-gcc
	make run     ARCH=$@ QEMU=qemu-ppc64le CODE=${FILE}

aarch64:
	make build   ARCH=$@
	make compile ARCH=$@ CC=aarch64-linux-gnu-gcc
	make run     ARCH=$@ QEMU=qemu-aarch64 CODE=${FILE}

riscv:
	make build   ARCH=$@
	make compile ARCH=$@ CC=riscv32-linux-gnu-gcc
	make run     ARCH=$@ QEMU=qemu-riscv32 CODE=${FILE}

build:
	../../HybroLang.py ${HLFLAGS} -a ${ARCH} -c -i ./VectorMatrix.hl
	mv VectorMatrix.c VectorMatrix.${ARCH}.c

compile: VectorMatrix.${ARCH}.c
	${CC} ${CFLAGS} ./VectorMatrix.${ARCH}.c -o ./VectorMatrix.${ARCH}

run:
	${QEMU} ${CODE}.${ARCH} Null      0  0  0  0   0  0  0  0   0  0  0  0   0  0  0  0
	${QEMU} ${CODE}.${ARCH} Id        1  0  0  0   0  1  0  0   0  0  1  0   0  0  0  1
	${QEMU} ${CODE}.${ARCH} Translate 1  0  0  4   0  1  0  5   0  0  1  6   0  0  0  1
	${QEMU} ${CODE}.${ARCH} Tran+Scal 4  0  0  4   0  5  0  5   0  0  6  6   0  0  0  1
	${QEMU} ${CODE}.${ARCH} General   4  2  3  4   5  6  7  8   9 10 11 12  13 14 15 16

clean:
	-rm ${FILE}.c ${FILE}
	-rm ${FILE}.aarch64.c ${FILE}.aarch64
	-rm ${FILE}.power.c   ${FILE}.power
	-rm ${FILE}.riscv.c   ${FILE}.riscv
