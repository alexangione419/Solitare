import arcade
import arcade.gui


class newCard(arcade.gui.UITextureButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        print("hi")
        arcade.exit()