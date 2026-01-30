#ifndef H2_COMMON
#define H2_COMMON
/* Common HybroGen inserted code */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>
#include <stdint.h>

bool h2_codeGenerationOK;	 // Does code generation fail ?
typedef int32_t h2_regSet_t; // Register set (signed, use -1 when not allocated)
static  uint32_t h2_insnGenerated;
typedef unsigned long long ticks_t;
static  ticks_t h2_codeGenTime;

typedef enum { H2REGISTER,    H2VALUE, } VALORREG;
typedef struct
{
  int ValOrReg; // is H2REGISTER or immediate VALUE ?
  char arith;   // int, flt or other arithmetic
  int vLen;     // vector len
  int wLen;     // word len
  int regNro;   // register number (if register)
  int valueImm; // immediate value (if not register)
  bool dontFree; // if register, don't free
} h2_sValue_t;
#define sValueDef(VALUE, ARITH, VECTORLEN, WORDLEN, REGNO, IMMVAL) ((h2_sValue_t){.ValOrReg = VALUE, .arith = ARITH, .vLen = VECTORLEN, .wLen = WORDLEN, .regNro = REGNO, .valueImm = IMMVAL})
#define intsValue(V) sValueDef(H2VALUE, 'i', 1, 32, -1, V)
#define immValueZero intsValue(0)
// Usefull macro instruction to simplify instruction selector code
#define isInt64_1(P)  ((P.arith == 'i') && (P.wLen <= 64) && (P.vLen == 1))
#define isInt32_1(P)  ((P.arith == 'i') && (P.wLen <= 32) && (P.vLen == 1))
#define isInt0(P)     ((P.arith == 'i') && (P.ValOrReg == H2VALUE) && (0 == P.valueImm))
#define isInt1(P)     ((P.arith == 'i') && (P.ValOrReg == H2VALUE) && (1 == P.valueImm))
#define isValue(P)    ((P.arith == 'i') && (P.ValOrReg == H2VALUE))
#define isReg32(P, X) ((P.arith == 'i') && (P.ValOrReg == H2REGISTER) && (X == P.regNro))
#define isRRR(P0, P1, P2) (P0.ValOrReg == H2REGISTER && P1.ValOrReg == H2REGISTER && P2.ValOrReg == H2REGISTER)
#define isRRV(P0, P1, P2) (P0.ValOrReg == H2REGISTER && P1.ValOrReg == H2REGISTER && P2.ValOrReg == H2VALUE)


typedef union {
    float f;
    unsigned long i;
} h2_float_int_u;

static int h2_log2(int value)
{ // integer logarithm
  int log = 0;
  while (value >>= 1) { ++log; }
  return log;
}

void printRev (int value, int pos)
{ // Print a bitset in reversal order (recursive)
  if (pos != 0)
	printRev (value >> 1, pos - 1);
  printf ("%1c", (value % 2)?'.':'F');
}

// Dynamic register allocation handling
// h2_regSet mask : 0 mean free register, 1 register set
//  3           2            1  Bit position = reg Number
// 1098 7654 3210 9876 5432 1098 7654 3210
// 1111 1111 1111 1111 0000 0001 0011 1111
typedef struct
{	// Register allocation sets for
  	// int, float, vector of ints, vector of floats
  int intSet, fltSet, vintSet, vfltSet ;
} h2_RegSets_t;

h2_RegSets_t h2_regSet, h2_regSetInit;

// Print integer register set
void printRegState(char * msg, int regNo, int registerSet)
{
  int count = 8 * sizeof (registerSet) - 1;
  h2_regSet_t tmpReg = registerSet;
  printf ("%02d : Reg %s\n", regNo, msg);
  for (int i = count; i >= 0; i--) // Tens
	(0 == (i % 10))?printf ("%d", i/10):printf (" ");
  printf ("\n");
  for (int i = count; i >= 0; i--) // Unit
	  printf ("%d", i%10);
  printf ("\n");
  printRev (tmpReg, count); // Bit set
  printf ("\n");
}

// Initialize registers sets allocation
static void h2_initRegisterMasks(int intmask, int fltmask, int vectorintmask, int vectorfltmask)
{ // See H2SymbolTable & H2RegisterBank
  h2_regSetInit.intSet  = intmask;
  h2_regSetInit.fltSet  = fltmask;
  h2_regSetInit.vintSet = vectorintmask;
  h2_regSetInit.vfltSet = vectorfltmask;
}

static void h2_resetRegisterMasks() // Reset register set from initializers
{
  h2_regSet.intSet  = h2_regSetInit.intSet;
  h2_regSet.fltSet  = h2_regSetInit.fltSet;
  h2_regSet.vintSet = h2_regSetInit.vintSet;
  h2_regSet.vfltSet = h2_regSetInit.vfltSet;
#ifdef H2_DEBUG_REGISTER
  printRegState("RESET", -1, h2_regSet.intSet);
#endif // H2_DEBUG_REGISTER
}
int h2_getReg () // Get new register
{
  /* Search for the 1st free register */
  h2_regSet_t tmpReg = h2_regSet.intSet;
  for (int i = 0; i < 8 * sizeof (h2_regSet.intSet); i++)
	{
	  if (tmpReg % 2 == 0)
		{						/* Free register found */
		  h2_regSet.intSet = h2_regSet.intSet | (1 << i); /* Update regSet */
#ifdef H2_DEBUG_REGISTER
		  printRegState("GET", i, h2_regSet.intSet);
#endif // H2_DEBUG_REGISTER
		  return i;
		}
	  tmpReg >>= 1;
	}
  printf ("Register allocation failed\n");
  h2_codeGenerationOK = false;
  return -1;
}

// h2_regSet_t regToBeFreed[32];

void h2_freeReg (h2_regSet_t v) // Free a register
{
#if 1 // TODO : To be rethinked
      // Is the register freeable ?
  int isOK = (h2_regSetInit.intSet >> v) & 1;
  if (0 == isOK)
    {
	h2_regSet.intSet = h2_regSet.intSet & ~(1 << v); /* Update regSet */
#ifdef H2_DEBUG_REGISTER
    printRegState("FREE", v, h2_regSet.intSet);
#endif // H2_DEBUG_REGISTER
    }
#endif
}
#endif /*H2_COMMON*/
