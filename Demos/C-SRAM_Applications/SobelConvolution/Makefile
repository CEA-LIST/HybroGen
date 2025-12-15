H2_ROOT=../../../
H2=$(H2_ROOT)/HybroLang.py
H2FLAGS=-a csram-v2.0 --toC -g -v

CC=riscv32-unknown-linux-gnu-gcc
CFLAGS= -Wall -I$(H2_ROOT)/HybroGen/include -O3 -static
CFLAGS_DEBUG=$(CFLAGS) -D DEBUG

ISS=qim --run

all: SobelConvolution_scalar.x SobelConvolution_cxram.x

%.c: %.hl
	rm -f $@
	$(H2) $(H2FLAGS) -i $<

csram_base.h:
	qim --gen-macros .

SobelConvolution_scalar.x : main.c csram_base.h Makefile
	$(CC) $(CFLAGS_DEBUG) -o $@ $< -lm

SobelConvolution_cxram.x : main.c csram_base.h Makefile
	$(CC) -D H2_CXRAM $(CFLAGS_DEBUG) -o $@ $< -lm

clean:
	rm -f *.x *.c *.pgm *.csv *.mem csram_*.h
