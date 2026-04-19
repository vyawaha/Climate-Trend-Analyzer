import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LinearRegression
import numpy as np
def forecast(df):
    df = df.copy()

    df['Year'] = df['Date'].dt.year

    X = df[['Year']]
    y = df['Temperature']

    model = LinearRegression()
    model.fit(X, y)

    future_years = pd.DataFrame({'Year': [2030, 2040, 2050]})
    predictions = model.predict(future_years)
   
    print("\n🔮 Future Temperature Predictions:")
    for year, pred in zip(future_years['Year'], predictions):
        print(f"{year}: {round(pred,2)} °C")