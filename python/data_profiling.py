import pandas as pd
import os

# --------------------------------------------------
# 1. Dataset path
# --------------------------------------------------

DATA_PATH = r"C:\Users\leena\Downloads\archive"


# --------------------------------------------------
# 2. Dataset files
# --------------------------------------------------

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


# --------------------------------------------------
# 3. Profile each dataset
# --------------------------------------------------

print("=" * 70)
print("PHASE 2 - DATA PROFILING")
print("=" * 70)

for name, filename in datasets.items():

    file_path = os.path.join(DATA_PATH, filename)

    df = pd.read_csv(file_path)

    print("\n" + "=" * 70)
    print(f"DATASET: {name.upper()}")
    print("=" * 70)

    # Shape
    print("\n1. Dataset Shape")
    print("Rows   :", df.shape[0])
    print("Columns:", df.shape[1])

    # Column names
    print("\n2. Columns")
    print(df.columns.tolist())

    # Data types
    print("\n3. Data Types")
    print(df.dtypes)

    # Missing values
    print("\n4. Missing Values")
    missing = df.isnull().sum()

    missing_percentage = (
        df.isnull().sum() / len(df) * 100
    ).round(2)

    missing_table = pd.DataFrame({
        "Missing Count": missing,
        "Missing %": missing_percentage
    })

    print(
        missing_table[missing_table["Missing Count"] > 0]
    )

    # Duplicate rows
    print("\n5. Duplicate Rows")
    print(df.duplicated().sum())

    # Unique values
    print("\n6. Unique Values")
    for column in df.columns:
        print(
            f"{column}: {df[column].nunique()}"
        )

    # Numerical summary
    print("\n7. Numerical Summary")

    numerical_columns = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    if len(numerical_columns) > 0:
        print(df[numerical_columns].describe())

    print("\n")


print("=" * 70)
print("DATA PROFILING COMPLETED")
print("=" * 70)