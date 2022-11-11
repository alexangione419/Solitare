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

        for i in range(len(self.playableDeck.deck)):
            self.playableDeck.deck[i].centerx = 500
            self.playableDeck.deck[i].centery = 500


    def on_draw(self):
        # sets the background of the board
        arcade.set_background_color(arcade.color.BOTTLE_GREEN)
        arcade.start_render()

        self.draw_deck(self.playableDeck)

    def on_mouse_press(self, x: float, y: float, button: int):
         cards = arcade.get_sprites_at_point((x, y), self.all_sprites)
    
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        return super().on_mouse_release(x, y, button, modifiers)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.playableDeck.deck[0].centerx += dx
        self.playableDeck.deck[0].centery += dy



    def draw_deck(self, playableDeck):
        for i in range(len(self.playableDeck.deck)):
            self.all_sprites.append(arcade.Sprite(self.playableDeck.deck[i].image,\
             center_x = self.playableDeck.deck[i].centerx, center_y = self.playableDeck.deck[i].centery))


        arcade.SpriteList.draw(self.all_sprites)

def main():
    solitare = Game()
    arcade.run()



if __name__ == "__main__":
    main()