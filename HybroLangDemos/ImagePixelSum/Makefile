.SUFFIXES : .hl

CC = gcc
CC = riscv32-unknown-linux-gcc
FILE=CxRAM-ImagePixelAccumulation
OBJS=ReadPgmImage.o ${FILE}.o
CFLAGS=-Wall -DH2_DEBUG -g -DQEMU_TARGET
.hl.c:
	../../HybroLang.py -c -a cxram -i $<

all: build

build: ${OBJS}
	${CC} -o ${FILE} ${OBJS} ${CFLAGS}

small: build
	qemu-riscv32 ${FILE} MonOeilGris.pgm

big: build
	qemu-riscv32 ${FILE} FusionofHelios4kDesktop.pgm

medium: build
	qemu-riscv32 ${FILE} valve.pgm

debug: ${OBJS}
	${CC} -o ${FILE} ${OBJS} -Wall -DH2_DEBUG -g
	qemu-riscv32 -g 5555 ${FILE} MonOeilGris.pgm

connect:
	riscv32-unknown-linux-gdb ${FILE}

clean:
	-rm -f ${FILE} ${FILE}.c ${OBJS}
