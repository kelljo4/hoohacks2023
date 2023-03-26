## Made by Dominik Lipari

import random
import sys

def MakeDeck(): # function creates a list to represent a deck of cards
    global deck # make the deck list accessible to other functions
    deckChar = ["\U0001F0A1", "\U0001F0B1", "\U0001F0C1", "\U0001F0D1", "\U0001F0A2", "\U0001F0B2", "\U0001F0C2", "\U0001F0D2", "\U0001F0A3", "\U0001F0B3", "\U0001F0C3", "\U0001F0D3", "\U0001F0A4", "\U0001F0B4", "\U0001F0C4", "\U0001F0D4", "\U0001F0A5", "\U0001F0B5", "\U0001F0C5", "\U0001F0D5", "\U0001F0A6", "\U0001F0B6", "\U0001F0C6", "\U0001F0D6", "\U0001F0A7", "\U0001F0B7", "\U0001F0C7", "\U0001F0D7", "\U0001F0A8", "\U0001F0B8", "\U0001F0C8", "\U0001F0D8", "\U0001F0A9", "\U0001F0B9", "\U0001F0C9", "\U0001F0D9", "\U0001F0AA", "\U0001F0BA", "\U0001F0CA", "\U0001F0DA", "\U0001F0AB", "\U0001F0BB", "\U0001F0CB", "\U0001F0DB", "\U0001F0AD", "\U0001F0BD", "\U0001F0CD", "\U0001F0DD", "\U0001F0AE", "\U0001F0BE", "\U0001F0CE", "\U0001F0DE"]
    # ^ list that contains the unicode characters for playing cards
    deckVal = []
    deck = []
    for i in range(52):
        deckVal.append((i // 4) + 1) # makes a list of integer represenatations of cards 
    for i in range(52):
        deck.append([deckVal[i], deckChar[i]]) # combines list of integer representations and unicode characters into nested array

def DrawCard(): # randomly draws a card from the deck
    picked = random.randint(0,len(deck) - 1) # pick card based on index
    drawnCard = deck[picked ] # save picked card array as drawnCard
    deck.pop(picked) # remove that card array from the deck array based on index
    return drawnCard # returns card array containing integer representation and unicode char.
    
def CheckForBlackjack(hand, pOrD, close): #checks to see if the hand given is bust or blackjack   pOrD is used to say who owns the hand 
    if sum(hand) == 21:
        print("Blackjack!!", pOrD, "wins!")
        while close != "Y":
            close = input("Close the program? Y/n")
        exit()
    elif sum(hand) > 21:
        print("Bust.", pOrD, "looses.")
        while close != "Y":
            close = input("Close the program? Y/n")
        exit()

pHand, dHand= [], []     

def CheckAgainstDealer(close): # Checks to see if the player or dealer has more points to determine a winner 
    if sum(ValHand(pHand)) < sum(ValHand(dHand)):
        print("You had ", sum(pHand), ". The dealer had ", sum(dHand), ". You loose.", sep="")
        while close != "Y":
            close = input("Close the program? Y/n")
        exit()
    elif sum(ValHand(pHand)) > sum(ValHand(dHand)):
        print("You had ", sum(ValHand(pHand)), ". The dealer had ", sum(ValHand(dHand)), ". You win!", sep="")
        while close != "Y":
            close = input("Close the program? Y/n")
        exit()
        

def ChoosePlay(choice, close): # function which allows player to hcoose to hit or stand to play the game
    while choice == "hit" or choice == "Hit" or choice == "stand" or choice =="Stand": 
        if choice == "hit" or choice == "Hit":
            pHand.append(DrawCard()) # add a card to the hand
            CheckForBlackjack(ValHand(pHand), "Player", close) # see if they won or lost
            print("Your hand", UniHand(pHand), sep=":") # show player their hand
            choice = input("Would you like to hit or stand?") # prompt for hit or stand 
            ChoosePlay(choice, close)
        elif choice == "stand" or "Stand":
            CheckAgainstDealer(close) # see who won
    else: 
        print("Please choose to hit or stand") # prompt user again if input is invalid
        ChoosePlay(choice, close)
        
def UniHand(hand):  # returns a unicode representation of the hand
    uniHand = []
    for card in hand:
        uniHand.append(card[1]) # pulls the unicode character from the card arrray
    return uniHand

def ValHand(hand): # returns an intiger representation of the hand for score calculations 
    valHand = []
    for card in hand:
        valHand.append(card[0]) # pulls the value from the card array
    return valHand

MakeDeck()

for i in range(2): #creates the dealer's hand 
    dHand.append(DrawCard())
for i in range(2): # creates the player's hand 
    pHand.append(DrawCard())


close = "no"
print("Welcome to Blackjack! Aces are low, and the dealer is lighting quick. Good luck!")
print("Here is your hand", UniHand(pHand), sep=":") # show player their hand
CheckForBlackjack(ValHand(pHand), "Player", close) # makes sure you start with a valid hand 
CheckForBlackjack(ValHand(dHand), "Dealer", close) # makes sure the dealer has a valid hand 
choice = input("Would you like to hit or stand?") # prompt for hit or stand 
ChoosePlay(choice, close)