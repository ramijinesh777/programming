"""1. Connect to a MySQL or PostgreSQL database using SQLAlchemy and pandas, then use 
pd.read_sql() to load the entire 'restaurants' table (imagine Zomato backend) into a 
DataFrame and display the first 5 rows."""

import pandas as pd
from sqlalchemy import create_engine

# MySQL database connection
username = "root"
password = "Mysql12345"
host = "localhost"
port = 3306
database = "zomato_db"

# Create SQLAlchemy engine
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# Load entire restaurants table
df = pd.read_sql("SELECT * FROM restaurants", engine)

# Display first 5 rows
print(df.head())

"""2. Use pd.read_sql_query() to fetch only the 'name' and 'rating' columns from a 'movies' 
table (think BookMyShow-like data) where rating is above 8, and print the resulting DataFrame.
Hint:Write a custom SQL SELECT query as the first argument to pd.read_sql_query()."""    

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# MySQL database connection
username = "root"
password = "Mysql12345"
host = "localhost"
port = 3306
database = "zomato_db"

# Create connection
connection_url = URL.create(
    drivername="mysql+pymysql",
    username=username,
    password=password,
    host=host,
    port=port,
    database=database
)

engine = create_engine(connection_url)

# SQL query
query = """
SELECT name, rating
FROM movies
WHERE rating > 8
"""

# Execute query and store result in DataFrame
df = pd.read_sql_query(query, engine)

# Print result
print(df)

"""3. Read a JSON dataset from the URL https://jsonplaceholder.typicode.com/users using pandas, 
convert it into a DataFrame, and print the usernames column.
Hint : Use pd.read_json() directly with the URL."""

import pandas as pd
url = "https://jsonplaceholder.typicode.com/users"
df = pd.read_json(url)
print(df)
print(df["username"])


"""4. You have two CSV files: 'orders.csv' (order_id, user_id, amount) and 'users.csv' 
(user_id, username). Load both into DataFrames using pathlib for file paths, then merge 
them on 'user_id' to show a combined table with username and amount."""

import pandas as pd
from pathlib import Path

# Get current folder
folder = Path(__file__).parent

# Create file paths
orders_path = folder / "orders_S5.csv"
users_path = folder / "users_S5.csv"

# Read CSV files
orders = pd.read_csv(orders_path)
users = pd.read_csv(users_path)

# Merge both DataFrames using user_id
combined = orders.merge(users, on="user_id")

# Show username and amount
result = combined[["username", "amount"]]

print(result)

"""5. Concatenate two DataFrames representing 'today_orders' and 'yesterday_orders' (each with 
columns: order_id, item, price), and display the combined DataFrame. Constraint:Use pd.concat() 
and reset the index after concatenation."""

import pandas as pd

# Today's orders
today_orders = pd.DataFrame({
    "order_id": [101, 102, 103],
    "item": ["Pizza", "Burger", "Biryani"],
    "price": [250, 150, 220]
})

# Yesterday's orders
yesterday_orders = pd.DataFrame({
    "order_id": [98, 99, 100],
    "item": ["Pasta", "Sandwich", "Dosa"],
    "price": [180, 120, 100]
})

# Concatenate both DataFrames and reset index
combined = pd.concat(
    [yesterday_orders, today_orders],
    ignore_index=True
)

# Display combined DataFrame
print(combined)