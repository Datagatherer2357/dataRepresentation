# Gareth Duffy g00364693 Data Representation week 3
# 8

import requests 
from bs4 import BeautifulSoup 
import csv 
 
employee_file = open('employee_file.csv', mode='w')  
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', 
quoting=csv.QUOTE_MINIMAL) 
 
employee_writer.writerow(['John Smith', 'Accounting', 'November']) 
employee_writer.writerow(['Erica Meyers', 'IT', 'March']) 
 
employee_file.close()