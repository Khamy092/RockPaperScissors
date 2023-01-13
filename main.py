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


ifPlay = False

def askUser():

    global ifPlay
    player = input("Would you like to play? [Y/N]: ")
    if player == "y" or player == "yes" or player == "YES" or player == "Y":
        ifPlay = True
    else:
        ifPlay = False

userChoice = ""
def showOptions():

    if ifPlay == True:

        print("""
        
    1 ---> Rock
    2 ---> Paper
    3 ---> Scissors
        
            """)

    global userChoice
    userChoice = input("Please choose one of the options above: [1, 2 or 3]: ")
    return userChoice

computerChoice = ""

def computerChoice():

    global computerChoice

    if ifPlay == True:
        computerChoice = random.randint(1,3)
    
    return computerChoice

def findWinner():
    if computerChoice == 1 and userChoice == 1:
        print("Draw!")
# main body

print(weclomeUser())
askUser()

while ifPlay != False:
    showOptions()
    findWinner()
    
input("Exit...? ")