# Main Hybrogen makefile

.PHONY: power riscv aarch64 cxram DbPopulate DbArch stats buildGrammar clean doregression

all:
	@echo "What action do you target ?"
	@echo "make buildGrammar # Build grammars (need antlr)"
	@echo "make DbPopulate   # Fill database with instruction sets"
	@echo "make clean # Clean grammars generated files and delete database"
	@echo "make buildAll # Clean environment Build grammars, fill database and build Demos. HybroGen ready to use"
	@echo "make check # To check if your installation is completed"   

buildAll: clean
	make buildGrammar
	make DbPopulate
	make cd ./Demos && make buildAll

# Uncomment if you whish to use distant database
# DBIDS = --dbIds "DistantHost:DataBaseName:UserDbName:DbPassword"

# Uncomment if you whish to use distant database
# DBIDS = --dbIds "DistantHost:DataBaseName:UserDbName:DbPassword"



DbPopulate:
	./H2Isa.py -n ${DBIDS} # Create database schema
	make DbArch ARCH=aarch64
	make DbArch ARCH=riscv
	make DbArch ARCH=power
	./H2Isa.py -i -a cxram ${DBIDS}	 # No register description for cxram
	@echo "Need to generate environment ?"
	@echo "Example : ./GenCrossTools.py -s -a cxram-linux -a powerpc"

DbArch:
	./H2Isa.py -i -a ${ARCH} ${DBIDS} # ISA description database insertion
	./H2Reg.py -i -a ${ARCH} ${DBIDS} # Register description database insertion

buildGrammar:
	(cd HybroGen  ; make all) # Lexers / parsers for input data
	(cd HybroLang ; make all) # Lexers / parsers for HybroLang language

stats:
	wc -l *.py HybroLang/*.py HybroGen/*.py

clean:
	make buildGrammar
	./H2Isa.py -p ${DBIDS}
	./H2Reg.py -p ${DBIDS}
	-(cd HybroGen ;     make clean)
	-(cd HybroLang;     make clean)
	-(cd CodeExamples/; make clean)
	-(cd docs/;         make clean)
	-(cd Demos/; 		make clean)

doregression:
	@(cd CodeExamples && ./Regression.py ${THEARCH})

aarch64:
	@make doregression THEARCH=aarch64

riscv:
	@make doregression THEARCH=riscv

power:
	@make doregression THEARCH=power

cxram:
	@make doregression THEARCH=cxram


VERBOSE ?= 0

ifeq ($(VERBOSE),1)
	REDIRECT :=
else
	REDIRECT := > /dev/null 2>&1
endif


check:
	@echo "[INFO] Start check with Regression test"
	@make --no-print-directory aarch64 ${REDIRECT} && (echo "[OK] Regression test on aarch64")|| (echo "[FAIL] Regression test fail for aarch64")
	@make --no-print-directory power ${REDIRECT} && (echo "[OK] Regression test on power")|| (echo "[FAIL] Regression test fail for power")
	@make --no-print-directory riscv ${REDIRECT} && (echo "[OK] Regression test on riscv")|| (echo "[FAIL] Regression test fail for riscv")
#	@echo "[INFO]start check with regressionSingleOp"
#	@(cd CodeExamples && ./RegressionSingleOp.py -d -a aarch64 riscv power ${REDIRECT})
#	@(cd CodeExamples && ./RegressionSingleOp.py -z -a aarch64 ${REDIRECT} ) && (echo "[OK] Regression test on aarch64")|| (echo "[FAIL] Regression test fail for aarch64")
#	@(cd CodeExamples && ./RegressionSingleOp.py -z -a power ${REDIRECT} ) && (echo "[OK] Regression test on power")|| (echo "[FAIL] Regression test fail for power")
#	@(cd CodeExamples && ./RegressionSingleOp.py -z -a riscv ${REDIRECT} ) && (echo "[OK] Regression test on riscv")|| (echo "[FAIL] Regression test fail for riscv")
	@echo "[INFO] Start trying Demo Stencil (can takes a lot of time (15-20 minutes))"
	@(cd ./Demos/Stencil && make -s --no-print-directory allAarch64Qemu ${REDIRECT} ) && (echo "[OK] Demo stencil on aarch64 works") || (echo "[FAIL] Demo Stencil fail on aarch64")
	@(cd ./Demos/Stencil && make -s --no-print-directory allRiscvQemu ${REDIRECT} ) && (echo "[OK] Demo stencil on riscv works") || (echo "[FAIL] Demo Stencil fail on riscv")
	@(cd ./Demos/Stencil && make -s --no-print-directory allPowerQemu ${REDIRECT} ) && (echo "[OK] Demo stencil on power works") || (echo "[FAIL] Demo Stencil fail on power")
	@echo "[INFO] Start Trying Demo Vector Matrix"
	@(cd ./Demos/VectorMatrix && make -s --no-print-directory aarch64 ${REDIRECT} ) && (echo "[OK] Demo Vector Matrix on aarch64 works") || (echo "[FAIL] Demo Vector Matrix fail on aarch64")
	@(cd ./Demos/VectorMatrix && make -s --no-print-directory riscv ${REDIRECT} ) && (echo "[OK] Demo Vector Matrix on riscv works") || (echo "[FAIL] Demo Vector Matrix fail on riscv")
	@(cd ./Demos/VectorMatrix && make -s --no-print-directory power ${REDIRECT} ) && (echo "[OK] Demo Vector Matrix on power works") || (echo "[FAIL] Demo Vector Matrix fail on power")
	@echo "[INFO] Start Trying Demo Newton-SquareRoot-VariablePrecision"
	@(cd ./Demos/Newton-SquareRoot-VariablePrecision && make -s --no-print-directory demo-aarch64 ${REDIRECT} ) && (echo "[OK] Demo Newton-SquareRoot-VariablePrecision on aarch64 works") || (echo "[FAIL] Demo Newton-SquareRoot-VariablePrecision fail on aarch64")
	@(cd ./Demos/Newton-SquareRoot-VariablePrecision && make -s --no-print-directory demo-power ${REDIRECT} ) && (echo "[OK] Demo Newton-SquareRoot-VariablePrecision on power works") || (echo "[FAIL] Demo Newton-SquareRoot-VariablePrecision fail on power")
	@(cd ./Demos/Newton-SquareRoot-VariablePrecision && make -s --no-print-directory demo-riscv ${REDIRECT} ) && (echo "[OK] Demo Newton-SquareRoot-VariablePrecision on riscv works") || (echo "[FAIL] Demo Newton-SquareRoot-VariablePrecision fail on riscv")
