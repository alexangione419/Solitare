import arcade
from Suit import Suit
from Card import Card
from GameSlot import GameSlot
from Deck import Deck

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

        self.draw_deck()
        

    def draw_deck(self):
        unshuffled = Deck()
        x_pos = 50
        y_pos = 400
        for i in unshuffled.deck:
            self.all_sprites.append(arcade.Sprite(i.image, center_x = x_pos, center_y = y_pos))
            x_pos += 25

        arcade.SpriteList.draw(self.all_sprites)

    



def main():
    solitare = Game()
    arcade.run()



if __name__ == "__main__":
    main()