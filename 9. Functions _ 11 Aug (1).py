"""Functions in Python"""

"""
Functions are in any programming language a set of code which is used to perform 
a specific task at regular intervals without the need to write the code again and again

Q. Why functions or what are the uses of functions?
1. Functions are the basic building blocks of modular approach of programming
2. They help to make the code scalable
3. Functions are the building blocks of layered approach of programming
4. They help us to decrease the length of code by increasing its reusability.
"""

# print("This is python class")

# import test
# n1 = 5
# n2 = 7
# sum = test.add(n1, n2)
# print(sum)




# n1 = 8
# n2 = 4
# res = float(n1) + float(n2)
# print(res)
#
# m = 9
# n = 15
# s = float(m) + float(n)
# print(s)
#
# x = 45
# y = 15
#
#
# a = 87
# b = 35
# sum = float(a) + float(b)
# print(sum)

"""
Syntax to create a function:

def functionName(arguments):
    function block
    return output


    
Note1: The return statement is sometimes not used in some functions

Note2: The value returned by the function will come back at the place from where the function 
was called. And from there, we can save it in a variable or do anything else with it that we 
like
"""

# def add(no1, no2):              # formal parameters / formal arguments
#     res = float(no1) + float(no2)
#     return res
#
#
# n1 = 8
# n2 = 4
# sum = add(n1, n2)             # no1 = n1, no2 = n2
# print(sum)
#
# m = 9
# n = 15
# s = add(m, n)                   # actual parameters / actual arguments
# print(s)
#
# x = 45
# y = 15
# z = add(x, y)
# print(z)
#
# a = 87
# b = 35
# c = add(a, b)
# print(c)


"""
How do we call a function?

Syntax to call a function:

functionName(arguments)
"""


"""
Layered Approach of Programming:

On the very basic level, each and every professional software is divided into two parts or 
layers. They are called:

1. Presentation Layer (Front End) which interacts with the user
The presentations is having 3 uses:
    a. Taking input from the user (input function)
    b. providing output to the user (print function)
    c. Calling functions from BLL based on input provided by the user

2. Business Logic Layer (Backend) which performs all the operations of the software
It performs all the other operations of the software
"""