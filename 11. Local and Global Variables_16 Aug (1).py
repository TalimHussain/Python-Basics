"Local and Global Variables"

# # New Program
# def func1():            # Line 1, Line 3
#     x = 5               # Line 4
#     print(x)            # Line 5
#     print(id(x))        # Line 6
#
# func1()                 # Line 2
# print(x)                # Line 7
# print(id(x))            # Line 8


# # New Program
# def func1():            # Line 1: func1 is created; Line 4
#     x = 5               # Line 5: Local var x is created
#     print(x)            # Line 6: Local var x is accessed
#     print(id(x))        # Line 7: Address of local var x is printed
#
#
# x = 11                  # Line 2: global var x is created
# func1()                 # Line 3: func1 is called
# print(x)                # Line 8: Global var x is accessed
# print(id(x))            # Line 9: Address of global var x is printed

"""
Output:
Choice 1:

5
address of 5

11 
address of 11


"""

# # New Program
# def func1():            # Line 1: func1 is created; Line 4
#     global x            # Line 5: Inside the function it has to access global var x only
#     x = 5               # Line 6: Global var x is updated
#     print(x)            # Line 7:
#     print(id(x))        # Line 8:
#
#
# x = 11                  # Line 2: global var x is created
# func1()                 # Line 3: func1 is called
# print(x)                # Line 9: Global var x is accessed
# print(id(x))            # Line 10: Address of global var x is printed



# # New Program
# def func1():        # Line 1, Line 3
#     global x        # Line 4
#     x = 5           # Line 5
#     print(x)        # Line 6
#     print(id(x))    # Line 7
#
# func1()             # Line 2
# x = 11              # Line 8
# print(x)            # Line 9
# print(id(x))        # Line 10





