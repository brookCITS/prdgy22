import arcade
screen_width = 600
screen_height = 600
screen_title = "New Game"

def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, screen_width, screen_height/3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

def draw_snow_person(x, y):
    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)
    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 47, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 37, arcade.color.WHITE)
    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)

def main():
    arcade.open_window(screen_width, screen_height, screen_title)

    arcade.start_render( )

    #call drawing functioncs
    draw_grass()
    for index in range(1,5):
        draw_snow_person(index*150,88+index)


    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()
