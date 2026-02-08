from game import BlackjackGame

def main():
    game = BlackjackGame()
    game.start_game()

    if game.player_turn():
        game.dealer_turn()
        game.check_winner()

if __name__ == "__main__":
    main()
