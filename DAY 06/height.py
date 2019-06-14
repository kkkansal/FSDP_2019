# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 05:36:00 2019

@author: kunal
"""


people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]

person = list(map(lambda j : j['height'], filter(lambda i : 'height' in i,people)))

from functools import reduce
sum1 = reduce(lambda x,y : x+y,person)

if sum1 > 0:
    avg = sum1/len(person)
    print (avg)