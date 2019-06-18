# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 04:36:37 2019

@author: kunal
"""

import pandas as pd
df=pd.read_csv('sealevel.csv')

list1=list(df['Year'])
list2=list(df['inches'])

import matplotlib
from matplotlib import pyplot as plt
plt.plot(list1,list2)
plt.show()
