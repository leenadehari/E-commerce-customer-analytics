import pandas as pd
import os

#Dataset path
DATA_PATH = r"C:\Users\leena\Downloads\archive"

#Dataset files
datasets = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "category_translation": "product_category_name_translation.csv"
}

#Profile each dataset
print("DATA PROFILING")

for name, filename in datasets.items():
    file_path = os.path.join(DATA_PATH, filename)
    df = pd.read_csv(file_path)

    # Shape
    print("\nDataset Shape")
    print("Rows   :", df.shape[0])
    print("Columns:", df.shape[1])

    # Column names
    print("\nColumns")
    print(df.columns.tolist())

    # Data types
    print("\nData Types")
    print(df.dtypes)

    # Missing values
    print("\nMissing Values")
    missing = df.isnull().sum()
    missing_percentage = (df.isnull().sum() / len(df) * 100).round(2)
    missing_table = pd.DataFrame({"Missing Count": missing,"Missing %": missing_percentage})
    print(missing_table[missing_table["Missing Count"] > 0])

    # Duplicate rows
    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    # Unique values
    print("\nUnique Values")
    for column in df.columns:
        print(
            f"{column}: {df[column].nunique()}"
        )
    # Numerical summary
    print("\nNumerical Summary")
    numerical_columns = df.select_dtypes(include=["int64", "float64"]).columns
    if len(numerical_columns) > 0:
        print(df[numerical_columns].describe())