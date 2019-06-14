# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 04:13:50 2019

@author: kunal
"""

file=open('absentee.txt', mode = 'wt')
while True:
    user_input = input("enter the value you want to insert")
    file.write(user_input)
    if not user_input:
        break
file.close()
file=open('absentee.txt',mode='rt')
kunal=file.read()
print(kunal).split(' ')
file.close()