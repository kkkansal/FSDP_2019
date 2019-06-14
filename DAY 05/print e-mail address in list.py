# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 23:06:10 2019

@author: kunal
"""
import re
#while True:
input1=(input("enter the e-mail address"))
  #  if not input1:
   #     break
match= re.search(r'\b[A-Z0-9+-]+@[A-Z0-9]+\.[A-Z]{1,}\b', input1,re.I)
print([match.group()])
 



























for item in l1:
    print (item)