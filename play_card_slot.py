import arcade
from Card import Card
from GameSlot import GameSlot

class playSlot(GameSlot):
    def __init__(self, x_pos, y_pos, loC) -> None:
        super().__init__(x_pos, y_pos, loC[0], loC[1:])


    def add_card(self, card : Card) -> bool:
        if self.front_card == 0 and card.value == 'K':
            self.cards_within.append(card)
            return True
        
        print(card.value)
        print(self.front_card.value)
        if (self.ref_vals.index(card.value) < self.ref_vals.index(self.front_card.value)) and (card.suit.color != self.front_card.suit.color):
            self.front_card = card
            self.cards_within.append(card)
            return True

        return False

    def within(self, x, y) -> bool:
        return self.x_pos - 75 <= x and self.x_pos + 75 >= x and y < 680

