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

        # cardSprite = arcade.Sprite(":resources:images/cards/cardSpadesA.png", \
        #     center_x = 200, center_y = 200)

        self.all_sprites.append(ace_spades.sprite)

        arcade.SpriteList.draw(self.all_sprites)

        # arcade.draw_rectangle_filled(500, 500, CARD_WIDTH, CARD_HEIGHT, arcade.color.JAPANESE_INDIGO)
        # arcade.draw_arc_filled(150, 144, 85, 86, arcade.color.ALABAMA_CRIMSON, 90, 230, 20, 100)
    



def main():
    solitare = Game()
    arcade.run()



if __name__ == "__main__":
    main()