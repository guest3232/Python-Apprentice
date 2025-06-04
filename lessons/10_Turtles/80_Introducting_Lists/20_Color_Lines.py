"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina
tina.write('This is Tina.')
tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 
movement = 50
turning = 90

bug = turtle.Turtle()                                   #Originally called the turtle "Bug" instead of turtle or t
bug.penup()
bug.shape("turtle")
bug.speed(0)
bug.goto(-100, 100)
bug.write('This is not Tina.')

colors = [ 'red', 'blue', 'black', 'orange']    # define a list of colors

for color in colors:                            # loop through the colors
    tina.pencolor(color)
    tina.forward(movement)
    tina.right(turning)


# 2) Make another square, but put the colors in reverse order, using a negative index. 
# Double click on this cell to copy the code. 
"""
import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
"""
colorsreverse = [ 'orange', 'black', 'blue', 'red']
bug.speed(2)
bug.pendown()
for color in colorsreverse:
    bug.pencolor(color)
    bug.forward(movement)
    bug.left(turning)
turtle.exitonclick()                     # Close the window when we click on it