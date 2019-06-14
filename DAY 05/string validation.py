# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 22:35:20 2019

@author: kunal
"""

import re
str1=(input("enter the string"))
re1=re.match(r'[+-.]?\d+\.\d{1,}',str1)
if re1:
    print("true")
else:
    print("false")
    
    
    
    
    re.I