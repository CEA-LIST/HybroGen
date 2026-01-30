#ifndef H2_AARCH64
#define H2_AARCH64

#define H2SYS 					/* Has  operating system */

#ifdef H2SYS
#include <sys/mman.h>
#endif

typedef uint32_t   h2_insn_t;   /* Instruction size */
static  h2_insn_t  *h2_asm_pc; /* PC for code generation */
static  h2_insn_t  *h2_save_asm_pc;
#define H2Aarch64SP  (h2_sValue_t) {REGISTER, 'i', 1, 32, 31, 0}
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
	h2_insnGenerated = (last-addr)/sizeof (h2_insn_t);
#ifdef H2SYS
  __clear_cache((char *)addr, (char *)last); // Flush data cache where binary code were written
  long pageSize= getpagesize();              // Make the page executable
  void *ptmp= (char *)((long)addr & ~(pageSize - 1));
  if (mprotect(ptmp, (last - addr), PROT_READ | PROT_WRITE | PROT_EXEC))
    {
      perror("iflush: mprotect");
      exit(-1);
    }
    /* Gcc function to clear data cache after code generation */
    __clear_cache((char *)addr, (char *)last);
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


#endif /* H2_AARCH64 */
