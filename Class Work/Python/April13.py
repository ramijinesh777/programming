# Sorting : Algorithms Methods
"""  
1) Bubble Sort
2) Quick Sort
3) Merge Sort
4) Selection Sort
5) Insertion Sort
6) Heap Sort
"""
#######################################################################################
# WAP assending given list through bubble sort methods

l = [10,18,36,21,9,54,31]

for i in range (0,len(l)):
    for j in range(i+1,len(l)):
        if(l[i]<l[j]):
            l[j],l[i]=l[i],l[j]
print(l)


######################################################################################
# WAP assending given list through center swap methods

# l = [22,33,46,52,31]

# left = 0
# right = len(l)-1

# while (left < right):
#     l[right],l[left] = l[left],l[right]
#     left += 1
#     right -= 1

# print(l)

#########################################################################################

# l = [22,33,46,52,31,99,10,2]

# n = len(l)

# for i in range(n):
#     left = 0
#     right = 1

#     while right < n:
#         if l[left] > l[right]:
#             l[left], l[right] = l[right], l[left]
#         left += 1
#         right += 1

# print(l)

##############################################################################################
# WAP of  Merge Sort   (easy way):

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2      # Find center
#         left = arr[:mid]         # Left half
#         right = arr[mid:]        # Right half

#         # Recursively sort both halves
#         merge_sort(left)
#         merge_sort(right)

#         i = j = k = 0

#         # Merge the two halves
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i += 1
#             else:
#                 arr[k] = right[j]
#                 j += 1
#             k += 1

#         # Check if any element left
#         while i < len(left):
#             arr[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             arr[k] = right[j]
#             j += 1
#             k += 1


# # Example
# l = [22, 33, 46, 52, 31, 99, 10, 2]
# merge_sort(l)
# print("Sorted List:", l)




