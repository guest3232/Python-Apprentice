"""
The is a simple Turtle program that draws a square and writes a message. The
lines that start with a # are comments. They are not executed by Python. The
lines inside the three quotes are also comments, but of a different sort (
called "doc comments" ) Comments are used to explain what the code does. Read
the program and try to understand what each line does.



"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast.

##
## Move Tina to the Starting Position
#

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.goto(-100, 100)                    # Move tina to the starting position
tina.pendown()                          # Put the pen down so we can draw

##
## Draw a Square
##


tina.pencolor('blue')                   # Set the pen color to blue
tina.forward(200)                       # Move tina forward by the forward distance
tina.right(90)                          # Turn tina left by the left turn

tina.pencolor('red')                    # Set the pen color to red
tina.forward(200)                       # Continuie the last two steps three more times
tina.right(90)                           # to draw a square

tina.pencolor('green')                  # Set the pen color to green
tina.forward(200)
tina.right(90)

tina.pencolor('purple')                 # Set the pen color to purple
tina.forward(200)
tina.right(90)

##
## Draw a Circle
##

tina.penup()     
tina.goto(0, -75)
tina.pendown()     

tina.pendown()
tina.color('red')                       # Set the color of tina to red
tina.begin_fill()
tina.circle(75)
tina.end_fill()

##
## Write a Message
##

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.goto(-50, -150)
tina.forward(20)                        # Move tina forward by 20
tina.left(90)                           # Turn tina left by 90 degrees
tina.forward(20)                        # Move tina forward by 20
tina.write("This is how to draw shapes on a computer using Python.")         # Write the message "Why, hello there!"
tina.backward(20)                       # Move tina backward by 20



turtle.exitonclick()                    # Close the window when we click on it  

# You're on your way, soon you'll be writing your own programs!
# But first, let's save your progress. Continue with 
# the next file, 03_Check_In_Your_Code.ipynb
