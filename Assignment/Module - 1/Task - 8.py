""" Questation : 8 --> 
WAP to check whether a list contains a sublist.
"""

list = [1,2,3,4,5]
sub_list = [4,5]

found = False # assume that sub_list is not in list

for i in range (len(list) - len(sub_list) + 1): # range(5 - 2 + 1) = range(4) = (0,1,2,3)
    if list[i : i+len(sub_list)] == sub_list:   # Compair each part with sub list
        found = True
        

if found:
    print("Sublist is Found : ",sub_list)
else:
    print(sub_list,": NOT Found in list")

""" 
i = 0 [0:2] - [1:2] 
i = 1 [1:3] - [2:3]
i = 2 [2:4] - [3:5]
i = 3 [3:5] - [4:5] = its equal or sub_list found
"""


