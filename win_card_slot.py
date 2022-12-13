from Card import Card
from GameSlot import GameSlot

class winSlot(GameSlot):
    def __init__(self, x_pos, y_pos) -> None:
        super().__init__(x_pos, y_pos, 0, [])
    
    
    def add_card(self, card : Card) -> None:
        """adds a card to this slot 

        Args:
            card (Card): the card to be added to the slot
        """
        if self.front_card == 0 and card.value == 'A':
            card.centerx = self.x_pos
            card.centery = self.y_pos
            card.sprite.center_x = self.x_pos
            card.sprite.center_y = self.y_pos

            self.front_card = card

        elif (self.ref_vals.index(card.value) == self.ref_vals.index(self.front_card.value) + 1) and (card.suit == self.front_card.suit):
            card.centerx = self.front_card.centerx + 0.001
            card.centery = self.front_card.centery + 0.001
            card.sprite.center_x = self.front_card.centerx + 0.001
            card.sprite.center_y = self.front_card.centery + 0.001

            prev_front = self.front_card
            self.front_card = card
            self.cards_within.append(prev_front)
    

    def valid_placement(self, card : Card) -> bool:
        """determines if the card given can be added to this slot based on the front card by the rules of solitare

        Args:
            card (Card): the card to be placed onto the slot

        Returns:
            boolean: whether or not the card should be placed
        """
        if (self.front_card == 0):
            return card.value == 'A'
        return ((self.ref_vals.index(card.value) == self.ref_vals.index(self.front_card.value) + 1) and (card.suit == self.front_card.suit))


    def remove_front(self):
        """method that removes the front card from a particular slot and adjusts the slot accordingly
        """
        if len(self.cards_within) > 0:
            self.front_card = self.cards_within[0]
            self.cards_within = self.cards_within[1:]
        else:
            self.front_card = 0
            self.cards_within = []
    