import pandas as pd
import os

CLEANED_PATH = r"C:\Users\leena\Downloads\archive\cleaned"

datasets = {
    "customers": "customers_clean.csv",
    "orders": "orders_clean.csv",
    "order_items": "order_items_clean.csv",
    "payments": "payments_clean.csv",
    "reviews": "reviews_clean.csv",
    "products": "products_clean.csv",
    "sellers": "sellers_clean.csv",
    "geolocation": "geolocation_clean.csv",
    "category_translation": "category_translation_clean.csv"
}
#LOAD AND VALIDATE

for name, filename in datasets.items():
    file_path = os.path.join(CLEANED_PATH, filename)
    df = pd.read_csv(file_path)
    print(f"DATASET: {name.upper()}")

    # Shape
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    # Duplicate rows
    duplicate_count = df.duplicated().sum()
    print("Duplicate rows:", duplicate_count)

    # Missing values
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    print("\nRemaining missing values:")

    if missing.empty:
        print("None")
    else:
        print(missing)

    # Data types
    print("\nData types:")
    print(df.dtypes)

#SPECIFIC VALIDATION
print("SPECIFIC CLEANING VALIDATION")

# Reviews
reviews = pd.read_csv(os.path.join(CLEANED_PATH,"reviews_clean.csv"))
print("\nREVIEW VALIDATION")
print("Missing review titles:",reviews["review_comment_title"].isna().sum())
print("Missing review messages:",reviews["review_comment_message"].isna().sum())
print('"No comment" titles:',(reviews["review_comment_title"] == "No comment").sum())
print('"No comment" messages:',(reviews["review_comment_message"] == "No comment").sum())

# Products
products = pd.read_csv(os.path.join(CLEANED_PATH,"products_clean.csv"))
print("\nPRODUCT VALIDATION")
print("Missing categories:",products["product_category_name"].isna().sum())
print("Unknown categories:",(products["product_category_name"] == "Unknown").sum())
print("Missing product name lengths:",products["product_name_lenght"].isna().sum())
print("Missing description lengths:",products["product_description_lenght"].isna().sum())
print("Missing photo quantities:",products["product_photos_qty"].isna().sum())

# Orders
orders = pd.read_csv(os.path.join(CLEANED_PATH,"orders_clean.csv"))
print("\nORDER VALIDATION")
print("Missing approved dates:",orders["order_approved_at"].isna().sum())
print("Missing carrier delivery dates:",orders["order_delivered_carrier_date"].isna().sum())
print("Missing customer delivery dates:",orders["order_delivered_customer_date"].isna().sum())