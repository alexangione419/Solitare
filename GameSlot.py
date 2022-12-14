from Card import Card

# represents a slot for cards to be held during the game
class GameSlot():
    def __init__(self, x_pos, y_pos, fcard : Card, cards : list) -> None:
        """initializes a game slot for cards to be held in

        Args:
            x_pos (int): the x position of the center of the slot on the game board
            y_pos (int): the y position of the center of the slot on the game board
            fcard (Card): the card to be noted as the one in the front of the slot 
            cards (list): all of the cards behind the "front card"
        """
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.front_card = fcard
        self.cards_within = cards

        self.ref_vals = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

        


