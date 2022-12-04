from Card import Card
from Suit import Suit
import arcade
import random

class Deck:
    def __init__(self) -> None:
        spades = Suit("Spades", "black")
        clubs = Suit("Clubs", "black")
        diamonds = Suit("Diamonds", "red")
        hearts = Suit("Hearts", "red")
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        suits = [spades, clubs, diamonds, hearts]

        self.deck = []
        for s in suits:
            for v in values:
                self.deck.append(Card(v, s, 0, 0))
        
        #Places the cards where they should go
        current_slot_x = 135
        slots = 1
        c_card = 0
        while slots < 8:
            current_slot_y = 580
            cards_to_place = slots
            while cards_to_place > 0:
                self.deck[c_card].centerx = current_slot_x
                self.deck[c_card].centery = current_slot_y
                self.deck[c_card].sprite.center_x = current_slot_x
                self.deck[c_card].sprite.center_y = current_slot_y

                c_card += 1
                current_slot_y -= 50
                cards_to_place -= 1
            slots += 1
            cards_to_place = slots
            current_slot_x += 270
        
        for i in range(c_card, len(self.deck)):
            self.deck[i].centerx = 80
            self.deck[i].centery = 970
            self.deck[i].sprite.center_x = 80
            self.deck[i].sprite.center_y = 970


    def shuffle(self) -> None:
        shuffled = []
        old = []
        old += self.deck
        for i in range(len(self.deck)):
            card_to_remove = random.randint(0, len(self.deck) - 1 - i)
            shuffled.append(old[card_to_remove])
            old.pop(card_to_remove)

        self.deck = shuffled
