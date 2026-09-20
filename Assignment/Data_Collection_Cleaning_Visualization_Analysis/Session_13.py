"""1. Load the 'tips' dataset from Seaborn and create a pairplot to quickly visualize relationships between
 all numeric variables."""
import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
df = sns.load_dataset("tips")

# Create pairplot for numeric variables
sns.pairplot(df)

# Display the plot
plt.show()

"""2. Using the 'flights' dataset from Seaborn, generate a heatmap showing the correlation between months 
and years based on the number of passengers.Use pivot_table to reshape the data before plotting the heatmap."""
import seaborn as sns
import matplotlib.pyplot as plt

# Load flights dataset
df = sns.load_dataset("flights")

# Create pivot table
pivot_data = df.pivot_table(
    index="month",
    columns="year",
    values="passengers"
)

# Create heatmap
plt.figure(figsize=(12, 6))

sns.heatmap(
    pivot_data,
    annot=True,
    fmt=".0f",
    cmap="YlOrRd"
)

# Title and labels
plt.title("Number of Passengers by Month and Year")
plt.xlabel("Year")
plt.ylabel("Month")

plt.tight_layout()
plt.show()

"""3. Create a relplot using the 'fmri' dataset from Seaborn to visualize how the signal changes over time
 for different event types."""
import seaborn as sns
import matplotlib.pyplot as plt

# Load the fmri dataset
df = sns.load_dataset("fmri")

# Create relational plot
sns.relplot(
    data=df,
    x="timepoint",
    y="signal",
    hue="event",
    kind="line",
    marker="o"
)

# Add title
plt.title("FMRI Signal Changes Over Time")
plt.xlabel("Time Point")
plt.ylabel("Signal")

plt.show()

"""4. Pick any categorical column from the 'titanic' dataset (like 'class' or 'sex') and use catplot to 
display the survival rate for each group with confidence intervals."""
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset
df = sns.load_dataset("titanic")

# Create catplot
sns.catplot(
    data=df,
    x="class",
    y="survived",
    kind="bar",
    errorbar=("ci", 95)
)

# Add title and labels
plt.title("Titanic Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")

plt.show()
    
"""5. Use jointplot on the 'penguins' dataset to visualize the relationship between bill_length_mm and 
flipper_length_mm, and fit a regression line on the scatter plot.<br><br><em><strong>Hint:</strong> Set 
kind='reg' in jointplot for regression line."""

import seaborn as sns
import matplotlib.pyplot as plt

# Load the penguins dataset
df = sns.load_dataset("penguins")

# Create jointplot with regression line
sns.jointplot(
    data=df,
    x="bill_length_mm",
    y="flipper_length_mm",
    kind="reg"
)

# Display the plot
plt.show()