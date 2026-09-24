""" Example : Find occurance if string."""

# s = input("Enter Name : ")
# d = { }

# for i in s:
#     if i in d:
#         d[i] += 1

#     else:
#         d[i] = 1

# print(d)

""" Example : 2 -- WAP of list and sublist in key value pair."""
# l = [1,4,6]
# l1 = [89,23,34]

# d = { }

# for i in range (len(l)):
#     d[l[i]] = l1[i]
# print(d)

""" Example : 3 -- WAP of dict and dict1 in key : value pair, and update same key in value plus """
# Class Work #
# d = {'p':100,'q':200,'r':100}
# d1 = {'p':300, 'q':400}
# ans = {}

# for i,j in d.items():
#     for k,l in d1.items():
#         if i==k:
#             ans[i]=j+l
#         else:
#             ans[i]=j
# print(ans)

######################################### HOme Work #################################
d = {'p':100,'q':200,'r':100}
d1 = {'p':300, 'q':400}
ans = {}

for i,j in d.items():
    ans[i] = j
    for k,l in d1.items():
        if i == k:
            ans[i] = j+l
print(ans)
