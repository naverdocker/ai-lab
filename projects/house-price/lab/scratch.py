#!/usr/bin/env python3

import sys
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from itertools import combinations

PROJECT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT / "data"
PLOT_DIR = PROJECT / "plots"
RAW_CSV = DATA_DIR / "raw.csv"
PLOT_PNG = PLOT_DIR / "plot.png"
TCOL = "rent"

if __name__ == "__main__":
    # DAY 7 - 10Nov25 (actually 11Nov post 00:00)
    df = pd.read_csv(RAW_CSV)

    # correlations
    print("---- correlations ----")
    corr = df.corr(numeric_only=True)
    target_corr = df.corr(numeric_only=True)[TCOL].sort_values(ascending=False)
#    print(target_corr)

    ####
    top_pos_corr = target_corr.index[1]
    top_neg_corr = target_corr.index[-1]
    print("top positive corr:", top_pos_corr)
    print("top negative corr:", top_neg_corr)

    ####
#    plt.figure(figsize=(12,8))
#    plt.imshow(corr, cmap="coolwarm", interpolation="nearest")
#    plt.colorbar(label="Correlation coefficient")
#    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
#    plt.yticks(range(len(corr.columns)), corr.columns)
#    plt.title(f"Correlation of each row with {TCOL}")
#    plt.tight_layout()
#    plt.show()

    ####
#    plt.figure(figsize=(12,8))
#    plt.bar(target_corr.index, target_corr.values)
#    plt.xticks(rotation=90)
#    plt.ylabel("Correlation coefficinet")
#    plt.title(f"Correlation of each feature with {TCOL}")
#    plt.tight_layout()
#    plt.show()

    ####
#    plt.figure(figsize=(12,8))
#    plt.subplot(1,2,1)
#    plt.scatter((df[top_pos_corr]), df[TCOL], s=10, alpha=0.5)
#    plt.xlabel(top_pos_corr); plt.ylabel(TCOL)
#    plt.title(f"{top_pos_corr} vs {TCOL}")

#    plt.subplot(1,2,2)
#    plt.scatter(df[top_neg_corr], df[TCOL], s=10, alpha=0.5)
#    plt.xlabel(top_neg_corr); plt.ylabel(TCOL)
#    plt.title(f"{top_neg_corr} vs {TCOL}")

#    plt.tight_layout()
#    plt.show()

    ####
#    print("\nHighly correlated feature pairs (|r|) > 0.8:")
#    for a, b in combinations(corr.columns, 2):
#        r = corr.loc[a, b]
#        if abs(r) > 0.8 and a!= b:
#            print(f"{a:15s} {b:15s} {r:6.3f}")
#
#    ####
#    ####
#    plt.figure(figsize=(12,8))
#    sns.heatmap(corr, cmap="coolwarm", annot=False, center=0)
#    plt.title("Feature Correlation Matrix")
#    plt.tight_layout()
#    plt.show()

    ####
    """
    target_corr = corr[TCOL].drop(TCOL).sort_values(ascending=False)
    topn = target_corr.head(10)
    plt.figure(figsize=(6,4))
    sns.barplot(x=topn.values, y=topn.index)
    plt.title(f"Top correlations with {TCOL}")
    plt.xlabel("correlation coefficient")
    plt.tight_layout()
    plt.show()
    """

    ####
    high_pairs = []
    for a, b in combinations(df.columns, 2):
        r = corr.loc[a, b]
        if abs(r) > 0.8 and a != TCOL and b != TCOL:
            high_pairs.append((a, b,c)

