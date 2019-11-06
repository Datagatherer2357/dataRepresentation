# Gareth Duffy - g00364693
# dataRepresentation wk 6  lab 01
# Deletes a car on the server by using the API

import requests

url = 'http://127.0.0.1:5000/cars/08%20C%201234'
response = requests.delete(url)
print (response.status_code)
print (response.text)