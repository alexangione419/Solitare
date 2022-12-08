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
            self.front_card = card
            self.cards_within.append(card)

        elif (self.ref_vals.index(card.value) == self.ref_vals.index(self.front_card.value) - 1) and (card.suit.color != self.front_card.suit.color):
            self.front_card = card
            self.cards_within.append(card)

    def within(self, x, y) -> bool:
        """determines if the given x and y fall within the borders of the slot

        Args:
            x (int): the x position to check
            y (int): the y position to check

        Returns:
            bool: wether or not the given coordinates are within the slot's boundaries
        """
        return self.x_pos - 75 <= x and self.x_pos + 75 >= x and y < 680

