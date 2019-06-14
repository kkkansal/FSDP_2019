# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 00:07:05 2019

@author: kunal
"""


A1 = int(input("Enter marks 1:-"))
A2 = int(input("Enter marks 2:-"))
A3 = int(input("Enter marks 3:-"))
E1 = int(input("Enter marks 1:-"))
E2 = int(input("Enter marks 2:-"))
weighted_score = ( A1 + A2 + A3 ) * 0.1 + (E1 + E2 ) *  0.35
print("Weighted Score is " + str(weighted_score))
 