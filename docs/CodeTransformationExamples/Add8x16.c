// -*- c -*-

#include <stdio.h>
#include <stdlib.h>

code * genAdd(insn * code) // C compilette prototype
{ // Compilette rewriting Add8x16.hl 
  // Macro definition genAdd RISCV

  struct {
    ValOrReg int; // Boolean
    Arith char;   // 
    Vlen int;     // Vector Len
    Wlen int;
    RegList * sRegList; 
    ValueList * sValueList;
  } sValue;
  gen_add_RISCV_RV32I_XfR8(sValue Dest, sValue S1, sValue S2)
    { // Only add 2 vectors of 16 elements of 8 bits floats
      // Check data type consistency (Arith, Vlen equals)
      // WSize depend on operation (+1 for add, *2 for mul ...)
      assert_type_consistency (Dest, S1); 
      assert_type_consistency (Dest, S2);       
      // Instruction selection
      if (Dest.Arith == "f" && Dest.Vlen == 16 && Dest.Wlen == 8 && ValOrReg == REG)
       {
         add_RISCV_RV32I_XfR8_FLT_1_8_RRR()
         add_RISCV_RV32I_XfR8_FLT_1_8_RRR()
         add_RISCV_RV32I_XfR8_FLT_1_8_RRR()
         add_RISCV_RV32I_XfR8_FLT_1_8_RRR()
         add_RISCV_RV32I_XfR8_FLT_1_8_RRR()
         add_RISCV_RV32I_XfR8_FLT_1_8_RRR()
         add_RISCV_RV32I_XfR8_FLT_1_8_RRR()
         add_RISCV_RV32I_XfR8_FLT_1_8_RRR()
         add_RISCV_RV32I_XfR8_FLT_1_8_RRR()
         add_RISCV_RV32I_XfR8_FLT_1_8_RRR()
         add_RISCV_RV32I_XfR8_FLT_1_8_RRR()
         add_RISCV_RV32I_XfR8_FLT_1_8_RRR()
         add_RISCV_RV32I_XfR8_FLT_1_8_RRR()
         add_RISCV_RV32I_XfR8_FLT_1_8_RRR()
         add_RISCV_RV32I_XfR8_FLT_1_8_RRR()
         add_RISCV_RV32I_XfR8_FLT_1_8_RRR()
       }
    }
  gen_return_RISCV()
    {
      return_RISCV_RV32I_XfR8()
    }

  // Resister name definition

  // Compilette generator
	code *  add (flt 8 16 , flt 8 16 b)
	{
      gen_add_RISCV_RV32I_RV32F(RISCV_out0, RISCV_in0, RISCV_in1);
      gen_return();
    }
} // End of compilette rewriting Add8x16.hl

// Simple addition between variables which are
// 2 vectors composed of 16 values of 8 bits float numbers

int main(int argv, char * argv)
{
  int i;
  float in1[16], res[16];
  h2_insn * ptr;
  for (i=0; i < 16; i++)
      in1[i] = atof(argv[1+i]);
  ptr = h2_alloc (1024);   // Allocate memory for 1024 instructions
  code = genAdd (ptr, RISCV_RV32F); // Generate instructions
  res = code (in1, in1);  // Call generated code
  for (i=0; i < 16; i++)
    printf("%d + %d = %d\n", in1[i], in[i], res[i]);
  return res; // return value for platforms without printf
}
