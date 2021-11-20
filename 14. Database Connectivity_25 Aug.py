"""Database Connectivity"""

"""
127.0.0.1 or localhost

Credentials: user name and password that you have provided while installing the DB

MySQL Database Server

Q. What is the difference between a database and a database server?
A. A Database Server is a collection of many databases
A Database is a collection of tables
A Table is a collection of rows and columns in which data is saved`


Types of databases:
1. Relational Databases: Here the data is stored in tabular format in rows and columns of a 
table. These are also called SQL Databases
Examples:
MySQL Server
Oracle DB
MS Access
MS SQL Server
PostGre / PostGre S / PostGre SQL


2. Non-Relational Databases: Here the data is not stored in tabular format, rather it is stored
in the form of keys and values. They are also called non-SQL Databases

Examples:
Mongo DB
HBase



MySQL Server: 
SQL : Structured Query Language


We will be learning CRUD Queries
C: Create
R: Read
U: Update
D: Delete
"""

"""
Requirements to connect python to DB Server:
1. IP Address (Mandatory)
2. Credentials (Mandatory)
3. DB Name (Optional)
4. Port Number (Optional)
"""

# import pymysql
# con = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'root123',
#                       database = 'pythondb')
# cur = con.cursor()
# print(type(con))
# print(type(cur))
# con.close()


# import pymysql
# con = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'root123',
#                       database = 'pythondb')
# cur = con.cursor()
# qry = "select * from students"
# cur.execute(qry)
# data = cur.fetchall()
# print(data)
# con.close()


# import pymysql
# con = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'root123',
#                       database = 'pythondb')
# cur = con.cursor()
# qry = "select * from students"
# cur.execute(qry)
# data = cur.fetchall()
#
# for id, name, age in data:
#     print(id, name, age)
#
# con.close()



# import pymysql
# con = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'root123')
# cur = con.cursor()
#
# cur.execute("use pythondb")
# qry = "insert into students values(8, 'Sharad', 47)"
# cur.execute(qry)
# con.commit()
# con.close()


# import pymysql
# con = pymysql.connect(host = '127.0.0.1', user = 'root', password = 'root123')
# cur = con.cursor()
#
# cur.execute("use pythondb")
# # cur.execute("create table Mirzapur(id int, name varchar(30), age int)")
#
# cur.execute("select * from students")
# data = cur.fetchall()
#
# f = open(r"C:\Users\cipl\PycharmProjects\21 July Batch\mirzapurData.csv", 'w')
# f.write("ID,Name,Age\n")
# for id, name, age in data:
#     # cur.execute(f"insert into Mirzapur values({id}, '{name}', {age})")
#     f.write(f"{id},{name},{age}\n")
#
# f.close()
#
#
# con.commit()
# con.close()









