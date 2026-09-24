############################################################################################
# List : [ ] , It's Mutable, Oderd 
############################################################################################
""" list is a collection data type in python. We can store multiple valurs in single variable.
--> its denoted bt [ ]
--> list is mutable
--> list is orderable 
"""

#######################################################################################
""" There are some Methods / Functions of List """
#######################################################################################
""" list = [10,20,40,True,False,10.20,50.78,10,20]

list.append(100)                :   append value at the last of list.
print(list)

print(list.count(10))           :   it show count of input value

list.extend([786,"How",8005])   :   its add multiple value at the end of list
print(list)

list.insert(2,"python")         :   at perticular index value added
print(list)

list.pop()                      :   Its remove last value at the list
print(list)

list.pop(2)                     :   its remove particular value at the index
print(list)

list.remove(50.78)              :   its remove particular value which you insert
print(list)

list.reverse()                  :   its reverse whole list
print(list)
"""

################################################################################################

""" Example : 1 ==> WAP to input 1 to 30 number in empty list """
list = [ ]
for i in range (1, 31):
    list.append(i)
print(list)

""" Example : 2 ==> WAP to find even and odd number in 1 to 30 """

i = [ ]
ev = [ ]
od = [ ]

for i in range (1, 31):
    if i % 2 == 0:
        ev.append(i)
    else:
        od.append(i)

print(ev)
print(od)

""" Example : 3 ==> WAP to remove duplicat value in given list """

list = [10,20,30,10,20]
uni = [ ]

for i in list:
    if i not in uni:
        uni.append(i)
print(uni)

""" Example : 4 ==> WAP to write duplicat value in given list """

list = [10,20,30,10,20]
uni = [ ]
dup = [ ]

for i in list:
    if i not in uni:
        uni.append(i)
    else:
        dup.append(i)
print(uni)
print(dup)
