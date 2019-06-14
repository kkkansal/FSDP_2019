# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 04:29:09 2019

@author: kunal
"""

import pymongo

client = pymongo.MongoClient("mongodb+srv://kunal:kk04091999%40@cluster0-nl5xh.mongodb.net/test?retryWrites=true&w=majority")
db = client.db_university

def add_student(name,age,branch,roll_no):
    db.student.insert_one(
            {
            "name":name,
            "age":age,
            "branch":branch,
            "roll_no":roll_no
            })
    return "student added successfully"

add_student('kunal', 19, 'computer',01)
add_student('akshay', 19, 'computer',02)
add_student ('nakul', 19, 'computer',03)
add_student ('prijiwal', 19, 'computer',04)
add_student ('yash', 19, 'computer',05)
add_student ('asd', 19, 'computer',06)
add_student ('dfg', 19, 'computer',07)
add_student ('tyu', 19, 'computer',08)
add_student ('ert', 19, 'computer',09)
add_student ('qwe', 19, 'computer',10)

def fetch_all_student():
    user=db>student.find()
    for i in user:
        print(i)
        
fetch_all_student()