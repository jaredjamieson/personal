# MyGraphic = Draws a Square

# Imports
from turtlegraphic import TurtleGraphic

# Class that represents mygraphic to be drawn on the screen.
class MyGraphic(TurtleGraphic):
    def __init__(self, turt, name, color, speed, xcoord, ycoord):
        TurtleGraphic.__init__(self, turt, name, color, speed, xcoord, ycoord)
        
    # Function to draw a square using a turtle. Parameters:
    def draw(self):
        TurtleGraphic.draw(self)
        
        # Draw square
        for i in range(4):
            self.get_turtle().forward(100)
            self.get_turtle().right(90)
        
        