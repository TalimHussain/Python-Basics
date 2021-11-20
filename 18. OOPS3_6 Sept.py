"""OOPS Continued"""

"""
We discussed in the first class of OOPS, that there are some properties like Abstraction,
Encapsulation, Inheritance and Polymorphism which can only be used if we follow OOPS way os 
programming


Abstraction: Hiding information

Encapsulation: It means enclosing something inside a capsule. In encapsulation we enclose
the whole class inside an object

Inheritance: It is a property of OOPS using which one class can use the methods and the 
variables of another class.
Here we generally have 2 classes called the parent class (super class) and the child class.
The child class can use the properties of the parent class if it does not have them itself.

Inheritance is of 6 different types:

1. Single Level Inheritance
2. Multi Level Inheritance
3. Hierarchical Inheritance
4. Multiple Inheritance
5. Hybrid Inheritance
    a. Hybrid Inheritance 1
    b. Hybrid Inheritance 2



Q. How does one class inherit another class?
"""

# class C1:
#     # def __init__(self):
#     #     self.a = 1
#     #     self.b = 2
#
#     def showData(self):
#         print("This is class C1")
#
# class C2(C1):
#
#     def showData(self):
#         print("This is class C2")
#
#
# ob = C2()
# ob.showData()
# # print(ob.a, ob.b)


"""
There is a pre-defined class called the 'object class', which is the parent class of all the 
other pre-defined as well as user-defined classes by default
"""

"Single Level Inheritance"
# class C1:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     def showData(self):
#         print("This is class C1")
#
# class C2(C1):
#
#     def __init__(self):
#         self.c = 3
#         self.d = 4
#         super().__init__()
#
#     def showData(self):
#         print("This is class C2")
#
#
# ob = C2()
# ob.showData()
# print(ob.a, ob.b, ob.c, ob.d)


"Multi Level Inheritance"

# class C1:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     def showData(self):
#         print("This is class C1")
#
# class C2(C1):
#     def __init__(self):
#         self.c = 3
#         self.d = 4
#         super().__init__()
#
#     # def showData(self):
#     #     print("This is class C2")
#
# class C3(C2):
#     def __init__(self):
#         self.e = 5
#         self.f = 6
#         super().__init__()
#
#     # def showData(self):
#     #     print("This is class C3")
#
# ob = C3()
# ob.showData()
# print(ob.a, ob.b, ob.c, ob.d, ob.e, ob.f)


"Hierarchical Inheritance"

# class C1:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     def showData(self):
#         print("This is class C1")
#
# class C2(C1):
#     def __init__(self):
#         self.c = 3
#         self.d = 4
#         super().__init__()
#
#     def showData(self):
#         print("This is class C2")
#
# class C3(C1):
#     def __init__(self):
#         self.e = 5
#         self.f = 6
#         super().__init__()
#
#     def showData(self):
#         print("This is class C3")
#
# class C4(C1):
#     def __init__(self):
#         self.g = 7
#         self.h = 8
#         super().__init__()
#
#     def showData(self):
#         print("This is class C4")
#
# ob = C4()
# ob.showData()
# print(ob.a, ob.b, ob.g, ob.h)

"""Multiple Inheritance"""

# class C1:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     # def showData(self):
#     #     print("This is class C1")
#
# class C2:
#     def __init__(self):
#         self.c = 3
#         self.d = 4
#
#
#     # def showData(self):
#     #     print("This is class C2")
#
# class C3:
#     def __init__(self):
#         self.e = 5
#         self.f = 6
#
#
#     def showData(self):
#         print("This is class C3")
#
# class C4(C1, C2, C3):
#     def __init__(self):
#         self.g = 7
#         self.h = 8
#         super().__init__()
#         C2.__init__(self)
#         C3.__init__(self)
#
#     # def showData(self):
#     #     print("This is class C4")
#
# ob = C4()
# ob.showData()
# print(C4.__mro__)
# print(ob.a, ob.b, ob.c, ob.d, ob.e, ob.f, ob.g, ob.h)


"""
Method Resolution Order: Python provides priorities to the parent classes using a technique
called MRO. These priorities can be checked using the pre-defined __mro__ variable
"""

"Hybrid Inheritance 1"

# class C1:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     def showData(self):
#         print("This is class C1")
#
# class C2(C1):
#     def __init__(self):
#         self.c = 3
#         self.d = 4
#         super().__init__()
#
#
#     def showData(self):
#         print("This is class C2")
#
# class C3(C1):
#     def __init__(self):
#         self.e = 5
#         self.f = 6
#         super().__init__()
#
#
#     def showData(self):
#         print("This is class C3")
#
# class C4(C2, C3):
#     def __init__(self):
#         self.g = 7
#         self.h = 8
#         super().__init__()
#         C3.__init__(self)
#
#     def showData(self):
#         print("This is class C4")
#
# ob = C4()
# ob.showData()
# print(C4.__mro__)
# print(ob.a, ob.b, ob.c, ob.d, ob.e, ob.f, ob.g, ob.h)


"Hybrid Inheritance 2"

# class C1:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     def showData(self):
#         print("This is class C1")
#
# class C2(C1):
#     def __init__(self):
#         self.c = 3
#         self.d = 4
#         super().__init__()
#
#
#     def showData(self):
#         print("This is class C2")
#
# class C3:
#     def __init__(self):
#         self.e = 5
#         self.f = 6
#
#     def showData(self):
#         print("This is class C3")
#
# class C4(C2, C3):
#     def __init__(self):
#         self.g = 7
#         self.h = 8
#         super().__init__()
#         C3.__init__(self)
#
#     def showData(self):
#         print("This is class C4")
#
# ob = C4()
# ob.showData()
# print(C4.__mro__)
# print(ob.a, ob.b, ob.c, ob.d, ob.e, ob.f, ob.g, ob.h)

"""
Polymorphism: It is a property of OOPS which comes into play when we have 2 or more methods
with the same name either in the same class or in parent and child class

Polymorphism is of two types:

1. Compile Time Polymorphism: It does not exist in python

2. Run Time Polymorphism:
    a. Method Overloading: Method Overloading occurs when we have 2 or more methods with the
    same name in the same class. This does not exist in python
    
    b. Method Overriding: This occurs when we have 2 methods with the same name, one is in 
    parent class and the other is in  the child class.
    In case, that method is present in the child class then it will be called from there only
    and if that method is not present in child class, then it will be called from the 
    parent class
"""


# class C1:
#
#     def showData(self):
#         print("We are in class C1")
#
#     def showData(self):
#         print("Welcome to python class")
#
# ob = C1()
# ob.showData()


class C1:
    def showData(self):
        print("This is class C1")

class C2(C1):
    def showData(self):
        print("This is class C2")

ob = C2()
ob.showData()
C1.showData(ob)




"""
MultiThreading
File Handling
JSON and Pickling
Delegation
GUI Programming
Iterators and Generators
"""








