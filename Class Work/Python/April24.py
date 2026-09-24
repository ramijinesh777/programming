""" Library :- random """

# WAP to generate lucky number game.
# import random
# lucky = random.randint(1,50)

# print("***** Enter Number between 1 to 51 *****")
# while True:
#     choice = int(input("Enter Choice : "))

#     if choice > 50:
#         print("Invalid input..!!")
#         break

#     elif choice == lucky:
#         print("win")
#         break

#     elif choice > lucky:
#         print("Number is grater then origional number!!")

#     else:
#         print("Number is less then origional number!!")

###########################################################################################

# WAP to to generate game of Rock , paper & scissors

import random
print("***** Rock, Paper & Scissors Game *****")
choices = ["rock", "paper","scissors"]

user = input("Enter your choice in (Rock, Paper or Scissors) : ")
computer = random.choice(choices)
print("Computer choice : ",computer)

if user == computer:
    print("Its Tie..!!")

elif (user == "rock" and computer == "scissors"):
     print("You Win")

elif(user == "paper" and computer == "rock"):
     print("You Win")

elif(user == "scissors" and computer == "paper"):
    print("You win!")

elif user in choices:
    print("Computer wins!")

else:
    print("Invalid input!")

############################################################################

# import random
# print("***** Rock, Paper & Scissors Game *****")
# # choices = ["rock", "paper","scissors"]

# # user = input("Enter your choice in (Rock, Paper or Scissors) : ")
# # computer = random.choice(choices)
# # print("Computer choice : ",computer)

# while True:
#     menu = """
#     Press 1 for Rock
#     Press 2 for Paper
#     Press 3 for Scissors
#     """
#     print(menu)
#     choice = 
#     user_choice = input("Enter Your Choice : ")


