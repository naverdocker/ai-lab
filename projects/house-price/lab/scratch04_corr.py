#!/usr/bin/env python3

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import subprocess

PROJECT = Path(__file__).resolve().parents[1]
PLOTS_PATH = PROJECT / "plots"
DATA_PATH = PROJECT / "data"
RAW_CSV = DATA_PATH / "raw.csv"
PLOT_PNG = PLOTS_PATH / "plot.png"
TCOL = "rent"

if __name__ == "__main__":

    # DAY 6 - 07Nov25 contd..

    df = pd.read_csv(RAW_CSV)

#    print(f"df.describe():\n", df.describe())

    # correlations
    print("\n---- correlations ----")
    corr = df.corr(numeric_only=True)
    target_corr = corr[TCOL].sort_values(ascending=False)
#    print("corr:\n", corr)
#    print("\ntarget_corr:\n", target_corr)

    top_pos_corr = target_corr.index[1]
    top_neg_corr = target_corr.index[-1]
    print()
#    print(f"Most positively correlated Attribute: {top_pos_corr} {target_corr[top_pos_corr]: .3f}")
#    print(f"Most negatively correlated Attribute: {top_neg_corr} {target_corr[top_neg_corr]: .3f}")

    plt.figure(figsize=(12,8))
    plt.imshow(corr, cmap="coolwarm", interpolation="nearest")
    plt.colorbar(label="Correlation coefficient")

    plt.savefig(PLOT_PNG)
    plt.close()

    subprocess.run(["wslview", PLOT_PNG])

    #plt.show()


