# Check Positive and Even Number
# num = int(input("Any Number : "))
# if num > 0:
#     if (num % 2 == 0):
#         print("Positive EVEN Number ..!!")
#     else:
#         print("Positive ODD Number ..!!")
# else:
#     print("Negative Number..!!")
##-------------------------------------------------------------................................

# Student Result (Nested Condition) : (Distinction : 75, First Class : 60, Pass : 35)
# marks = int(input("Enter marks : "))
# if (marks >= 35):
#     if (marks >= 75):
#         print("Distinction..!!")
#     elif (marks >= 60):
#         print("First Class..!!")
#     else:
#         print ("Pass..!!")
# else:
#     print("FAIL..!!")

##---------------------------------------------------------------------------------------------

# Age and License Check
# age = int(input("Enter your age : "))
# license = input("Do you have licence (yes or no) : ")

# if age >= 18:
#     if license == "yes":
#         print("You can drive..!!")
#     else:
#         print("You need a driving licence..")
# else:
#     print("You are under age")


#-------------------------------------------------------------------------------------------------
# Write a program to check a student's result:
# If marks ≥ 35 → Pass
# If marks ≥ 60 → First Class
# If marks ≥ 75 → Distinction
# Otherwise → Fail

# marks = int(input("Ener your marks : "))
# if (marks>= 35):
#     if (marks >= 75):
#         print("Ypu got a distinction...!!")
#     elif (marks >= 60):
#         print("Yoy got a First Class..!!")
#     else:
#         print("You are PASS..!!")
# else:
#     print("Your are FAIL..!!")

#----------------------------------------------------------------------------------------------------

# Driving Eligibility
# Write a program to check if a person can drive:
# Age must be 18 or above
# Person must have a driving license

# age = int(input("Enter your age : "))
# licence = input("Do you have a licence (Yes/No) : ")
# if (age>=18):
#     if licence == "yes" or licence == "YES" or licence =="Yes":
#         print("You can drive..!!")
#     else:
#         print("Apply for a licence..!!")
# else:
#     print("You can't drive..!!!")


#------------------------------------------------------------------------------------------------------
# Largest of Three Numbers 
# Write a program to find the largest number among three numbers using nested if

# a = int(input("Enter 1st number : "))
# b = int(input("Enter 2nd number : "))
# c = int(input("Enter 3rd number : "))

# if (a>b):
#     if(a>c):
#         print("1st Number A is largest : ",a)
#     else:
#         print("3rd Number C is Largest : ",c)
# else:
#     if(b>c):
#         print("2nd Number B is largest : ",b)
#     else:
#         print("3rd Number C is largest : ",c)

#-----------------------------------------------------------------------------------------------------
# Login System

# Write a program that checks:
# If username is correct
# Then check if password is correct
# Print Login Successful or Invalid Password.

# username = input("Enter Username : ")
# password = int(input("Enter Password : "))

# if (username == "admin"):
#     if (password == 1234):
#         print("Loged in Successfully")
#     else:
#         print("Wrong Passward -- XX")
# else:
#     print("Wrong Username..XX")


#-------------------------------------------------------------------------------------------------------
# Write a program : Number Check
# If a number is positive
# If positive, check whether it is even or odd
# Otherwise print Negative Number.

# num = int(input("Enter Number : "))
# if num > 0:
#     print("You entered POSITIVE number")
#     if num % 2 == 0:
#         print("Its EVEN number")
#     else:
#         print("Its ODD number")
# else:
#     print("You entered NEGATIVE number")

#-----------------------------------------------------------------------------------------------------
# Write a program : Voting Eligibility

# If age ≥ 18 → Eligible to vote
# If age ≥ 60 → Senior citizen voter
# Otherwise → Not eligible

# age = int(input("Enter your age : "))
# if age >= 18:
#     print("You can Vote...!!")
#     if age >= 60:
#         print("You are senior citizen voter")

# else:
#     print("You cant Vote...!!!")


#-----------------------------------------------------------------------------------------------------
# Temperature Check

# Write a program:
# If temperature > 35 → Hot
# If temperature 20–35 → Normal
# Otherwise → Cold

# temp = int(input("Enter Temperature : "))

# if temp > 35:
#     print("HOT")
# else:
#     if temp >= 20:
#         print("NORMAL")
#     else:
#         print("COLD")


#-----------------------------------------------------------------------------------------------------
# Write a program : Grade System

# If marks ≥ 90 → Grade A
# If marks ≥ 75 → Grade B
# If marks ≥ 50 → Grade C
# Otherwise → Fail

# marks = int(input("Enter your marks : "))

# if marks >= 90:
#     print("Grade A")
# else:
#     if marks >= 75:
#         print("Grade B")
#     elif marks >= 50:
#         print("Grade C")
#     else:
#         print("FAIL")
