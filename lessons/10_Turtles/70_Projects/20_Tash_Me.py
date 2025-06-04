""" Tash Me

Write a program that:
1) Loads an emoji image as the background
2) Make the turtle shape a moustach
3) Move the moustache to the right spont on the emoji

Hint: See 08a_More Turtle Programs, section 'Change the Background Image' and
'Change the Turtle Shape'
"""

... # Your code here
import turtle, random
bg = random.randint(1, 2)
moustache = random.randint(1, 3)
screen = turtle.Screen()
screen.setup(width=600, height=600)

def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""

    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

t=turtle.Turtle()
t.penup()
set_turtle_image(t, "moustache1.gif")
#set_turtle_image(t, "moustache2.gif")
#set_turtle_image(t, "moustache3.gif")
#set_background_image(screen, "emoji.png")
#t.sety(0)
set_background_image(screen, "emoji2.png")
t.sety(-25)
turtle.exitonclick()