#!/usr/bin/env python3
# Created By: Your Name
# Date: Month Day, Year
# Write what this program does.

import random


def main():

    random_variable = random.randint(1, 9)  # a number between 1 and 9

    # get the number from the user
    number = input("Enter a number between 0 and 9: ")

     # Verifies if number entered by user is an integer
    try:

        User_integer = int(number)

        # Check if the number is the correct guess
        if random_variable == User_integer:
            print("The number is the correct guess")

        # If not, then tell the user the correct number
        else:
            print(
            "Sorry, you are wrong. The correct guess is {}".format(random_variable)
        )
        
    except ValueError:
        print("{} is not an integer" . format(number))
            


if __name__ == "__main__":

        main()