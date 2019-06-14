# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 22:59:49 2019

@author: kunal
"""

import re
input1=(input("enter the e-mail address"))
re1 = re.search(r'\b[A-Z0-9+-]+@[A-Z0-9]+\.[A-Z]{1,}\b', input1,re.I)
#print(re1)
if re1:
    print("true")
else:
    print("false")