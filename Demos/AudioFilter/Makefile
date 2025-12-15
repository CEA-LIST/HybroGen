# http://peabody.sapp.org/class/350.838/lab/biquad/
BIQUADPARAM = 1.0 0.0 -1.0 1.0 0.1 0.9

all:
	HybroLang.py -a riscv -i biquad.hl -c
	riscv32-elf-gcc-9.3.0 -o biquad.riscv biquad.c -I../../HybroGen/include
	qemu-riscv32 biquad.riscv ${BIQUADPARAM} InFile.au OutFile.au

convert:
	sox  OprecompBonjourWithNoise.wav --encoding floating-point --channels 1 InFile.au

demoWithSox:
	sox  InFile.au OutFileSox.au biquad ${BIQUADPARAM}

demoNoise:
	-sox  --plot gnuplot Noise.wav OutFileSox.wav biquad ${BIQUADPARAM} > /tmp/a.plt
	-gnuplot /tmp/a.plt

clean:
	rm -f biquad.c biquad.riscv
