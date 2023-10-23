#Simple Guessing Game
#Kalen Funai
#10/23/2023

import random

randint = random.randint(1,10)
guessNumber = int(input("Guess a number 1-10!"))

if randint == guessNumber:
    print("Congrats! You guess the number correctly!")

while randint != guessNumber:
    print("You did not choose the correct number, sorry!")
    guessNumber = int(input("Guess a number 1-10!"))

print("Congrats! You guess the number correctly!")