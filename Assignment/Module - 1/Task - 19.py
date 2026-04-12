""" Questation : 19 --> 
Write a Python function that takes a list and returns a new list with unique elements 
of the first list."""

def unique_list(list):              # Creat function
    new_list = [ ]                  # Create empty list for uniqe number

    for i in list:                  # Run loop to check each element in list 
        if i not in new_list:       # check if its in uni
            new_list.append(i)      # If not add it 
    return new_list


list = [10,20,30,10,20,40,50]
result = unique_list(list)

print("Unique List is : ",result)
