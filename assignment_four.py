#Assignment Four
#Kalen Funai
#10/25/2023

import random

def getCard():
    cardOne = random.randint(1,10)
    cardTwo = random.randint(1,10)
    computerTotal = cardOne + cardTwo

getCard()
def userCards():
    userCardOne = random.randint(1,10)
    userCardTwo = random.randint(1,10)
    print("Your cards are", userCardOne, userCardTwo)
    userCardThree = input("Would you like to draw another card?")

userCards()



