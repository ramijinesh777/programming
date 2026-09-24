# import numpy as np
# a = np.array([1,2,3,4,5,6])
# print(a)
# a[2] = 27
# print(a)


# import numpy as np
# b = np.array([
#     [1,2,3],
#     [4,5,6]
# ])
# print(b)
# print(b.ndim)
# b[1]=90
# print(b)
# b[1,2] = 900
# b[0,0] = 400
# print(b)


###### attributes ######
# array  attributes  : ndim shape itemsize dtype
# import numpy as np
# arr = np.array([1,2,3,50,60,700])
# print(arr)
# print(arr.dtype)
# print(arr.ndim)
# print(arr.shape)
# print(arr.itemsize)


###### method ###### 
# np.one , np.zero ,np.full , np.arange , np.linspace
# import numpy as np
# a = np.arange(10) # start, stop , step
# print(a)

# b = np.arange(1,10,3)
# print(b)

# c = np.ones(10)
# c = np.ones(10,dtype=int)
# c = np.ones((2,3),dtype=int)
# print(c)

# d = np.zeros(10)
# d = np.zeros(10,dtype=int)
# d = np.zeros((2,3),dtype=int)
# print(d)

# e = np.full((2,3),100,dtype=int)
# print(e)

# f = np.linspace(1,10,3) # stop-start/step-1
# print(f)                # 10-1/3-1 = 4.5

###### reshape ######
# a = np.arange(10)
# print(a)
# print(a.reshape(2,5))

# b = np.ones(10).reshape(5,2)
# print(b)

###### identity matrix ######
# import numpy as np
# a = np.eye(3)
# print(a)

""" 1 0 0
    0 1 0
    0 0 1 """ # output


###### transpose ######
# import numpy as np
# a = np.arange(9).reshape(3,3)
# print(a)
# transpose = a.T
# print(transpose) # col convert in row


###### list ######
# l1 = [1,2,3,4,5,6]
# # l2 = l1           # Both l1 & l2 Change
# l2 = l1.copy()      # Only l2 Change
# l2[2] = 900
# print("l1 is : ",l1)
# print("l2 is : ",l2)


####### Task : 1 - reshape 1D ==> 2D #######
""" l1=["aba" ,"1221" ,"php","python","xyz","0000"]"""

# import numpy as np
# l1 = ["aba" ,"1221" ,"php","python","xyz","0000"]
# arr = np.array(l1).reshape(2,3)
# print(arr)


""" Lacture : 2 """
# indeding : 1D array
import numpy as np
# a = np.array([10,20,30,40,50,60,70,80,90])
# print(a)
# print(a[2])             # 30
# print(a[2:5])           # 30,40,50
# print(a[-1])            # 90
# print(a[4 :-2])         # 50,60,70
# print(a[4 :])           # 50,60,70,80,90
# print(a[-2 :])          # 80,90
# print(a[-2 : -5 :-1])   # 80,70,60
# print(a[-5 : -2])       # 50,60,70

# indeding & slicing: 2D array
# import numpy as np
# b = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])

# print(b)
# print(b[2])
# print(b[1:3])
# print(b[1:3,0:1])
# print(b[1:2,1:2])

# indeding & slicing: 3D array
# import numpy as np
# c = np.array([
#     [
#         [1,2],
#         [3,4]
#     ],
#     [
#         [11,12],
#         [13,14]
#     ]
# ])
# print(c)
# print(c[1,1,1]) # 14


# Extra : 
# import numpy as np
# a = np.arange(1,33).reshape(2,2,2,4)
# print(a)
# print(a[1,1,1,1])


# Boolean indexing : condition apply
import numpy as np
# a = np.array([1,-2,3,-4,5,6])
# print(a)
# print(a>0)
# result = a[a<0]
# print(result)

# negative value replace with 10.
# a = np.array([1,-2,3,-4,5,6])
# a[a<0] = 10
# print(a)

# 2D array
b = np.array([
    [1,-2,3],
    [4,5,6],
    [7,8,-9]
])
print(b[b<0])
b[b<0] = 100
print(b<0)
# print(b)


