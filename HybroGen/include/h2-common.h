#ifndef H2_COMMON
#define H2_COMMON
/* Common HybroGen inserted code */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>

bool h2_codeGenerationOK;		/* Does code generation fail ? */
typedef unsigned long long ticks_t;
static  ticks_t h2_start_codeGen, h2_end_codeGen;

typedef struct
{
  int ValOrReg; // is register or immediate value ?
  char arith;   // int, flt or other arithmetic
  int vLen;     // vector len
  int wLen;     // word len
  int regNro;   // register number (if register)
  int valueImm; // immediate value (if not register)
} h2_sValue_t;

typedef enum { REGISTER,    VALUE, } VALORREG;

typedef union {
    float f;
    unsigned long i;
} h2_float_int_u;

static int h2_log2(int value)
{
  int log = 0;
  while (value >>= 1) { ++log; }
  return log;
}
#endif /*H2_COMMON*/
