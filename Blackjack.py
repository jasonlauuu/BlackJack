from game_setting.game_init import BlackJack_Gambling

def main():
    new_game = BlackJack_Gambling()

    while 1:
        new_game.play_game()
        x = input("Would like to play again? y/n")
        if x!='y':
            break

if __name__ == "__main__":
    main()
