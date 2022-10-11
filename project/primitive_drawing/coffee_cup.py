#import arcade module
import arcade

#define screen properties (width, height, and title)
screen_width = 600
screen_height = 600
screen_title = "New Game"

#open window
arcade.open_window(screen_width, screen_height, screen_title)

#set background color
arcade.set_background_color( arcade.color.MEDIUM_SPRING_BUD)
#start render
arcade.start_render( )

#draw cup (trapiziod)
point_list = [(250, 99), (350, 99), (378, 400), (222,400)]
arcade.draw_polygon_filled(point_list, arcade.color.WHITE)
point_list = [(378, 405), (222, 405), (225, 411), (375,411)]
arcade.draw_polygon_filled(point_list, arcade.color.WHITE)

#draw a green circle [rgb -> (0, 112, 74)]


#finish render
arcade.finish_render( )
#run
arcade.run()
