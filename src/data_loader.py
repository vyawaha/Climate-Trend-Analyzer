import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import os

def generate_sample_data(path):
    if os.path.exists(path):
        return

    dates = pd.date_range(start="2000-01-01", periods=300, freq='ME')
    
    temperature = 25 + np.sin(np.arange(300)/12) * 2 + np.random.normal(0, 1, 300)
    rainfall = 100 + np.cos(np.arange(300)/12) * 20 + np.random.normal(0, 5, 300)

    df = pd.DataFrame({
        "Date": dates,
        "Temperature": temperature,
        "Rainfall": rainfall
    })

    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)


def load_data(path):
    df = pd.read_csv(path)
    return df