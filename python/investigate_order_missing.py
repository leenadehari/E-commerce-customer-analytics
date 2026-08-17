import pandas as pd
import os

DATA_PATH = r"C:\Users\leena\Downloads\archive"

orders = pd.read_csv(
    os.path.join(DATA_PATH, "olist_orders_dataset.csv")
)

print("=" * 70)
print("INVESTIGATION OF MISSING ORDER DATES")
print("=" * 70)


# --------------------------------------------------
# 1. Order status distribution
# --------------------------------------------------

print("\n1. ORDER STATUS DISTRIBUTION")
print("-" * 70)

print(
    orders["order_status"].value_counts()
)


# --------------------------------------------------
# 2. Missing approved date by order status
# --------------------------------------------------

print("\n2. MISSING APPROVED DATE BY ORDER STATUS")
print("-" * 70)

approved_missing = (
    orders[orders["order_approved_at"].isna()]
    ["order_status"]
    .value_counts()
)

print(approved_missing)


# --------------------------------------------------
# 3. Missing carrier date by order status
# --------------------------------------------------

print("\n3. MISSING CARRIER DELIVERY DATE BY ORDER STATUS")
print("-" * 70)

carrier_missing = (
    orders[orders["order_delivered_carrier_date"].isna()]
    ["order_status"]
    .value_counts()
)

print(carrier_missing)


# --------------------------------------------------
# 4. Missing customer delivery date by order status
# --------------------------------------------------

print("\n4. MISSING CUSTOMER DELIVERY DATE BY ORDER STATUS")
print("-" * 70)

customer_delivery_missing = (
    orders[orders["order_delivered_customer_date"].isna()]
    ["order_status"]
    .value_counts()
)

print(customer_delivery_missing)


# --------------------------------------------------
# 5. Orders missing ANY delivery information
# --------------------------------------------------

print("\n5. ORDERS WITH MISSING DELIVERY INFORMATION")
print("-" * 70)

delivery_columns = [
    "order_delivered_carrier_date",
    "order_delivered_customer_date"
]

missing_delivery = orders[
    orders[delivery_columns].isna().any(axis=1)
]

print(
    "Total orders with missing delivery information:",
    len(missing_delivery)
)

print("\nOrder status:")
print(
    missing_delivery["order_status"].value_counts()
)


# --------------------------------------------------
# 6. Cancelled orders with delivery dates
# --------------------------------------------------

print("\n6. CANCELLED ORDERS WITH DELIVERY DATES")
print("-" * 70)

cancelled = orders[
    orders["order_status"] == "canceled"
]

print(
    "Total cancelled orders:",
    len(cancelled)
)

print(
    "Cancelled orders with customer delivery date:",
    cancelled["order_delivered_customer_date"].notna().sum()
)

print(
    "Cancelled orders with carrier delivery date:",
    cancelled["order_delivered_carrier_date"].notna().sum()
)


# --------------------------------------------------
# 7. Final summary
# --------------------------------------------------

print("\n" + "=" * 70)
print("INVESTIGATION COMPLETED")
print("=" * 70)