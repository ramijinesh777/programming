"""1. Download a small dataset of IPL cricket matches (CSV or Excel), load it into a pandas DataFrame, and 
perform univariate analysis by printing the summary statistics (mean, median, min, max, std) for the 
'total_runs' column."""
import pandas as pd
# Load dataset
df = pd.read_csv("Data_Collection_Cleaning_Visualization_Analysis/deliveries_S14.csv")
# Display first 5 rows
print(df.head())

# Summary statistics for total_runs
print("Mean:", df["total_runs"].mean())
print("Median:", df["total_runs"].median())
print("Minimum:", df["total_runs"].min())
print("Maximum:", df["total_runs"].max())
print("Standard Deviation:", df["total_runs"].std())
    
"""2. Using a dataset of Flipkart product reviews (at least columns: 'rating', 'category'), create a bar 
plot showing the count of reviews for each rating (1-5 stars) using matplotlib or seaborn."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Data_Collection_Cleaning_Visualization_Analysis/flipkart_sales_S14.csv")

# Convert rating to numeric
df["rating"] = pd.to_numeric(df["Rating"], errors="coerce")

# Count ratings from 1 to 5
rating_counts = df["Rating"].value_counts().sort_index()

# Plot
sns.barplot(x=rating_counts.index, y=rating_counts.values)

plt.title("Flipkart Review Ratings")
plt.xlabel("Rating (Stars)")
plt.ylabel("Number of Reviews")

plt.show()


"""3. Take a dataset of Zomato restaurant listings (with 'average_cost_for_two' and 'user_rating' columns)
 and create a scatterplot to visualize the relationship between cost and user rating.
Hint:Use seaborn's scatterplot() function and label the axes clearly."""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Zomato_S14.csv")
print(df)

# scatterplot
sns.scatterplot(
    data = df,
    x = "rate for two",
    y = "rating"
)
# Lable & Tital
plt.xlabel("Rate For Two")
plt.ylabel("Rating")
plt.title("Relationship Between Cost and User Rating")

plt.show()


"""4. For a BookMyShow movie dataset (with 'genre' and 'box_office_collection' columns), use groupby 
analysis to find the average box office collection for each genre and display the results as a sorted table."""
import pandas as pd

df = pd.read_csv("bookmyshow_movies_S14.csv")

result = (
    df.groupby("genre", as_index= False)["box_office_collection"]
    .mean()
    .sort_values("box_office_collection", ascending=False)
)
print(result)

    
"""5. Use the seaborn 'pairplot' function on a Spotify songs dataset (with at least 'danceability', 
'energy', 'valence', and 'popularity' columns) to visualize pairwise relationships between these features.
Briefly describe one interesting pattern you observe."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Spotify dataset
df = pd.read_csv("spotify_tracks_S14.csv")

# Select required columns
features = ["danceability", "energy", "valence", "popularity"]

# Create pairplot
sns.pairplot(df[features])

plt.show()