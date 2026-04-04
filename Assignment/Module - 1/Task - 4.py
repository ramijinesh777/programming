# Question - 4
# Write a Python program to 
# get a single string from two given strings, 
# separated by a space and 
# swap the first two characters of each string.

# Define string or get input by user
a = input("Enter string 1 : ")  # a = Python
b = input("Enter string 2 : ")  # b = Java

# Swap first 2 characters
a1 = b[:2] + a[2:]
b1 = a[:2] + b[2:]

# Join both string & give space in between
str = a1 +" "+b1

print("Final Result : ",str)