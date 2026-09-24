""" 
Scenario: Supermarket Sales Analysis 
local supermarket recorded daily sales for 5 products over 7 days (one week). 
You are hired as a data analyst intern. Your job: clean the data, analyse it, 
and generate key business insights — all using NumPy.


Product     Mon     Tue     Wed     Thu     Fri     Sat     Sun
Rice        1200    1350    1100    1400    1250    1800    1600
Oil         800     750     -50     820     790     1100    950
Biscuits    400     420     380     450     430     600     580
Milk        950     1000    920     980     1010    1200    1150
Soap        300     280     310     -20     295     400     370
{Negative values (-50, -20) = data entry errors (bad data!)} """


""" Task 1: Array Creation : 
Create the 5×7 NumPy array from the data above. Print its shape, ndim, size, dtype."""

import numpy as np
sales = np.array([
    [1200, 1350, 1100, 1400, 1250, 1800, 1600],   # Rice
    [800, 750, -50, 820, 790, 1100, 950],         # Oil
    [400, 420, 380, 450, 430, 600, 580],          # Biscuits
    [950, 1000, 920, 980, 1010, 1200, 1150],      # Milk
    [300, 280, 310, -20, 295, 400, 370]           # Soap
])
print(sales)
# print("Shape :", sales.shape)
# print("Dimensions (ndim):", sales.ndim)
# print("Size :", sales.size)
# print("Data Type :", sales.dtype)


""" Task : 2 - Indexing & Slicing
Extract: (a) Rice sales only (b) Weekend sales (Sat+Sun) for all products (c) Oil sales on Wednesday
(the bad value)."""
# rice_sales = sales[0]
# print(rice_sales)

# weekend_sales = sales[:, 5:7]
# print(weekend_sales)

# oil_sales_wed = sales[1,2]
# print(oil_sales_wed)

""" Task : 3 - Boolean Indexing
Find all negative (bad) values. Replace them with 0 using a boolean mask."""
# mask = sales < 0
# print(mask)
# print(sales[mask])
# sales[sales < 0] = 0 
# print(sales)

""" Task : 4 - Broadcasting 
Apply a 5% weekend festival discount on ALL products for Sat & Sun using broadcasting."""
# discount = 0.95
# sales[:, 5:7] = sales[:, 5:7] * discount
# print(sales)

""" Task : 5 - Aggregation [Session 1 — array methods] 
Find: total weekly sales per product, best-selling day (column sum), average daily sale. """
# (Total weekly sales per product)
# weekly_sales = np.sum(sales,axis=1)
# print(weekly_sales)

# (Best selling day)
# daily_sales = np.sum(sales, axis=0)
# print(daily_sales)

# (Best Day)
# days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# best_day = days[np.argmax(daily_sales)]
# print(best_day)

# (Average daily sales)
# avg_daily_sale = np.mean(sales)
# print(avg_daily_sale)

""" Task : 6 - Bonus Challenge
Which product had zero sales on any day after cleaning? Use boolean indexing + any() to find out.
Then use broadcasting to add a flat n50 delivery charge to all products for Mon & Tue only."""


