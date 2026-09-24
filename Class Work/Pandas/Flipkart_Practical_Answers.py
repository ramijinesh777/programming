#####################################################################################################
# Series & DataFrame
#####################################################################################################
"""Q1.  Create a Pandas Series from the 'revenue' column of the Flipkart dataset and 
        display its first 10 values."""

# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# revenue = df["revenue"]
# print(revenue.head(10))

"""Q2.  Create a Pandas Series from the 'category' column. Display the unique values and total count of
        each category."""

# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# category = df["category"]           # Serirs Created
# print(category.unique())            # Find Unique
# print(category.value_counts())      # Find Count

"""Q3.  Create a DataFrame manually with 5 sample Flipkart orders containing columns: product_name,
        category, price, quantity, revenue."""

# import pandas as pd
# oders = {
#     "product_name": ["iPhone 14", "Laptop", "T-Shirt", "Headphones", "Shoes"],
#     "category": ["Electronics", "Electronics", "Clothing", "Electronics", "Footwear"],
#     "price": [70000, 55000, 800, 2000, 3000],
#     "quantity": [1, 1, 3, 2, 1],
#     "revenue": [70000, 55000, 2400, 4000, 3000]
# }

# df = pd.DataFrame(oders)
# print(df)


"""Q4.  Load flipkart_orders.csv and display the shape, column names, index, and data types of the
        DataFrame."""

# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# print(df.shape)
# print(df.columns)
# print(df.index)
# print(df.dtypes)

"""Q5.  Extract the 'product_name' and 'revenue' columns from the DataFrame and confirm the result is a
        DataFrame, not a Series."""

# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# df1 = df[["product_name","revenue"]]
# print(df1.head())
# print(type(df1))


#####################################################################################################
# Reading & Writing Data
#####################################################################################################
"""Q6. Load flipkart_orders.csv using pd.read_csv() and display the first 8 rows using head()."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# print(df.head(8))

"""Q7. Display the last 6 rows of the Flipkart dataset using tail()."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# print(df.tail(6))

"""Q8. Use df.info() to inspect the dataset. List all columns that have missing values."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# print(df.info())
# print(df.isnull().sum())


"""Q9.  Use df.describe(include='all') and report the mean price, maximum revenue, and most frequent
        payment method."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# describe =df.describe(include='all')
# # print(describe)
# print("Mean Price : ",df["price"].mean())
# print("Max_Revenue :",df["revenue"].max())
# print("Frequent Payment Method:", df["payment_method"].mode()[0])


"""Q10. Export the Flipkart dataset to a new CSV file named 'flipkart_cleaned.csv' without the index
        column."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# df.to_csv("flipkart_cleaned.csv", index=False)

#####################################################################################################
# Selecting & Filtering Data (loc & iloc)
#####################################################################################################
"""Q11. Select only the columns 'order_id', 'product_name', 'category', and 'revenue' 
        from the DataFrame."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# columns = df[['order_id', 'product_name', 'category', 'revenue']]
# print(columns)

"""Q12. Using iloc, display rows 50 to 60 and only the first 5 columns."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# print(df.iloc[50:61, 0:5])

"""Q13. Using loc, display all rows where order_status is 'Delivered'."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# order_status = df.loc[df["order_status"]=="Delivered"]
# print(order_status)

"""Q14. Using Boolean conditions, filter all orders where revenue is greater than 10,000."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# high_revenue = df[df["revenue"]>10000]
# print(high_revenue)

"""Q15. Filter all Electronics orders placed by customers from 'Mumbai'."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# elec_mumbai = df[(df["category"]=="Electronics") & (df["city"]=="Mumbai")]
# print(elec_mumbai)
                                            
"""Q16. Using loc, display all orders where discount_pct is 50 and order_status is 'Delivered'."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# result = df.loc[(df["discount_pct"] == 50) & (df["order_status"] == "Delivered")]
# print(result)

"""Q17. Filter orders where rating is greater than 4.0 and category is 'Electronics'. How many such orders
        exist?"""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# filtered_orders = df[(df["rating"] > 4.0) & (df["category"] == "Electronics")]
# print(filtered_orders)
# print("Total Orders : ",len(filtered_orders))

"""Q18. Using query(), find all orders where age is greater than 40 and payment_method is 'UPI."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# result = df.query("age > 40 and payment_method == 'UPI'")
# print(result)

#####################################################################################################
# Sorting & Reindexing
#####################################################################################################
"""Q19. Sort the Flipkart dataset by 'price' in descending order and display the top 10 most expensive
        products."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# top_10 = df.sort_values(by="price", ascending=False) 
# print(top_10.head(10))

"""Q20. Sort orders by 'order_date' in ascending order and display the 5 earliest orders."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# df["order_date"] = pd.to_datetime(df["order_date"])
# earli_5 = df.sort_values(by="order_date", ascending=True) 
# print(earli_5.head(5))

"""Q21. Sort the dataset by 'category' ascending and then by 'revenue' descending within each category."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# sort_df = df.sort_values(by=["category","revenue"],ascending = [True, False])
# print(sort_df)

"""Q22. After sorting by revenue, reset the index and confirm the old index is dropped."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# sorted_df = df.sort_values(by="revenue", ascending=False)
# sorted_df = sorted_df.reset_index(drop=True)
# print(sorted_df.head())
# print(sorted_df.index)

"""Q23. Sort the dataset by 'rating' descending (NaN last) and display the top 10 highest-rated orders."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# top_rated = df.sort_values(by="rating",ascending=False,na_position="last")
# print(top_rated.head(10))

"""Q24. Reindex the DataFrame using a custom range index starting from 1001 and display the first 5
rows."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# df.index = range(1001, 1001 + len(df))
# print(df.head(5))


#####################################################################################################
# Handling Missing Values
#####################################################################################################
"""Q25. Display the total count and percentage of missing values for every column in the 
        Flipkart dataset."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# missing_count = df.isnull().sum()
# missing_percentage = (df.isnull().sum()/len(df))*100
# missing_df = pd.DataFrame({
#     "missing_count" : missing_count,
#     "missing_percentage" : missing_percentage
# })
# print(missing_df)

"""Q26. Drop all rows where 'customer_name' is missing. How many rows remain?"""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# clean_df = df.dropna(subset=["customer_name"])
# print("remain Row : ",len(clean_df))

"""Q27. Drop only columns where more than 40% of values are missing."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# missing_percent = (df.isnull().sum() / len(df)) * 100
# columns_to_drop = missing_percent[missing_percent > 40].index
# new_df = df.drop(columns=columns_to_drop)
# print("Dropped columns:", list(columns_to_drop))
# print("Remaining columns:", new_df.columns)

"""Q28. Fill missing 'age' values with the median age of the entire dataset."""
# import pandas as pd
# df = pd.read_csv("flipkart_orders.csv")
# med_age = df["age"].median()
# df["age"] = df["age"].fillna(med_age)
# print(df["age"])

"""Q29. Fill missing 'city' values with the string 'Unknown'."""
import pandas as pd
df = pd.read_csv("flipkart_orders.csv")
df["city"] = df["city"].fillna("unknown")
print(df["city"])                  

"""Q30. Fill missing 'rating' values with the mean rating grouped by 'category'."""



"""Q31. Use forward fill to fill missing 'delivery_date' values and 
        check if any nulls remain."""



"""Q32. Fill missing 'review' values with 'No Review'. Then confirm no nulls exist 
        in that column."""