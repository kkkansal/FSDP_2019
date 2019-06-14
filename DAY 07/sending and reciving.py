# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 05:00:06 2019

@author: kunal
"""



import json
import requests

Host = "https://enhsng3agcf38.x.pipedream.net"
data = {"firstname":"akshay","hindi":"English", "POST":"H.R","collage":"Arya collage"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )






def get_method():
    response = requests.get("http://httpbin.org/get?firstname=akshay&hindi=English&post=H.R&collage=arya collage")
    return response

print (get_method().text)