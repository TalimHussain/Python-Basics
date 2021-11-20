"""Strings in python"""

"""
What are strings?
A string is a datatype / class which is a collection of characters

String is a class, similarly all the datatypes are also classes. So whenever we are going to
study a data type we are going to learn about the methods of that particular class

Q. What are methods?
A. The functions inside classes are called methods. They work only on the objects of that 
particular data type / class

Q. How are methods of a class accessed?
A. obj_name.method_name(arguments)
"""

# # New Program
# s = "Welcome to python class"
# res = s.upper()
# print(res)


# # New Program
# s = "WELCOME TO PYTHON CLASS"
# res = s.lower()
# print(res)


# # New Program
# s = "WELCOME TO PYTHON CLASS"
# res = s.title()
# print(res)

# # New Program
# s = "WelcoME tO PYthon ClAsS"
# res = s.swapcase()
# print(res)

# # New Porgram
# s = "Hello, Welcome to python Class"
# res = s.index('e')
# print(res)

# # New Porgram
# s = "Hello, Welcome to python Class"
# res = s.rindex('e')
# print(res)


# # New Porgram
# s = "Hello, Welcome to python Class"
# res = s.index('elc')
# print(res)


# # New Program
# s = "Welcome to python class"
# res = s.count('e')
# print(res)

# # New Porgram
# s = "Hello, Welcome to python Class"
# res = s.find('e')
# print(res)


# # New Porgram
# s = "Hello, Welcome to python Class"
# res = s.find('e', 5, 10)
# print(res)

# # New Porgram
# s = "Hello, Welcome to python Class"
# res = s.rfind('e', 5, 20)
# print(res)


# # New Porgram
# s = "Hello, Welcome to python Class"
# res = s.replace(" ", '**')
# print(res)

# # New Porgram
# s = "Hello, Wel.come .to pyt.hon Cla.ss"
# res = s.split(".", maxsplit=2)
# print(res)

# # New Porgram
# s = "Hello, Wel.come .to pyt.hon Cla.ss"
# res = s.rsplit(".", maxsplit=2)
# print(res)


# # New Program
# l = ["Hello", "Welcome", "to", "Python", "Class"]
# res = " ".join(l)
# print(res)

# # New Porgram
# s = "   Hello, Welcome to python Class      "
# print(s)
# res = s.strip()
# print(res)


# # New Porgram
# s = "abcbcaabccbabaHello, Welcome to python Classabcbcabcabcbcabc"
# print(s)
# res = s.strip('abc')
# print(res)


# # New Program
# s = "Welco\tme to pyth\ton class"
# print(s)
# res = s.expandtabs(10)
# print(res)


# # New Porgram
# s = "Hello, Welcome to python Class"
# res = s.startswith("H")
# print(res)


# # New Porgram
# s = "Hello, Welcome to python Class"
# res = s.endswith("abc")
# print(res)

# # New Program
# s = "123456"
# res = s.isdecimal()
# print(res)

"""
Q1. Write a program to take age as an input from the user. The entered 
age should be between 10 to 100 years

Q2. Write a program to take valid mobile number as an input from the user 
"""

# while True:
#     mob = input("Enter valid mobile number: ")
#
#     if mob.isdecimal() == True:
#         if len(mob) == 10:
#             print("Valid mobile Number")
#             break
#         else:
#             print("Enter 10 digit mobile number")
#
#     else:
#         print("Enter digits only")


# while True:
#     age = input("Please enter your age between 10 to 100 years: ")
#
#     if age.isdecimal() == True:
#         if int(age) >= 10 and int(age) <= 100:
#             print("Valid Age")
#             break
#         else:
#             print("Enter age between 10 to 100 years only")
#
#     else:
#         print("Enter digits only")


# # New Program
# s = "WelcOme TO python class"
# res = s.casefold()
# print(res)

# # New Program
# s = "WelcOmeTOpythonclass"
# res = s.isalpha()
# print(res)

# # New Program
# s = "WelcOme123TOpyt546honclass"
# res = s.isalnum()
# print(res)

"""
isdecimal(): It will check for numbers only

isdigit(): It will check for numbers as well as superscripts and subscripts also

isnumeric(): It will check for numbers, superscripts, subscripts and also for special characters
like roman numbers and fractions
"""


# # New Program
# s = "hello"
# res = s.zfill(10)
# print(res)


name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Your name is name and your age is age")
print("Your name is", name, "and your age is", age)
print(f"Your name is {name} and your age is {age}")
print("Your name is {} and your age is {}".format(name, age))
print("Your name is %s and your age is %d"%(name, age))
print("Your name is {n} and your age is {a}".format(a = age, n = name))