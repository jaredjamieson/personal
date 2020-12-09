# Imports
#import turtle
from turtlegraphic import TurtleGraphic

# Class that represents a wheel to be drawn on the screen.
class Wheel(TurtleGraphic):
    def __init__(self, turt, name, color, speed, xcoord, ycoord):
        TurtleGraphic.__init__(self, turt, name, color, speed, xcoord, ycoord)

    # Function to draw a wheel using a turtle. Parameters:
    def draw(self):
        TurtleGraphic.draw(self)
        
    # Draw wheel as series of overlapping triangles
        for i in range(12):
            for j in range(3):
                self.get_turtle().forward(40)
                self.get_turtle().left(120)
            self.get_turtle().left(30)
            
            