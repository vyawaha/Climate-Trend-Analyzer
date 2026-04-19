import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

plt.switch_backend('TkAgg')

def trend_analysis(df):
    df = df.copy()

    df['Rolling_Mean_Temp'] = df['Temperature'].rolling(window=12).mean()
    df['Rolling_Mean_Rain'] = df['Rainfall'].rolling(window=12).mean()

    return df