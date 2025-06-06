"""

Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. Then, access those
lists to draw the pattern.

Hint: all of your lists should have the same number of elements.
Review the 'Using Lists' section of the previous lessons if you need 
more help.

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 


forwards = range(80, 160, 10)
lefts = range(30, 360, 45)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown']

for i in range(8):

    forward = forwards[i]
    left = lefts[i]
    color = colors[i]
 

    tina.color(color)
    tina.forward(forward)
    tina.left(left)

turtle.exitonclick()