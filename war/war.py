# coded by Dominik Lipari

import random

def MakeDeck(): # function creates a list to represent a deck of cards
    global deck # make the deck list accessible to other functions
    deck = [0,0] # two jacks added manually 
    number, kings, queens, jacks = 0, 0, 0, 0
    for number in range(13): # 13 values of cards Ace through king
        for i in range(4): # one of each suit 
             deck.append(number)

def MakeHands():
    for cardNum in range(len(deck)): # for every card
        if cardNum % 2 == 0: # half the cards go to the player
            picked = random.randint(0,len(deck) - 1)
            pHand.append(deck[picked])
            deck.remove(deck[picked])
        else: # half the cards go to the computer 
            picked = random.randint(0,len(deck) - 1 )
            comHand.append(deck[picked])
            deck.remove(deck[picked])

def DrawCards(cardsInLimbo): # draws a card from everyone's hands 
    pCard = int(pHand[-1]) # select the last card in the player's hand and store it
    comCard = int(comHand[-1]) # select the last card in the computer's hand and store it
    input("Press enter to continue...")
    print("You drew", pCard, "The computer drew", comCard)
    WhosHigher(comCard, pCard, cardsInLimbo)

def WhosHigher(comCard, pCard, cardsInLimbo): # function to determine who's card was higher

    if comCard > pCard: # if the computer is higher
        print("The computer wins this battle!") 
        pHand.pop() # give the player's card to the computer 
        comHand.insert(0, pCard)
        comHand.insert(0, comCard)
        comHand.pop(-1)
        if len(cardsInLimbo) > 0:
            for i in range(len(cardsInLimbo)):
                comHand.insert(0, cardsInLimbo[i])
    elif pCard > comCard: # if the player is higher
        print("You win this battle!")
        comHand.pop() # give the computer's card to the player
        pHand.insert(0, comCard)
        pHand.insert(0, pCard)
        pHand.pop(-1)
        if len(cardsInLimbo) > 0:
            for i in range(len(cardsInLimbo)):
                pHand.insert(0, cardsInLimbo[i])
    elif pCard == comCard: # if it is a draw
        print("Its a real battle now!") 
        cardsInLimbo.append(pCard) # hold cards in limbo until something is decided 
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
