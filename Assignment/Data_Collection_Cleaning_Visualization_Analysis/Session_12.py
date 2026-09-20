"""1. Install Seaborn in your Python environment and use it to create a histplot showing the distribution 
of delivery times (in minutes) for 50 Zomato food orders. Generate random data if needed."""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate random delivery times for 50 Zomato orders
np.random.seed(42)
delivery_times = np.random.randint(20, 61, 50)

# Create histogram
sns.histplot(
    delivery_times,
    bins=8,
    kde=True
)

# Add title and labels
plt.title("Distribution of Zomato Delivery Times")
plt.xlabel("Delivery Time (Minutes)")
plt.ylabel("Number of Orders")

# Display the chart
plt.show()

"""2. Load the 'tips' dataset from Seaborn and create a boxplot to visualize the distribution of 
total bill amounts by day of the week, similar to how Zomato might analyze spending patterns across 
weekdays."""

import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
df = sns.load_dataset("tips")

# Create boxplot
sns.boxplot(x="day", y="total_bill", data=df)

# Add title and labels
plt.title("Total Bill Amount by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill Amount")

# Display the plot
plt.show()


"""3. Simulate IPL match scores for 8 teams and use a violinplot to compare the run distributions per team. Style your plot using 
the 'darkgrid' Seaborn theme."""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Seaborn theme
sns.set_theme(style="darkgrid")

# Set random seed
np.random.seed(42)

# IPL teams
teams = [
    "CSK", "MI", "RCB", "KKR",
    "SRH", "DC", "PBKS", "RR"
]

# Generate simulated scores for each team
data = []

for team in teams:
    scores = np.random.randint(120, 221, 20)

    for score in scores:
        data.append([team, score])

# Create DataFrame
df = pd.DataFrame(data, columns=["Team", "Runs"])

# Create violin plot
plt.figure(figsize=(12, 6))

sns.violinplot(
    x="Team",
    y="Runs",
    data=df
)

# Add title and labels
plt.title("IPL Run Distribution by Team")
plt.xlabel("IPL Team")
plt.ylabel("Runs Scored")

# Display plot
plt.show()

"""4. Create a countplot that displays the number of songs per genre from a list of 40 Spotify tracks, with at least 4 different 
genres represented.<br><br><em><strong>Hint:</strong> Use a Python list or pandas DataFrame to store your data, then plot 
with Seaborn."""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# List of 40 Spotify tracks with genres
genres = [
    "Pop", "Rock", "Hip-Hop", "Pop", "Jazz",
    "Rock", "Pop", "Hip-Hop", "Electronic", "Pop",
    "Rock", "Jazz", "Hip-Hop", "Pop", "Electronic",
    "Rock", "Pop", "Jazz", "Hip-Hop", "Pop",
    "Electronic", "Rock", "Pop", "Hip-Hop", "Jazz",
    "Pop", "Rock", "Electronic", "Hip-Hop", "Pop",
    "Jazz", "Rock", "Pop", "Electronic", "Hip-Hop",
    "Pop", "Rock", "Jazz", "Hip-Hop", "Electronic"
]

# Create DataFrame
df = pd.DataFrame({"Genre": genres})

# Create countplot
sns.countplot(x="Genre", data=df)

# Add title and labels
plt.title("Number of Spotify Songs by Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Songs")

# Display chart
plt.show()
    
"""5. Use Seaborn's kdeplot to visualize the distribution of daily step counts for a week, as if analyzing data from a fitness app. 
Apply the 'whitegrid' theme and customize the plot color."""

import seaborn as sns
import matplotlib.pyplot as plt

# Daily step counts for one week
steps = [6500, 7200, 8000, 9500, 7000, 11000, 8500]

# Apply whitegrid theme
sns.set_theme(style="whitegrid")

# Create KDE plot
sns.kdeplot(
    steps,
    color="green",
    fill=True
)

# Add title and labels
plt.title("Daily Step Count Distribution")
plt.xlabel("Number of Steps")
plt.ylabel("Density")

# Display the plot
plt.show()