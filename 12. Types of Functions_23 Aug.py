"""Types of Functions"""

"""
Functions are a user defined or pre-defined set of code which performs a specific task

When we use a function, then to perform the assigned task the function needs some input data
That input data is provided in the form of arguments

There are two types of arguments:
1. Formal Arguments 
2. Actual Arguments
"""

# def add(no1, no2):          # no1, no2 are formal arguments
#     res = no1 + no2
#     return res
#
# n1 = 87
# n2 = 65
# sum = add(n1, n2)           # n1, n2 are actual arguments
# print(sum)


"""
While calling a function the formal arguments save the values of actual arguments in them
formal = actual
"""
"""
Q. What are the different types of functions?
A. There are 5 or 6 different types of functions. They are:

1. Required argument function
2. Keyword argument functions
3. Default argument functions
4. Variable length argument functions
5. Variable length keyword argument functions 
6. lambda functions

Some people do not consider lambda functions as a type of functions


1. Required Argument Functions: While calling the function, we have to provide as many actual
arguments as there are the formal arguments, and they have to be provided in the same order.
All the functions that we have done till now are required argument functions only

2. Keyword Argument Functions: Here also, while calling these functions we have to provide as 
many actual arguments as there are formal arguments, but they can be provided in a 
different order
"""

# def add(no1, no2):
#     res = no1 + no2
#     return res
#
# n1 = 56
# n2 = 21
# sum = add(no2 = n2, no1 = n1)
# print(sum)


"""
3. Default Argument Functions: In default argument functions, the formal arguments are provided
some default values. If the user provides some values to those arguments, them the user is given
priority and his / her values are saved in those arguments, otherwise the default values are 
considered.
In this case, the number of actual arguments are not necessarily equal to the number of formal 
arguments. They can be less also
"""


# def add(no1 = 1, no2 = 1):
#     res = no1 + no2
#     return res
#
# n1 = 56
# n2 = 21
# sum = add(no2 = n2)
# print(sum)




"""
4. Variable length argument functions (tuple based): Here we can provide as many actual arguments
as we want
"""

# def func1(*t):
#     print(t)
#
#
# n1, n2, n3, n4, n5 = 1, 2, 3, 4, 5
#
# func1(n1, n2, n3)
# func1()
# func1(n2, n3, n4, n5)
# func1(n1, n2, n3, n4, n5)

"""
python and developer community prefers to call the argument of variable length argument 
functions as 'args'
"""

# def add(*args):
#     res = 0
#     for no in args:
#         res+=no
#     return res
#
# n1, n2, n3, n4, n5 = 1, 2, 3, 4, 5
# sum1 = add(n1, n2)
# sum2 = add(n1, n2, n3)
# sum3 = add(n1, n4)
# sum4 = add(n2, n3, n4, n5)
# sum5 = add(n1, n2, n3, n4, n5)
#
#
# print(sum1)
# print(sum2)
# print(sum3)
# print(sum4)
# print(sum5)


"""
5. Variable Length keyword argument functions: Here we can provide as many keyword arguments 
as we want while calling the functions.
They are dictionary based
"""

# def func1(**d):
#     print(d)
#
#
# func1(no1 = 1, no2 = 5, no3 = 11)
# func1(x = "Hello", y = "Welcome", z = 54.68, a = 21, b = 78)

"""
It is suggested that the argument should be named 'kwargs'
"""

# def add(**kwargs):
#     res = 0
#     for no in kwargs.values():
#         res+=no
#
#     return res
#
# sum1 = add(no1 = 5, no2 = 7)
# sum2 = add(n1 = 11, n2 = 12, n3 = 13, n4 = 14)
# sum3 = add(a = 1, b = 3, c = 5, d = 7, e = 9)
#
# print(sum1)
# print(sum2)
# print(sum3)

"""
6. lambda functions: These are single lined functions which return the value of the 
expression provided in them

Syntax to create lambda functions:

lambda arguments: expression

"""
x = lambda no1, no2: no1 + no2

y = lambda no1, no2: no1 - no2

print(x(3, 4))
print(y(11, 4))

