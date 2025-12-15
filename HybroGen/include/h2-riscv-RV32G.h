#ifndef H2_RISCV_RV32G
#define H2_RISCV_RV32G

#define H2SYS 					/* Has  operating system */

#include <stdint.h>
#ifdef H2SYS
#include <sys/mman.h>
#endif

typedef uint32_t    h2_insn_t;
static  h2_insn_t   *h2_asm_pc;
static  h2_insn_t    *h2_save_asm_pc;
static int h2_riscvVectorLen = 1;
static int h2_riscvVectorWidth = 1;
/*
https://stackoverflow.com/questions/52187221/how-to-calculate-the-no-of-clock-cycles-in-riscv-clang
*/

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


static void h2_iflush(void *addr, void *last)
{
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
	uint64_t codeGenDuration = h2_end_codeGen - h2_start_codeGen;
	uint64_t insnGenerated = (last-addr)/sizeof (h2_insn_t);
    printf ("Flush data cache from %p to %p\n", addr, last);
	printf ("%lld insn generated in %lld ticks. %lld ticks / insn\n", insnGenerated, codeGenDuration, codeGenDuration/insnGenerated);
#endif
	if (!h2_codeGenerationOK)
	  {
		fprintf (stderr, "(iflush) Failed code generation\n");
		exit(-5);
	  }
}

static h2_insn_t *h2_malloc (size_t size)
{
  return malloc (size);
}


#endif /*H2_RISCV_RV32G*/
