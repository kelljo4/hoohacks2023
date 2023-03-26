# coded by Dominik Lipari

import random

def MakeDeck(): # function creates a list to represent a deck of cards
    global deck # make the deck list accessible to other functions
    deck = [0,0] # two jacks added manually 
    number, kings, queens, jacks = 0, 0, 0, 0
    for number in range(13): # 13 values of cards Ace through king
        for i in range(4): # one of each suit 
             deck.append(number)

pHand, comHand = [], [] # create hands for player and computer
def MakeHands():
    for cardNum in range(len(deck)): # for every card
        if cardNum % 2 == 0: # half the cards go to the player
            picked = random.randint(0,len(deck))
            pHand.append(deck[picked])
            deck.remove(deck[picked])
        else: # half the cards go to the computer 
            picked = random.randint(0,len(deck))
            comHand.append(deck[picked])
            deck.remove(deck[picked])

def DrawCards():
    pCard = pHand[-1]
    comCard = comHand[-1]
    input("Press enter to continue...")
    


def WhosHigher():
    
    
# play cards from players hand and computers hand and compare values
# If computer wins, remove card from player's hand 
# if player wins, remove card from computer's hand
# if computer and player cards have same value, add 3 to the pot and draw again
# If someone runs out of cards, they loose     