# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 23:56:50 2019

@author: kunal
"""
s1=input("Enter a String:")
s2=""
for i in s1:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        pass
    else:
        s2+=i
s1=s2
print(s1)
