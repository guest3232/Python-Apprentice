""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()

def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

#def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""
"""
    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(600, 600, startx=0, starty=0)
    window.bgpic(image_path)
set_background_image(screen, "spiral.png")
"""
... # Your Code Here
t.shape("turtle")
#set_turtle_image(t, "leaguebot_bolt.gif")
#t.turtlesize(stretch_wid=1, stretch_len=1, outline=1)
t.pencolor('blue')
t.speed(2)
def draw_polygon(sides):
    angles = 360/sides
    print("Angle for ", sides, " sides is ", angles)

    for i in range(sides):
        t.forward(75)
        t.left(angles)
draw_polygon(6)

turtle.exitonclick()