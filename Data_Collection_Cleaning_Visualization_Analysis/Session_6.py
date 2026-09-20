"""1. Download a sample CSV file of IPL player stats (include columns like player name, runs, 
matches, and some missing values). Load it into a pandas DataFrame and use isnull() and 
notnull() to print how many missing values are present in each column."""

import pandas as pd
df = pd.read_csv("S6_IPL_Player_Sample.csv")
print(df)
print(df.isnull().sum())          # Count of missing values in each column
print(df.notnull().sum())         # Count of non-missing values in each column


"""2. Using the loaded IPL player stats DataFrame, apply dropna(axis=0, how='any') to remove 
all rows with any missing data and display the shape of the DataFrame before and after 
dropping."""
import pandas as pd
df = pd.read_csv("S6_IPL_Player_Sample.csv")
print(df.shape)                     # Before dropping rows with missing values
df_new = df.dropna(axis=0, how='any')
print(df_new.shape)                 # After dropping rows with missing values
print(df_new)                       # Display the DataFrame after dropping rows with missing values


"""3. For the 'runs' column in your IPL player stats DataFrame, use fillna() to replace 
missing values with the mean of the column. Print the updated column to verify the changes."""
import pandas as pd
df = pd.read_csv("S6_IPL_Player_Sample.csv")
print(df['runs'].isnull().sum())                    # Count of missing values in 'runs' column.
df['runs'] = df['runs'].fillna(df['runs'].mean())   # Fill missing values with mean.
print(df['runs'].isnull().sum())                    # Verify that there are no missing values.
print(df['runs'])                                   # Display the updated 'runs' column.


"""4. Simulate a Zomato-style restaurant ratings dataset with some missing ratings. Use 
forward fill (method='ffill') to fill missing values in the ratings column, then use 
backward fill (method='bfill') for any remaining missing values. Show the before and after 
results."""
import pandas as pd
data = {
    'restaurant': ['Doner King', 'Taco Bell', 'BrownBear', 'Crystal Restaurant & Bar', 'Burger King', 'Ovenstory Pizza', 'Pizza Hut', 'Dominos Pizza', 'KFC', 'Subway'],
    'ratings': [4.5, 4.0, None, 3.5, None, 4.2, None, 3.8, None, 4.1]
}                                                   

df = pd.DataFrame(data)
print("Before filling missing values:") 
print(df)                                   # Data before filling missing values
df['ratings'] = df['ratings'].ffill()       # Forward fill
df['ratings'] = df['ratings'].bfill()       # Backward fill
print(df)                                   # Display the DataFrame after filling missing values


"""5. Pick any one column with missing values from your dataset and explain which missingness 
mechanism (MCAR, MAR, or MNAR) is most likely and why, using 2-3 sentences.<br><br><em><strong>
Hint:</strong> Think about whether the missing data is random or related to other factors in 
the dataset.</em>"""
import pandas as pd
df = pd.read_csv("Zomato_Small_Data_S6.csv")
print(df)   # Display the Zomato dataset

# Explanation of missingness mechanism for the 'ratings' column:
# The 'ratings' column in the Zomato dataset has missing values that are likely to be Missing at Random (MAR). 
# This is because the missing ratings may depend on other observed factors, 
# such as the type of restaurant or its location, rather than being completely random. 




