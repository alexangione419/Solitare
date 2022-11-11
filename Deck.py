from Card import Card
from Suit import Suit
import arcade
import random

class Deck:
    def __init__(self, x, y) -> None:
        spades = Suit("Spades", "black")
        clubs = Suit("Clubs", "black")
        diamonds = Suit("Diamonds", "red")
        hearts = Suit("Hearts", "red")
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        suits = [spades, clubs, diamonds, hearts]

        self.deck = []
        for s in suits:
            for v in values:
                self.deck.append(Card(v, s, x, y))


    def shuffle(self) -> None:
        shuffled = []
        old = []
        old += self.deck
        for i in range(len(self.deck)):
            card_to_remove = random.randint(0, len(self.deck) - 1 - i)
            shuffled.append(old[card_to_remove])
            old.pop(card_to_remove)

        self.deck = shuffled
