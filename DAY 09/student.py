# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 03:08:54 2019

@author: kunal
"""

import sqlite3
from pandas import DataFrame
conn = sqlite3.connect ( 'db_university.db' )

c = conn.cursor()
c.execute ("""CREATE TABLE student(
          name TEXT,
          age INTEGER,
          branch TEXT,
          roll_no INTEGER
          )""")


c.execute("INSERT INTO student VALUES ('kunal', 19, 'computer',01)")
c.execute("INSERT INTO student VALUES ('akshay', 19, 'computer',02)")
c.execute("INSERT INTO student VALUES ('nakul', 19, 'computer',03)")
c.execute("INSERT INTO student VALUES ('prijiwal', 19, 'computer',04)")
c.execute("INSERT INTO student VALUES ('yash', 19, 'computer',05)")
c.execute("INSERT INTO student VALUES ('asd', 19, 'computer',06)")
c.execute("INSERT INTO student VALUES ('dfg', 19, 'computer',07)")
c.execute("INSERT INTO student VALUES ('tyu', 19, 'computer',08)")
c.execute("INSERT INTO student VALUES ('ert', 19, 'computer',09)")
c.execute("INSERT INTO student VALUES ('qwe', 19, 'computer',10)")
c.execute("SELECT * FROM student")
print ( c.fetchall() )
c.execute("SELECT * FROM student")

df = DataFrame(c.fetchall())  
df.columns = ["name","age","branch","roll_no"]
conn.commit()
conn.close()