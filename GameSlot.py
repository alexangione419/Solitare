from Card import Card
from Suit import Suit

# represents a slot for cards to be held during the game
class GameSlot():
    def __init__(self) -> None:
        self.cards = []
        self.empty = len(self.cards) == 0

    #adds a card to the slot
    def add_card(self, card) -> None:
        self.cards.append(card)
    
    def display_cards(self) -> None:
        print(self.cards)



