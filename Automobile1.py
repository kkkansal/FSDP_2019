# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 03:14:14 2019

@author: kunal
"""

import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_csv("Automobile.csv")
all = (data1.loc[:,'make']).value_counts()
top = all[:10]
labels = ('toyota', 'nissan', 'mazda', 'honda', 'mitsubishi', 'subru', 'volkswagan', 'volvo', 'peugot', 'dodge')
explode = (0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0) 
plt.pie(top, explode=explode,labels=labels, autopct='%.0f%%')
plt.show()








