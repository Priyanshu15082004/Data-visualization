# Import necessary libraries
# !pip3 install mysql-connector-python faker pandas
import mysql.connector
from faker import Faker
import random
import pandas as pd

# Initialize Faker
faker = Faker()

# Create a connection to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='jatin...',
    database='ecommerce_analysis'
)

cursor = connection.cursor()

# Number of records to generate
num_customers = 100
num_products = 50
num_orders = 200

# Define limited lists for cities and products
cities = [
    'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
    'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'
]

product_names = [
    'Wireless Mouse', 'Bluetooth Headphones', '4K Monitor', 'Keyboard',
    'Smartphone', 'Laptop', 'Smartwatch', 'Webcam', 'External Hard Drive', 'USB Hub'
]

# 1. Generate fake data for customers
customer = []
for _ in range(num_customers):
    customer.append((
        faker.uuid4()[:4],
        faker.name(),
        random.choice(cities),  # Use limited set of cities
        faker.email(),
        faker.phone_number()[:15],
        faker.address().replace("\n", " "),
        faker.postcode()
    ))

# Insert customer data into the customer table
customer_query = """
INSERT INTO customer (customer_id, name, city, email, phone_no, address, pin_code)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
cursor.executemany(customer_query, customer)
connection.commit()

# 2. Generate fake data for products
categories = ['Electronics', 'Clothing', 'Books', 'Home & Kitchen', 'Toys']
sub_categories = {
    'Electronics': ['Computers', 'Mobile Phones', 'Cameras'],
    'Clothing': ['Men', 'Women', 'Kids'],
    'Books': ['Fiction', 'Non-Fiction', 'Educational'],
    'Home & Kitchen': ['Furniture', 'Kitchen Appliances', 'Decor'],
    'Toys': ['Action Figures', 'Board Games', 'Puzzles']
}

products = []
for _ in range(num_products):
    category = random.choice(categories)
    sub_category = random.choice(sub_categories[category])
    products.append((
        faker.uuid4()[:7],
        random.choice(product_names),  # Use limited set of product names
        category,
        sub_category,
        round(random.uniform(5.0, 500.0), 2),
        round(random.uniform(5.0, 500.0), 2),
        random.randint(1, 100)
    ))

# Insert product data into the product table
product_query = """
INSERT INTO product (product_id, product_name, category, sub_category, original_price, selling_price, stock)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
cursor.executemany(product_query, products)
connection.commit()

# Fetch product IDs for reference
product_ids = [p[0] for p in products]

# 3. Generate fake data for order details
orders = []
for _ in range(num_orders):
    customer_id = random.choice([c[0] for c in customer])
    product_id = random.choice(product_ids)
    quantity = random.randint(1, 10)
    # Find the price of the selected product
    product_price = next(p[5] for p in products if p[0] == product_id)
    total_price = round(product_price * quantity, 2)
    orders.append((
        customer_id,
        product_id,
        quantity,
        total_price,
        random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Cash']),
        faker.date_time_this_year(),
        random.choice(['Pending', 'Delivered', 'Canceled'])
    ))

# Insert order details data into the order_details table
order_query = """
INSERT INTO order_details (customer_id, product_id, quantity, total_price, payment_mode, order_date, order_status)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
cursor.executemany(order_query, orders)
connection.commit()

# Close the connection
cursor.close()
connection.close()

print("Fake data has been inserted into the database.")
