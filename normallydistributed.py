# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 03:37:40 2019

@author: kunal
"""


import numpy as np
                           
x = np.random.normal(150, 20, 1000)

print("Mean value is: ", np.mean(x))
print("Median value is: ", np.median(x))
print("Standard Deviation is: ", np.std(x))

from scipy import stats
print("Mode value is: ", stats.mode(x)[0])
print("varience value is: ", np.var(x) )

print("Minimum value is: ", np.min(x))
print("Maximum value is: ", np.max(x))

import matplotlib.pyplot as plt
plt.hist(x, 100)
plt.show()

