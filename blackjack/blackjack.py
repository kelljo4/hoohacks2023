## Made by Dominik Lipari

import random
import sys

def MakeDeck(): # function creates a list to represent a deck of cards
    global deck # make the deck list accessible to other functions
    deck = []
    number, kings, queens, jacks = 0, 0, 0, 0
    for number in range(13): # 13 values of cards Ace through king
        for i in range(4): # one of each suit 
             deck.append(number)

def DrawCard(): # draws a card from the deck
    picked = random.randint(0,len(deck)) # pick card based on index
    drawnCard = deck[picked] # save picked card as drawnCard
    deck.pop(picked) # remove that card from the deck list based on index
    return drawnCard 
    
def CheckForBlackjack(hand, pOrD): #checks to see if the hand given is bust or blackjack   pOrD is used to say who owns the hand 
    if sum(hand) == 21:
        print("Blackjack!!", pOrD, "wins!")
        endPrompt = input("press X + Enter to close the program")
        exit()
    elif sum(hand) > 21:
        print("Bust.", pOrD, "looses.")
        endPrompt = input("press X + Enter to close the program")
        exit()

pHand, dHand= [], []     

def CheckAgainstDealer(): # Checks to see if the player or dealer has more points to determine a winner 
    if sum(pHand) < sum(dHand):
        print("You had ", sum(pHand), ". The dealer had ", sum(dHand), ". You loose.", sep="")
        endPrompt = input("press X + Enter to close the program")
        exit()
    elif sum(pHand) > sum(dHand):
        print("You had ", sum(pHand), ". The dealer had ", sum(dHand), ". You win!", sep="")
        endPrompt = input("press X + Enter to close the program")
        exit()
MakeDeck()


for i in range(2): #creates the dealer's hand 
    dHand.append(DrawCard())
for i in range(2): # creates the player's hand 
    pHand.append(DrawCard())

print("Welcome to Blackjack! Aces are low, and the dealer is lighting quick. Good luck!")
print("Here is your hand", pHand, sep=":") # show player their hand
CheckForBlackjack(pHand, "Player") # makes sure you start with a valid hand 
CheckForBlackjack(dHand, "Dealer") # makes sure the dealer has a valid hand 
choice = input("Would you like to hit or stand?") # prompt for hit or stand 

while choice == "hit" or choice == "Hit": 
    pHand.append(DrawCard()) # add a card to the hand
    CheckForBlackjack(pHand, "Player") # see if they won or lost
    print("Your hand", pHand, sep=":") # show player their hand
    choice = input("Would you like to hit or stand?") # prompt for hit or stand 
else:
    CheckAgainstDealer() # see who won
