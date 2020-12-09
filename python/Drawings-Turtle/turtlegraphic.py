# Homework 11 - Jamieson

# Imports
import turtle

# The TurtleGraphic class
class TurtleGraphic:
    
    # Constructor
    def __init__(self, turt, name, color, speed, xcoord, ycoord):
        self.__turtle = turt
        self.__name = name
        self.__color = color
        self.__speed = speed
        self.__xcoord = xcoord
        self.__ycoord = ycoord
        
    # Draw method - Sets turtle attributes
    def draw(self):
        self.__turtle.speed(self.__speed)
        self.__turtle.pensize(3)
        self.__turtle.color(self.__color)
        self.__turtle.penup()
        self.__turtle.setx(self.__xcoord)
        self.__turtle.sety(self.__ycoord)
        self.__turtle.pendown()
        
    # String method - Returns data associated with shape
    def __str__(self):
        datastr = [self.__turtle, self.__name, self.__color, self.__speed, self.__xcoord, self.__ycoord]
        return datastr
        
    # Sets the color
    def set_color(self):
        self.__color = str(input('Enter a graphic color: '))
    
    # Sets the speed
    def set_speed(self):
        self.__speed = str(input('Enter a speed: '))
        
    # Sets the xcoord
    def set_xcoord(self):
        self.__xcoord = str(input('Enter the x-coordinate: '))
        
    # Sets the ycoord
    def set_ycoord(self):
        self.__ycoord = str(input('Enter the y-coordinate: '))
    
    # Gets the color
    def get_color(self):
        return self.__color
    
    # Gets the speed
    def get_speed(self):
        return self.__speed
    
    # Gets the xcoord
    def get_xcoord(self):
        return self.__xcoord
    
    # Gets the ycoord
    def get_ycoord(self):
        return self.__ycoord
    
    # Gets the turtle
    def get_turtle(self):
        return self.__turtle

'''
# The main function
def main():
    
    # Innitialize the turtlegraphic class
                             # turt, name, color, speed, xcoord, ycoord
    mygraphic = TurtleGraphic('turt', 'name', 'red', 0, 100, 100)
    
    # Set method calls
    mygraphic.set_color()
    mygraphic.set_speed()
    mygraphic.set_xcoord()
    mygraphic.set_ycoord()
    
    # Get method calls
    print(mygraphic.get_color())
    print(mygraphic.get_speed())
    print(mygraphic.get_xcoord())
    print(mygraphic.get_ycoord())
    print(mygraphic.get_turtle())
    
main()
'''