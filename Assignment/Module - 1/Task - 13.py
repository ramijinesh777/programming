""" Questation : 13 --> WAP to sort a dictionary (ascending /descending) by value. """
d = {'a': 300, 'b': 100, 'c': 200, "d": 400}

# Sort by Value (Ascending)
def get_value(item):       # returns value (index 1)
    return item[1]         # return value part

items = list(d.items())    # its convert in list of tuples[('a',300), ('b',100), ('c',200), ("d",400)]
items.sort(key=get_value)  # sort using returned value

print(dict(items))         # converts back in to dictionary



# Sort by Value (Descending)
def get_value(item):        # returns value (index 1)
    return item[1]          # return value part

items = list(d.items())     # its convert in list of tuples[('a',300), ('b',100), ('c',200), ("d",400)]
items.sort(key=get_value, reverse=True) # reverse = True sort in reverse order

print(dict(items))          # converts back in to dictionary