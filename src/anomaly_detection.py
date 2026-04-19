import matplotlib
matplotlib.use('TkAgg')
import os

import matplotlib.pyplot as plt
def detect_anomalies(df):
    df = df.copy()

    mean = df['Temperature'].mean()
    std = df['Temperature'].std()

    df['Anomaly'] = (abs(df['Temperature'] - mean) > 2 * std)

    print("\n⚠️ Anomalies Detected:")
    print(df[df['Anomaly'] == True].head())

    return df

    print("\n⚠️ Anomalies Detected:")
    print(df[df['Anomaly'] == True])
    df[df['Anomaly']].to_csv("outputs/tables/anomalies.csv", index=False)

    import os

def detect_anomalies(df):
    df = df.copy()

    mean = df['Temperature'].mean()
    std = df['Temperature'].std()

    df['Anomaly'] = (abs(df['Temperature'] - mean) > 2 * std)

    os.makedirs("outputs/tables", exist_ok=True)
    df[df['Anomaly']].to_csv("outputs/tables/anomalies.csv", index=False)

    print("\n⚠️ Anomalies saved to outputs/tables/anomalies.csv")

    return df
    df[df['Anomaly']].to_csv("outputs/tables/anomalies.csv", index=False)