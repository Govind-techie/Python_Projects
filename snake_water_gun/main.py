'''
snake = 1
water = -1
gun = 0
'''

import random

computer = random.choice ([1,0,-1])
your_choice = input("Enter your choice : ")
your_dict = {"s" : 1 , "w" : -1 , "g" : 0} # Identify the given choices in form of input from user
reverse_dict = { 1 : "snake" , -1 : "water" , 0 : "gun"} # reverse_dict is use to assign the value to given, (Snake,Water,Gun)

you = your_dict[your_choice]

print(f"you choose {reverse_dict[you]}\ncomputer choose {reverse_dict[computer]}")

if (computer == you):
    print("Its a draw")

else:
    if(computer == 1 and you == 0):
        print("You Win")
    
    elif(computer == 1 and you == -1):
        print("You Lose")
    
    elif(computer == -1 and you == 1):
        print("You Win")
    
    elif(computer == -1 and you == 0):
        print("You Lose")
    
    elif(computer == 0 and you == 1):
        print("You Lose")
    
    elif(computer == 0 and you == -1):
        print("You Win")
    
    else:
        print("Something went wrong")

