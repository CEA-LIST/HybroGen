FILELIST=Makefile Stencil.aarch64.c Stencil.riscv.c						\
	StencilExperiment.py Image/Sun*.pgm ReadPgmImage.c ReadPgmImage.h	\
	Filter/* InstructionCount.awk CyclesPerGeneratedInsn.awk

# Performance & experimentations
# CFLAGS=-O3 # -DVERBOSE  -g  -DH2_DEBUG_REGISTER
HLFLAGS=

# Debuggage
# -g With instruction selector as functions instead of macro
# -z Visual tree
# HLFLAGS= -g
# CFLAGS=  -g -O0 -Wall -Wno-unused-variable -DVERBOSE -DH2_DEBUG  # -DH2_DEBUG_INSN # -DH2_DEBUG_REGISTER

all:
	@echo "make allAarch64Qemu"
	@echo "make allAarch64Native"
	@echo "make allRiscvQemu"
	@echo "make allRiscvNative"
	@echo "make allPowerQemu"


buildAll:
	make build ARCH=aarch64
	make build ARCH=riscv
	make build ARCH=power

exec:
	make compile CC=cc
	make run RUNNER=x

resizeAll:
	make resizeImage SIZE=2048x1536
	make resizeImage SIZE=1600x1200
	make resizeImage SIZE=1280x960
	make resizeImage SIZE=1024x768
	make resizeImage SIZE=800x600
	make resizeImage SIZE=640x480
	make resizeImage SIZE=320x240
	make resizeImage SIZE=11x9

resizeImage: # Works on ImageMagick > 7
	magick Image/Sun.pgm -resize $SIZE -compress none -colorspace Gray pgm:Image/Sun__${SIZE}.pg

# Do one experiment for ARCH which CC & emulation with QEMU
oneXperiment:
	make build   ARCH=${ARCH}
	make compile ARCH=${ARCH} CC=${CC}
	${QEMU} Stencil.${ARCH} Image/Sun_13x10.pgm S.pgm H4.pgm Filter/Null-3x3.pgm
	${QEMU} Stencil.${ARCH} Image/Sun_13x10.pgm S.pgm H4.pgm Filter/Id-3x3.pgm
	${QEMU} Stencil.${ARCH} Image/Sun_13x10.pgm S.pgm H4.pgm Filter/Blur-3x3.pgm
	${QEMU} Stencil.${ARCH} Image/Sun_13x10.pgm S.pgm H4.pgm Filter/GaussianFilter-3x3.pgm
	${QEMU} Stencil.${ARCH} Image/Sun_13x10.pgm S.pgm H4.pgm Filter/Synthetic-3x3.pgm

	${QEMU} Stencil.${ARCH} Image/Sun_13x10.pgm S.pgm H4.pgm Filter/Null-5x5.pgm
	${QEMU} Stencil.${ARCH} Image/Sun_13x10.pgm S.pgm H4.pgm Filter/Id-5x5.pgm
	${QEMU} Stencil.${ARCH} Image/Sun_13x10.pgm S.pgm H4.pgm Filter/Blur-5x5.pgm
	${QEMU} Stencil.${ARCH} Image/Sun_13x10.pgm S.pgm H4.pgm Filter/GaussianFilter-5x5.pgm
	${QEMU} Stencil.${ARCH} Image/Sun_13x10.pgm S.pgm H4.pgm Filter/Synthetic-5x5.pgm
riscv:
	make oneXperiment ARCH=riscv CC=riscv32-linux-gnu-gcc QEMU=qemu-riscv32

aarch64:
	make oneXperiment ARCH=aarch64 CC=aarch64-linux-gnu-gcc QEMU=qemu-aarch64

power:
	make oneXperiment ARCH=power CC=powerpc64le-linux-gnu-gcc QEMU=qemu-ppc64le

# Do all experiments for ARCH which CC & emulation with QEMU results in LOG file
allQemu:
	make build   ARCH=${ARCH}
	make compile ARCH=${ARCH} CC=${CC}
	make runAll	 ARCH=${ARCH} RUNNER=${RUNNER} LOG=${LOG}
	./InstructionCount.awk      ${LOG}
	./CyclesPerGeneratedInsn.awk ${LOG}

allpowerQemu:
	make allQemu ARCH=power CC=powerpc64le-linux-gnu-gcc RUNNER=qemu-ppc64le LOG=power-qemu-`date +"%Y-%m-%d-%H-%M-%S"`.log

allaarch64Qemu:
	make allQemu ARCH=aarch64 CC=aarch64-linux-gnu-gcc CFLAGS=-O0 RUNNER=qemu-aarch64 LOG=aarch-qemu-`date +"%Y-%m-%d-%H-%M-%S-O0"`.log
	make allQemu ARCH=aarch64 CC=aarch64-linux-gnu-gcc CFLAGS=-O3 RUNNER=qemu-aarch64 LOG=aarch-qemu-`date +"%Y-%m-%d-%H-%M-%S-O3"`.log

allriscvQemu:
	make allQemu ARCH=riscv CC=riscv32-linux-gnu-gcc RUNNER=qemu-riscv32 LOG=riscv-qemu-`date +"%Y-%m-%d-%H-%M-%S"`.log

# Do native experiment i.e. do only CC & run natively, log in LOG file
allaarch64Native:
	make allNative ARCH=aarch64 CC=cc CFLAGS=-O0 RUNNER= LOG=aarch-native-`date +"%Y-%m-%d-%H-%M-%S-O0"`.log
	make allNative ARCH=aarch64 CC=cc CFLAGS=-O3 RUNNER= LOG=aarch-native-`date +"%Y-%m-%d-%H-%M-%S-O3"`.log

allriscvNative:
	make allNative ARCH=riscv CC=cc RUNNER="" LOG=riscv-native-`date +"%Y-%m-%d-%H-%M-%S"`.log

allNative:
	make compile ARCH=${ARCH} CFLAGS=${CFLAGS} CC=${CC}
	make runAll	 ARCH=${ARCH} CFLAGS=${CFLAGS} RUNNER=${RUNNER} LOG=${LOG}
	./InstructionCount.awk      ${LOG}
	./CyclesPerGeneratedInsn.awk ${LOG}

runAll: # Run on various filters
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

run: # Then on various image sizes (image ratio 4:3)
	-make xperiment ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=${FILTER} SIZE=13x10
	-make xperiment ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=${FILTER} SIZE=160x120
	-make xperiment ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=${FILTER} SIZE=320x240
	-make xperiment ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=${FILTER} SIZE=640x480
	-make xperiment ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=${FILTER} SIZE=800x600
	-make xperiment ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=${FILTER} SIZE=1024x768
	-make xperiment ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=${FILTER} SIZE=1280x960
	# -make xperiment ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=${FILTER} SIZE=1600x1200
	# -make xperiment ARCH=${ARCH} LOG=${LOG} RUNNER=${RUNNER} FILTER=${FILTER} SIZE=2048x1536

xperiment:
	${RUNNER} ./Stencil.${ARCH} Image/Sun_${SIZE}.pgm S.pgm H4.pgm ${FILTER} >> ${LOG}

plot:
	./generatePlot.py --archi ${ARCH} --output ${ARCH}

build: Stencil.hl
	../../HybroLang.py ${HLFLAGS} -a ${ARCH} -c -i ./Stencil.hl

compile: Stencil.${ARCH}.c
	${CC} ${CFLAGS} ./Stencil.${ARCH}.c ./ReadPgmImage.c -o ./Stencil.${ARCH}

send:
	-tar cvf /tmp/a.tgz ${FILELIST}
	scp /tmp/a.tgz ${DEST}:/tmp

clean:
	-rm Stencil Stencil.riscv Stencil.aarch64 Stencil.power Stencil.c Stencil.*.c a.out