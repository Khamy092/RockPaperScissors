# AppName: Rock, Paper & Scissors Game
# Developed by Taqi Khaliqdad @ www.taqi.au
# Date: 12/01/2023




# code starts here
# main modules imported

import random


# functions start here

def weclomeUser():

    userName = input("Hey, What's your name?: ")
    return "Hey " + userName + "!"


ifPlay = True

def askUser():

    global ifPlay
    player = input("Would you like to play? [Y/N]: ")
    if player == "y" or player == "yes" or player == "YES" or player == "Y":
        ifPlay = True
    else:
        ifPlay = False

def showOptions():

    if ifPlay == True:

        print("""
        
    1 ---> Rock
    2 ---> Paper
    3 ---> Scissors
        
            """)


def userChoice():

    userChoice = int(input("Please enter your choice [1, 2 or 3]: "))
    if ifPlay == True:
        if userChoice == 1 or userChoice == 2 or userChoice == 3:
            if userChoice == 1:
                print("You chose Rock")
            elif userChoice == 2:
                print("You chose Paper")
            elif userChoice == 3:
                print("You chose Scissors")
            return userChoice

computerChoice = ""

def computerChoice():

    global computerChoice

    if ifPlay == True:
        computerChoice = random.randint(1,3)
        if computerChoice == 1:
            print("Computer chose Rock")
        elif computerChoice == 2:
            print("Computer chose Paper")
        elif computerChoice == 3:
            print("Computer chose Scissors")
        return computerChoice

def findWinner():
    if computerChoice == 1 and userChoice == 1:
        print("Draw!")
    elif computerChoice == 1 and userChoice == 2:
        print("You win!")
    elif computerChoice == 1 and userChoice == 3:
        print("Computer wins!")
    elif computerChoice == 2 and userChoice == 1:
        print("Computer wins!")
    elif computerChoice == 2 and userChoice == 2:
        print("Draw!")
    elif computerChoice == 2 and userChoice == 3:
        print("You win!")
    elif computerChoice == 3 and userChoice == 1:
        print("You win!")
    elif computerChoice == 3 and userChoice == 2:
        print("Computer wins!")
    elif computerChoice == 3 and userChoice == 3:
        print("Draw!")

print(weclomeUser())
while ifPlay != False:
    showOptions()
    userChoice()
    computerChoice()
    findWinner()
    askUser()
    if ifPlay == False:
        break
    
input("Exit...? ")