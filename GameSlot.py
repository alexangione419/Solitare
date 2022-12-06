import arcade
from Card import Card
from Suit import Suit

# represents a slot for cards to be held during the game
class GameSlot():
    def __init__(self, x_pos, y_pos, fcard : Card, cards : list) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.front_card = fcard
        self.cards_within = cards

        self.ref_vals = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']


    def remove_front(self):
        if len(self.cards_within) > 0:
            self.front_card = self.cards_within[0]
            self.cards_within = self.cards_within[1:]
        else:
            self.front_card = 0
            self.cards_within = []
        


