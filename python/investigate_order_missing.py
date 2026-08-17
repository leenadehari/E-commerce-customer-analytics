import pandas as pd
import os

DATA_PATH = r"C:\Users\leena\Downloads\archive"
orders = pd.read_csv(os.path.join(DATA_PATH, "olist_orders_dataset.csv"))

#Order status distribution
print("\nORDER STATUS DISTRIBUTION")
print(orders["order_status"].value_counts())

#Missing approved date by order status
print("\nMISSING APPROVED DATE BY ORDER STATUS")
approved_missing = (orders[orders["order_approved_at"].isna()]["order_status"].value_counts())
print(approved_missing)

#Missing carrier date by order status
print("\nMISSING CARRIER DELIVERY DATE BY ORDER STATUS")
carrier_missing = (orders[orders["order_delivered_carrier_date"].isna()]["order_status"].value_counts())
print(carrier_missing)

#Missing customer delivery date by order status
print("\nMISSING CUSTOMER DELIVERY DATE BY ORDER STATUS")
customer_delivery_missing = (orders[orders["order_delivered_customer_date"].isna()]["order_status"].value_counts())
print(customer_delivery_missing)

#Orders missing ANY delivery information
print("\nORDERS WITH MISSING DELIVERY INFORMATION")
delivery_columns = ["order_delivered_carrier_date","order_delivered_customer_date"]
missing_delivery = orders[orders[delivery_columns].isna().any(axis=1)]
print("Total orders with missing delivery information:",len(missing_delivery))
print("\nOrder status:")
print(missing_delivery["order_status"].value_counts())

#Cancelled orders with delivery dates
print("\nCANCELLED ORDERS WITH DELIVERY DATES")
cancelled = orders[orders["order_status"] == "canceled"]
print("Total cancelled orders:",len(cancelled))
print("Cancelled orders with customer delivery date:",cancelled["order_delivered_customer_date"].notna().sum())
print("Cancelled orders with carrier delivery date:",cancelled["order_delivered_carrier_date"].notna().sum())