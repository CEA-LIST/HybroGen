PRECISION_8=6
PRECISION_16=9
SAMPLE_LENGTH ?= 512
MAX_TOL_MARGIN=0.1
H2_ROOT=../../../

H2=$(H2_ROOT)/HybroLang.py
H2FLAGS=-a csram-v2.0 --toC -g

CC=riscv32-unknown-linux-gnu-gcc
CFLAGS=-Wall -I$(H2_ROOT)/HybroGen/include -I./include -O0 -g -static
CFLAGS_DEBUG=$(CFLAGS) -D DEBUG

INCLUDES=include/csram_base.h include/sine.h include/fft_utils.h

ISS=qim --run

.PRECIOUS : %.h %.c %.x

all : DFT_c_riscv DFT16_c_riscv DFT32_c_riscv

include/csram_base.h: Makefile
	qim --gen-macros include

include/fft_utils.h : scripts/gen_fft_utils.py Makefile
	./scripts/gen_fft_utils.py --8-bit $(PRECISION_8) --16-bit $(PRECISION_16) --length $(SAMPLE_LENGTH)

%.c: %.hl Makefile
	rm -f $@
	$(H2) $(H2FLAGS) -i $<

eval_%: %
	./scripts/gen_inputs.py $(SAMPLE_LENGTH) numpy_ref
	qim --run $<_$(SAMPLE_LENGTH).x numpy_ref.sine $<.dft
	./scripts/diff_dft.py numpy_ref.dft $<.dft $(MAX_TOL_MARGIN)

DFT_c_riscv: main.c $(INCLUDES) Makefile
	$(CC) $(CFLAGS) -o $@_$(SAMPLE_LENGTH).x $< -lm

DFT16_c_riscv: main.c $(INCLUDES) Makefile
	$(CC) $(CFLAGS) -D CPLX16 -o $@_$(SAMPLE_LENGTH).x $< -lm

DFT32_c_riscv: main.c $(INCLUDES) Makefile
	$(CC) $(CFLAGS) -D CPLX32 -o $@_$(SAMPLE_LENGTH).x $< -lm

DFT_4step_c_riscv: main_4step.c $(INCLUDES) Makefile
	$(CC) $(CFLAGS) -o $@_$(SAMPLE_LENGTH).x $< -lm

DFT16_4step_c_riscv: main_4step.c $(INCLUDES) Makefile
	$(CC) $(CFLAGS) -D CPLX16 -o $@_$(SAMPLE_LENGTH).x $< -lm

DFT32_4step_c_riscv: main_4step.c $(INCLUDES) Makefile
	$(CC) $(CFLAGS) -D CPLX32 -o $@_$(SAMPLE_LENGTH).x $< -lm

%.log: %.x Makefile
	$(ISS) $< | tee $@

clean:
	rm -f *.c *.x *.dft *.sine *.log *.csv *.mem *.png include/csram_*.h include/fft_utils.h
