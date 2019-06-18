# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 03:56:52 2019

@author: kunal
"""

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
print (incomes)

import numpy as np
print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))
print("Standard Deviation is: ", np.std(incomes))

import matplotlib.pyplot as plt
plt.hist(incomes, 50)
plt.show()
incomes=np.append(incomes,[10000000000000])

plt.boxplot(incomes)