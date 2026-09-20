"""1. Install NumPy in your Python environment using pip, then create a Python file called insta_likes.py 
    and import numpy as np at the top."""

# py -m pip install numpy
import numpy as np
print("NumPy import successfully")


"""2. Create a NumPy array called followers using np.array() that stores the follower counts for 5 Instagram 
    influencers: [1200, 15000, 67000, 340000, 1250000]. Print the array, its shape, number of dimensions, 
    and data type."""

import numpy as np
followers = np.array([1200, 15000, 67000, 340000, 125000])
print(followers)
print(followers.shape)
print(followers.ndim)
print(followers.dtype)


"""3. Use np.arange() to generate an array of order IDs for 10 consecutive Zomato orders starting from 101. 
    Print the array and its size."""

import numpy as np
order_id = np.arange(101, 111)
print(order_id)
print(order_id.size)

"""4. Create a 3x3 NumPy array using np.eye() to represent a 'like' identity matrix for a new Spotify playlist 
    feature. Print the matrix and explain what the diagonal values represent in a comment."""

import numpy as np
like_matrix = np.eye(3)
print(like_matrix)
'''Diagonal values represent that each Spotify playlist match it self.
Playlist 1 - match it self (1.)
Playlist 2 - match it self (1.)
Platlist 3 - match it self (1.)
'''

"""5. Convert a Python list of cricket scores [45, 67, 120, 89, 54] to a NumPy array, then use the .
    itemsize attribute to print how many bytes each score takes in memory.
    <br><br><em><strong>Hint:</strong> Use np.array() for conversion and .itemsize for memory size.</em>"""

import numpy as np
score = np.array([45, 67, 120, 89, 54])
print("Bytes per score :",score.itemsize) 


