FILELIST=Makefile Stencil.aarch64.c Stencil.riscv.c						\
	StencilExperiment.py Image/Sun*.pgm ReadPgmImage.c ReadPgmImage.h	\
	Filter/*
# CFLAGS=-O3 # -DVERBOSE # -g # -DH2_DEBUG -DVERBOSE -DH2_DEBUG_REGISTER
CFLAGS=-g -O1 -DVERBOSE -Wall -Wno-unused-variable  -DH2_DEBUG # -DH2_DEBUG_REGISTER
HLFLAGS=-g

all:
	echo "make allAarch64Qemu or make allAarch64Native"

exec:
	make compile CC=cc
	make run RUNNER=x

resize:
	./StencilExperiment.py ${EXPPARAM} --resize

# Do one experiment
riscv:
	make build   ARCH=riscv
	make compile ARCH=riscv CC=riscv32-linux-gnu-gcc
#	qemu-riscv32 Stencil.riscv Image/Sun_11x9.pgm S.pgm H4.pgm Filter/Id-1x1.pgm
	qemu-riscv32 

aarch64:
	make build   ARCH=aarch64
	make compile ARCH=aarch64 CC=aarch64-linux-gnu-gcc
	qemu-aarch64 Stencil.aarch64 Image/Sun_11x9.pgm S.pgm H4.pgm Filter/GaussianFilter-5x5.pgm

resizeImages:
	make resize  ARCH=aarch64 RUNNER=qemu-aarch64


# Do all experiments on aarch64 or riscv / qemu or native
allAarch64Qemu:
	make build   ARCH=aarch64
	make compile ARCH=aarch64 CC=aarch64-linux-gnu-gcc
	make runAll	 ARCH=aarch64 RUNNER=qemu-aarch64 LOG=aarch-qemu-`date +"%Y-%m-%d-%H-%M-%S"`.log

allAarch64Native:
	make compile ARCH=aarch64 CC=cc
	make runAll  ARCH=aarch64 RUNNER= LOG=aarch-native-`date +"%Y-%m-%d-%H-%M-%S"`.log

allRiscvQemu:
	make build   ARCH=riscv
	make compile ARCH=riscv CC=riscv32-linux-gnu-gcc
	make runAll	 ARCH=riscv RUNNER=qemu-riscv32 LOG=riscv-qemu-`date +"%Y-%m-%d-%H-%M-%S"`.log

allRiscvNative:
	make compile ARCH=riscv CC=cc
	make runAll  ARCH=riscv RUNNER= LOG=riscv-native-`date +"%Y-%m-%d-%H-%M-%S"`.log


# Run on various filters
runAll:
	-rm -f ${LOG}
	echo "# ${LOG} CFLAGS = ${CFLAGS} HLFLAFS = ${HLFLAGS}" > ${LOG}
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
	${CC} ${CFLAGS} ./Stencil.${ARCH}.c ./ReadPgmImage.c -o ./Stencil.${ARCH} -g

send:
	-tar cvf /tmp/a.tgz ${FILELIST}
	scp /tmp/a.tgz ${DEST}:/tmp

clean:
	-rm Stencil Stencil.riscv Stencil.aarch64 Stencil.c Stencil.*.c a.out 


