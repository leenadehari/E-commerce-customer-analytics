import pandas as pd
import os

# Path to raw dataset folder
DATA_PATH = r"C:\Users\leena\Downloads\archive"

print("E-COMMERCE DATASET OVERVIEW")

# Get all CSV files
files = [
    file for file in os.listdir(DATA_PATH)
    if file.endswith(".csv")
]

print(f"\nTotal CSV files found: {len(files)}")

# Check each dataset
for file in sorted(files):
    file_path = os.path.join(DATA_PATH, file)
    df = pd.read_csv(file_path)

    print(f"File: {file}")

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())
