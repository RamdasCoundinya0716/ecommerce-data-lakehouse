import pandas as pd
import random
import numpy as np
from faker import Faker

# Initialize Faker and set seed for reproducibility
fake = Faker()
Faker.seed(0)
random.seed(0)

# Number of rows for each dataset
num_customers = 5000
num_products = 150
num_sales = 30000

# Generate Customers
def generate_customers(num_customers):
    customers = []
    for _ in range(num_customers):
        customers.append({
            "CustomerID": fake.unique.uuid4(),
            "Name": fake.name(),
            "Email": fake.email(),
            "Phone": fake.phone_number(),
            "Address": fake.address(),
            "JoinDate": fake.date_this_decade()
        })
    return pd.DataFrame(customers)

# Generate Products
def generate_products(num_products):
    products = []
    for _ in range(num_products):
        products.append({
            "ProductID": fake.unique.uuid4(),
            "Name": fake.word(),
            "Category": fake.word(),
            "Price": round(random.uniform(5.0, 500.0), 2)
        })
    return pd.DataFrame(products)

# Generate Sales
def generate_sales(num_sales, customers, products):
    sales = []
    for _ in range(num_sales):
        sales.append({
            "SaleID": fake.unique.uuid4(),
            "CustomerID": random.choice(customers["CustomerID"]),
            "ProductID": random.choice(products["ProductID"]),
            "Quantity": random.randint(1, 10),
            "TotalAmount": round(random.uniform(10.0, 1000.0), 2),
            "SaleDate": fake.date_this_year()
        })
    return pd.DataFrame(sales)

# Introduce 80-10-10 discrepancies
def introduce_discrepancies(df, numerical_columns):
    for col in numerical_columns:
        # Ensure column is cast to object to allow for mixed types
        df[col] = df[col].astype(object)

        # Get total number of rows
        total_rows = len(df)

        # Determine the number of rows for each case
        num_null = int(total_rows * 0.1)  # 10% null
        num_na = int(total_rows * 0.1)    # 10% "N/A"

        # Randomly select indices for nulls and "N/A"
        null_indices = random.sample(range(total_rows), num_null)
        na_indices = random.sample(
            [i for i in range(total_rows) if i not in null_indices], num_na
        )

        # Apply discrepancies
        df.loc[null_indices, col] = None
        df.loc[na_indices, col] = np.nan

    return df

# Generate Data
customers_df = generate_customers(num_customers)
products_df = generate_products(num_products)
sales_df = generate_sales(num_sales, customers_df, products_df)

# Introduce discrepancies in numerical fields
sales_df = introduce_discrepancies(sales_df, numerical_columns=["Quantity", "TotalAmount"])

# Save Data to CSV
filePath = "E:/Tech/Projects/Data Engineering Projects/ecommerce-data-lakehouse"
customers_df.to_csv(f"{filePath}/data/raw/customers.csv", index=False)
products_df.to_csv(f"{filePath}/data/raw/products.csv", index=False)
sales_df.to_csv(f"{filePath}/data/raw/sales.csv", index=False)