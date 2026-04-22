""" Questation : 15 --> 
Given a number n, write a python program to make and print the list of Fibonacci series up to n.
Input : n=7
Hint : first 7 numbers in the series
Expected output :
First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13 """

n = 7

fib = [0, 1]                            # fib number always start with 0 and 1

for i in range(2, n+1):                 # start from index 2 to n+1
    next_num = fib[i-1] + fib[i-2]      # for find next num. start with i=2 then 3 to 7.
    fib.append(next_num)                # add new number to list.

print("First few Fibonacci numbers are:", fib)

