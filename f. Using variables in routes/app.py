"""
This is a boilerplate for using variables in routes
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World'

# A route with a string variable
@app.route('/content/<string>')
def content(string):
    return f'This is page for content: {string}'

# A route with an integer variable
@app.route('/page/<int:page_num>')
def page(page_num):
    return f'This is page #{page_num}'

if __name__ == '__main__':
    app.run()
