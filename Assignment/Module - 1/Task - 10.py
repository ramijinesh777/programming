""" Questation : 10 --> 
WAP to get unique values from a list.
"""

list = [10,20,30,10,20]
uni = [ ]                   # Create empty list for uniqe number

for i in list:              # Run loop to check each element in list 
    if i not in uni:        # check if its in uni
        uni.append(i)       # If not add it 
print(uni)