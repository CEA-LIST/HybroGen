#!/usr/bin/env python3

from PIL import Image

def myexec(cmdAndArgs, doPrint = True, wdir=None, doExec = True, environ = None):
    if (doPrint):
        if wdir != None:
            print("-->cd %s"%(wdir))
        # if environ != None :
        #     for P in ("PATH", "LD_LIBRARY_PATH"):
        #         print("%s=%s"%(P, environ[P]))
        print("%s"%(" ".join(cmdAndArgs)))
    returncode = 0
    data = "Success"
    if doExec:
        process = subprocess.Popen(cmdAndArgs, cwd=wdir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env= environ)
        data = process.stdout.read()
        returncode = process.wait()
    else:
        returncode = 0
        data = b''
    if 0 == returncode:
        return data
    else:
        print("Error : %s"%data.decode ("utf8").split("\n"))
        # sys.exit(-1)
        return None

def save_pgm_ascii(image, path):
    """
    Sauvegarde une image PIL en format ASCII PGM (P2)
    """
    width, height = image.size
    pixels = list(image.getdata())

    with open(path, "w") as f:
        f.write("P2\n")
        f.write("# Created by script\n")
        f.write(f"{width} {height}\n")
        f.write("255\n")
        for i in range(height):
            row = pixels[i * width:(i + 1) * width]
            f.write(" ".join(map(str, row)) + "\n")

if __name__ == "__main__":
    import argparse, os, sys, subprocess
    parser = argparse.ArgumentParser(
        description="Redimensionne une image ou applique un filtre avec un exécutable externe."
    )
    parser.add_argument("--input_file",   help="Chemin vers l'image source PGM")
    parser.add_argument("--resize",       action="store_true", help="Resize images")
    parser.add_argument("--runner",       default="x", help="Émulateur (ex: qemu-aarch64)")
    parser.add_argument("--program",      help="Program a exécuter (ex: stencil.aarch64)")
    parser.add_argument("--filter_file",  help="Chemin vers le fichier de filtre PGM")
    parser.add_argument("--param",        help="Paramètre supplémentaire à passer à l'exécutable")
    parser.add_argument("--logFile",      help="Log filename")
    args = parser.parse_args()
    print (args)

    # Résolutions cibles
    resolutions = [ # Ordonnés par nombre de pixels !
        # https://upload.wikimedia.org/wikipedia/commons/0/0c/Vector_Video_Standards8.svg
        (320, 240),  # QVGA
        (640, 480),  # VGA
        (800, 600),  # SVGA
        (1024, 768), # XGA
        # (1280, 720),
        # (1366, 768),
        # (1440, 900),
        (1280, 960), # QuadVGA
        # (1600,  900),
        # (1680, 1050),
        (1600, 1200), # UXGA
        # (1920, 1080),
        (2048, 1536), # QXGA
    ]
    if args.resize:
        original_image = Image.open(args.input_file).convert("L")
        for width, height in resolutions:
            print(f"==> Redimension à {width}x{height}")
            outputFile = f'{args.input_file}_{width}x{height}'
            # Redimensionne
            resized_image = original_image.resize((width, height), Image.NEAREST)
            save_pgm_ascii(resized_image, outputFile)
            print (outputFile)
    else:
        filter_name = os.path.splitext(os.path.basename(args.filter_file))[0]  # ex: "FilterFloudeGauss3x3"
        log = []
        for width, height in resolutions:
            # Prépare les chemins de sortie
            output_path_1 = "./Sun_Filter.pgm"
            output_path_2 = "./Sun_H4Filter.pgm"
            inputFile = f'{args.input_file}_{width}x{height}'
            # Commande à exécuter
            if args.runner != "x":
                prefix = [args.runner, args.program,]
            else:
                prefix = [args.program,]
            cmd = prefix + [inputFile, output_path_1, output_path_2, args.filter_file, args.param ]
            result = myexec(cmd, doPrint = True)
            if None != result:
                rawResult = result.decode ("utf8").split("\n")[0]
                log.append(rawResult)
        with open(args.logFile, "a") as f:
            f.write("\n".join(log))
            f.write("\n")
        print (f"Results in {args.logFile}")
