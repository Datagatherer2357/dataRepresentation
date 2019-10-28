# Gareth Duffy g00364693
# Lab05.2: Flask: intro to web server
# Q 1-8
#!flask/bin/python
import flask
from flask import Flask

# Server will fire up
# Serve static pages:
app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__' :
    app.run(debug= True)