"""
import pandas as pd
df = pd.read_csv("flipkart_orders.csv")
# print(df)
''' Inspect Data '''
print(df.shape)             # find row and columns
print(df.info())            # columns name + datatype + non null count
print(df.isnull().sum())    # missing values count

'''Remove Duplicate Rows'''
print("Duplicate Rows :",df.duplicated().sum())
df.drop_duplicates()

'''Fix Missing Age '''
median_age = df["age"].median()
df["age"] = df["age"].fillna(median_age)

''' Fix Missing City '''
df["city"] = df["city"].fillna("Unknown")

''' Fix Missing State '''
df["state"] = df["state"].fillna("Unknown")

''' Fix Missing Customer Name '''
df["customer_name"] = df["customer_name"].fillna("Unknown Customer")

''' Missing Rating '''
avg_rating = df["rating"].mean()
df["rating"] = df["rating"].fillna(avg_rating)

''' Missing Review '''
df["review"] = df["review"].fillna("No Review")

''' Convert Dates '''
df["order_date"] = pd.to_datetime(df["order_date"])
df["delivery_date"] = pd.to_datetime(df["delivery_date"])

''' Recalculate Delivery Days - Optional '''
df["delivery_days"] = (
    df["delivery_date"] - df["order_date"]
).dt.days

''' check negative values '''
print((df["price"]<0).sum())
print((df["revenue"]<0).sum())
print((df["quantity"]<=0).sum())

# remove bad rows
df = df[df["price"] >0]
df = df[df["quantity"] >0]

''' Check Outliers '''
print(df["price"].describe())

''' Standardize Taxt '''
df["city"] = df["city"].str.strip().str.title()
df["category"] = df["category"].str.strip().str.title()

''' Reset Index '''
df = df.reset_index(drop=True)

''' Final Missing Check '''
print(df.isnull().sum())

''' Export Clean CSV File '''
df.to_csv("flipkart_cleaned_final.csv", index=False)
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("flipkart_cleaned_final.csv")
df["order_date"] = pd.to_datetime(df["order_date"])

# Month Wise Sales Trend
df["month"] = df["order_date"].dt.month
month_sales = df.groupby("month")["revenue"].sum()
print(month_sales)

plt.figure(figsize=(8,4))
plt.plot(month_sales.index, month_sales.values, marker="o")
plt.title("Month Wise Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()


# Day Wise Sales Trend
df["day"] = df["order_date"].dt.day_name()
day_sales = df.groupby("day")["revenue"].sum()
print(day_sales)

plt.figure(figsize=(8,4))
plt.bar(day_sales.index, day_sales.values)
plt.title("Day Wise Sales")
plt.xlabel("Day")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()


# Year Wise Sales Trend
df["year"] = df["order_date"].dt.year
year_sales = df.groupby("year")["revenue"].sum()
print(year_sales)

plt.figure(figsize=(8,4))
plt.bar(year_sales.index, year_sales.values)
plt.title("Year Wise Sales")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.show()

