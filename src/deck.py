import random

class Deck:
    def __init__(self):
        self.cards = (
            [2, 3, 4, 5, 6, 7, 8, 9] * 4 +
            [10] * 16 +
            [11] * 4
        )
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()
