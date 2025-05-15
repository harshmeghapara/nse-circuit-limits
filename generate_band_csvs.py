import pandas as pd
import os

# Define the path to the source file
source_file = "sec_list_today.csv"  # Make sure this file is in the root folder

# Check if the source file exists
if not os.path.exists(source_file):
    print(f"Error: The file '{source_file}' does not exist in the current directory.")
    exit()

# Read the CSV file with the stock data
df = pd.read_csv(source_file)

# Ensure the 'symbol' column exists
if 'symbol' not in df.columns:
    print("Error: 'symbol' column not found in the source CSV.")
    exit()

# Create the 'data' folder if it doesn't exist
data_folder = 'data'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# Iterate through each stock symbol in the dataframe
for index, row in df.iterrows():
    stock_symbol = row['symbol']
    band = row['band']  # Assuming 'band' column contains the price band information
    file_name = f"{stock_symbol}.csv"
    file_path = os.path.join(data_folder, file_name)
    
    # Create a DataFrame for this stock with a sample value (for example, today's date and price band)
    stock_data = pd.DataFrame({
        'time': [pd.to_datetime('today').strftime('%Y-%m-%d')],
        'value': [band]  # Use the band or any other relevant value here
    })
    
    # Write the stock data to a CSV file
    stock_data.to_csv(file_path, index=False)
    print(f"Generated: {file_path}")

print("All files have been generated successfully!")
