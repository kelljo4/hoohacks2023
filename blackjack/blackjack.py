## Made by Dominik Lipari

import random
import sys

def MakeDeck(): # function creates a list to represent a deck of cards
    global deck # make the deck list accessible to other functions
    deck = []
    number = 0
    for number in range(13): # 13 values of cards Ace through king
        for i in range(4): # one of each suit 
             deck.append(number)

def DrawCard(): # draws a card from the deck
    picked = random.randint(0,len(deck) - 1) # pick card based on index
    drawnCard = deck[picked ] # save picked card as drawnCard
    deck.pop(picked) # remove that card from the deck list based on index
    return drawnCard 
    
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
    if sum(pHand) < sum(dHand):
        print("You had ", sum(pHand), ". The dealer had ", sum(dHand), ". You loose.", sep="")
        while close != "Y":
            close = input("Close the program? Y/n")
        exit()
    elif sum(pHand) > sum(dHand):
        print("You had ", sum(pHand), ". The dealer had ", sum(dHand), ". You win!", sep="")
        while close != "Y":
            close = input("Close the program? Y/n")
        exit()
        

def ChoosePlay(choice, close):
    while choice == "hit" or choice == "Hit" or choice == "stand" or choice =="Stand": 
        if choice == "hit" or choice == "Hit":
            pHand.append(DrawCard()) # add a card to the hand
            CheckForBlackjack(pHand, "Player", close) # see if they won or lost
            print("Your hand", pHand, sep=":") # show player their hand
            choice = input("Would you like to hit or stand?") # prompt for hit or stand 
            ChoosePlay(choice, close)
        elif choice == "stand" or "Stand":
            CheckAgainstDealer(close) # see who won
    else: 
        print("Please choose to hit or stand")
        ChoosePlay(choice, close)

MakeDeck()

for i in range(2): #creates the dealer's hand 
    dHand.append(DrawCard())
for i in range(2): # creates the player's hand 
    pHand.append(DrawCard())

close = "no"
print("Welcome to Blackjack! Aces are low, and the dealer is lighting quick. Good luck!")
print("Here is your hand", pHand, sep=":") # show player their hand
CheckForBlackjack(pHand, "Player", close) # makes sure you start with a valid hand 
CheckForBlackjack(dHand, "Dealer", close) # makes sure the dealer has a valid hand 
choice = input("Would you like to hit or stand?") # prompt for hit or stand 
ChoosePlay(choice, close)