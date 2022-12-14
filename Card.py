import arcade

class Suit:
    def __init__(self, name, color) -> None:
        """Represents a suit that a card can have

        Args:
            name (string): the name of the Suit, either spades, diamonds, clubs, or hearts
            color (string): the color that the suit appears with, either red or black
        """
        self.name = name
        self.color = color

class Card:
    def __init__(self, value, suit : Suit, x, y) -> None:
        """initializes a card object

        Args:
            value (String): a string representation of the cards "value" i.e. 2, 'J', 10
            suit (Suit): An object representing one of four card Suits
            x (int): x position of the card on the game board
            y (int): y position of the card on the game board
        """
        self.value = value
        self.suit = suit
        self.centerx = x
        self.centery = y

        self.image = f":resources:images/cards/card{self.suit.name}{self.value}.png"

        self.sprite = arcade.Sprite(self.image, center_x = self.centerx, center_y = self.centery)
        self.back = arcade.load_texture(':resources:images/cards/cardBack_green3.png')
        self.sprite.append_texture(self.back)


