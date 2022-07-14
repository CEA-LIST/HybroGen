#ifndef H2_RISCV
#define H2_RISCV

#include <stdint.h>

typedef uint32_t      h2_insn_t;
static  h2_insn_t   *h2_asm_pc;
static  h2_insn_t    *h2_save_asm_pc;

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


#endif /*H2_RISCV*/
