# Import all of the graphics required
from wreath import Wreath
from flower import Flower
from wheel import Wheel
import turtle
from mygraphic import MyGraphic 

def main():
    # Create a list to hold various types of graphics
    mylist = []

    # Create a wreath and add it to the list of graphics
    t1 = turtle.Turtle()
    wreath1 = Wreath(t1, "wreath1", "blue", 0, -150,0)
    mylist.append(wreath1)
    
    # Create a flower and add it to the list of graphics
    t2 = turtle.Turtle()
    flower1 = Flower(t2, "flower", "purple", 0, 100,100)
    mylist.append(flower1)
    
    # Create a wheel and add it to the list of graphics
    t3 = turtle.Turtle()
    wheel1 = Wheel(t3, "wheel", "green", 0, -200, -200)
    mylist.append(wheel1)

    # Create mygraphic and add it to the list of graphics
    t4 = turtle.Turtle()
    mygraphic = MyGraphic(t4, 'mygraphic', 'red', 0, 100, -100)
    mylist.append(mygraphic)
    
    # Loop through the list of graphics and display each
    for graphic in mylist:
        graphic.draw()
       
    
main()