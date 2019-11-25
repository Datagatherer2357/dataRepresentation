#!flask/bin/python
from flask import Flask
from flask_cors import CORS 

# Cors: A Flask extension for handling Cross Origin Resource 
# Sharing (CORS), making cross-origin AJAX possible.


# Create the flask app:
app = Flask(__name__, static_url_path='', static_folder='.')
#app = Flask(__name__)
CORS(app)

# map the url to a function: routing/URL mapping:
@app.route('/')
def index():
    return "Hello, World!"

@app.route('/book/<int:id>')
def getBook(id): # takes in the id
    return "you want book with "+ str(id) # return the converted as string

# Try it out...type "book/1234" into browser see what it returns
if __name__ == '__main__' :
    app.run(debug= True) # run the app