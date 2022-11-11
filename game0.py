import arcade
import math
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
        self.playableDeck = Deck(400, 400)
        self.playableDeck.shuffle()

        self.cardzzz = []

        for i in range(len(self.playableDeck.deck)):


            self.all_sprites.append(self.playableDeck.deck[i].sprite)

            


    def on_draw(self):
        # sets the background of the board
        arcade.set_background_color(arcade.color.BOTTLE_GREEN)
        
        arcade.start_render()
        dynamic_width_rect = math.floor(SCREEN_WIDTH/5)
        dynamic_height_rect = math.floor(SCREEN_HEIGHT/8)
        i = 0
        winslots = []
        for x in range (dynamic_width_rect,3*dynamic_width_rect, 200):
            arcade.draw_rectangle_outline(SCREEN_WIDTH-x,SCREEN_HEIGHT-dynamic_height_rect,175,225,arcade.color.AIR_SUPERIORITY_BLUE,3)
            
            winslots[i] = GameSlot(SCREEN_WIDTH-x,SCREEN_HEIGHT-dynamic_height_rect)
            i +=1
        i = 0
        playslots = []
        for x in range (dynamic_width_rect,5*dynamic_width_rect, 200):
            arcade.draw_rectangle_outline(SCREEN_WIDTH-x,SCREEN_HEIGHT-3*dynamic_height_rect,175,225,arcade.color.AIR_SUPERIORITY_BLUE,3)
            playslots[i] = GameSlot(SCREEN_WIDTH-x,SCREEN_HEIGHT-dynamic_height_rect)
            i+=1
        self.draw_deck(self.playableDeck)
   
   
    def on_mouse_press(self, x: float, y: float, button: int):
        self.cardszzz = arcade.get_sprites_at_point((x, y), self.all_sprites)
    
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        return super().on_mouse_release(x, y, button, modifiers)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        for sprite in self.cardzzz:
            for i in range(len(self.playableDeck.deck)):
                if sprite == self.playableDeck.deck[i].sprite:
                    self.playableDeck.deck[i].centerx += dx
                    self.playableDeck.deck[i].centery += dy
            
        


    def draw_deck(self):
        self.all_sprites = arcade.SpriteList()
        for i in range(len(self.playableDeck.deck)):
            self.all_sprites.append(self.playableDeck.deck[i].sprite)
        arcade.SpriteList.draw(self.all_sprites)


def main():
    solitare = Game()
    arcade.run()



if __name__ == "__main__":
    main()