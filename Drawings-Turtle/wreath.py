from turtlegraphic import TurtleGraphic

# Class that represents a wreath to be drawn on the screen.
class Wreath(TurtleGraphic):
    def __init__(self, turt, name, color, speed, xcoord, ycoord):
        TurtleGraphic.__init__(self, turt, name, color, speed, xcoord, ycoord)

# Function to draw a wreath using a turtle. Parameters:
    def draw(self):
        TurtleGraphic.draw(self)

# Draw wreath as series of overlapping squares
        for count in range(36):
            self.get_turtle().forward(100)
            self.get_turtle().right(100)

