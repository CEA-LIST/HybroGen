// Auto generated with chatgpt (pro version) lun. 13 avril 2026
// Dialogue :
// * Génère moi un programme C qui réalise un produit de matrice vecteur de taille 4x4
// -> version C raisonnable
// * donne moi une version en C qui génère le meme code en utilisant le JIT de LLVM
// -> code qui ne compile pas
// * Utilise LLVM version 22 et vérifie qu'il n'y a pas d'erreur de compilation
// -> part en boucle sur plein de vérifications
// * De quelles version llvm tu dispose ?
// -> version 17
// * Sur quel système d'exploitation est tu basé ?
// -> réponse qui fait penser à un container
// * Donne moi ce code 
// Compilation with : cc -g i.c -o i `llvm-config22  --cflags --ldflags --libs core executionengine native orcjit` -Wl,--export-dynamic
// 
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#include <llvm-c/Core.h>
#include <llvm-c/Analysis.h>
#include <llvm-c/ExecutionEngine.h>
#include <llvm-c/Target.h>
#include <llvm-c/TargetMachine.h>

void printVectors (float *a, int len, char *msg)
{
  printf ("%s :\n", msg);
  for (int i = 0; i < len; i++)
    {
      for (int j = 0; j < 4; j++)
	printf("%3.3f ", a[i*4+j]);
      printf ("\n");
    }
}

typedef unsigned long long ticks_t;
static  ticks_t h2_codeGenTime;
static inline ticks_t h2_getticks(void)
{
  uint64_t Rt;
  asm volatile("mrs %0,  CNTVCT_EL0" : "=r" (Rt));
  return Rt;
}


typedef void (*matvec4_batch_fn_t)(float *M, float *X, float *Y, uint32_t count);

static void die_llvm_message(const char *prefix, char *msg) {
    fprintf(stderr, "%s%s\n", prefix, msg ? msg : "(message LLVM absent)");
    if (msg) {
        LLVMDisposeMessage(msg);
    }
}

static LLVMValueRef build_matvec4_batch_function(LLVMModuleRef module, LLVMContextRef ctx) {
    LLVMTypeRef f32 = LLVMFloatTypeInContext(ctx);
    LLVMTypeRef void_ty = LLVMVoidTypeInContext(ctx);
    LLVMTypeRef i32 = LLVMInt32TypeInContext(ctx);
    LLVMTypeRef ptr_f32 = LLVMPointerType(f32, 0);

    LLVMTypeRef params[4] = {ptr_f32, ptr_f32, ptr_f32, i32};
    LLVMTypeRef fn_ty = LLVMFunctionType(void_ty, params, 4, 0);

    LLVMValueRef fn = LLVMAddFunction(module, "matvec4_batch", fn_ty);

    LLVMValueRef M = LLVMGetParam(fn, 0);
    LLVMValueRef X = LLVMGetParam(fn, 1);
    LLVMValueRef Y = LLVMGetParam(fn, 2);
    LLVMValueRef count = LLVMGetParam(fn, 3);

    LLVMBasicBlockRef entry = LLVMAppendBasicBlockInContext(ctx, fn, "entry");
    LLVMBasicBlockRef loop_k_cond = LLVMAppendBasicBlockInContext(ctx, fn, "loop_k_cond");
    LLVMBasicBlockRef loop_k_body = LLVMAppendBasicBlockInContext(ctx, fn, "loop_k_body");
    LLVMBasicBlockRef loop_k_end  = LLVMAppendBasicBlockInContext(ctx, fn, "loop_k_end");

    LLVMBuilderRef builder = LLVMCreateBuilderInContext(ctx);
    LLVMPositionBuilderAtEnd(builder, entry);
    LLVMBuildBr(builder, loop_k_cond);

    // for (k = 0; k < count; ++k)
    LLVMPositionBuilderAtEnd(builder, loop_k_cond);
    LLVMValueRef k_phi = LLVMBuildPhi(builder, i32, "k");
    LLVMValueRef k_init = LLVMConstInt(i32, 0, 0);
    LLVMAddIncoming(k_phi, &k_init, &entry, 1);

    LLVMValueRef k_lt_count = LLVMBuildICmp(builder, LLVMIntULT, k_phi, count, "k_lt_count");
    LLVMBuildCondBr(builder, k_lt_count, loop_k_body, loop_k_end);

    LLVMPositionBuilderAtEnd(builder, loop_k_body);

    // base = k * 4
    LLVMValueRef four = LLVMConstInt(i32, 4, 0);
    LLVMValueRef base = LLVMBuildMul(builder, k_phi, four, "base");

    // Déroulage complet des 4 lignes et 4 colonnes
    for (int i = 0; i < 4; ++i) {
        LLVMValueRef sum = LLVMConstReal(f32, 0.0);

        for (int j = 0; j < 4; ++j) {
            unsigned m_index_u = (unsigned)(i * 4 + j);

            LLVMValueRef m_index = LLVMConstInt(i32, m_index_u, 0);
            LLVMValueRef j_val = LLVMConstInt(i32, (unsigned)j, 0);

            LLVMValueRef x_index = LLVMBuildAdd(builder, base, j_val, "x_index");

            LLVMValueRef m_ptr = LLVMBuildGEP2(builder, f32, M, &m_index, 1, "m_ptr");
            LLVMValueRef x_ptr = LLVMBuildGEP2(builder, f32, X, &x_index, 1, "x_ptr");

            LLVMValueRef m_val = LLVMBuildLoad2(builder, f32, m_ptr, "m_val");
            LLVMValueRef x_val = LLVMBuildLoad2(builder, f32, x_ptr, "x_val");

            LLVMValueRef prod = LLVMBuildFMul(builder, m_val, x_val, "prod");
            sum = LLVMBuildFAdd(builder, sum, prod, "sum");
        }

        LLVMValueRef i_val = LLVMConstInt(i32, (unsigned)i, 0);
        LLVMValueRef y_index = LLVMBuildAdd(builder, base, i_val, "y_index");
        LLVMValueRef y_ptr = LLVMBuildGEP2(builder, f32, Y, &y_index, 1, "y_ptr");
        LLVMBuildStore(builder, sum, y_ptr);
    }

    LLVMValueRef one = LLVMConstInt(i32, 1, 0);
    LLVMValueRef k_next = LLVMBuildAdd(builder, k_phi, one, "k_next");
    LLVMBuildBr(builder, loop_k_cond);

    LLVMAddIncoming(k_phi, &k_next, &loop_k_body, 1);

    LLVMPositionBuilderAtEnd(builder, loop_k_end);
    LLVMBuildRetVoid(builder);

    LLVMDisposeBuilder(builder);
    return fn;
}

int main(void) {
    LLVMContextRef ctx = NULL;
    LLVMModuleRef module = NULL;
    LLVMExecutionEngineRef engine = NULL;
    struct LLVMMCJITCompilerOptions options;
    char *error = NULL;

    if (LLVMInitializeNativeTarget() != 0) {
        fprintf(stderr, "Erreur: LLVMInitializeNativeTarget a échoué.\n");
        return 1;
    }
    if (LLVMInitializeNativeAsmPrinter() != 0) {
        fprintf(stderr, "Erreur: LLVMInitializeNativeAsmPrinter a échoué.\n");
        return 1;
    }
    if (LLVMInitializeNativeAsmParser() != 0) {
        fprintf(stderr, "Erreur: LLVMInitializeNativeAsmParser a échoué.\n");
        return 1;
    }

    LLVMLinkInMCJIT();

    ctx = LLVMContextCreate();
    if (ctx == NULL) {
        fprintf(stderr, "Erreur: impossible de créer le contexte LLVM.\n");
        return 1;
    }

    module = LLVMModuleCreateWithNameInContext("jit_matvec4_batch_module", ctx);
    if (module == NULL) {
        fprintf(stderr, "Erreur: impossible de créer le module LLVM.\n");
        LLVMContextDispose(ctx);
        return 1;
    }


    build_matvec4_batch_function(module, ctx); // Build IR

    if (LLVMVerifyModule(module, LLVMReturnStatusAction, &error) != 0) {
        die_llvm_message("Erreur de vérification du module: ", error);
        LLVMDisposeModule(module);
        LLVMContextDispose(ctx);
        return 1;
    }

    h2_codeGenTime = h2_getticks();
    LLVMInitializeMCJITCompilerOptions(&options, sizeof(options));
    options.OptLevel = 0;
    options.CodeModel = LLVMCodeModelJITDefault;
    options.NoFramePointerElim = 0;
    options.EnableFastISel = 0;

    if (LLVMCreateMCJITCompilerForModule(
            &engine,
            module,
            &options,
            sizeof(options),
            &error) != 0) {
        die_llvm_message("Erreur création MCJIT: ", error);
        LLVMDisposeModule(module);
        LLVMContextDispose(ctx);
        return 1;
    }

    uint64_t fn_addr = LLVMGetFunctionAddress(engine, "matvec4_batch");
    if (fn_addr == 0) {
        fprintf(stderr, "Erreur: adresse de la fonction JIT introuvable.\n");
        LLVMDisposeExecutionEngine(engine);
        LLVMContextDispose(ctx);
        return 1;
    }

    matvec4_batch_fn_t matvec4_batch = (matvec4_batch_fn_t)(uintptr_t)fn_addr;
    h2_codeGenTime = h2_getticks() - h2_codeGenTime;
    printf ("Code Gen Ticks %llu\n", h2_codeGenTime);

    // Matrice 4x4
    float M[16] = {
         1.0f,  2.0f,  3.0f,  4.0f,
         0.0f,  1.0f,  0.0f,  0.0f,
         0.0f,  0.0f,  1.0f,  0.0f,
         0.0f,  0.0f,  0.0f,  1.0f
    };

    // 3 vecteurs d'entrée
    uint32_t count = 3;
    float X[12] = {
      1.0f, 1.0f, 1.0f, 1.0f, 
      1.0f, 0.0f, 0.0f, 0.0f, 
      0.0f, 1.0f, 0.0f, 0.0f, 
    };

    float Y[12] = {0};

    printVectors(X, 3, "Input");
    printVectors(Y, 3, "Before");
    matvec4_batch(M, X, Y, count);
    printVectors(Y, 3, "Output");


    LLVMDisposeExecutionEngine(engine);
    LLVMContextDispose(ctx);
    return 0;
}
