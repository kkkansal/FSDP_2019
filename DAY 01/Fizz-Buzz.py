# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 00:18:14 2019

@author: kunal
"""


for i in range(1,50):
    
    if i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print (i)