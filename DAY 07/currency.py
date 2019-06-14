# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 04:20:25 2019

@author: kunal
"""


import requests
url="https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=195b70aaa5523dc4eba6"
print (url)
response = requests.get(url)
response.content
jsondata=response.json()
print("USD to INR")
print(jsondata)
