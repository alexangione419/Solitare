from Suit import Suit
import arcade

# represents a Card with a value and suit
class Card:
    def __init__(self, value, suit : Suit) -> None:
        self.value = value
        self.suit = suit
        self.centerx = 0
        self.centery = 0

        self.image = f":resources:images/cards/card{self.suit.name}{self.value}.png"

    
    def __str__(self) -> str:
        return f'{self.value} of {self.suit}'

