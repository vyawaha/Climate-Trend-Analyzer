import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from src.data_loader import load_data, generate_sample_data
from src.preprocessing import clean_data
from src.eda import perform_eda
from src.trend_analysis import trend_analysis
from src.anomaly_detection import detect_anomalies
from src.forecasting import forecast
from src.visualization import plot_all

# Step 1: Generate dataset if not exists
file_path = "data/raw/climate_data.csv"
generate_sample_data(file_path)

# Step 2: Load data
df = load_data(file_path)

# Step 3: Clean data
df = clean_data(df)

# Step 4: EDA
perform_eda(df)

# Step 5: Trend analysis
df = trend_analysis(df)

# Step 6: Anomaly detection
df = detect_anomalies(df)

# Step 7: Forecast
forecast(df)

# Step 8: Visualization
plot_all(df)

print("\n✅ Project executed successfully!")

print("Step 1: Data Loaded")
print("Step 2: Cleaning Done")
print("Step 3: EDA Done")
print("Step 4: Trend Done")
print("Step 5: Anomaly Done")
print("Step 6: Forecast Done")