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

    # DAY 5 - 05Nov25
    df = pd.read_csv(RAW_CSV)

#    print(df.shape)
#    print(df.columns)
#    print(df.dtypes)
#    df.info()

#    print(df.isna().sum() / len(df)).sort_values(ascending=False)

#    print(df.describe(include=[np.number]).T)

#    corr = df.corr(numeric_only=True)[TCOL].sort_values(ascending=False); print(corr, "\n")

#    df.hist(figsize=(12, 8), bins=60)
#    plt.tight_layout()
#    plt.show()

#    df.plot.scatter(
#            x="Longitude", y="Latitude", c=TCOL,
#            cmap="viridis", s=10, figsize=(8,6)
#            )
#    plt.show()

#    print(df.nlargest(5, TCOL)[[TCOL, "MedInc"]])
#    print(df.nsmallest(5, TCOL)[[TCOL, "MedInc"]])

    print(df.groupby(pd.cut(df["MedInc"], bins=5))[TCOL].mean())
