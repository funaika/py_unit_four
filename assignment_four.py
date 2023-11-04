#Assignment Four
#Kalen Funai
#10/25/2023

import random

def getCard():
    '''
    this function generates a random card
    :return: card random number 1 through 10
    '''
    card = random.randint(1,10)
    return card

def userCards():
    '''
    function that gets user cards and figures out who wins
    :return: user total, who the winner is
    '''
    userCardOne = getCard()
    userCardTwo = getCard()
    userCardThree = getCard()
    print("Your cards are", userCardOne, userCardTwo)
    userTotalOne = userCardTwo + userCardOne
    print("Your total is",userTotalOne)
    anotherCard = float(input("Would you like to draw another card? 1 for y or 2 for n."))


    if anotherCard == 1:
        print("Your new card it", userCardThree)
        userTotalTwo = userCardOne + userCardTwo + userCardThree
        print("Your new total is ", userTotalTwo)

    else:
        print("Okay, your total is", userTotalOne)


    dealerCardOne = getCard()
    dealerCardTwo = getCard()
    dealerTotal = dealerCardTwo + dealerCardOne
    print("The dealers has a",dealerCardOne, "and a",dealerCardTwo)
    print("The dealers total is",dealerCardTwo + dealerCardOne)

    if userTotalOne > 21:
        print("You went over 21, you lose.")
    elif anotherCard == 1 and userTotalTwo > 21:
        print("You went over 21, you lose.")
    elif anotherCard == 1 and userTotalTwo > dealerTotal:
        print("User wins!")
    elif userTotalOne > dealerTotal:
        print("User wins!")
    elif anotherCard == 1 and dealerTotal > userTotalTwo:
        print("Dealer wins.")
    elif dealerTotal > userTotalOne:
        print("Dealer wins.")
    elif dealerTotal == userTotalOne:
        print("Tie, dealer wins.")
    elif anotherCard == 1 and dealerTotal == userTotalTwo:
        print("Tie, dealer wins.")



def main():
    '''
    main function
    :return: called other functions
    '''
    getCard()
    userCards()

main()