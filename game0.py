import arcade
from Suit import Suit
from Card import Card
from GameSlot import GameSlot
from Deck import Deck

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1060

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT,'first attempt')
        self.all_sprites = arcade.SpriteList()
        self.playableDeck = Deck()
        self.playableDeck.shuffle()


    def on_draw(self):
        # sets the background of the board
        arcade.set_background_color(arcade.color.BOTTLE_GREEN)
        arcade.start_render()

        
        
        self.draw_deck(self.playableDeck)
        

    def draw_deck(self, playableDeck):
        x_pos = 100
        y_pos = 400
        for i in playableDeck.deck:
            self.all_sprites.append(arcade.Sprite(i.image, center_x = x_pos, center_y = y_pos))
            x_pos += 40

        arcade.SpriteList.draw(self.all_sprites)

    



def main():
    solitare = Game()
    arcade.run()



if __name__ == "__main__":
    main()