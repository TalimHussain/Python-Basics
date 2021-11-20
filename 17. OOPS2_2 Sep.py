"""OOPS Contd."""

"""
Points to be remembered:
1. Identify the variables in the program
2. Identify the variables which will be used to transfer data between BLL and PL
3. Create these variables as instance variables of the class
4. Create methods for performing operations

Calculator using OOPS:
1. We shall have 4 variables here, no1, no2, res, choice
2. The variables used to transfer data would be no1, no2, res
3. no1, no2, res will be instance variables
4. The methods will be add, sub, mul, div....
"""


# # BLL Starts Here
#
# class Calculator:
#
#     def __init__(self):
#         self.no1 = 0
#         self.no2 = 0
#         self.res = 0
#
#     def add(self):
#         self.res = self.no1 + self.no2
#
#     def sub(self):
#         self.res = self.no1 - self.no2
#
#     def mul(self):
#         self.res = self.no1 * self.no2
#
#     def div(self):
#         self.res = self.no1 / self.no2
#
#
#
# # BLL Ends Here
#
# # PL Starts Here
#
# while True:
#     cal = Calculator()
#     cal.no1 = int(input("Enter First Number: "))
#     cal.no2 = int(input("Enter Second Number: "))
#
#     choice = input("""
#     Press + for addition
#     Press - for Subtraction
#     Press * for Multiplication
#     Press / for Division
#
#     Enter Your Choice: """)
#
#     if choice == '+':
#         cal.add()
#         print("The sum of numbers is:", cal.res)
#
#     elif choice == '-':
#         cal.sub()
#         print("The difference of numbers is:", cal.res)
#
#     elif choice == '*':
#         cal.mul()
#         print("The product of numbers is:", cal.res)
#
#     elif choice == '/':
#         cal.div()
#         print("The quotient is:", cal.res)
#
#     else:
#         print("Incorrect Choice")
#
#     chYN = input("Do you want to perform another calculation, Y/N: ")
#     if chYN == 'N' or chYN == 'n':
#         break
#
#
#
# # PL Ends Here


# class C1:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     def showData(self):
#         print(self.a, self.b)
#
# ob1 = C1()
# ob1.showData()
# ob2 = C1()
# ob2.showData()


# # New Program
#
# class C1:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     def showData(self):
#         print(self.a, self.b)
#
# ob1 = C1()
# ob2 = C1()
# ob1.a+=5
# ob1.b+=3
# ob1.showData()
# ob2.showData()


"""
Static methods and static variables: These are the methods and variables of class which are 
created without using objects

Static Variables: These are the variables which are created inside a class but outside any 
method of the class. They are created just like normal variables.

Syntax:

class ClassName:

    var_name = value
    
    methods
    
Note:
The static variables of a class are shared between all the objects of the class. They can be 
accessed using object names also, but it is preferable to access them using Class Name only.
"""

# class C1:
#     a = 1
#     b = 2
#
#     def __init__(self):
#         self.c = 3
#         self.d = 4
#
# ob1 = C1()
# print (ob1.a, ob1.b, ob1.c, ob1.d)
# print(C1.a, C1.b)

# # New Program
# class C1:
#     a = 1
#     b = 2
#
#     def __init__(self):
#         self.c = 3
#         self.d = 4
#
# ob1 = C1()
# ob2 = C1()
# C1.a = 7
# C1.b = 8
# ob1.c = 9
# ob1.d = 10
# print (ob1.a, ob1.b, ob1.c, ob1.d)
# print (ob2.a, ob2.b, ob2.c, ob2.d)



# # New Program
#
# class C1:
#     a = 0
#
#     def __init__(self):
#         self.x = 0
#
#     def incData(self):
#         C1.a+=1
#         self.x +=1
#         print(C1.a, self.x)
#
# ob = C1()
# ob.incData()
# ob.incData()
# ob.incData()

# # New Program
#
# class C1:
#     a = 0
#
#     def __init__(self):
#         self.x = 0
#
#     def incData(self):
#         C1.a+=1
#         self.x+=1
#         print(C1.a, self.x)
#
# ob1 = C1()
# ob1.incData()
# ob2 = C1()
# ob2.incData()
# ob3 = C1()
# ob3.incData()


"""
Static Methods
"""

# class C1:
#
#     @staticmethod
#     def method1():
#         print("This is static method of class C1")


"""
A decorator can modify the functionality / properties of a function or a method

All the methods of all the classes that we have studied till now are instance methods only
"""


# d1 = {1: 11, 2: 22, 3: 33, 4: 44}
# l = [3, 4, 5, 6]
#
# # d2 = d1.fromkeys(l)
# # print(d2)
#
# d2 = dict.fromkeys(l)
# print(d2)











