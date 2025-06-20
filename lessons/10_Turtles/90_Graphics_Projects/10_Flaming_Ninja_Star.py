"""Flaming Ninja Star

This program already works; run it to see what it does. 
Then change it to make it draw a different pattern. 
"""

import random
import turtle


# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["red", "blue", "green", "yellow", "orange"]
redfirecolors = ["red", "orange", "yellow", "grey", "gray", "black"]
bluefirecolors = ["blue", "purple", "magenta", "pink", "gray", "black"]

def getNextColor(i):
    return colors[i % len(colors)]

turtle.setup(600,600,0,0)               # Set the size of the window
window = turtle.Screen()

baseSize = 200  # the size of the black part of the star
flameSize = 130  # the length of the flaming arms

t = turtle.Turtle() 

t.shape("turtle") 

t.width(2) 

t.speed(0) 

for i in range(25):
    t.pencolor(getRandomColor())

    t.fillcolor(getRandomColor()) 
   
    t.begin_fill()

    t.forward(64) 

    t.left(70) 

    t.forward(flameSize) 

    t.right(170) 

    t.forward(flameSize) 

    t.right(72) 

    t.forward(baseSize) 

    t.end_fill()

t.hideturtle() 

turtle.done() 
