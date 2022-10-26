import arcade
import random

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5

class MyScene:


    def easy(self):

    def difficult(self):

class MyGame(arcade.Window):

    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # These are 'lists' that keep track of our sprites. Each sprite should

        arcade.set_background_color((251, 206, 177))

        self.scene = []
        self.player_sprite = None


    def setup(self):
        #player sprites
        self.player_sprite = arcade.Sprite("src/img/wizard.png", CHARACTER_SCALING)
        self.player_sprite.center_x = SCREEN_WIDTH/3
        self.player_sprite.center_y = SCREEN_HEIGHT/3 - 50

        for index in range(1,4):
            scene = arcade.Scene()

            # Create the Sprite lists
            scene.add_sprite_list("Player")
            #player sprites
            self.player_sprite = arcade.Sprite("src/img/wizard.png", CHARACTER_SCALING)
            self.player_sprite.center_x = 2*SCREEN_WIDTH/index
            self.player_sprite.center_y = SCREEN_HEIGHT/3 - 50

            scene.add_sprite("Player", self.player_sprite)

            self.scene.append(scene)


        print(len(self.scene))


    def on_draw(self):
        self.clear()

        self.scene[].draw()


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
