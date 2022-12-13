from Card import Card
from GameSlot import GameSlot

class playSlot(GameSlot):
    def __init__(self, x_pos, y_pos, loC : list) -> None:
        """creates a play slot to hold the main cards one can interact with, a child object of a game slot

        Args:
            x_pos (int): the x position of the center of the slot on the game board
            y_pos (int): the y position of the center of the slot on the game board
            loC (list): a list of all of the cards within the slot
        """
        loC.reverse()
        super().__init__(x_pos, y_pos, loC[0], loC[1:])
        self.set_behind_cards()

    def valid_placement(self, card : Card) -> bool:
        """determines if the card given can be added to this slot based on the front card by the rules of solitare

        Args:
            card (Card): the card to be placed onto the slot

        Returns:
            boolean: whether or not the card should be placed
        """
        if (self.front_card == 0):
            return card.value == 'K'
        return ((self.ref_vals.index(card.value) == self.ref_vals.index(self.front_card.value) - 1) and (card.suit.color != self.front_card.suit.color)) 
            

    def add_card(self, card : Card) -> None:
        """adds a card to this slot 

        Args:
            card (Card): the card to be added to the slot
        """
    
        if self.front_card == 0 and card.value == 'K':
            card.centerx = self.x_pos
            card.centery = self.y_pos
            card.sprite.center_x = self.x_pos
            card.sprite.center_y = self.y_pos

            prev_front = self.front_card
            self.front_card = card
            self.cards_within.append(prev_front)

        elif (self.ref_vals.index(card.value) == self.ref_vals.index(self.front_card.value) - 1) and (card.suit.color != self.front_card.suit.color):
            card.centerx = self.front_card.centerx + 0.001
            card.centery = self.front_card.centery - 40
            card.sprite.center_x = self.front_card.centerx + 0.001
            card.sprite.center_y = self.front_card.centery - 40
            
            prev_front = self.front_card
            self.front_card = card
            self.cards_within.append(prev_front)

    def remove_front(self):
        """method that removes the front card from a particular slot and adjusts the slot accordingly
        """
        if len(self.cards_within) > 0:
            self.front_card = self.cards_within[0]
            self.cards_within = self.cards_within[1:]

            self.front_card.sprite.set_texture(0)
        else:
            self.front_card = 0
            self.cards_within = []

    def set_behind_cards(self):
        """makes all of the cards behind the front card face down
        """
        for card in self.cards_within:
            card.sprite.set_texture(1)


