# coded by Dominik Lipari

def MakeDeck(): # function creates a list to represent a deck of cards
    global deck # make the deck list accessible to other functions
    deck = [0,0] # two jacks added manually 
    number, kings, queens, jacks = 0, 0, 0, 0
    for number in range(13): # 13 values of cards Ace through king
        for i in range(4): # one of each suit 
             deck.append(number)


    