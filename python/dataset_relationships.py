import pandas as pd
import os

# --------------------------------------------------
# 1. Dataset path
# --------------------------------------------------

DATA_PATH = r"C:\Users\leena\Downloads\archive"


# --------------------------------------------------
# 2. Load datasets
# --------------------------------------------------

customers = pd.read_csv(
    os.path.join(DATA_PATH, "olist_customers_dataset.csv")
)

orders = pd.read_csv(
    os.path.join(DATA_PATH, "olist_orders_dataset.csv")
)

order_items = pd.read_csv(
    os.path.join(DATA_PATH, "olist_order_items_dataset.csv")
)

products = pd.read_csv(
    os.path.join(DATA_PATH, "olist_products_dataset.csv")
)

sellers = pd.read_csv(
    os.path.join(DATA_PATH, "olist_sellers_dataset.csv")
)

payments = pd.read_csv(
    os.path.join(DATA_PATH, "olist_order_payments_dataset.csv")
)

reviews = pd.read_csv(
    os.path.join(DATA_PATH, "olist_order_reviews_dataset.csv")
)


print("=" * 70)
print("DATASET RELATIONSHIP & KEY VALIDATION")
print("=" * 70)


# --------------------------------------------------
# 3. Check primary key uniqueness
# --------------------------------------------------

print("\nPRIMARY KEY CHECK")
print("-" * 70)

print(
    "Customers - customer_id unique:",
    customers["customer_id"].is_unique
)

print(
    "Orders - order_id unique:",
    orders["order_id"].is_unique
)

print(
    "Products - product_id unique:",
    products["product_id"].is_unique
)

print(
    "Sellers - seller_id unique:",
    sellers["seller_id"].is_unique
)


# --------------------------------------------------
# 4. Customers -> Orders
# --------------------------------------------------

print("\nCUSTOMERS -> ORDERS")
print("-" * 70)

customer_ids = set(customers["customer_id"])

order_customer_ids = set(orders["customer_id"])

unmatched_customers = order_customer_ids - customer_ids

print(
    "Orders with customer IDs not found in customers:",
    len(unmatched_customers)
)


# --------------------------------------------------
# 5. Orders -> Order Items
# --------------------------------------------------

print("\nORDERS -> ORDER ITEMS")
print("-" * 70)

order_ids = set(orders["order_id"])

item_order_ids = set(order_items["order_id"])

unmatched_orders_in_items = item_order_ids - order_ids

print(
    "Order items with order IDs not found in orders:",
    len(unmatched_orders_in_items)
)


# --------------------------------------------------
# 6. Orders -> Payments
# --------------------------------------------------

print("\nORDERS -> PAYMENTS")
print("-" * 70)

payment_order_ids = set(payments["order_id"])

unmatched_orders_in_payments = payment_order_ids - order_ids

print(
    "Payments with order IDs not found in orders:",
    len(unmatched_orders_in_payments)
)


# --------------------------------------------------
# 7. Orders -> Reviews
# --------------------------------------------------

print("\nORDERS -> REVIEWS")
print("-" * 70)

review_order_ids = set(reviews["order_id"])

unmatched_orders_in_reviews = review_order_ids - order_ids

print(
    "Reviews with order IDs not found in orders:",
    len(unmatched_orders_in_reviews)
)


# --------------------------------------------------
# 8. Order Items -> Products
# --------------------------------------------------

print("\nORDER ITEMS -> PRODUCTS")
print("-" * 70)

product_ids = set(products["product_id"])

item_product_ids = set(order_items["product_id"])

unmatched_products = item_product_ids - product_ids

print(
    "Order items with product IDs not found in products:",
    len(unmatched_products)
)


# --------------------------------------------------
# 9. Order Items -> Sellers
# --------------------------------------------------

print("\nORDER ITEMS -> SELLERS")
print("-" * 70)

seller_ids = set(sellers["seller_id"])

item_seller_ids = set(order_items["seller_id"])

unmatched_sellers = item_seller_ids - seller_ids

print(
    "Order items with seller IDs not found in sellers:",
    len(unmatched_sellers)
)


# --------------------------------------------------
# 10. Display relationship structure
# --------------------------------------------------

print("\nRELATIONSHIP STRUCTURE")
print("-" * 70)

print("""
customers
    |
    | customer_id
    v
orders
    |
    | order_id
    +------------------+
    |                  |
    v                  v
order_items        payments
    |
    +------------------+
    |                  |
    v                  v
products           sellers

orders
    |
    v
reviews
""")


print("=" * 70)
print("RELATIONSHIP VALIDATION COMPLETED")
print("=" * 70)