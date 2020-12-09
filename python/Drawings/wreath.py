#Homework 10 - Jared Jamieson
import turtle

# Class that represents a wreath to be drawn on the screen.
class Wreath:

# The __init__ method is passed a turtle, the name of the graphic, the color of
# the graphic, the drawing speed and the x and y coordinates. 
    def __init__(self, turt, name, color, speed, xcoord, ycoord):
        self.__turtle = turt
        self.__name = name
        self.__color = color
        self.__speed = int(speed)
        self.__xcoord = xcoord
        self.__ycoord = ycoord
        
# Returns the data associated with a wreath as a string. 
    def __str__(self):
        datastr = [self.__turtle, self.__name, self.__color, self.__speed, self.__xcoord, self.__ycoord]
        return datastr
 
# The draw method draws a wreath on the screen.
    def draw(self):
        self.__turtle = turtle.Turtle(self.__turtle)
        self.__turtle.speed(self.__speed)
        self.__turtle.pensize(3)
        self.__turtle.color(self.__color)
        self.__turtle.penup()
        self.__turtle.setx(self.__xcoord)
        self.__turtle.sety(self.__ycoord)
        self.__turtle.pendown()

# Draw wreath as series of overlapping squares
        for count in range(36):
            self.__turtle.forward(100)
            self.__turtle.right(100)

# "Setter methods for the attributes of the Wreath class
    def set_color(self, color):
        self.__color = color
        
    def set_x(self, xcoord):
        self.__xcoord = xcoord
        
    def set_y(self, ycoord):
        self.__ycoord = ycoord
        
    def set_speed(self, speed):
        self.__speed = speed

# "Getter" methods for the Wreath class
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
    # Wreath object - Turtle Name, Graphic Name, Color, Speed, X Coord, Y Coord
    wreath1 = Wreath('MyTurtle', 'Wreath', 'Red', 5, 100, 100)
    #print(wreath1.__str__())
    #wreath1.draw() # ERROR 'str' object has no attribute 'speed'
    # Set method calls
    #wreath1.set_color('blue')
    #wreath1.set_x(50)
    #wreath1.set_y(50)
    #wreath1.set_speed(0)
    # Get method calls
    #print(wreath1.get_color())
    #print(wreath1.get_x())
    #print(wreath1.get_y())
    #print(wreath1.get_speed())
    
main()
