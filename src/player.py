class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def hand_value(self):
        value = sum(self.hand)
        aces = self.hand.count(11)

        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value

    def reset_hand(self):
        self.hand = []
