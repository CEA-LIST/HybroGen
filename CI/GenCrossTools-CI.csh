#!/bin/tcsh


if ($#argv < 1) then
    echo "Give an architecture name"
    echo "$0 [aarch64|riscv|power]"
    exit -1
endif


setenv ARCH $1
setenv TMPDIR /opt/H-CI/

echo "Génération pour $ARCH"
./GenCrossTools.py -a ${ARCH}  -p ${TMPDIR} -w ${TMPDIR}/tmp
./GenCrossTools.py -a ${ARCH}  -p ${TMPDIR} -w ${TMPDIR}/tmp -t
./GenCrossTools.py -a ${ARCH}  -p ${TMPDIR} -w ${TMPDIR}/tmp -s
source ${TMPDIR}/${ARCH}/.cshrc
cd CodeExamples/
./Regression.py ${ARCH}
rm -rf ${TMPDIR}/${ARCH}
rm -rf ${TMPDIR}/tmp/build
rm -rf ${TMPDIR}/tmp/src
