# Rock_Paper_Scissor Game :

import random
options = ["rock" , "paper" , "scissor"] # Choices

# User inputs : 
name = input("Enter your name : ")
user_choice = input("Enter your choice (rock,paper,scissor) : ") # User choice

computer_choice = random.choice(options) # Random choice from computer

# User and computer scorecard :
user = 0
computer = 0

def rock_paper_scissor(user_choice,computer_choice,user,computer):


    if user_choice.lower() == "rock" and computer_choice.lower() == "paper":
        print(f"Computer choice : {computer_choice}")
        print("Computer Wins.")
        computer += 1
    elif user_choice == "rock" and computer_choice == "scissor":
        print(f"Computer choice : {computer_choice}")
        print(f"{name} Wins.")
        user += 1
    elif user_choice.lower() == "paper" and computer_choice.lower() == "scissor":
        print(f"Computer choice : {computer_choice}")
        print("Computer Wins.")
        computer += 1
    elif user_choice.lower() == "paper" and computer_choice.lower() == "rock":
        print(f"Computer choice : {computer_choice}")
        print(f"{name} Wins.")
        user += 1
    elif user_choice.lower() == "scissor" and computer_choice.lower() == "rock":
        print(f"Computer choice : {computer_choice}")
        print("Computer Wins.")
        computer += 1
    elif user_choice.lower() == "scissor" and computer_choice.lower() == "paper":
        print(f"Computer choice : {computer_choice}")
        print(f"{name} Wins.")
        user += 1
    elif user_choice.lower() == computer_choice.lower():
        print(f"Computer choice : {computer_choice}")
        print("Its a Tie.")
    else:
        print("Invalid Choice. Please choose between rock, paper and scissor")

    print(f"Current Score : {name} = {user} , Computer = {computer}")

    return user,computer

user,computer = rock_paper_scissor(user_choice,computer_choice,user,computer)


while True:

    user_choice = input("Enter your choice (rock,paper,scissor) or quit : ")

    if user_choice.lower() == "quit":
        print("GameOver")
        print(f"Final score : {name} = {user} and Computer = {computer}")
        break
    else:
        computer_choice = random.choice(options)

    if user_choice not in options:
        print("Invalid Choice. Please choose between rock, paper and scissor")
        continue

    user,computer = rock_paper_scissor(user_choice,computer_choice,user,computer) # This updates the score of user and computer until they quit the game
    

   