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

COIN_SCALING = 0.5

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

        self.camera = None

        #self.collect_coin_sound = arcade.load_sound("src/sounds/Coin.wav")
        self.jump_sound = arcade.load_sound("src/sounds/jump1.wav")

        arcade.set_background_color((251, 206, 177))

    def setup(self):
         # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList()


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


        platform_count = 1
        for y in range(1, 3000, int(SCREEN_HEIGHT/4)):
            for x in range(int(SCREEN_WIDTH/2 + 100), int(SCREEN_WIDTH/2 + 200), 32):
                wall = arcade.Sprite("src/img/wall.png", TILE_SCALING)

                if platform_count%2 == 0:
                    wall.center_x = x - 100
                else:
                    wall.center_x = x + 100
                    #print(wall.center_x)
                wall.center_y = y
                self.wall_list.append(wall)
            platform_count += 1

        #Coin
        for x in range(128, 1250, 256):
            coin = arcade.Sprite("src/img/coinGold.png", COIN_SCALING)
            coin.center_x = x
            coin.center_y = 96
            self.coin_list.append(coin)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, self.wall_list, gravity_constant=GRAVITY
        )

        self.camera = arcade.Camera(self.width, self.height)


    def on_draw(self):
        self.clear()

        # Draw our sprites
        self.player_list.draw()
        self.wall_list.draw()
        self.coin_list.draw()
        self.camera.use()

        arcade.draw_text("Lives: "+str(self.player_lives),
                         77,
                         620,
                         arcade.color.BLACK,
                         12)

    def on_update(self, delta_time):
        """Movement and game logic"""
        self.physics_engine.update()
        self.center_camera_to_player()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        print(str(key)+" is pressed")

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)

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

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)

        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0

        player_centered = screen_center_x, screen_center_y
        self.camera.move_to(player_centered)

def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
