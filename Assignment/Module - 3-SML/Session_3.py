"""1.
Download a small sample of IPL match data (CSV) with some missing values in player stats. Load it 
using pandas and print the number of missing values in each column."""
import pandas as pd

df = pd.read_csv("S3_IPL_dataset.csv")
print(df.head())
print(df.isnull().sum())


"""2.
For the 'player_age' column in your IPL dataset, fill all missing values with the median age using pandas'
fillna() method and display the updated column."""
import pandas as pd

df = pd.read_csv("S3_IPL_dataset.csv")
print("Missing Values in AGE Column:")
print(df.isnull().sum())
print("Fill Missing Age Column")
df["AGE"] = df["AGE"].fillna(df["AGE"].median())
print(df.isnull().sum())

"""3.
Suppose the 'team' column in your IPL dataset contains missing values. Replace all missing team names 
with the constant value 'Unknown' and print the first 10 rows."""

import pandas as pd

df = pd.read_csv("S3_IPL_dataset.csv")
print("Missing Values in TEAM Column:")
print(df.isnull().sum())
print("Replace missing team names with Unknown")
df["TEAM"] = df["TEAM"].fillna("Unknown")
print(df.isnull().sum())
print(df.head(10)) # Print first 10 rows"""


"""4.
Take the 'venue' column (categorical) from your IPL dataset and apply one-hot encoding using pandas' 
get_dummies(). Show the resulting DataFrame with the new columns."""

import pandas as pd
df = pd.read_csv("S3_IPL_dataset.csv")
print(df.isnull().sum())
# One-hot encode the venue column
VENUE_ENCODED = pd.get_dummies(df["VENUE"],prefix="VENUE")
# Add the new columns to the DataFrame
df = pd.concat([df, VENUE_ENCODED], axis=1)
print(df)

"""5.
Use LabelEncoder from sklearn to encode the 'player_role' column (e.g., Batsman, Bowler, Allrounder) in 
your IPL dataset, and display the mapping from original roles to encoded values.
Hint: Use LabelEncoder's classes_ attribute to see the mapping."""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load IPL dataset
df = pd.read_csv("S3_IPL_dataset.csv")

# Create LabelEncoder
le = LabelEncoder()

# Encode player_role column
df["role_encoded"] = le.fit_transform(df["ROLE"])

# Display mapping
print("Player Role Mapping:")

for role, value in zip(le.classes_, le.transform(le.classes_)):
    print(role, "->", value)

# Display first 10 rows
print("Encoded Data:")
print(df[["ROLE", "role_encoded"]].head(10))