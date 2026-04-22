""" Dictionary in Python ----- Class-2 """
dicto = { }

while True:
    menu = """ 
    press 1 for Signup
    press 2 for login
    press 3 for change password
    press 4 for Exit
    """

    print(menu)
    choice = input("Enter Choice : ")

    if choice == "1":
        username = input("Enter user name : ")
        
        if username in dicto:
            print("username already exits")
        else:
            password = int(input("Enter Password : "))
            cpassword = int(input("Enter Password again : "))

            if password == cpassword:
                dicto[username] = password
                print("Login successfull...!!!")
            else:
                print("Password does not match")

    elif choice == "2":
        username = input("Enter user name : ")
        password = int(input("Enter Password : "))

        if username in dicto:
            if dicto[username] == password:
                print("login successfully...!!!")
            else:
                print("Invalid username or password...XXX")

    elif choice == "3":
        username = input("Enter user name : ")

        if username in dicto:
            password = int(input("Enter old password : "))

            if dicto[username] == password:
                cpassword = int(input("Enter new password : "))
                conform = int(input("Conform new password : "))

                if cpassword == conform:
                    dicto[username] = cpassword
                    print("Password change successfully...!!!")
                else: 
                    print("Password does not match...XXX")
            else:
                print("Old password is wrong...")
        else:
            print("username not found...XXX")

    elif choice == "4":
        print("Thank you..!!")
        break
    else:
        print("Invalid choice ..!! Try again...")
        break
#########################################################################################
""" 
Example :
WAP of manu driven login system through mobile no and OTP generation.(Use dictionary) """

# import random

# otp = random.randint(1001,9999)

# d = { }



# while True:
#     menu = """
#     press 1 for Signup
#     press 2 for login
#     press 3 for forgot-password
#     press 4 for Exit """

#     print(menu)
#     choice = int(input("Enter Choice : "))

#     if choice == 1:
#         name = input("Enter Name : ")
#         email = input("Enter Mail ID : ")
#         mno = int(input("Enter Mobile Number : "))
#         password = int(input("Enter Password : "))
#         cpassword = int(input("Enter conform password : "))

#         if password == cpassword:
#             d['email'] = email
#             d['mno'] = mno
#             d['password'] = password
#             print("Signup Successfully...!!")
#         else:
#             print("Password & Conform Password does not match...!!")

#     elif choice == 2:
#         email = input("Enter Mail ID : ")
#         password = int(input("Enter Password : "))

#         if d['email'] == email:    
#             if d['password'] == password:
#                 print("Login Successfully...!!")
#             else:
#                 print("Password does not match...!!")
#         else:
#             print("Email-ID does not match...!!!")

#     elif choice == 3:
#         mno = int(input("Enter Mobile Number : "))

#         if d['mno'] == mno:
#             print("Your OTP is : ",otp)

#             uotp = int(input("Enter OTP : "))

#             if otp == uotp:
#                 password = int(input("Enter Password : "))
#                 d['password'] = password
#                 print("Password updated..!! Successfully")
#             else:
#                 print("Invalid OTP entered..!!")
#         else:
#             print("Mobile number does not exist!!")

#     elif choice == 4:
#         print("Thank you..!!")
#         break
    
#     else:
#         print("Invalid choice..!!!")
#         break

















        

