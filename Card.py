from Suit import Suit
import arcade

# represents a Card with a value and suit
class Card:
    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit

        self.sprite = arcade.Sprite(f":resources:images/cards/{self.suit.name}{self.value}.png", \
            center_x = 200, center_y = 200)

    
    def __str__(self) -> str:
        return f'{self.value} of {self.suit}'


