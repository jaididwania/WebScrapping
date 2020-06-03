# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:52:20 2020

@author: HP-intel
"""   

   
import requests
import re
import time
from bs4 import BeautifulSoup
def cv():
    url="https://www.worldometers.info/coronavirus/country/india/"
    page = requests.get(url)
    
    page=page.text
    soup = BeautifulSoup(page, "html.parser" )
    l1=[]
    b = soup.findAll("h1")
    for i in b:
        y=i.text
        res1 = "".join(re.split("[^a-zA-Z]*", y))
        l1.append(res1)
    
    d={}
    
    c =soup.findAll("div", {"class":"maincounter-number"})
    j=1
    for i in c:
        
        x=i.text
        res = str(re.sub("\D", "", x))
        d[l1[j]]=res
        j+=1
    
    print("\n\n",l1[0]," Stats")    
    for x, y in d.items():
      print(x,":", y)
      
      
    url2="https://www.worldometers.info/coronavirus/"
    page2 = requests.get(url2)
    
    page2=page2.text
    
    
    soup2 = BeautifulSoup(page2, "html.parser" )
    c2 =soup2.findAll("div", {"class":"maincounter-number"})
    d={}
    
    j=1
    for i in c2:
        
        x=i.text
        res = str(re.sub("\D", "", x))
        d[l1[j]]=res
        j+=1  
    
    print("\n\nWorld Stats")
    for x, y in d.items():
      print(x,":", y)

for i in range(0,3,1):
    cv()
    time.sleep(120)
     

    
    
    