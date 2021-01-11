#This module defines a subclass of Dealer.
"""
Class
------
Dealer
    attributes:
        inherits from Player
    methods overriding:
        get_strategy: dealer's strategy.
        show_result:print hand and values
"""
from players.player import Player
class Dealer(Player):

    @classmethod
    def get_strategy(cls,hand):
        if hand.value < 17:
            return 'H'
        else:
            return 'S'

    def show_result(self,hand):
        final_hand = [card.value for card in hand.cards]
        print("Dealer's hand:", final_hand)
        print("Dealer's total values:", hand.value)