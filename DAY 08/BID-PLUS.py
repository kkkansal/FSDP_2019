# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 04:21:09 2019

@author: kunal
"""

import pandas as pd
from  selenium import webdriver
url = "https://bidplus.gem.gov.in/bidlists"
driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
for i in range(1,11):
    r1=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text
    A.append(r1)
    r2=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text
    B.append(r2)
    r3=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/strong').text
    C.append(r3)
    r4=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[1]/strong').text
    D.append(r4)
    r5=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[:11]
    E.append(r5)
    r6=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[12:]
    F.append(r6)
    r7=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[:11]
    G.append(r7)
    r8=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[12:]
    H.append(r8)

from collections import OrderedDict

col_name = ["Sq","er","ty","ui","op","gh","fd","ds"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F,G,H]))

df = pd.DataFrame(col_data) 
df.to_csv("bid_plus.csv")

df1=pd.read_csv("bid_plus.csv")

