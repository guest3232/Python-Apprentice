"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk
# Create a window object
window = Tk()     # Create a window object
# Hide the window, hint: use the withdraw method
window.withdraw() # Hide the window; we just want to see pop ups
# Ask the user for the first number   
integer1 = simpledialog.askinteger('Adding Two Numbers', 'Enter the First Number Here:')
# Ask the user for the second number
integer2 = simpledialog.askinteger('Adding Two Numbers', 'Enter the Second Number Here:')
# Display the sum of the two numbers 
messagebox.showinfo('Final Answer:', str(integer1+integer2))
print(integer1 + integer2)
# Keep the window open
#window.mainloop()