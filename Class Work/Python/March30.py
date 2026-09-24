###########################################################################
# Type : 1 --> Function without parameters & without return type
###########################################################################
# def fun1(): #defination
#     n = int(input("Enter Number : "))
#     if(n%2 == 0):
#         print("EVEN NO..!!")
#     else:
#         print("ODD..!!")

# fun1() # call

###############################################################

# def fact():
#     n = int(input("Enter Number : "))
#     fac = 1

#     for i in range(1, n+1):
#         fac *= i
#     print("Factorial : ",fac)
# fact()

###############################################################

# def revrse():
#     n  = int(input("Enter Number : "))
#     rem = 0
#     rev = 0

#     while(n != 0):
#         rem = n % 10   
#         rev = rev*10+rem     
#         n = n//10             
#     print(rev)
# revrse()

#################################################################
# def prime():
#     n = int(input("Enter Number : "))
#     prime = 0

#     for i in range(1, n+1):
#         if(n%i == 0):
#             prime += 1
#     if prime == 2:
#         print("Even Number ..!!")
#     else:
#         print("Odd Number..!!")

# prime()


###########################################################################
# Type : 2 --> Function with parameters without return type
###########################################################################

# def greter(n1,n2,n3): # parameters
#     if n1>n2 and n1>n3:
#         print(n1, "is greater")
#     elif n2>n1 and n2>n3:
#         print(n2, "is greater")
#     else:
#         print(n3, "is greater")

# n4 = int(input("Enter Number 1 : "))
# n5 = int(input("Enter Number 2 : "))
# n6 = int(input("Enter Number 3 : "))

# greter(n4, n5, n6) # arguments

#####################################################################

# def reverse(n):
#     rev = 0
#     rem = 0

#     while (n!=0):
#         rem = n%10
#         rev = rev*10+rem
#         n = n//10
#     print("Reverse Number : ", rev)
# n = int(input("Enter Number : "))
# reverse(n)

########################################################################

# def palindrom(n):
#     rev = 0
#     rem = 0
#     n1 = n

#     while(n!=0):
#         rem = n%10
#         rev = rev*10+rem
#         n = n//10
#     if n1 == rev:
#         print("Its Palindrom Number...!!!")
#     else:
#         print("Not Palindrome...!!!")
# n = int(input("Enter Number : "))
# palindrom(n)

###########################################################################
# Type : 3 --> Function without parameters with return type
###########################################################################
# WAF of factorial

# def factorial():
#     n = int(input("Enter Number : "))
#     fact = 1

#     for i in range (1, n+1):
#         fact *= i

#     return fact
# fact = factorial()
# print("Factorial is : ",fact) # print(factorial())

###########################################################################
# Type : 4 --> Function with parameters with return type
###########################################################################

# def greter(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
    
# gretest = greter(10,20,30)
# print("Gretest Number is : ",gretest)







