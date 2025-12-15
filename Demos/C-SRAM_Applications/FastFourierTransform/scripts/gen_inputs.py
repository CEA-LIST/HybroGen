#!/usr/bin/env python3
import os, sys, io
import numpy as np, matplotlib.pyplot as plt
from scipy import fft

def is_power_of_two(n):
    return (n & (n-1) == 0) and n != 0

def normalize_data(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

def rescale_data(data):
    return 2 * data - 1

def gen_random_sine(length):
    y = 0
    result = []
    for _ in range(length):
        result.append(y)
        y += np.random.normal(scale=1)
    return rescale_data(normalize_data(np.array(result)))

def write_data32(length, data, filename):
    raw_data = data.tobytes()
    raw_length = (length.to_bytes(4, sys.byteorder))
    with io.open(filename, 'wb') as fd:
        fd.write(raw_length)
        fd.write(raw_data)
    file_size = os.stat(filename).st_size
    data_size = len(raw_data) + len(raw_length)
    assert data_size == file_size,"Error : Data size and file size are different (%d != %d)" % (data_size + 4, file_size)

if len(sys.argv) != 3:
    print("USAGE : ./gen_inputs.py [size]")
    print("- Generates a sample file dft_input_{size}.sine, the according DFT dft_output_{size}.sine,")
    print("  and graphical representations of both signals in .jpg format")
    sys.exit(1)

length = int(sys.argv[1])
filename = sys.argv[2]

if not(is_power_of_two(length)):
    print("Error, sample length is not a power of two, aborting.")
    sys.exit(1)

x  = np.float32(gen_random_sine(length))

y  = fft(x)

y2 = []
real_y = np.real(y)
imag_y = np.imag(y)
for i in range(len(y)):
    y2 += [real_y[i] , imag_y[i]]
y2 = np.float32(y2)

dummy = np.array([7,42,123.456,456.789])

print(dummy)
raw_dummy = np.float32(dummy)

write_data32(len(raw_dummy), raw_dummy, "dummy.cplx")
write_data32(length, x, "%s.sine" % filename)
write_data32(length, y2, "%s.dft" % filename)

plt.plot(range(length), x)

plt.savefig("sine_%d.png" % length)

