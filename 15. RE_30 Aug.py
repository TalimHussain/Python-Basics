"""Regular Expressions"""

"""
Regular Expression is a small programming language which is used to find out 
patterns from strings

RE has integration with other programming languages like C, Java, Python, R, etc through 
libraries
"""

# import re
# s = """jai@gmail.com aln1234n;n himanshu123@hotmail.com shubi01@xyz.com an;kwjern k
# ankitraghav@gmail.com angelpriya@abc.com"""
# p = r'\w+@\w+[.]\w+'
# res = re.findall(p, s)
# print(res)


# import re
# s = '''Welcome to cetpa infotech pct ltd. cetpa is located in sector 2 noida. cetpa me
# mai kaam karta hu'''
# p = 'cetpa'
# res = re.findall(p, s)
# print(res)


"""
Metacharacters:

^   :   cap / hat / caret           Done
*                                   Done
+                                   Done
?                                   Done
.                                   Done
[]  :   character matcher class     Done
()  :   group measure class         Done
{}  :   quantity matcher class      Done
\                                   Done
|                                   Done
$                                   Done

In RE we have 4 types of patterns:

1. Character Matching Patterns  : Character Class, []
2. Quantity Matching Patterns   : Quantity matcher class, {}
3. Location Matching Patterns
4. Group Matching Patterns      : Group matcher class, ()
"""

"""
Character matching patterns: In these type of patterns, use use the character matcher class and
provide the required characters inside it. This class then finds out all the characters provided
to it using the ORing technique
"""

# # New Program
# import re
# s = "Welcome to python class. you are in cetpa noida"
# p = '[abmnpqr]'
# res = re.findall(p, s)
# print(res)

"""
[abcd]      :   It will search for either a or b or c or d in the given string
[a-d]       :   It will search for either a or b or c or d in the given string
[a-z]       :   It will search for all lower case characters from a to z
[A-Z]       :   It will search for all upper case characters from A to B
[a-zA-Z]    :   It will search for all english alphabets either small or capital
[0-9]       :   It will search for all digits from 0 to 9
[a-zA-Z0-9_]:   It will search for all alphanumeric characters

Note: RE considers _ as an alphanumeric character
"""

# # New Program
# import re
# s = 'Welcome to python class'
# p = '[abcd]'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'Welcome to python class'
# p = '[a-d]'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'Welcome 123 to @ python .767 class'
# p = '[a-z]'
# res = re.findall(p, s)
# print(res)


# # New Program
# import re
# s = 'Welcome 123 to @ python .767 class'
# p = '[A-Z]'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'Welcome 123 to @ python .767 class'
# p = '[a-zA-Z]'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'Welcome 123 to @ python .767 class'
# p = '[0-9]'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'Welcome 123 to @ python .767 class'
# p = '[a-zA-Z0-9_]'
# res = re.findall(p, s)
# print(res)


"""
[^abcd]      :   It will search for everything except a or b or c or d in the given string
[^a-d]       :   It will search for everything except a or b or c or d in the given string
[^a-z]       :   It will search for everything except all lower case characters from a to z
[^A-Z]       :   It will search for everything except all upper case characters from A to B
[^a-zA-Z]    :   It will search for everything except all english alphabets either small or capital
[^0-9]       :   It will search for everything except all digits from 0 to 9
[^a-zA-Z0-9_]:   It will search for everything except all alphanumeric characters
"""


# # New Program
# import re
# s = 'Welcome 123 to @ python .767 class'
# p = '[^a-zA-Z0-9_]'
# res = re.findall(p, s)
# print(res)

"""
[0-9]           :   \d
[^0-9]          :   \D
[a-zA-Z0-9_]    :   \w
[^a-zA-Z0-9_]   :   \W
.               :   Everything except new line character (\n)
\s              :   All the white spaces (spacebars, \t, \n)
\S              :   Everything except white spaces
"""

# # New Program
# import re
# s = 'Welcome 123 to @ python .767 class'
# p = r'\w'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = 'Welcome 123 to @ python .767 class'
# p = r'\W'
# res = re.findall(p, s)
# print(res)


"""
2. Quantity matching Patterns : Quantity Matcher Class {}
The quantity matcher class is always used in combination with the character matcher class.
It will find out the characters provided in the character matcher class in group of characters
provided to it

The quantity matching patterns can be used in two ways:
a. First way:

{m}     :   It will search for a patterns which contains exactly m number of characters
{m,n}   :   It will search for a pattern which contains minimum m and maximum n characters
{m,}    :   It will search for a pattern which contains minimum m characters
{,n}    :   It will search for a pattern which contains maximum n characters
"""

# # New Program
# import re
# s = "Welcome to 234 py@thon c34lass. You are ^ 456in cet8pa noida"
# p = r'[a-z]{3}'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = "Welcome to 234 py@thon c34lass. You are ^ 456in cet8pa noida"
# p = r'[a-z]{3,7}'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = "Welcome to 234 py@thon c34lass. You are ^ 456in cet8pa noida"
# p = r'[a-z]{2,}'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = "Welcome to 234 py@thon c34lass. You are ^ 456in cet8pa noida"
# p = r'[a-z]{,7}'
# res = re.findall(p, s)
# print(res)


"""
Create a pattern to find out email IDs:

1. User Name    :   Alphanumeric with min 1 character
2. @ symbol
3. Domain Name  :   Alphanumeric with min 1 character
4. . symbol
5. Website type :   Alphanumeric with min 1 character
"""


# # New Program
# import re
# s = """jai@gmail.com aln1234n;n himanshu123@hotmail.com shubi01@xyz1.com an;kwjern k
# ankitraghav@gmail.com angelpriya@abc.com varsha.gupta01@abc.in jaichitkara@abc.co.in"""
# p = r'\w{1,}@\w{1,}[.]\w{1,}'
# res = re.findall(p, s)
# print(res)


"""
2. Second Way 

*   :   It searches for a pattern with min 0 characters : {0,}
+   :   It searches for a pattern with min 1 character  : {1,}
?   :   It searches for a pattern with wither 0 or 1 characters : {0,1}

"""

# New Program
import re
s = """jai@gmail.com aln1234n;n himanshu123@hotmail.com shubi01@xyz1.com an;kwjern k
ankitraghav@gmail.com angelpriya@abc.com varsha.gupta01@abc.in jaichitkara@abc.co.in
jai.chitkara@abc.co.in"""
p = r'\w+[.]?\w*@\w+[.]\w+\.?\w*'
res = re.findall(p, s)
print(res)
