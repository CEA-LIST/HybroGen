#ifndef H2_RISCV_CXRAM
#define H2_RISCV_CXRAM

#include <stdint.h>
#include <sys/mman.h>

typedef uint32_t     h2_insn_t;
static  h2_insn_t   *h2_asm_pc;
static  h2_insn_t   *h2_save_asm_pc;


void fatalError (char * msg)
{
  fprintf(stderr, "%s\n", msg);
  exit(-1);
}
static void h2_init_cxram ()
{
  h2_cxram_line_t *base_addr, *cxram_imc;
  int prot, flags;

#if 0
  /* Tiles allocations */
  if (h2_cxram_tiles == NULL)
	h2_cxram_tiles = (h2_cxram_line_t *)calloc(CXRAM_BASE_SIZE, sizeof (char));
#endif

  /* mmap properties */
  prot =  PROT_READ  | PROT_WRITE    | PROT_EXEC;
  flags = MAP_SHARED | MAP_ANONYMOUS | MAP_FIXED;
  /* Tiles mapping at a fixed address */
  base_addr = (h2_cxram_line_t *)mmap((void *)CXRAM_BASE_ADDR, (CXRAM_BASE_SIZE), prot, flags, 0, 0);
  if(base_addr != (void*)((uintptr_t)CXRAM_BASE_ADDR))
	fatalError("Failed mmap for TILES\n");
  /* Mapping to avoid core dump during store word instructions */
  cxram_imc = (h2_cxram_line_t *)mmap((void *)CXRAM_IMC_ADDR,   (CXRAM_IMC_SIZE), prot, flags, 0, 0);
  if(cxram_imc != (void*)((uintptr_t)CXRAM_IMC_ADDR))
	fatalError("Failed mmap for \n");

#ifdef H2_DEBUG
  printf("Init CxRAM %p mapped at %p for %d bytes\n", CXRAM_BASE_ADDR, base_addr, CXRAM_BASE_SIZE);
#endif
  //  if (h2_cxram_tiles == NULL)
  h2_cxram_tiles = base_addr;
}

static void h2_iflush(void *addr, void *last)
{
#ifdef H2SYS
	long pageSize= getpagesize();
	void *ptmp= (char *)((long)addr & ~(pageSize - 1));
	if (mprotect(ptmp, (last - addr), PROT_READ | PROT_WRITE | PROT_EXEC))
	  fatalError("iflush: mprotect");
#ifdef H2_DEBUG
	printf("Flush data cache from %p to %p\n", addr, last);
#endif
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

#endif /*H2_RISCV_CXRAM*/
