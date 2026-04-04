# Example : Choice Menu (Menu driven)

###############################################################################
# Menu driven Control Statement : Calculator Program
###############################################################################

while True:
    menu = """
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit
    """
    print("Calculator Program")
    print(menu)
    choice = int(input("Enter your choice : "))

    if choice == 1:
        a = int(input("Enter Number : "))
        b = int(input("Enter Number : "))
        print("Sum is : ", a+b)

    elif choice == 2:
        a = int(input("Enter Number : "))
        b = int(input("Enter Number : "))
        print("Subtraction is : ", a-b)

    elif choice == 3:
        a = int(input("Enter Number : "))
        b = int(input("Enter Number : "))
        print("Multiplication is : ", a*b)

    elif choice == 4:
        a = int(input("Enter Number : "))
        b = int(input("Enter Number : "))
        if (a != 0):
            print("Division is : ", a/b)
        else:
            print("Cant Divided by zero")

    elif choice == 5:
        print("Thanks...!!!")
        break
    else:
        print("Invalid Choice..!!!")
        break


############################################################################################
# Menu Driven Programming : 
#############################################################################################
while True:
    menu = """ 
    press 1 for Prime Number
    press 2 for Factorial
    press 3 for Reverce Number
    press 4 for Exit
    """

    print(menu)
    choice = int(input("Enter Choice : "))

    if choice == 1:
        n = int(input("Enter Number : "))
        prime = 0
        for i in range(1, n+1):
            if(n%i == 0):
                prime += 1

        if prime == 2:
            print("Prime Number....!!!")
        else:
            print("Not Prime....!!!!")

    elif choice == 2:
        n = int(input("Enter Number : "))
        fact = 1

        for i in range(1, n+1):
            fact *= i
            i += 1

        print("Factorial : ",fact)

    elif choice == 3:
        n = int(input("Enter Number : "))
        rem = 0
        rev = 0

        while(n != 0):
            rem = n % 10   
            rev = rev*10+rem      
            n = n//10             
        print("Reverce Num : ",rev)

    elif choice == 4:
        print("Thanks...!!")
        break

    else:
        print("Invalid Choice")
        break




