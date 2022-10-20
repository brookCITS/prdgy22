import arcade
screen_width = 600
screen_height = 600
screen_title = "New Game"


class Charachter:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def update(self, delta_time):
        #all logic for moving and the game logic
        pass

    def on_key_press(self, key, key_modifiers):
        #called when keyboard is pressed
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        #called when the mouse is moved
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        #called when the mouse is clicked
        pass

class SnowPerson:
    def __init__(self, position):
        self.position = position
        self.speed = 0

    def update(self):
        #all logic for moving and the game logic
        self.position[0] += self.speed

        if self.position[0] >= screen_width:
            self.speed *= -1
        elif self.position[0] <= 0:
            self.speed *= -1

    def draw(self):
        x = self.position[0]
        y = self.position[1]
        # Draw a point at x, y for reference
        arcade.draw_point(x, y, arcade.color.RED, 5)
        # Snow
        arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
        arcade.draw_circle_filled(x, 140 + y, 47, arcade.color.WHITE)
        arcade.draw_circle_filled(x, 200 + y, 37, arcade.color.WHITE)
        # Eyes
        arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        #create characters and set up the game
        self.snow = SnowPerson([88,88])
        self.snow.speed = 3

    def on_draw(self):
        #Render the screen
        self.clear()
        self.snow.draw()

    def on_update(self, delta_time):
        # Move the rectangle
        self.snow.update()
        print(self.snow.position)
        print(self.snow.speed)


def main():
    game = MyGame(screen_width, screen_height, screen_title)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
