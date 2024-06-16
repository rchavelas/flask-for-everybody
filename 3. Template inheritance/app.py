"""
This is a boilerplate for a simple web application in Flask showing how
template inheritance works
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
