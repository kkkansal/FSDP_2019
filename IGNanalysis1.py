# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 03:14:28 2019

@author: kunal
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data2 = pd.read_csv("ign.csv")



xbox_one_filter = data2[(data2["score"] > 7) & (data2["platform"] == "Xbox One")]
xbox_one_filter.head(20)
      
data2[data2["platform"] == "Xbox One"]["score"].plot(kind="hist")
data2[data2["platform"] == "PlayStation 4"]["score"].plot(kind="hist")
xbox_one_filter["score"].hist()