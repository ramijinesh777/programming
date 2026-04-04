# s = "Java is best programming"
# print(len(s))
# print(s[-22:-11:3])
# print(s[-20: :4])
# print(s[ : :-1])
# print(s[ :-4:2])
# print(s[-17:-2:1])

###########################################################################
# Palindrome :
###########################################################################
s = input("Enter Name : ").lower()   # "MOM"  "nayan"

if s==s[ : :-1]:
    print("Its Palindrome..!!")
else:
    print("Its not palindrome...!!!")

###########################################################################
# WAP to find mid of string
###########################################################################
s = input("Enter Name : ") # Jineshh


if len(s)%2==0:
    print(s)
else:
    mid = len(s)//2
    print(s[mid-1]+s[mid]+s[mid+1])