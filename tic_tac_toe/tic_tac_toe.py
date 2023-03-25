## SET UP GAME

import os
print("Hello, welcome to Tic Tac Toe")
playerType = input("Will you be playing as X or O this game? ")
computerType = "" # will be set later based on player's input
correctInput = False # global variable for verifying input
squareSet = [1, 2, 3, 4, 5, 6, 7, 8, 9] # num set of possible squares
playerInput = "" # player input variable
computerInput = "" # computer input variable

## GLOBAL FUNCTIONS

# function for verifying user input
def verifySquare(input):
    for i in len(squareSet):
        try:
            if int(input) == squareSet(i):
                return True    
            else:
                return False  
        except:
                return False
        
# function for generating random computer choice of where to place its marker
def computerPlay(input):
    # TO DO

    return input

# function for making the square and resetting the terminal
def makeSqure(player, computer):
    # TO DO

    return None

## BEGIN PROGRAM

# verify input data
while correctInput == False:
    if playerType == "X" or playerType == "x":
        computerType = "O"
        playerType = "X"
        correctInput = True
    elif playerType == "O" or playerType == "o":
        computerType = "X"
        playerType = "O"
        correctInput = True
    else:
        correctInput = False
        playerType = input("That is not a valid input! Please try again: ")

# begin game
print("")
print("Beginning game now...")
print("")

print("""-------------------
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
-------------------
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
-------------------
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
-------------------""")

print("")
playerInput = input("Which squre would you like to place your marker? ")

# verify input
while verifySquare(playerInput) == True:
    print("You are placing your marker on square number " + playerInput)
    computerInput = computerPlay(playerInput)
    print("The computer is placing its marker on square number " + computerInput)

    makeSquare(playerInput, computerInput)

    

os.system('cls' if os.name == "nt" else 'clear')

