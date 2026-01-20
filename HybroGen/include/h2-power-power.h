#ifndef H2_POWER
#define H2_POWER

#define H2SYS 					/* Has  operating system */

#include <stdint.h>
#ifdef H2SYS
#include <sys/mman.h>
#endif

/* aarch64 / power examples :
   https://github.com/FFTW/fftw3/blob/master/kernel/cycle.h */

typedef uint32_t      h2_insn_t;
static  h2_insn_t     *h2_asm_pc;
static  h2_insn_t     *h2_save_asm_pc;

static ticks_t h2_getticks(void)
{
     unsigned int tbl, tbu0, tbu1;

     do {
	  __asm__ __volatile__ ("mftbu %0" : "=r"(tbu0));
	  __asm__ __volatile__ ("mftb %0" : "=r"(tbl));
	  __asm__ __volatile__ ("mftbu %0" : "=r"(tbu1));
     } while (tbu0 != tbu1);

     return (((unsigned long long)tbu0) << 32) | tbl;
}

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
#endif
#ifdef H2_DEBUG
    printf ("Flush data cache from %p to %p\n", addr, last);
	printf ("%ld insn generated in %ld ticks. %ld ticks / insn\n", h2_insnGenerated, h2_codeGenTime, h2_codeGenTime/h2_insnGenerated);
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

#endif /*H2_POWER*/
