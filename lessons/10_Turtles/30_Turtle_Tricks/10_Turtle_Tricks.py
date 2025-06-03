"""
For this program, you will tell Tina the Turtle to draw a triangle.

You should look at the previous programs to see how to use the turtle commands.
Copy lines of code from those programs to this one to draw a triangle.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

... # Your code here

tina.shape('turtle')
tina.speed(2)

tina.penup()
tina.goto(-100, 100)
tina.pendown()

tina.pencolor('red')
tina.forward(50)
tina.left(120)

tina.pencolor('orange')
tina.forward(50)
tina.left(120)

tina.pencolor('blue')
tina.forward(50)

tina.penup()
tina.pencolor('green')
tina.left(30)
tina.forward(40)

turtle.exitonclick()                    # Close the window when we click on it
