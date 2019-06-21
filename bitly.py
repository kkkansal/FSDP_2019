# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 04:37:50 2019

@author: kunal
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
import matplotlib.pyplot as plt


data = []
with open('usagov_bitly_data.json', 'r') as f:
    for var in f.readlines():
        data.append(json.loads(var))


df = pd.DataFrame(data)

df1 = df.replace((np.nan, ' '), ('missing values', 'unkonwn'), regex=True)
#df1 = df.replace(' ', 'unknown ' , regex=True)
time_zone = (df.loc[:,'tz']).value_counts()
top = time_zone[:10]
print(top)

label = ['america/new york', 'A/los angles', 'A/chicago', 'Europe/london', 'Europe/chopenhagen', 'Asia/tokyo', 'Europe/Amsterdam', 'Europe/berlin',
         'Africa/johannesburg']
no_of_time_zones = [112, 43, 35, 34, 26, 15, 14, 11,10]
index = np.arange(len(label))
plt.bar(index, no_of_time_zones)
plt.xticks(index, label, fontsize=5, rotation=30)
plt.show()