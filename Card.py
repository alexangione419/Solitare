from Suit import Suit

# represents a Card with a value and suit
class Card:
    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit
    
    def __str__(self) -> str:
        return f'{self.value} of {self.suit}'
