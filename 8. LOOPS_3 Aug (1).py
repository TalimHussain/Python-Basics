"""Loops Contd."""

"""
ASCII Encoding

s = "Welcome to python class"


A   :   65                          a   :   97
B   :   66                          b   :   98
C   :   67                          c   :   99
.
.
.
.
Z   :   90                          z   :   122


Q. How can we determine the ASCII codes / uni codes of the characters that we are saving?
A. We have a function for this, which is called the ord() function

It is called by using its name and providing () after it ==> ord()
It takes a single string type argument which contains a single character
It returns the uni code / ASCII code of the character that we have provided it with
"""

# print(ord('A'))
# print(ord('o'))

"""
chr() function

The chr() function takes a single int type argument and returns the character which is 
represented by that int type ASCII code
"""

# char = 'a'
# code = ord(char)
# print(code)
#
# char1 = chr(code)
# print(char1)

"""
Q. Write a program to convert all the characters of an input string into upper case

Input:
Welcome to python class

output:
WELCOME TO PYTHON CLASS
"""

# np_str = input("Enter a string: ")
#
# res_str = ""
#
# i = 0
# while i < len(inp_str):
#     char = inp_str[i]
#
#     code = ord(char)
#     if code >= 97 and code <= 122:
#         code -= 32  # code = code - 32
#
#     char = chr(code)
#     res_str += char  # res_str = res_str + char
#
#     i += 1  # i = i + 1
#
# print(res_str)







# s = "Welcome"
# var = s[3]
# print(var)
#
# # print(s[3])

# s1 = "Hello"
# s2 = "Welcome"
#
# print(s1 + s2)

"""
Q. WAP to convert all characters of an input string into lower case

Input:
WELcome TO. PYthON 123 CLASS

Output:
welcome to. python 123 class

"""

inp_str = input("Enter a string")
res_str = ""

i = 0
while i < len(inp_str):
    char = inp_str[i]
    code = ord(char)

    if code >= 65 and code <=90:
        code+=32

    char = chr(code)
    res_str+=char
    i+=1

print(res_str)



"""
Write a program to convert all characters at even indexes into upper case and all 
characters at odd indexes into case

Write a program to switch the casing of characters of an input string

Write to program to convert an input string into Title case

Input:

heLLo, welCOMe TO ceTPA

Output:
Hello, Welcome To Cetpa


Write all the above 5 programs using for loop

"""









