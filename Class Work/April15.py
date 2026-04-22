# Tuple : 
"""  
Tuple is a collection that stores the data in single variable 
-> Its denoted by ( )
-> Tuple is immutable
-> Its allows duplicate valus
-> Its faster then list
"""

t = (1,2,3,1,2,4)

print(t.count(1))
print(t.index(1))

l = list(t)
l.append(100)

t1 = tuple(l)
print(t1)