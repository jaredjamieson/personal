#Jared Jamieson, turtle_funct ,Homework 5
#This program draws flowers and spirales on the screen at various locations.

#Imports
import turtle
import random

#Global Variables
globalcolors = ["red", "blue", "green", "purple", "orange"]
numlist = [0, 1, 2, 3, 4, 5, 6]
t = turtle.Turtle()
t.pensize(10)

#Sets the background color to the user's choice.
def set_background(backgroundcolor):
    #Gets and sets screen to user choice color
    tscreen = turtle.Screen()
    tscreen.bgcolor(backgroundcolor)

# Draws a spiral of a particular color
def draw_spiral(side):
    # Code that draws the spiral
    for i in range (40):
        t.pendown()
        t.forward(side)
        t.left(24)
        side=side+1
        t.penup

# Function to draw a flower with num_ petals using circles of size 20 pixels.
# t - turtle
def num_petals(t, color, petals):
    t.penup
    while petals != 0:
        t.pendown()
        t.circle(20)
        t.pencolor(color)
        t.fillcolor(color)
        petals -= 1

def draw_flower(t, color, num_petals, x, y):
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()
    t.pencolor(color)
    t.fillcolor(color)
    # Calculate proper angle for petals on the flower based
    # on the number of petals so that they are evenly distributed
    # around the center
    angle = 360 / num_petals
    for i in range(num_petals):
        t.right(angle)
        t.forward(20)
        t.begin_fill()
        t.circle(8)
        t.end_fill()
        t.penup()
        t.setx(x)
        t.sety(y)
        t.pendown()

#Prints the menu options.
def print_menu():
    #Choices of what to draw
    print('1. Set background color') 
    print('2. Draw a flower using your color')
    print('3. Draw a flower using a random color')
    print('4. Draw a flower using a randow color and a random number of petals')
    print('5. Draw a spiral with your color')
    print('6. Draw a spiral with a random color')
    print('7. to quit')

#Uses a loop to print the menu and process user selections
def main():
    #Prime inputs
    backgroundcolor = 'white'
    side = 25
    color = 'red'
    num_petals = 0
    t.penup()
    x = t.setx(random.randint(-300,300))
    y = t.sety(random.randint(-300,300))
    t.pendown()
    flowers = random.randint(1, 3)
    spirals = random.randint(1, 3)
    #Prints user's choices
    print_menu()
    #User Choice
    menuchoice = int(input('Enter a menu choice: '))
    #Loop for print_menu choice
    while menuchoice != 7:
        if menuchoice == 1:
            backgroundcolor = input('Enter a background color: ')
            menuchoice = int(input('Enter a menu choice: '))
        elif menuchoice == 2:
            color = input('Enter a color: ')
            menuchoice = int(input('Enter a menu choice: '))
        elif menuchoice == 3:
            color = random.choice(globalcolors)
            menuchoice = int(input('Enter a menu choice: '))
        elif menuchoice == 4:
            color = random.choice(globalcolors)
            num_petals = random.choice(numlist)
            menuchoice = int(input('Enter a menu choice: '))
        elif menuchoice == 5:
            color = input('Enter a color: ')
            menuchoice = int(input('Enter a menu choice: '))
        else:
            color = random.choice(globalcolors)
            menuchoice = int(input('Enter a menu choice: '))
            
    while flowers > 0:
        draw_flower(t, color, num_petals, x, y)
        flowers = flowers - 1
        
    while spirals > 0:
        draw_spiral(side)
        spirals = spirals - 1
        
    #Function Calls
    set_background(backgroundcolor)

main()
