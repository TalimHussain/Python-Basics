"""print function contd and input function"""

"""
Before answering the 3 questions that we left yesterday, we have have to understand one more topic
first

Escape Characters:
These are some special characters in any programming language, which when printed do not 
appear on the screen, rather we can se their effect

Two most common escape characters are:
\n  :   New Line Character. This character takes the program into a new line from the point
where it is present

\t  :   Tab Character. This character provides a space of 1 tab  wherever it is present

"""

# s = "Welco\tme to pyth\ton \nclass"
# print(s)

"""
A more advanced syntax of the print function

print(comma separated arguments, sep = " ", end = "\n")

sep : This argument is printed after each and every argument provided to the print function is
printed

end : After the last argument is printed, the end argument is then printed on the screen in place
of the sep argument

sep and end are both default arguments. There is a property of default arguments, that is
If we do not provide any value to the default arguments, then they take their default values 
only and in case we provide them with a value, then they give us priority and then our values
are considered
"""

# a = 5
# b = 79.65
# c = "Welcome"
#
# print(a,b,c,87,34.58,"Hello",a == b,range(10),len(c),type(a), sep = '\n', end = '')
#
# a, b, c, d, e = 2, 3, 4, 5, 6
# # print()
"""
Output:

2#3%4&^5*6:

Input:
"""

# print(a, b, sep = '#', end = '%')
# print(c, d, sep = '&^', end ='*')
# print(e, end = ':')
# print()


"""
Output:

2@

3#4^

5!*6Hello

"""
# print(a,end ='@')
# print()
# print()
# print(b,c,sep='#',end='^')
# print()
# print()
# print(d,c,sep='!*',end='Hello')


"""
input() function: It takes an input from the user and saves the input value in a variable
which is then used by the program

Q1. How is the input function called?
A. By writing the input keyword followed by ()

Q2. What type of and how many arguments does the print function take?
A. It takes a single string type argument

Q3. What does the function return?
A. It returns the value provided by the user in str format

Syntax:

var_name = input(string)

Q. Write a program to add two input numbers provided by the user
"""

# n1 = input("Enter First Number: ")
# n2 = input("Enter Second Number: ")
# sum = n1 + n2
# print(sum)


# str1 = 'ABCD'
# str2 = 'EFGH'
# print(str1 + str2)

"""
Type Casting: Converting one data type into another data type is called type casting

Syntax of Type casting:

var_name = target_Class(data_source)

"""

# n1 = int(input("Enter First Number: "))
# n2 = int(input("Enter Second Number: "))
# print(type(n1))
# print(type(n2))
# sum = n1 + n2
# print(sum)


n1 = input("Enter First Number: ")
n2 = input("Enter Second Number: ")
print(type(n1))
print(type(n2))
n1 = int(n1)
n2 = int(n2)
print(type(n1))
print(type(n2))
sum = n1 + n2
print(sum)
