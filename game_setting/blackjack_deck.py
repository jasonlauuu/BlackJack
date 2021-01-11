#This module defines a basic class of card and deck.
#Current game version, one standard 52-card deck.
"""
Class
------
Card
------
Deck
    attribute:
        deck: a list of standard 52 cards.
    method:
        init_deck: append 52 cards
        shuffle
        deal: pop 1 card
"""
from random import shuffle
from data.enum import suits,values

class Card:
    def __init__(self,suit,name,value):
        self.suit = suit
        self.name = name
        self.value = value

class Deck:
    def __init__(self):
        self.deck = []

    def init_deck(self):
        for suit in suits:
            for name in values.keys():
                self.deck.append(Card(suit,name,values[name]))
        self.shuffle()

    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        return self.deck.pop()