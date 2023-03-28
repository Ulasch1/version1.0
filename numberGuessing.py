#Number Guessing Game

import random

print(" - Welcome to NumberGuessing Game - ")

#Inputs taking
print(" - Please enter lower bound - ")
lower_bound = int(input("Lower Bound : "))

print(" - Please enter upper bound - ")
upper_bound = int(input("Upper Bound : "))

#Random number between user input's
rand_num = int(random.randint(lower_bound , upper_bound))
print("Random number has been generated")

u_input = int(input("Please enter your guess > "))

while u_input != rand_num:
    if u_input < rand_num:
        print("You guessed low please enter new guess")
        u_input = input("New guess > ")

    elif u_input > rand_num:
        print("You guessed high please enter new guess")
        u_input = input("New guess > ")

    else:
        break

print("You guessed right.")








