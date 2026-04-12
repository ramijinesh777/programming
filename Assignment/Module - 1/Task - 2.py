# Question - 2
# Write a Python program to count occurrences of a substring in a string.

str = input("Enter main string : ").lower()       # "python program and java program"
sub_str = input("Enter sub string : ").lower()    # "program"


count = str.count(sub_str)
print("Occurrence : ",count)
