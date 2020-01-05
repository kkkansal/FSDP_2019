# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 17:27:04 2020

@author: kunal
"""
#to find out division
a=int(input("enter the mark"))
c=int(input("enter the mark"))
b=int(input("enter the mark"))
total=a+b+c
per=(total/300)*100
print(per)
if(per>=60):
    print("first division")
elif(per>=50):
    print("second division")
elif(per>=33):
    print("third division")
else:
    print("fail")
    
a=int(input("enter the age"))
if(a>=18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")