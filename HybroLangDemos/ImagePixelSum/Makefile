CC = gcc
CC = riscv32-unknown-linux-gcc

FILE=CxRAM-ImagePixelAccumulation

all: build

build:
	../../HybroLang.py -c -a cxram -i ${FILE}.hl
	${CC} -c ReadPgmImage.c -Wall
	${CC} -o ${FILE} ${FILE}.c ReadPgmImage.o -Wall

small: build
	qemu-riscv32 ${FILE} MonOeilGris.pgm
big: build
	qemu-riscv32 ${FILE} FusionofHelios4kDesktop.pgm
medium: build
	qemu-riscv32 ${FILE} valve.pgm

debug:
	../../HybroLang.py -c -g -a cxram -i ${FILE}.hl
	${CC} -o  ${FILE}  ${FILE}.c -Wall -DH2_DEBUG -g
	qemu-riscv32 -g 5555 ${FILE} MonOeilGris.pgm

connect:
	riscv32-unknown-linux-gdb ${FILE}

clean:
	-rm -f ${FILE} ${FILE}.c
