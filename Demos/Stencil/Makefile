EXPPARAM =--input_file Image/Sun.pgm --program Stencil.${ARCH} --runner	\
	${RUNNER} --logFile `date +"%Y-%m-%d"`_Result_Stencil_${ARCH}.log

FILELIST=Makefile Stencil.c StencilExperiment.py		\
	Image/Sun.pgm_* Image/Sun.pgm ReadPgmImage.c	\
	ReadPgmImage.h Filter/*

CFLAGS=-g -DH2_DEBUG
CFLAGS=-O3 -Wall  -Wno-unused-variable

all:
	echo "make allAarch64 or make allRiscV"

resizeImages:
	make resize  ARCH=aarch64 RUNNER=qemu-aarch64

allAarch64:
	make build   ARCH=aarch64
	make compile ARCH=aarch64 CC=aarch64-linux-gnu-gcc
	make run     ARCH=aarch64 RUNNER=qemu-aarch64

allRiscV:
	make build   ARCH=riscv
	make compile ARCH=riscv CC=riscv32-linux-gnu-gcc
	make run 	 ARCH=riscv RUNNER=qemu-riscv32

exec:
	make compile CC=cc
	make run RUNNER=x

resize:
	./StencilExperiment.py ${EXPPARAM} --resize

run:
	-rm Result_Stencil_${ARCH}.log
	./StencilExperiment.py ${EXPPARAM} --filter_file Filter/Blur-3x3.pgm 			--param 9
	./StencilExperiment.py ${EXPPARAM} --filter_file Filter/GaussianFilter-3x3.pgm 	--param 16
	./StencilExperiment.py ${EXPPARAM} --filter_file Filter/Synthetic-3x3.pgm		--param 39
	./StencilExperiment.py ${EXPPARAM} --filter_file Filter/Null-5x5.pgm 			--param 1
	./StencilExperiment.py ${EXPPARAM} --filter_file Filter/Id-5x5.pgm 				--param 1
	./StencilExperiment.py ${EXPPARAM} --filter_file Filter/GaussianFilter-5x5.pgm 	--param 256
	./StencilExperiment.py ${EXPPARAM} --filter_file Filter/Synthetic-5x5.pgm		--param 352

plot:
	./generatePlot.py --archi ${ARCH} --output ${ARCH}

build: Stencil.hl
	../../HybroLang.py -a ${ARCH} -c -i ./Stencil.hl

compile: Stencil.c
	${CC} ${CFLAGS} ./Stencil.c ./ReadPgmImage.c -o ./Stencil.${ARCH}

send:
	tar cvf /tmp/a.tgz ${FILELIST}
	scp /tmp/a.tgz ${DEST}:/tmp

clean:
	-rm Stencil Stencil.riscv Stencil.aarch64 Stencil.c a.out Image/Sun.pgm_*
