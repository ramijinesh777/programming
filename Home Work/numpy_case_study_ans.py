# Section 1 — Array Creation & Inspection
#####################################################################################################
"""1. Write NumPy code to create a random integer array of shape (30, 5) with values between 50
and 500. Name it sales_data."""

# import numpy as np
# from pandas import read_csv
# sales_data = np.random.randint(50, 501, size=(30, 5))
# print(sales_data)


"""2. What function would you use to check the shape, data type, and number of dimensions of
sales_data?""" # Hint: Use .shape, .dtype, .ndim
# sd = read_csv("numpy_retailcorp_sales_data.csv")
# print(sd.shape)
# print(sd.dtypes)
# print(sd.ndim)


"""3. How many total sales values are stored in this array? Write the NumPy expression to find this."""
# s_data = np.random.randint(50, 501, size=(30, 5))
# print("Total sales values:", s_data.size)

"""4. Extract the sales data for just the first product (column 0). What is the resulting shape?"""
# import numpy as np
# from pandas import read_csv
# s_data = sd = read_csv("numpy_retailcorp_sales_data.csv")
# first_product_sales = s_data.iloc[:, 0]
# print("Shape of first product sales:", first_product_sales.shape)


"""Q5. Slice the data to get sales for days 10 to 20 (inclusive) for all products."""
# import numpy as np
# from pandas import read_csv
# s_data = read_csv("numpy_retailcorp_sales_data.csv")
# slice_data = s_data.iloc[9:20, :]
# print(slice_data)
# print("Sliced data shape:", slice_data.shape)


#####################################################################################################
# Section 2 — Statistical Analysis
#####################################################################################################

"""Q6. Calculate the total sales for each product across all 30 days.
        Hint: Sum along axis=0 """
# import numpy as np
# from pandas import read_csv
# sales_data = read_csv("numpy_retailcorp_sales_data.csv").values
# total_sales = np.sum(sales_data, axis=0)
# print("Total sales for each product:", total_sales)


"""Q7. Find the average daily sales across all products combined."""
# import numpy as np
# from pandas import read_csv
# sales_data = read_csv("numpy_retailcorp_sales_data.csv").values
# average_daily_sales = np.mean(sales_data)
# print("Average daily sales across all products:", average_daily_sales)


"""Q8. Which product had the highest total sales? Write the NumPy code to find its index."""
# Hint: np.argmax()
# import numpy as np
# from pandas import read_csv
# sales_data = read_csv("numpy_retailcorp_sales_data.csv").values
# total_sales_per_product = np.sum(sales_data, axis=0)
# best_product_index = np.argmax(total_sales_per_product)
# print("Index of the best product:", best_product_index)


"""Q9. Find the standard deviation of sales for each product. What does a high std dev indicate?"""
# import numpy as np
# from pandas import read_csv
# sales_data = read_csv("numpy_retailcorp_sales_data.csv").values 
# standard_deviation_per_product = np.std(sales_data, axis=0)
# print("Standard deviation of sales for each product:", standard_deviation_per_product)


"""Q10. Calculate the median daily sales for the entire dataset."""
# import numpy as np
# from pandas import read_csv
# sales_data = read_csv("numpy_retailcorp_sales_data.csv").values
# median_daily_sales = np.median(sales_data)
# print("Median daily sales for the entire dataset:", median_daily_sales)


"""Q11. Find the minimum and maximum sales values recorded in the entire dataset."""
# import numpy as np
# from pandas import read_csv
# sales_data = read_csv("numpy_retailcorp_sales_data.csv").values
# min_sales_value = np.min(sales_data)
# max_sales_value = np.max(sales_data)
# print("Minimum sales value recorded in the dataset:", min_sales_value)
# print("Maximum sales value recorded in the dataset:", max_sales_value)


#####################################################################################################
# Section 3 — Data Filtering & Boolean Indexing
#####################################################################################################

"""Q12. Write code to find all days where sales of Product 3 exceeded 300 units."""
import numpy as np
from pandas import read_csv
sales_data = read_csv("numpy_retailcorp_sales_data.csv").values




"""Q13. How many days had total sales (across all products) greater than 1500?
Hint: Use np.sum() on a boolean mask"""




"""Q14. Replace all sales values below 60 with 60 (treat these as the minimum threshold). Write the
NumPy code."""




"""Q15. Find the indices (day numbers) where Product 1 had its top 5 highest sales days.
Hint: np.argsort()"""




