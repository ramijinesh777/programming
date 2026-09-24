""" task :1 Get the following array using intrinsic methods and slicing: using np.ones + slicing 

1 1 1 1 1
1 0 0 0 1
1 0 9 0 1
1 0 0 0 1
1 1 1 1 1 """

# import numpy as np
# arr = np.ones((5,5), dtype=int)
# arr[1:4, 1:4] = 0
# arr[2,2] = 9
# print(arr)

""" task :2 array shown below using advanced indexing : using  np.arange + slicing 

1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
26 27 28 29 30	

output  : 
[[11,12],
[16,17]] """

# import numpy as np
# arr = np.arange(1,31).reshape(6,5)
# print(arr)

# output = arr[2:4, 0:2]
# print(output)
 

""" task :3 using  np.arange()  create the array  (5,6)
input  : 
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
26 27 28 29 30	

output  :[[2,8,14,20]] """

# import numpy as np
# arr = np.arange(1,31).reshape(5,6)
# print(arr)
# output = arr[[0,1,2,3],[1,1,1,1]]
# print(output.reshape(1, 4))


""" task :4  using  np.arange()  create the array  (5,6)
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
26 27 28 29 30	

output : 
[[4,5],
[24,25],
[29,30]] """

# import numpy as np
# arr = np.arange(1,31).reshape(6,5)
# print(arr)
# output = arr[[0,4,5], 3:5]
# print(output)

