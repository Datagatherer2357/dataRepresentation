# Gareth Duffy g00364693 Data Representation week 3

# 4-7
import requests 
from bs4 import BeautifulSoup 

with open("../carviewer2.html") as fp:     
	soup = BeautifulSoup(fp,'html.parser') 

# print(soup.tr)

rows = soup.findAll("tr") 
for row in rows:      
#	print("------")      
#	print(row)
	
	cols = row.findAll("td")      
#	for col in cols:          
#		print(col.text) 
	
	dataList = []     
	for col in cols:         
		dataList.append(col.text)     
	print (dataList)