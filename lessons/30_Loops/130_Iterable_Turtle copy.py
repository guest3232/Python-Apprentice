"""
Programmable turtle graphics

Use what you've learned about lists, loop, cycle, slice and zip to draw a pattern

"""
#from itertools import islice
import turtle
t = turtle.Turtle()                  # Create a turtle named tina
t.shape('turtle')                    # Set the shape of the turtle to a turtle
t.speed(2)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'black'] # Make a list of colors

directions = [ # Create a list of directions and angles
    ( 15, 100 ),
    ( 25, 50 ),
    ( 45, 75 ),
    ( 60, 100 ),
    ( 5, 25 ),
    ( 30, 60 )
]

# Zip the colors and directions together, then unpack them. There is a good example of this
# in 10_More_iterables.ipynb in the discussion of zip()

for color, (angle, distance) in zip(colors, directions):
    t.color( color )
    t.forward( distance )
    t.left( angle )

# Don't forget the special way to end a turtle program. 
turtle.exitonclick()