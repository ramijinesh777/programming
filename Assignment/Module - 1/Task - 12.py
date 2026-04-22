""" Questation : 12 --> WAP to convert a list of tuples into a dictionary. """
l = [('a',100), ('b',200), ('c',300),('d',400)]

d = { }                 # Creat empty dictionary.

for i in l:             # Run loop in given list in each tuple
    k = i[0]            # 1st element = key
    v = i[1]            # 2nd element = value
    d[k] = v            # Insert in dict..
print(d)                # print updated dict..