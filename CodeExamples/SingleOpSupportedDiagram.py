import datetime
import json
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def display_results_table(data, operations, vLens, wLens,archName,axToFill):

    # Nombre de colonnes
    n_w = len(wLens)
    n_v = len(vLens)

    # Dimensions
    op_width = 2.0
    cell_width = 0.8
    row_height = 0.45

    header_height = row_height
    vlen_height = row_height

    total_width = op_width + n_v * n_w * cell_width
    total_height = (
        vlen_height
        + header_height
        + len(operations) * row_height
    )


    axToFill.set_xlim(0, total_width)
    axToFill.set_ylim(0, total_height)
    axToFill.axis("off")

    # --------------------------------------------------
    # Ligne vLen
    # --------------------------------------------------

    y = total_height - vlen_height

    # Cellule "Operation"
    axToFill.add_patch(
        plt.Rectangle(
            (0, y - header_height),
            op_width,
            vlen_height + header_height,
            fill=False,
            linewidth=1
        )
    )

    axToFill.text(
        op_width / 2,
        y - header_height / 2,
        "Operation",
        ha="center",
        va="center",
        fontweight="bold"
    )

    # Groupes vLen
    for i, vLen in enumerate(vLens):

        x = op_width + i * n_w * cell_width
        width = n_w * cell_width

        axToFill.add_patch(
            plt.Rectangle(
                (x, y),
                width,
                vlen_height,
                fill=False,
                linewidth=1
            )
        )

        axToFill.text(
            x + width / 2,
            y + vlen_height / 2,
            f"vLen = {vLen}",
            ha="center",
            va="center",
            fontweight="bold"
        )

    # --------------------------------------------------
    # Ligne wLen
    # --------------------------------------------------

    y = total_height - vlen_height - header_height

    for i, wLen in enumerate(
        wLen
        for _ in vLens
        for wLen in wLens
    ):

        x = op_width + i * cell_width

        axToFill.add_patch(
            plt.Rectangle(
                (x, y),
                cell_width,
                header_height,
                fill=False,
                linewidth=1
            )
        )

        axToFill.text(
            x + cell_width / 2,
            y + header_height / 2,
            str(wLen),
            ha="center",
            va="center",
            fontsize=10,
            fontweight="bold"
        )

    # --------------------------------------------------
    # Lignes des opérations
    # --------------------------------------------------

    for row, operation in enumerate(operations):

        y = (
            total_height
            - vlen_height
            - header_height
            - (row + 1) * row_height
        )

        # Nom de l'opération
        axToFill.add_patch(
            plt.Rectangle(
                (0, y),
                op_width,
                row_height,
                fill=False,
                linewidth=1
            )
        )

        axToFill.text(
            op_width / 2,
            y + row_height / 2,
            operation,
            ha="center",
            va="center",
            fontsize=10
        )

        # Résultats
        col = 0

        for vLen in vLens:

            for wLen in wLens:

                x = op_width + col * cell_width

                success = data.get(
                    (operation, (wLen, vLen))
                )
                color = '0'
                if success=="SUCCESS":
                    color = 'g'
                elif success=="FAIL":
                    color = 'r'
                else:
                    color = 'c'
                axToFill.add_patch(
                    plt.Rectangle(
                        (x, y),
                        cell_width,
                        row_height,
                        facecolor=color,
                        edgecolor='k',
                        fill=True,
                        linewidth=1
                    )
                )
                col += 1
    axToFill.set_title('Supported Operation on ' + archName)


def generate_figure(filename,archName,axToFill):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            operators = data["operator"]

        opp = []
        wLens = set()
        vLens = set()
        results = {}
        for category, operations in operators.items():
            for operation, tests in operations.items():
                opp.append(operation)
                print(f"\n===== {category}/{operation} =====")

                for test in tests:
                    wLens.add(test["wLen"])
                    vLens.add(test["vLen"])
                    result = test["results"][0]
                    results[(operation, (test["wLen"],test["vLen"]))] = result["success"]


        opp = sorted(set(opp))
        wLens = sorted(wLens)
        vLens = sorted(vLens)

        display_results_table(results,opp,vLens,wLens,archName,axToFill)

    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        return -1
    except PermissionError as e:
        print(f"ERROR: {e}")
        return -2
    except json.JSONDecodeError as e:
        print(f"ERROR: JSON invalide : {e}")
        return -3
    except Exception as e:
        print(f"ERROR inattendue : {e}")
        return -99
    

if __name__ == "__main__":
    import sys, subprocess, argparse, os
    from CCode import CCodeValue
    from CCode import CCodeAddress
    sys.path.append("..")
    from SwConfig import SwConfig
    config = SwConfig()

    parser = argparse.ArgumentParser()

    
    parser.add_argument('-a',   '--arch',     nargs="+",    default=config.getKeys(), help='Architecture name list')
    parser.add_argument('-f',   '--fuse',action='store_true', help='Everything on the same figure')
    parser.add_argument('-o', '--open', help='Open diagram after generating them')
    parser.add_argument('-v', '--verbose', help='Verbose mode for every result')
    #parser.add_argument('',)
    a = parser.parse_args()

    commit = subprocess.check_output(
        ["git", "rev-parse", "--short", "HEAD"],
        text=True
    ).strip()
    if len(a.arch) > 1:
        fig,axs = plt.subplots(len(a.arch))
        for i in range(0,len(a.arch)):
            generate_figure("RegressionSingleOp-" + a.arch[i] + ".json",a.arch[i],axs[i])
            for spine in axs[i].spines.values():
                spine.set_visible(True)
                spine.set_linewidth(2)

        green_patch = mpatches.Patch(color='g',label='Supported')
        red_patch = mpatches.Patch(color='r',label='Has to be supported but Not working')
        cyan_patch = mpatches.Patch(color='c',label='Not Supported')
        fig.legend(
            handles=[green_patch, red_patch, cyan_patch],
            loc='lower center',
            ncols=3,
            shadow=True,
            fancybox=True,
            title="Legend"
        )    
    else:
        fig,ax = plt.subplots()
        generate_figure("RegressionSingleOp-" + a.arch[0] + ".json",a.arch[0],ax)
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_linewidth(2)

        green_patch = mpatches.Patch(color='g',label='Supported')
        red_patch = mpatches.Patch(color='r',label='Has to be supported but Not working')
        cyan_patch = mpatches.Patch(color='c',label='Not Supported')
        fig.legend(
            handles=[green_patch, red_patch, cyan_patch],
            loc='lower center',
            ncols=3,
            shadow=True,
            fancybox=True,
            title="Legend"
        )

    plt.show()