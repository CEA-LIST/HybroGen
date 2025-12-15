H2_ROOT=../../../
H2=$(H2_ROOT)/HybroLang.py
H2FLAGS=-a csram-v2.0 --toC -g -v

CC=riscv32-unknown-linux-gnu-gcc
CFLAGS=-Wall -I$(H2_ROOT)/HybroGen/include -O3 -static
CFLAGS_DEBUG=$(CFLAGS) -D DEBUG

ISS=qim --run

.PRECIOUS : %.c %.o %.x 

all:

%.c: %.hl
	rm -f $@
	$(H2) $(H2FLAGS) -i $<
%.x : %.c
	$(CC) $(CFLAGS) -o $@ $<
%.csv %.mem %.log : %.x
	$(ISS) $< > $*.log

csram_base.h:
	qim --gen-macros .

clean:
	rm -f *.c *.o *.x *.pgm *.csv *.mem *.log csram_*.h
