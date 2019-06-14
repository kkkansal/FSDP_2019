# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 04:15:01 2019

@author: kunal
"""


import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
names2 = list(map(lambda x : random.choice(code_names),names))








 import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

for i in range(len(names)):
  names[i] = random.choice(code_names)

print (names)