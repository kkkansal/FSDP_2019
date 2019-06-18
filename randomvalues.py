# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 03:33:17 2019

@author: kunal
"""

import numpy as np
x=np.random.randint(5,15,40)
print(x)

from scipy import stats
print("Mode value is: ", stats.mode(x)[0])