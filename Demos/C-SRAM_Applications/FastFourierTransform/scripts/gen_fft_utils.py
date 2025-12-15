#!/usr/bin/env python3
import os, sys, math, numpy as np
from datetime import datetime
now = datetime.now()

def fatalError(s):
    print(s)
    sys.exit(1)

def twiddle(n, precision=None):
    y = np.exp(-2 * np.pi * 1j / n)
    y = [np.real(y), np.imag(y)]
    if precision is not None:
        y[0] = np.round(y[0] * (1 << precision))
        y[1] = np.round(y[1] * (1 << precision))
    return y[0], y[1]

def twiddle2(x, n, precision=None):
    y = np.exp(-2 * np.pi * 1j * x / n)
    print("twiddle2(%d/%d)=%s" % (x, n , str(y)))
    y = [np.real(y), np.imag(y)]
    if precision is not None:
        y[0] = np.round(y[0] * (1 << precision))
        y[1] = np.round(y[1] * (1 << precision))
    return y[0], y[1]

def is_power_of_two(n):
    return (n & (n-1) == 0) and n != 0

if len(sys.argv) != 7:
    fatalError("USAGE : ./gen_fft_utils.py --8-bit [precision8] --16-bit [precision16] --length [sample_length]")
    sys.exit(1)

prec8 = None
prec16 = None
length = None

for i, arg in enumerate(sys.argv[1:]):
    if '--' in arg:
        if arg == '--8-bit':
            prec8 = int(sys.argv[i + 2])
        elif arg == '--16-bit':
            prec16 = int(sys.argv[i + 2])
        elif arg == '--length':
            length = int(sys.argv[i + 2])
        else:
            fatalError("Error, unrecognized flag %s" % arg)
for k, v in [['--prec8', prec8], ['--prec16', prec16], ['--length', length]]:
    if v is None:
        fatalError("Error, missing argument %s" % k)

if not(is_power_of_two(length)):
    printf("Error, max sample length is not a power of two, aborting.")
    sys.exit(1)

floor_bits = {
    8  : 8  - prec8 - 1,
    16 : 16 - prec16- 1
}

values_16bit  = range(1 << 16)
values_8bit   = range(1 << 8)
log_len = int(math.log2(length))
powers_of_two = [ 2**j for j in list(range(log_len + 1)) ][1:]
n1 = 1
n2 = length
while(n2 > n1):
    n1 = n1 << 1
    n2 = n2 >> 1
log_n1 = int(math.log2(n1))
log_n2 = int(math.log2(n2))
powers_of_two_n1 = [ 2**j for j in list(range(log_n1 + 1)) ][1:]
powers_of_two_n2 = [ 2**j for j in list(range(log_n2 + 1)) ][1:]

c_code = """
/**************************************************************** 
 * fft_utils.h :                                                  
 * - Header library to compute the Fast Fourier Transform. This   
 * file was generated using the gen_fft_utils.py script (if you    
 * were given the header without the aforementioned script, you   
 * should contact your correspondant about this issue).           
 * - Fixed-Point Precision : Q%d.%d / Q%d.%d
 * - Max. Supported Length : %d-values DFT (%d x %d)
 * - Generated on the date : %s
 *                                                                
 * - CEA Grenoble, do not distribute without prior autorisation.      
 ****************************************************************/

#ifndef _FFT_TOOLS_H
#define _FFT_TOOLS_H

#include <stdint.h>

#ifdef CPLX32
#define PRECISION_BITS %d
#else
#define PRECISION_BITS %d
#endif
#define K (1 << (PRECISION_BITS - 1))

#define fixed_to_flt(n) ((float)(n) / (float)(1 << PRECISION_BITS))
#define flt_to_fixed(n) (int)((n) * (float)(1 << PRECISION_BITS))

#define SAMPLE_LENGTH %d\n
""" % (floor_bits[8], prec8, floor_bits[16], prec16, length, n1, n2,
       now.strftime("%Y-%m-%d %H:%M:%S"), prec16, prec8, length)

def bit_reverse(n, width):
    b = '{:0{width}b}'.format(n, width=width)
    return int(b[::-1], 2)

c_code += """
#ifdef CPLX32

typedef int16_t data_t;
"""

c_code += "int16_t twiddle_[] = {0, 0, "

for i in powers_of_two:
    tr, ti = twiddle(i, prec16)
    c_code += "%d, %d, " % (tr, ti)
c_code = c_code[:-1] + "};\n\n"

c_code += """
#else
#ifdef CPLX16

typedef int8_t data_t;
"""

c_code += "int8_t twiddle_[] = {0, 0, "
print (powers_of_two)
for i in powers_of_two:
    tr, ti = twiddle(i, prec8)
    c_code += "%d, %d, " % (tr, ti)
c_code = c_code[:-1] + "};\n\n"

c_code += """
#else

typedef float data_t;

"""

c_code += "float twiddle_[] = {0.0, 0.0, "
for i in powers_of_two:
    tr, ti = twiddle(i)
    c_code += "%f, %f, " % (tr, ti)
c_code = c_code[:-1] + "};\n\n"

c_code += "float twiddle2_[] = {0.0, 0.0, "
for i in range(length):
    tr, ti = twiddle2(i+1, length)
    c_code += "%f, %f, " % (tr, ti)
c_code = c_code[:-1] + "};\n\n"

c_code += "#endif\n#endif\n\n"

c_code += "// Pre-computed Look-Up Table for the bit reverse\n"
c_code += "uint32_t bit_reverse_2_[] = {"
for value in range(n1):
    c_code += '%d,' % bit_reverse(value, n1.bit_length() - 1)
c_code = c_code[:-1] + "};\n\n"
c_code += "uint32_t bit_reverse_1_[] = {"
for value in range(n2):
    c_code += '%d,' % bit_reverse(value, n2.bit_length() - 1)
c_code = c_code[:-1] + "};\n\n"
c_code += "uint32_t bit_reverse_[] = {"
for value in range(length):
    c_code += '%d,' % bit_reverse(value, length.bit_length() - 1)
c_code = c_code[:-1] + "};\n\n"
c_code += "uint32_t dummy_[] = {"
for value in range(length):
    c_code += '%d,' % value
c_code = c_code[:-1] + "};\n\n"

c_code += """
typedef struct {
    data_t real;
    data_t imag;
} cplx_t;

#define cplx_new(a, b) (cplx_t){.real=(data_t)a, .imag=(data_t)b}

#define cplx_add(a, b)\
    (cplx_t){a.real+b.real , a.imag+b.imag}

#define cplx_sub(a, b)\
    (cplx_t){a.real-b.real , a.imag-b.imag}

#if defined(CPLX32) || defined(CPLX16)

// Fixed-point multipion without rounding
#define data_mul(a, b) ( ((a) * (b) + K) >> PRECISION_BITS )
// Fixed-point multiplication with rounding
#define data_mulr(a, b) ( ((a) * (b) + K) >> PRECISION_BITS )

#else

// Floating-point multiplication is always performed at the highest precision,
// the following macros are just to keep compatibility with cplx_mul()
#define data_mul(a, b) ((a) * (b))
#define data_mulr(a, b) ((a) * (b))

#endif

#if NO_ROUNDING

#define cplx_mul(a, b) (cplx_t)\\
{\\
    data_mul(a.real, b.real) - data_mul(a.imag, b.imag),\\
    data_mul(a.real, b.imag) + data_mul(a.imag, b.real)\\
}

#else

#define cplx_mul(a, b) (cplx_t)\\
{\\
    data_mulr(a.real, b.real) - data_mulr(a.imag, b.imag),\\
    data_mulr(a.real, b.imag) + data_mulr(a.imag, b.real)\\
}

#endif

#define cplx_eq(a, b) (((a).real == (b).real) && ((a).imag == (b).imag))

char *cplx_str_flt(cplx_t c)
{
    char *res = (char *)malloc(64 * sizeof(char));

    #if defined(CPLX32) || defined(CPLX16)
    float r = fixed_to_flt(c.real);
    float i = fixed_to_flt(c.imag);

    #else
    float r = c.real;
    float i = c.imag;

    #endif
    sprintf(res, "(%f%+fi)", r, i);
    return res;
}

char *cplx_str_fx(cplx_t c)
{
    char *res = (char *)malloc(64 * sizeof(char));
    #if defined(CPLX32) || defined(CPLX16)
    data_t r = c.real;
    data_t i = c.imag;
    #else
    int r = flt_to_fixed(c.real);
    int i = flt_to_fixed(c.imag);
    #endif
    sprintf(res, "(%d%+di)", r, i);
    return res;
}

#define twiddle(n) (cplx_new(twiddle_[2*n], twiddle_[2*n+1]))
#define twiddle2(n) (cplx_new(twiddle2_[2*n], twiddle2_[2*n+1]))

"""

c_code += "#endif\n\n"

os.makedirs("include", exist_ok=True)
fd = open("include/fft_utils.h", 'w')
fd.write(c_code)
fd.close()

