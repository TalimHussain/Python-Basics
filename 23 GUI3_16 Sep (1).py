"""GUI 3"""

"""
Providing an image as background on a widget:

There are two techniques:

1. gif and png files
"""

# from tkinter import *
# root = Tk()
# root.geometry("600x600")
#
# image = PhotoImage(file ='mario.png')
# btn = Button(root, image = image)
# btn.pack()
#
# root.mainloop()

"""
2. Any other image type:

First of all you have to install a library called PIL (Python Imaging Libray)
Command: pip install Pillow
"""

# # New Program
# from tkinter import *
# from PIL import Image, ImageTk
#
# root = Tk()
# image = Image.open('landscape.jpeg')
# photo = ImageTk.PhotoImage(image)
#
# lbl = Label(root, image = photo)
# lbl.pack()
#
# root.mainloop()



# New Program
from tkinter import *
from tkinter import filedialog
import tkinter.colorchooser as tkc

def func1():
    print("Save is clicked")

def file_Open():
    path = filedialog.askopenfilename()
    print(path)
    f = open(path, 'r')
    data = f.read()
    print(data)

def exit_Click():
    exit()

def func2():
    print("Undo is clicked")

def selectColor():
    choice = tkc.askcolor()
    print(choice)
    color = choice[1]
    btn['bg'] = color

def func3(e):
    print("'a' is pressed")

def func4(e):
    print("'z' is pressed")

def func5(e):
    print("'Hello' is pressed")

def func6(e):
    print("Enter Button is pressed")

root = Tk()
root.geometry("500x500")

menubar = Menu(root)

filemenu = Menu(menubar)
filemenu.add_cascade(label = "Save", command = func1)
filemenu.add_cascade(label = "Open", command = file_Open)
filemenu.add_separator()
filemenu.add_cascade(label = "Exit", command = exit_Click)
menubar.add_cascade(label = 'File', menu = filemenu)

editmenu = Menu(menubar)
editmenu.add_cascade(label = "Undo", command = func2)
menubar.add_cascade(label = "Edit", menu = editmenu)

btn = Button(root, text = "Select Color", font = ("", 24), command = selectColor)
btn.pack()

root.bind('a', func3)
root.bind('z', func4)
root.bind('Hello', func5)
root.bind("<Return>", func6)


root.config(menu = menubar)
root.mainloop()

