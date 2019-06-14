# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 04:42:43 2019

@author: kunal
"""


names=['marry','Isla','sam']
names2 = list(map(hash,names))
print(names2)







#Code Challenge
 # Filename: 
  #  map2.py
  #problem Statement:

      names = ['Mary', 'Isla', 'Sam']

    for i in range(len(names)):
        names[i] = hash(names[i])

    print (names)