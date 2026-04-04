# Question - 1 
# Write a python program to sum of the first n positive integers.

n = int(input("Enter Number : "))
i = 1
sum = 0
if n < 0:
    print("Enter Positive Number..!!")
else: 
    while i <= n:
        sum += i
        i += 1

    print("SUM = ",sum)

##################################################

n = int(input("Enter Number : "))
sum = 0

if n < 0:
    print("Enter Positive Number..!!")

else: 
    for i in range(1, n+1):
        sum += i

    print("SUM = ",sum)
