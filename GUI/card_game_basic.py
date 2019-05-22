""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
from random import *

NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2
cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")


def clear_deck():
    for card in cardLoc:
        cardLoc[cardLoc.index(card)] = 0


def assign_card(user):
    card_assigned = False
    while not card_assigned:
        rand_card = randint(0, 51)
        if cardLoc[rand_card] != 0:
            continue
        else:
            cardLoc[rand_card] = user
            card_assigned = True


def show_deck():
    print("Location of all cards")
    print("{:<10}{:<15}{}".format("#", "card", "location"))
    card_i = rank_i = suit_i = 0
    suit = "null"
    rank = "null"
    for card in cardLoc:
        rank = rankName[rank_i]
        suit = suitName[suit_i]
        card_name = "{} of {}".format(rank, suit)
        player = playerName[card]

        print("{:<5}{:<20}{}".format(str(card_i), card_name, player))

        card_i += 1
        if rank_i < 12:
            rank_i += 1
        else:
            suit_i += 1
            rank_i = 0


def show_hand(user):
    print("\nDisplaying {} hand".format(playerName[user]))
    card_i = rank_i = suit_i = 0
    suit = "null"
    rank = "null"
    for card in cardLoc:
        rank = rankName[rank_i]
        suit = suitName[suit_i]
        card_name = "{} of {}".format(rank, suit)
        player = playerName[card]

        if card == user:
            print(card_name)

        card_i += 1
        if rank_i < 12:
            rank_i += 1
        else:
            suit_i += 1
            rank_i = 0



def main():
    clear_deck()
    for i in range(5):
        assign_card(PLAYER)
        assign_card(COMP)

    show_deck()
    show_hand(PLAYER)
    show_hand(COMP)

main()
