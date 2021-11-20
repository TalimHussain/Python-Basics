"""LOOPS in python"""

"""
Loops: A loop is a set of code which is used repeat certain statements in the program 
till the time a condition is followed.

In python we have two types of loops:

1. while loop
2. for loop

Whenever we are executing a loop, we need to follow 3 steps:

1. declare the loop variable
2. provide the loop condition
3. increment in the loop variable

We will study while loop first:

Syntax of while loop:

declare the loop variable

while condition:
    loop body
    increment in the loop variable


Example: Write a program to print the word welcome 10 times
"""

# print("welcome")
# print("welcome")
# print("welcome")
# print("welcome")
# print("welcome")
# print("welcome")
# print("welcome")
# print("welcome")
# print("welcome")
# print("welcome")

"""
Write a program to print the word welcome 10 times using while loop
"""

# i = 0
# while i < 10:
#     print("Welcome")
#     i+=1            # i = i + 1

"""
Q. Write a program to print the table of 16
"""

# n = 16
# i = 1
# while i <= 10:
#     print(n, "x", i, "=", n*i)
#     i+=1

"""
Write a program to print the table of any input number
"""

# n = int(input("Enter a Number: "))
# i = 1
# while i <= 10:
#     print(n, "x", i, "=", n*i)
#     i+=1

"""
range class: The range class returns a collection of numbers in the given limit

Syntax of range class:

range(start = 0, stop, step = 1)

range(m)
range(m, n)
range(m, n, o)

range(10)       =====> range(start = 0, stop = 10, step = 1) ==> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
range(2, 10)    =====> range(start = 2, stop = 10, step = 1) ==> 2, 3, 4, 5, 6, 7, 8, 9
range(2, 10, 3) =====> range(start = 2, stop = 10, step = 3) ==> 2, 5, 8

"""


"""
for loop in python:
It is a special loop in python which works on iterables only. It returns the elements of the
iterables in the loop variable one by one

Syntax:

for variable in iterable:
    loop block
"""

# s = "Hello"
#
# for e in s:
#     print(e)


# l = [5, 63.87, "Welcome", [1, 2, 3, 4]]
# for e in l:
#     print(e)

"""
Write a program to print numbers from 1 to 50 using while loop
"""

# i = 1
# while i <=50:
#     print(i)
#     i+=1

# i = 1
# while i <=5:
#     print(i)
#     i+=1


"""
Write a program to print all even numbers between 0 to 50
"""

# i = 0
# while i <=50:
#     print(i)
#     i+=2


"""
Same programs using for loop

All numbers from 1 to 50:
"""



# for i in range(1, 51):
#     print(i)

"""
Even numbers from 0 to 50
"""

# for i in range(0, 51, 2):
#     print(i)


# i = 0
# while i <10:
#     print(i)
#     i+=1

# i = 0
# while i <10:
#     i += 1
#     print(i)

# i = 0
# while i <10:
#     print(i)
#     i += 3

"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

# for i in range(10):
#     i+=3
#     print(i)



"""
Q. WAP to print all the even numbers between the range provided by the user

"""


# start = int(input("Enter the lower limit: "))
# stop = int(input("Enter the upper limit: "))
#
# if start%2 == 1:
#     start+=1
#
# while start <= stop:
#     print(start)
#     start +=2


# start = int(input("Enter the lower limit: "))
# stop = int(input("Enter the upper limit: "))
#
#
#
# while start <= stop:
#     if start%2 == 0:
#         print(start)
#     start +=1





# start = int(input("Enter the lower limit: "))
# stop = int(input("Enter the upper limit: "))
#
#
# if start%2 == 1:
#     start+=1
#
# for i in range(start, stop, 2):
#     print(i)


# start = int(input("Enter the lower limit: "))
# stop = int(input("Enter the upper limit: "))
#
#
# for i in range(start, stop):
#     if i%2 == 0:
#         print(i)