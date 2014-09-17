import turtle
import time

boxsize = 200
cauhgt = False
score = 0


#Functions called when keys are pressed
def up():
    mouse.forward(10)
    checkbound()

def left():
    mouse.left(45)

def right():
    mouse.right(45)

def back():
    mouse.backward(10)
    checkbound()

def quitTurtles():
    window.bye()

#prevents the mouse from leaving the square set by box size
def checkbound():
    global boxsize
    if mouse.xcor() > boxsize:
        mouse.goto(boxsize, mouse.ycor())
    if mouse.xcor() < -boxsize:
        mouse.goto(-boxsize, mouse.ycor())
    if mouse.xcor() > boxsize:
        mouse.goto(mouse.xcor, boxsize)
    if mouse.xcor() < -boxsize:
        mouse.goto(mouse.xcor, -boxsize)

#setup screen
window = turtle.Screen()
mouse = turtle.Turtle()
cat = turtle.Turtle()
mouse.penup()
mouse.goto(100, 100)
mouse.pendown()

#add key listeners
window.onkeypress(up, "Up")
window.onkeypress(left, "Left")
window.onkeypress(right, "Right")
window.onkeypress(back, "Down")
window.onkeypress(quitTurtles, "Escape")

difficulty = window.numinput("Difficulty", "Enter difficulty", minval=1, maxval=5)

while not cauhgt:
    cat.setheading(cat.towards(mouse))
    cat.forward(8+difficulty)
    score = score + 1
    if cat.distance(mouse) < 5:
        cauhgt = False
    time.sleep(0.2-(0.01*difficulty))

window.bye()
