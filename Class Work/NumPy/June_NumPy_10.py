# numpy  :  pip install numpy  
"""
1 string  2. list  3 tuple  4 set  5 dict 

numpy  : 
why  is important in DS / DA ? 

1. num operation 
2. faster 
3. statistics 
4. time  
5. matrix 
"""
###############################################################################################
# create array  : 
import  numpy as np 


# a= np.array([1,2,3,4,5,6])
# print(a)
# print(a.ndim)  # number dimenstional 
# a[2] =90
# print(a)

###############################################################################################
"""
b= np.array([
    [1,2,3], 
    [4,5,6]
])
print(b)
print(b.ndim)
b[1] =90 
print(b)
b[1,2] =900  # row  1, col 2
b[0,0] =400  # row  0, col 0
print(b)"""

###############################################################################################
# Array  Attributes  : ndim, shape, itemsize, dtype 
###############################################################################################
"""
arr =np.array([1,2,3,90,901])

b= np.array([
    [1,2,3], 
    [4,5,6]
])"""

# print(arr)
# print(arr.dtype)    # int 
# print(arr.ndim)     # 1 
# print(arr.shape)    # (5, )
# print(b.shape)      # (2,3)
# print(arr.itemsize) # 8

###############################################################################################
# Method  : np.arange , np.one , np.zero , np.full , np.linspace
###############################################################################################


# a=np.arange(10)     
# print(a)                       # [0 1 2 3 4 5 6 7 8 9] - op

# b= np.arange(1,10,3)           # start  :1  stop :10  step :3 
# print(b)                       # [1 4 7] - op

# c= np.ones(10,dtype=int)       # [1 1 1 1 1 1 1 1 1 1] - 10 time 1
# c= np.ones((3,2),dtype=int)    # 3 row & 2  col  - data type convert in int
# print(c)                       # 3 row & 2  col of 1

# d =np.zeros(10,dtype=int)      # [0 0 0 0 0 0 0 0 0 0] - 10 time 0
# d =np.zeros((2,3),dtype=int)   # 2 row & 3  col  - data type convert in int
# print(d)                       # 2 row & 3  col of 0

# e= np.full((2,3),100,dtype=int)  # 100
# print(e)

# f= np.linspace(1,10,3),dtype=int
# print(f)                       # [1., 5.5, 10.] - op

# formula  : 
"""
stop - start / step -1    # 10 -1 / 3-1 ===> 4.5 
"""
###############################################################################################
# Reshape : 
###############################################################################################

# a=np.arange(10)
# print(a)
# print(a.reshape(2,5))

# b= np.ones(10).reshape(5,2)
# print(b)

###############################################################################################
# identity  matrix : 
###############################################################################################
"""
1 0 0    
0 1 0 
0 0 1


a=np.eye(3)
print(a)"""

###############################################################################################
# transpose  :
###############################################################################################

# b= np.arange(9).reshape(3,3)
# print(b)
# transpose = b.T
# print(transpose)            # converts row into col


# list  : 
# l1= [1,2,3,4,5] 
# l2 = l1                     # both l1 & l2 change
# l2 = l1.copy()              # only l2 change
# l2[2] = 900 
# print("l1 is  : ",l1)
# print("l2 is  : ",l2)


##########################################################################################################
""" 
Task  : 1 reshape 1d   ===> convert  2d 
Task  : 2  list  : 1st letter and  last letter must be same  then append in another  list and length must  
        be 3 or more than 3 

input  :l1 = ["aba" ,"1221" ,"php","python","xyz"]
output  : l1 = ["aba" ,"1221" ,"php"] """

# l1 = ["aba" ,"1221" ,"php","python","xyz"]
# l2 = []

# for i in l1:
#     if len(i) >= 3 and i[0] == i[-1]:
#         l2.append(i)
# print(l2)
##########################################################################################################
