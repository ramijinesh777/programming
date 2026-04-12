""" Questation : 9 --> 
WAP to find the second smallest number in a list.
"""

list = [1,1,3,9,5,8]
list.sort() == list
# Step : 1 - Find uni number
new_list = [ ]

for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)
print("Second smallest number is : ",new_list[1])

