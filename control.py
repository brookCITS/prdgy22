import arcade
import random

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5

PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

class MyGame(arcade.Window):

    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.wall_list = None
        self.player_list = None

        self.physics_engine = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        self.player_lives = 3

        arcade.set_background_color((251, 206, 177))


    def setup(self):
         # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)


        self.player_sprite = arcade.Sprite("src/img/wizard.png", CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128

        self.player_list.append(self.player_sprite)


        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        for x in range(0, 1250, 32):
            wall = arcade.Sprite("src/img/wall.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        for x in range(int(SCREEN_WIDTH/2 + 100), int(SCREEN_WIDTH/2 + 200), 32):
            wall = arcade.Sprite("src/img/wall.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 1*SCREEN_HEIGHT/3
            self.wall_list.append(wall)
        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, self.wall_list, gravity_constant=GRAVITY
        )


    def on_draw(self):
        self.clear()

        # Draw our sprites
        self.player_list.draw()
        self.wall_list.draw()
        arcade.draw_text("Lives: "+str(self.player_lives),
                         77,
                         620,
                         arcade.color.BLACK,
                         12)

    def on_update(self, delta_time):
        """Movement and game logic"""
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        print(str(key)+" is pressed")

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED

        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
