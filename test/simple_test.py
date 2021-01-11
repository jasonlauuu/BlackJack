#
# A simple test written in Python to check the game.
#
from game_setting.game_init import BlackJack_Gambling
from data.enum import num_players
def main():
    new_game = BlackJack_Gambling()

    print('Initial Deal Check!')
    new_game.init_opponents()
    assert (len(new_game.opponents) == num_players - 1)
    new_game.initial_deal()
    assert (len(new_game.deck.deck) == 52-1-num_players*2)
    assert (len(new_game.dealer.hand[0].cards) == 1)
    assert (len(new_game.user.hand[0].cards) == 2)
    for player in new_game.opponents:
        assert (len(player.hand[0].cards) == 2)

    print('After One Round Check!')
    while 1:
        new_game.play_game()
        break
    num_deal = 0
    assert (len(new_game.dealer.hand[0].cards) >= 2)
    num_deal+= len(new_game.dealer.hand[0].cards)
    for hand in new_game.user.hand:
        assert (len(hand.cards) >= 2)
        num_deal+=len(hand.cards)
    for player in new_game.opponents:
        for hand in player.hand:
            assert(len(hand.cards) >=2)
            num_deal += len(hand.cards)
    assert(num_deal+len(new_game.deck.deck)==52)

    print('Test passed.')

if __name__ == '__main__':
    main()