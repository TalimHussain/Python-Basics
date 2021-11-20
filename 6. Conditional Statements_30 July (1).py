"""Conditional Statements"""

"""
Q. What are Conditional Statements?
A. The statements which check a given condition in the program and then execute the further 
statements based on the output of that condition

We provide conditional statements in python using if-elif-else keywords
So we are going to study these keywords one by one

if keyword:

Syntax:

if (condition):
    if-block

        OR
if condition:
    if-block

Note: The 'if block' is the block of code that is to be executed in case the condition provided
comes out to be True
Example:

Write a program to tell if the given input number is even
"""

# num = int(input("Enter a number: "))
#
# if num%2 == 0:
#     print("The number is even")
#
# print("Program terminated")

"""
else keyword:

Syntax:
else:
    else-block
    
The else block is always provided after providing atleast one if block. It is executed in case
condition provided in the if block comes out to be False and t he if-block is not executed

From here we can understand that if we have provided both if and else statements, then only 
one of them is going to be executed by the program

Example:
"""

# num = int(input("Enter a number: "))
#
# if num%2 == 0:
#     print("The number is even")
#
# else:
#      print("The number is odd")
#
# print("program terminated")


"""
elif statement:

Syntax:

elif condition:
    elif block
    
The elif block is used in case there are multiple conditions that need to be checked and the 
program has to be executed accordingly

Note: the elif block is also provided after atleast 1 if block. We can use as many elif blocks 
as we want after an if block.

Note: In case we are using elif blocks, then the else block is provided after all the 
elif blocks have been provided. Also, we can only use a single else block in the end

Example
"""

# num = int(input("Enter any number from 1 to 6: "))
#
# if num == 1:
#     print("Move 1 step forward")
#
# elif num == 2:
#     print("Move 2 steps forward")
#
# elif num == 3:
#     print("Move 3 steps forward")
#
# elif num == 4:
#     print("Move 4 steps forward")
#
# elif num == 5:
#     print("Move 5 steps forward")
#
# elif num == 6:
#     print("Move 6 steps forward")
#
# else:
#     print("Incorrect choice")
#
# print("Program Terminated")


"""
Q. Write a program to determine the greatest of two input numbers

"""

# n1 = int(input("Enter First Number: "))
# n2 = int(input("Enter Second Number: "))
#
# if n1 > n2:
#     print("First Number is greater")
#
# else:
#     print("Second Number is greater")

"""
Write a program to determine the greatest of 3 input numbers
"""

# n1 = int(input("Enter First Number: "))
# n2 = int(input("Enter Second Number: "))
# n3 = int(input("Enter Third Number: "))
#
# if n1 > n2:
#     if n1 > n3:
#         print("n1 is the greatest")
#     else:
#         print("n3 is greatest")
# else:
#     if n2 > n3:
#         print("n2 is greatest")
#     else:
#         print("n3 is greatest")


# n1 = int(input("Enter First Number: "))
# n2 = int(input("Enter Second Number: "))
# n3 = int(input("Enter Third Number: "))
#
# if n1 > n2 and n1 > n3:
#     print("n1 is the greatest")
#
# elif n2 > n1 and n2 > n3:
#     print("n2 is greatest")
#
# elif n3 > n1 and n3 > n2:
#     print("n3 is greatest")


"""
Types of statements in python:
There are 3 types of statements in python. They are:

1. Normal statements: These are the statements which are written outside any condition, loop,
function, class or method etc and at 0 indentation.

2. Headings: The statements in which we define a condition, loop, function, class or method etc
are called headings. They are also written at 0 indentation

3. Suites: These are the statements which are written inside headings. They are written atleast 
at 1 indentation
"""

n1 = int(input("Enter First Number: "))     # Normal Statement
n2 = int(input("Enter Second Number: "))    # Normal Statement

if n1 >= n2:                                 # Heading

    print("First Number is greater")        # Suite

else:                                       # Heading
    print("Second Number is greater")       # Suite


"""
Write a program to determine if a given input number is prime or composite
"""




