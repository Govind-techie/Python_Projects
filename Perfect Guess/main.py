# Perfect Guess :

import random # Here, we import a random module.

number = random.randint(1,20) # we stored the random number in number variable.
guess_count = 0 # Here, we intialized guess_count as 0.

# Game Introduction and Rules:

print("Welcome to Perfect Guess !!\n") # Here, (\n) gives us a new line while we run the program to make game more clean
print("RULES OF THE GAME :")
print("You have to guess a number between 1 to 20.")
print("But,there's a twist you only have 5 limited guess.")
print("If, you find the number within the guess limit or you lose.")

limit_guess = 20 # Here, we mention limit of the guess number that can be entered.
min_guess = 1 # Here, we mention minimum of the guess number that can be entered.

while True: # The while True in the code is an infinite loop. It means the loop will continue running indefinitely until it is explicitly broken with a break statement.
            # Note : The while True loop ensures that the game keeps prompting the user for guesses until they guess the correct number.
            guess = int(input("Enter your guess : "))
            guess_count += 1

            # RULE CONDITION BLOCK :

            if guess > limit_guess: # Here, we mention the limit number of guess should not be more than 20.
                  print("Enter the number within 100 number.")
            elif guess < min_guess:  # Here, we mention the minimum  number of guess should  be more than 0.
                  print("Enter the number more than 0 guess number.")
            elif guess_count >= 5: # Here, we mention the number of guess_attempt is more than 5 break the loop.
                  print(f"Oops!!, you are out of guesses. The correct number was {number}")
                  break # when this condition true break the loop and end the game.
            
            # HINT CONDITION BLOCK :

            elif guess > number: # Here, we metion the condition if the guess is high than the number.
                print("Your guess is high !!")
            elif guess < number: # Here, we metion the condition if the guess is low than the number.
                print("Your guess is low !!")
            elif guess == number: # Here, we mention the winning condition if the user guess the number.
                print(f"Hurray, you guessed it correct. The number was {number}")  
                print(f"Total attempts taken to guess : {guess_count}")
                break # Break the loop to exit the game automatically when the condition is true.

            





