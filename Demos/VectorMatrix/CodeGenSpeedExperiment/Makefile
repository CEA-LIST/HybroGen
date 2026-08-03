FILE = LLVM-22-VxM-4x4-chatgpt
CC = clang22
CFLAGS = -g -O3 `llvm-config22  --cflags --ldflags --libs core executionengine native orcjit` -Wl,--export-dynamic
all: 

send:
	scp Makefile ${FILE}.c ${HOST}:tmp/

experiment: ${FILE}
	./LLVM-22-VxM-4x4-chatgpt 1  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17

clean:
	-rm ${FILE}
