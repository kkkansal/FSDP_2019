# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 04:11:45 2019

@author: kunal
"""

from bs4 import BeautifulSoup 
import requests
wiki="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
source=requests.get(wiki).text
soup=BeautifulSoup(source,"lxml")
print(soup.prettify())
right_table=soup.find('table',class_='wikitable')
print(right_table.prettify())
tab_bod=right_table.find('tbody')
A=[]
B=[]
C=[]
for row in tab_bod.findAll('tr'):
    cells=row.findAll('td')
    if len(cells)==7:
       B.append(cells[1].text.strip())
       C.append(cells[4].text.strip())
import matplotlib
from matplotlib import pyplot as plt
plt.pie(C,labels=B,wedgeprops={'edgecolor':'black'})
plt.axis('equal')
plt.show()