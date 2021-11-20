"""Data Types"""

"""
Q. What is a data type?
A. Data Types in any programming language are a technique using which the variables / values 
are saved inside memory locations

Similar type of values are grouped inside a single data type
For example all the integer numbers are grouped as int data type
All decimal numbers are grouped as float data type, etc....

All the data types have fixed amount of memory requirements
For example in C language all the int type values required 2 bytes of memory
all float type values need 4 bytes of memory, etc....

There are a lot of different data types in python:
Some examples are:

int         :   It stores integer type values
float       :   It stores decimal values
str         :   It stores collection of characters
list        :   It stores multiple heterogeneous data types
tuple       :   It stores multiple heterogeneous data types
dictionary  :   It stores multiple heterogeneous data types but in key - value format
set         :   They store multiple unique heterogeneous values
frozen set  :   They store multiple unique heterogeneous values
NoneType    :   It stores None Values
Boolean     :   It stores boolean values (True or False)
etc.....

In python there are 50K+ (pre-defined + user defined) data types

"""

# a = 5
# b = 7.96
# c = "Welcome"
# d = [78, 21.58, "Hello", [1, 2, 3, 4]]
# e = (78, 21.58, "Hello", [1, 2, 3, 4])
# f = {'Roll Number': 1, "Name": "Aakash", 'Age': 12, "Marks": 78.6}
# g = {5, 45.689, "Hello", 5, "Welcome", "Hello", 5}
# h = None
# i = True
# j = False
#
# # print(g)
#
# print("Data type of a:", type(a))
# print("Data type of b:", type(b))
# print("Data type of c:", type(c))
# print("Data type of d:", type(d))
# print("Data type of e:", type(e))
# print("Data type of f:", type(f))
# print("Data type of g:", type(g))
# print("Data type of h:", type(h))
# print("Data type of i:", type(i))
# print("Data type of j:", type(j))


"""
The data types of python are divided into two categories: 

    1. Single valued Data types: These are the data types which store only a single value
    in them. Examples are: int, float, NoneType, bool, etc...
    
    
    2. Multi valued data types (iterables): The data types which store a collection of 
    multiple values in them. Examples are: str, list, tuple, dict, set, frozen set etc...
    
    The iterables are further divided into two categories:
        a. Mutable iterables: These are the iterables whose values at particular indexes 
        can be accessed and changed through indexing.
        Examples are: list, dictionary, set, etc...
        
        b. Immutable iterables: These are the iterables whose values at particular indexes 
        can be accessed through indexing but cannot be changed.
        Examples are: tuple, frozen set, str, etc...

Indexes:
"""


# c = "Welcome"
# d = [78, 21.58, "Hello", [1, 2, 3, 4]]
# e = (78, 21.58, "Hello", [1, 2, 3, 4])
# f = {'Roll Number': 1, "Name": "Aakash", 'Age': 12, "Marks": 78.6}
# g = {5, 45.689, "Hello", 5, "Welcome", "Hello", 5}
#
#
# print(len(c))
# print(len(d))
# print(len(e))
# print(len(f))
# print(len(g))


s = "Hello"
print(s)
s[2] = 'E'
print(s)


# l = ["Hi", 56, 54.21, "Welcome", 23]
# print(l)
# l[3] = 100
# print(l)

