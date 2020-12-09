# Simple Pong - Last Tested In: Python 3.7.2

# Imports
import turtle
import winsound
import time

# Create a window
window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

# Score
scorea = 0
scoreb = 0

# Paddle A
paddlea = turtle.Turtle()
paddlea.speed(0)
paddlea.shape("square")
paddlea.color("white")
paddlea.shapesize(5, 1)
paddlea.penup()
paddlea.goto(-350, 0)

# Paddle B
paddleb = turtle.Turtle()
paddleb.speed(0)
paddleb.shape("square")
paddleb.color("white")
paddleb.shapesize(5, 1)
paddleb.penup()
paddleb.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(100)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# d means delta, or change
ball.dx = .30
ball.dy = -.30

# Pen Turtle
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Player A: 0  Player B: 0", move = False, align = "center", font = ("Courier", 12, "normal"))

# Functions
def paddlea_up():
    y = paddlea.ycor()
    if y <= 250:
        y += 20
        paddlea.sety(y)
    
def paddlea_down():
    y = paddlea.ycor()
    if y >= -220:
        y -= 20
        paddlea.sety(y)
    
def paddleb_up():
    y = paddleb.ycor()
    if y <= 250:
        y += 20
        paddleb.sety(y)
    
def paddleb_down():
    y = paddleb.ycor()
    if y >= -220:
        y -= 20
        paddleb.sety(y)
    
# Keyboard Binding
window.listen()
window.onkeypress(paddlea_up, "w")
window.onkeypress(paddlea_down, "s")
window.onkeypress(paddlea_up, "W")
window.onkeypress(paddlea_down, "S")
window.onkeypress(paddleb_up, "Up")
window.onkeypress(paddleb_down, "Down")

# Main Game Loop
while True:
        window.update()
    
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
    
        # Boarder Checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) # Creates sound from file on windows
    
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            scorea += 1
            scoreboard.clear()
            scoreboard.write("Player A: {}  Player B: {}".format(scorea, scoreb), move = False, align = "center", font = ("Courier", 12, "normal"))
    
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            scoreb += 1
            scoreboard.clear()
            scoreboard.write("Player A: {}  Player B: {}".format(scorea, scoreb), move = False, align = "center", font = ("Courier", 12, "normal"))
        
        
        # Paddle and Ball Collision
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleb.ycor() + 40 and ball.ycor() > paddleb.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddlea.ycor() + 40 and ball.ycor() > paddlea.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
