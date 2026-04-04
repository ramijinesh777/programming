# Conditional Statement - Basic

# Positive or Negative ----------------------------------------------------------------------
# Write a program to check whether a number is positive, negative, or zero.
# n = int(input("Enter any number : "))
# if (n == 0):
#     print("Your entered Value is ZERO")
# elif (n<=-1):
#     print("You Entered NEGATIVE Value")
# else:
#     print("You Entered POSITIVE Value")


# Even or Odd -----------------------------------------------------------------------------
# Write a program to check whether a number is even or odd.
# n = int(input("Enter Number : "))
# if (n == 0):
#     print("Your entered Number is not ODD or EVEN")
# elif(n%2 == 0):
#     print("Your entered EVEN number : ",n)
# else:
#     print("Your entered ODD Number : ",n)


# Voting Eligibility ------------------------------------------------------------------------
# Write a program to check if a person is eligible to vote (age ≥ 18).
# age = int(input("Enter your age : "))
# if (age >= 18):
#     print("You can Vote..!!")
# else:
#     print("You Can't Vote")


# Largest of Two Numbers ---------------------------------------------------------------------
# Write a program to find the largest of two numbers.
# a = int(input("Enter 1st Number : "))
# b = int(input("Enter 2nd Number : "))
# if (a > b):
#     print("Largest number is A : ",a)
# else:
#     print("Largest number is B : ",b)


# Pass or Fail -------------------------------------------------------------------------------
# Write a program to check if a student passes or fails.
# Condition: Marks ≥ 35 = Pass, otherwise Fail.
# marks = int(input("Enter your marks : "))
# if (marks >= 35):
#     print("You are PASS in this subject")
# else:
#     print("You are FAIL in this subject")

############################################# Intermediate Level ############################################
# Largest of Three Numbers ----------------------------------------------------------------------------------
#Write a program to find the largest among three numbers.
# a = int(input("Enter 1st Number : "))
# b = int(input("Enter 2nd Number : "))
# c = int(input("Enter 3rd Number : "))

# if(a>b and a>c):
#     print("1st Number A is largest : ",a)
# elif(b>a and b>c):
#     print("2nd Number B is largest : ",b)
# else:
#     print("3rd Number c is largest : ",c)


# Leap Year Check ------------------------------------------------------------------------------------------
# Write a program to check whether a year is a leap year or not.
# year = int(input("Enter Year : "))
# if(year % 4 == 0 and year % 100 != 0): # if (year % 400 == 0):
#     print(year,"is Leap Year..!!")
# else:
#     print(year,"is not Leap Year..!!")    


# Grade System ---------------------------------------------------------------------------------------------
# Write a program to print grade based on marks:

# 90+ → Grade A
# 75–89 → Grade B
# 50–74 → Grade C
# Below 50 → Fail

# marks = int(input("Enter your Marks : "))
# if(marks>=90 and marks<=100):
#     print("You get A grade")
# elif(marks>=75 and marks<=89):
#     print("You get B grade")
# elif(marks>=50 and marks<=74):
#     print("You get C grade")
# else:
#     print("You are Fail...!!!")


# Divisible Check ------------------------------------------------------------------------------------------
# Write a program to check whether a number is divisible by both 5 and 11.
# n = int(input("Enter number : "))
# if (n%5 == 0 and n%11 == 0):
#     print("Entered number is Divisable by both 5 and 11")

# else:
#     print("Not Divisable by both 5 and 11")
        

# Number Comparison ----------------------------------------------------------------------------------------
# Take two numbers and check:

# if first number is greater
# if second number is greater
# or both are equal

# a = int(input("Enter 1st Number : "))
# b = int(input("Enter 2nd Number : "))

# if(a>b):
#     print("1st Number A is Largest : ",a)
# elif(b>a):
#     print("2nd Number B is Largest : ",b)
# else:
#     print("1st & 2nd Number both are equal : ",a and b)


############################################# Challenge Level ############################################
# Calculator Using Conditional Statements ----------------------------------------------------------------
# Take two numbers and an operator (+, -, *, /) and perform the operation.
# a = float(input("Enter 1st Number : "))
# b = float(input("Enter 2nd Number : "))

# print("Select any operation")
# print("1. Plus")
# print("2. Minus")
# print("3. Multiply")
# print("4. Divide")

# select = input("Select any one operation (1/2/3/4) : ")
# if (select == "1"):
#     print("Result : ",a+b)
# elif (select == "2"):
#     print("Result : ",a-b)
# elif (select == "3"):
#     print("Result : ",a*b)
# elif (select == "4"):
#     print("Result : ",a/b)
# else:
#     print("Invalid Choice")


# Find Smallest Number -----------------------------------------------------------------------------------
# Write a program to find the smallest among three numbers.

# a = int(input("Enter 1st Number : "))
# b = int(input("Enter 2nd Number : "))
# c = int(input("Enter 3rd Number : "))
# if(a<b and a<c):
#     print("Smallest Number is 1st : ",a)
# elif(b<a and a<c):
#     print("Smallest Number is 2nd : ",b)
# else:
#     print("Smallest Number is 3rd : ",c)


# Check Alphabet Type ------------------------------------------------------------------------------------
# Input a character and check whether it is: Vowel or Consonant

# char = input("Enter character : ")
# if char in ("a","e","i","o","u","A","E","I","O","U"):
#     print("Its Vowel...!!")
# else:
#     print("Its Consonant...!!")


# Temperature Check --------------------------------------------------------------------------------------
# Print message based on temperature:

# Above 35 → Hot
# 20–35 → Normal
# Below 20 → Cold

# temp = float(input("Enter Temperature : "))
# if (temp > 35):
#     temp = "HOT"
# elif (temp>=20 and temp<=35):
#     temp = "NORMAL"
# else:
#     temp = "COLD"

# print("Temperature is : ",temp)

# Number Range Check -------------------------------------------------------------------------------------
# Check whether a number is between 1 and 100

# num = int(input("Enter number : "))
# if(num>=1 and num<=100):
#     print("The number is between 1 to 100")
# else:
#     print("The number is not between 1 to 100")
