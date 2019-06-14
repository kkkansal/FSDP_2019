# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 03:57:18 2019

@author: kunal
"""


    
    
    
dict1={}
while True:
    user_input=input("enter the values")
    if not user_input:
        break
    user_input = user_input.split(" ")
    if " ".join(user_input[:-1]) in dict1:
        dict1[' '.join(user_input[:-1])] = int(dict1[' '.join(user_input[:-1])] ) + int(user_input[-1])
    else:
        dict1[ " ".join(user_input[:-1]) ] = user_input[-1]

