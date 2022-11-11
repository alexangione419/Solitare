from Suit import Suit
import arcade

# represents a Card with a value and suit
class Card:
    def __init__(self, value, suit : Suit, x, y) -> None:
        self.value = value
        self.suit = suit
        self.centerx = x
        self.centery = y

        self.image = f":resources:images/cards/card{self.suit.name}{self.value}.png"

        self.sprite = arcade.Sprite(self.image, center_x = self.centerx, center_y = self.centery)

    
    def __str__(self) -> str:
        return f'{self.value} of {self.suit}'

