H2_ROOT=../../../
H2=$(H2_ROOT)/HybroLang.py
H2FLAGS=-a csram-v2.0 --toC -g

CC=riscv32-unknown-linux-gnu-gcc
CFLAGS=-Wall -I$(H2_ROOT)/HybroGen/include -O3 -static
CFLAGS_DEBUG=$(CFLAGS) -D DEBUG

ISS=qim --run

all: ImageDiff_c_riscv.x ImageDiff_c_cxram.x ImageDiff_h2_cxram.x 

%.c: %.hl
	rm -f $@
	$(H2) $(H2FLAGS) -i $<

csram_base.h:
	qim --gen-macros .

ImageDiff_c_riscv.x : main.c csram_base.h Makefile
	#$(CC) $(CFLAGS_DEBUG) -o $@ $^
	$(CC) $(CFLAGS) -o $@ $<

ImageDiff_c_cxram.x : main.c csram_base.h Makefile
	#$(CC) $(CFLAGS_DEBUG) -D C_CXRAM -o $@ $^
	$(CC) $(CFLAGS) -D C_CXRAM -o $@ $<

ImageDiff_h2_cxram.x : main.c csram_base.h Makefile
	#$(CC) $(CFLAGS_DEBUG) -D H2_CXRAM -o $@ $^
	$(CC) $(CFLAGS) -D H2_CXRAM -o $@ $<

############################################################
# Not verified                                             #
############################################################
ImageDiff_h2_riscv : main.c
	$(CC) $(CFLAGS_DEBUG) -D H2_RISCV -o $@ $^
	# $(CC) $(CFLAGS) -D H2_RISCV -o $@ $^

clean:
	rm -f *.x *.c *.pgm *.csv *.mem csram_*.h
