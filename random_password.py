# import modules

import random
import string


# Save the characters in the list
str1 = list(string.ascii_lowercase)
str2 = list(string.ascii_uppercase)
str3 = list(string.digits)
str4 = list(string.punctuation)


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


# shuffle all lists
random.shuffle(str1)
random.shuffle(str2)
random.shuffle(str3)
random.shuffle(str4)


# calculate 30% & 20% of number of characters
part1 = round(number * (30/100))
part2 = round(number * (20/100))