#Homework 10 - Jared Jamieson
from flower import Flower
from wheel import Wheel
from wreath import Wreath

# Class that represents a picture to be drawn on the screen.
class Picture:

# The __init__ method is passed a turtle, the name of the graphic, the color of
# the graphic, the drawing speed and the x and y coordinates. 
    def __init__(self, turt, name, color, speed, xcoord, ycoord):
        self.__turtle = turt
        self.__name = name
        self.__color = color
        self.__speed = speed
        self.__xcoord = xcoord
        self.__ycoord = ycoord
        self.__graphicslist = []
        
# Prints the number of graphics contained in picture
    def __str__(self):
        print('There are %d elements in the picture' % len(self.__graphicslist))
        
# Adds a flower, wreath, or wheel to list of graphics
    def add_graphic(self):
        numgraphics = int(input('How many graphics would you like to add? '))
        while numgraphics != 0:
            self.__graphicslist.append(str(input('What graphic would you like to draw? (wreath, flower, or wheel): ')))
            numgraphics -= 1
        
# Returns list of graphics represented in picture
    def get_graphics(self):
        return(self.__graphicslist)
        
# Displays all graphics in graphics list
    def draw_picture(self):
        for i in self.__graphicslist:
            if i == 'flower':
                turt = 'turtle'
                name = str(input('Enter a turtle name: '))
                color = str(input('Enter a graphic color: '))
                speed = int(input('Enter a turtle speed: '))
                xcoord = int(input('Enter an x coordinate: '))
                ycoord = int(input('Enter a y coordinate: '))
                userflower = Flower(turt, name, color, int(speed), xcoord, ycoord)
                userflower.draw()
                
            elif i == 'wheel':
                turt = 'turtle'
                name = str(input('Enter a turtle name: '))
                color = str(input('Enter a graphic color: '))
                speed = int(input('Enter a turtle speed: '))
                xcoord = int(input('Enter an x coordinate: '))
                ycoord = int(input('Enter a y coordinate: '))
                userwheel = Wheel(turt, name, color, int(speed), xcoord, ycoord)
                userwheel.draw()
                
            else:
                turt = 'turtle'
                name = str(input('Enter a turtle name: '))
                color = str(input('Enter a graphic color: '))
                speed = int(input('Enter a turtle speed: '))
                xcoord = int(input('Enter an x coordinate: '))
                ycoord = int(input('Enter a y coordinate: '))
                userwreath = Wreath(turt, name, color, int(speed), xcoord, ycoord)
                userwreath.draw()
        Picture.__str__(self)
        
        
# Main function
def main():
    # Innitializes the Picture class
    pictureclass = Picture('Turtle', 'Name', 'Color', 'Speed', 'xcoord', 'ycoord')
    
    # Picture class function calls
    #pictureclass.__str__()
    pictureclass.add_graphic()
    #print(pictureclass.get_graphics())
    pictureclass.draw_picture()
    
    
    
main()
        