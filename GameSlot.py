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


spade = Suit("spade", "black")
ace_spades = Card("Ace", spade)

slot = GameSlot()
slot.add_card(ace_spades)
slot.display_cards()

