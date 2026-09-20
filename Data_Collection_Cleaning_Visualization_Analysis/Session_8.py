"""1.  Download a small sample of your recent Zomato order history as a CSV (or create a mock CSV with restaurant names 
    and order dates), then use pandas' duplicated() function to find and print any duplicate orders based on 
    restaurant name and date."""
import pandas as pd
df = pd.read_csv("Zomato_Small_Data_S8.csv")   
print(df)

# Find duplicate orders based on restaurant name and order date
duplicates = df[df.duplicated(
    subset = ['restaurant_name', 'order_date'], keep=False)]
print(duplicates)

"""2.  Given a list of Flipkart product reviews with some duplicate entries, use value_counts() in pandas to identify which 
    review texts are repeated most often and display the top 3 most common duplicate reviews."""
import pandas as pd
df = pd.read_csv("flipkart_reviews_S8.csv")   
print(df)

# Duplicate reviews and count their occurrences
duplicate_reviews = df['review_text'].value_counts()
print(duplicate_reviews)

# Top 3 most common duplicate reviews
print(duplicate_reviews.head(3))

"""3.  Create a DataFrame with mock data for Spotify playlists, including playlist names and creator usernames, where some 
    rows are exact duplicates. Use drop_duplicates() to remove duplicate playlists and print the cleaned DataFrame."""

# Create mock Spotify playlist data
import pandas as pd
data = {
    "playlist_name": [
        "Chill Vibes",
        "Workout Hits",
        "Top Bollywood",
        "Chill Vibes",
        "Party Songs",
        "Workout Hits",
        "Chill Vibes"
    ],
    "creator_username": [
        "jinesh123",
        "musiclover",
        "rahul45",
        "jinesh123",
        "dj_raj",
        "musiclover",
        "jinesh123"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)
print(df)

# Remove duplicate playlists Row
cleaned_df = df.drop_duplicates()
print(cleaned_df)

"""4.  Suppose you have a DataFrame of Instagram usernames where some entries have typos (like 'insta_queen', 'insta-queen', 
    'instaqueen'). Use the replace() function to standardize all these variants to 'instaqueen'."""
import pandas as pd

# Create Instagram usernames data
data = {
    "username": [
        "insta_queen",
        "insta-queen",
        "instaqueen",
        "jinesh123",
        "rami_king",
    ]
}

df = pd.DataFrame(data)
print(df)

# Use replace() to replace usernames
df['username'] = df['username'].replace({
    "insta_queen": "instaqueen",
    "insta-queen": "instaqueen"
})
print(df)

"""5.  You have a DataFrame column for payment status from a Paytm-like app with mixed values: 'Yes', 'yes', 'Y', 'No', 'no',
   'N', and some with extra spaces. Write code to unify this column so all paid statuses become 1 and all unpaid statuses 
    become 0, trimming whitespace and fixing capitalization where needed.
    Hint:Use str.strip(), str.lower(), and map/replace methods in pandas."""

import pandas as pd
df = pd.DataFrame({
    "payment_status": [
        "Yes",
        "yes",
        "Y",
        "No",
        "no",
        "N",
        " Yes ",
        " No "
    ]
})

# Remove whitespace and convert to lowercase
df['payment_status'] = df['payment_status'].str.strip().str.lower()
print(df)

# Convert to 1 for paid and 0 for unpaid
df['payment_status'] = df['payment_status'].map({
    'yes': 1,
    'y': 1,
    'no': 0,
    'n': 0
})
print(df)