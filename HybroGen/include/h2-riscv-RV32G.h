#ifndef H2_RISCV_RV32G
#define H2_RISCV_RV32G

#include <stdint.h>

typedef uint32_t    h2_insn_t;
typedef unsigned 	long ticks;
static  h2_insn_t   *h2_asm_pc;
static  h2_insn_t    *h2_save_asm_pc;

/* 
https://stackoverflow.com/questions/52187221/how-to-calculate-the-no-of-clock-cycles-in-riscv-clang
*/

unsigned long getticks(void)
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
#endif
#ifdef ASM_DEBUG
    printf("Flush data cache from %p to %p\n", addr, last);
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
