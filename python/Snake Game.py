# Simple Snake Game - Last Tested In: Python 3.7.2

# Imports
import turtle
import time
import random

delay = 0.1

# Score
score = 0
highscore = 0

segments = []

# Create a Window
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width = 700, height = 700)
window.tracer(0) # Turns off the screen updates

# Create Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Create Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Pen Turtle
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align = "center", font = ("Courier", 24, "normal"))

# Functions
def goup():
    if head.direction != "down":
        head.direction = "up"
    
def godown():
    if head.direction != "up":
        head.direction = "down"
    
def goright():
    if head.direction != "left":
        head.direction = "right"
    
def goleft():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
        
    if head.direction == "down":
        head.sety(head.ycor() - 20)
        
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard Bindings
window.listen()
window.onkeypress(goup, "w")
window.onkeypress(goup, "W")
window.onkeypress(goup, "Up")
window.onkeypress(godown, "s")
window.onkeypress(godown, "S")
window.onkeypress(godown, "Down")
window.onkeypress(goleft, "a")
window.onkeypress(goleft, "A")
window.onkeypress(goleft, "Left")
window.onkeypress(goright, "d")
window.onkeypress(goright, "D")
window.onkeypress(goright, "Right")

# Main Game Loop
while True:
    window.update()
    
    # Check For Collision With Boarders
    if head.xcor() > 320 or head.xcor() < -320 or head.ycor() > 320 or head.ycor() < -320:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
        # Hide the Segments
        for segment in segments:
            segment.goto(1000, 1000)
            
        # Clear the Segments List
        segments.clear()
        
        # Reset the Score
        score = 0
        
        # Reset the Delay
        delay = 0.1
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, highscore), align = "center", font = ("Courier", 24, "normal"))
    
    # Check for collision with food
    if head.distance(food) < 20:
        # Move Food to Rand Spot
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
    
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light green")
        new_segment.penup()
        segments.append(new_segment)
        
        # Shorten the Delay
        delay -= 0.001
        
        # Increase Score
        score += 10
        
        if score > highscore:
            highscore = score
            
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, highscore), align = "center", font = ("Courier", 24, "normal"))
    
    # Move End Segments First (Reverse Order)
    for index in range(len(segments) - 1, 0, -1):
        segments[index].goto(segments[index - 1].xcor(), segments[index - 1].ycor())
    
    # Move Segment 0 to head's last position
    if len(segments) > 0:
        segments[0].goto(head.xcor(),head.ycor())
    
    move()
    
    # Check for Head Collision With Body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            # Hide the Segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            # Clear the Segments List
            segments.clear()
            
            # Reset the Score
            score = 0
            
            # Reset the Delay
            delay = 0.1
            
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, highscore), align = "center", font = ("Courier", 24, "normal"))
    
    time.sleep(delay)



window.mainloop()


