
# what is Database ??

"""

- A database is an organized collection of structured information, or data,
typically stored electronically in a computer system. A database is usually controlled
by a database management system (DBMS). Together, the data and the DBMS, along with
the applications that are associated with them, are referred to as a database system,
often shortened to just database.

Data within the most common types of databases in operation today is typically
modeled in rows and columns in a series of tables to make processing and data querying
efficient. The data can then be easily accessed, managed, modified, updated, controlled,
and organized. Most databases use structured query language (SQL) for writing and querying data.

"""

# What is Structured Query Language (SQL)?
"""

- SQL is a programming language used by nearly all relational databases to query,
manipulate, and define data, and to provide access control. SQL was first developed
at IBM in the 1970s with Oracle as a major contributor, which led to implementation
of the SQL ANSI standard, SQL has spurred many extensions from companies such as IBM,
Oracle, and Microsoft. Although SQL is still widely used today, new programming languages
are beginning to appear.

"""


import sqlite3

conn = sqlite3.connect("testing.db")

sql_qry = """CREATE TABLE users(
        first_name TEXT,
        last_name TEXT,
        age INTEGER
        )"""



cur = conn.cursor()
cur.execute(sql_qry)
conn.commit()

conn.close()


# five types of datatypes
# NULL - nothing
# INTEGER - 1,23
# REAL - decimal 3.14
# TEXT - string
# BLOB - images files


# inserting data
# you can use execute() or executemany() based on requirement


conn = sqlite3.connect("testing.db")
cur = conn.cursor()

# 1 : execute :
cur.execute(" INSERT INTO users VALUES ('techie','programmer',20)")

# 2 : executemany()
multiList = [("jhon","rock",18),('william',"jones",20),("raj","bakshi",21)]
sql_qry =  "INSERT INTO users VALUES (?,?,?)"
cur.executemany(sql_qry,multiList)

conn.commit()

#fetching

# fetchone() - fetches one record
# fetchmany(n) - is the number of record
# fetchall() - fetches all the records

sql_qry =  " SELECT * FROM users "
variable = cur.executemany(sql_qry).fetchall() # fetchone() , fetchmany(n)

# variable holds the return data


# primary id
# primary id is the unique number that is assigned to a entry
# we can fetch it by
sql_qry =  " SELECT rowid,* FROM users "
# rowid holds the primary key of the entry

# WHERE clause
# it is used for conditional selection
sql_qry =  " SELECT rowid,* FROM users WHERE first_name = 'techie' "

# order by
# just orders in ASC or DESC order 
sql_qry =  " SELECT rowid,* FROM users order by rowid ASC "

# and/or 
# we can use it as                                                  or
sql_qry =  " SELECT rowid,* FROM users WHERE first_name = 'techie' and rowid = 1"

# like 
# like is used for pharsing 
sql_qry =  " SELECT rowid,* FROM users WHERE first_name LIKE 'te%' "

# limiting 
# it helps you to limit your results 
sql_qry =  " SELECT rowid,* FROM users LIMIT 2 "

# updating the record 
sql_qry =  " UPDATE users SET age = 21 WHERE first_name = 'techie' "

# deleting the record 
sql_qry =  " DELETE FROM users WHERE first_name = 'raj' "

# droping the table 
sql_qry =  " DROP TABLE users "

# Note :
# - make sure you use conn.commit() on every action you perform
# -- create
# -- update
# -- delete
# -- you can read data without commiting 

# i hope you enjoyed this 
# the code for the app is also given in the same dir make sure you check out 

# username : nilesh 
# password : nilesh 

# so see you in the next video :)


conn.close()


























