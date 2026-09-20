"""1.  Given a list of delivery timestamps as strings (e.g., ['2024-06-01 14:30', '2024-06-02 09:15', '2024-06-03 20:45']), use 
    pandas and pd.to_datetime() to convert them into datetime objects and print the result."""
# Create a list of delivery timestamps as strings
import pandas as pd
import numpy as np
timestamps = ['2024-06-01 14:30', 
              '2024-06-02 09:15', 
              '2024-06-03 20:45']
# print(timestamps)

# Convert the list of strings to datetime objects
datetime_objects = pd.to_datetime(timestamps)
print(datetime_objects)

"""2.  Load a CSV file containing order dates from a Flipkart-style order history (column: 'order_date', format:'YYYY-MM-DD HH:MM:SS'). 
    Extract the year, month, and weekday for each order and add them as new columns in the DataFrame."""
import pandas as pd
# Load the CSV file containing order dates
df = pd.read_csv("flipkart_orders_S9.csv")
print(df.head())

# Convert 'order_date' column to datetime
df['order_date'] = pd.to_datetime(df['order_date'],dayfirst=True)

# Extract year, month, and weekday and add them as new columns
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month
df['weekday'] = df['order_date'].dt.day_name()
print(df.head())


"""3. Set the 'order_date' column as the index of your DataFrame and use resampling to calculate the total 
    number of orders placed each week.
    Hint : Use df.resample('W').size() after setting the datetime index."""
import pandas as pd
df = pd.read_csv("flipkart_orders_S9.csv")
# Convert 'order_date' column to datetime
df['order_date'] = pd.to_datetime(df['order_date'],dayfirst=True)

# Set 'order_date' as the index
df.set_index('order_date', inplace=True)

# Resample the Data to calculate total number of orders placed each week
weekly_orders = df.resample('W').size()
print(weekly_orders)


"""4. Suppose you have a DataFrame of Instagram posts with a 'posted_at' column in UTC. Convert these timestamps to 'Asia/Kolkata' 
timezone and display the first 5 converted times."""
import pandas as pd
df = pd.DataFrame({
    'posted_at': ['2024-06-01 14:30:00',
                    '2024-06-02 09:15:00',
                    '2024-06-03 20:45:00',
                    '2024-06-04 11:00:00',
                    '2024-06-05 18:30:00']
})
# Convert 'posted_at' column to datetime with UTC timezone
df['posted_at'] = pd.to_datetime(df['posted_at'], utc=True)

# Convert the timestamps to 'Asia/Kolkata' timezone
df['posted_at'] = df['posted_at'].dt.tz_convert('Asia/Kolkata')
print(df['posted_at'].head())

"""5. Create a new feature called 'is_weekend' in your DataFrame that marks True if an order was placed 
on Saturday or Sunday, and False otherwise.
Constraint: Do not use any external libraries except pandas and numpy."""
import pandas as pd
df = pd.read_csv("flipkart_orders_S9.csv")

# Convert 'order_date' column to datetime
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True)

# Create 'is_weekend' feature
df['is_weekend'] = df['order_date'].dt.weekday >= 5
print(df[['order_date', 'is_weekend']].head())
