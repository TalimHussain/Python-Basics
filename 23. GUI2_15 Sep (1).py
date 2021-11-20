"""GUI Contd."""

# # New Program
# from tkinter import *
#
# def btn_Click():
#     print("Button is clicked")
#
# root = Tk()
# root.geometry("500x500+200+150")
#
# btn = Button(root, text = "Click Me", font = ("Monotype Corsiva", 24), command = btn_Click)
# btn.pack(side = 'top')
#
# root.mainloop()

"""
Entry Widget: In GUI Programming, Entry Widget works like the input function of CUI, i.e., it is
used to take input values from the user

var_name = value
"""

# x = int()
# print(x)


# # New Program
# from tkinter import *
#
# def btn_Click():
#     name = entrVar.get()
#     print(f"The name entered is: {name}")
#     entrVar.set("")
#
# root = Tk()
# root.geometry("500x350+600+200")
#
# lbl = Label(root, text = "Enter your name", font = ("Times New Roman", 22))
# lbl.grid(row = 0, column = 0)
#
# entrVar = StringVar()
# entr = Entry(root, textvariable = entrVar, font = ("Times New Roman", 22))
# entr.grid(row = 0, column = 1)
#
# btn = Button(root, text = "Submit", font = ("Times New Roman", 22), command = btn_Click)
# btn.grid(row = 1, column = 1)
#
# root.mainloop()


# # New Program
# from tkinter import *
#
# root = Tk()
# root.geometry("900x550+600+200")
#
# lblID = Label(root, text = "Enter Customer ID: ", font = ("Times New Roman", 24))
# lblID.grid(row = 0, column = 0)
# varID = StringVar()
# entrID = Entry(root, font = ("Times New Roman", 24), textvariable = varID)
# entrID.grid(row = 0, column = 1)
#
# lblName = Label(root, text = "Enter Customer Name: ", font = ("Times New Roman", 24))
# lblName.grid(row = 1, column = 0)
# varName = StringVar()
# entrName = Entry(root, font = ("Times New Roman", 24), textvariable = varName)
# entrName.grid(row = 1, column = 1)
#
# lblAge = Label(root, text = "Enter Customer Age: ", font = ("Times New Roman", 24))
# lblAge.grid(row = 2, column = 0)
# varAge = StringVar()
# entrAge = Entry(root, font = ("Times New Roman", 24), textvariable = varAge)
# entrAge.grid(row = 2, column = 1)
#
# lblMob = Label(root, text = "Enter Customer Mob: ", font = ("Times New Roman", 24))
# lblMob.grid(row = 3, column = 0)
# varMob = StringVar()
# entrMob = Entry(root, font = ("Times New Roman", 24), textvariable = varMob)
# entrMob.grid(row = 3, column = 1)
#
# btnAdd = Button(root, text = "Add Customer", font = ("Times New Roman", 24))
# btnAdd.grid(row = 4, column = 0)
#
# btnSearch = Button(root, text = "Search Customer", font = ("Times New Roman", 24))
# btnSearch.grid(row = 4, column = 1)
#
# btnUpdate = Button(root, text = "Update Customer", font = ("Times New Roman", 24))
# btnUpdate.grid(row = 4, column = 2)
#
# btnDelete = Button(root, text = "Delete Customer", font = ("Times New Roman", 24))
# btnDelete.grid(row = 5, column = 0)
#
# btnViewAll = Button(root, text = "View All Customer", font = ("Times New Roman", 24))
# btnViewAll.grid(row = 5, column = 1)
#
# btnExit = Button(root, text = "Exit", font = ("Times New Roman", 24))
# btnExit.grid(row = 5, column = 2)
#
# root.mainloop()




# # New Program
# from tkinter import *
#
# def btn_Click():
#     print("Button is clicked")
#
# root = Tk()
# root.geometry("500x500+200+150")
#
# btn = Button(root, text = "Click Me", font = ("Monotype Corsiva", 24), command = btn_Click)
# btn.pack(side = 'top')
#
# root.mainloop()

"""
The properties to a widget can be provided in 3 different ways:

1. While creating the widget
WidgetClass(properties as keyword arguments)

2. By accessing the properties like dictionary keys and then providing them with some values
widgetObject['property_name'] = value

3. Using config method:
widgetObject.config(properties as keyword arguments)
"""

# # New Program
# from tkinter import *
# root = Tk()
# root.geometry("300x300")
#
# btn = Button(root, text = "Click Me")
# btn.place(x = 125, y = 125)
# btn['font'] = ("Times New Roman", 24)
# btn['bg'] = "Black"
# btn.config(fg = "Orange")
#
# root.mainloop()


"""
Sometimes, we need to provide multiple handlers to the same widget, for example, when
on a button we have to perform two different operations when it is left clicked 
and right clicked

This is done with the help of the bind method.
In the bind method we provide the event that has to handled and its handler

Mouse Events:
There are different types of mouse events, like left mouse click, right mouse click, middle
mouse button click etc

"<Button 1>" ===> left mouse click
"<Button 2>" ===> middle mouse click
"<Button 3>" ===> right mouse click
"""

# # New Program
# from tkinter import *
#
# def btn1_Click(e):
#     print(e.x, e.y)
#     print(e.x_root, e.y_root)
#     print(e.widget)
#     widgt = e.widget
#     print(widgt['bg'])
#     print(widgt['text'])
#     print(widgt['fg'])
#
# root = Tk()
# root.geometry("500x500")
#
# btn = Button(root, text = "Click Me", font = ("", 24), bg = 'Red', fg = "Blue")
# btn.place(x = 200, y = 200)
# btn.bind("<Button 1>", btn1_Click)
#
# root.mainloop()


# New Program
from tkinter import *

def left_Click(e):
    btn['bg'] = "Red"

def right_Click(e):
    btn['bg'] = "Blue"

def btn_Enter(e):
    btn['bg'] = "Green"

def btn_Leave(e):
    btn['bg'] = "Yellow"

root = Tk()
root.geometry("500x500")

btn = Button(root, text = "Click Me", font = ("", 24))
btn.place(x = 200, y = 200)
btn.bind("<Button 1>", left_Click)
btn.bind("<Button 3>", right_Click)
btn.bind("<Enter>", btn_Enter)
btn.bind("<Leave>", btn_Leave)

root.mainloop()








