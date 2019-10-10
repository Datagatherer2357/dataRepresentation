# Gareth Duffy g00364693 Data Representation week 3

# 1,2
import requests 
from bs4 import BeautifulSoup 
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html") 
print (page) 
print("-------------------") 
print (page.content) 
soup1 = BeautifulSoup(page.content, 'html.parser') 
print("-------------------") 
print (soup1.prettify())


# 3
with open("../carviewer2.html") as fp:     
	soup = BeautifulSoup(fp,'html.parser') 
print (soup.prettify())

print("-----------------------------------")

print(soup.tr)