# Random Password Generator

import random # Here, we imported a random module.
import string # Here, we imported a string module.

password_length = 8 # Here, we mentioned that the password length should be of 8 characters

def Random_Password_Generator(): # Here, we created a function to generate a password
    password = "" # Here, we created an empty string named as password.
    for i in range(1,password_length): # Here, we created a loop that generates a random character
        Random_characters = random.choice(string.ascii_letters + string.digits + string.punctuation) # Here, it generates a random choice of characteres.
        password += Random_characters # Everytime, a random characters is generated it is stored in password 
 
    return password # Here, we return the password value

Random_Password_1 = Random_Password_Generator() # Here, we call the function.
print(f"Password 1 : {Random_Password_1}")

# Using List comprehensions : To make the code short

Random_Password_2 = "".join([random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(1,password_length)])
print(f"Password 2 : {Random_Password_2}")