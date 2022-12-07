from GameSlot import GameSlot
from Card import Card

class drawSlot(GameSlot):
    def __init__(self, x_pos, y_pos, loC : list) -> None:
        self.already_drawn = []
        super().__init__(x_pos, y_pos, loC[0], loC[1:])
    
    def within(self, x, y) -> bool:
        return self.x_pos - 75 <= x and self.x_pos + 75 >= x and y > 870


    def draw_card(self):
        self.front_card.centerx += 160
        self.front_card.sprite.center_x += 160
        
        self.already_drawn.append(self.front_card)
        self.remove_front()
        return self.already_drawn[-1]

