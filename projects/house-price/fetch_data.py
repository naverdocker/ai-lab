#!/usr/bin/env python3

from pathlib import Path
from sklearn.datasets import fetch_california_housing
import sklearn
import pandas as pd
import hashlib, json, datetime
import argparse

PROJECT = Path(__file__).resolve().parent
DATA_DIR = PROJECT / "data"
RAW_CSV = DATA_DIR / "raw.csv"

def fetch_california_housing_to_csv(out_path: Path, overwrite: bool = False):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and not overwrite:
        print(f"{out_path} exists - use --force to overwrite")
        return out_path

    try:
        data = fetch_california_housing(as_frame=True)

    except ConnectionError as e:
        print("Network connection error while fetching dataset: ", e)
        raise

    except TimeoutError as e:
        print("Fetch request timed out: ", e)
        raise

    except OSError as e:
        print("File or OS-level error while writing dataset: ", e)
        raise

    except Exception as e:
        print("Unexpected error: ", e)
        raise

    df = data.frame.rename(columns={"MedHouseVal": "rent"})
    df.to_csv(out_path, index=False)

    # checksum + metadata
    sha256 = hashlib.sha256(out_path.read_bytes()).hexdigest()
    meta = {
            "name": "california_housing",
            "fetched_on_utc": datetime.datetime.utcnow().isoformat(),
            "rows": len(df),
            "cols": df.columns.tolist(),
            "sklearn_version": sklearn.__version__,
            "sha256": sha256
            }
    with open(out_path.parent / "DATASET_SOURCE.json", "w") as f:
        json.dump(meta, f, indent=2)
    print("Saved", out_path)

    return out_path

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
            description="Fetch the California Housing dataset and save it to data/raw.csv"
            )
    parser.add_argument(
            "--force",
            action="store_true",
            help="Overwrite data/raw.csv if it already exists"
            )
    args = parser.parse_args()
    #args.force = True

    fetch_california_housing_to_csv(RAW_CSV, overwrite=args.force)
