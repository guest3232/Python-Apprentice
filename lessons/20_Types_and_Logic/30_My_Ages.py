
"""
Am I Big Yet?

Ask the user's age then use an if-elif-else statement to 
tell the user what age groups the user is in. The groups are:

0-2: Baby
3-5: Toddler
6-12: Child
13-19: Teen
20-64: Adult
65+: Senior

Except, if the user is the same age as you, print "You are pretty awesome!"

Here is how you ask the user's age in integer format.  The first argument is 
the title of the window, the second is the message to the user.

age = simpledialog.askinteger("Your Age", "How old are you?")

Or, you could ask the user for a float with simpledialog.askfloat() 

age =  simpledialog.askfloat("Your Age", "How old are you?")


Here is how you show the user a message window. The first parameter is the title of the window, 
the second is the message to show the user.

messagebox.showinfo('What you are', "You are a baby.")

"""

from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups

# Ask the user's age
age_ask = simpledialog.askinteger("Your Age", "How old are you?")
agegroup_title = 'Age Group'
agegroup_desc = 'This age group contains'
an = 'an'
a = 'a'
space = ' '
colon = ':'
vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O'] #'u', 'U'
# Use if statements to determine the age group
# and create a message
if age_ask >=0 and age_ask <=2:
    age = 'Baby'
elif age_ask >=3 and age_ask <=5:
    age = 'Toddler'
elif age_ask >=6 and age_ask <=12:
    age = 'Child'
elif age_ask >=13 and age_ask <=17:
    age = 'Teen'
elif age_ask >=18 and age_ask <=64:
    age = 'Adult'
else:
    age = 'Senior'
if age.startswith(str(vowel[1])):
    a_an = an
else:
    a_an = a
print(a_an)
agegroup_whole = messagebox.showinfo("agegroup_title", agegroup_desc + space + a_an + colon + space + age)
# Show the message to the user

#window.mainloop()  # Keeps the window open


# TODO: 
# Try to write your program so you only need to use one messagebox.showinfo() function.