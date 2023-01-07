from GameSlot import GameSlot
from Card import Card

class drawSlot(GameSlot):
    def __init__(self, x_pos, y_pos, loC : list) -> None:
        """initializes a slot representing all of the cards not on the board that the player can draw from

        Args:
            x_pos (int): the x position of the center of the slot on the game board
            y_pos (int): the y position of the center of the slot on the game board
            loC (list): the list of cards to be placed within the slot
        """
        self.already_drawn = []
        super().__init__(x_pos, y_pos, loC[0], loC[1:])


    def draw_card(self) -> Card:
        """draws a card to from the deck to be avalable for use by the player

        Returns:
            Card: returns the next available card for the player to draw
        """
        self.front_card.centerx += 160
        self.front_card.sprite.center_x += 160
        
        self.already_drawn.append(self.front_card)
        self.shift_front()

        return self.already_drawn[-1]


    def shift_front(self):
        """shifts the items within the deck so that said card is no longer able to be drawn from the deck until the player resets the deck
        """
        if len(self.cards_within) > 0:
            self.front_card = self.cards_within[0]
            self.cards_within = self.cards_within[1:]
        else:
            self.front_card = 0
            self.cards_within = []


    def remove_front(self):
        """removes a card from the deck once the player uses it, ensure it will be fully taken from the drawable deck 
        """
        if len(self.already_drawn) > 0:
            self.already_drawn = self.already_drawn[:len(self.already_drawn)-1]

        else:
            self.already_drawn = []

    
    def reset_deck(self):
        """resets the deck with all of the cards the player has not drawn from so they may begin to draw from it
        """
        self.front_card = self.already_drawn[0]
        self.cards_within = self.already_drawn[1:]
        
        self.already_drawn = []

        self.front_card.centerx -= 160
        self.front_card.sprite.center_x -= 160

        for card in self.cards_within:
            card.centerx -= 160
            card.sprite.center_x -= 160


    def valid_placement(self, card : Card):
        """method to ensure a player cannot place a card back onto the draw slot

        Returns:
            boolean: always false
        """
        return False

    