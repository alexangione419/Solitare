from GameSlot import GameSlot
from Card import Card

class drawSlot(GameSlot):
    def __init__(self, x_pos, y_pos, loC : list) -> None:
        loC.reverse()
        super().__init__(x_pos, y_pos, loC[0], loC[1:])
    
    def within(self, x, y) -> bool:
        return self.x_pos - 75 <= x and self.x_pos + 75 >= x and y > 870