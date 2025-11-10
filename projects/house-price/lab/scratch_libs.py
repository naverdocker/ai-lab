import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


__all__ = ["os", "sys", "Path", "np", "pd", "plt"]

if __name__ == "__main__":
    print("scratch common loader")
