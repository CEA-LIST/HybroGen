HLFLAGS= -g
CFLAGS =-Wall -O0 -g # -DH2_DEBUG_INSN # -DH2_DEBUG_REGISTER
CFLAGS =-Wall -O3 # -DH2_DEBUG_REGISTER  -DH2_DEBUG_INSN
FILE = VectorMatrix
FILELIST = VectorMatrix.aarch64.c VectorMatrix.riscv.c VectorMatrix.power.c Makefile
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
	make run     ARCH=$@ QEMU=qemu-aarch64 CODE=${FILE} REPEAT=10
	make run     ARCH=$@ QEMU=qemu-aarch64 CODE=${FILE} REPEAT=100
	make run     ARCH=$@ QEMU=qemu-aarch64 CODE=${FILE} REPEAT=1000
	make run     ARCH=$@ QEMU=qemu-aarch64 CODE=${FILE} REPEAT=10000
	make run     ARCH=$@ QEMU=qemu-aarch64 CODE=${FILE} REPEAT=100000
	make run     ARCH=$@ QEMU=qemu-aarch64 CODE=${FILE} REPEAT=1000000
	make run     ARCH=$@ QEMU=qemu-aarch64 CODE=${FILE} REPEAT=10000000
	make run     ARCH=$@ QEMU=qemu-aarch64 CODE=${FILE} REPEAT=100000000

riscv:
	make build   ARCH=$@
	make compile ARCH=$@ CC=riscv32-linux-gnu-gcc
	make run     ARCH=$@ QEMU=qemu-riscv32 CODE=${FILE}

build:
	../../HybroLang.py ${HLFLAGS} -a ${ARCH} -c -i ./VectorMatrix.hl
	mv VectorMatrix.c VectorMatrix.${ARCH}.c

compile: VectorMatrix.${ARCH}.c
	${CC} ${CFLAGS} ./VectorMatrix.${ARCH}.c -o ./VectorMatrix.${ARCH}


runAarch64Native:
	make allNative ARCH=aarch64 CC=cc CFLAGS=-O0 RUNNER= LOG=aarch-native-`date +"%Y-%m-%d-%H-%M-%S-O0"`.log
	make allNative ARCH=aarch64 CC=cc CFLAGS=-O3 RUNNER= LOG=aarch-native-`date +"%Y-%m-%d-%H-%M-%S-O3"`.log

allNative:
	make compile ARCH=${ARCH} CFLAGS=${CFLAGS} CC=${CC}
	make runAll	 ARCH=${ARCH} CFLAGS=${CFLAGS} RUNNER=${RUNNER} LOG=${LOG}

runAll:
	-rm -f ${LOG}
	echo "# ${LOG} CFLAGS = ${CFLAGS} HLFLAGS = ${HLFLAGS}" > ${LOG}
	make run  ARCH=${ARCH} CFLAGS=${CFLAGS} RUNNER=${RUNNER} REPEAT=10         >> ${LOG}
	make run  ARCH=${ARCH} CFLAGS=${CFLAGS} RUNNER=${RUNNER} REPEAT=100        >> ${LOG}
	make run  ARCH=${ARCH} CFLAGS=${CFLAGS} RUNNER=${RUNNER} REPEAT=1000       >> ${LOG}
	make run  ARCH=${ARCH} CFLAGS=${CFLAGS} RUNNER=${RUNNER} REPEAT=10000      >> ${LOG}
	make run  ARCH=${ARCH} CFLAGS=${CFLAGS} RUNNER=${RUNNER} REPEAT=100000     >> ${LOG}
	make run  ARCH=${ARCH} CFLAGS=${CFLAGS} RUNNER=${RUNNER} REPEAT=1000000    >> ${LOG}
#	make run  ARCH=${ARCH} CFLAGS=${CFLAGS} RUNNER=${RUNNER} REPEAT=10000000   >> ${LOG}
#	make run  ARCH=${ARCH} CFLAGS=${CFLAGS} RUNNER=${RUNNER} REPEAT=100000000  >> ${LOG}

run:
	${QEMU} ${FILE}.${ARCH} ${REPEAT} Null      0  0  0  0   0  0  0  0   0  0  0  0   0  0  0  0
	${QEMU} ${FILE}.${ARCH} ${REPEAT} Id        1  0  0  0   0  1  0  0   0  0  1  0   0  0  0  1
	${QEMU} ${FILE}.${ARCH} ${REPEAT} Translate 1  0  0  4   0  1  0  5   0  0  1  6   0  0  0  1
	${QEMU} ${FILE}.${ARCH} ${REPEAT} Tran+Scal 4  0  0  4   0  5  0  5   0  0  6  6   0  0  0  1
	${QEMU} ${FILE}.${ARCH} ${REPEAT} General   4  2  3  4   5  6  7  8   9 10 11 12  13 14 15 16

send:
	-tar cvf /tmp/a.tgz ${FILELIST}
	scp /tmp/a.tgz ${DEST}:/tmp

clean:
	-rm ${FILE}.c ${FILE}
	-rm ${FILE}.aarch64.c ${FILE}.aarch64
	-rm ${FILE}.power.c   ${FILE}.power
	-rm ${FILE}.riscv.c   ${FILE}.riscv
