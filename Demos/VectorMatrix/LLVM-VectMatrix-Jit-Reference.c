// ChatGPT.com prompt : "Donne moi un programme en C compilable par
// LLVM version 20 qui fait du JIT pour un produit de vecteur matrice
// de taille 4x4"


// Objective : measure LLVM JIT speed in terms of clock cycle per instruction

// Compile with (on a FreeBSD based raspberry-pi:
// clang22 -g -o LLVM-VectMatrix-Jit-Reference LLVM-VectMatrix-Jit-Reference.c `llvm-config22 --cflags --ldflags --libs --system-libs`

// Observe instruction count :
// lldb LLVM-VectMatrix-Jit-Reference
// - break set --basename main
// - break set --line 100
// run
// print fn
// disassemble -a 0x0000585cf8b7a000 -> 54 instruction

// 10 runs give 

// (2728970+2857041+2663514+2861284+2853811+2850587+2870527+2867097+2650588+2852286)/(10*54)
// -> 51955. cycle per instructions


// pi00:~/>bc -l
// 2919886/54
// 54071.96296296296296296296


#include <stdio.h>
#include <stdlib.h>
#include <llvm-c/Core.h>
#include <llvm-c/ExecutionEngine.h>
#include <llvm-c/Target.h>
#include <llvm-c/Analysis.h>
#include <llvm-c/Orc.h>

typedef unsigned long long ticks_t;
static  ticks_t h2_codeGenTime;
static inline ticks_t h2_getticks(void)
{
  uint64_t Rt;
  asm volatile("mrs %0,  CNTVCT_EL0" : "=r" (Rt));
  return Rt;
}

void printVector(float *vec, char* mesg)
{
    printf("%s:\n");  
    for (int i = 0; i < 4; i++)
      {
        printf("%2.2f ", vec[i]);
      }
    printf("\n");
}
void printMatrix(float *m, char* mesg)
{
    printf("%s:\n");  
    for (int i = 0; i < 4; i++)
      {
        for (int j = 0; j < 4; j++)
          {
            printf("%2.2f ", m[i * 4 + j]);
          }
        printf("\n");
      }
}
// Type de la fonction JIT
typedef void (*matvec4_func)(float *vec, float *mat, float *out);

int main() {
    LLVMInitializeNativeTarget();      // Initialisation LLVM
    LLVMInitializeNativeAsmPrinter();

    LLVMModuleRef  module  = LLVMModuleCreateWithName("jit_module");
    LLVMBuilderRef builder = LLVMCreateBuilder();
    LLVMTypeRef    floatTy = LLVMFloatType();

    LLVMTypeRef paramTypes[] = {      // Signature : void f(float* vec, float* mat, float* out)
        LLVMPointerType(floatTy, 0),
        LLVMPointerType(floatTy, 0),
        LLVMPointerType(floatTy, 0)
    };

    LLVMTypeRef funcType = LLVMFunctionType(LLVMVoidType(), paramTypes, 3, 0);
    LLVMValueRef  func   = LLVMAddFunction(module, "matvec4", funcType);

    LLVMValueRef vec = LLVMGetParam(func, 0);
    LLVMValueRef mat = LLVMGetParam(func, 1);
    LLVMValueRef out = LLVMGetParam(func, 2);

    LLVMBasicBlockRef entry = LLVMAppendBasicBlock(func, "entry");
    LLVMPositionBuilderAtEnd(builder, entry);


    for (int i = 0; i < 4; i++) {    // Fully unroll the loops
        LLVMValueRef sum = LLVMConstReal(floatTy, 0.0);
        for (int j = 0; j < 4; j++) {             // vec[j]
            LLVMValueRef idx_j   = LLVMConstInt(LLVMInt32Type(), j, 0);
            LLVMValueRef vec_ptr = LLVMBuildGEP2(builder, floatTy, vec, &idx_j, 1, "vec_ptr");
            LLVMValueRef vec_val = LLVMBuildLoad2(builder, floatTy, vec_ptr, "vec_val");
            // mat[i*4 + j]
            LLVMValueRef idx_m   = LLVMConstInt(LLVMInt32Type(), i * 4 + j, 0);
            LLVMValueRef mat_ptr = LLVMBuildGEP2(builder, floatTy, mat, &idx_m, 1, "mat_ptr");
            LLVMValueRef mat_val = LLVMBuildLoad2(builder, floatTy, mat_ptr, "mat_val");

            LLVMValueRef prod = LLVMBuildFMul(builder, vec_val, mat_val, "prod");
            sum = LLVMBuildFAdd(builder, sum, prod, "sum");
        }
        // out[i]
        LLVMValueRef idx_i = LLVMConstInt(LLVMInt32Type(), i, 0);
        LLVMValueRef out_ptr = LLVMBuildGEP2(builder, floatTy, out, &idx_i, 1, "out_ptr");
        LLVMBuildStore(builder, sum, out_ptr);
    }

    LLVMBuildRetVoid(builder);

    // Vérification
    if (LLVMVerifyModule(module, LLVMAbortProcessAction, NULL)) {
        fprintf(stderr, "Erreur module\n");
        return 1;
    }

    LLVMExecutionEngineRef engine;     // Création du moteur JIT
    char *error = NULL;

	h2_codeGenTime = h2_getticks();
    if (LLVMCreateExecutionEngineForModule(&engine, module, &error) != 0) {
        fprintf(stderr, "Erreur JIT: %s\n", error);
        LLVMDisposeMessage(error);
        return 1;
    }

    // Récupérer fonction JIT
    matvec4_func fn = (matvec4_func)LLVMGetFunctionAddress(engine, "matvec4");
	h2_codeGenTime = h2_getticks() - h2_codeGenTime;
    printf ("Code Gen Ticks %llu\n", h2_codeGenTime);

    float vec_data[4] = {random () % 1000, random () % 1000, random () % 1000, random () % 1000};     // Données test
    float mat_data[16] =
      {
        4, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12,
        13, 14, 15, 16,
      };
    float out_data[4] = {0};

    fn(vec_data, mat_data, out_data);    // Call jitted function

    printVector (vec_data, "Input");
    printMatrix (mat_data, "Matrix");
    printVector (out_data, "Output");

    LLVMDisposeBuilder(builder);
    LLVMDisposeExecutionEngine(engine);
    return 0;
}
