## Loading the Dataset ## 


""" Questation : 1 - Load titanic.csv into a DataFrame using pd.read_csv() and display the first 10 rows."""
# import pandas as pd
# df = pd.read_csv("Home Work\\titanic.csv")
# print(df.head(10))

"""Questation : 2 - Display the shape, column names, and data types of the Titanic dataset."""
# import pandas as pd
# print(df.shape)
# print(df.columns)
# print(df.dtypes)

"""Questation : 3 - The Titanic CSV file uses comma as delimiter. Reload it explicitly passing 
                    the separator and confirm it loads correctly."""

# import pandas as pd
# df = pd.read_csv("Home Work\\titanic.csv",sep=",")
# print(df.head(5))

##########################################################################################################
## Early Data Inspection ##


"""Q4. Use df.info() to display column names, non-null counts, and data types of the Titanic dataset."""
# import pandas as pd
# df = pd.read_csv("Home Work\\titanic.csv")
# print(df.info())

"""Q5. Use df.describe(include='all') and identify which column has the highest standard deviation. """

# import pandas as pd
# df = pd.read_csv("Home Work\\titanic.csv")
# print(df.describe(include="all"))
# sd_value = df.std(numeric_only=True)
# print(sd_value)
# highest_column = sd_value.idxmax
# print(highest_column)
# highest_std = sd_value.max()
# print(highest_std)

"""Q6. From df.describe(include='all'), identify which columns are numeric and which are categorical. """

# import pandas as pd
# df = pd.read_csv("Home Work\\titanic.csv")
# print(df)
# print(df.select_dtypes(include=['int64', 'float64']).columns)
# print(df.select_dtypes(include=['object']).columns)

"""Q7. Using df.info(), identify how many columns have at least one missing value. """

# import pandas as pd
# df = pd.read_csv("Home Work\\titanic.csv")
# print(df.info)
# missing = df.isnull().sum()
# print(missing)

# has_missing = missing > 0
# print(has_missing)

# count = has_missing.sum()
# print(count)
##########################################################################################################
## Identifying Missing Data ##


"""Q20. Display the total number of missing values in each column of the Titanic dataset"""
"""Q21. Display the percentage of missing values per column, sorted in descending order"""
"""Q22. Using notnull(), filter and display only rows where both 'Age' and 'Cabin' are present"""
"""Q23. Display the total count of missing values in the entire dataset as a single number"""


##########################################################################################################
## dropna() ##


"""Q24. Drop all rows that have any missing value and print how many rows were removed."""
"""Q25. Drop only the rows where 'Age' is missing using the subset parameter."""
"""Q26. Drop only columns that have more than 70% missing values."""
"""Q27. Use the thresh parameter to keep only rows that have at least 10 non-null values."""


##########################################################################################################
## fillna() ##

"""Q28. Fill missing values in the 'Age' column with the median age."""
"""Q29. Fill missing values in the 'Embarked' column with the mode."""
"""Q30. Fill missing values in 'Age' using forward fill and check if any nulls remain."""
"""Q31. Fill missing values in 'Fare' using backward fill."""
"""Q32. Fill missing 'Age' values with the mean age grouped by 'Pclass'."""
"""Q33. Fill missing 'Age' values with the mean age grouped by both 'Pclass' and 'Sex'."""


##########################################################################################################
## Missingness Mechanisms (Conceptual + Applied) ##

"""Q34. The 'Cabin' column has ~77% missing values. Analyze whether this is MCAR, MAR, or MNAR. 
    Justify with data evidence."""
"""Q35. Check if 'Age' missingness is related to 'Pclass'. Does this suggest MCAR, MAR, or MNAR?"""


##########################################################################################################
## Outlier Detection — Boxplot Method ##
"""Q36. Using IQR boundaries, identify how many outliers exist in the 'Fare' column based on a boxplot 
    analysis."""
"""Q37. Apply the boxplot method on the 'Age' column and list the outlier values found."""

##########################################################################################################
## Outlier Detection — Z-Score Method ##


"""Q38. Using the Z-score method (threshold = 3), find all rows where 'Fare' is an outlier"""
"""Q39. Apply Z-score outlier detection on the 'Age' column and display the count of detected outliers"""
"""Q40. Apply Z-score on all numeric columns and report which column has the highest number of outliers"""

##########################################################################################################
## Outlier Detection — IQR Method ##


'''Q41. Using the IQR method, detect outliers in the 'Fare' column. Display the lower and upper 
        bounds used.'''
'''Q42. Apply IQR-based outlier detection on the 'Age' column and display the percentage of rows 
        that are outliers.'''
'''Q43. Apply IQR outlier detection on both 'Age' and 'Fare'. Which column has more outliers?'''

##########################################################################################################
## Outlier Treatment — Capping ##


'''Q44. Cap outliers in the 'Fare' column at the 5th and 95th percentiles. Verify using describe().'''
'''Q45. Apply Winsorization (1st and 99th percentile) on the 'Age' column and compare min/max before 
        and after.'''
'''Q46. Cap 'Fare' outliers using IQR method (lower = Q1 - 1.5×IQR, upper = Q3 + 1.5×IQR) and display 
        the result.'''


