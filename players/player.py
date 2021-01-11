#This module defines a basic player superclass, which has three subclasses: human_player, dealer, computer_player.
#Player defines basic functions that a blackjack game player needs as follows.
"""
Class
------
Player
    attribute:
        hand: a list of current player's hand, list length could be two only if hand is split.
    method:
        set_hand: initialize current player's hand.
        get_strategy: get current player's strategy.
        play&play_hand:  according current strategy, make next steps.
        hit:deal&add card.
        split:call Hand method split, make attribute hand length become two. Play split hands seperately.

"""
class Player():
    def __init__(self):
        self.hand = []

    def set_hand(self, my_hand):
        self.hand.append(my_hand)

    def play(self, deck):
        for i in range(len(self.hand)):
            self.play_hand(self.hand[i], deck)

    @classmethod
    def get_strategy(cls,hand):
        pass

    def play_hand(self, hand, deck):
        if hand.length() < 2:
            if hand.cards[0].name == "Ace":
                hand.cards[0].value = 11
            self.hit(hand, deck)

        while not hand.busted() and not hand.blackjack():
            flag = self.get_strategy(hand)
            if flag == 'D':
                if hand.length() == 2:
                    hand.doubled = True
                    self.hit(hand, deck)
                    break
                else:
                    flag = 'H'

            if flag == 'Sr':
                if hand.length() == 2:
                    hand.surrender = True
                    break
                else:
                    flag = 'H'

            if flag == 'H':
                self.hit(hand, deck)

            if flag == 'P':
                self.split(hand, deck)
                break
            if flag == 'S':
                break
        self.show_result(hand)

    def hit(self, hand, deck):
        card = deck.deal()
        hand.add_card(card)
        if self.__class__.__name__ == 'Human_Player':
            print("Your new card: ", card.name)

    def split(self, hand, deck):
        split_hand = hand.split()
        self.hand.append(split_hand)
        self.play(deck)

    def show_result(self,hand):
        pass