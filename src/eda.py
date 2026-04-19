import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

def perform_eda(df):
    print("\n📊 Dataset Info:")
    print(df.info())

    print("\n📊 Summary Statistics:")
    print(df.describe())

    plt.figure()
    df['Temperature'].hist()
    plt.title("Temperature Distribution")
    plt.xlabel("Temperature")
    plt.ylabel("Frequency")
    plt.show(block=False)
    plt.pause(2)
    plt.close()