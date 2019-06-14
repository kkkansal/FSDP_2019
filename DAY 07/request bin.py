# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 04:48:02 2019

@author: kunal
"""


import json
import requests

Host = "https://en4kq54q8lo24.x.pipedream.net"

data = {"firstname":"dev","language":"English", "POST":"H.R"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )