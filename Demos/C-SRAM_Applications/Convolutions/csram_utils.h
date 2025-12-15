///////////////////////////////////////////////////////////////////////////////
// csram_utils
// - This library includes a few header definitions as well as functions to
//   write C-SRAM benchmarks
// Author : Kevin Mambu, CEA Grenoble, 2020
///////////////////////////////////////////////////////////////////////////////

#ifndef _CSRAM_UTILS_H
#define _CSRAM_UTILS_H

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <sys/mman.h>

#ifdef DEBUG
#define printf_(...) printf(__VA_ARGS__); fflush(stdout)
#else
#define printf_(...)
#endif

#define _CASE(errorcode) case errorcode: printf(__FILE__ ":%d"   " " #errorcode "(%d) ", __LINE__, error); break;
// -----------------------------------------------------------------------------
// _csram_mmap(): 
// ( Thanks to Valentin Egloff for helping me understand this sanity-checked
// mmap() routine ^_^ )
// -----------------------------------------------------------------------------
#define CSRAM_VECSIZE   16
#define CSRAM_BASE_ADDR 0x10000000
#define CSRAM_BASE_SIZE 8*1024
#define CSRAM_IMC_ADDR  0x80000000
#define CSRAM_IMC_SIZE  0x04000000

#define DIMA_WRITE_IS_ZERO_PADDED 0
#define DIMA_WRITE_IS_OVERWRITING 1

// QEMU insrtumentation counters
#define uncached_addr_addr (CSRAM_BASE_ADDR + CSRAM_BASE_SIZE)
#define uncached_size_addr (uncached_addr_addr + 4 )
#define to_counter_addr    (uncached_size_addr + 4 )

// DMU register interface
#define dima_src_addr_addr         (to_counter_addr            + 4)
#define dima_dst_addr_addr         (dima_src_addr_addr         + 4)
#define dima_stride_len_addr       (dima_dst_addr_addr         + 4)
#define dima_src_off_addr          (dima_stride_len_addr       + 4)
#define dima_dst_off_addr          (dima_src_off_addr          + 4)
#define dima_el_size_addr          (dima_dst_off_addr          + 4)
#define dima_start_addr            (dima_el_size_addr          + 4)
#define dima_done_addr             (dima_start_addr            + 4)

// BPF-specific registers
#define dmu_pattern1_addr          (dima_done_addr             + 4)
#define dmu_pattern2_addr          (dmu_pattern1_addr          + 4)
#define dmu_dram_region_width_addr (dmu_pattern2_addr          + 4)
#define dmu_seq_off_addr           (dmu_dram_region_width_addr + 4)

volatile int8_t   *_csram, *_csram_imc;
volatile uint32_t *to_counter, *uncached_addr, *uncached_size;
volatile uint32_t *dima_src_addr, *dima_dst_addr, *dima_src_off, *dima_dst_off;
volatile uint32_t *dima_el_size, *dima_stride_len, *dima_start, *dima_done;
volatile uint32_t *dmu_pattern1, *dmu_pattern2, *dmu_dram_region_width, *dmu_seq_off;

int8_t *_system_mmap(uint32_t addr, uint32_t size)
{
	uint32_t page_addr = (addr / sysconf(_SC_PAGE_SIZE)) * sysconf(_SC_PAGE_SIZE);
	uint32_t page_off  =  addr % sysconf(_SC_PAGE_SIZE);
	int8_t *base_addr = (int8_t *)mmap( (void *)addr,
			size,
			PROT_READ | PROT_WRITE | PROT_EXEC,
			MAP_SHARED | MAP_ANONYMOUS | MAP_FIXED,
			-1,
			0);
	if ((uint32_t)base_addr != (uint32_t)addr)
	{
		printf("Critical Error : got region address 0x%08x (expected 0x%08x), exiting.\n", (uint32_t)base_addr, (uint32_t)addr);
		exit(1);
	}
	//printf("0x%08x ==> 0x%08x + 0x%08x\n", addr, page_addr, page_off);
	return (int8_t *)base_addr;
}

void mmap_qemu_counters(void)
{
	//printf("Mapping DMU & Instrumentation registers...\n");
	uncached_addr          = (uint32_t *)_system_mmap(uncached_addr_addr, sizeof(uint32_t)*15);
	uncached_size          = (uint32_t *)uncached_size_addr;
	to_counter             = (uint32_t *)to_counter_addr;
	dima_src_addr          = (uint32_t *)dima_src_addr_addr;
	dima_dst_addr          = (uint32_t *)dima_dst_addr_addr;
	dima_src_off           = (uint32_t *)dima_src_off_addr;
	dima_dst_off           = (uint32_t *)dima_dst_off_addr;
	dima_el_size           = (uint32_t *)dima_el_size_addr;
	dima_stride_len        = (uint32_t *)dima_stride_len_addr;
	dima_start             = (uint32_t *)dima_start_addr;
	dima_done              = (uint32_t *)dima_done_addr;
	dmu_pattern1           = (uint32_t *)dmu_pattern1_addr;
	dmu_pattern2           = (uint32_t *)dmu_pattern2_addr;
	dmu_seq_off            = (uint32_t *)dmu_seq_off_addr;
	dmu_dram_region_width  = (uint32_t *)dmu_dram_region_width_addr;
	//printf("OK\n");
}

void mmap_qemu_csram(void) {
	//printf("Mapping C-SRAM storage & DMU register interface...\n");
	_csram     = _system_mmap(CSRAM_BASE_ADDR, CSRAM_BASE_SIZE);
	//printf("OK\n");
	//printf("Mapping C-SRAM instructions...\n");
	_csram_imc = _system_mmap(CSRAM_IMC_ADDR, CSRAM_IMC_SIZE );
	//printf("OK\n");
}

#endif
