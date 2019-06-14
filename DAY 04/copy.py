# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 04:23:02 2019

@author: kunal
"""

file1=open('new.txt',mode='rt')
file2=open('new1.txt',mode='wt')
with open ("new.txt","rt") as file1:
    with open ("new1.txt","wt") as file2:
        for line in file1:
            file2.write(line)