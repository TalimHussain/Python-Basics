"File Handling"

"""
File Handling: File handling is a technique which is used for permanent storage of data on the 
ROM.

In case that the data that we want to store permanently is small in size, then we use file 
handling, but if the data is large, then we use database
"""


# # New Program
# f = open(r"C:\Users\cipl\PycharmProjects\21 July Batch\file.txt", 'w')
# data = "Welcome to python class"
# f.write(data)
# f.close()


# # New Program
# f = open(r"C:\Users\cipl\PycharmProjects\21 July Batch\file.txt", 'r')
# data = f.read()
# print(data)
# f.close()


"""
Python is an OOPS based language, that means everything in python is done with the help of 
classes.
This means that file handling would also be achieved with the help of some class.
That class is the TextIOWrapper class
 
To use a class, we have to create an object of that class. But have we created an object of the 
TextIOWrapper class?

Factory functions: These are the functions which return the object of a class when they are 
called
"""

# class C1:
#     pass
#
#
# def func1():        # factory function
#     return C1()
#
# x = func1()
# print((type(x)))
#
# y = func1()
# print((type(y)))
#
# z = func1()
# print((type(z)))

"""
In file handling the open function is the factory function of the TextIOWrapper class
"""

# # New Program
# f = open(r"C:\Users\cipl\PycharmProjects\21 July Batch\file.txt", 'r')
# print(type(f))
# f.close()


"""
Different ways to access a file using file handling:

1. Character Oriented Stream: There are 6 different modes in which we can open a file in 
character oriented streams:

    a. 'r'  :   read mode   :   In the read mode if the specified file is present at the given 
    location, then it is opened and the data can be read. But if the file is not present at the 
    location, then it gives an error
    
    b. 'w'  :   write mode  :   In this mode, if the file is not present at the given location,
    then the program will create that file and write the data in it. But if that file already
    exists, then it will be truncated, i.e., the old data would be deleted and the new data 
    would be stored
    
    c. 'a'  :   append mode :   Here, if the file is not already present, then it is created and
    data is written in it. But if it is already present, then the new data would be written at
    the end of the file and the old data would not be deleted
    
    d. 'r+' :   read and write
    
    e. 'w+' :   write and read
    
    f. 'a+' :   append and read

2. Byte Oriented Stream: In byte oriented streams, the data is written and read in bytes format
It is also having 6 modes:

    a. 'rb' :   read bytes
    
    b. 'wb'
    
    c. 'ab'
    
    d. 'rb+'
    
    e. 'wb+'
    
    f. 'ab+'
"""

# # New Program
# f = open(r"C:\Users\cipl\PycharmProjects\21 July Batch\file1.txt", 'r')
# print(type(f))
# f.close()


# # New Program
# f = open(r"C:\Users\cipl\PycharmProjects\21 July Batch\file.txt", 'w')
# data = "You are at CETPA Noida"
# f.write(data)
# f.close()

# # New Program
# f = open(r"C:\Users\cipl\PycharmProjects\21 July Batch\file.txt", 'a')
# data = "Welcome to python class"
# f.write(data)
# f.close()



# # New Program
# f = open(r"C:\Users\cipl\PycharmProjects\21 July Batch\file.txt", 'r')
# data = f.read(10)
# print(data)
#
# print(f.tell())
#
# data = f.read(15)
# print(data)
#
# f.close()


"""
seek method: The seek method helps us to control the position of the cursor in the file that
we are using

Syntax:

seek(offset, whence)


whence: The whence argument is used to send the cursor at a place with respect to some position 
in the file.
In a byte oriented stream, it can have 3 values, i.e., 0, 1 and 2

whence = 0 : It will send the cursor to a position with respect to the starting of the file
whence = 1 : It will send the cursor to a position with respect to the current cursor position
whence = 2 : It will send the cursor to a position with respect to the end of the file

Note: In a character oriented stream, whence can have only one value, i.e., 0


offset: We can provide and positive or negative int value to this argument. It will move the 
cursor by that many places

offset: +ve: The cursor will move towards right by that many places

offset: -ve: THe cursor will move towards left by that many places
 


seek(7, 0) : The cursor will move 7 position towards right from the starting of the file

seek(0, 0) : The cursor will move 0 position from the starting of the file, i.e., the cursor
will reach at the starting of the file

seek(-5, 1) : The cursor will move 5 places towards left from the current position

seek(8,1) : 

seek(-14, 2) 


"""


# # New Program
# f = open(r"C:\Users\cipl\PycharmProjects\21 July Batch\file.txt", 'rb')
# data = f.read(12)
# print(data)
#
# print(f.tell())
#
# f.seek(7, 0)
#
# print(f.tell())
#
# data = f.read(15)
# print(data)
#
# print(f.tell())
#
# f.seek(5, 1)
#
# data = f.read(10)
# print(data)
#
# f.close()


# # New Program
#
# f = open(r"C:\Users\cipl\Desktop\GoToMeeting 000.png", 'rb')
# f1 = open(r"C:\Users\cipl\Desktop\GoToMeeting 000(1).png", 'wb')
#
# while True:
#     data = f.read(100)
#     if data == b'':
#         break
#     f1.write(data)
#
# f.close()
# f1.close()


"""
JSON and Pickling

Pickling; Pickling is python internal standard for transferring data between two python 
applications
Here the data is transferred in bytes format

JSON: JSON is the common standard using which we can transfer data from any application to any
other application

In JSON, data is transferred in the form of object arrays

[{'roll': 1, 'name': 'Aakash', 'marks': 90, 'phone': 1234},
{'roll': 2, 'name': 'Akshay', 'marks': 92, 'phone': 2345},
{'roll': 3, 'name': 'Biru Bhai', 'marks': 59, 'phone': 9876},
.
.
.
]

[] --> Arrays
{} --> object

JSON: Java Script Object Notation
"""


# # New program
# import pickle
# f = open(r"C:\Users\cipl\PycharmProjects\21 July Batch\pickle.txt", 'wb')
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# pickle.dump(data, f)
# f.close()


# # New program
# import pickle
# f = open(r"C:\Users\cipl\PycharmProjects\21 July Batch\pickle.txt", 'rb')
# data = pickle.load(f)
# print(data)
# f.close()


# # New program
# import json
# f = open(r"C:\Users\cipl\PycharmProjects\21 July Batch\json.txt", 'w')
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# json.dump(data, f)
# f.close()


# New program
import json
f = open(r"C:\Users\cipl\PycharmProjects\21 July Batch\json.txt", 'r')
data = json.load(f)
print(data)
f.close()














