from Card import Card, Suit
import random

class Deck:
    def __init__(self) -> None:
        """initializes a Deck object
                does so by creating a suit object for each possible suit, and creating a list of every possible value a card can have
                if then creates a card object for every combination of suit and value and places it into the deck
        """ 
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
        self.shuffle()

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
                current_slot_y -= 40
                cards_to_place -= 1
            slots += 1
            cards_to_place = slots
            current_slot_x += 270
        
        deckx = 87.000
        decky = 970.000
        for i in range(c_card, len(self.deck)):
            self.deck[i].centerx = self.deck[i].sprite.center_x = deckx + (.001 * i)
            self.deck[i].centery = self.deck[i].sprite.center_y = decky + (.001 * i)



    def shuffle(self) -> None:
        """shuffles the given deck by creating a copy and randomly choosing cards within to add to a "shuffled" list, which then becomes the main deck
        """
        shuffled = []
        old = []
        old = old + self.deck
        for i in range(len(self.deck)):
            card_to_remove = random.randint(0, len(self.deck) - 1 - i)
            shuffled.append(old[card_to_remove])
            old.pop(card_to_remove)

        self.deck = shuffled

    def get_card(self, x, y):
        """checks if there is a card at the specific given x and y coordinate, and if so returns said card object

        Args:
            x (int): x position to check
            y (int): y position to check

        Returns:
            _type_: _description_
        """
        for card in self.deck:
            if card.centerx == x and card.centery == y:
                return card

