# import modules

import random
import string


# Save the characters in the list
srt1 = list(string.ascii_lowercase)
srt2 = list(string.ascii_uppercase)
srt3 = list(string.digits)
srt4 = list(string.punctuation)


# Entering the number of passwords from users
user_input = input("How many characters do you want in your password? ")


# Checking input that is a number and more than 8 characters
while True:

    try:
        number = int(user_input)
        if number < 8:
            print("It must be more than 8 characters")

            user_input = input("Please, Enter your number again: ")
        else:
            break
    
    except:
        print("Please enter only numbers. ")
        user_input = input("Please, Enter your number again: ")
