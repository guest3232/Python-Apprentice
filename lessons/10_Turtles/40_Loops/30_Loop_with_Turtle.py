
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )

"""
import turtle
turtle.setup(600,600,0,0)
tina=turtle.Turtle()

tina.shape('turtle')
tina.speed(5)
tina.pencolor('red')
... # Movement
for i in range(5):
    tina.forward(150)                       # Move tina forward by the forward distance
    tina.left(72)
turtle.exitonclick()