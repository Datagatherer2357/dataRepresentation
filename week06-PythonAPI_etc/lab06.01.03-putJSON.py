# Gareth Duffy - g00364693
# dataRepresentation wk 6  lab 01
# Updates a car on the server by using the API


import requests
import json

dataString = {'make':'Ford','model':'Kuga'}
url = 'http://127.0.0.1:5000/cars/test'

response = requests.put(url, json=dataString)

print (response.status_code)
print (response.text)