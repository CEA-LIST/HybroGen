#ifndef _SOFT_DIMA_H
#define _SOFT_DIMA_H

#include <stdbool.h>
#include <string.h>

#define DIMA_TRANSFER_TO_CSRAM 0
#define DIMA_TRANSFER_TO_MEM   1

int soft_dima_transfer(void *mem_addr, void *csram_addr, int length, int mem_stride, int csram_stride, bool to_mem);

int soft_dima_transfer(void *mem_addr, void *csram_addr, int length, int mem_stride, int csram_stride, bool to_mem)
{
	if (mem_stride == 1 && csram_stride == 1)
	{
		if(to_mem)
			memcpy(mem_addr, csram_addr, length);
		else
			memcpy(csram_addr, mem_addr, length);
	}
	else
	{
		for(int i = 0; i < length; i += 1)
		{
			if(to_mem)
				((char *)mem_addr)[i * mem_stride] = ((char *)csram_addr)[i * csram_stride];
			else
				((char *)csram_addr)[i * csram_stride] = ((char *)mem_addr)[i * mem_stride];
		}
	}
	if(to_mem)
		return length * mem_stride;
	else
		return length * csram_stride;
}
#endif
