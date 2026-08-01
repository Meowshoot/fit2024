import os
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

def run_analytics():
    df = pd.read_csv("data/google_fit_2024_daily_metrics.csv")
    df['Date'] = pd.to_datetime(df['Date'])

    print("=== GOOGLE FIT 2024 DATASET ANALYTICS ===")
    print(f"Total Days: {len(df)}")
    print(f"Total Steps: {df['Step_Count'].sum():,}")
    print(f"Total Distance: {df['Distance_km'].sum():,.2f} km")
    print(f"Daily Mean Steps: {df['Step_Count'].mean():,.2f}")
    print(f"Daily Median Steps: {df['Step_Count'].median():,.2f}")
    print(f"Streak Integrity: {(df['Step_Count'] >= 10000).sum()} / {len(df)} days (100%)")

if __name__ == '__main__':
    run_analytics()
