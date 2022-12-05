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


        self.slot1 = playSlot(135, 580, self.playableDeck.deck[0:1])
        self.slot2 = playSlot(405, 580, self.playableDeck.deck[1:3])
        self.slot3 = playSlot(675, 580, self.playableDeck.deck[3:6])
        self.slot4 = playSlot(945, 580, self.playableDeck.deck[6:10])
        self.slot5 = playSlot(1215, 580, self.playableDeck.deck[10:15])
        self.slot6 = playSlot(1485, 580, self.playableDeck.deck[15:21])
        self.slot7 = playSlot(1755, 580, self.playableDeck.deck[21:28])
        print(self.playableDeck.deck[28])

        self.all_play_slots = [self.slot1, self.slot2, self.slot3, self.slot4, self.slot5, self.slot6, self.slot7]
        # self.win_Slot_1 = 
        # self.win_Slot_2 = 
        # self.win_Slot_3 = 
        # self.win_Slot_4 = 



        self.background = arcade.load_texture("background.png")

        for i in range(len(self.playableDeck.deck)):
            self.all_sprites.append(self.playableDeck.deck[i].sprite)

        # the card you are holding 
            # the first item will be the card sprite
            # the second tuple will be the original x and y
            # the third will be the card object
            # the fourth item will be the cards current slot
        self.held_card = [0, (0, 0), 0, 0]
  

    def on_draw(self):
        # sets the background of the board
        
        arcade.start_render()
        arcade.draw_texture_rectangle(949, 537, 1898, 1074, self.background)

        self.all_sprites.draw()
    
   
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        ## selects the frontmost card the player clicks on
        if len(arcade.get_sprites_at_point((x, y), self.all_sprites)) > 0:
            
            self.held_card[0] = arcade.get_sprites_at_point((x, y), self.all_sprites)[::-1][0]
            self.held_card[1] = (self.held_card[0].center_x, self.held_card[0].center_y)
            self.held_card[2] = self.playableDeck.get_card(self.held_card[0].center_x, self.held_card[0].center_y)
            self.held_card[3] = self.get_slot(self.all_play_slots, x, 0, 6)

            # brings the sprite to the back of the sprite list to place it on top of the others
            self.all_sprites.remove(self.held_card[0])
            self.all_sprites.insert(len(self.all_sprites) - 1, self.held_card[0])

    
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):        
        
        prev_slot = self.held_card[3]
        #if you are over a slot
        if(self.slot1.within(x, y)):
            # if the card you are holding can be placed in it, do it
            if self.slot1.add_card(self.held_card[2]):
                prev_slot.remove_front()
                self.held_card = [0, (0, 0), 0, prev_slot]
            else:
                self.held_card[0].center_x = self.held_card[1][0]
                self.held_card[0].center_y = self.held_card[1][1]
                self.held_card[2].centerx = self.held_card[1][0]
                self.held_card[2].centery = self.held_card[1][1]
                self.held_card = [0, (0, 0), 0, prev_slot]


        elif(self.slot2.within(x, y)):
            if self.slot2.add_card(self.held_card[2]):
                prev_slot.remove_front()
                self.held_card = [0, (0, 0), 0, prev_slot]
            else:
                self.held_card[0].center_x = self.held_card[1][0]
                self.held_card[0].center_y = self.held_card[1][1]
                self.held_card[2].centerx = self.held_card[1][0]
                self.held_card[2].centery = self.held_card[1][1]
                self.held_card = [0, (0, 0), 0, prev_slot]
        
        elif(self.slot3.within(x, y)):
            if self.slot3.add_card(self.held_card[2]):
                prev_slot.remove_front()
                self.held_card = [0, (0, 0), 0, prev_slot]
            else:
                self.held_card[0].center_x = self.held_card[1][0]
                self.held_card[0].center_y = self.held_card[1][1]
                self.held_card[2].centerx = self.held_card[1][0]
                self.held_card[2].centery = self.held_card[1][1]
                self.held_card = [0, (0, 0), 0, prev_slot]

        elif(self.slot4.within(x, y)):
            if self.slot4.add_card(self.held_card[2]):
                prev_slot.remove_front()
                self.held_card = [0, (0, 0), 0, prev_slot]
            else:
                self.held_card[0].center_x = self.held_card[1][0]
                self.held_card[0].center_y = self.held_card[1][1]
                self.held_card[2].centerx = self.held_card[1][0]
                self.held_card[2].centery = self.held_card[1][1]
                self.held_card = [0, (0, 0), 0, prev_slot]
        
        elif(self.slot5.within(x, y)):
            if self.slot5.add_card(self.held_card[2]):
                prev_slot.remove_front()
                self.held_card = [0, (0, 0), 0, prev_slot]
            else:
                self.held_card[0].center_x = self.held_card[1][0]
                self.held_card[0].center_y = self.held_card[1][1]
                self.held_card[2].centerx = self.held_card[1][0]
                self.held_card[2].centery = self.held_card[1][1]
                self.held_card = [0, (0, 0), 0, prev_slot]
        
        elif(self.slot6.within(x, y)):
            if self.slot6.add_card(self.held_card[2]):
                prev_slot.remove_front()
                self.held_card = [0, (0, 0), 0, prev_slot]
            else:
                self.held_card[0].center_x = self.held_card[1][0]
                self.held_card[0].center_y = self.held_card[1][1]
                self.held_card[2].centerx = self.held_card[1][0]
                self.held_card[2].centery = self.held_card[1][1]
                self.held_card = [0, (0, 0), 0, prev_slot]
        
        elif(self.slot7.within(x, y)):
            if self.slot7.add_card(self.held_card[2]):
                prev_slot.remove_front()
                self.held_card = [0, (0, 0), 0, prev_slot]
            else:
                self.held_card[0].center_x = self.held_card[1][0]
                self.held_card[0].center_y = self.held_card[1][1]
                self.held_card[2].centerx = self.held_card[1][0]
                self.held_card[2].centery = self.held_card[1][1]
                self.held_card = [0, (0, 0), 0, prev_slot]

        else:
            self.held_card[0].center_x = self.held_card[1][0]
            self.held_card[0].center_y = self.held_card[1][1]
            self.held_card[2].centerx = self.held_card[1][0]
            self.held_card[2].centery = self.held_card[1][1]
            self.held_card = [0, (0, 0), 0, prev_slot]

        return super().on_mouse_release(x, y, button, modifiers)
        

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if self.held_card[0] != 0:
            self.held_card[0].center_x += dx
            self.held_card[0].center_y += dy
            self.held_card[2].centerx += dx
            self.held_card[2].centery += dy

    def get_slot(self, slots, x, left, right):
        if left > right:
            return 0
        middle = (left + right) // 2
        if slots[middle].x_pos - 75 < x and slots[middle].x_pos + 75 > x:
            return slots[middle]
        elif slots[middle].x_pos + 75 < x:
            return self.get_slot(slots, x, middle + 1, right)
        else:
            return self.get_slot(slots, x, left, middle - 1)

 
                            



def main():
    solitare = Game()
    arcade.run()



if __name__ == "__main__":
    main()