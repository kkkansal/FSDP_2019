# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 03:20:38 2019

@author: kunal
"""

x=[ 13, 18, 13, 14, 13, 16, 14, 21, 13]

import numpy as np

print("Mean value is: ", np.mean(x))
print("Median value is: ", np.median(x))
print("Standard Deviation is: ", np.std(x))

from scipy import stats
print("Mode value is: ", stats.mode(x)[0])
 

print("Minimum value is: ", np.min(x))
print("Maximum value is: ", np.max(x))
