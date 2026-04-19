import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
import matplotlib.pyplot as plt

def plot_all(df):
    # Temperature trend
    plt.figure()
    plt.plot(df['Date'], df['Temperature'], label="Temperature")
    plt.plot(df['Date'], df['Rolling_Mean_Temp'], label="Rolling Mean")
    plt.legend()
    plt.title("Temperature Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Rainfall trend
    plt.figure()
    plt.plot(df['Date'], df['Rainfall'], label="Rainfall")
    plt.plot(df['Date'], df['Rolling_Mean_Rain'], label="Rolling Mean")
    plt.legend()
    plt.title("Rainfall Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Anomalies
    anomalies = df[df['Anomaly'] == True]

    plt.figure()
    plt.plot(df['Date'], df['Temperature'], label="Temperature")
    plt.scatter(anomalies['Date'], anomalies['Temperature'], label="Anomalies")
    plt.legend()
    plt.title("Anomaly Detection")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(2)
    plt.close()
def plot_all(df):
    os.makedirs("outputs/graphs", exist_ok=True)

    # Temperature trend
    plt.figure()
    plt.plot(df['Date'], df['Temperature'], label="Temperature")
    plt.plot(df['Date'], df['Rolling_Mean_Temp'], label="Rolling Mean")
    plt.legend()
    plt.title("Temperature Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/graphs/temperature_trend.png")
    plt.close()

    # Rainfall trend
    plt.figure()
    plt.plot(df['Date'], df['Rainfall'], label="Rainfall")
    plt.plot(df['Date'], df['Rolling_Mean_Rain'], label="Rolling Mean")
    plt.legend()
    plt.title("Rainfall Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/graphs/rainfall_trend.png")
    plt.close()

    # Anomalies
    anomalies = df[df['Anomaly'] == True]

    plt.figure()
    plt.plot(df['Date'], df['Temperature'], label="Temperature")
    plt.scatter(anomalies['Date'], anomalies['Temperature'], label="Anomalies")
    plt.legend()
    plt.title("Anomaly Detection")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/graphs/anomaly_detection.png")
    plt.close()
    plt.savefig("outputs/graphs/temp_trend.png")