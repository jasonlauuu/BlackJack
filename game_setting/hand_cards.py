#This module defines a class of player's Hand.
"""
Class
------
Hand
    attribute:
        cards: current hand cards
        _value: total value of current cards
        _aces = array of aces
        _aces_soft = number of soft aces
        splithand = boolean flag of split or not
        surrender = boolean flag of surrendered or not
        doubled = boolean flag of doubled or not
    method:
        value: calculate value
        aces/aces_soft/soft: calculate the situations with soft
        splitable: check if can be split
        blackjack: check if is black jack
        busted: over 21
        add cards: append card to cards
        split: pair situation, split to two hands.
"""
class Hand:
    _value = 0
    _aces = []
    _aces_soft = 0
    splithand = False
    surrender = False
    doubled = False

    def __init__(self,cards):
        self.cards = cards

    @property
    def value(self):
        self._value = 0
        for card in self.cards:
            self._value += card.value

        if self._value > 21 and self.aces_soft > 0:
            for ace in self.aces:
                if ace.value == 11:
                    self._value -= 10
                    ace.value = 1
                    if self._value <= 21:
                        break

        return self._value

    @property
    def aces(self):
        self._aces = []
        for card in self.cards:
            if card.name == "Ace":
                self._aces.append(card)
        return self._aces

    @property
    def aces_soft(self):
        self._aces_soft = 0
        for ace in self.aces:
            if ace.value == 11:
                self._aces_soft += 1
        return self._aces_soft

    def soft(self):
        return True if self.aces_soft > 0 else False


    def splitable(self):
        if self.length() == 2 and self.cards[0].name == self.cards[1].name and not self.splithand:
            return True
        else:
            return False

    def blackjack(self):
        if not self.splithand and self.value == 21:
            return True
        else:
            return False

    def busted(self):
        return True if self.value > 21 else False


    def add_card(self, card):
        self.cards.append(card)

    def split(self):
        self.splithand = True
        c = self.cards.pop()
        new_hand = Hand([c])
        new_hand.splithand = True
        return new_hand

    def length(self):

        return len(self.cards)