import arcade
from play_slot import playSlot
from win_card_slot import winSlot
from draw_slot import drawSlot
from Deck import Deck
# from new_card_button import newCard


SCREEN_WIDTH = 1898
SCREEN_HEIGHT = 1074

class Game(arcade.Window):
    def __init__(self):
        """Initializes the game object 
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT,'Solitaire')

        # creates the list of card sprites
        self.all_sprites = arcade.SpriteList()
        # creates the deck of cards, shuffles them, and arranges them for play
        self.playableDeck = Deck()

        # creates each of the 7 main slots the player will interact with
        self.slot1 = playSlot(135, 580, self.playableDeck.deck[0:1])
        self.slot2 = playSlot(405, 580, self.playableDeck.deck[1:3])
        self.slot3 = playSlot(675, 580, self.playableDeck.deck[3:6])
        self.slot4 = playSlot(945, 580, self.playableDeck.deck[6:10])
        self.slot5 = playSlot(1215, 580, self.playableDeck.deck[10:15])
        self.slot6 = playSlot(1485, 580, self.playableDeck.deck[15:21])
        self.slot7 = playSlot(1755, 580, self.playableDeck.deck[21:28])
        # a list of all of the slots, used for finding each one in particular 
        self.all_play_slots = [self.slot1, self.slot2, self.slot3, self.slot4, self.slot5, self.slot6, self.slot7]
        
        # creates the slot from which players can draw their cards
        self.draw_slot = drawSlot(240, 970, self.playableDeck.deck[28:])

        self.win_slot_1 = winSlot(1070, 890)
        self.win_slot_2 = winSlot(1320, 890)
        self.win_slot_3 = winSlot(1560, 890)
        self.win_slot_4 = winSlot(1800, 890)



        for i in range(len(self.playableDeck.deck)):
            self.all_sprites.append(self.playableDeck.deck[i].sprite)
        
        self.button = arcade.Sprite(':resources:images/cards/cardBack_green3.png', center_x = 87, center_y = 970)
        self.all_sprites.append(self.button)
        
        # the card you are holding 
            # the first item will be the card sprite
            # the second tuple will be the original x and y
            # the third will be the card object
            # the fourth item will be the cards current slot
        self.held_card = [0, (0, 0), 0, 0]
        self.background = arcade.load_texture("background.png")

    def on_draw(self):
        """the method responsible for drawing all of the sprites onto the board
        """
        # sets the background of the board
        
        arcade.start_render()
        arcade.draw_texture_rectangle(949, 537, 1898, 1074, self.background)

        self.all_sprites.draw()
        # self.manager.draw()


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):  
        """ is activated whenever the user presses on the game board with their mouse

        Args:
            x (float): the x position the user has clicked on
            y (float): the y position the user has clicked on
            button (int): Unused but essential for function
            modifiers (int): Unused but essential for function
        """
        on_sprites = arcade.get_sprites_at_point((x, y), self.all_sprites)

        # determines if the player has pressed the button and draws from the deck
        if len(on_sprites) > 0 and on_sprites[-1] == self.button:
            if not self.button.visible:
                self.button.visible = True
                self.draw_slot.reset_deck()

                self.all_sprites.remove(self.button)
                self.all_sprites.append(self.button)
            
            elif len(self.draw_slot.cards_within) == 0:
                self.button.visible = False
                
                new_card = self.draw_slot.draw_card()
                self.all_sprites.remove(new_card.sprite)
                self.all_sprites.append(new_card.sprite)
            
            else:
                new_card = self.draw_slot.draw_card()
                self.all_sprites.remove(new_card.sprite)
                self.all_sprites.append(new_card.sprite)
            
            
        # begins the process of moving the card selected by the player, chooses the frontmost card the player clicks on
        elif len(on_sprites) > 0:  
            self.all_sprites.remove(self.button)
            self.held_card[0] = on_sprites[-1]
            self.held_card[1] = (self.held_card[0].center_x, self.held_card[0].center_y)
            self.held_card[2] = self.playableDeck.get_card(self.held_card[0].center_x, self.held_card[0].center_y)
            self.held_card[3] = self.get_slot(self.all_play_slots, x, y, 0, 6)

            # brings the sprite to the back of the sprite list to place it on top of the others
            self.all_sprites.remove(self.held_card[0])
            self.all_sprites.append(self.button)
            self.all_sprites.append(self.held_card[0])

    
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        """determines the behavior when the mouse button is released

        Args:
            x (int): the x position where the mouse is released
            y (int): the y position where the mouse is released
            button (int): unused but required for function
            modifiers (int): unused but required for function
        """

        self.prev_slot = self.held_card[3]
        over_this_slot = self.get_slot(self.all_play_slots, x, y, 0, 6)
        
        if over_this_slot != 0 and over_this_slot.valid_placement(self.held_card[2]):
            over_this_slot.add_card(self.held_card[2])
            if self.prev_slot != 0:
                self.prev_slot.remove_front()
            else:
                self.held_card[0].center_x = self.held_card[1][0]
                self.held_card[0].center_y = self.held_card[1][1]
                self.held_card[2].centerx = self.held_card[1][0]
                self.held_card[2].centery = self.held_card[1][1]

        else:
            if self.held_card[0] != 0:
                self.held_card[0].center_x = self.held_card[1][0]
                self.held_card[0].center_y = self.held_card[1][1]
                self.held_card[2].centerx = self.held_card[1][0]
                self.held_card[2].centery = self.held_card[1][1]

        self.held_card = [0, (0, 0), 0, 0]
        return super().on_mouse_release(x, y, button, modifiers)
        

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """as the mouse moves, this function is called

        Args:
            x (float): the initial x position of the mouse click
            y (float): the initial y position of the mouse click
            dx (float): the change in the x position from its initial position
            dy (float): the change in the y position from its initial position
        """
        if self.held_card[0] != 0:
            self.held_card[0].center_x += dx
            self.held_card[0].center_y += dy
            self.held_card[2].centerx += dx
            self.held_card[2].centery += dy

    def get_slot(self, slots, x, y, left, right):
        """figues out what slot the user has pressed on

        Args:
            slots (list): the list of all of the possible play slots to be pressed on
            x (int): the x position of the slot to be identified
            y (int): the y position of the slot to be identified
            left (int): for the binary search algorithm, the leftmost index of the list to check
            right (int): for the binary search algorithm, the rightmost index of the list to check

        Returns:
            gameSlot: returns the gameslot at the given position
        """
        if y > 690:
            if x < 400:
                return self.draw_slot
            else:
                if x >= 940 and x < 1190:
                    return self.win_slot_1
                elif x > 1191 and x < 1450:
                    return self.win_slot_2
                elif x > 1451 and x < 1691:
                    return self.win_slot_3
                elif x > 1691:
                    return self.win_slot_4
                else:
                    return 0
        
        else:
            if left > right:
                return 0
            middle = (left + right) // 2
            if slots[middle].x_pos - 75 < x and slots[middle].x_pos + 75 > x:
                return slots[middle]
            elif slots[middle].x_pos + 75 < x:
                return self.get_slot(slots, x, y, middle + 1, right)
            else:
                return self.get_slot(slots, x, y, left, middle - 1)
           

def main():
    """the main method where the game is initially begun
    """
    solitare = Game()
    arcade.run()

if __name__ == "__main__":
    main()