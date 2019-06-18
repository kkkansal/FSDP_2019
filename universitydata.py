# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 04:08:58 2019

@author: kunal
"""

import pandas as pd
import csv
df=pd.read_csv('University_data.csv')

University_data = {}
with open('University_data.csv','rt') as ani:
    reader = csv.reader(ani,delimiter = ',')
    next(reader)
    for i in reader:
        if i[0] in University_data:
            University_data[i[0]] += int(i[1])
        else:
            University_data[i[0]] = int(i[1])

a=University_data.keys()
a=list(a)

b=University_data.values()
b=list(b)

import matplotlib
#from matplotlib import pyplot as plt

import matplotlib.pyplot as plt

explode = (0, 0, 0, 0, 0.1)

colors = ['red', 'blue', 'green', 'black', 'yellow']

plt.pie(b,labels=a,colors=colors,autopct='%1.1f%%')
plt.show()