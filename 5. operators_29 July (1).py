"""Operators"""

"""
Q. What are operators?
A. Operators are some special symbols in any programming language using which we can perform 
different operations

Based on the different types of operations that can be performed using operators, they are 
divided into many different categories.

Those categories are:

1. Arithmetic Operators
2. Conditional Operators
3. Assignment Operators
4. Logical Operators
5. Bitwise Operators
6. Identity Operators
7. Membership Operators


1. Arithmetic Operators: They Perform arithmetic operations
They are:

+   :   Addition
-   :   Subtraction
*   :   Multiplication
/   :   Division
//  :   Floor Division  :   It divides 2 numbers and returns the int number immediately 
                            before the result
%   :   Modulus         :   It divides 2 numbers and returns their remainder
**  :   exponent        :   It finds the power
"""


# a = -17
# b = 3
#
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)

"""
2. Conditional Operators: They check if a given condition is True or False
They are:
a. ==   :   Equals to operator
b. >    :   Greater Than
c. <    :   Less Than
d. >=   :   Greater Than or Equals to
e. <=   :   Less Than or Equals to
"""


# a = 17
# b = 15
# c = 32
#
#
# print(a == b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(c >= b)
# print(b >= c)
# print(a <= c)


"""
3. Assignment Operators: They are used to assign values to variables.
Using these we can assign the value present at right hand side into the variable present at the 
left hand side
They are:

a. =    : Assignment Operator
b. +=   : 
c. -=
d. *=
e. /=
f. //=
g. %=
h. **=

"""

# a = 11
# b = 2
#
# print(a)
# a+=b            # a = a + b
# print(a)
#
# a-=b            # a = a - b

"""
4. Logical Operators: These are the operators which check multiple conditions at a time
and return a boolean value accordingly.
They are:

a.  and :   It checks two conditions simultaneously and returns True if both of them are True
            otherwise it returns False
b.  or  :   It checks two conditions simultaneously and returns True even if one of them is 
            True and returns False only if both are False
c.  not :   it reverses the boolean result that it gets from a single condition
"""

# a = 15
# b = 13
# c = 7
# d = 15
#
# print(a == b and b == d)        # False and False ==> False
# print(a > c and b > d)          # True and False ===> False
# print(b >= c and d == a)        # True and True ====> True
#
# print(a == b or b == d)        # False or False ==> False
# print(a > c or b > d)          # True or False ===> True
# print(b >= c or d == a)        # True or True ====> True
#
#
# print(not(a == b or b == d))        # not(False or False) ==> not(False) ==> True
# print(not(a > c or b > d))          # not(True or False) ===> not(True) ===> False
# print(not(b >= c or d == a))        # not(True or True) ====> not(True) ===> False



"""
5. Bitwise Operator: They work on the bits of the byte code of a value. They are of 3 types

&   :   bitwise AND
|   :   bitwise OR
~   :   bitwise NOT
>>  :   bitwise shift right
<<  :   bitwise shift left
"""
# 1 ===> 00000001
# 2 ===> 00000010
# 3 ===> 00000011
# 5 ===> 00000101
# 7 ===> 00000111


# a = 7       # 00000111
# b = 2       # 00000010
#
# # print(a&b)  # 00000010
# # print(a|b)   # 00000111
# # print(~a)   # 11111000
#
# # print(a << b)   # |00000111 00<---2 places ===> 00|00011100 ==> 00011100
# # # shift the byte code of a towards left by b places
#
#
# c = 3
# print(a >> c)           # --->000 00000111| ===> 00000000|111


# a = 45
# b = a
# c = 45
#
# print(id(a))
# print(id(b))
# print(id(c))


# d = [1, 2, 4.5, "Hello"]
# e = d
# f = [1, 2, 4.5, "Hello"]
#
#
# print(id(d))
# print(id(e))
# print(id(f))

"""
Identity Operators: 
is
is not
"""

# a = 8
# b = 8
#
# print(a is b)
#
# c = 8.33
# d = 8.33
#
# print(c is d)
# print(a is c)
#
# e = [1, 2, 4.5, "Hello"]
# f = [1, 2, 4.5, "Hello"]
#
# print(e is f)

"""
7. Membership operators: These operators check if one element is a member of a given iterable 
or not

in
not in
"""

s = "Welcome"
print('e' in s)
print('elco' in s)
print('eco' in s)



