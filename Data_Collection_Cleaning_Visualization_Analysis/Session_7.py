"""1.  Given a CSV file containing Zomato restaurant ratings, use pandas to detect outliers in the 'user_rating' column using the IQR 
    method and print the indices of the detected outliers."""

import pandas as pd
df = pd.read_csv("Zomato_Small_Data_All_Col_S7.csv")
# print(df.info())                                # Display Data info to check for missing values and data types
df["Dining_Rating"] = df["Dining_Rating"].ffill() 
# print(df.info())                                # Display Data info to check after ffill missing values
print(df)                                    
# Detecting outliers in the 'user_rating' column using the IQR method
q1 = df['Dining_Rating'].quantile(0.25)
q3 = df['Dining_Rating'].quantile(0.75)
print("q1 value:", q1)
print("q3 value:", q3)

# Calculate IQR
iqr = q3 - q1
print("IQR value:", iqr)

# Calculate lower and upper limit for outliers
lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr
print("Lower limit for outliers:", lower_limit)
print("Upper limit for outliers:", upper_limit)

# Identify outliers
outliers = df[
    (df['Dining_Rating'] < lower_limit) | 
    (df['Dining_Rating'] > upper_limit)
    ]

print("Outlier indices:")
print(outliers.index.tolist())              



"""2.  Create a boxplot for the 'order_amount' column from a Zomato orders dataset using matplotlib, and visually identify any 
    outliers present.
    Hint: Use plt.boxplot() and label your axes for clarity."""

import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("Zomato_Small_Data_All_Col_S7.csv")
df["Dining_Rating"] = df["Dining_Rating"].ffill() 

plt.boxplot(df["Dining_Rating"].dropna())

plt.xlabel("Dining_Rating")
plt.ylabel("Dining_Rating")
plt.title("Boxplot of Zomato Dining Ratings")
plt.show()


"""3.  Apply winsorization to the 'transaction_amount' column in a Paytm transactions DataFrame to cap all values above the 95th 
    percentile and below the 5th percentile, then display the updated column statistics."""

import pandas as pd   
df = pd.read_csv("Paytm_Transection_Amout_Data_S7.csv")
print(df.info())       

# Find the 5th and 95th percentiles
lower_percentile = df["amount"].quantile(0.05)
upper_percentile = df["amount"].quantile(0.95)
print("5th Percentile:", lower_percentile)
print("95th Percentile:", upper_percentile)

# Apply winsorization to the 'amount' column
df["amount"] = df["amount"].clip(lower=lower_percentile, upper=upper_percentile)

# Display updated column statistics
print("5th Percentile after Winsorization:", lower_percentile)
print("95th Percentile after Winsorization:", upper_percentile)

print("Updated Column Statistics:")
print(df["amount"].describe())

"""4.  You have a DataFrame of Flipkart product prices stored as strings with currency symbols (e.g., '₹1,299'). Convert this column 
    to numeric type using pandas, ensuring all non-numeric characters are removed.
    Hint:Use str.replace() and astype()"""
import pandas as pd 
df = pd.read_csv("flipkart_S7.csv")
print(df.info())

# Convert the 'price' column to string type to numeric type
df["price"] = df["price"].str.replace('?', '').astype(float)
print(df["price"].head())                     # Display the first few rows of the converted 'price' column
print(df["price"].dtype)                      # Display the data type of the 'price' column after conversion



"""5.  Fix the following code snippet where the 'is_premium' column in a Spotify user DataFrame is a mix of boolean, string, 
    and integer types. Convert the entire column to boolean type, treating 'True', 1, and 'yes' as True, and everything 
    else as False."""

import pandas as pd
data = {
    'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'is_premium': [True, False, True, 1, 'Yes', 'No', False , 0, True, 1]}
df = pd.DataFrame(data)
print(df)                                    

# Convert the 'is_premium' column to boolean type
df['is_premium'] = df['is_premium'].apply(
lambda x: True if (
    x== True or x == 1 or str(x).lower() == 'yes') else False
)
print(df["is_premium"])
print(df["is_premium"].dtype)

                                          
