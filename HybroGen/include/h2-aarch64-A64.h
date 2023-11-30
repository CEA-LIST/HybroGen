#ifndef H2_AARCH64
#define H2_AARCH64

#define H2SYS 					/* Has  operating system */

#include <stdint.h>
#ifdef H2SYS
#include <sys/mman.h>
#endif

typedef uint32_t   h2_insn_t;
static  h2_insn_t  *h2_asm_pc;
static  h2_insn_t  *h2_save_asm_pc;

/* aarch64 / power examples :
   https://github.com/FFTW/fftw3/blob/master/kernel/cycle.h */

static inline ticks_t h2_getticks(void)
{
  uint64_t Rt;
  asm volatile("mrs %0,  CNTVCT_EL0" : "=r" (Rt));
  return Rt;
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
#ifdef H2_DEBUG
	uint64_t codeGenDuration = h2_end_codeGen - h2_start_codeGen;
	uint64_t insnGenerated = (last-addr)/sizeof (h2_insn_t);
    printf ("Flush data cache from %p to %p\n", addr, last);
	printf ("%ld insn generated in %ld ticks. %ld ticks / insn\n", insnGenerated, codeGenDuration, codeGenDuration/insnGenerated);
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


#endif /* H2_AARCH64 */
