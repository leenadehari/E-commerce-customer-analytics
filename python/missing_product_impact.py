import pandas as pd
import os

DATA_PATH = r"C:\Users\leena\Downloads\archive"
products = pd.read_csv(os.path.join(DATA_PATH, "olist_products_dataset.csv"))
order_items = pd.read_csv(os.path.join(DATA_PATH, "olist_order_items_dataset.csv"))

# Products with missing category
missing_category_products = products[products["product_category_name"].isna()]
missing_product_ids = set(missing_category_products["product_id"])

# Order items belonging to those products
affected_items = order_items[order_items["product_id"].isin(missing_product_ids)].copy()

print("BUSINESS IMPACT OF MISSING PRODUCT INFORMATION")

print("\nMissing-category products")
print("Number of affected products:",len(missing_category_products))
print("Number of affected order items:",len(affected_items))
print("Number of affected orders:",affected_items["order_id"].nunique())

# Revenue
print("\nVENUE IMPACT")
product_revenue = affected_items["price"].sum()
total_revenue = order_items["price"].sum()
revenue_percentage = (product_revenue / total_revenue * 100)
print(
    f"Revenue from missing-category products: "
    f"{product_revenue:,.2f}"
)
print(
    f"Total product revenue: "
    f"{total_revenue:,.2f}"
)
print(
    f"Revenue percentage: "
    f"{revenue_percentage:.2f}%"
)
# Quantity
print("\nSALES VOLUME IMPACT")
print(
    "Units/items sold:",
    len(affected_items)
)
print(
    "Total items sold:",
    len(order_items)
)
print(
    "Percentage of items:",
    f"{len(affected_items) / len(order_items) * 100:.2f}%"
)
