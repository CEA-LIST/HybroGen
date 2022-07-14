#ifndef H2_COMMON
#define H2_COMMON

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>
#ifdef H2SYS
#include <sys/mman.h>
#endif

bool h2_codeGenerationOK;

typedef struct
{
  int ValOrReg; // Boolean
  char arith;
  int vLen;
  int wLen;
  int regNro;
  int valueImm;
} h2_sValue_t;


enum ARCH_LIST {X86, RISCV, POWER,  K1,};
enum RISCV_VARIANT {RV32I,};
typedef enum {
    REGISTER,
    VALUE,
} VALORREG;

typedef union {
    float f;
    unsigned long i;
} h2_float_int_u;

#endif /*H2_COMMON*/
