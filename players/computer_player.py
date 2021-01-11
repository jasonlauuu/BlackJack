#This module defines a subclass of Computer_Player.
"""
Class
------
Computer_Player
    attributes:
        call super constructor
        dealer_hand to make decisions
        its own name
    methods overriding:
        set_hand:call super constructor to set hand;set dealer_hand
        get_strategy: Strategy comes from wikipedia.
        show_result:print hand and values
"""
from players.player import Player
from utils.get_strategy import Computer_Strategy
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("BlackJack-202011/")+len("BlackJack-202011/")]
dataPath = os.path.abspath(rootPath + 'data/Wikipedia.csv')

importer = Computer_Strategy(dataPath)
HARD_STRATEGY, SOFT_STRATEGY, PAIR_STRATEGY = importer.import_computer_strategy()

class Computer_Player(Player):
    def __init__(self,name):
        super().__init__()
        self.dealer_hand = None
        self.name = name

    def set_hand(self, new_hand, dealer_hand):
        super().set_hand(new_hand)
        self.dealer_hand = dealer_hand

    def get_strategy(self,hand):
        if hand.soft():
            flag = SOFT_STRATEGY[hand.value][self.dealer_hand.cards[0].name]
        elif hand.splitable():
            flag = PAIR_STRATEGY[hand.value][self.dealer_hand.cards[0].name]
        else:
            flag = HARD_STRATEGY[hand.value][self.dealer_hand.cards[0].name]
        return flag

    def show_result(self,hand):
        final_hand = [card.value for card in hand.cards]
        print(self.name+"'s hand:", final_hand)
        print(self.name+"'s total values:", hand.value)