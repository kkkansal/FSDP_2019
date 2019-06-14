# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 03:58:28 2019

@author: kunal
"""


import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Udaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


response = requests.get(url)
response.content
jsondata = response.json()
print (type(jsondata))
print ("temperature")
print(jsondata["main"]["temp"])
print("coordinates")
print(jsondata["coord"])
print("wind speed")
print(jsondata["wind"])
print("wind speed")
print(jsondata["wind"]['speed'])
print("sunrise")
print(jsondata["sys"]['sunrise'])
print("sunset")
print(jsondata["sys"]['sunset'])