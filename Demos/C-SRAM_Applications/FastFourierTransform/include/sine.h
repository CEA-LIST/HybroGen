#ifndef _SINE_H
#define _SINE_H

#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

#include <fft_utils.h>

typedef struct {
	uint32_t length;
	cplx_t *data;
} Sine1D;

typedef struct {
	uint32_t width;
	uint32_t height;
	cplx_t *data;
} Sine2D;

Sine1D *CreateSine1D(uint32_t length)
{
	Sine1D *res = (Sine1D *)malloc(sizeof(Sine1D));
	res->length = length;
	res->data = (cplx_t *)malloc(sizeof(cplx_t) * length);
	return res;
}

Sine2D *CreateSine2D(uint32_t width, uint32_t height)
{
	Sine2D *res = (Sine2D *)malloc(sizeof(Sine2D));
	res->width = width;
	res->height = height;
	res->data = (cplx_t *)malloc(sizeof(cplx_t) * width * height);
	return res;
}

Sine2D *CreateSine2D_2(Sine2D *src)
{
	return CreateSine2D(src->width, src->height);
}

Sine1D *ReadInputSine1D(char *filename)
{
	int fd;
	uint32_t length;
	float tmp;
	Sine1D *res;
	fd = open(filename, O_RDONLY);
	read(fd, &length, 4);
	res = CreateSine1D(length);
	for (int i = 0; i < length; i += 1)
	{
		read(fd, &tmp, sizeof(float));
#if defined(CPLX32) || defined(CPLX16)
		data_t tmp2 = flt_to_fixed(tmp);
		res->data[i] = cplx_new(tmp2, 0);
#else
		res->data[i] = cplx_new(tmp, 0);
#endif
	}
	close(fd);
	return res;
}

Sine2D *ReadInputSine2D(char *filename)
{
	int fd;
	uint32_t length, width, height;
	float tmp;
	Sine2D *res;
	fd = open(filename, O_RDONLY);
	read(fd, &length, 4);
	width = 1;
	height = length;
	while (height > width)
	{
		width = width << 1;
		height = height >> 1;
	}
	res = CreateSine2D(width, height);
	for (int i = 0; i < length; i += 1)
	{
		read(fd, &tmp, sizeof(float));
#if defined(CPLX32) || defined(CPLX16)
		data_t tmp2 = flt_to_fixed(tmp);
		res->data[i] = cplx_new(tmp2, 0);
#else
		res->data[i] = cplx_new(tmp, 0);
#endif
	}
	close(fd);
	return res;
}

#define PRINT_AS_FIXED 0
#define PRINT_AS_FLOAT 1
void PrintSine1D(Sine1D *sine, int as_float)
{
	printf("[");
	uint32_t length = sine->length;
	for(int i = 0; i < length; i += 1)
	{
		if (as_float)
			printf("%s", cplx_str_flt(sine->data[i]));
		else
			printf("%s", cplx_str_fx(sine->data[i]));
		if (i != length-1)
			printf(", ");
	}
	printf("]\n");
}

void PrintSine2D(Sine2D *sine, int as_float)
{
	printf("[");
	uint32_t length = sine->width * sine->height;
	for(int i = 0; i < length; i += 1)
	{
		if (as_float)
			printf("%s", cplx_str_flt(sine->data[i]));
		else
			printf("%s", cplx_str_fx(sine->data[i]));
		if (i != length-1)
			printf(", ");
	}
	printf("]\n");
}

void WriteSine1DFile(Sine1D *sine, char *filename)
{
	char mode[] = "0644";
	int fd = open(filename, O_CREAT | O_RDWR);
	write(fd, &sine->length, sizeof(sine->length));
	for(int x = 0; x < sine->length; x += 1)
	{
	#if defined(CPLX32) || defined(CPLX16)
		data_t r_ = (sine->data[x]).real;
		data_t i_ = (sine->data[x]).imag;
		float r = fixed_to_flt(r_);
		float i = fixed_to_flt(i_);
	#else
		float r = (sine->data[x]).real;
		float i = (sine->data[x]).imag;
	#endif
		write(fd, &r, sizeof(float));
		write(fd, &i, sizeof(float));
	}
	write(fd, &sine->data, sizeof(cplx_t) * sine->length);
	close(fd);
	chmod(filename, strtol(mode, 0, 8));
}

Sine2D *TransposeSine2D(Sine2D *src)
{
	uint32_t width = src->width, height = src->height;
	Sine2D *res = CreateSine2D(height, width);
	for (int i = 0; i < height; i += 1)
	{
		for (int j = 0; j < width; j += 1)
		{
			res->data[j * height + i] = src->data[i * width + j];
		}
	}
	return res;
}
#endif

