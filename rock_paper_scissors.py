
import random

userChoice = float(input("Choose 1 for rock, 2 for paper, 3 for scissors."))
computerChoice = random.randint(1,3)

print("...", computerChoice)
def rockPaperScissors(userChoice, computerChoice):
    if userChoice == 2 and computerChoice == 1:
        print("User wins!")
    elif userChoice == 3 and computerChoice == 2:
        print("User wins!")
    elif userChoice == 1 and computerChoice == 3:
        print("User wins!")
    elif userChoice == computerChoice:
        print("It's a tie!")
    else: print("Computer wins!")

rockPaperScissors(userChoice, computerChoice)