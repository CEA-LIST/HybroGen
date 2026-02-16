FILELIST=Makefile Stencil.aarch64.c Stencil.riscv.c						\
	StencilExperiment.py Image/Sun*.pgm ReadPgmImage.c ReadPgmImage.h	\
	Filter/*
CFLAGS=-O3 # -DVERBOSE  -g  -DH2_DEBUG_REGISTER
# CFLAGS= -DH2_DEBUG_REGISTER -g -O0 -Wall -Wno-unused-variable # -DVERBOSE -DH2_DEBUG  -DH2_DEBUG_INSN # -DH2_DEBUG_REGISTER
# -g With instruction selector as functions instead of macro
# -z Visual tree
# HLFLAGS= -g

all:
	@echo "make allAarch64Qemu"
	@echo "make allAarch64Native"
	@echo "make allRiscvQemu"
	@echo "make allRiscvNative"
	@echo "make allPowerQemu"
exec:
	make compile CC=cc
	make run RUNNER=x

resize:
	./StencilExperiment.py ${EXPPARAM} --resize

resizeImages:
	make resize  ARCH=aarch64 RUNNER=qemu-aarch64

# Do one experiment
riscv:
	make build   ARCH=riscv
	make compile ARCH=riscv CC=riscv32-linux-gnu-gcc
#	qemu-riscv32 Stencil.riscv Image/Sun_11x9.pgm S.pgm H4.pgm Filter/Id-3x3.pgm
	qemu-riscv32 Stencil.riscv Image/Sun_11x9.pgm S.pgm H4.pgm Filter/GaussianFilter-5x5.pgm

aarch64:
	make build   ARCH=aarch64
	make compile ARCH=aarch64 CC=aarch64-linux-gnu-gcc
	qemu-aarch64 Stencil.aarch64 Image/Sun_11x9.pgm S.pgm H4.pgm Filter/Id-3x3.pgm

power:
	make build   ARCH=power
	make compile ARCH=power CC=powerpc64le-linux-gnu-gcc
	qemu-ppc64le Stencil.power Image/Sun_11x9.pgm S.pgm H4.pgm Filter/GaussianFilter-5x5.pgm

# Do all experiments on aarch64 or riscv / qemu or native
allPowerQemu:
	make allQemu ARCH=power CC=powerpc64le-linux-gnu-gcc RUNNER=qemu-ppc64le LOG=power-qemu-`date +"%Y-%m-%d-%H-%M-%S"`.log

allAarch64Qemu:
	make allQemu ARCH=aarch64 CC=aarch64-linux-gnu-gcc RUNNER=qemu-aarch64 LOG=aarch-qemu-`date +"%Y-%m-%d-%H-%M-%S"`.log

allRiscvQemu:
	make allQemu ARCH=riscv CC=riscv32-linux-gnu-gcc RUNNER=qemu-riscv32 LOG=riscv-qemu-`date +"%Y-%m-%d-%H-%M-%S"`.log

allQemu:
	make build   ARCH=${ARCH}
	make compile ARCH=${ARCH} CC=${CC}
	make runAll	 ARCH=${ARCH} RUNNER=${RUNNER} LOG=${LOG}
	./InstructionCount.awk      ${LOG}
	./CyclesPerGeneratedInsn.awk ${LOG}

allAarch64Native:
	make allNative ARCH=aarch64 CC=cc RUNNER= LOG=aarch-native-`date +"%Y-%m-%d-%H-%M-%S"`.log

allRiscvNative:
	make allNative ARCH=riscv CC=cc RUNNER= LOG=riscv-native-`date +"%Y-%m-%d-%H-%M-%S"`.log

allNative:
	make compile ARCH=${ARCH} CC=${CC}
	make runAll	 ARCH=${ARCH} RUNNER=${RUNNER} LOG=${LOG}
	./InstructionCount.awk      ${LOG}
	./CyclesPerGeneratedInsn.awk ${LOG}

# Run on various filters
runAll:
	-rm -f ${LOG}
	echo "# ${LOG} CFLAGS = ${CFLAGS} HLFLAGS = ${HLFLAGS}" > ${LOG}
	make run ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=Filter/Null-3x3.pgm
	make run ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=Filter/Id-3x3.pgm
	make run ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=Filter/Blur-3x3.pgm
	make run ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=Filter/GaussianFilter-3x3.pgm
	make run ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=Filter/Synthetic-3x3.pgm

	make run ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=Filter/Null-5x5.pgm
	make run ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=Filter/Id-5x5.pgm
	make run ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=Filter/Blur-5x5.pgm
	make run ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=Filter/GaussianFilter-5x5.pgm
	make run ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=Filter/Synthetic-5x5.pgm
	echo "Results in ${LOG}"
# Then on various image sizes
run:
	-make xperiment ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=${FILTER} SIZE=320x240
	-make xperiment ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=${FILTER} SIZE=640x480
	-make xperiment ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=${FILTER} SIZE=800x600
	-make xperiment ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=${FILTER} SIZE=1024x768
	-make xperiment ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=${FILTER} SIZE=1280x960
	-make xperiment ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=${FILTER} SIZE=1600x1200
	-make xperiment ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=${FILTER} SIZE=2048x1536

xperiment:
	-${RUNNER} Stencil.${ARCH} Image/Sun_${SIZE}.pgm S.pgm H4.pgm ${FILTER} >> ${LOG}

plot:
	./generatePlot.py --archi ${ARCH} --output ${ARCH}

build: Stencil.hl
	../../HybroLang.py ${HLFLAGS} -a ${ARCH} -c -i ./Stencil.hl
	mv Stencil.c Stencil.${ARCH}.c

compile: Stencil.${ARCH}.c
	${CC} ${CFLAGS} ./Stencil.${ARCH}.c ./ReadPgmImage.c -o ./Stencil.${ARCH}

send:
	-tar cvf /tmp/a.tgz ${FILELIST}
	scp /tmp/a.tgz ${DEST}:/tmp

clean:
	-rm Stencil Stencil.riscv Stencil.aarch64 Stencil.c Stencil.*.c a.out
