#!/usr/bin/env python3

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing


PROJECT = Path(__file__).resolve().parents[1]
#DATA_RAW = PROJECT / "data" / "raw.csv"
RESULTS = PROJECT / "results"
PLOTS = RESULTS / "plots"
PLOTS.mkdir(parents=True, exist_ok=True)

# fetch raw data
data = fetch_california_housing(as_frame=True)
df = data.frame
df = df.rename(columns={"MedHouseVal": "rent"})
#DATA_RAW.parent.mkdir(exist_ok=True, parents=True)
#df.to_csv(DATA_RAW, index=False)

# ---- first exploration ----
#def exp_peek():


print(f"Saved {DATA_RAW} with shape {df.shape}")
#print()
