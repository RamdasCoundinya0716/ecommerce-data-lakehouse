import pandas as pd
import random
from faker import Faker

fake = Faker()

# Set random seed for reproducibility
random.seed(42)
Faker.seed(42)

# Number of records
num_customers = 5000
num_products = 150
num_sales = 30000

# Generate Customer Data
customers = []
for _ in range(num_customers):
    customers.append({
        "CustomerID": fake.uuid4(),
        "Name": fake.name(),
        "Email": fake.email(),
        "SignUpDate": fake.date_between(start_date='-2y', end_date='today'),
        "Country": fake.country(),
        "Age": random.randint(18, 70)
    })
customers_df = pd.DataFrame(customers)

# Generate Product Data
categories = ['Electronics', 'Clothing', 'Home Appliances', 'Books', 'Toys']
products = []
for _ in range(num_products):
    products.append({
        "ProductID": fake.uuid4(),
        "ProductName": fake.word().capitalize(),
        "Category": random.choice(categories),
        "Price": round(random.uniform(5, 500), 2),
        "Stock": random.randint(10, 200)
    })
products_df = pd.DataFrame(products)

# Generate Sales Data
sales = []
for _ in range(num_sales):
    customer = random.choice(customers)
    product = random.choice(products)
    quantity = random.randint(1, 5)
    sales.append({
        "OrderID": fake.uuid4(),
        "CustomerID": customer["CustomerID"],
        "OrderDate": fake.date_time_between(start_date='-1y', end_date='now'),
        "ProductID": product["ProductID"],
        "Category": product["Category"],
        "Price": product["Price"],
        "Quantity": quantity,
        "TotalAmount": round(product["Price"] * quantity, 2),
        "PaymentMethod": random.choice(["Credit Card", "PayPal", "Debit Card", "Net Banking"])
    })
sales_df = pd.DataFrame(sales)

# Save to CSV
customers_df.to_csv("E:/Tech/Projects/Data Engineering Projects/ecommerce-data-lakehouse/data/raw/customers.csv", index=False)
products_df.to_csv("E:/Tech/Projects/Data Engineering Projects/ecommerce-data-lakehouse/data/raw/products.csv", index=False)
sales_df.to_csv("E:/Tech/Projects/Data Engineering Projects/ecommerce-data-lakehouse/data/raw/sales.csv", index=False)

print("Data generated and saved as CSV files!")