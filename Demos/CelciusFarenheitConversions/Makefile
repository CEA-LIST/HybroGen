CC = echo "Please define CC compiler"
FILE=CelciusFarenheitTable
CFLAGSDEBUG=-O3 -Wall -g -DH2_DEBUG 
CFLAGSOPT=-O3 -Wall

all:
	echo "Options are :"
	echo "make build-and-run-aarch64"
	echo "make build-and-run-power"
	echo "make build-and-run-riscv"

build-and-run-aarch64:
	${MAKE} build-and-run ARCH=aarch64 PREFIX=aarch64-linux-gnu QEMU-SUFFIX=aarch64 CFLAGS="${CFLAGSOPT}"

build-and-run-power:
	${MAKE} build-and-run ARCH=power  PREFIX=powerpc64le-linux-gnu QEMU-SUFFIX=ppc64le CFLAGS=${CFLAGSOPT}

build-and-run-riscv:
	${MAKE} build-and-run ARCH=riscv PREFIX=riscv32-unknown-elf QEMU-SUFFIX=riscv32 CFLAGS=${CFLAGSOPT}

build-and-run:
	../../HybroLang.py --toC --arch ${ARCH} --inputfile ${FILE}.hl -g
	${PREFIX}-gcc ${CFLAGS} -o ${FILE} ${FILE}.c -Wall
	qemu-${QEMU-SUFFIX} ${FILE}

debug-and-run-aarch64:
	${MAKE} debug ARCH=aarch64  PREFIX=aarch64-linux-gnu QEMU-SUFFIX=aarch64 CFLAGS="${CFLAGSDEBUG}"

debug-and-run-power:
	${MAKE} debug ARCH=power  PREFIX=powerpc64le-linux-gnu QEMU-SUFFIX=ppc64le CFLAGS="${CFLAGSDEBUG}"

debug:
	../../HybroLang.py --toC --arch ${ARCH} --inputfile ${FILE}.hl -g
	${PREFIX}-gcc -O3 ${CFLAGS} -o ${FILE} ${FILE}.c -Wall
	${PREFIX}-objdump -d ${FILE} > ${FILE}.d
	@echo "run " qemu-${QEMU-SUFFIX} -g 5555 ${FILE}
	@echo "set sysroot /opt/H2/aarch64/aarch64-linux-gnu/"
	@echo "target remote :5555"
	@echo "break main"
	${PREFIX}-gdb ${FILE}

clean:
	-rm -f ${FILE} ${FILE}.c
