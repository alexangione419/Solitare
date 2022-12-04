import arcade
from Card import Card
from GameSlot import GameSlot

class winSlot(GameSlot):
    def __init__(self, x_pos, y_pos) -> None:
        super().__init__(x_pos, y_pos)
        