# Functions:

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

##############################################################################

# Example : Choice Menu (Menu driven)

while True:
    menu = """ 
    press 1 for Prime Number
    press 2 for Factorial
    press 3 for Reverce Number
    press 4 for Exit
    """

    print(menu)
    choice = int(input("Enter Choice : "))

    def prime_num():
        n = int(input("Enter Number : "))
        prime = 0
        for i in range(1, n+1):
            if(n%i == 0):
                prime += 1
            if prime == 2:
                print("Prime Number")
            else:
                print("Not Prime Number")
    
    def fact_num():
        n = int(input("Enter Number : "))
        fact = 1

        for i in range(1, n+1):
            fact *= i
            
        print("Factorial : ",fact)

    def reverse_num():
        n = int(input("Enter Number : "))
        rem = 0
        rev = 0

        while(n != 0):
            rem = n%10
            rev = rev*10+rem
            n = n//10

        print("Reverse Number : ",rev)

    if choice == 1:
        prime_num()

    elif choice == 2:
        fact_num()

    elif choice == 3:
        reverse_num()

    elif choice == 4:
        print("Thanks...!!")
        break

    else:
        print("Invalid Choice")
        break