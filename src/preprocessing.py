import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

import pandas as pd

def clean_data(df):
    df = df.copy()

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna()

    df = df.sort_values(by='Date')

    return df