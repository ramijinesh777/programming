import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("flipkart_cleaned_final.csv")
print(df.columns)

# Create figure with 2 rows and 2 columns
plt.figure(figsize=(14, 10))

# ------------------ Subplot 1 ------------------
plt.subplot(2, 2, 1)
top_category = df.groupby("category")["revenue"].sum().sort_values(ascending=False).head(5)
plt.bar(top_category.index, top_category.values)
plt.title("Top 5 Categories by Revenue")
plt.xticks(rotation=45)

# ------------------ Subplot 2 ------------------
plt.subplot(2, 2, 2)
payment_count = df["payment_method"].value_counts()
plt.bar(payment_count.index, payment_count.values)
plt.title("Payment Method Usage")
plt.xticks(rotation=45)

# ------------------ Subplot 3 ------------------
plt.subplot(2, 2, 3)
plt.hist(df["rating"], bins=5)
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")

# ------------------ Subplot 4 ------------------
plt.subplot(2, 2, 4)
delivery_avg = df.groupby("order_status")["delivery_days"].mean()
plt.bar(delivery_avg.index, delivery_avg.values)
plt.title("Avg Delivery Days")
plt.xticks(rotation=45)

# Adjust spacing
plt.tight_layout()
plt.show()