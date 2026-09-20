"""1. Install the pandas-profiling library and generate a profile report for the 'Spotify Top 100 Songs' dataset 
(CSV available on Kaggle); open the HTML report and note any missing values or data type issues."""
import pandas as pd
from ydata_profiling import ProfileReport

# Load dataset
df = pd.read_csv("spotify_tracks_S14.csv")

# Create profile report
profile = ProfileReport(
    df,
    title="Spotify Top 100 Songs - Data Profile",
    explorative=True
)

# Save HTML report
profile.to_file("spotify_profile_report.html")

print("Profile report created successfully!")

"""2. Use Sweetviz to create a comparison report between two CSV files: one containing Zomato restaurant 
data for Mumbai and another for Delhi. Briefly describe one key difference you spot in the visual report.
Use analyze() for single file and compare() for two datasets."""

import pandas as pd
import sweetviz as sv

# Load Mumbai dataset
mumbai = pd.read_csv("Zomato_Mumbai_S15.csv")

# Load Delhi dataset
delhi = pd.read_csv("Zomato_Delhi_S15.csv")

# 1. Single dataset analysis using analyze()
mumbai_report = sv.analyze(mumbai)
mumbai_report.show_html("zomato_mumbai_report.html")

# 2. Compare Mumbai and Delhi using compare()
compare_report = sv.compare(
    [mumbai, "Mumbai"],
    [delhi, "Delhi"]
)
compare_report.show_html("zomato_mumbai_vs_delhi.html")
print("Reports created successfully!")

   
"""3. Open the Myntra product listings dataset in D-Tale, explore the interface, and use it to filter 
products with a price above ₹2000. Take a screenshot of the filtered view and note the number of such 
products."""

import pandas as pd
import dtale

df = pd.read_csv("myntra_S15.csv")
d = dtale.show(df)
d.open_browser()

"""4. Given a pandas-profiling report for a Flipkart product reviews dataset, interpret and list two 
columns that may need cleaning or transformation before further analysis.
Hint:Look for columns with high cardinality,missing values, or warnings in the report."""

import pandas as pd

# Load dataset
df = pd.read_csv("Flipkart_S15.csv",encoding="latin1")

# Display basic information
print(df.shape)
print(df.info())

# Check missing values
print(df.isnull().sum())

# Check unique values / cardinality
print(df.nunique())

# Find columns with high cardinality
print("\nHigh Cardinality Columns:")
for col in df.columns:
    if df[col].nunique() > 0.8 * len(df):
        print(col, "->", df[col].nunique(), "unique values")

# Find columns having missing values
print("\nColumns With Missing Values:")
for col in df.columns:
    missing = df[col].isnull().sum()
    if missing > 0:
        print(col, "->", missing, "missing values")


"""5. Pick any one auto-EDA tool (pandas-profiling, Sweetviz, or D-Tale) and use ChatGPT or Copilot to generate a code snippet 
that loads a Swiggy food order CSV and produces a summary report. Run the code and attach the generated report or a screenshot 
as proof."""

import pandas as pd
import sweetviz as sv

df = pd.read_csv("swiggy_S15.csv")
# Display basic information
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print(df.head())

# Create Sweetviz Auto-EDA report
report = sv.analyze(df)
# Save Report
report.show_html("swiggy_auto_eda_report.html")

print("Report generated successfully!")