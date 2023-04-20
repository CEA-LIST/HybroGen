CFLAGS = -g -DH2_DEBUG -I../../HybroGen/include

demo-power:
	make clean newton run-newton ARCH="power" CC="powerpc64le-linux-gnu-gcc-10.2.0" SIM="qemu-ppc64le"

demo-riscv:
	make clean newton run-newton ARCH="riscv" CC="riscv32-unknown-elf-gcc"  SIM="qemu-riscv32"

demo-aarch64:
	make clean newton run-newton ARCH="aarch64" CC="aarch64-linux-gnu-gcc"  SIM="qemu-aarch64"

newton:
	../../HybroLang.py -c -a $(ARCH) -i Newton.hl -g
	$(CC) Newton.c -o Newton.$(ARCH) ${CFLAGS}

run-newton:
	make run-demo DEMOCODE=Newton.$(ARCH) DEMOARGS="65536 1e-13"

debug-newton-power: clean newton-power
	make debug-newton ARCH="power" GDB="/opt/hybrotools/powerpc64le/bin/powerpc64le-linux-gdb" SIM="qemu-ppc64le -L /usr/powerpc64le-linux-gnu/" CC="powerpc64le-linux-gnu-gcc-10.2.0"

debug-newton-riscv: clean newton-riscv
	make debug-newton ARCH="riscv" GDB="riscv32-elf-gdb" SIM="qemu-riscv32" CC="riscv32-unknown-elf-gcc"

debug-newton: clean newton
	make debug-demo DEMOCODE=Newton.$(ARCH) DEMOARGS="65536 1e-13"

divide:
	HybroLang.py -c -a power -i DivideThreshold.hl -g
	powerpc64le-linux-gnu-gcc-8 DivideThreshold.c -o DivideThreshold.power ${CFLAGS}

run-divide:
	make run-demo DEMOCODE=DivideThreshold.$(ARCH) DEMOARGS="4 .2 1e-10"

debug-divide: clean divide
	make debug-demo DEMOCODE=DivideThreshold.$(ARCH) DEMOARGS="4 .2 1e-10"

debug-demo:
	echo "$(GDB) ${DEMOCODE}"
	echo "target remote :5555"
	echo "break main"
	echo "continue"
	$(SIM) -g 5555 ${DEMOCODE} ${DEMOARGS}

run-demo:
	$(SIM) -- ${DEMOCODE} ${DEMOARGS}

clean:
	rm -f Newton.aarch64 Newton.power Newton.riscv Newton.c DivideThreshold.c DivideThreshold.power DivideThreshold.riscv
