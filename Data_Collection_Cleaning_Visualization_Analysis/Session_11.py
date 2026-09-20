"""1.Use plt.subplots() to create a 2x2 grid of subplots and plot four different types of charts 
(line, bar, scatter, and pie) using any sample data of your choice."""

import matplotlib.pyplot as plt
# Sample data
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
sales = [10, 15, 12, 20, 18]
subjects = ["Python", "Pandas", "NumPy", "ML"]
marks = [80, 70, 85, 75]
hours = [1, 2, 3, 4, 5]
scores = [50, 55, 65, 70, 80]
activities = ["Study", "Sleep", "Exercise", "Other"]
time = [6, 8, 2, 8]

# Create a 2x2 grid
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 1. Line chart
axes[0, 0].plot(days, sales, marker="o")
axes[0, 0].set_title("Daily Sales")
axes[0, 0].set_xlabel("Day")
axes[0, 0].set_ylabel("Sales")

# 2. Bar chart
axes[0, 1].bar(subjects, marks)
axes[0, 1].set_title("Subject Marks")
axes[0, 1].set_xlabel("Subject")
axes[0, 1].set_ylabel("Marks")

# 3. Scatter plot
axes[1, 0].scatter(hours, scores)
axes[1, 0].set_title("Study Hours vs Score")
axes[1, 0].set_xlabel("Study Hours")
axes[1, 0].set_ylabel("Score")

# 4. Pie chart
axes[1, 1].pie(time, labels=activities, autopct="%1.1f%%")
axes[1, 1].set_title("Daily Activities")

# Adjust spacing
plt.tight_layout()

# Display the figure
plt.show()

"""2.Plot a comparison of average delivery times for Zomato, Swiggy, and Domino's using a bar chart, 
and style each bar with a different color, linestyle, and linewidth using Matplotlib plot styling options."""
import matplotlib.pyplot as plt

# Sample data
services = ["Zomato", "Swiggy", "Domino's"]
delivery_time = [35, 30, 40]

# Create the bar chart
bars = plt.bar(services, delivery_time)

# Style each bar differently
bars[0].set_color("red")
bars[0].set_linestyle("--")
bars[0].set_linewidth(2)

bars[1].set_color("orange")
bars[1].set_linestyle(":")
bars[1].set_linewidth(3)

bars[2].set_color("blue")
bars[2].set_linestyle("-")
bars[2].set_linewidth(4)

# Add title and labels
plt.title("Average Delivery Time Comparison")
plt.xlabel("Food Delivery Service")
plt.ylabel("Average Delivery Time (Minutes)")

# Display the chart
plt.show()

"""3.Create a multi-axis chart that shows the number of Instagram followers (left y-axis) and average daily posts (right y-axis) for
five influencers. Use different colors and markers for each axis."""

import matplotlib.pyplot as plt

# Sample data
influencers = ["A", "B", "C", "D", "E"]
followers = [50000, 80000, 120000, 90000, 150000]
daily_posts = [2, 4, 3, 5, 6]

# Create figure and first y-axis
fig, ax1 = plt.subplots(figsize=(10, 6))
# Left Y-axis - Followers
ax1.plot(
    influencers,
    followers,
    color="blue",
    marker="o",
    linewidth=2,
    label="Followers"
)
ax1.set_xlabel("Influencers")
ax1.set_ylabel("Instagram Followers", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")
# Create second Y-axis
ax2 = ax1.twinx()
# Right Y-axis - Daily Posts
ax2.plot(
    influencers,
    daily_posts,
    color="red",
    marker="s",
    linestyle="--",
    linewidth=2,
    label="Average Daily Posts"
)
ax2.set_ylabel("Average Daily Posts", color="red")
ax2.tick_params(axis="y", labelcolor="red")
# Title
plt.title("Instagram Followers vs Average Daily Posts")
# Display chart
plt.show()
    
"""4.Plot the number of tickets sold for five recent Bollywood movies (categorical) versus their 
IMDB ratings (numeric) using a scatter plot. Add annotations to display the movie names above 
each point."""

import matplotlib.pyplot as plt

# Sample data
movies = ["Jawan", "Pathaan", "Animal", "Stree 2", "Dunki"]

# Number of tickets sold (in lakhs)
tickets_sold = [120, 110, 150, 135, 90]

# IMDb ratings
imdb_ratings = [7.0, 5.8, 6.1, 6.9, 6.5]

# Create numeric positions for categorical movie names
x = range(len(movies))

# Create scatter plot
plt.figure(figsize=(10, 6))

plt.scatter(x, imdb_ratings, s=tickets_sold, color="blue", marker="o")

# Add movie names above each point
for i in range(len(movies)):
    plt.annotate(
        movies[i],
        (x[i], imdb_ratings[i]),
        xytext=(0, 10),
        textcoords="offset points",
        ha="center"
    )

# Set x-axis labels
plt.xticks(x, movies)

# Add title and labels
plt.title("Bollywood Movies: Tickets Sold vs IMDb Rating")
plt.xlabel("Movies")
plt.ylabel("IMDb Rating")

# Add grid
plt.grid(True)

# Display plot
plt.show()

"""5.Add a custom text annotation to a Matplotlib chart showing Flipkart's monthly sales, marking the 
highest sales point with the label 'Big Billion Days'. Use the ax.annotate() function to place the label 
at the correct data point."""

import matplotlib.pyplot as plt

# Sample monthly sales data (in lakhs)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

sales = [120, 135, 150, 140, 160, 175,
         180, 190, 210, 450, 230, 200]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot monthly sales
ax.plot(months, sales, marker="o", linewidth=2)

# Find the highest sales
max_sales = max(sales)
max_index = sales.index(max_sales)

# Add annotation at the highest sales point
ax.annotate(
    "Big Billion Days",
    xy=(months[max_index], max_sales),
    xytext=(0, 40),
    textcoords="offset points",
    ha="center",
    arrowprops=dict(arrowstyle="->")
)

# Add title and labels
ax.set_title("Flipkart Monthly Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Sales (₹ Lakhs)")

# Add grid
ax.grid(True)

# Display chart
plt.tight_layout()
plt.show()
