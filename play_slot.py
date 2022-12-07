from Card import Card
from GameSlot import GameSlot

class playSlot(GameSlot):
    def __init__(self, x_pos, y_pos, loC : list) -> None:
        loC.reverse()
        super().__init__(x_pos, y_pos, loC[0], loC[1:])

    def valid_placement(self, card : Card):
        if (self.front_card == 0):
            return card.value == 'K'
        return ((self.ref_vals.index(card.value) == self.ref_vals.index(self.front_card.value) - 1) and (card.suit.color != self.front_card.suit.color)) 
            

    def add_card(self, card : Card) -> None:
        if self.front_card == 0 and card.value == 'K':
            self.front_card = card
            self.cards_within.append(card)

        elif (self.ref_vals.index(card.value) == self.ref_vals.index(self.front_card.value) - 1) and (card.suit.color != self.front_card.suit.color):
            self.front_card = card
            self.cards_within.append(card)

    def within(self, x, y) -> bool:
        return self.x_pos - 75 <= x and self.x_pos + 75 >= x and y < 680

    def remove_front(self):
        if len(self.cards_within) > 0:
            self.front_card = self.cards_within[0]
            self.cards_within = self.cards_within[1:]
        else:
            self.front_card = 0
            self.cards_within = []

