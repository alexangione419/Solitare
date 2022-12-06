import arcade
import arcade.gui


class newCard(arcade.gui.UITextureButton):
    @staticmethod
    def on_click_button(event):
        print('Button clicked!')