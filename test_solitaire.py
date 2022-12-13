import unittest
import arcade
from Deck import Deck
from play_slot import playSlot
from win_card_slot import winSlot
from draw_slot import drawSlot
from Card import Card, Suit

class Test_Deck_Methods(unittest.TestCase):

    def test_get_card(self):
        deck = Deck()
        self.assertEqual(deck.get_card(deck.deck[0].centerx, deck.deck[0].centery), deck.deck[0])
        self.assertEqual(deck.get_card(deck.deck[30].centerx, deck.deck[30].centery), deck.deck[30])
        self.assertEqual(deck.get_card(deck.deck[10].centerx, deck.deck[20].centery), None)
    
class Test_PlaySlot_Methods(unittest.TestCase):
    def test_add_card(self):
        card1 = Card("A", Suit("Spades", "black"), 50, 60)
        card2 = Card(9, Suit("Diamonds", "red"), 70, 40)
        card3 = Card(5, Suit("Clubs", "black"), 100, 70)
        card4 = Card("J", Suit("Hearts", "red"), 90, 20)
        card5 = Card(4, Suit("Hearts", "red"), 80, 20)


        play = playSlot(10, 15, [card1, card2, card3])
        self.assertEqual(play.cards_within, [card2, card1])
        self.assertEqual(play.front_card, card3)

        play.add_card(card4)

        self.assertEqual(play.cards_within, [card2, card1])
        self.assertEqual(play.front_card, card3)

        play.add_card(card5)
        self.assertEqual(play.cards_within, [card2, card1, card3])
        self.assertEqual(play.front_card, card5)
    
    def test_valid_placement(self):
        card1 = Card("A", Suit("Spades", "black"), 50, 60)
        card2 = Card(9, Suit("Diamonds", "red"), 70, 40)
        card3 = Card(5, Suit("Clubs", "black"), 100, 70)
        card4 = Card("J", Suit("Hearts", "red"), 90, 20)
        card5 = Card(4, Suit("Hearts", "red"), 80, 20)
        play = playSlot(10, 15, [card1, card2, card3])

        self.assertEqual(play.valid_placement(card4), False)
        self.assertEqual(play.valid_placement(card5), True)
    
    def test_remove_front(self):
        card1 = Card("A", Suit("Spades", "black"), 50, 60)
        card2 = Card(9, Suit("Diamonds", "red"), 70, 40)
        card3 = Card(5, Suit("Clubs", "black"), 100, 70)
        play = playSlot(10, 15, [card1, card2, card3])

        self.assertEqual(play.cards_within, [card2, card1])
        self.assertEqual(play.front_card, card3)

        play.remove_front()

        self.assertEqual(play.cards_within, [card1])
        self.assertEqual(play.front_card, card2)

class Test_WinSlot_Methods(unittest.TestCase):
    def test_add_card(self):
        spade = Suit("Spades", "black")
        card1 = Card("A", spade, 50, 60)
        card2 = Card(2, spade, 70, 40)
        card3 = Card(3, spade, 100, 70)
        card4 = Card("J", Suit("Hearts", "red"), 90, 20)
        card5 = Card(4, spade, 80, 20)

        win = winSlot(10, 15)
        win.add_card(card1)
        win.add_card(card2)
        win.add_card(card3)

        self.assertEqual(win.cards_within, [card1, card2])
        self.assertEqual(win.front_card, card3)

        win.add_card(card4)

        self.assertEqual(win.cards_within, [card1, card2])
        self.assertEqual(win.front_card, card3)

        win.add_card(card5)
        self.assertEqual(win.cards_within, [card1, card2, card3])
        self.assertEqual(win.front_card, card5)
    
    def test_valid_placement(self):
        spade = Suit("Spades", "black")
        card1 = Card("A", spade, 50, 60)
        card2 = Card(2, spade, 70, 40)
        card3 = Card(3, spade, 100, 70)
        card4 = Card("J", Suit("Hearts", "red"), 90, 20)
        card5 = Card(4, spade, 80, 20)
        win = winSlot(10, 15)

        self.assertEqual(win.valid_placement(card1), True)
        self.assertEqual(win.valid_placement(card2), False)

        win.add_card(card1)

        self.assertEqual(win.valid_placement(card2), True)
        self.assertEqual(win.valid_placement(card3), False)

    def test_remove_front(self):
        spade = Suit("Spades", "black")
        card1 = Card("A", spade, 50, 60)
        card2 = Card(2, spade, 70, 40)
        card3 = Card(3, spade, 100, 70)
        win = winSlot(10, 15)
        win.add_card(card1)
        win.add_card(card2)
        win.add_card(card3)

        self.assertEqual(win.cards_within, [card1, card2])
        self.assertEqual(win.front_card, card3)

        win.remove_front()

        self.assertEqual(win.cards_within, [card2])
        self.assertEqual(win.front_card, card1)

class Test_WinSlot_Methods(unittest.TestCase):
    def test_add_card(self):
        spade = Suit("Spades", "black")
        card1 = Card("A", spade, 50, 60)
        card2 = Card(2, spade, 70, 40)
        card3 = Card(3, spade, 100, 70)
        card4 = Card("J", Suit("Hearts", "red"), 90, 20)
        card5 = Card(4, spade, 80, 20)

        win = winSlot(10, 15)
        win.add_card(card1)
        win.add_card(card2)
        win.add_card(card3)

        self.assertEqual(win.cards_within, [card1, card2])
        self.assertEqual(win.front_card, card3)

        win.add_card(card4)

        self.assertEqual(win.cards_within, [card1, card2])
        self.assertEqual(win.front_card, card3)

        win.add_card(card5)
        self.assertEqual(win.cards_within, [card1, card2, card3])
        self.assertEqual(win.front_card, card5)
    
    def test_valid_placement(self):
        spade = Suit("Spades", "black")
        card1 = Card("A", spade, 50, 60)
        card2 = Card(2, spade, 70, 40)
        card3 = Card(3, spade, 100, 70)
        card4 = Card("J", Suit("Hearts", "red"), 90, 20)
        card5 = Card(4, spade, 80, 20)
        win = winSlot(10, 15)

        self.assertEqual(win.valid_placement(card1), True)
        self.assertEqual(win.valid_placement(card2), False)

        win.add_card(card1)

        self.assertEqual(win.valid_placement(card2), True)
        self.assertEqual(win.valid_placement(card3), False)

    def test_remove_front(self):
        spade = Suit("Spades", "black")
        card1 = Card("A", spade, 50, 60)
        card2 = Card(2, spade, 70, 40)
        card3 = Card(3, spade, 100, 70)
        win = winSlot(10, 15)
        win.add_card(card1)
        win.add_card(card2)
        win.add_card(card3)

        self.assertEqual(win.cards_within, [card1, card2])
        self.assertEqual(win.front_card, card3)

        win.remove_front()

        self.assertEqual(win.cards_within, [card2])
        self.assertEqual(win.front_card, card1)


class test_Draw_Slot(unittest.TestCase):
    def test_draw_card(self):
        card1 = Card("A", Suit("Spades", "black"), 50, 60)
        card2 = Card(9, Suit("Diamonds", "red"), 70, 40)
        card3 = Card(5, Suit("Clubs", "black"), 100, 70)
        card4 = Card("J", Suit("Hearts", "red"), 90, 20)
        draw = drawSlot(10, 20, [card1, card2, card3, card4])

        self.assertEqual(draw.front_card, card1)
        self.assertEqual(draw.draw_card(), card1)
        self.assertEqual(draw.front_card, card2)
        self.assertEqual(draw.draw_card(), card2)

    def test_shift_front(self):
        card1 = Card("A", Suit("Spades", "black"), 50, 60)
        card2 = Card(9, Suit("Diamonds", "red"), 70, 40)
        card3 = Card(5, Suit("Clubs", "black"), 100, 70)
        card4 = Card("J", Suit("Hearts", "red"), 90, 20)
        draw = drawSlot(10, 20, [card1, card2, card3, card4])

        self.assertEqual(draw.front_card, card1)
        draw.shift_front()
        self.assertEqual(draw.front_card, card2)
        draw.shift_front()
        self.assertEqual(draw.front_card, card3)

    def test_remove_front(self):
        card1 = Card("A", Suit("Spades", "black"), 50, 60)
        card2 = Card(9, Suit("Diamonds", "red"), 70, 40)
        card3 = Card(5, Suit("Clubs", "black"), 100, 70)
        card4 = Card("J", Suit("Hearts", "red"), 90, 20)
        draw = drawSlot(10, 20, [card1, card2, card3, card4])

        self.assertEqual(draw.already_drawn, [])
        draw.draw_card()
        self.assertEqual(draw.already_drawn, [card1])
        draw.remove_front()
        self.assertEqual(draw.already_drawn, [])

    def reset_deck(self):
        card1 = Card("A", Suit("Spades", "black"), 50, 60)
        card2 = Card(9, Suit("Diamonds", "red"), 70, 40)
        card3 = Card(5, Suit("Clubs", "black"), 100, 70)
        card4 = Card("J", Suit("Hearts", "red"), 90, 20)
        draw = drawSlot(10, 20, [card1, card2, card3, card4])

        draw.draw_card()
        draw.draw_card()
        draw.draw_card()
        draw.draw_card()

        self.assertEqual(draw.already_drawn, [card4, card3, card2, card1])
        self.assertEqual(draw.cards_within, [])
        draw.reset_deck()
        self.assertEqual(draw.already_drawn, [])
        self.assertEqual(draw.cards_within, [card4, card3, card2, card1])



 

