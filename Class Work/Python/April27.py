# Recursion ::::::::::::::::::::::::::::::
""" 
Function call it self called recursion
loop, fac, prime, fibo
cut problem into small problem
1. Base case
2. Recursive case
"""

# Factorial Numer
# def fac(n):
#     if n==0:
#         return 0
#     if n ==1:
#         return 1
#     else:
#         return n*fac(n-1)
    
# n = int(input("Enter Number : "))
# print(fac(n))

# Fibonachi Number

# def fibo(n):
#     if n==0:
#         return 0
#     if n ==1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
# print(fibo(10))
#################################################################
# Fibonachi Number

# def fibo(n):
#     if n==0:
#         return 0
#     if n ==1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
    
# n = int(input("Enter Number : "))
# print("fibonacci Series : ")
# for i in range(n):
#     print(fibo(i),end=" ")
##################################################################
# def fibo(n):
#     if n <= 1:
#         return n
#     return fibo(n-1) + fibo(n-2)


# def print_series(n, i=0):
#     if i == n:
#         return
#     print(fibo(i), end=" ")
#     print_series(n, i+1)


# n = int(input("Enter number: "))
# print_series(n)
