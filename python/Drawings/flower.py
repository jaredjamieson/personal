#Homework 10 - Jared Jamieson
import turtle

# Class that represents a flower to be drawn on the screen.
class Flower:
    
# The __init__ method is passed a turtle, the name of the graphic, the color of
# the graphic, the drawing speed and the x and y coordinates. 
    def __init__(self, turt, name, color, speed, xcoord, ycoord):
        self.__turtle = turt
        self.__name = name
        self.__color = color
        self.__speed = speed
        self.__xcoord = xcoord
        self.__ycoord = ycoord
        
# Returns the data associated with a flower as a string. 
    def __str__(self):
        datastr = [self.__turtle, self.__name, self.__color, self.__speed, self.__xcoord, self.__ycoord]
        return datastr
 
# The draw method draws a flower on the screen.
    def draw(self):
        self.__turtle = turtle.Turtle(self.__turtle)
        self.__turtle.speed(self.__speed)
        self.__turtle.pensize(3)
        self.__turtle.color(self.__color)
        self.__turtle.penup()
        self.__turtle.setx(self.__xcoord)
        self.__turtle.sety(self.__ycoord)
        self.__turtle.pendown()

# Draw flower as series of overlapping circles
        for i in range(6):
            self.__turtle.circle(20)
            self.__turtle.left(60)

# "Setter" methods for the attributes of the flower class
    def set_color(self, color):
        self.__color = color
        
    def set_x(self, xcoord):
        self.__xcoord = xcoord
        
    def set_y(self, ycoord):
        self.__ycoord = ycoord
        
    def set_speed(self, speed):
        self.__speed = speed

# "Getter" methods for the flower class
    def get_color(self):
        return self.__color
        
    def get_x(self):
        return self.__xcoord
        
    def get_y(self):
        return self.__ycoord
        
    def get_speed(self):
        return self.__speed 
    
# Main function
def main():
    # Flower object - Turtle Name, Graphic Name, Color, Speed, X Coord, Y Coord
    flower1 = Flower('MyTurtle', 'Flower', 'Red', 5, 100, 100)
    #print(flower1.__str__())
    #flower1.draw() # ERROR 'str' object has no attribute 'speed'
    # Set method calls
    #flower1.set_color('blue')
    #flower1.set_x(50)
    #flower1.set_y(50)
    #flower1.set_speed(0)
    # Get method calls
    #print(flower1.get_color())
    #print(flower1.get_x())
    #print(flower1.get_y())
    #print(flower1.get_speed())
    
main()
