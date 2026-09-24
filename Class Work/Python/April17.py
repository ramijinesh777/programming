""" Dictionary in Python ----- Class-1 """

# A dictionary in Python is a built-in data type used to store data in key–value pairs.
# It is written using curly brackets {}.
# Its mutable & keys must be unique.
# key + value = item

# Example : 
d = {1:"hello",2:"welcome",3:"python"}
print(d.get(1))                     # its give 1st key value
print(d.keys())                     # its written keys only
print(d.values())                   # its written values only
print(d.items())                    # its written keys and value pair 
d.update({4:"java",5:"python"})     # its update new dict
print(d)
d.pop(2)                            # its remove perticular value which key you written
print(d)
d.popitem()                         # its remove last key : value pair
print(d)

d1 = {}
t = (46,24,21)
print(d1.fromkeys(t))
print(d1.fromkeys(t,20))