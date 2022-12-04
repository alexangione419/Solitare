import arcade
from Card import Card
from Suit import Suit

# represents a slot for cards to be held during the game
class GameSlot():
    def __init__(self, x_pos, y_pos) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.ref_vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        self.front_card = 0
        self.cards_within = []


