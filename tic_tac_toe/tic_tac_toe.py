## GLOBAL VARIABLES

gameStatus = False # true = ongoing, false = stopped
numberSet = [1, 2, 3, 4, 5, 6, 7, 8, 9] # reference ints for game board
currentBoard = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # game board
inputVerification = False # global variable for verifying user input
playerMarker = ""
computerMarker = ""
playerInput = ""
computerInput = ""

## GLOBAL FUNCTIONS

def resetTerminal():
    return None

def getPlayerMove():
    return None

def getComputerMove():
    return None

def updateBoard():
    return None

def drawBoard():
    return None

def gameOver():
    return None

def endGame():
    return None

def playAgain():
    return None

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
