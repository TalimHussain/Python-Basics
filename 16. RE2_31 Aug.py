"""Regular Expressions Contd."""

"""
The reason to find out patters from the strings is that RE helps us to perform web scrapping

Q. What is web scrapping?
A. It is a technique using which we can download complete web pages and extract 
useful information from it

"""
# import re
# import urllib.request as rqst
# web = rqst.urlopen("https://www.nistinstitute.com/contact_us.php")
# data = web.read()
# print(type(data))
# data = str(data)
# print(type(data))
# p_mob = r'\d{10}'
# mob = re.findall(p_mob, data)
# print(mob)
# print(len(mob))
# mob = set(mob)
# print(mob)
# print(len(mob))
#
# p_email = r"\w+[.]?\w*@\w+[.]\w+\.?\w*"
# email = re.findall(p_email, data)
#
# print(email)
# print(len(email))
#
# email = set(email)
# print(email)
# print(len(email))

"""
3. Location Matching Patterns: They are used to find out a pattern at a given location

^   : It is used for finding out patterns at the beginning of the string
$   : It is used for finding out patterns at the end of the string

"""

# # New Program
# import re
# s = "Welcome to cetpa. You are in cetpa noida. cetpa provides training in python"
# p = '^cetpa'
# res = re.findall(p, s)
# print(res)


# # New Program
# import re
# s = "Welcome 4546 to cet3132 pa. You are in cetpa6+56132513 noida. cetpa provides tr56431aining in python531"
# p = r'^[0-9]{3}'
# res = re.findall(p, s)
# print(res)


# # New Program
# import re
# s = "Welcome 4546 to cet3132 pa. You are in cetpa6+56132513 noida. cetpa provides tr56431aining in python531"
# p = r'[0-9]{3}$'
# res = re.findall(p, s)
# print(res)


# # New Program
# import re
# s = "kuldeep pratibha sumit kuldeep varsha vivek sumit kuldeep"
# p = r'^kuldeep'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = "kuldeep pratibha sumit kuldeep varsha vivek sumit kuldeep"
# p = r'kuldeep$'
# res = re.findall(p, s)
# print(res)

# # New Program
# import re
# s = "kuldeep pratibha sumit kuldeep varsha vivek sumit kuldeep"
# p = r'^kuldeep$'
# res = re.findall(p, s)
# print(res)


# # New Program
# import re
# s = "kuldeep"
# p = r'^kuldeep$'
# res = re.findall(p, s)
# print(res)


import re
import urllib.request as rqst
web = rqst.urlopen("https://www.nistinstitute.com/contact_us.php")
data = web.read()
print(type(data))
data = str(data)
print(type(data))
p_cont = r'\d{10}|\w+[.]?\w*@\w+[.]\w+\.?\w*'
cont = re.findall(p_cont, data)
cont = set(cont)
print(cont)

"""
4. Group Matching Patterns: Group Matcher Class ()
"""

# # New Program
# import re
# s = "1234_ 567_ 23_ 7890_"
# p = r'(\d{2})_'
# res = re.findall(p, s)
# print(res)






