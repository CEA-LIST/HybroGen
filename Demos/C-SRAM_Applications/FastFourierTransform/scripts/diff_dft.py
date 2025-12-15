#!/usr/bin/env python3

import os, sys, io, numpy as np

def read_dft(filename):
    with io.open(filename, 'rb') as fd:
        raw_data = fd.read()
    length = int.from_bytes(raw_data[0:4], sys.byteorder)
    data = np.frombuffer(raw_data[4:], dtype='float32')
    return length, data[:length]

if len(sys.argv) != 4:
    print("USAGE : ./diff_dft.py [baseline_dft] [candidate_dft] [max_err_margin]")
    print("        - max_err_margin in the range [0, 1[")
    sys.exit(1)

baseline = sys.argv[1]
candidate = sys.argv[2]
tol_err_margin = float(sys.argv[3])
assert (tol_err_margin >= 0.0 and tol_err_margin < 1.0)

b_length, b_dft = read_dft(baseline)
c_length, c_dft = read_dft(candidate)

print(b_dft)
print(c_dft)

assert (b_length == c_length)

print("* Comparing %s to %s" % (candidate, baseline))
rmse = np.sqrt(((b_dft - c_dft) ** 2).mean())

rmseNOK = rmse > tol_err_margin

print("  - Tolerated error margin is %f" % tol_err_margin)
print("  - RMSE is %f (%sPASSED)" % (rmse, "NOT " if rmseNOK else ""))

sys.exit()

