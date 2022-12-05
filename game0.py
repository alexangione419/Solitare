import arcade
from Suit import Suit
from Card import Card
from play_card_slot import playSlot
from win_card_slot import winSlot
from Deck import Deck


SCREEN_WIDTH = 1898
SCREEN_HEIGHT = 1074

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT,'Solitaire')
        # creates the list of card sprites
        self.all_sprites = arcade.SpriteList()
        # creates the deck of cards, shuffles them, and arranges them for play
        self.playableDeck = Deck()

        self.slot1 = playSlot(135, 580)
        self.slot2 = playSlot(405, 580)
        self.slot3 = playSlot(675, 580)
        self.slot4 = playSlot(945, 580)
        self.slot5 = playSlot(1215, 580)
        self.slot6 = playSlot(1485, 580)
        self.slot7 = playSlot(1755, 580)

        # self.win_Slot_1 = 
        # self.win_Slot_2 = 
        # self.win_Slot_3 = 
        # self.win_Slot_4 = 



        self.background = arcade.load_texture("background.png")

        for i in range(len(self.playableDeck.deck)):
            self.all_sprites.append(self.playableDeck.deck[i].sprite)

        self.held_card = [0, (0, 0)]
  

    def on_draw(self):
        # sets the background of the board
        # arcade.set_background_color(arcade.color.BOTTLE_GREEN)
        
        arcade.start_render()
        arcade.draw_texture_rectangle(949, 537, 1898, 1074, self.background)

        self.all_sprites.draw()
    
   
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        ## selects the frontmost card the player clicks on
        if len(arcade.get_sprites_at_point((x, y), self.all_sprites)) > 0:
            self.held_card[0] = arcade.get_sprites_at_point((x, y), self.all_sprites)[::-1][0]
            self.held_card[1] = (x, y)

            self.all_sprites.remove(self.held_card[0])
            self.all_sprites.insert(len(self.all_sprites) - 1, self.held_card[0])

    
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.held_card[0] = 0
        
        if(self.slot1.within(x, y)):
            if self.slot1.add_card(self.held_card[0]):
                self.held_card = 0
            else:
                self.held_card[0].center_x = self.held_card[1][0]
                self.held_card[0].center_y = self.held_card[1][1]

        # if(self.slot2.within(x, y)):
        #     if self.slot2.add_card(self.held_card[0]):
        #         self.held_card = 0
        #     else:
        #         self.held_card[0].center_x = self.held_card[1][0]
        #         self.held_card[0].center_y = self.held_card[1][1]
        
        # if(self.slot3.within(x, y)):
        #     if self.slot3.add_card(self.held_card[0]):
        #         self.held_card = 0
        #     else:
        #         self.held_card[0].center_x = self.held_card[1][0]
        #         self.held_card[0].center_y = self.held_card[1][1]

        # if(self.slot4.within(x, y)):
        #     if self.slot4.add_card(self.held_card[0]):
        #         self.held_card = 0
        #     else:
        #         self.held_card[0].center_x = self.held_card[1][0]
        #         self.held_card[0].center_y = self.held_card[1][1]
        
        # if(self.slot5.within(x, y)):
        #     if self.slot5.add_card(self.held_card[0]):
        #         self.held_card = 0
        #     else:
        #         self.held_card[0].center_x = self.held_card[1][0]
        #         self.held_card[0].center_y = self.held_card[1][1]
        
        # if(self.slot6.within(x, y)):
        #     if self.slot6.add_card(self.held_card[0]):
        #         self.held_card = 0
        #     else:
        #         self.held_card[0].center_x = self.held_card[1][0]
        #         self.held_card[0].center_y = self.held_card[1][1]
        
        # if(self.slot7.within(x, y)):
        #     if self.slot7.add_card(self.held_card[0]):
        #         self.held_card = 0
        #     else:
        #         self.held_card[0].center_x = self.held_card[1][0]
        #         self.held_card[0].center_y = self.held_card[1][1]


        return super().on_mouse_release(x, y, button, modifiers)
        

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if self.held_card[0] != 0:
            self.held_card[0].center_x += dx
            self.held_card[0].center_y += dy
 
                            



def main():
    solitare = Game()
    arcade.run()



if __name__ == "__main__":
    main()