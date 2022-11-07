import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT, 'my first window')

arcade.set_background_color(arcade.color.NAVAJO_WHITE)

arcade.start_render()

def draw_card(x_off, y_off,):
    arcade.draw_rectangle_filled(x_off, y_off, 100, 175, arcade.color.WHITE)
    
    arcade.draw_arc_filled(150, 144, 85, 86,
    arcade.color.BOTTLE_GREEN, 90, 230, 20, 100)

    
draw_card(150,200)
arcade.finish_render()

arcade.run()