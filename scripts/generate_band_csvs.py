import pandas as pd
import os
from datetime import datetime

# Load NSE data
source_file = "sec_list_14052025.csv"
df = pd.read_csv(source_file)

# Get today's date in YYYY-MM-DD
today = datetime.today().strftime("%Y-%m-%d")

# Ensure output directory exists
output_folder = "data"
os.makedirs(output_folder, exist_ok=True)

# Loop through each stock
for _, row in df.iterrows():
    symbol = row['symbol'].strip()
    band = row['band']

    # Skip missing or non-numeric bands
    if pd.isna(band):
        continue

    # Output file path
    output_file = os.path.join(output_folder, f"{symbol}.csv")

    # Check if this file exists and today's data already added
    if os.path.exists(output_file):
        existing = pd.read_csv(output_file)
        if today in existing['time'].values:
            continue
        new_row = pd.DataFrame([[today, band]], columns=['time', 'value'])
        updated = pd.concat([existing, new_row])
    else:
        updated = pd.DataFrame([[today, band]], columns=['time', 'value'])

    # Save CSV
    updated.to_csv(output_file, index=False)
