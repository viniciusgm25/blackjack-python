from src.player import Player

def test_hand_value_without_ace():
    player = Player("Test")
    player.hand = [10, 9]
    assert player.hand_value() == 19

def test_hand_value_with_ace_under_21():
    player = Player("Test")
    player.hand = [11, 7]
    assert player.hand_value() == 18

def test_hand_value_with_ace_over_21():
    player = Player("Test")
    player.hand = [11, 10, 5]
    assert player.hand_value() == 16

def test_player_busted():
    player = Player("Test")
    player.hand = [10, 10, 5]
    assert player.is_busted() is True
