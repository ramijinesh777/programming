"""1. Create two NumPy arrays representing the daily step counts of two friends over a week and use 
element-wise addition, subtraction, multiplication, and division to compare their activity levels."""

import numpy as np
friend1 = np.array([8000, 9500, 10000, 8500, 11000, 12000, 8500])
friend2 = np.array([6900, 8500, 8400, 8100, 9800, 11600, 9600])

print("Addition:", friend1 + friend2)
print("Subtraction:", friend1 - friend2)
print("Multiplication:", friend1 * friend2)
print("Division:", friend1 / friend2)


"""2. Simulate a Spotify-like 'Recommended Songs' feature: Given two 3x3 matrices representing user-song 
interaction scores (user preferences and song popularity), use dot() and matmul() to compute the final 
recommendation matrix and explain the difference between the two results."""

import numpy as np

preferences = np.array([
    [5, 3, 2],
    [4, 1, 3],
    [2, 4, 5]                       # row = user
])                                  # col = music type

popularity = np.array([
    [2, 4, 1],
    [3, 1, 5],
    [4, 2, 3]                       # row = music type
])                                  # col = song
recommendation_dot = preferences.dot(popularity)
print(recommendation_dot)                                   # Using .dot()

recommendation_matmul = np.matmul(preferences, popularity)  # Using .matmul()
print(recommendation_matmul)

"""Difference :
--> dot() : Works for 1D, 2D, and higher dimensions & differently depending on array dimensions
--> matmul() : Specifically meant for matrix multiplication and use full in ML"""



"""3. Given a 4x4 NumPy matrix representing the pixel brightness of a small Instagram image, use 
transpose (T) to rotate the image and then calculate the mean, median, standard deviation, and 
variance of the pixel values."""

import numpy as np
insta_image = np.array([
                       [10,20,30,40],
                       [50,60,70,80],
                       [90,100,110,120],
                       [130,140,150,160]
])
print(insta_image)
rotated = insta_image.T
print(rotated)
print(np.mean(insta_image))     # Avg brightness
print(np.median(insta_image))   # Middle brightness
print(np.std(insta_image))      # Spread out pixel values
print(np.var(insta_image))      # Spread of data squared


"""4. Take a 3x3 NumPy matrix representing a Zomato restaurant rating correlation grid and 
use np.linalg.inv(), np.linalg.det(), and np.linalg.eig() to compute its inverse, determinant, and 
eigenvalues/eigenvectors.<br><br><em><strong>Hint:</strong> If the matrix is not invertible, 
modify one value and try again.</em>"""

import numpy as np
ratings = np.array([
    [8,4,2],
    [0,9,6],
    [4,2,8]
])
print(ratings)
det = np.linalg.det(ratings)
print(det)

inverse = np.linalg.inv(ratings)
print(inverse)

eigenvalues, eigenvectors = np.linalg.eig(ratings)
print(eigenvalues)
print(eigenvectors)


"""5. Create a NumPy array of shape (2, 6) representing the number of orders placed on Swiggy in 
two cities over 6 days. Reshape it to (3, 4), flatten it, split it into two equal parts, and then 
stack both parts vertically.
"""
import numpy as np
orders = np.array([
    [100,130,160,150,140,170],
    [120,110,170,160,150,180]
])
print(orders)
print(orders.shape)

reshaped = orders.reshape(3,4)      # Reshape in (3,4)
print(reshaped)

flat = reshaped.flatten()           # Use flatten 
print(flat)

split1, split2 = np.split(flat,2)   # Use split
print(split1)
print(split2)

stack = np.vstack((split1,split2))  # Use vstack 
print(stack)
