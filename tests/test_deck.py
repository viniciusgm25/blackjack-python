from src.deck import Deck

def test_deck_has_cards():
    deck = Deck()
    assert len(deck.cards) == 52

def test_draw_card_removes_card():
    deck = Deck()
    card = deck.draw_card()
    assert card is not None
    assert len(deck.cards) == 51
