import arcade
from Suit import Suit
from Card import Card
from GameSlot import GameSlot



SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720


# class Cardprop(arcade.sprite):
#     pass

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,'first attempt')
        arcade.set_background_color(arcade.color.NAVAJO_WHITE)
    def draw_card(x_off, y_off,):
        arcade.draw_rectangle_filled(x_off, y_off, 100, 175, arcade.color.WHITE)
        arcade.draw_rectangle_filled(x_off, y_off, 300, 475, arcade.color.WHITE)    
        arcade.draw_arc_filled(150, 144, 85, 86,
        arcade.color.BOTTLE_GREEN, 90, 230, 20, 100)



def main():
    window = Game()
    # window.setup()
    Game.draw_card(50,60)
    arcade.run()


if __name__ == "__main__":
    main()