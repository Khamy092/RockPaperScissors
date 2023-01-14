# Name: Rock, Paper & Scissors Game
# Developed by Taqi Khaliqdad @ www.taqi.au
# Date: 12/01/2023
# Version: 1.0.0
# Description: A simple Rock, Paper & Scissors game made in Python 3.9.1

# code starts here
# required modules imported

import random

# functions start here

def weclomePlayer(): # welcomes the user

    userName = input("Hey, What's your name?: ")
    return "Hey " + userName + "!"


ifPlay = True


def askPlayer(): # asks the user if they want to play

    global ifPlay
    player = input("Would you like to play? [Y/N]: ")
    if player == "y" or player == "yes" or player == "YES" or player == "Y":
        ifPlay = True
    elif player == "n" or player == "no" or player == "NO" or player == "N":
        ifPlay = False
        print()
        print("No problem, see you next time!")
    else:
        print("Please enter a valid input!")
        askPlayer()


def showOptions():  # shows the options to the user

    if ifPlay == True:

        print("""

    1 ---> Rock
    2 ---> Paper
    3 ---> Scissors

            """)

playerChoice = 0
def player():  # getting the player choice

    global playerChoice
    playerChoice = int(input("Please enter your choice [1, 2 or 3]: "))

    # user input validation ----> if incorrect
    while playerChoice != 1 and playerChoice != 2 and playerChoice != 3:
        print("Please enter a valid input!")
        playerChoice = int(input("Please enter your choice [1, 2 or 3]: "))

    # player input validation ----> if correct
    if playerChoice == 1 or playerChoice == 2 or playerChoice == 3:
        if ifPlay == True:
            if playerChoice == 1:
                    print("You chose Rock.")
            elif playerChoice == 2:
                print("You chose Paper.")
            elif playerChoice == 3:
                print("You chose Scissors.")
        return playerChoice

computerChoice = 0
def computer(): # getting the computer choice
        global computerChoice
        computerChoice = int(random.randint(1,3))
        if computerChoice == 1:
            print("Computer chose Rock.")
        elif computerChoice == 2:
            print("Computer chose Paper.")
        elif computerChoice == 3:
            print("Computer chose Scissors.")
        return computerChoice

# keeping count of the score --->
playerScore = 0
computerScore = 0
tieScore = 0

def winner(): # finding & displaying the winner

    global playerScore
    global computerScore
    global tieScore

    if playerChoice == computerChoice:
        print("It's a tie!")
        tieScore += 1
    elif playerChoice == 1 and computerChoice == 2:
        print("Computer wins!")
        computerScore += 1
    elif playerChoice == 1 and computerChoice == 3:
        print("You win!")
        playerScore += 1
    elif playerChoice == 2 and computerChoice == 1:
        print("You win!")
        playerScore += 1
    elif playerChoice == 2 and computerChoice == 3:
        print("Computer wins!")
        computerScore += 1
    elif playerChoice == 3 and computerChoice == 1:
        print("Computer wins!")
        computerScore += 1
    elif playerChoice == 3 and computerChoice == 2:
        print("You win!")
        playerScore += 1

# functions end here ---->

# main code starts here ---->

print(weclomePlayer())
askPlayer()
while ifPlay == True:
    showOptions()
    player()
    computer()
    winner()
    askPlayer()
    if ifPlay == False:
        print()
        print("Your score: " +      str(playerScore))
        print("Computer score: " +  str(computerScore))
        print("Tie score: " +       str(tieScore))
        print()
        break
print()
input("Press Enter to Exit...")

# main code ends here ---->