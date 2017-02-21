import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600

class MyApplication(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle(50, 100, 5, arcade.color.BLUE)
        arcade.draw_text("Hello world", 10, SCREEN_HEIGHT // 2, arcade.color.RED, 20)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE and key_modifiers == arcade.key.MOD_SHIFT:
            print("You pressed shift-space")
        elif key == arcade.key.SPACE:
            print("You pressed the space bar")

    def on_moust_motion(self, x, y, x_delta, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)

arcade.run()
