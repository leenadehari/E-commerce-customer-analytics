import pandas as pd
import os

DATA_PATH = r"C:\Users\leena\Downloads\archive"

products = pd.read_csv(
    os.path.join(DATA_PATH, "olist_products_dataset.csv")
)

print("=" * 70)
print("INVESTIGATION OF PRODUCT MISSING VALUES")
print("=" * 70)


# --------------------------------------------------
# 1. Products missing category
# --------------------------------------------------

missing_category = products[
    products["product_category_name"].isna()
]

print("\n1. PRODUCTS MISSING CATEGORY")
print("-" * 70)

print("Number of products:", len(missing_category))


# --------------------------------------------------
# 2. Check other missing fields in those products
# --------------------------------------------------

print("\n2. MISSING VALUES AMONG PRODUCTS WITH NO CATEGORY")
print("-" * 70)

print(
    missing_category.isnull().sum()
)


# --------------------------------------------------
# 3. Products missing physical dimensions
# --------------------------------------------------

print("\n3. PRODUCTS MISSING PHYSICAL DIMENSIONS")
print("-" * 70)

dimension_columns = [
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

missing_dimensions = products[
    products[dimension_columns].isnull().any(axis=1)
]

print(
    "Number of products:",
    len(missing_dimensions)
)

print("\nMissing values:")
print(
    missing_dimensions[dimension_columns].isnull().sum()
)


# --------------------------------------------------
# 4. Display affected product IDs
# --------------------------------------------------

print("\n4. PRODUCTS WITH MISSING CATEGORY")
print("-" * 70)

print(
    missing_category[
        [
            "product_id",
            "product_category_name",
            "product_name_lenght",
            "product_description_lenght",
            "product_photos_qty"
        ]
    ].head(20)
)


# --------------------------------------------------
# 5. Check whether missing-category products
#    appear in order_items
# --------------------------------------------------

order_items = pd.read_csv(
    os.path.join(DATA_PATH, "olist_order_items_dataset.csv")
)

used_product_ids = set(order_items["product_id"])

missing_category_used = missing_category[
    missing_category["product_id"].isin(used_product_ids)
]

print("\n5. MISSING-CATEGORY PRODUCTS USED IN ORDERS")
print("-" * 70)

print(
    "Products with missing category that appear in orders:",
    len(missing_category_used)
)


print("\n" + "=" * 70)
print("PRODUCT MISSING-VALUE INVESTIGATION COMPLETED")
print("=" * 70)