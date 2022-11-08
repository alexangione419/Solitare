import arcade
from Suit import Suit
from Card import Card
from GameSlot import GameSlot

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

class Game(arcade.Window):
    # def __init__(self):
    #     super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT,'first attempt')
    #     arcade.set_background_color(arcade.color.NAVAJO_WHITE)


    def on_draw(self):
        # arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, 'first attempt')
        arcade.set_background_color(arcade.color.NAVAJO_WHITE)
        arcade.start_render()
        arcade.draw_rectangle_filled(500, 500, 300, 475, arcade.color.WHITE)    
        arcade.draw_arc_filled(150, 144, 85, 86, arcade.color.BOTTLE_GREEN, 90, 230, 20, 100)
    



def main():
    solitare = Game(SCREEN_WIDTH, SCREEN_HEIGHT, 'Solitaire')
    arcade.run()



if __name__ == "__main__":
    main()