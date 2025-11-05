#!/usr/bin/env python3

import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# -----------------------------
# CONFIG
# -----------------------------
PROJECT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT / "data"
RAW_CSV = DATA_DIR / "raw.csv"
TARGET_COL = "rent"

def debug_vars():
    print(f"project: {PROJECT}")
    print(f"data_dir: {DATA_DIR}")
    print(f"raw_csv: {RAW_CSV}")
    print(f"target_col: {TARGET_COL}")


# -----------------------------
# LOAD DATA
# -----------------------------
def load_data(path=RAW_CSV):
    df = pd.read_csv(path)
    #print(f"✅ Loaded {len(df)} rows")
    return df


# -----------------------------
# QUICK EDA
# -----------------------------
def quick_glance(df):
    print("\n📊 Basic Info: df.info()")
    print(df.info())
    print("\n🔍 Sample Rows: df.head()")
    print(df.head())
    print("\n📈 Summary: df.describe()")
    print(df.describe())


# -----------------------------
# PREPROCESS (very basic)
# -----------------------------
def preprocess(df):
    df = df.dropna(subset=[TARGET_COL])
    df = df.select_dtypes(include=[np.number])
    return df


# -----------------------------
# TRAIN SIMPLE MODEL
# -----------------------------
def quick_model(df):
    x = df.drop(columns=[TARGET_COL])
    y = df[TARGET_COL]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"\n 💡 RMSE: {rmse:.2f}")
    return model


# -----------------------------
# MAIN FLOW
# -----------------------------
if __name__ == "__main__":

    df = load_data()
    assert TARGET_COL in df.columns, f"Target column '{TARGET_COL}' not found"

    print("<<")

#    debug_vars()


    # DAY 3 - 03Nov25
#    print(f"\n------\n------\ndf.cloumns:\n\n{df.columns}")
#    print(f"\n------\n------\ndf.dtypes:\n\n{df.dtypes}")
#    print(f"\n------\n------\ndf.info():\n"); df.info()
#    print(f"\n------\n------\ndf.describe(include='all'):\n\n", df.describe(include='all'))
#    print(f"\n------\n------\ndf.head():\n\n{df.head(25)}")


    # DAY 4 - 04Nov25
#    fn = "df.columns.tolist()"; print(f"\n{fn}:\n", eval(fn))
#    fn = "df.head()"; print(f"\n{fn}:\n", eval(fn))
#    fn = "df.tail()"; print(f"\n{fn}:\n", eval(fn))
#    fn = "df.corr(numeric_only=True)[TARGET_COL].sort_values(ascending=False)"; print(f"\n{fn}:\n", eval(fn))

    # testing df.corr
#    fn = "df.corr()"; print(f"\n{fn}:\n", eval(fn))
#    fn = "df.corr()[TARGET_COL]"; print(f"\n{fn}:\n", eval(fn))
#    fn = "df.corr()[TARGET_COL].sort_values"; print(f"\n{fn}:\n", eval(fn))
#    fn = "df.corr()[TARGET_COL].sort_values(ascending=False)"; print(f"\n{fn}:\n", eval(fn))

    # dataset exploration
#    fn = "(df.isna())"; print(f"\n{fn}:\n", eval(fn))
#    fn = "(df.isna().sum() / len(df)).sort_values(ascending=False)"; print(f"\n{fn}:\n", eval(fn))


#    fn = "df.describe(include=[np.number])"; print(f"\n{fn}:\n", eval(fn))
#    fn = "df.nlargest(5, TARGET_COL)[[TARGET_COL, 'MedInc', 'Latitude', 'Longitude']]"; print(f"\n{fn}:\n", eval(fn))
#    fn = "df.nsmallest(5, TARGET_COL)[[TARGET_COL, 'MedInc', 'Latitude', 'Longitude']]"; print(f"\n{fn}:\n", eval(fn))

    ## pausing dataset exploation here to take a quick refresher crash course on numpy and pandas

    #df.plot.scatter(x="Longitude", y="Latitude", c=TARGET_COL, cmap="viridis", s=10)

    # DAY 5 - 05Nov25
    # continuing in new scratch.py


    print(">>")

#    model = quick_model(df)
#    print("\n✅ Done")

