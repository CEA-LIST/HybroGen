#!/usr/bin/env python

import pandas as pd
from multiprocessing import Pool
from matplotlib import pyplot as plt
import os, sys, csv, subprocess
from tabulate import tabulate

architectures = {
    "riscv_scalar_gcc" :
    {
        "sim_cmd": "qim --forward-pid --no-csram",
        "binary":"ImageDiff_c_riscv.x"
    },
    "riscv_cxram_gcc" :
    {
        "sim_cmd": "qim --forward-pid",
        "binary":"ImageDiff_c_cxram.x"
    },
    "riscv_cxram_h2" :
    {
        "sim_cmd": "qim --forward-pid",
        "binary":"ImageDiff_h2_cxram.x"
    },
}

baseline = "riscv_cxram_gcc"
metrics = ["CPU_CYCLES", "CPU_INSNS", "MEM_LOADS", "MEM_STORES", "ENERGY_COST"]

image_sizes = ["16x16", "32x32", "50x50", "100x100",
               "320x240", "640x480", "1280x720",
               "1920x1080", "3840x2160"]


def bash_cmd(cmd):
    return os.system(cmd)

def bash_cmd_silent(cmd):
    return os.system(cmd+"> /dev/null 2>&1")

def run_simulation(obj):
    # Extraction of run info
    res = obj['res']
    sim = obj['sim_cmd']
    b = obj['binary']
    suffix = "%s_%s" % (b, res)
    # Benchmark-dependant part
    cmd = """
          convert -resize %s TestImages/a.ppm a_%s.pgm && \
          convert -resize %s TestImages/b.ppm b_%s.pgm && \
          %s -o %s --run %s a_%s.pgm b_%s.pgm c_%s.pgm
          """ % (res, suffix, res, suffix, sim, suffix, b, suffix, suffix, suffix)
    # Benchmark-independant part
    child = subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    child.communicate()
    ret = child.returncode
    if ret != 0:
        return -2
    return suffix

def load_csv(suffix):
    try:
        df = pd.read_csv(str(suffix)+".csv", sep=";", index_col=0).transpose(copy=True)
        return df
    except:
        return -1

def check_output(obj):
    cPID = list(obj.keys())[0]
    bPID = obj[cPID]
    ret = os.system("cmp c_%s.pgm c_%s.pgm" % (str(cPID), str(bPID)))
    return (ret == 0)

print("* Cleaning work directory")
ret = bash_cmd_silent("make clean")
if (ret != 0):
    print("* Error when running 'make', aborting.")
    sys.exit(1)
with Pool(len(image_sizes)) as P:
    for arch, o in architectures.items():
        print("* Architecture is %s" % arch)
        sim = o['sim_cmd']
        b = o['binary']
        print("* Building binary '%s'..." % b)
        ret = bash_cmd_silent("make %s" % b)
        if (ret != 0):
            print("* Failed. Aborting.")
            sys.exit(1)
        print("* OK")
        thread_data = [{"binary":b,"sim_cmd":sim,"res":s} for s in image_sizes]
        print("* Running simulations...")
        suffixes = P.map(run_simulation, thread_data)
        if suffixes.count(-1):
            i = suffixes.index(-1)
            print("* At least one run failed (%s). Aborting." % image_sizes[i])
            print(suffixes)
            sys.exit(1)
        print("OK")
        o['suffixes'] = suffixes
        print("* Loading CSV data...")
        dframes = P.map(load_csv, suffixes)
        for i, dframe in enumerate(dframes):
            if not isinstance(dframe, pd.DataFrame):
                print("* At least one run failed (%s). Aborting." % image_sizes[i])
                sys.exit(1)
        print("OK")
        stats = pd.concat(dframes)
        stats["resolution"] = image_sizes
        stats = stats.set_index("resolution")
        o['stats'] = stats
        print(stats.transpose())
        print("Done")

candidates = list(architectures.keys())
candidates.remove(baseline)

for candidate in candidates:
    print("* Checking outputs for '%s'..." % candidate)
    P = Pool(len(image_sizes))
    c_suffixes = architectures[candidate]['suffixes']
    b_suffixes = architectures[baseline]['suffixes']
    suffixes = [{c_suffixes[i]:b_suffixes[i]} for i in range(len(image_sizes))]
    resOK = P.map(check_output, suffixes)
    if resOK.count(0):
        i = resOK.index(0)
        print("* At least one run failed (%s). Aborting." % image_sizes[i])
        print(resOK)
        print(suffixes)
        sys.exit(1)

print("* Generating performance comparison")
print("  Evaluation metrics are : %s\n" % ", ".join(metrics))
writer = pd.ExcelWriter("Statistics.xlsx")
txt = open("Statistics.txt", 'w')
for candidate in candidates:
    s = "* Evaluating '%s' vs '%s':" % (candidate, baseline)
    print(s)
    txt.write(s + "\n")
    baseline_df = architectures[baseline]['stats'][metrics]
    candidate_df = architectures[candidate]['stats'][metrics]
    relative_df = (candidate_df - baseline_df) / baseline_df
    relative_df = relative_df.applymap("{:+.2%}".format)
    df_txt = tabulate(relative_df, headers=metrics, tablefmt="psql")
    print(df_txt)
    txt.write(df_txt + "\n\n")
    relative_df.to_excel(writer, sheet_name=candidate)
writer.save()
txt.close()
os.system("make clean")

