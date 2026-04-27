""" Questation : 16 --> 
Counting the frequencies in a list using a dictionary in Python.
Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]
Expected output : 1 : 5 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2
"""

input = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
d = { }                          # Create empty dictionary

for i in input:                  # Loop run each number in list
    if i in d:                   # If number already exists → increase count
        d[i] += 1
    else: 
        d[i] = 1                 # If number not exists → add it with value 1
# print(d)                       # {1: 5, 5: 2, 3: 3, 4: 3, 2: 4} 


for key in sorted(d):            # Sort dictionary keys.
    print(key, ":",d[key])       

