from Card import Card
from Suit import Suit

# represents a slot for cards to be held during the game
class GameSlot():
    def __init__(self,x_pos,y_pos) -> None:
        self.cards = []
        self.empty = len(self.cards) == 0
        self.x_pos = x_pos
        self.y_pos = y_pos

    #adds a card to the slot
    def add_card(self, card) -> None:
        

        #if card position is near this position then it is allowed in 
        self.cards.append(card)
    
    def display_cards(self) -> None:
        print(self.cards)



