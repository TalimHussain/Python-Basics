"""Exception Handling"""

# def div(no1, no2):
#     res = no1 / no2
#     return res
#
# n1 = int(input("Enter First Number: "))
# n2 = int(input("Enter Second Number: "))
#
# quo = div(n1, n2)
# print(quo)

"""
Exception Handling is the technique using which we handle the errors in our programs, i.e.,
we do not let our programs terminate after they encounter an error

There are a lot of pre-defined error classes in python. For Example;
1. ValueError
2. ZeroDivisionError
3. IndentationError
4. ModuleNotFoundError
5. FileNotFoundError
6. Exception
.
.
.
.
.
There are 100+ error classes in python.

Q. How are errors handled in python?
A. Errors can be handled using 2 different techniques:
    
    1. Manual Checking: In this we need to carefully write the program and provide input values
    
    2. Using pre-defined techniques: Here, some pre-defined keywords are used. This is actually
    exception handling. In python, we have 4 keywords defined for exception handling. They
    are: try, except, finally, raise.
    It is generally preferred to put the code inside at least 1 layer of try and except while
    writing the program


Syntax of try and except:

try:
    try-block of code
    
except:
    except-block of code
"""

# try:
#     n1 = int(input("Enter First Number: "))
#     n2 = int(input("Enter Second Number: "))
#     quo = n1 / n2
#     print(quo)
#
# except:
#     print("Error in the program")
#
#
# print("Program finished")


# try:
#     n1 = int(input("Enter First Number: "))
#     n2 = int(input("Enter Second Number: "))
#     quo = n1 / n2
#     print(quo)
#
# except Exception as err:
#     print("Error!!", err)
#
#
# print("Program finished")

# while True:
#     try:
#         n1 = int(input("Enter First Number: "))
#         n2 = int(input("Enter Second Number: "))
#         quo = n1 / n2
#         print(quo)
#         break
#
#     except ValueError:
#         print("Enter digits only")
#
#     except ZeroDivisionError:
#         print("Second number should not be zero")
#
#     except Exception as err:
#         print("Error!!", err)
#
#
# print("Program finished")



"""
finally: The statements which are written inside the finally block are executed under all
conditions.
"""

# while True:
#     try:
#         n1 = int(input("Enter First Number: "))
#         n2 = int(input("Enter Second Number: "))
#         quo = n1 / n2
#         print(quo)
#
#
#     except ValueError:
#         print("Enter digits only")
#
#     except ZeroDivisionError:
#         print("Second number should not be zero")
#
#     except Exception as err:
#         print("Error!!", err)
#
#     finally:
#         chYN = input("Do you wish to perform a calculation again, Y/N: ")
#         if chYN == 'N' or chYN == 'n':
#             print("Program terminated")
#             break


"""
raise keyword: The raise keyword is used to raise exceptions in the program
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
#     try:
#         cal = Calculator()
#         cal.no1 = int(input("Enter First Number: "))
#         cal.no2 = int(input("Enter Second Number: "))
#
#         choice = input("""
#         Press + for addition
#         Press - for Subtraction
#         Press * for Multiplication
#         Press / for Division
#
#         Enter Your Choice: """)
#
#         if choice == '+':
#             cal.add()
#             print("The sum of numbers is:", cal.res)
#
#         elif choice == '-':
#             cal.sub()
#             print("The difference of numbers is:", cal.res)
#
#         elif choice == '*':
#             cal.mul()
#             print("The product of numbers is:", cal.res)
#
#         elif choice == '/':
#             cal.div()
#             print("The quotient is:", cal.res)
#
#         else:
#             raise NotImplementedError
#
#     except ValueError:
#         print("Enter Digits only")
#
#     except ZeroDivisionError:
#         print("Seconf number should not be zero")
#
#     except NotImplementedError:
#         print("Incorrect Choice")
#
#     except Exception as err:
#         print("Error!!", err)
#
#     finally:
#         chYN = input("Do you want to perform another calculation, Y/N: ")
#         if chYN == 'N' or chYN == 'n':
#             break
# # PL Ends Here


# l = [1, 2, 3, 4]
# e = l[8]
# print(e)

# s = "Welcome"
# e = s[15]
# print(e)


# BLL Starts Here

class Calculator:

    def __init__(self):
        self.no1 = 0
        self.no2 = 0
        self.res = 0

    def add(self):
        self.res = self.no1 + self.no2

    def sub(self):
        self.res = self.no1 - self.no2

    def mul(self):
        self.res = self.no1 * self.no2

    def div(self):
        self.res = self.no1 / self.no2



# BLL Ends Here

# PL Starts Here

while True:
    try:
        cal = Calculator()
        cal.no1 = int(input("Enter First Number: "))
        cal.no2 = int(input("Enter Second Number: "))

        if cal.no2 == 0:
            raise NotImplementedError("Second number should not be Zero")

        choice = input("""
        Press + for addition
        Press - for Subtraction
        Press * for Multiplication
        Press / for Division

        Enter Your Choice: """)

        if choice == '+':
            cal.add()
            print("The sum of numbers is:", cal.res)

        elif choice == '-':
            cal.sub()
            print("The difference of numbers is:", cal.res)

        elif choice == '*':
            cal.mul()
            print("The product of numbers is:", cal.res)

        elif choice == '/':
            cal.div()
            print("The quotient is:", cal.res)

        else:
            raise NotImplementedError("Incorrect Choice")

    except ValueError:
        print("Enter Digits only")

    except ZeroDivisionError:
        print("Seconf number should not be zero")

    except NotImplementedError as err:
        print(err)

    except Exception as err:
        print("Error!!", err)

    finally:
        chYN = input("Do you want to perform another calculation, Y/N: ")
        if chYN == 'N' or chYN == 'n':
            break
# PL Ends Here








