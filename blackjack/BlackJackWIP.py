## Made by Dominik Lipari
def DeckOfCards(): # function returns a list to represent a deck of cards
    deck = ["J", "J"]
    number, kings, queens, jacks = 0, 0, 0, 0
    while number < 10:
        i = 0
        while i < 4:
             deck.append(str(number))
             i += 1
        number += 1
    while kings < 4:
        deck.append("K")
        kings += 1
    while queens < 4:
        deck.append("Q")
        queens += 1
    while jacks < 4:
        deck.append("J")
        jacks += 1
    return deck
