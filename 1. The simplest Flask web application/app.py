"""
This is a boilerplate for the simplest web application in Flask

It is recomended to create a virtual environment whenever working
with a flask application. To do so run in the console: 
    
    'python3 -m venv venv'

Make sure to first install Flask in the console with:
    
    'pip install Flask'

To run the application, run in the console within the file's directory:
    
    'flask run --debug'

"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World'

if __name__ == '__main__':
    app.run
