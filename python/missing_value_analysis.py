import pandas as pd
import os

DATA_PATH = r"C:\Users\leena\Downloads\archive"

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

for name, filename in datasets.items():
    file_path = os.path.join(DATA_PATH, filename)
    df = pd.read_csv(file_path)
    missing_count = df.isnull().sum()
    missing_percentage = (missing_count / len(df) * 100).round(2)
    result = pd.DataFrame({
        "Missing Count": missing_count,
        "Missing %": missing_percentage
    })
    result = result[result["Missing Count"] > 0]
    print(f"Dataset: {name}")
    if result.empty:
        print("No missing values.")
    else:
        print(result)