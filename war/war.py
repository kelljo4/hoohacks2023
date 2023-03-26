# coded by Dominik Lipari

import random

def MakeDeck(): # function creates a list to represent a deck of cards
    global deckVal
    global deckChar # make the deck list accessible to other functions
    deckVal = [] #make a list to contain list of values of cards 
    for value in range(52): # values of every card 
        deckVal.append(value)
    deckChar = ["\U0001F0BF", "\U0001F0DF", "\U0001F0A1", "\U0001F0B1", "\U0001F0C1", "\U0001F0D1", "\U0001F0A2", "\U0001F0B2", "\U0001F0C2", "\U0001F0D2", "\U0001F0A3", "\U0001F0B3", "\U0001F0C3", "\U0001F0D3", "\U0001F0A4", "\U0001F0B4", "\U0001F0C4", "\U0001F0D4", "\U0001F0A5", "\U0001F0B5", "\U0001F0C5", "\U0001F0D5", "\U0001F0A6", "\U0001F0B6", "\U0001F0C6", "\U0001F0D6", "\U0001F0A7", "\U0001F0B7", "\U0001F0C7", "\U0001F0D7", "\U0001F0A8", "\U0001F0B8", "\U0001F0C8", "\U0001F0D8", "\U0001F0A9", "\U0001F0B9", "\U0001F0C9", "\U0001F0D9", "\U0001F0AA", "\U0001F0BA", "\U0001F0CA", "\U0001F0DA", "\U0001F0AB", "\U0001F0BB", "\U0001F0CB", "\U0001F0DB", "\U0001F0AD", "\U0001F0BD", "\U0001F0CD", "\U0001F0DD", "\U0001F0AE", "\U0001F0BE", "\U0001F0CE", "\U0001F0DE"]
# ^ list that contains the unicode characters for playing cards

def MakeHands():
    for cardNum in range(len(deckVal)): # for every card
        if cardNum % 2 == 0: # half the cards go to the player
            picked = random.randint(0,len(deckVal) - 1)
            pHand.append(deckVal[picked])
            deckVal.pop(picked)
        else: # half the cards go to the computer 
            picked = random.randint(0,len(deckVal) - 1 )
            comHand.append(deckVal[picked])
            deckVal.pop(picked)

def DrawCards(cardsInLimbo): # draws a card from everyone's hands 
    pCard = int(pHand[-1]) # select the last card in the player's hand and store it
    comCard = int(comHand[-1]) # select the last card in the computer's hand and store it
    input("Press enter to continue...")
    print("You drew", deckChar[pCard], "The computer drew", deckChar[comCard])
    WhosHigher(comCard, pCard, cardsInLimbo)

def WhosHigher(comCard, pCard, cardsInLimbo): # function to determine who's card was higher

    if (comCard//4) > (pCard//4): # if the computer is higher
        print("The computer wins this battle!") 
        pHand.pop() # give the player's card to the computer 
        comHand.insert(0, pCard)
        comHand.insert(0, comCard) # move just played card to the bottom of the hand
        comHand.pop(-1)
        if len(cardsInLimbo) > 0:
            for i in range(len(cardsInLimbo)):
                comHand.insert(0, cardsInLimbo[i])
    elif (pCard//4) > (comCard//4): # if the player is higher
        print("You win this battle!")
        comHand.pop() # give the computer's card to the player
        pHand.insert(0, comCard)
        pHand.insert(0, pCard) # move just played card to the bottom of the hand 
        pHand.pop(-1)
        if len(cardsInLimbo) > 0:
            for i in range(len(cardsInLimbo)):
                pHand.insert(0, cardsInLimbo[i])
    elif (pCard//4) == (comCard//4): # if it is a draw
        print("Its a real battle now!") 
        cardsInLimbo.append(pCard) # hold cards in limbo until someone wins them 
        cardsInLimbo.append(comCard)
        pHand.pop()
        comHand.pop()
        DrawCards(cardsInLimbo)
        


gameStatus = "ongoing" # start the game 
pHand, comHand = [], [] # create hands for player and computer
cardsInLimbo = []
close = "no"
MakeDeck()
MakeHands()
while gameStatus == "ongoing": # while loop to keep the game going until there is a winner
    DrawCards(cardsInLimbo)
    if len(pHand) <= 0:  # if the player runs out of cards, the computer wins
        gameStatus = "end"
        winner = "Computer"
    elif len(comHand) <= 0: # if the computer runs out of cards, the player wins 
        gameStatus = "end"
        winner = "Player"
    cardsInLimbo = []
print(winner, "wins the war!!")

while close != "Y":
    close = input("Close the program? Y/n")
