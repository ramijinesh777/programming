""" Questation : 20 --> 
Mini project :
Problem Statement : Password Generator
Make a program to generate a strong password using the input given by the user. 
To generate a password, randomly take some words from the user input and then include 
numbers, special characters and capital letters to generate the password. Also, keep a 
check that password length is more than 8 characters.

Note: Include Exception handling wherever required. Also, make a ‘User’ class and store 
the details like user id, name and password of each user as a tuple."""

import random                                   # imports random number
users = [ ]                                     # list to store user data as tuple

def generate_password(text):                    # function for create password
    words = text.split()                        # splits sentence into words

    if len(words)==0:                           # program stop with error, if user can't enter sentence
        raise Exception("Input cant be empty!")
    
    base = words[0].lower()                     # take 1st word & converts into lowercase
    number = str(random.randint(10,99))         # take random 2 digit number
    special = random.choice("!@#$")             # take random special character
    capital = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") # take random capital letter

    password = base + number + special + capital # create password

    if len(password) <= 8:                       # if password length < 8 then add 123
        password = password + "123"
    return password                              # function send password back


while True:                                         # create infinite loop
    menu = """                                      
    Press 1 for creat user id & password
    Press 2 for view all user
    press 3 for Exit
    """
    print(menu)                                     # print menu
    choice = input("Enter choice : ")               # choice variable input

    if choice == "1":                               
        uid = int(input("Enter User ID : "))        # take user id
        name = input("Enter Name : ")               # take user name
        text = input("Enter Some Words : ")         # take user words

        pwd = generate_password(text)               # call password function for pwd

        users.append((uid, name, pwd))              # stores as tuple

        print("Generated Password : ",pwd)          # print generated password
        print("User Added Successfully!")

    elif choice == "2":
        if len(users) == 0:                         # if list is empty 
            print("No Users Found!")                # show message
        else:                                       
            print("\nStored Users : ")

            for u in users:
                print(u)                            # print all user

    elif choice == "3":
        print("Exit for the program")               # print message for exit
        print("Thank you..")
        break                                       # break loop

    else:
        print("Invalid Choice..!!")                 # print msg for invalid choice
    
