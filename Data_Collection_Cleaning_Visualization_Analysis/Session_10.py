"""1. Install Matplotlib in your Python environment and create a simple line plot showing the number of daily
 steps you took over the last 7 days. Save the chart as steps_lineplot.png."""
import matplotlib.pyplot as plt
# Sample data for daily steps over the last 7 days
daily_steps = [5000, 7000, 8000, 6000, 7500, 9000, 10000]
# Create a line plot
plt.plot(daily_steps)
plt.xlabel('Days')
plt.ylabel('Daily Steps')
plt.title('Steps Over Last 7 Days')
plt.savefig('steps_lineplot.png')

# Save the chart as steps_lineplot.png
plt.savefig('steps_lineplot_S10.png')
plt.show()


"""2. Using Matplotlib, create a scatter plot of 10 restaurants from your city with their Zomato ratings on 
    the x-axis and average meal price on the y-axis. Add axis labels and a title to the chart."""
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('ahmedabad_zomato_ratings_S10.csv')  # Assuming you have a CSV file with restaurant data
# Create a scatter plot
plt.scatter(df['rating'], 
            df['average_meal_price'], 
            color='blue')
plt.xlabel('Zomato Rating')
plt.ylabel('Average Meal Price')
plt.title('Restaurant Ratings vs. Meal Price')
plt.savefig('restaurant_scatterplot_S10.png')
plt.show()


"""3. Build a bar chart that shows the number of orders you or your friends placed on Swiggy, Zomato, 
    and Domino’s in the last month. Use different colors for each bar and add a legend."""
import matplotlib.pyplot as plt
# Sample data for orders placed on different platforms  
platforms = ["Zomato", "swiggy", "Domino's"]
order = [11, 17, 6]
colors = ["Blue", "Green", "Red"]

# Create Bar Chart
plt.bar(platforms, order, color = colors, label = platforms) 
plt.xlabel("Food Delivery Platforms")
plt.ylabel("No of Orders")
plt.title("Food Delivery Order Last Month")
plt.legend()
plt.savefig("Food_Delivery_Order_S10.png")
plt.show()


"""4. Create a histogram of the durations (in minutes) of your last 20 Spotify listening sessions using 
    Matplotlib. Set the number of bins to 5 and customize the color of the bars."""
import matplotlib.pyplot as plt
# Durations of Spotify Listening Music in Minutes
durations = [25, 40, 35, 60, 45,
             30, 55, 70, 20, 50,
             65, 40, 35, 80, 45,
             30, 55, 25, 60, 50]

# Create Histogram
plt.hist(
    durations,
    bins = 5,
    color = "green",
    edgecolor = "black",
)
plt.xlabel("Listening Durations (Minutes)")
plt.ylabel("No of Sessions")
plt.title("Spotify Listening Session Durations")
plt.grid(axis="y")
plt.savefig("Spotify listening sessions_S10.png")
plt.show()


"""5. Customize a Matplotlib figure by creating a plot with two subplots: one line plot showing your 
    daily Instagram screen time for a week, and one bar chart showing the number of posts you liked each
    day. Add appropriate titles, axis labels, and save the figure as social_media_usage.png.
    Hint:Use plt.subplots() to create multiple axes in one figure."""

import matplotlib.pyplot as plt
# Days of the week
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# Instagram screen time (hours)
screen_time = [2, 3, 2.5, 4, 3.5, 5, 4]
# Number of posts liked each day
posts_liked = [20, 25, 18, 30, 28, 40, 35]
# Create two subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
# First subplot - Line plot
axes[0].plot(days, screen_time, marker='o')
axes[0].set_title("Daily Instagram Screen Time")
axes[0].set_xlabel("Day")
axes[0].set_ylabel("Screen Time (Hours)")
axes[0].grid(True)
# Second subplot - Bar chart
axes[1].bar(days, posts_liked)
axes[1].set_title("Instagram Posts Liked")
axes[1].set_xlabel("Day")
axes[1].set_ylabel("Number of Posts Liked")
# Adjust spacing
plt.tight_layout()
# Save the figure
plt.savefig("social_media_usage_S10.png")
# Display the figure
plt.show()