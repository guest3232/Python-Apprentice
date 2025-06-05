"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules
import turtle #Yes. A turtle.
from tkinter import Tk, messagebox, simpledialog
# Create a window object
t=turtle.Turtle()
turtle.setup(600, 600, 0, 0)
turtle.shape('turtle')
window = Tk()
# Hide the window, hint: use the withdraw method
window.withdraw()
# Ask the user for the first number
str_integer = 'integer'
value = 0
accepted = 1
for i in range(1):
   int1 = simpledialog.askinteger('First Integer', 'Enter the first integer.')
   # Ask the user for the second number
   int2 = simpledialog.askinteger('Second Integer', 'Enter the second integer.')
   # Ask the user for the math operation
   operator_choice = simpledialog.askstring('Choose your Operator', 'Symbols or ALL lowercase letters.')
   # Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
   symbol_add = ['+', 'add', 'addition', 'sum', 'plus', 'more']
   symbol_subtract = ['-', 'subtract', 'subtraction', 'less', 'remove', 'more', 'minus', 'difference']
   symbol_multiply = ['*', 'times', 'multiply', 'multiplication', 'factor', 'x']
   symbol_divide = ['/', "divide", 'division', 'quotient', 'divide by', 'divide symbol']
   if operator_choice in symbol_add:
      value = int1 + int2
   elif operator_choice in symbol_subtract:
      value = int1 - int2
   elif operator_choice in symbol_multiply:
      value = int1 * int2
   elif operator_choice in symbol_divide:
      value = int1 / int2
         # If the user enters an unknown operation, display an error message. ( use messagebox.showerror()
   else:
      messagebox.showerror("Invalid Response", "This 'calculator' can only accept generic keyboard symbols or lowercase letters of addition, subtraction, multiplication, or division.")
      accepted = 0
if accepted:
   messagebox.showinfo('Value:', value)
# Keep the window open
turtle.exitonclick()