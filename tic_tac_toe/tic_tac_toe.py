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
    global playerInput
    global inputVerification

    try:
        playerInput = int(input("Please enter the number of the space you'd like to claim: "))
    except:
        placeholder = 0

    while inputVerification == False:
        for i in numberSet:
            try:
                if int(playerInput) == int(i):
                    inputVerification = True
                    return
                else:
                    inputVerification = False
            except:
                playerInput = input("Invalid input, please try again: ")

        if inputVerification == False:
            playerInput = input("Invalid input, please try again: ")

def getComputerMove():
    global playerInput
    global computerInput
    global playerMarker
    global computerMarker

    computerInput = random.randint(1, 9)

    if currentBoard[int(computerInput) - 1] == playerMarker or currentBoard[int(computerInput) - 1] == computerMarker:
        if playerInput == computerInput:
            return
        else:
            getComputerMove()
    else:
        return

def updateBoard():
    global currentBoard
    global playerInput
    global computerInput
    global playerMarker
    global computerMarker

    currentBoard[int(playerInput) - 1] = playerMarker
    currentBoard[int(computerInput) - 1] = computerMarker

    drawChecker = 0
    for i in numberSet:
        if currentBoard[i - 1] == playerMarker or currentBoard[i - 1] == computerMarker:
            drawChecker += 1
            
            if drawChecker == 9:
                winner = 3
                return

def drawBoard():
    global currentBoard

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
    global currentBoard
    global playerMarker
    global computerMarker
    global winner

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
    
    if winner == 3:
        winner = 3
        return True

def endGame():
    global winner

    if winner == 0:
        print("")
        print("Computer wins")
        return
    if winner == 1:
        print("")
        print("Player wins")
        return
    if winner == 3:
        print("")
        print("The game ends in a draw")
        return

def playAgain():
    global gameStatus
    global numberSet
    global currentBoard
    global inputVerification
    global playerMarker
    global computerMarker
    global playerInput
    global computerInput

    playAgain = input("Thank you for playing. Would you like to play again? y/n ")

    if playAgain == "y":
        gameStatus = True
        numberSet = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        currentBoard = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        inputVerification = False
        playerMarker = playerMarker
        computerMarker = computerMarker
        playerInput = ""
        computerInput = ""

        drawBoard()

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