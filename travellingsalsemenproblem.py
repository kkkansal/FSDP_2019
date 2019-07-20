# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 00:02:33 2019

@author: kunal
"""

import mlrose 
import numpy as np        

coords_list = [(3,3), (1,1), (1,5), (3,2)]          #coordinates

problem_no_fit = mlrose.TSPOpt(length = 4, coords = coords_list,
                               maximize=False)


best_state, best_fitness = mlrose.genetic_alg(problem_no_fit, random_state = 2)        #  genetic algorithm

print('The best state found is: ', best_state)

print('The fitness at the best state is: ', best_fitness)

