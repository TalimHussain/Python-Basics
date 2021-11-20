"Indexing and Print Function"

"""
Indexing: It is a technique using which we can access the elements present at a particular
index inside an iterable

Syntax of Indexing:
 
var_name[index_no]
"""

# s = "Welcome"
# x = s[4]
# print(x)

# s = "Welcome"
# print(s[4])


# l = [78, 21.58, "Hello", [1, 2, 3, 4]]
# print(l[3])



# l1 = [78, 21.58, "Hello", [1, 2, 3, 4]]
# print(l1)
# l1[3] = "Welcome"
# print(l1)


# s = "Welcome"
# print(s)
# s[2] = 'L'
# print(s)

# s = "Welcome to cetpa"
# print(s[15])
# print(s[-1])
# print(s[-2])
# print(s[-3])


# l1 = [78, 21.58, "Hello", [1, 2, 3, 4]]
# print(l1[2])
# print(l1[2][1])

"""
In Java

char c = 'R'
char[] ca = "Welcome"
"""



"""
Strings in python: 
A string is a datatype in python which can store a collection of characters in it

The strings in python are of two different types:
1. Single-Lined Strings:
These are the strings which start and end in the same line.
They can be created in 4 different ways:
    
    a. By using single quotes ('')
    b. By using double quotes ("")
    c. By using triple single quotes ('''''')
    d. By using triple double quotes ("""""")


2. Multi-Lined Strings
These are the strings which start in one line but end in some other line.
They can be created in two ways:

        a. By using triple single quotes ('''''')
        b. By using triple double quotes ("""""")
"""

# s1 = 'Hello, Welcome to Python Class'
#
# s2 = "Hello, Welcome to Python Class"
#
# s3 = '''Hello, Welcome to Python Class'''
#
# s4 = """Hello, Welcome to Python Class"""
#
# s5 = '''Hello, Welcome to CETPA
# You are in python class'''
#
# s6 = """Hello, Welcome to CETPA
# You are in python class"""


"""
Comments in python: These are the lines in our program which we do not want to execute with the 
rest of the program
They may contain some information in them

How do we create comments?
There are two ways of creating a comment in python:

1. Official Method: You have to provide # symbol before each and every line that you want to 
comment

Shortcut in pycharm: ctrl+/

2. Unofficial method: Write the lines of code that you want to comment inside a string and 
do not assign a variable to that string
"""

"""
Note: While studying any function, we should always know 3 things about it:
1. How is that function called?
2. What type of and how many arguments does that function take?
3. What does the function return?

Q. What is a function?
A. A function is a pre-defined or user-defined set of code which is used to perform a 
specific task repeatedly

As we discussed above, a function performs some operation, so it must need some data on
which that operation has to be performed, that data is provided inside the () of the function
when it is called.
This data is called the argument of a function

A function can have multiple arguments based on the type of operation that it has to perform

After the operation on the input values has been performed, the function then returns a 
result value



print() function
The print() function prints the value of all the arguments that we provide it with

Q1. How is the print function called?
A. By using the 'print' keyword and provide () after it

Q2. How many and what kind of arguments does it take?
A. It can take any number of arguments of any type.
It can take variables, values, conditions, loops, classes, function, etc..

Q3. What does the print function return?
A. It returns the values of all the arguments that we have provided it

Syntax of print function:

print(Comma separated arguments)
"""

a = 5
b = 79.65
c = "Welcome"

print(a,b,c,87,34.58,"Hello",a == b,range(10),len(c),type(a))

"""
Q1. We provided commas between the arguments of print function, but, they were removed and 
spaces were printed between the values> Can I remove the spaces and provide something 
else there?

Q2. After the last argument is printed, the program went into a new line. How do I prevent the 
program from going into a new line?

Q3. Can I print the values vertically?

5
79.65
Welcome 
.
.
.
.
"""



# def add(no1, no2):          # function to add two numbers together
#     res = no1 + no2
#     return res
#
# n1 = 5
# n2 = 7
# sum = add(n1, n2)
# print(sum)












