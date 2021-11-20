"Functions contd"

"""
First of all we are going to create a Calculator without functions
"""
# while True:
#
#     n1 = int(input("Enter First Number: "))
#     n2 = int(input("Enter Second Number: "))
#
#     choice = input("""
#     Press + for addition
#     Press - for subtraction
#     Press * for multiplication
#     Press / for division
#     Press % for remainder
#     Press // for floor division
#     Press ** for exponent
#
#     Enter your choice: """)
#
#     if choice == '+':
#         sum = n1 + n2
#         print("The sum of numbers is:", sum)
#
#     elif choice == '-':
#         diff = n1 - n2
#         print("The difference of numbers is:", diff)
#
#     elif choice == '*':
#         prod = n1 * n2
#         print("The product of numbers is:", prod)
#
#     elif choice == '/':
#         quo = n1 / n2
#         print("The quotient is:", quo)
#
#     elif choice == '%':
#         rem = n1 % n2
#         print("The remainder is:", rem)
#
#     elif choice == '//':
#         fldiv = n1 // n2
#         print("The result of floor division is:", fldiv)
#
#     elif choice == '**':
#         pow = n1 ** n2
#         print("The exponent is:", pow)
#
#     else:
#         print("Incorrect Choice")
#
#     chYN = input("Do you want to perform another calculation, Y/N ?")
#     if chYN == 'n' or chYN == 'N':
#         print("Thanks for using our calculator")
#         break

"""
Now we are going to create a calculator using functions
"""

"""
While calling a function, formal arguments = actual arguments
"""

# # BLL Starts Here
#
# def add(no1, no2):
#     res = no1 + no2
#     return res
#
# def sub(no1, no2):
#     res = no1 - no2
#     return res
#
# def mul(no1, no2):
#     res = no1 * no2
#     return res
#
# def div(no1, no2):
#     res = no1 / no2
#     return res
#
# def remainder(no1, no2):
#     res = no1 % no2
#     return res
#
# def floorDiv(no1, no2):
#     res = no1 // no2
#     return res
#
# def exp(no1, no2):
#     res = no1 ** no2
#     return res
#
# # BLL Ends Here
#
# # PL Starts Here
# while True:
#     n1 = int(input("Enter First Number: "))
#     n2 = int(input("Enter Second Number: "))
#
#     choice = input("""
#     Press + for addition
#     Press - for subtraction
#     Press * for multiplication
#     Press / for division
#     Press % for remainder
#     Press // for floor division
#     Press ** for exponent
#
#     Enter your choice: """)
#
#     if choice == '+':
#         sum = add(n1, n2)
#         print("The sum of numbers is:", sum)
#
#     elif choice == '-':
#         diff = sub(n1, n2)
#         print("The difference of numbers is:", diff)
#
#     elif choice == '*':
#         prod = mul(n1, n2)
#         print("The product of numbers is:", prod)
#
#     elif choice == '/':
#         quo = div(n1, n2)
#         print("The quotient is:", quo)
#
#     elif choice == '%':
#         rem = remainder(n1, n2)
#         print("The remainder is:", rem)
#
#     elif choice == '//':
#         fldiv = floorDiv(n1, n2)
#         print("The result of floor division is:", fldiv)
#
#     elif choice == '**':
#         pow = exp(n1, n2)
#         print("The exponent is:", pow)
#
#     else:
#         print("Incorrect Choice")
#
#     chYN = input("Do you want to perform another calculation, Y/N ?")
#     if chYN == 'n' or chYN == 'N':
#         print("Thanks for using our calculator")
#         break



# PL Ends Here


"""
A Sample Program
"""

# def add(no1, no2):          # Line 1: Function is defined; Line 5: formal = actual
#     res = no1 + no2         # Line 6
#     return res              # Line 7
#
# n1 = 8                      # Line 2: var n1 is created
# n2 = 7                      # Line 3: var n2 is created
# sum = add(n1, n2)           # Line 4: add function is called; Line 8: sum = returned value
# print(sum)                  # Line 9

"""
Q. In this program tell me the order in which the statements are going to be executed


A1. 165, 159, 160, 166 ==> Vivek

A2. 159, 160, 161, 163, 164, 165, 166 ==> Ankit

A3. 163, 164, 165, 159, 160, 161, 165, 166 ===> Kanishka, Kuldeep, Shreya, Safaat Hussain, Vikas

A3 is 98% Correct

159, 163, 164, 165, 159, 160, 161, 165, 166

"""

"""
Local and Global Variables:

Global Variables: These are the variables which are created outside a function, method or 
a class. They can be accessed anywhere in the program

Local Variables: These are the variables which are created inside a function or a method and 
they can be accessed inside that particular function only and they do not exist outside it


Q. How are variables created in python?
A. Syntax to create a variable in python is:

var_name = value

If the variable with the provided name is not already present in the program, then a new 
variable with that name is created
But if a variable with that same name is already present, then its value is updated and 
the new value is saved in it
"""
# x = 45
# print(x)
#
# x = 23
# print(x)
"""
Let's understand with examples:
"""



# def func1():            # Line 1; Line 6
#     print(x)            # Line 7
#     print(id(x))        # Line 8
#
# x = 5                   # Line 2
# print(x)                # Line 3
# print(id(x))            # Line 4
# func1()                 # Line 5









