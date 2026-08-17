import pandas as pd
import os

DATA_PATH = r"C:\Users\leena\Downloads\archive"

#Load datasets
customers = pd.read_csv(os.path.join(DATA_PATH, "olist_customers_dataset.csv"))
orders = pd.read_csv(os.path.join(DATA_PATH, "olist_orders_dataset.csv"))
order_items = pd.read_csv(os.path.join(DATA_PATH, "olist_order_items_dataset.csv"))
products = pd.read_csv(os.path.join(DATA_PATH, "olist_products_dataset.csv"))
sellers = pd.read_csv(os.path.join(DATA_PATH, "olist_sellers_dataset.csv"))
payments = pd.read_csv(os.path.join(DATA_PATH, "olist_order_payments_dataset.csv"))
reviews = pd.read_csv(os.path.join(DATA_PATH, "olist_order_reviews_dataset.csv"))

#Check primary key uniqueness
print("\nPRIMARY KEY CHECK")
print("Customers - customer_id unique:",customers["customer_id"].is_unique)
print("Orders - order_id unique:",orders["order_id"].is_unique)
print("Products - product_id unique:",products["product_id"].is_unique)
print("Sellers - seller_id unique:",sellers["seller_id"].is_unique)

#Customers -> Orders
print("\nCUSTOMERS -> ORDERS")
customer_ids = set(customers["customer_id"])
order_customer_ids = set(orders["customer_id"])
unmatched_customers = order_customer_ids - customer_ids
print("Orders with customer IDs not found in customers:",len(unmatched_customers))

#Orders -> Order Items
print("\nORDERS -> ORDER ITEMS")
order_ids = set(orders["order_id"])
item_order_ids = set(order_items["order_id"])
unmatched_orders_in_items = item_order_ids - order_ids
print("Order items with order IDs not found in orders:",len(unmatched_orders_in_items))

#Orders -> Payments
print("\nORDERS -> PAYMENTS")
payment_order_ids = set(payments["order_id"])
unmatched_orders_in_payments = payment_order_ids - order_ids
print("Payments with order IDs not found in orders:",len(unmatched_orders_in_payments))

#Orders -> Reviews
print("\nORDERS -> REVIEWS")
review_order_ids = set(reviews["order_id"])
unmatched_orders_in_reviews = review_order_ids - order_ids
print("Reviews with order IDs not found in orders:",len(unmatched_orders_in_reviews))

#Order Items -> Products
print("\nORDER ITEMS -> PRODUCTS")
product_ids = set(products["product_id"])
item_product_ids = set(order_items["product_id"])
unmatched_products = item_product_ids - product_ids
print("Order items with product IDs not found in products:",len(unmatched_products))

#Order Items -> Sellers
print("\nORDER ITEMS -> SELLERS")
seller_ids = set(sellers["seller_id"])
item_seller_ids = set(order_items["seller_id"])
unmatched_sellers = item_seller_ids - seller_ids
print("Order items with seller IDs not found in sellers:",len(unmatched_sellers))