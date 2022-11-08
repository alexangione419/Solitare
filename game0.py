import arcade
from Suit import Suit
from Card import Card
from GameSlot import GameSlot

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
CARD_HEIGHT = 100
CARD_WIDTH = 60

class Game(arcade.Window):
    #def __init__(self):
    #     super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT,'first attempt')
    #     arcade.set_background_color(arcade.color.NAVAJO_WHITE)


    def on_draw(self):

        # arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'first attempt')
        arcade.set_background_color(arcade.color.BOTTLE_GREEN)
        arcade.start_render()

        # spade = Suit("Spade", "black")
        # aceSpade = Card("Ace", spade)

        # cardSprite = arcade.sprite("resources/Diamond7.png", CARD_WIDTH, CARD_HEIGHT)





        arcade.draw_rectangle_filled(500, 500, CARD_WIDTH, CARD_HEIGHT, arcade.color.JAPANESE_INDIGO)    

        arcade.draw_arc_filled(150, 144, 85, 86, arcade.color.ALABAMA_CRIMSON, 90, 230, 20, 100)
    



def main():
    solitare = Game(SCREEN_WIDTH, SCREEN_HEIGHT, 'Solitaire')
    arcade.run()



if __name__ == "__main__":
    main()