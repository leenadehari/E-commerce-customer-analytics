import pandas as pd
import os

# Path to raw dataset folder
DATA_PATH = r"C:\Users\leena\Downloads\archive"

print("=" * 60)
print("E-COMMERCE DATASET OVERVIEW")
print("=" * 60)

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

    print("\n" + "-" * 60)
    print(f"File: {file}")
    print("-" * 60)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

print("\n" + "=" * 60)
print("DATASET CHECK COMPLETED")
print("=" * 60)