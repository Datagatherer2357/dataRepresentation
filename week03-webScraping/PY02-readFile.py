# Gareth Duffy g00364693 Data Representation week 3

# 2

from bs4 import BeautifulSoup

with open("../carviewer2.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

print (soup.prettify())