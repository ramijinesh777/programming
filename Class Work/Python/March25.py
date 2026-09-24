# Control Statement :
# break - Immidetly Stop
# continue - skip condition
# pass - use for future coding

# Example : WAP to print 1 to 10 & break at number 5.
# for i in range (1, 11):
#     if i == 5:
#         break
#     print(i)

# Example : WAP to skip number 5.

# for i in range (1 , 11):
#     if i == 5:
#         continue
#     print(i)

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

#     if choice == 1:
#         n = int(input("Enter Number : "))
#         prime = 0
#         for i in range(1, n+1):
#             if(n%i == 0):
#                 prime += 1

#         if prime == 2:
#             print("Prime Number....!!!")
#         else:
#             print("Not Prime....!!!!")

#     elif choice == 2:
#         n = int(input("Enter Number : "))
#         fact = 1

#         for i in range(1, n+1):
#             fact *= i
#             i += 1

#         print("Factorial : ",fact)

#     elif choice == 3:
#         n = int(input("Enter Number : "))
#         rem = 0
#         rev = 0

#         while(n != 0):
#             rem = n % 10   
#             rev = rev*10+rem      
#             n = n//10             
#         print("Reverce Num : ",rev)

#     elif choice == 4:
#         print("Thanks...!!")
#         break

#     else:
#         print("Invalid Choice")
#         break

