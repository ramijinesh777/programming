""" Questation : 14 --> WAP to find the highest 3 values in a dictionary. """
d = {'a': 300, 'b': 100, 'c': 200, 'd': 400, 'e': 500}

values = list(d.values())               # get values
values.sort(reverse=True)               # sort in ascending order
top3 = values[ : 3]                     # first 3 highist values
print("Highest of 3 values : ",top3)
