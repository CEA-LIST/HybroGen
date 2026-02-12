#ifndef H2_RISCV_RV32G
#define H2_RISCV_RV32G

#define H2SYS 					/* Has  operating system */

#include <stdint.h>
#ifdef H2SYS
#include <sys/mman.h>
#endif

typedef uint32_t    h2_insn_t;  /* Instruction size */
static  h2_insn_t   *h2_asm_pc; /* PC for code generation */
static  h2_insn_t    *h2_save_asm_pc;
static int h2_riscvVectorLen = 1;
static int h2_riscvVectorWidth = 1;
static h2_sValue_t SP= {H2REGISTER, 'i', 1, 32, 2, 0};

/*
https://stackoverflow.com/questions/52187221/how-to-calculate-the-no-of-clock-cycles-in-riscv-clang
*/

#if 0
ticks_t h2_getticks(void)
{
    unsigned long dst;
    // output into any register, likely a0
    // regular instruction:
    asm volatile ("csrrs %0, 0xc00, x0" : "=r" (dst) );
    // regular instruction with symbolic csr and register names
    // asm volatile ("csrrs %0, cycle, zero" : "=r" (dst) );
    // pseudo-instruction:
    // asm volatile ("csrr %0, cycle" : "=r" (dst) );
    // pseudo-instruction:
    //asm volatile ("rdcycle %0" : "=r" (dst) );
    return dst;
}
#else
// From https://github.com/FFTW/fftw3/blob/master/kernel/cycle.h
ticks_t h2_getticks(void)
{
  uint64_t result;
#if __riscv_xlen == 64
  asm volatile("rdtime %0" : "=r" (result));
#elif __riscv_xlen == 32
  uint32_t l, h, h2;
  do
	{
	  asm volatile(
				   "rdtimeh %0 \n"
				   "rdtime  %1 \n"
				   "rdtimeh %2 \n"
				   : "=r" (h), "=r" (l), "=r" (h2));
	} while (h2 != h);
  result = (((uint64_t)h)<<32) | ((uint64_t)l);
#else
#error "unknown __riscv_xlen"
#endif
  return result;
}

#endif

static void h2_iflush(void *addr, void *last)
{
	h2_insnGenerated = (last-addr)/sizeof (h2_insn_t);
#ifdef H2SYS
    long pageSize= getpagesize();
    void *ptmp= (char *)((long)addr & ~(pageSize - 1));
    if (mprotect(ptmp, (last - addr), PROT_READ | PROT_WRITE | PROT_EXEC))
    {
        perror("iflush: mprotect");
        exit(-1);
    }
    __clear_cache((char *)addr, (char *)last);
#endif
#ifdef H2_DEBUG
    printf ("Flush data cache from %p to %p\n", addr, last);
	printf ("%u insns generated in %lld ticks. %lld ticks / insn\n", (unsigned int)h2_insnGenerated, (long long) h2_codeGenTime,  (long long) h2_codeGenTime/h2_insnGenerated);
#endif
	if (!h2_codeGenerationOK)
	  {
		perror("(iflush) Failed code generation\n");
		exit(-5);
	  }
}

static h2_insn_t *h2_malloc (size_t size)
{
  return malloc (size);
}


#endif /*H2_RISCV_RV32G*/
