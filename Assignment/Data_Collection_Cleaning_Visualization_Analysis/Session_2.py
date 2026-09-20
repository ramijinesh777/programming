"""1. Create a 2D NumPy array representing the ratings (out of 5) given by 4 users to 5 different food 
    items on Zomato. Use slicing to extract the ratings given by the second and third users only."""

import numpy as np
ratings = np.array([
    [5,4,3,2,1],
    [4,5,1,2,3],
    [3,5,2,1,4],
    [2,3,4,5,1]
])                      # i take row as user & col as food items
print(ratings)
user_ratings = ratings[1:3]
print(user_ratings)


"""2. Given a NumPy array of daily steps tracked for 10 days, use boolean indexing to select only the 
    days where the steps were greater than 8000.<br><br><em><strong>Hint:</strong> Use an array like 
    steps = np.array([7500, 8200, 9000, ...]) and apply a boolean condition.</em> """

import numpy as np
daily_steps = np.array([7500, 8200, 9000, 6600, 9500 ,8200, 9150, 5000, 7800, 10000])
print(daily_steps)
print(daily_steps > 8000)                           # Boolean indexing apply

high_steps = daily_steps[daily_steps > 8000]        # its give me only value > 8000
print(high_steps)


"""3. Create a NumPy array of IPL team scores for 8 matches. Use fancy indexing to select the scores 
    from matches 2, 5, and 7, and print them."""

import numpy as np
scores = np.array([250,300,150,100,275,210,310,350])
print(scores)
match_score = scores[[1,4,6]]
print(match_score)


"""4. Suppose you have a NumPy array of product prices from Flipkart. Use broadcasting to apply 
    a 10% discount to all prices and print the new array.<br><br><em><strong>Constraint:</strong> 
    Do not use any loops.</em> """

import numpy as np
prices = np.array([500, 1200, 800, 400, 900, 1700])
print(prices)

new_prices = prices * 0.9           # Apply 10% discount to all prices
print(new_prices)


"""5. Given a NumPy array of user ratings (can be negative, zero, or positive) for songs on Spotify, 
    use boolean masking to set all negative ratings to zero, keeping other ratings unchanged."""

import numpy as np
ratings = np.array([5, -1, 0, 4, -2, 0, 5])
print(ratings)

print(ratings < 0)                  # Boolean indexing
ratings[ratings < 0 ] = 0           # Boolean masking 
print(ratings)                      # out put 