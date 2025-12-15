/******************************************************************************/
/* pixmap.h :                                                                 */
/* - light-weight library to manipulate Portable aNyMap (.PNM) images.        */
/*   Variants P1 to P6 are supported.                                         */
/*   See https://www.jchr.be/python/pnm-pam.htm for more information          */
/* - Author : Kevin Mambu, CEA Grenoble, 2020                                 */
/******************************************************************************/

#ifndef _PIXMAP_H
#define _PIXMAP_H

#ifdef DEBUG
#define printf_(...) printf(__VA_ARGS__); fflush(stdout)
#else
#define printf_(...)
#endif

#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define BITS_PER_BYTE 8

enum error_codes {
	ERR_UNKNOWN_FORMAT = 1,
	ERR_FILE_NOT_FOUND,
	ERR_INVALID_MAGIC,
	ERR_UNSUPPORTED_MAGIC,
	ERR_INCORRECT_FORMAT,
	ERR_VALUE_IS_ZERO,
	ERR_VALUE_IS_OVERFLOW
};

typedef struct {
	uint64_t data_size;
	uint32_t width;
	uint32_t height;
	uint32_t max_val;
	uint8_t *data;
	uint8_t format;
	uint8_t is_image_16bit;
} PixMap;

enum image_format {
	ASCII_PBM = 1,
	ASCII_PGM,
	ASCII_PPM,
	BINARY_PBM,
	BINARY_PGM,
	BINARY_PPM
};

#define is_bitmap(f) ((f == ASCII_PBM) || (f == BINARY_PBM))
#define is_graymap(f) ((f == ASCII_PGM) || (f == BINARY_PGM))
#define is_pixmap(f) ((f == ASCII_PPM) || (f == BINARY_PPM))
#define is_legal(f)  ((f >= ASCII_PBM) && (f <= BINARY_PPM))
#define is_ascii(f)   (f <= ASCII_PPM)
#define is_binary(f)  (f >= BINARY_PBM)

#define pixmap_8bit_threshold  ((1 <<  8) - 1)
#define pixmap_16bit_threshold ((1 << 16) - 1)

#define isspace(c) ( (c == ' ') || (c == '\n') || (c == '\t') )

#define read_str(fd, buffer) do {\
	int x = 1;\
	read(fd, &buffer[0], 1);\
	while (!isspace(buffer[x-1])) {\
		read(fd, &buffer[x], 1);\
		x += 1;\
	}\
	buffer[x-1] = '\0';\
	lseek(fd, -1, SEEK_CUR);\
} while(0)

#define skip_whitespaces_and_comments(fd, buf) do {\
	int exit_loop = 0;\
	int is_comment = 0;\
	while(!exit_loop) {\
		read(fd, buf, 1);\
		if (isspace(*buf)) {\
			if (*buf == '\n') is_comment = 0;\
			continue;\
		} else {\
			if (is_comment ) continue;\
			if (*buf == '#') is_comment = 1;\
			else             exit_loop = 1;\
		}\
	}\
	lseek(fd, -1, SEEK_CUR);\
} while(0)

PixMap *pixmap_new(uint8_t format, uint32_t width, uint32_t height, uint32_t max_val)
{
	PixMap *p = (PixMap *)malloc(sizeof(PixMap));

	p->format = format;
	p->width = width;
	p->height = height;
	p->max_val = max_val;

	uint8_t is_image_16bit = (max_val > pixmap_8bit_threshold);
	p->is_image_16bit  = is_image_16bit;
	//
	// Data size is first assumed as an 8-bit image
	uint64_t data_size = width * height;
	if ((format == BINARY_PBM) || (format == ASCII_PBM)) {
		uint64_t data_size_ = (data_size / BITS_PER_BYTE); // 1 bit per pixel
		if (data_size % BITS_PER_BYTE)
			data_size_ += 1;
		data_size = data_size_;
	}
	if ((format == BINARY_PPM) || (format == ASCII_PPM))
		data_size *= 3;  // due to RGB encoding
	if (is_image_16bit)
		data_size *= 2;  // due to the image being 16-bit encoded
	p->data_size = data_size;

	p->data = (uint8_t *)malloc(data_size);
	return p;
}

PixMap *pixmap_load(const char *path)
{
	int fd;
	char buffer[100];
	int i, j, format;
	uint32_t width, height, max_val = 1;

	// Open the file using its path
	if ((fd = open(path, O_RDONLY)) == -1) {
		printf_("Critical Error : opening of image file failed\n");
		exit(ERR_FILE_NOT_FOUND);
	}
	printf_("Opened file %s\n", path);
	// Read pixmap signature (2 characters)
	read(fd, buffer, 2);
	if (buffer[0] != 'P') {
		printf_("Critical Error : incorrect magic number\n");
		exit(ERR_FILE_NOT_FOUND);
	}
	format = (uint32_t)buffer[1] - 48;
	if (!is_legal(format))
	{
		printf_("Critical Error : unsupported format P%c\n", buffer[1]);
		exit(ERR_UNSUPPORTED_MAGIC);
	}
	printf_("Image format is P%d\n", format);
	skip_whitespaces_and_comments(fd, buffer);
	// Read 'width' parameter
	read_str(fd, buffer);
	width = atoi(buffer);
	printf_("Width is %d\n", width);
	skip_whitespaces_and_comments(fd, buffer);
	// Read 'height' parameter
	read_str(fd, buffer);
	height = atoi(buffer);
	printf_("Height is %d\n", height);
	skip_whitespaces_and_comments(fd, buffer);
	// Read 'max_val' parameter for PGM / PPM formats
	if ((format != BINARY_PBM) && (format != ASCII_PBM)) {
		read_str(fd, buffer);
		max_val = atoi(buffer);
		if (max_val == 0) {
			printf_("Critical Error : max_val is zero-value.\n");
			exit(ERR_VALUE_IS_ZERO);
		}
		if (max_val > pixmap_16bit_threshold) {
			printf_("Critical Error : max_val exceeds 16 bits.\n");
			exit(ERR_VALUE_IS_ZERO);
		}
		skip_whitespaces_and_comments(fd, buffer);
	}
	printf_("Max value is %d\n", max_val);
	PixMap *pixmap  = pixmap_new(format, width, height, max_val);
	if(pixmap->is_image_16bit) {
		printf_("Image is 16-bit encoded\n");
	}
	printf_("Data Size is %lld bytes\n", pixmap->data_size);
	uint64_t data_size = pixmap->data_size;
	// If it's binary, a srtaightforward read() is enough
	if (is_binary(format))
	{
		read(fd, pixmap->data, data_size);
	}
	else
	{
		uint64_t nb_pixels = width * height, no_pixel = 0;
		if (format == ASCII_PBM)
		{
			for (i = 0; i < data_size; i += 1)
			{
				((uint8_t *)pixmap->data)[i] = 0;
				for (j = 7; j >= 0; j -= 1)
				{
					read_str(fd, buffer);
					((uint8_t *)pixmap->data)[i] |= ((uint8_t)atoi(buffer) << j);
					if (no_pixel == nb_pixels - 1)
						break;
					else
						skip_whitespaces_and_comments(fd, buffer);
					no_pixel += 1;
				}
			}
		}
		else
		{
			uint64_t nb_values;
			if (!pixmap->is_image_16bit) nb_values = data_size;
			else nb_values = data_size / 2;
			for (i = 0; i < nb_values; i += 1)
			{
				read_str(fd, buffer);
				if (pixmap->is_image_16bit)
					((uint16_t *)pixmap->data)[i] = (uint16_t)atoi(buffer);
				else
					((uint8_t *)pixmap->data)[i] = (uint8_t)atoi(buffer);
				if (i != nb_values - 1)
					skip_whitespaces_and_comments(fd, buffer);
			}
		}
	}
	close(fd);
	return pixmap;
}

void pixmap_save(PixMap *p, char *path)
{
	char mode[] = "0744";
	int fd = open(path, O_CREAT | O_RDWR);
	dprintf(fd, "P%d\n%d %d\n", p->format, p->width, p->height);
	if(!is_bitmap(p->format))
	{
		dprintf(fd, "%d\n", p->max_val);
	}
	write(fd, p->data, p->data_size);
	close(fd);
	chmod(path, strtol(mode, 0, 8));
}

void pixmap_free(PixMap *p) {
	free(p->data);
	free(p);
}

void pixmap_print(PixMap *p) {
	int i, j;
	uint64_t data_size = p->data_size;
	uint32_t width = p->width;
	if (is_bitmap(p->format))
	{
		printf_("Pixmap Bitmap Format:\n");
		uint64_t no_pixel = 0;
		for (i = 0; i < data_size; i += 1)
		{
			for (j = 7; j >= 0; j -= 1) {
				if(!(no_pixel % width) && (no_pixel))
					printf("\n");
				uint8_t pix = (p->data[i] & (1 << j)) != 0;
				printf("%d ", pix);
				no_pixel += 1;
			}
		}
	}
	else
	{
		printf_("Portable GrayMap/PixMap Format:\n");
		for (uint64_t i = 0; i < data_size; i += 1)
		{
			if (!(i % width) && (i != 0))
				printf("\n");
			printf("%d ", p->data[i]);
		}
	}
	printf("\n");
}

PixMap *pixmap_clone_empty(PixMap *p) {
	PixMap *m = pixmap_new(p->format, p->width, p->height, p->max_val);
	return m;
}

#endif

