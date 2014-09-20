import turtle
import time

boxsize = 200
caught = False
score = 0


#Functions called when keys are pressed
def up() :
    mouse.forward(10)
    checkbound()

def left() :
    mouse.left(45)

def right() :
    mouse.right(45)

def back() :
    mouse.backward(10)
    checkbound()

def quitTurtles() :
    window.bye()

#prevents the mouse from leaving the square set by box size
def checkbound():
    global boxsize
    if mouse.xcor() > boxsize:
        mouse.goto(boxsize, mouse.ycor())
    if mouse.xcor() < -boxsize:
        mouse.goto(-boxsize, mouse.ycor())
    if mouse.ycor() > boxsize:
        mouse.goto(mouse.xcor(), boxsize)
    if mouse.ycor() < -boxsize:
        mouse.goto(mouse.xcor(), -boxsize)

#create a window two cats and the mouse tha will be in the game
window = turtle.Screen()
mouse = turtle.Turtle()
cat1 = turtle.Turtle()
cat2 = turtle.Turtle()
mouse.penup()
cat1.penup()
cat2.penup()

#goto corner of playing area
mouse.penup()
mouse.goto(-boxsize, -boxsize)
mouse.pendown()

#draw the borders of the playing area
for i in range(0, 4):
    mouse.forward(2*boxsize)
    mouse.left(90)

mouse.penup()

#set starting positions of the mouse and the cats
mouse.goto(0, 0)
cat1.goto(-boxsize, -boxsize)
cat2.goto(boxsize, boxsize)
cat1.setheading(cat1.towards(mouse))
cat2.setheading(cat2.towards(mouse))

#add key listeners
window.onkeypress(up, "Up")
window.onkeypress(left, "Left")
window.onkeypress(right, "Right")
window.onkeypress(back, "Down")
window.onkeypress(quitTurtles, "Escape")

difficulty = window.numinput("Difficulty", "Enter difficulty", minval=1, maxval=5)

window.listen()

while not caught:
    cat1.setheading(cat1.towards(mouse))
    cat1.forward(9+difficulty)
    cat2.setheading(cat2.towards(mouse))
    cat2.forward(7+difficulty)
    score = score + 1
    if cat1.distance(mouse) < 5:
        caught = True
    elif cat2.distance(mouse) < 5:
        caught = True
    time.sleep(0.2-(0.01*difficulty))

window.bye()
