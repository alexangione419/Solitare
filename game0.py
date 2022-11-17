import arcade
from Suit import Suit
from Card import Card
from GameSlot import GameSlot
from Deck import Deck
import math

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1060

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT,'Solitaire')
        self.all_sprites = arcade.SpriteList()
        self.playableDeck = Deck(500, 500)
        self.playableDeck.shuffle()

        for i in range(len(self.playableDeck.deck)):
            self.all_sprites.append(self.playableDeck.deck[i].sprite)
        self.cardzzz = []
  

    def on_draw(self):
        # sets the background of the board
        arcade.set_background_color(arcade.color.BOTTLE_GREEN)
        
        arcade.start_render()
        dynamic_width_rect = math.floor(SCREEN_WIDTH/5)
        dynamic_height_rect = math.floor(SCREEN_HEIGHT/8)
        i = 0
        winslots = []
        for x in range (300+ dynamic_width_rect,3*dynamic_width_rect, 200):
            arcade.draw_rectangle_outline(SCREEN_WIDTH-x,SCREEN_HEIGHT-dynamic_height_rect,175,225,arcade.color.AIR_SUPERIORITY_BLUE,3)
            
        #     i +=1
        # i = 0
        # playslots = []
        for x in range (300+ dynamic_width_rect,5*dynamic_width_rect, 175):
            arcade.draw_rectangle_outline(SCREEN_WIDTH-x,SCREEN_HEIGHT-3*dynamic_height_rect,175,225,arcade.color.AIR_SUPERIORITY_BLUE,3)
        #     playslots[i] = GameSlot(SCREEN_WIDTH-x,SCREEN_HEIGHT-dynamic_height_rect)
        #     i+=1
        self.draw_deck()
    
   
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.cardzzz = arcade.get_sprites_at_point((x, y), self.all_sprites)
    
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if len(self.cardzzz):
            self.cardzzz.pop(0)
        return super().on_mouse_release(x, y, button, modifiers)
        

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if len(self.cardzzz) > 0: 
            self.cardzzz[0].center_x += dx
            self.cardzzz[0].center_y += dy

                    

    def draw_deck(self):
        for i in range(len(self.playableDeck.deck)):
            self.all_sprites.append(arcade.Sprite(self.playableDeck.deck[i].image,\
             center_x = self.playableDeck.deck[i].centerx, center_y = self.playableDeck.deck[i].centery))
        arcade.SpriteList.draw(self.all_sprites)


def main():
    solitare = Game()
    arcade.run()



if __name__ == "__main__":
    main()