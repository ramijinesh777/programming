""" Questation : 17 --> 
WAP using function to find the sum of odd series and even series
Odd series: 12/ 1! + 32/ 3! + 52/ 5!+……n
Even series: 22/ 2! + 42/ 4! + 62/ 6!+……n
"""

def factorial(n):               # Create function to find factorial
    fact = 1                        # in fact variable we store result  
    for i in range (1, n+1):        # loop run from 1 to n
        fact *= i                   # multiply each num with fact.
        return fact                 # its returns final factorial value
    
def odd_num(n):                 # Create function to find odd number
    sum = 0                         # in sum variable we store sum 
    for i in range(1, n+1, 2):      # loop start from 1 increase by 2
        sum += i * i / factorial(i) # i * i = i squre , factorial(i) call factorial function
    return sum                      # return sum of odd number

def even_num(n):                # Create function to find even number
    sum = 0                         # in sum variable we store sum 
    for i in range(2, n+1, 2):      # loop start from 2 increase by 2
        sum += i * i / factorial(i) # i * i = i squre , factorial(i) call factorial function
    return sum                      # return sum of even number

n = int(input("Enter value of n : "))       # main program to input value of n
print("Sum of odd number : ",odd_num(n))    # print sum of odd number
print("Sum of even number : ",even_num(n))  # print sum of even number