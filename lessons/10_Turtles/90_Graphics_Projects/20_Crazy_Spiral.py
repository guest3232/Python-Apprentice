"""
Crazy Spiral

Make your own crazy spiral with a pattern like
in 14_FLaming_Ninja_Star.py, but use what you've learned about loops
"""

... # Copy code to make a turtle and set up the window
import turtle
import random
turtle.setup(600,600,0,0)
t = turtle.Turtle()# Create a turtle named t
t.shape('turtle')
t.speed(0)

# 1) Complete make_a_shape() to make the turtle move in some pattern. 
# For instance, you can make it go left 30 degrees, then forward 50 pixels, 
# then right 60 degrees, then forward 100 pixels. Make any shape you like.
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def make_a_shape(t):
    """Make a shape with turtle t. Make it go left or right or forward"""
    t.pencolor(getRandomColor())
    t.fillcolor(getRandomColor())
    t.begin_fill()
    t.left(30)
    t.forward(50)
    t.right(60)
    t.forward(100)
    t.left(60)
    t.forward(120)
    t.right(55)
    t.forward(45)
    t.end_fill()

# 2) Call make_a_shape() in a loop to make the turtle draw a spiral.
# For instance, you can call make_a_shape() 100 times to make a spiral with 100 shapes.
# The second ... in the for loop should be the number of shapes you want to make, 
# for example 100, or it could use islice(), cycle(), or a list of numbers.

num_shapes = 3

t.goto(-100, 100)
for i in range(70):
    make_a_shape(t)
    t.right(360/num_shapes)

turtle.exitonclick()