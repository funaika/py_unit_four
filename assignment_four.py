#Assignment Four
#Kalen Funai
#10/25/2023

import random

def getCard():
    '''
    this function gets the computers cards
    :return: computer total
    '''
    cardOne = random.randint(1,10)
    cardTwo = random.randint(1,10)
    computerTotal = cardOne + cardTwo

def userCards():
    '''
    function that gets user cards and figures out who wins
    :return: user total, who the winner is
    '''
    userCardOne = random.randint(1,10)
    userCardTwo = random.randint(1,10)
    userCardThree = random.randint(1, 10)
    userTotalTwo = userCardThree + userCardTwo + userCardOne
    print("Your cards are", userCardOne, userCardTwo)
    userTotalOne = userCardTwo + userCardOne
    print("Your total is",userTotalOne)
    anotherCard = float(input("Would you like to draw another card? 1 for y or 2 for n."))

    if anotherCard == 1:
        print("Your new card it", userCardThree)
        print("Your new total is ",userCardOne + userCardTwo +userCardThree)

    dealerCardOne = random.randint(1,10)
    dealerCardTwo = random.randint(1,10)
    dealerTotal = dealerCardTwo + dealerCardOne
    print("The dealers has a",dealerCardOne, "and a",dealerCardTwo)
    print("The dealers total is",dealerCardTwo + dealerCardOne)

    if userTotalOne > 21 or userTotalTwo > 21:
        print("You went over 21, you lose.")
    elif anotherCard == 1 and userTotalTwo > dealerTotal:
        print("User wins!")
    elif dealerTotal > userTotalTwo or dealerTotal > userTotalOne:
        print("Dealer wins.")
    elif dealerTotal == userTotalOne or dealerTotal == userTotalTwo:
        print("Tie, dealer wins.")


def main():
    '''
    main function
    :return: called other functions
    '''
    getCard()
    userCards()

main()