class Suit:
    def __init__(self, name, color) -> None:
        """Represents a suit that a card can have

        Args:
            name (string): the name of the Suit, either spades, diamonds, clubs, or hearts
            color (string): the color that the suit appears with, either red or black
        """
        self.name = name
        self.color = color
