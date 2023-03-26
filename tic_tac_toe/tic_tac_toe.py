import os
import random

## GLOBAL VARIABLES

gameStatus = False # true = ongoing, false = stopped
numberSet = [1, 2, 3, 4, 5, 6, 7, 8, 9] # reference ints for game board
currentBoard = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # game board
inputVerification = False # global variable for verifying user input
playerMarker = ""
computerMarker = ""
playerInput = ""
computerInput = ""
winner = None # set to 0 if computer wins, set to 1 if player wins

## GLOBAL FUNCTIONS

def resetTerminal():
    os.system('cls' if os.name == "nt" else 'clear')

def getPlayerMove():
    playerInput = input("Please enter the number of the space you'd like to claim: ")

    while inputVerification == False:
        for i in numberSet:
            if playerInput != i:
                inputVerification = False
            else:
                inputVerification = True
        
        if inputVerification == False:
            playerInput = input("Invalid input, please try again: ")

def getComputerMove():
    computerInput = random.randint(1, 9)

    if currentBoard[computerInput] == playerMarker or currentBoard[computerInput] == computerMarker:
        getComputerMove()
    else:
        return

def updateBoard():
    currentBoard[playerInput] = playerMarker
    currentBoard[computerInput] = computerMarker

def drawBoard():
    resetTerminal()
    print("""-------------------
|     |     |     |
|  """ + currentBoard[0] + """  |  """ + currentBoard[1] + """  |  """ + currentBoard[2] + """  |
|     |     |     |
-------------------
|     |     |     |
|  """ + currentBoard[3] + """  |  """ + currentBoard[4] + """  |  """ + currentBoard[5] + """  |
|     |     |     |
-------------------
|     |     |     |
|  """ + currentBoard[6] + """  |  """ + currentBoard[7] + """  |  """ + currentBoard[8] + """  |
|     |     |     |
-------------------""")
    print("")

def gameOver():
    # check for player win conditions
    if currentBoard[0] == playerMarker and currentBoard[1] == playerMarker and currentBoard[2] == playerMarker:
        winner = 1
        return True
    if currentBoard[3] == playerMarker and currentBoard[4] == playerMarker and currentBoard[5] == playerMarker:
        winner = 1
        return True
    if currentBoard[6] == playerMarker and currentBoard[7] == playerMarker and currentBoard[8] == playerMarker:
        winner = 1
        return True
    if currentBoard[0] == playerMarker and currentBoard[3] == playerMarker and currentBoard[6] == playerMarker:
        winner = 1
        return True
    if currentBoard[1] == playerMarker and currentBoard[4] == playerMarker and currentBoard[7] == playerMarker:
        winner = 1
        return True
    if currentBoard[2] == playerMarker and currentBoard[5] == playerMarker and currentBoard[8] == playerMarker:
        winner = 1
        return True
    if currentBoard[2] == playerMarker and currentBoard[1] == playerMarker and currentBoard[0] == playerMarker:
        winner = 1
        return True
    if currentBoard[5] == playerMarker and currentBoard[4] == playerMarker and currentBoard[3] == playerMarker:
        winner = 1
        return True
    if currentBoard[8] == playerMarker and currentBoard[7] == playerMarker and currentBoard[6] == playerMarker:
        winner = 1
        return True
    if currentBoard[6] == playerMarker and currentBoard[3] == playerMarker and currentBoard[0] == playerMarker:
        winner = 1
        return True
    if currentBoard[7] == playerMarker and currentBoard[4] == playerMarker and currentBoard[1] == playerMarker:
        winner = 1
        return True
    if currentBoard[8] == playerMarker and currentBoard[5] == playerMarker and currentBoard[2] == playerMarker:
        winner = 1
        return True
    if currentBoard[0] == playerMarker and currentBoard[4] == playerMarker and currentBoard[8] == playerMarker:
        winner = 1
        return True
    if currentBoard[8] == playerMarker and currentBoard[4] == playerMarker and currentBoard[0] == playerMarker:
        winner = 1
        return True
    if currentBoard[6] == playerMarker and currentBoard[4] == playerMarker and currentBoard[2] == playerMarker:
        winner = 1
        return True
    if currentBoard[2] == playerMarker and currentBoard[4] == playerMarker and currentBoard[6] == playerMarker:
        winner = 1
        return True
    
    # check for computer win conditions
    if currentBoard[0] == computerMarker and currentBoard[1] == computerMarker and currentBoard[2] == computerMarker:
        winner = 0
        return True
    if currentBoard[3] == computerMarker and currentBoard[4] == computerMarker and currentBoard[5] == computerMarker:
        winner = 0
        return True
    if currentBoard[6] == computerMarker and currentBoard[7] == computerMarker and currentBoard[8] == computerMarker:
        winner = 0
        return True
    if currentBoard[0] == computerMarker and currentBoard[3] == computerMarker and currentBoard[6] == computerMarker:
        winner = 0
        return True
    if currentBoard[1] == computerMarker and currentBoard[4] == computerMarker and currentBoard[7] == computerMarker:
        winner = 0
        return True
    if currentBoard[2] == computerMarker and currentBoard[5] == computerMarker and currentBoard[8] == computerMarker:
        winner = 0
        return True
    if currentBoard[2] == computerMarker and currentBoard[1] == computerMarker and currentBoard[0] == computerMarker:
        winner = 0
        return True
    if currentBoard[5] == computerMarker and currentBoard[4] == computerMarker and currentBoard[3] == computerMarker:
        winner = 0
        return True
    if currentBoard[8] == computerMarker and currentBoard[7] == computerMarker and currentBoard[6] == computerMarker:
        winner = 0
        return True
    if currentBoard[6] == computerMarker and currentBoard[3] == computerMarker and currentBoard[0] == computerMarker:
        winner = 0
        return True
    if currentBoard[7] == computerMarker and currentBoard[4] == computerMarker and currentBoard[1] == computerMarker:
        winner = 0
        return True
    if currentBoard[8] == computerMarker and currentBoard[5] == computerMarker and currentBoard[2] == computerMarker:
        winner = 0
        return True
    if currentBoard[0] == computerMarker and currentBoard[4] == computerMarker and currentBoard[8] == computerMarker:
        winner = 0
        return True
    if currentBoard[8] == computerMarker and currentBoard[4] == computerMarker and currentBoard[0] == computerMarker:
        winner = 0
        return True
    if currentBoard[6] == computerMarker and currentBoard[4] == computerMarker and currentBoard[2] == computerMarker:
        winner = 0
        return True
    if currentBoard[2] == computerMarker and currentBoard[4] == computerMarker and currentBoard[6] == computerMarker:
        winner = 0
        return True

def endGame():
    if winner == 0:
        print("")
        print("Computer wins")
    else:
        print("")
        print("Player wins")

def playAgain():
    playAgain = input("Thank you for playing. Would you like to play again? y/n")

    if playAgain == "y":
        gameStatus = True
        return
    else:
        gameStatus = False


## BEGIN PROGRAM

gameStatus = True
resetTerminal()

print("Hello, welcome to Tic Tac Toe.")
playerMarker = input("Please enter either X or O for your maker: ")

# verify user input & assign the computer the opposite marker
while inputVerification == False:
    if playerMarker == "X" or playerMarker == "x":
        playerMarker = "X"
        computerMarker = "O"
        inputVerification = True
    elif playerMarker == "O" or playerMarker == "o":
        playerMarker = "O"
        computerMarker = "X"
        inputVerification = True
    else:
        inputVerification = False
        playerMarker = input("Incorrect input, please try again: ")

inputVerification = False # reset global variable for other checks

print("")
print("Starting game...")
print("")

drawBoard()

while gameStatus == True:
    getPlayerMove()
    getComputerMove()

    updateBoard()
    drawBoard()

    if gameOver() == True:
        gameStatus = False
        endGame()
        playAgain()
