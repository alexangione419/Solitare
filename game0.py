import arcade
from Suit import Suit
from Card import Card
from GameSlot import GameSlot

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT,'first attempt')
        self.all_sprites = arcade.SpriteList()


    def on_draw(self):
        # sets the background of the board
        arcade.set_background_color(arcade.color.BOTTLE_GREEN)
        arcade.start_render()

        spades = Suit("Spades", "black")
        ace_spades = Card("A", spades)

        self.all_sprites.append(ace_spades.sprite)

        arcade.SpriteList.draw(self.all_sprites)

    



def main():
    solitare = Game()
    arcade.run()



if __name__ == "__main__":
    main()