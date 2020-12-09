from turtlegraphic import TurtleGraphic

# Class that represents a flower to be drawn on the screen.
class Flower(TurtleGraphic):
    def __init__(self, turt, name, color, speed, xcoord, ycoord):
        TurtleGraphic.__init__(self, turt, name, color, speed, xcoord, ycoord)
      
# Function to draw a flower using a turtle. Parameters:
    def draw(self):
        TurtleGraphic.draw(self)
        
# Draw flower as series of overlapping circles
        for i in range(6):
            self.get_turtle().circle(20)
            self.get_turtle().left(60)


