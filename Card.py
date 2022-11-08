from Suit import Suit

# represents a Card with a value and suit
class Card:
    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit


         

        # Image to use for the sprite when face up
        self.image_file_name = f":resources:images/cards/card{self.suit}{self.value}.png"

        # Call the parent
        # super().__init__(self.image_file_name, scale, hit_box_algorithm="None")
    
    def __str__(self) -> str:
        return f'{self.value} of {self.suit}'
