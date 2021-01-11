#This module defines a subclass of Player.
#A Huaman_Player decides the strategy by entering command in text_based console.
"""
Class
------
Human_Player
    attributes:
        inherits from Player
    methods overriding:
        get_strategy: decides the strategy by entering command in text_based console.
        show_result:print hand and values
"""
from players.player import Player

class Human_Player(Player):
    @classmethod
    def get_strategy(cls,hand):
        if hand.splitable():
            flag = input(
                "What's your Strategy?\nEnter 'H' for hit, 'S' for stand, 'Sr' for surrender,'D for double, 'P' for split")
        else:
            flag = input("What's your Strategy?\nEnter 'H' for hit, 'S' for stand, 'Sr' for surrender,'D for double")
        return flag

    def show_result(self,hand):
        final_hand = [card.value for card in hand.cards]
        print("Your hand:", final_hand)
        print("Your total values:", hand.value)