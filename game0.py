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

    def on_mouse_press(self, x: float, y: float, button: int):
         cards = arcade.get_sprites_at_point((x, y), self.all_sprites)
    
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        return super().on_mouse_release(x, y, button, modifiers)
    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        pass
        # for card in self.held_cards:
        #     card.center_x += dx
        #     card.center_y += dy


    def draw_deck(self, playableDeck):
        x_pos = 50
        y_pos = 400
        for i in playableDeck.deck:
            self.all_sprites.append(arcade.Sprite(i.image, center_x = x_pos, center_y = y_pos))
            x_pos += 25

        arcade.SpriteList.draw(self.all_sprites)

    



def main():
    solitare = Game()
    arcade.run()



if __name__ == "__main__":
    main()