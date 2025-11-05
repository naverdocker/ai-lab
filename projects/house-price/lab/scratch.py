#!/usr/bin/env python3

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


PROJECT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT / "data"
RAW_CSV = DATA_DIR / "raw.csv"
TCOL = "rent"


# -----------------------------
# MAIN FLOW
# -----------------------------
if __name__ == "__main__":

    # DAY 5 - 05Nov25 contd..
    df = pd.read_csv(RAW_CSV)

    pd.options.display.width = 120

    # missing values (absolute and percentage)
    print("\n---- missing values (absolute & percentage) ----")
    miss = df.isna().sum()
    print(pd.concat([miss, (miss/len(df)).round(2)], axis=1).rename(columns={0: "missing", 1: "percentage"}))

    # memory usage
    print("\n---- dtypes / memory usage ----")
    print(df.dtypes, "\n")
    print((df.memory_usage(deep=True).sum() / (1024**2)).round(2), "mb")


