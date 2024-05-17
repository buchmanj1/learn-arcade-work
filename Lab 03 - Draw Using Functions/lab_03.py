import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def setupdrawing():
    arcade.open_window(800, 600, )

    # Set the background color
    arcade.set_background_color(arcade.color.BLUE_GRAY)

    # Get ready to draw
    arcade.start_render()

    # Draw the ground
def drawground():
    arcade.draw_rectangle_filled(0, 800, 200, 0, arcade.color.WHITE)
    
def drawcloud():
    # --- Draw Clouds ---

    arcade.draw_ellipse_filled(200, 350, 50, 50, arcade.color.SNOW)

    arcade.draw_ellipse_filled(500, 270, 200, 110, arcade.color.SNOW)

    arcade.draw_ellipse_filled(10, 250, 110, 70, arcade.color.SNOW)

    arcade.draw_ellipse_filled(670, 280, 90, 70, arcade.color.SNOW)

    arcade.draw_ellipse_filled(400, 300, 70, 70, arcade.color.SNOW)

    arcade.draw_ellipse_filled(300, 400, 150, 70, arcade.color.SNOW)

    arcade.draw_ellipse_filled(750, 500, 150, 150, arcade.color.SNOW)

    arcade.draw_ellipse_filled(500, 500, 50, 50, arcade.color.SNOW)

def snowmantop():
    # Top Circle
    arcade.draw_circle_filled(490, 230, 25, arcade.color.BLACK)
    arcade.draw_circle_filled(490, 230, 15, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(490, 230, 18, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(490, 225, 3, arcade.color.ORANGE)
    arcade.draw_circle_filled(500, 230, 3, arcade.color.BLACK_BEAN)
    arcade.draw_circle_filled(480, 230, 3, arcade.color.BLACK_BEAN)

def snowmanmiddle():
    # Middle Circle
    arcade.draw_circle_filled(490, 180, 30, arcade.color.BLACK)
    arcade.draw_circle_filled(490, 180, 25, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(490, 180, 18, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(490, 180, 5, arcade.color.BLACK_BEAN)

def snowmanbottom():
    # Bottom circle
    arcade.draw_circle_filled(490, 110, 50, arcade.color.BLACK)
    arcade.draw_circle_filled(490, 110, 45, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(490, 110, 35, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(490, 110, 10, arcade.color.BLACK_BEAN)



def main():
    setupdrawing()
    drawground()
    drawcloud()
    snowmantop()
    snowmanbottom()
    snowmanmiddle()

    # --- Finish drawing ---
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
