#ifndef H2_GAP9
#define H2_GAP9

#include "h2-common.h"
#include "pmsis.h"

typedef uint32_t      h2_insn_t;
static  h2_insn_t   *h2_asm_pc;
static  h2_insn_t    *h2_save_asm_pc;

static void h2_iflush(void *addr, void *last)
{
#ifdef ASM_DEBUG
    printf("Flush data cache from %p to %p\n", addr, last);
#endif
}

static h2_insn_t *h2_malloc (size_t size)
{
  return pi_malloc (size);
}


#endif /*H2_GAP9*/
