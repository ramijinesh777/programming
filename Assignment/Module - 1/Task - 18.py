""" Questation : 18 --> 
Python Program to Find Factorial of Number Using Recursion
"""

def factorial(n):                           # Creat function for factorial
    if n == 0 or n == 1:                    # Base condition
        return 1
    else:
        return n * factorial(n-1)           # Recursive call

num = int(input("Enter a number: "))
result = factorial(num)

print("Factorial of", num, "is", result)