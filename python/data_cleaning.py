import pandas as pd
import os


# ==========================================================
# 1. PATHS
# ==========================================================

RAW_PATH = r"C:\Users\leena\Downloads\archive"

OUTPUT_PATH = r"C:\Users\leena\Downloads\archive\cleaned"

os.makedirs(OUTPUT_PATH, exist_ok=True)


# ==========================================================
# 2. LOAD DATASETS
# ==========================================================

print("=" * 70)
print("PHASE 2 - DATA CLEANING PIPELINE")
print("=" * 70)

customers = pd.read_csv(
    os.path.join(RAW_PATH, "olist_customers_dataset.csv")
)

orders = pd.read_csv(
    os.path.join(RAW_PATH, "olist_orders_dataset.csv")
)

order_items = pd.read_csv(
    os.path.join(RAW_PATH, "olist_order_items_dataset.csv")
)

payments = pd.read_csv(
    os.path.join(RAW_PATH, "olist_order_payments_dataset.csv")
)

reviews = pd.read_csv(
    os.path.join(RAW_PATH, "olist_order_reviews_dataset.csv")
)

products = pd.read_csv(
    os.path.join(RAW_PATH, "olist_products_dataset.csv")
)

sellers = pd.read_csv(
    os.path.join(RAW_PATH, "olist_sellers_dataset.csv")
)

geolocation = pd.read_csv(
    os.path.join(RAW_PATH, "olist_geolocation_dataset.csv")
)

category_translation = pd.read_csv(
    os.path.join(
        RAW_PATH,
        "product_category_name_translation.csv"
    )
)


print("\nAll datasets loaded successfully.")


# ==========================================================
# 3. CUSTOMERS
# ==========================================================

print("\nCleaning customers...")

customers = customers.drop_duplicates()

print(
    "Customers:",
    len(customers)
)


# ==========================================================
# 4. ORDERS
# ==========================================================

print("\nCleaning orders...")

orders = orders.drop_duplicates()

# Convert timestamp columns to datetime
order_date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in order_date_columns:
    orders[column] = pd.to_datetime(
        orders[column],
        errors="coerce"
    )

print(
    "Orders:",
    len(orders)
)


# ==========================================================
# 5. ORDER ITEMS
# ==========================================================

print("\nCleaning order items...")

order_items = order_items.drop_duplicates()

order_items["shipping_limit_date"] = pd.to_datetime(
    order_items["shipping_limit_date"],
    errors="coerce"
)

print(
    "Order items:",
    len(order_items)
)


# ==========================================================
# 6. PAYMENTS
# ==========================================================

print("\nCleaning payments...")

payments = payments.drop_duplicates()

print(
    "Payments:",
    len(payments)
)


# ==========================================================
# 7. REVIEWS
# ==========================================================

print("\nCleaning reviews...")

reviews = reviews.drop_duplicates()

reviews["review_comment_title"] = (
    reviews["review_comment_title"]
    .fillna("No comment")
)

reviews["review_comment_message"] = (
    reviews["review_comment_message"]
    .fillna("No comment")
)

reviews["review_creation_date"] = pd.to_datetime(
    reviews["review_creation_date"],
    errors="coerce"
)

reviews["review_answer_timestamp"] = pd.to_datetime(
    reviews["review_answer_timestamp"],
    errors="coerce"
)

print(
    "Reviews:",
    len(reviews)
)


# ==========================================================
# 8. PRODUCTS
# ==========================================================

print("\nCleaning products...")

products = products.drop_duplicates()

# Missing category
products["product_category_name"] = (
    products["product_category_name"]
    .fillna("Unknown")
)

# Missing descriptive information
products["product_name_lenght"] = (
    products["product_name_lenght"]
    .fillna(0)
)

products["product_description_lenght"] = (
    products["product_description_lenght"]
    .fillna(0)
)

products["product_photos_qty"] = (
    products["product_photos_qty"]
    .fillna(0)
)

print(
    "Products:",
    len(products)
)


# ==========================================================
# 9. SELLERS
# ==========================================================

print("\nCleaning sellers...")

sellers = sellers.drop_duplicates()

print(
    "Sellers:",
    len(sellers)
)


# ==========================================================
# 10. GEOLOCATION
# ==========================================================

print("\nCleaning geolocation...")

# Remove exact duplicate rows
geolocation = geolocation.drop_duplicates()

print(
    "Geolocation rows after removing exact duplicates:",
    len(geolocation)
)


# ==========================================================
# 11. CATEGORY TRANSLATION
# ==========================================================

print("\nCleaning category translation...")

category_translation = (
    category_translation
    .drop_duplicates()
)

print(
    "Category translation rows:",
    len(category_translation)
)


# ==========================================================
# 12. SAVE CLEANED DATA
# ==========================================================

print("\nSaving cleaned datasets...")

customers.to_csv(
    os.path.join(OUTPUT_PATH, "customers_clean.csv"),
    index=False
)

orders.to_csv(
    os.path.join(OUTPUT_PATH, "orders_clean.csv"),
    index=False
)

order_items.to_csv(
    os.path.join(OUTPUT_PATH, "order_items_clean.csv"),
    index=False
)

payments.to_csv(
    os.path.join(OUTPUT_PATH, "payments_clean.csv"),
    index=False
)

reviews.to_csv(
    os.path.join(OUTPUT_PATH, "reviews_clean.csv"),
    index=False
)

products.to_csv(
    os.path.join(OUTPUT_PATH, "products_clean.csv"),
    index=False
)

sellers.to_csv(
    os.path.join(OUTPUT_PATH, "sellers_clean.csv"),
    index=False
)

geolocation.to_csv(
    os.path.join(OUTPUT_PATH, "geolocation_clean.csv"),
    index=False
)

category_translation.to_csv(
    os.path.join(
        OUTPUT_PATH,
        "category_translation_clean.csv"
    ),
    index=False
)


# ==========================================================
# 13. FINAL SUMMARY
# ==========================================================

print("\n" + "=" * 70)
print("DATA CLEANING COMPLETED")
print("=" * 70)

print("\nCleaned files saved to:")
print(OUTPUT_PATH)

print("\nDataset sizes:")

print("Customers:", len(customers))
print("Orders:", len(orders))
print("Order Items:", len(order_items))
print("Payments:", len(payments))
print("Reviews:", len(reviews))
print("Products:", len(products))
print("Sellers:", len(sellers))
print("Geolocation:", len(geolocation))
print("Category Translation:", len(category_translation))

print("\n" + "=" * 70)