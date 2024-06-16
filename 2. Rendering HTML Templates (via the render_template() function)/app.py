"""
This is a boilerplate for a simple web application in Flask that returns
an HTML file as a template with render_template()

It is recommended to create a virtual environment whenever working
with a flask application. To do so run in the console: 
    
    'python3 -m venv venv'
    'venv\Scripts\activate' (if in windows)

Make sure to first install Flask in the console with:
    
    'pip install Flask'

To run the application, run in the console within the file's directory:

    'flask run --debug'
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
