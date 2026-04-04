
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

##############################################################################

# Example : Choice Menu (Menu driven)

# while True:
#     menu = """ 
#     press 1 for Prime Number
#     press 2 for Factorial
#     press 3 for Reverce Number
#     press 4 for Exit
#     """

#     print(menu)
#     choice = int(input("Enter Choice : "))

#     def prime_num():
#         n = int(input("Enter Number : "))
#         prime = 0
#         for i in range(1, n+1):
#             if(n%i == 0):
#                 prime += 1
#             if prime == 2:
#                 print("Prime Number")
#             else:
#                 print("Not Prime Number")
    
#     def fact_num():
#         n = int(input("Enter Number : "))
#         fact = 1

#         for i in range(1, n+1):
#             fact *= i
            
#         print("Factorial : ",fact)

#     def reverse_num():
#         n = int(input("Enter Number : "))
#         rem = 0
#         rev = 0

#         while(n != 0):
#             rem = n%10
#             rev = rev*10+rem
#             n = n//10

#         print("Reverse Number : ",rev)

#     if choice == 1:
#         prime_num()

#     elif choice == 2:
#         fact_num()

#     elif choice == 3:
#         reverse_num()

#     elif choice == 4:
#         print("Thanks...!!")
#         break

#     else:
#         print("Invalid Choice")
#         break

###########################################################################################
while True:
    menu = """
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit
    """
    print(menu)
    choice = int(input("Enter your choice : "))

    def add():
        a = int(input("Enter Number : "))
        b = int(input("Enter Number : "))
        print("Sum is : ", a+b)

    def sub():
        a = int(input("Enter Number : "))
        b = int(input("Enter Number : "))
        print("Subtraction is : ", a-b)

    def multi():
        a = int(input("Enter Number : "))
        b = int(input("Enter Number : "))
        print("Multiplication is : ", a*b)

    def divi():
        a = int(input("Enter Number : "))
        b = int(input("Enter Number : "))
        if (a != 0):
            print("Division is : ", a/b)
        else:
            print("Cant Divided by zero")


    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        multi()
    elif choice == 4:
        divi()
    elif choice == 5:
        print("Thanks...!!!")
        break
    else:
        print("Invalid Choice..!!!")
        break