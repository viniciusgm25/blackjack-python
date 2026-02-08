from deck import Deck
from player import Player

class BlackjackGame:
    def __init__(self):
        self.player = Player("Jogador")
        self.dealer = Player("Dealer")
        self.deck = Deck()

    def reset(self):
        self.deck = Deck()
        self.player.reset_hand()
        self.dealer.reset_hand()

    def start_game(self):
        self.reset()
        for _ in range(2):
            self.player.add_card(self.deck.draw_card())
            self.dealer.add_card(self.deck.draw_card())

    def player_turn(self):
        while True:
            print(f"Sua mão: {self.player.hand} (Total: {self.player.hand_value()})")
            choice = input("Comprar carta? (s/n): ").lower()

            if choice == 's':
                self.player.add_card(self.deck.draw_card())
                if self.player.hand_value() > 21:
                    print("Você estourou!")
                    return False
            else:
                return True

    def dealer_turn(self):
        while self.dealer.hand_value() < 17:
            self.dealer.add_card(self.deck.draw_card())

    def check_winner(self):
        player_score = self.player.hand_value()
        dealer_score = self.dealer.hand_value()

        print(f"Dealer: {self.dealer.hand} (Total: {dealer_score})")

        if dealer_score > 21 or player_score > dealer_score:
            print("Você venceu!")
        elif player_score < dealer_score:
            print("Dealer venceu!")
        else:
            print("Empate!")
