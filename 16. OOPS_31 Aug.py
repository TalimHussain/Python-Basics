"""Object Oriented Programming Systems - OOPS"""

"""
Q. What is OOPS?
A. Till now, we were following procedural way of programming, but now we are going to learn OOPS
way of programming in which we work with classes and objects

Q. What is a class?
1. A class is a collection of attributes, i.e, methods and variables
2. It is the blue print of an object
3. It is a data type either user defined or pre defined


Q .What is an object?
1. It is a real time entity
2. It is an instance of a class


Q. Why OOPS or why class and object?
1. Real world problems can be mapped very easily using OOPS
2. The code developed using OOPS is better scalable
3. OOPS provides with a lot different techniques like abstraction, encapsulation, inheritance
and polymorphism


A class is a combination of variables and methods
There are two types of variables and two types of methods inside a class

Types of methods:
1. Instance methods
2. Static methods

Types of variables:
1. Instance variables / object variables
2. Static variables / class variables / shared variables


Instance variables and instance methods can be accessed using only the object of the class

The static variables and static methods can be accessed using class name as well as object, but 
it is preferred to access them using class name only

Syntax to create a class:

class ClassName:
    methods and variables
    
Syntax to create an object:
obj_name = ClassName()

"""


# class C1:
#     pass
#
# obj = C1()
# print(type(obj))

"""
We discussed that there are methods and variables inside a class
There are instance methods and static methods, similarly, there are instance variables and 
static variables

First of all, we are going to discuss about instance methods and instance variables only.
Static methods and static variables will be discussed later on

Whenever we create methods inside a class, by default, the methods are instance methods only
and as we discussed, the instance methods are accessed using objects

Q. How to access instance methods?
A. The syntax to access instance methods is:

obj_name.method_name(arguments)

            OR
            
ClassName.methodName(obj_name, arguments)

"""

# class C1:
#
#     def method1(self, b, c):      # self = obj
#         print(self, b, c)
#
#
# obj = C1()
# print(obj)
# print()
# obj.method1(2, 3)

"""
Here, we can see that, when we call method1 with the help of object obj, 
then the object itself was saved in the first argument 'a' and the other 2 values were 
saved in b and c

Q. Why is this happening?
A. This is happening because the instance methods are created in such a way, that whenever they 
are called, the object itself, with the help of which the method is called, is saved in the first 
argument always.

Q. Why is the object saved in the first argument of the instance methods?
"""

# l1 = [1, 2, 3, 4]
#
# l2 = [9, 8, 7, 6]
#
# list.append(l1, 5)
#
# print(l1)
# print(l2)
#
# l1.append(5)


"""
Outside the class, object is referred by the name that we have provided
and inside the class, it is referred by self


Syntax to create instance variables

We have two different ways to create the instance variables of a class:

1. Inside the class

self.var_name = value


2. Outside the class:       (Python specific)

obj_name.var_name = value
"""

# class C1:
#
#     def method1(self):
#         self.b = 2
#         self.c = 3
#         print(self.a, self.b, self.c)
#
# ob = C1()
# ob.a = 1
# ob.method1()
# print(ob.a, ob.b, ob.c)

# # BLL
# class C1:                                   # Line 1
#
#     def method1(self):                      # Line 2, Line 6: self = ob
#         self.b = 2                          # Line 7
#         self.c = 3                          # Line 8
#         print(self.a, self.b, self.c)       # Line 9
#
#
# # PL
# ob = C1()                                   # Line 3
# ob.a = 1                                    # Line 4
# ob.method1()                                # Line 5
# print(ob.a, ob.b, ob.c)                     # Line 10


# # New Program
# class C1:
#
#     def method1(self):
#         self.b = 2
#         self.c = 3
#
# ob = C1()
# ob.a = 1
# print(ob.a, ob.b, ob.c)

"""
Constructor: The constructor of a class is a special method present inside that class, which 
helps the program to create an object of the class. The constructor is called automatically
as soon as the statement to create the object of the class is executed

In python the constructor method is given a special name, i.e., __init__

This method is present inside each and every class and is called automatically when the 
object is created
"""

# class C1:
#
#     def __init__(self):
#         print("Constructor is called")
#
# ob = C1()


# New Program
class C1:

    def __init__(self):
        self.b = 2
        self.c = 3

    def showData(self):
        print(self.a, self.b, self.c)

ob = C1()
ob.a = 1
ob.showData()











