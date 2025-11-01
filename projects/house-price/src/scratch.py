#!/usr/bin/env python3

import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

PROJECT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT / "data" / "raw.csv"

data = fetch_california_housing(as_frame=True)
df = data.frame

df = df.rename(columns={"MedHouseVal": "rent"})

DATA_PATH.parent.mkdir(exist_ok=True, parents=True)
df.to_csv(DATA_PATH, index=False)

#print(f"Saved {DATA_PATH} with shape {df.shape}")
#print()
