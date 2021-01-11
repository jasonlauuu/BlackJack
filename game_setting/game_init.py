#Initialize a BlackJack Gambling Game.
"""
Class
------
BlackJack_Gambling
    attribute:
        deck: one standard 52 cards deck.
        dealer: Dealer()
        user: 1 Human_Player
        opponents: an array of 5 computer players.
    method:
        init_opponents: add computer players to opponents
        initial_deal: set each player's and dealer's hand
        play_game: initialize opponents, initial deal, call each player's play() method.
        win_or_lose/single_hand_win: calculate result
"""
from data.enum import num_players
from players.human_player import Human_Player
from players.dealer import Dealer
from players.computer_player import Computer_Player
from game_setting.blackjack_deck import Deck
from game_setting.hand_cards import Hand

class BlackJack_Gambling:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.user = Human_Player()
        self.opponents = []

    def init_opponents(self):
        for i in range(num_players-1):
            opponent_name = "COM_"+str(i)
            self.opponents.append(Computer_Player(opponent_name))

    def initial_deal(self):
        self.deck.init_deck()
        dealer_hand = Hand([self.deck.deal()])
        for opponent in self.opponents:
            opponent_hand = Hand([self.deck.deal(), self.deck.deal()])
            opponent.set_hand(opponent_hand, dealer_hand)
        user_hand = Hand([self.deck.deal(), self.deck.deal()])
        #user_hand = Hand([Card("Hearts","Four",4),Card("Clubs","Four",4)])
        self.user.set_hand(user_hand)
        print("Your cards:")
        for card in self.user.hand[0].cards:
            print(card.name)

        self.dealer.set_hand(dealer_hand)
        print("Dealer's card:")
        for card in self.dealer.hand[0].cards:
            print(card.name)

    def play_game(self):
        self.__init__()
        self.init_opponents()
        self.initial_deal()
        self.user.play(self.deck)
        for opponent in self.opponents:
            opponent.play(self.deck)
        self.dealer.play(self.deck)

        print('YOU:')
        self.win_or_lose(self.user)
        for i in range(len(self.opponents)):
            print('Computer_'+str(i)+':')
            self.win_or_lose(self.opponents[i])

    def win_or_lose(self,player):
        n = len(player.hand)
        res = 0
        if n == 2:
            print("Split!")
        else:
            self.single_hand_win(player.hand[0])
            return
        for i in range(n):
            print("Hand_"+str(i+1)+":",player.hand[i].value)
            hand = player.hand[i]
            res+=self.single_hand_win(hand)
        print("Split Final Result:")
        if res == 0:
            print("Push")
        elif res >0:
            print("Win")
        else:
            print("Lose")

    def single_hand_win(self,hand):
        times = 1
        if hand.doubled:
            times =2
        if hand.surrender:
            print("Surrender!Lose!")
            times = 0.5
            return -1*times
        if hand.busted():
            print("Busted!Lose!")
            return -1*times
        if self.dealer.hand[0].busted():
            print("Dealer Busted! WIN!")
            return 1*times
        if hand.value > self.dealer.hand[0].value:
            print("WIN!")
            return 1*times
        elif hand.value == self.dealer.hand[0].value:
            print("PUSH!")
            return 0
        else:
            print("LOSE!")
            return -1*times